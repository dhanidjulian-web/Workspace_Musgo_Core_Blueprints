Building Claude Agent Skills - AI Skill Graded A- 

Skill created and graded
AI Skill Report Card
Building Claude Agent Skills
Creates and structures Claude Code agent skills following best practices. Use when building agent capabilities, documenting workflows, or packaging expertise into reusable skills.

A-85
·
Jun 14, 2026
·
Source: Web
Quick Start
15 / 15
YAML
---
name: analyzing-data-trends
description: Analyzes time-series data to identify patterns and anomalies. Use when examining datasets for insights or trend detection.
---

# Data Trend Analysis
Quick Start
15 / 15
Python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
trend = df.rolling(window=7).mean()
plt.plot(df.index, df.values, alpha=0.3)
plt.plot(trend.index, trend.values, linewidth=2)
plt.show()
Workflow
15 / 15
Load and clean data
Convert to time series format
Apply smoothing techniques
Identify patterns and outliers
Generate visualizations
Workflow
15 / 15
Progress:

 Analyze the expertise/methodology to extract
 Create YAML frontmatter with gerund name and trigger-based description
 Write Quick Start with immediate actionable example
 Document step-by-step workflow with checklist format
 Provide concrete input/output examples
 List best practices and common pitfalls
 Keep under 500 lines, be concise and specific
Examples
17 / 20
Example 1: Input: "I help companies optimize their database queries for better performance" Output:

YAML
---
name: optimizing-database-queries
description: Analyzes and improves SQL query performance through indexing and restructuring. Use when queries are slow or database performance needs improvement.
---

# Database Query Optimization
Quick Start
15 / 15
SQL
-- Before: Slow query
SELECT * FROM orders WHERE customer_id = 123 AND order_date > '2024-01-01';

-- After: Optimized with index
CREATE INDEX idx_customer_date ON orders(customer_id, order_date);
SELECT order_id, total FROM orders WHERE customer_id = 123 AND order_date > '2024-01-01';

**Example 2:**
Input: "Expert in reviewing pull requests and ensuring code quality"
Output:
```yaml
---
name: reviewing-code-quality
description: Conducts thorough code reviews focusing on maintainability, security, and performance. Use when evaluating pull requests or auditing codebases.
---

# Code Quality Review
Quick Start
15 / 15
Review checklist:

 Code follows style guidelines
 No security vulnerabilities
 Proper error handling
 Unit tests included
 Documentation updated
Best Practices
Use gerund naming: analyzing-data, writing-documentation, debugging-applications
Include triggers in description: "Use when [specific scenario]"
Start with executable examples: Code, commands, or concrete steps
Provide checklists for complex workflows: Use - [ ] format for trackable progress
Be implementation-focused: Show HOW, not just WHAT
Default to single best approach: Avoid option paralysis
Target practitioners: Assume technical competence, focus on methodology
Common Pitfalls
Vague descriptions: "Helps with data" vs "Analyzes customer churn patterns in subscription data"
Missing triggers: Description should explain WHEN to use the skill
Abstract examples: Show real input/output, not placeholders
Over-explanation: Don't define common terms or basic concepts
Analysis paralysis: Give one recommended approach, not multiple options
Passive voice: Use active voice and action-oriented language
Too generic: Skills should capture specific expertise, not general capabilities
