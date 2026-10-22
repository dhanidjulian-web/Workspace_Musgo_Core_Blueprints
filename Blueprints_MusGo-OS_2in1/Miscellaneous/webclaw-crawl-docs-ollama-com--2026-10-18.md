# Ollama documentation - Ollama

`https://docs.ollama.com/`

# Ollama documentation

Use open models in your desktop apps and coding agents, or build them into your application.


## Use your apps

Connect Claude or ChatGPT on your desktop, or launch a coding agent from your terminal.

## Build an application

Call cloud models with Ollama, OpenAI, or Anthropic APIs.


## [​](https://docs.ollama.com/#explore-models) Explore models


Choose cloud models or run models on your computer.


## Cloud models

Run models without a local GPU.

## Local models

Download Ollama and run a model on your computer.
Browse the [model library](https://ollama.com/search) for coding, vision, embeddings, and reasoning models.


## [​](https://docs.ollama.com/#documentation) Documentation


- [Integrations](https://docs.ollama.com/integrations) — connect an app, editor, or agent.
- [API reference](https://docs.ollama.com/api/introduction) — use Ollama’s API or compatible OpenAI and Anthropic clients.
- [Python library](https://github.com/ollama/ollama-python) and [JavaScript library](https://github.com/ollama/ollama-js) — use Ollama from your application.


## [​](https://docs.ollama.com/#community) Community


Join the conversation on [Discord](https://discord.gg/ollama) or [Reddit](https://reddit.com/r/ollama). ⌘ I

---

# Introduction - Ollama

`https://docs.ollama.com/api/introduction`

# Introduction

Use Ollama’s API to build applications with cloud or local models.


## [​](https://docs.ollama.com/api/introduction#get-started) Get started


Call cloud models with an [API key](https://ollama.com/settings/keys). No Ollama installation required. Start with the [API quickstart](https://docs.ollama.com/quickstart#build-an-application).
To run models on your computer, [install Ollama and run a local model](https://docs.ollama.com/quickstart#run-a-model-locally).


## [​](https://docs.ollama.com/api/introduction#base-urls) Base URLs


| API | Direct cloud access | Local Ollama server |
| --- | --- | --- |
| Ollama | `https://ollama.com/api` | `http://localhost:11434/api` |
| OpenAI compatibility | `https://ollama.com/v1` | `http://localhost:11434/v1` |
| Anthropic client base URL | `https://ollama.com` | `http://localhost:11434` |


The Anthropic client appends `/v1/messages` to its base URL.
Cloud requests need an API key. Local requests do not. To use cloud models through your local server, [sign in to Ollama](https://docs.ollama.com/api/authentication#signing-in).
Creating or deleting models requires a local Ollama server. For supported API features, see [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) and [Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility).


## [​](https://docs.ollama.com/api/introduction#ollama-api-example) Ollama API example


Set `OLLAMA_API_KEY` to your [API key](https://ollama.com/settings/keys), then call a cloud model:


```
curl https://ollama.com/api/chat \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [{"role": "user", "content": "Why is the sky blue?"}],
    "stream": false
  }'
```


Read the answer from `message.content`. For local inference, use `http://localhost:11434/api/chat` with a downloaded model and omit the authorization header.


## [​](https://docs.ollama.com/api/introduction#libraries) Libraries


Use Ollama’s official libraries with either a local server or the hosted API:


- [Python](https://github.com/ollama/ollama-python)
- [JavaScript](https://github.com/ollama/ollama-js)


For direct cloud access, set the host to `https://ollama.com` and supply your API key in the `Authorization: Bearer` header.
Browse [community libraries](https://github.com/ollama/ollama?tab=readme-ov-file#libraries--sdks).


## [​](https://docs.ollama.com/api/introduction#versioning) Versioning


Ollama’s API isn’t strictly versioned, but the API is expected to be stable and backwards compatible. Deprecations are rare and will be announced in the [release notes](https://github.com/ollama/ollama/releases). ⌘ I

---

# Quickstart - Ollama

`https://docs.ollama.com/quickstart`

# Quickstart

Use Ollama in [desktop apps](https://docs.ollama.com/quickstart#connect-a-desktop-app) and [coding agents](https://docs.ollama.com/quickstart#use-a-coding-agent), or [build an application](https://docs.ollama.com/quickstart#build-an-application) with an API key.


## [​](https://docs.ollama.com/quickstart#get-started) Get started


[Download Ollama](https://ollama.com/download) for macOS, Windows, or Linux. Open the app, or get started from your terminal:


```
ollama
```


Follow the setup prompts. Sign in to use cloud models, or choose a local model.


## [​](https://docs.ollama.com/quickstart#connect-a-desktop-app) Connect a desktop app


On macOS, open Ollama and select **Apps**. Connect **Claude** or **ChatGPT (Desktop)**. Follow the prompts to install or restart the app.
Choose your Ollama models in **Settings → Apps**.


- [Claude Desktop](https://docs.ollama.com/integrations/claude-desktop) — use Ollama models in Claude.
- [ChatGPT Desktop](https://docs.ollama.com/integrations/chatgpt) — use Ollama models in Codex mode. Regular Chat and voice use your usual ChatGPT connection.


## [​](https://docs.ollama.com/quickstart#use-a-coding-agent) Use a coding agent


From your project directory, launch your agent:


- Claude Code
- Codex CLI
- OpenCode


```
ollama launch claude
```

Ollama offers to install Claude Code if needed. See [Claude Code](https://docs.ollama.com/integrations/claude-code) for details. [Install Codex CLI](https://docs.ollama.com/integrations/codex#install) first, then launch it:

```
ollama launch codex
```

See [Codex CLI](https://docs.ollama.com/integrations/codex) for setup.

```
ollama launch opencode
```

Ollama offers to install OpenCode if needed. See [OpenCode](https://docs.ollama.com/integrations/opencode) for details.
Choose a model when prompted, then try:


```
Explain how this repository is organized.
```


For more tools, see [Integrations](https://docs.ollama.com/integrations). To connect an agent directly with an API key, see [Claude Code](https://docs.ollama.com/integrations/claude-code#connect-directly-to-ollama-cloud).


## [​](https://docs.ollama.com/quickstart#build-an-application) Build an application


Use cloud models with an API key, or run models locally without one. Cloud requests do not require an Ollama installation.


### [​](https://docs.ollama.com/quickstart#1-create-an-api-key) 1. Create an API key


For local models, skip this step and select **Local** under [Send a request](https://docs.ollama.com/quickstart#2-send-a-request).
For cloud models, sign in or create an account, then create an [API key](https://ollama.com/settings/keys).
Set your key in the terminal:
macOS / Linux Windows

```
export OLLAMA_API_KEY="your_api_key"
```


```
$env:OLLAMA_API_KEY = "your_api_key"
```


Keep your key on your application’s server, outside browser code and source control.


### [​](https://docs.ollama.com/quickstart#2-send-a-request) 2. Send a request


Make your first request to Ollama


- Cloud
- Local

These examples use the `gemma4:31b` [cloud model](https://ollama.com/search?c=cloud).

- Ollama API
- OpenAI Chat Completions
- OpenAI Responses
- Anthropic Messages


```
curl https://ollama.com/api/chat \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ],
    "stream": false
  }'
```

Read the answer from `message.content`. See [Ollama’s API and libraries](https://docs.ollama.com/api/introduction).

```
curl https://ollama.com/v1/chat/completions \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```

Read the answer from `choices[0].message.content`. See [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) for client setup and supported features.

```
curl https://ollama.com/v1/responses \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "input": "Say hello in one sentence."
  }'
```

Read the `output_text` content blocks inside `output`. The OpenAI Python client exposes the text as `response.output_text`. Responses requests are stateless: include conversation history in each request. `previous_response_id` and `conversation` aren’t supported. See [Responses compatibility](https://docs.ollama.com/api/openai-compatibility#responses-api).

```
curl https://ollama.com/v1/messages \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "gemma4:31b",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```

Read text blocks from `content`. Direct cloud requests use bearer authentication. See [Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility) for client setup and supported features. OpenAI and Anthropic compatibility each cover a subset of the original API. See [Cloud](https://docs.ollama.com/cloud) for models and usage limits. Run [Gemma 4 E2B](https://ollama.com/library/gemma4:e2b) on your computer. No API key required. The model download is about 7.2 GB. We recommend 8 GB of available VRAM, or unified memory on a Mac. Larger context windows need more memory. With less VRAM, Ollama can use system RAM, but responses may be slower. [Download Ollama](https://ollama.com/download) and open the app. On Linux, start the server with `ollama serve` if it is not already running. Download the model:

```
ollama pull gemma4:e2b
```

Send a request to your local server:

- Ollama API
- OpenAI Chat Completions
- OpenAI Responses
- Anthropic Messages


```
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e2b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ],
    "stream": false
  }'
```


```
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e2b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```

Read the answer from `choices[0].message.content`. See [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) for client setup and supported features.

```
curl http://localhost:11434/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e2b",
    "input": "Say hello in one sentence."
  }'
```

Read the `output_text` content blocks inside `output`. The OpenAI Python client exposes the text as `response.output_text`. Responses requests are stateless: include conversation history in each request. `previous_response_id` and `conversation` aren’t supported. See [Responses compatibility](https://docs.ollama.com/api/openai-compatibility#responses-api).

```
curl http://localhost:11434/v1/messages \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "gemma4:e2b",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```

Read text blocks from `content`. See [Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility) for client setup and supported features.


## [​](https://docs.ollama.com/quickstart#run-a-model-locally) Run a model locally


[Download Ollama](https://ollama.com/download), then run:


```
ollama run gemma4:e2b
```


Ollama downloads the model and starts a chat on your computer. Type `/bye` to leave.


## [​](https://docs.ollama.com/quickstart#next-steps) Next steps


Add [tool calling](https://docs.ollama.com/capabilities/tool-calling), [stream responses](https://docs.ollama.com/capabilities/streaming), or browse [more models](https://ollama.com/search). ⌘ I

---

# Overview - Ollama

`https://docs.ollama.com/integrations`

# Overview

Use Ollama models in your apps and tools.


## [​](https://docs.ollama.com/integrations#launch-a-coding-agent) Launch a coding agent


Run `ollama launch` in a terminal to choose a coding agent.
![](https://mintcdn.com/ollama-9269c548/VdS6E00liu8o_Gkj/images/launch-icons/claude-code.svg?fit=max&auto=format&n=VdS6E00liu8o_Gkj&q=85&s=edd8f01fa1844a0eca0a9e00be74a8a3)

## Claude Code

Read code, edit files, and run commands.![](https://mintcdn.com/ollama-9269c548/VdS6E00liu8o_Gkj/images/launch-icons/opencode.svg?fit=max&auto=format&n=VdS6E00liu8o_Gkj&q=85&s=ffa7d783e8ddf476a376ebbedaa064ae)

## OpenCode

Edit and run code from your terminal.![](https://mintcdn.com/ollama-9269c548/lUVF89V8OERH2XeN/images/launch-icons/deepseek-harness.svg?fit=max&auto=format&n=lUVF89V8OERH2XeN&q=85&s=7319c6893fc1ed94ba7882a2be3a3fcd)

## DeepSeek Harness

Use DeepSeek’s open-source coding agent in your browser.


## [​](https://docs.ollama.com/integrations#connect-a-desktop-app) Connect a desktop app


On macOS, open the [Ollama app](https://ollama.com/download) and select **Apps** in the sidebar. Connect Claude or ChatGPT.
![](https://mintcdn.com/ollama-9269c548/HSXjoAUgp7vt8Q9k/images/launch-icons/claude.svg?fit=max&auto=format&n=HSXjoAUgp7vt8Q9k&q=85&s=e1b9d4f4dadb9187a486a5bb4b93907f)

## Claude Desktop

Use local and cloud Ollama models.![](https://mintcdn.com/ollama-9269c548/HSXjoAUgp7vt8Q9k/images/launch-icons/chatgpt.svg?fit=max&auto=format&n=HSXjoAUgp7vt8Q9k&q=85&s=c1abef5f71760198760f4cb7669ef143)

## ChatGPT Desktop

Use Ollama models in Codex mode.


## [​](https://docs.ollama.com/integrations#run-a-personal-assistant) Run a personal assistant


Run `ollama launch` in a terminal and choose OpenClaw or Hermes Agent.
![](https://mintcdn.com/ollama-9269c548/VdS6E00liu8o_Gkj/images/launch-icons/openclaw.svg?fit=max&auto=format&n=VdS6E00liu8o_Gkj&q=85&s=41b25b9a809d087e9e55b1b7bdb76cae)

## OpenClaw

Chat with an assistant through your messaging apps.![](https://mintcdn.com/ollama-9269c548/VdS6E00liu8o_Gkj/images/launch-icons/hermes-agent.svg?fit=max&auto=format&n=VdS6E00liu8o_Gkj&q=85&s=23dcf989a34d894a97bdb847c3831057)

## Hermes Agent

Personal assistant with memory, reusable skills, and messaging.


## [​](https://docs.ollama.com/integrations#work-in-your-editor) Work in your editor


![](https://mintcdn.com/ollama-9269c548/VdS6E00liu8o_Gkj/images/launch-icons/vscode.svg?fit=max&auto=format&n=VdS6E00liu8o_Gkj&q=85&s=a2ba239e0b0f44900813a438537a1c98)

## VS Code

Install the Ollama extension to use models in VS Code Chat. ⌘ I

---

# ChatGPT Desktop - Ollama

`https://docs.ollama.com/integrations/chatgpt`

ChatGPT Desktop includes Codex, OpenAI’s desktop coding agent. Ollama adds compatible local and cloud models to Codex’s model picker alongside ChatGPT’s native models.


## [​](https://docs.ollama.com/integrations/chatgpt#prerequisites) Prerequisites


- Ollama v0.34.0 or newer


If ChatGPT is not installed, Ollama offers to download it during setup.


## [​](https://docs.ollama.com/integrations/chatgpt#connect-chatgpt) Connect ChatGPT


1. Open the Ollama desktop app and select **Apps**.
2. Toggle **ChatGPT (Desktop)** to On.
3. Follow the setup prompts. If ChatGPT is already open, Ollama asks to restart it before the new models appear.
4. Open the ChatGPT desktop app and use Codex mode.


## [​](https://docs.ollama.com/integrations/chatgpt#choose-models) Choose models


Open Ollama **Settings**, select **Apps**, then select ChatGPT. Choose up to five compatible local or cloud models and save your changes. Ollama asks to restart ChatGPT when a model change needs one.


## [​](https://docs.ollama.com/integrations/chatgpt#disconnect-chatgpt) Disconnect ChatGPT


Open Ollama **Apps** and turn ChatGPT off. Ollama restores ChatGPT’s connection settings and usual profile. If ChatGPT is open, Ollama asks to restart it so the change takes effect.


## [​](https://docs.ollama.com/integrations/chatgpt#codex-behavior-and-limits) Codex behavior and limits


- Only requests made with an Ollama model go to Ollama. ChatGPT’s native models keep using their usual provider.
- Ollama models are for Codex mode. Regular Chat and voice keep using their usual ChatGPT connection.
- Codex manages sessions. Ollama routes model requests and compaction when Codex asks for it, but does not store ChatGPT sessions.
- Web search uses Ollama’s web-search service when you use an Ollama model. It requires Ollama sign-in and is limited to three calls per response.


## [​](https://docs.ollama.com/integrations/chatgpt#related-integrations) Related integrations


- Use Codex from a terminal with [Codex CLI](https://docs.ollama.com/integrations/codex).
- Connect other desktop apps from [Claude Desktop](https://docs.ollama.com/integrations/claude-desktop).

⌘ I

---

# Streaming - Ollama

`https://docs.ollama.com/capabilities/streaming`

Streaming allows you to render text as it is produced by the model.
Streaming is enabled by default through the REST API, but disabled by default in the SDKs.
To enable streaming in the SDKs, set the `stream` parameter to `True`.


## [​](https://docs.ollama.com/capabilities/streaming#key-streaming-concepts) Key streaming concepts


1. Chatting: Stream partial assistant messages. Each chunk includes the `content` so you can render messages as they arrive.
2. Thinking: Thinking-capable models emit a `thinking` field alongside regular content in each chunk. Detect this field in streaming chunks to show or hide reasoning traces before the final answer arrives.
3. Tool calling: Watch for streamed `tool_calls` in each chunk, execute the requested tool, and append tool outputs back into the conversation.


## [​](https://docs.ollama.com/capabilities/streaming#handling-streamed-chunks) Handling streamed chunks


 It is necessary to accumulate the partial fields in order to maintain the history of the conversation. This is particularly important for tool calling where the thinking, tool call from the model, and the executed tool result must be passed back to the model in the next request.


- Python
- JavaScript


```
from ollama import chat

stream = chat(
  model='qwen3',
  messages=[{'role': 'user', 'content': 'What is 17 × 23?'}],
  stream=True,
)

in_thinking = False
content = ''
thinking = ''
for chunk in stream:
  if chunk.message.thinking:
    if not in_thinking:
      in_thinking = True
      print('Thinking:\n', end='', flush=True)
    print(chunk.message.thinking, end='', flush=True)
    # accumulate the partial thinking
    thinking += chunk.message.thinking
  elif chunk.message.content:
    if in_thinking:
      in_thinking = False
      print('\n\nAnswer:\n', end='', flush=True)
    print(chunk.message.content, end='', flush=True)
    # accumulate the partial content
    content += chunk.message.content

  # append the accumulated fields to the messages for the next request
  new_messages = [{ role: 'assistant', thinking: thinking, content: content }]
```


```
import ollama from 'ollama'

async function main() {
  const stream = await ollama.chat({
    model: 'qwen3',
    messages: [{ role: 'user', content: 'What is 17 × 23?' }],
    stream: true,
  })

  let inThinking = false
  let content = ''
  let thinking = ''

  for await (const chunk of stream) {
    if (chunk.message.thinking) {
      if (!inThinking) {
        inThinking = true
        process.stdout.write('Thinking:\n')
      }
      process.stdout.write(chunk.message.thinking)
      // accumulate the partial thinking
      thinking += chunk.message.thinking
    } else if (chunk.message.content) {
      if (inThinking) {
        inThinking = false
        process.stdout.write('\n\nAnswer:\n')
      }
      process.stdout.write(chunk.message.content)
      // accumulate the partial content
      content += chunk.message.content
    }
  }

  // append the accumulated fields to the messages for the next request
  new_messages = [{ role: 'assistant', thinking: thinking, content: content }]
}

main().catch(console.error)
```

⌘ I

---

# Authentication - Ollama

`https://docs.ollama.com/api/authentication`

# Authentication

The local API at `http://localhost:11434` does not require authentication.
To use cloud models, publish models, or download private models, sign in to Ollama. For direct API access to ollama.com, use an API key.


## [​](https://docs.ollama.com/api/authentication#api-keys) API keys


Direct cloud inference at `https://ollama.com/api` and `https://ollama.com/v1` requires an API key. No Ollama installation or local server is required.
Create an [API key](https://ollama.com/settings/keys), then set it in your terminal:


```
export OLLAMA_API_KEY="your_api_key"
```


Use the API key in the `Authorization: Bearer` header. This also applies to the hosted Anthropic-compatible `/v1/messages` endpoint; `x-api-key` alone is not supported.


```
curl https://ollama.com/api/chat \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [{"role": "user", "content": "Why is the sky blue?"}],
    "stream": false
  }'
```


API keys do not expire. Revoke a key in [API keys settings](https://ollama.com/settings/keys).
Keep keys outside browser code and source control. See the [API quickstart](https://docs.ollama.com/quickstart#build-an-application) for shell setup and compatibility examples.


## [​](https://docs.ollama.com/api/authentication#signing-in) Signing in


Sign in from your terminal:


```
ollama signin
```


Ollama then authenticates cloud requests for you:


```
ollama run gpt-oss:120b-cloud
```


This also works through the local API:


```
curl http://localhost:11434/api/generate -d '{
  "model": "gpt-oss:120b-cloud",
  "prompt": "Why is the sky blue?"
}'
```

⌘ I

---

# OpenAI compatibility - Ollama

`https://docs.ollama.com/api/openai-compatibility`

Connect OpenAI clients to Ollama. Ollama supports a subset of the [OpenAI API](https://platform.openai.com/docs/api-reference).


## [​](https://docs.ollama.com/api/openai-compatibility#direct-cloud-access) Direct cloud access


Set your [API key](https://ollama.com/settings/keys) in `OLLAMA_API_KEY`. Install the client with `pip install openai`. No Ollama installation required.


```
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://ollama.com/v1",
    api_key=os.environ["OLLAMA_API_KEY"],
)

response = client.chat.completions.create(
    model="gemma4:31b",
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print(response.choices[0].message.content)
```


The same client supports stateless Responses requests:


```
response = client.responses.create(
    model="gemma4:31b",
    input="Say hello in one sentence.",
)
print(response.output_text)
```


Choose a [cloud model](https://ollama.com/search?c=cloud). The cloud API does not support stateful Responses, built-in web search through `/v1/responses`, or custom/freeform tool-call replay.


## [​](https://docs.ollama.com/api/openai-compatibility#local-server-usage) Local server usage


These examples connect to your local Ollama server. The client requires an API key value, but Ollama ignores it. To use cloud models through this server, [sign in to Ollama](https://docs.ollama.com/api/authentication#signing-in).


### [​](https://docs.ollama.com/api/openai-compatibility#simple-/v1/chat/completions-example) Simple `/v1/chat/completions` example


basic.py

Python


```
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model='gpt-oss:20b',
)
print(chat_completion.choices[0].message.content)
```


```
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "http://localhost:11434/v1/",
  apiKey: "ollama", // required but ignored
});

const chatCompletion = await openai.chat.completions.create({
  messages: [{ role: "user", content: "Say this is a test" }],
  model: "gpt-oss:20b",
});

console.log(chatCompletion.choices[0].message.content);
```


```
curl -X POST http://localhost:11434/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "gpt-oss:20b",
  "messages": [{ "role": "user", "content": "Say this is a test" }]
}'
```


### [​](https://docs.ollama.com/api/openai-compatibility#simple-/v1/responses-example) Simple `/v1/responses` example


responses.py

Python


```
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

responses_result = client.responses.create(
  model='qwen3:8b',
  input='Write a short poem about the color blue',
)
print(responses_result.output_text)
```


```
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "http://localhost:11434/v1/",
  apiKey: "ollama", // required but ignored
});

const responsesResult = await openai.responses.create({
  model: "qwen3:8b",
  input: "Write a short poem about the color blue",
});

console.log(responsesResult.output_text);
```


```
curl -X POST http://localhost:11434/v1/responses \
-H "Content-Type: application/json" \
-d '{
  "model": "qwen3:8b",
  "input": "Write a short poem about the color blue"
}'
```


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/chat/completions-with-vision-example) `/v1/chat/completions` with vision example


vision.py

Python


```
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

response = client.chat.completions.create(
    model='qwen3-vl:8b',
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': "What's in this image?"},
                {
                    'type': 'image_url',
                    'image_url': 'data:image/png;base64,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',
                },
            ],
        }
    ],
    max_tokens=300,
)
print(response.choices[0].message.content)
```


```
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "http://localhost:11434/v1/",
  apiKey: "ollama", // required but ignored
});

const response = await openai.chat.completions.create({
  model: "qwen3-vl:8b",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "What's in this image?" },
        {
          type: "image_url",
          image_url:
            "data:image/png;base64,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",
        },
      ],
    },
  ],
});
console.log(response.choices[0].message.content);
```


```
curl -X POST http://localhost:11434/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "qwen3-vl:8b",
  "messages": [{ "role": "user", "content": [{"type": "text", "text": "What is this an image of?"}, {"type": "image_url", "image_url": "data:image/png;base64,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"}]}]
}'
```


## [​](https://docs.ollama.com/api/openai-compatibility#endpoints) Endpoints


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/chat/completions) `/v1/chat/completions`


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-features) Supported features


- Chat completions
- Streaming
- JSON mode
- Reproducible outputs
- Vision
- Tools
- Reasoning/thinking control (for thinking models)
- Logprobs


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-request-fields) Supported request fields


- `model`
- `messages`
  - Text `content`
  - Image `content`
    - Base64 encoded image
    - Image URL  - Array of `content` parts- `frequency_penalty`
- `presence_penalty`
- `response_format`
- `seed`
- `stop`
- `stream`
- `stream_options`
  - `include_usage`- `temperature`
- `top_p`
- `max_tokens`
- `tools`
- `reasoning_effort` (model-defined names and compatibility aliases)
- `reasoning`
  - `effort` (model-defined names and compatibility aliases)- `tool_choice`
- `logit_bias`
- `user`
- `n`


`reasoning_effort` and `reasoning.effort` control model thinking. Use `/api/show` to discover each model’s supported values and default. When a model uses its metadata to resolve named levels, supported names are applied exactly and unsupported names resolve to the model default. Boolean-only models that support enabling thinking map recognized compatibility efforts to `true`, while `"none"` requests `false`. Models without metadata retain the existing compatibility aliases: `"minimal"` maps to `"low"`, and `"xhigh"` or `"ultra"` map to `"max"`. GPT-OSS keeps its existing OpenAI compatibility conversion: `"minimal"` uses `"low"`, `"xhigh"` or `"ultra"` use `"high"`, and `"none"` requests no thinking output.


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/completions) `/v1/completions`


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-features-2) Supported features


- Completions
- Streaming
- JSON mode
- Reproducible outputs
- Logprobs


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-request-fields-2) Supported request fields


- `model`
- `prompt`
- `frequency_penalty`
- `presence_penalty`
- `seed`
- `stop`
- `stream`
- `stream_options`
  - `include_usage`- `temperature`
- `top_p`
- `max_tokens`
- `suffix`
- `best_of`
- `echo`
- `logit_bias`
- `user`
- `n`


#### [​](https://docs.ollama.com/api/openai-compatibility#notes) Notes


- `prompt` currently only accepts a string


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/models) `/v1/models`


#### [​](https://docs.ollama.com/api/openai-compatibility#notes-2) Notes


- `created` corresponds to when the model was last modified
- `owned_by` corresponds to the ollama username, defaulting to `"library"`


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/models/model) `/v1/models/{model}`


#### [​](https://docs.ollama.com/api/openai-compatibility#notes-3) Notes


- `created` corresponds to when the model was last modified
- `owned_by` corresponds to the ollama username, defaulting to `"library"`


### [​](https://docs.ollama.com/api/openai-compatibility#/v1/embeddings) `/v1/embeddings`


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-request-fields-3) Supported request fields


- `model`
- `input`
  - string
  - array of strings
  - array of tokens
  - array of token arrays- `encoding format`
- `dimensions`
- `user`


### [​](https://docs.ollama.com/api/openai-compatibility#responses-api) Responses API


`POST /v1/responses`


> Note: Added in Ollama v0.13.3


Ollama supports the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses). Only the non-stateful flavor is supported (i.e., there is no `previous_response_id` or `conversation` support).


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-features-3) Supported features


- Streaming
- Tools (function calling)
- Reasoning summaries (for thinking models)
- Stateful requests


#### [​](https://docs.ollama.com/api/openai-compatibility#supported-request-fields-4) Supported request fields


- `model`
- `input`
- `instructions`
- `tools`
- `stream`
- `temperature`
- `top_p`
- `max_output_tokens`
- `reasoning`
  - `effort` (model-defined names and compatibility aliases)- `think` (Ollama extension; boolean, model-defined string, or `null`)
- `previous_response_id` (stateful v1/responses not supported)
- `conversation` (stateful v1/responses not supported)
- `truncation`


## [​](https://docs.ollama.com/api/openai-compatibility#models) Models


For local inference, download a model before using it:


```
ollama pull llama3.2
```


Direct cloud requests use the identifiers from `https://ollama.com/api/tags` and do not require a pull. Through a signed-in local server, select a cloud model such as `gemma4:cloud`.


### [​](https://docs.ollama.com/api/openai-compatibility#default-model-names-on-a-local-server) Default model names on a local server


For tooling that relies on default OpenAI model names such as `gpt-3.5-turbo`, use `ollama cp` to copy an existing model name to a temporary name:


```
ollama cp llama3.2 gpt-3.5-turbo
```


Afterwards, this new model name can be specified the `model` field:


```
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```


### [​](https://docs.ollama.com/api/openai-compatibility#setting-the-local-context-size) Setting the local context size


The OpenAI API does not have a way of setting the context size for a model. If you need to change the context size, create a `Modelfile` which looks like:


```
FROM <some model>
PARAMETER num_ctx <context size>
```


Use the `ollama create mymodel` command to create a new model with the updated context size. Call the API with the updated model name:


```
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "mymodel",
        "messages": [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```

⌘ I

---

# Anthropic compatibility - Ollama

`https://docs.ollama.com/api/anthropic-compatibility`

# Anthropic compatibility

Connect Anthropic clients and tools such as Claude Code to Ollama. Ollama supports a subset of the [Anthropic Messages API](https://platform.claude.com/docs/en/api/http/messages/create).


## [​](https://docs.ollama.com/api/anthropic-compatibility#direct-cloud-access) Direct cloud access


Set your [API key](https://ollama.com/settings/keys) in `OLLAMA_API_KEY`. No Ollama installation required.


```
export OLLAMA_API_KEY="your_api_key"
```


Send a request with bearer authentication:


```
curl https://ollama.com/v1/messages \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "gemma4:31b",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ]
  }'
```


Read text blocks from `content`. The cloud endpoint requires `Authorization: Bearer`; it does not accept `x-api-key` alone.
Compatible models support messages, streaming, and function calling. Tool-choice controls, deferred tools, and hosted web search are not fully supported.


## [​](https://docs.ollama.com/api/anthropic-compatibility#local-server-usage) Local server usage


These examples connect to your local Ollama server. Use `ollama` as the placeholder API key. To use cloud models through this server, [sign in to Ollama](https://docs.ollama.com/api/authentication#signing-in).


### [​](https://docs.ollama.com/api/anthropic-compatibility#environment-variables) Environment variables


To use Ollama with tools that expect the Anthropic API (like Claude Code), set these environment variables:


```
export ANTHROPIC_AUTH_TOKEN=ollama  # required but ignored
export ANTHROPIC_BASE_URL=http://localhost:11434
```


### [​](https://docs.ollama.com/api/anthropic-compatibility#simple-/v1/messages-example) Simple `/v1/messages` example


basic.py

Python


```
import anthropic

client = anthropic.Anthropic(
    base_url='http://localhost:11434',
    api_key='ollama',  # required but ignored
)

message = client.messages.create(
    model='qwen3-coder',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': 'Hello, how are you?'}
    ]
)
print(message.content[0].text)
```


```
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "http://localhost:11434",
  apiKey: "ollama", // required but ignored
});

const message = await anthropic.messages.create({
  model: "qwen3-coder",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, how are you?" }],
});

console.log(message.content[0].text);
```


```
curl -X POST http://localhost:11434/v1/messages \
-H "Content-Type: application/json" \
-H "x-api-key: ollama" \
-H "anthropic-version: 2023-06-01" \
-d '{
  "model": "qwen3-coder",
  "max_tokens": 1024,
  "messages": [{ "role": "user", "content": "Hello, how are you?" }]
}'
```


### [​](https://docs.ollama.com/api/anthropic-compatibility#streaming-example) Streaming example


streaming.py

Python


```
import anthropic

client = anthropic.Anthropic(
    base_url='http://localhost:11434',
    api_key='ollama',
)

with client.messages.stream(
    model='qwen3-coder',
    max_tokens=1024,
    messages=[{'role': 'user', 'content': 'Count from 1 to 10'}]
) as stream:
    for text in stream.text_stream:
        print(text, end='', flush=True)
```


```
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "http://localhost:11434",
  apiKey: "ollama",
});

const stream = await anthropic.messages.stream({
  model: "qwen3-coder",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Count from 1 to 10" }],
});

for await (const event of stream) {
  if (
    event.type === "content_block_delta" &&
    event.delta.type === "text_delta"
  ) {
    process.stdout.write(event.delta.text);
  }
}
```


```
curl -X POST http://localhost:11434/v1/messages \
-H "Content-Type: application/json" \
-d '{
  "model": "qwen3-coder",
  "max_tokens": 1024,
  "stream": true,
  "messages": [{ "role": "user", "content": "Count from 1 to 10" }]
}'
```


### [​](https://docs.ollama.com/api/anthropic-compatibility#tool-calling-example) Tool calling example


tools.py

Python


```
import anthropic

client = anthropic.Anthropic(
    base_url='http://localhost:11434',
    api_key='ollama',
)

message = client.messages.create(
    model='qwen3-coder',
    max_tokens=1024,
    tools=[
        {
            'name': 'get_weather',
            'description': 'Get the current weather in a location',
            'input_schema': {
                'type': 'object',
                'properties': {
                    'location': {
                        'type': 'string',
                        'description': 'The city and state, e.g. San Francisco, CA'
                    }
                },
                'required': ['location']
            }
        }
    ],
    messages=[{'role': 'user', 'content': "What's the weather in San Francisco?"}]
)

for block in message.content:
    if block.type == 'tool_use':
        print(f'Tool: {block.name}')
        print(f'Input: {block.input}')
```


```
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  baseURL: "http://localhost:11434",
  apiKey: "ollama",
});

const message = await anthropic.messages.create({
  model: "qwen3-coder",
  max_tokens: 1024,
  tools: [
    {
      name: "get_weather",
      description: "Get the current weather in a location",
      input_schema: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA",
          },
        },
        required: ["location"],
      },
    },
  ],
  messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
});

for (const block of message.content) {
  if (block.type === "tool_use") {
    console.log("Tool:", block.name);
    console.log("Input:", block.input);
  }
}
```


```
curl -X POST http://localhost:11434/v1/messages \
-H "Content-Type: application/json" \
-d '{
  "model": "qwen3-coder",
  "max_tokens": 1024,
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather in a location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state"
          }
        },
        "required": ["location"]
      }
    }
  ],
  "messages": [{ "role": "user", "content": "What is the weather in San Francisco?" }]
}'
```


## [​](https://docs.ollama.com/api/anthropic-compatibility#using-with-claude-code) Using with Claude Code


See the [Claude Code guide](https://docs.ollama.com/integrations/claude-code) for Ollama Launch and [direct cloud setup](https://docs.ollama.com/integrations/claude-code#connect-directly-to-ollama-cloud).


## [​](https://docs.ollama.com/api/anthropic-compatibility#endpoints) Endpoints


### [​](https://docs.ollama.com/api/anthropic-compatibility#/v1/messages) `/v1/messages`


#### [​](https://docs.ollama.com/api/anthropic-compatibility#supported-features) Supported features


- Messages
- Streaming
- System prompts
- Multi-turn conversations
- Vision (images)
- Tools (function calling)
- Tool results
- Thinking/extended thinking


#### [​](https://docs.ollama.com/api/anthropic-compatibility#supported-request-fields) Supported request fields


- `model`
- `max_tokens`
- `messages`
  - Text `content`
  - Image `content` (base64)
  - Array of content blocks
  - `tool_use` blocks
  - `tool_result` blocks
  - `thinking` blocks- `system` (string or array)
- `stream`
- `temperature`
- `top_p`
- `top_k`
- `stop_sequences`
- `tools`
- `thinking`
- `output_config`
  - `effort` (model-defined names)- `tool_choice`
- `metadata`


#### [​](https://docs.ollama.com/api/anthropic-compatibility#supported-response-fields) Supported response fields


- `id`
- `type`
- `role`
- `model`
- `content` (text, tool_use, thinking blocks)
- `stop_reason` (end_turn, max_tokens, tool_use)
- `usage` (input_tokens, output_tokens)


#### [​](https://docs.ollama.com/api/anthropic-compatibility#streaming-events) Streaming events


- `message_start`
- `content_block_start`
- `content_block_delta` (text_delta, input_json_delta, thinking_delta)
- `content_block_stop`
- `message_delta`
- `message_stop`
- `ping`
- `error`


Use `/api/show` to discover a model’s supported thinking values and default. `thinking.type: "enabled"` and `"disabled"` act as explicit on/off controls. When a model uses its metadata to resolve named levels, supported `output_config.effort` names are applied exactly and unsupported names resolve to the model default. Models without metadata keep the existing compatibility behavior, which trims and lowercases effort names and maps `"xhigh"` to `"high"`.


## [​](https://docs.ollama.com/api/anthropic-compatibility#models) Models


Ollama supports both local and cloud models. See the currently supported models [here](https://ollama.com/search).


### [​](https://docs.ollama.com/api/anthropic-compatibility#local-models) Local models


Pull a local model before use:


```
ollama pull qwen3-coder
```


### [​](https://docs.ollama.com/api/anthropic-compatibility#cloud-models) Cloud models


Browse the [cloud model catalog](https://ollama.com/search?c=cloud). Through a signed-in Ollama server, use a cloud name such as `gemma4:cloud` without a separate pull. For direct cloud requests, use the hosted identifier, such as `gemma4:31b`.


### [​](https://docs.ollama.com/api/anthropic-compatibility#default-model-names-on-a-local-server) Default model names on a local server


For tooling that relies on default Anthropic model names such as `claude-3-5-sonnet`, use `ollama cp` to copy an existing model name:


```
ollama cp qwen3-coder claude-3-5-sonnet
```


Afterwards, this new model name can be specified in the `model` field:


```
curl http://localhost:11434/v1/messages \
    -H "Content-Type: application/json" \
    -d '{
        "model": "claude-3-5-sonnet",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```


## [​](https://docs.ollama.com/api/anthropic-compatibility#differences-from-the-anthropic-api) Differences from the Anthropic API


### [​](https://docs.ollama.com/api/anthropic-compatibility#behavior-differences) Behavior differences


- The local server does not validate API keys. Direct cloud inference requires a valid bearer token.
- The hosted endpoint rejects `anthropic-version` values older than `2023-06-01`. Use `2023-06-01` in requests.
- Token counts are approximations based on the underlying model’s tokenizer


### [​](https://docs.ollama.com/api/anthropic-compatibility#not-supported) Not supported


The following Anthropic API features are not currently supported:


| Feature | Description |
| --- | --- |
| `/v1/messages/count_tokens` | Token counting endpoint |
| `tool_choice` | Forcing specific tool use or disabling tools |
| `metadata` | Request metadata (user_id) |
| Prompt caching | `cache_control` blocks for caching prefixes |
| Batches API | `/v1/messages/batches` for async batch processing |
| Citations | `citations` content blocks |
| PDF support | `document` content blocks with PDF files |
| Server-sent errors | `error` events during streaming (errors return HTTP status) |


### [​](https://docs.ollama.com/api/anthropic-compatibility#partial-support) Partial support


| Feature | Status |
| --- | --- |
| Image content | Base64 images supported; URL images not supported |
| Extended thinking | Basic support; `budget_tokens` accepted but not enforced |

⌘ I

---

# Claude Code - Ollama

`https://docs.ollama.com/integrations/claude-code`

[Claude Code](https://code.claude.com/docs/en/overview) reads your codebase, edits files, and runs commands.
Ollama connects Claude Code to local and cloud models through its Anthropic-compatible API.


## [​](https://docs.ollama.com/integrations/claude-code#get-started) Get started


Launch Claude Code with Ollama:


```
ollama launch claude
```


## [​](https://docs.ollama.com/integrations/claude-code#capabilities) Capabilities


Chat Ask questions about a repository or task Command line Run commands with Claude Code’s permission flow Tool calling Use tools with compatible models File edits Read and edit files in your project Subagents Split work across tasks Web search Search the web through Ollama Web fetch Fetch and summarize web pages Vision Send images and screenshots Thinking Use thinking controls with compatible models


## [​](https://docs.ollama.com/integrations/claude-code#models) Models


Choose a model with enough context for your repository.


## Cloud models

Use larger models without downloading them.

## Local models

Choose a model and set a 64k+ context window.
For larger repositories, set the [context length](https://docs.ollama.com/context-length) to 64k or higher.


## [​](https://docs.ollama.com/integrations/claude-code#more-features) More features


### [​](https://docs.ollama.com/integrations/claude-code#run-without-interaction) Run without interaction


Use `--yes` for scripts, Docker, or CI:


```
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```


The `--yes` flag skips selectors, pulls the model when needed, and requires `--model`. Arguments after `--` are passed directly to Claude Code.


### [​](https://docs.ollama.com/integrations/claude-code#web-search) Web search


Use Ollama’s web search API from Claude Code.
See [Web search](https://docs.ollama.com/capabilities/web-search) for setup and usage.


### [​](https://docs.ollama.com/integrations/claude-code#scheduled-tasks-with-/loop) Scheduled tasks with `/loop`


Use `/loop` inside Claude Code to run a prompt or slash command on a schedule:


```
/loop <interval> <prompt or /command>
```


Examples:


```
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```


### [​](https://docs.ollama.com/integrations/claude-code#telegram) Telegram


Connect a Telegram bot to your Claude Code session. Install the [Telegram plugin](https://github.com/anthropics/claude-plugins-official), create a bot with [@BotFather](https://t.me/BotFather), then launch Claude Code:


```
ollama launch claude -- --channels plugin:telegram@claude-plugins-official
```


Claude Code prompts for permission on most actions. To allow the bot to work autonomously, configure [permission rules](https://code.claude.com/docs/en/permissions) or pass `--dangerously-skip-permissions` in an isolated environment.
See the [plugin README](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/telegram) for setup instructions.


## [​](https://docs.ollama.com/integrations/claude-code#connect-directly-to-ollama%E2%80%99s-cloud) Connect directly to Ollama’s cloud


Install Claude Code, then set your [API key](https://docs.ollama.com/quickstart#build-an-application) in `OLLAMA_API_KEY`. No Ollama installation required.
In Bash or Zsh, run:


```
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```


Use `ANTHROPIC_AUTH_TOKEN` for bearer authentication. Claude settings can override shell variables. Update any base URL or credentials in those settings, then run `/status` to check the connection.
Choose a [cloud model](https://ollama.com/search?c=cloud) that supports tools. Basic chat and file edits work with compatible models. Hosted WebSearch and advanced tool controls are not fully supported. See [Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility).


## [​](https://docs.ollama.com/integrations/claude-code#manual-setup) Manual setup
## Documentation Index
## ​Get started
## ​Capabilities
## ​Models
## ​More features
## ​Connect directly to Ollama’s cloud
## ​Manual setup









1. Install Claude Code


macOS / Linux Windows

```
curl -fsSL https://claude.ai/install.sh | bash
```


```
irm https://claude.ai/install.ps1 | iex
```


2. Set the environment variables


```
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
```


3. Run Claude Code


```
claude --model qwen3.5
```


Or run with environment variables inline:


```
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

⌘ I

---

# OpenCode - Ollama

`https://docs.ollama.com/integrations/opencode`

[OpenCode](https://opencode.ai) is an open-source coding agent that runs in your terminal, reads your project, edits files, and runs commands.
Ollama configures OpenCode to use local and cloud models.


## [​](https://docs.ollama.com/integrations/opencode#get-started) Get started


Launch OpenCode with Ollama:


```
ollama launch opencode
```


## [​](https://docs.ollama.com/integrations/opencode#capabilities) Capabilities


Chat Ask questions about a repository or task Command line Run commands from your working directory File edits Read and edit files in your project Subagents Split work across tasks Web fetch Fetch and summarize web pages Vision Send images and screenshots


## [​](https://docs.ollama.com/integrations/opencode#models) Models


Choose a model with enough context for your repository.


## Cloud models

Use larger models without downloading them.

## Local models

Choose a model and set a 64k+ context window.
OpenCode requires a context length of 64k or higher. See [Context length](https://docs.ollama.com/context-length) for more information.


## [​](https://docs.ollama.com/integrations/opencode#manual-setup) Manual setup
## Documentation Index
## ​Get started
## ​Capabilities
## ​Models
## ​Manual setup







1. Install OpenCode


macOS / Linux Windows

```
curl -fsSL https://opencode.ai/install | bash
```


```
npm install -g opencode-ai
```


2. Configure Ollama as a provider


Add an Ollama provider to `opencode.json`:


```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3.5": {
          "name": "qwen3.5"
        }
      }
    }
  }
}
```


3. Run OpenCode


```
opencode
```


To configure OpenCode with Ollama without starting an interactive session:


```
ollama launch opencode --config
```


### [​](https://docs.ollama.com/integrations/opencode#configuration-precedence) Configuration precedence


`ollama launch opencode` starts OpenCode with an inline config for the selected Ollama model. It does not overwrite `~/.config/opencode/opencode.json`; existing OpenCode settings still apply.
Models defined only in `opencode.json` do not appear in the `ollama launch` model picker.
See OpenCode’s [config precedence](https://opencode.ai/docs/config/#precedence-order). ⌘ I

---

# Codex CLI - Ollama

`https://docs.ollama.com/integrations/codex`

## [​](https://docs.ollama.com/integrations/codex#install) Install


Install the [Codex CLI](https://developers.openai.com/codex/cli/). For the ChatGPT desktop app, see [ChatGPT Desktop](https://docs.ollama.com/integrations/chatgpt).


```
npm install -g @openai/codex
```


## [​](https://docs.ollama.com/integrations/codex#usage-with-ollama) Usage with Ollama


Use a context window of at least 64k tokens for Codex.


### [​](https://docs.ollama.com/integrations/codex#quick-setup) Quick setup


```
ollama launch codex
```


When launched through `ollama launch codex`, Ollama refreshes the model catalog
and uses a dedicated Codex profile for that session.
Type `/model` inside Codex to switch between your installed, tool-capable Ollama
models without restarting. The starting model remains selected, and each model
keeps its own context window, vision, and thinking settings. Pull additional
models with `ollama pull <model>` before launching to include them in the picker.
To configure without launching:


```
ollama launch codex --config
```


To remove the Ollama launch profile and generated model catalog:


```
ollama launch codex --restore
```


### [​](https://docs.ollama.com/integrations/codex#manual-setup) Manual setup


To use `codex` with Ollama, use the `--oss` flag:


```
codex --oss
```


To use a specific model, pass the `-m` flag:


```
codex --oss -m gpt-oss:120b
```


To use a cloud model:


```
codex --oss -m gpt-oss:120b-cloud
```


### [​](https://docs.ollama.com/integrations/codex#profile-based-setup) Profile-based setup


For a persistent Codex CLI configuration, create `~/.codex/ollama-launch.config.toml`:


```
model = "gpt-oss:120b"
model_provider = "ollama-launch"
model_catalog_json = "/Users/you/.codex/model.json"

[model_providers.ollama-launch]
name = "Ollama"
base_url = "http://localhost:11434/v1/"
wire_api = "responses"
```


Then run:


```
codex --profile ollama-launch
```


## [​](https://docs.ollama.com/integrations/codex#web-search-through-local-ollama) Web search through local Ollama


Codex web-search requests sent through the Ollama profile are executed by
Ollama for both local and cloud models. Sign in with `ollama signin` to use the
web-search service.
To disable web search for a Codex session:


```
codex --profile ollama-launch -c 'web_search="disabled"'
```

⌘ I

---

# Claude Desktop - Ollama

`https://docs.ollama.com/integrations/claude-desktop`

# Claude Desktop

## [​](https://docs.ollama.com/integrations/claude-desktop#prerequisites) Prerequisites


- [Ollama](https://ollama.com/download/). Windows support coming soon.
- To use a local model, [download it](https://docs.ollama.com/quickstart#run-a-model-locally) before setup.
- To use a cloud model, sign in to Ollama and enable cloud models. Some models require a [paid plan](https://ollama.com/pricing).


If Claude is not installed, Ollama offers to download it during setup.


## [​](https://docs.ollama.com/integrations/claude-desktop#set-up-claude) Set up Claude


1. Open Ollama and select **Apps**.
2. Connect **Claude**.
3. Follow the setup prompts to install Claude if needed and restart it when prompted.


## [​](https://docs.ollama.com/integrations/claude-desktop#switch-models) Switch models


Open Ollama **Settings → Apps**. Choose your models, then select **Restart Claude**. You can use the same model for more than one option.


## [​](https://docs.ollama.com/integrations/claude-desktop#supported-features) Supported features


- **Subagents** - Split larger tasks across agents
- **Web search** - Supported by default through [Ollama’s web search](https://docs.ollama.com/capabilities/web-search)
- **Cowork** - Complete difficult tasks with Claude Cowork
- **Auto mode** - Let the agent decide when to ask before making changes


## [​](https://docs.ollama.com/integrations/claude-desktop#disconnect-claude) Disconnect Claude


Open Ollama **Apps** and disconnect Claude. Ollama restores Claude’s previous settings. Restart Claude when prompted.
You can also restore Claude from the terminal:


```
ollama launch claude-desktop --restore
```


Quitting Ollama while Claude is connected also restores Claude’s usual configuration. ⌘ I

---

# Cloud - Ollama

`https://docs.ollama.com/cloud`

Run models in Ollama’s cloud from your apps or terminal. No model or app download required.


## [​](https://docs.ollama.com/cloud#api-key) API Key


Create an [API key](https://ollama.com/settings/keys), then set it in Bash or Zsh:


```
export OLLAMA_API_KEY="your_api_key"
```


Send a request from the same terminal:


```
curl https://ollama.com/api/chat \
  -H "Authorization: Bearer $OLLAMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:31b",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in one sentence."
      }
    ],
    "stream": false
  }'
```


Read the answer from `message.content`. Keep your API key out of browser code and source control.
You can also use [OpenAI](https://docs.ollama.com/api/openai-compatibility) or [Anthropic](https://docs.ollama.com/api/anthropic-compatibility) clients. Each supports a subset of the original API. No Ollama installation is required.


## [​](https://docs.ollama.com/cloud#ollama-app-or-cli) Ollama App or CLI


[Download Ollama](https://ollama.com/download). Open the app, or run:


```
ollama
```


Follow the setup prompts and sign in to use cloud models.
On macOS, open **Apps** and connect Claude or ChatGPT. For coding agents, run a launch command:
Claude Code Codex CLI OpenCode

```
ollama launch claude
```


```
ollama launch codex
```


```
ollama launch opencode
```


For more integrations, open the Ollama app or run `ollama` in your terminal.
Ollama handles sign-in for connected apps. See the [quickstart](https://docs.ollama.com/quickstart) for setup.


## [​](https://docs.ollama.com/cloud#models) Models


Browse [cloud models](https://ollama.com/search?c=cloud), or list them with the API:


```
curl https://ollama.com/api/tags
```


For API requests to ollama.com, use the name returned by this list, such as `gemma4:31b`. In the Ollama app or CLI, use `gemma4:cloud`. Cloud models do not need to be downloaded.


## [​](https://docs.ollama.com/cloud#usage) Usage


Check your [usage](https://ollama.com/settings/usage) or compare [plans](https://ollama.com/pricing).


## [​](https://docs.ollama.com/cloud#retirements) Retirements


[Usage settings](https://ollama.com/settings) show upcoming retirements for models you’ve recently used. Switch models before the retirement date. Downloaded local models are not affected.


## [​](https://docs.ollama.com/cloud#data-handling) Data handling


Ollama processes cloud prompts and responses to answer your requests. We do not use them to train models. Read the [Privacy Policy](https://ollama.com/privacy) for details.
To use only local models, [disable cloud features](https://docs.ollama.com/faq#how-do-i-disable-ollama-cloud-features). ⌘ I

---

# Tool calling - Ollama

`https://docs.ollama.com/capabilities/tool-calling`

Ollama supports tool calling (also known as function calling) which allows a model to invoke tools and incorporate their results into its replies.


## [​](https://docs.ollama.com/capabilities/tool-calling#calling-a-single-tool) Calling a single tool


Invoke a single tool and include its response in a follow-up request.
Also known as “single-shot” tool calling.


- cURL
- Python
- JavaScript


```
curl -s http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "qwen3",
  "messages": [{"role": "user", "content": "What is the temperature in New York?"}],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_temperature",
        "description": "Get the current temperature for a city",
        "parameters": {
          "type": "object",
          "required": ["city"],
          "properties": {
            "city": {"type": "string", "description": "The name of the city"}
          }
        }
      }
    }
  ]
}'
```

**Generate a response with a single tool result**

```
curl -s http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "qwen3",
  "messages": [
    {"role": "user", "content": "What is the temperature in New York?"},
    {
      "role": "assistant",
      "tool_calls": [
        {
          "type": "function",
          "function": {
            "index": 0,
            "name": "get_temperature",
            "arguments": {"city": "New York"}
          }
        }
      ]
    },
    {"role": "tool", "tool_name": "get_temperature", "content": "22°C"}
  ],
  "stream": false
}'
```

Install the Ollama Python SDK:

```
# with pip
pip install ollama -U

# with uv
uv add ollama
```


```
from ollama import chat

def get_temperature(city: str) -> str:
  """Get the current temperature for a city

  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    "New York": "22°C",
    "London": "15°C",
    "Tokyo": "18°C",
  }
  return temperatures.get(city, "Unknown")

messages = [{"role": "user", "content": "What is the temperature in New York?"}]

# pass functions directly as tools in the tools list or as a JSON schema
response = chat(model="qwen3", messages=messages, tools=[get_temperature], think=True)

messages.append(response.message)
if response.message.tool_calls:
  # only recommended for models which only return a single tool call
  call = response.message.tool_calls[0]
  result = get_temperature(**call.function.arguments)
  # add the tool result to the messages
  messages.append({"role": "tool", "tool_name": call.function.name, "content": str(result)})

  final_response = chat(model="qwen3", messages=messages, tools=[get_temperature], think=True)
  print(final_response.message.content)
```

Install the Ollama JavaScript library:

```
# with npm
npm i ollama

# with bun
bun i ollama
```


```
import ollama from 'ollama'

function getTemperature(city: string): string {
  const temperatures: Record<string, string> = {
    'New York': '22°C',
    'London': '15°C',
    'Tokyo': '18°C',
  }
  return temperatures[city] ?? 'Unknown'
}

const tools = [
  {
    type: 'function',
    function: {
      name: 'get_temperature',
      description: 'Get the current temperature for a city',
      parameters: {
        type: 'object',
        required: ['city'],
        properties: {
          city: { type: 'string', description: 'The name of the city' },
        },
      },
    },
  },
]

const messages = [{ role: 'user', content: "What is the temperature in New York?" }]

const response = await ollama.chat({
  model: 'qwen3',
  messages,
  tools,
  think: true,
})

messages.push(response.message)
if (response.message.tool_calls?.length) {
  // only recommended for models which only return a single tool call
  const call = response.message.tool_calls[0]
  const args = call.function.arguments as { city: string }
  const result = getTemperature(args.city)
  // add the tool result to the messages
  messages.push({ role: 'tool', tool_name: call.function.name, content: result })

  // generate the final response
  const finalResponse = await ollama.chat({ model: 'qwen3', messages, tools, think: true })
  console.log(finalResponse.message.content)
}
```


## [​](https://docs.ollama.com/capabilities/tool-calling#parallel-tool-calling) Parallel tool calling


- cURL
- Python
- JavaScript

Request multiple tool calls in parallel, then send all tool responses back to the model.

```
curl -s http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "qwen3",
  "messages": [{"role": "user", "content": "What are the current weather conditions and temperature in New York and London?"}],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_temperature",
        "description": "Get the current temperature for a city",
        "parameters": {
          "type": "object",
          "required": ["city"],
          "properties": {
            "city": {"type": "string", "description": "The name of the city"}
          }
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_conditions",
        "description": "Get the current weather conditions for a city",
        "parameters": {
          "type": "object",
          "required": ["city"],
          "properties": {
            "city": {"type": "string", "description": "The name of the city"}
          }
        }
      }
    }
  ]
}'
```

**Generate a response with multiple tool results**

```
curl -s http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "qwen3",
  "messages": [
    {"role": "user", "content": "What are the current weather conditions and temperature in New York and London?"},
    {
      "role": "assistant",
      "tool_calls": [
        {
          "type": "function",
          "function": {
            "index": 0,
            "name": "get_temperature",
            "arguments": {"city": "New York"}
          }
        },
        {
          "type": "function",
          "function": {
            "index": 1,
            "name": "get_conditions",
            "arguments": {"city": "New York"}
          }
        },
        {
          "type": "function",
          "function": {
            "index": 2,
            "name": "get_temperature",
            "arguments": {"city": "London"}
          }
        },
        {
          "type": "function",
          "function": {
            "index": 3,
            "name": "get_conditions",
            "arguments": {"city": "London"}
          }
        }
      ]
    },
    {"role": "tool", "tool_name": "get_temperature", "content": "22°C"},
    {"role": "tool", "tool_name": "get_conditions", "content": "Partly cloudy"},
    {"role": "tool", "tool_name": "get_temperature", "content": "15°C"},
    {"role": "tool", "tool_name": "get_conditions", "content": "Rainy"}
  ],
  "stream": false
}'
```


```
from ollama import chat

def get_temperature(city: str) -> str:
  """Get the current temperature for a city

  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    "New York": "22°C",
    "London": "15°C",
    "Tokyo": "18°C"
  }
  return temperatures.get(city, "Unknown")

def get_conditions(city: str) -> str:
  """Get the current weather conditions for a city

  Args:
    city: The name of the city

  Returns:
    The current weather conditions for the city
  """
  conditions = {
    "New York": "Partly cloudy",
    "London": "Rainy",
    "Tokyo": "Sunny"
  }
  return conditions.get(city, "Unknown")


messages = [{'role': 'user', 'content': 'What are the current weather conditions and temperature in New York and London?'}]

# The python client automatically parses functions as a tool schema so we can pass them directly
# Schemas can be passed directly in the tools list as well
response = chat(model='qwen3', messages=messages, tools=[get_temperature, get_conditions], think=True)

# add the assistant message to the messages
messages.append(response.message)
if response.message.tool_calls:
  # process each tool call
  for call in response.message.tool_calls:
    # execute the appropriate tool
    if call.function.name == 'get_temperature':
      result = get_temperature(**call.function.arguments)
    elif call.function.name == 'get_conditions':
      result = get_conditions(**call.function.arguments)
    else:
      result = 'Unknown tool'
    # add the tool result to the messages
    messages.append({'role': 'tool',  'tool_name': call.function.name, 'content': str(result)})

  # generate the final response
  final_response = chat(model='qwen3', messages=messages, tools=[get_temperature, get_conditions], think=True)
  print(final_response.message.content)
```


```
import ollama from 'ollama'

function getTemperature(city: string): string {
  const temperatures: { [key: string]: string } = {
    "New York": "22°C",
    "London": "15°C",
    "Tokyo": "18°C"
  }
  return temperatures[city] || "Unknown"
}

function getConditions(city: string): string {
  const conditions: { [key: string]: string } = {
    "New York": "Partly cloudy",
    "London": "Rainy",
    "Tokyo": "Sunny"
  }
  return conditions[city] || "Unknown"
}

const tools = [
  {
    type: 'function',
    function: {
      name: 'get_temperature',
      description: 'Get the current temperature for a city',
      parameters: {
        type: 'object',
        required: ['city'],
        properties: {
          city: { type: 'string', description: 'The name of the city' },
        },
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'get_conditions',
      description: 'Get the current weather conditions for a city',
      parameters: {
        type: 'object',
        required: ['city'],
        properties: {
          city: { type: 'string', description: 'The name of the city' },
        },
      },
    },
  }
]

const messages = [{ role: 'user', content: 'What are the current weather conditions and temperature in New York and London?' }]

const response = await ollama.chat({
  model: 'qwen3',
  messages,
  tools,
  think: true
})

// add the assistant message to the messages
messages.push(response.message)
if (response.message.tool_calls) {
  // process each tool call
  for (const call of response.message.tool_calls) {
    // execute the appropriate tool
    let result: string
    if (call.function.name === 'get_temperature') {
      const args = call.function.arguments as { city: string }
      result = getTemperature(args.city)
    } else if (call.function.name === 'get_conditions') {
      const args = call.function.arguments as { city: string }
      result = getConditions(args.city)
    } else {
      result = 'Unknown tool'
    }
    // add the tool result to the messages
    messages.push({ role: 'tool', tool_name: call.function.name, content: result })
  }

  // generate the final response
  const finalResponse = await ollama.chat({ model: 'qwen3', messages, tools, think: true })
  console.log(finalResponse.message.content)
}
```


## [​](https://docs.ollama.com/capabilities/tool-calling#multi-turn-tool-calling-agent-loop) Multi-turn tool calling (Agent loop)


An agent loop allows the model to decide when to invoke tools and incorporate their results into its replies.
It also might help to tell the model that it is in a loop and can make multiple tool calls.


- Python
- JavaScript


```
from ollama import chat, ChatResponse


def add(a: int, b: int) -> int:
  """Add two numbers"""
  """
  Args:
    a: The first number
    b: The second number

  Returns:
    The sum of the two numbers
  """
  return a + b


def multiply(a: int, b: int) -> int:
  """Multiply two numbers"""
  """
  Args:
    a: The first number
    b: The second number

  Returns:
    The product of the two numbers
  """
  return a * b


available_functions = {
  'add': add,
  'multiply': multiply,
}

messages = [{'role': 'user', 'content': 'What is (11434+12341)*412?'}]
while True:
    response: ChatResponse = chat(
        model='qwen3',
        messages=messages,
        tools=[add, multiply],
        think=True,
    )
    messages.append(response.message)
    print("Thinking: ", response.message.thinking)
    print("Content: ", response.message.content)
    if response.message.tool_calls:
        for tc in response.message.tool_calls:
            if tc.function.name in available_functions:
                print(f"Calling {tc.function.name} with arguments {tc.function.arguments}")
                result = available_functions[tc.function.name](**tc.function.arguments)
                print(f"Result: {result}")
                # add the tool result to the messages
                messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
    else:
        # end the loop when there are no more tool calls
        break
  # continue the loop with the updated messages
```


```
import ollama from 'ollama'

type ToolName = 'add' | 'multiply'

function add(a: number, b: number): number {
  return a + b
}

function multiply(a: number, b: number): number {
  return a * b
}

const availableFunctions: Record<ToolName, (a: number, b: number) => number> = {
  add,
  multiply,
}

const tools = [
  {
    type: 'function',
    function: {
      name: 'add',
      description: 'Add two numbers',
      parameters: {
        type: 'object',
        required: ['a', 'b'],
        properties: {
          a: { type: 'integer', description: 'The first number' },
          b: { type: 'integer', description: 'The second number' },
        },
      },
    },
  },
  {
    type: 'function',
    function: {
      name: 'multiply',
      description: 'Multiply two numbers',
      parameters: {
        type: 'object',
        required: ['a', 'b'],
        properties: {
          a: { type: 'integer', description: 'The first number' },
          b: { type: 'integer', description: 'The second number' },
        },
      },
    },
  },
]

async function agentLoop() {
  const messages = [{ role: 'user', content: 'What is (11434+12341)*412?' }]

  while (true) {
    const response = await ollama.chat({
      model: 'qwen3',
      messages,
      tools,
      think: true,
    })

    messages.push(response.message)
    console.log('Thinking:', response.message.thinking)
    console.log('Content:', response.message.content)

    const toolCalls = response.message.tool_calls ?? []
    if (toolCalls.length) {
      for (const call of toolCalls) {
        const fn = availableFunctions[call.function.name as ToolName]
        if (!fn) {
          continue
        }

        const args = call.function.arguments as { a: number; b: number }
        console.log(`Calling ${call.function.name} with arguments`, args)
        const result = fn(args.a, args.b)
        console.log(`Result: ${result}`)
        messages.push({ role: 'tool', tool_name: call.function.name, content: String(result) })
      }
    } else {
      break
    }
  }
}

agentLoop().catch(console.error)
```


## [​](https://docs.ollama.com/capabilities/tool-calling#tool-calling-with-streaming) Tool calling with streaming


When streaming, gather every chunk of `thinking`, `content`, and `tool_calls`, then return those fields together with any tool results in the follow-up request.


- Python
- JavaScript


```
from ollama import chat


def get_temperature(city: str) -> str:
  """Get the current temperature for a city

  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    'New York': '22°C',
    'London': '15°C',
  }
  return temperatures.get(city, 'Unknown')


messages = [{'role': 'user', 'content': "What is the temperature in New York?"}]

while True:
  stream = chat(
    model='qwen3',
    messages=messages,
    tools=[get_temperature],
    stream=True,
    think=True,
  )

  thinking = ''
  content = ''
  tool_calls = []

  done_thinking = False
  # accumulate the partial fields
  for chunk in stream:
    if chunk.message.thinking:
      thinking += chunk.message.thinking
      print(chunk.message.thinking, end='', flush=True)
    if chunk.message.content:
      if not done_thinking:
        done_thinking = True
        print('\n')
      content += chunk.message.content
      print(chunk.message.content, end='', flush=True)
    if chunk.message.tool_calls:
      tool_calls.extend(chunk.message.tool_calls)
      print(chunk.message.tool_calls)

  # append accumulated fields to the messages
  if thinking or content or tool_calls:
    messages.append({'role': 'assistant', 'thinking': thinking, 'content': content, 'tool_calls': tool_calls})

  if not tool_calls:
    break

  for call in tool_calls:
    if call.function.name == 'get_temperature':
      result = get_temperature(**call.function.arguments)
    else:
      result = 'Unknown tool'
    messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': result})
```


```
import ollama from 'ollama'

function getTemperature(city: string): string {
  const temperatures: Record<string, string> = {
    'New York': '22°C',
    'London': '15°C',
  }
  return temperatures[city] ?? 'Unknown'
}

const getTemperatureTool = {
  type: 'function',
  function: {
    name: 'get_temperature',
    description: 'Get the current temperature for a city',
    parameters: {
      type: 'object',
      required: ['city'],
      properties: {
        city: { type: 'string', description: 'The name of the city' },
      },
    },
  },
}

async function agentLoop() {
  const messages = [{ role: 'user', content: "What is the temperature in New York?" }]

  while (true) {
    const stream = await ollama.chat({
      model: 'qwen3',
      messages,
      tools: [getTemperatureTool],
      stream: true,
      think: true,
    })

    let thinking = ''
    let content = ''
    const toolCalls: any[] = []
    let doneThinking = false

    for await (const chunk of stream) {
      if (chunk.message.thinking) {
        thinking += chunk.message.thinking
        process.stdout.write(chunk.message.thinking)
      }
      if (chunk.message.content) {
        if (!doneThinking) {
          doneThinking = true
          process.stdout.write('\n')
        }
        content += chunk.message.content
        process.stdout.write(chunk.message.content)
      }
      if (chunk.message.tool_calls?.length) {
        toolCalls.push(...chunk.message.tool_calls)
        console.log(chunk.message.tool_calls)
      }
    }

    if (thinking || content || toolCalls.length) {
      messages.push({ role: 'assistant', thinking, content, tool_calls: toolCalls } as any)
    }

    if (!toolCalls.length) {
      break
    }

    for (const call of toolCalls) {
      if (call.function.name === 'get_temperature') {
        const args = call.function.arguments as { city: string }
        const result = getTemperature(args.city)
        messages.push({ role: 'tool', tool_name: call.function.name, content: result } )
      } else {
        messages.push({ role: 'tool', tool_name: call.function.name, content: 'Unknown tool' } )
      }
    }
  }
}

agentLoop().catch(console.error)
```


This loop streams the assistant response, accumulates partial fields, passes them back together, and appends the tool results so the model can complete its answer.


## [​](https://docs.ollama.com/capabilities/tool-calling#using-functions-as-tools-with-ollama-python-sdk) Using functions as tools with Ollama Python SDK


The Python SDK automatically parses functions as a tool schema so we can pass them directly.
Schemas can still be passed if needed.


```
from ollama import chat

def get_temperature(city: str) -> str:
  """Get the current temperature for a city

  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    'New York': '22°C',
    'London': '15°C',
  }
  return temperatures.get(city, 'Unknown')

available_functions = {
  'get_temperature': get_temperature,
}
# directly pass the function as part of the tools list
response = chat(model='qwen3', messages=messages, tools=available_functions.values(), think=True)
```

⌘ I

---

# OpenClaw - Ollama

`https://docs.ollama.com/integrations/openclaw`

OpenClaw is a personal AI assistant that runs on your own devices. It bridges messaging services (WhatsApp, Telegram, Slack, Discord, iMessage, and more) to AI coding agents through a centralized gateway.


## [​](https://docs.ollama.com/integrations/openclaw#quick-start) Quick start


```
ollama launch openclaw
```


Ollama handles everything automatically:


1. **Install** — If OpenClaw isn’t installed, Ollama prompts to install it via npm
2. **Security** — On the first launch, a security notice explains the risks of tool access
3. **Model** — Pick a model from the selector (see supported local and cloud models [here](https://ollama.com/search))
4. **Onboarding** — Ollama configures the provider, installs the gateway daemon, sets your model as the primary, and enables OpenClaw’s bundled Ollama web search
5. **Gateway** — Starts in the background and opens the OpenClaw TUI


OpenClaw requires a larger context window. It is recommended to use a context window of at least 64k tokens if using local models. See [Context length](https://docs.ollama.com/context-length) for more information.
Previously known as Clawdbot. `ollama launch clawdbot` still works as an alias.


## [​](https://docs.ollama.com/integrations/openclaw#web-search-and-fetch) Web search and fetch


OpenClaw ships with a bundled Ollama `web_search` provider that lets local or cloud-backed Ollama setups search the web through the configured Ollama host.


```
ollama launch openclaw
```


Ollama web search is enabled automatically when launching OpenClaw through Ollama. To configure it manually:


```
openclaw configure --section web
```


Ollama web search for local models requires `ollama signin`.


## [​](https://docs.ollama.com/integrations/openclaw#configure-without-launching) Configure without launching


To change the model without starting the gateway and TUI:


```
ollama launch openclaw --config
```


To use a specific model directly:


```
ollama launch openclaw --model kimi-k2.5:cloud
```


If the gateway is already running, it restarts automatically to pick up the new model.


## [​](https://docs.ollama.com/integrations/openclaw#non-interactive-headless-mode) Non-interactive (headless) mode


Run OpenClaw without interaction for use in Docker, CI/CD, or scripts:


```
ollama launch openclaw --model kimi-k2.5:cloud --yes
```


The `--yes` flag auto-pulls the model, skips selectors, and requires `--model` to be specified.


## [​](https://docs.ollama.com/integrations/openclaw#connect-messaging-apps) Connect messaging apps


```
openclaw configure --section channels
```


Link WhatsApp, Telegram, Slack, Discord, or iMessage to chat with your local models from anywhere.


## [​](https://docs.ollama.com/integrations/openclaw#stopping-the-gateway) Stopping the gateway


```
openclaw gateway stop
```

⌘ I

---

# Web search - Ollama

`https://docs.ollama.com/capabilities/web-search`

Ollama’s web search API can be used to augment models with the latest information to reduce hallucinations and improve accuracy.
Web search is provided as a REST API with deeper tool integrations in the Python and JavaScript libraries. This also enables models like OpenAI’s gpt-oss models to conduct long-running research tasks.


## [​](https://docs.ollama.com/capabilities/web-search#authentication) Authentication


For access to Ollama’s web search API, create an [API key](https://ollama.com/settings/keys). A free Ollama account is required.


## [​](https://docs.ollama.com/capabilities/web-search#web-search-api) Web search API


Performs a web search for a single query and returns relevant results.


### [​](https://docs.ollama.com/capabilities/web-search#request) Request


`POST https://ollama.com/api/web_search`


- `query` (string, required): the search query string
- `max_results` (integer, optional): maximum results to return (default 5, max 10)


### [​](https://docs.ollama.com/capabilities/web-search#response) Response


Returns an object containing:


- `results` (array): array of search result objects, each containing:
  - `title` (string): the title of the web page
  - `url` (string): the URL of the web page
  - `content` (string): relevant content snippet from the web page


### [​](https://docs.ollama.com/capabilities/web-search#examples) Examples


Ensure OLLAMA_API_KEY is set or it must be passed in the Authorization header.


#### [​](https://docs.ollama.com/capabilities/web-search#curl-request) cURL Request


```
curl https://ollama.com/api/web_search \
  --header "Authorization: Bearer $OLLAMA_API_KEY" \
	-d '{
	  "query":"what is ollama?"
	}'
```


**Response**


```
{
  "results": [
    {
      "title": "Ollama",
      "url": "https://ollama.com/",
      "content": "Cloud models are now available..."
    },
    {
      "title": "What is Ollama? Introduction to the AI model management tool",
      "url": "https://www.hostinger.com/tutorials/what-is-ollama",
      "content": "Ariffud M. 6min Read..."
    },
    {
      "title": "Ollama Explained: Transforming AI Accessibility and Language ...",
      "url": "https://www.geeksforgeeks.org/artificial-intelligence/ollama-explained-transforming-ai-accessibility-and-language-processing/",
      "content": "Data Science Data Science Projects Data Analysis..."
    }
  ]
}
```


#### [​](https://docs.ollama.com/capabilities/web-search#python-library) Python library


```
import ollama
response = ollama.web_search("What is Ollama?")
print(response)
```


**Example output**


```
results = [
    {
        "title": "Ollama",
        "url": "https://ollama.com/",
        "content": "Cloud models are now available in Ollama..."
    },
    {
        "title": "What is Ollama? Features, Pricing, and Use Cases - Walturn",
        "url": "https://www.walturn.com/insights/what-is-ollama-features-pricing-and-use-cases",
        "content": "Our services..."
    },
    {
        "title": "Complete Ollama Guide: Installation, Usage & Code Examples",
        "url": "https://collabnix.com/complete-ollama-guide-installation-usage-code-examples",
        "content": "Join our Discord Server..."
    }
]
```


More Ollama [Python example](https://github.com/ollama/ollama-python/blob/main/examples/web-search.py)


#### [​](https://docs.ollama.com/capabilities/web-search#javascript-library) JavaScript Library


```
import { Ollama } from "ollama";

const client = new Ollama();
const results = await client.webSearch("what is ollama?");
console.log(JSON.stringify(results, null, 2));
```


**Example output**


```
{
  "results": [
    {
      "title": "Ollama",
      "url": "https://ollama.com/",
      "content": "Cloud models are now available..."
    },
    {
      "title": "What is Ollama? Introduction to the AI model management tool",
      "url": "https://www.hostinger.com/tutorials/what-is-ollama",
      "content": "Ollama is an open-source tool..."
    },
    {
      "title": "Ollama Explained: Transforming AI Accessibility and Language Processing",
      "url": "https://www.geeksforgeeks.org/artificial-intelligence/ollama-explained-transforming-ai-accessibility-and-language-processing/",
      "content": "Ollama is a groundbreaking..."
    }
  ]
}
```


More Ollama [JavaScript example](https://github.com/ollama/ollama-js/blob/main/examples/websearch/websearch-tools.ts)


## [​](https://docs.ollama.com/capabilities/web-search#web-fetch-api) Web fetch API


Fetches a single web page by URL and returns its content.


### [​](https://docs.ollama.com/capabilities/web-search#request-2) Request


`POST https://ollama.com/api/web_fetch`


- `url` (string, required): the URL to fetch


### [​](https://docs.ollama.com/capabilities/web-search#response-2) Response


Returns an object containing:


- `title` (string): the title of the web page
- `content` (string): the main content of the web page
- `links` (array): array of links found on the page


### [​](https://docs.ollama.com/capabilities/web-search#examples-2) Examples


#### [​](https://docs.ollama.com/capabilities/web-search#curl-request-2) cURL Request


```
curl --request POST \
  --url https://ollama.com/api/web_fetch \
  --header "Authorization: Bearer $OLLAMA_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
      "url": "ollama.com"
  }'
```


**Response**


```
{
  "title": "Ollama",
  "content": "[Cloud models](https://ollama.com/blog/cloud-models) are now available in Ollama...",
  "links": [
    "http://ollama.com/",
    "http://ollama.com/models",
    "https://github.com/ollama/ollama"
  ]
```


#### [​](https://docs.ollama.com/capabilities/web-search#python-sdk) Python SDK


```
from ollama import web_fetch

result = web_fetch('https://ollama.com')
print(result)
```


**Result**


```
WebFetchResponse(
    title='Ollama',
    content='[Cloud models](https://ollama.com/blog/cloud-models) are now available in Ollama\n\n**Chat & build
with open models**\n\n[Download](https://ollama.com/download) [Explore
models](https://ollama.com/models)\n\nAvailable for macOS, Windows, and Linux',
    links=['https://ollama.com/', 'https://ollama.com/models', 'https://github.com/ollama/ollama']
)
```


#### [​](https://docs.ollama.com/capabilities/web-search#javascript-sdk) JavaScript SDK


```
import { Ollama } from "ollama";

const client = new Ollama();
const fetchResult = await client.webFetch("https://ollama.com");
console.log(JSON.stringify(fetchResult, null, 2));
```


**Result**


```
{
  "title": "Ollama",
  "content": "[Cloud models](https://ollama.com/blog/cloud-models) are now available in Ollama...",
  "links": [
    "https://ollama.com/",
    "https://ollama.com/models",
    "https://github.com/ollama/ollama"
  ]
}
```


## [​](https://docs.ollama.com/capabilities/web-search#building-a-search-agent) Building a search agent


Use Ollama’s web search API as a tool to build a mini search agent.
This example uses Alibaba’s Qwen 3 model with 4B parameters.


```
ollama pull qwen3:4b
```


```
from ollama import chat, web_fetch, web_search

available_tools = {'web_search': web_search, 'web_fetch': web_fetch}

messages = [{'role': 'user', 'content': "what is ollama's new engine"}]

while True:
  response = chat(
    model='qwen3:4b',
    messages=messages,
    tools=[web_search, web_fetch],
    think=True
    )
  if response.message.thinking:
    print('Thinking: ', response.message.thinking)
  if response.message.content:
    print('Content: ', response.message.content)
  messages.append(response.message)
  if response.message.tool_calls:
    print('Tool calls: ', response.message.tool_calls)
    for tool_call in response.message.tool_calls:
      function_to_call = available_tools.get(tool_call.function.name)
      if function_to_call:
        args = tool_call.function.arguments
        result = function_to_call(**args)
        print('Result: ', str(result)[:200]+'...')
        # Result is truncated for limited context lengths
        messages.append({'role': 'tool', 'content': str(result)[:2000 * 4], 'tool_name': tool_call.function.name})
      else:
        messages.append({'role': 'tool', 'content': f'Tool {tool_call.function.name} not found', 'tool_name': tool_call.function.name})
  else:
    break
```


**Result**


```
Thinking:  Okay, the user is asking about Ollama's new engine. I need to figure out what they're referring to. Ollama is a company that develops large language models, so maybe they've released a new model or an updated version of their existing engine....

Tool calls:  [ToolCall(function=Function(name='web_search', arguments={'max_results': 3, 'query': 'Ollama new engine'}))]
Result:  results=[WebSearchResult(content='# New model scheduling\n\n## September 23, 2025\n\nOllama now includes a significantly improved model scheduling system. Ahead of running a model, Ollama’s new engine

Thinking:  Okay, the user asked about Ollama's new engine. Let me look at the search results.

First result is from September 23, 2025, talking about new model scheduling. It mentions improved memory management, reduced crashes, better GPU utilization, and multi-GPU performance. Examples show speed improvements and accurate memory reporting. Supported models include gemma3, llama4, qwen3, etc...

Content:  Ollama has introduced two key updates to its engine, both released in 2025:

1. **Enhanced Model Scheduling (September 23, 2025)**
   - **Precision Memory Management**: Exact memory allocation reduces out-of-memory crashes and optimizes GPU utilization.
   - **Performance Gains**: Examples show significant speed improvements (e.g., 85.54 tokens/s vs 52.02 tokens/s) and full GPU layer utilization.
   - **Multi-GPU Support**: Improved efficiency across multiple GPUs, with accurate memory reporting via tools like `nvidia-smi`.
   - **Supported Models**: Includes `gemma3`, `llama4`, `qwen3`, `mistral-small3.2`, and more.

2. **Multimodal Engine (May 15, 2025)**
   - **Vision Support**: First-class support for vision models, including `llama4:scout` (109B parameters), `gemma3`, `qwen2.5vl`, and `mistral-small3.1`.
   - **Multimodal Tasks**: Examples include identifying animals in multiple images, answering location-based questions from videos, and document scanning.

These updates highlight Ollama's focus on efficiency, performance, and expanded capabilities for both text and vision tasks.
```


### [​](https://docs.ollama.com/capabilities/web-search#context-length-and-agents) Context length and agents


Web search results can return thousands of tokens. It is recommended to increase the context length of the model to at least ~32000 tokens. Search agents work best with full context length. [Ollama’s cloud models](https://docs.ollama.com/cloud) run at the full context length.


## [​](https://docs.ollama.com/capabilities/web-search#mcp-server) MCP Server


You can enable web search in any MCP client through the [Python MCP server](https://github.com/ollama/ollama-python/blob/main/examples/web-search-mcp.py).


### [​](https://docs.ollama.com/capabilities/web-search#cline) Cline


Ollama’s web search can be integrated with Cline easily using the MCP server configuration.
`Manage MCP Servers` > `Configure MCP Servers` > Add the following configuration:


```
{
  "mcpServers": {
    "web_search_and_fetch": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "path/to/web-search-mcp.py"],
      "env": { "OLLAMA_API_KEY": "your_api_key_here" }
    }
  }
}
```


![Cline MCP Configuration](https://mintcdn.com/ollama-9269c548/lS1IbrlCxMxm029K/images/cline-mcp.png?fit=max&auto=format&n=lS1IbrlCxMxm029K&q=85&s=046239fbe74a8e928752b97b1a8954fa)


### [​](https://docs.ollama.com/capabilities/web-search#codex) Codex


Ollama works well with OpenAI’s Codex tool.
Add the following configuration to `~/.codex/config.toml`


```
[mcp_servers.web_search]
command = "uv"
args = ["run", "path/to/web-search-mcp.py"]
env = { "OLLAMA_API_KEY" = "your_api_key_here" }
```


![Codex MCP Configuration](https://mintcdn.com/ollama-9269c548/lS1IbrlCxMxm029K/images/codex-mcp.png?fit=max&auto=format&n=lS1IbrlCxMxm029K&q=85&s=775b41bb85af7836b0a5a609de7d1f6f)


### [​](https://docs.ollama.com/capabilities/web-search#goose) Goose


Ollama can integrate with Goose via its MCP feature.
![Goose MCP Configuration 1](https://mintcdn.com/ollama-9269c548/lS1IbrlCxMxm029K/images/goose-mcp-1.png?fit=max&auto=format&n=lS1IbrlCxMxm029K&q=85&s=5fea6e0aab7865dc950470f004c549e8)
![Goose MCP Configuration 2](https://mintcdn.com/ollama-9269c548/lS1IbrlCxMxm029K/images/goose-mcp-2.png?fit=max&auto=format&n=lS1IbrlCxMxm029K&q=85&s=c69c12389f7dd60ef1c53cd10af82a7d)


### [​](https://docs.ollama.com/capabilities/web-search#other-integrations) Other integrations


Ollama can be integrated into most of the tools available either through direct integration of Ollama’s API, Python / JavaScript libraries, OpenAI compatible API, and MCP server integration. ⌘ I

---

# Streaming - Ollama

`https://docs.ollama.com/api/streaming`

Certain API endpoints stream responses by default, such as `/api/generate`. These responses are provided in the newline-delimited JSON format (i.e. the `application/x-ndjson` content type). For example:


```
{"model":"gemma4","created_at":"2025-10-26T17:15:24.097767Z","response":"That","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.109172Z","response":"'","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.121485Z","response":"s","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.132802Z","response":" a","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.143931Z","response":" fantastic","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.155176Z","response":" question","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:15:24.166576Z","response":"!","done":true, "done_reason": "stop"}
```


## [​](https://docs.ollama.com/api/streaming#disabling-streaming) Disabling streaming


Streaming can be disabled by providing `{"stream": false}` in the request body for any endpoint that support streaming. This will cause responses to be returned in the `application/json` format instead:


```
{"model":"gemma4","created_at":"2025-10-26T17:15:24.166576Z","response":"That's a fantastic question!","done":true}
```


## [​](https://docs.ollama.com/api/streaming#when-to-use-streaming-vs-non-streaming) When to use streaming vs non-streaming


**Streaming (default)**:


- Real-time response generation
- Lower perceived latency
- Better for long generations


**Non-streaming**:


- Simpler to process
- Better for short responses, or structured outputs
- Easier to handle in some applications

⌘ I

---

# Hermes Desktop - Ollama

`https://docs.ollama.com/integrations/hermes-desktop`

Hermes Desktop is a native AI assistant app by Nous Research. It provides a desktop chat interface for Hermes Agent, an AI agent that can work with models, run tools, manage projects, use memory and skills, and connect to messaging gateways.
![Hermes Desktop with Ollama](http://files.ollama.com/hermes-agent.png)


## [​](https://docs.ollama.com/integrations/hermes-desktop#quick-start) Quick start


```
ollama launch hermes-desktop
```


Ollama handles the setup flow automatically:


1. **Install** - If Hermes isn’t installed, Ollama prompts to install the Hermes command-line agent. On first desktop launch, Hermes builds its packaged desktop app.
2. **Model** - Pick a model from the selector
3. **Configure** - Ollama configures Hermes Desktop to use your selected Ollama model
4. **Launch** - Ollama opens Hermes Desktop


## [​](https://docs.ollama.com/integrations/hermes-desktop#run-directly-with-a-model) Run directly with a model


```
ollama launch hermes-desktop --model <model>
```


Run `ollama launch hermes-desktop` again to switch models later.


## [​](https://docs.ollama.com/integrations/hermes-desktop#install-hermes-desktop-directly) Install Hermes Desktop directly


On macOS and Windows, the Hermes Desktop installer is the recommended upstream installation path. It installs the desktop app and Hermes Agent together. If you prefer the command line, `ollama launch hermes-desktop` remains the explicit Ollama-managed path and uses the same Hermes configuration, sessions, skills, and memory as the CLI.
To force Hermes to rebuild its packaged desktop app:


```
ollama launch hermes-desktop -- --force-build
```

⌘ I

---

# Errors - Ollama

`https://docs.ollama.com/api/errors`

## [​](https://docs.ollama.com/api/errors#status-codes) Status codes


Endpoints return appropriate HTTP status codes based on the success or failure of the request in the HTTP status line (e.g. `HTTP/1.1 200 OK` or `HTTP/1.1 400 Bad Request`). Common status codes are:


- `200`: Success
- `400`: Bad Request (missing parameters, invalid JSON, etc.)
- `404`: Not Found (model doesn’t exist, etc.)
- `429`: Too Many Requests (e.g. when a rate limit is exceeded)
- `500`: Internal Server Error
- `502`: Bad Gateway (e.g. when a cloud model cannot be reached)


## [​](https://docs.ollama.com/api/errors#error-messages) Error messages


Errors are returned in the `application/json` format with the following structure, with the error message in the `error` property:


```
{
  "error": "the model failed to generate a response"
}
```


## [​](https://docs.ollama.com/api/errors#errors-that-occur-while-streaming) Errors that occur while streaming


If an error occurs mid-stream, the error will be returned as an object in the `application/x-ndjson` format with an `error` property. Since the response has already started, the status code of the response will not be changed.


```
{"model":"gemma4","created_at":"2025-10-26T17:21:21.196249Z","response":" Yes","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:21:21.207235Z","response":".","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:21:21.219166Z","response":"I","done":false}
{"model":"gemma4","created_at":"2025-10-26T17:21:21.231094Z","response":"can","done":false}
{"error":"an error was encountered while running the model"}
```

⌘ I

---

# DeepSeek Harness - Ollama

`https://docs.ollama.com/integrations/deepseek-harness`

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is an open-source coding agent.
DeepSeek Harness is currently a developer preview. Its upstream configuration may change between releases.


## [​](https://docs.ollama.com/integrations/deepseek-harness#setup) Setup


```
ollama launch dsh
```


Ollama installs `@deepseek-ai/dsh` if needed. To choose a model:


```
ollama launch dsh --model qwen3.8
ollama launch dsh --model deepseek-v4-flash:cloud
```


To configure without starting:


```
ollama launch dsh --config
```


## [​](https://docs.ollama.com/integrations/deepseek-harness#web-search) Web search


Web search is enabled automatically. It requires access to Ollama’s cloud and a model that supports tools. Run `ollama signin` if needed.


## [​](https://docs.ollama.com/integrations/deepseek-harness#configuration) Configuration


Ollama stores its settings in `~/.ollama/launch/dsh/settings.yaml`. These settings load last and set the model, provider, and web search connection. Repeated launches preserve other settings in this file. Ollama does not change `~/.dsh/settings.yaml`, profiles, sessions, or credentials.
Launch rejects additional `--patch` arguments. Pass other Harness arguments after `--`:


```
ollama launch dsh -- --port 3081
```


## [​](https://docs.ollama.com/integrations/deepseek-harness#manual-install) Manual install


DeepSeek Harness requires Node.js. To install it manually:


```
npm install -g @deepseek-ai/dsh@latest
```


Then run `ollama launch dsh`. On Windows, install Node.js for Windows. ⌘ I

---

# Thinking - Ollama

`https://docs.ollama.com/capabilities/thinking`

Thinking-capable models emit a `thinking` field that separates their reasoning trace from the final answer.
Use this capability to audit model steps, animate the model *thinking* in a UI, or hide the trace entirely when you only need the final response.
See the [full list of thinking models](https://ollama.com/search?c=thinking).


## [​](https://docs.ollama.com/capabilities/thinking#discover-a-model%E2%80%99s-thinking-controls) Discover a model’s thinking controls


Thinking controls vary by model. Use `/api/show` to discover the values a model supports and the value Ollama uses by default:


```
curl http://localhost:11434/api/show -d '{
  "model": "gpt-oss"
}'
```


The response includes a top-level `thinking` object:


```
{
  "thinking": {
    "values": ["low", "medium", "high"],
    "default": "medium"
  }
}
```


- `values` can contain booleans (`true` or `false`) for on/off controls. It can also contain model-defined strings for named levels.
- `default` is used when `think` is not set.
- `values: [false]` means the model does not support thinking.
- If `thinking` is omitted, the model has no thinking metadata. The model might conduct thinking based on its existing behavior.


## [​](https://docs.ollama.com/capabilities/thinking#enable-thinking-in-api-calls) Enable thinking in API calls


Set the `think` field on a chat or generate request:


- `true`: request thinking output.
- `false`: request no thinking output, if the model permits it.
- `null`: use the model default.
- A string: select a supported level from `thinking.values`. Use the exact value from `/api/show`. Numbers are not supported.


If the model resolves named levels from `/api/show` metadata, Ollama applies supported names exactly. Unsupported names use the model default.
The reasoning output and answer use separate fields. Chat returns `message.thinking` and `message.content`. Generate returns `thinking` and `response`.


- cURL
- Python
- JavaScript


```
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3",
  "messages": [{
    "role": "user",
    "content": "How many letter r are in strawberry?"
  }],
  "think": true,
  "stream": false
}'
```


```
from ollama import chat

response = chat(
  model='qwen3',
  messages=[{'role': 'user', 'content': 'How many letter r are in strawberry?'}],
  think=True,
  stream=False,
)

print('Thinking:\n', response.message.thinking)
print('Answer:\n', response.message.content)
```


```
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'deepseek-r1',
  messages: [{ role: 'user', content: 'How many letter r are in strawberry?' }],
  think: true,
  stream: false,
})

console.log('Thinking:\n', response.message.thinking)
console.log('Answer:\n', response.message.content)
```


## [​](https://docs.ollama.com/capabilities/thinking#stream-the-reasoning-trace) Stream the reasoning trace


Thinking streams interleave reasoning tokens before answer tokens. Detect the first `thinking` chunk to render a “thinking” section, then switch to the final reply once `message.content` arrives.


- Python
- JavaScript


```
from ollama import chat

stream = chat(
  model='qwen3',
  messages=[{'role': 'user', 'content': 'What is 17 × 23?'}],
  think=True,
  stream=True,
)

in_thinking = False

for chunk in stream:
  if chunk.message.thinking and not in_thinking:
    in_thinking = True
    print('Thinking:\n', end='')

  if chunk.message.thinking:
    print(chunk.message.thinking, end='')
  elif chunk.message.content:
    if in_thinking:
      print('\n\nAnswer:\n', end='')
      in_thinking = False
    print(chunk.message.content, end='')
```


```
import ollama from 'ollama'

async function main() {
  const stream = await ollama.chat({
    model: 'qwen3',
    messages: [{ role: 'user', content: 'What is 17 × 23?' }],
    think: true,
    stream: true,
  })

  let inThinking = false

  for await (const chunk of stream) {
    if (chunk.message.thinking && !inThinking) {
      inThinking = true
      process.stdout.write('Thinking:\n')
    }

    if (chunk.message.thinking) {
      process.stdout.write(chunk.message.thinking)
    } else if (chunk.message.content) {
      if (inThinking) {
        process.stdout.write('\n\nAnswer:\n')
        inThinking = false
      }
      process.stdout.write(chunk.message.content)
    }
  }
}

main()
```

⌘ I

---

# FAQ - Ollama

`https://docs.ollama.com/faq`

# FAQ

## [​](https://docs.ollama.com/faq#how-can-i-upgrade-ollama) How can I upgrade Ollama?


Ollama on macOS and Windows will automatically download updates. Click on the taskbar or menubar item and then click “Restart to update” to apply the update. Updates can also be installed by downloading the latest version [manually](https://ollama.com/download/).
On Linux, re-run the install script:


```
curl -fsSL https://ollama.com/install.sh | sh
```


## [​](https://docs.ollama.com/faq#how-can-i-view-the-logs) How can I view the logs?


Review the [Troubleshooting](https://docs.ollama.com/troubleshooting) docs for more about using logs.


## [​](https://docs.ollama.com/faq#is-my-gpu-compatible-with-ollama) Is my GPU compatible with Ollama?


Please refer to the [GPU docs](https://docs.ollama.com/gpu).


## [​](https://docs.ollama.com/faq#how-can-i-specify-the-context-window-size) How can I specify the context window size?


By default, Ollama uses a context window size of 4096 tokens.
This can be overridden with the `OLLAMA_CONTEXT_LENGTH` environment variable. For example, to set the default context window to 8K, use:


```
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```


To change this when using `ollama run`, use `/set parameter`:


```
/set parameter num_ctx 4096
```


When using the API, specify the `num_ctx` parameter:


```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "options": {
    "num_ctx": 4096
  }
}'
```


## [​](https://docs.ollama.com/faq#how-can-i-tell-if-my-model-was-loaded-onto-the-gpu) How can I tell if my model was loaded onto the GPU?


Use the `ollama ps` command to see what models are currently loaded into memory.


```
ollama ps
```


**Output**:

```
NAME        ID            SIZE    PROCESSOR   UNTIL
llama3:70b  bcfb190ca3a7  42 GB   100% GPU    4 minutes from now
```


The `Processor` column will show which memory the model was loaded into:


- `100% GPU` means the model was loaded entirely into the GPU
- `100% CPU` means the model was loaded entirely in system memory
- `48%/52% CPU/GPU` means the model was loaded partially onto both the GPU and into system memory


## [​](https://docs.ollama.com/faq#how-do-i-configure-ollama-server) How do I configure Ollama server?


Ollama server can be configured with environment variables.


### [​](https://docs.ollama.com/faq#setting-environment-variables-on-mac) Setting environment variables on Mac


If Ollama is run as a macOS application, environment variables should be set using `launchctl`:


1. For each environment variable, call `launchctl setenv`. ``` launchctl setenv OLLAMA_HOST "0.0.0.0:11434" ```
2. Restart Ollama application.


### [​](https://docs.ollama.com/faq#setting-environment-variables-on-linux) Setting environment variables on Linux


If Ollama is run as a systemd service, environment variables should be set using `systemctl`:


1. Edit the systemd service by calling `systemctl edit ollama.service`. This will open an editor.
2. For each environment variable, add a line `Environment` under section `[Service]`: ``` [Service] Environment="OLLAMA_HOST=0.0.0.0:11434" ```
3. Save and exit.
4. Reload `systemd` and restart Ollama: ``` systemctl daemon-reload systemctl restart ollama ```


### [​](https://docs.ollama.com/faq#setting-environment-variables-on-windows) Setting environment variables on Windows


On Windows, Ollama inherits your user and system environment variables.


1. First Quit Ollama by clicking on it in the task bar.
2. Start the Settings (Windows 11) or Control Panel (Windows 10) application and search for *environment variables*.
3. Click on *Edit environment variables for your account*.
4. Edit or create a new variable for your user account for `OLLAMA_HOST`, `OLLAMA_MODELS`, etc.
5. Click OK/Apply to save.
6. Start the Ollama application from the Windows Start menu.


## [​](https://docs.ollama.com/faq#how-do-i-use-ollama-behind-a-proxy) How do I use Ollama behind a proxy?


Ollama pulls models from the Internet and may require a proxy server to access the models. Use `HTTPS_PROXY` to redirect outbound requests through the proxy. Ensure the proxy certificate is installed as a system certificate. Refer to the section above for how to use environment variables on your platform.
Avoid setting `HTTP_PROXY`. Ollama does not use HTTP for model pulls, only
HTTPS. Setting `HTTP_PROXY` may interrupt client connections to the server.


### [​](https://docs.ollama.com/faq#how-do-i-use-ollama-behind-a-proxy-in-docker) How do I use Ollama behind a proxy in Docker?


The Ollama Docker container image can be configured to use a proxy by passing `-e HTTPS_PROXY=https://proxy.example.com` when starting the container.
Alternatively, the Docker daemon can be configured to use a proxy. Instructions are available for Docker Desktop on [macOS](https://docs.docker.com/desktop/settings/mac/#proxies), [Windows](https://docs.docker.com/desktop/settings/windows/#proxies), and [Linux](https://docs.docker.com/desktop/settings/linux/#proxies), and Docker [daemon with systemd](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy).
Ensure the certificate is installed as a system certificate when using HTTPS. This may require a new Docker image when using a self-signed certificate.


```
FROM ollama/ollama
COPY my-ca.pem /usr/local/share/ca-certificates/my-ca.crt
RUN update-ca-certificates
```


Build and run this image:


```
docker build -t ollama-with-ca .
docker run -d -e HTTPS_PROXY=https://my.proxy.example.com -p 11434:11434 ollama-with-ca
```


## [​](https://docs.ollama.com/faq#does-ollama-send-my-prompts-and-answers-back-to-ollama-com) Does Ollama send my prompts and answers back to ollama.com?


Ollama runs locally. We don’t see your prompts or data when you run locally. When using cloud-hosted models, we process your prompts and responses to provide the service but do not store or log that content and never train on it. We collect basic account info and limited usage metadata to provide the service that does not include prompt or response content. We don’t sell your data. You can delete your account anytime.


## [​](https://docs.ollama.com/faq#how-do-i-disable-ollama-cloud-features) How do I disable Ollama’s cloud features?


Ollama can run in local only mode by disabling Ollama’s cloud features. By turning off Ollama’s cloud features, you will lose the ability to use Ollama’s cloud models and web search.
Set `disable_ollama_cloud` in `~/.ollama/server.json`:


```
{
  "disable_ollama_cloud": true
}
```


You can also set the environment variable:


```
OLLAMA_NO_CLOUD=1
```


Restart Ollama after changing configuration. Once disabled, Ollama’s logs will show `Ollama cloud disabled: true`.


## [​](https://docs.ollama.com/faq#how-can-i-expose-ollama-on-my-network) How can I expose Ollama on my network?


Ollama binds 127.0.0.1 port 11434 by default. Change the bind address with the `OLLAMA_HOST` environment variable.
Refer to the section [above](https://docs.ollama.com/faq#how-do-i-configure-ollama-server) for how to set environment variables on your platform.


## [​](https://docs.ollama.com/faq#how-can-i-use-ollama-with-a-proxy-server) How can I use Ollama with a proxy server?


Ollama runs an HTTP server and can be exposed using a proxy server such as Nginx. To do so, configure the proxy to forward requests and optionally set required headers (if not exposing Ollama on the network). For example, with Nginx:


```
server {
    listen 80;
    server_name example.com;  # Replace with your domain or IP
    location / {
        proxy_pass http://localhost:11434;
        proxy_set_header Host localhost:11434;
    }
}
```


## [​](https://docs.ollama.com/faq#how-can-i-use-ollama-with-ngrok) How can I use Ollama with ngrok?


Ollama can be accessed using a range of tunneling apps. For example with Ngrok:


```
ngrok http 11434 --host-header="localhost:11434"
```


## [​](https://docs.ollama.com/faq#how-can-i-use-ollama-with-cloudflare-tunnel) How can I use Ollama with Cloudflare Tunnel?


To use Ollama with Cloudflare Tunnel, use the `--url` and `--http-host-header` flags:


```
cloudflared tunnel --url http://localhost:11434 --http-host-header="localhost:11434"
```


## [​](https://docs.ollama.com/faq#how-can-i-allow-additional-web-origins-to-access-ollama) How can I allow additional web origins to access Ollama?


Ollama allows cross-origin requests from `127.0.0.1` and `0.0.0.0` by default. Additional origins can be configured with `OLLAMA_ORIGINS`.
For browser extensions, you’ll need to explicitly allow the extension’s origin pattern. Set `OLLAMA_ORIGINS` to include `chrome-extension://*`, `moz-extension://*`, and `safari-web-extension://*` if you wish to allow all browser extensions access, or specific extensions as needed:


```
# Allow all Chrome, Firefox, and Safari extensions
OLLAMA_ORIGINS=chrome-extension://*,moz-extension://*,safari-web-extension://* ollama serve
```


Refer to the section [above](https://docs.ollama.com/faq#how-do-i-configure-ollama-server) for how to set environment variables on your platform.


## [​](https://docs.ollama.com/faq#where-are-models-stored) Where are models stored?


- macOS: `~/.ollama/models`
- Linux: `/usr/share/ollama/.ollama/models`
- Windows: `C:\Users\%username%\.ollama\models`


### [​](https://docs.ollama.com/faq#how-do-i-set-them-to-a-different-location) How do I set them to a different location?


If a different directory needs to be used, set the environment variable `OLLAMA_MODELS` to the chosen directory.
On Linux using the standard installer, the `ollama` user needs read and write access to the specified directory. To assign the directory to the `ollama` user run `sudo chown -R ollama:ollama <directory>`.
Refer to the section [above](https://docs.ollama.com/faq#how-do-i-configure-ollama-server) for how to set environment variables on your platform.


## [​](https://docs.ollama.com/faq#how-can-i-use-ollama-in-visual-studio-code) How can I use Ollama in Visual Studio Code?


Install the [Ollama extension](https://marketplace.visualstudio.com/items?itemName=Ollama.ollama) to use Ollama models in VS Code Chat. See the [VS Code integration guide](https://docs.ollama.com/integrations/vscode) for setup and troubleshooting.


## [​](https://docs.ollama.com/faq#how-do-i-use-ollama-with-gpu-acceleration-in-docker) How do I use Ollama with GPU acceleration in Docker?


The Ollama Docker container can be configured with GPU acceleration in Linux or Windows (with WSL2). This requires the [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). See [ollama/ollama](https://hub.docker.com/r/ollama/ollama) for more details.
GPU acceleration is not available for Docker Desktop in macOS due to the lack of GPU passthrough and emulation.


## [​](https://docs.ollama.com/faq#why-is-networking-slow-in-wsl2-on-windows-10) Why is networking slow in WSL2 on Windows 10?


This can impact both installing Ollama, as well as downloading models.
Open `Control Panel > Networking and Internet > View network status and tasks` and click on `Change adapter settings` on the left panel. Find the `vEthernet (WSL)` adapter, right click and select `Properties`.
Click on `Configure` and open the `Advanced` tab. Search through each of the properties until you find `Large Send Offload Version 2 (IPv4)` and `Large Send Offload Version 2 (IPv6)`. *Disable* both of these
properties.


## [​](https://docs.ollama.com/faq#how-can-i-preload-a-model-into-ollama-to-get-faster-response-times) How can I preload a model into Ollama to get faster response times?


If you are using the API you can preload a model by sending the Ollama server an empty request. This works with both the `/api/generate` and `/api/chat` API endpoints.
To preload the mistral model using the generate endpoint, use:


```
curl http://localhost:11434/api/generate -d '{"model": "mistral"}'
```


To use the chat completions endpoint, use:


```
curl http://localhost:11434/api/chat -d '{"model": "mistral"}'
```


To preload a model using the CLI, use the command:


```
ollama run llama3.2 ""
```


## [​](https://docs.ollama.com/faq#how-do-i-keep-a-model-loaded-in-memory-or-make-it-unload-immediately) How do I keep a model loaded in memory or make it unload immediately?


By default models are kept in memory for 5 minutes before being unloaded. This allows for quicker response times if you’re making numerous requests to the LLM. If you want to immediately unload a model from memory, use the `ollama stop` command:


```
ollama stop llama3.2
```


If you’re using the API, use the `keep_alive` parameter with the `/api/generate` and `/api/chat` endpoints to set the amount of time that a model stays in memory. The `keep_alive` parameter can be set to:


- a duration string (such as “10m” or “24h”)
- a number in seconds (such as 3600)
- any negative number which will keep the model loaded in memory (e.g. -1 or “-1m”)
- ‘0’ which will unload the model immediately after generating a response


For example, to preload a model and leave it in memory use:


```
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": -1}'
```


To unload the model and free up memory use:


```
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": 0}'
```


Alternatively, you can change the amount of time all models are loaded into memory by setting the `OLLAMA_KEEP_ALIVE` environment variable when starting the Ollama server. The `OLLAMA_KEEP_ALIVE` variable uses the same parameter types as the `keep_alive` parameter types mentioned above. Refer to the section explaining [how to configure the Ollama server](https://docs.ollama.com/faq#how-do-i-configure-ollama-server) to correctly set the environment variable.
The `keep_alive` API parameter with the `/api/generate` and `/api/chat` API endpoints will override the `OLLAMA_KEEP_ALIVE` setting.


## [​](https://docs.ollama.com/faq#how-do-i-manage-the-maximum-number-of-requests-the-ollama-server-can-queue) How do I manage the maximum number of requests the Ollama server can queue?


If too many requests are sent to the server, it will respond with a 503 error indicating the server is overloaded. You can adjust how many requests may be queued by setting `OLLAMA_MAX_QUEUE`.


## [​](https://docs.ollama.com/faq#how-does-ollama-handle-concurrent-requests) How does Ollama handle concurrent requests?


Ollama supports two levels of concurrent processing. If your system has sufficient available memory (system memory when using CPU inference, or VRAM for GPU inference) then multiple models can be loaded at the same time. For a given model, if there is sufficient available memory when the model is loaded, it is configured to allow parallel request processing.
If there is insufficient available memory to load a new model request while one or more models are already loaded, all new requests will be queued until the new model can be loaded. As prior models become idle, one or more will be unloaded to make room for the new model. Queued requests will be processed in order. When using GPU inference new models must be able to completely fit in VRAM to allow concurrent model loads.
Parallel request processing for a given model results in increasing the context size by the number of parallel requests. For example, a 2K context with 4 parallel requests will result in an 8K context and additional memory allocation.
The following server settings may be used to adjust how Ollama handles concurrent requests on most platforms:


- `OLLAMA_MAX_LOADED_MODELS` - The maximum number of models that can be loaded concurrently provided they fit in available memory. The default is 3 * the number of GPUs or 3 for CPU inference.
- `OLLAMA_NUM_PARALLEL` - The maximum number of parallel requests each model will process at the same time, default 1. Required RAM will scale by `OLLAMA_NUM_PARALLEL` * `OLLAMA_CONTEXT_LENGTH`.
- `OLLAMA_MAX_QUEUE` - The maximum number of requests Ollama will queue when busy before rejecting additional requests. The default is 512


Note: Windows with Radeon GPUs currently default to 1 model maximum due to limitations in ROCm v5.7 for available VRAM reporting. Once ROCm v6.2 is available, Windows Radeon will follow the defaults above. You may enable concurrent model loads on Radeon on Windows, but ensure you don’t load more models than will fit into your GPU’s VRAM.


## [​](https://docs.ollama.com/faq#how-does-ollama-load-models-on-multiple-gpus) How does Ollama load models on multiple GPUs?


When loading a new model, Ollama evaluates the required VRAM for the model against what is currently available. If the model will entirely fit on any single GPU, Ollama will load the model on that GPU. This typically provides the best performance as it reduces the amount of data transferring across the PCI bus during inference. If the model does not fit entirely on one GPU, then it will be spread across all the available GPUs.


## [​](https://docs.ollama.com/faq#how-can-i-enable-flash-attention) How can I enable Flash Attention?


Flash Attention is a feature of most modern models that can significantly reduce memory usage as the context size grows. Ollama uses Flash Attention automatically when the selected backend and devices support it. To force Flash Attention on, set `OLLAMA_FLASH_ATTENTION=1` when starting the Ollama server. To disable it, set `OLLAMA_FLASH_ATTENTION=0`.


## [​](https://docs.ollama.com/faq#how-can-i-set-the-quantization-type-for-the-k/v-cache) How can I set the quantization type for the K/V cache?


The K/V context cache can be quantized to significantly reduce memory usage when Flash Attention is enabled.
To use quantized K/V cache with Ollama you can set the following environment variable:


- `OLLAMA_KV_CACHE_TYPE` - The quantization type for the K/V cache. Default is `f16`.


Currently this is a global option - meaning all models will run with the
specified quantization type.
The currently available K/V cache quantization types are:


- `f16` - high precision and memory usage (default).
- `q8_0` - 8-bit quantization, uses approximately 1/2 the memory of `f16` with a very small loss in precision, this usually has no noticeable impact on the model’s quality (recommended if not using f16).
- `q4_0` - 4-bit quantization, uses approximately 1/4 the memory of `f16` with a small-medium loss in precision that may be more noticeable at higher context sizes.


How much the cache quantization impacts the model’s response quality will depend on the model and the task. Models that have a high GQA count (e.g. Qwen2) may see a larger impact on precision from quantization than models with a low GQA count.
You may need to experiment with different quantization types to find the best balance between memory usage and quality.


## [​](https://docs.ollama.com/faq#where-can-i-find-my-ollama-public-key) Where can I find my Ollama Public Key?


Your **Ollama Public Key** is the public part of the key pair that lets your local Ollama instance talk to [ollama.com](https://ollama.com).
You’ll need it to:


- Push models to Ollama
- Pull private models from Ollama to your machine
- Run models hosted in [Ollama’s cloud](https://ollama.com/cloud)


### [​](https://docs.ollama.com/faq#how-to-add-the-key) How to Add the Key


- **Sign-in via the Settings page** in the **Mac** and **Windows App**
- **Sign‑in via CLI**


```
ollama signin
```


- **Manually copy & paste** the key on the **Ollama Keys** page: [https://ollama.com/settings/keys](https://ollama.com/settings/keys)


### [​](https://docs.ollama.com/faq#where-the-ollama-public-key-lives) Where the Ollama Public Key lives


| OS | Path to `id_ed25519.pub` |
| --- | --- |
| macOS | `~/.ollama/id_ed25519.pub` |
| Linux | `/usr/share/ollama/.ollama/id_ed25519.pub` |
| Windows | `C:\Users\<username>\.ollama\id_ed25519.pub` |


Replace <username> with your actual Windows user name.


## [​](https://docs.ollama.com/faq#how-can-i-stop-ollama-from-starting-when-i-login-to-my-computer) How can I stop Ollama from starting when I login to my computer?


Ollama for Windows and macOS register as a login item during installation.  You can disable this if you prefer not to have Ollama automatically start.  Ollama will respect this setting across upgrades, unless you uninstall the application.
**Windows**


- In `Task Manager` go to the `Startup apps` tab, search for `ollama` then click `Disable`


**MacOS**


- Open `Settings` and search for “Login Items”, find the `Ollama` entry under `Allow in the Background`, then click the slider to disable.

⌘ I

---

# Generate a response - Ollama

`https://docs.ollama.com/api/generate`

# Generate a response
## Documentation Index


Generates a response for the provided prompt

POST / api / generate

cURL


Default


```
curl http://localhost:11434/api/generate -d '{
  "model": "gemma4",
  "prompt": "Why is the sky blue?"
}'
```

200

```
{
  "model": "gemma4",
  "created_at": "2025-10-17T23:14:07.414671Z",
  "response": "Hello! How can I help you today?",
  "done": true,
  "done_reason": "stop",
  "total_duration": 174560334,
  "load_duration": 101397084,
  "prompt_eval_count": 11,
  "prompt_eval_duration": 13074791,
  "eval_count": 18,
  "eval_duration": 52479709
}
```


#### Body

application/json [​](https://docs.ollama.com/api/generate#body-model) model string required

Model name

[​](https://docs.ollama.com/api/generate#body-prompt) prompt string

Text for the model to generate a response from

[​](https://docs.ollama.com/api/generate#body-suffix) suffix string

Used for fill-in-the-middle models, text that appears after the user prompt and before the model response

[​](https://docs.ollama.com/api/generate#body-images) images string[]

Base64-encoded images for models that support image input

[​](https://docs.ollama.com/api/generate#body-format-one-of-0) format string object string object

Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.

[​](https://docs.ollama.com/api/generate#body-system) system string

System prompt for the model to generate a response from

[​](https://docs.ollama.com/api/generate#body-stream) stream boolean default: true

When true, returns a stream of partial responses

[​](https://docs.ollama.com/api/generate#body-think-one-of-0) think boolean string boolean string

Controls a model's thinking output. Use `/api/show` to discover the supported values and default for the selected model. `true` requests thinking, `false` requests no thinking output, and `null` uses the model default. String values are model-defined; supported names must match `/api/show` exactly. Numbers are not supported.

[​](https://docs.ollama.com/api/generate#body-raw) raw boolean

When true, returns the raw response from the model without any prompt templating

[​](https://docs.ollama.com/api/generate#body-keep-alive-one-of-0) keep_alive string number string number

Model keep-alive duration (for example `5m` or `0` to unload immediately)

[​](https://docs.ollama.com/api/generate#body-options) options object

Runtime options that control text generation


Show child attributes

[​](https://docs.ollama.com/api/generate#body-logprobs) logprobs boolean

Whether to return log probabilities of the output tokens

[​](https://docs.ollama.com/api/generate#body-top-logprobs) top_logprobs integer

Number of most likely tokens to return at each token position when logprobs are enabled


#### Response

200 application/json

Generation responses

[​](https://docs.ollama.com/api/generate#response-model) model string

Model name

[​](https://docs.ollama.com/api/generate#response-created-at) created_at string

ISO 8601 timestamp of response creation

[​](https://docs.ollama.com/api/generate#response-response) response string

The model's generated text response

[​](https://docs.ollama.com/api/generate#response-thinking) thinking string

The model's generated thinking output

[​](https://docs.ollama.com/api/generate#response-done) done boolean

Indicates whether generation has finished

[​](https://docs.ollama.com/api/generate#response-done-reason) done_reason string

Reason the generation stopped

[​](https://docs.ollama.com/api/generate#response-total-duration) total_duration integer

Time spent generating the response in nanoseconds

[​](https://docs.ollama.com/api/generate#response-load-duration) load_duration integer

Time spent loading the model in nanoseconds

[​](https://docs.ollama.com/api/generate#response-prompt-eval-count) prompt_eval_count integer

Number of input tokens in the prompt

[​](https://docs.ollama.com/api/generate#response-prompt-eval-cached-count) prompt_eval_cached_count integer

Number of prompt tokens read from the cache

[​](https://docs.ollama.com/api/generate#response-prompt-eval-duration) prompt_eval_duration integer

Time spent evaluating uncached prompt tokens in nanoseconds

[​](https://docs.ollama.com/api/generate#response-eval-count) eval_count integer

Number of output tokens generated in the response

[​](https://docs.ollama.com/api/generate#response-eval-duration) eval_duration integer

Time spent generating tokens in nanoseconds

[​](https://docs.ollama.com/api/generate#response-logprobs) logprobs object[]

Log probability information for the generated tokens when logprobs are enabled


Show child attributes

⌘ I

cURL


Default


```
curl http://localhost:11434/api/generate -d '{
  "model": "gemma4",
  "prompt": "Why is the sky blue?"
}'
```

200

```
{
  "model": "gemma4",
  "created_at": "2025-10-17T23:14:07.414671Z",
  "response": "Hello! How can I help you today?",
  "done": true,
  "done_reason": "stop",
  "total_duration": 174560334,
  "load_duration": 101397084,
  "prompt_eval_count": 11,
  "prompt_eval_duration": 13074791,
  "eval_count": 18,
  "eval_duration": 52479709
}
```

---

# Cline CLI - Ollama

`https://docs.ollama.com/integrations/cline-cli`

Cline CLI is an autonomous coding agent for interactive terminal sessions.
![Cline CLI launched with Ollama selected as the provider](https://mintcdn.com/ollama-9269c548/R8Po5VhSMKoXhTjd/images/cline-cli.png?fit=max&auto=format&n=R8Po5VhSMKoXhTjd&q=85&s=33b886c0f0667b90aa67fd7184f9a876)


## [​](https://docs.ollama.com/integrations/cline-cli#install) Install


Install the [Cline CLI](https://docs.cline.bot/usage/cli-overview). For the IDE extension, see [Cline](https://docs.ollama.com/integrations/cline).


```
npm install -g cline
```


If Cline CLI is not installed and `npm` is available, `ollama launch cline` will prompt to install `cline@latest`.


## [​](https://docs.ollama.com/integrations/cline-cli#usage-with-ollama) Usage with Ollama


### [​](https://docs.ollama.com/integrations/cline-cli#quick-setup) Quick setup


```
ollama launch cline
```


When launched through `ollama launch cline`, Ollama sets Cline’s provider to Ollama, points it at the local Ollama endpoint, and selects the model you choose.
To configure without launching:


```
ollama launch cline --config
```


### [​](https://docs.ollama.com/integrations/cline-cli#run-directly-with-a-model) Run directly with a model


```
ollama launch cline --model qwen3.5
```


To use a cloud model:


```
ollama launch cline --model kimi-k2.6:cloud
```


### [​](https://docs.ollama.com/integrations/cline-cli#pass-a-prompt-to-cline) Pass a prompt to Cline


Arguments after `--` are passed directly to Cline:


```
ollama launch cline -- "summarize this repository"
```


To open Cline’s Kanban board:


```
ollama launch cline -- kanban
```


![Cline Kanban board opened from the CLI](https://mintcdn.com/ollama-9269c548/R8Po5VhSMKoXhTjd/images/cline-kanban.png?fit=max&auto=format&n=R8Po5VhSMKoXhTjd&q=85&s=7326c5ed2b5a40428e5e24abd05f1a24)


### [​](https://docs.ollama.com/integrations/cline-cli#manual-setup) Manual setup


To configure Cline CLI manually, first make sure Ollama is running and the model you want to use is available:


```
ollama pull qwen3.5
```


Then run Cline’s interactive auth flow:


```
cline auth
```


Select Ollama as the provider, use `http://localhost:11434` as the base URL if prompted, and choose a model such as `qwen3.5` or `kimi-k2.6:cloud`.
To check the current Cline configuration:


```
cline config
```


To start an interactive session:


```
cline
```

⌘ I

---

# Copilot CLI - Ollama

`https://docs.ollama.com/integrations/copilot-cli`

GitHub Copilot CLI is GitHub’s AI coding agent for the terminal. It can understand your codebase, make edits, run commands, and help you build software faster.
Open models can be used with Copilot CLI through Ollama, enabling you to use models such as `qwen3.5`, `glm-5.3:cloud`, `kimi-k3:cloud` See all supported models [here](https://ollama.com/search).


## [​](https://docs.ollama.com/integrations/copilot-cli#install) Install


Install [Copilot CLI](https://github.com/features/copilot/cli/):
macOS / Linux (Homebrew) npm (all platforms) macOS / Linux (script) Windows (WinGet)

```
brew install copilot-cli
```


```
npm install -g @github/copilot
```


```
curl -fsSL https://gh.io/copilot-install | bash
```


```
winget install GitHub.Copilot
```


## [​](https://docs.ollama.com/integrations/copilot-cli#usage-with-ollama) Usage with Ollama


### [​](https://docs.ollama.com/integrations/copilot-cli#quick-setup) Quick setup


```
ollama launch copilot
```


### [​](https://docs.ollama.com/integrations/copilot-cli#run-directly-with-a-model) Run directly with a model


```
ollama launch copilot --model kimi-k2.5:cloud
```


## [​](https://docs.ollama.com/integrations/copilot-cli#non-interactive-headless-mode) Non-interactive (headless) mode


Run Copilot CLI without interaction for use in Docker, CI/CD, or scripts:


```
ollama launch copilot --model kimi-k2.5:cloud --yes -- -p "how does this repository work?"
```


The `--yes` flag auto-pulls the model, skips selectors, and requires `--model` to be specified. Arguments after `--` are passed directly to Copilot CLI.


## [​](https://docs.ollama.com/integrations/copilot-cli#manual-setup) Manual setup


Copilot CLI connects to Ollama using the OpenAI-compatible API via environment variables.


1. Set the environment variables:


```
export COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1
export COPILOT_PROVIDER_API_KEY=
export COPILOT_PROVIDER_WIRE_API=responses
export COPILOT_MODEL=qwen3.5
```


1. Run Copilot CLI:


```
copilot
```


Or run with environment variables inline:


```
COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1 COPILOT_PROVIDER_API_KEY= COPILOT_PROVIDER_WIRE_API=responses COPILOT_MODEL=glm-5:cloud copilot
```


**Note:** Copilot requires a large context window. We recommend at least 64k tokens. See the [context length documentation](https://docs.ollama.com/context-length) for how to adjust context length in Ollama. ⌘ I

---

# Embeddings - Ollama

`https://docs.ollama.com/capabilities/embeddings`

Embeddings turn text into numeric vectors you can store in a vector database, search with cosine similarity, or use in RAG pipelines. The vector length depends on the model (typically 384–1024 dimensions).


## [​](https://docs.ollama.com/capabilities/embeddings#generate-embeddings) Generate embeddings


- CLI
- cURL
- Python
- JavaScript

Generate embeddings directly from the command line:

```
ollama run embeddinggemma "Hello world"
```

You can also pipe text to generate embeddings:

```
echo "Hello world" | ollama run embeddinggemma
```

Output is a JSON array.

```
curl -X POST http://localhost:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{
    "model": "embeddinggemma",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
```


```
import ollama

single = ollama.embed(
  model='embeddinggemma',
  input='The quick brown fox jumps over the lazy dog.'
)
print(len(single['embeddings'][0]))  # vector length
```


```
import ollama from 'ollama'

const single = await ollama.embed({
  model: 'embeddinggemma',
  input: 'The quick brown fox jumps over the lazy dog.',
})
console.log(single.embeddings[0].length) // vector length
```


The `/api/embed` endpoint returns L2‑normalized (unit‑length) vectors.


## [​](https://docs.ollama.com/capabilities/embeddings#generate-a-batch-of-embeddings) Generate a batch of embeddings


Pass an array of strings to `input`.


- cURL
- Python
- JavaScript


```
curl -X POST http://localhost:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{
    "model": "embeddinggemma",
    "input": [
      "First sentence",
      "Second sentence",
      "Third sentence"
    ]
  }'
```


```
import ollama

batch = ollama.embed(
  model='embeddinggemma',
  input=[
    'The quick brown fox jumps over the lazy dog.',
    'The five boxing wizards jump quickly.',
    'Jackdaws love my big sphinx of quartz.',
  ]
)
print(len(batch['embeddings']))  # number of vectors
```


```
import ollama from 'ollama'

const batch = await ollama.embed({
  model: 'embeddinggemma',
  input: [
    'The quick brown fox jumps over the lazy dog.',
    'The five boxing wizards jump quickly.',
    'Jackdaws love my big sphinx of quartz.',
  ],
})
console.log(batch.embeddings.length) // number of vectors
```


## [​](https://docs.ollama.com/capabilities/embeddings#tips) Tips


- Use cosine similarity for most semantic search use cases.
- Use the same embedding model for both indexing and querying.

⌘ I

---

# Context length - Ollama

`https://docs.ollama.com/context-length`

Context length is the maximum number of tokens that the model has access to in memory.
Ollama defaults to the following context lengths based on VRAM:

- < 24 GiB VRAM: 4k context
- 24-48 GiB VRAM: 32k context
- >= 48 GiB VRAM: 256k context


Tasks which require large context like web search, agents, and coding tools should be set to at least 64000 tokens.


## [​](https://docs.ollama.com/context-length#setting-context-length) Setting context length


Setting a larger context length will increase the amount of memory required to run a model. Ensure you have enough VRAM available to increase the context length.
Cloud models are set to their maximum context length by default.


### [​](https://docs.ollama.com/context-length#app) App


Change the slider in the Ollama app under settings to your desired context length.
![Context length in Ollama app](https://mintcdn.com/ollama-9269c548/SjntZZpXgbN5v4M5/images/ollama-settings.png?fit=max&auto=format&n=SjntZZpXgbN5v4M5&q=85&s=e8a7ccd30fd9cee5e93662db05b43dc7)


### [​](https://docs.ollama.com/context-length#cli) CLI


If editing the context length for Ollama is not possible, the context length can also be updated when serving Ollama.


```
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```


### [​](https://docs.ollama.com/context-length#check-allocated-context-length-and-model-offloading) Check allocated context length and model offloading


For best performance, use the maximum context length for a model, and avoid offloading the model to CPU. Verify the split under `PROCESSOR` using `ollama ps`.


```
ollama ps
```


```
NAME             ID              SIZE      PROCESSOR    CONTEXT    UNTIL
gemma4:latest    c6eb396dbd59    9.6 GB    100% GPU     131072     2 minutes from now
```

⌘ I