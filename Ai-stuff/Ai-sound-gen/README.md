# Running ACE-Step Premium on Google Colab (Tesla T4) - Student Guide

This guide walks you through launching the ACE-Step Premium music-generation app on a free Google Colab Tesla T4 GPU and getting a public URL through **ngrok** so you can use the UI in your browser.

Estimated time end-to-end: **25-40 minutes**, most of which is unattended model downloading.

---

## What you need before you start

1. A free **Google account** (for Colab).
2. A free **ngrok account**. Sign up at https://dashboard.ngrok.com, then open `Your Authtoken` and copy the long string. You will paste it into the notebook later.
3. The notebook file `ACE_Step_Premium_Colab_T4.ipynb` (provided alongside this guide).

---

## Step 1 - Open the notebook in Colab

1. Go to https://colab.research.google.com.
2. Click `File` -> `Upload notebook` and select `ACE_Step_Premium_Colab_T4.ipynb`.
3. When it opens, click `Runtime` -> `Change runtime type`.
4. Set **Hardware accelerator** to `GPU` and **GPU type** to `T4`. Click `Save`.

You should now see "Connected" with a green tick at the top right.

---

## Step 2 - Confirm the GPU (notebook cell "Step 1")

Run the first code cell (`!nvidia-smi ...`). The output must show **Tesla T4** and `CUDA available : True`. If it shows anything else, repeat Step 1 above.

---

## Step 3 - Install FFmpeg (notebook cell "Step 2")

Run the FFmpeg cell. It downloads a fresh static build and copies `ffmpeg` and `ffprobe` into `/usr/local/bin`. The cell ends by printing the FFmpeg version line.

---

## Step 4 - Clone the repository (notebook cell "Step 3")

This pulls `FurkanGozukara/ACE-Step_Premium` into `/content/ACE-Step_Premium`. Takes ~10 seconds.

---

## Step 5 - Install Python dependencies (notebook cells "Step 4")

There are **three** cells in this step:

a. The first one writes a Tesla-T4-compatible `requirements_ACE_Step_Colab_T4.txt`. We **do not** install `flash_attn`, `xformers` or `sageattention` because the wheels shipped in the original requirements are built against CUDA 13.1, which Colab T4 does not have. The app falls back to PyTorch's built-in attention - that works fine on T4.

b. The second cell installs those slimmed requirements. Takes 2-4 minutes.

c. The third cell installs the bundled `nano-vllm` package from inside the cloned repo. Takes about a minute.

If pip prints warnings like "package X requires Y" you can usually ignore them as long as no `ERROR` appears.

---

## Step 6 - Download the models (notebook cell "Step 5")

Click the cell and run it. This is the slow step: **10-25 minutes** depending on Hugging Face speed. The downloader pulls:

- ACE-Step 1.5 VAE
- Qwen3-Embedding-0.6B (text encoder)
- 5Hz LMs (0.6B, 1.7B, 4B)
- **ACE-Step XL Turbo** DiT (the only XL variant we use on T4 - others need more VRAM than the T4's 16 GB)

Total disk: roughly **35-45 GB** in `/content/ACE-Step_Premium/models`.

If a file fails its SHA256 check or the connection drops, **just re-run the cell**. The downloader resumes and skips finished files.

---

## Step 7 - Add your ngrok token (notebook cell "Step 6")

1. Open https://dashboard.ngrok.com/get-started/your-authtoken and copy your token.
2. In the cell, replace `PASTE_YOUR_NGROK_AUTHTOKEN_HERE` with your token (keep the quotes).
3. Run the cell. It should print `ngrok configured.`

The token is only stored in this Colab session - it is wiped when the session ends.

---

## Step 8 - Launch the app and get the public URL (notebook cell "Step 7")

Run the final cell. The first lines of output look like:

```
======================================================================
  ACE-Step Premium PUBLIC URL:
   NgrokTunnel: "https://xxxx-xx-xx-xxx-xxx.ngrok-free.app" -> "http://localhost:7860"
======================================================================
```

Copy the `https://...ngrok-free.app` URL and **open it in a new browser tab**. The first time you visit, ngrok shows a yellow warning page - click `Visit Site`.

**Important:** the Gradio app takes another **30-90 seconds** after this point to load the models. If the page is blank or shows a 502 at first, wait, then refresh.

When the UI appears, you can:

- Enter lyrics in the textbox.
- Enter a music style prompt (e.g. "lofi hip hop, mellow piano, 90 BPM").
- Click `Generate` and listen.

Leave the Step 7 cell running in Colab. Closing or stopping that cell takes the app down.

---

## Sharing the URL with students

Send your students the `https://...ngrok-free.app` URL. They can use the UI directly from their own machines - no Colab account or GPU needed on their side.

Note that on the free ngrok plan:
- Each session URL is **temporary** - it changes every time you restart the notebook.
- You can have **only one** ngrok tunnel open at a time per account.
- The first visit shows a "you are about to visit..." warning page - that is normal and not a security problem.

---

## Stopping cleanly

1. Click the Stop (square) button on the Step 7 cell to kill the Gradio app.
2. Run the "Stop the app cleanly" cell to release port 7860 and tear the tunnel down.
3. (Optional) `Runtime` -> `Disconnect and delete runtime` to free the Colab session.

---

## Common problems

| Symptom | Fix |
|---|---|
| `No GPU detected` | Runtime menu -> Change runtime type -> T4 GPU, then re-run from Step 1. |
| `CUDA out of memory` during generation | Use shorter audio (about 60 s), the 0.6 B or 1.7 B LM, and the XL Turbo model only. Restart the runtime if it persists. |
| ngrok page shows `ERR_NGROK_4018` or `failed to connect` | Wait until Step 7 prints `Running on local URL: http://0.0.0.0:7860`. The app needs a minute to load. |
| `flash_attn ImportError` | Expected on T4. If a code path crashes on it, add `os.environ['ACESTEP_DISABLE_FLASH']='1'` at the top of the Step 7 cell and re-run. |
| Colab disconnects mid-session | Free Colab caps sessions at ~90 minutes idle / 12 hours total. Re-run Steps 6 and 7 to get a new public URL - the models are still on disk and skip re-download. |
| HF download keeps failing | Re-run the Step 5 cell. The downloader is resumable and verifies SHA256, so re-running is safe. |

---

## What the files in this bundle are

- `ACE_Step_Premium_Colab_T4.ipynb` - the notebook to upload to Colab.
- `requirements_ACE_Step_Colab_T4.txt` - the Tesla-T4-compatible requirements (also written inline by the notebook, kept here for reference).
- `Google_Colab_T4_Student_Guide.md` - this document.
