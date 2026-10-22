---
name: env-doctor-advanced
description: Diagnoses environment configuration issues across .env files, shell profiles, CI configs, and runtime environments. Detects missing variables, secret exposure, version mismatches, and path issues. Use when debugging environment setup, onboarding new devs, or auditing config hygiene.
when_to_use: |
  - User reports "it works on my machine but not CI"
  - User asks to audit .env or environment configuration
  - Onboarding a new developer to a project
  - Debugging missing environment variable errors
  - Do NOT use for: code debugging, dependency installation, or build errors unrelated to environment
effort: medium
_agensi: "e283ad5f-19e5-49da-83a0-e65830da87d0"
---

# Environment Doctor (Advanced)

## Overview

Diagnoses environment configuration issues across `.env` files, shell profiles, CI/CD configs, Docker environments, and runtime settings. Catches missing variables, accidentally committed secrets, version mismatches, and path resolution problems.

## When to Use

- "It works on my machine but not in CI"
- Debugging `undefined variable` or `command not found` errors
- Onboarding a new developer to a project
- Auditing environment security (exposed secrets, hardcoded credentials)
- **Do NOT use for:** code-level bugs, dependency resolution, build script errors

## Execution Steps

### Step 1: Environment Inventory

Detect the project's environment configuration layers:

1. **Local env files:** `.env`, `.env.local`, `.env.development`, `.env.production`, `.env.example`
2. **Shell profiles:** `.bashrc`, `.zshrc`, `.bash_profile`, `config.fish`
3. **CI configs:** `.github/workflows/*.yml`, `.circleci/config.yml`, `Jenkinsfile`, `.gitlab-ci.yml`
4. **Container configs:** `Dockerfile`, `docker-compose.yml`, `.dockerignore`
5. **Runtime configs:** `package.json` (engines, scripts), `pyproject.toml`, `requirements.txt`, `runtime.txt`

### Step 2: Variable Gap Analysis

Compare required vs. defined environment variables:

1. Parse `.env.example` or `README.md` for documented required variables
2. Parse `.env` (or equivalent) for actually defined variables
3. Parse CI configs for variables injected at runtime
4. Report:
   - **Missing:** Required but not defined anywhere
   - **Inconsistent:** Defined in `.env` but not in CI (or vice versa)
   - **Orphaned:** Defined but never referenced in code

Quick scan script:
```bash
# Find all env var references in source code
grep -rEho '\$[A-Z_]+|\bprocess\.env\.[A-Z_]+\bos\.environ\[[A-Z_]+\]' --include='*.{js,ts,py,sh,yml}' src/ 2>/dev/null | sort -u
```

### Step 3: Security Audit

Check for common security misconfigurations:

1. **Committed secrets:** Search `.env` files for patterns matching:
   - API keys: `sk-`, `pk_`, `api_key=`, `secret=`
   - Passwords: `password=`, `passwd=`, `pwd=`
   - Tokens: `token=`, `auth=`, `bearer`
   - Private keys: `-----BEGIN (RSA |EC )?PRIVATE KEY-----`

2. **Exposed in logs:** Check CI configs for `echo $SECRET` or printing env vars

3. **Weak defaults:** Variables with `localhost`, `127.0.0.1`, `test`, `changeme` in production configs

### Step 4: Version Compatibility Check

Compare declared vs. actual tool versions:

1. **Node.js:** Check `package.json` `engines.node` vs. runtime `node --version`
2. **Python:** Check `pyproject.toml` `requires-python` vs. runtime `python --version`
3. **Runtime tools:** Compare `Dockerfile` base image tags against CI runner versions
4. Flag mismatches that could cause "works locally, breaks in CI" issues

### Step 5: Path & Filesystem Audit

1. **Relative vs. absolute paths:** Check for hardcoded absolute paths that break on different machines
2. **Working directory assumptions:** Check if scripts assume a specific `cwd`
3. **Cross-platform issues:** Look for Windows-specific paths (`C:\`, `\\`) in Unix configs or vice versa
4. **Symlink/dotfile issues:** Check if `.env` loading depends on specific shell behavior

### Step 6: Generate Diagnosis Report

```markdown
## Environment Diagnosis Report

### Critical Issues
| Issue | Location | Impact |
|-------|----------|--------|
| Missing DB_HOST in CI config | .github/workflows/deploy.yml | App crashes on startup |

### Warnings
| Issue | Location | Recommendation |
|-------|----------|----------------|
| .env committed to git | root | Add to .gitignore, use .env.example |
| Node 18 required but CI runs 16 | package.json + CI runner | Update CI or downgrade engines |

### Security Findings
| Finding | File | Risk |
|---------|------|------|
| AWS secret key in .env.development | .env.development | High — may be committed |

### Environment Summary
| Layer | Variables | Missing | Inconsistent |
|-------|-----------|---------|--------------|
| Local (.env) | 23 | 2 | 1 |
| CI/CD | 18 | 5 | 3 |
| Docker | 15 | 0 | 0 |
```

## Security Note

This skill is **read-only** during diagnosis. It never modifies `.env` files, secrets, or configuration. Any suggested fixes are reported for user review.
