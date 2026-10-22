# Git Commit Writer (Free)

Generate clear Conventional Commit messages from staged git changes, including scope, intent, and concise body notes when useful.

## Installation

Copy to your skills directory:

**Codex (macOS/Linux):**
```bash
cp -r ./git-commit-writer-free ~/.codex/skills/
```

**Codex (Windows):**
```powershell
Copy-Item -Recurse .\git-commit-writer-free "$env:USERPROFILE\.codex\skills\"
```

## Usage

1. Stage your changes: `git add .`
2. Trigger the skill: "write commit message"
3. Copy the suggested commit or ask for alternatives

Example output:
```
feat(auth): add password reset flow

- Adds /forgot-password endpoint
- Adds email sending via Resend
- Adds reset token verification
```

## Requirements

- Git in PATH
- Files staged via `git add`

## Why Free?

This skill is free because good commit messages make everyone's life better. If you find it useful, check out my other skills:

- **HandoffPilot** ($19) — Never lose context between Claude Code sessions. `/handoff` before context fills, `/resume` where you left off.
- **Guardrail Doctor** ($29) — Test security hooks before deployment. Finds gaps in deny rules and prompt injection defenses.
- **Spec2Code** ($19) — Turn Notion specs into implementation plans. Tasks, dependencies, estimates.

[View all skills on Agensi →](https://agensi.io/@Fairy-Squadmother-Skills)

## License

MIT — free to use, modify, share. Just don't resell it as-is.
