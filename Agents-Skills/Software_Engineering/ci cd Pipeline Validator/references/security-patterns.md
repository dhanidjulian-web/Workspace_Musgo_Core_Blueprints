# CI/CD Security Anti-Patterns

This file catalogs common security vulnerabilities found in CI/CD pipeline configurations, with real-world impact and remediation guidance.

## Critical Vulnerabilities

### VULN-001: `pull_request_target` with Untrusted Code Checkout

**Platform:** GitHub Actions
**Risk:** Remote Code Execution (RCE)
**Severity:** CRITICAL

When `pull_request_target` triggers a workflow that checks out PR code and runs it, a malicious PR can execute arbitrary code with write access to the repository.

```yaml
# DANGEROUS
on: pull_request_target
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4  # Checks out PR code, not base
      - run: npm test               # Runs attacker's code with repo token
```

**Fix:** Use `pull_request` instead, or isolate untrusted code in a sandbox with no token access.

---

### VULN-002: Hardcoded Secrets in Config

**Platform:** All
**Risk:** Credential Exposure
**Severity:** CRITICAL

Secrets in pipeline config are visible to anyone with repo read access and appear in build logs.

```yaml
# DANGEROUS
env:
  AWS_SECRET_KEY: AKIAIOSFODNN7EXAMPLE
  DB_PASSWORD: supersecret123
```

**Fix:** Use platform-native secret stores (GitHub Secrets, GitLab CI/CD Variables, CircleCI Contexts, Jenkins Credentials).

---

### VULN-003: Unpinned Actions with Mutable Tags

**Platform:** GitHub Actions
**Risk:** Supply Chain Attack
**Severity:** HIGH

Using `@main`, `@master`, or `@latest` means the action code can change without your knowledge.

```yaml
# DANGEROUS
- uses: third-party/action@main
```

**Fix:** Pin to a specific version tag or commit SHA:
```yaml
- uses: third-party/action@v2.1.0
# or
- uses: third-party/action@a1b2c3d4e5f6...
```

---

### VULN-004: Overly Permissive `GITHUB_TOKEN` Permissions

**Platform:** GitHub Actions
**Risk:** Unauthorized Repository Modification
**Severity:** HIGH

Default permissions may be broader than needed. Explicitly scope to minimum required access.

```yaml
# DANGEROUS
permissions: write-all
# or (default may allow more than needed)
# no permissions block at all
```

**Fix:**
```yaml
permissions:
  contents: read
  packages: write
```

---

### VULN-005: Docker-in-Docker Without Justification

**Platform:** GitLab CI, CircleCI
**Risk:** Container Escape
**Severity:** HIGH

Running `docker:dind` gives the pipeline full control over the Docker daemon, which can escape to the host.

```yaml
# DANGEROUS (unless you truly need Docker)
services:
  - docker:dind
```

**Fix:** Use Docker socket binding with restrictions, or build images in isolated environments.

---

### VULN-006: Command Injection via Unsanitized Input

**Platform:** All
**Risk:** Remote Code Execution
**Severity:** CRITICAL

Pipeline variables or PR content used directly in shell commands without sanitization.

```yaml
# DANGEROUS (GitHub Actions)
- run: echo "PR from ***.user.login }}"
# If PR title is: "; rm -rf /; echo "
# The command becomes: echo "PR from "; rm -rf /; echo ""
```

**Fix:** Always quote variables and validate input:
```yaml
- run: echo "***' >> safe_output.txt
```

---

### VULN-007: Artifact Exfiltration

**Platform:** All
**Risk:** Data Leakage
**Severity:** HIGH

Pipeline artifacts may include sensitive files that get uploaded and become publicly accessible.

```yaml
# DANGEROUS
- run: cp .env build_output/
# If build_output/ is uploaded as an artifact, .env is exposed
```

**Fix:** Use `.artifactignore` or explicit file patterns to exclude sensitive files.

---

### VULN-008: Debug Mode in Production Pipelines

**Platform:** All
**Risk:** Secret Exposure in Logs
**Severity:** HIGH

Debug/verbose logging can accidentally print secrets, tokens, or credentials.

```yaml
# DANGEROUS
env:
  ACTIONS_STEP_DEBUG: true
```

**Fix:** Only enable debug logging in development/testing workflows, never in production.

---

## Detection Patterns

Use these regex patterns to scan pipeline configs:

| Pattern | Description | Severity |
|---------|-------------|----------|
| `(sk-|AKIA|ghp_|xox[bposr]-|-----BEGIN)` | Potential hardcoded secrets | CRITICAL |
| `@main\|@master\|@latest` | Unpinned action references | HIGH |
| `write-all\|admin` | Overly permissive permissions | HIGH |
| `pull_request_target.*checkout` | Dangerous fork workflow pattern | CRITICAL |
| `curl.*\|.*sh\|wget.*\|.*bash` | Download and execute pattern | HIGH |
| `docker:dind\|--privileged` | Privileged container execution | HIGH |
| `ACTIONS_STEP_DEBUG\|set -x` | Debug mode enabled | MEDIUM |
| `password\s*[:=]\s*["'][^"']+["']` | Password assignment | CRITICAL |
