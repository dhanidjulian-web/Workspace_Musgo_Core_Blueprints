code-review

Systematic code review covering correctness, security, performance, and style.

# Skill: code-review

Perform a thorough code review on the specified files or diff.

## Checklist

### Correctness
- [ ] Logic matches the stated intent.
- [ ] Edge cases handled (null, empty, overflow, concurrent access).
- [ ] Error paths return meaningful messages or propagate correctly.
- [ ] No off-by-one errors in loops or array indexing.
- [ ] Async operations awaited; no floating promises.

### Security
- [ ] No secrets, tokens, or credentials in source.
- [ ] User input validated and sanitized before use.
- [ ] No SQL/command injection vectors.
- [ ] Sensitive data not logged.
- [ ] Dependencies not pinned to known-vulnerable versions.

### Performance
- [ ] No N+1 query patterns.
- [ ] Expensive operations not in hot paths (render loops, tight loops).
- [ ] Large data structures not copied unnecessarily.
- [ ] Memoization used where appropriate.

### Maintainability
- [ ] Functions ≤ 40 lines; single responsibility.
- [ ] Names are descriptive and consistent with the codebase.
- [ ] No dead code or commented-out blocks.
- [ ] Complex logic has inline comments explaining *why*, not *what*.
- [ ] Tests exist for new behavior.

## Output format

For each issue found:

```
[SEVERITY] file.ts:42 — Short description
Why: explanation of the problem
Fix: concrete suggestion
```

Severity levels: **CRITICAL** · **HIGH** · **MEDIUM** · **LOW** · **NIT**

End with a **Summary** table:

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| HIGH | 0 |
| MEDIUM | 0 |
| LOW | 0 |
| NIT | 0 |
