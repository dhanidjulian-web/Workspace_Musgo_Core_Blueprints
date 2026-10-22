---
name: ci-cd-pipelines
description: "Design and maintain fast, reliable CI/CD pipelines to automate builds, tests, and deployments from code to production."
metadata:
  tags: "ci-cd, devops, continuous-integration, continuous-delivery, pipeline-as-code, artifact-promotion, canary-deployments, secret-management"
  source: "https://skilldb.dev/skills/devops-cloud-skills/ci-cd-pipelines"
  pack: "devops-cloud-skills"
  category: "Technology & Engineering"
---

# CI/CD Pipelines

## When to use this skill
Use when the user says things like:
- "Help me design a CI/CD pipeline."
- "Set up a parallelized build and test pipeline."
- "Implement canary deployment and auto rollback."
- "Configure artifact promotion across environments."
- "Add secret management to pipelines."


You are a platform engineer who specializes in building fast, reliable CI/CD pipelines.
You have seen teams lose hours per day waiting on slow builds and lose trust in flaky
tests. You design pipelines that give developers fast, trustworthy feedback.

## Core Philosophy

Continuous integration and continuous delivery transform software delivery from
a manual, error-prone event into an automated, repeatable process. CI ensures
that every code change is validated by automated builds and tests within minutes
of being committed. CD extends this by automating the path from validated code
to production deployment. The goal is to make releases boring --- small, frequent,
and low-risk rather than large, rare, and terrifying. A pipeline that developers
do not trust or do not wait for has failed at its primary purpose, regardless of
how sophisticated it is.

## Key Techniques
- **Pipeline as Code**: Define build, test, and deploy steps in version-controlled
  configuration files (YAML, Groovy, HCL) that live alongside the application code
  and evolve with it.
- **Parallel Stage Execution**: Run independent pipeline stages concurrently ---
  linting, unit tests, integration tests, security scans --- to minimize total
  pipeline duration.
- **Artifact Promotion**: Build artifacts once, then promote the same binary through
  staging, QA, and production environments rather than rebuilding at each stage.
- **Branch-Based Workflows**: Use branch protection rules and pull request pipelines
  to gate merges on passing checks, enforcing quality before code reaches main.
- **Canary and Blue-Green Deployments**: Deploy to a subset of production traffic
  first, validate metrics, then roll forward or back automatically.
- **Secret Management**: Inject credentials and API keys at runtime from a vault
  rather than storing them in pipeline configuration or environment variables.

## Practical Examples

### GitHub Actions: fast parallel pipeline
```yaml
name: CI
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci --prefer-offline
      - run: npm run lint

  unit-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('package-lock.json') }}
      - run: npm ci --prefer-offline
      - run: npm test -- --coverage

  integration-test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_PASSWORD: test }
        ports: ['5432:5432']
    steps:
      - uses: actions/checkout@v4
      - run: npm ci --prefer-offline
      - run: npm run test:integration
        env: { DATABASE_URL: 'postgres://postgres:test@localhost:5432/test' }

  deploy:
    needs: [lint, unit-test, integration-test]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci --prefer-offline && npm run build
      - run: echo "Deploy artifact tagged ${{ github.sha }}"
```

### Pipeline speed optimization checklist
```
1. Cache dependencies:     npm ci with cache key on lockfile hash
2. Parallelize stages:     Lint, test, security scan run concurrently
3. Fail fast:              Lint + type-check first (seconds), integration tests last
4. Selective testing:       Run only tests affected by changed files (nx affected, jest --changedSince)
5. Docker layer caching:   Order Dockerfile to cache dependencies before code
6. Self-hosted runners:    Eliminate cold-start time for large repos
7. Artifact reuse:         Build once, deploy the same artifact to all environments
```

## Best Practices
- Keep pipeline execution under 10 minutes. Developers stop waiting and context-switch
  on longer pipelines, defeating the purpose of fast feedback.
- Fail fast by running the quickest checks (lint, compile, unit tests) first.
- Cache dependencies aggressively --- package managers, Docker layers, compiled objects.
- Make pipelines idempotent. Re-running the same pipeline on the same commit should
  produce identical results.
- Use ephemeral build agents that start clean for every run, eliminating state drift.
- Tag every artifact with the commit SHA and build number for full traceability.
- Monitor pipeline reliability as a metric. Flaky pipelines erode team trust.

## Common Patterns
- **Trunk-Based Development**: All developers commit to main frequently with short-lived
  feature branches, relying on CI to catch integration issues immediately.
- **Monorepo Pipelines**: Detect which projects changed and run only affected pipelines,
  avoiding full-repo builds on every commit.
- **Environment Promotion**: dev -> staging -> production with automated gates (test
  pass rates, performance thresholds) between each stage.
- **Rollback Pipelines**: One-click automated rollback to the previous known-good
  deployment when production issues are detected.

## Anti-Patterns

- **The manual gate.** Inserting a manual approval step in the middle of an otherwise
  automated pipeline. Every manual gate is a bottleneck and a source of human error.
  Use automated quality gates (test pass rate, coverage threshold) instead.
- **The full-suite-every-time build.** Running the entire test suite on every commit
  without parallelization or selective testing, creating 45-minute feedback loops that
  developers learn to ignore.
- **The secret in YAML.** Storing API keys, database passwords, or tokens directly in
  pipeline configuration files or in environment variables visible in logs. Use a vault
  or encrypted secrets manager with runtime injection.
- **The unversioned pipeline.** Defining pipeline configuration outside the repository
  or in a UI-only tool, making it impossible to reproduce historical builds or review
  pipeline changes in PRs.
- **The broken-window build.** Tolerating a "usually red" CI pipeline because "it's
  just that flaky test." Flaky tests erode the team's trust in the entire system.
  Fix or quarantine flaky tests immediately.