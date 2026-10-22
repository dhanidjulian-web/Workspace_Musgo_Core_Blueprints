---
name: enterprise-multi-agent-automation
description: >
  Production-grade multi-agent orchestration framework for Claude Code.
  Covers task routing, denbun (handoff document) protocol, retry logic,
  rate-limit guards, structured logging, and self-healing — all battle-tested
  patterns extracted from real multi-agent deployments. Use when you need to
  orchestrate more than two Claude agents reliably in a single project.
_agensi: "f86ce7af-b586-4be3-a645-c29d261106eb"
---

# Enterprise Multi-Agent Automation

Battle-tested orchestration framework for running parallel Claude Code agents
at production scale. Covers every failure mode you will hit the moment you go
beyond two agents: task routing, graceful handoffs, retry / rate-limit logic,
structured logging, and automated self-healing.

## When to use

- You need 3+ Claude Code agents working in parallel on the same codebase
- Your multi-agent loop keeps breaking because one agent times out or goes off-task
- You need reliable handoffs between agents across context-compaction events
- You want structured audit logs and cost visibility for an agentic pipeline
- You are building a product on top of Claude Code and need a repeatable harness

---

## Core Concepts

### 1. Denbun Protocol — Agent Handoff Documents

The single biggest reliability win in any multi-agent system is externalising
all in-flight state into a versioned handoff document ("denbun").
When an agent is killed, compacted, or replaced, the next agent reads the
denbun and resumes without loss.

**File layout** (one denbun per task):

```
queue/denbun/denbun_<task_id>.md    ← active task state (source of truth)
queue/denbun/denbun.md              ← index of all active tasks
queue/denbun/archive/               ← completed tasks
```

**Minimal denbun frontmatter:**

```yaml
---
denbun_id: denbun_feature_auth
task_id: feat_auth_v2
owner: orchestrator→agent3
origin: "User request: add OAuth2 login"
status: in_progress          # assigned | in_progress | blocked | completed
assignable: true
updated: 2026-06-10T09:00
---
```

**Body sections to maintain:**

```markdown
## Current position
Implemented token refresh (auth/refresh.ts:42). Next: write unit tests.

## Next action
Run `pytest tests/test_auth.py` and fix failures.

## Blockers
None.

## Work log
- 09:05 Read existing auth module — no refresh logic found
- 09:20 Implemented refresh endpoint
- 09:35 Updated denbun — handing off to test agent

## Success procedures (reproducing this later)
- Token stored in Keychain item `oauth2-token`; load with `security find-generic-password -w`
- Rate-limit window is 60 s; always call `await rate_limit_guard()` before each request
```

**Rules:**
- Update denbun on every report, not just at task end.
- Never write instructions into the queue YAML itself — YAML points to the denbun; denbun holds the detail.
- On compaction/restart: read denbun first, dashboard second.

---

### 2. Task Routing — Sending Work to the Right Agent

Routing logic lives in a single shell function. It checks backend health
before dispatching and falls back cleanly.

```bash
# harness/task_router.sh

route_task() {
    local description="$1"
    local hint="${2:-auto}"          # gemma4 | claude_code | remo1 | codex
    local needs_net="${3:-false}"

    # 1. Explicit hint takes priority
    case "$hint" in
        gemma4)
            is_backend_available gemma4 && { dispatch_gemma4 "$description"; return; }
            ;;
        remo1)
            is_backend_available remo1 && { dispatch_remo1 "$description"; return; }
            ;;
        codex)
            dispatch_codex "$description"; return
            ;;
    esac

    # 2. Auto-selection: network tasks → remo1, heavy reasoning → claude_code
    if [[ "$needs_net" == "true" ]] && is_backend_available remo1; then
        dispatch_remo1 "$description"
    else
        dispatch_claude_code "$description"
    fi
}

is_backend_available() {
    local backend="$1"
    [[ "$backend" == "claude_code" ]] && return 0       # always available
    grep -q "${backend}:.*online" "$HARNESS_HEALTH" 2>/dev/null
}
```

**Key decisions:**
- `claude_code` is the unconditional fallback — it is always available.
- `gemma4` / local LLM: free tier for simple, repetitive subtasks (token savings).
- `remo1`: for browser automation, deploys, or anything that must not run on the main machine.
- `codex`: pure code generation without network access.

---

### 3. Retry Logic with Exponential Back-off

Every external call in an agentic pipeline will eventually fail.
Wrap them uniformly:

```python
# patterns/retry.py

import time, random, logging
from functools import wraps

logger = logging.getLogger(__name__)

def with_retry(max_attempts: int = 3, base_delay: float = 2.0,
               max_delay: float = 60.0, backoff: float = 2.0):
    """Decorator: exponential back-off with full jitter."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    if attempt == max_attempts:
                        logger.error("FAILED after %d attempts: %s", max_attempts, exc)
                        raise
                    jitter = random.uniform(0, delay * 0.3)
                    sleep_for = min(delay + jitter, max_delay)
                    logger.warning("Attempt %d/%d failed (%s). Retry in %.1fs",
                                   attempt, max_attempts, exc, sleep_for)
                    time.sleep(sleep_for)
                    delay = min(delay * backoff, max_delay)
        return wrapper
    return decorator

# Usage
@with_retry(max_attempts=3, base_delay=5.0)
def call_external_api(payload):
    ...
```

**Rules:**
- Never retry on 403 / authentication errors — stop immediately and report.
- Always log attempt number, exception message, and next sleep duration.
- Cap total sleep with `max_delay` to avoid infinite hangs.

---

### 4. Rate-Limit Guard

Prevents burst failures when an agent calls an API in a tight loop.

```python
# patterns/rate_limit_guard.py

import asyncio, time
from collections import deque

class RateLimitGuard:
    """Token-bucket rate limiter for async agent loops."""

    def __init__(self, calls_per_minute: int = 20):
        self._window = 60.0
        self._limit = calls_per_minute
        self._timestamps: deque = deque()

    async def acquire(self):
        now = time.monotonic()
        # Drop timestamps outside the window
        while self._timestamps and now - self._timestamps[0] >= self._window:
            self._timestamps.popleft()

        if len(self._timestamps) >= self._limit:
            sleep_for = self._window - (now - self._timestamps[0])
            await asyncio.sleep(sleep_for + 0.1)

        self._timestamps.append(time.monotonic())

# Usage
guard = RateLimitGuard(calls_per_minute=15)

async def agent_loop():
    for task in task_queue:
        await guard.acquire()
        result = await process(task)
```

---

### 5. Structured Logging — Machine-Readable Agent Audit Trail

Every agent action should produce a structured log line. This lets you:
- Calculate token cost per task
- Identify which agent caused a failure
- Replay decisions for debugging

```python
# patterns/agent_logger.py

import json, logging, sys, time
from typing import Any

class AgentLogger:
    """JSON-lines logger for multi-agent audit trails."""

    def __init__(self, agent_id: str, log_path: str):
        self._agent_id = agent_id
        self._fh = open(log_path, "a", buffering=1)   # line-buffered

    def log(self, event: str, **kwargs: Any):
        record = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "agent": self._agent_id,
            "event": event,
            **kwargs,
        }
        self._fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def close(self):
        self._fh.close()

# Usage
log = AgentLogger("agent3", "/tmp/agent3.jsonl")
log.log("task_start", task_id="feat_auth_v2", model="claude-sonnet-4-6")
log.log("api_call", endpoint="/token", status=200, latency_ms=320)
log.log("task_end",  task_id="feat_auth_v2", outcome="success")
```

**Log each of:** `task_start`, `task_end`, external API calls (endpoint + status + latency), errors, and handoff events.

---

### 6. Self-Healing — Automated Recovery from Common Failures

Agents die. The harness must detect and recover without human intervention.

```bash
# harness/self_healer.sh  (called on-demand, NOT polling)

heal_agent() {
    local agent="$1"            # e.g. "agent3"
    local pane="$2"             # e.g. "multiagent2:0.3"
    local cooldown_file="/tmp/.healer_${agent}_cooldown"

    # Respect 10-minute cooldown to avoid restart loops
    if [[ -f "$cooldown_file" ]]; then
        local age=$(( $(date +%s) - $(stat -f%m "$cooldown_file" 2>/dev/null || echo 0) ))
        if (( age < 600 )); then
            echo "[healer] ${agent}: in cooldown (${age}s). Skip."
            return 1
        fi
    fi

    echo "[healer] Restarting ${agent} on ${pane}"
    tmux send-keys -t "$pane" "" Enter   # Ctrl-C current process
    sleep 2
    tmux send-keys -t "$pane" "claude --resume" Enter
    touch "$cooldown_file"
    echo "[healer] ${agent}: restart issued"
}

# Called by orchestrator when an agent's YAML report is stale > 15 min
check_and_heal() {
    local agent="$1" pane="$2" report_yaml="$3"
    local last_modified
    last_modified=$(stat -f%m "$report_yaml" 2>/dev/null || echo 0)
    local age=$(( $(date +%s) - last_modified ))

    if (( age > 900 )); then   # 15 minutes
        echo "[healer] ${agent} report stale ${age}s — healing"
        heal_agent "$agent" "$pane"
    fi
}
```

---

### 7. Multi-Agent Communication Protocol

Agents communicate via YAML files + tmux send-keys (event-driven, no polling).

**Orchestrator → Agent (minimal task YAML):**

```yaml
# queue/tasks/agent3.yaml
worker_id: agent3
task_id: feat_auth_v2
model: sonnet
status: assigned
read_denbun: [denbun_feature_auth]
objective: |
  Implement OAuth2 token refresh in auth/refresh.ts.
  Full context in denbun_feature_auth.
on_complete: Send results to orchestrator pane 0.0.
```

**Agent → Orchestrator (report YAML):**

```yaml
# queue/reports/agent3_report.yaml
worker_id: agent3
task_id: feat_auth_v2
status: completed          # completed | failed | blocked
summary: "Token refresh implemented and tested. auth/refresh.ts:42"
next_action: "Integration test needed"
updated: 2026-06-10T10:30
```

**tmux notification (two-step — mandatory):**

```bash
# Step 1: send message text
tmux send-keys -t multiagent2:0.0 'agent3: feat_auth_v2 完了。auth/refresh.ts:42 実装済。'
# Step 2: send Enter in a SEPARATE shell call
tmux send-keys -t multiagent2:0.0 Enter
```

⚠️ Always split into two separate Bash calls. Combining them in one call
causes the Enter to be swallowed by the message text.

---

### 8. Health-Check Pattern

```bash
# harness/health_check.sh

check_remo1_connection() {
    ssh -o ConnectTimeout=5 -o BatchMode=yes remo1 "echo ok" &>/dev/null
}

check_all_backends() {
    local health_file="$PROJECT_ROOT/status/harness_health.yaml"
    {
        printf "backends:\n"
        if check_remo1_connection; then
            printf "  remo1: online\n"
        else
            printf "  remo1: offline\n"
        fi
        printf "  claude_code: online\n"     # always
        printf "checked_at: %s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    } > "$health_file"
}
```

---

## Quick-Start Checklist

1. **Create a denbun** for every new task before assigning it to an agent.
2. **Route via `route_task()`** — never hard-code a backend.
3. **Wrap all external calls** with `@with_retry`.
4. **Throttle all loops** with `RateLimitGuard`.
5. **Log every agent action** as a JSON line.
6. **Notify via tmux** in two separate shell calls (message → Enter).
7. **Heal stale agents** by checking report YAML modification time.
8. **Archive denbun** when task is `completed`; update the index.

---

## File Structure

```
harness/
  shutsujin_harness.sh    ← master startup (phase-by-phase init)
  task_router.sh          ← route_task() + is_backend_available()
  self_healer.sh          ← heal_agent() + check_and_heal()
  health_check.sh         ← check_remo1_connection() + check_all_backends()
  harness_registry.sh     ← agent registration + status tracking
  obsidian_bridge.sh      ← write healer events to Obsidian daily note

queue/
  denbun/                 ← task handoff documents (source of truth)
  tasks/                  ← orchestrator → agent instructions (minimal)
  reports/                ← agent → orchestrator results

patterns/
  retry.py                ← with_retry() decorator
  rate_limit_guard.py     ← RateLimitGuard async class
  agent_logger.py         ← AgentLogger JSON-lines logger

status/
  harness_health.yaml     ← backend online/offline state
  master_status.yaml      ← overall pipeline progress
```

---

## Tags

multi-agent, orchestration, claude-code, task-routing, retry, rate-limiting,
structured-logging, self-healing, denbun, handoff, tmux, harness, automation,
enterprise, production
