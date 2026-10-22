---
name: local-llm-troubleshooter
description: Diagnose why a local LLM stack is stuck or broken across Ollama, LM Studio, llama.cpp, vLLM, and Hugging Face downloads. Runs a bundled diagnostic script that probes the inference servers, scans their logs for known failure signatures, and detects stalled downloads, then walks the user through targeted fixes. Use when a local model will not load, inference is slow, the GPU sits idle, an inference server is unreachable, a runner keeps crashing, or a model download hangs.
_agensi: "6c6d3f90-a209-475d-a394-01e947ef3f22"
---

# Local LLM Troubleshooter

## Purpose

Find out why a local inference stack is stuck — and fix it — instead of guessing. This skill turns a vague "my local model is broken" into a specific diagnosis backed by connection state and log evidence.

## How it works

The skill bundles `scripts/llm_doctor.py`, a connection listener and log analyzer. The script is the sensor; you are the diagnosing agent. Run it, read its evidence, then translate the findings into ordered fixes for the user. The script never changes the user's system — it only probes localhost and reads local logs.

## Step 1 — Run the diagnostic

From the skill directory, run:

```
python3 scripts/llm_doctor.py --json
```

Use `--json` so you can parse the result reliably; the plain text form is for the user.

Flags worth knowing:

- `--watch 5` — poll every 5 seconds. Use this when the user reports an intermittent hang or a download that may be stalling, so you can watch a server stay stuck or a partial file fail to grow.
- `--lines 400` — scan more log history when the failure happened a while ago.
- `--ollama-log PATH`, `--llamacpp-log PATH`, `--lmstudio-log-dir DIR`, `--hf-home DIR` — point the script at logs or caches in non-default locations. llama.cpp has no standard log path, so always ask the user where its server output goes if llama.cpp is the suspect.

The script exits 1 when it finds a problem and 0 when it does not.

## Step 2 — Read the evidence

The output has four parts:

- **CONNECTIONS** — per server, one of three states. `down` means nothing is listening (server not started). `stuck` is the important one: the port is open but HTTP does not respond, or a server reports it is still loading a model. `up` means healthy.
- **LOGS** — failure-signature hits per tool, grouped into categories (`OOM`, `RUNNER_CRASH`, `MODEL_LOAD`, `GGUF_VERSION`, `GPU_MISS`, `PORT_CONFLICT`, `LOCK`, `DOWNLOAD`, `CONTEXT`).
- **DOWNLOADS** — partial Hugging Face and Ollama files, with size and idle time. An idle partial file is a stalled download.
- **DIAGNOSIS** — categories ranked by severity, each with a cause and starter fixes. The first is the most likely root cause.

## Step 3 — Map findings to fixes

Read `references/symptom-playbook.md` for the full cause-and-fix detail behind each category, including symptoms that leave no log signature (slow-but-working inference, a server stuck loading). Read `references/platform-notes.md` for the OS- and hardware-specific commands — Apple Silicon, NVIDIA, AMD, Windows/WSL2, Docker — and for tool-specific settings in Ollama, llama.cpp, LM Studio, and Hugging Face.

Give the user an ordered fix list, cheapest and most likely first. For memory failures that almost always means: reduce context window, then drop quantization, then use a smaller model.

## Step 4 — Apply one fix, then verify

Tell the user to change exactly one thing, then re-run `python3 scripts/llm_doctor.py`. Confirm the signature is gone before moving on. Changing several things at once hides which fix worked.

## Intake when the script cannot run

If the user cannot run the script, ask for: which tool and version, the exact symptom, the full error text, hardware (chip, RAM, GPU/VRAM), the model and its quantization, and the configured context size. Never ask for API keys, Hugging Face tokens, private endpoint URLs, or user-identifying log exports.

## Output format

Return:

1. **Verdict** — running, stuck, or down.
2. **What's stuck** — the specific server, model, or download.
3. **Most likely cause** — the primary diagnosis with its evidence.
4. **Fix steps** — ordered, cheapest first, with exact commands.
5. **Verification** — what to re-check after the fix.

## Constraints

This skill diagnoses; it does not act. The script makes no writes, restarts no services, and edits no configs — the user applies the fixes. It is a fast preflight and triage tool, not a replacement for full inference-stack architecture. For end-to-end hardware selection, model curation, and multi-machine inference design, defer to the Local LLM & Agent Setup skill.
