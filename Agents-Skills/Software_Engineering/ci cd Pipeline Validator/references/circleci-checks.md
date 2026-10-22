# CircleCI Validation Checks

## Syntax Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| S1 | Valid YAML | File must parse as valid YAML | FAIL |
| S2 | `version: 2.1` present | Must use modern config version | FAIL |
| S3 | `jobs:` section exists | Must define at least one job | FAIL |
| S4 | `workflows:` section exists | Must define workflow orchestration | FAIL |
| S5 | Job executor valid | `docker:`, `machine:`, or `macos:` must be specified | FAIL |
| S6 | Workflow job references valid | All referenced jobs must be defined | FAIL |
| S7 | `requires:` dependencies valid | Referenced jobs must exist in workflow | FAIL |
| S8 | No circular `requires:` dependencies | DAG must be acyclic | FAIL |
| S9 | Orb references valid | Orbs must be declared in `orbs:` section | FAIL |
| S10 | Commands used within jobs only | `commands:` cannot run standalone | FAIL |

## Security Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| SEC1 | No hardcoded secrets in config | Use CircleCI context or project settings | FAIL |
| SEC2 | Docker images from trusted sources | Avoid unverified images from Docker Hub | WARN |
| SEC3 | SSH fingerprints verified for `add_ssh_keys` | Prevent MITM on SSH connections | WARN |
| SEC4 | No `sudo` without justification | Principle of least privilege | WARN |
| SEC5 | Contexts used for environment-specific secrets | Separate prod/staging secrets via contexts | WARN |
| SEC6 | No public artifacts containing sensitive data | `store_artifacts` should not expose secrets | FAIL |
| SEC7 | Resource class appropriate | Don't use `large` when `medium` suffices (cost) | INFO |

## Performance Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| P1 | Workspace used for job-to-job file sharing | Avoid redundant builds between jobs | WARN |
| P2 | Cache keys include dependency lockfile hash | `{{ checksum "package-lock.json" }}` | WARN |
| P3 | Parallel test splitting configured | `parallelism:` + `circleci tests split` | INFO |
| P4 | `no_output_timeout` set for long-running steps | Prevent silent hangs | WARN |
| P5 | Resource class matches workload | Don't over-provision | INFO |
| P6 | Docker layer caching used | `setup_remote_docker` with caching | INFO |
| P7 | Workflow filters avoid redundant runs | `filters: branches: only:` for relevant branches | WARN |

## Best Practice Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| BP1 | Orbs used for common patterns | `circleci/node`, `circleci/python`, etc. | INFO |
| BP2 | Commands abstracted for reuse | Define `commands:` for repeated step sequences | INFO |
| BP3 | Executors defined for shared config | Use `executors:` for consistent job environments | INFO |
| BP4 | Approval gates for production deploys | `type: approval` before production | WARN |
| BP5 | Workflow triggers are specific | Avoid running on every commit if not needed | INFO |
| BP6 | Test results stored | `store_test_results` for analytics | INFO |
| BP7 | Branch filtering on deploy jobs | Deploy only from main/release branches | WARN |

## Common Anti-Patterns

### 1. No Workspace Between Jobs
```yaml
# BAD: Each job rebuilds from scratch
jobs:
  build:
    steps:
      - run: npm install && npm run build
  test:
    steps:
      - run: npm install  # Redundant!
# Use workspaces to pass files between jobs
```

### 2. Missing Cache Strategy
```yaml
# BAD: Fresh download every run
steps:
  - run: npm install
# Add:
steps:
  - restore_cache:
      keys:
        - v1-deps-{{ checksum "package-lock.json" }}
  - run: npm install
  - save_cache:
      key: v1-deps-{{ checksum "package-lock.json" }}
      paths:
        - node_modules
```

### 3. Monolithic Workflow
```yaml
# BAD: Single job does everything
workflows:
  version: 2
  build_test_deploy:
    jobs:
      - everything
# Split into focused jobs with proper dependencies
```
