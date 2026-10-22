# Symptom Playbook

Cause-and-fix detail for every category `llm_doctor.py` reports, plus the
symptoms that leave no log signature. Apply one fix at a time, then re-run the
script to confirm the signature cleared.

---

## RUNNER_CRASH — the model runner is being killed

**Signatures:** `llama runner process has terminated`, `signal: killed`,
`exit status 137`, `oom-kill`.

**What it means.** The process loading or running the model was terminated by
the operating system. Exit code 137 and "signal: killed" mean the OS
out-of-memory killer reclaimed it — the model plus its KV cache asked for more
memory than the machine had. This is the single most common local-LLM failure.

**Fixes, cheapest first:**

1. Lower the context window. A large context multiplies KV-cache memory. In
   Ollama this is `num_ctx` (or `OLLAMA_CONTEXT_LENGTH`); in llama.cpp it is
   `-c`; in LM Studio it is the context-length field.
2. Drop quantization one step (Q6 to Q5, Q5 to Q4). Each step cuts memory
   meaningfully at a modest quality cost.
3. Use a smaller model. A 7B model that fits beats a 13B that is swap-thrashing.
4. Close other memory-hungry apps and re-run while the model loads.

If none work, the hardware ceiling has been reached — see platform-notes.md
for raising the Apple Silicon GPU cap, and consider cloud inference as a
fallback for that workload.

---

## OOM — out of memory during load or generation

**Signatures:** `out of memory`, `CUDA error: out of memory`,
`failed to allocate`, `ggml_metal ... alloc`, `unable to allocate backend buffer`.

**What it means.** An allocation failed outright. Unlike RUNNER_CRASH (the OS
kills the process), here the runtime itself reports it could not get the memory.
Same root cause: model + context + batch exceed VRAM or unified memory.

**Fixes, cheapest first:**

1. Reduce context length first — it is the cheapest lever.
2. Pick a quant that fully fits. Rough rule of thumb for a 7B model: ~4–5 GB at
   Q4, ~5–6 GB at Q5, plus KV cache that grows with context. Multiply by model
   size for larger models.
3. Reduce GPU-offloaded layers so the model splits across GPU and CPU instead
   of demanding all-VRAM residency (llama.cpp `--n-gpu-layers`, Ollama
   `num_gpu`).
4. On Apple Silicon, raise the GPU memory cap (see platform-notes.md).
5. Reduce batch size if the runtime exposes it (vLLM `--max-num-batched-tokens`).

---

## GGUF_VERSION — model file format newer or older than the runtime

**Signatures:** `unsupported gguf version`, `this format is no longer supported`,
`obsolete`.

**What it means.** The model file uses a GGUF revision the installed binary
does not understand, or it is a pre-GGUF "GGML" file that modern runtimes have
dropped. The format moved; the binary did not.

**Fixes:**

1. Update the runtime — `llama.cpp` (rebuild from a recent commit), the Ollama
   app, or LM Studio's runtime selector.
2. Or download a model file built for the installed version.
3. Replace any old `.ggml` / pre-GGUF files with current GGUF builds.

---

## MODEL_LOAD — the model failed to load

**Signatures:** `error loading model`, `failed to load model`,
`unknown model architecture`, `invalid magic`, `tensor ... not found`,
`wrong number of tensors`.

**What it means.** Either the file is corrupt or truncated, or it is an
architecture the runtime does not support.

**Fixes:**

1. Re-download the model. A truncated file (interrupted download) fails exactly
   like this. Check the file size against the source repository.
2. `invalid magic` almost always means a corrupt or non-model file — re-pull.
3. `unknown model architecture` means the runtime is too old for a newer model
   family — update the runtime.

---

## PORT_CONFLICT — the server cannot bind its port

**Signatures:** `address already in use`, `eaddrinuse`, `bind ... failed`,
`listen tcp ... in use`.

**What it means.** Another process already holds the port — usually a previous
server instance that did not shut down cleanly.

**Fixes:**

1. Find the holder and stop it:
   - macOS / Linux: `lsof -i :11434` (or the relevant port), then `kill <PID>`.
   - Windows: `netstat -ano | findstr 11434`, then `taskkill /PID <PID> /F`.
2. Or start the server on a different port and point clients at the new one.
3. If it recurs on every boot, a duplicate service or launch agent is starting
   two copies — disable one.

---

## LOCK — file-lock contention on model weights

**Signatures:** `resource busy`, `could not acquire ... lock`,
`file is locked`, `errno 35`.

**What it means.** Multiple processes are trying to open the same weight file
at once, usually because the weights sit on a slow or network volume (NFS,
VirtioFS, SMB) where locking behaves badly.

**Fixes:**

1. Move model files to a local SSD. Network and virtualized filesystems are the
   usual culprit.
2. Stagger startup so only one process loads weights at a time.
3. Kill any orphaned loader process still holding the file.

---

## GPU_MISS — running on CPU instead of the GPU

**Signatures:** `no compatible GPUs were found`, `falling back to CPU`,
`cpu-only`, `unable to load cuda/cublas/hip/rocm`,
`cuda driver version is insufficient`.

**What it means.** The runtime could not use the GPU and silently dropped to
CPU. The model still works — it is just many times slower.

**Fixes:**

1. Confirm the build has GPU support. A CPU-only build of llama.cpp will never
   touch the GPU no matter what flags you pass — it must be compiled with
   `-DGGML_CUDA=ON` (NVIDIA), the ROCm backend (AMD), or Metal (macOS, on by
   default in Mac builds).
2. Confirm drivers: `nvidia-smi` must succeed on NVIDIA; install ROCm for AMD.
3. Set GPU layers above zero — llama.cpp `--n-gpu-layers 99`, Ollama `num_gpu`.
4. In a container, pass `--gpus all` and install the NVIDIA Container Toolkit.
5. On WSL2, GPU passthrough must be enabled with a recent Windows GPU driver.
6. In LM Studio, select the GPU runtime and raise the GPU-offload slider.

See platform-notes.md for the full per-platform detail.

---

## DOWNLOAD — a model download failed

**Signatures:** `401 client error`, `403 forbidden`, `gated repo`,
`repository not found`, `sha256 mismatch`, `checksum`, `incomplete read`,
`connection reset / timed out`.

**What it means.** A pull failed on authentication, permissions, or a dropped
connection.

**Fixes:**

1. `401` / `403` / `gated repo` — the repo needs a token or access approval.
   Set a valid Hugging Face token (`HF_TOKEN`, or `huggingface-cli login`) and,
   for gated models, request access on the model page first.
2. `repository not found` — check the model ID for a typo.
3. `sha256 mismatch` / `checksum` — the file is corrupt; delete it and re-pull.
4. `connection reset` / `timed out` — retry; downloads resume from partial files.

---

## CONTEXT — the prompt exceeds the context window

**Signatures:** `input exceeds context`, `number of tokens ... exceed`,
`context window full`.

**What it means.** The prompt plus conversation history is longer than the
model's configured context window.

**Fixes:**

1. Trim conversation history, or summarize older turns.
2. Raise the context window if memory allows — but a larger window costs memory,
   so watch for OOM afterward.

---

## STALLED_DOWNLOAD — a download is not growing

**Reported when:** an `.incomplete` (Hugging Face) or `*partial*` (Ollama) file
exists and has not changed for at least two minutes, or — under `--watch` — does
not grow between polls.

**Fixes:**

1. Cancel and restart the pull or download; partial files resume rather than
   restart from zero.
2. Check network reachability.
3. Check free disk space — a silent download stall is very often a full disk.

---

## STUCK_LOADING — a server is up but never goes healthy

**Reported when:** a port is open but HTTP does not respond, or llama.cpp's
`/health` keeps reporting `loading model`.

**What it means.** The server started but the model load has not finished.

**Fixes:**

1. Give it time — a large model on a slow disk can take minutes. Use
   `--watch 5` to see whether it is still making progress.
2. If it never finishes, the loader is likely thrashing swap under memory
   pressure. Check the logs for OOM signatures and switch to a smaller model or
   quantization.

---

## Symptoms with no log signature

Some failures leave nothing useful in the logs. Diagnose these by reasoning,
not by grep.

### Slow but working inference

The model runs and answers, just slowly (low tokens/sec, long time to first
token). Likely causes, in order:

1. **Running on CPU.** Check first — see GPU_MISS above. This is the biggest
   single cause of "why is it so slow."
2. **Partial GPU offload / memory pressure.** The model does not fully fit, so
   layers spill to CPU or the system swaps. Use a quant that fully fits.
3. **Context too large.** Long contexts slow every token. Trim it.
4. **Thermal throttling.** A laptop or a poorly cooled GPU throttles under
   sustained load. Watch temperatures; improve airflow.
5. **Long prompt processing.** A very long prompt is slow to ingest even before
   generation starts — separate "time to first token" from "tokens/sec."

### Server up, requests hang

Connections show `up` but a request never returns. Check whether a model is
actually loaded (`ollama ps`), whether the request's context is enormous, and
whether the machine is under memory pressure and swapping.
