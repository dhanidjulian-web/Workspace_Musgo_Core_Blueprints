> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

Get started with the [MuleRouter](https://mulerouter.ai) API in a few simple steps.

<Steps>
  <Step title="Get an API Key">
    In the [MuleRouter Console](https://mulerouter.ai/app/api-keys), open the `API Keys` tab and click `Generate new key`.

    Store your API key securely after creation.
  </Step>

  <Step title="Use the API Key">
    Use the API key to send requests to the MuleRouter API.

    For example, use the Nano Banana Pro endpoint:

    ```bash theme={null}
      curl --request POST \
        --url https://api.mulerouter.ai/vendors/google/v1/nano-banana-pro/generation \
        --header 'Authorization: Bearer <token>' \
        --header 'Content-Type: application/json' \
        --data '{
          "prompt": "A beautiful sunset over the mountains",
          "aspect_ratio": "5:4",
          "resolution": "2K"
      }'
    ```
  </Step>

  <Step title="Get Result of a Task">
    Use the [task ID](/api-reference/tasks) to get the result of the task.

    For example, use the task ID to get the result of the task:

    ```bash theme={null}
      curl --request GET \
      --url https://api.mulerouter.ai/vendors/google/v1/nano-banana-pro/generation/f81d4fae-7dec-11d0-a765-00a0c91e6bf6 \
      --header 'Authorization: Bearer <token>' \
    ```
  </Step>
</Steps>

---
===========🔐™️®️©️🔐===========

---

### MCP

https://www.mulerouter.ai/docs/mcp


---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Introduction to the MuleRouter API

## Overview

**MuleRouter is an All In One API service for Developers.**

With MuleRouter, you can easily call APIs from multiple model providers,

**No need to register multiple accounts or manage multiple API tokens, just ONE API key is all you need.**

Whether it's a large language model, an image generation model, or an AI-powered tool, everything can be accessed and used here with ease.

Meanwhile, MuleRouter negotiates higher-tier service levels with providers through aggregated purchasing, delivering more stable and efficient service.

**Follow our [Quick Start](/api-reference/quickstart) guide to get started in 3 steps.**

## Providers

All providers are exposed under the `/vendors` path, which distinguishes services by provider.

For example, `/vendors/openai` serves OpenAI models, and `/vendors/anthropic` serves Anthropic models.

For easier discovery, this documentation groups endpoints by practical use cases. Choose the category that best fits your needs.

## Endpoints

For most providers, we offer the same endpoints as upstream to simplify integration.

For instance, `/vendors/openai/v1/chat/completions` exposes OpenAI’s `v1/chat/completions` endpoint.

### Alias

For convenience and compatibility, we provide a small number of widely used industry aliases.

For example, `https://api.mulerouter.ai/v1/chat/completions` is an alias of `https://api.mulerouter.ai/vendors/openai/v1/chat/completions`.

Currently available aliases:

| Alias                  | Source                                |
| :--------------------- | :------------------------------------ |
| `/v1/chat/completions` | `/vendors/openai/v1/chat/completions` |
| `/v1/models`           | `/vendors/openai/v1/models`           |
| `/v1/messages`         | `/vendors/anthropic/v1/messages`      |

## Authentication

All endpoints require authentication via an API key (token).

You can create API keys in MuleRouter Console. See [Quick Start](/api-reference/quickstart) for details.

Include the `Authorization` HTTP header in each request:

```
Authorization: Bearer <API Key>
```

In a cURL request, the header looks like this:

```shell lines highlight={3} theme={null}
curl https://api.mulerouter.ai/v1/chat/completions  \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Your API Token>" \
```

## Requests and responses

### Requests

For most synchronous and streaming endpoints, you can simply switch the endpoint base URL with minimal or no changes to your code or workflow.

Our request and response schemas closely follow the upstream providers.

### Responses

#### Asynchronous tasks

For longer-running jobs, we execute via an asynchronous task system. After submitting a task, you receive a task ID that you can use to query status and retrieve results.

For more details, see [Asynchronous Tasks](/api-reference/tasks).

#### Traceparent

In the response header, you will receive a `Traceparent` header, this header is used to trace the request and response.

If you encounter any issues with your request, please include the Traceparent ID when submitting a bug report to help us resolve the problem as quickly as possible.

## Error handling

Errors are reflected in the returned HTTP status code.

For example, if your request contains invalid parameters, you will receive `400 Bad Request`.

The response body includes a JSON object compliant with RFC 9457, containing a MuleRouter error code and message.

For more information, see [Error Codes](/api-reference/error-codes).


---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Codes

## HTTP Status Codes

HTTP status codes are used to indicate the status of a request.

### Success Response (200 - 299)

The following status codes indicate a successful response.

| Response Status Code | Description                                                                                                                           |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| **200 OK**           | The synchronous task executed successfully and returned the result.                                                                   |
| **201 Created**      | The task was created successfully and a new resource was created (e.g., a session).                                                   |
| **202 Accepted**     | The request has been accepted but not yet processed; it does not indicate the final outcome (e.g., creation of an asynchronous task). |
| **201 Created**      | The task was created successfully and a new resource was created (e.g., a session).                                                   |
| **202 Accepted**     | The request has been accepted but not yet processed; it does not indicate the final outcome (e.g., creation of an asynchronous task). |

### Client Error Response (400 - 499)

The following status codes indicate a client error.

| Response Status Code                  | Description                                                                                                 |
| :------------------------------------ | :---------------------------------------------------------------------------------------------------------- |
| **400 Bad Request**                   | Invalid request parameters (e.g., malformed body, incorrect fields).                                        |
| **401 Unauthorized**                  | Unauthorized (e.g., token expired or invalid).                                                              |
| **403 Forbidden**                     | Forbidden (e.g., insufficient permissions to access the resource).                                          |
| **404 Not Found**                     | The requested resource was not found (e.g., incorrect path).                                                |
| **405 Method Not Allowed**            | Method not allowed (e.g., attempting to create an async task via a synchronous endpoint).                   |
| **409 Conflict**                      | Conflict (e.g., attempting to create an asynchronous task that already exists).                             |
| **423 Locked**                        | The requested resource is locked (e.g., attempting to write to a resource that is currently being written). |
| **429 Too Many Requests**             | Too many requests (e.g., rate limit or quota exceeded).                                                     |
| **451 Unavailable For Legal Reasons** | Unavailable for legal reasons.                                                                              |

### Server Error Response (500 - 599)

The following status codes indicate a server error. You can try again later.
If error continues, please contact us for assistance.

| Response Status Code          | Description                                                        |
| :---------------------------- | :----------------------------------------------------------------- |
| **500 Internal Server Error** | Server error (e.g., an unknown error occurred on the server).      |
| **502 Bad Gateway**           | Bad gateway (e.g., an upstream service returned an error).         |
| **503 Service Unavailable**   | Service unavailable (e.g., our service is experiencing an outage). |

## MuleRouter Errors

When an asynchronous task request fails, MuleRouter will return an RFC 7807 formatted error body.

<ResponseField name="status" type="integer" required>
  HTTP Status Code. Refer to [HTTP Status Codes](#http-status-codes) for more details.
</ResponseField>

<ResponseField name="title" type="string" required>
  Short title of the error
</ResponseField>

<ResponseField name="error_code" type="integer" required>
  MuleRouter Error Code. Refer to [MuleRouter Error Codes](#mulerouter-error-codes) for more details.
</ResponseField>

<ResponseField name="instance" type="string">
  A URI reference that identifies the specific occurrence of the problem.
</ResponseField>

<ResponseField name="type" type="string">
  A URI reference that identifies the problem type.
</ResponseField>

<ResponseField name="detail" type="string">
  Description of the error
</ResponseField>

For example:

```json theme={null}
{
  "status": 400,
  "title": "Model Not Found",
  "error_code": 2000,
  "instance": "/vendors/openai/v1/chat/completions",
  "type": "https://mulerouter.ai/docs/api-reference/error-codes#2000",
  "detail": "The model does not exist."
}
```

## MuleRouter Error Codes

### 1000 - 1999

These errors indicate that the error is related to creator account.

#### 1000 Creator Not Allowed

The creator is not allowed to access the MuleRouter API.

#### 1001 Invalid or expired token

The token is invalid or expired.

#### 1002 Creator Credits Insufficient

The creator's credits are insufficient.

### 2000 - 2999

These errors indicate that the error is related to the model.

#### 2000 Model Not Found

The model does not exist.

#### 2001 Model Unavailable

The model is not supported or unavailable.

#### 2002 Model Parameter Not Supported

The model does not support the parameter.

### 3000 - 3999

These errors indicate that the error is related to the asynchronous task.

#### 3000 Task Not Found

The task does not exist.

#### 3001 Task Execution Error

The task execution failed.

#### 3002 Task Canceled or Aborted

The task was cancelled or aborted.


---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Asynchronous Tasks

All MuleRouter asynchronous tasks follow the same usage pattern:

Create a task via a `POST` request, then use `GET` requests to retrieve its latest status and result.

## Task response structure

All asynchronous task responses follow the structure below:

### Task Information Object

<ResponseField name="task_info" type="object" required>
  Task Information object

  <Expandable title="properties" defaultOpen>
    <ResponseField name="task_info.id" type="string" required>
      Task ID, `UUID` format
    </ResponseField>

    <ResponseField name="task_info.status" type="string" required>
      Task Status. Enum: `queued`, `running`, `succeeded`, `failed`
    </ResponseField>

    <ResponseField name="task_info.created_at" type="string" required>
      Task Created Timestamp, `ISO 8601` format
    </ResponseField>

    <ResponseField name="task_info.updated_at" type="string" required>
      Task Updated Timestamp, `ISO 8601` format
    </ResponseField>
  </Expandable>
</ResponseField>

### Task Result

The corresponding JSON structure is as follows:

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "pending",
    "created_at": "2025-09-16T10:00:00Z",
    "updated_at": "2025-09-16T10:00:00Z"
  },
}
```

When querying, use the task ID to fetch the execution status and result.

## Create a task

MuleRouter integrates multiple model vendors. Some requests are synchronous or streaming, while others involve longer inference cycles. To improve the developer experience, we expose these as asynchronous tasks.

Create an asynchronous task via `POST` `/vendors/dummy/v1/videos/generation`.

You will receive a response similar to the following:

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "pending",
    "created_at": "2025-09-16T10:00:00Z",
    "updated_at": "2025-09-16T10:00:00Z"
  },
  ...
}
```

## Retrieve task status and result

In the above example, the task ID is `123e4567-e89b-12d3-a456-426614174000`.

To retrieve the latest status and result for the task ID.

Use `GET` `/vendors/dummy/v1/videos/generation/123e4567-e89b-12d3-a456-426614174000`.

For example, when the task status is `succeeded`, you may receive a response like the following:

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "succeeded",
    "created_at": "2025-09-16T10:00:00Z",
    "updated_at": "2025-09-16T10:00:00Z"
  },
  "videos": [
    "https://example.com/video-749337402830284.mp4"
  ]
}
```

The exact result payload varies by endpoint, refer to the model documentation. The task info response envelope remains consistent.


---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Models
```
| Model Name                | Model ID                    |
| :------------------------ | :-------------------------- |
| Qwen3.6 Plus              | `qwen3.6-plus`              |
| Qwen3.6 Max Preview       | `qwen3.6-max-preview`       |
| Qwen3.5 Plus              | `qwen3.5-plus`              |
| Qwen3 Max                 | `qwen3-max`                 |
| Qwen3 Max Thinking        | `qwen3-max-thinking`        |
| Qwen3 Plus                | `qwen-plus`                 |
| Qwen3 Flash               | `qwen-flash`                |
| Qwen3 VL Flash            | `qwen3-vl-flash`            |
| Qwen3 VL Plus             | `qwen3-vl-plus`             |
| Qwen3 Omni Flash          | `qwen3-omni-flash`          |
| Qwen3.5 Omni Flash        | `qwen3.5-omni-flash`        |
| Qwen3.5 Omni Plus         | `qwen3.5-omni-plus`         |
| Qwen VL Max               | `qwen-vl-max`               |
| Grok 4                    | `grok-4`                    |
| Grok 4 Fast Non-Reasoning | `grok-4-fast-non-reasoning` |
| Grok 4 Fast Reasoning     | `grok-4-fast-reasoning`     |
| Grok Code Fast 1          | `grok-code-fast-1`          |
| GLM 5.1                   | `glm-5.1`                   |
```

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Chat Completion

> Creates a new chat completion for the given model and prompt.

<Note>
  This API is compatible with OpenAI's format.

  For more details, please refer to OpenAI's [official documentation](https://platform.openai.com/docs/api-reference/chat).

  Not all models support all parameters.
</Note>


## OpenAPI

````yaml /api-reference/endpoint/openai/openai.yaml POST /vendors/openai/v1/chat/completions
openapi: 3.1.0
info:
  title: OpenAI
  description: OpenAI API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/openai/v1/chat/completions:
    post:
      tags:
        - Chat
      summary: Create chat completion
      description: Creates a new chat completion for the given model and prompt.
      operationId: createChatCompletion
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateChatCompletionRequest'
            example:
              model: qwen3-max
              messages:
                - role: system
                  content: You are a helpful assistant.
                - role: user
                  content: Hello! How are you?
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateChatCompletionResponse'
              example:
                id: chatcmpl-fJ5wOo5nqnWz2Z9jkF4NK
                object: chat.completion
                created: 1715392980
                model: qwen3-max
                choices:
                  - index: 0
                    message:
                      role: assistant
                      content: Hello! How are you?
                      refusal: null
                      annotations: []
                    logprobs: null
                    finish_reason: stop
                usage:
                  prompt_tokens: 10
                  completion_tokens: 10
                  total_tokens: 20
                  prompt_tokens_details:
                    cached_tokens: 0
                    audio_tokens: 0
                  completion_tokens_details:
                    cached_tokens: 0
                    audio_tokens: 0
                    accepted_prediction_tokens: 0
                    rejected_prediction_tokens: 0
            text/event-stream:
              schema:
                $ref: '#/components/schemas/CreateChatCompletionStreamResponse'
components:
  schemas:
    CreateChatCompletionRequest:
      allOf:
        - $ref: '#/components/schemas/CreateModelResponseProperties'
        - type: object
          properties:
            messages:
              description: >
                A list of messages comprising the conversation so far. Depending
                on the

                model you use, different message types (modalities) are

                supported, like text,

                images, and audio.
              type: array
              minItems: 1
              items:
                $ref: '#/components/schemas/ChatCompletionRequestMessage'
            model:
              $ref: '#/components/schemas/ModelIdsShared'
              description: >
                Model ID used to generate the response, like `qwen3-max` or
                `gpt-5`. Mulerouter

                offers a wide range of models with different capabilities,
                performance

                characteristics, and price points. 

                to browse and compare available models.
            modalities:
              $ref: '#/components/schemas/ResponseModalities'
            verbosity:
              $ref: '#/components/schemas/Verbosity'
            reasoning_effort:
              $ref: '#/components/schemas/ReasoningEffort'
            max_completion_tokens:
              description: >
                An upper bound for the number of tokens that can be generated
                for a completion, including visible output tokens and reasoning
                tokens.
              type: integer
              nullable: true
            frequency_penalty:
              type: number
              default: 0
              minimum: -2
              maximum: 2
              nullable: true
              description: >
                Number between -2.0 and 2.0. Positive values penalize new tokens
                based on

                their existing frequency in the text so far, decreasing the
                model's

                likelihood to repeat the same line verbatim.
            presence_penalty:
              type: number
              default: 0
              minimum: -2
              maximum: 2
              nullable: true
              description: >
                Number between -2.0 and 2.0. Positive values penalize new tokens
                based on

                whether they appear in the text so far, increasing the model's
                likelihood

                to talk about new topics.
            web_search_options:
              type: object
              title: Web search
              description: >
                This tool searches the web for relevant results to use in a
                response.
              properties:
                user_location:
                  type: object
                  nullable: true
                  required:
                    - type
                    - approximate
                  description: |
                    Approximate location parameters for the search.
                  properties:
                    type:
                      type: string
                      description: >
                        The type of location approximation. Always
                        `approximate`.
                      enum:
                        - approximate
                      x-stainless-const: true
                    approximate:
                      $ref: '#/components/schemas/WebSearchLocation'
                search_context_size:
                  $ref: '#/components/schemas/WebSearchContextSize'
            top_logprobs:
              description: >
                An integer between 0 and 20 specifying the number of most likely
                tokens to

                return at each token position, each with an associated log
                probability.

                `logprobs` must be set to `true` if this parameter is used.
              type: integer
              minimum: 0
              maximum: 20
              nullable: true
            response_format:
              description: >
                An object specifying the format that the model must output.


                Setting to `{ "type": "json_schema", "json_schema": {...} }`
                enables

                Structured Outputs which ensures the model will match your
                supplied JSON

                schema. 


                Setting to `{ "type": "json_object" }` enables the older JSON
                mode, which

                ensures the message the model generates is valid JSON. Using
                `json_schema`

                is preferred for models that support it.
              anyOf:
                - $ref: '#/components/schemas/ResponseFormatText'
                - $ref: '#/components/schemas/ResponseFormatJsonSchema'
                - $ref: '#/components/schemas/ResponseFormatJsonObject'
            audio:
              type: object
              nullable: true
              description: >
                Parameters for audio output. Required when audio output is
                requested with

                `modalities: ["audio"]`. 
              required:
                - voice
                - format
              properties:
                voice:
                  $ref: '#/components/schemas/VoiceIdsShared'
                  description: >
                    The voice the model uses to respond. Supported voices are

                    `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`,
                    `onyx`, `sage`, and `shimmer`.
                format:
                  type: string
                  enum:
                    - wav
                    - aac
                    - mp3
                    - flac
                    - opus
                    - pcm16
                  description: >
                    Specifies the output audio format. Must be one of `wav`,
                    `mp3`, `flac`,

                    `opus`, or `pcm16`.
            store:
              type: boolean
              default: false
              nullable: true
              description: >
                Whether or not to store the output of this chat completion
                request for

                use in our model distillation or

                evals products.


                Supports text and image inputs. Note: image inputs over 8MB will
                be dropped.
            stream:
              description: >
                If set to true, the model response data will be streamed to the
                client

                as it is generated using [server-sent
                events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              type: boolean
              nullable: true
              default: false
            stop:
              $ref: '#/components/schemas/StopConfiguration'
            logit_bias:
              type: object
              x-oaiTypeLabel: map
              default: null
              nullable: true
              additionalProperties:
                type: integer
              description: >
                Modify the likelihood of specified tokens appearing in the
                completion.


                Accepts a JSON object that maps tokens (specified by their token
                ID in the

                tokenizer) to an associated bias value from -100 to 100.
                Mathematically,

                the bias is added to the logits generated by the model prior to
                sampling.

                The exact effect will vary per model, but values between -1 and
                1 should

                decrease or increase likelihood of selection; values like -100
                or 100

                should result in a ban or exclusive selection of the relevant
                token.
            logprobs:
              description: >
                Whether to return log probabilities of the output tokens or not.
                If true,

                returns the log probabilities of each output token returned in
                the

                `content` of `message`.
              type: boolean
              default: false
              nullable: true
            max_tokens:
              description: >
                The maximum number of tokens that can be generated in the

                chat completion. This value can be used to control

                costs for text generated via API.


                This value is now deprecated in favor of
                `max_completion_tokens`, and is

                not compatible with o-series models.
              type: integer
              nullable: true
              deprecated: true
            'n':
              type: integer
              minimum: 1
              maximum: 128
              default: 1
              example: 1
              nullable: true
              description: >-
                How many chat completion choices to generate for each input
                message. Note that you will be charged based on the number of
                generated tokens across all of the choices. Keep `n` as `1` to
                minimize costs.
            prediction:
              nullable: true
              description: >
                Configuration for a Predicted Output

                which can greatly improve response times when large parts of the
                model

                response are known ahead of time. This is most common when you
                are

                regenerating a file with only minor changes to most of the
                content.
              anyOf:
                - $ref: '#/components/schemas/PredictionContent'
              discriminator:
                propertyName: type
            seed:
              type: integer
              minimum: -9223372036854776000
              maximum: 9223372036854776000
              nullable: true
              deprecated: true
              description: >
                This feature is in Beta.

                If specified, our system will make a best effort to sample
                deterministically, such that repeated requests with the same
                `seed` and parameters should return the same result.

                Determinism is not guaranteed, and you should refer to the
                `system_fingerprint` response parameter to monitor changes in
                the backend.
              x-oaiMeta:
                beta: true
            stream_options:
              $ref: '#/components/schemas/ChatCompletionStreamOptions'
            tools:
              type: array
              description: |
                A list of tools the model may call. You can provide either
                custom tools or
                function tools.
              items:
                anyOf:
                  - $ref: '#/components/schemas/ChatCompletionTool'
                  - $ref: '#/components/schemas/CustomToolChatCompletions'
                x-stainless-naming:
                  python:
                    model_name: chat_completion_tool_union
                    param_model_name: chat_completion_tool_union_param
                discriminator:
                  propertyName: type
                x-stainless-go-variant-constructor:
                  naming: chat_completion_{variant}_tool
            tool_choice:
              $ref: '#/components/schemas/ChatCompletionToolChoiceOption'
            parallel_tool_calls:
              $ref: '#/components/schemas/ParallelToolCalls'
            function_call:
              deprecated: true
              description: >
                Deprecated in favor of `tool_choice`.


                Controls which (if any) function is called by the model.


                `none` means the model will not call a function and instead
                generates a

                message.


                `auto` means the model can pick between generating a message or
                calling a

                function.


                Specifying a particular function via `{"name": "my_function"}`
                forces the

                model to call that function.


                `none` is the default when no functions are present. `auto` is
                the default

                if functions are present.
              anyOf:
                - type: string
                  description: >
                    `none` means the model will not call a function and instead
                    generates a message. `auto` means the model can pick between
                    generating a message or calling a function.
                  enum:
                    - none
                    - auto
                  title: function call mode
                - $ref: '#/components/schemas/ChatCompletionFunctionCallOption'
            functions:
              deprecated: true
              description: |
                Deprecated in favor of `tools`.

                A list of functions the model may generate JSON inputs for.
              type: array
              minItems: 1
              maxItems: 128
              items:
                $ref: '#/components/schemas/ChatCompletionFunctions'
          required:
            - model
            - messages
    CreateChatCompletionResponse:
      type: object
      description: >-
        Represents a chat completion response returned by model, based on the
        provided input.
      properties:
        id:
          type: string
          description: A unique identifier for the chat completion.
        choices:
          type: array
          description: >-
            A list of chat completion choices. Can be more than one if `n` is
            greater than 1.
          items:
            type: object
            required:
              - finish_reason
              - index
              - message
              - logprobs
            properties:
              finish_reason:
                type: string
                description: >
                  The reason the model stopped generating tokens. This will be
                  `stop` if the model hit a natural stop point or a provided
                  stop sequence,

                  `length` if the maximum number of tokens specified in the
                  request was reached,

                  `content_filter` if content was omitted due to a flag from our
                  content filters,

                  `tool_calls` if the model called a tool, or `function_call`
                  (deprecated) if the model called a function.
                enum:
                  - stop
                  - length
                  - tool_calls
                  - content_filter
                  - function_call
              index:
                type: integer
                description: The index of the choice in the list of choices.
              message:
                $ref: '#/components/schemas/ChatCompletionResponseMessage'
              logprobs:
                description: Log probability information for the choice.
                type: object
                nullable: true
                properties:
                  content:
                    description: >-
                      A list of message content tokens with log probability
                      information.
                    type: array
                    items:
                      $ref: '#/components/schemas/ChatCompletionTokenLogprob'
                    nullable: true
                  refusal:
                    description: >-
                      A list of message refusal tokens with log probability
                      information.
                    type: array
                    items:
                      $ref: '#/components/schemas/ChatCompletionTokenLogprob'
                    nullable: true
                required:
                  - content
                  - refusal
        created:
          type: integer
          description: >-
            The Unix timestamp (in seconds) of when the chat completion was
            created.
        model:
          type: string
          description: The model used for the chat completion.
        service_tier:
          $ref: '#/components/schemas/ServiceTier'
        system_fingerprint:
          type: string
          deprecated: true
          description: >
            This fingerprint represents the backend configuration that the model
            runs with.


            Can be used in conjunction with the `seed` request parameter to
            understand when backend changes have been made that might impact
            determinism.
        object:
          type: string
          description: The object type, which is always `chat.completion`.
          enum:
            - chat.completion
          x-stainless-const: true
        usage:
          $ref: '#/components/schemas/CompletionUsage'
      required:
        - choices
        - created
        - id
        - model
        - object
      x-oaiMeta:
        name: The chat completion object
        group: chat
        example: |
          {
            "id": "chatcmpl-B9MHDbslfkBeAs8l4bebGdFOJ6PeG",
            "object": "chat.completion",
            "created": 1741570283,
            "model": "gpt-4o-2024-08-06",
            "choices": [
              {
                "index": 0,
                "message": {
                  "role": "assistant",
                  "content": "The image shows a wooden boardwalk path running through a lush green field or meadow. The sky is bright blue with some scattered clouds, giving the scene a serene and peaceful atmosphere. Trees and shrubs are visible in the background.",
                  "refusal": null,
                  "annotations": []
                },
                "logprobs": null,
                "finish_reason": "stop"
              }
            ],
            "usage": {
              "prompt_tokens": 1117,
              "completion_tokens": 46,
              "total_tokens": 1163,
              "prompt_tokens_details": {
                "cached_tokens": 0,
                "audio_tokens": 0
              },
              "completion_tokens_details": {
                "reasoning_tokens": 0,
                "audio_tokens": 0,
                "accepted_prediction_tokens": 0,
                "rejected_prediction_tokens": 0
              }
            },
            "service_tier": "default",
            "system_fingerprint": "fp_fc9f1d7035"
          }
    CreateChatCompletionStreamResponse:
      type: object
      description: |
        Represents a streamed chunk of a chat completion response returned
        by the model, based on the provided input. 
      properties:
        id:
          type: string
          description: >-
            A unique identifier for the chat completion. Each chunk has the same
            ID.
        choices:
          type: array
          description: >
            A list of chat completion choices. Can contain more than one
            elements if `n` is greater than 1. Can also be empty for the

            last chunk if you set `stream_options: {"include_usage": true}`.
          items:
            type: object
            required:
              - delta
              - finish_reason
              - index
            properties:
              delta:
                $ref: '#/components/schemas/ChatCompletionStreamResponseDelta'
              logprobs:
                description: Log probability information for the choice.
                type: object
                nullable: true
                properties:
                  content:
                    description: >-
                      A list of message content tokens with log probability
                      information.
                    type: array
                    items:
                      $ref: '#/components/schemas/ChatCompletionTokenLogprob'
                    nullable: true
                  refusal:
                    description: >-
                      A list of message refusal tokens with log probability
                      information.
                    type: array
                    items:
                      $ref: '#/components/schemas/ChatCompletionTokenLogprob'
                    nullable: true
                required:
                  - content
                  - refusal
              finish_reason:
                type: string
                description: >
                  The reason the model stopped generating tokens. This will be
                  `stop` if the model hit a natural stop point or a provided
                  stop sequence,

                  `length` if the maximum number of tokens specified in the
                  request was reached,

                  `content_filter` if content was omitted due to a flag from our
                  content filters,

                  `tool_calls` if the model called a tool, or `function_call`
                  (deprecated) if the model called a function.
                enum:
                  - stop
                  - length
                  - tool_calls
                  - content_filter
                  - function_call
                nullable: true
              index:
                type: integer
                description: The index of the choice in the list of choices.
        created:
          type: integer
          description: >-
            The Unix timestamp (in seconds) of when the chat completion was
            created. Each chunk has the same timestamp.
        model:
          type: string
          description: The model to generate the completion.
        service_tier:
          $ref: '#/components/schemas/ServiceTier'
        system_fingerprint:
          type: string
          deprecated: true
          description: >
            This fingerprint represents the backend configuration that the model
            runs with.

            Can be used in conjunction with the `seed` request parameter to
            understand when backend changes have been made that might impact
            determinism.
        object:
          type: string
          description: The object type, which is always `chat.completion.chunk`.
          enum:
            - chat.completion.chunk
          x-stainless-const: true
        usage:
          $ref: '#/components/schemas/CompletionUsage'
          nullable: true
          description: >
            An optional field that will only be present when you set

            `stream_options: {"include_usage": true}` in your request. When
            present, it

            contains a null value **except for the last chunk** which contains
            the

            token usage statistics for the entire request.


            **NOTE:** If the stream is interrupted or cancelled, you may not

            receive the final usage chunk which contains the total token usage
            for

            the request.
      required:
        - choices
        - created
        - id
        - model
        - object
      x-oaiMeta:
        name: The chat completion chunk object
        group: chat
        example: >
          {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini",
          "system_fingerprint": "fp_44709d6fcb",
          "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}


          {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini",
          "system_fingerprint": "fp_44709d6fcb",
          "choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}


          ....


          {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini",
          "system_fingerprint": "fp_44709d6fcb",
          "choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}
    CreateModelResponseProperties:
      allOf:
        - $ref: '#/components/schemas/ModelResponseProperties'
        - type: object
          properties:
            top_logprobs:
              description: >
                An integer between 0 and 20 specifying the number of most likely
                tokens to

                return at each token position, each with an associated log
                probability.
              type: integer
              minimum: 0
              maximum: 20
    ChatCompletionRequestMessage:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionRequestDeveloperMessage'
        - $ref: '#/components/schemas/ChatCompletionRequestSystemMessage'
        - $ref: '#/components/schemas/ChatCompletionRequestUserMessage'
        - $ref: '#/components/schemas/ChatCompletionRequestAssistantMessage'
        - $ref: '#/components/schemas/ChatCompletionRequestToolMessage'
        - $ref: '#/components/schemas/ChatCompletionRequestFunctionMessage'
      discriminator:
        propertyName: role
    ModelIdsShared:
      anyOf:
        - type: string
    ResponseModalities:
      type: array
      nullable: true
      description: |
        Output types that you would like the model to generate.
        Most models are capable of generating text, which is the default:

        `["text"]`

        The `gpt-4o-audio-preview` model can also be used to 
        generate audio. To request that this model generate 
        both text and audio responses, you can use:

        `["text", "audio"]`
      items:
        type: string
        enum:
          - text
          - audio
    Verbosity:
      type: string
      enum:
        - low
        - medium
        - high
      default: medium
      nullable: true
      description: >
        Constrains the verbosity of the model's response. Lower values will
        result in

        more concise responses, while higher values will result in more verbose
        responses.

        Currently supported values are `low`, `medium`, and `high`.
    ReasoningEffort:
      type: string
      enum:
        - minimal
        - low
        - medium
        - high
      default: medium
      nullable: true
      description: >
        Constrains effort on reasoning for 

        reasoning models.

        Currently supported values are `minimal`, `low`, `medium`, and `high`.
        Reducing

        reasoning effort can result in faster responses and fewer tokens used

        on reasoning in a response.
    WebSearchLocation:
      type: object
      title: Web search location
      description: Approximate location parameters for the search.
      properties:
        country:
          type: string
          description: |
            The two-letter 
            ISO country code of the user,
            e.g. `US`.
        region:
          type: string
          description: |
            Free text input for the region of the user, e.g. `California`.
        city:
          type: string
          description: |
            Free text input for the city of the user, e.g. `San Francisco`.
        timezone:
          type: string
          description: |
            The IANA timezone 
            of the user, e.g. `America/Los_Angeles`.
    WebSearchContextSize:
      type: string
      description: >
        High level guidance for the amount of context window space to use for
        the 

        search. One of `low`, `medium`, or `high`. `medium` is the default.
      enum:
        - low
        - medium
        - high
      default: medium
    ResponseFormatText:
      type: object
      title: Text
      description: |
        Default response format. Used to generate text responses.
      properties:
        type:
          type: string
          description: The type of response format being defined. Always `text`.
          enum:
            - text
          x-stainless-const: true
      required:
        - type
    ResponseFormatJsonSchema:
      type: object
      title: JSON schema
      description: |
        JSON Schema response format. Used to generate structured JSON responses.
      properties:
        type:
          type: string
          description: The type of response format being defined. Always `json_schema`.
          enum:
            - json_schema
          x-stainless-const: true
        json_schema:
          type: object
          title: JSON schema
          description: |
            Structured Outputs configuration options, including a JSON Schema.
          properties:
            description:
              type: string
              description: >
                A description of what the response format is for, used by the
                model to

                determine how to respond in the format.
            name:
              type: string
              description: >
                The name of the response format. Must be a-z, A-Z, 0-9, or
                contain

                underscores and dashes, with a maximum length of 64.
            schema:
              $ref: '#/components/schemas/ResponseFormatJsonSchemaSchema'
            strict:
              type: boolean
              nullable: true
              default: false
              description: >
                Whether to enable strict schema adherence when generating the
                output.

                If set to true, the model will always follow the exact schema
                defined

                in the `schema` field. Only a subset of JSON Schema is supported
                when

                `strict` is `true`. 
          required:
            - name
      required:
        - type
        - json_schema
    ResponseFormatJsonObject:
      type: object
      title: JSON object
      description: >
        JSON object response format. An older method of generating JSON
        responses.

        Using `json_schema` is recommended for models that support it. Note that
        the

        model will not generate JSON without a system or user message
        instructing it

        to do so.
      properties:
        type:
          type: string
          description: The type of response format being defined. Always `json_object`.
          enum:
            - json_object
          x-stainless-const: true
      required:
        - type
    VoiceIdsShared:
      example: ash
      anyOf:
        - type: string
        - type: string
          enum:
            - alloy
            - ash
            - ballad
            - coral
            - echo
            - sage
            - shimmer
            - verse
            - marin
            - cedar
    StopConfiguration:
      description: |
        Not supported with latest reasoning models `o3` and `o4-mini`.

        Up to 4 sequences where the API will stop generating further tokens. The
        returned text will not contain the stop sequence.
      nullable: true
      anyOf:
        - type: string
          default: <|endoftext|>
          example: |+

          nullable: true
        - type: array
          minItems: 1
          maxItems: 4
          items:
            type: string
            example: '["\n"]'
    PredictionContent:
      type: object
      title: Static Content
      description: >
        Static predicted output content, such as the content of a text file that
        is

        being regenerated.
      required:
        - type
        - content
      properties:
        type:
          type: string
          enum:
            - content
          description: |
            The type of the predicted content you want to provide. This type is
            currently always `content`.
          x-stainless-const: true
        content:
          description: >
            The content that should be matched when generating a model response.

            If generated tokens would match this content, the entire model
            response

            can be returned much more quickly.
          anyOf:
            - type: string
              title: Text content
              description: |
                The content used for a Predicted Output. This is often the
                text of a file you are regenerating with minor changes.
            - type: array
              description: >-
                An array of content parts with a defined type. Supported options
                differ based on the model being used to generate the response.
                Can contain text inputs.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestMessageContentPartText
              minItems: 1
    ChatCompletionStreamOptions:
      description: >
        Options for streaming response. Only set this when you set `stream:
        true`.
      type: object
      nullable: true
      default: null
      properties:
        include_usage:
          type: boolean
          description: >
            If set, an additional chunk will be streamed before the `data:
            [DONE]`

            message. The `usage` field on this chunk shows the token usage
            statistics

            for the entire request, and the `choices` field will always be an
            empty

            array.


            All other chunks will also include a `usage` field, but with a null

            value. **NOTE:** If the stream is interrupted, you may not receive
            the

            final usage chunk which contains the total token usage for the
            request.
        include_obfuscation:
          type: boolean
          description: >
            When true, stream obfuscation will be enabled. Stream obfuscation
            adds

            random characters to an `obfuscation` field on streaming delta
            events to

            normalize payload sizes as a mitigation to certain side-channel
            attacks.

            These obfuscation fields are included by default, but add a small
            amount

            of overhead to the data stream. You can set `include_obfuscation` to

            false to optimize for bandwidth if you trust the network links
            between

            your application and the OpenAI API.
    ChatCompletionTool:
      type: object
      title: Function tool
      description: |
        A function tool that can be used to generate a response.
      properties:
        type:
          type: string
          enum:
            - function
          description: The type of the tool. Currently, only `function` is supported.
          x-stainless-const: true
        function:
          $ref: '#/components/schemas/FunctionObject'
      required:
        - type
        - function
    CustomToolChatCompletions:
      type: object
      title: Custom tool
      description: |
        A custom tool that processes input using a specified format.
      properties:
        type:
          type: string
          enum:
            - custom
          description: The type of the custom tool. Always `custom`.
          x-stainless-const: true
        custom:
          type: object
          title: Custom tool properties
          description: |
            Properties of the custom tool.
          properties:
            name:
              type: string
              description: The name of the custom tool, used to identify it in tool calls.
            description:
              type: string
              description: >
                Optional description of the custom tool, used to provide more
                context.
            format:
              description: >
                The input format for the custom tool. Default is unconstrained
                text.
              anyOf:
                - type: object
                  title: Text format
                  description: Unconstrained free-form text.
                  properties:
                    type:
                      type: string
                      enum:
                        - text
                      description: Unconstrained text format. Always `text`.
                      x-stainless-const: true
                  required:
                    - type
                  additionalProperties: false
                - type: object
                  title: Grammar format
                  description: A grammar defined by the user.
                  properties:
                    type:
                      type: string
                      enum:
                        - grammar
                      description: Grammar format. Always `grammar`.
                      x-stainless-const: true
                    grammar:
                      type: object
                      title: Grammar format
                      description: Your chosen grammar.
                      properties:
                        definition:
                          type: string
                          description: The grammar definition.
                        syntax:
                          type: string
                          description: >-
                            The syntax of the grammar definition. One of `lark`
                            or `regex`.
                          enum:
                            - lark
                            - regex
                      required:
                        - definition
                        - syntax
                  required:
                    - type
                    - grammar
                  additionalProperties: false
              discriminator:
                propertyName: type
          required:
            - name
      required:
        - type
        - custom
    ChatCompletionToolChoiceOption:
      description: >
        Controls which (if any) tool is called by the model.

        `none` means the model will not call any tool and instead generates a
        message.

        `auto` means the model can pick between generating a message or calling
        one or more tools.

        `required` means the model must call one or more tools.

        Specifying a particular tool via `{"type": "function", "function":
        {"name": "my_function"}}` forces the model to call that tool.


        `none` is the default when no tools are present. `auto` is the default
        if tools are present.
      anyOf:
        - type: string
          title: Auto
          description: >
            `none` means the model will not call any tool and instead generates
            a message. `auto` means the model can pick between generating a
            message or calling one or more tools. `required` means the model
            must call one or more tools.
          enum:
            - none
            - auto
            - required
        - $ref: '#/components/schemas/ChatCompletionAllowedToolsChoice'
        - $ref: '#/components/schemas/ChatCompletionNamedToolChoice'
        - $ref: '#/components/schemas/ChatCompletionNamedToolChoiceCustom'
      x-stainless-go-variant-constructor:
        naming: tool_choice_option_{variant}
    ParallelToolCalls:
      description: Whether to enable parallel function calling during tool use.
      type: boolean
      default: true
    ChatCompletionFunctionCallOption:
      type: object
      description: >
        Specifying a particular function via `{"name": "my_function"}` forces
        the model to call that function.
      properties:
        name:
          type: string
          description: The name of the function to call.
      required:
        - name
      x-stainless-variantName: function_call_option
    ChatCompletionFunctions:
      type: object
      deprecated: true
      properties:
        description:
          type: string
          description: >-
            A description of what the function does, used by the model to choose
            when and how to call the function.
        name:
          type: string
          description: >-
            The name of the function to be called. Must be a-z, A-Z, 0-9, or
            contain underscores and dashes, with a maximum length of 64.
        parameters:
          $ref: '#/components/schemas/FunctionParameters'
      required:
        - name
    ChatCompletionResponseMessage:
      type: object
      description: A chat completion message generated by the model.
      properties:
        content:
          type: string
          description: The contents of the message.
          nullable: true
        refusal:
          type: string
          description: The refusal message generated by the model.
          nullable: true
        tool_calls:
          $ref: '#/components/schemas/ChatCompletionMessageToolCalls'
        annotations:
          type: array
          description: |
            Annotations for the message, when applicable, as when using the
            web search tool.
          items:
            type: object
            description: |
              A URL citation when using web search.
            required:
              - type
              - url_citation
            properties:
              type:
                type: string
                description: The type of the URL citation. Always `url_citation`.
                enum:
                  - url_citation
                x-stainless-const: true
              url_citation:
                type: object
                description: A URL citation when using web search.
                required:
                  - end_index
                  - start_index
                  - url
                  - title
                properties:
                  end_index:
                    type: integer
                    description: >-
                      The index of the last character of the URL citation in the
                      message.
                  start_index:
                    type: integer
                    description: >-
                      The index of the first character of the URL citation in
                      the message.
                  url:
                    type: string
                    description: The URL of the web resource.
                  title:
                    type: string
                    description: The title of the web resource.
        role:
          type: string
          enum:
            - assistant
          description: The role of the author of this message.
          x-stainless-const: true
        function_call:
          type: object
          deprecated: true
          description: >-
            Deprecated and replaced by `tool_calls`. The name and arguments of a
            function that should be called, as generated by the model.
          properties:
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
            name:
              type: string
              description: The name of the function to call.
          required:
            - name
            - arguments
        audio:
          type: object
          nullable: true
          description: |
            If the audio output modality is requested, this object contains data
            about the audio response from the model. 
          required:
            - id
            - expires_at
            - data
            - transcript
          properties:
            id:
              type: string
              description: Unique identifier for this audio response.
            expires_at:
              type: integer
              description: >
                The Unix timestamp (in seconds) for when this audio response
                will

                no longer be accessible on the server for use in multi-turn

                conversations.
            data:
              type: string
              description: |
                Base64 encoded audio bytes generated by the model, in the format
                specified in the request.
            transcript:
              type: string
              description: Transcript of the audio generated by the model.
      required:
        - role
        - content
        - refusal
    ChatCompletionTokenLogprob:
      type: object
      properties:
        token:
          description: The token.
          type: string
        logprob:
          description: >-
            The log probability of this token, if it is within the top 20 most
            likely tokens. Otherwise, the value `-9999.0` is used to signify
            that the token is very unlikely.
          type: number
        bytes:
          description: >-
            A list of integers representing the UTF-8 bytes representation of
            the token. Useful in instances where characters are represented by
            multiple tokens and their byte representations must be combined to
            generate the correct text representation. Can be `null` if there is
            no bytes representation for the token.
          type: array
          items:
            type: integer
          nullable: true
        top_logprobs:
          description: >-
            List of the most likely tokens and their log probability, at this
            token position. In rare cases, there may be fewer than the number of
            requested `top_logprobs` returned.
          type: array
          items:
            type: object
            properties:
              token:
                description: The token.
                type: string
              logprob:
                description: >-
                  The log probability of this token, if it is within the top 20
                  most likely tokens. Otherwise, the value `-9999.0` is used to
                  signify that the token is very unlikely.
                type: number
              bytes:
                description: >-
                  A list of integers representing the UTF-8 bytes representation
                  of the token. Useful in instances where characters are
                  represented by multiple tokens and their byte representations
                  must be combined to generate the correct text representation.
                  Can be `null` if there is no bytes representation for the
                  token.
                type: array
                items:
                  type: integer
                nullable: true
            required:
              - token
              - logprob
              - bytes
      required:
        - token
        - logprob
        - bytes
        - top_logprobs
    ServiceTier:
      type: string
      description: |
        Specifies the processing type used for serving the request.
          - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
          - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
          - If set to 'flex' or 'priority', then the request will be processed with the corresponding service tier.
          - When not set, the default behavior is 'auto'.

          When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
      enum:
        - auto
        - default
        - flex
        - scale
        - priority
      nullable: true
      default: auto
    CompletionUsage:
      type: object
      description: Usage statistics for the completion request.
      properties:
        completion_tokens:
          type: integer
          default: 0
          description: Number of tokens in the generated completion.
        prompt_tokens:
          type: integer
          default: 0
          description: Number of tokens in the prompt.
        total_tokens:
          type: integer
          default: 0
          description: Total number of tokens used in the request (prompt + completion).
        completion_tokens_details:
          type: object
          description: Breakdown of tokens used in a completion.
          properties:
            accepted_prediction_tokens:
              type: integer
              default: 0
              description: |
                When using Predicted Outputs, the number of tokens in the
                prediction that appeared in the completion.
            audio_tokens:
              type: integer
              default: 0
              description: Audio input tokens generated by the model.
            reasoning_tokens:
              type: integer
              default: 0
              description: Tokens generated by the model for reasoning.
            rejected_prediction_tokens:
              type: integer
              default: 0
              description: >
                When using Predicted Outputs, the number of tokens in the

                prediction that did not appear in the completion. However, like

                reasoning tokens, these tokens are still counted in the total

                completion tokens for purposes of billing, output, and context
                window

                limits.
        prompt_tokens_details:
          type: object
          description: Breakdown of tokens used in the prompt.
          properties:
            audio_tokens:
              type: integer
              default: 0
              description: Audio input tokens present in the prompt.
            cached_tokens:
              type: integer
              default: 0
              description: Cached tokens present in the prompt.
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
    ChatCompletionStreamResponseDelta:
      type: object
      description: A chat completion delta generated by streamed model responses.
      properties:
        content:
          type: string
          description: The contents of the chunk message.
          nullable: true
        function_call:
          deprecated: true
          type: object
          description: >-
            Deprecated and replaced by `tool_calls`. The name and arguments of a
            function that should be called, as generated by the model.
          properties:
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
            name:
              type: string
              description: The name of the function to call.
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ChatCompletionMessageToolCallChunk'
        role:
          type: string
          enum:
            - developer
            - system
            - user
            - assistant
            - tool
          description: The role of the author of this message.
        refusal:
          type: string
          description: The refusal message generated by the model.
          nullable: true
    ModelResponseProperties:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/Metadata'
        top_logprobs:
          description: >
            An integer between 0 and 20 specifying the number of most likely
            tokens to

            return at each token position, each with an associated log
            probability.
          type: integer
          minimum: 0
          maximum: 20
          nullable: true
        temperature:
          type: number
          minimum: 0
          maximum: 2
          default: 1
          example: 1
          nullable: true
          description: >
            What sampling temperature to use, between 0 and 2. Higher values
            like 0.8 will make the output more random, while lower values like
            0.2 will make it more focused and deterministic.

            We generally recommend altering this or `top_p` but not both.
        top_p:
          type: number
          minimum: 0
          maximum: 1
          default: 1
          example: 1
          nullable: true
          description: >
            An alternative to sampling with temperature, called nucleus
            sampling,

            where the model considers the results of the tokens with top_p
            probability

            mass. So 0.1 means only the tokens comprising the top 10%
            probability mass

            are considered.


            We generally recommend altering this or `temperature` but not both.
        user:
          type: string
          example: user-1234
          deprecated: true
          description: >
            This field is being replaced by `safety_identifier` and
            `prompt_cache_key`. Use `prompt_cache_key` instead to maintain
            caching optimizations.

            A stable identifier for your end-users. 

            Used to boost cache hit rates by better bucketing similar requests
            and  to help OpenAI detect and prevent abuse. information. 
        service_tier:
          $ref: '#/components/schemas/ServiceTier'
    ChatCompletionRequestDeveloperMessage:
      type: object
      title: Developer message
      description: >
        Developer-provided instructions that the model should follow, regardless
        of

        messages sent by the user. With o1 models and newer, `developer`
        messages

        replace the previous `system` messages.
      properties:
        content:
          description: The contents of the developer message.
          anyOf:
            - type: string
              description: The contents of the developer message.
              title: Text content
            - type: array
              description: >-
                An array of content parts with a defined type. For developer
                messages, only type `text` is supported.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestMessageContentPartText
              minItems: 1
        role:
          type: string
          enum:
            - developer
          description: The role of the messages author, in this case `developer`.
          x-stainless-const: true
        name:
          type: string
          description: >-
            An optional name for the participant. Provides the model information
            to differentiate between participants of the same role.
      required:
        - content
        - role
      x-stainless-naming:
        go:
          variant_constructor: DeveloperMessage
    ChatCompletionRequestSystemMessage:
      type: object
      title: System message
      description: >
        Developer-provided instructions that the model should follow, regardless
        of

        messages sent by the user. With o1 models and newer, use `developer`
        messages

        for this purpose instead.
      properties:
        content:
          description: The contents of the system message.
          anyOf:
            - type: string
              description: The contents of the system message.
              title: Text content
            - type: array
              description: >-
                An array of content parts with a defined type. For system
                messages, only type `text` is supported.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestSystemMessageContentPart
              minItems: 1
        role:
          type: string
          enum:
            - system
          description: The role of the messages author, in this case `system`.
          x-stainless-const: true
        name:
          type: string
          description: >-
            An optional name for the participant. Provides the model information
            to differentiate between participants of the same role.
      required:
        - content
        - role
      x-stainless-naming:
        go:
          variant_constructor: SystemMessage
    ChatCompletionRequestUserMessage:
      type: object
      title: User message
      description: |
        Messages sent by an end user, containing prompts or additional context
        information.
      properties:
        content:
          description: |
            The contents of the user message.
          anyOf:
            - type: string
              description: The text contents of the message.
              title: Text content
            - type: array
              description: >-
                An array of content parts with a defined type. Supported options
                differ based on the model being used to generate the response.
                Can contain text, image, or audio inputs.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestUserMessageContentPart
              minItems: 1
        role:
          type: string
          enum:
            - user
          description: The role of the messages author, in this case `user`.
          x-stainless-const: true
        name:
          type: string
          description: >-
            An optional name for the participant. Provides the model information
            to differentiate between participants of the same role.
      required:
        - content
        - role
      x-stainless-naming:
        go:
          variant_constructor: UserMessage
    ChatCompletionRequestAssistantMessage:
      type: object
      title: Assistant message
      description: |
        Messages sent by the model in response to user messages.
      properties:
        content:
          nullable: true
          description: >
            The contents of the assistant message. Required unless `tool_calls`
            or `function_call` is specified.
          anyOf:
            - type: string
              description: The contents of the assistant message.
              title: Text content
            - type: array
              description: >-
                An array of content parts with a defined type. Can be one or
                more of type `text`, or exactly one of type `refusal`.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestAssistantMessageContentPart
              minItems: 1
        refusal:
          nullable: true
          type: string
          description: The refusal message by the assistant.
        role:
          type: string
          enum:
            - assistant
          description: The role of the messages author, in this case `assistant`.
          x-stainless-const: true
        name:
          type: string
          description: >-
            An optional name for the participant. Provides the model information
            to differentiate between participants of the same role.
        audio:
          type: object
          nullable: true
          description: |
            Data about a previous audio response from the model. 
          required:
            - id
          properties:
            id:
              type: string
              description: |
                Unique identifier for a previous audio response from the model.
        tool_calls:
          $ref: '#/components/schemas/ChatCompletionMessageToolCalls'
        function_call:
          type: object
          deprecated: true
          description: >-
            Deprecated and replaced by `tool_calls`. The name and arguments of a
            function that should be called, as generated by the model.
          nullable: true
          properties:
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
            name:
              type: string
              description: The name of the function to call.
          required:
            - arguments
            - name
      required:
        - role
      x-stainless-soft-required:
        - content
    ChatCompletionRequestToolMessage:
      type: object
      title: Tool message
      properties:
        role:
          type: string
          enum:
            - tool
          description: The role of the messages author, in this case `tool`.
          x-stainless-const: true
        content:
          description: The contents of the tool message.
          anyOf:
            - type: string
              description: The contents of the tool message.
              title: Text content
            - type: array
              description: >-
                An array of content parts with a defined type. For tool
                messages, only type `text` is supported.
              title: Array of content parts
              items:
                $ref: >-
                  #/components/schemas/ChatCompletionRequestToolMessageContentPart
              minItems: 1
        tool_call_id:
          type: string
          description: Tool call that this message is responding to.
      required:
        - role
        - content
        - tool_call_id
      x-stainless-naming:
        go:
          variant_constructor: ToolMessage
    ChatCompletionRequestFunctionMessage:
      type: object
      title: Function message
      deprecated: true
      properties:
        role:
          type: string
          enum:
            - function
          description: The role of the messages author, in this case `function`.
          x-stainless-const: true
        content:
          nullable: true
          type: string
          description: The contents of the function message.
        name:
          type: string
          description: The name of the function to call.
      required:
        - role
        - content
        - name
    ResponseFormatJsonSchemaSchema:
      type: object
      title: JSON schema
      description: |
        The schema for the response format, described as a JSON Schema object.
      additionalProperties: true
    ChatCompletionRequestMessageContentPartText:
      type: object
      title: Text content part
      description: |
        Learn about text inputs.
      properties:
        type:
          type: string
          enum:
            - text
          description: The type of the content part.
          x-stainless-const: true
        text:
          type: string
          description: The text content.
      required:
        - type
        - text
      x-stainless-naming:
        go:
          variant_constructor: TextContentPart
    FunctionObject:
      type: object
      properties:
        description:
          type: string
          description: >-
            A description of what the function does, used by the model to choose
            when and how to call the function.
        name:
          type: string
          description: >-
            The name of the function to be called. Must be a-z, A-Z, 0-9, or
            contain underscores and dashes, with a maximum length of 64.
        parameters:
          $ref: '#/components/schemas/FunctionParameters'
        strict:
          type: boolean
          nullable: true
          default: false
          description: >-
            Whether to enable strict schema adherence when generating the
            function call. If set to true, the model will follow the exact
            schema defined in the `parameters` field. Only a subset of JSON
            Schema is supported when `strict` is `true`. 
      required:
        - name
    ChatCompletionAllowedToolsChoice:
      type: object
      title: Allowed tools
      description: |
        Constrains the tools available to the model to a pre-defined set.
      properties:
        type:
          type: string
          enum:
            - allowed_tools
          description: Allowed tool configuration type. Always `allowed_tools`.
          x-stainless-const: true
        allowed_tools:
          $ref: '#/components/schemas/ChatCompletionAllowedTools'
      required:
        - type
        - allowed_tools
    ChatCompletionNamedToolChoice:
      type: object
      title: Function tool choice
      description: >-
        Specifies a tool the model should use. Use to force the model to call a
        specific function.
      properties:
        type:
          type: string
          enum:
            - function
          description: For function calling, the type is always `function`.
          x-stainless-const: true
        function:
          type: object
          properties:
            name:
              type: string
              description: The name of the function to call.
          required:
            - name
      required:
        - type
        - function
    ChatCompletionNamedToolChoiceCustom:
      type: object
      title: Custom tool choice
      description: >-
        Specifies a tool the model should use. Use to force the model to call a
        specific custom tool.
      properties:
        type:
          type: string
          enum:
            - custom
          description: For custom tool calling, the type is always `custom`.
          x-stainless-const: true
        custom:
          type: object
          properties:
            name:
              type: string
              description: The name of the custom tool to call.
          required:
            - name
      required:
        - type
        - custom
    FunctionParameters:
      type: object
      description: >-
        The parameters the functions accepts, described as a JSON Schema object.
        See the guide for examples, and the [JSON Schema
        reference](https://json-schema.org/understanding-json-schema/) for
        documentation about the format. 


        Omitting `parameters` defines a function with an empty parameter list.
      additionalProperties: true
    ChatCompletionMessageToolCalls:
      type: array
      description: The tool calls generated by the model, such as function calls.
      items:
        anyOf:
          - $ref: '#/components/schemas/ChatCompletionMessageToolCall'
          - $ref: '#/components/schemas/ChatCompletionMessageCustomToolCall'
        x-stainless-naming:
          python:
            model_name: chat_completion_message_tool_call_union
            param_model_name: chat_completion_message_tool_call_union_param
        discriminator:
          propertyName: type
        x-stainless-go-variant-constructor: skip
    ChatCompletionMessageToolCallChunk:
      type: object
      properties:
        index:
          type: integer
        id:
          type: string
          description: The ID of the tool call.
        type:
          type: string
          enum:
            - function
          description: The type of the tool. Currently, only `function` is supported.
          x-stainless-const: true
        function:
          type: object
          properties:
            name:
              type: string
              description: The name of the function to call.
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
      required:
        - index
    Metadata:
      type: object
      description: >
        Set of 16 key-value pairs that can be attached to an object. This can be

        useful for storing additional information about the object in a
        structured

        format, and querying for objects via API or the dashboard. 


        Keys are strings with a maximum length of 64 characters. Values are
        strings

        with a maximum length of 512 characters.
      additionalProperties:
        type: string
      nullable: true
    ChatCompletionRequestSystemMessageContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartText'
    ChatCompletionRequestUserMessageContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartText'
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartImage'
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartAudio'
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartFile'
      discriminator:
        propertyName: type
    ChatCompletionRequestAssistantMessageContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartText'
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartRefusal'
      discriminator:
        propertyName: type
    ChatCompletionRequestToolMessageContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionRequestMessageContentPartText'
    ChatCompletionAllowedTools:
      type: object
      title: Allowed tools
      description: |
        Constrains the tools available to the model to a pre-defined set.
      properties:
        mode:
          type: string
          enum:
            - auto
            - required
          description: >
            Constrains the tools available to the model to a pre-defined set.


            `auto` allows the model to pick from among the allowed tools and
            generate a

            message.


            `required` requires the model to call one or more of the allowed
            tools.
        tools:
          type: array
          description: >
            A list of tool definitions that the model should be allowed to call.


            For the Chat Completions API, the list of tool definitions might
            look like:

            ```json

            [
              { "type": "function", "function": { "name": "get_weather" } },
              { "type": "function", "function": { "name": "get_time" } }
            ]

            ```
          items:
            type: object
            x-oaiExpandable: false
            description: |
              A tool definition that the model should be allowed to call.
            additionalProperties: true
      required:
        - mode
        - tools
    ChatCompletionMessageToolCall:
      type: object
      title: Function tool call
      description: |
        A call to a function tool created by the model.
      properties:
        id:
          type: string
          description: The ID of the tool call.
        type:
          type: string
          enum:
            - function
          description: The type of the tool. Currently, only `function` is supported.
          x-stainless-const: true
        function:
          type: object
          description: The function that the model called.
          properties:
            name:
              type: string
              description: The name of the function to call.
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
          required:
            - name
            - arguments
      required:
        - id
        - type
        - function
    ChatCompletionMessageCustomToolCall:
      type: object
      title: Custom tool call
      description: |
        A call to a custom tool created by the model.
      properties:
        id:
          type: string
          description: The ID of the tool call.
        type:
          type: string
          enum:
            - custom
          description: The type of the tool. Always `custom`.
          x-stainless-const: true
        custom:
          type: object
          description: The custom tool that the model called.
          properties:
            name:
              type: string
              description: The name of the custom tool to call.
            input:
              type: string
              description: The input for the custom tool call generated by the model.
          required:
            - name
            - input
      required:
        - id
        - type
        - custom
    ChatCompletionRequestMessageContentPartImage:
      type: object
      title: Image content part
      description: |
        Learn about image inputs.
      properties:
        type:
          type: string
          enum:
            - image_url
          description: The type of the content part.
          x-stainless-const: true
        image_url:
          type: object
          properties:
            url:
              type: string
              description: Either a URL of the image or the base64 encoded image data.
              format: uri
            detail:
              type: string
              description: 'Specifies the detail level of the image. '
              enum:
                - auto
                - low
                - high
              default: auto
          required:
            - url
      required:
        - type
        - image_url
      x-stainless-naming:
        go:
          variant_constructor: ImageContentPart
    ChatCompletionRequestMessageContentPartAudio:
      type: object
      title: Audio content part
      description: |
        Learn about audio inputs.
      properties:
        type:
          type: string
          enum:
            - input_audio
          description: The type of the content part. Always `input_audio`.
          x-stainless-const: true
        input_audio:
          type: object
          properties:
            data:
              type: string
              description: Base64 encoded audio data.
            format:
              type: string
              enum:
                - wav
                - mp3
              description: >
                The format of the encoded audio data. Currently supports "wav"
                and "mp3".
          required:
            - data
            - format
      required:
        - type
        - input_audio
      x-stainless-naming:
        go:
          variant_constructor: InputAudioContentPart
    ChatCompletionRequestMessageContentPartFile:
      type: object
      title: File content part
      description: |
        Learn about file inputs for text generation.
      properties:
        type:
          type: string
          enum:
            - file
          description: The type of the content part. Always `file`.
          x-stainless-const: true
        file:
          type: object
          properties:
            filename:
              type: string
              description: >
                The name of the file, used when passing the file to the model as
                a 

                string.
            file_data:
              type: string
              description: >
                The base64 encoded file data, used when passing the file to the
                model 

                as a string.
            file_id:
              type: string
              description: |
                The ID of an uploaded file to use as input.
          x-stainless-naming:
            java:
              type_name: FileObject
            kotlin:
              type_name: FileObject
      required:
        - type
        - file
      x-stainless-naming:
        go:
          variant_constructor: FileContentPart
    ChatCompletionRequestMessageContentPartRefusal:
      type: object
      title: Refusal content part
      properties:
        type:
          type: string
          enum:
            - refusal
          description: The type of the content part.
          x-stainless-const: true
        refusal:
          type: string
          description: The refusal message generated by the model.
      required:
        - type
        - refusal
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Image Generation

> Generate images from text prompts using the wan2.6-t2i model.

<Note>
  This API is compatible with Alibaba's Tongyi Wanxiang (Wan2) models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-image-v2-api-reference) for more details.
</Note>

## Overview

Generate high-quality images from text descriptions using the wan2.6-t2i model. This is the latest Wan2.6 text-to-image model.

## Resolution Guidelines

* **Default**: 1280\*1280
* **Total pixels**: Between 768\*768 and 1440\*1440
* **Aspect ratio**: Between 1:4 and 4:1

### Common Aspect Ratios

| Aspect Ratio | Recommended Resolution   |
| ------------ | ------------------------ |
| 1:1          | 1280\*1280 or 1024\*1024 |
| 2:3          | 800\*1200                |
| 3:2          | 1200\*800                |
| 3:4          | 960\*1280                |
| 4:3          | 1280\*960                |
| 9:16         | 720\*1280                |
| 16:9         | 1280\*720                |

## Example Requests

### Basic Text-to-Image

```json theme={null}
{
  "prompt": "A small cat running in the moonlight",
  "n": 1
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "A serene mountain landscape at sunset, dramatic clouds, vibrant colors",
  "negative_prompt": "low resolution, error, worst quality, low quality",
  "size": "1280*720",
  "n": 4
}
```

### With Custom Seed

```json theme={null}
{
  "prompt": "Futuristic cityscape at night, neon lights, cyberpunk style",
  "size": "1280*720",
  "n": 1,
  "seed": 12345
}
```

## Parameters

### n (Number of Images)

* **Range**: 1-4
* **Default**: 4
* **Note**: Directly affects cost

### prompt\_extend (Prompt Rewriting)

* **Default**: false
* **Effect**: Uses AI to enhance and expand short prompts

### seed (Random Seed)

* **Range**: 0 to 2,147,483,647
* **Purpose**: Improves reproducibility of results


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-t2i/wan2.6-t2i.yaml POST /vendors/alibaba/v1/wan2.6-t2i/generation
openapi: 3.1.0
info:
  title: Wan2.6-t2i API
  description: Wan2.6 Text-to-Image Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-t2i/generation:
    post:
      summary: Create Generation Task
      description: Generate images from text prompts using the wan2.6-t2i model.
      operationId: wan26_t2i_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26T2IRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26T2IRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text description for the image (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters)
          maxLength: 500
        size:
          type: string
          description: |-
            Image resolution in format "width\*height" (e.g., "1280\*1280")

            Default: 1280\*1280
            Total pixels: [768\*768, 1440\*1440], aspect ratio: [1:4, 4:1]
          default: 1280*1280
        'n':
          type: integer
          description: Number of images to generate (1-4)
          minimum: 1
          maximum: 4
          default: 4
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (improves short prompts but
            increases processing time)
          default: false
        seed:
          type: integer
          description: Random seed for reproducibility [0, 2147483647]
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Image Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-t2i generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URLs in the `images` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image-1.jpg"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-t2i/wan2.6-t2i.yaml GET /vendors/alibaba/v1/wan2.6-t2i/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-t2i API
  description: Wan2.6 Text-to-Image Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-t2i/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_t2i_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26T2IResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26T2IResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
            description: URL of the generated image
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Image Generation

> Edit images using the wan2.6-image model with text prompts and reference images.

<Note>
  This API is compatible with Alibaba's Tongyi Wanxiang (Wan2) models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-image-v2-api-reference) for more details.
</Note>

## Overview

Edit and transform images using the wan2.6-image model with text prompts and reference images.

## Image Requirements

| Property          | Requirement                                   |
| ----------------- | --------------------------------------------- |
| **Formats**       | JPEG, JPG, PNG, BMP, WEBP                     |
| **Dimensions**    | \[384, 5000] pixels for both width and height |
| **Max file size** | 10MB per image                                |
| **Max images**    | 2 images                                      |
| **Input**         | Public URL or Base64 encoded data             |

## Resolution Guidelines

* **Default**: 1280\*1280
* **Total pixels**: Between 768\*768 and 1440\*1440
* **Aspect ratio**: Between 1:4 and 4:1

## Example Requests

### Basic Image Editing

```json theme={null}
{
  "prompt": "Replace the character's clothing with traditional Chinese Hanfu",
  "images": ["https://example.com/portrait.jpg"],
  "n": 1
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Transform the image into an oil painting style",
  "negative_prompt": "blurry, low quality, distorted",
  "images": ["https://example.com/photo.jpg"],
  "size": "1280*1280",
  "n": 1
}
```

### With Custom Seed

```json theme={null}
{
  "prompt": "Add a colorful sunset background",
  "images": ["https://example.com/portrait.jpg"],
  "size": "1280*720",
  "n": 1,
  "seed": 42
}
```

## Parameters

### images

* **Required**: Yes
* **Max items**: 2
* **Description**: Array of image URLs or Base64 encoded data

### n (Number of Images)

* **Range**: 1-4
* **Default**: 4
* **Note**: Directly affects cost

### prompt\_extend (Prompt Rewriting)

* **Default**: false
* **Effect**: Uses AI to enhance and expand short prompts

### seed (Random Seed)

* **Range**: 0 to 2,147,483,647
* **Purpose**: Improves reproducibility of results


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-image/wan2.6-image.yaml POST /vendors/alibaba/v1/wan2.6-image/generation
openapi: 3.1.0
info:
  title: Wan2.6-image API
  description: Wan2.6 Image Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-image/generation:
    post:
      summary: Create Generation Task
      description: >-
        Edit images using the wan2.6-image model with text prompts and reference
        images.
      operationId: wan26_image_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26ImageRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26ImageRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text description for the desired edit (max 2000 characters)
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters)
          maxLength: 500
        images:
          type: array
          items:
            type: string
          maxItems: 3
          description: |-
            Array of image URLs or Base64 encoded data (max 3 images)

            Supported formats: JPEG, JPG, PNG, BMP, WEBP
            Dimensions: [384, 5000] pixels for both width and height
            Max file size: 10MB per image
        size:
          anyOf:
            - type: string
            - type: 'null'
          description: |-
            Output image resolution (format: "width\*height")

            Default: 1280\*1280
            Total pixels: [768\*768, 1440\*1440], aspect ratio: [1:4, 4:1]
          default: 1280*1280
        'n':
          type: integer
          description: Number of images to generate (1-4)
          minimum: 1
          maximum: 4
          default: 4
        seed:
          type: integer
          description: Random seed [0, 2147483647]
          minimum: 0
          maximum: 2147483647
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting
          default: false
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - images
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Image Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-image generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URLs in the `images` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image-1.jpg"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-image/wan2.6-image.yaml GET /vendors/alibaba/v1/wan2.6-image/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-image API
  description: Wan2.6 Image Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-image/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_image_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26ImageResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26ImageResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Image Preview Generation

> Generate images from text prompts using the wan2.5-t2i-preview model.

<Note>
  This API is compatible with Alibaba's Tongyi Wanxiang (Wan2) models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-image-v2-api-reference) for more details.
</Note>

## Overview

Generate high-quality images from text descriptions using the wan2.5-t2i-preview model. This is the latest Wan2.5 text-to-image model with enhanced capabilities.

## Key Features

* Support for longer prompts (up to 2000 characters)
* Flexible resolution and aspect ratio support
* Higher quality output

## Resolution Guidelines

* **Default**: 1280\*1280
* **Total pixels**: Between 768\*768 and 1440\*1440
* **Aspect ratio**: Between 1:4 and 4:1
* **Example**: 768\*2700 is valid (meets pixel and ratio requirements)

### Common Aspect Ratios

| Aspect Ratio | Recommended Resolution   |
| ------------ | ------------------------ |
| 1:1          | 1280\*1280 or 1024\*1024 |
| 2:3          | 800\*1200                |
| 3:2          | 1200\*800                |
| 3:4          | 960\*1280                |
| 4:3          | 1280\*960                |
| 9:16         | 720\*1280                |
| 16:9         | 1280\*720                |
| 21:9         | 1344\*576                |

## Prompt Tips

For best results:

* Be specific and descriptive about what you want to see
* Include details about style, composition, lighting, and mood
* Use the negative prompt to exclude unwanted elements
* For short prompts, consider enabling `prompt_extend` for enhanced results

## Example Requests

### Basic Text-to-Image

```json theme={null}
{
  "prompt": "A sitting orange cat with a joyful expression, lively and cute, realistic and accurate",
  "n": 1
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "A serene mountain landscape at sunset, dramatic clouds, vibrant colors",
  "negative_prompt": "low resolution, error, worst quality, low quality, incomplete, extra fingers, poor proportions",
  "size": "1280*720",
  "n": 4
}
```

### High-Resolution Portrait

```json theme={null}
{
  "prompt": "Professional portrait of a woman in business attire, studio lighting, shallow depth of field, professional photography",
  "size": "960*1280",
  "n": 1,
  "prompt_extend": false
}
```

### With Custom Seed for Reproducibility

```json theme={null}
{
  "prompt": "Futuristic cityscape at night, neon lights, cyberpunk style",
  "size": "1344*576",
  "n": 1,
  "seed": 12345
}
```

## Parameters

### n (Number of Images)

* **Range**: 1-4
* **Default**: 4
* **Note**: Directly affects cost (cost = unit price × number of images)
* **Recommendation**: Set to 1 during testing to minimize costs

### prompt\_extend (Prompt Rewriting)

* **Default**: false
* **Effect**: Uses AI to enhance and expand short prompts
* **Trade-off**: Improves results for short prompts but increases processing time

### seed (Random Seed)

* **Range**: 0 to 2,147,483,647
* **Purpose**: Improves reproducibility of results
* **Note**: Due to probabilistic nature, same seed doesn't guarantee identical results
* **Behavior**: When n > 1, generates seeds as: seed, seed+1, seed+2, etc.


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-t2i-preview/wan2.5-t2i-preview.yaml POST /vendors/alibaba/v1/wan2.5-t2i-preview/generation
openapi: 3.1.0
info:
  title: Wan2.5-t2i-preview API
  description: Wan2.5 Text-to-Image Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-t2i-preview/generation:
    post:
      summary: Create Generation Task
      description: Generate images from text prompts using the wan2.5-t2i-preview model.
      operationId: wan25_t2i_preview_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25T2IPreviewRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25T2IPreviewRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text description for the image (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters)
          maxLength: 500
        size:
          type: string
          description: |-
            Image resolution in format "width\*height" (e.g., "1280\*1280")

            Default: 1280\*1280
            Total pixels: [768\*768, 1440\*1440], aspect ratio: [1:4, 4:1]
          default: 1280*1280
        'n':
          type: integer
          description: Number of images to generate (1-4)
          minimum: 1
          maximum: 4
          default: 4
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (improves short prompts but
            increases processing time)
          default: false
        seed:
          type: integer
          description: Random seed for reproducibility [0, 2147483647]
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Image Preview Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-t2i-preview generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URLs in the `images` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image-1.jpg",
    "https://example.com/generated-image-2.jpg"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-t2i-preview/wan2.5-t2i-preview.yaml GET /vendors/alibaba/v1/wan2.5-t2i-preview/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-t2i-preview API
  description: Wan2.5 Text-to-Image Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-t2i-preview/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_t2i_preview_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25T2IPreviewResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25T2IPreviewResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
            description: URL of the generated image
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Image Preview Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-t2i-preview generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URLs in the `images` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image-1.jpg",
    "https://example.com/generated-image-2.jpg"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-t2i-preview/wan2.5-t2i-preview.yaml GET /vendors/alibaba/v1/wan2.5-t2i-preview/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-t2i-preview API
  description: Wan2.5 Text-to-Image Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-t2i-preview/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_t2i_preview_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25T2IPreviewResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25T2IPreviewResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
            description: URL of the generated image
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Image Preview Generation

> Edit images using the wan2.5-i2i-preview model with reference images.

<Note>
  This API is compatible with Alibaba's Tongyi Wanxiang (Wan2) models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-image-v2-api-reference) for more details.
</Note>

## Overview

Edit and transform images using the wan2.5-i2i-preview model with text prompts and reference images.

## Key Features

* Support for up to 3 reference images
* Longer prompts (up to 2000 characters)
* Flexible output resolution and aspect ratio

## Image Requirements

| Property          | Requirement                                   |
| ----------------- | --------------------------------------------- |
| **Formats**       | JPEG, JPG, PNG, BMP, WEBP                     |
| **Dimensions**    | \[384, 5000] pixels for both width and height |
| **Max file size** | 10MB per image                                |
| **Max images**    | 3 images                                      |
| **Input**         | Public URL or Base64 encoded data             |

## Resolution Guidelines

* **Default**: 1280\*1280
* **Total pixels**: Between 768\*768 and 1440\*1440
* **Aspect ratio**: Between 1:4 and 4:1

## Example Requests

### Basic Image Editing

```json theme={null}
{
  "prompt": "Change the dress to a vintage style lace gown",
  "images": ["https://example.com/image1.jpg"],
  "n": 1
}
```

### With Two Reference Images

```json theme={null}
{
  "prompt": "Combine these two images into a single portrait scene",
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "size": "1280*720",
  "n": 4
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Transform the image into an oil painting style",
  "negative_prompt": "blurry, low quality, distorted",
  "images": ["https://example.com/photo.jpg"],
  "size": "1280*1280",
  "n": 1
}
```

### With Base64 Image

```json theme={null}
{
  "prompt": "Add a colorful background to this portrait",
  "images": ["data:image/jpeg;base64,/9j/4AAQSkZJRg..."],
  "size": "960*1280",
  "n": 2
}
```

## Parameters

### images

* **Required**: Yes
* **Max items**: 3
* **Description**: Array of image URLs or Base64 encoded data

### n (Number of Images)

* **Range**: 1-4
* **Default**: 4
* **Note**: Directly affects cost (cost = unit price × number of images)

### seed (Random Seed)

* **Range**: 0 to 2,147,483,647
* **Purpose**: Improves reproducibility of results
* **Behavior**: When n > 1, generates seeds as: seed, seed+1, seed+2, etc.

### prompt\_extend (Prompt Rewriting)

* **Default**: false
* **Effect**: Uses AI to enhance and expand short prompts


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-i2i-preview/wan2.5-i2i-preview.yaml POST /vendors/alibaba/v1/wan2.5-i2i-preview/generation
openapi: 3.1.0
info:
  title: Wan2.5-i2i-preview API
  description: Wan2.5 Image-to-Image Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-i2i-preview/generation:
    post:
      summary: Create Generation Task
      description: Edit images using the wan2.5-i2i-preview model with reference images.
      operationId: wan25_i2i_preview_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25I2IPreviewRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25I2IPreviewRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text description for the desired edit (max 2000 characters)
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters)
          maxLength: 500
        images:
          type: array
          items:
            type: string
          maxItems: 3
          description: |-
            Array of image URLs or Base64 encoded data (max 3 images)

            Supported formats: JPEG, JPG, PNG, BMP, WEBP
            Dimensions: [384, 5000] pixels for both width and height
            Max file size: 10MB per image
        size:
          anyOf:
            - type: string
            - type: 'null'
          description: |-
            Output image resolution (format: "width\*height")

            Default: 1280\*1280
            Total pixels: [768\*768, 1440\*1440], aspect ratio: [1:4, 4:1]
          default: 1280*1280
        'n':
          type: integer
          description: Number of images to generate (1-4)
          minimum: 1
          maximum: 4
          default: 4
        seed:
          type: integer
          description: Random seed [0, 2147483647]
          minimum: 0
          maximum: 2147483647
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (improves short prompts but
            increases processing time)
          default: false
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - images
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Image Preview Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-i2i-preview generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URLs in the `images` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image-1.jpg",
    "https://example.com/generated-image-2.jpg"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-i2i-preview/wan2.5-i2i-preview.yaml GET /vendors/alibaba/v1/wan2.5-i2i-preview/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-i2i-preview API
  description: Wan2.5 Image-to-Image Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-i2i-preview/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_i2i_preview_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25I2IPreviewResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25I2IPreviewResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image Max Generation

> Generate images from text prompts using the qwen-image-max model.

Qwen-Image-Max is a general-purpose image generation model that improves upon the Plus series by enhancing the realism and naturalness of images. It effectively reduces AI-generated artifacts and excels in rendering character textures, fine details, and text.

Key features:
- Supports multiple artistic styles
- Excels at complex text rendering
- Multi-line, paragraph-level text generation
- Fine-grained detail rendering

## Overview

Generate highly realistic and natural images from text descriptions using the qwen-image-max model. This advanced text-to-image model improves upon the Plus series with enhanced realism and reduced AI-generated artifacts.

## Key Features

* **Enhanced Realism**: Produces more natural-looking images with fewer AI artifacts
* **Character Excellence**: Superior rendering of human textures, skin tones, and facial details
* **Text Rendering**: Excels at generating clear, legible text in images
* **Multi-line Text**: Supports paragraph-level text generation within images
* **Fine Details**: Outstanding performance in rendering intricate details
* **Multiple Styles**: Supports various artistic and photographic styles
* **High Resolution**: Multiple aspect ratios from 1:1 to 16:9

## Pricing

**\$0.075 per image**

## Resolution Options

| Resolution              | Aspect Ratio | Best For                               |
| ----------------------- | ------------ | -------------------------------------- |
| **1664\*928** (default) | 16:9         | Landscape photos, banners, wide scenes |
| **1472\*1104**          | 4:3          | Standard photos, presentations         |
| **1328\*1328**          | 1:1          | Social media posts, profile images     |
| **1104\*1472**          | 3:4          | Portraits, vertical content            |
| **928\*1664**           | 9:16         | Mobile screens, stories                |

## Example Requests

### Basic Text-to-Image

```json theme={null}
{
  "prompt": "A professional portrait photograph of a woman in her 30s, natural lighting, soft smile, business attire"
}
```

### Complex Scene with Text

```json theme={null}
{
  "prompt": "A cozy coffee shop interior with a chalkboard menu on the wall displaying 'Daily Special: Cappuccino $4.50', warm ambient lighting, wooden furniture, customers in the background",
  "size": "1664*928",
  "prompt_extend": true
}
```

### Artistic Style Generation

```json theme={null}
{
  "prompt": "An oil painting of a sunset over mountains, impressionist style, vibrant colors, thick brush strokes",
  "negative_prompt": "low resolution, low quality, AI-like, overly smooth, waxy, no facial details",
  "size": "1472*1104"
}
```

## Parameters

### prompt (Required)

* **Type**: String
* **Max Length**: 800 characters
* **Languages**: Chinese and English supported

### negative\_prompt

* **Type**: String or null
* **Max Length**: 500 characters

### size

* **Type**: String (enum)
* **Default**: "1664\*928" (16:9)

### prompt\_extend

* **Type**: Boolean
* **Default**: true

### seed

* **Range**: 0 to 2,147,483,647


## OpenAPI

````yaml /api-reference/endpoint/alibaba/qwen-image-max/qwen-image-max.yaml POST /vendors/alibaba/v1/qwen-image-max/generation
openapi: 3.1.0
info:
  title: Qwen-Image-Max API
  description: Qwen-Image-Max Text-to-Image Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/qwen-image-max/generation:
    post:
      summary: Create Generation Task
      description: >-
        Generate images from text prompts using the qwen-image-max model.


        Qwen-Image-Max is a general-purpose image generation model that improves
        upon the Plus series by enhancing the realism and naturalness of images.
        It effectively reduces AI-generated artifacts and excels in rendering
        character textures, fine details, and text.


        Key features:

        - Supports multiple artistic styles

        - Excels at complex text rendering

        - Multi-line, paragraph-level text generation

        - Fine-grained detail rendering
      operationId: qwen_image_max_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QwenImageMaxRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    QwenImageMaxRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text description for the image (max 800 characters).

            Describes the desired content, style, and composition of the
            generated image.

            Supports both Chinese and English.
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Negative prompt describing unwanted content (max 500 characters).

            Used to constrain the image generation.

            Example: low resolution, low quality, deformed limbs, deformed
            fingers, oversaturated, waxy, no facial details, overly smooth,
            AI-like, chaotic composition, blurry text, distorted text.
          maxLength: 500
        size:
          type: string
          description: |-
            Image resolution in format "width\*height".

            Default: 1664\*928

            Available resolutions and aspect ratios:
            - 1664\*928 (default): 16:9
            - 1472\*1104: 4:3
            - 1328\*1328: 1:1
            - 1104\*1472: 3:4
            - 928\*1664: 9:16
          default: 1664*928
          enum:
            - 1664*928
            - 1472*1104
            - 1328*1328
            - 1104*1472
            - 928*1664
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting.

            When enabled, the model optimizes and refines the positive prompt.

            Keep enabled if your input prompt is simple or if you want the model
            to be more creative.

            Set to false if your prompt is already detailed and professional.
          default: true
        seed:
          type: integer
          description: >-
            Random seed for reproducibility [0, 2147483647].

            Using the same seed produces more consistent results.

            Note: Results are not guaranteed to be identical for every call even
            with the same seed.
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image Max Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a qwen-image-max generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated image URL in the `images` array. The URL is valid for 24 hours.

## Example Responses

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-02-09T10:30:00Z",
    "updated_at": "2025-02-09T10:30:45Z"
  },
  "images": [
    "https://example.com/generated-image.jpg"
  ]
}
```

## Polling Guidelines

1. **Initial Wait**: Wait at least 2-3 seconds before the first poll
2. **Poll Interval**: Poll every 2-3 seconds for `pending` or `processing` status
3. **Timeout**: Consider implementing a timeout (e.g., 5 minutes)


## OpenAPI

````yaml /api-reference/endpoint/alibaba/qwen-image-max/qwen-image-max.yaml GET /vendors/alibaba/v1/qwen-image-max/generation/{task_id}
openapi: 3.1.0
info:
  title: Qwen-Image-Max API
  description: Qwen-Image-Max Text-to-Image Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/qwen-image-max/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: qwen_image_max_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QwenImageMaxResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    QwenImageMaxResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
            description: URL of the generated image (valid for 24 hours)
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image Edit Max Generation

> Edit images using the qwen-image-edit-max model.

This model supports multi-image input and output. It can:
- Accurately modify text in images
- Add, delete, or move objects
- Change the action of a subject
- Transfer image styles
- Enhance image details
- Multi-image fusion (combine elements from up to 3 images)

Key features:
- Supports 1-3 input images
- Can generate 1-6 output images
- Supports custom output resolutions
- Supports intelligent prompt optimization

<Note>
  This is the premium tier of Qwen Image Edit model with enhanced quality and capabilities. For more details, refer to the official documentation.
</Note>

## Overview

Edit and enhance images using the qwen-image-edit-max model. This premium image editing model supports multi-image input and output with powerful editing capabilities at a higher quality tier.

## Key Features

* **Multi-image support**: Input 1-3 images for complex editing tasks
* **Precise text editing**: Accurately modify text content in images
* **Object manipulation**: Add, delete, or move objects within images
* **Action modification**: Change the action or pose of subjects
* **Style transfer**: Apply different artistic styles to images
* **Detail enhancement**: Improve image clarity and details
* **Image fusion**: Combine elements from multiple images (up to 3)
* **Flexible output**: Generate 1-6 images per request
* **Premium Quality**: Enhanced results compared to the Plus tier

## Pricing

**\$0.075 per image** - Premium tier with enhanced quality

Compare with Qwen Image Edit Plus: \$0.03 per image

## Image Requirements

| Property        | Requirement                                             |
| --------------- | ------------------------------------------------------- |
| **Formats**     | JPG, JPEG, PNG, BMP, TIFF, WEBP, GIF (first frame only) |
| **Resolution**  | Width and height: 384-3072 pixels                       |
| **File Size**   | Max 10MB per image                                      |
| **Input Count** | 1-3 images                                              |
| **Input Type**  | Public URL or Base64-encoded data                       |

## Resolution Guidelines

* **Default**: Maintains aspect ratio similar to input with resolution close to 1024\*1024
* **Custom**: Specify width\*height with both dimensions in range \[512, 2048] pixels
* **Aspect Ratio**: Determined by the last input image

## Example Requests

### Basic Single Image Edit

```json theme={null}
{
  "images": ["https://example.com/photo.jpg"],
  "prompt": "Change the person's shirt to red"
}
```

### Text Modification

```json theme={null}
{
  "images": ["https://example.com/sign.jpg"],
  "prompt": "Change the text on the sign from 'OPEN' to 'CLOSED'",
  "n": 1,
  "size": "1024*768"
}
```

### Multi-image Fusion

```json theme={null}
{
  "images": [
    "https://example.com/person.jpg",
    "https://example.com/background.jpg",
    "https://example.com/object.jpg"
  ],
  "prompt": "Place the person from Image 1 in the background from Image 2, holding the object from Image 3",
  "n": 4,
  "prompt_extend": true
}
```

### Style Transfer with Negative Prompt

```json theme={null}
{
  "images": ["https://example.com/portrait.jpg"],
  "prompt": "Transform this portrait into a watercolor painting style",
  "negative_prompt": "low resolution, error, worst quality, low quality, disfigured, extra fingers, bad proportions",
  "size": "1024*1024",
  "n": 2,
  "seed": 42
}
```

### Object Addition

```json theme={null}
{
  "images": ["https://example.com/room.jpg"],
  "prompt": "Add a modern floor lamp in the left corner of the room",
  "n": 3,
  "prompt_extend": true
}
```

## Parameters

### images (Required)

* **Type**: Array of strings
* **Count**: 1-3 images
* **Format**: URL or Base64-encoded image data
* **Note**: For multi-image input, reference them as "Image 1", "Image 2", "Image 3" in the prompt
* **Aspect Ratio**: Output aspect ratio is determined by the last image in the array

### prompt (Required)

* **Type**: String
* **Max Length**: 800 characters
* **Languages**: Chinese and English supported
* **Description**: Clear instructions for what you want to change or add to the image(s)

### negative\_prompt

* **Type**: String or null
* **Max Length**: 500 characters
* **Default**: null
* **Purpose**: Describe elements you want to avoid in the output
* **Example**: "low resolution, error, worst quality, low quality, disfigured"

### size

* **Type**: String
* **Format**: "width\*height" (e.g., "1024\*768")
* **Range**: Both width and height must be \[512, 2048] pixels
* **Default**: Auto-adjusted to maintain input aspect ratio near 1024\*1024

### n (Number of Images)

* **Range**: 1-6
* **Default**: 1
* **Note**: Each image incurs the per-image cost

### prompt\_extend (Prompt Rewriting)

* **Type**: Boolean
* **Default**: true
* **Effect**: Uses AI to enhance and optimize prompts for better results
* **Recommendation**: Especially useful for short or simple prompts

### seed (Random Seed)

* **Range**: 0 to 2,147,483,647
* **Purpose**: Helps ensure consistency across generations
* **Note**: Same seed doesn't guarantee identical results but improves reproducibility

## Use Cases

1. **E-commerce**: Change product colors, add accessories, or modify backgrounds
2. **Marketing**: Update text in promotional images, swap logos, or adjust layouts
3. **Photo Editing**: Remove unwanted objects, change clothing, or enhance details
4. **Creative Design**: Combine elements from multiple images, apply artistic styles
5. **Content Creation**: Generate variations with different actions or compositions

## Tips for Best Results

* Be specific and descriptive in your prompts
* Use "Image 1", "Image 2", "Image 3" when working with multiple images
* Enable `prompt_extend` for more polished results
* Use negative prompts to avoid common quality issues
* Request multiple outputs (n > 1) to explore variations
* Specify custom size when aspect ratio control is important


## OpenAPI

````yaml /api-reference/endpoint/alibaba/qwen-image-edit-max/qwen-image-edit-max.yaml POST /vendors/alibaba/v1/qwen-image-edit-max/generation
openapi: 3.1.0
info:
  title: Qwen-Image-Edit-Max API
  description: Qwen-Image-Edit-Max Image Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/qwen-image-edit-max/generation:
    post:
      summary: Create Generation Task
      description: |-
        Edit images using the qwen-image-edit-max model.

        This model supports multi-image input and output. It can:
        - Accurately modify text in images
        - Add, delete, or move objects
        - Change the action of a subject
        - Transfer image styles
        - Enhance image details
        - Multi-image fusion (combine elements from up to 3 images)

        Key features:
        - Supports 1-3 input images
        - Can generate 1-6 output images
        - Supports custom output resolutions
        - Supports intelligent prompt optimization
      operationId: qwen_image_edit_max_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QwenImageEditMaxRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    QwenImageEditMaxRequest:
      type: object
      additionalProperties: false
      properties:
        images:
          type: array
          description: >-
            Array of input image URLs or Base64-encoded images.

            Supports 1-3 images.

            For multi-image input, the order defines their sequence.

            The aspect ratio of the output image is determined by the last
            image.


            Image requirements:

            - Formats: JPG, JPEG, PNG, BMP, TIFF, WEBP, GIF (first frame only)

            - Resolution: Width and height should be between 384 and 3072 pixels

            - Size: No larger than 10 MB
          items:
            type: string
            description: Image URL or Base64-encoded image data
          minItems: 1
          maxItems: 3
        prompt:
          type: string
          description: >-
            Image editing instruction (max 800 characters).

            Describes the elements and visual features you want in the generated
            image.

            When editing multiple images, use "Image 1", "Image 2", "Image 3" to
            refer to corresponding images.

            Supports both Chinese and English.
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Negative prompt describing unwanted content (max 500 characters).

            Used to constrain the image generation.

            Example: low resolution, error, worst quality, low quality,
            disfigured, extra fingers, bad proportions.
          maxLength: 500
        size:
          type: string
          description: >-
            Output image resolution in format "width*height" (e.g.,
            "1024*1024").

            Width and height must be in range [512, 2048] pixels.

            Example: "1024*1024", "768*1024", "512*512"


            Leave empty to maintain aspect ratio similar to input image with
            resolution close to 1024*1024.
        'n':
          type: integer
          description: Number of images to generate (1-6).
          minimum: 1
          maximum: 6
          default: 1
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting.

            When enabled, a large language model optimizes the positive prompt.

            Significantly improves results for simple or less descriptive
            prompts.
          default: true
        seed:
          type: integer
          description: >-
            Random seed for reproducibility [0, 2147483647].

            Using the same seed helps ensure consistency of generated content.

            Note: Results are not guaranteed to be identical for every call even
            with the same seed.
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - images
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image Edit Max Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a qwen-image-edit-max generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated/edited image URLs in the `images` array. Each URL is valid for 24 hours.

## Example Responses

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-02-09T10:30:00Z",
    "updated_at": "2025-02-09T10:30:45Z"
  },
  "images": [
    "https://example.com/edited-image-1.jpg",
    "https://example.com/edited-image-2.jpg"
  ]
}
```

### Pending Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "pending",
    "created_at": "2025-02-09T10:30:00Z",
    "updated_at": "2025-02-09T10:30:00Z"
  }
}
```

### Processing Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "processing",
    "created_at": "2025-02-09T10:30:00Z",
    "updated_at": "2025-02-09T10:30:15Z"
  }
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-02-09T10:30:00Z",
    "updated_at": "2025-02-09T10:30:15Z",
    "error": {
      "code": 3001,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```

## Polling Guidelines

For asynchronous task processing:

1. **Initial Wait**: Wait at least 2-3 seconds before the first poll
2. **Poll Interval**: Poll every 2-3 seconds for `pending` or `processing` status
3. **Timeout**: Consider implementing a timeout (e.g., 5 minutes) for long-running tasks
4. **Exponential Backoff**: Consider increasing poll intervals for longer tasks

## Error Handling

If the task fails, check the `error` object in `task_info` for details:

* **code**: Numeric error code identifying the error type
* **title**: Brief error description
* **detail**: Detailed explanation of what went wrong

Common error scenarios:

* Invalid or prohibited content in prompt
* Image file size exceeds limit
* Unsupported image format
* Invalid resolution parameters


## OpenAPI

````yaml /api-reference/endpoint/alibaba/qwen-image-edit-max/qwen-image-edit-max.yaml GET /vendors/alibaba/v1/qwen-image-edit-max/generation/{task_id}
openapi: 3.1.0
info:
  title: Qwen-Image-Edit-Max API
  description: Qwen-Image-Edit-Max Image Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/qwen-image-edit-max/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: qwen_image_edit_max_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QwenImageEditMaxResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    QwenImageEditMaxResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated image URLs (only present when status is success)
          items:
            type: string
            format: uri
            description: URL of the generated image (valid for 24 hours)
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana Pro Image Generation

> Generate ultra-sharp images from text prompts using the Gemini Nano-Banana Pro model

## Overview

Generate ultra-sharp, cinematic frames from short text prompts using Google's Gemini Nano Banana Pro model. Compared with the base Nano Banana release, the Pro tier unlocks:

* Wider aspect ratios (from square up to 21:9 panoramic)
* Higher fidelity presets (`resolution` up to 4K)
* Better prompt adherence thanks to an upgraded vision-language alignment stack


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-pro/openapi.yaml POST /vendors/google/v1/nano-banana-pro/generation
openapi: 3.1.0
info:
  title: Gemini Nano-Banana Pro API
  description: Gemini Nano-Banana Pro high-fidelity image APIs
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-pro/generation:
    post:
      summary: Text to Image Generation
      description: >-
        Generate ultra-sharp images from text prompts using the Gemini
        Nano-Banana Pro model
      operationId: nano_banana_pro_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerationRequest'
            example:
              prompt: A beautiful sunset over the mountains
              aspect_ratio: '5:4'
              resolution: 2K
        required: true
      responses:
        '202':
          description: Task created successfully
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                properties:
                  task_info:
                    $ref: '#/components/schemas/TaskInfoResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: pending
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
components:
  schemas:
    GenerationRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text prompt for image generation
        aspect_ratio:
          type: string
          description: Aspect ratio of the generated image
          enum:
            - '1:1'
            - '2:3'
            - '3:2'
            - '3:4'
            - '4:3'
            - '4:5'
            - '5:4'
            - '9:16'
            - '16:9'
            - '21:9'
          default: '1:1'
        resolution:
          type: string
          description: Output resolution preset (longest side in pixels)
          enum:
            - 1K
            - 2K
          default: 2K
      required:
        - prompt
      description: Text to image generation request body
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - task_id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana Pro Image Generation

> Generate ultra-sharp images from text prompts using the Gemini Nano-Banana Pro model

## Overview

Generate ultra-sharp, cinematic frames from short text prompts using Google's Gemini Nano Banana Pro model. Compared with the base Nano Banana release, the Pro tier unlocks:

* Wider aspect ratios (from square up to 21:9 panoramic)
* Higher fidelity presets (`resolution` up to 4K)
* Better prompt adherence thanks to an upgraded vision-language alignment stack


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-pro/openapi.yaml POST /vendors/google/v1/nano-banana-pro/generation
openapi: 3.1.0
info:
  title: Gemini Nano-Banana Pro API
  description: Gemini Nano-Banana Pro high-fidelity image APIs
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-pro/generation:
    post:
      summary: Text to Image Generation
      description: >-
        Generate ultra-sharp images from text prompts using the Gemini
        Nano-Banana Pro model
      operationId: nano_banana_pro_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerationRequest'
            example:
              prompt: A beautiful sunset over the mountains
              aspect_ratio: '5:4'
              resolution: 2K
        required: true
      responses:
        '202':
          description: Task created successfully
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                properties:
                  task_info:
                    $ref: '#/components/schemas/TaskInfoResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: pending
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
components:
  schemas:
    GenerationRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text prompt for image generation
        aspect_ratio:
          type: string
          description: Aspect ratio of the generated image
          enum:
            - '1:1'
            - '2:3'
            - '3:2'
            - '3:4'
            - '4:3'
            - '4:5'
            - '5:4'
            - '9:16'
            - '16:9'
            - '21:9'
          default: '1:1'
        resolution:
          type: string
          description: Output resolution preset (longest side in pixels)
          enum:
            - 1K
            - 2K
          default: 2K
      required:
        - prompt
      description: Text to image generation request body
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - task_id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana Pro Image Edit

> Edit images based on text prompts using Gemini Nano-Banana Pro model

## Overview

Nano Banana Pro can restyle or surgically modify a reference image while maintaining global composition. Provide one or more images plus a short instruction—Pro's upgraded diffusion backbone keeps lighting, textures, and edge fidelity intact.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-pro/openapi.yaml POST /vendors/google/v1/nano-banana-pro/edit
openapi: 3.1.0
info:
  title: Gemini Nano-Banana Pro API
  description: Gemini Nano-Banana Pro high-fidelity image APIs
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-pro/edit:
    post:
      summary: Image to Image Edit
      description: Edit images based on text prompts using Gemini Nano-Banana Pro model
      operationId: nano_banana_pro_edit
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditRequest'
            example:
              prompt: >-
                make a photo of the man driving the car down the california
                coastline
              images:
                - https://example.com/image.png
                - https://example.com/image2.png
              aspect_ratio: '5:4'
              resolution: 2K
        required: true
      responses:
        '202':
          description: Task created successfully
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                properties:
                  task_info:
                    $ref: '#/components/schemas/TaskInfoResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: pending
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
components:
  schemas:
    EditRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text prompt for image editing
        images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 10
          description: >-
            List of images to edit. Supports both image URLs and base64-encoded
            images (minimum 1, maximum 14). Base64 encoded image data is like
            "data:image/png;base64,iVBORw0KGgoAAAA..."
        aspect_ratio:
          type: string
          description: Aspect ratio of the edited image
          enum:
            - '1:1'
            - '2:3'
            - '3:2'
            - '3:4'
            - '4:3'
            - '4:5'
            - '5:4'
            - '9:16'
            - '16:9'
            - '21:9'
          default: '1:1'
        resolution:
          type: string
          description: Output resolution preset (longest side in pixels)
          enum:
            - 1K
            - 2K
          default: 2K
      required:
        - prompt
        - images
      description: Image to image edit request body
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - task_id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana Pro Edit Task

> Get the result of an image to image edit task

Use this endpoint to poll an in-flight Nano Banana Pro image-edit task until it finishes and returns the edited image URLs.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-pro/openapi.yaml GET /vendors/google/v1/nano-banana-pro/edit/{task_id}
openapi: 3.1.0
info:
  title: Gemini Nano-Banana Pro API
  description: Gemini Nano-Banana Pro high-fidelity image APIs
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-pro/edit/{task_id}:
    get:
      summary: Get Image to Image Edit Task
      description: Get the result of an image to image edit task
      operationId: nano_banana_pro_edit_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EditResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: completed
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
                images:
                  - https://example.com/image.png
                description: A beautiful sunset over the mountains
components:
  schemas:
    EditResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          items:
            type: string
            description: URL of the edited image
            format: uri
          description: List of edited image URLs
        description:
          type: string
          description: Model generated description of the edited image
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - task_id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana Pro Edit Task

> Get the result of an image to image edit task

Use this endpoint to poll an in-flight Nano Banana Pro image-edit task until it finishes and returns the edited image URLs.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-pro/openapi.yaml GET /vendors/google/v1/nano-banana-pro/edit/{task_id}
openapi: 3.1.0
info:
  title: Gemini Nano-Banana Pro API
  description: Gemini Nano-Banana Pro high-fidelity image APIs
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-pro/edit/{task_id}:
    get:
      summary: Get Image to Image Edit Task
      description: Get the result of an image to image edit task
      operationId: nano_banana_pro_edit_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EditResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: completed
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
                images:
                  - https://example.com/image.png
                description: A beautiful sunset over the mountains
components:
  schemas:
    EditResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          items:
            type: string
            description: URL of the edited image
            format: uri
          description: List of edited image URLs
        description:
          type: string
          description: Model generated description of the edited image
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2025-09-21T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - task_id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana 2 Image Generation

> Generate images from text prompts using the Google Nano Banana 2 model (Gemini 3.1 Flash Image Preview).
Supports up to 4K resolution output and 14 different aspect ratios.

## Overview

Generate high-quality images from text prompts using Google's Nano Banana 2 model (Gemini 3.1 Flash Image Preview). Compared with the base Nano Banana release, Nano Banana 2 unlocks:

* 14 aspect ratios (from 1:4 portrait up to 21:9 panoramic)
* Higher fidelity presets (`resolution` up to 4K)
* Web search grounding for real-time data and accurate depictions of real-world subjects


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-2/openapi.yaml POST /vendors/google/v1/nano-banana-2/generation
openapi: 3.1.0
info:
  title: Google Nano Banana 2 Image Generation API
  description: >-
    Google Nano Banana 2 (Gemini 3.1 Flash Image Preview) Image Generation and
    Editing API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-2/generation:
    post:
      summary: Text to Image Generation
      description: >-
        Generate images from text prompts using the Google Nano Banana 2 model
        (Gemini 3.1 Flash Image Preview).

        Supports up to 4K resolution output and 14 different aspect ratios.
      operationId: nano_banana_2_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerationRequest'
            example:
              prompt: >-
                A photorealistic close-up portrait of an elderly Japanese
                ceramicist with a warm, knowing smile
              aspect_ratio: '3:4'
              resolution: 2K
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                properties:
                  task_info:
                    $ref: '#/components/schemas/TaskInfoResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: pending
                  created_at: '2026-02-27T00:00:00.000Z'
                  updated_at: '2026-02-27T00:00:00.000Z'
components:
  schemas:
    GenerationRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text prompt for image generation. For best results, describe the
            scene narratively rather than listing keywords.


            Include details such as:

            - Subject (object, person, animal, scenery)

            - Style (photorealistic, illustration, sketch, etc.)

            - Lighting and mood

            - Camera angle and composition

            - Color palette


            Example: "A photorealistic close-up portrait of an elderly Japanese
            ceramicist with deep, sun-etched wrinkles and a warm, knowing smile.
            Captured with an 85mm portrait lens, resulting in soft bokeh."
        aspect_ratio:
          type: string
          description: Aspect ratio of the generated image (width:height).
          default: '1:1'
          enum:
            - '1:1'
            - '1:4'
            - '1:8'
            - '2:3'
            - '3:2'
            - '3:4'
            - '4:1'
            - '4:3'
            - '4:5'
            - '5:4'
            - '8:1'
            - '9:16'
            - '16:9'
            - '21:9'
        resolution:
          type: string
          description: >-
            Output resolution preset.


            **Note:** Must use uppercase K (e.g. 1K, 2K, 4K). Lowercase will be
            rejected.
          default: 1K
          enum:
            - 1K
            - 2K
            - 4K
        web_search:
          type: boolean
          description: >-
            Enable Google Search grounding for image generation. When enabled,
            the model can use Google Search (including Web Search and Image
            Search) to verify facts and generate imagery based on real-time data
            such as current weather, stock charts, recent events, or accurate
            depictions of real-world subjects.
          default: false
      required:
        - prompt
      description: Text to image generation request body
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana 2 Generation Task

> Retrieve the status and result of a Nano Banana 2 text-to-image generation task

Retrieve the status and final images for a Nano Banana 2 text-to-image generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-2/openapi.yaml GET /vendors/google/v1/nano-banana-2/generation/{task_id}
openapi: 3.1.0
info:
  title: Google Nano Banana 2 Image Generation API
  description: >-
    Google Nano Banana 2 (Gemini 3.1 Flash Image Preview) Image Generation and
    Editing API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-2/generation/{task_id}:
    get:
      summary: Get Text to Image Generation Task
      description: >-
        Retrieve the status and result of a Nano Banana 2 text-to-image
        generation task
      operationId: nano_banana_2_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerationResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: completed
                  created_at: '2026-02-27T00:00:00.000Z'
                  updated_at: '2026-02-27T00:00:30.000Z'
                images:
                  - >-
                    https://mulerouter.muleusercontent.com/public/123e4567-e89b-12d3-a456-426614174000/image.png
                description: A photorealistic portrait of an elderly Japanese ceramicist
components:
  schemas:
    GenerationResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          items:
            type: string
            description: URL of the generated image
            format: uri
          description: List of generated image URLs (only present when status is completed)
        description:
          type: string
          description: Model generated description of the image
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana 2 Image Edit

> Edit images based on text prompts using the Google Nano Banana 2 model.
Supports up to 14 reference images (10 object images + 4 character images).

## Overview

Nano Banana 2 can restyle or surgically modify a reference image while maintaining global composition. Provide up to 14 reference images (10 object + 4 character) plus a short instruction—Nano Banana 2's upgraded diffusion backbone keeps lighting, textures, and edge fidelity intact.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-2/openapi.yaml POST /vendors/google/v1/nano-banana-2/edit
openapi: 3.1.0
info:
  title: Google Nano Banana 2 Image Generation API
  description: >-
    Google Nano Banana 2 (Gemini 3.1 Flash Image Preview) Image Generation and
    Editing API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-2/edit:
    post:
      summary: Image to Image Edit
      description: >-
        Edit images based on text prompts using the Google Nano Banana 2 model.

        Supports up to 14 reference images (10 object images + 4 character
        images).
      operationId: nano_banana_2_edit
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditRequest'
            example:
              prompt: >-
                Add a small knitted wizard hat on the cat's head, make it look
                natural
              images:
                - https://example.com/cat_photo.png
              aspect_ratio: '1:1'
              resolution: 2K
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
                properties:
                  task_info:
                    $ref: '#/components/schemas/TaskInfoResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: pending
                  created_at: '2026-02-27T00:00:00.000Z'
                  updated_at: '2026-02-27T00:00:00.000Z'
components:
  schemas:
    EditRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text prompt for image editing. Describe the desired change
            conversationally.


            For adding/removing elements: "Add a wizard hat on the cat's head"

            For inpainting: "Change only the blue sofa to a brown leather
            chesterfield"

            For style transfer: "Transform this photo into Van Gogh's Starry
            Night style"
        images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 14
          description: >-
            List of reference images for editing. Supports both image URLs and
            base64-encoded images.


            Base64 format: `data:image/png;base64,{base64_data}`


            Supported formats: JPEG, JPG, PNG, BMP, WEBP

            Max file size per image: 20MB


            Nano Banana 2 supports up to 14 reference images:

            - Up to 10 images of objects (high-fidelity preservation)

            - Up to 4 images of characters (character consistency)
        aspect_ratio:
          type: string
          description: Aspect ratio of the edited image (width:height).
          default: '1:1'
          enum:
            - '1:1'
            - '1:4'
            - '1:8'
            - '2:3'
            - '3:2'
            - '3:4'
            - '4:1'
            - '4:3'
            - '4:5'
            - '5:4'
            - '8:1'
            - '9:16'
            - '16:9'
            - '21:9'
        resolution:
          type: string
          description: >-
            Output resolution preset.


            **Note:** Must use uppercase K (e.g. 1K, 2K, 4K). Lowercase will be
            rejected.
          default: 1K
          enum:
            - 1K
            - 2K
            - 4K
        web_search:
          type: boolean
          description: >-
            Enable Google Search grounding for image editing. When enabled, the
            model can use Google Search (including Web Search and Image Search)
            to verify facts and generate imagery based on real-time data such as
            current weather, stock charts, recent events, or accurate depictions
            of real-world subjects.
          default: false
      required:
        - prompt
        - images
      description: Image to image edit request body
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 🍌 Nano Banana 2 Edit Task

> Retrieve the status and result of a Nano Banana 2 image edit task

Use this endpoint to poll an in-flight Nano Banana 2 image-edit task until it finishes and returns the edited image URLs.


## OpenAPI

````yaml /api-reference/endpoint/google/nano-banana-2/openapi.yaml GET /vendors/google/v1/nano-banana-2/edit/{task_id}
openapi: 3.1.0
info:
  title: Google Nano Banana 2 Image Generation API
  description: >-
    Google Nano Banana 2 (Gemini 3.1 Flash Image Preview) Image Generation and
    Editing API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/google/v1/nano-banana-2/edit/{task_id}:
    get:
      summary: Get Image to Image Edit Task
      description: Retrieve the status and result of a Nano Banana 2 image edit task
      operationId: nano_banana_2_edit_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EditResponse'
              example:
                task_info:
                  id: 123e4567-e89b-12d3-a456-426614174000
                  status: completed
                  created_at: '2026-02-27T00:00:00.000Z'
                  updated_at: '2026-02-27T00:00:30.000Z'
                images:
                  - >-
                    https://mulerouter.muleusercontent.com/public/123e4567-e89b-12d3-a456-426614174000/image.png
                description: A cat wearing a knitted wizard hat
components:
  schemas:
    EditResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          items:
            type: string
            description: URL of the edited image
            format: uri
          description: List of edited image URLs (only present when status is completed)
        description:
          type: string
          description: Model generated description of the edited image
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
          example: '2026-02-27T00:00:00.000Z'
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Diffusion

> Image Generation - Text to Image

<Note>
  The `prompt` parameter is compatible with Midjourney's format. Please refer to Midjourney's [official documentation](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List) for more details.
</Note>

## Pricing

| Task Name | Mode               |            Pricing |
| :-------- | :----------------- | -----------------: |
| Diffusion | Fast Mode          |  0.085\$ Per Image |
|           | Turbo Mode         |   0.17\$ Per Image |
|           | Draft Mode (Fast)  | 0.0425\$ Per Image |
|           | Draft Mode (Turbo) |  0.085\$ Per Image |


## OpenAPI

````yaml /api-reference/endpoint/midjourney/midjourney.yaml POST /vendors/midjourney/v1/tob/diffusion
openapi: 3.1.0
info:
  title: Midjourney API
  description: Midjourney Image and Video Generation API
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/midjourney/v1/tob/diffusion:
    post:
      summary: Text to Image
      description: Image Generation - Text to Image
      operationId: diffusion_text2image
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DiffusionRequest'
            example:
              prompt: >-
                A delicious-looking molten chocolate lava cake that has been cut
                open.
        required: true
      responses:
        '202':
          description: Task accepted and queued for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DiffusionTaskResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
components:
  schemas:
    DiffusionRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text prompt for image generation. Must be between 1 and 8192
            characters. This prompt is compatible with Midjourney's format.
          minLength: 1
          maxLength: 8192
      required:
        - prompt
      description: Text to Image generation request body
    DiffusionTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
      required:
        - task_info
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT Image 2 Image Generation

> Generate images from a text prompt using GPT Image 2.

## Overview

Generate high-quality images from text prompts using OpenAI's GPT Image 2 model. Supports multiple resolutions up to 4K, four quality tiers, and PNG / JPEG / WebP output — with up to 4 images per request.


## OpenAPI

````yaml /api-reference/endpoint/openai/gpt-image-2/openapi.yaml POST /vendors/openai/v1/gpt-image-2/generation
openapi: 3.1.0
info:
  title: GPT Image 2 Generation & Edit API
  description: Generate and edit images using the GPT Image 2 model via MuleRouter.
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/openai/v1/gpt-image-2/generation:
    post:
      summary: Text to Image
      description: Generate images from a text prompt using GPT Image 2.
      operationId: gpt_image_2_generation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerationRequest'
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    GenerationRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          minLength: 1
          description: Text prompt to guide image generation.
        quality:
          type: string
          description: Image quality level.
          enum:
            - high
            - medium
            - low
            - auto
          default: high
        size:
          $ref: '#/components/schemas/SizeEnum'
        'n':
          type: integer
          description: Number of images to generate.
          minimum: 1
          maximum: 4
          default: 1
        format:
          $ref: '#/components/schemas/FormatEnum'
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    SizeEnum:
      type: string
      description: Output image resolution.
      enum:
        - 1024x1024
        - 1536x1024
        - 1024x1536
        - 2048x2048
        - 2048x1152
        - 3840x2160
        - 2160x3840
        - auto
      default: auto
    FormatEnum:
      type: string
      description: Output image format.
      enum:
        - png
        - jpeg
        - webp
      default: png
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - pending
          description: Task status (pending when created)
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT Image 2 Generation Task

> Retrieve the status and result of a generation task.

Retrieve the status and final images for a GPT Image 2 generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/openai/gpt-image-2/openapi.yaml GET /vendors/openai/v1/gpt-image-2/generation/{task_id}
openapi: 3.1.0
info:
  title: GPT Image 2 Generation & Edit API
  description: Generate and edit images using the GPT Image 2 model via MuleRouter.
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/openai/v1/gpt-image-2/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task.
      operationId: gpt_image_2_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ImageResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated/edited image URLs (only present when status is completed)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
          description: Task status
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - failed
          description: Task status (always failed for error responses)
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT Image 2 Image Edit

> Edit images using a text prompt and optional mask with GPT Image 2.

## Overview

Edit existing images using a text prompt with GPT Image 2. Pass one or more input images (URL or Base64) and an optional mask to constrain the edit region. Supports up to 4K output and batch generation of 1–4 edited images per request.


## OpenAPI

````yaml /api-reference/endpoint/openai/gpt-image-2/openapi.yaml POST /vendors/openai/v1/gpt-image-2/edit
openapi: 3.1.0
info:
  title: GPT Image 2 Generation & Edit API
  description: Generate and edit images using the GPT Image 2 model via MuleRouter.
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/openai/v1/gpt-image-2/edit:
    post:
      summary: Image Edit
      description: Edit images using a text prompt and optional mask with GPT Image 2.
      operationId: gpt_image_2_edit
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditRequest'
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    EditRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          minLength: 1
          description: Text prompt describing the desired edit.
        images:
          type: array
          description: Input images to edit. Each item is a URL or Base64-encoded string.
          items:
            type: string
          minItems: 1
        size:
          $ref: '#/components/schemas/SizeEnum'
        'n':
          type: integer
          description: Number of edited images to generate.
          minimum: 1
          maximum: 4
          default: 1
        mask:
          type: string
          description: >-
            Optional mask image (URL or Base64-encoded) to specify the edit
            region.
        format:
          $ref: '#/components/schemas/FormatEnum'
      required:
        - prompt
        - images
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    SizeEnum:
      type: string
      description: Output image resolution.
      enum:
        - 1024x1024
        - 1536x1024
        - 1024x1536
        - 2048x2048
        - 2048x1152
        - 3840x2160
        - 2160x3840
        - auto
      default: auto
    FormatEnum:
      type: string
      description: Output image format.
      enum:
        - png
        - jpeg
        - webp
      default: png
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - pending
          description: Task status (pending when created)
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT Image 2 Edit Task

> Retrieve the status and result of an edit task.

Use this endpoint to poll an in-flight GPT Image 2 image-edit task until it finishes and returns the edited image URLs.


## OpenAPI

````yaml /api-reference/endpoint/openai/gpt-image-2/openapi.yaml GET /vendors/openai/v1/gpt-image-2/edit/{task_id}
openapi: 3.1.0
info:
  title: GPT Image 2 Generation & Edit API
  description: Generate and edit images using the GPT Image 2 model via MuleRouter.
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/openai/v1/gpt-image-2/edit/{task_id}:
    get:
      summary: Get Edit Task
      description: Retrieve the status and result of an edit task.
      operationId: gpt_image_2_edit_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ImageResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        images:
          type: array
          description: Generated/edited image URLs (only present when status is completed)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
          description: Task status
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
          description: UUID of the task
        status:
          type: string
          enum:
            - failed
          description: Task status (always failed for error responses)
        created_at:
          type: string
          format: date-time
          description: Task creation timestamp (ISO 8601)
        updated_at:
          type: string
          format: date-time
          description: Task last update timestamp (ISO 8601)
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Video Generation

> Generate videos from text prompts using the wan2.6-t2v model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from text prompts using the wan2.6-t2v model with support for longer durations and multi-shot generation.

## Key Features

* Text-to-video generation with audio support
* Multiple resolution options (720P/1080P)
* 5s, 10s, or 15s duration
* Single or multi-shot generation

## Resolution Options

### 720P

* 1280×720 (16:9)
* 720×1280 (9:16)
* 960×960 (1:1)
* 1088×832 (4:3)
* 832×1088 (3:4)

### 1080P

* 1920×1080 (16:9)
* 1080×1920 (9:16)
* 1440×1440 (1:1)
* 1632×1248 (4:3)
* 1248×1632 (3:4)

## Example Requests

### Basic Text-to-Video

```json theme={null}
{
  "prompt": "Miyazaki-style mule dancing",
  "size": "1280*720",
  "duration": 5
}
```

### Multi-shot Video

```json theme={null}
{
  "prompt": "Waves crashing against rocks, water splashing, sunlight on the sea",
  "size": "1920*1080",
  "duration": 10,
  "prompt_extend": true,
  "shot_type": "multi",
  "audio": true
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "A person walking through a city at night",
  "size": "1280*720",
  "duration": 15,
  "audio_url": "https://example.com/city_sounds.mp3"
}
```

## Parameters

### shot\_type

* **Default**: single
* **Effect**: When prompt rewriting is enabled, controls whether the output is single-shot or multi-shot
* **Only effective when**: `prompt_extend` is enabled

### duration

* **Options**: 5, 10, or 15 seconds
* **Note**: Longer durations may increase processing time


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-t2v/wan2.6-t2v.yaml POST /vendors/alibaba/v1/wan2.6-t2v/generation
openapi: 3.1.0
info:
  title: Wan2.6-t2v API
  description: Wan2.6 Text-to-Video Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-t2v/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from text prompts using the wan2.6-t2v model.
      operationId: wan26_t2v_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26T2VRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26T2VRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text description for the desired video content (max 2000
            characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        size:
          type: string
          description: >-
            Output resolution ("width\*height"). Supported tiers:

            - 720P: 1280\*720 (16:9), 720\*1280 (9:16), 960\*960 (1:1),
            1088\*832 (4:3), 832\*1088 (3:4)

            - 1080P: 1920\*1080 (16:9), 1080\*1920 (9:16), 1440\*1440 (1:1),
            1632\*1248 (4:3), 1248\*1632 (3:4)
          enum:
            - 1280*720
            - 720*1280
            - 960*960
            - 1088*832
            - 832*1088
            - 1920*1080
            - 1080*1920
            - 1440*1440
            - 1632*1248
            - 1248*1632
          default: 1280*720
        duration:
          type: integer
          description: Video duration in seconds. Supported values 5, 10, or 15.
          enum:
            - 5
            - 10
            - 15
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        shot_type:
          anyOf:
            - type: string
              enum:
                - single
                - multi
            - type: 'null'
          description: |-
            Specifies the shot type for video generation.

            Only takes effect when prompt_extend is enabled.

            - single: Default value, outputs single-shot video
            - multi: Outputs multi-shot video
          default: single
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Video Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-t2v generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:33:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-t2v/wan2.6-t2v.yaml GET /vendors/alibaba/v1/wan2.6-t2v/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-t2v API
  description: Wan2.6 Text-to-Video Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-t2v/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_t2v_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26T2VResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26T2VResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Video Generation

> Generate videos from images using the wan2.6-i2v model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from images using the wan2.6-i2v model with support for longer durations, multi-shot generation, and optional last frame specification.

## Key Features

* Image-to-video generation with audio support
* Multiple resolution options (720P/1080P)
* 5s, 10s, or 15s duration
* Single or multi-shot generation
* Optional first and last frame specification

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "A black cat looks curiously at the sky, camera gradually rises from eye-level to overhead",
  "image": "https://example.com/first_frame.jpg",
  "resolution": "720P",
  "duration": 5
}
```

### With Last Frame (Interpolation)

```json theme={null}
{
  "prompt": "Character starts walking, expression changes naturally",
  "image": "https://example.com/person.jpg",
  "last_frame": "https://example.com/person_end.jpg",
  "resolution": "1080P",
  "duration": 10,
  "audio": true
}
```

### Multi-shot Video

```json theme={null}
{
  "prompt": "Scene transition with smooth camera movement",
  "image": "https://example.com/scene.jpg",
  "resolution": "1080P",
  "duration": 15,
  "prompt_extend": true,
  "multi_shots": "multi"
}
```

## Parameters

### last\_frame

* **Optional**: Yes
* **Description**: End frame image for video interpolation between first and last frame
* **Use case**: Create smooth transitions between two specific frames

### multi\_shots

* **Default**: single
* **Effect**: When prompt rewriting is enabled, controls whether the output is single-shot or multi-shot
* **Only effective when**: `prompt_extend` is enabled


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-i2v/wan2.6-i2v.yaml POST /vendors/alibaba/v1/wan2.6-i2v/generation
openapi: 3.1.0
info:
  title: Wan2.6-i2v API
  description: Wan2.6 Image-to-Video Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-i2v/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from images using the wan2.6-i2v model.
      operationId: wan26_i2v_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26I2VRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26I2VRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description for the video (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 720P
            - 1080P
          enum:
            - 720P
            - 1080P
          default: 720P
        duration:
          type: integer
          description: Video duration in seconds. Supported values 5, 10, or 15.
          enum:
            - 5
            - 10
            - 15
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        shot_type:
          anyOf:
            - type: string
              enum:
                - single
                - multi
            - type: 'null'
          description: |-
            Specifies the shot type for video generation.

            Only takes effect when prompt_extend is enabled.

            - single: Default value, outputs single-shot video
            - multi: Outputs multi-shot video
          default: single
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Video Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-i2v generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:33:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.6-i2v/wan2.6-i2v.yaml GET /vendors/alibaba/v1/wan2.6-i2v/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-i2v API
  description: Wan2.6 Image-to-Video Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.6-i2v/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_i2v_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26I2VResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26I2VResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Video Preview Generation

> Generate videos from text prompts using the wan2.5-t2v-preview model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from text prompts using the wan2.5-t2v-preview model with optional audio generation.

## Key Features

* Text-to-video generation with auto sound or custom audio
* Multiple resolution options (480P/720P/1080P)
* 5s or 10s duration
* 24fps output

## Resolution Options

### 480P

* 832×480 (16:9)
* 480×832 (9:16)
* 624×624 (1:1)

### 720P

* 1280×720 (16:9)
* 720×1280 (9:16)
* 960×960 (1:1)
* 1088×832 (4:3)
* 832×1088 (3:4)

### 1080P

* 1920×1080 (16:9)
* 1080×1920 (9:16)
* 1440×1440 (1:1)
* 1632×1248 (4:3)
* 1248×1632 (3:4)

## Audio Features

### Auto-generated Audio

* Enabled by default
* Automatically generates synchronized audio based on video content

### Custom Audio

* Supported formats: WAV, MP3
* Duration: 3-30 seconds
* Max file size: 15MB
* **Behavior**: If audio is shorter than video, remaining portion is silent; if longer, it's truncated

## Example Requests

### Basic Text-to-Video

```json theme={null}
{
  "prompt": "A small cat running on a grassy field in the moonlight",
  "size": "1920*1080",
  "duration": 10,
  "audio": true
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "A person walking through a forest, birds chirping",
  "audio_url": "https://example.com/forest_sounds.mp3",
  "size": "1920*1080",
  "duration": 10
}
```

### Silent Video

```json theme={null}
{
  "prompt": "City night scene timelapse, flowing traffic, brilliant lights",
  "size": "1280*720",
  "duration": 5,
  "audio": false
}
```

## Prompt Tips

For best results when describing motion:

* Specify camera movement (pan left, zoom in, dolly shot)
* Describe subject motion (walks forward, turns around)
* Include environment details (windy, foggy, sunlit)


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-t2v-preview/wan2.5-t2v-preview.yaml POST /vendors/alibaba/v1/wan2.5-t2v-preview/generation
openapi: 3.1.0
info:
  title: Wan2.5-t2v-preview API
  description: Wan2.5 Text-to-Video Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-t2v-preview/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from text prompts using the wan2.5-t2v-preview model.
      operationId: wan25_t2v_preview_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25T2VPreviewRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25T2VPreviewRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text description for the desired video content (max 2000
            characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        size:
          type: string
          description: >-
            Output resolution ("width\*height"). Supported tiers:

            - 480P: 832\*480 (16:9), 480\*832 (9:16), 624\*624 (1:1)

            - 720P: 1280\*720 (16:9), 720\*1280 (9:16), 960\*960 (1:1),
            1088\*832 (4:3), 832\*1088 (3:4)

            - 1080P: 1920\*1080 (16:9), 1080\*1920 (9:16), 1440\*1440 (1:1),
            1632\*1248 (4:3), 1248\*1632 (3:4)
          enum:
            - 832*480
            - 480*832
            - 624*624
            - 1280*720
            - 720*1280
            - 960*960
            - 1088*832
            - 832*1088
            - 1920*1080
            - 1080*1920
            - 1440*1440
            - 1632*1248
            - 1248*1632
          default: 1280*720
        duration:
          type: integer
          description: Video duration in seconds (24 fps). Supported values 5 or 10.
          enum:
            - 5
            - 10
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Video Preview Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-t2v-preview generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-t2v-preview/wan2.5-t2v-preview.yaml GET /vendors/alibaba/v1/wan2.5-t2v-preview/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-t2v-preview API
  description: Wan2.5 Text-to-Video Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-t2v-preview/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_t2v_preview_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25T2VPreviewResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25T2VPreviewResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Video Preview Generation

> Generate videos from images using the wan2.5-i2v-preview model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from images using the wan2.5-i2v-preview model with optional audio generation.

## Key Features

* Image-to-video generation with auto sound or custom audio
* Multiple resolution options (480P/720P/1080P)
* 5s or 10s duration
* 24fps output

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Audio Features

### Auto-generated Audio

* Enabled by default
* Automatically generates synchronized audio based on video content

### Custom Audio

* Supported formats: WAV, MP3
* Duration: 3-30 seconds
* Max file size: 15MB

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "The cat starts running forward",
  "image": "https://example.com/cat.jpg",
  "resolution": "720P",
  "duration": 5
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "Scene becomes dynamic, clouds drifting",
  "image": "https://example.com/landscape.jpg",
  "audio_url": "https://example.com/ambient.mp3",
  "resolution": "1080P",
  "duration": 10
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Character turns head and smiles",
  "image": "https://example.com/portrait.jpg",
  "negative_prompt": "shaking, distortion",
  "resolution": "720P",
  "duration": 5
}
```

## Prompt Tips

For best results:

* Describe the motion/story you want to see
* Specify camera movements if needed
* Include transition descriptions


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-i2v-preview/wan2.5-i2v-preview.yaml POST /vendors/alibaba/v1/wan2.5-i2v-preview/generation
openapi: 3.1.0
info:
  title: Wan2.5-i2v-preview API
  description: Wan2.5 Image-to-Video Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-i2v-preview/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from images using the wan2.5-i2v-preview model.
      operationId: wan25_i2v_preview_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25I2VPreviewRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25I2VPreviewRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description for the video (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 480P
            - 720P
            - 1080P
          enum:
            - 480P
            - 720P
            - 1080P
          default: 720P
        duration:
          type: integer
          description: Video duration in seconds (24 fps). Supported values 5 or 10.
          enum:
            - 5
            - 10
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Video Preview Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-i2v-preview generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.5-i2v-preview/wan2.5-i2v-preview.yaml GET /vendors/alibaba/v1/wan2.5-i2v-preview/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-i2v-preview API
  description: Wan2.5 Image-to-Video Preview Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.5-i2v-preview/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_i2v_preview_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25I2VPreviewResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25I2VPreviewResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Text-To-Video Plus Generation

> Generate videos from text prompts using the wan2.2-t2v-plus model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from text prompts using the wan2.2-t2v-plus model. This is the Plus version with enhanced stability.

## Key Features

* Text-to-video generation
* 480P or 1080P resolution options
* Fixed 5s duration
* 30fps output

## Resolution Options

### 480P

* 832×480 (16:9)
* 480×832 (9:16)
* 624×624 (1:1)

### 1080P

* 1920×1080 (16:9)
* 1080×1920 (9:16)
* 1440×1440 (1:1)
* 1632×1248 (4:3)
* 1248×1632 (3:4)

## Example Requests

### Basic Text-to-Video

```json theme={null}
{
  "prompt": "A small cat running in the moonlight, slow motion close-up",
  "size": "1920*1080",
  "duration": 5
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Sunset over the ocean, waves crashing on the shore",
  "negative_prompt": "blurry, low quality",
  "size": "1280*720",
  "duration": 5
}
```

## Parameters

### duration

* **Fixed**: 5 seconds
* **FPS**: 30fps

### prompt

* **Max length**: 800 characters (shorter than Wan2.5/2.6 models)


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-t2v-plus/wan2.2-t2v-plus.yaml POST /vendors/alibaba/v1/wan2.2-t2v-plus/generation
openapi: 3.1.0
info:
  title: Wan2.2-t2v-plus API
  description: Wan2.2 Text-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-t2v-plus/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from text prompts using the wan2.2-t2v-plus model.
      operationId: wan22_t2v_plus_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan22T2VPlusRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan22T2VPlusRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Text prompt for the video (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        size:
          type: string
          description: >-
            Output resolution ("width\*height"). Supported tiers:

            - 480P: 832\*480 (16:9), 480\*832 (9:16), 624\*624 (1:1)

            - 1080P: 1920\*1080 (16:9), 1080\*1920 (9:16), 1440\*1440 (1:1),
            1632\*1248 (4:3), 1248\*1632 (3:4)
          enum:
            - 832*480
            - 480*832
            - 624*624
            - 1920*1080
            - 1080*1920
            - 1440*1440
            - 1632*1248
            - 1248*1632
          default: 1920*1080
        duration:
          type: integer
          description: Video duration in seconds (30 fps). Fixed at 5 seconds.
          enum:
            - 5
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting.
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Text-To-Video Plus Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.2-t2v-plus generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-t2v-plus/wan2.2-t2v-plus.yaml GET /vendors/alibaba/v1/wan2.2-t2v-plus/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.2-t2v-plus API
  description: Wan2.2 Text-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-t2v-plus/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan22_t2v_plus_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan22T2VPlusResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan22T2VPlusResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Image-To-Video Plus Generation

> Generate videos from images using the wan2.2-i2v-plus model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from images using the wan2.2-i2v-plus model. This is the professional version with enhanced stability.

## Key Features

* Image-to-video generation
* 480P or 1080P resolution options
* Fixed 5s duration
* 30fps output
* Optional first and last frame specification

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "Flowers swaying in the wind",
  "image": "https://example.com/flower.jpg",
  "resolution": "1080P",
  "duration": 5
}
```

### With Last Frame

```json theme={null}
{
  "prompt": "Smooth transition between two scenes",
  "image": "https://example.com/start.jpg",
  "last_frame": "https://example.com/end.jpg",
  "resolution": "1080P",
  "duration": 5
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Character turns head and smiles",
  "image": "https://example.com/portrait.jpg",
  "negative_prompt": "static, blurry",
  "resolution": "720P",
  "duration": 5
}
```

## Parameters

### duration

* **Fixed**: 5 seconds
* **FPS**: 30fps

### prompt

* **Max length**: 800 characters


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-i2v-plus/wan2.2-i2v-plus.yaml POST /vendors/alibaba/v1/wan2.2-i2v-plus/generation
openapi: 3.1.0
info:
  title: Wan2.2-i2v-plus API
  description: Wan2.2 Image-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-i2v-plus/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from images using the wan2.2-i2v-plus model.
      operationId: wan22_i2v_plus_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan22I2VPlusRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan22I2VPlusRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 480P
            - 1080P
          enum:
            - 480P
            - 1080P
          default: 1080P
        duration:
          type: integer
          description: Video duration in seconds (30 fps). Fixed at 5 seconds.
          enum:
            - 5
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting.
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Image-To-Video Plus Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.2-i2v-plus generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-i2v-plus/wan2.2-i2v-plus.yaml GET /vendors/alibaba/v1/wan2.2-i2v-plus/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.2-i2v-plus API
  description: Wan2.2 Image-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-i2v-plus/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan22_i2v_plus_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan22I2VPlusResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan22I2VPlusResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Image-To-Video Flash Generation

> Generate videos from images using the wan2.2-i2v-flash model. Fast version with 50% speed improvement.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from images using the wan2.2-i2v-flash model. This is the fast version with 50% speed improvement compared to the Plus version.

## Key Features

* Fast image-to-video generation (50% faster)
* 480P/720P resolution options
* Fixed 5s duration
* 30fps output
* Optional video effect templates

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "Character turns head and smiles",
  "image": "https://example.com/portrait.jpg",
  "resolution": "720P",
  "duration": 5
}
```

### With Video Effect Template

```json theme={null}
{
  "prompt": "Gentle motion, camera slowly pans right",
  "image": "https://example.com/scene.jpg",
  "template": "solaron",
  "resolution": "720P",
  "duration": 5
}
```

### With Base64 Image

```json theme={null}
{
  "prompt": "Subject starts moving slowly",
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
  "resolution": "720P",
  "duration": 5
}
```

## Parameters

### template

* **Optional**: Yes
* **Description**: Apply a video effect template
* **Use case**: Create specific visual effects

### duration

* **Fixed**: 5 seconds
* **FPS**: 30fps


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-i2v-flash/wan2.2-i2v-flash.yaml POST /vendors/alibaba/v1/wan2.2-i2v-flash/generation
openapi: 3.1.0
info:
  title: Wan2.2-i2v-flash API
  description: Wan2.2 Image-to-Video Flash Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-i2v-flash/generation:
    post:
      summary: Create Generation Task
      description: >-
        Generate videos from images using the wan2.2-i2v-flash model. Fast
        version with 50% speed improvement.
      operationId: wan22_i2v_flash_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan22I2VFlashRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan22I2VFlashRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 480P
            - 720P
          enum:
            - 480P
            - 720P
          default: 720P
        duration:
          type: integer
          description: Video duration in seconds (30 fps). Fixed at 5 seconds.
          enum:
            - 5
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting.
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Image-To-Video Flash Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.2-i2v-flash generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:31:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.2-i2v-flash/wan2.2-i2v-flash.yaml GET /vendors/alibaba/v1/wan2.2-i2v-flash/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.2-i2v-flash API
  description: Wan2.2 Image-to-Video Flash Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.2-i2v-flash/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan22_i2v_flash_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan22I2VFlashResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan22I2VFlashResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 Keyframe-To-Video Plus Generation

> Generate videos from first and last frame keyframes using the wan2.1-kf2v-plus model.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video generation models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Generate videos from first and last frame keyframes using the wan2.1-kf2v-plus model. This model creates smooth interpolation between two keyframe images.

## Key Features

* Keyframe-to-video interpolation
* First and last frame specification (required)
* 720P resolution
* Fixed 5s duration
* 30fps output

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Example Requests

### Basic Keyframe Interpolation

```json theme={null}
{
  "prompt": "A black cat looks curiously at the sky, camera gradually rises from eye-level to overhead",
  "image": "https://example.com/first_frame.jpg",
  "last_frame": "https://example.com/last_frame.jpg",
  "resolution": "720P",
  "duration": 5
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Character starts walking, motion is smooth and natural",
  "image": "https://example.com/start.jpg",
  "last_frame": "https://example.com/end.jpg",
  "negative_prompt": "shaking, distortion",
  "resolution": "720P",
  "duration": 5
}
```

### With Video Effect Template

```json theme={null}
{
  "prompt": "Scene transitions with special effects",
  "image": "https://example.com/keyframe1.jpg",
  "last_frame": "https://example.com/keyframe2.jpg",
  "template": "flying",
  "resolution": "720P"
}
```

## Prompt Tips

For best results when describing keyframe interpolation:

* Describe the transition between first and last frame
* Specify motion direction and camera movement
* Include timing cues if needed


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.1-kf2v-plus/wan2.1-kf2v-plus.yaml POST /vendors/alibaba/v1/wan2.1-kf2v-plus/generation
openapi: 3.1.0
info:
  title: Wan2.1-kf2v-plus API
  description: Wan2.1 Keyframe-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.1-kf2v-plus/generation:
    post:
      summary: Create Generation Task
      description: >-
        Generate videos from first and last frame keyframes using the
        wan2.1-kf2v-plus model.
      operationId: wan21_kf2v_plus_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan21KF2VPlusRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan21KF2VPlusRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Transition and motion description between the first and last frame
            (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First keyframe image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        last_frame:
          type: string
          description: >-
            Last keyframe image (URL or Base64). Same constraints as the first
            frame.
        template:
          anyOf:
            - type: string
            - type: 'null'
          description: Optional video effect template name.
        resolution:
          type: string
          description: Output Resolution
          enum:
            - 720P
          default: 720P
        duration:
          type: integer
          description: Video duration in seconds (30 fps). Fixed at 5 seconds.
          enum:
            - 5
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting.
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
        - last_frame
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 Keyframe-To-Video Plus Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.1-kf2v-plus generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.1-kf2v-plus/wan2.1-kf2v-plus.yaml GET /vendors/alibaba/v1/wan2.1-kf2v-plus/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.1-kf2v-plus API
  description: Wan2.1 Keyframe-to-Video Plus Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.1-kf2v-plus/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan21_kf2v_plus_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan21KF2VPlusResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan21KF2VPlusResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 Video Ace Plus Generation

> Edit videos using the wan2.1-vace-plus model with multi-modal inputs and various editing functions.

<Note>
  This API supports Alibaba Tongyi Wanxiang (Wan2) video editing models. Please refer to Alibaba Cloud's [official documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-video-api-reference) for more details.
</Note>

## Overview

Edit videos using the wan2.1-vace-plus model with multi-modal inputs. This model supports multiple video editing functions.

## Supported Functions

| Function            | Description                               |
| ------------------- | ----------------------------------------- |
| `image_reference`   | Generate videos from 1-3 reference images |
| `video_repainting`  | Repaint/restyle an existing video         |
| `video_edit`        | Local (masked) editing of video regions   |
| `video_extension`   | Extend video with new content             |
| `video_outpainting` | Expand video canvas in any direction      |

## Example Requests

### Multi-image Reference

```json theme={null}
{
  "function": "image_reference",
  "prompt": "A cat playing in the garden",
  "ref_images_url": [
    "https://example.com/cat.jpg",
    "https://example.com/garden.jpg"
  ],
  "obj_or_bg": ["obj", "bg"],
  "size": "1280*720",
  "duration": 5
}
```

### Video Repainting

```json theme={null}
{
  "function": "video_repainting",
  "prompt": "Transform the scene into a cyberpunk style",
  "video_url": "https://example.com/source.mp4",
  "control_condition": "depth",
  "strength": 0.8
}
```

### Local Editing

```json theme={null}
{
  "function": "video_edit",
  "prompt": "Replace the background with a beach sunset",
  "video_url": "https://example.com/source.mp4",
  "mask_image_url": "https://example.com/mask.png",
  "mask_type": "tracking"
}
```

### Video Extension

```json theme={null}
{
  "function": "video_extension",
  "prompt": "Continue the scene with the character walking forward",
  "first_clip_url": "https://example.com/clip.mp4",
  "duration": 5
}
```

### Video Outpainting

```json theme={null}
{
  "function": "video_outpainting",
  "prompt": "Expand to show more of the surrounding environment",
  "video_url": "https://example.com/source.mp4",
  "top_scale": 1.5,
  "left_scale": 1.3,
  "right_scale": 1.3
}
```

## Function Details

### image\_reference

* **Required**: `ref_images_url` (1-3 images)
* **Required when multiple images**: `obj_or_bg` array
* **Output**: 720P resolution, 5s duration

### video\_repainting

* **Required**: `video_url`, `control_condition`
* **Control conditions**: posebodyface, posebody, depth, scribble
* **Strength**: 0.0-1.0 (default 1.0)

### video\_edit

* **Required**: `video_url`
* **Mask options**: `mask_image_url` or `mask_video_url`
* **Mask types**: tracking (follows motion), fixed (static)

### video\_extension

* **Required**: `prompt`
* **Optional**: `first_frame_url`, `last_frame_url`, `first_clip_url`, `last_clip_url`
* **With guidance video**: requires `control_condition`

### video\_outpainting

* **Required**: `video_url`
* **Scale options**: `top_scale`, `bottom_scale`, `left_scale`, `right_scale` (1.0-2.0)

## Video Requirements

| Property         | Requirement |
| ---------------- | ----------- |
| **Format**       | MP4         |
| **Max size**     | 50MB        |
| **Min FPS**      | 16          |
| **Max duration** | 5s          |


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.1-vace-plus/wan2.1-vace-plus.yaml POST /vendors/alibaba/v1/wan2.1-vace-plus/generation
openapi: 3.1.0
info:
  title: Wan2.1-vace-plus API
  description: Wan2.1 VACE Plus Video Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.1-vace-plus/generation:
    post:
      summary: Create Generation Task
      description: >-
        Edit videos using the wan2.1-vace-plus model with multi-modal inputs and
        various editing functions.
      operationId: wan21_vace_plus_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VideoEditRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    VideoEditRequest:
      description: >-
        wan2.1-vace-plus video editing entry point. Select a function and supply
        the parameters supported by that function.
      oneOf:
        - $ref: '#/components/schemas/WanVideoEditImageReferenceRequest'
        - $ref: '#/components/schemas/WanVideoEditVideoRepaintingRequest'
        - $ref: '#/components/schemas/WanVideoEditLocalEditingRequest'
        - $ref: '#/components/schemas/WanVideoEditExtensionRequest'
        - $ref: '#/components/schemas/WanVideoEditOutpaintingRequest'
      discriminator:
        propertyName: function
        mapping:
          image_reference:
            $ref: '#/components/schemas/WanVideoEditImageReferenceRequest'
          video_repainting:
            $ref: '#/components/schemas/WanVideoEditVideoRepaintingRequest'
          video_edit:
            $ref: '#/components/schemas/WanVideoEditLocalEditingRequest'
          video_extension:
            $ref: '#/components/schemas/WanVideoEditExtensionRequest'
          video_outpainting:
            $ref: '#/components/schemas/WanVideoEditOutpaintingRequest'
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    WanVideoEditImageReferenceRequest:
      title: Multi-image Reference
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: Model name (only wan2.1-vace-plus is supported)
          enum:
            - wan2.1-vace-plus
        function:
          type: string
          const: image_reference
          enum:
            - image_reference
          description: Multi-image reference feature selector.
        prompt:
          type: string
          description: Text description for the synthesized video (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters).
          maxLength: 500
        ref_images_url:
          type: array
          minItems: 1
          maxItems: 3
          description: >-
            Public URLs for 1-3 reference images (JPG/JPEG/PNG/BMP/TIFF/WEBP,
            360-2000px, ≤10MB, ASCII URL). Required.
          items:
            type: string
            format: uri
        obj_or_bg:
          type: array
          description: >-
            Matches ref_images_url to label each image as entity ("obj") or
            background ("bg"). Required when multiple images are supplied;
            defaults to ["obj"] for a single image.
          items:
            type: string
            enum:
              - obj
              - bg
        size:
          description: >-
            Output resolution ("width\*height"). Supported: 1280\*720 (default),
            720\*1280, 960\*960, 832\*1088, 1088\*832.
          enum:
            - 1280*720
            - 720*1280
            - 960*960
            - 832*1088
            - 1088*832
          default: 1280*720
        duration:
          anyOf:
            - type: integer
              enum:
                - 5
            - type: 'null'
          description: Output duration (seconds). Fixed at 5.
        prompt_extend:
          type: boolean
          description: Enable intelligent prompt rewriting (default true).
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - model
        - function
        - prompt
        - ref_images_url
    WanVideoEditVideoRepaintingRequest:
      title: Video Repainting
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: Model name (only wan2.1-vace-plus is supported)
          enum:
            - wan2.1-vace-plus
        function:
          type: string
          const: video_repainting
          enum:
            - video_repainting
          description: Video repainting feature selector.
        prompt:
          type: string
          description: Text description for the repainted video (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters).
          maxLength: 500
        video_url:
          type: string
          format: uri
          description: >-
            Public MP4 URL for the source video (≤50MB, ≥16 FPS, ≤5s, ASCII
            URL).
        ref_images_url:
          type: array
          maxItems: 1
          description: >-
            Optional reference image URL (single entity image, same constraints
            as image_reference).
          items:
            type: string
            format: uri
        control_condition:
          type: string
          description: >-
            Feature extraction method: posebodyface, posebody, depth, or
            scribble.
          enum:
            - posebodyface
            - posebody
            - depth
            - scribble
        strength:
          anyOf:
            - type: number
              minimum: 0
              maximum: 1
            - type: 'null'
          description: >-
            Control strength applied to the extracted motion (0.0-1.0, default
            1.0).
        prompt_extend:
          type: boolean
          description: >-
            Enable prompt rewriting (default false, recommended off for
            consistency).
          default: false
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
      required:
        - model
        - function
        - prompt
        - video_url
        - control_condition
    WanVideoEditLocalEditingRequest:
      title: Local Editing
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: Model name (only wan2.1-vace-plus is supported)
          enum:
            - wan2.1-vace-plus
        function:
          type: string
          const: video_edit
          enum:
            - video_edit
          description: Local (masked) editing feature selector.
        prompt:
          type: string
          description: Text description for the edited region (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters).
          maxLength: 500
        video_url:
          type: string
          format: uri
          description: >-
            Public MP4 URL for the source video (≤50MB, ≥16 FPS, ≤5s, ASCII
            URL).
        ref_images_url:
          type: array
          maxItems: 1
          description: >-
            Optional reference image URL for replacement (single
            entity/background).
          items:
            type: string
            format: uri
        mask_image_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Public mask image URL (white = edit, black = keep). Resolution must
            match video_url.
        mask_frame_id:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          description: 1-based frame index where mask_image_url applies. Defaults to 1.
        mask_video_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Public mask video URL (MP4, same specs as video_url). Provide
            mask_image_url or mask_video_url.
        control_condition:
          anyOf:
            - type: string
              enum:
                - posebodyface
                - depth
            - type: 'null'
          description: Optional feature extraction method ("posebodyface" or "depth").
        mask_type:
          anyOf:
            - type: string
              enum:
                - tracking
                - fixed
            - type: 'null'
          description: >-
            Mask behavior (tracking = follows motion, fixed = static). Applies
            when mask_image_url is provided.
        expand_ratio:
          anyOf:
            - type: number
              minimum: 0
              maximum: 1
            - type: 'null'
          description: Expansion ratio for tracking masks (0.0-1.0, default 0.05).
        expand_mode:
          anyOf:
            - type: string
              enum:
                - hull
                - bbox
                - original
            - type: 'null'
          description: Shape of the tracking mask expansion.
        size:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Output resolution ("width\*height"). Supported: 1280\*720 (default),
            720\*1280, 960\*960, 832\*1088, 1088\*832.
          enum:
            - 1280*720
            - 720*1280
            - 960*960
            - 832*1088
            - 1088*832
          default: 1280*720
        duration:
          anyOf:
            - type: integer
              enum:
                - 5
            - type: 'null'
          description: Output duration (seconds). Fixed at 5.
        prompt_extend:
          type: boolean
          description: Enable prompt rewriting (default false).
          default: false
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
      required:
        - model
        - function
        - prompt
        - video_url
    WanVideoEditExtensionRequest:
      title: Video Extension
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: Model name (only wan2.1-vace-plus is supported)
          enum:
            - wan2.1-vace-plus
        function:
          type: string
          const: video_extension
          enum:
            - video_extension
          description: Video extension feature selector.
        prompt:
          type: string
          description: Text description for the extended video (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters).
          maxLength: 500
        first_frame_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: Public URL of the starting frame image (360-2000px, ≤10MB).
        last_frame_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Public URL of the ending frame image (same constraints as
            first_frame_url).
        first_clip_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: Public MP4 opening clip (≤3s, ≥16 FPS, ≤50MB).
        last_clip_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: Public MP4 ending clip (≤3s, ≥16 FPS, ≤50MB).
        video_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Optional guidance video (MP4, ≤5s, ≥16 FPS, ≤50MB). Requires
            control_condition.
        control_condition:
          anyOf:
            - type: string
              enum:
                - posebodyface
                - depth
            - type: 'null'
          description: >-
            Feature extraction for guidance video ("posebodyface" or "depth").
            Required when video_url is provided.
        duration:
          anyOf:
            - type: integer
              enum:
                - 5
            - type: 'null'
          description: Output duration (seconds). Fixed at 5.
        prompt_extend:
          type: boolean
          description: Enable prompt rewriting (default false).
          default: false
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
      required:
        - model
        - function
        - prompt
    WanVideoEditOutpaintingRequest:
      title: Video Outpainting
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: Model name (only wan2.1-vace-plus is supported)
          enum:
            - wan2.1-vace-plus
        function:
          type: string
          const: video_outpainting
          enum:
            - video_outpainting
          description: Video outpainting feature selector.
        prompt:
          type: string
          description: Text description for the outpainted areas (max 800 characters).
          maxLength: 800
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt (max 500 characters).
          maxLength: 500
        video_url:
          type: string
          format: uri
          description: >-
            Public MP4 URL for the source video (≤50MB, ≥16 FPS, ≤5s, ASCII
            URL).
        top_scale:
          anyOf:
            - type: number
              minimum: 1
              maximum: 2
            - type: 'null'
          description: Upward scaling ratio [1.0, 2.0]. Default 1.0.
        bottom_scale:
          anyOf:
            - type: number
              minimum: 1
              maximum: 2
            - type: 'null'
          description: Downward scaling ratio [1.0, 2.0]. Default 1.0.
        left_scale:
          anyOf:
            - type: number
              minimum: 1
              maximum: 2
            - type: 'null'
          description: Leftward scaling ratio [1.0, 2.0]. Default 1.0.
        right_scale:
          anyOf:
            - type: number
              minimum: 1
              maximum: 2
            - type: 'null'
          description: Rightward scaling ratio [1.0, 2.0]. Default 1.0.
        duration:
          anyOf:
            - type: integer
              enum:
                - 5
            - type: 'null'
          description: Output duration (seconds). Fixed at 5.
        prompt_extend:
          type: boolean
          description: Enable prompt rewriting (default false).
          default: false
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
      required:
        - model
        - function
        - prompt
        - video_url
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 Video Ace Plus Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.1-vace-plus generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input video format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/alibaba/wan2.1-vace-plus/wan2.1-vace-plus.yaml GET /vendors/alibaba/v1/wan2.1-vace-plus/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.1-vace-plus API
  description: Wan2.1 VACE Plus Video Editing Model API
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/alibaba/v1/wan2.1-vace-plus/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan21_vace_plus_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan21VacePlusResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan21VacePlusResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Video Spark Generation

> Generate videos from text prompts using the wan2.6-t2v-spark model.

<Note>
  This is a fine-tuned model by MuleRouter based on the Wan2.6 Text-to-Video architecture. It offers improved quality and performance for specific use cases.
</Note>

## Overview

Generate videos from text prompts using the wan2.6-t2v-spark model with support for longer durations and multi-shot generation.

## Key Features

* Text-to-video generation with audio support
* 1080P resolution options
* 5s, 10s, or 15s duration
* Single or multi-shot generation
* Fine-tuned for enhanced visual quality

## Resolution Options

### 1080P

* 1920×1080 (16:9)
* 1080×1920 (9:16)
* 1440×1440 (1:1)
* 1632×1248 (4:3)
* 1248×1632 (3:4)

## Example Requests

### Basic Text-to-Video

```json theme={null}
{
  "prompt": "Miyazaki-style mule dancing",
  "size": "1920*1080",
  "duration": 5
}
```

### Multi-shot Video

```json theme={null}
{
  "prompt": "Waves crashing against rocks, water splashing, sunlight on the sea",
  "size": "1920*1080",
  "duration": 10,
  "prompt_extend": true,
  "multi_shots": "multi",
  "audio": true
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "A person walking through a city at night",
  "size": "1920*1080",
  "duration": 15,
  "audio_url": "https://example.com/city_sounds.mp3"
}
```

## Parameters

### multi\_shots

* **Default**: single
* **Effect**: When prompt rewriting is enabled, controls whether the output is single-shot or multi-shot
* **Only effective when**: `prompt_extend` is enabled

### duration

* **Options**: 5, 10, or 15 seconds
* **Note**: Longer durations may increase processing time


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.6-t2v-spark/wan2.6-t2v-spark.yaml POST /vendors/mulerouter/v1/wan2.6-t2v-spark/generation
openapi: 3.1.0
info:
  title: Wan2.6-t2v-spark API
  description: Wan2.6 Text-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.6-t2v-spark/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from text prompts using the wan2.6-t2v-spark model.
      operationId: wan26_t2v_spark_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26T2VSparkRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26T2VSparkRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text description for the desired video content (max 2000
            characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        size:
          type: string
          description: >-
            Output resolution ("width\*height"). Supported tiers:

            - 1080P: 1920\*1080 (16:9), 1080\*1920 (9:16), 1440\*1440 (1:1),
            1632\*1248 (4:3), 1248\*1632 (3:4)
          enum:
            - 1920*1080
            - 1080*1920
            - 1440*1440
            - 1632*1248
            - 1248*1632
          default: 1920*1080
        duration:
          type: integer
          description: Video duration in seconds. Supported values 5, 10, or 15.
          enum:
            - 5
            - 10
            - 15
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        shot_type:
          anyOf:
            - type: string
              enum:
                - single
                - multi
            - type: 'null'
          description: |-
            Specifies the shot type for video generation.

            Only takes effect when prompt_extend is enabled.

            - single: Default value, outputs single-shot video
            - multi: Outputs multi-shot video
          default: single
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text-To-Video Spark Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-t2v-spark generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:33:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.6-t2v-spark/wan2.6-t2v-spark.yaml GET /vendors/mulerouter/v1/wan2.6-t2v-spark/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-t2v-spark API
  description: Wan2.6 Text-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.6-t2v-spark/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_t2v_spark_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26T2VSparkResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26T2VSparkResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Video Spark Generation

> Generate videos from images using the wan2.6-i2v-spark model.

<Note>
  This is a fine-tuned model by MuleRouter based on the Wan2.6 Image-to-Video architecture. It offers improved quality and performance for specific use cases.
</Note>

## Overview

Generate videos from images using the wan2.6-i2v-spark model with support for longer durations, multi-shot generation, and optional last frame specification.

## Key Features

* Image-to-video generation with audio support
* 1080P resolution
* 5s, 10s, or 15s duration
* Single or multi-shot generation
* Optional first and last frame specification
* Fine-tuned for enhanced visual quality

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "A black cat looks curiously at the sky, camera gradually rises from eye-level to overhead",
  "image": "https://example.com/first_frame.jpg",
  "resolution": "1080P",
  "duration": 5
}
```

### With Last Frame (Interpolation)

```json theme={null}
{
  "prompt": "Character starts walking, expression changes naturally",
  "image": "https://example.com/person.jpg",
  "last_frame": "https://example.com/person_end.jpg",
  "resolution": "1080P",
  "duration": 10,
  "audio": true
}
```

### Multi-shot Video

```json theme={null}
{
  "prompt": "Scene transition with smooth camera movement",
  "image": "https://example.com/scene.jpg",
  "resolution": "1080P",
  "duration": 15,
  "prompt_extend": true,
  "multi_shots": "multi"
}
```

## Parameters

### last\_frame

* **Optional**: Yes
* **Description**: End frame image for video interpolation between first and last frame
* **Use case**: Create smooth transitions between two specific frames

### multi\_shots

* **Default**: single
* **Effect**: When prompt rewriting is enabled, controls whether the output is single-shot or multi-shot
* **Only effective when**: `prompt_extend` is enabled


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.6-i2v-spark/wan2.6-i2v-spark.yaml POST /vendors/mulerouter/v1/wan2.6-i2v-spark/generation
openapi: 3.1.0
info:
  title: Wan2.6-i2v-spark API
  description: Wan2.6 Image-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.6-i2v-spark/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from images using the wan2.6-i2v-spark model.
      operationId: wan26_i2v_spark_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan26I2VSparkRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan26I2VSparkRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description for the video (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 1080P
          enum:
            - 1080P
          default: 1080P
        duration:
          type: integer
          description: Video duration in seconds. Supported values 5, 10, or 15.
          enum:
            - 5
            - 10
            - 15
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        shot_type:
          anyOf:
            - type: string
              enum:
                - single
                - multi
            - type: 'null'
          description: |-
            Specifies the shot type for video generation.

            Only takes effect when prompt_extend is enabled.

            - single: Default value, outputs single-shot video
            - multi: Outputs multi-shot video
          default: single
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image-To-Video Spark Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.6-i2v-spark generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:33:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.6-i2v-spark/wan2.6-i2v-spark.yaml GET /vendors/mulerouter/v1/wan2.6-i2v-spark/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.6-i2v-spark API
  description: Wan2.6 Image-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.6-i2v-spark/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan26_i2v_spark_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan26I2VSparkResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan26I2VSparkResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Video Spark Generation

> Generate videos from text prompts using the wan2.5-t2v-spark model.

<Note>
  This is a fine-tuned model by MuleRouter based on the Wan2.5 Text-to-Video architecture. It offers improved quality and performance for specific use cases.
</Note>

## Overview

Generate videos from text prompts using the wan2.5-t2v-spark model with optional audio generation.

## Key Features

* Text-to-video generation with auto sound or custom audio
* Multiple resolution options (720P/1080P)
* 5s or 10s duration
* 24fps output
* Fine-tuned for enhanced visual quality

## Resolution Options

### 720P

* 1280×720 (16:9)
* 720×1280 (9:16)
* 960×960 (1:1)
* 1088×832 (4:3)
* 832×1088 (3:4)

### 1080P

* 1920×1080 (16:9)
* 1080×1920 (9:16)
* 1440×1440 (1:1)
* 1632×1248 (4:3)
* 1248×1632 (3:4)

## Audio Features

### Auto-generated Audio

* Enabled by default
* Automatically generates synchronized audio based on video content

### Custom Audio

* Supported formats: WAV, MP3
* Duration: 3-30 seconds
* Max file size: 15MB
* **Behavior**: If audio is shorter than video, remaining portion is silent; if longer, it's truncated

## Example Requests

### Basic Text-to-Video

```json theme={null}
{
  "prompt": "A small cat running on a grassy field in the moonlight",
  "size": "1920*1080",
  "duration": 10,
  "audio": true
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "A person walking through a forest, birds chirping",
  "audio_url": "https://example.com/forest_sounds.mp3",
  "size": "1920*1080",
  "duration": 10
}
```

### Silent Video

```json theme={null}
{
  "prompt": "City night scene timelapse, flowing traffic, brilliant lights",
  "size": "1280*720",
  "duration": 5,
  "audio": false
}
```

## Prompt Tips

For best results when describing motion:

* Specify camera movement (pan left, zoom in, dolly shot)
* Describe subject motion (walks forward, turns around)
* Include environment details (windy, foggy, sunlit)


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.5-t2v-spark/wan2.5-t2v-spark.yaml POST /vendors/mulerouter/v1/wan2.5-t2v-spark/generation
openapi: 3.1.0
info:
  title: Wan2.5-t2v-spark API
  description: Wan2.5 Text-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.5-t2v-spark/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from text prompts using the wan2.5-t2v-spark model.
      operationId: wan25_t2v_spark_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25T2VSparkRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25T2VSparkRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Text description for the desired video content (max 2000
            characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        size:
          type: string
          description: >-
            Output resolution ("width\*height"). Supported tiers:

            - 720P: 1280\*720 (16:9), 720\*1280 (9:16), 960\*960 (1:1),
            1088\*832 (4:3), 832\*1088 (3:4)

            - 1080P: 1920\*1080 (16:9), 1080\*1920 (9:16), 1440\*1440 (1:1),
            1632\*1248 (4:3), 1248\*1632 (3:4)
          enum:
            - 1280*720
            - 720*1280
            - 960*960
            - 1088*832
            - 832*1088
            - 1920*1080
            - 1080*1920
            - 1440*1440
            - 1632*1248
            - 1248*1632
          default: 1280*720
        duration:
          type: integer
          description: Video duration in seconds (24 fps). Supported values 5 or 10.
          enum:
            - 5
            - 10
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Text-To-Video Spark Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-t2v-spark generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The prompt contains prohibited content"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.5-t2v-spark/wan2.5-t2v-spark.yaml GET /vendors/mulerouter/v1/wan2.5-t2v-spark/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-t2v-spark API
  description: Wan2.5 Text-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.5-t2v-spark/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_t2v_spark_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25T2VSparkResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25T2VSparkResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Video Spark Generation

> Generate videos from images using the wan2.5-i2v-spark model.

<Note>
  This is a fine-tuned model by MuleRouter based on the Wan2.5 Image-to-Video architecture. It offers improved quality and performance for specific use cases.
</Note>

## Overview

Generate videos from images using the wan2.5-i2v-spark model with optional audio generation.

## Key Features

* Image-to-video generation with auto sound or custom audio
* Multiple resolution options (720P/1080P)
* 5s or 10s duration
* 24fps output
* Fine-tuned for enhanced visual quality

## Image Requirements

| Property       | Requirement                                   |
| -------------- | --------------------------------------------- |
| **Formats**    | JPEG, JPG, PNG (no transparency), BMP, WEBP   |
| **Dimensions** | \[360, 2000] pixels for both width and height |
| **File Size**  | Max 10MB                                      |
| **Input**      | Public URL or Base64 encoded data             |

## Audio Features

### Auto-generated Audio

* Enabled by default
* Automatically generates synchronized audio based on video content

### Custom Audio

* Supported formats: WAV, MP3
* Duration: 3-30 seconds
* Max file size: 15MB

## Example Requests

### Basic Image-to-Video

```json theme={null}
{
  "prompt": "The cat starts running forward",
  "image": "https://example.com/cat.jpg",
  "resolution": "720P",
  "duration": 5
}
```

### With Custom Audio

```json theme={null}
{
  "prompt": "Scene becomes dynamic, clouds drifting",
  "image": "https://example.com/landscape.jpg",
  "audio_url": "https://example.com/ambient.mp3",
  "resolution": "1080P",
  "duration": 10
}
```

### With Negative Prompt

```json theme={null}
{
  "prompt": "Character turns head and smiles",
  "image": "https://example.com/portrait.jpg",
  "negative_prompt": "shaking, distortion",
  "resolution": "720P",
  "duration": 5
}
```

## Prompt Tips

For best results:

* Describe the motion/story you want to see
* Specify camera movements if needed
* Include transition descriptions


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.5-i2v-spark/wan2.5-i2v-spark.yaml POST /vendors/mulerouter/v1/wan2.5-i2v-spark/generation
openapi: 3.1.0
info:
  title: Wan2.5-i2v-spark API
  description: Wan2.5 Image-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.5-i2v-spark/generation:
    post:
      summary: Create Generation Task
      description: Generate videos from images using the wan2.5-i2v-spark model.
      operationId: wan25_i2v_spark_generation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Wan25I2VSparkRequest'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
components:
  schemas:
    Wan25I2VSparkRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: Motion/story description for the video (max 2000 characters).
          maxLength: 2000
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt describing unwanted content (max 500 characters).
          maxLength: 500
        image:
          type: string
          description: >-
            First-frame image (URL or Base64). Supported formats:
            JPEG/JPG/PNG/BMP/WEBP, 360-2000px, ≤10MB.
        audio:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable automatic audio generation. Set to false to force a silent
            output.
          default: true
        audio_url:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: >-
            Custom audio file URL (wav/mp3, 3-30s, ≤15MB). Overrides the audio
            flag.
        resolution:
          type: string
          description: |-
            Output resolution tier:
            - 720P
            - 1080P
          enum:
            - 720P
            - 1080P
          default: 720P
        duration:
          type: integer
          description: Video duration in seconds (24 fps). Supported values 5 or 10.
          enum:
            - 5
            - 10
        prompt_extend:
          type: boolean
          description: >-
            Enable intelligent prompt rewriting (slightly longer latency, better
            detail).
          default: true
        seed:
          type: integer
          description: Random seed [0, 2147483647].
          minimum: 0
          maximum: 2147483647
        safety_filter:
          anyOf:
            - type: boolean
            - type: 'null'
          description: >-
            Enable content safety filter. Defaults to true. Set to false to
            disable content safety inspection.
          default: true
      required:
        - prompt
        - image
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (pending when created)
          enum:
            - pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Image-To-Video Spark Task

> Retrieve the status and result of a generation task

## Overview

Retrieve the status and result of a wan2.5-i2v-spark generation task.

## Task Status

| Status       | Description                       |
| ------------ | --------------------------------- |
| `pending`    | Task is waiting to be processed   |
| `processing` | Task is currently being processed |
| `completed`  | Task completed successfully       |
| `failed`     | Task failed with an error         |

## Response

When the task is completed, the response will include the generated video URLs in the `videos` array.

## Example Response

### Completed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "completed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:32:00Z"
  },
  "videos": [
    "https://example.com/generated-video.mp4"
  ]
}
```

### Failed Task

```json theme={null}
{
  "task_info": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "status": "failed",
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:15Z",
    "error": {
      "code": 400,
      "title": "Invalid Request",
      "detail": "The input image format is not supported"
    }
  }
}
```


## OpenAPI

````yaml /api-reference/endpoint/mulerouter/wan2.5-i2v-spark/wan2.5-i2v-spark.yaml GET /vendors/mulerouter/v1/wan2.5-i2v-spark/generation/{task_id}
openapi: 3.1.0
info:
  title: Wan2.5-i2v-spark API
  description: Wan2.5 Image-to-Video Spark Model API - Fine-tuned by MuleRouter
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/mulerouter/v1/wan2.5-i2v-spark/generation/{task_id}:
    get:
      summary: Get Generation Task
      description: Retrieve the status and result of a generation task
      operationId: wan25_i2v_spark_generation_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Wan25I2VSparkResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Wan25I2VSparkResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          description: Generated video URLs (only present when status is success)
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status (always failed for error responses)
          enum:
            - failed
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Invalid Request
        detail:
          type: string
          description: MuleRouter Error detail
          example: The prompt contains prohibited content
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Text to Video

> Generate a video from a text prompt using the Kling V3 Omni model.

## Overview

Generate videos from text prompts using the Kling V3 Omni model. V3 Omni introduces:

* **Multi-shot video** — generate multi-scene videos via `multi_shot` and `multi_prompt`
* **Audio generation** — produce synchronized audio with `sound: "on"`
* **Extended duration** — 3 to 15 seconds
* **Element references** — reference up to 7 elements (images + elements combined)
* **Standard / Professional modes** — 720P (std) or 1080P (pro) output


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-text-to-video.yaml POST /vendors/klingai/v1/kling-v3-omni/text-to-video/generation
openapi: 3.1.0
info:
  title: Kling V3 Omni - Text to Video API
  version: 1.0.0
  description: Generate videos from text prompts using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/text-to-video/generation:
    post:
      summary: Text to Video Generation
      description: Generate a video from a text prompt using the Kling V3 Omni model.
      operationId: kling_v3_omni_text_to_video
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TextToVideoRequest'
            example:
              prompt: A futuristic cityscape with flying cars at sunset
              mode: pro
              aspect_ratio: '16:9'
              duration: 5
              sound: 'on'
      responses:
        '202':
          $ref: '#/components/responses/TaskCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  schemas:
    TextToVideoRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          anyOf:
            - type: string
              maxLength: 2500
            - type: 'null'
          description: >-
            Text prompt describing the video to generate. Either prompt or
            multi_prompt must be provided.
        multi_prompt:
          type: array
          items:
            $ref: '#/components/schemas/OmniMultiPrompt'
          minItems: 1
          maxItems: 6
          description: >-
            Multi-segment prompts for finer control. Either prompt or
            multi_prompt must be provided.
        negative_prompt:
          anyOf:
            - type: string
              maxLength: 2500
            - type: 'null'
          description: Negative prompt to exclude unwanted content.
        sound:
          type: string
          enum:
            - 'on'
            - 'off'
          default: 'off'
          description: Whether to generate sound for the video.
        mode:
          type: string
          enum:
            - std
            - pro
          default: pro
          description: Generation mode. std for standard quality, pro for higher quality.
        aspect_ratio:
          anyOf:
            - type: string
              enum:
                - '16:9'
                - '9:16'
                - '1:1'
            - type: 'null'
          description: Aspect ratio of the generated video.
        duration:
          type: integer
          default: 5
          description: Duration of the generated video in seconds (3-15).
        multi_shot:
          type: boolean
          default: false
          description: Whether to enable multi-shot generation.
        shot_type:
          anyOf:
            - type: string
              enum:
                - customize
                - intelligence
            - type: 'null'
          description: Shot type configuration.
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementItem'
          maxItems: 7
          description: >-
            Element list. Combined count of images and elements must not exceed
            7.
    OmniMultiPrompt:
      type: object
      additionalProperties: false
      required:
        - prompt
        - duration
      properties:
        prompt:
          type: string
          maxLength: 512
        duration:
          type: integer
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 3
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          type: array
          items:
            type: string
            format: uri
          minItems: 1
          description: Reference video URLs.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  responses:
    TaskCreated:
      description: Accepted - Task created successfully
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TaskCreatedResponse'
          example:
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: pending
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Text to Video Task

> Retrieve the status and result of a text-to-video generation task.

Retrieve the status and result of a Kling V3 Omni text-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-text-to-video.yaml GET /vendors/klingai/v1/kling-v3-omni/text-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling V3 Omni - Text to Video API
  version: 1.0.0
  description: Generate videos from text prompts using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/text-to-video/generation/{task_id}:
    get:
      summary: Get Text to Video Task
      description: Retrieve the status and result of a text-to-video generation task.
      operationId: kling_v3_omni_text_to_video_get
      parameters:
        - $ref: '#/components/parameters/TaskId'
      responses:
        '200':
          $ref: '#/components/responses/TaskResult'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  parameters:
    TaskId:
      name: task_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    TaskResult:
      description: Task result
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/VideoTaskResponse'
          example:
            videos:
              - >-
                https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: completed
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    VideoTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Image to Video

> Generate a video from one or more images using the Kling V3 Omni model.

## Overview

Generate videos from input images using the Kling V3 Omni model. Requires at least one frame image. In addition to text-to-video features, image-to-video supports:

* **First/Last frame control** — provide `first_frame` and `last_frame` images
* **Reference images** — additional image references via `images` array
* **Element references** — reference up to 3 elements when using first/last frame images
* **Multi-shot video** — generate multi-scene videos via `multi_shot` and `multi_prompt`


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-image-to-video.yaml POST /vendors/klingai/v1/kling-v3-omni/image-to-video/generation
openapi: 3.1.0
info:
  title: Kling V3 Omni - Image to Video API
  version: 1.0.0
  description: Generate videos from images using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/image-to-video/generation:
    post:
      summary: Image to Video Generation
      description: Generate a video from one or more images using the Kling V3 Omni model.
      operationId: kling_v3_omni_image_to_video
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImageToVideoRequest'
            example:
              first_frame: https://example.com/first-frame.jpg
              prompt: A gentle breeze blows through the scene, camera slowly zooms in
              mode: pro
              duration: 5
      responses:
        '202':
          $ref: '#/components/responses/TaskCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  schemas:
    ImageToVideoRequest:
      type: object
      additionalProperties: false
      properties:
        first_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            First frame image (URL or Base64). Sets the opening frame of the
            generated video.
        last_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Last frame image (URL or Base64). Sets the closing frame of the
            generated video.
        images:
          anyOf:
            - type: array
              items:
                type: string
              minItems: 1
            - type: 'null'
          description: List of reference image URLs or Base64 strings.
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Text prompt to guide video generation from the images.
        multi_prompt:
          type: array
          items:
            $ref: '#/components/schemas/OmniMultiPrompt'
          minItems: 1
          maxItems: 6
          description: Multi-segment prompts for finer control.
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt to exclude unwanted content.
        sound:
          type: string
          enum:
            - 'on'
            - 'off'
          default: 'off'
          description: Whether to generate sound for the video.
        mode:
          type: string
          enum:
            - std
            - pro
          default: pro
          description: Generation mode. std for standard quality, pro for higher quality.
        aspect_ratio:
          anyOf:
            - type: string
              enum:
                - '16:9'
                - '9:16'
                - '1:1'
            - type: 'null'
          description: Aspect ratio of the generated video.
        duration:
          type: integer
          default: 5
          description: Duration of the generated video in seconds (3-15).
        multi_shot:
          type: boolean
          default: false
          description: Whether to enable multi-shot generation.
        shot_type:
          anyOf:
            - type: string
              enum:
                - customize
                - intelligence
            - type: 'null'
          description: Shot type configuration.
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementItem'
          maxItems: 3
          description: Element list. Max 3 when using first/last frame images.
    OmniMultiPrompt:
      type: object
      additionalProperties: false
      required:
        - prompt
        - duration
      properties:
        prompt:
          type: string
          maxLength: 512
        duration:
          type: integer
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 3
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          type: array
          items:
            type: string
            format: uri
          minItems: 1
          description: Reference video URLs.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  responses:
    TaskCreated:
      description: Accepted - Task created successfully
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TaskCreatedResponse'
          example:
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: pending
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Image to Video Task

> Retrieve the status and result of an image-to-video generation task.

Retrieve the status and result of a Kling V3 Omni image-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-image-to-video.yaml GET /vendors/klingai/v1/kling-v3-omni/image-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling V3 Omni - Image to Video API
  version: 1.0.0
  description: Generate videos from images using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/image-to-video/generation/{task_id}:
    get:
      summary: Get Image to Video Task
      description: Retrieve the status and result of an image-to-video generation task.
      operationId: kling_v3_omni_image_to_video_get
      parameters:
        - $ref: '#/components/parameters/TaskId'
      responses:
        '200':
          $ref: '#/components/responses/TaskResult'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  parameters:
    TaskId:
      name: task_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    TaskResult:
      description: Task result
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/VideoTaskResponse'
          example:
            videos:
              - >-
                https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: completed
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    VideoTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Reference Image to Video

> Generate a video using reference images with the Kling V3 Omni model.

## Overview

Generate videos from reference images using the Kling V3 Omni model:

* **Reference images** — provide images via the `images` array to guide generation
* **First/Last frame control** — optionally set opening and closing frames
* **Element references** — reference up to 7 elements (images + elements combined)
* **Multi-shot video** — generate multi-scene videos via `multi_shot` and `multi_prompt`
* **Audio generation** — produce synchronized audio with `sound: "on"`


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-reference-image-to-video.yaml POST /vendors/klingai/v1/kling-v3-omni/reference-image-to-video/generation
openapi: 3.1.0
info:
  title: Kling V3 Omni - Reference Image to Video API
  version: 1.0.0
  description: Generate videos from reference images using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/reference-image-to-video/generation:
    post:
      summary: Reference Image to Video Generation
      description: Generate a video using reference images with the Kling V3 Omni model.
      operationId: kling_v3_omni_reference_image_to_video
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ReferenceToVideoRequest'
            example:
              prompt: A person walking through a beautiful garden
              images:
                - https://example.com/reference.jpg
              mode: pro
              aspect_ratio: '16:9'
              duration: 5
      responses:
        '202':
          $ref: '#/components/responses/TaskCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  schemas:
    ReferenceToVideoRequest:
      type: object
      additionalProperties: false
      properties:
        first_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            First frame image (URL or Base64). Sets the opening frame of the
            generated video.
        last_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Last frame image (URL or Base64). Sets the closing frame of the
            generated video.
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Text prompt to guide video generation.
        multi_prompt:
          type: array
          items:
            $ref: '#/components/schemas/OmniMultiPrompt'
          minItems: 1
          maxItems: 6
          description: Multi-segment prompts for finer control.
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt to exclude unwanted content.
        images:
          type: array
          items:
            type: string
          description: List of reference image URLs or Base64 strings.
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementItem'
          maxItems: 7
          description: >-
            Element list. Combined count of images and elements must not exceed
            7.
        sound:
          type: string
          enum:
            - 'on'
            - 'off'
          default: 'off'
          description: Whether to generate sound for the video.
        mode:
          type: string
          enum:
            - std
            - pro
          default: pro
          description: Generation mode. std for standard quality, pro for higher quality.
        aspect_ratio:
          anyOf:
            - type: string
              enum:
                - '16:9'
                - '9:16'
                - '1:1'
            - type: 'null'
          description: Aspect ratio of the generated video.
        duration:
          type: integer
          default: 5
          description: Duration of the generated video in seconds (3-15).
        multi_shot:
          type: boolean
          default: false
          description: Whether to enable multi-shot generation.
        shot_type:
          anyOf:
            - type: string
              enum:
                - customize
                - intelligence
            - type: 'null'
          description: Shot type configuration.
    OmniMultiPrompt:
      type: object
      additionalProperties: false
      required:
        - prompt
        - duration
      properties:
        prompt:
          type: string
          maxLength: 512
        duration:
          type: integer
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 3
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          type: array
          items:
            type: string
            format: uri
          minItems: 1
          description: Reference video URLs.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  responses:
    TaskCreated:
      description: Accepted - Task created successfully
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TaskCreatedResponse'
          example:
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: pending
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Reference Image to Video Task

> Retrieve the status and result of a reference-image-to-video generation task.

Retrieve the status and result of a Kling V3 Omni reference-image-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-reference-image-to-video.yaml GET /vendors/klingai/v1/kling-v3-omni/reference-image-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling V3 Omni - Reference Image to Video API
  version: 1.0.0
  description: Generate videos from reference images using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/reference-image-to-video/generation/{task_id}:
    get:
      summary: Get Reference Image to Video Task
      description: >-
        Retrieve the status and result of a reference-image-to-video generation
        task.
      operationId: kling_v3_omni_reference_image_to_video_get
      parameters:
        - $ref: '#/components/parameters/TaskId'
      responses:
        '200':
          $ref: '#/components/responses/TaskResult'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  parameters:
    TaskId:
      name: task_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    TaskResult:
      description: Task result
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/VideoTaskResponse'
          example:
            videos:
              - >-
                https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: completed
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    VideoTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Reference Video to Video

> Generate a new video based on a reference video using the Kling V3 Omni model.

## Overview

Generate new videos from a reference video using the Kling V3 Omni model:

* **Video reference** — provide a source video URL via `video`
* **Keep audio** — preserve audio from the source video with `keep_audio: true`
* **Element references** — reference up to 4 elements when using reference video
* **Standard / Professional modes** — 720P (std) or 1080P (pro) output


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-reference-video-to-video.yaml POST /vendors/klingai/v1/kling-v3-omni/reference-video-to-video/generation
openapi: 3.1.0
info:
  title: Kling V3 Omni - Reference Video to Video API
  version: 1.0.0
  description: Generate new videos from a reference video using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/reference-video-to-video/generation:
    post:
      summary: Reference Video to Video Generation
      description: >-
        Generate a new video based on a reference video using the Kling V3 Omni
        model.
      operationId: kling_v3_omni_video_to_video_generation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ReferenceVideoToVideoRequest'
            example:
              prompt: >-
                Transform the video into an animated painting style with vibrant
                colors
              video: https://example.com/source-video.mp4
              keep_audio: true
              mode: pro
      responses:
        '202':
          $ref: '#/components/responses/TaskCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  schemas:
    ReferenceVideoToVideoRequest:
      type: object
      additionalProperties: false
      required:
        - prompt
        - video
      properties:
        prompt:
          type: string
          maxLength: 2500
          description: Text prompt describing the desired transformation.
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt to exclude unwanted content.
        video:
          type: string
          description: Reference video URL.
        keep_audio:
          type: boolean
          default: false
          description: Whether to keep the audio from the source video.
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementItem'
          maxItems: 4
          description: >-
            Element list. Combined count of images and elements must not exceed
            4 when using reference video.
        mode:
          type: string
          enum:
            - std
            - pro
          default: pro
          description: Generation mode. std for standard quality, pro for higher quality.
        aspect_ratio:
          anyOf:
            - type: string
              enum:
                - '16:9'
                - '9:16'
                - '1:1'
            - type: 'null'
          description: Aspect ratio of the generated video.
        duration:
          type: integer
          default: 5
          description: Duration of the generated video in seconds (3-15).
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 3
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          type: array
          items:
            type: string
            format: uri
          minItems: 1
          description: Reference video URLs.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  responses:
    TaskCreated:
      description: Accepted - Task created successfully
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TaskCreatedResponse'
          example:
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: pending
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Reference Video to Video Task

> Retrieve the status and result of a reference video-to-video generation task.

Retrieve the status and result of a Kling V3 Omni video-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-reference-video-to-video.yaml GET /vendors/klingai/v1/kling-v3-omni/reference-video-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling V3 Omni - Reference Video to Video API
  version: 1.0.0
  description: Generate new videos from a reference video using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/reference-video-to-video/generation/{task_id}:
    get:
      summary: Get Reference Video to Video Task
      description: >-
        Retrieve the status and result of a reference video-to-video generation
        task.
      operationId: kling_v3_omni_video_to_video_generation_get
      parameters:
        - $ref: '#/components/parameters/TaskId'
      responses:
        '200':
          $ref: '#/components/responses/TaskResult'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  parameters:
    TaskId:
      name: task_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    TaskResult:
      description: Task result
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/VideoTaskResponse'
          example:
            videos:
              - >-
                https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: completed
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    VideoTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Video to Video Edit

> Edit an existing video using the Kling V3 Omni model.

## Overview

Edit existing videos using the Kling V3 Omni model:

* **Video editing** — modify existing videos with text prompts
* **Video input** — provide the source video URL via `video`
* **Element references** — reference up to 4 elements when using reference video
* **Standard / Professional modes** — 720P (std) or 1080P (pro) output


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-video-to-video-edit.yaml POST /vendors/klingai/v1/kling-v3-omni/video-to-video/edit
openapi: 3.1.0
info:
  title: Kling V3 Omni - Video to Video Edit API
  version: 1.0.0
  description: Edit existing videos using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/video-to-video/edit:
    post:
      summary: Video to Video Edit
      description: Edit an existing video using the Kling V3 Omni model.
      operationId: kling_v3_omni_video_to_video_edit
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VideoToVideoEditRequest'
            example:
              prompt: Add snow falling effect to the video
              video: https://example.com/source-video.mp4
      responses:
        '202':
          $ref: '#/components/responses/TaskCreated'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  schemas:
    VideoToVideoEditRequest:
      type: object
      additionalProperties: false
      required:
        - prompt
        - video
      properties:
        prompt:
          type: string
          maxLength: 2500
          description: Text prompt describing the desired edit.
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative prompt to exclude unwanted content.
        video:
          type: string
          description: Video URL to edit.
        images:
          type: array
          items:
            type: string
          description: Optional list of reference image URLs or Base64 strings.
        elements:
          type: array
          items:
            $ref: '#/components/schemas/ElementItem'
          maxItems: 4
          description: >-
            Element list. Combined count of images and elements must not exceed
            4 when using reference video.
        mode:
          type: string
          enum:
            - std
            - pro
          default: pro
          description: >-
            Generation mode. std for standard quality (720P), pro for higher
            quality (1080P).
        aspect_ratio:
          anyOf:
            - type: string
              enum:
                - '16:9'
                - '9:16'
                - '1:1'
            - type: 'null'
          description: Aspect ratio of the generated video.
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 3
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          type: array
          items:
            type: string
            format: uri
          minItems: 1
          description: Reference video URLs.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoCreated:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  responses:
    TaskCreated:
      description: Accepted - Task created successfully
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TaskCreatedResponse'
          example:
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: pending
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3 Omni Video to Video Edit Task

> Retrieve the status and result of a video-to-video edit task.

Retrieve the status and result of a Kling V3 Omni video-to-video edit task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3-omni/kling-v3-omni-video-to-video-edit.yaml GET /vendors/klingai/v1/kling-v3-omni/video-to-video/edit/{task_id}
openapi: 3.1.0
info:
  title: Kling V3 Omni - Video to Video Edit API
  version: 1.0.0
  description: Edit existing videos using Kling V3 Omni model.
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3-omni/video-to-video/edit/{task_id}:
    get:
      summary: Get Video to Video Edit Task
      description: Retrieve the status and result of a video-to-video edit task.
      operationId: kling_v3_omni_video_to_video_edit_get
      parameters:
        - $ref: '#/components/parameters/TaskId'
      responses:
        '200':
          $ref: '#/components/responses/TaskResult'
        '400':
          $ref: '#/components/responses/BadRequest'
      security:
        - bearerAuth: []
components:
  parameters:
    TaskId:
      name: task_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    TaskResult:
      description: Task result
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/VideoTaskResponse'
          example:
            videos:
              - >-
                https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
            task_info:
              id: 8e1e315e-b50d-4334-a231-be7d19a372f4
              status: completed
              created_at: '2026-03-03T00:00:00Z'
              updated_at: '2026-03-03T00:00:00Z'
    BadRequest:
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    VideoTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          type: object
          properties:
            id:
              type: string
              format: uuid
            status:
              type: string
              enum:
                - failed
            error:
              $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Text to Video

> Generate videos from text prompts using the Kling v3.0 model with multi-shot, audio generation, and extended duration support.

## Overview

Generate videos from text prompts using the Kling V3.0 model. V3.0 introduces:

* **Multi-shot video** — generate multi-scene videos in a single task via `multi_shot` and `multi_prompt`
* **Audio generation** — produce synchronized audio with `sound: "on"`
* **Extended duration** — 3 to 15 seconds in 1-second increments
* **Standard / Professional modes** — 720P (std) or 1080P (pro) output


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3/openapi.yaml POST /vendors/klingai/v1/kling-v3/text-to-video/generation
openapi: 3.1.0
info:
  title: Kling v3.0 API
  description: >-
    Kling v3.0 Video Generation Model API with Multi-Shot, Sound, and Element
    Support
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3/text-to-video/generation:
    post:
      summary: Text to Video Generation
      description: >-
        Generate videos from text prompts using the Kling v3.0 model with
        multi-shot, audio generation, and extended duration support.
      operationId: kling_v3_text_to_video
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Text2VideoRequest'
            example:
              prompt: A futuristic cityscape with flying cars at sunset
              mode: pro
              aspect_ratio: '16:9'
              duration: 10
              sound: 'on'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-02-14T00:00:00.000Z'
                  updated_at: '2026-02-14T00:00:00.000Z'
components:
  schemas:
    Text2VideoRequest:
      type: object
      additionalProperties: false
      properties:
        first_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            First frame image (URL or Base64). Sets the opening frame of the
            generated video.
        last_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Last frame image (URL or Base64). Sets the closing frame of the
            generated video.
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: >
            Positive text prompt. Cannot exceed 2500 characters.


            Required when `multi_shot` is `false` or when `shot_type` is
            `intelligence`.
          maxLength: 2500
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative text prompt. Cannot exceed 2500 characters.
          maxLength: 2500
        multi_shot:
          type: boolean
          description: >
            Whether to generate a multi-shot video.

            - `true`: Enable multi-shot mode. `prompt` is ignored; use
            `shot_type` and `multi_prompt` instead.

            - `false`: Single-shot mode (default).
          default: false
        shot_type:
          anyOf:
            - type: string
            - type: 'null'
          description: |
            Shot segmentation method. Required when `multi_shot` is `true`.
            - `customize`: Custom shots, requires `multi_prompt`.
            - `intelligence`: AI-generated shots, requires `prompt`.
          enum:
            - customize
            - intelligence
        multi_prompt:
          anyOf:
            - type: array
              items:
                $ref: '#/components/schemas/ShotPrompt'
              minItems: 1
              maxItems: 6
            - type: 'null'
          description: >
            Shot prompt list for multi-shot videos.

            - Max 6 shots, min 1 shot.

            - Each shot prompt max 512 characters.

            - Each shot duration must not exceed total duration and must be >=
            1.

            - Sum of all shot durations must equal total task duration.


            Required when `multi_shot` is `true` and `shot_type` is `customize`.
        sound:
          type: string
          description: |
            Generate audio simultaneously when generating videos.
            - `on`: Enable audio generation
            - `off`: Disable audio generation (silent video)
          default: 'off'
          enum:
            - 'on'
            - 'off'
        mode:
          type: string
          description: |
            Video generation mode.

            `std`: Standard Mode (720P), cost-effective.
            `pro`: Professional Mode (1080P), higher quality video output.
          default: std
          enum:
            - std
            - pro
        aspect_ratio:
          type: string
          description: The aspect ratio of the generated video frame (width:height).
          default: '16:9'
          enum:
            - '16:9'
            - '9:16'
            - '1:1'
        duration:
          type: integer
          description: Video length in seconds (3-15).
          default: 5
        elements:
          anyOf:
            - type: array
              items:
                $ref: '#/components/schemas/ElementItem'
              minItems: 1
              maxItems: 3
            - type: 'null'
          description: |
            Element definitions. Max 3 elements.
            Provide frontal and reference images.
            Use `<<<element_1>>>` in prompt to reference elements.
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ShotPrompt:
      type: object
      additionalProperties: false
      description: A single shot configuration for multi-shot video generation.
      properties:
        prompt:
          type: string
          description: Text prompt for this shot. Max 512 characters.
          maxLength: 512
        duration:
          type: integer
          description: >-
            Duration of this shot in seconds. Must be >= 1 and <= total task
            duration.
      required:
        - prompt
        - duration
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          anyOf:
            - type: array
              items:
                type: string
              minItems: 1
              maxItems: 3
            - type: 'null'
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          anyOf:
            - type: array
              items:
                type: string
                format: uri
              minItems: 1
            - type: 'null'
          description: Reference video URLs.
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Text to Video Task

> Retrieve the status and result of a text-to-video generation task

Retrieve the status and result of a Kling V3.0 text-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3/openapi.yaml GET /vendors/klingai/v1/kling-v3/text-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling v3.0 API
  description: >-
    Kling v3.0 Video Generation Model API with Multi-Shot, Sound, and Element
    Support
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3/text-to-video/generation/{task_id}:
    get:
      summary: Get Text to Video Task
      description: Retrieve the status and result of a text-to-video generation task
      operationId: kling_v3_text_to_video_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Text2VideoResponse'
              example:
                videos:
                  - >-
                    https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-02-14T00:00:00.000Z'
                  updated_at: '2026-02-14T00:00:00.000Z'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Text2VideoResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Image to Video

> Generate videos from images using the Kling v3.0 model with multi-shot, audio, element reference, and extended duration support.

## Overview

Generate videos from reference images using the Kling V3.0 model. In addition to the text-to-video features, image-to-video supports:

* **First/Last frame control** — provide `first_frame` and `last_frame` for start-to-end frame interpolation
* **Element references** — reference up to 3 subjects via `elements` with frontal and reference images


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3/openapi.yaml POST /vendors/klingai/v1/kling-v3/image-to-video/generation
openapi: 3.1.0
info:
  title: Kling v3.0 API
  description: >-
    Kling v3.0 Video Generation Model API with Multi-Shot, Sound, and Element
    Support
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3/image-to-video/generation:
    post:
      summary: Image to Video Generation
      description: >-
        Generate videos from images using the Kling v3.0 model with multi-shot,
        audio, element reference, and extended duration support.
      operationId: kling_v3_image_to_video
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Image2VideoRequest'
            example:
              mode: pro
              duration: 5
              first_frame: https://example.com/reference-image.jpg
              prompt: The character slowly turns to face the camera
              sound: 'off'
        required: true
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-02-14T00:00:00.000Z'
                  updated_at: '2026-02-14T00:00:00.000Z'
components:
  schemas:
    Image2VideoRequest:
      type: object
      additionalProperties: false
      properties:
        first_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >
            First frame image (URL or Base64). Sets the opening frame of the
            generated video.


            **Important**: When using Base64 encoding, do not add any prefixes
            such as `data:image/png;base64,`. Provide only the Base64-encoded
            string itself.


            - Supported image formats: .jpg, .jpeg, .png

            - Image file size cannot exceed 10MB

            - Width and height dimensions must not be less than 300px

            - Aspect ratio should be between 1:2.5 ~ 2.5:1

            - At least one of `first_frame` and `last_frame` must be provided.
        last_frame:
          anyOf:
            - type: string
            - type: 'null'
          description: >
            Last frame image (URL or Base64). Sets the closing frame of the
            generated video.


            - At least one of `first_frame` and `last_frame` must be provided.

            - `last_frame`, `dynamic_masks`/`static_mask`, and `camera_control`
            are mutually exclusive.
        prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: >
            Positive text prompt. Cannot exceed 2500 characters.


            Required when `multi_shot` is `false` or when `shot_type` is
            `intelligence`.
          maxLength: 2500
        negative_prompt:
          anyOf:
            - type: string
            - type: 'null'
          description: Negative text prompt. Cannot exceed 2500 characters.
          maxLength: 2500
        multi_shot:
          type: boolean
          description: >
            Whether to generate a multi-shot video.

            - `true`: Enable multi-shot mode. `prompt` is ignored; use
            `shot_type` and `multi_prompt` instead.

            - `false`: Single-shot mode (default).
          default: false
        shot_type:
          anyOf:
            - type: string
            - type: 'null'
          description: |
            Shot segmentation method. Required when `multi_shot` is `true`.
            - `customize`: Custom shots, requires `multi_prompt`.
            - `intelligence`: AI-generated shots, requires `prompt`.
          enum:
            - customize
            - intelligence
        multi_prompt:
          anyOf:
            - type: array
              items:
                $ref: '#/components/schemas/ShotPrompt'
              minItems: 1
              maxItems: 6
            - type: 'null'
          description: >
            Shot prompt list for multi-shot videos.

            - Max 6 shots, min 1 shot.

            - Each shot prompt max 512 characters.

            - Each shot duration must not exceed total duration and must be >=
            1.

            - Sum of all shot durations must equal total task duration.


            Required when `multi_shot` is `true` and `shot_type` is `customize`.
        elements:
          anyOf:
            - type: array
              items:
                $ref: '#/components/schemas/ElementItem'
              minItems: 1
              maxItems: 3
            - type: 'null'
          description: |
            Element definitions. Max 3 elements.
            Provide frontal and reference images.
            Use `<<<element_1>>>` in prompt to reference elements.
        sound:
          type: string
          description: |
            Generate audio simultaneously when generating videos.
            - `on`: Enable audio generation
            - `off`: Disable audio generation (silent video)
          default: 'off'
          enum:
            - 'on'
            - 'off'
        mode:
          type: string
          description: |
            Video generation mode.

            `std`: Standard Mode (720P), cost-effective.
            `pro`: Professional Mode (1080P), higher quality video output.
          default: std
          enum:
            - std
            - pro
        duration:
          type: integer
          description: Video length in seconds (3-15).
          default: 5
    TaskCreatedResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    ShotPrompt:
      type: object
      additionalProperties: false
      description: A single shot configuration for multi-shot video generation.
      properties:
        prompt:
          type: string
          description: Text prompt for this shot. Max 512 characters.
          maxLength: 512
        duration:
          type: integer
          description: >-
            Duration of this shot in seconds. Must be >= 1 and <= total task
            duration.
      required:
        - prompt
        - duration
    ElementItem:
      type: object
      additionalProperties: false
      required:
        - type
      properties:
        type:
          type: string
          enum:
            - image
            - video
          description: Element type.
        frontal_image:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Frontal reference image of the subject (URL or Base64). Constraints:
            jpg/jpeg/png, <=10MB, >=300px, aspect ratio 1:2.5~2.5:1.
        reference_images:
          anyOf:
            - type: array
              items:
                type: string
              minItems: 1
              maxItems: 3
            - type: 'null'
          description: >-
            Additional reference images from other angles (URL or Base64), up to
            3 images.
        reference_videos:
          anyOf:
            - type: array
              items:
                type: string
                format: uri
              minItems: 1
            - type: 'null'
          description: Reference video URLs.
    TaskInfoCreated:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
      required:
        - id
        - status
        - created_at
        - updated_at
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Image to Video Task

> Retrieve the status and result of an image-to-video generation task

Retrieve the status and result of a Kling V3.0 image-to-video generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/klingai/kling-v3/openapi.yaml GET /vendors/klingai/v1/kling-v3/image-to-video/generation/{task_id}
openapi: 3.1.0
info:
  title: Kling v3.0 API
  description: >-
    Kling v3.0 Video Generation Model API with Multi-Shot, Sound, and Element
    Support
  license:
    name: MIT
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/klingai/v1/kling-v3/image-to-video/generation/{task_id}:
    get:
      summary: Get Image to Video Task
      description: Retrieve the status and result of an image-to-video generation task
      operationId: kling_v3_image_to_video_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Image2VideoResponse'
              example:
                videos:
                  - >-
                    https://mulerouter.muleusercontent.com/public/079c5ad5-3b81-4eee-af06-4d85029899d0/result_000.mp4
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-02-14T00:00:00.000Z'
                  updated_at: '2026-02-14T00:00:00.000Z'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Image2VideoResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
        videos:
          type: array
          items:
            type: string
            format: uri
    ErrorResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoErrorResponse'
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoErrorResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
      required:
        - id
        - status
        - created_at
        - updated_at
        - error
    TaskInfoErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          example: 3001
        title:
          type: string
          example: Task Execution Error
        detail:
          type: string
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Diffusion

> Video Generation - Image to Video

<Note>
  The `prompt` parameter is compatible with Midjourney's format. Please refer to Midjourney's [official documentation](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List) for more details.
</Note>

## Pricing

| Task Name       | Resolution | Mode       | Pricing |
| :-------------- | ---------- | :--------- | ------: |
| Video Diffusion | 480p       | Fast Mode  |  0.51\$ |
|                 | 480p       | Turbo Mode |  1.02\$ |
|                 | 720p       | Fast Mode  | 1.632\$ |
|                 | 720p       | Turbo Mode | 3.264\$ |


## OpenAPI

````yaml /api-reference/endpoint/midjourney/midjourney.yaml POST /vendors/midjourney/v1/tob/video-diffusion
openapi: 3.1.0
info:
  title: Midjourney API
  description: Midjourney Image and Video Generation API
  version: 1.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/midjourney/v1/tob/video-diffusion:
    post:
      summary: Text/Image to Video
      description: Video Generation - Image to Video
      operationId: video_diffusion
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VideoDiffusionRequest'
            example:
              prompt: >-
                https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg
                A beautiful sunset over the mountains
              video_type: 0
        required: true
      responses:
        '202':
          description: Task accepted and queued for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VideoDiffusionTaskResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2025-09-21T00:00:00.000Z'
                  updated_at: '2025-09-21T00:00:00.000Z'
components:
  schemas:
    VideoDiffusionRequest:
      type: object
      additionalProperties: false
      properties:
        prompt:
          type: string
          description: >-
            Prompt for video generation. Must be between 1 and 8192 characters.
            Must start with an Image URL or Base64 encoded image string.
          minLength: 1
          maxLength: 8192
        video_type:
          type: integer
          description: |
            Video quality option provided by upstream service

            `0`: 480p
            `1`: 720p
          minimum: 0
          maximum: 1
          default: 0
      required:
        - prompt
      description: Image to Video generation request body
    VideoDiffusionTaskResponse:
      type: object
      additionalProperties: true
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
      required:
        - task_info
    TaskInfoResponse:
      type: object
      additionalProperties: true
      properties:
        id:
          type: string
          description: UUID of the task
          format: uuid
        status:
          type: string
          description: Task status
          enum:
            - pending
            - processing
            - completed
            - failed
          example: pending
        created_at:
          type: string
          description: Task creation timestamp (ISO 8601)
          format: date-time
        updated_at:
          type: string
          description: Task last update timestamp (ISO 8601)
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoResponseErrorObject'
          description: >-
            Error message of task execution, only returned when task status is
            failed
      required:
        - id
        - status
        - created_at
        - updated_at
    TaskInfoResponseErrorObject:
      type: object
      additionalProperties: true
      properties:
        code:
          type: integer
          description: MuleRouter Error code
          example: 3001
        title:
          type: string
          description: MuleRouter Error title
          example: Task Execution Error
        detail:
          type: string
          description: MuleRouter Error detail
          example: Task execution failed
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 HD Text to Speech

> Create a text-to-speech generation task using the speech-2.8-hd model.

## Overview

Generate high-definition speech from text using the MiniMax Speech 2.8 HD model. Speech 2.8 HD delivers:

* **High-definition audio quality** — superior clarity and naturalness
* **Pause tags** — insert precise pauses with `<#x#>` syntax (x = 0.01-99.99 seconds)
* **Interjection tags** — add natural expressions like `(laughs)`, `(sighs)`, `(coughs)`, `(clears throat)`, `(gasps)`, `(sniffs)`, `(groans)`, `(yawns)`
* **Voice settings** — control speed, volume, pitch, and emotion
* **40+ languages** — extensive language support with language boost
* **Audio customization** — configurable format (MP3/PCM/FLAC), sample rate, channel, and bitrate
* **Voice modification** — fine-tune pitch, intensity, and timbre
* **Pronunciation dictionary** — custom pronunciation replacements
* **Loudness normalization** — professional audio level control

## Supported Voice IDs

| No. | Language            | Voice ID                                    | Voice Name                |
| :-- | :------------------ | :------------------------------------------ | :------------------------ |
| 1   | Chinese (Mandarin)  | `male-qn-qingse`                            | Youthful Male             |
| 2   | Chinese (Mandarin)  | `male-qn-jingying`                          | Elite Young Male          |
| 3   | Chinese (Mandarin)  | `male-qn-badao`                             | Dominant Young Male       |
| 4   | Chinese (Mandarin)  | `male-qn-daxuesheng`                        | College Student Male      |
| 5   | Chinese (Mandarin)  | `female-shaonv`                             | Young Girl                |
| 6   | Chinese (Mandarin)  | `female-yujie`                              | Mature Female             |
| 7   | Chinese (Mandarin)  | `female-chengshu`                           | Sophisticated Woman       |
| 8   | Chinese (Mandarin)  | `female-tianmei`                            | Sweet Woman               |
| 9   | Chinese (Mandarin)  | `male-qn-qingse-jingpin`                    | Youthful Male Beta        |
| 10  | Chinese (Mandarin)  | `male-qn-jingying-jingpin`                  | Elite Young Male Beta     |
| 11  | Chinese (Mandarin)  | `male-qn-badao-jingpin`                     | Dominant Young Male Beta  |
| 12  | Chinese (Mandarin)  | `male-qn-daxuesheng-jingpin`                | College Student Male Beta |
| 13  | Chinese (Mandarin)  | `female-shaonv-jingpin`                     | Young Girl Beta           |
| 14  | Chinese (Mandarin)  | `female-yujie-jingpin`                      | Mature Female Beta        |
| 15  | Chinese (Mandarin)  | `female-chengshu-jingpin`                   | Sophisticated Woman Beta  |
| 16  | Chinese (Mandarin)  | `female-tianmei-jingpin`                    | Sweet Woman Beta          |
| 17  | Chinese (Mandarin)  | `clever_boy`                                | Clever Boy                |
| 18  | Chinese (Mandarin)  | `cute_boy`                                  | Cute Boy                  |
| 19  | Chinese (Mandarin)  | `lovely_girl`                               | Lovely Girl               |
| 20  | Chinese (Mandarin)  | `cartoon_pig`                               | Cartoon Pig               |
| 21  | Chinese (Mandarin)  | `bingjiao_didi`                             | Clingy Brother            |
| 22  | Chinese (Mandarin)  | `junlang_nanyou`                            | Handsome Boyfriend        |
| 23  | Chinese (Mandarin)  | `chunzhen_xuedi`                            | Innocent Junior           |
| 24  | Chinese (Mandarin)  | `lengdan_xiongzhang`                        | Cool Senior               |
| 25  | Chinese (Mandarin)  | `badao_shaoye`                              | Bossy Young Master        |
| 26  | Chinese (Mandarin)  | `tianxin_xiaoling`                          | Sweet Ling                |
| 27  | Chinese (Mandarin)  | `qiaopi_mengmei`                            | Playful Cute Girl         |
| 28  | Chinese (Mandarin)  | `wumei_yujie`                               | Charming Mature Woman     |
| 29  | Chinese (Mandarin)  | `diadia_xuemei`                             | Coquettish Junior Girl    |
| 30  | Chinese (Mandarin)  | `danya_xuejie`                              | Elegant Senior Girl       |
| 31  | Chinese (Mandarin)  | `Chinese (Mandarin)_Reliable_Executive`     | Reliable Executive        |
| 32  | Chinese (Mandarin)  | `Chinese (Mandarin)_News_Anchor`            | News Anchor               |
| 33  | Chinese (Mandarin)  | `Chinese (Mandarin)_Mature_Woman`           | Mature Woman              |
| 34  | Chinese (Mandarin)  | `Chinese (Mandarin)_Unrestrained_Young_Man` | Unrestrained Young Man    |
| 35  | Chinese (Mandarin)  | `Arrogant_Miss`                             | Arrogant Miss             |
| 36  | Chinese (Mandarin)  | `Robot_Armor`                               | Robot Armor               |
| 37  | Chinese (Mandarin)  | `Chinese (Mandarin)_Kind-hearted_Antie`     | Kind-hearted Auntie       |
| 38  | Chinese (Mandarin)  | `Chinese (Mandarin)_HK_Flight_Attendant`    | HK Flight Attendant       |
| 39  | Chinese (Mandarin)  | `Chinese (Mandarin)_Humorous_Elder`         | Humorous Elder            |
| 40  | Chinese (Mandarin)  | `Chinese (Mandarin)_Gentleman`              | Gentleman                 |
| 41  | Chinese (Mandarin)  | `Chinese (Mandarin)_Warm_Bestie`            | Warm Bestie               |
| 42  | Chinese (Mandarin)  | `Chinese (Mandarin)_Male_Announcer`         | Male Announcer            |
| 43  | Chinese (Mandarin)  | `Chinese (Mandarin)_Sweet_Lady`             | Sweet Lady                |
| 44  | Chinese (Mandarin)  | `Chinese (Mandarin)_Southern_Young_Man`     | Southern Young Man        |
| 45  | Chinese (Mandarin)  | `Chinese (Mandarin)_Wise_Women`             | Wise Woman                |
| 46  | Chinese (Mandarin)  | `Chinese (Mandarin)_Gentle_Youth`           | Gentle Youth              |
| 47  | Chinese (Mandarin)  | `Chinese (Mandarin)_Warm_Girl`              | Warm Girl                 |
| 48  | Chinese (Mandarin)  | `Chinese (Mandarin)_Kind-hearted_Elder`     | Kind-hearted Elder        |
| 49  | Chinese (Mandarin)  | `Chinese (Mandarin)_Cute_Spirit`            | Cute Spirit               |
| 50  | Chinese (Mandarin)  | `Chinese (Mandarin)_Radio_Host`             | Radio Host                |
| 51  | Chinese (Mandarin)  | `Chinese (Mandarin)_Lyrical_Voice`          | Lyrical Voice             |
| 52  | Chinese (Mandarin)  | `Chinese (Mandarin)_Straightforward_Boy`    | Straightforward Boy       |
| 53  | Chinese (Mandarin)  | `Chinese (Mandarin)_Sincere_Adult`          | Sincere Adult             |
| 54  | Chinese (Mandarin)  | `Chinese (Mandarin)_Gentle_Senior`          | Gentle Senior             |
| 55  | Chinese (Mandarin)  | `Chinese (Mandarin)_Stubborn_Friend`        | Stubborn Friend           |
| 56  | Chinese (Mandarin)  | `Chinese (Mandarin)_Crisp_Girl`             | Crisp Girl                |
| 57  | Chinese (Mandarin)  | `Chinese (Mandarin)_Pure-hearted_Boy`       | Pure-hearted Boy          |
| 58  | Chinese (Mandarin)  | `Chinese (Mandarin)_Soft_Girl`              | Soft Girl                 |
| 59  | Chinese (Cantonese) | `Cantonese_ProfessionalHost（F)`             | Professional Female Host  |
| 60  | Chinese (Cantonese) | `Cantonese_GentleLady`                      | Gentle Lady               |
| 61  | Chinese (Cantonese) | `Cantonese_ProfessionalHost（M)`             | Professional Male Host    |
| 62  | Chinese (Cantonese) | `Cantonese_PlayfulMan`                      | Playful Man               |
| 63  | Chinese (Cantonese) | `Cantonese_CuteGirl`                        | Cute Girl                 |
| 64  | Chinese (Cantonese) | `Cantonese_KindWoman`                       | Kind Woman                |
| 65  | English             | `Santa_Claus`                               | Santa Claus               |
| 66  | English             | `Grinch`                                    | Grinch                    |
| 67  | English             | `Rudolph`                                   | Rudolph                   |
| 68  | English             | `Arnold`                                    | Arnold                    |
| 69  | English             | `Charming_Santa`                            | Charming Santa            |
| 70  | English             | `Charming_Lady`                             | Charming Lady             |
| 71  | English             | `Sweet_Girl`                                | Sweet Girl                |
| 72  | English             | `Cute_Elf`                                  | Cute Elf                  |
| 73  | English             | `Attractive_Girl`                           | Attractive Girl           |
| 74  | English             | `Serene_Woman`                              | Serene Woman              |
| 75  | English             | `English_Trustworthy_Man`                   | Trustworthy Man           |
| 76  | English             | `English_Graceful_Lady`                     | Graceful Lady             |
| 77  | English             | `English_Aussie_Bloke`                      | Aussie Bloke              |
| 78  | English             | `English_Whispering_girl`                   | Whispering Girl           |
| 79  | English             | `English_Diligent_Man`                      | Diligent Man              |
| 80  | English             | `English_Gentle-voiced_man`                 | Gentle-voiced Man         |
| 81  | Japanese            | `Japanese_IntellectualSenior`               | Intellectual Senior       |
| 82  | Japanese            | `Japanese_DecisivePrincess`                 | Decisive Princess         |
| 83  | Japanese            | `Japanese_LoyalKnight`                      | Loyal Knight              |
| 84  | Japanese            | `Japanese_DominantMan`                      | Dominant Man              |
| 85  | Japanese            | `Japanese_SeriousCommander`                 | Serious Commander         |
| 86  | Japanese            | `Japanese_ColdQueen`                        | Cold Queen                |
| 87  | Japanese            | `Japanese_DependableWoman`                  | Dependable Woman          |
| 88  | Japanese            | `Japanese_GentleButler`                     | Gentle Butler             |
| 89  | Japanese            | `Japanese_KindLady`                         | Kind Lady                 |
| 90  | Japanese            | `Japanese_CalmLady`                         | Calm Lady                 |
| 91  | Japanese            | `Japanese_OptimisticYouth`                  | Optimistic Youth          |
| 92  | Japanese            | `Japanese_GenerousIzakayaOwner`             | Generous Izakaya Owner    |
| 93  | Japanese            | `Japanese_SportyStudent`                    | Sporty Student            |
| 94  | Japanese            | `Japanese_InnocentBoy`                      | Innocent Boy              |
| 95  | Japanese            | `Japanese_GracefulMaiden`                   | Graceful Maiden           |
| 96  | Korean              | `Korean_SweetGirl`                          | Sweet Girl                |
| 97  | Korean              | `Korean_CheerfulBoyfriend`                  | Cheerful Boyfriend        |
| 98  | Korean              | `Korean_EnchantingSister`                   | Enchanting Sister         |
| 99  | Korean              | `Korean_ShyGirl`                            | Shy Girl                  |
| 100 | Korean              | `Korean_ReliableSister`                     | Reliable Sister           |
| 101 | Korean              | `Korean_StrictBoss`                         | Strict Boss               |
| 102 | Korean              | `Korean_SassyGirl`                          | Sassy Girl                |
| 103 | Korean              | `Korean_ChildhoodFriendGirl`                | Childhood Friend Girl     |
| 104 | Korean              | `Korean_PlayboyCharmer`                     | Playboy Charmer           |
| 105 | Korean              | `Korean_ElegantPrincess`                    | Elegant Princess          |
| 106 | Korean              | `Korean_BraveFemaleWarrior`                 | Brave Female Warrior      |
| 107 | Korean              | `Korean_BraveYouth`                         | Brave Youth               |
| 108 | Korean              | `Korean_CalmLady`                           | Calm Lady                 |
| 109 | Korean              | `Korean_EnthusiasticTeen`                   | Enthusiastic Teen         |
| 110 | Korean              | `Korean_SoothingLady`                       | Soothing Lady             |
| 111 | Korean              | `Korean_IntellectualSenior`                 | Intellectual Senior       |
| 112 | Korean              | `Korean_LonelyWarrior`                      | Lonely Warrior            |
| 113 | Korean              | `Korean_MatureLady`                         | Mature Lady               |
| 114 | Korean              | `Korean_InnocentBoy`                        | Innocent Boy              |
| 115 | Korean              | `Korean_CharmingSister`                     | Charming Sister           |
| 116 | Korean              | `Korean_AthleticStudent`                    | Athletic Student          |
| 117 | Korean              | `Korean_BraveAdventurer`                    | Brave Adventurer          |
| 118 | Korean              | `Korean_CalmGentleman`                      | Calm Gentleman            |
| 119 | Korean              | `Korean_WiseElf`                            | Wise Elf                  |
| 120 | Korean              | `Korean_CheerfulCoolJunior`                 | Cheerful Cool Junior      |
| 121 | Korean              | `Korean_DecisiveQueen`                      | Decisive Queen            |
| 122 | Korean              | `Korean_ColdYoungMan`                       | Cold Young Man            |
| 123 | Korean              | `Korean_MysteriousGirl`                     | Mysterious Girl           |
| 124 | Korean              | `Korean_QuirkyGirl`                         | Quirky Girl               |
| 125 | Korean              | `Korean_ConsiderateSenior`                  | Considerate Senior        |
| 126 | Korean              | `Korean_CheerfulLittleSister`               | Cheerful Little Sister    |
| 127 | Korean              | `Korean_DominantMan`                        | Dominant Man              |
| 128 | Korean              | `Korean_AirheadedGirl`                      | Airheaded Girl            |
| 129 | Korean              | `Korean_ReliableYouth`                      | Reliable Youth            |
| 130 | Korean              | `Korean_FriendlyBigSister`                  | Friendly Big Sister       |
| 131 | Korean              | `Korean_GentleBoss`                         | Gentle Boss               |
| 132 | Korean              | `Korean_ColdGirl`                           | Cold Girl                 |
| 133 | Korean              | `Korean_HaughtyLady`                        | Haughty Lady              |
| 134 | Korean              | `Korean_CharmingElderSister`                | Charming Elder Sister     |
| 135 | Korean              | `Korean_IntellectualMan`                    | Intellectual Man          |
| 136 | Korean              | `Korean_CaringWoman`                        | Caring Woman              |
| 137 | Korean              | `Korean_WiseTeacher`                        | Wise Teacher              |
| 138 | Korean              | `Korean_ConfidentBoss`                      | Confident Boss            |
| 139 | Korean              | `Korean_AthleticGirl`                       | Athletic Girl             |
| 140 | Korean              | `Korean_PossessiveMan`                      | Possessive Man            |
| 141 | Korean              | `Korean_GentleWoman`                        | Gentle Woman              |
| 142 | Korean              | `Korean_CockyGuy`                           | Cocky Guy                 |
| 143 | Korean              | `Korean_ThoughtfulWoman`                    | Thoughtful Woman          |
| 144 | Korean              | `Korean_OptimisticYouth`                    | Optimistic Youth          |
| 145 | Spanish             | `Spanish_SereneWoman`                       | Serene Woman              |
| 146 | Spanish             | `Spanish_MaturePartner`                     | Mature Partner            |
| 147 | Spanish             | `Spanish_CaptivatingStoryteller`            | Captivating Storyteller   |
| 148 | Spanish             | `Spanish_Narrator`                          | Narrator                  |
| 149 | Spanish             | `Spanish_WiseScholar`                       | Wise Scholar              |
| 150 | Spanish             | `Spanish_Kind-heartedGirl`                  | Kind-hearted Girl         |
| 151 | Spanish             | `Spanish_DeterminedManager`                 | Determined Manager        |
| 152 | Spanish             | `Spanish_BossyLeader`                       | Bossy Leader              |
| 153 | Spanish             | `Spanish_ReservedYoungMan`                  | Reserved Young Man        |
| 154 | Spanish             | `Spanish_ConfidentWoman`                    | Confident Woman           |
| 155 | Portuguese          | `Portuguese_SentimentalLady`                | Sentimental Lady          |
| 156 | Portuguese          | `Portuguese_BossyLeader`                    | Bossy Leader              |
| 157 | Portuguese          | `Portuguese_Wiselady`                       | Wise Lady                 |
| 158 | Portuguese          | `Portuguese_Strong-WilledBoy`               | Strong-willed Boy         |
| 159 | Portuguese          | `Portuguese_Deep-VoicedGentleman`           | Deep-voiced Gentleman     |
| 160 | Portuguese          | `Portuguese_UpsetGirl`                      | Upset Girl                |
| 161 | French              | `French_Male_Speech_New`                    | Level-Headed Man          |
| 162 | French              | `French_Female_News Anchor`                 | Patient Female Presenter  |
| 163 | French              | `French_CasualMan`                          | Casual Man                |
| 164 | French              | `French_MovieLeadFemale`                    | Movie Lead Female         |
| 165 | French              | `French_FemaleAnchor`                       | Female Anchor             |
| 166 | French              | `French_MaleNarrator`                       | Male Narrator             |
| 167 | Indonesian          | `Indonesian_SweetGirl`                      | Sweet Girl                |
| 168 | Indonesian          | `Indonesian_ReservedYoungMan`               | Reserved Young Man        |
| 169 | Indonesian          | `Indonesian_CharmingGirl`                   | Charming Girl             |
| 170 | Indonesian          | `Indonesian_CalmWoman`                      | Calm Woman                |
| 171 | Indonesian          | `Indonesian_ConfidentWoman`                 | Confident Woman           |
| 172 | Indonesian          | `Indonesian_CaringMan`                      | Caring Man                |
| 173 | Indonesian          | `Indonesian_BossyLeader`                    | Bossy Leader              |
| 174 | Indonesian          | `Indonesian_DeterminedBoy`                  | Determined Boy            |
| 175 | Indonesian          | `Indonesian_GentleGirl`                     | Gentle Girl               |
| 176 | German              | `German_FriendlyMan`                        | Friendly Man              |
| 177 | German              | `German_SweetLady`                          | Sweet Lady                |
| 178 | German              | `German_PlayfulMan`                         | Playful Man               |
| 179 | Russian             | `Russian_HandsomeChildhoodFriend`           | Handsome Childhood Friend |
| 180 | Russian             | `Russian_BrightHeroine`                     | Bright Queen              |
| 181 | Russian             | `Russian_AmbitiousWoman`                    | Ambitious Woman           |
| 182 | Russian             | `Russian_ReliableMan`                       | Reliable Man              |
| 183 | Russian             | `Russian_CrazyQueen`                        | Crazy Girl                |
| 184 | Russian             | `Russian_PessimisticGirl`                   | Pessimistic Girl          |
| 185 | Russian             | `Russian_AttractiveGuy`                     | Attractive Guy            |
| 186 | Russian             | `Russian_Bad-temperedBoy`                   | Bad-tempered Boy          |
| 187 | Italian             | `Italian_BraveHeroine`                      | Brave Heroine             |
| 188 | Italian             | `Italian_Narrator`                          | Narrator                  |
| 189 | Italian             | `Italian_WanderingSorcerer`                 | Wandering Sorcerer        |
| 190 | Italian             | `Italian_DiligentLeader`                    | Diligent Leader           |
| 191 | Arabic              | `Arabic_CalmWoman`                          | Calm Woman                |
| 192 | Arabic              | `Arabic_FriendlyGuy`                        | Friendly Guy              |
| 193 | Turkish             | `Turkish_CalmWoman`                         | Calm Woman                |
| 194 | Turkish             | `Turkish_Trustworthyman`                    | Trustworthy Man           |
| 195 | Ukrainian           | `Ukrainian_CalmWoman`                       | Calm Woman                |
| 196 | Ukrainian           | `Ukrainian_WiseScholar`                     | Wise Scholar              |
| 197 | Dutch               | `Dutch_kindhearted_girl`                    | Kind-hearted Girl         |
| 198 | Dutch               | `Dutch_bossy_leader`                        | Bossy Leader              |
| 199 | Vietnamese          | `Vietnamese_kindhearted_girl`               | Kind-hearted Girl         |
| 200 | Thai                | `Thai_male_1_sample8`                       | Serene Man                |
| 201 | Thai                | `Thai_male_2_sample2`                       | Friendly Man              |
| 202 | Thai                | `Thai_female_1_sample1`                     | Confident Woman           |
| 203 | Thai                | `Thai_female_2_sample2`                     | Energetic Woman           |
| 204 | Polish              | `Polish_male_1_sample4`                     | Male Narrator             |
| 205 | Polish              | `Polish_male_2_sample3`                     | Male Anchor               |
| 206 | Polish              | `Polish_female_1_sample1`                   | Calm Woman                |
| 207 | Polish              | `Polish_female_2_sample3`                   | Casual Woman              |
| 208 | Romanian            | `Romanian_male_1_sample2`                   | Reliable Man              |
| 209 | Romanian            | `Romanian_male_2_sample1`                   | Energetic Youth           |
| 210 | Romanian            | `Romanian_female_1_sample4`                 | Optimistic Youth          |
| 211 | Romanian            | `Romanian_female_2_sample1`                 | Gentle Woman              |
| 212 | Greek               | `greek_male_1a_v1`                          | Thoughtful Mentor         |
| 213 | Greek               | `Greek_female_1_sample1`                    | Gentle Lady               |
| 214 | Greek               | `Greek_female_2_sample3`                    | Girl Next Door            |
| 215 | Czech               | `czech_male_1_v1`                           | Assured Presenter         |
| 216 | Czech               | `czech_female_5_v7`                         | Steadfast Narrator        |
| 217 | Czech               | `czech_female_2_v2`                         | Elegant Lady              |
| 218 | Finnish             | `finnish_male_3_v1`                         | Upbeat Man                |
| 219 | Finnish             | `finnish_male_1_v2`                         | Friendly Boy              |
| 220 | Finnish             | `finnish_female_4_v1`                       | Assertive Woman           |
| 221 | Hindi               | `hindi_male_1_v2`                           | Trustworthy Advisor       |
| 222 | Hindi               | `hindi_female_2_v1`                         | Tranquil Woman            |
| 223 | Hindi               | `hindi_female_1_v2`                         | News Anchor               |


## OpenAPI

````yaml /api-reference/endpoint/minimax/speech-2.8-hd/speech-2.8-hd.yaml POST /vendors/minimax/v1/speech-2.8-hd/text-to-speech/generation
openapi: 3.1.0
info:
  title: MiniMax Speech 2.8 HD API
  description: MiniMax Speech 2.8 HD - High-Definition Text-to-Speech Generation
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/speech-2.8-hd/text-to-speech/generation:
    post:
      summary: Create Speech Generation Task
      description: Create a text-to-speech generation task using the speech-2.8-hd model.
      operationId: speech_2_8_hd_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SpeechGenerationRequest'
            example:
              prompt: >-
                Hello world! Welcome to MiniMax's new text to speech model
                <#0.1#> Speech 2.8 HD (laughs) now available!
              voice_setting:
                voice_id: Wise_Woman
                speed: 1
                vol: 1
                pitch: 0
              output_format: url
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    SpeechGenerationRequest:
      type: object
      required:
        - prompt
      properties:
        prompt:
          type: string
          minLength: 1
          maxLength: 10000
          description: >
            Text to convert to speech. Use `<#x#>` for pauses (x = 0.01-99.99
            seconds). Supports interjection tags: `(laughs)`, `(sighs)`,
            `(coughs)`, `(clears throat)`, `(gasps)`, `(sniffs)`, `(groans)`,
            `(yawns)`.
        voice_setting:
          $ref: '#/components/schemas/VoiceSetting'
          description: Voice configuration settings (optional, defaults to Wise_Woman).
        audio_setting:
          anyOf:
            - $ref: '#/components/schemas/AudioSetting'
            - type: 'null'
          description: Audio configuration settings.
        language_boost:
          anyOf:
            - type: string
              enum:
                - Chinese
                - Chinese,Yue
                - English
                - Arabic
                - Russian
                - Spanish
                - French
                - Portuguese
                - German
                - Turkish
                - Dutch
                - Ukrainian
                - Vietnamese
                - Indonesian
                - Japanese
                - Italian
                - Korean
                - Thai
                - Polish
                - Romanian
                - Greek
                - Czech
                - Finnish
                - Hindi
                - Bulgarian
                - Danish
                - Hebrew
                - Malay
                - Slovak
                - Swedish
                - Croatian
                - Hungarian
                - Norwegian
                - Slovenian
                - Catalan
                - Nynorsk
                - Afrikaans
                - auto
            - type: 'null'
          description: Enhance recognition of specified languages and dialects.
        output_format:
          type: string
          enum:
            - url
            - hex
          default: hex
          description: 'Format of the output content (non-streaming only). Default: hex.'
        pronunciation_dict:
          anyOf:
            - $ref: '#/components/schemas/PronunciationDict'
            - type: 'null'
          description: Custom pronunciation dictionary for text replacement.
        normalization_setting:
          anyOf:
            - $ref: '#/components/schemas/LoudnessNormalizationSetting'
            - type: 'null'
          description: Loudness normalization settings for the audio.
        voice_modify:
          anyOf:
            - $ref: '#/components/schemas/VoiceModify'
            - type: 'null'
          description: Voice modification settings to adjust pitch, intensity, and timbre.
    TaskCreatedResponse:
      type: object
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    VoiceSetting:
      type: object
      properties:
        voice_id:
          type: string
          description: >-
            Voice ID for synthesis. Examples - Chinese: male-qn-qingse,
            female-shaonv, female-yujie; English: Charming_Lady,
            English_Trustworthy_Man, English_Graceful_Lady. See the Supported
            Voice IDs section in the overview for the full list.
        speed:
          type: number
          minimum: 0.5
          maximum: 2
          default: 1
          description: Speech speed, range [0.5, 2.0].
        vol:
          type: number
          minimum: 0.01
          maximum: 10
          default: 1
          description: Volume, range [0, 10].
        pitch:
          type: integer
          minimum: -12
          maximum: 12
          default: 0
          description: Voice pitch, range [-12, 12].
        emotion:
          anyOf:
            - type: string
              enum:
                - happy
                - sad
                - angry
                - fearful
                - disgusted
                - surprised
                - neutral
            - type: 'null'
          description: Emotion of the generated speech.
        english_normalization:
          type: boolean
          default: false
          description: >-
            Enables English text normalization to improve number reading
            performance.
    AudioSetting:
      type: object
      properties:
        format:
          type: string
          enum:
            - mp3
            - pcm
            - flac
          default: mp3
          description: Audio format.
        sample_rate:
          type: integer
          enum:
            - 8000
            - 16000
            - 22050
            - 24000
            - 32000
            - 44100
          default: 32000
          description: Sample rate of generated audio (Hz).
        channel:
          type: integer
          enum:
            - 1
            - 2
          default: 1
          description: Number of audio channels (1=mono, 2=stereo).
        bitrate:
          type: integer
          enum:
            - 32000
            - 64000
            - 128000
            - 256000
          default: 128000
          description: Bitrate of generated audio (bps).
    PronunciationDict:
      type: object
      properties:
        tone_list:
          type: array
          items:
            type: string
          description: >-
            List of pronunciation replacements in format
            ['text/(pronunciation)', ...].
    LoudnessNormalizationSetting:
      type: object
      properties:
        enabled:
          type: boolean
          default: true
          description: Enable loudness normalization for the audio.
        target_loudness:
          type: number
          minimum: -70
          maximum: -10
          default: -18
          description: Target loudness in LUFS.
        target_range:
          type: number
          minimum: 0
          maximum: 20
          default: 8
          description: Target loudness range in LU.
        target_peak:
          type: number
          minimum: -3
          maximum: 0
          default: -0.5
          description: Target peak level in dBTP.
    VoiceModify:
      type: object
      properties:
        pitch:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Pitch adjustment. Range: -100 to 100.'
        intensity:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Intensity/energy of the voice. Range: -100 to 100.'
        timbre:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Timbre adjustment. Range: -100 to 100.'
    TaskInfoCreated:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 HD Text to Speech Task

> Retrieve the status and result of a speech generation task.

Retrieve the status and result of a MiniMax Speech 2.8 HD text-to-speech generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/minimax/speech-2.8-hd/speech-2.8-hd.yaml GET /vendors/minimax/v1/speech-2.8-hd/text-to-speech/generation/{task_id}
openapi: 3.1.0
info:
  title: MiniMax Speech 2.8 HD API
  description: MiniMax Speech 2.8 HD - High-Definition Text-to-Speech Generation
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/speech-2.8-hd/text-to-speech/generation/{task_id}:
    get:
      summary: Get Speech Generation Task
      description: Retrieve the status and result of a speech generation task.
      operationId: speech_2_8_hd_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpeechGenerationResponse'
              example:
                audios:
                  - https://mulerouter.muleusercontent.com/public/xxx/result.mp3
                audio_length: 3.5
                audio_size: 56000
                usage_characters: 42
                word_count: 8
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    SpeechGenerationResponse:
      type: object
      properties:
        audios:
          type: array
          items:
            type: string
            format: uri
          description: List of generated audio file URLs.
        audio_length:
          anyOf:
            - type: number
            - type: 'null'
          description: Audio duration in seconds.
        audio_size:
          anyOf:
            - type: integer
            - type: 'null'
          description: Audio file size in bytes.
        usage_characters:
          anyOf:
            - type: integer
            - type: 'null'
          description: Number of billable characters.
        word_count:
          anyOf:
            - type: integer
            - type: 'null'
          description: Word count in input text.
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
    TaskInfoResponse:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      properties:
        code:
          type: integer
        title:
          type: string
        detail:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 Turbo Text to Speech

> Create a text-to-speech generation task using the speech-2.8-turbo model.

## Overview

Generate speech from text using the MiniMax Speech 2.8 Turbo model. Speech 2.8 Turbo delivers fast, high-quality synthesis:

* **Fast generation** — optimized for speed with Turbo-tier performance
* **Pause tags** — insert precise pauses with `<#x#>` syntax (x = 0.01-99.99 seconds)
* **Interjection tags** — add natural expressions like `(laughs)`, `(sighs)`, `(coughs)`, `(clears throat)`, `(gasps)`, `(sniffs)`, `(groans)`, `(yawns)`
* **Voice settings** — control speed, volume, pitch, and emotion
* **40+ languages** — extensive language support with language boost
* **Audio customization** — configurable format (MP3/PCM/FLAC), sample rate, channel, and bitrate
* **Voice modification** — fine-tune pitch, intensity, and timbre
* **Pronunciation dictionary** — custom pronunciation replacements
* **Loudness normalization** — professional audio level control

## Supported Voice IDs

Speech 2.8 Turbo supports the same 223+ system voice IDs as Speech 2.8 HD, covering 20+ languages including Chinese (Mandarin), Chinese (Cantonese), English, Japanese, Korean, Spanish, Portuguese, French, Indonesian, German, Russian, Italian, Arabic, Turkish, Ukrainian, Dutch, Vietnamese, Thai, Polish, Romanian, Greek, Czech, Finnish, and Hindi.

See the [Speech 2.8 HD documentation](/docs/api-reference/endpoint/minimax/speech-2.8-hd/text-to-speech) for the complete voice ID list.


## OpenAPI

````yaml /api-reference/endpoint/minimax/speech-2.8-turbo/speech-2.8-turbo.yaml POST /vendors/minimax/v1/speech-2.8-turbo/text-to-speech/generation
openapi: 3.1.0
info:
  title: MiniMax Speech 2.8 Turbo API
  description: MiniMax Speech 2.8 Turbo - Text-to-Speech Generation
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/speech-2.8-turbo/text-to-speech/generation:
    post:
      summary: Create Speech Generation Task
      description: >-
        Create a text-to-speech generation task using the speech-2.8-turbo
        model.
      operationId: speech_2_8_turbo_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SpeechGenerationRequest'
            example:
              prompt: Hello, this is a test of speech synthesis.
              voice_setting:
                voice_id: Wise_Woman
                speed: 1
                vol: 1
                pitch: 0
              output_format: url
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    SpeechGenerationRequest:
      type: object
      required:
        - prompt
      properties:
        prompt:
          type: string
          minLength: 1
          maxLength: 10000
          description: >
            Text to convert to speech. Use `<#x#>` for pauses (x = 0.01-99.99
            seconds). Supports interjection tags: `(laughs)`, `(sighs)`,
            `(coughs)`, `(clears throat)`, `(gasps)`, `(sniffs)`, `(groans)`,
            `(yawns)`.
        voice_setting:
          $ref: '#/components/schemas/VoiceSetting'
          description: Voice configuration settings (optional, defaults to Wise_Woman).
        audio_setting:
          anyOf:
            - $ref: '#/components/schemas/AudioSetting'
            - type: 'null'
          description: Audio configuration settings.
        language_boost:
          anyOf:
            - type: string
              enum:
                - Chinese
                - Chinese,Yue
                - English
                - Arabic
                - Russian
                - Spanish
                - French
                - Portuguese
                - German
                - Turkish
                - Dutch
                - Ukrainian
                - Vietnamese
                - Indonesian
                - Japanese
                - Italian
                - Korean
                - Thai
                - Polish
                - Romanian
                - Greek
                - Czech
                - Finnish
                - Hindi
                - Bulgarian
                - Danish
                - Hebrew
                - Malay
                - Slovak
                - Swedish
                - Croatian
                - Hungarian
                - Norwegian
                - Slovenian
                - Catalan
                - Nynorsk
                - Afrikaans
                - auto
            - type: 'null'
          description: Enhance recognition of specified languages and dialects.
        output_format:
          type: string
          enum:
            - url
            - hex
          default: hex
          description: 'Format of the output content (non-streaming only). Default: hex.'
        pronunciation_dict:
          anyOf:
            - $ref: '#/components/schemas/PronunciationDict'
            - type: 'null'
          description: Custom pronunciation dictionary for text replacement.
        normalization_setting:
          anyOf:
            - $ref: '#/components/schemas/LoudnessNormalizationSetting'
            - type: 'null'
          description: Loudness normalization settings for the audio.
        voice_modify:
          anyOf:
            - $ref: '#/components/schemas/VoiceModify'
            - type: 'null'
          description: Voice modification settings to adjust pitch, intensity, and timbre.
    TaskCreatedResponse:
      type: object
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    VoiceSetting:
      type: object
      properties:
        voice_id:
          type: string
          description: >-
            Voice ID for synthesis. Examples - Chinese: male-qn-qingse,
            female-shaonv, female-yujie; English: Charming_Lady,
            English_Trustworthy_Man, English_Graceful_Lady. See the Supported
            Voice IDs section in the overview for the full list.
        speed:
          type: number
          minimum: 0.5
          maximum: 2
          default: 1
          description: Speech speed, range [0.5, 2.0].
        vol:
          type: number
          minimum: 0.01
          maximum: 10
          default: 1
          description: Volume, range [0, 10].
        pitch:
          type: integer
          minimum: -12
          maximum: 12
          default: 0
          description: Voice pitch, range [-12, 12].
        emotion:
          anyOf:
            - type: string
              enum:
                - happy
                - sad
                - angry
                - fearful
                - disgusted
                - surprised
                - neutral
            - type: 'null'
          description: Emotion of the generated speech.
        english_normalization:
          type: boolean
          default: false
          description: >-
            Enables English text normalization to improve number reading
            performance.
    AudioSetting:
      type: object
      properties:
        format:
          type: string
          enum:
            - mp3
            - pcm
            - flac
          default: mp3
          description: Audio format.
        sample_rate:
          type: integer
          enum:
            - 8000
            - 16000
            - 22050
            - 24000
            - 32000
            - 44100
          default: 32000
          description: Sample rate of generated audio (Hz).
        channel:
          type: integer
          enum:
            - 1
            - 2
          default: 1
          description: Number of audio channels (1=mono, 2=stereo).
        bitrate:
          type: integer
          enum:
            - 32000
            - 64000
            - 128000
            - 256000
          default: 128000
          description: Bitrate of generated audio (bps).
    PronunciationDict:
      type: object
      properties:
        tone_list:
          type: array
          items:
            type: string
          description: >-
            List of pronunciation replacements in format
            ['text/(pronunciation)', ...].
    LoudnessNormalizationSetting:
      type: object
      properties:
        enabled:
          type: boolean
          default: true
          description: Enable loudness normalization for the audio.
        target_loudness:
          type: number
          minimum: -70
          maximum: -10
          default: -18
          description: Target loudness in LUFS.
        target_range:
          type: number
          minimum: 0
          maximum: 20
          default: 8
          description: Target loudness range in LU.
        target_peak:
          type: number
          minimum: -3
          maximum: 0
          default: -0.5
          description: Target peak level in dBTP.
    VoiceModify:
      type: object
      properties:
        pitch:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Pitch adjustment. Range: -100 to 100.'
        intensity:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Intensity/energy of the voice. Range: -100 to 100.'
        timbre:
          type: integer
          minimum: -100
          maximum: 100
          default: 0
          description: 'Timbre adjustment. Range: -100 to 100.'
    TaskInfoCreated:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 Turbo Text to Speech Task

> Retrieve the status and result of a speech generation task.

Retrieve the status and result of a MiniMax Speech 2.8 Turbo text-to-speech generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/minimax/speech-2.8-turbo/speech-2.8-turbo.yaml GET /vendors/minimax/v1/speech-2.8-turbo/text-to-speech/generation/{task_id}
openapi: 3.1.0
info:
  title: MiniMax Speech 2.8 Turbo API
  description: MiniMax Speech 2.8 Turbo - Text-to-Speech Generation
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/speech-2.8-turbo/text-to-speech/generation/{task_id}:
    get:
      summary: Get Speech Generation Task
      description: Retrieve the status and result of a speech generation task.
      operationId: speech_2_8_turbo_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpeechGenerationResponse'
              example:
                audios:
                  - https://mulerouter.muleusercontent.com/public/xxx/result.mp3
                audio_length: 3.5
                audio_size: 56000
                usage_characters: 42
                word_count: 8
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    SpeechGenerationResponse:
      type: object
      properties:
        audios:
          type: array
          items:
            type: string
            format: uri
          description: List of generated audio file URLs.
        audio_length:
          anyOf:
            - type: number
            - type: 'null'
          description: Audio duration in seconds.
        audio_size:
          anyOf:
            - type: integer
            - type: 'null'
          description: Audio file size in bytes.
        usage_characters:
          anyOf:
            - type: integer
            - type: 'null'
          description: Number of billable characters.
        word_count:
          anyOf:
            - type: integer
            - type: 'null'
          description: Word count in input text.
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
    TaskInfoResponse:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      properties:
        code:
          type: integer
        title:
          type: string
        detail:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Music 2.5 Text to Music

> Create a music generation task using the music-2.5 model.

## Overview

Generate music from text descriptions and lyrics using the MiniMax Music 2.5 model. Music 2.5 is the latest version with improved quality:

* **Style description** — specify music style, mood, and scenario via `prompt`
* **Lyrics support** — provide song lyrics with `lyrics_prompt`
* **Structure tags** — organize songs with `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]` tags
* **Up to 5 minutes** — generate songs up to 5 minutes long
* **Audio customization** — configurable format (MP3/PCM/FLAC), sample rate, and bitrate
* **Improved quality** — enhanced music generation compared to Music 2.0


## OpenAPI

````yaml /api-reference/endpoint/minimax/music-2.5/music-2.5.yaml POST /vendors/minimax/v1/music-2.5/text-to-music/generation
openapi: 3.1.0
info:
  title: MiniMax Music 2.5 API
  description: MiniMax Music 2.5 - Music Generation from Lyrics and Style Description
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/music-2.5/text-to-music/generation:
    post:
      summary: Create Music Generation Task
      description: Create a music generation task using the music-2.5 model.
      operationId: music_2_5_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MusicGenerationRequest'
            example:
              prompt: Acoustic, indie folk, gentle and reflective mood
              lyrics_prompt: |-
                [Intro]
                (Guitar strumming)

                [Verse]
                Sitting by the window
                Watching the rain fall down

                [Chorus]
                But I know tomorrow
                Will bring a brand new day
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    MusicGenerationRequest:
      type: object
      required:
        - prompt
        - lyrics_prompt
      properties:
        prompt:
          type: string
          minLength: 10
          maxLength: 2000
          description: >-
            A description of the music, specifying style, mood, and scenario.
            10-2000 characters.
        lyrics_prompt:
          type: string
          minLength: 10
          maxLength: 3000
          description: >
            Lyrics of the song. Use \n to separate lines. You may add structure
            tags like [Intro], [Verse], [Chorus], [Bridge], [Outro] to enhance
            the arrangement. 10-3000 characters.
        audio_setting:
          anyOf:
            - $ref: '#/components/schemas/AudioSetting'
            - type: 'null'
          description: Audio configuration settings.
    TaskCreatedResponse:
      type: object
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    AudioSetting:
      type: object
      properties:
        format:
          type: string
          enum:
            - mp3
            - pcm
            - flac
          default: mp3
          description: Audio format.
        sample_rate:
          type: integer
          enum:
            - 8000
            - 16000
            - 22050
            - 24000
            - 32000
            - 44100
          default: 44100
          description: Sample rate of generated audio (Hz).
        bitrate:
          type: integer
          enum:
            - 32000
            - 64000
            - 128000
            - 256000
          default: 256000
          description: Bitrate of generated audio (bps).
    TaskInfoCreated:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Music 2.5 Text to Music Task

> Retrieve the status and result of a music generation task.

Retrieve the status and result of a MiniMax Music 2.5 music generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/minimax/music-2.5/music-2.5.yaml GET /vendors/minimax/v1/music-2.5/text-to-music/generation/{task_id}
openapi: 3.1.0
info:
  title: MiniMax Music 2.5 API
  description: MiniMax Music 2.5 - Music Generation from Lyrics and Style Description
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/music-2.5/text-to-music/generation/{task_id}:
    get:
      summary: Get Music Generation Task
      description: Retrieve the status and result of a music generation task.
      operationId: music_2_5_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MusicGenerationResponse'
              example:
                audio: https://mulerouter.muleusercontent.com/public/xxx/result.mp3
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    MusicGenerationResponse:
      type: object
      properties:
        audio:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: Generated music file URL.
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
    TaskInfoResponse:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      properties:
        code:
          type: integer
        title:
          type: string
        detail:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Music 2.0 Text to Music

> Create a music generation task using the music-2.0 model.

## Overview

Generate music from text descriptions and lyrics using the MiniMax Music 2.0 model. Music 2.0 offers:

* **Style description** — specify music style, mood, and scenario via `prompt`
* **Lyrics support** — provide song lyrics with `lyrics_prompt`
* **Structure tags** — organize songs with `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]` tags
* **Up to 5 minutes** — generate songs up to 5 minutes long
* **Audio customization** — configurable format (MP3/PCM/FLAC), sample rate, and bitrate


## OpenAPI

````yaml /api-reference/endpoint/minimax/music-2.0/music-2.0.yaml POST /vendors/minimax/v1/music-2.0/text-to-music/generation
openapi: 3.1.0
info:
  title: MiniMax Music 2.0 API
  description: MiniMax Music 2.0 - Music Generation from Lyrics and Style Description
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/music-2.0/text-to-music/generation:
    post:
      summary: Create Music Generation Task
      description: Create a music generation task using the music-2.0 model.
      operationId: music_2_0_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MusicGenerationRequest'
            example:
              prompt: Acoustic, indie folk, gentle and reflective mood
              lyrics_prompt: |-
                [Intro]
                (Guitar strumming)

                [Verse]
                Sitting by the window
                Watching the rain fall down

                [Chorus]
                But I know tomorrow
                Will bring a brand new day
      responses:
        '202':
          description: Accepted - Task created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskCreatedResponse'
              example:
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: pending
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    MusicGenerationRequest:
      type: object
      required:
        - prompt
        - lyrics_prompt
      properties:
        prompt:
          type: string
          minLength: 10
          maxLength: 2000
          description: >-
            A description of the music, specifying style, mood, and scenario.
            10-2000 characters.
        lyrics_prompt:
          type: string
          minLength: 10
          maxLength: 3000
          description: >
            Lyrics of the song. Use \n to separate lines. You may add structure
            tags like [Intro], [Verse], [Chorus], [Bridge], [Outro] to enhance
            the arrangement. 10-3000 characters.
        audio_setting:
          anyOf:
            - $ref: '#/components/schemas/AudioSetting'
            - type: 'null'
          description: Audio configuration settings.
    TaskCreatedResponse:
      type: object
      properties:
        task_info:
          $ref: '#/components/schemas/TaskInfoCreated'
    AudioSetting:
      type: object
      properties:
        format:
          type: string
          enum:
            - mp3
            - pcm
            - flac
          default: mp3
          description: Audio format.
        sample_rate:
          type: integer
          enum:
            - 8000
            - 16000
            - 22050
            - 24000
            - 32000
            - 44100
          default: 44100
          description: Sample rate of generated audio (Hz).
        bitrate:
          type: integer
          enum:
            - 32000
            - 64000
            - 128000
            - 256000
          default: 256000
          description: Bitrate of generated audio (bps).
    TaskInfoCreated:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - pending
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

> ## Documentation Index
> Fetch the complete documentation index at: https://mulerouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Music 2.0 Text to Music Task

> Retrieve the status and result of a music generation task.

Retrieve the status and result of a MiniMax Music 2.0 music generation task using the `task_info.id` returned from the POST request.


## OpenAPI

````yaml /api-reference/endpoint/minimax/music-2.0/music-2.0.yaml GET /vendors/minimax/v1/music-2.0/text-to-music/generation/{task_id}
openapi: 3.1.0
info:
  title: MiniMax Music 2.0 API
  description: MiniMax Music 2.0 - Music Generation from Lyrics and Style Description
  version: 2.0.0
servers:
  - url: https://api.mulerouter.ai/
security:
  - bearerAuth: []
paths:
  /vendors/minimax/v1/music-2.0/text-to-music/generation/{task_id}:
    get:
      summary: Get Music Generation Task
      description: Retrieve the status and result of a music generation task.
      operationId: music_2_0_get
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MusicGenerationResponse'
              example:
                audio: https://mulerouter.muleusercontent.com/public/xxx/result.mp3
                task_info:
                  id: 8e1e315e-b50d-4334-a231-be7d19a372f4
                  status: completed
                  created_at: '2026-03-03T00:00:00Z'
                  updated_at: '2026-03-03T00:00:00Z'
components:
  schemas:
    MusicGenerationResponse:
      type: object
      properties:
        audio:
          anyOf:
            - type: string
              format: uri
            - type: 'null'
          description: Generated music file URL.
        task_info:
          $ref: '#/components/schemas/TaskInfoResponse'
    TaskInfoResponse:
      type: object
      required:
        - id
        - status
        - created_at
        - updated_at
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - completed
            - pending
            - processing
            - failed
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        error:
          $ref: '#/components/schemas/TaskInfoErrorObject'
    TaskInfoErrorObject:
      type: object
      properties:
        code:
          type: integer
        title:
          type: string
        detail:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````

---
===========🔐™️®️©️🔐===========

---

