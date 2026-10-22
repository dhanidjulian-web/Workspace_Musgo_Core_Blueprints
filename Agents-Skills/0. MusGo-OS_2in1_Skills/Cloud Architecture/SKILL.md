---
name: cloud-architecture
description: "Architect scalable, resilient cloud systems by applying multi-AZ, managed services, auto-scaling, and event-driven patterns to optimize cost and reliability."
metadata:
  tags: "cloud-architecture, cloud-computing, scalability, design-patterns, security, cost-optimization, reliability"
  source: "https://skilldb.dev/skills/devops-cloud-skills/cloud-architecture"
  pack: "devops-cloud-skills"
  category: "Technology & Engineering"
---

# Cloud Architecture

## When to use this skill
Use when the user says things like:
- "I need a cloud architecture design"
- "Show me how to build scalable cloud systems"
- "What are best practices for multi-AZ and auto-scaling"
- "How do I use managed services over self-hosting"
- "I want a Well-Architected review checklist"


## Core Philosophy
Cloud architecture is the discipline of designing systems that leverage cloud
platform capabilities — elastic compute, managed services, global infrastructure —
to achieve scalability, resilience, and operational efficiency that would be
impractical to build on-premises. Good cloud architecture makes deliberate tradeoffs
between cost, performance, reliability, and complexity based on actual business
requirements rather than theoretical maximums.

## Key Techniques
- **Multi-AZ Deployment**: Distribute workloads across multiple availability zones
  within a region to survive individual data center failures without manual
  intervention.
- **Managed Services Over Self-Hosted**: Use cloud-native databases, queues, and
  compute services to offload operational burden. Build on RDS rather than managing
  your own PostgreSQL cluster.
- **Auto-Scaling Groups**: Configure compute resources to scale horizontally based
  on demand metrics, paying only for capacity actually needed.
- **Event-Driven Architecture**: Use serverless functions, message queues, and
  event buses to decouple components and handle variable workloads efficiently.
- **Landing Zone Pattern**: Establish a multi-account structure with centralized
  networking, security, and governance before deploying workloads.
- **Well-Architected Reviews**: Regularly evaluate architectures against cloud
  provider frameworks (AWS Well-Architected, GCP Architecture Framework) across
  pillars of reliability, security, cost, performance, and operations.

## Best Practices
- Design for failure. Every component will eventually fail; architect so that
  failures are isolated and recovery is automatic.
- Use the smallest instance type that meets requirements and scale horizontally
  rather than vertically.
- Encrypt data at rest and in transit by default. Use cloud KMS for key management.
- Implement least-privilege IAM. No service or user should have more permissions
  than needed for their specific function.
- Use private subnets for workloads and expose only load balancers and API gateways
  to the public internet.
- Tag resources consistently for cost allocation, ownership, and lifecycle management.
- Architect for the cloud you are on. Do not replicate on-premises patterns in
  the cloud; leverage cloud-native services and paradigms.

## Common Patterns
- **Three-Tier Architecture**: Load balancer → application servers → managed
  database, each tier independently scalable and replaceable.
- **Microservices on Containers**: Decompose applications into independently
  deployable services running in orchestrated containers.
- **Data Lake**: Centralize raw data in object storage with schema-on-read,
  enabling diverse analytics workloads without upfront data modeling.
- **Multi-Region Active-Active**: Serve traffic from multiple regions simultaneously
  for global low-latency access and regional failure resilience.

## Anti-Patterns
- Lift-and-shift without rearchitecting. Running VMs in the cloud like they are
  on-premises wastes cloud capabilities and often costs more.
- Over-engineering for scale that will never materialize. Start simple and add
  complexity only when load demands it.
- Ignoring cloud costs until the bill arrives. Implement cost monitoring and
  budgets from day one.
- Hardcoding region-specific resources. Design for portability across regions
  and accounts.
- Running everything as a single monolith on a massive instance rather than
  decomposing into appropriate service boundaries.
- Neglecting security in favor of speed. A misconfigured S3 bucket or open
  security group can expose the entire organization.