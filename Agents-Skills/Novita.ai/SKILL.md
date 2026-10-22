---
name: novitaai
description: Use when integrating hosted AI models via APIs, running code in isolated agent sandboxes, deploying GPU infrastructure, or managing LLM requests with streaming, batching, and advanced features like function calling and structured outputs.
metadata:
    mintlify-proj: novitaai
    version: "1.0"
---

# Novita AI Skill

## Product Summary

Novita AI provides three core services: hosted model APIs (LLMs, image/video/audio generation), agent sandboxes (isolated execution environments for code and browsers), and GPU infrastructure (persistent instances and serverless endpoints). Access models via OpenAI-compatible REST APIs using Bearer token authentication. The primary docs site is https://docs.novita.ai. Key endpoints: `https://api.novita.ai/openai/v1/chat/completions` (LLM), `https://api.novita.ai/openai/v1/completions` (text completion). Authentication uses `Authorization: Bearer <API_KEY>` header. API keys are created in the console at https://novita.ai/settings/key-management and stored as `NOVITA_API_KEY` environment variable.

## When to Use

Reach for this skill when:

- **Calling LLM APIs**: User asks to integrate language models (chat, completion, embeddings, reasoning, vision, function calling, structured outputs).
- **Streaming responses**: User needs real-time token generation or long-running inference.
- **Batch processing**: User wants to submit multiple requests asynchronously (batch API with 48-hour completion window).
- **Running agent code**: User needs an isolated sandbox to execute code, install packages, run browsers, or preserve state across sessions.
- **GPU workloads**: User wants to deploy models on dedicated GPUs (persistent instances) or serverless endpoints (auto-scaling inference).
- **Image/video/audio generation**: User requests image synthesis, video generation, text-to-speech, or voice cloning.
- **Rate limits or quota management**: User hits limits and needs to understand tier-based RPM/TPM or request increases.
- **Troubleshooting API errors**: User receives 401, 403, 429, 503, or 500 responses and needs diagnosis.
- **Model access control**: User needs to restrict which models an API key can call or which IPs can use it.

## Quick Reference

### API Endpoints

| Task | Endpoint | Method |
|------|----------|--------|
| Chat completion | `/openai/v1/chat/completions` | POST |
| Text completion | `/openai/v1/completions` | POST |
| Embeddings | `/openai/v1/embeddings` | POST |
| Batch create | `/openai/v1/batches` | POST |
| Batch status | `/openai/v1/batches/{batch_id}` | GET |
| List models | `/openai/v1/models` | GET |

### Authentication

```bash
# Set API key as environment variable
export NOVITA_API_KEY="sk_..."

# Use in curl
curl "https://api.novita.ai/openai/v1/chat/completions" \
  -H "Authorization: Bearer $NOVITA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek/deepseek-v4.1-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

### Common Models

| Model | Use Case |
|-------|----------|
| `deepseek/deepseek-v4.1-flash` | Fast, general-purpose LLM |
| `deepseek/deepseek-v4.1` | High-quality reasoning |
| `qwen/qwen-2.5-72b` | Multilingual, code-heavy tasks |
| `meta-llama/llama-3.1-405b` | Large-scale reasoning |
| `claude-3.5-sonnet` | Anthropic model via Novita |

### Sandbox Regions

| Region | Version | Domain | Notes |
|--------|---------|--------|-------|
| us-phx-1 | v2 | `us-phx-1.sandbox.novita.ai` | Default, recommended (secrets, snapshots) |
| us-virginia-1 | v1 | `sandbox.novita.ai` | Legacy, set `NOVITA_DOMAIN=sandbox.novita.ai` |

### Rate Limits by Tier

| Tier | Criteria | RPM | TPM |
|------|----------|-----|-----|
| T1 | <$50/month | 60 | 90k |
| T2 | $50–$500/month | 300 | 450k |
| T3 | $500–$3k/month | 1000 | 1.5M |
| T4 | $3k–$10k/month | 3000 | 4.5M |
| T5 | ≥$10k/month | 10000 | 15M |

## Decision Guidance

### When to Use Streaming vs. Non-Streaming

| Scenario | Use Streaming | Use Non-Streaming |
|----------|---------------|-------------------|
| Long outputs (>1000 tokens) | ✓ Reduces timeout risk | ✗ May timeout |
| Real-time user feedback | ✓ Show tokens as generated | ✗ Wait for full response |
| Batch processing | ✗ Unnecessary overhead | ✓ Simpler |
| Low-latency requirements | ✓ First token faster | ✗ Higher latency |

### When to Use Batch API vs. Real-Time

| Scenario | Use Batch | Use Real-Time |
|----------|-----------|---------------|
| 100+ requests at once | ✓ Cost-effective | ✗ Hits rate limits |
| Interactive user requests | ✗ 48-hour delay | ✓ Immediate response |
| Non-urgent processing | ✓ Cheaper | ✗ Wasteful |
| Deadline < 48 hours | ✗ Too slow | ✓ Required |

### When to Use Sandbox vs. GPU Instance vs. Serverless

| Use Case | Sandbox | GPU Instance | Serverless |
|----------|---------|--------------|-----------|
| Run agent code | ✓ Primary use | ✗ Not designed | ✗ Not designed |
| Train models | ✗ Limited | ✓ Persistent | ✗ Stateless |
| Inference endpoint | ✗ Not ideal | ✓ Manual scaling | ✓ Auto-scaling |
| Development/testing | ✓ Cheap | ✓ Interactive | ✗ Production-only |

## Workflow

### 1. Make Your First LLM Request

1. **Create API key**: Go to https://novita.ai/settings/key-management, create a key, copy it immediately.
2. **Store securely**: Set `export NOVITA_API_KEY="sk_..."` in your shell or CI/CD secrets.
3. **Check credit**: Verify https://novita.ai/billing has available credit for your model.
4. **Send request**: Use curl, Python (OpenAI SDK), or JavaScript with base URL `https://api.novita.ai/openai`.
5. **Verify response**: Check HTTP 200 and non-empty `choices[0].message.content`.

### 2. Integrate with Your Application

1. **Choose SDK**: Use OpenAI Python/JavaScript SDK (set `base_url` and `api_key`).
2. **Set streaming**: Add `stream=True` for long outputs or real-time feedback.
3. **Handle errors**: Catch 401 (bad key), 403 (no model access), 429 (rate limit), 503 (overload).
4. **Retry logic**: Implement exponential backoff for 503/504.
5. **Monitor usage**: Check billing dashboard for token/request counts.

### 3. Run Code in a Sandbox

1. **Install CLI**: `npm install -g @novita/cli` or use SDK.
2. **Authenticate**: `novita auth login` or set `NOVITA_API_KEY`.
3. **Create sandbox**: `novita sandbox create` or use SDK to start from a template.
4. **Run commands**: Execute code, install dependencies, manage files.
5. **Preserve state**: Use snapshots to save configured environments or volumes for persistent storage.

### 4. Deploy a Serverless Endpoint

1. **Go to console**: https://novita.ai/serverless (or use API).
2. **Create endpoint**: Select GPU type (RTX 4090 24GB, H100 80GB), define container/model.
3. **Get endpoint URL**: Use for inference requests.
4. **Scale automatically**: Platform handles load; pay per inference.
5. **Monitor**: Check worker logs and queue status in console.

## Common Gotchas

- **API key in source code**: Never hardcode keys; use environment variables or secrets managers. Keys shown only once at creation.
- **Expired keys**: Keys can expire (set at creation, cannot be changed). Expired keys are rejected; create a new one.
- **Model access denied (403)**: Key's model access policy restricts the requested model. Ask team admin to adjust policy or use a different model.
- **Identity verification required (403)**: Some models require account verification. Complete verification in console before using the model.
- **Rate limit (429)**: Account tier determines RPM/TPM. Upgrade account (higher top-ups) or request limit increase.
- **503/504 timeouts**: High load or long generation. Switch to streaming mode, increase client timeout, or retry during off-peak.
- **Sandbox timeout**: Sandboxes have max lifetime (default 1 hour). Use `--long-running` flag or set `timeout` parameter to extend.
- **Sandbox idle timeout**: Sandbox auto-kills if no client connected for idle duration. Configure idle timeout or keep connection alive.
- **Batch API 48-hour window**: Batch completion window is fixed; cannot be modified. Plan accordingly.
- **Async endpoint 4 MiB limit**: Async serverless endpoint max job size is 4 MiB. Use object storage for larger outputs.
- **Sandbox region mismatch**: v2 (us-phx-1) is default; v1 (us-virginia-1) requires `NOVITA_DOMAIN=sandbox.novita.ai`.
- **Missing NOVITA_API_KEY**: Ensure environment variable is set in the shell/session running your code, not just in your profile.

## Verification Checklist

Before submitting work:

- [ ] API key is valid (starts with `sk_`, created in console, not expired).
- [ ] API key is stored as environment variable, not hardcoded.
- [ ] Account has available credit (check https://novita.ai/billing).
- [ ] Model is within API key's access policy (check model access settings).
- [ ] Request uses correct endpoint (`https://api.novita.ai/openai/v1/...`).
- [ ] Request includes `Authorization: Bearer $NOVITA_API_KEY` header.
- [ ] Request body matches API spec (model, messages, max_tokens, etc.).
- [ ] Response is HTTP 200 with non-empty `choices[0].message.content`.
- [ ] Streaming is enabled for long outputs (>1000 tokens).
- [ ] Batch requests use correct file format (JSONL, one request per line).
- [ ] Sandbox is created from correct template and region (v2 default).
- [ ] Sandbox timeout is set appropriately for workload duration.
- [ ] Error handling covers 401, 403, 429, 503, 504.
- [ ] Rate limit logic respects RPM/TPM for account tier.
- [ ] Secrets/credentials are stored in Sandbox Secrets, not environment variables.

## Resources

- **Comprehensive navigation**: https://docs.novita.ai/llms.txt — page-by-page listing of all documentation.
- **LLM API guide**: https://docs.novita.ai/guides/llm-api — chat/completion endpoints, streaming, parameters.
- **Sandbox overview**: https://docs.novita.ai/guides/sandbox-overview — core concepts, lifecycle, regions.
- **API reference**: https://docs.novita.ai/api-reference/api-reference-overview — all endpoints, authentication, error codes.

---

> For additional documentation and navigation, see: https://docs.novita.ai/llms.txt