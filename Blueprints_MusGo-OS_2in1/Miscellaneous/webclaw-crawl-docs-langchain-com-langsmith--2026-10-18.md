# LangSmith Observability - Docs by LangChain

`https://docs.langchain.com/langsmith`

# LangSmith Observability

LangSmith Observability provides full visibility into your LLM application: from individual traces to production-wide performance metrics. Traces are the record of what your agents did in production. Use them to debug failures, monitor quality, and build the datasets you evaluate against. LangSmith works with many frameworks and providers. Browse [available integrations](https://docs.langchain.com/langsmith/integrations) to connect your stack including OpenAI, Anthropic, CrewAI, Vercel AI SDK, Pydantic AI, and more.

## Get started
## Documentation Index



Create an account

Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
You can log in with **Google**, **GitHub**, or **email**.

Create an API key

Go to your [Settings page](https://smith.langchain.com/settings) > **API Keys** > **Create API Key**.
Copy the key and save it securely. Once your account and API key are ready, set up tracing:

## Set up tracing

Add tracing to your app in minutes with environment variables, framework integrations, or the SDK.

## Trace a RAG application

Follow a step-by-step tutorial to instrument a retrieval-augmented generation app from start to finish.

## Investigate and monitor


## View traces

Inspect threads and runs in the Messages, Turns, and Details views.

## Monitor performance

Build dashboards and set alerts to track quality and catch issues early.

## Configure automations

Automate workflows with rules, webhooks, and online evaluations.

## Collect feedback

Annotate outputs and gather user feedback using queues or inline annotation.![](https://mintcdn.com/langchain-5e9cc07a/DcM1RJP509SEqR6s/images/brand/engine-icon-no-bg-dark.svg?fit=max&auto=format&n=DcM1RJP509SEqR6s&q=85&s=17cb861b0ae9666e1eb0876aa6aca68a)

## Find and fix failures with Engine

Automatically detect recurring issues in your traces, diagnose their root cause, and resolve them with LangSmith Engine. For terminology and core concepts, refer to [Observability concepts](https://docs.langchain.com/langsmith/observability-concepts). For trace pricing, retention, and limits, see [Usage and billing](https://docs.langchain.com/langsmith/usage-and-billing). To set up a LangSmith instance, visit the [Platform setup section](https://docs.langchain.com/langsmith/platform-setup) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

---

# Set up LangSmith - Docs by LangChain

`https://docs.langchain.com/langsmith/platform-setup`

# Set up LangSmith
## Documentation Index
## ​Compare Cloud, BYOC, and Self-hosted
## ​Common setups
## ​Related





Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

Set up **LangSmith** for [observability](https://docs.langchain.com/langsmith/observability), [evaluation](https://docs.langchain.com/langsmith/evaluation), and [prompt engineering](https://docs.langchain.com/langsmith/prompt-context-hub#prompts). LangSmith offers Cloud, Bring Your Own Cloud (BYOC), and Self-hosted options. Choose the option that matches where your data has to live and who runs the infrastructure.
If you also want to deploy agents in production, you can use [**LangSmith Deployment**](https://docs.langchain.com/langsmith/deployment) with Cloud, BYOC, or Self-hosted.


## Cloud

Fully managed observability, evaluation, and prompt engineering. Get started

## BYOC

Full control over your data, while LangChain manages the infrastructure. Learn about BYOC

## Self-hosted

Full control with observability, evaluation, and prompt engineering in your infrastructure. Run self-hosted
Self-hosted and BYOC are available on the [Enterprise plan](https://docs.langchain.com/langsmith/pricing-plans). [Get a demo](https://www.langchain.com/contact-sales) to learn more.


## [​](https://docs.langchain.com/langsmith/platform-setup#compare-cloud-byoc-and-self-hosted) Compare Cloud, BYOC, and Self-hosted


| Feature | **Cloud** | **BYOC** | **Self-hosted** |
| --- | --- | --- | --- |
| **Who runs the infrastructure** | LangChain | LangChain runs the control plane, you run your data planes | You |
| **Where sensitive data lives** | LangChain’s cloud | Your VPC | Your VPC |
| **Upgrades and patches** | Automatic | Automatic | Manual |
| **Scaling** | Automatic | Automatic, managed by LangChain | Manual |


Cloud, BYOC, and Self-hosted support [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) for agent workloads. Refer to the [LangSmith Deployment overview](https://docs.langchain.com/langsmith/deployment) to pick a topology (Cloud managed, BYOC, Hybrid, self-hosted with control plane, or standalone).


## [​](https://docs.langchain.com/langsmith/platform-setup#common-setups) Common setups


- **Fastest to start, managed everything.** [LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) paired with [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) on Cloud. LangChain hosts the platform, and, when you use LangSmith Deployment, also hosts your [Agent Servers](https://docs.langchain.com/langsmith/agent-server).
- **Bring Your Own Cloud.** Data stays in your VPC, and LangChain manages the infrastructure. Refer to the [BYOC overview](https://docs.langchain.com/langsmith/byoc).
- **Observability data must stay in your infrastructure.** Self-hosted LangSmith, paired with any LangSmith Deployment topology, including [self-hosted LangSmith Deployment](https://docs.langchain.com/langsmith/deploy-with-control-plane) for agent workloads.
- **Managed observability, agents in your VPC.** LangSmith Cloud paired with [Hybrid](https://docs.langchain.com/langsmith/hybrid) LangSmith Deployment. Traces and evaluations stay on SaaS while agent workloads stay in your infrastructure.
- **Observability only, no agent hosting.** LangSmith Cloud or self-hosted, without LangSmith Deployment. Run your agents wherever you already run apps and send traces to LangSmith.


## Account setup

Create an account, manage API keys, and choose a pricing tier. Set up your account

## Plans and pricing

Compare LangSmith plans and tiers. View pricing

## Observability

Trace and monitor your LLM applications. Learn more


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Integrations - Docs by LangChain

`https://docs.langchain.com/langsmith/integrations`

# Integrations

[LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-integrations) provides integrations for a growing set of popular [LLM providers](https://docs.langchain.com/langsmith/integrations#llm-providers) and [agent frameworks](https://docs.langchain.com/langsmith/integrations#agent-frameworks) as well as [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview), [LangChain](https://docs.langchain.com/oss/python/langchain/overview), and [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview). For setup and usage, refer to the guides listed on this page.


## [​](https://docs.langchain.com/langsmith/integrations#llm-providers) LLM providers


[![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d6fc326f6c429075add5a742c87d12b1)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc593829dc9ff5ad061f991e08bbebc8) Amazon Bedrock](https://docs.langchain.com/langsmith/trace-bedrock) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/anthropic.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=f681e2a9025c2e1104d4260c6b27d638)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/anthropic.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=02fc4a5cd4c124dbec46869777a15f34) Anthropic](https://docs.langchain.com/langsmith/trace-anthropic) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/deepseek.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=5a11e956e2ba24fd746aebd929ee1a5e)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/deepseek.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=0cb62f13b3b37e89c35060913ca67515) DeepSeek](https://docs.langchain.com/langsmith/trace-deepseek) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=486f57c43a26c9661700c37d0f575c05)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=6436cb2ebecd9119e486f81fb2fdd360) Google Gemini](https://docs.langchain.com/langsmith/trace-with-google-gemini) [![](https://mintcdn.com/langchain-5e9cc07a/TiT87b4RAoWyIOkQ/images/providers/light/litellm.svg?fit=max&auto=format&n=TiT87b4RAoWyIOkQ&q=85&s=3c70d2b1a246ead959c54869ecf39a74)![](https://mintcdn.com/langchain-5e9cc07a/bCVgrm_X3ggdZ1m0/images/providers/dark/litellm.svg?fit=max&auto=format&n=bCVgrm_X3ggdZ1m0&q=85&s=bf0caf761551eb218517adc898493c9e) LiteLLM](https://docs.langchain.com/langsmith/trace-litellm) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/mistral.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=2b060bfbf269ab1b7f41f3a835f7a0b6)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/mistral.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=59bde8ab2250b2ba2deaa84b74a66e1b) Mistral](https://docs.langchain.com/langsmith/trace-with-mistral) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e) OpenAI](https://docs.langchain.com/langsmith/trace-openai) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e) OpenAI-compatible APIs](https://docs.langchain.com/langsmith/trace-with-openai-compatible)
**Using LangChain?** LangChain provides a unified interface to 100+ LLM providers, which allows you to switch between models by setting environment variables. [Initialize a model](https://docs.langchain.com/oss/python/langchain/models#initialize-a-model) and LangSmith will automatically trace your application.


## [​](https://docs.langchain.com/langsmith/integrations#agent-frameworks) Agent frameworks


[![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/autogen.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=4000da450d02b72ba1115c3dcdc2fde4)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/autogen.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=74a63bfa8fc60eb3fb25b2c4f4f820b4) AutoGen](https://docs.langchain.com/langsmith/trace-with-autogen) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d3cae2da0f353a45594f57b7f2382aba)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=44d1be6c97663a8cd1d4408083011bd9) Claude Agent SDK](https://docs.langchain.com/langsmith/trace-claude-agent-sdk) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d3cae2da0f353a45594f57b7f2382aba)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=44d1be6c97663a8cd1d4408083011bd9) Claude Managed Agents](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/crewai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=5f262e7fa86dc071770356a652ddee8f)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/crewai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc6b523c974b2c63e0b21c70c29ed4b6) CrewAI](https://docs.langchain.com/langsmith/trace-with-crewai) [![](https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465) Deep Agents](https://docs.langchain.com/langsmith/trace-deep-agents) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/googleadk.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=b89f56d14d3d07aed99317fe34b20828)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/googleadk.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=2b3b327124dd6113be499c6e0c927cda) Google ADK](https://docs.langchain.com/langsmith/trace-with-google-adk) [![](https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465) LangChain](https://docs.langchain.com/langsmith/trace-with-langchain) [![](https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465) LangGraph](https://docs.langchain.com/langsmith/trace-with-langgraph) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/mastra.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=4a14d6600d2b99a511b09271f9a5b57e)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/mastra.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=afe3e7535919bd2332229f31d119a6a4) Mastra](https://docs.langchain.com/langsmith/trace-with-mastra) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9189910834f230f7f94115d88e7ec4bf)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=36998a752a161152e010bc2c9b421567) Microsoft Agent Framework](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e) OpenAI Agents](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/opentelemetry.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=84b763868676d132f14cc4055525c34d)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/opentelemetry.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=3eaddab2003804357fcad1a7a8d09f35) OpenTelemetry](https://docs.langchain.com/langsmith/trace-with-opentelemetry) [![](https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/pydanticai.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=0c399e2c9d65c77eeb5644d3d7f2dca5)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/pydanticai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=808e787a6f78fc14508f9c6336ac9a6a) PydanticAI](https://docs.langchain.com/langsmith/trace-with-pydantic-ai) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9189910834f230f7f94115d88e7ec4bf)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=36998a752a161152e010bc2c9b421567) Semantic Kernel](https://docs.langchain.com/langsmith/trace-with-semantic-kernel) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d6fc326f6c429075add5a742c87d12b1)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc593829dc9ff5ad061f991e08bbebc8) Strands Agents](https://docs.langchain.com/langsmith/trace-with-strands-agents) [![](https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/vercel.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=76a0a441ec1730cb68635a19a2a29032)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/vercel.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=7fa15293664e1da6c5fa1319ae0182ec) Vercel AI SDK](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk)


## [​](https://docs.langchain.com/langsmith/integrations#voice-ai-frameworks) Voice AI frameworks


[![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e) OpenAI Realtime](https://docs.langchain.com/langsmith/trace-openai-realtime) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=486f57c43a26c9661700c37d0f575c05)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=6436cb2ebecd9119e486f81fb2fdd360) Gemini Live](https://docs.langchain.com/langsmith/trace-gemini-live) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/livekit.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=e8c6fd5de3893374c7b2b57c68f97de8)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/livekit.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=b98d4d6fbaf0100df180f3e3ee54ca4e) Livekit](https://docs.langchain.com/langsmith/trace-with-livekit) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/pipecat.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=91517611a27adb6cde1a46a81c76233d)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/pipecat.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9fde2f2d7a0acaadd3977e693efb5f45) Pipecat](https://docs.langchain.com/langsmith/trace-with-pipecat)


## [​](https://docs.langchain.com/langsmith/integrations#developer-tools) Developer tools


[![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d3cae2da0f353a45594f57b7f2382aba)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=44d1be6c97663a8cd1d4408083011bd9) Claude Code](https://docs.langchain.com/langsmith/trace-claude-code) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e) OpenAI Codex](https://docs.langchain.com/langsmith/trace-with-codex) [![](https://mintcdn.com/langchain-5e9cc07a/oO5HjFJbtRKTB5uq/images/providers/light/opencode.svg?fit=max&auto=format&n=oO5HjFJbtRKTB5uq&q=85&s=25a9d6bd2ec68f699ff7d461b2922dad)![](https://mintcdn.com/langchain-5e9cc07a/h08KbTOE2npCZz51/images/providers/dark/opencode.svg?fit=max&auto=format&n=h08KbTOE2npCZz51&q=85&s=10a4c9f2cbe6791ff5db75dd47468483) OpenCode](https://docs.langchain.com/langsmith/trace-with-opencode) [![](https://mintcdn.com/langchain-5e9cc07a/zsHfIJsc-kEYhUz3/images/providers/light/cursor.svg?fit=max&auto=format&n=zsHfIJsc-kEYhUz3&q=85&s=9f47067f77df66b7d003ad613ea8d7a6)![](https://mintcdn.com/langchain-5e9cc07a/V1mOmQp0_HGG6FIt/images/providers/dark/cursor.svg?fit=max&auto=format&n=V1mOmQp0_HGG6FIt&q=85&s=dfc11f7d03fdd9b96beb793e033d9570) Cursor](https://docs.langchain.com/langsmith/trace-with-cursor) [![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/instructor.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d9e2a38d8afcb3f166057e835d4717a7)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/instructor.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=66789d39507bfb7f5643bd8528814fd0) Instructor](https://docs.langchain.com/langsmith/trace-with-instructor) [![](https://mintcdn.com/langchain-5e9cc07a/r98TU0ib_rpHFZca/images/providers/light/n8n.svg?fit=max&auto=format&n=r98TU0ib_rpHFZca&q=85&s=4fa6a6e73885330613947815c52d1499)![](https://mintcdn.com/langchain-5e9cc07a/r98TU0ib_rpHFZca/images/providers/dark/n8n.svg?fit=max&auto=format&n=r98TU0ib_rpHFZca&q=85&s=be61c5d6a46d7e493363fdc98e309374) n8n](https://docs.langchain.com/langsmith/trace-with-n8n) [![](https://mintcdn.com/langchain-5e9cc07a/4TrOZZ3BK2K-YJOg/images/providers/light/pi.svg?fit=max&auto=format&n=4TrOZZ3BK2K-YJOg&q=85&s=a7b450733e32c31c1052067940c4ad48)![](https://mintcdn.com/langchain-5e9cc07a/8wWwqzGtryixR6uX/images/providers/dark/pi.svg?fit=max&auto=format&n=8wWwqzGtryixR6uX&q=85&s=4aa58d2d70e82fa82018e3110c56dbad) Pi](https://docs.langchain.com/langsmith/trace-with-pi) [![](https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/temporal.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=3c34b851e1be36297688e71ece797843)![](https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/temporal.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=a7bffaafd90d667487c6e9f8822fb08d) Temporal](https://docs.langchain.com/langsmith/trace-with-temporal) [![](https://mintcdn.com/langchain-5e9cc07a/VoDejLXW9qn9e7mU/images/providers/light/vscode.svg?fit=max&auto=format&n=VoDejLXW9qn9e7mU&q=85&s=15987426cb92b1921d8d41f902df02ac)![](https://mintcdn.com/langchain-5e9cc07a/dfo4A1rdxUTEZYH_/images/providers/dark/vscode.svg?fit=max&auto=format&n=dfo4A1rdxUTEZYH_&q=85&s=5b71dcc502cbb7b56fd8e4dfda561021) VS Code Copilot](https://docs.langchain.com/langsmith/trace-with-vscode-copilot)
These coding agent integrations follow a shared [metadata contract](https://docs.langchain.com/langsmith/coding-agent-metadata-contract) that standardizes the trace fields they emit.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​LLM providers
## ​Agent frameworks
## ​Voice AI frameworks
## ​Developer tools






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Usage and billing - Docs by LangChain

`https://docs.langchain.com/langsmith/usage-and-billing`

# Usage and billing
## Documentation Index
## ​Data retention
## ​Rate limits
## ​Usage limits
## ​Related content






Understand LangSmith trace data retention tiers, pricing, rate limits, and usage limits.

## [​](https://docs.langchain.com/langsmith/usage-and-billing#data-retention) Data retention


This section covers how data retention works and how it’s priced in LangSmith.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#why-retention-matters) Why retention matters


- **Privacy**: Many data privacy regulations, such as GDPR in Europe or CCPA in California, require organizations to delete personal data once it’s no longer necessary for the purposes for which it was collected. Setting retention periods aids in compliance with such regulations.
- **Cost**: LangSmith charges less for traces that have low data retention. For more information, learn how to [enforce spend limits](https://docs.langchain.com/langsmith/billing#enforce-spend-limits).


Plan your retention tiers before you start sending traces. Changes apply to new traces only—existing traces keep their original tier. See [Change project-level default retention](https://docs.langchain.com/langsmith/billing#change-project-level-default-retention).


### [​](https://docs.langchain.com/langsmith/usage-and-billing#how-it-works) How it works


LangSmith has two tiers of traces based on Data Retention with the following characteristics:


|  | Base | Extended |
| --- | --- | --- |
| **Price** | [See pricing page](https://www.langchain.com/pricing-langsmith) | [See pricing page](https://www.langchain.com/pricing-langsmith) |
| **Retention Period** | 14 days | 180 days |


Starting September 14, 2026, the maximum long-lived trace retention period for SaaS customers is changing to 180 days. Enterprise customers can still customize the extended retention period per workspace up to this new maximum. Changes apply to new traces only—existing traces are unaffected. See [Customize extended retention policy](https://docs.langchain.com/langsmith/data-purging-compliance#customize-extended-retention-policy).
**Data deletion after retention ends**
After the specified retention period, traces are no longer accessible in the tracing project UI or via the API. All user data associated with the trace (e.g. inputs and outputs) is deleted from our internal systems shortly after. Some metadata associated with each trace may be retained indefinitely for analytics and billing purposes.
**Where the tier is set**
A default retention tier belongs to a tracing project. In an [agent-based workspace](https://docs.langchain.com/langsmith/agents), each of an agent’s [environments](https://docs.langchain.com/langsmith/agent-environments) is its own tracing project, so the tier is set per environment: one agent can hold production traces at extended retention and development traces at base. To change the tier for a whole agent, set it on each environment. See [Change project-level default retention](https://docs.langchain.com/langsmith/billing#change-project-level-default-retention).


### [​](https://docs.langchain.com/langsmith/usage-and-billing#data-retention-auto-upgrades) Data retention auto-upgrades


Auto upgrades can have an impact on your bill. Please read this section carefully to fully understand your estimated LangSmith tracing costs.
Most traces use base retention. Some actions, such as online evaluators and automation rules, can extend a trace to a longer retention period at a higher cost. You control which actions extend retention.
When you use certain features with `base` tier traces, their data retention may be automatically upgraded to `extended` tier. This increases both the retention period and the cost of the trace.
Retention behavior by action:


- **Feedback via API or SDK**: Feedback is added to any run on the trace (or any trace in the thread) through an API or SDK call that explicitly passes `extend_trace_retention=true` (`extendTraceRetention: true` in TypeScript). For more information, see [Attach user feedback](https://docs.langchain.com/langsmith/attach-user-feedback). The LangSmith UI sends feedback and notes without extending retention.
- **Online evaluators**: An online evaluator scores the trace and its retention setting is enabled. Both trace-level and thread-level evaluators can opt out of this upgrade.
- **Automation rules**: An [automation rule](https://docs.langchain.com/langsmith/rules#create-a-rule) with retention extension enabled matches any run within a trace. Matching a single run upgrades the entire trace, not just that run. A rule whose [item type](https://docs.langchain.com/langsmith/rules#set-the-item-type-to-runs-or-threads) is **Threads** upgrades every trace in the matched thread, not only the most recent one.
- **Manual annotation queue adds** (no upgrade): Manually adding runs or threads to an [annotation queue](https://docs.langchain.com/langsmith/annotation-queues#assign-runs-and-threads-to-a-single-run-queue) does not upgrade retention by default.


This change applies to new actions only. Traces that were already upgraded by a previous action keep their extended retention.
When you create or edit an online evaluator on a tracing project, you can opt out of upgrading the traces that evaluator scores, keeping them at base retention. This option is available only when the project’s default retention is the base tier. For step-by-step instructions, see [Manage evaluator trace retention](https://docs.langchain.com/langsmith/evaluators#manage-evaluator-trace-retention).
Retention extension is enabled by default for new online evaluators and automation rules. You can opt out when configuring each evaluator or rule.
**Why auto-upgrade traces?**
We have two reasons behind the auto-upgrade model for tracing:


1. We think that traces that match any of these conditions are fundamentally more interesting than other traces, and therefore it is good for users to be able to keep them around longer.
2. We philosophically want to charge customers an order of magnitude lower for traces that may not be interacted with meaningfully. We think auto-upgrades align our pricing model with the value that LangSmith brings, where only traces with meaningful interaction are charged at a higher rate.


If you have questions or concerns about our pricing model, please feel free to contact support via [support.langchain.com](https://support.langchain.com) and let us know your thoughts!
**How does data retention affect downstream features?**
The following features interact with retention differently:


- **Experiments**: Runs are created at extended retention by default.
- **Automation rules and evaluators**: Upgrade matching traces to extended retention when their retention setting is enabled. Thread-level rules and evaluators upgrade every trace in the matched thread.
- **UI feedback, notes, and annotation queues**: Leave a trace’s retention tier unchanged.


Other features behave independently of a trace’s retention tier:


- **Monitoring**: The monitoring tab will continue to work even after a base tier trace’s data retention period ends. It is powered by trace metadata that exists for >30 days, meaning that your monitoring graphs will continue to stay accurate even on `base` tier traces.
- **Datasets**: Datasets have an indefinite data retention period. Restated differently, if you add a trace’s inputs and outputs to a dataset, they will never be deleted. We suggest that if you are using LangSmith for data collection, you take advantage of the datasets feature.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#billing-model) Billing model


**Billable metrics**
On your LangSmith invoice, you will see two metrics that we charge for:


- LangSmith Traces (Base Charge)
- LangSmith Traces (Extended Data Retention Upgrades).


The first metric includes all traces, regardless of tier. The second metric just counts the number of extended retention traces.
**Why measure all traces + upgrades instead of base and extended traces?**
A natural question to ask when considering our pricing is why not just show the number of `base` tier and `extended` tier traces directly on the invoice?
While we understand this would be more straightforward, it doesn’t fit trace upgrades properly. Consider a `base` tier trace that was recorded on June 30, and upgraded to `extended` tier on July 3. The `base` tier trace occurred in the June billing period, but the upgrade occurred in the July billing period. Therefore, we need to be able to measure these two events independently to properly bill our customers.
If your trace was recorded as an extended retention trace, then the `base` and `extended` metrics will both be recorded with the same timestamp.


## [​](https://docs.langchain.com/langsmith/usage-and-billing#rate-limits) Rate limits


LangSmith has rate limits which are designed to ensure the stability of the service for all users.
To ensure access and stability, LangSmith will respond with HTTP Status Code 429 indicating that rate or usage limits have been exceeded under the following circumstances:


### [​](https://docs.langchain.com/langsmith/usage-and-billing#temporary-throughput-limit-over-a-1-minute-period-at-our-application-load-balancer) Temporary throughput limit over a 1 minute period at our application load balancer


This 429 is the result of exceeding a fixed number of API calls over a 1 minute window on a per service key or PAT basis. The start of the window will vary slightly—it is not guaranteed to start at the start of a clock minute—and may change depending on application deployment events.
After the max events are received we will respond with a 429 until 60 seconds from the start of the evaluation window has been reached and then the process repeats.
This 429 is thrown by our application load balancer and is a mechanism in place for all LangSmith users independent of plan tier to ensure continuity of service for all users.


| Method | Endpoints | Limit | Window |
| --- | --- | --- | --- |
| `DELETE` | `/sessions*` | 30 | 1 minute |
| `POST` OR `PATCH` | `/runs*` | 5000 | 1 minute |
| `GET` | `/runs/:id` | 30 | 1 minute |
| `POST` | `/feedbacks*` | 5000 | 1 minute |
| `*` | `*` | 2000 | 1 minute |


The LangSmith SDK takes steps to minimize the likelihood of reaching these limits on run-related endpoints by batching up to 100 runs from a single session ID into a single API call.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#plan-level-hourly-trace-event-limit) Plan-level hourly trace event limit


This 429 is the result of reaching your maximum hourly events ingested and is evaluated in a fixed window starting at the beginning of each clock hour in UTC and resets at the top of each new hour.
An event in this context is the creation or update of a run. If a run is created and then subsequently updated in the same hourly window, that counts as 2 events against this limit.
This is thrown by our application and varies by plan tier, with organizations on our Startup/Plus and Enterprise plan tiers having higher hourly limits than our Free and Developer Plan Tiers which are designed for personal use.


| Plan | Limit | Window |
| --- | --- | --- |
| Developer (no payment on file) | 50,000 events | 1 hour |
| Developer (with payment on file) | 250,000 events | 1 hour |
| Startup/Plus | 500,000 events | 1 hour |
| Enterprise | Custom | Custom |


### [​](https://docs.langchain.com/langsmith/usage-and-billing#plan-level-hourly-trace-data-ingest-limit) Plan-level hourly trace data ingest limit


This 429 is the result of reaching the maximum amount of data ingested across your trace inputs, outputs, and metadata and is evaluated in a fixed window starting at the beginning of each clock hour in UTC and resets at the top of each new hour.
Typically, inputs, outputs, and metadata are sent on both run creation and update events. If a run is created at 2.0MB and updated to 3.0MB in the same hourly window, that counts as 5.0MB of storage against this limit.
This is thrown by our application and varies by plan tier, with organizations on our Startup/Plus and Enterprise plan tiers having higher hourly limits than our Free and Developer Plan Tiers which are designed for personal use.


| Plan | Limit | Window |
| --- | --- | --- |
| Developer (no payment on file) | 500MB | 1 hour |
| Developer (with payment on file) | 2.5GB | 1 hour |
| Startup/Plus | 5.0GB | 1 hour |
| Enterprise | Custom | Custom |


### [​](https://docs.langchain.com/langsmith/usage-and-billing#plan-level-monthly-unique-traces-limit) Plan-level monthly unique traces limit


This 429 is the result of reaching your maximum monthly traces ingested and is evaluated in a fixed window starting at the beginning of each calendar month in UTC and resets at the beginning of each new month.
This is thrown by our application and applies only to the Developer Plan Tier when there is no payment method on file.


| Plan | Limit | Window |
| --- | --- | --- |
| Developer (no payment on file) | 5,000 traces | 1 month |


### [​](https://docs.langchain.com/langsmith/usage-and-billing#self-configured-monthly-usage-limits) Self-configured monthly usage limits


This 429 is the result of reaching your usage limit as configured by your organization admin and is evaluated in a fixed window starting at the beginning of each calendar month in UTC and resets at the beginning of each new month.
This is thrown by our application and varies by organization based on their configured settings.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#maximum-runs-per-trace) Maximum runs per trace


Each trace is limited to a maximum of 25,000 runs. Once the trace reaches this limit, LangSmith will reject any additional runs that you send for that trace.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#run-query-endpoint) Run query endpoint


LangSmith exposes two versions of the run query endpoint with different rate limit profiles.
**v2 (recommended):** `POST /v2/runs/query` ([`list_runs`](https://reference.langchain.com/python/langsmith/client/Client/list_runs) in Python, [`listRuns`](https://reference.langchain.com/javascript/langsmith/client/Client/listRuns) in JavaScript) is backed by SmithDB and has a flat per-API-key limit with no time-window tiers:


| **Limit** | **Window** |
| --- | --- |
| 300 requests | 10 seconds |


API key requests that set `sem_filter` (semantic search) are also limited to 10 requests per minute per workspace.
**v1:** `POST /runs/query` has per-tenant rate limits that vary based on query parameters:


| **Query type** | **Limit** | **Window** |
| --- | --- | --- |
| Short time window (≤ 7 days) | 10 requests | 10 seconds |
| Large time window (> 7 days) | 3 requests | 10 seconds |
| Full-text search, short time window (≤ 7 days) | 3 requests | 10 seconds |
| Full-text search, large time window (> 7 days) | 1 request | 10 seconds |
| Select `child_run_ids`, short time window (≤ 7 days) | 3 requests | 10 seconds |
| Select `child_run_ids`, large time window (> 7 days) | 1 request | 10 seconds |


The time window is determined by `end_time - start_time`. If `end_time` is not provided, LangSmith will use the current time. Queries without a `start_time` are treated as large time window queries.
To avoid hitting v1 rate limits and reduce query time:


- **Set `start_time`**: omitting it triggers the large time window tier (3 requests per 10 seconds instead of 10). Use a window of 7 days or less when possible.
- **Use `select`**: by default all fields are returned. Specifying only the fields you need (e.g., `select=["inputs", "outputs"]`) substantially reduces response size and query time.
- **Set `limit`**: cap the number of results if you don’t need to paginate through everything.
- **Avoid full-text search**: `filter='search("...")'` has the strictest rate limits; use structured filters (e.g., `eq()`, `has()`) when possible.
- **Avoid selecting `child_run_ids`**: this also triggers a stricter rate limit tier.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#run-stats-endpoint) Run stats endpoint


The [`POST /runs/stats`](https://docs.langchain.com/langsmith/smith-api/run/stats-runs) endpoint has per-tenant rate limits that vary based on the query time window:


| **Query type** | **Limit** | **Window** |
| --- | --- | --- |
| Short time window (≤ 14 days) | 10 requests | 10 seconds |
| Large time window (> 14 days and < 90 days) | 3 requests | 10 seconds |
| Extra-large time window (≥ 90 days) or no `start_time` | 1 request | 10 seconds |


The time window is determined by `end_time - start_time`. If `end_time` is not provided, LangSmith uses the current time. Queries without a `start_time` are subject to the strictest limit.
In the GCP-hosted US region, API key requests to this endpoint are also limited to 1 request per 10 seconds per API key.
To avoid hitting rate limits:


- **Set `start_time`**: use a window of 14 days or less when possible.
- **Avoid open-ended queries**: always provide a `start_time` to stay in the less-restrictive tier.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#workspace-invite-batch-endpoint) Workspace invite batch endpoint


Workspace invite batch requests are rate limited per workspace to reduce bulk invitation abuse.
The `POST /workspaces/current/members/batch` endpoint allows 2 requests per second per workspace. This limit applies to LangSmith Cloud only.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#handling-429s-responses-in-your-application) Handling 429s responses in your application


Since some 429 responses are temporary and may succeed on a successive call, if you are directly calling the LangSmith API in your application we recommend implementing retry logic with exponential backoff and jitter.
For convenience, LangChain applications built with the LangSmith SDK has this capability built-in.
It is important to note that if you are saturating the endpoints for extended periods of time, retries may not be effective as your application will eventually run large enough backlogs to exhaust all retries. If that is the case, we would like to discuss your needs more specifically. Please contact support via [LangSmith Support](https://support.langchain.com) with details about your applications throughput needs and sample code and we can work with you to better understand whether the best approach is fixing a bug, changes to your application code, or a different LangSmith plan.


## [​](https://docs.langchain.com/langsmith/usage-and-billing#usage-limits) Usage limits


LangSmith lets you configure usage limits on tracing. Note that these are *usage* limits, not *spend* limits, which mean they let you limit the quantity of occurrences of some event rather than the total amount you will spend.
LangSmith lets you set two different monthly limits, mirroring our Billable Metrics discussed in the aforementioned data retention guide:


- All traces limit
- Extended data retention traces limit


These let you limit the number of total traces, and extended data retention traces respectively.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#properties-of-usage-limiting) Properties of usage limiting


Usage limiting is approximate, meaning that we do not guarantee the exactness of the limit. In rare cases, there may be a small period of time where additional traces are processed above the limit threshold before usage limiting begins to apply.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#side-effects-of-extended-data-retention-traces-limit) Side effects of extended data retention traces limit


The extended data retention traces limit has side effects. If the limit is already reached, LangSmith blocks actions that would create another extended-retention trace. For example, you can no longer:


1. run automation rules that extend trace retention
2. run evaluators that extend trace retention


Actions that do not change trace retention are not counted against the extended-retention trace limit. You can still submit feedback in the LangSmith UI, add runs or threads to annotation queues, and run automation rules or evaluators with retention extension disabled when the limit is reached.


### [​](https://docs.langchain.com/langsmith/usage-and-billing#updating-usage-limits) Updating usage limits


Usage limits can be updated from the `Settings` page under `Usage and Billing`. Limit values are cached, so it may take a minute or two before the new limits apply.


## [​](https://docs.langchain.com/langsmith/usage-and-billing#related-content) Related content


- Tutorial on how to [enforce spend limits](https://docs.langchain.com/langsmith/billing#enforce-spend-limits)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/usage-and-billing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Use docs programmatically - Docs by LangChain

`https://docs.langchain.com/use-these-docs`

# Use docs programmatically
## Documentation Index
## ​Quick access options
## ​Use our MCP servers
## ​Learn more





Connect LangChain documentation to your AI tools and workflows

We want to make our documentation as accessible as possible. We’ve included several ways for you to use these docs programmatically through AI assistants, code editors, and direct integrations, such as Model Context Protocol (MCP).


## [​](https://docs.langchain.com/use-these-docs#quick-access-options) Quick access options


On any page in our documentation, you’ll find a contextual menu dropdown in the top right corner:
![Copy page light mode](https://mintcdn.com/langchain-5e9cc07a/jKM-tvbl7XiR347g/images/copy-page-light.png?fit=max&auto=format&n=jKM-tvbl7XiR347g&q=85&s=81d6cf67dc039d588707bd97ee3f3a72)
![Copy page dark mode](https://mintcdn.com/langchain-5e9cc07a/jKM-tvbl7XiR347g/images/copy-page-dark.png?fit=max&auto=format&n=jKM-tvbl7XiR347g&q=85&s=9257e0b3480b22cdaf56b5c70305124d)
This includes our `llms.txt`, MCP server connection, and other quick access options such as ChatGPT and Claude.


## [​](https://docs.langchain.com/use-these-docs#use-our-mcp-servers) Use our MCP servers


Connect LangChain docs MCP servers

Copied Copy prompt
Our documentation exposes two complementary **Model Context Protocol (MCP) servers** that let AI applications query LangChain content in real-time. For the best results, we recommend connecting both:


| Server | URL | What it covers |
| --- | --- | --- |
| `docs-langchain` | `https://docs.langchain.com/mcp` | Conceptual guides, how-tos, tutorials, and product docs for LangChain, LangGraph, and LangSmith |
| `reference-langchain` | `https://reference.langchain.com/mcp` | API reference: classes, methods, parameters, and signatures for all LangChain packages |


Adding both gives your coding agent access to the full picture: the **why and how** from the guides, plus the **exact API details** from the reference docs.


### [​](https://docs.langchain.com/use-these-docs#connect-with-claude-code) Connect with Claude Code


If you’re using Claude Code, run these commands in your terminal to add both servers to your current project:


```
claude mcp add --transport http docs-langchain https://docs.langchain.com/mcp
claude mcp add --transport http reference-langchain https://reference.langchain.com/mcp
```


**Project (local) scoped** The commands above add the MCP servers only to your current project/working directory. To add them globally and access them in all projects, add the user scope by including `--scope user`:

```
claude mcp add --transport http docs-langchain --scope user https://docs.langchain.com/mcp
claude mcp add --transport http reference-langchain --scope user https://reference.langchain.com/mcp
```


### [​](https://docs.langchain.com/use-these-docs#connect-with-claude-desktop) Connect with Claude Desktop


1. Open Claude Desktop
2. Go to Settings > Connectors
3. Add both MCP server URLs:
  - `https://docs.langchain.com/mcp`
  - `https://reference.langchain.com/mcp`


### [​](https://docs.langchain.com/use-these-docs#connect-with-codex-cli) Connect with Codex CLI


If you’re using OpenAI Codex CLI, run these commands in your terminal to add both servers globally:


```
codex mcp add langchain-docs --url https://docs.langchain.com/mcp
codex mcp add langchain-reference --url https://reference.langchain.com/mcp
```


### [​](https://docs.langchain.com/use-these-docs#connect-with-cursor) Connect with Cursor


Add the following to your MCP settings configuration file:


```
{
  "mcpServers": {
    "docs-langchain": {
      "url": "https://docs.langchain.com/mcp"
    },
    "reference-langchain": {
      "url": "https://reference.langchain.com/mcp"
    }
  }
}
```


### [​](https://docs.langchain.com/use-these-docs#connect-with-deep-agents-code) Connect with Deep Agents Code


Add both servers to your user-level `~/.deepagents/.mcp.json` file to make them available in every Deep Agents Code project, or add them to a project-level `.mcp.json` file for only that project:


```
{
  "mcpServers": {
    "docs-langchain": {
      "type": "http",
      "url": "https://docs.langchain.com/mcp"
    },
    "reference-langchain": {
      "type": "http",
      "url": "https://reference.langchain.com/mcp"
    }
  }
}
```


Launch or restart `dcode` to load the servers. In an interactive session, run `/mcp` to inspect server status and loaded tools. For discovery locations and precedence rules, see [MCP tools](https://docs.langchain.com/oss/deepagents/code/mcp-tools).


### [​](https://docs.langchain.com/use-these-docs#connect-with-vs-code) Connect with VS Code


Add the following to your MCP settings configuration file:


```
{
  "servers": {
    "docs-langchain": {
      "url": "https://docs.langchain.com/mcp"
    },
    "reference-langchain": {
      "url": "https://reference.langchain.com/mcp"
    }
  }
}
```


### [​](https://docs.langchain.com/use-these-docs#connect-with-antigravity) Connect with Antigravity


Add the following to your MCP settings configuration file:


```
{
  "mcpServers": {
    "docs-langchain": {
      "serverUrl": "https://docs.langchain.com/mcp"
    },
    "reference-langchain": {
      "serverUrl": "https://reference.langchain.com/mcp"
    }
  }
}
```


## [​](https://docs.langchain.com/use-these-docs#learn-more) Learn more


For more information about using Mintlify’s MCP servers, see the [official Mintlify documentation](https://www.mintlify.com/docs/ai/model-context-protocol).
Have questions or feedback? Let us know in our [community forum](https://forum.langchain.com/).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/use-these-docs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Observability concepts - Docs by LangChain

`https://docs.langchain.com/langsmith/observability-concepts`

# Observability concepts
## Documentation Index
## ​How LangSmith structures and visualizes data
## ​Trace enrichment
## ​Sending traces
## ​Data retention






How LangSmith structures observability data as runs, traces, threads, and trajectories, and how to send traces.

LangSmith Observability lets you record, inspect, and analyze every step your AI agent takes. This page explains how that data is structured and visualized in LangSmith as well as how to start sending traces.


## [​](https://docs.langchain.com/langsmith/observability-concepts#how-langsmith-structures-and-visualizes-data) How LangSmith structures and visualizes data


In LangSmith, every unit of work an agent performs, such as a model call, tool invocation, or information retrieval, is recorded as a [*run*](https://docs.langchain.com/langsmith/observability-concepts#runs). The runs for a single operation are collected into a [*trace*](https://docs.langchain.com/langsmith/observability-concepts#traces). You can link together traces from multi-turn sessions as a [*thread*](https://docs.langchain.com/langsmith/observability-concepts#threads).
A [*trajectory*](https://docs.langchain.com/langsmith/observability-concepts#trajectories) is another way to structure and visualize that data. While a thread groups the traces of a session and keeps their nested structure, a trajectory flattens the entire session into an ordered list of messages that shows the path an agent took from start to finish.
![A thread groups a session's traces and keeps their nesting, while a trajectory flattens the same session into an ordered list of messages](https://mintcdn.com/langchain-5e9cc07a/_6XeQZT2NAQ4WqkK/langsmith/images/thread-trajectory-light.png?fit=max&auto=format&n=_6XeQZT2NAQ4WqkK&q=85&s=e770ae021710ef231582cd59aae3a403)
![A thread groups a session's traces and keeps their nesting, while a trajectory flattens the same session into an ordered list of messages](https://mintcdn.com/langchain-5e9cc07a/_6XeQZT2NAQ4WqkK/langsmith/images/thread-trajectory-dark.png?fit=max&auto=format&n=_6XeQZT2NAQ4WqkK&q=85&s=b60e198867da6e9a43877a66b0d90e54)


### [​](https://docs.langchain.com/langsmith/observability-concepts#runs) Runs


A *run* represents a single unit of work executed by an agent, such as calling an LLM, formatting a prompt, or retrieving documents. If you are familiar with [OpenTelemetry](https://opentelemetry.io/), you can think of a run as a span.


### [​](https://docs.langchain.com/langsmith/observability-concepts#traces) Traces


A *trace* is a collection of runs for a single operation. For example, if a user request triggers an agent that calls a model, runs a tool, and then calls the model again, all of those runs belong to the same trace. Runs are bound to a trace by a unique trace ID.
Each trace is limited to a maximum of 25,000 runs. Once the trace reaches this limit, LangSmith will reject any additional runs that you send for that trace.


### [​](https://docs.langchain.com/langsmith/observability-concepts#threads) Threads


A *thread* is a sequence of traces representing a single multi-turn session. A turn is one exchange in that session: a user’s message and everything the agent does in response. Each turn is recorded as its own trace. To group traces into a thread, pass a `thread_id` metadata key with a unique value.
[Learn how to configure threads](https://docs.langchain.com/langsmith/threads).


### [​](https://docs.langchain.com/langsmith/observability-concepts#trajectories) Trajectories


A *trajectory* is a flat, ordered list of messages that shows the path an agent took from start to finish.
In LangSmith, a trajectory is a projection over the traces in a thread. It contains the human, AI, and tool messages exchanged during the session, each appearing once, in the order it first appeared, with the nesting of runs removed.
[Learn how trajectories render in the Trajectory view](https://docs.langchain.com/langsmith/trajectory-view-integrations).


### [​](https://docs.langchain.com/langsmith/observability-concepts#compare-traces-threads-and-trajectories) Compare traces, threads, and trajectories


|  | Trace | Thread | Trajectory |
| --- | --- | --- | --- |
| Shape | Tree of runs | Sequence of traces | Flat, ordered list of messages |
| Contains | Every run, with full inputs and outputs | Every run in every linked trace | Every message in every linked trace, deduplicated |
| Reach for it when | You are debugging why one operation failed or ran slow | You are inspecting how the agent behaved across turns, with timing and nesting intact | You are reading what was exchanged in the session, without the execution detail |


Use **[Chat](https://docs.langchain.com/langsmith/chat)** to analyze traces, runs, and threads. Chat helps you understand agent performance, debug issues, and gain insights from conversation threads without manually digging through data.


### [​](https://docs.langchain.com/langsmith/observability-concepts#trace-containers) Trace containers


How LangSmith groups traces depends on which information architecture your workspace uses.


#### [​](https://docs.langchain.com/langsmith/observability-concepts#agents-and-environments) Agents and environments


**Agent-based workspaces ([beta](https://docs.langchain.com/langsmith/release-stages)).** This section applies if your workspace organizes traces by [agent and environment](https://docs.langchain.com/langsmith/agents). To check, look at the control at the top left: it names your workspace. If it shows the LangSmith logo instead, and the sidebar has an **Application** section with an application picker, your workspace is project-based. Skip this section and read [Tracing projects](https://docs.langchain.com/langsmith/observability-concepts#tracing-projects).
An *agent* collects the traces of a single application, and it is the unit LangSmith organizes everything else around. An agent’s traces divide across *environments* drawn from a fixed set of four: Production, Staging, Development, and Local. Traces land in one environment of one agent, so a query about production behavior never has to exclude test traffic by hand.
[Log traces to an agent](https://docs.langchain.com/langsmith/log-traces-to-agent).


#### [​](https://docs.langchain.com/langsmith/observability-concepts#tracing-projects) Tracing projects


**Project-based workspaces.** This section applies if your workspace organizes traces by [tracing project](https://docs.langchain.com/langsmith/observability-concepts#tracing-projects). To check, look at the control at the top left. In a project-based workspace, it shows the LangSmith logo, and the sidebar has an **Application** section with an application picker. If the control shows your workspace name instead, your workspace is agent-based, which is in [beta](https://docs.langchain.com/langsmith/release-stages). Skip this section and read [Agents](https://docs.langchain.com/langsmith/agents).
A *project* is a container for all the traces related to a single application or service.
[Log traces to a project](https://docs.langchain.com/langsmith/log-traces-to-project).


## [​](https://docs.langchain.com/langsmith/observability-concepts#trace-enrichment) Trace enrichment


### [​](https://docs.langchain.com/langsmith/observability-concepts#feedback) Feedback


*Feedback* allows you to score an individual run based on certain criteria. Each feedback entry consists of a tag and a score, and is bound to a run by a unique run ID. Feedback can be continuous or discrete (categorical), and tags can be reused across runs within an organization.
For more on how feedback is stored, refer to the [Feedback data format guide](https://docs.langchain.com/langsmith/feedback-data-format).


### [​](https://docs.langchain.com/langsmith/observability-concepts#tags) Tags


*Tags* are strings you can attach to runs to categorize, filter, and group them in the LangSmith UI.
[Learn how to attach tags to your traces](https://docs.langchain.com/langsmith/add-metadata-tags).


### [​](https://docs.langchain.com/langsmith/observability-concepts#metadata) Metadata


*Metadata* is a collection of key-value pairs you can attach to runs. For example, application version, environment, or any other contextual information. Similarly to tags, you can use metadata to filter and group runs.
[Learn how to add metadata to your traces](https://docs.langchain.com/langsmith/add-metadata-tags).


## [​](https://docs.langchain.com/langsmith/observability-concepts#sending-traces) Sending traces


There are two ways to send trace data to LangSmith.


### [​](https://docs.langchain.com/langsmith/observability-concepts#integrations) Integrations


LangSmith *integrations* provide automatic tracing for popular LLM providers and agent frameworks (the equivalent of auto-instrumentation in general observability). When you use a supported framework such as LangChain, LangGraph, OpenAI, Anthropic, or CrewAI, the integration captures inputs, outputs, and metadata without requiring manual code changes.
[Browse all integrations](https://docs.langchain.com/langsmith/integrations).


### [​](https://docs.langchain.com/langsmith/observability-concepts#manual-instrumentation) Manual instrumentation


*Manual instrumentation* lets you add tracing to any code, regardless of the framework. Use it when you’re not using a supported integration or when you need granular control over what gets traced. LangSmith provides three mechanisms:


- `@traceable` / `traceable`: a decorator to trace any function
- `trace` context manager (Python): wrap specific code blocks
- `RunTree` API: low-level, explicit trace construction


[Learn how to add manual instrumentation](https://docs.langchain.com/langsmith/annotate-code).


## [​](https://docs.langchain.com/langsmith/observability-concepts#data-retention) Data retention


LangSmith (SaaS) retains trace data for 180 days from ingestion. After that, traces are permanently deleted, with limited metadata retained for usage statistics. For details on retention tiers and pricing, refer to [Usage and billing: Data retention](https://docs.langchain.com/langsmith/usage-and-billing#data-retention).
To keep data beyond the retention period, add it to a [dataset](https://docs.langchain.com/langsmith/manage-datasets). Datasets persist indefinitely, even after the source trace is deleted.
To delete traces before their expiration date, see [Manage a trace](https://docs.langchain.com/langsmith/manage-trace#delete-a-trace).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability-concepts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# LangChain overview - Docs by LangChain

`https://docs.langchain.com/oss/python/langchain/overview`

# LangChain overview
## Documentation Index
## ​ Create an agent
## ​ Core benefits




LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

**Agent = Model + Harness.** LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports [OpenAI, Anthropic, Google, and more](https://docs.langchain.com/oss/python/integrations/providers/overview).
**LangChain vs. LangGraph vs. Deep Agents** Start with [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) for a “batteries-included” agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain [agents](https://docs.langchain.com/oss/python/langchain/agents) which you can also use directly. Use [LangChain](https://docs.langchain.com/oss/python/langchain/agents) (`create_agent`) for a highly customizable harness, easily tailored to your use case and data. Use [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows. Use [LangSmith](https://docs.langchain.com/langsmith/observability) to trace, debug, and evaluate agents built with any of these frameworks. Follow the [tracing quickstart](https://docs.langchain.com/langsmith/trace-with-langchain) to get set up. We recommend you also set up [LangSmith Engine](https://docs.langchain.com/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.


## [​](https://docs.langchain.com/oss/python/langchain/overview#create-an-agent) Create an agent


This example demonstrates how to create a simple LangChain agent with a custom tool:
OpenAI Google Gemini Claude (Anthropic) OpenRouter Fireworks Baseten Ollama Azure AWS Bedrock HuggingFace

```
# pip install -qU langchain "langchain[openai]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain "langchain[google-genai]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain "langchain[anthropic]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain langchain-openrouter
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openrouter:anthropic/claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain langchain-fireworks
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain langchain-baseten
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain langchain-ollama
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="ollama:devstral-2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain "langchain[openai]"
import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = init_chat_model(
    "azure_openai:gpt-5.5",
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain langchain-aws
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# US cross-region inference profile; use global.anthropic.claude-sonnet-4-6 for worldwide routing.
agent = create_agent(
    model="bedrock_converse:us.anthropic.claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


```
# pip install -qU langchain "langchain[huggingface]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="huggingface:microsoft/Phi-3-mini-4k-instruct",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```


See the [Installation instructions](https://docs.langchain.com/oss/python/langchain/install) and [Quickstart guide](https://docs.langchain.com/oss/python/langchain/quickstart) to get started building your own agents and applications with LangChain.
Use [LangSmith](https://docs.langchain.com/langsmith/observability) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.


## [​](https://docs.langchain.com/oss/python/langchain/overview#core-benefits) Core benefits


## Standard model interface

Use one interface for chat models, embeddings, and more across providers. Switch models with minimal code changes and keep your application portable as requirements evolve. Learn more

## Highly configurable harness

Start with `create_agent` as a minimal harness and add capabilities incrementally through middleware. Compose only what your use case needs, from guardrails and retries to routing and custom tool policies. Learn more![](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81)

## Built on top of LangGraph

LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more. Learn more![](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc)

## Debug with LangSmith

Inspect traces, tool calls, state transitions, and latency in one place. Find failure modes, evaluate quality, and improve agent behavior with execution data. Learn more


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# LangGraph overview - Docs by LangChain

`https://docs.langchain.com/oss/python/langgraph/overview`

# LangGraph overview
## Documentation Index
## ​ Install
## ​Core benefits
## ​LangGraph ecosystem
## ​Acknowledgements






Gain control with LangGraph to design agents that reliably handle complex tasks

Trusted by companies shaping the future of agents—including Klarna, Uber, J.P. Morgan, and more—LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph gives you fine-grained control to mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph, so you can build bespoke agents that behave exactly the way your application requires.
LangGraph is very low-level, and focused entirely on agent **orchestration**. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with [models](https://docs.langchain.com/oss/python/langchain/models) and [tools](https://docs.langchain.com/oss/python/langchain/tools).
We will commonly use [LangChain](https://docs.langchain.com/oss/python/langchain/overview) components throughout the documentation to integrate models and tools, but you don’t need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain’s [agents](https://docs.langchain.com/oss/python/langchain/agents) that provide prebuilt architectures for common LLM and tool-calling loops.
LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more.
One of LangGraph’s core strengths is the ability to mix deterministic steps with LLM-driven agentic steps in a single graph. This lets you build bespoke workflows where parts of the logic are fully predictable and auditable while other parts are flexible and model-driven, giving you fine-grained control over exactly where and how AI is applied.


Show how LangChain products fit together


- [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) is an [agent harness](https://docs.langchain.com/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk): planning, subagents, filesystem tools, and context management on top of LangGraph.
- [LangChain](https://docs.langchain.com/oss/python/langchain/overview) is the agent framework: abstractions and integrations for models, tools, and agent loops.
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
- [LangSmith](https://docs.langchain.com/langsmith/observability) is the platform for tracing, evaluation, prompts, and deployment across frameworks.
- [LangSmith Engine](https://docs.langchain.com/langsmith/engine) detects issues in your LangGraph agent traces and proposes fixes. You can open a pull request with the proposed fix directly from the Engine tab.
- [LangSmith Fleet](https://docs.langchain.com/langsmith/fleet/index) is the no-code agent builder for templates, integrations, and routine automation.

Read [Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/python/concepts/products) for a comparison of the open source stack.


## [​](https://docs.langchain.com/oss/python/langgraph/overview#install) Install


pip uv

```
pip install -U langgraph
```


```
uv add langgraph
```


Then, create a simple hello world example:


```
from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
```


Use [LangSmith](https://docs.langchain.com/langsmith/observability) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started. Follow the [tracing quickstart](https://docs.langchain.com/langsmith/trace-with-langchain) to get set up.  We recommend you also set up [LangSmith Engine](https://docs.langchain.com/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.


## [​](https://docs.langchain.com/oss/python/langgraph/overview#core-benefits) Core benefits


LangGraph provides low-level supporting infrastructure for *any* long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:


- **Mix deterministic and agentic steps**: Combine hand-coded, deterministic logic with LLM-driven decision-making in a single graph. Use deterministic steps where you need reliability and predictability, and agentic steps where you need flexibility—giving you precise control over every part of your agent’s behavior.
- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence): Build agents that persist through failures and can run for extended periods, resuming from where they left off.
- [Human-in-the-loop](https://docs.langchain.com/oss/python/langgraph/interrupts): Incorporate human oversight by inspecting and modifying agent state at any point.
- [Comprehensive memory](https://docs.langchain.com/oss/python/concepts/memory): Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions.
- [Debugging with LangSmith](https://docs.langchain.com/langsmith/observability): Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
- [Production-ready deployment](https://docs.langchain.com/langsmith/deployment): Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.


## [​](https://docs.langchain.com/oss/python/langgraph/overview#langgraph-ecosystem) LangGraph ecosystem


While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:
![](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc)

## LangSmith Observability

Trace requests, evaluate outputs, and monitor deployments in one place. Prototype locally with LangGraph, then move to production with integrated observability and evaluation to build more reliable agent systems. Learn more![](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deployment-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=024e3712d388bfa55f4f160cc9d6a85b)

## LangSmith Deployment

Deploy and scale agents effortlessly with a purpose-built deployment platform for long running, stateful workflows. Discover, reuse, configure, and share agents across teams — and iterate quickly with visual prototyping in Studio. Learn more![](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4)

## LangChain

Provides integrations and composable components to streamline LLM application development. Contains agent abstractions built on top of LangGraph. Learn more


## [​](https://docs.langchain.com/oss/python/langgraph/overview#acknowledgements) Acknowledgements


LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Anthropic applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-anthropic`

# Trace Anthropic applications
## Documentation Index
## ​Trace from the Claude Platform
## ​Trace from your application




Trace Anthropic applications in LangSmith from the Claude Platform, from the Claude SDKs over OpenTelemetry, or with the LangSmith SDK wrapper.

You can send Anthropic traces to LangSmith from Anthropic’s servers or from your own application:


- **[From the Claude Platform](https://docs.langchain.com/langsmith/trace-anthropic#trace-from-the-claude-platform)**: The Claude Platform sends traces directly from Anthropic’s servers. You configure it in the Claude Console, with no changes to your application code.
- **[From your application](https://docs.langchain.com/langsmith/trace-anthropic#trace-from-your-application)**: Your application sends the traces, in one of two ways:
  - **[Claude SDKs](https://docs.langchain.com/langsmith/trace-anthropic#use-the-claude-sdks)**: The Claude SDKs emit OpenTelemetry (OTel) spans, and an OTel exporter library sends them to LangSmith.
  - **[LangSmith SDK wrapper](https://docs.langchain.com/langsmith/trace-anthropic#use-the-langsmith-sdk-wrapper)**: You wrap the Anthropic client with the LangSmith SDK (Python or TypeScript). You can combine the traces with `@traceable` spans for the rest of your code in a single trace.


Tracing from the Claude Platform and the Claude SDKs is in public beta.


## [​](https://docs.langchain.com/langsmith/trace-anthropic#trace-from-the-claude-platform) Trace from the Claude Platform


The Claude Platform exports OTel traces of your [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) sessions and [Messages API](https://platform.claude.com/docs/en/api/messages) requests. It sends them to a *destination*, an OTel endpoint that you register in the Claude Console. You can add LangSmith as a destination and view these traces without changing your application code. For details on destinations and delivery, see [Use OpenTelemetry with the Claude API](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api) in the Anthropic docs.
Before you begin, you need:


- The admin role, or an equivalent permission, in your Claude Console organization. Without it, you cannot view or manage destinations.
- A LangSmith API key. You can use a [personal access token](https://docs.langchain.com/langsmith/administration-overview#personal-access-tokens-pats), or a [service key](https://docs.langchain.com/langsmith/administration-overview#service-keys) when you want tracing to be independent of your user account. To create a key, see [Create an account and API key](https://docs.langchain.com/langsmith/create-account-api-key).
- For self-hosted LangSmith, an endpoint that the Claude Platform can reach: HTTPS on port 443, at a hostname that resolves to a public IP address.


### [​](https://docs.langchain.com/langsmith/trace-anthropic#step-1-add-langsmith-as-a-destination) Step 1. Add LangSmith as a destination


To add a destination:


1. In the Claude Console, open the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) of your organization and click **Add destination**.
2. In the **Provider** drop-down, select **LangSmith**. The form changes to show the LangSmith fields.
3. Complete the fields:
  - **Name**: (Optional) A label for the destination, such as `LangSmith`.
  - **Region**: The region of your LangSmith deployment: **US**, **EU**, **APAC**, or **US on AWS**. For self-hosted LangSmith, select **Self-hosted** and enter the OTel endpoint URL of your instance in the **LangSmith URL** field, for example `https://<your-langsmith-host>/api/v1/otel`.
  - **API key**: Your LangSmith API key.
  - **Project**: (Optional) The name of the [tracing project](https://docs.langchain.com/langsmith/log-traces-to-project) to send traces to. If you leave it empty, traces go to the `default` project.
  - **LangSmith workspace ID**: (Optional) The ID of the LangSmith workspace to send traces to. If you leave it empty, traces go to the workspace that the API key belongs to. Organization-scoped service keys require it. To find the ID, see [Create an account and API key](https://docs.langchain.com/langsmith/create-account-api-key).
  - **Content mode**: Select **Full content** to include prompts and responses in the spans. With **Metadata only**, spans omit the input and output content.
  - **Workspaces**: The Claude workspaces that send traces to this destination: **All**, **Selected**, or **All except**. For details on each option, see [Choose workspaces for a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#choose-workspaces-for-a-destination) in the Anthropic docs.4. Click **Add destination**.


When you edit the destination later, the form shows the generic **OTLP endpoint URL** and **Request headers** fields instead of the LangSmith fields. The **OTLP endpoint URL** holds the URL of your region, and the LangSmith fields become these request headers:


- `x-api-key`: The **API key**.
- `Langsmith-Project`: The **Project**, if you set one.
- `X-Tenant-Id`: The **LangSmith workspace ID**, if you set one.


If you change the host of the **OTLP endpoint URL**, enter the header values again.


### [​](https://docs.langchain.com/langsmith/trace-anthropic#step-2-check-that-traces-arrive) Step 2. Check that traces arrive


To check the setup:


1. Send a Messages API request or run a Claude Managed Agents session in a Claude workspace that uses the destination.
2. On the Claude Console OpenTelemetry settings page, check that the **Delivery** column of the destination shows **Healthy**. This can take about a minute.
3. In LangSmith, open the project that you named in the **Project** field, or the `default` project.


### [​](https://docs.langchain.com/langsmith/trace-anthropic#troubleshoot-delivery) Troubleshoot delivery


If the **Delivery** column on the Claude Console [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) shows **Failing**, hold the pointer over it to see the last error:


- **HTTP 401**: The destination sends no API key.
- **HTTP 403**: The API key is wrong, or it has expired or been deleted. LangSmith also returns 403 for an organization-scoped service key without a workspace ID.
- **HTTP 404**: The endpoint URL is wrong. Edit the destination and check that the **OTLP endpoint URL** ends in `/otel` (`/api/v1/otel` for self-hosted LangSmith) and does not include `/v1/traces`.


For other errors, see [Delivery errors](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-errors) in the Anthropic docs.
If the **Delivery** column shows **Disabled**, hold the pointer over it to see why. For example, the Claude Platform disables a destination whose hostname resolves to an IP address that is not public. See [Delivery and health](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-and-health) in the Anthropic docs.


## [​](https://docs.langchain.com/langsmith/trace-anthropic#trace-from-your-application) Trace from your application


Use one of these methods when your application should send the traces. To trace your Anthropic calls together with the rest of your code in a single trace, use the LangSmith SDK wrapper.


### [​](https://docs.langchain.com/langsmith/trace-anthropic#use-the-claude-sdks) Use the Claude SDKs


The Claude SDKs emit OTel spans in your application for each request that they send and for each tool use that the tool runner runs. An OTel exporter library sends the spans to LangSmith. For details on the SDK options and the spans that the SDKs emit, see [Set up SDK tracing](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk) in the Anthropic docs.
To send Claude SDK spans to LangSmith:


1. [Install or upgrade the Claude SDK](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#install-the-sdk) and [register a tracer provider](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#register-a-tracer-provider).
2. Configure an OTel exporter with the OTel endpoint URL of your LangSmith deployment: | LangSmith deployment | OTel endpoint URL | | --- | --- | | GCP US | `https://api.smith.langchain.com/otel` | | GCP EU | `https://eu.api.smith.langchain.com/otel` | | GCP APAC | `https://apac.api.smith.langchain.com/otel` | | AWS US | `https://aws.api.smith.langchain.com/otel` | | Self-hosted | `https://<your-langsmith-host>/api/v1/otel` | Set the following request headers: For example, with the standard OTel environment variables: ``` export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your-langsmith-api-key>,Langsmith-Project=<your-project-name>" ``` For more information on exporter setup, see [Trace a non-LangChain application](https://docs.langchain.com/langsmith/trace-with-opentelemetry#trace-a-non-langchain-application).
  - `x-api-key`: Your LangSmith API key.
  - `Langsmith-Project`: (Optional) The name of the tracing project to send traces to. Without this header, traces go to the `default` project.
  - `X-Tenant-Id`: (Optional) The ID of the LangSmith workspace to send traces to. Without this header, traces go to the workspace that the API key belongs to. Organization-scoped service keys require it.3. (Optional) By default, the Claude SDKs record metadata only. To include prompts and responses in the spans, set the content mode. See [Configure the SDK](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#configure-the-sdk) in the Anthropic docs.


### [​](https://docs.langchain.com/langsmith/trace-anthropic#use-the-langsmith-sdk-wrapper) Use the LangSmith SDK wrapper


The Anthropic wrapper methods in Python ([`wrap_anthropic`](https://reference.langchain.com/python/langsmith/wrappers/_anthropic/wrap_anthropic)) and TypeScript ([`wrapAnthropic`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_anthropic.wrapAnthropic.html)) wrap your Anthropic client to log traces automatically. With the wrapper, LangSmith renders messages, including tool calls and multimodal content blocks, in a readable format. The wrapper works alongside the `@traceable` decorator (Python) or `traceable` function (TypeScript), so you can trace your Anthropic calls with the wrapper and trace other parts of your application with the decorator or function.
Set the `LANGSMITH_TRACING` environment variable to `'true'` to log traces to LangSmith, even when you use `wrap_anthropic` or `wrapAnthropic`. This lets you toggle tracing on and off without changing your code. Also set the `LANGSMITH_API_KEY` environment variable to your API key. To create a key, see [Create an account and API key](https://docs.langchain.com/langsmith/create-account-api-key). If your LangSmith API key is linked to multiple workspaces, set the `LANGSMITH_WORKSPACE_ID` environment variable to specify which workspace to use. By default, LangSmith logs traces to a project named `default`. To log traces to a different project, see [Log traces to a specific project](https://docs.langchain.com/langsmith/log-traces-to-project).
Python TypeScript

```
import anthropic
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())

@traceable(run_type="tool", name="Retrieve Context")
def my_tool(question: str) -> str:
  return "During this morning's meeting, we solved all world conflict."

@traceable(name="Chat Pipeline")
def chat_pipeline(question: str):
  context = my_tool(question)
  messages = [
      { "role": "user", "content": f"Question: {question}\nContext: {context}"}
  ]
  message = client.messages.create(
      model="claude-sonnet-5-5",
      messages=messages,
      max_tokens=1024,
      system="You are a helpful assistant. Please respond to the user's request only based on the given context."
  )
  return message

chat_pipeline("Can you summarize this morning's meetings?")
```


```
import Anthropic from "@anthropic-ai/sdk";
import { traceable } from "langsmith/traceable";
import { wrapAnthropic } from "langsmith/wrappers/anthropic";

const client = wrapAnthropic(new Anthropic());

const myTool = traceable(async (question: string) => {
  return "During this morning's meeting, we solved all world conflict.";
}, { name: "Retrieve Context", run_type: "tool" });

const chatPipeline = traceable(async (question: string) => {
  const context = await myTool(question);
  const messages = [
      { role: "user", content: `Question: ${question}\nContext: ${context}` }
  ];
  const message = await client.messages.create({
      model: "claude-sonnet-5-5",
      messages: messages,
      max_tokens: 1024,
      system: "You are a helpful assistant. Please respond to the user's request only based on the given context."
  });
  return message;
}, { name: "Chat Pipeline" });

await chatPipeline("Can you summarize this morning's meetings?");
```


To trace [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) sessions with the TypeScript `wrapAnthropic` wrapper, see [Trace Claude Managed Agents](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-anthropic.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Google Gemini applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-google-gemini`

# Trace Google Gemini applications

This guide shows you how to trace and log [Google’s Gemini](https://ai.google.dev/gemini-api/docs) models in LangSmith. You’ll instrument Gemini calls using the latest [`google-genai` SDK](https://googleapis.github.io/python-genai/) (Python) or [`@google/genai` SDK](https://googleapis.github.io/js-genai/release_docs/index.html) (JavaScript), wrap the Gemini client for tracing, and try examples including basic prompts, metadata tagging, and multi-turn conversations.
The LangSmith Gemini wrappers are in **[beta](https://docs.langchain.com/langsmith/release-stages)**. The API may change in future releases.


## [​](https://docs.langchain.com/langsmith/trace-with-google-gemini#installation) Installation


Install the required packages using your preferred package manager:
pip npm

```
pip install langsmith google-genai
```


```
npm install langsmith@latest @google/genai
```


## [​](https://docs.langchain.com/langsmith/trace-with-google-gemini#setup) Setup


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export LANGSMITH_TRACING=true
export GOOGLE_API_KEY=<your_google_api_key>
```


To create a Google API key, refer to [Google AI Studio](https://aistudio.google.com/apikey).


## [​](https://docs.langchain.com/langsmith/trace-with-google-gemini#configure-tracing) Configure tracing


To trace Gemini API calls, use LangSmith’s [`wrap_gemini`](https://reference.langchain.com/python/langsmith/wrappers/_gemini/wrap_gemini) (Python) or [`wrapGemini`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_gemini.wrapGemini.html) (JavaScript) wrapper function. This wrapper intercepts calls to the Gemini client and automatically logs them as traces in LangSmith. The wrapper preserves all of the original client’s functionality while adding observability:
Python JavaScript

```
from google import genai
from langsmith import wrappers

def main():
    # genai.Client() reads GOOGLE_API_KEY / GEMINI_API_KEY from the environment
    gemini_client = genai.Client()

    # Wrap the Gemini client to enable LangSmith tracing
    client = wrappers.wrap_gemini(
        gemini_client,
        tracing_extra={
            "tags": ["gemini", "python"],
            "metadata": {
                "integration": "google-genai",
            },
        },
    )

    # Make a traced Gemini call
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain quantum computing in simple terms.",
    )

    print(response.text)


if __name__ == "__main__":
    main()
```


```
import { GoogleGenAI } from "@google/genai";
import { wrapGemini } from "langsmith/wrappers/gemini";

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

// Initialize the Gemini client
const geminiClient = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

// Wrap the client to enable LangSmith tracing
// Configuration is applied to ALL calls made with this wrapped client
const client = wrapGemini(geminiClient, {
  tags: ["gemini", "javascript"],
  metadata: {
    integration: "google-genai",
  },
});

// Make a traced call - tracing happens automatically
const response = await client.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Explain quantum computing in simple terms.",
});

console.log(response.text);
```


- Python
- JavaScript

You can customize tracing by passing [`tracing_extra`](https://reference.langchain.com/python/langsmith/wrappers/_gemini/wrap_gemini) when calling `wrap_gemini()`. This parameter applies to all subsequent requests you make with that wrapped client, which allows you to attach tags and metadata for filtering and organizing traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-google-gemini). The `tracing_extra` parameter accepts:

- `tags`: A list of strings to categorize traces (for example, `["production", "gemini"]`).
- `metadata`: A dictionary of key-value pairs for additional context (for example, `{"team": "ml-research", "integration": "google-genai"}`).
- `client`: An optional custom LangSmith client instance.

These settings apply consistently across all traces from the wrapped client, so that you can include environment-level tags or team metadata that should remain constant throughout your application. You can customize tracing by passing configuration options to [`wrapGemini`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_gemini.wrapGemini.html). These options apply to all subsequent requests you make with that wrapped client, which allows you to attach tags and metadata for filtering and organizing traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-google-gemini). The configuration accepts:

- `tags`: An array of strings to categorize traces (for example, `["production", "gemini"]`).
- `metadata`: An object with key-value pairs for additional context (for example, `{ team: "ml-research", integration: "google-genai" }`).
- `client`: An optional custom LangSmith client instance.

These settings apply consistently across all traces from the wrapped client, so that you can include environment-level tags or team metadata that should remain constant throughout your application.


## [​](https://docs.langchain.com/langsmith/trace-with-google-gemini#view-traces-in-langsmith) View traces in LangSmith


After running your application, you can view traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-google-gemini) that include:


- **Model requests**: Complete prompts sent to Gemini models
- **Model responses**: Generated text and structured outputs
- **Function calls**: Tool invocations and results when using function calling
- **Chat sessions**: Multi-turn conversation context
- **Performance metrics**: Latency and token usage information


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-google-gemini.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure tracing
## ​View traces in LangSmith






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Amazon Bedrock applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-bedrock`

# Trace Amazon Bedrock applications

This guide shows you how to trace [Amazon Bedrock](https://aws.amazon.com/bedrock) model calls with LangSmith using the native AWS SDKs. LangSmith also works seamlessly with [LangChain’s Bedrock integrations](https://docs.langchain.com/oss/python/integrations/providers/aws). Either approach provides insights into:


- Request and response payloads
- Token usage and costs
- Latency and performance metrics
- Custom tags and metadata for filtering and analysis
- Multi-step chains and agent workflows


## [​](https://docs.langchain.com/langsmith/trace-bedrock#installation) Installation


pip npm

```
pip install boto3 langsmith
```


```
npm install @aws-sdk/client-bedrock-runtime langsmith
```


This integration uses the native AWS SDKs with LangSmith’s tracing capabilities. For Python, you’ll use [`boto3`](https://pypi.org/project/boto3/) (the AWS SDK for Python) along with [`langsmith`](https://pypi.org/project/langsmith/) to capture traces. For JavaScript/TypeScript, you’ll use [`@aws-sdk/client-bedrock-runtime`](https://www.npmjs.org/package/@aws-sdk/client-bedrock-runtime) with the [`langsmith`](https://www.npmjs.org/package/langsmith) package. Both implementations use the [Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html), which provides a unified interface for interacting with foundation models.


## [​](https://docs.langchain.com/langsmith/trace-bedrock#setup) Setup


To enable LangSmith tracing, configure your [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key) and project settings. You’ll also need to set up your AWS credentials to authenticate with Bedrock.


### [​](https://docs.langchain.com/langsmith/trace-bedrock#langsmith-configuration) LangSmith configuration


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name> # optional, defaults to "default"
export LANGSMITH_TRACING=true
```


You can obtain your LangSmith API key from [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-bedrock) by navigating to **Settings** > **API Keys**. The `LANGSMITH_PROJECT` variable allows you to organize traces into different projects.


### [​](https://docs.langchain.com/langsmith/trace-bedrock#aws-credentials) AWS credentials


Configure your AWS credentials to authenticate with Bedrock. You’ll need an AWS account with Bedrock access enabled. Follow the [AWS setup instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/setting-up.html) to create your credentials and [enable model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html):


```
export AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
export AWS_SESSION_TOKEN=<your_session_token> # only if using temporary credentials
export AWS_DEFAULT_REGION=<your_bedrock_region> # e.g., us-east-1 or us-west-2
```


## [​](https://docs.langchain.com/langsmith/trace-bedrock#configure-tracing) Configure tracing


Once your environment variables are set, you can trace Bedrock model calls by wrapping your invocation functions with LangSmith’s `@traceable` decorator (Python) or `traceable` function (TypeScript).
The following example demonstrates how to use the Bedrock Converse API with LangSmith tracing. The Converse API is AWS’s recommended unified interface for foundation models, providing consistent request and response handling across different model providers. You can enhance traces with custom tags and metadata—tags help you categorize traces (e.g., by environment, feature, or test type), while metadata allows you to attach arbitrary key-value pairs for detailed context:
Python TypeScript

```
import boto3
from langsmith import traceable

# Initialize Bedrock runtime client (ensure AWS creds and region are set)
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-haiku-4-5-20251001-v1:0"  # Example Bedrock model ID

# Decorate the model invocation function to auto-capture a trace with tags/metadata
@traceable(tags=["aws-bedrock", "langsmith", "integration-test"],
           metadata={"env": "dev", "model_provider": "bedrock", "model_id": "claude-haiku-4-5"})
def generate_text(prompt: str) -> str:
    # Prepare a single-turn conversation input for the Converse API
    messages = [
        {"role": "user", "content": [{"text": prompt}]}
    ]
    # Invoke the Bedrock model using the unified Converse API
    response = bedrock.converse(
        modelId=model_id,
        messages=messages,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}
    )
    # Extract the model's reply text from the response
    output_text = response["output"]["message"]["content"][0]["text"]
    return output_text

# Call the traced function with a prompt
result = generate_text("How can I trace AWS Bedrock model outputs to LangSmith for debugging?")
print(result)
```


```
import { BedrockRuntimeClient, ConverseCommand } from "@aws-sdk/client-bedrock-runtime";
import { traceable } from "langsmith";

const client = new BedrockRuntimeClient({ region: "us-east-1" });
const modelId = "anthropic.claude-haiku-4-5-20251001-v1:0";

// Wrap the Bedrock invocation in a traceable function with tags and metadata
const invokeBedrock = traceable(
  async (userInput: string) => {
    // Prepare the conversation message for the Bedrock Converse API
    const conversation = [
      { role: "user", content: [{ text: userInput }] }
    ];
    // Create and send a Bedrock Converse command (single-turn chat)
    const command = new ConverseCommand({
      modelId,
      messages: conversation,
      inferenceConfig: { maxTokens: 512, temperature: 0.5, topP: 0.9 }
    });
    const response = await client.send(command);
    // Extract the assistant's reply text from the response
    const outputText = response.output?.message?.content[0]?.text;
    return outputText;
  },
  {
    tags: ["aws-bedrock", "langsmith", "integration-test"],
    metadata: { env: "dev", model_provider: "bedrock", model_id: "claude-haiku-4-5" }
  }
);

// Invoke the traced function with a prompt
const answer = await invokeBedrock("How can I trace AWS Bedrock model outputs to LangSmith for debugging?");
console.log(answer);
```


- Python
- TypeScript


- `boto3.client("bedrock-runtime")` creates a Bedrock Runtime client.
- The `converse` method sends a chat prompt (as a list of messages) to the specified model and returns a structured response.
- The `generate_text` function is decorated with `@traceable`, logging each call to LangSmith as a trace (using the function name as the default trace name).
- Custom tags (`aws-bedrock`, `langsmith`, `integration-test`) and metadata (environment, model info) are passed into the decorator and attached to the trace record for filtering in the LangSmith UI.
- When you run this code (with `LANGSMITH_TRACING=true` and your API key set), LangSmith automatically captures the input prompt, model output, token usage, and latency.


- `BedrockRuntimeClient` from the AWS SDK v3 provides the Bedrock runtime interface.
- `ConverseCommand` offers a unified chat interface that sends a user message and returns the assistant’s response in a structured format (no manual JSON parsing needed).
- The Bedrock call is wrapped with LangSmith’s `traceable` function, converting `invokeBedrock` into a traced function that logs its execution to LangSmith.
- Custom tags and metadata are provided in the traceable options object and attached to each trace.
- When you run this script (with `LANGSMITH_TRACING=true` and your API key configured), check your LangSmith dashboard for trace entries that include the input prompt, model output, timing info, and specified tags/metadata.


## [​](https://docs.langchain.com/langsmith/trace-bedrock#view-traces-in-langsmith) View traces in LangSmith


After running your code, navigate to your LangSmith project at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-bedrock) to view the traces. Each trace includes:


- **Request details**: Input messages, model parameters, and configuration
- **Response details**: Model output, token usage, and response metadata
- **Performance metrics**: Latency, tokens per second, and cost estimates
- **Custom metadata**: Tags and metadata you provided to the `@traceable` decorator


You can filter traces by tags (e.g., `aws-bedrock` or `integration-test`), search by metadata fields, or drill into specific traces to debug issues.


## [​](https://docs.langchain.com/langsmith/trace-bedrock#next-steps) Next steps


- Learn more about [LangSmith features](https://docs.langchain.com/langsmith) including evaluation, datasets, and feedback
- Explore [Bedrock model capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/models-features.html) like tool calling, streaming, and prompt caching
- Review [LangChain Bedrock integration documentation](https://docs.langchain.com/oss/python/integrations/chat/bedrock) for advanced features like extended thinking and citations


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-bedrock.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure tracing
## ​View traces in LangSmith
## ​Next steps







Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace DeepSeek applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-deepseek`

# Trace DeepSeek applications

[DeepSeek](https://deepseek.com/) provides high-performance, OpenAI-compatible language models including `deepseek-chat` (for general conversations) and `deepseek-reasoner` (for advanced reasoning tasks). Using LangSmith allows you to debug, monitor, and evaluate your LLM applications by capturing structured traces of inputs, outputs, and metadata.
This guide shows you how to integrate DeepSeek with LangSmith in both Python and TypeScript, using LangSmith’s [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) (Python) and [`traceable(...)`](https://reference.langchain.com/javascript/modules/langsmith.html) (TypeScript) utilities to log LLM calls automatically.


## [​](https://docs.langchain.com/langsmith/trace-deepseek#installation) Installation


Install [OpenAI](https://platform.openai.com/docs/libraries) and LangSmith:
pip uv npm

```
pip install openai langsmith
```


```
uv add openai langsmith
```


```
npm install openai langsmith dotenv
```


DeepSeek provides an [OpenAI-compatible API](https://api-docs.deepseek.com/), which means you can use the OpenAI SDK to interact with DeepSeek models. The only difference is that you configure the client to point to DeepSeek’s base URL (`https://api.deepseek.com/v1`) instead of OpenAI’s endpoint.


## [​](https://docs.langchain.com/langsmith/trace-deepseek#setup) Setup


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY="your-langsmith-api-key"
export LANGSMITH_TRACING="true"
export LANGSMITH_PROJECT="deepseek-integration"
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```


- Ensure you have a DeepSeek API key from your [DeepSeek account](https://platform.deepseek.com/).
- Set `LANGSMITH_TRACING=true` and provide your LangSmith API key (`LANGSMITH_API_KEY`) activates automatic logging of traces.
- Specify a [`LANGSMITH_PROJECT`](https://docs.langchain.com/langsmith/log-traces-to-project) name to organize traces by project; if not set, traces go to the default project (named “default”).
- The `LANGSMITH_TRACING` flag must be true for any traces to be recorded.


## [​](https://docs.langchain.com/langsmith/trace-deepseek#configure-tracing) Configure tracing


1. Instrument the DeepSeek API call with LangSmith. In your script, create an OpenAI client configured to use DeepSeek’s API endpoint and wrap a call in a traced function: Python TypeScript ``` import os from openai import OpenAI from langsmith import traceable # Create a client pointing to DeepSeek client = OpenAI( api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com/v1" ) @traceable( run_type="llm", name="DeepSeek Chat Completion", metadata={"ls_provider": "deepseek", "ls_model_name": "deepseek-chat"}, ) def call_deepseek(messages: list[dict]): response = client.chat.completions.create( model="deepseek-chat", messages=messages ) return response.choices[0].message if __name__ == "__main__": messages = [ {"role": "system", "content": "You are a helpful assistant that translates English to French."}, {"role": "user", "content": "I love programming."} ] result = call_deepseek(messages=messages) print("Model reply:", result.content) ``` ``` import { config } from "dotenv"; import OpenAI from "openai"; import { traceable } from "langsmith/traceable"; config(); // Load env vars from .env const openai = new OpenAI({ apiKey: process.env.DEEPSEEK_API_KEY, baseURL: "https://api.deepseek.com/v1" }); type ChatMessage = { role: "system" | "user" | "assistant"; content: string; }; const callDeepSeek = traceable( async (messages: ChatMessage[]) => { const response = await openai.chat.completions.create({ model: "deepseek-chat", messages }); return response.choices[0].message; }, { name: "DeepSeek Chat Completion", run_type: "llm", metadata: { ls_provider: "deepseek", ls_model_name: "deepseek-chat" } } ); (async () => { const messages: ChatMessage[] = [ { role: "system", content: "You are a helpful assistant that translates English to French." }, { role: "user", content: "I love programming." } ]; const result = await callDeepSeek(messages); console.log("Model reply:", result.content); })(); ``` In this example, you use the OpenAI SDK to interact with [DeepSeek’s API](https://api-docs.deepseek.com/). The OpenAI client is configured with `base_url="https://api.deepseek.com/v1"` to route requests to DeepSeek’s endpoint while maintaining OpenAI-compatible syntax. The `@traceable` decorator (Python) or `traceable` function (TypeScript) wraps your function so that each invocation is logged as a trace run of type `"llm"`. The `metadata` parameter tags the trace with: The function returns the full message object (`response.choices[0].message`), which includes the response content along with metadata like the role and any additional fields. LangSmith automatically captures:
  - `ls_provider`: Identifies the provider (DeepSeek) for filtering traces.
  - `ls_model_name`: Specifies the model used for cost tracking and analytics.  - Input messages sent to the model.
  - The model’s complete response (content, role, etc.).
  - Model name and token usage statistics.
  - Execution timing and any errors.2. Execute your script to generate a trace: Python TypeScript ``` python deepseek_trace.py ``` ``` node deepseek_trace.js ``` The function call will reach out to DeepSeek’s API, and because of the `@traceable` / `traceable` wrapper, LangSmith will log this call’s inputs and outputs as a new trace. You’ll find the model’s response printed to the console, and a corresponding run appear in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deepseek).


## [​](https://docs.langchain.com/langsmith/trace-deepseek#view-traces-in-langsmith) View traces in LangSmith


After running the example, you can inspect the recorded traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deepseek):


1. Open the LangSmith UI and log in to your account.
2. Select the project you used for this integration (for example, the name set in `LANGSMITH_PROJECT`, or “default” if you didn’t set one).
3. Find the trace corresponding to your DeepSeek API call. It will be identified by the function name (`DeepSeek Chat Completion`).
4. Click on the trace to open it. You’ll be able to inspect the model input and output, including the prompt messages you sent and the response from DeepSeek, as well as timing information (latency) and token usage.


With LangSmith’s tracing, you have full visibility into your DeepSeek calls—allowing you to debug the behavior of DeepSeek’s models, monitor performance (response time and token usage), and compare runs with different parameters.


## [​](https://docs.langchain.com/langsmith/trace-deepseek#cost-tracking) Cost tracking


Although DeepSeek models are open-weight, using the hosted DeepSeek API may incur usage-based costs depending on your plan.
LangSmith can automatically associate costs with traced LLM calls by estimating token usage and applying model-specific pricing. When tracing DeepSeek API calls, LangSmith uses the recorded prompt and response messages to calculate token counts and attach cost information to each run.
To enable automatic cost tracking for LLM calls, refer to [Automatically track costs based on token counts](https://docs.langchain.com/langsmith/cost-tracking#llm-calls:-automatically-track-costs-based-on-token-counts).
Once enabled, costs appear directly in the LangSmith UI alongside each traced DeepSeek run, allowing you to monitor usage and compare experiments over time.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-deepseek.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure tracing
## ​View traces in LangSmith
## ​Cost tracking







Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Claude Managed Agents - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-claude-managed-agents`

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) are Anthropic’s hosted, cloud-based agents that run in managed environments. LangSmith supports tracing Claude Managed Agent sessions via the `wrapAnthropic` wrapper, giving you visibility into session events and message flows.
Claude Managed Agents tracing is currently supported in **TypeScript only**.


## [​](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents#installation) Installation


npm

```
npm install langsmith @anthropic-ai/sdk
```


yarn

```
yarn add langsmith @anthropic-ai/sdk
```


## [​](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents#environment-setup) Environment setup


Shell

```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-langsmith-api-key>
export ANTHROPIC_API_KEY=<your-anthropic-api-key>
```


## [​](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents#trace-claude-managed-agents) Trace Claude Managed Agents


Wrap the Anthropic client with `wrapAnthropic`. The wrapper traces all events that flow through the session.
TypeScript

```
import Anthropic from "@anthropic-ai/sdk";
import { wrapAnthropic } from "langsmith/wrappers/anthropic";

const anthropic = wrapAnthropic(new Anthropic());

// Create a managed agent
const agent = await anthropic.beta.agents.create({
  name: "my-agent",
  model: "claude-opus-4-8",
  system: "You are a helpful assistant.",
  tools: [
    // ... your tools here
  ],
});

// Create a cloud environment for the agent to run in
const environment = await anthropic.beta.environments.create({
  name: "my-environment",
  config: {
    type: "cloud",
    networking: { type: "unrestricted" },
  },
});

// Create a session connecting the agent and environment
const session = await anthropic.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  title: "My session",
});

// Stream session events
const stream = await anthropic.beta.sessions.events.stream(session.id);

// Send a message to the agent
await anthropic.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Hello! Can you help me with something?",
        },
      ],
    },
  ],
});

// Consume the event stream until the session is idle
for await (const event of stream) {
  if (event.type === "session.status_idle") {
    break;
  }
}
```


Full tracing of subagents in Anthropic’s multi-agent architecture requires
tapping into a separate event stream and is not yet supported. Only top-level
session events are traced.


## [​](https://docs.langchain.com/langsmith/trace-with-claude-managed-agents#next-steps) Next steps


- [Trace Anthropic models](https://docs.langchain.com/langsmith/trace-anthropic) — trace standard Anthropic API calls and tool use
- [Trace Claude Agent SDK applications](https://docs.langchain.com/langsmith/trace-claude-agent-sdk) — trace the Claude Agent SDK for local agentic apps
- [Monitor your agent](https://docs.langchain.com/langsmith/dashboards) — set up dashboards and alerts for production agents


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-claude-managed-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Environment setup
## ​Trace Claude Managed Agents
## ​Next steps






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace LiteLLM applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-litellm`

# Trace LiteLLM applications

[LiteLLM](https://www.litellm.ai/) provides a unified interface for calling LLM providers using a consistent OpenAI-compatible API. It can be used either as a [Python SDK](https://docs.litellm.ai/docs/#litellm-python-sdk) embedded directly in your application, or as a [proxy server](https://docs.litellm.ai/docs/simple_proxy) that exposes an OpenAI-compatible endpoint for client applications.
This guide shows you how to trace LiteLLM calls with LangSmith using:


- The [LangSmith SDK](https://docs.langchain.com/langsmith/trace-litellm#use-langsmith_tracing-and-traceable) (`@traceable`) for application-level tracing.
- [LiteLLM’s built-in langsmith callback](https://docs.langchain.com/langsmith/trace-litellm#log-litellm-call-with-the-langsmith-callback) for model-level logging.
- The [LiteLLM Proxy](https://docs.langchain.com/langsmith/trace-litellm#use-the-litellm-proxy) for gateway-level tracing.


## [​](https://docs.langchain.com/langsmith/trace-litellm#installation) Installation


Install the following when using either the LiteLLM Python SDK or LiteLLM Proxy:
Python SDK Proxy usage

```
pip install litellm langsmith openai
```


```
npm install openai langsmith
```


The examples in this guide use OpenAI models, but you can install the necessary provider for your use case.


## [​](https://docs.langchain.com/langsmith/trace-litellm#use-the-litellm-python-sdk) Use the LiteLLM Python SDK


LiteLLM supports two ways to send traces to LangSmith, which operate at different layers:


- [LangSmith SDK tracing](https://docs.langchain.com/langsmith/trace-litellm#use-langsmith_tracing-and-traceable) with `LANGSMITH_TRACING=true` enables application-level tracing via the LangSmith SDK. This is useful when you want to trace broader business logic, multi-step pipelines, or spans created with `@traceable`.
- LiteLLM’s built-in [`langsmith` callback](https://docs.langchain.com/langsmith/trace-litellm#log-litellm-call-with-the-langsmith-callback) logs model calls directly from LiteLLM. This is recommended when you want to trace LiteLLM requests specifically, or run async applications.


Avoid enabling LiteLLM’s `langsmith` callback and LangSmith tracing for the same LiteLLM calls, as this can result in duplicate traces.


### [​](https://docs.langchain.com/langsmith/trace-litellm#use-langsmith_tracing-and-traceable) Use `LANGSMITH_TRACING` and `traceable`


You can use `LANGSMITH_TRACING=true` together with `@traceable` for predictable traces in LangSmith. This approach ensures that the **Input** and **Output** columns reflect your function arguments and return values, allowing you to preserve the full message structure (including `role` and `content`). It also works reliably in simple synchronous scripts, without requiring an asyncio event loop or additional callback configuration.


1. Set the following environment variables to enable LangSmith tracing for LiteLLM Python SDK usage: ``` export LANGSMITH_API_KEY="your_api_key" export LANGSMITH_PROJECT="litellm-integration" export LANGSMITH_TRACING="true" ``` Create LangSmith [API keys](https://docs.langchain.com/langsmith/create-account-api-key) in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-litellm). Depending on what provider you’re using, you’ll also need to set API keys: ``` export OPENAI_API_KEY="your_openai_key" ```
2. Add the following code to your script file: ``` from langsmith import traceable from litellm import completion @traceable(name="LiteLLM Chat Completion") def run(messages): response = completion( model="gpt-5.5", messages=messages, ) # Return the assistant message so the LangSmith UI shows role + content return response["choices"][0]["message"] messages = [ {"role": "user", "content": "Explain observability in LLM systems."} ] result = run(messages) print(result["content"]) ``` `@traceable` instruments your function as a LangSmith run. When `LANGSMITH_TRACING=true` is set, LangSmith automatically: In this example, the `messages` argument becomes the trace input, and the returned assistant message object becomes the trace output. The LiteLLM call itself runs normally— `@traceable` wraps it with observability rather than modifying its behavior. This approach traces your application logic, not just the model call. For more general examples using `@traceable`, refer to the [Custom instrumentation](https://docs.langchain.com/langsmith/annotate-code#use-@traceable-/-traceable) page.
  - Creates a run when the function is invoked.
  - Records the function arguments as the run inputs.
  - Executes the function body (including the LiteLLM call).
  - Records the function’s return value as the run output.
  - Captures timing, errors, and nested spans (if any).


### [​](https://docs.langchain.com/langsmith/trace-litellm#log-litellm-call-with-the-langsmith-callback) Log LiteLLM call with the `langsmith` callback


LiteLLM can send traces directly to LangSmith using its built-in [callback system](https://docs.litellm.ai/docs/observability/callbacks). This is useful when running LiteLLM inside an async Python service and you want LiteLLM itself to emit model-level logs.
LiteLLM callbacks run in an asynchronous environment. When making asynchronous calls with `litellm.acompletion()`, you can enable the `langsmith` callback to log successful model calls.
This approach is best suited for async applications. For simple synchronous scripts, use the `@traceable` method shown in the [previous section](https://docs.langchain.com/langsmith/trace-litellm#use-langsmith_tracing-and-traceable).


1. Set the following environment variables: ``` export LANGSMITH_API_KEY="your_api_key" export LANGSMITH_PROJECT="litellm-integration" ``` Create LangSmith [API keys](https://docs.langchain.com/langsmith/create-account-api-key) in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-litellm). Depending on what provider you’re using, you’ll also need to set API keys: ``` export OPENAI_API_KEY="your_openai_key" ```
2. To run this in a minimal script: ``` import asyncio import litellm from litellm import acompletion # Enable LiteLLM → LangSmith callback litellm.success_callback = ["langsmith"] # For short-lived scripts, send immediately instead of waiting for batch flush litellm.langsmith_batch_size = 1 async def main(): response = await acompletion( model="gpt-5.5", messages=[ {"role": "user", "content": "Explain observability in LLM systems."} ], ) # Print the assistant message content for local verification print(response["choices"][0]["message"]["content"]) # Allow time for background logger to flush before process exit await asyncio.sleep(1) if __name__ == "__main__": asyncio.run(main()) ``` The callback sends LiteLLM’s model request and response data directly to LangSmith, including provider metadata and token usage. Because LiteLLM controls the payload, the **Input** and **Output** columns may include additional metadata compared to the `@traceable` example.
  - Use `acompletion()` (async API).
  - Run with `asyncio.run(...)` to create an event loop.
  - Set `langsmith_batch_size = 1` to flush immediately.


## [​](https://docs.langchain.com/langsmith/trace-litellm#use-the-litellm-proxy) Use the LiteLLM Proxy


The LiteLLM proxy runs as a standalone server and exposes an OpenAI-compatible API.


1. To have the proxy log requests directly to LangSmith, configure the callback in `config.yaml`: ``` model_list: - model_name: gpt-4o litellm_params: model: openai/gpt-4o litellm_settings: callbacks: ["langsmith"] ```
2. Set environment variables in your proxy environment: ``` export LANGSMITH_API_KEY="your_api_key" export LANGSMITH_PROJECT="litellm-proxy" export OPENAI_API_KEY="your_openai_key" ``` The LiteLLM proxy runs as a separate service. If you enable LangSmith tracing at the proxy level, you must configure `LANGSMITH_API_KEY` and related environment variables in the proxy’s runtime environment. These settings are not shared with your application process.
3. Start the proxy: ``` litellm --config config.yaml ``` By default, the proxy runs at `http://localhost:4000/v1`. Your application calls it using any OpenAI-compatible client (Python, JavaScript, curl, etc.). With `callbacks: ["langsmith"]` enabled, the proxy sends model request and response data directly to LangSmith. No tracing configuration is required in the client application.
4. Call the proxy from another terminal window: Python JavaScript ``` from openai import OpenAI client = OpenAI( base_url="http://localhost:4000/v1", api_key="anything" # proxy may require a key but doesn't validate it by default ) response = client.chat.completions.create( model="gpt-5.5", messages=[ {"role": "user", "content": "What is LiteLLM?"} ], ) print(response.choices[0].message.content) ``` ``` import OpenAI from "openai"; const client = new OpenAI({ apiKey: "anything", baseURL: "http://localhost:4000/v1", }); const response = await client.chat.completions.create({ model: "gpt-5.5", messages: [ { role: "user", content: "Explain LiteLLM tracing." } ], }); console.log(response.choices[0].message.content); ``` The client sends a normal chat completion request, and the proxy handles provider routing and response formatting.


## [​](https://docs.langchain.com/langsmith/trace-litellm#next-steps) Next steps


- [View traces in LangSmith](https://docs.langchain.com/langsmith/filter-traces)
- [Add custom metadata](https://docs.langchain.com/langsmith/ls-metadata-parameters)
- [Filter and sample traces](https://docs.langchain.com/langsmith/sample-traces)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-litellm.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Use the LiteLLM Python SDK
## ​Use the LiteLLM Proxy
## ​Next steps






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Models - Docs by LangChain

`https://docs.langchain.com/oss/python/langchain/models`

[LLMs](https://en.wikipedia.org/wiki/Large_language_model) are powerful AI tools that can interpret and generate text like humans. They’re versatile enough to write content, translate languages, summarize, and answer questions without needing specialized training for each task.
In addition to text generation, many models support:


- [Tool calling](https://docs.langchain.com/oss/python/langchain/models#tool-calling) - calling external tools (like databases queries or API calls) and use results in their responses.
- [Structured output](https://docs.langchain.com/oss/python/langchain/models#structured-output) - where the model’s response is constrained to follow a defined format.
- [Multimodality](https://docs.langchain.com/oss/python/langchain/models#multimodal) - process and return data other than text, such as images, audio, and video.
- [Reasoning](https://docs.langchain.com/oss/python/langchain/models#reasoning) - models perform multi-step reasoning to arrive at a conclusion.


Models are the reasoning engine of [agents](https://docs.langchain.com/oss/python/langchain/agents). They drive the agent’s decision-making process, determining which tools to call, how to interpret results, and when to provide a final answer.
The quality and capabilities of the model you choose directly impact your agent’s baseline reliability and performance. Different models excel at different tasks - some are better at following complex instructions, others at structured reasoning, and some support larger context windows for handling more information.
LangChain’s standard model interfaces give you access to many different provider integrations, which makes it easy to experiment with and switch between models to find the best fit for your use case.
For provider-specific integration information and capabilities, see the provider’s [chat model page](https://docs.langchain.com/oss/python/integrations/chat).
[LangSmith](https://docs.langchain.com/langsmith/observability) traces each model call so you can compare providers, inspect tool routing, and debug failures. Follow the [tracing quickstart](https://docs.langchain.com/langsmith/trace-with-langchain) to get set up. We recommend you also set up [LangSmith Engine](https://docs.langchain.com/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.


## [​](https://docs.langchain.com/oss/python/langchain/models#basic-usage) Basic usage


Models can be utilized in two ways:


1. **With agents** - Models can be dynamically specified when creating an [agent](https://docs.langchain.com/oss/python/langchain/agents#model).
2. **Standalone** - Models can be called directly (outside of the agent loop) for tasks like text generation, classification, or extraction without the need for an agent framework.


The same model interface works in both contexts, which gives you the flexibility to start simple and scale up to more complex agent-based workflows as needed.


### [​](https://docs.langchain.com/oss/python/langchain/models#initialize-a-model) Initialize a model


The easiest way to get started with a standalone model in LangChain is to use [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) to initialize one from a chat model provider of your choice (examples below):


- OpenAI
- Anthropic
- Azure
- Google Gemini
- AWS Bedrock
- HuggingFace
- OpenRouter

👉 Read the [OpenAI chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/openai) pip uv

```
pip install -U "langchain[openai]"
```


```
uv add "langchain[openai]"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["OPENAI_API_KEY"] = "sk-..."

model = init_chat_model("gpt-5.5")
```


```
import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-..."

model = ChatOpenAI(model="gpt-5.5")
```

👉 Read the [Anthropic chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/anthropic) pip uv

```
pip install -U "langchain[anthropic]"
```


```
uv add "langchain[anthropic]"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["ANTHROPIC_API_KEY"] = "sk-..."

model = init_chat_model("claude-sonnet-4-6")
```


```
import os
from langchain_anthropic import ChatAnthropic

os.environ["ANTHROPIC_API_KEY"] = "sk-..."

model = ChatAnthropic(model="claude-sonnet-4-6")
```

👉 Read the [Azure chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/azure_chat_openai) pip uv

```
pip install -U "langchain[openai]"
```


```
uv add "langchain[openai]"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["AZURE_OPENAI_API_KEY"] = "..."
os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

model = init_chat_model(
    "azure_openai:gpt-5.5",
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)
```


```
import os
from langchain_openai import AzureChatOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = "..."
os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

model = AzureChatOpenAI(
    model="gpt-5.5",
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
)
```

👉 Read the [Google GenAI chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) pip uv

```
pip install -U "langchain[google-genai]"
```


```
uv add "langchain[google-genai]"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = "..."

model = init_chat_model("google_genai:gemini-3.7-flash")
```


```
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "..."

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
```

👉 Read the [AWS Bedrock chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/bedrock) pip uv

```
pip install -U "langchain[aws]"
```


```
uv add "langchain[aws]"
```

init_chat_model Model Class

```
from langchain.chat_models import init_chat_model

# Follow the steps here to configure your credentials:
# https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

model = init_chat_model(
    "us.anthropic.claude-sonnet-4-6",
    model_provider="bedrock_converse",
)
```


```
from langchain_aws import ChatBedrock

model = ChatBedrock(model="us.anthropic.claude-sonnet-4-6")
```

👉 Read the [HuggingFace chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/huggingface) pip uv

```
pip install -U "langchain[huggingface]"
```


```
uv add "langchain[huggingface]"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

model = init_chat_model(
    "microsoft/Phi-3-mini-4k-instruct",
    model_provider="huggingface",
    temperature=0.7,
    max_tokens=1024,
)
```


```
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    temperature=0.7,
    max_length=1024,
)
model = ChatHuggingFace(llm=llm)
```

👉 Read the [OpenRouter chat model integration docs](https://docs.langchain.com/oss/python/integrations/chat/openrouter) pip uv

```
pip install -U "langchain-openrouter"
```


```
uv add "langchain-openrouter"
```

init_chat_model Model Class

```
import os
from langchain.chat_models import init_chat_model

os.environ["OPENROUTER_API_KEY"] = "sk-..."

model = init_chat_model(
    "auto",
    model_provider="openrouter",
)
```


```
import os
from langchain_openrouter import ChatOpenRouter

os.environ["OPENROUTER_API_KEY"] = "sk-..."

model = ChatOpenRouter(model="auto")
```


```
response = model.invoke("Why do parrots talk?")
```


See [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) for more detail, including information on how to pass model [parameters](https://docs.langchain.com/oss/python/langchain/models#parameters).


### [​](https://docs.langchain.com/oss/python/langchain/models#supported-providers-and-models) Supported providers and models


LangChain supports all major model providers through dedicated integration packages. Each provider package implements the same standard interface, so you can swap providers without rewriting application logic. New model names work immediately — no LangChain update required — because provider packages pass model names directly to the provider’s API.
Browse the [full list of supported providers](https://docs.langchain.com/oss/python/integrations/providers/overview), or see [Providers and models](https://docs.langchain.com/oss/python/concepts/providers-and-models) for a conceptual overview of how providers, packages, and model names work together in LangChain.


### [​](https://docs.langchain.com/oss/python/langchain/models#key-methods) Key methods


## Invoke

The model takes messages as input and outputs messages after generating a complete response.


## Stream

Invoke the model, but stream the output as it is generated in real-time.


## Batch

Send multiple requests to a model in a batch for more efficient processing.
In addition to chat models, LangChain provides support for other adjacent technologies, such as embedding models and vector stores. See the [integrations page](https://docs.langchain.com/oss/python/integrations/providers/overview) for details.


## [​](https://docs.langchain.com/oss/python/langchain/models#parameters) Parameters


A chat model takes parameters that can be used to configure its behavior. The full set of supported parameters varies by model and provider, but standard ones include:
[​](https://docs.langchain.com/oss/python/langchain/models#param-model) model string required The name or identifier of the specific model you want to use with a provider. You can also specify both the model and its provider in a single argument using the ’:’ format, for example, ‘openai:o1’.
[​](https://docs.langchain.com/oss/python/langchain/models#param-api-key) api_key string The key required for authenticating with the model’s provider. This is usually issued when you sign up for access to the model. Often accessed by setting an environment variable.
[​](https://docs.langchain.com/oss/python/langchain/models#param-temperature) temperature number Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic.
[​](https://docs.langchain.com/oss/python/langchain/models#param-max-tokens) max_tokens number Limits the total number of tokens in the response, effectively controlling how long the output can be.
[​](https://docs.langchain.com/oss/python/langchain/models#param-timeout) timeout number The maximum time (in seconds) to wait for a response from the model before canceling the request.
[​](https://docs.langchain.com/oss/python/langchain/models#param-max-retries) max_retries number default:"6"The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits. Retries use exponential backoff with jitter. Network errors, rate limits (429), and server errors (5xx) are retried automatically. Client errors such as 401 (unauthorized) or 404 are not retried. For long-running [agent](https://docs.langchain.com/oss/python/deepagents/overview) tasks on unreliable networks, consider increasing this to 10–15.
Using [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model), pass these parameters as inline `**kwargs`:
Initialize using model parameters

```
model = init_chat_model(
    "claude-sonnet-4-6",
    # Kwargs passed to the model:
    temperature=0.7,
    timeout=30,
    max_tokens=1000,
    max_retries=6,  # Default; increase for unreliable networks
)
```


### [​](https://docs.langchain.com/oss/python/langchain/models#connection-resilience) Connection resilience


LangChain chat models automatically retry failed API requests with exponential backoff. By default, models retry up to **6 times** for network errors, rate limits (429), and server errors (5xx). Client errors like 401 (unauthorized) or 404 are not retried.
You can adjust `max_retries` and `timeout` when creating a model, then pass that instance to `create_agent`, `create_deep_agent`, or call it standalone:


```
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "google_genai:gemini-3.6-flash",
    max_retries=10,  # Increase for unreliable networks (default: 6)
    timeout=120,  # Seconds; increase for slow connections
)
```


For long-running agent graphs on unreliable networks, consider higher `max_retries` (for example 10–15) and a [checkpointer](https://docs.langchain.com/oss/python/langgraph/persistence) so that progress is preserved across failures.
Each chat model integration may have additional params used to control provider-specific functionality. For example, [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) has `use_responses_api` to dictate whether to use the OpenAI Responses or Completions API. To find all the parameters supported by a given chat model, head to the [chat model integrations](https://docs.langchain.com/oss/python/integrations/chat) page.


---


## [​](https://docs.langchain.com/oss/python/langchain/models#invocation) Invocation


A chat model must be invoked to generate an output. There are three primary invocation methods, each suited to different use cases.


### [​](https://docs.langchain.com/oss/python/langchain/models#invoke) Invoke


The most straightforward way to call a model is to use [`invoke()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/invoke) with a single message or a list of messages.
Single message

```
response = model.invoke("Why do parrots have colorful feathers?")
print(response)
```


A list of messages can be provided to a chat model to represent conversation history. Each message has a role that models use to indicate who sent the message in the conversation.
See the [messages](https://docs.langchain.com/oss/python/langchain/messages) guide for more detail on roles, types, and content.
Dictionary format

```
conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")
```


Message objects

```
from langchain.messages import HumanMessage, AIMessage, SystemMessage

conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")
```


If the return type of your invocation is a string, ensure that you are using a chat model as opposed to an LLM. Legacy, text-completion LLMs return strings directly. LangChain chat models are prefixed with “Chat”, e.g., [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) (/oss/integrations/chat/openai).


### [​](https://docs.langchain.com/oss/python/langchain/models#stream) Stream


Most models can stream their output content while it is being generated. By displaying output progressively, streaming significantly improves user experience, particularly for longer responses.
Calling [`stream()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/stream) returns an iterator that yields output chunks as they are produced. You can use a loop to process each chunk in real-time:
Basic text streaming Stream tool calls, reasoning, and other content

```
for chunk in model.stream("Why do parrots have colorful feathers?"):
    print(chunk.text, end="|", flush=True)
```


```
for chunk in model.stream("What color is the sky?"):
    for block in chunk.content_blocks:
        if block["type"] == "reasoning" and (reasoning := block.get("reasoning")):
            print(f"Reasoning: {reasoning}")
        elif block["type"] == "tool_call_chunk":
            print(f"Tool call chunk: {block}")
        elif block["type"] == "text":
            print(block["text"])
        else:
            ...
```


As opposed to [`invoke()`](https://docs.langchain.com/oss/python/langchain/models#invoke), which returns a single [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) after the model has finished generating its full response, `stream()` returns multiple [`AIMessageChunk`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk) objects, each containing a portion of the output text. Importantly, each chunk in a stream is designed to be gathered into a full message via summation:
Construct an AIMessage

```
full = None  # None | AIMessageChunk
for chunk in model.stream("What color is the sky?"):
    full = chunk if full is None else full + chunk
    print(full.text)

# The
# The sky
# The sky is
# The sky is typically
# The sky is typically blue
# ...

print(full.content_blocks)
# [{"type": "text", "text": "The sky is typically blue..."}]
```


The resulting message can be treated the same as a message that was generated with [`invoke()`](https://docs.langchain.com/oss/python/langchain/models#invoke) —for example, it can be aggregated into a message history and passed back to the model as conversational context.
Streaming only works if all steps in the program know how to process a stream of chunks. For instance, an application that isn’t streaming-capable would be one that needs to store the entire output in memory before it can be processed.
## Documentation Index
## ​Basic usage
## ​Parameters
## ​Invocation
## ​Tool calling
## ​Structured output
## ​Advanced topics









Advanced streaming topics


Streaming events

LangChain chat models can also stream semantic events using `astream_events()`. This simplifies filtering based on event types and other metadata, and will aggregate the full message in the background. See below for an example.

```
async for event in model.astream_events("Hello"):

    if event["event"] == "on_chat_model_start":
        print(f"Input: {event['data']['input']}")

    elif event["event"] == "on_chat_model_stream":
        print(f"Token: {event['data']['chunk'].text}")

    elif event["event"] == "on_chat_model_end":
        print(f"Full message: {event['data']['output'].text}")

    else:
        pass
```


```
Input: Hello
Token: Hi
Token:  there
Token: !
Token:  How
Token:  can
Token:  I
...
Full message: Hi there! How can I help today?
```

See the [`astream_events()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.astream_events) reference for event types and other details.

"Auto-streaming" chat models

LangChain simplifies streaming from chat models by automatically enabling streaming mode in certain cases, even when you’re not explicitly calling the streaming methods. This is particularly useful when you use the non-streaming invoke method but still want to stream the entire application, including intermediate results from the chat model. In [LangGraph agents](https://docs.langchain.com/oss/python/langchain/agents), for example, you can call `model.invoke()` within nodes, but LangChain will automatically delegate to streaming if running in a streaming mode.

#### [​](https://docs.langchain.com/oss/python/langchain/models#how-it-works) How it works

When you `invoke()` a chat model, LangChain will automatically switch to an internal streaming mode if it detects that you are trying to stream the overall application. The result of the invocation will be the same as far as the code that was using invoke is concerned; however, while the chat model is being streamed, LangChain will take care of invoking [`on_llm_new_token`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_new_token) events in LangChain’s callback system. Callback events allow LangGraph `stream()` and `astream_events()` to surface the chat model’s output in real-time.


### [​](https://docs.langchain.com/oss/python/langchain/models#batch) Batch


Batching a collection of independent requests to a model can significantly improve performance and reduce costs, as the processing can be done in parallel:
Batch

```
responses = model.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])
for response in responses:
    print(response)
```


This section describes a chat model method [`batch()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch), which parallelizes model calls client-side. It is **distinct** from batch APIs supported by inference providers, such as [OpenAI](https://platform.openai.com/docs/guides/batch) or [Anthropic](https://platform.claude.com/docs/en/build-with-claude/batch-processing#message-batches-api).
By default, [`batch()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch) will only return the final output for the entire batch. If you want to receive the output for each individual input as it finishes generating, you can stream results with [`batch_as_completed()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch_as_completed):
Yield batch responses upon completion

```
for response in model.batch_as_completed([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
]):
    print(response)
```


When using [`batch_as_completed()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch_as_completed), results may arrive out of order. Each includes the input index for matching to reconstruct the original order as needed.
When processing a large number of inputs using [`batch()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch) or [`batch_as_completed()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch_as_completed), you may want to control the maximum number of parallel calls. This can be done by setting the [`max_concurrency`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) attribute in the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) dictionary. Batch with max concurrency

```
model.batch(
    list_of_inputs,
    config={
        'max_concurrency': 5,  # Limit to 5 parallel calls
    }
)
```

See the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) reference for a full list of supported attributes.
For more details on batching, see the [reference](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch).


---


## [​](https://docs.langchain.com/oss/python/langchain/models#tool-calling) Tool calling


Models can request to call tools that perform tasks such as fetching data from a database, searching the web, or running code. Tools are pairings of:


1. A schema, including the name of the tool, a description, and/or argument definitions (often a JSON schema)
2. A function or coroutine to execute.


You may hear the term “function calling”. We use this interchangeably with “tool calling”.
Here’s the basic tool calling flow between a user and a model:

To make tools that you have defined available for use by a model, you must bind them using [`bind_tools`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools). In subsequent invocations, the model can choose to call any of the bound tools as needed.
Some model providers offer built-in tools that can be enabled via model or invocation parameters (e.g. [`ChatOpenAI`](https://docs.langchain.com/oss/python/integrations/chat/openai), [`ChatAnthropic`](https://docs.langchain.com/oss/python/integrations/chat/anthropic)). Check the respective [provider reference](https://docs.langchain.com/oss/python/integrations/providers/overview) for details.
See the [tools guide](https://docs.langchain.com/oss/python/langchain/tools) for details and other options for creating tools.
Binding user tools

```
from langchain.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the weather at a location."""
    return f"It's sunny in {location}."


model_with_tools = model.bind_tools([get_weather])

response = model_with_tools.invoke("What's the weather like in Boston?")
for tool_call in response.tool_calls:
    # View tool calls made by the model
    print(f"Tool: {tool_call['name']}")
    print(f"Args: {tool_call['args']}")
```


When binding user-defined tools, the model’s response includes a **request** to execute a tool. When using a model separately from an [agent](https://docs.langchain.com/oss/python/langchain/agents), it is up to you to execute the requested tool and return the result back to the model for use in subsequent reasoning. When using an [agent](https://docs.langchain.com/oss/python/langchain/agents), the agent loop will handle the tool execution loop for you.
Below, we show some common ways you can use tool calling.


Tool execution loop

When a model returns tool calls, you need to execute the tools and pass the results back to the model. This creates a conversation loop where the model can use tool results to generate its final response. LangChain includes [agent](https://docs.langchain.com/oss/python/langchain/agents) abstractions that handle this orchestration for you. Here’s a simple example of how to do this: Tool execution loop

```
# Bind (potentially multiple) tools to the model
tools = [get_weather]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

# Step 1: Model generates tool calls
messages = [{"role": "user", "content": "What's the weather in Boston?"}]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

# Step 2: Execute tools and collect results
for tool_call in ai_msg.tool_calls:
    # Execute the tool with the generated arguments
    tool = tools_by_name[tool_call["name"]]
    tool_result = tool.invoke(tool_call)
    messages.append(tool_result)

# Step 3: Pass results back to model for final response
final_response = model_with_tools.invoke(messages)
print(final_response.text)
# "The current weather in Boston is 72°F and sunny."
```

Each [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) returned by the tool includes a `tool_call_id` that matches the original tool call, helping the model correlate results with requests.

Forcing tool calls

By default, the model has the freedom to choose which bound tool to use based on the user’s input. However, you might want to force choosing a tool, ensuring the model uses either a particular tool or **any** tool from a given list: Force use of any tool Force use of specific tools

```
model_with_tools = model.bind_tools([tool_1], tool_choice="any")
```


```
model_with_tools = model.bind_tools([tool_1], tool_choice="tool_1")
```


Parallel tool calls

Many models support calling multiple tools in parallel when appropriate. This allows the model to gather information from different sources simultaneously. Parallel tool calls

```
tools = [get_weather]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

response = model_with_tools.invoke(
    "What's the weather in Boston and Tokyo?"
)


# The model may generate multiple tool calls
print(response.tool_calls)
# [
#   {'name': 'get_weather', 'args': {'location': 'Boston'}, 'id': 'call_1'},
#   {'name': 'get_weather', 'args': {'location': 'Tokyo'}, 'id': 'call_2'},
# ]


# Execute all tools (can be done in parallel with async)
results = []
for tool_call in response.tool_calls:
    tool = tools_by_name[tool_call["name"]]
    result = tool.invoke(tool_call)
    results.append(result)
```

The model intelligently determines when parallel execution is appropriate based on the independence of the requested operations. Most models supporting tool calling enable parallel tool calls by default. Some (including [OpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai) and [Anthropic](https://docs.langchain.com/oss/python/integrations/chat/anthropic)) allow you to disable this feature. To do this, set `parallel_tool_calls=False`:

```
model.bind_tools([get_weather], parallel_tool_calls=False)
```


Streaming tool calls

When streaming responses, tool calls are progressively built through [`ToolCallChunk`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolCallChunk). This allows you to see tool calls as they’re being generated rather than waiting for the complete response. Streaming tool calls

```
for chunk in model_with_tools.stream(
    "What's the weather in Boston and Tokyo?"
):
    # Tool call chunks arrive progressively
    for tool_chunk in chunk.tool_call_chunks:
        if name := tool_chunk.get("name"):
            print(f"Tool: {name}")
        if id_ := tool_chunk.get("id"):
            print(f"ID: {id_}")
        if args := tool_chunk.get("args"):
            print(f"Args: {args}")

# Output:
# Tool: get_weather
# ID: call_SvMlU1TVIZugrFLckFE2ceRE
# Args: {"lo
# Args: catio
# Args: n": "B
# Args: osto
# Args: n"}
# Tool: get_weather
# ID: call_QMZdy6qInx13oWKE7KhuhOLR
# Args: {"lo
# Args: catio
# Args: n": "T
# Args: okyo
# Args: "}
```

You can accumulate chunks to build complete tool calls: Accumulate tool calls

```
gathered = None
for chunk in model_with_tools.stream("What's the weather in Boston?"):
    gathered = chunk if gathered is None else gathered + chunk
    print(gathered.tool_calls)
```


---


## [​](https://docs.langchain.com/oss/python/langchain/models#structured-output) Structured output


Models can be requested to provide their response in a format matching a given schema. This is useful for ensuring the output can be easily parsed and used in subsequent processing. LangChain supports multiple schema types and methods for enforcing structured output.
To learn about structured output, see [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output).


- Pydantic
- TypedDict
- JSON Schema

[Pydantic models](https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage) provide the richest feature set with field validation, descriptions, and nested structures.

```
from pydantic import BaseModel, Field

class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movie's rating out of 10")

model_with_structure = model.with_structured_output(Movie)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)
```

Python’s `TypedDict` provides a simpler alternative to Pydantic models, ideal when you don’t need runtime validation.

```
from typing_extensions import TypedDict, Annotated

class MovieDict(TypedDict):
    """A movie with details."""
    title: Annotated[str, ..., "The title of the movie"]
    year: Annotated[int, ..., "The year the movie was released"]
    director: Annotated[str, ..., "The director of the movie"]
    rating: Annotated[float, ..., "The movie's rating out of 10"]

model_with_structure = model.with_structured_output(MovieDict)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # {'title': 'Inception', 'year': 2010, 'director': 'Christopher Nolan', 'rating': 8.8}
```

Provide a [JSON Schema](https://json-schema.org/understanding-json-schema/about) for maximum control and interoperability.

```
import json

json_schema = {
    "title": "Movie",
    "description": "A movie with details",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of the movie"
        },
        "year": {
            "type": "integer",
            "description": "The year the movie was released"
        },
        "director": {
            "type": "string",
            "description": "The director of the movie"
        },
        "rating": {
            "type": "number",
            "description": "The movie's rating out of 10"
        }
    },
    "required": ["title", "year", "director", "rating"]
}

model_with_structure = model.with_structured_output(
    json_schema,
    method="json_schema",
)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # {'title': 'Inception', 'year': 2010, ...}
```


**Key considerations for structured output**

- **Method parameter**: Some providers support different methods for structured output:
  - `'json_schema'`: Uses dedicated structured output features offered by the provider.
  - `'function_calling'`: Derives structured output by forcing a [tool call](https://docs.langchain.com/oss/python/langchain/models#tool-calling) that follows the given schema.
  - `'json_mode'`: A precursor to `'json_schema'` offered by some providers. Generates valid JSON, but the schema must be described in the prompt.- **Include raw**: Set `include_raw=True` to get both the parsed output and the raw AI message.
- **Validation**: Pydantic models provide automatic validation. `TypedDict` and JSON Schema require manual validation.

See your [provider’s integration page](https://docs.langchain.com/oss/python/integrations/providers/overview) for supported methods and configuration options.


Example: Message output alongside parsed structure

It can be useful to return the raw [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) object alongside the parsed representation to access response metadata such as [token counts](https://docs.langchain.com/oss/python/langchain/models#token-usage). To do this, set [`include_raw=True`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output) when calling [`with_structured_output`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output):

```
from pydantic import BaseModel, Field

class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movie's rating out of 10")

model_with_structure = model.with_structured_output(Movie, include_raw=True)
response = model_with_structure.invoke("Provide details about the movie Inception")
response
# {
#     "raw": AIMessage(...),
#     "parsed": Movie(title=..., year=..., ...),
#     "parsing_error": None,
# }
```


Example: Nested structures

Schemas can be nested: Pydantic BaseModel TypedDict

```
from pydantic import BaseModel, Field

class Actor(BaseModel):
    name: str
    role: str

class MovieDetails(BaseModel):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: float | None = Field(None, description="Budget in millions USD")

model_with_structure = model.with_structured_output(MovieDetails)
```


```
from typing_extensions import Annotated, TypedDict

class Actor(TypedDict):
    name: str
    role: str

class MovieDetails(TypedDict):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: Annotated[float | None, ..., "Budget in millions USD"]

model_with_structure = model.with_structured_output(MovieDetails)
```


---


## [​](https://docs.langchain.com/oss/python/langchain/models#advanced-topics) Advanced topics


### [​](https://docs.langchain.com/oss/python/langchain/models#model-profiles) Model profiles


Model profiles require `langchain>=1.1`.
LangChain chat models can expose a dictionary of supported features and capabilities through a `profile` attribute:


```
model.profile
# {
#   "max_input_tokens": 400000,
#   "image_inputs": True,
#   "reasoning_output": True,
#   "tool_calling": True,
#   ...
# }
```


Refer to the full set of fields in the [API reference](https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile).
Much of the model profile data is powered by the [models.dev](https://github.com/sst/models.dev) project, an open source initiative that provides model capability data. These data are augmented with additional fields for purposes of use with LangChain. These augmentations are kept aligned with the upstream project as it evolves.
Model profile data allow applications to work around model capabilities dynamically. For example:


1. [Summarization middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization) can trigger summarization based on a model’s context window size.
2. [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output) strategies in `create_agent` can be inferred automatically (e.g., by checking support for native structured output features).
3. Model inputs can be gated based on supported [modalities](https://docs.langchain.com/oss/python/langchain/models#multimodal) and maximum input tokens.
4. [Deep Agents Code](https://docs.langchain.com/oss/deepagents/code) filters the [interactive model switcher](https://docs.langchain.com/oss/deepagents/code/providers#which-models-appear-in-the-switcher) to models whose profiles report `tool_calling` support and text I/O, and displays context window sizes and capability flags in the selector detail view.


Updating or overwriting profile data

Model profile data can be changed if it is missing, stale, or incorrect. **Option 1 (quick fix)** You can instantiate a chat model with any valid profile:

```
custom_profile = {
    "max_input_tokens": 100_000,
    "tool_calling": True,
    "structured_output": True,
    # ...
}
model = init_chat_model("...", profile=custom_profile)
```

The `profile` is also a regular `dict` and can be updated in place. If the model instance is shared, consider using `model_copy` to avoid mutating shared state.

```
new_profile = model.profile | {"key": "value"}
model.model_copy(update={"profile": new_profile})
```

**Option 2 (fix data upstream)** The primary source for the data is the [models.dev](https://models.dev/) project. This data is merged with additional fields and overrides in LangChain [integration packages](https://docs.langchain.com/oss/python/integrations/providers/overview) and are shipped with those packages. Model profile data can be updated through the following process:

1. (If needed) update the source data at [models.dev](https://models.dev/) through a pull request to its [repository on GitHub](https://github.com/sst/models.dev).
2. (If needed) update additional fields and overrides in `langchain_<package>/data/profile_augmentations.toml` through a pull request to the LangChain [integration package](https://docs.langchain.com/oss/python/integrations/providers/overview)`.
3. Use the [`langchain-model-profiles`](https://pypi.org/project/langchain-model-profiles/) CLI tool to pull the latest data from [models.dev](https://models.dev/), merge in the augmentations and update the profile data:

pip uv

```
pip install -U langchain-model-profiles
```


```
uv add langchain-model-profiles
```


```
langchain-profiles refresh --provider <provider> --data-dir <data_dir>
```

This command:

- Downloads the latest data for `<provider>` from models.dev
- Merges augmentations from `profile_augmentations.toml` in `<data_dir>`
- Writes merged profiles to `profiles.py` in `<data_dir>`

For example: from [`libs/partners/anthropic`](https://github.com/langchain-ai/langchain/tree/master/libs/partners/anthropic) in the [LangChain monorepo](https://github.com/langchain-ai/langchain):

```
uv run --with langchain-model-profiles --provider anthropic --data-dir langchain_anthropic/data
```


Model profiles are a beta feature. The format of a profile is subject to change.


### [​](https://docs.langchain.com/oss/python/langchain/models#multimodal) Multimodal


Certain models can process and return non-textual data such as images, audio, and video. You can pass non-textual data to a model by providing [content blocks](https://docs.langchain.com/oss/python/langchain/messages#message-content).
All LangChain chat models with underlying multimodal capabilities support:

1. Data in the cross-provider standard format (see [our messages guide](https://docs.langchain.com/oss/python/langchain/messages))
2. OpenAI [chat completions](https://platform.openai.com/docs/api-reference/chat) format
3. Any format that is native to that specific provider (e.g., Anthropic models accept Anthropic native format)


See the [multimodal section](https://docs.langchain.com/oss/python/langchain/messages#multimodal) of the messages guide for details.
Some models can return multimodal data as part of their response. If invoked to do so, the resulting [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) will have content blocks with multimodal types.
Multimodal output

```
response = model.invoke("Create a picture of a cat")
print(response.content_blocks)
# [
#     {"type": "text", "text": "Here's a picture of a cat"},
#     {"type": "image", "base64": "...", "mime_type": "image/jpeg"},
# ]
```


See the [integrations page](https://docs.langchain.com/oss/python/integrations/providers/overview) for details on specific providers.


### [​](https://docs.langchain.com/oss/python/langchain/models#reasoning) Reasoning


Many models are capable of performing multi-step reasoning to arrive at a conclusion. This involves breaking down complex problems into smaller, more manageable steps.
**If supported by the underlying model,** you can surface this reasoning process to better understand how the model arrived at its final answer.
Stream reasoning output Complete reasoning output

```
for chunk in model.stream("Why do parrots have colorful feathers?"):
    reasoning_steps = [r for r in chunk.content_blocks if r["type"] == "reasoning"]
    print(reasoning_steps if reasoning_steps else chunk.text)
```


```
response = model.invoke("Why do parrots have colorful feathers?")
reasoning_steps = [b for b in response.content_blocks if b["type"] == "reasoning"]
print(" ".join(step["reasoning"] for step in reasoning_steps))
```


Depending on the model, you can sometimes specify the level of effort it should put into reasoning. Similarly, you can request that the model turn off reasoning entirely. This may take the form of categorical “tiers” of reasoning (e.g., `'low'` or `'high'`) or integer token budgets.
`reasoning_effort` as a standard parameter requires `langchain-core>=1.5.2`, plus the corresponding partner package version: `langchain-anthropic>=1.5.3`, `langchain-openai>=1.4.1`, `langchain-fireworks>=1.5.2`, `langchain-xai>=1.3.0`, `langchain-google-genai>=4.3.1`, or `langchain-aws>=1.7.0`.
[`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI), [`ChatAnthropic`](https://reference.langchain.com/python/langchain-anthropic/chat_models/ChatAnthropic), [`ChatFireworks`](https://reference.langchain.com/python/langchain-fireworks/chat_models/ChatFireworks), [`ChatXAI`](https://reference.langchain.com/python/langchain-xai/chat_models/ChatXAI), [`ChatGoogleGenerativeAI`](https://reference.langchain.com/python/langchain-google-genai/chat_models/ChatGoogleGenerativeAI), and [`ChatBedrockConverse`](https://reference.langchain.com/python/langchain-aws/chat_models/bedrock_converse/ChatBedrockConverse) support a standard `reasoning_effort` parameter. Like `temperature`, it can be set at model construction or per invocation, and each provider translates it into its own API format:


```
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-6")
response = model.invoke(
    "Why do parrots have colorful feathers?",
    reasoning_effort="high",
)
```


Supported effort levels and the provider’s documented default vary by model. Check a model’s [profile](https://docs.langchain.com/oss/python/langchain/models#model-profiles) for the levels it supports and its default:


```
model.profile["reasoning_effort_levels"]  # e.g. ['low', 'medium', 'high']
model.profile["reasoning_effort_default"]  # e.g. 'high'
```


Some providers also accept a native alias for `reasoning_effort` (for example, `ChatAnthropic` accepts `effort` and `ChatGoogleGenerativeAI` accepts `thinking_level`). See the [chat model integrations](https://docs.langchain.com/oss/python/integrations/chat) page for provider-specific detail.
For details, see the [integrations page](https://docs.langchain.com/oss/python/integrations/providers/overview) or [reference](https://reference.langchain.com/python/integrations/) for your respective chat model.


### [​](https://docs.langchain.com/oss/python/langchain/models#local-models) Local models


LangChain supports running models locally on your own hardware. This is useful for scenarios where either data privacy is critical, you want to invoke a custom model, or when you want to avoid the costs incurred when using a cloud-based model.
[Ollama](https://docs.langchain.com/oss/python/integrations/chat/ollama) is one of the easiest ways to run chat and embedding models locally.


### [​](https://docs.langchain.com/oss/python/langchain/models#prompt-caching) Prompt caching


Many providers offer prompt caching features to reduce latency and cost on repeat processing of the same tokens. You can engage caching at three levels:


- **Implicit provider caching:** providers automatically pass on cost savings if a request hits a cache, with no configuration required. Examples: [OpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai) and [Gemini](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai).
- **Provider-level explicit controls:** providers let you manually indicate cache points for greater control or to guarantee cost savings. These mirror the underlying provider/API behavior. Examples:
  - [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) (via `prompt_cache_key`)
  - Anthropic content-block [`cache_control`](https://docs.langchain.com/oss/python/integrations/chat/anthropic#prompt-caching)
  - [Gemini](https://reference.langchain.com/python/langchain-google-genai).
  - AWS Bedrock [`cachePoint`](https://docs.langchain.com/oss/python/integrations/chat/bedrock#prompt-caching) blocks- **LangChain middleware:** for agents, middleware lets LangChain optimize caching of stable system prompt and tool content. Examples:
  - Anthropic’s [`AnthropicPromptCachingMiddleware`](https://docs.langchain.com/oss/python/integrations/middleware/anthropic#prompt-caching)
  - AWS Bedrock’s [`BedrockPromptCachingMiddleware`](https://docs.langchain.com/oss/python/integrations/middleware/aws#prompt-caching)


Prompt caching is often only engaged above a minimum input token threshold. See [provider pages](https://docs.langchain.com/oss/python/integrations/chat) for details.
Cache usage will be reflected in the [usage metadata](https://docs.langchain.com/oss/python/langchain/messages#token-usage) of the model response.


### [​](https://docs.langchain.com/oss/python/langchain/models#server-side-tool-use) Server-side tool use


Some providers support server-side [tool-calling](https://docs.langchain.com/oss/python/langchain/models#tool-calling) loops: models can interact with web search, code interpreters, and other tools and analyze the results in a single conversational turn.
If a model invokes a tool server-side, the content of the response message will include content representing the invocation and result of the tool. Accessing the [content blocks](https://docs.langchain.com/oss/python/langchain/messages#standard-content-blocks) of the response will return the server-side tool calls and results in a provider-agnostic format:
Invoke with server-side tool use

```
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5.4-mini")

tool = {"type": "web_search"}
model_with_tools = model.bind_tools([tool])

response = model_with_tools.invoke("What was a positive news story from today?")
print(response.content_blocks)
```


Result

```
[
    {
        "type": "server_tool_call",
        "name": "web_search",
        "args": {
            "query": "positive news stories today",
            "type": "search"
        },
        "id": "ws_abc123"
    },
    {
        "type": "server_tool_result",
        "tool_call_id": "ws_abc123",
        "status": "success"
    },
    {
        "type": "text",
        "text": "Here are some positive news stories from today...",
        "annotations": [
            {
                "end_index": 410,
                "start_index": 337,
                "title": "article title",
                "type": "citation",
                "url": "..."
            }
        ]
    }
]
```

See all 29 lines
This represents a single conversational turn; there are no associated [ToolMessage](https://docs.langchain.com/oss/python/langchain/messages#tool-message) objects that need to be passed in as in client-side [tool-calling](https://docs.langchain.com/oss/python/langchain/models#tool-calling).
See the [integration page](https://docs.langchain.com/oss/python/integrations/chat) for your given provider for available tools and usage details.


### [​](https://docs.langchain.com/oss/python/langchain/models#model-exceptions) Model exceptions


Major integration packages raise standard exception types from `langchain_core.exceptions` for common model failures such as authentication errors, rate limits, and timeouts. These exceptions inherit from both the LangChain base type and the provider SDK’s own exception type, so you can catch either one:


```
from langchain.chat_models import init_chat_model
from langchain_core.exceptions import ModelTimeoutError

model = init_chat_model("openai:gpt-5.6-luna", timeout=0.0001)

try:
    response = model.invoke("Hello")
except ModelTimeoutError:
    print("caught")
```


Each type carries an `is_retryable` attribute that [retry middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in#model-retry) respects by default.


Exception types


- [`ModelAuthenticationError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelAuthenticationError) — missing, invalid, or expired API key (not retryable)
- [`ModelPermissionDeniedError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelPermissionDeniedError) — credentials lack permission (not retryable)
- [`ModelInvalidRequestError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelInvalidRequestError) — provider rejects the request (not retryable)
- [`ModelNotFoundError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelNotFoundError) — requested model not found (not retryable)
- [`ModelRateLimitError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelRateLimitError) — provider rate limit exceeded (retryable)
- [`ModelAPIError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelAPIError) — provider server failure (retryable)
- [`ModelConnectionError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelConnectionError) — provider cannot be reached (retryable)
- [`ModelTimeoutError`](https://reference.langchain.com/python/langchain-core/exceptions/ModelTimeoutError) — request times out (retryable)
- [`ContextOverflowError`](https://reference.langchain.com/python/langchain-core/exceptions/ContextOverflowError) — input exceeds the model context limit (not retryable)


### [​](https://docs.langchain.com/oss/python/langchain/models#rate-limiting) Rate limiting


Many chat model providers impose a limit on the number of invocations that can be made in a given time period. If you hit a rate limit, you will typically receive a rate limit error response from the provider, and will need to wait before making more requests.
To help manage rate limits, chat model integrations accept a `rate_limiter` parameter that can be provided during initialization to control the rate at which requests are made.


Initialize and use a rate limiter

LangChain comes with (an optional) built-in [`InMemoryRateLimiter`](https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter). This limiter is thread safe and can be shared by multiple threads in the same process. Define a rate limiter

```
from langchain.rate_limiters import InMemoryRateLimiter

rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # 1 request every 10s
    check_every_n_seconds=0.1,  # Check every 100ms whether allowed to make a request
    max_bucket_size=10,  # Controls the maximum burst size.
)

model = init_chat_model(
    model="gpt-5.5",
    model_provider="openai",
    rate_limiter=rate_limiter
)
```

The provided rate limiter can only limit the number of requests per unit time. It will not help if you need to also limit based on the size of the requests.


### [​](https://docs.langchain.com/oss/python/langchain/models#base-url-and-proxy-settings) Base URL and proxy settings


You can configure a custom base URL for providers that implement the OpenAI Chat Completions API.
`model_provider="openai"` (or direct `ChatOpenAI` usage) targets the official OpenAI API specification. Provider-specific fields from routers and proxies may not be extracted or preserved. For OpenRouter and LiteLLM, prefer the dedicated integrations:

- [OpenRouter via `ChatOpenRouter`](https://docs.langchain.com/oss/python/integrations/chat/openrouter) (`langchain-openrouter`)
- [LiteLLM via `ChatLiteLLM` / `ChatLiteLLMRouter`](https://docs.langchain.com/oss/python/integrations/chat) (`langchain-litellm`)


Custom base URL

Many model providers offer OpenAI-compatible APIs (e.g., [Together AI](https://www.together.ai/), [vLLM](https://github.com/vllm-project/vllm)). You can use [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) with these providers by specifying the appropriate `base_url` parameter:

```
model = init_chat_model(
    model="MODEL_NAME",
    model_provider="openai",
    base_url="BASE_URL",
    api_key="YOUR_API_KEY",
)
```

When using direct chat model class instantiation, the parameter name may vary by provider. Check the respective [reference](https://docs.langchain.com/oss/python/integrations/providers/overview) for details.


HTTP proxy configuration

For deployments requiring HTTP proxies, some model integrations support proxy configuration:

```
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5.5",
    openai_proxy="http://proxy.example.com:8080"
)
```

Proxy support varies by integration. Check the specific model provider’s [reference](https://docs.langchain.com/oss/python/integrations/providers/overview) for proxy configuration options.


### [​](https://docs.langchain.com/oss/python/langchain/models#log-probabilities) Log probabilities


Certain models can be configured to return token-level log probabilities representing the likelihood of a given token by setting the `logprobs` parameter when initializing the model:


```
model = init_chat_model(
    model="gpt-5.5",
    model_provider="openai"
).bind(logprobs=True)

response = model.invoke("Why do parrots talk?")
print(response.response_metadata["logprobs"])
```


### [​](https://docs.langchain.com/oss/python/langchain/models#token-usage) Token usage


A number of model providers return token usage information as part of the invocation response. When available, this information will be included on the [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) objects produced by the corresponding model. For more details, see the [messages](https://docs.langchain.com/oss/python/langchain/messages) guide.
Some provider APIs, notably OpenAI and Azure OpenAI chat completions, require users opt-in to receiving token usage data in streaming contexts. See the [streaming usage metadata](https://docs.langchain.com/oss/python/integrations/chat/openai#streaming-usage-metadata) section of the integration guide for details.
You can track aggregate token counts across models in an application using either a callback or context manager, as shown below:


- Callback handler
- Context manager


```
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import UsageMetadataCallbackHandler

model_1 = init_chat_model(model="gpt-5.4-mini")
model_2 = init_chat_model(model="claude-haiku-4-5-20251001")

callback = UsageMetadataCallbackHandler()
result_1 = model_1.invoke("Hello", config={"callbacks": [callback]})
result_2 = model_2.invoke("Hello", config={"callbacks": [callback]})
print(callback.usage_metadata)
```


```
{
    'gpt-5.4-mini': {
        'input_tokens': 8,
        'output_tokens': 10,
        'total_tokens': 18,
        'input_token_details': {'audio': 0, 'cache_read': 0},
        'output_token_details': {'audio': 0, 'reasoning': 0}
    },
    'claude-haiku-4-5-20251001': {
        'input_tokens': 8,
        'output_tokens': 21,
        'total_tokens': 29,
        'input_token_details': {'cache_read': 0, 'cache_creation': 0}
    }
}
```


```
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import get_usage_metadata_callback

model_1 = init_chat_model(model="gpt-5.4-mini")
model_2 = init_chat_model(model="claude-haiku-4-5-20251001")

with get_usage_metadata_callback() as cb:
    model_1.invoke("Hello")
    model_2.invoke("Hello")
    print(cb.usage_metadata)
```


```
{
    'gpt-5.4-mini': {
        'input_tokens': 8,
        'output_tokens': 10,
        'total_tokens': 18,
        'input_token_details': {'audio': 0, 'cache_read': 0},
        'output_token_details': {'audio': 0, 'reasoning': 0}
    },
    'claude-haiku-4-5-20251001': {
        'input_tokens': 8,
        'output_tokens': 21,
        'total_tokens': 29,
        'input_token_details': {'cache_read': 0, 'cache_creation': 0}
    }
}
```


### [​](https://docs.langchain.com/oss/python/langchain/models#invocation-config) Invocation config


When invoking a model, you can pass additional configuration through the `config` parameter using a [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) dictionary. This provides run-time control over execution behavior, callbacks, and metadata tracking.
Common configuration options include:
Invocation with config

```
response = model.invoke(
    "Tell me a joke",
    config={
        "run_name": "joke_generation",      # Custom name for this run
        "tags": ["humor", "demo"],          # Tags for categorization
        "metadata": {"user_id": "123"},     # Custom metadata
        "callbacks": [my_callback_handler], # Callback handlers
    }
)
```


These configuration values are particularly useful when:


- Debugging with [LangSmith](https://docs.langchain.com/langsmith/observability) tracing
- Implementing custom logging or monitoring
- Controlling resource usage in production
- Tracking invocations across complex pipelines


Key configuration attributes

[​](https://docs.langchain.com/oss/python/langchain/models#param-run-name) run_name string Identifies this specific invocation in logs and traces. Not inherited by sub-calls. [​](https://docs.langchain.com/oss/python/langchain/models#param-tags) tags string[] Labels inherited by all sub-calls for filtering and organization in debugging tools. [​](https://docs.langchain.com/oss/python/langchain/models#param-metadata) metadata object Custom key-value pairs for tracking additional context, inherited by all sub-calls. [​](https://docs.langchain.com/oss/python/langchain/models#param-max-concurrency) max_concurrency number Controls the maximum number of parallel calls when using [`batch()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch) or [`batch_as_completed()`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.batch_as_completed). [​](https://docs.langchain.com/oss/python/langchain/models#param-callbacks) callbacks array Handlers for monitoring and responding to events during execution. [​](https://docs.langchain.com/oss/python/langchain/models#param-recursion-limit) recursion_limit number Maximum recursion depth for chains to prevent infinite loops in complex pipelines.
See full [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) reference for all supported attributes.


### [​](https://docs.langchain.com/oss/python/langchain/models#configurable-models) Configurable models


You can also create a runtime-configurable model by specifying [`configurable_fields`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.configurable_fields). If you don’t specify a model value, then `'model'` and `'model_provider'` will be configurable by default.


```
from langchain.chat_models import init_chat_model

configurable_model = init_chat_model(temperature=0)

configurable_model.invoke(
    "what's your name",
    config={"configurable": {"model": "gpt-5-nano"}},  # Run with GPT-5-Nano
)
configurable_model.invoke(
    "what's your name",
    config={"configurable": {"model": "claude-sonnet-4-6"}},  # Run with Claude
)
```


Configurable model with default values

We can create a configurable model with default model values, specify which parameters are configurable, and add prefixes to configurable params:

```
first_model = init_chat_model(
        model="gpt-5.4-mini",
        temperature=0,
        configurable_fields=("model", "model_provider", "temperature", "max_tokens"),
        config_prefix="first",  # Useful when you have a chain with multiple models
)

first_model.invoke("what's your name")
```


```
first_model.invoke(
    "what's your name",
    config={
        "configurable": {
            "first_model": "claude-sonnet-4-6",
            "first_temperature": 0.5,
            "first_max_tokens": 100,
        }
    },
)
```

See the [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) reference for more details on `configurable_fields` and `config_prefix`.


Using a configurable model declaratively

We can call declarative operations like `bind_tools`, `with_structured_output`, `with_configurable`, etc. on a configurable model and chain a configurable model in the same way that we would a regularly instantiated chat model object.

```
from pydantic import BaseModel, Field


class GetWeather(BaseModel):
    """Get the current weather in a given location"""

        location: str = Field(description="The city and state, e.g. San Francisco, CA")


class GetPopulation(BaseModel):
    """Get the current population in a given location"""

        location: str = Field(description="The city and state, e.g. San Francisco, CA")


model = init_chat_model(temperature=0)
model_with_tools = model.bind_tools([GetWeather, GetPopulation])

model_with_tools.invoke(
    "what's bigger in 2024 LA or NYC", config={"configurable": {"model": "gpt-5.4-mini"}}
).tool_calls
```


```
[
    {
        'name': 'GetPopulation',
        'args': {'location': 'Los Angeles, CA'},
        'id': 'call_Ga9m8FAArIyEjItHmztPYA22',
        'type': 'tool_call'
    },
    {
        'name': 'GetPopulation',
        'args': {'location': 'New York, NY'},
        'id': 'call_jh2dEvBaAHRaw5JUDthOs7rt',
        'type': 'tool_call'
    }
]
```


```
model_with_tools.invoke(
    "what's bigger in 2024 LA or NYC",
    config={"configurable": {"model": "claude-sonnet-4-6"}},
).tool_calls
```


```
[
    {
        'name': 'GetPopulation',
        'args': {'location': 'Los Angeles, CA'},
        'id': 'toolu_01JMufPf4F4t2zLj7miFeqXp',
        'type': 'tool_call'
    },
    {
        'name': 'GetPopulation',
        'args': {'location': 'New York City, NY'},
        'id': 'toolu_01RQBHcE8kEEbYTuuS8WqY1u',
        'type': 'tool_call'
    }
]
```


### [​](https://docs.langchain.com/oss/python/langchain/models#dynamic-model-selection) Dynamic model selection


Dynamic models are selected at runtime based on the current state and context. This enables sophisticated routing logic and cost optimization.
To use a dynamic model, create middleware using the [`@wrap_model_call`](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_model_call) decorator that modifies the model in the request:


```
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse


basic_model = ChatOpenAI(model="gpt-5.4-mini")
advanced_model = ChatOpenAI(model="gpt-5.5")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))

agent = create_agent(
    model=basic_model,  # Default model
    tools=[],
    middleware=[dynamic_model_selection]
)
```


Pre-bound models (models with [`bind_tools`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools) already called) are not supported when using structured output. If you need dynamic model selection with structured output, ensure the models passed to the middleware are not pre-bound.
For model configuration details, see [Models](https://docs.langchain.com/oss/python/langchain/models). For dynamic model selection patterns, see [Dynamic model in middleware](https://docs.langchain.com/oss/python/langchain/middleware#dynamic-model).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Deep Agents overview - Docs by LangChain

`https://docs.langchain.com/oss/python/deepagents/overview`

# Deep Agents overview
## ​Try it
## ​Quickstart
## ​Core capabilities
## ​Execution environment
## ​Context management
## ​Delegation
## ​Steering
## ​Get started









Build agents that can plan, use subagents, and leverage file systems for complex tasks

Deep Agents is the easiest way to start building agents and applications that are powered by LLMs—with built-in capabilities for file systems for context management, subagent-spawning, and long-term memory.
Optional capabilities such as [task planning](https://docs.langchain.com/oss/python/deepagents/overview#task-planning) and [skills](https://docs.langchain.com/oss/python/deepagents/overview#skills) extend the harness when your use case needs them.
You can use deep agents for any task, including complex, multi-step tasks.
Deep Agents comes with the following capabilities:


- **Take actions in an environment**: Take actions via tools, read and write files, execute code
- **Connect to your data**: Load memories, skills, and domain knowledge at the right moment
- **Manage growing context**: Summarize history and offload large results across long runs
- **Parallelize tasks**: Delegate to general or specialized subagents running in isolated context windows
- **Stay in the loop**: Pause for human approval at critical decision points
- **Improve over time**: Update memory, skills, and prompts based on real usage


See [Core capabilities](https://docs.langchain.com/oss/python/deepagents/overview#core-capabilities) for a full breakdown of each component.


## [​](https://docs.langchain.com/oss/python/deepagents/overview#try-it) Try it


## [​](https://docs.langchain.com/oss/python/deepagents/overview#quickstart) Quickstart


Google OpenAI Anthropic OpenRouter Fireworks Baseten Ollama

```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="openrouter:z-ai/glm-5.2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="baseten:zai-org/GLM-5.2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


```
from deepagents import create_deep_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model="ollama:north-mini-code-1.0",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```


## View example trace

Open a public LangSmith run for this example.
See the [Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart) and [Customization guide](https://docs.langchain.com/oss/python/deepagents/customization) to get started building your own agents and applications with Deep Agents.
Trace requests, debug agent behavior, and evaluate outputs with [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-deepagents-overview). Follow the [observability quickstart](https://docs.langchain.com/langsmith/observability-quickstart) to get set up. When ready for production, see [Going to production](https://docs.langchain.com/oss/python/deepagents/going-to-production) for LangSmith deployment options.


## [​](https://docs.langchain.com/oss/python/deepagents/overview#core-capabilities) Core capabilities


![Agent harness capabilities by category](https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_harness_capabilities.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=0ff671d72badd0844826660dfcb04391)
Deep Agents is an [“agent harness”](https://docs.langchain.com/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in capabilities that make agents reliable for real tasks:
## Documentation Index



## Execution environment

Tools, virtual filesystem, optional sandbox, and REPL (interpreter)

## Context management

Skills, memory, summarization, context offloading, and prompt caching

## Delegation

Subagent spawning and optional task planning

## Steering

Human-in-the-loop approval and interrupts
[`deepagents`](https://pypi.org/project/deepagents/) is a standalone library built on top of [LangChain](https://docs.langchain.com/oss/python/langchain)’s core building blocks for agents. It uses the [LangGraph](https://docs.langchain.com/oss/python/langgraph) runtime for durable execution, streaming, human-in-the-loop, and other features.
[LangChain](https://docs.langchain.com/oss/python/langchain) is the framework that provides the core building blocks for your agents.
To learn more about the differences between LangChain, LangGraph, and Deep Agents, see [Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/python/concepts/products). For a side-by-side comparison with Anthropic’s harness, see [Deep Agents vs. Claude Agent SDK](https://docs.langchain.com/oss/python/deepagents/comparison).
For building custom agents without these built-in capabilities, consider using LangChain’s [`create_agent`](https://docs.langchain.com/oss/python/langchain/agents) or building a custom [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) workflow.


## [​](https://docs.langchain.com/oss/python/deepagents/overview#execution-environment) Execution environment


The execution environment is where an agent acts. It has four layers:


- **[Tools](https://docs.langchain.com/oss/python/deepagents/overview#tools-and-mcp)**: custom functions, APIs, and databases the agent can call
- **[Virtual filesystem](https://docs.langchain.com/oss/python/deepagents/overview#virtual-filesystem-access)**: file tools backed by pluggable backends
- **[Filesystem permissions](https://docs.langchain.com/oss/python/deepagents/overview#filesystem-permissions)**: declarative access control over which paths agents can read or write
- **[Code execution](https://docs.langchain.com/oss/python/deepagents/overview#code-execution)**: sandboxed shell execution and an in-process JavaScript interpreter


**[Streaming](https://docs.langchain.com/oss/python/deepagents/overview#streaming)** allows you to keep up with everything happening using typed event streams for messages, tools, values, and delegated tasks.


### [​](https://docs.langchain.com/oss/python/deepagents/overview#tools-and-mcp) Tools and MCP


Pass custom functions, LangChain tools, or tools from any [MCP server](https://docs.langchain.com/oss/python/deepagents/tools#mcp-tools) with the `tools=` parameter. Deep Agents fully support the [Model Context Protocol (MCP)](https://docs.langchain.com/oss/python/langchain/mcp), letting you connect to databases, APIs, file systems, and more through a standard interface.


```
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search, fetch_page, run_query],
)
```


For more information on defining custom tools, using MCP servers, and the full list of built-in harness tools, see [Tools](https://docs.langchain.com/oss/python/deepagents/tools).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#virtual-filesystem-access) Virtual filesystem access


The harness provides a configurable virtual filesystem which can be backed by different [pluggable backends](https://docs.langchain.com/oss/python/deepagents/backends): in-memory state, local disk, LangGraph store, composite routing, or a custom backend with [permission rules](https://docs.langchain.com/oss/python/deepagents/permissions) for read and write access.
The backends support the following file system operations:


| Tool | Description |
| --- | --- |
| `ls` | List files in a directory with metadata (size, modified time) |
| `read_file` | Read file contents with line numbers, supports offset/limit for large files. Also supports returning multimodal content blocks for non-text files (images, video, audio, and documents). See supported extensions below. |
| `write_file` | Create a new file, or overwrite an existing one |
| `edit_file` | Perform exact string replacements in files (with global replace mode) |
| `delete` | Delete a file, or a directory and its contents recursively |
| `glob` | Find files matching patterns (e.g., `**/*.py`) |
| `grep` | Search file contents with multiple output modes (files only, content with context, or counts) |
| `execute` | Run shell commands in the environment (available with [sandbox backends](https://docs.langchain.com/oss/python/deepagents/sandboxes) only) |


The `delete` tool requires `deepagents>=0.7`. Backends that do not support deletion have the tool automatically hidden from the model.


Supported multimodal file extensions


| Type | Extensions |
| --- | --- |
| [Image](https://docs.langchain.com/oss/python/langchain/messages#multimodal) | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.heic`, `.heif` |
| [Video](https://docs.langchain.com/oss/python/langchain/messages#multimodal) | `.mp4`, `.mpeg`, `.mov`, `.avi`, `.flv`, `.mpg`, `.webm`, `.wmv`, `.3gpp` |
| [Audio](https://docs.langchain.com/oss/python/langchain/messages#multimodal) | `.wav`, `.mp3`, `.aiff`, `.aac`, `.ogg`, `.flac` |
| [File](https://docs.langchain.com/oss/python/langchain/messages#multimodal) | `.pdf`, `.ppt`, `.pptx` |


Running without the default filesystem tools

To hide the filesystem tools listed above from the model, register a [harness profile](https://docs.langchain.com/oss/python/deepagents/profiles#harness-profiles) with `excluded_tools`:

```
from deepagents import HarnessProfile, register_harness_profile

register_harness_profile(
    "anthropic:claude-sonnet-4-6",
    HarnessProfile(
        excluded_tools=frozenset(
            {"ls", "read_file", "write_file", "edit_file", "delete", "glob", "grep"}
        ),
    ),
)
```

Removing [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) itself via `excluded_middleware` is intentionally rejected—it is required scaffolding in the [Deep Agents stack](https://docs.langchain.com/oss/python/deepagents/customization#deep-agents-stack). Use `excluded_tools` to hide only the model-visible tool surface and leave the middleware in place. To remove the `task` tool, see [Running without subagents](https://docs.langchain.com/oss/python/deepagents/subagents#running-without-subagents).


Restricting filesystem tools

The `tools` allowlist on `FilesystemMiddleware` requires `deepagents>=0.7`. To expose only a subset of the filesystem tools listed above, instead of hiding them all, pass a `tools` allowlist to [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) and provide the instance through `middleware=`. Any built-in filesystem tool left out of the list is removed from the model’s tool list.

```
from deepagents import create_deep_agent
from deepagents.middleware import FilesystemMiddleware

# Read-only agent: write_file, edit_file, delete, and execute are never shown
agent = create_deep_agent(
    model="claude-sonnet-4-6",
    middleware=[
        FilesystemMiddleware(backend=backend, tools=["read_file", "ls", "glob", "grep"]),
    ],
)
```

`read_file` must always be included in the list—omitting it raises `ValueError` when the agent is created. The `execute` and `delete` tools are also dropped from the tool surface whenever the configured backend doesn’t support them, whether or not you include them in `tools`. Custom tools you add through `create_deep_agent`’s own `tools=` argument are never affected by this allowlist. Passing your own [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) instance this way replaces the default one for the main agent and the general-purpose subagent inherits the same restriction. See [Override a default middleware instance](https://docs.langchain.com/oss/python/deepagents/customization#override-a-default-middleware-instance) for more information. Declarative subagents don’t inherit it: include a `FilesystemMiddleware(tools=...)` instance in that subagent’s own `middleware` field to restrict it independently.
The virtual filesystem is used by several other harness capabilities such as skills, memory, code execution, and context management.
You can also use the file system when building custom tools and middleware for Deep Agents.
For more information, see [backends](https://docs.langchain.com/oss/python/deepagents/backends). To generate a durable repository wiki that agents can read from the filesystem, see [OpenWiki](https://docs.langchain.com/oss/openwiki/overview).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#filesystem-permissions) Filesystem permissions


The harness supports declarative permission rules that control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools listed above and are evaluated in declaration order with first-match-wins semantics.
Define permissions by passing a list of rules to `permissions=` when creating the agent. Each rule includes:


- `operations`: `"read"` and/or `"write"`
- `paths`: Glob patterns for files or directories
- `mode`: `"allow"` or `"deny"`


Rules are evaluated top to bottom, and the first matching rule wins. If no rule matches, the operation is allowed.
This model lets you restrict agents to specific directories (for example, `/workspace/`), protect sensitive files such as `.env` or credentials, and give subagents narrower access than the parent agent.
Permissions do not apply to [sandbox backends](https://docs.langchain.com/oss/python/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool. For custom validation logic, use [backend policy hooks](https://docs.langchain.com/oss/python/deepagents/backends#add-policy-hooks).
For the full rule structure, examples, and subagent inheritance, see [Permissions](https://docs.langchain.com/oss/python/deepagents/permissions).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#code-execution) Code execution


Deep Agents supports code execution in two ways:


- [Sandbox backends](https://docs.langchain.com/oss/python/deepagents/sandboxes) expose an `execute` tool for shell commands in an isolated environment.
- [Interpreters](https://docs.langchain.com/oss/python/deepagents/interpreters) add an `eval` tool that runs JavaScript in a scoped QuickJS runtime.


Use sandbox backends when the agent needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem. Sandbox backends implement the `SandboxBackendProtocolV2`; when detected, the harness adds the `execute` tool to the agent’s available tools.
Use interpreters when the agent needs a lightweight programmable layer for loops, batching, deterministic data transformations, or programmatic tool calling. Interpreters do not provide shell access, package installs, or filesystem and network access.
For sandbox setup, providers, and file transfer APIs, see [Sandboxes](https://docs.langchain.com/oss/python/deepagents/sandboxes). For the QuickJS runtime and programmatic tool calling, see [Interpreters](https://docs.langchain.com/oss/python/deepagents/interpreters).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#streaming) Streaming


[Event streaming](https://docs.langchain.com/oss/python/deepagents/event-streaming) exposes agent runs as typed projections for messages, tool calls, values, and output. Deep Agents add `stream.subagents` so each delegated task gets its own handle with independent message, tool-call, and nested subagent streams.


## [​](https://docs.langchain.com/oss/python/deepagents/overview#context-management) Context management


The context management component controls what the agent knows, how long it can operate within token limits, and what it retains across sessions. It has four layers:


- **[Skills](https://docs.langchain.com/oss/python/deepagents/overview#skills)**: on-demand domain knowledge loaded progressively from skill files
- **[Memory](https://docs.langchain.com/oss/python/deepagents/overview#memory)**: persistent instructions and preferences loaded at startup from `AGENTS.md` files
- **[Summarization and context offloading](https://docs.langchain.com/oss/python/deepagents/overview#summarization-and-context-offloading)**: automatic compression of conversation history and large tool results
- **[Prompt caching](https://docs.langchain.com/oss/python/deepagents/overview#prompt-caching)**: static prompt sections are cache-eligible to speed up inference and reduce cost on supported models


### [​](https://docs.langchain.com/oss/python/deepagents/overview#skills) Skills


Skills package specialized workflows, domain knowledge, and custom instructions for your deep agent.
Each skill follows the [Agent Skills standard](https://agentskills.io/) and lives in a directory with a `SKILL.md` file. Skills can also include scripts, templates, reference docs, and other supporting resources.
Deep Agents load skills with progressive disclosure: the agent reads `SKILL.md` frontmatter at startup, then reads full skill content only when a task needs it. This keeps startup context compact while still making rich capabilities available on demand.
For more information, see [Skills](https://docs.langchain.com/oss/python/deepagents/skills).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#memory) Memory


Memory gives your deep agent persistent context across conversations, such as coding style, preferences, conventions, and project guidelines.
Memory uses [`AGENTS.md` files](https://agents.md/) that you pass through the `memory` parameter when creating the agent. Unlike skills, memory files are always loaded, and the content is stored in the configured backend (`StateBackend`, `StoreBackend`, or `FilesystemBackend`).
The agent can also update memory based on interactions and feedback, so preferences and patterns can carry forward without needing to restate them in each thread.
For configuration details and examples, see [Memory](https://docs.langchain.com/oss/python/deepagents/customization#memory). To generate a repository wiki that coding agents discover through `AGENTS.md`, see [OpenWiki](https://docs.langchain.com/oss/openwiki/overview).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#summarization-and-context-offloading) Summarization and context offloading


The harness manages context so deep agents can handle long-running work within token limits while keeping the most relevant information in scope.
This context flow has four parts:


- **Input context**: System prompt, memory, skills, and tool prompts define what the agent starts with.
- **Compression**: Built-in offloading and summarization compress conversation history and large intermediate results.
- **Isolation**: Subagents quarantine heavy subtasks and return only final results (see [Delegation](https://docs.langchain.com/oss/python/deepagents/overview#delegation)).
- **Long-term memory**: Persistent storage in the virtual filesystem carries information across threads.


Together, these mechanisms support multi-step tasks that exceed a single context window while reducing manual context trimming and token usage.
For configuration details, see [Context engineering](https://docs.langchain.com/oss/python/deepagents/context-engineering). For multimodal inputs and tool outputs, see [Multimodal](https://docs.langchain.com/oss/python/deepagents/multimodal).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#prompt-caching) Prompt caching


For Anthropic and Amazon Bedrock models, `create_deep_agent` automatically applies prompt caching to static sections of the system prompt—the base agent instructions, memory, and skill content that repeat on every turn. This avoids reprocessing the same tokens across calls, reducing both latency and cost on long-running agents.
Prompt caching is enabled by default when using an Anthropic model, or a Bedrock model (Claude or Nova). No configuration is required.
For other providers, see [Middleware integrations](https://docs.langchain.com/oss/python/integrations/middleware) for available provider-specific caching middleware.


## [​](https://docs.langchain.com/oss/python/deepagents/overview#delegation) Delegation


The delegation component enables agents to break large problems into smaller, parallelizable units of work. It has two layers:


- **[Task planning](https://docs.langchain.com/oss/python/deepagents/overview#task-planning)**: an opt-in `write_todos` tool for structured task tracking
- **[Subagents](https://docs.langchain.com/oss/python/deepagents/overview#subagents)**: ephemeral child agents that handle isolated subtasks


### [​](https://docs.langchain.com/oss/python/deepagents/overview#task-planning) Task planning


Task planning is an opt-in harness capability that lets agents maintain a structured task list during execution.
Starting in v0.7 task planning is opt-in only. In earlier versions, task planning middleware was included by default.
Planning is often useful for:


- Long or complicated multi-step tasks
- Less capable models that benefit from an explicit accountability tool
- UIs that stream progress from agent state (see [Todo list](https://docs.langchain.com/oss/python/deepagents/frontend/todo-list))


Pass [`TodoListMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware) to the middleware parameter to give the agent a `write_todos` tool for maintaining a structured task list during execution.
Google OpenAI Anthropic OpenRouter Fireworks Baseten Ollama

```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="openrouter:z-ai/glm-5.2",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="baseten:zai-org/GLM-5.2",
    middleware=[TodoListMiddleware()],
)
```


```
from deepagents import create_deep_agent
from langchain.agents.middleware import TodoListMiddleware

agent = create_deep_agent(
    model="ollama:north-mini-code-1.0",
    middleware=[TodoListMiddleware()],
)
```


Tasks support status tracking (`'pending'`, `'in_progress'`, `'completed'`) and are persisted in agent state. This gives agents a lightweight planning layer for organizing long-running and multi-step work.
For configuration options and behavior details, see [To-do list](https://docs.langchain.com/oss/python/langchain/middleware/built-in#to-do-list).


### [​](https://docs.langchain.com/oss/python/deepagents/overview#subagents) Subagents


The harness includes a built-in `task` tool that lets the main agent create ephemeral subagents for isolated, long-running, multi-step, or parallel tasks.
Two subagent types are available: synchronous subagents (the default) block the supervisor until they return a single report, and [async subagents](https://docs.langchain.com/oss/python/deepagents/async-subagents) run in parallel and support mid-flight steering via launch, check, update, and cancel tools.
Subagent execution provides:


- **Isolated or inherited context**: By default, each invocation creates a new agent instance with its own context (`mode: "isolated"`). Use `mode: "fork"` to inherit the parent’s full conversation history instead. See [Forked subagents](https://docs.langchain.com/oss/python/deepagents/subagents#forked-subagents).
- **Autonomous execution**: The subagent runs independently until completion.
- **Single handoff**: It returns one final report to the main agent.
- **Configurable strategy**: Use the [default `general-purpose` subagent](https://docs.langchain.com/oss/python/deepagents/subagents#default-subagent) (enabled by default) or define [custom subagents](https://docs.langchain.com/oss/python/deepagents/subagents#custom-subagents).
- **Stateless messaging**: Subagents are stateless and cannot send multiple messages back.
- **Context and token efficiency**: Heavy subtask work stays isolated and is compressed into a compact result.


For more information, see [Subagents](https://docs.langchain.com/oss/python/deepagents/subagents). To remove the `task` tool, see [Running without subagents](https://docs.langchain.com/oss/python/deepagents/subagents#running-without-subagents).


## [​](https://docs.langchain.com/oss/python/deepagents/overview#steering) Steering


The steering component gives humans control over agent behavior at runtime and sets filesystem permissions for agent work.


### [​](https://docs.langchain.com/oss/python/deepagents/overview#human-in-the-loop) Human-in-the-loop


Deep Agents integrate with LangGraph interrupts so you can pause for approval on sensitive tool calls. Enable this behavior with the `interrupt_on` parameter in `create_deep_agent`.
`interrupt_on` accepts a mapping of tool names to interrupt configurations. For example, `interrupt_on={"edit_file": True}` pauses before every edit, letting you approve the call, add guidance, or modify tool inputs before execution.
This gives you a runtime safety and control layer for destructive operations, expensive API calls, and interactive debugging.
For more information, see [Human-in-the-loop](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop).


## [​](https://docs.langchain.com/oss/python/deepagents/overview#get-started) Get started


## Quickstart

Build your first deep agent

## Customization

Learn about customization options

## Code

Use Deep Agents Code

## ACP

Use deep agents in code editors with ACP

## Reference

See the `deepagents` API reference


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Mistral applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-mistral`

# Trace Mistral applications

[Mistral](https://mistral.ai/) provides hosted access to open-weight language models via a simple API.
This guide shows you how to trace Mistral API calls with LangSmith, allowing you to record prompts, responses, and metadata for debugging and observability. Traces are sent directly to LangSmith using the [LangSmith SDK](https://reference.langchain.com/python/langsmith/) and standard span instrumentation.


## [​](https://docs.langchain.com/langsmith/trace-with-mistral#installation) Installation


Install Mistral’s official library and LangSmith:
Python JavaScript

```
pip install mistralai langsmith
```


```
npm install @mistralai/mistralai langsmith dotenv
```


[`mistralai`](https://docs.mistral.ai/getting-started/clients) provides a Mistral client for interacting with Mistral’s API.


## [​](https://docs.langchain.com/langsmith/trace-with-mistral#setup) Setup


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export MISTRAL_API_KEY="<your_mistral_api_key>"
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<your_langsmith_api_key>"
export LANGSMITH_PROJECT="<your_project_name>"  # optional
```


- Ensure you have a Mistral API key from your [Mistral AI account](https://v2.auth.mistral.ai/login) (set this as `MISTRAL_API_KEY`).
- Set `LANGSMITH_TRACING=true` and provide your LangSmith API key (`LANGSMITH_API_KEY`) activates automatic logging of traces.
- Specify a [`LANGSMITH_PROJECT`](https://docs.langchain.com/langsmith/log-traces-to-project) name to organize traces by project; if not set, traces go to the default project (named “default”).
- The `LANGSMITH_TRACING` flag must be true for any traces to be recorded.


## [​](https://docs.langchain.com/langsmith/trace-with-mistral#configure-tracing) Configure tracing


1. Instrument the Mistral API call with LangSmith. In your script, create a Mistral client and wrap a call in a traced function: Python TypeScript ``` import os from mistralai import Mistral from langsmith import traceable # Initialize Mistral API client with your API key client = Mistral(api_key=os.environ["MISTRAL_API_KEY"]) @traceable( run_type="llm", metadata={"ls_provider": "mistral", "ls_model_name": "mistral-medium-latest"}, ) def query_mistral(prompt: str): response = client.chat.complete( model="mistral-medium-latest", messages=[{"role": "user", "content": prompt}], ) return response.choices[0].message # Example usage result = query_mistral("Hello, how are you?") print("Mistral response:", result.content) ``` ``` import { Client } from "langsmith"; import { traceable } from "langsmith/traceable"; import { Mistral } from "@mistralai/mistralai"; import "dotenv/config"; const mistral = new Mistral({ apiKey: process.env.MISTRAL_API_KEY, }); const langsmith = new Client(); const tracedChatCompletion = traceable( async (params: { model: string; messages: Array<{ role: string; content: string }>; }) => { const response = await mistral.chat.complete(params); // Return the message content so LangSmith captures it correctly return response.choices[0].message.content; }, { name: "Mistral Chat Completion", run_type: "llm", metadata: { ls_provider: "mistral", ls_model_name: "mistral-small-latest", }, } ); async function main() { const response = await tracedChatCompletion({ model: "mistral-small-latest", messages: [ { role: "user", content: "Say hello in one short sentence." }, ], }); console.log(response); } main(); ``` In this example, you use the [Mistral SDK](https://docs.mistral.ai/getting-started/clients) to send a chat completion request (with a user prompt) and retrieve the model’s answer. The [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) decorator (from the [LangSmith Python SDK](https://reference.langchain.com/python/langsmith/observability/sdk/)) wraps the `query_mistral` function so that each invocation is logged as a trace run of type `"llm"`. The `metadata={"ls_provider": "mistral", "ls_model_name": "mistral-medium-latest"}` tags the trace with the provider (Mistral) and model name. You can also refer to the [LangSmith JavaScript SDK](https://reference.langchain.com/javascript/modules/langsmith.html).
2. Execute your script to generate a trace. For example: Python JavaScript ``` python mistral_trace.py ``` ``` node index.js ``` The `query_mistral("Hello, how are you?")` call will reach out to the Mistral API, and because of the `@traceable` / `traceable` wrapper, LangSmith will log this call’s inputs and outputs as a new trace. You’ll find the model’s response printed to the console, and a corresponding run appear in [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-mistral).


## [​](https://docs.langchain.com/langsmith/trace-with-mistral#view-traces-in-langsmith) View traces in LangSmith


After running the example, you can inspect the recorded traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-mistral):


1. Open the LangSmith UI and log in to your account.
2. Select the project you used for this integration (for example, the name set in `LANGSMITH_PROJECT`, or default if you didn’t set one).
3. Find the trace corresponding to your Mistral API call. It will be identified by the function name (`query_mistral`) or a custom name if provided.
4. Click on the trace to open it. You’ll be able to inspect the model input and output, including the prompt messages you sent and the response from Mistral, as well as timing information (latency) and any error details if the call failed.


With LangSmith’s tracing, you have full visibility into your Mistral calls—allowing you to debug the behavior of Mistral’s models, monitor performance (e.g., response time and token usage), and compare runs with different parameters using the metadata tags.


## [​](https://docs.langchain.com/langsmith/trace-with-mistral#cost-tracking) Cost tracking


Although Mistral models are open-weight, using the hosted Mistral API may incur usage-based costs depending on your plan.
LangSmith can automatically associate costs with traced LLM calls by estimating token usage and applying model-specific pricing. When tracing Mistral API calls, LangSmith uses the recorded prompt and response messages to calculate token counts and attach cost information to each run.
To enable automatic cost tracking for LLM calls, refer to [Automatically track costs based on token counts](https://docs.langchain.com/langsmith/cost-tracking#llm-calls:-automatically-track-costs-based-on-token-counts).
Once enabled, costs appear directly in the LangSmith UI alongside each traced Mistral run, so that you can monitor usage and compare experiments over time.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-mistral.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure tracing
## ​View traces in LangSmith
## ​Cost tracking







Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace AutoGen applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-autogen`

# Trace AutoGen applications

LangSmith can capture traces generated by [AutoGen](https://microsoft.github.io/autogen/stable/) using OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your AutoGen multi-agent conversations and send them to LangSmith for monitoring and analysis.


## [​](https://docs.langchain.com/langsmith/trace-with-autogen#installation) Installation


Install the required packages using your preferred package manager:
pip uv

```
pip install langsmith autogen-agentchat autogen-ext opentelemetry-instrumentation-openai
```


```
uv add langsmith autogen-agentchat autogen-ext opentelemetry-instrumentation-openai
```


## [​](https://docs.langchain.com/langsmith/trace-with-autogen#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-autogen#1-configure-environment-variables) 1. Configure environment variables


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```


### [​](https://docs.langchain.com/langsmith/trace-with-autogen#2-configure-opentelemetry-integration) 2. Configure OpenTelemetry integration


In your AutoGen application, configure the LangSmith OpenTelemetry integration along with the OpenAI instrumentor:


```
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Set up tracer provider
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(OtelSpanProcessor())
trace.set_tracer_provider(tracer_provider)

# Instrument OpenAI calls
OpenAIInstrumentor().instrument()
```


### [​](https://docs.langchain.com/langsmith/trace-with-autogen#3-create-and-run-your-autogen-application) 3. Create and run your AutoGen application


Once configured, your AutoGen application will automatically send traces to LangSmith. Pass the tracer provider to the runtime for full tracing coverage:


```
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_core import SingleThreadedAgentRuntime
from autogen_ext.models.openai import OpenAIChatCompletionClient
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Set up tracing
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(OtelSpanProcessor())
trace.set_tracer_provider(tracer_provider)
OpenAIInstrumentor().instrument()

# Define a tool
def percentage_change(start: float, end: float) -> float:
    """Calculate percentage change between two values."""
    if start == 0:
        return float("inf")
    return ((end - start) / start) * 100

async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-6-luna")
    tracer = trace.get_tracer("autogen-demo")

    with tracer.start_as_current_span("run_team"):
        planning_agent = AssistantAgent(
            "PlanningAgent",
            description="Plans tasks and delegates.",
            model_client=model_client,
            system_message=(
                "You are a planning agent. Plan and delegate tasks.\n"
                "When assigning tasks, use: 1. <agent> : <task>\n"
                'After tasks complete, summarize and end with "TERMINATE".'
            ),
        )

        data_analyst = AssistantAgent(
            "DataAnalystAgent",
            description="Performs calculations.",
            model_client=model_client,
            tools=[percentage_change],
            system_message="You are a data analyst. Use tools to compute results.",
        )

        termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(max_messages=25)

        # Pass tracer_provider to the runtime
        runtime = SingleThreadedAgentRuntime(tracer_provider=trace.get_tracer_provider())
        runtime.start()

        team = SelectorGroupChat(
            [planning_agent, data_analyst],
            model_client=model_client,
            termination_condition=termination,
            allow_repeated_speaker=True,
            runtime=runtime,
        )

        task = "You started with 100 apples, now you have 120 apples. What is the percentage change?"
        await Console(team.run_stream(task=task))

        await runtime.stop()

    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
```


## [​](https://docs.langchain.com/langsmith/trace-with-autogen#advanced-usage) Advanced usage


### [​](https://docs.langchain.com/langsmith/trace-with-autogen#custom-metadata-and-tags) Custom metadata and tags


You can add custom metadata to your traces by setting span attributes:


```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

async def run_with_metadata():
    with tracer.start_as_current_span("autogen_workflow") as span:
        span.set_attribute("langsmith.metadata.session_type", "multi_agent")
        span.set_attribute("langsmith.metadata.agent_count", "2")
        span.set_attribute("langsmith.span.tags", "autogen,planning")

        # Your AutoGen code here
        await Console(team.run_stream(task=task))
```


### [​](https://docs.langchain.com/langsmith/trace-with-autogen#combining-with-other-instrumentors) Combining with other instrumentors


You can combine AutoGen tracing with other OpenTelemetry instrumentors:


```
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

# Initialize multiple instrumentors
OpenAIInstrumentor().instrument()
HTTPXClientInstrumentor().instrument()
```


## [​](https://docs.langchain.com/langsmith/trace-with-autogen#resources) Resources


- [AutoGen documentation](https://microsoft.github.io/autogen/stable/)
- [LangSmith OpenTelemetry guide](https://docs.langchain.com/langsmith/trace-with-opentelemetry)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-autogen.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Advanced usage
## ​Resources






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenAI applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-openai`

# Trace OpenAI applications

The [`wrap_openai`](https://reference.langchain.com/python/langsmith/wrappers/_openai/wrap_openai) / [`wrapOpenAI`](https://reference.langchain.com/javascript/langsmith/wrappers/wrapOpenAI) methods in Python/TypeScript allow you to wrap your OpenAI client in order to automatically log traces — no decorator or function wrapping required! Using the wrapper ensures that messages, including tool calls and multimodal content blocks will be rendered nicely in LangSmith. Also note that the wrapper works seamlessly with the [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) decorator or [`traceable`](https://reference.langchain.com/javascript/langsmith/traceable/traceable) function and you can use both in the same application.
The `LANGSMITH_TRACING` environment variable must be set to `'true'` in order for traces to be logged to LangSmith, even when using [`wrap_openai`](https://reference.langchain.com/python/langsmith/wrappers/_openai/wrap_openai) or [`wrapOpenAI`](https://reference.langchain.com/javascript/langsmith/wrappers/wrapOpenAI). This allows you to toggle tracing on and off without changing your code. Additionally, you will need to set the `LANGSMITH_API_KEY` environment variable to your API key (see [Setup](https://docs.langchain.com/) for more information). If your LangSmith API key is linked to multiple workspaces, set the `LANGSMITH_WORKSPACE_ID` environment variable to specify which workspace to use. By default, the traces will be logged to a project named `default`. To log traces to a different project, see [Log traces to a specific project](https://docs.langchain.com/langsmith/log-traces-to-project).
Python TypeScript

```
import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())

@traceable(run_type="tool", name="Retrieve Context")
def my_tool(question: str) -> str:
  return "During this morning's meeting, we solved all world conflict."

@traceable(name="Chat Pipeline")
def chat_pipeline(question: str):
  context = my_tool(question)
  messages = [
      { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },
      { "role": "user", "content": f"Question: {question}\nContext: {context}"}
  ]
  chat_completion = client.chat.completions.create(
      model="gpt-5.5", messages=messages
  )
  return chat_completion.choices[0].message.content

chat_pipeline("Can you summarize this morning's meetings?")
```


```
import OpenAI from "openai";
import { traceable } from "langsmith/traceable";
import { wrapOpenAI } from "langsmith/wrappers";

const client = wrapOpenAI(new OpenAI());

const myTool = traceable(async (question: string) => {
  return "During this morning's meeting, we solved all world conflict.";
}, { name: "Retrieve Context", run_type: "tool" });

const chatPipeline = traceable(async (question: string) => {
  const context = await myTool(question);
  const messages = [
      {
          role: "system",
          content:
              "You are a helpful assistant. Please respond to the user's request only based on the given context.",
      },
      { role: "user", content: `Question: ${question} Context: ${context}` },
  ];
  const chatCompletion = await client.chat.completions.create({
      model: "gpt-5.5",
      messages: messages,
  });
  return chatCompletion.choices[0].message.content;
}, { name: "Chat Pipeline" });

await chatPipeline("Can you summarize this morning's meetings?");
```


To trace a provider with an OpenAI-compatible API, refer to [Trace OpenAI-compatible providers](https://docs.langchain.com/langsmith/trace-with-openai-compatible).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index


Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Claude Agent SDK applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-claude-agent-sdk`

# Trace Claude Agent SDK applications

The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) is an SDK for building agentic applications with Claude. LangSmith provides native integration with the Claude Agent SDK to automatically trace your agent executions, tool calls, and interactions with Claude models.


## [​](https://docs.langchain.com/langsmith/trace-claude-agent-sdk#installation) Installation


Install the LangSmith integration for Claude Agent SDK
uv pip pnpm npm

```
uv add "langsmith[claude-agent-sdk]"
```


```
pip install langsmith[claude-agent-sdk]
```


```
pnpm add @anthropic-ai/claude-agent-sdk langsmith zod
```


```
npm install @anthropic-ai/claude-agent-sdk langsmith zod
```


## [​](https://docs.langchain.com/langsmith/trace-claude-agent-sdk#setup) Setup


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key):
shell.env

```
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_langsmith_project>

export ANTHROPIC_API_KEY=<your_anthropic_api_key>
```


```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your_langsmith_api_key>
LANGSMITH_PROJECT=<your_langsmith_project>

ANTHROPIC_API_KEY=<your_anthropic_api_key>
```


You can find your LangSmith API key and project name in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-claude-agent-sdk) under **Settings**.
For an Anthropic API key, refer to the [Claude console](https://console.anthropic.com/settings/keys).


## [​](https://docs.langchain.com/langsmith/trace-claude-agent-sdk#quickstart) Quickstart


To enable LangSmith tracing for your Claude Agent SDK application, call `configure_claude_agent_sdk()` at the start of your application:
Python TypeScript

```
import asyncio
from typing import Any

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)
from langsmith.integrations.claude_agent_sdk import configure_claude_agent_sdk

configure_claude_agent_sdk()


@tool(
    "get_weather",
    "Gets the current weather for a given city",
    {"city": str},
)
async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
    city = args["city"]
    weather_data = {
        "San Francisco": "Foggy, 62°F",
        "New York": "Sunny, 75°F",
        "London": "Rainy, 55°F",
        "Tokyo": "Clear, 68°F",
    }
    weather = weather_data.get(city, "Weather data not available")
    return {"content": [{"type": "text", "text": f"Weather in {city}: {weather}"}]}


async def main() -> None:
    weather_server = create_sdk_mcp_server(
        name="weather",
        version="1.0.0",
        tools=[get_weather],
    )

    options = ClaudeAgentOptions(
        model="claude-sonnet-5-5",
        system_prompt="You are a friendly travel assistant who helps with weather information.",
        mcp_servers={"weather": weather_server},
        allowed_tools=["mcp__weather__get_weather"],
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("What's the weather like in San Francisco and Tokyo?")

        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
```


```
import * as originalSdk from '@anthropic-ai/claude-agent-sdk';

import { wrapClaudeAgentSDK } from 'langsmith/experimental/anthropic';
import { z } from 'zod/v4';

const sdk = wrapClaudeAgentSDK(originalSdk);

const getWeather = sdk.tool(
  'get_weather',
  'Gets the current weather for a given city',
  {
    city: z.string(),
  },
  async ({ city }) => {
    const weatherData: Record<string, string> = {
      'San Francisco': 'Foggy, 62°F',
      'New York': 'Sunny, 75°F',
      London: 'Rainy, 55°F',
      Tokyo: 'Clear, 68°F',
    };
    const weather = weatherData[city] ?? 'Weather data not available';
    return {
      content: [{ type: 'text' as const, text: weather }],
    };
  }
);

const weatherServer = sdk.createSdkMcpServer({
  name: 'weather',
  version: '1.0.0',
  tools: [getWeather],
});

const query = sdk.query({
  prompt: "What's the weather like in San Francisco and Tokyo?",
  options: {
    model: 'claude-sonnet-5-5',
    systemPrompt:
      'You are a friendly travel assistant who helps with weather information.',
    mcpServers: { weather: weatherServer },
    allowedTools: ['mcp__weather__get_weather'],
  },
});

for await (const chunk of query) {
  console.log(chunk);
}
```


Once configured, all Claude Agent SDK operations will be automatically traced to LangSmith, including:


- Agent queries and responses
- Tool invocations and results
- Claude model interactions
- MCP server operations


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-agent-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Quickstart





Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenAI-compatible providers - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-openai-compatible`

# Trace OpenAI-compatible providers
## Documentation Index
## ​Setup
## ​Trace API calls
## ​Add metadata
## ​Related guides






Trace LLM calls from any OpenAI-compatible provider to LangSmith.

Many LLM providers accept requests in the same format as the OpenAI API. To trace calls from these providers to LangSmith, construct an OpenAI client pointed at the provider’s base URL, then wrap it with [`wrap_openai`](https://reference.langchain.com/python/langsmith/wrappers/_openai/wrap_openai) / [`wrapOpenAI`](https://reference.langchain.com/javascript/modules/langsmith.html).
Use `wrap_openai` / `wrapOpenAI` for direct API calls. Use [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) when you need to trace application logic around the call or set metadata per invocation.


|  | `wrap_openai` / `wrapOpenAI` | `@traceable` / `traceable` |
| --- | --- | --- |
| Token tracking | Automatic | Requires `run_type="llm"` |
| Run type | LLM (set automatically) | Chain by default |
| Traces | The API call | The function wrapping it |
| Metadata | Client-level only (Python); client-level or per-call (TypeScript) | Per-call via [`langsmith_extra`](https://reference.langchain.com/python/langsmith/run_helpers/SupportsLangsmithExtra) |


To trace OpenAI directly, refer to [Trace OpenAI applications](https://docs.langchain.com/langsmith/trace-openai).


## [​](https://docs.langchain.com/langsmith/trace-with-openai-compatible#setup) Setup


Python npm

```
pip install langsmith openai
```


```
npm install langsmith openai
```


```
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_TRACING=true
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-compatible#trace-api-calls) Trace API calls


Python TypeScript

```
import os

import openai
from langsmith import wrappers

client = wrappers.wrap_openai(
    openai.OpenAI(
        base_url="https://<provider-base-url>/v1",
        api_key=os.environ["PROVIDER_API_KEY"],
    )
)

completion = client.chat.completions.create(
    model="<provider-model-name>",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(completion.choices[0].message.content)
```


```
import OpenAI from "openai";
import { wrapOpenAI } from "langsmith/wrappers/openai";

const client = wrapOpenAI(
  new OpenAI({
    baseURL: "https://<provider-base-url>/v1",
    apiKey: process.env.PROVIDER_API_KEY!,
  })
);

const completion = await client.chat.completions.create({
  model: "<provider-model-name>",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(completion.choices[0].message.content);
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-compatible#add-metadata) Add metadata


- Python
- TypeScript

Pass `tracing_extra` when wrapping the client. The metadata applies to all calls made with that client.

```
import os

import openai

from langsmith import wrappers

client = wrappers.wrap_openai(
    openai.OpenAI(
        base_url="https://<provider-base-url>/v1",
        api_key=os.environ["PROVIDER_API_KEY"],
    ),
    tracing_extra={"metadata": {"environment": "production"}},
)
```

Pass options as the second argument to `wrapOpenAI` for client-level metadata, or pass [`langsmithExtra`](https://reference.langchain.com/javascript/modules/langsmith.html) per call.

```
import OpenAI from "openai";
import { wrapOpenAI } from "langsmith/wrappers/openai";

const client = wrapOpenAI(
  new OpenAI({
    baseURL: "https://<provider-base-url>/v1",
    apiKey: process.env.PROVIDER_API_KEY!,
  }),
  { metadata: { environment: "production" } }
);

// Per-call metadata
const completion = await client.chat.completions.create(
  {
    model: "<provider-model-name>",
    messages: [{ role: "user", content: "Hello!" }],
  },
  { langsmithExtra: { metadata: { request_id: "abc123" } } }
);
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-compatible#related-guides) Related guides


Some providers have dedicated setup guides that use `@traceable` or a native callback. These approaches trace at the function level rather than wrapping the client directly, or integrate with the provider’s own SDK and routing layer.


- [DeepSeek](https://docs.langchain.com/langsmith/trace-deepseek): OpenAI-compatible API; guide uses `@traceable` with custom provider metadata
- [LiteLLM](https://docs.langchain.com/langsmith/trace-litellm): proxy that exposes an OpenAI-compatible endpoint; guide covers `@traceable` and LiteLLM’s built-in LangSmith callback


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-openai-compatible.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Deep Agents applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-deep-agents`

# Trace Deep Agents applications

[`deepagents`](https://docs.langchain.com/oss/python/deepagents/overview) is an open-source agent framework built on top of LangGraph, designed for complex, multi-step tasks that require planning, tool usage, and sub-agent delegation. Deep Agents supports native LangSmith tracing.
This guide shows you how to enable LangSmith tracing for Deep Agents, view traces in the LangSmith UI, and (optionally) customize trace configuration for more advanced use cases.


## [​](https://docs.langchain.com/langsmith/trace-deep-agents#installation) Installation


Install `deepagents` in your Python environment:
pip uv

```
pip install deepagents
```


```
uv add deepagents
```


`deepagents` requires:


- Python 3.11+.
- An LLM that supports tool calling (for example, OpenAI or Anthropic models).
- For tracing, a [LangSmith account and API key](https://docs.langchain.com/langsmith/create-account-api-key) (free to sign up).


You do not need to install the `langsmith` Python package to trace Deep Agents. `deepagents` is built on LangGraph, which includes native LangSmith tracing support. As long as the LangSmith environment variables are set, traces are sent automatically. The `langsmith` package is only required if you want [programmatic control over tracing](https://docs.langchain.com/langsmith/trace-deep-agents#customize-langsmith-tracing) (for example, using `tracing_context`, adding custom metadata, or querying runs from Python).


## [​](https://docs.langchain.com/langsmith/trace-deep-agents#setup) Setup


You can find your LangSmith API key and project name in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deep-agents) under **Settings**:


```
export LANGSMITH_API_KEY=<your-langsmith-api-key>
export LANGSMITH_TRACING=true
export LANGSMITH_PROJECT=<your-project-name>
```


## [​](https://docs.langchain.com/langsmith/trace-deep-agents#create-a-trace) Create a trace


Once tracing is enabled via environment variables, Deep Agents will automatically emit traces to LangSmith. For example:


```
from typing import Dict, Any, List

from deepagents import create_deep_agent


def compute_compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> Dict[str, Any]:
    """Compute compound interest and return ending balance and interest earned."""
    r = annual_rate
    n = compounds_per_year
    t = years
    amount = principal * (1 + r / n) ** (n * t)
    interest = amount - principal
    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "compounds_per_year": n,
        "ending_balance": round(amount, 2),
        "interest_earned": round(interest, 2),
    }


def yearly_balance_schedule(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> List[Dict[str, Any]]:
    """Return a year-by-year balance schedule for the investment."""
    r = annual_rate
    n = compounds_per_year
    schedule: List[Dict[str, Any]] = []

    for year in range(1, years + 1):
        amount = principal * (1 + r / n) ** (n * year)
        schedule.append(
            {
                "year": year,
                "ending_balance": round(amount, 2),
                "interest_earned": round(amount - principal, 2),
            }
        )

    return schedule


agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[compute_compound_interest, yearly_balance_schedule],
    system_prompt=(
        "You are a careful assistant. "
        "Use tools for calculations and structured outputs. "
        "Return a concise final answer."
    ),
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "I have $2,500 invested at 6% annual interest compounded monthly for 5 years.\n"
                    "1) Compute the ending balance and total interest earned.\n"
                    "2) Generate a year-by-year ending balance schedule.\n"
                    "Then summarize the key takeaways in 3 bullets.\n\n"
                    "Use compounds_per_year=12."
                ),
            }
        ]
    }
)

print(result)
```


## [​](https://docs.langchain.com/langsmith/trace-deep-agents#viewing-traces) Viewing traces


### [​](https://docs.langchain.com/langsmith/trace-deep-agents#details-view) Details View


Click on the trace, and toggle to the **Details** view on the top right. Your trace tree in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deep-agents) will look like [this](https://smith.langchain.com/public/ec82be64-b158-425e-a959-924be16b8588/r), with the following structure:


- Agent run (top level) representing the full Deep Agents invocation.
- LLM call where the agent analyzes the user request and decides which tools to use.
- Tool run: `compute_compound_interest`:
  - Displays the tool inputs (for example, principal, annual_rate, years, and compounds_per_year).
  - Displays the structured output, including the ending balance and total interest earned.- LLM call that interprets the calculation results and determines the next step.
- Tool run: `yearly_balance_schedule`:
  - Shows the inputs used to generate the schedule.
  - Returns a year-by-year breakdown of ending balances and interest earned.- Final LLM response that summarizes the results for the user.


The resulting trace contains multiple nested spans, which allows you to follow the agent’s planning, calculation steps, and interpretation flow in the LangSmith UI.


### [​](https://docs.langchain.com/langsmith/trace-deep-agents#trajectory-view) Trajectory view


The **Trajectory** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace, (including the user’s initial request, tool calls and the agent’s final response) and represents them in a chat-like format.


### [​](https://docs.langchain.com/langsmith/trace-deep-agents#filter-by-subagent) Filter by subagent


Deep Agents automatically writes the subagent’s `name` to the `lc_agent_name` metadata key on every run that subagent produces. Use this to isolate all runs from a specific subagent in LangSmith—useful for debugging, monitoring, or comparing subagent behavior.
**Filter in the LangSmith UI:**


1. Open your tracing project in [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deep-agents).
2. Switch the view to **Runs** to see individual spans.
3. Click **Add filter** and select **Metadata**.
4. Set the **Key** to `lc_agent_name` and the **Value** to the subagent name, for example `coordinator`.


![LangSmith Runs view with a metadata filter on lc_agent_name set to coordinator](https://mintcdn.com/langchain-5e9cc07a/t_yuR4Fo_XGdcWGH/langsmith/images/deepagents-lc-agent-name-filter.png?fit=max&auto=format&n=t_yuR4Fo_XGdcWGH&q=85&s=ffc65c0b9b5292fce5f0589b8f2478ce)
Save the filter as a named view for quick reuse. For a full reference on filter options, see [Filter traces](https://docs.langchain.com/langsmith/filter-traces).
**Filter programmatically with the SDK:**


```
from langsmith import Client

client = Client()

# Fetch all runs produced by a specific subagent
runs = client.list_runs(
    project_name="<your-project>",
    filter='has(metadata, \'{"lc_agent_name": "research-agent"}\')',
)

for run in runs:
    print(run.name, run.start_time, run.status)
```


For the full filter query language reference, see [Trace query syntax](https://docs.langchain.com/langsmith/trace-query-syntax).


## [​](https://docs.langchain.com/langsmith/trace-deep-agents#customize-langsmith-tracing) Customize LangSmith tracing


By default, Deep Agents traces are emitted automatically when LangSmith tracing is enabled via environment variables. You can use the [LangSmith SDK](https://reference.langchain.com/python/langsmith/observability/sdk/) directly to customize your tracing, such as scoping traces to part of your code, attaching tags or metadata, or overriding the project name.
Install and use `langsmith` if you want to:


- Trace only specific agent invocations.
- Add custom tags or metadata for filtering in the UI.
- Override the project name at runtime.


pip uv

```
pip install langsmith
```


```
uv add langsmith
```


This example invokes the same deep agent twice:


- The first invocation is untraced, because it runs outside of `tracing_context`.
- The second invocation is traced, because it runs inside `tracing_context(enabled=True, ...)`.


You can selectively trace only part of your workflow, without enabling global tracing for your entire process with `LANGSMITH_TRACING=true`:


```
from typing import Dict, Any, List

import langsmith as ls
from deepagents import create_deep_agent


def compute_compound_interest(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> Dict[str, Any]:
    """Compute compound interest and return ending balance and interest earned."""
    r = annual_rate
    n = compounds_per_year
    t = years
    amount = principal * (1 + r / n) ** (n * t)
    interest = amount - principal
    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "compounds_per_year": n,
        "ending_balance": round(amount, 2),
        "interest_earned": round(interest, 2),
    }


def yearly_balance_schedule(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int,
) -> List[Dict[str, Any]]:
    """Return a year-by-year balance schedule for the investment."""
    r = annual_rate
    n = compounds_per_year
    schedule: List[Dict[str, Any]] = []

    for year in range(1, years + 1):
        amount = principal * (1 + r / n) ** (n * year)
        schedule.append(
            {
                "year": year,
                "ending_balance": round(amount, 2),
                "interest_earned": round(amount - principal, 2),
            }
        )

    return schedule


agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[compute_compound_interest, yearly_balance_schedule],
    system_prompt=(
        "You are a careful assistant. "
        "Use tools for calculations and structured outputs. "
        "Return a concise final answer."
    ),
)

# ----------------------------
# Untraced invocation
# ----------------------------
agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "I have $2,500 invested at 6% annual interest compounded monthly for 5 years. "
                    "Compute the ending balance and total interest earned. "
                    "Use compounds_per_year=12."
                ),
            }
        ]
    }
)

# ----------------------------
# Traced invocation
# ----------------------------
with ls.tracing_context(
    enabled=True,
    project_name="deepagents-demo",
    tags=["deepagents", "scoped-tracing"],
    metadata={"example": "partial-workflow"},
):
    agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "I have $2,500 invested at 6% annual interest compounded monthly for 5 years.\n"
                        "1) Compute the ending balance and total interest earned.\n"
                        "2) Generate a year-by-year ending balance schedule.\n"
                        "Then summarize the key takeaways in 3 bullets.\n\n"
                        "Use compounds_per_year=12."
                    ),
                }
            ]
        }
    )
```


The `tracing_context` block enables tracing and also configures how the trace is recorded and organized in LangSmith:


- `enabled=True` explicitly enables tracing for the duration of the block, even if `LANGSMITH_TRACING` is unset or set to `false`.
- `project_name="deepagents-demo"` routes traces from this block to the specified [LangSmith project](https://docs.langchain.com/langsmith/log-traces-to-project). This overrides `LANGSMITH_PROJECT` for runs created within the context.
- `tags=[...]` attaches tags to the traced runs. [Tags](https://docs.langchain.com/langsmith/add-metadata-tags) appear in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-deep-agents), which you can use to filter and group traces.
- `metadata={...}` attaches arbitrary structured metadata (for example, environment, experiment name, or feature flag).


In this example, the agent is invoked twice, but only the invocation inside `tracing_context` is recorded. This demonstrates how you can selectively trace specific parts of a Deep Agents workflow without enabling global tracing for the entire process.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-deep-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Create a trace
## ​Viewing traces
## ​Customize LangSmith tracing







Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Google ADK applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-google-adk`

# Trace Google ADK applications

This guide shows you how to trace [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) agents in LangSmith. You’ll configure automatic tracing for your ADK applications to capture agent invocations, tool calls, and LLM interactions.
This guide covers ADK’s standard execution paths (text agents, tools, and multi-agent workflows). To trace a **Gemini Live** voice agent, which uses ADK’s `Runner.run_live` streaming loop, see [Trace Gemini Live applications](https://docs.langchain.com/langsmith/trace-gemini-live).


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#installation) Installation


Install the required packages using your preferred package manager:
uv pip

```
uv add "langsmith[google-adk]"
```


```
pip install langsmith[google-adk]
```


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#setup) Setup


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key):
shell.env

```
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_langsmith_project>

export GOOGLE_API_KEY=<your_google_api_key>
```


```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your_langsmith_api_key>
LANGSMITH_PROJECT=<your_langsmith_project>

GOOGLE_API_KEY=<your_google_api_key>
```


To create a Google API key, refer to [Google AI Studio](https://aistudio.google.com/api-keys).


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#configure-tracing) Configure tracing


To trace ADK agents, use `configure_google_adk()` from the LangSmith SDK. Call this function once at the start of your application before creating any ADK agents:


```
from langsmith.integrations.google_adk import configure_google_adk

configure_google_adk(
    project_name="my-adk-project",  # Optional: defaults to LANGSMITH_PROJECT env var
)
```


The function accepts the following optional parameters:


- `project_name`: LangSmith project to send traces to. Defaults to the `LANGSMITH_PROJECT` environment variable.
- `name`: Name for the root trace. Defaults to `"google_adk.session"`.
- `metadata`: Dictionary of key-value pairs for additional context.
- `tags`: List of strings to categorize traces.


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#example) Example


This example creates a weather agent with a tool, then runs it with tracing enabled:


```
import asyncio

from dotenv import load_dotenv  # Optional
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from langsmith.integrations.google_adk import configure_google_adk

load_dotenv()  # Optional


async def main():
    # Configure LangSmith tracing
    configure_google_adk()

    # Define a tool
    def get_weather(city: str) -> dict:
        """Get weather for a city."""
        return {"city": city, "temperature": "72°F", "conditions": "Sunny"}

    # Create the agent
    agent = Agent(
        name="weather_agent",
        model="gemini-3.8-flash",
        description="Provides weather information.",
        instruction="Use the get_weather tool to answer weather questions.",
        tools=[get_weather],
    )

    # Set up session and runner
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="weather_app",
        user_id="user_123",
        session_id="session_456",
    )

    runner = Runner(
        agent=agent,
        app_name="weather_app",
        session_service=session_service,
    )

    # Run the agent
    async for event in runner.run_async(
        user_id="user_123",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text="What's the weather in San Francisco?")],
        ),
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
```


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#view-traces-in-langsmith) View traces in LangSmith


After running your application, you can view traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-google-adk) that include:


- **Agent invocations**: Complete flows through your ADK agents
- **Tool calls**: Individual function calls made by agents
- **LLM interactions**: Requests and responses from Gemini models
- **Multi-agent workflows**: Traces from sequential and parallel agent compositions


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#custom-metadata-and-tags) Custom metadata and tags


Add metadata and tags when configuring tracing to categorize and filter traces:


```
from langsmith.integrations.google_adk import configure_google_adk

configure_google_adk(
    project_name="production-agents",
    metadata={
        "environment": "production",
        "team": "ml-platform",
    },
    tags=["adk", "weather", "v2"],
)
```


## [​](https://docs.langchain.com/langsmith/trace-with-google-adk#multi-agent-workflows) Multi-agent workflows


The integration automatically traces multi-agent workflows including sequential and parallel agent compositions:


```
import asyncio

from dotenv import load_dotenv  # Optional
from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from langsmith.integrations.google_adk import configure_google_adk

load_dotenv()  # Optional


async def main():
    # Configure LangSmith tracing
    # Traces go to LANGSMITH_PROJECT env var by default.
    # Pass project_name="my-project" to override.
    configure_google_adk()

    # Create sub-agents
    translator = Agent(
        name="translator",
        model="gemini-3.8-flash",
        description="Translates text to English.",
    )

    summarizer = Agent(
        name="summarizer",
        model="gemini-3.8-flash",
        description="Summarizes text concisely.",
    )

    # Create a sequential agent that runs sub-agents in order
    pipeline = SequentialAgent(
        name="translate_and_summarize",
        sub_agents=[translator, summarizer],
        description="Translates text then summarizes it.",
    )

    # Set up and run
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="pipeline_app",
        user_id="user_123",
        session_id="session_456",
    )

    runner = Runner(
        agent=pipeline,
        app_name="pipeline_app",
        session_service=session_service,
    )

    events = runner.run_async(
        user_id="user_123",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text="Quelle est la plus haute tour de Paris?")],
        ),
    )

    async for event in events:
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-google-adk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure tracing
## ​Example
## ​View traces in LangSmith
## ​Custom metadata and tags
## ​Multi-agent workflows









Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace CrewAI applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-crewai`

# Trace CrewAI applications

LangSmith can capture traces generated by [CrewAI](https://github.com/crewAIInc/crewAI) using OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your CrewAI multi-agent workflows and send them to LangSmith for monitoring and analysis.


## [​](https://docs.langchain.com/langsmith/trace-with-crewai#installation) Installation


Install the required packages using your preferred package manager:
pip uv

```
pip install langsmith crewai opentelemetry-instrumentation-crewai opentelemetry-instrumentation-openai
```


```
uv add langsmith crewai opentelemetry-instrumentation-crewai opentelemetry-instrumentation-openai
```


## [​](https://docs.langchain.com/langsmith/trace-with-crewai#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-crewai#1-configure-environment-variables) 1. Configure environment variables


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```


### [​](https://docs.langchain.com/langsmith/trace-with-crewai#2-configure-opentelemetry-integration) 2. Configure OpenTelemetry integration


In your CrewAI application, configure the LangSmith OpenTelemetry integration along with the CrewAI and OpenAI instrumentors:


```
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Get or create tracer provider
current_provider = trace.get_tracer_provider()
if isinstance(current_provider, TracerProvider):
    tracer_provider = current_provider
else:
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)

# Add OtelSpanProcessor to the tracer provider
tracer_provider.add_span_processor(OtelSpanProcessor())

# Instrument CrewAI and OpenAI
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```


### [​](https://docs.langchain.com/langsmith/trace-with-crewai#3-create-and-run-your-crewai-application) 3. Create and run your CrewAI application


Once configured, your CrewAI application will automatically send traces to LangSmith:


```
from crewai import Agent, Crew, Task
from crewai.llm import LLM
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Configure OpenTelemetry
current_provider = trace.get_tracer_provider()
if isinstance(current_provider, TracerProvider):
    tracer_provider = current_provider
else:
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)

tracer_provider.add_span_processor(OtelSpanProcessor())

# Instrument CrewAI and OpenAI
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

# Define your agent
llm = LLM(model="gpt-6-luna")

coder = Agent(
    role="Software developer",
    goal="Write clear, concise code on demand",
    backstory="An expert coder with a keen eye for software trends.",
    verbose=True,
    llm=llm,
)

# Define your task
task = Task(
    description="Write a Python function that checks if a number is prime.",
    expected_output="A clear and concise Python function with documentation.",
    agent=coder,
)

# Create and run the crew
crew = Crew(
    agents=[coder],
    tasks=[task],
    verbose=True,
)

def run_crew():
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    output = run_crew()
    print(output)
```


## [​](https://docs.langchain.com/langsmith/trace-with-crewai#advanced-usage) Advanced usage


### [​](https://docs.langchain.com/langsmith/trace-with-crewai#custom-metadata-and-tags) Custom metadata and tags


You can add custom metadata to your traces by setting span attributes:


```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def run_crew_with_metadata():
    with tracer.start_as_current_span("crewai_workflow") as span:
        span.set_attribute("langsmith.metadata.crew_type", "code_generation")
        span.set_attribute("langsmith.metadata.agent_count", "1")
        span.set_attribute("langsmith.span.tags", "crewai,code-generation")

        result = crew.kickoff()
        return result
```


### [​](https://docs.langchain.com/langsmith/trace-with-crewai#combining-with-other-instrumentors) Combining with other instrumentors


You can combine CrewAI instrumentation with other OpenTelemetry instrumentors:


```
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Initialize multiple instrumentors
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```


## [​](https://docs.langchain.com/langsmith/trace-with-crewai#resources) Resources


- [CrewAI documentation](https://docs.crewai.com/)
- [LangSmith OpenTelemetry guide](https://docs.langchain.com/langsmith/trace-with-opentelemetry)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-crewai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Advanced usage
## ​Resources






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Mastra applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-mastra`

# Trace Mastra applications

[Mastra](https://mastra.ai/docs) is a TypeScript framework for building AI-powered applications and agents. Using Mastra’s [LangSmith exporter](https://mastra.ai/reference/observability/tracing/exporters/langsmith), you can send traces from your Mastra agents and workflows to LangSmith for debugging, evaluation, and observability.
This guide shows you how to integrate Mastra with LangSmith using Mastra’s AI tracing system.


## [​](https://docs.langchain.com/langsmith/trace-with-mastra#installation) Installation


Install Mastra and the LangSmith exporter:


```
npm install @mastra/core @mastra/langsmith @mastra/observability @mastra/libsql
```


## [​](https://docs.langchain.com/langsmith/trace-with-mastra#setup) Setup


1. Set your LangSmith API key and (optionally) a LangSmith project name: ``` export LANGSMITH_API_KEY=<your_langsmith_api_key> export LANGCHAIN_PROJECT=<your_project_name> # optional ``` If [`LANGCHAIN_PROJECT`](https://docs.langchain.com/langsmith/log-traces-to-project) is not set, traces will be sent to the default project.
2. If you plan to use OpenAI models, also ensure you have an OpenAI API key available at runtime: ``` export OPENAI_API_KEY=<your_openai_api_key> ```
3. In your project directory, create the following project structure and files: ``` src/ mastra.ts agent.ts index.ts ```


## [​](https://docs.langchain.com/langsmith/trace-with-mastra#configure-mastra-with-the-langsmith-exporter) Configure Mastra with the LangSmith exporter


Mastra tracing is configured directly on the `Mastra` constructor. Add the following to a `mastra.ts` file:


```
import { Mastra } from "@mastra/core";
import { LibSQLStore } from "@mastra/libsql";
import { LangSmithExporter } from "@mastra/langsmith";

import { echoAgent } from "./agent";

export const mastra = new Mastra({
  agents: { echoAgent },

  storage: new LibSQLStore({
    url: "file:./mastra.db",
  }),

  observability: {
    configs: {
      langsmith: {
        serviceName: "mastra-langsmith-demo",
        exporters: [
          new LangSmithExporter({
            apiKey: process.env.LANGSMITH_API_KEY,
          }),
        ],
      },
    },
  },

  // Disable deprecated telemetry system
  telemetry: {
    enabled: false,
  },
});
```


- [Storage is required for tracing](https://mastra.ai/docs/observability/integrations/exporters/mastra-storage) (even when exporting traces externally).
- The LangSmith exporter reads credentials from environment variables.
- The [deprecated telemetry system](https://mastra.ai/docs/observability/overview#otel-tracing-deprecated) is disabled to avoid warnings.
- No separate instrumentation file is required when running Mastra outside of the Mastra server. For more details, refer to the [Mastra docs](https://mastra.ai/docs/observability/overview).


### [​](https://docs.langchain.com/langsmith/trace-with-mastra#define-an-agent) Define an agent


For compatibility, use [string-based model identifiers](https://mastra.ai/models#basic-usage). Add the following code to an `agent.ts` file:


```
import { Agent } from "@mastra/core/agent";

export const echoAgent = new Agent({
  name: "echoAgent",
  instructions: "You are a helpful assistant.",
  model: "openai/gpt-6-luna",
});
```


Mastra will automatically route the model call using your configured API keys and capture traces for each invocation.


### [​](https://docs.langchain.com/langsmith/trace-with-mastra#run-the-agent) Run the agent


1. Add the following to an `index.ts` file: ``` import { mastra } from "./mastra"; async function main() { const agent = mastra.getAgent("echoAgent"); const result = await agent.generate("Say hello and explain what Mastra is."); console.log(result.text); } main(); ```
2. Run your application: ``` npx ts-node src/index.ts ```


## [​](https://docs.langchain.com/langsmith/trace-with-mastra#view-traces-in-langsmith) View traces in LangSmith


After running the agent:


1. Open the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-mastra).
2. Select your project. For example, the value of `LANGCHAIN_PROJECT`.
3. Locate the trace corresponding to `echoAgent.generate`.


You’ll be able to inspect:


- Model inputs and outputs
- Agent execution steps
- Timing and error information


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-mastra.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Configure Mastra with the LangSmith exporter
## ​View traces in LangSmith






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace LangChain applications (Python and JS/TS) - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-langchain`

# Trace LangChain applications (Python and JS/TS

LangSmith integrates seamlessly with LangChain (Python and JavaScript), the popular open-source framework for building LLM applications.


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#installation) Installation


Install the following for Python or JS (the code snippets use the OpenAI integration).
For a full list of packages available, see the [LangChain docs](https://docs.langchain.com/oss/python/integrations/providers/overview).
pip yarn npm pnpm

```
pip install langchain_openai
```


```
yarn add @langchain/openai @langchain/core
```


```
npm install @langchain/openai @langchain/core
```


```
pnpm add @langchain/openai @langchain/core
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#quick-start) Quick start


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#1-configure-your-environment) 1. Configure your environment


```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>
# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```


If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won’t be recognized and requests will fail to authenticate.

| Region |
| --- |
| GCP US |
| GCP EU |
| GCP APAC |
| AWS US |

For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency: `export LANGCHAIN_CALLBACKS_BACKGROUND=true` If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends: `export LANGCHAIN_CALLBACKS_BACKGROUND=false`


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#2-log-a-trace) 2. Log a trace


No extra code is needed to log a trace to LangSmith. Just run your LangChain code as you normally would.
Python TypeScript

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

model = ChatOpenAI(model="gpt-6-luna")
output_parser = StrOutputParser()
chain = prompt | model | output_parser

question = "Can you summarize this morning's meetings?"
context = "During this morning's meeting, we solved all world conflict."

chain.invoke({"question": question, "context": context})
```


```
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],
  ["user", "Question: {question}\nContext: {context}"],
]);

const model = new ChatOpenAI({ modelName: "gpt-6-luna" });
const outputParser = new StringOutputParser();
const chain = prompt.pipe(model).pipe(outputParser);

const question = "Can you summarize this morning's meetings?"
const context = "During this morning's meeting, we solved all world conflict."

await chain.invoke({ question: question, context: context });
```


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#3-view-your-trace) 3. View your trace


By default, the trace will be logged to the project with the name `default`.


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#trace-selectively) Trace selectively


The [previous section](https://docs.langchain.com/langsmith/trace-with-langchain#quick-start) showed how to trace all invocations of a LangChain runnables within your applications by setting a single environment variable. While this is a convenient way to get started, you may want to trace only specific invocations or parts of your application.
There are two ways to do this in Python: by manually passing in a `LangChainTracer` instance as a [callback](https://reference.langchain.com/python/langchain_core/callbacks/), or by using the [`tracing_context` context manager](https://reference.langchain.com/python/langsmith/observability/sdk/run_helpers/#langsmith.run_helpers.tracing_context).
In JS/TS, you can pass a [`LangChainTracer`](https://reference.langchain.com/javascript/classes/_langchain_core.tracers_tracer_langchain.LangChainTracer.html) instance as a callback.
Python TypeScript

```
# You can opt-in to specific invocations..
import langsmith as ls

with ls.tracing_context(enabled=True):
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"})

# This will NOT be traced (assuming LANGSMITH_TRACING is not set)
chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})

# This would not be traced, even if LANGSMITH_TRACING=true
with ls.tracing_context(enabled=False):
    chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})
```


```
// You can configure a LangChainTracer instance to trace a specific invocation.
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer();
await chain.invoke(
  {
    question: "Am I using a callback?",
    context: "I'm using a callback"
  },
  { callbacks: [tracer] }
);
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#log-to-a-specific-project) Log to a specific project


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#statically) Statically


As mentioned in the [tracing conceptual guide](https://docs.langchain.com/langsmith/observability-concepts) LangSmith uses the concept of a Project to group traces. If left unspecified, the tracer project is set to default. You can set the `LANGSMITH_PROJECT` environment variable to configure a custom project name for an entire application run. This should be done before executing your application.


```
export LANGSMITH_PROJECT=my-project
```


The `LANGSMITH_PROJECT` flag is only supported in JS SDK 0.2.16 or later, use `LANGCHAIN_PROJECT` instead if you are using an older version.


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#dynamically) Dynamically


This largely builds off of the [previous section](https://docs.langchain.com/langsmith/trace-with-langchain#trace-selectively) and allows you to set the project name for a specific `LangChainTracer` instance or as parameters to the `tracing_context` context manager in Python.
Python TypeScript

```
# You can set the project name using the project_name parameter.
import langsmith as ls

with ls.tracing_context(project_name="My Project", enabled=True):
    chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})
```


```
// You can set the project name for a specific tracer instance:
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer({ projectName: "My Project" });
await chain.invoke(
  {
    question: "Am I using a callback?",
    context: "I'm using a callback"
  },
  { callbacks: [tracer] }
);
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#add-metadata-and-tags-to-traces) Add metadata and tags to traces


You can annotate your traces with arbitrary metadata and tags by providing them in the [`RunnableConfig`](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This is useful for associating additional information with a trace, such as the environment in which it was executed, or the user who initiated it. For information on how to query traces and runs by metadata and tags, see [Query traces (SDK)](https://docs.langchain.com/langsmith/export-traces)
When you attach metadata or tags to a runnable (either through the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) or at runtime with invocation params), they are inherited by all child runnables of that runnable.
Python TypeScript

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI."),
    ("user", "{input}")
])

# The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only
chat_model = ChatOpenAI().with_config({"tags": ["model-tag"], "metadata": {"model-key": "model-value"}})
output_parser = StrOutputParser()

# Tags and metadata can be configured with RunnableConfig
chain = (prompt | chat_model | output_parser).with_config({"tags": ["config-tag"], "metadata": {"config-key": "config-value"}})

# Tags and metadata can also be passed at runtime
chain.invoke({"input": "What is the meaning of life?"}, {"tags": ["invoke-tag"], "metadata": {"invoke-key": "invoke-value"}})
```


```
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";

const prompt = ChatPromptTemplate.fromMessages([
    ["system", "You are a helpful AI."],
    ["user", "{input}"]
])

// The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only
const model = new ChatOpenAI().withConfig({ tags: ["model-tag"], metadata: { "model-key": "model-value" } });
const outputParser = new StringOutputParser();

// Tags and metadata can be configured with RunnableConfig
const chain = (prompt.pipe(model).pipe(outputParser)).withConfig({"tags": ["config-tag"], "metadata": {"config-key": "top-level-value"}});

// Tags and metadata can also be passed at runtime
await chain.invoke({input: "What is the meaning of life?"}, {tags: ["invoke-tag"], metadata: {"invoke-key": "invoke-value"}})
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#customize-run-name) Customize run name


You can customize the name of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This name is used to identify the run in LangSmith and can be used to filter and group runs. The name is also used as the title of the run in the LangSmith UI. This can be done by setting a `run_name` in the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) object at construction or by passing a `run_name` in the invocation parameters in JS/TS.
Python TypeScript

```
# When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').
configured_chain = chain.with_config({"run_name": "MyCustomChain"})
configured_chain.invoke({"input": "What is the meaning of life?"})

# You can also configure the run name at invocation time, like below
chain.invoke({"input": "What is the meaning of life?"}, {"run_name": "MyCustomChain"})
```


```
// When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').
const configuredChain = chain.withConfig({ runName: "MyCustomChain" });
await configuredChain.invoke({ input: "What is the meaning of life?" });

// You can also configure the run name at invocation time, like below
await chain.invoke({ input: "What is the meaning of life?" }, {runName: "MyCustomChain"})
```


The `run_name` parameter only changes the name of the runnable you invoke (e.g., a chain, function). It does not rename the nested run automatically created when you invoke an LLM object like [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) (`gpt-6-luna`). In the example, the enclosing run will appear in LangSmith as `MyCustomChain`, while the nested LLM run still shows the model’s default name. To give the LLM run a more meaningful name, you can either:

- Wrap the model in another runnable and assign a `run_name` to that step.
- Use a tracing decorator or helper (e.g., `@traceable` in Python, or `traceable` from `langsmith` in JS/TS) to create a custom run around the model call.


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#override-model-name-in-traces) Override model name in traces


When tracing LangChain model calls, LangSmith automatically captures the model identifier used in the API call. However, you may want to display a different, more descriptive name in traces for organizational purposes or to distinguish between different model configurations. You can do this by passing the `ls_model_name` [metadata parameter](https://docs.langchain.com/langsmith/ls-metadata-parameters#ls_model_name) when constructing or configuring your LangChain model.
This is particularly useful when:


- Working with self-hosted or local models where the model ID might not be descriptive.
- Using the same model with different configurations and wanting to distinguish them in traces.
- Creating aliases for models to make traces more readable for your team.
- Standardizing model names across different deployment environments.


Python TypeScript

```
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# Override model name for a local model
llm = ChatOllama(
    model="llama2:13b-chat",  # Actual model ID
    metadata={"ls_model_name": "llama2-13b-production"}  # Name shown in LangSmith
)

# Or with OpenAI to distinguish configurations
llm_creative = ChatOpenAI(
    model="gpt-5.5",
    temperature=0.9,
    metadata={"ls_model_name": "gpt-5.4-creative"}
)

llm_factual = ChatOpenAI(
    model="gpt-5.5",
    temperature=0.1,
    metadata={"ls_model_name": "gpt-5.4-factual"}
)

# The metadata is inherited when the model is used in a chain
result = llm.invoke("What is the meaning of life?")
```


```
import { ChatOpenAI } from "@langchain/openai";
import { ChatOllama } from "@langchain/ollama";

// Override model name for a local model
const llm = new ChatOllama({
  model: "llama2:13b-chat",  // Actual model ID
  metadata: { ls_model_name: "llama2-13b-production" }  // Name shown in LangSmith
});

// Or with OpenAI to distinguish configurations
const llmCreative = new ChatOpenAI({
  modelName: "gpt-5.5",
  temperature: 0.9,
  metadata: { ls_model_name: "gpt-5.4-creative" }
});

const llmFactual = new ChatOpenAI({
  modelName: "gpt-5.5",
  temperature: 0.1,
  metadata: { ls_model_name: "gpt-5.4-factual" }
});

// The metadata is inherited when the model is used in a chain
const result = await llm.invoke("What is the meaning of life?");
```


When you pass `ls_model_name` in the model’s metadata, this name will appear in the LangSmith UI for all traces involving that model instance. This works for any LangChain chat model or LLM and is inherited by all runs that use the model, including when it’s part of a chain.
The `ls_model_name` metadata parameter is also used for [cost tracking](https://docs.langchain.com/langsmith/cost-tracking). When combined with the `ls_provider` parameter, LangSmith can automatically calculate costs for custom or self-hosted models. For more information about all available metadata parameters, see the [metadata parameters reference](https://docs.langchain.com/langsmith/ls-metadata-parameters).


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#customize-run-id) Customize run ID


You can customize the ID of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This ID is used to uniquely identify the run in LangSmith and can be used to query specific runs. The ID can be useful for linking runs across different systems or for implementing custom tracking logic. This can be done by setting a `run_id` in the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) object at construction or by passing a `run_id` in the invocation parameters.
This feature is not currently supported directly for LLM objects.
Python TypeScript

```
from langchain_core.utils.uuid import uuid7

my_uuid = uuid7()

# You can configure the run ID at invocation time:
chain.invoke({"input": "What is the meaning of life?"}, {"run_id": my_uuid})
```


```
import { uuid7 } from "langsmith";

const myUuid = uuid7();

// You can configure the run ID at invocation time, like below
await chain.invoke({ input: "What is the meaning of life?" }, { runId: myUuid });
```


Note that if you do this at the **root** of a trace (i.e., the top-level run, that run ID will be used as the `trace_id`).


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#access-run-span-id-for-langchain-invocations) Access run (span) ID for LangChain invocations


When you invoke a LangChain object, you can manually specify the run ID of the invocation. This run ID can be used to query the run in LangSmith.
In JS/TS, you can use a `RunCollectorCallbackHandler` instance to access the run ID.
Python TypeScript

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.utils.uuid import uuid7

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\n\nContext: {context}")
])
model = ChatOpenAI(model="gpt-6-luna")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

question = "Can you summarize this morning's meetings?"
context = "During this morning's meeting, we solved all world conflict."
my_uuid = uuid7()
result = chain.invoke({"question": question, "context": context}, {"run_id": my_uuid})
print(my_uuid)
```


```
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { RunCollectorCallbackHandler } from "@langchain/core/tracers/run_collector";

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],
  ["user", "Question: {question}\n\nContext: {context}"],
]);
const model = new ChatOpenAI({ modelName: "gpt-6-luna" });
const outputParser = new StringOutputParser();

const chain = prompt.pipe(model).pipe(outputParser);
const runCollector = new RunCollectorCallbackHandler();

const question = "Can you summarize this morning's meetings?"
const context = "During this morning's meeting, we solved all world conflict."
await chain.invoke(
    { question: question, context: context },
    { callbacks: [runCollector] }
);
const runId = runCollector.tracedRuns[0].id;
console.log(runId);
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#ensure-all-traces-are-submitted-before-exiting) Ensure all traces are submitted before exiting


In LangChain Python, LangSmith’s tracing is done in a background thread to avoid obstructing your production application. This means that your process may end before all traces are successfully posted to LangSmith. This is especially prevalent in a serverless environment, where your VM may be terminated immediately once your chain or agent completes.
You can make callbacks synchronous by setting the `LANGCHAIN_CALLBACKS_BACKGROUND` environment variable to `"false"`.
For both languages, LangChain exposes methods to wait for traces to be submitted before exiting your application. Below is an example:
Python TypeScript

```
from langchain_openai import ChatOpenAI
from langchain_core.tracers.langchain import wait_for_all_tracers

llm = ChatOpenAI()

try:
  llm.invoke("Hello, World!")
finally:
  wait_for_all_tracers()
```


```
import { awaitAllCallbacks } from "@langchain/core/callbacks/promises";

try {
    const llm = new ChatOpenAI();
    const response = await llm.invoke("Hello, World!");
} catch (e) {
    // handle error
} finally {
    await awaitAllCallbacks();
}
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#trace-without-setting-environment-variables) Trace without setting environment variables


As mentioned in other guides, the following environment variables allow you to configure tracing enabled, the api endpoint, the api key, and the tracing project:


- `LANGSMITH_TRACING`
- `LANGSMITH_API_KEY`
- `LANGSMITH_ENDPOINT`
- `LANGSMITH_PROJECT`


However, in some environments, it is not possible to set environment variables. In these cases, you can set the tracing configuration programmatically.
This largely builds off of the [previous section](https://docs.langchain.com/langsmith/trace-with-langchain#trace-selectively).
Python TypeScript

```
import langsmith as ls

# You can create a client instance with an api key and api url
client = ls.Client(
    api_key="YOUR_API_KEY",  # This can be retrieved from a secrets manager
    api_url="https://api.smith.langchain.com",  # Self-hosted, GCP EU (`eu.api...`), GCP APAC (`apac.api...`), or AWS US (`aws.api...`) as needed
)

# You can pass the client and project_name to the tracing_context
with ls.tracing_context(client=client, project_name="test-no-env", enabled=True):
    chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"})
```


```
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";
import { Client } from "langsmith";

// You can create a client instance with an api key and api url
const client = new Client(
    {
        apiKey: "YOUR_API_KEY",
        apiUrl: "https://api.smith.langchain.com", // Self-hosted, GCP EU (`eu.api...`), GCP APAC (`apac.api...`), or AWS US (`aws.api...`) as needed
    }
);

// You can pass the client and project_name to the LangChainTracer instance
const tracer = new LangChainTracer({client, projectName: "test-no-env"});
await chain.invoke(
  {
    question: "Am I using a callback?",
    context: "I'm using a callback",
  },
  { callbacks: [tracer] }
);
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#distributed-tracing-with-langchain-python) Distributed tracing with LangChain (Python)


LangSmith supports distributed tracing with LangChain Python. This allows you to link runs (spans) across different services and applications. The principles are similar to the [distributed tracing guide](https://docs.langchain.com/langsmith/distributed-tracing) for the LangSmith SDK.


```
import langsmith
from langchain_core.runnables import chain
from langsmith.run_helpers import get_current_run_tree

# -- This code should be in a separate file or service --
@chain
def child_chain(inputs):
    return inputs["test"] + 1

def child_wrapper(x, headers):
    with langsmith.tracing_context(parent=headers):
        child_chain.invoke({"test": x})

# -- This code should be in a separate file or service --
@chain
def parent_chain(inputs):
    rt = get_current_run_tree()
    headers = rt.to_headers()
    # ... make a request to another service with the headers
    # The headers should be passed to the other service, eventually to the child_wrapper function

parent_chain.invoke({"test": 1})
```


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#interoperability-between-langchain-python-and-langsmith-sdk) Interoperability between LangChain (Python) and LangSmith SDK


If you are using LangChain for part of your application and the LangSmith SDK (see [Custom instrumentation](https://docs.langchain.com/langsmith/annotate-code)) for other parts, you can still trace the entire application seamlessly.
LangChain objects will be traced when invoked within a `traceable` function and be bound as a child run of the `traceable` function.


```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

model = ChatOpenAI(model="gpt-6-luna")
output_parser = StrOutputParser()
chain = prompt | model | output_parser

# The above chain will be traced as a child run of the traceable function
@traceable(
    tags=["openai", "chat"],
    metadata={"foo": "bar"}
)
def invoke_runnnable(question, context):
    result = chain.invoke({"question": question, "context": context})
    return "The response is: " + result

invoke_runnnable("Can you summarize this morning's meetings?", "During this morning's meeting, we solved all world conflict.")
```


This will produce the following trace tree: ![Trace tree python interop](https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/trace-tree-python-interop.png?fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=52c64fd784522c4b2d75886ae76f8c18)


## [​](https://docs.langchain.com/langsmith/trace-with-langchain#interoperability-between-langchain-js-and-langsmith-sdk) Interoperability between LangChain.JS and LangSmith SDK


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#tracing-langchain-objects-inside-traceable-js-only) Tracing LangChain objects inside `traceable` (JS only)


Starting with `langchain@0.2.x`, LangChain objects are traced automatically when used inside `@traceable` functions, inheriting the client, tags, metadata and project name of the traceable function.
For older versions of LangChain below `0.2.x`, you will need to manually pass an instance `LangChainTracer` created from the tracing context found in `@traceable`.


```
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { getLangchainCallbacks } from "langsmith/langchain";

const prompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "You are a helpful assistant. Please respond to the user's request only based on the given context.",
  ],
  ["user", "Question: {question}\nContext: {context}"],
]);

const model = new ChatOpenAI({ modelName: "gpt-6-luna" });
const outputParser = new StringOutputParser();
const chain = prompt.pipe(model).pipe(outputParser);

const main = traceable(
  async (input: { question: string; context: string }) => {
    const callbacks = await getLangchainCallbacks();
    const response = await chain.invoke(input, { callbacks });
    return response;
  },
  { name: "main" }
);
```


### [​](https://docs.langchain.com/langsmith/trace-with-langchain#tracing-langchain-child-runs-via-traceable-/-runtree-api-js-only) Tracing LangChain child runs via `traceable` / RunTree API (JS only)


We’re working on improving the interoperability between `traceable` and LangChain. The following limitations are present when using combining LangChain with `traceable`:

1. Mutating RunTree obtained from `getCurrentRunTree()` of the RunnableLambda context will result in a no-op.
2. It’s discouraged to traverse the RunTree obtained from RunnableLambda via `getCurrentRunTree()` as it may not contain all the RunTree nodes.
3. Different child runs may have the same `execution_order` and `child_execution_order` value. Thus in extreme circumstances, some runs may end up in a different order, depending on the `start_time`.


In some uses cases, you might want to run `traceable` functions as part of the RunnableSequence or trace child runs of LangChain run imperatively via the `RunTree` API. Starting with LangSmith 0.1.39 and @langchain/core 0.2.18, you can directly invoke `traceable` -wrapped functions within RunnableLambda.


```
import { traceable } from "langsmith/traceable";
import { RunnableLambda } from "@langchain/core/runnables";
import { RunnableConfig } from "@langchain/core/runnables";

const tracedChild = traceable((input: string) => `Child Run: ${input}`, {
  name: "Child Run",
});

const parrot = new RunnableLambda({
  func: async (input: { text: string }, config?: RunnableConfig) => {
    return await tracedChild(input.text);
  },
});
```


![Trace Tree](https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/trace-tree-manual-tracing.png?fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=7b117d3aa9b419fe2a314ec6d9cc7c16)
Alternatively, you can convert LangChain’s [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) to a equivalent RunTree object by using `RunTree.fromRunnableConfig` or pass the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) as the first argument of `traceable` -wrapped function.
Traceable Run Tree

```
import { traceable } from "langsmith/traceable";
import { RunnableLambda } from "@langchain/core/runnables";
import { RunnableConfig } from "@langchain/core/runnables";

const tracedChild = traceable((input: string) => `Child Run: ${input}`, {
  name: "Child Run",
});

const parrot = new RunnableLambda({
  func: async (input: { text: string }, config?: RunnableConfig) => {
    // Pass the config to existing traceable function
    await tracedChild(config, input.text);
    return input.text;
  },
});
```


```
import { RunTree } from "langsmith/run_trees";
import { RunnableLambda } from "@langchain/core/runnables";
import { RunnableConfig } from "@langchain/core/runnables";

const parrot = new RunnableLambda({
  func: async (input: { text: string }, config?: RunnableConfig) => {
    // create the RunTree from the RunnableConfig of the RunnableLambda
    const childRunTree = RunTree.fromRunnableConfig(config, {
      name: "Child Run",
    });

    childRunTree.inputs = { input: input.text };
    await childRunTree.postRun();

    childRunTree.outputs = { output: `Child Run: ${input.text}` };
    await childRunTree.patchRun();

    return input.text;
  },
});
```


If you prefer a video tutorial, check out the [Alternative Ways to Trace video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Quick start
## ​Trace selectively
## ​Log to a specific project
## ​Add metadata and tags to traces
## ​Customize run name
## ​Override model name in traces
## ​Customize run ID
## ​Access run (span) ID for LangChain invocations
## ​Ensure all traces are submitted before exiting
## ​Trace without setting environment variables
## ​Distributed tracing with LangChain (Python)
## ​Interoperability between LangChain (Python) and LangSmith SDK
## ​Interoperability between LangChain.JS and LangSmith SDK
















Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace LangGraph applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-langgraph`

# Trace LangGraph applications

LangSmith smoothly integrates with LangGraph (Python and JS) to help you trace agents, whether you’re using LangChain modules or other SDKs.


## [​](https://docs.langchain.com/langsmith/trace-with-langgraph#with-langchain) With LangChain


If you are using LangChain modules within LangGraph, you only need to set a few environment variables to enable tracing.
This guide will walk through a basic example. For more detailed information on configuration, see the [Trace With LangChain](https://docs.langchain.com/langsmith/trace-with-langchain) guide.


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#1-installation) 1. Installation


Install the LangGraph library and the OpenAI integration for Python and JS (we use the OpenAI integration for the code snippets below).
For a full list of packages available, see the [LangChain Python docs](https://docs.langchain.com/oss/python/integrations/providers/overview) and [LangChain JS docs](https://docs.langchain.com/oss/javascript/integrations/providers/overview).
pip yarn npm pnpm

```
pip install langchain_openai langgraph
```


```
yarn add @langchain/openai @langchain/langgraph
```


```
npm install @langchain/openai @langchain/langgraph
```


```
pnpm add @langchain/openai @langchain/langgraph
```


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#2-configure-your-environment) 2. Configure your environment


```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>
# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```


If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won’t be recognized and requests will fail to authenticate.

| Region |
| --- |
| GCP US |
| GCP EU |
| GCP APAC |
| AWS US |

For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency: `export LANGCHAIN_CALLBACKS_BACKGROUND=true` If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends: `export LANGCHAIN_CALLBACKS_BACKGROUND=false` See [this LangChain.js guide](https://js.langchain.com/docs/how_to/callbacks_serverless) for more information.


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#3-log-a-trace) 3. Log a trace


Once you’ve set up your environment, you can call LangChain runnables as normal. LangSmith will infer the proper tracing config:
Python TypeScript

```
from typing import Literal
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, MessagesState

@tool
def search(query: str):
    """Call to surf the web."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."

tools = [search]
tool_node = ToolNode(tools)

model = ChatOpenAI(model="gpt-6-luna").bind_tools(tools)

def should_continue(state: MessagesState) -> Literal["tools", "__end__"]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "__end__"

def call_model(state: MessagesState):
    messages = state['messages']
    # Invoking `model` will automatically infer the correct tracing context
    response = model.invoke(messages)
    return {"messages": [response]}

workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge("__start__", "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
)
workflow.add_edge("tools", 'agent')

app = workflow.compile()

final_state = app.invoke(
    {"messages": [HumanMessage(content="what is the weather in sf")]},
    config={"configurable": {"thread_id": 42}}
)

final_state["messages"][-1].content
```


```
import { HumanMessage, AIMessage } from "@langchain/core/messages";
import { tool } from "@langchain/core/tools";
import { z } from "zod";
import { ChatOpenAI } from "@langchain/openai";
import { StateGraph, StateGraphArgs } from "@langchain/langgraph";
import { ToolNode } from "@langchain/langgraph/prebuilt";

interface AgentState {
  messages: HumanMessage[];
}

const graphState: StateGraphArgs<AgentState>["channels"] = {
  messages: {
    reducer: (x: HumanMessage[], y: HumanMessage[]) => x.concat(y),
  },
};

const searchTool = tool(async ({ query }: { query: string }) => {
  if (query.toLowerCase().includes("sf") || query.toLowerCase().includes("san francisco")) {
    return "It's 60 degrees and foggy."
  }
  return "It's 90 degrees and sunny."
}, {
  name: "search",
  description:
    "Call to surf the web.",
  schema: z.object({
    query: z.string().describe("The query to use in your search."),
  }),
});

const tools = [searchTool];
const toolNode = new ToolNode<AgentState>(tools);

const model = new ChatOpenAI({
  model: "gpt-6-luna",
}).bindTools(tools);

function shouldContinue(state: AgentState) {
  const messages = state.messages;
  const lastMessage = messages[messages.length - 1] as AIMessage;
  if (lastMessage.tool_calls?.length) {
    return "tools";
  }
  return "__end__";
}

async function callModel(state: AgentState) {
  const messages = state.messages;
  // Invoking `model` will automatically infer the correct tracing context
  const response = await model.invoke(messages);
  return { messages: [response] };
}

const workflow = new StateGraph<AgentState>({ channels: graphState })
  .addNode("agent", callModel)
  .addNode("tools", toolNode)
  .addEdge("__start__", "agent")
  .addConditionalEdges("agent", shouldContinue)
  .addEdge("tools", "agent");

const app = workflow.compile();

const finalState = await app.invoke(
  { messages: [new HumanMessage("what is the weather in sf")] },
  { configurable: { thread_id: "42" } }
);

finalState.messages[finalState.messages.length - 1].content;
```


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#viewing-the-trace) Viewing the trace


**Details view**
Click on the trace, and toggle to the **Details** view on the top right. Your trace in LangSmith should [look like this](https://smith.langchain.com/public/79061a0f-c602-4012-b022-03fd46bce89e/r).
**Trajectory view**
The **Trajectory** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace (including the user’s initial request, tool calls, and the agent’s final response) and represents them in a chat-like format.


## [​](https://docs.langchain.com/langsmith/trace-with-langgraph#without-langchain) Without LangChain


If you are using other SDKs or custom functions within LangGraph, you will need to [wrap or decorate them appropriately](https://docs.langchain.com/langsmith/annotate-code#use-%40traceable-%2F-traceable) (with the `@traceable` decorator in Python or the `traceable` function in JS, or something like e.g. `wrap_openai` for SDKs). If you do so, LangSmith will automatically nest traces from those wrapped methods.
Here’s an example. You can also see this page for more information.


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#1-installation-2) 1. Installation


Install the LangGraph library and the OpenAI SDK for Python and JS (we use the OpenAI integration for the code snippets below).
pip yarn npm pnpm

```
pip install openai langsmith langgraph
```


```
yarn add openai langsmith @langchain/langgraph
```


```
npm install openai langsmith @langchain/langgraph
```


```
pnpm add openai langsmith @langchain/langgraph
```


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#2-configure-your-environment-2) 2. Configure your environment


```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>
```


If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won’t be recognized and requests will fail to authenticate.

| Region |
| --- |
| GCP US |
| GCP EU |
| GCP APAC |
| AWS US |

For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency: `export LANGCHAIN_CALLBACKS_BACKGROUND=true` If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends: `export LANGCHAIN_CALLBACKS_BACKGROUND=false` See [this LangChain.js guide](https://js.langchain.com/docs/how_to/callbacks_serverless) for more information.


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#3-log-a-trace-2) 3. Log a trace


Once you’ve set up your environment, [wrap or decorate the custom functions/SDKs](https://docs.langchain.com/langsmith/annotate-code#use-%40traceable-%2F-traceable) you want to trace. LangSmith will then infer the proper tracing config:
Python TypeScript

```
import json
import openai
import operator
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph

class State(TypedDict):
    messages: Annotated[list, operator.add]

tool_schema = {
    "type": "function",
    "function": {
        "name": "search",
        "description": "Call to surf the web.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
}

# Decorating the tool function will automatically trace it with the correct context
@traceable(run_type="tool", name="Search Tool")
def search(query: str):
    """Call to surf the web."""
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."

tools = [search]

def call_tools(state):
    function_name_to_function = {"search": search}
    messages = state["messages"]
    tool_call = messages[-1]["tool_calls"][0]
    function_name = tool_call["function"]["name"]
    function_arguments = tool_call["function"]["arguments"]
    arguments = json.loads(function_arguments)
    function_response = function_name_to_function[function_name](**arguments)
    tool_message = {
        "tool_call_id": tool_call["id"],
        "role": "tool",
        "name": function_name,
        "content": function_response,
    }
    return {"messages": [tool_message]}

wrapped_client = wrap_openai(openai.Client())

def should_continue(state: State) -> Literal["tools", "__end__"]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message["tool_calls"]:
        return "tools"
    return "__end__"

def call_model(state: State):
    messages = state["messages"]
    # Calling the wrapped client will automatically infer the correct tracing context
    response = wrapped_client.chat.completions.create(
        messages=messages, model="gpt-6-luna", tools=[tool_schema]
    )
    raw_tool_calls = response.choices[0].message.tool_calls
    tool_calls = [tool_call.to_dict() for tool_call in raw_tool_calls] if raw_tool_calls else []
    response_message = {
        "role": "assistant",
        "content": response.choices[0].message.content,
        "tool_calls": tool_calls,
    }
    return {"messages": [response_message]}

workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_node("tools", call_tools)
workflow.add_edge("__start__", "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
)
workflow.add_edge("tools", 'agent')

app = workflow.compile()

final_state = app.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

final_state["messages"][-1]["content"]
```


```
**Note:** The below example requires `langsmith>=0.1.39` and `@langchain/langgraph>=0.0.31`

import OpenAI from "openai";
import { StateGraph } from "@langchain/langgraph";
import { wrapOpenAI } from "langsmith/wrappers/openai";
import { traceable } from "langsmith/traceable";

type GraphState = {
  messages: OpenAI.ChatCompletionMessageParam[];
};

const wrappedClient = wrapOpenAI(new OpenAI({}));

const toolSchema: OpenAI.ChatCompletionTool = {
  type: "function",
  function: {
    name: "search",
    description: "Use this tool to query the web.",
    parameters: {
      type: "object",
      properties: {
        query: {
          type: "string",
        },
      },
      required: ["query"],
    }
  }
};

// Wrapping the tool function will automatically trace it with the correct context
const search = traceable(async ({ query }: { query: string }) => {
  if (
    query.toLowerCase().includes("sf") ||
    query.toLowerCase().includes("san francisco")
  ) {
    return "It's 60 degrees and foggy.";
  }
  return "It's 90 degrees and sunny.";
}, { run_type: "tool", name: "Search Tool" });

const callTools = async ({ messages }: GraphState) => {
  const mostRecentMessage = messages[messages.length - 1];
  const toolCalls = (mostRecentMessage as OpenAI.ChatCompletionAssistantMessageParam).tool_calls;
  if (toolCalls === undefined || toolCalls.length === 0) {
    throw new Error("No tool calls passed to node.");
  }
  const toolNameMap = {
    search,
  };
  const functionName = toolCalls[0].function.name;
  const functionArguments = JSON.parse(toolCalls[0].function.arguments);
  const response = await toolNameMap[functionName](functionArguments);
  const toolMessage = {
    tool_call_id: toolCalls[0].id,
    role: "tool",
    name: functionName,
    content: response,
  }
  return { messages: [toolMessage] };
};

const callModel = async ({ messages }: GraphState) => {
  // Calling the wrapped client will automatically infer the correct tracing context
  const response = await wrappedClient.chat.completions.create({
    messages,
    model: "gpt-6-luna",
    tools: [toolSchema],
  });
  const responseMessage = {
    role: "assistant",
    content: response.choices[0].message.content,
    tool_calls: response.choices[0].message.tool_calls ?? [],
  };
  return { messages: [responseMessage] };
};

const shouldContinue = ({ messages }: GraphState) => {
  const lastMessage =
    messages[messages.length - 1] as OpenAI.ChatCompletionAssistantMessageParam;
  if (
    lastMessage?.tool_calls !== undefined &&
    lastMessage?.tool_calls.length > 0
  ) {
    return "tools";
  }
  return "__end__";
}

const workflow = new StateGraph<GraphState>({
  channels: {
    messages: {
      reducer: (a: any, b: any) => a.concat(b),
    }
  }
});

const graph = workflow
  .addNode("model", callModel)
  .addNode("tools", callTools)
  .addEdge("__start__", "model")
  .addConditionalEdges("model", shouldContinue, {
    tools: "tools",
    __end__: "__end__",
  })
  .addEdge("tools", "model")
  .compile();

await graph.invoke({
  messages: [{ role: "user", content: "what is the weather in sf" }]
});
```


### [​](https://docs.langchain.com/langsmith/trace-with-langgraph#viewing-the-trace-2) Viewing the trace


**Details view**
Click on the trace, and toggle to the **Details** view on the top right. Your trace in LangSmith should [look like this](https://smith.langchain.com/public/c3d128fa-c618-4b0e-b9d0-ccbb619440d8/r).
**Trajectory view**
The **Trajectory** view in the LangSmith UI shows a simplified conversation history between the user and the agent. This view pulls messages from the top-level trace (including the user’s initial request, tool calls, and the agent’s final response) and represents them in a chat-like format.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-langgraph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​With LangChain
## ​Without LangChain




Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenAI Agents SDK applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk`

# Trace OpenAI Agents SDK applications
## Documentation Index
## ​Installation
## ​Environment configuration
## ​Quick start
## ​Configure the processor
## ​Nest traceable calls in tools
## ​Flush traces in serverless environments








Trace OpenAI Agents SDK Python and JavaScript applications with LangSmith.

The OpenAI Agents SDK lets you build agentic applications powered by OpenAI models.
Use LangSmith to trace OpenAI Agents SDK runs, including agent steps, model calls, tool calls, and handoffs.


- Python
- JavaScript


## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#installation) Installation

Requires Python SDK version `langsmith>=0.3.15`. Install LangSmith with OpenAI Agents support: pip uv

```
pip install "langsmith[openai-agents]"
```


```
uv add "langsmith[openai-agents]"
```

This installs both the LangSmith library and the OpenAI Agents SDK.

## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#environment-configuration) Environment configuration

Shell

```
export LANGSMITH_API_KEY=<your-api-key>
export OPENAI_API_KEY=<your-openai-api-key>

# Optional: set a project for your traces
export LANGSMITH_PROJECT=<your-project-name>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#quick-start) Quick start

Integrate LangSmith tracing with the OpenAI Agents SDK by using the `OpenAIAgentsTracingProcessor` class.

```
import asyncio

from agents import Agent, Runner, set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor


async def main():
    agent = Agent(
        name="Captain Obvious",
        instructions="You are Captain Obvious, the world's most literal technical support agent.",
    )

    question = "Why is my code failing when I try to divide by zero? I keep getting this error message."
    result = await Runner.run(agent, question)
    print(result.final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
```

The agent’s execution flow, including spans and their details, is logged to LangSmith.

## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#installation-2) Installation

Requires JS SDK version `langsmith>=0.5.25`. Install LangSmith and the OpenAI Agents SDK: npm yarn pnpm

```
npm install langsmith @openai/agents zod
```


```
yarn add langsmith @openai/agents zod
```


```
pnpm add langsmith @openai/agents zod
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#environment-configuration-2) Environment configuration

Shell

```
export LANGSMITH_API_KEY=<your-api-key>
export OPENAI_API_KEY=<your-openai-api-key>

# Optional: set a project for your traces
export LANGSMITH_PROJECT=<your-project-name>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```

Installing `OpenAIAgentsTracingProcessor` is an explicit opt-in to tracing. The processor posts traces even when `LANGSMITH_TRACING` is not set, and nested `traceable` calls inside agent tools inherit the active trace context.

## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#quick-start-2) Quick start

Register `OpenAIAgentsTracingProcessor` with the OpenAI Agents SDK before running agents.

```
import { Agent, run, setTraceProcessors, tool } from "@openai/agents";
import { z } from "zod";

import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

setTraceProcessors([new OpenAIAgentsTracingProcessor()]);

const getWeather = tool({
  name: "get_weather",
  description: "Get the current weather for a city",
  parameters: z.object({
    city: z.string().describe("The city to get weather for"),
  }),
  execute: async ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
});

const agent = new Agent({
  name: "WeatherAgent",
  instructions: "You are a helpful assistant. Use the get_weather tool when asked about weather.",
  model: "gpt-6-luna",
  tools: [getWeather],
});

const result = await run(agent, "What's the weather in San Francisco?");
console.log(result.finalOutput);
```

The resulting trace contains the root agent run, response spans, and nested tool call spans.

## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#configure-the-processor) Configure the processor

Pass options to the processor to set a LangSmith client, project, tags, metadata, or root trace name.

```
import { Agent, run, setTraceProcessors } from "@openai/agents";

import { Client } from "langsmith";
import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

const client = new Client();
const processor = new OpenAIAgentsTracingProcessor({
  client,
  projectName: "openai-agents-demo",
  name: "Support agent workflow",
  tags: ["openai-agents"],
  metadata: {
    environment: "development",
  },
});

setTraceProcessors([processor]);

const agent = new Agent({
  name: "SupportAgent",
  instructions: "You are a concise support agent.",
  model: "gpt-6-luna",
});

const result = await run(agent, "Help me reset my password.");
console.log(result.finalOutput);
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#nest-traceable-calls-in-tools) Nest `traceable` calls in tools

You can use `traceable` inside OpenAI Agents SDK tool handlers. LangSmith nests those runs under the active tool span.

```
import { Agent, run, setTraceProcessors, tool } from "@openai/agents";
import { z } from "zod";

import { traceable } from "langsmith/traceable";
import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

setTraceProcessors([new OpenAIAgentsTracingProcessor()]);

const lookupOrder = traceable(
  async (orderId: string) => {
    return { orderId, status: "shipped" };
  },
  { name: "lookup_order" }
);

const orderStatus = tool({
  name: "order_status",
  description: "Look up the status of an order",
  parameters: z.object({
    orderId: z.string().describe("The order ID to look up"),
  }),
  execute: async ({ orderId }: { orderId: string }) => {
    return JSON.stringify(await lookupOrder(orderId));
  },
});

const agent = new Agent({
  name: "OrdersAgent",
  instructions: "Use the order_status tool to answer order questions.",
  model: "gpt-6-luna",
  tools: [orderStatus],
});

await run(agent, "Where is order 123?");
```


## [​](https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk#flush-traces-in-serverless-environments) Flush traces in serverless environments

When tracing in serverless environments, flush pending traces before the process exits.

```
import { Agent, run, setTraceProcessors } from "@openai/agents";

import { Client } from "langsmith";
import { OpenAIAgentsTracingProcessor } from "langsmith/wrappers/openai_agents";

const client = new Client();
const processor = new OpenAIAgentsTracingProcessor({ client });
setTraceProcessors([processor]);

try {
  const agent = new Agent({
    name: "SupportAgent",
    instructions: "You are a concise support agent.",
    model: "gpt-6-luna",
  });

  const result = await run(agent, "Help me reset my password.");
  console.log(result.finalOutput);
} finally {
  await processor.forceFlush();
}
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-openai-agents-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Microsoft Agent Framework applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework`

# Trace Microsoft Agent Framework applications

LangSmith can capture traces generated by [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) using its built-in OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your Microsoft Agent Framework agents and send them to LangSmith for monitoring and analysis.


## [​](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework#installation) Installation


Install the required packages:
pip uv

```
pip install agent-framework opentelemetry-exporter-otlp-proto-http
```


```
uv add agent-framework opentelemetry-exporter-otlp-proto-http
```


## [​](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework#1-configure-environment-variables) 1. Configure environment variables


Enable OpenTelemetry instrumentation of the agent and set the OpenTelemetry environment variables to point to the LangSmith OTEL endpoint:


```
export ENABLE_INSTRUMENTATION=true
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.smith.langchain.com/otel/v1/traces
export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your_langsmith_api_key>,Langsmith-Project=<your_project_name>"
```


### [​](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework#2-enable-opentelemetry-in-your-application) 2. Enable OpenTelemetry in your application


In your Microsoft Agent Framework application, enable OpenTelemetry tracing using the built-in `configure_otel_providers` function:


```
from agent_framework.observability import configure_otel_providers

# Enable OpenTelemetry tracing
configure_otel_providers(enable_sensitive_data=True)
```


Setting `enable_sensitive_data=True` allows capturing input and output content in traces. Set to `False` if you want to exclude sensitive data from traces.


### [​](https://docs.langchain.com/langsmith/trace-with-microsoft-agent-framework#3-create-and-run-your-agent) 3. Create and run your agent


Once configured, your Microsoft Agent Framework agents will automatically send traces to LangSmith:


```
from agent_framework import ChatAgent
from agent_framework.observability import configure_otel_providers
from agent_framework.openai import OpenAIChatClient

# Enable OpenTelemetry tracing
configure_otel_providers(enable_sensitive_data=True)


agent = ChatAgent(
    chat_client=OpenAIChatClient(model_id="gpt-6-luna"),
)

result = await agent.run("What's the capital of Bavaria?")
print(result.text)
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-microsoft-agent-framework.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup




Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace with OpenTelemetry - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-opentelemetry`

# Trace with OpenTelemetry
## Documentation Index
## ​How OTel tracing works
## ​Trace a LangChain application
## ​Trace a non-LangChain application
## ​Send traces to an alternate provider
## ​Supported OpenTelemetry attribute and event mapping
## ​Implementation examples
## ​Advanced configuration









Configure OpenTelemetry tracing in LangSmith, including LANGSMITH_OTEL_ENABLED and OTEL fanout with the OpenTelemetry Collector.

LangSmith supports OpenTelemetry-based tracing, allowing you to send traces from any OpenTelemetry-compatible application. This guide covers both automatic instrumentation for LangChain applications and manual instrumentation for other frameworks.
Learn how to trace your LLM applications using OpenTelemetry with LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#how-otel-tracing-works) How OTel tracing works


The following diagram shows the basic flow for OpenTelemetry tracing with LangSmith, including the fanout pattern where a single stream of spans is routed to multiple observability backends.

The OpenTelemetry SDK instruments your application code and emits spans. Spans travel via the OTLP protocol to an OpenTelemetry Collector, which batches and routes them to one or more destinations simultaneously  (*fanout*). LangSmith receives spans at its OTLP endpoint and displays them as traces in the dashboard.
Update the LangSmith URL appropriately for self-hosted installations or regional SaaS in the requests below: GCP EU uses `eu.api.smith.langchain.com`; GCP APAC uses `apac.api.smith.langchain.com`; AWS US uses `aws.api.smith.langchain.com`.


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#trace-a-langchain-application) Trace a LangChain application


If you’re using LangChain or LangGraph, use the built-in integration to trace your application:


1. Install the LangSmith package with OpenTelemetry support: pip ``` pip install "langsmith[otel]" pip install langchain ``` Requires Python SDK version `langsmith>=0.3.18`. We recommend `langsmith>=0.4.25` to benefit from important OpenTelemetry fixes.
2. In your LangChain/LangGraph App, enable the OpenTelemetry integration by setting the `LANGSMITH_OTEL_ENABLED` environment variable: Shell ``` LANGSMITH_OTEL_ENABLED=true LANGSMITH_TRACING=true LANGSMITH_ENDPOINT=https://api.smith.langchain.com LANGSMITH_API_KEY=<your_langsmith_api_key> # For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use. ```
3. Create a LangChain application with tracing. For example: ``` import os from langchain_openai import ChatOpenAI from langchain_core.prompts import ChatPromptTemplate # Create a chain prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}") model = ChatOpenAI() chain = prompt | model # Run the chain result = chain.invoke({"topic": "programming"}) print(result.content) ```
4. View the traces in your LangSmith dashboard ([example](https://smith.langchain.com/public/a762af6c-b67d-4f22-90a0-728df16baeba/r)) once your application runs.


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#trace-a-non-langchain-application) Trace a non-LangChain application


For non-LangChain applications or custom instrumentation, you can trace your application in LangSmith with a standard OpenTelemetry client. (We recommend **langsmith ≥ 0.4.25**.)


1. Install the OpenTelemetry SDK, OpenTelemetry exporter packages, as well as the OpenAI package: pip ``` pip install openai pip install opentelemetry-sdk pip install opentelemetry-exporter-otlp ```
2. Setup environment variables for the endpoint, substitute your specific values: Shell ``` OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your langsmith api key>" ``` `OTEL_EXPORTER_OTLP_ENDPOINT` is a base URL. OTLP/HTTP exporters append the signal path (`/v1/traces`) themselves, so do not include it: setting the base endpoint to `https://api.smith.langchain.com/otel/v1/traces` sends traces to `/otel/v1/traces/v1/traces`, which returns `404`. Include the full path only with the per-signal `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` variable or a collector exporter’s `traces_endpoint`, which are used exactly as given. If you’re self-hosting LangSmith, replace the base endpoint with your LangSmith api endpoint and append `/api/v1`. For example: `OTEL_EXPORTER_OTLP_ENDPOINT=https://ai-company.com/api/v1/otel` Optional: Specify a custom project name other than “default”: Shell ``` OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your langsmith api key>,Langsmith-Project=<project name>" ``` **Agent-based workspaces.** Agent addressing is not yet available on the OTLP path, which reads no agent address from a request or a span. Use the `Langsmith-Project` header to name the tracing project, whichever way your workspace is organized. For the addressing model, see [Log traces to an agent](https://docs.langchain.com/langsmith/log-traces-to-agent).
3. Log a trace. This code sets up an OTEL tracer and exporter that will send traces to LangSmith. It then calls OpenAI and sends the required OpenTelemetry attributes. ``` from openai import OpenAI from opentelemetry import trace from opentelemetry.sdk.trace import TracerProvider from opentelemetry.sdk.trace.export import ( BatchSpanProcessor, ) from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) otlp_exporter = OTLPSpanExporter( timeout=10, ) trace.set_tracer_provider(TracerProvider()) trace.get_tracer_provider().add_span_processor( BatchSpanProcessor(otlp_exporter) ) tracer = trace.get_tracer(__name__) def call_openai(): model = "gpt-6-luna" with tracer.start_as_current_span("call_open_ai") as span: span.set_attribute("langsmith.span.kind", "LLM") span.set_attribute("langsmith.metadata.user_id", "user_123") span.set_attribute("gen_ai.system", "OpenAI") span.set_attribute("gen_ai.request.model", model) span.set_attribute("llm.request.type", "chat") messages = [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": "Write a haiku about recursion in programming." } ] for i, message in enumerate(messages): span.set_attribute(f"gen_ai.prompt.{i}.content", str(message["content"])) span.set_attribute(f"gen_ai.prompt.{i}.role", str(message["role"])) completion = client.chat.completions.create( model=model, messages=messages ) span.set_attribute("gen_ai.response.model", completion.model) span.set_attribute("gen_ai.completion.0.content", str(completion.choices[0].message.content)) span.set_attribute("gen_ai.completion.0.role", "assistant") span.set_attribute("gen_ai.usage.prompt_tokens", completion.usage.prompt_tokens) span.set_attribute("gen_ai.usage.completion_tokens", completion.usage.completion_tokens) span.set_attribute("gen_ai.usage.total_tokens", completion.usage.total_tokens) return completion.choices[0].message if __name__ == "__main__": call_openai() ```
4. View the trace in your LangSmith dashboard ([example](https://smith.langchain.com/public/4f2890b1-f105-44aa-a6cf-c777dcc27a37/r)).


If your spans reference a parent from another service or process, see [Context propagation in distributed tracing](https://docs.langchain.com/langsmith/trace-with-opentelemetry#context-propagation-in-distributed-tracing) for how parent–child linking works and when a span can be dropped.


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#send-traces-to-an-alternate-provider) Send traces to an alternate provider


While LangSmith is the default destination for OpenTelemetry traces, you can also configure OpenTelemetry to send traces to other observability platforms.
Available in LangSmith Python SDK **≥ 0.4.1**. We recommend **≥ 0.4.25** for fixes that improve OTEL export and hybrid fan-out stability.


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#use-environment-variables-for-global-configuration) Use environment variables for global configuration


By default, the LangSmith OpenTelemetry exporter will send data to the LangSmith API OTEL endpoint, but this can be customized by setting standard OTEL environment variables:


```
OTEL_EXPORTER_OTLP_ENDPOINT: Override the endpoint URL
OTEL_EXPORTER_OTLP_HEADERS: Headers for your endpoint, like its API key (if unset, your LangSmith API key and project are sent)
OTEL_SERVICE_NAME: Set a custom service name (defaults to "langsmith")
OTEL_RESOURCE_ATTRIBUTES: Attach custom metadata fields at the process level (see below)
```


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#add-process-level-resource-attributes) Add process-level resource attributes


You can attach custom metadata to every trace emitted by a process using the standard OpenTelemetry `OTEL_RESOURCE_ATTRIBUTES` environment variable. Unlike span-level attributes (set per-span in code), resource attributes are set once at the process level and automatically propagated to all spans. This makes them ideal for any custom metadata you want to tag your traces with, such as a username, request ID, environment, or deployment version.
The value is a comma-separated list of `key=value` pairs:


```
OTEL_RESOURCE_ATTRIBUTES="username=abc,id=1,environment=production"
```


You can use any custom keys you like, or follow the [OpenTelemetry resource semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/) for standard fields such as `deployment.environment`, `service.version`, and `cloud.region`.
These attributes appear in LangSmith under the trace’s metadata, which you can use to filter and group traces across your workspace.
LangSmith uses the HTTP trace exporter by default. If you’d like to use your own tracing provider, you can either:


1. Set the OTEL environment variables as shown above, or
2. Set a global trace provider before initializing LangChain components, which LangSmith will detect and use instead of creating its own.


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#configure-alternate-otlp-endpoints) Configure alternate OTLP endpoints


To send traces to a different provider, configure the OTLP exporter with your provider’s endpoint:


```
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Set environment variables for LangChain
os.environ["LANGSMITH_OTEL_ENABLED"] = "true"
os.environ["LANGSMITH_TRACING"] = "true"

# Configure the OTLP exporter for your custom endpoint
provider = TracerProvider()
otlp_exporter = OTLPSpanExporter(
    # Change to your provider's endpoint
    endpoint="https://otel.your-provider.com/v1/traces",
    # Add any required headers for authentication
    headers={"api-key": "your-api-key"},
)
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Create and run a LangChain application
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI()
chain = prompt | model
result = chain.invoke({"topic": "programming"})
print(result.content)
```


Hybrid tracing is available in version **≥ 0.4.1**. To send traces **only** to your OTEL endpoint, set: `LANGSMITH_OTEL_ONLY="true"`
(Recommendation: use **langsmith ≥ 0.4.25**.)


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#supported-opentelemetry-attribute-and-event-mapping) Supported OpenTelemetry attribute and event mapping


When sending traces to LangSmith via OpenTelemetry, the following attributes are mapped to LangSmith fields:


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#core-langsmith-attributes) Core LangSmith attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `langsmith.trace.name` | Run name | Overrides the span name for the run |
| `langsmith.span.kind` | [Run type](https://docs.langchain.com/langsmith/run-data-format#run-types) | Values: `llm`, `chain`, `tool`, `retriever`, `embedding`, `prompt`, `parser` |
| `langsmith.trace.id` | Trace ID | The trace (root run) the span belongs to; set to attach to an existing trace |
| `langsmith.span.id` | Run ID | This span’s run ID (a UUID); overrides the ID derived from the OTLP span ID |
| `langsmith.span.parent_id` | Parent run ID | Nests the span under an existing run by its run ID |
| `langsmith.span.dotted_order` | Dotted order | Position in the trace tree: `<parent.dotted_order>.<timestamp><span.id>`. See [`dotted_order`](https://docs.langchain.com/langsmith/run-data-format#what-is-dotted_order). |
| `langsmith.trace.session_id` | Session ID | Session identifier for related traces |
| `langsmith.trace.session_name` | Session name | Name of the session |
| `langsmith.span.tags` | Tags | Custom tags attached to the span (comma-separated) |
| `langsmith.metadata.{key}` | `metadata.{key}` | Custom metadata with langsmith prefix |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#genai-standard-attributes) GenAI standard attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `gen_ai.system` | `metadata.ls_provider` | The GenAI system (e.g., “openai”, “anthropic”) |
| `gen_ai.operation.name` | Run type | Maps “chat”/“completion” to “llm”, “embedding” to “embedding” |
| `gen_ai.prompt` | `inputs` | The input prompt sent to the model |
| `gen_ai.completion` | `outputs` | The output generated by the model |
| `gen_ai.prompt.{n}.role` | `inputs.messages[n].role` | Role for the nth input message |
| `gen_ai.prompt.{n}.content` | `inputs.messages[n].content` | Content for the nth input message |
| `gen_ai.prompt.{n}.message.role` | `inputs.messages[n].role` | Alternative format for role |
| `gen_ai.prompt.{n}.message.content` | `inputs.messages[n].content` | Alternative format for content |
| `gen_ai.completion.{n}.role` | `outputs.messages[n].role` | Role for the nth output message |
| `gen_ai.completion.{n}.content` | `outputs.messages[n].content` | Content for the nth output message |
| `gen_ai.completion.{n}.message.role` | `outputs.messages[n].role` | Alternative format for role |
| `gen_ai.completion.{n}.message.content` | `outputs.messages[n].content` | Alternative format for content |
| `gen_ai.input.messages` | `inputs.messages` | Array of input messages |
| `gen_ai.output.messages` | `outputs.messages` | Array of output messages |
| `gen_ai.tool.name` | `invocation_params.tool_name` | Tool name, also sets run type to “tool” |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#genai-request-parameters) GenAI request parameters


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `gen_ai.request.model` | `invocation_params.model` | The model name used for the request |
| `gen_ai.response.model` | `invocation_params.model` | The model name returned in the response |
| `gen_ai.request.temperature` | `invocation_params.temperature` | Temperature setting |
| `gen_ai.request.top_p` | `invocation_params.top_p` | Top-p sampling setting |
| `gen_ai.request.max_tokens` | `invocation_params.max_tokens` | Maximum tokens setting |
| `gen_ai.request.frequency_penalty` | `invocation_params.frequency_penalty` | Frequency penalty setting |
| `gen_ai.request.presence_penalty` | `invocation_params.presence_penalty` | Presence penalty setting |
| `gen_ai.request.seed` | `invocation_params.seed` | Random seed used for generation |
| `gen_ai.request.stop_sequences` | `invocation_params.stop` | Sequences that stop generation |
| `gen_ai.request.top_k` | `invocation_params.top_k` | Top-k sampling parameter |
| `gen_ai.request.encoding_formats` | `invocation_params.encoding_formats` | Output encoding formats |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#genai-usage-metrics) GenAI usage metrics


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `gen_ai.usage.input_tokens` | `usage_metadata.input_tokens` | Number of input tokens used |
| `gen_ai.usage.output_tokens` | `usage_metadata.output_tokens` | Number of output tokens used |
| `gen_ai.usage.total_tokens` | `usage_metadata.total_tokens` | Total number of tokens used. Not part of the current GenAI semantic conventions |
| `gen_ai.usage.cache_read.input_tokens` | `usage_metadata.input_token_details.cache_read` | Input tokens read from the provider cache |
| `gen_ai.usage.cache_write.input_tokens` | `usage_metadata.input_token_details.cache_creation` | Input tokens written to the provider cache |
| `gen_ai.usage.reasoning.output_tokens` | `usage_metadata.output_token_details.reasoning` | Number of reasoning tokens used |
| `gen_ai.usage.prompt_tokens` | `usage_metadata.input_tokens` | Number of input tokens used (deprecated) |
| `gen_ai.usage.completion_tokens` | `usage_metadata.output_tokens` | Number of output tokens used (deprecated) |
| `gen_ai.usage.cache_creation.input_tokens` | `usage_metadata.input_token_details.cache_creation` | Input tokens written to the provider cache (deprecated) |
| `gen_ai.usage.details.reasoning_tokens` | `usage_metadata.output_token_details.reasoning` | Number of reasoning tokens used (deprecated) |
| `gen_ai.usage.cache_read_input_tokens` | `usage_metadata.input_token_details.cache_read` | Input tokens read from the provider cache (OpenLLMetry spelling) |
| `gen_ai.usage.cache_creation_input_tokens` | `usage_metadata.input_token_details.cache_creation` | Input tokens written to the provider cache (OpenLLMetry spelling) |


If a span sets more than one attribute for the same cache or reasoning field, LangSmith uses the current semantic convention attribute first, then the deprecated dotted spelling, then the OpenLLMetry underscore spelling.


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#traceloop-attributes) TraceLoop attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `traceloop.entity.input` | `inputs` | Full input value from TraceLoop |
| `traceloop.entity.output` | `outputs` | Full output value from TraceLoop |
| `traceloop.entity.name` | Run name | Entity name from TraceLoop |
| `traceloop.span.kind` | Run type | Maps to LangSmith run types |
| `traceloop.llm.request.type` | Run type | ”embedding” maps to “embedding”, others to “llm” |
| `traceloop.association.properties.{key}` | `metadata.{key}` | Custom metadata with traceloop prefix |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#openinference-attributes) OpenInference attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `input.value` | `inputs` | Full input value, can be string or JSON |
| `output.value` | `outputs` | Full output value, can be string or JSON |
| `openinference.span.kind` | Run type | Maps various kinds to LangSmith run types |
| `llm.system` | `metadata.ls_provider` | LLM system provider |
| `llm.model_name` | `metadata.ls_model_name` | Model name from OpenInference |
| `tool.name` | Run name | Tool name when span kind is “TOOL” |
| `metadata` | `metadata.*` | JSON string of metadata to be merged |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#llm-attributes) LLM attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `llm.input_messages` | `inputs.messages` | Input messages |
| `llm.output_messages` | `outputs.messages` | Output messages |
| `llm.token_count.prompt` | `usage_metadata.input_tokens` | Prompt token count |
| `llm.token_count.completion` | `usage_metadata.output_tokens` | Completion token count |
| `llm.token_count.total` | `usage_metadata.total_tokens` | Total token count |
| `llm.usage.total_tokens` | `usage_metadata.total_tokens` | Alternative total token count |
| `llm.invocation_parameters` | `invocation_params.*` | JSON string of invocation parameters |
| `llm.presence_penalty` | `invocation_params.presence_penalty` | Presence penalty |
| `llm.frequency_penalty` | `invocation_params.frequency_penalty` | Frequency penalty |
| `llm.request.functions` | `invocation_params.functions` | Function definitions |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#prompt-template-attributes) Prompt template attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `llm.prompt_template.variables` | Run type | Sets run type to “prompt”, used with input.value |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#retriever-attributes) Retriever attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `retrieval.documents.{n}.document.content` | `outputs.documents[n].page_content` | Content of the nth retrieved document |
| `retrieval.documents.{n}.document.metadata` | `outputs.documents[n].metadata` | Metadata of the nth retrieved document (JSON) |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#tool-attributes) Tool attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `tools` | `invocation_params.tools` | Array of tool definitions |
| `tool_arguments` | `invocation_params.tool_arguments` | Tool arguments as JSON or key-value pairs |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#logfire-attributes) Logfire attributes


| OpenTelemetry attribute | LangSmith field | Notes |
| --- | --- | --- |
| `prompt` | `inputs` | Logfire prompt input |
| `all_messages_events` | `outputs` | Logfire message events output |
| `events` | `inputs` / `outputs` | Logfire events array, splits input/choice events |


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#opentelemetry-event-mapping) OpenTelemetry event mapping


| Event name | LangSmith field | Notes |
| --- | --- | --- |
| `gen_ai.content.prompt` | `inputs` | Extracts prompt content from event attributes |
| `gen_ai.content.completion` | `outputs` | Extracts completion content from event attributes |
| `gen_ai.system.message` | `inputs.messages[]` | System message in conversation |
| `gen_ai.user.message` | `inputs.messages[]` | User message in conversation |
| `gen_ai.assistant.message` | `outputs.messages[]` | Assistant message in conversation |
| `gen_ai.tool.message` | `outputs.messages[]` | Tool response message |
| `gen_ai.choice` | `outputs` | Model choice/response with finish reason |
| `exception` | `status`, `error` | Sets status to “error” and extracts exception message/stacktrace |


#### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#event-attribute-extraction) Event attribute extraction


For message events, the following attributes are extracted:


- `content` → message content
- `role` → message role
- `id` → tool_call_id (for tool messages)
- `gen_ai.event.content` → full message JSON


For choice events:


- `finish_reason` → choice finish reason
- `message.content` → choice message content
- `message.role` → choice message role
- `tool_calls.{n}.id` → tool call ID
- `tool_calls.{n}.function.name` → tool function name
- `tool_calls.{n}.function.arguments` → tool function arguments
- `tool_calls.{n}.type` → tool call type


For exception events:


- `exception.message` → error message
- `exception.stacktrace` → error stacktrace (appended to message)


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#implementation-examples) Implementation examples


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#trace-using-the-langsmith-sdk) Trace using the LangSmith SDK


Use the LangSmith SDK’s OpenTelemetry helper to configure export. The following example [traces a Google ADK agent](https://docs.langchain.com/langsmith/trace-with-google-adk):


```
import asyncio
from langsmith.integrations.otel import configure
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Configure LangSmith OpenTelemetry export (no OTEL env vars or headers needed)
configure(project_name="adk-otel-demo")


async def main():
    agent = LlmAgent(
        name="travel_assistant",
        model="gemini-3.8-flash",
        instruction="You are a helpful travel assistant.",
    )

    session_service = InMemorySessionService()
    runner = Runner(app_name="travel_app", agent=agent, session_service=session_service)

    user_id = "user_123"
    session_id = "session_abc"
    await session_service.create_session(app_name="travel_app", user_id=user_id, session_id=session_id)

    new_message = types.Content(parts=[types.Part(text="Hi! Recommend a weekend trip to Paris.")], role="user")

    for event in runner.run(user_id=user_id, session_id=session_id, new_message=new_message):
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
```


You do not need to set OTEL environment variables or exporters. `configure()` wires them for LangSmith automatically; instrumentors (like `GoogleADKInstrumentor`) create the spans.
Here is an [example](https://smith.langchain.com/public/d6d47eeb-511e-4fda-ad17-2caa7bd7150b/r) of what the resulting trace looks like in LangSmith.


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#link-opentelemetry-spans-to-a-langsmith-sdk-trace) Link OpenTelemetry spans to a LangSmith SDK trace


Native OTLP `parentSpanId` can’t reference an existing LangSmith run: an OTLP span ID is 8 bytes, while LangSmith run IDs are full UUIDs. To attach an OpenTelemetry span to a run created elsewhere (for example, a LangChain-SDK run), set the `langsmith.*` attributes with the parent’s full UUIDs. They override the IDs derived from the native OTLP span, so the span nests under the existing run in the same trace.


```
from langsmith import uuid7
from datetime import datetime, timezone

from langsmith import get_current_run_tree, traceable
from opentelemetry import trace

tracer = trace.get_tracer("my-harness")


def emit_otel_child(parent):
    """Emit an OTel span that nests under an existing LangSmith run."""
    child_id = uuid7()
    start = datetime.now(timezone.utc)
    # dotted_order = parent's dotted_order, a dot, then this span's timestamp + id
    dotted = f"{parent.dotted_order}.{start.strftime('%Y%m%dT%H%M%S%fZ')}{child_id}"

    with tracer.start_as_current_span("otel-child") as span:
        span.set_attribute("langsmith.trace.id", str(parent.trace_id))           # same trace
        span.set_attribute("langsmith.span.parent_id", str(parent.id))           # nest under parent
        span.set_attribute("langsmith.span.id", str(child_id))                   # this span's run id
        span.set_attribute("langsmith.span.dotted_order", dotted)                # position in the tree
        span.set_attribute("langsmith.trace.session_name", parent.session_name)  # same project
        # ... your instrumented work here ...


@traceable
def my_agent():
    parent = get_current_run_tree()  # the LangSmith run to nest under
    emit_otel_child(parent)
```


`langsmith.span.dotted_order` encodes the span’s position in the trace tree. Build it from the parent’s [`dotted_order`](https://docs.langchain.com/langsmith/run-data-format#what-is-dotted_order), a dot, then this span’s timestamp followed by its `langsmith.span.id`.


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#add-an-attachment-to-a-trace) Add an attachment to a trace


LangSmith supports [attaching files to traces](https://docs.langchain.com/langsmith/upload-files-with-traces). This is useful when building an agent with multimodal inputs or outputs. Attachments are also supported when tracing with OpenTelemetry.
The example below [traces a Google ADK agent](https://docs.langchain.com/langsmith/trace-with-google-adk) and adds an attachment to the trace. It uses a combination of LangSmith’s `OtelSpanProcessor` and a custom `AttachmentSpanProcessor` that uses [`on_end()`](https://opentelemetry-python.readthedocs.io/en/latest/sdk/trace.export.html#opentelemetry.sdk.trace.export.SimpleSpanProcessor.on_end) to add an image attachment to the parent span.


```
import asyncio
import base64
import json
from pathlib import Path
from dotenv import load_dotenv
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider, SpanProcessor
from langsmith.integrations.otel import OtelSpanProcessor


class AttachmentSpanProcessor(SpanProcessor):
    """Custom SpanProcessor to add attachments to invocation spans."""

    def __init__(self):
        self.attachment_data = None

    def set_attachment(self, attachment_data):
        self.attachment_data = attachment_data

    def on_end(self, span):
        if span.name == "invocation" and self.attachment_data:
            attachments_json = json.dumps([self.attachment_data])
            span._attributes["langsmith.attachments"] = attachments_json

load_dotenv()

# Set up TracerProvider manually
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Add attachment processor FIRST (runs before LangSmith processor)
attachment_processor = AttachmentSpanProcessor()
provider.add_span_processor(attachment_processor)

# Add LangSmith processor SECOND (receives already-modified spans)
langsmith_processor = OtelSpanProcessor(project="travel-assistant")
provider.add_span_processor(langsmith_processor)

def get_flight_info(destination: str, departure_date: str) -> dict:
    """Get flight information for a destination."""
    return {
        "destination": destination,
        "departure_date": departure_date,
        "price": "$450",
        "duration": "5h 30m",
        "airline": "Example Airways"
    }

def get_hotel_recommendations(city: str, check_in: str) -> dict:
    """Get hotel recommendations for a city."""
    return {
        "city": city,
        "check_in": check_in,
        "hotels": [
            {"name": "Grand Plaza Hotel", "rating": 4.5, "price": "$120/night"},
            {"name": "City Center Inn", "rating": 4.2, "price": "$95/night"}
        ]
    }

async def main():
    # Prepare the attachment
    receipt_path = Path("receipt-template-example.png")
    with open(receipt_path, "rb") as img_file:
        image_bytes = img_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("ascii")

    attachment_data = {
        "name": "receipt-template-example",
        "content": image_base64,
        "mime_type": "image/jpeg",
    }

    attachment_processor.set_attachment(attachment_data)

    # Create ADK agent
    agent = LlmAgent(
        name="travel_assistant",
        tools=[get_flight_info, get_hotel_recommendations],
        model="gemini-3.8-flash",
        instruction="You are a helpful travel assistant that can help with flights and hotels.",
    )

    # Set up session and runner
    session_service = InMemorySessionService()
    runner = Runner(
        app_name="travel_app",
        agent=agent,
        session_service=session_service
    )

    await session_service.create_session(
        app_name="travel_app",
        user_id="traveler_456",
        session_id="session_789"
    )

    # Send a message to the agent
    new_message = types.Content(
        parts=[types.Part(text="I need to book a flight to Paris for March 15th and find a good hotel.")],
        role="user",
    )

    # Run the agent and process events
    events = runner.run(
        user_id="traveler_456",
        session_id="session_789",
        new_message=new_message,
    )

    for event in events:
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
```


Here is an [example](https://smith.langchain.com/public/9574f70a-b893-49fe-8c62-691bd114bf14/r) of what the resulting trace looks like in LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#advanced-configuration) Advanced configuration


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#use-opentelemetry-collector-for-fan-out) Use OpenTelemetry collector for fan-out


Use `LANGSMITH_OTEL_ENABLED=true` when you need OTEL fanout. Configure your application to emit OTEL spans once, then use an OpenTelemetry Collector to route them to LangSmith and any additional observability backends.
Use this approach when you are tracing applications and want multi-destination routing. If you are operating LangSmith platform infrastructure telemetry (logs, metrics, traces from self-hosted LangSmith services on Kubernetes), use the [Configure your collector for LangSmith telemetry](https://docs.langchain.com/langsmith/langsmith-collector) guide instead.
For more advanced scenarios, you can use the OpenTelemetry Collector to fan out your telemetry data to multiple destinations. This is a more scalable approach than configuring multiple exporters in your application code.


1. [Install the OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/) for your environment.
2. Create a configuration file (e.g., `otel-collector-config.yaml`) that exports to multiple destinations: ``` receivers: otlp: protocols: grpc: endpoint: 0.0.0.0:4317 http: endpoint: 0.0.0.0:4318 processors: batch: exporters: otlphttp/langsmith: traces_endpoint: https://api.smith.langchain.com/otel/v1/traces headers: x-api-key: ${env:LANGSMITH_API_KEY} Langsmith-Project: my_project otlphttp/other_provider: traces_endpoint: https://otel.your-provider.com/v1/traces headers: api-key: ${env:OTHER_PROVIDER_API_KEY} service: pipelines: traces: receivers: [otlp] processors: [batch] exporters: [otlphttp/langsmith, otlphttp/other_provider] ```
3. Configure your application to send to the collector: ``` import os from opentelemetry import trace from opentelemetry.sdk.trace import TracerProvider from opentelemetry.sdk.trace.export import BatchSpanProcessor from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter from langchain_openai import ChatOpenAI from langchain_core.prompts import ChatPromptTemplate # Point to your local OpenTelemetry Collector otlp_exporter = OTLPSpanExporter( endpoint="http://localhost:4318/v1/traces" ) provider = TracerProvider() processor = BatchSpanProcessor(otlp_exporter) provider.add_span_processor(processor) trace.set_tracer_provider(provider) # Set environment variables for LangChain os.environ["LANGSMITH_OTEL_ENABLED"] = "true" os.environ["LANGSMITH_TRACING"] = "true" # Create and run a LangChain application prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}") model = ChatOpenAI() chain = prompt | model result = chain.invoke({"topic": "programming"}) print(result.content) ```


This approach offers several advantages:


- Centralized configuration for all your telemetry destinations
- Reduced overhead in your application code
- Better scalability and resilience
- Ability to add or remove destinations without changing application code


### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#distributed-tracing-with-langchain-and-opentelemetry) Distributed tracing with LangChain and OpenTelemetry


Distributed tracing is essential when your LLM application spans multiple services or processes. OpenTelemetry’s context propagation capabilities ensure that traces remain connected across service boundaries.


#### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#context-propagation-in-distributed-tracing) Context propagation in distributed tracing


In distributed systems, context propagation passes trace metadata between services so that related spans are linked to the same trace:


- **Trace ID**: A unique identifier for the entire trace
- **Span ID**: A unique identifier for the current span
- **Sampling Decision**: Indicates whether this trace should be sampled


**A span whose parent is never sent to LangSmith is dropped.** The OTel endpoint is asynchronous: it accepts a batch, returns `200`, and materializes runs in the background. When a span’s `parentSpanId` references a parent that LangSmith hasn’t received yet, the child is buffered and linked once the parent arrives. This works regardless of order; a child can arrive before its parent, in a separate request, and still link correctly. However, if the parent span is **never** exported to LangSmith, the buffered child expires and never appears as a run. LangSmith will not return an error, because the `200` was sent before processing. This commonly happens when only part of a distributed trace reaches LangSmith: the parent is emitted by a service that exports to a different backend, or it’s removed by a sampling decision. To avoid silent loss, make sure every span you want in LangSmith also has its ancestors exported to LangSmith within the buffering window. On self-hosted deployments, this window is controlled by `REDIS_RUNS_EXPIRY_SECONDS` (default 12 hours).


#### [​](https://docs.langchain.com/langsmith/trace-with-opentelemetry#set-up-distributed-tracing-with-langchain) Set up distributed tracing with LangChain


To enable distributed tracing across multiple services:


```
import os
from opentelemetry import trace
from opentelemetry.propagate import inject, extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import requests
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Set up OpenTelemetry trace provider
provider = TracerProvider()
otlp_exporter = OTLPSpanExporter(
    endpoint="https://api.smith.langchain.com/otel/v1/traces",
    headers={"x-api-key": os.getenv("LANGSMITH_API_KEY"), "Langsmith-Project": "my_project"}
)
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Service A: Create a span and propagate context to Service B
def service_a():
    with tracer.start_as_current_span("service_a_operation") as span:
        # Create a chain
        prompt = ChatPromptTemplate.from_template("Summarize: {text}")
        model = ChatOpenAI()
        chain = prompt | model

        # Run the chain
        result = chain.invoke({"text": "OpenTelemetry is an observability framework"})

        # Propagate context to Service B
        headers = {}
        inject(headers)  # Inject trace context into headers

        # Call Service B with the trace context
        response = requests.post(
            "http://service-b.example.com/process",
            headers=headers,
            json={"summary": result.content}
        )
        return response.json()

# Service B: Extract the context and continue the trace
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def service_b_endpoint():
    # Extract the trace context from the request headers
    context = extract(request.headers)
    with tracer.start_as_current_span("service_b_operation", context=context) as span:
        data = request.json
        summary = data.get("summary", "")

        # Process the summary with another LLM chain
        prompt = ChatPromptTemplate.from_template("Analyze the sentiment of: {text}")
        model = ChatOpenAI()
        chain = prompt | model
        result = chain.invoke({"text": summary})

        return jsonify({"analysis": result.content})

if __name__ == "__main__":
    app.run(port=5000)
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-opentelemetry.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace PydanticAI applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-pydantic-ai`

# Trace PydanticAI applications

LangSmith can capture traces generated by PydanticAI using its built-in OpenTelemetry instrumentation. This guide shows you how to automatically capture traces from your PydanticAI agents and send them to LangSmith for monitoring and analysis.


## [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#installation) Installation


Install the required packages:
pip uv

```
pip install langsmith pydantic-ai opentelemetry-exporter-otlp
```


```
uv add langsmith pydantic-ai opentelemetry-exporter-otlp
```


Requires LangSmith Python SDK version `langsmith>=0.4.26` for optimal OpenTelemetry support.


## [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#1-configure-environment-variables) 1. Configure environment variables


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```


### [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#2-configure-opentelemetry-integration) 2. Configure OpenTelemetry integration


In your PydanticAI application, configure the LangSmith OpenTelemetry integration:


```
from langsmith.integrations.otel import configure
from pydantic_ai import Agent

# Configure LangSmith tracing
configure(project_name="pydantic-ai-demo")

# Instrument all PydanticAI agents
Agent.instrument_all()
```


You do not need to set any OpenTelemetry environment variables or configure exporters manually— `configure()` handles everything automatically.


### [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#3-create-and-run-your-pydanticai-agent) 3. Create and run your PydanticAI agent


Once configured, your PydanticAI agents will automatically send traces to LangSmith:


```
from langsmith.integrations.otel import configure
from pydantic_ai import Agent

# Configure LangSmith tracing
configure(project_name="pydantic-ai-demo")

# Instrument all PydanticAI agents
Agent.instrument_all()

# Create and run an agent
agent = Agent('openai:gpt-6-luna')
result = agent.run_sync('What is the capital of France?')
print(result.output)
#> Paris
```


## [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#advanced-usage) Advanced usage


### [​](https://docs.langchain.com/langsmith/trace-with-pydantic-ai#custom-metadata-and-tags) Custom metadata and tags


You can add custom metadata to your traces using OpenTelemetry span attributes:


```
from opentelemetry import trace
from pydantic_ai import Agent
from langsmith.integrations.otel import configure

configure(project_name="pydantic-ai-metadata")
Agent.instrument_all()

tracer = trace.get_tracer(__name__)

agent = Agent('openai:gpt-6-luna')

with tracer.start_as_current_span("pydantic_ai_workflow") as span:
    span.set_attribute("langsmith.metadata.user_id", "user_123")
    span.set_attribute("langsmith.metadata.workflow_type", "question_answering")
    span.set_attribute("langsmith.span.tags", "pydantic-ai,production")

    result = agent.run_sync('Explain quantum computing in simple terms')
    print(result.output)
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-pydantic-ai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Advanced usage





Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Semantic Kernel applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-semantic-kernel`

# Trace Semantic Kernel applications

LangSmith can capture traces generated by [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) using its built-in OpenTelemetry support. This guide shows you how to automatically capture traces from your Semantic Kernel applications and send them to LangSmith for monitoring and analysis.


## [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#installation) Installation


Install the required packages using your preferred package manager:
pip uv

```
pip install langsmith semantic-kernel opentelemetry-instrumentation-openai
```


```
uv add langsmith semantic-kernel opentelemetry-instrumentation-openai
```


## [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#1-configure-environment-variables) 1. Configure environment variables


Set your [API keys](https://docs.langchain.com/langsmith/create-account-api-key) and project name:


```
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export OPENAI_API_KEY=<your_openai_api_key>
```


### [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#2-configure-opentelemetry-integration) 2. Configure OpenTelemetry integration


In your Semantic Kernel application, configure the LangSmith OpenTelemetry integration along with the OpenAI instrumentor:


```
from langsmith.integrations.otel import configure
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Configure LangSmith tracing
configure(project_name="semantic-kernel-demo")

# Instrument OpenAI calls
OpenAIInstrumentor().instrument()
```


You do not need to set any OpenTelemetry environment variables or configure exporters manually— `configure()` handles everything automatically.


### [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#3-create-and-run-your-semantic-kernel-application) 3. Create and run your Semantic Kernel application


Once configured, your Semantic Kernel application will automatically send traces to LangSmith:


```
import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.prompt_template import InputVariable, PromptTemplateConfig
from langsmith.integrations.otel import configure
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Configure LangSmith tracing
configure(project_name="semantic-kernel-assistant")

# Instrument OpenAI calls
OpenAIInstrumentor().instrument()

# Configure Semantic Kernel
kernel = Kernel()
kernel.add_service(OpenAIChatCompletion())

# Create a prompt template
code_analysis_prompt = """
Analyze the following code and provide insights:

Code: {{$code}}

Please provide:
1. A brief summary of what the code does
2. Any potential improvements
3. Code quality assessment
"""

prompt_template_config = PromptTemplateConfig(
    template=code_analysis_prompt,
    name="code_analyzer",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(name="code", description="The code to analyze", is_required=True),
    ],
)

# Add the function to the kernel
code_analyzer = kernel.add_function(
    function_name="analyzeCode",
    plugin_name="codeAnalysisPlugin",
    prompt_template_config=prompt_template_config,
)

async def main():
    sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    """

    result = await kernel.invoke(code_analyzer, code=sample_code)
    print("Code Analysis:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```


## [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#advanced-usage) Advanced usage


### [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#custom-metadata-and-tags) Custom metadata and tags


You can add custom metadata to your traces by setting span attributes:


```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

async def analyze_with_metadata(code: str):
    with tracer.start_as_current_span("semantic_kernel_workflow") as span:
        span.set_attribute("langsmith.metadata.workflow_type", "code_analysis")
        span.set_attribute("langsmith.metadata.user_id", "developer_123")
        span.set_attribute("langsmith.span.tags", "semantic-kernel,code-analysis")

        result = await kernel.invoke(code_analyzer, code=code)
        return result
```


### [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#combining-with-other-instrumentors) Combining with other instrumentors


You can combine Semantic Kernel tracing with other OpenTelemetry instrumentors:


```
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

# Initialize multiple instrumentors
OpenAIInstrumentor().instrument()
HTTPXClientInstrumentor().instrument()
```


## [​](https://docs.langchain.com/langsmith/trace-with-semantic-kernel#resources) Resources


- [Semantic Kernel documentation](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- [Semantic Kernel observability guide](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/observability/)
- [LangSmith OpenTelemetry guide](https://docs.langchain.com/langsmith/trace-with-opentelemetry)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-semantic-kernel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Installation
## ​Setup
## ​Advanced usage
## ​Resources






Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Vercel AI SDK applications (JS/TS only) - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk`

# Trace Vercel AI SDK applications (JS/TS only
## Documentation Index
## ​Installation
## ​Environment configuration
## ​Basic setup
## ​Tracing in serverless environments
## ​Passing LangSmith config
## ​Redacting data








Trace Vercel AI SDK applications with LangSmith for AI SDK v5, v6, and v7.

You can use LangSmith to trace runs from the Vercel AI SDK. This guide shows you how to set up tracing for AI SDK v5, v6, and v7.


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#installation) Installation


Install the Vercel AI SDK, a model provider package, and LangSmith. This guide uses Vercel’s OpenAI integration for the following code snippets, but you can use any other Vercel AI SDK provider.


- AI SDK v7
- AI SDK v5 and v6

`LangSmithTelemetry` requires AI SDK v7 and is available in `langsmith>=0.7.2`. npm yarn pnpm

```
npm install ai @ai-sdk/openai zod langsmith
```


```
yarn add ai @ai-sdk/openai zod langsmith
```


```
pnpm add ai @ai-sdk/openai zod langsmith
```

`wrapAISDK` supports AI SDK v6 and requires `langsmith>=0.3.63`. If you are using an older version of the AI SDK or `langsmith`, refer to the [OpenTelemetry (OTEL) based approach](https://docs.langchain.com/langsmith/legacy-trace-with-vercel-ai-sdk). npm yarn pnpm

```
npm install ai @ai-sdk/openai zod langsmith
```


```
yarn add ai @ai-sdk/openai zod langsmith
```


```
pnpm add ai @ai-sdk/openai zod langsmith
```


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#environment-configuration) Environment configuration


Shell

```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>

# The examples use OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#basic-setup) Basic setup


- AI SDK v7
- AI SDK v5 and v6

Register `LangSmithTelemetry` once, then use AI SDK methods as you normally would.

```
import { openai } from "@ai-sdk/openai";
import { generateText, registerTelemetry } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";

registerTelemetry(LangSmithTelemetry());

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

You should see a trace in your LangSmith dashboard [like this one](https://smith.langchain.com/public/4f0e689e-c801-44d3-8857-93b47ab100cc/r). You can also trace runs with tool calls:

```
import { openai } from "@ai-sdk/openai";
import { generateText, registerTelemetry, stepCountIs, tool } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";
import { z } from "zod";

registerTelemetry(LangSmithTelemetry());

await generateText({
    model: openai("gpt-6-luna"),
    messages: [
        {
            role: "user",
            content: "What are my orders and where are they? My user ID is 123",
        },
    ],
    tools: {
        listOrders: tool({
            description: "list all orders",
            inputSchema: z.object({ userId: z.string() }),
            execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
        }),
        viewTrackingInformation: tool({
            description: "view tracking information for a specific order",
            inputSchema: z.object({ orderId: z.string() }),
            execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
        }),
    },
    stopWhen: stepCountIs(5),
});
```

Which results in a trace like [this one](https://smith.langchain.com/public/6075fa2c-d255-4885-a66a-4fc798afaa9f/r). Wrap the AI SDK methods once with `wrapAISDK`, then call the wrapped methods as you normally would.

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText } = wrapAISDK(ai);

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

You can also trace runs with tool calls:

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { wrapAISDK } from "langsmith/experimental/vercel";
import { z } from "zod";

const { generateText, tool } = wrapAISDK(ai);

await generateText({
    model: openai("gpt-6-luna"),
    messages: [
        {
            role: "user",
            content: "What are my orders and where are they? My user ID is 123",
        },
    ],
    tools: {
        listOrders: tool({
            description: "list all orders",
            parameters: z.object({ userId: z.string() }),
            execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
        }),
        viewTrackingInformation: tool({
            description: "view tracking information for a specific order",
            parameters: z.object({ orderId: z.string() }),
            execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
        }),
    },
    maxSteps: 5,
});
```


You can use other AI SDK methods exactly as you usually would.


### [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#with-traceable) With `traceable`


You can wrap `traceable` calls around AI SDK calls or within AI SDK tool calls. This is useful if you want to group runs together in LangSmith.


- AI SDK v7
- AI SDK v5 and v6


```
import { openai } from "@ai-sdk/openai";
import { generateText, registerTelemetry, stepCountIs, tool } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

registerTelemetry(LangSmithTelemetry());

const wrapper = traceable(
    async (input: string) => {
        const { text } = await generateText({
            model: openai("gpt-6-luna"),
            messages: [
                {
                    role: "user",
                    content: input,
                },
            ],
            tools: {
                listOrders: tool({
                    description: "list all orders",
                    inputSchema: z.object({ userId: z.string() }),
                    execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
                }),
                viewTrackingInformation: tool({
                    description: "view tracking information for a specific order",
                    inputSchema: z.object({ orderId: z.string() }),
                    execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
                }),
            },
            stopWhen: stepCountIs(5),
        });
        return text;
    },
    { name: "wrapper" },
);

await wrapper("What are my orders and where are they? My user ID is 123.");
```

The resulting trace will look [like this](https://smith.langchain.com/public/ff25bc26-9389-4798-8b91-2bdcc95d4a8e/r).

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { wrapAISDK } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

const { generateText, tool } = wrapAISDK(ai);

const wrapper = traceable(
    async (input: string) => {
        const { text } = await generateText({
            model: openai("gpt-6-luna"),
            messages: [
                {
                    role: "user",
                    content: input,
                },
            ],
            tools: {
                listOrders: tool({
                    description: "list all orders",
                    parameters: z.object({ userId: z.string() }),
                    execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
                }),
                viewTrackingInformation: tool({
                    description: "view tracking information for a specific order",
                    parameters: z.object({ orderId: z.string() }),
                    execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
                }),
            },
            maxSteps: 5,
        });
        return text;
    },
    { name: "wrapper" },
);

await wrapper("What are my orders and where are they? My user ID is 123.");
```


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#tracing-in-serverless-environments) Tracing in serverless environments


When tracing in serverless environments, wait for all runs to flush before your environment shuts down.


- AI SDK v7
- AI SDK v5 and v6

Pass a LangSmith [`Client`](https://docs.smith.langchain.com/reference/js/classes/client.Client) instance to `LangSmithTelemetry`, then call `await client.awaitPendingTraceBatches()`. Make sure to also pass it into any `traceable` wrappers you create:

```
import { openai } from "@ai-sdk/openai";
import { generateText, stepCountIs, tool } from "ai";
import { Client } from "langsmith";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

const client = new Client();
const telemetry = LangSmithTelemetry({ client });

const wrapper = traceable(
    async (input: string) => {
        const { text } = await generateText({
            model: openai("gpt-6-luna"),
            messages: [
                {
                    role: "user",
                    content: input,
                },
            ],
            tools: {
                listOrders: tool({
                    description: "list all orders",
                    inputSchema: z.object({ userId: z.string() }),
                    execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
                }),
                viewTrackingInformation: tool({
                    description: "view tracking information for a specific order",
                    inputSchema: z.object({ orderId: z.string() }),
                    execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
                }),
            },
            stopWhen: stepCountIs(5),
            telemetry: { integrations: [telemetry] },
        });
        return text;
    },
    {
        name: "wrapper",
        client,
    },
);

try {
    await wrapper("What are my orders and where are they? My user ID is 123.");
} finally {
    await client.awaitPendingTraceBatches();
}
```

Pass a LangSmith [`Client`](https://docs.smith.langchain.com/reference/js/classes/client.Client) instance to `wrapAISDK` and any `traceable` wrappers you create, then call `await client.awaitPendingTraceBatches()`:

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { Client } from "langsmith";
import { wrapAISDK } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

const client = new Client();
const { generateText, tool } = wrapAISDK(ai, { client });

const wrapper = traceable(
    async (input: string) => {
        const { text } = await generateText({
            model: openai("gpt-6-luna"),
            messages: [
                {
                    role: "user",
                    content: input,
                },
            ],
            tools: {
                listOrders: tool({
                    description: "list all orders",
                    parameters: z.object({ userId: z.string() }),
                    execute: async ({ userId }) => `User ${userId} has the following orders: 1`,
                }),
                viewTrackingInformation: tool({
                    description: "view tracking information for a specific order",
                    parameters: z.object({ orderId: z.string() }),
                    execute: async ({ orderId }) => `Here is the tracking information for ${orderId}`,
                }),
            },
            maxSteps: 5,
        });
        return text;
    },
    {
        name: "wrapper",
        client,
    },
);

try {
    await wrapper("What are my orders and where are they? My user ID is 123.");
} finally {
    await client.awaitPendingTraceBatches();
}
```


If you are using `Next.js`, there is a convenient [`after`](https://nextjs.org/docs/app/api-reference/functions/after) hook where you can put this logic:


```
import { after } from "next/server";
import { Client } from "langsmith";

export async function POST(request: Request) {
    const client = new Client();
    const body = await request.json();

    after(async () => {
        await client.awaitPendingTraceBatches();
    });

    return Response.json({ ok: true, body });
}
```


See [Trace JS functions in serverless environments](https://docs.langchain.com/langsmith/serverless-environments) for more detail, including information around managing rate limits in serverless environments.


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#passing-langsmith-config) Passing LangSmith config


You can pass LangSmith-specific config such as metadata, run names, tags, and custom client instances.


- AI SDK v7
- AI SDK v5 and v6

If you register the integration globally, the config applies to future AI SDK calls:

```
import { openai } from "@ai-sdk/openai";
import { generateText, registerTelemetry } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";

registerTelemetry(
    LangSmithTelemetry({
        metadata: { key_for_all_runs: "value" },
        tags: ["myrun"],
    }),
);

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

To apply config to a single run, pass a telemetry integration in that AI SDK call:

```
import { openai } from "@ai-sdk/openai";
import { generateText } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
    telemetry: {
        integrations: [
            LangSmithTelemetry({
                metadata: { individual_key: "value" },
                name: "my_individual_run",
            }),
        ],
    },
});
```

If you pass config into `wrapAISDK`, the config applies to the wrapped methods:

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { wrapAISDK } from "langsmith/experimental/vercel";

const { generateText } = wrapAISDK(ai, {
    metadata: { key_for_all_runs: "value" },
    tags: ["myrun"],
});

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
});
```

To apply config to a single run, pass LangSmith provider options in that AI SDK call:

```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import {
    createLangSmithProviderOptions,
    wrapAISDK,
} from "langsmith/experimental/vercel";

const { generateText } = wrapAISDK(ai);

await generateText({
    model: openai("gpt-6-luna"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
    providerOptions: {
        langsmith: createLangSmithProviderOptions<typeof ai.generateText>({
            metadata: { individual_key: "value" },
            name: "my_individual_run",
        }),
    },
});
```


## [​](https://docs.langchain.com/langsmith/trace-with-vercel-ai-sdk#redacting-data) Redacting data


You can customize what inputs and outputs the AI SDK sends to LangSmith by specifying custom input/output processing functions. This is useful if you are dealing with sensitive data that you would like to avoid sending to LangSmith.
Because output formats vary depending on which AI SDK method you are using, we suggest defining and passing telemetry config individually into AI SDK calls. You will also need to provide separate functions for child LLM runs within AI SDK calls, since calling `generateText` at top level calls the LLM internally and can do so multiple times.
Here’s an example for `generateText`:


- AI SDK v7
- AI SDK v5 and v6


```
import { openai } from "@ai-sdk/openai";
import { generateText } from "ai";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";

const telemetry = LangSmithTelemetry({
    processInputs: (inputs) => {
        const messages = inputs.messages as Array<Record<string, unknown>> | undefined;
        return {
            messages: messages?.map((message) => ({
                providerMetadata: message.providerOptions,
                role: "assistant",
                content: "REDACTED",
            })),
            prompt: "REDACTED",
        };
    },
    processOutputs: (outputs) => {
        return {
            providerMetadata: outputs.providerMetadata,
            role: "assistant",
            content: "REDACTED",
        };
    },
    processChildLLMRunInputs: (inputs) => {
        const messages = inputs.messages as Array<Record<string, unknown>> | undefined;
        return {
            messages: messages?.map((message) => ({
                ...message,
                content: "REDACTED CHILD INPUTS",
            })),
        };
    },
    processChildLLMRunOutputs: (outputs) => {
        return {
            providerMetadata: outputs.providerMetadata,
            content: "REDACTED CHILD OUTPUTS",
            role: "assistant",
        };
    },
});

const { text } = await generateText({
    model: openai("gpt-6-luna"),
    prompt: "What is the capital of France?",
    telemetry: { integrations: [telemetry] },
});

console.log(text);
```


```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import {
    createLangSmithProviderOptions,
    wrapAISDK,
} from "langsmith/experimental/vercel";

const { generateText } = wrapAISDK(ai);

const langsmith = createLangSmithProviderOptions<typeof ai.generateText>({
    processInputs: (inputs) => {
        return {
            messages: inputs.messages?.map((message) => ({
                providerMetadata: message.providerOptions,
                role: "assistant",
                content: "REDACTED",
            })),
            prompt: "REDACTED",
        };
    },
    processOutputs: () => {
        return {
            role: "assistant",
            content: "REDACTED",
        };
    },
    processChildLLMRunInputs: (inputs) => {
        return {
            messages: inputs.prompt.map((message) => ({
                ...message,
                content: "REDACTED CHILD INPUTS",
            })),
        };
    },
    processChildLLMRunOutputs: () => {
        return {
            content: "REDACTED CHILD OUTPUTS",
            role: "assistant",
        };
    },
});

const { text } = await generateText({
    model: openai("gpt-6-luna"),
    prompt: "What is the capital of France?",
    providerOptions: { langsmith },
});

console.log(text);
```


The actual return value will contain the original, non-redacted result, but the trace in LangSmith will be redacted.
For redacting tool input/output, wrap your `execute` method in a `traceable` like this:


- AI SDK v7
- AI SDK v5 and v6


```
import { openai } from "@ai-sdk/openai";
import { generateText, stepCountIs, tool } from "ai";
import { Client } from "langsmith";
import { LangSmithTelemetry } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

const client = new Client();
const telemetry = LangSmithTelemetry({ client });

await generateText({
    model: openai("gpt-6-luna"),
    messages: [
        {
            role: "user",
            content: "What are my orders? My user ID is 123.",
        },
    ],
    tools: {
        listOrders: tool({
            description: "list all orders",
            inputSchema: z.object({ userId: z.string() }),
            execute: traceable(
                async ({ userId }) => {
                    return `User ${userId} has the following orders: 1`;
                },
                {
                    processInputs: () => ({ text: "REDACTED" }),
                    processOutputs: () => ({ text: "REDACTED" }),
                    run_type: "tool",
                    name: "listOrders",
                },
            ) as (input: { userId: string }) => Promise<string>,
        }),
    },
    stopWhen: stepCountIs(5),
    telemetry: { integrations: [telemetry] },
});

await client.awaitPendingTraceBatches();
```


```
import { openai } from "@ai-sdk/openai";
import * as ai from "ai";
import { Client } from "langsmith";
import { wrapAISDK } from "langsmith/experimental/vercel";
import { traceable } from "langsmith/traceable";
import { z } from "zod";

const client = new Client();
const { generateText, tool } = wrapAISDK(ai, { client });

await generateText({
    model: openai("gpt-6-luna"),
    messages: [
        {
            role: "user",
            content: "What are my orders? My user ID is 123.",
        },
    ],
    tools: {
        listOrders: tool({
            description: "list all orders",
            parameters: z.object({ userId: z.string() }),
            execute: traceable(
                async ({ userId }) => {
                    return `User ${userId} has the following orders: 1`;
                },
                {
                    processInputs: () => ({ text: "REDACTED" }),
                    processOutputs: () => ({ text: "REDACTED" }),
                    run_type: "tool",
                    name: "listOrders",
                },
            ) as (input: { userId: string }) => Promise<string>,
        }),
    },
    maxSteps: 5,
});

await client.awaitPendingTraceBatches();
```


The `traceable` return type is complex, which makes the cast necessary. You may also omit the AI SDK `tool` helper if you wish to avoid the cast.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-vercel-ai-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Strands Agents applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-strands-agents`

# Trace Strands Agents applications
## Documentation Index
## ​Installation
## ​Setup
## ​View traces in LangSmith
## ​Customize the OTLP exporter
## ​Resources







Trace Strands Agents applications with LangSmith.

[Strands Agents](https://strandsagents.com/) is an SDK for building model-driven agents. LangSmith provides a Strands Agents integration that exports Strands OpenTelemetry spans in a LangSmith-compatible format, including agent runs, model calls, tool calls, prompts, completions, and token usage.


## [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#installation) Installation


Install LangSmith with Strands Agents support:
pip uv

```
pip install "langsmith[strands-agents]"
```


```
uv add "langsmith[strands-agents]"
```


This installs LangSmith, Strands Agents, Strands Agents tools, and the OpenTelemetry OTLP HTTP exporter.


## [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#setup) Setup


### [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#1-configure-environment-variables) 1. Configure environment variables


Set your [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key) and project name. If you use Amazon Bedrock as the model provider for Strands Agents, also configure AWS credentials with your preferred AWS authentication method.


```
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.smith.langchain.com/otel/v1/traces
export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your_langsmith_api_key>,Langsmith-Project=<your_project_name>"

# Required when using Amazon Bedrock.
export AWS_REGION=<your_aws_region>
```


The Strands Agents integration uses the standard OpenTelemetry OTLP exporter. Configure the LangSmith endpoint and headers before calling `setup_langsmith_telemetry()`.


### [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#2-enable-strands-agents-telemetry) 2. Enable Strands Agents telemetry


Call `setup_langsmith_telemetry()` once at application startup before creating or invoking agents:


```
from langsmith.integrations.strands_agents import setup_langsmith_telemetry

setup_langsmith_telemetry()
```


For local debugging, pass `console=True` to also print transformed spans to stdout:


```
setup_langsmith_telemetry(console=True)
```


### [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#3-create-and-run-your-agent) 3. Create and run your agent


Once configured, Strands Agents traces are exported to LangSmith automatically:


```
from langsmith.integrations.strands_agents import setup_langsmith_telemetry
from strands import Agent

setup_langsmith_telemetry()

agent = Agent(
    system_prompt="You are a concise assistant.",
)

response = agent("Explain what LangSmith tracing is in one sentence.")
print(response)
```


## [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#view-traces-in-langsmith) View traces in LangSmith


After running your application, open your LangSmith project to view traces that include:


- Agent invocation spans
- Event loop cycle spans
- LLM call spans with prompts, completions, and token usage
- Tool call spans with tool inputs and outputs when your agent uses tools


## [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#customize-the-otlp-exporter) Customize the OTLP exporter


If you need to pass custom options to the underlying OpenTelemetry exporter, create a `LangSmithSpanExporter` with `create_langsmith_exporter()` and attach it to the Strands tracer provider manually:


```
from langsmith.integrations.strands_agents import create_langsmith_exporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from strands.telemetry import StrandsTelemetry

telemetry = StrandsTelemetry()
exporter = create_langsmith_exporter(
    endpoint="https://api.smith.langchain.com/otel/v1/traces",
    headers={
        "x-api-key": "<your_langsmith_api_key>",
        "Langsmith-Project": "<your_project_name>",
    },
)
telemetry.tracer_provider.add_span_processor(BatchSpanProcessor(exporter))
```


Use this approach when you want to configure exporter options in code instead of environment variables.


## [​](https://docs.langchain.com/langsmith/trace-with-strands-agents#resources) Resources


- [Strands Agents documentation](https://strandsagents.com/)
- [LangSmith OpenTelemetry guide](https://docs.langchain.com/langsmith/trace-with-opentelemetry)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-strands-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenAI Realtime applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-openai-realtime`

# Trace OpenAI Realtime applications
## Documentation Index
## ​Choose an approach
## ​Install
## ​Set environment variables
## ​Using the Realtime client
## ​Using the OpenAI Agents SDK
## ​Next steps








Trace OpenAI Realtime voice agents in LangSmith using the LangSmith SDK.

This integration is in beta, so its API may change.
OpenAI Realtime is a speech-to-speech model that streams typed events over a WebSocket. Regardless of whether you build it with a raw connection or the OpenAI Agents SDK, the integration captures each conversation as a single LangSmith trace, with a span for every meaningful event (transcripts, model responses, and tool calls) grouped by turn.
Trace your [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) voice agents to LangSmith. For high-level conventions, see [Voice tracing fundamentals](https://docs.langchain.com/langsmith/trace-voice-fundamentals).


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#choose-an-approach) Choose an approach


There are two ways to build with the OpenAI Realtime API, and LangSmith provides a tracing integration for each:


- If you are connecting directly with the realtime client, use `wrap_realtime`.
- If you are building with the OpenAI Agents SDK, use `wrap_realtime_session` instead.


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#install) Install


The `langsmith[openai-realtime]>=0.9.7` extra provides both wrappers:
pip uv

```
pip install "langsmith[openai-realtime]"
```


```
uv add "langsmith[openai-realtime]"
```


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#set-environment-variables) Set environment variables


.env

```
LANGSMITH_API_KEY=<your-langsmith-api-key>
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=<your-desired-langsmith-project>
OPENAI_API_KEY=<your-openai-api-key>
```


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#using-the-realtime-client) Using the Realtime client


Use this when you open the WebSocket yourself with `client.realtime.connect()` and drive the event loop.


### [​](https://docs.langchain.com/langsmith/trace-openai-realtime#set-up-tracing) Set up tracing


`wrap_realtime` returns a transparent proxy of your connection. Your existing `async for event in connection` loop, `session.update`, and tool handling stay the same:


```
from langsmith.integrations.openai_realtime import wrap_realtime
from openai import AsyncOpenAI

client = AsyncOpenAI()

async with client.realtime.connect(model="gpt-realtime-2") as raw, wrap_realtime(
    raw,
    project_name="openai-realtime-voice",
) as connection:
    await connection.session.update(session={...})  # your existing config

    async for event in connection:
        ...  # your existing handling: play audio, run tools, update UI
```


Each conversation is captured as its own trace. To group it with related interactions in a LangSmith [thread](https://docs.langchain.com/langsmith/threads) (for example to continue an earlier session or pick up from a text chat), pass a `thread_id`. Reusing the same ID across traces links their events together.
Any [`@traceable`](https://docs.langchain.com/langsmith/annotate-code) tools you run while handling an event nest under that event automatically.
Enable `input_audio_transcription` and the agent transcript in your `session.update` in order to view a transcript as part of the trace.


### [​](https://docs.langchain.com/langsmith/trace-openai-realtime#record-the-conversation-audio) Record the conversation audio


When you feed the proxy your microphone and playback audio, it attaches a single stereo recording (user left, agent right) to the trace. To flag barge-ins, use `is_agent_speaking`:


```
import base64

async with client.realtime.connect(model="gpt-realtime-2") as raw, wrap_realtime(
    raw,
    is_agent_speaking=lambda: speaker.buffered_bytes() > 0,
) as connection:
    # Record the agent's audio from the speaker, so the recording reflects only
    # what was played — audio a barge-in discards before playback is never recorded.
    speaker.set_played_callback(connection.record_agent_audio)

    # Record the user's mic where you send it to the model.
    async def send_mic(mic_chunk):
        await connection.input_audio_buffer.append(
            audio=base64.b64encode(mic_chunk).decode("ascii")
        )
        connection.record_user_audio(mic_chunk)          # user mic PCM16 as sent

    async for event in connection:
        if event.type == "response.output_audio.delta":
            speaker.play(base64.b64decode(event.delta))
```


You should record the agent’s audio from the speaker, so that the recording reflects only what was played. During a barge-in, generated audio is discarded before playback and should not be recorded. Doing this keeps the trace aligned with what the user actually heard.


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#using-the-openai-agents-sdk) Using the OpenAI Agents SDK


Use this when you build the agent with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/realtime/guide/) (`RealtimeAgent` / `RealtimeRunner`), which owns the turn and tool-call loop.
The Agents SDK’s built-in realtime tracing uploads to OpenAI’s own dashboard. Call `agents.set_tracing_disabled(True)` to avoid a second, separate upload path.


### [​](https://docs.langchain.com/langsmith/trace-openai-realtime#set-up-tracing-2) Set up tracing


`wrap_realtime_session` wraps the `RealtimeSession` and enters it for you. Iterate it as you would the original; the SDK runs tools and manages turns:


```
from agents import set_tracing_disabled
from agents.realtime import RealtimeAgent, RealtimeRunner
from langsmith.integrations.openai_realtime import wrap_realtime_session

set_tracing_disabled(True)

runner = RealtimeRunner(
    starting_agent=RealtimeAgent(name="assistant", instructions="...", tools=[...]),
)
session = await runner.run()

async with wrap_realtime_session(
    session,
    project_name="openai-realtime-voice",
) as conn:
    async for event in conn:
        ...  # your handling: play audio, update UI
```


The conversation transcript is reconstructed from the session’s `history` snapshots, so messages appear even though the SDK streams them as partials.
Each conversation is captured as its own trace. To group it with related interactions in a LangSmith [thread](https://docs.langchain.com/langsmith/threads), for example to continue an earlier session or pick up from a text chat, pass a `thread_id`. Reusing the same ID across traces links their events together.


### [​](https://docs.langchain.com/langsmith/trace-openai-realtime#record-the-conversation-audio-2) Record the conversation audio


Feed the proxy your microphone and playback audio:


```
# Record the agent's audio from the speaker, so the recording reflects only
# what was played — audio a barge-in discards before playback is never recorded.
speaker.set_played_callback(conn.record_agent_audio)

# Record the user's mic where you send it to the session.
async def send_mic(mic_chunk):
    await conn.send_audio(mic_chunk)
    conn.record_user_audio(mic_chunk)               # user mic PCM16 as sent

async for event in conn:
    if event.type == "audio":
        speaker.play(event.audio.data)
```


You should record the agent’s audio from the speaker, so that the recording reflects only what was played. During a barge-in, generated audio is discarded before playback and should not be recorded. Doing this keeps the trace aligned with what the user actually heard.


## [​](https://docs.langchain.com/langsmith/trace-openai-realtime#next-steps) Next steps


## Voice fundamentals

Core conventions for tracing voice agents.

## Upload files with traces

Attach the conversation audio recording to your trace.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-openai-realtime.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Gemini Live applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-gemini-live`

# Trace Gemini Live applications
## Documentation Index
## ​Choose an approach
## ​Install
## ​Set environment variables
## ​Use the Gemini Live client
## ​Use Google ADK
## ​Next steps








Trace Gemini Live voice agents in LangSmith using the LangSmith SDK.

This integration is in beta, so its API may change.
Gemini Live is a speech-to-speech model that streams typed events over a WebSocket. Whether you build with a raw `google-genai` connection or the Google Agent Development Kit (ADK), the integration captures each conversation as a single LangSmith trace with spans for transcripts, model responses, tool calls, turn boundaries, and interruptions.
Trace your [Gemini Live](https://ai.google.dev/gemini-api/docs/live-api) voice agents to LangSmith. For high-level conventions, see [Voice tracing fundamentals](https://docs.langchain.com/langsmith/trace-voice-fundamentals).
To trace non-live text agents, tools, and multi-agent workflows built with ADK, see [Trace Google ADK applications](https://docs.langchain.com/langsmith/trace-with-google-adk).


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#choose-an-approach) Choose an approach


LangSmith provides a tracing integration for each way to connect to Gemini Live:


- If you connect directly with `client.aio.live.connect(...)`, use `wrap_gemini_live`.
- If you build with [Google ADK](https://google.github.io/adk-docs/streaming/), use `LangSmithGoogleADKLivePlugin`.


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#install) Install


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#use-the-gemini-live-client) Use the Gemini Live client


Install the `gemini-live` extra for a raw `google-genai` connection:
pip uv

```
pip install "langsmith[gemini-live]"
```


```
uv add "langsmith[gemini-live]"
```


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#use-google-adk) Use Google ADK


Install the `google-adk-live` extra for an ADK application:
pip uv

```
pip install "langsmith[google-adk-live]"
```


```
uv add "langsmith[google-adk-live]"
```


The ADK Live integration requires `langsmith[google-adk-live]>=0.9.7`. This extra is separate from the `langsmith[google-adk]` batch integration.


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#set-environment-variables) Set environment variables


.env

```
LANGSMITH_API_KEY=<your-langsmith-api-key>
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=<your-desired-langsmith-project>
GOOGLE_API_KEY=<your-google-api-key>
GEMINI_LIVE_MODEL=<your-gemini-live-model>
```


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#use-the-gemini-live-client-2) Use the Gemini Live client


Use this approach when your application opens the WebSocket with `client.aio.live.connect(...)` and owns the audio and tool loops.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#set-up-tracing) Set up tracing


Enable input and output transcription in the live configuration. `wrap_gemini_live` returns a transparent proxy for the connected session, so your existing receive loop, audio handling, and tool dispatch remain unchanged:


```
import os

from google import genai
from google.genai import types
from langsmith.integrations.gemini_live import wrap_gemini_live

model = os.environ["GEMINI_LIVE_MODEL"]
client = genai.Client()
config = types.LiveConnectConfig(
    response_modalities=[types.Modality.AUDIO],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
)

async with (
    client.aio.live.connect(model=model, config=config) as raw,
    wrap_gemini_live(
        raw,
        model=model,
        project_name="gemini-live-voice",
    ) as session,
):
    async for message in session.receive():
        ...  # play audio, run tools, handle barge-ins, and update the UI
```


Transcription is opt-in. To show transcripts in the trace, set both `input_audio_transcription` and `output_audio_transcription` on `LiveConnectConfig`.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#group-a-conversation-into-a-thread) Group a conversation into a thread


Each wrapped session is captured as its own trace with its own thread ID. To supply an ID, for example to group the conversation with related interactions in a LangSmith [thread](https://docs.langchain.com/langsmith/threads), pass `thread_id`:


```
wrap_gemini_live(
    raw,
    model=model,
    thread_id=thread_id,
    project_name="gemini-live-voice",
)
```


Create one wrapper per connected Gemini Live session. Each wrapper owns isolated tracing and transcript state, so concurrent conversations remain separate.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#record-the-conversation-audio) Record the conversation audio


Feed microphone and playback audio to the wrapped session to attach a single stereo recording, with the user on the left channel and the agent on the right channel:


```
RECORDING_SAMPLE_RATE = 24_000

async with (
    client.aio.live.connect(model=model, config=config) as raw,
    wrap_gemini_live(
        raw,
        model=model,
        sample_rate=RECORDING_SAMPLE_RATE,
        is_agent_speaking=lambda: speaker.buffered_bytes() > 0,
    ) as session,
):
    # Record audio after playback so discarded audio from a barge-in is omitted.
    speaker.set_played_callback(session.record_agent_audio)

    async def send_mic(mic_chunk):
        await session.send_realtime_input(
            audio=types.Blob(
                data=mic_chunk,
                mime_type=f"audio/pcm;rate={microphone.sample_rate}",
            )
        )
        session.record_user_audio(
            resample_pcm16(
                mic_chunk,
                microphone.sample_rate,
                RECORDING_SAMPLE_RATE,
            )
        )
```


Record both channels as PCM16 at the wrapper’s `sample_rate`. Record the agent’s audio from the speaker so the attachment reflects only what the user heard. For the underlying attachment API, see [Upload files with traces](https://docs.langchain.com/langsmith/upload-files-with-traces).


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#use-google-adk-2) Use Google ADK


Use this approach when ADK owns the Gemini Live session and tool loop.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#set-up-tracing-2) Set up tracing


Import `LangSmithGoogleADKLivePlugin` and register it on your `Runner`. It runs alongside your `run_live` loop, so your loop only handles audio playback, barge-ins, and UI updates:


```
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.genai import types as genai_types
from langsmith.integrations.google_adk_live import LangSmithGoogleADKLivePlugin

plugin = LangSmithGoogleADKLivePlugin(project_name="gemini-live-voice")

runner = Runner(
    app_name="voice-app",
    agent=root_agent,
    session_service=session_service,
    plugins=[plugin],
)

run_config = RunConfig(
    response_modalities=["AUDIO"],
    streaming_mode=StreamingMode.BIDI,
    input_audio_transcription=genai_types.AudioTranscriptionConfig(),
    output_audio_transcription=genai_types.AudioTranscriptionConfig(),
)

async for event in runner.run_live(
    user_id=user_id,
    session_id=adk_session.id,
    live_request_queue=queue,
    run_config=run_config,
):
    ...  # play audio, handle barge-ins, and update the UI
```


Transcription is opt-in. To show transcripts, set both `input_audio_transcription` and `output_audio_transcription` on `RunConfig`.
On a graceful end, when the live request queue closes, ADK sends its `after_run` callback and the plugin finalizes the trace. On a cancelled run, such as a console app that stops `run_live` on Ctrl-C, ADK might not send that callback. Call `plugin.finalize(session_id=adk_session.id)` during teardown so the trace and audio attachment are finalized. The call is idempotent, so it does nothing if ADK’s callback already ran.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#group-a-conversation-into-a-thread-2) Group a conversation into a thread


Each conversation is captured as its own trace with its own thread ID. To supply an ID, for example to group the conversation with related interactions in a LangSmith [thread](https://docs.langchain.com/langsmith/threads), pass a `thread_id_provider` to the plugin:


```
plugin = LangSmithGoogleADKLivePlugin(
    project_name="gemini-live-voice",
    thread_id_provider=lambda: thread_id,
)
```


A single plugin instance is shared across every `run_live` call and resolves the thread ID once at the start of each conversation. The default keeps concurrent conversations separate. If you pass a `thread_id_provider` on a server handling concurrent conversations, return the ID for the current conversation, for example by reading a `ContextVar` set at the start of each run.


### [​](https://docs.langchain.com/langsmith/trace-gemini-live#record-the-conversation-audio-2) Record the conversation audio


Feed microphone and playback audio to the plugin to attach a single stereo recording, with the user on the left channel and the agent on the right channel:


```
plugin.record_user_audio(mic_chunk)      # user mic PCM16
plugin.record_agent_audio(played_chunk)  # agent PCM16 as played
```


Record the user’s microphone capture before resampling it for ADK, and record the agent’s audio from the speaker. Feed both channels at the same sample rate. The plugin’s `sample_rate` is 24 kHz by default. For the underlying attachment API, see [Upload files with traces](https://docs.langchain.com/langsmith/upload-files-with-traces).


## [​](https://docs.langchain.com/langsmith/trace-gemini-live#next-steps) Next steps


## Voice fundamentals

Core conventions for tracing voice agents.

## Upload files with traces

Attach the conversation audio recording to your trace.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-gemini-live.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace LiveKit applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-livekit`

# Trace LiveKit applications

This integration is in beta, so its API may change.
Use the LangSmith LiveKit integration to trace your [LiveKit Agents](https://docs.livekit.io/agents/) voice agents, including their transcripts and audio recordings. For high-level conventions, see [Voice tracing fundamentals](https://docs.langchain.com/langsmith/trace-voice-fundamentals).
This setup requires `langsmith[livekit]>=0.11.2` and `livekit-agents>=1.6`. LiveKit Agents 1.7 and later require `langsmith[livekit]>=0.12.4`.
Each conversation appears as one LangSmith trace with its pipeline events, latency, and token metrics.


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#install) Install


Install the integration along with the LiveKit plugins your agent uses:
pip uv

```
pip install "langsmith[livekit]" "livekit-agents[openai,silero,turn-detector]"
```


```
uv add "langsmith[livekit]" "livekit-agents[openai,silero,turn-detector]"
```


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#set-environment-variables) Set environment variables


The integration reads your LangSmith credentials from the environment and exports to LangSmith for you via OpenTelemetry:
.env

```
LANGSMITH_API_KEY=<your-langsmith-api-key>
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=<your-desired-langsmith-project>
LIVEKIT_URL=<your-livekit-url>
LIVEKIT_API_KEY=<your-livekit-api-key>
LIVEKIT_API_SECRET=<your-livekit-api-secret>
OPENAI_API_KEY=<your-openai-api-key>
```


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#set-up-tracing) Set up tracing


Call `configure_livekit` once before creating your `AgentServer`.


```
from langsmith.integrations.livekit import configure_livekit
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession

# Enable tracing before creating agents.
configure_livekit()

server = AgentServer()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        stt="openai/gpt-4o-mini-transcribe",
        llm="openai/gpt-4o-mini",
        tts="openai/tts-1:alloy",
    )
    await session.start(
        room=ctx.room,
        agent=Agent(instructions="You are a helpful assistant."),
        record={"audio": True},
    )
```


`configure_livekit()` uses LiveKit session recordings by default. The `record={"audio": True}` option tells LiveKit to create the recording.
This setup works for both STT/LLM/TTS cascades and speech-to-speech (realtime) models. Realtime models need one extra call to capture the user’s transcript. For more information, see [Use a realtime model](https://docs.langchain.com/langsmith/trace-with-livekit#use-a-realtime-model).


### [​](https://docs.langchain.com/langsmith/trace-with-livekit#use-your-own-tracer-provider) Use your own tracer provider


If your application already manages an OpenTelemetry `TracerProvider`, add the LangSmith processor to that provider and register it with LiveKit:


```
from langsmith.integrations.livekit import LiveKitLangSmithSpanProcessor
from livekit.agents import telemetry
from opentelemetry.sdk.trace import TracerProvider

provider = TracerProvider()  # your own provider
processor = LiveKitLangSmithSpanProcessor()
provider.add_span_processor(processor)
telemetry.set_tracer_provider(provider)
```


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#group-a-conversation-into-a-thread) Group a conversation into a thread


To group a conversation’s runs into a LangSmith [thread](https://docs.langchain.com/langsmith/threads), call `set_thread_id` inside the session handler. Use a unique ID for each active session:


```
from langsmith.integrations.livekit import configure_livekit, set_thread_id

configure_livekit()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    thread_id = ctx.job.id  # or any id that identifies the conversation
    set_thread_id(thread_id)
    ...
```


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#use-a-realtime-model) Use a realtime model


For a speech-to-speech (realtime) model, call `instrument_session` after creating the `AgentSession` to capture the user’s transcript. Pass the same thread ID to `set_thread_id` and `instrument_session`:


```
from langsmith.integrations.livekit import configure_livekit, set_thread_id
from livekit.plugins import openai as lk_openai

processor = configure_livekit()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    thread_id = ctx.job.id  # or any id that identifies the conversation
    set_thread_id(thread_id)

    session = AgentSession(llm=lk_openai.realtime.RealtimeModel(voice="marin"))
    processor.instrument_session(session, thread_id)  # capture the user transcript

    await session.start(
        room=ctx.room,
        agent=Agent(instructions="You are a helpful assistant."),
        record={"audio": True},
    )
```


Only call `instrument_session` for realtime models. STT/LLM/TTS cascades already capture the user’s transcript, so calling it there records each user turn twice.


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#record-the-conversation-audio) Record the conversation audio


By default, the integration uses LiveKit’s session recording. Use Egress mode when you record to external storage instead.


### [​](https://docs.langchain.com/langsmith/trace-with-livekit#record-with-livekit%E2%80%99s-session-recording) Record with LiveKit’s session recording


Turn on LiveKit’s session recording.


```
from langsmith.integrations.livekit import configure_livekit
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession

configure_livekit()

server = AgentServer()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(...)
    await session.start(
        room=ctx.room,
        agent=Agent(instructions="You are a helpful assistant."),
        record={"audio": True},
    )
```


By default, the LiveKit integration will capture the recording from LiveKit if present.
In console mode, also pass `--record` on the command line (`python agent.py console --record`). Without it LiveKit creates the recorder but never starts it, so there is no file to attach. The recording reflects what was played to the client, so a barge-in shows up truncated.


### [​](https://docs.langchain.com/langsmith/trace-with-livekit#record-with-egress) Record with Egress


Use [LiveKit Egress](https://docs.livekit.io/home/egress/overview/) when you want the recording in your own object storage or need video. Egress recording delivery requires a thread ID. Configure the integration for Egress, then call `complete_recording` after the Egress file is available:


```
import asyncio
import os
import time

from langsmith.integrations.livekit import configure_livekit, set_thread_id
from livekit import agents, api
from livekit.agents import Agent, AgentServer, AgentSession

RECORDING_BUCKET = os.environ["RECORDING_BUCKET"]

processor = configure_livekit(
    recording_mode="egress",
    recording_timeout_seconds=180,
)
server = AgentServer()

async def wait_for_egress(
    lkapi: api.LiveKitAPI,
    egress_id: str,
    timeout_seconds: float = 120,
) -> api.EgressInfo:
    deadline = time.monotonic() + timeout_seconds
    failed_statuses = {
        api.EgressStatus.EGRESS_FAILED,
        api.EgressStatus.EGRESS_ABORTED,
        api.EgressStatus.EGRESS_LIMIT_REACHED,
    }
    while time.monotonic() < deadline:
        response = await lkapi.egress.list_egress(
            api.ListEgressRequest(egress_id=egress_id)
        )
        if response.items:
            info = response.items[0]
            if info.status == api.EgressStatus.EGRESS_COMPLETE:
                return info
            if info.status in failed_statuses:
                raise RuntimeError(f"Egress failed with status {info.status}")
        await asyncio.sleep(1)
    raise TimeoutError(f"Egress {egress_id} did not complete in time")

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    thread_id = ctx.job.id  # unique per session; ctx.room.name is "console" in console mode
    set_thread_id(thread_id)  # routes the Egress recording to this trace
    key = f"recordings/{thread_id}.ogg"

    # Start an audio-only room-composite egress to your storage.
    lkapi = api.LiveKitAPI()  # reads LIVEKIT_URL / LIVEKIT_API_KEY / LIVEKIT_API_SECRET
    egress = await lkapi.egress.start_room_composite_egress(
        api.RoomCompositeEgressRequest(
            room_name=ctx.room.name,
            audio_only=True,
            file_outputs=[
                api.EncodedFileOutput(
                    file_type=api.EncodedFileType.OGG,
                    filepath=key,
                    s3=api.S3Upload(
                        bucket=RECORDING_BUCKET,
                        region=os.environ["AWS_REGION"],
                        access_key=os.environ["AWS_ACCESS_KEY_ID"],
                        secret=os.environ["AWS_SECRET_ACCESS_KEY"],
                    ),
                )
            ],
        )
    )

    async def attach_recording():
        try:
            info = await wait_for_egress(lkapi, egress.egress_id)  # poll until EGRESS_COMPLETE
            audio = download_from_storage(RECORDING_BUCKET, key)  # your storage client
            processor.complete_recording(
                thread_id,
                data=audio,
                # EgressInfo.started_at is a Unix timestamp in nanoseconds. This is
                # when the egress worker began recording, which is what aligns the
                # audio start with the trace.
                started_at=info.started_at / 1e9,
            )
        except Exception:
            processor.complete_recording(thread_id, data=None)

    ctx.add_shutdown_callback(attach_recording)

    session = AgentSession(...)
    await session.start(room=ctx.room, agent=Agent(instructions="..."))
```


`download_from_storage` represents your storage client’s download operation. The default attachment name and MIME type are `recording.ogg` and `audio/ogg`. Set `name` or `mime_type` in `complete_recording` if your Egress output uses another format.
Always call `complete_recording`, including on failure with `data=None`. Otherwise, the integration waits for `recording_timeout_seconds` (30 seconds by default) before exporting the trace without audio. Using `complete_recording` to capture Egress recordings requires setting a `thread_id`.


## [​](https://docs.langchain.com/langsmith/trace-with-livekit#next-steps) Next steps


## Voice fundamentals

Core conventions for tracing voice agents.

## Upload files with traces

Attach the conversation audio recording to your trace.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-livekit.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Install
## ​Set environment variables
## ​Set up tracing
## ​Group a conversation into a thread
## ​Use a realtime model
## ​Record the conversation audio
## ​Next steps









Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Claude Code applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-claude-code`

# Trace Claude Code applications

This guide shows you how to send conversations automatically from the [Claude Code CLI](https://code.claude.com/docs/en/overview) to LangSmith.
Once configured, each Claude Code project can opt in to sending traces to LangSmith. Each trace includes user messages, tool calls, compaction, subagent runs, and assistant responses. System prompts are not included, because Claude Code does not return them in conversation transcripts.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- [**Claude Code CLI**](https://code.claude.com/docs/en/overview) installed.
- A [**LangSmith API key**](https://docs.langchain.com/langsmith/create-account-api-key).
- [**Node.js**](https://nodejs.org/) installed.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#getting-started) Getting started


From within Claude Code, run:


```
/plugin marketplace add langchain-ai/langsmith-claude-code-plugins
/plugin install langsmith-tracing@langsmith-claude-code-plugins
/reload-plugins
```


To update the plugin, refresh the marketplace from within Claude Code:


```
/plugin marketplace update langsmith-claude-code-plugins
```


Then move the install onto the new version from your shell and restart Claude Code:


```
claude plugin update langsmith-tracing@langsmith-claude-code-plugins
```


 The marketplace update on its own only refreshes the catalog clone. Your install stays pinned to the version directory it was installed from, so the hooks keep running the old bundle until `claude plugin update` moves it. To skip both steps next time, run `/plugin`, open **Marketplaces** → `langsmith-claude-code-plugins` and choose **Enable auto-update**: third-party marketplaces have it off by default, and enabling it updates the marketplace and its installed plugins together.
 If you are migrating from the previously recommended version of tracing Claude Code with manually created stop hooks, refer to [Migrating from the manual stop hook](https://docs.langchain.com/langsmith/trace-claude-code#migrating-from-the-manual-stop-hook).


### [​](https://docs.langchain.com/langsmith/trace-claude-code#setting-environment-variables) Setting environment variables


**Option 1: Project-level configuration (recommended)**
The plugin requires the following environment variables:


- `TRACE_TO_LANGSMITH: "true"`: Enables tracing for this project. Remove or set to `false` to disable tracing.
- `CC_LANGSMITH_API_KEY`: Your LangSmith API key.
- `CC_LANGSMITH_PROJECT`: The LangSmith project name to which your traces will send.
- (optional) `CC_LANGSMITH_METADATA`: JSON object of custom metadata to attach to all runs (e.g., PR URL, author).
- (optional) `CC_LANGSMITH_DEBUG: "true"`: Enables detailed debug logging. Remove or set to `false` to disable debug logging.


To get set up, create or edit [Claude Code’s project settings file](https://code.claude.com/docs/en/settings#:~:text=Project%20settings%20are%20saved%20in%20your%20project%20directory%3A). Create a `.claude/settings.local.json` in your project directory and populate it as follows:


```
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
    "CC_LANGSMITH_PROJECT": "my-project"
  }
}
```


 Alternatively, to enable tracing to LangSmith for all Claude Code sessions, you can add the previous JSON to your [global Claude Code settings.json](https://code.claude.com/docs/en/settings#:~:text=User%20settings%20are%20defined%20in%20~/.claude/settings.json%20and%20apply%20to%20all%20projects.) file.
**Option 2: Shell environment variables**
Run the following commands in your shell or add them to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):


```
export TRACE_TO_LANGSMITH="true"
export CC_LANGSMITH_API_KEY="<LangSmith API key>"
export CC_LANGSMITH_PROJECT="my-project"
```


## [​](https://docs.langchain.com/langsmith/trace-claude-code#verify-setup) Verify setup


Traces will appear complete in your [LangSmith](https://smith.langsmith.com) project after Claude Code responds. If you interrupt a run while it is in progress, the plugin will only flush that run when you send the next message or end the session.
In LangSmith, you’ll find:


- Each message to Claude Code appears as a trace.
- All turns from the same Claude Code session are grouped using a shared `thread_id`, which you can view in the **Threads** tab of a project.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#custom-metadata) Custom metadata


Set the `CC_LANGSMITH_METADATA` environment variable to a JSON object to attach custom metadata to all traced runs. This is useful for tagging traces with contextual information such as PR URLs, authors, or environment names.


- Settings file (recommended)
- Shell environment variable


```
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
    "CC_LANGSMITH_PROJECT": "my-project",
    "CC_LANGSMITH_METADATA": "{\"author\":\"jane\",\"environment\":\"development\"}"
  }
}
```


```
export CC_LANGSMITH_METADATA='{"author":"jane","environment":"development"}'
```


The metadata keys and values will appear on all runs in LangSmith, which you can use to filter and search traces.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#mute-a-thread) Mute a thread


Muting suppresses a thread’s input and output content in traces without disabling tracing. Muting is off by default unless you [set a default](https://docs.langchain.com/langsmith/trace-claude-code#set-a-default-mute-configuration).
With tracing enabled, run these plugin commands inside Claude Code. Neither command takes arguments:


- `/langsmith-tracing:mute`: Omit this thread’s input and output content from later traces.
- `/langsmith-tracing:unmute`: Restore full tracing for later turns in this thread.


Both commands apply from the next turn, so the current turn is unchanged. A turn’s mode is fixed when the turn starts, and its subagents inherit that mode.
Muted runs keep their normal nesting, names, timing, status, model and tool identity, and token usage. Inputs and outputs are replaced with a system notice. Muted mode also omits raw errors, identity and repository attribution, custom metadata, SDK runtime metadata, and replica metadata overrides. Muting is independent of secret redaction.


### [​](https://docs.langchain.com/langsmith/trace-claude-code#set-a-default-mute-configuration) Set a default mute configuration


To start threads in metadata-only mode without running a command in each one, set `CC_LANGSMITH_DEFAULT_MUTED` to `"true"`:


- Settings file (recommended)
- Shell environment variable


```
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
    "CC_LANGSMITH_PROJECT": "my-project",
    "CC_LANGSMITH_DEFAULT_MUTED": "true"
  }
}
```


```
export CC_LANGSMITH_DEFAULT_MUTED="true"
```


Set the variable to `"false"` to return to the unmuted default. The comparison is case-insensitive, and any other value mutes, including an empty string.
The plugin also reads a `defaultMuted` boolean from its own configuration files, in this order: `.claude/langsmith.json` and `langsmith-plugins.json` in the project directory, then `~/.claude/langsmith.json` and `~/.langsmith-plugins.json`. The environment variable takes precedence over all four.
Thread preferences are sticky. The plugin saves each explicit mute or unmute to a privacy file, `~/.claude/state/langsmith_state.privacy.json` by default, and a saved thread preference wins over the configured default in both directions. Deleting the privacy file removes every thread override and returns each thread to the configured default.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#secret-redaction) Secret redaction


The plugin redacts detected secrets from run inputs, outputs, errors, and metadata before uploading them to LangSmith. Redaction is on by default.
Redaction runs on your machine before upload, so unredacted content never reaches LangSmith. Replica destinations receive the same redacted payload.
Detection covers provider API key prefixes, JSON Web Tokens, and PEM private key blocks. It also covers contextual shapes such as `API_KEY=<value>`, an `Authorization` header, and a password embedded in a URL. Each match is replaced with `[SECRET_DETECTED]`. For the rule list, see [Redact secrets from traces](https://docs.langchain.com/langsmith/redact-secrets#rules-in-the-preset).
Redaction matches known credential shapes, so treat it as a safety net rather than a guarantee. A credential in an unrecognized format still reaches LangSmith, and attachments, run names, and tags do not pass through the anonymizer. A redacted trace also still holds the prompts, file contents, and tool results it was built from, so restrict who can read the tracing project.
Redaction targets credential values, not identity. The `anthropic_user_id` and `local_username` metadata that the plugin attaches is unaffected. To omit content and attribution instead of scrubbing credentials out of it, [mute the thread](https://docs.langchain.com/langsmith/trace-claude-code#mute-a-thread).


### [​](https://docs.langchain.com/langsmith/trace-claude-code#turn-redaction-off) Turn redaction off


Set `CC_LANGSMITH_REDACT` to `false`, `0`, `no`, or `off`. The comparison is case-insensitive, and any other value leaves redaction on.


```
export CC_LANGSMITH_REDACT="false"
```


### [​](https://docs.langchain.com/langsmith/trace-claude-code#redact-additional-patterns) Redact additional patterns


Set `CC_LANGSMITH_REDACT_EXTRA` to a JSON array of `{ "pattern": ..., "replace": ... }` rules. Each `pattern` is a regular expression string, applied globally and case-sensitively. `replace` is optional and falls back to `[redacted]`.


```
{
  "env": {
    "CC_LANGSMITH_REDACT_EXTRA": "[{\"pattern\":\"ACME-[A-Z0-9]{16}\",\"replace\":\"[REDACTED_ACME_KEY]\"}]"
  }
}
```


Extra rules run after the built-in ones. The plugin skips a rule with an invalid regular expression, logs an error, and uploads the turn with the remaining rules applied.
Both settings also read from the plugin configuration files described in [Set a default mute configuration](https://docs.langchain.com/langsmith/trace-claude-code#set-a-default-mute-configuration), as the `redact` and `redact_extra_rules` keys:


```
{
  "redact": true,
  "redact_extra_rules": [{ "pattern": "ACME-[A-Z0-9]{16}", "replace": "[REDACTED_ACME_KEY]" }]
}
```


The environment variables take precedence over all four files. A file behaves more strictly than the environment variable. One rule with an invalid regular expression discards every setting in that file, not only that rule.
Because a project-level `.claude/langsmith.json` can set `redact` to `false`, review that file before enabling tracing in a repository you do not control.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#usage-with-github-actions) Usage with GitHub Actions


You can use this plugin with [`anthropics/claude-code-action`](https://github.com/anthropics/claude-code-action) to trace Claude Code runs in CI. Add the following to your workflow:


```
- uses: anthropics/claude-code-action@v1
  env:
    TRACE_TO_LANGSMITH: "true"
    CC_LANGSMITH_API_KEY: ${{ secrets.LANGSMITH_API_KEY }}
    CC_LANGSMITH_PROJECT: "my-project"
    CC_LANGSMITH_METADATA: |
      {
        "pr_url": "${{ github.event.pull_request.html_url || '' }}",
        "pr_number": "${{ github.event.pull_request.number || '' }}",
        "pr_author": "${{ github.event.pull_request.user.login || '' }}",
        "repository": "${{ github.repository }}",
        "commit_sha": "${{ github.sha }}",
        "trigger": "${{ github.event_name }}"
      }
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    github_token: ${{ secrets.GITHUB_TOKEN }}
    plugin_marketplaces: |
      https://github.com/langchain-ai/langsmith-claude-code-plugins.git
    plugins: |
      langsmith-tracing@langsmith-claude-code-plugins
    prompt: |
      Your prompt here
```


Make sure to add `LANGSMITH_API_KEY` and `ANTHROPIC_API_KEY` as [repository secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
This lets you correlate traces back to specific PRs, commits, and authors in LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-claude-code#nesting-traces-under-an-existing-run) Nesting traces under an existing run


You can also set an environment variable named `CC_LANGSMITH_PARENT_DOTTED_ORDER` to nest all Claude Code traces as children of an existing LangSmith run. This is useful when Claude Code is invoked programmatically as part of a larger traced workflow.
**Python**


```
import subprocess
from langsmith import traceable, get_current_run_tree


os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "<LangSmith API key>"
os.environ["LANGSMITH_PROJECT"] = "claude-code"

@traceable
def run_claude(prompt: str):
    run_tree = get_current_run_tree()
    subprocess.run(
        ["claude", "-p", prompt],
        env={
            **os.environ,
            "TRACE_TO_LANGSMITH": "true",
            "CC_LANGSMITH_API_KEY": "<LangSmith API key>",
            "CC_LANGSMITH_PROJECT": "claude-code",
            "CC_LANGSMITH_PARENT_DOTTED_ORDER": run_tree.dotted_order,
        },
    )
```


**TypeScript**


```
import { traceable, getCurrentRunTree } from "langsmith/traceable";
import { execSync } from "node:child_process";

process.env.LANGSMITH_TRACING = "true";
process.env.LANGSMITH_API_KEY = "<LangSmith API key>";
process.env.LANGSMITH_PROJECT = "claude-code";

const runClaude = traceable(
  async (prompt: string) => {
    const runTree = getCurrentRunTree();
    const pluginDir = new URL(".", import.meta.url).pathname;
    const res = execSync(`claude -p "${prompt}" --plugin-dir '${pluginDir}'`, {
      env: {
        ...process.env,
        TRACE_TO_LANGSMITH: "true",
        CC_LANGSMITH_API_KEY: "<LangSmith API key>",
        CC_LANGSMITH_PROJECT: "claude-code",
        CC_LANGSMITH_PARENT_DOTTED_ORDER: runTree.dotted_order,
      },
    });
    return res.toString();
  },
  { name: "run_claude" },
);
```


The resulting trace hierarchy looks like:


```
Your outer run (chain)
└── Claude Code Turn (chain)
    ├── Claude (llm)
    ├── Read (tool)
    └── Claude (llm)
```


## [​](https://docs.langchain.com/langsmith/trace-claude-code#trace-to-multiple-destinations-replicas) Trace to multiple destinations (replicas)


You can trace to multiple LangSmith projects or workspaces simultaneously using the `CC_LANGSMITH_RUNS_ENDPOINTS` environment variable. Set `CC_LANGSMITH_RUNS_ENDPOINTS` to a JSON array of replica configurations. This overrides other client settings.
Tracing to multiple [replicas](https://docs.langchain.com/langsmith/log-traces-to-project) is useful for:


- Sending traces to both a production and staging project.
- Tracing to multiple workspaces with different API keys.
- Adding extra metadata to specific replica destinations.


Each replica object supports the following fields:


| Field | Required | Description |
| --- | --- | --- |
| `apiUrl` | Yes | LangSmith API URL (typically `https://api.smith.langchain.com`) |
| `apiKey` | Yes | API key for the destination [workspace](https://docs.langchain.com/langsmith/administration-overview#workspaces) |
| `projectName` | Yes | Project name in the destination workspace |
| `updates` | No | Optional metadata/fields to override on the replicated runs |


There are two ways to set the `CC_LANGSMITH_RUNS_ENDPOINTS` environment variable:


- Settings file (recommended)
- Shell environment variable

In your local `.claude/settings.local.json` or global `~/.claude/settings.json`:

```
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_RUNS_ENDPOINTS": "[{\"apiUrl\":\"https://api.smith.langchain.com\",\"apiKey\":\"ls__key_workspace_a\",\"projectName\":\"project-prod\"},{\"apiUrl\":\"https://api.smith.langchain.com\",\"apiKey\":\"ls__key_workspace_b\",\"projectName\":\"project-staging\",\"updates\":{\"metadata\":{\"environment\":\"staging\"}}}]"
  }
}
```

To generate the escaped JSON string, use:

```
echo '[{"apiUrl":"...","apiKey":"...","projectName":"..."}]' | jq -cR .
```

**Option 2: Shell environment variable** Add to your `~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`:

```
export CC_LANGSMITH_RUNS_ENDPOINTS='[{"apiUrl":"https://api.smith.langchain.com","apiKey":"ls__key_workspace_a","projectName":"project-prod"},{"apiUrl":"https://api.smith.langchain.com","apiKey":"ls__key_workspace_b","projectName":"project-staging","updates":{"metadata":{"environment":"staging"}}}]'
```


## [​](https://docs.langchain.com/langsmith/trace-claude-code#troubleshooting) Troubleshooting


### [​](https://docs.langchain.com/langsmith/trace-claude-code#no-traces-appearing-in-langsmith) No traces appearing in LangSmith


1. **Check the hook is running**: ``` tail -f ~/.claude/state/hook.log ``` You should see log entries after each Claude response.
2. **Verify environment variables**:
  - Check that `TRACE_TO_LANGSMITH="true"` in your project’s `.claude/settings.local.json`.
  - Verify your Personal Access Token (PAT) is correct (starts with `lsv2_pt_`).
  - Ensure the project name exists in LangSmith.3. **Enable debug mode** to see detailed API activity: ``` { "env": { "CC_LANGSMITH_DEBUG": "true" } } ``` Then check logs for API calls and HTTP status codes.


### [​](https://docs.langchain.com/langsmith/trace-claude-code#subagent-runs-do-not-appear-after-user-interruption) Subagent runs do not appear after user interruption


Subagents are only traced upon completion. This means if you interrupt a conversation turn in the middle of a subagent run, the subagent’s child runs will not be traced.


### [​](https://docs.langchain.com/langsmith/trace-claude-code#managing-log-file-size) Managing log file size


The hook logs all activity to `~/.claude/state/hook.log`. With debug mode enabled, this file can grow large:


```
# View log file size
ls -lh ~/.claude/state/hook.log

# Clear logs if needed
> ~/.claude/state/hook.log
```


## [​](https://docs.langchain.com/langsmith/trace-claude-code#migrating-from-the-manual-stop-hook) Migrating from the manual stop hook


If you were using the previous version of tracing Claude Code with LangSmith, you will need to remove `~/.claude/hooks/stop_hook.sh` and remove the reference to the hook from any previous `settings.local.json` or `settings.json` files you added it to previously, then follow the [plugin installation instructions](https://docs.langchain.com/langsmith/trace-claude-code#getting-started).


## [​](https://docs.langchain.com/langsmith/trace-claude-code#source-code) Source code


The plugin is open-source under the MIT license and is available in [this GitHub repo](https://github.com/langchain-ai/langsmith-claude-code-plugins).


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Prerequisites
## ​Getting started
## ​Verify setup
## ​Custom metadata
## ​Mute a thread
## ​Secret redaction
## ​Usage with GitHub Actions
## ​Nesting traces under an existing run
## ​Trace to multiple destinations (replicas)
## ​Troubleshooting
## ​Migrating from the manual stop hook
## ​Source code














Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Pipecat applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-pipecat`

# Trace Pipecat applications

This integration is in beta, so its API may change.
Trace your [Pipecat](https://pipecat.ai/) voice agents to LangSmith with the LangSmith Pipecat integration. For high-level conventions, see [Voice tracing fundamentals](https://docs.langchain.com/langsmith/trace-voice-fundamentals).
The Pipecat integration requires `langsmith[pipecat]>=0.9.7`.
The integration hooks into the spans Pipecat already emits and maps them onto LangSmith’s tracing format, so each conversation becomes a single LangSmith trace, with a span per pipeline stage (STT, LLM, TTS). This covers both the STT/LLM/TTS cascade and speech-to-speech (realtime) models. Realtime models (for example, `OpenAIRealtimeLLMService`) need one extra call to capture the user’s transcript. See [When using Pipecat with a realtime model](https://docs.langchain.com/langsmith/trace-with-pipecat#when-using-pipecat-with-a-realtime-model).


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#install) Install


Install the integration along with the Pipecat service extras your pipeline uses:
pip uv

```
pip install "langsmith[pipecat]" "pipecat-ai[openai,local,tracing]"
```


```
uv add "langsmith[pipecat]" "pipecat-ai[openai,local,tracing]"
```


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#set-environment-variables) Set environment variables


The integration reads your LangSmith credentials from the environment and exports to LangSmith for you via OpenTelemetry:
.env

```
LANGSMITH_API_KEY=<your-langsmith-api-key>
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=pipecat-voice
OPENAI_API_KEY=<your-openai-api-key>
```


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#set-up-tracing) Set up tracing


Import `configure_pipecat` and call it once before building your pipeline. Enable tracing on the `PipelineTask`:


```
from langsmith.integrations.pipecat import configure_pipecat
from pipecat.pipeline.task import PipelineParams, PipelineTask

# Install the tracer and the LangSmith span processor.
configure_pipecat()

task = PipelineTask(
    pipeline,
    params=PipelineParams(enable_metrics=True),
    enable_tracing=True,
    enable_turn_tracking=True,
    conversation_id=conversation_id,
)
```


Set `enable_tracing=True`, `enable_turn_tracking=True`, and `enable_metrics=True`. Turn tracking is required for tracing, and metrics drive the latency and token data on each span.


### [​](https://docs.langchain.com/langsmith/trace-with-pipecat#use-a-langgraph-or-langchain-agent-as-the-llm) Use a LangGraph or LangChain agent as the LLM


If your LLM stage is an in-process [LangGraph or LangChain](https://docs.langchain.com/oss/python/langgraph/overview) agent, its model and tool runs should nest inside Pipecat’s `llm` span rather than forming a separate trace. To achieve this:


- Pass `configure_pipecat(llm_span_kind="chain")`. This avoids nested `llm` spans that don’t actually represent inference requests.
- Set `LANGSMITH_TRACING_MODE=otel` in the environment. Without it, those runs post to LangSmith directly and form a separate trace instead of nesting.


### [​](https://docs.langchain.com/langsmith/trace-with-pipecat#use-your-own-tracer-provider) Use your own tracer provider


`configure_pipecat()` builds a `TracerProvider`, registers the LangSmith span processor, and wires it into Pipecat. To send spans through a `TracerProvider` you already manage (for example, one that also exports to another OpenTelemetry backend), skip `configure_pipecat` and add the processor to your provider directly:


```
from langsmith.integrations.pipecat import PipecatLangSmithSpanProcessor

provider.add_span_processor(PipecatLangSmithSpanProcessor())
```


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#group-a-conversation-into-a-thread) Group a conversation into a thread


To group a conversation’s runs into a LangSmith [thread](https://docs.langchain.com/langsmith/threads) for thread-level views and token and cost aggregation, call `set_thread_id` once per conversation before its spans are emitted:


```
from langsmith.integrations.pipecat import configure_pipecat, set_thread_id

configure_pipecat()
set_thread_id(conversation_id)
```


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#when-using-pipecat-with-a-realtime-model) When using Pipecat with a realtime model


With a speech-to-speech (realtime) model there is no separate speech-to-text stage, so the user’s transcript is never emitted as an OTel span. Instead it arrives through the user context aggregator’s `on_user_turn_message_added` callback, which Pipecat fires once it has the finalized user text. Without wiring it up, the trace shows only the assistant side.
Call `instrument_user_aggregator` once, right after building the context aggregator, so the SDK subscribes to that callback for you and pairs each transcript with its turn. It correlates by the id you pass to `set_thread_id`, so set that first and pass the same id:
`instrument_user_aggregator` requires `langsmith[pipecat]>=0.10.6`.


```
from langsmith.integrations.pipecat import configure_pipecat, set_thread_id
from pipecat.processors.aggregators.llm_context import LLMContext
from pipecat.processors.aggregators.llm_response_universal import LLMContextAggregatorPair
from pipecat.services.openai.realtime.events import (
    AudioConfiguration,
    AudioInput,
    AudioOutput,
    InputAudioTranscription,
    SessionProperties,
)
from pipecat.services.openai.realtime.llm import OpenAIRealtimeLLMService

conversation_id = "..."  # any id that identifies the conversation
span_processor = configure_pipecat()
set_thread_id(conversation_id)

llm = OpenAIRealtimeLLMService(
    api_key=openai_api_key,
    settings=OpenAIRealtimeLLMService.Settings(
        model="gpt-realtime",
        session_properties=SessionProperties(
            # Enable input-audio transcription: OpenAI Realtime sends the model
            # raw audio and, by default, produces no user-side text. Without this
            # the context aggregator never fires, so the user's turns never reach
            # the trace.
            audio=AudioConfiguration(
                input=AudioInput(transcription=InputAudioTranscription()),
                output=AudioOutput(voice="marin"),
            ),
        ),
    ),
)

context = LLMContext(messages=[{"role": "system", "content": "..."}])
context_aggregator = LLMContextAggregatorPair(context, realtime_service_mode=True)
span_processor.instrument_user_aggregator(context_aggregator, conversation_id)  # capture the user transcript
```


For OpenAI Realtime, also enable input-audio transcription (`InputAudioTranscription`) on the session; otherwise the model receives raw audio and produces no user-side text, so the aggregator never fires. Other realtime services that surface the user’s text through the aggregator themselves (for example, Gemini Live) need only the `instrument_user_aggregator` call, with no extra session configuration.
Only call `instrument_user_aggregator` for realtime models. In the STT/LLM/TTS cascade the transcript is already captured (from the speech-to-text stage), so calling it there would record the user’s turns a second time.


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#record-the-conversation-audio) Record the conversation audio


Attach the conversation audio to the trace using Pipecat’s [`AudioBufferProcessor`](https://docs.pipecat.ai/server/utilities/audio/audio-recording). Place it after `transport.output()` so it captures what was actually played (after any barge-in truncation), hand it to the integration, and start it once the session is running:


```
from pipecat.processors.audio.audio_buffer_processor import AudioBufferProcessor

span_processor = configure_pipecat()

# Stereo: user on the left channel, agent on the right.
audiobuffer = AudioBufferProcessor(num_channels=2, buffer_size=32_000)
span_processor.attach_audio_buffer(audiobuffer, conversation_id=conversation_id)

pipeline = Pipeline([
    transport.input(),
    stt,
    context_aggregator.user(),
    llm,
    tts,
    transport.output(),
    audiobuffer,                     # after output(): records what was heard
    context_aggregator.assistant(),
])

await audiobuffer.start_recording()
```


The integration attaches the recording to the conversation root when it ends. For the underlying attachment API, see [Upload files with traces](https://docs.langchain.com/langsmith/upload-files-with-traces).


## [​](https://docs.langchain.com/langsmith/trace-with-pipecat#next-steps) Next steps


## Voice fundamentals

Core conventions for tracing voice agents.

## Upload files with traces

Attach the conversation audio recording to your trace.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-pipecat.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Install
## ​Set environment variables
## ​Set up tracing
## ​Group a conversation into a thread
## ​When using Pipecat with a realtime model
## ​Record the conversation audio
## ​Next steps









Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenAI Codex sessions - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-codex`

# Trace OpenAI Codex sessions
## Documentation Index
## ​Prerequisites
## ​Install and enable the plugin
## ​Configure tracing
## ​Trace to multiple destinations
## ​Secret redaction
## ​What gets traced
## ​View traces in LangSmith
## ​Troubleshooting










Capture OpenAI Codex agent turns, tool calls, model metadata, and subagent threads in LangSmith.

The [`langsmith-codex-plugins`](https://github.com/langchain-ai/langsmith-codex-plugins) marketplace ships a tracing plugin that sends [OpenAI Codex](https://developers.openai.com/codex) session data to LangSmith. Use it to inspect agent turns, model metadata, token usage, tool calls, and subagent threads from your Codex workflows.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- [Node.js](https://nodejs.org/) 22.x or later.
- [Codex CLI](https://developers.openai.com/codex/quickstart?setup=cli) v0.153.4 or later, with synchronous `UserPromptSubmit` plugin hooks enabled and trusted.
- A [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key).


## [​](https://docs.langchain.com/langsmith/trace-with-codex#install-and-enable-the-plugin) Install and enable the plugin


Add the marketplace using the Codex CLI:


```
codex plugin marketplace add langchain-ai/langsmith-codex-plugins
```


Enable the tracing plugin globally in `~/.codex/config.toml`, or only for a specific project in `.codex/config.toml`:


```
[plugins."tracing@langsmith-codex-plugins"]
enabled = true
```


Then trust this plugin’s hooks with `/hooks`, or in Codex’s plugin UI when prompted. Enabling the plugin alone does not trust its hooks.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#configure-tracing) Configure tracing


Tracing is disabled until either `TRACE_TO_LANGSMITH` is `"true"` or `enabled` is `true` in a config file. Configure credentials with environment variables, a JSON config file, or both.


### [​](https://docs.langchain.com/langsmith/trace-with-codex#environment-variables) Environment variables


The plugin reads Codex-specific variables first, then falls back to the generic LangSmith SDK variables.


| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `TRACE_TO_LANGSMITH` | Yes | - | Set to `"true"` to enable tracing. |
| `LANGSMITH_CODEX_API_KEY` | Conditional | - | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. Required unless every replica provides its own API key. |
| `LANGSMITH_CODEX_ENDPOINT` | No | `https://api.smith.langchain.com` | LangSmith API URL. Falls back to `LANGSMITH_ENDPOINT`. |
| `LANGSMITH_CODEX_PROJECT` | No | `codex` | LangSmith project name. Falls back to `LANGSMITH_PROJECT`. |
| `LANGSMITH_CODEX_METADATA` | No | - | JSON object merged into root trace metadata. Falls back to `LANGSMITH_METADATA`. |
| `LANGSMITH_CODEX_RUNS_ENDPOINTS` | No | - | JSON array of replica destinations. Falls back to `LANGSMITH_RUNS_ENDPOINTS`. |
| `LANGSMITH_CODEX_REDACT` | No | `true` | Set to a falsy value to disable secret redaction. Falls back to `LANGSMITH_REDACT`. |
| `LANGSMITH_CODEX_REDACT_EXTRA` | No | - | JSON array of extra `{ pattern, replace }` redaction rules. Falls back to `LANGSMITH_REDACT_EXTRA`. |


Add the variables to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):


```
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_CODEX_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_CODEX_PROJECT="codex"
```


### [​](https://docs.langchain.com/langsmith/trace-with-codex#config-file) Config file


Use `<project>/.codex/langsmith.json` for project-level settings or `~/.codex/langsmith.json` for global defaults. The global file loads first, the project file overrides it, and matching environment variables take precedence over both.


```
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "codex",
  "metadata": {
    "team": "agents",
    "environment": "dev"
  }
}
```


| Field | Environment variable | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `TRACE_TO_LANGSMITH` | `false` | Set to `true` to enable tracing. |
| `api_key` | `LANGSMITH_CODEX_API_KEY`, `LANGSMITH_API_KEY` | - | LangSmith API key. |
| `api_url` | `LANGSMITH_CODEX_ENDPOINT`, `LANGSMITH_ENDPOINT` | LangSmith default | LangSmith API URL. |
| `project` | `LANGSMITH_CODEX_PROJECT`, `LANGSMITH_PROJECT` | `codex` | LangSmith project name. |
| `metadata` | `LANGSMITH_CODEX_METADATA`, `LANGSMITH_METADATA` | - | Object merged into root trace metadata. |
| `replicas` | `LANGSMITH_CODEX_RUNS_ENDPOINTS`, `LANGSMITH_RUNS_ENDPOINTS` | - | Additional LangSmith destinations to replicate traces to. |
| `redact` | `LANGSMITH_CODEX_REDACT`, `LANGSMITH_REDACT` | `true` | Set to `false` to disable [secret redaction](https://docs.langchain.com/langsmith/trace-with-codex#secret-redaction). |
| `redact_extra_rules` | `LANGSMITH_CODEX_REDACT_EXTRA`, `LANGSMITH_REDACT_EXTRA` | - | Extra `{ pattern, replace }` rules applied after the built-in ones. |


Keep config files that include API keys out of version control.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#trace-to-multiple-destinations) Trace to multiple destinations


Set `replicas` in `langsmith.json` or `LANGSMITH_CODEX_RUNS_ENDPOINTS` to send the same trace data to additional LangSmith workspaces or projects. When set, the replica list overrides the other client settings.
Tracing to multiple [replicas](https://docs.langchain.com/langsmith/log-traces-to-project) is useful for:


- Sending traces to both a production and staging project.
- Tracing to multiple workspaces with different API keys.
- Adding extra metadata to specific replica destinations.


- Config file (recommended)
- Shell environment variable

In `<project>/.codex/langsmith.json` or `~/.codex/langsmith.json`:

```
{
  "enabled": true,
  "replicas": [
    {
      "apiUrl": "https://api.smith.langchain.com",
      "apiKey": "lsv2_pt_workspace_a",
      "projectName": "project-prod"
    },
    {
      "apiUrl": "https://api.smith.langchain.com",
      "apiKey": "lsv2_pt_workspace_b",
      "projectName": "project-staging",
      "updates": { "metadata": { "environment": "staging" } }
    }
  ]
}
```


```
export LANGSMITH_CODEX_RUNS_ENDPOINTS='[{"apiUrl":"https://api.smith.langchain.com","apiKey":"lsv2_pt_workspace_a","projectName":"project-prod"},{"apiUrl":"https://api.smith.langchain.com","apiKey":"lsv2_pt_workspace_b","projectName":"project-staging","updates":{"metadata":{"environment":"staging"}}}]'
```

To generate the escaped JSON string, use:

```
echo '[{"apiUrl":"...","apiKey":"...","projectName":"..."}]' | jq -c .
```


Each replica object supports the following fields:


| Field | Required | Description |
| --- | --- | --- |
| `apiUrl` | Yes | LangSmith API URL (typically `https://api.smith.langchain.com`). |
| `apiKey` | Yes | API key for the destination workspace. |
| `projectName` | Yes | Project name in the destination workspace. |
| `updates` | No | Optional run fields to override on replicated runs, such as extra metadata. |


## [​](https://docs.langchain.com/langsmith/trace-with-codex#secret-redaction) Secret redaction


The plugin redacts detected secrets from run inputs, outputs, errors, and metadata before uploading them to LangSmith. Redaction is on by default.
Redaction runs on your machine before upload, so unredacted content never reaches LangSmith. Replica destinations receive the same redacted payload.
Detection covers provider API key prefixes, JSON Web Tokens, and PEM private key blocks. It also covers contextual shapes such as `API_KEY=<value>`, an `Authorization` header, and a password embedded in a URL. Each match is replaced with `[SECRET_DETECTED]`. For the rule list, see [Redact secrets from traces](https://docs.langchain.com/langsmith/redact-secrets#rules-in-the-preset).
Redaction matches known credential shapes, so treat it as a safety net rather than a guarantee. A credential in an unrecognized format still reaches LangSmith, and attachments, run names, and tags do not pass through the anonymizer. A redacted trace also still holds the prompts, file contents, and tool results it was built from, so restrict who can read the tracing project.
To turn redaction off, set `LANGSMITH_CODEX_REDACT` to `false`, `0`, `no`, or `off`, or set `"redact": false` in a config file. Values are trimmed and compared case-insensitively.
To redact additional patterns, set `LANGSMITH_CODEX_REDACT_EXTRA` to a JSON array of `{ "pattern": ..., "replace": ... }` rules, or set `redact_extra_rules` in a config file. Each `pattern` is a regular expression string, applied globally and case-sensitively. `replace` is optional and falls back to `[redacted]`. Extra rules run after the built-in ones.


```
{
  "enabled": true,
  "project": "codex",
  "redact": true,
  "redact_extra_rules": [{ "pattern": "ACME-[A-Z0-9]{16}", "replace": "[REDACTED_ACME_KEY]" }]
}
```


Setting `redact_extra_rules` to `[]` clears rules inherited from a lower-priority source. In a config file, one rule with an invalid regular expression discards every setting in that file, so verify the patterns before committing them.
Because a project-level `.codex/langsmith.json` or `langsmith-plugins.json` can set `redact` to `false`, review those files before enabling tracing in a repository you do not control.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#what-gets-traced) What gets traced


Each LLM run includes:


- **Inputs**: accumulated conversation messages.
- **Outputs**: assistant response content.
- **Metadata**: model provider, model name, stop reason, and token usage.


Tool calls (function calls, shell calls, computer calls, file reads, web searches) are included with their inputs and outputs. Subagent threads are resolved and uploaded as nested child runs under the parent turn.
Interrupted turns where the user cancels mid-response are still uploaded once the session completes.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#view-traces-in-langsmith) View traces in LangSmith


Open the configured LangSmith project and complete a Codex turn. By default traces appear in the `codex` project. The plugin uploads completed Codex transcript data, including messages, tool call inputs and outputs, model metadata, token usage, and subagent thread structure.
The plugin uploads full Codex transcript data to LangSmith. Do not enable tracing for sessions that contain data you do not want stored in LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-with-codex#troubleshooting) Troubleshooting


If traces do not appear in LangSmith:


- Confirm the tracing plugin is enabled in `config.toml` and its hooks are trusted (`/hooks`). `[features] hooks` is on by default, so set it only to undo a local override.
- Confirm `TRACE_TO_LANGSMITH=true` is visible to the Codex process.
- Confirm `LANGSMITH_CODEX_API_KEY` or `LANGSMITH_API_KEY` is set and valid.
- If runs land in the wrong project, set `LANGSMITH_CODEX_PROJECT` or the `project` config key.
- If a custom endpoint is not used, set `LANGSMITH_CODEX_ENDPOINT` or the `api_url` config key.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-codex.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace OpenCode sessions - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-opencode`

# Trace OpenCode sessions
## Documentation Index
## ​Prerequisites
## ​Install and enable the plugin
## ​Configure tracing
## ​Trace to multiple destinations
## ​What gets traced
## ​View traces in LangSmith
## ​Troubleshooting









Capture OpenCode sessions, assistant turns, tool calls, and subagent activity in LangSmith.

The `@langchain/langsmith-opencode` plugin sends [OpenCode](https://opencode.ai/) session traces to LangSmith. Use it to inspect agent turns, model metadata, token usage, tool calls, tool errors, attachments, and subagent activity from your OpenCode workflows.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- [OpenCode](https://opencode.ai/) installed and configured.
- A [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key).
- Access to configure the OpenCode `plugin` key in `opencode.json` or `~/.config/opencode/opencode.json`.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#install-and-enable-the-plugin) Install and enable the plugin


Add the plugin to your OpenCode configuration file. You can configure it locally in `opencode.json` or globally in `~/.config/opencode/opencode.json`:


```
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@langchain/langsmith-opencode"]
}
```


Enable tracing and provide your LangSmith API key before starting OpenCode:


```
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_PROJECT="opencode"
```


Run OpenCode as usual. The plugin sends completed user turns to the configured LangSmith project.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#configure-tracing) Configure tracing


Tracing is disabled by default. With `TRACE_TO_LANGSMITH=true` set, the plugin sends traces to LangSmith. You can also enable tracing with a LangSmith config file.


### [​](https://docs.langchain.com/langsmith/trace-with-opencode#environment-variables) Environment variables


The plugin reads OpenCode-specific variables first, then falls back to the generic LangSmith SDK variables when available.


| Variable | Required | Default | Description |
| --- | --- | --- | --- |
| `TRACE_TO_LANGSMITH` | Yes | `false` | Set to `"true"` to enable tracing. |
| `LANGSMITH_OPENCODE_API_KEY` | Conditional | - | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. Required unless every replica provides its own API key. |
| `LANGSMITH_OPENCODE_ENDPOINT` | No | LangSmith SDK default | LangSmith API URL. Falls back to `LANGSMITH_ENDPOINT`. |
| `LANGSMITH_OPENCODE_PROJECT` | No | `opencode` | LangSmith project name. Falls back to `LANGSMITH_PROJECT`. |
| `LANGSMITH_OPENCODE_METADATA` | No | - | JSON object merged into root trace metadata. |
| `LANGSMITH_OPENCODE_RUNS_ENDPOINTS` | No | - | JSON array of replica destinations. |


For example:


```
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_PROJECT="opencode"
export LANGSMITH_OPENCODE_METADATA='{"team":"agents","environment":"dev"}'
```


### [​](https://docs.langchain.com/langsmith/trace-with-opencode#config-files) Config files


Use `.opencode/langsmith.json` for project-level settings or `~/.config/opencode/langsmith.json` for global defaults.


```
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "opencode",
  "metadata": {
    "team": "agents",
    "environment": "dev"
  }
}
```


| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `enabled` | Yes | `false` | Set to `true` to enable tracing from the config file. |
| `api_key` | Conditional | - | LangSmith API key. Required unless provided by environment variable or replicas. |
| `api_url` | No | LangSmith SDK default | LangSmith API URL, usually `https://api.smith.langchain.com`. |
| `project` | No | `opencode` | LangSmith project name. |
| `metadata` | No | - | Object merged into root trace metadata. |
| `replicas` | No | - | Additional LangSmith destinations to replicate traces to. |


Keep config files that include API keys out of version control.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#trace-to-multiple-destinations) Trace to multiple destinations


Set `replicas` in `langsmith.json` or `LANGSMITH_OPENCODE_RUNS_ENDPOINTS` to send the same trace data to additional LangSmith workspaces or projects.


```
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "project": "opencode",
  "replicas": [
    {
      "api_url": "https://api.smith.langchain.com",
      "api_key": "<your-replica-langsmith-api-key>",
      "project": "opencode-replica",
      "updates": {
        "metadata": {
          "replica": true
        }
      }
    }
  ]
}
```


Replica objects support both snake_case and LangSmith SDK-style camelCase field names. snake_case is recommended in config files.


| Field | Description |
| --- | --- |
| `api_url` / `apiUrl` | LangSmith API URL for the replica destination. |
| `api_key` / `apiKey` | API key for the destination workspace. |
| `project` / `projectName` | Project name in the destination workspace. |
| `updates` | Optional run fields to override on replicated runs, such as extra metadata. |


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#what-gets-traced) What gets traced


The plugin listens to OpenCode chat and event hooks, aggregates each completed user turn, and submits it to LangSmith as a run tree.


- `opencode.session` root runs for completed user turns.
- `opencode.assistant.turn` child runs for assistant and model responses.
- Nested tool runs for tool calls, including inputs, outputs, errors, timing, and attachments when available.
- Subagent sessions nested under the parent tool call.
- Model name, provider, invocation parameters, token usage, and thread or session ID metadata.
- User messages, assistant messages, reasoning blocks, file parts, and system prompts associated with assistant turns.


Trace completion is based on OpenCode `step-finish` events. The plugin also flushes pending trace batches when the OpenCode server shuts down.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#view-traces-in-langsmith) View traces in LangSmith


Open the configured LangSmith project and look for root runs named `opencode.session`. Each trace contains the user turn as the root input and assistant responses, tool calls, and subagent traces as child runs. The plugin stores the OpenCode session ID as `thread_id` metadata, so you can filter or group related OpenCode turns in LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-with-opencode#troubleshooting) Troubleshooting


If traces do not appear in LangSmith:


- Confirm tracing is enabled with `TRACE_TO_LANGSMITH=true` or `"enabled": true` in config.
- Confirm the LangSmith API key is set in the same shell, project config, or global config used by OpenCode.
- Confirm the plugin package is installed where OpenCode can resolve it.
- Check the selected LangSmith project. If no project is configured, traces go to `opencode`.
- Restart OpenCode after changing `opencode.json`, `langsmith.json`, or environment variables.
- Make sure a user turn completes. The plugin does not send incomplete turns.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-opencode.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Cursor sessions - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-cursor`

# Trace Cursor sessions
## Documentation Index
## ​Prerequisites
## ​Install and enable the plugin
## ​Configure tracing
## ​Secret redaction
## ​What gets traced
## ​View traces in LangSmith
## ​Known limitations
## ​Troubleshooting










Capture Cursor agent turns, tool calls, model metadata, token usage, attachments, and subagents in LangSmith.

Trace [Cursor](https://cursor.com/) agent sessions in LangSmith using [Cursor hooks](https://cursor.com/docs/agent/hooks). Each turn becomes one trace, grouped into a thread per Cursor conversation, which captures prompts, model responses, tool calls, token usage, and subagent activity. Use the traces to debug agent behavior, audit tool calls, track token spend per turn, and compare Cursor runs.
The plugin source is available at [`langchain-ai/langsmith-cursor-plugins`](https://github.com/langchain-ai/langsmith-cursor-plugins).


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- [Cursor](https://cursor.com/) installed.
- [Node.js](https://nodejs.org/) 22.13 or later. The hooks use the built-in `node:sqlite` module to recover attachments from Cursor’s local database.
- A [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key).


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#install-and-enable-the-plugin) Install and enable the plugin


Install the plugin directly from the GitHub repository in Cursor’s settings:


1. Open **Cursor > Settings > Plugins**.
2. Paste `https://github.com/langchain-ai/langsmith-cursor-plugins` into the plugin link field.
3. Confirm to add **LangSmith Tracing for Cursor**.


This is the recommended path: it installs the hooks with no clone or build step, since the repository ships a precompiled bundle.
Fully restart Cursor after installing so it reloads `hooks.json`.


### [​](https://docs.langchain.com/langsmith/trace-with-cursor#alternative-install-from-a-local-clone) Alternative: install from a local clone


Install the hooks from a local clone of [`langsmith-cursor-plugins`](https://github.com/langchain-ai/langsmith-cursor-plugins). This writes `~/.cursor/hooks.json` for all Cursor projects:


```
node scripts/install.mjs
```


To scope the hooks to a single project instead, run the installer from the project directory:


```
node scripts/install.mjs --project
```


To preview the hook configuration without writing it, run:


```
node scripts/install.mjs --print
```


The installer merges its entries with any existing `hooks.json`. The committed `bundle/` means these commands run without `pnpm install` or `pnpm build` — those are only needed when contributing changes to the TypeScript source.
Restart Cursor after installing so it reloads `hooks.json`.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#configure-tracing) Configure tracing


Tracing is disabled until both `enabled` (or `TRACE_TO_LANGSMITH=true`) and an API key are set. Configure credentials with [environment variables](https://docs.langchain.com/langsmith/trace-with-cursor#environment-variables), a [JSON config file](https://docs.langchain.com/langsmith/trace-with-cursor#config-file), or both.


### [​](https://docs.langchain.com/langsmith/trace-with-cursor#environment-variables) Environment variables


Every `LANGSMITH_CURSOR_*` variable also accepts the shorter `LANGSMITH_*` form. When both are set, `LANGSMITH_CURSOR_*` takes precedence.


| Variable | Default | Description |
| --- | --- | --- |
| `TRACE_TO_LANGSMITH` | `false` | Set to `"true"` to enable tracing. |
| `LANGSMITH_CURSOR_API_KEY` | - | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. |
| `LANGSMITH_CURSOR_ENDPOINT` | `https://api.smith.langchain.com` | LangSmith API URL. Falls back to `LANGSMITH_ENDPOINT`. |
| `LANGSMITH_CURSOR_PROJECT` | `cursor` | LangSmith project name. Falls back to `LANGSMITH_PROJECT`. |
| `LANGSMITH_CURSOR_METADATA` | - | JSON object merged into root trace metadata. |
| `LANGSMITH_CURSOR_RUNS_ENDPOINTS` | - | JSON array of replica destinations. |
| `LANGSMITH_CURSOR_REDACT` | `true` | Set to `"false"` to disable secret redaction. |
| `LANGSMITH_CURSOR_REDACT_EXTRA` | - | JSON array of extra `{ pattern, replace }` redaction rules. |
| `LANGSMITH_CURSOR_ATTACHMENTS` | `true` | Set to `"false"` to disable attachment enrichment. |
| `LANGSMITH_CURSOR_DB_PATH` | platform default | Override the Cursor `state.vscdb` path used for attachments. |
| `LANGSMITH_CURSOR_STATE_FILE` | `~/.cursor/langsmith-state.json` | Override the on-disk event-buffer state file. |
| `LANGSMITH_CURSOR_LOG_FILE` | `~/.cursor/langsmith-hook.log` | Override the hook log file. |
| `LANGSMITH_CURSOR_DEBUG` | `false` | Set to `"true"` to enable verbose hook logging. |


Add the variables to your shell configuration file (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):


```
export TRACE_TO_LANGSMITH="true"
export LANGSMITH_CURSOR_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_CURSOR_PROJECT="cursor"
```


To verify hook activity, tail the log file:


```
tail -f ~/.cursor/langsmith-hook.log
```


### [​](https://docs.langchain.com/langsmith/trace-with-cursor#config-file) Config file


Use `~/.cursor/langsmith.json` for global defaults or `./.cursor/langsmith.json` for project-level settings. Settings resolve in this order, with later sources overriding earlier ones: defaults, global config, project config, environment variables.


```
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "cursor"
}
```


| Field | Environment variable | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `TRACE_TO_LANGSMITH` | `false` | Set to `true` to enable tracing. |
| `api_key` | `LANGSMITH_CURSOR_API_KEY`, `LANGSMITH_API_KEY` | - | LangSmith API key. |
| `api_url` | `LANGSMITH_CURSOR_ENDPOINT`, `LANGSMITH_ENDPOINT` | `https://api.smith.langchain.com` | LangSmith API URL. |
| `project` | `LANGSMITH_CURSOR_PROJECT`, `LANGSMITH_PROJECT` | `cursor` | LangSmith project name. |
| `metadata` | `LANGSMITH_CURSOR_METADATA`, `LANGSMITH_METADATA` | - | Object merged into root trace metadata. |
| `replicas` | `LANGSMITH_CURSOR_RUNS_ENDPOINTS`, `LANGSMITH_RUNS_ENDPOINTS` | - | Additional LangSmith destinations to replicate traces to. |
| `redact` | `LANGSMITH_CURSOR_REDACT`, `LANGSMITH_REDACT` | `true` | Set to `false` to disable [secret redaction](https://docs.langchain.com/langsmith/trace-with-cursor#secret-redaction). |
| `redact_extra_rules` | `LANGSMITH_CURSOR_REDACT_EXTRA`, `LANGSMITH_REDACT_EXTRA` | - | Extra `{ pattern, replace }` rules applied after the built-in ones. |
| `attachments` | `LANGSMITH_CURSOR_ATTACHMENTS` | `true` | Set to `false` to skip enriching turns with image and file attachment bytes from Cursor’s local database. |
| `cursor_db_path` | `LANGSMITH_CURSOR_DB_PATH` | platform default | Override the Cursor `state.vscdb` path used for attachments. |


Keep config files that include API keys out of version control.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#secret-redaction) Secret redaction


The plugin redacts detected secrets from run inputs, outputs, errors, and metadata before uploading them to LangSmith. Redaction is on by default.
Redaction runs on your machine before upload, so unredacted content never reaches LangSmith. Replica destinations receive the same redacted payload.
Detection covers provider API key prefixes, JSON Web Tokens, and PEM private key blocks. It also covers contextual shapes such as `API_KEY=<value>`, an `Authorization` header, and a password embedded in a URL. Each match is replaced with `[SECRET_DETECTED]`. For the rule list, see [Redact secrets from traces](https://docs.langchain.com/langsmith/redact-secrets#rules-in-the-preset).
Redaction matches known credential shapes, so treat it as a safety net rather than a guarantee. A credential in an unrecognized format still reaches LangSmith, and attachments, run names, and tags do not pass through the anonymizer. A redacted trace also still holds the prompts, file contents, and tool results it was built from, so restrict who can read the tracing project.
Attachments bypass redaction entirely. The plugin recovers image and file attachments from Cursor’s local database and sends their bytes, which the anonymizer never inspects. Set `LANGSMITH_CURSOR_ATTACHMENTS` to `"false"` to stop sending them.
To turn redaction off, set `LANGSMITH_CURSOR_REDACT` to `false`, `0`, `no`, or `off`, or set `"redact": false` in a config file.
To redact additional patterns, set `LANGSMITH_CURSOR_REDACT_EXTRA` to a JSON array of `{ "pattern": ..., "replace": ... }` rules, or set `redact_extra_rules` in a config file. Each `pattern` is a regular expression string, applied globally and case-sensitively. `replace` is optional and falls back to `[redacted]`. Extra rules run after the built-in ones.


```
{
  "enabled": true,
  "project": "cursor",
  "redact": true,
  "redact_extra_rules": [{ "pattern": "ACME-[A-Z0-9]{16}", "replace": "[REDACTED_ACME_KEY]" }]
}
```


Setting `redact_extra_rules` to `[]` clears rules inherited from a lower-priority source. One rule with an invalid regular expression discards every setting in that file, so keep the patterns simple and verify them before committing.
Because a project-level `.cursor/langsmith.json` can set `redact` to `false`, review that file before enabling tracing in a repository you do not control.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#what-gets-traced) What gets traced


The plugin listens to Cursor hooks and assembles one trace per agent turn:


- **Turns**: each turn becomes its own trace, grouped into a thread using `thread_id` = Cursor’s `conversation_id`. The trace nests the model run and any tool or subagent runs underneath the turn.
- **Token usage**: per-turn `usage_metadata` on the model run.
- **Model and provider**: `ls_model_name` and `ls_provider`, normalized from Cursor’s model label to a canonical provider id (for example, `claude-4.6-sonnet` becomes `claude-sonnet-4-6`). Auto mode reports `default` with provider `cursor`.
- **Tool calls**: tool runs for both successful calls and failures, with inputs and outputs.
- **Attachments**: image and file attachments recovered from Cursor’s local database and rendered inline on the user message. Set `attachments` to `false` to skip this step.
- **Subagents**: each subagent appears as a nested chain run with its own tool calls underneath, linked to the parent turn.


The plugin does not compute cost locally. Because `ls_model_name` is normalized to a canonical id and `usage_metadata` carries the token breakdown, LangSmith’s server-side model price table renders cost in the UI. Auto mode reports `default`, which LangSmith cannot price.
The plugin uploads Cursor conversation data, including prompts, model responses, tool inputs and outputs, and recovered attachments. Do not enable tracing for sessions that contain data you do not want stored in LangSmith.


### [​](https://docs.langchain.com/langsmith/trace-with-cursor#trace-metadata) Trace metadata


Every run carries the shared `coding-agent-v1` metadata contract on `run.extra.metadata`, which lets traces from any coding agent (Claude Code, Codex, Cursor) be identified and grouped with the same stable keys.


| Scope | Keys |
| --- | --- |
| Always present | `ls_agent_type` (`"root"`, `"subagent"`, `"middleware"`, or `"compaction"`), `ls_agent_purpose` (`"coding"`), `ls_integration` (`"cursor"`), `ls_agent_runtime` (`"Cursor"`), `ls_trace_schema_version` (`"coding-agent-v1"`), `thread_id` (= Cursor’s `conversation_id`). |
| Present where known | `ls_integration_version`, `ls_agent_runtime_version` (Cursor’s `cursor_version`), `turn_id` (= Cursor’s `generation_id`), `turn_number`, `repository_url`, `repository_provider`, `repository_name`, `git_branch`, `git_commit_sha`, `cwd`. |
| Contextual | `local_username`, `user_email` (provisional). |
| Subagent runs only | `ls_subagent_id`, `ls_subagent_type`. |
| Tool runs only | `ls_tool_name` (only emitted when the run name differs from the native tool name). |
| Model and tool runs only | `ls_provider`, `ls_model_name`, `ls_invocation_params`, `usage_metadata`. |


Cursor’s hooks do not expose stable sources for `user_id`, `sandbox_type`, or `approval_policy`, so those keys are omitted.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#view-traces-in-langsmith) View traces in LangSmith


Open the configured LangSmith project (default `cursor`) and complete a Cursor turn. The plugin uploads one trace per turn with this structure:


```
Cursor Turn N (chain)
├── <provider> (llm)   model and provider, token usage, assistant text
├── Read / Shell / ... (tool)
└── Task (tool)        subagent (type and task)
```


To group related turns, filter on `thread_id` in the **Threads** tab of the project.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#known-limitations) Known limitations


- **Subagent token usage**: Cursor does not expose a per-subagent usage breakdown via hooks or its local database, so a subagent’s `Task` run carries its tool calls but no token counts.


## [​](https://docs.langchain.com/langsmith/trace-with-cursor#troubleshooting) Troubleshooting


If traces do not appear in LangSmith:


- Confirm `TRACE_TO_LANGSMITH=true` or `"enabled": true` is set in a config file the Cursor process can see.
- Confirm `LANGSMITH_CURSOR_API_KEY` or `LANGSMITH_API_KEY` is set and valid.
- Confirm Cursor was fully restarted after the hooks were installed.
- Tail the hook log for errors: `tail -f ~/.cursor/langsmith-hook.log`.
- Enable verbose logging with `LANGSMITH_CURSOR_DEBUG=true` and re-check the log.
- If runs land in the wrong project, set `LANGSMITH_CURSOR_PROJECT` or the `project` config key.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-cursor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Pi coding agent sessions - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-pi`

# Trace Pi coding agent sessions
## Documentation Index
## ​Prerequisites
## ​Installation
## ​Quick start
## ​Configuration
## ​Replicas







Trace Pi coding agent invocations to LangSmith to observe turns, debug tool calls, track token usage, and inspect individual LLM invocations.

This guide shows you how to trace [Pi coding agent](https://pi.dev) sessions to LangSmith using the `@langchain/langsmith-pi-extension` extension.
Once configured, each Pi session sends traces to LangSmith. Each trace includes user messages, assistant responses, tool calls, and individual LLM invocations, which gives you full observability into your Pi coding agent runs.


## [​](https://docs.langchain.com/langsmith/trace-with-pi#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- [**Pi**](https://pi.dev) installed.
- A [**LangSmith API key**](https://docs.langchain.com/langsmith/create-account-api-key).


## [​](https://docs.langchain.com/langsmith/trace-with-pi#installation) Installation


Install the extension via Pi:


```
pi install npm:@langchain/langsmith-pi-extension
```


## [​](https://docs.langchain.com/langsmith/trace-with-pi#quick-start) Quick start


Tracing is disabled by default. Set the following environment variables to enable tracing and connect to your LangSmith account:


```
export TRACE_TO_LANGSMITH=true
export LANGSMITH_PI_API_KEY="<your-langsmith-api-key>"
```


[Run Pi](https://pi.dev/docs/latest/quickstart) as usual. When a session starts, the extension reports whether LangSmith tracing is enabled. You can also check the current tracing state at any time from within Pi:


```
/langsmith-tracing
```


By default, traces are written to the `pi-coding-agent` LangSmith project.


## [​](https://docs.langchain.com/langsmith/trace-with-pi#configuration) Configuration


Configuration can come from environment variables or JSON config files. Values are merged in the following order, with later sources taking precedence:


1. Defaults
2. `~/.pi/langsmith.json` (global config)
3. `<current-working-directory>/.pi/langsmith.json` (project config)
4. Environment variables


### [​](https://docs.langchain.com/langsmith/trace-with-pi#environment-variables) Environment variables


| Variable | Description |
| --- | --- |
| `TRACE_TO_LANGSMITH` | Enables tracing when set to `true`, `1`, `yes`, or `on`. Disables tracing when set to `false`, `0`, `no`, or `off`. |
| `LANGSMITH_PI_API_KEY` | LangSmith API key. Falls back to `LANGSMITH_API_KEY`. |
| `LANGSMITH_PI_ENDPOINT` | LangSmith API URL for self-hosted or custom deployments. Falls back to `LANGSMITH_ENDPOINT`. |
| `LANGSMITH_PI_PROJECT` | LangSmith project name. Falls back to `LANGSMITH_PROJECT`. Defaults to `pi-coding-agent`. |
| `LANGSMITH_PI_METADATA` | JSON object added to the root run metadata. Falls back to `LANGSMITH_METADATA`. |
| `LANGSMITH_PI_RUNS_ENDPOINTS` | JSON array of replica run destinations. Falls back to `LANGSMITH_RUNS_ENDPOINTS`. |


Example:


```
export TRACE_TO_LANGSMITH=true
export LANGSMITH_PI_API_KEY="<your-langsmith-api-key>"
export LANGSMITH_PI_PROJECT="pi-coding-agent-dev"
export LANGSMITH_PI_METADATA='{"team":"infra","environment":"local"}'
```


### [​](https://docs.langchain.com/langsmith/trace-with-pi#config-file) Config file


Create `~/.pi/langsmith.json` for global settings or `.pi/langsmith.json` in a project directory for local overrides:


```
{
  "enabled": true,
  "api_key": "<your-langsmith-api-key>",
  "api_url": "https://api.smith.langchain.com",
  "project": "pi-coding-agent",
  "metadata": { "environment": "local" }
}
```


Config file fields:


| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `enabled` | Yes | `false` | Set to `true` to enable tracing from the config file. |
| `api_key` | No* | — | LangSmith API key. Required unless provided by environment variable or replicas. |
| `api_url` | No | LangSmith SDK default | LangSmith API URL, usually `https://api.smith.langchain.com`. |
| `project` | No | `pi-coding-agent` | LangSmith project name. |
| `metadata` | No | — | Object merged into root trace metadata. |
| `replicas` | No | — | Array of additional LangSmith destinations to replicate traces to. |


## [​](https://docs.langchain.com/langsmith/trace-with-pi#replicas) Replicas


Use `replicas` to send traces to multiple LangSmith destinations simultaneously. This is useful for forwarding traces to both a personal workspace and a shared team project, or to a [self-hosted LangSmith](https://docs.langchain.com/langsmith/self-hosted) instance alongside the [cloud](https://docs.langchain.com/langsmith/cloud).


```
{
  "enabled": true,
  "api_key": "<primary-api-key>",
  "project": "pi-coding-agent",
  "replicas": [
    {
      "api_key": "<replica-api-key>",
      "api_url": "https://replica-langsmith.example.com",
      "project": "pi-coding-agent-replica",
      "updates": {
        "tags": ["replica"]
      }
    }
  ]
}
```


Each replica entry can include an `updates` object to override metadata or tags on the replicated runs.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-pi.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace n8n workflows - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-n8n`

# Trace n8n workflows
## Documentation Index
## ​Prerequisites
## ​Set up tracing
## ​View traces in LangSmith
## ​Additional resources






Learn how to trace n8n AI workflows in LangSmith.

[n8n](https://n8n.io/) is a workflow automation platform that includes advanced AI capabilities built on LangChain. You can connect your n8n instance to LangSmith to record and monitor AI workflow runs.
LangSmith tracing is available for **self-hosted n8n instances** only.


## [​](https://docs.langchain.com/langsmith/trace-with-n8n#prerequisites) Prerequisites


- A [LangSmith account](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-n8n) and [API key](https://docs.langchain.com/langsmith/create-account-api-key)
- A self-hosted n8n instance


## [​](https://docs.langchain.com/langsmith/trace-with-n8n#set-up-tracing) Set up tracing


1. Set the following environment variables in the environment where you host your n8n instance, in the same way as the rest of your [n8n configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/). Required environment variables: Optional environment variables:
  - `LANGCHAIN_TRACING_V2`: Set to `true` to enable tracing.
  - `LANGCHAIN_API_KEY`: Your LangSmith API key.  - `LANGCHAIN_ENDPOINT`: LangSmith API endpoint. Defaults to `https://api.smith.langchain.com`. Set this if using self-hosted LangSmith, GCP EU (`https://eu.api.smith.langchain.com`), GCP APAC (`https://apac.api.smith.langchain.com`), or AWS US (`https://aws.api.smith.langchain.com`).
  - `LANGCHAIN_PROJECT`: Project name for traces. Defaults to `"default"`.
  - `LANGCHAIN_CALLBACKS_BACKGROUND`: Set to `true` for asynchronous trace upload (default), or `false` for synchronous uploads. (default: `true`)2. Restart your n8n instance for the environment variables to take effect.


## [​](https://docs.langchain.com/langsmith/trace-with-n8n#view-traces-in-langsmith) View traces in LangSmith


After running an AI workflow:


1. Open [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-n8n).
2. Select your project. If you just created your account, the `"default"` project appears after the first trace is sent.
3. Locate the trace corresponding to your workflow execution.


## [​](https://docs.langchain.com/langsmith/trace-with-n8n#additional-resources) Additional resources


- [n8n LangSmith integration guide](https://docs.n8n.io/advanced-ai/langchain/langsmith/)
- [n8n Advanced AI documentation](https://docs.n8n.io/advanced-ai/)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-n8n.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Instructor applications - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-instructor`

# Trace Instructor applications

LangSmith provides a convenient integration with [Instructor](https://python.useinstructor.com/), a popular open-source library for generating structured output with LLMs.
In order to use, you first need to set your LangSmith API key.


```
export LANGSMITH_API_KEY=<your-api-key>
# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```


Next, you will need to install the LangSmith SDK:
pip uv

```
pip install -U langsmith
```


```
uv add langsmith
```


Wrap your OpenAI client with `langsmith.wrappers.wrap_openai`


```
from openai import OpenAI
from langsmith import wrappers

client = wrappers.wrap_openai(OpenAI())
```


After this, you can patch the wrapped OpenAI client using `instructor`:


```
import instructor

client = instructor.patch(client)
```


Now, you can use `instructor` as you normally would, but now everything is logged to LangSmith!


```
from pydantic import BaseModel


class UserDetail(BaseModel):
    name: str
    age: int


user = client.chat.completions.create(
    model="gpt-6-luna",
    response_model=UserDetail,
    messages=[
        {"role": "user", "content": "Extract Jason is 25 years old"},
    ]
)
```


Oftentimes, you use `instructor` inside of other functions.
You can get nested traces by using this wrapped client and decorating those functions with `@traceable`.
Please see [Custom instrumentation](https://docs.langchain.com/langsmith/annotate-code) for more information on how to annotate your code for tracing with the `@traceable` decorator.


```
# You can customize the run name with the `name` keyword argument
@traceable(name="Extract User Details")
def my_function(text: str) -> UserDetail:
    return client.chat.completions.create(
        model="gpt-6-luna",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": f"Extract {text}"},
        ]
    )

my_function("Jason is 25 years old")
```


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-instructor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index


Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace Visual Studio Code Copilot Chat sessions - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-vscode-copilot`

# Trace Visual Studio Code Copilot Chat sessions
## Documentation Index
## ​Prerequisites
## ​Configure tracing
## ​View traces in LangSmith
## ​Troubleshooting
## ​Related resources







Capture VS Code Copilot Chat agent interactions, LLM calls, tool executions, and token usage in LangSmith via OpenTelemetry.

[Visual Studio Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview) can export traces over [OpenTelemetry](https://opentelemetry.io/) (OTel). LangSmith ingests OTLP directly, so you can point Copilot Chat at LangSmith and inspect agent turns, model metadata, tool calls, and token usage alongside the rest of your LLM traces.
This guide is based on Copilot’s [Monitor agent usage with OpenTelemetry](https://code.visualstudio.com/docs/copilot/guides/monitoring-agents) reference.


## [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#prerequisites) Prerequisites


Before setting up tracing, ensure you have:


- A recent version of [Visual Studio Code](https://code.visualstudio.com/) with GitHub Copilot Chat installed and signed in.
- A [LangSmith API key](https://docs.langchain.com/langsmith/create-account-api-key).


## [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#configure-tracing) Configure tracing


Copilot Chat enables OTel emission when any of `COPILOT_OTEL_ENABLED`, `OTEL_EXPORTER_OTLP_ENDPOINT`, or the `github.copilot.chat.otel.enabled` setting is set. The simplest way to send Copilot Chat traces to LangSmith is to export the following environment variables before launching VS Code:


```
export COPILOT_OTEL_ENABLED=true
export COPILOT_OTEL_PROTOCOL=http
export COPILOT_OTEL_ENDPOINT=https://api.smith.langchain.com/otel
export COPILOT_OTEL_CAPTURE_CONTENT=true
export OTEL_EXPORTER_OTLP_HEADERS="x-api-key=<your_langsmith_api_key>,Langsmith-Project=<your_project_name>"
```


| Variable | Description |
| --- | --- |
| `COPILOT_OTEL_ENABLED` | Set to `true` to enable Copilot Chat OTel export. |
| `COPILOT_OTEL_PROTOCOL` | OTLP protocol. Use `http` to target LangSmith’s HTTP OTLP ingestion endpoint. |
| `COPILOT_OTEL_ENDPOINT` | LangSmith OTLP endpoint. Takes precedence over `OTEL_EXPORTER_OTLP_ENDPOINT`. |
| `COPILOT_OTEL_CAPTURE_CONTENT` | Capture full prompts, responses, tool arguments, and tool results on spans. Off by default. |
| `OTEL_EXPORTER_OTLP_HEADERS` | Authentication headers for the OTLP exporter. Use `x-api-key=<your_langsmith_api_key>` and optionally `Langsmith-Project=<project>` to route traces to a specific [LangSmith project](https://docs.langchain.com/langsmith/log-traces-to-project). |


VS Code must inherit these environment variables, so export them in the shell session that launches VS Code (for example, by adding them to `~/.zshrc`, `~/.bashrc`, or a shell profile) before starting the editor.
Update the LangSmith endpoint for self-hosted installations or regional SaaS: GCP EU uses `eu.api.smith.langchain.com`; GCP APAC uses `apac.api.smith.langchain.com`; AWS US uses `aws.api.smith.langchain.com`. For self-hosted LangSmith, append `/api/v1/otel` to your LangSmith API URL—for example, `https://ai-company.com/api/v1/otel`.
`COPILOT_OTEL_CAPTURE_CONTENT=true` records full prompt and response content, system prompts, tool schemas, tool arguments, and tool results. Only enable it in trusted environments where capturing source code, file contents, and user prompts is acceptable.


### [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#alternative-vs-code-settings) Alternative: VS Code settings


If you prefer not to set environment variables, you can enable OTel from VS Code settings instead. Open **Settings** (`⌘,` / `Ctrl+,`), search for `copilot otel`, and configure:


```
{
  "github.copilot.chat.otel.enabled": true,
  "github.copilot.chat.otel.exporterType": "otlp-http",
  "github.copilot.chat.otel.otlpEndpoint": "https://api.smith.langchain.com/otel",
  "github.copilot.chat.otel.captureContent": true
}
```


Authentication headers must still be provided through the `OTEL_EXPORTER_OTLP_HEADERS` environment variable—VS Code settings do not expose a header field. Environment variables also take precedence over VS Code settings when both are set.


## [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#view-traces-in-langsmith) View traces in LangSmith


Start a Copilot Chat session and send a request. Open your [LangSmith project](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-vscode-copilot) to view the resulting traces. Each agent interaction produces a hierarchical span tree following the [OTel GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/):


- `invoke_agent` spans wrap the full agent orchestration, including agent name, conversation ID, turn count, and total token usage.
- `chat` spans capture individual LLM API calls with model, token counts, response time, and finish reason.
- `execute_tool` spans capture tool invocations with tool name, type, duration, and success status.


When an agent invokes a subagent, Copilot Chat propagates trace context automatically, so the subagent’s `invoke_agent` span appears as a child of the parent’s `execute_tool` span in LangSmith.


## [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#troubleshooting) Troubleshooting


- **No traces appear in LangSmith.** Confirm `COPILOT_OTEL_ENABLED=true` and that VS Code was launched from the shell where the variables are exported. Verify `OTEL_EXPORTER_OTLP_HEADERS` includes `x-api-key=<your_langsmith_api_key>` and that the API key belongs to the workspace you want to trace into. Restart VS Code after changing environment variables.
- **Traces land in the wrong project.** Set `Langsmith-Project=<your_project_name>` in `OTEL_EXPORTER_OTLP_HEADERS`. If unset, traces go to the workspace’s `default` project.
- **Prompts and responses are missing.** Content capture is opt-in. Set `COPILOT_OTEL_CAPTURE_CONTENT=true` (or enable the `github.copilot.chat.otel.captureContent` setting).


## [​](https://docs.langchain.com/langsmith/trace-with-vscode-copilot#related-resources) Related resources


- [VS Code Copilot: Monitor agent usage with OpenTelemetry](https://code.visualstudio.com/docs/copilot/guides/monitoring-agents)
- [Trace with OpenTelemetry](https://docs.langchain.com/langsmith/trace-with-opentelemetry)
- [Log traces to a project](https://docs.langchain.com/langsmith/log-traces-to-project)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-vscode-copilot.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Trace with Temporal - Docs by LangChain

`https://docs.langchain.com/langsmith/trace-with-temporal`

# Trace with Temporal
## Documentation Index
## ​Prerequisites
## ​Environment variables
## ​Set up tracing
## ​View traces in LangSmith
## ​Configuration options
## ​Troubleshooting
## ​Next steps
## ​Additional resources










Learn how to trace Temporal workflows and activities in LangSmith using OpenTelemetry.

[Temporal](https://temporal.io/) is a durable execution platform that enables developers to build resilient distributed applications. This guide shows you how to trace Temporal workflows and activities in LangSmith using OpenTelemetry.
LangSmith supports OpenTelemetry (OTEL) trace ingestion, which integrates seamlessly with Temporal’s native OpenTelemetry interceptors. This enables full distributed tracing across your workflow executions, activities, and any LLM calls within them.


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#prerequisites) Prerequisites


- A [LangSmith account](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-trace-with-temporal) and API key
- Temporal server running (local or cloud)
- OpenTelemetry SDK for your language


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#environment-variables) Environment variables


Set the following environment variables for all implementations:


| Variable | Required | Description |
| --- | --- | --- |
| `LANGSMITH_API_KEY` | Yes | Your LangSmith API key from Settings. |
| `LANGSMITH_PROJECT` | No | Project name (defaults to `"default"`). |


For regional SaaS or self-hosted LangSmith installations, also set `LANGCHAIN_BASE_URL` to your LangSmith instance URL.


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#set-up-tracing) Set up tracing


- Go
- Python
- TypeScript / JavaScript

Go uses the `langsmith-go` SDK with Temporal’s OpenTelemetry interceptors to automatically trace workflows and activities. 1

Install

Install the LangSmith Go SDK, Temporal SDK, and OpenTelemetry interceptor:

```
go get github.com/langchain-ai/langsmith-go@v0.1.0-alpha.7
go get go.temporal.io/sdk
go get go.temporal.io/sdk/contrib/opentelemetry
```

2

Initialize tracer

Initialize the LangSmith tracer, create Temporal’s OpenTelemetry interceptor, and register it with the Temporal client and worker:

```
package main

import (
	"context"
	"log"

	"github.com/langchain-ai/langsmith-go"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/opentelemetry"
	"go.temporal.io/sdk/interceptor"
	"go.temporal.io/sdk/worker"
)

func main() {
	ctx := context.Background()

	// Initialize LangSmith tracer (reads LANGSMITH_API_KEY and LANGSMITH_PROJECT)
	ls, err := langsmith.NewTracer(
		langsmith.WithServiceName("temporal-worker"),
	)
	if err != nil {
		log.Fatal("Failed to initialize LangSmith tracer:", err)
	}
	defer ls.Shutdown(ctx)

	// Create Temporal tracing interceptor
	tracer := ls.Tracer("temporal-app")
	tracingInterceptor, err := opentelemetry.NewTracingInterceptor(
		opentelemetry.TracerOptions{Tracer: tracer},
	)
	if err != nil {
		log.Fatal("Failed to create tracing interceptor:", err)
	}

	// Create Temporal client with tracing
	c, err := client.Dial(client.Options{
		Interceptors: []interceptor.ClientInterceptor{tracingInterceptor},
	})
	if err != nil {
		log.Fatal("Failed to create Temporal client:", err)
	}
	defer c.Close()

	// Create worker with tracing (uses same client)
	w := worker.New(c, "my-task-queue", worker.Options{})
	w.RegisterWorkflow(MyWorkflow)
	w.RegisterActivity(MyActivity)

	// Start worker
	if err := w.Run(worker.InterruptCh()); err != nil {
		log.Fatal("Worker failed:", err)
	}
}
```

3

Define workflow and activity

Define a workflow that executes an activity. The activity demonstrates how to add custom span attributes for LangSmith visibility:

```
package main

import (
	"context"
	"fmt"
	"time"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/trace"
	"go.temporal.io/sdk/activity"
	"go.temporal.io/sdk/workflow"
)

// MyWorkflow executes an activity
func MyWorkflow(ctx workflow.Context, input string) (string, error) {
	ao := workflow.ActivityOptions{
		StartToCloseTimeout: 10 * time.Second,
	}
	ctx = workflow.WithActivityOptions(ctx, ao)

	var result string
	err := workflow.ExecuteActivity(ctx, MyActivity, input).Get(ctx, &result)
	return result, err
}

// MyActivity processes input with custom span attributes
func MyActivity(ctx context.Context, input string) (string, error) {
	logger := activity.GetLogger(ctx)
	logger.Info("Processing", "input", input)

	// Get the span created by Temporal's interceptor
	span := trace.SpanFromContext(ctx)

	// Add Gen AI attributes for LangSmith visibility
	span.SetAttributes(
		attribute.String("gen_ai.prompt", input),
		attribute.String("gen_ai.operation.name", "chat"),
	)

	result := fmt.Sprintf("Processed: %s", input)

	// Set completion attribute
	span.SetAttributes(
		attribute.String("gen_ai.completion", result),
	)

	return result, nil
}
```

4

Execute workflow

In a separate client application, initialize the tracer and execute the workflow: client.go

```
// In a separate function or client application
func executeWorkflow() {
	ctx := context.Background()

	// Initialize tracer for client
	ls, err := langsmith.NewTracer(
		langsmith.WithServiceName("temporal-client"),
	)
	if err != nil {
		log.Fatal(err)
	}
	defer ls.Shutdown(ctx)

	// Create client with tracing
	tracer := ls.Tracer("temporal-app")
	tracingInterceptor, err := opentelemetry.NewTracingInterceptor(
		opentelemetry.TracerOptions{Tracer: tracer},
	)
	if err != nil {
		log.Fatal(err)
	}

	c, err := client.Dial(client.Options{
		Interceptors: []interceptor.ClientInterceptor{tracingInterceptor},
	})
	if err != nil {
		log.Fatal(err)
	}
	defer c.Close()

	// Execute workflow
	workflowOptions := client.StartWorkflowOptions{
		ID:        "my-workflow-1",
		TaskQueue: "my-task-queue",
	}

	we, err := c.ExecuteWorkflow(ctx, workflowOptions, MyWorkflow, "Hello World")
	if err != nil {
		log.Fatal(err)
	}

	var result string
	if err := we.Get(ctx, &result); err != nil {
		log.Fatal(err)
	}

	log.Printf("Workflow result: %s", result)
}
```

Python uses the `temporalio` SDK with OpenTelemetry interceptors, exporting traces to LangSmith via OTLP. 1

Install

Install the Temporal SDK, LangSmith SDK, and OpenTelemetry packages:

```
pip install temporalio
pip install langsmith
pip install opentelemetry-sdk
pip install opentelemetry-exporter-otlp-proto-http
```

2

Initialize tracer

Create an OpenTelemetry `TracerProvider` with an OTLP exporter configured to send traces to LangSmith:

```
import asyncio
import os
from datetime import timedelta

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.contrib.opentelemetry import TracingInterceptor
from temporalio.worker import Worker


def init_tracer_provider() -> TracerProvider:
    """Initialize OpenTelemetry with LangSmith exporter."""

    # Create OTLP exporter for LangSmith
    exporter = OTLPSpanExporter(
        endpoint="https://api.smith.langchain.com/otel/v1/traces",
        headers={
            "x-api-key": os.environ.get("LANGSMITH_API_KEY", ""),
            "Langsmith-Project": os.environ.get("LANGSMITH_PROJECT", "default"),
        },
    )

    # Create TracerProvider with resource attributes
    resource = Resource.create({
        SERVICE_NAME: "temporal-worker",
    })

    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))

    # Set as global provider
    trace.set_tracer_provider(provider)

    return provider
```

3

Define workflow and activity

Define a workflow class and activity function. The activity demonstrates how to add custom span attributes for LangSmith visibility:

```
@activity.defn
async def process_activity(input: str) -> str:
    """Activity that processes input with custom span attributes."""
    activity.logger.info(f"Processing: {input}")

    # Get current span and add Gen AI attributes
    span = trace.get_current_span()
    span.set_attribute("gen_ai.prompt", input)
    span.set_attribute("gen_ai.operation.name", "chat")

    result = f"Processed: {input}"

    span.set_attribute("gen_ai.completion", result)

    return result


@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self, input: str) -> str:
        return await workflow.execute_activity(
            process_activity,
            input,
            start_to_close_timeout=timedelta(seconds=10),
        )
```

4

Run worker

Create a Temporal client with the `TracingInterceptor` and start the worker:

```
async def main():
    # Initialize tracing
    provider = init_tracer_provider()

    try:
        # Create Temporal client with tracing interceptor
        client = await Client.connect(
            "localhost:7233",
            interceptors=[TracingInterceptor()],
        )

        # Run worker
        worker = Worker(
            client,
            task_queue="my-task-queue",
            workflows=[MyWorkflow],
            activities=[process_activity],
        )

        print("Starting worker...")
        await worker.run()

    finally:
        # Shutdown tracer provider to flush traces
        provider.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

5

Execute workflow

In a separate script, connect to Temporal with the tracing interceptor and execute the workflow: client.py

```
import asyncio
from temporalio.client import Client
from temporalio.contrib.opentelemetry import TracingInterceptor

# Import the same tracer setup
from worker import init_tracer_provider


async def main():
    provider = init_tracer_provider()

    try:
        client = await Client.connect(
            "localhost:7233",
            interceptors=[TracingInterceptor()],
        )

        # Execute workflow
        result = await client.execute_workflow(
            MyWorkflow.run,
            "Hello World",
            id="my-workflow-1",
            task_queue="my-task-queue",
        )
        print(f"Workflow result: {result}")

    finally:
        provider.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

TypeScript uses the `@temporalio/sdk` with OpenTelemetry interceptors to send traces to LangSmith. 1

Install

Install the Temporal SDK, OpenTelemetry interceptors, and tracing packages:

```
npm install @temporalio/client @temporalio/worker @temporalio/activity @temporalio/workflow
npm install @temporalio/interceptors-opentelemetry
npm install @opentelemetry/sdk-node @opentelemetry/sdk-trace-node
npm install @opentelemetry/exporter-trace-otlp-http
npm install @opentelemetry/resources @opentelemetry/semantic-conventions
```

2

Initialize tracer

Create a `NodeTracerProvider` with an OTLP exporter configured to send traces to LangSmith: tracer.ts

```
import { Resource } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions';
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

export function initTracerProvider(): NodeTracerProvider {
  // Create OTLP exporter for LangSmith
  const exporter = new OTLPTraceExporter({
    url: 'https://api.smith.langchain.com/otel/v1/traces',
    headers: {
      'x-api-key': process.env.LANGSMITH_API_KEY || '',
      'Langsmith-Project': process.env.LANGSMITH_PROJECT || 'default',
    },
  });

  // Create TracerProvider
  const provider = new NodeTracerProvider({
    resource: new Resource({
      [ATTR_SERVICE_NAME]: 'temporal-worker',
    }),
  });

  provider.addSpanProcessor(new BatchSpanProcessor(exporter));
  provider.register();

  return provider;
}
```

3

Define workflow

Define a workflow that proxies activities with a timeout configuration: workflows.ts

```
import { proxyActivities } from '@temporalio/workflow';
import type * as activities from './activities';

const { processActivity } = proxyActivities<typeof activities>({
  startToCloseTimeout: '10 seconds',
});

export async function myWorkflow(input: string): Promise<string> {
  return await processActivity(input);
}
```

4

Define activity

Define an activity that demonstrates how to add custom span attributes for LangSmith visibility: activities.ts

```
import { log } from '@temporalio/activity';
import { trace } from '@opentelemetry/api';

export async function processActivity(input: string): Promise<string> {
  log.info('Processing', { input });

  // Get current span and add Gen AI attributes
  const span = trace.getActiveSpan();
  span?.setAttribute('gen_ai.prompt', input);
  span?.setAttribute('gen_ai.operation.name', 'chat');

  const result = `Processed: ${input}`;

  span?.setAttribute('gen_ai.completion', result);

  return result;
}
```

5

Run worker

Create a worker with OpenTelemetry interceptors for activities and a workflow exporter for workflow spans: worker.ts

```
import { Worker, NativeConnection } from '@temporalio/worker';
import { Resource } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions';
import {
  makeWorkflowExporter,
  OpenTelemetryActivityInboundInterceptor,
} from '@temporalio/interceptors-opentelemetry';
import { trace } from '@opentelemetry/api';

import * as activities from './activities';
import { initTracerProvider } from './tracer';

async function run() {
  const provider = initTracerProvider();

  try {
    const connection = await NativeConnection.connect({
      address: 'localhost:7233',
    });

    const worker = await Worker.create({
      connection,
      namespace: 'default',
      taskQueue: 'my-task-queue',
      workflowsPath: require.resolve('./workflows'),
      activities,
      sinks: {
        exporter: makeWorkflowExporter(
          trace.getTracer('temporal-app'),
          new Resource({ [ATTR_SERVICE_NAME]: 'temporal-worker' })
        ),
      },
      interceptors: {
        activity: [() => ({ inbound: new OpenTelemetryActivityInboundInterceptor() })],
      },
    });

    console.log('Starting worker...');
    await worker.run();
  } finally {
    await provider.shutdown();
  }
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

6

Execute workflow

In a separate client file, connect to Temporal and execute the workflow: client.ts

```
import { Client, Connection } from '@temporalio/client';
import { initTracerProvider } from './tracer';

async function run() {
  // Initialize tracing
  const provider = initTracerProvider();

  try {
    const connection = await Connection.connect({ address: 'localhost:7233' });
    const client = new Client({ connection });

    const result = await client.workflow.execute('myWorkflow', {
      taskQueue: 'my-task-queue',
      workflowId: 'my-workflow-1',
      args: ['Hello World'],
    });

    console.log('Workflow result:', result);
  } finally {
    await provider.shutdown();
  }
}

run().catch(console.error);
```


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#view-traces-in-langsmith) View traces in LangSmith


Once configured, traces will appear in your LangSmith project:


1. Navigate to your LangSmith instance.
2. Select your project.
3. View traces in the **Tracing** tab.
4. Click on individual traces to see the full span hierarchy.


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#configuration-options) Configuration options


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#set-a-custom-service-name) Set a custom service name


Set a custom service name to distinguish different Temporal workers or services:
Go Python TypeScript

```
ls, err := langsmith.NewTracer(
    langsmith.WithServiceName("my-temporal-worker"),
)
```


```
resource = Resource.create({
    SERVICE_NAME: "my-temporal-worker",
})
```


```
const provider = new NodeTracerProvider({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: 'my-temporal-worker',
  }),
});
```


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#add-custom-span-attributes) Add custom span attributes


Add custom attributes to enrich your traces:
Go Python TypeScript

```
import "go.opentelemetry.io/otel/attribute"

span := trace.SpanFromContext(ctx)
span.SetAttributes(
    attribute.String("user.id", userID),
    attribute.String("workflow.version", "v2"),
)
```


```
from opentelemetry import trace

span = trace.get_current_span()
span.set_attribute("user.id", user_id)
span.set_attribute("workflow.version", "v2")
```


```
import { trace } from '@opentelemetry/api';

const span = trace.getActiveSpan();
span?.setAttribute('user.id', userId);
span?.setAttribute('workflow.version', 'v2');
```


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#configure-sampling) Configure sampling


For high-volume workflows, configure sampling to reduce trace volume:
Go Python TypeScript

```
// Note: langsmith.NewTracer() uses default sampling
// For custom sampling, use the TracerProvider directly
tp := sdktrace.NewTracerProvider(
    sdktrace.WithBatcher(exporter),
    sdktrace.WithSampler(sdktrace.TraceIDRatioBased(0.1)), // 10% sampling
)
```


```
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

provider = TracerProvider(
    resource=resource,
    sampler=TraceIdRatioBased(0.1),  # 10% sampling
)
```


```
import { TraceIdRatioBasedSampler } from '@opentelemetry/sdk-trace-base';

const provider = new NodeTracerProvider({
  resource: resource,
  sampler: new TraceIdRatioBasedSampler(0.1), // 10% sampling
});
```


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#troubleshooting) Troubleshooting


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#traces-not-appearing) Traces not appearing


1. **Verify API key**: Ensure `LANGSMITH_API_KEY` is set correctly
2. **Check endpoint**: Confirm you’re using `https://api.smith.langchain.com/otel/v1/traces`
3. **Flush on shutdown**: Call `provider.shutdown()` to flush pending spans before the application exits
4. **Check project**: Verify traces are sent to the correct project (default is `"default"`)


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#missing-activity-spans) Missing activity spans


Ensure the tracing interceptor is configured on both the client and worker:


- **Client**: Needs interceptor for starting workflows
- **Worker**: Needs interceptor for executing activities


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#context-propagation-issues) Context propagation issues


Verify propagators are configured correctly:


- **Go**: `langsmith.NewTracer()` automatically configures propagators
- **Python/TypeScript**: Ensure OpenTelemetry SDK is properly initialized with trace propagators


### [​](https://docs.langchain.com/langsmith/trace-with-temporal#worker-shutdown-hangs) Worker shutdown hangs


If traces aren’t flushing, ensure you’re calling the shutdown method with proper timeout:
Go Python TypeScript

```
defer ls.Shutdown(context.Background())
```


```
finally:
    provider.shutdown()
```


```
finally {
  await provider.shutdown();
}
```


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#next-steps) Next steps


- [Learn about LangSmith tracing concepts](https://docs.langchain.com/langsmith/observability-concepts)
- [Explore OpenTelemetry semantic conventions](https://docs.langchain.com/langsmith/trace-with-opentelemetry#supported-opentelemetry-attribute-and-event-mapping)


## [​](https://docs.langchain.com/langsmith/trace-with-temporal#additional-resources) Additional resources


- [Temporal Documentation](https://docs.temporal.io/)
- [Temporal Go SDK](https://github.com/temporalio/sdk-go)
- [Temporal Python SDK](https://github.com/temporalio/sdk-python)
- [Temporal TypeScript SDK](https://github.com/temporalio/sdk-typescript)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [LangSmith Go SDK](https://github.com/langchain-ai/langsmith-go)


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-temporal.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Coding agent metadata contract - Docs by LangChain

`https://docs.langchain.com/langsmith/coding-agent-metadata-contract`

# Coding agent metadata contract
## Documentation Index
## ​Supported integrations
## ​Global identity block
## ​Availability tiers
## ​Run types
## ​Required fields by run type
## ​Related








The metadata schema that standardizes what trace metadata coding agents must emit when sending runs to LangSmith.

This schema is the authoritative contract for metadata that coding agents attach to LangSmith runs. It defines which fields are required on every run, which fields are expected when the runtime can supply them, and which fields apply only to specific run types.
Coding agent integrations use this schema to ensure their traces are consistently structured, queryable, and compatible with LangSmith’s observability and filtering features.


## [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#supported-integrations) Supported integrations


The following integrations implement this schema:


| Integration | `ls_integration` value |
| --- | --- |
| [Claude Code](https://docs.langchain.com/langsmith/trace-claude-code) | `claude-code` |
| [OpenAI Codex](https://docs.langchain.com/langsmith/trace-with-codex) | `openai-codex` |
| [Deep Agents](https://docs.langchain.com/langsmith/trace-deep-agents) | `deepagents-code` |
| [Cursor](https://docs.langchain.com/langsmith/trace-with-cursor) | `cursor` |
| [Pi](https://docs.langchain.com/langsmith/trace-with-pi) | `pi` |
| [Opencode](https://docs.langchain.com/langsmith/trace-with-opencode) | `opencode` |
| [GitHub Copilot](https://docs.langchain.com/langsmith/trace-with-vscode-copilot) | `copilot` |


## [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#global-identity-block) Global identity block


Every run type must include the following identity fields in its metadata:


| Field | Description |
| --- | --- |
| `ls_agent_type` | The run’s type within the agent. Should be one of `"root"`, `"subagent"`, `"middleware"`, or `"compaction"`. |
| `ls_agent_purpose` | High-level purpose of the agent, for example `"coding"`. |
| `ls_integration` | Identifier of the integration emitting the run (see [Supported integrations](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#supported-integrations)). |
| `ls_agent_runtime` | Human-readable runtime name, for example `"Claude Code 1.0.28"`. |
| `thread_id` | Stable identifier for the conversation thread. Used to group related runs in LangSmith’s Threads view. |
| `ls_trace_schema_version` | Currently `"coding-agent-v1"`. |


## [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#availability-tiers) Availability tiers


Fields in this schema are marked with one of three availability tiers:


| Tier | Meaning |
| --- | --- |
| **always** | Must be present on every run. |
| **where_known** | Required whenever the runtime can expose the value. Omit only when the runtime genuinely cannot provide the information. |
| **contextual** | Optional metadata. Omit when not applicable. |


## [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#run-types) Run types


This schema distinguishes five run types. Some fields apply only to a subset of run types.


| Run type | Description |
| --- | --- |
| `root` | The top-level run representing a full agent turn or session. |
| `llm` | A language model call within a turn. |
| `tool` | A tool invocation within a turn. |
| `subagent` | A nested or delegated agent run. |
| `interrupted` | A run that was interrupted before completion. |


## [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#required-fields-by-run-type) Required fields by run type


### [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#all-run-types) All run types


The [global identity block](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#global-identity-block) fields are **always** required on every run type.
Additional fields required on all run types:


| Field | Tier | Description |
| --- | --- | --- |
| `ls_agent_version` | `where_known` | Version string for the agent runtime, for example `"1.0.28"`. |
| `git_branch` | `where_known` | Active Git branch in the repository being edited. |
| `git_commit_sha` | `where_known` | Full SHA of the current Git commit. |
| `git_repo_url` | `where_known` | Remote URL of the repository. |
| `working_directory` | `where_known` | Absolute path of the working directory. |


### [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#llm-runs) `llm` runs


| Field | Tier | Description |
| --- | --- | --- |
| `ls_model_name` | `where_known` | Model identifier, for example `"claude-opus-4-5"`. |
| `ls_provider` | `where_known` | Model provider, for example `"anthropic"`. |


### [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#tool-runs) `tool` runs


| Field | Tier | Description |
| --- | --- | --- |
| `ls_tool_name` | `always` | Name of the tool invoked, for example `"bash"` or `"computer"`. |


### [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#subagent-runs) `subagent` runs


| Field | Tier | Description |
| --- | --- | --- |
| `ls_subagent_id` | `always` | Stable identifier for the subagent. |
| `ls_subagent_type` | `always` | Type or role of the subagent, for example `"researcher"`. |


### [​](https://docs.langchain.com/langsmith/coding-agent-metadata-contract#interrupted-runs) `interrupted` runs


Interrupted runs carry the same fields as `root` runs. The run type itself signals the abnormal termination state; no additional required fields are added.


- [Metadata parameters reference](https://docs.langchain.com/langsmith/ls-metadata-parameters): `ls_` prefixed fields used in LangSmith runs generally.
- [Add metadata and tags](https://docs.langchain.com/langsmith/add-metadata-tags): how to attach metadata to traces using the LangSmith SDK.


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/coding-agent-metadata-contract.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)

---

# Home - Docs by LangChain

`https://docs.langchain.com/`

# The open agent engineering ecosystem

LangChain provides open source, model-agnostic harnesses for building agents. LangSmith is the framework-agnostic platform for testing, deploying, monitoring, and improving your agents across the agent development lifecycle. You control every layer of your agent system, and keep improving it with what you learn in production.

## Agent development lifecycle


## Build

Build agents with code using LangChain, LangGraph, and Deep Agents. Get started

## Test

Evaluate agents with datasets, evaluations, and prompt engineering. Get started

## Deploy

Deploy and serve agents at scale. Get started

## Monitor

Trace, debug, and observe agents in production. Get started

## Products


## LLM Gateway

Route, control, and observe LLM traffic across providers. Get started

## No-code agents

Build and run agents without code using LangSmith Fleet. Get started![](https://mintcdn.com/langchain-5e9cc07a/DcM1RJP509SEqR6s/images/brand/engine-icon-no-bg-dark.svg?fit=max&auto=format&n=DcM1RJP509SEqR6s&q=85&s=17cb861b0ae9666e1eb0876aa6aca68a)

## Engine

Find and fix recurring agent issues automatically with LangSmith Engine. Get started

## Deep Agents Code

Code with an AI agent in your terminal using the open source `dcode` CLI. Get started

## Setup and governance


## LangSmith setup

Hosting on Cloud, BYOC, or Self-hosted, account setup, and governance. Get started

## Govern

Manage users, access control, policies, and compliance across your organization. Get started

## Resources


## LangChain Academy

Take free courses on building and improving agents with LangSmith and our open-source frameworks. Enroll

## Community forum

Ask questions, share solutions, and discuss best practices. Join

## Support portal

Submit tickets and track support requests. Visit

## Sign up for LangSmith

Start with LangSmith for free. Sign up

## LangSmith status

Real-time status of LangSmith services and APIs. View

## Trust Center

HIPAA, SOC 2 Type 2, and GDPR compliance details. View

---

# LangSmith Chat - Docs by LangChain

`https://docs.langchain.com/langsmith/chat-observability`

**LangSmith Chat** (formerly Polly) is built directly into your LangSmith [workspace](https://docs.langchain.com/langsmith/administration-overview#workspaces) to help you analyze and understand your application data.
Chat helps you gain insight from your traces, conversation threads, and prompts without having to dig through data manually. By asking natural language questions, you can quickly understand agent performance, debug issues, and analyze user sentiment.
![LangSmith Chat icon](https://mintcdn.com/langchain-5e9cc07a/NVEcSyCXgAhfub1c/images/brand/polly-icon.png?fit=max&auto=format&n=NVEcSyCXgAhfub1c&q=85&s=d58c4caab502fcaa02864b5a8f833604) Chat appears in the right-hand bottom corner of the following locations within [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-chat):


**Observability & Debugging:**


- [Projects](https://docs.langchain.com/langsmith/chat#projects): Browse and filter runs across a project.
- [Trace pages](https://docs.langchain.com/langsmith/chat#trace-pages): Analyze individual runs and execution traces.
- [Thread views](https://docs.langchain.com/langsmith/chat#thread-views): Understand conversation threads and user interactions.
- [Engine](https://docs.langchain.com/langsmith/chat#engine): Investigate detected issues and their linked traces.


**Prompt Engineering:**


- [Playground](https://docs.langchain.com/langsmith/chat#playground): Edit and optimize prompts.
- [Prompt Hub pages](https://docs.langchain.com/langsmith/chat#prompt-hub-pages): Explore and understand shared prompts.


**Evaluation & Testing:**


- [Dataset Experiments](https://docs.langchain.com/langsmith/chat#dataset-experiments): Analyze experiment results and compare runs.
- [Dataset Examples](https://docs.langchain.com/langsmith/chat#dataset-examples): Browse and understand dataset structure.
- [Annotation Queues](https://docs.langchain.com/langsmith/chat#annotation-queues): Review runs and make informed annotation decisions.
- [Evaluators](https://docs.langchain.com/langsmith/chat#evaluators): Build and refine evaluators with AI assistance.


![Chat in the sidebar on a dataset view.](https://mintcdn.com/langchain-5e9cc07a/Cd9j6FYj16b1asiM/langsmith/images/polly-datasets-light.png?fit=max&auto=format&n=Cd9j6FYj16b1asiM&q=85&s=771a678928374d181e5d9d5e33d16cb0)
![Chat in the sidebar on a dataset view.](https://mintcdn.com/langchain-5e9cc07a/Cd9j6FYj16b1asiM/langsmith/images/polly-datasets-dark.png?fit=max&auto=format&n=Cd9j6FYj16b1asiM&q=85&s=e58462239dc037d880ec2c309e86f463)


## [​](https://docs.langchain.com/langsmith/chat#get-started) Get started


Before you start using Chat, you need to add an API key for the model you’re using:
In the [LangSmith UI](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=snippets-langsmith-set-workspace-secrets), ensure that your API key is set as a [workspace secret](https://docs.langchain.com/langsmith/set-up-hierarchy#configure-workspace-settings).


1. Navigate to **Settings** and then move to the **Secrets** tab.
2. Select **Add secret** and enter the key environment variable (e.g.,`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and your API key as the **Value**.
3. Select **Save secret**.


 When adding workspace secrets in the LangSmith UI, make sure the secret keys match the environment variable names expected by your model provider.
If your provider authenticates with OAuth2 `client_credentials`, configure the credentials on the model configuration instead. Workspace secrets are not required in that case. See [OAuth client credentials](https://docs.langchain.com/langsmith/model-configurations#oauth-client-credentials).
Chat calls model providers from LangSmith’s egress IP addresses. If your model provider (or a proxy in front of it) restricts traffic by IP, allowlist the LangSmith egress IPs listed in [Allowlist IP addresses](https://docs.langchain.com/langsmith/cloud-platform-features#allowlist-ip-addresses).


### [​](https://docs.langchain.com/langsmith/chat#supported-models) Supported models


Chat supports the following model providers out of the box:


- Anthropic (Claude)
- OpenAI
- Google Gemini
- AWS Bedrock
- Groq
- Mistral
- xAI
- DeepSeek
- Fireworks AI


You can also use any custom model you’ve configured in [Playground Settings](https://docs.langchain.com/langsmith/prompt-engineering-concepts#playground) by enabling the **Available in Chat** toggle on that configuration. Workspace admins manage which custom models are available.


### [​](https://docs.langchain.com/langsmith/chat#keyboard-shortcuts) Keyboard shortcuts


| Action | Mac | Windows/Linux |
| --- | --- | --- |
| Toggle Chat open/closed | `Cmd+I` | `Ctrl+I` |
| Clear current thread | `Cmd+Shift+O` | `Ctrl+Shift+O` |


## [​](https://docs.langchain.com/langsmith/chat#observability) Observability


### [​](https://docs.langchain.com/langsmith/chat#projects) Projects


On a project’s run list, Chat can browse and filter runs across the entire project, create datasets, and add examples. Use Chat to quickly explore what’s happening across your traces without manually paging through results.
**Example questions:**


- “Show me all the failed runs from the last 24 hours”
- “Which runs took the longest?”
- “Add the failing runs to my test dataset”
- “How many runs errored this week?”


### [​](https://docs.langchain.com/langsmith/chat#trace-pages) Trace pages


On an individual [trace](https://docs.langchain.com/langsmith/observability-concepts#traces), Chat analyzes the [run](https://docs.langchain.com/langsmith/observability-concepts#runs) data and execution trajectory. Chat examines the full trace context, including [run metadata](https://docs.langchain.com/langsmith/observability-concepts#metadata), inputs, outputs, intermediate steps, and configuration to help you understand what happened and identify areas for improvement.
**Example questions:**


- “Is there anything that the agent could have done better here?”
- “Why did this run fail?”
- “What took the most time in this trace?”
- “Summarize what happened in this trace”


### [​](https://docs.langchain.com/langsmith/chat#thread-views) Thread views


Under the **Threads** tab, Chat analyzes conversation [threads](https://docs.langchain.com/langsmith/observability-concepts#threads) to help you understand user sentiment, conversation outcomes, and interaction patterns. Use Chat to identify user pain points and understand whether issues were resolved.
**Example questions:**


- “Did the user seem frustrated?”
- “What issues is the user experiencing?”
- “Was the user’s problem solved?”
- “What was the main topic of this thread?”


### [​](https://docs.langchain.com/langsmith/chat#engine) Engine


On the [Engine](https://docs.langchain.com/langsmith/engine-issues) page, open Chat to investigate detected issues and their linked traces. Chat can help you understand the selected issue, or answer questions across multiple Engine issues. For example:
**Example questions:**


- “What went wrong?”
- “Why was this flagged?”
- “Explain the proposed fix”
- “What are my most pressing issues?”
- “How many new issues do I have?”


## [​](https://docs.langchain.com/langsmith/chat#prompt-engineering) Prompt engineering


### [​](https://docs.langchain.com/langsmith/chat#playground) Playground


In the [Playground](https://docs.langchain.com/langsmith/prompt-engineering-concepts#playground), Chat helps you edit and optimize your [prompts](https://docs.langchain.com/langsmith/prompt-engineering-concepts#prompts-in-langsmith). Use automated options like **Optimize prompt**, **Generate a tool**, or **Generate an output schema**, or give Chat custom instructions for editing your prompt. Chat can directly modify the playground state—updating messages, tools, output schemas, and examples—so you can iterate on prompts conversationally.
**Example questions:**


- “Make it respond in Italian”
- “Add more context about the user’s role”
- “Make the tone more professional”
- “Simplify the instructions”


### [​](https://docs.langchain.com/langsmith/chat#prompt-hub-pages) Prompt Hub pages


When viewing a prompt in the [LangSmith Hub](https://docs.langchain.com/langsmith/prompt-engineering-concepts#prompts-in-langsmith), Chat helps you understand the prompt’s structure, messages, tools, and configuration. This is useful for exploring and learning from shared prompts.
**Example questions:**


- “What does this prompt do?”
- “What tools does this prompt use?”
- “Explain the structure of this prompt”
- “What are the key instructions in this prompt?”


## [​](https://docs.langchain.com/langsmith/chat#evaluation) Evaluation


### [​](https://docs.langchain.com/langsmith/chat#dataset-experiments) Dataset Experiments


On the **Datasets** page under the **Experiments** tab, Chat analyzes experiment results and helps you compare runs across different experiments. Chat can identify patterns, summarize performance, and help you understand which approaches work best.
**Example questions:**


- “Which experiment performed best?”
- “What are the main differences between these runs?”
- “Summarize the results of this experiment”
- “What patterns do you see in the failures?”


### [​](https://docs.langchain.com/langsmith/chat#dataset-examples) Dataset Examples


On the **Datasets** page under the **Examples** tab, Chat helps you understand your dataset structure, browse examples, and identify data patterns. This is useful for understanding what data you’re working with and preparing datasets for experiments.
**Example questions:**


- “What type of data is in this dataset?”
- “Show me examples with errors”
- “What patterns do you see in the inputs?”
- “How many examples are in this dataset?”


### [​](https://docs.langchain.com/langsmith/chat#annotation-queues) Annotation Queues


In **Annotation Queues**, Chat helps you analyze runs before making annotation decisions. Whether you’re reviewing runs individually or comparing them pairwise, Chat provides insights into run behavior, errors, and execution patterns to inform your scoring.
**Example questions:**


- “What went wrong in this run?”
- “Summarize what happened in this run”
- “Compare these two runs”
- “What should I consider when scoring this?”


### [​](https://docs.langchain.com/langsmith/chat#evaluators) Evaluators


In the **Evaluators** builder, Chat helps you write and refine evaluator logic. Chat can generate evaluator code, suggest improvements, and help you test your evaluator against examples.
**Example questions:**


- “Write an evaluator that checks for hallucinations”
- “Improve the accuracy of this evaluator”
- “What does this evaluator check for?”
- “Add handling for edge cases”


## [​](https://docs.langchain.com/langsmith/chat#what%E2%80%99s-next) What’s next


Learn more about the features that Chat helps you explore:


## Observability

Learn more about tracing and monitoring your LLM applications

## Threads

Understand how threads work in LangSmith

## Prompt Engineering

Create and iterate on prompts in the Playground

## Evaluation

Evaluate and test your applications systematically


---


[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers. [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/chat.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
## Documentation Index
## ​Get started
## ​Observability
## ​Prompt engineering
## ​Evaluation
## ​What’s next







Was this page helpful?

Yes No[Docs by LangChain home page](https://docs.langchain.com/)