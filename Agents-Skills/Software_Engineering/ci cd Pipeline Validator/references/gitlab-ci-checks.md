# GitLab CI Validation Checks

## Syntax Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| S1 | Valid YAML | File must parse as valid YAML | FAIL |
| S2 | `stages:` defined | Must declare pipeline stages | FAIL |
| S3 | Job names are unique | No duplicate job keys | FAIL |
| S4 | Valid `stage:` references | Each job's `stage:` must exist in `stages:` | FAIL |
| S5 | `script:` or `trigger:` present | Jobs must have executable content | FAIL |
| S6 | Valid `image:` reference | Docker images must be resolvable | FAIL |
| S7 | `variables:` are valid types | No circular variable references | FAIL |
| S8 | `rules:` / `only:` / `except:` are valid | Condition syntax must be correct | FAIL |
| S9 | `needs:` dependencies valid | Referenced jobs must exist | FAIL |
| S10 | No conflicting `parallel` + `needs` | Incompatible combination | FAIL |

## Security Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| SEC1 | No hardcoded secrets in `variables:` | CI/CD variables should use CI/CD settings, not config | FAIL |
| SEC2 | `CI_SERVER_TLS_CAFILE` not overridden | Don't bypass TLS verification | FAIL |
| SEC3 | Docker images from trusted registries | Avoid unverified third-party images | WARN |
| SEC4 | No `docker:dind` without justification | Docker-in-Docker is a privilege escalation vector | WARN |
| SEC5 | Protected variables for production | Secrets used in prod-deploy jobs should be "protected" | WARN |
| SEC6 | No `git fetch` from untrusted URLs | Prevent supply chain injection | FAIL |
| SEC7 | Job token scope limited | `CI_JOB_TOKEN` should not have unnecessary access | WARN |

## Performance Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| P1 | Cache configured for dependencies | `cache: key:` + `cache: paths:` | WARN |
| P2 | Artifacts expire in reasonable time | `artifacts: expire_in:` set | INFO |
| P3 | `needs:` used instead of stage ordering | DAG pipelines are faster than strict stages | INFO |
| P4 | Parallel jobs for independent tasks | Use `parallel:` where applicable | INFO |
| P5 | Shallow clone when possible | `GIT_DEPTH: 1` for jobs not needing history | INFO |
| P6 | Job timeout set | `timeout:` prevents hung pipelines | WARN |
| P7 | Artifact size reasonable | No unnecessary large file uploads | WARN |

## Best Practice Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| BP1 | `.pre` and `.post` stages used for setup/teardown | Keep main stages focused | INFO |
| BP2 | Reusable `!reference` tags for common config | Avoid duplication | INFO |
| BP3 | `include:` for shared configs across projects | Modularize pipeline definitions | INFO |
| BP4 | `rules:` preferred over `only:`/`except:` | `rules:` is more flexible and recommended | WARN |
| BP5 | Environment tracking for deployments | `environment:` with URL and action | WARN |
| BP6 | Merge request pipelines configured | `rules: - if: $CI_MERGE_REQUEST_IID` | WARN |
| BP7 | Retries configured for flaky steps | `retry: max: 2` for network-dependent steps | INFO |
| BP8 | No deprecated keywords | `only/except` → `rules` | WARN |

## Common Anti-Patterns

### 1. Monolithic Single Job
```yaml
# BAD: One job does everything
test_and_deploy:
  stage: deploy
  script:
    - npm install
    - npm test
    - npm run build
    - npm run deploy
```

### 2. Overlapping `only` and `except` Rules
```yaml
# BAD: Confusing and error-prone
deploy:
  only:
    - main
  except:
    - tags
# Use rules: instead
deploy:
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

### 3. Missing Cache Configuration
```yaml
# BAD: Downloads dependencies every run
# Add cache:
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/
```

### 4. No DAG Dependencies (Stage Fan-Out)
```yaml
# SLOW: Waits for entire stage to complete
stages:
  - build
  - test
  - deploy
# Use needs: for faster pipelines
test_unit:
  stage: test
  needs: [build]
test_integration:
  stage: test
  needs: [build]
```
