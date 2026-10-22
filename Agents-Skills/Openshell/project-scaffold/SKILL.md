project-scaffold

Scaffold a new project with standard folder structure, config files, and git setup.

# Skill: project-scaffold

Create a well-structured new project from scratch.

## Workflow

1. **Gather requirements** — ask the user:
   - Project name (slug, lowercase-hyphen)
   - Project type (Node/TS, React Native, Python, plain JS, other)
   - Brief description (one sentence)
   - License (MIT, Apache-2.0, proprietary)

2. **Create folder structure** — use `write` to create files:

### Node / TypeScript
```
<name>/
  src/
    index.ts
  tests/
  package.json
  tsconfig.json
  .gitignore
  README.md
```

### Python
```
<name>/
  src/<name>/
    __init__.py
    main.py
  tests/
    test_main.py
  pyproject.toml
  .gitignore
  README.md
```

3. **Populate config files** with sensible defaults for the detected type.

4. **Write README.md** with:
   - Project name and description
   - Install instructions
   - Usage example
   - License

5. **Initialize git** — follow the `git-init` skill.

## Rules

- Always ask before creating files in an existing directory.
- Use the project name as the package name (normalized).
- Never add dependencies that are not explicitly requested.
- Keep initial code minimal — scaffold only, no business logic.
