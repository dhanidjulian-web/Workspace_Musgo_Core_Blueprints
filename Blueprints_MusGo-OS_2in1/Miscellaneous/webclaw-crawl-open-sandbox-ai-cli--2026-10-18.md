# OpenSandbox Documentation

`https://open-sandbox.ai/cli`

# OpenSandbox CLI


`osb` is the command-line interface for OpenSandbox. It is built for the common day-to-day flows:


- create and manage sandboxes
- run commands inside a sandbox
- read and modify sandbox files
- inspect runtime egress policy
- manage sandbox-local Credential Vault state
- collect low-level diagnostics
- install OpenSandbox-specific skills for coding agents
## Install ​
## Before You Start ​
## Quick Start ​
*Use -- before the sandbox command payload.*

## Common Tasks ​
*--image, --template, and --snapshot-id are mutually exclusive.*

## Output Formats ​
## Command Groups ​
## Agent Skills ​
## Configuration Model ​
## Development ​











It uses the OpenSandbox Python SDK under the hood and is intended to be the shortest path from a terminal to a working sandbox workflow.


## Install

pip uv pipx bash

```
pip install opensandbox-cli
```

bash

```
uv tool install opensandbox-cli
```

bash

```
pipx install opensandbox-cli
```


Confirm the install:

bash

```
osb --help
osb --version
```


## Before You Start


Make sure an OpenSandbox server is reachable. If you are running locally, start the server first and then point the CLI at it.

bash

```
opensandbox-server
```


## Quick Start


### 1. Initialize config

bash

```
osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set connection.api_key <your-api-key>
osb config show -o json
```


If you want a non-default config file, choose it at the root command level for the whole invocation:

bash

```
osb --config /tmp/dev.toml config init
osb --config /tmp/dev.toml config set connection.domain localhost:8080
osb --config /tmp/dev.toml config show -o json
```


### 2. Create a sandbox

bash

```
osb sandbox create --image python:3.12 --timeout 30m -o json
```


If you set defaults first, later create commands can be shorter:

bash

```
osb config set defaults.image python:3.12
osb config set defaults.timeout 30m
osb sandbox create -o json
```


### 3. Verify it is usable

bash

```
osb sandbox get <sandbox-id> -o json
osb sandbox health <sandbox-id> -o json
```


### 4. Run a command inside the sandbox


Use `--` before the sandbox command payload.

bash

```
osb command run <sandbox-id> -o raw --argv -- python -c "print(1 + 1)"
```


### 5. Read or write a file

bash

```
osb file write <sandbox-id> /tmp/hello.txt -c "hello" -o json
osb file cat <sandbox-id> /tmp/hello.txt -o raw
```


### 6. Clean up

bash

```
osb sandbox kill <sandbox-id> -o json
```


`kill` now returns `status: "deletion_requested"` instead of `terminated`; update scripts that match this value. It confirms request acceptance. To wait for deletion, see [cleanup completion](https://open-sandbox.ai/architecture/control-plane/server#asynchronous-lifecycle-with-absolute-expiration).


## Common Tasks


### Create sandboxes


Basic:

bash

```
osb sandbox create --image python:3.12
```


Private image:

bash

```
osb sandbox create \
  --image my-registry.example.com/team/app:latest \
  --image-auth-username alice \
  --image-auth-password <token>
```


Manual cleanup mode:

bash

```
osb sandbox create --image python:3.12 --timeout none
```


Explicit entrypoint argv:

bash

```
osb sandbox create \
  --image python:3.12 \
  --entrypoint python \
  --entrypoint -m \
  --entrypoint http.server
```


Create with network policy and volumes:

bash

```
osb sandbox create \
  --image python:3.12 \
  --network-policy-file network-policy.json \
  --volumes-file volumes.json
```


Create with Credential Vault proxy enabled:

bash

```
osb sandbox create --image python:3.12 --network-policy-file network-policy.json --credential-proxy -o json
```


Create from a template (golden image):

bash

```
osb sandbox create --template <template-id> --timeout 30m -o json
```


Template mode fixes the workload shape on the server: `--image`, `--env`, `--resource`, `--entrypoint`, `--volumes-file`, and `--credential-proxy` cannot be combined with `--template`. Only `--timeout` (required), `--metadata`, `--extension`, and `--network-policy-file` may accompany it. Only templates in the `Succeeded` phase can be used. See [Manage templates](https://open-sandbox.ai/cli/#manage-templates).


Create from a snapshot:

bash

```
osb sandbox create --snapshot-id <snapshot-id> --timeout 30m -o json
```


`--image`, `--template`, and `--snapshot-id` are mutually exclusive.


### Manage templates


Templates are golden-image builds; the build runs asynchronously, so poll `template get` until the status phase is `Succeeded`. Template management requires a Kubernetes-backed runtime.

bash

```
osb template create --image python:3.12 --publish s3://bucket/publish -o json
osb template get <template-id> -o json
osb template list -o json
osb template delete <template-id> -o json
```


`template create` also accepts `--resource cpu=1 memory=512Mi disk=2Gi`, `--entrypoint` (repeat per argv item), `--env KEY=VALUE`, `--metadata KEY=VALUE`, `--format native|overlaybd`, `--readiness-probe`, and `--warmup-seconds`.


### Manage snapshots


Snapshots capture a sandbox's state and can back new sandboxes.

bash

```
osb snapshot create <sandbox-id> --name golden -o json
osb snapshot get <snapshot-id> -o json
osb snapshot list --sandbox-id <sandbox-id> -o json
osb snapshot delete <snapshot-id> -o json
```


### List and inspect sandboxes

bash

```
osb sandbox list
osb sandbox list -o json
osb sandbox list --state running --state paused
osb sandbox get <sandbox-id> -o json
osb sandbox metrics <sandbox-id>
osb sandbox metrics <sandbox-id> --watch -o raw
```


### Pause, resume, and renew

bash

```
osb sandbox pause <sandbox-id> -o json
osb sandbox get <sandbox-id> -o json
# Repeat get with a deadline until status.state is Paused; stop on Failed.
# Only then resume:
osb sandbox resume <sandbox-id> --resume-timeout 60s -o json
osb sandbox renew <sandbox-id> --timeout 30m -o json
```


Pause is asynchronous. A successful pause response means the request was accepted. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume) for runtime-specific behavior.


### Expose a service

bash

```
osb sandbox endpoint <sandbox-id> --port 8080 -o json
```


Use the returned endpoint and headers together. The command resolves a route; it does not start a service or prove that the application is healthy.


### Run commands


Foreground streaming:

bash

```
osb command run <sandbox-id> -o raw -- sh -lc 'echo ready'
```


Tracked background execution:

bash

```
osb command run <sandbox-id> --background -o json -- sh -c "sleep 10; echo done"
osb command status <sandbox-id> <execution-id> -o json
osb command logs <sandbox-id> <execution-id> -o json
```


By default the CLI shell-quotes each argument and joins them into a command string. To use pipelines, redirection, or sandbox-side variable expansion, pass an explicit shell and script:

bash

```
osb command run <sandbox-id> -o raw -- sh -c 'echo "$HOME"; printf "ready\n" | cat'
```


Use `--argv` for native execution without a shell. It requires execd support for the `argv` request field:

bash

```
osb command run <sandbox-id> -o raw --argv -- python3 -c "import sys; print(sys.argv[1:])" "a b" '$HOME' "x'y" ""
osb command interrupt <sandbox-id> <execution-id> -o json
```


Foreground `command run` accepts `-o raw`; background execution accepts `table`, `json`, or `yaml`.


Background execution metadata is returned only after execd confirms startup. An execution error or a stream that ends before this confirmation makes the CLI exit non-zero without printing success metadata. A successful background start does not mean the process has finished; use `command status` and `command logs` to check its eventual result.


Persistent shell session:

bash

```
osb command session create <sandbox-id> --workdir /workspace -o json
osb command session run <sandbox-id> <session-id> -o raw -- pwd
osb command session run <sandbox-id> <session-id> -o raw -- export FOO=bar
osb command session run <sandbox-id> <session-id> -o raw -- sh -c 'echo $FOO'
osb command session delete <sandbox-id> <session-id> -o json
```


### Work with files

bash

```
osb file upload <sandbox-id> ./local.txt /workspace/local.txt -o json
osb file download <sandbox-id> /workspace/result.json ./result.json -o json
osb file search <sandbox-id> /workspace --pattern "*.py" -o json
osb file info <sandbox-id> /workspace/main.py -o json
osb file replace <sandbox-id> /workspace/app.py --old old --new new -o json
osb file chmod <sandbox-id> /workspace/script.sh --mode 755 -o json
```


For regular files, `file download` replaces the local destination only after the entire download succeeds. If the download fails or you interrupt it, an existing file stays unchanged and temporary download files are removed. The destination directory must be writable so the CLI can stage the download before replacing the file.


Existing devices (such as `/dev/null`) and named pipes receive the download directly. They are not replaced, and bytes already written cannot be rolled back if the download fails or is interrupted.


Destinations that refer to standard output, such as `/dev/stdout` and `/dev/fd/1`, stream directly even when stdout is redirected to a regular file. These downloads omit the success message in all output formats so stdout contains only file bytes; errors still go to stderr. A failed or interrupted stream can contain partial data.


### Manage runtime egress policy


Inspect current policy:

bash

```
osb egress get <sandbox-id> -o json
```


Patch specific rules:

bash

```
osb egress patch <sandbox-id> --rule allow=pypi.org --rule deny=internal.example.com -o json
```


If you are debugging connectivity, verify behavior with an actual command:

bash

```
osb command run <sandbox-id> -o raw -- curl -I https://pypi.org
```


### Manage Credential Vault


Credential Vault operations call the sandbox egress sidecar through the Python SDK. Create the sandbox with `--credential-proxy` and an explicit network policy before writing vault state. Template-backed sandboxes do not support Credential Vault. See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for payload examples and revision checks.

bash

```
osb credential-vault create <sandbox-id> --file vault.yaml -o json
osb credential-vault get <sandbox-id> -o json
osb credential-vault patch <sandbox-id> --file mutation.yaml -o json
osb credential-vault credential list <sandbox-id> -o json
osb credential-vault binding list <sandbox-id> -o json
osb credential-vault delete <sandbox-id> -o json
```


WARNING


Use `--file -` to read a JSON/YAML payload from stdin. Do not pass plaintext credential values as command-line flags; keep them in the payload stream or file.


### Collect diagnostics


Use the stable diagnostics commands for API-backed log and event descriptors.

bash

```
osb diagnostics events <sandbox-id> --scope runtime -o raw
osb diagnostics events <sandbox-id> --scope all -o raw
osb diagnostics logs <sandbox-id> --scope container -o raw
osb diagnostics logs <sandbox-id> --scope all -o json
osb diagnostics events <sandbox-id> --scope runtime -o json
osb diagnostics logs <sandbox-id> --scope container -o yaml
```


`--scope` is required for stable diagnostics. The built-in server supports `container` and `all` for logs, and `runtime` and `all` for events. Docker/Kubernetes return `DIAGNOSTICS_SCOPE_UNSUPPORTED` for unavailable scopes, including lifecycle events. Best-effort scopes may include a `warnings` field when the backend can only provide a subset. Raw output prints inline diagnostic text, or the content URL when diagnostics are delivered as a temporary URL; raw output does not download that URL. JSON/YAML use Python model names such as `content_url`, `content_type`, and `expires_at` (the HTTP API uses camelCase). See [Diagnostics](https://open-sandbox.ai/api/#diagnostics) for runtime differences. Older server builds may still return `DIAGNOSTICS_NOT_IMPLEMENTED` for scoped diagnostics.


INFO


Legacy DevOps diagnostics remain experimental. Prefer `osb diagnostics logs/events` for stable API-backed log and event collection.

bash

```
osb devops inspect <sandbox-id> -o raw
osb devops summary <sandbox-id> -o raw
```


## Output Formats


Output selection is command-scoped, not global.


- `table`: human-readable tables and panels
- `json`: machine-readable JSON
- `yaml`: machine-readable YAML
- `raw`: unformatted text or streaming output


Examples:

bash

```
osb sandbox list -o json
osb sandbox list -o yaml
osb file cat <sandbox-id> /workspace/hello.txt -o raw
```


Not every command supports every format. Use `--help` on the specific command when in doubt.


## Command Groups


The main command groups are:


- `osb sandbox`: lifecycle management
- `osb template`: golden-image template builds
- `osb snapshot`: snapshot management
- `osb command`: command execution and persistent sessions
- `osb file`: file and directory operations
- `osb egress`: runtime egress policy
- `osb credential-vault`: sandbox-local credentials and bindings
- `osb diagnostics`: stable diagnostics logs and events
- `osb devops`: experimental legacy diagnostics
- `osb config`: local CLI configuration
- `osb skills`: bundled skills for AI tools


The CLI does not provide Client Pool or pool tracing commands; use the SDK/API for those workflows. A feature in the Python SDK is not automatically a CLI command.


Explore them directly:

bash

```
osb sandbox --help
osb template --help
osb snapshot --help
osb command --help
osb file --help
osb skills --help
```


## Agent Skills


The CLI ships with built-in OpenSandbox skills for coding agents and agent-oriented tools.


Bundled skills:


- `sandbox-lifecycle`
- `command-execution`
- `file-operations`
- `network-egress`
- `sandbox-troubleshooting`


Supported targets:


| Target | Install location |
| --- | --- |
| `claude` | `./.claude/skills/<name>/SKILL.md` or `~/.claude/skills/<name>/SKILL.md` |
| `cursor` | `./.cursor/rules/` or `~/.cursor/rules/` |
| `codex` | `./.codex/skills/<name>/SKILL.md` or `~/.codex/skills/<name>/SKILL.md` |
| `copilot` | `./.github/copilot-instructions.md` or `~/.copilot/copilot-instructions.md` |
| `windsurf` | `./.windsurfrules` or `~/.windsurfrules` |
| `cline` | `./.clinerules` or `~/.cline/rules/opensandbox-<name>.md` |
| `opencode` | `./.agents/skills/<name>/SKILL.md` or `~/.agents/skills/<name>/SKILL.md` |


Common flows:

bash

```
osb skills list
osb skills show sandbox-lifecycle
osb skills install sandbox-lifecycle --target codex --scope project
osb skills install --all-builtins --target codex --scope global
osb skills uninstall sandbox-troubleshooting --target claude --scope global
```


For scripts or agents, use structured output:

bash

```
osb skills install sandbox-lifecycle --target codex --scope project -o json
```


## Configuration Model


The CLI resolves configuration in this order:


1. root CLI flags such as `--api-key`, `--domain`, `--protocol`, `--request-timeout`, `--config`
2. environment variables such as `OPEN_SANDBOX_API_KEY` and `OPEN_SANDBOX_DOMAIN`
3. config file, defaulting to `~/.opensandbox/config.toml`
4. SDK defaults


Config commands:

bash

```
osb config init
osb config show
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set defaults.image python:3.12
osb config set defaults.timeout 30m
```


Example config file:

toml

```
[connection]
api_key = "your-api-key"
domain = "localhost:8080"
protocol = "http"
request_timeout = 30
use_server_proxy = false

[output]
color = true

[defaults]
image = "python:3.12"
timeout = "30m"
```


## Development


For local development in this monorepo:

bash

```
cd cli
uv sync
uv run osb --help
uv run pytest
```


This repository uses a local `uv` source override for the OpenSandbox Python SDK, so running from `cli/` will resolve against the checked-out SDK in the monorepo.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/cli/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/observability`

# SDK Observability
## Pool warmup tracing ​
## Creation metrics ​




Use creation metrics to track sandbox startup latency and pool warmup traces to locate slow phases. They have separate controls and export paths:


| Signal | Use it to | SDK support | Default | Export path |
| --- | --- | --- | --- | --- |
| [Pool warmup traces](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing) | Inspect creation, readiness, preparation, renewal, and idle publication | Python, JavaScript/TypeScript, Kotlin/Java | Off; enable tracing in the connection config | Application-owned OpenTelemetry provider and exporter |
| [Creation metrics](https://open-sandbox.ai/sdks/observability#creation-metrics) | Measure sandbox create latency and success | All five SDKs | On; disable through config or `OPENSANDBOX_DISABLE_METRICS=1` | SDK posts to the lifecycle server, which exports metrics when `[otel]` is enabled |


OpenTelemetry (OTel) provides the tracing and metrics infrastructure; enabling tracing does not enable or disable creation metrics. For remote sandbox logs and events, see the [diagnostics API](https://open-sandbox.ai/api/#diagnostics).


## Pool warmup tracing


The Python, JavaScript/TypeScript, and Kotlin/Java SDKs can emit [OpenTelemetry](https://opentelemetry.io/) traces for the client-side `SandboxPool` warmup path. Each warmup task becomes one trace that covers the full lifecycle — from the moment the reconcile loop submits the task until the warmed sandbox is committed to the idle buffer — with per-phase spans so you can find the actual warmup bottleneck.


Tracing is **opt-in** (`enable_tracing=True` in Python or `enableTracing: true` in JavaScript, or `.enableTracing(true)` on the JVM) and **best-effort**: without an OpenTelemetry SDK + exporter in the application, all span calls are no-ops and nothing is exported. Tracing never affects pool behavior.


### SDK support


| SDK | Pool warmup tracing |
| --- | --- |
| Python async/sync | Phase spans, sandbox identity, terminal classification, readiness counters |
| JavaScript/TypeScript | Phase spans, pool identity, success/failure and error type |
| Kotlin/Java | Phase spans, sandbox identity, terminal classification, readiness counters, SLF4J MDC |
| Go / C# | No built-in pool warmup tracing |


This guide describes the default branch. Check your installed SDK's `ConnectionConfig` for `enable_tracing` / `enableTracing` before enabling it. Tracing defaults to **off**, independently of [create-latency telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics), which defaults to **on**.


### Enabling tracing


#### 1. Add an OpenTelemetry SDK + exporter to your application


These SDKs depend only on the OpenTelemetry API (no-op by default). To actually export traces you bring your own SDK and exporter. For Python:

bash

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```


For Node.js, install an OpenTelemetry SDK and exporter compatible with your application. See the [OpenTelemetry Node.js setup](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/).


For Kotlin/Java:

kotlin

```
dependencies {
    implementation("io.opentelemetry:opentelemetry-api:1.51.0")
    implementation("io.opentelemetry:opentelemetry-sdk:1.51.0")
    implementation("io.opentelemetry:opentelemetry-exporter-otlp:1.51.0")
}
```


#### 2. Configure the global OpenTelemetry provider


Warmup spans use the language's global provider. Configure it at application startup, before creating or starting the pool. In JavaScript, register the provider, async context manager, and W3C propagator with the global `@opentelemetry/api` instance (a Node.js OpenTelemetry SDK can configure these together). For Python, use `opentelemetry.trace.set_tracer_provider(...)`; for Kotlin/Java, configure `GlobalOpenTelemetry`, for example:

java

```
import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;

SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
    .addSpanProcessor(BatchSpanProcessor.create(
        OtlpGrpcSpanExporter.builder()
            .setEndpoint("http://otel-collector:4317")
            .build()))
    .build();

OpenTelemetrySdk sdk = OpenTelemetrySdk.builder()
    .setTracerProvider(tracerProvider)
    .build();

GlobalOpenTelemetry.set(sdk);
```


Propagators


`OpenTelemetrySdk.builder()` defaults to **noop propagators**. If you want the SDK to inject the W3C `traceparent` header into lifecycle requests (so the lifecycle server can join the same trace once it supports tracing), configure W3C propagation explicitly:

java

```
.setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))
```


Sampling


To keep trace volume bounded, use a sampling strategy such as `parentbased_traceidratio(0.1)` on the `SdkTracerProvider`. Trace-id-ratio sampling keeps client and server spans consistent for the same warmup.


#### 3. Turn tracing on for the pool


JavaScript / TypeScript:

ts

```
import { ConnectionConfig } from "@alibaba-group/opensandbox";

const config = new ConnectionConfig({ enableTracing: true });
// Pass config as connectionConfig when constructing SandboxPool.
```


Python:

python

```
from opensandbox.config import ConnectionConfig

config = ConnectionConfig(enable_tracing=True)
```


Kotlin/Java:

java

```
ConnectionConfig config = ConnectionConfig.builder()
    .enableTracing(true)
    .build();

SandboxPool pool = SandboxPool.builder()
    .poolName("demo-pool")
    .maxIdle(3)
    .stateStore(new InMemoryPoolStateStore())
    .connectionConfig(config)
    .creationSpec(PoolCreationSpec.builder().image("ubuntu:22.04").build())
    .build();
```


Pass this connection config to the pool. The SDK flag defaults to `false`; OpenTelemetry exporter and sampling configuration remain application-owned. Shut down the pool before flushing and closing the application tracer provider.


### What is traced


Each warmup task produces **one trace** with a root span and six possible phase types (siblings under the root, so each phase duration stands alone for comparison). Each readiness stage is summarized by one span across all of its delayed attempts; optional stages are absent when they are not configured:


| Span name | Covers |
| --- | --- |
| `pool.warmup` (root) | Warmup task, from admission through completion. Python/JVM backdate it to submission time to include queue wait |
| `pool.warmup.create` | Sandbox creator invocation. The built-in lifecycle path makes one HTTP attempt; readiness is no longer part of this span |
| `pool.warmup.readiness` | Complete pre-prepare readiness stage (`warmupHealthCheck` or `ping`), including all delayed attempts |
| `pool.warmup.prepare` | The single invocation of `warmupSandboxPreparer` (user init script / setup work) |
| `pool.warmup.post_prepare_readiness` | Complete optional post-prepare validation stage, including all delayed attempts |
| `pool.warmup.renew` | TTL renewal right before committing the sandbox |
| `pool.warmup.commit` | Primary-lock renewal + `putIdle` against the state store |


#### Attributes by language


All three SDKs emit `pool.name`, `pool.owner`, `pool.run.generation`, and `pool.leader.epoch`. JavaScript currently adds `warmup.result` (`success` or `failure`) and `warmup.error.type`; it does not emit the sandbox identity, terminal-stage classification, or readiness-attempt counters below. Its success flag alone does not prove that the sandbox was committed to idle.


The following richer root attributes apply to **Python and Kotlin/Java**:


| Attribute | Value |
| --- | --- |
| `pool.name` | Pool name |
| `pool.owner` | Pool owner id |
| `pool.run.generation` | Pool run generation |
| `pool.leader.epoch` | Leader epoch captured when this warmup was admitted |
| `sandbox.id` | Sandbox id when creation progressed far enough to obtain one |
| `sandbox.image` | Creation image |
| `warmup.stage` | Terminal stage: `admission`, `create`, `readiness`, `prepare`, `post_prepare_readiness`, `renew`, or `commit` |
| `warmup.result` | `success`, `failure`, `dropped`, or `cancelled` |
| `warmup.reason` | Stable terminal reason when the result is not successful |
| `warmup.error.category` | Stable error category such as `rate_limit`, `http_4xx`, `http_5xx`, `timeout`, `connection`, `callback`, or `state_store` |
| `warmup.error.type` | Exception class when an error is available |


Python/JVM readiness summary spans additionally expose `warmup.health.attempt_count`, `warmup.health.false_count`, `warmup.health.exception_count`, and `warmup.scheduler.delay_ms`. Failures are recorded with `recordException` on the affected phase span. The root span keeps the classified terminal stage, result, reason, and OpenTelemetry error status without duplicating the phase exception event.


Development snapshot attribute migration


Earlier development snapshots used the unnamespaced `result` and `drop.reason` attributes. The supported schema uses `warmup.result` and `warmup.reason` consistently across traces and structured logs. The old keys are not emitted in parallel; update any dashboards created against a development snapshot.


### Correlating logs to traces


In Kotlin/Java, while a warmup trace is in progress, the pool publishes trace IDs to the SLF4J [MDC](https://www.slf4j.org/api/org/slf4j/MDC.html):


| MDC key | Value |
| --- | --- |
| `trace_id` | Current trace id |
| `span_id` | Current span id |


MDC requires a real SLF4J provider (logback, log4j2, ...). Add the keys to your log pattern once, and every pool log line carries the trace context:

xml

```
<pattern>%d %-5level [%thread] %logger{36} trace_id=%X{trace_id} span_id=%X{span_id} - %msg%n</pattern>
```


### Querying traces


The trace id is random, so a warmup trace cannot be looked up "by pool name" directly. The reliable paths are:


1. **JVM log correlation.** With MDC configured, the pool logs `pool_name` and `sandbox_id` on its warmup lines (e.g. `Pool warmup sandbox entered idle`). Search your logs for a `sandbox_id` — the matching log lines carry `trace_id`, which you can open directly in your trace backend.
2. **Attribute query in the trace backend.** Filter spans by time window and attribute, e.g. TraceQL `{ span.pool.name = "demo-pool" }` (Grafana Tempo), or Jaeger tag search on `pool.name=...`. Backends that derive metrics from spans (Tempo metrics, Datadog span analytics) let you look at `pool.warmup` duration percentiles per `pool.name` first, then drill into slow traces.
3. **Trace-id-ratio sampling.** With sampled traces, `trace_id` in logs and the backend are consistent for the same warmup.


#### Bottleneck drill-down


The readiness counters and backdated queue timing below apply to Python/JVM. For JavaScript, compare phase durations and the four pool identity attributes.


```
pool.warmup root duration (p50/p95/p99) per pool.name
  └─ phase spans: create / readiness / prepare / post_prepare_readiness / renew / commit
       └─ single trace: root start gap = queue wait, then each phase duration
```


| Symptom | Likely cause |
| --- | --- |
| Long gap before `pool.warmup.create` | Create tasks waiting for an executor thread; compare `warmupCreateQps` with create latency |
| Long gap between create and the first readiness span | Expected `warmupHealthCheckInitialDelay`, or delayed-stage capacity exhausted because `warmupConcurrency` is too low |
| `pool.warmup.create` slow | Lifecycle create API slow (for example image pull / execd startup) |
| Slow `pool.warmup.readiness` with a high `warmup.health.attempt_count` | Sandbox startup or the configured readiness predicate is the bottleneck |
| `pool.warmup.prepare` slow | Your `warmupSandboxPreparer` work is the bottleneck |
| Slow `pool.warmup.post_prepare_readiness` with a high attempt count | Prepared service is not yet healthy, or its validation predicate is slow |
| `pool.warmup.renew` slow | Lifecycle API TTL renewal |
| `pool.warmup.commit` slow | State-store lease renewal or idle publication (for example Redis round-trips) |


## Creation metrics


OpenSandbox SDKs report sandbox creation latency to the configured lifecycle server by default. This reporting is separate from opt-in [pool warmup tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing). Reporting is best-effort: failures never affect `Sandbox.create`, and the payload contains no user content.


### Requirements


The `POST /v1/metrics/events` endpoint and the SDK reporters described below require the following minimum versions. Older SDKs simply do not emit events; older servers reject unknown routes with `404`, which the SDK swallows silently (see [Version skew](https://open-sandbox.ai/sdks/observability#version-skew) below).


| Component | Minimum version |
| --- | --- |
| Server (`opensandbox-server`) | `0.2.2` |
| Python SDK (`opensandbox`) | `0.1.15` |
| JavaScript / TypeScript SDK (`@alibaba-group/opensandbox`) | `0.1.11` |
| Go SDK (`github.com/alibaba/OpenSandbox/sdks/sandbox/go`) | `1.0.5` |
| C# SDK (`Alibaba.OpenSandbox`) | `0.1.5` |
| Kotlin / Java SDK (`com.alibaba.opensandbox:sandbox`) | `1.0.17` |


#### Version skew


Reporting is fire-and-forget in every SDK: the POST runs on a background task/thread, and reporting failures are ignored. Debug logging varies by SDK; JavaScript, for example, does not log these failures. This means you can upgrade the SDK and the server independently:


- **New SDK, old server (`< 0.2.2`)**: the server returns `404` for `/v1/metrics/events`. The SDK ignores the response. `Sandbox.create` behavior is unchanged and no user-visible error is raised. A debug message may be emitted depending on the SDK.
- **Old SDK, new server**: the SDK does not emit events. The server histogram simply records nothing for that client.
- **Network errors, TLS failures, timeouts**: same behavior as the `404` case — swallowed, `Sandbox.create` unaffected.


### What is sent


After create succeeds or fails, the SDK fire-and-forget posts to `POST /v1/metrics/events`:

json

```
{
  "eventType": "sandbox.create",
  "sandboxId": "sbx_...",
  "image": "python:3.12",
  "createDurationMs": 1842,
  "success": true
}
```


- `sandboxId` / `image` may be omitted when create fails early.
- SDK language and version come from the HTTP `User-Agent` header (for example `OpenSandbox-Python-SDK/0.1.15`), not from body fields.


The server accepts the event with `204` and, when `[otel]` is enabled, records an OTEL histogram. See [server configuration](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md#otel).


### When it runs


| SDK | Trigger |
| --- | --- |
| Python (async + sync) | After `Sandbox.create` / sync create completes or raises |
| JavaScript / TypeScript | After `Sandbox.create` completes or fails |
| Go | After `CreateSandbox` completes or fails |
| C# | After `Sandbox.CreateAsync` completes or fails |
| Kotlin | After standalone `Sandbox.builder()...build()` or a pool direct-create fallback completes or fails |


Kotlin staged pool warmup


Kotlin staged warmup deliberately does **not** emit the legacy `sandbox.create` event. Its create phase returns before readiness polling, optional preparation, post-prepare validation, renewal, and idle commit, so reporting that partial phase as the existing end-to-end create histogram would give the metric a different meaning from standalone create.


This exclusion applies only to staged warmup. Standalone create and pool direct-create fallback keep reporting normally. Use the pool's structured summary logs and optional [warmup tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing) to observe the complete staged-warmup lifecycle.


### How to disable


Default is on. Opt out with either:


1. Environment variable (all SDKs):

bash

```
export OPENSANDBOX_DISABLE_METRICS=1
```


1. Connection config field:

Python JavaScript Go C# Kotlin python

```
from opensandbox import Sandbox
from opensandbox.config import ConnectionConfig

config = ConnectionConfig(disable_metrics=True)
sandbox = await Sandbox.create("python:3.12", connection_config=config)
```

typescript

```
import { ConnectionConfig, Sandbox } from "@alibaba-group/opensandbox";

const connectionConfig = new ConnectionConfig({ disableMetrics: true });
const sandbox = await Sandbox.create({
  image: "python:3.12",
  connectionConfig,
});
```

go

```
cfg := opensandbox.ConnectionConfig{DisableMetrics: true}
sandbox, err := opensandbox.CreateSandbox(ctx, cfg, opensandbox.SandboxCreateOptions{
    Image: "python:3.12",
})
```

csharp

```
using OpenSandbox;
using OpenSandbox.Config;

var connectionConfig = new ConnectionConfig(new ConnectionConfigOptions
{
    DisableMetrics = true,
});
var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    Image = "python:3.12",
    ConnectionConfig = connectionConfig,
});
```

kotlin

```
import com.alibaba.opensandbox.sandbox.Sandbox
import com.alibaba.opensandbox.sandbox.config.ConnectionConfig

val connectionConfig = ConnectionConfig.builder()
    .disableMetrics(true)
    .build()
val sandbox = Sandbox.builder()
    .image("python:3.12")
    .connectionConfig(connectionConfig)
    .build()
```


These requests go to your configured lifecycle server. Use opt-out when you do not want this additional traffic or create-latency data recorded there.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/observability.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/mcp`

# OpenSandbox MCP Sandbox Server


## Overview
## Overview ​
## Installation & Startup ​
## Integrations ​
## Tools ​
## Minimal Workflow ​
## Usage Examples ​








OpenSandbox MCP Server exposes the OpenSandbox Python SDK as MCP tools for Claude Code, Cursor, and other MCP-capable clients. It provides focused sandbox lifecycle management, command execution, and text file operations.


## Installation & Startup


### Source

bash

```
cd sdks/mcp/sandbox/python
uv sync
uv run opensandbox-mcp
```


### Package

bash

```
pip install opensandbox-mcp
opensandbox-mcp
```


### Configuration


Environment variables:


- `OPEN_SANDBOX_API_KEY`
- `OPEN_SANDBOX_DOMAIN`


CLI overrides:

bash

```
opensandbox-mcp --api-key ... --domain ... --protocol https
```


Config fields:


- `api_key`: OpenSandbox API key for authentication.
- `domain`: OpenSandbox API domain, for example `api.opensandbox.io`.
- `protocol`: `http` or `https` for API requests.
- `request_timeout_seconds`: HTTP request timeout in seconds.
- `transport`: `stdio` by default, or `streamable-http`.


### Streamable HTTP

bash

```
opensandbox-mcp \
  --transport streamable-http \
  --host 0.0.0.0 \
  --port 8000
```


The HTTP transport defaults to `127.0.0.1:8000`. Set `--host 0.0.0.0` when the MCP server must be reached from another container, and use `--port` to select a different listening port. Keep the default loopback host unless the container network or an upstream gateway protects the exposed endpoint.


## Integrations


### Claude Code stdio

bash

```
claude mcp add opensandbox-sandbox --transport stdio -- \
  opensandbox-mcp --api-key "$OPEN_SANDBOX_API_KEY" --domain "$OPEN_SANDBOX_DOMAIN"
```


### Claude Code http

bash

```
claude mcp add opensandbox-sandbox --transport http http://localhost:8000/mcp
```


### Cursor stdio

json

```
{
  "mcpServers": {
    "opensandbox-sandbox": {
      "command": "opensandbox-mcp",
      "args": [
        "--api-key",
        "${OPEN_SANDBOX_API_KEY}",
        "--domain",
        "${OPEN_SANDBOX_DOMAIN}"
      ]
    }
  }
}
```


### Cursor http

json

```
{
  "mcpServers": {
    "opensandbox-sandbox": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```


## Tools


INFO


- Tools that interact with a sandbox use an ID registered by `sandbox_create` or `sandbox_connect`. `sandbox_list` lists server-side sandboxes without an existing local sandbox registration.
- `file_read`/`file_write` are text-only; use `encoding` and `range_header` for large files.


The MCP server exposes the tool set below, not the complete Python SDK. It does not currently register tools for Client Pool, pool tracing, snapshots, templates, Credential Vault, or stable remote diagnostic logs/events. Use the [SDK guides](https://open-sandbox.ai/sdks/) or [CLI](https://open-sandbox.ai/cli/) for those workflows where supported.


### Sandbox


- `sandbox_create`: create a new sandbox and register it locally
- `sandbox_connect`: attach to an existing sandbox and register it locally
- `sandbox_kill`: terminate a sandbox by ID
- `sandbox_get_info`: fetch sandbox info by ID
- `sandbox_list`: list sandboxes with optional `filter` object
- `sandbox_renew`: extend sandbox expiration
- `sandbox_healthcheck`: check if sandbox is healthy
- `sandbox_get_metrics`: get resource metrics
- `sandbox_get_endpoint`: get network endpoint for a port


### Command Execution


- `command_run`: run a command inside a sandbox
- `command_interrupt`: interrupt a running command


### Filesystem


- `file_read`: read a text file
- `file_write`: write a text file
- `file_delete`: delete files
- `file_search`: search for files by glob
- `file_create_directories`: create directories
- `file_delete_directories`: delete directories
- `file_move`: move/rename files or directories
- `file_replace_contents`: replace file content


## Minimal Workflow


1. `sandbox_create` -> keep the `sandbox_id`.
2. `file_write` code or assets into the sandbox.
3. `command_run` to execute, install dependencies, or start a service.
4. `sandbox_get_endpoint` if you expose a port.
5. `sandbox_kill` when finished.


## Usage Examples


Here are some examples of what you can ask an LLM to do:


- "Create a Python sandbox and run a quick health command."
- "Write a Python script into the sandbox and run it."
- "Download a GitHub repo, install dependencies, and run its tests."
- "Generate a CSV file with fake sales data and run a simple summary script."
- "Start a tiny web server on port 8000 and return the public URL."
- "Build a minimal REST API (hello + health) and expose it on port 8000."
- "Create a tar.gz of /app and report the file size."
- "Build a simple Snake game and return the web endpoint where it can be accessed."[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/mcp.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/control-plane/server`

Return to top

# Lifecycle Server
## Architecture ​
## Design decisions ​
## Where to go next ​





The server is the control plane of an OpenSandbox deployment: one authenticated HTTP API that every SDK, CLI, and MCP client talks to, regardless of what runs the sandboxes. It owns lifecycle orchestration — validating requests, enforcing access control, persisting server-managed records — and delegates the actual sandbox work to a configured runtime backend (Docker, Kubernetes, or the Fast Sandbox integration).


![Sandbox lifecycle states](https://open-sandbox.ai/assets/server-lifecycle.Dn1dDGYh.svg)


## Architecture


![Server internal architecture](https://open-sandbox.ai/assets/server-architecture.eVaXkPOu.svg)


The server is a FastAPI application organized in layers, each replaceable behind an interface:


- **API layer** (`api/`) — thin HTTP routers (lifecycle, proxy, pool, templates, network policy, diagnostics, metrics) with their request/response schemas. All validation happens here.
- **Middleware** (`middleware/`) — cross-cutting concerns: authentication, request IDs, date headers, HTTP metrics, CORS.
- **Service layer** (`services/`) — the lifecycle state machines and runtime integrations, described below.
- **Repositories** (`repositories/`) — persistence for server-managed records only.
- **Tenants** (`tenants/`) — pluggable identity providers that resolve a request's tenant from its API key.
- **Integrations** (`integrations/`) — optional add-ons, such as renew-on-access consumers and OpenTelemetry metrics.


Two rules define the layering, and both exist to keep the control plane honest and replaceable:


1. **The API never talks to a runtime directly.** Everything goes through a service interface, so backend specifics never leak past the boundary — which is why the API layer can stay thin and the runtime can be swapped by configuration alone.
2. **Sandboxes are not rows in the server's database.** The Docker container, the Kubernetes resources, or the fast-sandbox CRs are the source of truth. The server persists only what it owns (snapshot metadata and the template catalog), which is what makes the storage backend swappable and failover tractable at all.


## Design decisions


### One contract over pluggable runtimes


All runtimes implement one `SandboxService` interface, selected by configuration (`runtime.type`): Docker for local and single-host deployments, Kubernetes for container workloads via the controller or agent-sandbox, and Fast Sandbox for template-backed microVMs. Under Kubernetes, `CompositeSandboxService` composes the container workload provider with `FastSandboxService` — a `templateId` -based create or an `fsb-` -prefixed ID routes to Fast Sandbox, everything else to the container provider. The API, response models, and SDKs are identical across all three; the Fast Sandbox composition is described in [Fast Sandbox](https://open-sandbox.ai/architecture/fast-sandbox/).


### Asynchronous lifecycle with absolute expiration


Creation returns before the sandbox is running (`Pending`), and clients poll status or use SDK readiness helpers. This keeps the API non-blocking for slow runtimes — provisioning a pod or a microVM must never hold an HTTP request open. Expiration is an absolute TTL rather than an idle timeout: server or runtime restarts do not reset it, so a sandbox's lifetime is auditable from creation time alone.


A sandbox is observed as `Pending` or `Running`, moves through the `Pausing` / `Paused` / `Resuming` / `Stopping` transitions, and ends in `Terminated` (exit code 0) or `Failed` (non-zero). `resume()` is deliberately a pause-state operation, never a general restart: a workload that already exited is `Terminated` or `Failed`, and the honest answer to that is a replacement sandbox, not a silent revive. Pausing on Kubernetes keeps the sandbox ID and restores the root filesystem — with the opt-in QEMU mode, even guest memory. See [Pause & Resume](https://open-sandbox.ai/guides/pause-resume).


For Kubernetes BatchSandbox workloads, `DELETE /sandboxes/{id}` returns `204` and SDK `kill()` returns when deletion is accepted. Poll `GET /sandboxes/{id}`: it reports `Stopping` while cleanup finishes, then returns `404`. Under normal managed deletion, non-pooled sandboxes and pools using the default `Delete` strategy wait for pods to disappear; pool `Noop` preserves processes, so its `404` does not confirm runtime termination.


### Endpoint resolution is part of the contract


Clients never guess how to reach a sandbox service. `GET /sandboxes/{id}/endpoints/{port}` returns a reachable address in one of three forms, chosen by runtime and deployment topology: a direct address (Docker host mapping or pod IP), an ingress gateway route, or a server-proxied URL for deployments where neither direct nor gateway paths exist. The proxy is the compatibility fallback, not the fast path.


### Fail-fast security posture


The server refuses to start in an unsafe configuration rather than degrading: no API key in a non-interactive environment is fatal unless insecurity is explicitly acknowledged, the configured runtime is validated against insecure exposure at startup, and with multi-tenancy enabled every enumerable tenant namespace must exist and be accessible before traffic is accepted. Failing at boot is preferred to failing at request time, because misconfigured isolation is invisible per-request.


### Multi-tenancy as namespace isolation


Multi-tenancy is opt-in and Kubernetes-only. API keys come from a tenant provider (a local file or a remote HTTP lookup) instead of a single server key, and each authenticated request is scoped to the tenant's namespace: creates land in it, and reads and mutations only resolve that tenant's sandboxes. Identity lives in a provider — not in server config — so tenant management stays with the platform that owns identities. Pool routes remain a shared resource today. Setup: [Multi-Tenancy](https://open-sandbox.ai/guides/multi-tenancy).


### Scoped persistence, scoped HA


Server-managed records — snapshot metadata and the template catalog — persist to SQLite by default, or PostgreSQL when explicitly configured. The default deployment is **single-active**: one replica, brief API interruption during upgrades, SQLite.


PostgreSQL does not turn the server into a horizontally scaled API. It enables one narrowly scoped multi-replica capability: two replicas coordinating public snapshot creation on the Kubernetes runtime. General load-balanced lifecycle HA is not supported yet — and is not pretended.


The two-replica design avoids leases and leader election by riding on two existing invariants: the `SandboxSnapshot` CR name is deterministic, and the Kubernetes API is already a serialized, watchable store.


1. **Observe before create.** A replica checks for the deterministic-named CR before creating it; a peer's earlier create (even a finished one) is converged on, and a genuine create race is absorbed as `409 AlreadyExists` and treated as success.
2. **CAS on the terminal write.** The terminal database result is written conditionally on the expected prior state, so when two replicas race to finish the same snapshot, one wins and the other's write is a no-op.
3. **Recovery scans.** A crashed replica leaves its row non-terminal; the surviving replica re-scans unfinished rows on an interval and drives them to completion through the same CR observation.


No exactly-once guarantee is claimed across the database, Kubernetes, and the image registry — the recovery interval shapes peer-takeover latency, not atomicity. Helm wiring of the two-replica topology: [Kubernetes Deployment](https://open-sandbox.ai/deployment/#use-postgresql-for-server-persistence).


## Where to go next


- [Kubernetes Controller](https://open-sandbox.ai/architecture/control-plane/operator) — the operator the server programs on Kubernetes
- [Fast Sandbox](https://open-sandbox.ai/architecture/fast-sandbox/) — the template-backed microVM composition
- [Multi-Tenancy](https://open-sandbox.ai/guides/multi-tenancy), [Pause & Resume](https://open-sandbox.ai/guides/pause-resume) — operational guides
- [Server configuration reference](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md) — all keys and defaults[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/control-plane/server.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/pause-resume`

Return to top

# Pause and Resume Guide
## Table of Contents ​
## Overview ​
## Architecture ​
## Prerequisites ​
## Controller Configuration ​
## Registry and Secret Setup ​
*For development with a cluster-internal registry:2 deployment:*

## Usage Guide ​
*Response: 202 Accepted with an empty body.*

*The sandbox transitions through: paused → resuming → running*

## Administrator Guide ​
*The controller creates a short-lived Kubernetes Job for each pause:*

## SandboxSnapshot Reference ​
## Troubleshooting ​
## Getting Help ​
## Measure resume latency ​














This guide explains how to use the pause and resume features for Kubernetes-backed sandboxes in OpenSandbox. Pause commits the sandbox's root filesystem as an OCI image and releases cluster resources. Resume restores the sandbox from that image.


## Table of Contents


- [Overview](https://open-sandbox.ai/guides/pause-resume#overview)
- [Architecture](https://open-sandbox.ai/guides/pause-resume#architecture)
- [Prerequisites](https://open-sandbox.ai/guides/pause-resume#prerequisites)
- [Controller Configuration](https://open-sandbox.ai/guides/pause-resume#controller-configuration)
- [Registry and Secret Setup](https://open-sandbox.ai/guides/pause-resume#registry-and-secret-setup)
- [Usage Guide](https://open-sandbox.ai/guides/pause-resume#usage-guide)
- [Administrator Guide](https://open-sandbox.ai/guides/pause-resume#administrator-guide)
- [SandboxSnapshot Reference](https://open-sandbox.ai/guides/pause-resume#sandboxsnapshot-reference)
- [Troubleshooting](https://open-sandbox.ai/guides/pause-resume#troubleshooting)


---


## Overview


### What Pause and Resume Does


|  | Behavior |
| --- | --- |
| **Pause** | Creates an internal `SandboxSnapshot`, commits the running container root filesystem as an OCI image, then quiesces the sandbox runtime and releases Pods / pooled allocations |
| **Resume** | Reuses the same `BatchSandbox`, rewrites its template to the latest snapshot image, and recreates the runtime from that image |
| **sandboxId** | Stable across pause/resume cycles — callers use the same ID throughout the sandbox lifetime |
| **Replica support** | Currently limited to `BatchSandbox.spec.replicas=1`. Server-created Kubernetes sandboxes use `replicas: 1`; direct CRs with another replica count are rejected by the controller pause entry. |


### Key Design Principle


**Controller-level configuration**: Registry URL and push/pull secrets are configured on the Kubernetes controller manager, not in `~/.sandbox.toml`. SDK users and API callers require **no code changes** to use pause/resume — they just call `pause` and `resume` on the existing sandbox ID.


### Lifecycle

text

```
Time ---------------------------------------------------------------->

Sandbox lifecycle:   [Running]--[Pausing]--[Paused]--[Resuming]--[Running]
                         |                     |
                  commit rootfs          rewrite template images
                  push to registry       recreate runtime from snapshot
                  release pods/alloc
```


### State Machine Details


The sandbox transitions through both stable and intermediate states:


| State | Type | Description |
| --- | --- | --- |
| `Running` | Stable | Sandbox is active and processing requests |
| `Pausing` | Intermediate | Pause operation in progress. Snapshot commit is coordinated through an internal `SandboxSnapshot` resource. |
| `Paused` | Stable | Sandbox is paused, the latest rootfs snapshot is ready, and runtime Pods / pooled allocations have been released |
| `Resuming` | Intermediate | Resume operation in progress. The controller is rewriting the sandbox template to the latest snapshot image and recreating the runtime |
| `Failed` | Stable | Operation failed (check `reason` and `message` for details) |


The Lifecycle API exposes only the coarse-grained sandbox states above. For detailed snapshot progress, inspect the internal `SandboxSnapshot` resource:


Pod termination can continue after the controller reports `Paused`. A resume request can be submitted during this interval; the controller waits for the old Pod to be removed before recreating its replacement. Pods with a deletion timestamp do not contribute new runtime failure conditions, including terminal exit statuses reported by Kubernetes during deletion. Failures already recorded on the sandbox remain terminal, and failures of replacement Pods are still reported normally.


- `Pending`: snapshot request accepted, waiting to resolve source Pod / create commit Job
- `Committing`: commit Job is running and pushing snapshot images
- `Succeed`: snapshot is ready and can be used for the next resume
- `Failed`: snapshot creation failed


### What Is Preserved


|  | Preserved? |
| --- | --- |
| Root filesystem contents | ✅ Yes — committed as OCI image |
| Environment variables | ✅ Yes — from BatchSandbox template |
| Running processes / memory | Rootfs mode: no. Opt-in QEMU-in-runc mode: the QEMU process and Guest memory are restored; other outer processes restart. See [QEMU VMState Snapshots](https://open-sandbox.ai/guides/qemu-vmstate-snapshots). |
| Explicit volume mounts | Depends on volume type |
| Credential Vault entries | No - stored only in egress sidecar memory; re-inject from a trusted control plane after resume |


Pause/resume is currently single-replica only. The internal pause snapshot records one source Pod's container images and does not store per-replica state, so the Kubernetes controller rejects pause requests unless `BatchSandbox.spec.replicas=1`.


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault#persistence-across-pause-and-resume) for the required post-resume credential re-injection procedure.


### Durability and abnormal termination


The root filesystem is durable only after the snapshot reaches `Succeed` and the OCI image has been pushed to the configured registry. A pause request being accepted, or a snapshot being in `Pending` or `Committing`, does not provide a durability guarantee.


Changes made after the last successful snapshot remain in the container's writable layer. They are not automatically snapshotted when the process exits, the container is OOM-killed, the Pod enters `Failed`, the Pod is evicted, or the node becomes unavailable. The lifecycle API does not currently expose a post-failure snapshot or recovery operation, and a new container created by a Kubernetes restart does not inherit the old writable layer.


The image-committer can sometimes read a stopped container directly from containerd while its metadata and writable snapshot still exist on the source node. This is a best-effort operator recovery path, not a supported durability contract: the normal snapshot API requires a `Running` sandbox, and containerd or kubelet garbage collection, Pod replacement, node loss, or a reused container identity can make the old layer unavailable or ambiguous.


For data that must survive an unexpected termination, store it in a persistent volume or an external service and take explicit root filesystem snapshots for reproducible environment state. Files in mounted volumes follow the persistence and backup behavior of that volume; they are not included in the OCI rootfs snapshot.


---


## Architecture


```
API caller
    │ POST /v1/sandboxes/{id}/pause
    ▼
OpenSandbox Server
    │ PATCH BatchSandbox.spec.pause=true
    ▼
BatchSandbox Controller (Kubernetes)
    │ validates lifecycle state
    │ creates internal SandboxSnapshot CR
    ▼
SandboxSnapshot Controller
    │ resolves running Pod
    │ creates commit Job on the same node
    ▼
commit Job Pod (image-committer)
    │ containerd API: commit container rootfs → OCI image
    │ OCI registry resolver: push image
    ▼
SandboxSnapshot.status.phase = Succeed
    │ BatchSandbox.status.phase = Paused
    │ deletes Pods or releases pooled allocation
    ▼
Cluster resources released

--- Later: resume ---

API caller
    │ POST /v1/sandboxes/{id}/resume
    ▼
OpenSandbox Server
    │ PATCH BatchSandbox.spec.pause=false
    ▼
BatchSandbox Controller
    │ reads internal SandboxSnapshot
    │ rewrites pod template images from snapshot
    │ clears poolRef for pooled sandboxes
    │ recreates runtime Pods
    ▼
Sandbox running again with restored filesystem
```


---


## Prerequisites


1. **Kubernetes cluster** with the OpenSandbox controller deployed
2. **OCI-compatible container registry** accessible from cluster nodes (push) and the Kubernetes API (pull)
3. **Kubernetes Secrets** of type `kubernetes.io/dockerconfigjson` for registry authentication
4. **Controller manager** configured with snapshot registry and secret flags


---


## Controller Configuration


Configure the controller manager deployment with snapshot flags:

yaml

```
- --snapshot-registry=registry.example.com/sandboxes
- --snapshot-registry-insecure=false
- --snapshot-push-secret=registry-snapshot-push-secret
- --resume-pull-secret=registry-pull-secret
```


### Configuration Reference


| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `--snapshot-registry` | string | `""` | **Required.** OCI registry prefix. By default, images are stored as `<registry>/<sandboxName>-<container>:snap-gen<N>`. |
| `--snapshot-image-uri-template` | string | `""` | Go named-field template for snapshot image URIs; empty uses the default naming rule below. |
| `--snapshot-registry-insecure` | bool | `false` | Enables insecure registry mode for snapshot push operations. Use only for HTTP or self-signed local registries. |
| `--snapshot-push-secret` | string | `""` | Kubernetes Secret name for pushing snapshots. Must be `kubernetes.io/dockerconfigjson` type. |
| `--image-committer-pod-template-file` | string | `""` | Path to a PodTemplateSpec overlay for commit Job Pods. |
| `--resume-pull-secret` | string | `""` | Kubernetes Secret name injected into resumed sandboxes for pulling snapshot images. Can be the same as push secret. |
| `--image-committer-image` | string | `"image-committer:dev"` | Image used by commit Jobs. |
| `--commit-job-timeout` | duration | `"10m"` | Timeout for commit Jobs. |


### Helm chart support


The `opensandbox-controller` Helm chart now exposes the snapshot-related controller values directly:


- `controller.snapshot.imageCommitterImage`
- `controller.snapshot.imageCommitterPodTemplate`
- `controller.snapshot.commitJobTimeout`
- `controller.snapshot.registry`
- `controller.snapshot.imageURITemplate`
- `controller.snapshot.registryInsecure`
- `controller.snapshot.snapshotPushSecret`
- `controller.snapshot.resumePullSecret`


For the all-in-one `opensandbox` chart, use the same values under the `opensandbox-controller.*` prefix.


### Startup behavior


The server no longer carries dedicated pause/resume config. Missing registry or secret settings are surfaced by the Kubernetes controllers when a `SandboxSnapshot` is processed, for example as `SandboxSnapshot.status.conditions[type=Failed]` with reasons like `RegistryNotConfigured`.


---


## Registry and Secret Setup


### Step 1: Prepare your registry


Any OCI-compatible registry works (Docker Hub, GitHub Container Registry, Harbor, a private `registry:2` instance, etc.). The registry must be:


- **Reachable from cluster nodes** (for the commit Job to push)
- **Reachable from the Kubernetes API server / kubelet** (for image pull on resume)


### Step 2: Create the push secret

bash

```
kubectl create secret docker-registry registry-snapshot-push-secret \
  --docker-server=registry.example.com \
  --docker-username=<username> \
  --docker-password=<password-or-token> \
  --namespace=<sandbox-namespace>
```


### Step 3: Create the pull secret


The pull secret is used by the resumed `BatchSandbox` Pod to pull the snapshot image. It can be the same secret as the push secret if your credentials have both read and write access:

bash

```
kubectl create secret docker-registry registry-pull-secret \
  --docker-server=registry.example.com \
  --docker-username=<username> \
  --docker-password=<password-or-token> \
  --namespace=<sandbox-namespace>
```


### Using a private `registry:2` (development)


For development with a cluster-internal `registry:2` deployment:

bash

```
# Create a registry deployment
kubectl create deployment docker-registry \
  --image=registry:2 --port=5000

kubectl expose deployment docker-registry --port=5000

# No authentication needed for internal registry
# Leave snapshot push/pull secret flags empty on the controller manager
```


---


## Usage Guide


Once the controller manager is configured and the server is running, pause/resume works through the standard Lifecycle API. No SDK changes are needed.


### Pause a sandbox

bash

```
curl -X POST http://localhost:8080/v1/sandboxes/{sandbox_id}/pause \
  -H "Content-Type: application/json"
```


**Response:** `202 Accepted` with an empty body.


The pause is asynchronous. The sandbox transitions through: `running` → `pausing` → `paused`


### Check pause status

bash

```
curl http://localhost:8080/v1/sandboxes/{sandbox_id}
```


When `status` is `paused`, the filesystem has been committed and cluster resources have been released.


### Resume a sandbox

bash

```
curl -X POST http://localhost:8080/v1/sandboxes/{sandbox_id}/resume \
  -H "Content-Type: application/json"
```


**Response:** `202 Accepted` with an empty body.


The sandbox transitions through: `paused` → `resuming` → `running`


### Multiple pause/resume cycles


Pause and resume can be repeated. Each pause cycle produces a new snapshot image tag (`snap-gen1`, `snap-gen2`, ...). The latest snapshot is always used for the next resume.


---


## Administrator Guide


### Controller RBAC


The OpenSandbox controller requires the following RBAC permissions for pause/resume (included in the Helm chart and `make manifests` output):


| Resource | Verbs | Purpose |
| --- | --- | --- |
| `sandboxsnapshots` | get, list, watch, create, update, patch, delete | Manage SandboxSnapshot CRs |
| `jobs` / `jobs/status` | full | Create/monitor commit Jobs |
| `secrets` | get | Validate push secret exists before creating commit Job |
| `pods` | get, list, watch | Find running Pod for commit |


### Snapshot image naming


Internal pause/resume snapshot images are named:


```
<snapshot-registry>/<sandboxName>-<containerName>:snap-gen<N>
```


For example, with `--snapshot-registry=registry.example.com/sandboxes`, sandbox `my-sandbox`, container `sandbox`, first pause:


```
registry.example.com/sandboxes/my-sandbox-sandbox:snap-gen1
```


Server-managed public snapshots use the same repository layout but a stable snapshot-id-derived tag:


```
<snapshot-registry>/<sandboxName>-<containerName>:snap-<snapshotIdHex>
```


The controller distinguishes the two modes by owner reference. Pause/resume snapshots are created by the `BatchSandbox` controller and have a controller ownerReference to the owning `BatchSandbox`; public snapshots are created by the Lifecycle server and do not use that ownerReference.


#### Custom image names


Set `--snapshot-image-uri-template` on the controller manager, or `controller.snapshot.imageURITemplate` in the controller Helm chart, to replace the naming rule. An empty value uses this Go `text/template`:

text

```
{{.Registry}}/{{.SandboxName}}-{{.ContainerName}}:{{.SnapshotTag}}
```


The template receives these named fields:


| Field | Value |
| --- | --- |
| `Registry` | The required `--snapshot-registry` prefix, including any repository path |
| `Namespace` | The snapshot's Kubernetes namespace |
| `SandboxName` | The source BatchSandbox name |
| `SnapshotName` | The SandboxSnapshot name |
| `SnapshotUID` | The SandboxSnapshot UID |
| `SnapshotCreationTime` | The SandboxSnapshot `metadata.creationTimestamp` as a Go `time.Time` in the controller process's local timezone |
| `ContainerName` | The source container name, or `vmstate` for a QEMU VM-state artifact |
| `SnapshotTag` | The existing `snap-gen<N>` or public snapshot tag described above |
| `ArtifactKind` | `rootfs` for container images, or `vmstate` for a QEMU VM-state artifact |


For example, use one repository with a distinct tag for each snapshot artifact:

yaml

```
controller:
  snapshot:
    registry: registry.example.com/sandboxes
    imageURITemplate: '{{.Registry}}/snapshots:{{.SnapshotUID}}-{{.ArtifactKind}}-{{.ContainerName}}'
```


To group images by the snapshot creation date in the controller's local timezone while retaining the sandbox, container, and snapshot tag:

yaml

```
controller:
  snapshot:
    registry: registry.example.com/team
    imageURITemplate: '{{.Registry}}/library/snapshots-{{date "2006-01-02" .SnapshotCreationTime}}:{{.SandboxName}}-{{.ContainerName}}-{{.SnapshotTag}}'
```


The date functions follow Helm's names and argument order and accept a Go `time.Time`, such as `SnapshotCreationTime`:

text

```
{{date "2006-01-02" .SnapshotCreationTime}}
{{dateInZone "2006-01-02" .SnapshotCreationTime "UTC"}}
{{dateInZone "2006-01-02-15-04-05" .SnapshotCreationTime "+08:00"}}
{{dateInZone "2006-01-02" .SnapshotCreationTime "America/New_York"}}
```


`date` uses Go's `time.Local`. `dateInZone` accepts `Local` or an empty timezone for the same default, `UTC` or `Z`, a signed `HH:MM` offset (hours 00–23, minutes 00–59), or an IANA `Area/Location` name. Fixed offsets such as `+05:30` do not change with daylight saving time; named zones follow the rules for the snapshot's creation instant. Unknown zones and malformed offsets fail template execution. These helpers reject a zero timestamp instead of substituting the current time.


On Unix, the local timezone comes from `TZ`, or `/etc/localtime` when `TZ` is unset. In Kubernetes this is the controller container's timezone; set its `TZ` environment variable or provide its timezone files to select the intended local zone. The controller embeds timezone data for named zones when the OS has none.


Formatting uses Go's standard layouts: `2006-01-02` for a date, `20060102-150405` for a compact timestamp, and `2006-01-02-15-04-05.000` for milliseconds. Java-style `yyyy-MM-dd` patterns are not supported. Layouts must produce a valid image reference in their template position: spaces, colons, or uppercase month names are unsuitable in a repository name and fail validation.


Native methods remain available: `.SnapshotCreationTime.Format "2006-01-02"` uses the local timezone, while `.SnapshotCreationTime.UTC.Format "2006-01-02"` selects UTC explicitly. Templates written for the earlier UTC-only field should select UTC explicitly to preserve their date when the controller's local zone is not UTC.


The source is always the snapshot creation timestamp, so retries after midnight keep the same date with the same timezone configuration. Existing commit Jobs retain their resolved targets when the template or timezone setting changes.


For the umbrella chart, nest these values under `opensandbox-controller`. Helm passes the template literally; it does not evaluate the Go template fields. For Kustomize or a direct Deployment, add an argument to the manager container:

yaml

```
- '--snapshot-image-uri-template={{.Registry}}/snapshots:{{.SnapshotUID}}-{{.ArtifactKind}}-{{.ContainerName}}'
```


The controller renders the URI before creating the commit Job. The image committer pushes directly to that URI, and restore uses the recorded reference; there is no intermediate push or rename. QEMU rootfs and VM-state artifacts use the same template and original snapshot tag.


Templates must produce valid tagged OCI image references without a digest. Custom template results are normalized to fully qualified references before they are recorded and passed to the image committer: `snapshots:tag` becomes `docker.io/library/snapshots:tag`, and `team/snapshots:tag` becomes `docker.io/team/snapshots:tag`. Include an explicit registry host (a hostname containing a dot, a host with a port, or `localhost`) to target another registry. An empty template keeps the original naming rule and registry prefix unchanged. Names are not automatically sanitized or truncated. Include fields that keep artifacts and snapshots distinct; the controller rejects duplicate targets within a snapshot, but cannot detect collisions with other snapshots. Template syntax errors prevent controller startup; rendering errors, invalid references, and duplicate targets fail the snapshot before a commit Job is created. Changes apply when creating new commit Jobs; existing Jobs keep their resolved targets, and completed snapshots retain their recorded restore references.


### Runtime compatibility


The built-in `rootfs-v1` image committer requires a container runtime that exposes compatible containerd task pause/resume and writable-snapshot APIs. gVisor RuntimeClasses whose handler is `runsc` do not currently satisfy that contract. The Lifecycle server rejects public snapshot creation for those workloads before it persists a snapshot record or creates a `SandboxSnapshot` resource, leaving the running sandbox untouched.


Native gVisor checkpoint/restore requires a dedicated snapshot backend and is not provided by the `rootfs-v1` committer.


### Commit Job


The controller creates a short-lived Kubernetes `Job` for each pause:


- **Job name**: `<snapshotName>-commit`
- **Node affinity**: Runs on the **same node** as the source Pod (containerd socket access required)
- **Timeout**: 10 minutes (`ActiveDeadlineSeconds`)
- **TTL**: 5 minutes after completion (`TTLSecondsAfterFinished`)
- **Image**: `image-committer` (configurable via controller `--image-committer-image` flag)


The commit Job mounts the host containerd socket from the source node and runs as UID 0. This gives the `image-committer` image node-level container runtime access. Use only a trusted image, preferably pinned by digest or controlled by an admission policy.


The built-in image committer uses containerd APIs directly for container lookup, task pause/unpause, writable-snapshot image creation, and registry push. Before committing, it verifies that the node's content store contains every base-image blob for the node platform and fetches missing blobs from the original image digest; this avoids snapshot failures after CRI discards compressed content during image unpack. Source registries use HTTPS by default. For a trusted source registry that requires skipped TLS verification or plain HTTP, inject `SOURCE_IMAGE_REGISTRY_INSECURE=true` into the `commit` container through the image-committer Pod template. The reusable Go contracts and default implementations are exposed in [`pkg/imagecommitter`](https://github.com/opensandbox-group/OpenSandbox/tree/main/kubernetes/pkg/imagecommitter); provider-specific binaries can supply a credential provider and reuse the standard CLI contract. The Job also retains the host `/run/containerd/fifo` mount so compatible implementations can use containerd task exec. Any preparation command used by the built-in implementation is best effort and does not change the commit interface.


The operator-controlled Pod template can add labels, annotations, a ServiceAccount, scheduling settings, init containers, sidecars, and settings on the required `commit` container such as resources, `env`, and `envFrom`. The template is the merge base, and controller-generated invariants override conflicting template values. The controller reserves the source `nodeName`, restart policy, committer image, image pull policy, command, arguments, security context, termination-message settings, and required environment variables, mounts, and volumes. Environment variables, mounts, and volumes are merged by name, with required controller values winning conflicts. Additional regular sidecars must terminate for the Job to complete.


Any ServiceAccount or admission configuration referenced by the template must exist in every sandbox namespace. Unpause Jobs do not receive the commit Pod template because they do not access the registry.


If the commit Job fails, the controller creates a best-effort `<snapshotName>-unpause` Job on the same node to unpause any source containers that may have been left paused by an abrupt committer exit.


Deleting a `SandboxSnapshot` cleans up Kubernetes commit/unpause Jobs, but does not delete pushed OCI images from the registry. Repeated pause cycles create tags such as `snap-gen<N>`; configure registry retention or garbage collection externally.


### Monitoring


Check SandboxSnapshot status:

bash

```
kubectl get sandboxsnapshot -n <namespace>
# NAME          PHASE       SANDBOX_ID     AGE
# my-snapshot   Succeed     my-sandbox     5m

kubectl describe sandboxsnapshot my-snapshot -n <namespace>
```


Key fields to watch:


- `status.phase`: `Pending` → `Committing` → `Succeed` / `Failed`
- `status.conditions`: readiness or failure reasons with human-readable messages
- `status.containers`: image URIs for each committed container
- `status.sourcePodName` / `status.sourceNodeName`: resolved execution source for the snapshot


#### Monitoring Sandbox State Transitions


When checking sandbox state via the Lifecycle API, you'll see intermediate states:


**Pause flow:**

bash

```
curl http://localhost:8080/v1/sandboxes/{sandbox_id}
# Response during pause:
{
  "id": "my-sandbox",
  "status": {
    "state": "Pausing",
    "reason": "PAUSING",
    "message": "Pausing sandbox"
  }
}
```


**Resume flow:**

bash

```
curl http://localhost:8080/v1/sandboxes/{sandbox_id}
# Response during resume:
{
  "id": "my-sandbox",
  "status": {
    "state": "Resuming",
    "reason": "RESUMING",
    "message": "Resuming sandbox"
  }
}
```


---


## SandboxSnapshot Reference


### Spec fields


| Field | Type | Description |
| --- | --- | --- |
| `sandboxName` | string | Target `BatchSandbox` name in the same namespace |


### Status fields (set by Controller)


| Field | Type | Description |
| --- | --- | --- |
| `phase` | string | `Pending` / `Committing` / `Succeed` / `Failed` |
| `conditions` | list | `Ready` / `Failed` conditions with reason and message |
| `sourcePodName` | string | Pod name used for commit |
| `sourceNodeName` | string | Node where commit Job runs |
| `containers` | list | `{containerName, imageUri, imageDigest}` per container. `imageDigest` is the image config digest, preserving the image ID semantics of earlier image-committer versions. |
| `observedGeneration` | int | Last processed spec generation |


---


## Troubleshooting


### 1. Snapshot stuck in `Failed` — push secret not found


**Cause**: The controller manager was configured with a `--snapshot-push-secret` that does not exist in the sandbox namespace.


**Solution**:

bash

```
kubectl get secret registry-snapshot-push-secret -n <namespace>
# If missing:
kubectl create secret docker-registry registry-snapshot-push-secret \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<token> \
  -n <namespace>
```


The controller validates secret existence **before** creating the commit Job (fail-fast). Once the secret is created, trigger a new pause cycle.


---


### 2. Snapshot stuck in `Committing` for a long time


**Check the commit Job and its Pod:**

bash

```
kubectl get job -n <namespace> -l sandbox.opensandbox.io/snapshot=<snapshotName>
kubectl describe pod <commit-pod-name> -n <namespace>
```


**Common causes:**


| Symptom | Cause | Solution |
| --- | --- | --- |
| `ContainerCreating` for >30s | Secret missing or wrong type | Re-create secret as `kubernetes.io/dockerconfigjson` |
| `FailedMount` event | Secret not found | See issue #1 above |
| Pod running but job never completes | Registry unreachable from node | Check network connectivity from node to registry |
| `unauthorized` in Pod logs | Wrong credentials in secret | Verify secret content with `kubectl get secret ... -o yaml` |


---


### 3. Wrong secret type


Docker registry secrets **must** be type `kubernetes.io/dockerconfigjson`. Generic secrets (`Opaque`) will cause a `FailedMount` error.

bash

```
# Check secret type
kubectl get secret registry-snapshot-push-secret -o jsonpath='{.type}'
# Expected: kubernetes.io/dockerconfigjson

# If wrong type, delete and recreate:
kubectl delete secret registry-snapshot-push-secret
kubectl create secret docker-registry registry-snapshot-push-secret \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<token>
```


---


### 4. Registry unreachable (`Committing` → `Failed` after timeout)


**Symptoms**: Commit Job Pod starts, runs for a while, then fails with a push error.


**Check:**

bash

```
# Inspect commit Pod logs
kubectl logs <commit-pod-name> -n <namespace>

# Test registry connectivity from a node
kubectl run registry-test --rm -it --image=alpine -- \
  wget -O- https://<registry>/v2/ --timeout=5
```


**Common causes:**


- Registry behind a firewall not accessible from cluster nodes
- Self-signed TLS certificate not trusted by containerd
- Wrong registry URL (http vs https)


---


### 5. Resume accepted but the runtime Pod fails to start


**Cause**: The snapshot image cannot be pulled.

bash

```
kubectl describe pod <resumed-pod-name> -n <namespace>
# Look for: ErrImagePull or ImagePullBackOff
```


**Check:**


- `--resume-pull-secret` is correctly configured and the Secret exists in the namespace
- The registry is accessible from the node pulling the image
- The snapshot image was successfully pushed during pause (check `status.containers`)


---


### 6. SandboxSnapshot not being processed (no status)


**Cause**: The OpenSandbox controller is not running.

bash

```
kubectl get pods -n opensandbox-system
kubectl logs -n opensandbox-system deployment/opensandbox-controller-manager
```


---


## Getting Help


- **Documentation**: [OpenSandbox GitHub](https://github.com/opensandbox-group/OpenSandbox)
- **Issues**: [GitHub Issues](https://github.com/opensandbox-group/OpenSandbox/issues)
- **Kubernetes controller**: [Kubernetes Overview](https://open-sandbox.ai/architecture/control-plane/operator)


## Measure resume latency


See [Kubernetes Resume Benchmark](https://open-sandbox.ai/guides/kubernetes-resume-benchmark) for an opt-in rootfs benchmark with raw samples, P50/P95, failure reporting, and explicit cache conditions.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/pause-resume.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/credential-vault`

Return to top

# Credential Vault
## Requirements ​
## How It Works ​
## Persistence Across Pause and Resume ​
## Service Mesh Compatibility ​
*For the underlying egress-sidecar limitation, see Egress.*

## Auth Types ​
## Egress Sidecar Configuration ​
## SDK Quick Reference ​
## Claude Code With Anthropic ​
## Git And Curl With Vault-Injected Credentials ​
## Binding Guidance ​
## Path Ambiguity Guard ​
## Migrating From ports ​
## Experimental Live Credential-Bound Admission (OSEP-0023) ​















Credential Vault is OpenSandbox's outbound credential broker for sandboxed agents and developer tools. Real credentials are written to the egress sidecar by the host-side SDK, while the sandbox process only receives fake or empty credential values. When tools such as Claude Code, Git, curl, package managers, or model API clients make allowed outbound HTTPS requests, the sidecar matches the request against Credential Vault bindings and injects the required authentication headers on the way out. This lets existing tools keep their normal workflows while keeping real secrets out of the sandbox environment, command line, filesystem, and logs, reducing credential exfiltration risk from prompt injection or untrusted code.


## Requirements


- `opensandbox-server` >= 0.2.0
- `egress` >= 1.1.1
- Python SDK >= 0.1.11
- JavaScript/TypeScript SDK >= 0.1.9
- Kotlin SDK >= 1.0.13
- Go SDK >= 1.0.3
- C# SDK >= 0.1.3
- Server config sets `[egress].image`.
- Server config sets `[egress].mode = "dns+nft"`. Credential Vault refuses to activate in DNS-only mode because direct-IP connections can bypass DNS policy.
- Sandbox create request includes an outbound network policy.
- The outbound network policy should use `defaultAction="deny"` and explicitly allow every host referenced by a credential binding. Default-allow remains temporarily supported for backward compatibility but emits a security warning.
- Sandbox create request enables Credential Proxy.
- Sandbox pods are not running with an additional transparent service-mesh sidecar (for example Istio/Envoy injection) in the same network namespace. Credential Vault currently assumes the OpenSandbox egress sidecar is the only transparent outbound interception layer in the pod.
- The sandbox image has the tools you want to run. For Claude Code, use an image with Node.js and npm, such as the OpenSandbox code-interpreter image.


Migration notice


Credential Proxy still requires server `[egress].mode = "dns+nft"`; deployments that cannot provide nft enforcement cannot safely enable credential injection. Default-allow policies remain accepted during the compatibility period, but emit a security warning and should migrate to `defaultAction="deny"` before enforcement is tightened in a future release.


## How It Works


![Credential Vault request flow](https://open-sandbox.ai/assets/credential-vault.D1G0mnIx.png)


Credential Vault is implemented by the egress sidecar. A sandbox must be created with both an outbound `network_policy` / `networkPolicy` and Credential Proxy enabled. The lifecycle API field name is `credentialProxy.enabled`; SDKs expose that field using their language-specific naming conventions.


At a high level:


1. The lifecycle server attaches the egress sidecar to the sandbox.
2. The SDK writes credentials and bindings to the sidecar Credential Vault API.
3. The sandbox process runs with fake or empty credential environment variables.
4. When the sandbox makes an HTTPS request, transparent MITM in the sidecar inspects the request metadata.
5. If exactly one binding matches the request scheme, host, port, method, and path, the sidecar injects the configured auth header and scoped placeholder substitutions.
6. Secret values are redacted from vault responses and response headers.


When the active-vault check succeeds, requests that do not match any credential binding are forwarded unchanged. Credential path-safety checks apply only after a binding matches and the request would otherwise receive credentials. The active-vault check itself runs before binding selection for every intercepted flow, including requests to hosts that would not match a binding.


The active vault used by the MITM process is served over a local Unix domain socket inside the sidecar. The sandbox workload cannot fetch this active state over the normal server proxy path.


Each new flow conditionally reads that private endpoint with the cached opaque snapshot tag in `If-None-Match`. A `304 Not Modified` response reuses the same immutable in-process snapshot without rendering or transferring secret values; a `200 OK` response carries a fully validated replacement snapshot and a new opaque `ETag`. Successful create and patch responses are acknowledged only after the store has changed that tag, so the next flow immediately observes the new credentials without a cache-TTL delay.


The opaque tag is separate from the public vault revision. Deleting a vault and creating it again can reset the public revision to `1`, but the recreated vault receives a different tag and cannot reuse plaintext from the deleted snapshot. A `404 Not Found` from the private endpoint is the normal "no active vault" result: the MITM process clears its cached snapshot and continues without credential injection.


Runtime availability dependency


The private active-vault socket is a hard availability dependency for all traffic intercepted by Credential Proxy, not only traffic that ultimately matches a credential binding. A timeout, refused connection, unexpected EOF, `5xx` response, malformed snapshot, or invalid `ETag` clears the affected plaintext cache and fails the request closed before any upstream forwarding. Small requests whose bodies are safely buffered receive a local `503 Service Unavailable` response. Requests that are already streaming, may cross the streaming threshold, or have an unknown body length are terminated instead, because mitmproxy cannot safely synthesize a local response after streaming has started. Operators should monitor the sidecar and private socket as part of the egress data plane's availability.


## Persistence Across Pause and Resume


In-memory state


Credential Vault entries are process-local memory in the egress sidecar; they are not part of the sandbox root filesystem or the `BatchSandbox` Pod template. Kubernetes pause deletes the Pod after snapshotting, so the fresh egress sidecar created by resume starts with an empty vault. Credential injection does not resume until a trusted client creates the credentials and bindings again.


Keep the original vault request or an equivalent secret-manager reference in a trusted control plane outside the sandbox. After the sandbox returns to `Running`, call the Credential Vault create API again before allowing work that depends on those credentials. Do not persist real credential values in sandbox metadata, environment variables, snapshots, or logs.


Docker pause/unpause retains the existing container processes, but any egress sidecar replacement or restart also creates a new in-memory vault and requires the same re-injection procedure.


Fast-sandbox profile: server-routed vault


For template-backed (fsb) sandboxes the vault is egress-held: the server pushes complete vault revisions to the egress vault over the FastPath handler relay and the relay response is the synchronous egress-validated ack. The same SDK entry points (`sandbox.credential_vault` / `credentialVault` / `CredentialVault`) work for template-backed sandboxes through the server-routed API — no sidecar endpoint is resolved. The vault is **not** carried at create time: create the sandbox first, then call the vault API.


Everything else is unchanged for this profile: values are write-only and stripped from every read, `PATCH` is atomic (composed server-side over the relay; a `412` means another writer won the revision — re-read and retry with the fresh `expectedRevision`), and the vault persists egress-locally (memory plus one plaintext v1 file per sandbox under a Pod-scoped `emptyDir`), so an egress container restart inside the live Pod recovers locally when the Fastlet replays the bindings, and a Kubernetes pause/resume carries the vault files in the snapshot bundle (export strictly before teardown, re-stamped import at restore). The vault volume is part of the credential trust surface (mount it with `medium: Memory` to keep plaintext off node disk). See [fast-sandbox networking](https://open-sandbox.ai/architecture/fast-sandbox/networking#credential-delivery).


## Service Mesh Compatibility


Credential Vault depends on the egress sidecar's transparent redirect and MITM path. If the sandbox pod is also injected with a transparent service-mesh sidecar such as Istio/Envoy, both layers will try to intercept outbound traffic in the same network namespace. OpenSandbox does not currently support that combination for Credential Vault.


Use one of these operator patterns instead:


- disable mesh sidecar injection for sandbox pods that need Credential Vault
- keep mesh injection enabled, but do not enable `credentialProxy` / Credential Vault for those pods
- move outbound policy and credential handling to a platform mechanism outside the sandbox pod if mesh injection is mandatory


For the underlying egress-sidecar limitation, see [Egress](https://open-sandbox.ai/architecture/network/egress#service-mesh-compatibility).


Credential bindings are intentionally precise. A default-deny egress policy is required. Use a narrow path match, for example `/v1/*` for Anthropic API calls.


## Auth Types


Each binding uses an `auth` rule to describe how the referenced credential is rendered into the outbound request:


- `bearer`: injects `Authorization: Bearer <credential>`.
- `basic`: injects `Authorization: Basic <credential>`. The credential value must already be base64-encoded `username:password`.
- `apiKey`: injects the credential value into the configured header name.
- `customHeaders`: injects multiple configured headers, each backed by its own credential.
- `passthrough`: does not inject an auth header. Use it with `substitutions` when the upstream API requires a credential in a path, query string, or body placeholder instead of a header.


Simple examples:

python

```
auth={"type": "bearer", "credential": "github-token"}
```

http

```
Authorization: Bearer <github-token>
```

python

```
auth={"type": "basic", "credential": "registry-basic"}
```

http

```
Authorization: Basic <base64(username:password)>
```

python

```
auth={"type": "apiKey", "name": "x-api-key", "credential": "anthropic-api-key"}
```

http

```
x-api-key: <anthropic-api-key>
```

python

```
auth={
    "type": "customHeaders",
    "headers": [
        {"name": "X-Client-Id", "credential": "client-id"},
        {"name": "X-Client-Secret", "credential": "client-secret"},
    ],
}
```

http

```
X-Client-Id: <client-id>
X-Client-Secret: <client-secret>
```


### Scoped Placeholder Substitutions


Some upstream APIs require credentials in a request URL or body instead of a dedicated auth header. Credential Vault can handle those APIs without placing the real credential in the sandbox process. All auth types accept an optional `substitutions` list. Each substitution names a credential, a literal placeholder, and the request surfaces where replacement is allowed:

python

```
auth={
    "type": "passthrough",
    "substitutions": [
        {
            "credential": "client-secret",
            "placeholder": "__client_secret__",
            "in": ["body", "query"],
        }
    ],
}
```


Use `type="passthrough"` when the binding only performs substitutions and should not inject an auth header. You can also combine substitutions with `bearer`, `basic`, `apiKey`, or `customHeaders` when the same upstream request needs both header injection and placeholder replacement.


Substitution is disabled by default and is exact, literal, and case-sensitive. Only the configured surfaces are rewritten:


| Surface | Behavior |
| --- | --- |
| `path` | Replaces placeholders in the request path and URL-encodes the credential value. If the rewritten path contains ambiguous path segments, encoded separators, or traversal-like content, the sidecar rejects the request instead of forwarding a secret-bearing URL outside the matched scope. |
| `query` | Replaces placeholders in the query string and URL-encodes the credential value. |
| `header` | Replaces placeholders in the original request headers, excluding hop-by-hop and security-sensitive headers such as `Host`, `Content-Length`, and forwarding headers. Substitutions run before Credential Vault injects auth headers, so the sidecar does not rewrite the credential headers it creates. |
| `body` | Replaces placeholders in UTF-8 request bodies. For `application/json`, the replacement is encoded as JSON string contents, so put the placeholder inside a quoted JSON string. For `application/x-www-form-urlencoded`, the replacement is form-encoded. Compressed and multipart bodies are skipped. |


The sidecar applies all replacements for a surface against the original request text in one pass. Inserted credential values are not scanned again for later placeholders, which prevents one secret from accidentally rewriting another secret. When a body is rewritten, the sidecar updates `Content-Length` and removes `Transfer-Encoding` because the forwarded request now has a fixed-size buffered body.


The placeholder, raw credential value, URL-encoded value, form-encoded value, and JSON-escaped values are added to the active redaction set. A binding with substitutions that matched the request but did not find any placeholder emits a substitution-miss log without exposing credential values.


Example configuration:

python

```
await sandbox.credential_vault.create(
    credentials=[
        Credential(name="tenant-id", source={"value": "tenant 42"}),
        Credential(name="api-key", source={"value": "query secret+value"}),
        Credential(name="client-secret", source={"value": 'body "secret" value'}),
    ],
    bindings=[
        CredentialBinding(
            name="token-request",
            match={
                "schemes": ["https"],
                "hosts": ["api.example.com"],
                "methods": ["POST"],
                "paths": ["/tenants/__tenant_id__/token"],
            },
            auth={
                "type": "passthrough",
                "substitutions": [
                    {
                        "credential": "tenant-id",
                        "placeholder": "__tenant_id__",
                        "in": ["path"],
                    },
                    {
                        "credential": "api-key",
                        "placeholder": "__api_key__",
                        "in": ["query"],
                    },
                    {
                        "credential": "client-secret",
                        "placeholder": "__client_secret__",
                        "in": ["body"],
                    },
                ],
            },
        )
    ],
)
```


The sandbox can use placeholders instead of real secrets:

bash

```
curl -X POST \
  "https://api.example.com/tenants/__tenant_id__/token?api_key=__api_key__" \
  -H "content-type: application/json" \
  --data '{"client_secret":"__client_secret__"}'
```


The upstream receives the rewritten request:

http

```
POST /tenants/tenant%2042/token?api_key=query%20secret%2Bvalue HTTP/1.1
content-type: application/json

{"client_secret":"body \"secret\" value"}
```


## Egress Sidecar Configuration


| Environment variable | Default | Description |
| --- | --- | --- |
| `OPENSANDBOX_EGRESS_CREDENTIAL_VAULT_REQUIRE_TLS` | off | When enabled (`true` / `1` / `on`), credential vault write operations (create, patch, delete) require TLS, loopback transport, or `X-Forwarded-Proto: https` from a configured trusted proxy. When disabled (default), any authenticated request is accepted regardless of transport. Enable this in deployments where the egress sidecar is directly reachable from untrusted networks without a TLS-terminating reverse proxy. |
| `OPENSANDBOX_EGRESS_CREDENTIAL_VAULT_TRUSTED_PROXY_CIDRS` | empty | Comma-separated IP addresses or CIDRs allowed to assert `X-Forwarded-Proto: https`. Forwarded transport headers from all other peers are ignored. Configure this when TLS terminates at a reverse proxy before the egress sidecar. |
| `OPENSANDBOX_EGRESS_CREDENTIAL_VAULT_REQUIRE_SCOPED_MATCH` | off | When enabled, every credential binding must explicitly provide non-empty `match.methods` and `match.paths`, and paths cannot contain the host-wide `/*` pattern. Vault create and patch requests that omit either field are rejected instead of receiving compatibility defaults. Enable this for control planes that translate higher-level API tool definitions into Credential Vault bindings. |


The scoped-match setting is a fail-closed integration guard. It does not infer methods or paths from another platform's API tool definition. The caller that creates the vault must still copy the intended methods and paths into each binding and verify the sanitized binding readback.


## SDK Quick Reference


All sandbox SDKs use the same wire contract. The main differences are naming and language style:


| SDK | Enable proxy on sandbox create | Vault entry point | Create / patch methods |
| --- | --- | --- | --- |
| Python | `credential_proxy=CredentialProxyConfig(enabled=True)` | `sandbox.credential_vault` | `create(...)`, `patch(...)` |
| Go | `CredentialProxy: &opensandbox.CredentialProxyConfig{Enabled: true}` | `sandbox.CredentialVault(ctx)` or sandbox helpers | `CreateCredentialVault(ctx, req)`, `PatchCredentialVault(ctx, req)` |
| JavaScript/TypeScript | `credentialProxy: { enabled: true }` | `sandbox.credentialVault` | `create(request)`, `patch(request)` |
| Kotlin/JVM | `.credentialProxyEnabled(true)` or `.credentialProxy { enabled(true) }` | `sandbox.credentialVault()` | `create(request)`, `patch(request)` |
| C#/.NET | `CredentialProxy = new CredentialProxyConfig { Enabled = true }` | `sandbox.CredentialVault` or sandbox helpers | `CreateCredentialVaultAsync(...)`, `PatchCredentialVaultAsync(...)` |


The vault APIs return sanitized metadata. Plaintext credential values are write-only and are not returned by `get`, `list`, or patch responses.


The same entry points and methods work for template-backed (fsb) sandboxes: the SDK routes the vault through the lifecycle server, which relays revisions to the egress-held vault. No sidecar endpoint is resolved for them, and the `credentialProxy` create-time flag is ignored on that profile (the vault is set after creation, through the API).


## Claude Code With Anthropic


This example installs Claude Code in the sandbox and calls the official Anthropic API endpoint. The real API key is read on the host and written to Credential Vault. The sandbox only sees a fake `ANTHROPIC_API_KEY`.


Before running the script:

bash

```
export ANTHROPIC_API_KEY="sk-ant-..."
# Optional: export ANTHROPIC_MODEL="<a Claude Code supported Anthropic model>"
```


Run:

python

```
import os
from datetime import timedelta

from opensandbox import SandboxSync
from opensandbox.models.sandboxes import (
    Credential,
    CredentialBinding,
    CredentialProxyConfig,
    NetworkPolicy,
    NetworkRule,
    SandboxImageSpec,
)


ANTHROPIC_HOST = "api.anthropic.com"
ANTHROPIC_BASE_URL = "https://api.anthropic.com"
REAL_API_KEY = os.environ["ANTHROPIC_API_KEY"]


sandbox_env = {
    "ANTHROPIC_BASE_URL": ANTHROPIC_BASE_URL,
    "ANTHROPIC_API_KEY": "fake-key-inside-sandbox",
}
if os.getenv("ANTHROPIC_MODEL"):
    sandbox_env["ANTHROPIC_MODEL"] = os.environ["ANTHROPIC_MODEL"]


sandbox = SandboxSync.create(
    image=SandboxImageSpec(
        os.getenv("SANDBOX_IMAGE", "opensandbox/code-interpreter:latest")
    ),
    timeout=timedelta(minutes=15),
    env=sandbox_env,
    network_policy=NetworkPolicy(
        defaultAction="deny",
        egress=[
            NetworkRule(action="allow", target=ANTHROPIC_HOST),
            NetworkRule(action="allow", target="registry.npmjs.org"),
        ],
    ),
    credential_proxy=CredentialProxyConfig(enabled=True),
)

try:
    sandbox.credential_vault.create(
        credentials=[
            Credential(
                name="anthropic-api-key",
                source={"value": REAL_API_KEY},
            )
        ],
        bindings=[
            CredentialBinding(
                name="anthropic-api",
                match={
                    "schemes": ["https"],
                    "hosts": [ANTHROPIC_HOST],
                    "methods": ["GET", "POST"],
                    "paths": ["/v1/*"],
                },
                auth={
                    "type": "apiKey",
                    "name": "x-api-key",
                    "credential": "anthropic-api-key",
                },
            )
        ],
    )

    sandbox.commands.run(
        "npm install -g @anthropic-ai/claude-code --no-audit --no-fund"
    )
    result = sandbox.commands.run("claude -p '1+1'")
    output = "".join(part.text for part in result.logs.stdout)
    print(output)
finally:
    sandbox.kill()
    sandbox.close()
```


The Claude Code process reads the fake key from `ANTHROPIC_API_KEY`, but the outbound HTTPS request to `api.anthropic.com/v1/*` receives the real `x-api-key` header from Credential Vault. If your environment uses a private npm mirror, replace `registry.npmjs.org` in the network policy and the `npm install` command with that mirror host.


## Git And Curl With Vault-Injected Credentials


Credential Vault can also protect credentials used by command-line tools such as `git` and `curl`. Keep the command free of real secrets and bind the request shape to the credential in Vault instead.


For a private Git repository, store a base64-encoded `username:token` value and bind it with `basic` auth:

python

```
Credential(name="git-basic", source={"value": "<base64(username:token)>"})

CredentialBinding(
    name="git-basic",
    match={
        "schemes": ["https"],
        "hosts": ["git.example.com"],
        "paths": ["/org/private-repo.git*"],
    },
    auth={"type": "basic", "credential": "git-basic"},
)
```


Then run the normal URL without embedding credentials:

bash

```
GIT_TERMINAL_PROMPT=0 git clone https://git.example.com/org/private-repo.git
```


For an API request that expects a token header, bind the path and method to an `apiKey` auth rule:

python

```
Credential(name="api-token", source={"value": "<token>"})

CredentialBinding(
    name="api-token",
    match={
        "schemes": ["https"],
        "hosts": ["api.example.com"],
        "methods": ["GET"],
        "paths": ["/v1/projects/123/variables"],
    },
    auth={"type": "apiKey", "name": "PRIVATE-TOKEN", "credential": "api-token"},
)
```


The sandbox command stays secret-free:

bash

```
curl -fsS https://api.example.com/v1/projects/123/variables
```


## Binding Guidance


- Use `defaultAction="deny"` and only allow the service hosts required by the tool. Default-allow policies are deprecated because they may allow credential destination bypass and will emit a security warning.
- Scope bindings by path whenever possible, for example `/v1/*`.
- Avoid overlapping bindings at the same precedence; ambiguous matches are rejected.
- Rejected requests (ambiguous paths, encoded separators crossing a binding boundary) return `403` when the request body is small and fully known. Requests with bodies above the mitmproxy streaming threshold (~1 MiB) or with unknown length (chunked) cannot be answered with a `403` while the body is being streamed, so the sidecar drops the connection instead — either way the request is never forwarded upstream.
- Do not put real secrets in sandbox `env`, command arguments, files, or metadata.
- Keep fake environment variables when a CLI refuses to start without a key; the vault-injected header is what authenticates the outbound request.


## Path Ambiguity Guard


The sidecar inspects the request path only for requests that would receive injected credentials. A request is rejected with `403` when its path contains dot-segments (`..`) or backslashes (`\`, `%5c`) at any percent-decoding depth, or when percent-decoding does not converge within the guard's iteration bound — these are traversal or path-confusion primitives that legitimate clients do not send.


Encoded slashes (`%2f`, including nested forms like `%252f`) are allowed when every decoding depth of the path matches the same credential binding. This keeps legitimate encoded wire formats working — npm scoped registry paths (`/@scope%2fname`) and artifact-store download URLs whose coordinates are double-encoded (for example `pkg%252F1.0`, as produced by some internal pypi proxies) — while a path whose decoding would cross a binding boundary is still rejected before any credential is injected. Requests outside every binding scope pass through untouched.


## Migrating From `ports`


The `match.ports` field is deprecated. Port is now derived from scheme (`https` →443, `http` →80). Only ports 80 and 443 are supported; non-standard values are rejected with a validation error.


If you have existing bindings that use `ports` to narrow scope, migrate them to the equivalent `schemes` restriction:


| Before | After |
| --- | --- |
| `schemes: ["http", "https"], ports: [443]` | `schemes: ["https"]` |
| `schemes: ["http", "https"], ports: [80]` | `schemes: ["http"]` |
| `schemes: ["https"], ports: [443]` | `schemes: ["https"]` (remove `ports`) |


## Experimental Live Credential-Bound Admission (OSEP-0023)


Experimental boundary


The live credential-bound loop is an internal sidecar experiment, not a supported deployment mode. It is documented here to bound what the current implementation actually does; the gate remains off by default and no public configuration surface is added.


When the experimental revision runtime is enabled, the sidecar installs an immutable decision snapshot into the mitmproxy child over a private authenticated IPC channel and admits traffic per connection and per request:


- **Dynamic decisions use the installed snapshot.** Unbound HTTPS passes through opaquely; bound hosts are decrypted only with a registry admission. Unknown identity denies. For a known identity, ECH, no-SNI and validated static TLS/443 bypass retain their early precedence, including during bootstrap. Other unknown, bootstrapping or mismatched state denies.
- **Static TLS/443 bypass is operator-owned.** Set `OPENSANDBOX_EGRESS_MITMPROXY_PASSTHROUGH_HOSTS` to a JSON array of exact FQDNs or leftmost `*.` selectors, for example `["status.example.com","*.logs.example.com"]`. A wildcard covers all proper subdomains, including multiple labels, but not its apex. Go normalizes IDNA, case, surrounding whitespace and one root dot, then freezes a sorted unique list. Unset and `[]` mean empty; explicit empty text is an error. JSON input and canonical output each have a 64 KiB limit; at most 256 input entries are allowed before deduplication. IPs, URLs, ports and regexes are rejected.
- **Migrate native bypass options before enabling live admission.** Both effective mitmproxy `ignore_hosts` and `allow_hosts` must remain empty. Static selectors run in the typed TLS hook at actual destination port 443, not in native regex options. HTTP/80 behavior and network policy are unchanged. Non-empty selectors cannot be combined with a chained upstream proxy. Explicit use of this variable outside live mode is rejected. Legacy regex behavior remains unchanged when the variable is unset. Existing `tcp_hosts` may still bypass HTTP credential handling; this change does not establish a general addon/options isolation boundary.
- **TLS overlap is rejected before publication.** Any semantic intersection between a static selector and an HTTPS/443 binding rejects the complete Vault or Policy candidate before IPC prepare, policy persistence or nft application. Methods and paths do not exempt an overlap. HTTP-only bindings remain eligible. The child independently rejects overlap before staging. The list cannot be changed by a Vault update and adds no snapshot fields; changing it requires replacing the sidecar process.
- **Sticky recovery, no same-sidecar restart.** Any terminal outcome with unknown external effects (a mutation whose remote result cannot be confirmed, a session cleanup failure, an unexpected child exit) latches a permanent recovery-required state: readiness drops, outstanding bootstrap tickets are invalidated, nft writes are quiesced, and quarantine is attempted. Packet isolation is established only when quarantine is confirmed. The same sidecar cannot bootstrap a fresh revision session afterwards; a whole-sidecar restart is not a verified safe recovery procedure.
- **Request admission and cutover.** A vault mutation is applied to the live receiver first and published publicly only after exact confirmation. A rendered snapshot exceeding the IPC size limit is rejected with HTTP 400 before transmission; the current vault and sidecar remain available. In-flight requests finish on their admitted revision; new requests on a connection whose host was removed are fenced immediately: HTTP/1 receives 403; valid HTTP/2 requests refused at `requestheaders` receive `REFUSED_STREAM` without reaching the origin. The retired transport is force-closed at the drain deadline. Deleting the vault affects new requests and new connections; a retired connection can never be revived by re-adding the host. Already-admitted requests may finish only inside the bounded drain window — deletion does not recall requests the remote origin already received or revoke credentials already delivered remotely.
- **Policy updates share the revision barrier.** Existing `POST`/`PUT`/`PATCH`/`DELETE /policy` operations and automatic `deny.always` / `allow.always` reloads validate the complete Policy/Vault pair. A policy that would deny any active binding is rejected before file, nft or receiver effects. A policy-only update preserves the public Vault revision, pinned credential bytes and bindings; it does not reread credential sources. Its commit order is optional user-policy file persistence, nft application, exact receiver confirmation, then Go proxy/base publication and API success. Reload skips user-policy persistence and publishes the accepted loader view only after receiver confirmation. Subsequent Vault writes and bootstraps use the committed internal Policy epoch rather than resetting it to zero.
- **Policy visibility and failure.** Disk, nft and receiver updates are not instantaneously atomic: new nft rules may affect traffic before receiver confirmation. A receiver failure after successful nft application requires sticky recovery, quarantine and exact-child cleanup, even if the receiver definitively rejected the candidate. Replaying old nft rules or restoring the file cannot prove that new connections or requests were undone. Unavailable or unconfirmed revision updates and recovery-blocked writes return a fixed, sanitized 503; the initial file/nft error may still be 500. Validation failures before effects do not themselves require recovery.
- **Policy no-ops and retries.** A DELETE with no matching target and an unchanged always-rule reload do not advance the internal Policy epoch, but cannot bypass recovery checks. Other committed writes, including equal content or a loader-detected rewrite, can advance the epoch and initiate another drain. No public epoch, Policy idempotency key or new SDK method is added. `GET /policy` reports the last Go-published user policy, not an in-progress transaction, always-rule overlay or packet-isolation status.
- **Drain accounting.** Retired transports carry a bounded retirement deadline (default 30 seconds, internal range 1–300). The drain sweep pages expired transports and closes them; a failed close is retried on the next sweep rather than extending the deadline. An HTTP 101 protocol upgrade (including WebSocket) retains its request admission until the connection disconnects, so credential rotation and policy-only changes also drain an upgraded transport even when its host remains bound. API success waits for publication and retirement-deadline registration, not for the 30-second window to elapse. Repeated updates never extend an older request's earliest deadline. A still-covered connection may admit new-revision requests, but closing it for an expired old request also interrupts those newer requests. A still-covered idle connection with no old request is not retired solely because the Policy epoch changes. Sweep scheduling and failed-close retries can delay actual closure; this is not a deadline for opaque or direct-IP connections outside the registry. HTTP/2 normal retirement delays the single `NO_ERROR` GOAWAY with its frozen admitted-stream upper bound until old streams and their downstream/upstream output obligations are terminal. Deadline expiry is abnormal closure, not graceful completion.
- **ECH is opaque pass-through.** A ClientHello carrying the `encrypted_client_hello` extension (0xfe0d), including GREASE forms, is forwarded untouched as an opaque tunnel without decryption; uninspectable ClientHello data denies. The implementation does not decrypt the inner ClientHello and does not guarantee that an ECH-enabled origin handshake succeeds.
- **HTTP/1 authority gate.** On a decrypted HTTP/1 connection every request must carry exactly one syntactically strict `Host` header equal to the intercepted SNI and the admission binding (port omitted or 443). A conflicting absolute-form target, a CONNECT authority-form inside the stream and missing/duplicate/malformed Host values are rejected before any credential can be injected.
- **HTTP/2 authority gate.** The fixed-version direct/lazy adapter validates original HTTPS pseudo-headers, authority, actual port 443 and SNI association before credential injection; invalid or missing identity fails closed.
- **`ssl_insecure` is refused in live mode.** The launcher and the addon reject an insecure-upstream configuration when the live admission bundle is active; the legacy installation-only receiver keeps its existing behavior.
- **Scope.** This mode is scoped to the internal sidecar profile: Docker DNS + nft enforcement, exact-host HTTPS on port 443, HTTP/1.1 origin-form or matching absolute-form requests, and inline credentials injected as headers. Experimental HTTP/2 admission and bounded drain wiring additionally cover only the fixed-dependency direct/lazy path; configured chained upstream proxies remain rejected for this live HTTP/2 path. Long-held responses can still cause Go retries to time out; full client migration and Linux acceptance remain follow-up work. See the [HTTP/2 integration boundary](https://open-sandbox.ai/architecture/network/osep-0023-h2-integration). The fast-sandbox profile and recovery across a complete sidecar replacement remain out of scope. Dynamic DNS learning and Kubernetes deployments are not covered by this experiment's evidence. Policy participation is part of this implementation; its acceptance evidence is recorded separately from the earlier live-Vault checks below.


The task-level acceptance record for this experiment lives in [Live Vault Acceptance](https://open-sandbox.ai/guides/live-vault-acceptance).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/credential-vault.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/api`

# OpenSandbox API Specifications


This section contains the OpenAPI specification documents for the OpenSandbox project, defining the complete API interfaces and data models. Use the server base URLs defined in each spec (for example, `http://localhost:8080/v1` for the lifecycle API, `http://localhost:44772` for execd, and `http://localhost:18080` for egress) when constructing requests.


## Specification Files


Implementing an alternative backend or integrating a workload's own API? Read [Implementation compatibility](https://open-sandbox.ai/api/implementation-compatibility) for the boundary between these contracts, the reference daemons, and current SDK expectations.


### 1. sandbox-lifecycle.yml


[OpenAPI source](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/sandbox-lifecycle.yml)
## Specification Files ​
*Main Endpoints (base path /v1):*

*Optional Sandbox.allocation response field:*

*Isolated Execution (base path /v1/isolated):*

## Technical Features ​




**Sandbox Lifecycle Management API**


Defines the complete lifecycle interfaces for creating, managing, and destroying sandbox environments from container images or snapshots.


**Core Features:**


- **Sandbox Management**: Create, list, query, and delete sandbox instances with metadata filters and pagination
- **State Control**: Pause and resume sandbox execution
- **Lifecycle States**: Supports transitions across Pending -> Running -> Pausing -> Paused -> Stopping -> Terminated, and error handling with `Failed`
- **Resource & Runtime Configuration**: Specify resource limits and optional Kubernetes `resourceRequests`, image startup `entrypoint`, `platform`, lifecycle hooks, optional `secureAccess`, volumes, environment variables, and opaque `extensions`
- **Image Support**: Create sandboxes from public or private registries, including registry auth
- **Timeout Management**: Optional `timeout` on creation (omit or set to `null` to disable automatic expiration) with explicit renewal via API
- **Endpoint Access**: Retrieve public access endpoints for services running inside sandboxes, including required headers when secured access is enabled; endpoint lookups report the sandbox origin via the `OPEN-SANDBOX-ORIGIN` response header (`template` for fsb golden-image sandboxes)
- **Template Management**: Create, list, inspect, and delete fsb golden-image templates; template builds are asynchronous (poll until `Succeeded`)
- **Snapshot Management**: Create snapshots from sandboxes, list snapshots with source/name filters, and delete snapshots


**Main Endpoints (base path `/v1`):**


- `POST /sandboxes` - Create a sandbox from an image, snapshot, or template with timeout and resource limits
- `GET /sandboxes` - List sandboxes with state/metadata filters and pagination
- `GET /sandboxes/{sandboxId}` - Get full sandbox details (including startup source and entrypoint)
- `DELETE /sandboxes/{sandboxId}` - Delete a sandbox
- `POST /sandboxes/{sandboxId}/snapshots` - Create a snapshot from a sandbox
- `GET /snapshots` - List snapshots with optional source sandbox, exact name, and state filtering plus pagination
- `GET /snapshots/{snapshotId}` - Get snapshot state and metadata
- `DELETE /snapshots/{snapshotId}` - Delete a snapshot
- `POST /sandboxes/{sandboxId}/pause` - Pause a sandbox (asynchronous); returns `409 Conflict` if it is already paused
- `POST /sandboxes/{sandboxId}/resume` - Resume a paused sandbox
- `POST /sandboxes/{sandboxId}/renew-expiration` - Set the absolute sandbox expiration time
- `PATCH /sandboxes/{sandboxId}/metadata` - Patch sandbox metadata (JSON Merge Patch, RFC 7396)
- `GET /sandboxes/{sandboxId}/endpoints/{port}` - Get an access endpoint and required headers; supports `use_server_proxy` and signed-endpoint `expires` parameters
- `GET/PUT/PATCH/DELETE /sandboxes/{sandboxId}/networkpolicy` - Inspect and manage the sandbox egress network policy (Fsb persists intent on the Sandbox CR; other backends proxy the sandbox-side egress service)
- `POST/GET/PATCH/DELETE /sandboxes/{sandboxId}/credential-vault` (+ sanitized `credentials` / `bindings` reads) - Manage the sandbox Credential Vault (fsb relays to the egress-held vault over FastPath; other backends proxy the sandbox-side egress service; values are write-only and never returned)
- `POST /templates` - Create a fsb template (asynchronous golden-image build)
- `GET /templates` - List templates with metadata filters and pagination
- `GET /templates/{templateId}` - Get template status and artifact references
- `DELETE /templates/{templateId}` - Delete a template


**Expiration updates:** `renew-expiration` sets `expiresAt` to the supplied future timestamp, which may be earlier than, equal to, or later than the current expiration. The configured `server.max_sandbox_timeout_seconds` applies only to `timeout` on creation; it does not cap expiration updates. See [Sandbox expiration](https://open-sandbox.ai/getting-started/configuration#sandbox-expiration).


**Optional `Sandbox.allocation` response field:**


- Returned only when the runtime confirms the sandbox's current concrete Pool allocation.
- Omitted for unconfirmed allocations, non-Pool sandboxes, and allocations being released.
- This field is not a request echo, allocation history, or readiness signal, and does not expose Pod names or other Kubernetes-internal fields.


**Authentication:**


- HTTP Header: `OPEN-SANDBOX-API-KEY: your-api-key`
- Environment Variable: `OPEN_SANDBOX_API_KEY` (for SDK clients)


### 2. diagnostic-api.yml


[OpenAPI source](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/diagnostic-api.yml)


**Sandbox Diagnostics API**


Defines structured routing context and best-effort troubleshooting descriptors for sandbox diagnostic logs and events. Context identifies the runtime backend and its diagnostic identifiers. Log and event descriptors either embed plain-text content inline or return a download URL. This spec does not define a structured audit or observability model.


**Main Endpoints (base path `/v1`):**


- `GET /sandboxes/{sandboxId}/diagnostics/context` - Retrieve the runtime backend and backend-defined diagnostic identifiers
- `GET /sandboxes/{sandboxId}/diagnostics/logs` - Retrieve a diagnostic log content descriptor; `scope` is required
- `GET /sandboxes/{sandboxId}/diagnostics/events` - Retrieve a diagnostic event content descriptor; `scope` is required


**Authentication:**


- HTTP Header: `OPEN-SANDBOX-API-KEY: your-api-key`
- Environment Variable: `OPEN_SANDBOX_API_KEY` (for SDK clients)


`scope` is required. Docker and Kubernetes support `container` / `all` for logs and `runtime` / `all` for events. Fast Sandbox supports `runtime` / `all` events; log collection is not implemented there. Unsupported scopes return `DIAGNOSTICS_SCOPE_UNSUPPORTED`.


Responses use `delivery: inline` with `content`, or `delivery: url` with `contentUrl` and an optional expiry. The SDK does not download URL content; inspect `truncated` and `warnings` before treating results as complete. Python models and CLI JSON/YAML use snake_case fields such as `content_url`. CLI raw output prints the content or URL without following it.


See [SDK diagnostics](https://open-sandbox.ai/sdks/#diagnostics) for language support and [CLI diagnostics](https://open-sandbox.ai/cli/#collect-diagnostics) for command examples.


### 3. execd-api.yaml


[OpenAPI source](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/execd-api.yaml)


**Code Execution API Inside Sandbox**


Defines interfaces for executing code, commands, and file operations within sandbox environments, providing complete code interpreter and filesystem management capabilities. Forward the headers returned by lifecycle endpoint resolution, including `X-EXECD-ACCESS-TOKEN` when required. Do not hard-code an execd address or assume the lifecycle API key alone authorizes direct sandbox access.


**Core Features:**


- **Code Execution**: Stateful code execution supporting Python, JavaScript, and other languages with context lifecycle management
- **Command Execution**: Shell command execution with foreground/background modes and polling endpoints for status/output
- **File Operations**: Complete CRUD operations for files and directories
- **Real-time Streaming**: Real-time output streaming via SSE (Server-Sent Events)
- **System Monitoring**: Real-time monitoring of CPU and memory metrics
- **Access Control**: Token-based API authentication via `X-EXECD-ACCESS-TOKEN`


**Main Endpoint Categories:**


**Health Check:**


- `GET /ping` - Service health check


**Code Interpreter:**


- `GET /code/contexts` - List active code execution contexts (filterable by language)
- `DELETE /code/contexts` - Delete all contexts for a language
- `DELETE /code/contexts/{context_id}` - Delete a specific context
- `POST /code/context` - Create a code execution context
- `POST /code` - Execute code in a context (streaming output)
- `DELETE /code` - Interrupt code execution


**Command Execution:**


- `POST /command` - Execute shell command (streaming output)
- `DELETE /command` - Interrupt command execution
- `GET /command/status/{id}` - Get foreground/background command status
- `GET /command/{id}/logs` - Fetch accumulated stdout/stderr for a background command


**Bash Session:**


- `POST /session` - Create a bash session
- `POST /session/{sessionId}/run` - Run command in a bash session (streaming output)
- `DELETE /session/{sessionId}` - Delete a bash session


**Filesystem:**


- `GET /files/info` - Get metadata for files
- `DELETE /files` - Delete files (not directories)
- `POST /files/permissions` - Change file permissions
- `POST /files/mv` - Move/rename files
- `GET /files/search` - Search files (supports glob patterns)
- `POST /files/replace` - Batch replace file content
- `POST /files/upload` - Upload files (multipart)
- `GET /files/download` - Download files (supports range requests)


**Directory Operations:**


- `GET /directories/list` - List directory contents with optional depth control
- `POST /directories` - Create directories with permissions (mkdir -p semantics)
- `DELETE /directories` - Recursively delete directories


**System Metrics:**


- `GET /metrics` - Get system resource metrics
- `GET /metrics/watch` - Watch system metrics in real-time (SSE stream)


**Isolated Execution (base path `/v1/isolated`):**


- `POST /session` - Create an isolated bash session
- `GET /sessions` - List isolated sessions
- `GET /capabilities` - Get isolator capabilities
- `GET /session/{sessionId}` - Get isolated session state
- `DELETE /session/{sessionId}` - Delete an isolated session
- `POST /session/{sessionId}/run` - Run a command in an isolated session (foreground SSE or background execution)
- `GET/DELETE /session/{sessionId}/runs/{runId}` - Get status or interrupt an isolated run
- `GET /session/{sessionId}/runs/{runId}/logs` - Retrieve isolated run logs
- `GET /session/{sessionId}/files/info` - Get file information
- `GET /session/{sessionId}/files/download` - Download a file
- `POST /session/{sessionId}/files/upload` - Upload a file
- `DELETE /session/{sessionId}/files` - Remove files
- `POST /session/{sessionId}/files/mv` - Rename or move files
- `POST /session/{sessionId}/files/permissions` - Change file permissions
- `POST /session/{sessionId}/files/replace` - Replace file content
- `GET /session/{sessionId}/files/search` - Search files
- `GET /session/{sessionId}/directories/list` - List directory contents
- `POST /session/{sessionId}/directories` - Create directories
- `DELETE /session/{sessionId}/directories` - Delete directories


`GET /session/{sessionId}/diff` and `POST /session/{sessionId}/commit` appear in the contract but are not implemented in the current execd: both return `503` with a not-supported error, and capabilities report `diff_supported: false` and `commit_supported: false`. Check `/v1/isolated/capabilities` before using runtime-dependent isolation features.


### 4. egress-api.yaml


[OpenAPI source](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/egress-api.yaml)


**Sandbox Egress Runtime API**


Defines the runtime egress policy interface exposed directly by the [egress sidecar](https://open-sandbox.ai/architecture/network/egress) inside a sandbox. Unlike lifecycle operations, this API is reached by first resolving the sandbox endpoint for the egress port and then calling the sidecar endpoint directly.


**Core Features:**


- **Policy Inspection**: Retrieve the currently enforced egress policy and derived runtime mode
- **Policy Mutation**: Patch egress rules at runtime using sidecar merge semantics
- **Direct Sidecar Access**: Access via sandbox endpoint resolution instead of server-side lifecycle forwarding
- **Optional Sidecar Auth**: Supports endpoint-specific headers when the egress sidecar requires auth


**Main Endpoints:**


- `GET /policy` - Get the current egress policy
- `PATCH /policy` - Merge new egress rules into the current policy
- `DELETE /policy` - Remove specific egress rules from the current policy by target
- `POST/GET/PATCH/DELETE /credential-vault` - Create, inspect, mutate, or delete vault state
- `GET /credential-vault/credentials` and `GET /credential-vault/credentials/{credential_name}` - Read sanitized credential metadata
- `GET /credential-vault/bindings` and `GET /credential-vault/bindings/{binding_name}` - Read binding metadata


Credential values are write-only. Enable Credential Proxy and an egress policy before creating a vault. Template-backed (fsb) sandboxes use the server-routed `/sandboxes/{sandboxId}/credential-vault` endpoints above: the server relays revisions to the egress-held vault over the FastPath handler relay, the ack is synchronous, and values never appear on any read (see [Credential Vault](https://open-sandbox.ai/guides/credential-vault)).


## Technical Features


### Streaming Output (Server-Sent Events)


Code execution and command execution interfaces use SSE for real-time streaming output, supporting the following event types:


- `init` - Initialization event
- `status` - Status update
- `stdout` / `stderr` - Standard output/error streams
- `result` - Execution result
- `execution_complete` - Execution completed
- `execution_count` - Execution count
- `error` - Error information


### Resource Limits


Supports flexible resource configuration (similar to Kubernetes):

json

```
{
  "cpu": "500m",
  "memory": "512Mi",
  "gpu": "1"
}
```


### File Permissions


Supports Unix-style file permission management:


- Owner
- Group
- Permission mode values such as 644 or 755[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/api/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/`

# OpenSandboxUniversal Sandbox Infrastructure for AI Applications

OpenSandbox is listed in the CNCF Landscape.

# OpenSandbox Universal Sandbox Infrastructure for AI Applications
## Typical Scenarios ​
*Explore all examples in Examples.*

## Quick Install ​




Securely run commands, code interpreters, browsers, and developer tools in isolated environments with multi-language SDKs.

[Quick Start](https://open-sandbox.ai/getting-started/) [Architecture](https://open-sandbox.ai/architecture/) [SDKs](https://open-sandbox.ai/sdks/)

## Sandbox Lifecycle Management


Provision, monitor, renew, pause/resume, and terminate sandbox instances with Docker and Kubernetes runtimes.


## Multi-Language SDKs


Build with Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, and Go SDKs on top of standardized lifecycle and execution protocols.


## In-Sandbox Execution


Execute shell commands, manage files, run multi-language code interpreters, expose ports, and stream logs and metrics.


## Built for AI Workloads


Supports coding agents, browser automation, remote development, code execution, and reinforcement learning scenarios.


## Typical Scenarios


OpenSandbox is listed in the [CNCF Landscape](https://landscape.cncf.io/?item=orchestration-management--scheduling-orchestration--opensandbox).

[### Coding Agents Run Claude Code, Gemini CLI, Codex, and other coding agents in isolated sandboxes.](https://open-sandbox.ai/examples/claude-code) [### Browser Automation Execute Chrome and Playwright workloads with controlled runtime, filesystem, and networking.](https://open-sandbox.ai/examples/playwright) [### Remote Development Host VS Code Web and desktop-like environments for secure cloud development workflows.](https://open-sandbox.ai/examples/vscode) [### AI Code Execution Run model-generated code safely, stream outputs, and iterate quickly with reproducible environments.](https://open-sandbox.ai/examples/code-interpreter)

Explore all examples in [Examples](https://open-sandbox.ai/examples/).


## Quick Install

Python SDK JavaScript SDK Kotlin (Gradle) Go SDK C# SDK bash

```
pip install opensandbox
```

bash

```
npm install @alibaba-group/opensandbox
```

kotlin

```
dependencies {
    implementation("com.alibaba.opensandbox:sandbox:{latest_version}")
}
```

bash

```
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```

bash

```
dotnet add package Alibaba.OpenSandbox
```


See [Getting Started](https://open-sandbox.ai/getting-started/) for the full setup guide.

## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides`

# Feature Guides


Use these guides to add capabilities to a working [sandbox application](https://open-sandbox.ai/getting-started/). Check the [SDK capability matrix](https://open-sandbox.ai/sdks/#capability-coverage) for language support.


## Lifecycle and security


- [Pause and resume](https://open-sandbox.ai/guides/pause-resume)
- [Lifecycle hooks](https://open-sandbox.ai/guides/lifecycle-hooks)
- [Isolation sessions](https://open-sandbox.ai/guides/isolation-sessions)
- [Credential Vault](https://open-sandbox.ai/guides/credential-vault)
- [Chained upstream proxy](https://open-sandbox.ai/guides/egress-upstream-proxy)
- [Secure access](https://open-sandbox.ai/guides/secure-access)
- [Secure container runtimes](https://open-sandbox.ai/guides/secure-container)
- [Network isolation on Kubernetes](https://open-sandbox.ai/guides/network-isolation)
- [Multi-tenancy](https://open-sandbox.ai/guides/multi-tenancy)
- [Windows sandboxes](https://open-sandbox.ai/guides/windows-sandbox)


## Operations


- [Telemetry](https://open-sandbox.ai/guides/telemetry)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/getting-started`

# Quick Start
## Prerequisites ​
## 1. Start the Server ​
## 2. Install an SDK ​
*For Kotlin/Java, see Installation.*

## 3. Create and Use a Sandbox ​
## 4. Try the CLI ​
## Next Steps ​








OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes.


## Prerequisites


- **Docker** Engine 20.10+ (for local execution)
- **Python** 3.10+ (for the server and Python SDK)
- **uv** (recommended) or pip


## 1. Start the Server

bash

```
# Generate a starter config
uvx opensandbox-server init-config ~/.sandbox.toml --example docker

# Start the server
uvx opensandbox-server
```


Verify the server is running:

bash

```
curl http://127.0.0.1:8080/health
# → {"status": "healthy"}
```


## 2. Install an SDK

Python JavaScript Go C# bash

```
pip install opensandbox
```

bash

```
npm install @alibaba-group/opensandbox
```

bash

```
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```

bash

```
dotnet add package Alibaba.OpenSandbox
```


For Kotlin/Java, see [Installation](https://open-sandbox.ai/getting-started/installation).


## 3. Create and Use a Sandbox


This example uses the sandbox SDK and a standard Python image. If the server has an API key configured, set `OPEN_SANDBOX_API_KEY` in your client environment.

python

```
import asyncio
from datetime import timedelta

from opensandbox import Sandbox
from opensandbox.config import ConnectionConfig
from opensandbox.models import WriteEntry


async def main() -> None:
    sandbox = await Sandbox.create(
        "python:3.12",
        timeout=timedelta(minutes=10),
        connection_config=ConnectionConfig(
            domain="localhost:8080",
            use_server_proxy=True,
        ),
    )
    try:
        execution = await sandbox.commands.run("python -c 'print(1 + 1)'")
        for output in execution.logs.stdout:
            print(output.text)

        await sandbox.files.write_files([
            WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        ])
        print(await sandbox.files.read_file("/tmp/hello.txt"))
    finally:
        await sandbox.destroy()


if __name__ == "__main__":
    asyncio.run(main())
```


`use_server_proxy=True` routes sandbox traffic through the lifecycle server, which is useful when the client cannot reach container addresses directly. `destroy()` terminates the remote sandbox and closes local SDK resources. Closing the client alone does not terminate the remote sandbox.


## 4. Try the CLI

bash

```
pip install opensandbox-cli

osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set connection.use_server_proxy true
osb sandbox create --image python:3.12 --timeout 30m -o json
osb command run <sandbox-id> -o raw --argv -- python -c "print(1 + 1)"
osb sandbox kill <sandbox-id> -o json
```


## Next Steps


- [Installation](https://open-sandbox.ai/getting-started/installation) — Detailed installation for all SDKs and runtimes
- [Configuration](https://open-sandbox.ai/getting-started/configuration) — Server configuration reference
- [Architecture](https://open-sandbox.ai/architecture/) — How OpenSandbox works under the hood
- [Guides](https://open-sandbox.ai/guides/) — Client Pool, tracing, diagnostics, and security features
- [SDK capability matrix](https://open-sandbox.ai/sdks/#capability-coverage) — Check support before choosing a language
- [Examples](https://open-sandbox.ai/examples/) — Real-world usage examples[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/getting-started/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks`

# SDKs


OpenSandbox provides five sandbox SDKs for lifecycle management, command execution, file operations, and resource metrics. This site follows the repository's default branch; a feature merged here may require a newer package than the one you have installed. Check the [release index](https://github.com/opensandbox-group/OpenSandbox/releases) when upgrading.


## Installation


| Language | Package | Install |
| --- | --- | --- |
| [Python](https://open-sandbox.ai/sdks/python) | `opensandbox` | `pip install opensandbox` |
| [JavaScript/TypeScript](https://open-sandbox.ai/sdks/javascript) | `@alibaba-group/opensandbox` | `npm install @alibaba-group/opensandbox` |
| [Kotlin/Java](https://open-sandbox.ai/sdks/kotlin) | `com.alibaba.opensandbox:sandbox` | Gradle/Maven |
| [Go](https://open-sandbox.ai/sdks/go) | `github.com/alibaba/OpenSandbox/sdks/sandbox/go` | `go get github.com/alibaba/OpenSandbox/sdks/sandbox/go` |
| [C#/.NET](https://open-sandbox.ai/sdks/csharp) | `Alibaba.OpenSandbox` | `dotnet add package Alibaba.OpenSandbox` |


## Capability coverage
## Installation ​
## Capability coverage ​
## Feature guides ​
## Diagnostics ​
## Lifecycle and cleanup ​
## CLI ​
## MCP server ​









“Yes” means a public SDK entry point exists. Availability also depends on the server runtime and the execd version installed in the sandbox.


| Capability | Python async/sync | JavaScript/TypeScript | Kotlin/Java | Go | C#/.NET |
| --- | --- | --- | --- | --- | --- |
| Create, connect, renew, pause/resume, kill | Yes | Yes | Yes | Yes | Yes |
| Snapshots and template management | Yes | Yes | Yes | Yes | Yes |
| Resource requests, volumes, lifecycle hooks | Yes | Yes | Yes | Yes | Yes |
| Commands, files, resource metrics | Yes | Yes | Yes | Yes | Yes |
| Egress policy and Credential Vault | Yes | Yes | Yes | Yes | Yes |
| Isolated sessions | Yes | Yes | Yes | Yes | Yes |
| [Client Pool](https://open-sandbox.ai/guides/client-pool), including Redis | Yes | Yes | Yes | Yes | No |
| [Pool warmup tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing) | Yes | Yes, fewer attributes | Yes | No | No |
| [Remote diagnostic logs/events](https://open-sandbox.ai/api/#diagnostics) | Yes | No | Yes | No | No |
| [Create-latency telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics) | Yes | Yes | Yes | Yes | Yes |


### Differences that affect application code


- **Pools:** Go exposes different warmup controls; the fields accepted by the default pool creator also differ across languages. See the [pool configuration matrix](https://open-sandbox.ai/guides/client-pool#configuration).
- **Go command control:** interrupt, command status, and accumulated command logs are exposed by `ExecdClient`, rather than the high-level `Sandbox` wrapper. Neither `Sandbox.CreateSession` nor `ExecdClient.CreateSession` accepts an initial working directory. Set `Cwd` when running a command in the session instead.
- **Go connect/resume readiness:** pass `ReadyOptions` to request readiness checks. Without it, connecting resolves the endpoint without checking sandbox health.
- **Metrics streaming:** Go exposes `ExecdClient.WatchMetrics`; the other SDKs' stable metrics services provide point-in-time reads. The [CLI](https://open-sandbox.ai/cli/) also has a metrics stream via `osb sandbox metrics --watch`.
- **Timeout units:** use Python `timedelta` and JVM `Duration`; JavaScript and C# command timeouts use seconds. Go `RunCommandRequest.Timeout` uses **milliseconds**.


Template-backed sandboxes require an explicit TTL and inherit their workload configuration from the published template. Their egress policy is managed through the lifecycle API; they do not have a sandbox-side Credential Vault.


## Feature guides


- [Client Pool](https://open-sandbox.ai/guides/client-pool): keep a ready buffer, select an acquire policy, share state through Redis, and retire a pool namespace.
- [Observability](https://open-sandbox.ai/sdks/observability): configure pool warmup traces and creation metrics, understand the default settings, and locate slow startup phases.


## Diagnostics


Python and Kotlin/Java expose remote logs/events on both `Sandbox` and `SandboxManager`. Use a manager when execd is not ready. Python methods are `get_diagnostic_logs` / `get_diagnostic_events`; JVM methods are `getDiagnosticLogs` / `getDiagnosticEvents`. Pass a sandbox ID to manager methods and an explicit scope such as `container` for logs or `runtime` for events.


JavaScript, Go, and C# can use the [CLI](https://open-sandbox.ai/cli/#collect-diagnostics) or [HTTP API](https://open-sandbox.ai/api/#diagnostics). C# `SdkDiagnosticsOptions` controls local SDK logging. See the API reference for supported scopes and inline/URL delivery.


## Lifecycle and cleanup


High-level image/snapshot creation defaults to a 10-minute TTL. Configure the TTL explicitly for your workload. To disable expiration, use Python `timeout=None`, JavaScript `timeoutSeconds: null`, Kotlin `timeout(null)`, or the Go/C# `ManualCleanup` option. Template creation requires a TTL.


`close()`, `DisposeAsync()`, and context-manager exit release local client resources; they do not kill the remote sandbox. Kill it in a `finally` / `defer` block, or use Python's `destroy()` helper. Pool acquisitions are consumed once and are not returned to the idle buffer.


## CLI


Use the [CLI](https://open-sandbox.ai/cli/) to manage sandboxes, run commands, and work with files from a terminal.

bash

```
uv tool install opensandbox-cli
```


## MCP server


The [MCP server](https://open-sandbox.ai/sdks/mcp) exposes sandbox operations to MCP-capable clients:

bash

```
pip install opensandbox-mcp
```[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture`

Return to top

# OpenSandbox Architecture
## Architecture Overview ​
*The implementation is documented by architectural layer under architecture/:*

## 1. Client Surface ​
## 2. Protocol Surface ​
*OpenSandbox treats specs/ as the public contract source of truth.*

## 3. Lifecycle Control Plane ​
*The server selects its lifecycle implementation based on [runtime].type:*

## 4. Runtime Backends ​
## 5. Sandbox Data Plane ​
## 6. Networking and Access ​
## 7. Core Flows ​
## 8. Design Principles ​
## 9. Common Use Cases ​












OpenSandbox is a general-purpose sandbox platform for AI applications. It provides client SDKs and tools, protocol definitions, a lifecycle control plane, Docker and Kubernetes runtime backends (supporting both container workloads and template-backed microVMs), and in-sandbox execution components for commands, files, code interpreters, browser automation, desktop environments, and training workloads.


This document describes the current repository architecture and the main boundaries between public contracts, server implementation, runtime providers, and sandbox data-plane components.


## Architecture Overview


![OpenSandbox Architecture](https://open-sandbox.ai/assets/architecture-overview.BtL716wh.svg)


The architecture distinguishes three primary interaction paths:


- **Lifecycle management** (orange arrows): Applications, agents, and operators send lifecycle requests (creating, listing, renewing, pausing, resuming, or deleting sandboxes, as well as managing snapshots and templates) to the FastAPI lifecycle server. The server persists metadata and delegates provisioning and orchestration to the configured runtime backend.
- **Execution and service access** (blue arrows): For command, file, PTY, and Jupyter code execution, or reaching user workload services, clients bypass lifecycle orchestration and connect directly to resolved endpoints—via direct host/pod addresses, the lifecycle server proxy, or an optional Kubernetes ingress gateway.
- **Outbound controls** (green arrows): Outbound requests from the sandbox to external APIs, model providers, or web services can be filtered and secured through egress controls (a per-sandbox sidecar for container workloads or a shared egress process per Fastlet pod for FastSandbox), with support for DNS/nftables policies and optional Credential Vault secret injection.


Runtime and networking capabilities depend on the selected backend; the diagram shows the shared architecture, not a requirement to deploy every component.


OpenSandbox is organized around six practical surfaces:


1. **Client surface** - SDKs, the `osb` CLI, and the MCP server used by applications, agents, and operators.
2. **Protocol surface** - OpenAPI contracts under `specs/` for lifecycle, diagnostics, in-sandbox execution, and egress policy.
3. **Lifecycle control plane** - the FastAPI server under `server/` that authenticates requests, validates config, persists server-managed records, and delegates lifecycle work to a configured runtime service.
4. **Runtime backends** - Docker for local and single-host deployments, and Kubernetes with container workload providers (BatchSandbox or `kubernetes-sigs/agent-sandbox`) alongside an optional FastSandbox integration for template-backed microVMs.
5. **Sandbox data plane** - the user workload and `execd` daemon inside a container or microVM, with optional Jupyter/code-interpreter support. Volume and egress integration depend on the runtime.
6. **Network and security plane** - endpoint resolution, server proxying, Kubernetes ingress gateway routing, secure endpoint access, egress policy enforcement, credential vault, resource limits, and secure container runtimes.


The split is intentional: SDKs and tools should depend on the public contracts, the server should own lifecycle orchestration, runtime providers should own platform-specific resource creation, and `execd` /egress should own operations that happen from inside the sandbox network and filesystem namespace.


The implementation is documented by architectural layer under `architecture/`:


| Layer | Responsibility | Documentation |
| --- | --- | --- |
| Control plane | Lifecycle orchestration, workload orchestration, snapshots | [Server](https://open-sandbox.ai/architecture/control-plane/server), [Kubernetes Controller](https://open-sandbox.ai/architecture/control-plane/operator) |
| Data plane | In-sandbox execution, node-side collection | [Execd](https://open-sandbox.ai/architecture/data-plane/execd), [Node Agent](https://open-sandbox.ai/architecture/data-plane/node-agent) |
| Network | Inbound access, outbound policy | [Ingress](https://open-sandbox.ai/architecture/network/ingress), [Egress](https://open-sandbox.ai/architecture/network/egress), [Single-Host Network](https://open-sandbox.ai/architecture/network/single-host-network) |
| Backend integration | Template-backed sandboxes on the fast-sandbox platform | [Fast Sandbox](https://open-sandbox.ai/architecture/fast-sandbox/) |


## 1. Client Surface


The client surface is the developer-facing entry point for OpenSandbox.


### 1.1 Sandbox SDKs


The sandbox SDKs wrap lifecycle operations and in-sandbox operations behind language-native APIs:


- Python: `sdks/sandbox/python`
- JavaScript/TypeScript: `sdks/sandbox/javascript`
- Java/Kotlin: `sdks/sandbox/kotlin`
- C#/.NET: `sdks/sandbox/csharp`
- Go: `sdks/sandbox/go`


Common capabilities include:


- Create, list, inspect, pause, resume, renew, and delete sandboxes.
- Resolve service endpoints for sandbox ports.
- Execute commands with streamed output and background status/log polling.
- Manage files and directories.
- Read resource metrics from `execd`.
- Inspect or patch runtime egress policy when an egress sidecar is attached.


Generated OpenAPI clients live beside handwritten adapters. Generated code handles ordinary request/response APIs; handwritten layers cover SDK ergonomics, streaming, transport lifecycle, error mapping, and high-level models.


### 1.2 Code Interpreter SDKs


The code-interpreter SDKs build on the sandbox SDKs and `execd` code execution APIs. They manage code execution contexts and expose language-oriented code execution helpers.


The official code-interpreter image is maintained in [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images) (previously located under `sandboxes/code-interpreter/`; see [Migration Reference](https://open-sandbox.ai/reference/code-interpreter-image-migration)). It provides Python, Java, Node.js, and Go runtimes, and Jupyter kernels for Python, Java, TypeScript/JavaScript, Go, and Bash. Exact language versions are image-controlled and selected through environment variables such as `PYTHON_VERSION`, `JAVA_VERSION`, `NODE_VERSION`, and `GO_VERSION`.


### 1.3 CLI and MCP


The `osb` CLI under `cli/` is a terminal interface for day-to-day sandbox operations:


- `osb sandbox`: lifecycle and endpoint management
- `osb command`: command execution, background logs, and shell sessions
- `osb file`: file and directory operations
- `osb egress`: runtime egress policy inspection and mutation
- `osb devops`: low-level diagnostics
- `osb skills`: OpenSandbox-specific agent skill installation


The MCP server under `sdks/mcp/sandbox/python` exposes focused sandbox lifecycle, command, and text-file tools to MCP-capable clients such as Claude Code and Cursor.


## 2. Protocol Surface


OpenSandbox treats `specs/` as the public contract source of truth.


### 2.1 Lifecycle API


`specs/sandbox-lifecycle.yml` defines the lifecycle API, served by the server with the base path `/v1`.


Main resource groups:


- **Sandboxes**: create from an image, snapshot, or template; list, get, delete, pause, resume, renew expiration, and resolve port endpoints. FastSandbox also supports inspecting and managing runtime network policy through `GET/PUT/PATCH/DELETE /sandboxes/{sandboxId}/networkpolicy`, and reports the sandbox origin to clients via the `OPEN-SANDBOX-ORIGIN` response header on endpoint lookups.
- **Snapshots**: create a persistent snapshot from a sandbox, list snapshots, get snapshot state, and delete snapshots.
- **Templates**: create, list, inspect, and delete template definitions in the catalog used by FastSandbox (`/templates`).


Important request features:


- `image` or `snapshotId` for container startup, or `templateId` for the FastSandbox path in Kubernetes mode.
- `entrypoint`, environment variables, metadata, and opaque `extensions`.
- `resourceLimits` for CPU, memory, GPU, and future resource keys.
- `platform` constraints.
- `volumes` for host paths, platform-managed named volumes/PVCs, and OSSFS.
- `networkPolicy` for outbound network policy configuration.
- `secureAccess` for Kubernetes ingress gateway deployments that require endpoint credentials.


### 2.2 Diagnostics API


`specs/diagnostic-api.yml` defines best-effort diagnostic descriptors for sandbox logs and events. The server also exposes practical DevOps diagnostics routes that return plain text for operators and AI troubleshooting workflows.


### 2.3 Execd API


`specs/execd-api.yaml` defines the in-sandbox execution API exposed by `components/execd/`.


Main capabilities:


- Health check: `GET /ping`
- Code contexts and execution: `/code/contexts`, `/code/context`, `/code`
- Bash sessions: `/session`
- Commands: `/command`, command status, and background command logs
- Files and directories: `/files/*`, `/directories`
- Metrics: `/metrics`, `/metrics/watch`


Command and code execution use Server-Sent Events for streaming output. The current `execd` implementation also includes interactive PTY WebSocket endpoints under `/pty` for long-lived shell sessions.


### 2.4 Egress API


`specs/egress-api.yaml` defines the runtime policy and credential broker APIs exposed by `components/egress/`:


- **Policy**: `GET /policy` to inspect the current policy; `PATCH /policy` to mutate rules at runtime.
- **Credential Vault**: `GET`, `POST`, `PATCH`, and `DELETE` on `/credential-vault` to manage sandbox-local credential bindings and token injection without exposing raw secrets to the workload.


For container backends, callers resolve the sandbox endpoint for the egress sidecar port and connect directly (forwarding endpoint authentication headers when sidecar auth is enabled). For FastSandbox, runtime network policy is managed through the lifecycle API (`/sandboxes/{sandboxId}/networkpolicy`), while the shared egress process (one per Fastlet pod) routes policy and per-subject credential vault operations using internal request headers.


## 3. Lifecycle Control Plane


The lifecycle server under `server/` is a FastAPI application. It owns request validation, API-key authentication, server configuration, lifecycle orchestration, endpoint formatting, diagnostics, and server-managed persistence.


### 3.1 Server Structure


Key packages:


- `opensandbox_server/main.py`: app startup, middleware, router registration, runtime validation, and renew-intent startup.
- `opensandbox_server/api/`: lifecycle routes, proxy routes, pool routes, diagnostics routes, and request/response schemas.
- `opensandbox_server/services/`: lifecycle service interfaces and Docker/Kubernetes implementations.
- `opensandbox_server/services/k8s/`: Kubernetes workload providers, endpoint resolution, volume/egress helpers, informer support, and provider-specific mapping.
- `opensandbox_server/repositories/`: persistence adapters, used for server-managed snapshot records and the FastSandbox template catalog.
- `opensandbox_server/integrations/renew_intent/`: optional auto-renew-on-access integration.
- `opensandbox_server/middleware/`: API-key authentication and request ID middleware.


### 3.2 Runtime Service Selection


The server selects its lifecycle implementation based on `[runtime].type`:


- `docker` -> `DockerSandboxService`
- `kubernetes` -> `CompositeSandboxService`, which combines `KubernetesSandboxService` (backed by BatchSandbox or agent-sandbox providers) with `FastSandboxService` for template-based microVM execution.


The top-level `runtime.type` configuration option remains strictly `docker` or `kubernetes`. All implementations satisfy the same `SandboxService` interface, keeping API routes thin and delegating behavior to services. Under Kubernetes mode, `CompositeSandboxService` inspects creation requests: requests specifying a `templateId` dispatch to `FastSandboxService`, while container requests specifying an `image` or `snapshotId` dispatch to `KubernetesSandboxService`. Operations on existing sandboxes are routed by their ID prefix (IDs starting with `fsb-` route to `FastSandboxService`). Runtime-specific details stay behind the service boundary.


### 3.3 Server Persistence


The `[store]` configuration selects SQLite (the default, at `~/.opensandbox/opensandbox.db`) or PostgreSQL. The server persists snapshot metadata and the FastSandbox template catalog through separate repository adapters (`repositories/snapshots/` and `repositories/templates/`). The template catalog stored in the database is the public source of truth; Kubernetes `SandboxTemplate` resources drive golden-image builds and provide asynchronous status updates.


### 3.4 Server Proxy and Endpoint Resolution


The lifecycle endpoint API returns the reachable address for a service port inside a sandbox. Depending on runtime and configuration, the endpoint may be:


- A Docker host/bridge mapped endpoint.
- A Kubernetes ingress gateway endpoint.
- A server-proxied URL under `/sandboxes/{sandboxId}/proxy/{port}` when `use_server_proxy=true`.


Header-routed ingress endpoints include `OpenSandbox-Ingress-To` in their endpoint metadata. When the endpoint is rewritten to a server-proxied URL, the server removes only this ingress routing header and preserves other required endpoint headers.


The server proxy supports HTTP and WebSocket traffic and is also integrated with optional renew-on-access behavior. For HTTP responses, it strips hop-by-hop headers and the backend `Server` header while preserving an origin `Date`; the server adds a current `Date` only when the response does not already contain one. A root-relative `Location` value that starts with a single `/` is rebased under the same sandbox proxy route, while absolute URLs, network-path references (`//host/path`), and ordinary path-relative values are forwarded unchanged.


HTTP proxy responses preserve the sandbox service's status code, body, and `Content-Type`, including redirects and backend errors. The generated Server OpenAPI describes `200` and `default` responses with `*/*` and no fixed payload schema because the sandbox service controls the payload. Server-side validation and authentication still apply before forwarding; the explicit `422` validation response remains documented. These response declarations cover both root and `/v1` aliases, with and without a backend path, for every supported HTTP method.


## 4. Runtime Backends


### 4.1 Docker Runtime


The Docker runtime is the local and single-host backend. It talks directly to the Docker daemon and manages containers, timers, labels, volumes, ports, optional sidecars, and snapshots.


Core responsibilities:


- Pull public or private images, including per-request registry authentication.
- Create containers with CPU, memory, GPU, platform, capability, AppArmor, seccomp, PID, and secure-runtime settings.
- Stage the `execd` binary from `[runtime].execd_image` into the sandbox and install a bootstrap launcher before starting the user entrypoint.
- Support network modes `host`, `bridge`, `none`, `pasta`, `slirp4netns`, and custom user-defined networks. The user-mode modes (`pasta`, `slirp4netns`) expose no host-routable container IP and are reached through the published host ports.
- Allocate host ports for `execd` and user service endpoints in non-host network modes.
- Restore expiration timers for existing managed containers after server restart.
- Support host bind mounts, Docker named volumes via the `pvc` volume model, and OSSFS-backed mounts.
- Attach an egress sidecar when `networkPolicy` is requested and Docker networking is compatible.
- Create Docker-backed persistent snapshots as local images and restore sandboxes from those snapshot images.


Docker pause/resume uses container-level pause/resume. For sandboxes with an egress sidecar, pause freezes the sandbox container before the sidecar, while resume unfreezes the sidecar before the sandbox container. Docker snapshots are exposed through the public snapshot API.


### 4.2 Kubernetes Runtime


The Kubernetes runtime delegates actual workload creation to a workload provider selected by `kubernetes.workload_provider`.


Supported providers:


- `batchsandbox` - the default provider backed by OpenSandbox's Kubernetes controller and `BatchSandbox` CRD.
- `agent-sandbox` - a provider for `kubernetes-sigs/agent-sandbox`.


The Kubernetes server path handles:


- Kubernetes client initialization and informer-backed reads.
- Workload creation from image requests; `snapshotId` startup resolves to a stored restorable image when the snapshot record supports restore.
- Template merging for BatchSandbox and agent-sandbox manifests.
- Per-request image pull secrets where the provider supports them.
- Resource limits and GPU translation to Kubernetes extended resources.
- Platform constraints and RuntimeClass integration for secure runtimes.
- Volumes, egress sidecars, and secure endpoint access annotations.
- Endpoint resolution through direct workload data or ingress gateway configuration.
- Pause/resume delegation to providers.
- Plain-text diagnostics from Kubernetes resources.


### 4.3 BatchSandbox Controller


The Kubernetes controller under `kubernetes/` implements OpenSandbox-specific CRDs for high-throughput and pooled sandbox delivery:


- `BatchSandbox`: create one or many sandbox replicas from a pod template.
- `Pool`: maintain pre-warmed resources for fast allocation.
- `SandboxSnapshot`: snapshot records used by BatchSandbox pause/resume and the public snapshot workflow.


BatchSandbox supports both template-based creation and pool-based creation via `extensions.poolRef`. It also supports optional task orchestration for batch and RL-style workloads.


For supported single-replica BatchSandbox workloads, the rootfs pause/resume path commits the sandbox filesystem to an OCI image and releases runtime resources; resume recreates the workload from that image while preserving the sandbox ID. Workloads configured with a QEMU snapshot contract use a VM-state checkpoint and restore path instead.


The public snapshot API supports Docker and compatible `BatchSandbox` workloads. `DockerSnapshotRuntime` commits containers to local images, while `KubernetesSnapshotRuntime` creates a public `SandboxSnapshot` CR to commit and push images to an OCI registry. This is distinct from internal pause/resume, which releases compute while preserving sandbox continuity. Public snapshot support does not extend to every Kubernetes provider or VM runtime.


### 4.4 FastSandbox Integration


In Kubernetes mode, `FastSandboxService` connects OpenSandbox to the external `fast-sandbox` platform for template-backed microVM provisioning:


- **Routing**: `CompositeSandboxService` routes create requests with `templateId` to `FastSandboxService`, and routes operations on existing sandboxes by the `fsb-` ID prefix. FastSandbox is part of the Kubernetes composition, not a separate `runtime.type` value.
- **Control Protocol**: Communicates with an external `fast-sandbox` control plane via gRPC FastPath v2 (port 9090).
- **State**: FastPath owns mutations and live runtime operations; Kubernetes LIST/WATCH reads persisted `sandbox.fast.io/v1alpha2` resources and their observations.
- **Pause/resume**: Delegates to FastPath, which restores the checkpoint on resume. Clients must resolve endpoints again after restoration.
- **Networking**: The configured Fastlet pool supplies a shared egress process (one per Fastlet pod); the adapter sends network policy through FastPath Actions. This differs from attaching a per-sandbox container sidecar. The current server adapter rejects the `credentialProxy.enabled` creation flag and volume mounts on this path.


The adapter and endpoint integration live in this repository; FastPath and the microVM runtime are provided by the external platform. See the [service dispatch](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/opensandbox_server/services/composite_service.py) and [FastSandbox adapter](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/opensandbox_server/services/fast_sandbox/service.py) for the implementation boundaries, and the [Fast Sandbox integration](https://open-sandbox.ai/architecture/fast-sandbox/) documentation for the full design.


## 5. Sandbox Data Plane


Each sandbox runs the user's image and entrypoint, with OpenSandbox control processes injected around it.


### 5.1 Execd


`components/execd/` is a Go daemon built with Gin. It runs inside the sandbox and exposes the execution API.


Responsibilities:


- Shell command execution with SSE streaming.
- Background command status and incremental log retrieval.
- Persistent bash sessions.
- Interactive PTY sessions over WebSocket.
- File and directory operations.
- Process isolation sessions for executing commands in isolated environments.
- Jupyter-backed code contexts and code execution.
- Local CPU/memory metrics and optional OpenTelemetry metrics export.
- Optional shared access token enforcement through `X-EXECD-ACCESS-TOKEN`.


In Docker, the server stages `execd` into the container and installs a bootstrap script. In Kubernetes BatchSandbox template mode, an init container copies `execd` and `bootstrap.sh` from the configured `execd_image` into an `emptyDir` volume mounted by the main sandbox container.


For FastSandbox, the template build includes `execd` in the guest image before the microVM starts.


### 5.2 Code Interpreter Runtime


The code-interpreter sandbox image starts Jupyter inside the sandbox. `execd` talks to Jupyter over HTTP/WebSocket and translates Jupyter kernel messages into OpenSandbox streaming events.


The Code Interpreter SDKs are optional high-level clients. The lower-level execution API remains available through the sandbox SDKs and direct `execd` clients.


### 5.3 Volumes


The lifecycle API exposes runtime-neutral volume models:


- `host`: bind a permitted host path.
- `pvc`: platform-managed named storage. Docker maps this to a Docker named volume; Kubernetes maps it to a PersistentVolumeClaim.
- `ossfs`: mount Alibaba Cloud OSS through the server/runtime integration.


Runtime providers validate and materialize these volume definitions differently, but the API shape stays shared. Volume mounts are supported for Docker and Kubernetes container workloads; the FastSandbox adapter currently rejects volume mounts.


### 5.4 Egress Sidecar


`components/egress/` enforces outbound network policy and provides credential proxying for sandboxes.


Capabilities:


- FQDN and wildcard-domain allow/deny rules.
- `dns` mode for DNS filtering.
- `dns+nft` mode for DNS plus nftables enforcement of resolved IPs and CIDR/IP rules where supported.
- Credential Vault / Proxy: transparent TLS MITM proxy (active in `dns+nft` mode) that provides scoped credential injection for outbound HTTPS requests based on host-managed secret bindings, keeping raw secrets out of the sandbox workload.
- Runtime policy inspection and patching through `/policy`.
- Optional sidecar authentication.
- Optional platform-enforced always-allow and always-deny overlays.


Docker starts the egress sidecar as a separate container and runs the main sandbox container in the sidecar network namespace. Kubernetes container providers append the egress sidecar to the pod spec and drop `NET_ADMIN` from the main sandbox container so only the sidecar mutates network rules. FastSandbox uses the shared egress process (one per Fastlet pod, outside the microVM guest), receiving policy actions through FastPath.


## 6. Networking and Access


### 6.1 Ingress


`components/ingress/` is a Kubernetes-oriented HTTP/WebSocket reverse proxy. It watches sandbox resources and routes traffic to sandbox ports.


Supported routing modes:


- Header mode: `OpenSandbox-Ingress-To: <sandbox-id>-<port>` or host parsing.
- URI mode: `/<sandbox-id>/<port>/<path>`.
- Wildcard host mode through server endpoint formatting.


For `BatchSandbox`, ingress reads endpoint data from the `sandbox.opensandbox.io/endpoints` annotation. For `agent-sandbox`, it reads `status.serviceFQDN`.


For FastSandbox routes, ingress asks FastPath to resolve the endpoint and forwards traffic through the returned Fastlet or central proxy address.


### 6.2 Secure Access


`secureAccess` is currently supported for Kubernetes sandboxes exposed through ingress gateway mode. When enabled, the server provisions endpoint credentials and returns required headers with endpoint responses. Signed route tokens are also supported when gateway secure-access signing keys are configured.


### 6.3 Auto-Renew on Access


The optional renew-intent integration extends sandbox TTL when access is observed. It can be triggered by server proxy requests or by ingress gateway events delivered through Redis. Per-sandbox opt-in is controlled by the `extensions["access.renew.extend.seconds"]` create parameter.


## 7. Core Flows


### 7.1 Sandbox Creation

text

```
Client / SDK / CLI / MCP
  -> POST /v1/sandboxes
  -> FastAPI lifecycle server validates request and config
  -> selected service creates a Docker container, Kubernetes workload, or FastSandbox microVM
  -> runtime stages execd or uses a prepared guest image, with backend-specific networking and storage
  -> sandbox reaches Running or reports Failed with status reason/message
```


Creation is asynchronous from the API perspective. Clients should poll `GET /v1/sandboxes/{sandboxId}` or use SDK readiness helpers.


### 7.2 Command, File, and Code Execution

text

```
Client
  -> resolve execd endpoint from sandbox metadata or server proxy
  -> call execd API with X-EXECD-ACCESS-TOKEN when required
  -> execd runs command, file operation, session, PTY, or Jupyter code execution
  -> execd streams SSE/WebSocket output or returns structured responses
```


### 7.3 Service Exposure

text

```
Client
  -> GET /v1/sandboxes/{sandboxId}/endpoints/{port}
  -> server returns Docker-mapped, ingress-gateway, or server-proxy endpoint
  -> client includes returned headers when secure access or sidecar auth requires them
  -> HTTP/WebSocket traffic reaches the target sandbox port
```


### 7.4 Egress Policy

text

```
Create request with networkPolicy
  -> server validates runtime-specific network policy settings
  -> runtime attaches egress sidecar or binds policy actions to the shared Fastlet egress process
  -> sandbox outbound DNS/network traffic is filtered
  -> FastSandbox clients manage policy via GET/PUT/PATCH/DELETE /v1/sandboxes/{sandboxId}/networkpolicy
  -> container clients resolve the egress endpoint and PATCH /policy
```


### 7.5 Pause, Resume, and Snapshots

text

```
Pause / resume
  -> lifecycle server delegates to runtime provider
  -> Docker pauses/resumes the sandbox container and its egress sidecar when present
  -> BatchSandbox uses rootfs commit/recreate or the configured QEMU VM-state restore path
  -> FastSandbox delegates pause/resume to external FastPath v2 service

Public snapshot API
  -> server persists snapshot metadata
  -> Docker runtime commits the sandbox to a local OCI image
  -> Kubernetes runtime (scoped to BatchSandbox) creates a public SandboxSnapshot CR that commits and pushes to an OCI registry
  -> create-from-snapshot resolves that image and starts a new sandbox
```


## 8. Design Principles


### Protocol First


Public behavior starts from OpenAPI contracts in `specs/`. SDKs and clients should align to those contracts, and generated outputs should be regenerated from source specs rather than patched as the only fix.


### Control Plane vs Data Plane


The lifecycle server should orchestrate and validate. Platform-specific provisioning belongs in runtime services/providers. In-sandbox operations belong in `execd` and egress sidecars.


### Runtime Neutral API, Runtime Specific Execution


The lifecycle API uses shared concepts such as resource limits, volumes, endpoints, network policy, and metadata. Docker and Kubernetes can materialize those concepts differently while preserving the API contract.


### Secure Defaults with Explicit Escape Hatches


The server supports API-key authentication, startup guardrails for unauthenticated mode, resource limits, capability drops, optional secure runtimes, egress controls, endpoint headers, and platform-specific network isolation. Less restrictive modes are intended for local development or explicit operator choice.


### Observable Failures


Sandbox state includes `state`, `reason`, `message`, and transition time. `execd` exposes metrics, the server exposes diagnostics, ingress/egress/execd support logs and OpenTelemetry metrics where implemented, and request IDs are propagated for debugging.


## 9. Common Use Cases


- **Coding agents**: run Claude Code, Gemini CLI, Codex CLI, Qwen Code, Kimi CLI, or other agent tools in isolated sandboxes.
- **AI code execution**: execute model-generated code with command/file/code-interpreter APIs and streamed feedback.
- **Browser automation**: run Chrome or Playwright with controlled filesystem and network behavior.
- **Remote development**: expose VS Code Web, desktops, VNC, or development servers through sandbox endpoints.
- **RL and evaluation workloads**: use Kubernetes BatchSandbox, Pool, and task orchestration for high-throughput sandbox delivery.
- **Enterprise isolation**: combine secure runtimes, ingress, egress, endpoint access headers, and Kubernetes deployment controls.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/deployment`

# Kubernetes Deployment
## Prerequisites ​
## Deployment Order ​
## Install ​
*Add optional resource settings to the [egress] section of configToml:*

## Upgrade ​
## Operator Metrics ​
*Enable it through the opensandbox-controller chart values:*

## Configure the Server for Kubernetes ​
*See Configuration for the full reference.*

## Components on Kubernetes ​
## Uninstall ​
## Related ​











This guide covers deploying OpenSandbox on Kubernetes: the cluster foundation (CRDs), the controller, the lifecycle server, and the optional components (ingress gateway, node agent, fast-sandbox runtime).


Charts are versioned sources in the [OpenSandbox repository](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts). They are installed from a checkout of a `release-X.Y.Z` tag — standalone chart packages are not published.


## Prerequisites


- Kubernetes 1.21.1+
- Helm 3.x
- `kubectl` configured for your cluster


## Deployment Order


Install the charts in this order:

text

```
base → opensandbox-controller → fast-sandbox* → ingress-gateway → opensandbox-server → optional components
```


* `fast-sandbox` is optional, but when used it must be installed **before** the ingress gateway and the server. `ingress-gateway` is required for Kubernetes deployments — sandbox Pods are ClusterIP-only, so client traffic routes through the gateway. It is installed **before the server** so the server announces it from the first install.


| Step | Chart | Why it comes here |
| --- | --- | --- |
| 1 | `base` | Owns the `sandbox.opensandbox.io` CRDs, the fast-sandbox CRDs (`sandbox.fast.io`), and their RBAC. Everything else depends on these objects existing. Install once per cluster. |
| 2 | `opensandbox-controller` | Reconciles `BatchSandbox`, `Pool`, and `SandboxSnapshot` objects created by you and by the server. Requires the CRDs from `base`. |
| 3 | `fast-sandbox` (optional) | Firecracker runtime (`sandbox.fast.io`). Must be installed **before the server**: the server's `[runtime]` /fsb configuration points at the FastPath gRPC endpoint (`fast-sandbox-fastpath...svc:9090`) and watches `sandbox.fast.io` objects at startup. Also consumes the ServiceAccounts from `base` — keep the namespace values in sync with it. Skip if you only use the default Kubernetes runtime. |
| 4 | `ingress-gateway` | Required for Kubernetes deployments: sandbox Pods are ClusterIP-only and client traffic routes through the gateway. Installed before the server so the announcement is configured from the first install. When serving sandboxes through the fsb runtime, point `gateway.fastpathEndpoint` at the FastPath service from the previous step. |
| 5 | `opensandbox-server` | The lifecycle REST API that creates and deletes sandboxes. Requires the CRDs from `base`, a running controller, and — when serving sandboxes through the fsb runtime — the FastPath endpoint from the fast-sandbox release. Announces the ingress gateway through `server.gateway.*`. |
| 6 | `opensandbox-node-agent` (optional) | Node-level sandbox data collection. Order-independent. |


If you use the umbrella chart, this order is handled for you in a single release.


## Install


Check out the version you want to deploy:

bash

```
git clone https://github.com/opensandbox-group/OpenSandbox.git
cd OpenSandbox
git checkout release-1.1.0   # or main for development
```


### Option 1: Umbrella chart (recommended)


One release installs every component with the correct ordering:

bash

```
cd manifests/charts

# Package the sub-charts (charts/ is git-ignored, rebuilt every time)
helm dependency build opensandbox

helm install opensandbox opensandbox \
  --namespace opensandbox-system \
  --create-namespace
```


Optional components default to off. For Kubernetes deployments, enable the ingress gateway — sandbox Pods are ClusterIP-only and client traffic routes through it:

bash

```
helm install opensandbox opensandbox \
  --namespace opensandbox-system \
  --create-namespace \
  --set ingress-gateway.enabled=true
```


### Option 2: Per-component releases

bash

```
# 1. Cluster foundation: CRDs + RBAC
helm install base manifests/charts/base

# 2. Controller
helm install opensandbox-controller manifests/charts/controller \
  --namespace opensandbox-system \
  --create-namespace

# 3. Ingress gateway (required on Kubernetes; see Deployment Order)
helm install ingress-gateway manifests/charts/ingress-gateway \
  --namespace opensandbox-system

# 4. Lifecycle server
helm install opensandbox-server manifests/charts/server \
  --namespace opensandbox-system \
  --create-namespace
```


### Configure API authentication


By default, the server refuses to start without an API key in a non-interactive container. Create both the control-plane namespace and the default sandbox workload namespace, then store the key in a Kubernetes `Secret`:

bash

```
kubectl create namespace opensandbox-system --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace opensandbox --dry-run=client -o yaml | kubectl apply -f -

read -s OPENSANDBOX_API_KEY
kubectl create secret generic opensandbox-api-key \
  --namespace opensandbox-system \
  --from-literal=api-key="${OPENSANDBOX_API_KEY}" \
  --dry-run=client -o yaml | kubectl apply -f -
unset OPENSANDBOX_API_KEY
```


Reference the Secret from a values file:

yaml

```
# values-server.yaml
server:
  replicaCount: 1
  env:
    - name: OPENSANDBOX_SERVER_API_KEY
      valueFrom:
        secretKeyRef:
          name: opensandbox-api-key
          key: api-key
```


Use an external secret manager instead of creating the Secret manually in production environments.


The chart installs the server into `opensandbox-system`, while the default `configToml` creates sandbox and pool resources in `opensandbox`. If you change `[kubernetes].namespace` in `configToml`, create that namespace instead of `opensandbox` before submitting workloads.


Single-active Server default


The chart defaults to `server.replicaCount: 1`. Keep one active Lifecycle Server unless you deliberately use the PostgreSQL-backed Kubernetes public snapshot topology documented below. That exception coordinates public snapshots only; it does not provide general multi-replica Server HA. The Server Deployment uses the `Recreate` strategy so an upgrade stops the active Server before starting its replacement; expect a brief API interruption during upgrades.


### Use PostgreSQL for server persistence


Create a Secret containing the PostgreSQL connection string:

bash

```
read -s OPENSANDBOX_POSTGRESQL_DSN
kubectl create secret generic opensandbox-postgresql \
  --namespace opensandbox-system \
  --from-literal=dsn="${OPENSANDBOX_POSTGRESQL_DSN}" \
  --dry-run=client -o yaml | kubectl apply -f -
unset OPENSANDBOX_POSTGRESQL_DSN
```


In `values-server.yaml`, keep the default `server.replicaCount` at `1`, add the Secret-backed environment variable below, and add the shown `[store]` tables to the complete `configToml` value:

yaml

```
server:
  replicaCount: 1
  env:
    - name: OPENSANDBOX_STORE_POSTGRESQL_DSN
      valueFrom:
        secretKeyRef:
          name: opensandbox-postgresql
          key: dsn

configToml: |
  # Keep the rest of the chart's complete server configuration here.
  [store]
  type = "postgresql"

  [store.postgresql]
  min_pool_size = 1
  max_pool_size = 10
  snapshot_recovery_interval_seconds = 15
```


INFO


The chart default remains one Server replica. You may explicitly set `server.replicaCount: 2` for multi-active public snapshot handling only when both replicas use the same PostgreSQL database and the Kubernetes runtime. SQLite and Docker snapshot execution do not support this multi-active topology.


### Install the server with the API key and verify


Install the server referencing your values file:

bash

```
helm install opensandbox-server manifests/charts/server \
  --namespace opensandbox-system \
  --create-namespace \
  --values values-server.yaml
```


Wait for the Deployment and verify the API health endpoint:

bash

```
kubectl rollout status deployment/opensandbox-server \
  --namespace opensandbox-system \
  --timeout=180s

kubectl port-forward \
  --namespace opensandbox-system \
  service/opensandbox-server 8080:80
```


In another terminal:

bash

```
curl --fail http://127.0.0.1:8080/health
```


### Important values


| Value | Purpose | Notes |
| --- | --- | --- |
| `server.image.repository` | Server image registry and repository | Override for a private mirror or custom build. |
| `server.image.tag` | Server image version | Defaults to the `release-<appVersion>` image published with the chart version; override only for custom builds. |
| `server.replicaCount` | Number of server Pods | Defaults to `1`; general multi-replica Server HA is not supported yet. |
| `server.env` | Additional container environment variables | Use it with `secretKeyRef` for `OPENSANDBOX_SERVER_API_KEY`. |
| `configToml` | Complete server configuration | Mounted at `/etc/opensandbox/config.toml`; overriding it replaces the complete default TOML, including the workload namespace. |
| `server.gateway.enabled` | Announce an ingress gateway to clients | Defaults to `false`. The gateway itself is deployed by the [ingress-gateway chart](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts/ingress-gateway). |
| `server.service.type` | Service type for the server | Defaults to `ClusterIP`. Use `NodePort` or `LoadBalancer` for access from outside the cluster; pin the port with `server.service.nodePort`. |
| `namespaceOverride` | Namespace used by chart resources | Defaults to `opensandbox-system`. |


The server container and its Service use port `80`. Keep `[server].port = 80` when replacing `configToml` unless the chart templates are also updated to use a different port. The Service is `ClusterIP` by default; set `server.service.type` to reach the server from outside the cluster.


### Configure egress sidecar resources


When a create request includes `networkPolicy`, the lifecycle server adds an egress sidecar to each non-pooled sandbox Pod. Namespace `LimitRange` defaults apply to this container when it does not declare resources, which can reserve substantially more capacity than basic DNS/nft enforcement needs.


Add optional resource settings to the `[egress]` section of `configToml`:

toml

```
[egress]
image = "opensandbox/egress:release-1.1.0"
requests = { cpu = "25m", memory = "64Mi" }
limits = { cpu = "250m", memory = "256Mi" }
```


You can omit either `requests` or `limits`. Treat these values as a starting point and tune them from observed usage; Credential Vault and transparent mitmproxy generally need more headroom than basic DNS/nft enforcement.


### Ingress gateway (required on Kubernetes)


Sandbox Pods on Kubernetes are ClusterIP-only — client traffic reaches sandboxes through the ingress gateway (`[ingress] mode = "gateway"`, the Kubernetes-oriented mode; the Docker runtime uses `direct` and does not need the gateway). Install the gateway **before the server**, then include the announcement in the server install:

bash

```
helm install ingress-gateway manifests/charts/ingress-gateway \
  --namespace opensandbox-system \
  --set gateway.fastpathEndpoint=fast-sandbox-fastpath.opensandbox-system.svc:9090
```


Install the server with the announcement enabled (or `helm upgrade` an existing server release with the same flags):

bash

```
helm install opensandbox-server manifests/charts/server \
  --namespace opensandbox-system \
  --set server.gateway.enabled=true \
  --set server.gateway.host=gateway.example.com \
  --values values-server.yaml
```


Keep `server.gateway.gatewayRouteMode` in sync with `gateway.gatewayRouteMode` of the gateway chart. For signed, expiring sandbox routes, configure the shared secure-access key ring on both charts — see [secure-access keys](https://github.com/opensandbox-group/OpenSandbox/blob/main/manifests/HELM-DEPLOYMENT.md#secure-access-keys-osep-0011).


### Optional: fast-sandbox runtime


The `fast-sandbox` chart adds the Firecracker (`sandbox.fast.io`) runtime. Install it **before the ingress gateway and the lifecycle server** (see [Deployment Order](https://open-sandbox.ai/deployment/#deployment-order)): the server's `[runtime]` /fsb configuration points at the FastPath gRPC endpoint this chart creates. It also requires `base` first, KVM-capable nodes, and companion images built from a pinned upstream commit — see the [fast-sandbox runtime deployment guide](https://github.com/opensandbox-group/OpenSandbox/blob/main/manifests/HELM-DEPLOYMENT.md#fast-sandbox-runtime-firecracker).


## Upgrade


Upgrade the umbrella release from a newer checkout:

bash

```
git fetch --tags
git checkout release-1.2.0

cd manifests/charts
helm dependency build opensandbox
helm upgrade opensandbox opensandbox --namespace opensandbox-system
```


For a per-component server release:

bash

```
git checkout release-1.2.0
helm upgrade opensandbox-server manifests/charts/server \
  --namespace opensandbox-system \
  --values values-server.yaml
```


For the complete values reference and local development installation, see the [`opensandbox-server` chart README](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts/server).


## Operator Metrics


The operator (controller-manager) exposes standard [controller-runtime](https://book.kubebuilder.io/reference/metrics) Prometheus metrics — reconcile rate and latency (`controller_runtime_reconcile_*`), work-queue depth, client-go request counts, and Go runtime stats. The endpoint is **disabled by default** (`--metrics-bind-address=0`).


Enable it through the `opensandbox-controller` chart values:


| Value | Default | Purpose |
| --- | --- | --- |
| `controller.metrics.enabled` | `false` | Expose the `/metrics` endpoint (sets `--metrics-bind-address`) |
| `controller.metrics.port` | `8080` | Port for the metrics endpoint |
| `controller.metrics.secure` | `false` | Serve over HTTPS with authn/authz (`--metrics-secure`); set `false` for plain HTTP scraping |

yaml

```
controller:
  metrics:
    enabled: true
    port: 8080
    secure: false   # plain HTTP, e.g. for a PodMonitoring/ServiceMonitor scrape
```


- With `secure: false` the endpoint is plain HTTP and can be scraped directly (no TLS or bearer token).
- With `secure: true` the controller-runtime filter authenticates and authorizes each scrape via `TokenReview`/`SubjectAccessReview`. The chart then provisions two `ClusterRole`s automatically:
  - `opensandbox-metrics-auth-role` (bound to the manager) — lets the controller run the auth checks.
  - `opensandbox-metrics-reader` (**not** bound by the chart) — grants `get` on the `/metrics` non-resource URL. Bind it to your scraper's `ServiceAccount` (e.g. Prometheus) and have the scraper present that account's bearer token.


Point your Prometheus stack at the `metrics` container port (for example via a `ServiceMonitor` or `PodMonitoring`).


### Business capacity metrics


The elected controller also exports low-cardinality business capacity metrics over OTLP/HTTP when `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` or `OTEL_EXPORTER_OTLP_ENDPOINT` is set. This is independent of the controller-runtime Prometheus endpoint and remains disabled when neither variable is configured.

yaml

```
extraEnv:
  - name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
    value: http://otel-collector.observability:4318/v1/metrics
```


| Metric | Unit | Attributes | Description |
| --- | --- | --- | --- |
| `controller.pool.pods` | `{pod}` | `namespace`, `pool_name`, `state` | Current Pool Pods, where `state` is `total`, `allocated`, `available`, or `updated` |
| `controller.pool.cpu.requested` | `{cpu}` | `namespace`, `pool_name`, `state` | Scheduler-equivalent CPU requests represented by total, allocated, or available Pool Pods |
| `controller.pool.memory.requested` | `By` | `namespace`, `pool_name`, `state` | Scheduler-equivalent memory requests represented by total, allocated, or available Pool Pods |
| `controller.batchsandbox.count` | `{batchsandbox}` | `namespace`, `phase`, `allocation_mode` | Current BatchSandbox objects by lifecycle phase and pool/direct mode |
| `controller.batchsandbox.pods` | `{pod}` | `namespace`, `state`, `allocation_mode` | Desired, current, allocated, and ready BatchSandbox Pod counts |
| `controller.capacity.collect.duration` | `s` | None | Time spent reading cached objects and collecting one capacity snapshot |


The metrics deliberately omit sandbox, BatchSandbox, and Pod identifiers. Only the leader exports them, so multiple controller replicas do not duplicate cluster totals. An unset initial BatchSandbox phase is exported as `Unknown`. Derive Pool utilization from `allocated / total` and calculate peak, valley, or percentile capacity in the telemetry backend. Actual CPU and memory usage remains available from kubelet/cAdvisor rather than being duplicated here.


Each collection reads all Pools and BatchSandboxes from the controller manager's informer cache, then performs one cached, owner-UID-indexed Pod list for every non-deleting Pool. Collection CPU and memory therefore grow linearly with the number of cached Pools, BatchSandboxes, and Pool-owned Pods, without issuing one API-server list request per Pool. The OpenTelemetry periodic reader exports every 60 seconds by default; `OTEL_METRIC_EXPORT_INTERVAL` can change the interval in milliseconds. Monitor `controller.capacity.collect.duration` and validate the target cluster scale before shortening that interval. If OTLP setup fails after an endpoint is configured, the controller continues reconciling and logs the failed setup stage together with the endpoint environment variable and a credential-stripped endpoint.


## Configure the Server for Kubernetes


Generate a Kubernetes-oriented server config:

bash

```
opensandbox-server init-config ~/.sandbox.toml --example k8s
```


Key Kubernetes-specific configuration sections:


| Section | Purpose |
| --- | --- |
| `[kubernetes]` | Workload provider, BatchSandbox template file |
| `[agent_sandbox]` | Agent sandbox settings |
| `[ingress]` | Ingress gateway for sandbox traffic routing |
| `[secure_runtime]` | Secure container runtime (gVisor, Kata) |


See [Configuration](https://open-sandbox.ai/getting-started/configuration) for the full reference.


## Components on Kubernetes


| Component | Deployment | Purpose |
| --- | --- | --- |
| CRDs + RBAC (`base`) | Cluster-scoped | `BatchSandbox`, `Pool`, `SandboxSnapshot` and `sandbox.fast.io` API types |
| Server | Deployment | Lifecycle control plane |
| Controller (operator) | Deployment | Manages BatchSandbox/Pool CRDs |
| Ingress gateway | Deployment | Routes traffic to sandboxes; required on Kubernetes deployments |
| Egress | Sidecar | Per-sandbox egress policy enforcement |
| Execd | Built into sandbox images | In-sandbox execution |
| Node agent | DaemonSet | Optional node-level sandbox data collection |
| fast-sandbox | Deployment + DaemonSet | Optional Firecracker control plane and node runtime |


## Uninstall

bash

```
helm uninstall opensandbox -n opensandbox-system
```


CRDs carry the `helm.sh/resource-policy: keep` annotation and are retained across uninstalls; the `opensandbox-dataplane` namespace (created by `base` for fast-sandbox) is kept as well. Delete them manually once their data is no longer needed:

bash

```
kubectl delete crd batchsandboxes.sandbox.opensandbox.io \
  pools.sandbox.opensandbox.io \
  sandboxsnapshots.sandbox.opensandbox.io
kubectl delete namespace opensandbox-dataplane
```


- [Kubernetes Overview](https://open-sandbox.ai/architecture/control-plane/operator) — Operator features and CRDs
- [Pause & Resume](https://open-sandbox.ai/guides/pause-resume) — Snapshot-based pause/resume on Kubernetes
- [Secure Container](https://open-sandbox.ai/guides/secure-container) — gVisor and Kata on Kubernetes
- [Network Isolation on Kubernetes](https://open-sandbox.ai/guides/network-isolation) — Egress policy design for Kubernetes
- [Helm charts source](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts) — Chart sources and values reference[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/deployment/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/reference/execd-path-migration`

# Execd Path Migration Guide


PR: [#1014](https://github.com/opensandbox-group/OpenSandbox/pull/1014)


## Background


OpenSandbox previously installed execd and bootstrap.sh to `/opt/opensandbox/bin/`, creating unnecessary nesting. The execd image already places these artifacts at the root:


```
/execd
/bootstrap.sh
```


While bootstrap.sh defaults to `EXECD=/opt/opensandbox/execd` (no `bin/`), the Kubernetes provider and Pool CR templates historically injected files into a `bin/` subdirectory. This PR flattens the layout:


| Before | After |
| --- | --- |
| `/opt/opensandbox/bin/execd` | `/opt/opensandbox/execd` |
| `/opt/opensandbox/bin/bootstrap.sh` | `/opt/opensandbox/bootstrap.sh` |
| `/opt/opensandbox/bin/task-executor` | `/opt/opensandbox/task-executor` |


Additionally, the Docker runtime now uses the **full** `bootstrap.sh` from the execd image instead of a minimal 15-line inline-generated shim. This gives Docker sandboxes the same capabilities as Kubernetes: MITM CA trust setup, SIGTERM forwarding, pre-script sourcing, and chained commands.


## Who is affected


| User profile | Impact |
| --- | --- |
| **code-interpreter image `<=v1.0.2`** | **Must upgrade to `v1.1.0`** — emptyDir at `/opt/opensandbox` shadows old scripts under `/opt/opensandbox/` |
| **Pool CR with custom templates** | Must update execd init container paths and volume mount |
| **Custom execd images** | Must now include `/bootstrap.sh` alongside `/execd` |
| **Docker runtime users (default)** | No manual action — bootstrap.sh is auto-installed |


## Migration steps


### 1. code-interpreter image


**Must upgrade the image from `v1.0.2` to `v1.1.0`.**


In code-interpreter `v1.0.2`, the entrypoint scripts (`code-interpreter.sh`, `code-interpreter-env.sh`) live directly under `/opt/opensandbox/`. Before this PR, the emptyDir volume was mounted at `/opt/opensandbox/bin/`, shadowing only that subdirectory. Now the emptyDir mounts at `/opt/opensandbox/`, shadowing the entire directory — including those scripts. The pod starts but cannot find its own entrypoint.


[PR #1012](https://github.com/opensandbox-group/OpenSandbox/pull/1012) moved all code-interpreter scripts from `/opt/opensandbox/` to `/opt/code-interpreter/`, avoiding the conflict. Version `v1.1.0` is the first image with that change.

yaml

```
# In your Pool CR or sandbox creation request:
image: sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0
```


The Python SDK (`opensandbox-code-interpreter`) does not require an upgrade — it communicates with execd over the network and does not reference filesystem paths.


### 2. Pool CR template
*PR: #1014*

## Background ​
## Who is affected ​
## Migration steps ​
*Must upgrade the image from v1.0.2 to v1.1.0.*

## Compatibility ​
## Release notes ​







If you maintain a custom Pool CR that defines the execd init container, update it:

yaml

```
# Before
initContainers:
  - name: execd-installer
    image: opensandbox/execd:latest
    args:
      - |
        cp ./execd /opt/opensandbox/bin/execd &&
        cp ./bootstrap.sh /opt/opensandbox/bin/bootstrap.sh &&
        chmod +x /opt/opensandbox/bin/execd &&
        chmod +x /opt/opensandbox/bin/bootstrap.sh
    volumeMounts:
      - name: opensandbox-bin
        mountPath: /opt/opensandbox/bin

# After
initContainers:
  - name: execd-installer
    image: opensandbox/execd:latest
    args:
      - |
        cp ./execd /opt/opensandbox/execd &&
        cp ./bootstrap.sh /opt/opensandbox/bootstrap.sh &&
        chmod +x /opt/opensandbox/execd &&
        chmod +x /opt/opensandbox/bootstrap.sh
    volumeMounts:
      - name: opensandbox-bin
        mountPath: /opt/opensandbox
```


The same update applies to the task-executor init container if used:

yaml

```
# Before
cp /workspace/server /opt/opensandbox/bin/task-executor && chmod +x /opt/opensandbox/bin/task-executor
# After
cp /workspace/server /opt/opensandbox/task-executor && chmod +x /opt/opensandbox/task-executor
```


And the main container's env vars and volume mount:

yaml

```
# Before
- name: EXECD
  value: /opt/opensandbox/bin/execd
volumeMounts:
  - name: opensandbox-bin
    mountPath: /opt/opensandbox/bin

# After
- name: EXECD
  value: /opt/opensandbox/execd
volumeMounts:
  - name: opensandbox-bin
    mountPath: /opt/opensandbox
```


### 3. Custom execd images (Docker)


If you override `[runtime].execd_image` with a custom image, that image must now contain `/bootstrap.sh` **in addition to** `/execd`. Previously only `/execd` was required because the Docker runtime generated a minimal inline bootstrap script.


If your custom execd image is built from a Dockerfile that only copies the execd binary, add bootstrap.sh:

dockerfile

```
COPY bootstrap.sh /bootstrap.sh
```


The official `opensandbox/execd` image already includes both files and requires no change.


### 4. Custom entrypoint scripts


If you hardcode `/opt/opensandbox/bin/execd` or `/opt/opensandbox/bin/bootstrap.sh` in entrypoint scripts or build pipelines, update those references to `/opt/opensandbox/`.


## Compatibility


### Old paths are not available


After this change, the paths `/opt/opensandbox/bin/execd` and `/opt/opensandbox/bin/bootstrap.sh` no longer exist. Any script, tool, or template referencing them will fail with "file not found".


### How failures manifest


| Scenario | Failure mode |
| --- | --- |
| Old code-interpreter image (`<=v1.0.2`) | emptyDir at `/opt/opensandbox` shadows `code-interpreter.sh`; pod starts but entrypoint not found |
| Old Pool CR template | execd init container succeeds (it copies to its own mount), but main container cannot find `/opt/opensandbox/bin/bootstrap.sh` |
| Old custom execd image (no bootstrap.sh) | Docker sandbox creation fails with "bootstrap.sh not found in execd image cache" |


### Verification


After migration, confirm the sandbox starts successfully:

bash

```
# In a running sandbox:
ls /opt/opensandbox/execd /opt/opensandbox/bootstrap.sh
# Both should exist. Verify /opt/opensandbox/bin/ does NOT exist:
test -d /opt/opensandbox/bin && echo "STALE PATH EXISTS" || echo "OK"
```


## Release notes


For release note authors: include a summary that links to this document.

markdown

```
### Breaking: execd install path flattened

execd and bootstrap.sh are now installed to `/opt/opensandbox/` instead of
`/opt/opensandbox/bin/`. code-interpreter image users must upgrade to `>=v1.1.0`.
Custom Pool CR templates and custom execd images require updates.

See [execd Path Migration Guide](/reference/execd-path-migration) for full details.
```[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/reference/execd-path-migration.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/community/contributing`

# Contributing to OpenSandbox
## Contributor Advancement ​



The contributing guide is maintained in the repository root to keep GitHub's contributor experience consistent.

[Read the Contributing Guide on GitHub →](https://github.com/opensandbox-group/OpenSandbox/blob/main/CONTRIBUTING.md)

## Contributor Advancement


OpenSandbox maintains an explicit advancement process for contributors to become component maintainers or project maintainers. For nomination requirements, voting periods, and approval thresholds, see the project governance guide:

[Read the Maintainer Advancement Process on GitHub →](https://github.com/opensandbox-group/OpenSandbox/blob/main/GOVERNANCE.md#becoming-a-maintainer)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/community/contributing.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/data-plane/execd`

Return to top

# Execd
## Capabilities at a glance ​
## API surface ​
## Command execution ​
## Code execution ​
## Interactive terminals ​
## Files and directories ​
## Isolated sessions ​
*See the Isolation Sessions guide for the full workflow.*

## Layered security ​
## Supervision and exit codes ​
## A fresh identity per allocation ​
## Observability ​













Execd is the reference daemon for OpenSandbox's in-sandbox execution API. Sandbox SDK command and file operations use this API; sandbox creation and lifecycle management use the separate lifecycle server. Clients can also access workload-specific services through resolved sandbox endpoints, using those services' own protocols and clients.


For example, the [AIO Sandbox example](https://open-sandbox.ai/examples/aio-sandbox) resolves port `8080` and uses `AioSandboxClient` for the image's shell, file, and browser API. Those requests are not execd command or file operations, even when an execd reverse proxy carries the traffic. See [Implementation compatibility](https://open-sandbox.ai/api/implementation-compatibility) for the published contracts, current SDK endpoint assumptions, and backend-dependent features.


![execd overview](https://open-sandbox.ai/assets/execd-overview.CBdepYh4.svg)


The reference platform provisions execd next to your entrypoint — as a staged binary in Docker, an init container in Kubernetes, or a baked-in part of a Fast Sandbox template image. Execd serves an HTTP API (default port `44772`); when access-token protection is enabled, clients forward the token supplied by endpoint resolution. The published [execd API spec](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/execd-api.yaml) describes the execution contract; some reference-implementation extensions, including PTY routes, are not yet covered by it.


Execd also fronts a small reverse proxy (`/proxy/{port}`), so one exposed host port can reach every port inside the sandbox — see [Single-Host Network (Docker)](https://open-sandbox.ai/architecture/network/single-host-network).


## Capabilities at a glance


| Capability | What you get |
| --- | --- |
| Command execution | Run any command with live streamed output; foreground or background with status polling and log retrieval |
| Code execution | Jupyter-backed code contexts and kernels — the foundation of the Code Interpreter SDKs |
| Interactive terminals | A real terminal (PTY) over WebSocket, shareable with read-only viewers |
| Files and directories | Upload, download, list, search, move, chmod, remove, in-place content replace — the sandbox filesystem is fully scriptable |
| Isolated sessions | Run a shell inside a private namespace for untrusted or exploratory work |
| Metrics | Sandbox CPU and memory as point-in-time snapshots or a live stream |


## API surface


Everything execd exposes lives under one API. When the platform configures an access token, every endpoint below requires it in the `X-EXECD-ACCESS-TOKEN` header — only liveness and readiness are always open. The contract lives in [specs/execd-api.yaml](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/execd-api.yaml).


![execd request pipeline](https://open-sandbox.ai/assets/execd-request-pipeline.Cdt62Tb1.svg)


| Area | Endpoints | Notes |
| --- | --- | --- |
| Health | `GET /ping`, `GET /ready` | Liveness and readiness; no token required |
| Commands | `/command` | Run foreground or background, interrupt, poll status, fetch logs |
| Shell sessions | `/session` | Persistent stateful shell across calls |
| Code | `/code`, `/code/contexts` | Contexts and Jupyter-backed execution |
| Terminals | `/pty` | PTY sessions with a WebSocket attach point |
| Files | `/files`, `/directories` | The whole filesystem surface |
| Isolated sessions | `/v1/isolated/*` | Private-namespace shells with their own file operations |
| Metrics | `/metrics`, `/metrics/watch` | Snapshot and live stream |
| Reverse proxy | `/proxy/{port}` | Reach any sandbox port through execd |


## Command execution


Commands can be submitted in two forms:


- **Shell syntax** — pipelines, redirection, environment expansion; what you would type at a prompt.
- **Direct argv** — a program plus literal arguments, no shell parsing. Safer when parts of the command come from untrusted input, and it preserves empty strings and special characters exactly.


Execution modes:


- **Foreground** returns the output as a live Server-Sent-Events stream while the command runs.
- **Background** returns immediately; you poll status and retrieve incremental logs. Completed background output stays retrievable for 24 hours, and running commands are never cleaned up.


Foreground `stdout` and `stderr` event text preserves the command's line endings (`\n`, `\r`, or `\r\n`). Concatenate event text for each stream to reconstruct its output; the last event may be an unterminated fragment.


Sessions use Bash when the image provides it and fall back to POSIX `sh` on minimal images — commands sent to a fallback session must be `sh` -compatible. Windows sandboxes are supported (environment names are case-insensitive; batch files require shell syntax).


## Code execution


Code contexts are persistent Jupyter kernels managed by execd. You execute code in a context and receive streamed results — standard output, execution results, and errors — across multiple calls that share state, exactly like a notebook.


The official [code-interpreter image](https://github.com/opensandbox-group/sandbox-images) ships Python, Java, Node.js, and Go runtimes with matching Jupyter kernels — see the [Code Interpreter example](https://open-sandbox.ai/examples/code-interpreter). Code execution is available through the plain sandbox SDKs and the raw API.


## Interactive terminals


Each terminal session is a real PTY served over WebSocket — not a wrapped command, so interactive programs (editors, REPLs, agent CLIs) behave normally.


![execd PTY model](https://open-sandbox.ai/assets/execd-pty.BCWtVkev.svg)


The sharing model is deliberate: exactly one **holder** owns the keyboard, and any number of **viewers** can watch. Viewers first replay what has already been printed, then follow live output — useful for supervision, debugging assistants, or letting a second person watch an agent work without giving it input.


## Files and directories


One API covers the whole filesystem tree: stream files in and out, list and search directories, inspect and change permissions, replace file contents, move and remove paths. The file APIs in every sandbox SDK are a thin wrapper over these endpoints.


### Filesystem execution identity


On Linux, a trusted backend can select the identity performing ordinary file operations by prefixing the file API path with `/v1/filesystem/{uid}/{gid}`. Both IDs are required decimal integers between 0 and 4294967294. For example, `GET /v1/filesystem/1001/1001/files/download?path=/workspace/session-b/result.txt` reads the file as UID 1001 with primary GID 1001. The same prefix supports all ordinary file and directory operations, including uploads, metadata, search, replacement, rename, deletion, and permission changes.


Each request runs in a separate worker process with the selected credentials. Supplementary groups come from the selected user's system account; an unknown numeric UID has no supplementary groups. Account or group lookup failures other than an unknown UID fail the request. The worker never inherits Execd's supplementary groups as a fallback. Execd must have permission to establish the requested credentials; failure does not retry the operation as Execd. Relative paths resolve from `/`, and `~` uses the selected account's home directory (or `/` for an unknown UID). Workers do not inherit Execd's environment.


Linux checks path traversal, parent directory access, file access, and metadata changes under that identity. Upload `owner`, `group`, and `mode` remain target metadata and cannot grant the worker additional privileges. Requests with different identities can run concurrently without changing Execd's credentials.


To share a sandbox between conversations, provision a separate user and workspace for each conversation, allow the desired read access, and reserve directory write access for the owner. Deletion and rename permissions depend on the parent directory, so read-only file modes alone are insufficient. Keep sandbox API credentials in the trusted backend that selects these identities. This feature does not provide a separate mount namespace or a tenant isolation boundary.


The existing `/files` and `/directories` routes retain their default identity. The identity-prefixed routes require Linux and a supporting Execd version. Older servers return an unsupported route instead of silently ignoring identity options; clients must not fall back to the unprefixed routes.


## Isolated sessions


An isolated session runs a shell inside a per-execution [bubblewrap](https://github.com/containers/bubblewrap) namespace — a private view of mounts and identity, created fresh for each session:


- Explicit bind mounts bring host paths in, read-only or read-write.
- Writes are confined to an allowlist, enforced against fully resolved paths, so a symlink cannot redirect a bind outside it.
- Session creation reports what the current environment supports, so callers can adapt instead of guessing.


See the [Isolation Sessions guide](https://open-sandbox.ai/guides/isolation-sessions) for the full workflow.


## Layered security


Execd applies defense in depth to everything a sandbox runs:


- **Sandbox boundary** — resource limits, identity, and the isolation runtime (runc container, gVisor, Kata, Firecracker microVM) are chosen at create time (see the [Secure Container guide](https://open-sandbox.ai/guides/secure-container)).
- **Hardening floor** — when the operator enables it, every user process is launched through a native launcher that drops capabilities, sets `no_new_privs`, installs a syscall denylist, and confines filesystem writes with Landlock.
- **Isolated sessions** — the per-execution namespace above, for work that needs its own boundary.
- **Optional eBPF audit** — records process exec, network connect, and privilege changes, scoped to the sandbox's own cgroup. Ships as a separate `execd-ebpf` build variant, not in the default image.


Each layer reports its state — active, degraded, or unsupported — so clients can verify what is actually enforced rather than assume. One boundary to keep in mind: execd's lifecycle hooks (setup commands the platform configures) run as trusted code inside the sandbox; they are convenience, not a security control.


## Supervision and exit codes


Execd can act as the sandbox's init process. It reaps orphaned children, forwards signals to your entrypoint, and propagates its exit code to the runtime — so sandbox states like `Terminated` and `Failed` reflect what your process actually did, and long-running sessions do not accumulate zombie processes.


## A fresh identity per allocation


Sandboxes can be pre-warmed in pools and reused across allocations. Execd makes this safe: the platform delivers a per-allocation binding — sandbox ID, environment, access token, lifecycle hooks — at assignment time, and execd applies it atomically before the API opens. While a warm sandbox waits for its binding (and until startup completes), every business endpoint answers `503`; only `GET /ping` and `GET /ready` respond. Environment variables, tokens, and telemetry attribution never leak between the sandbox that came before and yours.


![execd allocation binding flow](https://open-sandbox.ai/assets/execd-binding-flow.KMhVY7Uv.svg)


## Observability


Execd exposes local CPU and memory metrics as a snapshot and as a live stream, and exports OpenTelemetry metrics when the platform configures an endpoint — attributed to your sandbox ID and allocation. See [telemetry](https://open-sandbox.ai/guides/telemetry#execd) for the metric list and how export is configured.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/data-plane/execd.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/control-plane/operator`

Return to top

# Kubernetes Controller
## High-level design ​
## BatchSandbox ​
## Pool ​
## Task orchestration ​
## SandboxSnapshot ​
## Reading status ​
## Performance ​
## Installing ​










The controller is the Kubernetes operator behind container-backed sandboxes. It watches three custom resources and turns them into running sandboxes with pod-level scheduling, pre-warmed pools for constant-time delivery, optional task orchestration, and snapshot-based pause/resume. The lifecycle server creates and manages these resources on behalf of API clients, but the resources are ordinary Kubernetes objects — visible, auditable, and directly usable.


![Controller resource model](https://open-sandbox.ai/assets/operator-model.9kgWiKcz.svg)


## High-level design


The controller manager runs three reconcilers, one per custom resource. Each follows the standard Kubernetes pattern: watch the desired state, diff it against observed pods, and converge with idempotent operations.


![Controller reconcilers](https://open-sandbox.ai/assets/operator-reconcilers.By2VykQ5.svg)


- **BatchSandboxReconciler** — owns sandbox pods: scales them in direct (non-pooled) mode, parses pool allocations, schedules tasks, enforces `expireTime`, and drives the pause/resume handoff (`internal/controller/batchsandbox_controller.go`).
- **PoolReconciler** — owns pool pods and watches `BatchSandbox` objects: schedules warm pods to waiting sandboxes, scales the buffer, rolls out template updates, and processes evictions (`internal/controller/pool_controller.go`).
- **SandboxSnapshot reconciler** — turns a `SandboxSnapshot` into a commit `Job` on the source node and records the pushed image results (`internal/controller/sandboxsnapshot_controller.go`).


Two contracts connect the reconcilers without coupling them:


- **Allocation annotations.** The pool reconciler writes `sandbox.opensandbox.io/alloc-status` (allocated pods, `poolRef`, generation) and `alloc-release` on the `BatchSandbox`; the `endpoints` annotation carries resolved endpoints consumed server-side. Pods carry the `sandbox.opensandbox.io/pool-name` and `pool-revision` labels.
- **Task dispatch.** The batch reconciler runs an in-process `TaskScheduler` that assigns tasks to pods and calls the task-executor HTTP server running inside each sandbox pod.


## BatchSandbox


`BatchSandbox` is the workhorse: one or many identical sandboxes described declaratively.


| Spec field | Meaning |
| --- | --- |
| `replicas` | Number of sandboxes (default 1) |
| `template` | The pod template every replica starts from |
| `poolRef` | Allocate from a named `Pool` instead of scheduling fresh pods; mutually exclusive with `template` |
| `shardPatches` | Per-replica patches applied on top of `template` — one replica can differ in image, env, or resources |
| `taskTemplate` | Optional process each replica runs after allocation, executed by an in-pod task executor |
| `shardTaskPatches` | Per-replica variants of `taskTemplate` — heterogeneous tasks across one batch |
| `taskResourcePolicyWhenCompleted` | What happens to sandbox resources when its task reaches Succeeded/Failed: `Retain` (default) keeps them until deletion, `Release` frees them immediately |
| `expireTime` | Absolute expiration time at which the controller begins deletion |
| `pause` | Pause/resume intent: `true` pauses, `false` resumes. The controller never clears the field; it acks progress via `status.pauseObservedGeneration`, which also gates re-entry |


If `poolRef` is empty, the controller can still auto-select a pool using configurable profiles: predicate plugins (capacity, image, resource, node selector) filter candidates, then a scoring plugin (least-allocated by default) picks one (`internal/controller/poolassign/`).


Status separates sandbox health from task progress: `replicas` / `allocated` / `ready` and `phase` / `conditions` describe the runtime; `taskRunning` / `taskSucceed` / `taskFailed` / `taskPending` / `taskUnknown` counters plus `taskLastErrorMessage` describe tasks.


## Pool


`Pool` holds pre-warmed pods so that allocation becomes a claim on existing capacity instead of a scheduling round-trip.


| Spec field | Meaning |
| --- | --- |
| `template` | The pod template warm pods start from |
| `capacitySpec` | `bufferMin` / `bufferMax` govern the ready band; `poolMin` / `poolMax` bound the whole pool |
| `scaleStrategy` | `maxUnavailable` caps how fast the pool scales (absolute or percentage, default 25%) |
| `updateStrategy` | Same cap for rolling out template changes across existing pods |
| `recycleStrategy` | What happens when an allocated pod is released back: `Delete` (default), `Restart`, or `Noop` |


Status reports `total` / `allocated` / `available` / `updated` plus a `revision` identifying the current template version — a SHA-256 hash (first 8 bytes) of the template.


### Pool design


The pool maintains a **two-level capacity model**:


![Pool capacity model](https://open-sandbox.ai/assets/operator-pool-capacity.D0zjgANK.svg)


- **Buffer** — warm, unallocated pods that are Running and Ready. This is what allocations draw from, kept between `bufferMin` and `bufferMax`. The controller continuously reconciles toward this band: an allocation that drains the buffer triggers a scale-up; released capacity above `bufferMax` triggers a scale-down.
- **Total pool** — everything the pool owns, allocated or not, bounded by `poolMin` and `poolMax`. Pods that are still starting count toward the total but are never advertised as available buffer, so the pool never promises capacity it cannot hand out.


Scaling is deliberately paced: each reconcile creates or deletes at most `maxUnavailable` pods (minus the ones already not-ready), so a burst of allocations produces a measured ramp of new pods, not a thundering herd.


**Allocation and return.** Allocating is a constant-time claim on a warm pod: the pool reconciler schedules pods to waiting sandboxes, then persists the assignment via the allocation annotations. When the sandbox using a pod goes away, the pod returns to the pool and the `recycleStrategy` decides its fate:


- `Delete` (default) — the returned pod is replaced with a fresh one, so every allocation starts from the template's clean state.
- `Restart` — containers restart in place: cheaper than a full pod churn, still scrubbing process state.
- `Noop` — returned as-is: fastest, but filesystem and process state leak into the next allocation.


**Template updates.** Editing the pool template changes the revision; the controller deletes idle pods still on the old revision (never pods allocated to a sandbox) and replenishes at the new revision under `updateStrategy` caps, with `status.updated` tracking progress.


**Eviction.** Labeling an idle pool pod with `pool.opensandbox.io/evict` requests its removal. The controller protects pods already allocated to a `BatchSandbox`, deletes idle ones, and lets replenishment restore the buffer.


**Exhaustion.** When no eligible pool has a free slot, the controller sets the `PoolAllocationPending` condition (reason `PoolCapacityExhausted`) on the waiting `BatchSandbox` and rechecks every 5 seconds; the server waits up to a bounded window and surfaces a retryable `429` if capacity never frees up. A slot released during that window can still satisfy the request.


### Lifecycle-API constraints on pools


Because pool pods exist before any request, the lifecycle API cannot inject per-request state into them:


- `entrypoint` / `env` are delivered as a post-allocation task, not by rewriting the pod — seeing the original template in the pod spec is expected.
- `volumes` and `networkPolicy` cannot be combined with a pool reference; configure them in the pool template up front.
- Pool pods must satisfy the task contract (in-pod task executor, bootstrap entrypoint, execd installed) for lifecycle-API use.


## Task orchestration


Tasks are optional: a `BatchSandbox` without a `taskTemplate` is pure allocation. With one, each replica runs a defined process — uniform across the batch, or customized per sandbox through shard patches.


A process task can run **Local** (inside the task-executor container, the default) or **Remote** (inside the main container via `nsenter`), selected per task with `execMode`. Process tasks also support `preStart` and `postStop` lifecycle hooks: a failed or timed-out `preStart` prevents the main process from starting, and `postStop` runs on every terminal outcome, including deletion — suitable for staging inputs and persisting outputs to mounted volumes.


API deletion and TTL expiration finish task cleanup, including `postStop`, before deleting or recycling pods. Direct foreground deletion of the BatchSandbox, or deletion of its Pool or pods, can bypass this ordering.


## SandboxSnapshot


`SandboxSnapshot` is the checkpoint record behind pause/resume. Its spec is a single field — the target `BatchSandbox` name (same namespace); the controller resolves the pod and node. Registry, push credentials, and snapshot type come from controller startup flags, not the spec. Status carries the outcome: a `Pending → Committing → Succeed / Failed` phase, a `format` of `rootfs-v1` (default) or `qemu-v1`, per-container committed image URIs with immutable config digests, the source pod and node, and — for the QEMU contract — a separate VM-state image with payload digests and a restore-compatibility summary. See [QEMU VMState Snapshots](https://open-sandbox.ai/guides/qemu-vmstate-snapshots).


Pausing persists the rootfs, pushes it to the configured registry, and releases pods and pool slots; resuming recreates the workload from the snapshot image with the same sandbox ID. Pause/resume is limited to single-replica sandboxes (`spec.replicas=1`). During pause the controller manages an internal snapshot named after the sandbox; the commit runs as a job on the source node. Registry credentials, retention, and capacity planning are operator concerns — deleting a snapshot record does not delete the pushed images.


![Pause/resume phases](https://open-sandbox.ai/assets/operator-pause-phases.B2bffplR.svg)


Set `--snapshot-image-uri-template` (Helm: `controller.snapshot.imageURITemplate`) to customize snapshot image names before the initial push. An empty template preserves the default naming rule; see [custom image names](https://open-sandbox.ai/guides/pause-resume#custom-image-names) for the named fields and date/timezone formatting helpers.


## Reading status


The phase reports sandbox runtime health; the conditions explain it. Both are Kubernetes-native and inspectable with plain `kubectl`.


| Phase | Meaning |
| --- | --- |
| `Pending` | No running, ready sandbox pod observed yet |
| `Succeed` | At least one sandbox pod is running and ready — the steady state, **not** task completion |
| `Pausing` / `Paused` / `Resuming` | Pause/resume transitions |
| `Failed` | Terminal runtime failure — inspect conditions and pod events |


Conditions (`Ready`, `Progressing`, `Paused`, `PauseFailed`, `ResumeFailed`, `PodFailed`, `PoolAllocationPending`) carry reasons and messages; count a condition only when it exists with status `True`, and check `status.observedGeneration` against `metadata.generation` before trusting post-update status.


## Performance


With pooling enabled, measured delivery of 100 sandboxes:


| Scenario | Total time |
| --- | --- |
| SIG Agent-Sandbox (concurrency 1 / 10 / 50) | 76.4 s / 23.2 s / 33.9 s |
| BatchSandbox | 0.92 s |


## Installing


Install the CRDs and controller through the base and controller Helm charts (or Kustomize for development); the [Kubernetes Deployment](https://open-sandbox.ai/deployment/) page walks through the full stack, and the [controller source](https://github.com/opensandbox-group/OpenSandbox/tree/main/kubernetes) documents chart values and local builds.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/control-plane/operator.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples`

Return to top

# Examples
## Coding Agents ​
## Browser & Desktop ​
## Core Usage ​
## Storage ​
## How to Run ​







OpenSandbox provides ready-to-run examples covering SDK usage, agent integrations, browser automation, and training workloads.


TIP


All example source code is available in the [`examples/`](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples) directory on GitHub.


## Coding Agents


Run coding CLIs and AI agent frameworks inside isolated sandboxes.


| Example | Description |
| --- | --- |
| [Claude Code](https://open-sandbox.ai/examples/claude-code) | Run Claude Code CLI in a sandbox |
| [Gemini CLI](https://open-sandbox.ai/examples/gemini-cli) | Run Gemini CLI in a sandbox |
| [Codex CLI](https://open-sandbox.ai/examples/codex-cli) | Run OpenAI Codex CLI in a sandbox |
| [Apply Model Patches](https://open-sandbox.ai/examples/apply-patch) | Apply Codex-style file patches with a custom sandbox image |
| [OpenCode](https://open-sandbox.ai/examples/opencode) | Run the OpenCode coding agent in a sandbox |
| [Qwen Code](https://open-sandbox.ai/examples/qwen-code) | Run Qwen Code CLI in a sandbox |
| [Kimi CLI](https://open-sandbox.ai/examples/kimi-cli) | Run Kimi CLI (Moonshot AI) in a sandbox |
| [LangGraph](https://open-sandbox.ai/examples/langgraph) | LangGraph state-machine workflow with sandbox |
| [Deep Agents](https://open-sandbox.ai/examples/deep-agents) | Deep Agents file/shell tools running in a sandbox |
| [Google ADK](https://open-sandbox.ai/examples/google-adk) | Google ADK agent using OpenSandbox tools |
| [OpenClaw](https://open-sandbox.ai/examples/openclaw) | OpenClaw Gateway inside a sandbox |
| [DeerFlow](https://open-sandbox.ai/examples/deer-flow) | DeerFlow agent turns with tools running in a sandbox |


## Browser & Desktop


Execute browser workloads and host desktop environments in sandboxes.


| Example | Description |
| --- | --- |
| [Chrome](https://open-sandbox.ai/examples/chrome) | Chromium sandbox with VNC and DevTools |
| [Playwright](https://open-sandbox.ai/examples/playwright) | Playwright + Chromium headless testing |
| [Desktop](https://open-sandbox.ai/examples/desktop) | Full desktop environment with VNC |
| [VS Code](https://open-sandbox.ai/examples/vscode) | VS Code Web (code-server) in a sandbox |


## Core Usage


Fundamental sandbox operations and SDK workflows.


| Example | Description |
| --- | --- |
| [Code Interpreter](https://open-sandbox.ai/examples/code-interpreter) | End-to-end Code Interpreter SDK workflow |
| [Scheduled Client Pool](https://open-sandbox.ai/examples/client-pool-schedule) | Adjust idle capacity by business hours using Go's pool Resize API |
| [AIO Sandbox](https://open-sandbox.ai/examples/aio-sandbox) | All-in-One sandbox setup |
| [Agent Sandbox](https://open-sandbox.ai/examples/agent-sandbox) | Kubernetes agent-sandbox integration |
| [AKS + Kata](https://open-sandbox.ai/examples/aks-kata) | AKS deployment with Kata VM isolation, ingress, egress, and Credential Vault |
| [Windows](https://open-sandbox.ai/examples/windows) | Windows sandbox via KVM/QEMU |
| [Harbor Evaluation](https://open-sandbox.ai/examples/harbor-evaluation) | Run a Harbor agent evaluation, one sandbox per trial |


## Storage


Persistent and shared storage patterns for sandboxes.


| Example | Description |
| --- | --- |
| [Host Volume Mount](https://open-sandbox.ai/examples/host-volume-mount) | Mount host directories into sandboxes |
| [Docker PVC Volume](https://open-sandbox.ai/examples/docker-pvc-volume-mount) | Docker named volume mounts |
| [Docker OSSFS Volume](https://open-sandbox.ai/examples/docker-ossfs-volume-mount) | Docker OSSFS (OSS FUSE) mounts |
| [rclone Volume Mount](https://open-sandbox.ai/examples/rclone-volume-mount) | Remote storage through external Docker plugins or Kubernetes CSI volumes |
| [Kubernetes PVC](https://open-sandbox.ai/examples/kubernetes-pvc-volume-mount) | Kubernetes PersistentVolumeClaim mounts |


## How to Run


1. Start the OpenSandbox server (see [Quick Start](https://open-sandbox.ai/getting-started/))
2. Set environment variables: `export SANDBOX_DOMAIN=...`, `export SANDBOX_API_KEY=...`
3. Add provider-specific variables as needed (e.g., `ANTHROPIC_AUTH_TOKEN`, `OPENAI_API_KEY`)
4. Navigate to the example directory and run: `python main.py`


TIP


Most examples include a `main.py` entry point. Follow each example's run instructions for other languages. Some also include a `Dockerfile` for containerized execution.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/data-plane/node-agent`

Return to top

# Node Agent


Sandboxes are ephemeral by design: when a sandbox is deleted, everything it printed to stdout and stderr disappears with it. **Node Agent** is an optional DaemonSet that fixes this — one collector per Linux node watches every sandbox pod on that node and ships their output to durable storage, so records outlive the sandbox that produced them. Collection is entirely node-side and invisible to the workload.


![Node Agent data path](https://open-sandbox.ai/assets/node-agent-data-path.D1vPaBwb.svg)
## Capabilities at a glance ​
## How collection works ​
## Sources ​
## Where records land ​
## Delivery guarantees ​
## Safety model ​
## Observability ​
## Enabling it ​










Experimental capacity


Collection and delivery are implemented, but production resource defaults still await benchmark and soak results ([OSEP-0019](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0019-node-agent-sandbox-collection.md)). Treat the chart's resource values as starting points.


## Capabilities at a glance


| Capability | What you get |
| --- | --- |
| Log collection | stdout/stderr of every sandbox pod on the node (pooled warm pods are excluded — they are not allocations) |
| Syscall observation | An optional kernel-level source recording each syscall a sandbox makes, via an embedded eBPF program |
| Durable targets | Alibaba Cloud OSS or durable local files — one target per Agent; a best-effort stdout mode exists for debugging |
| Delivery | At-least-once, crash-recovering, with explicit completeness markers per stream |
| Organization | Records laid out per cluster / namespace / sandbox / pod, ready for downstream consumption |
| Safety | Backpressure instead of silent drops; refuses unsafe bucket configurations |
| Observability | Liveness vs readiness split; metrics free of sensitive labels |


## How collection works


The Agent is a pipeline: **sources** produce records, bounded per-sandbox queues carry them, and one **sink** writes them out. Three design choices shape the whole system:


- **Sources and sinks are compile-time registries, not plugins.** A build embeds the sources it supports; configuration selects among them, and an unknown name leaves the Agent unready rather than starting a partial pipeline. No code is loaded at runtime.
- **Queues are bounded, and the drop policy is explicit.** The default `block` policy applies backpressure to the source when a sink slows down — collection slows, nothing is lost. The alternative `drop` policy bounds memory harder and accounts for whatever it discards in the stream's completeness marker. A global memory budget, a per-sandbox queue budget, and an optional per-sandbox rate limit keep one noisy sandbox from starving the node.
- **Fail closed, never crash-loop.** Invalid configuration, damaged or mismatched recovery state, or an unusable target keeps the process alive but not ready, reporting a named reason. It never silently resets and re-collects, and it never advances progress onto an unverified destination.


Pod selection is identity-based, not label-guesswork: a pod is collected when it carries sandbox identity (the sandbox ID label, the sandbox container, its restart count) and is **not** allocated from a pool (pods labeled with their pool are warm capacity, not sandboxes).


## Sources


**`container-logs`** (default) tails the kubelet's log files for sandbox pods on the node and streams each container stream as `container-log` records. An inotify hot path backed by low-frequency reconciliation follows rotation, compression, and file reuse; partial CRI lines are reassembled before delivery. Log files are identified by fingerprint, so a reclaimed or replaced file becomes an accounted gap instead of silently spliced data. A stream is finalized only after its pod has terminated and its reads have stayed at end-of-file.


**`syscalls`** records what sandboxes actually do at the kernel level: an embedded eBPF program is attached to each sandbox pod's cgroup and emits one record per syscall — syscall number, host PID/TID, command name, timestamps — as `syscall` records. Kernel ring-buffer overflows, agent-restart intervals, and late attachment are all tracked per stream and reflected in the markers, and container restarts rebind the tracer behind a drain barrier so events cannot be misattributed across generations. This source is Linux-only (kernel 5.11+, cgroup v2) and requires BPF and PERFMON capabilities.


Each source owns its record kind and storage format; both feed the same marker and recovery machinery.


## Where records land


Each stream becomes an object family under a layout that mirrors cluster reality. Every record kind has its own family (`container-log`, `syscall`), each with its own encoding and marker set:

text

```
<cluster>/<namespace>/<sandbox_id>/<pod_uid>/
  sandbox.log
  sandbox.<generation>.log
  sandbox.finalized.<revision>.json
```


Non-log record kinds are isolated in a separate `<cluster>/_streams/<kind>/…` tree under the same rules.


The `finalized` marker is the stream's closing statement — a cumulative, immutable snapshot listing every closed object with its size and checksum, which consumers verify. It answers the only question that matters after an incident: **can I trust these logs?**


| Marker status | Meaning |
| --- | --- |
| `complete` | No intentional drop or known gap. At-least-once delivery may still contain duplicates. |
| `complete-with-drops` | At least one record was intentionally dropped, with the affected interval accounted for. |
| `incomplete` | At least one known interval could not be read, or its coverage cannot be proved. |


The honesty is deliberate. If the Agent restarts while a stream is open, the recovered data is still delivered — but the next marker is `incomplete`, because nothing can prove that a short-lived rotation didn't vanish during the outage. Consumers get truth, not optimism.


## Delivery guarantees


- **At-least-once, never silent loss**: a record's cursor advances only after the sink has durably accepted it and the source has acknowledged it; finalization itself is a two-phase, crash-recoverable transaction. Duplicates are possible; unaccounted loss is not. Anything questionable shows up in the marker.
- **Strict per-stream ordering**: a stream has at most one in-flight batch and one finalizing revision at a time — the next revision starts only after the previous marker is durable.
- **State bound to the destination**: local recovery state is keyed to a digest of the configured target. A damaged or mismatched state makes the Agent unready — it never silently resets and re-collects from scratch.
- **Bounded footprint**: local files rotate under size, count, and total-volume caps; retention-driven cleanup is crash-resumable — it moves a finished family into a staging area and removes it only after the move is durable, and it never deletes one generation to make room for another.
- **Retention is the operator's job**: the Agent collects; it does not make retention policy. OSS deletion always happens through a separate offline cleanup tool that requires explicit delete credentials — collection credentials never have them. The stdout debug mode is best-effort: it publishes no markers and makes no durability claim.


## Safety model


- **Least-privilege credentials**: OSS collection credentials need append, read, and write permissions — never delete.
- **Refuses unsafe targets**: bucket versioning or WORM, or an overlapping lifecycle rule, is a permanent startup error — configurations that would break the Agent's integrity assumptions are rejected, not worked around.
- **Host reserves are validated at startup**: file-descriptor and inotify limits, disk headroom for state and output, and the queue budget against the cgroup memory limit are checked before collection begins — problems Helm's resource schema cannot express fail startup instead of failing collection later.
- **Readiness means trustworthy**: `/readyz` aggregates a set of named, low-cardinality reasons (invalid config, target unreachable, retry loop active, …) and passes only when none apply. A not-ready Agent is visible and diagnosable, not silently dropping data.


## Observability


Liveness (`/healthz`) and readiness (`/readyz`) are deliberately separate: the process can be alive while collection is blocked, and readiness surfaces why using low-cardinality reason codes — never credentials, paths, or bucket names. When an OTLP endpoint is configured, the Agent reports record and byte counts, intentional drops, retries, and queue depth, with no sandbox or pod identifiers as labels.


## Enabling it


Node Agent ships in the `node-agent` Helm chart and is disabled by default in the umbrella chart. See the [node-agent chart](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts/node-agent) for values — target type, OSS credentials, retention, and cluster ID — and the [component source](https://github.com/opensandbox-group/OpenSandbox/tree/main/components/nodeagent) for implementation details.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/data-plane/node-agent.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/network/ingress`

Return to top

# Ingress
## How a request reaches a sandbox ​
## Error semantics ​
## WebSocket support ​
## Fronting ingress with TLS ​
## Health and network readiness ​
## Extending sandbox expiration on access ​
## Fast Sandbox routes ​









The ingress gateway is the front door for sandbox traffic on Kubernetes: one reverse proxy standing in front of every sandbox, with no per-sandbox configuration. It watches the state workloads already publish — endpoint annotations, service FQDNs, or the FastPath control plane — and resolves each incoming request against a live cache.


![Ingress routing](https://open-sandbox.ai/assets/ingress-routing.DV3m-2Hn.svg)


## How a request reaches a sandbox


The route to a sandbox is a pair of sandbox ID and port, discovered in one of two modes:


- **Header mode** (default): the `OpenSandbox-Ingress-To` header carries `<sandbox-id>-<port>`, or the host label encodes the same pair (`my-sandbox-8080.example.com`). The pre-rename legacy header is still accepted.
- **URI mode**: the first two path segments carry the pair — `/<sandbox-id>/<port>/<path>` — so clients that cannot set headers still work.


With [secure access](https://open-sandbox.ai/guides/secure-access), the route can instead be a signed route token: sandbox ID, port, expiry, and MAC in one label, verifiable without a lookup.


Resolution reads the endpoint from the workload that owns the sandbox — BatchSandbox endpoint annotations, agent-sandbox service FQDNs, or FastPath for Fast Sandbox routes. Before forwarding, the ingress strips the routing headers, adds `X-Forwarded-*`, filters hop-by-hop headers, and preserves the request path and query exactly.


## Error semantics


When routing cannot proceed, the failure is precise — clients can branch on status codes:


| Status | Meaning |
| --- | --- |
| `404` | No such sandbox (or no longer exists) |
| `503` | Sandbox exists but is not ready — no reachable endpoint yet |
| `502` | Infrastructure-level failure (cluster API errors and the like) |


Once a sandbox is reached, its responses pass through **verbatim**, including redirects and errors. The ingress never follows a redirect itself, so a stale `Location` can never leak credentials to an unrelated endpoint.


## WebSocket support


WebSocket is a first-class path, not an upgrade hack bolted onto HTTP proxying:


- Upgrades follow RFC 6455 over HTTP/1.1, with a 45-second backend handshake budget.
- Client-selected subprotocols and backend `Set-Cookie` headers cross the handshake.
- Application close codes are propagated as-is — a policy violation (`1008`) or app code (`4001+`) is never rewritten to `1000`.
- Single messages up to 64 MiB work in either direction, sized for terminal and Jupyter traffic.
- `Connection` header tokens are matched case-insensitively, and both directions stream without buffering the peer.


## Fronting ingress with TLS


The ingress speaks cleartext HTTP/1.1 and never terminates TLS. Put an L7 proxy in front of it — but mind the WebSocket constraint:


![Ingress behind TLS](https://open-sandbox.ai/assets/ingress-tls-l7.B28OXJ3u.svg)


WebSocket-over-HTTP/2 (RFC 8441) is **not** accepted, and RFC 7540 forbids the `Upgrade` headers on plain h2 requests. The front proxy must therefore deliver WebSocket upgrades as classic HTTP/1.1. In order of preference:


1. Remove `h2` from the browser-facing ALPN list — portable, verified fallback.
2. Per-WebSocket HTTP/1.1 fallback, if the proxy supports it while keeping h2 for other traffic.
3. RFC 8441 → RFC 6455 translation — proxy-specific; verify with a real browser before trusting it.


Never forward HTTP/2 to the ingress itself: the upgrade never reaches the WebSocket handler and the plain proxy path cannot complete the handshake either.


## Health and network readiness


- `/status.ok` — liveness: the process is up and serving.
- `/status.ok/network-readiness` — a **shadow** signal, for operators watching node-to-sandbox network health. It classifies the TCP connections the ingress opens (success, timeout, unreachable, refused, …) over a recent window and reports `DEGRADED` when timeouts and unreachables dominate across enough distinct targets.


The shadow endpoint always answers `200` with `OK` or `DEGRADED` and never gates traffic — it is a decision input for operators, not a load-balancer hook. Window length and thresholds are tunable; targets and sandbox IDs are deliberately absent from its metrics.


## Extending sandbox expiration on access


When enabled, the ingress publishes a **renew-intent** event for each proxied request (after the sandbox resolves), and the lifecycle server extends the expiration of sandboxes that opted in at creation. Publishing is throttled per sandbox and delivery is best-effort — an idle sandbox still expires; a busy one stays alive without client changes.


### Per-request opt-out


A single request can opt out of renew-intent publishing with a control header:

text

```
OpenSandbox-Access-Renew: skip
```


- Honored by both proxy paths — the ingress gateway and the server's `/sandboxes/{id}/proxy/{port}/...` route — so behavior does not depend on which path serves the traffic.
- The exact sentinel value `skip` suppresses the intent for that one request (it bypasses the per-sandbox throttle entirely); unknown values are ignored for forward compatibility.
- The header is stripped before forwarding upstream, like `OpenSandbox-Ingress-To`, so backend applications never observe it.
- Typical use: health probes and other background traffic hitting an opted-in sandbox without extending its lifetime.


WebSocket upgrades carry the header on the handshake request; long-lived connections do not produce per-request intents anyway.


## Fast Sandbox routes


The `FastSandboxProvider` serves authenticated `f1.` route scopes by resolving endpoints through FastPath v2 and forwarding traffic to Fastlet pods. It can run standalone or share one ingress process with the legacy Kubernetes providers; route-scope verification uses the same signing key ring as the server. See [Fast Sandbox: Networking](https://open-sandbox.ai/architecture/fast-sandbox/networking).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/network/ingress.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/network/egress`

Return to top

# Egress


Egress is how a sandbox gets a network policy instead of open internet access. It runs as a sidecar sharing the sandbox's network namespace, so every outbound packet passes it — no application configuration, and no way around it from inside. Policy is declared at create time (`networkPolicy`) or by the platform, and enforced continuously.


![Egress control flow](https://open-sandbox.ai/assets/egress-control-flow.HulHIsJC.svg)


## Capabilities at a glance


| Capability | What you get |
| --- | --- |
| FQDN rules | Allow or deny by domain, wildcard (`*.pypi.org`), IP, or CIDR — optionally scoped to TCP destination ports |
| DNS filtering (default) | Denied domains fail resolution; allowed ones resolve normally |
| Network enforcement (`dns+nft`) | Strict default-deny at the packet layer, fed by DNS-resolved addresses with bounded leases |
| Platform overlays | Operator-set `deny.always` / `allow.always` floors that user policy cannot override, plus a TCP port floor (`reachable.ports.cap`) that caps which ports are reachable at all |
| Credential Vault | Secrets stay in the sidecar; credentials are injected into matching outbound requests |
| Transparent TLS interception (L7) | See, control, and authenticate outbound HTTPS — production-usable mechanism, experimental configuration surface |
| Fail-closed startup | If enforcement cannot be installed, the sidecar exits — it never runs as a no-op |


## How interception works


- **Layer 1 — DNS.** All port-53 traffic is redirected into the sidecar's DNS proxy. Denied domains answer `NXDOMAIN`; allowed domains resolve through to the real upstream, and their resolved addresses are recorded.
- **Layer 2 — Network (`dns+nft` mode).** nftables drops everything not explicitly allowed. Allowed traffic passes by static rule or via DNS-learned address sets: a resolved IP receives a bounded lease (with a grace window for active TCP connections), so "allowed" never silently becomes "allowed forever". UDP and QUIC flows rely on DNS lease timing alone.
- **Precedence.** First matching rule wins: platform `deny.always`, then platform `allow.always`, then your policy — the platform's deny always beats your allow. Overlays live inside the sidecar image and hot-reload every minute; a reload publishes only after nftables accepts the corresponding static policy. Parse or apply failures keep the last accepted in-memory rules and stay eligible for retry.
- **Runtime mutation.** Your policy is set per sandbox and can be mutated at runtime (add, replace, remove by target) through the API the SDKs expose.


**Port floor.** Operators can also ship an `reachable.ports.cap` file next to the overlays: a whitelist of TCP ports (one port or `lo-hi` range per line) that are reachable **at all**. The sidecar derives the complement and enforces it as an always-deny ahead of every user rule — so regardless of what a sandbox's `defaultAction` or allow rules say, only the whitelisted ports pass (TCP only; the same fail-closed ordering that makes a deny rule win over any allow). A missing or empty file means no floor. Under transparent MITM, intercepted ports are governed by the interception config, so keep intercepted ports within the whitelist. Note established connections persist until their lease expires, as with any policy change.


### Port-scoped rules


A rule's `target` may be omitted when `ports` is set, so a rule can scope by TCP destination port alone — `{"action": "deny", "ports": [25]}` blocks outbound SMTP regardless of destination. `target` and `ports` can also combine to scope an IP or CIDR rule to specific ports. Ports are enforced at the network layer (`dns+nft` mode) as `tcp dport` matches, and a deny rule — port-scoped or not — always wins over an allow rule.


**DNS limitation for targetless allows.** The DNS proxy only resolves hostnames matched by a domain rule; a targetless `allow` with `ports` is invisible to it. Under `defaultAction: deny`, hostname lookups therefore still fail (`NXDOMAIN`) and such a rule serves clients that dial IPs directly. Hostname access needs explicit domain allow rules — which are not port-scoped — or destinations addressed by stable IP.


Current limits: TCP only (no UDP); at most 256 ports per rule; domain targets cannot combine with `ports` (domain rules are evaluated at the DNS layer, which has no port dimension) and are rejected at validation; `DELETE /policy` removes rules by `target` — port-only rules have none, so `DELETE` with an explicit empty string (`""`) in the target list removes them all, or a full `POST` / `PUT` replaces the policy. The Fast Sandbox profile rejects `ports` with a 400 until its enforcement path supports them. Independently of user rules, operators can cap reachable ports platform-wide with the `reachable.ports.cap` floor (see [Precedence](https://open-sandbox.ai/architecture/network/egress#precedence)). One boundary to keep in mind: under transparent MITM, intercepted ports are redirected into the sidecar before the nft policy chain sees them, so port-scoped rules and the cap govern only non-intercepted traffic — keep the interception port list within the cap.


## Design decisions


| Decision | Rationale |
| --- | --- |
| Enforcement lives in the data path | The sidecar installs redirect rules in the shared namespace; the workload holds no `NET_ADMIN`, so there is nothing to bypass and no application cooperation required. |
| Two layers, two costs | DNS filtering alone is cheap and universal but only gates names. `dns+nft` adds packet-level default-deny with DNS-learned, leased exceptions. |
| Encrypted DNS is an escape hatch | DoT (853) is always dropped, and blocking DoH over 443 is a one-switch option. |
| Fail-closed over best-effort | If redirect rules cannot be installed, the sidecar exits instead of running as silent pass-through; a supervisor restarts it with backoff and a crash-loop breaker. |
| Portable by fallback, honest about limits | Redirects install via iptables where available and fall back to native nftables (Firecracker-style guest kernels). gVisor's netstack cannot support this — Kata is the supported secure runtime — and transparent mesh sidecars conflict by construction. |


## Transparent TLS interception (L7)


Layers 1 and 2 decide *whether* a connection may happen; the transparent MITM layer adds control and visibility over *what goes through it*. When enabled, outbound HTTP and HTTPS is redirected into a mitmproxy listener inside the sidecar, which recovers the true destination from connection state and terminates TLS on the sandbox's behalf.


**Status: experimental but production-usable.** Interception, credential injection, and CA delivery are complete and run in production settings; the configuration surface — extra ports and diagnostic switches — may still change between releases.
## Capabilities at a glance ​
## How interception works ​
## Design decisions ​
## Transparent TLS interception (L7) ​
## Credentials without secrets in the sandbox ​
## Where it runs ​
## Service Mesh Compatibility ​
## Shutdown ​
## Observability (OpenTelemetry) ​











Internal OSEP-0023 revision runtime


`OPENSANDBOX_EGRESS_EXPERIMENTAL_REVISION_RUNTIME=true` is a development-only sidecar gate (default off) for the OSEP-0023 revision protocol. It adds no public configuration surface or supported `interceptionMode`, and does not enable Fast Sandbox.


The internal sidecar experiment covers bound HTTPS/443 HTTP/1.1 traffic and experimental HTTP/2 admission and bounded-drain wiring on the fixed-dependency direct/lazy path. Configured chained upstream proxies remain rejected for live HTTP/2. Long-held responses can still cause Go retries to time out; full client migration and Linux acceptance remain follow-up work. Key properties:


- Admission is per connection and per request, from an immutable snapshot installed over an authenticated channel; unknown or mismatched state denies — the mode never falls back to decrypt-all.
- Any uncertain outcome (unconfirmed mutation, session cleanup failure, unexpected child exit) latches a sticky recovery-required state: readiness drops, nft writes quiesce, and an independent quarantine table is installed for the process lifetime. Restarting the sidecar is not a verified recovery — destroy and recreate the sandbox instead.
- Updates are not one atomic visibility boundary: nft rules can affect traffic before receiver acknowledgement, and a committed update is not rolled back if the API response is lost. Retired connections drain within a bounded window (default 30 seconds).


Full contract, including the egress-owned policy-file storage requirements when `OPENSANDBOX_EGRESS_POLICY_FILE` is set: [credential vault guide](https://open-sandbox.ai/guides/credential-vault#experimental-live-credential-bound-admission-osep-0023), [OSEP-0023](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0023-credential-bound-tls-interception.md), and the [HTTP/2 integration boundary](https://open-sandbox.ai/architecture/network/osep-0023-h2-integration).


**Trust is delivered, not disabled.** The sidecar exports its CA, and sandbox bootstrap installs it into the system, NSS, and JDK trust stores on a best-effort basis — clients keep certificate verification on (`curl` without `-k`). Chromium-family images should ship the native `certutil` package so the per-user NSS store can be updated.


What it enables:


- **Credential Vault** — injection happens when request headers are read, so it applies regardless of body size, including fully streamed uploads.
- **TLS-level observability** — optional request-level outcome metrics (decrypt / passthrough) for targeted diagnostic windows.


**Extendable at L7.** The bundled system addon always loads first, then any comma-separated mitmproxy addons in `OPENSANDBOX_EGRESS_MITMPROXY_SCRIPT`, in order. Addons are standard mitmproxy scripts with the full L7 hook surface (hostname, method, URI path, headers, bodies), so operators can add hostname/method/header filtering, header injection, or request rewriting as ordinary Python addons — on top of, never ahead of, the built-in behavior.


**Chained upstream proxy.** Set `OPENSANDBOX_EGRESS_UPSTREAM_PROXY` to `http(s)://host[:port]` — optionally with `OPENSANDBOX_EGRESS_UPSTREAM_PROXY_AUTH` (a complete `Proxy-Authorization` value) — to chain all mitmproxy-handled egress through that proxy via `CONNECT`:


- The endpoint accepts only `host[:port]` or a single `/` path, and the host must be a literal IP or dotted domain (a dotless name resolves differently through the pod resolver's search list, so containment sets could miss the dialed address). Credentials, query, fragment, and other paths are rejected.
- Fail-closed: flows that cannot be chained (no SNI, `ignore_hosts`/`tcp_hosts`/`udp_hosts` matches, UDP) are refused rather than sent direct. Chaining requires transparent MITM, plus `dns+nft` outside the fast-sandbox profile; invalid combinations fail startup.
- Under `dns+nft`, the proxy endpoint is reachable only from the mitmproxy process (UID-, IP-, and port-scoped nft rules), never through the sandbox allow sets. Literal proxy IPs are permanently seeded in those sets; DNS-learned ones use bounded TTLs.
- Fast-sandbox profile: the endpoint is dropped profile-wide ahead of per-subject rules, and its hostname is registered as an infrastructure domain. The shared mitmproxy queries the pod resolver and its forward upstreams concurrently and seeds permanent drop sets with the union; startup fails (previous kernel table intact) unless both succeed with a nonempty union.
- Configuration: the server's `[egress.upstream_proxy]` section on Docker and Kubernetes — see [server configuration](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md#egress) and [Chained Upstream Proxy Operations](https://open-sandbox.ai/guides/egress-upstream-proxy). The same section can deliver an extra CA bundle (a Docker host PEM path or a Kubernetes Secret mounted read-only into the egress sidecar only) that mitmproxy trusts in addition to — never instead of — the system roots.


**Scope notes:**


- Ports 80 and 443 are always intercepted; a bounded list of extra ports can be added. Vault binding matching currently fires on 80/443 only — extra ports are decrypted and logged but not credentialed.
- IPv6 destinations are intercepted alongside IPv4 (listeners and redirect rules cover both address families).
- A not-yet-initialized proxy is visible in health: the sidecar answers `503 mitmproxy not ready` rather than passing traffic unexamined.
- An SSE body larger than ~1 MB can be truncated when the origin closes the connection with a TCP RST mid-body — standard TCP semantics, not an interception bug. See [Egress SSE Truncation](https://open-sandbox.ai/guides/egress-sse-truncation).


## Credentials without secrets in the sandbox


With transparent TLS interception enabled, the sidecar can inject credentials into outbound requests that match a vault binding — bearer tokens, basic auth, API keys, or custom headers. The vault lives in the sidecar's memory only: the sandbox workload sees authenticated traffic but never holds the secret itself. See [Credential Vault](https://open-sandbox.ai/guides/credential-vault).


## Where it runs


| Deployment | Shape |
| --- | --- |
| Docker | A separate sidecar container; the sandbox joins the sidecar's network namespace |
| Kubernetes | The sidecar is appended to the sandbox pod and holds the pod's only `NET_ADMIN` |
| Pooled sandboxes | Pre-warmed pods cannot gain a sidecar per request — put required controls in the Pool template (per-request `networkPolicy` + pool references are rejected) |
| Fast Sandbox | A shared egress process per Fastlet pod, one subject per sandbox — see [Fast Sandbox: Networking](https://open-sandbox.ai/architecture/fast-sandbox/networking) |


## Service Mesh Compatibility


Not supported with transparent mesh sidecars


Egress is designed to be the only transparent outbound interception layer in the sandbox's network namespace. Deployments that inject a service-mesh sidecar (Istio/Envoy and similar) into the same pod are not currently supported for egress features.


Both layers rewrite outbound traffic in the same namespace, so per-sandbox policy, transparent MITM, and Credential Vault cannot be relied on alongside mesh injection. Prefer excluding sandbox pods from mesh injection, or enforce outbound policy with a CNI-level mechanism. The same constraint applies to gVisor — use Kata, which provides comparable isolation and full egress support (see the [compatibility matrix](https://open-sandbox.ai/guides/secure-container#compatibility-matrix)).


## Shutdown


On shutdown, the sidecar keeps DNS and network rules working while in-flight deliveries finish (a bounded window), then removes its network rules and flushes telemetry in the legacy path; the experimental containment owner retains ordinary rules instead. Delivery is best effort — forced termination can drop events. Docker gives the sidecar a 9-second stop budget on deletion. A supervisor restarts crashes with exponential backoff, a crash-loop breaker, and stale-redirect cleanup before a fresh start.


## Observability (OpenTelemetry)


When the platform configures an OTLP endpoint, the sidecar exports per-sandbox metrics: denied request counts, DNS query outcomes (denied-by-policy and resolver-failure are deliberately separate counters — alerting on the wrong one inverts the diagnosis), nftables update failures, and process resource usage. Cardinality is bounded: no queried domain or destination ever becomes a label. See [telemetry](https://open-sandbox.ai/guides/telemetry#egress-sidecar) for the metric list and export configuration.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/network/egress.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/network/osep-0023-h2-integration`

Return to top

# Experimental HTTP/2 admission and drain
## Compatibility boundary ​
## Admission and identity ​
## Retirement and drain ​
## Failure containment ​
## Verification boundaries ​







Experimental implementation


This is an internal, default-off extension of the [OSEP-0023 revision runtime](https://open-sandbox.ai/architecture/network/egress#transparent-tls-interception-l7). Client-migration acceptance and the full runtime verification matrix remain incomplete. It adds no supported public configuration surface or Fast Sandbox support. HTTP/3, CONNECT and cross-SNI coalescing are outside its scope.


## Compatibility boundary


The adapter supports CPython 3.10 and 3.11 with the shipped direct/lazy connection strategy and exactly `mitmproxy==11.0.2`, `h2==4.1.0` and `hyperframe==6.0.1`. The image pins these dependencies and runs the adapter's version check during its build; missing or mismatched versions fail closed at runtime. Changing the pins requires compatibility verification of the adapter, rather than widening the gate alone. Other interpreters and Python versions, including Python 3.12 and later, are rejected before H2 adapter installation and request admission. The TLS slot, already acquired before ALPN selection, is reclaimed by normal disconnect. Their task scheduling and transport-registration ordering are not covered by this compatibility boundary. Configured chained upstream proxies are rejected for this H2 path because their tunnel and transport ownership is not covered. Existing H1 and legacy behavior is unchanged. Genuine untracked, non-TLS cleartext HTTP/2 remains outside credential admission; rewriting the visible scheme of tracked or decrypted HTTP/2 does not bypass raw-identity validation.


## Admission and identity


The existing `LiveReceiver` → `RevisionPublisher` → registry/receiver path remains the only publication owner, with Registry → Receiver lock order and unchanged authenticated IPC.


A request is admitted when the system `requestheaders` hook obtains its unique handle and immutable snapshot, not when HEADERS are parsed. The registry records the actual inbound client stream ID and a monotonic connection high-water mark. The first host removal freezes that bound, including zero if nothing was admitted. Finished streams, repeated publication and remove/re-add cannot reopen or raise it.


Before credential injection, the adapter validates the original pseudo-headers: HTTPS, one ASCII authority on port 443, actual destination port 443, an optional consistent single Host, and agreement with connection/token SNI. Rewritten scheme or host cannot substitute for original identity. Missing, malformed or unassociated identity fails closed.


## Retirement and drain


1. Before mutation acknowledgement, publication atomically installs the snapshot, new-request fence, frozen stream bound and first retirement deadlines. Acknowledgement does not wait for drain.
2. Valid requests refused at `requestheaders` receive REFUSED_STREAM and do not reach the origin. Previously admitted requests retain their own snapshots.
3. Once old requests and their local downstream/upstream output obligations are terminal, ordinary h2 APIs send one NO_ERROR GOAWAY with the frozen bound, followed by close.
4. Deadline expiry force-closes the whole connection and can interrupt other streams after rotation of a still-covered host. This is abnormal closure, not graceful completion.


Maintenance polling uses the exact connection handler's registered wakeup task. No-op housekeeping is filtered before dependency event dispatch, so it does not continually refresh the network inactivity watchdog. Actionable drain and cleanup work still runs without requiring new client traffic. The integration does not replace dependency classes or globally patch task scheduling.


Response/error hooks alone do not release a handle: DATA, trailers, queued upstream requests and unfinished uploads remain obligations. The adapter observes actual upstream children and client/upstream stream mappings without rewriting their queues or forcing H1 upstreams. Reset-stranded trailers wait only for an existing first deadline, or close abnormally if none exists. An early response followed by reset during an unfinished upload can orphan upstream work; the client and verified owned upstreams then close immediately.


Only the marked kill/NO_RESPONSE path represents normal refusal. Pre-hook 400/413 responses, parser errors and missing identity must not become retryable refusals. Pending identity storage is bounded by the request budget. Exhausting that association budget closes the connection abnormally; ordinary registry capacity denial uses the `requestheaders` refusal path.


### Client retry limitation


Delayed GOAWAY does not guarantee migration while an old response is unfinished. In the recorded Go 1.27.2 `net/http` synthetic GET configuration, retries after REFUSED_STREAM repeatedly selected the same connection and exhausted an eight-second deadline without reaching the origin. The held-old acceptance case remains **FAIL**.


A separate bounded-old case passed only when the harness released the old response early. The new GET completed once on a fresh connection with **HTTP/1.1 200**, while the old HTTP/2 response completed intact. This does not prove H2-to-H2 migration, migration while old remains unfinished, or success for arbitrary finite response durations. Go-peer frames were not captured, so GOAWAY causality and wire ordering remain unproven. Neither outcome should be generalized to other client versions or configurations.


The proxy does not replay requests or change error codes to influence client pooling. The narrower passing case does not replace the failed acceptance gate.


## Failure containment


Client disconnect fences admission immediately, but cleanup retains exact ownership until related upstreams are verified terminal. A disconnected hook, a CLOSED flag or an exit code alone does not establish transport closure. Cleanup observes actual task/IO identities and writer-close confirmation; callbacks must remain effective through canceled wakeups while handler registration remains valid.


There are two distinct fatal recovery conditions. Neither releases accounting for resources whose terminal state is unproven.


### Completed-task transport defect


An exceptional once-only `os._exit(86)` of the current mitmdump is permitted only when all of these observations agree on its owner loop:


- The exact live runtime, client/token, adapter, registered handler and actual HttpLayer-owned upstream/task identities match.
- That task was captured before requesting normal close, and the ordinary close command or the same handler's synchronous close was consumed.
- The task has ended, the connection is CLOSED, and the current transport entry still identifies that task and an actual TCP StreamWriter that is not closing. An old pre-connect IO entry is insufficient.
- The runtime's escalation flag has not previously been set.


The flag is set before exit, without logging, IPC, network operations or cleanup hooks in between. The adapter does not signal the Go owner. Normal RST/refusal, pending tasks, canceled pre-connect tasks without IO, closing writers, stale identities and unknown ownership do not satisfy this predicate. Failure to satisfy it is not proof that a handle is safe to release.


### Unverifiable cleanup ownership


If lifecycle observation cannot establish required ownership or prove completed cleanup, the runtime exits the current mitmdump with code 87 instead of leaving it running indefinitely with retained admission budgets. This is a separate condition from the completed-task/current-writer defect above: it does not claim that an open writer was proven. The runtime sets its once-only exit flag before exiting, without releasing unproven resources or logging first. Ordinary stale callbacks after admission replacement or release still use their identity guards. A completed task whose admission is still exactly retained but whose handler/IO ownership no longer matches triggers code 87; an unrelated late callback does not.


### Owner recovery and availability


The existing Go generation owner reaps an unexpected owned-child exit and retains session, readiness and recovery responsibilities. An exit can interrupt other requests served by the same mitmdump process. For a current, running, non-stopping owned child, the experimental runtime latches recovery-required when its quarantine controller is configured (nft-based modes). It attempts namespace quarantine, which can stop all sandbox networking, including loopback, DNS and control/health connections. Recovery from that state requires sandbox destruction and recreation. Without the nft quarantine controller, the MITM readiness gate becomes false on exit, but ordinary child restart may succeed; the same sticky-quarantine recovery behavior does not apply. Neither path guarantees an instantaneous atomic readiness response or automatic restoration. `QuarantineUnknown`, an exit code or a 503 does not establish packet isolation. The boundary excludes arbitrary addon descendants or inherited FDs, origin business completion, replay safety and a strict total reap deadline. Changed addon connection shapes require new ownership verification. See the [revision-runtime warning](https://open-sandbox.ai/architecture/network/egress#transparent-tls-interception-l7).


## Verification boundaries


Socket-free tests cover registry/publication, the fixed-version adapter, lifecycle, hooks and H1 regressions. They do not prove socket, TLS or IPC behavior.


The opt-in runtime runner uses the actual system addon, authenticated Unix IPC, and SOCKS5 followed by TLS to a real `127.0.0.1:443` destination. Its 15 manual-peer cases cover attachment, removal/drain, rotation, remove/re-add, reset and disconnect with H1/H2 upstreams, short/default expiry and the isolated exceptional-exit case. These passed on an earlier tested tree; they were **NOT_RUN** in the later two-case Go run. Historical results are not fresh verification of subsequent revisions.


Outstanding acceptance includes:


- H2-A5: successful library-driven migration with the old response preserved; the held-old Go case remains failed.
- P2: pre-ACK/paused-hook races, fragmented HEADERS and flow-control variants, upstream queues/unfinished uploads/stranded trailers, and path-only or policy-only rotation.
- P3: Linux transparent-443/original-destination behavior, the restricted production user, applicable IPv4/IPv6 paths, actual Go owner/quarantine readback and the complete relevant H1/policy/credential regression matrix.


Loopback testing, including loopback on Linux, does not establish these production networking properties. Process reap and origin socket closure do not establish kernel quarantine or origin business completion.


The runner reports PASS, FAIL, BLOCKED and NOT_RUN separately, with exact commit/tree and dependency identities. A selected subset passing is not full acceptance. Go observations require a separately built fixture and an explicit exact `--require-go-version`; the runner must not infer that requirement from the binary under test or silently select another toolchain. See the [runtime runner](https://github.com/opensandbox-group/OpenSandbox/blob/main/components/egress/tests/test_credential_bound_h2_runtime.py) and [Go fixture instructions](https://github.com/opensandbox-group/OpenSandbox/blob/main/components/egress/tests/fixtures/h2_retry_client_README.md) for execution requirements.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/network/osep-0023-h2-integration.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/network/auto-pause-wake-on-access`

Return to top

# Auto-Pause and Wake-on-Access


Fast Sandbox sandboxes occupy their full CPU and memory allocation for as long as they live, and agent workloads are idle most of that time. Auto-pause and wake-on-access turn the existing checkpoint machinery into an automatic cycle: a sandbox that opts in is paused after **X** seconds without ingress traffic, and the next request to it **wakes** it — the gateway parks the request for up to a budget **Y** while the sandbox restores, then forwards normally. Both halves default to off; scope is the fast-sandbox backend only.


Full proposal: [OSEP-0024](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0024-auto-pause-and-wake-on-access-for-fast-sandbox.md). Enablement and configuration: [the user guide](https://open-sandbox.ai/guides/auto-pause-wake).


## Lifecycle


![Auto-pause and wake-on-access lifecycle](https://open-sandbox.ai/assets/auto-pause-wake-lifecycle.BPudXWCd.svg)
*Full proposal: OSEP-0024. Enablement and configuration: the user guide.*

## Lifecycle ​
## Design principles ​
## How it works ​
## Failure behavior ​
## Security ​
## Observability ​
## References ​









Three properties of this state machine carry most of the design:


- **Pausing is cancelable.** A wake arriving mid-checkpoint flips the sandbox back to `Running` — a wrongly-timed pause never completes.
- **Pausing does not stop the expiry clock.** A paused sandbox whose `expires_at` passes becomes `Terminated` (CR retained) and wake then fails fast with `404`.
- **Absence of policy is a hard no-op.** A sandbox that never declares `lifecycle.idlePolicy` is never auto-paused and never auto-woken, regardless of deployment flags.


## Design principles


1. **One observation point.** All client traffic transits the ingress, so it is the only activity producer and the only wake authority. What the ingress cannot see does not keep a sandbox alive; `activeProbe` is the single app-declared exception.
2. **Desired state over coordination.** `PauseSandbox` / `ResumeSandbox` are idempotent CAS patches on the Sandbox CR. Pause needs only a per-sandbox lock (checkpoints must not double-run); wake needs none — duplicate resumes converge because the restore is driven by `spec.state`, not by callers.
3. **Three-party activation.** Server config, ingress flags, and the per-sandbox policy must all agree. An unreadable or malformed policy is treated as absent — never as an implicit opt-in.
4. **Fail-safe direction.** Redis down → no pauses (wake does not use Redis). Missing activity key → *unknown*, tombstoned: data loss can delay a pause, never accelerate one. Any pause failure leaves the sandbox `Running`.
5. **Bounded wake.** One resume flight per sandbox per replica (singleflight); a parking lot and restore permits admit before any RPC; budget exhaustion answers `503 + Retry-After` and never cancels an in-flight restore.
6. **Provenance-gated replay.** The gateway-owned `OpenSandbox-Wake: expired` marker proves a request was never forwarded — only marked responses are SDK-auto-retried; post-forward re-entry retries idempotent methods once, everything else keeps today's `503`.


## How it works


![Auto-pause and wake-on-access sequence](https://open-sandbox.ai/assets/auto-pause-wake-sequence.CVvbpEWD.png)


👉 [Interactive sequence diagram](https://open-sandbox.ai/architecture/network/auto-pause-wake.html) — walk the three phases with guided views, theme switching, and relationship tracing.


**Observe.** Every proxied request produces one activity observation: `SET opensandbox:activity:{id} = now_ms EX ttl`, a monotonic-max write issued asynchronously and coalesced per sandbox — fire-and-forget, never on the forwarding hot path. Create and resume write immediately, so the idle clock starts at the latest lifecycle transition. Since `X ≤ activity_ttl_seconds` is enforced at create time, a present-but-stale key is idle *by value*; a missing key is resolved by tombstones, not assumptions. A sandbox that declares `activeProbe` adds a pull-mode producer: when the sweeper is otherwise ready to pause, it probes the app through the gateway (sentinel-carried, never counted as activity) — a busy answer is recorded as ordinary activity, an explicit not-active lets the pause proceed, and any failure drops the candidate.


**Pause.** Each server replica sweeps every `sweep_interval_seconds`: enumerate `Running` sandboxes, batch-read activity keys, then apply the gates in order — opt-in annotation → `Running` → idle ≥ X → not expired → `NX` lock → re-verify → probe. Surviving candidates get `PauseSandbox` (idempotent CAS). There is no leader election: the lock admits one replica per idle episode and idempotency absorbs lost races, so a crashed replica leaves no stuck state. The worst case of the whole subsystem is a missed pause.


**Wake.** A request whose route resolution reports `FailedPrecondition` (or that surfaces a stale-route error) reads the sandbox state and policy; `Paused` / `Pausing` / `Resuming` start or join a resume flight. The flight — one per sandbox per replica — issues `ResumeSandbox` fenced on `expected_checkpoint_id`, parks its requests, and polls `GetSandbox` with backoff until Ready or budget Y. Parked requests hold no upstream connection; WebSocket upgrades complete after wake. Budget exhaustion answers the [wake-timeout contract](https://open-sandbox.ai/guides/auto-pause-wake#wake-behavior-and-sdk-retry) while the restore converges in the background — the next request is served on the fast path.


## Failure behavior


| Failure | Outcome |
| --- | --- |
| Redis unreachable | Sweeps skipped — no pauses; wake unaffected (no Redis on that path) |
| Redis data loss | Tombstone ⇒ pause delayed by ≥ X from first observation, never accelerated |
| Replicas race to pause | Lock + idempotent CAS ⇒ exactly one pause per idle episode |
| Resume races a re-pause | `expected_checkpoint_id` fence ⇒ `Aborted`; the flight restarts within budget |
| Slow (cross-node) restore | Budget Y bounds the client; `503` + `Retry-After` while the restore continues |
| Burst to many paused sandboxes | Lot + permits bound; overflow shed before any `ResumeSandbox` |


## Security


The ingress gains exactly two FastPath calls on the channel it already holds (`GetSandbox`, `ResumeSandbox`) plus one read-only Kubernetes grant to read the idle-policy annotation. It can never pause. Parking happens after the existing host/route-scope/signature verification, so wake is reachable only for sandboxes a client can already address.


## Observability


The loop exposes wake flights, park wait durations, shed count, active restores, dropped activity writes, and probe outcomes. The **flap ratio** (pauses followed by a quick wake — the primary tuning signal for X) is derived per sandbox from pause and wake telemetry. See the [Telemetry guide](https://open-sandbox.ai/guides/telemetry).


## References


- [User guide](https://open-sandbox.ai/guides/auto-pause-wake) — enablement, `idlePolicy` reference, SDK retry behavior, tuning.
- [Ingress](https://open-sandbox.ai/architecture/network/ingress) — the observation point and wake authority.
- [Fast Sandbox: Pause, Resume, and Snapshots](https://open-sandbox.ai/architecture/fast-sandbox/checkpoints) — the checkpoint machinery this loop automates.
- [OSEP-0024](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0024-auto-pause-and-wake-on-access-for-fast-sandbox.md) — full proposal, alternatives, and test plan.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/network/auto-pause-wake-on-access.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/network/single-host-network`

Return to top

# Single-Host Network (Docker)


This page describes the **Docker runtime** on a single host. Its counterpart on Kubernetes is the [Ingress gateway](https://open-sandbox.ai/architecture/network/ingress), which routes sandbox traffic across the cluster.


The Docker runtime exposes every sandbox port through one host port per sandbox: `execd` bundles a reverse proxy, and the runtime maps only that proxy port to the host.


![Single-host sandbox routing](https://open-sandbox.ai/assets/single-host-network.pyF1dAVy.svg)


## Single-host routing model


- Every sandbox container starts `execd` listening on container port `44772`. `execd` bundles a lightweight reverse proxy that intercepts requests with the `/proxy/{port}` prefix and forwards them to `127.0.0.1:{port}` inside the same container.
- The Docker runtime binds only the host side of the execd proxy port (labeled `opensandbox.io/embedding-proxy-port`). Callers use `get_endpoint(..., port=X)` to receive `{public_host}:{host_proxy_port}/proxy/{X}`, and execd transparently routes the request back to the sandbox service on port `X`.
- Because the proxy preserves `Upgrade`, `Connection`, and other HTTP headers, HTTP, Server-Sent Events, and WebSocket traffic share the same mapped host port without additional configuration.
- With this setup, a single host port per sandbox suffices to reach **all** container ports. You can safely run many sandboxes on one machine without worrying about overlapping host port allocations.
- When the caller can actually route to the sandbox's Docker network, use `get_endpoint(..., resolve_internal=True)` to bypass the host mapping and return the sandbox IP (e.g., `172.17.0.3:5900`) instead. Merely running the lifecycle server in a container is not sufficient: a server attached to a Compose network cannot normally route to sandboxes created on Docker's separate default bridge.
- The diagram above shows the routing path: host traffic hits the proxy port, execd rewrites the request towards the target container port, and upstream services remain isolated within the sandbox.


## Network modes


### Host network mode (single-host constraints)


- Containers share the host network stack (`network_mode=host`) so sandbox ports are directly accessible on the host.
- Because each sandbox binds its ports on the host, this mode practically limits you to one sandbox instance per host unless you reserve dedicated ports per sandbox.
- `get_endpoint(..., port=X)` returns `{public_host}:{X}` with no `/proxy/` prefix, so the caller needs to know the exact host port and the host must manage firewall rules for each sandbox port.


### Bridge network mode (default for single-host deployments)


- Docker places sandboxes on an isolated bridge network, preventing container ports from being reachable without explicit mapping.
- For single-host scaling, OpenSandbox maps only execd’s proxy port (`44772`) and, optionally, port `8080`. Any other container port stays private and is reached via the proxy.
- The reverse proxy label (`opensandbox.io/embedding-proxy-port`) identifies a host port that fronts `execd`. `get_endpoint(..., port=X)` returns `{public_host}:{host_proxy_port}/proxy/{X}`, so all internal ports can share the same host binding.
- Port `8080` may also receive a direct host binding (`opensandbox.io/http-port`), providing a conventional HTTP endpoint without the proxy path when required.
- This bridge setup lets a single machine host many sandboxes without port conflicts, because the same host proxy port can multiplex requests for HTTP, SSE, WebSocket, VNC, etc.


### User-mode network modes (podman: `pasta`, `slirp4netns`)


- Some container runtimes can attach a container to a user-mode network namespace instead of a bridge. Podman uses this for rootless containers, and `network_mode = "pasta"` is the practical choice on hosts where bridge networking is unavailable (for example a rootless podman machine whose netavark cannot apply its nftables ruleset).
- These modes involve **no** bridge, so no host-routable container IP exists: the Docker-compatible inspect reports an empty `NetworkSettings.IPAddress` and no `NetworkSettings.Networks` entry. The host reaches the sandbox only through the published ports.
- `get_endpoint(..., resolve_internal=True)` therefore returns the server-local host-mapped endpoint (`{proxy_host}:{host_proxy_port}/proxy/{X}`) for these modes — the same fallback used for sandboxes that share an egress sidecar network namespace — instead of failing with `NETWORK_MODE_ENDPOINT_UNAVAILABLE`.
- Everything else is unchanged: `host` / `bridge` / `none` and user-defined networks keep their existing behaviour, and `networkPolicy` (egress sidecar) still requires `bridge`.


## Containerized lifecycle server
## Single-host routing model ​
## Network modes ​
## Containerized lifecycle server ​
## Operational notes ​






When the lifecycle server runs on a Compose network and creates sandboxes on Docker's default bridge through the mounted Docker socket, route server-proxy traffic through the host-published ports:

toml

```
[server]
host = "0.0.0.0"

[proxy]
resolve_internal = false

[docker]
network_mode = "bridge"
host_ip = "host.docker.internal"
```


The server container must resolve `host.docker.internal` to the Docker host. On Linux, add `extra_hosts: ["host.docker.internal:host-gateway"]` to its Compose service, as shown in the [Compose example](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/docker-compose.example.yaml). Both HTTP and WebSocket proxy requests then use the host-mapped endpoint. A configured `[server].eip` remains the public endpoint address; the server-side proxy uses the locally reachable host instead.


Upgrade legacy server images


The legacy `server/v0.2.3` release hardcodes internal-IP resolution in both proxy paths. Setting `resolve_internal = false` alone cannot fix that release: SDK readiness checks can still time out even when the sandbox's host-mapped `/ping` endpoint responds.


Use `opensandbox/server:release-1.1.0`, which includes the configurable proxy resolution and local proxy-host fixes. OpenSandbox now uses [unified release tags](https://open-sandbox.ai/community/versioning); the frozen `server/v*` tags do not identify newer server releases. The Compose example pins the fixed image explicitly instead of relying on `latest`.


After updating the image and configuration, pull and recreate the server container. From the repository root:

bash

```
docker compose -f server/docker-compose.example.yaml pull opensandbox-server
docker compose -f server/docker-compose.example.yaml up -d --force-recreate opensandbox-server
```


Retry the SDK readiness check through the server proxy after the server starts.


## Operational notes


- If execd’s proxy port (`44772`) or the optional `8080` host mapping is missing, `get_endpoint` responds with HTTP 500 and a message stating which mapping was unavailable.
- Always keep the `/proxy/{port}` prefix (including any additional path or query string) when embedding URLs in browser-based clients or SDKs so that execd can correctly dispatch the request.
- This proxy-based approach means additional ports never need to be published on the host, simplifying firewall management and improving security.
- When the lifecycle server runs in Docker with the host socket mounted, set `[proxy] resolve_internal = false`, configure `[docker] host_ip`, and make that hostname resolve to the Docker host from the server container. The repository's `server/docker-compose.example.yaml` demonstrates this topology.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/network/single-host-network.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/templates`

Return to top

# Templates


Templates are how Fast Sandbox fixes a workload before any request exists: runtime, image, entrypoint, and resources are decided at build time, so the create API only needs to express intent — which template, whose sandbox, for how long. `templateId` is mutually exclusive with `image` / `snapshotId`, and per-request workload fields (entrypoint, env, resources, volumes) are rejected.


## Two layers, one template
## Two layers, one template ​
## What a build produces ​
## Using templates ​





A template exists in two places, on purpose:


- **Server-persisted metadata** (SQLite/PostgreSQL) is the source of truth for template definitions and tenant ownership. Templates are tenant-private; the catalog is served through the same server that serves sandboxes, so SDKs manage templates with the same authentication and tenancy as everything else.
- **`SandboxTemplate` CRs** drive the actual build on the fast-sandbox side. The server persists the definition and creates the CR; the platform's builder turns it into a golden-image artifact asynchronously. Template state converges from CR observations — the same pattern as sandbox state.


Builds are asynchronous by design: the API returns an accepted state immediately, and the template becomes usable when the build reports readiness.


## What a build produces


A `SandboxTemplate` describes a conversion, not just a copy: an ordinary OCI image plus the OpenSandbox guest wiring, compiled into an immutable golden image.


- **Guest wiring is injected**: an init path (PID 1, carrying the readiness marker and heartbeat) and the execd runtime files always come from the template — every sandbox built from it is execd-ready by construction.
- **Business entrypoint and envs** are baked in: an empty entrypoint defaults to a keep-alive; envs are injected literally into the guest (no runtime indirection).
- **Runtime shape is declared**: the template names the Firecracker guest kernel and reference machine; readiness defines when the guest counts as up.
- **Output is content-addressed**: the build publishes artifacts to the store and records a manifest reference plus artifact digest in the CR status — builds are immutable and verifiable, never mutated in place.


## Using templates


Sandbox creation with a `templateId` resolves to the recorded artifact; capacity comes from the referenced pool, not from the template. Because the template pins the workload, per-sandbox behavior is limited to intent: identity, TTL, metadata, network policy, and an optional pool reference (see [Scheduling](https://open-sandbox.ai/architecture/fast-sandbox/scheduling)). Updating a template rebuilds the artifact and yields a new digest — existing sandboxes keep running their admitted revision; new creations pick up the new build.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/templates.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/checkpoints`

Return to top

# Pause, Resume, and Snapshots
## What a checkpoint contains ​
## Pause and resume ​
*Pause (POST /sandboxes/{id}/pause):*

*Resume (POST /sandboxes/{id}/resume):*

## Snapshots ​
## Why copy-on-write is safe here ​
## Relationship to BatchSandbox pause/resume ​







Fast Sandbox checkpoints runtime state into the same content-addressed artifact store that golden images use. Pausing a sandbox writes a complete checkpoint and releases its Fastlet, so a paused sandbox has zero compute footprint; resuming restores the checkpoint on whichever Fastlet admission chooses — not necessarily the original host. Snapshots are the public form of the same machinery: they publish a running sandbox's state as a reusable artifact set that new sandboxes can be created from.


The public lifecycle API is unchanged across backends: `POST /sandboxes/{id}/pause`, `/resume`, and `/sandboxes/{id}/snapshots` return **202 Accepted** and the work completes asynchronously. The server submits intent to FastPath over gRPC and observes progress on the durable `sandbox.fast.io` Sandbox record — the same submit-and-converge pattern as every other mutation (see [High Availability](https://open-sandbox.ai/architecture/fast-sandbox/ha)).


## What a checkpoint contains


A pause checkpoint captures the sandbox's runtime state as one artifact set in the store:


| Part | Content |
| --- | --- |
| `rootfs` | The sandbox's writable root filesystem |
| `vmstate` | MicroVM device and vCPU state for Firecracker-backed templates |
| `memory` | Guest memory, staged through the node's `/dev/shm` during capture |
| `SHA256SUMS` | Digest manifest over the set |


The Sandbox record's `status.runtime.checkpoint` carries the result: a `checkpointID` derived from the sandbox UID, the spec generation that requested the pause, and a `pauseAttempt` retry epoch; the `manifestRef` (`s3://` URI) of the published set; its digest and size. The checkpoint is written digest-first — **a pause is only reported complete after the artifact set is fully in the store** — and a Paused sandbox without a recorded checkpoint cannot be resumed; it must be reset.


## Pause and resume


**Pause** (`POST /sandboxes/{id}/pause`):


1. The server reads the Sandbox record, fences the call with its `uid`, and sends `PauseSandbox` to FastPath with the request ID.
2. FastPath records the intent (`spec.state: Paused`); the runtime captures rootfs, VM state, and guest memory, publishes the artifact set, records the checkpoint on the Sandbox status, then **releases the Fastlet capacity**.
3. Status converges by observation: `Pausing → Paused` on the Sandbox record. Routes through the ingress are rejected once paused — a paused sandbox is unreachable, not degraded.


**Resume** (`POST /sandboxes/{id}/resume`):


1. The server fences with the UID and submits `ResumeSandbox`.
2. FastPath flips the record back to `Running`; the controller restores the recorded checkpoint **possibly on a different Fastlet** — the artifact store, not node locality, is what makes resume portable.
3. Resume advances the route generation, so clients must re-resolve endpoints; existing routes do not follow the sandbox to its new host.


Only a Ready runtime may pause; UID mismatches and missing checkpoints surface as `409 Conflict`.


## Snapshots


A snapshot turns a running sandbox's state into a durable, reusable artifact set — published under the same content-addressed layout as template golden images, so a restored snapshot and a native template behave identically at create time.


1. `POST /sandboxes/{id}/snapshots` accepts only a Running source, creates the `SandboxSnapshot` record with a deterministic name and a `sandboxRef.uid` fence, and then persists the `CREATING` row — the runtime intent always exists behind a readable row, on every replica.
2. The platform drives the record through `Pending → Creating → Publishing → Succeeded/Failed`. Creation may briefly pause the sandbox while state is captured; publishing writes the artifact set plus an index entry keyed by the snapshot's template name.
3. The server converges the row by watching the record, re-checking on read, and CAS-writing the terminal state; recovery resubmits the same idempotent intent, so a crashed server leaves the row recoverable, not stuck.
4. `POST /sandboxes {"snapshotId": ...}` restores from a `READY` snapshot: the index entry resolves like a template, and creation routes to Fast Sandbox. The sandbox ID is new; the snapshot is a starting point, not a continuation.


Snapshot names are cluster-wide index keys with last-writer-wins semantics, so FastPath rejects a non-terminal holder of a name before accepting a new one. Deleting a snapshot record does not delete the pushed artifacts — store retention is operator policy (see [Storage](https://open-sandbox.ai/architecture/fast-sandbox/storage)).


## Why copy-on-write is safe here


- **Checkpoints are immutable artifacts.** Resume and restore never trust a mutable tag; every artifact set is referenced by manifest digest and verifiable against `SHA256SUMS`.
- **Node-local rootfs copies are CoW reflinks.** Each node keeps a private XFS state root where per-sandbox rootfs instances are reflink copies of cached artifacts — instant provisioning without duplicating bytes, and without sharing state across failure domains (see [Firecracker](https://open-sandbox.ai/architecture/fast-sandbox/firecracker)).
- **Delivery is amortized, not shared.** [DART](https://github.com/data-accelerator/dart) fetches each block from the origin roughly once cluster-wide and serves peers from node-local caches, so a resume after pause pays little more than a local clone.


## Relationship to BatchSandbox pause/resume


Fast Sandbox and the Kubernetes operator run **two independent checkpoint mechanisms**. `sandbox.fast.io` Sandbox records checkpoint microVM runtime state (rootfs + VM state + memory) for template-backed sandboxes; the operator's `SandboxSnapshot` (`sandbox.opensandbox.io`) commits container rootfs — and, for the QEMU contract, VM state — to an OCI registry (see [Pause and Resume](https://open-sandbox.ai/guides/pause-resume)). They share the lifecycle API and 202 semantics, not the artifact format or the control plane.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/checkpoints.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox`

Return to top

# Fast Sandbox Integration


Fast Sandbox is a runtime backend that connects OpenSandbox to the external [fast-sandbox](https://github.com/opensandbox-group/fast-sandbox) platform. It provisions template-backed **Firecracker microVM** sandboxes inside pre-warmed **Fastlet** pods, removing the per-sandbox Kubernetes scheduler, watch propagation, and kubelet path from the creation hot path.


The adapter and endpoint integration live in this repository. FastPath, the Fastlet runtime, and the `sandbox.fast.io` CRDs are owned by the fast-sandbox platform and consumed as-is.


## How it fits


- **Backend selection**: Fast Sandbox is not a separate `runtime.type`. Under `runtime.type = "kubernetes"`, `CompositeSandboxService` routes create requests carrying `templateId` to `FastSandboxService`, and dispatches operations on existing `fsb-` prefixed sandbox IDs to it. Image- and snapshot-based requests keep using the Kubernetes workload providers.
- **Control protocol**: the server and ingress talk to the fast-sandbox control plane (FastPath v2) over gRPC. gRPC ends at FastPath: the FastPath/Reconciler-to-Fastlet control protocol is JSON over HTTP (`/api/v2/fastlet/*`). FastPath owns mutations and live runtime operations; reads of persisted state use Kubernetes LIST/WATCH on `sandbox.fast.io` custom resources.
- **Tenancy**: a tenant provider maps each authenticated tenant to a fast-sandbox namespace; request-scoped operations resolve it from context, background work falls back to a lookup by sandbox ID.


![Fast Sandbox architecture](https://open-sandbox.ai/assets/fast-sandbox-architecture.B6cp5cP9.svg)


👉 [Interactive architecture diagram](https://open-sandbox.ai/architecture/fast-sandbox/architecture.html) — explore sandbox creation, template artifact flow, checkpoints, and deployment topology in a full-view explorable map.


## Core components


| Component | Responsibility | Design goal |
| --- | --- | --- |
| FastPath (gRPC control plane) | Serves every mutation and live operation: create, update, expiry, endpoint resolution, snapshots | Constant-time create via in-memory placement; restartable because durable state lives in CRDs, not here |
| Reconcilers (controller) | Drive CRs to reality: build templates, run pools, place sandboxes, finish snapshots | Converge by observation — no leader election, replay from CRs after any restart |
| Sandbox CRDs (`sandbox.fast.io`) | Durable record of intent, placement, policy bindings, and observations per sandbox | Intent survives every component failure; the CR is the source of truth |
| Fastlet (pre-warmed pod) | Hosts many sandboxes in one network domain; provides runtime capacity and shared services | Density with isolation: pre-provisioned network slots, shared egress and DNS amortized across sandboxes |
| Runtime agent (per node) | Owns Firecracker VM lifecycle over a unix socket; node readiness checks and self-labeling; installs assets | Node autonomy: the control plane delegates, the node verifies itself before admitting workloads |
| [DART](https://github.com/data-accelerator/dart) (per node) | Peer-to-peer artifact delivery between node state roots | Amortize the origin: each block fetched from the store roughly once cluster-wide |
| Egress process (per Fastlet) | Multi-sandbox outbound policy: subjects, Sandbox Actions handler, DNS and network enforcement | Fail-closed per-sandbox policy without per-sandbox sidecars — policy may be late, never open |
| Template builder | Converts OCI images into golden-image artifacts (guest wiring, init, execd baked in) | Workload fixed before any request: creates express intent, not configuration |
| Janitor | Sweeps orphaned resources of failed operations | Reconciliation finishes interrupted work; the janitor removes what should no longer exist |


## Design principles


- **No new public API**: template-based creation and `fsb-` ID dispatch ride the existing lifecycle contract. SDKs work unchanged across backends, and no sandbox-to-backend registration store exists — the ID prefix is the dispatcher.
- **CRD-first control**: durable per-sandbox intent lives in `sandbox.fast.io` resources; FastPath gRPC carries the mutation hot path. The Kubernetes scheduler, watch propagation, and kubelet leave the create path — the durable write does not.
- **Fail-closed multi-tenant egress**: every subject denies traffic from registration until its data plane is ready — policy delivery can be late, never early-open.
- **Authenticated routing**: sandbox routes are signed `f1.` scopes verified at ingress; endpoint issuance is decoupled from readiness.
- **Firecracker by template**: golden images are built for Firecracker microVMs — the runtime shape is fixed at build time, not per request.


## Documentation


| Page | Content |
| --- | --- |
| [Interactive Architecture](https://open-sandbox.ai/architecture/fast-sandbox/architecture.html) | Explorable component map: sandbox creation, template artifact flow, checkpoints, and deployment topology |
| [Templates](https://open-sandbox.ai/architecture/fast-sandbox/templates) | Template catalog, golden-image builds, artifact publication |
| [Scheduling](https://open-sandbox.ai/architecture/fast-sandbox/scheduling) | Pools and Fastlets, the create hot path, lifecycle and pause/resume |
| [Networking](https://open-sandbox.ai/architecture/fast-sandbox/networking) | Network slots, inbound route scopes and resolution, outbound egress enforcement |
| [Pause, Resume, and Snapshots](https://open-sandbox.ai/architecture/fast-sandbox/checkpoints) | Checkpoint artifacts, pause/resume across Fastlets, snapshot publication and restore |
| [High Availability](https://open-sandbox.ai/architecture/fast-sandbox/ha) | What survives which failure: control plane, nodes, sandboxes |
| [Storage](https://open-sandbox.ai/architecture/fast-sandbox/storage) | Artifact store, peer-to-peer block delivery, node state roots |
| [Firecracker](https://open-sandbox.ai/architecture/fast-sandbox/firecracker) | Host requirements, per-VM networking model, agent delegation |
| [Performance](https://open-sandbox.ai/architecture/fast-sandbox/performance) | ACK create, request, snapshot, and same-node pause/resume measurements |[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/index.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/scheduling`

Return to top

# Scheduling


Fast Sandbox schedules sandboxes into **pools** of pre-warmed **Fastlet** pods. A pool fixes the runtime profile and resource shape; a Fastlet hosts many sandboxes; a sandbox claims a slice of one Fastlet. The result: creating a sandbox is a constant-time admission into capacity that already exists, instead of a fresh scheduling round.


## Pools


A `SandboxPool` is the unit of capacity and policy:


- **`capacity`** sizes the Fastlet fleet — how many warm pods to hold, and the ceiling.
- **`runtime`** selects one immutable, platform-owned runtime profile (the Firecracker profile). All sandboxes in a pool share it.
- **`sandboxResources`** is the immutable resource shape of every sandbox the pool produces.
- **`fastletTemplate`** is an ordinary Kubernetes pod template for the Fastlet pods themselves — node selectors, affinity, and spreads stay Kubernetes-native.
- **`infraComponents`** declares the pod-local infrastructure (such as the egress action handler). It is compiled into an immutable revision: updating it rolls new Fastlets while existing sandboxes stay on the revision they were admitted with.
- **`maxSandboxesPerPod`** bounds density; **`warmImages`** lists artifacts to pre-pull, protected from ordinary cache eviction, so readiness never waits on a pull.


## Placement and admission
## Pools ​
*A SandboxPool is the unit of capacity and policy:*

## Placement and admission ​
## Sandbox lifecycle ​





When the server submits a create, FastPath ranks in-memory candidates — image-cache affinity first, then normalized load, then a stable-hash tiebreak — and admits the sandbox atomically on the chosen Fastlet. Two properties make this safe rather than merely fast:


- The **network slot exists before the runtime**: netns, veth, and masquerading are pre-provisioned per sandbox, and the attachment identity plus policy bindings ship with the admission. A sandbox is never reachable before its policy is (see [Networking](https://open-sandbox.ai/architecture/fast-sandbox/networking)).
- The **Sandbox CR is written first and completely**: intent, initial policy, and pool reference are durable before the runtime starts, so an admission interrupted by any failure is recoverable by reconciliation instead of leaking a half-created sandbox.


## Sandbox lifecycle


The Sandbox CR carries the lifecycle in three fields:


- **`state`** — `Running` keeps a live runtime; `Paused` checkpoints it to the artifact store and releases the Fastlet capacity. Resume restores the checkpoint **possibly on a different Fastlet**, which is why routes must be re-resolved after resume.
- **`expireTime`** — absolute deletion deadline, enforced by the platform.
- **`failurePolicy` + `recoveryTimeoutSeconds`** — what to do when a Fastlet is lost (default: manual recovery after 60 seconds of lost contact). `resetRevision` triggers a deliberate reset and rescheduling.


Task execution is part of admission: the request's entrypoint is delivered as a task to the sandbox rather than baked into the pod, which is what allows a pre-warmed Fastlet to serve arbitrary templates (see [Templates](https://open-sandbox.ai/architecture/fast-sandbox/templates)).


Snapshots and pause/resume follow the same submit-and-converge pattern as every other mutation — see [Pause, Resume, and Snapshots](https://open-sandbox.ai/architecture/fast-sandbox/checkpoints) and [High Availability](https://open-sandbox.ai/architecture/fast-sandbox/ha).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/scheduling.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/networking`

Return to top

# Networking
## Design highlights ​
## Inbound: route scope to Fastlet ​
## Outbound: one egress control plane, N subjects ​





Fast Sandbox traffic flows through two adapters in this repository:


- **Inbound** (client → sandbox): the ingress gateway's `FastSandboxProvider` verifies signed route scopes and forwards traffic to the Fastlet through FastPath endpoint resolution (`components/ingress/`).
- **Outbound** (sandbox → external): one shared egress process per Fastlet pod enforces per-subject policy for N sandboxes, driven by the Sandbox Actions protocol (`components/egress/`).


## Design highlights


- **Authenticated scopes instead of raw routing keys**: a route is a signed `f1.` scope binding tenant namespace, sandbox ID, and port. The ingress verifies before it routes; there is no unauthenticated path to a sandbox.
- **Lazy resolution**: the upstream address resolves only when traffic arrives, so routes stay valid across Fastlet rescheduling without an invalidation protocol.
- **Fail-closed egress**: every subject denies traffic from registration until its data plane is ready — policy delivery can be late, never early-open.
- **Policy as data**: egress policy rides the Sandbox CRD's revisioned `actionBindings`; only credentials travel out of band, memory-only.
- **One dispatch point**: DNS filtering and network enforcement are shared pod-netns services, dispatched per packet by source IP.


## Inbound: route scope to Fastlet


### Route scopes


A Fast Sandbox route is an authenticated scope, not a plain host or path. The server signs the tenant namespace, sandbox ID, and port with the `opensandbox-fsb-route-v1` scheme; the `f1.` prefix identifies the scope format version, and the ingress shares the server's signing key ring.


- Header mode expresses the scope as an `OpenSandbox-Ingress-To` header; URI mode encodes it in the path.
- Wildcard-host scopes are deliberately unsupported: namespace, sandbox ID, and MAC do not fit safely in one DNS label.
- Clients must preserve the returned route and headers verbatim — the scope is the credential.


The server issues these routes without calling FastPath or waiting for readiness: signing the tenant namespace, sandbox ID, and port is a local operation keyed by the shared ingress key ring. Issuance is therefore decoupled from sandbox state, and endpoint discovery never proves existence — the ingress resolves and verifies when traffic arrives.


### Endpoint resolution


The ingress resolves the upstream address through the FastPath `ResolveEndpoint` RPC when a request arrives. Resolution returns the target endpoint, the proxy address to forward through, and any required headers.


Failure semantics are part of the contract:


- A `FailedPrecondition` — including a not-yet-published route — surfaces as `503` with `Retry-After`. It is never reported as a missing sandbox: the ingress must not leak the difference between "not ready" and "does not exist".
- The policy port (`18080`) is resolvable for SDK compatibility but returns `501` for traffic; policy operations belong to the server's network policy route, not the data path.


### Access modes


| Mode | Path | Trade-off |
| --- | --- | --- |
| `direct-fastlet-proxy` (default) | Ingress → Fastlet pod directly | Lower latency; requires ingress to reach Fastlet pod IPs |
| `central-proxy` | Ingress → fast-sandbox central proxy → Fastlet | No pod-IP reachability requirement; extra hop |


Direct mode bypasses the central proxy, so the pod network must restrict Fastlet data-plane ports to trusted ingress workloads, and FastPath must admit the ingress namespace when the two systems deploy separately. The mode is chosen per deployment, not per request.


### Transport and interoperability


The ingress speaks only the `ResolveEndpoint` subset of FastPath v2 at a pinned wire revision shared with the server's generated client, so the components stay interoperable as fast-sandbox evolves. gRPC transport is plaintext; isolation between ingress, Fastlets, and FastPath is a deployment concern (network policy), with TLS deferred until both sides support it.


## Outbound: one egress control plane, N subjects


Fastlet pods host many sandboxes in one network domain, so the per-sandbox egress sidecar does not apply. The egress component runs the opt-in **fast-sandbox profile** (`OPENSANDBOX_EGRESS_PROFILE=fast-sandbox`): one egress process per Fastlet pod serves N sandboxes as independent **subjects**, each with its own policy, credentials, and kernel rules. The default sidecar profile is unchanged; the two profiles are mutually exclusive deployment forms.


Policy reaches subjects as data: the server writes it to the Sandbox CRD's revisioned `actionBindings` through the shared lifecycle policy route, with sidecar-compatible semantics — replace is total, merge follows sidecar rules (same-target rules replace in place, first per target wins), removal is by target and idempotent. Writes are fenced by sandbox UID and generation (`409` on a lost race; other tenants are indistinguishable from missing, `404`), and a successful write commits intent only — enforcement converges on the Fastlet asynchronously, and a cleared binding resets the subject to deny-first.


### Network slots


Each sandbox is pre-provisioned with a **network slot** in the Fastlet pod netns before it exists: netns, veth, and masquerading are set up ahead of any create request, and the attachment identity ships in the `SET_BINDING` envelope. A sandbox never waits for network setup, and egress can enforce policy from its first packet.


![Fast Sandbox network slots](https://open-sandbox.ai/assets/fast-sandbox-network-slot.DEzWWRyy.svg)


The slot's IP is the dispatch key: the shared DNS proxy selects the subject for each packet by source IP, so one service per Fastlet serves every sandbox with per-subject policy.


| `attachment.network` field | Role |
| --- | --- |
| `ip` | Dispatch key — `ip saddr` matches select the subject's rules |
| `gateway` | Target of the DNS REDIRECT |
| `privateCidr` | Sibling-isolation rules between sandboxes |
| `hostVeth` | Reserved — on the bridge topology, policy hooks see the bridge device, not the veth |


### Subject lifecycle


A **subject** is the unit of policy, credential, and rule ownership — one per sandbox, identified by the sandbox UID. The egress process maintains a per-subject state machine:

text

```
absent ──SET_BINDING──► denying ──data-plane-ready──► active
   ▲                        │                            │
   └──────REMOVE_BINDING────┴────────────────────────────┘
```


Subject lifecycle and policy are delivered by the Fastlet over the public **Sandbox Actions Handler** protocol (`sandbox.fast.io/actions/v1`). The egress process is the handler; two Pod-loopback HTTP endpoints serve it:


- `POST /_fastlet/v1/actions` — `SET_BINDING`, `LIFECYCLE_HOOK`, `REMOVE_BINDING`.
- `GET /_fastlet/v1/actions/status` — process incarnation probe. A changed `instanceId` makes the Fastlet replay the latest binding and all reached hooks.


Every operation carries fencing fields (`runtimeInstanceId`, `attachmentId`) so a control-plane reset can never look like a rebinding. Unknown protocol versions, operations, or hook names are validation errors and are never silently ignored.


### Credential delivery


Credential vault revisions are **egress-held** (OSEP-0022): the server pushes complete vault revisions over the FastPath handler-relay (`InvokeHandlerAction`) to the egress vault surface (`/vault/{sandboxUid}`) on the Pod loopback. FastPath validates tenant-scoped sandbox ownership before the Fastlet forwards the payload — there is no proxy-injected identity header. The relay response is the synchronous ack: success means egress has validated **and durably persisted** the revision. Pushes stay in egress — memory plus an egress-local per-subject file, no Secret volumes, no CRD/etcd vault material. A vault mutation for a subject that has not reached `data-plane-ready` is held at the same barrier as the policy; there is no separate pending-cache channel.


**Egress-local persistence** (OSEP-0022 stage 2) backs the ack with durable state:


- **Layout**: one file per subject at `<egress-volume>/vault/<sandboxUid>.json` (Pod-scoped `emptyDir`; survives an egress container restart, dies with the Pod). Format: `{"v": 1, "incarnation": <runtimeInstanceId>, "attachmentId": <attachmentId>, "revision": …, "vault": {…vault JSON…}}` — a versioned shared server↔egress contract; v1 is plaintext and the volume joins the credential trust surface (mount the `emptyDir` with `medium: Memory` to keep plaintext off node disk).
- **Commit protocol**: the relay write persists the file (atomic temp + rename + parent-dir fsync, reusing the policy-persistence machinery) **before** applying to the live store and acknowledging — acked ⇒ durable and applied. Uncertain outcomes restore the previous file and latch a recovery state that freezes vault writes until the process restarts; a rejected request never leaves a partially applied revision. The relay request body is parsed before the control-plane lock is taken and the listener sets explicit read timeouts, so a stalled client can never freeze the shared data plane.
- **Reload at registration**: on egress restart the Fastlet replays `SET_BINDING`; the committed file reloads only when its recorded fence (runtimeInstanceId + attachmentId) matches the envelope — a mismatch (sandbox reset, or a rebind that changed only the attachment) is stale and purged, never carried into a new sandbox. A structurally corrupt file, or content the binding policy rejects, degrades that subject's vault: credential interception fails closed for it while policy enforcement continues — observable through the actions status payload (`degradedVaults`), with the unusable file quarantined so a restart cannot re-degrade on it (a file whose schema version is newer than this egress understands is preserved, not destroyed). `/healthz` stays 503 only while the recovery latch freezes writes; a per-subject degradation is never a process-health failure. A successful vault write clears the degradation.
- **Snapshot transfer across pause/resume**: the egress exposes `VAULT_EXPORT` / `VAULT_IMPORT` actions (OSEP-0022 "Vault Lifecycle"). Export copies the subject's file into the driver-provided bundle target **strictly before** the runtime teardown purges it and seals the subject (vault ops answer 409; policy enforcement is unchanged while paused). Import lands the bundle file through the same commit protocol and re-stamps it with the restored runtime fence — the only authorized incarnation transfer, since restore may land on any Pod — before `data-plane-ready`; the vault activates with the policy at that barrier. The driver pause/resume hooks and the snapshot-manifest entry invoke the transfer.
- **Server surface**: the user-facing vault API is server-routed (`POST|PATCH|GET|DELETE /v1/sandboxes/{id}/credential-vault[...]`). fsb sandboxes relay over this channel (the server composes `PATCH` as relay GET → in-memory merge → relay PUT carrying the read revision, so a lost cross-replica race answers 412); other backends proxy their sandbox-side sidecar. Values never leave the server on any public read.
- **Configuration**: persistence is enabled by setting `OPENSANDBOX_EGRESS_VAULT_DIR` (the mounted `emptyDir` subdirectory) on the egress container; unset keeps the vault memory-only. `REMOVE_BINDING` purges memory plus the file (terminal).


### Enforcement


Enforcement is nftables in the Fastlet pod network namespace, dispatched by source IP — the attachment block of each action envelope supplies the subject's IP, gateway, host veth, and private CIDR.


- **DNS**: one shared proxy on loopback `127.0.0.1:15353`. Per-subject prerouting REDIRECTs forward sandbox DNS addressed to the attachment gateway, preserving the source IP so per-query policy dispatches to the right subject.
- **Forward path**: per-subject `hook prerouting` chains mark allowed destinations (`meta mark 0x2`); the master forward chain drops unmarked traffic. The path deliberately never emits an explicit `accept` — with `net.bridge.bridge-nf-call-iptables=1` (the fast-sandbox bridge topology) an accept verdict returns the frame to bridge L2 and is lost.
- **Dynamic sets**: DNS-learned IPs get bounded leases; a per-subject connection refresh loop renews leases of active TCP connections. UDP/QUIC relies on DNS TTLs.
- **Encrypted DNS**: DoT (853) is always dropped; optional DoH-over-443 blocking applies globally to every subject.
- **Chained upstream proxy**: when `OPENSANDBOX_EGRESS_UPSTREAM_PROXY` is set alongside transparent MITM, all shared-mitmproxy egress is chained through that proxy via `CONNECT`. The endpoint is infrastructure, not sandbox egress: it is dropped profile-wide in the master dispatch chain (forward and input paths, ahead of every per-subject rule) so no subject policy — default-allow included — can CONNECT the proxy directly. A hostname endpoint is registered as an infrastructure domain on the shared DNS proxy, so its answers never feed the dynamic allow sets; the shared mitmdump resolves the name through the Fastlet pod's own resolver, so it must be resolvable via cluster DNS. Since the DNS proxy's forward upstreams and the pod resolver can return different address sets (split-horizon or operator-configured DNS), the egress's self-resolution refresh queries both authorities and seeds the drop sets with the union — an address only the pod resolver returns is one a sandbox could otherwise CONNECT directly. Drop elements are permanent (no kernel timeout): containment persists through egress downtime like every other rule in the table, and expiry is owned by the egress — the refresh loop prunes addresses both authorities stop returning, while a failed resolve keeps every element (fail-closed retention). The first seed retries with bounded backoff at startup and fails egress startup if the hostname cannot be resolved, before any sandbox action is served.
- **Upstream proxy refresh and recovery**: both resolver authorities run concurrently. Partial failures are logged and only add returned addresses; pruning requires absence from two successful refreshes of both authorities, and a sandbox DNS lookup renews retention. Before resetting the nft table, startup resolves the hostname with bounded retries and seeds the in-memory addresses. Both authorities must complete successfully with a nonempty union; failure leaves the previous kernel table intact. DNS resolution and nft application have separate timeouts.
- **Atomicity**: static sets are swapped atomically; on restart the egress wipes stale subject rules while installing the seeded proxy addresses, publishes a new `instanceId`, and the Fastlet replays every live binding.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/networking.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/storage`

Return to top

# Storage


Fast Sandbox reduces storage to one shape: **everything a sandbox runs or resumes from is a content-addressed artifact** in a single S3-compatible store. Golden images, pause checkpoints, and snapshots are all artifacts, referenced by manifest digest — never mutated, always verifiable.


![Artifact storage and delivery](https://open-sandbox.ai/assets/fast-sandbox-artifacts.DQMbicus.svg)


## Where artifacts come from


- **Template builds** convert an OCI image (plus guest wiring and, for microVM runtimes, a kernel) into a golden-image artifact and publish it; the SandboxTemplate CR records the manifest reference and digest (see [Templates](https://open-sandbox.ai/architecture/fast-sandbox/templates)).
- **Pause checkpoints and snapshots** are written by the same machinery: the runtime state is captured, pushed, and recorded digest-first in the SandboxSnapshot CR (see [Pause, Resume, and Snapshots](https://open-sandbox.ai/architecture/fast-sandbox/checkpoints)). Resume never trusts a mutable tag.


## Where artifacts go


Nodes keep a **private state root** — an XFS-reflink-backed cache local to each node, never shared between nodes. This is deliberate: a fastlet's instant starts come from node-local artifacts, and cross-node state sharing would turn every node into part of every other node's failure domain.


The cost of private caches is duplicate downloads, and that is what **[DART](https://github.com/data-accelerator/dart)** eliminates: a node-local delivery daemon per node, peer-aware through a headless Service roster. Block-level fetches (4 MiB) follow `cache → peer → origin` — each block is fetched from the origin roughly once cluster-wide, then served peer-to-peer. Per-node block source counters make the delivery path observable.


## What is deliberately *not* stored


- **Egress credentials** stay memory-only in the egress process — pushed per subject over the proxy route, never written to a Secret volume or disk.
- **Sandbox runtime writes** (files a sandbox created) live in the sandbox's own slice; they are captured only when an explicit checkpoint or snapshot says so. Storage for sandboxes is an act of the lifecycle, not a background sync.
- **Routing and policy state** lives in the CRDs, not in the artifact store — the store carries bytes, the cluster carries meaning.


## Operating it
## Where artifacts come from ​
## Where artifacts go ​
## What is deliberately not stored ​
## Operating it ​






The artifact store is plain S3-compatible object storage; capacity planning reduces to artifact sizes and retention. Deleting a SandboxSnapshot record does not delete the pushed artifacts — retention and cleanup of the store are operator policy, kept outside the sandbox lifecycle on purpose.


### Prepare the node state disk


The `fast-sandbox` chart mounts `runtime.stateRoot` from the host (default `/var/lib/fast-sandbox/firecracker`). `DirectoryOrCreate` creates a directory on the existing filesystem; it does not provision a separate disk. When using the `opensandbox` umbrella chart, set `fast-sandbox.runtime.stateRoot`. Set the chart value to the same directory used as the helper's mountpoint. Prepare this mount **before deploying the runtime DaemonSet** on each node. Otherwise, drain the node's sandboxes and restart the runtime Pods after mounting: an already-running sandbox may continue seeing the old filesystem.


Prefer a dedicated XFS data disk with reflink enabled. For a **new, empty device**, after verifying its identity and that it contains no required data:

bash

```
sudo mkfs.xfs -m reflink=1 /dev/vdb
sudo mkdir -p /var/lib/fast-sandbox/firecracker
sudo mount -o noatime /dev/vdb /var/lib/fast-sandbox/firecracker
sudo blkid /dev/vdb
```


Persist the mount in `/etc/fstab` using the device's UUID. Formatting destroys the device's contents; never run these commands on an existing state disk. Keep the mountpoint empty before mounting so existing state is not hidden.


When no extra device is available, the repository provides [`scripts/fast-sandbox-state-root-setup.sh`](https://github.com/opensandbox-group/OpenSandbox/blob/main/scripts/fast-sandbox-state-root-setup.sh):

bash

```
bash scripts/fast-sandbox-state-root-setup.sh --dry-run 50G
sudo bash scripts/fast-sandbox-state-root-setup.sh 50G
# Optional: SIZE MOUNTPOINT BACKING_FILE
sudo bash scripts/fast-sandbox-state-root-setup.sh 100G /data/firecracker /data/firecracker.xfs
```


The helper allocates a new backing file, formats it with XFS `reflink=1`, mounts it with `loop,noatime`, and verifies an actual reflink copy. It requires Linux, `xfsprogs`, GNU coreutils, and util-linux. It refuses existing backing files, symlinked paths, mounted targets, and nonempty mountpoints. It prints an fstab entry for review; it does not edit fstab or restart workloads. On failure, it retains any created backing file for inspection instead of risking deletion of mounted data. Inspect `findmnt` and `losetup -j BACKING_FILE` before cleanup or retry.


Unlike a sparse file, the helper uses `fallocate` to reserve the requested space and checks that at least another 10 GiB remains on the backing filesystem. This is a point-in-time check, not a host-wide reservation: other workloads can still fill that filesystem, and thin-provisioned storage needs its own capacity monitoring. A dedicated disk avoids coupling the state cache to root-disk usage.


### Capacity and readiness


Budget for every distinct cached template's rootfs **plus guest-memory snapshot**, active sandbox writable data, and cache overhead. Start with at least 50% workload headroom and keep **more than 10 GiB free** on the state filesystem (the default host-readiness floor). The helper's minimum volume size is 11 GiB; that is not a production sizing recommendation. Reflink saves initial copying but subsequent writes still allocate blocks.


Old template artifacts are not automatically reclaimed just because a template version changes. Track disk usage, retire unused templates, drain sandboxes using them, and stop the node runtime before manually reconciling its local caches. Do not delete live `images`, `cache`, or `jails` directories. Preserve any state needed for recovery, and expect artifacts to be downloaded again after cleanup.


After provisioning, verify the filesystem and the runtime's readiness report:

bash

```
# Use your configured runtime.stateRoot (for example /data/firecracker):
STATE_ROOT=/var/lib/fast-sandbox/firecracker
findmnt -M "$STATE_ROOT"
df -h "$STATE_ROOT"
sudo xfs_info "$STATE_ROOT"   # expect reflink=1
kubectl -n opensandbox-system get daemonsets
# Use the deployed Firecracker runtime DaemonSet name:
kubectl -n opensandbox-system rollout restart daemonset/<runtime-daemonset>
kubectl -n opensandbox-system logs daemonset/<runtime-daemonset> --all-containers --tail=100
```


The `stateroot-filesystem` check should report `type xfs` and `reflink CoW supported`. Insufficient free space fails readiness and can remove the Firecracker scheduling labels; missing reflink support warns and falls back to full rootfs copies. A healthy state disk alone does not guarantee readiness: KVM, memory, and runtime assets must also pass their checks.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/storage.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/ha`

Return to top

# High Availability


Fast Sandbox's availability story follows from one decision: **every sandbox's intent, placement, policy bindings, and observations live in Kubernetes CRDs**, not in the memory of any component. Components are restartable because the durable state is not theirs.


## The control plane is deliberately single
## The control plane is deliberately single ​
## Converge by observation ​
## Cleanup ​
## What failure looks like ​






The fast-sandbox controller (reconcilers + FastPath) runs as a single replica without leader election. This is a design position, not an omission:


- Mutations are fast precisely because FastPath can hold placement and candidate state in memory; a replicated control plane would need consensus around exactly that state.
- Nothing durable depends on that memory. A crashed control plane loses only in-flight reconciliation work, which CR-driven reconciliation replays: sandboxes, pools, templates, and snapshots all re-converge from their CRs.


Availability of the *sandboxes* is therefore independent of availability of the *control plane*: running sandboxes keep running, and traffic keeps flowing, while the control plane restarts.


## Converge by observation


Recovery everywhere uses the same pattern — **submit intent, converge by observing the durable record** — instead of leases or leader election:


- **Snapshots**: creating a snapshot submits intent and returns immediately; terminal state is observed from the SandboxSnapshot CR. Two servers coordinating snapshots converge on the deterministic CR: one observes before creating, create races are absorbed as `409`, and the terminal database write is conditional on the expected prior state.
- **Egress**: on restart the egress process wipes its rules and publishes a new incarnation ID; the Fastlet replays every live binding and reached hook, so subjects re-enter deny-first and re-open only after their data plane is confirmed ready.
- **Nodes**: the runtime agent reports Fastlet health to the platform; a lost Fastlet is handled according to the sandbox's `failurePolicy` after `recoveryTimeoutSeconds` — manual by default.


## Cleanup


A janitor runs on a scan interval and removes orphaned artifacts of failed operations (stale pods, leftover resources) after an orphan timeout — the complement to convergence: reconciliation finishes interrupted work, the janitor sweeps what should no longer exist.


## What failure looks like


| Failure | Effect | Recovery |
| --- | --- | --- |
| Control plane restart | Brief loss of mutation capacity; running sandboxes unaffected | CR-driven reconciliation replays intent |
| Fastlet pod lost | Sandboxes on that Fastlet go down | Per-sandbox `failurePolicy` after `recoveryTimeoutSeconds`; checkpoints (if any) resume on another Fastlet |
| Server restart | No effect on sandboxes; open operations resume from durable records | Same observe-and-converge pattern |
| Artifact store outage | New starts degrade to direct pulls; running sandboxes unaffected | DART resumes peer/origin service when the store returns |


Pause/resume deserves a note: pausing checkpoints the runtime and **releases** the Fastlet, so a paused sandbox has no compute footprint at all — and resume lands on whichever Fastlet admission chooses, not necessarily the original one.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/ha.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/performance`

Return to top

# Performance
## How to read these numbers ​
## Environment ​
## Create ​
## Request latency ​
## Live snapshot ​
## Restore from snapshot ​
## Pause / resume ​
## Artifact delivery (DART P2P) ​
## Boot characteristics ​
## Interpreting the results ​
## Reproducing ​













ACK (Alibaba Cloud Container Service for Kubernetes) is Alibaba Cloud's managed Kubernetes service. This page reports measurements collected on a two-node ACK cluster on 2026-10-08: serial and concurrent creates, request latency, live snapshot, and same-node pause/resume through the OpenSandbox SDK. Runtime logs provide phase timings alongside the SDK results. These are engineering measurements, not a production latency guarantee.


The warm create path admits work into pre-warmed capacity (see [Scheduling](https://open-sandbox.ai/architecture/fast-sandbox/scheduling)) and restores a snapshot instead of booting a kernel (see [Firecracker](https://open-sandbox.ai/architecture/fast-sandbox/firecracker)). Pause/resume uses the submit-and-converge mutation path (see [High Availability](https://open-sandbox.ai/architecture/fast-sandbox/ha)). Capacity, runtime work, and the readiness boundary still determine the observed latency and success rate.


## How to read these numbers


- **SDK readiness** includes the Python SDK, lifecycle server, FastPath, ingress gateway, and guest `/ping` 200. Runtime creation ends earlier.
- **Warm creates** have template artifacts cached and Fastlet capacity prepared. First-use artifact delivery is a separate cost.
- **Sample counts and failures** are reported with latency. Successful-attempt percentiles do not describe failed or timed-out requests, or prove throughput.
- **Batch differences** matter: client resources and placement, and artifact-store persistence changed between the initial serial baseline and later runs. The two batches are reported separately and are not a controlled A/B comparison.


[Download the raw SDK report](https://open-sandbox.ai/benchmarks/fast-sandbox-ack-2026-10-08.json) for individual samples, failures, runtime phases, image digests, and settings.


## Environment


| Dimension | ACK environment (2026-10-08) |
| --- | --- |
| Cluster | Two ACK nodes, Kubernetes `1.36.2-aliyun.1`, containerd 2.1.9 |
| CPU | Per node: AMD EPYC 9T95, 192 CPUs exposed, 191.45 allocatable |
| Memory | Approximately 742 GiB allocatable per node |
| OS / kernel | ContainerOS/Lifsea, `5.10.134-19.6.1.lifsea8.x86_64` |
| StateRoot | 50 GiB XFS `reflink=1` loop filesystem per node, backed by an ext4 ESSD data disk |
| Pool | Five Fastlets, four slots each: 20 slots |
| Snapshot workload | Alpine 3.19 + execd, 1 vCPU, 2 GiB memory, 2 GiB rootfs |
| Artifact store | RustFS on a persistent hostPath on one node during the later runs |
| Firecracker | 1.16.1 |


The SDK deployment uses server, controller, and runtime agent `release-1.1.1-rc.1`. Its derived Fastlet image adds GNU coreutils `cp` 9.11; working reflink support requires both the filesystem and copy tool. The XFS startup rejection change was not deployed during measurement. The template artifact digest is `d78575470094c6fe1a2da2a71b7578971dff9e77cd5381dee236dd53e01b54cb`, cached on both nodes. SDK version: `1.1.1rc2.dev106+gc7dc78a4.d20261008`.


## Create


### SDK creates


Each SDK create run has two untimed warmups and 100 timed attempts, with template artifacts already cached. Timing starts before `Sandbox.create_from_template()` and ends at guest `/ping` 200 through the gateway. Each sandbox is killed after readiness. Concurrent batches have a five-second reclamation pause; deletion and batch pauses are excluded from individual latency. The later serial and concurrent runs retain the same pool configuration.


The in-cluster client disables metrics, uses a ten-second HTTP request timeout, and polls readiness every 10 ms (SDK default: 200 ms). Percentiles use the nearest-rank method. Client differences between the initial serial baseline and later comparison runs are noted below.


| Measurement | Success | p50 | p90 | p99 | Mean |
| --- | --- | --- | --- | --- | --- |
| SDK create, initial serial baseline | 100/100 | **64.0 ms** | 93.8 ms | 108.3 ms | 70.6 ms |
| SDK create, serial repeat alongside concurrency runs | 100/100 | 77.9 ms | 105.3 ms | 112.5 ms | 78.2 ms |
| SDK create, concurrency 10 | 100/100 | 102.7 ms | 120.1 ms | 125.4 ms | 102.4 ms |
| SDK create, concurrency 20 | 51/100 | 136.7 ms | 163.0 ms | 197.0 ms | 134.2 ms |


The initial 100-create validation is retained as the warm serial baseline. Its exact p50 is 63.995 ms, mean 70.587 ms, and range 53.811–113.326 ms; all 100 creates reached guest readiness. It used the same cluster, template, pool shape, SDK version, timeout, and 10 ms readiness criterion. Its client Pod had a two-CPU limit with placement not explicitly pinned; the later comparison client has a four-CPU limit and runs on one selected node. RustFS persistence also changed between runs, although these warm creates used cached template artifacts.


The 77.9 ms repeat remains visible because it was collected alongside the concurrent runs with their client configuration. Both serial batches are in the raw report and are not pooled. Their difference is not a controlled experiment that isolates a host, client-CPU, or storage change.


Runtime logs from the same creation windows give the following breakdown. These include each run's two untimed warmups, so their sample counts differ from the SDK table. They stop at runtime creation, before SDK readiness:


| Load | Runtime create p50 | Rootfs preparation p50 | VM state load/resume p50 | Runtime log samples |
| --- | --- | --- | --- | --- |
| Serial repeat | 50.0 ms | 2.31 ms | 0.233 ms | 102 |
| Concurrency 10 | 34.1 ms | 2.76 ms | 0.234 ms | 102 |
| Concurrency 20 | 33.5 ms | 2.63 ms | 0.225 ms | 53 |


The initial serial validation's separate runtime window has a 39.43 ms runtime-create median and 2.286 ms rootfs-preparation median across 103 creates (100 timed, two warmups, and one subsequent lifecycle create).


Saturation result


The concurrency-20 latency distribution contains **successful attempts only**. There were 48 `SandboxRateLimitException` failures (HTTP 429 / Fastlet `CapacityRejected`) and one readiness timeout with repeated gateway HTTP 503. Four test CRs also stuck in deletion with an assignment annotation/status projection conflict. Their stale placement projections were cleared to let the controller perform cleanup before the next experiment. This run does not establish reliable 20-way admission or a sustainable requests-per-second rate. The implementation cause of the admission/projection failure needs a separate fix; replacing the host disk alone does not resolve it.


## Request latency


The SDK samples use one warm sandbox and 100 sequential calls per path:


| Path | Success | p50 | p90 | p99 | Mean |
| --- | --- | --- | --- | --- | --- |
| Warm SDK `/ping` through the gateway | 100/100 | 0.92 ms | 1.15 ms | 5.91 ms | 1.07 ms |
| SDK `commands.run('echo ack-perf')`, through completion and stream EOF | 100/100 | 202.8 ms | 204.3 ms | 207.1 ms | 203.2 ms |


The [execd command handler](https://github.com/opensandbox-group/OpenSandbox/blob/c7dc78a4090e5de2b9119e9bd93952cae24f87bd/components/execd/pkg/web/controller/command.go) has a default 200 ms stream-close grace period; the observed approximately 203 ms is consistent with that behavior. It is not a measurement of shell process startup alone.


## Live snapshot


One live snapshot was measured:


| Phase | Measured |
| --- | --- |
| Snapshot request accepted | 14.4 ms |
| Request → available snapshot (`Ready` in the SDK) | 60.63 s |
| VM frozen during dump | 11.14 s |
| Runtime artifact publication | 46.22 s |
| Artifact set | 2 GiB rootfs + 2 GiB memory |


The SDK source was healthy afterward, with its file marker and boot ID preserved. Requests were not sampled throughout its freeze, so this establishes no zero-interruption claim. The initial probe used an incorrect terminal-state check and is excluded from the timings.


## Restore from snapshot


Creating a new sandbox from a published live snapshot was not measured in this ACK run. Cached checkpoint restoration was measured as part of [same-node pause/resume](https://open-sandbox.ai/architecture/fast-sandbox/performance#pause-resume); template restoration is covered by [Create](https://open-sandbox.ai/architecture/fast-sandbox/performance#create). These operations have separate completion boundaries.


## Pause / resume


For this test only, the idle pool was restricted to one existing node, retaining five Fastlets and four slots per Fastlet. Every sample's source and destination Kubernetes node were verified through the CR's placement and the Fastlet Pod's `spec.nodeName`. All three resumes moved to a different Fastlet on that **same node** and used the node's checkpoint cache. The original pool selector was restored afterward.


| Measurement | Median | Observed range (3 samples) |
| --- | --- | --- |
| SDK pause request accepted | 22.4 ms | 22.0–25.5 ms |
| Pause request → durable `Paused`, including upload and release | 61.14 s | 61.13–61.23 s |
| VM frozen during checkpoint dump | 11.15 s | 11.13–11.18 s |
| Publish approximately 4 GiB (2 GiB rootfs + 2 GiB memory) | 45.61 s | 45.61–45.63 s |
| Resume runtime creation, after cached artifacts are available | 35.49 ms | 33.64–35.50 ms |
| Resume rootfs preparation | 2.92 ms | 2.64–3.26 ms |
| SDK same-node resume → guest `/ping` 200 | **62.66 s** | **58.29–65.16 s** |


All three samples preserved the filesystem marker, tmpfs marker, boot ID, background PID, and process start time. The sandbox identity also stayed the same. No checkpoint artifact-delivery attempt appears in the corresponding Fastlet logs. Rootfs checkpoint cloning took 0.88–0.94 ms with zero full-copy time. Three samples establish this observed range, not a reliable p99.


Same-node resume remains slow


Cached runtime restoration is tens of milliseconds, but usable SDK resume is approximately a minute in this deployment. Runtime logs publish the route immediately after restoration, leaving most elapsed time in endpoint/guest availability and client waiting. These measurements do not isolate which network, gateway, endpoint-resolution, or retry mechanism causes that gap. The gap cannot be explained by copying a 2 GiB rootfs or fetching a checkpoint onto another node. Do not substitute the runtime number for SDK resume.


The probe used a four-minute resume budget and ten-second HTTP request timeout; the SDK's default resume budget is 30 seconds. The reported result includes actual readiness waiting and does not skip health checks.


## Artifact delivery (DART P2P)


Not verified in this ACK run. Template artifacts were already cached on both nodes, and same-node resumes used the checkpoint cache. Cold delivery latency, origin/peer block counts, and P2P efficiency require separate measurements.


## Boot characteristics


Cold kernel boot was not verified in this ACK run. Template creates restore `vmstate.snap` instead of booting a kernel; their measured VM state load/resume phases appear under [Create](https://open-sandbox.ai/architecture/fast-sandbox/performance#create).


## Interpreting the results


XFS reflink support and GNU `cp` keep warm rootfs preparation in the millisecond range: the initial serial runtime window measured a 2.286 ms median. This measures the storage/copy phase, not total SDK readiness.


Concurrency changes admission contention; durable pause includes dumping, hashing, and uploading a checkpoint; SDK readiness includes endpoint resolution, HTTP timeouts, and retries. The saturation failures under [Create](https://open-sandbox.ai/architecture/fast-sandbox/performance#create) are control-plane evidence, not a host-only explanation. The same-node resume gap also remains unresolved. A warm `/ping`, completed command stream, runtime restore, and SDK resume have different completion boundaries.


## Reproducing


### SDK measurements


Use a source-built SDK matching the recorded version. Set `DOMAIN`, `API_KEY`, and `TEMPLATE_ID` for the target cluster without putting credentials in the report. Run from an in-cluster client to retain this network boundary:

bash

```
REQUEST_TIMEOUT=10 DISABLE_METRICS=1 PING_INTERVAL_MS=10 READY_TIMEOUT_WARM=180 \
N=100 CONCURRENCY=1 BATCH_PAUSE=0 REPORT_PATH=serial.json \
  python scripts/fast-sandbox-env/create-bench.py

REQUEST_TIMEOUT=10 DISABLE_METRICS=1 PING_INTERVAL_MS=10 READY_TIMEOUT_WARM=180 \
N=100 CONCURRENCY=10 BATCH_PAUSE=5 REPORT_PATH=concurrent10.json \
  python scripts/fast-sandbox-env/create-bench.py

# Saturation diagnostic: record failures as well as successful latencies.
REQUEST_TIMEOUT=10 DISABLE_METRICS=1 PING_INTERVAL_MS=10 READY_TIMEOUT_WARM=180 \
N=100 CONCURRENCY=20 BATCH_PAUSE=5 REPORT_PATH=concurrent20.json \
  python scripts/fast-sandbox-env/create-bench.py
```


`REPORT_PATH` saves raw attempts, settings, success/failure counts, and nearest-rank percentiles. A run with failed creates returns a nonzero exit status. Save the deployed image digests, host/storage details, template digest, pool shape, and timestamped Fastlet/controller logs alongside it. The SDK run used an equivalent probe that also collected lifecycle and request samples; the report retains those original samples.


For the other measurements, retain the same SDK connection settings:


1. On one warm sandbox, time 100 sequential `sandbox.is_healthy()` calls, asserting success; then time 100 `sandbox.commands.run('echo ack-perf')` calls through stream EOF, asserting the expected output.
2. On an idle pool restricted to one node, create a fresh sandbox for each of three lifecycle samples. Before pausing, wait for CR `status.runtime.state == Ready`; the SDK's early readiness result can precede that projection. Write markers to the filesystem and tmpfs and record the boot ID and a background process's PID/start time.
3. Start the pause timer before `sandbox.pause()`. Poll `manager.get_sandbox_info(id).status.state == 'Paused'` every 200 ms; an accepted pause response alone is not a durable checkpoint.
4. Time `Sandbox.resume(id, resume_timeout=timedelta(minutes=4), health_check_polling_interval=timedelta(milliseconds=10), connection_config=config)` through its normal readiness check. Verify placement on the original node and all guest markers before killing the sandbox. Restore the pool's original selector and wait for five warm, ready Fastlets.
5. For live snapshot, time `sandbox.create_snapshot()` acceptance separately from `manager.get_snapshot(id).status.state == 'Ready'` (200 ms polling). The public snapshot API uses `Ready`; template builds use `Succeeded`. Verify the source and delete the test snapshot and sandbox.


Capture runtime dump, publish, restore, and route-publication log timestamps to distinguish checkpoint I/O from later SDK readiness. Clean up only the artifacts created by the test after their sandbox/snapshot resources are gone.


Keep hardware, kernel, Firecracker version, template digest, pool shape, client placement, and artifact-store placement fixed when comparing load shapes.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/performance.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/architecture/fast-sandbox/firecracker`

Return to top

# Firecracker Support
## Topology ​
## Node architecture: agent delegation and P2P delivery ​
## Host and node requirements ​
## Networking model ​
## Measured characteristics ​
## Isolation guarantees ​








Fast Sandbox templates build golden images for Firecracker microVMs, and every sandbox runs as a real KVM virtual machine inside the Fastlet pod network namespace, alongside the shared egress process. The per-VM networking, isolation, and checkpoint machinery has been verified end-to-end on real hardware.


## Topology

text

```
host
└── Fastlet pod netns (docker bridge)
    └── fastlet container (privileged, /dev/kvm)
        ├── egress container (--network container:fastlet)   shared control plane
        ├── firecracker vm1 (10.30.0.5, gw 10.30.0.1)        policy + vault per VM
        └── firecracker vm2 (10.30.0.6, gw 10.30.0.2)        policy + vault per VM
              tap ── br0 ── veth ──► pod netns (per-subject policy enforcement)
```


The microVMs are first-class subjects of the [egress profile](https://open-sandbox.ai/architecture/fast-sandbox/networking#outbound-one-egress-control-plane-n-subjects): each VM registers through `SET_BINDING` with its attachment block (IP, gateway, host veth, private CIDR), stays deny-first until `sandbox.data-plane-ready`, and owns an isolated slice of policy, credentials, and kernel rules. Template builds and on-demand artifact delivery are described in [Templates](https://open-sandbox.ai/architecture/fast-sandbox/templates) and [Storage](https://open-sandbox.ai/architecture/fast-sandbox/storage).


## Node architecture: agent delegation and P2P delivery


The fast-sandbox control plane does not drive Firecracker directly. Each node runs a **runtime-agent** (DaemonSet) that owns the VM lifecycle locally; the control plane delegates VM operations to it over a host unix socket (`/run/fast-sandbox/firecracker/runtime.sock`). Readiness is reported through the same API — the agent answers `dartUp` alongside Firecracker health.


Golden-image artifacts are delivered by **DART**, a node-local daemon with peer-to-peer fallback. Each node keeps a private state-root subdirectory, so one node's cache never satisfies another node's pull; block-level fetches (4 MiB) flow `cache → peer → origin`, and the S3-compatible origin is hit roughly once per block cluster-wide.


![Firecracker node architecture](https://open-sandbox.ai/assets/fast-sandbox-firecracker-node.l6gyYnyQ.svg)


Peer discovery uses a headless `dart` Service: every daemon must see the full roster before pulls begin, so the second node's first create is served by the first node's blocks instead of the origin. Per-node block source counters (`cache` / `peer` / `origin`) make the delivery path observable.


## Host and node requirements


These are the checks the integration actually performs (chart + environment tooling) before a node hosts Firecracker sandboxes:


**Host** (bare metal, or a VM with nested virtualization exposing KVM):


- **Host kernel ≥ 5.10.**
- `/dev/kvm` present and passed through into the node containers, together with the KVM device node under `/sys`. Nested virtualization works as long as KVM is exposed; a host without it is never labeled and never receives microVM sandboxes.
- `/dev/net/tun` — TAP devices carry each sandbox network namespace's data plane. The Firecracker driver probes only `/dev/kvm` and `/dev/net/tun`; `vhost-vsock` is deliberately not mounted.
- `/dev/shm` sized beyond the container default — snapshot memory staging happens there.
- **cgroup v2** (unified hierarchy); cgroup v1 hosts are rejected up front.
- `fs.inotify.max_user_instances` raised on the host for the duration of the cluster.
- An **XFS filesystem with reflink support** backing the node state root: per-sandbox rootfs copies are copy-on-write reflinks, and the setup probes reflink explicitly — if the probe fails, setup refuses rather than degrading. Disabling XFS falls back to full copies. Reflink works only within one filesystem, which is why each node binds its own subtree of a single shared XFS volume.
- Headroom: the node readiness gate requires **10 GiB free disk** and **2 GiB free memory** by default.


**Node readiness is self-service.** The firecracker-runtime DaemonSet runs on every candidate node, performs the host checks, installs the Firecracker assets (default version `v1.16.1`; an optional custom kernel URL is supported — this section hot-reloads on every readiness pass), and only then labels the node (`sandbox.fast.io/kvm=true`, `fast-sandbox.io/firecracker-node=true`) and sets the `FirecrackerReady` condition. Pools place Fastlets only on labeled nodes; operators never label by hand.


**Not asserted by this repository:** an NVMe requirement — the checks above are the ones expressed in the chart and environment tooling; anything deeper (specific storage devices) would live in the fast-sandbox runtime source, which is outside this repository.


## Networking model


- **Per-VM gateway addresses.** Every VM gets its own veth pair and gateway IP in the pod netns. Sharing one gateway across VMs breaks under `arp_ignore=1`: the second VM's ARP goes unanswered and its traffic never leaves the guest. Per-VM gateways match the real per-VM veths, and the egress dispatches per attachment automatically.
- **Network namespace visibility.** `/var/run/netns` is mounted with `:rslave` propagation in both containers so VM netns created after container start are visible to management tooling; the default `rprivate` propagation hides them.
- **Guest traffic bypasses container netfilter.** Traffic crossing a VM netns is L2 bridge traffic from the pod's perspective. The authoritative enforcement layers are therefore the pod-netns forward chain — the pod-netns layers, not any container OUTPUT path.


Lifecycle ordering is fixed: VM netns created → `SET_BINDING` (deny-first) → `data-plane-ready` → sandbox traffic flows under its own policy.


## Measured characteristics


The ACK measurements cover template creates, request latency, live snapshot, and same-node pause/resume; results and environment details live in [Performance](https://open-sandbox.ai/architecture/fast-sandbox/performance). Cold kernel boot and DART P2P performance were not verified in that run.


## Isolation guarantees


- **Per-VM policy enforcement**: each VM's outbound traffic is filtered by its own subject policy at the DNS and network layers.
- **Cross-VM isolation**: a VM targeting another VM's host is refused at DNS resolution by its own policy.
- **Tamper resistance**: guests have no `NET_ADMIN` in the pod network namespace; enforcement rules are invisible and immutable from inside the guest.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/architecture/fast-sandbox/firecracker.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/multi-tenancy`

Return to top

# Multi-Tenancy
## Requirements ​
## How It Works ​
## Configuration ​
*Add to server.toml:*

*Then create tenants.toml at one of these paths (checked in order):*

*Example tenants.toml:*

## Namespace Setup ​
*Add Kubernetes resource settings to the server's [egress] configuration:*

## Hot Reload ​
## Key Rotation ​
## Migration from Single-Tenant ​
## Isolation Model ​
## Troubleshooting ​











Multi-tenancy enables a single OpenSandbox Server deployment to serve multiple independent consumers, each isolated in its own Kubernetes namespace. Each tenant gets dedicated API key(s), and all sandbox lifecycle operations (create, list, get, delete) are automatically scoped to the tenant's namespace.


## Requirements


- `opensandbox-server` >= 0.2.2
- Kubernetes runtime (`runtime.type = "kubernetes"` in `server.toml`)
- One Kubernetes namespace per tenant, **pre-created by a cluster admin**
- Default Helm chart RBAC (already includes ClusterRole with cross-namespace access)


Proxy routes in multi-tenant mode


Unlike single-tenant mode, proxy routes require `OPEN-SANDBOX-API-KEY` when multi-tenancy is enabled. Ensure clients include the header for proxy requests.


Docker not supported


Multi-tenancy requires Kubernetes namespace isolation. If `runtime.type = "docker"` is configured and tenants are enabled, the server refuses to start with a fatal error.


## How It Works


```
Request with OPEN-SANDBOX-API-KEY header
       │
       ├── Tenant provider configured?
       │       ├── YES → lookup key in tenant provider
       │       │       ├── found  → inject tenant context, route to tenant namespace
       │       │       └── not found → 401 Unauthorized
       │       └── NO  → validate against server.api_key (single-tenant legacy)
```


When multi-tenancy is active:


1. Auth middleware resolves the API key to a `TenantEntry` via the configured provider.
2. The tenant's namespace is injected into a request-scoped `ContextVar`.
3. Sandbox lifecycle operations (create/list/get/delete) use the resolved namespace.
4. List operations only return sandboxes within the authenticated tenant's namespace.
5. Proxy routes (`/sandboxes/{id}/proxy/...`) also require `OPEN-SANDBOX-API-KEY` in multi-tenant mode.
6. Create stamps `opensandbox.io/tenant=<name>` on the workload. When several tenants share one namespace, list/get/delete/proxy hide other tenants' labeled sandboxes (`404`). Unlabeled legacy sandboxes stay visible until they expire.


## Configuration


Multi-tenancy is enabled by adding a `[tenants]` section to `server.toml`. Two provider backends are available: **file** (local TOML) and **http** (remote endpoint).


### File Provider (default)


Add to `server.toml`:

toml

```
[tenants]
provider = "file"
```


Then create `tenants.toml` at one of these paths (checked in order):


1. `$SANDBOX_TENANTS_CONFIG_PATH` environment variable
2. `~/.opensandbox/tenants.toml`


Example `tenants.toml`:

toml

```
[[tenants]]
name = "team-alpha"
namespace = "sandbox-alpha"
api_keys = ["sk-alpha-key-1", "sk-alpha-key-2"]

[[tenants]]
name = "team-beta"
namespace = "sandbox-beta"
api_keys = ["sk-beta-key-1"]
```


Each tenant entry requires:


| Field | Description |
| --- | --- |
| `name` | Unique human-readable tenant identifier |
| `namespace` | Target Kubernetes namespace (must exist at server startup) |
| `api_keys` | One or more API keys for this tenant (supports key rotation) |


Constraints:


- API keys must be unique across all tenants (duplicate → startup error).
- Every tenant must have at least one key.
- `server.api_key` in `server.toml` must be removed when using `[tenants]`.


### HTTP Provider


For environments where tenants are managed by an external IAM or tenant management system:

toml

```
[tenants]
provider = "http"
endpoint = "https://iam.internal/opensandbox/tenant-lookup"
max_stale_seconds = 300.0
timeout_seconds = 5.0
auth_header = "X-Internal-Auth"
auth_token = "bearer-token-here"
```


| Field | Default | Description |
| --- | --- | --- |
| `provider` | `"file"` | `"file"` or `"http"` |
| `endpoint` | — | Required for HTTP. URL the server GETs to resolve a key. |
| `max_stale_seconds` | `300.0` | Max seconds to serve stale cache when endpoint is unreachable. |
| `timeout_seconds` | `5.0` | HTTP request timeout. |
| `auth_header` | — | Optional header name for provider-level auth. |
| `auth_token` | — | Optional token value for that header. |


**HTTP endpoint contract:**


Request:


```
GET {endpoint}
Header: OPEN-SANDBOX-API-KEY: <api_key>
```


Response (200):

json

```
{
  "namespace": "sandbox-alpha",
  "ttl": 60
}
```


Response (401):

json

```
{
  "code": "UNAUTHORIZED",
  "message": "Invalid API key"
}
```


The HTTP provider caches results per key using the server-suggested `ttl`. On TTL expiry it re-fetches synchronously. If the endpoint is unreachable, stale entries are served up to `max_stale_seconds`, after which requests fail with 503.


HTTP provider skips startup namespace validation


The HTTP provider resolves tenants per API key and cannot enumerate all tenants at startup, so the fail-fast namespace check is skipped for it (a warning is logged instead). The file provider, which loads the full `tenants.toml` at startup, still fails fast when any tenant namespace is missing or inaccessible. With the HTTP provider, ensure namespaces exist and are accessible before issuing tenant API keys.


## Namespace Setup


Before onboarding a tenant, the cluster admin must prepare the target namespace.


### 1. Create namespace

bash

```
kubectl create namespace sandbox-alpha
```


### 2. ResourceQuota (recommended)

yaml

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-quota
  namespace: sandbox-alpha
spec:
  hard:
    requests.cpu: "8"
    requests.memory: 16Gi
    limits.cpu: "16"
    limits.memory: 32Gi
    pods: "20"
```


#### Quota exhaustion behavior


When the namespace quota is exhausted, `POST /v1/sandboxes` fails fast with `403 KUBERNETES::QUOTA_EXCEEDED` instead of waiting for the sandbox-creation timeout and returning `KUBERNETES::POD_READY_TIMEOUT`:


- **Count quotas** (`count/sandboxes.agents.x-k8s.io`): the Sandbox create is rejected by Kubernetes admission immediately.
- **Compute quotas** (`requests.cpu`, `requests.memory`, `pods`): the Sandbox is created, but its Pod cannot be admitted; the server surfaces the rejection from the workload status (`ReconcilerError`) as soon as the controller records it (typically within a second).


The response body uses the standard `ErrorResponse` shape, and `message` carries the Kubernetes admission details, e.g. `exceeded quota: tenant-quota, requested: requests.cpu=1, used: requests.cpu=8, limited: requests.cpu=8`. SDK clients surface this as a typed error with HTTP status 403. Raise the quota or free capacity, then retry — no server restart is needed.


This fail-fast contract currently applies to the `agent-sandbox` workload provider (`[kubernetes] workload_provider = "agent-sandbox"`). With the default `batchsandbox` provider, the controller does not yet propagate admission rejections onto the CR status, so quota exhaustion still waits for the sandbox creation timeout and returns `KUBERNETES::POD_READY_TIMEOUT`.


### 3. LimitRange (recommended)

yaml

```
apiVersion: v1
kind: LimitRange
metadata:
  name: tenant-limits
  namespace: sandbox-alpha
spec:
  limits:
  - default:
      cpu: "1"
      memory: 2Gi
    defaultRequest:
      cpu: 250m
      memory: 512Mi
    type: Container
```


The `Container` defaults apply to every container that omits the corresponding resource setting, including the OpenSandbox egress sidecar. Configure smaller, sidecar-specific values in the lifecycle server so egress containers do not inherit defaults intended for sandbox workloads.


### 4. Egress sidecar resources (recommended)


Add Kubernetes resource settings to the server's `[egress]` configuration:

toml

```
[egress]
image = "opensandbox/egress:v1.1.7"
requests = { cpu = "25m", memory = "64Mi" }
limits = { cpu = "250m", memory = "256Mi" }
```


Requests and limits can be configured independently. These values are a starting point for basic DNS/nft enforcement; benchmark your workload and allow more headroom when using Credential Vault or transparent mitmproxy. If your `LimitRange` defines minimum values, the egress settings must satisfy them.


### 5. Server RBAC


The default Helm chart (`opensandbox-server`) already deploys a ClusterRole + ClusterRoleBinding with cross-namespace access. No additional RBAC changes are needed for multi-tenancy — the server ServiceAccount can already operate in any namespace.


## Hot Reload


### File provider


The file provider watches `tenants.toml` for changes (polls every 2 seconds). Changes take effect without server restart:


- **New key added** → immediately valid on next request.
- **Key removed** → immediately invalid (401).
- **Parse error during reload** → previous config retained, warning logged.
- **File deleted** → all tenant keys invalidated.


The watcher monitors the parent directory to handle Kubernetes ConfigMap atomic symlink swaps.


### HTTP provider


No explicit reload needed — cache entries expire per their `ttl` and are re-fetched on next lookup.


## Key Rotation


Multi-tenancy supports multiple API keys per tenant specifically for zero-downtime key rotation:


1. Add the new key to `tenants.toml` (or issue it via HTTP provider).
2. Wait for hot-reload (file) or TTL expiry (HTTP).
3. Update clients to use the new key.
4. Remove the old key from config.


Both old and new keys are valid simultaneously during the transition window.


## Migration from Single-Tenant


1. Create target namespace(s) for your tenant(s).
2. Write `tenants.toml` with your existing API key as a tenant entry, pointing to the existing namespace:toml ``` [[tenants]] name = "default" namespace = "your-existing-namespace" api_keys = ["your-existing-api-key"] ```
3. Add `[tenants]` section to `server.toml`:toml ``` [tenants] provider = "file" ```
4. Remove `api_key` from `[server]` in `server.toml`.
5. Deploy. The existing key continues working, now as a tenant key.
6. Add more tenants as needed.


**Rollback:** Remove the `[tenants]` section from `server.toml`, restore `server.api_key`, restart.


## Isolation Model


The server itself does not enforce resource quotas or network policies. Isolation is delegated to Kubernetes:


| Dimension | Kubernetes Mechanism | Scope |
| --- | --- | --- |
| Resource quota | `ResourceQuota` | Per-namespace CPU, memory, storage |
| Default limits | `LimitRange` | Per-namespace default container resources |
| Network isolation | Egress sidecar | Per-sandbox outbound policy via egress proxy |
| Sandbox count | `ResourceQuota` (pod count) | Per-namespace pod limit |
| RBAC | `RoleBinding` | Per-namespace API access |


Pool APIs are not tenant-scoped


Pool management routes (`/pools`) currently operate in the server's configured default namespace, not the authenticated tenant's namespace. Pools are shared resources. If you need per-tenant pool isolation, create separate server deployments or wait for future per-tenant pool support.


## Troubleshooting


| Symptom | Cause | Fix |
| --- | --- | --- |
| Server exits at startup: "Multi-tenancy requires Kubernetes namespaces" | `runtime.type = "docker"` with `[tenants]` configured | Use Kubernetes runtime or remove `[tenants]` |
| Server exits: "Remove server.api_key from server.toml" | Both `server.api_key` and `[tenants]` present | Remove `api_key` from `[server]` section |
| Server exits: namespace not found | Tenant namespace doesn't exist | `kubectl create namespace <ns>` before starting server |
| 401 on valid key after config change | Hot-reload hasn't picked up change yet | Wait 2s (file) or TTL seconds (HTTP) |
| 503 TENANT_PROVIDER_UNAVAILABLE | HTTP endpoint unreachable and cache expired past `max_stale_seconds` | Fix endpoint connectivity; increase `max_stale_seconds` |
| Duplicate api_key error at startup | Same key assigned to multiple tenants | Ensure each key is unique across all tenants |[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/multi-tenancy.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/egress-upstream-proxy`

Return to top

# Egress Chained Upstream Proxy Operations
## Overview and prerequisites ​
## Docker and Kubernetes configuration examples ​
## Traffic and security model ​
## Runtime compatibility matrix ​
*Compatibility reflects current upstream main only:*

## Protocol and streaming behavior ​
## Deployment, rotation, and rollback ​
## Verification checklist ​
## Troubleshooting table ​
## Known limits and references ​











OpenSandbox provides an administrator-managed chained upstream proxy capability for sandboxes running with egress network policies. This guide explains how to configure, operate, verify, and roll back an upstream forward proxy next hop across Docker and Kubernetes environments.


## Overview and prerequisites


The chained upstream proxy routes egress traffic through an external HTTP/HTTPS forward proxy via standard HTTP CONNECT tunnels. The configuration is lifecycle-server-wide and administrator-only; request environments cannot override proxy destinations, credentials, or custom CA bundles.


Prerequisites:


- Egress sidecar enabled by provisioning sandboxes with a `networkPolicy`.
- Server `[egress]` configuration set to `mode = "dns+nft"`.
- Transparent interception enabled via `credentialProxy.enabled=true` or `OPENSANDBOX_EGRESS_MITMPROXY_TRANSPARENT=true`.
- For Docker: `[docker] network_mode = "bridge"`.
- For Kubernetes: non-pooled AgentSandbox or BatchSandbox workloads.


WARNING


Transparent service-mesh sidecars (such as Envoy or Istio) injected into the same pod network namespace are unsupported because both layers intercept and rewrite outbound packets. Use the external chained upstream proxy hop instead.


## Docker and Kubernetes configuration examples


Configure the `[egress.upstream_proxy]` section in the lifecycle server configuration. For the complete configuration schema and field definitions, refer to the [Server Configuration Reference](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md#egress).


### Docker configuration


For a private proxy CA in Docker, `ca_cert_path` must reference an absolute POSIX path on the Docker daemon host. The file is bind-mounted read-only into the egress sidecar container only.

toml

```
[egress]
image = "opensandbox/egress:<version>"
mode = "dns+nft"

[egress.upstream_proxy]
url = "https://proxy.example.com:8443"
# Optional complete Proxy-Authorization value:
# authorization = "Basic <base64>"
ca_cert_path = "/etc/ssl/certs/proxy-ca.pem"
```


### Kubernetes configuration


For a private proxy CA in Kubernetes, `ca_secret_name` references a Secret in the sandbox namespace. The Secret must contain the fixed key `ca.crt`, which is projected read-only into the egress sidecar container.

toml

```
[egress]
image = "opensandbox/egress:<version>"
mode = "dns+nft"

[egress.upstream_proxy]
url = "https://proxy.example.com:8443"
# Optional complete Proxy-Authorization value:
# authorization = "Basic <base64>"
ca_secret_name = "upstream-proxy-ca"
```


## Traffic and security model


For a detailed overview of egress packet flows, see [/architecture/network/egress](https://open-sandbox.ai/architecture/network/egress).


1. **Resolution & Routing**: Under `dns+nft`, proxy hostnames are resolved by infrastructure DNS even under a deny-all policy. Egress reachability is enforced by dedicated nftables sets scoped strictly to the mitmproxy UID, proxy IP, and proxy port, isolating proxy traffic from sandbox dynamic allow sets.
2. **Protocol & Next Hop**: Both `http://` and `https://` proxy endpoints are supported. For HTTPS endpoints, SNI and server hostname validation are enforced. Configured CA bundles augment the system trust store and apply to all mitmproxy upstream TLS verifications.
3. **CONNECT Authority**: Intercepted TLS traffic uses the SNI or Host-derived FQDN for the CONNECT authority when available, falling back to `IP:port`. Direct dials are strictly refused when chaining is enabled to prevent silent bypass.
4. **Credential Isolation**: Business credentials from Credential Vault are injected into the inner target request, while `authorization` is attached exclusively as `Proxy-Authorization` on the outer CONNECT request. Neither value is written to logs. For secret management details, see [/guides/credential-vault](https://open-sandbox.ai/guides/credential-vault).
5. **Secret Exposure Bounds**: Proxy authorization values appear as literal environment variables inside the egress container and are visible via `docker inspect` or Kubernetes Pod specs. Restrict host and cluster inspection permissions accordingly. The authorization environment and CA mount are added only to the egress container, not the sandbox container.


## Runtime compatibility matrix


Compatibility reflects current upstream `main` only:


| Runtime / Platform | Support Status | Operational Constraints |
| --- | --- | --- |
| Docker (`runc`) | Supported | Requires `[docker] network_mode = "bridge"`; use `ca_cert_path` only when a private CA is required. |
| Kubernetes (`runc`) | Supported | Non-pooled AgentSandbox and BatchSandbox workloads; use `ca_secret_name` only when a private CA is required. |
| Kubernetes (`Kata`) | Supported | Accepted by egress validation; validate the selected RuntimeClass, CNI, and kernel in your deployment. |
| gVisor (`secure_runtime.type = "gvisor"`) | Rejected | Sandbox creation returns HTTP 400 because gVisor netstack lacks the required iptables nat redirect. |
| Kubernetes Pool Mode | Unsupported | Rejects per-request `networkPolicy`; cannot attach per-allocation egress sidecars. |
| Fast Sandbox | Unsupported | Current fast-sandbox profile rejects `networkPolicy` when `upstream_proxy` is set. |


## Protocol and streaming behavior


| Protocol / Traffic Type | Supported | Behavior & Constraints |
| --- | --- | --- |
| HTTP/1.1 and HTTP/2 application traffic | Yes | Mitmproxy can negotiate HTTP/2 with application targets. The upstream web-proxy hop uses HTTP/1 CONNECT; HTTP/2 CONNECT is not supported by mitmproxy 11.0.2. |
| Ports 80 & 443 | Yes | Always intercepted; Credential Vault binding applies to canonical ports 80/443. |
| Extra TCP Ports | Bounded | Intercepted when configured, but Credential Vault binding does not apply. |
| Streaming and large request bodies | Preserved with limits | Credential header injection occurs in `requestheaders` before body streaming. Body placeholder substitution is skipped for streamed bodies. |
| Server-Sent Events (SSE) | Caveat | Forced into streaming mode. Truncation can occur if origin closes with TCP RST; see [/guides/egress-sse-truncation](https://open-sandbox.ai/guides/egress-sse-truncation). |
| TLS pass-through | No | Non-empty `ignore_hosts`, `tcp_hosts`, or `udp_hosts` makes the upstream addon fail to load; no-SNI pass-through is refused at request time. |
| UDP and QUIC | No | These flows cannot use HTTP CONNECT and are refused rather than sent directly. |
| WebSocket (WSS) | Unverified | Dedicated chained-proxy WSS compatibility is not independently verified. |
| IPv6 Egress | Incomplete | Incomplete Kubernetes dual-stack support; `egress.disable_ipv6` defaults to `true`. |


The default-off experimental OSEP-0023 revision runtime has a narrower live HTTP/2 admission boundary: only the fixed-dependency direct/lazy path is wired, and configured chained upstream proxies remain rejected for that path. Existing HTTP/1 and legacy proxy behavior in the matrix above is unchanged. See the [HTTP/2 integration boundary](https://open-sandbox.ai/architecture/network/osep-0023-h2-integration) for drain semantics and incomplete client-migration and Linux acceptance.


## Deployment, rotation, and rollback


- **Application Bounds**: Proxy configuration changes apply only to newly created sandboxes. Existing sidecars retain their creation-time proxy settings.
- **Proxy or Authorization Rotation**: Update the lifecycle server configuration, restart the lifecycle server, then recreate affected sandboxes.
- **CA Rotation**: Update the Docker CA file or Kubernetes Secret. If its configured path or Secret name is unchanged, the lifecycle server does not need a restart, but affected sandboxes still need recreation. Recreating avoids relying on bind-mount or Secret `subPath` update behavior.
- **Rollback Procedure**: Remove the `[egress.upstream_proxy]` section, restart the lifecycle server, and recreate affected sandboxes. Existing sandboxes remain unchanged until they are recreated, and proxy failure never triggers an automatic direct fallback.


## Verification checklist


1. Confirm the lifecycle server starts with the new configuration; invalid URL, mode, and runtime-specific CA fields fail validation before sandbox creation.
2. Create a new sandbox with `networkPolicy` and transparent interception enabled.
3. Confirm the egress health endpoint returns `200 OK`; `503 mitmproxy not ready` means the interception process did not initialize.
4. Check startup logs for the `credential proxy: upstream proxy chaining enabled` message, without printing environment values.
5. From the sandbox, access an allowed HTTPS destination with normal certificate verification. Do not use `curl -k` or set `ssl_insecure`.
6. Confirm a denied destination stays denied and inspect the external proxy's telemetry for the expected FQDN CONNECT authority.
7. If Credential Vault is enabled, confirm the target receives the business credential while the forward proxy receives only `Proxy-Authorization`.


## Troubleshooting table


| Failure Category | Observed Symptoms | Root Cause & Resolution |
| --- | --- | --- |
| Config-load error | Server fails to start; configuration parse errors | Invalid proxy URL, non-absolute Docker CA path, or mixing Docker and Kubernetes CA settings. |
| Request 400 error | Sandbox creation rejected with HTTP 400 | Transparent interception is missing, `secure_runtime.type = "gvisor"` is selected, or Pool/Fast Sandbox is combined with per-request `networkPolicy`. |
| Pod or bind setup failure | Kubernetes Pod stays pending, or Docker container creation fails | The Kubernetes Secret/key is missing, or the Docker daemon cannot read the configured host path. Correct the administrator-managed source and recreate the sandbox. |
| Sidecar startup failure | Egress container restarts or fails readiness | Custom pass-through settings are incompatible, or the mounted CA bundle is malformed or unreadable. |
| Sidecar 503 error | Egress health checks return HTTP 503 | Mitmproxy has not initialized. Inspect sidecar startup logs; runtime proxy outages affect requests but do not by themselves make the local listener unready. |
| TLS / SAN failure | Handshake failure; certificate validation errors | Upstream proxy certificate SAN does not match proxy hostname, or missing custom CA bundle. |
| Proxy auth failure | Requests through the proxy fail; proxy telemetry reports 407 | Supply the complete, valid `authorization` value in server configuration and recreate the sandbox. |
| Direct-dial error | Logs contain `upstream proxy required: direct egress dial refused` | Expected fail-closed behavior for a flow that cannot be chained; do not bypass it by disabling TLS verification. |
| SSE / stream truncation | Streaming connection drops prematurely | Origin closed connection with TCP RST while unread bytes remained; review upstream gateway keep-alive settings. |


## Known limits and references


- **No Per-Request Proxy**: Proxy settings cannot be modified per request or through environment variables.
- **No Hot Reload**: Existing sandbox sidecars cannot reload proxy configurations dynamically.
- **No Dedicated OTLP Metrics**: There is no dedicated chained-proxy metric family; rely on egress health checks, DNS/nftables metrics, and proxy logs.
- **Runtime Scope**: No production certification is claimed for every Kata implementation, custom RuntimeClass, CNI, or kernel combination.
- **References**:
  - [Egress Architecture Specification](https://open-sandbox.ai/architecture/network/egress)
  - [Credential Vault Operations Guide](https://open-sandbox.ai/guides/credential-vault)
  - [Server-Sent Events Truncation Guide](https://open-sandbox.ai/guides/egress-sse-truncation)
  - [Server Configuration Reference](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md#egress)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/egress-upstream-proxy.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/secure-access`

Return to top

# Secure Access
## Requirements ​
## How It Works ​
## Static Header Token ​
*GetEndpoint returns an opaque SecureAccessToken. Clients attach it as:*

## Signed Short-Lived URLs ​
## Server Configuration ​
## Enabling It ​
## Calling a Secured Endpoint ​
## Errors ​
## Notes ​
## See Also ​












Secure Access is OpenSandbox's inbound access control for sandbox endpoints. When enabled on a sandbox, the ingress gateway (and the server proxy path) require every caller to prove they are authorized before HTTP or WebSocket traffic reaches the sandbox.


Its counterparts:


- [Credential Vault](https://open-sandbox.ai/guides/credential-vault) — protects **outbound** requests.
- [Secure Container Runtime](https://open-sandbox.ai/guides/secure-container) — isolates the **workload**.


## Requirements


- Kubernetes runtime (Docker rejects `secureAccess: true` with `400`).
- `[ingress] mode = "gateway"`.
- Signed URLs additionally require `[ingress.secure_access]` with at least one signing key.


## How It Works


![Secure Access request flow](https://open-sandbox.ai/assets/secure-access.CB0-anbK.svg)


On the **control plane**, creating a sandbox with `secureAccess: true` and calling `GetEndpoint` yields a per-sandbox opaque `SecureAccessToken`. Passing `?expires=<unix_seconds>` also mints a signed, time-limited routing token using the active key under `[ingress.secure_access]`.


On the **data plane**, the ingress gateway evaluates two mechanisms in a fixed order:


1. **Header present** → constant-time compare against `SecureAccessToken`. Mismatch returns `401` immediately; there is **no** fallback to the signed-URL branch.
2. **Header absent** → parse the signed token, check `now ≤ expires`, verify the signature.


Requests that pass either check are forwarded upstream with the header or signed prefix stripped, so the workload never sees the credential.


## Static Header Token


`GetEndpoint` returns an opaque `SecureAccessToken`. Clients attach it as:

http

```
OpenSandbox-Secure-Access: <token>
```


SDKs pick this header up from the endpoint response automatically, so application code usually does not touch it.


## Signed Short-Lived URLs


Mint a signed URL by adding `?expires=<unix_seconds>` (decimal `uint64` epoch seconds, **not** milliseconds):


```
GET /sandboxes/{sandboxId}/endpoints/{port}?expires=<unix_seconds>
```


The returned routing token has the shape:


```
{sandbox_id}-{port}-{expires_b36}-{signature}
```


where `expires_b36` is base-36 seconds and `signature` is 8 hex digits plus the 1-character `key_id` that signed it. The gateway accepts it in three routing modes:


| Mode | Where the token appears |
| --- | --- |
| wildcard | Host: `{token}.<parent>` |
| header | Value of the sandbox routing header |
| uri | Path prefix: `/{sandbox_id}/{port}/{expires_b36}/{signature}/…` |


Use signed URLs to hand out shareable, time-limited endpoints without exposing the static token.


## Server Configuration


Signed URLs need signing keys; the static header token does not.

toml

```
# ~/.sandbox.toml
[ingress]
mode = "gateway"

[ingress.gateway]
# Wildcard mode requires a wildcard address (e.g. *.sandbox.example.com);
# header and uri modes take a plain host (e.g. sandbox.example.com).
address = "*.sandbox.example.com"

[ingress.gateway.route]
mode = "wildcard"   # or "header" or "uri"

[ingress.secure_access]
active_key = "a"    # 1 char [0-9a-z], must exist in keys

[[ingress.secure_access.keys]]
key_id = "a"
key = "<base64-encoded-secret>"   # raw base64, no "base64:" prefix
```


The `opensandbox-server` Helm chart exposes the same shape under `server.gateway.secureAccess` and wires the keys into both the server and the ingress gateway.


To keep key material out of the config file, the server also accepts the `OPENSANDBOX_SECURE_ACCESS_KEYS` (`a=<base64-secret>[,b=...]`) and `OPENSANDBOX_SECURE_ACCESS_ACTIVE_KEY` (`a`) environment variables, which override the TOML block; the chart's `server.gateway.secureAccess.existingSecret` option sources them from a Secret.


**Key rotation.** Add a new key entry, deploy, then flip `active_key`. Verification loads every configured key, so tokens signed by older keys stay valid until you remove them — keep old entries until the longest possible token lifetime has elapsed.


## Enabling It


Set `secureAccess: true` on create. SDK equivalents: Python `secure_access=True`, JS/TS `secureAccess: true`, C# `SecureAccess = true`.

bash

```
curl -X POST http://localhost:8080/v1/sandboxes \
  -H "Content-Type: application/json" \
  -d '{
    "image": {"uri": "python:3.11"},
    "resourceLimits": {"cpu": "500m", "memory": "512Mi"},
    "entrypoint": ["python", "/app/main.py"],
    "secureAccess": true
  }'
```


## Calling a Secured Endpoint


With the static header token:

bash

```
# Fetch endpoint; the response carries OpenSandbox-Secure-Access.
curl -s http://localhost:8080/v1/sandboxes/${SANDBOX_ID}/endpoints/8080

curl -H "OpenSandbox-Secure-Access: ${TOKEN}" \
  https://${SANDBOX_ID}-8080.sandbox.example.com/
```


With a signed URL (valid for one hour):

bash

```
EXPIRES=$(( $(date +%s) + 3600 ))
curl -s "http://localhost:8080/v1/sandboxes/${SANDBOX_ID}/endpoints/8080?expires=${EXPIRES}"
# → https://{sandbox_id}-8080-{expires_b36}-{signature}.sandbox.example.com/
```


## Errors


| Code | Cause |
| --- | --- |
| `400` | `secureAccess: true` on Docker; malformed `expires` or routing token; invalid `expires_b36` / `port` / `signature`. |
| `401` | Header mismatch; signed URL expired; bad signature; unknown key ID; secure access required but no credential presented. |


Omitting `expires` on `GetEndpoint` is not a `400` — it returns the unsigned response, still carrying the static `SecureAccessToken`.


## Notes


- Enforcement covers both ingress gateway and the server proxy path (`/v1/sandboxes/{id}/proxy/...`), HTTP and WebSocket.
- The gateway strips `OpenSandbox-Secure-Access` and any signed URI prefix before forwarding.
- In URI mode, path segments that resemble `expires_b36/signature` are only interpreted as a signed prefix when the sandbox actually has secure access enabled; otherwise the full path is forwarded unchanged.
- Secure Access is independent of the execd access token (`X-EXECD-ACCESS-TOKEN`) and Credential Vault; all can be used together.


## See Also


- [Credential Vault](https://open-sandbox.ai/guides/credential-vault)
- [Secure Container Runtime](https://open-sandbox.ai/guides/secure-container)
- [Ingress component](https://open-sandbox.ai/architecture/network/ingress)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/secure-access.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/secure-container`

Return to top

# Secure Container Runtime Guide
## Table of Contents ​
## Overview ​
## Server Configuration ​
*Edit ~/.sandbox.toml:*

## Multiple Runtime Profiles on Kubernetes ​
## Docker Mode ​
*Use the runsc install command to automatically configure Docker daemon:*

*Or manually edit /etc/docker/daemon.json:*

*Edit /etc/docker/daemon.json to register Kata as a runtime:*

## Kubernetes Mode ​
*Edit /etc/containerd/config.toml:*

*Follow the official Kata Containers installation guide.*

## User Guide ​
## Administrator Guide ​
## Troubleshooting and Best Practices ​











This guide explains how to use secure container runtimes with OpenSandbox to provide hardware-level isolation for executing untrusted AI-generated code.


## Table of Contents


- [Overview](https://open-sandbox.ai/guides/secure-container#overview)
- [Server Configuration](https://open-sandbox.ai/guides/secure-container#server-configuration)
- [Multiple Runtime Profiles on Kubernetes](https://open-sandbox.ai/guides/secure-container#multiple-runtime-profiles-on-kubernetes)
- [Docker Mode](https://open-sandbox.ai/guides/secure-container#docker-mode)
- [Kubernetes Mode](https://open-sandbox.ai/guides/secure-container#kubernetes-mode)
- [User Guide](https://open-sandbox.ai/guides/secure-container#user-guide)
- [Administrator Guide](https://open-sandbox.ai/guides/secure-container#administrator-guide)
- [Troubleshooting and Best Practices](https://open-sandbox.ai/guides/secure-container#troubleshooting-and-best-practices)


---


## Overview


### What are Secure Container Runtimes?


Secure container runtimes provide stronger isolation than the standard runc runtime used by Docker and containerd. They add additional security layers through different mechanisms:


| Runtime | Isolation Mechanism | Startup Overhead | Memory Overhead | Best For |
| --- | --- | --- | --- | --- |
| **runc** (default) | Process-level cgroups | ~0ms | Minimal | Trusted workloads, local development |
| **gVisor** | User-space kernel (syscall interception) | ~10-50ms | ~50MB | General workloads with low overhead |
| **Kata (QEMU)** | Full VM with QEMU hypervisor | ~500ms | ~20-50MB | Maximum compatibility and isolation |
| **Kata (Firecracker)** | MicroVM with Firecracker hypervisor | ~125ms | ~5MB | High density, minimal footprint |
| **Kata (CLH)** | Cloud Hypervisor | ~200ms | ~10-20MB | Balanced performance and isolation |


### Why Use Secure Runtimes?


OpenSandbox is designed to execute untrusted code generated by AI models (Claude, GPT-4, Gemini, etc.). Secure runtimes provide:


1. **Container Escape Protection**: Prevents malicious code from breaking out of the container
2. **Kernel-Level Isolation**: Each sandbox gets its own kernel context
3. **Multi-Tenant Safety**: Different users' sandboxes are strongly isolated
4. **Compliance**: Meets security requirements for regulated industries


### Supported Runtime Types


OpenSandbox supports the following secure runtime types through server-level configuration:


- `"gvisor"` - Google gVisor with runsc
- `"kata"` - Kata Containers with QEMU hypervisor (default)
- `"firecracker"` - Kata Containers with Firecracker hypervisor
- `""` (empty) - Standard runc (default, no secure runtime)


### Key Design Principle


**Server-Level Configuration**: The secure runtime is configured once at the server level by administrators. All sandboxes on that server transparently use the configured runtime. SDK users and API callers require **no code changes**.


---


## Server Configuration


Secure runtimes are configured through the `~/.sandbox.toml` configuration file. The server validates the configured runtime at startup and will refuse to start if the runtime is unavailable.


### Configuration File


Edit `~/.sandbox.toml`:

toml

```
[runtime]
type = "docker"  # or "kubernetes"
execd_image = "opensandbox/execd:latest"

# Secure container runtime configuration
# When enabled, ALL sandboxes on this server use the specified runtime
[secure_runtime]
# Runtime type: "", "gvisor", "kata", "firecracker"
type = ""

# Docker mode: OCI runtime name (e.g., "runsc" for gVisor, "kata-runtime" for Kata)
# Required when runtime.type = "docker" and type is not empty
docker_runtime = "runsc"

# Kubernetes mode: RuntimeClass name (e.g., "gvisor", "kata-qemu", "kata-fc")
# Required when runtime.type = "kubernetes" and type is not empty
k8s_runtime_class = "gvisor"
```


### Configuration Examples


#### Example 1: gVisor on Docker

toml

```
[runtime]
type = "docker"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "gvisor"
docker_runtime = "runsc"
k8s_runtime_class = "gvisor"
```


#### Example 2: Kata Containers on Kubernetes

toml

```
[runtime]
type = "kubernetes"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "kata"
docker_runtime = "kata-runtime"
k8s_runtime_class = "kata-qemu"
```


#### Example 3: Kata + Firecracker on Kubernetes

toml

```
[runtime]
type = "kubernetes"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "firecracker"
docker_runtime = ""  # Not supported in Docker mode
k8s_runtime_class = "kata-fc"
```


### Startup Validation


When the server starts, it automatically validates that the configured secure runtime is available:

bash

```
$ opensandbox-server
INFO     Validating secure runtime for Docker backend
INFO     Docker OCI runtime 'runsc' is available: {...}
INFO     Application startup complete.
```


If the runtime is not available, the server will refuse to start with a clear error message:


```
ERROR    Configured Docker runtime 'runsc' is not available.
        Available runtimes: runc.
        Please install and configure it in /etc/docker/daemon.json.
```


---


## Multiple Runtime Profiles on Kubernetes


`[secure_runtime]` is a server startup setting, not a sandbox creation field. One Lifecycle Server process therefore applies one runtime profile to every template-mode sandbox it creates. To offer runc and a stronger runtime such as Kata in the same Kubernetes cluster, run one independently addressed Lifecycle Server release per profile and route each client to the appropriate Server API.


| Server profile | API Service | `[secure_runtime]` | Resulting Pod field |
| --- | --- | --- | --- |
| Standard | `opensandbox-runc` | `type = ""` | `runtimeClassName` omitted |
| Isolated | `opensandbox-kata` | `type = "kata"`, `k8s_runtime_class = "kata-qemu"` | `runtimeClassName: kata-qemu` |


Both profiles can use the same OpenSandbox controller and sandbox workload namespace. The RuntimeClass should carry its own scheduling constraints so Kata Pods land only on nodes where Kata is installed.


Resource names must be unique


The Server chart defaults `fullnameOverride` to `opensandbox-server`, so changing only the Helm release name is not sufficient: two default releases would render the same Deployment, ServiceAccount, RBAC, ConfigMap, and Service names. Set a different `fullnameOverride` for every profile. The standalone ingress-gateway chart also defaults to a fixed `fullnameOverride` (`opensandbox-ingress-gateway`); give each gateway a distinct value, such as `opensandbox-runc-gateway` and `opensandbox-kata-gateway`. Its ClusterRole and ClusterRoleBinding names derive from this value and must be unique across the cluster. Separate control-plane namespaces alone do not prevent those RBAC collisions.


### Deploy two Server profiles


Create the `opensandbox` workload namespace and one control-plane namespace per profile. Create the API-key Secrets in their corresponding control-plane namespaces as described in [Kubernetes Deployment](https://open-sandbox.ai/deployment/#configure-api-authentication). Use `opensandbox-runc-api-key` in `opensandbox-runc-system` and `opensandbox-kata-api-key` in `opensandbox-kata-system` to match the references below.


Use the values files below for both releases. They replace `configToml` in full, including the `[egress]` image and mode needed for sandbox network policies. The examples use direct sandbox endpoints: clients must be able to reach the sandbox Pod IPs inside the cluster. For external clients, configure a gateway as described below. Match the execd and egress image tags to the checked-out release.

values-runc.yaml values-kata.yaml yaml

```
fullnameOverride: opensandbox-runc
namespaceOverride: opensandbox-runc-system

server:
  replicaCount: 1
  gateway:
    enabled: false
  env:
    - name: OPENSANDBOX_SERVER_API_KEY
      valueFrom:
        secretKeyRef:
          name: opensandbox-runc-api-key
          key: api-key

configToml: |
  [server]
  host = "0.0.0.0"
  port = 80
  api_key = ""

  [log]
  level = "INFO"

  [runtime]
  type = "kubernetes"
  execd_image = "sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/execd:release-1.1.1-rc.1"

  [kubernetes]
  namespace = "opensandbox"
  workload_provider = "batchsandbox"

  [egress]
  image = "sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/egress:release-1.1.1-rc.1"
  mode = "dns+nft"

  [secure_runtime]
  type = ""
```

yaml

```
fullnameOverride: opensandbox-kata
namespaceOverride: opensandbox-kata-system

server:
  replicaCount: 1
  gateway:
    enabled: false
  env:
    - name: OPENSANDBOX_SERVER_API_KEY
      valueFrom:
        secretKeyRef:
          name: opensandbox-kata-api-key
          key: api-key

configToml: |
  [server]
  host = "0.0.0.0"
  port = 80
  api_key = ""

  [log]
  level = "INFO"

  [runtime]
  type = "kubernetes"
  execd_image = "sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/execd:release-1.1.1-rc.1"

  [kubernetes]
  namespace = "opensandbox"
  workload_provider = "batchsandbox"

  [egress]
  image = "sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/egress:release-1.1.1-rc.1"
  mode = "dns+nft"

  [secure_runtime]
  type = "kata"
  k8s_runtime_class = "kata-qemu"
```


From an OpenSandbox checkout with the base CRDs and controller already installed, install both profiles using the Server chart at `manifests/charts/server`. The chart supplies its matching Server image tag by default:

bash

```
kubectl create namespace opensandbox --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install opensandbox-runc manifests/charts/server \
  --namespace opensandbox-runc-system \
  --create-namespace \
  --values values-runc.yaml

helm upgrade --install opensandbox-kata manifests/charts/server \
  --namespace opensandbox-kata-system \
  --create-namespace \
  --values values-kata.yaml
```


Expose the two Services under different internal DNS names, hostnames, or API gateway routes. Do not put them behind an unqualified round-robin route: runtime selection is made by choosing the Server endpoint. Keep subsequent get, renew, pause, resume, snapshot, and delete calls on the same profile endpoint that created the sandbox.


### Gateway access


`server.gateway.enabled=true` only makes the Server announce a gateway address; it does not deploy the gateway. Install one standalone `manifests/charts/ingress-gateway` release per profile with the distinct `fullnameOverride` values above. Set `gateway.dataplaneNamespace` to that profile's workload namespace (`opensandbox` in these examples).


Expose each gateway through its own client-reachable host, and set the matching Server's `server.gateway.host` to that host. Match `server.gateway.gatewayRouteMode` to the gateway's `gateway.gatewayRouteMode`. If signed access is enabled, configure the same signing key ring on each Server/gateway pair as described in [Secure Access](https://open-sandbox.ai/guides/secure-access).


For example, install the two gateways and update the existing Server releases:

bash

```
helm upgrade --install opensandbox-runc-gateway manifests/charts/ingress-gateway \
  --namespace opensandbox-runc-system \
  --set namespaceOverride=opensandbox-runc-system \
  --set fullnameOverride=opensandbox-runc-gateway \
  --set gateway.dataplaneNamespace=opensandbox \
  --set gateway.gatewayRouteMode=header

helm upgrade --install opensandbox-kata-gateway manifests/charts/ingress-gateway \
  --namespace opensandbox-kata-system \
  --set namespaceOverride=opensandbox-kata-system \
  --set fullnameOverride=opensandbox-kata-gateway \
  --set gateway.dataplaneNamespace=opensandbox \
  --set gateway.gatewayRouteMode=header

helm upgrade --install opensandbox-runc manifests/charts/server \
  --namespace opensandbox-runc-system --values values-runc.yaml \
  --set server.gateway.enabled=true \
  --set-string server.gateway.host=runc-gateway.example.com \
  --set server.gateway.gatewayRouteMode=header

helm upgrade --install opensandbox-kata manifests/charts/server \
  --namespace opensandbox-kata-system --values values-kata.yaml \
  --set server.gateway.enabled=true \
  --set-string server.gateway.host=kata-gateway.example.com \
  --set server.gateway.gatewayRouteMode=header
```


The gateway chart uses `namespaceOverride` for its resource namespace; setting only Helm's `--namespace` does not change that default. The gateway Services above are `ClusterIP` by default. Expose them through your cluster's ingress or load balancer and replace the `*.example.com` hosts with those reachable addresses before running the Server upgrades. A gateway host routes sandbox traffic; clients still use the corresponding Server API endpoint for lifecycle operations.


### Verify profile selection


Create one sandbox through each Server, then inspect the generated BatchSandbox Pod template:

bash

```
kubectl get batchsandbox --namespace opensandbox <runc-sandbox-id> \
  -o jsonpath='{.spec.template.spec.runtimeClassName}'
# Empty output: the cluster's default OCI runtime is used.

kubectl get batchsandbox --namespace opensandbox <kata-sandbox-id> \
  -o jsonpath='{.spec.template.spec.runtimeClassName}'
# kata-qemu
```


Pool mode


Pool-backed sandboxes reuse Pods that already exist, so the Server's `[secure_runtime]` setting does not rewrite their runtime. Create a separate Pool per profile, set `spec.template.spec.runtimeClassName` on each Pool explicitly, and expose only the matching `poolRef` through that profile.


Operational boundary


Multiple Server profiles provide deterministic runtime selection, not a security or tenancy boundary. Servers targeting the same workload namespace can observe the same Kubernetes resources. Use separate workload namespaces (and suitably scoped RBAC or separate clusters) when profiles must also be isolated from one another. Separate gateway names and hosts avoid resource and routing collisions; they do not restrict access to workloads in a shared namespace.


---


## Docker Mode


Docker mode is fully supported for secure container runtimes.


### Prerequisites


- Docker daemon installed and running
- Secure runtime installed on the host


### gVisor Setup for Docker


#### Step 1: Install gVisor runsc


For Docker mode, you only need to install the **runsc** OCI runtime:

bash

```
# Ubuntu/Debian
curl -fsSL https://gvisor.dev/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/gvisor-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] https://storage.googleapis.com/gvisor/releases release main" | \
  sudo tee /etc/apt/sources.list.d/gvisor.list
sudo apt-get update && sudo apt-get install -y runsc

# Verify installation
runsc --version
```


> **Note**: For Docker mode, only `runsc` is required. The `containerd-shim-runsc-v1` is only needed for Kubernetes/containerd.
>
>
>
> **Reference**: See [gVisor Installation Guide](https://gvisor.dev/docs/user_guide/install/) for other distributions and installation methods.


#### Step 2: Configure Docker daemon


Use the `runsc install` command to automatically configure Docker daemon:

bash

```
sudo runsc install
```


Or manually edit `/etc/docker/daemon.json`:

json

```
{
  "runtimes": {
    "runsc": {
      "path": "/usr/bin/runsc",
      "runtimeArgs": [
        "--platform=systrap",
        "--network=host",
        "--overlay2=none"
      ]
    }
  }
}
```


Docker snapshots require `--overlay2=none`


runsc normally keeps root filesystem changes in its own `root:self` overlay. Docker cannot include those changes in `docker commit`, so a Docker-backed OpenSandbox snapshot can report success while restoring only the original image. Keep `--overlay2=none` in the runtime arguments when you use snapshot, fork, or restore workflows. This makes sandbox writes visible to Docker's storage driver and therefore available to the snapshot image.


Existing runsc installations created without this argument must update `daemon.json` and restart Docker before taking snapshots. See gVisor's [filesystem documentation](https://gvisor.dev/docs/user_guide/filesystem/) for the root filesystem overlay behavior.


Restart Docker:

bash

```
sudo systemctl restart docker
```


> **Reference**: See [gVisor Docker Quick Start](https://gvisor.dev/docs/user_guide/quick_start/docker/) for more details.


#### Step 3: Configure OpenSandbox Server


Edit `~/.sandbox.toml`:

toml

```
[runtime]
type = "docker"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "gvisor"
docker_runtime = "runsc"
```


#### Step 4: Start Server and Verify

bash

```
opensandbox-server
```


Create a test sandbox:

bash

```
curl -X POST http://localhost:8080/v1/sandboxes \
  -H "Content-Type: application/json" \
  -d '{
    "image": {"uri": "python:3.11"},
    "timeout": 3600,
    "resourceLimits": {"cpu": "500m", "memory": "512Mi"},
    "entrypoint": ["python", "-u", "-c", "import time\nwhile True: print('hello from gVisor!'); time.sleep(1)"],
    "metadata": {
      "name": "gvisor-docker-sandbox"
    }
  }'
```


Verify the runtime:

bash

```
docker ps --format "{{.ID}}\t{{.Image}}\t{{.Names}}"
docker inspect <container_id> | grep -A2 Runtime
# Expected output:
# "Runtime": "runsc",
```


### Kata Containers Setup for Docker


#### System Requirements


Kata Containers requires hardware virtualization support. Verify your system meets the following requirements:


**Hardware Virtualization Support:**

bash

```
# Check if CPU supports hardware virtualization (VT-x for Intel, AMD-V for AMD)
lscpu | grep Virtualization
# Expected output: Virtualization: VT-x (Intel) or AMD-V (AMD)

# Alternatively on Intel
grep -E --color=auto 'vmx|svm' /proc/cpuinfo
# Expected: vmx (Intel) or svm (AMD) flags present
```


**KVM Module:**

bash

```
# Check if KVM module is loaded
lsmod | grep kvm
# Expected: kvm_intel (Intel) or kvm_amd (AMD)

# If not loaded, load KVM module
sudo modprobe kvm_intel  # For Intel
# or
sudo modprobe kvm_amd    # For AMD
```


**Kernel Requirements:**


- Linux kernel 5.10 or later recommended
- KVM enabled in kernel config


**Docker Requirements:**


- Docker 20.10 or later
- `/etc/docker/daemon.json` configured for Kata runtime


#### Installation


Download and install Kata Containers static binaries from GitHub releases:

bash

```
# Find the latest release at https://github.com/kata-containers/kata-containers/releases
KATA_VERSION="3.27.0"
wget https://github.com/kata-containers/kata-containers/releases/download/${KATA_VERSION}/kata-static-${KATA_VERSION}-amd64.tar.zst

# Extract to root directory - Kata will be installed in /opt/kata
zstd -d kata-static-${KATA_VERSION}-amd64.tar.zst
tar -xvf kata-static-${KATA_VERSION}-amd64.tar -C /

# Create symbolic links for PATH access
sudo ln -sf /opt/kata/bin/kata-runtime /usr/local/bin/kata-runtime
sudo ln -sf /opt/kata/bin/containerd-shim-kata-v2 /usr/local/bin/containerd-shim-kata-v2

# Verify installation
kata-runtime --version
```


#### Configure Docker Daemon


Edit `/etc/docker/daemon.json` to register Kata as a runtime:

json

```
{
  "default-runtime": "runc",
  "runtimes": {
    "kata": {
      "runtimeType": "io.containerd.kata.v2"
    }
  }
}
```


Restart Docker to apply changes:

bash

```
sudo systemctl restart docker

# Verify Kata is available in Docker
docker info | grep -A5 Runtimes
# Expected output should include "io.containerd.runc.v2 kata"
```


#### Configure OpenSandbox Server


Edit `~/.sandbox.toml`:

toml

```
[runtime]
type = "docker"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "kata"
docker_runtime = "kata"
```


#### Verify Installation


**Test with OpenSandbox API**


Create a sandbox and verify it's running in a VM by checking the kernel:

bash

```
# Create a test sandbox
curl --location 'http://127.0.0.1:8080/v1/sandboxes' \
  --header 'Content-Type: application/json' \
  --data '{
    "image": {"uri": "ubuntu:latest"},
    "timeout": 3600,
    "resourceLimits": {"cpu": "500m", "memory": "512Mi"},
    "entrypoint": ["/bin/bash", "-c", "while true; do uname -a; sleep 1; done"],
    "metadata": {
      "name": "kata-sandbox"
    }
  }'
```


Check the container's kernel to verify VM isolation:

bash

```
# Get the container ID
docker ps | grep kata-sandbox

# Check the kernel inside the container (should be different from host)
docker exec <container_id> uname -a
# Expected output: Linux <hostname> 5.10.x-generic #x86_64 ... (Kata VM kernel)

# Compare with host kernel
uname -a
# Host kernel might be different version or have different hostname
```


**Key Indicators of Kata VM:**


- Container runs in a separate kernel with different hostname
- Kernel version is typically `5.10.x` (Kata's guest kernel)
- Host process list shows `qemu-system-x86_64` or similar hypervisor process


---


## Kubernetes Mode


Kubernetes mode supports secure runtimes through RuntimeClass resources.


### Prerequisites


- Kubernetes cluster with containerd runtime
- Secure runtime installed on all nodes
- RuntimeClass CRDs created


### gVisor Setup for Kubernetes


#### Step 1: Install gVisor Components on All Nodes


For Kubernetes with containerd, you need to install **two** components:


1. **runsc** - the gVisor OCI runtime
2. **containerd-shim-runsc-v1** - the containerd shim for gVisor

bash

```
# On each node - Ubuntu/Debian
curl -fsSL https://gvisor.dev/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/gvisor-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] https://storage.googleapis.com/gvisor/releases release main" | \
  sudo tee /etc/apt/sources.list.d/gvisor.list
sudo apt-get update

# Install both gVisor components
sudo apt-get install -y runsc containerd-shim-runsc-v1

# Verify installation
runsc --version
containerd-shim-runsc-v1 --version
```


> **Reference**: See [gVisor Installation Guide](https://gvisor.dev/docs/user_guide/containerd/configuration/) for complete installation instructions and other distributions.


#### Step 2: Configure containerd


Edit `/etc/containerd/config.toml`:

toml

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runsc]
          runtime_type = "io.containerd.runsc.v1"
          [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runsc.options]
            TypeUrl = "io.containerd.runsc.v1.options"
            ConfigPath = "/etc/containerd/runsc.toml"
```

bash

```
sudo tee /etc/containerd/runsc.toml > /dev/null <<'EOF'
[runsc]
  platform = "ptrace"
EOF
```


Restart containerd:

bash

```
sudo systemctl restart containerd
```


#### Step 3: Create RuntimeClass CRD

yaml

```
# gvisor-runtimeclass.yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
scheduling:
  nodeSelector:
    kubernetes.io/arch: amd64
```

bash

```
kubectl apply -f gvisor-runtimeclass.yaml
```


#### Step 4: Configure OpenSandbox Server


Edit `~/.sandbox.toml`:

toml

```
[runtime]
type = "kubernetes"
execd_image = "opensandbox/execd:latest"

[secure_runtime]
type = "gvisor"
k8s_runtime_class = "gvisor"
```


#### Step 5: Verify Installation

bash

```
# Test the RuntimeClass
kubectl run test-gvisor --restart=Never --image=hello-world --runtime-class=gvisor
kubectl logs test-gvisor
kubectl delete pod test-gvisor
```


### Kata Containers Setup for Kubernetes


#### Step 1: Install Kata Containers


Follow the [official Kata Containers installation guide](https://github.com/kata-containers/kata-containers/blob/main/tools/packaging/kata-deploy/helm-chart/README.md).


Quick installation using Helm:

bash

```
# Install kata-deploy which will set up Kata Containers via DaemonSet
helm install kata-deploy "oci://ghcr.io/kata-containers/kata-deploy-charts/kata-deploy" --version "3.27.0" --namespace kube-system --create-namespace

# Wait for kata-deploy pods to be ready
kubectl wait --for=condition=ready pod -l name=kata-deploy -n kube-system --timeout=300s
```


> **Note**: The `kata-deploy` DaemonSet will automatically configure containerd on all nodes. Manual containerd configuration is not required when using kata-deploy.


#### Step 2: Verify Installation


Check that Kata Containers is installed and RuntimeClasses are created:

bash

```
# Check RuntimeClasses
kubectl get runtimeclass

# Expected output:
# NAME         HANDLER     AGE
# kata         kata-qemu   10m
# kata-qemu    kata-qemu   10m
# kata-clh     kata-clh    10m
# kata-fc      kata-fc     10m

# Test Kata with a simple pod
kubectl run test-kata --restart=Never --image=hello-world --runtime-class=kata-qemu
kubectl logs test-kata
kubectl delete pod test-kata
```


### Creating Pools for Different Runtimes (Optional)


When using Pool CRDs for pre-warmed sandboxes, create separate pools for each runtime type:

yaml

```
# gvisor-pool.yaml
apiVersion: sandbox.opensandbox.io/v1alpha1
kind: Pool
metadata:
  name: gvisor-pool
  labels:
    runtime: gvisor
spec:
  template:
    spec:
      runtimeClassName: gvisor
      containers:
        - name: sandbox-container
          image: opensandbox/code-interpreter:v1.1.0
  capacitySpec:
    bufferMax: 10
    bufferMin: 2
    poolMax: 20
    poolMin: 5
```


---


## User Guide


This section is for AI application developers using OpenSandbox.


### No Code Changes Required


**Important**: The secure runtime is configured at the server level. Your code does not need to change.


Simply create a sandbox using the OpenSandbox Lifecycle API - the server automatically applies the configured secure runtime:


**Create a test sandbox:**

bash

```
curl -X POST http://localhost:8080/v1/sandboxes \
  -H "Content-Type: application/json" \
  -d '{
    "image": {"uri": "python:3.11"},
    "timeout": 3600,
    "resourceLimits": {"cpu": "500m", "memory": "512Mi"},
    "entrypoint": ["python", "-u", "-c", "import time\nwhile True: print(\"hello from secure sandbox!\"); time.sleep(1)"],
    "metadata": {
      "name": "my-secure-sandbox"
    }
  }'
```


**Response:**

json

```
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "running"
}
```


The sandbox will automatically use the secure runtime configured on the server (gVisor, Kata, or runc).


### How It Works


1. **Administrator** configures the secure runtime in `~/.sandbox.toml`
2. **Server** validates the runtime at startup
3. **Server** automatically injects the runtime into each sandbox:
  - Docker mode: Adds `runtime` to HostConfig
  - Kubernetes mode: Adds `runtimeClassName` to Pod spec4. **User** creates sandboxes via API - no runtime parameter needed


### Verifying Runtime Isolation


After creating a sandbox, verify the runtime being used:


**Docker mode:**

bash

```
docker ps --format "{{.ID}}\t{{.Image}}\t{{.Names}}"
docker inspect <container_id> | grep -A2 Runtime
# Expected output for gVisor:
# "Runtime": "runsc",
```


**Kubernetes mode:**

bash

```
kubectl get pod <pod-name> -o jsonpath='{.spec.runtimeClassName}'
# Expected output for gVisor:
# gvisor
```


---


## Administrator Guide


This section is for platform operators and SREs managing secure runtime infrastructure.


### Prerequisites


Secure runtimes must be installed and configured on your infrastructure **before** configuring OpenSandbox. OpenSandbox does not install runtimes automatically.


### Installation Summary


| Runtime | Docker | Kubernetes |
| --- | --- | --- |
| gVisor | Install runsc → Configure daemon.json | Install runsc → Configure containerd → Create RuntimeClass |
| Kata (QEMU) | Install kata-runtime → Configure daemon.json | Install Kata → Configure containerd → Create RuntimeClass |
| Kata (Firecracker) | Not supported | Install Kata → Configure containerd → Create RuntimeClass |


### Configuration Validation


The server validates secure runtime configuration at startup:


1. **Docker mode**: Checks if the runtime exists in Docker daemon's runtime list
2. **Kubernetes mode**: Checks if the RuntimeClass exists in the cluster


If validation fails, the server refuses to start with a clear error message.


### Security Best Practices


1. **Default to gVisor**: Provides good security with acceptable performance for most workloads
2. **Use Kata for Untrusted Code**: Maximum isolation for completely unknown code
3. **Regular Updates**: Keep runtimes updated for security patches
4. **Test Compatibility**: Validate your workloads with the chosen runtime before production
5. **Monitor Resources**: Secure runtimes have higher memory overhead


### Runtime Selection Guidelines


| Use Case | Recommended Runtime | Reasoning |
| --- | --- | --- |
| Development/Testing | runc (default) | Fastest startup, lowest overhead |
| Production AI Code Execution | gVisor | Good balance of security and performance |
| High-Security Requirements | Kata (QEMU) | Maximum isolation, full compatibility |
| High-Density Multi-Tenant | Kata (Firecracker) | Minimal memory overhead per sandbox |
| Untrusted Network Code | gVisor or Kata | Syscall filtering prevents network attacks |


---


## Troubleshooting and Best Practices


### Common Issues


#### 1. Runtime Not Found (Docker)


**Error**: `Configured Docker runtime 'runsc' is not available.`


**Solution**: Ensure the runtime is configured in `/etc/docker/daemon.json` and Docker has been restarted:

bash

```
sudo systemctl restart docker
docker info | grep -A5 Runtimes
```


#### 2. RuntimeClass Not Found (Kubernetes)


**Error**: `RuntimeClass 'gvisor' does not exist.`


**Solution**: Create the RuntimeClass CRD:

bash

```
kubectl get runtimeclass
kubectl apply -f gvisor-runtimeclass.yaml
```


#### 3. Syscall Compatibility Issues


**Error**: Container exits with code 1, no logs


**Cause**: gVisor doesn't implement all syscalls. Some applications may not be compatible.


**Solution**: Check the [gVisor compatibility guide](https://gvisor.dev/docs/user_guide/compatibility/). Try using Kata (QEMU) which has better compatibility.


#### 4. Pod Stuck in ContainerCreating


**Cause**: RuntimeClass handler not configured on the node.


**Solution**: Verify containerd configuration:

bash

```
# On the node
sudo containerd config dump
sudo systemctl restart containerd
```


#### 5. Egress Sidecar Incompatible with gVisor


**Error**: Sandbox pods CrashLoopBackOff with egress container log:


```
iptables: Failed to initialize nft: Protocol not supported
```


Or with iptables-legacy:


```
iptables v1.8.9 (legacy): can't initialize iptables table 'nat': Table does not exist (do you need to insmod?)
```


**Cause**: gVisor's netstack implements the `filter` and `mangle` iptables tables but does not implement the `nat` table. The egress sidecar uses a REDIRECT rule in the `nat` table to intercept DNS queries (port 53 → 15353), so it cannot start under gVisor. This is an upstream gVisor limitation ([gvisor#170](https://github.com/google/gvisor/issues/170)).


**Solution**:


- Use `secure_runtime.type = "kata"` with `k8s_runtime_class = "kata-qemu"` — Kata provides a full Linux kernel per pod, so the `nat` table is available and the egress sidecar works unchanged.
- Use a CNI-level FQDN policy (e.g., Cilium `toFQDNs`) instead of the egress sidecar for network isolation under gVisor.
- Remove `network_policy` from sandbox creation requests if egress control is not required.


> **Note**: The server validates this combination at request time and returns HTTP 400 with a clear error message when `secure_runtime.type = "gvisor"` and `network_policy` are used together.


### Compatibility Matrix


| Feature | runc | gVisor | Kata (QEMU) | Kata (CLH) | Kata (FC) |
| --- | --- | --- | --- | --- | --- |
| Syscall Compatibility | Full | Partial | Full | Full | Limited |
| GPU Support | Yes | No | Yes | Yes | No |
| IPv6 | Yes | Yes | Yes | Yes | Yes |
| Privileged Mode | Yes | No | Yes | Yes | No |
| Docker Volume | Yes | Yes | Yes | Yes | Yes |
| Systemd | Yes | No | Yes | Yes | No |
| iptables `nat` table (egress sidecar) | Yes | **No** | Yes | Yes | Yes |


### Getting Help


- **Documentation**: [OpenSandbox GitHub](https://github.com/opensandbox-group/OpenSandbox)
- **Issues**: Report bugs via [GitHub Issues](https://github.com/opensandbox-group/OpenSandbox/issues)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/secure-container.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/network-isolation`

Return to top

# Network Isolation on Kubernetes


## Problem
## Problem ​
## Native Kubernetes NetworkPolicy ​
## Approach 1: Global Enforced Isolation via Egress Sidecar deny.always ​
*The implementation is in components/egress/pkg/policy/always_rules.go:*

*Create a Dockerfile that embeds the deny.always file into the image:*

## Allowing Legitimate In-Cluster Services ​
## Approach 2: On-Demand Isolation via Per-Sandbox NetworkPolicy ​
## Comparison ​
## Runtime Compatibility ​
## Recommendations ​










On a Kubernetes cluster, each OpenSandbox sandbox runs as an independent Pod with a dedicated Pod IP assigned by the CNI plugin. By default, any sandbox can reach other sandboxes in the same cluster directly via Pod IP. This introduces several security risks:


- **Internal network scanning**: malicious code inside a sandbox can scan the cluster Pod CIDR range to discover other sandboxes.
- **Unauthorized access**: an attacker can connect to other sandboxes' listening ports directly, bypassing OpenSandbox's authentication and authorization mechanisms.
- **Data leakage**: when sandboxes from different tenants co-exist in the same cluster, the lack of isolation may lead to unauthorized cross-tenant data access.


A mechanism is needed to prevent direct IP-based communication between sandboxes while preserving legitimate external access paths (via OpenSandbox Ingress).


## Native Kubernetes NetworkPolicy


Kubernetes NetworkPolicy controls traffic through **Pod label selectors**. It faces fundamental limitations in the sandbox isolation scenario:


- **Unpredictable labels**: sandbox Pod labels are injected automatically by the platform and are not user-controllable. Sandboxes from different tenants or security levels may share the same label set, making it impossible to define precise isolation boundaries with label selectors.
- **Dynamic lifecycle**: sandboxes are created and destroyed frequently. NetworkPolicy is a static declaration and cannot track the expected isolation relationships of each sandbox in real time.
- **Granularity mismatch**: NetworkPolicy operates on Pod sets (namespace + label selector), while sandbox isolation requires each sandbox to be an independent security domain that denies access from all other sandboxes by default. Expressing "deny access from all other Pods to me" with NetworkPolicy would require a separate rule per sandbox, and cannot cover sandboxes created in the future.
- **No outbound control**: NetworkPolicy Ingress rules can block inbound traffic, but cannot prevent sandbox processes from initiating outbound connections (e.g., curling another sandbox's Pod IP). Blocking outbound direct connections requires bidirectional (Ingress + Egress) policies per sandbox, which runs into the same label unpredictability and dynamicity problems.


Therefore, OpenSandbox does not rely on native Kubernetes NetworkPolicy. Instead, it uses **sandbox-level egress control** to enforce sandbox-to-sandbox isolation. The control point lives inside the sandbox (egress sidecar), not at the cluster network layer.


## Approach 1: Global Enforced Isolation via Egress Sidecar `deny.always`


### How It Works


The OpenSandbox egress sidecar provides a `deny.always` mechanism: place a file at `/var/egress/rules/deny.always` inside the sidecar container, and the rules declared in it take effect **unconditionally**, with higher priority than any allow rules set by users via the SDK or API.


The implementation is in `components/egress/pkg/policy/always_rules.go`:

go

```
func MergeAlwaysOverlay(user *NetworkPolicy, alwaysDeny, alwaysAllow []EgressRule) *NetworkPolicy {
    // alwaysDeny is prepended so it matches first, achieving unconditional denial
    merged = append(merged, alwaysDeny...)
    merged = append(merged, alwaysAllow...)
    merged = append(merged, out.Egress...)
}
```


`MergeAlwaysOverlay` is called on every policy change (both initial startup and runtime updates), merging always-deny, always-allow, and user policies by priority. Since rules match in order, `deny.always` rules have the highest priority and cannot be overridden by users through the SDK or API.


Additionally, the `deny.always` file is automatically reloaded every minute, so updates take effect without restarting the container.


### Configuration Steps


#### 1. Determine Cluster Pod CIDR and Service CIDR


Obtain the Pod and Service CIDR ranges of the Kubernetes cluster:

bash

```
# Service CIDR: usually set by kube-controller-manager's --service-cluster-ip-range
# Pod CIDR: usually set by the CNI plugin or kube-controller-manager's --pod-network-cidr
```


Common example values:


- Pod CIDR: `10.244.0.0/16`
- Service CIDR: `10.96.0.0/12`


#### 2. Create the `deny.always` Rule File

text

```
10.244.0.0/16
10.96.0.0/12
```


Supported target types: IP addresses (e.g., `10.0.0.5`), CIDR ranges (e.g., `10.0.0.0/8`), or domain names (e.g., `internal.service.local`, with `*.` wildcard prefix support).


#### 3. Build a Custom Image Based on the Official Egress Image


Create a `Dockerfile` that embeds the `deny.always` file into the image:

dockerfile

```
FROM opensandbox/egress:latest

COPY deny.always /var/egress/rules/deny.always
```


Build and push to a registry accessible by the cluster:

bash

```
docker build -t registry.example.com/opensandbox/egress:hardened .
docker push registry.example.com/opensandbox/egress:hardened
```


#### 4. Update the Server Configuration


In the OpenSandbox server configuration, point the `[egress]` `image` to the custom image:

toml

```
[egress]
image = "registry.example.com/opensandbox/egress:hardened"
mode = "dns+nft"
```


After this configuration is applied, all newly created sandboxes will use the egress sidecar image that includes the `deny.always` rules. No changes to individual sandbox creation requests are needed.


> Note: the `deny.always` file is hot-reloaded every minute. To change the rules (e.g., after a cluster CIDR change), update the `deny.always` file, rebuild the image, and perform a rolling update of the server configuration.


### Effects


- **Pod IP blocked**: sandboxes cannot directly reach other Pods in the same cluster via Pod IP.
- **Service ClusterIP blocked**: sandboxes cannot reach in-cluster services via Service ClusterIP.
- **Forced access path**: legitimate cross-sandbox communication must go through the `GetEndpoint()` API, which returns an external access endpoint proxied by OpenSandbox Ingress with authentication and authorization.
- **Transparent to users**: users do not need to declare any additional parameters in SDK calls. Isolation is enforced automatically at the platform level.


## Allowing Legitimate In-Cluster Services


When `defaultAction: deny` is enabled, allowing a sandbox to reach a Kubernetes Service requires **both** layers of the egress sidecar to agree:


1. **DNS layer**: allow the service hostname so the DNS proxy does not return `NXDOMAIN`.
2. **Network layer** (`dns+nft` mode): allow the Service CIDR (or a narrower ClusterIP range) so nftables does not drop the resolved TCP connection.


For example, if a sandbox should reach `postgres.opensandbox.svc.cluster.local`, this is not enough by itself:

json

```
{ "action": "allow", "target": "postgres.opensandbox.svc.cluster.local" }
```


The request can still fail after DNS resolution if the Service ClusterIP falls inside a denied CIDR such as `10.96.0.0/12`. In `dns+nft` mode you must also allow the Service CIDR (or the specific ClusterIP range you want exposed):

json

```
{ "action": "allow", "target": "10.96.0.0/12" }
```


### Recommended Patterns


- **Platform-managed allowlist**: if many sandboxes need the same internal services, keep the Service CIDR allowance in `allow.always` and let users request only the DNS names they should reach.
- **Per-sandbox allowlist**: if access should be tightly scoped, include both the service FQDN and the required Service CIDR in the sandbox's `network_policy` / `networkPolicy`.
- **Avoid assuming CoreDNS exemptions are enough**: the sidecar automatically allows nameserver IPs so DNS forwarding works, but it does **not** automatically allow arbitrary Service ClusterIPs for application traffic.


## Approach 2: On-Demand Isolation via Per-Sandbox NetworkPolicy


If global enforced isolation is not desired, or if specific sandboxes need more permissive access, you can explicitly deny internal network access at sandbox creation time via the `network_policy` parameter:


Pool mode limitation


Per-request `networkPolicy` is not supported when the lifecycle API creates a sandbox from a pre-warmed Pool via `extensions.poolRef`. Pool pods already exist, so the server cannot inject the egress sidecar for an individual allocation and rejects requests that contain both fields. Configure the required network controls in the Pool pod template before its pods are created, or use a non-pooled sandbox when each request needs its own policy.

python

```
from opensandbox import Sandbox, NetworkPolicy, EgressRule

sandbox = await Sandbox.create(
    image="python:3.11",
    network_policy=NetworkPolicy(
        default_action="deny",
        egress=[
            EgressRule(action="deny", target="10.244.0.0/16"),   # Deny Pod CIDR
            EgressRule(action="deny", target="10.96.0.0/12"),   # Deny Service CIDR
            EgressRule(action="allow", target="*.example.com"),  # Allow external domains
        ],
    ),
)
```


### Limitations


- **Per-sandbox declaration**: each sandbox must explicitly pass the `network_policy` parameter at creation. The platform cannot enforce it by default.
- **CIDR exposure**: users need to know the cluster's Pod CIDR and Service CIDR. In multi-tenant scenarios, this is sensitive information that should not be exposed to users.
- **Overridable**: users can declare higher-priority allow rules within the same `network_policy` to override their own deny rules, making this less secure than the `deny.always` enforcement in Approach 1.


## Comparison


| Dimension | Global `deny.always` | Per-Sandbox NetworkPolicy |
| --- | --- | --- |
| Enforcement | Yes (user cannot override) | No (user can modify policy) |
| User awareness | Transparent (platform-level) | Requires explicit declaration |
| Operational cost | Low (one-time image build, global effect) | High (declare per sandbox) |
| Cluster CIDR exposure | Not exposed to users | Must be exposed to users |
| Use case | Platform-wide default isolation, recommended | Whitelist mode, fine-grained control |


## Runtime Compatibility


Both Approach 1 (`deny.always` via egress sidecar) and Approach 2 (per-sandbox `network_policy`) depend on the egress sidecar, which uses an iptables `nat` table REDIRECT rule for DNS interception. This works with `runc` (default) and all Kata Containers variants (`kata-qemu`, `kata-clh`, `kata-fc`), but **not with gVisor** — gVisor's netstack does not implement the `nat` table.


If you need both gVisor's syscall isolation and FQDN egress control:


- Use `kata-qemu` instead — it provides comparable security isolation and supports the egress sidecar.
- Alternatively, use a CNI-level FQDN policy (e.g., Cilium `toFQDNs`) for network isolation alongside gVisor.


The same architectural constraint applies to transparent service meshes such as Istio/Envoy sidecar injection: OpenSandbox egress expects to own outbound interception inside the pod network namespace. If a mesh sidecar also rewrites outbound traffic in that namespace, egress-sidecar features such as per-sandbox network policy, transparent MITM, and Credential Vault are not currently supported together. Prefer excluding sandbox pods from mesh injection or enforcing outbound policy at the platform network layer instead.


See the [Compatibility Matrix](https://open-sandbox.ai/guides/secure-container#compatibility-matrix) in the Secure Container Runtime Guide for the full feature support table.


## Recommendations


1. **Default full isolation**: use `deny.always` to block the cluster's internal CIDR ranges as the platform's default security baseline.
2. **Whitelist with `allow.always`**: for scenarios requiring cross-sandbox communication (e.g., an agent dispatching tasks to sandboxes), use the `allow.always` file (`/var/egress/rules/allow.always`) to open specific Pod IPs or Service DNS names. `allow.always` has higher priority than user policies but lower than `deny.always`, giving the platform precise control over the open scope.
3. **External access entry**: the only way for a sandbox to expose services externally should be the `GetEndpoint()` API, proxied through OpenSandbox Ingress. Pod IPs should not be used as external service endpoints.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/network-isolation.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/isolation-sessions`

Return to top

# Isolation Sessions


Isolation sessions run a **long-lived `bash` inside a [bubblewrap](https://github.com/containers/bubblewrap) namespace**, so one sandbox pod can host many mutually isolated task runs without spinning up a new container. Each session gets its own PID, mount, tmpfs, and env namespaces; startup is sub-millisecond.


## Table of Contents


- [Requirements](https://open-sandbox.ai/guides/isolation-sessions#requirements)
- [Overview](https://open-sandbox.ai/guides/isolation-sessions#overview)
- [How It Works](https://open-sandbox.ai/guides/isolation-sessions#how-it-works)
- [Quick Start](https://open-sandbox.ai/guides/isolation-sessions#quick-start)
- [Session Lifecycle](https://open-sandbox.ai/guides/isolation-sessions#session-lifecycle)
- [Workspace Modes](https://open-sandbox.ai/guides/isolation-sessions#workspace-modes)
- [Bind Mounts and Allowlist](https://open-sandbox.ai/guides/isolation-sessions#bind-mounts-and-allowlist)
- [Profiles and Defaults](https://open-sandbox.ai/guides/isolation-sessions#profiles-and-defaults)
- [Environment, UID, and Networking](https://open-sandbox.ai/guides/isolation-sessions#environment-uid-and-networking)
- [Filesystem Proxy](https://open-sandbox.ai/guides/isolation-sessions#filesystem-proxy)
- [Capabilities and Probing](https://open-sandbox.ai/guides/isolation-sessions#capabilities-and-probing)
- [Server Configuration](https://open-sandbox.ai/guides/isolation-sessions#server-configuration)
- [Limitations](https://open-sandbox.ai/guides/isolation-sessions#limitations)
- [See Also](https://open-sandbox.ai/guides/isolation-sessions#see-also)


---


## Requirements
## Table of Contents ​
## Requirements ​
## Overview ​
## How It Works ​
## Quick Start ​
## Session Lifecycle ​
## Background Runs ​
## Workspace Modes ​
*Overlay upper dirs live under upper_root (default /var/lib/execd/isolation).*

## Multiple Overlay Mounts ​
## Bind Mounts and Allowlist ​
## Profiles and Defaults ​
## Environment, UID, and Networking ​
## Filesystem Proxy ​
## Capabilities and Probing ​
## Server Configuration ​
*Example: components/execd/configs/isolation.example.toml.*

## Limitations ​
## See Also ​



















Component versions needed for the features covered by this guide:


- `execd` >= 1.0.20 for base isolation session support; **>= 1.0.21 recommended** for `binds`, `List sessions`, `uid_mode: "userns"`, and the default writable allowlist (`/workspace`, `/mnt`, `/media`, `/data`)
- `opensandbox-server` >= 0.2.1 — the server injects `CAP_SYS_ADMIN`, unconfined AppArmor, seccomp, and protected-system-path settings, and the tmpfs mount required by `bwrap` when the execd image declares `bootstrap.execd.isolation`
- Python SDK >= 0.1.14 (`isolation.run_once` / `isolation.session` context manager); >= 0.1.13 for the generated isolation client only
- JavaScript / TypeScript SDK >= 0.1.10 (`isolation.runOnce` / `isolation.withSession`)
- Kotlin / Java SDK >= 1.0.16 (`isolation.runOnce()` / `isolation.withSession { ... }`); >= 1.0.15 for the generated isolation client only
- C# SDK >= 0.1.4 (`RunOnceAsync` / `WithSessionAsync`)
- Go SDK >= 1.0.4 (`IsolationRunOnce` / `IsolationWithSession`)


The `setpriv_available` / `userns_available` fields on [`/capabilities`](https://open-sandbox.ai/guides/isolation-sessions#capabilities-and-probing) were added after execd v1.0.21 and are only present on execd builds from `main` at the time of writing; older execd omits both fields (clients must tolerate their absence).


Host requirements (`bwrap` binary, `CAP_SYS_ADMIN`, `overlayfs`, etc.) are listed under [Server Configuration → Host Requirements](https://open-sandbox.ai/guides/isolation-sessions#server-configuration).


The published execd image includes the fail-closed native workload gate used during session startup. For a Linux source build, `make build` requires a C compiler plus static libc and produces `bin/opensandbox-session-gate`; run `make build-session-gate` and then `sudo make install-session-gate` before starting execd to install the helper at `/opt/opensandbox/opensandbox-session-gate`. Keep that path and its parent directory root-owned and not group- or world-writable.


---


## Overview


| Concept | Boundary | Startup | Typical Use |
| --- | --- | --- | --- |
| **Isolation session** | bubblewrap namespaces inside one sandbox | ~100 ms to create; subsequent `run` in an existing session is near-zero overhead | Many short, mutually isolated task runs reusing one long-lived session |
| Bash session (`/session`) | bash process, no extra namespaces | ms | Interactive REPL-style command sequences |
| Sandbox | container or pod | 100s of ms to seconds | Tenant, workspace, or user boundary |
| Secure runtime (gVisor / Kata) | user-space kernel or VM per sandbox | 10–500 ms | Hardware-level protection against container escape |


Session creation vs. per-run cost


Creating a session takes about 100 ms because execd waits briefly after starting `bwrap` to detect an immediately-exiting child. Once the session exists, each `POST /run` reuses the same bash process, so per-run overhead is negligible. Design workloads that amortize the create cost across many `run` calls in one session.


Good fits: **RL rollouts**, **batch code grading**, **multi-tool agent runs** — one sandbox per worker, many isolated tasks inside.


Not a fit: cross-language kernels (use `/code`), interactive REPLs (use `/session`), or hard trust boundaries against kernel exploits (use gVisor / Kata; see [Secure Container Runtime](https://open-sandbox.ai/guides/secure-container)).


---


## How It Works


`execd` forks one `bwrap` child per session; `bwrap` sets up Linux namespaces, then `exec`s a long-lived `bash` inside them.


![Isolation session runtime layout](https://open-sandbox.ai/assets/isolation-sessions-layout.BTYDbSL0.svg)


Two things the diagram doesn't show:


- `bash` is long-lived, so `export X=1` in one `run` is visible to the next `run` **in the same session** (never in another session).
- The FS proxy reads and writes the merged workspace view from **outside** the namespace, so uploads and downloads work while `bash` is busy.


### `run` request flow


![Isolation session run flow](https://open-sandbox.ai/assets/isolation-sessions-run-flow.CG1CaVgh.svg)


Non-happy paths:


| Event | What happens |
| --- | --- |
| Run `timeout_seconds` elapsed | execd cancels the run context, which sends `SIGINT` to the bwrap process group and emits an `IsolatedError` SSE event; the session itself stays alive. |
| `bwrap` process exited | The next `run` returns an `IsolatedError` SSE event with `session process has exited`; only `ErrContextNotFound` (session ID unknown) becomes an HTTP-level error. `DELETE` + recreate. |
| Idle timeout reached | GC runs the same teardown as `DELETE`. |
| Client disconnects mid-SSE | The Gin request context is cancelled and execd sends `SIGINT` to the running command; the run does **not** continue in the background. |


---


## Quick Start


### curl

bash

```
# Probe.
curl -s http://localhost:44772/v1/isolated/capabilities

# Create.
SESSION=$(curl -s -X POST http://localhost:44772/v1/isolated/session \
  -H "Content-Type: application/json" \
  -d '{
    "profile": "strict",
    "workspace": {"path": "/workspace", "mode": "overlay"},
    "idle_timeout_seconds": 300
  }' | jq -r .session_id)

# Run (SSE: stdout / error / complete).
curl -N -X POST "http://localhost:44772/v1/isolated/session/$SESSION/run" \
  -H "Content-Type: application/json" \
  -d '{"code": "export X=1; echo $X", "timeout_seconds": 30}'

# Second run reuses shell state.
curl -N -X POST "http://localhost:44772/v1/isolated/session/$SESSION/run" \
  -H "Content-Type: application/json" \
  -d '{"code": "echo $X"}'  # prints 1

# Delete.
curl -X DELETE "http://localhost:44772/v1/isolated/session/$SESSION"
```


### Python SDK

python

```
from opensandbox import Sandbox
from opensandbox.models.isolated import (
    CreateIsolatedSessionRequest, IsolatedWorkspaceSpec, IsolatedRunOpts,
)

# Sandbox.create is an async classmethod, so await it before entering
# the async context manager.
async with (await Sandbox.create("python:3.11")) as sandbox:
    # One-shot.
    await sandbox.isolation.run_once(
        "python -c 'print(42)'", workspace="/workspace", profile="strict",
    )

    # Persistent session.
    async with sandbox.isolation.session(
        CreateIsolatedSessionRequest(
            workspace=IsolatedWorkspaceSpec(path="/workspace", mode="overlay"),
            profile="strict",
            idle_timeout_seconds=300,
        )
    ) as session:
        await session.run("export STAGE=train")
        await session.run("python train.py", opts=IsolatedRunOpts(timeout_seconds=600))
        await session.files.write_file("/workspace/data.csv", data_bytes)

    # Reattach after a client restart.
    handle = await sandbox.isolation.attach(known_session_id)
```


### JavaScript / TypeScript SDK

ts

```
await sandbox.isolation.runOnce("node -e 'console.log(1)'", "/workspace", {
  profile: "strict",
});

await sandbox.isolation.withSession(
  { profile: "strict", workspace: { path: "/workspace", mode: "overlay" } },
  async (session) => { await session.run("npm test"); },
);
```


### Kotlin SDK

kotlin

```
sandbox.isolation().runOnce(code = "python -c 'print(1)'", workspace = "/workspace")

sandbox.isolation().withSession(request) { session ->
    session.run("ls /workspace")
}
```


---


## Session Lifecycle


Under `/v1/isolated/` on execd. Use `X-EXECD-ACCESS-TOKEN` when execd has an access token configured.


| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/session` | Create; returns `{session_id, created_at}`. |
| `GET` | `/sessions` | List active sessions. |
| `GET` | `/session/{id}` | Full state; echoes creation params so a stateless client can rebuild the handle. |
| `POST` | `/session/{id}/run` | Foreground (default): SSE stream `stdout` / `error` / `complete`. Background (`"background": true`): returns `202` with a run handle. Runs on the same session are serialized. |
| `GET` | `/session/{id}/runs/{runId}` | Background run status: `running`, `exit_code`, `error`, timestamps. |
| `GET` | `/session/{id}/runs/{runId}/logs` | Background run combined output as plain text, with byte-cursor pagination. |
| `DELETE` | `/session/{id}` | Destroy. |
| `GET` | `/capabilities` | Probe. |


`idle_timeout_seconds > 0` destroys idle sessions automatically; set to `0` to disable idle GC and always `DELETE` explicitly.


---


## Background Runs


A background run starts code detached inside the session and returns immediately; the run's combined stdout/stderr and exit code are captured by execd, and the client polls them while other work continues on the session.

bash

```
# Start detached; 202 returns {"session_id", "run_id", "started_at"}.
RUN=$(curl -s -X POST "http://localhost:44772/v1/isolated/session/$SESSION/run" \
  -H "Content-Type: application/json" \
  -d '{"code": "sleep 5 && echo done", "background": true}' | jq -r .run_id)

# Poll status until running=false.
curl -s "http://localhost:44772/v1/isolated/session/$SESSION/runs/$RUN"

# Read output (plain text). The response header EXECD-ISOLATED-TAIL-CURSOR
# carries the next byte offset for incremental reads.
curl -s "http://localhost:44772/v1/isolated/session/$SESSION/runs/$RUN/logs"
curl -s "http://localhost:44772/v1/isolated/session/$SESSION/runs/$RUN/logs?cursor=123"
```


Python SDK:

python

```
session = await sandbox.isolation.create(CreateIsolatedSessionRequest(
    workspace=IsolatedWorkspaceSpec(path="/workspace", mode="rw"),
))

run = await session.run_background("sleep 5 && echo done")
while (status := await session.run_status(run.run_id)).running:
    await asyncio.sleep(0.2)
print(status.exit_code)
logs = await session.run_logs(run.run_id)   # .text + .cursor for pagination
```


Background run semantics:


- `timeout_seconds` is foreground-only; background runs are not time-limited.
- Idle GC is suspended while a background run is active; after it finishes, the normal idle window applies. Deleting the session kills the run.
- Background runs require a writable log location, so sessions with a read-only (`ro`) workspace reject them with `400`; `rw` and `overlay` workspaces are supported.
- Runs share the session's process group, so session-level signals (e.g. the `SIGINT` sent when a foreground run times out or is cancelled) also reach them.
- Each `logs` request returns at most 16 MiB; page through large output with the returned cursor. Per-run log retention is capped at 16 MiB — output beyond the cap is discarded when the run completes, so drain incrementally while the run is active if you need more than the first page.
- A run whose session dies mid-flight reports `running: false` with `error: "session terminated"`; run records and their logs are removed when the session is deleted or garbage-collected.


---


## Workspace Modes


| Mode | Semantics |
| --- | --- |
| `rw` | Bind-mount read-write; writes persist on the host. |
| `overlay` (default) | Copy-on-write via overlayfs; writes go to a per-session upper dir and vanish on `DELETE`. |
| `ro` | Bind-mount read-only; writes fail with `EROFS`. |


Overlay upper dirs live under `upper_root` (default `/var/lib/execd/isolation`).


Because isolated-session state lives only in execd's memory, every session left under `upper_root` when execd exits is stale. Before publishing a new session, execd creates a durable cleanup record at `<upper_root>/.execd-cleanup/<session-id>`; on startup it recovers those records and removes the exact matching session directories. A record is retired only after the entire session subtree has been deleted, so partial deletion and transient filesystem failure retain a retryable identity across restarts. Residue that cannot be removed yet — e.g. an upper still referenced by a mount from the previous lifetime — stays counted toward `upper_max_bytes` and is retried by the idle collector.


Only recorded session directories are removed. Unrecorded children under `upper_root`, including allocator-shaped directory trees, are treated as operator data and are never reclaimed automatically. Directories left by execd versions that predate the cleanup registry therefore require explicit migration or manual cleanup; keep `upper_root` dedicated to execd and do not modify the reserved `.execd-cleanup` registry. In pooled / pre-provisioned sandboxes this prevents one occupant's session data from leaking to the next.

json

```
{ "workspace": { "path": "/workspace", "mode": "overlay" } }
```


---


## Multiple Overlay Mounts


A session can carry **several independent overlay mounts** via the `overlays` request field (the single `workspace` remains supported as sugar for a one-element list; when both are present, `workspace` is prepended):

json

```
{
  "overlays": [
    { "path": "/", "mode": "overlay" },
    { "path": "/workspace", "mode": "overlay", "persist": true },
    { "path": "/data/scratch", "mode": "overlay", "persist": false }
  ]
}
```


- Each entry has its own mount semantics, so workspace files, system-level changes (`apt install` → `/usr`, config → `/etc`), and additional project directories get **independent copy-on-write uppers**.
- Mounts are applied shallow-first; a nested overlay (e.g. `/workspace` on top of a `/` root overlay) shadows its ancestors within its own subtree. Paths must be absolute and unique.
- `persist` (overlay mode only, default `true`): `true` allocates a host upper directory under `upper_root`; `false` uses an ephemeral tmpfs upper whose writes are discarded when the session ends. `rw`/`ro` entries must not set `persist`. An ephemeral upper lives inside the namespace only, so the files API serves `persist=false` overlays from their host-side content: in-session writes under such an overlay are not observable through the files API and files-API writes into it are rejected.
- The files API routes each request to the overlay whose mount path is the longest prefix of the requested path; relative paths resolve against the first overlay.
- Background runs use the **first** overlay for their log location: it must be `rw`, or `overlay` with `persist: true`; otherwise background runs are rejected.


---


## Bind Mounts and Allowlist


- **`extra_writable`** — paths bind-mounted read-write at the same path (`source == destination`).
- **`binds`** — explicit `source` → `dest` mappings, optionally `readonly`. `source` must already exist; `dest` must already exist inside the namespace (bake it into the sandbox image).

json

```
{
  "workspace": { "path": "/workspace", "mode": "rw" },
  "extra_writable": ["/data/scratch"],
  "binds": [
    { "source": "/data/in",  "dest": "/mnt/in",  "readonly": true },
    { "source": "/data/out", "dest": "/mnt/out" }
  ]
}
```


Every `source` is checked against the operator-configured `allowed_writable` allowlist **after** symlink resolution, so symlinks cannot escape it. Default allowlist: `/workspace`, `/mnt`, `/media`, `/data` (subpaths allowed). Empty allowlist rejects all extra binds.


---


## Profiles and Defaults


The `profile` field currently controls only how `/tmp` is exposed inside the namespace:


| Profile | `/tmp` |
| --- | --- |
| `strict` (default) | Private tmpfs (`--tmpfs /tmp`) |
| `balanced` | Shared with the sandbox (`--bind /tmp /tmp`) |


`workspace.mode` and `env_passthrough` are **independent** of the profile: when they are omitted, execd normalizes `workspace.mode` to `overlay` and `env_passthrough.mode` to `deny` regardless of which profile you pick. Set those fields explicitly if you want persistent workspace writes (`"rw"`) or host env passthrough (`"allow"`).


---


## Environment, UID, and Networking


- **`env_passthrough`** — `mode: "allow"` + `keys` whitelists host env vars; default `deny`. Per-run overrides go in `IsolatedRunRequest.envs`.
- **`uid` / `gid`** with **`uid_mode: "setpriv"`** (default, real setuid/setgid drop) or **`"userns"`** (user namespace remap). Check `setpriv_available` / `userns_available` from [`/capabilities`](https://open-sandbox.ai/guides/isolation-sessions#capabilities-and-probing) before requesting a mode.
- **`share_net: true`** shares the sandbox's network namespace. Sandbox-level egress and Credential Vault policies still apply.
- **`share_net: false`** creates a private network namespace. Before releasing the workload startup gate, execd opens the authenticated NetNS, obtains its real owning UserNS with `NS_GET_USERNS`, and bind-pins both below `/run/execd/namespaces/<opaque-id>/`. Any validation or pin failure aborts Session creation. Execd attempts pin cleanup on failed startup, process exit, explicit delete, idle collection, and runner shutdown; retryable failures retain Session ownership and are retried while execd remains alive. This applies to both UID modes; hardened network backends will require `uid_mode: "userns"`.


The legacy default remains unchanged in this phase: omitting `share_net` continues to share the sandbox network namespace. Namespace pinning alone does not enable Session egress or ingress.


Private Sessions are not recoverable across an execd restart. Deployments that enable them must treat execd as sandbox-critical and recreate the entire sandbox/container if execd exits; they must not launch a replacement execd inside the surviving mount namespace. Destroying the sandbox/container tears down that mount namespace and releases all pins. Execd intentionally does not scan and adopt opaque namespace-pin directories on startup because they do not carry a durable sandbox generation, so doing so could unmount another live process's resources.


---


## Filesystem Proxy


Reads and writes the session's **merged** workspace view from outside the namespace — this is how SDKs `upload`, `download`, and `list` without spawning a shell. All paths are per session under `/v1/isolated/session/{id}/`:


| Method | Path |
| --- | --- |
| `GET` | `files/info?path=...` |
| `GET` | `files/download?path=...` (supports `Range` and `offset` / `limit`) |
| `POST` | `files/upload` (multipart: `metadata` + `file`) |
| `DELETE` | `files?path=...` |
| `POST` | `files/mv` |
| `POST` | `files/permissions` |
| `POST` | `files/replace?verbose=true` |
| `GET` | `files/search?path=...&pattern=...` |
| `GET` | `directories/list?path=...&depth=N` |
| `POST` | `directories` |
| `DELETE` | `directories?path=...` |


Writes on a `ro` workspace fail; writes on `overlay` land in the upper dir and vanish on `DELETE`.


---


## Capabilities and Probing

bash

```
curl -s http://localhost:44772/v1/isolated/capabilities
```

json

```
{
  "available": true,
  "isolator": "bwrap",
  "version": "0.9.0",
  "setpriv_available": true,
  "userns_available": false,
  "commit_supported": false,
  "diff_supported": false
}
```


- `available: false` — the trusted native workload gate is missing or untrusted, bubblewrap is missing, or the host can't create the required namespaces (missing `CAP_SYS_ADMIN`, restricted user-ns sysctl, etc.).
- `setpriv_available` / `userns_available` — whether sessions with `uid_mode: "setpriv"` or `"userns"` can be created. `setpriv_available` reflects only execd's **default** UID/GID; a session that requests a different UID/GID may still return `503 NOT_SUPPORTED` when identity switching is unavailable.
- `commit_supported` / `diff_supported` — Phase 2 stubs, currently return `503`.


---


## Server Configuration


Point execd at an optional TOML file:


| Flag | Env |
| --- | --- |
| `--isolation-config` | `EXECD_ISOLATION_CONFIG` |

toml

```
# Parent directory for per-session overlay upper dirs.
upper_root = "/var/lib/execd/isolation"

# Allocation-time threshold for total overlay upper-directory size (bytes).
# Existing sessions can write beyond this value.
# Default: 8 GiB. Set to 0 to disable the allocation check.
upper_max_bytes = 8589934592  # 8 GiB

# Sources allowed for extra_writable / binds (symlink-resolved).
# Default: ["/workspace", "/mnt", "/media", "/data"]. Empty = reject all.
allowed_writable = ["/workspace", "/mnt", "/media", "/data"]
```


Example: `components/execd/configs/isolation.example.toml`.


`upper_max_bytes` is checked when creating an `overlay` workspace (the default mode). If a successful usage scan reports a total at or above the configured positive limit, the new session is rejected. This setting does not cap writes by existing sessions and does not apply to `rw` or `ro` workspaces.


Deleting an overlay session can restore admission once its cleanup succeeds and total usage falls below the threshold. Deletion discards that session's private upper data, so preserve any data you need before deleting it.


**Host requirements:** `bwrap` and the trusted native workload gate in the execd image; `CAP_SYS_ADMIN` (and `kernel.unprivileged_userns_clone=1` for `uid_mode: "userns"`); `overlayfs` in the kernel for `overlay` workspaces. The published image installs the gate automatically. Linux source builds must run `make build-session-gate` and then `sudo make install-session-gate` from `components/execd` before starting execd.


Note: `/capabilities` reports `available: false` when the native workload gate cannot be opened as a trusted executable or when bwrap itself cannot be started (missing binary or missing namespace capabilities). A missing `overlayfs` does **not** flip `available` — the overlay probe only influences Phase 2 `commit` / `diff` support, and default overlay-mode session creation can still fail at runtime on such hosts. If you rely on `workspace.mode: "overlay"`, verify `overlayfs` support directly on the host.


---


## Limitations


- **`diff` / `commit` are Phase 2 stubs**, currently return `503`.
- **No hardware-level guarantee.** Namespaces + seccomp only; pair with a secure runtime for kernel-exploit defense.
- **Linux only.** Non-Linux builds return `available: false`.
- **Serialized runs per session** — create multiple sessions for parallelism.
- **Bind destinations must pre-exist** in the sandbox image.


---


## See Also


- [execd](https://open-sandbox.ai/architecture/data-plane/execd)
- [Secure Container Runtime](https://open-sandbox.ai/guides/secure-container)
- [execd OpenAPI spec](https://open-sandbox.ai/api/)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/isolation-sessions.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/auto-pause-wake`

Return to top

# Auto-Pause & Wake-on-Access Guide


This guide shows how to enable and operate **auto-pause** and **wake-on-access** for Fast Sandbox (`fsb-`) sandboxes: a sandbox that opts in is paused automatically after **X** seconds without ingress traffic (checkpointed, memory and CPU released), and the next request to it **wakes** it — the gateway parks the request for up to **Y** seconds while the sandbox restores, then forwards normally instead of failing with a permanent `503`.


For the design rationale and internal mechanics, see [Auto-Pause and Wake-on-Access architecture](https://open-sandbox.ai/architecture/network/auto-pause-wake-on-access).


## How it works in one minute

text

```
active    every request through the ingress refreshes activity:{id} in Redis (async, coalesced)
idle      server sweeper (every 15s) checks gates → PauseSandbox → checkpoint → Paused
wake      next request → gateway resumes + parks the request ≤ Y → forwards when Ready
          (budget exhausted → 503 + Retry-After + OpenSandbox-Wake: expired; restore continues)
```


Three parties must agree before anything happens — the server, the ingress, and the sandbox itself. All three default to **off**, and a sandbox that never declares an `idlePolicy` keeps today's behavior exactly: never auto-paused, never auto-woken.


## Prerequisites


- **OpenSandbox full stack v1.2.0 or later.** The lifecycle server, ingress gateway, and SDKs must all be at v1.2.0+; earlier stacks do not accept `lifecycle.idlePolicy` or the wake-timeout contract.
- **Fast Sandbox backend only.** Docker and Kubernetes pod sandboxes are not covered (their manual pause/resume is separate — see [Pause & Resume](https://open-sandbox.ai/guides/pause-resume)).
- **Traffic through the ingress gateway.** The ingress is the only activity source. Sandboxes reached through the server proxy path (`/sandboxes/{id}/proxy/{port}`, the SDK `useServerProxy` mode) neither record activity nor wake — do not opt those workloads in.
- **Redis reachable from both the ingress and the server** (the same deployment as renew-intents). Wake itself does not use Redis — a Redis outage can only delay pauses, never break wake.


## Step 1 — Enable the sweeper on the server


In the server's `config.toml`:

toml

```
[automation.idle_pause]
enabled = true                    # master switch: enables the idle sweeper
sweep_interval_seconds = 15       # detection cadence
activity_ttl_seconds = 1800       # must stay ≥ the largest accepted X (see constraints)

[automation.idle_pause.redis]
dsn = "redis://127.0.0.1:6379/0"  # required when enabled = true
lock_ttl_seconds = 30
```


See [`[automation.idle_pause]` in the server configuration reference](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md) for all keys.


## Step 2 — Enable the ingress

text

```
--activity-enabled=true           # record activity while proxying
--wake-enabled=true               # trigger resume + park requests
## How it works in one minute ​
## Prerequisites ​
## Step 1 — Enable the sweeper on the server ​
*In the server's config.toml:*

*See [automation.idle_pause] in the server configuration reference for all keys.*

## Step 2 — Enable the ingress ​
## Step 3 — Opt in sandboxes via lifecycle.idlePolicy ​
## Wake behavior and SDK retry ​
*Exhaustion raises SandboxWakeTimeoutException.*

## Composition with other features ​
## Constraints checklist ​
## Operating the feature ​
## Troubleshooting ​
## Reference ​











```


Relevant flags and defaults:


| Flag | Default | Purpose |
| --- | --- | --- |
| `--activity-enabled` | `false` | Record per-sandbox activity in Redis |
| `--activity-redis-dsn` | `redis://127.0.0.1:6379/0` | Redis for activity writes |
| `--activity-min-interval` | `5s` | Per-sandbox write coalescing |
| `--activity-ttl-seconds` | `1800` | Key TTL — keep equal to the server's `activity_ttl_seconds` |
| `--wake-enabled` | `false` | Resume + request parking |
| `--wake-park-budget` | `5s` | Park budget **Y** (operator-owned latency policy) |
| `--wake-park-max` | `1024` | Parking-lot capacity (held requests) |
| `--wake-restore-max` | `256` | Concurrent restore permits (must be ≤ `--wake-park-max`) |
| `--wake-retry-interval` | `50ms` | First poll interval |
| `--wake-retry-factor` | `1.3` | Poll backoff factor |
| `--wake-retry-jitter` | `0.1` | Poll backoff jitter |
| `--wake-max-flight-lifetime` | `5m` | Cap on one flight's establish+poll phase |


## Step 3 — Opt in sandboxes via `lifecycle.idlePolicy`


Set the policy at create time:

json

```
{
  "templateId": "tpl_2f0c...",
  "timeout": 86400,
  "lifecycle": {
    "idlePolicy": {
      "idleTimeoutSeconds": 300,
      "onIdle": "pause",
      "wakeOnAccess": true
    }
  }
}
```


Official SDKs expose typed parameters. Python (`create_from_template` is the fast-sandbox path — `idle_policy` rides alongside the template):

python

```
from datetime import timedelta

from opensandbox.models import IdlePolicy
from opensandbox.sandbox import Sandbox

sandbox = await Sandbox.create_from_template(
    "tpl_2f0c...",
    timeout=timedelta(hours=24),
    idle_policy=IdlePolicy(
        idle_timeout_seconds=300,
        on_idle="pause",
        wake_on_access=True,
    ),
)
```


The policy is desired state: validated updates take effect on the next read, without re-creating the sandbox. It is stored as the `sandbox.opensandbox.io/idle-policy` Sandbox CR annotation and hidden from public metadata.


### `idlePolicy` reference


| Field | Type | Default | Meaning |
| --- | --- | --- | --- |
| `idleTimeoutSeconds` | int 30–86400 | — | Idle threshold **X**. Required together with `onIdle`. Create is rejected with `400` if `X > activity_ttl_seconds`. |
| `onIdle` | enum | — | Only `pause` today. The field exists so a future action (e.g. `terminate`) stays additive. |
| `wakeOnAccess` | bool | `true` | Within a declared policy, `false` opts out of wake: traffic never resumes the sandbox (permanent `503`), only `POST /sandboxes/{id}/resume` does. |
| `activeProbe` | object | — | App-defined activity probe — see below. **Auto-pause only:** requires `idleTimeoutSeconds` (a wake-only policy is never probed, so the create is rejected with `400`); all three sub-fields required when present. |


**Wake-only policy**: omit `idleTimeoutSeconds` and `onIdle`, keep `wakeOnAccess: true`. The sandbox is never auto-paused, but a (manually) paused sandbox wakes on traffic.


**Omission invariant**: no `lifecycle` or no `idlePolicy` ⇒ never auto-paused and never auto-woken, regardless of server/ingress flags.


### The activity probe


Ingress observation cannot see work that generates no inbound traffic — a request that started a 20-minute in-sandbox computation, a background poller. `activeProbe` lets the application veto such a pause (it is auto-pause only: it must be declared together with `idleTimeoutSeconds`):

json

```
"activeProbe": {
  "port": 8080,
  "path": "/active",
  "timeoutSeconds": 2
}
```


When the sweeper is otherwise ready to pause, it issues `GET {path}` on `{port}` through the ingress gateway (sentinel-carried; it never resets the idle clock). Your endpoint answers:

text

```
200 {"active": true}    → busy: counts as activity, pause dropped for this sweep (re-probed ~X later)
200 {"active": false}   → idle: pause proceeds; optional "message" lands in the pause audit log
anything else / timeout → no record, candidate dropped this sweep (fail-safe: only an explicit
                          "not active" lets a pause through)
```


TIP


Use the probe when your workload has meaningful silent work. Without it, such a sandbox **will** be paused; the next request recovers state after restore, but the restore cost is real.


## Wake behavior and SDK retry


A request arriving at a paused, opted-in, `wakeOnAccess: true` sandbox is parked while the gateway resumes it (same-node restore is typically tens of milliseconds; the wake P95 target is < 500 ms):


- **Ready within Y** → forwarded like any other request. For the client, the park is just added latency — no status or body bytes are written during the wait, so keep LB/Envoy idle timeouts and client response-header timeouts above Y.
- **Y exhausted** → the gateway answers:

text

```
HTTP/1.1 503 Service Unavailable
Retry-After: 1
OpenSandbox-Wake: expired

{"error": {"code": "sandbox_wake_timeout",
           "message": "restore still in progress; request was never forwarded and is safe to retry",
           "sandboxId": "sb_..."}}
```


The `OpenSandbox-Wake: expired` header is gateway-owned (stripped from every upstream response), so its presence proves the request never reached the sandbox — that is what makes automatic retry safe for any method, including command/code-execution starts, provided the body is replayable. Official SDKs apply this contract to the marked response only:


- Wait per `Retry-After`, resend the original request. On by default, disable-able per client.
- Total wait bound: a wake-retry deadline (default 60 s) and a max-attempts cap (default 5) spanning all wake cycles; retries never reset the deadline.
- Success continues the original call; exhausted budget raises a typed wake-timeout error carrying the attempt count and waited time. A bare `503` (no marker) is never auto-retried for non-idempotent methods.


Python example:

python

```
from datetime import timedelta

from opensandbox.config import ConnectionConfig
from opensandbox.transport import RetryPolicy

config = ConnectionConfig(
    retry_policy=RetryPolicy(
        wake_retry_enabled=False,             # disable auto wake-retry
        wake_overall_deadline=timedelta(seconds=120),
        wake_max_attempts=10,
    )
)
```


Exhaustion raises `SandboxWakeTimeoutException`.


## Composition with other features


- **Renew-on-access ([OSEP-0009](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0009-auto-renew-sandbox-on-ingress-access.md))** is independent — one request can feed both. Recommended: enable both, so active sandboxes keep extending their expiry while idle ones get reclaimed.
- **Expiry is absolute**: pausing neither stops nor extends `expires_at`. A paused sandbox whose expiry passes becomes `Terminated`; wake then fails fast with `404`.
- **Manual pause/resume** keeps working. Wake treats manually and automatically paused sandboxes identically (unless `wakeOnAccess: false`).


## Constraints checklist


- `X ≤ activity_ttl_seconds` (server + ingress values must match); X floor is 30 s — lower values are rejected to keep the checkpoint cycle worth its cost.
- Everything in front of the ingress (LB idle timeouts, client response-header timeouts) must exceed **Y**, otherwise middle layers cut parked connections before the gateway can answer `503 + Retry-After`.
- Pause timing = X + at most one sweep interval of detection lag.
- Only new HTTP requests count: open WebSocket/SSE streams are not activity — frames (including WS ping/pong) are relayed without being recorded, so application-level WS pings cannot keep a sandbox alive. After X seconds without a fresh request the sandbox pauses and the connection breaks. Keep a background HTTP request cadence shorter than X, declare an `activeProbe`, or do not opt in.
- Scheduled workloads: a paused sandbox cannot wake itself. Arrange an external scheduler to call `POST /sandboxes/{id}/resume` before each run.
- Checkpoint cost is proportional to guest memory; every paused sandbox holds a full checkpoint in the artifact store until resumed or deleted. Size artifact-store capacity for peak concurrent paused sandboxes.


## Operating the feature


- **Rollout order**: deploy with all flags off → enable activity + sweeper for a canary tenant → enable wake on a canary ingress → opt in real workloads via `idlePolicy`.
- **Rollback**: disable the flags. Sandboxes left `Paused` stay resumable through the manual API — resume or delete stranded ones after disabling wake, since traffic will no longer wake them.
- **Key metrics** (see [Telemetry](https://open-sandbox.ai/guides/telemetry)):
  - `opensandbox.server.idlep.pause.requests` (`outcome` = accepted/gated/failed) — pause pipeline health.
  - `opensandbox.server.idlep.probe.outcome` — sustained `error` ⇒ broken probe endpoint on an opted-in workload.
  - `ingress.activity.writes_dropped` — Redis pressure on the producer side.
  - `ingress.park.shed` — parking-lot overflows; sustained growth ⇒ raise `--wake-park-max` or investigate restore latency.
  - `ingress.park.wait.duration` and `ingress.wake.restore.active` — wake health; same-node wake P95 target < 500 ms.
  - Flap ratio (pauses followed by a quick wake — the primary tuning signal for X) is not emitted as an instrument yet: derive it per sandbox by joining `pause.requests{outcome="accepted"}` with subsequent wake flights. Sustained flapping means traffic period ≈ X — raise X above the workload period.


## Troubleshooting


| Symptom | Likely cause | What to do |
| --- | --- | --- |
| Sandbox never pauses | No `idlePolicy` annotation, traffic through server-proxy mode, or Redis unreachable | Check the sandbox was created with `idlePolicy`; route through the ingress; check server logs for skipped sweeps |
| Sandbox pauses while working | Silent background work invisible to the ingress | Declare `activeProbe` and answer `{"active": true}` while busy |
| Paused-and-expired sandbox returns 404 | Absolute expiry passed while paused | Expected — pausing does not extend expiry; compose with renew-on-access |
| Clients see plain 503 (no marker) on a paused sandbox | `wakeOnAccess: false`, no declared policy, or `--wake-enabled=false` | Check the three activation parties |
| Wake latency above P95 target | Cross-node restore (artifact fetch + full materialization) | Size Y from the cluster's actual resume distribution; checkpoint-affinity scheduling is future work |
| Pauses/wakes flapping | Traffic period ≈ X | Raise X; track pauses followed by a quick wake per sandbox (the flap ratio is derived, not an emitted instrument — see [Monitoring](https://open-sandbox.ai/guides/auto-pause-wake#operating-the-feature)) |


## Reference


- [Architecture: Auto-Pause and Wake-on-Access](https://open-sandbox.ai/architecture/network/auto-pause-wake-on-access)
- [OSEP-0024](https://github.com/opensandbox-group/OpenSandbox/blob/main/oseps/0024-auto-pause-and-wake-on-access-for-fast-sandbox.md) — full proposal, alternatives, test plan
- [Fast Sandbox: Pause, Resume, and Snapshots](https://open-sandbox.ai/architecture/fast-sandbox/checkpoints)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/auto-pause-wake.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/kubernetes-resume-benchmark`

Return to top

# Kubernetes Resume Benchmark


The opt-in [runner](https://github.com/opensandbox-group/OpenSandbox/blob/main/tests/python/benchmarks/kubernetes_resume.py) measures standard Kubernetes **standalone, rootfs** pause/resume. It creates one sandbox per trial, writes a unique marker outside volume mounts, pauses it, waits for its Pods to disappear, resumes it, and checks the marker through a foreground command. It deletes the sandbox after each trial. QEMU VMState, pooled creation, and Fast Sandbox are outside this baseline.


## Prerequisites


- A lifecycle server configured for the Kubernetes BatchSandbox provider, with the controller and OCI snapshot registry configured as in [Pause and Resume](https://open-sandbox.ai/guides/pause-resume).
- `kubectl` connected to the same cluster, with permission to read BatchSandbox, SandboxSnapshots, Pods, nodes, and cluster version in the sandbox namespace. Pass an explicit context to avoid measuring against a different cluster.
- An immutable image digest containing `/bin/sh`, `cat`, and `sleep`. The server must inject execd. Do not put the marker directory under a volume mount.
- A runner with network access to the lifecycle server and sandbox endpoints; `--server-proxy` measures the server proxy route instead of direct access.
## Prerequisites ​
## Run ​
## Measurement boundaries ​
## Cache conditions ​
## Results and interpretation ​







This is an explicit benchmark, not part of the default E2E suite. Use a dedicated test cluster. No node caches are evicted by the runner.


## Run


Create an environment file containing the versions and conditions needed to repeat the experiment. For example, `environment.json`:

json

```
{
  "server_revision": "<git SHA or image digest>",
  "controller_image": "<image digest>",
  "execd_image": "<image digest>",
  "image_committer_image": "<image digest>",
  "runtime_class": "runc (default)",
  "node_resources": "<CPU, RAM, disk type>",
  "registry": "<implementation, placement, network conditions>",
  "snapshot_configuration": "<non-secret controller flags>",
  "cache_evidence": "Uncontrolled; no cache intervention",
  "background_load": "<other workloads and concurrency>"
}
```


Do not include credentials. The output also records the runner revision, Python and SDK versions, Kubernetes version, node runtime versions, context, image, resource limits, proxy mode, timeouts, and polling interval.

bash

```
cd tests/python
uv sync --frozen
export OPEN_SANDBOX_DOMAIN=localhost:8080
export OPEN_SANDBOX_API_KEY='<your API key>'
uv run python benchmarks/kubernetes_resume.py \
  --image '<image>@sha256:<digest>' \
  --namespace default --context '<test-context>' \
  --environment environment.json --scenario uncontrolled \
  --warmups 3 --samples 30 --output resume-uncontrolled.jsonl
```


Use `--protocol https` for a TLS server and `--server-proxy` when direct endpoints are inaccessible. Run `--help` for resource, polling, and timeout options. The script disables SDK retries and telemetry for this experiment. Polling remains explicit and includes its delay in the measured observation time.


## Measurement boundaries


All durations use the runner's monotonic clock and start immediately before `SandboxManager.resume_sandbox`. The resume portion has one shared timeout:


| Field | End of interval |
| --- | --- |
| `api_ack_ms` | Resume API returns; acceptance is not readiness |
| `running_ms` | First lifecycle GET reporting `Running` |
| `ready_ms` | A fresh `Sandbox.connect` resolves endpoints and passes execd health checks |
| `command_ms` | A foreground command returns successfully and prints the exact persisted marker |


These are cumulative times, not additive stages. `command_ms` includes an execd round trip and is the primary user-visible result. It does not measure an application-specific Agent initialization; add that workload in a separate experiment. Lifecycle observation and SDK readiness are sequential, so the polling interval and HTTP overhead affect results. No attempt is made to infer scheduler or image-pull durations from these client timings.


Creation, marker writing, pause, Pod deletion, optional cache preparation, and evidence collection, and cleanup are outside the resume interval. Waiting for source Pods to disappear avoids declaring a terminating source instance to be the restored instance. The runner verifies the created ID exists as a standalone rootfs BatchSandbox in the selected namespace before pausing it.


## Cache conditions


`--scenario` is an experiment label, not automatic proof of cache state. Choose `uncontrolled`, `snapshot-cache-hit`, or `snapshot-cache-miss`. The latter two require `--prepare-script` pointing to a Python preparation/verification script you supply. It runs after pause and Pod deletion, before the timer, as:

text

```
python prepare.py <sandbox-id> <namespace> <context> <scenario>
```


The script must exit zero only after establishing and checking the declared condition. It can inspect the sandbox's owned SandboxSnapshot CR to find the committed image digest. Its stdout is retained as `preparation_evidence` in that trial; keep it concise and free of secrets. There is a bounded preparation timeout. A failure prevents resume and is retained as a failed trial.


For a cache-hit run, pre-pull the **committed snapshot image**, not just the base image, onto every eligible node and verify it is present. For a cache-miss run, use fresh isolated workers or a controlled cache setup and verify the snapshot is absent before resume. Node pinning, image pull policy, registry caching, and layer sharing affect the result; record them in the environment file. Every trial creates a new snapshot, so warmup trials alone do not establish snapshot cache hits. Do not mix scenarios, resource profiles, or proxy modes when comparing percentiles. The runner does not validate a preparation script's claims; inspect its evidence and the retained restored Pod node/image information. Collect kubelet events separately if you need image-pull or scheduling attribution.


## Results and interpretation


The new output path is opened exclusively to avoid overwriting previous results. JSONL contains an environment record, a flushed record for every completed trial (including excluded warmups), and a summary. Trials include their sandbox ID, stage of failure, completed timings, snapshot artifacts, restored Pod node/image information, and cleanup errors. Failed cleanup stops the run and prints the ID for manual deletion; creation response failures also stop and retain a `benchmark_run` metadata value to locate an ambiguously created sandbox; it never silently moves on to accumulating leaked sandboxes.


P50 and P95 use nearest-rank percentiles over **successful measured trials**. The summary separately reports measured failure rate and cleanup failures. A failure at a later stage does not enter partial timings into the percentile population. Warmups never enter the measured statistics. An all-failed run has null percentiles. A nonzero exit status indicates a trial or cleanup failure, including warmups. Interruptions leave the flushed records on disk; only a final summary with `completed_requested_trials: true` indicates a completed run.


Thirty samples are a starting point, not a stable tail-latency claim. Increase sample count, repeat independent runs, retain raw samples, and report successes, timeouts, failures, and environment alongside percentiles. Compare baseline and candidate revisions under the same conditions without machine-speed thresholds in CI. This guide provides a harness; it contains no measured performance claim.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/kubernetes-resume-benchmark.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/pod-recovery`

Return to top

# Pod Provision Failure Recovery


When a BatchSandbox pod lands on an unhealthy node, provisioning can stall before the pod ever becomes Ready. The most common class is a main container image pull that fails persistently — for example `ImagePullBackOff` caused by a full node disk:

text

```
failed to prepare extraction snapshot ...: no space left on device
```


The sandbox stays `Pending` forever: kubelet keeps retrying on the same broken node, and nothing recovers the sandbox. The controller replaces such pods automatically during initial startup, so the scheduler gets a chance to place the recreated pod on a healthy node.


## Behavior


The controller watches sandboxes that have **never been Ready** (`Phase` is `Pending` or empty). A pod is considered stuck when it stays in one of the tracked failure conditions longer than the threshold. Today's tracked conditions:


- **Image pull failures** — `ImagePullBackOff` / `ErrImagePull`, typically caused by a broken node (for example a full disk).
- **Kubelet admission rejections** — the scheduler placed the pod, but kubelet's local resource ledger disagreed (insufficient CPU, memory, or ephemeral storage; node cordoned or not ready; node-pressure eviction). These pods land in `Failed` with reasons like `OutOfcpu`, `OutOfmemory`, `OutOfephemeral-storage`, `Evicted`, `NodeNotSchedulable`, `KubeletNotReady`, or `UnexpectedAdmissionError`, and Kubernetes never retries them on its own. The tracked rejection reason set is configurable via `pod-recovery-admission-reasons` (see [Configuration](https://open-sandbox.ai/guides/pod-recovery#configuration)).
## Behavior ​
## Configuration ​
## Monitoring ​





For a stuck pod:


1. The controller deletes it. The sandbox recreates the pod from its template and the pod is rescheduled like any new pod.
2. Replacement attempts are bounded: after `pod-recovery-max-attempts` replacements, the controller stops and records a `PodRecoveryLimitReached` warning event. The sandbox stays `Pending` and needs operator attention.
3. Updating the sandbox template (for example, fixing the image) resets the replacement attempts.


Intentionally excluded


`CreateContainerConfigError` is a spec problem that rescheduling cannot fix. Terminal failures (`PodFailed`, `ContainerFailed`, `InitContainerFailed`) keep their existing freeze semantics. `CrashLoopBackOff` is not covered: moving a crashing pod rarely helps and can mask application bugs. Scheduling failures (`Unschedulable`) are left to the kube-scheduler, which retries them automatically. Pool-mode sandboxes have a different lifecycle and are out of scope.


### Broken images


An image that cannot be pulled **from any node** (missing tag or manifest, repository does not exist, or denied access) fails identically after every replacement. The controller recognizes these cases and does **not** waste replacement attempts: the pod stays, and an `ImagePullPermanentFailure` warning event names the image error. Fix the image or credentials; once fixed, the pod recovers on its next pull attempt without a restart.


Interplay with upper-layer Pending watchdogs


If an upper-layer manager tears down sandboxes stuck in `Pending` after its own timeout (for example ~7.5 minutes), note that with the default settings (`1m` threshold, 3 attempts) the controller finishes its recovery attempts within roughly 4 minutes — before such a watchdog fires. Raising `pod-recovery-stuck-threshold` above about a third of the watchdog timeout means replacement attempts may still be in flight when the sandbox gets torn down.


Large images and cold pulls


A low threshold replaces pods whose image pull simply takes longer than the threshold. While kubelet is actively pulling, the container shows `ContainerCreating` (not counted); only explicit pull failures advance the timer. If your clusters pull very large images from slow registries, raise `pod-recovery-stuck-threshold`.


## Configuration


Feature configuration lives in the `feature-flags` ConfigMap in the controller's namespace (plain `data` key-value entries). Changes are hot-reloaded without restarting the controller:

yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: feature-flags
  namespace: opensandbox-system  # the controller's namespace
data:
  # How long a pod must stay stuck in a tracked failure condition during
  # initial startup before it is replaced. Defaults to 1m.
  pod-recovery-stuck-threshold: "1m"
  # Maximum number of stuck-pod replacements per BatchSandbox template.
  # Defaults to 3.
  pod-recovery-max-attempts: "3"
  # Optional: comma-separated kubelet admission rejection reasons that
  # replacement can recover. When set, it replaces the built-in set
  # (NodeNotSchedulable, KubeletNotReady, UnexpectedAdmissionError, Evicted);
  # the OutOf* family (OutOfcpu, OutOfmemory, ...) always applies. Useful for
  # vendor-specific kubelet rejection reasons.
  # pod-recovery-admission-reasons: "KubeletNotReady,Evicted"
```


Missing or invalid entries fall back to the built-in defaults (`1m` / `3`), and deleting the ConfigMap restores the defaults.


Helm (controller chart) renders this ConfigMap from values:

yaml

```
controller:
  podRecovery:
    stuckThreshold: "1m"
    maxAttempts: 3
    # Optional; leave empty for the built-in admission reasons.
    admissionReasons: ""
```


## Monitoring


Events recorded on the BatchSandbox:


| Event | Type | Meaning |
| --- | --- | --- |
| `ReplacedStuckPod` | Normal | A stuck pod was deleted and will be recreated on another node. |
| `PodRecoveryLimitReached` | Warning | Replacement attempts are exhausted; the sandbox stays `Pending` and needs operator attention. |
| `ImagePullPermanentFailure` | Warning | The image itself cannot be pulled (missing manifest/repository or denied access); fix the image or credentials. |


Prometheus metrics on the controller metrics endpoint:


| Metric | Labels | Description |
| --- | --- | --- |
| `opensandbox_pod_recovery_replacements_total` | `condition` | Stuck pods replaced during initial startup. |
| `opensandbox_pod_recovery_skips_total` | `condition`, `reason` | Stuck pods detected but not replaced; `reason` is `permanent_failure` (broken image) or `budget_exhausted` (operator attention needed). |


To find affected sandboxes:

bash

```
kubectl get events --field-selector reason=ReplacedStuckPod,reason=PodRecoveryLimitReached,reason=ImagePullPermanentFailure
```[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/pod-recovery.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/egress-sse-truncation`

Return to top

# Egress Mitmproxy: Large SSE Chunks Truncated at the Tail


## Symptom


Sandboxes calling an LLM API through the egress sidecar sometimes receive a **truncated SSE stream**: a `data:` event larger than ~1 MB is cut off near the end, and the SDK reports malformed JSON or a dropped connection. The lost amount varies (a few bytes to hundreds of KB).


## Root cause


Byte-level instrumentation of the full data path shows this is **standard TCP RST semantics**, not a mitmproxy or OpenSandbox bug:


1. The upstream closes the connection while data is still unread in its receive buffer (e.g. a gateway that streams a response without consuming the client's request body). The kernel sends **TCP RST** instead of a clean FIN.
2. Per [RFC 793](https://www.rfc-editor.org/rfc/rfc793), a RST discards the receiver's unread kernel receive buffer — the unread tail of the response is lost before any application code sees it.
3. mitmproxy's h11 parser then hard-errors (`incomplete chunked read`), the flow is killed and the client connection closed.
## Symptom ​
## Root cause ​
## Reproduce ​
## Fix (gateway side) ​
## Status ​







Confirmed by a controlled A/B/C experiment (same server code, payload, proxy and client; only the close behavior differs):


| Close behavior | mitmproxy TCP signature | Client result |
| --- | --- | --- |
| A. Unread request data on close → kernel RST | `ConnectionResetError` | Truncated, 5/5 |
| B. Request consumed, close → clean FIN | clean EOF | Complete, 5/5 |
| C. Request consumed + `SO_LINGER=0` forced RST (empty receive buffer) | `ConnectionResetError` | Truncated, 4/5 |


Cell C is the smoking gun: **RST alone reproduces the truncation even with no unread data; FIN never does**. A direct slow-reading client loses the whole body against server A and nothing against server B, so the loss is purely a function of how much of the tail is still unread when the RST lands. HTTP/2 upstreams and keep-alive connections are unaffected.


## Reproduce


Scripts in [`components/egress/tests/mitm-sse-truncation/`](https://github.com/opensandbox-group/OpenSandbox/blob/main/components/egress/tests/mitm-sse-truncation/run.sh) drive a local `mitmdump` (same options as egress transparent mode) against a synthetic RST-closing SSE upstream:

bash

```
cd components/egress
./tests/mitm-sse-truncation/run.sh            # reproduce the truncation (TLS, 4 MiB, RST close)
./tests/mitm-sse-truncation/run.sh --plain     # controls that must pass
./tests/mitm-sse-truncation/run.sh --delay-close 1
./tests/mitm-sse-truncation/run.sh --read-request
./tests/mitm-sse-truncation/run.sh --probe --keep-workdir   # show the error hook in the mitmdump log
```


Requires `python3`, `openssl`, `mitmdump` (pass `--mitmdump PATH` if not on `PATH`). Options: `--size`, `--iterations`, `--delay-close`, `--plain`, `--read-request`, `--probe`, `--mitmdump`, `--port`, `--upstream-port`, `--workdir`, `--keep-workdir`.


## Fix (gateway side)


There is no code fix in mitmproxy or OpenSandbox — the bytes are gone from the kernel. The fix belongs to the upstream server.


**Confirm it is a RST first** (run on/in front of the gateway while reproducing):

bash

```
tcpdump -ni any 'tcp port 443 and tcp[tcpflags] & (tcp-rst) != 0'   # RST right after the last response byte, no FIN
netstat -s | grep -i reset
# from a client: "Recv failure: Connection reset by peer" / curl: (56) instead of a clean EOF
```


**Then fix the close behavior** — the rule: consume the request before closing; for SSE, prefer not closing at all:


- **nginx**: keep `lingering_close on` (default) with `lingering_time 30s` / `lingering_timeout 5s`; check this especially if `proxy_request_buffering off` was set.
- **FastAPI / uvicorn / Starlette**: read the request body before streaming (`await request.body()`), otherwise a streaming response followed by close can leave the body unread → RST.
- **Go net/http**: drain the body explicitly (`io.Copy(io.Discard, r.Body)`); Go does not drain for you. Never use `SO_LINGER` 0 (`SetLinger(0)`) on streaming responses.
- **Generic**: prefer keep-alive (end chunked bodies with `0\r\n\r\n`); if you must close, drain the receive buffer first; HTTP/2 connections avoid this whole class of failure.


If the gateway cannot be changed: route the sandbox to the gateway over HTTP/2, or front it with a proxy that consumes the request body and forwards keep-alive.


## Status


- mitmproxy upstream: [mitmproxy/mitmproxy#8364](https://github.com/mitmproxy/mitmproxy/issues/8364) — closed as not-a-bug (TCP RST semantics).
- OpenSandbox tracking: [opensandbox-group/OpenSandbox#1461](https://github.com/opensandbox-group/OpenSandbox/issues/1461) — awaiting field confirmation.


A bigger egress-side read buffer was considered and measured: it shrinks the loss window at burst rate but never changes the user-visible outcome (the trailing SSE event is lost either way), so no patch is shipped.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/egress-sse-truncation.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/qemu-vmstate-snapshots`

Return to top

# QEMU VMState Snapshots


This guide explains how to prepare, deploy, and validate a QEMU-in-runc workload that supports process-level pause and resume. The workload runs QEMU inside a normal runc container; it does not use a virtualized Kubernetes `RuntimeClass`.


This mode is experimental. It restores the QEMU Guest memory, vCPU, and migratable device state. Other processes in the outer runc container restart from the `BatchSandbox` Pod template.


The initial `qemu-v1` implementation supports pause and resume of the same `BatchSandbox`. The public snapshot clone API does not yet restore QEMU VMState because its snapshot record does not persist the complete Pod template and QEMU launch plan. A standalone public snapshot operation resumes its source VM after publishing the artifacts.


## State and artifact model


| State | Storage |
| --- | --- |
| Outer container rootfs | Existing rootfs snapshot image |
| Writable guest qcow2 overlay | Rootfs snapshot image; the overlay must not be under a Kubernetes volume mount |
| Guest RAM, vCPU, and emulated device state | VMState image containing a zstd-compressed QEMU migration stream |
| Immutable guest base image | Original image layer or an independently available read-only volume |
| PVC, hostPath, cloud disk, network peer state | Not copied by OpenSandbox |


Both images are pushed to the configured image Registry and recorded by manifest digest in one `SandboxSnapshot.status`. Resume never relies on mutable tags.


## Prepare the QEMU workload image
## State and artifact model ​
## Prepare the QEMU workload image ​
## Pause and resume sequence ​
## Production deployment with Helm ​
## Validation ​
## Troubleshooting ​








QEMU support is a contract between the workload image and OpenSandbox. The image must:


1. start QEMU with a QMP Unix socket;
2. generate an OpenSandbox launch manifest from the effective QEMU settings;
3. keep each writable Guest overlay captured by v1 in the container rootfs;
4. recognize the OpenSandbox restore environment and add QEMU `-incoming`;
5. become Ready only after the QMP socket and Guest service are available;
6. for an internal BatchSandbox pause snapshot, ensure that workload-controlled processes do not independently resume the source VM via QMP (e.g. `cont`) or restart the source QEMU process after migration export and before the source Pod is deleted (this does not restrict the snapshot worker from resuming the source on failure, or during standalone public snapshots).


### Declare the Pod template contract


Set these annotations on the Pod template that creates the QEMU container. For a standalone sandbox, use `BatchSandbox.spec.template.metadata`. For a pooled sandbox, use `Pool.spec.template.metadata` so the allocated Pod carries the contract.

yaml

```
annotations:
  sandbox.opensandbox.io/checkpoint-provider: qemu
  sandbox.opensandbox.io/qemu-container: qemu
  sandbox.opensandbox.io/qemu-qmp-socket: /run/qemu/qmp.sock
  sandbox.opensandbox.io/qemu-launch-manifest: /run/qemu/launch.json
  # Optional: constrain restore to compatible nodes.
  sandbox.opensandbox.io/qemu-required-node-class: shenlong-v1
```


| Annotation | Required | Purpose |
| --- | --- | --- |
| `checkpoint-provider` | Yes | Selects the `qemu` provider. OpenSandbox does not scan process names. |
| `qemu-container` | Yes | Names the Pod container that owns QEMU, QMP, and the launch manifest. |
| `qemu-qmp-socket` | Yes | Clean absolute path of the QMP Unix socket inside that container. |
| `qemu-launch-manifest` | Yes | Clean absolute path of the OpenSandbox launch manifest inside that container. |
| `qemu-required-node-class` | No | Restricts restore to nodes carrying the matching OpenSandbox QEMU node-class label. |


The paths are container paths. They do not need to be mounted into the controller Pod. The snapshot worker reaches the target container through the node container runtime.


### Generate the OpenSandbox launch manifest


The launch manifest is defined by OpenSandbox. It is not a native QEMU file, and QEMU does not create it automatically. The workload image owner is responsible for producing it before the Pod becomes Ready.


Generate the file in the container entrypoint from the same effective values used to build the QEMU command. Do not bake a static file into the Docker image when CPU, memory, disks, or devices can change through environment variables or the Pod template.


Example launch manifest:

json

```
{
  "formatVersion": "qemu-v1",
  "architecture": "amd64",
  "qemuVersion": "6.2.0",
  "machineType": "pc-q35-6.2",
  "cpuModel": "host",
  "vcpus": 2,
  "memoryBytes": 536870912,
  "qemuConfigDigest": "sha256:...",
  "disks": [
    {
      "id": "osdisk",
      "overlayPath": "/vm/state.qcow2",
      "capture": "rootfs"
    }
  ]
}
```


| Field | Meaning |
| --- | --- |
| `formatVersion` | Must be `qemu-v1`. |
| `architecture` | Guest host architecture used by QEMU, for example `amd64`. |
| `qemuVersion` | Version reported by the running QEMU process. The worker verifies this value through QMP. |
| `machineType` | Explicitly versioned machine type, for example `pc-q35-6.2`. |
| `cpuModel` | Effective QEMU CPU model. `host` normally requires homogeneous restore nodes. |
| `vcpus` | Effective vCPU count. |
| `memoryBytes` | Effective Guest RAM size in bytes. |
| `qemuConfigDigest` | Workload-generated SHA-256 identity of compatibility-sensitive QEMU configuration. |
| `disks` | Writable overlays and their capture policy. v1 supports only `capture: rootfs`. |


`qemuConfigDigest` is an opaque compatibility value in v1. Compute it deterministically from a canonical representation of machine, CPU, memory, firmware, disk, network, and device settings. Exclude transient values such as PID, timestamps, QMP paths, and generated socket names. OpenSandbox records the digest but does not reconstruct the QEMU command line from it.


Write the manifest atomically so a concurrent snapshot cannot read a partial JSON file:

bash

```
runtime_dir=/run/qemu
manifest_tmp="$runtime_dir/launch.json.tmp"
manifest="$runtime_dir/launch.json"

mkdir -p "$runtime_dir"
cat >"$manifest_tmp" <<EOF
{
  "formatVersion": "qemu-v1",
  "architecture": "amd64",
  "qemuVersion": "$qemu_version",
  "machineType": "$machine_type",
  "cpuModel": "$cpu_model",
  "vcpus": $vcpus,
  "memoryBytes": $memory_bytes,
  "qemuConfigDigest": "$qemu_config_digest",
  "disks": [
    {"id":"osdisk","overlayPath":"/vm/state.qcow2","capture":"rootfs"}
  ]
}
EOF
mv "$manifest_tmp" "$manifest"
```


The reference E2E entrypoint shows the manifest and QEMU arguments being built from one set of variables. See the [reference entrypoint](https://github.com/alibaba/OpenSandbox/blob/main/kubernetes/test/e2e_qemu/testdata/entrypoint.sh).


### Expose QMP and support restore


Create the declared QMP Unix socket when QEMU starts:

bash

```
qemu_args+=(
  -qmp "unix:/run/qemu/qmp.sock,server=on,wait=off"
)
```


QMP controls the live QEMU process and transports the migration stream. The launch manifest separately declares compatibility and disk-capture intent that cannot be recovered reliably from QMP alone.


The workload entrypoint must detect `OPENSANDBOX_RESTORE_MODE=qemu-v1` and start QEMU with the loader stream supplied in `OPENSANDBOX_VMSTATE_DIR`:

bash

```
if [[ "${OPENSANDBOX_RESTORE_MODE:-}" == "qemu-v1" ]]; then
  test -x "$OPENSANDBOX_VMSTATE_DIR/vmstate-loader"
  qemu_args+=(
    -incoming
    "exec:$OPENSANDBOX_VMSTATE_DIR/vmstate-loader stream --dir $OPENSANDBOX_VMSTATE_DIR"
  )
fi
```


OpenSandbox injects the restore directory and loader; the workload still owns the complete QEMU command line. It must recreate the same machine, CPU, memory, firmware, disks, network, and device topology before consuming the incoming stream.


### Keep the writable overlay in the rootfs


Every disk declared with `capture: rootfs` must be a file in the QEMU container's writable rootfs. It must not resolve under a Kubernetes `volumeMount` or `volumeDevice`, including PVC, hostPath, projected volume, or `emptyDir`. `nerdctl commit` does not capture those mounts, and the snapshot worker rejects the configuration instead of creating an incomplete snapshot.


An immutable base image can come from the original image layer or another independently available read-only source. Existing user init containers run again before the injected VMState loader on resume, so they must be idempotent and must not overwrite the restored writable overlay.


## Pause and resume sequence


1. The controller resolves the annotated QEMU container and schedules the snapshot Job on the same node.
2. The worker validates that every writable overlay declared as `capture: rootfs` is outside the container's Kubernetes volume mount paths.
3. The worker uses QMP migration to export VM state, compresses it with zstd, and puts it into a standard container image.
4. After QEMU reaches post-migration state, the worker freezes companion outer containers (leaving the QEMU container unfrozen to avoid kernel worker freeze deadlocks while QEMU remains quiesced in postmigrate), commits their root filesystems, and pushes both image types.
5. The controller publishes rootfs and VMState manifest digests atomically, then removes the source Pod.
6. On resume, a loader init container restores and verifies the VMState files in an `emptyDir`. It is appended after all user init containers.
7. The recreated QEMU container consumes the migration stream. Other outer-container processes start normally from the Pod template.


`savevm` is not used. It creates an internal snapshot coupled to qcow2 storage and is not the transport for live Guest RAM used here.


## Production deployment with Helm


There is no QEMU-specific Helm feature switch. Helm installs the cluster-level snapshot capability; each `BatchSandbox` or `Pool` Pod template opts in through the annotations above. Rootfs-only workloads continue to use the existing behavior.


### Prerequisites


- Linux nodes with `/dev/kvm` exposed to the QEMU container.
- The image Registry must accept Docker schema 2 or OCI image manifests and be reachable from both snapshot Jobs and kubelet/containerd.
- The QEMU version, versioned machine type, CPU model, vCPU count, RAM size, device configuration digest, and optional node class must match on restore.
- The snapshot Job needs the host containerd runtime directory, host PID namespace, and `SYS_PTRACE`. It already operates inside the node-level trust boundary because it controls the containerd socket. Pod Security and admission policies must explicitly allow this Job.
- VMState can contain credentials and user data from Guest RAM. Apply the same access control, encryption, retention, and deletion policy as sensitive persistent storage.
- Plan Registry capacity from measured compressed payload size. Compression depends on Guest memory contents; it is not guaranteed to be small.


The controller image and image-committer image must both come from a version that supports `qemu-v1`. In particular, do not rely on an older chart default for `controller.snapshot.imageCommitterImage`; override it explicitly.


### Create Registry credentials


The commit Job and resumed Pod run in the sandbox namespace, so the referenced Secrets must exist in every namespace that uses snapshot and restore:

bash

```
kubectl -n sandbox-team create secret docker-registry snapshot-registry \
  --docker-server=registry.example.com \
  --docker-username='<username>' \
  --docker-password='<password-or-token>'
```


One Secret can be used for push, image-committer pull, and resume pull when the credential has all three permissions. Production deployments may use separate least-privilege Secrets with the same names in each sandbox namespace.


### Configure and install the chart


Create a values file:

yaml

```
controller:
  image:
    repository: registry.example.com/opensandbox/controller
    tag: qemu-v1
  snapshot:
    imageCommitterImage: registry.example.com/opensandbox/image-committer:qemu-v1
    containerdSocketPath: /var/run/containerd/containerd.sock
    commitJobTimeout: 15m
    registry: registry.example.com/opensandbox-snapshots
    registryInsecure: false
    snapshotPushSecret: snapshot-registry
    imageCommitterPullSecret: snapshot-registry
    resumePullSecret: snapshot-registry
```


Install or upgrade the controller. On a fresh cluster, install the base chart first — the controller chart no longer ships the CRDs:

bash

```
helm upgrade --install base ./manifests/charts/base

helm upgrade --install opensandbox-controller \
  ./manifests/charts/controller \
  --namespace opensandbox-system \
  --create-namespace \
  --values qemu-snapshot-values.yaml
```


Sync the CRDs into the base chart (`make -C manifests helm-gen-crds`) and upgrade `base` so the updated `SandboxSnapshot` CRD lands. Verify the deployed capability before creating workloads:

bash

```
kubectl -n opensandbox-system rollout status \
  deployment/opensandbox-controller-manager
kubectl -n opensandbox-system get deployment,pod
kubectl get crd sandboxsnapshots.sandbox.opensandbox.io
kubectl get crd sandboxsnapshots.sandbox.opensandbox.io \
  -o jsonpath='{.spec.versions[0].schema.openAPIV3Schema.properties.status.properties.virtualMachine.type}{"\n"}'
```


Confirm that cluster admission permits the node-trusted snapshot Job. QEMU mode requires the host PID namespace, `SYS_PTRACE`, and the host containerd runtime directory. The QEMU workload itself needs `/dev/kvm` and normally runs privileged unless the platform supplies narrower device permissions.


For heterogeneous fleets, label compatible restore nodes and declare the matching class on the workload:

bash

```
kubectl label node <node> \
  sandbox.opensandbox.io/qemu-node-class=shenlong-v1
```

yaml

```
metadata:
  annotations:
    sandbox.opensandbox.io/qemu-required-node-class: shenlong-v1
```


By default, snapshot image names are generated below the configured Registry prefix. A QEMU sandbox produces normal container rootfs images such as `<prefix>/<sandbox>-<container>:<tag>` and a VMState image such as `<prefix>/<sandbox>-vmstate:<tag>`. Both artifact names can be customized with [`--snapshot-image-uri-template`](https://open-sandbox.ai/guides/pause-resume#custom-image-names); VM-state artifacts receive `ContainerName` and `ArtifactKind` equal to `vmstate`. Resume resolves and uses their immutable manifest digests.


## Validation


The dedicated E2E allocates a warm QEMU-in-runc Pod from a `Pool`, writes independent values into an anonymous mmap, the raw Guest disk, and the outer rootfs, snapshots both images, and restores a standalone Pod. It verifies Pool replenishment and detachment, immutable rootfs and VMState image digests, loader completion, snapshot cleanup, all three values, the Guest boot ID, and the live counter:

bash

```
cd kubernetes
make test-e2e-qemu
```


The test requires Linux amd64, Docker, Kind, kubectl, and `/dev/kvm`. By default it deploys an isolated `registry:2` Pod in the Kind cluster. Set `QEMU_E2E_SNAPSHOT_REGISTRY` and `QEMU_E2E_DOCKER_CONFIG` to verify the same flow against an authenticated external Registry; the two repositories are `<prefix>/qemu-rootfs` and `<prefix>/qemu-vmstate`. Set `KEEP_QEMU_E2E_CLUSTER=true` to retain the dedicated Kind cluster for diagnostics. See the [E2E README](https://github.com/alibaba/OpenSandbox/tree/main/kubernetes/test/e2e_qemu) for all overrides.


### Reusable Kind validation environment


The E2E harness can build the images, create a dedicated KVM-enabled Kind cluster, deploy the controller and Registry, run the reference Pool flow, and leave the environment available for manual checks:

bash

```
cd kubernetes
KEEP_QEMU_E2E_CLUSTER=true make test-e2e-qemu
```


The resulting context is `kind-opensandbox-qemu-vmstate-e2e`. The controller runs in `opensandbox-system`, while the in-cluster `registry:2` Pod and the automated test objects run in `qemu-vmstate-e2e`:

bash

```
kubectl --context kind-opensandbox-qemu-vmstate-e2e \
  -n opensandbox-system get deploy,pod
kubectl --context kind-opensandbox-qemu-vmstate-e2e \
  -n qemu-vmstate-e2e get pod,service,pool,batchsandbox
```


To exercise an authenticated external Registry instead, provide its repository prefix and a local Docker `config.json`; the harness creates the temporary Kubernetes pull/push Secret without printing its contents:

bash

```
QEMU_E2E_SNAPSHOT_REGISTRY=registry.example.com/team \
QEMU_E2E_DOCKER_CONFIG=/path/to/config.json \
KEEP_QEMU_E2E_CLUSTER=true \
make test-e2e-qemu
```


The commands below use a separate `qemu-manual` namespace, so the retained E2E objects do not need to be deleted first.


### Manual validation in a prepared Kind cluster


This flow deliberately leaves lifecycle actions to the operator. It assumes the controller, snapshot Registry, image-committer image, and demo QEMU image are already installed in a Kind cluster with `/dev/kvm`. From the repository root, select that cluster and create only the standalone `BatchSandbox`:

bash

```
export OSB_QEMU_CONTEXT=kind-opensandbox-qemu-vmstate-e2e
export OSB_QEMU_NAMESPACE=qemu-manual
export OSB_QEMU_SANDBOX=qemu-standalone
export OSB_QEMU_POD=qemu-standalone-0

test -c /dev/kvm
kubectl --context "$OSB_QEMU_CONTEXT" get nodes
kubectl --context "$OSB_QEMU_CONTEXT" -n opensandbox-system \
  rollout status deployment/opensandbox-controller-manager
kubectl --context "$OSB_QEMU_CONTEXT" apply \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/standalone.yaml
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  wait --for=condition=Ready pod/"$OSB_QEMU_POD" --timeout=180s
```


Before pausing, verify the exact contract that the snapshot worker will use:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get pod "$OSB_QEMU_POD" \
  -o jsonpath='{.metadata.annotations}{"\n"}'
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  test -S /run/qemu-e2e/qmp.sock
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  cat /run/qemu-e2e/launch.json
```


Do not continue if the annotated container, socket path, manifest path, or effective QEMU settings disagree.


The demo Guest runs the HTTP server and the mutable memory map in the same PID 1 process. QEMU user networking forwards the outer container's loopback port `18080` to Guest port `8080`; the service is not exposed on the Pod IP.


| Endpoint | Purpose |
| --- | --- |
| `GET /healthz` | Verify that the resumed Guest process is serving requests |
| `PUT /value` | Store a value of up to 512 bytes in the process memory map |
| `GET /value` | Read the current memory-map value |
| `GET /status` | Read PID, Guest boot ID, mmap-backed live counter, and value |
| `PUT /disk` | Store a marker in the raw writable Guest disk |
| `GET /disk` | Read the raw Guest disk marker |


Define a phase waiter and put three independent markers in Guest memory, the Guest disk, and the outer container rootfs:

bash

```
wait_for_sandbox_phase() {
  local wanted=$1
  local phase=
  for _ in $(seq 1 180); do
    phase=$(kubectl --context "$OSB_QEMU_CONTEXT" \
      -n "$OSB_QEMU_NAMESPACE" get batchsandbox "$OSB_QEMU_SANDBOX" \
      -o jsonpath='{.status.phase}' 2>/dev/null || true)
    if [[ "$phase" == "$wanted" ]]; then
      return 0
    fi
    sleep 2
  done
  echo "timed out waiting for phase=$wanted; last phase=$phase" >&2
  return 1
}

export OSB_MEMORY_TOKEN="MANUAL-MMAP-$(date -u +%Y%m%dT%H%M%SZ)"
export OSB_DISK_TOKEN="MANUAL-DISK-$(date -u +%Y%m%dT%H%M%SZ)"
export OSB_ROOTFS_TOKEN="MANUAL-ROOTFS-$(date -u +%Y%m%dT%H%M%SZ)"

kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  curl --fail --silent --show-error --request PUT \
  --data-binary "$OSB_MEMORY_TOKEN" http://127.0.0.1:18080/value
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  curl --fail --silent --show-error --request PUT \
  --data-binary "$OSB_DISK_TOKEN" http://127.0.0.1:18080/disk
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- sh -c \
  'mkdir -p /var/lib/opensandbox && printf "%s" "$1" > /var/lib/opensandbox/rootfs-marker' \
  sh "$OSB_ROOTFS_TOKEN"

OSB_BEFORE=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  curl --fail --silent --show-error http://127.0.0.1:18080/status)
OSB_SOURCE_UID=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get pod "$OSB_QEMU_POD" -o jsonpath='{.metadata.uid}')
printf 'before: %s\nsource uid: %s\n' "$OSB_BEFORE" "$OSB_SOURCE_UID"
```


In another terminal, watch the resources involved in pause and resume:

bash

```
watch -n 1 kubectl --context "$OSB_QEMU_CONTEXT" \
  -n "$OSB_QEMU_NAMESPACE" get batchsandbox,sandboxsnapshot,pod,job
```


The initial manifest intentionally omits `spec.pause`: setting it to `false` on a brand-new object is interpreted as an explicit resume request. Pause the sandbox by adding `spec.pause: true`, then inspect the two immutable image artifacts:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  edit batchsandbox "$OSB_QEMU_SANDBOX"
wait_for_sandbox_phase Paused

export OSB_SNAPSHOT_NAME="$OSB_QEMU_SANDBOX-pause"
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get sandboxsnapshot "$OSB_SNAPSHOT_NAME" -o yaml
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  wait --for=delete pod/"$OSB_QEMU_POD" --timeout=120s
```


The snapshot must report `status.format: qemu-v1`, a rootfs image digest under `status.containers`, and a different VMState image digest plus a non-zero compressed size under `status.virtualMachine`.


Resume by editing `spec.pause` to `false`, then verify process-level continuity and both filesystem layers:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  edit batchsandbox "$OSB_QEMU_SANDBOX"
wait_for_sandbox_phase Succeed
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  wait --for=condition=Ready pod/"$OSB_QEMU_POD" --timeout=180s

OSB_AFTER=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  curl --fail --silent --show-error http://127.0.0.1:18080/status)
OSB_AFTER_DISK=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- \
  curl --fail --silent --show-error http://127.0.0.1:18080/disk)
OSB_AFTER_ROOTFS=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_QEMU_POD" -c qemu -- cat /var/lib/opensandbox/rootfs-marker)
OSB_RESTORED_UID=$(kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get pod "$OSB_QEMU_POD" -o jsonpath='{.metadata.uid}')

OSB_BEFORE_BOOT_ID=$(printf '%s\n' "$OSB_BEFORE" | sed -n 's/.*"boot_id":"\([^"]*\)".*/\1/p')
OSB_AFTER_BOOT_ID=$(printf '%s\n' "$OSB_AFTER" | sed -n 's/.*"boot_id":"\([^"]*\)".*/\1/p')
OSB_BEFORE_COUNTER=$(printf '%s\n' "$OSB_BEFORE" | sed -n 's/.*"counter":\([0-9]*\).*/\1/p')
OSB_AFTER_COUNTER=$(printf '%s\n' "$OSB_AFTER" | sed -n 's/.*"counter":\([0-9]*\).*/\1/p')

[[ "$OSB_SOURCE_UID" != "$OSB_RESTORED_UID" ]]
[[ "$OSB_BEFORE_BOOT_ID" == "$OSB_AFTER_BOOT_ID" ]]
((OSB_AFTER_COUNTER > OSB_BEFORE_COUNTER))
[[ "$OSB_AFTER" == *"\"value\":\"$OSB_MEMORY_TOKEN\""* ]]
[[ "$OSB_AFTER_DISK" == *"\"value\":\"$OSB_DISK_TOKEN\""* ]]
[[ "$OSB_AFTER_ROOTFS" == "$OSB_ROOTFS_TOKEN" ]]

printf 'after: %s\ndisk: %s\nrootfs: %s\nrestored uid: %s\n' \
  "$OSB_AFTER" "$OSB_AFTER_DISK" "$OSB_AFTER_ROOTFS" "$OSB_RESTORED_UID"
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get pod "$OSB_QEMU_POD" -o jsonpath='{range .status.initContainerStatuses[*]}{.name}{"="}{.state.terminated.reason}{"\n"}{end}'
```


All assertions must return zero. The Pod UID must change, the Guest boot ID must remain the same, the live counter must increase, all three tokens must match, and the VMState loader init container must report `Completed`. The internal `SandboxSnapshot` is deleted after a successful resume. Remove only the test object when finished; the Kind infrastructure remains available:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" delete \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/standalone.yaml
```


### Manual validation with a Pool


Create the Pool first and wait for its warm QEMU Pod. Then create a `BatchSandbox` that allocates that Pod:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" apply \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/pool.yaml
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get pool qemu-pool -w
```


After the Pool reports ready capacity, stop the watch and run:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" apply \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/pooled-sandbox.yaml
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get batchsandbox qemu-pooled -w
```


Read the allocated Pod name from the allocation annotation and write the same three markers used by the standalone case:

bash

```
export OSB_POOLED_POD=$(kubectl --context "$OSB_QEMU_CONTEXT" \
  -n "$OSB_QEMU_NAMESPACE" get batchsandbox qemu-pooled \
  -o jsonpath='{.metadata.annotations.sandbox\.opensandbox\.io/alloc-status}' \
  | jq -r '.pods[0]')

export OSB_POOL_MEMORY_TOKEN="POOL-MMAP-$(date -u +%Y%m%dT%H%M%SZ)"
export OSB_POOL_DISK_TOKEN="POOL-DISK-$(date -u +%Y%m%dT%H%M%SZ)"
export OSB_POOL_ROOTFS_TOKEN="POOL-ROOTFS-$(date -u +%Y%m%dT%H%M%SZ)"

kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_POOLED_POD" -c qemu -- \
  curl --fail --silent --show-error --request PUT \
  --data-binary "$OSB_POOL_MEMORY_TOKEN" http://127.0.0.1:18080/value
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_POOLED_POD" -c qemu -- \
  curl --fail --silent --show-error --request PUT \
  --data-binary "$OSB_POOL_DISK_TOKEN" http://127.0.0.1:18080/disk
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  exec "$OSB_POOLED_POD" -c qemu -- sh -c \
  'mkdir -p /var/lib/opensandbox && printf "%s" "$1" > /var/lib/opensandbox/rootfs-marker' \
  sh "$OSB_POOL_ROOTFS_TOKEN"
```


Run `kubectl edit batchsandbox qemu-pooled -n qemu-manual` and add `spec.pause: true`. On successful pause, verify the Pool-specific handoff:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get batchsandbox qemu-pooled \
  -o jsonpath='phase={.status.phase}{" poolRef="}{.spec.poolRef}{" templateContainers="}{.spec.template.spec.containers[*].name}{"\n"}'
kubectl --context "$OSB_QEMU_CONTEXT" -n "$OSB_QEMU_NAMESPACE" \
  get sandboxsnapshot qemu-pooled-pause -o yaml
```


The phase must be `Paused`. The controller materializes the allocated Pod's template into the `BatchSandbox` and clears `spec.poolRef`; this detach is intentional, so resume creates an independent Pod instead of returning to the Pool. Edit `spec.pause` back to `false`, wait for `qemu-pooled-0` to become Ready, then call `GET /status`, `GET /disk`, and the rootfs marker check against it.


Clean up the Pool example without deleting the Kind cluster:

bash

```
kubectl --context "$OSB_QEMU_CONTEXT" delete \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/pooled-sandbox.yaml
kubectl --context "$OSB_QEMU_CONTEXT" delete \
  -f kubernetes/config/samples/alibaba/qemu-vmstate/pool.yaml
```


## Troubleshooting


| Symptom | Check |
| --- | --- |
| `InvalidCheckpointContract` | Confirm all four required annotations are on the actual Pod template and name an existing container. Paths must be clean and absolute. |
| Launch manifest copy or decode failure | Exec into the annotated container, read the exact path, and verify that the entrypoint writes complete JSON before readiness succeeds. |
| QMP probe failure | Verify that the declared path is a Unix socket and that QEMU uses `server=on,wait=off`. Check whether a supervisor removed or replaced the socket. |
| QEMU version mismatch | Compare `qemuVersion` in the manifest with the running binary. Generate the manifest at container startup instead of baking a stale version into the image. |
| Writable disk rejected | Check every `volumeMount` and `volumeDevice` on the QEMU container. A `capture: rootfs` overlay cannot live below any mounted path. |
| Snapshot Job rejected by admission | Permit the image-committer Job identity to use host PID, `SYS_PTRACE`, and the host containerd runtime directory on snapshot-capable nodes. |
| Snapshot Job `ImagePullBackOff` | Ensure `imageCommitterPullSecret` exists in the sandbox namespace and can pull the configured image-committer image. |
| Resumed Pod `ImagePullBackOff` | Ensure `resumePullSecret` exists in the sandbox namespace and can pull both rootfs and VMState image repositories. |
| QEMU exits while consuming `-incoming` | Compare QEMU version, machine type, CPU model, vCPU count, memory, firmware, disks, network, and device topology with the captured compatibility data. |
| Pod cannot schedule after resume | Check `/dev/kvm`, node affinity, and `qemu-required-node-class` against the node's `qemu-node-class` label. |


Start diagnosis from the snapshot status and commit Job logs:

bash

```
kubectl -n <namespace> get sandboxsnapshot <name> -o yaml
kubectl -n <namespace> get job,pod \
  -l sandbox.opensandbox.io/sandbox-snapshot-name=<name>
kubectl -n <namespace> logs job/<commit-job-name> --all-containers
```[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/qemu-vmstate-snapshots.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/lifecycle-hooks`

Return to top

# Lifecycle Hooks


Lifecycle hooks let a sandbox run declarative commands at defined points in its runtime. OpenSandbox currently supports a blocking `preStart` hook and one or more non-blocking `periodic` hooks.


## Supported hooks


| Hook | Cardinality | When it runs | Failure behavior |
| --- | --- | --- | --- |
| `preStart` | Zero or one | After execd starts listening, before the user entrypoint starts | A failure or timeout prevents the user entrypoint from starting |
| `periodic` | Zero or more | The scheduler starts after `preStart` succeeds and runs each hook on its schedule | A failed or timed-out run is logged and later runs normally continue; if a timed-out process cannot be terminated, that hook is disabled |


Both hooks run inside the sandbox with the sandbox environment. Commands are argument arrays and are executed directly. To use shell syntax such as pipes, redirects, or variable expansion, invoke a shell explicitly, for example `['sh', '-c', 'command > file']`.


![Lifecycle hook timing in bootstrap and execd-as-init modes](https://open-sandbox.ai/assets/lifecycle-hooks-startup.BkL0HGSr.png)
## Supported hooks ​
## Configuration ​
## Current availability ​
## Operational guidance ​






The ordering is the same in both startup modes:


1. execd starts and its HTTP server begins listening.
2. `preStart` runs to completion, if configured.
3. The periodic scheduler starts, if configured.
4. The user entrypoint starts.


In execd-as-init mode, execd remains PID 1 and starts the entrypoint as its supervised child. In bootstrap mode, the bootstrap process starts the entrypoint after execd reports that lifecycle startup completed.


## Configuration


Lifecycle hooks are part of the sandbox creation request:

json

```
{
  "image": { "uri": "ubuntu:24.04" },
  "entrypoint": ["tail", "-f", "/dev/null"],
  "resourceLimits": {
    "cpu": "1",
    "memory": "1Gi"
  },
  "lifecycle": {
    "preStart": {
      "command": ["sh", "-c", "echo ready > /tmp/prestart.done"],
      "timeoutSeconds": 120
    },
    "periodic": [
      {
        "name": "checkpoint",
        "schedule": "@every 5m",
        "command": ["sh", "-c", "date -u >> /tmp/checkpoints.log"],
        "timeoutSeconds": 120
      }
    ]
  }
}
```


### `preStart`


| Field | Required | Description |
| --- | --- | --- |
| `command` | Yes | Non-empty command and argument array |
| `timeoutSeconds` | No | When omitted, defaults to 60 seconds; explicit values must be from 1 through 10800 seconds (3 hours) |


`preStart` runs on each container start. Make the command idempotent so retrying or restarting a sandbox does not corrupt its state.


### `periodic`


| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Non-blank name, unique within the sandbox |
| `schedule` | Yes | Standard five-field cron expression or descriptor such as `@hourly` or `@every 30s` |
| `command` | Yes | Non-empty command and argument array |
| `timeoutSeconds` | No | When omitted, defaults to 60 seconds; explicit values must be from 1 through 300 seconds |


An `@every` interval must be a whole number of seconds and at least one second. Runs of the same named hook never overlap: if the previous run is still active, the next scheduled run is skipped.


## Current availability


Lifecycle hooks currently require the Kubernetes provider. They are rejected by the Docker provider and Fast Sandbox backend. A request cannot combine `lifecycle` with `poolRef`.


The SDKs expose lifecycle fields on their sandbox creation APIs but do not enforce the timeout range. The Server is the authority for request validation. See the language-specific examples in the [SDK documentation](https://open-sandbox.ai/sdks/).


## Operational guidance


- Keep `preStart` bounded and deterministic because the entrypoint waits for it.
- Make periodic work idempotent and safe to retry.
- Store credentials through the platform's supported secret mechanism rather than embedding them in commands.
- Write data that must survive node replacement to durable storage. Lifecycle hooks schedule recovery and synchronization work; they do not make the sandbox filesystem durable by themselves.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/lifecycle-hooks.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/windows-sandbox`

Return to top

# Windows Sandbox


A Windows sandbox runs a Windows guest in a Linux container via KVM/QEMU and is managed end-to-end through the OpenSandbox lifecycle API (create, expose endpoints, delete). The current Windows profile is based on [`dockur/windows`](https://github.com/dockur/windows), with service integration and capabilities provided by OpenSandbox.


## Scope


This guide covers the OpenSandbox Server Windows profile (`platform.os=windows`):


- Create a Windows sandbox
- Check status and endpoints
- Common resources and volume settings
- Delete and cleanup


## How it works


- **Runtime**: [`dockur/windows`](https://github.com/dockur/windows) runs the Windows guest in a Linux container (requires KVM/QEMU), using mount points such as `/storage` and `/boot.iso` for the system disk and install media.
- **Control plane**: On create, OpenSandbox Server injects the Windows profile configuration (devices, capabilities, `execd`, port mappings) and enforces resource checks, state, and endpoint publication.
- **Client**: You call the Lifecycle API or the Python SDK with `platform.os=windows`, then follow create → poll `Running` → get endpoints → use → delete.


## Prerequisites


- Reachable OpenSandbox Server (e.g. `http://localhost:8080`)
- Host meets the Windows profile requirements:
  - `/dev/kvm` present
  - `/dev/net/tun` present- Server `storage.allowed_host_paths` configured for allowed host paths
- A host directory to bind to `/storage` (recommended)
- Optional: a local Windows ISO for `/boot.iso` (cuts repeated download time)


## Key settings and constraints


### Platform and image


- Set `platform: {"os":"windows","arch":"amd64"}` (`arm64` depends on the host)
- Suggested image: `dockurr/windows:latest`; see [`dockur/windows` releases](https://github.com/dockur/windows/releases) and [Docker Hub tags](https://hub.docker.com/r/dockurr/windows/tags)


### Minimum resources
## Scope ​
*This guide covers the OpenSandbox Server Windows profile (platform.os=windows):*

## How it works ​
## Prerequisites ​
## Key settings and constraints ​
*If resourceLimits is set, the server maps it to and overwrites these env vars:*

*Prefer resourceLimits only; do not set those three env vars manually.*

*It also builds or merges USER_PORTS (often 44772,8080,3389,8006).*

## End-to-end example (Python) ​
## FAQ ​








The Windows profile enforces:


- `resourceLimits.cpu >= 2`
- `resourceLimits.memory >= 4G`
- `resourceLimits.disk >= 64G`


### `resourceLimits` vs. environment variables


If `resourceLimits` is set, the server maps it to and overwrites these env vars:


- `CPU_CORES`
- `RAM_SIZE`
- `DISK_SIZE`


Prefer `resourceLimits` only; do not set those three env vars manually.


### Default ports and `USER_PORTS`


The Windows profile wires these ports by default:


- `44772` (execd)
- `8080`
- `3389/tcp`, `3389/udp` (RDP)
- `8006/tcp` (typical web console)


It also builds or merges `USER_PORTS` (often `44772,8080,3389,8006`).


### Storage mounts


- Bind a writable host directory to `/storage`
- Optional: bind an ISO file to `/boot.iso` (`readOnly=true`)
- Host paths must fall under `storage.allowed_host_paths` or the request is rejected


## End-to-end example (Python)


This flow:


1. Create a Windows sandbox
2. Wait until `Running`
3. Get the `44772` endpoint
4. Use the Python SDK against the sandbox
5. Delete the sandbox


### Minimal example

python

```
import os
from datetime import timedelta

from opensandbox import SandboxSync
from opensandbox.config import ConnectionConfigSync
from opensandbox.models.sandboxes import PlatformSpec

BASE_URL = os.getenv("OPEN_SANDBOX_BASE_URL", "http://localhost:8080")
API_KEY = os.getenv("OPEN_SANDBOX_API_KEY", "")


def main() -> None:
    cfg = ConnectionConfigSync(
        domain=BASE_URL,
        api_key=API_KEY or None,
        use_server_proxy=True,
    )

    sbx = None
    try:
        sbx = SandboxSync.create(
            image="dockurr/windows:latest",
            timeout=timedelta(hours=12),
            ready_timeout=timedelta(minutes=30),
            resource={
                "cpu": "4",
                "memory": "8G",
                "disk": "64G",
            },
            env={"VERSION": "11"},
            entrypoint=["cmd", "/c", "echo OpenSandbox Windows profile"],
            platform=PlatformSpec(os="windows", arch="amd64"),
            connection_config=cfg,
        )
        print("created:", sbx.id)

        endpoint = sbx.get_endpoint(44772)
        print("execd endpoint:", endpoint.endpoint)
        print("sdk health:", sbx.is_healthy())
    finally:
        if sbx is not None:
            try:
                sbx.kill()
                print("deleted:", sbx.id)
            finally:
                sbx.close()


if __name__ == "__main__":
    main()
```


> The sample keeps SDK health waiting (`ready_timeout=30m`). Windows cold start can be slow; increase `ready_timeout` as needed. For custom readiness logic, use `skip_health_check=True` and poll for `Running` in your app.


### Advanced options


#### Persistent `/storage`


Bind a host path to `/storage` for a persistent system/user data directory. The directory **need not exist** ahead of time: it may be created on bind mount (fresh), or reused if it already exists. `host.path` must still be under an allowed `storage.allowed_host_paths` prefix, regardless of whether the directory exists.

python

```
from opensandbox.models.sandboxes import Host, Volume

volumes = [
    Volume(
        name="win-storage",
        host=Host(path="/data/opensandbox/windows-storage"),
        mount_path="/storage",
        read_only=False,
    ),
]
# Pass as SandboxSync.create(..., volumes=volumes, ...)
```


#### Existing ISO on the host


Bind a local Windows install ISO read-only to `/boot.iso` to avoid downloading media each time (also requires `allowed_host_paths`; the path must be a **file**):

python

```
from opensandbox.models.sandboxes import Host, Volume

volumes = [
    Volume(
        name="win-iso",
        host=Host(path="/data/iso/Win11_23H2.iso"),
        mount_path="/boot.iso",
        read_only=True,
    ),
]
```


#### Customizing `dockur/windows`


[`dockur/windows`](https://github.com/dockur/windows) is configured with **environment variables**. OpenSandbox passes your `env` into the container as documented upstream. **Install / UX** settings often include:


- `VERSION`: Windows variant code (e.g. `11`, `11l`, `10` — full table in the project README) or, in some cases, a custom ISO `https://` URL
- `USERNAME` / `PASSWORD`: first user and password (defaults in the image if omitted — see upstream)
- `LANGUAGE`: install language (e.g. `English`, `Chinese`)
- `REGION` / `KEYBOARD`: locale and layout (e.g. `en-US`, `zh-CN`)
- Advanced cases may use `DHCP`, `ARGUMENTS` (extra QEMU args), etc. — see the [`dockur/windows` FAQ](https://github.com/dockur/windows)


If you already set CPU, memory, and disk via `resourceLimits`, do **not** repeat the same **resource** keys in `env` as in the dockur docs; see [`resourceLimits` vs. environment variables](https://open-sandbox.ai/guides/windows-sandbox#resourcelimits-vs-environment-variables) above. Other non-resource keys can be combined freely.

python

```
env = {
    "VERSION": "11l",
    "USERNAME": "Docker",
    "PASSWORD": "your-secure-password",
    "LANGUAGE": "Chinese",
    "REGION": "zh-CN",
    "KEYBOARD": "zh-CN",
}
```


For the full list, defaults, and interactions, use the [`dockur/windows` repository](https://github.com/dockur/windows) and image tags.


#### Using your own Windows image


In [`dockur/windows` documentation](https://github.com/dockur/windows), **“your own”** usually means **which Windows install ISO to use** — not a custom recipe unrelated to upstream. The [custom install FAQ](https://github.com/dockur/windows#how-do-i-install-a-custom-image) states:


- For an ISO **not** in the project’s version table, set `VERSION` to the ISO’s **download URL** (`https://...`); the container fetches and installs it.
- If you **already have a local ISO file**, bind it to **`/boot.iso`** as in [Existing ISO on the host](https://open-sandbox.ai/guides/windows-sandbox#existing-iso-on-the-host) above; upstream documents that `VERSION` is then ignored.


In OpenSandbox, set `VERSION` in `env` and, when needed, add a volume for the local ISO at `/boot.iso`, matching the upstream flow; keep `image` as `dockurr/windows` or another compatible upstream image, as in the other examples.


Snippet for the **`VERSION` = ISO URL** case (same as passing `env` in the minimal example):

python

```
env = {
    "VERSION": "https://example.com/path/to/your.iso",
    # same pattern as the minimal example for resource / platform / etc.
}
```


## FAQ


- `Unsupported platform.os 'windows'` on create — server build has no Windows profile; upgrade to a version that includes it.
- `INVALID_PARAMETER` for `resourceLimits.*` — ensure `cpu >= 2`, `memory >= 4G`, `disk >= 64G`.
- Stays `Pending` a long time — first Windows install is slow; check host resources and `/storage` space, and increase wait timeouts.
- Status `Running` but endpoint unreachable — verify `GET /v1/sandboxes/{id}/endpoints/44772` returns a valid address; set `env.USER_PORTS` if you need more ports forwarded.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/windows-sandbox.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/node-agent`

Return to top

# Node Agent configuration


The [Node Agent](https://open-sandbox.ai/architecture/data-plane/node-agent) is an optional DaemonSet that collects sandbox stdout/stderr (and, optionally, syscalls) on every Linux node and writes them to durable storage. This guide covers enabling it, choosing a sink, and the operational rules that protect its delivery guarantees. For the full values reference, see the [node-agent chart README](https://github.com/opensandbox-group/OpenSandbox/tree/main/manifests/charts/node-agent).


## Prerequisites


- A Kubernetes cluster from the [OpenSandbox deployment](https://open-sandbox.ai/deployment/) — the Agent is order-independent, so you can enable it at any time.
- One Agent per Linux node is automatic: the chart pins `kubernetes.io/os: linux`.
- Each node needs local disk for checkpoint state (`hostPaths.state`, default `/var/lib/opensandbox/nodeagent`), which must survive Pod restarts — it is a `hostPath` volume.


The Agent discovers sandbox Pods by identity (`opensandbox.io/id` label, `sandbox` container) and skips pooled warm Pods. No per-Pod configuration is needed.


## Enable the Agent


**Umbrella chart** — set the sub-chart condition:

bash

```
helm upgrade opensandbox opensandbox \
  --namespace opensandbox-system \
  --set opensandbox-node-agent.enabled=true
```


**Standalone chart** — install it directly:

bash

```
helm install node-agent manifests/charts/node-agent \
  --namespace opensandbox-system \
## Prerequisites ​
## Enable the Agent ​
## Choose a sink ​
## Opt into syscall collection ​
## Key values ​
## Metrics ​
*See telemetry for the metric list and shared exporter behavior.*

## Operating rules ​







  --create-namespace
```


Verify the DaemonSet rolled out and the Agent reports ready. Readiness is meaningful: it only turns green when configuration, recovery state, sink target, and host reserves are all valid.

bash

```
kubectl rollout status daemonset -l app.kubernetes.io/component=node-agent -n opensandbox-system

kubectl port-forward -n opensandbox-system daemonset/node-agent 8080:8080
curl http://127.0.0.1:8080/readyz   # {"ready":true,"reasons":[]}
```


Always set a real cluster ID


`config.clusterID` (default `dev-cluster`) names your cluster in every record and object path, and is part of the Agent's target identity. Set it once, before go-live — changing it later is a target change and requires draining (see [Changing sink or cluster ID](https://open-sandbox.ai/guides/node-agent#changing-sink-or-cluster-id)).


## Choose a sink


Exactly one sink target per Agent. Records land under `<keyPrefix>/<cluster>/<namespace>/<sandbox_id>/<pod_uid>/` as numbered generations plus a `sandbox.finalized.<revision>.json` completeness marker per stream.


The examples below use the umbrella-chart key prefix (`opensandbox-node-agent.`); if you installed the standalone chart, drop that prefix.


### Local files (default)

yaml

```
# values-node-agent.yaml
opensandbox-node-agent:
  enabled: true
  config:
    clusterID: prod-cluster
  sink:
    type: file
    file:
      path: /var/lib/opensandbox/nodeagent-data
      maxBytes: 1073741824      # rotate a generation at 1 GiB
      maxFiles: 16              # per stream
      maxTotalBytes: 10737418240
      retention: 24h            # cleanup after the marker's repair window
```


Keep `sink.file.path` and `hostPaths.fileData` in sync — the chart uses them for the mount and the write target. Retention-driven cleanup runs inside the Agent and only ever removes whole, already-finalized families.


The file sink is for single-node debugging and small clusters. For anything durable across node loss, use OSS.


### Alibaba Cloud OSS


Create the credentials first. Collection credentials must be able to append, read, and write — **never delete**. Deletion happens through a separate offline tool (below), with its own credentials.

bash

```
kubectl create secret generic nodeagent-oss-credentials \
  --namespace opensandbox-system \
  --from-literal=access-key-id=... \
  --from-literal=access-key-secret=...        # optional: --from-literal=session-token=...
```

yaml

```
opensandbox-node-agent:
  enabled: true
  config:
    clusterID: prod-cluster
  sink:
    type: oss
    oss:
      endpoint: https://oss-cn-zhangjiakou.aliyuncs.com   # HTTPS origin required
      bucket: my-sandbox-logs
      keyPrefix: logs
      existingSecret: nodeagent-oss-credentials
```


The bucket must satisfy the Agent's integrity assumptions — startup fails permanently otherwise:


- versioning disabled, no WORM retention policy
- no lifecycle rule whose prefix overlaps `<keyPrefix>/<clusterID>/` (lifecycle deletion would corrupt the marker guarantees)


Objects are written with appendable writes and sealed into immutable generations; markers are written with overwrite forbidden, so consumers can verify them by size and checksum. Because collection credentials cannot delete, cleanup is an explicit, marker-aware offline operation — run [`nodeagent-oss-cleanup`](https://github.com/opensandbox-group/OpenSandbox/tree/main/components/nodeagent/cmd/oss-cleanup) from an operator machine with delete-capable credentials. It plans before it deletes and requires an explicit target-drain confirmation.


## Opt into syscall collection


The default source set is `container-logs` only. Adding `syscalls` enables an embedded eBPF program that records one event per syscall made by each sandbox:

yaml

```
opensandbox-node-agent:
  config:
    sources:
      - container-logs
      - syscalls
```


The chart handles the Kubernetes plumbing automatically when `syscalls` is present: it mounts the host cgroup v2 hierarchy and tracefs read-only and adds the `BPF` and `PERFMON` capabilities. The nodes themselves must provide:


- Linux kernel 5.11 or newer
- cgroup v2 unified hierarchy
- tracefs mounted at `/sys/kernel/tracing`


Syscall records land in their own `<cluster>/_streams/syscall/…` tree and carry their own markers. Expect the syscall marker to be `incomplete` by design in some cases — for example, the tracer attaches only after Kubernetes reports the container ID, so the interval before attachment is reported as a gap rather than claimed as covered.


## Key values


| Value | Default | What it controls |
| --- | --- | --- |
| `config.sources` | `["container-logs"]` | Enabled sources; the image must contain every named source |
| `config.clusterID` | `dev-cluster` | Cluster name in records, paths, and target identity |
| `config.memoryBudgetBytes` | 256 MiB | Global queue budget for buffered records |
| `config.perSandboxQueueBytes` | 16 MiB | Per-sandbox queue budget before backpressure |
| `config.perSandboxRateLimit` | `0` (off) | Per-sandbox records rate limit |
| `config.dropPolicy` | `block` | `block` applies backpressure; `drop` discards and accounts for it in markers |
| `config.sinkTimeout` / `config.retryMaxInterval` | 30s / 30s | Sink write timeout and retry backoff cap |
| `config.stateDir` + `hostPaths.state` | `/var/lib/opensandbox/nodeagent` | Checkpoint state location (keep the two in sync) |
| `config.maxLineBytes` | 1 MiB | Longest log line; longer lines are dropped and accounted |
| `config.endedStateRetention` | 24h | How long a finished stream can still accept late data before its state is pruned |
| `resources` | 50m/128Mi – 1/512Mi | DaemonSet resources (experimental defaults — benchmark before production sizing) |


The defaults follow the safe posture: `block` backpressure means a slow sink slows collection instead of losing data. Only switch to `drop` if you understand that dropped records are gone — they are reported in the stream marker, but not recoverable.


## Metrics


The Agent exports OTLP metrics (`opensandbox.nodeagent.*`: records, bytes, drops, retries, queue depth, sink latency) with no sandbox or Pod identifiers as labels. It requires an explicit endpoint — the node-IP fallback used by other components is disabled:

yaml

```
opensandbox-node-agent:
  extraEnv:
    - name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
      value: http://otel-collector.observability:4318/v1/metrics
```


See [telemetry](https://open-sandbox.ai/guides/telemetry#node-agent) for the metric list and [shared exporter behavior](https://open-sandbox.ai/guides/telemetry#shared-otlp-configuration-for-go-components).


## Operating rules


These protect the delivery guarantee — violating them turns streams `incomplete` or leaves the Agent not-ready (which is the intended, visible outcome):


- **Never remove or rotate the state directory.** It holds checkpoints and finalize intents, not payloads. Deleting it mid-stream forfeits recovery.
- **Do not rotate or delete the file sink's output out-of-band.** The Agent owns its layout and cleanup.
- **Readiness is diagnostic.** `kubectl get daemonset` + `curl /readyz` gives named reasons (`invalid-config`, `state-unavailable`, `operation-retrying`, `store-stale`, …). An unready Agent never silently drops data.
- **Expect a restart to be honest, not lossless.** After an Agent restart, affected markers report `incomplete` — the guarantee is at-least-once within the provable coverage window, and markers never claim more.


### Changing sink or cluster ID


The target identity is a digest of the sink configuration plus cluster ID. If you change `sink.*` or `config.clusterID`, the Agent refuses to reuse old state — by design, so it cannot append one cluster's records onto another target. To change targets safely:


1. Stop collection (scale the DaemonSet to zero) and let streams finalize.
2. Drain the old target (for OSS, complete the offline cleanup/drain confirmation).
3. Update values and redeploy.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/node-agent.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/live-vault-acceptance`

Return to top

# OSEP-0023 Live Credential-Bound Vault: Acceptance
## Policy revision integration acceptance ​
## Historical live-Vault evidence (PR #2176) ​




Internal task document


This page separates the current Policy revision acceptance from the historical live-Vault evidence that preceded PR #2176. Earlier `fresh` or `pass` results do not validate the Policy integration or establish a passing current CI run. The runtime remains default-off and unsupported as a public deployment mode.


## Policy revision integration acceptance


- Branch: `feat/osep0023-policy-revision`.
- Implementation starting commit: `1adfcecec408c2732071befb16f2412463bc3315`.
- Design baseline: `12b77ddefdeb7b35cd933bad18cf253e2c02fcbf` (PR #2176 merge).
- Scope: existing Policy API handlers and automatic always-rule reloads join the shared Policy/Vault mutation barrier. Subsequent Vault updates and bootstrap retain the committed internal Policy epoch. No public methods, schema fields, supported mode, HTTP/2 or Fast Sandbox support are added.


Success requires optional user-policy file persistence, nft application, exact receiver confirmation, then Go proxy/base publication. Reload omits user-policy persistence. This is not atomic pre-ACK visibility: nft can affect traffic first. Receiver failure after successful nft requires sticky recovery and quarantine, even on definitive rejection. API success waits for publication and old-request deadline registration, not the default 30-second drain. Expiry closes the whole connection, potentially affecting newer requests; repeated revisions do not extend the earliest old-request deadline.


The following rows separate executed checks from blocked acceptance layers. Selected unit-test passes are not full-suite or end-to-end acceptance. Command summaries below apply to the current implementation worktree; the final commit identity belongs in the corresponding validation handoff.


| ID | Required evidence | Current result |
| --- | --- | --- |
| P1 | Go owner: Policy methods/reset, no-ops, binding preflight, exact candidate/identity, file/nft failures, cancellation, serialized reload and lifecycle cleanup | Fresh pass: selected owner units and focused race checks, including authoritative Policy shadowing and all three shutdown paths. Broader permitted selection: 18 packages, 594 top-level passes; exclusions and skips detailed below |
| P2 | Real Go → Unix → Python: Policy and reload confirmation, lost-ACK reconciliation, Policy → Vault epoch continuity, bootstrap fencing | Blocked: AF_UNIX socket creation returns EPERM in this environment |
| P3 | Real mitmdump: policy-only keepalive, still-covered idle reuse, long request/upgrade retirement, earliest deadline and whole-connection closure | Registry units: 69/69 pass. Real runtime blocked: AF_UNIX EPERM causes 14 setup failures; one negative startup check passes, not an aggregate runtime pass |
| P4 | Privileged Linux file/nft/quarantine: unchanged start failure, committed effect followed by receiver rejection/unknown, actual packet fence | Blocked: nft and required capabilities are unavailable; unshare returns EPERM |
| P5 | Current-checkout image: Policy methods, bound-deny rejection, real periodic always reload, default 30-second drain, Policy then Vault rotation; record image identity and owned-resource cleanup | Runner units: 33/33 pass. Image run fails prerequisite checks (exit 1, zero skips): Docker/nft absent and unshare returns EPERM |
| P6 | Existing Go SDK PatchPolicy/DeletePolicy 200 structure and 503 propagation; narrow spec generation; docs-site build | Fresh pass: Go SDK full suite and focused Policy cases; docs-site build. Python/TypeScript generation is limited to the documented responses; both Python handlers pass 200/503 response checks and the generated TypeScript contracts pass strict type checking |


Current checks (2026-10-11 UTC) ran on the starting commit plus the Policy integration worktree:


- Egress Go tests used package-scoped `go test -json` selections with 64 named Unix-socket or privileged tests explicitly excluded. The permitted selection passes in 18 packages, with 594 top-level test passes, four privileged tests skipped and two ACL subtests skipped. This is **not a full egress suite pass**.
- Selected owner units and `go test -race` checks pass, including the authoritative Policy shadowing regression and Policy API, always-rule reload and Vault shutdown paths. The broader focused race selection passes 75 top-level tests with zero skips or failures; it does not cover blocked IPC or privileged paths.
- `go vet ./...` and `go build .` pass with `GOFLAGS=-buildvcs=false`, because the environment cannot execute the VCS-stamping subprocess. Go dependency checks use the provisioned module cache with `GOPROXY=off` and `GOSUMDB=off`.
- Python discovery finds 363 tests; 53 runtime/Unix-socket cases are explicitly excluded from the pure-Python selection. All 310 selected tests pass with zero skips, including the 69 registry tests. This is **not full discovery acceptance** and does not replace real mitmdump evidence.
- `python -m unittest discover -v -s scripts -p 'test_*.py'` under `components/egress` passes 85 tests, including the 33 image-runner unit tests.
- `cd sdks/sandbox/go && go test ./...`: pass; main SDK package and the `poolredis` package (which has no tests).
- `go test -v -run 'Test(PatchPolicy|DeletePolicy|PolicyMutationServiceUnavailable)$'`: pass, including separate PATCH and DELETE 503 cases.
- Egress-only regeneration with `openapi-python-client 0.28.0` and `openapi-typescript 7.13.0`: baseline outputs match the checked-in files; updated outputs change only two Python Policy handlers and the TypeScript Policy response types/descriptions. Public schemas and methods are unchanged.
- Generated Python `sync_detailed` handlers: mocked HTTP 200 and plain-text 503 responses pass for PATCH and DELETE, including strict unexpected-status mode.
- TypeScript 5.9.3: strict no-emit check of the generated Policy 200/503 contracts passes. This is not a full Python or JavaScript SDK suite result.
- `cd docs && pnpm docs:build`: pass under Node 22.23.3 and pnpm 9.15.0; VitePress reports a bundle-size warning, with zero build errors.


The image runner includes `TestPolicyRevisionAPIMutations`, `TestPolicyRevisionRejectsBoundDeny`, `TestAlwaysReloadRevision`, `TestPolicyOnlyDrain` and `TestPolicyThenVaultMutation`. The Policy drain case uses the production 30-second default without an override; always-rule cases wait for the actual one-minute reload job. Their presence and runner-unit coverage do not establish image acceptance when prerequisites fail. No image was built and no real-image case ran in this environment. Real IPC, mitmdump, nft/packet and image acceptance remain blocked; no full acceptance or current GitHub CI pass is claimed.


Neither unit tests nor loopback runtime tests replace image/packet evidence. Missing Docker, nft, namespace permissions or dependencies must be reported as blocked rather than a passing skip. Image evidence must identify the actual commit/tree, dirty-diff fingerprint, image ID, executed cases, return codes and cleanup results. Do not expose credentials or add a public epoch debug API.


## Historical live-Vault evidence (PR #2176)


The remaining record is retained from the earlier live-Vault work. Its branch, baselines, session-relative evidence states and deferred checks belong to that work and are not the status of the Policy revision integration above.


- Branch: `feat/osep0023-live-vault`
- Validation baseline: `f46ff91ef572589daeeb67b453ea4e8714a68a26` was the clean starting commit. Local checks ran against that baseline plus the repair worktree, not against the unchanged baseline alone.
- Retained implementation base: `447a7be3bd3c0ee0ac2e9da5412c281aa44b1ca9`. This publication does not rebase onto upstream main; PR creation and base selection remain with the user.
- Owner: current Devin session (implementation + focused tests). Independent review is unavailable in this context — **blocked**; lead review of the full diff is complete and does not count as independent.
- Write set: `components/egress/**`, `docs/guides/credential-vault.md`, `docs/guides/live-vault-acceptance.md`, `components/egress/docs/live-vault-acceptance.md`, `oseps/0023-credential-bound-tls-interception.md`.
- Historical evidence notes: earlier runs reported "18 Go packages ok", "309 Python tests, 0 skips", "6/6 image cases PASS" — these are self-reported and unverified; no current pass is claimed until fresh logs land in the evidence directory for this session.


### Task spec


Harden the experimental live credential-bound loop before it can be trusted:


1. Unknown mutation outcomes must latch sticky recovery instead of restarting from possibly-stale prior state (AC1).
2. `ssl_insecure` must be refused wherever the live admission bundle is active (AC2).
3. ECH-bearing ClientHellos must be detected from the actual extension list and passed through opaquely; uninspectable data denies (AC3).
4. Decrypted HTTP/1 requests must prove their authority equals the admitted SNI before any credential can be injected (AC4).
5. The real Vault lifecycle (rotation, keepalive, stale revision, remove/re-add) holds under the real runtime (AC5).
6. Drain must page all expired transports, retry failed closes, and clean up all runner-created resources with recorded results (AC6).
7. Legacy installation-only behavior is unchanged (AC7).


### Plan


- Go: latch `requireRevisionRecoveryLocked(ExternalEffectsUnknown)` before every terminal detach in `mutateRevisionVault`; reject `LiveAdmission && ssl_insecure` in `validateRevisionIPCConfig`.
- Python addon: ECH detection from `ClientHello.extensions`, strict H1 authority validation, ssl_insecure fences in load/configure/per-request, cursor-based drain paging.
- Harness: live-vault image runner records per-resource cleanup results and a sanitized evidence schema; real-mitmproxy and raw-wire tests provide the boundary evidence.
- Verification: focused offline Go tests, focused Python unit tests, real loopback mitmdump tests; Docker image tests only after explicit authorization.


### Acceptance criteria and evidence matrix


Evidence state is tracked per AC: `fresh` = produced by this session's runs, `reused` = pre-existing unchanged coverage, `missing` = not yet run, `blocked` = needs a permission or resource this context lacks. Pass/fail is recorded only for checks that actually executed in this session.


| AC | Requirement | Evidence layers | Evidence state | Result |
| --- | --- | --- | --- | --- |
| AC1 | Uncertain lifecycle: every terminal detach latches recovery; fresh bootstrap, stale tickets and watcher restarts rejected; old credentials never reauthorized; known rejection/cancelled/shutdown paths nonsticky | Go unit + Python-IPC integration tests (`TestRevision*`) | fresh | pass — `go test ./...` exit 0, 18 packages (log `rework-20261010/go-test-all.txt`); Go test-case skip count not recorded (not verbose) |
| AC2 | Cert/security config: live bundle + `ssl_insecure` rejected in Go launch validation and by real mitmdump startup; safe setting and legacy accepted; lazy handshake verifies upstream | Go env tests, real mitmdump startup tests | fresh | pass — 3/3 `LiveSslInsecureStartupTest` under real mitmdump |
| AC3 | ECH opaque: extension 0xfe0d (incl. GREASE) detected from the real extension list; opaque ignore_connection, no token, zero credential visibility; malformed data denies | subprocess-isolated raw-wire tests parsed by real `mitmproxy.tls.ClientHello` + real-mitmdump boundary test | fresh | pass — 2/2 `test_ech_wire` incl. real-mitmdump origin-vs-mitm cert contrast |
| AC4 | H1 authority: exactly one strict Host equal to SNI and admission token; absolute target agreement; CONNECT/dup/missing/malformed/H2 denied before injection | unit + subprocess-isolated real `read_request_head` tests | fresh (unit/parser); deferred (Docker raw H1 inputs, image layer) | pass — 17 real-parser worker cases; image layer deferred |
| AC5 | Real Vault lifecycle: rotation on keepalive, stale expectedRevision conflict, removal fence, remove/re-add | real mitmdump runtime tests; Docker image run | fresh (loopback); deferred (image run, user decision) | pass (loopback) — 344 Python tests incl. 6 runtime cases, 0 skips; Vault HTTP API stale/remove-readd in real Docker remains deferred |
| AC6 | Idle/multipage drain: after_serial paging, failed close retried, no starvation, no deadline extension, full cleanup accounting | unit tests + real mitmdump idle-close loopback test + runner unit tests; image idle-drain case | fresh (unit+loopback); deferred (image layer) | pass — idle transport closes only at deadline; runner mocked-cleanup units pass |
| AC7 | Legacy unchanged: installation-only receiver, pull-based vault path and non-live envs keep existing behavior | existing tests kept green | fresh | pass — included in the 344-test discovery |


The Docker image layer (real transparent port-443 interception, container lifecycle) is **deferred by user decision**: image acceptance is deferred to GitHub CI or a later session. It has not run, no CI has passed, and this deferral is not an acceptance downgrade — the code is prepared so the image suite can run unchanged once authorized. The docs-site build also remains deferred (offline dependency store incomplete).


### Evidence layers


Unit tests do not substitute for the real-runtime run, and no environment skip is reported as a pass. Fresh per-command logs for this session are written under the session evidence directory (`/tmp/live-vault-evidence-final/`), one child directory per run, and are linked from the handoff report rather than copied into this page.


- Go unit and cross-language IPC integration: `cd components/egress && umask 022 && GOPROXY=off GOSUMDB=off go test . -run 'TestRevision(VaultMutation|WriteHandler|Recovery)'` and `go test ./pkg/mitmproxy ./pkg/revisionruntime`.
- Python addon unit tests: `python -m unittest discover -v -s tests -p "test_*.py"` under the provisioned mitmproxy 11.0.2 venv.
- Real-mitmdump runtime tests (loopback only, disposable): `test_credential_bound_runtime.py`, `test_mitmproxy_runtime.py`, ECH/H1 wire tests.
- Real Docker image end-to-end: `components/egress/scripts/test_live_vault_image.py --image <egress image> --artifacts <evidence dir>` — **deferred by user decision** (to GitHub CI or a later session); not run in this session.


### Scope exclusions


- HTTP/2 GOAWAY/stream drain, the fast-sandbox subject profile and recovery across a complete sidecar replacement remain out of scope. Dynamic Policy and always-rule reload participation were excluded from this historical slice; they have a separate acceptance matrix above.
- Dynamic DNS learning and Kubernetes deployments are not verified by this experiment's current evidence; the Docker-network runner pins origin addresses and uses static allow rules (the local Docker embedded DNS is a runner convenience, unrelated to runtime DNS or Kubernetes evidence).
- The Dockerfile build knobs `GOPROXY` and `APT_MIRROR` remain optional and empty by default; they are local-mirror conveniences for restricted build networks only. Override setup errors fail the build; `APT_MIRROR` also requires at least one supported APT source file.


### Evidence hygiene


Test output and this document contain no credential values: fixtures mask injected headers, the origin records only header names, the runner sanitizes known fixture secrets in recorded commands, and runtime failures are reported through fixed error classes.


### Commit Identity Rewrite


The user authorized rewriting only the four live-Vault slice commits. Their author and committer are now `hpliStartAgain` with the verified-account noreply address `118508408+hpliStartAgain@users.noreply.github.com`. Each commit retains its original tree, timestamps, and Claude co-author trailer. The evidence commit's message now references the rewritten implementation commit.


| Original SHA | Rewritten SHA |
| --- | --- |
| `a90a41330029fb646be5c63de86b3d4d8f4ac40a` | `362e7136f14621e5015ab7447b9fb7eff19feeae` |
| `a6354dea8f8df4c523fa68b146e1b8d2e4df9341` | `6c6619d38b00b6672680ac4ec69a430c7959e1a9` |
| `205d6c8601997415a34b3159b6a7e027dffe8559` | `87a3133b94202480d737057bc3043684ab24c57a` |
| `f46ff91ef572589daeeb67b453ea4e8714a68a26` | `437ff10c43cf830bd3cf91e762f33b78cd1a45ad` |


The old baseline references identify the original validation history. The security repair is a separate child commit, not part of this metadata-only rewrite. A local backup ref retains the old published tip.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/live-vault-acceptance.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/telemetry`

Return to top

# Telemetry


OpenSandbox components export OpenTelemetry (OTLP/HTTP) metrics. This page is the unified reference: each component's metrics with their meaning and attributes, plus the configuration that controls export. SDK-side creation metrics and pool warmup tracing are covered separately in [SDK observability](https://open-sandbox.ai/sdks/observability).


| Component | Meter / service name | Metric families |
| --- | --- | --- |
| [Lifecycle server](https://open-sandbox.ai/guides/telemetry#lifecycle-server) | `opensandbox-server` | HTTP request latency, SDK-reported create latency |
| [Kubernetes controller](https://open-sandbox.ai/guides/telemetry#kubernetes-controller) | `opensandbox/controller` | Allocator histograms, capacity gauges (+ controller-runtime endpoint) |
| [Execd](https://open-sandbox.ai/guides/telemetry#execd) | `opensandbox/execd` | HTTP, execution, filesystem, system resources, OOM, isolation |
| [Egress sidecar](https://open-sandbox.ai/guides/telemetry#egress-sidecar) | `opensandbox/egress` | DNS, policy, nftables, node/process resources |
| [Ingress gateway](https://open-sandbox.ai/guides/telemetry#ingress-gateway) | `opensandbox-ingress-<version>` | HTTP/routing, upstream dial, network readiness shadow, wake-on-access, host |
| [Node agent](https://open-sandbox.ai/guides/telemetry#node-agent) | `opensandbox.nodeagent.*` | Log pipeline records, bytes, drops, retries, queue depth, sink latency |


## Shared OTLP configuration for Go components


Execd, egress, ingress, and node-agent share the OTLP metrics exporter in `components/internal/telemetry`. Set these variables in the **component process environment**. Setting them on the lifecycle server or in a sandbox creation request does not automatically configure another container, such as the egress sidecar. For server-managed egress endpoints, see [egress observability](https://open-sandbox.ai/architecture/network/egress#observability-opentelemetry).


### Export endpoints


- `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` takes precedence over `OTEL_EXPORTER_OTLP_ENDPOINT`.
- Export uses HTTP/protobuf against a collector's HTTP receiver (usually port 4318). gRPC export and switching transport with `OTEL_EXPORTER_OTLP_PROTOCOL` are not implemented.
- Node-IP fallback: when neither endpoint is set, execd, egress, and ingress fall back to `HOST_IP:4318`, or the node IP read from `/etc/hostinfo`, over plain HTTP. If no node IP resolves, metrics are not exported. Components that set `DisableEndpointFallback` in their shared telemetry configuration (node-agent) skip this fallback. Consequently, clearing the endpoint variables alone does not always disable metrics.


### Disabling metrics
## Shared OTLP configuration for Go components ​
## Lifecycle server ​
## Kubernetes controller ​
## Execd ​
## Egress sidecar ​
*Meter: opensandbox/egress · Service name: opensandbox-egress-<version>.*

*egress.dns.query.duration declares its bucket boundaries explicitly:*

## Ingress gateway ​
*Meter: opensandbox/ingress · Service name: opensandbox-ingress-<version>.*

## Node agent ​
*See node agent configuration for the full agent setup.*

## SDK metrics ​










Set either of these standard switches to prevent metrics export, including explicit endpoints and the node-IP fallback:

sh

```
OTEL_SDK_DISABLED=true
# Or disable metrics only:
OTEL_METRICS_EXPORTER=none
```


Values are case-insensitive. Other values leave the existing export configuration unchanged; `OTEL_METRICS_EXPORTER` does not select an alternative exporter here. These switches do not disable native application logs or execd's local `/metrics` and `/metrics/watch` APIs. They also suppress the egress sidecar's automatic collector allow rule, including when the effective policy is rebuilt. Operator-provided allow rules remain in effect.


### Aggregation temporality


Set `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` to select the exporter's standard aggregation behavior:


| Value | Counter and Histogram | ObservableCounter | UpDownCounter and ObservableUpDownCounter |
| --- | --- | --- | --- |
| `cumulative` | Cumulative | Cumulative | Cumulative |
| `delta` | Delta | Delta | Cumulative |
| `lowmemory` | Delta | Cumulative | Cumulative |
| Unset, empty, or whitespace-only | Delta | Cumulative | Cumulative |


Values are case-insensitive. An invalid nonempty value uses the upstream exporter's cumulative default and produces its configuration warning. Gauges remain instantaneous measurements.


Prometheus-style backends expect cumulative counters and histograms. Either set `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=cumulative` in the component environment, or configure the Collector's `deltatocumulative` processor when ingesting delta metrics. Choose the setting before component startup; these environment variables are not hot-reloaded.


## Lifecycle server


Optional OTLP export for server HTTP requests and SDK-reported sandbox creation latency (`POST /v1/metrics/events`). Off by default; the HTTP middleware and the ingestion endpoint remain active but record as noops.


Configuration keys under `[otel]` (see the [server configuration reference](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md) for the authoritative list):


| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `false` | Enable OTLP metrics export. |
| `endpoint` | string | omitted | `null` | OTLP HTTP metrics endpoint. When omitted, uses `OTEL_EXPORTER_OTLP_ENDPOINT` / `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`. |
| `service_name` | string | `"opensandbox-server"` | `service.name` resource attribute. |
| `export_interval_millis` | integer | `60000` | Periodic export interval (≥ 1000). |


Exported metrics:


| Metric | Type | Unit | Attributes | Description |
| --- | --- | --- | --- | --- |
| `server.http.request.duration` | Histogram | `ms` | `http_method`, `http_route`, `http_status_code` | Server HTTP request latency. Histogram count provides request volume. |
| `opensandbox.sandbox.create.duration` | Histogram | `ms` | `sdk.language`, `sdk.version`, `success` | SDK-reported creation latency from create start until ready or failure. |


The HTTP metric uses the matched route template rather than the raw request path. Requests that do not reach a matched route, including early authentication failures and unmatched URLs, use `http_route=unknown`. Standard HTTP methods are recorded in uppercase, while extension methods use `http_method=OTHER` to keep attribute cardinality bounded. The metric never includes sandbox IDs, tenant IDs, API keys, request or response bodies, query strings, or other unbounded request data.


Client-side controls for the creation metric (`OPENSANDBOX_DISABLE_METRICS=1`) and pool warmup traces live in [SDK observability](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Kubernetes controller


The sandbox controller emits OTLP metrics for the pool allocation path and controller capacity. Design principles: only core signals (no speculative instrumentation), reuse what controller-runtime already exposes, and use standard OTel SDK instruments so measurements aggregate across controller replicas.


All custom controller metrics export through one process-wide global OTel meter provider, configured through the standard OpenTelemetry environment variables (see [Enabling OTLP export](https://open-sandbox.ai/guides/telemetry#enabling-otlp-export-for-the-controller)). There are no controller-specific flags.


### Allocator-path metrics


All instruments are `Float64Histogram` on meter scope `opensandbox/controller`, recorded with unit `s` (seconds), with explicit bucket boundaries `[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]` (seconds). Success/error separation is expressed through the `success` boolean attribute; histogram `count` per attribute set provides the success/error counts.


| Name | Attributes | Covers | Emitted from |
| --- | --- | --- | --- |
| `controller.allocator.schedule.duration` | `namespace`, `pool_name`, `success` | The schedule decision itself (`Allocator.Schedule`, including recovery, request building, and the packing algorithm) | `pool_controller.go` `scheduleSandbox` |
| `controller.allocator.persist_alloc_state.duration` | `namespace`, `pool_name`, `success` | Persisting allocation state: the `alloc-status` annotation Patch against the API server | `allocator.go` `annoAllocationSyncer.SetAllocation` |
| `controller.allocator.sync_alloc_result.duration` | `namespace`, `pool_name`, `success` | Syncing the batch allocation result to all sandboxes of a pool (the full concurrent sync round) | `pool_controller.go` `doAllocate` |
| `controller.allocator.sync_single_alloc_result.duration` | `namespace`, `pool_name`, `success` | Per-sandbox allocation-result sync (in-memory store update + annotation Patch); recorded for both `allocated` and `released` syncs | `pool_controller.go` `syncSandboxConcurrently` |


Attribute semantics:


- `namespace`: Kubernetes namespace of the Pool (or BatchSandbox for the per-sandbox instruments).
- `pool_name`: Pool name (`pool.name` semantics; `BatchSandbox.spec.poolRef` for the per-sandbox instruments).
- `success`: `true` when the operation completed without error, `false` otherwise.


Cardinality


The attribute set is intentionally bounded by (namespace, pool_name, success); there is deliberately no `sandbox_name` label. Per-sandbox identity remains available through Kubernetes objects and events; traces are the intended vehicle for per-sandbox latency attribution.


### Capacity metrics


Gauge-style signals collected periodically from the informer cache, registered on the same global OTel meter provider and driven by a leader-elected manager Runnable that unregisters on shutdown:


| Name | Type | Unit | Attributes |
| --- | --- | --- | --- |
| `controller.pool.pods` | ObservableGauge | `{pod}` | `namespace`, `pool_name`, `state` (`total` / `allocated` / `available` / `updated`) |
| `controller.pool.cpu.requested` | ObservableGauge | `{cpu}` | `namespace`, `pool_name`, `state` |
| `controller.pool.memory.requested` | ObservableGauge | `By` | `namespace`, `pool_name`, `state` |
| `controller.batchsandbox.count` | ObservableGauge | `{batchsandbox}` | `namespace`, `phase`, `allocation_mode` (`pool` / `direct`) |
| `controller.batchsandbox.pods` | ObservableGauge | `{pod}` | `namespace`, `state` (`desired` / `current` / `allocated` / `ready`), `allocation_mode` |
| `controller.capacity.collect.duration` | ObservableGauge | `s` | — |


### Controller-runtime metrics (reused, not duplicated)


The controller-runtime metrics endpoint (disabled by default; enable with `--metrics-bind-address`) already exposes workqueue depth/latency, per-driver reconcile counts and durations (`controller_runtime_reconcile_*`), and REST client metrics. These are the source for reconcile health and workqueue signals; the controller does not emit competing custom versions. Pod provisioning failure recovery additionally publishes `opensandbox_pod_recovery_*` counters on that endpoint — see [pod provision failure recovery](https://open-sandbox.ai/guides/pod-recovery).


### Enabling OTLP export for the controller


| Environment variable | Default | Description |
| --- | --- | --- |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | (unset) | Per-signal OTLP/HTTP endpoint, used as-is (no path appended). |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | (unset) | Generic OTLP/HTTP endpoint, used as a base URL; `/v1/metrics` is appended when no path is present. Takes effect when the metrics-specific variable is unset. |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` / `OTEL_EXPORTER_OTLP_HEADERS` | (unset) | W3C Baggage-style `key1=value1,key2=value2` headers attached to export requests. |
| `OTEL_METRIC_EXPORT_INTERVAL` | `60000` (ms) | Interval between OTLP metric exports. |
| `OTEL_SERVICE_NAME` | `opensandbox-controller` | `service.name` resource attribute. |
| `OTEL_RESOURCE_ATTRIBUTES` | (unset) | Additional resource attributes (`key1=value1,key2=value2`). |
| `OTEL_SDK_DISABLED` / `OTEL_METRICS_EXPORTER` | (unset) | Set `OTEL_SDK_DISABLED=true`, or set `OTEL_METRICS_EXPORTER` to a comma-separated list that does not include `otlp`, to disable export. |


Example (Kubernetes container env):

yaml

```
env:
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    value: http://otel-collector.observability:4318
  - name: OTEL_METRIC_EXPORT_INTERVAL
    value: "30000"
```


Behavior:


- With no endpoint configured, the meter provider stays a no-op and nothing is exported.
- The capacity gauges register only on the elected leader (leader-elected Runnable); allocator histograms are recorded and exported on every replica.
- Export failures are retried by the OTLP exporter; setup/configuration errors never block controller startup (telemetry degrades with an error log).
- On shutdown the provider flushes pending data with a 5-second budget.


### Prometheus rendering


When exporting through an OTLP → Prometheus converter (e.g. the OpenTelemetry Collector's `prometheusremotewrite` exporter or a Prometheus OTLP receiver), dots become underscores and the unit is appended, for example:


```
controller_allocator_schedule_duration_seconds{namespace="default",pool_name="pool-a",success="true"}
```


## Execd


Meter: `opensandbox/execd` · Service name: `opensandbox-execd-<version>` (fixed by execd; `OTEL_SERVICE_NAME` is not read).


| Metric | Type | Unit | Attributes | Meaning |
| --- | --- | --- | --- | --- |
| `execd.http.request.duration` | Histogram | `ms` | `http_method`, `http_route`, `http_status_code` | HTTP request latency. |
| `execd.execution.duration` | Histogram | `ms` | `operation`, `result` | Code/command execution duration. |
| `execd.filesystem.operations.duration` | Histogram | `ms` | `operation`, `result` | Filesystem operation duration. |
| `execd.system.process.count` | Observable Gauge | - | - | Current process count. |
| `execd.system.cpu.usage` | Observable Gauge | `%` | - | Sandbox CPU usage percent: sandbox cgroup when resource limits are configured, host `/proc` otherwise (e.g. microVM guests). |
| `execd.system.memory.usage_bytes` | Observable Gauge | `By` | - | Sandbox memory used bytes: sandbox cgroup when resource limits are configured, host `/proc` otherwise (e.g. microVM guests). |
| `execd.system.network.io.bytes` | Observable Counter | `By` | `direction` (`in` / `out`) | Cumulative network I/O bytes. |
| `execd.system.network.connections.active` | Observable Gauge | - | `protocol` (`tcp` / `udp`) | Current active network connections. |
| `execd.system.oom.kills` | Counter | `{kill}` | `level` (`local` / `descendant`, cgroup v2 only) | OOM kills detected in the sandbox cgroup (see below). |
| `execd.isolation.run.duration` | Histogram | `ms` | `result` | Isolated session run duration. |
| `execd.isolation.session.count` | Observable Gauge | - | - | Current number of active isolated sessions. |
| `execd.isolation.upper.usage_bytes` | Observable Gauge | `By` | - | Total bytes used by isolated session upper directories. |


### OOM kill observation


Execd polls its own cgroup every 5 seconds and diffs the kernel OOM kill counter: `memory.events` (`oom_kill`) on cgroup v2, `memory.oom_control` on cgroup v1. Coverage spans the whole sandbox cgroup subtree — user and business processes and nested cgroups (e.g. isolated sessions), not only the sandbox main process. cgroup v2 hosts are covered fully; cgroup v1 reports a single increment without `level`. Kernel logs (dmesg) are intentionally not used: the sandbox container has no `CAP_SYSLOG`, and the kernel ring buffer is not sandbox-scoped.


Every detection produces two signals:


- Metric `execd.system.oom.kills` with a `level` attribute: `local` for kills of processes in the sandbox cgroup itself, `descendant` for kills in nested cgroups.
- A structured warn log line on the container stdout (or the file configured with `EXECD_LOG_FILE`) with troubleshooting context:
  - `memory=<used>/<limit> peak=<peak>` — where memory stood against the cgroup limit when the detection fired
  - `events=[oom=N oom_kill=N oom_group_kill=N]` — deltas of the `memory.events` sub-counters (cgroup v2 only)
  - `kill_cgroups=a,b` — first-level child cgroups whose subtree received the kills
  - `exited=[pid=N comm=x ppid=N rss=N age=Ns, ...]` — processes that disappeared from `/proc` between the polls surrounding the event (candidates for victims; bounded by the kill count, capped at 5 entries)


On warm sandboxes rebound by `POST /internal/init`, the counter interval that crosses a binding handoff is dropped rather than attributed to the new sandbox identity.


### Shared attributes


- `sandbox_id` from `OPENSANDBOX_ID` (when set)
- extra key/value attributes from `OPENSANDBOX_EXECD_METRICS_EXTRA_ATTRS` (when set)


Execd additionally serves local CPU/memory snapshots and live streams through its `/metrics` and `/metrics/watch` APIs, independent of OTLP export — see [execd architecture](https://open-sandbox.ai/architecture/data-plane/execd#observability).


### Endpoint configuration


Export is enabled only when at least one OTLP endpoint is set (`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, fallback `OTEL_EXPORTER_OTLP_ENDPOINT`); otherwise execd keeps metrics local. If both are unset, the node-IP fallback described [above](https://open-sandbox.ai/guides/telemetry#export-endpoints) applies.

bash

```
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://otel-collector:4318"
```


## Egress sidecar


Meter: `opensandbox/egress` · Service name: `opensandbox-egress-<version>`.


| Metric | Type | Unit | Meaning |
| --- | --- | --- | --- |
| `egress.dns.query.duration` | Histogram | `s` | Upstream DNS forward latency (recorded for allowed queries). |
| `egress.dns.query.failed_total` | Counter | - | Queries the proxy could not resolve, by `reason`. |
| `egress.dns.reply.failed_total` | Counter | - | Reply writes that failed after a decision, by `stage`. A nonzero count means a query was handled but its answer never reached the client. |
| `egress.mitm.tls.connections_total` | Counter | - | Experimental live sidecar TLS admission decisions, by closed `mode`, `decision`, and `reason` labels; not successful handshakes or HTTP requests. |
| `egress.policy.denied_total` | Counter | - | Number of DNS queries denied by policy. |
| `egress.nftables.rules.count` | Observable Gauge | `{element}` | Approximate policy size after last successful static apply (fast-sandbox profile: summed across every installed subject's policy, 0 while deny-first). |
| `egress.nftables.updates.count` | Counter | - | Number of successful nftables updates (static apply + dynamic IP add). |
| `egress.nftables.updates.failed_total` | Counter | - | nftables updates that failed, by `operation`. |
| `egress.system.memory.usage_bytes` | Observable Gauge | `By` | **Node** memory used bytes (Linux: gopsutil; non-Linux build: `0`). |
| `egress.system.cpu.utilization` | Observable Gauge | `1` | **Node** CPU busy ratio in `[0,1]` (Linux: gopsutil; non-Linux build: `0`). |
| `egress.process.memory.usage_bytes` | Observable Gauge | `By` | Memory charged to the sidecar's own cgroup. Only present when cgroupfs is readable. |
| `egress.process.cpu.time` | Observable Counter | `s` | CPU seconds consumed by the sidecar's own cgroup. Only present when cgroupfs is readable. |


### Experimental TLS admission decisions


`egress.mitm.tls.connections_total` is emitted only by the experimental credential-bound sidecar runtime. `mode` is always `credential-bound`; no new configuration or public interception mode is enabled. The existing request-weighted shadow metric remains separate.


| `decision` | Allowed `reason` values |
| --- | --- |
| `decrypt` | `binding_host` |
| `passthrough` | `ech`, `no_sni`, `static_ignore`, `no_binding_host` |
| `deny` | `unknown_identity`, `invalid_sni`, `snapshot_missing`, `generation_mismatch`, `invalid_input`, `registry_exhausted`, `admission_disabled`, `ssl_insecure`, `malformed_extensions` |


Each final ClientHello admission decision increments the counter once. A new handshake admission on the same transport is another decision; HTTP/1.1 requests and HTTP/2 streams do not increment it. `decrypt` means the registry admitted decryption, not that tracking, the TLS handshake, or later HTTP/2 handling succeeded. `snapshot_missing` includes bootstrap without an installed snapshot and a closed registry.


Collection uses best-effort `ctx.log.warn` events forwarded to Go. Record failures do not alter admission; events may be lost and add logging cost. No hostname, credential, subject identifier, revision, or raw error is added as a metric label. The closed label set bounds cardinality but does not authenticate the log source: use this as an operational observation, not security evidence or a standalone paging signal. Failed handshakes may produce no HTTP requests, so handshake event volume is not necessarily below request volume.


### `system` vs `process`


They measure different things, and the difference matters because this sidecar runs **per sandbox**:


- `egress.system.*` comes from gopsutil, i.e. `/proc/meminfo` and `/proc/stat`, which inside a container describe the **node**. Every sandbox on a node therefore publishes the same figure under its own `sandbox_id`. Do not chart these "by sandbox": the series look per-sandbox but are N copies of one node number. Prefer kubelet/cAdvisor or a node exporter for node-level data.
- `egress.process.*` is read from the sidecar's own cgroup (v2 `memory.current` and `cpu.stat`, falling back to v1 `memory.usage_in_bytes` and `cpuacct.usage`), so it really is per sandbox.


`egress.process.cpu.time` is a **cumulative counter of consumed seconds**, not a sampled ratio: use `rate()` on it. Both `process` instruments are registered only if their cgroup files can be read — a runtime that does not expose cgroupfs (a sandbox pod under `secure_runtime`, for instance) gets no series at all, rather than a flat zero that reads like an idle sidecar.


### DNS latency histogram boundaries


`egress.dns.query.duration` declares its bucket boundaries explicitly:


```
0.001  0.0025  0.005  0.01  0.025  0.05  0.1  0.25  0.5  1  2.5  5  10  15  30  60  120  300  600
```


The instrument records **seconds**, while the SDK default boundaries are the spec's millisecond ladder (`0, 5, 10, … 10000`), so every realistic latency would fall into the single `le=5` bucket and the quantiles would be meaningless. The coarse tail exists because the recorded duration covers the **whole resolver chain**: forwarding walks the upstreams serially, each with the full timeout (`OPENSANDBOX_EGRESS_DNS_UPSTREAM_TIMEOUT`, 2s by default), so a query can legitimately take `timeout x len(upstreams)`. A late **success** lands in the tail too, not only an exhausted failure. The chain has no finite worst case (`OPENSANDBOX_EGRESS_DNS_UPSTREAM` accepts an unbounded resolver list), so past the last boundary quantile resolution is lost by construction and `_count` is what remains. Both successful and failed lookups feed this histogram, so its tail mixes slow resolutions with exhausted retry chains.


### Failure signals


`egress.dns.query.failed_total` and `egress.policy.denied_total` answer different questions, and confusing them inverts the diagnosis:


- **denied** — the policy did its job. The workload asked for something it is not allowed to reach. Expected traffic in a working system.
- **failed** — the sidecar could not do its job. The workload asked for something allowed and got `SERVFAIL`. Never expected.


`reason` comes from a closed set, so the counter's cardinality is fixed and neither the queried name nor the error text is ever attached:


| `reason` | Meaning |
| --- | --- |
| `no_upstreams` | No resolvers configured or discovered. |
| `upstream_error` | Every resolver failed to answer (network error, timeout). |
| `empty_response` | A resolver returned a nil message. |
| `rcode` | The last resolver answered with a failover-worthy rcode, e.g. `SERVFAIL`. |


`egress.nftables.updates.failed_total` covers another silent failure class. Its `operation` attribute is one of `static_apply`, `dynamic_add`, `remove`, or — in the fast-sandbox profile (OSEP-0022) — `deny_first`, `reset`. `dynamic_add` is the one to alert on: a failed add means the kernel never learned about IPs the policy allows, so the chain drops traffic that should pass — which looks exactly like a policy denial from inside the sandbox while `egress.policy.denied_total` stays flat.


`egress.dns.reply.failed_total` covers the last silent failure class: a query that was **handled** (decided, maybe forwarded and answered upstream) whose reply write then failed. Its `stage` attribute is one of `malformed`, `unknown_source`, `deny`, `upstream_error`, `answer`, and every failure also emits a `[dns] reply write failed (stage=… remote=… question=…)` warning with the remote address and query name. Alert on any nonzero value: like `dynamic_add`, an `answer` -stage failure means traffic the policy allows is not reaching the client.


A `static_apply` failure happens during startup, where the sidecar logs and exits. Metrics leave through a periodic reader and `os.Exit` skips the deferred shutdown, so that path flushes telemetry explicitly before terminating — otherwise the one sample explaining why the sidecar died would never be exported.


### Automatic egress allow rule


When an OTLP destination is configured — the endpoint env vars, or the exporter fallback node IP (`HOST_IP` / `/etc/hostinfo`) when both are unset — egress automatically injects an always-allow egress rule for that host (domain or IP, any port), so telemetry export works under the default deny-all policy without manually managing allowlist rules. This also covers the sidecar's own metric export, which shares the sandbox network namespace and would otherwise be blocked by its own egress chain.


- Precedence: `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` wins over `OTEL_EXPORTER_OTLP_ENDPOINT`; the fallback node IP applies only when neither is set. A set-but-invalid endpoint never falls back (the exporter does not either), so no rule is injected in that case.
- The endpoint must be a URL (`https://host:4318/v1/metrics`) — the `otlpmetrichttp` env-var form. Bare `host:port` or `host` values are not accepted; a trailing root dot on FQDNs is trimmed to match DNS policy normalization.
- The rule lives in the always-allow layer: it survives user `POST`/`PATCH`/`DELETE` policy updates and always-rule file reloads. Operators can still block the target with `deny.always`, which takes precedence.
- Rules are host-scoped (any port), matching the egress rule model; ports are not enforced per rule.


WARNING


Use a fully-qualified service name or an IP in the endpoint. Single-label names (e.g. `otel-collector`) are subject to resolver search-domain expansion, and the deny-all DNS proxy answers the expanded names (e.g. `otel-collector.<ns>.svc.cluster.local`) with NXDOMAIN without falling back to the bare name, so the auto-generated exact-host allow rule would not be reached.


### Shared attributes


- `sandbox_id` from `OPENSANDBOX_EGRESS_SANDBOX_ID` (when set). Without it the sidecars of different sandboxes export identical attribute sets, so their series collide in the backend — which matters most for the per-sandbox `egress.process.*` gauges.
- extra key/value attributes from `OPENSANDBOX_EGRESS_METRICS_EXTRA_ATTRS` (when set)


### Endpoint configuration


Export is enabled only when at least one OTLP endpoint is set; otherwise egress keeps metrics local (no OTLP export), subject to the node-IP fallback described [above](https://open-sandbox.ai/guides/telemetry#export-endpoints).

bash

```
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://otel-collector.sandbox.svc.cluster.local:4318"
# An IP endpoint works as well:
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://10.0.0.5:4318"
```


The server can inject the endpoint into every egress sidecar via `[egress].otlp_endpoint`; see [egress observability](https://open-sandbox.ai/architecture/network/egress#observability-opentelemetry).


### Structured logs (JSON)


Egress structured logs are emitted by zap (typically to stdout). OTLP log export is not implemented in-tree.


- Common fields: `sandbox_id` (when `OPENSANDBOX_EGRESS_SANDBOX_ID` is set), key/value pairs from `OPENSANDBOX_EGRESS_METRICS_EXTRA_ATTRS` merged into the root logger, and `opensandbox.event` identifying the event family.
- `opensandbox.event=egress.outbound` — emitted on allow-path DNS handling (success or forward error) with `target.host`, `target.ips`, `peer`, and `error`.
- Policy lifecycle: `opensandbox.event=egress.loaded` (initial effective policy loaded), `egress.updated` (policy update applied), `egress.update_failed` (policy update failed), with `egress.default` (`allow`/`deny`), `rules`, and `error` fields.


## Ingress gateway


Meter: `opensandbox/ingress` · Service name: `opensandbox-ingress-<version>`.


### HTTP requests & routing


| Metric | Type | Unit | Attributes | Description |
| --- | --- | --- | --- | --- |
| `ingress.http.request.count` | Counter | — | `http_method`, `http_status_code`, `proxy_type` | Request count (QPS derivable) |
| `ingress.http.request.duration` | Histogram | `ms` | `http_method`, `http_status_code`, `proxy_type` | Full request duration |
| `ingress.routing.resolutions.count` | Counter | — | `routing_result` | Routing resolution count |
| `ingress.routing.resolution.duration` | Histogram | `ms` | `routing_result` | Routing resolution latency |


### Upstream connectivity


| Metric | Type | Unit | Attributes | Description |
| --- | --- | --- | --- | --- |
| `ingress.upstream.connect.count` | Counter | — | `connect_result`, `proxy_type` | Upstream TCP dial attempts by result |
| `ingress.upstream.connect.duration` | Histogram | `ms` | `connect_result`, `proxy_type` | Upstream TCP dial duration |


### Network readiness (shadow assessment)


Reported for the most recent complete window; tuned by the `--network-readiness-shadow-*` flags. Shadow gauges never gate traffic.


| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `ingress.network.shadow.attempts` | Observable Gauge | — | TCP connection attempts in the window |
| `ingress.network.shadow.signal_failures` | Observable Gauge | — | Timeout or unreachable results in the window |
| `ingress.network.shadow.distinct_targets` | Observable Gauge | — | Bounded distinct upstream targets in the window |
| `ingress.network.shadow.distinct_signal_targets` | Observable Gauge | — | Distinct targets with timeout/unreachable results |
| `ingress.network.shadow.qualified` | Observable Gauge | — | 1 when the window has enough samples |
| `ingress.network.shadow.degraded` | Observable Gauge | — | 1 when the qualified window is degraded |


### Wake-on-access (OSEP-0024)


Emitted when wake-on-access is enabled. Restore saturation, parking-lot shedding, policy gate failures, and Redis write drops are the signals to watch.


| Metric | Type | Unit | Attributes | Description |
| --- | --- | --- | --- | --- |
| `ingress.wake.flights` | Counter | — | `outcome` (`triggered` / `joined` / `none`) | Wake flight count by outcome |
| `ingress.park.active` | UpDownCounter | — | - | Currently parked requests |
| `ingress.park.wait.duration` | Histogram | `s` | `outcome` (`served` / `budget_exhausted` / `canceled` / `error`) | Per-parked-request wait duration; buckets are sized around the default 5s park budget (a ~200ms same-node resume vs a near-exhaustion wait) |
| `ingress.park.shed` | Counter | — | - | Requests shed because the parking lot was full |
| `ingress.wake.restore.active` | UpDownCounter | — | - | Wake flights currently holding a restore permit (the concurrent-restore gauge) |
| `ingress.idlep.policy.reads` | Counter | — | `outcome` (`allowed` / `denied` / `error`) | Idle-policy gate outcomes; sustained `error` means an RBAC or apiserver problem |
| `ingress.activity.writes_dropped` | Counter | — | - | Activity observations dropped before reaching Redis |


### Host metrics (Linux only; 0 elsewhere)


| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `ingress.system.cpu.usage` | Observable Gauge | `1` | CPU busy ratio `[0,1]` |
| `ingress.system.memory.usage_bytes` | Observable Gauge | `By` | Memory used bytes |
| `ingress.connections.active` | Observable Gauge | — | TCP ESTABLISHED connections (from `/proc/net/tcp`) |


**Attribute values:**


- `proxy_type`: `http` | `websocket`
- `routing_result`: `success` | `not_found` | `not_ready` | `error`
- `connect_result`: `success` | `timeout` | `unreachable` | `refused` | `dns_error` | `canceled` | `other`


### Endpoint configuration

bash

```
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://otel-collector:4318"
```


Fallback: `OTEL_EXPORTER_OTLP_ENDPOINT`. When both are unset, export falls back to the node IP (`HOST_IP` env, then `/etc/hostinfo`) on port 4318 over plain HTTP; if no node IP resolves, metrics are not exported. Disable export with `OTEL_SDK_DISABLED=true` or `OTEL_METRICS_EXPORTER=none`. Default temporality: delta for synchronous Counter/Histogram, cumulative for observable gauges — override with `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`.


## Node agent


The node agent's log pipeline exports OTLP metrics with no sandbox or Pod identifiers as labels:


| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `opensandbox.nodeagent.records` | Counter | - | Records consumed from sources and handed to the sink. |
| `opensandbox.nodeagent.bytes` | Counter | `By` | Record payload bytes consumed. |
| `opensandbox.nodeagent.drops` | Counter | - | Records dropped (only possible under `drop` backpressure). |
| `opensandbox.nodeagent.retries` | Counter | - | Sink delivery retry attempts. |
| `opensandbox.nodeagent.queue.bytes` | UpDownCounter | `By` | Bytes currently queued for delivery (queue depth proxy). |
| `opensandbox.nodeagent.sink.consume.duration` | Histogram | `ms` | Sink consumption (write) latency. |


It requires an explicit endpoint — the node-IP fallback used by other components is disabled (`DisableEndpointFallback`):

yaml

```
opensandbox-node-agent:
  extraEnv:
    - name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
      value: http://otel-collector.observability:4318/v1/metrics
```


See [node agent configuration](https://open-sandbox.ai/guides/node-agent) for the full agent setup.


## SDK metrics


The SDKs report sandbox creation latency to the lifecycle server (`POST /v1/metrics/events`), which the server exports as `opensandbox.sandbox.create.duration` when `[otel]` is enabled, and can emit pool warmup traces through the application's own OpenTelemetry provider. Client-side enablement and disablement are covered in [SDK observability](https://open-sandbox.ai/sdks/observability).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/telemetry.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/api/implementation-compatibility`

# Implementation compatibility
## Contracts and processes ​
*The published OpenAPI files are the starting point for implementation:*

## Workload APIs and endpoint resolution ​
## Current Python SDK endpoint expectations ​
## Backend-dependent features and unsupported operations ​
## Choosing an initial compatibility target ​







OpenSandbox separates sandbox lifecycle management, in-sandbox execution, and workload-specific services. This page describes the current repository's interfaces and client behavior. It does not define a new v1 conformance profile or a capability-negotiation protocol. Pin the spec revision and SDK version you target: an implementation of one API is not automatically compatible with every feature exposed by a sandbox SDK.


## Contracts and processes


The [published OpenAPI files](https://open-sandbox.ai/api/) are the starting point for implementation:


| Contract | Interface and consumers |
| --- | --- |
| [`sandbox-lifecycle.yml`](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/sandbox-lifecycle.yml) | Control plane: creation, inspection, deletion, expiration, endpoint resolution, pause/resume, snapshots, templates, and lifecycle network-policy operations. Used by sandbox SDKs and management clients. |
| [`diagnostic-api.yml`](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/diagnostic-api.yml) | Additional lifecycle-server routes for diagnostic log/event descriptors. Needed when clients use diagnostics; not the command-output API. |
| [`execd-api.yaml`](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/execd-api.yaml) | Data plane: health, commands, files, directories, code contexts, metrics, and isolated-session operations. Used by the execution services in sandbox SDKs and Code Interpreter clients. |
| [`egress-api.yaml`](https://github.com/opensandbox-group/OpenSandbox/blob/main/specs/egress-api.yaml) | Egress policy and Credential Vault management. A separate API from execd; the reference deployment normally serves it through an egress component. |


The wire contract does not require an independent implementation to run the Go `execd` binary. A native execution service can serve the execd operations that its clients use. Compatibility requires their behavior as well as their route names: request/response schemas, authentication headers, file transfer semantics, SSE event payloads and completion, errors, and context/command lifetimes all matter. Implementing only the lifecycle contract does not supply SDK command, file, or code execution. Conversely, an execd-compatible service alone does not implement sandbox creation or endpoint resolution.


The reference server's binary injection, container bootstrap, init/supervision, Jupyter integration, and proxy layout are implementation mechanisms. A backend can use different mechanisms, but must preserve the observable semantics of the operations it claims to support. OpenAPI coverage is not complete for every reference extension: for example, the current [execd router](https://github.com/opensandbox-group/OpenSandbox/blob/main/components/execd/pkg/web/router.go) exposes `/pty` HTTP/WebSocket routes which are not yet in `execd-api.yaml`. Do not infer support for such extensions from OpenAPI compatibility alone.


## Workload APIs and endpoint resolution


`GET /v1/sandboxes/{sandboxId}/endpoints/{port}` resolves access to a service on the requested sandbox port. It does not convert that service into an execd API or impose execd's command/file schemas on it. In the [AIO example](https://github.com/opensandbox-group/OpenSandbox/blob/main/examples/aio-sandbox/main.py), OpenSandbox manages the sandbox and resolves port `8080`, then `AioSandboxClient` speaks the image's own shell/file/browser API.


Endpoint resolution is agnostic to the workload's application API; transport support still depends on the selected network path. For example, the [Docker embedding proxy](https://open-sandbox.ai/architecture/network/single-host-network) forwards HTTP, SSE, and WebSocket traffic. An arbitrary port number does not imply a generic TCP/UDP tunnel. Preserve the returned address (including proxy path) and required headers, and use a client suitable for the service and transport. Passing through execd's proxy does not make the destination process execd.


## Current Python SDK endpoint expectations


The following describes [`SandboxSync`](https://github.com/opensandbox-group/OpenSandbox/blob/main/sdks/sandbox/python/src/opensandbox/sync/sandbox.py) in the current tree, rather than a portable protocol requirement for all clients:


| Flow | Endpoint resolution before the health check |
| --- | --- |
| `create()` from an image or snapshot | Resolves execd port `44772`, then egress port `18080`. If the execd endpoint reports template origin, policy operations use the lifecycle service, but this create path has already resolved the egress endpoint. |
| `create_from_template()` | Resolves `44772`; uses lifecycle network-policy operations without resolving `18080`. |
| `connect()` | Resolves `44772` and reads the endpoint response's `OPEN-SANDBOX-ORIGIN` header. Template origin selects lifecycle network policy; other origins also resolve `18080`. |


A custom `health_check` replaces the default execd `/ping` readiness probe. It does **not** remove these endpoint lookups or the construction of SDK service adapters. `skip_health_check=True` also still waits for endpoint publication. This explains why the AIO example's custom health check does not make it a lifecycle-only SDK client. Resolving an endpoint is distinct from invoking its API: service adapters are constructed before the application chooses operations.


An independent backend targeting these high-level flows must account for these lookups, returned headers, and the operations it will expose. A client using only the lifecycle HTTP API and a workload-specific client can choose a narrower integration. Verify other SDK languages and versions separately; the table is not a promise that all SDKs have identical startup behavior. Template origin is an existing routing signal, not a general capability manifest.


## Backend-dependent features and unsupported operations


The presence of an operation in a spec or SDK does not mean every runtime, image, or deployment enables it:


| Feature | Current boundary |
| --- | --- |
| Pause/resume and snapshots | Depend on the workload provider, runtime, and storage configuration. In particular, the Kubernetes rootfs snapshot committer rejects gVisor RuntimeClasses. Do not infer snapshot support from basic create/execute support. |
| Templates | Template management uses the Kubernetes Fast Sandbox integration; the reference Docker server rejects it with HTTP `501`. |
| Egress policy and Credential Vault | Depend on egress configuration and backend routing. Template-backed Python sandboxes manage policy through the lifecycle service; `credential_vault` access raises an SDK exception for that origin. Policy support does not imply Vault support. |
| Code execution | The reference execd uses Jupyter and installed kernels for code contexts. A shell-only image does not thereby support notebook-style code execution. A native implementation must reproduce the code API semantics if it claims that feature. |
| PTY and isolated sessions | Depend on platform facilities and reference extensions. `/v1/isolated/capabilities` describes the isolator/hardening environment, not all lifecycle and execution features. Isolated diff/commit currently report unsupported and are not implemented. |


There is no single general capability-negotiation endpoint in the current contracts. Document a backend's supported operations and prerequisites, and use feature-specific discovery where available. Unsupported requests should produce an explicit failure with an actionable error, not a fabricated success. Use the operation's specified error shape and distinguish an unsupported feature from missing authorization, missing resources, or a temporarily unready service.


There is also no universal unsupported-operation status to substitute everywhere. Current reference examples include HTTP `501` for unsupported template management, HTTP `409` for the snapshot service's unsupported-runtime preflight, and HTTP `503` for unimplemented isolated diff/commit. See the [template handler](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/opensandbox_server/api/templates.py), [snapshot service](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/opensandbox_server/services/snapshot_service.py), and [isolated API notes](https://open-sandbox.ai/api/). These describe present behavior, not a new uniform error convention.


## Choosing an initial compatibility target


Start with a named client version and an explicit operation set. For a command and file integration, validate lifecycle create/inspect/delete and endpoint resolution, authentication and readiness, command SSE completion and errors, and the file operations the client needs. Add code contexts, snapshots, or policy/Vault operations only when the backend can provide their semantics. Use the repository's [SDK end-to-end tests](https://github.com/opensandbox-group/OpenSandbox/tree/main/tests) for the selected operations and document unimplemented features. This is a practical integration target, not a claim of full protocol conformance.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/api/implementation-compatibility.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/getting-started/configuration`

# Configuration


The OpenSandbox server reads a **TOML** configuration file. Default path: `~/.sandbox.toml`. Override with the `SANDBOX_CONFIG_PATH` environment variable or the `--config` flag.


## Generate a Config File

bash

```
# Docker runtime (default)
opensandbox-server init-config ~/.sandbox.toml --example docker

# Kubernetes runtime
opensandbox-server init-config ~/.sandbox.toml --example k8s

# Schema-only skeleton (no defaults)
opensandbox-server init-config ~/.sandbox.toml

# Overwrite existing config
opensandbox-server init-config ~/.sandbox.toml --example docker --force
```


## Run the Server

bash

```
opensandbox-server
# or specify a config path
opensandbox-server --config /path/to/sandbox.toml
```


The server listens on the `server.host` / `server.port` values from your TOML config.


## Authentication


Authentication is enforced when `server.api_key` is set. All API endpoints (except `/health`, `/version`, `/docs`, `/redoc`, and `/openapi.json`) require the `OPEN-SANDBOX-API-KEY` header:

bash

```
curl -H "OPEN-SANDBOX-API-KEY: your-secret-api-key" http://localhost:8080/v1/sandboxes
```


WARNING


If `server.api_key` is empty, the server runs without authentication. In non-interactive environments (Docker/Kubernetes/CI), set `OPENSANDBOX_INSECURE_SERVER=YES` to acknowledge the risk. **Always set an API key in production.**


## Key Configuration Areas


| Section | Description |
| --- | --- |
| `[server]` | Host, port, API key, and general server settings |
| `[runtime]` | Runtime selection and execd image configuration |
| `[otel]` | OpenTelemetry export for SDK create-latency metrics |
| `[proxy]` | Server-side sandbox proxy target selection; use host mappings when the server cannot route to sandbox IPs |
| `[docker]` | Docker runtime networking, host address, and image-pull settings |
| `[kubernetes]` | Kubernetes runtime: `workload_provider`, `batchsandbox_template_file` |
| `[egress]` | Egress sidecar for `networkPolicy` enforcement |
| `[ingress]` | Ingress gateway configuration |
| `[secure_runtime]` | Secure container runtime (gVisor, Kata, Firecracker) |
| `[store]` | Persistence backend (default: SQLite at `~/.opensandbox/opensandbox.db`) |
| `[renew_intent]` | Auto-renew on access (experimental) |
| `[agent_sandbox]` | Agent sandbox settings for Kubernetes |


For the full configuration reference with all keys and defaults, see the [server configuration.md](https://github.com/opensandbox-group/OpenSandbox/blob/main/server/configuration.md).


## Sandbox Expiration


`server.max_sandbox_timeout_seconds` limits the `timeout` supplied when creating a sandbox. If configured, it must be at least `60` seconds; omit it to disable the creation-time upper bound. It does not limit renewal requests or the total lifetime of a sandbox.


`POST /v1/sandboxes/{sandboxId}/renew-expiration` sets an absolute `expiresAt`. Despite the endpoint name, it can shorten, preserve, or extend the current expiration, provided the requested timestamp is still in the future. A timestamp beyond `now + max_sandbox_timeout_seconds` is also accepted.


Duration-based SDK `renew()` methods calculate the target as `now + duration`, not `current expiresAt + duration`. For example, renewing for five minutes when thirty minutes remain moves expiration earlier. Callers that require extension only must account for the current expiration before choosing a target.


## Kubernetes Creation Wait


For the BatchSandbox and agent-sandbox providers, the server waits for the workload status to become `Running` or `Allocated` before returning a successful create response. This does not check whether your application inside the sandbox is ready.
## Generate a Config File ​
## Run the Server ​
## Authentication ​
## Key Configuration Areas ​
## Sandbox Expiration ​
## Kubernetes Creation Wait ​
## API Documentation ​
## Environment Variables ​
## Related ​











Creation requests share the existing resource watches. A workload change wakes its waiting request immediately, which evaluates the object carried by the event without another API read. The initial check and periodic fallback still use normal cache/API reads. Events overlapping a read or describing deletion trigger a fresh check. Providers without subscription support continue polling.


| `[kubernetes]` setting | Default | Meaning |
| --- | --- | --- |
| `sandbox_create_timeout_seconds` | `60` | Overall creation wait limit |
| `pool_acquisition_timeout_seconds` | `30` | Cumulative wait limit while Pool capacity is exhausted |
| `sandbox_create_poll_interval_seconds` | `1.0` | Fallback status-check interval when no notification arrives |


The default fallback interval remains unchanged. Increasing it (for example to `5.0`) reduces repeated checks while nothing changes, but can delay detection when watch notifications are unavailable. Overall and Pool capacity deadlines still apply independently of this interval. Unavailable cache reads continue to fall back to the Kubernetes API.


## API Documentation


Once the server is running, interactive API docs are available at:


- **Swagger UI**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`


## Environment Variables


| Variable | Description |
| --- | --- |
| `SANDBOX_CONFIG_PATH` | Override the config file path |
| `DOCKER_HOST` | Custom Docker daemon address |
| `OPENSANDBOX_INSECURE_SERVER` | Set to `YES` to run without API key in non-interactive mode |


- [Secure Container Runtime](https://open-sandbox.ai/guides/secure-container) — gVisor, Kata, and Firecracker configuration
- [Credential Vault](https://open-sandbox.ai/guides/credential-vault) — Secure credential injection
- [Network Isolation on Kubernetes](https://open-sandbox.ai/guides/network-isolation) — Egress policy design
- [Kubernetes Deployment](https://open-sandbox.ai/deployment/) — Kubernetes-specific setup[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/getting-started/configuration.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/guides/client-pool`

# Client Pool


The OpenSandbox SDKs ship an experimental **client-side sandbox pool** that keeps a small buffer of ready sandboxes warm on the server so that `acquire()` returns quickly instead of paying the full sandbox creation latency on the hot path.
## What it actually pools ​
## Empty-buffer behavior: AcquirePolicy ​
## Configuration ​
## Minimal usage ​
*SandboxPoolAsync has the same surface plus an async with context manager:*

## Diagnostics and operations ​
*Go — (*SandboxPoolManager).Destroy(ctx, poolName, options):*

## Further reading ​








Available in Python (async and sync), JavaScript/TypeScript, Kotlin/Java, and Go. C# does not currently ship a client pool.


Experimental


The client pool API is marked experimental and may change between minor releases. Pin your SDK version if you rely on it in production.


## What it actually pools


The pool does **not** pool SDK `Sandbox` objects. It pools the **IDs of pre-warmed, ready sandboxes** running on the OpenSandbox server.


Use a pool for latency-sensitive workers that repeatedly need a fresh sandbox. The pool keeps remote sandboxes ready; it is separate from an HTTP connection pool. Borrowed sandboxes still consume server resources and must be explicitly cleaned up.


![Client pool architecture](https://open-sandbox.ai/assets/client-pool-architecture.OibEErxj.svg)


Two flows happen concurrently:


- **Warmup (leader-only).** A background reconcile loop runs on every node. Whichever node holds the primary lock computes the idle deficit and replenishes it. Python, JavaScript, and Kotlin use a nominal one-second cadence and admit at most `warmup_create_qps` new creates per completed tick. Kotlin schedules at a fixed rate; JavaScript skips a tick if the previous reconcile is still running; Python waits one second after the previous tick completes. Go uses a configurable `reconcile_interval` and caps each tick with `warmup_concurrency`. A successful warmup is published independently to the idle buffer with a TTL of `idle_timeout`.
- **Acquire (any node).** `acquire()` pops an idle ID from the store, connects a `Sandbox` client to it, optionally runs a health check and a `renew()` to the caller-supplied timeout, and hands it to the caller. Non-leader nodes can acquire freely; only replenish and shrink are gated by the leader lock.


Idle membership carries sandbox IDs and their expiry, never HTTP connections or client-side `Sandbox` objects. The state store also coordinates the leader lease, shared idle target and TTL, and namespace-destroy fence. A Redis-backed store makes that coordination and idle membership visible across processes and pods.


The warmup path — the leader-only replenish flow above — is worth zooming in on because it is the only part of the pool that is gated by a distributed lock:


![Warmup reconcile sequence](https://open-sandbox.ai/assets/client-pool-warmup-sequence.C_Rvy_ny.svg)


### Lifecycle model


During graceful operation, each pool instance moves through `NOT_STARTED → STARTING → RUNNING → DRAINING → STOPPED`. A failed start or non-graceful shutdown can transition directly to `STOPPED`. If awaiting Python's `SandboxPoolAsync.start()` is cancelled, it waits for startup-owned resource cleanup, even if the caller cancels repeatedly during cleanup. Successful cleanup returns the pool to `STOPPED` before propagating `CancelledError`, so the same instance can then be started again. If cleanup itself fails after a further caller cancellation, `CancelledError` takes precedence and retains the cleanup error as its cause. Without a further cancellation, the cleanup error propagates normally. In either case the lifecycle state is `STOPPED`, allowing another `start()` attempt instead of silently returning in `STARTING`. Resource cleanup may still be incomplete when closing fails. Health is tracked separately as `HEALTHY | DEGRADED | DRAINING | STOPPED`; after `degraded_threshold` consecutive warmup or reconcile failures the pool enters `DEGRADED`. Go applies exponential replenish backoff while degraded. Python, JavaScript, and Kotlin continue attempting reconciliation at their nominal one-second cadence: `warmup_create_qps` is their pressure control, and `snapshot().backoff_active` / `snapshot().backoffActive` is retained only for compatibility and is always `false`. Callers do not need to observe these states directly — `snapshot()` exposes them for diagnostics.


Python, JavaScript, and Kotlin built-in warmup creates make a single lifecycle request. Python and Kotlin disable the connection-level retry policy for HTTP 429, other retryable statuses, and transport recovery; JavaScript's lifecycle transport does not add automatic retries. There is no pool-level `Retry-After` throttle. A custom `PooledSandboxCreator` receives the warmup connection configuration through `PooledSandboxCreateContext.connection_config` or `createConnectionConfig` and must honor it, together with `skipHealthCheck`, to preserve the staged behavior. A failed create is recorded and a later tick may admit replacement work. Normal standalone creation and `AcquirePolicy.DIRECT_CREATE` retain their usual transport behavior.


![Client pool lifecycle state machine](https://open-sandbox.ai/assets/client-pool-lifecycle.CGlaWr34.svg)


### There is no `release()`


Sandboxes are ephemeral. Once you have called `acquire()`, the sandbox is yours until you `destroy()` / `kill()` it. `max_idle` bounds the **warm buffer**, not the number of sandboxes borrowed by application code and not the number of sandboxes produced by `DIRECT_CREATE` fallback.


In Python's `SandboxPoolAsync`, ownership transfers when `acquire()` returns. If the call fails or is cancelled after connecting to or creating a sandbox, the pool attempts to kill that sandbox and closes its local resources before propagating the error. Cancellation during renewal or the final pool-state checks, including repeated cancellation during cleanup, does not skip that cleanup. Once acquisition succeeds, the caller remains responsible for disposal.


## Empty-buffer behavior: `AcquirePolicy`


All four pool SDKs expose these policies. Acquire consumes a candidate; it does not wait for future warmup work to fill an empty buffer.


| Policy | Idle candidates attempted | When candidates are exhausted |
| --- | --- | --- |
| `FAIL_FAST` | At most one | Return a pool-empty/acquire error |
| `DIRECT_CREATE` (default) | At most one | Create a fresh sandbox |
| `RETRY_NEXT_IDLE` | Up to `max_acquire_retries` | Return a pool-empty/acquire error |
| `RETRY_NEXT_IDLE_THEN_CREATE` | Up to `max_acquire_retries` | Create a fresh sandbox |


`max_acquire_retries` / `maxAcquireRetries` / `MaxAcquireRetries` defaults to `3`. It bounds the **total candidate attempts**, not three additional retries after the first. Each candidate can consume the acquire-readiness budget; direct creation adds its own startup latency.


`start()` begins background replenishment and does not wait for a full buffer. Use `DIRECT_CREATE` during startup, or observe the idle count before using `FAIL_FAST`. A pool is not a concurrency limit: direct creation and already borrowed sandboxes can exceed `max_idle`.


## Configuration


The SDKs share the pool concepts, but their scheduling surfaces differ. This table is the canonical reference; refer to the per-language builder or constructor for exact camelCase / snake_case naming.


| Parameter | Python / JavaScript / Kotlin default | Go default | Meaning |
| --- | --- | --- | --- |
| `pool_name` | required | required | Logical namespace shared by all nodes of one distributed pool |
| `owner_id` | auto (`pool-owner-<uuid>`) | auto (`pool-owner-<host/pid>`) | Identity of this process for primary-lock ownership; **must be unique per node** |
| `max_idle` | required (≥ 0) | required (≥ 0) | Target size and cap of the idle buffer |
| `state_store` | required in Python/Kotlin; JavaScript defaults to in-memory | builder defaults to in-memory | `InMemoryPoolStateStore` or Redis-backed store |
| `connection_config` | required | required | Used for lifecycle and execd calls |
| `creation_spec` | required in Python/Kotlin; required in JavaScript only without a creator | required only when `sandbox_creator` is unset | Template for warmed sandboxes; exact fields vary by language |
| `sandbox_creator` | `null` | `null` | Optional callback that overrides default creation. Python and Kotlin still require `creation_spec`; JavaScript and Go allow a creator-only pool. |
| `warmup_create_qps` | `10` | not available | Maximum warmup creates admitted on each completed reconcile tick |
| `warmup_concurrency` | `128` | `max(1, ceil(max_idle * 0.2))` | Python / JavaScript / Kotlin: concurrent post-create work; it does not control create admission. Go: create cap per tick and worker concurrency. |
| `primary_lock_ttl` | `60 s` | `60 s` | Leader lease TTL |
| `reconcile_interval` | nominal `1 s`, not exposed | `30 s`, configurable | Reconcile cadence; long Python/JavaScript ticks reduce the effective rate |
| `degraded_threshold` | `3` | `3` | Consecutive failures before `DEGRADED`; only Go pauses replenish with backoff |
| `acquire_ready_timeout` | `30 s` | `30 s` | Max wait for the returned sandbox to become ready |
| `acquire_health_check_polling_interval` | `200 ms` | `200 ms` | Ready-poll interval during acquire |
| `acquire_health_check` | `null` | `null` | Custom readiness predicate for acquire |
| `acquire_skip_health_check` | `false`; JavaScript also has a per-acquire override | per-acquire option | Skip the readiness check on acquire |
| `acquire_min_remaining_ttl` | `min(60 s, idle_timeout / 2)` | `min(60 s, idle_timeout / 2)` | Discard idles closer to expiry than this on acquire |
| `warmup_ready_timeout` | `30 s` | `30 s` | Max readiness-check window for a warmed sandbox |
| `warmup_health_check_initial_delay` | `0 s` | not available | Delay between successful create and the first readiness check |
| `warmup_health_check_polling_interval` | `500 ms` | `200 ms` | Ready-poll interval during warmup; Python / JavaScript / Kotlin also use it for post-prepare checks |
| `warmup_health_check` | `null` | `null` | Custom warmup readiness predicate |
| `warmup_sandbox_preparer` | `null` | `null` | Runs once after readiness and before publishing to the idle buffer |
| `warmup_post_prepare_health_check` | `null` | not available | Optional validation after the preparer; retries do not rerun the preparer |
| `warmup_post_prepare_health_check_timeout` | `30 s` | not available | Retry window for post-prepare validation |
| `warmup_skip_health_check` | `false` | `false` | Skip the pre-prepare readiness stage during warmup |
| `idle_timeout` | `24 h` | `24 h` | Server-side TTL for pool-created sandboxes |
| `drain_timeout` | `30 s` | `30 s` | Max wait for in-flight ops during graceful shutdown |


### JavaScript settings and creator coverage


JavaScript uses the Python/JVM scheduling defaults above: `warmupCreateQps: 10`, `warmupConcurrency: 128`, a nominal one-second reconcile cadence, 500 ms warmup polling, and 30-second readiness windows. Its store defaults to `InMemoryPoolStateStore`; `creationSpec` can be omitted when `sandboxCreator` is supplied. Time settings include units in their names, such as `idleTimeoutSeconds` and `warmupHealthCheckInitialDelayMillis`.


Default pool creators expose fewer options than standalone sandbox creation:


| Creation field | Python | JavaScript | Kotlin/Java | Go |
| --- | --- | --- | --- | --- |
| Snapshot restore | No | Yes | No | Yes |
| Resource configuration | Yes | Yes | Yes | Yes |
| Lifecycle hooks | No | Yes | No | No |
| Credential Proxy | No | Yes | Yes | Yes |


All four standalone sandbox creation APIs accept these fields. Use a custom `sandbox_creator` / `sandboxCreator` when the default pool spec is insufficient, and honor the supplied connection config, readiness controls, and timeout.


JavaScript and Go also accept minimum remaining TTL and skip-health-check overrides on each acquire. Python and Kotlin expose these as pool-level configuration.


### Staged warmup


Staged warmup separates creation admission from post-create work:


![Staged warmup flow](https://open-sandbox.ai/assets/client-pool-staged-warmup.uBs7e348.svg)


1. On each reconcile tick, the leader admits at most `min(max_idle - idle - warming, warmup_create_qps)` creates. The lifecycle create request is attempted once and returns a client without running its normal inline readiness loop. The create execution limit is internal and resolves to `ceil(warmup_create_qps * 1.5)`, so slow creates cannot grow active create work without bound. A custom creator must honor the supplied warmup connection config and `skipHealthCheck` from its `PooledSandboxCreateContext`.
2. The created sandbox enters a delayed stage queue. The first readiness check runs after `warmup_health_check_initial_delay`; failures retry every `warmup_health_check_polling_interval` until `warmup_ready_timeout`, including one final check at the deadline.
3. `warmup_sandbox_preparer` runs once. If configured, `warmup_post_prepare_health_check` then retries at the same polling interval until `warmup_post_prepare_health_check_timeout`; retries never rerun the preparer.
4. A healthy sandbox is renewed and committed to the idle buffer. `warmup_concurrency` bounds active post-create work. Delays between unsuccessful readiness polls do not permanently occupy the entire capacity.


There is no Python, JavaScript, or Kotlin `reconcile_interval` setting and no replenish backoff. For Python/Kotlin configurations that used the older setting, remove `reconcile_interval=...` / `reconcileInterval(...)`, choose `warmup_create_qps` / `warmupCreateQps(...)` for create admission, and use `warmup_concurrency` / `warmupConcurrency(...)` only for post-create capacity.


`warmup_create_qps` is an admission ceiling, not a completion-rate guarantee. Create latency, readiness, preparation, state-store latency, event-loop or executor capacity, and a delayed/skipped reconcile tick can all reduce observed warmup throughput.


### Choosing a state store


- **`InMemoryPoolStateStore`** — single process only. Suitable for development, tests, and single-instance workers. Not process-wide for gunicorn/uvicorn workers, Celery, or Kubernetes replicas.
- **Redis-backed store** (`RedisPoolStateStore`, `AsyncRedisPoolStateStore`, `sandbox-pool-redis` on the JVM, `poolredis` in Go, `@alibaba-group/opensandbox/pool-redis` in JavaScript) — required for multi-process or multi-pod deployments. All nodes in one logical pool must share the same `pool_name` and Redis `key_prefix`, and each process must use a **unique** `owner_id`.


![Single-node vs distributed pool topology](https://open-sandbox.ai/assets/client-pool-topology.CGj8otaf.svg)


### Rules that apply to every deployment


- `max_idle` bounds the warm buffer only. It does not cap borrowed sandboxes or `DIRECT_CREATE` fallbacks.
- All nodes sharing one pool must use the same creation and warmup definition. If that definition changes, roll out under a **new** `pool_name` (or Redis `key_prefix`) and retire the old one (see "Retiring an old pool namespace" below). Do not attempt to refill a changed template into the same `pool_name`: `release_all_idle()` does not fence other nodes, does not lower `max_idle`, and does not stop any current leader (which may still be running the old code) from immediately re-publishing old-template sandbox IDs into the shared buffer during a rolling deploy.
- `resize(max_idle)` and `release_all_idle()` can be called from any node.
- Configure `primary_lock_ttl` above `warmup_ready_timeout` plus expected preparer time and operational headroom. The SDKs renew leadership independently and fence every commit, but a lost lease causes in-flight warmups to be discarded instead of published.


## Minimal usage


### Python (sync)

python

```
from datetime import timedelta

from opensandbox import (
    AcquirePolicy,
    InMemoryPoolStateStore,
    PoolCreationSpec,
    SandboxPoolSync,
)
from opensandbox.config import ConnectionConfigSync

pool = SandboxPoolSync(
    pool_name="demo-pool",
    owner_id="worker-1",
    max_idle=2,
    state_store=InMemoryPoolStateStore(),
    connection_config=ConnectionConfigSync(domain="api.opensandbox.io"),
    creation_spec=PoolCreationSpec(image="ubuntu:22.04"),
    warmup_create_qps=10,
    warmup_concurrency=128,
)

pool.start()
try:
    sandbox = pool.acquire(
        sandbox_timeout=timedelta(minutes=30),
        policy=AcquirePolicy.DIRECT_CREATE,
    )
    try:
        result = sandbox.commands.run("echo pool-ok")
        print(result.logs.stdout[0].text)
    finally:
        sandbox.destroy()
finally:
    pool.shutdown(graceful=True)
```


### Python (asyncio)


`SandboxPoolAsync` has the same surface plus an `async with` context manager:

python

```
from datetime import timedelta

from opensandbox import (
    AcquirePolicy,
    InMemoryAsyncPoolStateStore,
    PoolCreationSpec,
    SandboxPoolAsync,
)
from opensandbox.config import ConnectionConfig

async with SandboxPoolAsync(
    pool_name="demo-pool",
    owner_id="worker-1",
    max_idle=2,
    state_store=InMemoryAsyncPoolStateStore(),
    connection_config=ConnectionConfig(domain="api.opensandbox.io"),
    creation_spec=PoolCreationSpec(image="ubuntu:22.04"),
) as pool:
    sandbox = await pool.acquire(
        sandbox_timeout=timedelta(minutes=30),
        policy=AcquirePolicy.DIRECT_CREATE,
    )
    try:
        result = await sandbox.commands.run("echo pool-ok")
    finally:
        await sandbox.destroy()
```


### Kotlin / Java

java

```
SandboxPool pool = SandboxPool.builder()
    .poolName("demo-pool")
    .ownerId("worker-1")
    .maxIdle(3)
    .stateStore(new InMemoryPoolStateStore())
    .connectionConfig(config)
    .creationSpec(PoolCreationSpec.builder()
        .image("ubuntu:22.04")
        .entrypoint(List.of("tail", "-f", "/dev/null"))
        .build())
    .warmupReadyTimeout(Duration.ofSeconds(45))
    .build();

pool.start();
try {
    Sandbox sb = pool.acquire(Duration.ofMinutes(10), AcquirePolicy.DIRECT_CREATE);
    try {
        sb.commands().run("echo pool-ok");
    } finally {
        try {
            sb.kill();
        } finally {
            sb.close();
        }
    }
} finally {
    pool.shutdown(true);
}
```


### Go


Inside a function returning `error`, with `ctx` and the usual `context`, `fmt`, `time`, and `opensandbox` imports:

go

```
pool, err := opensandbox.NewSandboxPoolBuilder().
    PoolName("demo-pool").
    OwnerID("worker-1").
    MaxIdle(3).
    ConnectionConfig(opensandbox.ConnectionConfig{Domain: "api.opensandbox.io"}).
    CreationSpec(opensandbox.PoolCreationSpec{Image: "ubuntu:22.04"}).
    StateStore(opensandbox.NewInMemoryPoolStateStore()).
    Build()
if err != nil {
    return err
}
if err := pool.Start(ctx); err != nil {
    return err
}
defer pool.Shutdown(context.Background(), true)

policy := opensandbox.AcquirePolicyDirectCreate
sb, err := pool.Acquire(ctx, opensandbox.AcquireOptions{
    SandboxTimeout: 10 * time.Minute,
    Policy:         &policy,
})
if err != nil {
    return err
}
defer sb.Close()
defer sb.Kill(context.Background())

result, err := sb.RunCommand(ctx, "echo pool-ok", nil)
if err != nil {
    return err
}
fmt.Println(result.Logs.Stdout)
return nil
```


### JavaScript / TypeScript

ts

```
import { AcquirePolicy, SandboxPool } from "@alibaba-group/opensandbox";

const pool = SandboxPool.create({
  poolName: "demo-pool",
  maxIdle: 2,
  connectionConfig: { domain: "localhost:8080", useServerProxy: true },
  creationSpec: { image: "python:3.12" },
  warmupCreateQps: 10,
  warmupConcurrency: 128,
});

await pool.start();
try {
  const sandbox = await pool.acquire({
    sandboxTimeoutSeconds: 600,
    policy: AcquirePolicy.DIRECT_CREATE,
  });
  try {
    const result = await sandbox.commands.run("echo pool-ok");
    console.log(result.logs.stdout);
  } finally {
    try {
      await sandbox.kill();
    } finally {
      await sandbox.close();
    }
  }
} finally {
  await pool.shutdown(true);
}
```


To share state across processes, install `redis`, connect it in the application, and pass this store as `stateStore`:

ts

```
import { createClient } from "redis";
import { RedisPoolStateStore } from "@alibaba-group/opensandbox/pool-redis";

const redis = createClient({ url: process.env.REDIS_URL });
await redis.connect();
const stateStore = new RedisPoolStateStore({
  client: redis,
  keyPrefix: "opensandbox:pool:prod",
});
// Pass stateStore to SandboxPool.create(...).
// After all pools/managers using it are shut down:
// await redis.quit();
```


The caller owns the Redis connection. Custom JavaScript preparers and health checks must bound their own work: cancellation can stop waiting for a callback without stopping the callback itself.


## Diagnostics and operations


Each pool SDK exposes these operations (names follow language conventions):


- `snapshot()` — pool phase, health, counters (idle size, in-flight warmups, consecutive failures, last error).
- `snapshot_idle_entries()` — the current idle sandbox IDs with expiry timestamps.
- `resize(max_idle)` — change the target buffer size at runtime. For business-hours sizing, see the [scheduled client pool example](https://open-sandbox.ai/examples/client-pool-schedule), which calls `Resize` from an application-level controller.
- `release_all_idle()` — drain the currently visible idle buffer and best-effort kill each entry, without stopping the pool. Useful to force a fresh set of warmups after a transient upstream problem. It does **not** change `max_idle`, does **not** fence other nodes, and does **not** stop an active leader from immediately replenishing — so it is not a safe way to swap creation templates on the same `pool_name`. For that case, retire the whole namespace under a new `pool_name` (see below).


The existing cleanup methods retain their original execution behavior. For opt-in bounded parallel cleanup, use Python's `release_all_idle_parallel(max_workers=50)`, Kotlin's `releaseAllIdle(concurrency)`, JavaScript's `releaseAllIdle(concurrency)`, or Go's concrete `(*DefaultSandboxPool).ReleaseAllIdleParallel(ctx, maxWorkers)`. These methods validate a positive concurrency value and wait for every drained ID to receive a best-effort kill attempt. The Go method is intentionally outside the `SandboxPool` interface to preserve compatibility with third-party implementors.


### Tracing warmups


Python, JavaScript, and Kotlin/Java emit opt-in OpenTelemetry warmup spans. Set `enable_tracing=True` in Python or `enableTracing: true` / `.enableTracing(true)` in JavaScript/JVM connection configuration. The application supplies its OpenTelemetry provider and exporter. See [SDK Tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing) for phase names and language-specific attributes.


Pool `shutdown` stops that local pool instance; it does not terminate sandboxes already handed to callers. To retire a shared namespace, use the manager below.


### Retiring an old pool namespace


Each supported pool SDK exposes a `SandboxPoolManager` with a `destroy` operation that applies the same `DESTROYING → DESTROYED` protocol:


1. Write a `DESTROYING` fence into the state store, so any still-running peer instance sees it and stops replenishing instead of racing the retirement.
2. Best-effort drain and kill every idle sandbox, bounded by the drain timeout.
3. Clear the persistent per-pool state.
4. Write a `DESTROYED` tombstone with the tombstone TTL (default 7 days) so future callers cannot silently rebind to the same `pool_name`.


Destroy is idempotent: calling it on an already-tombstoned namespace reports `DESTROYED` without draining or killing anything. If the drain or the cleanup cannot finish, the namespace stays `DESTROYING` and the call reports the destroy as incomplete; retrying is safe and picks up where it left off.


**Python / Kotlin** — `SandboxPoolManager.destroy(poolName, options)`, configured through `PoolDestroyOptions` (`strategy`, `drain_timeout`, `tombstone_ttl`).


**JavaScript** — `SandboxPoolManager.create({ stateStore, connectionConfig })`, then `await manager.destroy(poolName, options)`.


**Go** — `(*SandboxPoolManager).Destroy(ctx, poolName, options)`:

go

```
manager, err := opensandbox.NewSandboxPoolManagerBuilder().
    StateStore(store).
    ConnectionConfig(connCfg).
    Build()
if err != nil {
    return err
}

result, err := manager.Destroy(ctx, "orders-v2", opensandbox.PoolDestroyOptions{})
if err != nil {
    return err
}
log.Printf("retired %s: drained=%d killed=%d",
    result.PoolName, result.DrainedIdleCount, result.KilledIdleCount)
```


`PoolDestroyOptions` mirrors the other SDKs. `Strategy` selects the algorithm and only `PoolDestroyForce` is implemented. `DrainTimeout` and `TombstoneTTL` are `*time.Duration`: leave them nil for the defaults (30s and 7 days), or set an explicit zero to drain without a deadline and to write a tombstone that never expires.


The fence is what makes retirement safe without stopping every writer first, and it is enforced on two levels. The state store refuses `PutIdle`, `SetMaxIdle` and `SetIdleEntryTTL` with a `*PoolDestroyedError` and hands out no primary lock, which stops replenishment. The pool itself also checks the fence when it starts, before every acquire, again once an acquire holds a live sandbox, and on each reconcile tick: a surviving peer stops outright on its next tick, an in-flight acquire fails rather than minting a fresh sandbox into the retired namespace through the direct-create fallthrough, and a sandbox obtained just before the fence landed is killed instead of handed out. The post-acquire check matters because the idle take is deliberately left unfenced so `destroy` can drain: once an ID has been taken, `destroy` can no longer reach it, so the acquire has to dispose of it itself. Starting a fresh pool against a tombstoned `PoolName` fails for the same reason, so rebinding the name requires either waiting out the tombstone TTL or rotating to a new `PoolName`.


One deliberate exception: if the state store itself is unreachable, the destroy state is unknowable, so policies that already fall through to direct create on a store outage (`DIRECT_CREATE`, `RETRY_NEXT_IDLE_THEN_CREATE`) assume `ACTIVE` and proceed, matching the existing `try_take_idle` outage behavior. `FAIL_FAST` and `RETRY_NEXT_IDLE` surface the outage instead. That relaxation stops at a sandbox already taken from the idle buffer: there the check is fail-closed and an unreachable store means the sandbox is killed, because nothing else is tracking it any more.


## Further reading


- Python: [`/sdks/python`](https://open-sandbox.ai/sdks/python) — `SandboxPoolSync`, `SandboxPoolAsync`, Redis store.
- JavaScript: [SDK entry point](https://open-sandbox.ai/sdks/javascript) — `SandboxPool` and the `/pool-redis` export.
- Kotlin: [`/sdks/kotlin`](https://open-sandbox.ai/sdks/kotlin) — `SandboxPool` builder, `sandbox-pool-redis` module.
- Go: [`/sdks/go`](https://open-sandbox.ai/sdks/go) — `SandboxPool` interface, `RedisPoolStateStore`, distributed deployment notes.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/guides/client-pool.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/vscode`

# VS Code Example
## Build the VS Code Sandbox Image ​
## Start OpenSandbox server [local] ​
## Create and Access the VS Code Sandbox ​
## References ​






Launch code-server (VS Code Web) in OpenSandbox to provide browser access.


## Build the VS Code Sandbox Image


The Dockerfile in the example directory builds a sandbox image with code-server pre-installed:

shell

```
cd examples/vscode
docker build -t opensandbox/vscode:latest .
```


This image includes:


- code-server (VS Code Web) pre-installed
- Non-root user (vscode) for security
- Workspace directory at `/workspace`


## Start OpenSandbox server [local]


Pre-pull the VS Code image:

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/vscode:latest
```


Start the local OpenSandbox server:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the VS Code Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

uv run python examples/vscode/main.py
```


The script starts code-server (with authentication disabled), binds it to the specified port and outputs the accessible address. Uses the prebuilt VS Code image by default.


![VS Code screenshot shell](https://open-sandbox.ai/assets/vscode-screenshot-shell.BNH0vdPi.jpg) ![VS Code screenshot vscode](https://open-sandbox.ai/assets/vscode-screenshot-vscode.BFiUyHGW.jpg)


## References


- [code-server (VS Code Web)](https://github.com/coder/code-server)
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/vscode)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/vscode.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/claude-code`

Return to top

# Claude Code Example


Access Claude via the `claude-cli` npm package in OpenSandbox.


## Start OpenSandbox server [local]
*Access Claude via the claude-cli npm package in OpenSandbox.*

## Start OpenSandbox server [local] ​
## Create and Access the Claude Sandbox ​
## Headless Mode and Session Resume ​
## Environment Variables ​
## References ​







Pre-pull the code-interpreter image (includes Node.js):

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use docker hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


Then start the local OpenSandbox server, stdout logs will be visible in the terminal:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the Claude Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

# Run the example (requires SANDBOX_DOMAIN / SANDBOX_API_KEY / ANTHROPIC_AUTH_TOKEN)
uv run python examples/claude-code/main.py
```


The script installs the Claude CLI (`npm i -g @anthropic-ai/claude-code@latest`) at runtime (Node.js is already in the code-interpreter image), then sends a simple request `claude "Compute 1+1=?."`. Auth is passed via `ANTHROPIC_AUTH_TOKEN`, and you can override endpoint/model with `ANTHROPIC_BASE_URL` / `ANTHROPIC_MODEL`.


![Claude Code screenshot](https://open-sandbox.ai/assets/claude-code-screenshot.Bxpkwuls.jpg)


## Headless Mode and Session Resume


The example script also runs the two patterns used by coding-agent integrations: a headless run with structured output, and a follow-up turn that resumes the same conversation.


### Turn 1: headless run with structured output

shell

```
claude -p "Remember this for later: my favorite sandbox number is 42." --output-format json
```


With `-p` (print mode) the CLI answers the prompt and exits. `--output-format json` prints the reply, `session_id`, usage, and cost metadata as a single JSON object, so the script extracts `session_id` for the next turn.


### Turn 2: resume the session

shell

```
claude -p "What is my favorite sandbox number? Reply with just the number." \
  --resume <session_id> --output-format json
```


`--resume` continues a specific conversation with its context intact — the reply recalls "42" from turn 1. `--continue` resumes the most recent conversation instead; an explicit `--resume <session_id>` stays deterministic when several conversations live in the same sandbox.


Concurrent follow-ups


Add `--fork-session` to `--resume` / `--continue` to create a new session ID instead of reusing the original, so parallel follow-ups on the same conversation don't overwrite each other.


### Permission prompts in unattended runs


There is no terminal to answer permission prompts in a `-p` run: requests that would prompt are denied, so a task that needs a tool (file edits, shell commands) can fail. Two common remedies for agent workloads:


- `--dangerously-skip-permissions` (equivalent to `--permission-mode bypassPermissions`) runs tools without prompts — a common choice inside an ephemeral OpenSandbox container, where the sandbox itself is the isolation boundary.
- `--permission-mode dontAsk` stays fail-closed: only tools pre-approved by your permission rules run — the standard pattern for locked-down CI. (`--permission-prompts none`, Claude Code v2.1.259+, is the print-mode equivalent.)


The interactive UI needs a TTY


The interactive REPL (`claude "..."`) renders its UI, including permission prompts, on a terminal. Through a plain command pipe there is no way to answer a prompt, so the run can wait indefinitely. Use `-p` for scripted runs, or drive the interactive UI over a [PTY session](https://open-sandbox.ai/architecture/data-plane/execd).


To receive output as it is generated (token-level events) instead of a single final JSON object, use `--output-format stream-json --verbose --include-partial-messages`.


## Environment Variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional for local)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |
| `ANTHROPIC_AUTH_TOKEN` | *(required)* | Your Anthropic auth token |
| `ANTHROPIC_BASE_URL` | *(optional)* | Anthropic API endpoint (e.g., self-hosted proxy) |
| `ANTHROPIC_MODEL` | `claude_sonnet4` | Model name |


## References


- [claude-code](https://www.npmjs.com/package/claude-code) - NPM package for Claude Code CLI
- [Claude Code headless mode](https://code.claude.com/docs/en/headless) - Print mode, output formats, and session resume
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/claude-code)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/claude-code.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/playwright`

Return to top

# Playwright Example
## Build the Playwright Sandbox Image ​
## Start OpenSandbox server [local] ​
## Create and Access the Playwright Sandbox ​
## References ​






Access web pages in headless mode using Playwright + Chromium in OpenSandbox to scrape title/body snippets.


## Build the Playwright Sandbox Image


The Dockerfile in the example directory builds a sandbox image with Playwright and Chromium pre-installed:

shell

```
cd examples/playwright
docker build -t opensandbox/playwright:latest .
```


This image includes:


- Playwright Python package
- Chromium browser binaries
- Node.js and npm (for Playwright MCP)
- Non-root user (playwright) for security


## Start OpenSandbox server [local]


Pre-pull the Playwright image:

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/playwright:latest
```


Start the local OpenSandbox server:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the Playwright Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

uv run python examples/playwright/main.py
```


The script launches Chromium in headless mode to access the target URL, prints title/body snippets, and saves a full-page screenshot to `/home/playwright/screenshot.png` inside the sandbox. It also downloads the screenshot to the local working directory as `./screenshot.png`. Uses the prebuilt Playwright image by default.


![Playwright screenshot](https://open-sandbox.ai/assets/playwright-screenshot.CiGT7tK7.png)


## References


- [Playwright](https://playwright.dev/)
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/playwright)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/playwright.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/reference/code-interpreter-image-migration`

# Code Interpreter Image Migration Guide


Issue: [#1764](https://github.com/opensandbox-group/OpenSandbox/issues/1764)


## Background


Historically, the source Dockerfiles, environment setup scripts, and build tooling for the official `opensandbox/code-interpreter` container image lived inside the OpenSandbox monorepo under `sandboxes/code-interpreter/`.
*Issue: #1764*

## Background ​
## Scope of Separation ​
## Compatibility and Continuity ​
## Contributing and Reporting Issues ​






To separate platform runtime and SDK governance from specific sandbox userland environment implementations, the container image implementation has been extracted into a dedicated repository:


- **New repository**: [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images)


## Scope of Separation


### Extracted to Dedicated Repository


The following components and artifacts are now developed, versioned, and published from [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images):


- Dockerfiles (`Dockerfile`, `Dockerfile_base`)
- Environment bootstrap and lifecycle scripts (`code-interpreter.sh`, `code-interpreter-env.sh`, `jupyter_notebook_config.py`)
- Image build scripts and test suites (`build.sh`, `tests/test_code_interpreter_node_setup.sh`)
- Standalone image publication and release workflows


### Retained in OpenSandbox Monorepo


OpenSandbox continues to maintain full support for the code-interpreter experience in the monorepo:


- **Code Interpreter SDKs**: Multi-language SDKs for Python, JavaScript/TypeScript, C#/.NET, Kotlin/Java, and Go (`sdks/sandbox/go/code_interpreter.go`) remain in `sdks/`
- **Execution Daemon & Contracts**: In-sandbox daemon (`components/execd`) and public API contracts (`specs/execd-api.yaml`, `specs/sandbox-lifecycle.yml`)
- **Runnable Examples & Tests**: End-to-end tests and sample applications (`examples/code-interpreter/`)


## Compatibility and Continuity


This migration is purely structural for monorepo maintenance. Container image coordinates, pinned versions, startup paths, and SDK APIs remain fully compatible:


| Property | Status | Details |
| --- | --- | --- |
| **Image Names** | Unchanged | Published to `docker.io/opensandbox/code-interpreter`, `ghcr.io/opensandbox-group/opensandbox/code-interpreter`, and `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter` |
| **Existing Tags** | Valid | Existing pinned tags (such as `v1.1.0`) continue to resolve and run |
| **Startup Path** | Unchanged | Entrypoint `/opt/code-interpreter/code-interpreter.sh` remains standard |
| **Environment Variables** | Unchanged | Language version selection via `PYTHON_VERSION`, `JAVA_VERSION`, `NODE_VERSION`, `GO_VERSION` remains identical |
| **SDK Usage** | Unchanged | Client code using `CodeInterpreter` classes requires no modifications |


### Signature and Provenance Verification


Operators and users who verify container image signatures or build provenance should note the workflow identity:


- **Existing image releases** (such as `v1.1.0` and earlier) were published by the OpenSandbox monorepo and continue using the OpenSandbox workflow identity (`publish-components.yml`).
- **New releases** from [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images) use that repository's `release.yml` workflow identity.
- Users verifying Cosign signatures or provenance attestations for new releases must follow the verification documentation in [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images).


## Contributing and Reporting Issues


- **Container Image Issues or Requests**: If you need new pre-installed packages, updated language versions, or custom kernels in the `code-interpreter` environment image, please submit an issue or pull request at [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images).
- **SDK or Lifecycle Platform Issues**: For SDK bugs, lifecycle control plane features, or `execd` daemon issues, continue contributing to [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/reference/code-interpreter-image-migration.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/go`

# OpenSandbox Go SDK


Go client library for the [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox/) API.
*Go client library for the OpenSandbox API.*

## Installation ​
## Quick Start ​
*See Credential Vault for auth types, binding guidance, and Git/curl examples.*

## Lifecycle Hooks ​
## Fsb Template Management ​
## Snapshots and metadata ​
## API Reference ​
*Created with NewLifecycleClient(baseURL, apiKey string, opts ...Option).*

*Created with NewExecdClient(baseURL, accessToken string, opts ...Option).*

*Created with NewEgressClient(baseURL, authToken string, opts ...Option).*

## SSE Streaming ​
*Each StreamEvent contains:*

## Client Options ​
## Error Handling ​
*Non-2xx responses are returned as *opensandbox.APIError:*

## License ​












Provides high-level sandbox helpers and low-level clients for these API areas:


- **Lifecycle** -- Create, manage, and destroy sandbox instances
- **Execd** -- Execute commands, manage files, monitor metrics inside sandboxes
- **Egress** -- Inspect and mutate sandbox network policy at runtime


## Installation

bash

```
# go 1.20+
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```


## Quick Start


### Create and manage a sandbox


Use the high-level helper to create a sandbox, resolve its endpoint, and wait for readiness before running commands:

go

```
package main

import (
    "context"
    "fmt"
    "log"

    opensandbox "github.com/alibaba/OpenSandbox/sdks/sandbox/go"
)

func run() error {
    ctx := context.Background()
    ttl := 600
    config := opensandbox.ConnectionConfig{
        Domain: "localhost:8080",
        Protocol: "http",
        UseServerProxy: true,
    }
    sandbox, err := opensandbox.CreateSandbox(ctx, config, opensandbox.SandboxCreateOptions{
        Image: "python:3.12",
        TimeoutSeconds: &ttl,
    })
    if err != nil {
        return err
    }
    defer sandbox.Close()
    defer sandbox.Kill(context.Background())

    result, err := sandbox.RunCommand(ctx, "echo sandbox-ready", nil)
    if err != nil {
        return err
    }
    fmt.Println(result.Text())
    return nil
}

func main() {
    if err := run(); err != nil {
        log.Fatal(err)
    }
}
```


`ConnectSandbox` and `ResumeSandbox` check health only when you pass the optional `ReadyOptions` argument (an empty `ReadyOptions{}` uses the default check). Omitting it resolves the endpoint without a health check. Pause is asynchronous: wait until sandbox info reports `Paused` before resuming.


The following snippets go inside a function returning `error`, with the live `sandbox`, `config`, and `ctx` above. Add standard-library imports used by each snippet. Creation examples are alternatives; terminate sandboxes with `Kill` when done. `Close` currently does not terminate the sandbox.


### Run a command with streaming output


Use structured callbacks for normal command output:

go

```
result, err := sandbox.RunCommand(ctx, "echo 'Hello from sandbox!'", &opensandbox.ExecutionHandlers{
    OnStdout: func(message opensandbox.OutputMessage) error {
        fmt.Println(message.Text)
        return nil
    },
})
if err != nil {
    return err
}
if result.ExitCode == nil || *result.ExitCode != 0 {
    return fmt.Errorf("command failed: %v", result.Error)
}
```


Use the low-level client when you need raw SSE events or command status/log APIs. `event.Data` contains JSON; import `encoding/json` and `os` for this example:

go

```
endpoint, err := sandbox.GetEndpoint(ctx, 44772)
if err != nil {
    return err
}
exec := opensandbox.NewExecdClient(
    config.Protocol + "://" + endpoint.Endpoint, "",
    opensandbox.WithHeaders(endpoint.Headers),
)

err = exec.RunCommand(ctx, opensandbox.RunCommandRequest{
    Command: "echo 'Hello from sandbox!'",
    Timeout: 30000,
}, func(event opensandbox.StreamEvent) error {
    var message struct{ Type, Text string }
    if err := json.Unmarshal([]byte(event.Data), &message); err != nil {
        return err
    }
    switch message.Type {
    case "stdout":
        fmt.Println(message.Text)
    case "stderr":
        fmt.Fprintln(os.Stderr, message.Text)
    case "execution_complete":
        fmt.Println("[done]")
    }
    return nil
})
if err != nil {
    return err
}
```


`RunCommandRequest.Timeout` is in **milliseconds**. Use this low-level client for `InterruptCommand`, `GetCommandStatus`, and `GetCommandLogs`, which are not exposed as high-level `Sandbox` methods.


For native execution, replace the request above with the following. On Linux, it prints literal `$HOME` and keeps `hello world` as one argument:

go

```
_, err = sandbox.RunCommandWithOpts(ctx, opensandbox.RunCommandRequest{
    Argv:    []string{"printf", "%s\n", "$HOME", "hello world"},
    Timeout: 30000,
}, nil)
if err != nil {
    return err
}
```


Native argv execution requires an updated execd. See [command execution modes](https://open-sandbox.ai/architecture/data-plane/execd#command-execution) for executable lookup and platform behavior.


### Background commands


Reuse the `exec` client from the streaming example to poll status and incremental logs. Command timeout is in milliseconds and is separate from sandbox TTL.

go

```
execution, err := sandbox.RunCommandWithOpts(ctx, opensandbox.RunCommandRequest{
    Command: "for i in 1 2 3; do echo step-$i; sleep 1; done",
    Background: true,
    Timeout: 30_000,
}, nil)
if err != nil {
    return err
}
if execution.ID == "" {
    return fmt.Errorf("no command ID returned")
}
cursor := int64(0)
deadline := time.Now().Add(45 * time.Second)
for {
    if time.Now().After(deadline) {
        if err := exec.InterruptCommand(ctx, execution.ID); err != nil {
            return err
        }
        return fmt.Errorf("command did not finish")
    }
    status, err := exec.GetCommandStatus(ctx, execution.ID)
    if err != nil {
        return err
    }
    logs, err := exec.GetCommandLogs(ctx, execution.ID, &cursor)
    if err != nil {
        return err
    }
    fmt.Print(logs.Output)
    cursor = logs.Cursor
    if !status.Running {
        if status.ExitCode == nil || *status.ExitCode != 0 {
            return fmt.Errorf("command failed: %s", status.Error)
        }
        break
    }
    select {
    case <-ctx.Done():
        return ctx.Err()
    case <-time.After(500 * time.Millisecond):
    }
}
```


### Persistent shell sessions


A Bash session preserves shell variables and the working directory across commands.

go

```
session, err := sandbox.CreateSession(ctx)
if err != nil {
    return err
}
defer sandbox.DeleteSession(context.Background(), session.ID)
_, err = sandbox.RunInSession(ctx, session.ID, opensandbox.RunInSessionRequest{
    Command: "cd /tmp; export DEMO=hello",
    Timeout: 30_000,
}, nil)
if err != nil {
    return err
}
result, err := sandbox.RunInSession(ctx, session.ID, opensandbox.RunInSessionRequest{
    Command: "echo \"$DEMO\"; pwd",
    Timeout: 30_000,
}, nil)
if err != nil {
    return err
}
fmt.Println(result.Text())
```


### Persistent environment variables


Set environment variables that the runtime injects into every subsequent command and session — without hand-writing shell escaping against the sandbox env file.

go

```
err := sandbox.SetEnv(ctx, "MY_TOKEN", "it's a safe value")
```


Keys must match `[A-Za-z_][A-Za-z0-9_]*`. Values without a single quote are stored verbatim; values containing a single quote use the env file's double-quoted form, in which shell-style `$NAME` sequences may be expanded when the runtime loads the file. The env file is append-only: the last write for a key wins. Returns an error if the sandbox fails to persist the variable.


For filesystem/process isolation within a sandbox, see [Isolation Sessions](https://open-sandbox.ai/guides/isolation-sessions). These are separate from Bash sessions.


### File operations


Upload from an `io.Reader` and close download streams after use. This example uses `strings`, `io`, and `os` from the standard library:

go

```
err := sandbox.UploadFile(ctx, strings.NewReader("Hello Sandbox!"), opensandbox.UploadFileOptions{
    Metadata: opensandbox.FileMetadata{Path: "/tmp/demo.txt", Mode: 644},
})
if err != nil {
    return err
}
body, err := sandbox.DownloadFile(ctx, "/tmp/demo.txt", "")
if err != nil {
    return err
}
_, copyErr := io.Copy(os.Stdout, body)
closeErr := body.Close()
if copyErr != nil {
    return copyErr
}
if closeErr != nil {
    return closeErr
}
entries, err := sandbox.ListDirectory(ctx, "/tmp")
if err != nil {
    return err
}
for _, entry := range entries {
    fmt.Println(entry.Path)
}
if err := sandbox.DeleteFiles(ctx, []string{"/tmp/demo.txt"}); err != nil {
    return err
}
```


The same upload/download methods support binary files. Pass a Range header such as `"bytes=0-1023"` to `DownloadFile` for a partial download.


#### File operations with an explicit identity


Bind a filesystem client to a Linux UID and GID:

go

```
files, err := sandbox.FilesWithIdentity(1001, 2000)
if err != nil {
    return err
}
```


The bound client exposes the usual file operations and shares the sandbox connection, authentication, and endpoint routing headers. The existing file client retains its default identity. Select the UID/GID separately for command execution.


This requires Linux and an Execd version that supports filesystem execution identity. Unsupported servers return an error; requests never fall back to the default filesystem routes. Keep sandbox credentials and identity selection in the trusted backend. Linux filesystem permissions apply; this feature does not create a tenant isolation boundary. See [Execd](https://open-sandbox.ai/architecture/data-plane/execd) for permission and workspace provisioning details.


### Pause and reconnect


Pause is asynchronous and runtime-dependent. Use a deadline before resuming:

go

```
pauseCtx, cancel := context.WithTimeout(ctx, 2*time.Minute)
defer cancel()
if err := sandbox.Pause(pauseCtx); err != nil {
    return err
}
for {
    info, err := sandbox.GetInfo(pauseCtx)
    if err != nil {
        return err
    }
    if info.Status.State == "Paused" {
        break
    }
    if info.Status.State == "Failed" {
        return fmt.Errorf("pause failed: %s", info.Status.Message)
    }
    select {
    case <-pauseCtx.Done():
        return pauseCtx.Err()
    case <-time.After(time.Second):
    }
}
resumed, err := opensandbox.ResumeSandbox(ctx, config, sandbox.ID(), opensandbox.ReadyOptions{})
if err != nil {
    return err
}
defer resumed.Close()
if _, err := resumed.Renew(ctx, 30*time.Minute); err != nil {
    return err
}
```


Use `ConnectSandbox(ctx, config, id, opensandbox.ReadyOptions{})` to attach to an already running sandbox with a readiness check. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume).


### Resource metrics


Use `metrics, err := sandbox.GetMetrics(ctx)` to read current sandbox resource usage. This is separate from [SDK creation telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


### Check egress policy


Runtime egress reads and patches go directly to the sandbox egress sidecar. The SDK first resolves the sandbox endpoint on port `18080`, then calls the sidecar `/policy` API.

go

```
policy, err := sandbox.GetEgressPolicy(ctx)
if err != nil {
    return err
}
fmt.Printf("Mode: %s, Default: %s\n", policy.Mode, policy.Policy.DefaultAction)

_, err = sandbox.PatchEgressRules(ctx, []opensandbox.NetworkRule{
    {Action: "allow", Target: "api.example.com"},
})
if err != nil {
    return err
}
```


Template-backed sandboxes have no sandbox-side egress sidecar: the SDK detects them via the server's `OPEN-SANDBOX-ORIGIN` response header (see [Fsb Template Management](https://open-sandbox.ai/sdks/go#fsb-template-management)) and routes the same `GetEgressPolicy` / `PatchEgressRules` / `DeleteEgressRules` calls through the lifecycle control plane (`/sandboxes/{sandboxId}/networkpolicy`) instead.


Patch uses merge semantics:


- Incoming rules take priority over existing rules with the same `target`.
- Existing rules for other targets remain unchanged.


### Use Credential Vault


Credential Vault injects outbound credentials from the egress sidecar while keeping real secrets out of sandbox environment variables, commands, files, and logs. Create the sandbox with `CredentialProxy` enabled, then write credentials and bindings through the sandbox helpers or `EgressClient`.

go

```
config := opensandbox.ConnectionConfig{
    Domain:   "localhost:8080",
    Protocol: "http",
    APIKey:   "your-api-key",
}

sandbox, err := opensandbox.CreateSandbox(ctx, config, opensandbox.SandboxCreateOptions{
    Image: "python:3.11",
    NetworkPolicy: &opensandbox.NetworkPolicy{
        DefaultAction: "deny",
        Egress: []opensandbox.NetworkRule{
            {Action: "allow", Target: "api.example.com"},
        },
    },
    CredentialProxy: &opensandbox.CredentialProxyConfig{Enabled: true},
})
if err != nil {
    return err
}

_, err = sandbox.CreateCredentialVault(ctx, opensandbox.CredentialVaultCreateRequest{
    Credentials: []opensandbox.Credential{
        {
            Name: "api-token",
            Source: opensandbox.InlineCredentialSource{
                Type:  opensandbox.CredentialSourceInline,
                Value: "<token>",
            },
        },
    },
    Bindings: []opensandbox.CredentialBinding{
        {
            Name: "api-token",
            Match: opensandbox.CredentialMatch{
                Schemes: []opensandbox.CredentialScheme{opensandbox.CredentialSchemeHTTPS},
                Ports:   []int{443},
                Hosts:   []string{"api.example.com"},
                Paths:   []string{"/v1/*"},
            },
            Auth: opensandbox.CredentialAuth{
                Type:       opensandbox.CredentialAuthAPIKey,
                Name:       "x-api-key",
                Credential: "api-token",
            },
        },
    },
})
```


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for auth types, binding guidance, and Git/curl examples.


WARNING


Credential Vault is unavailable for template-backed sandboxes: they have no sandbox-side egress sidecar. `sandbox.CredentialVault(ctx)` returns an error for them.


### Client Pool


Use `NewSandboxPoolBuilder` with an in-memory store or the Redis adapter in `github.com/alibaba/OpenSandbox/sdks/sandbox/go/poolredis`. Go supports all four acquire policies, namespace retirement, and per-acquire TTL/health-check overrides.


Go uses `ReconcileInterval` and `WarmupConcurrency`; it does not expose the Python/JVM/JavaScript create-QPS, initial-delay, or post-prepare-check settings. See [Client Pool](https://open-sandbox.ai/guides/client-pool) for defaults, examples, and cleanup. Go does not currently emit built-in pool warmup traces or expose stable remote diagnostics; use [CLI or HTTP diagnostics](https://open-sandbox.ai/api/#diagnostics).


## Lifecycle Hooks


Set `Lifecycle` in `SandboxCreateOptions`. `PreStart` completes before the entrypoint starts, while `Periodic` hooks run on their schedules after startup.

go

```
hookTimeout := 120
sandbox, err := opensandbox.CreateSandbox(ctx, config, opensandbox.SandboxCreateOptions{
    Image: "ubuntu:24.04",
    Lifecycle: &opensandbox.SandboxLifecycle{
        PreStart: &opensandbox.LifecycleHook{
            Command:        []string{"sh", "-c", "echo ready > /tmp/prestart.done"},
            TimeoutSeconds: &hookTimeout,
        },
        Periodic: []opensandbox.PeriodicLifecycleHook{
            {
                Name:           "checkpoint",
                Schedule:       "@every 5m",
                Command:        []string{"sh", "-c", "date -u >> /tmp/checkpoints.log"},
                TimeoutSeconds: &hookTimeout,
            },
        },
    },
})
if err != nil {
    return err
}
defer sandbox.Close()
defer sandbox.Kill(context.Background())
fmt.Println(sandbox.ID())
```


The Server validates `TimeoutSeconds`; `PreStart` accepts 1–10800 seconds, while `Periodic` accepts 1–300 seconds. Both default to 60 seconds when omitted. See [Lifecycle Hooks](https://open-sandbox.ai/guides/lifecycle-hooks) for timing, failure behavior, and provider limitations.


### Idle policy (auto-pause and wake-on-access)


`SandboxLifecycle.IdlePolicy` (OSEP-0024, fast-sandbox only) tells the control plane to auto-pause the sandbox after `IdleTimeoutSeconds` (30–86400) of continuously idle ingress-observed traffic, and to wake it on the next request. It is control-plane state: it never reaches the guest, is accepted in template mode (`SandboxFromTemplateOptions.IdlePolicy`), and is rejected by non-fast-sandbox backends. Omitting it preserves non-automated behavior exactly.

go

```
idleTimeout := 300
wakeOnAccess := true
sandbox, err := opensandbox.CreateSandbox(ctx, config, opensandbox.SandboxCreateOptions{
    Image: "ubuntu:24.04",
    Lifecycle: &opensandbox.SandboxLifecycle{
        IdlePolicy: &opensandbox.IdlePolicy{
            IdleTimeoutSeconds: &idleTimeout,
            OnIdle:             opensandbox.OnIdlePause,
            WakeOnAccess:       &wakeOnAccess,
        },
    },
})
```


`ActiveProbe` lets the application veto a pause while real work runs without producing ingress traffic: declare an endpoint answering `{"active": bool, "message"?: string}` and the server polls it when the sandbox is otherwise idle; a busy answer resets the idle clock. Invalid policies fail fast client-side through `IdlePolicy.Validate()`.


### Wake retry


A request to a paused sandbox may arrive while its restore is still in progress. The gateway answers `503` with the `OpenSandbox-Wake: expired` marker; the client recognizes it and resends the original request after the `Retry-After` delay (safe for any method — the marker proves the request was never forwarded). The wake budget defaults to 5 attempts / 60 seconds across all wake cycles; when it is exhausted the client returns a `*SandboxWakeTimeoutError` (carrying `Attempts` and `Waited`) while the server-side resume continues in the background. Bare `503` responses follow the existing retry rules untouched. Wake retry is active whenever a `WithRetry` config is set (`WakeRetryEnabled` defaults to enabled even for hand-built configs; pass `WakeRetryDisabled()` to opt out); streaming connections bypass wake retry — a waking sandbox fails fast with the marked 503 instead of parking the connect — matching the other official SDKs, and established streams are never re-executed.


## Fsb Template Management


fsb (fast-sandbox microVM) golden-image templates are managed through `SandboxManager`. Template builds are asynchronous: `CreateTemplate` returns with `Status.Phase` set to `Pending`; poll `GetTemplate` until the phase reaches `Succeeded` or `Failed`. Only a `Succeeded` template can create sandboxes. Template management requires a configured Fsb provider on Kubernetes. Replace the publish URI with a location configured for your server.

go

```
manager := opensandbox.NewSandboxManager(config)

buildCtx, cancel := context.WithTimeout(ctx, 15*time.Minute)
defer cancel()

// Start the async build (starts at TemplatePhasePending)
template, err := manager.CreateTemplate(buildCtx, opensandbox.CreateTemplateRequest{
    Image:          "alpine:3.19",
    Publish:        "s3://bucket/publish",
    ResourceLimits: opensandbox.ResourceLimits{"cpu": "1", "memory": "512Mi", "disk": "2Gi"},
    Readiness:      &opensandbox.TemplateReadiness{Probe: "tcp://127.0.0.1:44772"},
    Metadata:       map[string]string{"team": "backend"},
})
if err != nil {
    return err
}

// Poll until the build finishes
for template.Status.Phase != opensandbox.TemplatePhaseSucceeded &&
    template.Status.Phase != opensandbox.TemplatePhaseFailed {
    select {
    case <-buildCtx.Done():
        return buildCtx.Err()
    case <-time.After(2 * time.Second):
    }
    template, err = manager.GetTemplate(buildCtx, template.TemplateID)
    if err != nil {
        return err
    }
}
if template.Status.Phase == opensandbox.TemplatePhaseFailed {
    return fmt.Errorf("template build failed: %s", template.TemplateID)
}

// List with metadata filters (1-indexed paging)
listed, err := manager.ListTemplates(ctx, opensandbox.ListTemplatesOptions{
    Metadata: map[string]string{"team": "backend"},
    Page:     1,
    PageSize: 20,
})
if err != nil {
    return err
}
fmt.Println(listed)

// When no longer needed: manager.DeleteTemplate(ctx, template.TemplateID)
```


### Creating a Sandbox from a Template


Use `CreateSandboxFromTemplate` to create a sandbox from a `Succeeded` template. Template mode fixes the workload shape on the server: only `Metadata`, `NetworkPolicy` and `Extensions` may accompany the template ID, and `TimeoutSeconds` is required.

go

```
sandbox, err := opensandbox.CreateSandboxFromTemplate(ctx, config, "tpl-abc",
    opensandbox.SandboxFromTemplateOptions{
        TimeoutSeconds: 600,
        NetworkPolicy: &opensandbox.NetworkPolicy{
            DefaultAction: "deny",
            Egress: []opensandbox.NetworkRule{
                {Action: "allow", Target: "api.example.com"},
            },
        },
    })
if err != nil {
    return err
}

fmt.Println(sandbox.Origin()) // "template"
```


## Snapshots and metadata


`Sandbox.CreateSnapshot` and `SandboxManager.CreateSnapshot` start snapshot creation. Use manager `GetSnapshot`, `ListSnapshots`, and `DeleteSnapshot` to manage snapshots, then pass `SnapshotID` to `SandboxCreateOptions` to restore. Poll snapshot status before restore. Use `Sandbox.PatchMetadata` or `SandboxManager.PatchSandboxMetadata` to add/replace keys; nil values remove keys.


Snapshot support depends on the runtime and server configuration. Renew the source sandbox first if its remaining TTL may expire during snapshot creation. Wait for `Ready` before restoring. This example retains the snapshot for reuse:

go

```
manager := opensandbox.NewSandboxManager(config)
snapshot, err := sandbox.CreateSnapshot(ctx, opensandbox.CreateSnapshotRequest{Name: "demo"})
if err != nil {
    return err
}
fmt.Println("Snapshot:", snapshot.ID)
snapshotCtx, cancel := context.WithTimeout(ctx, 15*time.Minute)
defer cancel()
for {
    snapshot, err = manager.GetSnapshot(snapshotCtx, snapshot.ID)
    if err != nil {
        return err
    }
    if snapshot.Status.State == opensandbox.SnapshotStateReady {
        break
    }
    if snapshot.Status.State == opensandbox.SnapshotStateFailed {
        return fmt.Errorf("snapshot failed: %s", snapshot.Status.Message)
    }
    select {
    case <-snapshotCtx.Done():
        return snapshotCtx.Err()
    case <-time.After(2 * time.Second):
    }
}
restored, err := opensandbox.CreateSandbox(ctx, config, opensandbox.SandboxCreateOptions{
    SnapshotID: snapshot.ID,
})
if err != nil {
    return err
}
defer restored.Close()
defer restored.Kill(context.Background())
fmt.Println(restored.ID())
// When no longer needed: manager.DeleteSnapshot(ctx, snapshot.ID)
```


Add/replace a metadata key and remove another:

go

```
project := "demo"
if _, err := sandbox.PatchMetadata(ctx, opensandbox.MetadataPatch{
    "project": &project, "obsolete-key": nil,
}); err != nil {
    return err
}
```


## API Reference


### LifecycleClient


Created with `NewLifecycleClient(baseURL, apiKey string, opts ...Option)`.


| Method | Description |
| --- | --- |
| `CreateSandbox(ctx, req)` | Create a new sandbox from a container image |
| `GetSandbox(ctx, id)` | Get sandbox details by ID |
| `ListSandboxes(ctx, opts)` | List sandboxes with filtering and pagination |
| `DeleteSandbox(ctx, id)` | Delete a sandbox |
| `PauseSandbox(ctx, id)` | Pause a running sandbox |
| `ResumeSandbox(ctx, id)` | Resume a paused sandbox |
| `RenewExpiration(ctx, id, expiresAt)` | Set sandbox expiration to a future timestamp (may shorten or extend) |
| `GetEndpoint(ctx, sandboxID, port, useServerProxy)` | Get public endpoint for a sandbox port |
| `GetSignedEndpoint(ctx, sandboxID, port, expires)` | Get signed endpoint URL with a signed route token |
| `CreateTemplate(ctx, req)` | Declare a fsb template (async golden-image build) |
| `GetTemplate(ctx, templateID)` | Get a template with its latest build status |
| `ListTemplates(ctx, opts)` | List templates with metadata filtering and pagination |
| `DeleteTemplate(ctx, templateID)` | Delete a template |
| `GetNetworkPolicy(ctx, sandboxID)` | Get a sandbox's egress policy from the control plane |
| `PatchNetworkPolicy(ctx, sandboxID, rules)` | Merge egress rules into a sandbox's policy |
| `DeleteNetworkPolicyRules(ctx, sandboxID, targets)` | Remove a sandbox's egress rules by target |


### ExecdClient


Created with `NewExecdClient(baseURL, accessToken string, opts ...Option)`.


**Health:**


| Method | Description |
| --- | --- |
| `Ping(ctx)` | Check server health |


**Code Execution:**


| Method | Description |
| --- | --- |
| `ListContexts(ctx, language)` | List active code execution contexts |
| `CreateContext(ctx, req)` | Create a code execution context |
| `GetContext(ctx, contextID)` | Get context details |
| `DeleteContext(ctx, contextID)` | Delete a context |
| `DeleteContextsByLanguage(ctx, language)` | Delete all contexts for a language |
| `ExecuteCode(ctx, req, handler)` | Execute code with SSE streaming |
| `InterruptCode(ctx, sessionID)` | Interrupt running code |


**Command Execution:**


| Method | Description |
| --- | --- |
| `CreateSession(ctx)` | Create a bash session |
| `RunInSession(ctx, sessionID, req, handler)` | Run command in session with SSE |
| `DeleteSession(ctx, sessionID)` | Delete a bash session |
| `RunCommand(ctx, req, handler)` | Run a command with SSE streaming |
| `InterruptCommand(ctx, sessionID)` | Interrupt running command |
| `GetCommandStatus(ctx, commandID)` | Get command execution status |
| `GetCommandLogs(ctx, commandID, cursor)` | Get command stdout/stderr |


**File Operations:**


| Method | Description |
| --- | --- |
| `GetFileInfo(ctx, path)` | Get file metadata |
| `DeleteFiles(ctx, paths)` | Delete files |
| `SetPermissions(ctx, req)` | Change file permissions |
| `MoveFiles(ctx, req)` | Move/rename files |
| `SearchFiles(ctx, dir, pattern)` | Search files by glob pattern |
| `ListDirectory(ctx, path)` | List immediate directory contents (server-side default depth) |
| `ListDirectoryWithDepth(ctx, path, depth)` | List directory contents up to the given depth (`0` returns empty) |
| `ReplaceInFiles(ctx, req)` | Text replacement in files |
| `UploadFile(ctx, file, opts)` | Upload a file to the sandbox |
| `UploadFiles(ctx, entries)` | Upload multiple files to the sandbox |
| `DownloadFile(ctx, remotePath, rangeHeader)` | Download a file from the sandbox |


**Directory Operations:**


| Method | Description |
| --- | --- |
| `CreateDirectory(ctx, path, mode)` | Create a directory (mkdir -p) |
| `DeleteDirectory(ctx, path)` | Delete a directory recursively |


**Metrics:**


| Method | Description |
| --- | --- |
| `GetMetrics(ctx)` | Get system resource metrics |
| `WatchMetrics(ctx, handler)` | Stream metrics via SSE |


### EgressClient


Created with `NewEgressClient(baseURL, authToken string, opts ...Option)`.


| Method | Description |
| --- | --- |
| `GetPolicy(ctx)` | Get current egress policy |
| `PatchPolicy(ctx, rules)` | Merge rules into current policy |
| `CreateCredentialVault(ctx, req)` | Create sandbox-local Credential Vault state |
| `GetCredentialVault(ctx)` | Get sanitized Credential Vault state |
| `PatchCredentialVault(ctx, req)` | Atomically mutate credentials and bindings |
| `DeleteCredentialVault(ctx)` | Delete sandbox-local Credential Vault state |
| `ListCredentialVaultCredentials(ctx)` | List sanitized credential metadata |
| `GetCredentialVaultCredential(ctx, name)` | Get sanitized metadata for one credential |
| `ListCredentialVaultBindings(ctx)` | List sanitized binding metadata |
| `GetCredentialVaultBinding(ctx, name)` | Get sanitized metadata for one binding |


## SSE Streaming


Methods that stream output (`RunCommand`, `ExecuteCode`, `RunInSession`, `WatchMetrics`) accept an `EventHandler` callback:

go

```
type EventHandler func(event opensandbox.StreamEvent) error
```


Each `StreamEvent` contains:


- `Event` -- the event type (e.g. `"stdout"`, `"stderr"`, `"result"`, `"execution_complete"`). For NDJSON streams, this is extracted from the JSON `type` field automatically.
- `Data` -- the raw event payload (JSON string for NDJSON streams).
- `ID` -- optional event identifier


Return a non-nil error from the handler to stop processing the stream early.


## Client Options


All client constructors accept optional `Option` functions. Custom HTTP clients and health checks must honor context cancellation for timeouts to take effect:

go

```
// Reuse the resolved endpoint from the streaming example.
execClient := opensandbox.NewExecdClient(
    config.Protocol + "://" + endpoint.Endpoint, "",
    opensandbox.WithHeaders(endpoint.Headers),
    opensandbox.WithHTTPClient(&http.Client{Timeout: 60 * time.Second}),
)
if err := execClient.Ping(ctx); err != nil {
    return err
}
```


TLS Certificate Strength


SDK-created HTTP clients enforce NIST 2030 minimum TLS certificate strength by default (RSA >= 2048, EC >= 224, DSA P >= 2048/Q >= 224, hash >= 224). If you must interoperate with legacy endpoints, set `AllowWeakServerCertKeyLengths: true` in `TransportConfig`.


SDK Telemetry


`CreateSandbox` reports create latency to `POST /v1/metrics/events` by default. Set `ConnectionConfig.DisableMetrics` or `OPENSANDBOX_DISABLE_METRICS=1` to opt out. See [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


### Follow redirects


The Go SDK retains Go's standard redirect behavior, including for file uploads and downloads. On redirects to a different origin (scheme, hostname, or effective port), it removes the client's default and configured authentication headers (including `X-EXECD-ACCESS-TOKEN`, `X-API-Key`, or a custom `WithAuthHeader` name), as well as all headers whose names start with `OPEN-SANDBOX-` or `OPENSANDBOX-`, case-insensitively. Each redirect destination is compared with the initial request's origin, so subsequent hops on another origin remain protected. Same-origin redirects retain these headers. Unrelated custom headers continue to follow Go's standard forwarding rules.


This protection applies to lifecycle (including creation metrics), execd, egress, file transfers, and SSE requests. A custom `http.Client.CheckRedirect` supplied through `WithHTTPClient` or `ConnectionConfig.HTTPClient` still controls whether redirects are followed; the SDK removes protected headers after that callback runs, even if the callback adds them again. The SDK copies the supplied HTTP client rather than modifying it. HTTP and HTTPS default ports are treated as equivalent to explicit ports 80 and 443 respectively. Upload method conversion and body replay follow Go's existing rules; this protection does not enable replay of streaming multipart bodies.


## Error Handling


Non-2xx responses are returned as `*opensandbox.APIError`:

go

```
_, err := sandbox.GetInfo(ctx)
if err != nil {
    var apiErr *opensandbox.APIError
    if errors.As(err, &apiErr) {
        fmt.Printf("HTTP %d: %s — %s\n", apiErr.StatusCode, apiErr.Response.Code, apiErr.Response.Message)
    }
    return err
}
```


## License


Apache 2.0[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/go.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/python`

# OpenSandbox SDK for Python
## Installation ​
## Quick Start ​
## Client Pool and observability ​
## Lifecycle Hooks ​
## Usage Examples ​
*Use SandboxManager for administrative tasks and finding existing sandboxes.*

## Snapshots, templates, and metadata ​
*Create from an existing template after its build reaches Succeeded:*

## Configuration ​









Create sandboxes, run commands, and manage files with async or synchronous Python APIs.


## Installation


### pip

bash

```
pip install opensandbox
```


### uv

bash

```
uv add opensandbox
```


## Quick Start


The following example shows how to create a sandbox and execute a shell command.


TIP


Before running this example, ensure the OpenSandbox service is running. See the [Getting Started](https://open-sandbox.ai/getting-started/) guide for startup instructions.

python

```
import asyncio
from opensandbox.sandbox import Sandbox
from opensandbox.config import ConnectionConfig
from opensandbox.exceptions import SandboxException

async def main():
    # 1. Configure connection
    config = ConnectionConfig(
        domain="api.opensandbox.io",
        api_key="your-api-key"
    )

    # 2. Create a Sandbox
    try:
        sandbox = await Sandbox.create(
            "ubuntu",
            connection_config=config
        )
        try:
            # 3. Execute a shell command
            execution = await sandbox.commands.run("echo 'Hello Sandbox!'")

            # 4. Print output
            print(execution.logs.stdout[0].text)
        finally:
            # 5. Terminate the remote sandbox and close local resources
            await sandbox.destroy()

    except SandboxException as e:
        # Handle Sandbox specific exceptions
        print(f"Sandbox Error: [{e.error.code}] {e.error.message}")
        # Server logs can be correlated by this request id (if available)
        print(f"Request ID: {e.request_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```


### Synchronous Quick Start


If you prefer a synchronous API, use `SandboxSync` / `SandboxManagerSync` and `ConnectionConfigSync`:

python

```
from datetime import timedelta

from opensandbox import SandboxSync
from opensandbox.config import ConnectionConfigSync

config = ConnectionConfigSync(
    domain="api.opensandbox.io",
    api_key="your-api-key",
    request_timeout=timedelta(seconds=30),
)

sandbox = SandboxSync.create("ubuntu", connection_config=config)
try:
    execution = sandbox.commands.run("echo 'Hello Sandbox!'")
    print(execution.logs.stdout[0].text)
finally:
    sandbox.destroy()
```


Use `destroy()` for create-use-discard workflows. It calls `kill()` before `close()` and still closes local resources if remote termination fails. Context managers continue to call only `close()`, so the remote sandbox remains available for later `connect()` calls unless you explicitly kill or destroy it.


## Client Pool and observability


Use `SandboxPoolSync` for synchronous applications and `SandboxPoolAsync` for asyncio. Both provide in-memory and Redis-backed stores, four acquire policies, and staged warmup controls. See [Client Pool](https://open-sandbox.ai/guides/client-pool) for examples, configuration, cleanup, and distributed deployment.


Enable `ConnectionConfig(enable_tracing=True)` or `ConnectionConfigSync(enable_tracing=True)` for [pool warmup traces](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing). For remote logs/events, use the [Diagnostics](https://open-sandbox.ai/api/#diagnostics) manager API. Create-latency reporting is controlled separately by [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Lifecycle Hooks


Pass a `SandboxLifecycle` when creating a sandbox. `pre_start` completes before the entrypoint starts, while `periodic` hooks run on their schedules after startup.

python

```
from opensandbox.models.sandboxes import (
    LifecycleHook,
    PeriodicLifecycleHook,
    SandboxLifecycle,
)

sandbox = await Sandbox.create(
    "ubuntu:24.04",
    connection_config=config,
    lifecycle=SandboxLifecycle(
        pre_start=LifecycleHook(
            command=["sh", "-c", "echo ready > /tmp/prestart.done"],
            timeout_seconds=120,
        ),
        periodic=[
            PeriodicLifecycleHook(
                name="checkpoint",
                schedule="@every 5m",
                command=["sh", "-c", "date -u >> /tmp/checkpoints.log"],
                timeout_seconds=120,
            )
        ],
    ),
)
```


The Server validates `timeout_seconds`; `pre_start` accepts 1–10800 seconds, while `periodic` accepts 1–300 seconds. Both default to 60 seconds when omitted. See [Lifecycle Hooks](https://open-sandbox.ai/guides/lifecycle-hooks) for timing, failure behavior, and provider limitations.


### Idle policy (auto-pause and wake-on-access)


`SandboxLifecycle.idle_policy` (OSEP-0024, fast-sandbox only) tells the control plane to auto-pause the sandbox after `idle_timeout_seconds` (30–86400) of continuously idle ingress-observed traffic, and to wake it on the next request. It is control-plane state: it never reaches the guest, is allowed in template mode (`Sandbox.create_from_template(idle_policy=...)`), and is rejected by non-fast-sandbox backends. Omitting it preserves non-automated behavior exactly.

python

```
sandbox = await Sandbox.create(
    "ubuntu:24.04",
    connection_config=config,
    timeout_seconds=86400,
    lifecycle=SandboxLifecycle(
        idle_policy=IdlePolicy(
            idle_timeout_seconds=300,
            on_idle="pause",
            wake_on_access=True,
        )
    ),
)
```


`active_probe` lets the application veto a pause while real work runs without producing ingress traffic: declare an endpoint answering `{"active": bool, "message"?: string}` and the server polls it when the sandbox is otherwise idle; a busy answer resets the idle clock.

python

```
IdlePolicy(
    idle_timeout_seconds=300,
    on_idle="pause",
    active_probe=ActivityProbe(port=8080, path="/active", timeout_seconds=2),
)
```


### Wake retry


A request to a paused sandbox may arrive while its restore is still in progress. The gateway answers `503` with the `OpenSandbox-Wake: expired` marker; the SDK recognizes it and resends the original request after the `Retry-After` delay (safe for any method — the marker proves the request was never forwarded). The wake budget defaults to 5 attempts / 60 seconds across all wake cycles; when it is exhausted the SDK raises `SandboxWakeTimeoutException` (carrying `attempts` and `waited`) while the server-side restore continues in the background. Bare `503` responses follow the existing retry rules untouched. Streaming (SSE) calls bypass wake retry.


## Usage Examples


The snippets below use `config` and a live `sandbox` from the quick start. Run async snippets inside an async function, before its cleanup block. Creation examples are alternatives; call `destroy()` when each sandbox is no longer needed. For the synchronous API, use `SandboxSync` and `SandboxManagerSync`, and omit `await` / `async` from SDK calls and context managers.


### 1. Lifecycle Management


Manage the sandbox lifecycle, including renewal, pausing, and resuming.

python

```
import time
from datetime import timedelta

# Renew the sandbox
# This resets the expiration time to (current time + duration)
await sandbox.renew(timedelta(minutes=30))

# Request pause (runtime-dependent)
await sandbox.pause()

deadline = time.monotonic() + 120
while True:
    if time.monotonic() >= deadline:
        raise TimeoutError("Sandbox did not pause within 120 seconds")
    info = await sandbox.get_info()
    if info.status.state == "Paused":
        break
    if info.status.state == "Failed":
        raise RuntimeError(info.status.message)
    await asyncio.sleep(1)

# Resume creates a new local handle.
resumed = await Sandbox.resume(sandbox_id=sandbox.id, connection_config=config)
await sandbox.close()
sandbox = resumed

# Get current status
info = await sandbox.get_info()
print(f"State: {info.status.state}")
print(f"Expires: {info.expires_at}")  # None when no automatic expiration is configured
```


Pause is asynchronous and runtime-dependent. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume). Use `await Sandbox.connect(sandbox_id, connection_config=config)` to attach to an already running sandbox without resuming it.


Create a non-expiring sandbox by explicitly passing `timeout=None`. Omitting `timeout` uses the default 10-minute TTL:

python

```
manual = await Sandbox.create(
    "ubuntu",
    connection_config=config,
    timeout=None,
)
```


### 2. Custom Health Check


Resolving an endpoint confirms that a route exists; it does not confirm that the application on that port is healthy. For service readiness, make a bounded request to the application's health endpoint and include the returned endpoint headers.


With the built-in health probe, readiness checks during creation, connection, and resume fail immediately when the health endpoint returns HTTP 401 or 403. The SDK raises `SandboxApiException` with the original status, error details, and request ID instead of waiting for `SandboxReadyTimeoutException`. Check the endpoint credentials or permissions before retrying. Transient health failures retain their existing polling behavior; `is_healthy()` still returns `False` for a failed built-in health probe.


Define custom logic to determine if the sandbox is healthy. This overrides the default ping check. Synchronous checks must set their own timeouts because the SDK cannot interrupt them; asynchronous checks must not block the event loop or suppress cancellation.

python

```
import httpx

async def custom_health_check(sbx: Sandbox) -> bool:
    endpoint = await sbx.get_endpoint(80)
    url = f"{sbx.connection_config.protocol}://{endpoint.endpoint}/"
    try:
        async with httpx.AsyncClient(timeout=2) as client:
            response = await client.get(url, headers=endpoint.headers)
        return response.status_code == 200
    except httpx.RequestError:
        return False

sandbox = await Sandbox.create(
    "nginx:latest",
    entrypoint=["nginx", "-g", "daemon off;"],
    connection_config=config,
    health_check=custom_health_check,
)
```


### 3. Command Execution & Streaming


Execute commands and handle output streams in real-time.

python

```
from opensandbox.models.execd import ExecutionHandlers, RunCommandOpts

# Define async handlers for streaming output
async def handle_stdout(msg):
    print(f"STDOUT: {msg.text}")

async def handle_stderr(msg):
    print(f"STDERR: {msg.text}")

async def handle_complete(complete):
    print(f"Command finished in {complete.execution_time_in_millis}ms")

# Create handlers (all handlers must be async)
handlers = ExecutionHandlers(
    on_stdout=handle_stdout,
    on_stderr=handle_stderr,
    on_execution_complete=handle_complete
)

# Execute command with handlers
result = await sandbox.commands.run(
    "for i in {1..5}; do echo \"Count $i\"; sleep 0.5; done",
    handlers=handlers
)
```


To execute a native program without shell parsing, pass an argument list. On Linux, this example prints literal `$HOME` and keeps `hello world` as one argument:

python

```
result = await sandbox.commands.run(["printf", "%s\n", "$HOME", "hello world"])
```


Native argv execution requires an updated execd. See [command execution modes](https://open-sandbox.ai/architecture/data-plane/execd#command-execution) for executable lookup and platform behavior.


#### Background commands


Start a bounded command, read incremental logs, and check its exit status. Command timeout and sandbox TTL are separate settings.

python

```
import time
from datetime import timedelta
from opensandbox.models.execd import RunCommandOpts

execution = await sandbox.commands.run(
    'for i in 1 2 3; do echo "step $i"; sleep 1; done',
    opts=RunCommandOpts(background=True, timeout=timedelta(seconds=30)),
)
if not execution.id:
    raise RuntimeError("No command ID returned")
cursor = 0
deadline = time.monotonic() + 45
while True:
    if time.monotonic() >= deadline:
        await sandbox.commands.interrupt(execution.id)
        raise TimeoutError("Command did not finish")
    status = await sandbox.commands.get_command_status(execution.id)
    logs = await sandbox.commands.get_background_command_logs(execution.id, cursor)
    print(logs.content, end="")
    cursor = logs.cursor if logs.cursor is not None else cursor
    if status.running is False:
        if status.exit_code != 0:
            raise RuntimeError(f"Command failed: {status.exit_code}, {status.error}")
        break
    await asyncio.sleep(0.5)
```


#### Persistent shell sessions


Use a Bash session to preserve shell variables and the working directory across commands. Delete the session when finished.

python

```
session_id = await sandbox.commands.create_session(working_directory="/tmp")
try:
    await sandbox.commands.run_in_session(session_id, "export DEMO=hello")
    result = await sandbox.commands.run_in_session(session_id, 'echo "$DEMO"; pwd')
    print("".join(message.text for message in result.logs.stdout))
finally:
    await sandbox.commands.delete_session(session_id)
```


#### Persistent environment variables


Set environment variables that the runtime injects into every subsequent command and session — without hand-writing shell escaping against the sandbox env file.

python

```
await sandbox.commands.set_env("MY_TOKEN", "it's a safe value")
```


Keys must match `[A-Za-z_][A-Za-z0-9_]*`. Values without a single quote are stored verbatim; values containing a single quote use the env file's double-quoted form, in which shell-style `$NAME` sequences may be expanded when the runtime loads the file. The env file is append-only: the last write for a key wins. Raises `SandboxException` if the sandbox fails to persist the variable. The sync API exposes the same method on `sandbox.commands`.


For commands that need filesystem/process isolation within a sandbox, see [Isolation Sessions](https://open-sandbox.ai/guides/isolation-sessions). These are separate from Bash sessions.


### 4. File Operations


Manage files and directories, including read, write, list, delete, and search.

python

```
from opensandbox.models.filesystem import DirectoryListEntry, WriteEntry, SearchEntry

# 1. Write file
await sandbox.files.write_files([
    WriteEntry(
        path="/tmp/hello.txt",
        data="Hello World",
        mode=644
    )
])

# 2. Read file
content = await sandbox.files.read_file("/tmp/hello.txt")
print(f"Content: {content}")

# List immediate children; search filters by a filename pattern.
entries = await sandbox.files.list_directory(DirectoryListEntry(path="/tmp", depth=1))
print([entry.path for entry in entries])

# 3. Search files
files = await sandbox.files.search(
    SearchEntry(
        path="/tmp",
        pattern="*.txt"
    )
)
for f in files:
    print(f"Found: {f.path}")

# 4. Delete file
await sandbox.files.delete_files(["/tmp/hello.txt"])
```


For binary data, pass `bytes` to `WriteEntry.data` and use `read_bytes()`; use `read_bytes_stream()` for large downloads. `read_file()` and `read_bytes()` also accept `offset` and `limit` for partial reads.


#### File operations with an explicit identity


Bind a filesystem client to a Linux UID and GID:

python

```
files = sandbox.files_with_identity(1001, 2000)
```


Both the asynchronous and synchronous Sandbox clients expose this helper.


The bound client exposes the usual file operations and shares the sandbox connection, authentication, and endpoint routing headers. The existing file client retains its default identity. Select the UID/GID separately for command execution.


This requires Linux and an Execd version that supports filesystem execution identity. Unsupported servers return an error; requests never fall back to the default filesystem routes. Keep sandbox credentials and identity selection in the trusted backend. Linux filesystem permissions apply; this feature does not create a tenant isolation boundary. See [Execd](https://open-sandbox.ai/architecture/data-plane/execd) for permission and workspace provisioning details.


### 5. Sandbox Management (Admin)


Use `SandboxManager` for administrative tasks and finding existing sandboxes.

python

```
from opensandbox.manager import SandboxManager
from opensandbox.models.sandboxes import SandboxFilter

# Create manager using async context manager
async with await SandboxManager.create(connection_config=config) as manager:

    # First page only; increase page to retrieve subsequent pages.
    sandboxes = await manager.list_sandbox_infos(
        SandboxFilter(
            states=["Running"],
            page_size=10
        )
    )

    for info in sandboxes.sandbox_infos:
        print(f"Found sandbox: {info.id}")
```


### Resource metrics


Read current sandbox resource usage with `await sandbox.get_metrics()`. This is separate from [SDK creation telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Snapshots, templates, and metadata


| Operation | Public API |
| --- | --- |
| Snapshot a sandbox | `sandbox.create_snapshot(name=...)` or `manager.create_snapshot(sandbox_id, name=...)` |
| Inspect/list/delete snapshots | `manager.get_snapshot`, `list_snapshots`, `delete_snapshot` |
| Restore a snapshot | `Sandbox.create(snapshot_id=..., connection_config=config)` |
| Manage Fsb templates | `manager.create_template`, `get_template`, `list_templates`, `delete_template` |
| Create from a published template | `Sandbox.create_from_template(template_id, timeout=..., connection_config=config)` |
| Patch metadata | `sandbox.patch_metadata` or `manager.patch_sandbox_metadata` |


These APIs also exist on the synchronous SDK. Snapshot creation and template builds are asynchronous: inspect status before restoring or using a template. Templates must reach `Succeeded`; template-backed creation requires a TTL and inherits environment, resources, volumes, and lifecycle hooks from the template. Metadata patch values add/replace keys; `None` deletes a key. See the [lifecycle contract](https://open-sandbox.ai/api/#1-sandbox-lifecycle-yml) for backend constraints.


Snapshot support depends on the runtime and server configuration. Renew the source sandbox first if its remaining TTL may expire during snapshot creation. This example waits up to 15 minutes, restores a new sandbox, and retains the snapshot for reuse:

python

```
import time
from opensandbox.manager import SandboxManager

async with await SandboxManager.create(connection_config=config) as manager:
    snapshot = await sandbox.create_snapshot(name="demo")
    print("Snapshot:", snapshot.id)
    deadline = time.monotonic() + 900
    while True:
        if time.monotonic() >= deadline:
            raise TimeoutError(f"Snapshot {snapshot.id} is not ready")
        snapshot = await manager.get_snapshot(snapshot.id)
        if snapshot.status.state == "Ready":
            break
        if snapshot.status.state == "Failed":
            raise RuntimeError(snapshot.status.message)
        await asyncio.sleep(2)
    restored = await Sandbox.create(snapshot_id=snapshot.id, connection_config=config)
    try:
        print(restored.id)
    finally:
        await restored.destroy()
    # When no longer needed: await manager.delete_snapshot(snapshot.id)
```


Create from an existing template after its build reaches `Succeeded`:

python

```
from datetime import timedelta

templated = await Sandbox.create_from_template(
    "your-published-template-id",
    timeout=timedelta(minutes=10),
    connection_config=config,
)
```


Add, replace, or remove metadata on a running sandbox:

python

```
await sandbox.patch_metadata({"project": "demo", "obsolete-key": None})
```


## Configuration


### 1. Connection Configuration


The `ConnectionConfig` class manages API server connection settings.


| Parameter | Description | Default | Environment Variable |
| --- | --- | --- | --- |
| `api_key` | API Key for authentication | Optional; needed when server auth is enabled | `OPEN_SANDBOX_API_KEY` |
| `domain` | The endpoint domain of the sandbox service | `localhost:8080` | `OPEN_SANDBOX_DOMAIN` |
| `protocol` | HTTP protocol (http/https) | `http` | - |
| `request_timeout` | Timeout for API requests | 30 seconds | - |
| `debug` | Enable debug logging for HTTP requests | `False` | - |
| `headers` | Custom HTTP headers | Empty | - |
| `follow_redirects` | Follow HTTP redirects for SDK requests | `False` | - |
| `event_hooks` | Additional httpx hooks for adapter clients | Empty | - |
| `transport` | Shared httpx transport (pool/proxy/retry); custom transports must honor request timeouts | SDK-created per instance | - |
| `retry_policy` | Automatic retry policy for non-streaming requests (see [Automatic retries](https://open-sandbox.ai/sdks/python#_2-automatic-retries)) | Enabled (`RetryPolicy()`) | - |
| `use_server_proxy` | Use sandbox server as proxy for execd/endpoint requests (e.g. when client cannot reach the sandbox directly) | `False` | - |
| `disable_metrics` | Disable SDK create-latency telemetry (see [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics)) | `False` | `OPENSANDBOX_DISABLE_METRICS` |
| `enable_tracing` | Enable OpenTelemetry tracing for pool warmup (see [SDK Tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing)) | `False` | - |


The Python Code Interpreter inherits the sandbox's connection configuration. With `use_server_proxy=True`, context requests and streamed code execution include the configured API key in `OPEN-SANDBOX-API-KEY` for server authentication. In direct mode, the SDK does not automatically attach this key to code execution requests. This applies to both the asynchronous and synchronous APIs.


When `follow_redirects` is enabled, same-origin redirects preserve request headers. An origin is the combination of scheme, host, and port, so changing any of those values is cross-origin. Before following a cross-origin redirect, the SDK removes every header whose name starts with `OPEN-SANDBOX-` or `OPENSANDBOX-` (case-insensitive). Other custom headers are not stripped automatically.


File uploads never follow redirects, even when `follow_redirects` is enabled, because streamed or file-backed multipart request bodies cannot always be safely replayed. This applies to both direct chunked uploads and uploads through the server proxy. A redirect response from an upload is surfaced as a `SandboxApiException` with the original 3xx status.


`ConnectionConfig.event_hooks` accepts async httpx hooks, while `ConnectionConfigSync.event_hooks` accepts synchronous hooks. Configured request hooks run before the SDK safety hook, so they cannot re-add protected OpenSandbox headers to a cross-origin request. Lifecycle telemetry honors `follow_redirects` and the SDK safety hook, but does not invoke configured user hooks.

python

```
from datetime import timedelta

# 1. Basic configuration
config = ConnectionConfig(
    api_key="your-key",
    domain="api.opensandbox.io",
    request_timeout=timedelta(seconds=60)
)

# 2. Advanced: Custom headers and custom transport
# If you create many Sandbox instances, configuring a shared transport is recommended to optimize resource usage.
# SDK default keep-alive is 30 seconds for its own transports.
import httpx

config = ConnectionConfig(
    api_key="your-key",
    domain="api.opensandbox.io",
    headers={
        "X-Custom-Header": "value",
        "X-Request-ID": "trace-123",
    },
    transport=httpx.AsyncHTTPTransport(
        limits=httpx.Limits(
            max_connections=100,
            max_keepalive_connections=50,
            keepalive_expiry=30.0,
        )
    ),
)

# If you provide a custom transport, you are responsible for closing it:
# await config.transport.aclose()
```


### 2. Automatic retries


The SDK retries transient failures automatically. `ConnectionConfig` / `ConnectionConfigSync` install a retry wrapper around the default shared transport, controlled by `retry_policy` (`opensandbox.transport.RetryPolicy`).


Default behavior:


- **Enabled by default.** Idempotent methods (`GET/HEAD/PUT/DELETE/OPTIONS`) are retried on `429`, `502`, `503`, and on pre-send transport failures (DNS, TCP connect, TLS handshake, fresh-connection reset).
- **`POST` / `PATCH` are never retried on a status code by default**, since the request may already have been applied server-side. Pre-send transport failures (before any byte is written) are still retried for these methods.
- Up to `3` retries with decorrelated-jitter exponential backoff, honoring a server `Retry-After` header (capped at 60s).
- **SSE / streaming requests bypass retry** entirely (bodies are not replayable).


Behavior change


Retries are on by default. This can increase the number of HTTP attempts and tail latency compared to earlier SDK versions. If you rely on fast-fail semantics, opt out explicitly with `RetryPolicy.disabled()`.

python

```
from datetime import timedelta

from opensandbox.transport import RetryPolicy

# Fast-fail: never retry (also skips fresh-connection recovery).
config = ConnectionConfig(
    api_key="your-key",
    domain="api.opensandbox.io",
    retry_policy=RetryPolicy.disabled(),
)

# Custom policy: more retries, an overall wall-clock deadline, and an
# opt-in to retry POST/PATCH on 503 (only safe if your endpoints are
# idempotent).
from http import HTTPStatus

config = ConnectionConfig(
    api_key="your-key",
    domain="api.opensandbox.io",
    retry_policy=RetryPolicy(
        max_retries=5,
        overall_deadline=timedelta(seconds=20),
        retryable_status_codes_non_idempotent=frozenset(
            {HTTPStatus.SERVICE_UNAVAILABLE}
        ),
    ),
)
```


INFO


If you pass a custom `transport`, the SDK does **not** wrap it; installing retry behavior is then your responsibility.


### 3. Sandbox Creation Configuration


The `Sandbox.create()` allows configuring the sandbox environment.


| Parameter | Description | Default |
| --- | --- | --- |
| `image` | Docker image specification | One of image or snapshot ID |
| `timeout` | Automatic termination timeout | 10 minutes |
| `entrypoint` | Container entrypoint command | `["tail", "-f", "/dev/null"]` |
| `resource` | CPU and memory limits | `{"cpu": "1", "memory": "2Gi"}` |
| `env` | Environment variables | Empty |
| `metadata` | Custom metadata tags | Empty |
| `network_policy` | Optional outbound network policy (egress) | - |
| `credential_proxy` | Optional Credential Vault proxy startup settings | - |
| `ready_timeout` | Total budget for endpoint publication and health checks | 30 seconds |
| `snapshot_id` | Restore a snapshot instead of passing `image` | - |
| `resource_requests` | Kubernetes resource requests; must not exceed limits | - |
| `lifecycle` | Pre-start and periodic hooks | - |
| `platform` | OS/architecture constraint | - |
| `volumes` | Host, PVC, or OSSFS mounts | - |
| `secure_access` | Require endpoint access credentials | `False` |
| `skip_health_check` | Skip health checks; endpoint publication is still awaited | `False` |


WARNING


Metadata keys under `opensandbox.io/` are reserved for system-managed labels and will be rejected by the server.

python

```
from datetime import timedelta

from opensandbox.models.sandboxes import NetworkPolicy, NetworkRule

sandbox = await Sandbox.create(
    "python:3.11",
    connection_config=config,
    timeout=timedelta(minutes=30),
    resource={"cpu": "2", "memory": "4Gi"},
    env={"PYTHONPATH": "/app"},
    metadata={"project": "demo"},
    network_policy=NetworkPolicy(
        defaultAction="deny",
        egress=[NetworkRule(action="allow", target="pypi.org")],
    ),
)
```


### 4. Runtime Egress Policy Updates


Runtime egress policy routing depends on the sandbox origin. For image-backed sandboxes, the SDK resolves port `18080` and calls the sidecar `/policy` API. For template-backed sandboxes (including restored template snapshots), the SDK detects `OPEN-SANDBOX-ORIGIN: template` and routes policy operations through the lifecycle `/sandboxes/{sandboxId}/networkpolicy` API.


Patch uses merge semantics:


- Incoming rules take priority over existing rules with the same `target`.
- Existing rules for other targets remain unchanged.
- Within a single patch payload, the first rule for a `target` wins.
- The current `defaultAction` is preserved.

python

```
from opensandbox.models.sandboxes import NetworkRule

policy = await sandbox.get_egress_policy()

await sandbox.patch_egress_rules(
    [
        NetworkRule(action="allow", target="www.github.com"),
        NetworkRule(action="deny", target="pypi.org"),
    ]
)
```


### 5. Credential Vault


Credential Vault requires a sandbox-side egress service and is unavailable for template-backed sandboxes. It injects outbound credentials from the egress sidecar while keeping real secrets out of sandbox environment variables, commands, files, and logs. Create the sandbox with `credential_proxy` enabled, then write credentials and bindings through `sandbox.credential_vault`.

python

```
from opensandbox.models.sandboxes import (
    Credential,
    CredentialBinding,
    CredentialProxyConfig,
    NetworkPolicy,
    NetworkRule,
)

sandbox = await Sandbox.create(
    "python:3.11",
    connection_config=config,
    network_policy=NetworkPolicy(
        defaultAction="deny",
        egress=[NetworkRule(action="allow", target="api.example.com")],
    ),
    credential_proxy=CredentialProxyConfig(enabled=True),
)

await sandbox.credential_vault.create(
    credentials=[Credential(name="api-token", source={"value": "<token>"})],
    bindings=[
        CredentialBinding(
            name="api-token",
            match={
                "schemes": ["https"],
                "hosts": ["api.example.com"],
                "paths": ["/v1/*"],
            },
            auth={"type": "apiKey", "name": "x-api-key", "credential": "api-token"},
        )
    ],
)
```


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for auth types, binding guidance, and Git/curl examples.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/python.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/code-interpreter`

Return to top

# Code Interpreter Sandbox
## Getting Code Interpreter image ​
## Start OpenSandbox server [local] ​
## Create and access the Code Interpreter Sandbox ​
## Environment variables ​
## Example output ​
## Code Interpreter Sandbox from pool ​
## References ​









Complete demonstration of running Python code using the Code Interpreter SDK.


## Getting Code Interpreter image


Image Source


The container image source and environment definitions are maintained in [opensandbox-group/sandbox-images](https://github.com/opensandbox-group/sandbox-images).


Pull the prebuilt image from a registry:

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use docker hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


## Start OpenSandbox server [local]


Start the local OpenSandbox server:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and access the Code Interpreter Sandbox

shell

```
# Install OpenSandbox packages
uv pip install opensandbox opensandbox-code-interpreter

# Run the example (requires SANDBOX_DOMAIN / SANDBOX_API_KEY)
uv run python examples/code-interpreter/main.py
```


The script creates a Sandbox + CodeInterpreter, runs a Python code snippet and prints stdout/result, then terminates the remote instance. Cleanup is attempted in a `finally` block even if interpreter setup or code execution raises an exception.


## Environment variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |


## Example output

text

```
=== Python example ===
[Python stdout] Hello from Python!

[Python result] {'py': '3.14.2', 'sum': 4}

=== Java example ===
[Java stdout] Hello from Java!

[Java stdout] 2 + 3 = 5

[Java result] 5

=== Go example ===
[Go stdout] Hello from Go!
3 + 4 = 7


=== TypeScript example ===
[TypeScript stdout] Hello from TypeScript!

[TypeScript stdout] sum = 6
```


## Code Interpreter Sandbox from pool


### Start OpenSandbox server [k8s]


Install the k8s OpenSandbox operator, and create a pool:

yaml

```
apiVersion: sandbox.opensandbox.io/v1alpha1
kind: Pool
metadata:
  labels:
    app.kubernetes.io/name: sandbox-k8s
    app.kubernetes.io/managed-by: kustomize
  name: pool-sample
  namespace: opensandbox
spec:
  template:
    metadata:
      labels:
        app: example
    spec:
      volumes:
        - name: sandbox-storage
          emptyDir: { }
        - name: opensandbox-bin
          emptyDir: { }
      initContainers:
        - name: task-executor-installer
          image: sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/task-executor:v0.1.0
          command: [ "/bin/sh", "-c" ]
          args:
            - |
              cp /workspace/server /opt/opensandbox/task-executor &&
              chmod +x /opt/opensandbox/task-executor
          volumeMounts:
            - name: opensandbox-bin
              mountPath: /opt/opensandbox
        - name: execd-installer
          image: sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/execd:v1.1.0
          command: [ "/bin/sh", "-c" ]
          args:
            - |
              cp ./execd /opt/opensandbox/execd &&
              cp ./bootstrap.sh /opt/opensandbox/bootstrap.sh &&
              chmod +x /opt/opensandbox/execd &&
              chmod +x /opt/opensandbox/bootstrap.sh
          volumeMounts:
            - name: opensandbox-bin
              mountPath: /opt/opensandbox
      containers:
        - name: sandbox
          image: sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0
          command:
          - "/bin/sh"
          - "-c"
          - |
            /opt/opensandbox/task-executor \
              -listen-addr=0.0.0.0:5758 \
              -log-dir=/tmp
          env:
          - name: SANDBOX_MAIN_CONTAINER
            value: main
          - name: EXECD_ENVS
            value: /opt/opensandbox/.env
          - name: EXECD
            value: /opt/opensandbox/execd
          volumeMounts:
            - name: sandbox-storage
              mountPath: /var/lib/sandbox
            - name: opensandbox-bin
              mountPath: /opt/opensandbox
      tolerations:
        - operator: "Exists"
  capacitySpec:
    bufferMax: 3
    bufferMin: 1
    poolMax: 5
    poolMin: 0
```


#### How Pool entrypoint injection works


The lifecycle API allocates an already-running Pod from the Pool, so it does not replace that Pod's `command`, `args`, or `env`. When a create request supplies an `entrypoint` or environment variables, the server records them in `BatchSandbox.spec.taskTemplate`. The controller then sends the task to the allocated Pod's IP on port `5758`.


The Pool template must provide all parts of that execution path:


- Install and run task-executor, listening on `0.0.0.0:5758`. Set its `-log-dir` explicitly so the troubleshooting path is deterministic; the example writes `/tmp/task-executor.log`.
- Install execd and `bootstrap.sh` into the shared volume before the Pod starts.
- Keep `bootstrap.sh` at `/opt/opensandbox/bootstrap.sh`. The server-generated task invokes that exact path. The execd binary can use another path only when the task-executor environment sets `EXECD` accordingly.
- Start execd through `bootstrap.sh` after allocation so request-specific values such as `EXECD_ACCESS_TOKEN` are available. The example above leaves task-executor as the warm Pod's foreground process for this reason.


The Pod YAML continuing to show the Pool template is therefore expected. Inspect the `BatchSandbox` resource and task-executor instead:

shell

```
# Confirm that the server injected the requested process and environment.
kubectl get batchsandbox <sandbox-name> -n <namespace> \
  -o jsonpath='{.spec.taskTemplate}{"\n"}'

# Find the allocated Pod. The annotation value contains a JSON `pods` array.
kubectl get batchsandbox <sandbox-name> -n <namespace> \
  -o jsonpath='{.metadata.annotations.sandbox\.opensandbox\.io/alloc-status}{"\n"}'

# Replace <pool-pod> with the first Pod name from that array.
kubectl exec <pool-pod> -n <namespace> -- \
  sh -c 'test -x /opt/opensandbox/task-executor && test -x /opt/opensandbox/bootstrap.sh'
kubectl exec <pool-pod> -n <namespace> -- \
  tail -n 100 /tmp/task-executor.log

# Check the executor health endpoint from a second terminal while this runs.
kubectl port-forward pod/<pool-pod> -n <namespace> 5758:5758
curl http://127.0.0.1:5758/health
curl http://127.0.0.1:5758/getTasks

# The lifecycle server uses <sandbox-name>-0 as the task name. Check the task's
# captured output (adjust the path if task-executor uses a custom data directory).
kubectl exec <pool-pod> -n <namespace> -- \
  sh -c 'tail -n 100 /var/lib/sandbox/tasks/<sandbox-name>-0/stdout.log; tail -n 100 /var/lib/sandbox/tasks/<sandbox-name>-0/stderr.log'

# Check controller logs for delivery failures between the controller and port 5758.
kubectl logs -n opensandbox-system -l control-plane=controller-manager --tail=100
```


If `taskTemplate` exists but the health check cannot reach port `5758`, verify that task-executor is installed and remains running. The generated task intentionally starts `bootstrap.sh` in the background, so its wrapper can report success even when `bootstrap.sh` is missing or the requested entrypoint later fails. Do not rely on `taskFailed` or `taskLastErrorMessage` alone for these failures; inspect the task's captured `stderr.log` and `stdout.log`, then verify the execd or application process directly.


Start the k8s OpenSandbox server:

shell

```
uv pip install opensandbox-server

# replace with your k8s cluster config, kubeconfig etc.
opensandbox-server init-config ~/.sandbox.toml --example k8s
curl -o ~/batchsandbox-template.yaml https://raw.githubusercontent.com/opensandbox-group/OpenSandbox/main/server/opensandbox_server/examples/example.batchsandbox-template.yaml

opensandbox-server
```


### Create and access the Code Interpreter Sandbox (pool)

shell

```
# Install OpenSandbox packages
uv pip install opensandbox opensandbox-code-interpreter

# Run the example (requires SANDBOX_DOMAIN / SANDBOX_API_KEY)
uv run python examples/code-interpreter/main_use_pool.py
```


### Pool example output

text

```
=== Verify Environment Variable ===
[ENV Check] TEST_ENV value: test

[ENV Result] 'test'

=== Java example ===
[Java stdout] Hello from Java!

[Java stdout] 2 + 3 = 5

[Java result] 5

=== Go example ===
[Go stdout] Hello from Go!
3 + 4 = 7


=== TypeScript example ===
[TypeScript stdout] Hello from TypeScript!

[TypeScript stdout] sum = 6
```


## References


- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/code-interpreter)
- [Code Interpreter Image Repository](https://github.com/opensandbox-group/sandbox-images)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/code-interpreter.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/getting-started/installation`

# Installation


## Server
## Server ​
*See Configuration for server setup.*

## SDKs ​
*For detailed SDK usage, see the SDK documentation.*

## CLI ​
*The osb CLI provides terminal-based sandbox management.*

*See the CLI reference for the full command set.*

## MCP Server ​






The OpenSandbox server is a FastAPI-based service that manages sandbox lifecycles. It supports Docker and Kubernetes runtimes.

pip uv bash

```
pip install opensandbox-server
```

bash

```
uv pip install opensandbox-server
```


**Requirements:**


- Python 3.10+
- Docker Engine 20.10+ (Docker runtime) or Kubernetes 1.21.1+ (Kubernetes runtime)
- Linux, macOS, or Windows with WSL2


See [Configuration](https://open-sandbox.ai/getting-started/configuration) for server setup.


## SDKs


### Sandbox SDKs


The core SDKs for sandbox lifecycle management, command execution, and file operations.

Python JavaScript/TypeScript Kotlin/Java (Gradle) Kotlin/Java (Maven) Go C#/.NET bash

```
pip install opensandbox
```

bash

```
npm install @alibaba-group/opensandbox
```

kotlin

```
dependencies {
    implementation(platform("com.alibaba.opensandbox:sandbox-bom:{latest_version}"))
    implementation("com.alibaba.opensandbox:sandbox")
}
```

xml

```
<dependency>
    <groupId>com.alibaba.opensandbox</groupId>
    <artifactId>sandbox</artifactId>
    <version>{latest_version}</version>
</dependency>
```

bash

```
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```

bash

```
dotnet add package Alibaba.OpenSandbox
```


For detailed SDK usage, see the [SDK documentation](https://open-sandbox.ai/sdks/).


Choose a published SDK version for your application. Replace `{latest_version}` in the JVM examples with that version; use the BOM when combining JVM modules such as `sandbox` and `sandbox-pool-redis`. See the [release index](https://github.com/opensandbox-group/OpenSandbox/releases).


Feature availability differs by language. See the [capability matrix](https://open-sandbox.ai/sdks/#capability-coverage), [Client Pool](https://open-sandbox.ai/guides/client-pool), and [SDK Tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing).


## CLI


The `osb` CLI provides terminal-based sandbox management.

pip uv bash

```
pip install opensandbox-cli
```

bash

```
uv tool install opensandbox-cli
```


See the [CLI reference](https://open-sandbox.ai/cli/) for the full command set.


## MCP Server


The MCP server exposes sandbox operations to MCP-capable clients like Claude Code and Cursor.

pip uv bash

```
pip install opensandbox-mcp
```

bash

```
uv pip install opensandbox-mcp
```

bash

```
opensandbox-mcp --domain localhost:8080 --protocol http
```


Minimal stdio config for MCP clients:

json

```
{
  "mcpServers": {
    "opensandbox": {
      "command": "opensandbox-mcp",
      "args": ["--domain", "localhost:8080", "--protocol", "http"]
    }
  }
}
```


See the [MCP documentation](https://open-sandbox.ai/sdks/mcp) for client-specific setup.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/getting-started/installation.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/javascript`

# OpenSandbox SDK for JavaScript/TypeScript
## Installation ​
## Quick Start ​
## Lifecycle Hooks ​
## Client Pool and observability ​
## Usage Examples ​
*Create a non-expiring sandbox by passing timeoutSeconds: null:*

*Use SandboxManager for administrative tasks and finding existing sandboxes.*

## Snapshots, templates, and metadata ​
*Use an existing template after its build reaches Succeeded:*

## Configuration ​
*The ConnectionConfig class manages API server connection settings.*

*Sandbox.create() allows configuring the sandbox environment.*

*See Credential Vault for auth types, binding guidance, and Git/curl examples.*

## Browser Notes ​










A TypeScript/JavaScript SDK for low-level interaction with OpenSandbox. It provides the ability to create, manage, and interact with secure sandbox environments, including executing shell commands, managing files, and reading resource metrics.


## Installation


### npm

bash

```
npm install @alibaba-group/opensandbox
```


### pnpm

bash

```
pnpm add @alibaba-group/opensandbox
```


### yarn

bash

```
yarn add @alibaba-group/opensandbox
```


## Quick Start


This example uses Node.js 20+ with ES modules and top-level `await`. It creates a sandbox, runs a shell command, and releases both remote and local resources.


TIP


Before running this example, ensure the OpenSandbox service is running. See the [Getting Started](https://open-sandbox.ai/getting-started/) guide for startup instructions.

ts

```
import { ConnectionConfig, Sandbox, SandboxException } from "@alibaba-group/opensandbox";

const config = new ConnectionConfig({
  domain: "api.opensandbox.io",
  apiKey: "your-api-key",
  // protocol: "https",
  // requestTimeoutSeconds: 60,
});

try {
  const sandbox = await Sandbox.create({
    connectionConfig: config,
    image: "ubuntu",
    timeoutSeconds: 10 * 60,
  });

  try {
    const execution = await sandbox.commands.run("echo 'Hello Sandbox!'");
    console.log(execution.logs.stdout[0]?.text);
  } finally {
    try {
      await sandbox.kill();
    } finally {
      await sandbox.close();
    }
  }
} catch (err) {
  if (err instanceof SandboxException) {
    console.error(
      `Sandbox Error: [${err.error.code}] ${err.error.message ?? ""}`,
    );
    console.error(`Request ID: ${err.requestId ?? "N/A"}`);
  } else {
    console.error(err);
  }
}
```


## Lifecycle Hooks


Set `lifecycle` in `Sandbox.create`. `preStart` completes before the entrypoint starts, while `periodic` hooks run on their schedules after startup.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "ubuntu:24.04",
  lifecycle: {
    preStart: {
      command: ["sh", "-c", "echo ready > /tmp/prestart.done"],
      timeoutSeconds: 120,
    },
    periodic: [
      {
        name: "checkpoint",
        schedule: "@every 5m",
        command: ["sh", "-c", "date -u >> /tmp/checkpoints.log"],
        timeoutSeconds: 120,
      },
    ],
  },
});
```


The Server validates `timeoutSeconds`; `preStart` accepts 1–10800 seconds, while `periodic` accepts 1–300 seconds. Both default to 60 seconds when omitted. See [Lifecycle Hooks](https://open-sandbox.ai/guides/lifecycle-hooks) for timing, failure behavior, and provider limitations.


### Idle policy (auto-pause and wake-on-access)


`lifecycle.idlePolicy` (OSEP-0024, fast-sandbox only) tells the control plane to auto-pause the sandbox after `idleTimeoutSeconds` (30–86400) of continuously idle ingress-observed traffic, and to wake it on the next request. It is control-plane state: it never reaches the guest, is allowed in template mode (`Sandbox.createFromTemplate({ idlePolicy })`), and is rejected by non-fast-sandbox backends. Omitting it preserves non-automated behavior exactly.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "ubuntu:24.04",
  timeoutSeconds: 86400,
  lifecycle: {
    idlePolicy: {
      idleTimeoutSeconds: 300,
      onIdle: "pause",
      wakeOnAccess: true,
    },
  },
});
```


`activeProbe` lets the application veto a pause while real work runs without producing ingress traffic: declare an endpoint answering `{"active": bool, "message"?: string}` and the server polls it when the sandbox is otherwise idle; a busy answer resets the idle clock.


### Wake retry


A request to a paused sandbox may arrive while its restore is still in progress. The gateway answers `503` with the `OpenSandbox-Wake: expired` header; the transport recognizes it and resends the original request after the `Retry-After` delay (safe for any method — the marker proves the request was never forwarded). The wake budget defaults to 5 attempts / 60 seconds across all wake cycles; when it is exhausted the SDK throws `SandboxWakeTimeoutException` (carrying `attempts` and `waitedMs`) while the server-side resume continues in the background. Bare `503` responses follow the existing rules untouched. Tune it on the connection config: `wakeRetryEnabled` (default true), `wakeMaxAttempts` (5), `wakeOverallDeadlineSeconds` (60, `null` for unbounded). The SSE transport is wrapped too, so `commands.run()` wakes a paused sandbox like any other request (an established stream is never re-dispatched — only the marked 503 connect replays); the upload transport stays bare because upload bodies are streams and cannot be replayed.


## Client Pool and observability


`SandboxPool` provides in-memory and Redis-backed stores, four acquire policies, and staged warmup controls. The Redis store is exported from `@alibaba-group/opensandbox/pool-redis`. See [Client Pool](https://open-sandbox.ai/guides/client-pool) for examples, configuration, and namespace retirement.


Set `enableTracing: true` in `ConnectionConfig` to enable [pool warmup tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing). JavaScript emits phase spans but fewer diagnostic attributes than Python/JVM. Create-latency [telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics) has a separate opt-out setting. Remote diagnostic logs/events are available through [CLI or HTTP](https://open-sandbox.ai/api/#diagnostics), not through the JavaScript SDK.


## Usage Examples


The snippets below use `config` and a live `sandbox` from the quick start. Run them before its cleanup block. Examples use TypeScript with top-level `await` in Node.js; omit type annotations in JavaScript. Creation examples are alternatives. Terminate each sandbox with `kill()` and release its client with `close()` when done.


### 1. Lifecycle Management


Manage the sandbox lifecycle, including renewal, pausing, and resuming.

ts

```
const info = await sandbox.getInfo();
console.log("State:", info.status.state);
console.log("Created:", info.createdAt);
console.log("Expires:", info.expiresAt); // null when manual cleanup mode is used

await sandbox.pause();

const deadline = Date.now() + 120_000;
while (true) {
  if (Date.now() >= deadline) throw new Error("Sandbox did not pause within 120 seconds");
  const current = await sandbox.getInfo();
  if (current.status.state === "Paused") break;
  if (current.status.state === "Failed") throw new Error(current.status.message);
  await new Promise((resolve) => setTimeout(resolve, 1000));
}

// Resume returns a fresh handle; close both handles when done.
const resumed = await sandbox.resume();
try {
  await resumed.renew(30 * 60); // expiresAt = now + timeoutSeconds
} finally {
  await resumed.close();
}
```


Pause is asynchronous and runtime-dependent. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume). Attach to an already running sandbox with `Sandbox.connect({ sandboxId, connectionConfig: config })`.


Create a non-expiring sandbox by passing `timeoutSeconds: null`:

ts

```
const manual = await Sandbox.create({
  connectionConfig: config,
  image: "ubuntu",
  timeoutSeconds: null,
});
```


### 2. Custom Health Check


Resolving an endpoint confirms that a route exists; it does not confirm that the application on that port is healthy. For service readiness, make a bounded request to the application's health endpoint and include the returned endpoint headers.


Define custom logic to determine whether the sandbox is ready/healthy. This overrides the default ping check. Checks must not block the event loop and may continue running after timeout.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "nginx:latest",
  entrypoint: ["nginx", "-g", "daemon off;"],
  healthCheck: async (sbx) => {
    const ep = await sbx.getEndpoint(80);
    const url = await sbx.getEndpointUrl(80);
    try {
      const response = await fetch(url, {
        headers: ep.headers,
        signal: AbortSignal.timeout(2000),
      });
      await response.body?.cancel();
      return response.status === 200;
    } catch {
      return false;
    }
  },
});
```


### 3. Command Execution & Streaming


Execute commands and handle output streams in real-time.

ts

```
import type { ExecutionHandlers } from "@alibaba-group/opensandbox";

const handlers: ExecutionHandlers = {
  onStdout: (m) => console.log("STDOUT:", m.text),
  onStderr: (m) => console.error("STDERR:", m.text),
  onExecutionComplete: (c) =>
    console.log("Finished in", c.executionTimeMs, "ms"),
};

await sandbox.commands.run(
  'for i in 1 2 3; do echo "Count $i"; sleep 0.2; done',
  undefined,
  handlers,
);
```


To execute a native program without shell parsing, pass an argument list. On Linux, this example prints literal `$HOME` and keeps `hello world` as one argument:

ts

```
await sandbox.commands.run(["printf", "%s\n", "$HOME", "hello world"]);
```


Native argv execution requires an updated execd. See [command execution modes](https://open-sandbox.ai/architecture/data-plane/execd#command-execution) for executable lookup and platform behavior.


#### Background commands


Poll status and incremental logs. The command timeout is separate from sandbox TTL.

ts

```
const execution = await sandbox.commands.run(
  'for i in 1 2 3; do echo "step $i"; sleep 1; done',
  { background: true, timeoutSeconds: 30 },
);
if (!execution.id) throw new Error("No command ID returned");
let cursor = 0;
const deadline = Date.now() + 45_000;
while (true) {
  if (Date.now() >= deadline) {
    await sandbox.commands.interrupt(execution.id);
    throw new Error("Command did not finish");
  }
  const status = await sandbox.commands.getCommandStatus(execution.id);
  const logs = await sandbox.commands.getBackgroundCommandLogs(execution.id, cursor);
  process.stdout.write(logs.content);
  cursor = logs.cursor ?? cursor;
  if (status.running === false) {
    if (status.exitCode !== 0) throw new Error(`Command failed: ${status.exitCode}, ${status.error}`);
    break;
  }
  await new Promise((resolve) => setTimeout(resolve, 500));
}
```


#### Persistent shell sessions


A Bash session preserves shell variables and the working directory across commands.

ts

```
const sessionId = await sandbox.commands.createSession({ workingDirectory: "/tmp" });
try {
  await sandbox.commands.runInSession(sessionId, "export DEMO=hello");
  const result = await sandbox.commands.runInSession(sessionId, 'echo "$DEMO"; pwd');
  console.log(result.logs.stdout.map((message) => message.text).join(""));
} finally {
  await sandbox.commands.deleteSession(sessionId);
}
```


#### Persistent environment variables


Set environment variables that the runtime injects into every subsequent command and session — without hand-writing shell escaping against the sandbox env file.

ts

```
await sandbox.commands.setEnv("MY_TOKEN", "it's a safe value");
```


Keys must match `[A-Za-z_][A-Za-z0-9_]*`. Values without a single quote are stored verbatim; values containing a single quote use the env file's double-quoted form, in which shell-style `$NAME` sequences may be expanded when the runtime loads the file. The env file is append-only: the last write for a key wins. Throws if the sandbox fails to persist the variable.


For filesystem/process isolation within a sandbox, see [Isolation Sessions](https://open-sandbox.ai/guides/isolation-sessions). These are separate from Bash sessions.


### 4. File Operations


Manage files and directories, including read, write, list/search, and delete.

ts

```
await sandbox.files.createDirectories([{ path: "/tmp/demo", mode: 755 }]);

await sandbox.files.writeFiles([
  { path: "/tmp/demo/hello.txt", data: "Hello World", mode: 644 },
]);

const content = await sandbox.files.readFile("/tmp/demo/hello.txt");
console.log("Content:", content);

const entries = await sandbox.files.listDirectory({ path: "/tmp/demo", depth: 1 });
console.log(entries.map((entry) => entry.path));

const files = await sandbox.files.search({
  path: "/tmp/demo",
  pattern: "*.txt",
});
console.log(files.map((f) => f.path));

await sandbox.files.deleteDirectories(["/tmp/demo"]);
```


For binary files, pass a `Uint8Array` to `writeFiles()` and read with `readBytes()` or `readBytesStream()`. Read options support `offset` and `limit` for partial downloads.


#### File operations with an explicit identity


Bind a filesystem client to a Linux UID and GID:

ts

```
const files = sandbox.filesWithIdentity(1001, 2000);
```


The bound client exposes the usual file operations and shares the sandbox connection, authentication, and endpoint routing headers. The existing file client retains its default identity. Select the UID/GID separately for command execution.


This requires Linux and an Execd version that supports filesystem execution identity. Unsupported servers return an error; requests never fall back to the default filesystem routes. Keep sandbox credentials and identity selection in the trusted backend. Linux filesystem permissions apply; this feature does not create a tenant isolation boundary. See [Execd](https://open-sandbox.ai/architecture/data-plane/execd) for permission and workspace provisioning details.


### 5. Endpoints


`getEndpoint()` returns an endpoint **without a scheme** (for example `"localhost:44772"`). Use `getEndpointUrl()` if you want a ready-to-use absolute URL (for example `"http://localhost:44772"`).

ts

```
const endpoint = await sandbox.getEndpoint(44772);
const url = await sandbox.getEndpointUrl(44772);
console.log(url, Object.keys(endpoint.headers ?? {}));
```


When making an HTTP request to a sandbox service, forward `endpoint.headers`, including credentials required by secure access. The health-check example above shows a request to an application that is actually listening on the target port.


### 6. Volume Mounts


`volumes` supports `host`, `pvc`, and `ossfs` backends. Each volume must specify exactly one backend.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "ubuntu",
  volumes: [
    {
      name: "oss-data",
      ossfs: {
        bucket: "bucket-a",
        endpoint: "oss-cn-hangzhou.aliyuncs.com",
        accessKeyId: process.env.OSS_ACCESS_KEY_ID!,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET!,
        version: "2.0",
      },
      mountPath: "/mnt/oss",
      subPath: "prefix",
    },
  ],
});
```


### 7. Sandbox Management (Admin)


Use `SandboxManager` for administrative tasks and finding existing sandboxes.

ts

```
import { SandboxManager } from "@alibaba-group/opensandbox";

const manager = SandboxManager.create({ connectionConfig: config });
try {
  // First page only; increase page for subsequent pages.
  const list = await manager.listSandboxInfos({
    states: ["Running"], pageSize: 10, page: 1,
  });
  console.log(list.items.map((s) => s.id));
} finally {
  await manager.close();
}
```


### Resource metrics


Read current sandbox resource usage with `await sandbox.getMetrics()`. This is separate from [SDK creation telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Snapshots, templates, and metadata


| Operation | Public API |
| --- | --- |
| Snapshot a sandbox | `manager.createSnapshot(sandboxId, { name })` |
| Inspect/list/delete snapshots | `manager.getSnapshot`, `listSnapshots`, `deleteSnapshot` |
| Restore a snapshot | `Sandbox.create({ snapshotId, connectionConfig })` |
| Manage Fsb templates | `manager.createTemplate`, `getTemplate`, `listTemplates`, `deleteTemplate` |
| Create from a published template | `Sandbox.createFromTemplate({ templateId, timeoutSeconds, connectionConfig })` |
| Patch metadata | `sandbox.patchMetadata` or `manager.patchSandboxMetadata` |


Poll snapshot status before restoring. Template builds are asynchronous; wait for `status.phase === "Succeeded"` before use. Template-backed creation requires a TTL and inherits workload configuration from the published template. Metadata patch values add/replace keys; `null` deletes a key. See the [lifecycle contract](https://open-sandbox.ai/api/#1-sandbox-lifecycle-yml) for backend constraints.


Snapshot support depends on the runtime and server configuration. Renew the source sandbox first if its remaining TTL may expire during snapshot creation. Wait for `Ready` before restoring; the snapshot remains available after this example:

ts

```
import { SandboxManager } from "@alibaba-group/opensandbox";

const manager = SandboxManager.create({ connectionConfig: config });
try {
  let snapshot = await manager.createSnapshot(sandbox.id, { name: "demo" });
  console.log("Snapshot:", snapshot.id);
  const deadline = Date.now() + 900_000;
  while (true) {
    if (Date.now() >= deadline) throw new Error(`Snapshot ${snapshot.id} is not ready`);
    snapshot = await manager.getSnapshot(snapshot.id);
    if (snapshot.status.state === "Ready") break;
    if (snapshot.status.state === "Failed") throw new Error(snapshot.status.message);
    await new Promise((resolve) => setTimeout(resolve, 2000));
  }
  const restored = await Sandbox.create({ snapshotId: snapshot.id, connectionConfig: config });
  try {
    console.log(restored.id);
  } finally {
    try { await restored.kill(); } finally { await restored.close(); }
  }
  // When no longer needed: await manager.deleteSnapshot(snapshot.id);
} finally {
  await manager.close();
}
```


Use an existing template after its build reaches `Succeeded`:

ts

```
const templated = await Sandbox.createFromTemplate({
  templateId: "your-published-template-id",
  timeoutSeconds: 600,
  connectionConfig: config,
});
```


Add/replace a metadata key and remove another:

ts

```
await sandbox.patchMetadata({ project: "demo", "obsolete-key": null });
```


## Configuration


### 1. Connection Configuration


The `ConnectionConfig` class manages API server connection settings.


Runtime Notes


- In browsers, the SDK uses the global `fetch` implementation.
- `requestTimeoutSeconds` bounds the wait for a response: it stops applying once the response headers arrive (streaming responses are not cut off). It never caps a healthy file upload body, which can legitimately take longer than the timeout; on Node.js a stalled upload, or an upload that gets no response headers within the timeout once the body has been sent, is aborted instead of hanging (the Go SDK's `ResponseHeaderTimeout` contract).
- In Node.js, every `Sandbox` and `SandboxManager` clones the base `ConnectionConfig` via `withTransportIfMissing()`, so each instance gets an isolated `undici` keep-alive pool. Call `sandbox.close()` or `manager.close()` when you are done so the SDK can release the associated agent.


| Parameter | Description | Default | Environment Variable |
| --- | --- | --- | --- |
| `apiKey` | API key for authentication | Optional | `OPEN_SANDBOX_API_KEY` |
| `domain` | Sandbox service domain (`host[:port]`) | `localhost:8080` | `OPEN_SANDBOX_DOMAIN` |
| `protocol` | HTTP protocol (`http` / `https`) | `http` | - |
| `requestTimeoutSeconds` | Request timeout applied to SDK HTTP calls | `30` | - |
| `debug` | Enable basic HTTP debug logging | `false` | - |
| `headers` | Extra headers applied to every request | `{}` | - |
| `useServerProxy` | Use sandbox server as proxy for execd/endpoint requests (e.g. when client cannot reach the sandbox directly) | `false` | - |
| `enableTracing` | Enable [pool warmup tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing) | `false` | - |
| `disableMetrics` | Disable SDK create-latency telemetry (see [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics)) | `false` | `OPENSANDBOX_DISABLE_METRICS` |

ts

```
import { ConnectionConfig } from "@alibaba-group/opensandbox";

// 1. Basic configuration
const config = new ConnectionConfig({
  domain: "api.opensandbox.io",
  apiKey: "your-key",
  requestTimeoutSeconds: 60,
});

// 2. Advanced: custom headers
const config2 = new ConnectionConfig({
  domain: "api.opensandbox.io",
  apiKey: "your-key",
  headers: { "X-Custom-Header": "value" },
});
```


### 2. Sandbox Creation Configuration


`Sandbox.create()` allows configuring the sandbox environment.


| Parameter | Description | Default |
| --- | --- | --- |
| `image` | Docker image to use | One of image or snapshot ID |
| `timeoutSeconds` | Automatic termination timeout (server-side TTL) | 10 minutes |
| `entrypoint` | Container entrypoint command | `["tail","-f","/dev/null"]` |
| `resource` | CPU and memory limits (string map) | `{"cpu":"1","memory":"2Gi"}` |
| `env` | Environment variables | `{}` |
| `metadata` | Custom metadata tags | `{}` |
| `networkPolicy` | Optional outbound network policy (egress) | - |
| `credentialProxy` | Optional Credential Vault proxy startup settings | - |
| `extensions` | Extra server-defined fields | `{}` |
| `skipHealthCheck` | Skip readiness checks (`Running` + health check) | `false` |
| `healthCheck` | Custom readiness check | - |
| `readyTimeoutSeconds` | Max time to wait for readiness | 30 seconds |
| `healthCheckPollingInterval` | Poll interval while waiting (milliseconds) | 200 ms |
| `snapshotId` | Restore a snapshot instead of passing `image` | - |
| `resourceRequests` | Kubernetes resource requests; must not exceed limits | - |
| `lifecycle` | Pre-start and periodic hooks | - |
| `platform` | OS/architecture constraint | - |
| `volumes` | Host, PVC, or OSSFS mounts | - |
| `secureAccess` | Require endpoint access credentials | `false` |


WARNING


Metadata keys under `opensandbox.io/` are reserved for system-managed labels and will be rejected by the server.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "python:3.11",
  networkPolicy: {
    defaultAction: "deny",
    egress: [{ action: "allow", target: "pypi.org" }],
  },
});
```


### 3. Runtime Egress Policy Updates


Runtime egress policy routing depends on the sandbox origin. For image-backed sandboxes, the SDK resolves port `18080` and calls the sidecar `/policy` API. For template-backed sandboxes (including restored template snapshots), the SDK detects `OPEN-SANDBOX-ORIGIN: template` and routes policy operations through the lifecycle `/sandboxes/{sandboxId}/networkpolicy` API.


Patch uses merge semantics:


- Incoming rules take priority over existing rules with the same `target`.
- Existing rules for other targets remain unchanged.
- Within a single patch payload, the first rule for a `target` wins.
- The current `defaultAction` is preserved.

ts

```
const policy = await sandbox.getEgressPolicy();

await sandbox.patchEgressRules([
  { action: "allow", target: "www.github.com" },
  { action: "deny", target: "pypi.org" },
]);
```


### 4. Credential Vault


Credential Vault requires a sandbox-side egress service and is unavailable for template-backed sandboxes. It injects outbound credentials from the egress sidecar while keeping real secrets out of sandbox environment variables, commands, files, and logs. Create the sandbox with `credentialProxy` enabled, then write credentials and bindings through `sandbox.credentialVault`.

ts

```
const sandbox = await Sandbox.create({
  connectionConfig: config,
  image: "python:3.11",
  networkPolicy: {
    defaultAction: "deny",
    egress: [{ action: "allow", target: "api.example.com" }],
  },
  credentialProxy: { enabled: true },
});

await sandbox.credentialVault.create({
  credentials: [{ name: "api-token", source: { value: "<token>" } }],
  bindings: [
    {
      name: "api-token",
      match: {
        schemes: ["https"],
        hosts: ["api.example.com"],
        paths: ["/v1/*"],
      },
      auth: { type: "apiKey", name: "x-api-key", credential: "api-token" },
    },
  ],
});
```


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for auth types, binding guidance, and Git/curl examples.


### 5. Resource Cleanup


Both `Sandbox` and `SandboxManager` own a scoped HTTP agent when running on Node.js so you can safely reuse the same `ConnectionConfig`. Once you are finished interacting with the sandbox or administration APIs, call `sandbox.close()` / `manager.close()` to release the underlying agent.


## Browser Notes


WARNING


- The SDK can run in browsers, but **streaming file uploads are Node-only**.
- If you pass `ReadableStream` or `AsyncIterable` for `writeFiles`, the browser will fall back to **buffering in memory** before upload.
- Reason: browsers do not support streaming `multipart/form-data` bodies with custom boundaries (required by the execd upload API).[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/javascript.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/kotlin`

# OpenSandbox SDK for Kotlin/Java
## Installation ​
## Quick Start ​
## Lifecycle Hooks ​
## Usage Examples ​
*Create a non-expiring sandbox by passing timeout(null):*

*Use SandboxManager for administrative tasks and finding existing sandboxes.*

## Snapshots and metadata ​
## Configuration ​
*The ConnectionConfig class manages API server connection settings.*

*The Sandbox.builder() allows configuring the sandbox environment.*

*See Credential Vault for auth types, binding guidance, and Git/curl examples.*

## Fsb Template Management ​









Create sandboxes, run commands, and manage files from Java or Kotlin. Both languages use the same JVM SDK and synchronous APIs.


## Installation


### Gradle (Kotlin DSL)

kotlin

```
dependencies {
    implementation("com.alibaba.opensandbox:sandbox:{latest_version}")
}
```


### Maven

xml

```
<dependency>
    <groupId>com.alibaba.opensandbox</groupId>
    <artifactId>sandbox</artifactId>
    <version>{latest_version}</version>
</dependency>
```


## Quick Start


The Java examples use Java 11+. The quick start creates a sandbox, runs a shell command, and releases both remote and local resources.


TIP


Before running this example, ensure the OpenSandbox service is running. See the [Getting Started](https://open-sandbox.ai/getting-started/) guide for startup instructions.

java

```
import com.alibaba.opensandbox.sandbox.Sandbox;
import com.alibaba.opensandbox.sandbox.config.ConnectionConfig;
import com.alibaba.opensandbox.sandbox.domain.exceptions.SandboxException;
import com.alibaba.opensandbox.sandbox.domain.models.execd.executions.Execution;

public class QuickStart {
    public static void main(String[] args) {
        // 1. Configure connection
        ConnectionConfig config = ConnectionConfig.builder()
            .domain("api.opensandbox.io")
            .apiKey("your-api-key")
            .build();

        // 2. Create a Sandbox using try-with-resources
        try (Sandbox sandbox = Sandbox.builder()
                .connectionConfig(config)
                .image("ubuntu")
                .build()) {

            try {
                Execution execution = sandbox.commands().run("echo 'Hello Sandbox!'");
                System.out.println(execution.getLogs().getStdout().get(0).getText());
            } finally {
                sandbox.kill();
            } // try-with-resources closes the client even if kill() fails.

        } catch (SandboxException e) {
            // Handle Sandbox specific exceptions
            System.err.println("Sandbox Error: [" + e.getError().getCode() + "] " + e.getError().getMessage());
            System.err.println("Request ID: " + e.getRequestId());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```


### Kotlin

kotlin

```
import com.alibaba.opensandbox.sandbox.Sandbox
import com.alibaba.opensandbox.sandbox.config.ConnectionConfig

fun main() {
    val config = ConnectionConfig.builder()
        .domain("api.opensandbox.io")
        .apiKey("your-api-key")
        .build()
    Sandbox.builder().image("ubuntu").connectionConfig(config).build().use { sandbox ->
        try {
            val result = sandbox.commands().run("echo 'Hello Sandbox!'")
            result.logs.stdout.forEach { print(it.text) }
        } finally {
            sandbox.kill()
        }
    }
}
```


`use` / try-with-resources releases the local client. `kill()` terminates the remote sandbox. The remaining examples use Java; Kotlin calls the same methods.


## Lifecycle Hooks


Configure lifecycle hooks on `Sandbox.Builder`. `preStart` completes before the entrypoint starts, while `periodic` hooks run on their schedules after startup.

java

```
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.LifecycleHook;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.PeriodicLifecycleHook;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.SandboxLifecycle;

SandboxLifecycle lifecycle = SandboxLifecycle.builder()
    .preStart(LifecycleHook.builder()
        .command("sh", "-c", "echo ready > /tmp/prestart.done")
        .timeoutSeconds(120)
        .build())
    .periodic(PeriodicLifecycleHook.builder()
        .name("checkpoint")
        .schedule("@every 5m")
        .command("sh", "-c", "date -u >> /tmp/checkpoints.log")
        .timeoutSeconds(120)
        .build())
    .build();

Sandbox sandbox = Sandbox.builder()
    .connectionConfig(config)
    .image("ubuntu:24.04")
    .lifecycle(lifecycle)
    .build();
```


The Server validates `timeoutSeconds`; `preStart` accepts 1–10800 seconds, while `periodic` accepts 1–300 seconds. Both default to 60 seconds when omitted. See [Lifecycle Hooks](https://open-sandbox.ai/guides/lifecycle-hooks) for timing, failure behavior, and provider limitations.


### Idle policy (auto-pause and wake-on-access)


`SandboxLifecycle.idlePolicy` (OSEP-0024, fast-sandbox only) tells the control plane to auto-pause the sandbox after `idleTimeoutSeconds` (30–86400) of continuously idle ingress-observed traffic, and to wake it on the next request. It is control-plane state: it never reaches the guest, is accepted in template mode (`TemplateLauncher.idlePolicy(...)`), and is rejected by non-fast-sandbox backends. Omitting it preserves non-automated behavior exactly.

kotlin

```
val sandbox = Sandbox.builder()
    .connectionConfig(config)
    .image("ubuntu:24.04")
    .lifecycle(
        SandboxLifecycle.builder()
            .idlePolicy {
                idleTimeoutSeconds(300)
                onIdle(OnIdleAction.PAUSE)
                wakeOnAccess(true)
            }
            .build()
    )
    .build()
```


`activeProbe` lets the application veto a pause while real work runs without producing ingress traffic: declare an endpoint answering `{"active": bool, "message"?: string}` and the server polls it when the sandbox is otherwise idle; a busy answer resets the idle clock. Invalid policies fail fast in the `IdlePolicy.Builder`.


### Wake retry


A request to a paused sandbox may arrive while its restore is still in progress. The gateway answers `503` with the `OpenSandbox-Wake: expired` marker; the retry interceptor recognizes it and resends the original request after the `Retry-After` delay (safe for any method — the marker proves the request was never forwarded). The wake budget defaults to 5 attempts / 60 seconds across all wake cycles; when it is exhausted the SDK throws `SandboxWakeTimeoutException` (carrying `attempts` and `waited`) while the server-side resume continues in the background. Bare `503` responses follow the existing retry rules untouched. Tune it on `RetryPolicy`: `wakeRetryEnabled` (default true), `wakeMaxAttempts` (5), `wakeOverallDeadline` (60s, `null` for unbounded).


## Usage Examples


Use a live `sandbox` and `config` from the quick start, before cleanup. Java snippets belong inside a method that handles or declares checked exceptions; place imports at the top of the file. Common imports are:

java

```
import java.time.Duration;
import java.util.*;
import com.alibaba.opensandbox.sandbox.SandboxManager;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.*;
import com.alibaba.opensandbox.sandbox.domain.models.execd.executions.*;
import com.alibaba.opensandbox.sandbox.domain.models.execd.filesystem.*;
```


Creation examples are alternatives. Close each client and kill sandboxes that are no longer needed.


### 1. Lifecycle Management


Manage the sandbox lifecycle, including renewal, pausing, and resuming.

java

```
// Renew the sandbox
// This resets the expiration time to (current time + duration)
sandbox.renew(Duration.ofMinutes(30));

// Request pause (runtime-dependent)
sandbox.pause();

long deadline = System.nanoTime() + Duration.ofMinutes(2).toNanos();
while (true) {
    if (System.nanoTime() >= deadline) throw new IllegalStateException("Pause timed out");
    SandboxInfo info = sandbox.getInfo();
    if (SandboxState.PAUSED.equals(info.getStatus().getState())) break;
    if (SandboxState.FAILED.equals(info.getStatus().getState())) {
        throw new IllegalStateException(info.getStatus().getMessage());
    }
    Thread.sleep(1000);
}

// Resume returns a new local handle.
try (Sandbox resumed = Sandbox.resumer()
    .sandboxId(sandbox.getId())
    .connectionConfig(config)
    .resume()) {
    System.out.println("State: " + resumed.getInfo().getStatus().getState());
}
```


Pause is asynchronous and runtime-dependent. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume). To attach to a running sandbox, use `Sandbox.connector().sandboxId(id).connectionConfig(config).connect()`.


Create a non-expiring sandbox by passing `timeout(null)`:

java

```
Sandbox manual = Sandbox.builder()
    .connectionConfig(config)
    .image("ubuntu")
    .timeout(null)
    .build();
```


### 2. Custom Health Check


Resolving an endpoint confirms that a route exists; it does not confirm that the application on that port is healthy. For service readiness, make a bounded request to the application's health endpoint and include the returned endpoint headers.


Define custom logic to determine if the sandbox is healthy. This overrides the default ping check. Set timeouts within custom checks; the SDK cannot interrupt them.

java

```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

// This HTTP probe uses Java 11+.
HttpClient http = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(2)).build();
Sandbox sandbox = Sandbox.builder()
    .connectionConfig(config)
    .image("nginx:latest")
    .entrypoint(List.of("nginx", "-g", "daemon off;"))
    .healthCheck(sbx -> {
        try {
            SandboxEndpoint endpoint = sbx.getEndpoint(80);
            HttpRequest.Builder request = HttpRequest.newBuilder()
                .uri(URI.create(config.getProtocol() + "://" + endpoint.getEndpoint() + "/"))
                .timeout(Duration.ofSeconds(2)).GET();
            endpoint.getHeaders().forEach(request::header);
            return http.send(request.build(), HttpResponse.BodyHandlers.discarding()).statusCode() == 200;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new IllegalStateException("Health check interrupted", e);
        } catch (Exception e) {
            return false;
        }
    })
    .build();
```


### 3. Command Execution & Streaming


Execute commands and handle output streams in real-time.

java

```
// Create handlers for streaming output
ExecutionHandlers handlers = ExecutionHandlers.builder()
    .onStdout(msg -> System.out.println("STDOUT: " + msg.getText()))
    .onStderr(msg -> System.err.println("STDERR: " + msg.getText()))
    .onExecutionComplete(complete ->
        System.out.println("Command finished in " + complete.getExecutionTimeInMillis() + "ms")
    )
    .build();

// Execute command with handlers
RunCommandRequest request = RunCommandRequest.builder()
    .command("for i in {1..5}; do echo \"Count $i\"; sleep 0.5; done")
    .handlers(handlers)
    .build();

sandbox.commands().run(request);
```


To execute a native program without shell parsing, pass an argument list. On Linux, this example prints literal `$HOME` and keeps `hello world` as one argument:

java

```
sandbox.commands().run(RunCommandRequest.builder()
    .argv(List.of("printf", "%s\n", "$HOME", "hello world"))
    .build());
```


Native argv execution requires an updated execd. See [command execution modes](https://open-sandbox.ai/architecture/data-plane/execd#command-execution) for executable lookup and platform behavior.


#### Background commands


Poll incremental logs and status. Command timeout is separate from sandbox TTL.

java

```
Execution execution = sandbox.commands().run(RunCommandRequest.builder()
    .command("for i in 1 2 3; do echo step-$i; sleep 1; done")
    .background(true).timeout(Duration.ofSeconds(30)).build());
String commandId = Objects.requireNonNull(execution.getId(), "No command ID returned");
Long cursor = 0L;
long deadline = System.nanoTime() + Duration.ofSeconds(45).toNanos();
while (true) {
    if (System.nanoTime() >= deadline) {
        sandbox.commands().interrupt(commandId);
        throw new IllegalStateException("Command did not finish");
    }
    CommandStatus status = sandbox.commands().getCommandStatus(commandId);
    CommandLogs logs = sandbox.commands().getBackgroundCommandLogs(commandId, cursor);
    System.out.print(logs.getContent());
    if (logs.getCursor() != null) cursor = logs.getCursor();
    if (Boolean.FALSE.equals(status.getRunning())) {
        if (!Integer.valueOf(0).equals(status.getExitCode())) {
            throw new IllegalStateException("Command failed: " + status.getExitCode() + ", " + status.getError());
        }
        break;
    }
    Thread.sleep(500);
}
```


#### Persistent shell sessions


A Bash session preserves shell variables and the working directory across commands.

java

```
String sessionId = sandbox.commands().createSession("/tmp");
try {
    sandbox.commands().runInSession(sessionId, RunInSessionRequest.builder()
        .command("export DEMO=hello").build());
    Execution result = sandbox.commands().runInSession(sessionId, RunInSessionRequest.builder()
        .command("echo \"$DEMO\"; pwd").build());
    result.getLogs().getStdout().forEach(message -> System.out.print(message.getText()));
} finally {
    sandbox.commands().deleteSession(sessionId);
}
```


#### Persistent environment variables


Set environment variables that the runtime injects into every subsequent command and session — without hand-writing shell escaping against the sandbox env file.

java

```
sandbox.commands().setEnv("MY_TOKEN", "it's a safe value");
```


Keys must match `[A-Za-z_][A-Za-z0-9_]*`. Values without a single quote are stored verbatim; values containing a single quote use the env file's double-quoted form, in which shell-style `$NAME` sequences may be expanded when the runtime loads the file. The env file is append-only: the last write for a key wins. Throws `SandboxException` if the sandbox fails to persist the variable.


For filesystem/process isolation within a sandbox, see [Isolation Sessions](https://open-sandbox.ai/guides/isolation-sessions). These are separate from Bash sessions.


### 4. File Operations


Manage files and directories, including read, write, list, delete, and search.

java

```
// 1. Write file
sandbox.files().write(List.of(
    WriteEntry.builder()
        .path("/tmp/hello.txt")
        .data("Hello World")
        .mode(644)
        .build()
));

// 2. Read file
String content = sandbox.files().readFile("/tmp/hello.txt", "UTF-8", null);
System.out.println("Content: " + content);

// List immediate children; search filters by a filename pattern.
sandbox.files().listDirectory("/tmp").forEach(entry -> System.out.println(entry.getPath()));

// 3. Search files
List<EntryInfo> files = sandbox.files().search(
    SearchEntry.builder()
        .path("/tmp")
        .pattern("*.txt")
        .build()
);
files.forEach(f -> System.out.println("Found: " + f.getPath()));

// 4. Delete file
sandbox.files().deleteFiles(List.of("/tmp/hello.txt"));
```


#### File operations with an explicit identity


Bind a filesystem client to a Linux UID and GID:

kotlin

```
val files = sandbox.filesWithIdentity(1001, 2000)
```


The bound client exposes the usual file operations and shares the sandbox connection, authentication, and endpoint routing headers. The existing file client retains its default identity. Select the UID/GID separately for command execution.


This requires Linux and an Execd version that supports filesystem execution identity. Unsupported servers return an error; requests never fall back to the default filesystem routes. Keep sandbox credentials and identity selection in the trusted backend. Linux filesystem permissions apply; this feature does not create a tenant isolation boundary. See [Execd](https://open-sandbox.ai/architecture/data-plane/execd) for permission and workspace provisioning details.


### 5. Sandbox Management (Admin)


Use `SandboxManager` for administrative tasks and finding existing sandboxes.

java

```
try (SandboxManager manager = SandboxManager.builder()
    .connectionConfig(config)
    .build()) {
    // First page only; increase page for subsequent pages.
    PagedSandboxInfos sandboxes = manager.listSandboxInfos(
        SandboxFilter.builder().states(SandboxState.RUNNING).pageSize(10).page(1).build()
    );
    sandboxes.getSandboxInfos().forEach(info -> System.out.println(info.getId()));
}
```


### Resource metrics


Read current sandbox resource usage with `sandbox.getMetrics()`. This is separate from [SDK creation telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


### 6. Client Pool and observability


`SandboxPool` provides four acquire policies and staged warmup controls. Use `InMemoryPoolStateStore` in one process, or the optional `com.alibaba.opensandbox:sandbox-pool-redis` module with a caller-managed Jedis client for distributed deployments. See [Client Pool](https://open-sandbox.ai/guides/client-pool) for configuration, examples, cleanup, and namespace retirement.


Set `ConnectionConfig.builder().enableTracing(true)` to emit [pool warmup traces](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing). The JVM SDK also adds trace IDs to SLF4J MDC. For remote logs/events, use `SandboxManager.getDiagnosticLogs` / `getDiagnosticEvents`; see [Diagnostics](https://open-sandbox.ai/api/#diagnostics). Create-latency reporting is controlled separately by [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Snapshots and metadata


Create a snapshot with `sandbox.createSnapshot` or `manager.createSnapshot`. `SandboxManager` exposes `getSnapshot`, `listSnapshots`, `deleteSnapshot`, and `waitForSnapshotReady` to wait for asynchronous snapshot completion. Restore with `Sandbox.builder().snapshotId(snapshotId).connectionConfig(config).build()`.


Use `sandbox.patchMetadata` or `manager.patchSandboxMetadata` to add/replace metadata keys; a `null` value removes a key. Runtime support is described by the [lifecycle contract](https://open-sandbox.ai/api/#1-sandbox-lifecycle-yml).


Snapshot support depends on the runtime and server configuration. Renew the source sandbox first if its remaining TTL may expire during snapshot creation. The JVM helper waits for `Ready` and raises an exception on failure or timeout:

java

```
try (SandboxManager manager = SandboxManager.builder().connectionConfig(config).build()) {
    SnapshotInfo snapshot = sandbox.createSnapshot("demo");
    System.out.println("Snapshot: " + snapshot.getId());
    manager.waitForSnapshotReady(snapshot.getId(), Duration.ofMinutes(15));
    try (Sandbox restored = Sandbox.builder()
            .snapshotId(snapshot.getId()).connectionConfig(config).build()) {
        try {
            System.out.println(restored.getId());
        } finally {
            restored.kill();
        }
    }
    // The snapshot is retained. When no longer needed: manager.deleteSnapshot(snapshot.getId());
}
```


Metadata updates can include both replacement values and removals. Use a map that accepts null values (`Map.of` does not):

java

```
Map<String, String> patch = new HashMap<>();
patch.put("project", "demo");
patch.put("obsolete-key", null);
sandbox.patchMetadata(patch);
```


## Configuration


### 1. Connection Configuration


The `ConnectionConfig` class manages API server connection settings.


Transfer timeouts


`requestTimeout` bounds each transport phase - connecting, waiting for response headers, and waiting for more of a response body - but it never caps a healthy file upload or download that keeps making progress. A transfer that stalls for longer than the timeout, or an upload that gets no response headers within it after the body has been sent, fails instead of hanging (the Go SDK's `ResponseHeaderTimeout` contract). An explicit `RetryPolicy.overallDeadline` still caps the whole transfer.


| Parameter | Description | Default | Environment Variable |
| --- | --- | --- | --- |
| `apiKey` | API Key for authentication | Optional; needed when server auth is enabled | `OPEN_SANDBOX_API_KEY` |
| `domain` | The endpoint domain of the sandbox service | `localhost:8080` | `OPEN_SANDBOX_DOMAIN` |
| `protocol` | HTTP protocol (http/https) | `http` | - |
| `requestTimeout` | Timeout for API requests | 30 seconds | - |
| `debug` | Enable debug logging for HTTP requests | `false` | - |
| `headers` | Custom HTTP headers | Empty | - |
| `connectionPool` | Shared OKHttp ConnectionPool | SDK-created per instance | - |
| `retryPolicy` | Automatic retry policy for non-streaming requests (see [Automatic retries](https://open-sandbox.ai/sdks/kotlin#_2-automatic-retries)) | Enabled (`RetryPolicy()`) | - |
| `useServerProxy` | Use sandbox server as proxy for execd/endpoint requests (e.g. when client cannot reach the sandbox directly) | `false` | - |
| `disableMetrics` | Disable SDK create-latency telemetry (see [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics)) | `false` | `OPENSANDBOX_DISABLE_METRICS` |
| `enableTracing` | Enable OpenTelemetry tracing for pool warmup (see [SDK Tracing](https://open-sandbox.ai/sdks/observability#pool-warmup-tracing)) | `false` | - |

java

```
import okhttp3.ConnectionPool;
import java.util.concurrent.TimeUnit;

// 1. Basic configuration
ConnectionConfig config = ConnectionConfig.builder()
    .apiKey("your-key")
    .domain("api.opensandbox.io")
    .requestTimeout(Duration.ofSeconds(60))
    .build();

// 2. Advanced: Shared Connection Pool
// If you create many Sandbox instances, sharing a connection pool is recommended to save resources.
// SDK default keep-alive is 30 seconds for its own pools.
ConnectionPool sharedPool = new ConnectionPool(50, 30, TimeUnit.SECONDS);

ConnectionConfig sharedConfig = ConnectionConfig.builder()
    .apiKey("your-key")
    .domain("api.opensandbox.io")
    .headers(Map.of(
        "X-Custom-Header", "value",
        "X-Request-ID", "trace-123"
    ))
    .connectionPool(sharedPool) // Inject shared pool
    .build();
```


SDK Telemetry


`Sandbox.builder()...build()` reports create latency to `POST /v1/metrics/events` by default. Call `ConnectionConfig.builder().disableMetrics(true)` or export `OPENSANDBOX_DISABLE_METRICS=1` to opt out. See [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


### 2. Automatic retries


The SDK retries transient failures automatically. `ConnectionConfig` installs a `RetryInterceptor` (`com.alibaba.opensandbox.sandbox.transport.RetryPolicy`) on the SDK's non-streaming HTTP clients.


Default behavior:


- **Enabled by default.** Idempotent methods (`GET/HEAD/PUT/DELETE/OPTIONS`) are retried on `429`, `502`, `503`, and on pre-send transport failures (DNS, TCP connect, TLS handshake).
- **`POST` / `PATCH` are never retried on a status code by default**, since the request may already have been applied server-side. Pre-send transport failures (before any byte is written) are still retried for these methods.
- Up to `3` retries with decorrelated-jitter exponential backoff, honoring a server `Retry-After` header (capped at 60s).
- **SSE / streaming requests bypass all automatic retry** because their bodies are not safely replayable. The SSE client also disables OkHttp's built-in connection recovery to prevent a streaming command POST from being replayed.


Behavior change


SDK-policy retries are on by default. This can increase the number of HTTP attempts and tail latency compared to earlier SDK versions. To disable the new SDK-policy retries, use `RetryPolicy.disabled()`; non-streaming requests then fall back to OkHttp's pre-existing built-in connection recovery.

java

```
import com.alibaba.opensandbox.sandbox.transport.RetryPolicy;
import com.alibaba.opensandbox.sandbox.transport.StatusCode;
import java.time.Duration;
import java.util.Set;

// Disable SDK-policy retries and retain OkHttp's built-in connection recovery.
ConnectionConfig config = ConnectionConfig.builder()
    .apiKey("your-key")
    .domain("api.opensandbox.io")
    .retryPolicy(RetryPolicy.disabled())
    .build();

// Custom policy: more retries, an overall wall-clock deadline, and an opt-in to
// retry POST/PATCH on 503 (only safe if your endpoints are idempotent).
ConnectionConfig tuned = ConnectionConfig.builder()
    .apiKey("your-key")
    .domain("api.opensandbox.io")
    .retryPolicy(new RetryPolicy(
        /* maxRetries */ 5,
        /* initialBackoff */ Duration.ofMillis(500),
        /* maxBackoff */ Duration.ofSeconds(30),
        /* backoffMultiplier */ 2.0,
        /* jitter */ com.alibaba.opensandbox.sandbox.transport.JitterMode.DECORRELATED,
        /* retryableStatusCodesIdempotent */ RetryPolicy.DEFAULT_IDEMPOTENT_STATUS,
        /* retryableStatusCodesNonIdempotent */ Set.of(StatusCode.SERVICE_UNAVAILABLE),
        /* perAttemptTimeout */ null,
        /* overallDeadline */ Duration.ofSeconds(20),
        /* onRetry */ null))
    .build();
```


### 3. Sandbox Creation Configuration


The `Sandbox.builder()` allows configuring the sandbox environment.


| Parameter | Description | Default |
| --- | --- | --- |
| `image` | Docker image to use | One of image or snapshot ID |
| `timeout` | Automatic termination timeout | 10 minutes |
| `entrypoint` | Container entrypoint command | `["tail", "-f", "/dev/null"]` |
| `resource` | CPU and memory limits | `{"cpu": "1", "memory": "2Gi"}` |
| `env` | Environment variables | Empty |
| `metadata` | Custom metadata tags | Empty |
| `extensions` | Opaque server-side extension parameters | Empty |
| `networkPolicy` | Optional outbound network policy (egress) | - |
| `credentialProxy` | Optional Credential Vault proxy startup settings | - |
| `readyTimeout` | Max time to wait for sandbox to be ready | 30 seconds |
| `snapshotId` | Restore a snapshot instead of an image | - |
| `resourceRequests` | Kubernetes resource requests; must not exceed limits | - |
| `lifecycle` | Pre-start and periodic hooks | - |
| `platform` | OS/architecture constraint | - |
| `volumes` | Host, PVC, or OSSFS mounts | - |
| `secureAccess` | Require endpoint access credentials | `false` |


WARNING


Metadata keys under `opensandbox.io/` are reserved for system-managed labels and will be rejected by the server.

java

```
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.NetworkPolicy;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.NetworkRule;

Sandbox sandbox = Sandbox.builder()
    .connectionConfig(config)
    .image("python:3.11")
    .timeout(Duration.ofMinutes(30))
    .resource(Map.of("cpu", "2", "memory", "4Gi"))
    .env("PYTHONPATH", "/app")
    .metadata("project", "demo")
    .extension("storage.id", "dataset-001")
    .networkPolicy(
        NetworkPolicy.builder()
            .defaultAction(NetworkPolicy.DefaultAction.DENY)
            .addEgress(
                NetworkRule.builder()
                    .action(NetworkRule.Action.ALLOW)
                    .target("pypi.org")
                    .build()
            )
            .build()
    )
    .build();
```


### 4. Runtime Egress Policy Updates


Runtime egress reads and patches go directly to the sandbox egress sidecar. The SDK first resolves the sandbox endpoint on port `18080`, then calls the sidecar `/policy` API.


Template-backed sandboxes have no sandbox-side egress sidecar: the SDK detects them via the server's `OPEN-SANDBOX-ORIGIN` response header (see [Fsb Template Management](https://open-sandbox.ai/sdks/kotlin#fsb-template-management)) and routes the same `getEgressPolicy` / `patchEgressRules` / `deleteEgressRules` calls through the lifecycle control plane (`/sandboxes/{sandboxId}/networkpolicy`) instead.


Patch uses merge semantics:


- Incoming rules take priority over existing rules with the same `target`.
- Existing rules for other targets remain unchanged.
- Within a single patch payload, the first rule for a `target` wins.
- The current `defaultAction` is preserved.

java

```
NetworkPolicy policy = sandbox.getEgressPolicy();

sandbox.patchEgressRules(
    List.of(
        NetworkRule.builder().action(NetworkRule.Action.ALLOW).target("www.github.com").build(),
        NetworkRule.builder().action(NetworkRule.Action.DENY).target("pypi.org").build()
    )
);
```


### 5. Credential Vault


Credential Vault injects outbound credentials from the egress sidecar while keeping real secrets out of sandbox environment variables, commands, files, and logs. Create the sandbox with `credentialProxyEnabled(true)`, then write credentials and bindings through `sandbox.credentialVault()`.

java

```
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.Credential;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.CredentialAuth;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.CredentialBinding;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.CredentialMatch;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.CredentialVaultCreateRequest;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.NetworkPolicy;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.NetworkRule;
import java.util.List;

Sandbox sandbox = Sandbox.builder()
    .connectionConfig(config)
    .image("python:3.11")
    .networkPolicy(
        NetworkPolicy.builder()
            .defaultAction(NetworkPolicy.DefaultAction.DENY)
            .addEgress(
                NetworkRule.builder()
                    .action(NetworkRule.Action.ALLOW)
                    .target("api.example.com")
                    .build()
            )
            .build()
    )
    .credentialProxyEnabled(true)
    .build();

sandbox.credentialVault().create(
    CredentialVaultCreateRequest.builder()
        .credentials(
            List.of(
                Credential.builder()
                    .name("api-token")
                    .inlineSource("<token>")
                    .build()
            )
        )
        .bindings(
            List.of(
                CredentialBinding.builder()
                    .name("api-token")
                    .match(
                        CredentialMatch.builder()
                            .schemes(CredentialMatch.Scheme.HTTPS)
                            .hosts("api.example.com")
                            .paths("/v1/*")
                            .build()
                    )
                    .auth(CredentialAuth.apiKey("x-api-key", "api-token"))
                    .build()
            )
        )
        .build()
);
```


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for auth types, binding guidance, and Git/curl examples.


WARNING


Credential Vault is unavailable for template-backed sandboxes: they have no sandbox-side egress sidecar. `sandbox.credentialVault()` throws for them.


## Fsb Template Management


fsb (fast-sandbox microVM) golden-image templates are managed through `SandboxManager`. Template builds are asynchronous: `createTemplate` returns with `status.phase` set to `Pending`; poll `getTemplate` until the phase reaches `Succeeded` or `Failed`. Only a `Succeeded` template can create sandboxes. These operations require a configured Fsb runtime. Replace the example publish URI with a location configured for your server, and use an open `SandboxManager` created with `SandboxManager.builder().connectionConfig(config).build()`. Close the manager when finished.

java

```
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.CreateTemplateRequest;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.TemplateFilter;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.TemplateInfo;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.TemplatePhase;
import com.alibaba.opensandbox.sandbox.domain.models.sandboxes.TemplateReadiness;

CreateTemplateRequest request = CreateTemplateRequest.builder()
    .image("alpine:3.19")
    .publish("s3://bucket/publish")
    .resourceLimits(Map.of("cpu", "1", "memory", "512Mi", "disk", "2Gi"))
    .readiness(TemplateReadiness.builder().probe("tcp://127.0.0.1:44772").build())
    .metadata(Map.of("team", "backend"))
    .build();

// Start the async build (starts at TemplatePhase.PENDING)
TemplateInfo template = manager.createTemplate(request);

// Poll for up to 15 minutes; adjust for the image and runtime.
long deadline = System.nanoTime() + Duration.ofMinutes(15).toNanos();
while (!template.getStatus().getPhase().equals(TemplatePhase.SUCCEEDED)
    && !template.getStatus().getPhase().equals(TemplatePhase.FAILED)) {
    if (System.nanoTime() >= deadline) throw new IllegalStateException("Template build timed out");
    Thread.sleep(2000);
    template = manager.getTemplate(template.getTemplateId());
}
if (TemplatePhase.FAILED.equals(template.getStatus().getPhase())) {
    throw new IllegalStateException("Template build failed: " + template.getTemplateId());
}

// List with metadata filters (1-indexed paging)
manager.listTemplates(
    TemplateFilter.builder()
        .metadata(Map.of("team", "backend"))
        .pageSize(20)
        .page(1)
        .build()
);

// When no longer needed: manager.deleteTemplate(template.getTemplateId());
```


### Creating a Sandbox from a Template


Use `Sandbox.fromTemplate()` to create a sandbox from a `Succeeded` template. Template mode fixes the workload shape on the server: only `metadata`, `networkPolicy` and `extensions` may accompany the template id, and `timeout` is required.

java

```
import java.time.Duration;

Sandbox sandbox = Sandbox.fromTemplate()
    .connectionConfig(config)
    .templateId("tpl_123")
    .timeout(Duration.ofMinutes(30))
    .metadata("project", "demo")
    .networkPolicy(
        NetworkPolicy.builder()
            .defaultAction(NetworkPolicy.DefaultAction.DENY)
            .addEgress(
                NetworkRule.builder()
                    .action(NetworkRule.Action.ALLOW)
                    .target("pypi.org")
                    .build()
            )
            .build()
    )
    .create();
```


The created sandbox reports `SandboxOrigin.TEMPLATE` from `sandbox.getOrigin()`. Template-backed sandboxes have no egress sidecar, so the SDK routes their egress policy through the lifecycle control plane automatically — including `Sandbox.connector()` and `Sandbox.resumer()` re-attach flows, which detect the origin from the server's `OPEN-SANDBOX-ORIGIN` response header.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/kotlin.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/deployment/ack`

# ACK 部署


OpenSandbox 可部署在任何标准 Kubernetes 集群上，ACK 完全兼容标准 Kubernetes API。组件安装细节见 [Kubernetes 部署](https://open-sandbox.ai/deployment/) ，本文介绍在 ACK 上部署的具体步骤与注意事项。


## 前提条件


- 阿里云账号，已开通容器服务 ACK 并完成默认角色授权
- Kubernetes 1.21.1+
- Helm 3.x（仅用作模板渲染器）、`kubectl`
- 集群 KubeConfig 凭证（见[第二步](https://open-sandbox.ai/deployment/ack#%E7%AC%AC%E4%BA%8C%E6%AD%A5-%E8%BF%9E%E6%8E%A5%E9%9B%86%E7%BE%A4)）


## 第一步：创建 ACK 集群


推荐使用 **ACK 托管集群（Pro）** ，参考 [创建 ACK 托管集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2/) 完成创建，关键配置如下：


| 配置项 | 建议 |
| --- | --- |
| 集群版本 | ≥ 1.21 |
| 网络插件 | Terway（沙箱 Pod 拥有 VPC 内可直接路由的 Pod IP） |
| 初始节点池 | 2–3 台通用型实例，承载控制面组件 |
| 安全组 | 放行 Worker 节点间 VPC 内互通 |


## 第二步：连接集群


参考 [获取集群 KubeConfig 并通过 kubectl 工具连接集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster/) ，配置 `~/.kube/config` 后验证：

bash

```
kubectl get nodes
```


## 第三步：新增节点


为沙箱工作负载创建 **独立节点池** （可开启自动伸缩），与控制面组件隔离，参考 [创建和管理节点池](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool/) ；已有 ECS 实例可通过 [添加已有节点](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster/) 接入集群。日常管理参考 [节点管理](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/node-management/) 。
## 前提条件 ​
## 第一步：创建 ACK 集群 ​
## 第二步：连接集群 ​
## 第三步：新增节点 ​
## 第四步：部署 OpenSandbox ​
*按组件顺序部署（与 Deployment Order 一致）：*

*渲染并部署（artifactStore 与 Bucket、Endpoint 保持一致）：*

## ACK 环境注意事项 ​
## 卸载 ​
## 相关链接 ​










污点隔离


沙箱节点池配置污点（Taint）时，需在 BatchSandbox Pod 模板中添加对应的 Toleration，否则沙箱 Pod 无法调度。


fast-sandbox 节点池要求


fast-sandbox（Firecracker）对节点有两个要求：Worker 节点必须是 **裸金属服务器** （依赖 KVM）；节点池内 **所有节点的 CPU 型号必须一致** 。混用不同代际的机型会导致微虚拟机快照无法跨节点恢复，因此建议锁定单一实例规格并单独建节点池。


## 第四步：部署 OpenSandbox


采用 GitOps 渲染模式部署： `helm template` 将 chart 渲染为 YAML，经 `kubectl diff` 审阅后用 `kubectl apply --server-side` 应用到集群。渲染产物与 values 文件纳入 Git 管理。


按组件顺序部署（与 [Deployment Order](https://open-sandbox.ai/deployment/#deployment-order) 一致）：

text

```
base → controller → fast-sandbox* → ingress-gateway → server
```


* `fast-sandbox` 为可选组件；启用时需在 ingress-gateway 与 server 之前部署。


注意：


- 不要与 `helm install` / `helm upgrade` 混用，两种方式会互相覆盖
- 使用 `--server-side`（Server-Side Apply）：CRD 体量超过 client-side apply 的注解上限


准备仓库与命名空间：

bash

```
git clone https://github.com/opensandbox-group/OpenSandbox.git
cd OpenSandbox
git checkout release-1.1.0   # 部署对应发布版本
mkdir -p out                 # 渲染产物目录

# 渲染部署不会自动创建 namespace，需提前创建
kubectl create namespace opensandbox-system --dry-run=client -o yaml \
  | kubectl apply --server-side -f -
kubectl create namespace opensandbox --dry-run=client -o yaml \
  | kubectl apply --server-side -f -
```


### 1. 部署 base（CRD + RBAC）

bash

```
helm template base manifests/charts/base > out/base.yaml

kubectl diff -f out/base.yaml
kubectl apply --server-side -f out/base.yaml
```


应用成功后输出 21 行 `serverside-applied` （1 Namespace + 7 CRD + 11 ClusterRole + 2 ClusterRoleBinding）。验证 CRD：

bash

```
kubectl get crd | grep -E 'sandbox\.(opensandbox|fast)\.io'
```

text

```
batchsandboxes.sandbox.opensandbox.io               2026-09-28T08:48:54Z
pools.sandbox.opensandbox.io                        2026-09-28T08:48:55Z
sandboxes.sandbox.fast.io                           2026-09-28T08:49:04Z
sandboxpools.sandbox.fast.io                        2026-09-28T08:48:59Z
sandboxsnapshots.sandbox.fast.io                    2026-09-28T08:49:06Z
sandboxsnapshots.sandbox.opensandbox.io             2026-09-28T08:48:57Z
sandboxtemplates.sandbox.fast.io                    2026-09-28T08:49:07Z
```


### 2. 部署 controller

bash

```
helm template opensandbox-controller manifests/charts/controller \
  -n opensandbox-system \
  --set controller.replicaCount=2 > out/controller.yaml

kubectl diff -f out/controller.yaml
kubectl apply --server-side -f out/controller.yaml

kubectl rollout status deployment/opensandbox-controller-manager \
  --namespace opensandbox-system --timeout=180s
```


应用成功后输出 6 行 `serverside-applied` （SA + Role/Binding + ClusterRole/Binding + Deployment）。rollout 与 Pod 状态：

text

```
deployment "opensandbox-controller-manager" successfully rolled out

opensandbox-controller-manager-865887c57-mvbr9   1/1   Running   0   6m25s   10.79.205.208   ap-southeast-1.10.79.205.204
opensandbox-controller-manager-865887c57-rhgxn   1/1   Running   0   37s     10.79.205.209   ap-southeast-1.10.79.205.203
```


### 3. 部署 fast-sandbox


必须在 server 之前部署：server 启动时会连接 FastPath gRPC 端点。


#### 准备制品仓库（OSS）


fast-sandbox 的 golden image 与快照存放在 S3 兼容的制品仓库。ACK 上建议使用与集群同 region 的 OSS，并通过 VPC 内网域名访问（避免公网流量）：


1. 在与集群相同的 region 创建 OSS Bucket（如 `my-sandbox-images`）
2. 创建 RAM 子账号 AK/SK，授予该 Bucket 的读写权限
3. VPC 内网 Endpoint 格式为 `https://oss-<region>.internal.aliyuncs.com`（如 `https://oss-ap-southeast-1.internal.aliyuncs.com`）


#### 配置凭证 Secret


WARNING


registry.json 的最终 schema 由 fast-sandbox 上游编译工具生成，以下为 **占位符** 示例，仅用于让 Pod 正常启动；实际拉取制品前需按工具产物补全。

bash

```
cat > /tmp/registry.json <<'EOF'
{
  "endpoint": "https://oss-ap-southeast-1.internal.aliyuncs.com",
  "bucket": "my-sandbox-images",
  "accessKeyId": "<YOUR_ACCESS_KEY_ID>",
  "accessKeySecret": "<YOUR_ACCESS_KEY_SECRET>"
}
EOF

kubectl create secret generic fast-sandbox-agent-registry \
  -n opensandbox-system \
  --from-file=registry.json=/tmp/registry.json \
  --dry-run=client -o yaml | kubectl apply --server-side -f -
rm /tmp/registry.json   # AK/SK 不落盘、不进 Git
```


渲染并部署（ `artifactStore` 与 Bucket、Endpoint 保持一致）：

bash

```
helm template fast-sandbox manifests/charts/fast-sandbox \
  -n opensandbox-system \
  --set artifactStore.store=s3://my-sandbox-images/publish \
  --set artifactStore.endpoint=https://oss-ap-southeast-1.internal.aliyuncs.com \
  > out/fast-sandbox.yaml

kubectl diff -f out/fast-sandbox.yaml
kubectl apply --server-side -f out/fast-sandbox.yaml
```


应用成功后输出 13 行 `serverside-applied` （PDB + SA + Secret/ConfigMap + RBAC + 2 Service + DaemonSet + Deployment）。验证 Pod 状态与节点标签：

text

```
fast-sandbox-controller-7d79b6447b-8q5bp   1/1   Running
firecracker-runtime-hkg9d                  2/2   Running
firecracker-runtime-z8mq9                  2/2   Running

NAME                           STATUS   KVM    FIRECRACKER-NODE
ap-southeast-1.10.79.205.203   Ready    true   true
ap-southeast-1.10.79.205.204   Ready    true   true
```


runtime 就绪后会为节点自动打 4 个标签（ `kvm` 、 `firecracker-node` 、 `cpu-identity` 、 `cpu-template` ）。其中 `cpu-identity` 标识 CPU 型号（厂商-家族-型号），同一节点池内必须一致，否则微虚拟机快照无法跨节点恢复：

bash

```
kubectl get nodes -L sandbox.fast.io/kvm,fast-sandbox.io/cpu-identity,fast-sandbox.io/firecracker-node
```


节点需加载 kvm 内核模块


ECS 裸金属节点默认不加载 kvm 模块，readiness 会报 `/dev/kvm unusable: device does not exists` 。此时需在节点上执行 `modprobe kvm kvm_amd` （可通过 privileged Pod 的 `nsenter -t 1 -m` 或节点 SSH），再执行 `kubectl rollout restart daemonset/firecracker-runtime -n opensandbox-system` 让 Pod 重建 `/dev` 。模块加载在节点重启后失效，需重新执行；建议通过节点池 bootstrap 脚本或自定义镜像持久化。


模板构建、镜像准备等前置步骤见 [fast-sandbox runtime 部署指南](https://github.com/opensandbox-group/OpenSandbox/blob/main/manifests/HELM-DEPLOYMENT.md#fast-sandbox-runtime-firecracker) 。


### 4. 部署 ingress-gateway


Kubernetes 环境中沙箱 Pod 只有 ClusterIP，客户端流量须经 ingress-gateway 路由。在 server 之前部署，这样 server 首次安装即可完成网关公告配置。


`providerType=fast-sandbox` 时网关强制要求 secure-access 签名密钥环（OSEP-0011）：server 用它签发路由令牌，网关用它验证。先生成密钥，部署 server 时复用：

bash

```
KEY=$(openssl rand -base64 32)   # 保存好，部署 server 时复用

helm template ingress-gateway manifests/charts/ingress-gateway \
  -n opensandbox-system \
  --set gateway.providerType=fast-sandbox \
  --set gateway.fastpathEndpoint=fast-sandbox-fastpath.opensandbox-system.svc:9090 \
  --set "gateway.secureAccess.keys[0].key_id=a" \
  --set "gateway.secureAccess.keys[0].key=$KEY" \
  > out/ingress-gateway.yaml

kubectl diff -f out/ingress-gateway.yaml
kubectl apply --server-side -f out/ingress-gateway.yaml

kubectl rollout status deployment/opensandbox-ingress-gateway \
  --namespace opensandbox-system --timeout=180s
```


验证：

text

```
deployment "opensandbox-ingress-gateway" successfully rolled out

opensandbox-ingress-gateway-66bd4bf7b7-59nfz   1/1   Running   0   67s
opensandbox-ingress-gateway-66bd4bf7b7-dbc2v   1/1   Running   0   56s
```


### 5. 部署 lifecycle server


创建 API Key Secret（生产环境建议使用外部密钥管理系统）：

bash

```
read -s OPENSANDBOX_API_KEY
kubectl create secret generic opensandbox-api-key \
  --namespace opensandbox-system \
  --from-literal=api-key="${OPENSANDBOX_API_KEY}" \
  --dry-run=client -o yaml | kubectl apply -f -
unset OPENSANDBOX_API_KEY
```


在 values 文件中引用 Secret 并配置网关公告。注意 `secureAccess` 必须与 ingress-gateway 使用同一把密钥（ `activeKey` 对应 key_id）； `gatewayRouteMode` 需与 ingress-gateway chart 的 `gateway.gatewayRouteMode` 一致（默认均为 `header` ）：

yaml

```
# values-server.yaml
server:
  env:
    - name: OPENSANDBOX_SERVER_API_KEY
      valueFrom:
        secretKeyRef:
          name: opensandbox-api-key
          key: api-key
  gateway:
    enabled: true
    host: opensandbox-ingress-gateway.opensandbox-system.svc
    secureAccess:
      activeKey: a
      keys:
        - key_id: a
          key: <部署网关时生成的 base64 密钥>
```


INFO


`configToml` （沙箱工作负载命名空间、镜像地址、运行时等）与 PostgreSQL 持久化等也在这个文件中配置，渲染前补齐。完整参考见 [Kubernetes 部署](https://open-sandbox.ai/deployment/) 。


渲染并部署：

bash

```
helm template opensandbox-server manifests/charts/server \
  -n opensandbox-system \
  -f values-server.yaml > out/server.yaml

kubectl diff -f out/server.yaml
kubectl apply --server-side -f out/server.yaml

kubectl rollout status deployment/opensandbox-server \
  --namespace opensandbox-system --timeout=180s

kubectl port-forward --namespace opensandbox-system \
  service/opensandbox-server 8080:80
curl --fail http://127.0.0.1:8080/health
```


预期输出：

text

```
deployment "opensandbox-server" successfully rolled out

{"status":"healthy"}
```


### 可选：部署共享 SandboxPool


SandboxPool（ `sandbox.fast.io` ）是 fast-sandbox 的容量与策略单元，定义 Fastlet 的预热规模（ `capacity` ）、运行时 profile（ `runtime` ）、每个沙箱的资源规格（ `sandboxResources` ）与调度约束（ `fastletTemplate` ），同一池中的沙箱共享这些设置。仓库提供了示例 `manifests/examples/sandboxpool-fast-sandbox.yaml` ：

yaml

```
apiVersion: sandbox.fast.io/v1alpha2
kind: SandboxPool
metadata:
  name: shared-pool
  namespace: opensandbox-dataplane
spec:
  runtime: firecracker
  sandboxResources:
    cpu: "1"
    memory: 2Gi
    pids: 256
  capacity:
    poolMin: 5
    poolMax: 10
    bufferMin: 0
    bufferMax: 2
  maxSandboxesPerPod: 4
  fastletTemplate:
    spec:
      containers:
      - name: fastlet
        image: opensandbox/fsb-fastlet:release-1.1.1-rc.1
        imagePullPolicy: IfNotPresent
        env:
        - name: FAST_SANDBOX_RUNTIME_AGENT_SOCKET
          value: /run/fast-sandbox/firecracker/runtime.sock
        volumeMounts:
        - name: agent-socket
          mountPath: /run/fast-sandbox/firecracker
      volumes:
      - name: agent-socket
        hostPath:
          path: /run/fast-sandbox/firecracker
          type: DirectoryOrCreate
      nodeSelector:
        fast-sandbox.io/firecracker-node: "true"
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app: sandbox-fastlet
              topologyKey: kubernetes.io/hostname
  warmImages: []
```


注意： `fastletTemplate` 必须包含名为 `fastlet` 的容器（fast-sandbox companion 镜像），并挂载节点上 runtime-agent 的 UDS socket，否则 controller 会拒绝处理。需要 egress 网络策略时，参考集成环境的完整示例 `scripts/fast-sandbox-env/manifests/pool/firecracker-egress-pool.yaml` （含 egress sidecar 与 `infraComponents` / `actionHandlers` 声明）。


部署并验证：

bash

```
kubectl apply --server-side -f manifests/examples/sandboxpool-fast-sandbox.yaml

kubectl get pods -n opensandbox-dataplane
kubectl get sandboxpool shared-pool -n opensandbox-dataplane -o jsonpath='{.status.conditions[?(@.type=="RuntimeReady")].status}'
```


`poolMin=5` 表示预热 5 个 Fastlet（反亲和分散到各节点），全部就绪后 `RuntimeReady` 转为 `True` ：

text

```
NAME                        READY   STATUS    RESTARTS   AGE
shared-pool-fastlet-5nh85   2/2     Running   0          54s
shared-pool-fastlet-cxrln   2/2     Running   0          54s
shared-pool-fastlet-gzhml   2/2     Running   0          54s
shared-pool-fastlet-wnlsx   2/2     Running   0          54s
shared-pool-fastlet-zdrd4   2/2     Running   0          54s

True
```


### 升级


切换到新版本标签，重新渲染全部组件，diff 审阅后逐个 apply：

bash

```
git fetch --tags
git checkout release-1.2.0

helm template base manifests/charts/base > out/base.yaml
helm template opensandbox-controller manifests/charts/controller \
  -n opensandbox-system > out/controller.yaml
helm template ingress-gateway manifests/charts/ingress-gateway \
  -n opensandbox-system \
  --set gateway.fastpathEndpoint=fast-sandbox-fastpath.opensandbox-system.svc:9090 \
  > out/ingress-gateway.yaml
helm template opensandbox-server manifests/charts/server \
  -n opensandbox-system -f values-server.yaml > out/server.yaml

kubectl diff -f out/base.yaml && kubectl apply --server-side -f out/base.yaml
kubectl diff -f out/controller.yaml && kubectl apply --server-side -f out/controller.yaml
kubectl diff -f out/server.yaml && kubectl apply --server-side -f out/server.yaml
```


`kubectl diff` 在存在差异时退出码为 `1` ，脚本化时不应视为失败。


### 对外暴露 Server


在 `values-server.yaml` 中设置 `server.service.type: LoadBalancer` （ACK 会自动创建 SLB），重新渲染并 apply。生产环境建议使用内网 SLB，沙箱流量经由 ingress gateway。


## ACK 环境注意事项


| 主题 | 说明 |
| --- | --- |
| 网络插件 | 推荐 Terway；Flannel 模式下 Pod IP 为 overlay 地址，对外暴露沙箱前需确认路由可达 |
| fast-sandbox | 必须使用裸金属节点（KVM）且 CPU 型号一致，否则跳过该组件，使用默认运行时。详见 [fast-sandbox runtime](https://github.com/opensandbox-group/OpenSandbox/blob/main/manifests/HELM-DEPLOYMENT.md#fast-sandbox-runtime-firecracker) |
| 镜像拉取 | 默认镜像托管在 Docker Hub，VPC 内建议通过 ACR 同步后覆盖 `server.image.repository` 及 `configToml` 中的沙箱镜像地址 |
| Server 持久化 | 生产环境建议使用 RDS for PostgreSQL（见 [PostgreSQL 持久化](https://open-sandbox.ai/deployment/#use-postgresql-for-server-persistence) ） |
| 监控 | Controller 的 Prometheus 指标见 [Operator Metrics](https://open-sandbox.ai/deployment/#operator-metrics) ，可接入 ARMS Prometheus |


## 卸载


按部署的逆序删除渲染产物。注意：删除 `out/base.yaml` 会连同 CRD 一起删除（kubectl 不理会 `resource-policy: keep` ），并级联删除所有自定义资源：

bash

```
kubectl delete -f out/server.yaml
kubectl delete -f out/ingress-gateway.yaml
kubectl delete -f out/fast-sandbox.yaml      # 如部署
kubectl delete -f out/controller.yaml
kubectl delete -f out/base.yaml
```


如需保留 CRD、仅删除组件，跳过 `out/base.yaml` 即可；CRD 清理见 [Kubernetes 部署 → Uninstall](https://open-sandbox.ai/deployment/#uninstall) 。


## 相关链接


- [Kubernetes 部署](https://open-sandbox.ai/deployment/) — 组件完整安装与配置
- [Kubernetes Controller 概述](https://open-sandbox.ai/architecture/control-plane/operator) — CRD 与控制器机制
- [ACK 快速入门](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/getting-started/)
- [创建 ACK 托管集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2/)
- [创建和管理节点池](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool/)
- [添加已有节点](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster/)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/deployment/ack.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/reference/snapshot-store-migration`

# Snapshot Store Migration Guide


Feature: [#1653](https://github.com/opensandbox-group/OpenSandbox/pull/1653)


## Background


The server persists the public snapshot catalog in a configurable store. SQLite is the default backend; the PostgreSQL backend is opt-in for operators that need external persistence. The PostgreSQL backend does **not** read an existing SQLite database, so a server switched from `store.type = "sqlite"` to `store.type = "postgresql"` starts with an empty snapshot catalog.


Use the `migrate-snapshots` command to copy existing snapshot records from SQLite to PostgreSQL before switching the store type.


## Before you start


- Stop the server (or at least stop issuing snapshot requests) so the source SQLite database is not modified while it is read.
- The target PostgreSQL database must be reachable and the configured role must be able to create the `snapshots` table.
- Run the command against the same target database the server will use after the switch.


## Migrate
*Feature: #1653*

## Background ​
## Before you start ​
## Migrate ​
## Behavior ​
## Switch the server ​
## Verify ​








Dry-run first to see what would be copied:

bash

```
opensandbox-server migrate-snapshots \
  --from ~/.opensandbox/opensandbox.db \
  --to postgresql://user:password@localhost:5432/opensandbox \
  --dry-run
```


Then run the migration:

bash

```
opensandbox-server migrate-snapshots \
  --from ~/.opensandbox/opensandbox.db \
  --to postgresql://user:password@localhost:5432/opensandbox
```


The command prints a summary:

text

```
Snapshots migrated: total=42, migrated=42, skipped=0
```


## Behavior


- Records whose id already exists in PostgreSQL are skipped, so the command can be re-run safely. A repeated run reports `migrated=0` and `skipped=42`.
- `--dry-run` reports the counts without writing anything, including without creating the PostgreSQL `snapshots` table, so it works with read-only target credentials.
- The source SQLite database is opened read-only and is never modified, so a backup on a read-only mount can be migrated.
- The PostgreSQL schema is created only on a real migration run, when the table does not already exist.
- Timestamps stored as naive UTC in SQLite are written as `TIMESTAMPTZ` in UTC.


## Switch the server


After migration, update the server configuration:

toml

```
[store]
type = "postgresql"

[store.postgresql]
# In production, inject the DSN with OPENSANDBOX_STORE_POSTGRESQL_DSN instead.
dsn = "postgresql://user:password@localhost:5432/opensandbox"
```


Restart the server. Snapshot lookups and restore requests now read the shared PostgreSQL catalog, including the migrated records.


## Verify


- `GET /v1/sandboxes/{id}/snapshots` returns the migrated snapshot records.
- Restoring a sandbox with an existing `snapshotId` succeeds.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/reference/snapshot-store-migration.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/sdks/csharp`

# OpenSandbox SDK for C#
## Installation ​
## Quick Start ​
## Lifecycle Hooks ​
## Usage Examples ​
*Pause is asynchronous and runtime-dependent. See Pause and Resume.*

*Create a non-expiring sandbox by setting ManualCleanup = true:*

*Use SandboxManager for administrative tasks and finding existing sandboxes.*

## Snapshots, templates, and metadata ​
*Use an existing template after its build reaches Succeeded:*

## Configuration ​
*The ConnectionConfig class manages API server connection settings.*

*Sandbox.CreateAsync() allows configuring the sandbox environment.*

*See Credential Vault for auth types, binding guidance, and Git/curl examples.*

## Error Handling ​
## Supported Frameworks ​
## License ​











A C# SDK for low-level interaction with OpenSandbox. It provides the ability to create, manage, and interact with secure sandbox environments, including executing shell commands, managing files, and reading resource metrics.


## Installation


### NuGet

bash

```
dotnet add package Alibaba.OpenSandbox
```


### Package Manager

powershell

```
Install-Package Alibaba.OpenSandbox
```


## Quick Start


Run this example in a .NET 8+ console project with implicit usings enabled. It creates a sandbox, runs a shell command, and releases remote and local resources.


TIP


Before running this example, ensure the OpenSandbox service is running. See the [Getting Started](https://open-sandbox.ai/getting-started/) guide for startup instructions.

csharp

```
using OpenSandbox;
using OpenSandbox.Config;
using OpenSandbox.Core;

var config = new ConnectionConfig(new ConnectionConfigOptions
{
    Domain = "api.opensandbox.io",
    ApiKey = "your-api-key",
    // Protocol = ConnectionProtocol.Https,
    // RequestTimeoutSeconds = 60,
});

try
{
    await using var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
    {
        ConnectionConfig = config,
        Image = "ubuntu",
        TimeoutSeconds = 10 * 60,
    });

    try
    {
        var execution = await sandbox.Commands.RunAsync("echo 'Hello Sandbox!'");
        Console.WriteLine(execution.Logs.Stdout.FirstOrDefault()?.Text);
    }
    finally
    {
        await sandbox.KillAsync();
    } // await using releases the client even if KillAsync fails.
}
catch (SandboxException ex)
{
    Console.Error.WriteLine($"Sandbox Error: [{ex.Error.Code}] {ex.Error.Message}");
    Console.Error.WriteLine($"Request ID: {ex.RequestId}");
}
```


## Lifecycle Hooks


Set `Lifecycle` in `SandboxCreateOptions`. `PreStart` completes before the entrypoint starts, while `Periodic` hooks run on their schedules after startup.

csharp

```
using OpenSandbox.Models;

await using var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "ubuntu:24.04",
    Lifecycle = new SandboxLifecycle
    {
        PreStart = new LifecycleHook
        {
            Command = new[] { "sh", "-c", "echo ready > /tmp/prestart.done" },
            TimeoutSeconds = 120,
        },
        Periodic = new[]
        {
            new PeriodicLifecycleHook
            {
                Name = "checkpoint",
                Schedule = "@every 5m",
                Command = new[] { "sh", "-c", "date -u >> /tmp/checkpoints.log" },
                TimeoutSeconds = 120,
            },
        },
    },
});
```


The Server validates `TimeoutSeconds`; `PreStart` accepts 1–10800 seconds, while `Periodic` accepts 1–300 seconds. Both default to 60 seconds when omitted. See [Lifecycle Hooks](https://open-sandbox.ai/guides/lifecycle-hooks) for timing, failure behavior, and provider limitations.


### Idle policy (auto-pause and wake-on-access)


`SandboxLifecycle.IdlePolicy` (OSEP-0024, fast-sandbox only) tells the control plane to auto-pause the sandbox after `IdleTimeoutSeconds` (30–86400) of continuously idle ingress-observed traffic, and to wake it on the next request. It is control-plane state: it never reaches the guest, is accepted in template mode (`SandboxCreateFromTemplateOptions.IdlePolicy`), and is rejected by non-fast-sandbox backends. Omitting it preserves non-automated behavior exactly.

csharp

```
var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "ubuntu:24.04",
    Lifecycle = new SandboxLifecycle
    {
        IdlePolicy = new IdlePolicy
        {
            IdleTimeoutSeconds = 300,
            OnIdle = OnIdleAction.Pause,
            WakeOnAccess = true
        }
    }
});
```


`ActiveProbe` lets the application veto a pause while real work runs without producing ingress traffic: declare an endpoint answering `{"active": bool, "message"?: string}` and the server polls it when the sandbox is otherwise idle; a busy answer resets the idle clock. Invalid policies fail fast client-side through `IdlePolicy.Validate()`.


### Wake retry


A request to a paused sandbox may arrive while its restore is still in progress. The gateway answers `503` with the `OpenSandbox-Wake: expired` header; the HTTP transport recognizes it and resends the original request after the `Retry-After` delay (safe for any method — the marker proves the request was never forwarded). The wake budget defaults to 5 attempts / 60 seconds across all wake cycles; when it is exhausted the SDK throws `SandboxWakeTimeoutException` (carrying `Attempts` and `Waited`) while the server-side resume continues in the background. Bare `503` responses follow the existing rules untouched. Tune it on the connection config: `WakeRetryEnabled` (default true), `WakeMaxAttempts` (5), `WakeOverallDeadlineSeconds` (60, non-positive for unbounded). SSE and file stream transports bypass wake retry.


## Usage Examples


The snippets below use `config` and a live `sandbox` from the quick start. Run them before its cleanup block, with `using OpenSandbox.Models;` at the top of the file. Creation examples are alternatives. `await using` releases local clients; call `KillAsync()` to terminate sandboxes that are no longer needed.


### 1. Lifecycle Management


Manage the sandbox lifecycle, including renewal, pausing, and resuming.

csharp

```
var info = await sandbox.GetInfoAsync();
Console.WriteLine($"State: {info.Status.State}");
Console.WriteLine($"Created: {info.CreatedAt}");
Console.WriteLine($"Expires: {info.ExpiresAt}"); // null when manual cleanup mode is used

await sandbox.PauseAsync();

using var pauseBudget = new CancellationTokenSource(TimeSpan.FromMinutes(2));
while (true)
{
    var current = await sandbox.GetInfoAsync(pauseBudget.Token);
    if (current.Status.State == SandboxStates.Paused) break;
    if (current.Status.State == "Failed")
        throw new InvalidOperationException(current.Status.Message);
    await Task.Delay(1000, pauseBudget.Token);
}

// Resume returns a fresh local handle.
await using var resumed = await sandbox.ResumeAsync();

// Renew: expiresAt = now + timeoutSeconds
await resumed.RenewAsync(30 * 60);
```


Pause is asynchronous and runtime-dependent. See [Pause and Resume](https://open-sandbox.ai/guides/pause-resume).


Create a non-expiring sandbox by setting `ManualCleanup = true`:

csharp

```
var manual = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "ubuntu",
    ManualCleanup = true,
});
```


INFO


`TimeoutSeconds = null` uses the default TTL. Set `ManualCleanup = true` to disable automatic expiration.


### Connect to an Existing Sandbox


Use `ConnectAsync` when you already have a sandbox ID and need a new SDK instance bound to it.

csharp

```
await using var connected = await Sandbox.ConnectAsync(new SandboxConnectOptions
{
    SandboxId = "existing-sandbox-id",
    ConnectionConfig = config
});
```


### 2. Custom Health Check


Resolving an endpoint confirms that a route exists; it does not confirm that the application on that port is healthy. For service readiness, make a bounded request to the application's health endpoint and include the returned endpoint headers.


Define custom logic to determine whether the sandbox is ready/healthy.

csharp

```
using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(2) };
await using var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "nginx:latest",
    Entrypoint = new[] { "nginx", "-g", "daemon off;" },
    HealthCheck = async (sbx) =>
    {
        var ep = await sbx.GetEndpointAsync(80);
        using var request = new HttpRequestMessage(HttpMethod.Get, await sbx.GetEndpointUrlAsync(80));
        foreach (var header in ep.Headers)
            request.Headers.TryAddWithoutValidation(header.Key, header.Value);
        try
        {
            using var response = await http.SendAsync(request);
            return response.StatusCode == System.Net.HttpStatusCode.OK;
        }
        catch (HttpRequestException) { return false; }
        catch (TaskCanceledException) { return false; }
    },
});
```


### 3. Command Execution & Streaming


Execute commands and handle output streams in real-time.

csharp

```
using OpenSandbox.Models;

var handlers = new ExecutionHandlers
{
    OnStdout = msg => { Console.WriteLine($"STDOUT: {msg.Text}"); return Task.CompletedTask; },
    OnStderr = msg => { Console.Error.WriteLine($"STDERR: {msg.Text}"); return Task.CompletedTask; },
    OnExecutionComplete = c => { Console.WriteLine($"Finished in {c.ExecutionTimeMs}ms"); return Task.CompletedTask; },
};

await sandbox.Commands.RunAsync(
    "for i in 1 2 3; do echo \"Count $i\"; sleep 0.2; done",
    handlers: handlers
);
```


To execute a native program without shell parsing, pass an argument list. On Linux, this example prints literal `$HOME` and keeps `hello world` as one argument:

csharp

```
await sandbox.Commands.RunAsync(new[] { "printf", "%s\n", "$HOME", "hello world" });
```


Native argv execution requires an updated execd. See [command execution modes](https://open-sandbox.ai/architecture/data-plane/execd#command-execution) for executable lookup and platform behavior.


#### Background commands


Poll status and incremental logs. Command timeout is separate from sandbox TTL.

csharp

```
var execution = await sandbox.Commands.RunAsync(
    "for i in 1 2 3; do echo step-$i; sleep 1; done",
    options: new RunCommandOptions
    {
        Background = true,
        TimeoutSeconds = 30,
    });

var commandId = execution.Id ?? throw new InvalidOperationException("No command ID returned");
long cursor = 0;
using var budget = new CancellationTokenSource(TimeSpan.FromSeconds(45));
try
{
    while (true)
    {
        var status = await sandbox.Commands.GetCommandStatusAsync(commandId, budget.Token);
        var logs = await sandbox.Commands.GetBackgroundCommandLogsAsync(commandId, cursor, budget.Token);
        Console.Write(logs.Content);
        cursor = logs.Cursor ?? cursor;
        if (status.Running == false)
        {
            if (status.ExitCode != 0)
                throw new InvalidOperationException($"Command failed: {status.ExitCode}, {status.Error}");
            break;
        }
        await Task.Delay(500, budget.Token);
    }
}
catch (OperationCanceledException) when (budget.IsCancellationRequested)
{
    await sandbox.Commands.InterruptAsync(commandId);
    throw;
}
```


#### Persistent shell sessions


A Bash session preserves shell variables and the working directory across commands.

csharp

```
var sessionId = await sandbox.Commands.CreateSessionAsync(
    new CreateSessionOptions { WorkingDirectory = "/tmp" });
try
{
    await sandbox.Commands.RunInSessionAsync(sessionId, "export DEMO=hello");
    var result = await sandbox.Commands.RunInSessionAsync(sessionId, "echo \"$DEMO\"; pwd");
    foreach (var message in result.Logs.Stdout) Console.Write(message.Text);
}
finally
{
    await sandbox.Commands.DeleteSessionAsync(sessionId);
}
```


#### Persistent environment variables


Set environment variables that the runtime injects into every subsequent command and session — without hand-writing shell escaping against the sandbox env file.

csharp

```
await sandbox.Commands.SetEnvAsync("MY_TOKEN", "it's a safe value");
```


Keys must match `[A-Za-z_][A-Za-z0-9_]*`. Values without a single quote are stored verbatim; values containing a single quote use the env file's double-quoted form, in which shell-style `$NAME` sequences may be expanded when the runtime loads the file. The env file is append-only: the last write for a key wins. Throws `SandboxException` if the sandbox fails to persist the variable.


For filesystem/process isolation within a sandbox, see [Isolation Sessions](https://open-sandbox.ai/guides/isolation-sessions). These are separate from Bash sessions.


### 4. File Operations


Manage files and directories, including read, write, list/search, and delete.

csharp

```
await sandbox.Files.CreateDirectoriesAsync(new[]
{
    new CreateDirectoryEntry { Path = "/tmp/demo", Mode = 755 }
});

await sandbox.Files.WriteFilesAsync(new[]
{
    new WriteEntry { Path = "/tmp/demo/hello.txt", Data = "Hello World", Mode = 644 }
});

var content = await sandbox.Files.ReadFileAsync("/tmp/demo/hello.txt");
Console.WriteLine($"Content: {content}");

var entries = await sandbox.Files.ListDirectoryAsync("/tmp/demo", depth: 1);
foreach (var entry in entries) Console.WriteLine(entry.Path);

var files = await sandbox.Files.SearchAsync(new SearchEntry { Path = "/tmp/demo", Pattern = "*.txt" });
foreach (var file in files)
{
    Console.WriteLine(file.Path);
}

await sandbox.Files.DeleteFilesAsync(new[] { "/tmp/demo/hello.txt" });
await sandbox.Files.DeleteDirectoriesAsync(new[] { "/tmp/demo" });
```


For binary data, use `byte[]` or `Stream` in `WriteEntry.Data`, and download with `ReadBytesAsync()` or `ReadBytesStreamAsync()`. Read options support partial downloads.


#### File operations with an explicit identity


Bind a filesystem client to a Linux UID and GID:

csharp

```
var files = sandbox.FilesWithIdentity(1001, 2000);
```


The bound client exposes the usual file operations and shares the sandbox connection, authentication, and endpoint routing headers. The existing file client retains its default identity. Select the UID/GID separately for command execution.


This requires Linux and an Execd version that supports filesystem execution identity. Unsupported servers return an error; requests never fall back to the default filesystem routes. Keep sandbox credentials and identity selection in the trusted backend. Linux filesystem permissions apply; this feature does not create a tenant isolation boundary. See [Execd](https://open-sandbox.ai/architecture/data-plane/execd) for permission and workspace provisioning details.


### 5. Endpoints


`GetEndpointAsync()` returns an endpoint **without a scheme** (for example `"localhost:44772"`). Use `GetEndpointUrlAsync()` if you want a ready-to-use absolute URL.

csharp

```
var endpoint = await sandbox.GetEndpointAsync(44772);
Console.WriteLine(endpoint.EndpointAddress);

var url = await sandbox.GetEndpointUrlAsync(44772);
Console.WriteLine(url); // e.g., "http://localhost:44772"
```


Forward `endpoint.Headers` on requests to the sandbox service, including any secure-access credentials. The health-check example above shows an HTTP request to an application listening on the target port.


### 6. Sandbox Management (Admin)


Use `SandboxManager` for administrative tasks and finding existing sandboxes.

csharp

```
await using var manager = SandboxManager.Create(new SandboxManagerOptions
{
    ConnectionConfig = config
});

var list = await manager.ListSandboxInfosAsync(new SandboxFilter
{
    States = new[] { SandboxStates.Running },
    Page = 1, // First page only; increase for subsequent pages.
    PageSize = 10
});

foreach (var s in list.Items)
{
    Console.WriteLine(s.Id);
}
```


### Resource metrics


Read current sandbox resource usage with `await sandbox.Metrics.GetMetricsAsync()`. This is separate from [SDK creation telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


## Snapshots, templates, and metadata


| Operation | Public API |
| --- | --- |
| Snapshot a sandbox | `sandbox.CreateSnapshotAsync` or `manager.CreateSnapshotAsync` |
| Inspect/list/delete snapshots | `manager.GetSnapshotAsync`, `ListSnapshotsAsync`, `DeleteSnapshotAsync` |
| Restore a snapshot | `Sandbox.CreateAsync` with `SnapshotId` and no `Image` / `Entrypoint` |
| Manage Fsb templates | `manager.CreateTemplateAsync`, `GetTemplateAsync`, `ListTemplatesAsync`, `DeleteTemplateAsync` |
| Create from a published template | `Sandbox.CreateFromTemplateAsync` with `SandboxCreateFromTemplateOptions` |
| Patch metadata | `sandbox.PatchMetadataAsync` or `manager.PatchSandboxMetadataAsync` |


Poll snapshot status before restoring. Template builds are asynchronous; wait for `Succeeded` before use. Template-backed creation requires `TimeoutSeconds` and inherits workload configuration from the published template. Metadata patch values add/replace keys; `null` deletes a key. See the [lifecycle contract](https://open-sandbox.ai/api/#1-sandbox-lifecycle-yml) for backend constraints.


Snapshot support depends on the runtime and server configuration. Renew the source sandbox first if its remaining TTL may expire during snapshot creation. This example waits up to 15 minutes and retains the snapshot for reuse:

csharp

```
await using var manager = SandboxManager.Create(new SandboxManagerOptions { ConnectionConfig = config });
var snapshot = await sandbox.CreateSnapshotAsync("demo");
Console.WriteLine($"Snapshot: {snapshot.Id}");
using var budget = new CancellationTokenSource(TimeSpan.FromMinutes(15));
while (true)
{
    snapshot = await manager.GetSnapshotAsync(snapshot.Id, budget.Token);
    if (snapshot.Status.State == "Ready") break;
    if (snapshot.Status.State == "Failed")
        throw new InvalidOperationException(snapshot.Status.Message);
    await Task.Delay(2000, budget.Token);
}
await using var restored = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    SnapshotId = snapshot.Id,
    ConnectionConfig = config,
});
try { Console.WriteLine(restored.Id); }
finally { await restored.KillAsync(); }
// When no longer needed: await manager.DeleteSnapshotAsync(snapshot.Id);
```


Use an existing template after its build reaches `Succeeded`:

csharp

```
await using var templated = await Sandbox.CreateFromTemplateAsync(new SandboxCreateFromTemplateOptions
{
    TemplateId = "your-published-template-id",
    TimeoutSeconds = 600,
    ConnectionConfig = config,
});
```


Add/replace a metadata key and remove another:

csharp

```
await sandbox.PatchMetadataAsync(new Dictionary<string, string?>
{
    ["project"] = "demo",
    ["obsolete-key"] = null,
});
```


## Configuration


### 1. Connection Configuration


The `ConnectionConfig` class manages API server connection settings.


Transfer timeouts


`RequestTimeoutSeconds` bounds the wait for response headers, not the whole transfer. The deadline starts with the request (so the connect phase is bounded too), is cleared while the request body is written, and is re-armed once the body of the current hop has been sent: a healthy upload or download that keeps making progress is never cut off by it. A download that gets no response headers, or an upload that gets none within the timeout after its body has been sent, fails with a `TaskCanceledException` carrying a `TimeoutException` instead of hanging (the Go SDK's `ResponseHeaderTimeout` contract); a caller cancellation still surfaces as an `OperationCanceledException` with the caller's token. All non-transfer calls keep the whole-call request timeout.


A request body that never finishes being sent, and a response body that stops making progress after the headers have arrived, are bounded only by the `CancellationToken` you pass to the call, so pass one when a transfer needs an end-to-end cap. The upload guarantee assumes the HTTP handler streams the request body (for example `SocketsHttpHandler` on .NET 5+): the default `HttpClientHandler` on .NET Framework buffers the request body before sending it, so a slow but progressing upload can still count against the header timeout there.


A 307/308 redirect resends the request body once per hop. A seekable upload source (`FileStream`, `MemoryStream`, ...) is rewound and resent in full; a non-seekable source cannot be replayed without buffering it, so the upload fails with a clear error instead of sending an empty file part to the redirected endpoint.


| Parameter | Description | Default | Environment Variable |
| --- | --- | --- | --- |
| `ApiKey` | API key for authentication | Optional | `OPEN_SANDBOX_API_KEY` |
| `Domain` | Sandbox service domain (`host[:port]`) | `localhost:8080` | `OPEN_SANDBOX_DOMAIN` |
| `Protocol` | HTTP protocol (`Http` / `Https`) | `Http` | - |
| `RequestTimeoutSeconds` | Request timeout applied to SDK HTTP calls | `30` | - |
| `UseServerProxy` | Request server-proxied sandbox endpoint URLs | `false` | - |
| `Headers` | Extra headers applied to every request | `{}` | - |
| `DisableMetrics` | Disable SDK create-latency telemetry (see [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics)) | `false` | `OPENSANDBOX_DISABLE_METRICS` |

csharp

```
using OpenSandbox.Config;

// 1. Basic configuration
var config = new ConnectionConfig(new ConnectionConfigOptions
{
    Domain = "api.opensandbox.io",
    ApiKey = "your-key",
    RequestTimeoutSeconds = 60,
    // UseServerProxy = true, // Useful when the client cannot access sandbox endpoint directly
});

// 2. Advanced: custom headers
var config2 = new ConnectionConfig(new ConnectionConfigOptions
{
    Domain = "api.opensandbox.io",
    ApiKey = "your-key",
    Headers = new Dictionary<string, string>
    {
        ["X-Custom-Header"] = "value"
    },
});
```


SDK Telemetry


`Sandbox.CreateAsync` reports create latency to `POST /v1/metrics/events` by default. Set `ConnectionConfigOptions.DisableMetrics = true` or export `OPENSANDBOX_DISABLE_METRICS=1` to opt out. See [SDK Telemetry](https://open-sandbox.ai/sdks/observability#creation-metrics).


### 2. SDK Logging


The SDK uses `Microsoft.Extensions.Logging` abstractions. `SdkDiagnosticsOptions` configures local logging; it does not retrieve remote sandbox diagnostic logs or events. Use the [CLI or HTTP API](https://open-sandbox.ai/api/#diagnostics) for those. Client Pool and built-in pool warmup tracing are not currently available in C#. Install `Microsoft.Extensions.Logging.Console` to use `AddConsole()` below.

csharp

```
using Microsoft.Extensions.Logging;
using OpenSandbox.Config;

using var loggerFactory = LoggerFactory.Create(builder =>
{
    builder.SetMinimumLevel(LogLevel.Debug);
    builder.AddConsole();
});

var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    Image = "python:3.11",
    ConnectionConfig = new ConnectionConfig(),
    Diagnostics = new SdkDiagnosticsOptions
    {
        LoggerFactory = loggerFactory
    }
});
```


### 3. Sandbox Creation Configuration


`Sandbox.CreateAsync()` allows configuring the sandbox environment.


| Parameter | Description | Default |
| --- | --- | --- |
| `Image` | Docker image to use | One of image or snapshot ID |
| `TimeoutSeconds` | Automatic termination timeout (server-side TTL) | 10 minutes |
| `Entrypoint` | Container entrypoint command | `["tail","-f","/dev/null"]` |
| `Resource` | CPU and memory limits (string map) | `{"cpu":"1","memory":"2Gi"}` |
| `Env` | Environment variables | `{}` |
| `Metadata` | Custom metadata tags | `{}` |
| `NetworkPolicy` | Optional outbound network policy (egress) | - |
| `CredentialProxy` | Optional Credential Vault proxy startup settings | - |
| `Volumes` | Optional storage mounts (`Host` / `PVC` / `OSSFS`, supports `ReadOnly` and `SubPath`) | - |
| `Extensions` | Extra server-defined fields | `{}` |
| `SkipHealthCheck` | Skip readiness checks (`Running` + health check) | `false` |
| `HealthCheck` | Custom readiness check | - |
| `ReadyTimeoutSeconds` | Max time to wait for readiness | 30 seconds |
| `HealthCheckPollingInterval` | Poll interval while waiting (milliseconds) | 200 ms |
| `SnapshotId` | Restore a snapshot instead of passing `Image`; omit `Entrypoint` | - |
| `ResourceRequests` | Kubernetes resource requests; must not exceed limits | - |
| `Lifecycle` | Pre-start and periodic hooks | - |
| `Platform` | OS/architecture constraint | - |
| `SecureAccess` | Require endpoint access credentials | `false` |
| `ManualCleanup` | Disable TTL expiration for image/snapshot creation | `false` |


WARNING


Metadata keys under `opensandbox.io/` are reserved for system-managed labels and will be rejected by the server.

csharp

```
var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "python:3.11",
    NetworkPolicy = new NetworkPolicy
    {
        DefaultAction = NetworkRuleAction.Deny,
        Egress = new List<NetworkRule>
        {
            new() { Action = NetworkRuleAction.Allow, Target = "pypi.org" }
        }
    },
    Volumes = new[]
    {
        new Volume
        {
            Name = "workspace",
            Host = new Host { Path = "/tmp/opensandbox-e2e/host-volume-test" },
            MountPath = "/workspace",
            ReadOnly = false
        }
    }
});
```


### 4. Runtime Egress Policy Updates


Runtime egress policy routing depends on the sandbox origin. For image-backed sandboxes, the SDK resolves port `18080` and calls the sidecar `/policy` API. For template-backed sandboxes (including restored template snapshots), the SDK detects `OPEN-SANDBOX-ORIGIN: template` and routes policy operations through the lifecycle `/sandboxes/{sandboxId}/networkpolicy` API.


Patch uses merge semantics:


- Incoming rules take priority over existing rules with the same `Target`.
- Existing rules for other targets remain unchanged.
- Within a single patch payload, the first rule for a `Target` wins.
- The current `DefaultAction` is preserved.

csharp

```
var policy = await sandbox.GetEgressPolicyAsync();

await sandbox.PatchEgressRulesAsync(new[]
{
    new NetworkRule { Action = NetworkRuleAction.Allow, Target = "www.github.com" },
    new NetworkRule { Action = NetworkRuleAction.Deny, Target = "pypi.org" }
});
```


### 5. Credential Vault


Credential Vault requires a sandbox-side egress service and is unavailable for template-backed sandboxes. It injects outbound credentials from the egress sidecar while keeping real secrets out of sandbox environment variables, commands, files, and logs. Create the sandbox with `CredentialProxy` enabled, then write credentials and bindings through `sandbox.CredentialVault` or the sandbox helper methods.

csharp

```
var sandbox = await Sandbox.CreateAsync(new SandboxCreateOptions
{
    ConnectionConfig = config,
    Image = "python:3.11",
    NetworkPolicy = new NetworkPolicy
    {
        DefaultAction = NetworkRuleAction.Deny,
        Egress = new List<NetworkRule>
        {
            new() { Action = NetworkRuleAction.Allow, Target = "api.example.com" }
        }
    },
    CredentialProxy = new CredentialProxyConfig { Enabled = true }
});

await sandbox.CreateCredentialVaultAsync(
    new[]
    {
        new Credential
        {
            Name = "api-token",
            Source = new InlineCredentialSource { Value = "<token>" }
        }
    },
    new[]
    {
        new CredentialBinding
        {
            Name = "api-token",
            Match = new CredentialMatch
            {
                Schemes = new[] { "https" },
                Hosts = new[] { "api.example.com" },
                Paths = new[] { "/v1/*" }
            },
            Auth = new CredentialAuth
            {
                Type = "apiKey",
                Name = "x-api-key",
                Credential = "api-token"
            }
        }
    });
```


See [Credential Vault](https://open-sandbox.ai/guides/credential-vault) for auth types, binding guidance, and Git/curl examples.


### 6. Timeout and Retry Behavior


- `ConnectionConfig.RequestTimeoutSeconds` controls timeout for SDK HTTP calls. File uploads and downloads are exempt while they keep making progress; the timeout still bounds the connect phase and how long a transfer waits for response headers before failing.
- `RunCommandOptions.TimeoutSeconds` controls command execution timeout for command runs.
- `RunInSessionOptions.TimeoutSeconds` controls command execution timeout for session runs.
- `SandboxCreateOptions.TimeoutSeconds` controls sandbox server-side TTL.
- `ReadyTimeoutSeconds` controls readiness waits. For `ConnectAsync` / `ResumeAsync`, endpoint discovery and health checks share this timeout. Blocking custom code can delay timeout reporting.
- The SDK does not automatically retry failed API requests; implement retries in caller code where appropriate.


### 7. Resource Cleanup


Both `Sandbox` and `SandboxManager` implement `IAsyncDisposable`. Use `await using` or call `DisposeAsync()` when done.

csharp

```
await using var sandbox = await Sandbox.CreateAsync(options);
// ... use sandbox ...
// Automatically disposed when leaving scope
```


## Error Handling


The SDK throws `SandboxException` (and derived exceptions such as `SandboxApiException`, `SandboxReadyTimeoutException`, and `InvalidArgumentException`) when operations fail.

csharp

```
try
{
    var execution = await sandbox.Commands.RunAsync("echo 'Hello Sandbox!'");
    Console.WriteLine(execution.Logs.Stdout.FirstOrDefault()?.Text);
}
catch (SandboxReadyTimeoutException)
{
    Console.Error.WriteLine("Sandbox did not become ready before the configured timeout.");
}
catch (SandboxApiException ex)
{
    Console.Error.WriteLine($"API Error: status={ex.StatusCode}, requestId={ex.RequestId}, message={ex.Message}");
}
catch (SandboxException ex)
{
    Console.Error.WriteLine($"Sandbox Error: [{ex.Error.Code}] {ex.Error.Message}");
}
```


## Supported Frameworks


- .NET Standard 2.0 (for maximum compatibility with .NET Framework 4.6.1+, .NET Core 2.0+, Mono, Xamarin, etc.)
- .NET Standard 2.1
- .NET 6.0
- .NET 7.0
- .NET 8.0
- .NET 9.0
- .NET 10.0


## License


Apache License 2.0[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/sdks/csharp.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/gemini-cli`

Return to top

# Gemini CLI Example


Call Google Gemini via the `@google/gemini-cli` npm package in OpenSandbox.


## Start OpenSandbox server [local]
*Call Google Gemini via the @google/gemini-cli npm package in OpenSandbox.*

## Start OpenSandbox server [local] ​
## Create and Access the Gemini Sandbox ​
## Environment Variables ​
## References ​






Pre-pull the code-interpreter image (includes Node.js):

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use docker hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


Start the local OpenSandbox server, logs will be visible in the terminal:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the Gemini Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

# Run the example (requires SANDBOX_DOMAIN / SANDBOX_API_KEY / GEMINI_API_KEY)
uv run python examples/gemini-cli/main.py
```


The script installs the Gemini CLI (`npm install -g @google/gemini-cli@latest`) at runtime (Node.js is already in the code-interpreter image), then sends a simple request `gemini "Compute 1+1=?."`. Auth is passed via `GEMINI_API_KEY`; you can override endpoint/model with `GEMINI_BASE_URL` / `GEMINI_MODEL`.


## Environment Variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional for local)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |
| `GEMINI_API_KEY` | *(required)* | Your Google Gemini API key |
| `GEMINI_BASE_URL` | *(optional)* | Gemini API endpoint (e.g., proxy) |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Model to use |


## References


- [@google/gemini-cli](https://www.npmjs.com/package/@google/gemini-cli) - Gemini CLI
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/gemini-cli)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/gemini-cli.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/qwen-code`

Return to top

# Qwen Code Example


Run [Qwen Code](https://github.com/QwenLM/qwen-code) inside an OpenSandbox container through an OpenAI-compatible endpoint.


## Start OpenSandbox server [local]
## Start OpenSandbox server [local] ​
## Create and Access the Qwen Sandbox ​
## Environment Variables ​
## References ​






Pre-pull the code-interpreter image (includes Node.js):

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use docker hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


Then start the local OpenSandbox server, stdout logs will be visible in the terminal:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the Qwen Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

# Export provider settings
export API_KEY=your-api-key
export BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
export MODEL_NAME=qwen3-coder-plus

# Run the example
uv run python examples/qwen-code/main.py
```


The script installs Qwen Code (`npm install -g @qwen-code/qwen-code@latest`) at runtime, writes a project-local `.qwen/settings.json` inside the sandbox, and runs `qwen -p "Compute 1+1 and reply with only the final number."` in headless mode. The API key is injected only through the `API_KEY` environment variable and is not written into the repository.


## Environment Variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional for local)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |
| `API_KEY` | *(required)* | API key for the OpenAI-compatible provider used by Qwen Code |
| `BASE_URL` | `https://dashscope.aliyuncs.com/compatible-mode/v1` | OpenAI-compatible base URL |
| `MODEL_NAME` | `qwen3-coder-plus` | Model name for Qwen Code |


## References


- [Qwen Code](https://github.com/QwenLM/qwen-code) - Official repository
- [Qwen Code Authentication](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/) - Provider configuration reference
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/qwen-code)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/qwen-code.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/codex-cli`

Return to top

# Codex/OpenAI CLI Example


Use the official `@openai/codex` npm package to call OpenAI/Codex-like models in OpenSandbox.


## Start OpenSandbox server [local]
## Start OpenSandbox server [local] ​
## Create and Access the Codex Sandbox ​
## Multi-Turn Sessions: Resume a Previous Run ​
## Sandbox and Approval Modes ​
## Environment Variables ​
## References ​








Pre-pull the code-interpreter image (includes Node.js):

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use docker hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


Start the local OpenSandbox server, logs will be visible in the terminal:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the Codex Sandbox

shell

```
# Install OpenSandbox package
uv pip install opensandbox

# Run the example (requires SANDBOX_DOMAIN / SANDBOX_API_KEY / OPENAI_API_KEY)
uv run python examples/codex-cli/main.py
```


The script installs the Codex CLI (`npm install -g @openai/codex@latest`) at runtime (Node.js is already in the code-interpreter image), then executes a simple request `codex exec "Compute 1+1 and return JSON with keys result and reasoning." --skip-git-repo-check`. Auth is passed via `OPENAI_API_KEY`; you can override endpoint/model with `OPENAI_BASE_URL` / `OPENAI_MODEL`.


## Multi-Turn Sessions: Resume a Previous Run


Each `codex exec` run is a session. For pipelines that need a follow-up turn (review → fix, plan → implement), resume the session instead of starting over with a fresh context.


Turn 1 — run with `--json` and capture the session id. `--json` turns stdout into a JSON Lines (JSONL) event stream; the first event, `thread.started`, carries the `thread_id`, which is the session id that `codex exec resume` accepts:

shell

```
codex exec --json "Remember this for later: my favorite sandbox number is 42." --skip-git-repo-check
```

json

```
{"type": "thread.started", "thread_id": "0199a213-81c0-7800-8aa1-bbab2a035a53"}
```


Turn 2 — resume that session with a follow-up prompt; the model recalls the context of the previous turns, so the reply is `42`:

shell

```
codex exec resume "0199a213-81c0-7800-8aa1-bbab2a035a53" "What is my favorite sandbox number? Reply with just the number." --skip-git-repo-check
```


TIP


`codex exec resume --last "..."` continues the most recent session from the current working directory — convenient for quick two-stage pipelines. The example script captures the explicit id instead, which stays correct when several sessions interleave.


If you only need the final message for a downstream step, `-o <path>` / `--output-last-message <path>` writes it to a file, and `--output-schema <file>` validates the final response against a JSON Schema.


## Sandbox and Approval Modes


Codex applies its own sandbox policy to model-generated shell commands; these flags control it inside the OpenSandbox container:


- `--sandbox workspace-write` (or `-s workspace-write`) lets model-generated commands write inside the workspace — the usual choice for autonomous runs.
- `--sandbox read-only` keeps the run strictly read-only.
- `-a never` / `--ask-for-approval never` never pauses for human approval, so a non-interactive run cannot block on a person.
- `--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`) runs every command without approvals or sandboxing. The Codex CLI documents it as safe only "inside an externally hardened environment" — in OpenSandbox terms, that means a sandbox running a hardened runtime (gVisor, Kata), not the default runc; see [Secure Container Runtimes](https://open-sandbox.ai/guides/secure-container).


WARNING


`--full-auto` is deprecated — prefer `--sandbox workspace-write`; Codex prints a warning when the old flag is used.


## Environment Variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional for local)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |
| `OPENAI_API_KEY` | *(required)* | Your OpenAI API key |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` | OpenAI API endpoint |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model to use |


## References


- [@openai/codex](https://www.npmjs.com/package/@openai/codex) - Official OpenAI Codex CLI
- [Codex non-interactive mode](https://developers.openai.com/codex/noninteractive) - `codex exec`, JSONL output, and session resume
- [Codex CLI reference](https://developers.openai.com/codex/cli/reference) - Sandbox and approval flags
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/codex-cli)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/codex-cli.md)

[Next pageApply Model Patches](https://open-sandbox.ai/examples/apply-patch)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/opencode`

Return to top

# OpenCode Example


Run [OpenCode](https://opencode.ai/) inside an OpenSandbox container. The example installs the official CLI and executes a prompt non-interactively with `opencode run`.


## Start OpenSandbox server [local]
## Start OpenSandbox server [local] ​
## Create and Access the OpenCode Sandbox ​
## Environment Variables ​
## References ​






Pre-pull the code-interpreter image (includes Node.js):

shell

```
docker pull sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0

# use Docker Hub
# docker pull opensandbox/code-interpreter:v1.1.0
```


Then start the local OpenSandbox server. Logs will be visible in the terminal:

shell

```
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
opensandbox-server
```


## Create and Access the OpenCode Sandbox

shell

```
# Install the OpenSandbox package
uv pip install opensandbox

# Run the example. The default free model does not require an API key.
uv run python examples/opencode/main.py
```


The script installs OpenCode (`npm install -g opencode-ai@latest`) at runtime, creates an isolated working directory, and runs `opencode run` with a simple prompt. The default model is currently available without authentication. Set `OPENCODE_API_KEY` and `OPENCODE_MODEL` to use an authenticated model from the OpenCode provider instead.


## Environment Variables


| Variable | Default | Description |
| --- | --- | --- |
| `SANDBOX_DOMAIN` | `localhost:8080` | Sandbox service address |
| `SANDBOX_API_KEY` | *(optional for local)* | API key if your server requires authentication |
| `SANDBOX_IMAGE` | `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/code-interpreter:v1.1.0` | Sandbox image to use |
| `OPENCODE_MODEL` | `opencode/deepseek-v4-flash-free` | Model ID in `provider/model` format |
| `OPENCODE_API_KEY` | *(optional)* | API key for authenticated models from the OpenCode provider |


INFO


The default free model is offered by OpenCode for a limited time. Do not send private code, credentials, or other confidential data to a free model; review the provider's data-use terms before using it. Override `OPENCODE_MODEL` when you need a different model. Other providers may require additional environment variables or configuration.


## References


- [OpenCode CLI](https://opencode.ai/docs/cli/) - Installation and non-interactive `run` command
- [OpenCode Providers](https://opencode.ai/docs/providers) - Provider authentication and configuration
- [OpenCode Zen](https://opencode.ai/docs/zen/) - Model availability and data-use notes
- [Source code on GitHub](https://github.com/opensandbox-group/OpenSandbox/tree/main/examples/opencode)[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/opencode.md)

[Previous pageApply Model Patches](https://open-sandbox.ai/examples/apply-patch)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration

---

# OpenSandbox Documentation

`https://open-sandbox.ai/examples/apply-patch`

Return to top

# Apply Model Patches


OpenSandbox exposes file operations and command execution, but the default `execd` image does not include a patch interpreter. The `/files/replace` API performs literal string replacement; it does not understand contextual hunks, file creation, deletion, or moves.


If your coding agent emits the patch format used by OpenAI Codex, install the standalone `apply_patch` executable in a custom sandbox image and run it inside the sandbox. This keeps the patch dialect in the agent image instead of adding vendor-specific behavior to the OpenSandbox file API.


## Build a custom image


The following example builds the executable from a pinned Codex revision and copies it into the OpenSandbox `execd` image. Pin `CODEX_REF` to a reviewed commit in production so image builds remain reproducible.

dockerfile

```
FROM rust:alpine AS apply-patch-builder

ARG CODEX_REF=<reviewed-commit>
RUN apk add --no-cache build-base git musl-dev
WORKDIR /src
RUN git clone --depth 1 https://github.com/openai/codex.git . \
    && git fetch --depth 1 origin ${CODEX_REF} \
    && git checkout ${CODEX_REF}
WORKDIR /src/codex-rs
RUN cargo build --release --locked -p codex-apply-patch

FROM opensandbox/execd:v1.1.0
COPY --from=apply-patch-builder /src/codex-rs/target/release/apply_patch /usr/local/bin/apply_patch
RUN chmod 0755 /usr/local/bin/apply_patch
## Build a custom image ​
## Apply a patch from the Python SDK ​
## Operational notes ​



```


Build and publish the image, then use its name when creating the sandbox:

shell

```
docker build --build-arg CODEX_REF=<reviewed-commit> \
  -t my-registry/opensandbox-execd-with-patch:1 .
docker push my-registry/opensandbox-execd-with-patch:1
```


The builder and runtime stages must produce compatible binaries. If your base image is not Alpine, use a builder with the matching C library and toolchain.


## Apply a patch from the Python SDK


Write the model output to a temporary file, then invoke `apply_patch` through the existing command API. The executable accepts either one patch argument or the patch on standard input; using a file avoids shell quoting and argument length problems.


Run the following snippet inside an async function. It assumes `/workspace/hello.py` already exists and contains `print("hello")`.

python

```
import sys

from opensandbox import Sandbox

patch = """*** Begin Patch
*** Update File: /workspace/hello.py
@@
-print("hello")
+print("hello from OpenSandbox")
*** End Patch
"""

async with (await Sandbox.create(image="my-registry/opensandbox-execd-with-patch:1")) as sandbox:
    await sandbox.files.write_file("/tmp/change.patch", patch)
    result = await sandbox.commands.run(
        "cd /workspace && apply_patch < /tmp/change.patch"
    )
    stdout = "".join(message.text for message in result.logs.stdout)
    stderr = "".join(message.text for message in result.logs.stderr)
    print(stdout, end="")
    print(stderr, end="", file=sys.stderr)
    if result.exit_code != 0:
        raise RuntimeError(f"apply_patch failed (exit code: {result.exit_code})")
```


Patch paths are resolved relative to the command working directory unless the patch uses an absolute path. Keep the working directory and patch paths inside the sandbox workspace, and treat patch content as untrusted input from the model.


## Operational notes


- `apply_patch` can add, update, delete, and move files and matches update hunks using surrounding context.
- A failed patch can leave earlier file changes committed. Check the command exit status and inspect the affected files before retrying.
- The default OpenSandbox images remain unchanged. Use the custom image only for agents that need this patch format.
- For agents that already manage their own editing tools, continue using the regular file and command APIs instead of installing this executable.


See the [OpenAPI specifications](https://open-sandbox.ai/api/) and the [Codex CLI example](https://open-sandbox.ai/examples/codex-cli) for the surrounding sandbox setup.[Edit this page on GitHub](https://github.com/opensandbox-group/OpenSandbox/edit/main/docs/examples/apply-patch.md)



## Additional Content

Universal Sandbox Infrastructure for AI Applications

Edit this page on GitHub

Copyright © 2024-present OpenSandbox Contributors

Released under the Apache 2.0 License.

Migration Guides

Implementation Compatibility

Kubernetes Controller

Experimental HTTP/2

Single-Host Network (Docker)

Auto-Pause & Wake-on-Access

Pause, Resume, and Snapshots

High Availability

Enhancement Proposals

Release Automation

Release Verification

Kubernetes Deployment

Apply Model Patches

Browser & Desktop

Code Interpreter

Scheduled Client Pool

Harbor Evaluation

Host Volume Mount

Docker PVC Volume

Docker OSSFS Volume

rclone Volume Mount

Credential Vault

Chained Upstream Proxy

Secure Container

Network Isolation on Kubernetes

Isolation Sessions

Kubernetes Resume Benchmark

Pod Provision Failure Recovery

QEMU VMState Snapshots

Egress SSE Truncation

Node Agent Configuration

Execd Path Migration

Snapshot Store Migration

Code Interpreter Image Migration