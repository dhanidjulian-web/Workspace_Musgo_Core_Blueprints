---
name: "Managing Long Coding Sessions with Claude"
description: "Use when the user is in a long or multi-day coding session and wants to keep work coherent across Claude Code's context window and across sessions. Routes session-management work through Claude Code's built-in primitives — TaskCreate, the persistent memory system, CLAUDE.md, Plan mode, ScheduleWakeup — instead of manual handoff documents."
version: 1.0.0
author: Markus Isaksson
license: MIT
price: 0
tags: ["claude", "claude-code", "long-sessions", "memory", "claude-md", "workflow", "free"]
_agensi: "6ea7d423-529f-4ab3-9f7a-e6de0f1271d7"
---

# Managing Long Coding Sessions with Claude

**Trigger Conditions:**
The user mentions the session is getting long, they've been working for hours, they're losing track of decisions, they want help maintaining context across a multi-day effort, or they're about to pause / resume work.

**Do NOT use** for short, one-off tasks.

## Why This Skill Exists

Claude Code handles **tactical** context drift automatically — older turns get summarized into the next window, so work can continue without manual handoff documents. But Claude Code can't decide on its own what's **strategically** worth preserving across sessions, what belongs in the persistent memory, what should land in CLAUDE.md, or what's just churn. Without discipline, long sessions either bloat the chat with redundant summaries, or lose load-bearing context because nobody wrote it down in the right place. This skill provides a process for using Claude Code's own primitives (TaskCreate, memory, CLAUDE.md, Plan mode, ScheduleWakeup) deliberately, instead of falling back to "let me summarize" reflexes that were necessary on agents without these features.

## What You'll Gain

- A clean separation between **tactical context** (handled by Claude's auto-compression — don't fight it) and **strategic context** (must be persisted explicitly)
- A repeatable pattern for capturing decisions in project memory while they're fresh
- A session-pause protocol that produces a CLAUDE.md update or a memory entry, not a transient handoff doc that will rot
- Practice with TaskCreate as the running record of work-in-flight
- Confidence that resuming tomorrow won't lose what was decided today

## Agent Operating Procedure

When this skill is activated, follow this exact process:

### Phase 1: Session Structuring

1. Ask the user to state the current main goal in one sentence and any sub-goals.
2. **If the project has a CLAUDE.md or existing project memory entries, read them first.** State what you read. Don't skip this step — it's the fastest way to inherit yesterday's state.
3. **Create a TaskCreate list** capturing today's work. Each task: actionable subject + brief description. Mark the first as `in_progress`.

**Rule:** Do not maintain a todo list in chat text. TaskCreate is the durable surface — it persists across the session, deduplicates, and the user can see state without scrolling.

### Phase 2: Memory Hygiene (Continuous)

Throughout the session, watch for things that belong in persistent memory at `~/.claude/projects/<project-slug>/memory/`:

- **User preferences** the user explicitly states ("I always want X", "never do Y") → save as `feedback` memory with the reason
- **Project facts** that aren't derivable from the code (who's doing what, why a decision was made, a stakeholder constraint) → save as `project` memory
- **External system references** (Linear projects, Grafana dashboards, Slack channels) → save as `reference` memory

When you save, briefly tell the user what you saved so they can correct stale or wrong entries.

**Rule:** Don't save code patterns, file paths, architecture summaries, or anything `git log`/`grep`/`Read` can answer. Memory is for non-derivable facts only.

### Phase 3: Trust Auto-Compression; Manage Strategic Context Deliberately

1. **Don't preemptively summarize** the conversation. Claude Code compresses old turns when context fills — your manual summary is wasted effort that just pollutes the window faster.
2. **DO** check in with the user at natural break points (after a major task completes, when changing direction, before risky operations). Brief, not heavy.
3. **DO** update CLAUDE.md when the session produces a durable repo-level fact that every future Claude should see at session-start (build commands changed, a new sub-project added, a convention was decided).

**Rule:** A session that ends without a CLAUDE.md or memory update — when one was warranted — is a session that loses its lesson.

### Phase 4: Plan Mode at Decision Points

Before major direction changes or risky operations, use **Plan mode (`ExitPlanMode`)** to present:

- One sentence on where we are
- The two or three options you see
- A recommendation and the trade-off

This is more valuable than a midstream "let me summarize" — it forces the choice into the user's hands at the exact moment they can still change direction cheaply.

### Phase 5: Pause / Resume Protocol

When the user wants to pause for the day or session:

1. **Update TaskList state** honestly — mark `in_progress` items as `pending` (or `completed` if actually done), delete tasks no longer relevant. Tomorrow's user resumes from a list that reflects reality, not aspiration.
2. **Write or update a project memory entry** capturing what was decided, what's still open, and what the next move is. The chat may be summarized; the memory file isn't.
3. **Update CLAUDE.md** if anything load-bearing changed (commands, sub-project layout, conventions, gotchas).
4. **Optional: ScheduleWakeup** if there's a time-based follow-up — a CI run that will be done in 90 minutes, a "tomorrow morning" check-in. Use sparingly; most pauses don't need one.
5. Tell the user what you wrote, and where.

Do **not** generate a "Session Handoff Document" as a standalone artifact unless the user explicitly asks. Memory + CLAUDE.md + TaskList already cover that ground; a separate doc duplicates and rots out of sync.

## Expected Output Patterns

**At session start (Phase 1):**

> Read `CLAUDE.md` and `project_<name>.md` from memory. Current state per those sources: [1-sentence summary]. Goal you stated: [restated]. TaskCreate list initialized with N items. Starting on task #1: [subject].

**At a memory checkpoint (Phase 2):**

> Saved to `feedback_<slug>.md`: [the rule, in user's words]. Tell me if I've captured it wrong.

**At a pause point (Phase 5):**

> Pause summary:
> - **TaskList:** [N completed], [M still pending — listed by subject]
> - **Memory:** wrote/updated `project_<slug>.md` with [one-sentence decision summary]
> - **CLAUDE.md:** [updated to note X / no changes needed]
> - **Next move when you resume:** [one sentence]

## Common Pitfalls to Avoid

| Don't Do This | Do This Instead |
|---|---|
| Maintain a running todo list in chat text | Use TaskCreate — it persists, deduplicates, and surfaces state durably |
| Summarize the conversation every 30 minutes "just in case" | Trust auto-compression; summarize only at user-visible decision points |
| Generate a fresh "Session Handoff Document" each pause | Update memory + CLAUDE.md + TaskList — those ARE the handoff |
| Save derivable facts to memory ("the API lives in `src/api/`") | Memory is for non-derivable facts; let the repo answer the rest |
| Save feedback silently | Tell the user what you saved so they can correct stale entries |
| Skip the CLAUDE.md update because "the chat has it" | The chat will be summarized away; CLAUDE.md is loaded every session |
| Carry every TODO forward across sessions | Prune the TaskList honestly at pause — stale tasks hide the live ones |

## Recommended Starting Prompt

```
We're going to be working on this for a while — likely multi-session. Please
apply the Managing Long Coding Sessions with Claude skill. Start with Phase 1:
read any existing CLAUDE.md and project memory, then initialize a TaskCreate
list for what we're doing today.
```

## Works Well With

- **Plan Mode Mastery for Claude Code** (paid, $5) — Phase 4 of this skill uses Plan mode at decision points; Plan Mode Mastery teaches the craft of writing plans that get approved on the first read, including the "what was missing from the plan" retrospection that compounds into a per-codebase plan library.
- **Effective Debugging with Claude** (free) — Long debugging investigations are the canonical case where this session-management discipline earns its keep.
- **Technical Documentation with Claude** (free) — Phase 5's pause protocol updates CLAUDE.md; the docs skill teaches how to write CLAUDE.md so the next Claude session inherits the right strategic context.

## Compatibility

Skills on Agensi follow the open SKILL.md standard and work with any compatible agent, including Claude Code, Cursor, VS Code Copilot, Codex CLI, Gemini CLI, and Grok Build CLI / TUI.

**Compatibility Note:** This skill is specifically optimized for **Claude Code**. It depends on Claude Code's distinctive primitives — automatic context compression, the persistent memory system at `~/.claude/projects/<project>/memory/`, the CLAUDE.md auto-loading convention, TaskCreate/TaskUpdate/TaskList, Plan mode (`ExitPlanMode`), and ScheduleWakeup. A Grok-flavored sibling (`managing-long-coding-sessions-with-grok`) exists for agents without these features, where the manual handoff-document pattern is the right answer.

---

## Permissions

**Recommended**

**Tools Used**

- **TaskCreate / TaskUpdate / TaskList**: Yes — Phase 1, Phase 4, Phase 5 all use these.
- **Memory writes** (`~/.claude/projects/<project>/memory/`): Yes — Phase 2 and Phase 5 write feedback / project / reference memory entries.
- **Read Files**: Yes — For reading CLAUDE.md and existing memory at session start.
- **Edit / Write**: Sometimes — When updating CLAUDE.md to reflect session-end state.
- **Plan Mode (`ExitPlanMode`)**: Recommended — For Phase 4 decision-point presentation.
- **ScheduleWakeup**: Sometimes — For Phase 5 when there's a time-based follow-up.
- **Bash / Terminal**: Sometimes — For checking git state, running tests at checkpoints.
- **WebFetch / WebSearch**: No
- **Network Access**: No (the agent's other tools may, but this skill doesn't require it)

**Environment Variables**: None required

**Allowed Hosts**: None

**File Scopes**:
- `CLAUDE.md`
- `**/CLAUDE.md`
- `~/.claude/projects/<project-slug>/memory/**`
- `docs/**`

**Notes**:
This skill leans heavily on Claude Code's persistent memory and CLAUDE.md infrastructure. If used in a project that doesn't yet have a CLAUDE.md, the Phase 1 and Phase 5 steps will create one. The skill is intentionally opposed to "write a fresh handoff doc each pause" — that pattern is necessary on agents without persistent state but is an anti-pattern with Claude Code, where it duplicates and then rots out of sync with the actual memory.
