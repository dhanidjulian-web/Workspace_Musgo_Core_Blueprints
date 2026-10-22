# Local LLM Troubleshooter

A focused diagnostic skill for stuck local LLM stacks. It bundles a working
tool — `scripts/llm_doctor.py` — that probes your inference servers, scans
their logs, and tells you why things are stuck.

## What's inside

- `SKILL.md` — instructions for the agent: run the script, read the evidence,
  walk the user through fixes.
- `scripts/llm_doctor.py` — connection listener + log analyzer (stdlib Python,
  no installs, no network egress beyond localhost).
- `references/symptom-playbook.md` — cause-and-fix detail for every problem
  category the script reports.
- `references/platform-notes.md` — OS, hardware, and per-tool specifics
  (Apple Silicon, NVIDIA, AMD, WSL2, Docker; Ollama, llama.cpp, LM Studio,
  Hugging Face).
- `agents/openai.yaml` — agent interface configuration.

## Run the script directly

```
python3 scripts/llm_doctor.py            # one-shot diagnostic
python3 scripts/llm_doctor.py --json     # machine-readable output
python3 scripts/llm_doctor.py --watch 5  # poll every 5s
```

Point it at non-default log locations when needed:

```
python3 scripts/llm_doctor.py \
  --ollama-log ~/.ollama/logs/server.log \
  --llamacpp-log ~/llamacpp/server.log \
  --lmstudio-log-dir ~/.lmstudio \
  --hf-home ~/.cache/huggingface/hub
```

It probes Ollama (:11434), LM Studio (:1234), llama.cpp (:8080), vLLM (:8000),
and text-generation-webui (:7860). Exit code is 1 when a problem is found, 0
when nothing is wrong.

## Requirements

- Python 3.8 or newer. No third-party packages.
- Run it on the machine where the local LLM stack lives.

## Scope

This skill diagnoses; it does not act. It makes no writes, restarts no
services, and edits no configs. For end-to-end hardware selection, model
curation, and multi-machine inference design, see the companion skill
**Local LLM & Agent Setup: Soup to Nuts**.
