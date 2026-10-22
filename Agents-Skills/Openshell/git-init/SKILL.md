git-init

Initialize a git repo with .gitignore, README, and first commit.

# Skill: git-init

Bootstrap a new git repository with sensible defaults.

## Steps

1. **Confirm workspace** — verify the target directory exists and is not already a git repo (`git_status`).
2. **Initialize** — run `git_init` in the workspace root.
3. **Create .gitignore** — write a `.gitignore` appropriate for the project type detected (Node, Python, Android, etc.).
4. **Create README.md** — minimal README with project name and one-line description.
5. **Stage everything** — `git_add` with path `.`.
6. **First commit** — `git_commit` with message `chore: initial commit`.

## .gitignore templates

### Node / React Native
```
node_modules/
.expo/
dist/
build/
*.log
.env
.env.local
.DS_Store
```

### Python
```
__pycache__/
*.pyc
.venv/
dist/
build/
*.egg-info/
.env
```

### Android
```
*.iml
.gradle/
local.properties
.idea/
.DS_Store
build/
captures/
```

## Rules

- Never commit secrets (`.env`, credentials, API keys).
- Always create `.gitignore` before the first commit.
- Use `chore: initial commit` as the first commit message.
- Ask the user for the project name and description before writing README.
