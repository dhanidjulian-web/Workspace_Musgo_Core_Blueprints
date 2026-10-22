OpenCode

Endpoints
Zen
Curated list of models provided by OpenCode.

OpenCode Zen is a list of tested and verified models provided by the OpenCode team.

Zen works like any other provider in OpenCode. You login to OpenCode Zen and get your API key. It’s completely optional and you don’t need to use it to use OpenCode.

Background
There are a large number of models out there but only a few of these models work well as coding agents. Additionally, most providers are configured very differently; so you get very different performance and quality.

Tip

We tested a select group of models and providers that work well with OpenCode.

So if you are using a model through something like OpenRouter, you can never be sure if you are getting the best version of the model you want.

To fix this, we did a couple of things:

We tested a select group of models and talked to their teams about how to best run them.
We then worked with a few providers to make sure these were being served correctly.
Finally, we benchmarked the combination of the model/provider and came up with a list that we feel good recommending.
OpenCode Zen is an AI gateway that gives you access to these models.

How it works
OpenCode Zen works like any other provider in OpenCode.

You sign in to OpenCode Zen, add your billing details, and copy your API key.
You run the /connect command in the TUI, select OpenCode Zen, and paste your API key.
Run /models in the TUI to see the list of models we recommend.
You are charged per request and you can add credits to your account.

```
Endpoints
You can also access our models through the following API endpoints.

Model	Model ID	Endpoint	AI SDK Package
GPT 5.5	gpt-5.5	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.5 Pro	gpt-5.5-pro	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4	gpt-5.4	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Pro	gpt-5.4-pro	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Mini	gpt-5.4-mini	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Nano	gpt-5.4-nano	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.3 Codex	gpt-5.3-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.3 Codex Spark	gpt-5.3-codex-spark	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.2	gpt-5.2	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.2 Codex	gpt-5.2-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1	gpt-5.1	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex	gpt-5.1-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex Max	gpt-5.1-codex-max	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex Mini	gpt-5.1-codex-mini	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5	gpt-5	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5 Codex	gpt-5-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5 Nano	gpt-5-nano	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
Claude Opus 4.8	claude-opus-4-8	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.7	claude-opus-4-7	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.6	claude-opus-4-6	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.5	claude-opus-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.1	claude-opus-4-1	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4.6	claude-sonnet-4-6	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4.5	claude-sonnet-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4	claude-sonnet-4	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Haiku 4.5	claude-haiku-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Haiku 3.5	claude-3-5-haiku	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Gemini 3.5 Flash	gemini-3.5-flash	https://opencode.ai/zen/v1/models/gemini-3.5-flash	@ai-sdk/google
Gemini 3.1 Pro	gemini-3.1-pro	https://opencode.ai/zen/v1/models/gemini-3.1-pro	@ai-sdk/google
Gemini 3 Flash	gemini-3-flash	https://opencode.ai/zen/v1/models/gemini-3-flash	@ai-sdk/google
Qwen3.7 Max	qwen3.7-max	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.7 Plus	qwen3.7-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.6 Plus	qwen3.6-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.5 Plus	qwen3.5-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
DeepSeek V4 Flash	deepseek-v4-flash	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiniMax M2.7	minimax-m2.7	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiniMax M2.5	minimax-m2.5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
GLM 5.1	glm-5.1	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
GLM 5	glm-5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Kimi K2.5	kimi-k2.5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Kimi K2.6	kimi-k2.6	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Grok Build 0.1	grok-build-0.1	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Big Pickle	big-pickle	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiMo-V2.5 Free	mimo-v2.5-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Nemotron 3 Ultra Free	nemotron-3-ultra-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
DeepSeek V4 Flash Free	deepseek-v4-flash-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
```

The model id in your OpenCode config uses the format opencode/<model-id>. For example, for GPT 5.5, you would use opencode/gpt-5.5 in your config.

Models
You can fetch the full list of available models and their metadata from:

https://opencode.ai/zen/v1/models