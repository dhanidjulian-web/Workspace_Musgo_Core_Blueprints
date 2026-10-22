# README Generator (Free)

Build a repo-aware README from manifests, source files, and project structure. Produces install steps, usage notes, and caveats without hand-writing the bones.

## Installation

Copy to your skills directory:

**Codex (macOS/Linux):**
```bash
cp -r ./readme-generator-free ~/.codex/skills/
```

**Codex (Windows):**
```powershell
Copy-Item -Recurse .\readme-generator-free "$env:USERPROFILE\.codex\skills\"
```

**Claude Code (macOS/Linux):**
```bash
cp -r ./readme-generator-free ~/.claude/skills/
```

**Claude Code (Windows):**
```powershell
Copy-Item -Recurse .\readme-generator-free "$env:USERPROFILE\.claude\skills\"
```

## Usage

Open any project and trigger the skill with:

- "generate readme"
- "create README"
- "write project documentation"
- "make a readme"

README Generator scans the project and detects:

- Language/framework from `package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, Java build files, and related manifests
- Main entry points such as `index.js`, `main.py`, `main.go`, `src/index.ts`, and language-specific equivalents
- Dependencies from real manifest files only
- Scripts and commands from `package.json`, `Makefile`, and build metadata
- Existing comments, docstrings, JSDoc, JavaDoc, and license files

It generates:

- Title and description
- License, language, version, and build status badges
- Installation instructions
- Usage examples
- API documentation when source comments exist
- Contributing guidelines
- License section

## Example Prompt

```text
generate readme for this project
```

## Price

FREE ($0 on Agensi).

## Upgrade Path

README Generator is free because every project deserves documentation people can actually use. If you want deeper developer workflow automation, check out my paid skills:

- **HandoffPilot** ($19): Never lose context between Claude Code sessions. `/handoff` before context fills, `/resume` where you left off.
- **Guardrail Doctor** ($29): Test security hooks before deployment. Finds gaps in deny rules and prompt injection defenses.
- **Spec2Code** ($19): Turn Notion specs into implementation plans. Tasks, dependencies, estimates.
- **CI Doctor** ($12): Diagnose failing GitHub Actions and CI pipelines with root-cause fixes.

[View all skills on Agensi](https://www.agensi.io/creators/justhandled)

## License

MIT - free to use, modify, and share. Please do not resell it as-is.
