git-commit

Conventional Commits format — staged diff analysis and message generation.

# Skill: git-commit

Write commit messages following the **Conventional Commits** specification.

## Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer(s)]
```

## Types

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code change that is neither a fix nor a feature |
| `docs` | Documentation only |
| `style` | Formatting, whitespace — no logic change |
| `test` | Adding or updating tests |
| `chore` | Build process, tooling, dependencies |
| `perf` | Performance improvement |
| `ci` | CI/CD configuration |
| `revert` | Reverts a previous commit |

## Workflow

1. Run `git_status` to see what is staged.
2. Run `git_diff` (staged) to read the actual changes.
3. Identify the primary intent — choose the correct **type**.
4. Derive a short **scope** from the affected module/file (optional but recommended).
5. Write a concise **subject** in imperative mood, lowercase, no period.
6. Add a **body** only when the why is not obvious from the subject.
7. Add **BREAKING CHANGE:** footer when the commit breaks the public API.
8. Run `git_commit` with the composed message.

## Rules

- Subject ≤ 72 characters.
- Body lines ≤ 100 characters.
- Never use past tense ("added") — use imperative ("add").
- Do not mention file names in the subject unless they are the entire change.
- One logical change per commit — split unrelated changes.

## Examples

```
feat(auth): add biometric login support

Adds FaceID/fingerprint authentication as an alternative to PIN.
Requires expo-local-authentication ≥ 13.

BREAKING CHANGE: AuthContext.login() now returns Promise<AuthResult>
```

```
fix(chat): prevent duplicate messages on stream reconnect
```

```
chore(deps): upgrade expo-sqlite to 15.1.2
```
