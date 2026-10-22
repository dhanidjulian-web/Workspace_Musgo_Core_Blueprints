# Skill Install Safety Gate Output Contract

This contract defines required outputs for `skill-install-safety-gate`.

## JSON Contract

The main JSON output must preserve these top-level fields in this order:

1. `input`
2. `package_summary`
3. `compatibility_checks`
4. `security_findings`
5. `install_plan`
6. `install_result`
7. `gate_decision`
8. `assumptions`
9. `next_steps`
10. `generated_at`

### Field Notes

- `input` records the supplied source, target directory, target runtime, and install-on-pass flag.
- `package_summary` records package type, discovered skill root, skill name, description, version, file count, size, script presence, and declared requirements.
- `compatibility_checks` records pass/review/block checks for installability and host readiness.
- `security_findings` records static risk findings with severity, category, evidence, recommendation, and decision impact.
- `install_plan` records whether the package would be copied and where.
- `install_result` records `installed`, `skipped`, or `blocked`.
- `gate_decision` records `allow`, `review`, or `block`.
- `assumptions` and `next_steps` must not claim malware proof, certification, or runtime safety.

## Markdown Sections

The Markdown report must contain these sections in this order:

1. `Package Summary`
2. `Gate Decision`
3. `Compatibility Checks`
4. `Security Findings`
5. `Install Plan`
6. `Install Result`
7. `Assumptions`
8. `Next Steps`

## CSV Outputs

### `security-findings.csv`

Columns:

- `id`
- `severity`
- `category`
- `title`
- `file`
- `evidence`
- `recommendation`
- `decision_impact`

Rows must match `security_findings`.

### `compatibility-checks.csv`

Columns:

- `id`
- `status`
- `check`
- `detail`
- `evidence`

Rows must match `compatibility_checks`.

## Install Receipt

When `--out-install-receipt` is supplied, write JSON containing:

- `gate_decision`
- `install_result`
- `package_summary`
- `generated_at`

The receipt should be written whether the install was completed or skipped.

## Gate Policy

- `allow`: no compatibility checks with `block`, no compatibility checks with `review`, no security findings with `block`, and no security findings with `review`.
- `review`: no blockers, but at least one compatibility review item or security review item.
- `block`: any compatibility blocker or security blocker.
- Security findings with decision impact `warn` do not prevent `allow`.
- `--install-on-pass` may copy only when decision is `allow`.
- `review` and `block` must never copy files into the target skill directory.

## Guardrails

- Do not execute source package code during scan or install.
- Do not run install hooks, dependency installers, or bundled binaries.
- Do not overwrite existing target skill folders.
- Do not treat a clean static result as malware-free certification.
- Do not write secret values into JSON, Markdown, CSV, receipt, or console output.
