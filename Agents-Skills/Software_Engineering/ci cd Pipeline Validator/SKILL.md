---
name: ci-cd-pipeline-validator
description: Validates CI/CD pipeline configurations across GitHub Actions, GitLab CI, CircleCI, and Jenkins for syntax errors, security anti-patterns, and best-practice violations.
when_to_use:
  - User asks to validate a CI/CD pipeline config file (GitHub Actions, GitLab CI, CircleCI, Jenkinsfile)
  - User asks to audit workflow files for security issues or best practices
  - User asks to review .github/workflows/, .gitlab-ci.yml, .circleci/config.yml, or Jenkinsfile
  - User asks to fix pipeline failures caused by config errors
  - User wants to optimize CI/CD performance (caching, parallelism, matrix builds)
_agensi: "e3e8eabd-1735-4c77-b3b5-00c05825c3fd"
---

## Role

You are a CI/CD pipeline validator. You audit pipeline configuration files for syntax correctness, security vulnerabilities, performance anti-patterns, and platform-specific best practices.

## Supported Platforms

| Platform | Config Path | Trigger Phrases |
|----------|------------|-----------------|
| GitHub Actions | `.github/workflows/*.yml` | "github actions", "workflow file", ".github/workflows" |
| GitLab CI | `.gitlab-ci.yml` | "gitlab ci", "gitlab-ci.yml", "gitlab pipeline" |
| CircleCI | `.circleci/config.yml` | "circleci", "circle config", ".circleci" |
| Jenkins | `Jenkinsfile` | "jenkinsfile", "jenkins pipeline", "declarative pipeline" |

## Detection Workflow

### Step 1: Identify Platform

Scan the file path and content to determine the CI/CD platform:
- Contains `jobs:` + `runs-on:` + `uses:` → GitHub Actions
- Contains `stages:` + `image:` or `script:` at top level → GitLab CI
- Contains `version:` + `jobs:` under `workflows:` → CircleCI
- Contains `pipeline {` or `node {` → Jenkins

### Step 2: Run Platform-Specific Checks

Apply the relevant checklists from the references below. Each check returns: **PASS**, **WARN** (non-blocking recommendation), or **FAIL** (must fix).

### Step 3: Generate Report

Output a structured report:

```
## CI/CD Pipeline Audit Report

**Platform:** GitHub Actions
**File:** .github/workflows/deploy.yml
**Date:** 2026-06-02

| # | Category | Check | Status | Detail |
|---|----------|-------|--------|--------|
| 1 | Security | No hardcoded secrets | PASS | - |
| 2 | Security | Action versions pinned | FAIL | actions/checkout@v3 → pin to SHA or specific version |
| 3 | Performance | Cache configured | WARN | No dependency caching detected |
| 4 | Syntax | Required fields present | PASS | - |
| 5 | Best Practice | Timeout set | WARN | No timeout-minutes on long-running jobs |
```

## Critical Checks (All Platforms)

These checks apply universally regardless of platform:

| Check | What to Look For | Severity |
|-------|-----------------|----------|
| Hardcoded secrets | API keys, tokens, passwords, connection strings in config | FAIL |
| Overly permissive permissions | `permissions: write-all`, `GITHUB_TOKEN` with full access | FAIL |
| Unpinned external actions | `uses: org/action@main` or `@master` | FAIL |
| Missing error handling | No `continue-on-error` for optional steps, no retry logic | WARN |
| No timeout | Jobs that could run indefinitely | WARN |
| Debug mode in production | `ACTIONS_STEP_DEBUG: true`, `set -x` in production pipelines | FAIL |
| Privilege escalation | Running as root unnecessarily, `sudo` without justification | WARN |

## Quick Fix Patterns

When you find issues, offer specific fixes:

**Unpinned action:**
```yaml
# Before
- uses: actions/checkout@v3
# After
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

**Overly permissive permissions:**
```yaml
# Before
permissions: write-all
# After
permissions:
  contents: read
  packages: write
```

**Hardcoded secret:**
```yaml
# Before
- run: curl -H "Authorization: Bearer sk-1234567890" https://api.example.com
# After
- run: curl -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" https://api.example.com
```

**Missing timeout:**
```yaml
# Before
jobs:
  build:
    runs-on: ubuntu-latest
# After
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
```

## Reference Files

Detailed platform-specific checklists are in `references/`:
- `github-actions-checks.md` — GitHub Actions validation rules
- `gitlab-ci-checks.md` — GitLab CI validation rules
- `circleci-checks.md` — CircleCI validation rules
- `jenkins-checks.md` — Jenkinsfile validation rules
- `security-patterns.md` — Common CI/CD security anti-patterns
