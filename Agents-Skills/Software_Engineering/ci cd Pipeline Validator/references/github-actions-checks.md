# GitHub Actions Validation Checks

## Syntax Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| S1 | Valid YAML | File must parse as valid YAML | FAIL |
| S2 | `on:` trigger present | Must have at least one trigger event | FAIL |
| S3 | `jobs:` section exists | Must define at least one job | FAIL |
| S4 | Job IDs are unique | No duplicate job keys | FAIL |
| S5 | Step `id`s are unique within a job | No duplicate step IDs | FAIL |
| S6 | Valid `runs-on` value | Must be a valid runner label | FAIL |
| S7 | Expression syntax valid | `${{ }}` expressions must be well-formed | FAIL |
| S8 | No circular job dependencies | `needs:` must not create cycles | FAIL |

## Security Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| SEC1 | No hardcoded secrets | No API keys, tokens, passwords visible in config | FAIL |
| SEC2 | No `pull_request_target` with checkout + code execution | Dangerous fork PR escalation | FAIL |
| SEC3 | `permissions:` is scoped | Avoid `write-all`; use least-privilege | FAIL |
| SEC4 | Actions pinned to SHA or version | `uses: org/action@main` → pin to `@v4.1.1` or SHA | FAIL |
| SEC5 | Third-party actions reviewed | Actions from non-`actions/` org should be audited | WARN |
| SEC6 | No `GITHUB_TOKEN` passed to untrusted actions | Tokens should not flow to external actions | FAIL |
| SEC7 | No inline scripts downloading and executing remote code | `curl | bash` patterns | FAIL |
| SEC8 | `ACTIONS_STEP_DEBUG` disabled in production workflows | Debug logging can leak secrets | FAIL |

## Performance Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| P1 | Dependency caching configured | `actions/cache` or built-in cache for node_modules, pip, etc. | WARN |
| P2 | `timeout-minutes` set on long jobs | Prevent zombie pipelines | WARN |
| P3 | Matrix builds used for multi-platform testing | Avoid duplicating jobs manually | INFO |
| P4 | Artifact upload/download is efficient | No unnecessary large file transfers | WARN |
| P5 | `fetch-depth: 1` for checkout when full history not needed | Speeds up clone | INFO |
| P6 | Reusable workflows for common patterns | Avoid copy-paste across workflow files | INFO |
| P7 | Concurrency groups configured | Prevent redundant runs on same branch | WARN |

## Best Practice Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| BP1 | Workflow name is descriptive | `name: Deploy to Production` not `name: CI` | INFO |
| BP2 | Steps have meaningful `name:` fields | Every step should be labeled | INFO |
| BP3 | Error handling for critical steps | `if: failure()` or `continue-on-error` as appropriate | WARN |
| BP4 | Environment protection rules for production | `environment: production` with required reviewers | WARN |
| BP5 | Branch protection referenced | Production deploy gated by branch rules | WARN |
| BP6 | No deprecated actions | `actions/setup-node@v2` → upgrade to v4 | WARN |
| BP7 | Runner OS is current | `ubuntu-20.04` → `ubuntu-24.04` | INFO |

## Common Anti-Patterns

### 1. The "Everything in One Job" Monolith
```yaml
# BAD: Single job does lint, test, build, deploy
jobs:
  everything:
    steps:
      - run: npm run lint
      - run: npm test
      - run: npm run build
      - run: npm run deploy
```

### 2. Secrets in Environment Variables (Leaked in Logs)
```yaml
# BAD: Secret echoed in logs
env:
  API_KEY: sk-12345
```

### 3. Unpinned Third-Party Actions
```yaml
# BAD: @main can change under you
- uses: some-org/some-action@main
```

### 4. No Concurrency Control
```yaml
# BAD: Every push spawns a new workflow run
# Add:
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
