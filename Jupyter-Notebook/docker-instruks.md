# Jupyter + JavaScript (Node.js) in Docker (Windows 11) — Student Guide

This guide gets you from zero to running **Jupyter Notebook/Lab with a JavaScript (Node.js) kernel** using Docker on Windows 11.

* Image you’ll run: **`jensern/jupyter-ijs:1.0`**
* Login password: **`class`**
* Nothing else to install (Node, Python, etc. are inside the container)

---

## 0) Requirements

* Windows 11 with **hardware virtualization** enabled (most PCs already have this).
* **Admin** rights (to install Docker Desktop).
* \~3 GB free disk space.

---

## 1) Install Docker Desktop (WSL2 backend)

1. Download **Docker Desktop for Windows**: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Run the installer. **Keep “Use WSL 2 instead of Hyper-V” checked.**
3. When installation finishes, **restart your PC** if prompted.
4. Open **Docker Desktop** and wait until it says **Engine running**.

> If WSL isn’t installed, open **PowerShell (Admin)** and run:
>
> ```powershell
> wsl --install
> wsl --update
> ```

---

## 2) Verify Docker works

Open **PowerShell** and run:

```powershell
docker --version
docker compose version
docker run hello-world
```

You should see messages showing Docker is working.

---

## 3) Get the class image (optional pre-pull)

```powershell
docker pull jensern/jupyter-ijs:1.0
```

---

## 4) Run with Docker Compose (recommended)

### A) Create a project folder

```powershell
mkdir jupyter-class
cd jupyter-class
```

### B) Create `compose.yaml`

Create a file named **`compose.yaml`** in this folder with the following content:

```yaml
services:
  jupyter-ijs:
    image: jensern/jupyter-ijs:1.0
    ports:
      - "8888:8888"
    environment:
      JUPYTER_PASSWORD: class   # login using this password
      JUPYTER_TOKEN: ""         # disable token links
    command: start-notebook.sh --ServerApp.token=''  # force no token
    volumes:
      - ./:/home/jovyan/work    # your current folder is mounted into the container
```

### C) Start Jupyter

```powershell
docker compose up -d
```

Open your browser to **[http://127.0.0.1:8888](http://127.0.0.1:8888)**
**Password:** `class`

> If port 8888 is busy, change the line to `"8889:8888"` and start again.

### D) Create your first JavaScript notebook

1. In Jupyter, click **Launcher → JavaScript (Node.js)**.
2. Test cell:

   ```javascript
   console.log("Node:", process.version);
   1 + 2
   ```

> Your files are saved on **your Windows folder** (`jupyter-class`) because it’s mounted into the container.

### E) Stop / Start later

```powershell
# stop and remove the container
docker compose down

# start again (in background)
docker compose up -d

# view logs
docker compose logs -f
```

---

## 5) (Alternative) Run without Compose

If you prefer a one-line command:

**PowerShell**

```powershell
docker run -d --name jupyter-ijs `
  -p 8888:8888 `
  -e JUPYTER_PASSWORD=class -e JUPYTER_TOKEN= `
  -v ${PWD}:/home/jovyan/work `
  jensern/jupyter-ijs:1.0 `
  start-notebook.sh --ServerApp.token=''
```

Open **[http://127.0.0.1:8888](http://127.0.0.1:8888)**, password **class**.

To stop:

```powershell
docker rm -f jupyter-ijs
```

---

## 6) Installing npm packages for your notebook

Packages should live **next to your notebook** in your project folder.

**Option A — from Jupyter’s Terminal**

1. In Jupyter, **File → New → Terminal**.
2. Run:

   ```bash
   cd work
   npm init -y
   npm install lodash
   ```
3. In a JS notebook cell:

   ```javascript
   const _ = require("lodash");
   _.chunk([1,2,3,4,5], 2);
   ```

**Option B — from PowerShell on Windows**

```powershell
cd jupyter-class
npm init -y
npm install lodash
```

---

## 7) Updating to a new version (when told by the teacher)

```powershell
cd jupyter-class
docker compose pull
docker compose up -d
```

(Or if you used `docker run`, stop and re-run with the same command.)

---

## 8) Troubleshooting

### A) “Docker engine not running” / WSL errors

* Open **Docker Desktop** and wait for **Engine running**.
* In PowerShell (Admin):

  ```powershell
  wsl --update
  wsl --shutdown
  ```
* Docker Desktop → **Settings → General**: ensure **Use WSL 2 based engine** is checked.
  **Settings → Resources → WSL Integration**: enable your default distro.

### B) Browser asks for a token instead of password

We disable tokens via `command: start-notebook.sh --ServerApp.token=''`.
If you still see token links, you’re likely on an old container:

```powershell
docker compose down
docker compose up -d --force-recreate
```

### C) Port already in use

Edit `compose.yaml`:

```yaml
ports:
  - "8889:8888"
```

Then:

```powershell
docker compose up -d
```

### D) “JavaScript (Node.js)” kernel missing

It’s included in the image. To double-check:

```powershell
docker compose exec jupyter-ijs jupyter kernelspec list
```

You should see **javascript**. If not, recreate the container:

```powershell
docker compose down
docker compose up -d --force-recreate
```

### E) Reset everything (safe; your files stay on Windows)

```powershell
docker compose down
docker image rm jensern/jupyter-ijs:1.0
docker compose up -d
```

---

## 9) Quick command cheatsheet

```powershell
# start in background
docker compose up -d

# stop & remove
docker compose down

# restart
docker compose restart

# see running containers
docker ps

# view logs (Ctrl+C to stop watching)
docker compose logs -f
```

---

### You’re done!

Open **[http://127.0.0.1:8888](http://127.0.0.1:8888)**, log in with **password `class`**, create a **JavaScript (Node.js)** notebook, and start coding.
