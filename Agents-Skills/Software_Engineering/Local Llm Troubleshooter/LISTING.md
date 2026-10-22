# Local LLM Troubleshooter

## Title
Local LLM Troubleshooter

## Summary
Find out why your local LLM stack is stuck — and fix it — instead of guessing.
Bundles a working diagnostic tool that probes Ollama, LM Studio, llama.cpp, and
vLLM, scans their logs for known failure signatures, and catches stalled
Hugging Face downloads, then walks you through the fix.

## Full Description

Local LLMs fail in predictable ways: a runner gets OOM-killed at 3am, the GPU
quietly sits idle while everything runs on CPU, a model download stalls at 80%,
a server is "up" but never answers. This skill turns a vague "it's broken" into
a specific diagnosis backed by connection state and log evidence.

It ships `llm_doctor.py`, a connection listener and log analyzer:

- **Probes every local inference server** — Ollama, LM Studio, llama.cpp, vLLM,
  text-generation-webui — and tells the difference between *not running* and
  *stuck* (port open, never answers, or still loading a model).
- **Scans the logs** of Ollama, LM Studio, llama.cpp, and the system journal
  for known failure signatures: out-of-memory, runner crashes, model-load
  errors, GGUF version mismatches, port conflicts, file-lock contention, and
  GPU fallback.
- **Catches stalled downloads** — partial Hugging Face and Ollama files that
  have stopped growing.
- **Ranks the diagnosis** by severity and hands back ordered, cheapest-first
  fixes.

A `--watch` mode polls continuously so you can catch intermittent hangs and
downloads that stall mid-stream.

**What you'll get:**
- A diagnostic script that runs anywhere Python does — no installs, no network
  egress beyond localhost, no writes to your system.
- A symptom playbook with cause-and-fix detail for every failure category,
  including the slow-but-working case that leaves no log signature.
- Platform notes for Apple Silicon, NVIDIA, AMD, WSL2, and Docker, plus
  tool-specific settings for Ollama, llama.cpp, LM Studio, and Hugging Face.

**Who this is for:**
- Anyone running local models who is tired of guessing why one stopped working.
- Builders who want a fast triage step before a deep debugging session.

## Compatibility

- **Operating Systems:** macOS 12+, Linux, Windows 10/11 (incl. WSL2)
- **Inference stacks:** Ollama, LM Studio, llama.cpp, vLLM, text-generation-webui
- **Sources:** Hugging Face hub cache, Ollama model blobs
- **Requires:** Python 3.8+ (standard library only). Run on the host where the
  local LLM stack lives.

## Key Differentiators

- **A working tool, not just advice** — ships a real diagnostic script, not a
  prose checklist.
- **Down vs stuck** — distinguishes a server that never started from one that
  is hung or still loading, which point to completely different fixes.
- **Evidence-driven** — every diagnosis is backed by a log line or a connection
  state, so fixes are targeted instead of speculative.
- **Safe by design** — probes localhost and reads logs only; no writes, no
  service restarts, no config edits, no network egress.
- **Pairs with the deep-dive** — a fast triage companion to the Local LLM &
  Agent Setup skill.

## Permissions

- **Read:** SKILL.md, references (symptom-playbook.md, platform-notes.md),
  scripts/llm_doctor.py
- **Shell:** runs the bundled Python script, which reads local log files and
  makes HTTP requests to localhost inference ports
- **No write, no outbound network, no environment modification**

## Price
$5.00

## Tags
local-llm, troubleshooting, ollama, llama-cpp, lm-studio, vllm, huggingface,
diagnostics, gpu, oom, inference, debugging, log-analysis, mac, cuda
