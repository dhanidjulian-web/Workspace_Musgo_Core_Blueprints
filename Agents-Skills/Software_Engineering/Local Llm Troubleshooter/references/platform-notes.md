# Platform & Tool Notes

Hardware-, OS-, and tool-specific detail behind the fixes in
symptom-playbook.md. Verify exact flags against the current docs of the
installed version — local LLM tooling moves fast.

---

## Apple Silicon (M-series)

- **Unified memory.** CPU and GPU share one memory pool; there is no separate
  VRAM. The GPU is the Metal backend, on by default in Mac builds of llama.cpp,
  Ollama, and LM Studio.
- **GPU memory cap.** macOS limits how much of unified memory the GPU may use —
  roughly two-thirds of RAM on machines with 36 GB or less, about three-quarters
  above that. A big model can OOM even with free RAM because of this cap.
- **Raising the cap.** `sudo sysctl iogpu.wired_limit_mb=<MB>` raises it
  immediately, no reboot needed (this key replaced the older
  `debug.iogpu.wired_limit`). The value is megabytes: 60 GB is `61440`. **Leave
  8–16 GB for macOS** — allocating everything causes beachballs or a hard lock.
  Restart the inference app afterward to pick up the new limit.
- **Verify.** When a model loads you will see a line like
  `ggml_metal_init: recommendedMaxWorkingSetSize = <MB>` — it should reflect the
  new cap.
- This tweak is unsupported by Apple; a macOS update may change the behavior.
- No GPU drivers to install or break — if a Mac build is slow, suspect memory
  pressure or thermal throttling, not a missing driver.

## NVIDIA (Linux / Windows)

- **Drivers first.** `nvidia-smi` must run and list the GPU. If it fails,
  nothing downstream will use the GPU — fix the driver before anything else.
- **CUDA toolkit** is needed to build GPU runtimes.
- **Building llama.cpp with CUDA:** `cmake -B build -DGGML_CUDA=ON` then
  `cmake --build build --config Release`. The old `LLAMA_CUBLAS` flag is
  obsolete and no longer works. Clean the `build/` directory when switching
  backends — a stale CMake cache causes subtle failures.
- A prebuilt CPU-only binary will never use the GPU regardless of runtime flags.
- Exit code 137 from a runner means the OS OOM-killer reclaimed it.

## AMD

- GPU acceleration uses **ROCm**. On Linux, recent Ollama builds support ROCm;
  confirm ROCm is installed and the GPU is on the supported list.
- Windows AMD support is more limited than NVIDIA — a Vulkan backend or CPU
  fallback may be the realistic path. Check current tool docs.

## Windows / WSL2

- Native Windows builds of Ollama and LM Studio exist and use the GPU directly.
- For CUDA inside **WSL2**: install a recent Windows NVIDIA driver (it provides
  the WSL CUDA stack); do not install a separate Linux driver inside WSL.
  `nvidia-smi` should work inside the WSL distro once set up.
- Windows environment variables (for Ollama: `OLLAMA_*`) are set via System
  Properties → Environment Variables; quit and restart Ollama afterward.

## Docker

- Pass `--gpus all` to the container and install the **NVIDIA Container
  Toolkit** on the host. Without both, the container sees no GPU and silently
  runs on CPU.
- Mount model weights from a local SSD path, not a network volume, to avoid the
  file-lock contention described in symptom-playbook.md.

---

## Ollama

- **Logs:** macOS `~/.ollama/logs/server.log`; Windows
  `%LOCALAPPDATA%\Ollama\server.log`; Linux via `journalctl -u ollama` when run
  as a service, or stdout when run with `ollama serve`.
- **Context window:** the default is small (4096 tokens in recent versions).
  Raise it with the `num_ctx` parameter or the `OLLAMA_CONTEXT_LENGTH`
  environment variable. A `PARAMETER num_ctx` baked into a Modelfile overrides
  the environment variable — check the Modelfile if the env var seems ignored.
  Required RAM scales with `OLLAMA_NUM_PARALLEL` × context length.
- **Is it on the GPU?** `ollama ps` shows a processor column — `100% GPU`, a
  CPU/GPU split, or `100% CPU`. A split or all-CPU means the model did not fully
  fit in GPU memory.
- **Partial pulls:** interrupted `ollama pull` leaves `*partial*` files under
  `~/.ollama/models/blobs/`; re-running the pull resumes them.

## llama.cpp

- **No standard log file** — it writes to stdout/stderr. Capture it
  (`./llama-server ... 2>&1 | tee server.log`) and pass that path to
  `llm_doctor.py --llamacpp-log`.
- **GPU offload at runtime:** `--n-gpu-layers <N>` (or `-ngl`). `99` offloads
  every layer; a lower number splits across GPU and CPU.
- **Context:** `-c <tokens>`.
- **Server health:** `GET /health` returns `{"status":"ok"}` when ready and a
  loading status (often HTTP 503) while a model loads — that is the STUCK_LOADING
  signal.
- Models are GGUF. Pre-GGUF GGML files are no longer supported.

## LM Studio

- **Logs** live under `~/.lmstudio` (server logs in a `server-logs` subfolder;
  layout varies by version). Point `llm_doctor.py` at it with
  `--lmstudio-log-dir` if auto-discovery misses it.
- **GPU offload** is a slider in the model load settings — at zero, the model
  runs on CPU. Raise it until the model is fully or mostly on the GPU.
- **Runtime selection:** LM Studio ships multiple backends (Metal, CUDA, Vulkan,
  CPU). The wrong one selected explains a GPU sitting idle.
- **Context length** is set in the model load panel; too high triggers OOM.
- The built-in server is OpenAI-compatible, default port 1234, `/v1/models`.

## Hugging Face downloads

- **Cache location:** `~/.cache/huggingface/hub` by default; overridden by
  `HF_HOME`, `HF_HUB_CACHE`, or `HUGGINGFACE_HUB_CACHE`.
- **Partial files:** an in-progress download is a `*.incomplete` file in the
  cache. One that has stopped growing is a stalled download.
- **Auth:** gated or private repos need a token — `huggingface-cli login` or the
  `HF_TOKEN` environment variable — and gated models also require requesting
  access on the model page.
- **Resuming:** re-running the download resumes from the `.incomplete` file;
  deleting it forces a clean restart.
- A download that stalls silently is very often a full disk — check free space.
