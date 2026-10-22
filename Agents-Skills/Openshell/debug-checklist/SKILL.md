debug-checklist

Systematic debugging workflow: reproduce, isolate, hypothesize, verify, fix.

# Skill: debug-checklist

Follow a disciplined debugging process to find and fix bugs reliably.

## Phase 1 — Reproduce

1. Get the exact error message, stack trace, or unexpected behavior description.
2. Identify the **minimum reproducible case** — simplest input that triggers the bug.
3. Confirm the bug is deterministic or characterize its frequency.

## Phase 2 — Isolate

1. Read the stack trace top-to-bottom — find the first frame in *your* code.
2. Use `grep` and `read` to locate the relevant code.
3. Narrow the scope: which function, which branch, which condition?
4. Check recent changes: `git_log` + `git_diff` to see what changed last.

## Phase 3 — Hypothesize

Form 2–3 specific hypotheses ranked by likelihood:

```
H1: [most likely cause] — evidence: ...
H2: [second candidate] — evidence: ...
H3: [edge case]        — evidence: ...
```

## Phase 4 — Verify

Test each hypothesis cheapest-first:
- Read the code path for H1.
- Add temporary `console.log` / logging if needed.
- Check assumptions about data types, nullability, async ordering.
- Confirm the fix resolves the reproduction case.

## Phase 5 — Fix

1. Apply the minimal change that fixes the root cause.
2. Do not fix symptoms — fix the root cause.
3. Remove any debug logging added in Phase 4.
4. Write a regression test if the bug was not caught by existing tests.
5. Commit with `fix(<scope>): <description>` following the `git-commit` skill.

## Common patterns to check

| Symptom | Common cause |
|---------|-------------|
| Undefined is not a function | Missing null check, wrong import |
| Infinite loop / hang | Missing await, circular dependency |
| Stale data in UI | Missing state update, wrong dependency array |
| Works locally, fails in prod | Env var missing, path difference, timezone |
| Intermittent failure | Race condition, unhandled promise rejection |
