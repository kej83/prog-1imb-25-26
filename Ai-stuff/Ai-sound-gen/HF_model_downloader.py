from huggingface_hub import HfApi, hf_hub_url, get_hf_file_metadata
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import requests
import shutil
import sys
import threading
import time
from typing import Any, Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parent
APP_DIRNAME = "ACE-Step_Premium"
MODELS_DIRNAME = "models"
APP_ROOT = REPO_ROOT if REPO_ROOT.name == APP_DIRNAME else REPO_ROOT / APP_DIRNAME
TARGET_DIR = APP_ROOT / MODELS_DIRNAME

MAIN_REPO_ID = "ACE-Step/Ace-Step1.5"
DEFAULT_DIT_MODEL = "acestep-v15-xl-sft"
DEFAULT_BASE_DIT_MODEL = "acestep-v15-xl-base"
DEFAULT_TURBO_DIT_MODEL = "acestep-v15-xl-turbo"
DEFAULT_SMALL_LM_MODEL = "acestep-5Hz-lm-0.6B"
DEFAULT_LM_MODEL = "acestep-5Hz-lm-1.7B"
DEFAULT_LARGE_LM_MODEL = "acestep-5Hz-lm-4B"
MAIN_BUNDLE_KEY = "main"
SHARED_MODEL_KEYS = (
    "vae",
    "Qwen3-Embedding-0.6B",
    DEFAULT_SMALL_LM_MODEL,
    DEFAULT_LM_MODEL,
    DEFAULT_LARGE_LM_MODEL,
)
DEFAULT_DIT_MODEL_KEYS = (
    DEFAULT_DIT_MODEL,
    DEFAULT_BASE_DIT_MODEL,
    DEFAULT_TURBO_DIT_MODEL,
)
DEFAULT_MODEL_KEYS = (
    *SHARED_MODEL_KEYS,
    *DEFAULT_DIT_MODEL_KEYS,
)

DOWNLOAD_STATUS_DOWNLOADED = "downloaded"
DOWNLOAD_STATUS_SKIPPED = "skipped"
DOWNLOAD_STATUS_FAILED = "failed"

MODEL_CODE_VARIANTS: Dict[str, str] = {
    "acestep-v15-base": "base",
    "acestep-v15-sft": "sft",
    "acestep-v15-turbo": "turbo",
    "acestep-v15-turbo-shift1": "turbo",
    "acestep-v15-turbo-shift3": "turbo",
    "acestep-v15-turbo-continuous": "turbo",
    "acestep-v15-xl-base": "xl_base",
    "acestep-v15-xl-sft": "xl_sft",
    "acestep-v15-xl-turbo": "xl_turbo",
}

MODEL_CONFIGS: Dict[str, Dict[str, Any]] = {
    "vae": {
        "repo_id": MAIN_REPO_ID,
        "subdir": "vae",
        "local_target_subdir": "vae",
        "name": "VAE",
        "description": "ACE-Step audio encoder/decoder from the shared ACE-Step 1.5 bundle",
    },
    "Qwen3-Embedding-0.6B": {
        "repo_id": MAIN_REPO_ID,
        "subdir": "Qwen3-Embedding-0.6B",
        "local_target_subdir": "Qwen3-Embedding-0.6B",
        "name": "Qwen3-Embedding-0.6B",
        "description": "Shared text embedding model used by ACE-Step 1.5",
    },
    DEFAULT_LM_MODEL: {
        "repo_id": MAIN_REPO_ID,
        "subdir": DEFAULT_LM_MODEL,
        "local_target_subdir": DEFAULT_LM_MODEL,
        "name": DEFAULT_LM_MODEL,
        "description": "Default 5Hz LM model shipped with the ACE-Step premium bundle",
    },
    DEFAULT_SMALL_LM_MODEL: {
        "repo_id": f"ACE-Step/{DEFAULT_SMALL_LM_MODEL}",
        "local_target_subdir": DEFAULT_SMALL_LM_MODEL,
        "name": DEFAULT_SMALL_LM_MODEL,
        "description": "Small 5Hz LM model bundled with every ACE-Step premium preset download",
    },
    DEFAULT_LARGE_LM_MODEL: {
        "repo_id": f"ACE-Step/{DEFAULT_LARGE_LM_MODEL}",
        "local_target_subdir": DEFAULT_LARGE_LM_MODEL,
        "name": DEFAULT_LARGE_LM_MODEL,
        "description": "Large 5Hz LM model bundled with every ACE-Step premium preset download",
    },
    DEFAULT_DIT_MODEL: {
        "repo_id": f"ACE-Step/{DEFAULT_DIT_MODEL}",
        "local_target_subdir": DEFAULT_DIT_MODEL,
        "name": DEFAULT_DIT_MODEL,
        "description": "Default premium ACE-Step 1.5 XL SFT DiT model",
    },
    DEFAULT_BASE_DIT_MODEL: {
        "repo_id": f"ACE-Step/{DEFAULT_BASE_DIT_MODEL}",
        "local_target_subdir": DEFAULT_BASE_DIT_MODEL,
        "name": DEFAULT_BASE_DIT_MODEL,
        "description": "Default premium ACE-Step 1.5 XL base DiT model",
    },
    DEFAULT_TURBO_DIT_MODEL: {
        "repo_id": f"ACE-Step/{DEFAULT_TURBO_DIT_MODEL}",
        "local_target_subdir": DEFAULT_TURBO_DIT_MODEL,
        "name": DEFAULT_TURBO_DIT_MODEL,
        "description": "Default premium ACE-Step 1.5 XL Turbo DiT model",
    },
}

DOWNLOAD_CONFIG = {
    "num_connections": 16,
    "chunk_size": 10 * 1024 * 1024,
    "max_retries": 5,
    "retry_delay": 2,
    "max_retry_delay": 30,
    "timeout": 300,
}


def _get_hf_token() -> Optional[str]:
    return (
        os.environ.get("HF_TOKEN")
        or os.environ.get("HUGGINGFACE_HUB_TOKEN")
        or os.environ.get("HUGGINGFACE_TOKEN")
    )


def _create_hf_api() -> HfApi:
    token = _get_hf_token()
    if not token:
        return HfApi()
    try:
        return HfApi(token=token)
    except TypeError:
        return HfApi()


class RobustDownloader:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=20,
            pool_maxsize=20,
            max_retries=3,
        )
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers.update(
            {
                "User-Agent": "ACE-Step-Premium-Downloader/1.0",
                "Accept-Encoding": "identity",
            }
        )
        self.hf_token = _get_hf_token()
        if self.hf_token:
            self.session.headers.update({"Authorization": f"Bearer {self.hf_token}"})

        self.sha_cache_file = REPO_ROOT / "sha256_cache.json"
        self.sha_cache = self.load_sha_cache()
        self.verified_cache_file = REPO_ROOT / "verified_files_cache.json"
        self.verified_cache = self.load_verified_cache()

        self._progress_lock = threading.Lock()
        self._active_progress = False
        self._last_progress_len = 0
        self._repo_files_meta: Dict[str, Dict[str, Dict[str, Any]]] = {}
        self._range_support_cache: Dict[str, bool] = {}

    def _hf_api(self) -> HfApi:
        return _create_hf_api()

    def _hf_file_metadata(self, url: str):
        if not self.hf_token:
            return get_hf_file_metadata(url)
        try:
            return get_hf_file_metadata(url, token=self.hf_token)
        except TypeError:
            return get_hf_file_metadata(url)

    def prefetch_repo_metadata(self, repo_id: str):
        if repo_id in self._repo_files_meta:
            return

        try:
            api = self._hf_api()
            info = api.model_info(repo_id, files_metadata=True)
            meta: Dict[str, Dict[str, Any]] = {}
            for file_info in getattr(info, "siblings", []) or []:
                rfilename = getattr(file_info, "rfilename", None)
                if not rfilename:
                    continue

                size = getattr(file_info, "size", None)
                sha256: Optional[str] = None
                lfs = getattr(file_info, "lfs", None)
                if lfs:
                    if isinstance(lfs, dict):
                        sha256 = lfs.get("sha256") or lfs.get("oid")
                        if size is None:
                            size = lfs.get("size")
                    else:
                        sha256 = getattr(lfs, "sha256", None) or getattr(lfs, "oid", None)
                        if size is None:
                            size = getattr(lfs, "size", None)

                if isinstance(size, str) and size.isdigit():
                    size = int(size)
                elif isinstance(size, float):
                    size = int(size)

                meta[rfilename] = {"size": size, "sha256": sha256}
            self._repo_files_meta[repo_id] = meta
        except Exception as exc:
            self._repo_files_meta[repo_id] = {}
            self.log(f"Warning: Could not prefetch metadata for {repo_id}: {exc}")

    def _get_prefetched_meta(self, repo_id: str, filename: str) -> Dict[str, Any]:
        if repo_id not in self._repo_files_meta:
            self.prefetch_repo_metadata(repo_id)
        return self._repo_files_meta.get(repo_id, {}).get(filename, {}) or {}

    def supports_range(self, url: str) -> bool:
        if url in self._range_support_cache:
            return self._range_support_cache[url]

        ok = False
        try:
            response = self.session.get(
                url,
                headers={"Range": "bytes=0-0", "Accept-Encoding": "identity"},
                timeout=30,
                stream=True,
                allow_redirects=True,
            )
            try:
                ok = response.status_code == 206 and bool(response.headers.get("content-range"))
            finally:
                response.close()
        except Exception:
            ok = False

        self._range_support_cache[url] = ok
        return ok

    def _get_terminal_width(self) -> int:
        try:
            return shutil.get_terminal_size(fallback=(100, 20)).columns
        except Exception:
            return 100

    def _clear_progress_line_locked(self):
        width = self._get_terminal_width()
        clear_len = max(self._last_progress_len, width)
        sys.stdout.write("\r" + " " * clear_len + "\r")
        sys.stdout.flush()
        self._last_progress_len = 0
        self._active_progress = False

    def clear_progress_line(self):
        with self._progress_lock:
            if self._active_progress:
                self._clear_progress_line_locked()

    def show_progress_line(self, text: str):
        with self._progress_lock:
            width = self._get_terminal_width()
            max_len = max(1, width - 1)
            if len(text) > max_len:
                text = text[:max_len]

            sys.stdout.write("\r" + text)
            extra_spaces = max(0, self._last_progress_len - len(text))
            if extra_spaces:
                sys.stdout.write(" " * extra_spaces)
                sys.stdout.write("\r" + text)
            sys.stdout.flush()
            self._last_progress_len = len(text)
            self._active_progress = True

    def finalize_progress_line(self, final_text: Optional[str] = None):
        with self._progress_lock:
            if final_text is not None:
                width = self._get_terminal_width()
                max_len = max(1, width - 1)
                if len(final_text) > max_len:
                    final_text = final_text[:max_len]
                sys.stdout.write("\r" + final_text)
                extra_spaces = max(0, self._last_progress_len - len(final_text))
                if extra_spaces:
                    sys.stdout.write(" " * extra_spaces)
                    sys.stdout.write("\r" + final_text)
                sys.stdout.write("\n")
                sys.stdout.flush()
            elif self._active_progress:
                sys.stdout.write("\n")
                sys.stdout.flush()

            self._last_progress_len = 0
            self._active_progress = False

    def log(self, msg: str):
        with self._progress_lock:
            if self._active_progress:
                self._clear_progress_line_locked()
            print(msg, flush=True)

    def load_sha_cache(self) -> Dict[str, str]:
        if self.sha_cache_file.exists():
            try:
                return json.loads(self.sha_cache_file.read_text(encoding="utf-8"))
            except Exception:
                return {}
        return {}

    def save_sha_cache(self):
        try:
            self.sha_cache_file.write_text(json.dumps(self.sha_cache, indent=2), encoding="utf-8")
        except Exception as exc:
            self.log(f"Warning: Could not save SHA cache: {exc}")

    def load_verified_cache(self) -> Dict[str, Dict[str, Any]]:
        if self.verified_cache_file.exists():
            try:
                return json.loads(self.verified_cache_file.read_text(encoding="utf-8"))
            except Exception:
                return {}
        return {}

    def save_verified_cache(self):
        try:
            self.verified_cache_file.write_text(
                json.dumps(self.verified_cache, indent=2),
                encoding="utf-8",
            )
        except Exception as exc:
            self.log(f"Warning: Could not save verified cache: {exc}")

    def is_file_verified(self, repo_id: str, filename: str, filepath: str, expected_sha: str) -> bool:
        if not expected_sha:
            return False

        cache_key = f"{repo_id}/{filename}"
        cached_info = self.verified_cache.get(cache_key)
        if not cached_info or not os.path.exists(filepath):
            return False

        current_size = os.path.getsize(filepath)
        current_mtime = os.path.getmtime(filepath)
        return (
            cached_info.get("sha256") == expected_sha
            and cached_info.get("size") == current_size
            and abs(cached_info.get("mtime", 0) - current_mtime) < 1.0
        )

    def mark_file_verified(self, repo_id: str, filename: str, filepath: str, sha256: str):
        if not os.path.exists(filepath):
            return

        self.verified_cache[f"{repo_id}/{filename}"] = {
            "sha256": sha256,
            "size": os.path.getsize(filepath),
            "mtime": os.path.getmtime(filepath),
            "verified_at": time.time(),
        }
        self.save_verified_cache()

    def get_file_sha256(self, repo_id: str, filename: str) -> Optional[str]:
        cache_key = f"{repo_id}/{filename}"
        cached = self.sha_cache.get(cache_key)
        if cached:
            return cached

        try:
            meta = self._get_prefetched_meta(repo_id, filename)
            sha256 = meta.get("sha256")
            if isinstance(sha256, str) and len(sha256) == 64:
                self.sha_cache[cache_key] = sha256
                self.save_sha_cache()
                return sha256

            metadata = self._hf_file_metadata(hf_hub_url(repo_id, filename))
            etag = str(getattr(metadata, "etag", "")).replace('"', "").replace("W/", "")
            if len(etag) == 64:
                self.sha_cache[cache_key] = etag
                self.save_sha_cache()
                return etag

            api = self._hf_api()
            model_info = api.model_info(repo_id, files_metadata=True)
            for file_info in getattr(model_info, "siblings", []) or []:
                if getattr(file_info, "rfilename", None) != filename:
                    continue
                lfs = getattr(file_info, "lfs", None)
                if not lfs:
                    break
                if isinstance(lfs, dict):
                    sha256 = lfs.get("sha256") or lfs.get("oid")
                else:
                    sha256 = getattr(lfs, "sha256", None) or getattr(lfs, "oid", None)
                if isinstance(sha256, str) and len(sha256) == 64:
                    self.sha_cache[cache_key] = sha256
                    self.save_sha_cache()
                    return sha256
        except Exception as exc:
            self.log(f"Warning: Could not get SHA256 for {filename}: {exc}")

        return None

    def format_bytes(self, bytes_val: float) -> str:
        if bytes_val < 0:
            return "0 B"
        for unit in ["B", "KB", "MB", "GB"]:
            if bytes_val < 1024.0:
                return f"{bytes_val:.1f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.1f} TB"

    def format_time(self, seconds: float) -> str:
        if seconds < 0:
            return "0s"
        seconds = int(seconds)
        if seconds < 60:
            return f"{seconds}s"
        if seconds < 3600:
            mins = seconds // 60
            secs = seconds % 60
            return f"{mins}m" if secs == 0 else f"{mins}m {secs}s"
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        return f"{hours}h" if mins == 0 else f"{hours}h {mins}m"

    def print_progress(
        self,
        current: int,
        total: int,
        start_time: float,
        filename: str,
        speed_bytes_per_sec: Optional[float] = None,
    ):
        if total <= 0:
            return

        elapsed = max(0.001, time.time() - start_time)
        percent = min(100.0, (current / total * 100))
        if speed_bytes_per_sec is None:
            speed_bytes_per_sec = current / elapsed if elapsed > 0 else 0.0

        if speed_bytes_per_sec > 0 and total > current:
            eta_str = self.format_time((total - current) / speed_bytes_per_sec)
        else:
            eta_str = "Complete" if current >= total else "Unknown"

        bar_length = 40
        filled = int(percent * bar_length / 100)
        bar = "=" * max(0, min(filled, bar_length)) + "-" * max(0, bar_length - filled)
        speed_str = self.format_bytes(speed_bytes_per_sec) + "/s" if speed_bytes_per_sec else "0 B/s"
        line = (
            f"{filename}: [{bar}] {percent:.1f}% "
            f"({self.format_bytes(current)}/{self.format_bytes(total)}) "
            f"{speed_str} ETA: {eta_str}"
        )
        self.show_progress_line(line)

    def get_file_url(self, repo_id: str, filename: str) -> str:
        return f"https://huggingface.co/{repo_id}/resolve/main/{filename}"

    def get_file_size(
        self,
        url: str,
        repo_id: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> Optional[int]:
        try:
            if repo_id and filename:
                meta = self._get_prefetched_meta(repo_id, filename)
                size = meta.get("size")
                if isinstance(size, int) and size >= 0:
                    return size
                if isinstance(size, str) and size.isdigit():
                    return int(size)

            if repo_id and filename:
                try:
                    metadata = self._hf_file_metadata(hf_hub_url(repo_id, filename))
                    meta_size = getattr(metadata, "size", None)
                    if isinstance(meta_size, int) and meta_size >= 0:
                        return meta_size
                    if isinstance(meta_size, str) and meta_size.isdigit():
                        return int(meta_size)
                except Exception:
                    pass

            response = self.session.head(url, timeout=30, allow_redirects=True)
            if response.status_code in (200, 206):
                content_length = response.headers.get("content-length")
                if content_length and str(content_length).isdigit():
                    return int(content_length)
                content_range = response.headers.get("content-range")
                if content_range and "/" in content_range:
                    total_size = content_range.split("/")[-1]
                    if total_size.isdigit():
                        return int(total_size)

            response = self.session.get(
                url,
                headers={"Range": "bytes=0-0", "Accept-Encoding": "identity"},
                timeout=30,
                stream=True,
                allow_redirects=True,
            )
            try:
                if response.status_code == 206:
                    content_range = response.headers.get("content-range")
                    if content_range and "/" in content_range:
                        total_size = content_range.split("/")[-1]
                        if total_size.isdigit():
                            return int(total_size)
                elif response.status_code == 200:
                    content_length = response.headers.get("content-length")
                    if content_length and str(content_length).isdigit():
                        return int(content_length)
            finally:
                response.close()
        except Exception as exc:
            self.log(f"Warning: Could not get file size: {exc}")
        return None

    def verify_file_sha256(self, filepath: str, expected_sha: str, filename: str = "") -> bool:
        if not expected_sha:
            self.log("[WARNING] No SHA256 available for verification")
            return True

        display_name = filename or os.path.basename(filepath) or filepath
        self.log(f"[VERIFYING] Computing SHA256 for {display_name}...")
        try:
            sha256_hash = hashlib.sha256()
            file_size = os.path.getsize(filepath)
            bytes_read = 0
            start_time = time.time()
            last_update = 0.0
            chunk_size = 8 * 1024 * 1024

            with open(filepath, "rb") as handle:
                while True:
                    chunk = handle.read(chunk_size)
                    if not chunk:
                        break
                    sha256_hash.update(chunk)
                    bytes_read += len(chunk)
                    now = time.time()
                    if now - last_update >= 0.2:
                        percent = (bytes_read / file_size) * 100 if file_size > 0 else 0.0
                        speed = bytes_read / max(0.001, (now - start_time))
                        line = (
                            f"[VERIFYING] {display_name}: {percent:.1f}% "
                            f"({self.format_bytes(bytes_read)}/{self.format_bytes(file_size)}) "
                            f"{self.format_bytes(speed)}/s"
                        )
                        self.show_progress_line(line)
                        last_update = now

            computed_sha = sha256_hash.hexdigest()
            if computed_sha == expected_sha:
                self.finalize_progress_line(f"[VERIFIED] SHA256 match: {computed_sha[:16]}...")
                return True

            self.finalize_progress_line("[ERROR] SHA256 mismatch!")
            self.log(f"  Expected: {expected_sha}")
            self.log(f"  Got:      {computed_sha}")
            return False
        except Exception as exc:
            self.finalize_progress_line()
            self.log(f"[ERROR] Failed to verify SHA256: {exc}")
            return False

    def download_chunk(
        self,
        url: str,
        start: int,
        end: int,
        filepath: str,
        chunk_id: int,
        progress_callback=None,
    ) -> bool:
        chunk_file = os.path.normpath(f"{filepath}.part{chunk_id}")
        chunk_size_expected = end - start + 1

        if os.path.exists(chunk_file):
            existing_size = os.path.getsize(chunk_file)
            if existing_size == chunk_size_expected:
                if progress_callback:
                    progress_callback(chunk_id, chunk_size_expected)
                return True
            if existing_size > chunk_size_expected:
                os.remove(chunk_file)
                resume_pos = 0
            else:
                resume_pos = existing_size
        else:
            resume_pos = 0

        for attempt in range(self.config["max_retries"]):
            try:
                actual_start = start + resume_pos
                response = self.session.get(
                    url,
                    headers={"Range": f"bytes={actual_start}-{end}", "Accept-Encoding": "identity"},
                    timeout=self.config["timeout"],
                    stream=True,
                    allow_redirects=True,
                )

                if response.status_code == 200:
                    raise RuntimeError("Server did not honor Range request (got 200)")
                if response.status_code != 206:
                    raise RuntimeError(f"Bad status code: {response.status_code}")

                mode = "ab" if resume_pos > 0 else "wb"
                downloaded = resume_pos
                with open(chunk_file, mode) as handle:
                    for data in response.iter_content(chunk_size=self.config["chunk_size"]):
                        if data:
                            handle.write(data)
                            downloaded += len(data)
                            if progress_callback:
                                progress_callback(chunk_id, downloaded)

                final_size = os.path.getsize(chunk_file)
                if final_size == chunk_size_expected:
                    if progress_callback:
                        progress_callback(chunk_id, chunk_size_expected)
                    return True
                if final_size < chunk_size_expected:
                    resume_pos = final_size
                    raise RuntimeError(f"Chunk incomplete: {final_size}/{chunk_size_expected}")

                os.remove(chunk_file)
                resume_pos = 0
                raise RuntimeError(f"Chunk too large: {final_size}/{chunk_size_expected}")
            except Exception as exc:
                if attempt < self.config["max_retries"] - 1:
                    delay = min(
                        self.config["retry_delay"] * (2 ** attempt),
                        self.config["max_retry_delay"],
                    )
                    time.sleep(delay)
                else:
                    self.log(f"Chunk {chunk_id} failed after {self.config['max_retries']} attempts: {exc}")
                    return False
        return False

    def merge_chunks(self, filepath: str, num_chunks: int) -> bool:
        temp_file = os.path.normpath(f"{filepath}.tmp")
        try:
            total_size = 0
            chunk_files: List[Tuple[str, int]] = []
            for idx in range(num_chunks):
                chunk_file = os.path.normpath(f"{filepath}.part{idx}")
                if not os.path.exists(chunk_file):
                    self.log(f"Error: Missing chunk {idx}")
                    return False
                size = os.path.getsize(chunk_file)
                chunk_files.append((chunk_file, size))
                total_size += size

            merged_size = 0
            start_time = time.time()
            last_update = 0.0
            with open(temp_file, "wb") as outfile:
                for chunk_file, chunk_size in chunk_files:
                    with open(chunk_file, "rb") as infile:
                        bytes_copied = 0
                        while bytes_copied < chunk_size:
                            data = infile.read(64 * 1024 * 1024)
                            if not data:
                                break
                            outfile.write(data)
                            bytes_copied += len(data)
                            merged_size += len(data)
                            now = time.time()
                            if now - last_update >= 0.5:
                                percent = (merged_size / total_size) * 100 if total_size > 0 else 0.0
                                speed = merged_size / max(0.001, (now - start_time))
                                line = (
                                    f"[MERGING] {percent:.1f}% "
                                    f"({self.format_bytes(merged_size)}/{self.format_bytes(total_size)}) "
                                    f"Speed: {self.format_bytes(speed)}/s"
                                )
                                self.show_progress_line(line)
                                last_update = now

            elapsed = max(0.001, time.time() - start_time)
            avg_speed = total_size / elapsed
            self.finalize_progress_line(
                f"[MERGING] 100.0% ({self.format_bytes(total_size)}/{self.format_bytes(total_size)}) "
                f"Completed in {self.format_time(elapsed)} - Avg: {self.format_bytes(avg_speed)}/s"
            )

            if os.path.exists(filepath):
                os.remove(filepath)
            os.rename(temp_file, filepath)

            for chunk_file, _ in chunk_files:
                try:
                    os.remove(chunk_file)
                except Exception:
                    pass
            return True
        except Exception as exc:
            self.finalize_progress_line()
            self.log(f"Error merging: {exc}")
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass
            return False

    def download_parallel(self, url: str, filepath: str, filename: str, file_size: int) -> bool:
        num_chunks = self.config["num_connections"]
        base_chunk_size = file_size // num_chunks
        chunks = []
        for idx in range(num_chunks):
            start = idx * base_chunk_size
            end = file_size - 1 if idx == num_chunks - 1 else ((idx + 1) * base_chunk_size - 1)
            chunks.append((idx, start, end))

        self.log(
            f"[DOWNLOADING] {filename} ({self.format_bytes(file_size)}) using {num_chunks} connections"
        )

        chunk_progress: Dict[int, int] = {}
        progress_lock = threading.Lock()

        def update_progress(chunk_id: int, bytes_downloaded: int):
            with progress_lock:
                chunk_progress[chunk_id] = bytes_downloaded

        for chunk_id, _start, _end in chunks:
            chunk_file = os.path.normpath(f"{filepath}.part{chunk_id}")
            chunk_progress[chunk_id] = os.path.getsize(chunk_file) if os.path.exists(chunk_file) else 0

        initial_bytes = sum(chunk_progress.values())
        if initial_bytes > 0:
            self.log(f"[RESUMING] Already downloaded: {self.format_bytes(initial_bytes)}")

        start_time = time.time()
        failed_chunks: List[int] = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_chunks) as executor:
            futures = {}
            for chunk_id, start, end in chunks:
                chunk_file = os.path.normpath(f"{filepath}.part{chunk_id}")
                expected_size = end - start + 1
                if os.path.exists(chunk_file) and os.path.getsize(chunk_file) == expected_size:
                    continue
                futures[
                    executor.submit(
                        self.download_chunk,
                        url,
                        start,
                        end,
                        filepath,
                        chunk_id,
                        update_progress,
                    )
                ] = chunk_id

            if not futures:
                self.log("[MERGING] All chunks already complete")
                if self.merge_chunks(filepath, num_chunks) and os.path.getsize(filepath) == file_size:
                    self.log(f"[OK] {filename} completed")
                    return True
                self.log("[ERROR] Size mismatch after merge")
                try:
                    os.remove(filepath)
                except Exception:
                    pass
                return False

            last_update = 0.0
            last_bytes = initial_bytes
            while futures:
                done, _pending = concurrent.futures.wait(
                    list(futures.keys()),
                    timeout=0.5,
                    return_when=concurrent.futures.FIRST_COMPLETED,
                )

                for future in done:
                    chunk_id = futures.pop(future)
                    try:
                        success = future.result()
                        if not success:
                            failed_chunks.append(chunk_id)
                    except Exception as exc:
                        self.log(f"Chunk {chunk_id} exception: {exc}")
                        failed_chunks.append(chunk_id)

                current_time = time.time()
                if current_time - last_update >= 1.0 or not futures:
                    with progress_lock:
                        current_bytes = sum(chunk_progress.values())
                    time_delta = current_time - last_update if last_update > 0 else (current_time - start_time)
                    bytes_delta = current_bytes - last_bytes if last_update > 0 else (current_bytes - initial_bytes)
                    speed = bytes_delta / max(0.001, time_delta)
                    self.print_progress(current_bytes, file_size, start_time, filename, speed)
                    last_update = current_time
                    last_bytes = current_bytes

        self.clear_progress_line()

        if failed_chunks:
            self.log(f"[ERROR] Failed chunks: {failed_chunks}")
            return False

        for chunk_id, start, end in chunks:
            chunk_file = os.path.normpath(f"{filepath}.part{chunk_id}")
            expected_size = end - start + 1
            if not os.path.exists(chunk_file):
                self.log(f"[ERROR] Missing chunk {chunk_id}")
                return False
            actual_size = os.path.getsize(chunk_file)
            if actual_size != expected_size:
                self.log(f"[ERROR] Chunk {chunk_id} incomplete: {actual_size}/{expected_size}")
                return False

        self.log(f"[MERGING] Merging {num_chunks} chunks...")
        if self.merge_chunks(filepath, num_chunks):
            final_size = os.path.getsize(filepath)
            if final_size == file_size:
                elapsed = max(0.001, time.time() - start_time)
                avg_speed = (file_size - initial_bytes) / elapsed if elapsed > 0 else 0
                self.log(
                    f"[OK] {filename} completed in {self.format_time(elapsed)} "
                    f"- Average: {self.format_bytes(avg_speed)}/s"
                )
                return True
            self.log(f"[ERROR] Final size mismatch: {final_size} != {file_size}")
            try:
                os.remove(filepath)
            except Exception:
                pass
            return False

        self.log("[ERROR] Merge failed")
        return False

    def download_single(self, url: str, filepath: str, filename: str, file_size: int) -> bool:
        for attempt in range(self.config["max_retries"]):
            try:
                resume_pos = os.path.getsize(filepath) if os.path.exists(filepath) else 0
                if resume_pos >= file_size:
                    self.log(f"[OK] {filename} already complete")
                    return True

                headers = {"Range": f"bytes={resume_pos}-", "Accept-Encoding": "identity"} if resume_pos > 0 else {
                    "Accept-Encoding": "identity"
                }
                response = self.session.get(
                    url,
                    headers=headers,
                    timeout=self.config["timeout"],
                    stream=True,
                    allow_redirects=True,
                )

                if resume_pos > 0 and response.status_code != 206:
                    self.log(f"[WARNING] Resume not supported for {filename}, restarting")
                    response.close()
                    resume_pos = 0
                    response = self.session.get(
                        url,
                        headers={"Accept-Encoding": "identity"},
                        timeout=self.config["timeout"],
                        stream=True,
                        allow_redirects=True,
                    )

                response.raise_for_status()

                mode = "ab" if resume_pos > 0 else "wb"
                downloaded = 0
                start_time = time.time()
                last_update = 0.0

                if resume_pos > 0:
                    self.log(f"[RESUMING] {filename} from {self.format_bytes(resume_pos)}")
                else:
                    self.log(f"[DOWNLOADING] {filename} ({self.format_bytes(file_size)})")

                with open(filepath, mode) as handle:
                    for chunk in response.iter_content(chunk_size=self.config["chunk_size"]):
                        if chunk:
                            handle.write(chunk)
                            downloaded += len(chunk)
                            now = time.time()
                            if now - last_update >= 0.5:
                                total = resume_pos + downloaded
                                self.print_progress(total, file_size, start_time, filename)
                                last_update = now

                total = resume_pos + downloaded
                self.print_progress(total, file_size, start_time, filename)
                self.clear_progress_line()

                if os.path.getsize(filepath) == file_size:
                    self.log(f"[OK] {filename} completed")
                    return True

                self.log("[ERROR] Size mismatch")
            except Exception as exc:
                self.finalize_progress_line()
                self.log(f"[ERROR] Attempt {attempt + 1}: {exc}")
                if attempt < self.config["max_retries"] - 1:
                    delay = min(
                        self.config["retry_delay"] * (2 ** attempt),
                        self.config["max_retry_delay"],
                    )
                    time.sleep(delay)
                else:
                    return False
        return False

    def download_unknown_size(
        self,
        url: str,
        filepath: str,
        filename: str,
        expected_sha: Optional[str],
        repo_id: str = "",
    ) -> str:
        for attempt in range(self.config["max_retries"]):
            try:
                resume_pos = os.path.getsize(filepath) if os.path.exists(filepath) else 0
                if resume_pos > 0:
                    self.log(f"[RESUMING] {filename} (unknown size) from {self.format_bytes(resume_pos)}")
                    headers = {"Range": f"bytes={resume_pos}-", "Accept-Encoding": "identity"}
                else:
                    self.log(f"[DOWNLOADING] {filename} (unknown size)")
                    headers = {"Accept-Encoding": "identity"}

                response = self.session.get(
                    url,
                    headers=headers,
                    timeout=self.config["timeout"],
                    stream=True,
                    allow_redirects=True,
                )

                if resume_pos > 0 and response.status_code == 416:
                    response.close()
                    if expected_sha:
                        if self.is_file_verified(repo_id, filename, filepath, expected_sha):
                            self.log(f"[SKIP] {filename} already complete and verified (cached)")
                            return DOWNLOAD_STATUS_SKIPPED
                        if self.verify_file_sha256(filepath, expected_sha, filename):
                            self.mark_file_verified(repo_id, filename, filepath, expected_sha)
                            self.log(f"[SKIP] {filename} already complete and verified")
                            return DOWNLOAD_STATUS_SKIPPED
                        self.log(f"[WARNING] {filename} failed verification, re-downloading")
                        try:
                            os.remove(filepath)
                        except Exception:
                            pass
                        resume_pos = 0
                    else:
                        self.log(f"[SKIP] {filename} already complete (range not satisfiable)")
                        return DOWNLOAD_STATUS_SKIPPED

                if resume_pos > 0 and response.status_code != 206:
                    self.log(f"[WARNING] Resume not supported for {filename} (status {response.status_code}), restarting")
                    response.close()
                    resume_pos = 0
                    response = self.session.get(
                        url,
                        headers={"Accept-Encoding": "identity"},
                        timeout=self.config["timeout"],
                        stream=True,
                        allow_redirects=True,
                    )

                response.raise_for_status()

                downloaded = 0
                start_time = time.time()
                last_update = 0.0
                total_size: Optional[int] = None

                if response.status_code == 206:
                    content_range = response.headers.get("content-range")
                    if content_range and "/" in content_range:
                        total_str = content_range.split("/")[-1]
                        if total_str.isdigit():
                            total_size = int(total_str)
                elif response.status_code == 200:
                    content_length = response.headers.get("content-length")
                    if content_length and str(content_length).isdigit():
                        total_size = int(content_length)

                mode = "ab" if resume_pos > 0 else "wb"
                with open(filepath, mode) as handle:
                    for chunk in response.iter_content(chunk_size=self.config["chunk_size"]):
                        if chunk:
                            handle.write(chunk)
                            downloaded += len(chunk)
                            now = time.time()
                            if now - last_update >= 0.5:
                                if total_size and total_size > 0:
                                    self.print_progress(resume_pos + downloaded, total_size, start_time, filename)
                                else:
                                    elapsed = max(0.001, now - start_time)
                                    speed = downloaded / elapsed
                                    line = (
                                        f"[DOWNLOADING] {filename}: {self.format_bytes(resume_pos + downloaded)} "
                                        f"@ {self.format_bytes(speed)}/s"
                                    )
                                    self.show_progress_line(line)
                                last_update = now
                response.close()

                final_size = os.path.getsize(filepath)
                elapsed = max(0.001, time.time() - start_time)
                avg_speed = final_size / elapsed
                self.finalize_progress_line(
                    f"[OK] {filename} completed ({self.format_bytes(final_size)}) "
                    f"in {self.format_time(elapsed)} - Avg: {self.format_bytes(avg_speed)}/s"
                )

                if expected_sha:
                    if not self.verify_file_sha256(filepath, expected_sha, filename):
                        self.log(f"[ERROR] {filename} downloaded but failed SHA256 verification")
                        try:
                            os.remove(filepath)
                        except Exception:
                            pass
                        return DOWNLOAD_STATUS_FAILED
                    if repo_id:
                        self.mark_file_verified(repo_id, filename, filepath, expected_sha)
                return DOWNLOAD_STATUS_DOWNLOADED
            except Exception as exc:
                self.finalize_progress_line()
                self.log(f"[ERROR] Attempt {attempt + 1}: {exc}")
                if attempt < self.config["max_retries"] - 1:
                    delay = min(
                        self.config["retry_delay"] * (2 ** attempt),
                        self.config["max_retry_delay"],
                    )
                    time.sleep(delay)
                else:
                    return DOWNLOAD_STATUS_FAILED
        return DOWNLOAD_STATUS_FAILED

    def download_file(
        self,
        repo_id: str,
        filename: str,
        local_dir: str,
        local_relpath: Optional[str] = None,
    ) -> str:
        url = self.get_file_url(repo_id, filename)
        local_path = local_relpath if local_relpath else filename
        filepath = os.path.normpath(os.path.join(local_dir, local_path))
        display_name = local_path

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        expected_sha = self.get_file_sha256(repo_id, filename)
        if expected_sha:
            self.log(f"[INFO] Expected SHA256: {expected_sha[:16]}...")

        file_size = self.get_file_size(url, repo_id=repo_id, filename=filename)

        if os.path.exists(filepath):
            actual_size = os.path.getsize(filepath)
            if isinstance(file_size, int) and file_size >= 0:
                if actual_size == file_size:
                    if expected_sha and self.is_file_verified(repo_id, filename, filepath, expected_sha):
                        self.log(
                            f"[SKIP] {display_name} already complete and verified (cached) "
                            f"({self.format_bytes(file_size)})"
                        )
                        return DOWNLOAD_STATUS_SKIPPED
                    if expected_sha:
                        if self.verify_file_sha256(filepath, expected_sha, display_name):
                            self.mark_file_verified(repo_id, filename, filepath, expected_sha)
                            self.log(
                                f"[SKIP] {display_name} already complete and verified "
                                f"({self.format_bytes(file_size)})"
                            )
                            return DOWNLOAD_STATUS_SKIPPED
                        self.log(f"[WARNING] {display_name} failed verification, re-downloading")
                        try:
                            os.remove(filepath)
                        except Exception:
                            pass
                    else:
                        self.log(f"[SKIP] {display_name} already complete ({self.format_bytes(file_size)})")
                        return DOWNLOAD_STATUS_SKIPPED
                elif actual_size > file_size:
                    self.log(f"[WARNING] {display_name} corrupted (larger than expected), re-downloading")
                    try:
                        os.remove(filepath)
                    except Exception:
                        pass
                else:
                    self.log(
                        f"[RESUMING] {display_name} from "
                        f"{self.format_bytes(actual_size)}/{self.format_bytes(file_size)}"
                    )
            elif expected_sha and actual_size > 0:
                if self.is_file_verified(repo_id, filename, filepath, expected_sha):
                    self.log(
                        f"[SKIP] {display_name} exists and verified (cached) "
                        f"({self.format_bytes(actual_size)})"
                    )
                    return DOWNLOAD_STATUS_SKIPPED
                if self.verify_file_sha256(filepath, expected_sha, display_name):
                    self.mark_file_verified(repo_id, filename, filepath, expected_sha)
                    self.log(f"[SKIP] {display_name} exists and verified ({self.format_bytes(actual_size)})")
                    return DOWNLOAD_STATUS_SKIPPED
                self.log(f"[WARNING] {display_name} failed verification, re-downloading")
                try:
                    os.remove(filepath)
                except Exception:
                    pass

        if file_size is None:
            self.log(f"[INFO] Could not determine size for {display_name}; downloading without size info")
            return self.download_unknown_size(url, filepath, display_name, expected_sha, repo_id)

        if file_size > 10 * 1024 * 1024:
            if self.supports_range(url):
                success = self.download_parallel(url, filepath, display_name, file_size)
            else:
                self.log(f"[INFO] Range requests not supported for {display_name}; using single connection")
                success = self.download_single(url, filepath, display_name, file_size)
        else:
            success = self.download_single(url, filepath, display_name, file_size)

        if success and expected_sha:
            if not self.verify_file_sha256(filepath, expected_sha, display_name):
                self.log(f"[ERROR] {display_name} downloaded but failed SHA256 verification")
                try:
                    os.remove(filepath)
                except Exception:
                    pass
                return DOWNLOAD_STATUS_FAILED
            self.mark_file_verified(repo_id, filename, filepath, expected_sha)

        return DOWNLOAD_STATUS_DOWNLOADED if success else DOWNLOAD_STATUS_FAILED


def _normalize_subdir_prefix(subdir: Optional[str]) -> str:
    if not subdir:
        return ""
    return subdir.replace("\\", "/").strip("/") + "/"


def _dedupe_preserve_order(values: Sequence[str]) -> List[str]:
    seen = set()
    result: List[str] = []
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result


def _expand_model_keys(model_types: Optional[Sequence[str]]) -> List[str]:
    requested = list(model_types) if model_types else [MAIN_BUNDLE_KEY]
    expanded: List[str] = []
    for key in requested:
        if key == MAIN_BUNDLE_KEY:
            expanded.extend(DEFAULT_MODEL_KEYS)
        elif key in MODEL_CODE_VARIANTS:
            expanded.extend((*SHARED_MODEL_KEYS, key))
        else:
            expanded.append(key)
    return _dedupe_preserve_order(expanded)


def _resolve_target_dir(download_dir: Optional[str]) -> Path:
    if download_dir:
        return Path(download_dir).expanduser().resolve()
    env_dir = os.environ.get("ACESTEP_CHECKPOINTS_DIR", "").strip()
    if env_dir:
        return Path(env_dir).expanduser().resolve()
    return TARGET_DIR.resolve()


def _sync_model_code_files(model_name: str, model_dir: Path) -> List[str]:
    variant = MODEL_CODE_VARIANTS.get(model_name)
    if not variant:
        return []

    source_dir = APP_ROOT / "acestep" / "models" / variant
    if not source_dir.exists() or not model_dir.exists():
        return []

    synced: List[str] = []
    for src_file in source_dir.glob("*.py"):
        if src_file.name == "__init__.py":
            continue
        shutil.copy2(src_file, model_dir / src_file.name)
        synced.append(src_file.name)
    return synced


def scan_repo_files(repo_id: str, specific_files: Optional[List[str]] = None) -> List[str]:
    if specific_files:
        return specific_files
    try:
        api = _create_hf_api()
        return list(api.list_repo_files(repo_id=repo_id, repo_type="model"))
    except Exception as exc:
        print(f"Error scanning repository {repo_id}: {exc}")
        return specific_files or []


def _download_model_config(
    downloader: RobustDownloader,
    target_dir: Path,
    key: str,
    cfg: Dict[str, Any],
    dry_run: bool = False,
) -> Tuple[int, int, int]:
    repo_id = cfg["repo_id"]
    name = cfg.get("name") or key
    description = cfg.get("description") or ""
    subdir_prefix = _normalize_subdir_prefix(cfg.get("subdir"))
    local_target_subdir = (cfg.get("local_target_subdir") or "").replace("\\", "/").strip("/")

    files_to_download = scan_repo_files(repo_id, cfg.get("files"))
    if not files_to_download:
        print(f"[ERROR] No files found for {name} ({repo_id})")
        return 0, 1, 0

    if subdir_prefix:
        files_to_download = [
            filename
            for filename in files_to_download
            if isinstance(filename, str) and filename.replace("\\", "/").startswith(subdir_prefix)
        ]
        if not files_to_download:
            print(f"[ERROR] No files found under subdir '{subdir_prefix}' in {repo_id}")
            return 0, 1, 0

    model_dir = target_dir / local_target_subdir if local_target_subdir else target_dir
    model_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 72}")
    print(f"Downloading {name}")
    if description:
        print(f"Description: {description}")
    print(f"Repository: {repo_id}")
    print(f"Target: {model_dir}")
    print(f"Files: {len(files_to_download)}")
    if subdir_prefix:
        print(f"Source subdir: {subdir_prefix}")

    if dry_run:
        sample_targets: List[str] = []
        for remote_name in files_to_download[:5]:
            remote_name = remote_name.replace("\\", "/")
            local_rel = remote_name[len(subdir_prefix):] if subdir_prefix else remote_name
            sample_targets.append(str((model_dir / local_rel).resolve()))
        print("[DRY RUN] Planned file targets:")
        for sample in sample_targets:
            print(f"  - {sample}")
        if len(files_to_download) > 5:
            print(f"  ... and {len(files_to_download) - 5} more")
        return 0, 0, 0

    downloader.prefetch_repo_metadata(repo_id)

    downloaded = 0
    failed = 0
    skipped = 0
    for remote_name in files_to_download:
        remote_name = remote_name.replace("\\", "/")
        local_rel = remote_name[len(subdir_prefix):] if subdir_prefix else remote_name
        status = downloader.download_file(repo_id, remote_name, str(model_dir), local_relpath=local_rel)
        if status == DOWNLOAD_STATUS_DOWNLOADED:
            downloaded += 1
        elif status == DOWNLOAD_STATUS_SKIPPED:
            skipped += 1
        else:
            failed += 1

    synced = _sync_model_code_files(local_target_subdir or key, model_dir)
    if synced:
        print(f"Synced model code files: {', '.join(synced)}")

    print(f"\nSummary for {name}:")
    print(f"  Downloaded: {downloaded}")
    print(f"  Skipped: {skipped}")
    print(f"  Failed: {failed}")
    return downloaded, failed, skipped


def download_models(
    download_dir: Optional[str] = None,
    model_types: Optional[Sequence[str]] = None,
    dry_run: bool = False,
) -> int:
    target_dir = _resolve_target_dir(download_dir)
    os.environ.setdefault("ACESTEP_PROJECT_ROOT", str(APP_ROOT.resolve()))
    os.environ["ACESTEP_CHECKPOINTS_DIR"] = str(target_dir)

    selected_keys = _expand_model_keys(model_types)
    invalid = [key for key in selected_keys if key not in MODEL_CONFIGS]
    if invalid:
        print(f"Error: Invalid model keys: {', '.join(invalid)}")
        print(f"Valid options: {', '.join([MAIN_BUNDLE_KEY] + sorted(MODEL_CONFIGS.keys()))}")
        return 1

    downloader = RobustDownloader(DOWNLOAD_CONFIG)
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Target directory: {target_dir}")
    print(f"Requested models: {', '.join(model_types) if model_types else MAIN_BUNDLE_KEY}")
    if MAIN_BUNDLE_KEY in (model_types or [MAIN_BUNDLE_KEY]):
        print("Default premium bundle expands to: " f"{', '.join(DEFAULT_MODEL_KEYS)}")
    elif selected_keys != list(model_types or []):
        print("Expanded download set: " f"{', '.join(selected_keys)}")
    print(f"Mode: {'dry run' if dry_run else 'download'}")

    total_downloaded = 0
    total_failed = 0
    total_skipped = 0
    for key in selected_keys:
        downloaded, failed, skipped = _download_model_config(
            downloader=downloader,
            target_dir=target_dir,
            key=key,
            cfg=MODEL_CONFIGS[key],
            dry_run=dry_run,
        )
        total_downloaded += downloaded
        total_failed += failed
        total_skipped += skipped

    print(f"\n{'=' * 72}")
    print("OVERALL SUMMARY")
    print(f"  Downloaded: {total_downloaded}")
    print(f"  Skipped: {total_skipped}")
    print(f"  Failed: {total_failed}")
    print(f"  Model directory: {target_dir}")
    if dry_run:
        print("  No files were downloaded because --dry-run was used.")
        return 0

    if total_failed == 0:
        print("\n[SUCCESS] ACE-Step downloads completed successfully.")
        return 0

    print(f"\n[ERROR] {total_failed} file downloads failed.")
    return 1


def print_model_list():
    print("\nAvailable ACE-Step downloader targets:")
    print("=" * 72)
    print(f"\n[Default bundle]")
    print(f"  {MAIN_BUNDLE_KEY} -> {', '.join(DEFAULT_MODEL_KEYS)}")

    print("\n[Shared components]")
    for key in SHARED_MODEL_KEYS:
        cfg = MODEL_CONFIGS[key]
        print(f"  {key} -> {cfg['repo_id']}::{cfg.get('subdir', key)}")

    print("\n[Premium DiT models]")
    for key in DEFAULT_DIT_MODEL_KEYS:
        cfg = MODEL_CONFIGS[key]
        print(f"  {key} -> {cfg['repo_id']}")

    print("\nNotes:")
    print(f"  - Running without arguments downloads the default premium bundle ({MAIN_BUNDLE_KEY}).")
    print("  - Requesting a DiT model downloads the shared runtime, bundled LMs, and that DiT model.")
    print("=" * 72)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Robust ACE-Step Hugging Face downloader with SHA verification and resume support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python HF_model_downloader.py\n"
            "  python HF_model_downloader.py --model main\n"
            "  python HF_model_downloader.py --model acestep-v15-xl-turbo  # shared runtime + XL-Turbo\n"
            "  python HF_model_downloader.py --model main acestep-v15-xl-base\n"
            "  python HF_model_downloader.py --list\n"
        ),
    )
    parser.add_argument(
        "--model",
        "-m",
        nargs="+",
        help=f"Models to download. Valid keys: {', '.join([MAIN_BUNDLE_KEY] + sorted(MODEL_CONFIGS.keys()))}",
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Download every explicitly listed ACE-Step target",
    )
    parser.add_argument(
        "--dir",
        "-d",
        type=str,
        default=None,
        help=f"Custom model directory (default: {TARGET_DIR})",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List ACE-Step downloader targets",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned downloads without transferring files",
    )

    args = parser.parse_args()

    if args.list:
        print_model_list()
        return 0

    model_types = list(MODEL_CONFIGS.keys()) if args.all else args.model
    return download_models(
        download_dir=args.dir,
        model_types=model_types,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    raise SystemExit(main())
