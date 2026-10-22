# Jenkinsfile Validation Checks

## Syntax Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| S1 | Valid Groovy syntax | File must parse as valid Declarative or Scripted Pipeline | FAIL |
| S2 | `pipeline { }` block present (Declarative) | Root block must be `pipeline` | FAIL |
| S3 | `agent` defined | Must specify where to run | FAIL |
| S4 | `stages { }` section exists | Must define at least one stage | FAIL |
| S5 | Stage names are unique | No duplicate stage names | FAIL |
| S6 | `steps { }` in each stage | Stages must contain executable steps | FAIL |
| S7 | `post { }` blocks valid | Only allowed at pipeline or stage level | FAIL |
| S8 | `when { }` conditions valid | Directive syntax must be correct | FAIL |
| S9 | No unclosed blocks | Balanced braces and parentheses | FAIL |
| S10 | Valid `environment { }` syntax | No invalid variable declarations | FAIL |

## Security Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| SEC1 | No hardcoded credentials | Use `credentials()` binding, not plaintext | FAIL |
| SEC2 | Credentials bound with `withCredentials` | Don't echo secrets in logs | FAIL |
| SEC3 | No `sh` commands with unsanitized input | Prevent command injection | FAIL |
| SEC4 | `checkout scm` used instead of hardcoded URLs | Prevent fetching from untrusted repos | FAIL |
| SEC5 | Agent labels restrict execution | Don't run on any available agent without restriction | WARN |
| SEC6 | Script approval reviewed for `@NonCPS` | Bypassed sandbox can be dangerous | WARN |
| SEC7 | No `writeFile` with external data without sanitization | Prevent path traversal | FAIL |
| SEC8 | `disableConcurrentBuilds()` for critical pipelines | Prevent race conditions on shared resources | WARN |

## Performance Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| P1 | Parallel stages used for independent work | `parallel { }` block | INFO |
| P2 | Workspace cleanup configured | `cleanWs()` or `wipeOut` | WARN |
| P3 | Artifact archival is selective | `archiveArtifacts` with specific patterns | WARN |
| P4 | Build timeout set | `timeout` step prevents hung builds | WARN |
| P5 | Stash/unstash used efficiently | Don't stash unnecessary files | INFO |
| P6 | Agent reuse for related stages | Same agent label avoids provisioning | INFO |
| P7 | Pipeline library shared code | Use Shared Libraries for common logic | INFO |

## Best Practice Checks

| # | Check | Rule | Severity |
|---|-------|------|----------|
| BP1 | Declarative Pipeline preferred over Scripted | Easier to read, validate, and maintain | WARN |
| BP2 | `options { }` block configured | BuildDiscarder, timeout, timestamps | INFO |
| BP3 | `triggers { }` defined for scheduled runs | Don't rely solely on manual triggers | INFO |
| BP4 | `parameters { }` for configurable values | Avoid hardcoded thresholds | INFO |
| BP5 | Post-build actions in `post { }` block | `always`, `success`, `failure`, `unstable` | INFO |
| BP6 | Input steps for approval gates | `input` before production deploys | WARN |
| BP7 | Notifications on failure | `mail`, `slack`, or `mattermost` in post | INFO |
| BP8 | No `catchError` swallowing failures | Errors should be visible, not hidden | WARN |
| BP9 | Pipeline version in `Jenkinsfile` header | Document required Jenkins version | INFO |

## Common Anti-Patterns

### 1. Scripted Pipeline When Declarative Would Suffice
```groovy
// BAD: Harder to validate, more error-prone
node {
    stage('Build') {
        sh 'make'
    }
}
// GOOD: Declarative is self-validating
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make'
            }
        }
    }
}
```

### 2. Credentials in Plain Text
```groovy
// BAD: Secret visible in config and build logs
sh 'curl -H "Authorization: Bearer sk-12345" https://api.example.com'
// GOOD: Bound to environment variable
withCredentials([string(credentialsId: 'api-token', variable: 'TOKEN')]) {
    sh 'curl -H "Authorization: Bearer $TOKEN" https://api.example.com'
}
```

### 3. No Parallel Execution
```groovy
// SLOW: Tests run sequentially
stage('Test') {
    steps {
        sh 'make test-unit'
        sh 'make test-integration'
        sh 'make test-e2e'
    }
}
// FAST: Run independent tests in parallel
stage('Test') {
    parallel {
        stage('Unit') { steps { sh 'make test-unit' } }
        stage('Integration') { steps { sh 'make test-integration' } }
        stage('E2E') { steps { sh 'make test-e2e' } }
    }
}
```
