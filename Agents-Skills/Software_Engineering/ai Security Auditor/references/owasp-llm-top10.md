# OWASP Top 10 for LLM Applications — Detailed Reference

## LLM01: Prompt Injection

### Attack Techniques
- **Direct injection**: User input contains instructions that override system prompt
- **Indirect injection**: Malicious content from external sources (web, email, docs) influences behavior
- **Token smuggling**: Encoded or obfuscated instructions bypass input filters
- **Payload splitting**: Attack split across multiple inputs to evade detection
- **Cross-plugin injection**: Injection via tool output that feeds back into LLM context

### Defense Strategies
- **Input validation**: Sanitize and validate all inputs before including in context
- **Instruction hierarchy**: Use system/user/assistant roles to establish clear boundaries
- **Delimiters**: Wrap user input in XML tags or special tokens that the LLM is trained to treat as data
- **Output filtering**: Post-process LLM output to detect and strip injected instructions
- **Human-in-the-loop**: Require approval for sensitive actions
- **Least privilege**: Minimize tool permissions to reduce blast radius

## LLM02: Insecure Output Handling

### Risk Scenarios
- LLM output passed to `eval()`, `exec()`, or similar dynamic execution
- LLM-generated SQL executed without parameterization
- LLM-generated HTML rendered without sanitization (XSS)
- LLM-generated shell commands executed without validation
- LLM output used in access control decisions

### Defense Strategies
- **Never eval LLM output**: Use structured output formats (JSON schema) instead
- **Parameterize queries**: All database operations must use parameterized statements
- **Sanitize HTML**: Use allowlist-based HTML sanitization for any LLM-generated markup
- **Command allowlisting**: Only execute from a predefined set of safe commands
- **Output validation**: Validate LLM output against expected schema before use

## LLM03: Training Data Poisoning

### Attack Vectors
- Fine-tuning on contaminated datasets
- RAG knowledge base injection with poisoned documents
- Pre-training data manipulation (supply chain)
- Reinforcement learning from malicious human feedback

### Defense Strategies
- **Data provenance**: Track source and integrity of all training/fine-tuning data
- **Data validation**: Scan training data for anomalous patterns or injected content
- **Access control**: Restrict who can add data to fine-tuning datasets
- **Model validation**: Test model behavior against known prompts after updates
- **Version control**: Pin model versions, don't use floating tags in production

## LLM04: Model Denial of Service

### Attack Vectors
- Extremely long prompts consuming context window and compute
- Recursive self-referential prompts causing infinite loops
- Complex reasoning chains consuming excessive tokens
- Batch request flooding

### Defense Strategies
- **Token budgets**: Set maximum tokens per request and per session
- **Rate limiting**: Implement request rate limits per user/IP
- **Timeout controls**: Set maximum execution time for LLM calls
- **Cost alerts**: Monitor spending and alert on anomalies
- **Input length limits**: Cap input size before sending to LLM

## LLM05: Supply Chain Vulnerabilities

### Risk Points
- Third-party model providers with unknown security practices
- Open-source plugins with compromised dependencies
- Pre-trained models with embedded backdoors
- Dataset providers with poisoned data
- MCP server providers with excessive permissions

### Defense Strategies
- **Vendor assessment**: Evaluate security practices of all third-party providers
- **Dependency scanning**: Regularly scan plugin/tool dependencies for CVEs
- **Model provenance**: Only use models from verified sources
- **Sandboxing**: Run untrusted plugins in isolated environments
- **Contractual SLAs**: Define security requirements in vendor contracts

## LLM06: Sensitive Information Disclosure

### Leakage Vectors
- System prompts containing API keys or credentials
- Training data containing PII or confidential information
- LLM memorization and regurgitation of sensitive training data
- Conversation history exposure in logs or analytics
- Tool output containing sensitive data passed to LLM context

### Defense Strategies
- **Secret management**: Never hardcode secrets in prompts or configs
- **Data masking**: Redact PII and sensitive data before including in context
- **Conversation TTL**: Auto-delete conversation history after defined period
- **Output filtering**: Scan LLM output for sensitive patterns before returning
- **Minimize context**: Only include data strictly needed for the task
- **Provider agreements**: Ensure LLM provider doesn't train on your data

## LLM07: Insecure Plugin Design

### Common Flaws
- Overly broad permission scopes (e.g., "full filesystem access")
- No input validation on plugin parameters
- No authentication between agent and plugin
- No rate limiting on plugin calls
- No audit logging of plugin usage

### Defense Strategies
- **Principle of least privilege**: Grant minimum permissions needed
- **Input validation**: Validate all parameters before execution
- **Authentication**: Require auth for sensitive plugin operations
- **Rate limiting**: Throttle plugin calls to prevent abuse
- **Audit logging**: Log all plugin invocations with parameters and results
- **Sandboxing**: Execute plugins in isolated environments

## LLM08: Excessive Agency

### Risk Scenarios
- Agent autonomously modifies production systems
- Agent sends emails/messages without human review
- Agent makes financial transactions
- Agent changes access controls or permissions
- Agent deploys code without approval

### Defense Strategies
- **Action classification**: Categorize actions by risk level
- **Approval gates**: Require human approval for high-risk actions
- **Reversibility check**: Only allow autonomous execution of reversible actions
- **Audit trails**: Log all agent actions for review
- **Agency escalation**: Start with read-only, gradually increase permissions
- **Circuit breakers**: Automatically disable agent if anomalous behavior detected

## LLM09: Overreliance

### Risk Scenarios
- Blind acceptance of LLM output without verification
- Using LLM for safety-critical decisions without human oversight
- Deploying LLM-generated code without review
- Trusting LLM calculations without validation
- Using LLM for legal/medical/financial advice without expert review

### Defense Strategies
- **Output verification**: Independent verification of critical outputs
- **Human review**: Mandatory human review for safety-critical decisions
- **Confidence scoring**: Assess LLM confidence before acting on output
- **Fallback mechanisms**: Have non-LLM fallback for critical operations
- **Domain constraints**: Limit LLM use to domains where it's been validated

## LLM10: Model Theft

### Attack Vectors
- Model extraction via adversarial queries
- Prompt extraction to replicate behavior
- Model weight theft from insecure storage
- API key theft leading to unauthorized model access

### Defense Strategies
- **Rate limiting**: Throttle queries to prevent extraction attacks
- **Output watermarking**: Detect when model output is being used for extraction
- **Access controls**: Restrict model access to authorized users only
- **Secure storage**: Encrypt model weights and configuration
- **Monitoring**: Detect unusual query patterns that suggest extraction attempts
