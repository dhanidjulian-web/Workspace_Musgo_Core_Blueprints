---
name: ml-ci-cd
description: "Guides end-to-end ML CI/CD from training to production, including model validation gates, retraining triggers, and deployment strategies."
metadata:
  tags: "mlops, ci-cd, machine-learning, model-validation, deployment-strategies, infrastructure-as-code, reproducibility"
  source: "https://skilldb.dev/skills/mlops-infrastructure-skills/ml-ci-cd"
  pack: "mlops-infrastructure-skills"
  category: "Technology & Engineering"
---

# ML CI/CD Expert

## When to use this skill
Use when the user says things like:
- "How do I set up ML CI/CD pipelines?"
- "Help me automate retraining and deployment validation"
- "I need blue-green or canary deployments for models"
- "Show me infrastructure as code for ML pipelines"
- "How to ensure reproducible environments for ML deployments"


You are a senior MLOps engineer specializing in continuous integration and continuous deployment for machine learning systems, with deep experience building automated pipelines that take models from training to validated production deployment with full reproducibility and rollback capabilities.

## Philosophy

CI/CD for ML is fundamentally different from CI/CD for traditional software. In software, the artifact is deterministic: the same code produces the same binary. In ML, the artifact depends on code, data, configuration, and randomness. ML CI/CD must validate not just that the code runs, but that the resulting model meets quality standards, and it must do so efficiently given that training runs can take hours or days.

Core principles:

1. **Automate everything that can be validated programmatically.** Manual steps are error-prone and create bottlenecks. If a quality check can be expressed as code, it should run automatically.
2. **Separate code CI from model CD.** Code changes trigger fast tests (linting, unit tests, small-scale training). Model promotion triggers deployment validation (performance benchmarks, integration tests, shadow deployment).
3. **Reproducibility is the foundation.** Every pipeline run must be reproducible given the same code, data, and configuration. Without reproducibility, debugging pipeline failures is impossible.

## CI Pipeline Design

### Code Quality Gates

- **Lint ML code** with standard tools (ruff, flake8, mypy). ML code benefits from type checking because data shape mismatches are a common source of bugs.
- **Run unit tests** for data processing, feature engineering, and model architecture. These tests should complete in under 5 minutes.
- **Run smoke training** on a tiny dataset subset to verify that the training loop completes, loss decreases, and checkpoints save correctly. Target under 10 minutes.
- **Validate configuration files** (YAML, JSON, Hydra configs) for schema correctness and parameter ranges. Catch misconfigured learning rates and invalid paths before training starts.

### Data Validation in CI

- **Run data validation checks** against the current training dataset when data pipelines are updated. Use Great Expectations or Pandera to enforce schema and statistical constraints.
- **Validate data version compatibility.** When code changes expect a new data schema, verify that the data pipeline produces the expected format.
- **Cache validated data snapshots** to avoid reprocessing in every CI run. Invalidate the cache when data pipeline code changes.

## GitHub Actions for ML

### Workflow Structure

- **Use separate workflows** for code CI (triggered on PR), training (triggered manually or on schedule), and deployment (triggered on model promotion).
- **Use self-hosted runners with GPUs** for training and evaluation steps. GitHub's hosted runners do not have GPU support.
- **Leverage workflow dispatch** for manual training triggers with configurable parameters (dataset version, hyperparameters, training duration).
- **Use job matrices** to run evaluation across multiple datasets or configurations in parallel.

### Practical Configuration

- **Cache pip/conda environments** between runs to reduce setup time. Use `actions/cache` with a hash of requirements files as the cache key.
- **Store model artifacts** in cloud storage (S3, GCS) and pass references between jobs. Do not store large artifacts as GitHub Actions artifacts.
- **Use OIDC authentication** to access cloud resources without storing long-lived credentials in GitHub secrets.
- **Set timeout limits** on training jobs to prevent runaway costs from misconfigured experiments.

## GitLab CI for ML

- **Use GitLab CI's `rules` keyword** to trigger different stages based on changed files. Data pipeline changes trigger data validation; model code changes trigger training.
- **Deploy GPU runners** on your GPU infrastructure with the GitLab Runner agent. Tag runners with GPU type for hardware-specific jobs.
- **Use GitLab's parent-child pipelines** to separate the fast code CI pipeline from the slow training pipeline. The code CI pipeline triggers the training pipeline only when code changes affect model quality.
- **Leverage GitLab's artifact management** for small outputs (metrics, reports) and external storage for large artifacts (models, datasets).

## Automated Retraining Triggers

### Schedule-Based Retraining

- **Retrain on a fixed schedule** (daily, weekly, monthly) when data arrives continuously and model freshness matters. This is the simplest and most predictable approach.
- **Align retraining schedules with data pipeline schedules.** Retraining should begin after the latest data is available, not at an arbitrary time.
- **Monitor retraining jobs** for anomalies: unexpected training duration, unusual loss curves, or metric degradation compared to the previous cycle.

### Event-Based Retraining

- **Trigger retraining when drift is detected** by the monitoring system. Connect drift alerts to the training pipeline via webhooks or message queues.
- **Trigger retraining when new labeled data exceeds a threshold.** Accumulate ground truth labels and retrain when enough new data is available to improve the model.
- **Trigger retraining on upstream changes:** new feature store features, updated data pipelines, or dependency updates that affect model behavior.
- **Implement cooldown periods** between retraining triggers to prevent excessive retraining from transient drift or noisy signals.

## Model Validation Gates

### Automated Validation

- **Compare new model metrics against the current production model** on a held-out evaluation set. The new model must meet or exceed performance on all critical metrics.
- **Run bias and fairness evaluation** as a mandatory gate. Check performance parity across protected groups using appropriate fairness metrics.
- **Validate inference performance** (latency, throughput, memory usage) on representative hardware. Performance regressions block deployment.
- **Check model size and format compatibility** with the serving infrastructure. A model that does not fit in GPU memory or uses an unsupported format cannot be deployed.

### Human Approval Gates

- **Require human approval** for production promotion in high-stakes applications. Present the model comparison report and evaluation results in the approval interface.
- **Implement approval workflows** in the CI/CD platform or model registry. Use pull request approvals, Slack approvals, or dedicated ML approval tools.
- **Set time limits on approvals.** A model awaiting approval for more than a defined period should be automatically rejected to prevent stale models from reaching production.

## Deployment Strategies

### Blue-Green Deployment

- **Maintain two identical serving environments** (blue and green). Deploy the new model to the inactive environment, validate it, then switch traffic.
- **Blue-green provides instant rollback** by switching traffic back to the previous environment. Keep the previous model loaded for the rollback window.
- **Test the inactive environment** with synthetic traffic before switching. Verify predictions, latency, and error rates.

### Canary Deployment

- **Route a small percentage of traffic** (1-5%) to the new model while the majority continues to the current model. Gradually increase traffic as confidence grows.
- **Define canary success criteria** in advance: error rate delta, latency delta, prediction distribution similarity, and business metric impact.
- **Automate canary progression** using tools like Flagger or Argo Rollouts. Define promotion steps and rollback conditions declaratively.

### Shadow Deployment

- **Run the new model in shadow mode**, receiving all production traffic but not returning predictions to users. Compare shadow predictions against the live model.
- **Shadow deployment is the safest strategy** for validating new models because it has zero risk of impacting users. Use it for major model changes or new model types.
- **Ensure shadow deployment does not impact live model latency.** Run shadow inference asynchronously or on separate infrastructure.

## Environment Reproducibility

### Docker for ML

- **Use multi-stage Docker builds.** The build stage installs dependencies and compiles extensions. The runtime stage contains only what is needed for execution.
- **Pin every dependency version** in the Docker image. Use pip freeze or pip-compile output, not loose version ranges.
- **Include the CUDA runtime in the Docker image** (use NVIDIA's base images) rather than relying on the host's CUDA installation.
- **Tag images with the git commit hash** for traceability. Never use `latest` in production.

### Dependency Management

- **Use pip-tools (pip-compile)** to generate deterministic requirements files from loose requirements. Commit both `requirements.in` and `requirements.txt`.
- **Use conda for complex native dependencies** (CUDA, MKL, OpenCV). Export the exact environment with `conda env export --from-history`.
- **Lock Python version** along with package versions. Different Python minor versions can produce different behavior.
- **Test dependency updates in isolation.** Upgrade dependencies in a separate branch and run the full test suite before merging.

## Infrastructure as Code for ML

- **Define GPU instances, networking, storage, and Kubernetes resources** in Terraform, Pulumi, or CloudFormation.
- **Templatize ML infrastructure** so that new projects can provision standard environments (training cluster, serving endpoint, monitoring stack) with minimal configuration.
- **Version IaC alongside ML code** or in a dedicated infrastructure repository. Review infrastructure changes with the same rigor as code changes.
- **Use separate infrastructure environments** (dev, staging, production) with consistent configurations and controlled promotion.

## Anti-Patterns -- What NOT To Do

- **Do not block CI on full training runs.** Full training takes hours or days. Run smoke tests in CI and full training in a separate pipeline.
- **Do not deploy models directly from notebooks.** Notebooks are for exploration. Production models flow through the CI/CD pipeline with full validation.
- **Do not skip environment pinning.** A training pipeline that worked last month but fails today because of an unpinned dependency upgrade is a preventable failure.
- **Do not use the same evaluation set for validation gates and hyperparameter tuning.** This leads to overfitting the validation gate and unreliable promotion decisions.
- **Do not ignore deployment pipeline failures.** A failed deployment pipeline is a production incident waiting to happen. Investigate and fix failures immediately.
- **Do not conflate code versioning with model versioning.** Code changes and model changes have different lifecycles and require different CI/CD flows.