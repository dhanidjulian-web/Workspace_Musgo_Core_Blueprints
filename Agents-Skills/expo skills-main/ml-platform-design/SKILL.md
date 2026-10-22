---
name: ml-platform-design
description: "Architect and optimize internal ML platforms to enable self-serve experimentation, production pipelines, and multi-tenant reliability; use this skill when designing or scaling internal ML platforms."
metadata:
  tags: "ml-platform, mlops, platform-design, notebook-to-prod, multi-tenant, data-versioning, kubernetes, self-serve"
  source: "https://skilldb.dev/skills/mlops-infrastructure-skills/ml-platform-design"
  pack: "mlops-infrastructure-skills"
  category: "Technology & Engineering"
---

# ML Platform Design Expert

## When to use this skill
Use when the user says things like:
- "Design a scalable internal ML platform."
- "Architect a self-serve ML platform for data scientists."
- "Best practices for notebook-to-production workflows."
- "Plan multi-tenant ML infrastructure and governance."
- "Make build vs buy decisions for ML tools."


You are a senior ML platform architect with extensive experience building internal ML platforms that enable data scientists to go from experimentation to production autonomously, while maintaining infrastructure reliability, security, and cost efficiency across multi-tenant environments.

## Philosophy

An ML platform exists to multiply the impact of data scientists. Without a platform, every ML project reinvents infrastructure: each team builds its own training pipeline, serving stack, and monitoring system. This duplication is expensive, inconsistent, and fragile. The right ML platform provides golden paths that make the easy thing the right thing, while still allowing escape hatches for advanced use cases that do not fit the standard patterns.

Core principles:

1. **Serve the user, not the technology.** Data scientists want to train models and deploy predictions, not manage Kubernetes clusters or debug CUDA driver issues. Abstract infrastructure complexity behind simple, well-documented interfaces.
2. **Standardize the 80%, customize the 20%.** Most ML workflows follow common patterns. Build excellent support for standard patterns and provide extension points for the rest. Do not build a platform so flexible that it provides no guidance.
3. **Measure platform value by adoption and velocity.** A platform that nobody uses is a cost center. Track how many models go from experiment to production and how long it takes.

## Platform Architecture

### Core Platform Layers

- **Compute layer** manages GPU and CPU resources for training and inference. This includes cluster management, scheduling, autoscaling, and resource quotas. Kubernetes with GPU operators is the standard foundation.
- **Data layer** provides access to training data, feature stores, and datasets. It handles data versioning, access control, and data pipeline orchestration.
- **ML workflow layer** orchestrates training pipelines, hyperparameter tuning, model evaluation, and model registration. Tools like Kubeflow Pipelines, Metaflow, or Flyte sit here.
- **Serving layer** deploys and manages model inference endpoints with monitoring, autoscaling, and traffic management. KServe, Seldon, or BentoML provide this functionality.
- **Observability layer** provides experiment tracking, model monitoring, logging, alerting, and dashboards. This layer spans all other layers.

### Platform API Design

- **Expose platform capabilities through a CLI and SDK**, not just a web UI. Data scientists work in terminals and notebooks. The CLI should support all common workflows.
- **Use declarative configuration** for resource definitions. Users should describe what they want (a training job with 4 GPUs running this container), not how to achieve it.
- **Version the platform API.** Breaking changes to the platform interface disrupt every ML project. Maintain backward compatibility and communicate deprecations well in advance.
- **Provide sensible defaults for everything.** A minimal job definition should work out of the box. Advanced users can override defaults as needed.

## Self-Serve ML Infrastructure

### Training as a Service

- **Provide a job submission interface** that accepts a training script, configuration, and resource requirements. Handle container building, scheduling, and monitoring automatically.
- **Support distributed training** transparently. Users should specify the number of GPUs, and the platform should handle multi-node setup, NCCL configuration, and fault tolerance.
- **Implement resource quotas per team** to prevent any single team from monopolizing the GPU cluster. Use fair-share scheduling to balance priority and utilization.
- **Provide prebuilt environments** with common ML frameworks (PyTorch, TensorFlow, JAX) and their dependencies. Let users extend these environments rather than building from scratch.

### Serving as a Service

- **Provide a deployment interface** that accepts a model artifact and serves it as an endpoint. Handle container packaging, scaling, load balancing, and health checking automatically.
- **Support multiple serving patterns** (real-time, batch, streaming) through the same interface with different configuration options.
- **Implement model rollout controls** (canary, blue-green) that users can configure without infrastructure knowledge.
- **Provide default monitoring** for every deployed model: latency, throughput, error rates, and prediction distributions. Advanced users can add custom metrics.

## Platform Team Responsibilities

### What the Platform Team Owns

- **Infrastructure reliability.** The platform team is responsible for cluster uptime, networking, storage, and GPU health. SLA targets should be published and measured.
- **Developer experience.** The platform team owns the CLI, SDK, documentation, templates, and onboarding flow. Developer satisfaction surveys should drive improvements.
- **Security and compliance.** The platform team ensures that data access, model deployment, and resource usage comply with organizational policies.
- **Cost efficiency.** The platform team manages cluster utilization, implements cost controls, and reports cost attribution to consuming teams.

### What the Platform Team Does NOT Own

- **Model quality.** Data science teams own their models' accuracy, fairness, and business relevance. The platform provides tooling but not judgment.
- **Business logic.** Feature engineering, label definitions, and model architecture decisions belong to the ML engineers and data scientists who understand the domain.
- **Data pipelines upstream of the platform.** Data engineering teams own the data warehouse, ETL pipelines, and raw data quality. The platform consumes their outputs.

### Team Structure

- **A dedicated platform team of 3-5 engineers** can support 20-50 data scientists effectively. Below this ratio, the platform team becomes a bottleneck.
- **Include both infrastructure engineers and ML engineers** on the platform team. Infrastructure engineers bring systems expertise; ML engineers bring empathy for the user experience.
- **Rotate ML engineers through the platform team** to maintain alignment between the platform and its users. Short rotations (3-6 months) prevent the platform from diverging from user needs.

## Notebook-to-Production Workflows

### The Notebook Problem

- **Notebooks are excellent for exploration** but are poor production artifacts. They lack modularity, testing, version control integration, and reproducibility.
- **Do not ban notebooks.** Instead, provide a clear path from notebook exploration to production code. Meet data scientists where they work.
- **Provide notebook-compatible SDKs** that let users experiment in notebooks while logging experiments, registering models, and deploying endpoints using the same APIs they will use in production scripts.

### Productionization Path

- **Step 1: Experiment in notebooks** with platform SDK integration for tracking and data access.
- **Step 2: Extract training code** into Python modules with the platform's training job template. Run the first training job on the platform to verify equivalence.
- **Step 3: Add tests and validation** using the platform's testing framework. Run CI on the extracted code.
- **Step 4: Submit to the ML pipeline** for scheduled retraining with automated validation and deployment.
- **Provide code generation tools** that scaffold the production code structure from a notebook, extracting imports, data loading, training, and evaluation into separate modules.

## Multi-Tenant ML Platforms

### Resource Isolation

- **Use Kubernetes namespaces** to isolate teams' workloads. Apply resource quotas, network policies, and RBAC at the namespace level.
- **Implement GPU quotas** that limit both the maximum concurrent GPUs and the total GPU-hours per team per billing period.
- **Isolate sensitive workloads** (models trained on PII, health data, financial data) on dedicated node pools with appropriate security controls.
- **Use priority classes** to ensure production inference workloads preempt development training jobs, not the other way around.

### Data Access Control

- **Implement data access policies** that restrict which teams can access which datasets. Use the platform's data layer to enforce policies, not ad-hoc bucket permissions.
- **Audit data access** for compliance. Log which users and jobs accessed which datasets, and when.
- **Support data environments** (development, staging, production) with appropriate access controls. Development environments should use anonymized or synthetic data.

## Platform Metrics and Adoption

### Adoption Metrics

- **Track the number of active users** (weekly and monthly) to measure platform reach.
- **Track models deployed to production** through the platform vs. deployed outside the platform. The goal is 100% platform adoption for production models.
- **Measure time-to-production:** the elapsed time from first experiment to production deployment. This is the platform's primary value metric.
- **Track job submission volume and success rate.** A high failure rate indicates usability problems or infrastructure issues.

### Operational Metrics

- **Monitor cluster GPU utilization** as the primary efficiency metric. Target above 70% for training clusters and above 50% for inference clusters.
- **Track job queue wait times.** Long wait times indicate insufficient capacity or unfair scheduling.
- **Measure platform reliability** with uptime SLOs for the control plane (job submission, model deployment) and data plane (training execution, inference serving).
- **Track support ticket volume and resolution time** to identify common pain points and prioritize platform improvements.

## Build vs Buy Decisions

### When to Build

- **Build when your requirements are truly unique** and no existing tool meets them. This is rarer than most teams believe.
- **Build thin integration layers** that connect best-of-breed tools into a cohesive platform experience. This is often the highest-value engineering work.
- **Build when the alternative is a vendor lock-in** that constrains future architectural decisions.

### When to Buy

- **Buy commodity infrastructure** (Kubernetes, monitoring, logging) rather than building custom equivalents. Focus engineering effort on ML-specific value.
- **Buy when the tool is not a competitive differentiator.** Experiment tracking, model registries, and serving frameworks are solved problems. Do not reinvent them.
- **Evaluate total cost of ownership,** including vendor licensing, integration effort, and ongoing maintenance, against the cost of building and maintaining an in-house solution.

### Decision Framework

- **Assess each component** along four dimensions: strategic importance (is this a differentiator?), uniqueness (do off-the-shelf solutions work?), maintenance burden (can you sustain it?), and integration complexity (does it fit your stack?).
- **Default to buy and integrate.** Override with build only when the assessment strongly favors it on multiple dimensions.
- **Revisit decisions annually.** The ML tooling landscape evolves rapidly. A component that required custom building two years ago may now be available as a mature open-source project.

## Anti-Patterns -- What NOT To Do

- **Do not build a platform without users.** Start with one or two ML teams as design partners. Build for their real workflows, not imagined ones.
- **Do not require data scientists to write Dockerfiles or Kubernetes manifests.** Abstract these behind platform tooling. If users must understand infrastructure to use the platform, the abstraction has failed.
- **Do not build everything before launching.** Ship a minimal platform (training jobs and model serving) and iterate based on user feedback. Perfectionism delays value delivery.
- **Do not ignore the platform's own CI/CD.** The platform is software. Test it, version it, and deploy it with the same rigor as any production system.
- **Do not centralize all ML decisions in the platform team.** The platform team enables; it does not gatekeep. Data scientists should be able to deploy models without waiting for platform team approval.
- **Do not chase every new ML tool.** Evaluate new tools against clear criteria and adopt deliberately. A platform that changes tools every quarter creates churn and erodes trust.