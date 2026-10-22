#!/usr/bin/env python3
"""
llm_doctor.py - Local LLM connection listener + log troubleshooter.

Probes the local inference servers (Ollama, LM Studio, llama.cpp, vLLM,
text-generation-webui), scans their logs and the Hugging Face download
cache, and reports why a stack is stuck.

Standard library only. No installs. No network egress beyond localhost.

Usage:
    python3 llm_doctor.py                 # one-shot diagnostic
    python3 llm_doctor.py --json          # machine-readable output
    python3 llm_doctor.py --watch 5       # poll every 5s (the "listener")
    python3 llm_doctor.py --lines 400     # scan more log history
    python3 llm_doctor.py --llamacpp-log /path/to/server.log

Exit code: 0 = nothing wrong found, 1 = at least one problem detected.
"""

import argparse
import glob
import json
import os
import platform
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

VERSION = "1.0.0"

# --------------------------------------------------------------------------
# Service definitions: what we probe and how we read "healthy".
# --------------------------------------------------------------------------
SERVICES = [
    {
        "name": "Ollama",
        "host": "127.0.0.1",
        "port": 11434,
        "health": "http://127.0.0.1:11434/api/tags",
        "extra": "http://127.0.0.1:11434/api/ps",
    },
    {
        "name": "LM Studio",
        "host": "127.0.0.1",
        "port": 1234,
        "health": "http://127.0.0.1:1234/v1/models",
        "extra": None,
    },
    {
        "name": "llama.cpp",
        "host": "127.0.0.1",
        "port": 8080,
        "health": "http://127.0.0.1:8080/health",
        "extra": None,
    },
    {
        "name": "vLLM",
        "host": "127.0.0.1",
        "port": 8000,
        "health": "http://127.0.0.1:8000/health",
        "extra": None,
    },
    {
        "name": "text-gen-webui",
        "host": "127.0.0.1",
        "port": 7860,
        "health": "http://127.0.0.1:7860/",
        "extra": None,
    },
]

# --------------------------------------------------------------------------
# Log failure signatures. Each maps a regex to a problem category.
# Categories are ordered by severity in DIAGNOSIS (see CATEGORY_ORDER).
# --------------------------------------------------------------------------
SIGNATURES = [
    ("OOM", r"cuda (error: )?out of memory"),
    ("OOM", r"\bout of memory\b"),
    ("OOM", r"failed to allocate"),
    ("OOM", r"ggml_metal.*(alloc|insufficient)"),
    ("OOM", r"unable to allocate backend buffer"),
    ("RUNNER_CRASH", r"llama runner process has terminated"),
    ("RUNNER_CRASH", r"signal: killed"),
    ("RUNNER_CRASH", r"exit (status|code) 137"),
    ("RUNNER_CRASH", r"oom-kill|oom killer|killed process"),
    ("MODEL_LOAD", r"error loading model"),
    ("MODEL_LOAD", r"failed to load model"),
    ("MODEL_LOAD", r"unknown model architecture"),
    ("MODEL_LOAD", r"unsupported.{0,20}architecture"),
    ("MODEL_LOAD", r"invalid magic|wrong number of tensors|tensor .* not found"),
    ("GGUF_VERSION", r"unsupported gguf version"),
    ("GGUF_VERSION", r"this (gguf )?format is no longer supported|obsolete"),
    ("GPU_MISS", r"no compatible gpus? (were )?found|no gpu detected"),
    ("GPU_MISS", r"unable to load.{0,30}(cuda|cublas|hip|rocm)"),
    ("GPU_MISS", r"falling back to cpu|cpu[- ]only"),
    ("GPU_MISS", r"cuda driver version is insufficient"),
    ("GPU_MISS", r"no .*metal.*device|metal not supported"),
    ("PORT_CONFLICT", r"address already in use|eaddrinuse"),
    ("PORT_CONFLICT", r"bind.{0,20}(in use|failed)|listen tcp.*in use"),
    ("LOCK", r"resource busy|could not acquire.{0,20}lock|file is locked"),
    ("LOCK", r"errno 35|deadlock"),
    ("CONTEXT", r"(input|prompt).{0,30}exceed.{0,20}context"),
    ("CONTEXT", r"number of tokens.{0,20}exceed|context window.*full"),
    ("DOWNLOAD", r"401 client error|403 forbidden|gated repo|repository not found"),
    ("DOWNLOAD", r"sha256 mismatch|checksum|incomplete read|connection.*(reset|timed out)"),
]
COMPILED = [(cat, re.compile(pat, re.IGNORECASE)) for cat, pat in SIGNATURES]

CATEGORY_ORDER = [
    "RUNNER_CRASH", "OOM", "GGUF_VERSION", "MODEL_LOAD",
    "PORT_CONFLICT", "LOCK", "GPU_MISS", "DOWNLOAD", "CONTEXT",
]

# Short, actionable fixes. The skill's symptom-playbook.md expands these.
FIXES = {
    "RUNNER_CRASH": (
        "The model runner is being killed (exit 137 / 'signal: killed' = the OS "
        "OOM-killer). The model + context does not fit in memory.",
        ["Lower the context window (Ollama default is small; OLLAMA_CONTEXT_LENGTH "
         "or the num_ctx parameter set too high will blow up RAM).",
         "Drop to a smaller quantization (Q5 -> Q4) or a smaller model.",
         "Close other GPU/RAM-heavy apps; re-run llm_doctor while the model loads."],
    ),
    "OOM": (
        "Out of memory while loading or generating. The model, its context/KV "
        "cache, or batch size exceeds available VRAM / unified memory.",
        ["Reduce context length first - it is the cheapest fix.",
         "Use a lighter quant that fully fits (rule of thumb: a 7B model is "
         "~4-5 GB at Q4, ~5-6 GB at Q5, plus KV cache).",
         "On Apple Silicon, raise the GPU memory cap with "
         "'sudo sysctl iogpu.wired_limit_mb=<MB>' (leave 8-16 GB for macOS).",
         "Reduce offloaded GPU layers so the model splits across GPU+CPU."],
    ),
    "GGUF_VERSION": (
        "The model file is a newer (or obsolete) GGUF version than this runtime "
        "understands. The format moved on; the binary did not.",
        ["Update the runtime (llama.cpp, the Ollama app, or LM Studio's runtime).",
         "Or re-download a model file built for your installed version.",
         "Old pre-GGUF 'GGML' files are no longer supported - get a GGUF build."],
    ),
    "MODEL_LOAD": (
        "The model failed to load - corrupt/incomplete file, or an architecture "
        "this runtime does not support.",
        ["Re-pull / re-download the model; a truncated file fails the same way.",
         "Verify the file size matches the source repo.",
         "Confirm the runtime supports the model architecture; update if newer."],
    ),
    "PORT_CONFLICT": (
        "The server cannot bind its port - another process already holds it "
        "(often a previous instance that did not exit).",
        ["Find the holder: 'lsof -i :<port>' (macOS/Linux) or "
         "'netstat -ano | findstr <port>' (Windows), then stop it.",
         "Or start the server on a different port."],
    ),
    "LOCK": (
        "File-lock contention on the model weights - usually weights on a slow "
        "or network volume with multiple processes loading at once.",
        ["Move model files to a local SSD (avoid NFS / VirtioFS / network shares).",
         "Stagger startup so only one process loads weights at a time.",
         "Confirm no orphaned loader process is still holding the file."],
    ),
    "GPU_MISS": (
        "The runtime is not using the GPU and fell back to CPU - slow.",
        ["Confirm the GPU build: llama.cpp must be compiled with -DGGML_CUDA=ON "
         "(NVIDIA) or the ROCm/Metal backend; a CPU build never uses the GPU.",
         "Check drivers: 'nvidia-smi' must succeed; install ROCm for AMD.",
         "Set GPU layers > 0 (llama.cpp '--n-gpu-layers 99', Ollama 'num_gpu').",
         "In a container, pass '--gpus all'; on WSL2, enable CUDA passthrough.",
         "In LM Studio, pick the GPU runtime and raise the GPU-offload slider."],
    ),
    "DOWNLOAD": (
        "A model download failed or stalled - auth, gated repo, or a dropped "
        "connection leaving a partial file.",
        ["For gated/private repos, set a valid HF token (HF_TOKEN / huggingface-cli login).",
         "Delete the '.incomplete' file and re-download to resume cleanly.",
         "Check free disk space - silent download stalls are often a full disk."],
    ),
    "CONTEXT": (
        "The prompt/conversation exceeds the model's context window.",
        ["Trim conversation history or raise the context window if memory allows.",
         "Note: a bigger context window costs memory - watch for OOM after raising it."],
    ),
    "STALLED_DOWNLOAD": (
        "A download is in progress but not growing - the connection is stalled.",
        ["Cancel and restart the pull/download; partial files resume.",
         "Check network reachability and free disk space."],
    ),
    "STUCK_LOADING": (
        "A server is up but stuck loading a model - the port answers but health "
        "never goes green.",
        ["Large models on slow disks can take minutes - watch with '--watch 5'.",
         "If it never finishes, the loader is likely thrashing swap (memory "
         "pressure) - check the logs for OOM and use a smaller model/quant."],
    ),
}


# --------------------------------------------------------------------------
# Connection probing
# --------------------------------------------------------------------------
def probe(service, timeout):
    """Return a status dict for one service."""
    name, host, port = service["name"], service["host"], service["port"]
    result = {"name": name, "port": port, "state": "down", "detail": "", "info": {}}

    # Fast TCP check first: distinguishes "nothing listening" from "hung".
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        sock.close()
    except (ConnectionRefusedError, OSError):
        result["state"] = "down"
        result["detail"] = "not running (connection refused / port closed)"
        return result
    except socket.timeout:
        result["state"] = "stuck"
        result["detail"] = "port filtered or unresponsive (TCP connect timed out)"
        return result

    # Port is open - try the HTTP health endpoint.
    try:
        req = urllib.request.Request(service["health"], headers={"Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(8192).decode("utf-8", "replace")
        result["state"] = "up"
        result["detail"] = "running"
        _enrich(result, service, body, timeout)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read(2048).decode("utf-8", "replace")
        except Exception:
            pass
        if "loading" in body.lower() or e.code == 503:
            result["state"] = "stuck"
            result["detail"] = "server up but still loading a model (HTTP %s)" % e.code
        else:
            result["state"] = "up"
            result["detail"] = "responding (HTTP %s)" % e.code
    except (socket.timeout, urllib.error.URLError) as e:
        # Port open, HTTP hangs/fails -> stuck, not down.
        result["state"] = "stuck"
        reason = getattr(e, "reason", e)
        result["detail"] = "port open but HTTP unresponsive (%s)" % reason
    return result


def _enrich(result, service, body, timeout):
    """Pull a little extra detail from a healthy server."""
    try:
        data = json.loads(body)
    except (ValueError, TypeError):
        data = None
    if service["name"] == "Ollama" and isinstance(data, dict):
        models = data.get("models", [])
        result["info"]["models_installed"] = len(models)
        if service.get("extra"):
            try:
                with urllib.request.urlopen(service["extra"], timeout=timeout) as r:
                    ps = json.loads(r.read(8192).decode("utf-8", "replace"))
                running = ps.get("models", [])
                result["info"]["models_loaded"] = len(running)
                procs = [m.get("name", "?") for m in running]
                if procs:
                    result["info"]["loaded"] = ", ".join(procs)
            except Exception:
                pass
    elif service["name"] == "LM Studio" and isinstance(data, dict):
        result["info"]["models_loaded"] = len(data.get("data", []))
    elif service["name"] == "llama.cpp" and isinstance(data, dict):
        if data.get("status"):
            result["info"]["status"] = data["status"]


# --------------------------------------------------------------------------
# Log discovery
# --------------------------------------------------------------------------
def candidate_logs(args):
    """Map tool name -> list of existing log file paths."""
    home = Path.home()
    found = {}

    def add(tool, paths):
        existing = [str(p) for p in paths if p and Path(p).is_file()]
        if existing:
            found[tool] = existing

    # Ollama
    ollama = [
        home / ".ollama" / "logs" / "server.log",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Ollama" / "server.log",
    ]
    if args.ollama_log:
        ollama.insert(0, Path(args.ollama_log))
    add("Ollama", ollama)

    # LM Studio - logs live under ~/.lmstudio, layout varies by version.
    lms = []
    if args.lmstudio_log_dir:
        lms += [Path(p) for p in glob.glob(str(Path(args.lmstudio_log_dir) / "**" / "*.log"), recursive=True)]
    for pat in ("**/server-logs/*.log", "**/*.log"):
        lms += [Path(p) for p in glob.glob(str(home / ".lmstudio" / pat), recursive=True)]
    lms = sorted(set(lms), key=lambda p: p.stat().st_mtime if p.exists() else 0, reverse=True)[:3]
    add("LM Studio", lms)

    # llama.cpp - no standard location; user must point us at it.
    if args.llamacpp_log:
        add("llama.cpp", [Path(args.llamacpp_log)])

    # System log hint for OOM-killer events (Linux only, best-effort).
    syslog = [Path("/var/log/syslog"), Path("/var/log/kern.log")]
    add("system", syslog)

    return found


def scan_log(path, lines):
    """Scan the last `lines` lines of a log file for known signatures."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            tail = fh.readlines()[-lines:]
    except OSError as e:
        return {"error": str(e), "hits": []}
    hits = {}
    for ln in tail:
        matched = set()  # count each category at most once per line
        for cat, rx in COMPILED:
            if cat in matched:
                continue
            if rx.search(ln):
                matched.add(cat)
                rec = hits.setdefault(cat, {"count": 0, "sample": ""})
                rec["count"] += 1
                if not rec["sample"]:
                    rec["sample"] = ln.strip()[:200]
    return {"error": None, "hits": [
        {"category": c, "count": v["count"], "sample": v["sample"]}
        for c, v in hits.items()
    ]}


# --------------------------------------------------------------------------
# Download stall detection
# --------------------------------------------------------------------------
def hf_cache_root(args):
    if args.hf_home:
        return Path(args.hf_home)
    for var in ("HF_HUB_CACHE", "HUGGINGFACE_HUB_CACHE", "HF_HOME"):
        v = os.environ.get(var)
        if v:
            p = Path(v)
            return p / "hub" if (var == "HF_HOME" and (p / "hub").exists()) else p
    return Path.home() / ".cache" / "huggingface" / "hub"


def find_partial_downloads(args):
    """Find in-progress / partial downloads (HF cache + Ollama blobs)."""
    partials = []
    seen = set()
    now = time.time()

    hf = hf_cache_root(args)
    if hf.exists():
        for f in glob.glob(str(hf / "**" / "*.incomplete"), recursive=True):
            if f in seen:
                continue
            seen.add(f)
            p = Path(f)
            try:
                st = p.stat()
            except OSError:
                continue
            partials.append({
                "tool": "HuggingFace", "path": str(p),
                "size_mb": round(st.st_size / 1048576, 1),
                "age_min": round((now - st.st_mtime) / 60, 1),
            })

    ollama_blobs = Path(os.environ.get("OLLAMA_MODELS", "")) if os.environ.get("OLLAMA_MODELS") \
        else Path.home() / ".ollama" / "models" / "blobs"
    if ollama_blobs.exists():
        for f in glob.glob(str(ollama_blobs / "*partial*")):
            if f in seen:
                continue
            seen.add(f)
            p = Path(f)
            try:
                st = p.stat()
            except OSError:
                continue
            partials.append({
                "tool": "Ollama", "path": str(p),
                "size_mb": round(st.st_size / 1048576, 1),
                "age_min": round((now - st.st_mtime) / 60, 1),
            })
    return partials


# --------------------------------------------------------------------------
# Diagnosis
# --------------------------------------------------------------------------
def diagnose(connections, logs, partials, prev_partials=None):
    """Build a ranked list of problems from all collected evidence."""
    categories = {}  # category -> evidence list

    for tool, scan in logs.items():
        for h in scan.get("hits", []):
            categories.setdefault(h["category"], []).append(
                "%s log: %s (x%d) - %s" % (tool, h["category"], h["count"], h["sample"])
            )

    for c in connections:
        if c["state"] == "stuck":
            categories.setdefault("STUCK_LOADING", []).append(
                "%s: %s" % (c["name"], c["detail"])
            )

    for p in partials:
        stalled = p["age_min"] >= 2
        if prev_partials is not None:
            prev = next((q for q in prev_partials if q["path"] == p["path"]), None)
            if prev is not None:
                stalled = p["size_mb"] <= prev["size_mb"]
        if stalled:
            categories.setdefault("STALLED_DOWNLOAD", []).append(
                "%s download not growing: %s (%.1f MB, idle %.1f min)"
                % (p["tool"], os.path.basename(p["path"]), p["size_mb"], p["age_min"])
            )

    order = CATEGORY_ORDER + ["STUCK_LOADING", "STALLED_DOWNLOAD"]
    ranked = []
    for cat in order:
        if cat in categories:
            cause, fixes = FIXES.get(cat, ("Unrecognized condition.", []))
            ranked.append({
                "category": cat, "cause": cause,
                "fixes": fixes, "evidence": categories[cat],
            })
    return ranked


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------
ICON = {"up": "[ OK ]", "down": "[ -- ]", "stuck": "[STUCK]"}


def collect(args):
    """Run one full pass; return a result dict."""
    connections = [probe(s, args.timeout) for s in SERVICES]
    logs = {}
    for tool, paths in candidate_logs(args).items():
        if tool == "system" and platform.system() != "Linux":
            continue
        merged = {"error": None, "hits": []}
        seen = {}
        for path in paths:
            scan = scan_log(path, args.lines)
            for h in scan["hits"]:
                key = h["category"]
                if key in seen:
                    seen[key]["count"] += h["count"]
                else:
                    seen[key] = dict(h)
        merged["hits"] = list(seen.values())
        merged["paths"] = paths
        logs[tool] = merged
    partials = find_partial_downloads(args)
    return {"connections": connections, "logs": logs, "partials": partials}


def render_text(snap, diagnosis):
    out = []
    out.append("Local LLM Doctor v%s  -  %s" % (VERSION, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    out.append("host: %s %s" % (platform.system(), platform.machine()))
    out.append("")
    out.append("CONNECTIONS")
    for c in snap["connections"]:
        info = ""
        if c["info"]:
            info = "  {%s}" % ", ".join("%s=%s" % (k, v) for k, v in c["info"].items())
        out.append("  %-7s %-16s :%-6d %s%s" %
                    (ICON[c["state"]], c["name"], c["port"], c["detail"], info))
    out.append("")
    out.append("LOGS")
    if not snap["logs"]:
        out.append("  (no known log files found - pass --ollama-log / --llamacpp-log "
                    "/ --lmstudio-log-dir if your logs live elsewhere)")
    for tool, scan in snap["logs"].items():
        paths = ", ".join(scan.get("paths", []))
        out.append("  %s  [%s]" % (tool, paths))
        if not scan["hits"]:
            out.append("    no known failure signatures in last lines scanned")
        for h in scan["hits"]:
            out.append("    ! %-14s x%-3d  %s" % (h["category"], h["count"], h["sample"]))
    out.append("")
    out.append("DOWNLOADS")
    if not snap["partials"]:
        out.append("  no partial / in-progress downloads found")
    for p in snap["partials"]:
        out.append("  %s  %s  (%.1f MB, idle %.1f min)" %
                    (p["tool"], os.path.basename(p["path"]), p["size_mb"], p["age_min"]))
    out.append("")
    out.append("DIAGNOSIS")
    if not diagnosis:
        any_up = any(c["state"] == "up" for c in snap["connections"])
        if any_up:
            out.append("  No problems detected. Servers are reachable and logs are clean.")
        else:
            out.append("  No failure signatures found, but no server is running either.")
            out.append("  -> Start your inference server, then re-run llm_doctor.")
    else:
        for i, d in enumerate(diagnosis, 1):
            tag = "PRIMARY" if i == 1 else "also"
            out.append("  [%s] %s" % (tag, d["category"]))
            out.append("    %s" % d["cause"])
            for fx in d["fixes"]:
                out.append("      - %s" % fx)
            for ev in d["evidence"][:3]:
                out.append("      evidence: %s" % ev)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(
        description="Local LLM connection listener + log troubleshooter.")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    ap.add_argument("--watch", type=float, metavar="SECONDS",
                    help="poll continuously every SECONDS (Ctrl-C to stop)")
    ap.add_argument("--lines", type=int, default=200,
                    help="log lines to scan from the tail (default 200)")
    ap.add_argument("--timeout", type=float, default=3.0,
                    help="per-probe timeout in seconds (default 3)")
    ap.add_argument("--ollama-log", help="explicit Ollama server.log path")
    ap.add_argument("--lmstudio-log-dir", help="explicit LM Studio log directory")
    ap.add_argument("--llamacpp-log", help="explicit llama.cpp server log path")
    ap.add_argument("--hf-home", help="explicit Hugging Face hub cache directory")
    args = ap.parse_args()

    if args.watch:
        prev_partials = None
        try:
            while True:
                snap = collect(args)
                diagnosis = diagnose(snap["connections"], snap["logs"],
                                     snap["partials"], prev_partials)
                prev_partials = snap["partials"]
                ts = datetime.now().strftime("%H:%M:%S")
                if args.json:
                    print(json.dumps({"time": ts, "snapshot": snap,
                                       "diagnosis": diagnosis}))
                else:
                    line = " | ".join("%s:%s" % (c["name"], c["state"])
                                       for c in snap["connections"])
                    flag = ""
                    if diagnosis:
                        flag = "  <-- %s" % diagnosis[0]["category"]
                    print("[%s] %s%s" % (ts, line, flag))
                sys.stdout.flush()
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\n--- final diagnostic ---")
            snap = collect(args)
            diagnosis = diagnose(snap["connections"], snap["logs"], snap["partials"])
            print(render_text(snap, diagnosis))
            sys.exit(1 if diagnosis else 0)

    snap = collect(args)
    diagnosis = diagnose(snap["connections"], snap["logs"], snap["partials"])
    if args.json:
        print(json.dumps({"version": VERSION, "snapshot": snap,
                           "diagnosis": diagnosis}, indent=2))
    else:
        print(render_text(snap, diagnosis))
    sys.exit(1 if diagnosis else 0)


if __name__ == "__main__":
    main()
