# Quickstart - microsandbox

`https://docs.microsandbox.dev/getting-started/quickstart`

# Quickstart
## Documentation Index
## ​Run your first sandbox
## ​What just happened?
## ​Next steps





Get a sandbox running in under 5 minutes.

## [​](https://docs.microsandbox.dev/getting-started/quickstart#run-your-first-sandbox) Run your first sandbox


npx macOS & Linux Windows

```
npx microsandbox run debian
```


```
curl -fsSL https://install.microsandbox.dev | sh
msb run debian
```


```
irm https://install.microsandbox.dev/windows | iex
msb run debian
```


Prefer short commands such as `msb run debian` for everyday use. `msb sandbox run debian` and `msb sbx run debian` do the same thing, with the same flags. Explore the full group with `msb sandbox --help`.
Having trouble with a local installation? Choose your platform for setup checks and fixes.
[**Linux** glibc 2.28+ and KVM](https://docs.microsandbox.dev/troubleshooting/linux) [**macOS** Apple Silicon](https://docs.microsandbox.dev/troubleshooting/macos) [**Windows** 10+ · WHP](https://docs.microsandbox.dev/troubleshooting/windows)
1

Install microsandbox

For application code, install the SDK for your language. For terminal workflows, use one of the CLI options above. Both run microsandbox locally by default; there is no separate server or daemon to set up. The same installation also drives [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview) when an API key is set. TypeScript Rust Python Go Ruby

```
npm install microsandbox
```


```
cargo add microsandbox
```


```
pip install microsandbox
```


```
go get github.com/superradcompany/microsandbox/sdk/go
```


```
gem install microsandbox
```

You can also provision the runtime with the CLI installer above or explicit SDK setup helpers. See [Runtime setup](https://docs.microsandbox.dev/sdk/setup#bring-your-own-runtime) for Node’s bundled binaries and Rust’s opt-out options. Check local virtualization support with: Shell

```
msb doctor
```

For platform-specific setup notes, see [Linux troubleshooting](https://docs.microsandbox.dev/troubleshooting/linux), [macOS troubleshooting](https://docs.microsandbox.dev/troubleshooting/macos), or [Windows troubleshooting](https://docs.microsandbox.dev/troubleshooting/windows). 2

Run code in a sandbox

Create a sandbox, execute code inside it, and get the result back. TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("hello")
    .image("python")
    .memory(512)
    .create();

const output = await sb.exec("python", ["-c", "print('Hello from a microVM!')"]);
console.log(output.stdout()); // Hello from a microVM!
```


```
use std::error::Error;

use microsandbox::Sandbox;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let sb = Sandbox::builder("hello")
        .image("python")
        .memory(512)
        .create()
        .await?;

    let output = sb.exec("python", ["-c", "print('Hello from a microVM!')"]).await?;
    println!("{}", output.stdout()?); // Hello from a microVM!

    sb.stop().await?;
    Ok(())
}
```


```
import asyncio
from microsandbox import Sandbox

async def main():
    sb = await Sandbox.create(
        "hello",
        image="python",
        memory=512,
    )

    output = await sb.exec("python", ["-c", "print('Hello from a microVM!')"])
    print(output.stdout_text)  # Hello from a microVM!

    await sb.stop()

asyncio.run(main())
```


```
sb, err := m.CreateSandbox(ctx, "hello",
    m.WithImage("python"),
    m.WithMemory(512),
)
if err != nil {
    return err
}
defer sb.Stop(ctx)

output, err := sb.Exec(ctx, "python", []string{"-c", "print('Hello from a microVM!')"})
if err != nil {
    return err
}
fmt.Println(output.Stdout()) // Hello from a microVM!
```


```
require "microsandbox"

Microsandbox.install unless Microsandbox.installed?

Microsandbox::Sandbox.with("hello", image: "python", memory: 512) do |sandbox|
  output = sandbox.exec("python", ["-c", "print('Hello from a microVM!')"])
  puts output.stdout
end
```


```
msb run python -- python3 -c "print('Hello from a microVM!')"
```


## [​](https://docs.microsandbox.dev/getting-started/quickstart#what-just-happened) What just happened?


Here’s what happened behind that `Sandbox.builder(...).create()` call:


1. **Pulled the image** from Docker Hub, unless it was already cached.
2. **Assembled a copy-on-write filesystem** so changes inside the sandbox do not modify the base image.
3. **Booted a microVM** as a child process with the resource limits you configured.
4. **Started the guest agent** so the SDK can run commands and move data in and out.


The `exec` call uses the host-guest command channel, not SSH and not the sandbox network.
Want the same sandbox on hosted infrastructure? Set `MSB_BACKEND=cloud` and export `MSB_API_KEY`; the code above then runs on [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview) unchanged.


## [​](https://docs.microsandbox.dev/getting-started/quickstart#next-steps) Next steps


- [SDK references](https://docs.microsandbox.dev/sdk/overview#reference): choose TypeScript, Rust, Python, Go, or Ruby for sandbox lifecycle and API details
- [Protect API credentials](https://docs.microsandbox.dev/sandboxes/secrets): let sandboxed code use an API without receiving the credential value
- [Browse guides](https://docs.microsandbox.dev/how-to/overview): set up agents, CI/CD, Docker, and more
- [Run on microsandbox cloud](https://docs.microsandbox.dev/cloud/overview): the same code on hosted infrastructure
- [Modify live sandbox settings](https://docs.microsandbox.dev/sandboxes/tuning): resize headroom, labels, secrets, and storage
- [Troubleshoot Linux setup](https://docs.microsandbox.dev/troubleshooting/linux): KVM, `/dev/kvm`, and permissions
- [Troubleshoot macOS setup](https://docs.microsandbox.dev/troubleshooting/macos): Apple Silicon and local runtime checks
- [Troubleshoot Windows setup](https://docs.microsandbox.dev/troubleshooting/windows): WHP, `msb doctor`, and runtime setup
- [Run commands and stream output](https://docs.microsandbox.dev/sandboxes/commands): `exec`, `shell`, `attach`, and streaming
- [Control network access](https://docs.microsandbox.dev/networking/overview): policies, DNS interception, and secret protection
- [Manage sandboxes with the CLI](https://docs.microsandbox.dev/cli/overview): create, inspect, and manage sandboxes from the terminal


Was this page helpful?

Yes No ⌘ I

---

# Live Modify - microsandbox

`https://docs.microsandbox.dev/sandboxes/tuning`

# Live Modify
## Documentation Index
## ​Supported changes
## ​Apply changes
## ​Set resize limits
## ​Preview changes
## ​Update settings
## ​Restart required
## ​Reference









Resize a running sandbox and update its configuration without replacing it

Local-only
You do not need to replace a running sandbox just because its workload changes. `modify` can resize the VM, update host-side metadata, rotate existing secrets, and change the defaults used by future commands while the sandbox stays up.

Live modification is available through TypeScript, Rust, Python, Go, and the CLI. Ruby does not expose a modification API; set its supported options when creating a sandbox.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#supported-changes) Supported changes


When a change takes effect depends on the setting:


| Change | When it takes effect | Notes |
| --- | --- | --- |
| CPU and memory | Live, within the boot-time `max_*` ceilings | The VM and workload keep running |
| Labels | Live | Host-side metadata; guest processes do not change |
| Existing secret material or removal | Live | Adding a secret or changing its placeholder needs a restart |
| Environment and workdir | Future execs | Processes that are already running keep their current values |
| `max_cpus` and `max_memory` | Restart or next start | These ceilings are fixed when the VM boots |
| Root disk size | Live, restart or next start | Managed and flat ext4 roots grow only; tmpfs changes on boot |
| Named volumes, mount tmpfs, and user disk images | Outside `modify` | Capacity is managed where the storage is defined |


The default policy applies only changes that can complete without restarting. If a patch contains one restart-required change, microsandbox rejects the whole patch and the old configuration stays intact.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#apply-changes) Apply changes


This patch doubles the running sandbox’s CPU and memory and updates a label in the same operation:
CLI TypeScript Rust Python Go

```
msb modify worker --cpus 4 --memory 2G --label tier=web
```


```
const plan = await sandbox.modify({
  cpus: 4,
  memory: 2048,
  labels: { tier: "web" },
});
```


```
let plan = sb.modify()
    .cpus(4)
    .memory(2048)
    .label("tier", "web")
    .apply()
    .await?;
```


```
plan = await sb.modify(
    cpus=4,
    memory=2048,
    labels={"tier": "web"},
)
```


```
plan, err := sb.Modify(ctx, m.ModifyOptions{
    CPUs:      4,
    MemoryMiB: 2048,
    Labels:    map[string]string{"tier": "web"},
})
```


The result is a modification plan showing what changed and whether each change was applied. CPU and memory can take a moment to converge inside the guest. The new host limits take effect immediately, and the workload continues running.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#set-resize-limits) Set resize limits


Live growth needs capacity reserved when the VM boots. Set `max_cpus` and `max_memory` above the starting allocation when you create a sandbox that may need to scale:
TypeScript Rust Python Go Ruby CLI

```
await using sandbox = await Sandbox.builder("worker")
  .image("python")
  .cpus(2)
  .memory(1024)
  .maxCpus(8)
  .maxMemory(4096)
  .create();
```


```
let sb = Sandbox::builder("worker")
    .image("python")
    .cpus(2)
    .memory(1024)
    .max_cpus(8)
    .max_memory(4096)
    .create()
    .await?;
```


```
sb = await Sandbox.create(
    "worker",
    image="python",
    cpus=2,
    memory=1024,
    max_cpus=8,
    max_memory=4096,
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithCPUs(2),
    m.WithMemory(1024),
    m.WithMaxCPUs(8),
    m.WithMaxMemory(4096),
)
```


```
sb = Microsandbox::Sandbox.create(
  "worker",
  image: "python",
  cpus: 2,
  memory: 1024,
  max_cpus: 8,
  max_memory: 4096
)
```


```
msb create python --name worker \
  --cpus 2 --memory 1G \
  --max-cpus 8 --max-memory 4G
```


The sandbox starts with two vCPUs and 1 GiB of memory, but it can grow live to eight vCPUs and 4 GiB. The ceilings default to the starting size, so omitting them leaves no live growth headroom.
Reserving headroom is cheap: spare vCPUs stay parked, and microsandbox backs spare memory only when the guest uses it. You can lower CPU or memory live without pre-planning, then grow back up to the booted ceiling later.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#preview-changes) Preview changes


Use a dry run when a patch mixes settings or you are unsure whether a restart is needed:
CLI TypeScript Rust Python Go

```
msb modify worker --max-memory 16G --dry-run
```


```
const plan = await sandbox.modify({
  maxMemory: 16_384,
  dryRun: true,
});
```


```
let plan = sb.modify()
    .max_memory(16_384)
    .dry_run()
    .await?;
```


```
plan = await sb.modify(max_memory=16_384, dry_run=True)
```


```
plan, err := sb.Modify(ctx, m.ModifyOptions{
    MaxMemoryMiB: 16_384,
    DryRun:        true,
})
```


The planner classifies every requested field before it changes anything:


| Disposition | Meaning |
| --- | --- |
| `live` | Applies without restarting the VM |
| `next start` | Is saved and applies the next time the sandbox starts |
| `requires restart` | Cannot affect the running VM under the default policy |
| `unsupported` | Is invalid for this sandbox or backing type |


## [​](https://docs.microsandbox.dev/sandboxes/tuning#update-settings) Update settings


### [​](https://docs.microsandbox.dev/sandboxes/tuning#resize-cpu-and-memory) Resize CPU and memory


![A terminal changes CPU, memory, and a label while the sandbox remains running](https://mintcdn.com/superradcompanyinc/uksi6OYeD2cA6qdw/images/live-modify.svg?fit=max&auto=format&n=uksi6OYeD2cA6qdw&q=85&s=c1516b6f3c41ca60464f5c14899a8617)
Raise or lower CPU and memory while the workload runs:
CLI TypeScript Rust Python Go

```
msb modify worker --cpus 4 --memory 2G
```


```
const plan = await sandbox.modify({ cpus: 4, memory: 2048 });
```


```
let plan = sb.modify()
    .cpus(4)
    .memory(2048)
    .apply()
    .await?;
```


```
plan = await sb.modify(cpus=4, memory=2048)
```


```
plan, err := sb.Modify(ctx, m.ModifyOptions{
    CPUs:      4,
    MemoryMiB: 2048,
})
```


Use [`msb ps`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-status) to see allocation as `effective / max`, and [`msb metrics`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-metrics) to check real usage before resizing. The apply result reports each resource’s [resize state](https://docs.microsandbox.dev/sdk/rust/sandbox#resourceresizestatus), so automation can wait for the guest to settle.


### [​](https://docs.microsandbox.dev/sandboxes/tuning#update-labels) Update labels


Labels are host-side metadata, so adding, changing, or removing one is immediate:
CLI TypeScript Rust Python Go

```
msb modify worker --label tier=web --label-rm stale
```


```
const plan = await sandbox.modify({
  labels: { tier: "web" },
  labelsRemove: ["stale"],
});
```


```
let plan = sb.modify()
    .label("tier", "web")
    .remove_label("stale")
    .apply()
    .await?;
```


```
plan = await sb.modify(
    labels={"tier": "web"},
    labels_rm=["stale"],
)
```


```
plan, err := sb.Modify(ctx, m.ModifyOptions{
    Labels:       map[string]string{"tier": "web"},
    LabelsRemove: []string{"stale"},
})
```


Running guest processes do not change. The new labels are available to listing, selection, metrics attribution, and other host-side workflows. See [Labels](https://docs.microsandbox.dev/sandboxes/labels) for naming and cardinality guidance.


### [​](https://docs.microsandbox.dev/sandboxes/tuning#set-command-defaults) Set command defaults


Environment and workdir updates require no restart, but they affect only commands started after the patch:
CLI TypeScript Rust Python Go

```
msb modify worker --env MODE=prod --workdir /app
msb exec worker -- printenv MODE
```


```
await sandbox.modify({
  env: { MODE: "prod" },
  workdir: "/app",
});

const output = await sandbox.exec("printenv", ["MODE"]);
```


```
sb.modify()
    .env("MODE", "prod")
    .workdir("/app")
    .apply()
    .await?;

let output = sb.exec("printenv", ["MODE"]).await?;
```


```
await sb.modify(env={"MODE": "prod"}, workdir="/app")
output = await sb.exec("printenv", ["MODE"])
```


```
_, err := sb.Modify(ctx, m.ModifyOptions{
    Env:     map[string]string{"MODE": "prod"},
    Workdir: "/app",
})
out, err := sb.Exec(ctx, "printenv", []string{"MODE"})
```


Processes that were already running keep their original environment and working directory.


### [​](https://docs.microsandbox.dev/sandboxes/tuning#rotate-secrets) Rotate secrets


Rotating the value of an existing secret is live because substitution happens at the host network boundary. Guest code keeps using the same placeholder while microsandbox begins injecting the new value:
CLI TypeScript Rust Python Go

```
msb modify worker --secret GITHUB_TOKEN@api.github.com
```


```
const plan = await sandbox.modify({
  secrets: {
    GITHUB_TOKEN: {
      env: "GITHUB_TOKEN",
      allowedHosts: ["api.github.com"],
    },
  },
});
```


```
use microsandbox::sandbox::SecretSource;

let plan = sb.modify()
    .secret(|secret| secret
        .env("GITHUB_TOKEN")
        .source(SecretSource::Env { var: "GITHUB_TOKEN".into() })
        .allow("api.github.com"))
    .remove_secret("OLD_TOKEN")
    .apply()
    .await?;
```


```
plan = await sb.modify(
    secrets={
        "GITHUB_TOKEN": {
            "env": "GITHUB_TOKEN",
            "allowed_hosts": ["api.github.com"],
        },
    },
)
```


```
plan, err := sb.Modify(ctx, m.ModifyOptions{
    Secrets: map[string]m.SecretModifySpec{
        "GITHUB_TOKEN": {
            Env:          "GITHUB_TOKEN",
            AllowedHosts: []string{"api.github.com"},
        },
    },
})
```


Adding a new secret or changing its guest-visible placeholder requires a restart because existing processes cannot receive a new placeholder. If the new secret requires TLS identity while interception is off, the plan also enables `tls`, which needs the same restart or next start. Existing secrets configured with `require_tls_identity(false)` continue to rotate live over plain HTTP without enabling interception. Removing a secret does not require recreating the sandbox, and removing every TLS-dependent secret leaves interception on. See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets) for sources, host allow lists, and storage behavior.


### [​](https://docs.microsandbox.dev/sandboxes/tuning#grow-the-root-disk) Grow the root disk


Grow an owned managed or flat ext4 root without restarting, including roots backed by checkpoint layers:
CLI TypeScript Rust Python Go

```
msb modify worker --root-disk 8G
```


```
await sandbox.modify({ rootDiskSize: 8192 });
```


```
sb.modify().root_disk_size(8192).apply().await?;
```


```
await sb.modify(root_disk_size=8192)
```


```
_, err := sb.Modify(ctx, m.ModifyOptions{RootDiskSizeMiB: 8192})
```


Microsandbox briefly pauses the VM to extend its writable disk, resumes it, then asks ext4 to make the space usable. Existing snapshots and sealed backing layers stay unchanged. A stopped sandbox grows before the new size is persisted.
Growth is explicit and grow-only. The ext4 image must have enough reserved metadata headroom; older runtimes and filesystems without online-resize support return an error instead of silently restarting. User-supplied disks and cloud sandboxes remain unsupported. Use `--next-start` to defer growth or `--restart` to use stopped growth.
If the disk grows but guest filesystem expansion fails, the error reports incomplete growth. Retry the same target, or stop and restart to finish recovery. Microsandbox never truncates the disk to roll back; snapshots and compaction stay blocked until recovery completes.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#restart-required) Restart required


These changes take effect after a restart:


| Change | Apply now | Defer safely |
| --- | --- | --- |
| Raise `max_cpus` or `max_memory` | `--restart` | `--next-start` |
| Resize a tmpfs root disk | On restart | `--next-start` |
| Add a new secret or change its placeholder | `--restart` | `--next-start` |


CLI TypeScript Rust Python Go

```
msb modify worker --max-memory 16G --next-start
msb modify worker --root-disk 8G --restart
```


```
await sandbox.modify({
  maxMemory: 16_384,
  policy: "next_start",
});

await sandbox.modify({
  rootDiskSize: 8192,
  policy: "restart",
});
```


```
sb.modify()
    .max_memory(16_384)
    .next_start()
    .apply()
    .await?;

sb.modify()
    .root_disk_size(8192)
    .restart()
    .apply()
    .await?;
```


```
from microsandbox import ModificationPolicy

await sb.modify(
    max_memory=16_384,
    policy=ModificationPolicy.NEXT_START,
)

await sb.modify(
    root_disk_size=8192,
    policy=ModificationPolicy.RESTART,
)
```


```
_, err := sb.Modify(ctx, m.ModifyOptions{
    MaxMemoryMiB: 16_384,
    Policy:       m.ModificationPolicyNextStart,
})

_, err = sb.Modify(ctx, m.ModifyOptions{
    RootDiskSizeMiB: 8192,
    Policy:          m.ModificationPolicyRestart,
})
```


`--next-start` saves the desired configuration without touching the running VM. `--restart` stops and starts the sandbox only when the patch needs it. The default policy does neither and rejects restart-required changes.
Root disk resizing remains conservative: managed and flat OCI disks grow only, tmpfs can grow or shrink at the next boot, and user-supplied disk images are never resized by microsandbox. Named volume and mount capacity is managed where that storage is defined. See [Volumes](https://docs.microsandbox.dev/sandboxes/volumes) and [Images](https://docs.microsandbox.dev/images/overview) for the storage model.


## [​](https://docs.microsandbox.dev/sandboxes/tuning#reference) Reference


For every CLI flag and result state, see [`msb modify`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-modify). The SDK sandbox references expose the same planner and policies for [TypeScript](https://docs.microsandbox.dev/sdk/typescript/sandbox), [Rust](https://docs.microsandbox.dev/sdk/rust/sandbox), [Python](https://docs.microsandbox.dev/sdk/python/sandbox), and [Go](https://docs.microsandbox.dev/sdk/go/sandbox).

Was this page helpful?

Yes No ⌘ I

---

# Secrets - microsandbox

`https://docs.microsandbox.dev/sandboxes/secrets`

Secrets give sandboxed code a placeholder instead of a credential. When it sends that placeholder to an allowed API, microsandbox verifies the destination and substitutes the real value outside the guest.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#add-a-secret) Add a secret


Set `GITHUB_TOKEN` in your host environment, then bind it to `api.github.com`:
TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python:3.12-bookworm")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
    )
    .create();
```


```
use microsandbox::{Sandbox};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python:3.12-bookworm")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret

sb = await Sandbox.create(
    "worker",
    image="python:3.12-bookworm",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12-bookworm"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
            },
        ),
    ),
)
if err != nil { return err }
```


```
require "microsandbox"

sb = Microsandbox::Sandbox.create(
  "worker",
  image: "python:3.12-bookworm",
  secrets: [{
    env: "GITHUB_TOKEN",
    value: ENV.fetch("GITHUB_TOKEN"),
    allowed_host: "api.github.com"
  }]
)
```


```
msb create python:3.12-bookworm --name worker \
  --secret 'GITHUB_TOKEN@api.github.com'
```


The guest receives `$MSB_GITHUB_TOKEN`. Default placeholders preserve the environment variable’s spelling; custom placeholders are optional.
Passing a raw value through an SDK persists it in the host-side sandbox configuration. Stopping the sandbox does not remove that stored value. The CLI example stores an environment reference and reads it at sandbox startup; inline credential values are rejected.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#use-a-secret) Use a secret


Run the request inside the sandbox:
TypeScript Rust Python Go Ruby CLI

```
const output = await sb.exec("sh", ["-c",
    'curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN"',
]);
console.log(output.stdout());
```


```
let output = sb.exec("sh", ["-c",
    r#"curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN""#,
]).await?;
println!("{}", output.stdout()?);
```


```
output = await sb.exec("sh", ["-c",
    'curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN"',
])
print(output.stdout_text)
```


```
output, err := sb.Exec(ctx, "sh", []string{"-c",
    `curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN"`,
})
if err != nil { return err }
fmt.Print(output.Stdout())
```


```
output = sb.exec("sh", ["-c",
  'curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN"'
])
puts output.stdout
```


```
msb exec worker -- sh -c \
  'curl -sS https://api.github.com/user -H "Authorization: Bearer $GITHUB_TOKEN"'
```


Inside the sandbox, `GITHUB_TOKEN` holds a placeholder. microsandbox substitutes the real token when the request reaches the allowed host.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#choose-substitution-locations) Choose substitution locations


| Location | Default |
| --- | --- |
| Headers, including Basic authentication | Enabled |
| URL query parameters | Disabled |
| Request body | Disabled |


Enable only the locations your API needs. For headers, list credential fields such as `Authorization`; an empty list permits every header and could let an allowed endpoint echo a substituted secret back to the guest.


### [​](https://docs.microsandbox.dev/sandboxes/secrets#query-parameters) Query parameters


Enable query substitution only when the API requires a credential in the URL:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .substituteInQuery(true)
    )
    .create();
```


```
use microsandbox::{Sandbox};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .substitute_in_query(true)
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret, SecretSubstitution

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            substitution=SecretSubstitution(query=True),
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                Substitution: m.SecretSubstitution{Query: true},
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN:query@api.github.com'
```


### [​](https://docs.microsandbox.dev/sandboxes/secrets#request-bodies) Request bodies


Enable body substitution only when the API requires a credential in the body:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .substituteInBody(true)
    )
    .create();
```


```
use microsandbox::{Sandbox};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .substitute_in_body(true)
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret, SecretSubstitution

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            substitution=SecretSubstitution(body=True),
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                Substitution: m.SecretSubstitution{Body: true},
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN:body@api.github.com'
## Documentation Index
## ​Add a secret
## ​Use a secret
## ​Choose substitution locations
## ​Violation actions
## ​Pass through placeholders
## ​Custom denial message
## ​Update secrets
## ​YAML configuration
## ​Security boundary
## ​Troubleshooting
## ​SDK reference












```


Substitution limits and disabled locations

On a destination that passes the secret’s host and TLS checks, placeholders in disabled locations pass through unchanged. Other destinations need explicit passthrough permission or follow the violation action. Disabling headers also disables Basic authentication substitution; a non-empty header list requires header substitution to be enabled. When enabled, body substitution supports fixed-length HTTP/1 bodies up to 16 MiB and chunked HTTP/1 bodies. Larger fixed-length bodies are blocked. Encoded bodies pass through unchanged; HTTP/2 body substitution is unsupported and matching body placeholders are blocked. See [body limits](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinbody).


## [​](https://docs.microsandbox.dev/sandboxes/secrets#violation-actions) Violation actions


A secret-policy violation occurs when a request carries a placeholder to a destination that can receive neither the credential nor the unchanged placeholder. Choose what happens to that request:


| Action | Result |
| --- | --- |
| Block | Block without a violation log |
| Block and log (default) | Block the request and log a warning |
| Block and terminate | Block, log an error, and stop the sandbox |


Per-secret actions override the sandbox default. [Placeholder passthrough](https://docs.microsandbox.dev/sandboxes/secrets#passthrough) is a separate host rule. The [denial message](https://docs.microsandbox.dev/sandboxes/secrets#http-denial-responses) controls what a blocked HTTP request can show to the caller.


### [​](https://docs.microsandbox.dev/sandboxes/secrets#block) Block


Reject the request without a violation log:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .violationAction("block")
    )
    .create();
```


```
use microsandbox::{Sandbox, SecretViolationAction};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .violation_action(SecretViolationAction::Block)
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret, ViolationAction

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            violation_action=ViolationAction.BLOCK,
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                ViolationAction: m.ViolationActionBlock,
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN@api.github.com' \
  --secret-violation-action block
```


### [​](https://docs.microsandbox.dev/sandboxes/secrets#block-and-log) Block and log


The default. No additional configuration is needed; to set it explicitly:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .violationAction("block-and-log")
    )
    .create();
```


```
use microsandbox::{Sandbox, SecretViolationAction};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .violation_action(SecretViolationAction::BlockAndLog)
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret, ViolationAction

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            violation_action=ViolationAction.BLOCK_AND_LOG,
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                ViolationAction: m.ViolationActionBlockAndLog,
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN@api.github.com' \
  --secret-violation-action block-and-log
```


### [​](https://docs.microsandbox.dev/sandboxes/secrets#block-and-terminate) Block and terminate


Stop the sandbox when a violation occurs:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .violationAction("block-and-terminate")
    )
    .create();
```


```
use microsandbox::{Sandbox, SecretViolationAction};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .violation_action(SecretViolationAction::BlockAndTerminate)
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret, ViolationAction

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            violation_action=ViolationAction.BLOCK_AND_TERMINATE,
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                ViolationAction: m.ViolationActionBlockAndTerminate,
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN@api.github.com' \
  --secret-violation-action block-and-terminate
```


## [​](https://docs.microsandbox.dev/sandboxes/secrets#pass-through-placeholders) Pass through placeholders


Allow an additional host to receive the **unchanged placeholder** where substitution does not apply. Credential-allowed hosts already receive unchanged placeholders in disabled locations after passing the secret’s identity checks. This permission does not grant access to the credential; existing substitution permissions still apply. For example, allow the placeholder to appear in an AI request:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .secret(s =>
        s.env("GITHUB_TOKEN")
            .value(process.env.GITHUB_TOKEN!)
            .allow("api.github.com")
            .allowPlaceholderFor("api.anthropic.com")
    )
    .create();
```


```
use microsandbox::{Sandbox};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com")
        .allow_placeholder_for("api.anthropic.com")
    )
    .create()
    .await?;
```


```
import os
from microsandbox import Sandbox, Secret

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[
        Secret.env(
            "GITHUB_TOKEN",
            value=os.environ["GITHUB_TOKEN"],
            allow=["api.github.com"],
            allow_placeholder_for=["api.anthropic.com"],
        ),
    ],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(
        m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
            m.SecretEnvOptions{
                Allow: []string{"api.github.com"},
                AllowPlaceholderFor: []string{"api.anthropic.com"},
            },
        ),
    ),
)
if err != nil { return err }
```


```
msb create python --name worker \
  --secret 'GITHUB_TOKEN:passthrough=api.anthropic.com@api.github.com'
```


Passthrough neither grants network access nor adds the host to the credential allow list. Other destinations still follow the violation action.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#custom-denial-message) Custom denial message


Local-only
Supported secret-policy blocks return JSON `403` responses by default. Set the message shown to the caller:
TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python:3.12-bookworm")
    .network(n => n.http(h => h
        .denyResponse(true)
        .denyResponseFormat("json")
        .secretDenyMessage("Check secret access for this destination.")))
    .secret(s => s.env("GITHUB_TOKEN")
        .value(process.env.GITHUB_TOKEN!)
        .allow("api.github.com"))
    .create();
```


```
use microsandbox::{Sandbox, sandbox::HttpDenyResponseFormat};

let token = std::env::var("GITHUB_TOKEN")?;
let sb = Sandbox::builder("worker")
    .image("python:3.12-bookworm")
    .network(|n| n.http(|h| h
        .deny_response(true)
        .deny_response_format(HttpDenyResponseFormat::Json)
        .secret_deny_message("Check secret access for this destination.")))
    .secret(|s| s.env("GITHUB_TOKEN")
        .value(token)
        .allow("api.github.com"))
    .create()
    .await?;
```


```
import os
from microsandbox import HttpConfig, Network, Sandbox, Secret

sb = await Sandbox.create(
    "worker",
    image="python:3.12-bookworm",
    network=Network(http=HttpConfig(
        deny_response=True,
        deny_response_format="json",
        secret_deny_message="Check secret access for this destination.",
    )),
    secrets=[Secret.env(
        "GITHUB_TOKEN",
        value=os.environ["GITHUB_TOKEN"],
        allow=["api.github.com"],
    )],
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12-bookworm"),
    m.WithNetwork(&m.NetworkConfig{
        HTTP: &m.HTTPConfig{
            DenyResponse: true,
            DenyResponseFormat: m.HTTPDenyResponseJSON,
            SecretDenyMessage: "Check secret access for this destination.",
        },
    }),
    m.WithSecrets(m.Secret.Env("GITHUB_TOKEN", os.Getenv("GITHUB_TOKEN"),
        m.SecretEnvOptions{Allow: []string{"api.github.com"}},
    )),
)
if err != nil { return err }
```


```
require "microsandbox"

sb = Microsandbox::Sandbox.create(
  "worker",
  image: "python:3.12-bookworm",
  http: {
    deny_response: true,
    deny_response_format: "json",
    secret_deny_message: "Check secret access for this destination."
  },
  secrets: [{
    env: "GITHUB_TOKEN",
    value: ENV.fetch("GITHUB_TOKEN"),
    allowed_host: "api.github.com"
  }]
)
```


The message is literal; the response also includes `code: secret_policy_denied` and the requested `domain`. The [YAML example](https://docs.microsandbox.dev/sandboxes/secrets#yaml-configuration) shows the same setting. See [HTTP denial responses](https://docs.microsandbox.dev/networking/overview#http-denial-responses) for response limits, TLS requirements, and opt-out settings.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#update-secrets) Update secrets


Local-only
You can rotate a secret, change its allowed hosts, or remove it live when supported. Adding a secret or changing its placeholder or substitution requires a restart. These examples use a host environment reference:


TLS and restart details

New secrets added through `modify` require TLS identity by default and enable interception if needed. That change requires a restart and appears in the plan as `tls`. Existing secrets that explicitly allow plain-HTTP substitution can still rotate live. Removing the last TLS-dependent secret leaves interception enabled.
TypeScript Rust Python Go CLI

```
await sb.modify({
  secrets: {
    GITHUB_TOKEN: { env: "GITHUB_TOKEN", allowedHosts: ["api.github.com"] },
  },
  policy: "restart",
});

await sb.modify({ secretsRemove: ["GITHUB_TOKEN"] });
```


```
use microsandbox::sandbox::SecretSource;

let plan = sb.modify()
    .secret(|s| s
        .env("GITHUB_TOKEN")
        .source(SecretSource::Env { var: "GITHUB_TOKEN".into() })
        .allow("api.github.com"))
    .restart()
    .apply()
    .await?;

sb.modify().remove_secret("GITHUB_TOKEN").apply().await?;
```


```
from microsandbox import ModificationPolicy

await sb.modify(
    secrets={
        "GITHUB_TOKEN": {
            "env": "GITHUB_TOKEN",
            "allowed_hosts": ["api.github.com"],
        },
    },
    policy=ModificationPolicy.RESTART,
)

await sb.modify(secrets_rm=["GITHUB_TOKEN"])
```


```
_, err := sb.Modify(ctx, m.ModifyOptions{
    Secrets: map[string]m.SecretModifySpec{
        "GITHUB_TOKEN": {
            Env:          "GITHUB_TOKEN",
            AllowedHosts: []string{"api.github.com"},
        },
    },
    Policy: m.ModificationPolicyRestart,
})

_, err = sb.Modify(ctx, m.ModifyOptions{
    SecretsRemove: []string{"GITHUB_TOKEN"},
})
```


```
msb modify worker --secret GITHUB_TOKEN@api.github.com --restart  # add or rotate
msb modify worker --secret-rm GITHUB_TOKEN                       # remove
```


Updating a sandbox secret does not rotate or revoke it at the issuing service. See [Live Modify](https://docs.microsandbox.dev/sandboxes/tuning) for restart and TLS behavior.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#yaml-configuration) YAML configuration


You can also declare secrets and the custom denial message in sandbox YAML. An exact environment reference avoids persisting the resolved value:
YAML

```
network:
  http:
    deny_response: true
    deny_response_format: json
    secret_deny_message: "Check secret access for this destination."
secrets:
  GITHUB_TOKEN:
    value: ${GITHUB_TOKEN}
    allow: [api.github.com]
    substitution:
      headers: true
      header_fields: []
      query: false
      body: false
    passthrough: [api.anthropic.com]
    violation_action: block-and-log
```


In YAML, `substitution` selects where credentials are inserted; `passthrough` permits unchanged placeholders on additional hosts. A top-level `secret_violation_action` sets the sandbox-wide default. See [CLI configuration](https://docs.microsandbox.dev/cli/configuration#secrets) for loading configuration and CLI equivalents.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#security-boundary) Security boundary


- **Destination checks:** Injection checks the allowed host against observed DNS and TLS identity, including the HTTP request authority. A forged hostname or hard-coded IP is not enough.
- **TLS:** Injection requires intercepted TLS by default. Bypassed TLS cannot be inspected for placeholders or receive injected credentials. See [TLS inspection](https://docs.microsandbox.dev/networking/tls).
- **Trusted hosts:** Allowed endpoints receive the real value and could return it to the guest. Keep allow lists narrow and include redirect destinations only when trusted. Wildcards include the root domain and its subdomains.
- **Network access:** Secret rules decide where credentials can be injected; network rules still control connectivity.
- **Guest-side signing:** A placeholder cannot replace raw credentials used to sign requests inside the guest. Supplying the real value as a plain environment variable exposes it to guest code.


See [Secret handling](https://docs.microsandbox.dev/security/secrets) for the protection boundary and storage details.


## [​](https://docs.microsandbox.dev/sandboxes/secrets#troubleshooting) Troubleshooting


| Symptom | Check |
| --- | --- |
| Request blocked | Check host logs, destination rules, and enabled request locations. |
| Sandbox stops after a request | Check for a terminate-on-violation policy. |
| API receives a placeholder | Check TLS interception, substitution settings, and passthrough rules. |
| Guest prints the placeholder | Expected: substitution happens outside the guest. |


## [​](https://docs.microsandbox.dev/sandboxes/secrets#sdk-reference) SDK reference


[TypeScript](https://docs.microsandbox.dev/sdk/typescript/secrets) · [Rust](https://docs.microsandbox.dev/sdk/rust/secrets) · [Python](https://docs.microsandbox.dev/sdk/python/secrets) · [Go](https://docs.microsandbox.dev/sdk/go/secrets)

Was this page helpful?

Yes No ⌘ I

---

# How-to guides - microsandbox

`https://docs.microsandbox.dev/how-to/overview`

## [​](https://docs.microsandbox.dev/how-to/overview#running-agents) Agents


- [Run Claude Code](https://docs.microsandbox.dev/how-to/agents/claude-code)
- [Run Codex CLI](https://docs.microsandbox.dev/how-to/agents/codex)
- [Run OpenCode](https://docs.microsandbox.dev/how-to/agents/opencode)
- [Set up OpenClaw](https://docs.microsandbox.dev/how-to/agents/openclaw)
- [Run Goose](https://docs.microsandbox.dev/how-to/agents/goose)
- [Run Gemini CLI](https://docs.microsandbox.dev/how-to/agents/gemini-cli)
- [Set up Hermes Agent](https://docs.microsandbox.dev/how-to/agents/hermes-agent)
- [Run Pi](https://docs.microsandbox.dev/how-to/agents/pi)


## [​](https://docs.microsandbox.dev/how-to/overview#development-environments) Development


- [Connect VS Code](https://docs.microsandbox.dev/how-to/development/vscode)
- [Connect JetBrains via ACP](https://docs.microsandbox.dev/how-to/development/jetbrains-acp)
- [Run code-server](https://docs.microsandbox.dev/how-to/development/code-server)
- [Run JupyterLab](https://docs.microsandbox.dev/how-to/development/jupyterlab)
- [Open a VNC desktop](https://docs.microsandbox.dev/how-to/development/vnc-desktop)


## [​](https://docs.microsandbox.dev/how-to/overview#browser-automation) Browser automation


- [Run a browser agent](https://docs.microsandbox.dev/how-to/browser-automation/browser-use)
- [Automate a browser](https://docs.microsandbox.dev/how-to/browser-automation/playwright)


## [​](https://docs.microsandbox.dev/how-to/overview#working-with-workloads) Workloads


- [Transcode media with FFmpeg](https://docs.microsandbox.dev/how-to/file-processing/ffmpeg)
- [Convert documents to PDF](https://docs.microsandbox.dev/how-to/file-processing/libreoffice-pdf)
- [Vet a Terraform provider offline](https://docs.microsandbox.dev/how-to/plugins/terraform)
- [Rehearse a database migration](https://docs.microsandbox.dev/how-to/data/migration-rehearsal)
- [Crawl a site with Scrapy](https://docs.microsandbox.dev/how-to/web-automation/scrapy)
- [Process a batch in parallel](https://docs.microsandbox.dev/how-to/automation/parallel-batch-jobs)


## [​](https://docs.microsandbox.dev/how-to/overview#sandbox-setup) Sandbox setup


- [Run Docker in a sandbox](https://docs.microsandbox.dev/how-to/docker/docker-in-sandbox)
- [Use local images](https://docs.microsandbox.dev/how-to/docker/local-images)
- [Boot with systemd](https://docs.microsandbox.dev/how-to/guest/systemd-services)
- [Start warm workers from snapshots](https://docs.microsandbox.dev/how-to/sandboxing/warm-workers)


## [​](https://docs.microsandbox.dev/how-to/overview#hosting) Deployment


- [Run microsandbox in Docker](https://docs.microsandbox.dev/how-to/docker/docker)
- [Run microsandbox in Kubernetes](https://docs.microsandbox.dev/how-to/sandboxing/kubernetes)


## [​](https://docs.microsandbox.dev/how-to/overview#storage) Storage


- [Run PostgreSQL](https://docs.microsandbox.dev/how-to/data/postgresql)
- [Run Redis](https://docs.microsandbox.dev/how-to/data/redis)
- [Mount S3 with JuiceFS](https://docs.microsandbox.dev/how-to/data/juicefs-s3)


## [​](https://docs.microsandbox.dev/how-to/overview#ci-automation) CI/CD


- [Run a GitHub Actions job](https://docs.microsandbox.dev/how-to/ci-cd/github-actions-runner)
- [Run isolated PR checks](https://docs.microsandbox.dev/how-to/ci-cd/pr-checks)
- [Run Docker Compose tests](https://docs.microsandbox.dev/how-to/ci-cd/compose-tests)
- [Serve a preview deployment](https://docs.microsandbox.dev/how-to/ci-cd/preview-deploys)
- [Schedule dependency audits](https://docs.microsandbox.dev/how-to/automation/dependency-audits)


## [​](https://docs.microsandbox.dev/how-to/overview#observability) Observability


- [Send metrics to Grafana Cloud](https://docs.microsandbox.dev/how-to/metrics-backends/grafana-cloud)
- [Forward metrics with Grafana Alloy](https://docs.microsandbox.dev/how-to/metrics-backends/grafana-alloy)
- [Inspect metrics with OpenTelemetry](https://docs.microsandbox.dev/how-to/metrics-backends/otel-collector)
- [Send metrics to Prometheus](https://docs.microsandbox.dev/how-to/metrics-backends/prometheus)
- [Send metrics to Datadog](https://docs.microsandbox.dev/how-to/metrics-backends/datadog)


Was this page helpful?

Yes No ⌘ I Assistant Responses are generated using AI and may contain mistakes.

---

# Introduction - microsandbox

`https://docs.microsandbox.dev/getting-started/introduction`

# Introduction
## Documentation Index
## ​Why microsandbox
## ​Example use cases
## ​Minimal example
## ​Next steps






Easy, fast microVMs for untrusted workloads

microsandbox is a local-first microVM runtime for untrusted workloads: AI agents, user code, plugins, package installs, CI jobs, dev environments, scrapers, and automation.
Each sandbox is a lightweight VM with its own Linux kernel, filesystem, and network boundary. Start one locally with the `msb` CLI or an SDK, or run it on [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview) with an API key. From there, what you do inside the sandbox is up to you.
It keeps the familiar workflow of OCI images and command execution, while moving risky work out of the host process.
npx macOS & Linux Windows

```
npx microsandbox run debian
```


```
curl -fsSL https://install.microsandbox.dev | sh
msb run debian
```


```
irm https://install.microsandbox.dev/windows | iex
msb run debian
```


## [​](https://docs.microsandbox.dev/getting-started/introduction#why-microsandbox) Why microsandbox


- **Hardware isolation.** Each sandbox is a VM, not a container namespace on the host kernel.
- **Local runtime.** The SDK starts the sandbox process directly. No daemon, remote service, or infrastructure setup.
- **Cloud when you want it.** The same SDK and CLI run sandboxes on [hosted infrastructure](https://docs.microsandbox.dev/cloud/overview); an API key is the only change.
- **Fast startup.** Sandboxes are lightweight enough to create from application code.
- **Docker-like inputs.** Use familiar OCI images from Docker Hub, GHCR, ECR, GCR, or another registry.
- **Programmable controls.** Configure resources, volumes, secrets, networking, and lifecycle from the CLI or SDK.
- **Multi-language SDKs.** TypeScript, Rust, Python, Go, and Ruby expose the same core model.


## [​](https://docs.microsandbox.dev/getting-started/introduction#example-use-cases) Example use cases


- **AI agents.** Give coding agents and tool-using assistants a dedicated machine for commands, files, package installs, and generated code.
- **User code execution.** Run submitted scripts, notebooks, plugins, and extensions away from the host.
- **CI/CD and builds.** Isolate test jobs, compilers, package managers, and build tools.
- **Dev environments.** Create disposable Linux machines without touching your laptop or host Docker daemon.
- **Scrapers and automation.** Allow internet access while blocking private networks and metadata services.
- **Secure tool execution.** Run CLIs and dependencies that should not see host secrets or ambient credentials.


[Guides Put microsandbox to work Tested workflows for agents, CI/CD, Docker, automation, and more. Browse all](https://docs.microsandbox.dev/how-to/overview)


## [​](https://docs.microsandbox.dev/getting-started/introduction#minimal-example) Minimal example


TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("hello")
    .image("python")
    .create();

const output = await sb.exec("python", ["-c", "print('Hello from a microVM!')"]);
console.log(output.stdout());
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("hello")
    .image("python")
    .create()
    .await?;

let output = sb.exec("python", ["-c", "print('Hello from a microVM!')"]).await?;
println!("{}", output.stdout()?);

sb.stop().await?;
```


```
from microsandbox import Sandbox

sb = await Sandbox.create("hello", image="python")

output = await sb.exec("python", ["-c", "print('Hello from a microVM!')"])
print(output.stdout_text)

await sb.stop()
```


```
sb, err := m.CreateSandbox(ctx, "hello", m.WithImage("python"))
if err != nil {
    return err
}
defer sb.Stop(ctx)

out, err := sb.Exec(ctx, "python", []string{"-c", "print('Hello from a microVM!')"})
if err != nil {
    return err
}
fmt.Println(out.Stdout())
```


```
require "microsandbox"

Microsandbox::Sandbox.with("hello", image: "python") do |sb|
  output = sb.exec("python", ["-c", "print('Hello from a microVM!')"])
  puts output.stdout
end
```


## [​](https://docs.microsandbox.dev/getting-started/introduction#next-steps) Next steps


## Quickstart

Install microsandbox and run your first sandbox.

## microsandbox cloud

Run the same sandboxes on hosted infrastructure.

## CLI overview

Manage sandboxes from the terminal.

## SDK reference

Choose a language and look up the API surface.

Was this page helpful?

Yes No ⌘ I

---

# Commands - microsandbox

`https://docs.microsandbox.dev/sandboxes/commands`

# Commands
## Documentation Index
## ​Run the image default workload
## ​Execute a command
## ​Background jobs
## ​Execution options
## ​Shell commands
## ​Stream output
## ​Interactive attach
## ​Write stdin
## ​Session IDs
## ​Reference












Execute commands, stream output, and interact with sandboxes

Run commands, read their output, and check exit codes without SSH. Execution uses a dedicated host-to-guest channel, so it works even with networking disabled.


## [​](https://docs.microsandbox.dev/sandboxes/commands#run-the-image-default-workload) Run the image default workload


Sandbox creation is boot-only: configuring an image, ENTRYPOINT, or CMD does not execute that workload. Use the default-workload methods when you want the SDK to resolve the effective OCI `ENTRYPOINT + CMD` and run it. A configured CMD override replaces the image CMD while preserving the effective entrypoint. If neither field supplies an executable, these methods return the typed `NoDefaultCommand` error instead of falling back to a shell.
TypeScript Rust Python Go

```
const sb = await Sandbox.builder("worker")
  .image("example/worker:latest")
  .cmd(["worker.py", "--once"])
  .create();
const output = await sb.execDefault();
```


```
let sb = Sandbox::builder("worker")
    .image("example/worker:latest")
    .cmd(["worker.py", "--once"])
    .create()
    .await?;
let output = sb.exec_default().await?;
```


```
sb = await Sandbox.create(
    "worker",
    image="example/worker:latest",
    cmd=["worker.py", "--once"],
)
output = await sb.exec_default()
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("example/worker:latest"),
    m.WithCmd("worker.py", "--once"),
)
output, err := sb.ExecDefault(ctx)
```


The default workload also supports streaming and interactive execution:
TypeScript Rust Python Go

```
// Choose one: stream output, or attach the current terminal.
const stream = await sb.execDefaultStream();
// const exit = await sb.attachDefault();
```


```
// Choose one: stream output, or attach the current terminal.
let stream = sb.exec_default_stream().await?;
// let exit = sb.attach_default().await?;
```


```
# Choose one: stream output, or attach the current terminal.
stream = await sb.exec_default_stream()
# exit_code = await sb.attach_default()
```


```
// Choose one: stream output, or attach the current terminal.
stream, err := sb.ExecDefaultStream(ctx)
if err != nil {
    return err
}
defer stream.Close()
// exitCode, err := sb.AttachDefault(ctx)
```


Consume the stream as shown in [Streaming output](https://docs.microsandbox.dev/sandboxes/commands#stream-output). Literal command execution and terminal attachment continue to ignore ENTRYPOINT and CMD.


## [​](https://docs.microsandbox.dev/sandboxes/commands#execute-a-command) Execute a command


Run a command and wait for it to complete. You get back the exit code, stdout, and stderr.
TypeScript Rust Python Go Ruby CLI

```
const output = await sb.exec("python", ["-c", "print('hello')"]);
console.log(output.stdout()); // "hello\n"
console.log(output.success);  // true
console.log(output.code);     // 0
```


```
let output = sb.exec("python", ["-c", "print('hello')"]).await?;
println!("{}", output.stdout()?);     // "hello\n"
println!("{}", output.status().code); // 0
```


```
output = await sb.exec("python", ["-c", "print('hello')"])
print(output.stdout_text)     # "hello\n"
print(output.success)         # True
print(output.exit_code)       # 0
```


```
output, err := sb.Exec(ctx, "python", []string{"-c", "print('hello')"})
fmt.Print(output.Stdout())     // "hello\n"
fmt.Println(output.Success())  // true
fmt.Println(output.ExitCode()) // 0
```


```
output = sb.exec("python", ["-c", "print('hello')"])
puts output.stdout     # "hello\n"
puts output.success?   # true
puts output.exit_code  # 0
```


```
msb exec worker -- python -c "print('hello')"
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#background-jobs) Background jobs


Use a background job for a command that should keep running after you disconnect. The local sandbox must already be running. Starting the job returns an ID you can use to check its progress or reconnect.
TypeScript Rust Python Go Ruby CLI

```
const job = await sb.execDetachedWith("sh", (e) => e
    .args(["-c", "echo started; sleep 60; echo done"])
    .stdinNull());
console.log(job.id);
const result = await job.wait();
const output = await job.logs();
```


```
use microsandbox::sandbox::jobs::JobLogOptions;

let job = sb.exec_detached_with("sh", |e| e
    .args(["-c", "echo started; sleep 60; echo done"])
    .stdin_null()).await?;
println!("{}", job.id());
let result = job.wait().await?;
let output = job.logs(&JobLogOptions::default()).await?;
```


```
from microsandbox import Stdin

job = await sb.exec_detached(
    "sh", ["-c", "echo started; sleep 60; echo done"], stdin=Stdin.null(),
)
print(job.id)
result = await job.wait()
output = await job.logs()
```


```
job, err := sb.ExecDetached(ctx, "sh",
    []string{"-c", "echo started; sleep 60; echo done"}, m.WithExecStdinNull(),
)
if err != nil {
    return err
}
defer job.Close()
fmt.Println(job.ID())
result, err := job.Wait(ctx)
if err != nil {
    return err
}
```


```
job = sb.exec_detached("sh", ["-c", "echo started; sleep 60; echo done"], stdin: :null)
puts job.id
result = job.wait
output = job.logs
```


```
msb create alpine --name worker
job=$(msb exec -d --no-stdin worker -- sh -c 'echo started; sleep 60; echo done')
msb logs worker --job "$job" --follow
msb wait worker --job "$job"
```


Stopping the sandbox stops its jobs. Restarting never reruns them. Finish active jobs before taking a full snapshot or forking; pause and resume remain supported.


| Command | Purpose |
| --- | --- |
| `msb jobs <sandbox>` | List active jobs; `--all` includes retained history |
| `msb logs <sandbox> --job ID` | Read output; add `--follow` to stream it |
| `msb inspect <sandbox> --job ID` | Show command, state, input mode, and exit result |
| `msb attach <sandbox> --job ID` | Reconnect; Ctrl-] detaches without stopping the job |
| `msb wait <sandbox> --job ID` | Wait for exit; `--timeout 30s` limits the wait, not the job |
| `msb signal <sandbox> --job ID --signal TERM` | Send a Linux signal to the process group |
| `msb kill <sandbox> --job ID` | Request SIGKILL; use `wait` to confirm exit |
| `msb eof <sandbox> --job ID` | Close pipe input permanently; use Ctrl-D for a terminal |


Job IDs belong to one sandbox and are separate from process IDs. Without `--job`, `logs`, `inspect`, and `wait` refer to the sandbox itself. All commands also support the `msb sandbox ...` form.


Input and interactive shells

`--no-stdin` sends EOF and disables automatic terminal allocation. Otherwise, input stays open for a later attachment. `--tty` forces a terminal; `--no-tty` uses pipes. Detached launch never reads your terminal’s input and cannot be combined with `--stream`. Shell

```
shell_job=$(msb exec -d --tty worker -- sh)
msb attach worker --job "$shell_job"
# Press Ctrl-] to detach, then attach again with the same job ID.
```

One attachment can write at a time; others can use `--read-only`. Detaching or reaching local input EOF leaves guest input open. An abrupt disconnect releases input ownership within 30 seconds. Terminal output combines stdout and stderr as `output`; pipes keep them separate.


History and limits

Job metadata and captured output remain available after disconnect or sandbox shutdown. After a runtime restart, a job without a confirmed exit is marked `lost`.

- Up to 32 active jobs and 256 retained histories per sandbox.
- Two 512 KiB output segments per job. Reading pruned output reports a cursor-gap error.
- After 65,536 job admissions, restart the sandbox to launch more.

Use `--limit N` and `--cursor ID` to page through `jobs`. `jobs`, `inspect`, and `wait` accept `--format json`. Logs retain their usual tail, time, source, and format options. If output storage fails, capture stops permanently for that job. Previously saved output stays readable, and the process and live attachments continue. Inspect the job for the cutoff. If metadata storage also fails, its diagnostic stays in memory until a later update can save it.


Timeouts and interrupted input

Execution timeouts still apply after you disconnect. Older runtimes and unsupported backends reject job launch before dispatch. SDK job errors expose stable codes. If launch confirmation is lost, the error includes a job ID; inspect it before retrying to avoid starting the command twice. While paused, you can inspect or wait for jobs, but waiting does not resume them. Signals take effect after resume. Full input buffers do not block signals or deadlines. Input bytes and EOF remain ordered; a signal may interrupt queued input. Inspect reports signal-delivery failures. Ctrl-] remains available while input is blocked, with up to 1 MiB of buffered lookahead. Detaching waits up to two seconds for earlier input to be accepted. Overflow discards further input but keeps the attachment open until you detach, reach local EOF, or the job finishes. `input_not_flushed` means some input was dropped or could not be confirmed. Do not resend it automatically: the job may already have received it. Detaching restores your terminal without stopping the job or closing its input. A graceful sandbox stop interrupts queued command input while preserving filesystem ordering. If stop times out, it reports failure without forcing termination.


## [​](https://docs.microsandbox.dev/sandboxes/commands#execution-options) Execution options


These options apply to a single execution and don’t change the sandbox’s defaults.
TypeScript Rust Python Go Ruby CLI

```
const output = await sb.execWith("python", (e) =>
    e.args(["compute.py"])
        .cwd("/app")
        .env("PYTHONPATH", "/app/lib")
        .timeout(30_000)
        .rlimit("nofile", 1024),
);
```


```
let output = sb.exec_with("python", |e| e
    .args(["compute.py"])
    .cwd("/app")
    .env("PYTHONPATH", "/app/lib")
    .timeout(Duration::from_secs(30))
    .rlimit(RlimitResource::Nofile, 1024)
).await?;
```


```
from microsandbox import Rlimit

output = await sb.exec(
    "python",
    ["compute.py"],
    cwd="/app",
    env={"PYTHONPATH": "/app/lib"},
    timeout=30.0,
    rlimits=[Rlimit.nofile(1024)],
)
```


```
output, err := sb.Exec(ctx, "python", []string{"compute.py"},
    m.WithExecCwd("/app"),
    m.WithExecEnv(map[string]string{"PYTHONPATH": "/app/lib"}),
    m.WithExecTimeout(30*time.Second),
)
```


```
output = sb.exec(
  "python", ["compute.py"],
  cwd: "/app",
  env: { "PYTHONPATH" => "/app/lib" },
  timeout: 30.0,
  rlimits: { nofile: 1024 }
)
```


```
msb exec worker \
  -w /app \
  -e PYTHONPATH=/app/lib \
  --timeout 30s \
  --rlimit nofile=1024 \
  -- python compute.py
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#shell-commands) Shell commands


Run a command through the sandbox’s configured shell (defaults to `/bin/sh`). Useful for pipelines, redirects, and other shell syntax that `exec` doesn’t interpret.
TypeScript Rust Python Go Ruby CLI

```
const output = await sb.shell("ls -la /app && echo done")
```


```
let output = sb.shell("ls -la /app && echo done").await?;
```


```
output = await sb.shell("ls -la /app && echo done")
```


```
output, err := sb.Shell(ctx, "ls -la /app && echo done")
```


```
output = sb.shell("ls -la /app && echo done")
```


```
msb exec worker -- sh -c "ls -la /app && echo done"
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#stream-output) Stream output


Ruby currently collects command output with `exec` and `shell`. It does not expose streaming handles, interactive attach, or session IDs.
For long-running processes or large output, streaming gives you stdout, stderr, and exit events as they happen instead of buffering everything until the command finishes.
TypeScript Rust Python Go

```
const handle = await sb.execStream("tail", ["-f", "/var/log/app.log"]);

for await (const event of handle) {
    switch (event.kind) {
        case "stdout": process.stdout.write(event.data); break;
        case "stderr": process.stderr.write(event.data); break;
        case "exited": console.log(`Exited: ${event.code}`); break;
    }
}
```


```
let mut handle = sb.exec_stream("tail", ["-f", "/var/log/app.log"]).await?;

while let Some(event) = handle.recv().await {
    match event {
        ExecEvent::Stdout(data) => print!("{}", String::from_utf8_lossy(&data)),
        ExecEvent::Stderr(data) => eprint!("{}", String::from_utf8_lossy(&data)),
        ExecEvent::Exited { code } => break,
        _ => {}
    }
}
```


```
from microsandbox import ExecEventType

handle = await sb.exec_stream("tail", ["-f", "/var/log/app.log"])

async for event in handle:
    match event.event_type:
        case ExecEventType.STDOUT: print(event.data.decode(), end="")
        case ExecEventType.STDERR: print(event.data.decode(), end="", file=sys.stderr)
        case ExecEventType.EXITED: print(f"Exited: {event.code}")
```


```
handle, err := sb.ExecStream(ctx, "tail", []string{"-f", "/var/log/app.log"})
for {
    event, err := handle.Recv(ctx)
    if err != nil {
        return err
    }
    switch event.Kind {
    case m.ExecEventStdout:
        os.Stdout.Write(event.Data)
    case m.ExecEventStderr:
        os.Stderr.Write(event.Data)
    case m.ExecEventExited:
        fmt.Printf("Exited: %d\n", event.ExitCode)
    case m.ExecEventDone:
        return nil
    }
}
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#interactive-attach) Interactive attach


Bridges your terminal directly to a process inside the sandbox for a fully interactive PTY session. Useful for debugging, running REPLs, or anything that expects a real terminal.
TypeScript Rust Python Go CLI

```
// Attach to the default shell
const exitCode = await sb.attachShell();

// Attach to a specific command with custom detach keys
await sb.attachWith("bash", (a) =>
    a.env("DEBUG", "1").cwd("/app").detachKeys("ctrl-q"),
);
```


```
let exit_code = sb.attach_shell().await?;

let exit_code = sb.attach_with("python", |a| a
    .env("DEBUG", "1")
    .cwd("/app")
    .detach_keys("ctrl-q")
).await?;
```


```
# Attach to the default shell
exit_code = await sb.attach_shell()

# Attach to a specific command with custom detach keys
exit_code = await sb.attach(
    "python",
    env={"DEBUG": "1"},
    cwd="/app",
    detach_keys="ctrl-q",
)
```


```
// Attach to the default shell.
exitCode, err := sb.AttachShell(ctx)
if err != nil {
    return err
}
fmt.Println("shell exited with", exitCode)

// Attach to a specific command with options.
exitCode, err = sb.AttachWith(ctx, "python", nil,
    m.WithAttachUser("dev"),
    m.WithAttachEnv(map[string]string{"DEBUG": "1"}),
    m.WithAttachCwd("/app"),
    m.WithAttachDetachKeys("ctrl-q"),
)
if err != nil {
    return err
}
fmt.Println("python exited with", exitCode)
```


```
# Attach to the default shell
msb exec -t worker

# Attach to a specific command
msb exec -t worker -e DEBUG=1 -w /app -- python
```


Press `Ctrl+]` (or your configured detach keys) to detach from the session without stopping the process. The process keeps running inside the VM and you can reattach later via its session ID.


## [​](https://docs.microsandbox.dev/sandboxes/commands#write-stdin) Write stdin


TypeScript, Rust, Python, and Ruby can pass input bytes with the command. Ruby does not expose a streaming stdin writer; Go uses a pipe to supply input and collect the result.
TypeScript Rust Python Go Ruby

```
const output = await sandbox.execWith("cat", (e) => e.stdinBytes(Buffer.from("hello\n")));
console.log(output.stdout());
```


```
let output = sandbox.exec_with("cat", |e| e.stdin_bytes(b"hello\n".to_vec())).await?;
println!("{}", output.stdout()?);
```


```
output = await sandbox.exec("cat", stdin=b"hello\n")
print(output.stdout_text)
```


```
handle, err := sandbox.ExecStream(ctx, "cat", nil, m.WithExecStdinPipe())
if err != nil {
    return err
}
defer handle.Close()
stdin := handle.TakeStdin()
if _, err := stdin.Write([]byte("hello\n")); err != nil {
    return err
}
if err := stdin.Close(); err != nil {
    return err
}
output, err := handle.Collect(ctx)
if err != nil {
    return err
}
fmt.Print(output.Stdout())
```


```
output = sandbox.exec("cat", stdin: "hello\n")
puts output.stdout
```


Streaming handles can also accept stdin. Enable `stdin_pipe` and write bytes to it. Combined with `tty: true`, this lets you drive interactive processes programmatically.
TypeScript Rust Python Go

```
const handle = await sb.execStreamWith("python", (e) => e.stdinPipe().tty(true));
const stdin = await handle.takeStdin();
await stdin!.write("print('hello')\n");
await stdin!.write("exit()\n");
await stdin!.close();
await handle.wait();
```


```
let mut handle = sb.exec_stream_with("python", |e| e.stdin_pipe().tty(true)).await?;
let stdin = handle.take_stdin().unwrap();
stdin.write(b"print('hello')\n").await?;
stdin.write(b"exit()\n").await?;
handle.wait().await?;
```


```
from microsandbox import Stdin

handle = await sb.exec_stream("python", stdin=Stdin.pipe(), tty=True)
stdin = handle.take_stdin()
await stdin.write(b"print('hello')\n")
await stdin.write(b"exit()\n")
await stdin.close()
await handle.wait()
```


```
handle, err := sb.ExecStream(ctx, "python", nil, m.WithExecStdinPipe())
stdin := handle.TakeStdin()
_, _ = stdin.Write([]byte("print('hello')\n"))
_, _ = stdin.Write([]byte("exit()\n"))
_ = stdin.Close()
_, err = handle.Wait(ctx)
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#session-ids) Session IDs


Each streaming exec creates a session ID that you can use to correlate stream events and persisted log entries.
TypeScript Rust Python Go

```
const handle = await sb.execStream("python", ["server.py"])
const sessionId = handle.id
```


```
let handle = sb.exec_stream("python", ["server.py"]).await?;
let session_id = handle.id().to_string();
```


```
handle = await sb.exec_stream("python", ["server.py"])
session_id = handle.id
```


```
handle, err := sb.ExecStream(ctx, "python", []string{"server.py"})
if err != nil {
    return err
}
sessionID, err := handle.ID()
```


## [​](https://docs.microsandbox.dev/sandboxes/commands#reference) Reference


For exact execution APIs, see [TypeScript](https://docs.microsandbox.dev/sdk/typescript/execution), [Rust](https://docs.microsandbox.dev/sdk/rust/execution), [Python](https://docs.microsandbox.dev/sdk/python/execution), [Go](https://docs.microsandbox.dev/sdk/go/execution), or [Ruby](https://docs.microsandbox.dev/sdk/ruby/execution). For command-line execution, see [`msb run`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-run) and [`msb exec`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-exec).

Was this page helpful?

Yes No ⌘ I

---

# Microsandbox CLI installation and command reference

`https://docs.microsandbox.dev/cli/overview`

# CLI overview
## Documentation Index
## ​Install
## ​Quick start
## ​Command forms
## ​Quick reference
## ​Global options
## ​Output formatting
## ​Shell completion
## ​Command tree










Install the microsandbox CLI and manage local or cloud microVM sandboxes from your terminal.

Interactive sessions are detected automatically; no `-it` flags are needed.
Set an API key to use [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview). Each reference page marks local-only commands and cloud limitations.


## [​](https://docs.microsandbox.dev/cli/overview#install) Install


CLI (Linux & macOS) Homebrew (macOS) CLI (Windows)

```
curl -fsSL https://install.microsandbox.dev | sh
```


```
brew install superradcompany/tap/microsandbox
```


```
irm https://install.microsandbox.dev/windows | iex
```


On Linux and macOS, the install script writes the runtime to `~/.microsandbox/` and creates command links in `~/.local/bin/`. It does not edit shell startup files. If `~/.local/bin` is not on your `PATH`, the installer prints the command to add it. On macOS, Homebrew provides the same CLI through the official tap. On Windows, use PowerShell. Windows support is currently in preview.
Local sandboxes require Linux with glibc 2.28 or newer and KVM, an Apple Silicon Mac, or an x64 or ARM64 machine running Windows 10 or later with Windows Hypervisor Platform enabled. See [Linux troubleshooting](https://docs.microsandbox.dev/troubleshooting/linux), [macOS troubleshooting](https://docs.microsandbox.dev/troubleshooting/macos), or [Windows troubleshooting](https://docs.microsandbox.dev/troubleshooting/windows) for setup help.
Check your local setup with:
Shell

```
msb doctor
```


## [​](https://docs.microsandbox.dev/cli/overview#quick-start) Quick start


Shell

```
msb create python --name worker
msb exec worker -- python -c "print('hello')"
msb stop worker
msb rm worker
```


`msb run` without `--name` creates an ephemeral sandbox, removed when its command finishes. Named sandboxes persist. Names must contain 1–128 UTF-8 bytes.


## [​](https://docs.microsandbox.dev/cli/overview#command-forms) Command forms


Use short commands for everyday work. These forms are equivalent:
Shell

```
msb run alpine -- echo hello
msb sandbox run alpine -- echo hello
msb sbx run alpine -- echo hello
```


Aliases such as `ls`, `rm`, `cp`, and `mod` also work inside `sandbox` and `sbx`.
Saved-state operations are grouped under `msb snap`. The equivalent long form, `msb snapshot`, is also supported; this documentation uses `msb snap` consistently:
Shell

```
msb snap create ready --sandbox devbox --full
msb snap restore devbox:ready --name worker
msb snap ls --group devbox
msb snap export devbox:ready --output ready.msb
msb snap import ready.msb --group received
```


Snapshot behavior, aliases, and backend support

Omit `--full` to save disk state for a fresh boot. The group defaults to the source sandbox’s name, so the first command creates `devbox:ready`. Full captures, live forks, groups, and archive operations are local-only. Use `msb fork devbox --names worker-a worker-b` to create children directly from the same live moment. See [Snapshots](https://docs.microsandbox.dev/sandboxes/snapshots) for backend limits and resource bindings. Existing top-level `restore` and snapshot `save` / `load` commands remain supported.


## [​](https://docs.microsandbox.dev/cli/overview#quick-reference) Quick reference


| Commands | Purpose |
| --- | --- |
| [`run`, `create`, `start`, `stop`, `restart`](https://docs.microsandbox.dev/cli/sandbox-commands) | Manage sandbox lifecycles |
| [`exec`, `copy`, `logs`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-exec) | Run commands and access files or output |
| [`ls`, `ps`, `inspect`, `metrics`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-ls) | Inspect sandboxes |
| [`modify`, `pause`, `resume`, `fork`, `rm`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-modify) | Change, fork, or remove sandboxes |
| [`snap`](https://docs.microsandbox.dev/cli/snapshot-commands) | Save and restore state |
| [`ssh`](https://docs.microsandbox.dev/cli/ssh-commands) | SSH sessions, keys, and listeners |
| [`volume`, `volumes`](https://docs.microsandbox.dev/cli/volume-commands) | Manage named storage |
| [`df`, `prune`](https://docs.microsandbox.dev/cli/storage-commands) | Inspect local storage and reclaim unused runtime RAM |
| [`pull`, `load`, `save`, `images`, `rmi`, `image`](https://docs.microsandbox.dev/cli/image-commands) | Manage cached images |
| [`registry`, `registries`](https://docs.microsandbox.dev/cli/registry-commands) | Manage registry credentials |
| [`context`](https://docs.microsandbox.dev/cli/management#msb-context) | Show the active backend |
| [`install`, `uninstall`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-install) | Turn sandboxes into shell commands |
| [`doctor`, `update`, `downgrade`, `self`](https://docs.microsandbox.dev/cli/management#msb-self) | Manage the CLI installation |
| [`completion`](https://docs.microsandbox.dev/cli/overview#shell-completion) | Generate shell completions |


## [​](https://docs.microsandbox.dev/cli/overview#global-options) Global options


| Flag | Description |
| --- | --- |
| `--tree` | Display the complete command tree with descriptions |
| `-L, --levels <N>` | Limit tree depth, counting the selected root as level 0 (requires `--tree`) |
| `-C, --commands` | Hide flags and arguments in the command tree (requires `--tree`) |
| `-b, --brief` | Omit descriptions from the command tree (requires `--tree`) |
| `--error` | Show only errors |
| `--warn` | Show warnings and errors |
| `--info` | Show info, warnings, and errors |
| `--debug` | Show debug output |
| `--trace` | Show all output including trace |


## [​](https://docs.microsandbox.dev/cli/overview#output-formatting) Output formatting


Command results normally go to stdout; progress and diagnostics go to stderr. Use JSON output when a command supports it for scripting.


Streams, units, and output exceptions

Progress, styled action confirmations, warnings, and errors go to stderr. Tables, inspection results, and JSON go to stdout. Empty-list messages retain their command-specific behavior: the registry empty-list message goes to stdout, while listing installed aliases produces no output when none exist. The plain `snapshot reindex` completion message also remains on stdout. Indented output uses two spaces, with nested content at four spaces. Human-readable image, snapshot, and volume sizes use binary units (KiB, MiB, GiB, TiB); JSON retains its documented numeric fields.


## [​](https://docs.microsandbox.dev/cli/overview#shell-completion) Shell completion


`msb completion <shell>` prints a completion script for `bash`, `zsh`, `fish`, `elvish`, or `powershell`. Write it to the location your shell loads completions from:
bash zsh fish elvish PowerShell

```
# Requires the bash-completion package. Without it, add this line to
# ~/.bashrc instead:  source <(msb completion bash)
mkdir -p ~/.local/share/bash-completion/completions
msb completion bash > ~/.local/share/bash-completion/completions/msb
```


```
mkdir -p ~/.zsh/completions
msb completion zsh > ~/.zsh/completions/_msb
# Add this line to ~/.zshrc before compinit runs:
#   fpath=(~/.zsh/completions $fpath)
```


```
mkdir -p ~/.config/fish/completions
msb completion fish > ~/.config/fish/completions/msb.fish
```


```
mkdir -p ~/.config/elvish/completions
msb completion elvish > ~/.config/elvish/completions/msb.elv
# Add this line to ~/.config/elvish/rc.elv:
#   eval (slurp < ~/.config/elvish/completions/msb.elv)
```


```
$completions = Join-Path (Split-Path $PROFILE) "completions"
New-Item -Path $completions -ItemType Directory -Force | Out-Null
msb completion powershell > (Join-Path $completions "msb.ps1")
# Add this line to your profile ($PROFILE):
#   . "$PSScriptRoot/completions/msb.ps1"
```


Restart your shell. Regenerate saved completions after upgrading.


## [​](https://docs.microsandbox.dev/cli/overview#command-tree) Command tree


Use `--tree` as an alternative to `--help` to see every command, subcommand, and flag at once:
Shell

```
msb --tree
```


You can scope it to a specific subcommand:
Shell

```
msb image --tree    # Show only image commands
msb volume --tree   # Show only volume commands
msb run --tree      # Show all flags for run
msb sandbox --tree  # Show the canonical sandbox command group
msb sbx run --tree  # Show run flags through the group alias
```


Limit the depth or hide flags and arguments for a compact command overview:
Shell

```
msb --tree -L 2
msb --tree --commands
msb image --tree --commands -L 1
msb --tree --brief --commands -L 2
msb --tree -Cb -L 2
```


Tree depth and display rules

`-L N` (or `--levels N`) counts the selected root as level 0, so `-L 1` shows its immediate children and `-L 0` shows only the root. Omitting the limit shows all levels. At the depth limit, an inline marker such as `… 4 subcommands, 2 arguments` counts the immediate children that were collapsed; arguments include both flags and positional arguments. Hidden commands and options are excluded, and `--commands` excludes arguments from both the tree and these counts. `--brief` omits command and argument descriptions and their alignment padding, while retaining names, aliases, value placeholders, and collapse counts. It works with both `-L` and `--commands`.

Was this page helpful?

Yes No ⌘ I

---

# Overview - microsandbox

`https://docs.microsandbox.dev/networking/overview`

# Overview

Microsandbox checks sandbox traffic against a host-controlled network policy. Start with the defaults, then allow only the destinations and ports your workload needs.


## [​](https://docs.microsandbox.dev/networking/overview#defaults) Defaults


Sandboxes can reach the public internet by default. Private networks, the host, loopback, link-local addresses, and cloud metadata endpoints are blocked. Inbound traffic needs a published port.
To isolate a sandbox from the network:
TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("isolated")
    .image("python")
    .disableNetwork()
    .create();
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("isolated")
    .image("python")
    .network(|n| n.enabled(false))
    .create()
    .await?;
```


```
from microsandbox import Network, Sandbox

sb = await Sandbox.create("isolated", image="python", network=Network.none())
```


```
sb, err := m.CreateSandbox(ctx, "isolated",
    m.WithImage("python"),
    m.WithNetwork(m.NetworkPolicy.None()),
)
```


```
sb = Microsandbox::Sandbox.create("isolated", image: "python", network: :none)
```


```
msb create python --name isolated --no-net
```


The TypeScript and Rust examples disable the network device. Python `Network.none()`, Go `NetworkPolicy.None()`, and CLI `--no-net` keep the device but deny traffic in both directions.
Ruby exposes network disablement, host/port allowlists, proxies, and basic TLS interception. Deployment profiles, policy profiles, NAT64, port publishing, and rate limits require TypeScript, Rust, Python, Go, or the CLI; see the [Ruby networking reference](https://docs.microsandbox.dev/sdk/ruby/networking) for its available options.


## [​](https://docs.microsandbox.dev/networking/overview#deployment-profiles) Deployment profiles


Local sandboxes use `single-tenant` by default. Use `multi-tenant` for shared hosts: it enforces public-network access, DNS rebinding protection, and stricter limits. Sandbox policies can restrict access further. Cloud chooses its own profile.
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("shared-worker")
    .image("python")
    .deploymentProfile("multi-tenant")
    .create();
```


```
use microsandbox::sandbox::DeploymentProfile;
use microsandbox::Sandbox;

let sb = Sandbox::builder("shared-worker")
    .image("python")
    .deployment_profile(DeploymentProfile::MultiTenant)
    .create()
    .await?;
```


```
from microsandbox import DeploymentProfile, Sandbox

sb = await Sandbox.create(
    "shared-worker",
    image="python",
    deployment_profile=DeploymentProfile.MULTI_TENANT,
)
```


```
sb, err := m.CreateSandbox(ctx, "shared-worker",
    m.WithImage("python"),
    m.WithDeploymentProfile(m.DeploymentProfileMultiTenant),
)
```


```
msb create python --name shared-worker --deployment-profile multi-tenant
## Documentation Index
## ​Defaults
## ​Deployment profiles
## ​High-level profiles
## ​Low-level custom policies
## ​NAT64 prefixes
## ​Hostname rules and HTTPS
## ​Port mapping
## ​Rate limits
## ​HTTP denial responses
## ​Reaching the host
## ​Reference
## ​Next













```


Deployment restrictions and operator settings

In `multi-tenant` mode, traffic must pass both the platform’s public-network policy and the sandbox’s policy. Custom DNS servers and interface overrides are removed; host CA import and published ports are disabled. The sandbox cannot relax these restrictions. An operator can set `deployment_profile` in `~/.microsandbox/config.json` or on `LocalBackend`. This overrides the sandbox’s choice on create and restart. Managed cloud requests do not carry a deployment profile; the hosting driver selects it.


Connection limits and compatibility

The per-sandbox `maxTcpConnections` setting optionally limits concurrent TCP connections. `maxConnections` remains a deprecated TCP-only alias. When omitted, `single-tenant` has no connection-count cap and `multi-tenant` defaults to 1,024. An explicit positive value overrides either default; zero explicitly selects unlimited. These are runtime defaults, not operator-enforced ceilings. Services accepting tenant configuration must enforce their own policy on overrides. Legacy v0.6.x launch contracts keep their historical default of 256 TCP connections when the limit is omitted. The current SDK rejects explicit unlimited TCP connections, values above 4,096, or multi-tenant values above 256 when launching an older runtime because those peers cannot preserve the requested meaning. A current runtime also rejects legacy zero TCP limits: old zero meant deny all connections, not unlimited. Current-contract defaults and explicit limits are unchanged. `maxUdpConnections` independently limits host-side UDP relay sessions. Omission is unlimited in `single-tenant` mode and defaults to 1,024 in `multi-tenant` mode; zero explicitly selects unlimited. At a finite limit, a new session evicts the least recently active session. Sessions expire after 60 seconds of inactivity. Historical runtime launch contracts do not support an explicit UDP limit, including zero; the SDK rejects that override with an upgrade-required error instead of silently ignoring it. Each tracked TCP socket currently allocates 64 KiB for receiving and 64 KiB for
sending. A ceiling of 1024 therefore requires up to 128 MiB of socket-buffer
capacity per sandbox, in addition to other runtime allocations. Reserve that
capacity on the host when configuring a ceiling. Selecting unlimited does not
remove memory or operating-system resource constraints. Closing sockets remain tracked
until their TCP state permits removal. Host file descriptors and shared egress
source ports impose additional constraints.


## [​](https://docs.microsandbox.dev/networking/overview#high-level-profiles) High-level profiles


Combine `public`, `private`, and `host` to allow those destination groups. Use `none` to deny all traffic or `all` to allow all traffic. This example allows public and private networks:
TypeScript Rust Python Go CLI

```
import { NetworkPolicy, Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .network((n) => n.policy(NetworkPolicy.fromProfiles(["public", "private"])))
    .create();
```


```
use microsandbox::{NetworkPolicy, NetworkProfile, Sandbox};

let policy = NetworkPolicy::from_profiles([NetworkProfile::Public, NetworkProfile::Private]);
let sb = Sandbox::builder("worker")
    .image("python")
    .network(|n| n.policy(policy))
    .create()
    .await?;
```


```
from microsandbox import Network, NetworkProfile, Sandbox

sb = await Sandbox.create(
    "worker",
    image="python",
    network=Network.from_profiles(NetworkProfile.PUBLIC, NetworkProfile.PRIVATE),
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithNetwork(m.NetworkPolicy.FromProfiles(m.NetworkProfilePublic, m.NetworkProfilePrivate)),
)
```


```
msb create python --name worker --net "public,private"
```


Add `host` for services on your machine; see [Reaching the host](https://docs.microsandbox.dev/networking/overview#reaching-the-host). Duplicate profiles are ignored. Explicit rules placed before profile rules take precedence.


## [​](https://docs.microsandbox.dev/networking/overview#low-level-custom-policies) Low-level custom policies


For finer control, set default actions and add rules. The first matching rule wins. This example allows public HTTPS and gateway DNS while denying other outbound traffic:
TypeScript Rust Python Go CLI

```
import { NetworkPolicy, Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("restricted-worker")
    .image("alpine")
    .network((n) => n.policy(
        NetworkPolicy.builder()
            .defaultDeny()
            .egress((e) => e.tcp().port(443).allowPublic())
            .egress((e) => e.udp().tcp().port(53).allowHost())
            .build(),
    ))
    .create();
```


```
use microsandbox::{NetworkPolicy, Sandbox};

let policy = NetworkPolicy::builder()
    .default_deny()
    .egress(|e| e.tcp().port(443).allow_public())
    .egress(|e| e.udp().tcp().port(53).allow_host())
    .build()?;

let sb = Sandbox::builder("restricted-worker")
    .image("alpine")
    .network(|n| n.policy(policy))
    .create()
    .await?;
```


```
from microsandbox import Action, DestGroup, Destination, Network, NetworkPolicy, Protocol, Rule, Sandbox

sb = await Sandbox.create(
    "restricted-worker",
    image="alpine",
    network=Network(policy=NetworkPolicy(
        default_egress=Action.DENY,
        rules=(
            Rule.allow(destination=Destination.group(DestGroup.PUBLIC), protocol=Protocol.TCP, port=443),
            *Rule.allow_dns(),
        ),
    )),
)
```


```
sb, err := m.CreateSandbox(ctx, "restricted-worker",
    m.WithImage("alpine"),
    m.WithNetwork(&m.NetworkConfig{
        DefaultEgress: m.PolicyActionDeny,
        Rules: []m.PolicyRule{
            {Action: m.PolicyActionAllow, Direction: m.PolicyDirectionEgress, Destination: "public", Protocol: m.PolicyProtocolTCP, Port: "443"},
            m.Rule.AllowDNS(),
        },
    }),
)
```


```
msb create alpine --name restricted-worker \
  --net-default-egress deny \
  --net-rule "allow@public:tcp:443,allow@dns"
```


Rules can match destination groups, IPs, CIDRs, domains, and ports. See the [CLI rule syntax](https://docs.microsandbox.dev/cli/sandbox-commands#network-rule-syntax) or an [SDK reference](https://docs.microsandbox.dev/networking/overview#reference) for exact options.


## [​](https://docs.microsandbox.dev/networking/overview#nat64-prefixes) NAT64 prefixes


NAT64 lets IPv6 networks reach IPv4 destinations. Microsandbox checks both addresses against policy, so translated private and metadata addresses stay blocked. The standard `64:ff9b::/96` prefix is included by default.
If your local network routes another `/96` prefix, add it like this:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("translated")
    .image("python")
    .network((n) => n.nat64Prefix("64:ff9b:1::/96"))
    .create();
```


```
use microsandbox::Sandbox;

let prefix = "64:ff9b:1::/96".parse()?;
let sb = Sandbox::builder("translated")
    .image("python")
    .network(|n| n.nat64_prefix(prefix))
    .create()
    .await?;
```


```
from microsandbox import Network, Sandbox

sb = await Sandbox.create(
    "translated",
    image="python",
    network=Network(nat64_prefixes=("64:ff9b::/96", "64:ff9b:1::/96")),
)
```


```
sb, err := m.CreateSandbox(ctx, "translated",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        NAT64Prefixes: []string{"64:ff9b::/96", "64:ff9b:1::/96"},
    }),
)
```


```
msb create python --name translated --net-nat64-prefix 64:ff9b:1::/96
```


This setting classifies traffic; it does not set up NAT64 routing. Cloud rejects custom or empty prefix lists. See [CLI options](https://docs.microsandbox.dev/cli/sandbox-commands#network-profiles) for details.


## [​](https://docs.microsandbox.dev/networking/overview#hostname-rules-and-https) Hostname rules and HTTPS


Allow specific domains with hostname rules. By default, HTTPS allowed only by a hostname rule requires [TLS inspection](https://docs.microsandbox.dev/networking/tls), so microsandbox can check the hostname inside the request:
TypeScript Rust Python Go Ruby CLI

```
import { NetworkPolicy, Sandbox } from "microsandbox";

const policy = NetworkPolicy.builder()
    .defaultDeny()
    .egress((e) => e.tcp().port(443).allowDomain("github.com"))
    .egress((e) => e.udp().tcp().port(53).allowHost())
    .build();

await using sb = await Sandbox.builder("github-only")
    .image("python")
    .network((n) => n.policy(policy))
    .interceptTls()
    .create();
```


```
use microsandbox::{NetworkPolicy, Sandbox};

let policy = NetworkPolicy::builder()
    .default_deny()
    .egress(|e| e.tcp().port(443).allow_domains(["github.com"]))
    .egress(|e| e.udp().tcp().port(53).allow_host())
    .build()?;

let sb = Sandbox::builder("github-only")
    .image("python")
    .network(|n| n.policy(policy))
    .intercept_tls()
    .create()
    .await?;
```


```
from microsandbox import Action, Destination, Network, NetworkPolicy, Protocol, Rule, Sandbox

sb = await Sandbox.create(
    "github-only",
    image="python",
    network=Network(policy=NetworkPolicy(
        default_egress=Action.DENY,
        rules=(
            Rule.allow(destination=Destination.domain("github.com"), protocol=Protocol.TCP, port=443),
            *Rule.allow_dns(),
        ),
    )),
    intercept_tls=True,
)
```


```
sb, err := m.CreateSandbox(ctx, "github-only",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        DefaultEgress: m.PolicyActionDeny,
        Rules: []m.PolicyRule{
            {Action: m.PolicyActionAllow, Direction: m.PolicyDirectionEgress, Destination: "github.com", Protocol: m.PolicyProtocolTCP, Port: "443"},
            m.Rule.AllowDNS(),
        },
    }),
    m.WithInterceptTLS(),
)
```


```
sb = Microsandbox::Sandbox.create(
  "github-only",
  image: "python",
  network: { allowed_hosts: ["github.com"], allowed_ports: [443] },
  intercept_tls: true
)
```


```
msb create python --name github-only \
  --net-default-egress deny \
  --net-rule "allow@github.com:tcp:443,allow@dns" \
  --tls-intercept
```


How strict hostname checks work

Domain and domain-suffix rules start with the hostname microsandbox can observe. DNS rules see the query name, and TLS connections usually expose SNI before the encrypted session starts. That is enough to decide whether a connection may be opened, but it is not the same as seeing the HTTP request authority. For plaintext HTTP, microsandbox can inspect the `Host` header and require it to match the hostname that policy allowed. For HTTPS without TLS interception, or for a host that is configured to bypass interception, the HTTP `Host` header and HTTP/2 `:authority` value are encrypted. In that case microsandbox cannot prove which application hostname the request is using after the TLS session starts. Strict hostname policy mode is enabled by default: hostname allowlists fail closed unless microsandbox can inspect the request authority. In strict mode, hostname-based allow rules still work for plaintext HTTP and TLS-intercepted HTTPS. Non-intercepted HTTPS is denied when it would otherwise be allowed only by a hostname rule. IP, CIDR, group, and default allow rules are not treated as hostname-based allows. Set `--net-strict=false` or `network.strict: false` in sandbox configuration to opt out.


## [​](https://docs.microsandbox.dev/networking/overview#port-mapping) Port mapping


Publish a guest port to your host machine. This example forwards host port `8080` to guest port `80`, listening on `127.0.0.1` by default. Port publishing is local-only.
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("api")
    .image("python")
    .port(8080, 80)
    .create();
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("api")
    .image("python")
    .port(8080, 80)
    .create()
    .await?;
```


```
from microsandbox import PortBinding, Sandbox

sb = await Sandbox.create("api", image="python", ports=[PortBinding.tcp(8080, 80)])
```


```
sb, err := m.CreateSandbox(ctx, "api",
    m.WithImage("python"),
    m.WithPorts(map[uint16]uint16{8080: 80}),
)
```


```
msb create python --name api -p 8080:80
```


Bind addresses, port ranges, and Windows

Use an explicit bind address, such as `0.0.0.0`, only when you intentionally want to listen beyond localhost. `-p 8080:80` and SDK helpers like `.port(8080, 80)` bind to `127.0.0.1`; `-p 127.0.0.1:8080:80` is the same loopback-only shape. `-p 0.0.0.0:8080:80` or a specific LAN interface address makes the host listener reachable outside the machine, subject to your OS firewall and network policy. If the host starts without IPv4 or IPv6 routes, microsandbox assigns private guest addresses for published ports unless guest addresses are already configured. A specific host bind address must still exist at startup. CLI `-p` and YAML `ports` lists also accept inclusive, equal-length port ranges: `-p 8000-8002:80-82` forwards three TCP ports, while `-p 0.0.0.0:10240-11264:10240-11264/udp` publishes 1,025 UDP ports. Ranges expand into the same individual mappings used by the SDKs, with one host socket per port. See [Published ports](https://docs.microsandbox.dev/cli/sandbox-commands#published-ports) for validation and host resource requirements. On Windows, the first published port may trigger a Windows Defender Firewall prompt for `msb.exe` because the runtime opens a host listening socket. For local development, keep the bind address on `127.0.0.1`. Only allow private/public network access in the firewall prompt when you intentionally bind a published port beyond loopback.


## [​](https://docs.microsandbox.dev/networking/overview#rate-limits) Rate limits


Limit inbound or outbound bandwidth and packet rate on local sandboxes. Omitted limits leave traffic unthrottled; changes take effect on the next start. Cloud does not support this setting.
This example allows 1 MiB/s outbound, a one-time 512 KiB burst, and 1,000 packets per second:
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("throttled")
    .image("python")
    .network((n) => n.rateLimiter((r) => r.egress((r) => r
        .bandwidth(1_048_576, 1_000)
        .bandwidthBurst(524_288)
        .ops(1_000, 1_000))))
    .create();
```


```
use std::time::Duration;

use microsandbox::size::SizeExt;
use microsandbox::Sandbox;

let sb = Sandbox::builder("throttled")
    .image("python")
    .network(|n| n.rate_limiter(|r| r.egress(|r| r
        .bandwidth(1.mib(), Duration::from_secs(1))
        .bandwidth_burst(512.kib())
        .ops(1_000, Duration::from_secs(1)))))
    .create()
    .await?;
```


```
from microsandbox import Network, NetworkRateLimiter, RateLimiter, Sandbox, TokenBucket

sb = await Sandbox.create(
    "throttled",
    image="python",
    network=Network(
        rate_limiter=NetworkRateLimiter(
            egress=RateLimiter(
                bandwidth=TokenBucket(size=1_048_576, refill_time_ms=1_000, one_time_burst=524_288),
                ops=TokenBucket(size=1_000, refill_time_ms=1_000),
            ),
        ),
    ),
)
```


```
sb, err := m.CreateSandbox(ctx, "throttled",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        RateLimiter: &m.NetworkRateLimiterConfig{
            Egress: &m.RateLimiterConfig{
                Bandwidth: &m.TokenBucketConfig{Size: 1 << 20, RefillTime: time.Second, OneTimeBurst: 512 << 10},
                Ops:       &m.TokenBucketConfig{Size: 1000, RefillTime: time.Second},
            },
        },
    }),
)
```


```
msb create python --name throttled \
  --net-egress-bandwidth 1M/1s \
  --net-egress-bandwidth-burst 512K \
  --net-egress-ops 1000/1s
```


How limits and bursts are applied

Network rate limits apply only to traffic crossing a sandbox’s virtual network device. They do not limit CPU, memory, disk I/O, API requests, or how many sandboxes can run. If you do not configure a limiter, microsandbox does not throttle the sandbox’s network bandwidth or packet rate. Once configured, the limiter is enforced independently for outbound (egress) and inbound (ingress) traffic. For each direction, you can configure a bandwidth bucket measured in bytes per refill interval, a packet-rate bucket measured in packets per interval, or both. An omitted direction or bucket remains unthrottled. Buckets start full, refill continuously, and can include a one-time startup burst that does not refill. Limits are set at creation and take effect on the next sandbox start. The `--net-ingress-*` flags mirror the egress flags for inbound traffic (`--net-ingress-bandwidth`, `--net-ingress-bandwidth-burst`, `--net-ingress-ops`, `--net-ingress-ops-burst`). Sizes accept raw bytes plus `K`, `M`, and `G` suffixes; the interval defaults to one second when omitted. A frame larger than the bandwidth bucket is delivered once and the limiter then pauses long enough to pay it off, so oversized packets are throttled instead of stuck.


## [​](https://docs.microsandbox.dev/networking/overview#http-denial-responses) HTTP denial responses


Local-only
Supported denied HTTP requests return JSON `403` responses with `code`, `message`, and `domain` fields. Set separate messages for network and secret-policy blocks:
TypeScript Rust Python Go Ruby sandbox.yml

```
await using sb = await Sandbox.builder("agent")
    .image("python")
    .network((n) => n.http((h) => h
            .denyResponse(true)
            .denyResponseFormat("json")
            .networkDenyMessage("Ask the user for network access.")
            .secretDenyMessage("Ask the user to review secret access.")))
    .create();
```


```
use microsandbox::sandbox::HttpDenyResponseFormat;

let sb = Sandbox::builder("agent")
    .image("python")
    .network(|n| n.http(|h| h
            .deny_response(true)
            .deny_response_format(HttpDenyResponseFormat::Json)
            .network_deny_message("Ask the user for network access.")
            .secret_deny_message("Ask the user to review secret access.")))
    .create()
    .await?;
```


```
from microsandbox import HttpConfig, Network, Sandbox

sb = await Sandbox.create(
    "agent",
    image="python",
    network=Network(
        http=HttpConfig(
            deny_response=True,
            deny_response_format="json",
            network_deny_message="Ask the user for network access.",
            secret_deny_message="Ask the user to review secret access.",
        ),
    ),
)
```


```
sb, err := m.CreateSandbox(ctx, "agent",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        HTTP: &m.HTTPConfig{
            DenyResponse: true,
            DenyResponseFormat: m.HTTPDenyResponseJSON,
            NetworkDenyMessage: "Ask the user for network access.",
            SecretDenyMessage: "Ask the user to review secret access.",
        },
    }),
)
```


```
sb = Microsandbox::Sandbox.create(
  "agent",
  image: "python",
  http: {
    deny_response: true,
    deny_response_format: "json",
    network_deny_message: "Ask the user for network access.",
    secret_deny_message: "Ask the user to review secret access."
  }
)
```


```
network:
  http:
    deny_response: true
    deny_response_format: json
    network_deny_message: "Ask the user for network access."
    secret_deny_message: "Ask the user to review secret access."
```


Messages are literal; the destination is in `domain`. Check the HTTP status, or use `curl --fail` to make a `403` return a nonzero exit code. Set `deny_response: false` to close denied connections without a response.


Which requests receive a response?


- Responses cover HTTP/1.0 and HTTP/1.1. HTTPS needs [TLS interception](https://docs.microsandbox.dev/networking/tls) without a host bypass. Network-policy denials never reach the upstream server.
- Secret-policy denials can respond only to the first request, before any upstream response bytes. Later or pipelined requests, an upstream response (including `100 Continue`), `HEAD`, `CONNECT`, `block-and-terminate`, and unsupported body substitution close the connection instead.
- DNS denials return `NXDOMAIN`. HTTP/2, other protocols, malformed or incomplete requests, and silent clients close without an HTTP response.


Response format

JSON responses use `Content-Type: application/json`. Match `code` to identify the error and display `message` to the user. `domain` is the requested hostname, an IP address fallback for network denials, or `null` when unknown. Network-policy denial:

```
{
  "code": "network_policy_denied",
  "message": "Request blocked by network policy.",
  "domain": "example.com"
}
```

Secret-policy denial:

```
{
  "code": "secret_policy_denied",
  "message": "Request blocked by secret policy.",
  "domain": "example.com"
}
```

Custom messages are JSON-escaped; omitted messages use the defaults. v0.7.8 supports opt-in `text` mode for network denials: `deny_message` expands `{host}`, while secret-policy violations close without a response. JSON mode requires a newer runtime. Changing the message or format does not override `deny_response: false`.


## [​](https://docs.microsandbox.dev/networking/overview#reaching-the-host) Reaching the host


`host.microsandbox.internal` points to the host machine from inside a local sandbox. The default policy blocks it, so allow the `host` group when the guest needs a local service:
TypeScript Rust Python Go CLI

```
import { NetworkPolicy, Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("devbox")
    .image("python")
    .network((n) => n.policy(NetworkPolicy.fromProfiles(["public", "host"])))
    .create();
```


```
use microsandbox::{NetworkPolicy, NetworkProfile, Sandbox};

let policy = NetworkPolicy::from_profiles([NetworkProfile::Public, NetworkProfile::Host]);
let sb = Sandbox::builder("devbox")
    .image("python")
    .network(|n| n.policy(policy))
    .create()
    .await?;
```


```
from microsandbox import Network, NetworkProfile, Sandbox

sb = await Sandbox.create(
    "devbox",
    image="python",
    network=Network.from_profiles(NetworkProfile.PUBLIC, NetworkProfile.HOST),
)
```


```
sb, err := m.CreateSandbox(ctx, "devbox",
    m.WithImage("python"),
    m.WithNetwork(m.NetworkPolicy.FromProfiles(m.NetworkProfilePublic, m.NetworkProfileHost)),
)
```


```
msb create python --name devbox --net "public,host"
```


Guest `127.0.0.1` is inside the sandbox, not the host. On cloud, the `host` group refers to the cloud worker, not the machine running your SDK.


## [​](https://docs.microsandbox.dev/networking/overview#reference) Reference


For exact APIs, see [TypeScript](https://docs.microsandbox.dev/sdk/typescript/networking), [Rust](https://docs.microsandbox.dev/sdk/rust/networking), [Python](https://docs.microsandbox.dev/sdk/python/networking), [Go](https://docs.microsandbox.dev/sdk/go/networking), or [Ruby](https://docs.microsandbox.dev/sdk/ruby/networking). For flags and configuration, see [Sandbox commands](https://docs.microsandbox.dev/cli/sandbox-commands#network-profiles) and [Sandbox configuration](https://docs.microsandbox.dev/cli/configuration#network).


## [​](https://docs.microsandbox.dev/networking/overview#next) Next


- [DNS](https://docs.microsandbox.dev/networking/dns): nameservers and domain blocking
- [Outbound proxies](https://docs.microsandbox.dev/networking/outbound-proxy): route traffic through a proxy
- [TLS inspection](https://docs.microsandbox.dev/networking/tls): inspect HTTPS traffic
- [Host sockets](https://docs.microsandbox.dev/networking/host-sockets): connect to host IPC without a TCP port
- [Network security](https://docs.microsandbox.dev/security/network): understand the policy boundary and defenses


Was this page helpful?

Yes No ⌘ I

---

# Windows - microsandbox

`https://docs.microsandbox.dev/troubleshooting/windows`

Windows support is currently in preview. To run sandboxes locally, use Windows 10 or later on an x64 or ARM64 machine and enable Windows Hypervisor Platform (WHP).


## [​](https://docs.microsandbox.dev/troubleshooting/windows#install-or-reinstall) Install or reinstall


Run the installer in PowerShell, then open a new terminal:
PowerShell

```
irm https://install.microsandbox.dev/windows | iex
```


## [​](https://docs.microsandbox.dev/troubleshooting/windows#quick-checks) Quick checks


Start with the doctor command:
PowerShell

```
msb doctor
```


If the only failure is Windows Hypervisor Platform setup, let `msb` open the elevated fix prompt:
PowerShell

```
msb doctor --fix
```


`msb doctor --fix` keeps the normal doctor command free of host-configuration changes. The normal check may create and immediately remove a small clone-capability probe inside `MSB_HOME`. The fix path opens an elevated PowerShell window and applies the supported host setup change.


## [​](https://docs.microsandbox.dev/troubleshooting/windows#windows-hypervisor-platform) Windows Hypervisor Platform


microsandbox uses Windows Hypervisor Platform through libkrun. If you prefer to enable it manually, run this from an elevated PowerShell and reboot after it completes:
PowerShell

```
Enable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -All -NoRestart
```


`HypervisorPlatform` is separate from `VirtualMachinePlatform`, which Docker Desktop and WSL2 commonly enable. microsandbox needs `HypervisorPlatform` because that exposes the WHP API used by libkrun.
You can check the feature state with:
PowerShell

```
Get-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform
```


If the feature is enabled but `msb doctor` still reports that the hypervisor is unavailable, confirm that virtualization is enabled in firmware/UEFI, then reboot once.


## [​](https://docs.microsandbox.dev/troubleshooting/windows#runtime-path) Runtime path


The default Windows runtime root is `%USERPROFILE%\.microsandbox`. The CLI binary lives under `bin\msb.exe`, and the runtime library lives under `lib\libkrunfw.dll`.
If Windows is finding a stale binary, check the command path:
PowerShell

```
where.exe msb
```


If an error mentions `libkrunfw.so` or `libkrunfw.dylib`, clear any old Unix/macOS override in `MSB_LIBKRUNFW_PATH` or `config.json`, or point it at `libkrunfw.dll`.


## [​](https://docs.microsandbox.dev/troubleshooting/windows#updates-and-reinstalls) Updates and reinstalls


`msb self update` stages and verifies the new Windows release before scheduling the installed files for replacement. The command can exit while another `msb` or `microsandbox` process still has an executable locked. The background task keeps retrying and writes its progress to the log path printed by the command.
The PowerShell installer checks both public executable names before changing the installation. If it reports that an executable is still running, stop the listed process or its active sandbox, then rerun the installer.


## [​](https://docs.microsandbox.dev/troubleshooting/windows#firewall-and-terminals) Firewall and terminals


Published ports open a listening socket on the Windows host. Windows Defender Firewall can prompt the first time `msb.exe` opens that listener. For local development, keep published ports bound to `127.0.0.1`; only allow private or public network access when you intentionally bind beyond loopback.
Windows Terminal, PowerShell, and cmd are supported for normal interactive attach flows. Run interactive commands from a real console, not from a redirected CI shell or background task. That lets `msb` read input, forward resize events, and restore the console when the session exits.
## Documentation Index
## ​Install or reinstall
## ​Quick checks
## ​Windows Hypervisor Platform
## ​Runtime path
## ​Updates and reinstalls
## ​Firewall and terminals








Was this page helpful?

Yes No ⌘ I

---

# Linux - microsandbox

`https://docs.microsandbox.dev/troubleshooting/linux`

microsandbox local sandboxes use hardware virtualization. On Linux, confirm that the host has glibc 2.28 or newer and that KVM is available through `/dev/kvm`.


## [​](https://docs.microsandbox.dev/troubleshooting/linux#install-or-reinstall) Install or reinstall


Run the installer, then open a new terminal if it updates your `PATH`:
Shell

```
curl -fsSL https://install.microsandbox.dev | sh
```


## [​](https://docs.microsandbox.dev/troubleshooting/linux#glibc-version) glibc version


Microsandbox Linux releases require glibc 2.28 or newer on x64 and ARM64 hosts. Check the version provided by your distribution:
Shell

```
getconf GNU_LIBC_VERSION
```


If `getconf` is unavailable, inspect the first line reported by `ldd`:
Shell

```
ldd --version | head -n 1
```


Use a newer glibc-based distribution if the version is below 2.28. Do not replace the system C library manually. Musl-only environments, such as a bare Alpine host, cannot run the local runtime; use a supported host or [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview) instead.


## [​](https://docs.microsandbox.dev/troubleshooting/linux#quick-checks) Quick checks


Start with the doctor command for the local setup checks:
Shell

```
msb doctor
```


If sandbox startup still fails with a KVM-related error, check the KVM module and device:
Shell

```
lsmod | grep kvm
ls -l /dev/kvm
```


An enabled Intel host usually shows `kvm_intel` and `kvm`; an enabled AMD host usually shows `kvm_amd` and `kvm`.
Then confirm that your current user can read and write the KVM device:
Shell

```
[ -r /dev/kvm ] && [ -w /dev/kvm ] && echo "OK" || echo "FAIL"
```


## [​](https://docs.microsandbox.dev/troubleshooting/linux#missing-/dev/kvm) Missing `/dev/kvm`


If `/dev/kvm` is missing, make sure CPU virtualization is enabled in firmware/UEFI and visible to Linux:
Shell

```
grep -E -c '(vmx|svm)' /proc/cpuinfo
```


A `0` result usually means virtualization is disabled in firmware, unavailable on the machine, or hidden by an outer VM. After enabling virtualization in firmware, reboot and check the KVM module again.
You can also try loading the host-specific KVM module:
Shell

```
sudo modprobe kvm_intel  # Intel
sudo modprobe kvm_amd    # AMD
```


If you are inside a cloud VM, CI runner, or another hypervisor, the outer environment must expose nested virtualization before `/dev/kvm` can appear.


## [​](https://docs.microsandbox.dev/troubleshooting/linux#permission-denied) Permission denied


If `/dev/kvm` exists but sandbox startup fails with a permission error, your user probably cannot open the device. Check the device owner and group:
Shell

```
stat -c '%U %G %a %n' /dev/kvm
```


Many distributions grant access through the `kvm` group. Check whether the group exists, whether `/dev/kvm` uses it, and whether your shell is already in that group:
Shell

```
getent group kvm
ls -l /dev/kvm
groups
```


If `/dev/kvm` belongs to `kvm`, add your user to the group:
Shell

```
sudo usermod -aG kvm "$USER"
```


Log out and back in after changing group membership. If you want to refresh the current shell only, `newgrp kvm` may work, but opening a new login session is the least surprising path.
Some distributions use access control lists instead of group membership. If `setfacl` is available, you can grant your user read/write access directly:
Shell

```
sudo setfacl -m "u:$USER:rw" /dev/kvm
```


Re-run the read/write check after changing group membership or ACLs:
Shell

```
[ -r /dev/kvm ] && [ -w /dev/kvm ] && echo "OK" || echo "FAIL"
```


If your distribution uses a different group, udev rule, or enterprise policy for `/dev/kvm`, follow that local policy instead.


## [​](https://docs.microsandbox.dev/troubleshooting/linux#containers-and-vms) Containers and VMs


When running microsandbox inside another VM or container, the outer environment must expose hardware virtualization. Many hosted CI runners and cloud VMs do not expose nested virtualization by default.
For Docker-based workflows, pass `/dev/kvm` into the container. See [Run microsandbox in Docker](https://docs.microsandbox.dev/how-to/docker/docker) for the container flags and host preflight.


## [​](https://docs.microsandbox.dev/troubleshooting/linux#interrupt-acceleration) Interrupt acceleration


On Linux x86 hosts, `msb doctor` reports AMD AVIC or Intel APICv when the applicable KVM capability can be inspected:


```
KVM AVIC   enabled (x2AVIC available)
KVM APICv  enabled by KVM policy
```


Doctor reports host policy and advertised capability, not proof that one running sandbox used hardware acceleration. An outer hypervisor may hide the capability on nested or cloud VMs.
If the capability is available but disabled, doctor prints the current-boot module reload command. Stop every KVM user before unloading either module; reloading it affects every VM on the host.
## Documentation Index
## ​Install or reinstall
## ​glibc version
## ​Quick checks
## ​Missing /dev/kvm
## ​Permission denied
## ​Containers and VMs
## ​Interrupt acceleration










Current-boot KVM policy commands

AMD: Shell

```
sudo modprobe -r kvm_amd && sudo modprobe kvm_amd avic=1
cat /sys/module/kvm_amd/parameters/avic
```

Intel: Shell

```
sudo modprobe -r kvm_intel && sudo modprobe kvm_intel enable_apicv=1
cat /sys/module/kvm_intel/parameters/enable_apicv
```

Do not run either command while `/dev/kvm` has users. A distribution may build KVM into the kernel, prevent module removal, or require the setting in its boot configuration instead.
Microsandbox never changes this host-wide policy automatically. See [Performance](https://docs.microsandbox.dev/sandboxes/optimization#host) for when interrupt acceleration matters.

Was this page helpful?

Yes No ⌘ I

---

# macOS - microsandbox

`https://docs.microsandbox.dev/troubleshooting/macos`

microsandbox local sandboxes on macOS require Apple Silicon. Intel Macs are not supported for the local runtime.


## [​](https://docs.microsandbox.dev/troubleshooting/macos#install-or-reinstall) Install or reinstall


Run the installer, then open a new terminal if it updates your `PATH`:
Shell

```
curl -fsSL https://install.microsandbox.dev | sh
```


## [​](https://docs.microsandbox.dev/troubleshooting/macos#quick-checks) Quick checks


Start with the doctor command for the local setup checks:
Shell

```
msb doctor
```


Confirm that the host is Apple Silicon:
Shell

```
uname -m
```


The expected result is `arm64`. If the result is `x86_64`, the machine is an Intel Mac or the command is running under an x86_64 environment. microsandbox needs Apple Silicon; Rosetta does not make an Intel Mac supported for local sandboxes.


## [​](https://docs.microsandbox.dev/troubleshooting/macos#hardware-virtualization) Hardware virtualization


Unlike Linux and Windows, macOS does not require enabling a separate KVM or Windows Hypervisor Platform feature. Apple Silicon Macs include the hypervisor support that microsandbox uses.
If sandbox startup fails on an Apple Silicon Mac, first run `msb doctor`, then try a fresh terminal session so your current `PATH` is visible.


## [​](https://docs.microsandbox.dev/troubleshooting/macos#runtime-path) Runtime path


The default runtime root is `~/.microsandbox`. The CLI binary lives under `bin/msb`, and the runtime library lives under `lib/libkrunfw.dylib`.
If macOS is finding a stale binary, check the command path:
## Documentation Index
## ​Install or reinstall
## ​Quick checks
## ​Hardware virtualization
## ​Runtime path





Shell

```
which msb
```


Was this page helpful?

Yes No ⌘ I

---

# Microsandbox SDKs for TypeScript, Rust, Python, Go, and Ruby

`https://docs.microsandbox.dev/sdk/overview`

# Overview
## Documentation Index
## ​Installation
## ​Small example
## ​Reference





Install a microsandbox SDK, create your first microVM sandbox, and find API references for TypeScript, Rust, Python, Go, and Ruby.

The SDK runs microsandbox directly from your application. Running locally, creating a sandbox spawns a VM as a child process; there is no daemon to install and no server to connect to. With an API key set, the same SDK runs sandboxes on [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview) instead.


## [​](https://docs.microsandbox.dev/sdk/overview#installation) Installation


TypeScript Rust Python Go Ruby

```
npm install microsandbox
```


```
cargo add microsandbox
```


```
pip install microsandbox
```


```
go get github.com/superradcompany/microsandbox/sdk/go
```


```
gem install microsandbox
```


Provisioning the runtime separately

All five SDKs can use a separately provisioned runtime. See [Runtime setup](https://docs.microsandbox.dev/sdk/setup#bring-your-own-runtime) for code tabs covering each SDK’s packaging and setup requirements.


## [​](https://docs.microsandbox.dev/sdk/overview#small-example) Small example


Create a sandbox from a container image, run a command, print the output, and stop it.
TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("hello")
    .image("python")
    .create();

const output = await sb.exec("python", ["-c", "print('Hello, World!')"]);
console.log("Output:", output.stdout());
```


```
use std::error::Error;

use microsandbox::Sandbox;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let sb = Sandbox::builder("hello")
        .image("python")
        .create()
        .await?;

    let output = sb.exec("python", ["-c", "print('Hello, World!')"]).await?;
    println!("{}", output.stdout()?);

    sb.stop().await?;
    Ok(())
}
```


```
import asyncio
from microsandbox import Sandbox

async def main():
    sb = await Sandbox.create(
        "hello",
        image="python",
    )

    output = await sb.exec("python", ["-c", "print('Hello, World!')"])
    print("Output:", output.stdout_text)

    await sb.stop()

asyncio.run(main())
```


```
package main

import (
    "context"
    "fmt"
    "log"

    m "github.com/superradcompany/microsandbox/sdk/go"
)

func main() {
    ctx := context.Background()

    if _, err := m.EnsureRuntime(ctx, m.RuntimeConfig{}, m.InstallOptions{}); err != nil {
        log.Fatal(err)
    }

    sb, err := m.CreateSandbox(ctx, "hello", m.WithImage("python"))
    if err != nil {
        log.Fatal(err)
    }
    defer func() {
        _ = sb.Stop(context.Background())
        _ = sb.Close()
    }()

    out, err := sb.Exec(ctx, "python", []string{"-c", "print('Hello, World!')"})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Output:", out.Stdout())
}
```


```
require "microsandbox"

Microsandbox.install unless Microsandbox.installed?

Microsandbox::Sandbox.with("hello", image: "python") do |sandbox|
  output = sandbox.exec("python", ["-c", "print('Hello, World!')"])
  puts "Output: #{output.stdout}"
end
```


## [​](https://docs.microsandbox.dev/sdk/overview#reference) Reference


Choose the SDK for your language:


- [TypeScript SDK](https://docs.microsandbox.dev/sdk/typescript/sandbox)
- [Rust SDK](https://docs.microsandbox.dev/sdk/rust/sandbox)
- [Python SDK](https://docs.microsandbox.dev/sdk/python/sandbox)
- [Go SDK](https://docs.microsandbox.dev/sdk/go/sandbox)
- [Ruby SDK](https://docs.microsandbox.dev/sdk/ruby/sandbox)


For low-level protocol integrations, see the Agent Client references for [TypeScript](https://docs.microsandbox.dev/sdk/typescript/agent-client), [Rust](https://docs.microsandbox.dev/sdk/rust/agent-client), [Python](https://docs.microsandbox.dev/sdk/python/agent-client), and [Go](https://docs.microsandbox.dev/sdk/go/agent-client). See also [error handling](https://docs.microsandbox.dev/sdk/errors).

Was this page helpful?

Yes No ⌘ I

---

# Cloud - microsandbox

`https://docs.microsandbox.dev/cloud/overview`

microsandbox cloud is in **private beta**, and currently requires you to explicitly [request access](https://dashboard.microsandbox.dev/signup). If you already have access, you can get your API key from the [dashboard](https://dashboard.microsandbox.dev/access/api-keys).
microsandbox cloud runs your sandboxes on hosted infrastructure. The SDKs and the `msb` CLI are the same ones you use locally: the same builders, the same commands, the same code. Select the cloud backend and provide an API key; there is no daemon or separate client.


## [​](https://docs.microsandbox.dev/cloud/overview#connect) Connect


Shell

```
export MSB_BACKEND=cloud
export MSB_API_KEY="msb_..."
msb context
```


`msb context` confirms that subsequent commands will run on cloud and shows what selected it without exposing the API key. For profiles, SDK selection, and precedence, see [Local or cloud](https://docs.microsandbox.dev/operations/backends).


## [​](https://docs.microsandbox.dev/cloud/overview#sandbox-identity) Sandbox identity


Looking up a sandbox by name selects the sandbox currently using that name.
The returned object retains that sandbox’s ID for lifecycle operations, commands,
and file access. If the sandbox is deleted and its name reused, operations on
an old object fail instead of reaching the replacement. Fetch the sandbox by
name again to select the replacement; you do not need to manage IDs yourself.


## [​](https://docs.microsandbox.dev/cloud/overview#same-code-different-backend) Same code, different backend


Everything from the [quickstart](https://docs.microsandbox.dev/getting-started/quickstart) works unchanged. With cloud selected and the API key exported, this creates a sandbox on cloud instead of your machine:
TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("hello")
    .image("python")
    .memory(512)
    .create();

const output = await sb.exec("python", ["-c", "print('Hello from the cloud!')"]);
console.log(output.stdout());
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("hello")
    .image("python")
    .memory(512)
    .create()
    .await?;

let output = sb.exec("python", ["-c", "print('Hello from the cloud!')"]).await?;
println!("{}", output.stdout()?);

sb.stop().await?;
```


```
from microsandbox import Sandbox

sb = await Sandbox.create("hello", image="python", memory=512)

output = await sb.exec("python", ["-c", "print('Hello from the cloud!')"])
print(output.stdout_text)

await sb.stop()
```


```
sb, err := m.CreateSandbox(ctx, "hello",
    m.WithImage("python"),
    m.WithMemory(512),
)
if err != nil {
    return err
}
defer sb.Stop(ctx)

output, err := sb.Exec(ctx, "python", []string{"-c", "print('Hello from the cloud!')"})
fmt.Println(output.Stdout())
```


```
require "microsandbox"

Microsandbox::Sandbox.with("hello", image: "python", memory: 512) do |sb|
  output = sb.exec("python", ["-c", "print('Hello from the cloud!')"])
  puts output.stdout
end
```


```
msb run python -- python3 -c "print('Hello from the cloud!')"
```


Hardware virtualization support on your machine is not needed for cloud sandboxes; `msb doctor` checks apply to the local runtime only.


## [​](https://docs.microsandbox.dev/cloud/overview#what-works-on-cloud) What works on cloud


## Sandbox lifecycle

Create, inspect, list, reconnect, start, stop, and remove sandboxes.

## Commands and files

Run buffered, streaming, and interactive commands, then move files in or out.

## Persistent storage

Create managed volumes and access their files without starting a sandbox.

## Network controls

Apply egress policy and hostname-scoped secrets from the same SDK surface.


## [​](https://docs.microsandbox.dev/cloud/overview#compatibility) Compatibility


The everyday workflow is shared across local and cloud: sandbox lifecycle, command execution, common guest-filesystem operations, network policy, secrets, SSH sessions, and managed storage. The differences below are the ones to plan for.
Across the docs, no badge means a feature works everywhere. Exceptions use only three badges: **Local-only**, **Limited on cloud**, and **Cloud-only**.


| Area | Cloud status | Difference or alternative |
| --- | --- | --- |
| Sandbox lifecycle and execution | **Works everywhere** | Create, start, inspect, list, stop, remove, exec, shell, streaming, and interactive PTY workflows use the same SDK and CLI surface. |
| Guest filesystem | **Limited on cloud** | Common path operations and host-to-guest copies work. Low-level open-handle operations are local-only. |
| Managed volumes | **Limited on cloud** | Default and named directory volumes support lifecycle and filesystem access. Create a named volume before mounting it; disk-kind volumes and create-on-mount are local-only. |
| Volume and host paths | **Limited on cloud** | Bind and disk-image source paths resolve against the organization’s host volume, not the machine running the client. |
| Network policy and secrets | **Works everywhere** | Egress policies and hostname-scoped secret substitution carry across backends. |
| Custom networking | **Local-only** | Published ports, custom nameservers, interface overrides, rate limiters, TLS interception, and host-CA trust are not accepted by cloud create. |
| Logs | **Limited on cloud** | SDK live-follow and `msb logs -f` work. Bounded or historical reads are local-only; persist followed output externally when retention matters. |
| SSH | **Limited on cloud** | Native SDK sessions and `msb ssh` work. `msb ssh serve` is local-only; reusable SDK servers require explicit key material. |
| Images | **Limited on cloud** | OCI image references and registry credentials work. Local cache commands, host-directory or disk-image roots, plain-HTTP registries, and custom registry CAs are local-only. |
| Reconfiguration | **Local-only** | Recreate the sandbox with the new CPU, memory, mounts, or other settings instead of using `modify`. |
| Snapshots | **Limited on cloud** | Capture disk snapshots from stopped persistent sandboxes and restore them into new sandboxes. Live capture, full checkpoints, forking, groups, and local artifact archives remain local-only. |
| Resource metrics | **Local-only** | Instrument the workload with an external monitoring system. |
| Process controls | **Limited on cloud** | Graceful stop plus maximum-duration and idle-timeout policies work. Force kill, drain, ping, and touch are local-only. |


## [​](https://docs.microsandbox.dev/cloud/overview#rest-api) REST API


The same key also authenticates the [REST API](https://docs.microsandbox.dev/api-reference/overview) directly, so you can manage sandboxes, volumes, and usage over plain HTTPS without an SDK. Command execution, file transfer, and SSH ride the sandbox command channel, which the SDKs and CLI handle for you.


## [​](https://docs.microsandbox.dev/cloud/overview#what-to-know) What to know


- **Local or cloud.** Cloud is explicit: set `MSB_BACKEND=cloud`, select a cloud profile, or choose it in code. See [Local or cloud](https://docs.microsandbox.dev/operations/backends).
- **Networking.** Cloud sandboxes get a platform-assigned hostname. SSH works through the same `msb ssh` and SDK SSH clients you use locally.
- **Images.** Specify an OCI image when you create the sandbox; the cloud pulls it for you.
- **Managed settings.** [Device policy](https://docs.microsandbox.dev/enterprise/managed-configuration) applies to create requests and CLI/SDK SSH sessions. Unsupported create settings fail before the request is sent. Existing cloud sandboxes and the hosted SSH gateway keep their settings.
- **Keys and billing.** API keys, usage, and invoices live in the [dashboard](https://dashboard.microsandbox.dev).


## [​](https://docs.microsandbox.dev/cloud/overview#next-steps) Next steps


## API reference

The REST API behind the SDKs, authenticated with your API key.

## Local or cloud

Force local, select in code, or switch with profiles.

## Quickstart

New to microsandbox? Start here; everything carries over.
## Documentation Index
## ​Connect
## ​Sandbox identity
## ​Same code, different backend
## ​What works on cloud
## ​Compatibility
## ​REST API
## ​What to know
## ​Next steps










Was this page helpful?

Yes No ⌘ I

---

# Microsandbox SDK runtime setup

`https://docs.microsandbox.dev/sdk/setup`

# Runtime setup
## Documentation Index
## ​Set up the runtime
## ​How runtime selection works
## ​Advanced setup
## ​Troubleshooting
## ​API reference







Prepare a local runtime before creating your first sandbox.

Local sandboxes need `msb` and `libkrunfw`. Call the setup helper once at application startup: it reuses an existing runtime or installs one when missing. Sandbox creation does not download it automatically. Cloud sandboxes do not need a local runtime.


## [​](https://docs.microsandbox.dev/sdk/setup#set-up-the-runtime) Set up the runtime


TypeScript Rust Python Go Ruby

```
import { ensureRuntime } from "microsandbox";

const runtime = await ensureRuntime();
console.log(runtime.msbPath, runtime.libkrunfwPath);
```


```
use microsandbox::{config::GlobalConfig, setup::{InstallOptions, ensure_runtime}};

let runtime = ensure_runtime(&GlobalConfig::default(), InstallOptions::default()).await?;
```


```
from microsandbox import ensure_runtime

runtime = await ensure_runtime()
print(runtime.msb_path, runtime.libkrunfw_path)
```


```
import (
    "fmt"
    m "github.com/superradcompany/microsandbox/sdk/go"
)

runtime, err := m.EnsureRuntime(ctx, m.RuntimeConfig{}, m.InstallOptions{})
if err != nil {
    return err
}
fmt.Println(runtime.MSBPath, runtime.LibkrunfwPath)
```


```
require "microsandbox"

Microsandbox.install unless Microsandbox.installed?
```


The default installation directory is `~/.microsandbox` (`%USERPROFILE%\.microsandbox` on Windows). Keep `msb` and `libkrunfw` from the same runtime bundle.


### [​](https://docs.microsandbox.dev/sdk/setup#resolve-check-install-and-ensure) Choose a setup operation


Use ensure for normal startup. The calls below are alternatives; choose the one your application needs.
TypeScript Rust Python Go Ruby

```
import * as msb from "microsandbox";

await msb.ensureRuntime();  // Reuse or install if missing.
msb.resolveRuntime();       // Require an existing runtime; never install.
msb.isRuntimeInstalled();   // Check availability; returns a boolean.
await msb.installRuntime(); // Install from the selected source.
```


```
use microsandbox::{config::GlobalConfig, setup};

let config = GlobalConfig::default();

// Reuse or install if missing.
setup::ensure_runtime(&config, Default::default()).await?;
// Require an existing runtime; never install.
setup::resolve_runtime(&config)?;
// Check availability; returns a boolean.
setup::is_runtime_installed(&config);
// Install from the selected source.
setup::install_runtime(&config, Default::default()).await?;
```


```
import microsandbox as msb

await msb.ensure_runtime()  # Reuse or install if missing.
msb.resolve_runtime()       # Require an existing runtime; never install.
msb.is_runtime_installed()  # Check availability; returns a boolean.
await msb.install_runtime() # Install from the selected source.
```


```
import m "github.com/superradcompany/microsandbox/sdk/go"

config := m.RuntimeConfig{}
options := m.InstallOptions{}

// Reuse or install if missing. Returns (ResolvedRuntime, error).
m.EnsureRuntime(ctx, config, options)
// Require an existing runtime. Returns (ResolvedRuntime, error).
m.ResolveRuntime(config)
// Check availability; returns bool.
m.IsRuntimeInstalled(config)
// Install from the selected source. Returns (ResolvedRuntime, error).
m.InstallRuntime(ctx, config, options)
```


```
require "microsandbox"

Microsandbox.installed? # Check availability; returns a boolean.
Microsandbox.install   # Install using the default source and options.

# Reuse or install if missing:
Microsandbox.install unless Microsandbox.installed?
# Ruby does not expose resolve or per-call installation options.
```


Ensure does not repair incomplete installations or ignore invalid explicit paths.


## [​](https://docs.microsandbox.dev/sdk/setup#choose-a-runtime) How runtime selection works


The SDK checks these locations in order:
It first checks **explicit paths**: environment variables, process-level setters, then configured paths. Next it checks the **runtime home**: configured `home`, then `MSB_HOME`, then `~/.microsandbox`. Finally it checks the **SDK package** for bundled binaries, when available.


Path resolution, backend lifetime, and runtime versions

A local backend captures its effective home, relative directory overrides, configured runtime paths, and registry CA certificate path when it is constructed. Later changes to the working directory or `MSB_HOME` do not move that backend’s files. Construct a new backend to select another home. Relative host paths in global `config.json` and managed configuration resolve against the contributing file’s directory. Programmatic paths and environment defaults use the caller’s working directory. Process-level SDK runtime setters capture relative paths when registered; environment runtime overrides are captured during backend construction, below managed policy. Existing saved sandbox records retain their legacy relative-path interpretation without rewriting. A complete home installation wins over bundled Python and Node runtimes, even if its version differs from the SDK. Updating an SDK does not replace that installation. Go also reuses a complete home installation. [Managed runtime paths](https://docs.microsandbox.dev/enterprise/deploy-and-verify#apply-configuration-updates) override user choices.
To use a custom installation, set both `MSB_PATH` and `MSB_LIBKRUNFW_PATH` before constructing a backend. See [path overrides](https://docs.microsandbox.dev/sdk/setup#override-runtime-paths) for SDK setters and precedence details.


## [​](https://docs.microsandbox.dev/sdk/setup#advanced-setup) Advanced setup


### [​](https://docs.microsandbox.dev/sdk/setup#bring-your-own-runtime) Bring your own runtime


Use an existing `msb` executable and its matching `libkrunfw` library instead of downloading a runtime at application startup. Install the pair with the [CLI installer](https://docs.microsandbox.dev/getting-started/quickstart), or provision it yourself.
Set both paths before starting your application. Replace these example paths with your installation:
Linux macOS Windows

```
export MSB_PATH="/opt/microsandbox/bin/msb"
export MSB_LIBKRUNFW_PATH="/opt/microsandbox/lib/libkrunfw.so.5"
```


```
export MSB_PATH="/opt/microsandbox/bin/msb"
export MSB_LIBKRUNFW_PATH="/opt/microsandbox/lib/libkrunfw.dylib"
```


```
$env:MSB_PATH = "C:\microsandbox\bin\msb.exe"
$env:MSB_LIBKRUNFW_PATH = "C:\microsandbox\lib\libkrunfw.dll"
```


Use the [resolve helper](https://docs.microsandbox.dev/sdk/setup#resolve-check-install-and-ensure) to check that the pair is available without installing anything. These environment variables also select the runtime for subsequent sandbox operations; see [path overrides](https://docs.microsandbox.dev/sdk/setup#override-runtime-paths) for precedence.


SDK packaging and build options

All SDKs can use the runtime paths above. You still need to install the SDK itself, including its native bindings. The packaging details differ: TypeScript Rust Python Go Ruby

```
# Keep optional dependencies: the platform package contains both the
# bundled runtime and the required native addon.
# --omit=optional removes that addon too.
npm install microsandbox
```


```
# Embedding is opt-in. Disable the default Cargo-time runtime download:
cargo add microsandbox --no-default-features --features local,net

# These features still allow explicit setup::ensure_runtime() calls.
```


```
# Wheels include the native extension and a bundled runtime.
# The runtime paths above override the bundled runtime.
python -m pip install --only-binary=:all: microsandbox
```


```
# The module embeds its native FFI library and extracts it on first use.
# Your msb and libkrunfw pair is separate from that library.
go get github.com/superradcompany/microsandbox/sdk/go
```


```
# The gem needs its native extension even with an existing runtime.
# Installing a source gem requires a Rust toolchain (1.85+).
gem install microsandbox
```


### [​](https://docs.microsandbox.dev/sdk/setup#use-a-custom-kernel) Use a custom kernel


If your workload needs additional Linux kernel features, build a custom `libkrunfw`, the library that bundles the guest kernel. This applies to local sandboxes; it does not change the managed cloud kernel.
Start from the `vendor/libkrunfw` revision pinned by your microsandbox release in our [libkrunfw fork](https://github.com/superradcompany/libkrunfw). It includes the kernel patches microsandbox relies on; an upstream build may not be compatible.


1. Enable the required kernel options or apply your patches, then follow the [build instructions](https://github.com/superradcompany/libkrunfw#building) for your platform and architecture.
2. Select the compatible `msb` executable and your rebuilt library before starting your application.


For example, on Linux, replace these paths with your executable and custom library:
Linux

```
export MSB_PATH="/opt/microsandbox/bin/msb"
export MSB_LIBKRUNFW_PATH="/opt/custom-kernel/libkrunfw.so.5"
```


You can also use the [SDK path setters](https://docs.microsandbox.dev/sdk/setup#override-runtime-paths) before constructing a backend.
Boot a fresh guest to use the new kernel. Running guests and full snapshots retain their existing kernel.


### [​](https://docs.microsandbox.dev/sdk/setup#offline-installation) Offline installation


Use a directory or archive source to install a pre-downloaded release bundle. To require an installation that already exists, call the resolve helper instead of ensure. See [installation examples and options](https://docs.microsandbox.dev/sdk/setup#customize-installation) and [offline deployment](https://docs.microsandbox.dev/enterprise/prepare-environment#prepare-offline-devices).


### [​](https://docs.microsandbox.dev/sdk/setup#embedded-runtime) Embedded runtime


If your SDK build includes an embedded runtime archive, you can install from it without downloading. Select the `embedded_archive` source in the [installation options](https://docs.microsandbox.dev/sdk/setup#customize-installation).
Ensure reuses an existing runtime before extracting the archive. Resolve only finds an existing installation; it does not extract one.


## [​](https://docs.microsandbox.dev/sdk/setup#troubleshooting) Troubleshooting


| Problem | What to do |
| --- | --- |
| Incomplete installation | Restore a matching executable and library. Setup does not repair a partial pair or fall back to bundled binaries. |
| Invalid explicit path | Correct the override. Invalid paths do not fall through to another installation. |
| Unexpected runtime version | Check explicit paths and the runtime home; both take precedence over bundled binaries. |
| Feature unsupported by an older runtime | Upgrade the selected runtime. Updating the SDK alone may leave it unchanged. |
| Embedded archive unavailable | Use a native SDK built with embedding, or choose a directory, archive, or download source. |


For existing installations, see the [v0.7 migration guide](https://docs.microsandbox.dev/migrations/v0.7) before upgrading a shared database. Helper details are available below.


## [​](https://docs.microsandbox.dev/sdk/setup#api-reference) API reference


Customize installation

Python, TypeScript, and Go accept a `RuntimeConfig` and `InstallOptions`. Their per-call home and binary-path overrides are layered on persisted global configuration. Rust accepts `GlobalConfig` and `InstallOptions` directly. Environment binary-path overrides retain the highest priority. Use the directory source to provision a runtime from a flat release-bundle directory containing `msb` and `libkrunfw` side by side, without downloading: TypeScript Rust Python Go

```
import { installRuntime } from "microsandbox";

const runtime = await installRuntime(
  { home: "/opt/microsandbox" },
  { source: "directory", sourcePath: "/opt/runtime-bundle" },
);
```


```
use microsandbox::{
    config::GlobalConfig,
    setup::{InstallOptions, InstallSource, install_runtime},
};

let config = GlobalConfig { home: Some("/opt/microsandbox".into()), ..Default::default() };
let runtime = install_runtime(&config, InstallOptions {
    source: InstallSource::Directory("/opt/runtime-bundle".into()),
    ..Default::default()
}).await?;
```


```
from microsandbox import InstallOptions, RuntimeConfig, install_runtime

runtime = await install_runtime(
    RuntimeConfig(home="/opt/microsandbox"),
    InstallOptions(source="directory", source_path="/opt/runtime-bundle"),
)
```


```
runtime, err := m.InstallRuntime(ctx,
    m.RuntimeConfig{Home: "/opt/microsandbox"},
    m.InstallOptions{Source: m.InstallSourceDirectory, SourcePath: "/opt/runtime-bundle"},
)
if err != nil {
    return err
}
```


| Option | Behavior |
| --- | --- |
| Home and binary paths | Select the runtime home or explicit pair for this call. |
| Source | `release_download` (default), `directory`, `archive`, or `embedded_archive`; directory and archive require a source path. |
| Version | Select the release to download; defaults to the SDK’s pinned release. |
| Force | Replace a complete installation; never repair a partial pair. |
| Verify | Verify the installed pair; defaults to true. Go uses `*bool` so its zero value preserves this default. |
| Expected archive SHA-256 | Validate downloaded, local, or embedded archive bytes before publishing files. |

An embedded source requires a native SDK built with an embedded runtime archive. If unavailable, explicit installation errors. Ensure still reuses an existing pair before acquisition, even when an embedded source is requested. To require a pre-provisioned runtime, call resolve directly. Each call uses its own configuration; Go no longer caches a process-wide successful setup result.

Override runtime paths

Use process-wide SDK setters where available, or the environment variables below. Go uses environment variables for process-wide overrides and `RuntimeConfig` for individual setup calls. Call setters before creating a local sandbox. Automatic package discovery is a fallback and does not occupy the explicit setter slot. A public libkrunfw setter overrides the library for the selected executable, whether that executable comes from configured paths, home, or a package. TypeScript Rust Python Go Ruby

```
import { setRuntimeLibkrunfwPath } from "microsandbox";

setRuntimeLibkrunfwPath("/opt/microsandbox/lib/libkrunfw.dylib");
```


```
use microsandbox::config::{set_sdk_libkrunfw_path, set_sdk_msb_path};

// Process-wide configuration, not a SandboxBuilder method.
// Set both paths before constructing the backend.
set_sdk_msb_path("/opt/microsandbox/bin/msb");
set_sdk_libkrunfw_path("/opt/microsandbox/lib/libkrunfw.dylib");
```


```
from microsandbox import set_libkrunfw_path

set_libkrunfw_path("/opt/microsandbox/lib/libkrunfw.dylib")
```


```
// These overrides apply to this setup call.
// Use MSB_PATH and MSB_LIBKRUNFW_PATH for subsequent sandbox operations.
runtime, err := m.ResolveRuntime(m.RuntimeConfig{
    MSBPath: "/opt/microsandbox/bin/msb",
    LibkrunfwPath: "/opt/microsandbox/lib/libkrunfw.dylib",
})
if err != nil {
    return err
}
```


```
require "microsandbox"

Microsandbox.set_runtime_libkrunfw_path("/opt/microsandbox/lib/libkrunfw.dylib")
```

Set runtime paths before constructing a backend. Each backend captures these settings; create a new backend to pick up changes. Environment variables work across the SDKs and take precedence over SDK-provided or user-configured paths. [Managed runtime paths](https://docs.microsandbox.dev/enterprise/deploy-and-verify#apply-configuration-updates) take precedence over all three:

| Variable | Purpose |
| --- | --- |
| `MSB_PATH` | Override the `msb` executable used by local SDK operations. |
| `MSB_LIBKRUNFW_PATH` | Override the `libkrunfw` shared library loaded by the process. |
| `MSB_AGENTD_PATH` | Override the Agentd guest executable read by `msb` before VM startup. |

Set these process-wide overrides before creating any local sandbox. Prefer setting `MSB_PATH` and `MSB_LIBKRUNFW_PATH` together to select a matching pair. `MSB_PATH` alone may resolve a library adjacent to that executable; `MSB_LIBKRUNFW_PATH` alone is incomplete and fails closed. An incomplete explicit pair is not repaired by falling back to another installation. `MSB_AGENTD_PATH` takes precedence over global `paths.agentd`; the selected file is read eagerly and must name a compatible Linux ELF executable. These variables do not belong to an individual sandbox configuration.

Read a runtime version

TypeScript and Rust can read the Cargo package version embedded in an `msb` executable without running it. This is an optional inspection of the specified file; firmware and a complete runtime installation are not required. TypeScript Rust

```
import { resolveRuntimeVersion } from "microsandbox";

const version = await resolveRuntimeVersion("/path/to/msb");
```


```
use microsandbox::setup::resolve_runtime_version;

let version = resolve_runtime_version("/path/to/msb")?;
```

Rust returns `Option<setup::Version>` and TypeScript returns `string | null`. Older executables without the version section produce `None` or `null`. Invalid executable metadata, malformed version sections and file access failures are errors. The reader supports ELF, PE and thin or universal Mach-O files, limits metadata reads to 4 MiB and version contents to 256 bytes, and never falls back to executing `msb --version`. Universal Mach-O slices must agree on the version, including section absence. The version identifies the build; it does not authenticate the executable or guarantee feature compatibility. Sandbox startup separately resolves a tested launch contract for the selected runtime. When embedded version metadata is absent, startup may run a bounded `msb --version` probe and cache the result for that native executable’s identity within the SDK process. Replacing the executable invalidates that cache. This startup behavior does not change the read-only version inspection methods above.

Inspect Go versions

Go setup helpers may load the SDK’s embedded FFI library on first use; resolve does not install host runtime binaries. Go also exposes the SDK’s pinned release version and the version reported by the loaded FFI library: Go

```
sdkVersion := m.SDKVersion()

runtimeVersion, err := m.RuntimeVersion()
if err != nil {
    return err
}
```

`SDKVersion() string` does not load the FFI library. `RuntimeVersion() (string, error)` loads it automatically on first use and returns an error if loading fails.

Compatibility: setup APIs before v0.7

These APIs were replaced in v0.7.0. Use this mapping when upgrading from v0.6; new applications should use the current helpers above.

| SDK | Replace | With |
| --- | --- | --- |
| TypeScript | `install` | `installRuntime` |
| TypeScript | `isInstalled` | `isRuntimeInstalled` |
| Python | `install` | `install_runtime` |
| Python | `is_installed` | `is_runtime_installed` |
| Go | `EnsureInstalled` | `EnsureRuntime` |
| Go | `IsInstalled` | `IsRuntimeInstalled` |


- **TypeScript:** replace the `setup` / `Setup` builder with runtime helpers accepting `RuntimeConfig` and `InstallOptions`.
- **Go:** replace `SetupOption` with `RuntimeConfig` and `InstallOptions`. Replace `WithSkipDownload` with `ResolveRuntime` when installation must be avoided.

Install and ensure now return the selected runtime paths. Rust’s four helper names and Ruby’s setup API are unchanged. See [setup operations](https://docs.microsandbox.dev/sdk/setup#resolve-check-install-and-ensure).

Was this page helpful?

Yes No ⌘ I

---

# Run microsandbox in Docker - microsandbox

`https://docs.microsandbox.dev/how-to/docker/docker`

Local-only
This guide runs the `msb` CLI inside Docker and starts an Alpine microVM from the container. It works in any Docker environment that can pass a usable `/dev/kvm` device into the container.


## [​](https://docs.microsandbox.dev/how-to/docker/docker#run-microsandbox-in-docker) Run microsandbox in Docker
## Documentation Index
## ​Run microsandbox in Docker
## ​Troubleshooting
## ​Image tags






1

Check Docker support

Pull the image, then run `msb doctor` inside it before starting a sandbox: Shell

```
docker pull ghcr.io/superradcompany/microsandbox:latest
```

Run the preflight inside the container: macOS & Linux Windows

```
docker run --rm --device /dev/kvm \
  ghcr.io/superradcompany/microsandbox:latest \
  doctor
```


```
docker run --rm --device /dev/kvm `
  ghcr.io/superradcompany/microsandbox:latest `
  doctor
```

A compatible Docker environment reports both checks as successful:

```
✓ KVM device   /dev/kvm
✓ KVM access   read/write
```

If both checks pass, continue with the example. If either fails, the Docker environment does not currently expose the virtualization support microsandbox needs. `/dev/kvm` is the authoritative compatibility check: Docker Engine can pass it through directly, while Docker Desktop depends on whether its Linux VM makes nested virtualization available. If Docker rejects the device mapping or `msb doctor` reports that `/dev/kvm` is missing, consult the relevant setup guide:

- **Linux Docker Engine:** Follow the [`/dev/kvm` setup and permission checks](https://docs.microsandbox.dev/troubleshooting/linux#missing-/dev/kvm).
- **Docker Desktop:** Review the [Mac virtual machine manager](https://docs.docker.com/desktop/features/vmm/) or [Windows backend](https://docs.docker.com/desktop/setup/install/windows-install/) documentation. Hardware virtualization on the physical machine does not by itself make `/dev/kvm` available to containers.
- **Docker Desktop inside another VM or VDI:** Follow Docker’s [nested-virtualization guide](https://docs.docker.com/desktop/setup/vm-vdi/).

After changing the Docker or hypervisor configuration, rerun the preflight. Adding `--privileged` cannot create a KVM device that the Docker environment does not have. 2

Open an interactive sandbox

Run Alpine and attach your terminal to its shell: macOS & Linux Windows

```
docker run --rm -it \
  --device /dev/kvm \
  ghcr.io/superradcompany/microsandbox:latest \
  run alpine --name my-sandbox --replace
```


```
docker run --rm -it `
  --device /dev/kvm `
  ghcr.io/superradcompany/microsandbox:latest `
  run alpine --name my-sandbox --replace
```


- `--rm` removes the outer container when it exits.
- `-it` carries your terminal through Docker and `msb` to the sandbox. Without it, the sandbox can be running with no usable prompt.
- `--device /dev/kvm` grants the specific hardware interface microsandbox needs. The container does not require Docker’s blanket `--privileged` mode.

At the Alpine prompt, verify the guest and exit: Shell

```
uname -a
exit
```

3

Run one command

For automation, pass a command instead of allocating a terminal: macOS & Linux Windows

```
docker run --rm --device /dev/kvm \
  ghcr.io/superradcompany/microsandbox:latest \
  run alpine --name my-sandbox --replace -- \
  echo "hello from a microVM"
```


```
docker run --rm --device /dev/kvm `
  ghcr.io/superradcompany/microsandbox:latest `
  run alpine --name my-sandbox --replace -- `
  echo "hello from a microVM"
```

The command’s output and exit code pass through both layers to the host. 4

Persist images and sandboxes

Without a volume, the outer container owns the microsandbox image cache and database. `--rm` deletes them with the container, so the next run downloads Alpine again. Mount a Docker volume when repeated runs should reuse that state: Shell

```
docker volume create microsandbox-data
```

Mount it at microsandbox’s data directory: macOS & Linux Windows

```
docker run --rm -it \
  --device /dev/kvm \
  --volume microsandbox-data:/root/.microsandbox \
  ghcr.io/superradcompany/microsandbox:latest \
  run alpine --name my-sandbox --replace
```


```
docker run --rm -it `
  --device /dev/kvm `
  --volume microsandbox-data:/root/.microsandbox `
  ghcr.io/superradcompany/microsandbox:latest `
  run alpine --name my-sandbox --replace
```

The Docker volume preserves pulled images, stopped sandboxes, snapshots, and the microsandbox database. Remove it only when that state is no longer needed: Shell

```
docker volume rm microsandbox-data
```


## [​](https://docs.microsandbox.dev/how-to/docker/docker#troubleshooting) Troubleshooting


The process exits with SIGABRT before the agent starts

Run the `msb doctor` preflight above. An early abort while entering the VM commonly means the outer Linux environment did not provide usable KVM access.

The command keeps running but shows no prompt

Check that the Docker command includes `-it`. From another terminal, `docker ps` may show that the outer container is running even though its standard input and terminal were not attached.

The guest image downloads on every run

Mount `microsandbox-data` at `/root/.microsandbox`. An ephemeral outer container otherwise starts with an empty microsandbox cache.


## [​](https://docs.microsandbox.dev/how-to/docker/docker#image-tags) Image tags


| Tag | Description |
| --- | --- |
| `latest` | Latest microsandbox release. |
| `x.y.z` | Exact release version. |
| `x.y` | Latest patch release in a minor series. |


Was this page helpful?

Yes No ⌘ I

---

# Performance - microsandbox

`https://docs.microsandbox.dev/sandboxes/optimization`

# Performance
## Documentation Index
## ​Baseline
## ​Storage
## ​CPU
## ​Memory
## ​Writeback
## ​Host
## ​Measure









Choose the settings that can improve local sandbox performance

Local-only
There is no single fastest setup. Start with the defaults, measure your
workload, and change one setting at a time.
The CLI and SDKs can tune individual sandboxes. Use the
[global config](https://docs.microsandbox.dev/configuration) to set host-wide defaults. Sandbox YAML does
not currently expose these local performance controls.
The SDK examples use TypeScript, Rust, Python, and Go. Ruby does not expose flat-root selection, placement policies, or huge-page controls.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#baseline) Baseline


Check the host and the sandbox before tuning:
Shell

```
msb doctor
msb inspect my-sandbox
```


`msb doctor` reports host capabilities, including native root-disk cloning and
interrupt acceleration. `msb inspect` shows the settings the sandbox actually
uses. Replace `my-sandbox` with the sandbox you want to tune. Decide whether
you are improving creation time, workload latency, or throughput, then record
that result at your normal concurrency.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#storage) Storage


Every OCI sandbox has a root disk. Choose its layout based on the bottleneck
you are trying to remove.
![Layered roots share OCI image layers and add a writable layer per sandbox, while flat roots clone a materialized ext4 image into a private disk per sandbox](https://mintcdn.com/superradcompanyinc/r29rG4N2-LJQIDzz/images/storage-layouts.svg?fit=max&auto=format&n=r29rG4N2-LJQIDzz&q=85&s=97b77ec3709787fb201cbbf5d8b9e850)


|  | Layered (default) | Flat |
| --- | --- | --- |
| Layout | Shared read-only image layers with a writable layer per sandbox | One ext4 disk cloned per sandbox |
| Best for | Sharing images and maximum portability | Faster creation and filesystem-heavy work |
| Disk use | Image layers are shared | Each sandbox gets a private clone |
| Patches and snapshots | Supported | Not supported |
| Host needs | None | Copy-on-write support for the fastest cloning |


Keep the layered layout unless creation time or filesystem throughput is a
measured bottleneck.
**Configure a flat root**
CLI TypeScript Rust Python Go

```
msb create python:3.12 --name worker --root-disk flat:8G,clone=auto
```


```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
  .image("python:3.12")
  .rootDisk((disk) => disk.flat().size(8192).cloneStrategy("auto"))
  .create();
```


```
use microsandbox::sandbox::FlatClone;
use microsandbox::Sandbox;

let sb = Sandbox::builder("worker")
    .image("python:3.12")
    .root_disk_with(|disk| disk.flat().size(8192).clone_strategy(FlatClone::Auto))
    .create()
    .await?;
```


```
from microsandbox import FlatClone, Image, RootDisk, Sandbox

sb = await Sandbox.create(
    "worker",
    image=Image.oci(
        "python:3.12",
        root_disk=RootDisk.flat(8192, clone=FlatClone.AUTO),
    ),
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12"),
    m.WithRootDisk(m.RootDisk.Flat(m.RootDiskFlatOptions{
        SizeMiB: 8192,
        Clone:   m.FlatCloneAuto,
    })),
)
```


To make flat roots the default for future sandboxes, set
`sandbox_defaults.oci.root_disk` in the [global config](https://docs.microsandbox.dev/configuration).
**Prepare for benchmarking**
Missing flat images are materialized automatically. To exclude that one-time
work from a creation benchmark, prepare the image first:
Shell

```
msb pull python:3.12 --materialize flat
```


### [​](https://docs.microsandbox.dev/sandboxes/optimization#clone-strategies) Clone strategies


Choose how the private flat-root disk is copied:


| Strategy | Behavior |
| --- | --- |
| `auto` | Uses a native copy-on-write clone when available, otherwise makes a sparse copy. |
| `reflink` | Requires native cloning and fails when the host cannot provide it. |
| `copy` | Always makes an independent sparse copy. |


Use `auto` unless clone support is an operational requirement.
**Verify**
Run `msb inspect worker` to see the resolved root layout and clone strategy.
See [Bootstrap](https://docs.microsandbox.dev/sandboxes/bootstrap#flat-oci-rootfs) for the flat-root API and
[OCI images](https://docs.microsandbox.dev/images/overview#oci-images) for image behavior.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#cpu) CPU


### [​](https://docs.microsandbox.dev/sandboxes/optimization#policies) Policies


Sandbox vCPU threads use the host scheduler by default. Linux and Windows can
also place those threads according to a policy.


| Policy | Behavior | Use when |
| --- | --- | --- |
| `inherit` (default) | Leaves placement to the host scheduler. | You do not need managed placement. |
| `auto` | Uses available physical cores first, then shares CPUs. | You run a dedicated sandbox host. |
| `spread` | Spreads work across physical cores. | CPU throughput matters most. |
| `compact` | Packs work onto fewer physical cores. | Cache locality or host density matters most. |


**Configure placement**
CLI TypeScript Rust Python Go

```
msb create python:3.12 --name worker --cpus 2 --cpu-placement spread
```


```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
  .image("python:3.12")
  .cpus(2)
  .cpuPlacement("spread")
  .create();
```


```
use microsandbox::sandbox::{CpuPlacement, Sandbox};

let sb = Sandbox::builder("worker")
    .image("python:3.12")
    .cpus(2)
    .cpu_placement(CpuPlacement::Spread)
    .create()
    .await?;
```


```
from microsandbox import CpuPlacement, Sandbox

sb = await Sandbox.create(
    "worker",
    image="python:3.12",
    cpus=2,
    cpu_placement=CpuPlacement.SPREAD,
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12"),
    m.WithCPUs(2),
    m.WithCPUPlacement(m.CPUPlacementSpread),
)
```


Set `sandbox_defaults.cpu_placement` in the
[global config](https://docs.microsandbox.dev/configuration) to choose a host-wide default.


### [​](https://docs.microsandbox.dev/sandboxes/optimization#numa) NUMA


On a multi-node host, a placement profile can keep a sandbox’s CPU and memory
on one NUMA node. Define the profile in the [global config](https://docs.microsandbox.dev/configuration):
JSON

```
{
  "runtime": {
    "placement_profiles": {
      "latency": {
        "numa": { "mode": "prefer_single" },
        "memory": { "mode": "follow_cpu" }
      }
    }
  }
}
```


Then select it when creating the sandbox:
CLI TypeScript Rust Python Go

```
msb create python:3.12 \
  --name worker \
  --cpus 2 \
  --cpu-placement auto \
  --placement-profile latency
```


```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
  .image("python:3.12")
  .cpus(2)
  .cpuPlacement("auto")
  .placementProfile("latency")
  .create();
```


```
use microsandbox::sandbox::{CpuPlacement, Sandbox};

let sb = Sandbox::builder("worker")
    .image("python:3.12")
    .cpus(2)
    .cpu_placement(CpuPlacement::Auto)
    .placement_profile("latency")
    .create()
    .await?;
```


```
from microsandbox import CpuPlacement, Sandbox

sb = await Sandbox.create(
    "worker",
    image="python:3.12",
    cpus=2,
    cpu_placement=CpuPlacement.AUTO,
    placement_profile="latency",
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12"),
    m.WithCPUs(2),
    m.WithCPUPlacement(m.CPUPlacementAuto),
    m.WithPlacementProfile("latency"),
)
```


Use `prefer_single` as an optimization: it falls back to normal placement when
one node cannot fit the sandbox. Use `strict_single` when the workload should
not start without single-node placement.
**Verify**
Run `msb inspect worker` to see the resolved policy, profile, and assigned host
CPUs.


### [​](https://docs.microsandbox.dev/sandboxes/optimization#caveats) Caveats


- Placement coordinates only sandboxes that share the same `MSB_HOME`.
- It considers the sandbox’s maximum CPU count, including CPUs currently offline.
- Normal policies may share logical CPUs when exclusive capacity runs out.
- Placement does not isolate host processes or reserve dedicated cores.
- macOS falls back to `inherit` because public APIs do not provide hard CPU affinity.
- Normal policies fall back to `inherit` when placement fails; `strict_single` fails the sandbox instead.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#memory) Memory


Transparent huge pages (THP) control how the guest handles large memory
mappings.


| Policy | Use when |
| --- | --- |
| `madvise` (default) | You want the safe default. |
| `always` | Benchmarks show a gain for large, sustained mappings. |
| `never` | Predictable small-page behavior matters more. |


THP changes apply on the next boot. Keep `madvise` unless workload tests show
a clear gain.
**Configure THP**
CLI TypeScript Rust Python Go

```
msb create python:3.12 --name memory-worker --thp always
```


```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("memory-worker")
  .image("python:3.12")
  .thp("always")
  .create();
```


```
use microsandbox::{sandbox::TransparentHugePagePolicy, Sandbox};

let sb = Sandbox::builder("memory-worker")
    .image("python:3.12")
    .thp(TransparentHugePagePolicy::Always)
    .create()
    .await?;
```


```
from microsandbox import Sandbox

sb = await Sandbox.create(
    "memory-worker",
    image="python:3.12",
    thp="always",
)
```


```
sb, err := m.CreateSandbox(ctx, "memory-worker",
    m.WithImage("python:3.12"),
    m.WithTHP(m.THPAlways),
)
```


Set `sandbox_defaults.thp` in the [global config](https://docs.microsandbox.dev/configuration) to choose a
host-wide default. The policy cannot change with `msb modify`; create or
replace the sandbox to select another value.
**Verify**
Run `msb inspect memory-worker` to see the resolved THP policy.
See [Bootstrap](https://docs.microsandbox.dev/sandboxes/bootstrap#transparent-huge-pages) for how THP is
applied and [Live modify](https://docs.microsandbox.dev/sandboxes/tuning) for memory sizing and resize
headroom.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#writeback) Writeback


On Linux, block writeback limits the buffered disk data that active sandboxes
can hold in host memory.


- `auto` derives safe limits from the host and is the recommended setting.
- `fixed` uses operator-defined limits. Choose it only after measuring a representative workload.
- `off` removes the limit for new sandboxes, allowing buffered guest writes to create more host-memory pressure.


**Configure writeback**
Writeback is global runtime policy, not a per-sandbox SDK option:
JSON

```
{
  "runtime": {
    "block_writeback": {
      "mode": "auto"
    }
  }
}
```


Writeback does not affect non-Linux hosts, read-only disks, or direct I/O. See
[Global config](https://docs.microsandbox.dev/configuration) for `fixed` limits and pool settings.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#host) Host


On Linux x86, AMD AVIC and Intel APICv can accelerate virtual interrupts. These
are host-wide KVM policies, not sandbox settings. `msb doctor` reports their
status without changing them.
The same command probes whether `MSB_HOME` supports native flat-root clones.
A copy fallback is correct but slower to provision.
Read [Linux troubleshooting](https://docs.microsandbox.dev/troubleshooting/linux#interrupt-acceleration)
before changing a KVM module because the change affects every VM on the host.


## [​](https://docs.microsandbox.dev/sandboxes/optimization#measure) Measure


- Cache or materialize the same image before each test unless cold-start cost is what you are measuring.
- Keep CPU, memory, storage, host power settings, and concurrency unchanged.
- Measure sandbox creation separately from the workload.
- Repeat each test and compare the median, not a single run.
- Use `msb inspect` to confirm the intended setting was applied.


Was this page helpful?

Yes No ⌘ I

---

# Deploy and verify - microsandbox

`https://docs.microsandbox.dev/enterprise/deploy-and-verify`

# Deploy and verify
## Documentation Index
## ​Choose your device manager
## ​Verify the configuration
## ​Apply configuration updates





Pilot your configuration, distribute it to employee devices, and manage updates

Roll out the runtime packages, images, and policy you prepared on one device. Verify them in an employee session before expanding to the team.
Before deployment, finish [environment preparation](https://docs.microsandbox.dev/enterprise/prepare-environment) and [define and protect the policy](https://docs.microsandbox.dev/enterprise/managed-configuration). The steps below distribute it, verify the result, and maintain it over time.


## [​](https://docs.microsandbox.dev/enterprise/deploy-and-verify#choose-your-device-manager) Choose your device manager


Use your device manager to distribute the policy to a pilot group first.


Jamf Pro

1

Build a configuration package

On a packaging Mac, place `managed.json` in `/Library/Application Support/microsandbox/`. Drag the folder into [Composer](https://learn.jamf.com/r/en-US/jamf-connect-documentation-current/Packaging_Files_and_Images_with_Composer) to create a package source. Set the owner to **root**, group to **wheel**, directory permissions to `0755`, and file permissions to `0644`. Select **Build as PKG** and sign according to your organization’s policy. 2

Upload the package

In Jamf Pro, open **Settings > Computer management > Packages > New**. [Upload the PKG](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Uploading_a_Package_to_Jamf_Pro) and make it available on your distribution point. 3

Create a deployment policy

Open **Computers > Policies > New**. In **General**, select **Recurring Check-in** and a daily execution frequency. Under **Packages**, add the PKG with the **Install** action. 4

Deploy to a pilot group

In **Scope**, select your pilot computers and save the [policy](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Deploying_a_Package_Using_a_Policy). After check-in, review its logs and [verify the effective settings](https://docs.microsandbox.dev/enterprise/deploy-and-verify#verify-the-configuration) as an employee before expanding the scope.

Intune macOS

1

Prepare the file deployment

Use Intune’s [macOS shell-script workflow](https://learn.microsoft.com/en-us/intune/device-management/tools/run-shell-scripts-macos). Your organization’s deployment script must write the JSON to the [macOS policy path](https://docs.microsandbox.dev/enterprise/managed-configuration#file-location), apply the required permissions, and safely replace an existing policy. It should succeed when the correct file is already present. 2

Add the deployment in Intune

Open **Devices > By platform > macOS > Manage devices > Scripts > Add**. Give the policy a name in **Basics**, then upload your script under **Script settings**. 3

Configure execution


| Setting | Value |
| --- | --- |
| Run script as signed-in user | **No**, so it runs as root |
| Script frequency | Daily |
| Max number of times to retry if script fails | Set a retry count |

The Intune management agent must be installed. Microsoft’s script prerequisites require direct Internet access; proxy connections are unsupported for this delivery path. 4

Assign and verify

Under **Assignments**, include a pilot device group. Select **Review + add > Add**, then review **Device status**. [Verify the effective settings](https://docs.microsandbox.dev/enterprise/deploy-and-verify#verify-the-configuration) in an employee session before extending the assignment.

Intune Windows

1

Package the policy

Use your application-packaging tool to create a per-machine MSI that installs `managed.json` beneath the system ProgramData folder with the [Windows permissions](https://docs.microsandbox.dev/enterprise/managed-configuration#file-protection). This is your organization’s configuration package, separate from the microsandbox runtime. Wrap the MSI as an `.intunewin` file with Microsoft’s [Win32 Content Prep Tool](https://learn.microsoft.com/en-us/intune/app-management/deployment/create-win32-package). 2

Create a Win32 app

Open **Apps > All Apps > Create**. Choose **Windows app (Win32)** and upload the `.intunewin` file. On **Program**, enter the MSI’s silent installation and uninstallation commands, choose **System** install behavior, and set **Allow available uninstall** to **No**. 3

Configure detection

In **Detection rules**, choose **Manually configure detection rules**, add an **MSI** rule, and enter your package’s product code and version check. See [Intune’s Win32 app guide](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-win32). MSI detection confirms package installation. It does not prove that the JSON content or permissions still match your policy. 4

Assign and verify

Assign the app as **Required** to a pilot device group, then create it. Review installation status and [verify the effective settings](https://docs.microsandbox.dev/enterprise/deploy-and-verify#verify-the-configuration) as an employee before widening the assignment.


## [​](https://docs.microsandbox.dev/enterprise/deploy-and-verify#verify-the-configuration) Verify the configuration


The check below uses the [sample policy](https://docs.microsandbox.dev/enterprise/managed-configuration#define-managed-settings), which enforces two vCPUs and 1 GiB of memory. Adjust the expected values for your own policy.


1. Sign in as an employee and open a fresh terminal. Confirm `msb context` selects a local backend.
2. Create a sandbox with values that conflict with the sample policy: Shell ``` msb create alpine --name managed-check --cpus 1 --memory 512M msb inspect managed-check --format json ```
3. Confirm `config.resources.cpus` is `2` and `config.resources.memory_mib` is `1024`. Repeat with your employees’ SDKs.
4. Remove the test sandbox with `msb rm --force managed-check`.


Before expanding the pilot, check each supported OS and SDK:


| Check | Pass condition |
| --- | --- |
| Conflicting CLI and SDK options | Managed values win |
| [Registry and network access](https://docs.microsandbox.dev/enterprise/corporate-networking#verify-private-services) | Approved requests succeed; blocked destinations fail |
| Policy update and rollback | A new backend uses the expected policy after each change |
| Cloud creation, if used | Supported settings apply; unsupported options report an error |
| [Disconnected operation](https://docs.microsandbox.dev/enterprise/prepare-environment#verify-without-downloads), if needed | Cached workloads run without downloads |


## [​](https://docs.microsandbox.dev/enterprise/deploy-and-verify#apply-configuration-updates) Apply configuration updates


- **Publish:** replace the complete file atomically, preserving permissions. Update the device-manager package or action and its detection rules together.
- **Roll back:** redeploy the previous policy through the same tool. Removing a device from a deployment’s scope does not remove its file.


There are no file watchers. Applying a policy update depends on what is already running:


| Existing state | How to pick up the change |
| --- | --- |
| CLI command | Run a new command |
| Long-running SDK application | Create a new backend, or restart the application |
| Saved or running sandbox | Policy updates do not rewrite its configuration; create a new sandbox to verify new defaults |
| Open SSH session | Start a new session through a new backend |


Restarting a VM alone does not reload `managed.json`. Keep previous runtime binaries available until applications replace their backend handles and running VMs stop using them. Changing data paths does not migrate existing data.
A missing policy file means no managed overrides; an invalid or unreadable file causes an error when loaded.

Was this page helpful?

Yes No ⌘ I

---

# Microsandbox cloud REST API reference

`https://docs.microsandbox.dev/api-reference/overview`

# Overview
## Documentation Index
## ​Credentials
## ​Base URL
## ​Errors
## ​Pagination
## ​Usage and billing







Authenticate cloud REST API requests with API keys or personal tokens, and handle errors and pagination.

microsandbox cloud is in [private beta](https://docs.microsandbox.dev/cloud/overview); the API is available to organizations with access.
The microsandbox cloud REST API manages sandboxes and the accounts around them. Use it directly when an SDK does not cover your workflow, or when you need account, billing, or audit endpoints.
For running code in sandboxes (exec, streaming, PTY, file transfer, SSH), use the [SDKs](https://docs.microsandbox.dev/sdk/overview) or [CLI](https://docs.microsandbox.dev/cli/overview). They speak the sandbox command channel, which is not part of this REST surface.


## [​](https://docs.microsandbox.dev/api-reference/overview#credentials) Credentials


The sidebar separates endpoints by who the request represents:


| Credential | Format | Represents | Use for |
| --- | --- | --- | --- |
| API key | `msb_...` | An organization | Services, SDKs, CLI automation, and organization resources |
| Personal token | `msb_pat_...` | A user | Account and organization administration |


API keys and personal tokens are both sent as bearer tokens:
Shell

```
curl https://api.microsandbox.dev/v1/sandboxes \
  -H "Authorization: Bearer $MSB_API_KEY"
```


API keys are created in the [dashboard](https://dashboard.microsandbox.dev/access/api-keys). API-key paths infer the organization from the key. Personal-token paths include the organization slug when the request needs an organization.


## [​](https://docs.microsandbox.dev/api-reference/overview#base-url) Base URL


```
https://api.microsandbox.dev
```


## [​](https://docs.microsandbox.dev/api-reference/overview#errors) Errors


Errors return an `error` object with a stable machine-readable `code`, a human-readable `message`, and optional structured `details`:
JSON

```
{
  "error": {
    "code": "invalid_api_key",
    "message": "unauthorized",
    "details": null
  }
}
```


## [​](https://docs.microsandbox.dev/api-reference/overview#pagination) Pagination


List endpoints use cursor pagination. Pass `limit` to size the page and `cursor` to continue from a previous response:
JSON

```
{
  "data": [ ... ],
  "has_more": true,
  "next_cursor": "eyJv..."
}
```


Request the next page with `?cursor=<next_cursor>`; `has_more: false` means you have everything.


## [​](https://docs.microsandbox.dev/api-reference/overview#usage-and-billing) Usage and billing


The usage endpoints report metered consumption for the current period. Reported cost figures are estimates; the [dashboard](https://dashboard.microsandbox.dev/billing) is the source of truth for billing.

Was this page helpful?

Yes No ⌘ I

---

# Local or cloud - microsandbox

`https://docs.microsandbox.dev/operations/backends`

# Local or cloud

microsandbox exposes one CLI and SDK surface across the local runtime and [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview). Local is the default; cloud requires explicit intent and a usable credential.
Use the simplest selector that matches who owns the decision:


| Selector | Best for |
| --- | --- |
| `MSB_BACKEND` | One command, a shell, CI, or deployment configuration |
| SDK | Applications that must choose independently of their environment |
| Named profile | Regular switching or shared environment defaults |


## [​](https://docs.microsandbox.dev/operations/backends#environment) Environment


The `MSB_BACKEND` environment variable selects a backend for a single command or shell, unless an administrator has set a managed active profile:
Shell

```
MSB_BACKEND=local msb run python -- python -V
MSB_BACKEND=cloud MSB_API_KEY="msb_..." msb ls
```


Cloud selection and credentials are separate. `MSB_API_KEY` does not select cloud by itself. `MSB_API_URL` only overrides the cloud endpoint and does not select cloud either.


## [​](https://docs.microsandbox.dev/operations/backends#sdk) SDK


Programmatic selection wins over environment and profile resolution. Use it when the application should decide regardless of where it is launched:
TypeScript Rust Python Ruby

```
import { setDefaultBackend } from "microsandbox";

setDefaultBackend({ kind: "cloud", apiKey: process.env.MSB_API_KEY! });

// Or force the local runtime.
setDefaultBackend("local");
```


```
use microsandbox::{set_default_backend, CloudBackend, LocalBackend};

// Reads MSB_API_KEY.
set_default_backend(CloudBackend::from_env()?);

// Or pass the key explicitly.
set_default_backend(CloudBackend::with_api_key(api_key)?);

// Or force the local runtime.
set_default_backend(LocalBackend::lazy()?);
```


```
import os
from microsandbox import set_default_backend

set_default_backend("cloud", api_key=os.environ["MSB_API_KEY"])

# Or force the local runtime.
set_default_backend("local")
```


```
require "microsandbox"

Microsandbox.use_cloud_backend!(ENV.fetch("MSB_API_KEY"))

# Or force the local runtime.
Microsandbox.use_local_backend!
```


Go selects its backend through the [environment](https://docs.microsandbox.dev/operations/backends#environment) or [profiles](https://docs.microsandbox.dev/operations/backends#profiles); it does not expose a programmatic selector. For an explicit configuration file in Rust, see [backend configuration](https://docs.microsandbox.dev/sdk/rust/configuration#config_path).
Local and cloud backends read user and managed configuration during construction. Invalid files cause an error even when cloud credentials are supplied explicitly. Existing backends retain their settings; construct a new backend to load file changes.


## [​](https://docs.microsandbox.dev/operations/backends#profiles) Profiles


Profiles are named backend configurations in `~/.microsandbox/config.json`. Use them when you switch regularly or want a shared default for an environment:
JSON

```
{
  "active_profile": "production",
  "profiles": {
    "production": {
      "backend": "cloud",
      "api_key_ref": "env:MSB_API_KEY"
    },
    "local": {
      "backend": "local"
    }
  }
}
```


`active_profile` sets the default. `MSB_PROFILE=<name>` selects another profile for one command:
Shell

```
MSB_PROFILE=production msb run python -- python -V
```


Cloud profiles require `api_key_ref`. The optional `url` field defaults to `https://api.microsandbox.dev`; set it only for a development, self-hosted, or on-premises control plane. See the [profiles schema](https://docs.microsandbox.dev/configuration#profiles) for every field and credential-reference format.


## [​](https://docs.microsandbox.dev/operations/backends#precedence) Precedence


Backend resolution uses this order:


1. Programmatic backend set by the SDK
2. Managed `active_profile`, if supplied
3. `MSB_BACKEND=local|cloud`
4. `MSB_PROFILE=<name>`
5. User `active_profile`
6. Local runtime


A managed `active_profile` set to `null` or an empty string clears saved and environment-selected profiles while preserving `MSB_BACKEND`. With no explicit backend, it uses the local fallback. To enforce local execution over `MSB_BACKEND`, select a named managed profile with `backend: local`. Managed profile entries replace same-named user entries. See [Managed deployment](https://docs.microsandbox.dev/enterprise/managed-configuration) for deployment and file format. An explicitly constructed SDK backend keeps its identity. Both local and cloud backends apply managed sandbox settings and host-side SSH policy.
Selecting a cloud profile with `MSB_PROFILE` or `active_profile` is explicit cloud intent when that profile has `"backend": "cloud"`. `MSB_BACKEND=cloud` without a usable API key or cloud profile returns a configuration error; it never falls back to local execution.


## [​](https://docs.microsandbox.dev/operations/backends#verify) Verify


Use `msb context` to inspect the backend kind, selection source, profile, and cloud API URL without exposing the API key:
Shell

```
msb context
msb context --format json
```


Use the SDK accessors to inspect the active backend without exposing its API key. Detailed backend info includes the kind, cloud API URL, selection source, and profile when applicable:
TypeScript Rust Python Go Ruby

```
import { defaultBackendInfo } from "microsandbox";

console.log(defaultBackendInfo());
console.log(sandbox.backendKind);
```


```
let info = microsandbox::default_backend_info();
println!("{}", info.kind.as_str());
println!("{}", sandbox.backend_kind().as_str());
```


```
from microsandbox import default_backend_info

print(default_backend_info())
print(sandbox.backend_kind)
```


```
info, err := microsandbox.DefaultBackendInfo()
if err != nil {
    return err
}
fmt.Println(info.Kind)
fmt.Println(sandbox.BackendKind())
```


```
require "microsandbox"

puts Microsandbox.default_backend_kind
puts sandbox.backend
```


For global defaults and profile storage, see [Configuration](https://docs.microsandbox.dev/operations/configuration). For backend feature differences, see [Cloud compatibility](https://docs.microsandbox.dev/cloud/overview#compatibility).
## Documentation Index
## ​Environment
## ​SDK
## ​Profiles
## ​Precedence
## ​Verify







Was this page helpful?

Yes No ⌘ I

---

# Enforce team settings - microsandbox

`https://docs.microsandbox.dev/enterprise/managed-configuration`

# Enforce team settings
## Documentation Index
## ​Define managed settings
## ​Understand policy coverage
## ​Protect the policy file
## ​Next step






Define the settings your team must use and protect them on employee devices

Once your [pilot environment](https://docs.microsandbox.dev/enterprise/prepare-environment) works with [company networking](https://docs.microsandbox.dev/enterprise/corporate-networking), define which settings employees must use. A protected `managed.json` overrides user configuration and CLI or SDK options; omitted settings remain under employee control.
![Configuration precedence: built-in defaults, user configuration, CLI or SDK options, then managed overrides. Later layers override supplied fields.](https://mintcdn.com/superradcompanyinc/FEDQXJWe4Ve5Sw9P/images/enterprise/managed-deployment-light.svg?fit=max&auto=format&n=FEDQXJWe4Ve5Sw9P&q=85&s=1f07333fc6d63b56900d61e2109cfe62)![Configuration precedence: built-in defaults, user configuration, CLI or SDK options, then managed overrides. Later layers override supplied fields.](https://mintcdn.com/superradcompanyinc/FEDQXJWe4Ve5Sw9P/images/enterprise/managed-deployment-dark.svg?fit=max&auto=format&n=FEDQXJWe4Ve5Sw9P&q=85&s=3363fd14e79be8b0460b54aff75dfb03)


## [​](https://docs.microsandbox.dev/enterprise/managed-configuration#define-managed-settings) Define managed settings


Save the settings you want to enforce as `managed.json`:
JSON

```
{
  "version": 1,
  "overrides": {
    "sandbox_defaults": {
      "cpus": 2,
      "memory_mib": 1024
    },
    "ssh": {
      "inactivity_timeout_secs": 900
    }
  }
}
```


This example enforces **two vCPUs and 1 GiB of memory** for new local and cloud sandboxes, plus a **15-minute inactivity timeout** for SSH sessions created through the CLI or SDK, including sessions to cloud sandboxes.


- **`version`** identifies the managed file format and defaults to `1` when omitted. It is independent of the user config version.
- **`overrides`** accepts the fields in [Global config](https://docs.microsandbox.dev/configuration), including registries, paths, runtime settings, and [outbound proxies](https://docs.microsandbox.dev/enterprise/corporate-networking#route-sandbox-traffic).
- **Omitted settings** remain under employee control. Managed values are never written into the user’s `config.json`.
- **Unrecognized keys** are ignored with a warning listing their paths. Check warnings during rollout to catch misspelled settings.


How overrides are merged

Precedence, from lowest to highest: **built-in defaults → user config → CLI/SDK options → managed overrides**.

| Value | Behavior |
| --- | --- |
| Omitted field | Keep the lower-layer value |
| `null` | Clear a nullable field |
| Nested section | Merge by field |
| Registry hosts | Merge by host and field; omitted auth keeps employee credentials |
| Other maps | Merge by key; replace each supplied entry |
| Array or tagged value | Replace the whole value |

Tagged values need their discriminator, such as `kind`, `mode`, or `protocol`. See [registry rules](https://docs.microsandbox.dev/configuration#auth-resolution-order) and [backend selection](https://docs.microsandbox.dev/operations/backends#precedence) for their specific behavior.


## [​](https://docs.microsandbox.dev/enterprise/managed-configuration#understand-policy-coverage) Understand policy coverage


Supported CLI and SDK backends apply managed settings on the employee device. The file does not configure the cloud service or its hosted SSH gateway.


| Setting | Applies to |
| --- | --- |
| Sandbox defaults, such as CPU and memory | Local creation and outgoing cloud create requests; unsupported cloud options fail |
| Outbound proxy | Local sandboxes; cloud creation fails while a proxy is enforced |
| Registry settings | Host image pulls; cloud pulls use explicit or cloud-stored credentials |
| Runtime and data paths | The local backend |
| SSH inactivity timeout | New CLI/SDK SSH sessions, including connections to cloud sandboxes |
| DNS, destination rules, guest CA trust, published ports | Per-sandbox configuration, rather than individual managed overrides |


An enforced `multi-tenant` [deployment profile](https://docs.microsandbox.dev/networking/overview#deployment-profiles) restricts several network settings together. Snapshot restores reject policy that conflicts with the captured root-disk layout or full-checkpoint CPU and memory geometry.


### [​](https://docs.microsandbox.dev/enterprise/managed-configuration#keep-credentials-separate) Keep credentials separate


Employees can read `managed.json`. Distribute credential references rather than passwords or tokens, and provision the credentials separately. For registries, omit `auth` to preserve employee credentials, supply it to enforce an authentication configuration, or set it to `null` to require anonymous access. See the [registry example](https://docs.microsandbox.dev/enterprise/corporate-networking#connect-to-private-registries).


## [​](https://docs.microsandbox.dev/enterprise/managed-configuration#protect-the-policy-file) Protect the policy file


Your deployment tool must install the policy at the system location below and prevent employees from modifying or replacing it.


### [​](https://docs.microsandbox.dev/enterprise/managed-configuration#file-location) File location


| Platform | Managed file |
| --- | --- |
| macOS | `/Library/Application Support/microsandbox/managed.json` |
| Linux | `/etc/microsandbox/managed.json` |
| Windows | System ProgramData folder + `microsandbox\managed.json`, usually `C:\ProgramData\microsandbox\managed.json` |


`MSB_HOME` and `MSB_CONFIG_PATH` do not change this location. microsandbox needs no additional enrollment, daemon, plist, or mobileconfig.


### [​](https://docs.microsandbox.dev/enterprise/managed-configuration#file-protection) File protection


| Platform | Required deployment permissions |
| --- | --- |
| macOS / Linux | Root-owned directory `0755` and file `0644`; no employee write access through ACLs |
| Windows | Administrators and SYSTEM have full control; employees can read the file and traverse the directory, without write or replacement access |


On macOS and Linux, backend construction fails if the file or its immediate parent directory is not root-owned or is group- or world-writable, or if their permissions cannot be checked. An administrator must correct the reported ownership or permissions before retrying. These checks do not inspect ACLs or other ancestor directories; Windows permissions are not checked. Protect the complete path.
Older CLI and SDK releases do not enforce managed settings. Include supported versions in your rollout. Local administrators can remove policy or replace the runtime.


## [​](https://docs.microsandbox.dev/enterprise/managed-configuration#next-step) Next step


[Deploy and verify](https://docs.microsandbox.dev/enterprise/deploy-and-verify) the policy on a pilot group before rolling it out to the team.

Was this page helpful?

Yes No ⌘ I

---

# AI agents - microsandbox

`https://docs.microsandbox.dev/getting-started/agents`

AI agents are a natural fit for microsandbox. They run tools, inspect files, install packages, call APIs, and execute generated code, often with more ambient access than they should have.
microsandbox gives those actions a dedicated microVM instead of your host process. Agents can still work normally, but the sandbox boundary controls their filesystem, network, lifecycle, and secrets.
The SDK and CLI give you full programmatic control, and there are two additional ways to connect agents directly: **Agent Skills** for coding assistants and an **MCP server** for any MCP-compatible client.


## [​](https://docs.microsandbox.dev/getting-started/agents#agent-skills) Agent Skills


[Agent Skills](https://github.com/superradcompany/skills) teach AI coding agents how to use microsandbox without any custom integration code. Once installed, the agent can create sandboxes, run commands, manage files, and control the full sandbox lifecycle through natural language.
Works with Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, and other agents that support the skills format.
Shell

```
npx skills add superradcompany/skills
```


This installs a set of skill files into your project that the agent reads as context. No server process, no configuration, just files that describe how to use microsandbox.


## [​](https://docs.microsandbox.dev/getting-started/agents#mcp-server) MCP server


The [microsandbox MCP server](https://github.com/superradcompany/microsandbox-mcp) exposes microsandbox as a set of structured tool calls over the [Model Context Protocol](https://modelcontextprotocol.io). Any MCP-compatible client can use it to manage sandbox lifecycle, execute commands, access the filesystem, work with volumes, and monitor sandbox state.
Claude Code Cursor VS Code Claude Desktop Windsurf Open Code Zed

```
claude mcp add --transport stdio microsandbox -- npx -y microsandbox-mcp
```


```
// ~/.cursor/mcp.json
{
  "mcpServers": {
    "microsandbox": {
      "command": "npx",
      "args": ["-y", "microsandbox-mcp"]
    }
  }
}
```


```
// .vscode/mcp.json
{
  "servers": {
    "microsandbox": {
      "command": "npx",
      "args": ["-y", "microsandbox-mcp"]
    }
  }
}
```


```
// ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "microsandbox": {
      "command": "npx",
      "args": ["-y", "microsandbox-mcp"]
    }
  }
}
```


```
// ~/.codeium/windsurf/mcp_config.json
{
  "mcpServers": {
    "microsandbox": {
      "command": "npx",
      "args": ["-y", "microsandbox-mcp"]
    }
  }
}
```


```
// .opencode.json
{
  "mcpServers": {
    "microsandbox": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "microsandbox-mcp"]
    }
  }
}
```


```
// Zed settings
{
  "context_servers": {
    "microsandbox": {
      "command": {
        "path": "npx",
        "args": ["-y", "microsandbox-mcp"]
      }
    }
  }
}
```


Once connected, the agent gets access to tools for creating sandboxes, running commands inside them, reading and writing files, and managing the sandbox lifecycle, all through the MCP protocol.
## Documentation Index
## ​Agent Skills
## ​MCP server




Was this page helpful?

Yes No ⌘ I

---

# Prepare your environment - microsandbox

`https://docs.microsandbox.dev/enterprise/prepare-environment`

# Prepare your environment
## Documentation Index
## ​Choose versions and platforms
## ​Establish a working installation
## ​Prepare offline devices
## ​Next step






Prepare and test one local installation before deploying to the team

Start with one representative employee device. Confirm the runtime, application dependencies, and approved images work before adding company policy or deploying across the fleet.


## [​](https://docs.microsandbox.dev/enterprise/prepare-environment#choose-versions-and-platforms) Choose versions and platforms


Choose compatible CLI and SDK releases for each target OS and architecture. Use releases that support managed configuration; older clients do not enforce it. Check the [installation requirements](https://docs.microsandbox.dev/getting-started/quickstart) and [migration guide](https://docs.microsandbox.dev/migrations/v0.7) when upgrading existing devices.


## [​](https://docs.microsandbox.dev/enterprise/prepare-environment#establish-a-working-installation) Establish a working installation


Follow [runtime setup](https://docs.microsandbox.dev/sdk/setup), install your application’s SDK dependencies, and run `msb doctor` in the employee’s session. Confirm a basic workload starts successfully with an approved image.
Package the approved runtime and dependencies for each target platform, separately from `managed.json`. Install runtimes in the employee’s home or a shared protected location, not root’s or SYSTEM’s home.
The remaining steps cover devices that cannot download dependencies directly. For connected devices, continue to [company networking](https://docs.microsandbox.dev/enterprise/corporate-networking).


## [​](https://docs.microsandbox.dev/enterprise/prepare-environment#prepare-offline-devices) Prepare offline devices


Prepare runtime files, SDK packages, and images on a connected machine, then transfer them through your approved distribution system.


### [​](https://docs.microsandbox.dev/enterprise/prepare-environment#provision-the-runtime) Provision the runtime


Package matching `msb`, `libkrunfw`, and SDK dependencies for each target OS and architecture. Preserve the release’s executable permissions and library links. Follow [runtime setup](https://docs.microsandbox.dev/sdk/setup) and use [managed paths](https://docs.microsandbox.dev/configuration#paths) if you install the runtime in a shared location.
Install application dependencies before disconnecting. Setup helpers can download missing runtime files; use [resolve](https://docs.microsandbox.dev/sdk/setup#resolve-check-install-and-ensure) to require an existing installation without downloading.
Distribution steps are covered in [Deploy and verify](https://docs.microsandbox.dev/enterprise/deploy-and-verify).


### [​](https://docs.microsandbox.dev/enterprise/prepare-environment#transfer-approved-images) Transfer approved images


On a connected machine with the same CPU architecture as the target, pull and export an image. This example uses Alpine; substitute your approved image:
Shell

```
msb pull alpine
msb save --output alpine.tar alpine
```


Transfer the archive through your distribution system. On the employee device, confirm `msb context` selects the local backend, then import it as the employee who will run sandboxes:
Shell

```
msb load --input alpine.tar --tag offline-alpine:approved
```


Load into the same configured home and cache used by the application. Image export can change manifest and layer digests, so use the imported reference rather than assuming the original digest is preserved. See [image archives](https://docs.microsandbox.dev/cli/image-commands#msb-save).


### [​](https://docs.microsandbox.dev/enterprise/prepare-environment#verify-without-downloads) Verify without downloads


Disconnect public network access, run `msb doctor`, and test the imported image:
Shell

```
msb run offline-alpine:approved --pull never --no-net -- /bin/sh -c 'echo offline-ready'
```


`--pull never` fails if the image is unavailable locally. `--no-net` disables guest networking; it does not control host installer downloads. This unnamed sandbox is removed when the command finishes.
Repeat with your actual application and SDK. Include every image, package, and runtime dependency it needs. Fully disconnected workloads can continue directly to [Enforce team settings](https://docs.microsandbox.dev/enterprise/managed-configuration).


## [​](https://docs.microsandbox.dev/enterprise/prepare-environment#next-step) Next step


[Configure company networking](https://docs.microsandbox.dev/enterprise/corporate-networking) for private services and registries.

Was this page helpful?

Yes No ⌘ I

---

# Migrating from v0.6 to v0.7 - microsandbox

`https://docs.microsandbox.dev/migrations/v0.7`

# Migrating from v0.6 to v0.7
## Documentation Index
## ​What changed and why
## ​What the upgrade affects
## ​Upgrade your installation
## ​Later v0.7 releases
## ​Review secret policies
## ​Update snapshot code
## ​Review other application changes
## ​Recover from a migration error
## ​Downgrade to an older release











Upgrade existing sandboxes, update secret and snapshot code, and understand rollback limits.

v0.7 introduces more flexible secret policies and snapshot groups for saved checkpoints and branching. It also improves migration of older configurations and checks for incompatible settings before launch or downgrade.
Use **v0.7.3 or a later compatible patch release**. Earlier v0.7 releases have compatibility gaps addressed in v0.7.3.


## [​](https://docs.microsandbox.dev/migrations/v0.7#what-changed-and-why) What changed and why


- **Secrets have separate controls** for credential substitution, unchanged placeholders, and violation handling. This allows more precise policies, but changes how disabled substitution locations behave.
- **Snapshot groups keep checkpoints immutable**, so overwriting a named member is no longer supported. Capture a new member instead.
- **Compatibility checks catch unsupported state earlier.** Saved configurations migrate automatically; launch and downgrade checks reject settings the selected release cannot represent.


## [​](https://docs.microsandbox.dev/migrations/v0.7#what-the-upgrade-affects) What the upgrade affects


| Component | What to expect |
| --- | --- |
| Saved sandbox configurations | Migrated in place, including image, mount, CPU, and secret settings in saved and recorded active configurations. Valid sandboxes do not need recreating. |
| Application code and configuration files | Not rewritten. Review the changes below. |
| Older SDK applications and CLI jobs sharing `MSB_HOME` | Stop and upgrade them together. Older processes can write incompatible records or fail to read the upgraded database. |
| Running sandbox VMs | Can remain running during migration. They keep their runtime and guest code until restarted. |


Supported older runtimes remain usable for existing operations; newer features may require an upgrade. Selecting an older runtime does not restore older SDK access to an upgraded database.
Cloud users do not run this local migration. Cloud compatibility is handled by the service and requires server support, not just an updated SDK.


## [​](https://docs.microsandbox.dev/migrations/v0.7#upgrade-your-installation) Upgrade your installation


1. **Stop older SDK applications and CLI jobs** sharing the home.
2. **Back up the home.** Stop its sandboxes while copying their disks for a consistent backup.
3. **Update SDK dependencies, lockfiles, and the installed runtime.** Keep `msb` and `libkrunfw` from the same bundle. A home-installed runtime takes precedence over Python and Node bundles; updating the SDK alone may still select it. See [runtime setup](https://docs.microsandbox.dev/sdk/setup).
4. **Apply the code and configuration changes below**, then verify sandbox startup, saved data, and authenticated requests before removing the backup.


For Python:


```
python -m pip install --upgrade 'microsandbox>=0.7.3,<0.8'
```


Use your package manager for other SDKs. For an installed runtime, [`msb self update`](https://docs.microsandbox.dev/cli/management#msb-self) installs the latest release; it cannot select a specific version.


## [​](https://docs.microsandbox.dev/migrations/v0.7#later-v0-7-releases) Later v0.7 releases


If upgrading from an earlier v0.7 release, check these changes as well. Updating SDK packages does not replace the runtime inside an already-running sandbox. Restart it to use new runtime capabilities.


### [​](https://docs.microsandbox.dev/migrations/v0.7#v0-7-7) v0.7.7


- **Ruby:** requires Ruby 3.3 or newer.
- **Go:** update the native SDK library for configured-shell execution and lossless binary output. An older library rejects configured-shell operations.
- **Guest clock:** `--guest-clock off` requires a supporting local runtime. Full snapshots retain the policy; older tools reject those snapshots. Database downgrade is blocked while any saved or active sandbox policy is `off`; stopping alone does not clear a saved policy. See [guest clock](https://docs.microsandbox.dev/sandboxes/snapshots#keep-the-guest-clock).
- **Windows snapshots:** full snapshots now preserve all tracked bind-mount hardlink names. Restore them with an updated runtime; disk-only compatibility is unchanged.


### [​](https://docs.microsandbox.dev/migrations/v0.7#v0-7-8) v0.7.8


- **Disk restores:** supply mappings for every recorded external host mount. `--allow-missing-resources` explicitly permits starting without them. Older disk snapshots without mount records retain their previous behavior. Full restore also requires captured additional disks. See [external mounts](https://docs.microsandbox.dev/sandboxes/snapshots#external-mounts).
- **Detached jobs:** require a supporting local runtime. Wait for or terminate active jobs before a full snapshot or fork. Pausing remains supported; stopping the sandbox terminates its processes, and restarting does not rerun jobs. See [job controls](https://docs.microsandbox.dev/sandboxes/commands#managed-jobs).
- **Secret header restrictions:** non-empty `substitution.header_fields` needs a runtime that enforces it. Older runtimes are rejected rather than silently broadening substitution. Downgrade checks also reject policies the target cannot preserve; do not remove restrictions merely to bypass that check.
- **Filesystem state:** changing `snapshots.max_filesystem_state_mib` affects snapshot admission immediately, while running sandboxes retain their startup budget. Restart them after changing it and configure sufficient budgets on every reader. Older readers may reject larger snapshots. See [snapshot limits](https://docs.microsandbox.dev/configuration#snapshots).


For features and fixes, see [v0.7.7](https://docs.microsandbox.dev/changelog/v0.7.7) and [v0.7.8](https://docs.microsandbox.dev/changelog/v0.7.8).


## [​](https://docs.microsandbox.dev/migrations/v0.7#review-secret-policies) Review secret policies


Saved policies migrate automatically. Update code and configuration files using these previous settings:


| v0.6 setting | v0.7 equivalent |
| --- | --- |
| `injection` | `substitution` |
| `query_params` | `query` |
| Separate `headers` and `basic_auth` | `headers`, enabled if either old switch was enabled |
| Passthrough destinations in the violation policy | Separate passthrough destinations |


Review these behavior changes when using a v0.7 runtime:


- **Basic Auth shares the header switch.** An old Basic-Auth-only policy now also permits substitution in other headers.
- **Disabled locations are version-dependent.** v0.7.0 through v0.7.4 block a placeholder in a disabled location unless its destination has explicit passthrough permission. From v0.7.5, a destination that passes the secret’s host and TLS checks may receive that placeholder unchanged. Other destinations still need explicit passthrough permission or follow the violation policy. Enable substitution to send the credential itself.
- **At least one substitution location must be enabled.** All-disabled policies migrate, but cannot launch until you enable a location or remove the policy.
- **Explicit global passthrough defaults are preserved**, including for future secrets. Per-secret blocking actions override them.


See [SDK examples](https://docs.microsandbox.dev/sandboxes/secrets) and [YAML configuration](https://docs.microsandbox.dev/cli/configuration#secrets).


## [​](https://docs.microsandbox.dev/migrations/v0.7#update-snapshot-code) Update snapshot code


Local snapshot group members are immutable. `force=True` fails even for a new name.
Before: v0.6

```
from microsandbox import Snapshot

snapshot = await Snapshot.create(
    "checkpoint", from_sandbox="workbench", force=True
)
```


Use a generated or unique name and leave `force=False`:
After: v0.7

```
from microsandbox import Snapshot

snapshot = await Snapshot.create(from_sandbox="workbench")
```


To reuse a name, call [`Snapshot.remove()`](https://docs.microsandbox.dev/sdk/python/snapshots#snapshot-remove) first. Removal checks dependencies. **If the next capture fails, the removed checkpoint is lost.** Use a new name to keep the previous checkpoint.
This applies to installed group members; direct archive output can still be overwritten. See [snapshot groups](https://docs.microsandbox.dev/sandboxes/snapshots#snapshot-groups).


### [​](https://docs.microsandbox.dev/migrations/v0.7#restore-external-resources) Restore external resources


For restore and fork (formerly called branch), supply host mounts, published ports, and custom vsock routes explicitly. Snapshots do not copy host files or restore external connections. Full snapshots require compatible runtime and firmware versions.


### [​](https://docs.microsandbox.dev/migrations/v0.7#check-flush-behavior) Check flush behavior


| Policy | Behavior |
| --- | --- |
| `auto` (default) | Flushes running disk-only snapshots. Full snapshots, branches, and pause retain pending writes in memory. |
| `required` | Requires writes on disk, useful when restoring only a full snapshot’s disks. Fails for stopped or crashed sandboxes. Paused sandboxes need a prior acknowledged flush. |


Restart older runtimes before live capture requiring the new flush capability. Go also needs a policy-aware native library. See [Guest flushing](https://docs.microsandbox.dev/sandboxes/snapshots#guest-flushing).


## [​](https://docs.microsandbox.dev/migrations/v0.7#review-other-application-changes) Review other application changes


### [​](https://docs.microsandbox.dev/migrations/v0.7#runtime-setup) Runtime setup


Local creation no longer downloads missing runtimes. Call the explicit [setup helpers](https://docs.microsandbox.dev/sdk/setup) first. Python, TypeScript, and Go setup APIs were also renamed in v0.7.0; see the [old-to-new API mapping](https://docs.microsandbox.dev/sdk/setup#earlier-setup-apis).


### [​](https://docs.microsandbox.dev/migrations/v0.7#https-hostname-rules) HTTPS hostname rules


Strict hostname checking is on by default in v0.7.3. Hostname-only HTTPS allow rules need TLS interception. IP, CIDR, group, and default allow rules are unaffected.
To opt out, use `--net-strict=false` or `network.strict: false`. Go replaces `Strict` with `DisableStrict`. See [hostname rules and HTTPS](https://docs.microsandbox.dev/networking/overview#hostname-rules-and-https).


### [​](https://docs.microsandbox.dev/migrations/v0.7#shutdown-and-connection-limits) Shutdown and connection limits


- **Graceful stop:** no default deadline. Set a timeout where needed; expiry does not force-kill the sandbox.
- **Connections:** unlimited by default for single-tenant sandboxes; 1,024 each for TCP and UDP in multi-tenant sandboxes. Zero means unlimited. `maxConnections` remains a deprecated TCP-only alias.


### [​](https://docs.microsandbox.dev/migrations/v0.7#rust-api-changes) Rust API changes


| API | Change |
| --- | --- |
| `LocalBackend::lazy()` | Now returns `Result`. |
| `LocalBackendBuilder::build_lazy()` | Now returns `Result`. |
| `SdkConfig` | Removed. |
| `load_sdk_config()` | Removed. |
| `SnapshotSpec` | New field: `guest_flush`. |
| `SecretsConfig` | New field: `passthrough_hosts`. |
| `CloudSecretsConfig` | New field: `passthrough_hosts`. |


Handle the new `Result` returns. In struct literals, supply the new fields or use `..Default::default()` where supported. In exhaustive patterns, include the fields or `..`.
For replacements for the removed APIs, see [configuration](https://docs.microsandbox.dev/operations/configuration) and [runtime setup](https://docs.microsandbox.dev/sdk/setup).


## [​](https://docs.microsandbox.dev/migrations/v0.7#recover-from-a-migration-error) Recover from a migration error


If v0.7.0–v0.7.2 reports `unsupported persisted sandbox configuration`, upgrade to v0.7.3 and retry first. A v0.7.2 database can upgrade directly; no downgrade to v0.6 is needed.
A malformed saved configuration aborts the whole migration before converted rows are written. The error names the sandbox and configuration column.


1. Stop SDK applications sharing the home and keep a consistent backup.
2. Repair the named configuration using the previous SDK/CLI that can read it. Remove the sandbox only if its data is no longer needed.
3. Retry the upgrade.


Do not delete the database, edit migration history, or skip the row. If previous tools cannot read it, report the error and SDK/runtime versions. Do not share unredacted secrets.


## [​](https://docs.microsandbox.dev/migrations/v0.7#downgrade-to-an-older-release) Downgrade to an older release


Run `msb self downgrade` from the **newer CLI** before replacing it, including through Homebrew, or reinstalling older SDKs. Only the newer CLI contains the rollback steps for its migrations.


```
msb self downgrade 0.6.18
```


- Stop applications sharing the home and keep the default backup enabled.
- Schema rollbacks and v0.6 configuration rewrites require stopped sandboxes. If the command reports active sandboxes, stop them and retry.
- Incompatible settings are rejected before changes. For example, v0.7.0–v0.7.2 cannot preserve global secret passthrough defaults, even empty lists. Force flags do not bypass these checks.


A database downgrade does not make every newer snapshot or feature usable by an older release. See [downgrade options](https://docs.microsandbox.dev/cli/management#msb-self).


### [​](https://docs.microsandbox.dev/migrations/v0.7#database-schema-is-newer-than-this-msb-binary) Database schema is newer than this msb binary


After replacing a v0.7 binary with v0.6, even `msb list` can report:


```
database schema is newer than this msb binary
```


Attempting downgrade from the older CLI can instead report:


```
local database was updated by a newer msb or does not contain a valid migration prefix
```


After a binary-only downgrade, these errors indicate newer database state, not necessarily corruption.
If you already uninstalled the newer CLI:


1. Reinstall the release that last migrated the home, or a later compatible release, with its matching `libkrunfw`. Keep the existing `MSB_HOME`.
2. Check `msb --version` to confirm your shell is invoking the newer binary.
3. Follow the stopped-sandbox and backup requirements above, then run `msb self downgrade 0.6.18` from that newer binary.
4. After the command succeeds, verify `msb list` with the target release before returning SDK applications to that version.


Do not delete the catalog or edit migration history to bypass the refusal. If the restored newer CLI also rejects the catalog, report the error and the versions involved.


### [​](https://docs.microsandbox.dev/migrations/v0.7#snapshot-groups-can-block-downgrade) Snapshot groups can block downgrade


Downgrading to a release without group support is refused while groups, even empty ones, or duplicate snapshot identities remain. The error begins `snapshot groups prevent downgrade`.
New v0.7 captures use a [group](https://docs.microsandbox.dev/sandboxes/snapshots#snapshot-groups) by default, including disk snapshots. Existing v0.6 snapshots remain ungrouped when upgrading.
To proceed, export the snapshots you need, verify the backup, then remove the blocking snapshots and empty groups before retrying the downgrade.
Exports preserve snapshots for later use with v0.7. They do **not** convert snapshots for v0.6.


Back up snapshots before downgrading

Use the newer CLI and follow the backup requirements above. This example uses one snapshot, `app:ready`.

1. Export outside `MSB_HOME`, including ancestors and the image: ``` mkdir -p "$HOME/msb-snapshot-backups" msb snap export app:ready \ --output "$HOME/msb-snapshot-backups/app-ready.msb" \ --with-parents --with-image ```
2. Import and verify with the newer CLI in a separate home: ``` recovery_home=$(mktemp -d) MSB_HOME="$recovery_home" msb snap import \ "$HOME/msb-snapshot-backups/app-ready.msb" --group recovered MSB_HOME="$recovery_home" msb snap verify recovered ``` Keep the recovery home and archive, and test a restore before removing the original. Import into a separate home to avoid creating another group that blocks downgrade.
3. After confirming the backup, remove the original snapshot: ``` msb snap rm app:ready msb snap ls --group app ``` For multiple members, export each snapshot you need. Remove children before parents, selecting another head with `msb snap head app:<member>` before removing the current head. Do not force past dependency errors.
4. Once the group is empty, move its remaining directory outside the snapshot store. For the default location: ``` mv "${MSB_HOME:-$HOME/.microsandbox}/snapshots/app" \ "$HOME/msb-snapshot-backups/app-empty-group" msb self downgrade 0.6.18 ``` Adjust the path for a custom snapshot location. Repeat for other groups before downgrading; ungrouped duplicate instances may also need cleanup.


#### [​](https://docs.microsandbox.dev/migrations/v0.7#import-after-returning-to-v0-7) Import after returning to v0.7

With a compatible v0.7 CLI installed again:

```
msb snap import "$HOME/msb-snapshot-backups/app-ready.msb" --group app
msb snap ls --group app
```


Was this page helpful?

Yes No ⌘ I

---

# Microsandbox SDK errors and resource cleanup

`https://docs.microsandbox.dev/sdk/errors`

# Error handling
## Documentation Index
## ​Matching errors
## ​Spawn-time exec failures
## ​Name conflicts
## ​When a sandbox object is stale
## ​Stop observation timeouts
## ​Sandbox start failures
## ​Resource cleanup









Handle sandbox errors and clean up resources across the microsandbox SDKs.

Use typed errors to handle specific failures without parsing messages. The examples show each SDK’s matching and cleanup conventions.


## [​](https://docs.microsandbox.dev/sdk/errors#matching-errors) Matching errors


TypeScript Rust Python Go Ruby

```
// Each error variant has a dedicated subclass; match it with instanceof.
import {
    ExecTimeoutError,
    RuntimeError,
    Sandbox,
} from "microsandbox";

const sb = await Sandbox.builder("worker")
    .image("python")
    .connectOrCreate();

try {
    const output = await sb.exec("python", ["script.py"]);
    if (!output.success) {
        console.error(`Failed (exit ${output.code}):`, output.stderr());
    }
} catch (e) {
    if (e instanceof ExecTimeoutError) {
        console.error(`Timed out after ${e.timeoutMs}ms`);
    } else if (e instanceof RuntimeError) {
        console.error("Runtime:", e.message);
    } else {
        throw e;
    }
}
```


```
// Match variants of the Error enum.
use microsandbox::{Sandbox, Error};

let sb = Sandbox::builder("worker")
    .image("python")
    .connect_or_create()
    .await?;

match sb.exec("python", ["script.py"]).await {
    Ok(output) if output.status().success => {
        println!("{}", output.stdout()?);
    }
    Ok(output) => {
        eprintln!("Exit {}: {}", output.status().code, output.stderr()?);
    }
    Err(Error::ExecTimeout) => eprintln!("Timed out"),
    Err(Error::Runtime(msg)) => eprintln!("Runtime: {msg}"),
    Err(e) => return Err(e),
}
```


```
# Match dedicated exception classes.
from microsandbox import ExecTimeoutError, Sandbox

sb = await Sandbox.connect_or_create("worker", image="python")

try:
    output = await sb.exec("python", ["script.py"])
    if not output.success:
        print(f"Exit {output.exit_code}: {output.stderr_text}")
except ExecTimeoutError:
    print("Timed out")
```


```
// *Error carries an ErrorKind; inspect it with IsKind or errors.As.
import (
    "context"
    "errors"
    "log"

    m "github.com/superradcompany/microsandbox/sdk/go"
)

sb, err := m.ConnectOrCreateSandbox(ctx, "worker", m.WithImage("python"))
if err != nil {
    log.Fatal(err)
}

out, err := sb.Exec(ctx, "python", []string{"script.py"})
switch {
case err == nil && !out.Success():
    log.Printf("exit %d: %s", out.ExitCode(), out.Stderr())
case m.IsKind(err, m.ErrExecTimeout):
    log.Println("timed out")
case err != nil:
    // errors.As for deeper inspection.
    var me *m.Error
    if errors.As(err, &me) {
        log.Printf("kind=%s message=%s", me.Kind, me.Message)
    }
}
```


```
# Since v0.7.4, typed Error subclasses expose stable code strings.
# Failures without a dedicated subclass still use Microsandbox::Error.
require "microsandbox"

sb = Microsandbox::Sandbox.connect_or_create("worker", image: "python")

begin
  output = sb.exec("python", ["script.py"])
  warn "Exit #{output.exit_code}: #{output.stderr}" unless output.success?
rescue Microsandbox::ExecTimeoutError => error
  warn "Timed out: #{error.message}"
rescue Microsandbox::Error => error
  warn error.message
end
```


## [​](https://docs.microsandbox.dev/sdk/errors#spawn-time-exec-failures) Spawn-time exec failures


`exec()` distinguishes between:
**A program that ran and exited non-zero**: the call returns an `ExecOutput` with a non-zero `code`. This is *not* an error in the SDK sense; it’s a normal result.
**A program that never started**: the binary doesn’t exist, isn’t executable, the working directory is unreachable, etc. The call returns or raises an SDK error.
TypeScript Rust Python Go Ruby

```
try {
    const output = await sb.exec("nonexistent");
    // program ran, check output.success / output.code
} catch (e) {
    console.error("Program could not be started:", e);
}
```


```
use microsandbox::{protocol::exec::ExecFailureKind, Error};

match sb.exec("nonexistent", []).await {
    Ok(output) => { /* program ran, check output.status() */ }
    Err(Error::ExecFailed(payload)) => {
        match payload.kind {
            ExecFailureKind::NotFound => {
                eprintln!("Binary not found on PATH: {}", payload.message);
            }
            ExecFailureKind::PermissionDenied => {
                eprintln!("Not executable (chmod +x?): {}", payload.message);
            }
            kind => {
                eprintln!("Spawn failed ({:?}): {}", kind, payload.message);
            }
        }
        // payload.errno, payload.errno_name, payload.stage are also available
    }
    Err(e) => return Err(e),
}
```


```
from microsandbox import MicrosandboxError

try:
    output = await sb.exec("nonexistent")
    # If the program ran, check output.success and output.exit_code.
except MicrosandboxError as e:
    print(f"Program could not be started: {e}")
```


```
// Streaming exec surfaces spawn-failure detail via ExecEventFailed.
h, err := sb.ExecStream(ctx, "nonexistent", nil)
if err != nil {
    return err
}
defer h.Close()

for {
    ev, err := h.Recv(ctx)
    if err != nil {
        return err
    }
    switch ev.Kind {
    case m.ExecEventExited:
        // Program ran; inspect ev.ExitCode.
    case m.ExecEventFailed:
        f := ev.Failure // *m.ExecFailure
        switch f.Kind {
        case "not_found":
            log.Printf("Binary not on PATH: %s", f.Message)
        case "permission_denied":
            log.Printf("Not executable (chmod +x?): %s", f.Message)
        default:
            log.Printf("Spawn failed (%s): %s", f.Kind, f.Message)
        }
        // f.Errno (*int), f.ErrnoName, f.Path are also available.
    case m.ExecEventDone:
        return nil
    }
}
```


```
require "microsandbox"

begin
  output = sandbox.exec("nonexistent")
  # If the program ran, check output.success? and output.exit_code.
rescue Microsandbox::Error => e
  warn "Program could not be started: #{e.message}"
end
```


Structured spawn-failure details

See [Rust failure kinds](https://docs.microsandbox.dev/sdk/rust/execution#execfailurekind) and [Go execution failures](https://docs.microsandbox.dev/sdk/go/execution#execfailure) for structured payloads. The handling examples above show how to inspect them.
The CLI maps these kinds to POSIX-style exit codes: `127` for `NotFound`, `126` for `PermissionDenied` and `NotExecutable`, and `1` otherwise.


## [​](https://docs.microsandbox.dev/sdk/errors#name-conflicts) Name conflicts


Creating a sandbox with a name that’s already in use (and without `replace`) surfaces a typed error. Branch on it to decide how to recover, such as resuming the existing sandbox or regenerating the name.
TypeScript Rust Python Go Ruby

```
import { Sandbox, SandboxAlreadyExistsError } from "microsandbox";

try {
    const sb = await Sandbox.builder("worker").image("alpine").create();
} catch (e) {
    if (e instanceof SandboxAlreadyExistsError) {
        console.error("sandbox already exists; resume or pass replace()");
    } else {
        throw e;
    }
}
```


```
use microsandbox::{Error, Sandbox};

match Sandbox::builder("worker").image("alpine").create().await {
    Ok(sb) => { /* ... */ }
    Err(Error::SandboxAlreadyExists(name)) => {
        eprintln!("sandbox {name} already exists; resume or pass .replace()");
    }
    Err(e) => return Err(e),
}
```


```
from microsandbox import Sandbox, SandboxAlreadyExistsError

try:
    sb = await Sandbox.create("worker", image="alpine")
except SandboxAlreadyExistsError:
    print("sandbox already exists; resume or pass replace=True")
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("alpine"))
if m.IsKind(err, m.ErrSandboxAlreadyExists) {
    log.Println("sandbox already exists; resume or pass WithReplace()")
}
```


```
begin
  sb = Microsandbox::Sandbox.create("worker", image: "alpine")
rescue Microsandbox::SandboxAlreadyExistsError
  warn "sandbox already exists; use connect_or_create to reuse it or replace: true to recreate it"
end
```


Use `connect_or_create` and its language-specific equivalents to reuse the existing sandbox without changing its configuration. Pass `replace()` / `replace=True` / `replace: true` / `--replace` / `WithReplace()` only when you intend to stop the existing sandbox and create a new one. See [Naming conflicts](https://docs.microsandbox.dev/sandboxes/overview#naming-conflicts) for the grace-period setting.


## [​](https://docs.microsandbox.dev/sdk/errors#when-a-sandbox-object-is-stale) When a sandbox object is stale


A `Sandbox` or `SandboxHandle` keeps the ID of the exact sandbox it represents. If that sandbox is removed and the name is reused, lifecycle methods refuse to act on the replacement and return a typed error.
TypeScript Rust Python Go Ruby

```
import { SandboxReplacedError } from "microsandbox";

try {
  await staleHandle.destroy();
} catch (error) {
  if (!(error instanceof SandboxReplacedError)) throw error;
}
```


```
match stale_handle.destroy().await {
    Err(Error::SandboxReplaced { expected, actual, .. }) => {
        eprintln!("refusing stale operation: {expected} -> {actual}");
    }
    result => result?,
}
```


```
from microsandbox import SandboxReplacedError

try:
    await stale_handle.destroy()
except SandboxReplacedError:
    pass
```


```
if err := staleHandle.Destroy(ctx); m.IsKind(err, m.ErrSandboxReplaced) {
    log.Println("refusing stale lifecycle operation")
}
```


```
# No dedicated stale-identity subclass yet: Error and the stable
# "was replaced" message are the contract. Replacement is never acted on.
begin
  stale_handle.destroy
rescue Microsandbox::Error => error
  raise unless error.message.include?("was replaced")
end
```


## [​](https://docs.microsandbox.dev/sdk/errors#stop-observation-timeouts) Stop observation timeouts


On Local, a graceful-stop timeout causes the SDK to force-kill the sandbox.
On Cloud, the same timeout only limits how long the SDK waits: the accepted server-side stop is not cancelled and may still complete.
Cloud reports this with `SandboxStopTimedOutError` in TypeScript and Python, `Error::SandboxStopTimedOut` in Rust, and `ErrSandboxStopTimedOut` in Go. Ruby currently raises `Microsandbox::Error` with a message explaining that the accepted stop may still complete.
After a Cloud timeout, poll the sandbox status or call the wait-until-stopped method if you still need confirmation. Calling `request_stop` first is useful when the application wants to submit the stop and control its own observation deadline.


## [​](https://docs.microsandbox.dev/sdk/errors#sandbox-start-failures) Sandbox start failures


When a sandbox process exits before the agent relay is ready, creation returns or raises an SDK error.
TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

try {
    const sb = await Sandbox.builder("svc").image("alpine").create();
} catch (e) {
    console.error("Sandbox failed to start:", e);
}
```


```
// BootStart exposes the failure stage and underlying message.
use microsandbox::{Error, Sandbox};

match Sandbox::builder("svc").image("alpine").create().await {
    Ok(sb) => { /* ... */ }
    Err(Error::BootStart { name, err }) => {
        eprintln!("Sandbox {name:?} failed at stage {:?}: {}", err.stage, err.message);
    }
    Err(e) => return Err(e),
}
```


```
from microsandbox import MicrosandboxError, Sandbox

try:
    sb = await Sandbox.create("svc", image="alpine")
except MicrosandboxError as e:
    print(f"Sandbox failed to start: {e}")
```


```
_, err := m.CreateSandbox(ctx, "svc", m.WithImage("alpine"))
if err != nil {
    log.Printf("sandbox failed to start: %v", err)
}
```


```
require "microsandbox"

begin
  sandbox = Microsandbox::Sandbox.create("svc", image: "alpine")
rescue Microsandbox::Error => e
  warn "Sandbox failed to start: #{e.message}"
end
```


Startup errors include guest initialization failures, such as a user missing from the image.
The CLI prints the startup failure before any captured log output so the immediate cause stays visible.


## [​](https://docs.microsandbox.dev/sdk/errors#resource-cleanup) Resource cleanup


Limited on cloud
Sandboxes hold compute resources, so release them when done.
TypeScript Rust Python Go Ruby

```
async function runTemporary(): Promise<string> {
    // Node 22+: prefer `await using`; it calls Sandbox.stop() on scope exit.
    await using sb = await Sandbox.builder("temp")
        .image("python")
        .replace()
        .create();

    const out = await sb.exec("python", ["-c", "print('hello')"]);
    return out.stdout();
}
```


```
use microsandbox::Sandbox;

// Sandbox implements Drop, so resources are released when `sb` goes out of scope.
// For explicit control, call stop() or kill().
{
    let sb = Sandbox::builder("temp")
        .image("python")
        .create()
        .await?;

    let output = sb.exec("python", ["-c", "print('hello')"]).await?;
} // sb is dropped here, resources are cleaned up
```


```
# Use async context manager: auto-kills and removes on exit.
async with await Sandbox.create("temp", image="python") as sb:
    output = await sb.exec("python", ["-c", "print('hello')"])
    print(output.stdout_text)
```


```
// Pair each CreateSandbox with deferred Stop and Close.
sb, err := m.CreateSandbox(ctx, "temp",
    m.WithImage("python"),
    m.WithReplace(),
)
if err != nil {
    log.Fatal(err)
}
defer func() {
    stopCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    _ = sb.Stop(stopCtx)
    _ = sb.Close()
}()

out, _ := sb.Exec(ctx, "python", []string{"-c", "print('hello')"})
fmt.Println(out.Stdout())
```


```
Microsandbox::Sandbox.with("temp", image: "python", replace: true) do |sandbox|
  output = sandbox.exec("python", ["-c", "print('hello')"])
  puts output.stdout
end
```


Was this page helpful?

Yes No ⌘ I

---

# TypeScript SDK Sandbox reference

`https://docs.microsandbox.dev/sdk/typescript/sandbox`

See [Overview](https://docs.microsandbox.dev/sandboxes/overview) for configuration examples and [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle) for state management.

See [Snapshots](https://docs.microsandbox.dev/sdk/typescript/snapshots#forking) for live fork methods.


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#functions) Functions


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#allsandboxmetrics) allSandboxMetrics()


Local-only


```
allSandboxMetrics(): Promise<Record<string, SandboxMetrics>>
```


Return one [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) snapshot for every running sandbox, keyed by sandbox name. See [Metrics](https://docs.microsandbox.dev/sandboxes/metrics) for a complete example.


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox) Sandbox


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-builder) Sandbox. builder()


```
static builder(name: string): SandboxBuilder
```


Example


```
await using sandbox = await Sandbox.builder("api")
  .image("python")
  .create();
```


Begin building a new sandbox. Configure it with chainable setters, then call `.create()` to boot it. Sandbox names must be non-empty and no longer than 128 UTF-8 bytes. See [`SandboxBuilder`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder) for all available options.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


[SandboxBuilder](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder) Fluent builder for configuring the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-get) Sandbox. get()


```
static get(name: string): Promise<SandboxHandle>
```


Example


```
const handle = await Sandbox.get("api");
console.log(handle.status);
```


Get a live handle to an existing sandbox (running or stopped). The handle provides status, configuration, and lifecycle control without requiring a full connection to the guest agent.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


[Promise<SandboxHandle>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxhandle) Live handle with status and lifecycle control.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-list) Sandbox. list()


```
static list(): Promise<SandboxPage>
```


Example


```
const page = await Sandbox.list();
for (const h of page.sandboxes) {
  console.log(`${h.name} - ${h.status}`);
}
```


Return the first page of sandboxes (running, stopped, and crashed), ordered newest first. The default page size is 20. Handles are read-only - call [`Sandbox.get(name)`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-get) to get a live handle for lifecycle calls.


Returns


Promise<SandboxPage> Read-only handles in this page and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-listwith) Sandbox. listWith()


```
static listWith(configure: (list: SandboxListBuilder) => SandboxListBuilder): Promise<SandboxPage>
```


Example


```
const page = await Sandbox.listWith((list) =>
  list.limit(50).label("role", "worker"),
);

if (page.nextCursor) {
  const nextPage = await Sandbox.listWith((list) =>
    list.limit(50).cursor(page.nextCursor!).label("role", "worker"),
  );
}
```


Return a configured page of sandboxes. Label filters are applied before pagination and are AND-matched. Like [`list()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-list), returned handles are read-only.


Parameters


`configure` (list: SandboxListBuilder) => SandboxListBuilder Configure a limit (1-100), next-page cursor, and/or AND-matched labels.


Returns


Promise<SandboxPage> Matching read-only handles and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-remove) Sandbox. remove()


```
static remove(name: string): Promise<void>
```


Example


```
await Sandbox.remove("api");
```


Delete a stopped sandbox by name. See [Destroy or remove](https://docs.microsandbox.dev/sandboxes/lifecycle#destroy-or-remove) for the exact local deletion scope and the external resources that are preserved. Fails if the sandbox is still running. Stop it first.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-start) Sandbox. start()


```
static start(name: string): Promise<Sandbox>
```


Example


```
await using sandbox = await Sandbox.start("api");
```


Restart a previously stopped sandbox. The VM reboots using the persisted configuration. A local handle enters attached mode and stops when its `await using` binding goes out of scope. A cloud handle does not own the service-managed VM, so stop or remove it explicitly.


Parameters


`name` string Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[Promise<Sandbox>](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-startdetached) Sandbox. startDetached()


```
static startDetached(name: string): Promise<Sandbox>
```


Example


```
const sandbox = await Sandbox.startDetached("worker");
```


Restart a stopped sandbox in detached mode. The sandbox survives after your process exits.


Parameters


`name` string Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[Promise<Sandbox>](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) Running sandbox.
## Documentation Index
## ​Functions
## ​Sandbox
## ​SandboxBuilder
## ​PatchBuilder
## ​LogEntry
*Returned by logs() · logStream()*

## ​LogStream
*Returned by logStream()*

## ​MetricsStream
*Returned by metricsStream()*

## ​PullProgressCreate
*Returned by createWithPullProgress()*

## ​SandboxListBuilder
## ​SandboxHandle
*Returned by Sandbox.get() · Sandbox.list() · Sandbox.listWith()*

## ​RegistryConfigBuilder
## ​Types















Instance methods


A running `Sandbox` exposes `name` (`string`), `id` (`string`), and `ownsLifecycle` (`boolean`) as read-only properties. The stable opaque `id` changes when a removed name is recreated. Local attached handles own lifecycle; local detached handles and all cloud handles do not, because the cloud worker owns the sandbox process.
Command execution (`exec`, `execWith`, `execStream`, `execStreamWith`, `shell`, `shellStream`) and foreground attachment (`attach`, `attachWith`, `attachShell`) live on the [Execution](https://docs.microsandbox.dev/sdk/typescript/execution) page.
Lifecycle calls do not wait for unrelated guest operations on the same handle to finish. For example, you can pause and resume while an `exec()` promise is pending. Await operations explicitly when their order matters; stopping a sandbox may interrupt pending commands or filesystem requests.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-config) sandbox. config()


```
config(): Promise<SandboxConfig>
```


Example


```
const config = await sandbox.config();
console.log(`${config.memoryMib} MiB`);
```


Get the full configuration the sandbox was created with - image, cpus, memory, env, mounts, and the rest. The shape mirrors [`SandboxBuilder.build()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-build).


Returns


[Promise<SandboxConfig>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig) Sandbox configuration.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-detach) sandbox. detach()


```
detach(): Promise<void>
```


Example


```
await sandbox.detach(); // keeps running in the background
```


Release the handle without stopping the sandbox. The sandbox continues running as a background process. Reconnect later with [`Sandbox.get()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-get).
After detaching, this handle and its existing `fs()` objects reject new guest operations. Already-started operations retain their connection; await them before detaching if you need their results first.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-fs) sandbox. fs()


```
fs(): SandboxFsOps
```


Example


```
await sandbox.fs().writeFile("/tmp/hello.txt", "hi");
```


Get a filesystem handle for reading and writing files inside the running sandbox. See [Filesystem](https://docs.microsandbox.dev/sdk/typescript/filesystem) for API details.


Returns


[SandboxFsOps](https://docs.microsandbox.dev/sdk/typescript/filesystem) Filesystem handle.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-kill) sandbox. kill()


Local-only


```
kill(): Promise<void>
```


Example


```
await sandbox.kill(); // no graceful shutdown
```


Force-terminate the sandbox and wait until stopped state is observed. No graceful shutdown - use when the sandbox is unresponsive. Pending writes that the workload hasn’t `fsync`’d may be lost, same durability semantics as a sudden power loss on a physical machine. Prefer [`stop()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-stop) for graceful shutdown that gives the workload a chance to flush.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-killwithtimeout) sandbox. killWithTimeout()


Local-only


```
killWithTimeout(timeoutMs: number): Promise<void>
```


Example


```
await sandbox.killWithTimeout(2000);
```


Force-terminate the sandbox and wait up to `timeoutMs` for stopped-state observation.


Parameters


`timeoutMs` number Milliseconds to wait for the stopped state to be observed.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logs) sandbox. logs()


Local-only


```
logs(opts?: LogReadOptions): Promise<LogEntry[]>
```


Example


```
import { Sandbox } from "microsandbox";

const handle = await Sandbox.get("web");

// Default: all user-program output, regardless of pipe/pty mode
const entries = await handle.logs();

for (const e of entries) {
  const source =
    e.source === "stdout" ? "OUT" :
    e.source === "stderr" ? "ERR" :
    e.source === "output" ? "PTY" :
    "SYS";

  console.log(
    `[${e.timestamp.toISOString()}] ${source} ${e.sessionId}: ${e.text().trimEnd()}`
  );
}

// Filtered: last 50 entries from the past hour, including system lines
const recent = await handle.logs({
  tail: 50,
  since: new Date(Date.now() - 60 * 60 * 1000),
  sources: ["stdout", "stderr", "output", "system"],
});
```


Read captured output from the sandbox’s `exec.log`. Backed by an on-disk JSON Lines file the runtime writes via the relay tap. Works on running and stopped sandboxes alike - there is no protocol traffic. The same method is available on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxhandle) for callers that don’t want to start the sandbox first.
The default sources are `"stdout"`, `"stderr"`, and `"output"` (PTY-merged). Pass `"system"` to also include synthetic lifecycle markers and runtime/kernel diagnostic lines, or `"all"` for every source.


Parameters


`opts` [LogReadOptions?](https://docs.microsandbox.dev/sdk/typescript/sandbox#logreadoptions) Filters: `tail`, `since`, `until`, `sources`. Omit for the default user-program sources.


Returns


[Promise<LogEntry[]>](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) Matching entries in chronological order.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logstream) sandbox. logStream()


Limited on cloud


```
logStream(opts?: LogStreamOptions): Promise<LogStream>
```


Example


```
await using stream = await sandbox.logStream({ follow: true });
for await (const e of stream) {
  console.log(e.text().trimEnd());
}
```


Stream captured output as it appears, with optional follow. Backed by the same on-disk `exec.log` as [`logs()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logs), but yields entries lazily. Pass `{ follow: true }` to keep the stream open past current EOF and pick up new entries as they are written; otherwise the stream drains the current contents and ends. Each yielded [`LogEntry`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) carries an opaque `cursor` that can be passed back via [`LogStreamOptions.fromCursor`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstreamoptions) to resume.


Parameters


`opts` [LogStreamOptions?](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstreamoptions) Filters plus `follow` and resume controls (`since`, `fromCursor`).


Returns


[Promise<LogStream>](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstream) Async iterable of log entries.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-ping) sandbox. ping()


Local-only


```
ping(): Promise<SandboxPingResult>
```


Example


```
const health = await sandbox.ping();
console.log(`${health.name}: ${health.latencyMs.toFixed(1)} ms`);
```


Check that the running sandbox’s guest agent is reachable without refreshing idle activity. This sends `core.ping` and waits for `core.pong`; it does not start stopped sandboxes and returns an error if the sandbox is not running or `agentd` cannot respond. After upgrading from a runtime that predates protocol generation 6, restart already-running sandboxes so the guest agent understands the message.


Returns


[Promise<SandboxPingResult>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxpingresult) Sandbox name and agent round-trip latency.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-touch) sandbox. touch()


Local-only


```
touch(): Promise<SandboxTouchResult>
```


Example


```
const keepalive = await sandbox.touch();
console.log(`${keepalive.name}: ${keepalive.activitySeq}`);
```


Explicitly refresh the running sandbox’s idle activity. This sends `core.touch`, receives `core.touched`, and advances the guest activity sequence used by the runtime idle-timeout monitor. It does not start stopped sandboxes and it does not bypass `maxDuration`.


Returns


[Promise<SandboxTouchResult>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxtouchresult) Sandbox name and updated activity sequence.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-modify) sandbox. modify()


Local-only


```
modify(opts?: ModifyOptions): Promise<SandboxModificationPlan>
```


Example


```
// Live resize: applies to the running VM when within the booted capacity
const plan = await sandbox.modify({ cpus: 4, memory: 4096 });
for (const r of plan.resizeStatus) {
  console.log(`${r.resource}: ${r.requested} -> ${r.actual} (${r.state})`);
}

// Preview a change without applying it
const preview = await sandbox.modify({ maxMemory: 16384, dryRun: true });
for (const c of preview.changes) {
  console.log(`${c.field}: ${c.disposition}`);
}

// Make an env change active now by restarting
await sandbox.modify({ env: { MODE: "prod" }, policy: "restart" });
// Grow the owned OCI root disk while it is running
await sandbox.modify({ rootDiskSize: 8192 });

// Add or rotate a host-environment secret; restart if it is newly added
await sandbox.modify({
  secrets: {
    API_KEY: { env: "API_KEY", allowedHosts: ["api.example.com"] },
  },
  policy: "restart",
});

// Remove an existing secret
await sandbox.modify({ secretsRemove: ["OLD_API_KEY"] });
```


Plan or apply a configuration change. The returned plan labels each change `"live"`, `"next start"`, `"requires restart"`, or `"unsupported"`.
`cpus` and `memory` resize live within the [`maxCpus`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-maxcpus) / [`maxMemory`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-maxmemory) ceilings; raising a ceiling requires a restart.
`rootDiskSize` grows owned managed and flat ext4 roots live, including checkpoint-backed roots, tmpfs root disks can change in either direction on the next boot, and user-supplied disk images are rejected.
Env and workdir changes affect future execs only. Stopped roots grow before the new size is saved. Explicit restart and next-start policies remain available.
Secret specs are keyed by stable secret name. Each `SecretModifySpec` selects at most one source (`env`, `value`, or `store`) and may also set `placeholder` and `allowedHosts`; omitting a source updates only the other supplied fields. Plans expose only safe references and metadata; raw secret values never appear in a plan. Removal is explicit through `secretsRemove`.
A live CPU or memory resize can take a moment to settle. The new limits are enforced immediately, and the returned plan’s `resizeStatus` reports when the sandbox has finished adjusting. See [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmodificationplan).


Parameters


`opts` [ModifyOptions](https://docs.microsandbox.dev/sdk/typescript/sandbox#modifyoptions) Requested changes plus `policy` and `dryRun`. Omitted fields are left unchanged.


Returns


[Promise<SandboxModificationPlan>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmodificationplan) The modification plan, applied unless `dryRun: true`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-metrics) sandbox. metrics()


Local-only


```
metrics(): Promise<SandboxMetrics>
```


Example


```
const m = await sandbox.metrics();
console.log(`cpu ${m.cpuPercent.toFixed(1)}% · mem ${Math.round(m.memoryBytes / 1048576)} MiB`);
```


Get a point-in-time snapshot of the sandbox’s resource usage: CPU, memory, disk I/O, network I/O, optional upper disk usage, and uptime.


Returns


[Promise<SandboxMetrics>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) Resource metrics.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-metricsstream) sandbox. metricsStream()


Local-only


```
metricsStream(intervalMs: number): Promise<MetricsStream>
```


Example


```
await using stream = await sandbox.metricsStream(1000);
for await (const snapshot of stream) {
  console.log(`${snapshot.cpuPercent.toFixed(1)}%`);
}
```


Stream resource metrics at a regular interval. The returned [`MetricsStream`](https://docs.microsandbox.dev/sdk/typescript/sandbox#metricsstream) supports both `recv()` and `for await...of`.


Parameters


`intervalMs` number Milliseconds between metric snapshots.


Returns


[Promise<MetricsStream>](https://docs.microsandbox.dev/sdk/typescript/sandbox#metricsstream) Async stream yielding a snapshot each interval.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-requestdrain) sandbox. requestDrain()


Local-only


```
requestDrain(): Promise<void>
```


Example


```
await sandbox.requestDrain();
await sandbox.waitUntilStopped();
```


Request a graceful drain and return once the request is sent. Existing commands run to completion, but new `exec` calls are rejected. The sandbox transitions to `stopped` when all in-flight commands finish. Use [`waitUntilStopped()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-waituntilstopped) when the caller needs stopped-state observation. Useful for zero-downtime rotation of worker sandboxes.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-requestkill) sandbox. requestKill()


Local-only


```
requestKill(): Promise<void>
```


Example


```
await sandbox.requestKill();
```


Request force termination and return once the signal is sent, without waiting for the stopped state to be observed.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-requeststop) sandbox. requestStop()


```
requestStop(): Promise<void>
```


Example


```
await sandbox.requestStop();
```


Request graceful shutdown and return once the request is sent, without waiting for the stopped state to be observed.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-ssh) sandbox. ssh()


```
ssh(): SandboxSshOps
```


Get an SSH handle for opening interactive sessions and port forwards into the running guest. See [SSH](https://docs.microsandbox.dev/sdk/typescript/ssh) for API details.


Returns


[SandboxSshOps](https://docs.microsandbox.dev/sdk/typescript/ssh) SSH handle.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-stop) sandbox. stop()


Different on cloud


```
stop(): Promise<void>
```


Example


```
await sandbox.stop();
```


Wait indefinitely for graceful shutdown and release of the targeted runtime’s ownership. Success allows immediate removal without racing teardown. No implicit kill is requested. Paused or unreachable sandboxes return errors; resume or kill explicitly. Ignoring a Promise does not cancel its operation.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-waitforstatus) sandbox. waitForStatus()


```
waitForStatus(status: SandboxStatus): Promise<SandboxHandle>
```


Wait without a built-in timeout until this exact persisted sandbox reaches `status`. Returns a refreshed metadata handle and throws `SandboxReplacedError` rather than following a reused name. Use `Promise.race` when the caller needs its own deadline; the underlying wait is not cancellable yet.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-restart) sandbox. restart()


```
restart(options?: { force?: boolean; timeoutMs?: number; detached?: boolean }): Promise<Sandbox>
```


Restart this exact sandbox. Defaults to graceful shutdown, a 10_000 ms timeout, and attached local start. A stopped, crashed, or created sandbox starts directly; `Starting` is observed until it settles. Set `force` to kill, `timeoutMs` to change how long shutdown can take, or `detached` for a local background start.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-destroy) sandbox. destroy()


```
destroy(options?: { force?: boolean; timeoutMs?: number }): Promise<void>
```


Stop and remove this exact sandbox. Defaults to graceful shutdown with a 10_000 ms timeout. Identity checks throw `SandboxReplacedError` instead of deleting a replacement that reused the name.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-stopwithtimeout) sandbox. stopWithTimeout()


Different on cloud


```
stopWithTimeout(timeoutMs: number): Promise<void>
```


Example


```
await sandbox.stopWithTimeout(5000);
```


Apply one total budget to graceful dispatch and completion. Expiry throws `StopTimeoutError` without killing; `0` expires before dispatch. A delivered request can complete later. Only explicit `kill()` requests force termination.


Parameters


`timeoutMs` number Total graceful-completion budget, as an integer from 0 to 4294967295 milliseconds. Zero expires before dispatch.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-waituntilstopped) sandbox. waitUntilStopped()


```
waitUntilStopped(): Promise<SandboxStopResult>
```


Example


```
const result = await sandbox.waitUntilStopped();
console.log(result.status, result.exitCode);
```


Block until the sandbox is observed in a terminal non-running state, without triggering a stop or kill request.


Returns


[Promise<SandboxStopResult>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstopresult) Terminal status, exit code, and signal that were observed.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-symbol-asyncdispose) sandbox. [Symbol.asyncDispose](https://docs.microsandbox.dev/sdk/typescript/sandbox)


Limited on cloud


```
[Symbol.asyncDispose](): Promise<void>
```


Example


```
{
  await using sandbox = await Sandbox.builder("api").image("python").create();
  await sandbox.exec("python", ["-V"]);
} // sandbox.stop() runs here, automatically
```


Implements `AsyncDisposable` so the sandbox can be used with `await using`. When the binding goes out of scope, the sandbox is stopped (best-effort) - but only if `ownsLifecycle` is `true`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-restorewarnings) sandbox. restoreWarnings()


```
restoreWarnings(): Promise<ExternalMountWarning[]>
```


Return warnings for unavailable external filesystems and accepted restore mismatches. See [External mounts](https://docs.microsandbox.dev/sandboxes/snapshots#external-mounts) for restore options.
Each `ExternalMountWarning` contains:


| Field | Type | Description |
| --- | --- | --- |
| `guestPath` | `string` | Guest-visible mount path. |
| `reason` | `string` | Why the resource could not be reconstructed. |
| `staleInodes` | `readonly bigint[]` | Permanently invalid captured node IDs; empty when the whole export is unavailable. |


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder) SandboxBuilder


Fluent builder for configuring a sandbox before creation. Obtained via [`Sandbox.builder(name)`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-builder). Every setter returns the same builder so calls chain. Examples are shown on the methods where usage is non-obvious.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-build) sandboxBuilder. build()


```
build(): Promise<SandboxConfig>
```


Materialize the [`SandboxConfig`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig) without booting the sandbox. Validates the configuration and consumes the builder. For booting, use [`create`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-create) instead - it builds internally.


Returns


[Promise<SandboxConfig>](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig) Validated, ready-to-boot configuration.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-cpus) sandboxBuilder. cpus()


```
cpus(n: number): this
```


Set the number of virtual CPUs. This is a limit, not a reservation.


Parameters


`n` number Number of vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-maxcpus) sandboxBuilder. maxCpus()


Local-only


```
maxCpus(n: number): this
```


Set the boot-time maximum possible virtual CPU capacity. This reserves the envelope a sandbox can use after restart-backed changes and future live CPU activation; it does not increase the effective vCPU count by itself.


Parameters


`n` number Maximum possible vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-create) sandboxBuilder. create()


```
create(): Promise<Sandbox>
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .image("python")
  .detached(true)
  .create();
await sandbox.detach();
```


Build and boot the sandbox. By default, a local handle is attached and stops when its `await using` binding goes out of scope. A cloud handle does not own the service-managed VM, so stop or remove it explicitly. Call [`detached(true)`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-detached) first for local background mode.


Returns


[Promise<Sandbox>](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-connectorcreate) sandboxBuilder. connectOrCreate()


```
connectOrCreate(): Promise<Sandbox>
```


Reuse or create the sandbox with this name. The method connects when it is running, waits while it is starting, starts it when it is created, stopped, or crashed, and creates it only when the name is unused. Builder settings apply only to a new sandbox. Concurrent callers reuse the same sandbox. Calling [`replace()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-replace) or [`replaceWithTimeout()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-replacewithtimeout) on this builder is invalid.


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-createwithpullprogress) sandboxBuilder. createWithPullProgress()


Limited on cloud


```
createWithPullProgress(): Promise<PullProgressCreate>
```


Example


```
const creation = await Sandbox.builder("demo")
  .image("alpine")
  .createWithPullProgress();

for await (const ev of creation) {
  if (ev.kind === "layerDownloadProgress") {
    console.log(`${ev.layerIndex}: ${ev.downloadedBytes}/${ev.totalBytes}`);
  }
}

const sandbox = await creation.awaitSandbox();
```


Build and boot while streaming image pull progress. Returns a [`PullProgressCreate`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogresscreate) that yields [`PullProgress`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogress) events as the image is resolved, downloaded, and materialized; call `awaitSandbox()` after iteration to obtain the live sandbox.


Returns


[Promise<PullProgressCreate>](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogresscreate) Async iterable creation handle.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-detached) sandboxBuilder. detached()


```
detached(enabled: boolean): this
```


Create in detached/background mode when `true`. A detached sandbox survives after your process exits and does not auto-stop on `await using` scope exit.


Parameters


`enabled` boolean Whether to boot in detached mode.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-disablemetricssample) sandboxBuilder. disableMetricsSample()


Local-only


```
disableMetricsSample(): this
```


Disable periodic background metrics sampling for this sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-disablenetwork) sandboxBuilder. disableNetwork()


```
disableNetwork(): this
```


Fully disable networking. No network interface is created.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-entrypoint) sandboxBuilder. entrypoint()


```
entrypoint(cmd: string[]): this
```


Override the image ENTRYPOINT used by default-workload execution. [`sandbox.execDefault`](https://docs.microsandbox.dev/sdk/typescript/execution) combines it with the effective CMD. Literal [`sandbox.exec`](https://docs.microsandbox.dev/sdk/typescript/execution), [`sandbox.attach`](https://docs.microsandbox.dev/sdk/typescript/execution), and [`sandbox.shell`](https://docs.microsandbox.dev/sdk/typescript/execution) calls ignore it.


Parameters


`cmd` string[] Entrypoint command and arguments.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-env) sandboxBuilder. env()


```
env(key: string, value: string): this
```


Set an environment variable visible to all commands. Can be called multiple times. Per-command env vars (via `execWith`) are merged on top.


Parameters


`key` string Variable name. `value` string Variable value.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-envs) sandboxBuilder. envs()


```
envs(vars: Record<string, string>): this
```


Add many environment variables at once.


Parameters


`vars` Record<string, string> Map of variable names to values.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-ephemeral) sandboxBuilder. ephemeral()


```
ephemeral(enabled: boolean): this
```


When `true`, the sandbox and all its persisted state are removed automatically once it stops, rather than left on disk for restart.


Parameters


`enabled` boolean Whether the sandbox is ephemeral.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-hostname) sandboxBuilder. hostname()


Local-only


```
hostname(name: string): this
```


Set the guest hostname.


Parameters


`name` string Hostname.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-libkrunfwpath) sandboxBuilder. libkrunfwPath()


```
libkrunfwPath(path: string): this
```


Deprecated compatibility alias for older builder chains. This sets the same process-level override as `setRuntimeLibkrunfwPath(path)` and returns the builder; it is not a per-sandbox setting.


Parameters


`path` string Path to the libkrunfw shared library.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-idletimeout) sandboxBuilder. idleTimeout()


```
idleTimeout(secs: number): this
```


Auto-drain the sandbox after this many seconds of inactivity (no active exec sessions). Enforced on the host side.


Parameters


`secs` number Idle timeout in seconds.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-image) sandboxBuilder. image()


Limited on cloud


```
image(src: string): this
```


Set the root filesystem source. Accepts OCI image names (`"alpine"`), local directory paths, or disk image paths. The format is auto-detected. **Required** for creation; use `Sandbox.restore()` for snapshots.


Parameters


`src` string OCI image name, local directory path, or disk image path.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-imagewith) sandboxBuilder. imageWith()


Limited on cloud


```
imageWith(configure: (b: ImageBuilder) => ImageBuilder): this
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .imageWith((i) => i.oci("python:3.12").rootDisk(8192))
  .create();
```


Configure an explicit rootfs source. Use this for OCI-only settings such as the writable root disk, or for disk images when the filesystem type can’t be auto-detected.


Parameters


`configure` (b: ImageBuilder) => ImageBuilder Configure the rootfs source.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-cmd) sandboxBuilder. cmd()


```
cmd(cmd: string[]): this
```


Override the image CMD used by default-workload execution. An empty array explicitly clears the image CMD. This describes durable configuration and does not execute anything during `create()`.


```
const sandbox = await Sandbox.builder("worker")
  .image("example/worker:latest")
  .cmd(["worker.py", "--once"])
  .create();
```


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-init) sandboxBuilder. init()


```
init(cmd: string, args?: string[]): this
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .image("jrei/systemd-debian:12")
  .init("auto")
  .create();
```


Hand off PID 1 inside the guest to `cmd` after agentd finishes its boot-time setup. `cmd` is either an absolute path inside the guest rootfs or the literal `"auto"`, which honors a known image ENTRYPOINT init then falls back to probing common init paths. See [Custom init system](https://docs.microsandbox.dev/sandboxes/bootstrap#custom-init-system). For init binaries that need extra env, use [`initWith`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-initwith).


Parameters


`cmd` string Absolute path inside the guest, or `“auto”`. `args` string[]? Optional argv for the init binary.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-initwith) sandboxBuilder. initWith()


```
initWith(cmd: string, configure: (b: InitOptionsBuilder) => InitOptionsBuilder): this
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .image("jrei/systemd-debian:12")
  .initWith("/lib/systemd/systemd", (i) =>
    i.args(["--unit=multi-user.target"]).env("container", "microsandbox"))
  .create();
```


Like [`init`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-init), but with a closure-builder for argv and env vars. The builder exposes `.arg`, `.args`, `.env`, and `.envs`. Calling `init` or `initWith` more than once overwrites.


Parameters


`cmd` string Absolute path to the init binary inside the guest. `configure` (b: InitOptionsBuilder) => InitOptionsBuilder Closure populating argv and env.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-label) sandboxBuilder. label()


```
label(key: string, value: string): this
```


Attach a single label to the sandbox. Labels can be matched later with [`Sandbox.listWith()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-listwith).


Parameters


`key` string Label key. `value` string Label value.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-labels) sandboxBuilder. labels()


```
labels(labels: Record<string, string>): this
```


Attach many labels at once.


Parameters


`labels` Record<string, string> Map of label keys to values.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-loglevel) sandboxBuilder. logLevel()


```
logLevel(level: LogLevel): this
```


Override the sandbox process’s log verbosity.


Parameters


`level` [LogLevel](https://docs.microsandbox.dev/sdk/typescript/sandbox#loglevel) Log level.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-maxduration) sandboxBuilder. maxDuration()


```
maxDuration(secs: number): this
```


Set the maximum sandbox lifetime in seconds. When exceeded, the sandbox is drained and stopped. Enforced on the host side - the guest cannot override it.


Parameters


`secs` number Maximum lifetime in seconds.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-memory) sandboxBuilder. memory()


```
memory(mib: number): this
```


Set the guest memory size in MiB. Physical pages are only allocated as the guest touches them, so this is a limit, not an upfront reservation.


Parameters


`mib` number Memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-maxmemory) sandboxBuilder. maxMemory()


Local-only


```
maxMemory(mib: number): this
```


Set the boot-time maximum hotpluggable guest memory in MiB. This reserves the envelope a sandbox can use after restart-backed changes and future live memory activation; it does not increase the effective memory by itself.


Parameters


`mib` number Maximum memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-thp) sandboxBuilder. thp()


```
thp(policy: "always" | "madvise" | "never"): this
```


Select the guest transparent huge-page policy applied through the kernel command line at boot. Default: `"madvise"`.


Parameters


`policy`”always” | “madvise” | “never” The THP policy persisted for the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-metricssampleintervalms) sandboxBuilder. metricsSampleIntervalMs()


Local-only


```
metricsSampleIntervalMs(ms: number): this
```


Set the interval, in milliseconds, at which the host samples background metrics for this sandbox.


Parameters


`ms` number Sampling interval in milliseconds.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-intercepttls) sandboxBuilder. interceptTls()


```
interceptTls(): this
```


Enable [TLS interception](https://docs.microsandbox.dev/networking/tls) for a local sandbox. Existing network and TLS settings are preserved. Later `network()` callbacks preserve settings unless explicitly changed. Calling `tls()` inside the callback replaces the TLS settings.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-network) sandboxBuilder. network()


```
network(configure: (b: NetworkBuilder) => NetworkBuilder): this
```


Configure DNS, TLS, policy, and secrets. See [Networking](https://docs.microsandbox.dev/sdk/typescript/networking) for the full builder API.


Parameters


`configure` [(b: NetworkBuilder) => NetworkBuilder](https://docs.microsandbox.dev/sdk/typescript/networking) Configure the network.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-proxy) sandboxBuilder. proxy()


```
proxy(configure: (proxy: OutboundProxyBuilder) => HttpConnectProxyBuilder | Socks4ProxyBuilder | Socks5ProxyBuilder): this
```


Configure the single proxy used for outbound sandbox connections. See [Proxies](https://docs.microsandbox.dev/sdk/typescript/proxies) for the protocol builders and examples.


Parameters


`configure` function Callback that selects and configures one proxy protocol.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-patch) sandboxBuilder. patch()


```
patch(configure: (b: PatchBuilder) => PatchBuilder): this
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .image("python")
  .patch((p) => p.text("/etc/app.conf", "mode=prod\n", { mode: 0o644 }))
  .create();
```


Modify the rootfs before the VM boots. Patches go into the writable layer - the base image is untouched. See [`PatchBuilder`](https://docs.microsandbox.dev/sdk/typescript/sandbox#patchbuilder) for the operations.


Parameters


`configure` [(b: PatchBuilder) => PatchBuilder](https://docs.microsandbox.dev/sdk/typescript/sandbox#patchbuilder) Configure rootfs patches.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-port) sandboxBuilder. port()


Local-only


```
port(host: number, guest: number): this
```


Publish a TCP port from the sandbox to the host. The default host bind address is `127.0.0.1`. For an explicit bind address, use [`portBind`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-portbind).


Parameters


`host` number Port on the host. `guest` number Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-portbind) sandboxBuilder. portBind()


Local-only


```
portBind(bind: string, host: number, guest: number): this
```


Publish a TCP port on a specific host bind address, such as `"0.0.0.0"`.


Parameters


`bind` string Host bind address. `host` number Port on the host. `guest` number Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-portudp) sandboxBuilder. portUdp()


Local-only


```
portUdp(host: number, guest: number): this
```


Publish a UDP port. The default host bind address is `127.0.0.1`.


Parameters


`host` number Port on the host. `guest` number Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-portudpbind) sandboxBuilder. portUdpBind()


Local-only


```
portUdpBind(bind: string, host: number, guest: number): this
```


Publish a UDP port on a specific host bind address.


Parameters


`bind` string Host bind address. `host` number Port on the host. `guest` number Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-pullpolicy) sandboxBuilder. pullPolicy()


```
pullPolicy(policy: PullPolicy): this
```


Control when the OCI image is pulled from the registry.


Parameters


`policy` [PullPolicy](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullpolicy) Pull behavior.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-quietlogs) sandboxBuilder. quietLogs()


```
quietLogs(): this
```


Suppress sandbox process log output.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-registry) sandboxBuilder. registry()


Limited on cloud


```
registry(configure: (b: RegistryConfigBuilder) => RegistryConfigBuilder): this
```


Example


```
const sandbox = await Sandbox.builder("worker")
  .image("registry.internal/app:latest")
  .registry((r) =>
    r.auth({ kind: "basic", username: "user", password: "token" }),
  )
  .create();
```


Configure the OCI registry connection: authentication, insecure transport, and CA certificates.


Parameters


`configure` [(b: RegistryConfigBuilder) => RegistryConfigBuilder](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfigbuilder) Configure registry authentication, transport, and CA certificates.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-replace) sandboxBuilder. replace()


Local-only


```
replace(): this
```


If a sandbox with the same name already exists, stop it (10s SIGTERM grace, then SIGKILL), remove it, and create a fresh one. Without this, creation fails on name conflict.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-replacewithtimeout) sandboxBuilder. replaceWithTimeout()


Local-only


```
replaceWithTimeout(timeoutMs: number): this
```


Same as [`replace()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-replace) with a custom SIGTERM timeout in milliseconds. `0` skips SIGTERM and force-kills immediately. Implies `replace()`.


Parameters


`timeoutMs` number Milliseconds to wait after SIGTERM before escalating to SIGKILL.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-rlimit) sandboxBuilder. rlimit()


```
rlimit(resource: string, limit: number): this
```


Set a guest resource limit (a soft and hard limit at the same value). For separate soft/hard values, use [`rlimitRange`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-rlimitrange).


Parameters


`resource` string Resource name, e.g. `“nofile”`. `limit` number Limit value applied to both soft and hard.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-rlimitrange) sandboxBuilder. rlimitRange()


```
rlimitRange(resource: string, soft: number, hard: number): this
```


Set a guest resource limit with explicit soft and hard values.


Parameters


`resource` string Resource name, e.g. `“nofile”`. `soft` number Soft limit. `hard` number Hard limit.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-script) sandboxBuilder. script()


```
script(name: string, content: string): this
```


Add a named script at `/.msb/scripts/` inside the guest. Scripts are added to `PATH` and can be called by name via `exec()` or `shell()`.


Parameters


`name` string Script name (becomes the filename). `content` string Script content.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-scripts) sandboxBuilder. scripts()


```
scripts(scripts: Record<string, string>): this
```


Add many named scripts at once.


Parameters


`scripts` Record<string, string> Map of script names to contents.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-security) sandboxBuilder. security()


```
security(profile: "default" | "restricted"): this
```


Set the in-guest security profile.


Parameters


`profile`”default” | “restricted” Security profile.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-secret) sandboxBuilder. secret()


```
secret(configure: (b: SecretBuilder) => SecretBuilder): this
```


Add a secret with full configuration. See [Secrets](https://docs.microsandbox.dev/sdk/typescript/secrets) for the builder API. Automatically enables TLS interception.


Parameters


`configure` [(b: SecretBuilder) => SecretBuilder](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) Configure the secret.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-secretenv) sandboxBuilder. secretEnv()


```
secretEnv(envVar: string, value: string, allowedHost: string): this
```


Auto-placeholder shorthand for adding a header-injected secret. Generates a `$MSB_<env_var>` placeholder usable in headers.


Parameters


`envVar` string Environment variable name (non-empty, no `=` or NUL). `value` string Secret value. `allowedHost` string Allowed destination host.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-shell) sandboxBuilder. shell()


```
shell(shell: string): this
```


Set the shell binary used by [`sandbox.shell()`](https://docs.microsandbox.dev/sdk/typescript/execution).


Parameters


`shell` string Shell path (e.g. `“/bin/bash”`).


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-user) sandboxBuilder. user()


```
user(user: string): this
```


Set the default guest user for all commands.


Parameters


`user` string User name or UID.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-volume) sandboxBuilder. volume()


```
volume(guest: string, configure: (b: MountBuilder) => MountBuilder): this
```


Add a volume mount. See [Volumes](https://docs.microsandbox.dev/sdk/typescript/volumes) for mount types.


Parameters


`guest` string Mount point inside the sandbox. `configure` [(b: MountBuilder) => MountBuilder](https://docs.microsandbox.dev/sdk/typescript/volumes) Configure the mount.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-workdir) sandboxBuilder. workdir()


```
workdir(path: string): this
```


Set the default working directory for all commands.


Parameters


`path` string Absolute path inside the guest.


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patchbuilder) PatchBuilder


Builder for pre-boot root filesystem patches.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-append) patch. append()


```
append(path: string, content: string): this
```


Append `content` to an existing file at `path`. If the file lives in a lower image layer, it’s copied up first.


Parameters


`path` string Absolute path inside the guest. `content` string Text to append.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-copydir) patch. copyDir()


Limited on cloud


```
copyDir(src: string, dst: string, opts?: { replace?: boolean }): this
```


Recursively copy a host directory at `src` into the guest rootfs at `dst`.


Parameters


`src` string Host source directory. `dst` string Absolute destination path inside the guest. `opts.replace` boolean When `true`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-copyfile) patch. copyFile()


Limited on cloud


```
copyFile(src: string, dst: string, opts?: { mode?: number; replace?: boolean }): this
```


Copy a single host file at `src` into the guest rootfs at `dst`.


Parameters


`src` string Host source file. `dst` string Absolute destination path inside the guest. `opts.mode` number File mode, e.g. `0o644`. Omit to keep the source mode. `opts.replace` boolean When `true`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-file) patch. file()


```
file(path: string, content: Buffer, opts?: { mode?: number; replace?: boolean }): this
```


Write raw bytes at `path`.


Parameters


`path` string Absolute path inside the guest. `content` Buffer Raw byte content. `opts.mode` number File mode, e.g. `0o644`. `opts.replace` boolean When `true`, overwrite an existing path.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-mkdir) patch. mkdir()


```
mkdir(path: string, opts?: { mode?: number }): this
```


Create a directory at `path`. Idempotent: a no-op if the directory already exists.


Parameters


`path` string Absolute path inside the guest. `opts.mode` number Directory mode, e.g. `0o755`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-remove) patch. remove()


```
remove(path: string): this
```


Delete a file or directory at `path`. Idempotent: a no-op if the path doesn’t exist.


Parameters


`path` string Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-symlink) patch. symlink()


```
symlink(target: string, link: string, opts?: { replace?: boolean }): this
```


Create a symlink at `link` pointing to `target`.


Parameters


`target` string What the symlink points to (literal symlink target text). `link` string Absolute path of the symlink itself. `opts.replace` boolean When `true`, overwrite an existing path at `link`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#patch-text) patch. text()


```
text(path: string, content: string, opts?: { mode?: number; replace?: boolean }): this
```


Write UTF-8 text content at `path`.


Parameters


`path` string Absolute path inside the guest. `content` string Text content. `opts.mode` number File mode, e.g. `0o644`. `opts.replace` boolean When `true`, overwrite an existing path.


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) LogEntry


Returned by [logs()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logs) · [logStream()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logstream)


A class wrapping one captured log entry from `exec.log`. Bytes are exposed via `data`; use `text()` for a UTF-8-lossy decode.


| Field | Type | Description |
| --- | --- | --- |
| `timestamp` | `Date` | Wall-clock capture time on the host |
| `source` | [`LogSource`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logsource) | Where the chunk came from |
| `sessionId` | `number | null` | Relay-monotonic session id; `null` for `"system"` entries |
| `data` | `Uint8Array` | The captured chunk’s bytes (UTF-8 lossy decoded by default) |
| `cursor` | `string` | Opaque resume token; pass to [`LogStreamOptions.fromCursor`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstreamoptions) to resume |


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#entry-text) entry. text()


```
text()
```


Convenience: UTF-8 decode of `data` (lossy - invalid bytes are replaced)


Returns


`string`


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstream) LogStream


Returned by [logStream()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logstream)


An async iterable of [`LogEntry`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) values. Drain it with `for await...of` or call `recv()` directly. Implements `AsyncDisposable`, so it works with `await using`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstream-recv) logStream. recv()


```
recv()
```


Receive the next entry. Returns `null` when the stream ends.


Returns


`Promise<` [`LogEntry`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) ` \| null>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#stream-symbol-asynciterator) stream. [Symbol.asyncIterator](https://docs.microsandbox.dev/sdk/typescript/sandbox)


```
[Symbol.asyncIterator]()
```


Use with `for await...of`


Returns


`AsyncIterator<` [`LogEntry`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#stream-symbol-asyncdispose) stream. [Symbol.asyncDispose](https://docs.microsandbox.dev/sdk/typescript/sandbox)


```
[Symbol.asyncDispose]()
```


Stop iterating; safe to use with `await using`


Returns


`Promise<void>`


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#metricsstream) MetricsStream


Returned by [metricsStream()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-metricsstream)


Async stream for receiving periodic metrics snapshots. Implements `AsyncDisposable`, so it works with `await using`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#metricsstream-recv) metricsStream. recv()


```
recv()
```


Receive the next snapshot. Returns `null` when the stream ends.


Returns


`Promise<` [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) ` \| null>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#stream-symbol-asynciterator-2) stream. [Symbol.asyncIterator](https://docs.microsandbox.dev/sdk/typescript/sandbox)


```
[Symbol.asyncIterator]()
```


Use with `for await...of`


Returns


`AsyncIterator<` [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#stream-symbol-asyncdispose-2) stream. [Symbol.asyncDispose](https://docs.microsandbox.dev/sdk/typescript/sandbox)


```
[Symbol.asyncDispose]()
```


Stop iterating; safe to use with `await using`


Returns


`Promise<void>`


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogresscreate) PullProgressCreate


Returned by [createWithPullProgress()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-createwithpullprogress)


Async iterable creation handle returned by [`createWithPullProgress()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-createwithpullprogress). Yields [`PullProgress`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogress) events as the image is resolved, downloaded, and materialized. Call `awaitSandbox()` after iteration to obtain the live sandbox.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pull-progress) pull. progress


`NapiPullProgressStream`
The underlying progress event stream


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pull-awaitsandbox) pull. awaitSandbox()


```
awaitSandbox()
```


Resolve the underlying creation task and return the running sandbox


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pull-symbol-asynciterator) pull. [Symbol.asyncIterator](https://docs.microsandbox.dev/sdk/typescript/sandbox)


```
[Symbol.asyncIterator]()
```


Use with `for await...of`


Returns


`AsyncIterator<` [`PullProgress`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogress) `>`


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxlistbuilder) SandboxListBuilder


Fluent configuration passed to [`Sandbox.listWith()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-listwith). Keep the labels and limit unchanged when continuing with a cursor.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#list-limit) list. limit()


```
limit(n)
```


Set a page size from 1 through 100


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#list-cursor) list. cursor()


```
cursor(cursor)
```


Continue after a previous page’s `nextCursor`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#list-label) list. label()


```
label(key, value)
```


Require one label; repeated calls are AND-matched


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#list-labels) list. labels()


```
labels(record)
```


Add several AND-matched labels


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxhandle) SandboxHandle


Returned by [Sandbox.get()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-get) · [Sandbox.list()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-list) · [Sandbox.listWith()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-listwith)


A metadata and lifecycle handle for an existing sandbox.


| Field | Type | Description |
| --- | --- | --- |
| `name` | `string` | Sandbox name, up to 128 UTF-8 bytes |
| `id` | `string` | Opaque stable identity captured by this handle. Receiver lifecycle methods remain bound to this value and throw `SandboxReplacedError` if the reusable name now points to another sandbox. |
| `status` | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstatus) | Current status |
| `configJson` | `string` | Raw JSON configuration |
| `createdAt` | `Date | null` | Creation timestamp |
| `updatedAt` | `Date | null` | Last update timestamp |


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-config) handle. config()


Local-only


```
config()
```


Parsed configuration


Returns


[`SandboxConfig`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig)


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-refresh) handle. refresh()


```
refresh()
```


Re-read the handle’s state from the database


Returns


`Promise<` [`SandboxHandle`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxhandle) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-ping) handle. ping()


Local-only


```
ping()
```


Check agent reachability without refreshing idle activity; does not start stopped sandboxes


Returns


`Promise<` [`SandboxPingResult`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxpingresult) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-touch) handle. touch()


Local-only


```
touch()
```


Explicitly refresh idle activity; does not start stopped sandboxes


Returns


`Promise<` [`SandboxTouchResult`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxtouchresult) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-modify) handle. modify()


Local-only


```
modify(opts?)
```


Plan or apply a configuration change; same options as [`modify()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-modify). Does not start stopped sandboxes; changes persist for the next boot


Returns


`Promise<` [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmodificationplan) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-metrics) handle. metrics()


Local-only


```
metrics()
```


Point-in-time resource metrics


Returns


`Promise<` [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-logs) handle. logs()


Local-only


```
logs()
```


Read captured `exec.log` (works without starting)


Returns


`Promise<` [`LogEntry`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) `[]>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-logstream) handle. logStream()


```
logStream()
```


Stream captured `exec.log`, with optional follow


Returns


`Promise<` [`LogStream`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstream) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-start) handle. start()


```
start()
```


Start in attached mode


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-startdetached) handle. startDetached()


```
startDetached()
```


Start in detached mode


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-connect) handle. connect()


```
connect()
```


Connect to a running sandbox without taking ownership. Returns an error if it doesn’t respond within 10_000 ms


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-connectwithtimeout) handle. connectWithTimeout()


```
connectWithTimeout(timeoutMs)
```


Same as `connect()` with an explicit timeout in milliseconds


Returns


`Promise<` [`Sandbox`](https://docs.microsandbox.dev/sdk/typescript/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-connectorstart) handle. connectOrStart()


```
connectOrStart(options?: { detached?: boolean }): Promise<Sandbox>
```


Connect when this exact sandbox is running, wait through `starting`, or start it when it is `created`, `stopped`, or `crashed`. `draining` and `paused` are rejected. Set `detached` only to make a required local start run in the background; connecting to an already-running sandbox does not change ownership.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-waitforstatus) handle. waitForStatus()


```
waitForStatus(status: SandboxStatus): Promise<SandboxHandle>
```


Wait without a built-in timeout until this exact sandbox reaches `status`, returning a refreshed handle. Throws `SandboxReplacedError` rather than rebinding to a replacement.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-restart) handle. restart()


```
restart(options?: { force?: boolean; timeoutMs?: number; detached?: boolean }): Promise<Sandbox>
```


Restart this exact sandbox with the same state and option semantics as [`sandbox.restart()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-restart).


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-destroy) handle. destroy()


```
destroy(options?: { force?: boolean; timeoutMs?: number }): Promise<void>
```


Stop and remove this exact sandbox. A stale handle cannot destroy a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-stop) handle. stop()


Different on cloud


```
stop()
```


Wait indefinitely for graceful completion and release of the targeted runtime’s ownership. Never implicitly kills.


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-stopwithtimeout) handle. stopWithTimeout()


Different on cloud


```
stopWithTimeout(timeoutMs)
```


Same completion contract as `stop()` under one total milliseconds budget. Expiry throws `StopTimeoutError` without killing; zero expires before dispatch.


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-requeststop) handle. requestStop()


```
requestStop()
```


Request graceful shutdown without waiting


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-kill) handle. kill()


Local-only


```
kill()
```


Force terminate and wait until stopped state is observed


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-killwithtimeout) handle. killWithTimeout()


Local-only


```
killWithTimeout(timeoutMs)
```


Same as `kill()` with an explicit observation timeout


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-requestkill) handle. requestKill()


Local-only


```
requestKill()
```


Request force termination without waiting


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-requestdrain) handle. requestDrain()


Local-only


```
requestDrain()
```


Request graceful drain without waiting


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-waituntilstopped) handle. waitUntilStopped()


```
waitUntilStopped()
```


Block until the sandbox reaches terminal state


Returns


`Promise<` [`SandboxStopResult`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstopresult) `>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-remove) handle. remove()


```
remove()
```


Delete sandbox and state


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#handle-snapshot) handle. snapshot()


Limited on cloud


```
snapshot(name)
```


Capture a disk snapshot. Locally, the name selects a member within the sandbox’s snapshot group. See [Snapshots](https://docs.microsandbox.dev/sdk/typescript/snapshots).


Returns


`Promise<Snapshot>`


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfigbuilder) RegistryConfigBuilder


Fluent builder for OCI registry connection settings. Obtain it through [`SandboxBuilder.registry()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-registry); the callback’s returned builder is stored in the sandbox configuration.


```
.registry((r) =>
  r.auth({ kind: "basic", username: "user", password: "token" })
    .caCertsPath("/etc/company-registry-ca.pem"),
)
```


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registry-auth) registry. auth()


```
auth(auth: RegistryAuth): this
```


Set registry authentication credentials.


Returns


`this`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registry-insecure) registry. insecure()


```
insecure(): this
```


Use plain HTTP instead of TLS.


Returns


`this`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registry-cacerts) registry. caCerts()


```
caCerts(pemData: Buffer): this
```


Add a PEM-encoded CA certificate. May be called repeatedly.


Returns


`this`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registry-cacertspath) registry. caCertsPath()


```
caCertsPath(path: string): this
```


Read and add a PEM-encoded CA certificate from a filesystem path.


Returns


`this`


#### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registry-build) registry. build()


```
build(): RegistryConfig
```


Snapshot the accumulated registry configuration.


Returns


[`RegistryConfig`](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfig)


## [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#types) Types


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#loglevel) LogLevel


Used by [logLevel()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-loglevel)


Sandbox process log verbosity. String literal type.


| Value | Description |
| --- | --- |
| `"error"` | Errors only |
| `"warn"` | Warnings and errors only |
| `"info"` | Info and higher |
| `"debug"` | Debug and higher |
| `"trace"` | Most verbose - all diagnostic output |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logreadoptions) LogReadOptions


Used by [logs()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logs)


Filters passed to [`logs()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logs). All fields optional. Omit the argument entirely for the default sources (`stdout` + `stderr` + `output`).


| Field | Type | Description |
| --- | --- | --- |
| tail | `number?` | Show only the last N entries after other filters apply |
| since | `Date?` | Inclusive lower bound on entry timestamp |
| until | `Date?` | Exclusive upper bound on entry timestamp |
| sources | `ReadonlyArray<` [`LogSource`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logsource) ` | "all">?` | Sources to include. Omit = `["stdout", "stderr", "output"]`. Add `"system"` or pass `"all"` to merge runtime/kernel diagnostics. |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logstreamoptions) LogStreamOptions


Used by [logStream()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logstream)


Options passed to [`logStream()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-logstream). All fields optional. `since` and `fromCursor` are mutually exclusive - passing both rejects at the boundary.


| Field | Type | Description |
| --- | --- | --- |
| sources | `ReadonlyArray<` [`LogSource`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logsource) ` | "all">?` | Same shape as [`LogReadOptions.sources`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logreadoptions) |
| since | `Date?` | Start at the first entry whose timestamp is `>= since`. Mutually exclusive with `fromCursor`. |
| fromCursor | `string?` | Resume strictly after the entry whose [`LogEntry.cursor`](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) matches. Mutually exclusive with `since`. |
| until | `Date?` | Stop emitting at the first entry whose timestamp is `>= until` |
| follow | `boolean?` | When `true`, keep the stream open past current EOF and yield new entries as they are written. Defaults to `false`. |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#logsource) LogSource


Used by [LogEntry.source](https://docs.microsandbox.dev/sdk/typescript/sandbox#logentry) · [LogReadOptions.sources](https://docs.microsandbox.dev/sdk/typescript/sandbox#logreadoptions)


Tag indicating where a captured log entry came from. String literal type:


```
type LogSource = "stdout" | "stderr" | "output" | "system";
```


| Value | Description |
| --- | --- |
| `"stdout"` | Captured from a session’s stdout (pipe mode - streams stayed separated) |
| `"stderr"` | Captured from a session’s stderr (pipe mode) |
| `"output"` | Captured from a session running in PTY mode. PTY allocation merges stdout and stderr at the kernel level inside the guest, so they arrive as a single stream - tagged `"output"` rather than mislabeled as `"stdout"`. |
| `"system"` | Synthetic entry: lifecycle markers in `exec.log` plus runtime/kernel diagnostic lines merged in at read time when `"system"` is requested. |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#modifyoptions) ModifyOptions


Used by [modify()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-modify)


A requested sandbox modification. Omitted fields are left unchanged.


| Field | Type | Description |
| --- | --- | --- |
| cpus | `number` | Desired effective vCPU count. Live when within the booted `maxCpus` |
| maxCpus | `number` | Boot-time maximum possible vCPUs (restart-backed) |
| memory | `number` | Desired effective guest memory in MiB. Live when within the booted `maxMemory` |
| maxMemory | `number` | Boot-time maximum hotpluggable memory in MiB (restart-backed) |
| rootDiskSize | `number` | Desired root disk size in MiB. Managed and flat OCI disks are grow-only; applies on restart or next start |
| env | `Record<string, string>` | Environment variables to set for future execs |
| envRemove | `string[]` | Environment variable keys to remove |
| labels | `Record<string, string>` | Labels to set |
| labelsRemove | `string[]` | Label keys to remove |
| workdir | `string` | Working directory for future execs |
| secrets | `Record<string, SecretModifySpec>` | Desired secret specs keyed by stable secret name |
| secretsRemove | `string[]` | Secret names to remove explicitly |
| policy | `"no_restart" | "next_start" | "restart"` | `"no_restart"` (default) applies only changes that can complete without restarting; `"next_start"` persists changes for the next start without mutating a running VM; `"restart"` restarts if needed so restart-required changes become active now |
| dryRun | `boolean` | Compute the plan without applying anything. Defaults to `false` |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#secretmodifyspec) SecretModifySpec


Used by [modify()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-modify)


Desired state for one secret. `env`, `value`, and `store` are mutually exclusive sources. Omit all three to update only the placeholder or allowed hosts.


| Field | Type | Description |
| --- | --- | --- |
| env | `string` | Host environment variable to resolve when applying the modification |
| value | `string` | Raw secret value. Stored in the durable sandbox config until replaced by a source reference |
| store | `string` | Reserved for a host-side secret store reference; currently unsupported |
| placeholder | `string` | Explicit guest-visible placeholder. New secrets default to `$MSB_<NAME>` |
| allowedHosts | `string[]` | Desired allowed host patterns. A new secret requires at least one; an empty list leaves existing hosts unchanged |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullpolicy) PullPolicy


Used by [pullPolicy()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-pullpolicy)


Controls when the SDK fetches an OCI image from the registry. String literal type.


| Value | Description |
| --- | --- |
| `"always"` | Pull the image every time, even if cached locally |
| `"if-missing"` | Pull only if the image is not already cached. This is the default. |
| `"never"` | Never pull; fail if the image is not cached locally |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogress) PullProgress


Yielded by [PullProgressCreate](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogresscreate)


Image pull and materialize progress event emitted by [`PullProgressCreate`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullprogresscreate). A discriminated union. Narrow on `kind` to access variant-specific fields.


| `kind` value | Additional fields |
| --- | --- |
| `"resolving"` | `reference: string` |
| `"resolved"` | `reference: string`, `manifestDigest: string`, `layerCount: number`, `totalDownloadBytes?: number` |
| `"layerDownloadProgress"` | `layerIndex: number`, `digest: string`, `downloadedBytes: number`, `totalBytes?: number` |
| `"layerDownloadComplete"` | `layerIndex: number`, `digest: string`, `downloadedBytes: number` |
| `"layerDownloadVerifying"` | `layerIndex: number`, `digest: string` |
| `"layerMaterializeStarted"` | `layerIndex: number`, `diffId: string` |
| `"layerMaterializeProgress"` | `layerIndex: number`, `bytesRead: number`, `totalBytes: number` |
| `"layerMaterializeWriting"` | `layerIndex: number` |
| `"layerMaterializeComplete"` | `layerIndex: number`, `diffId: string` |
| `"stitchMergingTrees"` | `layerCount: number` |
| `"stitchWritingFsmeta"` | (none) |
| `"stitchWritingVmdk"` | (none) |
| `"stitchComplete"` | (none) |
| `"complete"` | `reference: string`, `layerCount: number` |


`totalDownloadBytes` and `totalBytes` on the `"resolved"` / `"layerDownloadProgress"` variants may be absent if the manifest omits sizes.


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryauth) RegistryAuth


Authentication used when pulling images from an OCI registry.


```
type RegistryAuth =
  | { kind: "anonymous" }
  | { kind: "basic"; username: string; password: string };
```


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfig) RegistryConfig


Built by [RegistryConfigBuilder](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfigbuilder) · stored in [SandboxConfig.registry](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig)


OCI registry connection settings produced by [`RegistryConfigBuilder.build()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfigbuilder).


| Field | Type | Description |
| --- | --- | --- |
| auth | [`RegistryAuth`](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryauth) ` | undefined` | Registry authentication, if configured. |
| insecure | `boolean` | Whether to use plain HTTP instead of TLS. |
| caCertsCount | `number` | Number of CA certificates added through `caCerts()` or `caCertsPath()`. |
| caCertsPath | `string | undefined` | Last CA certificate path passed to `caCertsPath()`, if any. |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxconfig) SandboxConfig


Returned by [config()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-config) · [build()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-build)


Configuration object produced by [`build()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxbuilder-build) and returned by [`config()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-config). You generally should not construct this by hand; use the builder.


| Field | Type | Description |
| --- | --- | --- |
| name | `string` | Sandbox name, up to 128 UTF-8 bytes |
| image | `RootfsSource` | OCI / bind / disk discriminated union |
| cpus | `number | null` | Virtual CPUs |
| maxCpus | `number | null` | Boot-time maximum possible virtual CPUs |
| memoryMib | `number | null` | Guest memory in MiB |
| maxMemoryMib | `number | null` | Boot-time maximum hotpluggable memory in MiB |
| logLevel | [`LogLevel`](https://docs.microsandbox.dev/sdk/typescript/sandbox#loglevel) ` | null` | Log verbosity |
| quietLogs | `boolean` | Suppress log output |
| workdir | `string | null` | Default working directory |
| shell | `string | null` | Shell binary |
| securityProfile | `"default" | "restricted"` | In-guest security profile |
| entrypoint | `string[] | null` | Override the image ENTRYPOINT used by default-workload execution |
| cmd | `string[] | null` | Override the image CMD used by default-workload execution; an empty array clears CMD |
| hostname | `string | null` | Guest hostname |
| user | `string | null` | Default guest user |
| env | `Array<readonly [string, string]>` | Environment variables |
| scripts | `Array<readonly [string, string]>` | Named scripts |
| mounts | `VolumeMount[]` | Volume mounts |
| patches | `Patch[]` | Rootfs modifications applied before boot |
| pullPolicy | [`PullPolicy`](https://docs.microsandbox.dev/sdk/typescript/sandbox#pullpolicy) ` | null` | Image pull behavior |
| replace | `boolean` | Replace existing sandbox with same name |
| replaceWithTimeoutMs | `number` | Milliseconds to wait after `SIGTERM` before escalating to `SIGKILL` (default `10000`; `0` skips `SIGTERM`) |
| maxDurationSecs | `number | null` | Maximum sandbox lifetime |
| idleTimeoutSecs | `number | null` | Stop after idle time |
| portsTcp | `Array<readonly [number, number]>` | TCP host→guest mappings |
| portsUdp | `Array<readonly [number, number]>` | UDP host→guest mappings |
| registry | [`RegistryConfig`](https://docs.microsandbox.dev/sdk/typescript/sandbox#registryconfig) ` | null` | Registry connection settings |
| network | `NetworkConfig | null` | Network configuration |
| disableNetwork | `boolean` | Disable networking entirely |
| secrets | `SecretEntry[]` | Secret entries (top-level) |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxpage) SandboxPage


One stable, newest-first page returned by [`Sandbox.list()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-list) or [`Sandbox.listWith()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-listwith).


| Property | Type | Description |
| --- | --- | --- |
| `sandboxes` | `SandboxHandle[]` | Handles in this page |
| `nextCursor` | `string | undefined` | Opaque continuation cursor, absent on the final page |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmodificationplan) SandboxModificationPlan


Returned by [modify()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-modify)


Dry-run or apply plan for a sandbox modification. Values never appear in a plan: secret entries carry only guest-visible references.


| Field | Type | Description |
| --- | --- | --- |
| sandbox | `string` | Sandbox being modified |
| status | `string` | Status used for classification (`"running"`, `"stopped"`, …) |
| applied | `boolean` | Whether the changes were applied; `false` for dry runs |
| policy | `"no_restart" | "next_start" | "restart"` | Policy used to produce the plan |
| changes | [`PlannedChange`](https://docs.microsandbox.dev/sdk/typescript/sandbox#plannedchange) `[]` | Planned changes, one entry per field or secret |
| conflicts | `{ field, message }[]` | Conflicts that must be resolved before the patch can apply |
| warnings | `{ field, message }[]` | Non-fatal warnings, e.g. the future-execs-only env caveat |
| resizeStatus | `ResourceResizeStatus[]` | Live resource resize outcomes, populated by apply when a live change ran (see below) |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#plannedchange) PlannedChange


Used by [SandboxModificationPlan.changes](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmodificationplan)


Discriminated union on `kind`. Both variants carry `field`, `change`, `disposition`, and `reason`.


| Variant | Type | Description |
| --- | --- | --- |
| `kind: "config"` | [`ConfigPlannedChange`](https://docs.microsandbox.dev/sdk/typescript/sandbox#configplannedchange) | Ordinary config change |
| `kind: "secret"` | [`SecretPlannedChange`](https://docs.microsandbox.dev/sdk/typescript/sandbox#secretplannedchange) | Secret change. Values are omitted by construction; references are guest-visible only |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#configplannedchange) ConfigPlannedChange


Variant of [PlannedChange](https://docs.microsandbox.dev/sdk/typescript/sandbox#plannedchange)


Ordinary configuration change in a modification plan.


| Field | Type | Description |
| --- | --- | --- |
| field | `string` | Config field being changed |
| change | `"added" | "updated" | "removed"` | Natural change type for table rendering |
| before | `string | null` | Previous safe visible state |
| after | `string | null` | New safe visible state |
| disposition | `"live" | "next start" | "requires restart" | "unsupported"` | When or whether the change can take effect |
| reason | `string | null` | Human-readable reason for the classification, when useful |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#secretplannedchange) SecretPlannedChange


Variant of [PlannedChange](https://docs.microsandbox.dev/sdk/typescript/sandbox#plannedchange)


Secret change in a modification plan. Values are omitted by construction; `beforeRef` and `afterRef` are guest-visible references.


| Field | Type | Description |
| --- | --- | --- |
| field | `string` | Always `"secret"` |
| name | `string` | Stable secret identity, usually the environment variable name |
| change | `"added" | "rotated" | "removed" | "renamed" | "hosts updated" | "placeholder updated"` | Natural change type for table rendering |
| beforeRef | `string | null` | Previous guest-visible reference or placeholder |
| afterRef | `string | null` | New guest-visible reference or placeholder |
| disposition | `"live" | "next start" | "requires restart" | "unsupported"` | When or whether the change can take effect |
| allowHosts | `string[]` | Allowed hosts after the requested change |
| reason | `string | null` | Human-readable reason for the classification, when useful |


`ResourceResizeStatus` reports runtime convergence for a live resize; enforcement applies immediately, the guest converges asynchronously:


| Field | Type | Description |
| --- | --- | --- |
| resource | `"cpus" | "memory"` | Resource being resized |
| requested | `string` | Requested value |
| actual | `string` | Actual value observed in the guest/runtime |
| enforced | `string` | Host/VMM-enforced value |
| state | `"accepted" | "converging" | "applied" | "guest-refused" | "failed"` | `"applied"` when requested, actual, and enforced match; `"converging"` while the guest is still onlining CPUs or plugging memory; `"guest-refused"` when the guest would not cooperate (the host enforces the new limit anyway) |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxpingresult) SandboxPingResult


Returned by [ping()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-ping)


Agent reachability result.


| Field | Type | Description |
| --- | --- | --- |
| name | `string` | Sandbox name |
| latencyMs | `number` | Round-trip latency in milliseconds |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxtouchresult) SandboxTouchResult


Returned by [touch()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-touch)


Explicit idle-refresh result.


| Field | Type | Description |
| --- | --- | --- |
| name | `string` | Sandbox name |
| activitySeq | `number` | Monotonic activity sequence after the touch |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxmetrics) SandboxMetrics


Returned by [metrics()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-metrics) · yielded by [MetricsStream](https://docs.microsandbox.dev/sdk/typescript/sandbox#metricsstream)


Point-in-time resource usage snapshot.


| Field | Type | Description |
| --- | --- | --- |
| cpuPercent | `number` | CPU usage as a percentage |
| vcpuTimeNs | `number` | Cumulative vCPU time in nanoseconds |
| memoryBytes | `number` | Current memory usage in bytes |
| memoryAvailableBytes | `number | null` | Guest-visible available memory in bytes when reported |
| memoryHostResidentBytes | `number | null` | Host-resident memory backing the guest in bytes when reported |
| memoryLimitBytes | `number` | Memory limit in bytes |
| diskReadBytes | `number` | Total bytes read from disk since boot |
| diskWriteBytes | `number` | Total bytes written to disk since boot |
| netRxBytes | `number` | Total bytes received over the network since boot |
| netTxBytes | `number` | Total bytes sent over the network since boot |
| upperUsedBytes | `number | null` | Guest-visible OCI upper filesystem used bytes when the protected reporter is available and fresh |
| upperFreeBytes | `number | null` | Guest-visible OCI upper filesystem free bytes when the protected reporter is available and fresh |
| upperHostAllocatedBytes | `number | null` | Host-allocated bytes for the writable OCI upper image when available |
| uptimeMs | `number` | Time since the sandbox was created (ms) |
| timestamp | `Date` | When this measurement was taken |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstopresult) SandboxStopResult


Returned by [waitUntilStopped()](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-waituntilstopped)


Observed terminal sandbox state returned by [`waitUntilStopped()`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandbox-waituntilstopped).


| Field | Type | Description |
| --- | --- | --- |
| name | `string` | Sandbox name |
| status | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstatus) | Terminal status that was observed |
| exitCode | `number | null` | Process exit code when it is available |
| signal | `number | null` | Terminating signal when the process was killed |
| observedAt | `Date` | When the terminal state was observed |
| source | `string | null` | Origin of the observation when reported |


### [​](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstatus) SandboxStatus


Used by [SandboxHandle.status](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxhandle) · [SandboxStopResult.status](https://docs.microsandbox.dev/sdk/typescript/sandbox#sandboxstopresult)


Current lifecycle state of a sandbox. String literal type.


| Value | Description |
| --- | --- |
| `"created"` | Persisted resource exists but has not started |
| `"starting"` | Runtime is booting or waiting for capacity |
| `"running"` | Guest agent is ready; `exec`, `shell`, `fs` work |
| `"draining"` | Graceful shutdown in progress; existing commands finish, new ones rejected |
| `"paused"` | VM is paused |
| `"stopped"` | VM shut down; configuration persisted; can be restarted |
| `"crashed"` | VM exited unexpectedly (kernel panic, OOM, etc.) |


Was this page helpful?

Yes No ⌘ I

---

# Rust SDK Sandbox reference

`https://docs.microsandbox.dev/sdk/rust/sandbox`

See [Overview](https://docs.microsandbox.dev/sandboxes/overview) for configuration examples and [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle) for state management.

See [Snapshots](https://docs.microsandbox.dev/sdk/rust/snapshots#forking) for live fork methods.


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox) Sandbox


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder) Sandbox:: builder()


```
fn builder(name: impl Into<String>) -> SandboxBuilder
```


Example


```
let sb = Sandbox::builder("api")
    .image("python")
    .create()
    .await?;
```


Create a builder for configuring a new sandbox. The builder lets you set the image, resources, volumes, networking, secrets, and other options before booting the VM. Sandbox names must be non-empty and no longer than 128 UTF-8 bytes. See [`SandboxBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder) for all available options.


Parameters


`name` impl Into<String> Sandbox name. Must be unique and no longer than 128 UTF-8 bytes.


Returns


[SandboxBuilder](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder) Builder for configuring the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxget) Sandbox:: get()


```
async fn get(name: &str) -> MicrosandboxResult<SandboxHandle>
```


Example


```
let handle = Sandbox::get("api").await?;
println!("{:?}", handle.status());
```


Get a handle to an existing sandbox (running or stopped). The handle provides status, configuration, and lifecycle control without requiring a full connection to the guest agent.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


Returns


[SandboxHandle](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle) Handle with status and lifecycle control.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist) Sandbox:: list()


```
async fn list() -> MicrosandboxResult<SandboxPage>
```


Example


```
let page = Sandbox::list().await?;
for h in page.sandboxes {
    println!("{} - {:?}", h.name(), h.status());
}
```


Return the first page of sandboxes (running, stopped, and crashed), ordered newest first. The default page size is 20.


Returns


SandboxPage Handles in this page and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist_with) Sandbox:: list_with()


```
async fn list_with(
    configure: impl FnOnce(SandboxListBuilder) -> SandboxListBuilder,
) -> MicrosandboxResult<SandboxPage>
```


Return a configured page of sandboxes. Limits must be between 1 and 100. Labels are AND-matched before pagination.


Example


```
let page = Sandbox::list_with(|list| {
    list.limit(50).label("role", "worker")
}).await?;

if let Some(cursor) = page.next_cursor {
    let next_page = Sandbox::list_with(|list| {
        list.limit(50).cursor(cursor).label("role", "worker")
    }).await?;
}
```


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxremove) Sandbox:: remove()


```
async fn remove(name: &str) -> MicrosandboxResult<()>
```


Example


```
Sandbox::remove("api").await?;
```


Delete a stopped sandbox by name. Locally, this removes the same state as [`sb.remove_persisted()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-remove_persisted); see [Destroy or remove](https://docs.microsandbox.dev/sandboxes/lifecycle#destroy-or-remove) for the exact deletion scope. Unlike `remove_persisted()`, this associated function routes through the default backend and also supports cloud sandboxes. Fails if the sandbox is still running. Stop it first.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstart) Sandbox:: start()


```
async fn start(name: &str) -> MicrosandboxResult<Sandbox>
```


Example


```
let sb = Sandbox::start("api").await?;
```


Restart a previously stopped sandbox. The VM reboots using the persisted configuration. Local handles enter attached mode and stop the sandbox when the client process exits; cloud handles do not own the service-managed VM.


Parameters


`name` &str Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstart_detached) Sandbox:: start_detached()


```
async fn start_detached(name: &str) -> MicrosandboxResult<Sandbox>
```


Restart a stopped sandbox in detached mode. The sandbox survives after your process exits.


Parameters


`name` &str Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) Running sandbox.
## Documentation Index
## ​Sandbox
## ​SandboxBuilder
## ​PatchBuilder
## ​SandboxModificationBuilder
## ​RegistryConfigBuilder
*Used by registry()*

## ​SandboxListBuilder
## ​SandboxHandle
*Returned by Sandbox::get() · Sandbox::list()*

## ​SecretPatchBuilder
*Used by secret()*

## ​Metrics reports
## ​Types













Instance methods


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-config) sb. config()


```
fn config(&self) -> &SandboxConfig
```


Example


```
println!("{} MiB", sb.config().memory_mib);
```


Access the sandbox’s full configuration.


Returns


[&SandboxConfig](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxconfig) Sandbox configuration.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-id) sb. id()


```
fn id(&self) -> SandboxId
```


Return the opaque stable identity of this persisted sandbox. The ID is backend-qualified, remains unchanged across stop and restart, and changes when the name is removed and recreated. Treat it as an equality and correlation token; do not parse it.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-detach) sb. detach()


```
async fn detach(self)
```


Example


```
sb.detach().await; // keeps running in the background
```


Release the handle without stopping the sandbox. The sandbox continues running as a background process. Reconnect later with [`Sandbox::get()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxget).


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-drain) sb. drain()


Local-only


```
async fn drain(&self) -> MicrosandboxResult<()>
```


Example


```
sb.drain().await?;
```


Start a graceful drain. Existing commands run to completion, but new `exec` calls are rejected. The sandbox transitions to `Stopped` when all in-flight commands finish. Useful for zero-downtime rotation of worker sandboxes.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-request_drain) sb. request_drain()


Local-only


```
async fn request_drain(&self) -> MicrosandboxResult<()>
```


Request graceful drain and return once the request is sent. Pair with [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait_until_stopped) when the caller needs stopped-state observation.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-fs) sb. fs()


```
fn fs(&self) -> SandboxFsOps<'_>
```


Example


```
sb.fs().write("/tmp/hello.txt", "hi").await?;
```


Get a filesystem handle for reading and writing files inside the running sandbox. See [Filesystem](https://docs.microsandbox.dev/sdk/rust/filesystem) for API details.


Returns


[SandboxFsOps](https://docs.microsandbox.dev/sdk/rust/filesystem) Filesystem handle.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-kill) sb. kill()


Local-only


```
async fn kill(&self) -> MicrosandboxResult<()>
```


Example


```
sb.kill().await?; // SIGKILL, no graceful shutdown
```


Force-terminate the sandbox immediately with SIGKILL. No graceful shutdown; use when the sandbox is unresponsive. Waits up to five seconds for stopped-state observation after the kill request. Pending writes that the workload hasn’t `fsync`’d may be lost, same durability semantics as a sudden power loss on a physical machine. Prefer [`stop()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop) for graceful shutdown that gives the workload a chance to flush.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-kill_with_timeout) sb. kill_with_timeout()


Local-only


```
async fn kill_with_timeout(&self, timeout: Duration) -> MicrosandboxResult<()>
```


Force-terminate the sandbox and wait up to `timeout` for stopped-state observation.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-request_kill) sb. request_kill()


Local-only


```
async fn request_kill(&self) -> MicrosandboxResult<()>
```


Request force termination and return once the request is sent, without waiting for stopped-state observation.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-metrics) sb. metrics()


Local-only


```
async fn metrics(&self) -> MicrosandboxResult<SandboxMetrics>
```


Example


```
let m = sb.metrics().await?;
println!("cpu {:.1}% · mem {} MiB", m.cpu_percent, m.memory_bytes / 1_048_576);
```


Get a point-in-time snapshot of the sandbox’s resource usage: CPU, memory, disk I/O, network I/O, optional upper disk usage, and uptime.


Returns


[SandboxMetrics](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetrics) Resource metrics.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-metrics_stream) sb. metrics_stream()


Local-only


```
fn metrics_stream(&self, interval: Duration) -> impl Stream<Item = MicrosandboxResult<SandboxMetrics>>
```


Example


```
use futures::StreamExt;

let mut stream = sb.metrics_stream(Duration::from_secs(1));
while let Some(snapshot) = stream.next().await {
    println!("{:.1}%", snapshot?.cpu_percent);
}
```


Stream resource metrics at a regular interval. Returns an async stream that yields a new snapshot every `interval` duration.


Parameters


`interval` Duration Time between metric snapshots.


Returns


[impl Stream<SandboxMetrics>](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetrics) Async stream yielding a snapshot each interval.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-logs) sb. logs()


Local-only


```
fn logs(&self, opts: &LogOptions) -> MicrosandboxResult<Vec<LogEntry>>
```


Example


```
use microsandbox::sandbox::{LogOptions, LogSource, Sandbox};

let handle = Sandbox::get("web").await?;

// Default: all user-program output, regardless of pipe/pty mode
let entries = handle.logs(&LogOptions::default())?;

for e in entries {
    let source = match e.source {
        LogSource::Stdout => "OUT",
        LogSource::Stderr => "ERR",
        LogSource::Output => "PTY",
        LogSource::System => "SYS",
    };
    println!(
        "[{}] {} {:?}: {}",
        e.timestamp.to_rfc3339(),
        source,
        e.session_id,
        String::from_utf8_lossy(&e.data).trim_end()
    );
}

// Filtered: last 50 entries from the past hour, including system lines
let recent = handle.logs(&LogOptions {
    tail: Some(50),
    since: Some(chrono::Utc::now() - chrono::Duration::hours(1)),
    sources: vec![
        LogSource::Stdout,
        LogSource::Stderr,
        LogSource::Output,
        LogSource::System,
    ],
    ..Default::default()
})?;
```


Read captured output from the sandbox’s `exec.log`. Backed by an on-disk JSON Lines file the runtime writes via the relay tap. Works on running and stopped sandboxes alike; there is no protocol traffic. The same method is available on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle) for callers that don’t want to start the sandbox first.
The default sources are `Stdout`, `Stderr`, and `Output` (PTY-merged). Pass `LogSource::System` to also include synthetic lifecycle markers and runtime/kernel diagnostic lines. `logs()` is **synchronous** because it’s a pure file read.


Parameters


`opts` [&LogOptions](https://docs.microsandbox.dev/sdk/rust/sandbox#logoptions) Filters: `tail`, `since`, `until`, `sources`. `LogOptions::default()` returns everything for the default sources.


Returns


[Vec<LogEntry>](https://docs.microsandbox.dev/sdk/rust/sandbox#logentry) Matching entries in chronological order.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-ping) sb. ping()


Local-only


```
async fn ping(&self) -> MicrosandboxResult<SandboxPingResult>
```


Example


```
let result = sb.ping().await?;
println!("{} reachable in {:?}", result.name, result.latency);
```


Check whether the running sandbox’s guest agent is reachable. This sends `core.ping`, returns the SDK-measured round-trip latency, and does not refresh the sandbox idle timer.


Returns


[SandboxPingResult](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxpingresult) Sandbox name and ping latency.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-touch) sb. touch()


Local-only


```
async fn touch(&self) -> MicrosandboxResult<SandboxTouchResult>
```


Example


```
let result = sb.touch().await?;
println!("{} activity seq {}", result.name, result.activity_seq);
```


Explicitly refresh the running sandbox’s idle timer. This sends `core.touch`; use it when keeping an idle sandbox alive is intentional.


Returns


[SandboxTouchResult](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxtouchresult) Sandbox name and agent activity sequence after the touch.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-modify) sb. modify()


Local-only


```
fn modify(&self) -> SandboxModificationBuilder
```


Example


```
let plan = sb.modify()
    .cpus(4)             // live when 4 <= max_cpus
    .memory(4096)        // live when 4096 MiB <= max_memory
    .env("MODE", "prod") // future execs only; the plan warns about this
    .apply()
    .await?;

for r in &plan.resize_status {
    println!("{:?}: requested {} · actual {} · {:?}", r.resource, r.requested, r.actual, r.state);
}
```


Plan or apply a configuration change. Set what to change (CPUs, memory, env vars, labels, workdir, secrets), then call [`dry_run()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-dry_run) to preview or [`apply()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-apply) to commit. Both return a [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan) labeling each change `live`, `next start`, `requires restart`, or `unsupported`. Apply is all-or-nothing.
CPU and memory resize live within the [`max_cpus`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_cpus) / [`max_memory`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_memory) ceilings; raising a ceiling requires a restart.
Env and workdir changes affect future execs only. On a stopped sandbox, changes are saved for the next boot.
Changing a secret’s substitution rules, violation action, TLS identity requirement, or placeholder passthrough hosts requires a restart if the sandbox is running. Use `.restart()` to apply now, or `.next_start()` to save for the next start. Omitted options keep their current settings.
See [`SandboxModificationBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationbuilder) for all setters and [`msb modify`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-modify) for the CLI.


Returns


[SandboxModificationBuilder](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationbuilder) Fluent builder; terminate with `dry_run()` or `apply()`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-name) sb. name()


```
fn name(&self) -> &str
```


Get the sandbox name.


Returns


&str Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-owns_lifecycle) sb. owns_lifecycle()


```
fn owns_lifecycle(&self) -> bool
```


Whether this handle owns the sandbox lifecycle. Local attached handles return `true`; local detached handles and all cloud handles return `false`, because the cloud worker owns the sandbox process.


Returns


bool `true` for a local attached handle.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-remove_persisted) sb. remove_persisted()


Local-only


```
async fn remove_persisted(&self) -> MicrosandboxResult<()>
```


Example


```
sb.stop().await?;
sb.remove_persisted().await?;
```


Delete this stopped sandbox’s persisted state. This receiver-based form is useful when you still hold the `Sandbox` instance; it has exactly the same deletion scope as [`Sandbox::remove(name)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxremove). It does **not** perform additional cleanup. See [Destroy or remove](https://docs.microsandbox.dev/sandboxes/lifecycle#destroy-or-remove) for what is deleted and which external resources are preserved.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-request_stop) sb. request_stop()


```
async fn request_stop(&self) -> MicrosandboxResult<()>
```


Request graceful shutdown and return once the request is sent, without waiting for stopped-state observation. Pair with [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait_until_stopped) when the caller needs the terminal state.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop) sb. stop()


Different on cloud


```
async fn stop(&self) -> MicrosandboxResult<()>
```


Example


```
sb.stop().await?;
```


Request graceful shutdown and wait indefinitely for the targeted run to become terminal and release runtime ownership. Success allows immediate removal without racing teardown. Cancelling the wait does not kill the sandbox or undo a delivered request. Paused or unreachable sandboxes return an error; resume explicitly or choose `kill()` when force termination is intended.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop_with_timeout) sb. stop_with_timeout()


Different on cloud


```
async fn stop_with_timeout(&self, timeout: Duration) -> MicrosandboxResult<()>
```


Apply one total budget to graceful dispatch and completion. Expiry returns `MicrosandboxError::StopTimeout` without killing; `Duration::ZERO` expires before dispatch. A shutdown request already sent may complete later. Only explicit `kill()` requests force termination.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop_and_wait) sb. stop_and_wait()


Local-only


```
async fn stop_and_wait(&self) -> MicrosandboxResult<ExitStatus>
```


Example


```
let status = sb.stop_and_wait().await?;
println!("exited: {}", status.success());
```


Stop the sandbox and wait for runtime completion. An owned child-process handle supplies its actual exit status. Detached or connected handles retain the existing synthetic success status; use [`stop()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop) or [`stop_with_timeout()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-stop_with_timeout) when you only need completion.


Returns


[ExitStatus](https://docs.microsandbox.dev/sdk/rust/execution#exitstatus) Exit code and success flag.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait) sb. wait()


Local-only


```
async fn wait(&self) -> MicrosandboxResult<ExitStatus>
```


Example


```
let status = sb.wait().await?;
```


Block until the sandbox exits on its own (without triggering a stop). Returns the exit status.


Returns


[ExitStatus](https://docs.microsandbox.dev/sdk/rust/execution#exitstatus) Exit code and success flag.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait_until_stopped) sb. wait_until_stopped()


```
async fn wait_until_stopped(&self) -> MicrosandboxResult<SandboxStopResult>
```


Block until the sandbox is observed in a terminal non-running state. Owned local sandboxes can include process exit details; detached, name-addressed, and cloud-backed sandboxes report the observed backend state.


Returns


[SandboxStopResult](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstopresult) Observed terminal sandbox state.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait_for_status) sb. wait_for_status()


```
async fn wait_for_status(&self, status: SandboxStatus) -> MicrosandboxResult<SandboxHandle>
```


Wait until this exact persisted sandbox reaches `status`. The method intentionally has no built-in timeout; wrap the future with `tokio::time::timeout` or another cancellation primitive when a deadline is required. Returns `SandboxReplaced` rather than following a reused name.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-restart) sb. restart()


```
async fn restart(&self) -> MicrosandboxResult<Sandbox>
```


Gracefully stop and start this exact sandbox using the persisted configuration. A stopped, crashed, or newly created sandbox starts directly; a starting sandbox is observed until it settles. Returns an attached local handle or a service-owned cloud handle.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-restart_with) sb. restart_with()


```
async fn restart_with(&self, options: RestartOptions) -> MicrosandboxResult<Sandbox>
```


Restart with explicit lifecycle controls. `RestartOptions` defaults to graceful shutdown, a ten-second timeout, and attached local start. Set `force` to kill instead of draining, `timeout` to control how long shutdown can take, and `detached` to start a local background sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-destroy) sb. destroy()


```
async fn destroy(&self) -> MicrosandboxResult<()>
```


Gracefully stop and remove this exact sandbox. Unlike [`remove_persisted()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-remove_persisted), `destroy` accepts a running sandbox, waits for it to shut down, and then deletes its persisted state.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-destroy_with) sb. destroy_with()


```
async fn destroy_with(&self, options: DestroyOptions) -> MicrosandboxResult<()>
```


Destroy with explicit shutdown controls. `DestroyOptions` defaults to graceful shutdown with a ten-second timeout; set `force` to kill immediately or `timeout` to change how long shutdown can take. Identity checks prevent this receiver from deleting a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-restore_warnings) sb. restore_warnings()


```
async fn restore_warnings(&self) -> MicrosandboxResult<Vec<ExternalMountWarning>>
```


Return warnings for unavailable external filesystems and accepted restore mismatches. See [External mounts](https://docs.microsandbox.dev/sandboxes/snapshots#external-mounts) for restore options.
Each `ExternalMountWarning` contains:


| Field | Type | Description |
| --- | --- | --- |
| `guest_path` | `String` | Guest-visible mount path. |
| `reason` | `String` | Why the resource could not be reconstructed. |
| `stale_inodes` | `Vec<u64>` | Permanently invalid captured node IDs; empty when the whole export is unavailable. |


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder-2) SandboxBuilder


Builder for configuring a sandbox before creation. Obtained via [`Sandbox::builder(name)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder). Every setter returns `Self`, so calls chain. Examples are shown on the methods where usage is non-obvious.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-slug) sandbox. slug()


Cloud-only


```
fn slug(self, slug: impl Into<String>) -> Self
```


Request a globally unique cloud slug. When omitted, microsandbox cloud assigns one; creation fails if the requested slug is already taken.


Parameters


`slug` impl Into<String> Requested cloud slug.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-build) sandbox. build()


```
async fn build(self) -> MicrosandboxResult<SandboxConfig>
```


Materialize the [`SandboxConfig`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxconfig) without pulling an image or booting the sandbox. Validates fresh-boot configuration. Use `Sandbox::restore()` for snapshots. For booting, use [`create`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-create) instead; call [`detached(true)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-detached) first for background mode. Local `create()` keeps patches until image metadata is available. Cloud `create()` layers settings before sending the request; the cloud worker resolves image metadata.


Returns


[SandboxConfig](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxconfig) Validated, ready-to-boot configuration.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-overlay) sandbox. overlay()


```
fn overlay(self, patch: SandboxConfigPatch) -> Self
```


Apply sparse sandbox settings and create-time options after built-in and global defaults. Builder methods called after `overlay` take precedence over the patch; managed overrides are applied last.
The builder uses the active backend’s cached configuration when `build()` or `create()` runs. Local creation stacks image defaults, global defaults, CLI/SDK patches, then managed overrides in one resolver before validation. Omitted fields inherit lower layers; explicit nullable clears survive image defaults. Cloud creation also applies user and managed settings, then rejects unsupported options before sending the request.
`build()` returns a concrete `SandboxConfig` without pulling image metadata. On local creation, `workdir: None` inherits global defaults, then image defaults if global workdir is omitted. A concrete config cannot distinguish omission from an explicit clear; use direct builder `create()` to preserve sparse clears through image resolution. Managed overrides apply last in both paths.
`SandboxConfigPatch` patches the SDK configuration. Its `spec` field is a `SandboxSpecPatch` for shared settings such as image, resources, and networking. Create-time options, including registry credentials, replacement settings, and the requested slug, live alongside `spec`.


Example


```
use microsandbox::{
    EnvVar, Sandbox, SandboxConfigPatch, SandboxResourcesPatch, SandboxSpecPatch,
};

let resources = SandboxResourcesPatch::new()
    .max_memory_mib(1024)
    .memory_mib(1024)
    .max_cpus(2)
    .cpus(2);

let patch = SandboxConfigPatch::new()
    .spec(
        SandboxSpecPatch::new()
            .resources(resources)
            .env(vec![EnvVar::new("MODE", "production")]),
    )
    .replace_existing(true);

let sandbox = Sandbox::builder("agent")
    .image("python:3.12")
    .overlay(patch)
    .memory(2048)
    .create()
    .await?;
```


Environment variables merge by variable name, while labels and scripts merge by map key. Secret entries merge by environment-variable name. Later values win when keys match. Use the generated `replace_*` methods to replace a complete collection; `clear_*` removes the field from the patch so the lower-precedence value remains unchanged.
Patch fields preserve the visibility of their source configuration fields, so ordinary fields and nested patches can be updated directly:


```
let mut patch = SandboxConfigPatch::new();
patch.spec.resources.cpus = Some(2);
patch.spec.runtime.cmd = Some(vec!["python".into(), "app.py".into()]);
patch.spec.runtime.workdir = Some(None); // Explicitly clear the working directory.
patch.registry_auth = Some(None); // Explicitly clear per-create credentials.
```


For nullable fields, `None` omits the update, `Some(None)` clears the value, and `Some(Some(value))` sets it.
Mergeable collections keep their merge/replacement state private and expose `get_<field>()` for borrowing their pending values. Ordinary fields have no generated getters. The collections’ `get_<field>_mut()` accessors edit pending values without cloning, initializing an absent collection empty in merge mode and preserving any existing replacement mode:


```
patch.spec.get_env_mut().push(EnvVar::new("REGION", "us-east"));
patch.spec.get_labels_mut().insert("team".into(), "platform".into());
```


These accessors edit pending values without deduplicating them. Use `env_mut(...)` to merge entries by name immediately, or `replace_env_mut(...)` to replace the collection. Fluent setters, replacements, clears, and `overlay` remain available, along with their `_mut` variants returning `&mut Self`.
Use fluent setters to construct patches and `if let` for optional inputs. Once all overlays are composed, `into_config()` applies the patch to the type’s defaults:


```
use microsandbox::{SandboxConfigPatch, SandboxResourcesPatch, SandboxSpecPatch};

let cpus = Some(4);
let mut resources = SandboxResourcesPatch::new();
if let Some(cpus) = cpus {
    resources.cpus_mut(cpus);
}
let config = SandboxConfigPatch::new()
    .spec(
        SandboxSpecPatch::new()
            .name("example".into())
            .resources(resources),
    )
    .into_config();
```


`into_config()` does not load configuration files, consult a backend, or validate the result. Keep patches for `SandboxBuilder::overlay()` when creating a sandbox so backend and managed settings can still be layered. Use `apply_to(&mut config)` when updating an existing value.
Both patches contain typed inputs. YAML loading, relative-path resolution, `${ENV}` expansion, and snapshot lookup remain CLI or builder responsibilities. Runtime metadata stays internal, and create-time credentials and flags retain their existing serialization exclusions.


Migrating from the earlier patch types

The shared patch previously named `SandboxConfigPatch` is now `SandboxSpecPatch`. To use it with the builder, wrap it with `SandboxConfigPatch::new().spec(spec_patch)`. Update direct field access such as `patch.resources` to `patch.spec.resources` when using the SDK patch. Existing configuration files and serialized sandbox specifications keep their shape. The generated patch model also replaces the handwritten patch hierarchy from microsandbox 0.6.15 and earlier:

| Earlier type | Current type |
| --- | --- |
| `ResourceConfigPatch` | `SandboxResourcesPatch` |
| `RuntimeConfigPatch` | `SandboxRuntimeOptionsPatch` |
| `NetworkConfigPatch` | `NetworkSpecPatch` |
| `NetworkPolicyConfigPatch` | `SandboxPolicyPatch` |
| `SecretConfigPatch` | `SecretsConfigPatch` |

Closure-based patch modifiers have been removed. Update Rust call sites to use direct field access or mutable collection accessors instead. Filesystem, script, image, and init values use `SandboxSpecPatch`, nested under `SandboxConfigPatch.spec` in the SDK. `LocalConfig` remains available as a deprecated alias of `GlobalConfig`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-cpus) sandbox. cpus()


```
fn cpus(self, count: u8) -> Self
```


Set the number of virtual CPUs. This is a limit, not a reservation. Default: `1`.


Parameters


`count` u8 Number of vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-max_cpus) sandbox. max_cpus()


Local-only


```
fn max_cpus(self, count: u8) -> Self
```


Set the boot-time maximum possible virtual CPU capacity. This reserves the envelope a sandbox can use after restart-backed changes and future live CPU activation; it does not increase the effective vCPU count by itself.


Parameters


`count` u8 Maximum possible vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-create) sandbox. create()


```
async fn create(self) -> MicrosandboxResult<Sandbox>
```


Boot the sandbox. Local handles use attached mode and stop the sandbox when the client process exits; cloud handles do not own the service-managed VM, so stop or remove cloud sandboxes explicitly.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-connect_or_create) sandbox. connect_or_create()


```
async fn connect_or_create(self) -> MicrosandboxResult<Sandbox>
```


Reuse or create the sandbox with this name. The method connects when it is running, waits while it is starting, starts it when it is created, stopped, or crashed, and creates it only when the name is unused. Builder configuration applies only to a new sandbox. Concurrent callers reuse the same sandbox. Combining this method with [`replace()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-replace) returns `InvalidConfig`.


Returns


`MicrosandboxResult<` [`Sandbox`](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-detached) sandbox. detached()


```
fn detached(self, detached: bool) -> Self
```


Example


```
let sb = Sandbox::builder("worker")
    .image("python")
    .detached(true)
    .create()
    .await?;
sb.detach().await;
```


Choose whether the sandbox is created in detached/background mode. Detached sandboxes survive the creating process. Defaults to `false`.


Parameters


`detached` bool When `true`, create the sandbox in detached mode.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-create_detached) sandbox. create_detached()


```
async fn create_detached(self) -> MicrosandboxResult<Sandbox>
```


Example


```
let sb = Sandbox::builder("worker")
    .image("python")
    .create_detached()
    .await?;
sb.detach().await;
```


Boot the sandbox in detached mode. This is a compatibility helper for `.detached(true).create()`. Prefer [`detached(true)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-detached) with [`create()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-create) for new code so attached and detached creation use the same flow.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-disable_network) sandbox. disable_network()


```
fn disable_network(self) -> Self
```


Fully disable networking. No network interface is created.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-entrypoint) sandbox. entrypoint()


```
fn entrypoint(self, cmd: impl IntoIterator<Item = impl Into<String>>) -> Self
```


Override the image ENTRYPOINT used by default-workload execution. [`Sandbox::exec_default`](https://docs.microsandbox.dev/sdk/rust/execution) combines it with the effective CMD. Literal [`Sandbox::exec`](https://docs.microsandbox.dev/sdk/rust/execution), [`Sandbox::attach`](https://docs.microsandbox.dev/sdk/rust/execution), and [`Sandbox::shell`](https://docs.microsandbox.dev/sdk/rust/execution) calls ignore it.


Parameters


`cmd` impl IntoIterator Entrypoint command and arguments.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-env) sandbox. env()


```
fn env(self, key: impl Into<String>, value: impl Into<String>) -> Self
```


Set an environment variable visible to all commands. Can be called multiple times. Per-command env vars (via `exec_with`) are merged on top.


Parameters


`key` impl Into<String> Variable name. `value` impl Into<String> Variable value.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-hostname) sandbox. hostname()


Local-only


```
fn hostname(self, hostname: impl Into<String>) -> Self
```


Set the guest hostname.


Parameters


`hostname` impl Into<String> Hostname.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-idle_timeout) sandbox. idle_timeout()


```
fn idle_timeout(self, secs: u64) -> Self
```


Auto-drain the sandbox after this many seconds of inactivity (no active exec sessions). Enforced on the host side.


Parameters


`secs` u64 Idle timeout in seconds.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-cmd) sandbox. cmd()


```
fn cmd(self, cmd: impl IntoIterator<Item = impl Into<String>>) -> Self
```


Override the image CMD used by default-workload execution. An empty array explicitly clears the image CMD. This describes durable configuration and does not execute anything during `create()`.


```
let sb = Sandbox::builder("worker")
    .image("example/worker:latest")
    .cmd(["worker.py", "--once"])
    .create()
    .await?;
```


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-init) sandbox. init()


```
fn init(self, cmd: impl Into<PathBuf>) -> Self
```


Example


```
let sb = Sandbox::builder("worker")
    .image("jrei/systemd-debian:12")
    .init("auto")
    .create()
    .await?;
```


Hand off PID 1 inside the guest to `cmd` after agentd finishes its boot-time setup. The agent forks; the parent execs the init and becomes PID 1; the agent continues as a child process. See [Custom init system](https://docs.microsandbox.dev/sandboxes/bootstrap#custom-init-system) for image picks, shutdown semantics, and tradeoffs.
`cmd` is either an absolute path inside the guest rootfs or the literal `"auto"`.
Auto first honors a known init at the start of the image ENTRYPOINT, such as `/init` in s6-overlay images. If none is found, it falls back to probing `/sbin/init`, `/lib/systemd/systemd`, and `/usr/lib/systemd/systemd` inside the guest.
When attached `msb run` uses an image-declared init entrypoint, the remaining ENTRYPOINT plus CMD or trailing command is passed to that init instead of direct-executed through agentd. For init binaries that take argv or extra env (rare), use [`init_with`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-init_with).


Parameters


`cmd` impl Into<PathBuf> Absolute path inside the guest, or `“auto”`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-init_with) sandbox. init_with()


```
fn init_with(
    self,
    cmd: impl Into<PathBuf>,
    f: impl FnOnce(InitOptionsBuilder) -> InitOptionsBuilder,
) -> Self
```


Example


```
let sb = Sandbox::builder("worker")
    .image("jrei/systemd-debian:12")
    .init_with("/lib/systemd/systemd", |i| i
        .args(["--unit=multi-user.target"])
        .env("container", "microsandbox"))
    .create()
    .await?;
```


Like [`init`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-init), but with a closure-builder for argv and env vars. Mirrors `exec_with` in shape. The builder exposes `arg`, `args`, `env`, and `envs`. Calling `init` or `init_with` more than once overwrites, unlike `env`, which appends. The init is one-shot pre-boot.


Parameters


`cmd` impl Into<PathBuf> Absolute path to the init binary inside the guest. `f` FnOnce(InitOptionsBuilder) Closure populating argv and env.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-image) sandbox. image()


Limited on cloud


```
fn image(self, image: impl IntoImage) -> Self
```


Set the root filesystem source. Accepts OCI image names, local directory paths, or disk image paths. The format is auto-detected.


Parameters


`image` impl IntoImage OCI image name, local directory path, or disk image path.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-image_with) sandbox. image_with()


Limited on cloud


```
fn image_with(self, f: impl FnOnce(ImageBuilder) -> ImageBuilder) -> Self
```


Example


```
use microsandbox::size::SizeExt;

let sb = Sandbox::builder("worker")
    .image_with(|i| i.oci("python:3.12").root_disk(8.gib()))
    .create()
    .await?;
```


Configure an explicit rootfs source. Use this for OCI-only settings such as the writable root disk, or for disk images when the filesystem type can’t be auto-detected.


Parameters


`f` FnOnce(ImageBuilder) Configure the rootfs source.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-log_level) sandbox. log_level()


```
fn log_level(self, level: LogLevel) -> Self
```


Override the sandbox process’s log verbosity.


Parameters


`level` [LogLevel](https://docs.microsandbox.dev/sdk/rust/sandbox#loglevel) Log level.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-max_duration) sandbox. max_duration()


```
fn max_duration(self, secs: u64) -> Self
```


Set the maximum sandbox lifetime in seconds. When exceeded, the host drains and stops the sandbox. Enforced on the host side; the guest cannot override it.


Parameters


`secs` u64 Maximum lifetime in seconds.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-memory) sandbox. memory()


```
fn memory(self, size: impl Into<Mebibytes>) -> Self
```


Set the guest memory size. Physical pages are only allocated as the guest touches them, so this is a limit, not an upfront reservation. Default: `512` MiB.


Parameters


`size` impl Into<Mebibytes> Memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-max_memory) sandbox. max_memory()


Local-only


```
fn max_memory(self, size: impl Into<Mebibytes>) -> Self
```


Set the boot-time maximum hotpluggable guest memory. This reserves the envelope a sandbox can use after restart-backed changes and future live memory activation; it does not increase the effective memory by itself.


Parameters


`size` impl Into<Mebibytes> Maximum memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-thp) sandbox. thp()


```
fn thp(self, policy: TransparentHugePagePolicy) -> Self
```


Select the guest transparent huge-page policy applied through the kernel command line at boot. Default: `TransparentHugePagePolicy::Madvise`.


Parameters


`policy` TransparentHugePagePolicy `Always`, `Madvise`, or `Never`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-guest_clock) sandbox. guest_clock()


```
fn guest_clock(self, policy: GuestClockPolicy) -> Self
```


Control whether the sandbox clock follows the host. Full snapshots save this setting; restores inherit it unless overridden. Local-only. See [guest clock](https://docs.microsandbox.dev/sandboxes/snapshots#keep-the-guest-clock) for details.


Parameters


`policy` GuestClockPolicy `Sync` (default) follows host time; `Off` stops host clock updates after boot.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-intercept_tls) sandbox. intercept_tls()


```
fn intercept_tls(self) -> Self
```


Enable [TLS interception](https://docs.microsandbox.dev/networking/tls) for a local sandbox. Existing network and TLS settings are preserved, including bypass hosts and custom CAs. Does not re-enable disabled networking.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-network) sandbox. network()


```
fn network(self, f: impl FnOnce(NetworkBuilder) -> NetworkBuilder) -> Self
```


Configure networking. See [Networking](https://docs.microsandbox.dev/sdk/rust/networking) for the full builder API.


Parameters


`f` [NetworkBuilder](https://docs.microsandbox.dev/sdk/rust/networking#networkbuilder) Configure the network.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-proxy) sandbox. proxy()


```
fn proxy<P>(self, configure: impl FnOnce(OutboundProxyBuilder) -> P) -> Self
where
    P: OutboundProxyConfig
```


Configure the single proxy used for outbound sandbox connections. See [Proxies](https://docs.microsandbox.dev/sdk/rust/proxies) for the protocol builders and examples.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-patch) sandbox. patch()


```
fn patch(self, f: impl FnOnce(PatchBuilder) -> PatchBuilder) -> Self
```


Modify the rootfs before the VM boots. Patches go into the writable layer; the base image is untouched. See [`PatchBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#patchbuilder) for the operations.


Parameters


`f` [FnOnce(PatchBuilder)](https://docs.microsandbox.dev/sdk/rust/sandbox#patchbuilder) Configure rootfs patches.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-port) sandbox. port()


Local-only


```
fn port(self, host_port: u16, guest_port: u16) -> Self
```


Publish a TCP port from the sandbox to the host. The default host bind address is `127.0.0.1`.


Parameters


`host_port` u16 Port on the host. `guest_port` u16 Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-port_bind) sandbox. port_bind()


Local-only


```
fn port_bind(self, host_bind: IpAddr, host_port: u16, guest_port: u16) -> Self
```


Publish a TCP port on a specific host bind address, such as `0.0.0.0`.


Parameters


`host_bind` IpAddr Host bind address. `host_port` u16 Port on the host. `guest_port` u16 Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-port_udp) sandbox. port_udp()


Local-only


```
fn port_udp(self, host_port: u16, guest_port: u16) -> Self
```


Publish a UDP port. The default host bind address is `127.0.0.1`.


Parameters


`host_port` u16 Port on the host. `guest_port` u16 Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-port_udp_bind) sandbox. port_udp_bind()


Local-only


```
fn port_udp_bind(self, host_bind: IpAddr, host_port: u16, guest_port: u16) -> Self
```


Publish a UDP port on a specific host bind address.


Parameters


`host_bind` IpAddr Host bind address. `host_port` u16 Port on the host. `guest_port` u16 Port inside the sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-pull_policy) sandbox. pull_policy()


```
fn pull_policy(self, policy: PullPolicy) -> Self
```


Control when the OCI image is pulled from the registry.


Parameters


`policy` [PullPolicy](https://docs.microsandbox.dev/sdk/rust/sandbox#pullpolicy) Pull behavior.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-registry) sandbox. registry()


Limited on cloud


```
fn registry(self, f: impl FnOnce(RegistryConfigBuilder) -> RegistryConfigBuilder) -> Self
```


Example


```
use microsandbox::{RegistryAuth, Sandbox};

let sb = Sandbox::builder("worker")
    .image("registry.example.com/team/app:latest")
    .registry(|r| r.auth(RegistryAuth::Basic {
        username: "user".into(),
        password: "token".into(),
    }))
    .create()
    .await?;
```


Configure registry connection settings for the sandbox image pull, including explicit auth, insecure HTTP, and custom CA certificates.


Parameters


`f` [RegistryConfigBuilder](https://docs.microsandbox.dev/sdk/rust/sandbox#registryconfigbuilder) Closure that configures registry auth and TLS options.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-replace) sandbox. replace()


Local-only


```
fn replace(self) -> Self
```


If a sandbox with the same name already exists, stop it, remove it, and create a fresh one. Without this, creation fails on name conflict.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-script) sandbox. script()


```
fn script(self, name: impl Into<String>, content: impl Into<String>) -> Self
```


Add a named script at `/.msb/scripts/` inside the guest. Scripts are added to `PATH` and can be called by name via `exec()` or `shell()`.


Parameters


`name` impl Into<String> Script name (becomes the filename). `content` impl Into<String> Script content.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret) sandbox. secret()


```
fn secret(self, f: impl FnOnce(SecretBuilder) -> SecretBuilder) -> Self
```


Add a secret with full configuration. See [Secrets](https://docs.microsandbox.dev/sdk/rust/secrets) for the builder API. Automatically enables TLS interception.


Parameters


`f` [SecretBuilder](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder) Configure the secret.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret_env) sandbox. secret_env()


```
fn secret_env(self, env_var: impl Into<String>, value: impl Into<String>, allowed_host: impl Into<String>) -> Self
```


Shorthand for adding a header-injected secret. Equivalent to `.secret(|s| s.env(env_var).value(value).allow(allowed_host))`.
**Plaintext at rest.** The value is persisted verbatim in the durable sandbox config until a later `modify` rotate migrates the entry to a source reference. Prefer `.secret(|s| s.source(..))` when the value can be referenced; use this path when you hold only a value. A future host-side secret store will switch this method to import-then-reference with no signature change.


Parameters


`env_var` impl Into<String> Environment variable name (non-empty, no `=` or NUL). `value` impl Into<String> Secret value. `allowed_host` impl Into<String> Allowed destination host.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-shell) sandbox. shell()


```
fn shell(self, shell: impl Into<String>) -> Self
```


Set the shell used by [`Sandbox::shell()`](https://docs.microsandbox.dev/sdk/rust/execution). Default: `/bin/sh`.


Parameters


`shell` impl Into<String> Shell path (e.g. `“/bin/bash”`).


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-user) sandbox. user()


```
fn user(self, user: impl Into<String>) -> Self
```


Set the default guest user for all commands.


Parameters


`user` impl Into<String> User name or UID.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-volume) sandbox. volume()


```
fn volume(self, guest_path: impl Into<String>, f: impl FnOnce(MountBuilder) -> MountBuilder) -> Self
```


Add a volume mount. See [Volumes](https://docs.microsandbox.dev/sdk/rust/volumes) for mount types.


Parameters


`guest_path` impl Into<String> Mount point inside the sandbox. `f` [MountBuilder](https://docs.microsandbox.dev/sdk/rust/volumes#mountbuilder) Configure the mount.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-workdir) sandbox. workdir()


```
fn workdir(self, path: impl Into<String>) -> Self
```


Set the default working directory for all commands.


Parameters


`path` impl Into<String> Absolute path inside the guest.


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patchbuilder) PatchBuilder


Builder for pre-boot root filesystem patches.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-append) patch. append()


```
fn append(self, path: impl Into<String>, content: impl Into<String>) -> Self
```


Append `content` to an existing file at `path`. If the file lives in a lower image layer, it’s copied up first.


Parameters


`path` impl Into<String> Absolute path inside the guest. `content` impl Into<String> Text to append.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-copy_dir) patch. copy_dir()


Limited on cloud


```
fn copy_dir(self, src: impl Into<PathBuf>, dst: impl Into<String>, replace: bool) -> Self
```


Recursively copy a host directory at `src` into the guest rootfs at `dst`.


Parameters


`src` impl Into<PathBuf> Host source directory. `dst` impl Into<String> Absolute destination path inside the guest. `replace` bool When `true`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-copy_file) patch. copy_file()


Limited on cloud


```
fn copy_file(
    self,
    src: impl Into<PathBuf>,
    dst: impl Into<String>,
    mode: Option<u32>,
    replace: bool,
) -> Self
```


Copy a single host file at `src` into the guest rootfs at `dst`.


Parameters


`src` impl Into<PathBuf> Host source file. `dst` impl Into<String> Absolute destination path inside the guest. `mode` Option<u32> File mode, e.g. `Some(0o644)`. `None` keeps the source mode. `replace` bool When `true`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-file) patch. file()


```
fn file(
    self,
    path: impl Into<String>,
    content: impl Into<Vec<u8>>,
    mode: Option<u32>,
    replace: bool,
) -> Self
```


Write raw bytes at `path`.


Parameters


`path` impl Into<String> Absolute path inside the guest. `content` impl Into<Vec<u8>> Raw byte content. `mode` Option<u32> File mode, e.g. `Some(0o644)`. `replace` bool When `true`, overwrite an existing path.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-mkdir) patch. mkdir()


```
fn mkdir(self, path: impl Into<String>, mode: Option<u32>) -> Self
```


Create a directory at `path`. Idempotent: a no-op if the directory already exists.


Parameters


`path` impl Into<String> Absolute path inside the guest. `mode` Option<u32> Directory mode, e.g. `Some(0o755)`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-remove) patch. remove()


```
fn remove(self, path: impl Into<String>) -> Self
```


Delete a file or directory at `path`. Idempotent: a no-op if the path doesn’t exist.


Parameters


`path` impl Into<String> Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-symlink) patch. symlink()


```
fn symlink(self, target: impl Into<String>, link: impl Into<String>, replace: bool) -> Self
```


Create a symlink at `link` pointing to `target`.


Parameters


`target` impl Into<String> What the symlink points to (literal symlink target text). `link` impl Into<String> Absolute path of the symlink itself. `replace` bool When `true`, overwrite an existing path at `link`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#patch-text) patch. text()


```
fn text(
    self,
    path: impl Into<String>,
    content: impl Into<String>,
    mode: Option<u32>,
    replace: bool,
) -> Self
```


Write UTF-8 text content at `path`.


Parameters


`path` impl Into<String> Absolute path inside the guest. `content` impl Into<String> Text content. `mode` Option<u32> File mode, e.g. `Some(0o644)`. `replace` bool When `true`, overwrite an existing path.


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationbuilder) SandboxModificationBuilder


Builder for planning or applying sandbox configuration changes.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-apply) modification. apply()


```
async fn apply(self) -> MicrosandboxResult<SandboxModificationPlan>
```


Apply the changes. Live changes are made to the running sandbox first, and the new config is saved only after they succeed, so a failed apply leaves the old config in place. Changes for a stopped sandbox, or requested with [`next_start()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-next_start), are saved and take effect on the next start. With [`restart()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-restart), `apply()` stops and starts the sandbox so that restart-required changes take effect.
A live CPU or memory resize can take a moment to settle. The returned plan’s `resize_status` reports progress per resource; see [`ResourceResizeStatus`](https://docs.microsandbox.dev/sdk/rust/sandbox#resourceresizestatus).


Returns


[SandboxModificationPlan](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan) The applied plan, with `applied: true` and live resize outcomes in `resize_status`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-cpus) modification. cpus()


```
fn cpus(self, cpus: u8) -> Self
```


Set the desired effective vCPU count. Applies live to a running sandbox when the target fits inside the booted `max_cpus`; otherwise it requires a restart.


Parameters


`cpus` u8 Number of vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_cpus) modification. max_cpus()


Local-only


```
fn max_cpus(self, max_cpus: u8) -> Self
```


Set the desired boot-time maximum possible vCPU count. Capacity is fixed at boot, so this is always restart-backed on a running sandbox.


Parameters


`max_cpus` u8 Maximum possible vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-dry_run) modification. dry_run()


```
async fn dry_run(self) -> MicrosandboxResult<SandboxModificationPlan>
```


Example


```
let plan = sb.modify().cpus(8).dry_run().await?;

for change in &plan.changes {
    if let PlannedChange::Config(c) = change {
        println!("{}: {:?} -> {:?} ({:?})", c.field, c.before, c.after, c.disposition);
    }
}
```


Compute the modification plan without applying anything. Use it to preview how each change classifies and whether conflicts block the patch.


Returns


[SandboxModificationPlan](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan) The plan, with `applied: false`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-env) modification. env()


```
fn env(self, key: impl Into<String>, value: impl Into<String>) -> Self
```


Set an environment variable for future execs. Can be called multiple times. On a running sandbox this applies to future execs only; running processes keep their current environment.


Parameters


`key` impl Into<String> Variable name. `value` impl Into<String> Variable value.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-remove_env) modification. remove_env()


```
fn remove_env(self, key: impl Into<String>) -> Self
```


Remove an environment variable. Same future-execs-only semantics as [`env()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-env).


Parameters


`key` impl Into<String> Variable name to remove.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-label) modification. label()


```
fn label(self, key: impl Into<String>, value: impl Into<String>) -> Self
```


Set a sandbox label. Can be called multiple times.


Parameters


`key` impl Into<String> Label key. `value` impl Into<String> Label value.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-remove_label) modification. remove_label()


```
fn remove_label(self, key: impl Into<String>) -> Self
```


Remove a sandbox label.


Parameters


`key` impl Into<String> Label key to remove.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-memory) modification. memory()


```
fn memory(self, size: impl Into<Mebibytes>) -> Self
```


Set the desired effective guest memory. Applies live to a running sandbox when the target fits inside the booted `max_memory`; otherwise it requires a restart.


Parameters


`size` impl Into<Mebibytes> Memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-memory_mib) modification. memory_mib()


```
fn memory_mib(self, memory_mib: u32) -> Self
```


Set the desired effective guest memory in MiB. Same as [`memory()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-memory) with an explicit unit.


Parameters


`memory_mib` u32 Memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_memory) modification. max_memory()


Local-only


```
fn max_memory(self, size: impl Into<Mebibytes>) -> Self
```


Set the desired boot-time maximum hotpluggable memory. Capacity is fixed at boot, so this is always restart-backed on a running sandbox.


Parameters


`size` impl Into<Mebibytes> Maximum memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_memory_mib) modification. max_memory_mib()


Local-only


```
fn max_memory_mib(self, max_memory_mib: u32) -> Self
```


Set the desired boot-time maximum hotpluggable memory in MiB. Same as [`max_memory()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-max_memory) with an explicit unit.


Parameters


`max_memory_mib` u32 Maximum memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-next_start) modification. next_start()


```
fn next_start(self) -> Self
```


Persist the requested changes for the next start, leaving any running VM unchanged. Every change classifies as `next start`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-restart) modification. restart()


```
fn restart(self) -> Self
```


Plan under restart-backed apply semantics. When the patch contains restart-required changes, [`apply()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-apply) stops the sandbox, persists the config, and starts it again so the changes become active now.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-secret) modification. secret()


```
fn secret(self, f: impl FnOnce(SecretPatchBuilder) -> SecretPatchBuilder) -> Self
```


Example


```
use microsandbox::sandbox::SecretSource;

let plan = sb.modify()
    .secret(|s| s
        .env("API_KEY")
        .source(SecretSource::Env { var: "API_KEY".into() })
        .allow("api.example.com"))
    .apply()
    .await?;
```


Declare the desired state of one secret via a [`SecretPatchBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#secretpatchbuilder) closure. The spec mirrors the create-time [`SecretBuilder`](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder) vocabulary. The planner diffs it against the existing config to infer the change. A secret that does not exist yet is `added`, and material on an existing secret is `rotated`. Host or placeholder differences update those aspects. Declaring the same secret again replaces the earlier spec; removal is always explicit through [`remove_secret()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-remove_secret).


Parameters


`f` FnOnce(SecretPatchBuilder) Closure declaring the secret’s desired state.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-remove_secret) modification. remove_secret()


```
fn remove_secret(self, name: impl Into<String>) -> Self
```


Remove a secret. Removal is always explicit; omitting a secret from the patch never removes it.


Parameters


`name` impl Into<String> Secret name (its environment variable name).


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-workdir) modification. workdir()


```
fn workdir(self, path: impl Into<String>) -> Self
```


Set the working directory for future execs. On a running sandbox this applies to future execs only.


Parameters


`path` impl Into<String> Absolute path inside the guest.


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#registryconfigbuilder) RegistryConfigBuilder


Used by [registry()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-registry)


Builder passed to [`registry()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-registry) for per-sandbox registry connection settings.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#registry-auth) registry. auth()


```
auth(auth: RegistryAuth)
```


Set explicit credentials for the image registry


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#registry-insecure) registry. insecure()


```
insecure()
```


Use plain HTTP for the registry


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#registry-ca_certs) registry. ca_certs()


```
ca_certs(pem_data: Vec<u8>)
```


Trust additional PEM-encoded CA certificates


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlistbuilder) SandboxListBuilder


Fluent configuration passed to [`Sandbox::list_with()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist_with). Keep the labels and limit unchanged when continuing with a cursor.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#list-limit) list. limit()


```
limit(n)
```


Set a page size from 1 through 100


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#list-cursor) list. cursor()


```
cursor(cursor)
```


Continue after a previous page’s `next_cursor`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#list-label) list. label()


```
label(key, value)
```


Require one label; repeated calls are AND-matched


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#list-labels) list. labels()


```
labels(iterable)
```


Add several AND-matched labels


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle) SandboxHandle


Returned by [Sandbox::get()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxget) · [Sandbox::list()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist)


A sandbox metadata and lifecycle handle that does not require an active guest-agent connection.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-config) h. config()


Local-only


```
config()
```


Parsed configuration


Returns


`Result<` [`SandboxConfig`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxconfig) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-config_json) h. config_json()


```
config_json()
```


Raw JSON configuration


Returns


`&str`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-connect) h. connect()


```
connect()
```


Connect to a running sandbox; returns an error if it doesn’t respond within ten seconds


Returns


`Result<` [`Sandbox`](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-connect_with_timeout) h. connect_with_timeout()


```
connect_with_timeout(timeout)
```


Same as `connect()` with an explicit timeout


Returns


`Result<` [`Sandbox`](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-connect_or_start) h. connect_or_start()


```
async fn connect_or_start(&self) -> MicrosandboxResult<Sandbox>
```


Connect to this exact sandbox when it is running, wait through `Starting`, or start it in attached mode when it is `Created`, `Stopped`, or `Crashed`. `Draining` and `Paused` are rejected. If another caller starts it at the same time, both callers connect to the same sandbox without following a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-connect_or_start_detached) h. connect_or_start_detached()


```
async fn connect_or_start_detached(&self) -> MicrosandboxResult<Sandbox>
```


Behaves like [`connect_or_start()`](https://docs.microsandbox.dev/sdk/rust/sandbox#h-connect_or_start), but starts a local stopped sandbox in detached/background mode. Connecting to an already-running sandbox never changes its ownership.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-created_at) h. created_at()


```
created_at()
```


Creation timestamp


Returns


`Option<DateTime<Utc>>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-kill) h. kill()


Local-only


```
kill()
```


Force terminate and wait until stopped state is observed


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-kill_with_timeout) h. kill_with_timeout()


Local-only


```
kill_with_timeout(timeout)
```


Same as `kill()` with an explicit observation timeout


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-logs) h. logs()


Local-only


```
logs()
```


Read captured `exec.log` (works without starting)


Returns


`Result<Vec<` [`LogEntry`](https://docs.microsandbox.dev/sdk/rust/sandbox#logentry) `>>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-metrics) h. metrics()


Local-only


```
metrics()
```


Point-in-time resource metrics


Returns


`Result<` [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetrics) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-modify) h. modify()


Local-only


```
modify()
```


Start planning a configuration change (works without starting; changes on a stopped sandbox persist for the next boot)


Returns


[`SandboxModificationBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationbuilder)


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-name) h. name()


```
name()
```


Sandbox name, up to 128 UTF-8 bytes


Returns


`&str`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-id) h. id()


```
fn id(&self) -> SandboxId
```


Return the stable identity captured by this metadata handle. Receiver lifecycle calls stay bound to this ID and return `SandboxReplaced` if the reusable name now points to another sandbox.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-ping) h. ping()


Local-only


```
ping()
```


Check agent reachability without refreshing idle activity


Returns


`Result<` [`SandboxPingResult`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxpingresult) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-remove) h. remove()


```
remove()
```


Delete sandbox and state


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-request_drain) h. request_drain()


Local-only


```
request_drain()
```


Request graceful drain without waiting


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-request_kill) h. request_kill()


Local-only


```
request_kill()
```


Request force termination without waiting


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-request_stop) h. request_stop()


```
request_stop()
```


Request graceful shutdown without waiting


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-start) h. start()


```
start()
```


Start the sandbox. The returned local handle is attached; a cloud handle does not own the service-managed VM.


Returns


`Result<` [`Sandbox`](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-start_detached) h. start_detached()


```
start_detached()
```


Start in detached mode


Returns


`Result<` [`Sandbox`](https://docs.microsandbox.dev/sdk/rust/sandbox#instance-methods) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-wait_for_status) h. wait_for_status()


```
async fn wait_for_status(&self, status: SandboxStatus) -> MicrosandboxResult<SandboxHandle>
```


Wait without a built-in timeout until this exact sandbox reaches `status`, returning a refreshed handle. Returns `SandboxReplaced` rather than rebinding to a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-restart) h. restart()


```
async fn restart(&self) -> MicrosandboxResult<Sandbox>
```


Gracefully restart this exact sandbox with default options.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-restart_with) h. restart_with()


```
async fn restart_with(&self, options: RestartOptions) -> MicrosandboxResult<Sandbox>
```


Restart with explicit force, shutdown timeout, and detached-start controls. See [`sb.restart_with()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-restart_with) for state behavior and defaults.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-destroy) h. destroy()


```
async fn destroy(&self) -> MicrosandboxResult<()>
```


Gracefully stop and remove this exact sandbox. A stale handle cannot destroy a replacement that reused the name.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-destroy_with) h. destroy_with()


```
async fn destroy_with(&self, options: DestroyOptions) -> MicrosandboxResult<()>
```


Destroy with explicit force and shutdown-timeout controls. See [`sb.destroy_with()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-destroy_with) for defaults.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-status) h. status()


```
status()
```


Current status


Returns


[`SandboxStatus`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstatus)


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-stop) h. stop()


Different on cloud


```
stop()
```


Wait indefinitely for graceful completion and release of the same runtime’s ownership. No implicit kill; cancellation stops only the wait.


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-stop_with_timeout) h. stop_with_timeout()


Different on cloud


```
stop_with_timeout(timeout)
```


Same completion contract as `stop()` under one total budget. Expiry returns `MicrosandboxError::StopTimeout` without killing; `Duration::ZERO` expires before dispatch.


Returns


`Result<()>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-touch) h. touch()


Local-only


```
touch()
```


Explicitly refresh the sandbox idle timer


Returns


`Result<` [`SandboxTouchResult`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxtouchresult) `>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-updated_at) h. updated_at()


```
updated_at()
```


Last update timestamp


Returns


`Option<DateTime<Utc>>`


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#h-wait_until_stopped) h. wait_until_stopped()


```
wait_until_stopped()
```


Block until terminal state is observed


Returns


`Result<` [`SandboxStopResult`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstopresult) `>`


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secretpatchbuilder) SecretPatchBuilder


Used by [secret()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationbuilder-secret)


Builder for one declarative secret change.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-env) secret. env()


```
fn env(self, name: impl Into<String>) -> Self
```


Name the secret. This is the environment variable that exposes the placeholder inside the guest. **Required.**


Parameters


`name` impl Into<String> Secret name, usually the environment variable name.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-source) secret. source()


```
fn source(self, source: SecretSource) -> Self
```


Provide the secret material as a host-side [`SecretSource`](https://docs.microsandbox.dev/sdk/rust/sandbox#secretsource) reference. The durable config records only the reference, and the value is resolved host-side when the change applies. Mutually exclusive with `value(...)`.


Parameters


`source` [SecretSource](https://docs.microsandbox.dev/sdk/rust/sandbox#secretsource) Host-side reference for the secret material.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-value) secret. value()


```
fn value(self, value: impl Into<String>) -> Self
```


Provide the secret material as a raw value, for embedders that hold only a value. The value is zeroized on drop, redacted from `Debug`, and never enters the plan. Applying a value persists it into the durable config until a later source-based rotate migrates it to a reference, the same at-rest property as `secret_env()`. Mutually exclusive with `source(...)`.


Parameters


`value` impl Into<String> Raw secret value held by the embedding process.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-placeholder) secret. placeholder()


```
fn placeholder(self, placeholder: impl Into<String>) -> Self
```


Set the guest-visible placeholder. Placeholder changes cannot reach already-running processes, so they classify as `requires restart` on a running sandbox.


Parameters


`placeholder` impl Into<String> Guest-visible placeholder string.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-allow) secret. allow()


```
fn allow(self, host: impl Into<String>) -> Self
```


Add an allowed host pattern, such as `api.example.com`, `*.example.org`, or `*`. A non-empty list replaces the secret’s current allow-list; an empty list leaves it unchanged. A new secret needs at least one.


Parameters


`host` impl Into<String> Allowed exact host, wildcard host pattern, or `*`.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-substitution) secret. substitution()


```
fn substitution(self, value: SecretSubstitution) -> Self
```


Replace the enabled request locations for this secret. Omit this method to leave existing settings unchanged. At least one location must remain enabled. See [SecretSubstitution](https://docs.microsandbox.dev/sdk/rust/secrets#secretsubstitution) for defaults and protocol limits.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-allow_placeholder_for) secret. allow_placeholder_for()


```
fn allow_placeholder_for(self, host: impl Into<String>) -> Self
```


Add a destination allowed to receive the unchanged placeholder where substitution does not apply. `allow_passthrough_for()` remains a deprecated alias. This does not grant access to the real secret.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-violation_action) secret. violation_action()


```
fn violation_action(self, value: SecretViolationAction) -> Self
```


Set the per-secret blocking action. See [SecretViolationAction](https://docs.microsandbox.dev/sdk/rust/secrets#secretviolationaction).


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secret-require_tls_identity) secret. require_tls_identity()


```
fn require_tls_identity(self, value: bool) -> Self
```


Set whether substitution requires a verified TLS identity. Omit this method to retain the existing setting.


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#metrics-reports) Metrics reports


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#all_sandbox_metrics_reports_local) all_sandbox_metrics_reports_local()


```
async fn all_sandbox_metrics_reports_local(
    local: &LocalBackend,
    include_exited: bool,
) -> MicrosandboxResult<Vec<SandboxMetricsReport>>
```


Read local metrics joined with catalog context. Set `include_exited` to retain terminal samples until their registry slots are reused. Sandboxes removed from the catalog are always excluded. See [metrics behavior](https://docs.microsandbox.dev/sandboxes/metrics).


Example


```
use microsandbox::{all_sandbox_metrics_reports_local, LocalBackend};

let local = LocalBackend::lazy()?;

// All sandboxes; pass true to include exited ones.
let reports = all_sandbox_metrics_reports_local(&local, false).await?;
for r in &reports {
    println!("{} [{:?}] {:.2} cores of {:?}", r.name, r.state, r.metrics.cpu_percent / 100.0, r.cpus);
}
```


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox_metrics_report_local) sandbox_metrics_report_local()


```
async fn sandbox_metrics_report_local(
    local: &LocalBackend,
    name: &str,
) -> MicrosandboxResult<Option<SandboxMetricsReport>>
```


Read one sandbox’s report in any state, including exited sandboxes. Unlike [`metrics()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-metrics), this does not require a running sandbox. Returns `None` when the sandbox exists but has no registry slot, either because it was never sampled or the slot was reused. A missing sandbox returns `SandboxNotFound`.


Example


```
use microsandbox::{sandbox_metrics_report_local, LocalBackend};

let local = LocalBackend::lazy()?;
let report = sandbox_metrics_report_local(&local, "my-app").await?;
```


## [​](https://docs.microsandbox.dev/sdk/rust/sandbox#types) Types


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#logentry) LogEntry


Returned by [logs()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-logs)


A single captured log entry returned by [`logs()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-logs).


| Field | Type | Description |
| --- | --- | --- |
| timestamp | `DateTime<Utc>` | Wall-clock capture time on the host |
| source | [`LogSource`](https://docs.microsandbox.dev/sdk/rust/sandbox#logsource) | Where the chunk came from |
| session_id | `Option<u64>` | Relay-monotonic session id; `None` for `System` entries |
| data | `Bytes` | The chunk’s bytes (UTF-8 lossy decoded by default; raw bytes if `--raw` mode was used) |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#loglevel) LogLevel


Used by [log_level()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-log_level)


Sandbox process log verbosity.


| Value | Description |
| --- | --- |
| `Error` | Errors only |
| `Warn` | Warnings and errors only |
| `Info` | Info and higher |
| `Debug` | Debug and higher |
| `Trace` | Most verbose, all diagnostic output |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#logoptions) LogOptions


Used by [logs()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-logs)


Filters passed to [`logs()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-logs). All fields optional. `LogOptions::default()` returns everything for the default sources (`Stdout` + `Stderr` + `Output`).


| Field | Type | Description |
| --- | --- | --- |
| tail | `Option<usize>` | Show only the last N entries after other filters apply |
| since | `Option<DateTime<Utc>>` | Inclusive lower bound on entry timestamp |
| until | `Option<DateTime<Utc>>` | Exclusive upper bound on entry timestamp |
| sources | `Vec<` [`LogSource`](https://docs.microsandbox.dev/sdk/rust/sandbox#logsource) `>` | Sources to include. Empty = `[Stdout, Stderr, Output]` (the default user-program sources). Add `System` to merge runtime/kernel diagnostics. |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#logsource) LogSource


Used by [LogEntry.source](https://docs.microsandbox.dev/sdk/rust/sandbox#logentry) · [LogOptions.sources](https://docs.microsandbox.dev/sdk/rust/sandbox#logoptions)


Tag indicating where a captured log entry came from.


| Value | Description |
| --- | --- |
| `Stdout` | Captured from a session’s stdout (pipe mode; streams stayed separated) |
| `Stderr` | Captured from a session’s stderr (pipe mode) |
| `Output` | Captured from a session running in pty mode. PTY allocation merges stdout and stderr at the kernel level inside the guest, so they arrive as a single stream, tagged `Output` rather than mislabeled as `Stdout`. |
| `System` | Synthetic entry: lifecycle markers in `exec.log` plus runtime/kernel diagnostic lines merged in at read time when `System` is requested. |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxpingresult) SandboxPingResult


Returned by [ping()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-ping) · [SandboxHandle.ping()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle)


Result of a successful agent reachability check.


| Field | Type | Description |
| --- | --- | --- |
| name | `String` | Sandbox name that was pinged |
| latency | `Duration` | SDK-measured round-trip latency |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxtouchresult) SandboxTouchResult


Returned by [touch()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-touch) · [SandboxHandle.touch()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle)


Result of an explicit idle-timer refresh.


| Field | Type | Description |
| --- | --- | --- |
| name | `String` | Sandbox name that was touched |
| activity_seq | `u64` | Agent activity sequence after the touch was recorded |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#pullpolicy) PullPolicy


Used by [pull_policy()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-pull_policy)


Controls when the SDK fetches an OCI image from the registry.


| Value | Description |
| --- | --- |
| `Always` | Pull the image every time, even if cached locally |
| `IfMissing` | Pull only if the image is not already cached. This is the default. |
| `Never` | Never pull; fail if the image is not cached locally |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#registryauth) RegistryAuth


Used by [registry()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-registry)


Credentials for authenticating to a private container registry.


| Variant | Fields | Description |
| --- | --- | --- |
| `Basic` | - `username: String` - `password: String` | Username and password authentication |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxconfig) SandboxConfig


Returned by [config()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-config) · [build()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-build)


The full configuration of a sandbox. Obtained via [`config()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-config) or built via [`SandboxBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder). Contains all settings used to create the sandbox.


| Field | Type | Description |
| --- | --- | --- |
| cpus | `u8` | Number of virtual CPUs |
| env | `Vec<(String, String)>` | Environment variables |
| idle_timeout_secs | `Option<u64>` | Idle timeout |
| image | `RootfsSource` | Root filesystem source (OCI, bind, or disk image) |
| max_duration_secs | `Option<u64>` | Maximum lifetime |
| max_cpus | `u8` | Boot-time maximum possible virtual CPUs |
| max_memory_mib | `u32` | Boot-time maximum hotpluggable memory in MiB |
| memory_mib | `u32` | Guest memory in MiB |
| name | `String` | Sandbox name, up to 128 UTF-8 bytes |
| patches | `Vec<Patch>` | Rootfs patches |
| scripts | `Vec<(String, String)>` | Named scripts |
| shell | `Option<String>` | Shell for `shell()` calls |
| volumes | `Vec<VolumeMount>` | Volume mounts |
| workdir | `Option<String>` | Default working directory |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxpage) SandboxPage


One stable, newest-first page returned by [`Sandbox::list()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist) or [`Sandbox::list_with()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxlist_with).


| Field | Type | Description |
| --- | --- | --- |
| `sandboxes` | `Vec<SandboxHandle>` | Handles in this page |
| `next_cursor` | `Option<String>` | Opaque continuation cursor, or `None` on the final page |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan) SandboxModificationPlan


Returned by [dry_run()](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-dry_run) · [apply()](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-apply)


Dry-run or apply plan for a sandbox modification. Values never appear in a plan: secret entries carry only guest-visible references.


| Field | Type | Description |
| --- | --- | --- |
| sandbox | `String` | Sandbox being modified |
| status | `String` | Sandbox status used for classification (`"running"`, `"stopped"`, …) |
| applied | `bool` | Whether the changes were applied; `false` for dry runs |
| policy | `ModificationPolicy` | Policy used to produce the plan: `NoRestart` (default), `NextStart`, or `Restart` |
| changes | `Vec<` [`PlannedChange`](https://docs.microsandbox.dev/sdk/rust/sandbox#plannedchange) `>` | Planned changes, one entry per field or secret |
| conflicts | `Vec<ModificationConflict>` | Conflicts (`field` + `message`) that must be resolved before the patch can apply |
| warnings | `Vec<ModificationWarning>` | Non-fatal warnings (`field` + `message`) about the patch or current runtime capabilities, e.g. the future-execs-only env caveat |
| resize_status | `Vec<` [`ResourceResizeStatus`](https://docs.microsandbox.dev/sdk/rust/sandbox#resourceresizestatus) `>` | Live resource resize outcomes, populated by `apply()` when a live change ran |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secretsource) SecretSource


Used by [SecretPatchBuilder.source()](https://docs.microsandbox.dev/sdk/rust/sandbox#secretpatchbuilder-source)


Host-side source for secret material. The source is resolved when the modification applies, and plans only show guest-visible references.
Import path: `microsandbox::sandbox::SecretSource`.


| Variant | Field | Description |
| --- | --- | --- |
| `Env` | `var: String` | Read the value from a host environment variable at apply time |
| `Store` | `reference: String` | Reserved for a host-side secret store reference; current modifiers report it as unsupported |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#plannedchange) PlannedChange


Used by [SandboxModificationPlan.changes](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan)


One planned modification entry. This enum has a `Config` variant for ordinary configuration fields and a `Secret` variant for secret changes.


| Variant | Type | Description |
| --- | --- | --- |
| `Config` | [`ConfigPlannedChange`](https://docs.microsandbox.dev/sdk/rust/sandbox#configplannedchange) | Ordinary config change |
| `Secret` | [`SecretPlannedChange`](https://docs.microsandbox.dev/sdk/rust/sandbox#secretplannedchange) | Secret change. Values are omitted by construction; references are guest-visible only |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#configplannedchange) ConfigPlannedChange


Variant of [PlannedChange::Config](https://docs.microsandbox.dev/sdk/rust/sandbox#plannedchange)


Ordinary configuration change in a modification plan.


| Field | Type | Description |
| --- | --- | --- |
| field | `String` | Config field being changed |
| change | `ChangeKind` | `Added`, `Updated`, or `Removed` |
| before | `Option<String>` | Previous safe visible state |
| after | `Option<String>` | New safe visible state |
| disposition | [`ModificationDisposition`](https://docs.microsandbox.dev/sdk/rust/sandbox#modificationdisposition) | When or whether the change can take effect |
| reason | `Option<String>` | Human-readable reason for the classification, when useful |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#secretplannedchange) SecretPlannedChange


Variant of [PlannedChange::Secret](https://docs.microsandbox.dev/sdk/rust/sandbox#plannedchange)


Secret change in a modification plan. Values are omitted by construction; `before_ref` and `after_ref` are guest-visible references.


| Field | Type | Description |
| --- | --- | --- |
| field | `String` | Always `"secret"` |
| name | `String` | Stable secret identity, usually the environment variable name |
| change | `SecretChangeKind` | `Added`, `Rotated`, `Removed`, `Renamed`, `HostsUpdated`, or `PlaceholderUpdated` |
| before_ref | `Option<String>` | Previous guest-visible reference or placeholder |
| after_ref | `Option<String>` | New guest-visible reference or placeholder |
| disposition | [`ModificationDisposition`](https://docs.microsandbox.dev/sdk/rust/sandbox#modificationdisposition) | When or whether the change can take effect |
| allow_hosts | `Vec<String>` | Allowed hosts after the requested change |
| reason | `Option<String>` | Human-readable reason for the classification, when useful |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#modificationdisposition) ModificationDisposition


Used by [ConfigPlannedChange.disposition](https://docs.microsandbox.dev/sdk/rust/sandbox#configplannedchange) · [SecretPlannedChange.disposition](https://docs.microsandbox.dev/sdk/rust/sandbox#secretplannedchange)


When or whether a planned change can take effect. Serializes as the quoted strings below.


| Value | Description |
| --- | --- |
| `Live` (`"live"`) | Applies to the running VM now |
| `NextStart` (`"next start"`) | Persists to the desired config and applies the next time the sandbox starts |
| `RequiresRestart` (`"requires restart"`) | Needs a restart before it can take effect; `apply()` refuses it unless the [`restart()`](https://docs.microsandbox.dev/sdk/rust/sandbox#modification-restart) policy is selected |
| `Unsupported` (`"unsupported"`) | Cannot be changed by `modify` |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#resourceresizestatus) ResourceResizeStatus


Used by [SandboxModificationPlan.resize_status](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmodificationplan)


Runtime convergence status for a live resource resize. Enforcement applies immediately; the guest converges asynchronously (onlining CPUs, plugging memory blocks).


| Field | Type | Description |
| --- | --- | --- |
| resource | `ResourceKind` | `Cpus` or `Memory` |
| requested | `String` | Requested value |
| actual | `String` | Actual value observed in the guest/runtime |
| enforced | `String` | Host/VMM-enforced value |
| state | `ResourceConvergenceState` | Convergence state, see below |


| State | Description |
| --- | --- |
| `Accepted` | The runtime accepted the request |
| `Converging` | The guest and VMM are still converging on the requested state |
| `Applied` | Desired, actual, and enforced state match |
| `GuestRefused` | The guest would not cooperate; the host enforces the new limit anyway |
| `Failed` | The resize failed |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstopresult) SandboxStopResult


Observed terminal sandbox state returned by [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-wait_until_stopped).


| Field | Type | Description |
| --- | --- | --- |
| name | `String` | Sandbox name |
| status | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstatus) | Terminal status that was observed |
| exit_code | `Option<i32>` | Process exit code when available from an owned child process |
| signal | `Option<i32>` | Terminating signal when available from an owned child process |
| observed_at | `DateTime<Utc>` | When the terminal state was observed |
| source | `Option<String>` | Description of the observation source |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetrics) SandboxMetrics


Returned by [metrics()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-metrics) · [metrics_stream()](https://docs.microsandbox.dev/sdk/rust/sandbox#sb-metrics_stream)


Point-in-time resource usage snapshot.


| Field | Type | Description |
| --- | --- | --- |
| cpu_percent | `f32` | CPU usage as a percentage |
| disk_read_bytes | `u64` | Total bytes read from disk since boot |
| disk_write_bytes | `u64` | Total bytes written to disk since boot |
| memory_bytes | `u64` | Current memory usage in bytes |
| memory_limit_bytes | `u64` | Memory limit in bytes |
| net_rx_bytes | `u64` | Total bytes received over the network since boot |
| net_tx_bytes | `u64` | Total bytes sent over the network since boot |
| upper_used_bytes | `Option<u64>` | Guest-visible OCI upper filesystem used bytes when the protected reporter is available and fresh |
| upper_free_bytes | `Option<u64>` | Guest-visible OCI upper filesystem free bytes when the protected reporter is available and fresh |
| upper_host_allocated_bytes | `Option<u64>` | Host-allocated bytes for the writable OCI upper image when available |
| timestamp | `DateTime<Utc>` | When this measurement was taken |
| uptime | `Duration` | Time since the sandbox was created |


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetricsreport) SandboxMetricsReport


`name` String Sandbox name. `sandbox_id` i32 Catalog sandbox ID. `run_id` i32 Catalog run ID that produced the sample. `state` SandboxMetricsState Report state; see [SandboxMetricsState](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetricsstate). `cpus` Option<u32> vCPUs from the active catalog configuration, when resolvable. `metrics` SandboxMetrics Metrics sample. Its memory limit comes from live sizing, falling back to the active configuration when unavailable, so live resizes are reflected.


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxmetricsstate) SandboxMetricsState


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#running) Running


The runtime owns its slot, is alive, and its sample is fresh.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#stalled) Stalled


The runtime is alive, but no sample has arrived within three sampling intervals.


#### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#exited) Exited


The preserved terminal sample of a stopped sandbox; this is not a live reading.


### [​](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxstatus) SandboxStatus


Used by [SandboxHandle.status()](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxhandle)


| Value | Description |
| --- | --- |
| `Created` | Persisted resource exists but has not started |
| `Starting` | Runtime is booting and the guest agent is not ready yet |
| `Running` | Guest agent is ready; `exec`, `shell`, and `fs` work |
| `Draining` | Graceful shutdown in progress; existing commands finish and new ones are rejected |
| `Paused` | VM is paused |
| `Stopped` | VM shut down; configuration persisted; can be restarted |
| `Crashed` | VM exited unexpectedly (kernel panic, OOM, etc.) |


Was this page helpful?

Yes No ⌘ I

---

# Python SDK Sandbox reference

`https://docs.microsandbox.dev/sdk/python/sandbox`

See [Overview](https://docs.microsandbox.dev/sandboxes/overview) for configuration examples and [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle) for state management.

See [Snapshots](https://docs.microsandbox.dev/sdk/python/snapshots#forking) for live fork methods.


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox) Sandbox
## Documentation Index
## ​Sandbox
## ​Patch
## ​SandboxHandle
*Returned by Sandbox.get() · Sandbox.list() · Sandbox.list_with()*

## ​MetricsStream
*Returned by metrics_stream()*

## ​LogEntry
*Returned by logs() · iterated from LogStream*

## ​LogStream
*Returned by log_stream()*

## ​PullSession
*Returned by create_with_progress()*

## ​Types











Instance properties


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-owns_lifecycle) sb. owns_lifecycle


```
@property
async def owns_lifecycle(self) -> bool
```


Whether this handle owns the sandbox lifecycle. Local attached sandboxes returned by [`create()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) or [`start()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-start) own lifecycle. Local detached sandboxes, cloud sandboxes, and handles upgraded via [`SandboxHandle.connect()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) return `False`. This is an async property; use `await sb.owns_lifecycle`.


Returns


bool `True` if this handle owns the lifecycle.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-fs) sb. fs


```
@property
def fs(self) -> SandboxFsOps
```


Example


```
await sb.fs.write("/tmp/hello.txt", b"hi")
```


Get a filesystem handle for reading and writing files inside the running sandbox. This is a synchronous property; use `sb.fs` (no `await`). See [Filesystem](https://docs.microsandbox.dev/sdk/python/filesystem) for API details.


Returns


[SandboxFsOps](https://docs.microsandbox.dev/sdk/python/filesystem) Filesystem handle.


Static methods


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) Sandbox. create()


Limited on cloud


```
@staticmethod
async def create(name: str, **kwargs) -> Sandbox
```


Example


```
async with await Sandbox.create("my-sandbox", image="alpine") as sb:
    output = await sb.shell("echo hello")
    print(output.stdout_text)
# Local sandbox is automatically killed and removed on exit
```


Create and boot a sandbox. Keyword arguments provide individual config fields; see [`SandboxConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig) for the full set. Pulls the image if needed, boots the VM, starts the guest agent, and waits until it is ready to accept commands. Sandbox names must be non-empty and no longer than 128 UTF-8 bytes.
The returned `Sandbox` is an async context manager. On the local backend, `async with` guarantees cleanup: exit kills the sandbox and removes its persisted state. Cloud handles do not own the host process, so stop or remove them explicitly before leaving the context.
Pass `intercept_tls=True` to enable [TLS interception](https://docs.microsandbox.dev/networking/tls) while preserving supplied network settings. `False` leaves them unchanged.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes. `**kwargs` [SandboxConfig](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig) Configuration fields: `image`, `cpus`, `memory`, `volumes`, `ports`, `network`, `proxy`, `secrets`, `detached`, and more.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods) Running sandbox, usable as an async context manager.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create_with_progress) Sandbox. create_with_progress()


Limited on cloud


```
@staticmethod
def create_with_progress(name: str, **kwargs) -> PullSession
```


Example


```
session = Sandbox.create_with_progress("my-sandbox", image="ubuntu:latest")
async with session:
    async for event in session.progress:
        print(event.event_type)
    sb = await session.result()
```


Same parameters as [`create()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) but returns a [`PullSession`](https://docs.microsandbox.dev/sdk/python/sandbox#pullsession) that reports image preparation and local startup. This factory is synchronous; the async work happens through the session. Startup events have `event_type == PullEventType.STARTUP`, with `phase`, `completed_bytes`, and optional `total_bytes`. They distinguish backing preparation, cache waits/reuse, syncing, and activation. Preparation does not consume the activation timeout. Ignoring progress does not cancel creation; await `session.result()` for the outcome.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes. `**kwargs` [SandboxConfig](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig) Same configuration fields as [create()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create).


Returns


[PullSession](https://docs.microsandbox.dev/sdk/python/sandbox#pullsession) Session for tracking pull progress and obtaining the final sandbox.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-connect_or_create) Sandbox. connect_or_create()


```
@staticmethod
async def connect_or_create(name: str, **kwargs) -> Sandbox
```


Reuse or create the sandbox with this name. The method connects when it is running, waits while it is starting, starts it when it is created, stopped, or crashed, and creates it only when the name is unused. Keyword arguments apply only to a new sandbox. Concurrent callers reuse the same sandbox. Passing `replace=True` or `replace_with_timeout` raises an invalid-configuration error.


Parameters


- `name`: reusable sandbox name, up to 128 UTF-8 bytes.
- `**kwargs`: the same creation fields accepted by [`Sandbox.create()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create), used only if creation is necessary.


Returns


[`Sandbox`](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods)


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-start) Sandbox. start()


```
@staticmethod
async def start(name: str, *, detached: bool = False) -> Sandbox
```


Example


```
sb = await Sandbox.start("api")
```


Restart a previously stopped sandbox. The VM reboots using the persisted configuration.


Parameters


`name` str Name of a stopped sandbox, up to 128 UTF-8 bytes. `detached` bool When `True`, the sandbox survives after your process exits. Default `False`.


Returns


[Sandbox](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-get) Sandbox. get()


```
@staticmethod
async def get(name: str) -> SandboxHandle
```


Example


```
handle = await Sandbox.get("api")
print(handle.status)
```


Get a handle to an existing sandbox (running or stopped). The handle provides status, configuration, and lifecycle control without requiring a full connection to the guest agent.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes.


Returns


[SandboxHandle](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) Handle with status and lifecycle control.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list) Sandbox. list()


```
@staticmethod
async def list() -> SandboxPage
```


Example


```
page = await Sandbox.list()
for h in page.sandboxes:
    print(h.name, h.status)
```


Return the first page of sandboxes (running, stopped, and crashed), ordered newest first. The default page size is 20.


Returns


SandboxPage Handles in this page and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list_with) Sandbox. list_with()


```
@staticmethod
async def list_with(
    *,
    cursor: str | None = None,
    limit: int | None = None,
    labels: Mapping[str, str] | None = None,
) -> SandboxPage
```


Example


```
page = await Sandbox.list_with(limit=50, labels={"role": "worker"})
if page.next_cursor is not None:
    next_page = await Sandbox.list_with(
        cursor=page.next_cursor,
        limit=50,
        labels={"role": "worker"},
    )
```


Return a configured page of sandboxes. Label filters are applied before pagination and match every supplied key/value pair.


Parameters


`cursor` str | None Opaque `next_cursor` from the preceding page. `limit` int | None Page size from 1 through 100. Defaults to 20. `labels` Mapping[str, str] | None Label key/value pairs to match. `None` returns every sandbox, like [list()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list).


Returns


SandboxPage Matching handles and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-remove) Sandbox. remove()


```
@staticmethod
async def remove(name: str) -> None
```


Example


```
await Sandbox.remove("api")
```


Delete a stopped sandbox by name. See [Destroy or remove](https://docs.microsandbox.dev/sandboxes/lifecycle#destroy-or-remove) for the exact local deletion scope and the external resources that are preserved. Fails if the sandbox is still running; stop it first.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes.


Instance methods


Command execution (`exec`, `exec_stream`, `shell`, `shell_stream`) is documented on the [Execution](https://docs.microsandbox.dev/sdk/python/execution) page; SSH (`ssh`) on the [SSH](https://docs.microsandbox.dev/sdk/python/ssh) page. The lifecycle, attach, metrics, and logs methods follow.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-name) sb. name()


```
async def name(self) -> str
```


Example


```
print(await sb.name())
```


Return the sandbox name.


Returns


str Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-id) sb. id


```
identity: str = await sb.id
```


Await the opaque stable identity of this persisted sandbox. It remains unchanged across stop and restart and changes when the reusable name is removed and recreated. Use it for equality, logging, and correlation; do not parse it.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-attach) sb. attach()


```
async def attach(
    self,
    cmd: str,
    args: list[str] | None = None,
    *,
    cwd: str | None = None,
    user: str | None = None,
    env: Mapping[str, str] | None = None,
    detach_keys: str | None = None,
) -> int
```


Example


```
code = await sb.attach("python", ["-i"])
```


Bridge your terminal directly to a process inside the sandbox for a fully interactive PTY session. Returns the process exit code once the session ends.


Parameters


`cmd` str Command to run. `args` list[str] | None Command arguments. `cwd` str | None Working directory. `user` str | None Guest user. `env` Mapping[str, str] | None Environment variables. `detach_keys` str | None Custom detach key sequence.


Returns


int Exit code of the process.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-attach_shell) sb. attach_shell()


```
async def attach_shell(self) -> int
```


Example


```
await sb.attach_shell()
```


Attach your terminal to the sandbox’s default shell for an interactive session.


Returns


int Exit code.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-ping) sb. ping()


Local-only


```
async def ping(self) -> SandboxPingResult
```


Example


```
health = await sb.ping()
print(f"{health.name}: {health.latency_ms:.1f} ms")
```


Check that the running sandbox’s guest agent is reachable without refreshing idle activity. This sends `core.ping` and waits for `core.pong`; it does not start stopped sandboxes and raises an error if the sandbox is not running or `agentd` cannot respond. After upgrading from a runtime that predates protocol generation 6, restart already-running sandboxes so the guest agent understands the message.


Returns


[SandboxPingResult](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxpingresult) Sandbox name and agent round-trip latency.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-touch) sb. touch()


Local-only


```
async def touch(self) -> SandboxTouchResult
```


Example


```
keepalive = await sb.touch()
print(f"{keepalive.name}: {keepalive.activity_seq}")
```


Explicitly refresh the running sandbox’s idle activity. This sends `core.touch`, receives `core.touched`, and advances the guest activity sequence used by the runtime idle-timeout monitor. It does not start stopped sandboxes and it does not bypass `max_duration`.


Returns


[SandboxTouchResult](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxtouchresult) Sandbox name and updated activity sequence.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-modify) sb. modify()


Local-only


```
async def modify(
    self,
    *,
    cpus: int | None = None,
    max_cpus: int | None = None,
    memory: int | None = None,
    max_memory: int | None = None,
    root_disk_size: int | None = None,
    env: Mapping[str, str] | None = None,
    env_rm: list[str] | None = None,
    labels: Mapping[str, str] | None = None,
    labels_rm: list[str] | None = None,
    workdir: str | None = None,
    secrets: Mapping[str, SecretModifySpec] | None = None,
    secrets_rm: list[str] | None = None,
    policy: ModificationPolicy | None = None,
    dry_run: bool = False,
) -> SandboxModificationPlan
```


Example


```
from microsandbox import (
    ModificationDisposition,
    ModificationPolicy,
    ResourceConvergenceState,
)

# Live resize: applies to the running VM when within the booted capacity
plan = await sb.modify(cpus=4, memory=4096)
for r in plan.get("resize_status", []):
    if r["state"] is ResourceConvergenceState.APPLIED:
        print(f'{r["resource"]}: {r["requested"]} -> {r["actual"]}')

# Preview a change without applying it
plan = await sb.modify(max_memory=16384, dry_run=True)
for change in plan["changes"]:
    if change["disposition"] is ModificationDisposition.REQUIRES_RESTART:
        print(f'{change["field"]} needs a restart')

# Make an env change active now by restarting
await sb.modify(env={"MODE": "prod"}, policy=ModificationPolicy.RESTART)

# Grow the owned OCI root disk while it is running
await sb.modify(root_disk_size=8192)

# Add or rotate a host-environment secret; restart if it is newly added
await sb.modify(
    secrets={
        "API_KEY": {
            "env": "API_KEY",
            "allowed_hosts": ["api.example.com"],
        },
    },
    policy=ModificationPolicy.RESTART,
)

# Remove an existing secret
await sb.modify(secrets_rm=["OLD_API_KEY"])
```


Plan or apply a configuration change. The returned plan uses [`ModificationDisposition`](https://docs.microsandbox.dev/sdk/python/sandbox#modificationdisposition) to classify when each change takes effect.
`cpus` and `memory` resize live within the `max_cpus` / `max_memory` ceilings; raising a ceiling requires a restart.
`root_disk_size` grows owned managed and flat ext4 roots live, including checkpoint-backed roots, tmpfs root disks can change in either direction on the next boot, and user-supplied disk images are rejected.
Env and workdir changes affect future execs only. Stopped roots grow before the new size is saved. Explicit restart and next-start policies remain available.
Secrets are keyed by name. Each `SecretModifySpec` can set one source (`env`, `value`, or `store`) and optional settings listed below. Omitted fields stay unchanged. Plans never include secret values. Use `secrets_rm` to remove secrets.
Changing a secret’s substitution rules, violation action, TLS identity requirement, or placeholder passthrough hosts requires a restart if the sandbox is running. Use `policy=ModificationPolicy.RESTART` to apply now, or `policy=ModificationPolicy.NEXT_START` to save for the next start. Omitted options keep their current settings.
The returned [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmodificationplan) is a typed dictionary:


| Key | Type | Description |
| --- | --- | --- |
| `sandbox` | `str` | Sandbox being modified |
| `status` | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstatus) | Status used for classification |
| `applied` | `bool` | Whether the changes were applied; `False` with `dry_run=True` |
| `policy` | [`ModificationPolicy`](https://docs.microsandbox.dev/sdk/python/sandbox#modificationpolicy) | Policy used to produce the plan |
| `changes` | `list[ConfigPlannedChange | SecretPlannedChange]` | Typed config or secret changes, discriminated by [`PlannedChangeKind`](https://docs.microsandbox.dev/sdk/python/sandbox#plannedchangekind) |
| `conflicts` | `list[dict]` | Conflicts (`field` + `message`) that must be resolved before the patch can apply |
| `warnings` | `list[dict]` | Non-fatal warnings (`field` + `message`), e.g. the future-execs-only env caveat |
| `resize_status` | `list[ResourceResizeStatus]` | Live resize outcomes after apply, using [`ResourceKind`](https://docs.microsandbox.dev/sdk/python/sandbox#resourcekind) and [`ResourceConvergenceState`](https://docs.microsandbox.dev/sdk/python/sandbox#resourceconvergencestate). Omitted when no live resize ran |


A live CPU or memory resize can take a moment to settle. The new limits are enforced immediately, and `resize_status` reports when the sandbox has finished adjusting.


Parameters


`cpus` int | None Desired effective vCPU count. Live when within the booted `max_cpus`. `max_cpus` int | None Boot-time maximum possible vCPUs (restart-backed). `memory` int | None Desired effective guest memory in MiB. Live when within the booted `max_memory`. `max_memory` int | None Boot-time maximum hotpluggable memory in MiB (restart-backed). `root_disk_size` int | None Desired root disk size in MiB. Managed and flat OCI disks are grow-only; applies on restart or next start. `env` Mapping[str, str] | None Environment variables to set for future execs. `env_rm` list[str] | None Environment variable keys to remove. `labels` Mapping[str, str] | None Labels to set. `labels_rm` list[str] | None Label keys to remove. `workdir` str | None Working directory for future execs. `secrets` Mapping[str, SecretModifySpec] | None Desired secret specs keyed by secret name. Each spec may contain at most one of `env`, `value`, or `store`, plus optional `placeholder` and `allowed_hosts`. `secrets_rm` list[str] | None Secret names to remove explicitly. `policy` [ModificationPolicy | None](https://docs.microsandbox.dev/sdk/python/sandbox#modificationpolicy) `NO_RESTART` (default) applies only changes that can complete without restarting; `NEXT_START` persists changes for the next start without mutating a running VM; `RESTART` restarts if needed so restart-required changes become active now. `dry_run` bool When `True`, compute the plan without applying anything. Default `False`.


Returns


[SandboxModificationPlan](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmodificationplan) The modification plan, applied unless `dry_run=True`.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-metrics) sb. metrics()


Local-only


```
async def metrics(self) -> SandboxMetrics
```


Example


```
m = await sb.metrics()
print(f"cpu {m.cpu_percent:.1f}% · mem {m.memory_bytes // 1_048_576} MiB")
```


Get a point-in-time snapshot of the sandbox’s resource usage: CPU, memory, disk I/O, network I/O, optional upper disk usage, and uptime.


Returns


[SandboxMetrics](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics) Resource metrics.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-metrics_stream) sb. metrics_stream()


Local-only


```
async def metrics_stream(self, interval: float = 1.0) -> MetricsStream
```


Example


```
stream = await sb.metrics_stream(1.0)
async for snapshot in stream:
    print(f"{snapshot.cpu_percent:.1f}%")
```


Stream resource metrics at a regular interval. The returned [`MetricsStream`](https://docs.microsandbox.dev/sdk/python/sandbox#metricsstream) supports both `recv()` and `async for`.


Parameters


`interval` float Seconds between metric snapshots. Default `1.0`.


Returns


[MetricsStream](https://docs.microsandbox.dev/sdk/python/sandbox#metricsstream) Async stream yielding a snapshot each interval.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-logs) sb. logs()


Local-only


```
async def logs(
    self,
    tail: int | None = None,
    since_ms: float | None = None,
    until_ms: float | None = None,
    sources: list[LogReadSource] | None = None,
) -> list[LogEntry]
```


Example


```
import time
from microsandbox import LogReadSource, Sandbox

handle = await Sandbox.get("web")

# Default: all user-program output, regardless of pipe/pty mode
entries = await handle.logs()
for e in entries:
    label = {"stdout": "OUT", "stderr": "ERR", "output": "PTY", "system": "SYS"}[e.source]
    print(f"[{e.timestamp_ms / 1000:.3f}] {label} {e.session_id}: {e.text().rstrip()}")

# Filtered: last 50 entries from the past hour, including system lines
recent = await handle.logs(
    tail=50,
    since_ms=(time.time() - 3600) * 1000,
    sources=[
        LogReadSource.STDOUT,
        LogReadSource.STDERR,
        LogReadSource.OUTPUT,
        LogReadSource.SYSTEM,
    ],
)
```


Read captured output from the sandbox’s `exec.log`. Backed by an on-disk JSON Lines file the runtime writes via the relay tap. Works on running and stopped sandboxes alike; there is no protocol traffic. The same method is available on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) for callers that don’t want to start the sandbox first.
The default sources are `STDOUT`, `STDERR`, and `OUTPUT` (PTY-merged). Add `LogReadSource.SYSTEM` to include synthetic lifecycle markers and runtime/kernel diagnostic lines, or use `LogReadSource.ALL` as shorthand for all four. Timestamps are exposed as `float` ms since the Unix epoch (UTC) for parity with [`SandboxMetrics.timestamp_ms`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics).


Parameters


`tail` int | None Show only the last N entries after other filters apply. `since_ms` float | None Inclusive lower bound on entry timestamp (ms since epoch). `until_ms` float | None Exclusive upper bound on entry timestamp (ms since epoch). `sources` [list[LogReadSource] | None](https://docs.microsandbox.dev/sdk/python/sandbox#logreadsource) Sources to include. `None` selects `STDOUT`, `STDERR`, and `OUTPUT`. Add `SYSTEM` to merge runtime/kernel diagnostics, or use `ALL` for all four.


Returns


[list[LogEntry]](https://docs.microsandbox.dev/sdk/python/sandbox#logentry) Matching entries in chronological order.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-log_stream) sb. log_stream()


Limited on cloud


```
async def log_stream(
    self,
    sources: list[LogReadSource] | None = None,
    since_ms: float | None = None,
    from_cursor: str | None = None,
    until_ms: float | None = None,
    follow: bool = False,
) -> LogStream
```


Example


```
stream = await sb.log_stream(follow=True)
async for entry in stream:
    print(entry.text().rstrip())
```


Stream captured log entries as a [`LogStream`](https://docs.microsandbox.dev/sdk/python/sandbox#logstream). With `follow=True` the stream stays open and yields new entries as they are written, like `tail -f`. Resume an earlier stream by passing the [`cursor`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry) of the last entry you saw as `from_cursor`. Also available on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle).


Parameters


`sources` [list[LogReadSource] | None](https://docs.microsandbox.dev/sdk/python/sandbox#logreadsource) Sources to include. Same semantics as [logs()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-logs). `since_ms` float | None Inclusive lower bound on entry timestamp (ms since epoch). `from_cursor` str | None Resume after this opaque cursor (from a prior [LogEntry.cursor](https://docs.microsandbox.dev/sdk/python/sandbox#logentry)). `until_ms` float | None Exclusive upper bound on entry timestamp (ms since epoch). `follow` bool When `True`, keep the stream open and yield new entries as they arrive. Default `False`.


Returns


[LogStream](https://docs.microsandbox.dev/sdk/python/sandbox#logstream) Async stream of log entries.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-stop) sb. stop()


Different on cloud


```
async def stop(self, timeout: float | None = None) -> None
```


Example


```
await sb.stop()
```


Wait indefinitely for graceful shutdown and release of the targeted runtime’s ownership. Success allows immediate removal. Cancelling the await does not kill the sandbox or undo a delivered shutdown request. Paused or unreachable sandboxes return errors; resume or kill explicitly. The optional `timeout` retains its call syntax and uses the same total budget as `stop_with_timeout()`.


Parameters


`timeout` float | None Total graceful-completion budget in seconds. `None` waits indefinitely; expiry raises `StopTimeoutError` without killing.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-stop_with_timeout) sb. stop_with_timeout()


```
async def stop_with_timeout(self, timeout: float) -> None
```


Use `await sb.stop_with_timeout(seconds)` for an explicit total graceful-completion budget. Expiry raises `StopTimeoutError`; zero expires before dispatch. A delivered request may finish later, but the timeout never requests force termination.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-request_stop) sb. request_stop()


```
async def request_stop(self) -> None
```


Example


```
await sb.request_stop()
```


Request graceful shutdown and return once the request is sent, without waiting for stopped state. Pair with [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_until_stopped) when the caller needs to observe the terminal state.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-kill) sb. kill()


Local-only


```
async def kill(self, timeout: float | None = None) -> None
```


Example


```
await sb.kill()  # SIGKILL, no graceful shutdown
```


Force-terminate the sandbox and wait until stopped state is observed. No graceful shutdown; use when the sandbox is unresponsive. Pending writes that the workload hasn’t `fsync`’d may be lost, same durability semantics as a sudden power loss on a physical machine. Prefer [`stop()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-stop) for graceful shutdown that gives the workload a chance to flush.


Parameters


`timeout` float | None Seconds to wait for the stopped state to be observed.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-request_kill) sb. request_kill()


Local-only


```
async def request_kill(self) -> None
```


Example


```
await sb.request_kill()
```


Request force termination and return once the signal is sent, without waiting for stopped state.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-request_drain) sb. request_drain()


Local-only


```
async def request_drain(self) -> None
```


Example


```
await sb.request_drain()
```


Request a graceful drain and return once the request is sent. Existing commands run to completion, but new `exec` calls are rejected; the sandbox transitions to stopped when all in-flight commands finish. Useful for zero-downtime rotation of worker sandboxes. Use [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_until_stopped) when the caller needs stopped-state observation.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_until_stopped) sb. wait_until_stopped()


```
async def wait_until_stopped(self) -> SandboxStopResult
```


Example


```
result = await sb.wait_until_stopped()
print(result.status, result.exit_code)
```


Block until the sandbox is observed in a terminal non-running state, without triggering a stop or kill request.


Returns


[SandboxStopResult](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstopresult) Terminal status and optional observed exit code.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_for_status) sb. wait_for_status()


```
async def wait_for_status(self, status: SandboxStatus) -> SandboxHandle
```


Wait without a built-in timeout until this exact sandbox reaches `status`, returning a refreshed metadata handle. Raises `SandboxReplacedError` rather than following a reused name. Wrap the coroutine with `asyncio.wait_for()` when a deadline is required.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-restart) sb. restart()


```
async def restart(
    self,
    *,
    force: bool = False,
    timeout: float | None = None,
    detached: bool = False,
) -> Sandbox
```


Restart this exact sandbox. Defaults to graceful shutdown, the SDK’s ten-second timeout, and attached local start. A created, stopped, or crashed sandbox starts directly; a starting sandbox is observed until it settles. Set `force` to kill, `timeout` in seconds to change how long shutdown can take, or `detached` for a local background start.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-destroy) sb. destroy()


```
async def destroy(self, *, force: bool = False, timeout: float | None = None) -> None
```


Stop and remove this exact sandbox. Defaults to graceful shutdown with the SDK’s ten-second timeout. Raises `SandboxReplacedError` rather than deleting a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sb-detach) sb. detach()


```
async def detach(self) -> None
```


Example


```
sb = await Sandbox.create("worker", image="python", detached=True)
await sb.detach()  # keeps running in the background
```


Release the handle without stopping the sandbox. The sandbox continues running as a background process. Reconnect later with [`Sandbox.get()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-get).


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch) Patch


Factory for pre-boot root filesystem patches.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-text) Patch. text()


```
@staticmethod
def text(path: str, content: str, *, mode: int | None = None, replace: bool = False) -> PatchConfig
```


Example


```
from microsandbox import Patch, Sandbox

sb = await Sandbox.create(
    "api",
    image="python",
    patches=[Patch.text("/etc/app.conf", "debug=1\n", mode=0o644)],
)
```


Write UTF-8 text content at `path`.


Parameters


`path` str Absolute path inside the guest. `content` str Text content. `mode` int | None File mode, e.g. `0o644`. `replace` bool When `True`, overwrite an existing path.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-file) Patch. file()


```
@staticmethod
def file(path: str, content: bytes, *, mode: int | None = None, replace: bool = False) -> PatchConfig
```


Write arbitrary bytes at `path`. Use [`text()`](https://docs.microsandbox.dev/sdk/python/sandbox#patch-text) for UTF-8 text.


Parameters


`path` str Absolute path inside the guest. `content` bytes Binary file content. `mode` int | None File mode, e.g. `0o644`. `replace` bool When `True`, overwrite an existing path.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-append) Patch. append()


```
@staticmethod
def append(path: str, content: str) -> PatchConfig
```


Append `content` to an existing file at `path`. If the file lives in a lower image layer, it’s copied up first.


Parameters


`path` str Absolute path inside the guest. `content` str Text to append.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-mkdir) Patch. mkdir()


```
@staticmethod
def mkdir(path: str, *, mode: int | None = None) -> PatchConfig
```


Create a directory at `path`. Idempotent: a no-op if the directory already exists.


Parameters


`path` str Absolute path inside the guest. `mode` int | None Directory mode, e.g. `0o755`.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-remove) Patch. remove()


```
@staticmethod
def remove(path: str) -> PatchConfig
```


Delete a file or directory at `path`. Idempotent: a no-op if the path doesn’t exist.


Parameters


`path` str Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-copy_file) Patch. copy_file()


Limited on cloud


```
@staticmethod
def copy_file(src: str, dst: str, *, mode: int | None = None, replace: bool = False) -> PatchConfig
```


Copy a single host file at `src` into the guest rootfs at `dst`.


Parameters


`src` str Host source file. `dst` str Absolute destination path inside the guest. `mode` int | None File mode, e.g. `0o644`. `None` keeps the source mode. `replace` bool When `True`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-copy_dir) Patch. copy_dir()


Limited on cloud


```
@staticmethod
def copy_dir(src: str, dst: str, *, replace: bool = False) -> PatchConfig
```


Recursively copy a host directory at `src` into the guest rootfs at `dst`.


Parameters


`src` str Host source directory. `dst` str Absolute destination path inside the guest. `replace` bool When `True`, overwrite an existing path at `dst`.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patch-symlink) Patch. symlink()


```
@staticmethod
def symlink(target: str, link: str, *, replace: bool = False) -> PatchConfig
```


Create a symlink at `link` pointing to `target`.


Parameters


`target` str What the symlink points to (literal symlink target text). `link` str Absolute path of the symlink itself. `replace` bool When `True`, overwrite an existing path at `link`.


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) SandboxHandle


Returned by [Sandbox.get()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-get) · [Sandbox.list()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list) · [Sandbox.list_with()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list_with)


A metadata and lifecycle handle for an existing sandbox.


| Field | Type | Description |
| --- | --- | --- |
| `name` | `str` | Sandbox name, up to 128 UTF-8 bytes |
| `id` | `str` | Opaque stable identity captured by this metadata handle. Receiver lifecycle calls remain bound to this value and raise `SandboxReplacedError` when the reusable name now points to another sandbox. |
| `status` | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstatus) | Current status |
| `config_json` | `str` | Raw JSON configuration |
| `created_at` | `float | None` | Creation timestamp (ms since epoch) |
| `updated_at` | `float | None` | Last update timestamp (ms since epoch) |


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-config) handle. config()


Local-only


```
config()
```


Parsed configuration


Returns


`dict[str, Any]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-refresh) handle. refresh()


```
refresh()
```


Re-fetch status and metadata, returning a fresh handle


Returns


`Awaitable[` [`SandboxHandle`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-ping) handle. ping()


Local-only


```
ping()
```


Check agent reachability without refreshing idle activity; does not start stopped sandboxes


Returns


`Awaitable[` [`SandboxPingResult`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxpingresult) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-touch) handle. touch()


Local-only


```
touch()
```


Explicitly refresh idle activity; does not start stopped sandboxes


Returns


`Awaitable[` [`SandboxTouchResult`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxtouchresult) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-modify) handle. modify()


Local-only


```
modify(...)
```


Plan or apply a configuration change; same kwargs as [`modify()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-modify). Does not start stopped sandboxes; changes persist for the next boot


Returns


`Awaitable[` [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmodificationplan) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-connect) handle. connect()


```
connect(timeout=None)
```


Connect to a running sandbox, optionally with an explicit timeout in seconds


Returns


`Awaitable[` [`Sandbox`](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-connect_or_start) handle. connect_or_start()


```
async def connect_or_start(self, *, detached: bool = False) -> Sandbox
```


Connect when this exact sandbox is running, wait through `STARTING`, or start it when it is `CREATED`, `STOPPED`, or `CRASHED`. `DRAINING` and `PAUSED` are rejected. `detached=True` affects only a required local start; connecting to an already-running sandbox does not change ownership.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-wait_for_status) handle. wait_for_status()


```
async def wait_for_status(self, status: SandboxStatus) -> SandboxHandle
```


Wait without a built-in timeout until this exact sandbox reaches `status`, returning a refreshed handle. Raises `SandboxReplacedError` rather than rebinding to a replacement.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-restart) handle. restart()


```
async def restart(
    self,
    *,
    force: bool = False,
    timeout: float | None = None,
    detached: bool = False,
) -> Sandbox
```


Restart this exact sandbox with the same state and option semantics as [`sb.restart()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-restart).


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-destroy) handle. destroy()


```
async def destroy(self, *, force: bool = False, timeout: float | None = None) -> None
```


Stop and remove this exact sandbox. A stale handle cannot destroy a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-start) handle. start()


```
start(*, detached=False)
```


Start in attached or detached mode


Returns


`Awaitable[` [`Sandbox`](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-stop) handle. stop()


Different on cloud


```
stop(timeout=None)
```


Wait indefinitely for graceful completion and runtime ownership release. `await handle.stop_with_timeout(seconds)` supplies one total budget; expiry raises `StopTimeoutError` without killing, and zero expires before dispatch. The optional `stop(timeout=...)` argument uses the same behavior.


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-request_stop) handle. request_stop()


```
request_stop()
```


Request graceful shutdown without waiting


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-kill) handle. kill()


Local-only


```
kill(timeout=None)
```


Force terminate and wait until stopped state is observed


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-request_kill) handle. request_kill()


Local-only


```
request_kill()
```


Request force termination without waiting


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-request_drain) handle. request_drain()


Local-only


```
request_drain()
```


Request graceful drain without waiting


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-wait_until_stopped) handle. wait_until_stopped()


```
wait_until_stopped()
```


Block until the sandbox reaches terminal state


Returns


`Awaitable[` [`SandboxStopResult`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstopresult) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-remove) handle. remove()


```
remove()
```


Delete sandbox and state


Returns


`Awaitable[None]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-metrics) handle. metrics()


Local-only


```
metrics()
```


Point-in-time resource metrics


Returns


`Awaitable[` [`SandboxMetrics`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-logs) handle. logs()


Local-only


```
logs(...)
```


Read captured `exec.log` (works without starting)


Returns


`Awaitable[list[` [`LogEntry`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry) `]]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-log_stream) handle. log_stream()


```
log_stream(...)
```


Stream captured log entries (works without starting)


Returns


`Awaitable[` [`LogStream`](https://docs.microsandbox.dev/sdk/python/sandbox#logstream) `]`


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#handle-snapshot) handle. snapshot()


Limited on cloud


```
snapshot(name)
```


Create a named [snapshot](https://docs.microsandbox.dev/sdk/python/snapshots) of the sandbox


Returns


`Awaitable[Snapshot]`


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#metricsstream) MetricsStream


Returned by [metrics_stream()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-metrics_stream)


Async stream for receiving periodic metrics snapshots.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#metrics_stream-aiter) metrics_stream. **aiter** ()


```
__aiter__()
```


Use with `async for`


Returns


[`SandboxMetrics`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics)


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#metrics_stream-anext) metrics_stream. **anext** ()


```
__anext__()
```


Use with `async for`


Returns


[`SandboxMetrics`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics)


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#logentry) LogEntry


Returned by [logs()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-logs) · iterated from [LogStream](https://docs.microsandbox.dev/sdk/python/sandbox#logstream)


A single captured log entry returned by [`logs()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-logs) or iterated from a [`LogStream`](https://docs.microsandbox.dev/sdk/python/sandbox#logstream).


| Field | Type | Description |
| --- | --- | --- |
| `timestamp_ms` | `float` | Wall-clock capture time (ms since Unix epoch, UTC) |
| `source` | [`LogSource`](https://docs.microsandbox.dev/sdk/python/sandbox#logsource) | Where the chunk came from |
| `session_id` | `int | None` | Relay-monotonic session id; `None` for `"system"` entries |
| `cursor` | `str` | Opaque resume token; pass back via `log_stream(from_cursor=...)` |
| `data` | `bytes` | The chunk’s raw bytes |


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#entry-text) entry. text()


```
text()
```


Convenience: UTF-8 decode of `data` (lossy; invalid bytes are replaced)


Returns


`str`


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#logstream) LogStream


Returned by [log_stream()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-log_stream)


Async stream of [`LogEntry`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry) values, returned by [`log_stream()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-log_stream).


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#log_stream-aiter) log_stream. **aiter** ()


```
__aiter__()
```


Use with `async for`


Returns


[`LogEntry`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry)


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#log_stream-anext) log_stream. **anext** ()


```
__anext__()
```


Use with `async for`


Returns


[`LogEntry`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry)


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#pullsession) PullSession


Returned by [create_with_progress()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create_with_progress)


Returned by [`create_with_progress()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create_with_progress). The factory itself is synchronous; use the returned session as an async context manager to track image pull progress.


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#session-progress) session. progress


`AsyncIterator[` [`PullEvent`](https://docs.microsandbox.dev/sdk/python/sandbox#pullevent) `]`
Async iterator of pull progress events


#### [​](https://docs.microsandbox.dev/sdk/python/sandbox#session-result) session. result()


```
result()
```


Await once to get the final running sandbox. A second call raises `RuntimeError`


Returns


`Awaitable[` [`Sandbox`](https://docs.microsandbox.dev/sdk/python/sandbox#instance-methods) `]`


```
session = Sandbox.create_with_progress("my-sandbox", image="ubuntu:latest")
async with session:
    async for event in session.progress:
        print(event)
    sb = await session.result()
```


## [​](https://docs.microsandbox.dev/sdk/python/sandbox#types) Types


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig) SandboxConfig


Used by [create()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) · [create_with_progress()](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create_with_progress)


Limited on cloud
The keyword arguments accepted by [`create()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) and [`create_with_progress()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create_with_progress). There is no `SandboxConfig` object you construct directly; these are passed as `**kwargs`.


| Field | Type | Default | Description |
| --- | --- | --- | --- |
| image | `str | os.PathLike[str] | ` [`ImageSource`](https://docs.microsandbox.dev/sdk/python/images) | - | OCI image, local path, or disk image. Required; use `Sandbox.restore()` for snapshots. Use `Image.oci("python:3.12", root_disk=RootDisk.managed(8192))` to set a managed OCI root-disk size |
| cpus | `int` | `1` | Virtual CPUs. This is a limit, not a reservation |
| max_cpus | `int` | same as `cpus` | Boot-time maximum possible virtual CPUs |
| memory | `int` | `512` | Guest memory in MiB. This is a limit, not a reservation |
| max_memory | `int` | same as `memory` | Boot-time maximum hotpluggable memory in MiB |
| thp | `"always" | "madvise" | "never"` | `"madvise"` | Guest transparent huge-page policy selected at boot |
| workdir | `str` | - | Default working directory for commands |
| shell | `str` | `"/bin/sh"` | Shell for `shell()` calls |
| security | [`SecurityProfile`](https://docs.microsandbox.dev/sdk/python/sandbox#securityprofile) | `DEFAULT` | In-guest security profile. `RESTRICTED` sets `no_new_privs`, drops mount-admin capability from user commands, and forces `nosuid,nodev` on user mounts |
| hostname | `str` | - | Guest hostname |
| user | `str` | - | Default guest user |
| entrypoint | `Sequence[str]` | - | Override the image’s stored ENTRYPOINT used by `exec_default`; literal `exec` and `shell` ignore it |
| cmd | `Sequence[str]` | - | Override the image’s stored CMD used by `exec_default`; an empty sequence clears CMD |
| init | `str | ` [`InitConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#initconfig) `|` [`InitOptions`](https://docs.microsandbox.dev/sdk/python/sandbox#initoptions) | - | Hand off PID 1 to a guest init binary. See [Custom init system](https://docs.microsandbox.dev/sandboxes/bootstrap#custom-init-system) and [`InitConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#initconfig) for accepted shapes |
| replace | `bool` | `False` | Replace an existing sandbox with the same name (10s SIGTERM grace, then SIGKILL) |
| replace_with_timeout | `float` | `10` | Seconds to wait after `SIGTERM` before escalating to `SIGKILL` (`0` skips `SIGTERM`). Implies `replace=True` |
| max_duration | `float` | - | Maximum sandbox lifetime in seconds; finite and non-negative, rounded up to whole seconds |
| idle_timeout | `float` | - | Idle timeout in seconds; finite and non-negative, rounded up to whole seconds |
| ephemeral | `bool` | `False` | If `True`, the sandbox and all its persisted state are removed automatically once it stops, rather than left on disk for restart |
| env | `Mapping[str, str]` | `{}` | Environment variables visible to all commands |
| labels | `Mapping[str, str]` | `{}` | User-defined labels attached to the sandbox. Filter with [`list_with()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list_with); see [Select in bulk](https://docs.microsandbox.dev/sandboxes/labels#select-in-bulk). Keys starting with `sandbox.`, `microsandbox.`, or `service.` are reserved and rejected |
| scripts | `Mapping[str, str]` | `{}` | Named scripts mounted at `/.msb/scripts/` and added to `PATH` |
| pull_policy | [`PullPolicy`](https://docs.microsandbox.dev/sdk/python/sandbox#pullpolicy) | `IF_MISSING` | Image pull behavior |
| log_level | [`LogLevel`](https://docs.microsandbox.dev/sdk/python/sandbox#loglevel) | - | Override log verbosity |
| registry_auth | [`RegistryAuth`](https://docs.microsandbox.dev/sdk/python/sandbox#registryauth) | - | Private registry credentials |
| registry_insecure | `bool` | `False` | Pull images over plain HTTP instead of HTTPS (local or self-hosted registries) |
| registry_ca_certs | `list[bytes | bytearray | str | os.PathLike]` | `[]` | Additional CA roots for image pulls. File paths are read when `create()` is called. |
| volumes | `Mapping[str, ` [`MountConfig`](https://docs.microsandbox.dev/sdk/python/volumes) `]` | `{}` | Volume mounts. See [Volumes](https://docs.microsandbox.dev/sdk/python/volumes) |
| patches | `Sequence[` [`PatchConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#patchconfig) `]` | `[]` | Rootfs modifications applied before boot |
| ports | `Mapping[int, int] | Sequence[` [`PortBinding`](https://docs.microsandbox.dev/sdk/python/networking#portbinding) `]` | `{}` | Port mappings. Mapping form is TCP and binds to `127.0.0.1`; use `PortBinding` for explicit bind addresses or UDP |
| network | [`Network`](https://docs.microsandbox.dev/sdk/python/networking#network) | public profile | Network policy and configuration |
| proxy | [`OutboundProxy`](https://docs.microsandbox.dev/sdk/python/proxies#outboundproxy) ` | None` | `None` | Single proxy used for outbound connections. See [Proxies](https://docs.microsandbox.dev/sdk/python/proxies) |
| secrets | `Sequence[` [`SecretEntry`](https://docs.microsandbox.dev/sdk/python/secrets#secretentry) `]` | `[]` | Secret injection |
| secret_violation_action | [`ViolationAction`](https://docs.microsandbox.dev/sdk/python/secrets#violationaction) | `BLOCK_AND_LOG` | Sandbox-wide default action when a secret placeholder would leak to a non-eligible destination. Shorthand for `Network.secret_violation_action`; if both are provided, this top-level value takes precedence. |
| detached | `bool` | `False` | If `True`, spawn the sandbox in detached mode; call [`detach()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-detach) before dropping the returned handle when it should keep running |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#initconfig) InitConfig


Used by [create(init=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Custom init specification. Pass it (or one of the equivalent shorthand shapes) as the `init=` kwarg to [`create()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-create) to hand PID 1 inside the guest off to your own init binary after agentd’s setup. Frozen dataclass. See [Custom init system](https://docs.microsandbox.dev/sandboxes/bootstrap#custom-init-system) for image picks, shutdown semantics, and tradeoffs.


| Field | Type | Default | Description |
| --- | --- | --- | --- |
| cmd | `str` | - | Absolute path or `"auto"` to the init binary. Auto honors a known image ENTRYPOINT init before probing `/sbin/init`, `/lib/systemd/systemd`, and `/usr/lib/systemd/systemd`, and preserves attached init-entrypoint commands |
| args | `tuple[str, ...]` | `()` | Supplemental argv (`argv[0]` is implicitly `cmd`) |
| env | `Mapping[str, str]` | `{}` | Extra env vars merged on top of the inherited env |


The `init=` kwarg accepts a bare scalar for the simple case, an [`InitConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#initconfig) dataclass, or an [`InitOptions`](https://docs.microsandbox.dev/sdk/python/sandbox#initoptions) typed dictionary for the rich case.


| Form | Equivalent to |
| --- | --- |
| `init="auto"` or `init="/sbin/init"` | `InitConfig(cmd=...)` |
| `init={"cmd": ..., "args": [...], "env": {...}}` | dict equivalent of `InitConfig` |
| `init=InitConfig(cmd="/sbin/init", args=("--foo",))` | itself |


```
from microsandbox import InitConfig, Sandbox

# Common case: bare string.
sb = await Sandbox.create("worker", image="jrei/systemd-debian:12", init="auto")

# Argv / env: dataclass.
sb = await Sandbox.create(
    "worker",
    image="jrei/systemd-debian:12",
    init=InitConfig(
        cmd="/lib/systemd/systemd",
        args=("--unit=multi-user.target",),
        env={"container": "microsandbox"},
    ),
)
```


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#initoptions) InitOptions


Used by [create(init=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Typed-dictionary form of [`InitConfig`](https://docs.microsandbox.dev/sdk/python/sandbox#initconfig). `cmd` is required; `args` and `env` are optional.


| Key | Type | Description |
| --- | --- | --- |
| `cmd` | `str` | Absolute path or `"auto"` to the init binary |
| `args` | `list[str]` | Supplemental argv |
| `env` | `dict[str, str]` | Extra environment variables |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#securityprofile) SecurityProfile


Used by [create(security=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Sandbox-wide in-guest security profile.


| Member | Value | Description |
| --- | --- | --- |
| `SecurityProfile.DEFAULT` | `"default"` | Standard profile |
| `SecurityProfile.RESTRICTED` | `"restricted"` | Sets `no_new_privs`, drops mount-admin capability from user commands, and forces `nosuid,nodev` on user mounts |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxpage) SandboxPage


One stable, newest-first page returned by [`Sandbox.list()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list) or [`Sandbox.list_with()`](https://docs.microsandbox.dev/sdk/python/sandbox#sandbox-list_with).


| Property | Type | Description |
| --- | --- | --- |
| `sandboxes` | `list[SandboxHandle]` | Handles in this page |
| `next_cursor` | `str | None` | Opaque continuation cursor, or `None` on the final page |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxpingresult) SandboxPingResult


Returned by [ping()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-ping)


Agent reachability result.


| Property | Type | Description |
| --- | --- | --- |
| name | `str` | Sandbox name |
| latency_ms | `float` | Round-trip latency in milliseconds |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxtouchresult) SandboxTouchResult


Returned by [touch()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-touch)


Explicit idle-refresh result.


| Property | Type | Description |
| --- | --- | --- |
| name | `str` | Sandbox name |
| activity_seq | `int` | Monotonic activity sequence after the touch |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstopresult) SandboxStopResult


Returned by [wait_until_stopped()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_until_stopped)


Observed terminal sandbox state returned by [`wait_until_stopped()`](https://docs.microsandbox.dev/sdk/python/sandbox#sb-wait_until_stopped).


| Property | Type | Description |
| --- | --- | --- |
| name | `str` | Sandbox name |
| status | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstatus) | Terminal status that was observed |
| exit_code | `int | None` | Process exit code when it is available |
| signal | `int | None` | Terminating signal number when the sandbox was killed by a signal |
| observed_at | `float` | When the terminal state was observed (ms since epoch) |
| source | `str | None` | Where the terminal observation came from |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstatus) SandboxStatus


Used by [SandboxHandle.status](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxhandle) · [SandboxStopResult.status](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstopresult)


Sandbox lifecycle status returned by `status` fields.


| Member | Value | Description |
| --- | --- | --- |
| `SandboxStatus.CREATED` | `"created"` | Sandbox metadata exists but the VM has not started |
| `SandboxStatus.STARTING` | `"starting"` | A start request is in progress |
| `SandboxStatus.RUNNING` | `"running"` | Guest agent is ready; `exec`, `shell`, and `fs` work |
| `SandboxStatus.STOPPED` | `"stopped"` | VM shut down; configuration persisted; can be restarted |
| `SandboxStatus.CRASHED` | `"crashed"` | VM exited unexpectedly (kernel panic, OOM, etc.) |
| `SandboxStatus.DRAINING` | `"draining"` | Graceful shutdown in progress; existing commands finish, new ones rejected |
| `SandboxStatus.PAUSED` | `"paused"` | VM paused |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#backendkind) BackendKind


Used by `set_default_backend()` · `backend_scope()` · returned by `default_backend_kind()`


Selected sandbox backend.


| Member | Value | Description |
| --- | --- | --- |
| `BackendKind.LOCAL` | `"local"` | Local libkrun backend |
| `BackendKind.CLOUD` | `"cloud"` | Microsandbox cloud backend; requires an API key or named profile |


```
from microsandbox import BackendKind, set_default_backend

set_default_backend(BackendKind.CLOUD, profile="production")
```


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#modificationpolicy) ModificationPolicy


Used by [modify(policy=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sb-modify)


Controls how sandbox modifications that cannot apply live are handled.


| Member | Value | Description |
| --- | --- | --- |
| `ModificationPolicy.NO_RESTART` | `"no_restart"` | Apply only changes that do not require a restart |
| `ModificationPolicy.NEXT_START` | `"next_start"` | Persist changes for the next start without restarting a running VM |
| `ModificationPolicy.RESTART` | `"restart"` | Restart when required so changes become active immediately |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#secretmodifyspec) SecretModifySpec


Used by [modify(secrets=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sb-modify)


Desired state for one secret. `env`, `value`, and `store` are mutually exclusive sources. Omit all three to update only the supplied policy or placeholder fields.


| Key | Type | Description |
| --- | --- | --- |
| `env` | `str` | Host environment variable to resolve when applying the modification |
| `value` | `str` | Raw secret value. Stored in the durable sandbox config until replaced by a source reference |
| `store` | `str` | Reserved for a host-side secret store reference; currently unsupported |
| `placeholder` | `str` | Explicit guest-visible placeholder. New secrets default to `$MSB_<NAME>` |
| `allowed_hosts` | `list[str]` | Desired allowed host patterns. A new secret requires at least one; an empty list leaves existing hosts unchanged |
| `substitution` | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/python/secrets#secretsubstitution) | Desired substitution locations. Omission preserves the existing policy; new secrets default to headers only |
| `violation_action` | [`ViolationAction`](https://docs.microsandbox.dev/sdk/python/secrets#violationaction) | Per-secret blocking action. Omission preserves the existing override |
| `require_tls_identity` | `bool` | Whether substitution requires verified TLS identity. Omission preserves the existing setting; new secrets default to `True`. Explicit `False` disables this requirement |
| `allow_placeholder_for` | `Sequence[str]` | Hosts permitted to receive unchanged placeholders. A nonempty sequence replaces existing passthrough hosts; an empty sequence leaves them unchanged |
| `passthrough` | `Sequence[str]` | Deprecated alias for `allow_placeholder_for`. Nonempty values emit `DeprecationWarning`; when both keys are supplied, their sequences are combined |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmodificationplan) SandboxModificationPlan


Typed dictionary returned by `Sandbox.modify()` and `SandboxHandle.modify()`. Config changes and secret changes use different typed shapes and are discriminated by their `kind` member.


| Key | Type | Description |
| --- | --- | --- |
| `sandbox` | `str` | Sandbox being modified |
| `status` | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxstatus) | Status used to classify the requested changes |
| `applied` | `bool` | Whether the plan was applied |
| `policy` | [`ModificationPolicy`](https://docs.microsandbox.dev/sdk/python/sandbox#modificationpolicy) | Policy used to produce the plan |
| `changes` | `list[ConfigPlannedChange | SecretPlannedChange]` | Planned changes |
| `conflicts` | `list[ModificationConflict]` | Blocking conflicts, each with `field` and `message` |
| `warnings` | `list[ModificationWarning]` | Non-fatal warnings, each with `field` and `message` |
| `resize_status` | `list[ResourceResizeStatus]` | Optional live-resize convergence results |


`ConfigPlannedChange` has `kind`, `field`, `change`, and `disposition`, plus optional `before`, `after`, and `reason`. `SecretPlannedChange` has `kind`, `field`, `name`, `change`, and `disposition`, plus optional `before_ref`, `after_ref`, `allow_hosts`, and `reason`. Secret values never appear in a plan.


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#plannedchangekind) PlannedChangeKind


Discriminator for entries in `SandboxModificationPlan.changes`.


| Member | Value | Description |
| --- | --- | --- |
| `PlannedChangeKind.CONFIG` | `"config"` | Ordinary configuration change |
| `PlannedChangeKind.SECRET` | `"secret"` | Secret metadata or material change |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#changekind) ChangeKind


Natural operation for a configuration change.


| Member | Value | Description |
| --- | --- | --- |
| `ChangeKind.ADDED` | `"added"` | A field is being added |
| `ChangeKind.UPDATED` | `"updated"` | A field is being updated |
| `ChangeKind.REMOVED` | `"removed"` | A field is being removed |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#secretchangekind) SecretChangeKind


Natural operation for a secret change.


| Member | Value | Description |
| --- | --- | --- |
| `SecretChangeKind.ADDED` | `"added"` | A secret is being added |
| `SecretChangeKind.ROTATED` | `"rotated"` | Secret material is being rotated |
| `SecretChangeKind.REMOVED` | `"removed"` | A secret is being removed |
| `SecretChangeKind.RENAMED` | `"renamed"` | A secret is being renamed |
| `SecretChangeKind.HOSTS_UPDATED` | `"hosts updated"` | Allowed hosts are being updated |
| `SecretChangeKind.PLACEHOLDER_UPDATED` | `"placeholder updated"` | The guest-visible placeholder is being updated |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#modificationdisposition) ModificationDisposition


When or whether a planned change can take effect.


| Member | Value | Description |
| --- | --- | --- |
| `ModificationDisposition.LIVE` | `"live"` | Applies to the running VM now |
| `ModificationDisposition.NEXT_START` | `"next start"` | Applies the next time the sandbox starts |
| `ModificationDisposition.REQUIRES_RESTART` | `"requires restart"` | Requires a restart before taking effect |
| `ModificationDisposition.UNSUPPORTED` | `"unsupported"` | Cannot be changed through `modify()` |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#resourcekind) ResourceKind


Resource reported by a live-resize result.


| Member | Value | Description |
| --- | --- | --- |
| `ResourceKind.CPUS` | `"cpus"` | vCPU count |
| `ResourceKind.MEMORY` | `"memory"` | Guest memory |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#resourceconvergencestate) ResourceConvergenceState


Observed convergence state for an accepted live resize.


| Member | Value | Description |
| --- | --- | --- |
| `ResourceConvergenceState.ACCEPTED` | `"accepted"` | Runtime accepted the request |
| `ResourceConvergenceState.CONVERGING` | `"converging"` | Guest and VMM are still converging |
| `ResourceConvergenceState.APPLIED` | `"applied"` | Desired, actual, and enforced values match |
| `ResourceConvergenceState.GUEST_REFUSED` | `"guest-refused"` | Guest refused or failed to cooperate |
| `ResourceConvergenceState.FAILED` | `"failed"` | Resize failed |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxmetrics) SandboxMetrics


Returned by [metrics()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-metrics) · [metrics_stream()](https://docs.microsandbox.dev/sdk/python/sandbox#sb-metrics_stream)


Point-in-time resource usage snapshot.


| Field | Type | Description |
| --- | --- | --- |
| cpu_percent | `float` | CPU usage as a percentage |
| vcpu_time_ns | `int` | Cumulative vCPU time consumed since boot, in nanoseconds |
| memory_bytes | `int` | Current memory usage in bytes |
| memory_available_bytes | `int | None` | Guest-reported available memory in bytes when known |
| memory_host_resident_bytes | `int | None` | Host-resident memory backing the guest in bytes when known |
| memory_limit_bytes | `int` | Memory limit in bytes |
| disk_read_bytes | `int` | Total bytes read from disk since boot |
| disk_write_bytes | `int` | Total bytes written to disk since boot |
| net_rx_bytes | `int` | Total bytes received over the network since boot |
| net_tx_bytes | `int` | Total bytes sent over the network since boot |
| upper_used_bytes | `int | None` | Guest-visible OCI upper filesystem used bytes when the protected reporter is available and fresh |
| upper_free_bytes | `int | None` | Guest-visible OCI upper filesystem free bytes when the protected reporter is available and fresh |
| upper_host_allocated_bytes | `int | None` | Host-allocated bytes for the writable OCI upper image when available |
| uptime_ms | `int` | Time since the sandbox was created (ms) |
| timestamp_ms | `float` | When this measurement was taken (ms since epoch) |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#logsource) LogSource


Returned by [LogEntry.source](https://docs.microsandbox.dev/sdk/python/sandbox#logentry)


Source attached to each [`LogEntry`](https://docs.microsandbox.dev/sdk/python/sandbox#logentry).


| Member | Value | Description |
| --- | --- | --- |
| `LogSource.STDOUT` | `"stdout"` | Captured from a session’s stdout (pipe mode, streams stayed separated) |
| `LogSource.STDERR` | `"stderr"` | Captured from a session’s stderr (pipe mode) |
| `LogSource.OUTPUT` | `"output"` | Captured from a PTY session, where stdout and stderr are merged by the guest kernel |
| `LogSource.SYSTEM` | `"system"` | Synthetic lifecycle or runtime diagnostic entry |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#logreadsource) LogReadSource


Used by [logs(sources=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sb-logs) · [log_stream(sources=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sb-log_stream)


Log source selector accepted by `logs()` and `log_stream()`.


| Member | Value | Description |
| --- | --- | --- |
| `LogReadSource.STDOUT` | `"stdout"` | Select stdout entries |
| `LogReadSource.STDERR` | `"stderr"` | Select stderr entries |
| `LogReadSource.OUTPUT` | `"output"` | Select PTY-merged output entries |
| `LogReadSource.SYSTEM` | `"system"` | Select lifecycle and runtime diagnostic entries |
| `LogReadSource.ALL` | `"all"` | Select all four sources |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#loglevel) LogLevel


Used by [create(log_level=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Sandbox process log verbosity.


| Member | Value | Description |
| --- | --- | --- |
| `LogLevel.TRACE` | `"trace"` | Most verbose, all diagnostic output |
| `LogLevel.DEBUG` | `"debug"` | Debug and higher |
| `LogLevel.INFO` | `"info"` | Info and higher |
| `LogLevel.WARN` | `"warn"` | Warnings and errors only |
| `LogLevel.ERROR` | `"error"` | Errors only |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#pullpolicy) PullPolicy


Used by [create(pull_policy=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Controls when the SDK fetches an OCI image from the registry.


| Member | Value | Description |
| --- | --- | --- |
| `PullPolicy.ALWAYS` | `"always"` | Pull the image every time, even if cached locally |
| `PullPolicy.IF_MISSING` | `"if-missing"` | Pull only if the image is not already cached. This is the default |
| `PullPolicy.NEVER` | `"never"` | Never pull; fail if the image is not cached locally |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#registryauth) RegistryAuth


Used by [create(registry_auth=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


Credentials for authenticating to a private container registry. Frozen dataclass; construct directly or via `RegistryAuth.basic(username, password)`.


| Field | Type | Description |
| --- | --- | --- |
| username | `str` | Registry username |
| password | `str` | Registry password |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patchconfig) PatchConfig


Returned by [Patch.* factory methods](https://docs.microsandbox.dev/sdk/python/sandbox#patch-text) · used by [create(patches=…)](https://docs.microsandbox.dev/sdk/python/sandbox#sandboxconfig)


A single rootfs patch. Produced by the [`Patch`](https://docs.microsandbox.dev/sdk/python/sandbox#patch) factory; you’d normally not construct one directly. Frozen dataclass.


| Field | Type | Description |
| --- | --- | --- |
| kind | [`PatchKind`](https://docs.microsandbox.dev/sdk/python/sandbox#patchkind) | Patch operation |
| path | `str | None` | Absolute guest path (text / file / mkdir / remove / append) |
| content | `str | bytes | None` | Text content for `TEXT` / `APPEND`, or binary content for `FILE` |
| src | `str | None` | Host source path (copy_file / copy_dir) |
| dst | `str | None` | Guest destination path (copy_file / copy_dir) |
| target | `str | None` | Symlink target |
| link | `str | None` | Symlink path |
| mode | `int | None` | File / directory mode for text, file, copy-file, or mkdir patches (e.g. `0o644`) |
| replace | `bool` | When `True`, overwrite an existing destination for text, file, copy, or symlink patches. Defaults to `False` |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#patchkind) PatchKind


Used by [PatchConfig.kind](https://docs.microsandbox.dev/sdk/python/sandbox#patchconfig)


Rootfs patch operation.


| Member | Value | Description |
| --- | --- | --- |
| `PatchKind.TEXT` | `"text"` | Write a UTF-8 text file |
| `PatchKind.FILE` | `"file"` | Write an arbitrary binary file |
| `PatchKind.APPEND` | `"append"` | Append to a text file |
| `PatchKind.COPY_FILE` | `"copy_file"` | Copy a host file into the guest |
| `PatchKind.COPY_DIR` | `"copy_dir"` | Copy a host directory into the guest |
| `PatchKind.SYMLINK` | `"symlink"` | Create a symbolic link |
| `PatchKind.MKDIR` | `"mkdir"` | Create a directory |
| `PatchKind.REMOVE` | `"remove"` | Remove a path |


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#pullevent) PullEvent


Iterated from [PullSession.progress](https://docs.microsandbox.dev/sdk/python/sandbox#pullsession)


Native event object emitted by [`PullSession.progress`](https://docs.microsandbox.dev/sdk/python/sandbox#pullsession). Inspect `event_type` and the fields relevant to that event; fields that do not apply to a particular event are `None`.


| Field | Type | Description |
| --- | --- | --- |
| event_type | [`PullEventType`](https://docs.microsandbox.dev/sdk/python/sandbox#pulleventtype) | Event discriminator |
| reference | `str | None` | Image reference being pulled |
| manifest_digest | `str | None` | Resolved manifest digest |
| layer_count | `int | None` | Number of layers |
| total_download_bytes | `int | None` | Total bytes to download across layers |
| layer_index | `int | None` | Index of the layer this event concerns |
| digest | `str | None` | Layer blob digest |
| diff_id | `str | None` | Layer diff id |
| downloaded_bytes | `int | None` | Bytes downloaded so far for the layer |
| total_bytes | `int | None` | Total bytes for the layer |
| bytes_read | `int | None` | Bytes read during materialization |


```
from microsandbox import PullEventType, Sandbox

session = Sandbox.create_with_progress("my-sandbox", image="ubuntu:latest")
async with session:
    async for event in session.progress:
        if event.event_type is PullEventType.RESOLVED:
            print(f"{event.layer_count} layers, {event.total_download_bytes} bytes")
        elif event.event_type is PullEventType.LAYER_DOWNLOAD_PROGRESS:
            print(f"layer {event.layer_index}: {event.downloaded_bytes}/{event.total_bytes}")
    sb = await session.result()
```


### [​](https://docs.microsandbox.dev/sdk/python/sandbox#pulleventtype) PullEventType


Discriminator returned by [`PullEvent.event_type`](https://docs.microsandbox.dev/sdk/python/sandbox#pullevent).


| Member | Value | Description |
| --- | --- | --- |
| `PullEventType.RESOLVING` | `"resolving"` | Resolving the image reference |
| `PullEventType.RESOLVED` | `"resolved"` | Manifest resolved |
| `PullEventType.LAYER_DOWNLOAD_PROGRESS` | `"layer_download_progress"` | Layer download advanced |
| `PullEventType.LAYER_DOWNLOAD_COMPLETE` | `"layer_download_complete"` | Layer download completed |
| `PullEventType.LAYER_DOWNLOAD_VERIFYING` | `"layer_download_verifying"` | Layer digest is being verified |
| `PullEventType.LAYER_MATERIALIZE_STARTED` | `"layer_materialize_started"` | Layer materialization started |
| `PullEventType.LAYER_MATERIALIZE_PROGRESS` | `"layer_materialize_progress"` | Layer materialization advanced |
| `PullEventType.LAYER_MATERIALIZE_WRITING` | `"layer_materialize_writing"` | Materialized layer is being written |
| `PullEventType.LAYER_MATERIALIZE_COMPLETE` | `"layer_materialize_complete"` | Layer materialization completed |
| `PullEventType.STITCH_MERGING_TREES` | `"stitch_merging_trees"` | Layer trees are being merged |
| `PullEventType.STITCH_WRITING_FSMETA` | `"stitch_writing_fsmeta"` | Filesystem metadata is being written |
| `PullEventType.STITCH_WRITING_VMDK` | `"stitch_writing_vmdk"` | VMDK image is being written |
| `PullEventType.STITCH_COMPLETE` | `"stitch_complete"` | Image stitching completed |
| `PullEventType.COMPLETE` | `"complete"` | Image pull completed |


Was this page helpful?

Yes No ⌘ I

---

# Ruby SDK Sandbox reference

`https://docs.microsandbox.dev/sdk/ruby/sandbox`

See [Overview](https://docs.microsandbox.dev/sandboxes/overview) for configuration examples and [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle) for state management. See [Error handling](https://docs.microsandbox.dev/sdk/errors) for cross-SDK behavior.


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox) Sandbox


Class methods


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-create) Microsandbox::Sandbox. create()


```
Microsandbox::Sandbox.create(name, **options) # => Sandbox
```


Example


```
sandbox = Microsandbox::Sandbox.create("worker", image: "alpine", memory: 512)
```


Create and start a sandbox. An existing name is an error unless replacement is requested. See [Networking](https://docs.microsandbox.dev/sdk/ruby/networking) for network, proxy, and secret options.


Parameters


`name` String Sandbox name. `image` String OCI image reference. `cpus` Integer Initial virtual CPU count. `max_cpus` Integer Maximum virtual CPU count. `memory` Integer Initial memory in MiB. `max_memory` Integer Maximum memory in MiB. `env` Hash Environment variables with string keys and values. `labels` Hash Labels with string keys and values. `workdir` String Guest working directory. `shell` String Shell used for shell commands. `hostname` String Guest hostname. `user` String Guest user. `detached` Boolean Start locally in the background. `ephemeral` Boolean Remove sandbox state when its lifecycle ends. `max_duration` Integer Maximum lifetime in seconds. `idle_timeout` Integer Idle timeout in seconds. `replace` Boolean Replace an existing sandbox with this name. `replace_timeout` Numeric Finite, non-negative replacement timeout in seconds. `root_disk` Integer Managed root disk size in MiB. `disable_network` Boolean Disable sandbox networking. `network` Symbol | Hash Use :none or the allowlist hash documented in the Networking reference. `proxy` OutboundProxy SOCKS proxy configuration; see the Networking reference. `secrets` Array<Hash> Secret injection entries; see the Networking reference. `quiet_logs` Boolean Suppress sandbox log output. `entrypoint` Array<String> Override the image entrypoint; creation does not execute it. `init` String Guest init program. `pull_policy` String Image pull policy: if_missing (or if-missing), always, or never. `scripts` Hash Named scripts with string keys and values. `slug` String Human-readable sandbox slug.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-builder) Microsandbox::Sandbox. builder()


```
Microsandbox::Sandbox.builder(name) # => SandboxBuilder
```


Create a chainable sandbox builder.


Parameters


`name` String Sandbox name.


Returns


SandboxBuilder Configuration builder.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-start) Microsandbox::Sandbox. start()


```
Microsandbox::Sandbox.start(name, detached: false) # => Sandbox
```


Start an existing sandbox.


Parameters


`name` String Sandbox name. `detached` Boolean Start locally in the background; defaults to false.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-get) Microsandbox::Sandbox. get()


```
Microsandbox::Sandbox.get(name) # => SandboxHandle
```


Obtain persisted metadata without connecting to the guest agent.


Parameters


`name` String Sandbox name.


Returns


SandboxHandle Metadata handle bound to this sandbox identity.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-list) Microsandbox::Sandbox. list()


```
Microsandbox::Sandbox.list(**options) # => Hash
```


Example


```
page = Microsandbox::Sandbox.list(limit: 20)
page["sandboxes"].each { |handle| puts handle.name }
```


List sandboxes with optional pagination and label filtering.


Parameters


`cursor` String Optional cursor from the previous page. `limit` Integer Optional maximum page size. `labels` Hash Optional label filter with string keys and values.


Returns


Hash String keys: sandboxes (Array<SandboxHandle>) and next_cursor (String or nil).


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-remove) Microsandbox::Sandbox. remove()


```
Microsandbox::Sandbox.remove(name) # => nil
```


Remove a stopped sandbox and its local state. Use destroy to stop and remove a sandbox.


Parameters


`name` String Sandbox name.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-with) Microsandbox::Sandbox. with()


```
Microsandbox::Sandbox.with(name, **options) { |sandbox| } # => Object
```


Example


```
Microsandbox::Sandbox.with("worker", image: "alpine") do |sandbox|
  puts sandbox.exec("echo", ["hello"]).stdout
end
```


Create a sandbox and yield it to the block. Gracefully stop it when the block exits, including on an exception. This does not remove persisted sandbox state. Without a block, return the created sandbox.


Parameters


`name` String Sandbox name. `options` Hash The same creation options as create().


Returns


Object The block result, or a Sandbox when no block is supplied.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#microsandboxsandbox-connect_or_create) Microsandbox::Sandbox. connect_or_create()


```
Microsandbox::Sandbox.connect_or_create(name, **options) # => Sandbox
```


Reuse or create the sandbox with this name. The method connects when it is running, waits while it is starting, starts it when it is created, stopped, or crashed, and creates it only when the name is unused. Options apply only to a new sandbox, and concurrent callers reuse the same sandbox. Replace options are rejected because they request a different sandbox.


Example


```
sandbox = Microsandbox::Sandbox.connect_or_create(
  "worker",
  image: "python",
  memory: 1024,
  env: { "ROLE" => "worker" }
)
```


Use `Sandbox.create` when name conflicts must remain an error, or explicit replace options when the old identity should be discarded.


Parameters


`name` String Sandbox name. `options` Hash Creation options, applied only when creating a new sandbox.


Returns


Sandbox Live sandbox connection.
## Documentation Index
## ​Sandbox
## ​SandboxBuilder
## ​SandboxHandle
## ​SandboxMetrics
## ​Stop result
## ​Identity errors
## ​Installation requirements
## ​Managed jobs











Instance methods


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-name) sandbox. name


```
sandbox.name # => String
```


Returns


String Sandbox name.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-owns_lifecycle) sandbox. owns_lifecycle?


```
sandbox.owns_lifecycle? # => Boolean
```


Returns


Boolean Whether this connection owns the sandbox lifecycle.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-backend) sandbox. backend


```
sandbox.backend # => String
```


Returns


String Selected backend: local or cloud.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-status) sandbox. status


```
sandbox.status # => String
```


Returns


String Current lifecycle status, fetched from the backend: `created`, `starting`, `running`, `draining`, `paused`, `stopped`, or `crashed`.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-last_failure_message) sandbox. last_failure_message


```
sandbox.last_failure_message # => String | nil
```


Returns


String | nil Most recent recorded failure, if available.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-kill) sandbox. kill()


```
sandbox.kill(timeout: nil) # => nil
```


Force termination and wait for shutdown. Omit timeout for an unbounded wait. Force termination is local-only.


Parameters


`timeout` Numeric Optional finite, non-negative timeout in seconds. May also be passed positionally, but not both ways.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-wait_until_stopped) sandbox. wait_until_stopped()


```
sandbox.wait_until_stopped # => Hash
```


Wait for termination without a built-in timeout.


Returns


Hash Stop result with string keys; see Stop result below.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-ping) sandbox. ping()


```
sandbox.ping # => Hash
```


Check sandbox responsiveness.


Returns


Hash String keys: name (String) and latency_ms (Integer).


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-touch) sandbox. touch()


```
sandbox.touch # => Hash
```


Record activity to refresh the sandbox idle timer.


Returns


Hash String keys: name (String) and activity_seq (Integer).


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-metrics) sandbox. metrics()


```
sandbox.metrics # => SandboxMetrics
```


Read a metrics sample.


Returns


SandboxMetrics Metrics sample; call to_h for its fields.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-request_kill) sandbox. request_kill()


```
sandbox.request_kill # => nil
```


Request forced termination without waiting for shutdown. Local-only.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-detach) sandbox. detach()


```
sandbox.detach # => nil
```


Detach from the local runtime. This consumes the live connection; subsequent operations on it fail.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-stop) sandbox. stop()


```
sandbox.stop # => nil
sandbox.stop(timeout: 30) # Existing optional bounded form
```


Request graceful shutdown and wait for this exact sandbox run to finish, including local runtime ownership release. There is no built-in deadline or automatic force-kill. A supplied `timeout:` bounds the wait without changing graceful shutdown into forced termination. These semantics require the matching updated native extension and runtime.


Parameters


`timeout` Numeric Optional finite, non-negative deadline in seconds; no deadline when omitted.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-stop_with_timeout) sandbox. stop_with_timeout()


```
sandbox.stop_with_timeout(seconds) # => nil
```


Bound graceful shutdown with an explicit finite, non-negative timeout. The deadline covers local transition ownership, request dispatch, and termination observation. Expiry raises `Microsandbox::Error` without force-killing; zero expires before sending a request. Call `kill` separately when forced termination is intended.


Parameters


`seconds` Numeric Finite, non-negative timeout in seconds.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-request_stop) sandbox. request_stop()


```
sandbox.request_stop # => nil
```


Send the graceful shutdown request without waiting for termination or scheduling a force-kill. Pair with `wait_until_stopped` to observe completion.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-id) sandbox. id


```
sandbox.id # => String
```


Opaque stable identity of the persisted sandbox. It remains unchanged across stop and restart and changes when a removed name is recreated. Use it for equality, logging, and correlation; do not parse it.


Returns


String Stable sandbox identity.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-wait_for_status) sandbox. wait_for_status()


```
sandbox.wait_for_status(status) # => SandboxHandle
```


Wait without a built-in timeout until this exact sandbox reaches the requested [lifecycle status](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-status). Returns a refreshed metadata handle. Ruby’s `Timeout.timeout` does not reliably interrupt the native wait. Use an SDK operation with an explicit timeout when you need a bounded shutdown.


Parameters


`status` String Target lifecycle status.


Returns


SandboxHandle Refreshed metadata handle.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-restart) sandbox. restart()


```
sandbox.restart(force: false, timeout: nil, detached: false) # => Sandbox
```


Restart this exact sandbox. Defaults to graceful shutdown, the SDK’s ten-second timeout, and attached local start. A created, stopped, or crashed sandbox starts directly; a starting sandbox is observed until it settles. Set `force: true` to kill, `timeout:` in seconds to change how long shutdown can take, or `detached: true` for a local background start.
On microsandbox cloud, graceful restart is supported, but timeout expiry cannot escalate to force kill. `force: true` is local-only, and `detached:` affects only local process ownership.


Parameters


`force` Boolean Use forced termination; defaults to false and is local-only. `timeout` Numeric | nil Shutdown timeout in seconds; nil uses the SDK default of ten seconds. `detached` Boolean Start locally in the background; defaults to false.


Returns


Sandbox Live connection to the restarted sandbox.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-destroy) sandbox. destroy()


```
sandbox.destroy(force: false, timeout: nil) # => nil
```


Stop and remove this exact sandbox. Defaults to graceful shutdown with the SDK’s ten-second timeout. Identity checks refuse to delete a same-name replacement.


Parameters


`force` Boolean Use forced termination; defaults to false. `timeout` Numeric | nil Shutdown timeout in seconds; nil uses the SDK default of ten seconds.


Returns


nil No return value.


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandboxbuilder) SandboxBuilder


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-image) builder. image()


```
builder.image(value) # => SandboxBuilder
```


OCI image reference.


Parameters


`value` String OCI image reference.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-cpus) builder. cpus()


```
builder.cpus(value) # => SandboxBuilder
```


Initial virtual CPU count.


Parameters


`value` Integer Initial virtual CPU count.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-max_cpus) builder. max_cpus()


```
builder.max_cpus(value) # => SandboxBuilder
```


Maximum virtual CPU count.


Parameters


`value` Integer Maximum virtual CPU count.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-memory) builder. memory()


```
builder.memory(value) # => SandboxBuilder
```


Initial memory in MiB.


Parameters


`value` Integer Initial memory in MiB.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-max_memory) builder. max_memory()


```
builder.max_memory(value) # => SandboxBuilder
```


Maximum memory in MiB.


Parameters


`value` Integer Maximum memory in MiB.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-env) builder. env()


```
builder.env(key, value) # => SandboxBuilder
```


Environment variables with string keys and values.


Parameters


`key` String Environment variable name. `value` String Environment variable value.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-workdir) builder. workdir()


```
builder.workdir(value) # => SandboxBuilder
```


Guest working directory.


Parameters


`value` String Guest working directory.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-shell) builder. shell()


```
builder.shell(value) # => SandboxBuilder
```


Shell used for shell commands.


Parameters


`value` String Shell used for shell commands.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-hostname) builder. hostname()


```
builder.hostname(value) # => SandboxBuilder
```


Guest hostname.


Parameters


`value` String Guest hostname.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-user) builder. user()


```
builder.user(value) # => SandboxBuilder
```


Guest user.


Parameters


`value` String Guest user.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-intercept_tls) builder. intercept_tls()


```
builder.intercept_tls # => SandboxBuilder
```


Enable [TLS interception](https://docs.microsandbox.dev/networking/tls) while preserving existing network settings. `Sandbox.create` also accepts `intercept_tls: true`.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-detached) builder. detached()


```
builder.detached(value) # => SandboxBuilder
```


Start locally in the background.


Parameters


`value` Boolean Start locally in the background.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-ephemeral) builder. ephemeral()


```
builder.ephemeral(value) # => SandboxBuilder
```


Remove sandbox state when its lifecycle ends.


Parameters


`value` Boolean Remove sandbox state when its lifecycle ends.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-max_duration) builder. max_duration()


```
builder.max_duration(value) # => SandboxBuilder
```


Maximum lifetime in seconds.


Parameters


`value` Integer Maximum lifetime in seconds.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-idle_timeout) builder. idle_timeout()


```
builder.idle_timeout(value) # => SandboxBuilder
```


Idle timeout in seconds.


Parameters


`value` Integer Idle timeout in seconds.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-replace) builder. replace()


```
builder.replace # => SandboxBuilder
```


Replace an existing sandbox with this name.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-root_disk) builder. root_disk()


```
builder.root_disk(value) # => SandboxBuilder
```


Managed root disk size in MiB.


Parameters


`value` Integer Managed root disk size in MiB.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-disable_network) builder. disable_network()


```
builder.disable_network # => SandboxBuilder
```


Disable sandbox networking.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-proxy) builder. proxy()


```
builder.proxy(value) # => SandboxBuilder
```


SOCKS proxy configuration; see the Networking reference.


Parameters


`value` OutboundProxy SOCKS proxy configuration; see the Networking reference.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-quiet_logs) builder. quiet_logs()


```
builder.quiet_logs # => SandboxBuilder
```


Suppress sandbox log output.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-entrypoint) builder. entrypoint()


```
builder.entrypoint(value) # => SandboxBuilder
```


Override the image entrypoint; creation does not execute it.


Parameters


`value` Array<String> Override the image entrypoint; creation does not execute it.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-init) builder. init()


```
builder.init(value) # => SandboxBuilder
```


Guest init program.


Parameters


`value` String Guest init program.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-label) builder. label()


```
builder.label(key, value) # => SandboxBuilder
```


Add a label.


Parameters


`key` String Label key. `value` String Label value.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-replace_with_timeout) builder. replace_with_timeout()


```
builder.replace_with_timeout(seconds) # => SandboxBuilder
```


Replace an existing sandbox with a bounded wait.


Parameters


`seconds` Numeric Finite, non-negative timeout in seconds.


Returns


SandboxBuilder The builder, for chaining.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-create) builder. create()


```
builder.create # => Sandbox
```


Example


```
sandbox = Microsandbox::Sandbox.builder("worker")
  .image("alpine")
  .memory(512)
  .create
```


Create and start the configured sandbox. This consumes the builder; it cannot be reused.


Returns


Sandbox Live sandbox connection.
The chainable setters above also have bang forms, such as `image!`, which mutate the builder and return `nil`. See [VSock](https://docs.microsandbox.dev/sdk/ruby/vsock) for `vsock` and `vsock_dgram`. Network allowlists, secret entries, pull policy, scripts, and slug are creation keywords, not Ruby builder methods.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-connect_or_create) builder. connect_or_create()


```
Microsandbox::Sandbox.builder(name).connect_or_create # => Sandbox
```


Create or reuse the configured sandbox, with the same behavior as `Microsandbox::Sandbox.connect_or_create`. This consumes the builder.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#builder-http) builder. http()


```
builder.http { |h| h.deny_response(true).deny_message(message) } # => SandboxBuilder
```


Denial responses are disabled by default. Call `h.deny_response(true)` to enable readable `403` responses. Optionally set `deny_message` to customize the body; `{host}` names the blocked hostname. Setting a message alone does not enable responses. Enabling requires a supporting local runtime; cloud rejects it. See [HTTP denial responses](https://docs.microsandbox.dev/networking/overview#what-a-denied-http-request-sees) for which requests receive a response.


Example


```
builder = Microsandbox::Sandbox.builder("agent")
  .image("python")
  .http { |h| h.deny_response(true).deny_message("{host} is blocked. Ask the user to allow it.") }
```

The same option is available when creating a sandbox:

```
Microsandbox::Sandbox.create(
  "agent",
  image: "python",
  network: { allowed_hosts: ["example.com"], allowed_ports: [80, 443] },
  http: { deny_response: true, deny_message: "{host} is blocked. Ask the user to allow it." }
)
```


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandboxhandle) SandboxHandle


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-name) handle. name


```
handle.name # => String
```


Returns


String Sandbox name.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-status) handle. status


```
handle.status # => String
```


Returns


String Status captured by this metadata handle. Call refresh for current metadata.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-config_json) handle. config_json


```
handle.config_json # => String
```


Returns


String Saved desired configuration as JSON.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-active_config_json) handle. active_config_json


```
handle.active_config_json # => String | nil
```


Returns


String | nil Configuration used for the active run, when available.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-last_failure_message) handle. last_failure_message


```
handle.last_failure_message # => String | nil
```


Returns


String | nil Failure message captured by this handle, if available.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-kill) handle. kill()


```
handle.kill(timeout: nil) # => nil
```


Force termination and wait for shutdown. Omit timeout for an unbounded wait. Force termination is local-only.


Parameters


`timeout` Numeric Optional finite, non-negative timeout in seconds. May also be passed positionally, but not both ways.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-wait_until_stopped) handle. wait_until_stopped()


```
handle.wait_until_stopped # => Hash
```


Wait for termination without a built-in timeout.


Returns


Hash Stop result with string keys; see Stop result below.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-ping) handle. ping()


```
handle.ping # => Hash
```


Check sandbox responsiveness.


Returns


Hash String keys: name (String) and latency_ms (Integer).


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-touch) handle. touch()


```
handle.touch # => Hash
```


Record activity to refresh the sandbox idle timer.


Returns


Hash String keys: name (String) and activity_seq (Integer).


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-metrics) handle. metrics()


```
handle.metrics # => SandboxMetrics
```


Read a metrics sample.


Returns


SandboxMetrics Metrics sample; call to_h for its fields.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-refresh) handle. refresh()


```
handle.refresh # => SandboxHandle
```


Fetch current metadata for this sandbox.


Returns


SandboxHandle A refreshed handle; assign the returned value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-connect) handle. connect()


```
handle.connect # => Sandbox
```


Connect to the running sandbox without starting it.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-start) handle. start()


```
handle.start(detached: false) # => Sandbox
```


Start this existing sandbox.


Parameters


`detached` Boolean Start locally in the background; defaults to false.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-remove) handle. remove()


```
handle.remove # => nil
```


Remove this stopped sandbox. The handle remains bound to its original identity.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-id) handle. id


```
handle.id # => String
```


Opaque stable identity captured by this handle. Receiver lifecycle calls remain bound to this value.


Returns


String Stable sandbox identity.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-stop) handle. stop()


```
handle.stop # No built-in deadline
handle.stop(timeout: 30) # Existing optional bounded form
```


Request graceful shutdown for this exact sandbox run and wait for termination and local runtime ownership release. `stop` has no built-in timeout. Both bounded forms raise `Microsandbox::Error` on expiry without force-killing; zero expires before sending a request. A stale identity is refused rather than stopping a replacement. On cloud, a timeout limits the SDK wait; an accepted stop may continue server-side.


Parameters


`timeout` Numeric Optional finite, non-negative deadline in seconds; no deadline when omitted.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-stop_with_timeout) handle. stop_with_timeout()


```
handle.stop_with_timeout(seconds) # => nil
```


Request graceful shutdown and wait up to the supplied deadline. Timeout does not force-kill the sandbox; zero expires before sending a request.


Parameters


`seconds` Numeric Finite, non-negative timeout in seconds.


Returns


nil No return value.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-connect_or_start) handle. connect_or_start()


```
handle.connect_or_start(detached: false) # => Sandbox
```


Connect when this exact sandbox is running, wait through `starting`, or start it when it is `created`, `stopped`, or `crashed`. `draining` and `paused` are rejected. `detached: true` affects only a required local start; connecting to an already-running sandbox does not change ownership.


Parameters


`detached` Boolean Start locally in the background if needed; defaults to false.


Returns


Sandbox Live sandbox connection.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-wait_for_status) handle. wait_for_status()


```
handle.wait_for_status(status) # => SandboxHandle
```


Wait until this exact sandbox reaches `status`, returning a refreshed handle. The method does not have a built-in timeout.


Parameters


`status` String Target lifecycle status.


Returns


SandboxHandle Refreshed metadata handle.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-restart) handle. restart()


```
handle.restart(force: false, timeout: nil, detached: false) # => Sandbox
```


Restart this exact sandbox with the same state and option semantics as `Sandbox#restart`.


Parameters


`force` Boolean Use forced termination; defaults to false and is local-only. `timeout` Numeric | nil Shutdown timeout in seconds; nil uses the SDK default of ten seconds. `detached` Boolean Start locally in the background; defaults to false.


Returns


Sandbox Live connection to the restarted sandbox.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#handle-destroy) handle. destroy()


```
handle.destroy(force: false, timeout: nil) # => nil
```


Stop and remove this exact sandbox. A stale handle refuses to destroy a replacement that reused the name.


Parameters


`force` Boolean Use forced termination; defaults to false. `timeout` Numeric | nil Shutdown timeout in seconds; nil uses the SDK default of ten seconds.


Returns


nil No return value.


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandboxmetrics) SandboxMetrics


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#metrics-to_h) metrics. to_h()


```
metrics.to_h # => Hash
```


Example


```
sample = sandbox.metrics.to_h
puts sample["memory_bytes"]
```


Return the metrics sample as a hash with string keys.


Returns


Hash Metrics fields below.


Fields


`cpu_percent` Float CPU utilization percentage. `vcpu_time_ns` Integer Accumulated virtual CPU time in nanoseconds. `memory_bytes` Integer Memory usage in bytes. `memory_limit_bytes` Integer Memory limit in bytes. `disk_read_bytes` Integer Bytes read from disk. `disk_write_bytes` Integer Bytes written to disk. `net_rx_bytes` Integer Network bytes received. `net_tx_bytes` Integer Network bytes sent. `uptime_ms` Integer Uptime in milliseconds. `timestamp` String RFC 3339 sample timestamp.


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#stop-result) Stop result


Fields


`name` String Sandbox name. `status` String Observed terminal status. `exit_code` Integer | nil Exit code, if available. `signal` Integer | nil Termination signal, if available. `observed_at` String RFC 3339 observation timestamp. `source` String | nil Source of the termination observation.


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#identity-errors) Identity errors


Stale handles raise `Microsandbox::SandboxReplacedError` rather than acting on a replacement with the same name. See [Error handling](https://docs.microsandbox.dev/sdk/errors#when-a-sandbox-object-is-stale).


Example


```
begin
  stale_handle.destroy
rescue Microsandbox::SandboxReplacedError => error
  warn error.message
end
```


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#installation-requirements) Installation requirements


```
gem install microsandbox
```


Ruby 3.3, 3.4, and 4.0 are supported. When a matching platform gem is available, it carries the native extension; otherwise the source gem requires Rust 1.85 or newer to build it locally.
Blocking native calls release Ruby’s global VM lock (GVL), allowing other Ruby threads to run.


Example


```
require "microsandbox"

Microsandbox.install unless Microsandbox.installed?
```


## [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#managed-jobs) Managed jobs


Run and reconnect to background commands. See [Background jobs](https://docs.microsandbox.dev/sandboxes/commands#background-jobs) for lifecycle, retention, and runtime limits.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-exec_detached) sandbox. exec_detached()


```
sandbox.exec_detached(cmd, args = [], **options) # => Job
```


Start a job after confirming guest startup. Accepts the `exec` options: `cwd`, `user`, `env`, `timeout`, `stdin`, `tty`, and `rlimits`. Stdin defaults to `:pipe`; `:null` closes it, and a String supplies at most 64 KiB followed by EOF.


Example


```
job = sb.exec_detached("cat", cwd: "/tmp")
io = job.attach
io.write_stdin("hello\n")
io.detach
found = sb.get_job(job.id)
found.eof
result = found.wait
output = found.logs
page = sb.list_jobs(all: true, limit: 50)
```


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-get_job) sandbox. get_job()


```
sandbox.get_job(id) # => Job
```


Retrieve a retained job by ID. Also available on `SandboxHandle`.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#sandbox-list_jobs) sandbox. list_jobs()


```
sandbox.list_jobs(all: false, limit: 50, cursor: nil) # => JobPage
```


List active jobs, or include retained history with the all option. Returns items and a next-page cursor. Default page size: 50; range: 1–100. Also available on `SandboxHandle`.


### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job) Job


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-id) job. id


```
job.id # => String
```


The job ID within its sandbox.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-inspect) job. inspect


```
job.inspect # => JobInfo
```


Read current metadata without starting a stopped sandbox.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-wait) job. wait


```
job.wait # => JobExit
```


Wait for a confirmed exit without consuming output. The result contains the exit code, success flag, and timeout flag. Blocking operations release the Ruby GVL.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-signal) job. signal


```
job.signal(signal) # => nil
```


Send a Linux signal to the process group.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-kill) job. kill


```
job.kill # => nil
```


Request SIGKILL. Wait separately to confirm exit.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-eof) job. eof


```
job.eof # => nil
```


Permanently close pipe input after accepted bytes. PTYs reject this operation; use terminal control characters instead.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-logs) job. logs


```
job.logs(tail: nil, since: nil, until: nil, sources: [], from_cursor: nil) # => Array<JobLogEntry>
```


Read retained output. Entries contain original bytes, a source, a Unix-millisecond timestamp, and an opaque cursor belonging to this job. `since` is inclusive and `until` exclusive, both in Unix milliseconds; `from_cursor` cannot be combined with `since`.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-log_stream) job. log_stream


```
job.log_stream(tail: nil, since: nil, until: nil, sources: [], from_cursor: nil, follow: false) # => JobLogStream
```


Read retained output and optionally follow new records. Use `each` for automatic cleanup or close the stream explicitly.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-follow_logs) job. follow_logs


```
job.follow_logs(**options) # => JobLogStream
```


Stream logs with following enabled. Accepts the same filters as `logs`.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#job-attach) job. attach


```
job.attach(read_only: false, replay_bytes: nil, cursor: nil) # => JobAttachment
```


Attach to live I/O. Only one attachment may own input; read-only observers may coexist. Recent-byte replay and cursor replay are alternatives.


### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#jobattachment) JobAttachment


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#attachment-recv) attachment. recv


```
attachment.recv # => JobEvent or nil
```


Read an output, history-gap, or completion event. `each` iterates events and detaches on exit. Input and output can run on separate Ruby threads.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#attachment-write_stdin) attachment. write_stdin


```
attachment.write_stdin(bytes) # => nil
```


Write a String of up to 16 KiB through the input-owning attachment.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#attachment-resize) attachment. resize


```
attachment.resize(rows, cols) # => nil
```


Resize the job terminal. Each dimension must fit an unsigned 16-bit integer.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#attachment-detach) attachment. detach


```
attachment.detach # => nil
```


Release the attachment when finished. The job and its input remain open. `close` is an alias.


### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#joblogstream) JobLogStream


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#stream-next) stream. next


```
stream.next # => JobLogEntry or nil
```


Read the next log entry. `each` iterates entries and closes the stream on exit.


#### [​](https://docs.microsandbox.dev/sdk/ruby/sandbox#stream-close) stream. close


```
stream.close # => nil
```


Stop observing logs. This does not stop the job.

Was this page helpful?

Yes No ⌘ I

---

# Go SDK Sandbox reference

`https://docs.microsandbox.dev/sdk/go/sandbox`

See [Overview](https://docs.microsandbox.dev/sandboxes/overview) for configuration examples and [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle) for state management.

See [Snapshots](https://docs.microsandbox.dev/sdk/go/snapshots#forking) for live fork methods.


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#functions) Functions


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox) m. CreateSandbox()


```
func CreateSandbox(ctx context.Context, name string, opts ...SandboxOption) (*Sandbox, error)
```


Example


```
sb, err := m.CreateSandbox(ctx, "api",
    m.WithImage("python:3.12"),
    m.WithMemory(512),
    m.WithCPUs(2),
    m.WithEnv(map[string]string{"PYTHONDONTWRITEBYTECODE": "1"}),
)
if err != nil {
    return err
}
defer func() {
    _ = sb.Stop(context.Background())
    _ = sb.Close()
}()
```


Create and boot a new sandbox. Pulls the image if needed, boots the VM, starts the guest agent, and waits until it is ready to accept commands. Sandbox names must be non-empty and no longer than 128 UTF-8 bytes. The returned [`*Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) owns the VM process. Call `Close` (or `Stop` + `Close`) when done. See [Options](https://docs.microsandbox.dev/sdk/go/sandbox#options) for all configuration knobs.


Parameters


`ctx` context.Context Cancels the boot operation only. Cancelling after this function returns has no effect on the running sandbox. `name` string Sandbox name, up to 128 UTF-8 bytes. `opts` […SandboxOption](https://docs.microsandbox.dev/sdk/go/sandbox#options) Functional options applied in order.


Returns


[*Sandbox](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) Running sandbox. Safe for concurrent use from multiple goroutines. error Typed `*Error`, see [Error handling](https://docs.microsandbox.dev/sdk/errors).


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-connectorcreatesandbox) m. ConnectOrCreateSandbox()


```
func ConnectOrCreateSandbox(ctx context.Context, name string, opts ...SandboxOption) (*Sandbox, error)
```


Reuse or create the sandbox with this name. The function connects when it is running, waits while it is starting, starts it when it is created, stopped, or crashed, and creates it only when the name is unused. Options apply only to a new sandbox. Concurrent callers reuse the same sandbox. `WithReplace` and `WithReplaceWithTimeout` are invalid with this function.


Parameters


- `ctx`: controls this operation; cancellation does not stop a sandbox already returned.
- `name`: reusable sandbox name, up to 128 UTF-8 bytes.
- `opts`: the same creation options accepted by [`CreateSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox), used only when creation is necessary.


Returns


`(*` [`Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-getsandbox) m. GetSandbox()


```
func GetSandbox(ctx context.Context, name string) (*SandboxHandle, error)
```


Example


```
h, err := m.GetSandbox(ctx, "api")
if err != nil {
    return err
}
fmt.Println(h.Status())
```


Look up a sandbox by name and return a metadata handle without connecting to it. Returns an error with `Kind == ErrSandboxNotFound` if no such sandbox exists. The returned [`*SandboxHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle) exposes `Connect`, `Start`, `Stop`, `Kill`, `Remove`, `Ping`, `Touch`, `Metrics`, `Logs`, and snapshot methods.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


[*SandboxHandle](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle) Metadata handle with status and lifecycle control.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxes) m. ListSandboxes()


```
func ListSandboxes(ctx context.Context) (*SandboxPage, error)
```


Example


```
page, err := m.ListSandboxes(ctx)
if err != nil {
    return err
}
for _, h := range page.Sandboxes {
    fmt.Printf("%s - %s\n", h.Name(), h.Status())
}
```


Return the first page of known sandboxes (running, stopped, draining, crashed), ordered newest first. The default page size is 20.


Returns


*SandboxPage Handles in this page and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxeswith) m. ListSandboxesWith()


```
func ListSandboxesWith(ctx context.Context, options ...SandboxListOption) (*SandboxPage, error)
```


Example


```
page, err := m.ListSandboxesWith(
    ctx,
    m.WithListLimit(50),
    m.WithListLabels(map[string]string{"user.id": "alice"}),
)
if err != nil {
    return err
}
if page.NextCursor != nil {
    nextPage, err := m.ListSandboxesWith(
        ctx,
        m.WithListLimit(50),
        m.WithListCursor(*page.NextCursor),
        m.WithListLabels(map[string]string{"user.id": "alice"}),
    )
}
```


Return a configured page of sandbox metadata. Label selectors are applied before pagination and AND-matched.


Parameters


`options` …SandboxListOption `WithListLimit`, `WithListCursor`, and/or `WithListLabels` options.


Returns


*SandboxPage Matching handles and an optional cursor for the next page.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-startsandbox) m. StartSandbox()


```
func StartSandbox(ctx context.Context, name string) (*Sandbox, error)
```


Example


```
sb, err := m.StartSandbox(ctx, "api")
```


Restart a previously stopped sandbox. The VM reboots using the persisted configuration and returns a live [`*Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox).


Parameters


`name` string Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[*Sandbox](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) Running sandbox.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-startsandboxdetached) m. StartSandboxDetached()


```
func StartSandboxDetached(ctx context.Context, name string) (*Sandbox, error)
```


Boot a stopped sandbox in detached mode. The VM keeps running after the returned handle is released.


Parameters


`name` string Name of a stopped sandbox, up to 128 UTF-8 bytes.


Returns


[*Sandbox](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) Running sandbox in detached mode.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-removesandbox) m. RemoveSandbox()


```
func RemoveSandbox(ctx context.Context, name string) error
```


Example


```
err := m.RemoveSandbox(ctx, "api")
```


Delete a stopped sandbox by name. See [Destroy or remove](https://docs.microsandbox.dev/sandboxes/lifecycle#destroy-or-remove) for the exact local deletion scope and the external resources that are preserved. Fails if the sandbox is still running; stop it first.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#m-allsandboxmetrics) m. AllSandboxMetrics()


Local-only


```
func AllSandboxMetrics(ctx context.Context) (map[string]*Metrics, error)
```


Example


```
all, err := m.AllSandboxMetrics(ctx)
for name, metrics := range all {
    fmt.Printf("%s: %.1f%% CPU\n", name, metrics.CPUPercent)
}
```


Return a point-in-time [`Metrics`](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) snapshot for every running sandbox, keyed by sandbox name. Only running and draining sandboxes appear.


Returns


[map[string]*Metrics](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) Per-sandbox metrics keyed by name.


See [Runtime setup](https://docs.microsandbox.dev/sdk/setup#resolve-check-install-and-ensure) for runtime installation and verification helpers. See [Inspect Go versions](https://docs.microsandbox.dev/sdk/setup#inspect-go-versions) for the Go-only version helpers.


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) Sandbox


A live sandbox connection that is safe for concurrent use.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-name) sb. Name()


```
func (s *Sandbox) Name() string
```


Return the sandbox name.


Returns


string Sandbox name, up to 128 UTF-8 bytes.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-id) sb. ID()


```
func (s *Sandbox) ID() string
```


Return the opaque stable identity of this persisted sandbox. It remains unchanged across stop and restart and changes when the reusable name is removed and recreated. Use it for equality, logging, and correlation; do not parse it.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-fs) sb. FS()


```
func (s *Sandbox) FS() *SandboxFSOps
```


Example


```
err := sb.FS().Write(ctx, "/tmp/hello.txt", []byte("hi"))
```


Return a filesystem accessor for reading and writing files inside the running sandbox. See [Filesystem](https://docs.microsandbox.dev/sdk/go/filesystem) for the API.


Returns


[*SandboxFSOps](https://docs.microsandbox.dev/sdk/go/filesystem) Filesystem accessor.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ssh) sb. SSH()


```
func (s *Sandbox) SSH() *SandboxSSHOps
```


Example


```
client, err := sb.SSH().OpenClient(ctx)
```


Return an SSH accessor for opening a native in-process SSH client or preparing a reusable SSH server endpoint against the running sandbox. See [SSH](https://docs.microsandbox.dev/sdk/go/ssh) for the API.


Returns


[*SandboxSSHOps](https://docs.microsandbox.dev/sdk/go/ssh) SSH accessor.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logs) sb. Logs()


Local-only


```
func (s *Sandbox) Logs(ctx context.Context, opts LogOptions) ([]LogEntry, error)
```


Example


```
entries, err := sb.Logs(ctx, m.LogOptions{
    Sources: []m.LogSource{m.LogSourceStdout, m.LogSourceStderr},
})
for _, e := range entries {
    fmt.Printf("[%s] %s", e.Source, e.Text())
}
```


Read persisted output from the sandbox’s `exec.log`. Backed by an on-disk file, so it works for running and stopped sandboxes alike without guest-agent protocol traffic. The default sources are stdout and stderr; add `LogSourceOutput` for PTY-merged output or `LogSourceSystem` for runtime and kernel diagnostics. The same method exists on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle) for callers that don’t want to start the sandbox first.


Parameters


`opts` [LogOptions](https://docs.microsandbox.dev/sdk/go/sandbox#logoptions) Filters: `Tail`, `Since`, `Until`, `Sources`. The zero value returns everything for the default stdout and stderr sources.


Returns


[[]LogEntry](https://docs.microsandbox.dev/sdk/go/sandbox#logentry) Matching entries in chronological order.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logstream) sb. LogStream()


Limited on cloud


```
func (s *Sandbox) LogStream(ctx context.Context, opts LogStreamOptions) (*LogStreamHandle, error)
```


Example


```
stream, err := sb.LogStream(ctx, m.LogStreamOptions{Follow: true})
if err != nil {
    return err
}
defer stream.Close()
for {
    entry, err := stream.Recv(ctx)
    if err != nil || entry == nil {
        break
    }
    fmt.Print(entry.Text())
}
```


Start a streaming log subscription against a live sandbox. Pass `LogStreamOptions{Follow: true}` to keep the stream open past current EOF and pick up new entries as they are written. Close the returned [`*LogStreamHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamhandle) when done. Also available on [`SandboxHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle).


Parameters


`opts` [LogStreamOptions](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamoptions) Sources, follow mode, and a `Since` or `FromCursor` start point.


Returns


[*LogStreamHandle](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamhandle) Live subscription; call `Recv` in a loop.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ping) sb. Ping()


Local-only


```
func (s *Sandbox) Ping(ctx context.Context) (*SandboxPingResult, error)
```


Example


```
health, err := sb.Ping(ctx)
if err != nil {
    return err
}
fmt.Printf("%s: %s\n", health.Name, health.Latency)
```


Check that the running sandbox’s guest agent is reachable without refreshing idle activity. This sends `core.ping` and waits for `core.pong`; it does not start stopped sandboxes and returns an error if the sandbox is not running or `agentd` cannot respond. After upgrading from a runtime that predates protocol generation 6, restart already-running sandboxes so the guest agent understands the message.


Returns


[*SandboxPingResult](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxpingresult) Sandbox name and agent round-trip latency.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-touch) sb. Touch()


Local-only


```
func (s *Sandbox) Touch(ctx context.Context) (*SandboxTouchResult, error)
```


Example


```
keepalive, err := sb.Touch(ctx)
if err != nil {
    return err
}
fmt.Printf("%s: %d\n", keepalive.Name, keepalive.ActivitySeq)
```


Explicitly refresh the running sandbox’s idle activity. This sends `core.touch`, receives `core.touched`, and advances the guest activity sequence used by the runtime idle-timeout monitor. It does not start stopped sandboxes and it does not bypass `MaxDuration`.


Returns


[*SandboxTouchResult](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxtouchresult) Sandbox name and updated activity sequence.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-modify) sb. Modify()


Local-only


```
func (s *Sandbox) Modify(ctx context.Context, opts ModifyOptions) (*SandboxModificationPlan, error)
```


Example


```
// Live resize: applies to the running VM when within the booted capacity
plan, err := sb.Modify(ctx, m.ModifyOptions{CPUs: 4, MemoryMiB: 4096})
if err != nil {
    return err
}
for _, r := range plan.ResizeStatus {
    fmt.Printf("%s: %s -> %s (%s)\n", r.Resource, r.Requested, r.Actual, r.State)
}

// Preview a change without applying it
preview, err := sb.Modify(ctx, m.ModifyOptions{MaxMemoryMiB: 16384, DryRun: true})
if err != nil {
    return err
}
for _, c := range preview.Changes {
    fmt.Printf("%s: %s\n", c.Field, c.Disposition)
}

// Make an env change active now by restarting
_, err = sb.Modify(ctx, m.ModifyOptions{
    Env:    map[string]string{"MODE": "prod"},
    Policy: m.ModificationPolicyRestart,
})
// Grow the owned OCI root disk while it is running
_, err = sb.Modify(ctx, m.ModifyOptions{
    RootDiskSizeMiB: 8192,
})

// Add or rotate a host-environment secret; restart if it is newly added
_, err = sb.Modify(ctx, m.ModifyOptions{
    Secrets: map[string]m.SecretModifySpec{
        "API_KEY": {
            Env:          "API_KEY",
            AllowedHosts: []string{"api.example.com"},
        },
    },
    Policy: m.ModificationPolicyRestart,
})

// Remove an existing secret
_, err = sb.Modify(ctx, m.ModifyOptions{
    SecretsRemove: []string{"OLD_API_KEY"},
})
```


Plan or apply a configuration change. The returned plan labels each change `"live"`, `"next start"`, `"requires restart"`, or `"unsupported"`.
`CPUs` and `MemoryMiB` resize live within the [`WithMaxCPUs`](https://docs.microsandbox.dev/sdk/go/sandbox#withmaxcpus) / [`WithMaxMemory`](https://docs.microsandbox.dev/sdk/go/sandbox#withmaxmemory) ceilings; raising a ceiling requires a restart.
`RootDiskSizeMiB` grows owned managed and flat ext4 roots live, including checkpoint-backed roots, tmpfs root disks can change in either direction on the next boot, and user-supplied disk images are rejected.
Env and workdir changes affect future execs only. Stopped roots grow before the new size is saved. Explicit restart and next-start policies remain available.
Secret specs are keyed by stable secret name. Each `SecretModifySpec` selects at most one source (`Env`, `Value`, or `Store`) and may also set `Placeholder` and `AllowedHosts`; omitting a source updates only the other supplied fields. Plans expose only safe references and metadata; raw secret values never appear in a plan. Removal is explicit through `SecretsRemove`.
A live CPU or memory resize can take a moment to settle. The new limits are enforced immediately, and the returned plan’s `ResizeStatus` reports when the sandbox has finished adjusting. See [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxmodificationplan).


Parameters


`opts` [ModifyOptions](https://docs.microsandbox.dev/sdk/go/sandbox#modifyoptions) Requested changes plus `Policy` and `DryRun`. Zero-valued fields are left unchanged.


Returns


[*SandboxModificationPlan](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxmodificationplan) The modification plan, applied unless `DryRun` is set.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-metrics) sb. Metrics()


Local-only


```
func (s *Sandbox) Metrics(ctx context.Context) (*Metrics, error)
```


Example


```
metrics, err := sb.Metrics(ctx)
fmt.Printf("cpu %.1f%% · mem %d MiB\n",
    metrics.CPUPercent, metrics.MemoryBytes/(1<<20))
```


Get a point-in-time snapshot of the sandbox’s resource usage: CPU, memory, disk I/O, network I/O, optional upper-disk usage, and uptime.


Returns


[*Metrics](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) Resource snapshot.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-metricsstream) sb. MetricsStream()


Local-only


```
func (s *Sandbox) MetricsStream(ctx context.Context, interval time.Duration) (*MetricsStreamHandle, error)
```


Example


```
stream, err := sb.MetricsStream(ctx, 500*time.Millisecond)
if err != nil {
    return err
}
defer stream.Close()
for {
    metrics, err := stream.Recv(ctx)
    if err != nil || metrics == nil {
        break
    }
    fmt.Printf("CPU: %.1f%%\n", metrics.CPUPercent)
}
```


Start a streaming metrics subscription that delivers a [`Metrics`](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) snapshot every `interval`. Sub-millisecond precision is rounded up; a zero or negative value uses the runtime minimum (~1 ms). Close the returned [`*MetricsStreamHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#metricsstreamhandle) when done.


Parameters


`interval` time.Duration Time between snapshots.


Returns


[*MetricsStreamHandle](https://docs.microsandbox.dev/sdk/go/sandbox#metricsstreamhandle) Live subscription; call `Recv` in a loop.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attach) sb. Attach()


```
func (s *Sandbox) Attach(ctx context.Context, cmd string, args ...string) (int, error)
```


Bridge the caller’s terminal to a process inside the sandbox for a fully interactive PTY session. Blocks until the process exits and returns its exit code. The caller’s terminal must be a real TTY, so this is primarily useful for CLI tools, not library code.


Parameters


`cmd` string Command to run. `args` …string Command arguments.


Returns


int Exit code of the process.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attachwith) sb. AttachWith()


```
func (s *Sandbox) AttachWith(ctx context.Context, cmd string, args []string, opts ...AttachOption) (int, error)
```


Example


```
exitCode, err := sb.AttachWith(ctx, "bash", []string{"-l"},
    m.WithAttachUser("dev"),
    m.WithAttachCwd("/app"),
    m.WithAttachEnv(map[string]string{"DEBUG": "1"}),
    m.WithAttachDetachKeys("ctrl-q"),
)
```


Same as [`Attach`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attach), but takes [`AttachOption`](https://docs.microsandbox.dev/sdk/go/sandbox#attachoption) values. Use them to run the session as a different guest user, in a different working directory, with extra environment variables, or with custom detach keys.


Parameters


`cmd` string Command to run. `args` []string Command arguments; may be `nil`. `opts` […AttachOption](https://docs.microsandbox.dev/sdk/go/sandbox#attachoption) Attach options.


Returns


int Exit code of the process.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attachshell) sb. AttachShell()


```
func (s *Sandbox) AttachShell(ctx context.Context) (int, error)
```


Attach to the sandbox’s default shell (configured via [`WithShell`](https://docs.microsandbox.dev/sdk/go/sandbox#withshell), defaults to `/bin/sh`). Blocks until the shell exits and returns its exit code.


Returns


int Exit code of the shell.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stop) sb. Stop()


Different on cloud


```
func (s *Sandbox) Stop(ctx context.Context, opts ...StopOption) error
```


Example


```
err := sb.Stop(ctx)
```


Request graceful shutdown and wait for the same sandbox run to finish, including local runtime ownership release. There is no built-in deadline and no automatic force-kill. Cancelling `ctx` ends the wait without force-killing. Use [`StopWithTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stopwithtimeout) or [`WithStopTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#withstoptimeout) for a bounded wait. These semantics require the matching updated native SDK and runtime; an older native library returns an unsupported-operation error.


Parameters


`opts` […StopOption](https://docs.microsandbox.dev/sdk/go/sandbox#withstoptimeout) Optional wait deadline, e.g. `WithStopTimeout(30 * time.Second)`; expiry never force-kills.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stopwithtimeout) sb. StopWithTimeout()


```
func (s *Sandbox) StopWithTimeout(ctx context.Context, timeout time.Duration) error
```


Bound graceful shutdown with an explicit deadline. The deadline includes local transition ownership, request dispatch, and termination observation. Expiry returns `ErrStopTimeout` without force-killing; zero or a negative duration expires before sending a request. Use [`Kill`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-kill) separately when forced termination is intended.


```
err := sb.StopWithTimeout(ctx, 30*time.Second)
```


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-requeststop) sb. RequestStop()


```
func (s *Sandbox) RequestStop(ctx context.Context) error
```


Request graceful shutdown and return once the request is sent, without waiting for the sandbox to reach stopped state or scheduling a force-kill. Pair with [`WaitUntilStopped`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-waituntilstopped) to await termination. A paused sandbox is not force-killed merely because its agent cannot process shutdown.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-kill) sb. Kill()


Local-only


```
func (s *Sandbox) Kill(ctx context.Context, opts ...KillOption) error
```


Example


```
err := sb.Kill(ctx)
```


Force-terminate the sandbox with SIGKILL and wait until stopped state is observed. No graceful shutdown, so pending writes the workload hasn’t `fsync`’d may be lost. Prefer [`Stop`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stop) for graceful shutdown. Defaults to a five-second observation window; pass [`WithKillTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#withkilltimeout) to change it.


Parameters


`opts` […KillOption](https://docs.microsandbox.dev/sdk/go/sandbox#withkilltimeout) Stopped-state observation window.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-requestkill) sb. RequestKill()


Local-only


```
func (s *Sandbox) RequestKill(ctx context.Context) error
```


Request force termination and return once the request is sent, without waiting for the sandbox to reach stopped state.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-requestdrain) sb. RequestDrain()


Local-only


```
func (s *Sandbox) RequestDrain(ctx context.Context) error
```


Request a graceful drain and return once the request is sent. Existing commands run to completion while new exec calls are rejected; the sandbox transitions to stopped when all in-flight commands finish. Useful for zero-downtime rotation of worker sandboxes.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-waituntilstopped) sb. WaitUntilStopped()


```
func (s *Sandbox) WaitUntilStopped(ctx context.Context) (*SandboxStopResult, error)
```


Example


```
result, err := sb.WaitUntilStopped(ctx)
fmt.Printf("ended as %s\n", result.Status)
```


Block until the sandbox is observed in a terminal state, then return how it ended.


Returns


[*SandboxStopResult](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstopresult) Terminal status, exit code, and signal.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-waitforstatus) sb. WaitForStatus()


```
func (s *Sandbox) WaitForStatus(ctx context.Context, status SandboxStatus) (*SandboxHandle, error)
```


Wait until this exact sandbox reaches `status`, returning a refreshed metadata handle. The context supplies cancellation or a deadline. Returns `ErrSandboxReplaced` rather than following a reused name.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-restart) sb. Restart()


```
func (s *Sandbox) Restart(ctx context.Context, opts ...RestartOption) (*Sandbox, error)
```


Restart this exact sandbox. Defaults to graceful shutdown, a ten-second timeout, and attached local start. A created, stopped, or crashed sandbox starts directly; a starting sandbox is observed until it settles. Use `WithRestartForce`, `WithRestartTimeout`, and `WithRestartDetached` for explicit controls.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-destroy) sb. Destroy()


```
func (s *Sandbox) Destroy(ctx context.Context, opts ...DestroyOption) error
```


Stop and remove this exact sandbox. Defaults to graceful shutdown with a ten-second timeout. Use `WithDestroyForce` or `WithDestroyTimeout` for explicit controls. Returns `ErrSandboxReplaced` instead of deleting a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-detach) sb. Detach()


```
func (s *Sandbox) Detach(ctx context.Context) error
```


Example


```
err := sb.Detach(ctx) // keeps running in the background
```


Release the Rust-side handle **without** stopping the VM. Use on sandboxes created with [`WithDetached`](https://docs.microsandbox.dev/sdk/go/sandbox#withdetached) once the caller is done with the handle but the sandbox should keep running in the background. After `Detach`, the handle is invalid; a subsequent `Close` returns an error with `Kind == ErrInvalidHandle`. Reconnect later with [`GetSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-getsandbox).


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-close) sb. Close()


Limited on cloud


```
func (s *Sandbox) Close() error
```


Example


```
defer sb.Close()
```


Release the Rust-side handle. Safe to call multiple times; the second call returns an error with `Kind == ErrInvalidHandle`. A local attached handle stops its VM on `Close`; local detached and cloud handles release client resources only. Stop or remove a cloud sandbox explicitly.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ownslifecycle) sb. OwnsLifecycle()


```
func (s *Sandbox) OwnsLifecycle() (bool, error)
```


Report whether this handle owns the VM process. Local attached handles return `true`; local detached handles and all cloud handles return `false`, because the cloud worker owns the sandbox process. The error return covers stale handles and FFI failures; use [`OwnsLifecycleOrFalse`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ownslifecycleorfalse) for callers that don’t need the error.


Returns


bool `true` for a local attached handle.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ownslifecycleorfalse) sb. OwnsLifecycleOrFalse()


```
func (s *Sandbox) OwnsLifecycleOrFalse() bool
```


Convenience wrapper around [`OwnsLifecycle`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ownslifecycle) that swallows the error and returns `false` for cloud, detached, or invalid handles. Suitable for log lines and best-effort branching.


Returns


bool `true` if attached, `false` on detach or error.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sb-restorewarnings) sb. RestoreWarnings()


```
func (s *Sandbox) RestoreWarnings(ctx context.Context) ([]ExternalMountWarning, error)
```


Return warnings for unavailable external filesystems and accepted restore mismatches. See [External mounts](https://docs.microsandbox.dev/sandboxes/snapshots#external-mounts) for restore options.
Each `ExternalMountWarning` contains:


| Field | Type | Description |
| --- | --- | --- |
| `GuestPath` | `string` | Guest-visible mount path. |
| `Reason` | `string` | Why the resource could not be reconstructed. |
| `StaleInodes` | `[]uint64` | Permanently invalid captured node IDs; empty when the whole export is unavailable. |


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#options) Options


Functional options for creating and listing sandboxes. Map and slice options merge across repeated calls; single-value setters like [`WithImage`](https://docs.microsandbox.dev/sdk/go/sandbox#withimage) replace.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withlistlimit) WithListLimit()


```
func WithListLimit(limit uint32) SandboxListOption
```


Set the maximum number of sandboxes returned in a page. The limit must be between 1 and 100.


Parameters


`limit` uint32 Maximum number of sandboxes in the page.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withlistcursor) WithListCursor()


```
func WithListCursor(cursor string) SandboxListOption
```


Continue listing after a previous page’s `NextCursor`. Keep the same label filters when requesting the next page.


Parameters


`cursor` string Opaque cursor returned by the previous page.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withlistlabels) WithListLabels()


```
func WithListLabels(labels map[string]string) SandboxListOption
```


Require every supplied label. Repeated selectors are AND-matched.


Parameters


`labels` map[string]string Label key-value pairs that every result must match.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withimage) WithImage()


Limited on cloud


```
func WithImage(image string) SandboxOption
```


Set the root filesystem source: an OCI image name, local directory path, or disk image path (e.g. `"python:3.12"`, `"docker.io/library/alpine"`). Required for creation; use `RestoreSandbox` for snapshots. Use [`WithImageDisk`](https://docs.microsandbox.dev/sdk/go/sandbox#withimagedisk) when a disk-image root needs an explicit filesystem type.


Parameters


`image` string OCI image, local path, or disk image.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withrootdisk) WithRootDisk()


```
func WithRootDisk(disk RootDiskConfig) SandboxOption
```


Configure root storage for an OCI image. Construct the value with the [`RootDisk`](https://docs.microsandbox.dev/sdk/go/sandbox#rootdisk) factory.


Example


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12"),
    m.WithRootDisk(m.RootDisk.Managed(8192)),
)
```


Parameters


`disk` RootDiskConfig Managed, tmpfs, user-supplied disk-image, or flat OCI root storage.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withociuppersize) WithOCIUpperSize()


```
func WithOCIUpperSize(mebibytes uint32) SandboxOption
```


Deprecated alias for `WithRootDisk(RootDisk.Managed(mebibytes))`.


Parameters


`mebibytes` uint32 Upper layer size in MiB.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withimagedisk) WithImageDisk()


Local-only


```
func WithImageDisk(path string, fstype string) SandboxOption
```


Use a disk image as the root filesystem and optionally provide the inner filesystem type, e.g. `"ext4"`. The disk format is inferred from the path extension (`.qcow2`, `.raw`, or `.vmdk`).


Parameters


`path` string Host path to the disk image. `fstype` string Inner filesystem hint, empty to auto-detect.


---


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withmemory) WithMemory()


```
func WithMemory(mebibytes uint32) SandboxOption
```


Set the guest memory limit in MiB. This is a limit, not an upfront reservation. Default: `512` MiB.


Parameters


`mebibytes` uint32 Memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withmaxmemory) WithMaxMemory()


Local-only


```
func WithMaxMemory(mebibytes uint32) SandboxOption
```


Set the boot-time maximum hotpluggable guest memory in MiB. This reserves the envelope a sandbox can use after restart-backed changes and future live memory activation; it does not increase the effective memory by itself.


Parameters


`mebibytes` uint32 Maximum memory in MiB.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withthp) WithTHP()


```
func WithTHP(policy THPPolicy) SandboxOption
```


Select the guest transparent huge-page policy applied through the kernel command line at boot. Default: `THPMadvise`.


Parameters


`policy` THPPolicy `THPAlways`, `THPMadvise`, or `THPNever`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withcpus) WithCPUs()


```
func WithCPUs(cpus uint8) SandboxOption
```


Set the number of virtual CPUs. This is a limit, not a reservation. Default: `1`.


Parameters


`cpus` uint8 Number of vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withmaxcpus) WithMaxCPUs()


Local-only


```
func WithMaxCPUs(cpus uint8) SandboxOption
```


Set the boot-time maximum possible virtual CPU capacity. This reserves the envelope a sandbox can use after restart-backed changes and future live CPU activation; it does not increase the effective vCPU count by itself.


Parameters


`cpus` uint8 Maximum possible vCPUs.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withworkdir) WithWorkdir()


```
func WithWorkdir(path string) SandboxOption
```


Set the default working directory for all commands.


Parameters


`path` string Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withshell) WithShell()


```
func WithShell(shell string) SandboxOption
```


Set the shell used by [`Shell`](https://docs.microsandbox.dev/sdk/go/execution) and [`AttachShell`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attachshell). Defaults to `/bin/sh` on most images.


Parameters


`shell` string Shell path, e.g. `“/bin/bash”`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withsecurityprofile) WithSecurityProfile()


```
func WithSecurityProfile(profile SecurityProfile) SandboxOption
```


Set the in-guest security profile. [`SecurityProfileRestricted`](https://docs.microsandbox.dev/sdk/go/sandbox#securityprofile) applies stronger hardening: sets `no_new_privs`, drops mount-admin capability from user commands, and forces `nosuid,nodev` on user mounts.


Parameters


`profile` [SecurityProfile](https://docs.microsandbox.dev/sdk/go/sandbox#securityprofile) Security profile.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withenv) WithEnv()


```
func WithEnv(env map[string]string) SandboxOption
```


Set environment variables visible to all commands. Called repeatedly, the maps merge; later keys overwrite earlier ones.


Parameters


`env` map[string]string Environment variables.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withlabels) WithLabels()


```
func WithLabels(labels map[string]string) SandboxOption
```


Attach labels to the sandbox for metrics attribution and [`ListSandboxesWith`](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxeswith) filtering. Called repeatedly, the maps merge; later keys overwrite earlier ones. Keys must not use the reserved prefixes `sandbox.`, `microsandbox.`, or `service.`.


Parameters


`labels` map[string]string Label key-value pairs.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withlabel) WithLabel()


```
func WithLabel(key, value string) SandboxOption
```


Attach a single label. Shorthand for [`WithLabels`](https://docs.microsandbox.dev/sdk/go/sandbox#withlabels) with one entry.


Parameters


`key` string Label key. `value` string Label value.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withhostname) WithHostname()


Local-only


```
func WithHostname(hostname string) SandboxOption
```


Set the guest hostname.


Parameters


`hostname` string Hostname.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withuser) WithUser()


```
func WithUser(user string) SandboxOption
```


Set the default guest user (UID or name) for all commands.


Parameters


`user` string User name or UID.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withreplace) WithReplace()


Local-only


```
func WithReplace() SandboxOption
```


Replace any existing sandbox with the same name. Sends SIGTERM, waits up to 10s for graceful exit, then escalates to SIGKILL. Without this, creation fails on name conflict. Use [`WithReplaceWithTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#withreplacewithtimeout) to set a different window.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withreplacewithtimeout) WithReplaceWithTimeout()


Local-only


```
func WithReplaceWithTimeout(timeout time.Duration) SandboxOption
```


Like [`WithReplace`](https://docs.microsandbox.dev/sdk/go/sandbox#withreplace) but with a caller-specified timeout between SIGTERM and SIGKILL. Implies `WithReplace`; calling this alone is enough. A zero duration skips SIGTERM and SIGKILLs immediately.


Parameters


`timeout` time.Duration Grace period before SIGKILL.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withdetached) WithDetached()


```
func WithDetached() SandboxOption
```


Create the sandbox in detached mode. The VM continues running after the Go process exits; reattach via [`GetSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-getsandbox). `Close` releases this non-owning handle without stopping the VM.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withephemeral) WithEphemeral()


```
func WithEphemeral(ephemeral bool) SandboxOption
```


Mark whether the runtime should remove the sandbox’s DB row, on-disk state, logs, and captured output after it reaches a terminal status.


Parameters


`ephemeral` bool `true` to delete all state on termination.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withentrypoint) WithEntrypoint()


```
func WithEntrypoint(cmd ...string) SandboxOption
```


Override the image ENTRYPOINT used by default-workload execution. Literal `Exec`, `Attach`, and `Shell` calls ignore it. This is the user workload, **not** the guest PID 1; for that, use [`WithInit`](https://docs.microsandbox.dev/sdk/go/sandbox#withinit) instead.


Parameters


`cmd` …string Entrypoint command and arguments.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withcmd) WithCmd()


```
func WithCmd(cmd ...string) SandboxOption
```


Override the image CMD used by default-workload execution. Calling `WithCmd()` with no arguments explicitly clears the image CMD. This describes durable configuration and does not execute anything during `CreateSandbox`.


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("example/worker:latest"),
    m.WithCmd("worker.py", "--once"),
)
```


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withinit) WithInit()


```
func WithInit(cfg InitConfig) SandboxOption
```


Example


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("jrei/systemd-debian:12"),
    m.WithInit(m.Init.Auto()),
)
```


Hand off PID 1 inside the guest to a custom init binary after agentd finishes boot-time setup. Construct `cfg` via the [`Init`](https://docs.microsandbox.dev/sdk/go/sandbox#init) factory. See [Custom init system](https://docs.microsandbox.dev/sandboxes/bootstrap#custom-init-system) for image picks and shutdown semantics.


Parameters


`cfg` [InitConfig](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) Init specification.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withloglevel) WithLogLevel()


```
func WithLogLevel(level LogLevel) SandboxOption
```


Override the sandbox process’s log verbosity. See [`LogLevel`](https://docs.microsandbox.dev/sdk/go/sandbox#loglevel).


Parameters


`level` [LogLevel](https://docs.microsandbox.dev/sdk/go/sandbox#loglevel) Log level.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withquietlogs) WithQuietLogs()


```
func WithQuietLogs() SandboxOption
```


Suppress sandbox-level log output entirely.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withscripts) WithScripts()


```
func WithScripts(scripts map[string]string) SandboxOption
```


Add named scripts mounted at `/.msb/scripts/<name>` inside the guest. Scripts are added to `PATH` and can be called by name. Called repeatedly, entries merge; later names overwrite earlier ones.


Parameters


`scripts` map[string]string Script name to script content.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withpullpolicy) WithPullPolicy()


```
func WithPullPolicy(p PullPolicy) SandboxOption
```


Control when the OCI image is pulled from the registry. See [`PullPolicy`](https://docs.microsandbox.dev/sdk/go/sandbox#pullpolicy).


Parameters


`p` [PullPolicy](https://docs.microsandbox.dev/sdk/go/sandbox#pullpolicy) Pull behavior.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withmaxduration) WithMaxDuration()


```
func WithMaxDuration(d time.Duration) SandboxOption
```


Cap the sandbox’s total runtime. When exceeded, the sandbox is drained and stopped. Zero means unlimited. Sub-second precision is rounded up to whole seconds. Enforced on the host side.


Parameters


`d` time.Duration Maximum lifetime.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withidletimeout) WithIdleTimeout()


```
func WithIdleTimeout(d time.Duration) SandboxOption
```


Stop the sandbox after this much wall-clock time without exec activity. Zero means unlimited. Sub-second precision is rounded up to whole seconds.


Parameters


`d` time.Duration Idle timeout.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withregistryauth) WithRegistryAuth()


```
func WithRegistryAuth(auth RegistryAuth) SandboxOption
```


Set credentials for pulling from a private OCI registry. See [`RegistryAuth`](https://docs.microsandbox.dev/sdk/go/sandbox#registryauth).


Parameters


`auth` [RegistryAuth](https://docs.microsandbox.dev/sdk/go/sandbox#registryauth) Registry credentials.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withregistryinsecure) WithRegistryInsecure()


Local-only


```
func WithRegistryInsecure() SandboxOption
```


Use plain HTTP for the registry instead of HTTPS, for local or self-hosted registries served without TLS such as `localhost:5050/my-app:latest`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withregistrycacerts) WithRegistryCACerts()


Local-only


```
func WithRegistryCACerts(pem []byte) SandboxOption
```


Trust additional PEM-encoded CA certificates when pulling, for registries served with a private certificate authority. Called repeatedly, the bundles accumulate.


Parameters


`pem` []byte PEM-encoded CA certificates.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withregistrycacertspath) WithRegistryCACertsPath()


Local-only


```
func WithRegistryCACertsPath(path string) SandboxOption
```


Like [`WithRegistryCACerts`](https://docs.microsandbox.dev/sdk/go/sandbox#withregistrycacerts) but reads the PEM bundle from a file. The file is read when [`CreateSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox) runs, which fails if it is unreadable. Called repeatedly, the bundles accumulate.


Parameters


`path` string Path to a PEM file.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withports) WithPorts()


Local-only


```
func WithPorts(ports map[uint16]uint16) SandboxOption
```


Publish guest TCP ports onto host ports (map key = host port, value = guest port). The default host bind address is `127.0.0.1`. Called repeatedly, the maps merge.


Parameters


`ports` map[uint16]uint16 Host port to guest port.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withportsudp) WithPortsUDP()


Local-only


```
func WithPortsUDP(ports map[uint16]uint16) SandboxOption
```


Publish guest UDP ports onto host ports. The default host bind address is `127.0.0.1`.


Parameters


`ports` map[uint16]uint16 Host port to guest port.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withportbindings) WithPortBindings()


Local-only


```
func WithPortBindings(bindings ...PortBinding) SandboxOption
```


Publish ports on explicit host bind addresses, such as `0.0.0.0`. See [`PortBinding`](https://docs.microsandbox.dev/sdk/go/networking#portbinding) for the type definition and UDP examples.


Parameters


`bindings` […PortBinding](https://docs.microsandbox.dev/sdk/go/networking#portbinding) Explicit bind-address port mappings.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withintercepttls) WithInterceptTLS()


```
func WithInterceptTLS() SandboxOption
```


Enable [TLS interception](https://docs.microsandbox.dev/networking/tls) for a local sandbox. Existing network and TLS settings are preserved. A later `WithNetwork()` option replaces the network configuration.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withnetwork) WithNetwork()


```
func WithNetwork(net *NetworkConfig) SandboxOption
```


Example


```
sb, err := m.CreateSandbox(ctx, "api",
    m.WithImage("python"),
    m.WithNetwork(m.NetworkPolicy.FromProfiles(m.NetworkProfilePublic)),
)
```


Configure the network stack: profiles, custom rules, DNS, and TLS interception. Build via the [`NetworkPolicy`](https://docs.microsandbox.dev/sdk/go/networking) factory or a [`*NetworkConfig`](https://docs.microsandbox.dev/sdk/go/networking#networkconfig) literal. See [Networking](https://docs.microsandbox.dev/sdk/go/networking).


Parameters


`net` [*NetworkConfig](https://docs.microsandbox.dev/sdk/go/networking#networkconfig) Network configuration.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withproxy) WithProxy()


```
func WithProxy(proxy *OutboundProxy) SandboxOption
```


Configure the single proxy used for outbound sandbox connections. See [Proxies](https://docs.microsandbox.dev/sdk/go/proxies) for constructors and examples.


Parameters


`proxy` [*OutboundProxy](https://docs.microsandbox.dev/sdk/go/proxies#outboundproxy) Protocol-specific outbound proxy configuration.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withsecrets) WithSecrets()


```
func WithSecrets(secrets ...SecretEntry) SandboxOption
```


Append credential secrets to the sandbox. Secrets never enter the VM; the network proxy substitutes them at the transport layer. Build entries via the [`Secret`](https://docs.microsandbox.dev/sdk/go/secrets) factory. See [Secrets](https://docs.microsandbox.dev/sdk/go/secrets).


Parameters


`secrets` […SecretEntry](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) Secret injection entries.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withpatches) WithPatches()


```
func WithPatches(patches ...PatchConfig) SandboxOption
```


Example


```
sb, err := m.CreateSandbox(ctx, "api",
    m.WithImage("python"),
    m.WithPatches(
        m.Patch.Mkdir("/app", m.PatchOptions{}),
        m.Patch.Text("/app/config.txt", "ready\n", m.PatchOptions{}),
    ),
)
```


Append rootfs patches applied before the VM boots. Patches go into the writable layer; the base image is untouched. Only compatible with OverlayFS rootfs (not disk images). Build entries via the [`Patch`](https://docs.microsandbox.dev/sdk/go/sandbox#patch) factory.


Parameters


`patches` […PatchConfig](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig) Ordered rootfs patches.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withmounts) WithMounts()


```
func WithMounts(mounts map[string]MountConfig) SandboxOption
```


Example


```
sb, err := m.CreateSandbox(ctx, "api",
    m.WithImage("python"),
    m.WithMounts(map[string]m.MountConfig{
        "/data": m.Mount.Named("my-vol", m.MountOptions{}),
        "/tmp":  m.Mount.Tmpfs(m.TmpfsOptions{SizeMiB: 256}),
    }),
)
```


Add volume mount configurations keyed by guest path. Build values via the [`Mount`](https://docs.microsandbox.dev/sdk/go/volumes) factory. Called repeatedly, the maps merge; later entries overwrite earlier ones for the same guest path. See [Volumes](https://docs.microsandbox.dev/sdk/go/volumes).


Parameters


`mounts` map[string]MountConfig Guest path to mount config.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withstoptimeout) WithStopTimeout()


```
func WithStopTimeout(timeout time.Duration) StopOption
```


Set a deadline for [`Stop`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stop), which otherwise waits without a built-in timeout. Expiry returns `ErrStopTimeout` without force-killing. Zero or a negative duration expires before sending a shutdown request. This is a `StopOption`, not a `SandboxOption`; pass it to [`Stop`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stop), or use [`StopWithTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stopwithtimeout).


Parameters


`timeout` time.Duration Stopped-state observation deadline.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withconnectorstartdetached) WithConnectOrStartDetached()


```
func WithConnectOrStartDetached() ConnectOrStartOption
```


When `ConnectOrStart` must start a local sandbox, start it in detached/background mode. This option does not change ownership when the sandbox is already running.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withrestartforce) WithRestartForce()


```
func WithRestartForce() RestartOption
```


Force-kill instead of requesting graceful shutdown during `Restart`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withrestarttimeout) WithRestartTimeout()


```
func WithRestartTimeout(timeout time.Duration) RestartOption
```


Set how long `Restart` waits for graceful shutdown before it times out. The default is ten seconds.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withrestartdetached) WithRestartDetached()


```
func WithRestartDetached() RestartOption
```


Start the restarted local sandbox in detached/background mode.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withdestroyforce) WithDestroyForce()


```
func WithDestroyForce() DestroyOption
```


Force-kill instead of requesting graceful shutdown during `Destroy`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withdestroytimeout) WithDestroyTimeout()


```
func WithDestroyTimeout(timeout time.Duration) DestroyOption
```


Set how long `Destroy` waits for graceful shutdown before it times out. The default is ten seconds.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withkilltimeout) WithKillTimeout()


```
func WithKillTimeout(timeout time.Duration) KillOption
```


Set how long [`Kill`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-kill) waits for stopped-state observation. The default is five seconds. This is a `KillOption`; pass it to [`Kill`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-kill).


Parameters


`timeout` time.Duration Observation window.
Use `ResolveRuntime(RuntimeConfig{})` to require a pre-provisioned runtime without downloading. See [Runtime setup](https://docs.microsandbox.dev/sdk/setup#customize-installation).


Attach options


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withattachcwd) WithAttachCwd()


```
func WithAttachCwd(path string) AttachOption
```


Set the working directory for the attached session. Defaults to the sandbox’s workdir.


Parameters


`path` string Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withattachuser) WithAttachUser()


```
func WithAttachUser(user string) AttachOption
```


Run the attached session as the given guest user instead of the sandbox’s default user (set via [`WithUser`](https://docs.microsandbox.dev/sdk/go/sandbox#withuser)).


Parameters


`user` string Guest user as a UID or name, optionally `user:group`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withattachenv) WithAttachEnv()


```
func WithAttachEnv(env map[string]string) AttachOption
```


Add environment variables for the attached session, merged on top of the sandbox’s env. Called repeatedly, maps merge; later keys overwrite earlier ones.


Parameters


`env` map[string]string Environment variables to set.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#withattachdetachkeys) WithAttachDetachKeys()


```
func WithAttachDetachKeys(keys string) AttachOption
```


Set the key sequence that detaches from the session without stopping it. Uses Docker-style syntax: `ctrl-]` (the default), `ctrl-p,ctrl-q`, or a single character like `q`.


Parameters


`keys` string Detach key sequence.


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch) Patch


Produces [PatchConfig](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig) for [WithPatches()](https://docs.microsandbox.dev/sdk/go/sandbox#withpatches)


Factory for [`PatchConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig) values.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-text) Patch. Text()


```
func (patchFactory) Text(path, content string, opts PatchOptions) PatchConfig
```


Write UTF-8 text content at `path`.


Parameters


`path` string Absolute path inside the guest. `content` string Text content. `opts` [PatchOptions](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) `Mode` and `Replace`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-append) Patch. Append()


```
func (patchFactory) Append(path, content string) PatchConfig
```


Append `content` to an existing file at `path`. If the file lives in a lower image layer, it is copied up first.


Parameters


`path` string Absolute path inside the guest. `content` string Text to append.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-mkdir) Patch. Mkdir()


```
func (patchFactory) Mkdir(path string, opts PatchOptions) PatchConfig
```


Create a directory. Idempotent. Only `opts.Mode` is honored; `Replace` is ignored.


Parameters


`path` string Absolute path inside the guest. `opts` [PatchOptions](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) Only `Mode` applies.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-remove) Patch. Remove()


```
func (patchFactory) Remove(path string) PatchConfig
```


Delete a file or directory at `path`. Idempotent.


Parameters


`path` string Absolute path inside the guest.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-symlink) Patch. Symlink()


```
func (patchFactory) Symlink(target, link string, opts PatchOptions) PatchConfig
```


Create a symlink at `link` pointing to `target`. Only `opts.Replace` is honored.


Parameters


`target` string What the symlink points to. `link` string Absolute path of the symlink itself. `opts` [PatchOptions](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) Only `Replace` applies.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-copyfile) Patch. CopyFile()


Limited on cloud


```
func (patchFactory) CopyFile(src, dst string, opts PatchOptions) PatchConfig
```


Copy a single host file at `src` into the guest rootfs at `dst`.


Parameters


`src` string Host source file. `dst` string Absolute destination path inside the guest. `opts` [PatchOptions](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) `Mode` and `Replace`.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patch-copydir) Patch. CopyDir()


Limited on cloud


```
func (patchFactory) CopyDir(src, dst string, opts PatchOptions) PatchConfig
```


Recursively copy a host directory at `src` into the guest rootfs at `dst`. Only `opts.Replace` is honored.


Parameters


`src` string Host source directory. `dst` string Absolute destination path inside the guest. `opts` [PatchOptions](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) Only `Replace` applies.


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#init) Init


Produces [InitConfig](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) for [WithInit()](https://docs.microsandbox.dev/sdk/go/sandbox#withinit)


Factory for [`InitConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) values.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#init-auto) Init. Auto()


```
func (initFactory) Auto() InitConfig
```


Example


```
m.WithInit(m.Init.Auto())
```


Use a known init at the start of the image ENTRYPOINT when present, preserving attached init-entrypoint commands. Otherwise, delegate to agentd to probe common init paths (`/sbin/init`, `/lib/systemd/systemd`, …) inside the guest.


Returns


[InitConfig](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) Auto-detect init config.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#init-cmd) Init. Cmd()


```
func (initFactory) Cmd(cmd string, opts InitOptions) InitConfig
```


Example


```
m.WithInit(m.Init.Cmd(
    "/lib/systemd/systemd",
    m.InitOptions{
        Args: []string{"--unit=multi-user.target"},
        Env:  map[string]string{"container": "microsandbox"},
    },
))
```


Specify the init binary explicitly with optional argv and env. `cmd` must be an absolute path inside the guest rootfs.


Parameters


`cmd` string Absolute path to the init binary inside the guest. `opts` [InitOptions](https://docs.microsandbox.dev/sdk/go/sandbox#initoptions) Argv and env.


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle) SandboxHandle


Returned by [GetSandbox()](https://docs.microsandbox.dev/sdk/go/sandbox#m-getsandbox) · [ListSandboxes()](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxes) · [ListSandboxesWith()](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxeswith)


A sandbox metadata and lifecycle handle that does not require an active guest-agent connection.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-name) h. Name()


```
Name()
```


Sandbox name, up to 128 UTF-8 bytes


Returns


`string`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-id) h. ID()


```
func (h *SandboxHandle) ID() string
```


Return the opaque stable identity captured by this metadata handle. Receiver lifecycle calls remain bound to this value and return `ErrSandboxReplaced` when the reusable name now points to another sandbox.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-status) h. Status()


```
Status()
```


Last-known lifecycle status


Returns


[`SandboxStatus`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstatus)


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-configjson) h. ConfigJSON()


```
ConfigJSON()
```


Raw JSON configuration


Returns


`string`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-config) h. Config()


Local-only


```
Config()
```


Parsed configuration


Returns


`(*` [`SandboxConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxconfig) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-createdat) h. CreatedAt()


```
CreatedAt()
```


Creation time, zero value if unknown


Returns


`time.Time`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-updatedat) h. UpdatedAt()


```
UpdatedAt()
```


Last-update time, zero value if unknown


Returns


`time.Time`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-refresh) h. Refresh()


```
Refresh(ctx)
```


Fresh handle for the same name


Returns


`(*SandboxHandle, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-ping) h. Ping()


Local-only


```
Ping(ctx)
```


Check agent reachability without refreshing idle activity; does not start stopped sandboxes


Returns


`(*` [`SandboxPingResult`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxpingresult) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-touch) h. Touch()


Local-only


```
Touch(ctx)
```


Explicitly refresh idle activity; does not start stopped sandboxes


Returns


`(*` [`SandboxTouchResult`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxtouchresult) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-modify) h. Modify()


Local-only


```
Modify(ctx, opts)
```


Plan or apply a configuration change; same [`ModifyOptions`](https://docs.microsandbox.dev/sdk/go/sandbox#modifyoptions) as [`Modify()`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-modify). Does not start stopped sandboxes; changes persist for the next boot


Returns


`(*` [`SandboxModificationPlan`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxmodificationplan) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-metrics) h. Metrics()


Local-only


```
Metrics(ctx)
```


Point-in-time resource metrics


Returns


`(*` [`Metrics`](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-logs) h. Logs()


Local-only


```
Logs(ctx, opts)
```


Read captured `exec.log` (works without starting)


Returns


`([]` [`LogEntry`](https://docs.microsandbox.dev/sdk/go/sandbox#logentry) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-logstream) h. LogStream()


```
LogStream(ctx, opts)
```


Stream captured output


Returns


`(*` [`LogStreamHandle`](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamhandle) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-connect) h. Connect()


```
Connect(ctx)
```


Reattach to the running sandbox


Returns


`(*` [`Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-connectorstart) h. ConnectOrStart()


```
func (h *SandboxHandle) ConnectOrStart(ctx context.Context, opts ...ConnectOrStartOption) (*Sandbox, error)
```


Connect when this exact sandbox is running, wait through `SandboxStatusStarting`, or start it when it is created, stopped, or crashed. Draining and paused states are rejected. `WithConnectOrStartDetached` affects only a required local start; connecting to an already-running sandbox does not change ownership.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-start) h. Start()


```
Start(ctx)
```


Boot a stopped sandbox. The returned local handle is attached; a cloud handle does not own the service-managed VM.


Returns


`(*` [`Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-startdetached) h. StartDetached()


```
StartDetached(ctx)
```


Boot a stopped sandbox in detached mode


Returns


`(*` [`Sandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#sandbox) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-waitforstatus) h. WaitForStatus()


```
func (h *SandboxHandle) WaitForStatus(ctx context.Context, status SandboxStatus) (*SandboxHandle, error)
```


Wait until this exact sandbox reaches `status`, returning a refreshed handle. The context supplies cancellation or a deadline. Returns `ErrSandboxReplaced` rather than rebinding to a replacement.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-restart) h. Restart()


```
func (h *SandboxHandle) Restart(ctx context.Context, opts ...RestartOption) (*Sandbox, error)
```


Restart this exact sandbox with the same state and option semantics as [`Sandbox.Restart`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-restart).


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-destroy) h. Destroy()


```
func (h *SandboxHandle) Destroy(ctx context.Context, opts ...DestroyOption) error
```


Stop and remove this exact sandbox. A stale handle returns `ErrSandboxReplaced` instead of destroying a same-name replacement.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-stop) h. Stop()


Different on cloud


```
Stop(ctx, opts...)
```


Request graceful shutdown and wait for this exact sandbox run and local runtime ownership release, without a built-in deadline or force-kill. Accepts [`StopOption`](https://docs.microsandbox.dev/sdk/go/sandbox#withstoptimeout); context cancellation ends only the wait.


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-stopwithtimeout) h. StopWithTimeout()


```
StopWithTimeout(ctx, timeout)
```


Bound graceful shutdown for this exact sandbox run. Expiry returns `ErrStopTimeout` without force-killing; zero or a negative duration expires before sending a request.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-requeststop) h. RequestStop()


```
RequestStop(ctx)
```


Send a graceful shutdown request without waiting for completion or scheduling forced termination.


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-kill) h. Kill()


Local-only


```
Kill(ctx, opts...)
```


Force terminate; accepts [`KillOption`](https://docs.microsandbox.dev/sdk/go/sandbox#withkilltimeout)


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-requestkill) h. RequestKill()


Local-only


```
RequestKill(ctx)
```


Async kill request


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-requestdrain) h. RequestDrain()


Local-only


```
RequestDrain(ctx)
```


Async drain request


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-waituntilstopped) h. WaitUntilStopped()


```
WaitUntilStopped(ctx)
```


Block until terminal state


Returns


`(*` [`SandboxStopResult`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstopresult) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-remove) h. Remove()


```
Remove(ctx)
```


Delete sandbox and persisted state


Returns


`error`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#h-snapshot) h. Snapshot()


Limited on cloud


```
Snapshot(ctx, name)
```


Capture a disk snapshot. Locally, the name selects a member within the sandbox’s snapshot group. See [Snapshots](https://docs.microsandbox.dev/sdk/go/snapshots).


Returns


`(*SnapshotArtifact, error)`


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#metricsstreamhandle) MetricsStreamHandle


Returned by [MetricsStream()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-metricsstream)


Live metrics subscription. Call `Close` to release Rust-side resources.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#metricsstream-recv) metricsStream. Recv()


```
Recv(ctx)
```


Block until the next snapshot arrives. Returns `(nil, nil)` when the stream ends (sandbox exited)


Returns


`(*` [`Metrics`](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#metricsstream-close) metricsStream. Close()


```
Close()
```


Stop the stream and release Rust-side resources


Returns


`error`


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#logentry) LogEntry


Returned by [Logs()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logs) · [LogStream()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logstream)


A single captured log entry.


| Field | Type | Description |
| --- | --- | --- |
| `Source` | [`LogSource`](https://docs.microsandbox.dev/sdk/go/sandbox#logsource) | Origin of the captured data |
| `SessionID` | `*uint64` | Relay-monotonic session id; nil for system entries |
| `Timestamp` | `time.Time` | Wall-clock capture time on the host |
| `Data` | `[]byte` | The captured bytes |
| `Cursor` | `string` | Opaque resume token; pass to [`LogStreamOptions.FromCursor`](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamoptions) |


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#entry-text) entry. Text()


```
Text()
```


Captured bytes as a string


Returns


`string`


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamhandle) LogStreamHandle


Returned by [LogStream()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logstream)


Live log subscription. Call `Close` to release Rust-side resources.


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#logstream-recv) logStream. Recv()


```
Recv(ctx)
```


Block until the next entry arrives. Returns `(nil, nil)` when the stream ends


Returns


`(*` [`LogEntry`](https://docs.microsandbox.dev/sdk/go/sandbox#logentry) `, error)`


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#logstream-close) logStream. Close()


```
Close()
```


Stop the stream and release Rust-side resources


Returns


`error`


## [​](https://docs.microsandbox.dev/sdk/go/sandbox#types) Types


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxpingresult) SandboxPingResult


Returned by [Ping()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-ping)


Agent reachability result.


| Field | Type | Description |
| --- | --- | --- |
| Name | `string` | Sandbox name |
| Latency | `time.Duration` | Round-trip latency |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxtouchresult) SandboxTouchResult


Returned by [Touch()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-touch)


Explicit idle-refresh result.


| Field | Type | Description |
| --- | --- | --- |
| Name | `string` | Sandbox name |
| ActivitySeq | `uint64` | Monotonic activity sequence after the touch |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#modifyoptions) ModifyOptions


Used by [Modify()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-modify)


A requested sandbox modification. Zero-valued fields are left unchanged (`0` is not a valid CPU, memory, or disk size).


| Field | Type | Description |
| --- | --- | --- |
| CPUs | `uint8` | Desired effective vCPU count. Live when within the booted `MaxCPUs` |
| MaxCPUs | `uint8` | Boot-time maximum possible vCPUs (restart-backed) |
| MemoryMiB | `uint32` | Desired effective guest memory in MiB. Live when within the booted `MaxMemoryMiB` |
| MaxMemoryMiB | `uint32` | Boot-time maximum hotpluggable memory in MiB (restart-backed) |
| RootDiskSizeMiB | `uint32` | Desired root disk size in MiB. Managed and flat OCI disks are grow-only; applies on restart or next start |
| Env | `map[string]string` | Environment variables to set for future execs |
| EnvRemove | `[]string` | Environment variable keys to remove |
| Labels | `map[string]string` | Labels to set |
| LabelsRemove | `[]string` | Label keys to remove |
| Workdir | `string` | Working directory for future execs |
| Secrets | `map[string]SecretModifySpec` | Desired secret specs keyed by stable secret name |
| SecretsRemove | `[]string` | Secret names to remove explicitly |
| Policy | `ModificationPolicy` | `ModificationPolicyNoRestart` (default) applies only changes that can complete without restarting; `ModificationPolicyNextStart` persists changes for the next start without mutating a running VM; `ModificationPolicyRestart` restarts if needed so restart-required changes become active now |
| DryRun | `bool` | Compute the plan without applying anything |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#secretmodifyspec) SecretModifySpec


Used by [Modify()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-modify)


Desired state for one secret. `Env`, `Value`, and `Store` are mutually exclusive sources. Leave all three empty to update only the placeholder or allowed hosts.


| Field | Type | Description |
| --- | --- | --- |
| Env | `string` | Host environment variable to resolve when applying the modification |
| Value | `string` | Raw secret value. Stored in the durable sandbox config until replaced by a source reference |
| Store | `string` | Reserved for a host-side secret store reference; currently unsupported |
| Placeholder | `string` | Explicit guest-visible placeholder. New secrets default to `$MSB_<NAME>` |
| AllowedHosts | `[]string` | Desired allowed host patterns. A new secret requires at least one; an empty slice leaves existing hosts unchanged |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxmodificationplan) SandboxModificationPlan


Returned by [Modify()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-modify)


Dry-run or apply plan for a sandbox modification. Values never appear in a plan: secret entries carry only guest-visible references.


| Field | Type | Description |
| --- | --- | --- |
| Sandbox | `string` | Sandbox being modified |
| Status | `string` | Status used for classification (`"running"`, `"stopped"`, …) |
| Applied | `bool` | Whether the changes were applied; `false` for dry runs |
| Policy | `ModificationPolicy` | Policy used to produce the plan |
| Changes | `[]PlannedChange` | Planned changes, one entry per field or secret (see below) |
| Conflicts | `[]ModificationConflict` | Conflicts (`Field` + `Message`) that must be resolved before the patch can apply |
| Warnings | `[]ModificationWarning` | Non-fatal warnings (`Field` + `Message`), e.g. the future-execs-only env caveat |
| ResizeStatus | `[]ResourceResizeStatus` | Live resource resize outcomes, populated by apply when a live change ran (see below) |


`PlannedChange` is one planned entry. `Kind` is `"config"` or `"secret"`; config entries carry `Before` / `After` while secret entries carry `Name`, `BeforeRef` / `AfterRef` (guest-visible references, values are omitted by construction), and `AllowHosts`:


| Field | Type | Description |
| --- | --- | --- |
| Kind | `string` | `"config"` or `"secret"` |
| Field | `string` | Config field being changed; always `"secret"` for secret entries |
| Name | `string` | Secret name (secret entries only) |
| Change | `string` | `"added"`, `"updated"`, or `"removed"` for config; `"added"`, `"rotated"`, `"removed"`, `"renamed"`, `"hosts updated"`, or `"placeholder updated"` for secrets |
| Before / After | `*string` | Previous / new visible state (config entries) |
| BeforeRef / AfterRef | `*string` | Previous / new guest-visible reference (secret entries) |
| Disposition | `string` | `"live"`, `"next start"`, `"requires restart"`, or `"unsupported"` |
| AllowHosts | `[]string` | Allowed hosts after the requested change (secret entries) |
| Reason | `*string` | Human-readable reason for the classification, when useful |


`ResourceResizeStatus` reports runtime convergence for a live resize; enforcement applies immediately, the guest converges asynchronously:


| Field | Type | Description |
| --- | --- | --- |
| Resource | `string` | `"cpus"` or `"memory"` |
| Requested | `string` | Requested value |
| Actual | `string` | Actual value observed in the guest/runtime |
| Enforced | `string` | Host/VMM-enforced value |
| State | `string` | `"applied"` when requested, actual, and enforced match; `"converging"` while the guest is still onlining CPUs or plugging memory; `"guest-refused"` when the guest would not cooperate (the host enforces the new limit anyway); `"accepted"` or `"failed"` otherwise |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxpage) SandboxPage


One stable, newest-first page returned by [`ListSandboxes`](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxes) or [`ListSandboxesWith`](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxeswith). Pass `NextCursor` back through `WithListCursor` with the same filters to continue.


| Field | Type | Description |
| --- | --- | --- |
| `Sandboxes` | `[]*SandboxHandle` | Handles in this page |
| `NextCursor` | `*string` | Opaque continuation cursor, or `nil` on the final page |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxlistoption) SandboxListOption


Functional options accepted by [`ListSandboxesWith`](https://docs.microsandbox.dev/sdk/go/sandbox#m-listsandboxeswith).


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxconfig) SandboxConfig


Populated by [SandboxOption](https://docs.microsandbox.dev/sdk/go/sandbox#options) · parsed by [SandboxHandle.Config()](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle)


The full configuration of a sandbox. Most callers build a sandbox via `CreateSandbox(ctx, name, ...opts)`; `SandboxConfig` is exported for callers that prefer to construct a value directly.


| Field | Type | Description |
| --- | --- | --- |
| Name | `string` | Sandbox name, up to 128 UTF-8 bytes |
| Image | `string` | OCI image, local path, or disk image |
| ImageFstype | `string` | Optional inner filesystem type for disk-image roots |
| RootDisk | [`*RootDiskConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskconfig) | Root storage for an OCI image |
| OCIUpperSizeMiB | `uint32` | Deprecated managed-root-disk size alias; ignored when `RootDisk` is set |
| MemoryMiB | `uint32` | Guest memory in MiB |
| CPUs | `uint8` | Virtual CPUs |
| MaxMemoryMiB | `uint32` | Boot-time maximum hotpluggable memory in MiB |
| MaxCPUs | `uint8` | Boot-time maximum possible virtual CPUs |
| Workdir | `string` | Default working directory |
| Shell | `string` | Shell binary used by `Shell` calls |
| SecurityProfile | [`SecurityProfile`](https://docs.microsandbox.dev/sdk/go/sandbox#securityprofile) | In-guest security profile |
| Hostname | `string` | Guest hostname |
| User | `string` | Default guest user |
| Replace | `bool` | Replace existing sandbox with same name |
| ReplaceWithTimeout | `*time.Duration` | Timeout between SIGTERM and SIGKILL (implies `Replace`) |
| Env | `map[string]string` | Environment variables |
| Labels | `map[string]string` | Labels for metrics attribution and filtering |
| Detached | `bool` | If `true`, sandbox survives after the process exits |
| Ephemeral | `bool` | If `true`, all state is removed on termination |
| Entrypoint | `[]string` | Override the image ENTRYPOINT used by default-workload execution |
| Cmd | `[]string` | Override the image CMD used by default-workload execution; an empty non-nil slice clears CMD |
| Init | [`*InitConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) | Hand PID 1 off to a guest init binary |
| LogLevel | [`LogLevel`](https://docs.microsandbox.dev/sdk/go/sandbox#loglevel) | Sandbox log verbosity override |
| QuietLogs | `bool` | Suppress sandbox-level log output |
| Scripts | `map[string]string` | Named scripts mounted at `/.msb/scripts/` |
| PullPolicy | [`PullPolicy`](https://docs.microsandbox.dev/sdk/go/sandbox#pullpolicy) | Image pull behavior |
| MaxDuration | `time.Duration` | Maximum sandbox lifetime |
| IdleTimeout | `time.Duration` | Idle timeout |
| RegistryAuth | [`*RegistryAuth`](https://docs.microsandbox.dev/sdk/go/sandbox#registryauth) | Private registry credentials |
| Ports | `map[uint16]uint16` | Host to guest TCP port mappings |
| PortsUDP | `map[uint16]uint16` | Host to guest UDP port mappings |
| PortBindings | [`[]PortBinding`](https://docs.microsandbox.dev/sdk/go/networking#portbinding) | Port mappings with explicit bind addresses |
| Network | [`*NetworkConfig`](https://docs.microsandbox.dev/sdk/go/networking#networkconfig) | Network policy and configuration |
| Secrets | [`[]SecretEntry`](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) | Secret injection entries |
| Patches | [`[]PatchConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig) | Rootfs modifications applied before boot |
| Volumes | `map[string]MountConfig` | Volume mounts keyed by guest path |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdisk) RootDisk


Factory namespace for [`RootDiskConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskconfig) values. Pass the result to [`WithRootDisk`](https://docs.microsandbox.dev/sdk/go/sandbox#withrootdisk).


```
m.RootDisk.Managed(8192)
m.RootDisk.Tmpfs(m.RootDiskTmpfsOptions{SizeMiB: 512})
m.RootDisk.Disk("./scratch.qcow2", m.RootDiskImageOptions{Format: "qcow2", Fstype: "ext4"})
m.RootDisk.Flat(m.RootDiskFlatOptions{SizeMiB: 8192, Clone: m.FlatCloneAuto})
```


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskconfig) RootDiskConfig


Root storage configuration returned by the [`RootDisk`](https://docs.microsandbox.dev/sdk/go/sandbox#rootdisk) factory. Use [`Kind()`](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskconfig-kind) to inspect its backing.


| Field | Type | Description |
| --- | --- | --- |
| `SizeMiB` | `uint32` | Managed, tmpfs, or flat root-disk size; zero selects the runtime default where supported |
| `Path` | `string` | Host path for a user-supplied disk image |
| `Format` | `string` | Disk-image format: `raw` or `qcow2`; inferred from the path when empty |
| `Fstype` | `string` | Inner filesystem type; defaults to `ext4` |
| `Clone` | [`FlatClone`](https://docs.microsandbox.dev/sdk/go/sandbox#flatclone) | Private flat-root provisioning strategy |


#### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskconfig-kind) rootDiskConfig. Kind()


```
func (r RootDiskConfig) Kind() RootDiskKind
```


Return the configured root-disk backing.


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskkind) RootDiskKind


| Constant | Description |
| --- | --- |
| `RootDiskKindManaged` | Microsandbox-owned sparse ext4 writable layer |
| `RootDiskKindTmpfs` | Ephemeral RAM-backed writable layer |
| `RootDiskKindDiskImage` | User-supplied writable disk image |
| `RootDiskKindFlat` | Complete OCI root filesystem mounted without guest OverlayFS |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdisktmpfsoptions) RootDiskTmpfsOptions


| Field | Type | Description |
| --- | --- | --- |
| `SizeMiB` | `uint32` | Tmpfs size; zero uses half of sandbox memory |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskimageoptions) RootDiskImageOptions


| Field | Type | Description |
| --- | --- | --- |
| `Format` | `string` | Optional `raw` or `qcow2` format; inferred from the path when empty |
| `Fstype` | `string` | Optional inner filesystem type; defaults to `ext4` |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#rootdiskflatoptions) RootDiskFlatOptions


| Field | Type | Description |
| --- | --- | --- |
| `SizeMiB` | `uint32` | Final guest capacity; zero uses the runtime default |
| `Fstype` | `string` | Generated filesystem type; currently `ext4` |
| `Clone` | [`FlatClone`](https://docs.microsandbox.dev/sdk/go/sandbox#flatclone) | Private disk provisioning strategy |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#flatclone) FlatClone


| Constant | Value | Description |
| --- | --- | --- |
| `FlatCloneAuto` | `"auto"` | Try a native reflink, then fall back to a sparse copy |
| `FlatCloneCopy` | `"copy"` | Always create a sparse copy |
| `FlatCloneReflink` | `"reflink"` | Require a native reflink and fail when unavailable |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxoption) SandboxOption


Consumed by [CreateSandbox()](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox)


```
type SandboxOption func(*SandboxConfig)
```


A functional option for [`CreateSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox). Every `WithX` helper in the [Options](https://docs.microsandbox.dev/sdk/go/sandbox#options) section returns one. The lifecycle setters [`WithStopTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#withstoptimeout) and [`WithKillTimeout`](https://docs.microsandbox.dev/sdk/go/sandbox#withkilltimeout) return distinct `StopOption` / `KillOption` types passed to [`Stop`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-stop) and [`Kill`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-kill) instead.


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#attachconfig) AttachConfig


Populated by [AttachOption](https://docs.microsandbox.dev/sdk/go/sandbox#attachoption)


Configures a single [`AttachWith`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attachwith) call. Most callers set fields through the `WithAttach*` functional options; `AttachConfig` is exported for parity with the other SDKs’ config types.


| Field | Type | Description |
| --- | --- | --- |
| `Cwd` | `string` | Working directory inside the guest; defaults to the sandbox workdir |
| `User` | `string` | Guest user (UID or name, optionally `user:group`); defaults to the sandbox user |
| `Env` | `map[string]string` | Environment variables merged on top of the sandbox env |
| `DetachKeys` | `string` | Detach key sequence; defaults to `ctrl-]` |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#attachoption) AttachOption


Accepted by [sb.AttachWith()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-attachwith)


```
type AttachOption func(*AttachConfig)
```


A functional option that mutates an [`AttachConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#attachconfig). Construct them with the `WithAttach*` functions below.


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#metrics) Metrics


Returned by [Metrics()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-metrics) · [MetricsStream()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-metricsstream) · [AllSandboxMetrics()](https://docs.microsandbox.dev/sdk/go/sandbox#m-allsandboxmetrics)


Point-in-time resource usage snapshot.


| Field | Type | Description |
| --- | --- | --- |
| CPUPercent | `float64` | CPU usage as a percentage |
| VCPUTimeNs | `uint64` | Cumulative vCPU time in nanoseconds |
| MemoryBytes | `uint64` | Current memory usage in bytes |
| MemoryAvailableBytes | `*uint64` | Guest-reported available memory when known |
| MemoryHostResidentBytes | `*uint64` | Host RSS backing the guest when known |
| MemoryLimitBytes | `uint64` | Memory limit in bytes |
| DiskReadBytes | `uint64` | Total bytes read from disk since boot |
| DiskWriteBytes | `uint64` | Total bytes written to disk since boot |
| NetRxBytes | `uint64` | Total bytes received over the network since boot |
| NetTxBytes | `uint64` | Total bytes sent over the network since boot |
| UpperUsedBytes | `*uint64` | Guest-visible OCI upper filesystem used bytes when the protected reporter is available and fresh |
| UpperFreeBytes | `*uint64` | Guest-visible OCI upper filesystem free bytes when the protected reporter is available and fresh |
| UpperHostAllocatedBytes | `*uint64` | Host-allocated bytes for the writable OCI upper image when available |
| Uptime | `time.Duration` | Time since the sandbox was created |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstopresult) SandboxStopResult


Returned by [WaitUntilStopped()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-waituntilstopped)


Describes a terminal sandbox state observed by [`WaitUntilStopped`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-waituntilstopped).


| Field | Type | Description |
| --- | --- | --- |
| Name | `string` | Sandbox name |
| Status | [`SandboxStatus`](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstatus) | Terminal status (`stopped` or `crashed`) |
| ExitCode | `*int` | Process exit code when known |
| Signal | `*int` | Terminating signal when known |
| ObservedAt | `time.Time` | When the terminal state was observed |
| Source | `*string` | Origin of the stop observation when known |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstatus) SandboxStatus


Used by [SandboxHandle.Status()](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxhandle) · [SandboxStopResult.Status](https://docs.microsandbox.dev/sdk/go/sandbox#sandboxstopresult)


```
type SandboxStatus string
```


| Constant | Value | Description |
| --- | --- | --- |
| `SandboxStatusCreated` | `"created"` | Persisted resource exists but has not started |
| `SandboxStatusStarting` | `"starting"` | Runtime is booting or waiting for capacity |
| `SandboxStatusRunning` | `"running"` | Guest agent is ready; `Exec`, `Shell`, `FS` work |
| `SandboxStatusDraining` | `"draining"` | Graceful shutdown in progress; existing commands finish, new ones rejected |
| `SandboxStatusPaused` | `"paused"` | VM is paused |
| `SandboxStatusStopped` | `"stopped"` | VM shut down; configuration persisted; can be restarted |
| `SandboxStatusCrashed` | `"crashed"` | VM exited unexpectedly (kernel panic, OOM, etc.) |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#logoptions) LogOptions


Used by [Logs()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logs)


Filters passed to [`Logs`](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logs). The zero value returns everything for the default sources (stdout + stderr).


| Field | Type | Description |
| --- | --- | --- |
| Tail | `uint64` | Keep only the last N matching entries |
| Since | `time.Time` | Inclusive lower timestamp bound |
| Until | `time.Time` | Exclusive upper timestamp bound |
| Sources | `[]` [`LogSource`](https://docs.microsandbox.dev/sdk/go/sandbox#logsource) | Sources to include; empty = stdout + stderr. Add `LogSourceOutput` or `LogSourceSystem` for PTY-merged output or runtime/kernel diagnostics |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamoptions) LogStreamOptions


Used by [LogStream()](https://docs.microsandbox.dev/sdk/go/sandbox#sb-logstream)


Configures a live log stream. The zero value reads the default sources from the beginning with follow off. `Since` and `FromCursor` are mutually exclusive.


| Field | Type | Description |
| --- | --- | --- |
| Sources | `[]` [`LogSource`](https://docs.microsandbox.dev/sdk/go/sandbox#logsource) | Sources to include; empty = stdout + stderr + output |
| Since | `time.Time` | Start at the first entry with timestamp >= this; mutually exclusive with `FromCursor` |
| FromCursor | `string` | Resume strictly after the entry whose `Cursor` matches; mutually exclusive with `Since` |
| Until | `time.Time` | Stop at the first entry with timestamp >= this |
| Follow | `bool` | Keep the stream open past EOF and yield new entries as written |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#logsource) LogSource


Used by [LogEntry.Source](https://docs.microsandbox.dev/sdk/go/sandbox#logentry) · [LogOptions.Sources](https://docs.microsandbox.dev/sdk/go/sandbox#logoptions) · [LogStreamOptions.Sources](https://docs.microsandbox.dev/sdk/go/sandbox#logstreamoptions)


```
type LogSource string
```


| Constant | Value | Description |
| --- | --- | --- |
| `LogSourceStdout` | `"stdout"` | Captured stdout (pipe mode, streams stayed separated) |
| `LogSourceStderr` | `"stderr"` | Captured stderr (pipe mode) |
| `LogSourceOutput` | `"output"` | PTY-merged stdout and stderr from a session running in PTY mode |
| `LogSourceSystem` | `"system"` | Synthetic lifecycle markers plus runtime/kernel diagnostic lines |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#loglevel) LogLevel


Used by [WithLogLevel()](https://docs.microsandbox.dev/sdk/go/sandbox#withloglevel)


```
type LogLevel string
```


Sandbox process log verbosity.


| Constant | Value | Description |
| --- | --- | --- |
| `LogLevelDefault` | `""` | Runtime default |
| `LogLevelTrace` | `"trace"` | Most verbose, all diagnostic output |
| `LogLevelDebug` | `"debug"` | Debug and higher |
| `LogLevelInfo` | `"info"` | Info and higher |
| `LogLevelWarn` | `"warn"` | Warnings and errors only |
| `LogLevelError` | `"error"` | Errors only |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#pullpolicy) PullPolicy


Used by [WithPullPolicy()](https://docs.microsandbox.dev/sdk/go/sandbox#withpullpolicy)


```
type PullPolicy string
```


Controls when the SDK fetches an OCI image from the registry.


| Constant | Value | Description |
| --- | --- | --- |
| `PullPolicyDefault` | `""` | Runtime default (currently `PullPolicyIfMissing`) |
| `PullPolicyAlways` | `"always"` | Pull every time, even if cached locally |
| `PullPolicyIfMissing` | `"if-missing"` | Pull only if not already cached |
| `PullPolicyNever` | `"never"` | Never pull; fail if missing |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#securityprofile) SecurityProfile


Used by [WithSecurityProfile()](https://docs.microsandbox.dev/sdk/go/sandbox#withsecurityprofile)


```
type SecurityProfile string
```


Sandbox-wide in-guest security profile.


| Constant | Value | Description |
| --- | --- | --- |
| `SecurityProfileDefault` | `"default"` | Normal guest-root semantics |
| `SecurityProfileRestricted` | `"restricted"` | Stronger hardening: `no_new_privs`, dropped mount-admin capability, forced `nosuid,nodev` on user mounts |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#registryauth) RegistryAuth


Used by [WithRegistryAuth()](https://docs.microsandbox.dev/sdk/go/sandbox#withregistryauth)


Credentials for a private OCI registry.


| Field | Type | Description |
| --- | --- | --- |
| Username | `string` | Registry username |
| Password | `string` | Registry password |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#initconfig) InitConfig


Built by [Init](https://docs.microsandbox.dev/sdk/go/sandbox#init) · used by [WithInit()](https://docs.microsandbox.dev/sdk/go/sandbox#withinit)


Custom guest PID-1 init specification. Construct via the [`Init`](https://docs.microsandbox.dev/sdk/go/sandbox#init) factory rather than building the struct directly.


| Field | Type | Description |
| --- | --- | --- |
| Cmd | `string` | Absolute path inside the guest, or `"auto"` |
| Args | `[]string` | Supplemental argv (`argv[0]` is implicitly `Cmd`) |
| Env | `map[string]string` | Extra env vars merged on top of the inherited env |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#initoptions) InitOptions


Used by [Init.Cmd()](https://docs.microsandbox.dev/sdk/go/sandbox#init-cmd)


Tuning struct for [`Init.Cmd`](https://docs.microsandbox.dev/sdk/go/sandbox#init-cmd) beyond the required cmd.


| Field | Type | Description |
| --- | --- | --- |
| Args | `[]string` | Supplemental argv |
| Env | `map[string]string` | Extra env vars |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig) PatchConfig


Built by [Patch](https://docs.microsandbox.dev/sdk/go/sandbox#patch) · used by [WithPatches()](https://docs.microsandbox.dev/sdk/go/sandbox#withpatches)


A single rootfs patch. Construct via the [`Patch`](https://docs.microsandbox.dev/sdk/go/sandbox#patch) factory; the fields populated depend on the [`PatchKind`](https://docs.microsandbox.dev/sdk/go/sandbox#patchkind).


| Field | Type | Description |
| --- | --- | --- |
| Kind | [`PatchKind`](https://docs.microsandbox.dev/sdk/go/sandbox#patchkind) | Patch flavor |
| Path | `string` | Absolute guest path (text / append / mkdir / remove) |
| Content | `string` | Text content (text / append) |
| Mode | `*uint32` | File or directory mode, e.g. `0o644` |
| Replace | `bool` | When `true`, overwrite an existing path at the destination |
| Src | `string` | Host source path (copy_file / copy_dir) |
| Dst | `string` | Guest destination path (copy_file / copy_dir) |
| Target | `string` | Symlink target |
| Link | `string` | Symlink path |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patchoptions) PatchOptions


Used by [Patch](https://docs.microsandbox.dev/sdk/go/sandbox#patch) methods


Tuning struct passed to [`Patch`](https://docs.microsandbox.dev/sdk/go/sandbox#patch) methods that accept a mode and replace flag.


| Field | Type | Description |
| --- | --- | --- |
| Mode | `*uint32` | File or directory mode |
| Replace | `bool` | Overwrite an existing path |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#patchkind) PatchKind


Used by [PatchConfig.Kind](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig)


```
type PatchKind string
```


Discriminator for [`PatchConfig`](https://docs.microsandbox.dev/sdk/go/sandbox#patchconfig). Prefer the [`Patch`](https://docs.microsandbox.dev/sdk/go/sandbox#patch) factory.


| Constant | Value |
| --- | --- |
| `PatchKindText` | `"text"` |
| `PatchKindAppend` | `"append"` |
| `PatchKindMkdir` | `"mkdir"` |
| `PatchKindRemove` | `"remove"` |
| `PatchKindSymlink` | `"symlink"` |
| `PatchKindCopyFile` | `"copy_file"` |
| `PatchKindCopyDir` | `"copy_dir"` |


### [​](https://docs.microsandbox.dev/sdk/go/sandbox#installoptions) InstallOptions


See [Runtime setup](https://docs.microsandbox.dev/sdk/setup#customize-installation) for the setup-only `InstallOptions` type.
## Documentation Index
## ​Functions
## ​Sandbox
## ​Options
## ​Patch
*Produces PatchConfig for WithPatches()*

## ​Init
*Produces InitConfig for WithInit()*

## ​SandboxHandle
*Returned by GetSandbox() · ListSandboxes() · ListSandboxesWith()*

## ​MetricsStreamHandle
*Returned by MetricsStream()*

## ​LogEntry
*Returned by Logs() · LogStream()*

## ​LogStreamHandle
*Returned by LogStream()*

## ​Types












Was this page helpful?

Yes No ⌘ I

---

# TypeScript SDK Agent client reference

`https://docs.microsandbox.dev/sdk/typescript/agent-client`

# Agent client
## Documentation Index
## ​Constants
## ​AgentClient
## ​AgentStream
*Returned by stream()*

## ​Types






Send requests to the sandbox guest agent with the TypeScript SDK.

Low-level raw CBOR transport for communicating with `agentd` through a sandbox relay.


## [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#constants) Constants


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#flag_terminal) FLAG_TERMINAL


```
const FLAG_TERMINAL = 0b0000_0001
```


Frame flag: this is the last message for the given correlation id. When a frame on an open stream carries this bit, no further frames will arrive for that id.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#flag_session_start) FLAG_SESSION_START


```
const FLAG_SESSION_START = 0b0000_0010
```


Frame flag: this is the first message of a new session. Set it on the opening frame of a request/response RPC or a streaming session.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#flag_shutdown) FLAG_SHUTDOWN


```
const FLAG_SHUTDOWN = 0b0000_0100
```


Frame flag: this message requests sandbox shutdown.


## [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient) AgentClient


Low-level client for raw agent frames.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-connectsandbox) AgentClient. connectSandbox()


Local-only


```
static connectSandbox(name: string, opts?: AgentConnectOptions): Promise<AgentClient>
```


Example


```
const client = await AgentClient.connectSandbox("dev", { timeoutMs: 5000 });
```


Connect to a running sandbox by name. Resolves the sandbox’s relay socket path and performs the `core.ready` handshake. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes. `opts` [AgentConnectOptions](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentconnectoptions) Optional connect settings, e.g. handshake timeout.


Returns


[Promise<AgentClient>](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-connect) AgentClient. connect()


Local-only


```
static connect(path: string, opts?: AgentConnectOptions): Promise<AgentClient>
```


Example


```
const path = AgentClient.socketPath("dev");
const client = await AgentClient.connect(path);
```


Connect to an `agentd` relay socket by path. Use this when you already have the socket path, for example one returned by [`socketPath()`](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-socketpath).


Parameters


`path` string Filesystem path of the relay socket. `opts` [AgentConnectOptions](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentconnectoptions) Optional connect settings, e.g. handshake timeout.


Returns


[Promise<AgentClient>](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-socketpath) AgentClient. socketPath()


Local-only


```
static socketPath(name: string): string
```


Example


```
const path = AgentClient.socketPath("dev");
```


Resolve a sandbox’s `agentd` relay socket path **without connecting**. Returns the same path [`connectSandbox()`](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-connectsandbox) would dial. Use it to talk to `agentd` over a raw byte transport instead of this frame client, for example a transparent relay that splices bytes to and from the socket. The sandbox need not be running. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


string Relay socket path.


Instance methods


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-request) client. request()


```
request(flags: number, body: Buffer): Promise<RawFrame>
```


Example


```
import { encode, decode } from "cbor-x";
import { FLAG_SESSION_START } from "microsandbox";

const body = encode({ v: 1, t: "core.fs.request", p: encode({ op: { Stat: { path: "/etc" } } }) });
const frame = await client.request(FLAG_SESSION_START, body);
console.log(decode(frame.body));
```


Send one frame and await a single response frame. Use for request/response RPCs that produce exactly one terminal response (for example `FsRequest` to `FsResponse`).


Parameters


`flags` number Frame flag byte, e.g. `FLAG_SESSION_START`. `body` Buffer CBOR-encoded protocol message body.


Returns


[Promise<RawFrame>](https://docs.microsandbox.dev/sdk/typescript/agent-client#rawframe) The single response frame.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-stream) client. stream()


```
stream(flags: number, body: Buffer): Promise<AgentStream>
```


Example


```
import { FLAG_SESSION_START, FLAG_TERMINAL } from "microsandbox";

const stream = await client.stream(FLAG_SESSION_START, body);
for await (const frame of stream) {
  if ((frame.flags & FLAG_TERMINAL) !== 0) break;
}
```


Open a streaming session. The returned [`AgentStream`](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream) carries the protocol correlation `id` (pass it to [`send()`](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-send) for follow-up frames) and is also an async iterator of raw frames.


Parameters


`flags` number Frame flag byte for the opening frame, e.g. `FLAG_SESSION_START`. `body` Buffer CBOR-encoded protocol message body.


Returns


[Promise<AgentStream>](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream) Open stream of raw frames.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-send) client. send()


```
send(id: number, flags: number, body: Buffer): Promise<void>
```


Example


```
await client.send(stream.id, 0, encode({ v: 1, t: "core.pty.stdin", p: encode({ data: "ls\n" }) }));
```


Send a follow-up frame on an existing correlation id (for example stdin, a signal, a resize, or data chunks on an open session). Use the `id` of the [`AgentStream`](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream) returned by [`stream()`](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-stream).


Parameters


`id` number Correlation id of an open session. `flags` number Frame flag byte. `body` Buffer CBOR-encoded protocol message body.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-readybytes) client. readyBytes()


```
readyBytes(): Buffer
```


Example


```
import { decode } from "cbor-x";

const ready = decode(client.readyBytes());
```


Return the cached handshake `core.ready` frame body as CBOR bytes. Captured during connect, so this is a synchronous accessor with no protocol traffic.


Returns


Buffer CBOR-encoded `core.ready` frame body.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-close) client. close()


```
close(): Promise<void>
```


Example


```
await client.close();
```


Close the connection. Idempotent: calling it more than once is safe.


## [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream) AgentStream


Returned by [stream()](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-stream)


An open raw agent stream. Implements `AsyncIterableIterator<RawFrame>`, so it can be driven with `for await`. The iterator ends after a frame carrying [`FLAG_TERMINAL`](https://docs.microsandbox.dev/sdk/typescript/agent-client#flag_terminal) or when the underlying stream is exhausted.


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#stream-id) stream. id


`number`
Protocol correlation id; pass to [`send()`](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-send) for follow-up frames


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#stream-next) stream. next()


```
next()
```


Pull the next frame; `done` once terminal or exhausted


Returns


`Promise<IteratorResult<` [`RawFrame`](https://docs.microsandbox.dev/sdk/typescript/agent-client#rawframe) `>>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#stream-close) stream. close()


```
close()
```


Release the stream handle early (idempotent)


Returns


`Promise<void>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#stream-return) stream. return()


```
return()
```


Async-iterator early-exit hook; closes the stream


Returns


`Promise<IteratorResult<` [`RawFrame`](https://docs.microsandbox.dev/sdk/typescript/agent-client#rawframe) `>>`


#### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#stream-symbol-asynciterator) stream. [Symbol.asyncIterator](https://docs.microsandbox.dev/sdk/typescript/agent-client)


```
[Symbol.asyncIterator]()
```


Returns itself so the stream is iterable


Returns


[`AgentStream`](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream)


## [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#types) Types


### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#rawframe) RawFrame


Returned by [request()](https://docs.microsandbox.dev/sdk/typescript/agent-client#client-request) · iterated from [AgentStream](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentstream)


A raw protocol frame. The `body` is the CBOR-encoded `Message` body (`v`, `t`, `p`) as it appeared on the wire; decode it with a CBOR library such as `cbor-x`.


| Field | Type | Description |
| --- | --- | --- |
| id | `number` | Correlation id from the frame header |
| flags | `number` | Frame flags (`FLAG_TERMINAL`, `FLAG_SESSION_START`, …) |
| body | `Buffer` | Raw CBOR-encoded body bytes |


### [​](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentconnectoptions) AgentConnectOptions


Used by [connectSandbox()](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-connectsandbox) · [connect()](https://docs.microsandbox.dev/sdk/typescript/agent-client#agentclient-connect)


Options for connecting to an agent relay.


| Field | Type | Description |
| --- | --- | --- |
| timeoutMs | `number` | Handshake timeout in milliseconds. Defaults to `10_000`. |


Was this page helpful?

Yes No ⌘ I

---

# Python SDK Agent client reference

`https://docs.microsandbox.dev/sdk/python/agent-client`

# Agent client
## Documentation Index
## ​Constants
## ​AgentClient
## ​AgentStream
*Returned by stream()*

## ​Types






Send requests to the sandbox guest agent with the Python SDK.

Low-level raw CBOR transport for communicating with `agentd` through a sandbox relay.


## [​](https://docs.microsandbox.dev/sdk/python/agent-client#constants) Constants


| Name | Value | Description |
| --- | --- | --- |
| `FLAG_TERMINAL` | `0b0000_0001` | Last frame for a correlation id |
| `FLAG_SESSION_START` | `0b0000_0010` | First frame of a streaming session |
| `FLAG_SHUTDOWN` | `0b0000_0100` | Shutdown frame |


## [​](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient) AgentClient


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient-connect_sandbox) AgentClient. connect_sandbox()


Local-only


```
@classmethod
async def connect_sandbox(cls, name: str, *, timeout: float | None = None) -> AgentClient
```


Example


```
client = await AgentClient.connect_sandbox("dev", timeout=5.0)
```


Connect to a running sandbox by name. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes. `timeout` float | None Connection timeout in seconds. `None` uses the default.


Returns


AgentClient Connected client.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient-connect) AgentClient. connect()


Local-only


```
@classmethod
async def connect(cls, path: str, *, timeout: float | None = None) -> AgentClient
```


Example


```
path = AgentClient.socket_path("dev")
client = await AgentClient.connect(path)
```


Connect to an agent relay socket by path. Use this when you already know the socket path, for example one returned by [`socket_path()`](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient-socket_path).


Parameters


`path` str Path to the agentd relay socket. `timeout` float | None Connection timeout in seconds. `None` uses the default.


Returns


AgentClient Connected client.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient-socket_path) AgentClient. socket_path()


Local-only


```
@staticmethod
def socket_path(name: str) -> str
```


Example


```
path = AgentClient.socket_path("dev")
```


Resolve a sandbox’s `agentd` relay socket path **without connecting**. Returns the same path [`connect_sandbox()`](https://docs.microsandbox.dev/sdk/python/agent-client#agentclient-connect_sandbox) would dial. Use it to talk to `agentd` over a raw byte transport instead of this frame client, for example a transparent relay that splices bytes to and from the socket. The sandbox need not be running. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` str Sandbox name, up to 128 UTF-8 bytes.


Returns


str Filesystem path to the relay socket.


Instance methods


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#client-request) client. request()


```
async def request(self, flags: int, body: bytes) -> RawFrame
```


Example


```
frame = await client.request(0, body)
print(frame["id"], frame["flags"])
```


Send one raw frame and wait for one response frame.


Parameters


`flags` int Frame flag byte, e.g. a combination of `FLAG_*` constants. `body` bytes CBOR-encoded protocol message body.


Returns


[RawFrame](https://docs.microsandbox.dev/sdk/python/agent-client#rawframe) The response frame.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#client-stream) client. stream()


```
async def stream(self, flags: int, body: bytes) -> AgentStream
```


Example


```
from microsandbox import FLAG_SESSION_START, FLAG_TERMINAL

stream = await client.stream(FLAG_SESSION_START, body)
async for frame in stream:
    if frame["flags"] & FLAG_TERMINAL:
        break
```


Open a raw streaming session. The returned [`AgentStream`](https://docs.microsandbox.dev/sdk/python/agent-client#agentstream) carries the protocol correlation id and is also an async iterator of raw frames.


Parameters


`flags` int Frame flag byte; pass `FLAG_SESSION_START` to open a session. `body` bytes CBOR-encoded protocol message body.


Returns


[AgentStream](https://docs.microsandbox.dev/sdk/python/agent-client#agentstream) Open streaming session.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#client-send) client. send()


```
async def send(self, id: int, flags: int, body: bytes) -> None
```


Example


```
stream = await client.stream(FLAG_SESSION_START, body)
await client.send(stream.id, 0, follow_up_body)
```


Send a follow-up frame on an existing correlation id. Use the `id` from the [`AgentStream`](https://docs.microsandbox.dev/sdk/python/agent-client#agentstream) returned by [`stream()`](https://docs.microsandbox.dev/sdk/python/agent-client#client-stream).


Parameters


`id` int Correlation id of an open session, from `stream.id`. `flags` int Frame flag byte. `body` bytes CBOR-encoded protocol message body.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#client-ready_bytes) client. ready_bytes()


```
def ready_bytes(self) -> bytes
```


Example


```
ready = client.ready_bytes()
```


Return the cached handshake `core.ready` frame body as CBOR bytes.


Returns


bytes CBOR-encoded `core.ready` frame body.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#client-close) client. close()


```
async def close(self) -> None
```


Example


```
await client.close()
```


Close the client. Calling it more than once is safe.


## [​](https://docs.microsandbox.dev/sdk/python/agent-client#agentstream) AgentStream


Returned by [stream()](https://docs.microsandbox.dev/sdk/python/agent-client#client-stream)


An async iterator of raw agent frames.


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#stream-id) stream. id


`int`
Protocol correlation id; pass to [`send()`](https://docs.microsandbox.dev/sdk/python/agent-client#client-send) for follow-up frames


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#stream-next) stream. next()


```
next()
```


Read the next frame; returns `None` at EOF


Returns


`Awaitable[` [`RawFrame`](https://docs.microsandbox.dev/sdk/python/agent-client#rawframe) ` \| None]`


#### [​](https://docs.microsandbox.dev/sdk/python/agent-client#stream-close) stream. close()


```
close()
```


Release the stream handle early; safe to call more than once


Returns


`Awaitable[None]`


Example


```
from microsandbox import FLAG_SESSION_START, FLAG_TERMINAL

async with await client.stream(FLAG_SESSION_START, body) as stream:
    async for frame in stream:
        if frame["flags"] & FLAG_TERMINAL:
            break
```


## [​](https://docs.microsandbox.dev/sdk/python/agent-client#types) Types


### [​](https://docs.microsandbox.dev/sdk/python/agent-client#rawframe) RawFrame


Returned by [request()](https://docs.microsandbox.dev/sdk/python/agent-client#client-request) · yielded by [AgentStream](https://docs.microsandbox.dev/sdk/python/agent-client#agentstream)


A raw protocol frame with a CBOR-encoded body.


```
class RawFrame(TypedDict):
    id: int
    flags: int
    body: bytes
```


| Field | Type | Description |
| --- | --- | --- |
| id | `int` | Protocol correlation id |
| flags | `int` | Frame flag byte (combination of `FLAG_*` constants) |
| body | `bytes` | CBOR-encoded protocol message body |


Was this page helpful?

Yes No ⌘ I

---

# Rust SDK Agent client reference

`https://docs.microsandbox.dev/sdk/rust/agent-client`

# Agent client
## Documentation Index
## ​Module functions
## ​AgentClient
## ​AgentBridge
## ​Types






Send requests to the sandbox guest agent with the Rust SDK.

Low-level typed and raw transport for communicating with `agentd` through a sandbox relay.


## [​](https://docs.microsandbox.dev/sdk/rust/agent-client#module-functions) Module functions


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox) agent:: connect_sandbox()


Local-only


```
async fn connect_sandbox(name: &str) -> AgentClientResult<AgentClient>
```


Example


```
use microsandbox::agent;

let client = agent::connect_sandbox("dev").await?;
```


Resolve a sandbox name to its agent relay socket path and connect, using the default ten-second handshake timeout. The socket lives under the SDK’s configured runtime directory at a short, name-derived path. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox_with_timeout) agent:: connect_sandbox_with_timeout()


Local-only


```
async fn connect_sandbox_with_timeout(name: &str, timeout: Duration) -> AgentClientResult<AgentClient>
```


Example


```
use std::time::Duration;
use microsandbox::agent;

let client = agent::connect_sandbox_with_timeout("dev", Duration::from_secs(2)).await?;
```


Like [`connect_sandbox`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox), but with an explicit handshake timeout instead of the ten-second default.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes. `timeout` Duration Maximum time to wait for the relay handshake.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


## [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) AgentClient


Returned by [agent::connect_sandbox()](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox), [AgentClient::connect()](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect) · wrapped by [AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge)


Low-level client for raw agent frames.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect) AgentClient:: connect()


Local-only


```
async fn connect(sock_path: impl AsRef<Path>) -> AgentClientResult<AgentClient>
```


Example


```
use microsandbox::agent::AgentClient;

let path = AgentClient::socket_path("dev")?;
let client = AgentClient::connect(&path).await?;
```


Connect to an arbitrary agent relay socket by path, using the default ten-second handshake timeout. The connection performs the relay handshake, validates the cached `core.ready` frame, and starts one background reader task.


Parameters


`sock_path` impl AsRef<Path> Path to the agent relay socket.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect_with_timeout) AgentClient:: connect_with_timeout()


Local-only


```
async fn connect_with_timeout(sock_path: impl AsRef<Path>, timeout: Duration) -> AgentClientResult<AgentClient>
```


Connect to an arbitrary agent relay socket by path with an explicit handshake timeout.


Parameters


`sock_path` impl AsRef<Path> Path to the agent relay socket. `timeout` Duration Maximum time to wait for the relay handshake.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect_with_deadline) AgentClient:: connect_with_deadline()


Local-only


```
async fn connect_with_deadline(sock_path: impl AsRef<Path>, deadline: Instant) -> AgentClientResult<AgentClient>
```


Connect to an arbitrary agent relay socket by path with an explicit handshake deadline. The deadline bounds both handshake reads, so an accepted connection that stalls before writing the handshake bytes cannot block this call indefinitely.


Parameters


`sock_path` impl AsRef<Path> Path to the agent relay socket. `deadline` Instant Tokio instant by which the handshake must complete.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect_sandbox) AgentClient:: connect_sandbox()


Local-only


```
async fn connect_sandbox(name: &str) -> AgentClientResult<AgentClient>
```


Resolve a sandbox name to its agent socket path and connect. Equivalent to the module-level [`agent::connect_sandbox`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox).


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientconnect_sandbox_with_timeout) AgentClient:: connect_sandbox_with_timeout()


Local-only


```
async fn connect_sandbox_with_timeout(name: &str, timeout: Duration) -> AgentClientResult<AgentClient>
```


Resolve a sandbox name to its agent socket path and connect with an explicit handshake timeout. Equivalent to the module-level [`agent::connect_sandbox_with_timeout`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox_with_timeout).


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes. `timeout` Duration Maximum time to wait for the relay handshake.


Returns


[AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) Connected client.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientsocket_path) AgentClient:: socket_path()


Local-only


```
fn socket_path(name: &str) -> MicrosandboxResult<PathBuf>
```


Example


```
use microsandbox::agent::AgentClient;

let path = AgentClient::socket_path("dev")?;
println!("{}", path.display());
```


Resolve a sandbox’s relay socket path **without connecting**. Returns the same path [`connect_sandbox`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentconnect_sandbox) would dial: the hashed path under the runtime directory when it fits the platform’s Unix-socket length limit, and the legacy name-derived path otherwise. Useful for talking to `agentd` over a raw byte transport (for example a transparent relay that splices bytes to and from the socket) instead of this frame client. The sandbox need not be running.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


Returns


PathBuf Relay socket path.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientensure_version_compat_for) AgentClient:: ensure_version_compat_for()


```
fn ensure_version_compat_for(t: MessageType, negotiated: u8) -> AgentClientResult<()>
```


Example


```
use microsandbox::{agent::AgentClient, protocol::message::MessageType};

AgentClient::ensure_version_compat_for(MessageType::FsRequest, 2)?;
```


Check a message type against an explicit negotiated generation. The single place the rule lives, exposed for callers that hold the negotiated generation but not a live client. Returns [`AgentClientError::UnsupportedOperation`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror) if the type was introduced after the given generation.


Parameters


`t` MessageType Protocol message type to gate. `negotiated` u8 Protocol generation to check against.


Instance methods


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-request) client. request()


```
async fn request<T: Serialize>(&self, t: MessageType, payload: &T) -> AgentClientResult<Message>
```


Example


```
use microsandbox::protocol::{
    fs::{FsOp, FsRequest, FsResponse},
    message::MessageType,
};

let response = client
    .request(
        MessageType::FsRequest,
        &FsRequest {
            op: FsOp::Stat {
                path: "/etc/os-release".to_string(),
                follow_symlink: true,
            },
        },
    )
    .await?;
let fs_response: FsResponse = response.payload()?;
```


Send one typed protocol message and wait for one response frame with the same correlation id. Flags are derived from the message type. Use this for one-shot RPCs such as filesystem stat or list requests. Fails fast with [`AgentClientError::UnsupportedOperation`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror) if the connected sandbox is too old for the message type.


Parameters


`t` MessageType Protocol message type. `payload` &T: Serialize Message payload, serialized with CBOR.


Returns


Message Decoded response message.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream) client. stream()


```
async fn stream<T: Serialize>(&self, t: MessageType, payload: &T) -> AgentClientResult<(u32, Receiver<Message>)>
```


Example


```
use microsandbox::protocol::{exec::ExecRequest, message::MessageType};

let (id, mut rx) = client
    .stream(MessageType::ExecRequest, &ExecRequest {
        cmd: "echo".into(),
        args: vec!["hi".into()],
        env: Vec::new(),
        cwd: None,
        user: None,
        tty: false,
        rows: 24,
        cols: 80,
        rlimits: Vec::new(),
    })
    .await?;

while let Some(msg) = rx.recv().await {
    println!("{:?}", msg.t);
}
```


Open a typed streaming session. The returned id is the protocol correlation id. Use it with [`send()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-send) for follow-up messages such as stdin, resize, signal, or file data chunks. The receiver yields messages until a terminal frame is delivered or the connection closes.


Parameters


`t` MessageType Protocol message type for the opening frame. `payload` &T: Serialize Opening message payload, serialized with CBOR.


Returns


(u32, Receiver<Message>) Correlation id and a typed message receiver.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-send) client. send()


```
async fn send<T: Serialize>(&self, id: u32, t: MessageType, payload: &T) -> AgentClientResult<()>
```


Example


```
use microsandbox::protocol::{exec::ExecStdin, message::MessageType};

client.send(id, MessageType::ExecStdin, &ExecStdin { data: b"input\n".to_vec() }).await?;
```


Send a typed follow-up message on an existing correlation id (the id returned by [`stream()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream)).


Parameters


`id` u32 Correlation id from the open stream. `t` MessageType Protocol message type. `payload` &T: Serialize Message payload, serialized with CBOR.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-request_raw) client. request_raw()


```
async fn request_raw(&self, flags: u8, body: Vec<u8>) -> AgentClientResult<RawFrame>
```


Example


```
let frame = client.request_raw(flags, body).await?;
println!("id={} flags={}", frame.id, frame.flags);
```


Allocate a correlation id, send one raw frame with `(flags, body)`, and wait for one raw response frame with the matching id. CBOR encoding and decoding are left to the caller.


Parameters


`flags` u8 Frame flag byte. `body` Vec<u8> CBOR-encoded protocol message body.


Returns


[RawFrame](https://docs.microsandbox.dev/sdk/rust/agent-client#rawframe) Raw response frame.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream_raw) client. stream_raw()


```
async fn stream_raw(&self, flags: u8, body: Vec<u8>) -> AgentClientResult<(u32, Receiver<RawFrame>)>
```


Open a raw streaming session. The receiver yields raw frames for the returned correlation id until a frame with the terminal flag arrives or the receiver is dropped. Use [`send_raw()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-send_raw) with the returned id to send follow-up frames.


Parameters


`flags` u8 Frame flag byte for the opening frame. `body` Vec<u8> CBOR-encoded protocol message body.


Returns


(u32, Receiver<RawFrame>) Correlation id and a raw frame receiver.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-send_raw) client. send_raw()


```
async fn send_raw(&self, id: u32, flags: u8, body: &[u8]) -> AgentClientResult<()>
```


Send a raw follow-up frame on an existing correlation id (the id returned by [`stream_raw()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream_raw)).


Parameters


`id` u32 Correlation id from the open raw stream. `flags` u8 Frame flag byte. `body` &[u8] CBOR-encoded protocol message body.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-ready) client. ready()


```
fn ready(&self) -> AgentClientResult<Ready>
```


Example


```
let ready = client.ready()?;
println!("boot {} ns", ready.boot_time_ns);
```


Return the decoded `core.ready` payload captured during the handshake (boot timings and the runtime’s self-reported version).


Returns


Ready Decoded handshake payload.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-ready_bytes) client. ready_bytes()


```
fn ready_bytes(&self) -> &[u8]
```


Return the cached handshake `core.ready` frame body as CBOR bytes. Useful for bindings that want to deserialize the ready payload with their own CBOR tooling. For typed access, use [`ready()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-ready).


Returns


&[u8] CBOR-encoded ready frame body.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-protocol) client. protocol()


```
fn protocol(&self) -> AgentProtocol
```


The agent protocol generation (wire codec) negotiated for this connection.


Returns


[AgentProtocol](https://docs.microsandbox.dev/sdk/rust/agent-client#agentprotocol) Codec generation: `Current` or `LegacyV1`.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-is_legacy_protocol) client. is_legacy_protocol()


```
fn is_legacy_protocol(&self) -> bool
```


Whether this connection is using the legacy pre-0.5 protocol.


Returns


bool `true` if the relay speaks the pre-0.5 protocol.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-negotiated_version) client. negotiated_version()


```
fn negotiated_version(&self) -> u8
```


The negotiated protocol generation for this connection: the lower of what this client speaks and what the sandbox advertised at handshake. This is the capability gate that drives [`supports()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-supports) and the typed send path, and it is distinct from [`protocol()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-protocol), which selects the wire codec.


Returns


u8 Negotiated capability generation.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-agent_version) client. agent_version()


```
fn agent_version(&self) -> &str
```


The runtime’s self-reported package version, taken from its `core.ready` frame. Empty when the runtime predates this field (an older agent), in which case fall back to the generation for diagnostics.


Returns


&str Runtime package version, or empty if unknown.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-supports) client. supports()


```
fn supports(&self, t: MessageType) -> bool
```


Example


```
use microsandbox::protocol::message::MessageType;

if client.supports(MessageType::FsRequest) {
    // safe to issue filesystem RPCs
}
```


Whether the connected sandbox is new enough to handle the given message type. The single source of truth for feature gating: callers that cannot gate by sending (for example the SSH/SFTP layer) consult this instead of inspecting the protocol generation directly.


Parameters


`t` MessageType Protocol message type to check.


Returns


bool `true` if the runtime can handle the type.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-ensure_version_compat) client. ensure_version_compat()


```
fn ensure_version_compat(&self, t: MessageType) -> AgentClientResult<()>
```


Example


```
use microsandbox::protocol::message::MessageType;

client.ensure_version_compat(MessageType::TcpConnect)?;
```


Reject a message type the connected sandbox is too old to handle, against this connection’s negotiated generation. Fails before any bytes are sent, so only that one operation fails and the session continues. The typed [`request()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-request), [`stream()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream), and [`send()`](https://docs.microsandbox.dev/sdk/rust/agent-client#client-send) methods call this internally.


Parameters


`t` MessageType Protocol message type to gate.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#client-close) client. close()


```
async fn close(self)
```


Example


```
client.close().await;
```


Close the client by consuming it. Drops the writer and aborts the reader task; any in-flight requests resolve with [`AgentClientError::Closed`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror). Dropping the client has the same effect.


## [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) AgentBridge


FFI-friendly bytes-in/bytes-out wrapper around [`AgentClient`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient).


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridgeconnect_sandbox) AgentBridge:: connect_sandbox()


Local-only


```
async fn connect_sandbox(name: &str) -> AgentClientResult<AgentBridge>
```


Connect to a sandbox by name, resolving the socket path from SDK config. Sandbox names are limited to 128 UTF-8 bytes.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes.


Returns


[AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) Connected bridge.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridgeconnect_sandbox_with_timeout) AgentBridge:: connect_sandbox_with_timeout()


Local-only


```
async fn connect_sandbox_with_timeout(name: &str, timeout: Duration) -> AgentClientResult<AgentBridge>
```


Connect to a sandbox by name with an explicit handshake timeout.


Parameters


`name` &str Sandbox name, up to 128 UTF-8 bytes. `timeout` Duration Maximum time to wait for the relay handshake.


Returns


[AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) Connected bridge.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridgeconnect_path) AgentBridge:: connect_path()


Local-only


```
async fn connect_path(path: &str) -> AgentClientResult<AgentBridge>
```


Connect to an arbitrary agentd relay socket by path.


Parameters


`path` &str Path to the agent relay socket.


Returns


[AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) Connected bridge.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridgeconnect_path_with_timeout) AgentBridge:: connect_path_with_timeout()


Local-only


```
async fn connect_path_with_timeout(path: &str, timeout: Duration) -> AgentClientResult<AgentBridge>
```


Connect to an arbitrary agentd relay socket by path with an explicit handshake timeout.


Parameters


`path` &str Path to the agent relay socket. `timeout` Duration Maximum time to wait for the relay handshake.


Returns


[AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) Connected bridge.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-request) bridge. request()


```
async fn request(&self, flags: u8, body: Vec<u8>) -> AgentClientResult<BridgeFrame>
```


One-shot request: send `(flags, body)` and wait for one response frame.


Parameters


`flags` u8 Frame flag byte. `body` Vec<u8> CBOR-encoded protocol message body.


Returns


[BridgeFrame](https://docs.microsandbox.dev/sdk/rust/agent-client#bridgeframe) Response frame.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-send) bridge. send()


```
async fn send(&self, id: u32, flags: u8, body: Vec<u8>) -> AgentClientResult<()>
```


Send a follow-up frame on an existing correlation id.


Parameters


`id` u32 Correlation id from an open stream. `flags` u8 Frame flag byte. `body` Vec<u8> CBOR-encoded protocol message body.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_open) bridge. stream_open()


```
async fn stream_open(&self, flags: u8, body: Vec<u8>) -> AgentClientResult<(u32, StreamHandle)>
```


Open a streaming session. Returns the protocol correlation id (for follow-up sends via [`send()`](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-send)) and an opaque stream handle (for [`stream_next()`](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_next) and [`stream_close()`](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_close)).


Parameters


`flags` u8 Frame flag byte for the opening frame. `body` Vec<u8> CBOR-encoded protocol message body.


Returns


(u32, [StreamHandle](https://docs.microsandbox.dev/sdk/rust/agent-client#streamhandle)) Correlation id and an opaque stream handle.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_next) bridge. stream_next()


```
async fn stream_next(&self, handle: StreamHandle) -> AgentClientResult<Option<BridgeFrame>>
```


Example


```
let (id, handle) = bridge.stream_open(flags, body).await?;
while let Some(frame) = bridge.stream_next(handle).await? {
    // decode frame.body with your own CBOR tooling
}
```


Pull the next frame from a stream. Returns `None` when the stream has ended (the terminal frame was already delivered, or the stream was closed or dropped).


Parameters


`handle` [StreamHandle](https://docs.microsandbox.dev/sdk/rust/agent-client#streamhandle) Handle returned by [`stream_open()`](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_open).


Returns


Option< [BridgeFrame](https://docs.microsandbox.dev/sdk/rust/agent-client#bridgeframe) > Next frame, or `None` at end of stream.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_close) bridge. stream_close()


```
async fn stream_close(&self, handle: StreamHandle)
```


Close a stream and drop its handle. Idempotent.


Parameters


`handle` [StreamHandle](https://docs.microsandbox.dev/sdk/rust/agent-client#streamhandle) Handle returned by [`stream_open()`](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_open).


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-ready_bytes) bridge. ready_bytes()


```
fn ready_bytes(&self) -> AgentClientResult<Vec<u8>>
```


The cached handshake `core.ready` frame body bytes (CBOR). Errors with [`AgentClientError::Closed`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror) if the bridge has been closed.


Returns


Vec<u8> CBOR-encoded ready frame body.


#### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-close) bridge. close()


```
async fn close(&self)
```


Example


```
bridge.close().await;
```


Close the connection. Idempotent. After close, every operation except another close returns [`AgentClientError::Closed`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror).


## [​](https://docs.microsandbox.dev/sdk/rust/agent-client#types) Types


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#bridgeframe) BridgeFrame


Returned by [bridge.request()](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-request), [bridge.stream_next()](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_next)


FFI-friendly view of a [`RawFrame`](https://docs.microsandbox.dev/sdk/rust/agent-client#rawframe): id, flags, body bytes.


| Field | Type | Description |
| --- | --- | --- |
| `id` | `u32` | Correlation ID from the frame header. |
| `flags` | `u8` | Frame flags from the frame header. |
| `body` | `Vec<u8>` | Raw CBOR-encoded body bytes. |


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#streamhandle) StreamHandle


Returned by [bridge.stream_open()](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_open) · used by [bridge.stream_next()](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_next), [bridge.stream_close()](https://docs.microsandbox.dev/sdk/rust/agent-client#bridge-stream_close)


```
pub type StreamHandle = u64;
```


Opaque handle identifying an open stream on an [`AgentBridge`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge). Foreign-language wrappers reference streams by this `u64` instead of owning a tokio receiver.


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentprotocol) AgentProtocol


Returned by [client.protocol()](https://docs.microsandbox.dev/sdk/rust/agent-client#client-protocol)


Agent protocol generation (wire codec) spoken by a connected sandbox relay.


| Variant | Description |
| --- | --- |
| `Current` | Current protocol generation. |
| `LegacyV1` | Pre-0.5 microsandbox relay handshake and agent protocol. |


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#rawframe) RawFrame


Returned by [client.request_raw()](https://docs.microsandbox.dev/sdk/rust/agent-client#client-request_raw), [client.stream_raw()](https://docs.microsandbox.dev/sdk/rust/agent-client#client-stream_raw)


A framed protocol message at the byte level. `id` is the protocol correlation id, `flags` is the frame flag byte, and `body` is the CBOR-encoded protocol message body. Re-exported from `microsandbox::protocol::codec`.


| Field | Type | Description |
| --- | --- | --- |
| `id` | `u32` | Protocol correlation id. |
| `flags` | `u8` | Frame flag byte. |
| `body` | `Vec<u8>` | CBOR-encoded protocol message body. |


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror) AgentClientError


Error variant of [AgentClientResult](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientresult)


Errors raised by [`AgentClient`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) and [`AgentBridge`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge).


| Variant | Description |
| --- | --- |
| `Connect { path, source }` | Failed to open the Unix socket connection to the relay. |
| `Handshake(String)` | Handshake with the relay failed (timeout, EOF, or malformed frame). |
| `SandboxNotFound(String)` | Sandbox name could not be resolved to an agent socket path. |
| `InvalidSandboxName(String)` | Sandbox name failed SDK validation before socket resolution. |
| `Io(std::io::Error)` | An I/O error occurred on the socket after connect. |
| `Protocol(ProtocolError)` | A wire-protocol error (framing, CBOR, oversize frame). |
| `Cbor(String)` | CBOR encoding or decoding failed. |
| `InvalidPacket(String)` | The supplied packet did not contain exactly one complete transport frame. |
| `UnsupportedOperation { msg_type, needs, peer }` | The connected sandbox’s runtime is older than the requested feature needs; restart the sandbox to update its runtime. |
| `ReaderClosed(u32)` | The reader task closed before the in-flight request received its response. |
| `Closed` | The client has been closed. |
| `IdRangeExhausted` | The relay-assigned correlation ID range has no available IDs. |
| `NotImplemented(&'static str)` | The operation is not implemented yet. |


### [​](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclientresult) AgentClientResult


Returned by most [AgentClient](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclient) and [AgentBridge](https://docs.microsandbox.dev/sdk/rust/agent-client#agentbridge) methods


```
pub type AgentClientResult<T> = Result<T, AgentClientError>;
```


Result alias for agent client operations. The error is [`AgentClientError`](https://docs.microsandbox.dev/sdk/rust/agent-client#agentclienterror).

Was this page helpful?

Yes No ⌘ I

---

# Go SDK Agent client reference

`https://docs.microsandbox.dev/sdk/go/agent-client`

# Agent client
## Documentation Index
## ​Constants
## ​Functions
## ​AgentClient
*Returned by ConnectAgentSandbox() · ConnectAgentPath()*

## ​AgentStream
*Returned by Stream()*

## ​Types







Send requests to the sandbox guest agent with the Go SDK.

Low-level raw CBOR transport for communicating with `agentd` through a sandbox relay.


## [​](https://docs.microsandbox.dev/sdk/go/agent-client#constants) Constants


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#flagterminal) FlagTerminal


```
const FlagTerminal uint8 = 0b0000_0001
```


Frame flag: this is the last message for the given correlation id. When a frame on an open stream carries this bit, no further frames will arrive for that id. Also available as `FLAG_TERMINAL`, the cross-SDK constant spelling.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#flagsessionstart) FlagSessionStart


```
const FlagSessionStart uint8 = 0b0000_0010
```


Frame flag: this is the first message of a new session. Set it on the opening frame of a request/response RPC or a streaming session. Also available as `FLAG_SESSION_START`.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#flagshutdown) FlagShutdown


```
const FlagShutdown uint8 = 0b0000_0100
```


Frame flag: this message requests sandbox shutdown. Also available as `FLAG_SHUTDOWN`.


## [​](https://docs.microsandbox.dev/sdk/go/agent-client#functions) Functions


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#m-connectagentsandbox) m. ConnectAgentSandbox()


Local-only


```
func ConnectAgentSandbox(ctx context.Context, name string) (*AgentClient, error)
```


Example


```
client, err := m.ConnectAgentSandbox(ctx, "dev")
if err != nil {
    return err
}
defer client.Close()
```


Connect to a running sandbox by name. Resolves the sandbox’s relay socket path and performs the `core.ready` handshake. Sandbox names are limited to 128 UTF-8 bytes. Use `context.WithTimeout` to override the default 10s handshake timeout.


Parameters


`ctx` context.Context Bounds the handshake; defaults to a 10s timeout if none is set. `name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


[*AgentClient](https://docs.microsandbox.dev/sdk/go/agent-client#agentclient) Connected client. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#m-connectagentpath) m. ConnectAgentPath()


Local-only


```
func ConnectAgentPath(ctx context.Context, path string) (*AgentClient, error)
```


Example


```
path, err := m.AgentSocketPath("dev")
if err != nil {
    return err
}

client, err := m.ConnectAgentPath(ctx, path)
if err != nil {
    return err
}
defer client.Close()
```


Connect to an `agentd` relay socket by path. Use this when you already have the socket path, for example one returned by [`AgentSocketPath()`](https://docs.microsandbox.dev/sdk/go/agent-client#m-agentsocketpath). Use `context.WithTimeout` to override the default 10s handshake timeout.


Parameters


`ctx` context.Context Bounds the handshake; defaults to a 10s timeout if none is set. `path` string Filesystem path of the relay socket.


Returns


[*AgentClient](https://docs.microsandbox.dev/sdk/go/agent-client#agentclient) Connected client. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#m-agentsocketpath) m. AgentSocketPath()


Local-only


```
func AgentSocketPath(name string) (string, error)
```


Example


```
path, err := m.AgentSocketPath("dev")
if err != nil {
    return err
}
fmt.Println(path)
```


Resolve a sandbox’s `agentd` relay socket path **without connecting**. Returns the same path [`ConnectAgentSandbox()`](https://docs.microsandbox.dev/sdk/go/agent-client#m-connectagentsandbox) would dial internally. It prefers the hashed path and falls back to the legacy name-derived path. Use it to talk to `agentd` over a raw byte transport instead of this frame client, for example a transparent relay that splices bytes between a WebSocket and the socket. The sandbox need not be running; the path is derived from the name and the configured home directory.


Parameters


`name` string Sandbox name, up to 128 UTF-8 bytes.


Returns


string Relay socket path. error Typed microsandbox error.


## [​](https://docs.microsandbox.dev/sdk/go/agent-client#agentclient) AgentClient


Returned by [ConnectAgentSandbox()](https://docs.microsandbox.dev/sdk/go/agent-client#m-connectagentsandbox) · [ConnectAgentPath()](https://docs.microsandbox.dev/sdk/go/agent-client#m-connectagentpath)


Low-level client for raw agent frames.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-request) c. Request()


```
func (c *AgentClient) Request(ctx context.Context, flags uint8, body []byte) (*RawFrame, error)
```


Example


```
frame, err := client.Request(ctx, m.FlagSessionStart, body)
if err != nil {
    return err
}

var msg map[string]any
if err := cbor.Unmarshal(frame.Body, &msg); err != nil {
    return err
}
```


Send one frame and await a single response frame. Use for request/response RPCs that produce exactly one terminal response (for example a `core.fs.request` to its `core.fs.response`).


Parameters


`ctx` context.Context Cancels the request. `flags` uint8 Frame flag byte, e.g. `FlagSessionStart`. `body` []byte CBOR-encoded protocol message body.


Returns


[*RawFrame](https://docs.microsandbox.dev/sdk/go/agent-client#rawframe) The single response frame. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-stream) c. Stream()


```
func (c *AgentClient) Stream(ctx context.Context, flags uint8, body []byte) (*AgentStream, error)
```


Example


```
stream, err := client.Stream(ctx, m.FlagSessionStart, body)
if err != nil {
    return err
}
defer stream.Close(ctx)

for {
    frame, err := stream.Next(ctx)
    if err != nil {
        return err
    }
    if frame == nil || frame.Flags&m.FlagTerminal != 0 {
        break
    }
}
```


Open a streaming session. The returned [`AgentStream`](https://docs.microsandbox.dev/sdk/go/agent-client#agentstream) carries the protocol correlation id (read it with [`ID()`](https://docs.microsandbox.dev/sdk/go/agent-client#s-id) and pass it to [`Send()`](https://docs.microsandbox.dev/sdk/go/agent-client#c-send) for follow-up frames), and yields frames one at a time via [`Next()`](https://docs.microsandbox.dev/sdk/go/agent-client#s-next).


Parameters


`ctx` context.Context Cancels opening the stream. `flags` uint8 Frame flag byte for the opening frame, e.g. `FlagSessionStart`. `body` []byte CBOR-encoded protocol message body.


Returns


[*AgentStream](https://docs.microsandbox.dev/sdk/go/agent-client#agentstream) Open stream of raw frames. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-send) c. Send()


```
func (c *AgentClient) Send(ctx context.Context, id uint32, flags uint8, body []byte) error
```


Example


```
if err := client.Send(ctx, stream.ID(), 0, stdinBytes); err != nil {
    return err
}
```


Send a follow-up frame on an existing correlation id (for example stdin, a signal, a resize, or data chunks on an open session). Use the id returned by [`AgentStream.ID()`](https://docs.microsandbox.dev/sdk/go/agent-client#s-id).


Parameters


`ctx` context.Context Cancels the send. `id` uint32 Correlation id of an open session. `flags` uint8 Frame flag byte. `body` []byte CBOR-encoded protocol message body.


Returns


error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-readybytes) c. ReadyBytes()


```
func (c *AgentClient) ReadyBytes() ([]byte, error)
```


Example


```
ready, err := client.ReadyBytes()
if err != nil {
    return err
}

var msg map[string]any
if err := cbor.Unmarshal(ready, &msg); err != nil {
    return err
}
```


Return the cached handshake `core.ready` frame body as CBOR bytes. Captured during connect, so this reads from the cached handshake rather than producing protocol traffic.


Returns


[]byte CBOR-encoded `core.ready` frame body. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-close) c. Close()


```
func (c *AgentClient) Close() error
```


Example


```
defer client.Close()
```


Release the client handle. Idempotent: calling it more than once is safe.


Returns


error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#c-closectx) c. CloseCtx()


```
func (c *AgentClient) CloseCtx(ctx context.Context) error
```


Example


```
if err := client.CloseCtx(ctx); err != nil {
    return err
}
```


Release the client handle with a caller-controlled context. Like [`Close()`](https://docs.microsandbox.dev/sdk/go/agent-client#c-close), but lets you bound or cancel the teardown.


Parameters


`ctx` context.Context Cancels the close.


Returns


error Typed microsandbox error.


## [​](https://docs.microsandbox.dev/sdk/go/agent-client#agentstream) AgentStream


Returned by [Stream()](https://docs.microsandbox.dev/sdk/go/agent-client#c-stream)


An open raw agent streaming session. Drive it by calling [`Next()`](https://docs.microsandbox.dev/sdk/go/agent-client#s-next) until it returns `nil`, which happens after a frame carrying [`FlagTerminal`](https://docs.microsandbox.dev/sdk/go/agent-client#flagterminal) or when the underlying stream is exhausted.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#s-next)s. Next()


```
func (s *AgentStream) Next(ctx context.Context) (*RawFrame, error)
```


Example


```
for {
    frame, err := stream.Next(ctx)
    if err != nil {
        return err
    }
    if frame == nil {
        break
    }
}
```


Pull the next frame from the stream. Returns `nil, nil` at EOF, so loop until the frame is `nil` or carries [`FlagTerminal`](https://docs.microsandbox.dev/sdk/go/agent-client#flagterminal).


Parameters


`ctx` context.Context Cancels waiting for the next frame.


Returns


[*RawFrame](https://docs.microsandbox.dev/sdk/go/agent-client#rawframe) Next frame, or `nil` at EOF. error Typed microsandbox error.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#s-id)s. ID()


```
func (s *AgentStream) ID() uint32
```


Example


```
id := stream.ID()
if err := client.Send(ctx, id, 0, stdinBytes); err != nil {
    return err
}
```


Return the protocol correlation id for this stream. Pass it to [`AgentClient.Send()`](https://docs.microsandbox.dev/sdk/go/agent-client#c-send) for follow-up frames in the session.


Returns


uint32 Correlation id for this session.


#### [​](https://docs.microsandbox.dev/sdk/go/agent-client#s-close)s. Close()


```
func (s *AgentStream) Close(ctx context.Context) error
```


Example


```
defer stream.Close(ctx)
```


Release the stream handle.


Parameters


`ctx` context.Context Cancels the close.


Returns


error Typed microsandbox error.


## [​](https://docs.microsandbox.dev/sdk/go/agent-client#types) Types


### [​](https://docs.microsandbox.dev/sdk/go/agent-client#rawframe) RawFrame


Returned by [Request()](https://docs.microsandbox.dev/sdk/go/agent-client#c-request) · yielded by [Next()](https://docs.microsandbox.dev/sdk/go/agent-client#s-next)


A raw protocol frame. `Body` is the CBOR-encoded `Message` body (`v`, `t`, `p`) as it appeared on the wire; decode it with a CBOR library such as `fxamacker/cbor`.


| Field | Type | Description |
| --- | --- | --- |
| ID | `uint32` | Correlation id from the frame header |
| Flags | `uint8` | Frame flags (`FlagTerminal`, `FlagSessionStart`, …) |
| Body | `[]byte` | Raw CBOR-encoded body bytes |


Was this page helpful?

Yes No ⌘ I

---

# Microsandbox CLI YAML configuration reference

`https://docs.microsandbox.dev/cli/configuration`

# Configuration
## Documentation Index
## ​Sparse configuration
## ​Scoped config files
## ​Combining files
## ​Schema
## ​Validation







Configure sandbox resources, networking, and storage with reusable microsandbox CLI YAML files.

Load reusable sandbox settings with `--conf`. See [configuration precedence](https://docs.microsandbox.dev/operations/configuration#precedence) for global defaults.
Common image, resource, lifecycle, environment, policy, secret, script, and patch fields work everywhere. Host-integrated networking, local rootfs forms, snapshots, replace behavior, and several runtime fields are unavailable on microsandbox cloud.
Files may have any name and contain only the fields you need. Explicit CLI arguments override their values.
YAML

```
# sandbox.yaml
image: "python:3.12"
cpus: 2
memory: "1G"
workdir: "/app"
mounts:
  - "./src:/app"
network:
  allow: ["api.openai.com"]
  ports: ["8000:8000"]
secret_violation_action: block-and-log
secrets:
  OPENAI_API_KEY:
    allow: ["api.openai.com"]
    substitution:
      headers: true
      query: false
      body: false
    passthrough: ["telemetry.example.com"]
scripts:
  start: "python app.py"
```


Shell

```
msb run --conf sandbox.yaml -- start
msb create --conf sandbox.yaml --name agent
msb install --conf sandbox.yaml --name agent
```


Files are never auto-discovered; pass each file explicitly.


## [​](https://docs.microsandbox.dev/cli/configuration#sparse-configuration) Sparse configuration


Required fields are checked after merging files and CLI arguments. For example, supply the image separately from a network-only file:
YAML

```
# net-policy.yaml
network:
  policy: public
  allow:
    - "api.openai.com"
  deny:
    - "169.254.169.254"
```


Shell

```
msb run python --conf net-policy.yaml
```


If neither the files nor the arguments provide an image, the command fails before pulling an image or creating sandbox state.


## [​](https://docs.microsandbox.dev/cli/configuration#scoped-config-files) Scoped config files


Scoped files contain one group of settings without its wrapper key. Unrelated fields are rejected.


| Flag | Accepted fields |
| --- | --- |
| `--conf PATH` | Any sandbox configuration field |
| `--net-conf PATH` | `policy`, `allow`, `deny`, `ports`, `dns`, `tls`, `strict`, `trust_host_cas`, `max_tcp_connections`, `max_udp_connections`, `tcp_accept_queue_size` |
| `--resource-conf PATH` | `cpus`, `memory`, `max_duration`, `idle_timeout`, `rlimits` |
| `--runtime-conf PATH` | `workdir`, `shell`, `user`, `hostname`, `security`, `entrypoint`, `cmd`, `env`, `labels`, `init` |
| `--fs-conf PATH` | `mounts`, `patch_files`, `patches` |
| `--secret-conf PATH` | A map of secret names to secret definitions |
| `--script-conf PATH` | A map of script names to shell snippets |


For example, `--net-conf` expects this unwrapped document:
YAML

```
policy: public
allow:
  - "api.openai.com"
deny:
  - "169.254.169.254"
```


Shell

```
msb run python --net-conf net-policy.yaml
```


Passing `network: {...}` to `--net-conf` is an error; use `--conf` for a
root-shaped document.


## [​](https://docs.microsandbox.dev/cli/configuration#combining-files) Combining files


Root and scoped configuration flags are repeatable and may be interleaved. The
CLI applies each file from left to right, then applies explicit flags and
positional arguments. See [Precedence](https://docs.microsandbox.dev/operations/configuration#precedence)
and [Merge precedence](https://docs.microsandbox.dev/operations/configuration#merge-precedence) for the
complete resolution rules.
`--net-conf` cannot be combined with `--net`, `--no-net`, `--net-rule`, or `--net-default*`. When network policy is loaded through a root `--conf` file instead, a policy CLI flag replaces it, while `--net-rule` remains additive and is evaluated before rules loaded from the file.
Shell

```
# Files overlay left to right; --memory wins unless managed policy overrides it.
msb run python \
  --conf base.yaml \
  --resource-conf standard.yaml \
  --conf project.yaml \
  --resource-conf large.yaml \
  --memory 12G
```


Relative host paths are resolved against the file that contains them. Paths inside a file listed by `patch_files` are resolved against that patch file.
For sparse configuration without YAML, see [typed patches in the Rust reference](https://docs.microsandbox.dev/sdk/rust/configuration#sandbox-configuration-patches), including merge behavior and migration from earlier patch types.


## [​](https://docs.microsandbox.dev/cli/configuration#schema) Schema


### [​](https://docs.microsandbox.dev/cli/configuration#image-and-registry) Image and registry


The common image form is a string. Local paths beginning with `.`, `..`, or `/` are resolved as bind roots or disk images; other strings are OCI references.
YAML

```
image: "python:3.12"
pull_policy: missing       # missing | always | never
registry:
  username: "deploy"
  password_env: "REGISTRY_TOKEN"
```


Use the object form to select a source explicitly:
YAML

```
image: { oci: "python:3.12", upper_size: "8G" }
image: { snapshot: "prepared-agent" }
image: { disk: "./ubuntu.qcow2", fstype: ext4 }
image: { bind: "./rootfs" }
```


Exactly one source is allowed. Project layer references are not valid in single-sandbox configuration; consume a published layer as an OCI reference instead.


### [​](https://docs.microsandbox.dev/cli/configuration#resources-and-lifecycle) Resources and lifecycle


YAML

```
cpus: 2
memory: "1G"
max_duration: "12h"
idle_timeout: "10m"
rlimits:
  - { resource: nofile, soft: 8192, hard: 16384 }
  - { resource: nproc, soft: 512 }
```


When `hard` is omitted it equals `soft`.


### [​](https://docs.microsandbox.dev/cli/configuration#runtime) Runtime


YAML

```
workdir: "/app"
shell: "/bin/bash"
user: "app"
hostname: "api"
security: restricted       # default | restricted
entrypoint: ["/usr/bin/tini", "--"]
cmd: ["python", "app.py"]
env:
  MODE: "production"
labels:
  team: "platform"
init:
  cmd: auto                # auto or an absolute guest path
  args: []
  env: {}
```


`cmd` is the default workload for `msb run`. `msb create` stores it without launching it.


### [​](https://docs.microsandbox.dev/cli/configuration#mounts) Mounts


A string mount is a config-relative bind mount using the same `SOURCE:TARGET[:OPTIONS]` option grammar as a bind passed to `-v/--volume`. Options include `ro`, `rw`, `noexec`, `nosuid`, `nodev`, `follow-root-symlinks`, `stat-virt=strict|relaxed|off`, `host-perms=private|mirror`, `quota=<size>`, and paired `uid=<N>,gid=<N>`:
YAML

```
mounts:
  - "./src:/app"
  - "./certs:/etc/app/certs:ro,noexec"
  - "./workspace:/workspace:uid=1000,gid=1000"
```


Object mounts require exactly one source and a guest `target`:
YAML

```
mounts:
  - bind: "./src"
    target: "/app"
    stat_virtualization: strict
    host_permissions: private
    uid: 1000
    gid: 1000
  - named: cache
    target: "/var/cache/app"
    create: ensure-exists
  - tmpfs: { size: "256M" }
    target: "/run"
    noexec: true
  - disk: "./seed.qcow2"
    target: "/seed"
    format: qcow2
    fstype: ext4
    readonly: true
```


All mount kinds accept `readonly`, `noexec`, `nosuid`, and `nodev`. `stat_virtualization`, `host_permissions`, and paired `uid` / `gid` apply only to bind and directory-backed named mounts. Ownership changes only the guest fallback for files without a per-file stat override; it does not change host inode ownership. Duplicate guest targets are rejected.


### [​](https://docs.microsandbox.dev/cli/configuration#rootfs-patches) Rootfs patches


Patch files run first in listed order, followed by inline patches:
YAML

```
patch_files:
  - "./patches/common.yaml"
patches:
  - copy_file: { src: "./config.toml", dst: "/etc/app/config.toml", mode: "0644", replace: true }
  - copy_dir: { src: "./certs", dst: "/etc/app/certs" }
  - text: { path: "/etc/app/build.txt", content: "release", mode: "0644" }
  - file: { path: "/etc/app/blob.bin", content_base64: "SGVsbG8=", mode: "0600" }
  - mkdir: { path: "/var/cache/app", mode: "0755" }
  - symlink: { target: "/etc/app/config.toml", link: "/etc/app/active.toml" }
  - append: { path: "/etc/hosts", content: "10.0.0.5 db.internal\n" }
  - remove: { path: "/etc/motd" }
```


A patch file has one top-level `patches` list using the same operations. File modes must be quoted four-digit octal strings.


### [​](https://docs.microsandbox.dev/cli/configuration#network) Network


Use a preset string for the common cases:
YAML

```
network: public             # none | public | open
```


`public`, the default, permits public internet access while blocking private, loopback, link-local, and metadata destinations. `none` denies ingress and egress. `open` is unrestricted.
The object form adds rules and network services:
YAML

```
network:
  policy: public
  allow: ["api.openai.com", "*.stripe.com"]
  deny: ["169.254.169.254"]
  ports: ["8000:8000", "9100:9100/udp"]
  dns:
    rebind_protection: true
    nameservers: ["1.1.1.1", "8.8.8.8"]
    query_timeout: "5s"
  tls:
    enabled: true
    bypass: ["*.internal.example"]
    verify_upstream: true
    block_quic: true
  strict: true
  trust_host_cas: false
  max_tcp_connections: 256
```


A non-empty `allow` list implies deny-by-default egress. `strict` defaults to `true` and requires hostname-based allow rules to use an inspectable request authority. Plain HTTP exposes that authority in `Host`; HTTPS only exposes it when TLS interception is enabled and not bypassed. Without that visibility, strict mode denies HTTPS that would otherwise be allowed only by a hostname rule. Set `strict: false` to opt out. Top-level `ports` is shorthand for `network.ports`; when both are present, the lists are combined and duplicate host ports are rejected.
Both `ports` lists accept inclusive, equal-length host and guest ranges, including bind addresses and `/tcp` or `/udp`:
YAML

```
network:
  policy: open
  ports:
    - "0.0.0.0:10240-11264:10240-11264/udp"
    - "8000-8002:80-82"
```


Ranges pair ports in ascending order and expand into individual mappings before launch. Endpoints must be from 1 to 65535; reversed, malformed, out-of-bounds, and unequal-length ranges are rejected. The first entry opens 1,025 host sockets, so provision host socket/file-descriptor capacity accordingly. See [Published ports](https://docs.microsandbox.dev/cli/sandbox-commands#published-ports) for bind addresses and resource considerations.


### [​](https://docs.microsandbox.dev/cli/configuration#secrets) Secrets


Every secret requires a non-empty destination allowlist. When `value` is omitted, the host environment variable with the same name is used. An exact `${NAME}` value records `NAME` as the host-side source instead of copying its plaintext into durable config.
YAML

```
secrets:
  OPENAI_API_KEY:
    allow: ["api.openai.com"]
  DATABASE_URL:
    value: "${DB_DSN}"
    allow: ["db.internal"]
    substitution:
      headers: false
      query: false
      body: true
    passthrough: ["audit.internal"]
    violation_action: block-and-terminate
    require_tls_identity: true
```


`substitution` controls headers, query parameters, and request bodies independently; it defaults to headers only, and Basic authentication follows the header setting. On credential-allowed hosts that pass the secret’s identity checks, disabled locations forward the placeholder unchanged. Other destinations must appear in `passthrough` or follow the violation action. `secret_violation_action` sets the sandbox-wide blocking action, while a per-secret `violation_action` overrides it. Declaring a secret enables TLS interception and DNS-rebind protection.


### [​](https://docs.microsandbox.dev/cli/configuration#scripts) Scripts


Scripts are named shell snippets installed as executables in `/.msb/scripts`, which is on `PATH`. The sandbox configuration’s `shell` selects their shebang and defaults to `/bin/sh`.
YAML

```
shell: "/bin/bash"
scripts:
  start: "python app.py"
  migrate: "alembic upgrade head"
```


Run a script like any other guest command:
Shell

```
msb run --conf sandbox.yaml -- migrate
```


## [​](https://docs.microsandbox.dev/cli/configuration#validation) Validation


Sandbox configuration is data, not a templating language. The loader rejects unknown fields, duplicate keys, multiple YAML documents, anchors, aliases, merge keys, and custom tags. Bare YAML 1.1 booleans such as `yes`, `no`, `on`, and `off` are rejected. Quote modes, sizes, durations, ports, domains, image references, and other typed strings.
Only `${NAME}` environment substitution is supported. Substituted variables must exist when the config is loaded; an exact secret `value: "${NAME}"` is the exception because it records a host-side source that is resolved when the sandbox starts. Shell-style operators such as `${NAME:-fallback}`, includes, templates, loops, and expressions are not supported.
Project envelope fields such as `sandboxes`, `volumes`, and `layers`, plus per-project fields such as `depends_on`, are rejected in single-sandbox configuration.


### [​](https://docs.microsandbox.dev/cli/configuration#udp-session-limit) UDP session limit


Set `max_udp_connections` in the network configuration, or pass `--max-udp-connections 512`. The default is unlimited in single-tenant mode and 1,024 relay sessions in multi-tenant mode; zero explicitly selects unlimited. At capacity, new sessions evict the least recently active session.
`max_connections` and `--max-connections` remain deprecated TCP-only aliases for `max_tcp_connections` and `--max-tcp-connections`. Specifying both TCP names in one configuration or command is an error. The UDP limit is independent.


### [​](https://docs.microsandbox.dev/cli/configuration#published-port-accept-queue-size) Published-port accept queue size


Set `tcp_accept_queue_size` in the network configuration, or pass `--tcp-accept-queue-size 4096`, to change how many not-yet-accepted connections each published TCP port queues on the host. The default is 1,024, and values from 1 to 2,147,483,647 are accepted; the host kernel caps the effective depth at its own `somaxconn`. See [Published ports](https://docs.microsandbox.dev/cli/sandbox-commands#published-ports).

Was this page helpful?

Yes No ⌘ I

---

# Secret handling - microsandbox

`https://docs.microsandbox.dev/security/secrets`

# Secret handling
## Documentation Index
## ​The idea
## ​The data flow
## ​What gates a substitution
## ​What this protects
## ​What this does not protect
## ​Where the values live
## ​See also









How credentials stay on the host, and the exact boundary of the guarantee

Secret injection keeps credentials out of the guest while allowing requests to trusted endpoints. This page explains the boundary of that protection. For the configuration surface like binding secrets, allow lists, and placeholders, see [Secrets](https://docs.microsandbox.dev/sandboxes/secrets).


## [​](https://docs.microsandbox.dev/security/secrets#the-idea) The idea


Instead of putting a real credential inside the VM, microsandbox puts a **placeholder** there. The real value stays in host memory. When the guest sends a request to a host you’ve allowed, the host-side network stack swaps the placeholder for the real value at the network boundary, on the way out. Anywhere else, the placeholder is just a meaningless string.
So a workload can call an API with a credential it never actually holds.


## [​](https://docs.microsandbox.dev/security/secrets#the-data-flow) The data flow


1. You bind a secret to an environment variable and list the hosts it’s allowed for.
2. The guest’s environment receives a placeholder (`$MSB_<env_var>` by default), never the real value.
3. The workload uses the placeholder as if it were the credential, in a header, auth field, query string, or body.
4. On egress to an allowed host, the host-side proxy decrypts the intercepted TLS, verifies the request is really going where it claims, substitutes the real value, and forwards it upstream.
5. The upstream server receives the real credential. The guest never did.


![A placeholder becomes the real secret only at an allowed host; any other host receives only the placeholder.](https://mintcdn.com/superradcompanyinc/b2Kff8GKGqDeh1zw/images/security/secret-substitution-light.svg?fit=max&auto=format&n=b2Kff8GKGqDeh1zw&q=85&s=4c049d00ea27c5104586c2f22f5486f4)![A placeholder becomes the real secret only at an allowed host; any other host receives only the placeholder.](https://mintcdn.com/superradcompanyinc/b2Kff8GKGqDeh1zw/images/security/secret-substitution-dark.svg?fit=max&auto=format&n=b2Kff8GKGqDeh1zw&q=85&s=bfdae0dc431cdb133bbfe0d7189b7f26)


## [​](https://docs.microsandbox.dev/security/secrets#what-gates-a-substitution) What gates a substitution


A placeholder only becomes a real value when **every** one of these holds. They use the same DNS and SNI machinery the [network page](https://docs.microsandbox.dev/security/network#dns-to-ip-binding-toctou) describes:


- **Allowed-host match.** The TLS SNI matches one of the secret’s allowed host patterns.
- **DNS pin.** The destination IP was actually resolved for that host through the interceptor, so a hard-coded IP with a forged SNI doesn’t qualify.
- **TLS identity.** By default a secret requires intercepted TLS, so it is never substituted over a connection the host can’t see into.
- **Authority alignment.** For intercepted HTTP, the request’s `Host` or `:authority` must match the SNI, which closes domain-fronting.
- **Header scope.** When a secret sets `header_fields`, the placeholder is replaced only in those header fields; a placeholder anywhere else is treated as a disabled location: on a verified allowed destination it is forwarded unchanged, while other destinations follow the violation policy. A non-empty list with header substitution disabled is rejected. Restrict this to the credential header (for example `authorization`) so a reflecting endpoint cannot return the secret in an unrelated header.


Once the destination passes the secret’s host and TLS identity checks, placeholders outside enabled substitution locations are forwarded unchanged. If those checks fail and there is no explicit placeholder permission, detecting a placeholder blocks the request and logs a warning by default. You can choose silent blocking, sandbox termination, or scoped passthrough of the unchanged placeholder. See [Violation policy](https://docs.microsandbox.dev/sandboxes/secrets#violation-actions). Opaque, bypassed TLS cannot be inspected for placeholders.


## [​](https://docs.microsandbox.dev/security/secrets#what-this-protects) What this protects


- **The credential cannot leak to a host you didn’t allow.** Detected requests to disallowed hosts are blocked by default; explicitly permitted passthrough sends only the placeholder.
- **Secret bindings do not give the guest the credential.** Guest code receives the placeholder. This does not protect credentials separately supplied to the guest or returned by an allowed endpoint.
- **Hard-coded-IP and SNI-spoof exfiltration attempts** don’t receive the injection at all, because they fail the DNS pin or authority checks.


## [​](https://docs.microsandbox.dev/security/secrets#what-this-does-not-protect) What this does not protect


Being candid about the edges matters more than the headline.


- **The allowed endpoint receives the real credential.** This stops exfiltration to *other* hosts. It does not stop the host you explicitly allowed from misusing what you sent it. Keep allow lists narrow. An allowed endpoint that echoes a credential in its response can expose it to the guest, so scope substitution to the intended header with `header_fields` instead of substituting in every header.
- **It needs TLS inspection for that host.** Over a bypassed-TLS domain, or plain HTTP with the default TLS-identity requirement on, no substitution happens. That’s by design, since the host can’t verify where opaque traffic is really going. You can opt a secret into plain-HTTP injection, but it’s weaker and not recommended.
- **A few content shapes aren’t rewritten.** Body injection is opt-in and has format, encoding, and size limits. When body injection is enabled, encoded bodies are forwarded unchanged unless a placeholder is detected; detected placeholders in unsupported body formats are blocked. See [SecretSubstitution](https://docs.microsandbox.dev/sdk/typescript/secrets#secretsubstitution).
- **Real values live in host process memory.** The host must access real values to inject them. Anyone who can read the host process’s memory is already on the trusted side of the boundary, and [host compromise is out of scope](https://docs.microsandbox.dev/security/overview#scope-what-the-boundary-covers) for the model.


## [​](https://docs.microsandbox.dev/security/secrets#where-the-values-live) Where the values live


Secret bindings put placeholders in the guest environment. Raw values supplied through an SDK are also persisted in the host-side sandbox configuration; stopping the sandbox does not remove that copy. Host environment references avoid storing the value in that configuration. See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets#add-a-secret) for storage and rotation guidance.


## [​](https://docs.microsandbox.dev/security/secrets#see-also) See also


- [Secrets](https://docs.microsandbox.dev/sandboxes/secrets): binding secrets, placeholders, and allow lists
- [TLS inspection](https://docs.microsandbox.dev/networking/tls): what interception sees and what bypass makes opaque
- [Network defenses](https://docs.microsandbox.dev/security/network): the DNS pin and SNI checks the gates share


Was this page helpful?

Yes No ⌘ I

---

# TypeScript SDK Secrets reference

`https://docs.microsandbox.dev/sdk/typescript/secrets`

See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets) for usage examples and security boundaries.


## [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) SecretBuilder


Builder for one secret configuration.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-env) secret. env()


```
env(varName: string): this
```


Set the environment variable name that holds the placeholder inside the guest. The guest sees `$MSB_<varName>` (or a custom [`placeholder`](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-placeholder)), never the real value. Names must be non-empty and cannot contain `=` or NUL; shell-identifier syntax is not required. **Required.**


Parameters


`varName` string Environment variable name (non-empty, no `=` or NUL).


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-value) secret. value()


```
value(value: string): this
```


Set the real secret value. This is the string that replaces the placeholder when a request reaches an allowed host. It never enters the guest VM. **Required.**


Parameters


`value` string The actual credential or token.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-placeholder) secret. placeholder()


```
placeholder(placeholder: string): this
```


Override the auto-generated placeholder string. By default microsandbox generates `$MSB_<envVar>`. Use this when you need a specific format or when the placeholder must match a particular byte length. Placeholders must be non-empty, at most 1024 bytes, and cannot contain NUL, CR, or LF.


Parameters


`placeholder` string Custom placeholder string: non-empty, up to 1024 bytes, no NUL/CR/LF.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-allow) secret. allow()


```
allow(host: string): this
```


Example


```
.secret((s) =>
  s.env("STRIPE_KEY")
    .value(process.env.STRIPE_KEY!)
    .allow("api.stripe.com")
    .allow("files.stripe.com"),
)
```


Add an exact host or wildcard pattern allowed to receive the real secret value. A `*.suffix` pattern matches the suffix itself and its single- or multi-label subdomains. The proxy checks the host against the connection’s verified TLS identity and observed DNS history. Can be called multiple times to allow several hosts. At least one allowed host (exact, pattern, or any) is required.


Parameters


`host` string Hostname or wildcard pattern, e.g. `“api.example.com”` or `“*.example.com”` (ASCII case-insensitive).


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-allowanyhostdangerous) secret. allowAnyHostDangerous()


```
allowAnyHostDangerous(iUnderstand: boolean): this
```


Allow substitution on **any** host. Every server the guest connects to can then receive the real secret, which effectively disables host-based protection. The call is a no-op unless `iUnderstand` is `true`. Only use this when the secret is not sensitive or the sandbox network is fully locked down. This is the one allow-list pattern that skips DNS and TLS-identity pinning.


Parameters


`iUnderstand` boolean Must be `true` to take effect.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-requiretlsidentity) secret. requireTlsIdentity()


```
requireTlsIdentity(enabled: boolean): this
```


When `true`, the secret is only substituted on TLS-intercepted connections where the proxy has verified it is performing MITM and the SNI matches an allowed host. Bypassed TLS is opaque and never receives substitution. Disable only when you know the traffic path is safe and explicitly supports non-TLS substitution. Default: `true`.


Parameters


`enabled` boolean Require verified TLS identity. Default: `true`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinheaders) secret. substituteInHeaders()


```
substituteInHeaders(enabled: boolean): this
```


Control whether the placeholder is replaced anywhere in HTTP headers, including decoded and re-encoded Basic authentication credentials. This is the most common injection scope, covering `Authorization: Bearer $MSB_...` and similar patterns. Default: `true`.


Parameters


`enabled` boolean Substitute in headers. Default: `true`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinheaderfields) secret. substituteInHeaderFields()


```
substituteInHeaderFields(fields: string[]): this
```


Enable header substitution but restrict it to the given header field names (matched case-insensitively), for example `["authorization"]`. A placeholder found in any other header is treated as a disabled location: on a verified allowed destination it is forwarded unchanged, while other destinations follow the violation policy. An empty list restores the default of substituting in every header. A non-empty list with header substitution disabled is rejected. Names must be valid HTTP field names.
Restricting this list matters for confidentiality, not just correctness: with every header substitutable, an untrusted guest can place the placeholder in a header the upstream host reflects back in its response and read the real secret from that response. Allow only the intended credential header.


Parameters


`fields` string[] Header field names allowed to receive the substitution. Empty restores all headers.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinquery) secret. substituteInQuery()


```
substituteInQuery(enabled: boolean): this
```


Control whether the placeholder is replaced in the URL query string (the `?key=value` portion of the request line). Default: `false`.


Parameters


`enabled` boolean Substitute in query parameters. Default: `false`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinbody) secret. substituteInBody()


```
substituteInBody(enabled: boolean): this
```


Control whether the placeholder is replaced in inspectable request bodies. When enabled, fixed-length HTTP/1 bodies up to 16 MiB are rewritten with an updated `Content-Length`; larger fixed-length bodies are blocked. Chunked HTTP/1 bodies are decoded and re-encoded with fresh chunk sizes. Encoded bodies pass through unchanged. HTTP/2 DATA-frame body substitution is unsupported, and matching body placeholders are blocked. Default: `false`.


Parameters


`enabled` boolean Substitute in request bodies. Default: `false`.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-allowplaceholderfor) secret. allowPlaceholderFor()


```
allowPlaceholderFor(host: string): this
```


Allow an exact host or wildcard pattern to receive the placeholder unchanged when it cannot be substituted. Repeat this method for multiple hosts. `allowPassthroughFor()` remains a deprecated alias. This never grants permission to receive the real secret; use [`allow()`](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-allow) for substitution. Credential-allowed hosts already permit unchanged placeholders outside enabled substitution locations once the secret’s host and TLS identity checks pass. Without either permission, the configured blocking action applies.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-violationaction) secret. violationAction()


```
violationAction(action: "block" | "block-and-log" | "block-and-terminate"): this
```


Override the [sandbox-wide action](https://docs.microsandbox.dev/sdk/typescript/secrets#networkbuilder-secretviolationaction) for this secret. Omitting this method inherits the network setting, whose default is `"block-and-log"`. Invalid action strings throw an error. Passthrough is a separate per-secret host policy, not a violation action.


Example


```
.secret((s) =>
  s.env("API_KEY")
    .value(process.env.API_KEY!)
    .allow("api.github.com")
    .allowPlaceholderFor("api.anthropic.com")
    .substituteInBody(true)
    .violationAction("block-and-terminate"),
)
```


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-build) secret. build()


```
build(): SecretEntry
```


Materialize the [`SecretEntry`](https://docs.microsandbox.dev/sdk/typescript/secrets#secretentry). Called for you by [`SandboxBuilder.secret`](https://docs.microsandbox.dev/sdk/typescript/secrets#sandboxbuilder-secret), so you rarely call it directly. If [`placeholder`](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-placeholder) was not set, it defaults to `$MSB_<envVar>`. Consumes the builder; do not reuse it afterward. Throws if `env` or `value` was not set, or if the allow-list is empty. Sandbox configuration validation also rejects invalid environment names or placeholders and configurations with every substitution site disabled.


Returns


[SecretEntry](https://docs.microsandbox.dev/sdk/typescript/secrets#secretentry) The materialized secret entry.


## [​](https://docs.microsandbox.dev/sdk/typescript/secrets#sandboxbuilder) SandboxBuilder


Two methods on [`SandboxBuilder`](https://docs.microsandbox.dev/sdk/typescript/sandbox) for adding secrets without reaching into a [`NetworkBuilder`](https://docs.microsandbox.dev/sdk/typescript/networking). Both automatically enable TLS interception.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#sandbox-secret) sandbox. secret()


```
secret(configure: (s: SecretBuilder) => SecretBuilder): this
```


Example


```
await using sb = await Sandbox.builder("payments-worker")
  .image("python")
  .secret((s) =>
    s.env("STRIPE_KEY")
      .value(process.env.STRIPE_KEY!)
      .allow("api.stripe.com")
      .allow("*.stripe.com")
      .substituteInHeaders(true)
      .substituteInQuery(false),
  )
  .create();
```


Add a secret with full configuration via a [`SecretBuilder`](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) closure. The builder’s [`build()`](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-build) is called for you.


Parameters


`configure` [(s: SecretBuilder) => SecretBuilder](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) Configure the secret.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#sandbox-secretenv) sandbox. secretEnv()


```
secretEnv(envVar: string, value: string, allowedHost: string): this
```


Example


```
await using sb = await Sandbox.builder("agent")
  .image("python")
  .secretEnv("OPENAI_API_KEY", process.env.OPENAI_API_KEY!, "api.openai.com")
  .create();
```


Three-argument shorthand. Auto-generates the placeholder as `$MSB_<envVar>` and allows substitution only on `allowedHost`. The default injection scopes apply (headers and Basic Auth enabled, query and body disabled).
**Plaintext at rest.** The value is persisted verbatim in the durable sandbox config until a later modify rotate migrates the entry to a source reference. Use this path when you hold only a value; use source references through the [live-modify API](https://docs.microsandbox.dev/sandboxes/secrets#update-secrets) when the value is available in the host environment.


Parameters


`envVar` string Environment variable name (non-empty, no `=` or NUL). `value` string Secret value. `allowedHost` string Allowed destination host (exact match).


## [​](https://docs.microsandbox.dev/sdk/typescript/secrets#networkbuilder) NetworkBuilder


The same secret configuration is available inside [`SandboxBuilder.network(n => ...)`](https://docs.microsandbox.dev/sdk/typescript/networking) for callers who are already configuring networking. These methods set the secrets and the sandbox-wide violation policy directly on the network.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#network-secret) network. secret()


```
secret(configure: (s: SecretBuilder) => SecretBuilder): this
```


Example


```
await using sb = await Sandbox.builder("agent")
  .image("python")
  .network((n) =>
    n.secret((s) =>
      s.env("OPENAI_API_KEY")
        .value(process.env.OPENAI_API_KEY!)
        .allow("api.openai.com"),
    ),
  )
  .create();
```


Add a secret with full configuration via a [`SecretBuilder`](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) closure. Identical in behavior to [`SandboxBuilder.secret`](https://docs.microsandbox.dev/sdk/typescript/secrets#sandboxbuilder-secret).


Parameters


`configure` [(s: SecretBuilder) => SecretBuilder](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder) Configure the secret.


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#network-secretenv) network. secretEnv()


```
secretEnv(envVar: string, value: string, placeholder: string, allowedHost: string): this
```


Four-argument shorthand. Same as the `SandboxBuilder` form but lets you provide the placeholder explicitly instead of auto-generating `$MSB_<envVar>`.


Parameters


`envVar` string Environment variable name (non-empty, no `=` or NUL). `value` string Secret value. `placeholder` string Explicit placeholder: non-empty, up to 1024 bytes, no NUL/CR/LF. `allowedHost` string Allowed destination host (exact match).


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#network-secretenvsimple) network. secretEnvSimple()


```
secretEnvSimple(envVar: string, value: string, allowedHost: string): this
```


Three-argument shorthand on `NetworkBuilder`. Auto-generates the placeholder as `$MSB_<envVar>`, matching [`SandboxBuilder.secretEnv`](https://docs.microsandbox.dev/sdk/typescript/secrets#sandboxbuilder-secretenv). Like `NetworkBuilder.secret()` and `NetworkBuilder.secretEnv()`, it enables TLS interception while preserving other TLS settings. The guest receives only the placeholder. Earlier SDK versions incorrectly exposed the supplied secret as the placeholder in this helper. Code that intentionally needs a raw guest environment value should use ordinary environment configuration; this helper keeps the credential on the host. Updating the SDK does not rewrite existing sandbox configurations; recreate or explicitly reconfigure sandboxes created with the affected helper.


Parameters


`envVar` string Environment variable name (non-empty, no `=` or NUL). `value` string Secret value. `allowedHost` string Allowed destination host (exact match).


#### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#network-secretviolationaction) network. secretViolationAction()


```
secretViolationAction(action: "block" | "block-and-log" | "block-and-terminate"): this
```


Set the sandbox-wide blocking action for placeholders that cannot be substituted or passed through. [`SecretBuilder.violationAction()`](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-violationaction) overrides it per secret. This method belongs to `NetworkBuilder`, so configure it through `SandboxBuilder.network()`.


Example


```
await using sb = await Sandbox.builder("agent")
  .image("python")
  .network((n) =>
    n.secretEnvSimple("OPENAI_API_KEY", process.env.OPENAI_API_KEY!, "api.openai.com")
      .secretViolationAction("block-and-log"),
  )
  .create();
```


## [​](https://docs.microsandbox.dev/sdk/typescript/secrets#types) Types


### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secretentry) SecretEntry


Returned by [SecretBuilder.build()](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-build)


The materialized object produced by `SecretBuilder.build()`. Configure secrets through the builder; its output is not the sparse live-modification input.


| Field | Type | Description |
| --- | --- | --- |
| `envVar` | `string` | Environment variable name (non-empty, no `=` or NUL) |
| `value` | `string` | Real secret value (stays on the host; raw values are persisted) |
| `placeholder` | `string` | Guest-visible placeholder; defaults to `$MSB_<envVar>`, non-empty, at most 1024 bytes, no NUL/CR/LF |
| `allowedHosts` | `string[]` | Exact allowed hosts |
| `allowedHostPatterns` | `string[]` | Wildcard allowed hosts |
| `allowAnyHost` | `boolean` | Permit substitution to any host |
| `passthroughHosts` | `string[]` | Hosts or patterns allowed to receive the unchanged placeholder |
| `requireTlsIdentity` | `boolean` | Require verified TLS identity before substitution |
| `substitution` | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/typescript/secrets#secretsubstitution) | Enabled request locations |


### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#secretsubstitution) SecretSubstitution


Used by [SecretEntry.substitution](https://docs.microsandbox.dev/sdk/typescript/secrets#secretentry)


The materialized substitution settings. Set them through the `substituteIn*` methods on [`SecretBuilder`](https://docs.microsandbox.dev/sdk/typescript/secrets#secretbuilder). At least one location must remain enabled. On credential-allowed hosts that pass the secret’s identity checks, disabled locations forward the placeholder unchanged. Other destinations require explicit placeholder permission or follow the violation action.


| Field | Type | Builder default | Description |
| --- | --- | --- | --- |
| `headers` | `boolean` | `true` | Substitute in headers, including Basic authentication. |
| `headerFields` | `string[]` | `[]` (all) | When non-empty, restrict header substitution to these field names. |
| `query` | `boolean` | `false` | Substitute in URL query parameters. |
| `body` | `boolean` | `false` | Substitute in supported bodies; see [limits](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-substituteinbody). |


### [​](https://docs.microsandbox.dev/sdk/typescript/secrets#violationaction) ViolationAction


Used by [SecretBuilder.violationAction()](https://docs.microsandbox.dev/sdk/typescript/secrets#secret-violationaction) · [NetworkBuilder.secretViolationAction()](https://docs.microsandbox.dev/sdk/typescript/secrets#networkbuilder-secretviolationaction)


The `ViolationActions` array enumerates these values. Per-secret settings override the network default; passthrough is configured separately.


```
type ViolationAction = "block" | "block-and-log" | "block-and-terminate";
```


| Value | Description |
| --- | --- |
| `"block"` | Block the request without logging. |
| `"block-and-log"` | Block and emit a warning on the host. This is the default. |
| `"block-and-terminate"` | Block, log an error, and shut down the sandbox. |
## Documentation Index
## ​SecretBuilder
## ​SandboxBuilder
## ​NetworkBuilder
## ​Types







Was this page helpful?

Yes No ⌘ I

---

# TLS inspection - microsandbox

`https://docs.microsandbox.dev/networking/tls`

Local-only
TLS inspection lets microsandbox inspect HTTPS traffic. This enables URL policy checks, request logging, and secure secret injection for matching hosts.


## [​](https://docs.microsandbox.dev/networking/tls#how-it-works) How it works


When interception is enabled, microsandbox:


1. Loads an interception certificate authority, or CA.
2. Adds that CA to the guest’s trust store.
3. Creates a certificate for each intercepted host.
4. Opens a separate verified TLS connection to the upstream server.


microsandbox stores the default CA at `~/.microsandbox/tls/ca.{crt,key}` and reuses it across local sandboxes. Delete both files to generate a new CA. Use the intercept CA certificate and key settings when sandboxes should use a CA that you provide.
For new local sandboxes, relative paths to upstream CA certificates and interception CA certificate/key files are resolved when the sandbox is created and saved as absolute paths. Starting the same sandbox from another working directory does not select different TLS files. Existing saved sandboxes with relative TLS paths retain their previous resolution behavior. They remain usable without recreation, and restart does not rewrite their saved paths.


## [​](https://docs.microsandbox.dev/networking/tls#enabling-interception) Enabling interception


Enable interception with the default settings as shown below. Configuring TLS options also enables it, so no separate shortcut is needed when setting bypass hosts or custom certificates.
TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
  .image("python")
  .interceptTls()
  .create();
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("worker")
    .image("python")
    .intercept_tls()
    .create()
    .await?;
```


```
from microsandbox import Sandbox

sb = await Sandbox.create(
    "worker",
    image="python",
    intercept_tls=True,
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithInterceptTLS(),
)
```


```
require "microsandbox"

sb = Microsandbox::Sandbox.create("worker", image: "python", intercept_tls: true)
```


```
msb create python --name worker --tls-intercept
```


## [​](https://docs.microsandbox.dev/networking/tls#trusting-certificates-in-applications) Trusting certificates in applications


Applications with their own certificate stores may need extra setup.
We provide [msb-trust.sh](https://github.com/superradcompany/microsandbox/blob/main/scripts/msb-trust/msb-trust.sh),
a helper script that configures common applications to trust the Microsandbox TLS CA.
Save it as `./msb-trust.sh`, copy it into the sandbox, and run it after boot.
TypeScript Rust Python Go Ruby CLI

```
import { Sandbox } from "microsandbox";

const sb = await Sandbox.builder("app")
  .image("ubuntu:24.04")
  .interceptTls()
  .patch((p) => p.copyFile("./msb-trust.sh", "/msb-trust.sh"))
  .create();

const setup = await sb.shell("sh /msb-trust.sh all");
if (!setup.success) throw new Error(setup.stderr());
console.log(setup.stdout());
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("app")
    .image("ubuntu:24.04")
    .intercept_tls()
    .patch(|p| p.copy_file("./msb-trust.sh", "/msb-trust.sh", None, false))
    .create()
    .await?;

let setup = sb.shell("sh /msb-trust.sh all").await?;
if !setup.status().success {
    return Err(setup.stderr()?.into());
}
print!("{}", setup.stdout()?);
```


```
from microsandbox import Patch, Sandbox

sb = await Sandbox.create(
    "app",
    image="ubuntu:24.04",
    intercept_tls=True,
    patches=[Patch.copy_file("./msb-trust.sh", "/msb-trust.sh")],
)

setup = await sb.shell("sh /msb-trust.sh all")
if setup.exit_code != 0:
    raise RuntimeError(setup.stderr_text)
print(setup.stdout_text)
```


```
sb, err := m.CreateSandbox(ctx, "app",
    m.WithImage("ubuntu:24.04"),
    m.WithInterceptTLS(),
    m.WithPatches(m.Patch.CopyFile(
        "./msb-trust.sh", "/msb-trust.sh", m.PatchOptions{},
    )),
)
if err != nil {
    log.Fatal(err)
}

setup, err := sb.Shell(ctx, "sh /msb-trust.sh all")
if err != nil {
    log.Fatal(err)
}
if !setup.Success() {
    log.Fatal(setup.Stderr())
}
fmt.Print(setup.Stdout())
```


```
require "microsandbox"

sb = Microsandbox::Sandbox.create("app", image: "ubuntu:24.04", intercept_tls: true)
sb.fs.write("/msb-trust.sh", File.binread("./msb-trust.sh"))

setup = sb.shell("sh /msb-trust.sh all")
raise setup.stderr unless setup.success?
puts setup.stdout
sb.detach
```


```
msb create ubuntu:24.04 --name app \
  --tls-intercept \
  --copy-file ./msb-trust.sh:/msb-trust.sh

msb exec app -- sh /msb-trust.sh all
```


The examples use `all` to configure supported applications whose tools are installed
and report missing prerequisites. To choose specific applications, run
`sh /msb-trust.sh --help` for the supported names, then pass one or more names
instead of `all`.
The helper tries every selected application and returns an error if any cannot be configured.
Missing your application? PRs are welcome. We consider broad usefulness and
maintenance effort when deciding which applications to support.


## [​](https://docs.microsandbox.dev/networking/tls#bypass-patterns) Bypass patterns


Some clients trust a specific certificate or public key instead of the guest’s trust store. Interception will fail for these clients.
Add their hosts to the bypass list. Exact domains such as `api.example.com` and wildcards such as `*.apple.com` are supported. Bypassed traffic stays encrypted between the guest and upstream server, so content-based policy checks and secret injection do not apply.
TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
  .image("python")
  .network((n) => n.tls((t) =>
    t.bypass("pinned-api.example.com").bypass("*.gov"),
  ))
  .create();
```


```
use microsandbox::Sandbox;

let sb = Sandbox::builder("worker")
    .image("python")
    .network(|n| n.tls(|t| t
        .bypass("pinned-api.example.com")
        .bypass("*.gov")
    ))
    .create()
    .await?;
```


```
from microsandbox import Network, Sandbox, TlsConfig

sb = await Sandbox.create(
    "worker",
    image="python",
    network=Network(
        tls=TlsConfig(bypass=("pinned-api.example.com", "*.gov")),
    ),
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        TLS: &m.TLSConfig{
            Bypass: []string{"pinned-api.example.com", "*.gov"},
        },
    }),
)
```


```
msb create python --name worker \
  --tls-intercept \
  --tls-bypass "pinned-api.example.com" \
  --tls-bypass "*.gov"
```


## [​](https://docs.microsandbox.dev/networking/tls#upstream-ca-trust) Upstream CA trust


The proxy verifies upstream certificates with the host’s root store by default. You can add:


- a CA trusted for every intercepted host
- a CA trusted only for matching hosts
- a host pattern that skips upstream verification


TypeScript Rust Python Go CLI

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("agent")
  .image("python")
  .network((n) => n.tls((t) =>
    t.upstreamCaCert("/etc/ssl/corp-root.pem")
      .upstreamCaCertFor("api.internal.example.com", "./certs/api-ca.pem")
      .verifyUpstreamFor("*.preview.internal", false),
  ))
  .create();
```


```
let sb = Sandbox::builder("agent")
    .image("python")
    .network(|n| n.tls(|t| t
        .upstream_ca_cert("/etc/ssl/corp-root.pem")
        .upstream_ca_cert_for("api.internal.example.com", "./certs/api-ca.pem")
        .verify_upstream_for("*.preview.internal", false)
    ))
    .create()
    .await?;
```


```
from microsandbox import (
    Network, Sandbox, ScopedUpstreamCACert, ScopedVerifyUpstream, TlsConfig,
)

sb = await Sandbox.create(
    "agent",
    image="python",
    network=Network(tls=TlsConfig(
        upstream_ca_certs=("/etc/ssl/corp-root.pem",),
        scoped_upstream_ca_certs=(
            ScopedUpstreamCACert("api.internal.example.com", "./certs/api-ca.pem"),
        ),
        scoped_verify_upstream=(
            ScopedVerifyUpstream("*.preview.internal", False),
        ),
    )),
)
```


```
sb, err := m.CreateSandbox(ctx, "agent",
    m.WithImage("python"),
    m.WithNetwork(&m.NetworkConfig{
        TLS: &m.TLSConfig{
            UpstreamCACerts: []string{"/etc/ssl/corp-root.pem"},
            ScopedUpstreamCACerts: []m.ScopedUpstreamCACert{
                {Pattern: "api.internal.example.com", Path: "./certs/api-ca.pem"},
            },
            ScopedVerifyUpstream: []m.ScopedVerifyUpstream{
                {Pattern: "*.preview.internal", Verify: false},
            },
        },
    }),
)
if err != nil {
    return err
}
```


```
msb create python --name agent \
  --tls-intercept \
  --tls-upstream-ca-cert /etc/ssl/corp-root.pem \
  --tls-upstream-ca-cert-for 'api.internal.example.com=./certs/api-ca.pem' \
  --tls-no-verify-upstream-for '*.preview.internal'
```


Skipping verification is similar to using `curl -k`. Use it only for hosts you control and only when a trusted CA is not available.


## [​](https://docs.microsandbox.dev/networking/tls#limits) Limits


- Clients that pin certificates or public keys must be bypassed.
- Bypassed traffic cannot use content-based policy checks or secret injection.
- microsandbox does not proxy guest client certificates. Bypass hosts that require guest mTLS.
- microsandbox does not intercept QUIC and HTTP/3 traffic.


## [​](https://docs.microsandbox.dev/networking/tls#trusting-host-cas) Trusting host CAs


Corporate proxies often replace server certificates with certificates signed by a company CA. The host trusts that CA, but a sandbox normally does not. Commands such as `apk update`, `pip install`, and `curl` can then fail with a certificate error.
Enable host CA trust to copy trusted host roots into the guest when it starts:
TypeScript Rust Python Go CLI

```
await using sb = await Sandbox.builder("devbox")
  .image("alpine")
  .network((n) => n.trustHostCAs(true))
  .create();
```


```
let sb = Sandbox::builder("devbox")
    .image("alpine")
    .network(|n| n.trust_host_cas(true))
    .create()
    .await?;
```


```
sb = await Sandbox.create(
    "devbox",
    image="alpine",
    network=Network(trust_host_cas=True),
)
```


```
trustHostCAs := true
sb, err := m.CreateSandbox(ctx, "devbox",
    m.WithImage("alpine"),
    m.WithNetwork(&m.NetworkConfig{
        TrustHostCAs: &trustHostCAs,
    }),
)
```


```
msb run alpine --trust-host-cas -- apk update
```


Host CA trust gives the guest every root certificate trusted by the host. Enable it only when you trust the host’s CA store.
Host CA trust can be used alongside TLS inspection. Enable both when connections that bypass inspection, such as Postgres or Redis over TLS, also need to trust your host’s certificates.


## [​](https://docs.microsandbox.dev/networking/tls#reference) Reference


For exact TLS and network APIs, see [TypeScript](https://docs.microsandbox.dev/sdk/typescript/networking#tlsbuilder), [Rust](https://docs.microsandbox.dev/sdk/rust/networking#tlsbuilder), [Python](https://docs.microsandbox.dev/sdk/python/networking#tlsconfig), or [Go](https://docs.microsandbox.dev/sdk/go/networking#tlsconfig). For CLI fields and flags, see [Sandbox configuration](https://docs.microsandbox.dev/cli/configuration#network) and [Sandbox commands](https://docs.microsandbox.dev/cli/sandbox-commands).


- [DNS](https://docs.microsandbox.dev/networking/dns) explains DNS policy and DNS over TLS.
- [Proxies](https://docs.microsandbox.dev/networking/outbound-proxy) explains routing outbound TCP and non-DNS UDP through an external SOCKS proxy.
- [Network defenses](https://docs.microsandbox.dev/security/network) explains SSRF protection.
- [Secret handling](https://docs.microsandbox.dev/security/secrets) explains credential injection.
## Documentation Index
## ​How it works
## ​Enabling interception
## ​Trusting certificates in applications
## ​Bypass patterns
## ​Upstream CA trust
## ​Limits
## ​Trusting host CAs
## ​Reference
## ​Related












Was this page helpful?

Yes No ⌘ I

---

# Rust SDK Secrets reference

`https://docs.microsandbox.dev/sdk/rust/secrets`

See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets) for usage examples and security boundaries.


## [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder) SecretBuilder


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuildernew) SecretBuilder:: new()


```
fn new() -> SecretBuilder
```


Example


```
use microsandbox::sandbox::SecretBuilder;

let entry = SecretBuilder::new()
    .env("STRIPE_KEY")
    .value(stripe_key)
    .allow("api.stripe.com")
    .build();
```


Start building a secret with defaults: no env var, no value, no allowed hosts, the default [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/rust/secrets#secretsubstitution) (headers and Basic Auth on, query and body off), no per-secret violation override, and `require_tls_identity = true`. You rarely call this yourself: [`SandboxBuilder::secret(|s| s...)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret) hands you a fresh builder and calls [`build()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-build) for you. `SecretBuilder::default()` is equivalent.


Returns


[SecretBuilder](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder) A builder with default injection scopes.


Builder methods


Builder for one secret’s placeholder, allowed hosts, and injection scopes. Obtained through [`SandboxBuilder::secret(|s| s...)`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret) or [`SecretBuilder::new()`](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuildernew); each secret maps an environment variable to a real value that is only revealed when traffic reaches an allowed host through the TLS proxy. Every setter returns `Self`, so calls chain. [`env()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-env), exactly one of [`value()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-value) or [`source()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-source), and at least one allowed host are required; [`build()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-build) panics otherwise.
Import path: `microsandbox::sandbox::SecretBuilder`. Adding any secret automatically enables TLS interception.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-env) secret. env()


```
fn env(self, var: impl Into<String>) -> Self
```


Set the environment variable name that holds the placeholder inside the guest. The guest sees `$MSB_<var>` (or a custom [`placeholder`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-placeholder)), never the real value. Names must be non-empty and cannot contain `=` or NUL; shell-identifier syntax is not required since Linux only requires a `NAME=value` shape. **Required.**


Parameters


`var` impl Into<String> Environment variable name (non-empty, no `=` or NUL).


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-value) secret. value()


```
fn value(self, value: impl Into<String>) -> Self
```


Set the real secret value. This is the string that replaces the placeholder when a request reaches an allowed host. It never enters the guest VM, but inline values are persisted verbatim in the durable sandbox configuration. Mutually exclusive with [`source()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-source); prefer a source reference when available.


Parameters


`value` impl Into<String> The actual credential or token.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-source) secret. source()


```
fn source(self, source: SecretSource) -> Self
```


Resolve secret material from a host-side reference at spawn time. Exactly one of `source()` and `value()` must be set. The durable configuration stores only the reference, not the resolved plaintext.


```
use microsandbox::sandbox::{SecretBuilder, SecretSource};

let entry = SecretBuilder::new()
    .env("API_KEY")
    .source(SecretSource::Env { var: "API_KEY".into() })
    .allow("api.example.com")
    .build();
```


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-placeholder) secret. placeholder()


```
fn placeholder(self, placeholder: impl Into<String>) -> Self
```


Override the auto-generated placeholder string. By default microsandbox generates `$MSB_<env_var>`. Use this when you need a specific format or when the placeholder must match a particular byte length. Placeholders must be non-empty, at most 1024 bytes ([`MAX_SECRET_PLACEHOLDER_BYTES`](https://docs.microsandbox.dev/sdk/rust/secrets#secretconfigerror)), and cannot contain NUL, CR, or LF.


Parameters


`placeholder` impl Into<String> Custom placeholder string: non-empty, up to 1024 bytes, no NUL/CR/LF.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow) secret. allow()


```
fn allow(self, host: impl AsRef<str>) -> Self
```


Example


```
.secret(|s| s
    .env("STRIPE_KEY")
    .value(stripe_key)
    .allow("api.stripe.com")
    .allow("files.stripe.com"))
```


Add an exact host or wildcard pattern allowed to receive the real secret value. A `*.suffix` pattern matches the suffix itself and its subdomains. The proxy checks the host against the connection’s verified TLS identity and observed DNS history. Can be called multiple times to allow several hosts. At least one allowed host (exact, pattern, or any) is required.


Parameters


`host` impl AsRef<str> Exact hostname or wildcard pattern, e.g. `“api.example.com”` or `“*.example.com”`. Parsed as a [HostPattern](https://docs.microsandbox.dev/sdk/rust/secrets#hostpattern).


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow_any_host_dangerous) secret. allow_any_host_dangerous()


```
fn allow_any_host_dangerous(self, i_understand_the_risk: bool) -> Self
```


Allow substitution on **any** host. Every server the guest connects to can then receive the real secret, which effectively disables host-based protection. The call is a no-op unless `i_understand_the_risk` is `true`. Only use this when the secret is not sensitive or the sandbox network is fully locked down. Adds a [`HostPattern::Any`](https://docs.microsandbox.dev/sdk/rust/secrets#hostpattern) to the allow list, the one pattern that skips DNS and TLS-identity pinning.


Parameters


`i_understand_the_risk` bool Must be `true` to take effect.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow_placeholder_for) secret. allow_placeholder_for()


```
fn allow_placeholder_for(self, host: impl AsRef<str>) -> Self
```


Allow an exact host, wildcard pattern, or `*` to receive the placeholder unchanged when it cannot be substituted. Repeated calls are additive. The old `allow_passthrough_for()` name remains available as a deprecated alias. This does not grant access to the real value: substitution still requires an allowed host and an enabled request location.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-violation_action) secret. violation_action()


```
fn violation_action(self, action: SecretViolationAction) -> Self
```


Override the sandbox-wide blocking action for this secret. With no override, the network’s [`secret_violation_action()`](https://docs.microsandbox.dev/sdk/rust/networking#network-secret_violation_action) applies; its default is `SecretViolationAction::BlockAndLog`. Passthrough is a separate per-secret host policy.


Example


```
use microsandbox::{Sandbox, SecretViolationAction};

let sb = Sandbox::builder("worker")
    .image("python")
    .secret(|s| s
        .env("API_KEY")
        .value(api_key)
        .allow("api.github.com")
        .allow_placeholder_for("api.anthropic.com")
        .substitute_in_body(true)
        .violation_action(SecretViolationAction::BlockAndTerminate))
    .secret_violation_action(SecretViolationAction::BlockAndLog)
    .create()
    .await?;
```


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-require_tls_identity) secret. require_tls_identity()


```
fn require_tls_identity(self, enabled: bool) -> Self
```


When `true`, the secret is only substituted on TLS-intercepted connections where the proxy has verified it is performing MITM and the SNI matches an allowed host. Bypassed TLS is opaque and never receives substitution. Disable only when you know the traffic path is safe and explicitly supports non-TLS substitution. Default: `true`.


Parameters


`enabled` bool Require verified TLS identity. Default: `true`.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-substitute_in_headers) secret. substitute_in_headers()


```
fn substitute_in_headers(self, enabled: bool) -> Self
```


Control whether the placeholder is replaced anywhere in HTTP headers, including decoded and re-encoded Basic authentication credentials. This is the most common injection scope, covering `Authorization: Bearer $MSB_...` and similar patterns. Default: `true`.


Parameters


`enabled` bool Substitute in headers. Default: `true`.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-substitute_in_header_fields) secret. substitute_in_header_fields()


```
fn substitute_in_header_fields(fields: impl IntoIterator<Item = impl Into<String>>) -> Self
```


Enable header substitution but restrict it to the given header field names (matched case-insensitively), e.g. only `Authorization`. A placeholder found in any other header field is treated as a disabled location: on a verified allowed destination it is forwarded unchanged, while other destinations follow the violation policy. Passing an empty list restores the default of substituting in every header field. A non-empty list with header substitution disabled is rejected. Names must be valid HTTP field names.
Restricting this list matters for confidentiality, not just correctness: with every header substitutable, an untrusted guest can place the placeholder in a header the upstream host reflects back in its response and read the real secret from that response. Allow only the intended credential header.


Parameters


`fields` IntoIterator<Item = impl Into<String>> Header field names allowed to receive the substitution. Empty restores all headers.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-substitute_in_query) secret. substitute_in_query()


```
fn substitute_in_query(self, enabled: bool) -> Self
```


Control whether the placeholder is replaced in the URL query string (the `?key=value` portion of the request line). Default: `false`.


Parameters


`enabled` bool Substitute in query parameters. Default: `false`.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-substitute_in_body) secret. substitute_in_body()


```
fn substitute_in_body(self, enabled: bool) -> Self
```


Control whether the placeholder is replaced in HTTP/1 request bodies. When enabled, fixed-length bodies up to 16 MiB are substituted and their `Content-Length` updated; larger fixed-length bodies are blocked. Chunked bodies are decoded and re-encoded with fresh chunk sizes. Encoded bodies pass through unchanged. HTTP/2 DATA-frame substitution is not supported, so matching body placeholders are blocked rather than leaked. Default: `false`.


Parameters


`enabled` bool Substitute in request bodies. Default: `false`.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secret-build) secret. build()


```
fn build(self) -> SecretEntry
```


Materialize the [`SecretEntry`](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry). Called for you by [`SandboxBuilder::secret`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret), so you rarely call it directly. If [`placeholder`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-placeholder) was not set, it defaults to `$MSB_<env_var>`.


Returns


[SecretEntry](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) The materialized secret entry.


Panics


Panics if `env` was not set, if neither or both of `value` and `source` were set, or if the allow list is empty. Use [allow_any_host_dangerous(true)](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow_any_host_dangerous) for an explicit any-host secret.


## [​](https://docs.microsandbox.dev/sdk/rust/secrets#sandboxbuilder) SandboxBuilder


Two convenience methods on [`SandboxBuilder`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandboxbuilder) for the common cases, so you don’t have to spell out a [`SecretBuilder`](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder) closure. Both automatically enable TLS interception.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#sandbox-secret_env) sandbox. secret_env()


```
fn secret_env(
    self,
    env_var: impl Into<String>,
    value: impl Into<String>,
    allowed_host: impl Into<String>,
) -> Self
```


Example


```
let sb = Sandbox::builder("agent")
    .image("python")
    .secret_env("OPENAI_API_KEY", api_key, "api.openai.com")
    .create()
    .await?;
```


Equivalent to `.secret(|s| s.env(env_var).value(value).allow(allowed_host))`. The placeholder is auto-generated as `$MSB_<env_var>` and the default injection scopes apply (headers and Basic Auth enabled, query and body disabled).


Parameters


`env_var` impl Into<String> Environment variable name (non-empty, no `=` or NUL). `value` impl Into<String> Secret value. `allowed_host` impl Into<String> Allowed destination host (exact match).


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#sandbox-secret_entry) sandbox. secret_entry()


```
fn secret_entry(self, entry: SecretEntry) -> Self
```


Example


```
use microsandbox::sandbox::SecretBuilder;

let entry = SecretBuilder::new()
    .env("STRIPE_KEY")
    .value(stripe_key)
    .allow("api.stripe.com")
    .build();

let sb = Sandbox::builder("billing")
    .image("python")
    .secret_entry(entry)
    .create()
    .await?;
```


Add a pre-built [`SecretEntry`](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) directly. Use this escape hatch when you already have a materialized entry. For example, the entry can be produced by [`SecretBuilder::build()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-build), loaded from configuration, or constructed by hand for full control over the serialized shape. Both [`secret()`](https://docs.microsandbox.dev/sdk/rust/sandbox#sandbox-secret) and [`secret_env()`](https://docs.microsandbox.dev/sdk/rust/secrets#sandbox-secret_env) funnel through this method. The entry is validated when the sandbox is built; an invalid one surfaces as a config error rather than a panic.


Parameters


`entry` [SecretEntry](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) A materialized secret entry.


## [​](https://docs.microsandbox.dev/sdk/rust/secrets#hostpattern) HostPattern


Used by [SecretEntry](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) · [allow()](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow) · [allow_placeholder_for()](https://docs.microsandbox.dev/sdk/rust/secrets#secret-allow_placeholder_for)


Destination host pattern used by secret policies.


| Variant | Builder methods | Matches |
| --- | --- | --- |
| `Exact(String)` | `allow("api.example.com")`, `allow_placeholder_for("api.example.com")` | Exact hostname, ASCII case-insensitive |
| `Wildcard(String)` | `allow("*.example.com")`, `allow_placeholder_for("*.example.com")` | The suffix and its subdomains |
| `Any` | `allow_any_host_dangerous(true)`, `allow_placeholder_for("*")` | Every host |


Use the explicit dangerous opt-in for any-host substitution; `allow("*")` panics.


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#pattern-matches) pattern. matches()


```
fn matches(&self, hostname: &str) -> bool
```


Whether `hostname` matches this pattern (ASCII case-insensitive).


## [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) SecretEntry


returned by [SecretBuilder::build()](https://docs.microsandbox.dev/sdk/rust/secrets#secret-build) · used by [secret_entry()](https://docs.microsandbox.dev/sdk/rust/secrets#sandbox-secret_entry)


Materialized secret configuration produced by [`SecretBuilder`](https://docs.microsandbox.dev/sdk/rust/secrets#secretbuilder).


| Field | Type | Description |
| --- | --- | --- |
| `env_var` | `String` | Environment variable holding the placeholder. Non-empty, no `=` or NUL. |
| `value` | `Zeroizing<String>` | The real secret value; never enters the guest. Inline values are persisted; source-backed durable entries carry an empty value until host-side resolution. Debug output redacts the value. |
| `source` | `Option<SecretSource>` | Host-side reference resolved at spawn time. Prefer the builder’s [`source()`](https://docs.microsandbox.dev/sdk/rust/secrets#secret-source) method rather than populating a resolved entry manually. |
| `placeholder` | `String` | What the guest sees. Non-empty, at most 1024 bytes, no NUL/CR/LF. |
| `allowed_hosts` | `Vec<HostPattern>` | Hosts allowed to receive the real value. |
| `substitution` | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/rust/secrets#secretsubstitution) | Where in the request the value may be substituted. |
| `violation_action` | `Option<SecretViolationAction>` | Per-secret violation override. `None` falls back to the sandbox-wide action. |
| `passthrough_hosts` | `Vec<HostPattern>` | Destinations allowed to receive the unchanged placeholder. Empty by default. |
| `require_tls_identity` | `bool` | Require verified TLS identity before substituting. Default: `true`. |


#### [​](https://docs.microsandbox.dev/sdk/rust/secrets#entry-validate) entry. validate()


```
fn validate(&self, secret_index: usize) -> Result<(), SecretConfigError>
```


Validate this entry’s env var, allowed hosts, enabled substitution locations, and placeholder.


## [​](https://docs.microsandbox.dev/sdk/rust/secrets#types) Types


### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretsubstitution) SecretSubstitution


Used by [SecretEntry.substitution](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry)


Request locations enabled through the `substitute_in_*` methods. At least one must remain enabled. On credential-allowed hosts that pass the secret’s identity checks, disabled locations forward the placeholder unchanged. Other destinations must match the secret’s passthrough list or follow the violation action.


| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `headers` | `bool` | `true` | Substitute in headers, including Basic authentication. |
| `header_fields` | `Vec<String>` | `[]` (all) | When non-empty, restrict header substitution to these field names. |
| `query` | `bool` | `false` | Substitute in the URL query string. |
| `body` | `bool` | `false` | Substitute in supported HTTP/1 bodies. |


When body substitution is enabled, fixed-length HTTP/1 bodies up to 16 MiB update `Content-Length`; larger fixed-length bodies are blocked. Chunked HTTP/1 bodies are decoded and re-encoded with fresh chunk sizes. Encoded bodies pass through unchanged. HTTP/2 DATA-frame body substitution is unsupported, and matching body placeholders are blocked.


### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretviolationaction) SecretViolationAction


Used by [SecretEntry](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry) · [violation_action()](https://docs.microsandbox.dev/sdk/rust/secrets#secret-violation_action) · [NetworkBuilder::secret_violation_action()](https://docs.microsandbox.dev/sdk/rust/networking#network-secret_violation_action)


Blocking action when a placeholder cannot be substituted or passed through. A per-secret action overrides the network default. Passthrough is a host policy, not an enum variant.


| Variant | Description |
| --- | --- |
| `Block` | Block the request without logging. |
| `BlockAndLog` | Block and emit a warning on the host. This is the default. |
| `BlockAndTerminate` | Block, log an error, and shut down the sandbox. |


### [​](https://docs.microsandbox.dev/sdk/rust/secrets#secretconfigerror) SecretConfigError


returned by [SecretEntry::validate()](https://docs.microsandbox.dev/sdk/rust/secrets#secretentry)


Why a secret entry failed validation. Each variant carries the offending `secret_index`. The placeholder ceiling is the public constant `MAX_SECRET_PLACEHOLDER_BYTES = 1024`.


| Variant | Description |
| --- | --- |
| `EmptyEnvVar` | The environment variable name is empty. |
| `EnvVarContainsEquals` | The environment variable name contains `=`. |
| `EnvVarContainsNul` | The environment variable name contains NUL. |
| `MissingAllowedHosts` | No allowed hosts were configured. |
| `MissingSubstitutionLocation` | Headers, query, and body substitution were all disabled. |
| `EmptyPlaceholder` | The placeholder is empty. |
| `PlaceholderTooLong` | The placeholder exceeds `MAX_SECRET_PLACEHOLDER_BYTES` (carries `actual_bytes`, `max_bytes`). |
| `PlaceholderContainsNul` | The placeholder contains NUL. |
| `PlaceholderContainsLineBreak` | The placeholder contains CR or LF. |
## Documentation Index
## ​SecretBuilder
## ​SandboxBuilder
## ​HostPattern
*Used by SecretEntry · allow() · allow_placeholder_for()*

## ​SecretEntry
*returned by SecretBuilder::build() · used by secret_entry()*

## ​Types








Was this page helpful?

Yes No ⌘ I

---

# Python SDK Secrets reference

`https://docs.microsandbox.dev/sdk/python/secrets`

See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets) for usage examples and security boundaries.


## [​](https://docs.microsandbox.dev/sdk/python/secrets#secret) Secret


#### [​](https://docs.microsandbox.dev/sdk/python/secrets#secret-env) Secret. env()


```
@staticmethod
def env(
    env_var: str,
    *,
    value: str,
    allow: Sequence[str] = (),
    allow_placeholder_for: Sequence[str] = (),
    passthrough: Sequence[str] = (),  # deprecated alias
    placeholder: str | None = None,
    require_tls_identity: bool = True,
    violation_action: ViolationAction | None = None,
    substitution: SecretSubstitution | None = None,
) -> SecretEntry
```


Example


```
import os
from microsandbox import Sandbox, Secret, SecretSubstitution, ViolationAction

secret = Secret.env(
    "SERVICE_API_KEY",
    value=os.environ["SERVICE_API_KEY"],
    allow=["api.example.com", "*.example.com"],
    allow_placeholder_for=["api.anthropic.com"],
    violation_action=ViolationAction.BLOCK_AND_TERMINATE,
    substitution=SecretSubstitution(query=True),
)

sb = await Sandbox.create(
    "worker",
    image="python",
    secrets=[secret],
    secret_violation_action=ViolationAction.BLOCK_AND_LOG,
)
```


Create a secret entry that maps an environment variable to a real value. The guest sees a placeholder; the TLS proxy substitutes the real value only when traffic goes to an allowed host. Pass the returned entry to `Sandbox.create(..., secrets=[...])`.


Parameters


`env_var` str Environment variable name. Must be non-empty and cannot contain `=` or NUL; shell-identifier syntax is not required. `value` str The real secret value. Never enters the guest VM. Keyword-only and required. Raw values are persisted in the durable sandbox configuration. `allow` Sequence[str] Exact hosts or wildcard patterns allowed to receive the real value. At least one exact or wildcard host is required. Default `()`. `allow_placeholder_for` Sequence[str] Exact hosts or wildcard patterns allowed to receive the unchanged placeholder. Does not grant access to the real value. Default `()`. `placeholder` str | None Custom placeholder string: non-empty, up to 1024 bytes, no NUL/CR/LF. Auto-generated as `$MSB_<env_var>` when `None`. Default `None`. `require_tls_identity` bool Only substitute on TLS-intercepted connections. Disable only if you know the traffic is safe. Default `True`. `violation_action` [ViolationAction](https://docs.microsandbox.dev/sdk/python/secrets#violationaction) | None Per-secret blocking action. Default `None` inherits the network setting, whose default is `BLOCK_AND_LOG`. `substitution` [SecretSubstitution](https://docs.microsandbox.dev/sdk/python/secrets#secretsubstitution) | None Where in the HTTP request to substitute. `None` uses `SecretSubstitution()` defaults. Default `None`.


Returns


[SecretEntry](https://docs.microsandbox.dev/sdk/python/secrets#secretentry) Secret entry for `Sandbox.create(secrets=[…])`.


## [​](https://docs.microsandbox.dev/sdk/python/secrets#validation-and-lifecycle) Validation and lifecycle


Sandbox configuration validation rejects empty environment names, names containing `=` or NUL, missing allowed hosts, every substitution location disabled, and placeholders that are empty, longer than 1024 bytes, or contain NUL/CR/LF. `Secret.env()` constructs an entry; it does not itself run all native validation.
Raw values are persisted at rest. Prefer source references through [live modification](https://docs.microsandbox.dev/sandboxes/secrets#update-secrets) when the secret is available in the host environment. Rotating or removing an existing secret does not require a restart; adding a secret or changing its guest-visible placeholder does. Live modification is local-only.
`passthrough=` remains a deprecated alias for `allow_placeholder_for=` and emits a `DeprecationWarning` when used with hosts. If both are supplied, the host lists are combined. The returned `SecretEntry.passthrough` field and serialized configuration keep their existing names.


## [​](https://docs.microsandbox.dev/sdk/python/secrets#types) Types


### [​](https://docs.microsandbox.dev/sdk/python/secrets#secretentry) SecretEntry


Returned by [Secret.env()](https://docs.microsandbox.dev/sdk/python/secrets#secret-env)


A single secret entry, used in `Sandbox.create(secrets=[...])`. Construct it with [`Secret.env()`](https://docs.microsandbox.dev/sdk/python/secrets#secret-env) rather than directly.


| Field | Type | Default | Description |
| --- | --- | --- | --- |
| env_var | `str` | required | Environment variable name (non-empty, no `=` or NUL) |
| value | `str` | required | Secret value. Never enters the guest |
| allow | `tuple[str, ...]` | `()` | Exact or wildcard hosts allowed to receive the real value |
| passthrough | `tuple[str, ...]` | `()` | Exact or wildcard hosts allowed to receive the unchanged placeholder |
| placeholder | `str | None` | `None` | Placeholder string: non-empty, up to 1024 bytes, no NUL/CR/LF. Auto-generated as `$MSB_<env_var>` when `None` |
| require_tls_identity | `bool` | `True` | Only substitute on TLS-intercepted connections |
| violation_action | [`ViolationAction`](https://docs.microsandbox.dev/sdk/python/secrets#violationaction) `| None` | `None` | Per-secret override; inherits the sandbox-wide action when omitted |
| substitution | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/python/secrets#secretsubstitution) | `SecretSubstitution()` | Per-request substitution scopes |


### [​](https://docs.microsandbox.dev/sdk/python/secrets#secretsubstitution) SecretSubstitution


#### [​](https://docs.microsandbox.dev/sdk/python/secrets#substitution-headers) substitution. headers


```
headers: bool = True
```


Substitute in headers, including Basic authentication. Default: `True`.


#### [​](https://docs.microsandbox.dev/sdk/python/secrets#substitution-header_fields) substitution. header_fields


```
header_fields: tuple[str, ...] = ()
```


Restrict substitution to these header names. An empty list allows all headers. Requires header substitution to be enabled. Prefer only the intended credential header, such as `Authorization`, to prevent other headers from exposing a secret in a reflected response.


#### [​](https://docs.microsandbox.dev/sdk/python/secrets#substitution-query) substitution. query


```
query: bool = False
```


Substitute in the URL query string. Default: `False`.


#### [​](https://docs.microsandbox.dev/sdk/python/secrets#substitution-body) substitution. body


```
body: bool = False
```


Substitute in supported HTTP/1 bodies. Default: `False`. Fixed-length bodies up to 16 MiB update `Content-Length`; larger bodies are blocked. Chunked bodies are decoded and re-encoded. Encoded bodies pass through unchanged. HTTP/2 body substitution is unsupported, and matching placeholders are blocked.
At least one substitution location must remain enabled. On verified allowed hosts, disabled locations forward the placeholder unchanged. Other destinations must match the passthrough policy or follow the violation action.
This is a frozen dataclass. Defaults are omitted from serialized configuration; explicit `headers=False` is preserved. Assigning another type to `SecretEntry.substitution` raises `TypeError` when serialized.


### [​](https://docs.microsandbox.dev/sdk/python/secrets#violationaction) ViolationAction


Used by [Secret.env()](https://docs.microsandbox.dev/sdk/python/secrets#secret-env) · [SecretEntry.violation_action](https://docs.microsandbox.dev/sdk/python/secrets#secretentry)


String enum defining the blocking action when a placeholder cannot be substituted or passed through. Set the sandbox-wide default with `Network.secret_violation_action` or the top-level `Sandbox.create(secret_violation_action=...)`; the top-level value takes precedence if both are supplied. A secret’s `violation_action` overrides that default. Passthrough is a host policy, not an enum member.


| Member | Value | Description |
| --- | --- | --- |
| `ViolationAction.BLOCK` | `"block"` | Silently drop the request. The guest sees a connection reset. |
| `ViolationAction.BLOCK_AND_LOG` | `"block-and-log"` | Drop the request and emit a warning log on the host side. This is the default. |
| `ViolationAction.BLOCK_AND_TERMINATE` | `"block-and-terminate"` | Drop the request, log an error, and shut down the entire sandbox. |


### [​](https://docs.microsandbox.dev/sdk/python/secrets#secretviolationerror) SecretViolationError


Subclass of `MicrosandboxError`


Raised when a secret placeholder was sent to a disallowed host. Carries `code = "secret-violation"`.
## Documentation Index
## ​Secret
## ​Validation and lifecycle
## ​Types





Was this page helpful?

Yes No ⌘ I

---

# Go SDK Secrets reference

`https://docs.microsandbox.dev/sdk/go/secrets`

See [Secrets](https://docs.microsandbox.dev/sandboxes/secrets) for usage examples and security boundaries.


## [​](https://docs.microsandbox.dev/sdk/go/secrets#functions) Functions


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#withsecrets) WithSecrets()


```
func WithSecrets(secrets ...SecretEntry) SandboxOption
```


Example


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python:3.12"),
    m.WithSecrets(
        m.Secret.Env("STRIPE_KEY", os.Getenv("STRIPE_KEY"),
            m.SecretEnvOptions{Allow: []string{"api.stripe.com"}}),
        m.Secret.Env("OPENAI_API_KEY", os.Getenv("OPENAI_API_KEY"),
            m.SecretEnvOptions{Allow: []string{"*.openai.com"}}),
    ),
)
```


Append credential secrets to the sandbox. Each call appends, so multiple calls accumulate. Secrets never enter the VM; the network proxy substitutes them at the transport layer. Pass to [`CreateSandbox`](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox) alongside the other options.


Parameters


`secrets` […SecretEntry](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) Secret entries to attach, usually built with [Secret.Env](https://docs.microsandbox.dev/sdk/go/secrets#secret-env).


Returns


SandboxOption Functional option for [CreateSandbox](https://docs.microsandbox.dev/sdk/go/sandbox#m-createsandbox).


## [​](https://docs.microsandbox.dev/sdk/go/secrets#secret) Secret


The [`Secret`](https://docs.microsandbox.dev/sdk/go/secrets#secret-env) factory is a package-level value. Call its methods to build [`SecretEntry`](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) values without populating struct literals by hand.


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#secret-env) Secret. Env()


```
func (secretFactory) Env(envVar, value string, opts SecretEnvOptions) SecretEntry
```


Example


```
m.Secret.Env("STRIPE_KEY", os.Getenv("STRIPE_KEY"),
    m.SecretEnvOptions{
        Allow:               []string{"api.stripe.com", "*.stripe.com"},
        AllowPlaceholderFor: []string{"api.anthropic.com"},
        Substitution:        m.SecretSubstitution{Body: true},
        Placeholder:         "$MSB_STRIPE",
    },
)
```


Build a [`SecretEntry`](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) that maps an environment variable to a real value. The guest sees a placeholder; the real value is substituted by the TLS proxy only when traffic goes to an allowed host. Supply at least one exact or wildcard host in `Allow`; an empty allow-list is rejected when the sandbox configuration is validated.


Parameters


`envVar` string Environment variable name holding the placeholder inside the sandbox. Must be non-empty and cannot contain `=` or NUL; shell-identifier syntax is not required. `value` string The real secret value. Passed to the native host runtime, never exposed inside the guest. `opts` [SecretEnvOptions](https://docs.microsandbox.dev/sdk/go/secrets#secretenvoptionsstruct) Allowed hosts, placeholder override, TLS requirement, and violation action.


Returns


[SecretEntry](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) Pass to [WithSecrets](https://docs.microsandbox.dev/sdk/go/secrets#withsecrets).


## [​](https://docs.microsandbox.dev/sdk/go/secrets#validation-and-lifecycle) Validation and lifecycle


Sandbox configuration validation rejects invalid environment names (empty or containing `=` or NUL), an empty allow-list, all substitution locations disabled, and invalid placeholders. `Secret.Env()` constructs a value; errors surface when the configuration is validated.
Raw values are persisted in the durable sandbox configuration. See [source references and live modification](https://docs.microsandbox.dev/sandboxes/secrets#update-secrets) to rotate or remove secrets without restarting. Adding a secret or changing its guest-visible placeholder requires a restart. Live modification is local-only.


## [​](https://docs.microsandbox.dev/sdk/go/secrets#types) Types


### [​](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) SecretEntry struct


accepted by [WithSecrets()](https://docs.microsandbox.dev/sdk/go/secrets#withsecrets) · returned by [Secret.Env()](https://docs.microsandbox.dev/sdk/go/secrets#secret-env)


A single credential the network proxy substitutes at the transport layer. The value never reaches the guest VM. Usually produced by [`Secret.Env`](https://docs.microsandbox.dev/sdk/go/secrets#secret-env); exported for callers that prefer struct literals.


| Field | Type | Description |
| --- | --- | --- |
| `EnvVar` | `string` | Environment variable name holding the placeholder inside the sandbox. Must be non-empty and cannot contain `=` or NUL; shell-identifier syntax is not required |
| `Value` | `string` | Real secret value; stays on the host, including across the native FFI boundary |
| `Allow` | `[]string` | Exact hosts or wildcard patterns allowed to receive the real value |
| `Passthrough` | `[]string` | Exact hosts or wildcard patterns allowed to receive the unchanged placeholder |
| `Substitution` | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/go/secrets#secretsubstitutionstruct) | Enabled request locations; zero value enables headers only |
| `Placeholder` | `string` | Custom placeholder shown inside the sandbox in place of the secret. Auto-generated from `EnvVar` when empty. Custom values must be non-empty, at most 1024 bytes, and cannot contain NUL, CR, or LF |
| `RequireTLSIdentity` | `*bool` | Require a verified TLS identity before substituting. Defaults to `true` when `nil` |
| `ViolationAction` | [`ViolationAction`](https://docs.microsandbox.dev/sdk/go/secrets#violationactionstring-enum) | Override the sandbox-wide action when this secret is detected going to a disallowed host. This overrides the network default for this secret only |


### [​](https://docs.microsandbox.dev/sdk/go/secrets#secretenvoptionsstruct) SecretEnvOptions struct


accepted by [Secret.Env()](https://docs.microsandbox.dev/sdk/go/secrets#secret-env)


Tunes [`Secret.Env`](https://docs.microsandbox.dev/sdk/go/secrets#secret-env) beyond the required `envVar` and `value`.


| Field | Type | Description |
| --- | --- | --- |
| `Allow` | `[]string` | Exact hosts or wildcard patterns allowed to receive the real value |
| `AllowPlaceholderFor` | `[]string` | Hosts allowed to receive the unchanged placeholder where substitution does not apply |
| `Passthrough` | `[]string` | Deprecated alias; combined with `AllowPlaceholderFor` when both are supplied |
| `Substitution` | [`SecretSubstitution`](https://docs.microsandbox.dev/sdk/go/secrets#secretsubstitutionstruct) | Zero value enables headers only |
| `Placeholder` | `string` | Custom placeholder: non-empty, up to 1024 bytes, no NUL/CR/LF |
| `RequireTLSIdentity` | `*bool` | Require a verified TLS identity before substituting. Defaults to `true` when `nil` |
| `ViolationAction` | [`ViolationAction`](https://docs.microsandbox.dev/sdk/go/secrets#violationactionstring-enum) | Per-secret violation action |


### [​](https://docs.microsandbox.dev/sdk/go/secrets#secretsubstitutionstruct) SecretSubstitution struct


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#substitution-headers) substitution. Headers


```
Headers *bool
```


Substitute in headers, including Basic authentication. Default: `true` when `nil`; use a pointer to set `false`.


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#substitution-headerfields) substitution. HeaderFields


```
HeaderFields []string
```


Restrict substitution to these header names. An empty list allows all headers. Requires header substitution to be enabled. Prefer only the intended credential header, such as `Authorization`, to prevent other headers from exposing a secret in a reflected response.


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#substitution-query) substitution. Query


```
Query bool
```


Substitute in the URL query string. Default: `false`.


#### [​](https://docs.microsandbox.dev/sdk/go/secrets#substitution-body) substitution. Body


```
Body bool
```


Substitute in supported HTTP/1 bodies. Default: `false`. Fixed-length bodies up to 16 MiB update `Content-Length`; larger bodies are blocked. Chunked bodies are decoded and re-encoded. Encoded bodies pass through unchanged. HTTP/2 body substitution is unsupported, and matching placeholders are blocked.
At least one substitution location must remain enabled. On verified allowed hosts, disabled locations forward the placeholder unchanged. Other destinations must match the passthrough policy or follow the violation action.


Example


```
headers := false
secret := m.Secret.Env("GH_TOKEN", os.Getenv("GH_TOKEN"), m.SecretEnvOptions{
    Allow:               []string{"github.com", "api.github.com"},
    AllowPlaceholderFor: []string{"api.anthropic.com"},
    Substitution:        m.SecretSubstitution{Headers: &headers, Body: true},
    ViolationAction:     m.ViolationActionBlockAndTerminate,
})
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithSecrets(secret),
    m.WithNetwork(&m.NetworkConfig{
        SecretViolationAction: m.ViolationActionBlockAndLog,
    }),
)
```


### [​](https://docs.microsandbox.dev/sdk/go/secrets#violationactionstring-enum) ViolationAction string enum


field of [SecretEntry](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct) · [NetworkConfig](https://docs.microsandbox.dev/sdk/go/networking#networkconfig)


```
type ViolationAction string
```


What happens when a secret placeholder cannot be substituted or passed through. Passthrough is a separate per-secret host policy, not a violation action. Configure the sandbox-wide default on [`NetworkConfig.SecretViolationAction`](https://docs.microsandbox.dev/sdk/go/networking#networkconfig); override per-secret with [`SecretEntry.ViolationAction`](https://docs.microsandbox.dev/sdk/go/secrets#secretentrystruct).


| Constant | Value | Description |
| --- | --- | --- |
| `ViolationActionDefault` | `""` | Leave the runtime default in place (currently `block-and-log`) |
| `ViolationActionBlock` | `"block"` | Silently drop the request. The guest sees a connection reset |
| `ViolationActionBlockAndLog` | `"block-and-log"` | Drop the request and emit a warning log on the host side |
| `ViolationActionBlockAndTerminate` | `"block-and-terminate"` | Drop the request, log an error, and shut down the entire sandbox |
## Documentation Index
## ​Functions
## ​Secret
## ​Validation and lifecycle
## ​Types







Was this page helpful?

Yes No ⌘ I

---

# Images - microsandbox

`https://docs.microsandbox.dev/images/overview`

## [​](https://docs.microsandbox.dev/images/overview#oci-images) OCI images


microsandbox uses standard OCI container images as root filesystems. Docker Hub, GHCR, ECR, GCR, any OCI-compatible registry works. Existing images run as-is.
When you specify an image like `python`, microsandbox pulls the manifest, downloads the layers in parallel, and stacks them as a copy-on-write filesystem. Changes inside the sandbox don’t modify the base image. Two sandboxes using the same image share the same cached layers on disk.


### [​](https://docs.microsandbox.dev/images/overview#pull-policies) Pull policies


By default, microsandbox pulls an image only if it isn’t already cached. You can change this behavior.


| Policy | Behavior |
| --- | --- |
| `"if-missing"` | Pull only if not cached (default) |
| `"always"` | Always check the registry for updates |
| `"never"` | Use local cache only, fail if missing |


TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

await using sb = await Sandbox.builder("worker")
    .image("python")
    .pullPolicy("always")
    .create();
```


```
let sb = Sandbox::builder("worker")
    .image("python")
    .pull_policy(PullPolicy::Always)
    .create()
    .await?;
```


```
from microsandbox import PullPolicy, Sandbox

sb = await Sandbox.create("worker", image="python", pull_policy=PullPolicy.ALWAYS)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("python"),
    m.WithPullPolicy(m.PullPolicyAlways),
)
```


```
sb = Microsandbox::Sandbox.create("worker", image: "python", pull_policy: "always")
```


Once microsandbox resolves an image reference, it pins the exact layers. At first pull, `python` resolves to a specific set of immutable layers. Subsequent `start()` calls use the pinned layers without re-resolving the mutable tag, so your sandbox is reproducible even if the upstream tag moves.


### [​](https://docs.microsandbox.dev/images/overview#private-registries) Private registries


Authenticate to private registries by passing credentials.
TypeScript Rust Python Go

```
await using sb = await Sandbox.builder("worker")
    .image("registry.corp.io/team/app:latest")
    .registry((r) => r.auth({
        kind: "basic",
        username: "deploy",
        password: process.env.REGISTRY_TOKEN!,
    }))
    .pullPolicy("always")
    .create();
```


```
let sb = Sandbox::builder("worker")
    .image("registry.corp.io/team/app:latest")
    .registry(|r| r.auth(RegistryAuth::Basic {
        username: "deploy".into(),
        password: std::env::var("REGISTRY_PASSWORD")?,
    }))
    .pull_policy(PullPolicy::Always)
    .create()
    .await?;
```


```
import os
from microsandbox import PullPolicy, RegistryAuth, Sandbox

sb = await Sandbox.create(
    "worker",
    image="registry.corp.io/team/app:latest",
    registry_auth=RegistryAuth.basic("deploy", os.environ["REGISTRY_PASSWORD"]),
    pull_policy=PullPolicy.ALWAYS,
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("registry.corp.io/team/app:latest"),
    m.WithRegistryAuth(m.RegistryAuth{
        Username: "deploy",
        Password: os.Getenv("REGISTRY_PASSWORD"),
    }),
    m.WithPullPolicy(m.PullPolicyAlways),
)
```


### [​](https://docs.microsandbox.dev/images/overview#registry-tls) Registry TLS


Local-only
By default, microsandbox connects to registries over HTTPS using system CA roots. You can customize this per-registry in `~/.microsandbox/config.json`.


#### [​](https://docs.microsandbox.dev/images/overview#plain-http-registries) Plain HTTP registries


Local registries often run without TLS. Mark them as insecure to connect over plain HTTP:
JSON

```
{
  "registries": {
    "hosts": {
      "localhost:5050": {
        "insecure": true
      }
    }
  }
}
```


#### [​](https://docs.microsandbox.dev/images/overview#custom-ca-certificates) Custom CA certificates


For registries using self-signed or internal CA certificates, point `ca_certs` to a PEM file. This applies globally to all registry connections:
JSON

```
{
  "registries": {
    "ca_certs": "/path/to/ca-bundle.pem"
  }
}
```


microsandbox adds these certificates to the default system roots, so public registries continue to work normally. You can also supply the same roots per-sandbox through the SDK: `caCerts` in TypeScript, `ca_certs` in Rust, `registry_ca_certs` in Python, and `WithRegistryCACerts` / `WithRegistryCACertsPath` in Go.


#### [​](https://docs.microsandbox.dev/images/overview#combined-configuration) Combined configuration


JSON

```
{
  "registries": {
    "ca_certs": "/path/to/corporate-ca.pem",
    "hosts": {
      "localhost:5050": {
        "insecure": true,
        "auth": { "username": "deploy", "password_env": "REGISTRY_TOKEN" }
      },
      "ghcr.io": {
        "auth": { "username": "user", "store": "keyring" }
      }
    }
  }
}
```


Per-sandbox SDK options override user registry settings. [Managed registry settings](https://docs.microsandbox.dev/configuration#auth-resolution-order) take precedence over both. Managed `insecure: false` requires TLS without changing credentials; managed `auth: null` forces anonymous access, and managed CA settings replace per-call custom certificates.
TypeScript Rust Python Go

```
await using sb = await Sandbox.builder("worker")
    .image("localhost:5050/my-app:latest")
    .registry((r) => r.insecure())
    .create();
```


```
let sb = Sandbox::builder("worker")
    .image("localhost:5050/my-app:latest")
    .registry(|r| r.insecure())
    .create()
    .await?;
```


```
from microsandbox import Sandbox

sb = await Sandbox.create(
    "worker",
    image="localhost:5050/my-app:latest",
    registry_insecure=True,
)
```


```
sb, err := m.CreateSandbox(ctx, "worker",
    m.WithImage("localhost:5050/my-app:latest"),
    m.WithRegistryInsecure(),
)
```


### [​](https://docs.microsandbox.dev/images/overview#image-storage) Image storage


Local-only
Images are cached in the global microsandbox home directory:


| Path | Description |
| --- | --- |
| `~/.microsandbox/cache/layers/` | Materialized EROFS image layers |
| `~/.microsandbox/cache/fsmeta/` | Merged metadata images for cached manifests |
| `~/.microsandbox/cache/vmdk/` | VMDK descriptors used to boot cached images |
| `~/.microsandbox/db/` | Database tracking image metadata and digests |


Layers are content-addressable and deduplicated. If `python:3.12` and `python:3.11` share a base layer, it’s stored once.
Use `msb pull` from the CLI to pre-pull images before creating sandboxes. This avoids blocking on a download during `Sandbox.create`.
Use `msb image prune` to remove cached images that are not used by any sandbox or indexed snapshot and reclaim dangling image artifacts. Prune keeps images referenced by existing sandboxes or snapshots. It cleans up image metadata, unreachable manifests, orphaned layers, layer EROFS artifacts, fsmeta EROFS artifacts, and VMDK descriptor artifacts.
`msb load` accepts Docker image archives and OCI Image Layout archives. By default, `msb save` exports from the materialized EROFS cache as a Docker archive. Use `--format oci` to export as an OCI Image Layout archive instead. The expanded forms are `msb image load` and `msb image save`. The exported image should run the same way after `msb load`, but it is a regenerated archive: manifest digest and layer digests can differ from the original registry image.


## [​](https://docs.microsandbox.dev/images/overview#disk-images) Disk images


Local-only
In addition to OCI container images, microsandbox can boot a sandbox directly from a disk image file. The guest gets raw block device access, and its kernel mounts the filesystem from the device directly.
This is a fundamentally different path from OCI images. With OCI, microsandbox stacks image layers as a copy-on-write filesystem. With disk images, the guest owns the block device. No overlay, no copy-on-write between sandboxes.
Use disk images when you need a pre-built VM template, a custom kernel configuration, or an OS that isn’t available as a container image.


### [​](https://docs.microsandbox.dev/images/overview#supported-formats) Supported formats


| Format | Description |
| --- | --- |
| **QCOW2** | QEMU Copy-On-Write v2. Supports thin provisioning and backing files. The most common format. |
| **Raw** | Uncompressed raw disk image. No overhead, but no thin provisioning. |
| **VMDK** | VMware virtual disk format. |


### [​](https://docs.microsandbox.dev/images/overview#usage) Usage


When you pass a file path ending in `.qcow2`, `.raw`, or `.vmdk`, microsandbox auto-detects the format. For disk-image roots, rename ambiguous files with one of those extensions and set the filesystem type when auto-detection needs a hint.
TypeScript Rust Python Go Ruby

```
import { Sandbox } from "microsandbox";

// Auto-detect format from the file extension
await using sb = await Sandbox.builder("custom-vm")
    .image("./ubuntu-22.04.qcow2")
    .cpus(2)
    .memory(2048)
    .create();

// Explicit filesystem type via the ImageBuilder
await using sb2 = await Sandbox.builder("custom-vm")
    .imageWith((i) => i.disk("./alpine.raw").fstype("ext4"))
    .cpus(1)
    .memory(512)
    .create();
```


```
use microsandbox::size::SizeExt;

// Auto-detect
let sb = Sandbox::builder("custom-vm")
    .image("./ubuntu-22.04.qcow2")
    .cpus(2)
    .memory(2.gib())
    .create()
    .await?;

// Explicit filesystem type
let sb2 = Sandbox::builder("custom-vm")
    .image_with(|i| i.disk("./alpine.raw").fstype("ext4"))
    .cpus(1)
    .memory(512)
    .create()
    .await?;
```


```
from microsandbox import Image, Sandbox

# Auto-detect format from file extension
sb = await Sandbox.create("custom-vm", image="./ubuntu-22.04.qcow2", cpus=2, memory=2048)

# Explicit filesystem type
sb2 = await Sandbox.create("custom-vm", image=Image.disk("./alpine.raw", fstype="ext4"), cpus=1, memory=512)
```


```
// Auto-detect format from the file extension
sb, err := m.CreateSandbox(ctx, "custom-vm",
    m.WithImage("./ubuntu-22.04.qcow2"),
    m.WithCPUs(2),
    m.WithMemory(2048),
)

// Explicit filesystem type
sb2, err := m.CreateSandbox(ctx, "custom-vm-2",
    m.WithImageDisk("./alpine.raw", "ext4"),
    m.WithCPUs(1),
    m.WithMemory(512),
)
```


```
# Auto-detect the format from the file extension.
sb = Microsandbox::Sandbox.create(
  "custom-vm", image: "./ubuntu-22.04.qcow2", cpus: 2, memory: 2048
)
# Ruby accepts image paths but does not expose a filesystem-type override.
```


The filesystem type (`ext4`, `xfs`, etc.) must match what’s actually on the disk image. The guest kernel mounts it using the specified filesystem driver.


## [​](https://docs.microsandbox.dev/images/overview#reference) Reference


For exact image APIs, see [TypeScript](https://docs.microsandbox.dev/sdk/typescript/images), [Rust](https://docs.microsandbox.dev/sdk/rust/images), [Python](https://docs.microsandbox.dev/sdk/python/images), [Go](https://docs.microsandbox.dev/sdk/go/images), or [Ruby](https://docs.microsandbox.dev/sdk/ruby/images). For local image management, see [Image commands](https://docs.microsandbox.dev/cli/image-commands).
## Documentation Index
## ​OCI images
## ​Disk images
## ​Reference





Was this page helpful?

Yes No ⌘ I

---

# Filesystem - microsandbox

`https://docs.microsandbox.dev/sandboxes/filesystem`

# Filesystem
## Documentation Index
## ​Write a file
## ​Read a file
## ​List a directory
## ​Stream large files
## ​Copy from host
## ​Reference








Read and write files inside a running sandbox

The filesystem API lets you read, write, and manage files inside a sandbox without mounting volumes or SSH. It uses the same channel as command execution, so it doesn’t touch the sandbox’s network.
Handy for pushing generated code into a sandbox, pulling back results, or inspecting logs without having to pre-mount a shared directory.


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#write-a-file) Write a file


TypeScript Rust Python Go Ruby

```
await sb.fs().write("/app/config.json", '{"debug": true}');
```


```
sb.fs().write("/app/config.json", r#"{"debug": true}"#).await?;
```


```
await sb.fs.write("/app/config.json", b'{"debug": true}')
```


```
err := sb.FS().WriteString(ctx, "/app/config.json", `{"debug": true}`)
```


```
sb.fs.write("/app/config.json", '{"debug": true}')
```


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#read-a-file) Read a file


TypeScript Rust Python Go Ruby

```
const content = await sb.fs().readToString("/app/config.json");
```


```
let content = sb.fs().read_to_string("/app/config.json").await?;
```


```
content = await sb.fs.read_text("/app/config.json")
```


```
content, err := sb.FS().ReadString(ctx, "/app/config.json")
```


```
content = sb.fs.read("/app/config.json").force_encoding(Encoding::UTF_8)
```


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#list-a-directory) List a directory


TypeScript Rust Python Go Ruby

```
const entries = await sb.fs().list("/app");
for (const entry of entries) {
    console.log(`${entry.path}: ${entry.kind}`);
}
```


```
let entries = sb.fs().list("/app").await?;
for entry in entries {
    println!("{}: {:?}", entry.path, entry.kind);
}
```


```
entries = await sb.fs.list("/app")
for entry in entries:
    print(f"{entry.path}: {entry.kind}")
```


```
entries, err := sb.FS().List(ctx, "/app")
for _, entry := range entries {
    fmt.Printf("%s: %s\n", entry.Path, entry.Kind)
}
```


```
sb.fs.list("/app").each do |entry|
  puts "#{entry.fetch("path")}: #{entry.fetch("kind")}"
end
```


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#stream-large-files) Stream large files


For files too large to fit in memory, use streaming. Data is transferred in chunks of approximately 3 MiB each.
TypeScript Rust Python Go

```
const stream = await sb.fs().readStream("/app/data.bin");
for await (const chunk of stream) {
    processChunk(chunk); // chunk is a Uint8Array
}
```


```
let mut stream = sb.fs().read_stream("/app/data.bin").await?;
while let Some(chunk) = stream.recv().await? {
    process(&chunk);
}
```


```
stream = await sb.fs.read_stream("/app/data.bin")
async for chunk in stream:
    process(chunk)
```


```
stream, err := sb.FS().ReadStream(ctx, "/app/data.bin")
for {
    chunk, err := stream.Recv(ctx)
    if err != nil {
        return err
    }
    if chunk == nil {
        break
    }
    process(chunk)
}
```


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#copy-from-host) Copy from host


Copy a file from the host machine into the sandbox in a single call.
TypeScript Rust Python Go Ruby

```
await sb.fs().copyFromHost("./local-file.txt", "/app/remote-file.txt");
```


```
sb.fs().copy_from_host("./local-file.txt", "/app/remote-file.txt").await?;
```


```
await sb.fs.copy_from_host("./local-file.txt", "/app/remote-file.txt")
```


```
err := sb.FS().CopyFromHost(ctx, "./local-file.txt", "/app/remote-file.txt")
```


```
sb.fs.copy_from_host("./local-file.txt", "/app/remote-file.txt")
```


If you need to transfer many files at once, consider using a [bind-mounted volume](https://docs.microsandbox.dev/sandboxes/volumes) instead. Volumes give the guest direct filesystem access, whereas the filesystem API transfers each file individually. For bulk operations, volumes are significantly faster.


## [​](https://docs.microsandbox.dev/sandboxes/filesystem#reference) Reference


For exact filesystem APIs, see [TypeScript](https://docs.microsandbox.dev/sdk/typescript/filesystem), [Rust](https://docs.microsandbox.dev/sdk/rust/filesystem), [Python](https://docs.microsandbox.dev/sdk/python/filesystem), [Go](https://docs.microsandbox.dev/sdk/go/filesystem), or [Ruby](https://docs.microsandbox.dev/sdk/ruby/filesystem). For host-to-sandbox copies, see [`msb copy`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-copy).

Was this page helpful?

Yes No ⌘ I

---

# https://docs.microsandbox.dev/llms.txt

`https://docs.microsandbox.dev/llms.txt`

# microsandbox

> Easy, fast microVMs for untrusted workloads, on your machine or in the cloud

- [Introduction](https://docs.microsandbox.dev/getting-started/introduction.md): Easy, fast microVMs for untrusted workloads
- [Quickstart](https://docs.microsandbox.dev/getting-started/quickstart.md): Get a sandbox running in under 5 minutes.
- [Cloud](https://docs.microsandbox.dev/cloud/overview.md): Run the same sandboxes on hosted infrastructure with an API key
- [AI agents](https://docs.microsandbox.dev/getting-started/agents.md): Connect AI agents to isolated microsandbox machines
- [Overview](https://docs.microsandbox.dev/sandboxes/overview.md): What sandboxes are and how to configure them
- [Lifecycle](https://docs.microsandbox.dev/sandboxes/lifecycle.md): Create, start, stop, and manage sandbox state
- [Commands](https://docs.microsandbox.dev/sandboxes/commands.md): Execute commands, stream output, and interact with sandboxes
- [Filesystem](https://docs.microsandbox.dev/sandboxes/filesystem.md): Read and write files inside a running sandbox
- [Secrets](https://docs.microsandbox.dev/sandboxes/secrets.md): Let sandboxed code use credentials without receiving their values
- [Images](https://docs.microsandbox.dev/images/overview.md): Use OCI container images or boot from disk image files
- [Volumes](https://docs.microsandbox.dev/sandboxes/volumes.md): Persist and share data across sandboxes
- [SSH](https://docs.microsandbox.dev/sandboxes/ssh.md): Connect to sandboxes through SSH protocol sessions
- [Snapshots](https://docs.microsandbox.dev/sandboxes/snapshots.md): Save files or running workloads and restore them into new sandboxes
- [Live Modify](https://docs.microsandbox.dev/sandboxes/tuning.md): Resize a running sandbox and update its configuration without replacing it
- [Labels](https://docs.microsandbox.dev/sandboxes/labels.md): Organize sandboxes, act on them in bulk, and attribute metrics
- [Logs](https://docs.microsandbox.dev/sandboxes/logs.md): Capture, read, and diagnose sandbox output
- [Metrics](https://docs.microsandbox.dev/sandboxes/metrics.md): Monitor sandbox resource usage
- [Bootstrap](https://docs.microsandbox.dev/sandboxes/bootstrap.md): Prepare scripts, patches, and PID 1 before work starts
- [Overview](https://docs.microsandbox.dev/networking/overview.md): Control network access and isolation
- [TLS inspection](https://docs.microsandbox.dev/networking/tls.md): Inspect HTTPS traffic and manage certificate trust
- [DNS](https://docs.microsandbox.dev/networking/dns.md): Control how sandboxes resolve domain names
- [Proxies](https://docs.microsandbox.dev/networking/outbound-proxy.md): Route outbound sandbox traffic through an HTTP CONNECT or SOCKS proxy
- [Host sockets](https://docs.microsandbox.dev/networking/host-sockets.md): Connect a sandbox to a Unix socket or Windows named pipe
- [Local or cloud](https://docs.microsandbox.dev/operations/backends.md): Choose where CLI and SDK operations run
- [Configuration](https://docs.microsandbox.dev/operations/configuration.md): Understand how global defaults, sandbox YAML, CLI flags, SDK inputs, and managed settings determine sandbox configuration.
- [Observability](https://docs.microsandbox.dev/observability/msb-metrics.md): Export microsandbox metrics to an OpenTelemetry-compatible backend
- [Performance](https://docs.microsandbox.dev/sandboxes/optimization.md): Choose the settings that can improve local sandbox performance
- [Linux](https://docs.microsandbox.dev/troubleshooting/linux.md): Diagnose KVM, permissions, and host runtime setup on Linux
- [macOS](https://docs.microsandbox.dev/troubleshooting/macos.md): Diagnose Apple Silicon and local runtime setup on macOS
- [Windows](https://docs.microsandbox.dev/troubleshooting/windows.md): Diagnose Windows Hypervisor Platform, doctor checks, and terminal setup
- [Overview](https://docs.microsandbox.dev/sdk/overview.md): Install a microsandbox SDK, create your first microVM sandbox, and find API references for TypeScript, Rust, Python, Go, and Ruby.
- [Runtime setup](https://docs.microsandbox.dev/sdk/setup.md): Prepare a local runtime before creating your first sandbox.
- [Error handling](https://docs.microsandbox.dev/sdk/errors.md): Handle sandbox errors and clean up resources across the microsandbox SDKs.
- [Global configuration](https://docs.microsandbox.dev/configuration.md): Configure microsandbox defaults for the CLI and SDKs using the shared config.json file.
- [Sandbox](https://docs.microsandbox.dev/sdk/typescript/sandbox.md): Create and manage microVM sandboxes with the TypeScript SDK.
- [Execution](https://docs.microsandbox.dev/sdk/typescript/execution.md): Run sandbox commands and stream their output with the TypeScript SDK.
- [SSH](https://docs.microsandbox.dev/sdk/typescript/ssh.md): Open sandbox SSH sessions and transfer files over SFTP with the TypeScript SDK.
- [Filesystem](https://docs.microsandbox.dev/sdk/typescript/filesystem.md): Read, write, and stream sandbox files with the TypeScript SDK.
- [Volumes](https://docs.microsandbox.dev/sdk/typescript/volumes.md): Create and mount persistent sandbox volumes with the TypeScript SDK.
- [Networking](https://docs.microsandbox.dev/sdk/typescript/networking.md): Configure sandbox network policies with the TypeScript SDK.
- [Proxies](https://docs.microsandbox.dev/sdk/typescript/proxies.md): Route outbound sandbox connections through an HTTP CONNECT, SOCKS4, or SOCKS5 proxy with the TypeScript SDK.
- [VSock](https://docs.microsandbox.dev/sdk/typescript/vsock.md): Connect a sandbox to host Unix sockets or local Windows named pipes over virtio-vsock with the TypeScript SDK.
- [Secrets](https://docs.microsandbox.dev/sdk/typescript/secrets.md): Configure destination-bound sandbox credentials with the TypeScript SDK.
- [Snapshots](https://docs.microsandbox.dev/sdk/typescript/snapshots.md): Create snapshots, fork sandboxes, and restore snapshots with the TypeScript SDK.
- [Images](https://docs.microsandbox.dev/sdk/typescript/images.md): Inspect and manage the local OCI image cache with the TypeScript SDK.
- [Agent client](https://docs.microsandbox.dev/sdk/typescript/agent-client.md): Send requests to the sandbox guest agent with the TypeScript SDK.
- [Sandbox](https://docs.microsandbox.dev/sdk/rust/sandbox.md): Create and manage microVM sandboxes with the Rust SDK.
- [Configuration](https://docs.microsandbox.dev/sdk/rust/configuration.md): Read global settings and configure local backends with the Rust SDK.
- [Execution](https://docs.microsandbox.dev/sdk/rust/execution.md): Run sandbox commands and stream their output with the Rust SDK.
- [SSH](https://docs.microsandbox.dev/sdk/rust/ssh.md): Open sandbox SSH sessions and transfer files over SFTP with the Rust SDK.
- [Filesystem](https://docs.microsandbox.dev/sdk/rust/filesystem.md): Read, write, and stream sandbox files with the Rust SDK.
- [Volumes](https://docs.microsandbox.dev/sdk/rust/volumes.md): Create and mount persistent sandbox volumes with the Rust SDK.
- [Networking](https://docs.microsandbox.dev/sdk/rust/networking.md): Configure sandbox network policies with the Rust SDK.
- [Proxies](https://docs.microsandbox.dev/sdk/rust/proxies.md): Route outbound sandbox connections through an HTTP CONNECT, SOCKS4, or SOCKS5 proxy with the Rust SDK.
- [VSock](https://docs.microsandbox.dev/sdk/rust/vsock.md): Connect a sandbox to host Unix sockets or local Windows named pipes over virtio-vsock with the Rust SDK.
- [Secrets](https://docs.microsandbox.dev/sdk/rust/secrets.md): Configure destination-bound sandbox credentials with the Rust SDK.
- [Snapshots](https://docs.microsandbox.dev/sdk/rust/snapshots.md): Create snapshots, fork sandboxes, and restore snapshots with the Rust SDK.
- [Images](https://docs.microsandbox.dev/sdk/rust/images.md): Inspect and manage the local OCI image cache with the Rust SDK.
- [Agent client](https://docs.microsandbox.dev/sdk/rust/agent-client.md): Send requests to the sandbox guest agent with the Rust SDK.
- [Sandbox](https://docs.microsandbox.dev/sdk/python/sandbox.md): Create and manage microVM sandboxes with the Python SDK.
- [Execution](https://docs.microsandbox.dev/sdk/python/execution.md): Run sandbox commands and stream their output with the Python SDK.
- [SSH](https://docs.microsandbox.dev/sdk/python/ssh.md): Open sandbox SSH sessions and transfer files over SFTP with the Python SDK.
- [Filesystem](https://docs.microsandbox.dev/sdk/python/filesystem.md): Read, write, and stream sandbox files with the Python SDK.
- [Volumes](https://docs.microsandbox.dev/sdk/python/volumes.md): Create and mount persistent sandbox volumes with the Python SDK.
- [Networking](https://docs.microsandbox.dev/sdk/python/networking.md): Configure sandbox network policies with the Python SDK.
- [Proxies](https://docs.microsandbox.dev/sdk/python/proxies.md): Route outbound sandbox connections through an HTTP CONNECT, SOCKS4, or SOCKS5 proxy with the Python SDK.
- [VSock](https://docs.microsandbox.dev/sdk/python/vsock.md): Connect a sandbox to host Unix sockets or local Windows named pipes over virtio-vsock with the Python SDK.
- [Secrets](https://docs.microsandbox.dev/sdk/python/secrets.md): Configure destination-bound sandbox credentials with the Python SDK.
- [Snapshots](https://docs.microsandbox.dev/sdk/python/snapshots.md): Create snapshots, fork sandboxes, and restore snapshots with the Python SDK.
- [Images](https://docs.microsandbox.dev/sdk/python/images.md): Configure sandbox image sources and manage the local cache with the Python SDK.
- [Agent client](https://docs.microsandbox.dev/sdk/python/agent-client.md): Send requests to the sandbox guest agent with the Python SDK.
- [Sandbox](https://docs.microsandbox.dev/sdk/go/sandbox.md): Create and manage microVM sandboxes with the Go SDK.
- [Execution](https://docs.microsandbox.dev/sdk/go/execution.md): Run sandbox commands and stream their output with the Go SDK.
- [SSH](https://docs.microsandbox.dev/sdk/go/ssh.md): Open sandbox SSH sessions and transfer files over SFTP with the Go SDK.
- [Filesystem](https://docs.microsandbox.dev/sdk/go/filesystem.md): Read, write, and stream sandbox files with the Go SDK.
- [Volumes](https://docs.microsandbox.dev/sdk/go/volumes.md): Create and mount persistent sandbox volumes with the Go SDK.
- [Images](https://docs.microsandbox.dev/sdk/go/images.md): Inspect and manage the local OCI image cache with the Go SDK.
- [Networking](https://docs.microsandbox.dev/sdk/go/networking.md): Configure sandbox network policies with the Go SDK.
- [Proxies](https://docs.microsandbox.dev/sdk/go/proxies.md): Route outbound sandbox connections through an HTTP CONNECT, SOCKS4, or SOCKS5 proxy with the Go SDK.
- [VSock](https://docs.microsandbox.dev/sdk/go/vsock.md): Connect a sandbox to host Unix sockets or local Windows named pipes over virtio-vsock with the Go SDK.
- [Secrets](https://docs.microsandbox.dev/sdk/go/secrets.md): Configure destination-bound sandbox credentials with the Go SDK.
- [Snapshots](https://docs.microsandbox.dev/sdk/go/snapshots.md): Create snapshots, fork sandboxes, and restore snapshots with the Go SDK.
- [Agent client](https://docs.microsandbox.dev/sdk/go/agent-client.md): Send requests to the sandbox guest agent with the Go SDK.
- [Sandbox](https://docs.microsandbox.dev/sdk/ruby/sandbox.md): Create and manage microVM sandboxes with the Ruby SDK.
- [Configuration](https://docs.microsandbox.dev/sdk/ruby/configuration.md): Select a backend and configure the local runtime with the Ruby SDK.
- [Execution](https://docs.microsandbox.dev/sdk/ruby/execution.md): Run commands and collect output with the Ruby SDK.
- [SSH](https://docs.microsandbox.dev/sdk/ruby/ssh.md): Run SSH commands with the Ruby SDK.
- [Filesystem](https://docs.microsandbox.dev/sdk/ruby/filesystem.md): Read, write, and transfer guest files with the Ruby SDK.
- [Volumes](https://docs.microsandbox.dev/sdk/ruby/volumes.md): Create and manage named volumes with the Ruby SDK.
- [Networking](https://docs.microsandbox.dev/sdk/ruby/networking.md): Configure network access, proxies, and secret injection with the Ruby SDK.
- [VSock](https://docs.microsandbox.dev/sdk/ruby/vsock.md): Connect a sandbox to host Unix sockets or local Windows named pipes over virtio-vsock with the Ruby SDK.
- [Snapshots](https://docs.microsandbox.dev/sdk/ruby/snapshots.md): Capture and manage snapshots with the Ruby SDK.
- [Images](https://docs.microsandbox.dev/sdk/ruby/images.md): Inspect and manage cached images with the Ruby SDK.
- [CLI overview](https://docs.microsandbox.dev/cli/overview.md): Install the microsandbox CLI and manage local or cloud microVM sandboxes from your terminal.
- [Configuration](https://docs.microsandbox.dev/cli/configuration.md): Configure sandbox resources, networking, and storage with reusable microsandbox CLI YAML files.
- [Sandbox commands](https://docs.microsandbox.dev/cli/sandbox-commands.md): Create, run, connect to, and remove microVM sandboxes with the microsandbox CLI.
- [Snapshot commands](https://docs.microsandbox.dev/cli/snapshot-commands.md): Capture, inspect, restore, and transfer sandbox snapshots with the microsandbox CLI.
- [SSH commands](https://docs.microsandbox.dev/cli/ssh-commands.md): Connect to running sandboxes and serve SSH endpoints with the microsandbox CLI.
- [Volume commands](https://docs.microsandbox.dev/cli/volume-commands.md): Create, mount, and manage persistent sandbox volumes with the microsandbox CLI.
- [Storage commands](https://docs.microsandbox.dev/cli/storage-commands.md): Check local storage usage and clean up unused memory files.
- [Image commands](https://docs.microsandbox.dev/cli/image-commands.md): Pull, inspect, and manage cached OCI images with the microsandbox CLI.
- [Registry commands](https://docs.microsandbox.dev/cli/registry-commands.md): Manage container registry credentials for local OCI image pulls with the microsandbox CLI.
- [CLI management](https://docs.microsandbox.dev/cli/management.md): Inspect the active backend, diagnose runtime setup, and manage the microsandbox CLI installation.
- [Overview](https://docs.microsandbox.dev/api-reference/overview.md): Authenticate cloud REST API requests with API keys or personal tokens, and handle errors and pagination.
- [List sandboxes](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/list-sandboxes.md): List the organization's sandboxes with cursor pagination and optional label filtering.
- [Create a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/create-a-sandbox.md): Create a sandbox, optionally start it immediately, and optionally wait until it is ready.
- [Get a sandbox by name](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/get-a-sandbox-by-name.md): Retrieve one sandbox by its organization-scoped name.
- [Delete a sandbox by name](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/delete-a-sandbox-by-name.md): Delete a sandbox selected by its organization-scoped name. Resource cleanup continues asynchronously.
- [Start a sandbox by name](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/start-a-sandbox-by-name.md): Start a sandbox selected by its organization-scoped name.
- [Stop a sandbox by name](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/stop-a-sandbox-by-name.md): Stop a running sandbox selected by its organization-scoped name.
- [Get a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/get-a-sandbox.md): Retrieve one sandbox by its unique identifier.
- [Delete a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/delete-a-sandbox.md): Delete a sandbox. Resource cleanup continues asynchronously.
- [Update a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/update-a-sandbox.md): Rename a sandbox by updating its display name or slug.
- [Get sandbox metrics](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/get-sandbox-metrics.md)
- [Start a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/start-a-sandbox.md): Start a sandbox and optionally wait until it is running.
- [Stop a sandbox](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/stop-a-sandbox.md): Stop a running sandbox.
- [List mounted volumes](https://docs.microsandbox.dev/api-reference/endpoints/sandboxes/list-mounted-volumes.md)
- [List snapshot candidates](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/list-snapshot-candidates.md): List persistent, stopped sandboxes supported by the current disk snapshot policy.
- [List snapshot operations](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/list-snapshot-operations.md): List asynchronous snapshot operations requested by this organization.
- [Get a snapshot operation](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/get-a-snapshot-operation.md): Poll an asynchronous snapshot operation.
- [List snapshots](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/list-snapshots.md): List the organization's managed disk snapshots.
- [Create a snapshot](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/create-a-snapshot.md): Create a managed or host-volume disk snapshot asynchronously.
- [Get a snapshot by name](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/get-a-snapshot-by-name.md): Retrieve a managed disk snapshot by its organization-unique name.
- [Delete a snapshot by name](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/delete-a-snapshot-by-name.md): Delete a managed disk snapshot by its organization-unique name.
- [Get a snapshot](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/get-a-snapshot.md): Retrieve a managed disk snapshot by its immutable identifier.
- [Delete a snapshot](https://docs.microsandbox.dev/api-reference/endpoints/snapshots/delete-a-snapshot.md): Delete a managed disk snapshot by its immutable identifier.
- [List volumes](https://docs.microsandbox.dev/api-reference/endpoints/volumes/list-volumes.md): List persistent volumes available to the organization, including current usage.
- [Create a volume](https://docs.microsandbox.dev/api-reference/endpoints/volumes/create-a-volume.md): Create a named persistent volume with optional capacity and labels.
- [Get the default volume](https://docs.microsandbox.dev/api-reference/endpoints/volumes/get-the-default-volume.md)
- [Delete a volume](https://docs.microsandbox.dev/api-reference/endpoints/volumes/delete-a-volume.md): Schedule an unused named volume for deletion.
- [Update a volume](https://docs.microsandbox.dev/api-reference/endpoints/volumes/update-a-volume.md): Update a named volume's capacity limit or labels.
- [List directory contents](https://docs.microsandbox.dev/api-reference/endpoints/volumes/list-directory-contents.md)
- [Delete a file or directory](https://docs.microsandbox.dev/api-reference/endpoints/volumes/delete-a-file-or-directory.md)
- [Read a file](https://docs.microsandbox.dev/api-reference/endpoints/volumes/read-a-file.md)
- [Write a file](https://docs.microsandbox.dev/api-reference/endpoints/volumes/write-a-file.md)
- [Copy a file or directory](https://docs.microsandbox.dev/api-reference/endpoints/volumes/copy-a-file-or-directory.md)
- [Check if a file exists](https://docs.microsandbox.dev/api-reference/endpoints/volumes/check-if-a-file-exists.md)
- [Create a directory](https://docs.microsandbox.dev/api-reference/endpoints/volumes/create-a-directory.md)
- [Move a file or directory](https://docs.microsandbox.dev/api-reference/endpoints/volumes/move-a-file-or-directory.md)
- [Get file details](https://docs.microsandbox.dev/api-reference/endpoints/volumes/get-file-details.md)
- [Get volume metrics](https://docs.microsandbox.dev/api-reference/endpoints/volumes/get-volume-metrics.md)
- [Get quota usage](https://docs.microsandbox.dev/api-reference/endpoints/quotas/get-quota-usage.md): Return current resource usage, plan limits, and organization-specific quota overrides.
- [Get billing summary](https://docs.microsandbox.dev/api-reference/endpoints/billing/get-billing-summary.md)
- [List invoices](https://docs.microsandbox.dev/api-reference/endpoints/billing/list-invoices.md)
- [Get an invoice](https://docs.microsandbox.dev/api-reference/endpoints/billing/get-an-invoice.md)
- [List billing plans](https://docs.microsandbox.dev/api-reference/endpoints/billing/list-billing-plans.md)
- [Get a usage summary](https://docs.microsandbox.dev/api-reference/endpoints/billing/get-a-usage-summary.md): Return billable usage for the organization.
- [Get per-sandbox usage](https://docs.microsandbox.dev/api-reference/endpoints/billing/get-per-sandbox-usage.md): Return billable usage grouped by sandbox for a selected UTC time range.
- [Get per-volume storage usage](https://docs.microsandbox.dev/api-reference/endpoints/billing/get-per-volume-storage-usage.md): Return persistent storage usage grouped by volume for a selected UTC time range.
- [List audit events](https://docs.microsandbox.dev/api-reference/endpoints/audit-events/list-audit-events.md): List audit events for the organization with cursor pagination and optional filters.
- [Get an audit event](https://docs.microsandbox.dev/api-reference/endpoints/audit-events/get-an-audit-event.md): Retrieve one audit event by its identifier.
- [Get the current organization](https://docs.microsandbox.dev/api-reference/endpoints/organization/get-the-current-organization.md): Returns the organization associated with the current credential.
- [List organization members](https://docs.microsandbox.dev/api-reference/endpoints/members/list-organization-members.md): List organization members and their roles with cursor pagination.
- [Get your profile](https://docs.microsandbox.dev/api-reference/personal/account/get-your-profile.md)
- [Delete your account](https://docs.microsandbox.dev/api-reference/personal/account/delete-your-account.md): Deletes the account's personal information, signs out active sessions, removes organization memberships, and revokes pending invitations sent by the user. Audit history is retained.
- [Update your profile](https://docs.microsandbox.dev/api-reference/personal/account/update-your-profile.md)
- [List your organizations](https://docs.microsandbox.dev/api-reference/personal/organization/list-your-organizations.md)
- [Create an organization](https://docs.microsandbox.dev/api-reference/personal/organization/create-an-organization.md): The current user becomes its owner.
- [Get an organization](https://docs.microsandbox.dev/api-reference/personal/organization/get-an-organization.md)
- [Delete an organization](https://docs.microsandbox.dev/api-reference/personal/organization/delete-an-organization.md): Hides the organization immediately and schedules its resources for cleanup. The request must confirm the organization slug.
- [Update an organization](https://docs.microsandbox.dev/api-reference/personal/organization/update-an-organization.md)
- [List organization members](https://docs.microsandbox.dev/api-reference/personal/members/list-organization-members.md)
- [Remove a member](https://docs.microsandbox.dev/api-reference/personal/members/remove-a-member.md)
- [Change a member's role](https://docs.microsandbox.dev/api-reference/personal/members/change-a-members-role.md)
- [Accept an invite](https://docs.microsandbox.dev/api-reference/personal/invites/accept-an-invite.md)
- [Decline an invite](https://docs.microsandbox.dev/api-reference/personal/invites/decline-an-invite.md)
- [List pending invites](https://docs.microsandbox.dev/api-reference/personal/invites/list-pending-invites.md)
- [Invite a member](https://docs.microsandbox.dev/api-reference/personal/invites/invite-a-member.md)
- [Cancel an invite](https://docs.microsandbox.dev/api-reference/personal/invites/cancel-an-invite.md)
- [Get organization SSO settings](https://docs.microsandbox.dev/api-reference/personal/oidc/get-organization-sso-settings.md)
- [Configure organization SSO](https://docs.microsandbox.dev/api-reference/personal/oidc/configure-organization-sso.md)
- [Remove organization SSO settings](https://docs.microsandbox.dev/api-reference/personal/oidc/remove-organization-sso-settings.md)
- [List API keys](https://docs.microsandbox.dev/api-reference/personal/credentials/list-api-keys.md): Admins and owners see all keys. Members see only their own keys.
- [List personal tokens](https://docs.microsandbox.dev/api-reference/personal/credentials/list-personal-tokens.md): Returns metadata without token values.
- [Revoke a personal token](https://docs.microsandbox.dev/api-reference/personal/credentials/revoke-a-personal-token.md): Returns not found when the token is missing or already revoked.
- [List registry credentials](https://docs.microsandbox.dev/api-reference/personal/registry-credentials/list-registry-credentials.md): Returns credential metadata without secret values.
- [Create or update a registry credential](https://docs.microsandbox.dev/api-reference/personal/registry-credentials/create-or-update-a-registry-credential.md): Each registry host can have one stored credential.
- [Delete a registry credential](https://docs.microsandbox.dev/api-reference/personal/registry-credentials/delete-a-registry-credential.md)
- [Check sandbox name availability](https://docs.microsandbox.dev/api-reference/personal/sandboxes/check-sandbox-name-availability.md): Check whether the sandbox slug is valid and available.
- [Suggest a sandbox name](https://docs.microsandbox.dev/api-reference/personal/sandboxes/suggest-a-sandbox-name.md): Generate an available sandbox slug.
- [List sandboxes](https://docs.microsandbox.dev/api-reference/personal/sandboxes/list-sandboxes.md)
- [Create a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/create-a-sandbox.md): By default, the sandbox is created without starting. Use `start=true` to start it immediately and `wait_for=running` to wait until it is ready.
- [Get a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/get-a-sandbox.md)
- [Delete a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/delete-a-sandbox.md): Resource cleanup continues asynchronously.
- [Update a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/update-a-sandbox.md)
- [Get sandbox metrics](https://docs.microsandbox.dev/api-reference/personal/sandboxes/get-sandbox-metrics.md): Returns CPU, memory, disk, and network metrics for a time range.
- [Start a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/start-a-sandbox.md)
- [Stop a sandbox](https://docs.microsandbox.dev/api-reference/personal/sandboxes/stop-a-sandbox.md)
- [List mounted volumes](https://docs.microsandbox.dev/api-reference/personal/sandboxes/list-mounted-volumes.md)
- [List sandboxes available for snapshots](https://docs.microsandbox.dev/api-reference/personal/snapshots/list-sandboxes-available-for-snapshots.md)
- [List snapshot operations](https://docs.microsandbox.dev/api-reference/personal/snapshots/list-snapshot-operations.md)
- [Get a snapshot operation](https://docs.microsandbox.dev/api-reference/personal/snapshots/get-a-snapshot-operation.md)
- [List snapshots](https://docs.microsandbox.dev/api-reference/personal/snapshots/list-snapshots.md)
- [Create a snapshot](https://docs.microsandbox.dev/api-reference/personal/snapshots/create-a-snapshot.md)
- [Get a snapshot by name](https://docs.microsandbox.dev/api-reference/personal/snapshots/get-a-snapshot-by-name.md)
- [Delete a snapshot by name](https://docs.microsandbox.dev/api-reference/personal/snapshots/delete-a-snapshot-by-name.md)
- [Get a snapshot by ID](https://docs.microsandbox.dev/api-reference/personal/snapshots/get-a-snapshot-by-id.md)
- [Delete a snapshot by ID](https://docs.microsandbox.dev/api-reference/personal/snapshots/delete-a-snapshot-by-id.md)
- [List volumes](https://docs.microsandbox.dev/api-reference/personal/volumes/list-volumes.md)
- [Create a volume](https://docs.microsandbox.dev/api-reference/personal/volumes/create-a-volume.md)
- [Get the default volume](https://docs.microsandbox.dev/api-reference/personal/volumes/get-the-default-volume.md)
- [Delete a volume](https://docs.microsandbox.dev/api-reference/personal/volumes/delete-a-volume.md)
- [Update a volume](https://docs.microsandbox.dev/api-reference/personal/volumes/update-a-volume.md)
- [List directory contents](https://docs.microsandbox.dev/api-reference/personal/volumes/list-directory-contents.md)
- [Delete a file or directory](https://docs.microsandbox.dev/api-reference/personal/volumes/delete-a-file-or-directory.md)
- [Read a file](https://docs.microsandbox.dev/api-reference/personal/volumes/read-a-file.md)
- [Write a file](https://docs.microsandbox.dev/api-reference/personal/volumes/write-a-file.md)
- [Copy a file or directory](https://docs.microsandbox.dev/api-reference/personal/volumes/copy-a-file-or-directory.md)
- [Check if a file exists](https://docs.microsandbox.dev/api-reference/personal/volumes/check-if-a-file-exists.md)
- [Check if files exist](https://docs.microsandbox.dev/api-reference/personal/volumes/check-if-files-exist.md)
- [Create a directory](https://docs.microsandbox.dev/api-reference/personal/volumes/create-a-directory.md)
- [Move a file or directory](https://docs.microsandbox.dev/api-reference/personal/volumes/move-a-file-or-directory.md)
- [Get file details](https://docs.microsandbox.dev/api-reference/personal/volumes/get-file-details.md)
- [Get volume metrics](https://docs.microsandbox.dev/api-reference/personal/volumes/get-volume-metrics.md)
- [Get quota usage](https://docs.microsandbox.dev/api-reference/personal/quotas/get-quota-usage.md)
- [Get billing summary](https://docs.microsandbox.dev/api-reference/personal/billing/get-billing-summary.md)
- [Cancel the subscription](https://docs.microsandbox.dev/api-reference/personal/billing/cancel-the-subscription.md): Cancellation takes effect at the end of the billing period.
- [List invoices](https://docs.microsandbox.dev/api-reference/personal/billing/list-invoices.md)
- [Get an invoice](https://docs.microsandbox.dev/api-reference/personal/billing/get-an-invoice.md)
- [Open the payment portal](https://docs.microsandbox.dev/api-reference/personal/billing/open-the-payment-portal.md): Returns a URL for managing payment methods.
- [Change the billing plan](https://docs.microsandbox.dev/api-reference/personal/billing/change-the-billing-plan.md)
- [List billing plans](https://docs.microsandbox.dev/api-reference/personal/billing/list-billing-plans.md)
- [Get estimated usage costs](https://docs.microsandbox.dev/api-reference/personal/billing/get-estimated-usage-costs.md): Includes the subscription and estimated overage for the current period.
- [Get sandbox usage](https://docs.microsandbox.dev/api-reference/personal/billing/get-sandbox-usage.md): Groups compute usage by sandbox and day for the requested time range.
- [Get storage usage](https://docs.microsandbox.dev/api-reference/personal/billing/get-storage-usage.md): Groups persistent storage usage by volume and day for the requested time range.
- [List audit events](https://docs.microsandbox.dev/api-reference/personal/audit-events/list-audit-events.md): Returns customer-visible audit events with optional filters.
- [Get an audit event](https://docs.microsandbox.dev/api-reference/personal/audit-events/get-an-audit-event.md)
- [How-to guides](https://docs.microsandbox.dev/how-to/overview.md): Practical steps for running your tools and workloads in microsandbox
- [Claude Code](https://docs.microsandbox.dev/how-to/agents/claude-code.md): Run Anthropic's Claude Code against a project on your host
- [Codex CLI](https://docs.microsandbox.dev/how-to/agents/codex.md): Run OpenAI Codex CLI against a project on your host
- [OpenCode](https://docs.microsandbox.dev/how-to/agents/opencode.md): Run the OpenCode terminal agent against a project on your host
- [OpenClaw](https://docs.microsandbox.dev/how-to/agents/openclaw.md): Onboard OpenClaw and run its persistent gateway inside a microVM
- [Goose](https://docs.microsandbox.dev/how-to/agents/goose.md): Run the native Goose coding agent against a project on your host
- [Gemini CLI](https://docs.microsandbox.dev/how-to/agents/gemini-cli.md): Run Google's Gemini CLI against a project on your host
- [Hermes Agent](https://docs.microsandbox.dev/how-to/agents/hermes-agent.md): Set up Hermes Agent from its official image and persist its state
- [Pi coding agent](https://docs.microsandbox.dev/how-to/agents/pi.md): Run the Pi terminal coding agent against a project on your host
- [Using with VS Code](https://docs.microsandbox.dev/how-to/development/vscode.md): Edit files and run tools in a sandbox with VS Code Remote-SSH
- [Use JetBrains with a sandboxed agent](https://docs.microsandbox.dev/how-to/development/jetbrains-acp.md): Run OpenCode in a sandbox and chat with it from your JetBrains IDE
- [code-server](https://docs.microsandbox.dev/how-to/development/code-server.md): Open an isolated VS Code workspace in the browser
- [JupyterLab](https://docs.microsandbox.dev/how-to/development/jupyterlab.md): Run token-authenticated notebooks in an isolated Python environment
- [VNC desktop](https://docs.microsandbox.dev/how-to/development/vnc-desktop.md): Open a modern CPU-only Linux desktop in the browser with LXQt, TigerVNC, and noVNC
- [Run a browser agent](https://docs.microsandbox.dev/how-to/browser-automation/browser-use.md): Run an AI browser agent with isolated Chromium inside a microVM
- [Automate a browser](https://docs.microsandbox.dev/how-to/browser-automation/playwright.md): Capture pages or expose a remote browser server without a GPU
- [Transcode media with FFmpeg](https://docs.microsandbox.dev/how-to/file-processing/ffmpeg.md): Prepare FFmpeg once and process untrusted media in an offline worker
- [Convert documents and render PDFs](https://docs.microsandbox.dev/how-to/file-processing/libreoffice-pdf.md): Prepare LibreOffice once, then convert untrusted documents without network access
- [Vet a Terraform provider offline](https://docs.microsandbox.dev/how-to/plugins/terraform.md): Download a provider once, then validate and plan without network access
- [Rehearse a database migration](https://docs.microsandbox.dev/how-to/data/migration-rehearsal.md): Snapshot PostgreSQL, apply a risky migration, and restore the baseline
- [Crawl a site with Scrapy](https://docs.microsandbox.dev/how-to/web-automation/scrapy.md): Run a bounded crawler with a single-site network allowlist
- [Fan out isolated batch jobs](https://docs.microsandbox.dev/how-to/automation/parallel-batch-jobs.md): Run independent inputs in parallel microVMs and collect their output
- [Run Docker in a sandbox](https://docs.microsandbox.dev/how-to/docker/docker-in-sandbox.md): Start dockerd inside a microsandbox VM and run containers from an interactive shell
- [Use local images](https://docs.microsandbox.dev/how-to/docker/local-images.md): Use locally built Docker images with microsandbox
- [Booting under systemd](https://docs.microsandbox.dev/how-to/guest/systemd-services.md): Hand PID 1 to systemd inside the guest so services run under a real init
- [Start warm workers from a snapshot](https://docs.microsandbox.dev/how-to/sandboxing/warm-workers.md): Install a toolchain once and launch clean workers from the captured disk state
- [Run microsandbox in Docker](https://docs.microsandbox.dev/how-to/docker/docker.md): Run the microsandbox CLI from a Linux container with KVM access
- [Run microsandbox in Kubernetes](https://docs.microsandbox.dev/how-to/sandboxing/kubernetes.md): Run local microVM sandboxes with shared files inside a Kubernetes pod
- [PostgreSQL](https://docs.microsandbox.dev/how-to/data/postgresql.md): Run a persistent PostgreSQL service with a localhost-only forwarded port
- [Redis](https://docs.microsandbox.dev/how-to/data/redis.md): Run an authenticated Redis service with persistent data
- [Mount S3 with JuiceFS](https://docs.microsandbox.dev/how-to/data/juicefs-s3.md): Mount an S3-backed JuiceFS filesystem and verify persistent file operations inside a sandbox
- [Run GitHub Actions in a microVM](https://docs.microsandbox.dev/how-to/ci-cd/github-actions-runner.md): Give one self-hosted job a disposable runner
- [Run isolated PR checks](https://docs.microsandbox.dev/how-to/ci-cd/pr-checks.md): Stream a commit into a bounded microVM and run its tests there
- [Run Docker Compose integration tests](https://docs.microsandbox.dev/how-to/ci-cd/compose-tests.md): Run a Compose stack without exposing the host Docker socket
- [Create an ephemeral preview deploy](https://docs.microsandbox.dev/how-to/ci-cd/preview-deploys.md): Serve a built site from a time-limited microVM
- [Schedule dependency audits](https://docs.microsandbox.dev/how-to/automation/dependency-audits.md): Run npm audit in a short-lived sandbox and copy out the report
- [Grafana Cloud](https://docs.microsandbox.dev/how-to/metrics-backends/grafana-cloud.md): Ship msb-metrics output to Grafana Cloud's OTLP gateway
- [Grafana Alloy](https://docs.microsandbox.dev/how-to/metrics-backends/grafana-alloy.md): Forward msb-metrics output to Grafana Cloud (or anywhere) via local Alloy
- [otel-collector](https://docs.microsandbox.dev/how-to/metrics-backends/otel-collector.md): Inspect msb-metrics output locally with the OpenTelemetry Collector
- [Prometheus](https://docs.microsandbox.dev/how-to/metrics-backends/prometheus.md): Ship msb-metrics output directly to Prometheus's OTLP ingestion endpoint
- [Datadog](https://docs.microsandbox.dev/how-to/metrics-backends/datadog.md): Ship msb-metrics output to Datadog via the Datadog Agent's OTLP receiver
- [Enterprise deployment](https://docs.microsandbox.dev/enterprise.md): Choose a deployment approach for employee devices or your own infrastructure
- [Prepare your environment](https://docs.microsandbox.dev/enterprise/prepare-environment.md): Prepare and test one local installation before deploying to the team
- [Configure company networking](https://docs.microsandbox.dev/enterprise/corporate-networking.md): Use company routing, DNS, certificates, and registries with local sandboxes
- [Enforce team settings](https://docs.microsandbox.dev/enterprise/managed-configuration.md): Define the settings your team must use and protect them on employee devices
- [Deploy and verify](https://docs.microsandbox.dev/enterprise/deploy-and-verify.md): Pilot your configuration, distribute it to employee devices, and manage updates
- [Talk to the microsandbox team](https://docs.microsandbox.dev/enterprise/contact.md): Let’s plan your microsandbox deployment
- [Security model](https://docs.microsandbox.dev/security/overview.md): The trust boundary microsandbox enforces, what it protects, and what it leaves to you
- [Isolation boundary](https://docs.microsandbox.dev/security/isolation.md): The microVM boundary, the host-guest control channel, and in-guest privilege
- [Filesystem & images](https://docs.microsandbox.dev/security/filesystem.md): Private root, mounts, snapshots, and the image supply chain
- [Network defenses](https://docs.microsandbox.dev/security/network.md): Egress filtering, SSRF, DNS rebinding, and cloud-metadata protection
- [Secret handling](https://docs.microsandbox.dev/security/secrets.md): How credentials stay on the host, and the exact boundary of the guarantee
- [Hardening](https://docs.microsandbox.dev/security/hardening.md): Dial the controls to match your threat level
- [Migrating from v0.6 to v0.7](https://docs.microsandbox.dev/migrations/v0.7.md): Upgrade existing sandboxes, update secret and snapshot code, and understand rollback limits.
- [v0.7.8](https://docs.microsandbox.dev/changelog/v0.7.8.md): Keep commands running after disconnecting, narrow secret substitution, and restore snapshots with explicit storage bindings.
- [v0.7.7](https://docs.microsandbox.dev/changelog/v0.7.7.md): Connect through HTTP proxies, inspect local storage, and control the clock in snapshot-based tests.
- [v0.7.6](https://docs.microsandbox.dev/changelog/v0.7.6.md): Host paths stay fixed after a sandbox is created, and local volume operations stay inside the volume.
- [v0.7.5](https://docs.microsandbox.dev/changelog/v0.7.5.md): Fork running sandboxes with clearer commands, run scripted commands without stdin, and opt in to readable network denials.
- [v0.7.4](https://docs.microsandbox.dev/changelog/v0.7.4.md): More reliable secret scanning, writable macOS hard links, and typed Ruby errors.
- [v0.7.3](https://docs.microsandbox.dev/changelog/v0.7.3.md): Enforce team settings, work with simpler snapshot commands, and wait for sandboxes in scripts.
- [v0.7.2](https://docs.microsandbox.dev/changelog/v0.7.2.md): Upgrade your local sandbox database without stopping running sandboxes.
- [v0.7.1](https://docs.microsandbox.dev/changelog/v0.7.1.md): Choose how snapshots save pending disk writes, with fixes for upgrades and Node package installation.
- [v0.7.0](https://docs.microsandbox.dev/changelog/v0.7.0.md): Save running sandboxes, branch them into independent copies, and resume work from a checkpoint.
- [Week of September 25, 2026](https://docs.microsandbox.dev/changelog/2026-09-25.md): v0.7.3 fixes for saved sandbox configuration and macOS runtime discovery, plus snapshot upgrade guidance.
- [Week of September 11, 2026](https://docs.microsandbox.dev/changelog/2026-09-11.md): Strict hostname policy mode for network allowlists, standard stream devices in the guest, and forward-compatible cloud request handling.
- [Week of September 4, 2026](https://docs.microsandbox.dev/changelog/2026-09-04.md): Outbound SOCKS proxies for sandbox traffic, SOCKS5 UDP relay and proxy authentication, and a fix for upgrades from earlier releases.
- [Week of August 28, 2026](https://docs.microsandbox.dev/changelog/2026-08-28.md): Guest ownership for directory mounts, sparse layered sandbox configuration, Go SDK MSB_HOME support, isolated single-file mounts, and fixes for read-only mounts, log retrieval, and network slot exhaustion.
- [Week of August 26, 2026](https://docs.microsandbox.dev/changelog/2026-08-26.md): Reuse named sandboxes safely across every SDK.
- [Week of August 21, 2026](https://docs.microsandbox.dev/changelog/2026-08-21.md): Configurable SSH inactivity timeout, plural resource list shortcuts, precompiled Ruby platform gems, a fallible lazy local backend builder, faster Windows root-disk copies, and reliability fixes across networking, mounts, runtime bootstrap, and Linux releases.
- [Week of August 14, 2026](https://docs.microsandbox.dev/changelog/2026-08-14.md): Per-sandbox network rate limits, NUMA-aware placement profiles, sparse configuration patches with reusable config files, guest-to-host vsock routes, deployment profile from config.json, and reliability fixes across Windows attach, cloud request shapes, image archives, and DNS rules.
- [Week of August 7, 2026](https://docs.microsandbox.dev/changelog/2026-08-07.md): A first-class Ruby SDK, flat OCI root disks, deployment profiles, default-workload execution, host performance improvements, cloud volume filesystem access, and reliability fixes.
- [Week of July 31, 2026](https://docs.microsandbox.dev/changelog/2026-07-31.md): Unified cloud backend in every SDK with paginated sandbox listings, per-registry insecure and custom-CA overrides in Go and Python, msb completion for shell tab-completion, a shared log registry for tailing many sandboxes, and fixes for guest TCP half-close, DNS upstream failover, and cloud exec rec…
- [Week of July 24, 2026](https://docs.microsandbox.dev/changelog/2026-07-24.md): Composable network profiles across CLI and SDKs, bidirectional snapshot migration with msb self downgrade, msb run -d that honors image CMD, TTY resize in every SDK, and Go SDK on Windows.
- [Week of July 17, 2026](https://docs.microsandbox.dev/changelog/2026-07-17.md): Image archives on every SDK, a finalized snapshot API with dest_dir and --from-snapshot, hole-perfect snapshot archives across platforms, a newer guest kernel, and a batch of secret, snapshot, and SDK fixes.
- [Week of July 10, 2026](https://docs.microsandbox.dev/changelog/2026-07-10.md): Structured root disk for OCI sandboxes, default symlink protection on mount roots, secret modify across every SDK, offline OCI upper growth, cleaner guest shutdown, and a batch of snapshot, filesystem, and lifecycle fixes.
- [Week of July 5, 2026](https://docs.microsandbox.dev/changelog/2026-07-05.md): Modify existing sandboxes, inspect resize headroom, trust private TLS upstreams, load images faster, and pick up CLI, network, and SDK fixes.
- [Week of June 26, 2026](https://docs.microsandbox.dev/changelog/2026-06-26.md): Windows host support, guest-write quotas for virtiofs mounts, host-directory bind rootfs across all SDKs, non-PTY bidirectional `exec --stream`, upper disk usage metrics, an `msb doctor` command, runtime-owned ephemeral cleanup, and a round of SDK and runtime fixes.
- [Week of June 19, 2026](https://docs.microsandbox.dev/changelog/2026-06-19.md): Local and cloud backend routing in the SDKs, detached image init entrypoints, shared sandbox spec types, secret substitution through HTTP CONNECT tunnels and plain HTTP, and snapshot import hardening.
- [Week of June 12, 2026](https://docs.microsandbox.dev/changelog/2026-06-12.md): Guest runtime metrics, idempotent named volumes, unified sandbox lifecycle APIs, explicit mount kind flags, cleaner installer, raw agent socket paths, and richer secret violation logs.
- [Week of June 5, 2026](https://docs.microsandbox.dev/changelog/2026-06-05.md): OTLP sandbox metrics, SSH TCP forwarding, image archive commands, pruning, Python image management, Homebrew install, and smoother host upgrades.
- [Week of May 29, 2026](https://docs.microsandbox.dev/changelog/2026-05-29.md): Native SSH and SFTP, configurable OCI root disk size, msb copy and rootfs patch flags, hardened mount options, env-backed secret shorthand, and a fix for multi-second published-port stalls.
- [Week of May 22, 2026](https://docs.microsandbox.dev/changelog/2026-05-22.md): Rotation-aware log streaming, raw agent client across SDKs, per-mount passthroughfs policies, network policy CLI cleanup, configurable port bind addresses, and ergonomic --script.
- [Week of May 15, 2026](https://docs.microsandbox.dev/changelog/2026-05-15.md): Go SDK, file-first disk snapshots, guest init handoff, exec and boot logs, and DNS egress policy.
- [Week of May 1, 2026](https://docs.microsandbox.dev/changelog/2026-05-01.md): TypeScript SDK redesign, network policy redesign, disk-image volumes, and more.
- [Week of April 24, 2026](https://docs.microsandbox.dev/changelog/2026-04-24.md): Block-backed OCI rootfs, guest rlimits, and TypeScript SDK improvements.
- [Week of April 17, 2026](https://docs.microsandbox.dev/changelog/2026-04-17.md): New Python SDK, Docker image publishing, and TLS proxy fixes.
- [Week of April 10, 2026](https://docs.microsandbox.dev/changelog/2026-04-10.md): File-level volume mounts, TypeScript SDK streams, and `msb shell` removal.
- [Week of April 3, 2026](https://docs.microsandbox.dev/changelog/2026-04-03.md): The microsandbox rewrite around an embeddable SDK, smoltcp networking, and a composable filesystem.

## OpenAPI Specs

- [openapi](/api-reference/openapi.json)
- [openapi.personal](/api-reference/openapi.personal.json)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.

---

# Security model - microsandbox

`https://docs.microsandbox.dev/security/overview`

# Security model
## Documentation Index
## ​The trust boundary
## ​What you get by default
## ​Scope: what the boundary covers
## ​How the model is enforced
## ​Reporting a vulnerability







The trust boundary microsandbox enforces, what it protects, and what it leaves to you

microsandbox runs code you don’t trust, like AI agents, user submissions, plugins, scrapers, and build jobs, without handing any of it your host. This page describes the security model end to end: the boundary it draws, the guarantees that boundary gives you by default, and the things it deliberately leaves to you.
The whole model rests on one idea. **The guest is untrusted, the host is trusted, and a hardware hypervisor sits between them.** Every interaction a workload has with the outside world, whether files, network, secrets, or the control channel, is brokered by host-side code on the trusted side of that boundary.


## [​](https://docs.microsandbox.dev/security/overview#the-trust-boundary) The trust boundary


A sandbox is a microVM: a real virtual machine with its own Linux kernel, scheduled by a hardware hypervisor (KVM on Linux, Apple’s Hypervisor.framework on macOS). It is **not** a container sharing your host kernel.
![An untrusted guest reaches the trusted host only through hypervisor-mediated virtio channels: console, network, files, and disks.](https://mintcdn.com/superradcompanyinc/b2Kff8GKGqDeh1zw/images/security/trust-boundary-light.svg?fit=max&auto=format&n=b2Kff8GKGqDeh1zw&q=85&s=c959537875789f22a800eb7769fb29b0)![An untrusted guest reaches the trusted host only through hypervisor-mediated virtio channels: console, network, files, and disks.](https://mintcdn.com/superradcompanyinc/b2Kff8GKGqDeh1zw/images/security/trust-boundary-dark.svg?fit=max&auto=format&n=b2Kff8GKGqDeh1zw&q=85&s=78b0dc9242aac6f85ad0a742537dba51)
Two actors sit on either side of one boundary:


| Side | What lives there | How it’s treated |
| --- | --- | --- |
| **Guest** | Your workload and its processes, the guest Linux kernel, and `agentd` (the in-guest agent) | Fully untrusted. Assume it is adversarial. |
| **Host** | Your application or the `msb` CLI, plus the per-sandbox process that embeds the VMM, network stack, filesystem broker, and secret injection | Trusted. It enforces the boundary. |


The guest reaches the host only through a fixed, small set of paravirtual (virtio) devices. It cannot make host syscalls, read host memory, or open host connections on its own. Everything it asks for is mediated by the trusted side.


## [​](https://docs.microsandbox.dev/security/overview#what-you-get-by-default) What you get by default


Before any configuration, a sandbox already gives you:


- **Hardware-isolated execution.** Each sandbox has its own kernel and memory, scheduled by the hypervisor. A guest kernel compromise stays in the guest.
- **A private filesystem.** The guest sees only its image plus whatever you explicitly mount. Your host filesystem stays invisible.
- **An isolated writable root.** Writes land in a per-sandbox layer that never touches the shared image cache or another sandbox.
- **A network that can’t pivot inward.** The public internet is reachable, but private ranges, loopback, link-local, cloud metadata, and your host are all denied. Inbound traffic only reaches the ports you publish.
- **Secrets that stay on the host.** Credentials you bind never enter the VM. The guest only ever sees a meaningless placeholder.


One default surprises people: workloads run as **root inside the guest**. That is in-guest root, contained by the VM boundary. It is not a privilege on your host, and you can drop it. See [Isolation boundary](https://docs.microsandbox.dev/security/isolation#in-guest-privilege) and [Hardening](https://docs.microsandbox.dev/security/hardening).


## [​](https://docs.microsandbox.dev/security/overview#scope-what-the-boundary-covers) Scope: what the boundary covers


Being candid about the edges is more useful than a long list of features. Here is where the model defends you, where it does not, and what it expects you to own.


### [​](https://docs.microsandbox.dev/security/overview#defended-by-the-model) Defended by the model


- **Guest-to-host escape.** The VM and hypervisor boundary is what keeps a compromised guest off your host.
- **Sandbox-to-sandbox isolation.** Separate VMs, separate processes, separate writable layers, separate network gateways.
- **Egress filtering and SSRF.** Workloads cannot reach your private network, host, or cloud metadata service by default.
- **Secret leakage to unintended hosts.** A bound credential is only revealed at the host you allow it for.
- **Host filesystem privacy.** The guest sees nothing of your host disk unless you mount it.


### [​](https://docs.microsandbox.dev/security/overview#out-of-scope-by-design) Out of scope, by design


- **A compromised host.** If an attacker already controls your host, or the process that launches sandboxes, they are on the trusted side. Secret values live in host memory, and host configuration defines the policy. microsandbox protects the host from the guest, not a guest from a hostile host.
- **The hypervisor and CPU.** The model trusts KVM, Hypervisor.framework, and the silicon to enforce VM isolation. A hypervisor or hardware vulnerability sits below this boundary.
- **What an allowed destination does with your data.** If you allow egress to `api.example.com` and inject a secret there, that endpoint receives the real credential. The model controls *where* data can go, not what the far side does with it.
- **Image provenance.** Pulled content is verified against its declared digest, but signatures and attestations are not checked. The registry you pull from is part of your trusted base. See [Filesystem & images](https://docs.microsandbox.dev/security/filesystem#image-supply-chain).
- **Self-inflicted denial of service.** A workload can exhaust its own CPU and memory within the limits you set. That doesn’t affect other sandboxes or the host.


### [​](https://docs.microsandbox.dev/security/overview#your-responsibility) Your responsibility


- Pick a network policy that matches your threat model. The default is sensible, but high-stakes workloads often want deny-by-default.
- Drop in-guest privileges when the workload doesn’t need root.
- Pin images you trust, and mount only what’s needed, read-only where possible.
- Keep the host that runs sandboxes secure. It is the trusted anchor for everything above.


## [​](https://docs.microsandbox.dev/security/overview#how-the-model-is-enforced) How the model is enforced


Each subsystem carries part of the boundary. The pages below go deep on each, candidly including the limits.


## Isolation boundary

The microVM, the host-guest channel, and in-guest privilege.

## Filesystem & images

Private root, mounts, snapshots, and image supply chain.

## Network defenses

Egress filtering, SSRF, DNS rebinding, and metadata.

## Secret handling

How credentials stay on the host, and the exact guarantee.

## Hardening

Dial the controls to match your threat level.


## [​](https://docs.microsandbox.dev/security/overview#reporting-a-vulnerability) Reporting a vulnerability


If you find a way across any of these boundaries, like a guest-to-host escape, a cross-sandbox leak, an egress-filter bypass, or a secret revealed outside its intended host, we want to hear about it. Use [GitHub’s private vulnerability reporting](https://github.com/superradcompany/microsandbox/security/advisories/new) or email `security@superrad.company`. The full process and scope are in the project’s [security policy](https://github.com/superradcompany/microsandbox/blob/main/SECURITY.md).

Was this page helpful?

Yes No ⌘ I

---

# Enterprise deployment - microsandbox

`https://docs.microsandbox.dev/enterprise`

# Enterprise deployment
## ​Choose your deployment
## ​Roll out to employee devices
## ​Discuss your deployment




Choose a deployment approach for employee devices or your own infrastructure

Use microsandbox on employee devices or in your own infrastructure. Choose the deployment approach that fits your workloads and operational requirements.


## [​](https://docs.microsandbox.dev/enterprise#choose-your-deployment) Choose your deployment


| Deployment | Purpose | Next step |
## Documentation Index

| --- | --- | --- |
| Employee devices | Standardize local development and team settings | [Rollout guides](https://docs.microsandbox.dev/enterprise#roll-out-to-employee-devices) |
| Runtime on your infrastructure | Run sandboxes on your servers or clusters | [Discuss your deployment](https://docs.microsandbox.dev/enterprise/contact) |
| Private cloud deployment | Run the microsandbox cloud platform in your infrastructure | [Discuss requirements](https://docs.microsandbox.dev/enterprise/contact) |


For our hosted service, see [microsandbox Cloud](https://docs.microsandbox.dev/cloud/overview).


## [​](https://docs.microsandbox.dev/enterprise#roll-out-to-employee-devices) Roll out to employee devices


Start with one working installation, connect it to company services, then apply policy and roll it out to a pilot group.


| Step | Outcome |
| --- | --- |
| [Prepare your environment](https://docs.microsandbox.dev/enterprise/prepare-environment) | Approved SDKs, runtime files, and images work on the target devices, including offline installations. |
| [Configure company networking](https://docs.microsandbox.dev/enterprise/corporate-networking) | Sandboxes can reach approved services through company routing, DNS, and certificate trust. |
| [Enforce team settings](https://docs.microsandbox.dev/enterprise/managed-configuration) | A protected policy defines which supported settings employees cannot override. |
| [Deploy and verify](https://docs.microsandbox.dev/enterprise/deploy-and-verify) | A tested pilot, repeatable device deployment, and an update and rollback process. |


### [​](https://docs.microsandbox.dev/enterprise#deployment-responsibilities) Deployment responsibilities


| microsandbox provides | Your organization manages |
| --- | --- |
| Local sandbox isolation and network controls | Device security, host permissions, and approved workloads |
| Managed overrides for supported CLI and SDK settings | Policy distribution, file protection, and supported client versions |
| Runtime and image installation tools | Package approval, distribution, and updates |
| Configuration for company network access | VPN/proxy enrollment, credentials, DNS, and corporate certificates |


Managed settings apply through supported CLI and SDK clients. They are not a replacement for device security: local administrators can remove policy or replace the runtime.
These guides focus on local sandboxes on company-managed devices. Some managed settings also apply to outgoing cloud requests, as described in [Enforce team settings](https://docs.microsandbox.dev/enterprise/managed-configuration). They do not reconfigure the cloud service.


## [​](https://docs.microsandbox.dev/enterprise#discuss-your-deployment) Discuss your deployment


Planning a runtime rollout or private cloud deployment? [Contact our team](https://docs.microsandbox.dev/enterprise/contact) with a short description of your workloads and deployment needs.

Was this page helpful?

Yes No ⌘ I

---

# Claude Code - microsandbox

`https://docs.microsandbox.dev/how-to/agents/claude-code`

This guide installs a pinned Claude Code release inside a Node.js microVM and opens it in a project mounted from your host. Claude Code can edit the checkout directly, while its installation, authentication, settings, and sessions stay on the sandbox’s root disk.


## [​](https://docs.microsandbox.dev/how-to/agents/claude-code#run-claude-code) Run Claude Code
## Documentation Index
## ​Run Claude Code
## ​Reference





1

Start Claude Code

Local-only Replace `./my-project` with the project directory you want Claude Code to work on: macOS & Linux Windows

```
msb run -t --name claude-code-demo --replace \
  --cpus 2 --memory 4G --root-disk 4G \
  --mount-dir ./my-project:/workspace:rw \
  --workdir /workspace \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g @anthropic-ai/claude-code@2.1.235 &&
    exec claude
  '
```


```
msb run -t --name claude-code-demo --replace `
  --cpus 2 --memory 4G --root-disk 4G `
  --mount-dir ./my-project:/workspace:rw `
  --workdir /workspace `
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g @anthropic-ai/claude-code@2.1.235 &&
    exec claude
  '
```

Choose a terminal theme, then follow the sign-in prompts. If Claude Code cannot open a browser from the microVM, copy the displayed login URL and open it in a browser on your host. Anthropic recommends its standalone installer for normal host installations. This guide uses the pinned npm package for a reproducible sandbox setup; the package installs the same platform-native Claude Code binary. For an isolated workspace, or when using microsandbox cloud, replace `--mount-dir ./my-project:/workspace:rw` with `--copy-dir ./my-project:/workspace`. 2

Start another session

After leaving Claude Code, return to the same sandbox and workspace with: Shell

```
msb exec -t claude-code-demo -- claude
```

The sandbox root disk retains Claude Code’s authentication, configuration, and conversation state between sessions. 3

Verify the installation

Exit the TUI and run: Shell

```
msb exec claude-code-demo -- claude --version
```

The pinned example prints `2.1.235 (Claude Code)`. 4

Review or export changes

With the default writable mount, changes are already in the host checkout. Review them inside the sandbox: Shell

```
msb exec claude-code-demo -- sh -lc 'cd /workspace && git status --short && git diff --stat && git diff'
```

If you chose the isolated `--copy-dir` alternative, create a patch inside the sandbox: Shell

```
msb exec claude-code-demo -- sh -lc 'cd /workspace && git add -N . && git diff --binary > /tmp/claude-code.patch'
```

Copy the patch to the host: Shell

```
msb cp claude-code-demo:/tmp/claude-code.patch ./claude-code.patch
```

Check that it applies cleanly before applying it: Shell

```
git apply --check ./claude-code.patch
```

5

Clean up

Remove the sandbox: Shell

```
msb rm -f claude-code-demo
```

Removing the sandbox also removes its Claude Code credentials, settings, and sessions. Changes made through the default workspace mount remain in the host checkout.


## [​](https://docs.microsandbox.dev/how-to/agents/claude-code#reference) Reference


- [Claude Code setup](https://code.claude.com/docs/en/setup)
- [Claude Code authentication](https://code.claude.com/docs/en/authentication)


Was this page helpful?

Yes No ⌘ I

---

# Codex CLI - microsandbox

`https://docs.microsandbox.dev/how-to/agents/codex`

This guide installs a pinned Codex CLI release inside a Node.js microVM and opens it in a project mounted from your host. Codex can work directly in the checkout, while its executable, authentication, configuration, and sessions stay inside the sandbox.


## [​](https://docs.microsandbox.dev/how-to/agents/codex#run-codex-cli) Run Codex CLI


1

Start Codex

Local-only Replace `./my-project` with the project directory you want Codex to work on: macOS & Linux Windows

```
msb run -t --name codex-demo --replace \
  --cpus 2 --memory 2G --root-disk 4G \
  --mount-dir ./my-project:/workspace:rw \
  --workdir /workspace \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g @openai/codex@0.148.0 &&
    exec codex
  '
```


```
msb run -t --name codex-demo --replace `
  --cpus 2 --memory 2G --root-disk 4G `
  --mount-dir ./my-project:/workspace:rw `
  --workdir /workspace `
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g @openai/codex@0.148.0 &&
    exec codex
  '
```

On first launch, choose Sign in with ChatGPT, Sign in with Device Code, or provide an API key. Browser-based sign-in happens on your host while the resulting Codex credentials are stored on the sandbox’s root disk. For an isolated workspace, or when using microsandbox cloud, replace `--mount-dir ./my-project:/workspace:rw` with `--copy-dir ./my-project:/workspace`. 2
## Documentation Index
## ​Run Codex CLI
## ​Reference




Start another session

After leaving Codex, return to the same sandbox and workspace with: Shell

```
msb exec -t codex-demo -- codex
```

The sandbox root disk retains the files under `/root/.codex`, including authentication, configuration, and session history. 3

Verify the installation

Exit the TUI and run: Shell

```
msb exec codex-demo -- codex --version
```

The pinned example prints `codex-cli 0.148.0`. 4

Review or export changes

With the default writable mount, changes are already in the host checkout. Review them inside the sandbox: Shell

```
msb exec codex-demo -- sh -lc 'cd /workspace && git status --short && git diff --stat && git diff'
```

If you chose the isolated `--copy-dir` alternative, create a patch inside the sandbox: Shell

```
msb exec codex-demo -- sh -lc 'cd /workspace && git add -N . && git diff --binary > /tmp/codex.patch'
```

Copy the patch to the host: Shell

```
msb cp codex-demo:/tmp/codex.patch ./codex.patch
```

Check that it applies cleanly before applying it: Shell

```
git apply --check ./codex.patch
```

5

Clean up

Remove the sandbox: Shell

```
msb rm -f codex-demo
```

Removing the sandbox also removes its Codex credentials, configuration, and sessions. Changes made through the default workspace mount remain in the host checkout.


## [​](https://docs.microsandbox.dev/how-to/agents/codex#reference) Reference


- [Codex CLI](https://developers.openai.com/codex/cli/)
- [Codex CLI repository](https://github.com/openai/codex)


Was this page helpful?

Yes No ⌘ I

---

# OpenCode - microsandbox

`https://docs.microsandbox.dev/how-to/agents/opencode`

This guide installs OpenCode in a microVM and opens its terminal UI in a project mounted from your host. OpenCode edits the source checkout directly while its tools and dependencies stay inside the sandbox.


## [​](https://docs.microsandbox.dev/how-to/agents/opencode#run-opencode) Run OpenCode


1

Start OpenCode

Local-only Replace `./my-project` with the project directory you want OpenCode to work on: macOS & Linux Windows

```
msb run -t --name opencode-demo --replace \
  --cpus 2 --memory 2G --root-disk 4G \
  --mount-dir ./my-project:/workspace:rw \
  --workdir /workspace \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g opencode-ai@1.18.4 &&
    exec opencode
  '
```


```
msb run -t --name opencode-demo --replace `
  --cpus 2 --memory 2G --root-disk 4G `
  --mount-dir ./my-project:/workspace:rw `
  --workdir /workspace `
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g opencode-ai@1.18.4 &&
    exec opencode
  '
```

The first run downloads the package and may take a couple of minutes. OpenCode should render its prompt and offer `/connect` for provider setup. Its XDG configuration, provider connections, and session data live on the sandbox’s 4 GiB root disk and remain available when the sandbox stops and starts. For an isolated workspace, or when using microsandbox cloud, replace `--mount-dir ./my-project:/workspace:rw` with `--copy-dir ./my-project:/workspace`. To try the TUI without a project, use `--mkdir /workspace` instead. 2
## Documentation Index
## ​Run OpenCode
## ​Use OpenCode from any project
## ​Reference





Start another session

After leaving OpenCode, return to the same sandbox and workspace with: Shell

```
msb exec -t opencode-demo -- opencode
```

3

Verify the installation

Exit the TUI, then run: Shell

```
msb exec opencode-demo -- opencode --version
```

The pinned example prints `1.18.4`. 4

Review or export changes

With the default writable mount, changes are already in the host checkout. Review the diff from either side of the mount: Shell

```
msb exec opencode-demo -- sh -lc 'cd /workspace && git status --short && git diff --stat && git diff'
```

If you chose the isolated `--copy-dir` alternative, export a patch from the sandbox: Shell

```
msb exec opencode-demo -- sh -lc 'cd /workspace && git add -N . && git diff --binary > /tmp/opencode.patch'
```

Copy the patch to the host: Shell

```
msb cp opencode-demo:/tmp/opencode.patch ./opencode.patch
```

Check that it applies cleanly before applying it: Shell

```
git apply --check ./opencode.patch
```

5

Clean up

Remove the sandbox: Shell

```
msb rm -f opencode-demo
```

Removing the sandbox also removes its provider connections, sessions, and OpenCode configuration. Changes made through the default workspace mount remain in the host checkout. Never copy an agent’s entire home directory back to the host.


## [​](https://docs.microsandbox.dev/how-to/agents/opencode#use-opencode-from-any-project) Use OpenCode from any project


To launch OpenCode from whichever project folder you are in, install a reusable host command:
macOS & Linux Windows

```
msb install --tmp --name opencode-project \
  --cpus 2 --memory 2G \
  --mount-dir ./:/workspace:rw --workdir /workspace \
  --mount-named opencode-config:/root/.config/opencode \
  --mount-named opencode-data:/root/.local/share/opencode \
  --mount-named opencode-state:/root/.local/state/opencode \
  node:24-bookworm-slim -- sh -lc 'apt-get update && apt-get install -y --no-install-recommends ca-certificates git && npm install -g opencode-ai@1.18.4 && exec opencode'
```


```
msb install --tmp --name opencode-project `
  --cpus 2 --memory 2G `
  --mount-dir ./:/workspace:rw --workdir /workspace `
  --mount-named opencode-config:/root/.config/opencode `
  --mount-named opencode-data:/root/.local/share/opencode `
  --mount-named opencode-state:/root/.local/state/opencode `
  node:24-bookworm-slim -- sh -lc 'apt-get update && apt-get install -y --no-install-recommends ca-certificates git && npm install -g opencode-ai@1.18.4 && exec opencode'
```


Then run this from a project folder on your host:
Shell

```
opencode-project
```


`--tmp` creates a fresh sandbox for each session and removes it on exit. The `./` mount uses the folder you launch `opencode-project` from. Keep it relative; passing a full path during installation fixes the command to that folder.
Project edits stay on your host. The named volumes keep OpenCode’s configuration, provider connections, and session history across runs. Other sandbox changes are discarded, so this example installs OpenCode and its dependencies again on each launch.
Without `--tmp`, an installed command reuses the same sandbox and its original workspace mount. See [`msb install`](https://docs.microsandbox.dev/cli/sandbox-commands#msb-install).
To remove the host command:
Shell

```
msb uninstall opencode-project
```


The three named volumes remain until you [remove them explicitly](https://docs.microsandbox.dev/cli/volume-commands#msb-volume-rm).


## [​](https://docs.microsandbox.dev/how-to/agents/opencode#reference) Reference


- [OpenCode installation](https://opencode.ai/docs/)


Was this page helpful?

Yes No ⌘ I

---

# Goose - microsandbox

`https://docs.microsandbox.dev/how-to/agents/goose`

Goose publishes native Linux binaries for both `aarch64` and `x86_64`. Its installer detects the guest architecture, which makes it a relatively small agent setup compared with a large Python environment.


## [​](https://docs.microsandbox.dev/how-to/agents/goose#run-goose) Run Goose


1

Start Goose

Local-only macOS & Linux Windows

```
msb run -t --name goose-demo --replace \
  --cpus 2 --memory 2G --root-disk 3G \
  --mount-dir ./my-project:/workspace:rw \
  --workdir /workspace \
  debian:bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates curl bzip2 git &&
    curl -fsSL https://github.com/aaif-goose/goose/releases/download/v1.44.0/download_cli.sh |
      GOOSE_BIN_DIR=/usr/local/bin GOOSE_VERSION=v1.44.0 CONFIGURE=false bash &&
    exec goose session
  '
```


```
msb run -t --name goose-demo --replace `
  --cpus 2 --memory 2G --root-disk 3G `
  --mount-dir ./my-project:/workspace:rw `
  --workdir /workspace `
  debian:bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates curl bzip2 git &&
    curl -fsSL https://github.com/aaif-goose/goose/releases/download/v1.44.0/download_cli.sh |
      GOOSE_BIN_DIR=/usr/local/bin GOOSE_VERSION=v1.44.0 CONFIGURE=false bash &&
    exec goose session
  '
```

On first launch Goose asks whether to share anonymous usage data, then walks through provider configuration. `GOOSE_BIN_DIR` installs the executable on the sandbox’s normal `PATH`, including later `msb exec` sessions. Goose keeps its configuration, data, and session state on the sandbox’s 3 GiB root disk. For an isolated workspace, or when using microsandbox cloud, replace `--mount-dir ./my-project:/workspace:rw` with `--copy-dir ./my-project:/workspace`. To test Goose without a project, use `--mkdir /workspace` instead. 2
## Documentation Index
## ​Run Goose
## ​Reference




Start another session

After leaving Goose, return to the same sandbox and workspace with: Shell

```
msb exec -t goose-demo -- goose session
```

3

Verify the installation

Exit the session and run: Shell

```
msb exec goose-demo -- goose --version
```

The pinned installer reports `1.44.0`. 4

Review or export changes

With the default writable mount, changes are already in the host checkout. Review them inside the sandbox: Shell

```
msb exec goose-demo -- sh -lc 'cd /workspace && git status --short && git diff --stat && git diff'
```

If you chose the isolated `--copy-dir` alternative, create a patch inside the sandbox: Shell

```
msb exec goose-demo -- sh -lc 'cd /workspace && git add -N . && git diff --binary > /tmp/goose.patch'
```

Copy the patch to the host: Shell

```
msb cp goose-demo:/tmp/goose.patch ./goose.patch
```

Check that it applies cleanly before applying it: Shell

```
git apply --check ./goose.patch
```

5

Clean up

Remove the sandbox: Shell

```
msb rm -f goose-demo
```

Removing the sandbox also removes its Goose configuration and session data. Changes made through the default workspace mount remain in the host checkout.


## [​](https://docs.microsandbox.dev/how-to/agents/goose#reference) Reference


- [Goose repository and installer](https://github.com/aaif-goose/goose)
- [Goose environment variables](https://github.com/aaif-goose/goose/blob/main/documentation/docs/guides/environment-variables.md)


Was this page helpful?

Yes No ⌘ I

---

# OpenClaw - microsandbox

`https://docs.microsandbox.dev/how-to/agents/openclaw`

OpenClaw combines an interactive agent with a long-running gateway. This guide persists its state in a named volume and maps the gateway only to host loopback.


## [​](https://docs.microsandbox.dev/how-to/agents/openclaw#set-up-openclaw) Set up OpenClaw


1

Run onboarding

Limited on cloud macOS & Linux Windows

```
msb run -t --name openclaw-setup --replace \
  --cpus 2 --memory 2G --root-disk 4G \
  --mount-named openclaw-data:/root/.openclaw \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g openclaw@2026.7.1-2 &&
    exec openclaw onboard --mode local
  '
```


```
msb run -t --name openclaw-setup --replace `
  --cpus 2 --memory 2G --root-disk 4G `
  --mount-named openclaw-data:/root/.openclaw `
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g openclaw@2026.7.1-2 &&
    exec openclaw onboard --mode local
  '
```

Complete the provider and channel prompts. The `openclaw-data` volume retains the workspace, configuration, credentials, sessions, and gateway state after the setup sandbox is removed. Verify the installed version before removing the setup sandbox: Shell

```
msb exec openclaw-setup -- openclaw --version
```

The pinned package reports `OpenClaw 2026.7.1-2`. 2

Run the gateway

Local-only Generate a token in the host shell: macOS & Linux Windows

```
export OPENCLAW_GATEWAY_TOKEN="$(openssl rand -hex 32)"
```


```
$bytes = New-Object byte[] 32
$rng = [Security.Cryptography.RandomNumberGenerator]::Create()
$rng.GetBytes($bytes)
$rng.Dispose()
$env:OPENCLAW_GATEWAY_TOKEN = -join ($bytes | ForEach-Object { $_.ToString('x2') })
```

Start a fresh gateway sandbox using the persisted state: macOS & Linux Windows

```
msb run -d --name openclaw-gateway --replace \
  --cpus 2 --memory 2G --root-disk 4G \
  -p 127.0.0.1:18789:18789 \
  -e OPENCLAW_GATEWAY_TOKEN="$OPENCLAW_GATEWAY_TOKEN" \
  --mount-named openclaw-data:/root/.openclaw \
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g openclaw@2026.7.1-2 &&
    exec openclaw gateway run --bind lan --port 18789 --auth token
  '
```


```
msb run -d --name openclaw-gateway --replace `
  --cpus 2 --memory 2G --root-disk 4G `
  -p 127.0.0.1:18789:18789 `
  -e "OPENCLAW_GATEWAY_TOKEN=$env:OPENCLAW_GATEWAY_TOKEN" `
  --mount-named openclaw-data:/root/.openclaw `
  node:24-bookworm-slim -- sh -lc '
    apt-get update &&
    apt-get install -y --no-install-recommends ca-certificates git &&
    npm install -g openclaw@2026.7.1-2 &&
    exec openclaw gateway run --bind lan --port 18789 --auth token
  '
```

The gateway listens inside the guest on port 18789, while microsandbox exposes it only at `127.0.0.1:18789` on the host. Follow its output with: Shell

```
msb logs -f openclaw-gateway
```

`OPENCLAW_GATEWAY_TOKEN` is visible to the guest and to processes that can inspect the host command environment. Use the microsandbox [secrets workflow](https://docs.microsandbox.dev/sandboxes/secrets) for production credentials. Do not change the host bind address to `0.0.0.0` without adding transport security and understanding the exposure. 3

Clean up

Remove the setup and gateway sandboxes: Shell

```
msb rm -f openclaw-setup openclaw-gateway
```

Remove persisted OpenClaw state only when you no longer need it: Shell

```
msb volume rm openclaw-data
```

Clear the token from the host shell: macOS & Linux Windows

```
unset OPENCLAW_GATEWAY_TOKEN
```


```
Remove-Item Env:OPENCLAW_GATEWAY_TOKEN
```

Keep `openclaw-data` if you want the configured agent to survive sandbox replacement.


## [​](https://docs.microsandbox.dev/how-to/agents/openclaw#reference) Reference


- [OpenClaw getting started](https://docs.openclaw.ai/getting-started)
- [OpenClaw gateway CLI](https://docs.openclaw.ai/cli/gateway)
## Documentation Index
## ​Set up OpenClaw
## ​Reference





Was this page helpful?

Yes No ⌘ I