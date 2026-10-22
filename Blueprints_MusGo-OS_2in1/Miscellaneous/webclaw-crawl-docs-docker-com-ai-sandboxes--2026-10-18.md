# Docker Sandboxes

`https://docs.docker.com/ai/sandboxes`

# Docker Sandboxes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker Sandboxes run AI coding agents in isolated environments on your machine or on Docker-managed cloud infrastructure. Use the `sbx` CLI to create and manage either kind of sandbox.


The `sbx` CLI and local sandbox compute are free to use, including for commercial work. Cloud compute uses a [pay-as-you-go subscription](https://docs.docker.com/agentic-platform/signup/#billing). Model-provider charges are separate.


Organization admins can [centrally manage sandbox network, filesystem, and MCP policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/), for local sandboxes across developer machines. Available on a separate paid subscription.


## [Get started](https://docs.docker.com/ai/sandboxes#get-started)


[Install the `sbx` CLI](https://docs.docker.com/ai/sandboxes/install/) and sign in, then choose where to run your agent:


| Environment | Use it for | Start here |
| --- | --- | --- |
| Local sandboxes | Work with files and supported hardware on your machine | [Get started locally](https://docs.docker.com/ai/sandboxes/get-started/) |
| Cloud sandboxes | Run on Docker-managed compute without local virtualization | [Get started in the cloud](https://docs.docker.com/ai/sandboxes/cloud/#get-started) |


The two environments have separate credentials, network policies, and lifecycle controls. See [Compare local and cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/) before adapting a workflow.


To create and manage cloud sandboxes from your application, see [Sandboxes API and SDK](https://docs.docker.com/ai/sandboxes-api/).


*Install the sbx CLI and sign in, then choose where to run your
agent:*

## [Learn more](https://docs.docker.com/ai/sandboxes#learn-more)


The following guides describe local sandbox workflows. For cloud workflows, see [Cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/).


- [Agents](https://docs.docker.com/ai/sandboxes/agents/) — supported agents and per-agent configuration
- [Workflows](https://docs.docker.com/ai/sandboxes/workflows/) — patterns for Git, local development, authentication, agent skills, and automation
- [Configuration](https://docs.docker.com/ai/sandboxes/configuration/) — manage credentials, declare project environments, turn on GPU passthrough, and configure an upstream proxy
- [Integrations](https://docs.docker.com/ai/sandboxes/integrations/) — connect editors and apps like VS Code and Cursor to a sandbox over SSH
- [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/) — register MCP servers and connect them to sandboxed agents
- [Kits](https://docs.docker.com/ai/sandboxes/customize/) — package tools and configuration into reusable sandbox environments
- [Architecture](https://docs.docker.com/ai/sandboxes/architecture/) — microVM isolation, workspace mounting, networking
- [Security](https://docs.docker.com/ai/sandboxes/security/) — isolation model, credential handling, and network policies
- [CLI reference](https://docs.docker.com/reference/cli/sbx/) — full list of `sbx` commands and options
- [Troubleshooting](https://docs.docker.com/ai/sandboxes/troubleshooting/) — common issues and fixes
- [FAQ](https://docs.docker.com/ai/sandboxes/faq/) — login requirements, telemetry, etc


## [Feedback](https://docs.docker.com/ai/sandboxes#feedback)


Your feedback shapes what gets built next. If you run into a bug, hit a missing feature, or have a suggestion, open an issue at [github.com/docker/sbx-releases/issues](https://github.com/docker/sbx-releases/issues).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Home

`https://docs.docker.com/`

Start a new chat
Answers are generated based on the documentation.

# How can we help?


How do I get started with Docker?


Can I run my AI agent in a sandbox?


How do I containerize an application?


What are Docker Hardened Images?


Why should I use Docker Compose? [### Get started Containerize an app, sandbox an agent, or pilot Docker for your organization.](https://docs.docker.com/get-started/) [### Guides Optimize your development workflows with Docker.](https://docs.docker.com/guides/) [### Manuals Install, set up, configure, and use Docker products.](https://docs.docker.com/manuals/) [### Reference Browse the CLI and API documentation.](https://docs.docker.com/reference/)

1. Sep 29 [Docker Home Sep 29 Assign licenses to teams Assign a product license to a team so every current and future member receives it. The Licenses page in Docker Home shows available licenses and whether they are assigned to teams or individuals.](https://docs.docker.com/accounts/organization/manage/manage-licenses/#teams)
2. Sep 24 [Docker Sandboxes Sep 24 Run sandboxes on Docker-managed cloud infrastructure Create and manage cloud sandboxes with the sbx CLI, including cloud-specific credentials, network policies, lifecycle controls, and transfers between local and cloud environments.](https://docs.docker.com/ai/sandboxes/cloud/)
3. Sep 24 [Docker Sandboxes Sep 24 Manage cloud sandboxes with the API and TypeScript SDK Create cloud sandboxes, run commands, transfer files, and manage images, snapshots, volumes, and secrets from applications and automated workflows.](https://docs.docker.com/ai/sandboxes-api/)
4. Sep 24 [Docker Sandboxes Sep 24 Compose sandbox environments with kits v3 Build sandbox environments from workload and mixin kits, combine them into reusable kit sets, and publish the result as a container image.](https://docs.docker.com/ai/sandboxes/customize/)
5. Sep 24 [Docker Skills Sep 24 Give coding agents guidance with Docker Skills Install Docker's official open-source skills in compatible coding agents to give them guidance for Dockerfiles, Compose applications, and other Docker tasks.](https://docs.docker.com/ai/skills/)
6. Sep 15 [Docker Sandboxes Sep 15 Share agent skills read-only by default Sandboxes created with version 0.43.0 mount shared agent skills read-only by default. Choose read-only, read-write, or no access when creating a sandbox.](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/#shared-store-behavior)
7. Sep 7 [Docker Sandboxes Sep 7 Run agents without mounting host files Create a sandbox without a host workspace mount. Keep agent files inside the sandbox across stops and restarts, and copy files between the sandbox and host when needed.](https://docs.docker.com/ai/sandboxes/usage/#choose-a-workspace)
8. Sep 7 [Docker Sandboxes Sep 7 Install and update shared skills from Git repositories Install agent skills from Git repositories into a persistent store shared across sandboxes, and update or remove them with sbx skills.](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/)
9. Sep 3 [Docker Build Cloud Sep 3 Use Docker Build Cloud with standard Buildx Buildx 0.37.0 includes the cloud driver, so you can connect to Docker Build Cloud from the standard Buildx CLI plugin without installing a separate client.](https://docs.docker.com/build/builders/drivers/cloud/)


Show more

---

# Cloud sandboxes

`https://docs.docker.com/ai/sandboxes/cloud`

# Cloud sandboxes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Cloud sandboxes run AI agents on Docker-managed infrastructure instead of your local machine. Use them when you need an isolated environment that doesn't depend on the compute resources or virtualization support of your host.


Cloud sandboxes use the same `sbx` CLI as local sandboxes. Add the global `--cloud` flag to send a supported command to the Cloud Sandboxes API:


```console
$ sbx --cloud ls
```


Cloud and local sandboxes have separate state and different capabilities. A cloud sandbox can't mount a host workspace or use host hardware, and its secrets, network policy, ports, and lifecycle are managed in the cloud. See [Local and cloud differences](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/) before adapting a local workflow.


## [Prerequisites](https://docs.docker.com/ai/sandboxes/cloud#prerequisites)


To use cloud sandboxes, you need:


- The [`sbx` CLI](https://docs.docker.com/ai/sandboxes/install/), version 0.45.0 or later
- An active [Docker Agentic Platform subscription](https://docs.docker.com/agentic-platform/signup/#activate-cloud-access)


Follow [Signup and billing](https://docs.docker.com/agentic-platform/signup/) to activate cloud access and review compute charges. Then return here to sign in from the CLI and configure your agent.


### [Sign in from the CLI](https://docs.docker.com/ai/sandboxes/cloud#sign-in-from-the-cli)


Sign in with the same Docker account you used to subscribe:


```console
$ sbx login
```


For CI and other environments without a browser, sign in with a Docker Personal Access Token (PAT) for the subscribed account:


```console
$ echo "$DOCKER_PAT" | sbx login --username <your-docker-id> --password-stdin
```


For PAT setup instructions, see [CI and headless use](https://docs.docker.com/ai/sandboxes/workflows/automation/).


Check cloud connectivity and account access:


```console
$ sbx --cloud diagnose
```


If the check reports that your account doesn't have access, follow [Check account access](https://docs.docker.com/agentic-platform/signup/#check-account-access).


*For PAT setup instructions, see CI and headless use.*

## [Get started](https://docs.docker.com/ai/sandboxes/cloud#get-started)


Credentials configured for local sandboxes aren't available to cloud sandboxes. Configure a cloud credential for your agent before launching it. For Claude Code, store an Anthropic API key:


```console
$ sbx --cloud secret set anthropic
```


See [Authenticate cloud agents](https://docs.docker.com/ai/sandboxes/cloud/credentials/) for other agents and credential options.


Cloud sandboxes expire after one hour by default. On expiration, the service stops sandboxes that can be resumed and deletes the rest. Check the timeout action before relying on a sandbox to retain your work. See [Configure expiration](https://docs.docker.com/ai/sandboxes/cloud/usage/#configure-expiration).


Create a sandbox without attaching, allowing access to GitHub for this example:


```console
$ sbx --cloud create --name cloud-project --allow-network github.com:443 claude
```


Cloud sandboxes don't accept a local workspace path. Clone the public [Welcome to Docker repository](https://github.com/docker/welcome-to-docker) inside the sandbox:


```console
$ sbx --cloud exec cloud-project git clone \
    https://github.com/docker/welcome-to-docker.git /home/agent/workspace/project
```


Attach to the agent:


```console
$ sbx --cloud attach cloud-project
```


Ask Claude to inspect `/home/agent/workspace/project` and write a description of the application to `/home/agent/workspace/review.md`. When the file is ready, press `Ctrl+\` to detach and leave the agent running.


Copy the result to your machine:


```console
$ sbx --cloud cp cloud-project:/home/agent/workspace/review.md ./review.md
```


Read the result, then remove the sandbox when you're finished:


```console
$ sbx --cloud rm cloud-project
```


Removal deletes files stored only in the sandbox. For your own projects, see [Transfer files](https://docs.docker.com/ai/sandboxes/cloud/usage/#transfer-files) and [Authenticate cloud agents](https://docs.docker.com/ai/sandboxes/cloud/credentials/) before cloning private repositories.


*See Authenticate cloud agents for other agents and credential
options.*

## [Learn more](https://docs.docker.com/ai/sandboxes/cloud#learn-more)


- [Signup and billing](https://docs.docker.com/agentic-platform/signup/) covers activation and compute charges
- [Local and cloud differences](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/) compares the two execution environments
- [Use cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/usage/) covers creation, files, ports, and lifecycle
- [Authenticate cloud agents](https://docs.docker.com/ai/sandboxes/cloud/credentials/) covers cloud-specific secrets, API keys, and OAuth
- [Manage cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) covers account-level and sandbox-level network access
- [Move a sandbox](https://docs.docker.com/ai/sandboxes/cloud/move/) explains filesystem transfers between local and cloud environments
- [`sbx` CLI reference](https://docs.docker.com/reference/cli/sbx/) lists commands and options[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Organization policies

`https://docs.docker.com/ai/sandboxes/governance/access-controls/organization`

# Organization policies


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The governance described here applies to local sandboxes. Cloud sandboxes use separate network policy configuration. See [Cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) for cloud controls.


[Local policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/) give individual developers control over what their sandboxes can access. Organization policy moves that control to the admin level: organization policies apply to local sandboxes across the organization, either to every member or to specific teams. When organization governance is active, only organization allow rules grant access: local `sbx policy` allow rules are no longer evaluated and can't expand what the organization permits. Local network deny rules remain active, so developers can restrict access further but never loosen it.


Admins can manage organization policies through the Docker Home UI. For programmatic management of network and filesystem policies, use the [Governance API](https://docs.docker.com/reference/api/ai-governance/).


By default, only organization [owners](https://docs.docker.com/security/roles-and-permissions/core-roles/) can view and manage AI Governance policies. To let someone other than an owner manage policies, create a [custom role](https://docs.docker.com/security/roles-and-permissions/custom-roles/) with the **Governance** permissions and assign it to a user or team.


> Note
>
> Sandbox organization governance is available on a separate paid subscription. [Contact Docker Sales](https://www.docker.com/products/ai-governance/#contact-sales) to request access.


## [Create a policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#create-a-policy)


Manage policies from the **AI Platform** section in the left-hand navigation of [Docker Home](https://app.docker.com).


To create a policy:


1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. In the left-hand navigation, expand **AI Platform** and select **Network access**, **Filesystem access**, or **MCP access**.
3. Select **Create policy**.
4. Enter a **Policy name**.
5. Set the **Scope** to **Organization** or **Teams**. If you select **Teams**, choose the teams the policy applies to. See [Scope policies to teams](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#scope-policies-to-teams).
6. Define the policy rules.
  - Network and filesystem policies: select **Add rule** for each rule. For a network policy, see [Add a network rule](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#add-a-network-rule).
  - MCP policies: enter Cedar statements in the policy editor. See [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/).7. For a network policy, set **Require approval before access** if developers should confirm each destination before a sandbox can reach it. See [Require approval for a network policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#require-approval-for-a-network-policy).


Existing policies are listed with their name, scope, rule count, and last update. Use the action menu (⋮) to edit or delete a policy.


### [Add a network rule](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#add-a-network-rule)


Each rule has an optional **Rule name**, a **Type** that decides what the rule matches, and a **Decision** of **Allow** or **Deny**.


- **HTTP** matches only HTTP requests with the methods and paths you specify.
  - In **Destination**, enter the host or IP address the rule covers. It matches any port unless you add one. Enter the destination with no scheme and no path, so `api.github.com` rather than `https://api.github.com/repos`. A local HTTP rule accepts only a host.
  - Under **HTTP methods**, select the methods the rule applies to. Use **Select all** to select every method, or **Read-only** to select `GET`, `HEAD`, and `OPTIONS`. A rule saved with no methods selected matches every method the composer lists. The composer doesn't list `CONNECT` or `TRACE`, which differs from the CLI, where `--method ANY` matches every HTTP method.
  - Under **Path patterns**, add one or more paths the rule covers, such as `/repos/*` and `/v1/**`. Leave it empty to match any path.- **All traffic** matches every request to the destinations you list, on any port, method, and path.
  - Under **Protocols**, select **TCP**, **UDP**, or **Both**.
  - Under **Destinations**, add the hosts, IP addresses, or CIDR ranges the rule covers. A destination matches any port unless you add one, such as `example.com:8080`.


An HTTP rule's paths all belong to its one destination, so to cover paths on a second host, add a second rule. For the pattern syntax and how HTTP rules combine with **All traffic** rules, see [HTTP rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#http-method-and-path).


### [Require approval for a network policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#require-approval-for-a-network-policy)


Turning on **Require approval before access** means the destinations a network policy allows aren't reachable until the developer confirms each one. For how approval behaves and what satisfies it, see [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


To set it on an existing policy:


1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. In the left-hand navigation, expand **AI Platform** and select **Network access**.
3. In the policy list, open the policy's action menu (⋮) and select **Edit**.
4. Turn on **Require approval before access**.
5. Select **Save**.


The policy's detail page reports approval as **Required** or **Not required**. Editing a policy replaces it in full, so turning the setting off removes the requirement from every rule in that policy.


## [Configure a support message](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#configure-a-support-message)


Admins can add an optional support message that appears after the policy denial details when a sandbox action is blocked by organization governance. Use it to point members to an internal support channel, ticket queue, or security contact.


To set the message:


1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. In the left-hand navigation, expand **AI Platform** and select **Manage**.
3. In **Support message**, enter up to 500 characters.
4. Select **Save changes**.


Docker shows the message only for denials caused by organization governance policy and for requests an [approval-required policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access) blocks. If you leave it blank, Docker shows the policy denial without additional contact text.


## [Choose a policy type](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#choose-a-policy-type)


Organization policies are managed by access surface. Use the access-control pages for syntax, examples, and enforcement details:


- [Network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/): control outbound network access from sandboxes, by host or by HTTP method and path.
- [Filesystem access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/): control which host paths sandboxes can mount as workspaces.
- [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/): control MCP server registration, tool calls, resources, prompts, and approval gates with Cedar policy.


When organization governance is active, local and kit-defined allow rules are not evaluated, while deny rules from those sources still apply. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence). To see which rules are active on a developer machine, use [Monitoring policies](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/).


## [Scope policies to teams](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#scope-policies-to-teams)


An organization can have more than one policy, and each policy applies either to the whole organization or to specific teams. Scoping lets you apply different rules to different parts of the organization.


A policy's [**Scope**](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#create-a-policy) controls who it applies to. Set it to **Organization** to apply the policy to every member, or to **Teams** to apply it only to members of the teams you select.


### [Before you start](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#before-you-start)


Team scoping targets your organization's existing [teams](https://docs.docker.com/accounts/organization/manage/manage-a-team/), so a team must exist before you can scope a policy to it. Create teams and manage their members in one of two ways:


- Manually, in Docker Home.
- Automatically, by using [group mapping](https://docs.docker.com/security/provisioning/scim/group-mapping/) to synchronize your identity provider's groups with the teams in your organization. Group mapping creates teams that don't already exist and keeps their membership in step with your IdP groups.


Because policies apply by team, a user's policies update automatically as their team membership changes, including changes synced from your IdP.


### [How scoped policies combine](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#how-scoped-policies-combine)


A user is governed by all of their [effective policies](https://docs.docker.com/ai/sandboxes/governance/concepts/#policy-scope): every org-wide policy, plus the team-scoped policies for the teams they belong to. Use org-wide policies for guardrails that must apply everywhere, and team-scoped policies for access that only some teams need.


For precedence between local and organization policies, and for how allow and deny rules combine, see [Policy concepts](https://docs.docker.com/ai/sandboxes/governance/concepts/).


## [Troubleshooting](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#troubleshooting)


### [Policy changes not taking effect](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#policy-changes-not-taking-effect)


After updating organization policies, changes take up to 5 minutes to propagate to developer machines. To apply changes immediately, users can run `sbx policy reset`, which stops the daemon and forces it to pull the latest organization policies on the next `sbx` command.


> Warning
>
> `sbx policy reset` deletes all locally configured policy rules, including any destinations the developer has approved under an [approval-required policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access). Those destinations are requested again the next time a sandbox reaches them. The command prompts for confirmation before proceeding.


#### [Enforcement timing by policy type](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization#enforcement-timing-by-policy-type)


Policy types differ in when a change takes effect after it reaches the developer machine:


- Network policy is evaluated on every outbound request. Once a policy change has synced to the developer's machine (up to 5 minutes), it applies immediately to subsequent requests. HTTP rules are evaluated per request in the same way.
- An approval requirement applies from the point the policy change syncs. Destinations a developer already approved stay reachable, because the approval is recorded on the developer's machine. To withdraw one, add a deny rule. A deny takes precedence over a recorded approval.
- Filesystem policy is only checked when a workspace is mounted — that is, when a sandbox is created. Once a sandbox is running, changing the filesystem policy has no effect on that sandbox. The sandbox continues to access the previously allowed path until it is removed and a new one is created.
- MCP registration policy is evaluated when a server is registered with `sbx mcp add`. Changing registration rules doesn't remove existing registrations or stop an already-loaded server by itself.
- MCP use-time policy is evaluated by the MCP gateway when a sandbox makes a governed MCP request, such as a tool call, resource read, prompt retrieval, or built-in gateway tool call. Once a policy change has synced, use-time rules apply to subsequent governed MCP requests through the gateway.


To apply a filesystem policy change immediately, remove the running sandbox and create a new one. To prevent use of an MCP server that is already registered or loaded, add use-time rules for the registered server name. For examples, see [Withdraw server access](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/#withdraw-server-access).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Manuals

`https://docs.docker.com/manuals`

# Manuals


Ask Gordon


Copy Markdown


View Markdown

---


---


This section contains user guides on how to install, set up, configure, and use Docker products.


## [AI and agents](https://docs.docker.com/manuals#ai-and-agents)


All the Docker AI tools in one easy-to-access location.

[### Docker Agentic Platform Run agents in cloud sandboxes with this experimental platform.](https://docs.docker.com/agentic-platform/) [### Docker Sandboxes Run AI coding agents in isolated environments.](https://docs.docker.com/ai/sandboxes/) [### Sandboxes API and SDK Create and manage cloud sandboxes from your applications.](https://docs.docker.com/ai/sandboxes-api/) [### MCP Catalog and Toolkit Augment your AI workflow with MCP servers.](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) [### Gordon Streamline your workflow and get the most out of the Docker ecosystem with your personal AI assistant.](https://docs.docker.com/ai/gordon/) [### Docker Model Runner View and manage your local models.](https://docs.docker.com/ai/model-runner/) [### Docker Agent The open-source multi-agent solution to assist you in your tasks.](https://docs.docker.com/ai/docker-agent) [### Docker Skills Docker's official skills for AI coding agents.](https://docs.docker.com/ai/skills/)

## [Application development](https://docs.docker.com/manuals#application-development)


End-to-end developer solutions for innovative teams.

[### Docker Desktop Your command center for container development.](https://docs.docker.com/desktop/) [### Docker Offload Build and run containers in the cloud.](https://docs.docker.com/offload/) [### Docker Build Cloud Build your images faster in the cloud.](https://docs.docker.com/build-cloud/) [### Testcontainers Run containers programmatically in your preferred programming language.](https://docs.docker.com/testcontainers/) [### Docker Build Build and ship any application anywhere.](https://docs.docker.com/build/) [### Docker Engine The industry-leading container runtime.](https://docs.docker.com/engine/) [### Docker Compose Define and run multi-container applications.](https://docs.docker.com/compose/)

## [Supply chain security](https://docs.docker.com/manuals#supply-chain-security)


Security guardrails and image analysis for your software supply chain.

[### Docker Hub Discover, share, and integrate container images.](https://docs.docker.com/docker-hub/) [### Docker Hardened Images Secure, minimal images for trusted software delivery.](https://docs.docker.com/dhi/) [### Docker Scout Image analysis and policy evaluation.](https://docs.docker.com/scout/)

## [Accounts and admin](https://docs.docker.com/manuals#accounts-and-admin)


Manage Docker accounts, administration, subscriptions, billing, and security.

[### Accounts Manage Docker individual and organization accounts.](https://docs.docker.com/accounts/) [### Subscription and billing Manage Docker subscriptions, plans, billing, and payments.](https://docs.docker.com/subscription-billing/) [### Security Security guardrails for both administrators and developers.](https://docs.docker.com/security/) [### FAQs Frequently asked questions about Docker accounts, organizations, companies, subscriptions, billing, and security.](https://docs.docker.com/faqs/) [### Support Support options for paid subscriptions and community resources.](https://docs.docker.com/support/) [### Release notes Features, bug fixes, and breaking changes for Docker Home, billing, security, and subscriptions.](https://docs.docker.com/platform-release-notes/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Sign up for Docker Agentic Platform

`https://docs.docker.com/agentic-platform/signup`

# Sign up for Docker Agentic Platform


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


> Note
>
> Docker Agentic Platform is experimental. Features and behavior may change.


To use Docker Agentic Platform or run cloud sandboxes through the CLI, API, or SDKs, activate a Docker Agentic Platform pay-as-you-go subscription. The same subscription provides cloud access for all these interfaces.


## [Before you begin](https://docs.docker.com/agentic-platform/signup#before-you-begin)


Subscribe using your personal Docker account. You can use this account even if you belong to an organization. The Docker Agentic Platform subscription is attached to your personal account and billed separately from your Docker subscription. Review the [billing details](https://docs.docker.com/agentic-platform/signup#billing) before subscribing.


## [Activate cloud access](https://docs.docker.com/agentic-platform/signup#activate-cloud-access)


1. Open the [Docker Agentic Platform Console](https://agentic-platform.docker.com/) and sign in with the Docker account you want to use for cloud sandboxes.
2. If your account doesn't have access, follow the redirect to Docker Billing. Review the Docker Agentic Platform pay-as-you-go plan, provide the requested billing and payment details, and complete checkout. If you see **Docker Agentic Platform access required** instead of a redirect, select **Go to Docker Billing** to subscribe.
3. Return to the Console after checkout. If your account already has an active subscription, you can skip checkout.


To create a sandbox in the Console, follow [Get started](https://docs.docker.com/agentic-platform/get-started/). Use the same Docker account for CLI sign-in or API authentication that you used to subscribe. Agent credentials are configured separately from subscription activation; follow your interface's instructions to set them up.


## [Check account access](https://docs.docker.com/agentic-platform/signup#check-account-access)


If the Console, CLI, or API reports that your account doesn't have access, confirm that checkout completed and that you're using the account with the active subscription. You can review the plan in Docker Home under **Billing** > **Active subscriptions** > **Docker Agentic Platform**.


## [Billing](https://docs.docker.com/agentic-platform/signup#billing)


Cloud sandboxes use pay-as-you-go compute with no recurring subscription fee. Docker meters compute in seconds, based on sandbox runtime and the CPU and memory configuration. Your model provider bills inference separately.


Open [Usage & billing](https://agentic-platform.docker.com/usage) in the Console to review pricing, usage, and available credits. Compute credits offset eligible cloud compute usage; they don't cover model-provider charges.


Billing is monthly, on the day you subscribed. Your invoice reflects usage accrued during the previous billing period. Stop or delete sandboxes you no longer need.


For instructions on reviewing your plan, billing dates, and cancellation, see [Docker Agentic Platform plans](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform/).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Get started with local Docker Sandboxes

`https://docs.docker.com/ai/sandboxes/get-started`

# Get started with local Docker Sandboxes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This walkthrough uses local sandboxes. For cloud credentials and a first cloud session, see [Get started with cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/#get-started).


Docker Sandboxes run AI coding agents in isolated microVM sandboxes. Each sandbox gets its own Docker daemon, filesystem, and network — the agent can build containers, install packages, and modify files without accessing host resources beyond those you share.


This page walks through your first session: run an agent in a sandbox, see how the sandbox isolates it, control what it can reach on the network, and clean up.


## [Prerequisites](https://docs.docker.com/ai/sandboxes/get-started#prerequisites)


- [Install the `sbx` CLI](https://docs.docker.com/ai/sandboxes/install/) and sign in to Docker
- Configure an authentication method for the agent you want to use. Most agents require an API key for their model provider. See the [agent pages](https://docs.docker.com/ai/sandboxes/agents/) for provider-specific instructions.


## [Authenticate your agent](https://docs.docker.com/ai/sandboxes/get-started#authenticate-your-agent)


For Claude Code with a Claude subscription (Max, Team, or Enterprise), no upfront setup is needed — use the `/login` command inside the sandbox to sign in with OAuth. The session token stays on your host and is never stored inside the sandbox.


If you prefer to authenticate with an API key, see [Credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/) for how to store one with `sbx secret set`.


To give the agent access to GitHub for creating pull requests or interacting with repositories:


```console
$ sbx secret set github --command 'gh auth token'
```


## [Run your first sandbox](https://docs.docker.com/ai/sandboxes/get-started#run-your-first-sandbox)


Pick a project directory and launch an agent with [`sbx run`](https://docs.docker.com/reference/cli/sbx/run/):


```console
$ cd ~/my-project
$ sbx run --name my-sandbox claude
```


The first time you run a sandbox, the CLI prompts you to choose a default network preset:


```text
Initialize the global network policy for your sandboxes:

  Applies to all sandboxes, current and future — change it later with
  "sbx policy allow/deny/rm". Kits, including built-in agent kits, may
  also add per-sandbox rules.

     1. Open         — All network traffic allowed, no restrictions.
  ❯  2. Balanced     — Default deny, with common dev sites allowed.
     3. Locked Down  — All network traffic blocked unless you allow it.

  Use ↑/↓ or 1–3 to navigate, Enter to confirm, Esc to cancel.
```


**Balanced** is a good starting point — it permits traffic to common development services while blocking everything else. You can adjust individual rules later. See [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/) for a full description of each option.


Replace `claude` with the agent you want to use — see [Agents](https://docs.docker.com/ai/sandboxes/agents/) for the full list.


The first run takes a little longer while the agent image is pulled. Subsequent runs reuse the cached image and start in seconds.


This attaches you to the agent running inside the sandbox. Give it a real task — ask it to add a feature, install a dependency, or build and run your project. The agent has a full Linux environment with its own Docker daemon, so it can install packages, build images, and start containers on its own while it works.


*Pick a project directory and launch an agent with
sbx run:*

*Replace claude with the agent you want to use — see Agents for the
full list.*

## [See what the agent can touch](https://docs.docker.com/ai/sandboxes/get-started#see-what-the-agent-can-touch)


From another terminal, list your sandboxes:


```console
$ sbx ls
SANDBOX      AGENT    STATUS      PORTS   WORKSPACE      CREATED
my-sandbox   claude   ● running           ~/my-project   2m
```


Each row shows a sandbox's name, agent, status, [published ports](https://docs.docker.com/ai/sandboxes/usage/#publish-ports), workspace, and age. The workspace is the host directory shared into the sandbox and the one part of your machine the agent can see.


When you run `sbx run` from a project directory without passing a workspace path, the current directory is mounted read-write. The agent and your host see the same files. Edits the agent makes to your project appear in your working tree as it writes them, and you review them as an ordinary Git diff before committing.


Everything else runs inside the microVM, isolated from your host:


- The agent has its own filesystem, Docker daemon, and network.
- Packages it installs, images it pulls, and containers it starts stay inside the sandbox. Your host system is untouched, and removing the sandbox discards them.


If you'd rather the agent not touch your working tree at all — for example, when running several agents on one repository — use [clone mode](https://docs.docker.com/ai/sandboxes/usage/#clone-mode), which gives it a private clone instead.


## [Control what the agent can reach](https://docs.docker.com/ai/sandboxes/get-started#control-what-the-agent-can-reach)


Isolation isn't only about the filesystem. You also control what the sandbox can reach on the network. You chose a default policy before the sandbox started, and you can inspect or adjust it at any time.


Check which rules are in effect:


```console
$ sbx policy ls
```


To allow a specific host:


```console
$ sbx policy allow network registry.npmjs.org
```


With **Locked Down**, even your model provider API is blocked unless you explicitly allow it. With **Balanced**, common development services are permitted by default. See [local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/) for the full rule set and how to customize it.


## [Clean up](https://docs.docker.com/ai/sandboxes/get-started#clean-up)


Sandboxes persist after the agent exits, so you can stop one and pick up where you left off later:


```console
$ sbx stop my-sandbox
```


Installed packages, Docker images, and configuration changes are preserved across restarts. When you're done with a sandbox, remove it to reclaim disk space:


```console
$ sbx rm my-sandbox
```


Removing a sandbox deletes everything inside it — installed packages, Docker images, and the in-sandbox Git clone if you used clone mode. Files in your host working tree are unaffected.


## [What's next](https://docs.docker.com/ai/sandboxes/get-started#whats-next)


You've run an agent, seen how the sandbox isolates it, and controlled its network access. A few directions from here.


Run `sbx` with no arguments to open the interactive dashboard: a live view of every sandbox where you can attach to agents, open shells, and manage network rules from one place.

![The interactive dashboard showing sandbox status, resource usage, and network governance controls.](https://docs.docker.com/ai/sandboxes/images/sbx-dashboard.png)


Then explore:


- [Usage guide](https://docs.docker.com/ai/sandboxes/usage/) — basic commands, reconnecting, workspaces, and port publishing.
- [Workflow patterns](https://docs.docker.com/ai/sandboxes/workflows/) — Git strategies, local services, CI, and authenticated tools.
- [Sandbox environment files](https://docs.docker.com/ai/sandboxes/configuration/environment-files/) — declare and share repeatable local sandbox configurations with `sbxenv.yaml`.
- [Customize with kits](https://docs.docker.com/ai/sandboxes/customize/) — package an agent, its tools, and its network rules into a reusable definition you launch with a single flag.
- [Agents](https://docs.docker.com/ai/sandboxes/agents/) — the full list of supported agents and how to configure each one.
- [Governance](https://docs.docker.com/ai/sandboxes/governance/) — centrally manage network, filesystem, and MCP policies across a team.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Install Docker Sandboxes

`https://docs.docker.com/ai/sandboxes/install`

# Install Docker Sandboxes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Install the `sbx` CLI to run AI coding agents in local or cloud sandboxes. You don't need Docker Desktop or Docker Engine to use `sbx`. Cloud sandboxes require version 0.45.0 or later for the workflows in these guides.


## [Prerequisites](https://docs.docker.com/ai/sandboxes/install#prerequisites)


The operating system and processor requirements apply to the CLI installation. Hypervisor and KVM setup is required only to run local sandboxes. For cloud account requirements, see [Cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/#prerequisites).


### [macOS](https://docs.docker.com/ai/sandboxes/install#macos)


- macOS Sonoma version 14 or later
- Apple silicon


### [Windows](https://docs.docker.com/ai/sandboxes/install#windows)


- Windows 11
- A 64-bit Intel or AMD processor
- Windows Hypervisor Platform for local sandboxes


To run local sandboxes, open an elevated PowerShell prompt and turn on Windows Hypervisor Platform:


```powershell
Enable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -All
```


### [Linux](https://docs.docker.com/ai/sandboxes/install#linux)


- Ubuntu 24.04 or later
- A 64-bit Intel or AMD processor, or a 64-bit Arm processor
- For local sandboxes, KVM hardware virtualization supported and turned on by the CPU, and your user account in the `kvm` group


To run local sandboxes inside a virtual machine or virtual desktop infrastructure environment, the environment must support nested virtualization. Cloud sandboxes don't require this setup.


For local sandboxes, verify that KVM is available:


```console
$ lsmod | grep kvm
```


A working setup shows `kvm_intel`, `kvm_amd`, `kvm_arm64`, or `kvm` in the output. If the output is empty, run `kvm-ok` for diagnostics. The local sandbox runtime requires KVM to start.


Add your user to the `kvm` group:


```console
$ sudo usermod -aG kvm $USER
```


Sign out and back in, or run `newgrp kvm`, for the group change to take effect.


*Add your user to the kvm group:*

*Sign out and back in, or run newgrp kvm, for the group change to take effect.*

## [Install on macOS](https://docs.docker.com/ai/sandboxes/install#install-on-macos)


Install `sbx` using Homebrew:


```console
$ brew trust docker/tap
$ brew install docker/tap/sbx
```


*Install sbx using Homebrew:*

## [Install on Windows](https://docs.docker.com/ai/sandboxes/install#install-on-windows)


### [Install for the current user](https://docs.docker.com/ai/sandboxes/install#install-for-the-current-user)


Install `sbx` using Windows Package Manager:


```powershell
winget install -h Docker.sbx
```


WinGet installs the per-user `DockerSandboxes.msi` package in `%LOCALAPPDATA%\DockerSandboxes` and adds its `bin` directory to your user `PATH`. You can install it without administrator privileges.


### [Install for all users](https://docs.docker.com/ai/sandboxes/install#install-for-all-users)


For administrator-managed deployments, download `DockerSandboxesMachine.msi` from the [Docker Sandboxes releases](https://github.com/docker/sbx-releases/releases). From an elevated PowerShell prompt, install the package silently:


```powershell
msiexec.exe /i DockerSandboxesMachine.msi /quiet
```


The machine-wide package installs in `%ProgramFiles%\DockerSandboxes` and adds its `bin` directory to the system `PATH`.


A machine-wide upgrade might require restarting Windows if an `sbx` daemon in another user's session is using the installed files.


*Install sbx using Windows Package Manager:*

## [Install on Ubuntu](https://docs.docker.com/ai/sandboxes/install#install-on-ubuntu)


> Note
>
> Docker does not test or support Docker Sandboxes on Ubuntu derivatives, such as Linux Mint and Pop!_OS. The convenience script can configure an incorrect package repository on these distributions.


You can install `sbx` with Docker Engine or install only the `sbx` package.


### [Install Docker Engine and SBX](https://docs.docker.com/ai/sandboxes/install#install-docker-engine-and-sbx)


Run Docker's convenience script with `SBX=1` to install Docker Engine and the `docker-sbx` package together:


```console
$ curl -fsSL https://get.docker.com | sudo SBX=1 sh
```


### [Install SBX only](https://docs.docker.com/ai/sandboxes/install#install-sbx-only)


To install `sbx` without Docker Engine on the host, add Docker's `apt` repository and install the `docker-sbx` package:


```console
$ curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh
$ sudo apt install docker-sbx
```


*You can install sbx with Docker Engine or install only the sbx package.*

## [Install from release artifacts](https://docs.docker.com/ai/sandboxes/install#install-from-release-artifacts)


To install `sbx` from a package or archive, follow the [manual installation instructions](https://github.com/docker/sbx-releases#manual-install-from-release-artifacts). The availability of a Linux release artifact does not indicate that Docker tests or supports the corresponding distribution.


## [Sign in](https://docs.docker.com/ai/sandboxes/install#sign-in)


Sign in to Docker:


```console
$ sbx login
```


The command opens a browser for Docker OAuth. See the [FAQ](https://docs.docker.com/ai/sandboxes/faq/) for why sign-in is required and how Docker handles your data.


After signing in, [run your first local sandbox](https://docs.docker.com/ai/sandboxes/get-started/) or [get started with cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/#get-started).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Sandboxes API and SDK

`https://docs.docker.com/ai/sandboxes-api`

# Docker Sandboxes API and SDK


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Use the Docker Sandboxes API to create cloud sandboxes, run commands, and transfer files from your applications and automated workflows. You can also manage related resources, including images, snapshots, volumes, and secrets.


To try it, [run your first cloud sandbox](https://docs.docker.com/ai/sandboxes-api/get-started/) with the TypeScript SDK. The tutorial uses a bundled kit that supplies a shell environment for running commands.


## [Activate cloud access](https://docs.docker.com/ai/sandboxes-api#activate-cloud-access)


To use the API or SDK, [activate a Docker Agentic Platform subscription](https://docs.docker.com/agentic-platform/signup/#activate-cloud-access). Use the same Docker account to [authenticate your application](https://docs.docker.com/ai/sandboxes-api/authentication/).


Cloud compute is billed separately from your Docker subscription. See [Billing](https://docs.docker.com/agentic-platform/signup/#billing) for details.


## [Choose an interface](https://docs.docker.com/ai/sandboxes-api#choose-an-interface)


Use the TypeScript SDK in your JavaScript or TypeScript application. The SDK provides typed requests and responses, waits for sandboxes to start or stop, and handles file transfers and interactive processes. See [Install the SDK](https://docs.docker.com/ai/sandboxes-api/install/) for installation instructions.


You can also call the REST API directly from any language or HTTP tool. See the [API reference](https://docs.docker.com/reference/api/sandboxes/latest/) for operations, request fields, responses, and the downloadable OpenAPI specification.


To run agents from your terminal, see [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/).


*To run agents from your terminal, see Docker Sandboxes.*

## [Develop your application](https://docs.docker.com/ai/sandboxes-api#develop-your-application)


- [SDK cookbook](https://docs.docker.com/ai/sandboxes-api/cookbook/): follow examples for processes, files, storage, networking, and other sandbox operations.
- [API concepts](https://docs.docker.com/ai/sandboxes-api/concepts/): choose a kit or image, identify resources, and wait for actions to finish.
- [Authentication and authorization](https://docs.docker.com/ai/sandboxes-api/authentication/): authenticate requests and understand which permissions your application needs.
- [Errors and retries](https://docs.docker.com/ai/sandboxes-api/errors/): handle failures and retry requests without duplicating work.
- [Compute sizes and limits](https://docs.docker.com/ai/sandboxes-api/limits/): choose resources and handle account quotas and request rate limits.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Compare local and cloud sandboxes

`https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud`

# Compare local and cloud sandboxes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Local and cloud sandboxes provide isolated environments for AI agents, but they run against different resources and stores. This comparison helps you choose an environment and identify workflows that need cloud-specific setup.


| Capability | Local sandbox | Cloud sandbox |
| --- | --- | --- |
| Compute | Uses resources from the host | Uses Docker-managed cloud resources |
| CPU architecture | Uses the platform supported by the local runtime | Supports `linux/amd64` and `linux/arm64`, subject to account availability; moves must retain the source platform |
| Workspace | Mounts host paths or uses a private Git clone backed by the host repository | Has no access to host paths; transfer files or clone a repository inside the sandbox |
| Hardware | Can use supported host integrations, such as GPU, USB, display, and nested virtualization | Has no access to host hardware |
| Ports | Binds sandbox ports to host addresses and ports | Exposes a sandbox port through a public HTTPS URL |
| Secrets | Reads from the local `sbx` secret store | Reads from the separate `sbx --cloud` secret store |
| Network policy | Uses local and organization policy sources supported by the local runtime | Uses separate, network-only account and sandbox policy; local policies aren't copied |
| MCP servers | Uses servers registered in the local MCP store | Uses servers connected through Docker Agentic Platform |
| Storage | Persists in the local sandbox and its attached host resources | Persists in the cloud sandbox and optional cloud volumes |
| Lifetime | Persists across stops until you remove it | Expires according to its time-to-live and timeout action |
| Billing | No metered sandbox compute charge | [Pay-as-you-go compute](https://docs.docker.com/agentic-platform/signup/#billing) |


If your workflow runs Docker inside the sandbox, review the [Docker exec and healthcheck limitation](https://docs.docker.com/ai/sandboxes/cloud/usage/#docker-exec-and-healthchecks). It can affect container setup, debugging, and Compose service readiness.


## [Host-dependent features](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud#host-dependent-features)


A cloud sandbox has no path back to the machine where you run `sbx`. The following local features don't apply in cloud mode:


- Workspace paths, bind mounts, `--clone`, and Git worktrees created with `--branch`
- GPU, USB, display, and nested virtualization options
- Model selection through `--model` and `--provider`
- Host port bindings
- Host-backed agent skills and the full local MCP management workflow


The CLI rejects local-only flags used with `--cloud` instead of ignoring them.


You can use [environment files](https://docs.docker.com/ai/sandboxes/configuration/environment-files/#use-a-cloud-environment) with `sbx --cloud env`. Cloud environments support a subset of the local configuration fields, including agents, environment variables, resource limits, and credentials. Remove host workspace and port mappings before using a local environment file in the cloud.


*The CLI rejects local-only flags used with --cloud instead of ignoring them.*

## [Separate resources](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud#separate-resources)


Adding `--cloud` changes the backend for the command. A sandbox shown by `sbx ls` doesn't appear in `sbx --cloud ls`, and resources created for one backend don't automatically become available to the other.


This separation applies to sandboxes, templates, secrets, volumes, and network policy. Use [`sbx move`](https://docs.docker.com/ai/sandboxes/cloud/move/) when you need to copy a sandbox filesystem between backends. Moving doesn't unify the resource stores or transfer host-mounted files or managed secrets. Credentials saved in copied files can still travel with the sandbox.


## [Network policy differences](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud#network-policy-differences)


Configure and verify [cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) separately. Moving a sandbox doesn't carry its local policy configuration into the cloud. The cloud CLI supports account and sandbox network rules, but rejects local governance profiles and the `--protocol` option.


HTTP method and path restrictions, also called L7 filtering, aren't supported in cloud sandboxes. If these rules apply to a local sandbox, `sbx move` warns and asks for confirmation before moving it to the cloud.


## [What changes when you move](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud#what-changes-when-you-move)


[`sbx move`](https://docs.docker.com/ai/sandboxes/cloud/move/) copies a filesystem snapshot and creates a separate destination sandbox. It doesn't transfer running processes or memory, and it leaves the source sandbox in place. Large images can take time to upload or download, depending on image size and available bandwidth. For cloud-to-local moves, also allow for [temporary disk space](https://docs.docker.com/ai/sandboxes/cloud/move/#move-from-cloud-to-local).


| State | Local to cloud | Cloud to local | What to do |
| --- | --- | --- | --- |
| Network policy | Local rules aren't copied; the CLI warns that cloud policy applies | Cloud rules aren't copied; the CLI notice explains that the host's default egress policy applies | Configure destination rules and verify allowed and blocked connections before continuing work |
| Managed secrets | Uses applicable credentials in the cloud secret store | Uses applicable credentials in the local secret store | Configure credentials in the destination store; the CLI warns that secrets aren't copied and you may need to sign in again |
| Workspace and attached storage | Host mounts and clone-mode volumes aren't copied; a workspace triggers a warning and confirmation | Cloud volumes aren't copied and no host folder is mounted | Transfer needed files separately with `sbx cp` |
| Published ports | TCP ports get cloud URLs; refused ports are skipped with a warning | Ports use local loopback bindings; cloud URLs aren't retained | Inspect destination ports and update clients |
| CPU and memory | Rounds recorded source limits up to a supported cloud size; missing limits use defaults with a warning | Uses local defaults | Check destination resources and workload performance; `sbx move` has no CPU or memory override flags |
| CPU architecture | Cloud access must support the source platform | The local runtime must support the source platform | Match platforms; the CLI checks compatibility before transfer |


The managed-secret warning doesn't itself block a move. Configure [cloud credentials](https://docs.docker.com/ai/sandboxes/cloud/credentials/) or [local credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/) before using an agent that needs them. Credentials written to files inside the sandbox can be included in the snapshot; remove those files before moving if you don't want the credentials copied.


Cloud-to-local moves display a notice and ask for confirmation. Local-to-cloud moves ask for confirmation when workspace files or L7 filtering would be left behind. If a confirmation is required and standard input isn't a terminal, the move fails unless you pass `--force`. This flag skips confirmation but retains warnings and doesn't change what transfers.


Verify the destination's files, credentials, network access, ports, and [expiration settings](https://docs.docker.com/ai/sandboxes/cloud/usage/#configure-expiration) before removing the source.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Workflow patterns

`https://docs.docker.com/ai/sandboxes/workflows`

# Workflow patterns


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Choose a workflow based on how you want to develop, authenticate tools, or run local sandboxes in automation. For command syntax and lifecycle basics, see [Usage](https://docs.docker.com/ai/sandboxes/usage/).


## [Choose how code moves](https://docs.docker.com/ai/sandboxes/workflows#choose-how-code-moves)


Your workspace strategy determines when an agent's changes appear on the host. Direct mode edits the host working tree in place. Clone mode keeps changes in a private clone until you fetch or push them. Host worktrees provide branch isolation while keeping Git operations on the host. See [Git workflows](https://docs.docker.com/ai/sandboxes/workflows/git/) to choose a strategy for single or parallel tasks.


## [Develop in the sandbox](https://docs.docker.com/ai/sandboxes/workflows#develop-in-the-sandbox)


Each sandbox has a private Docker daemon and runtime for building images, installing dependencies, and running tests. You can publish services from the sandbox or connect to services on the host. See [Develop and test locally](https://docs.docker.com/ai/sandboxes/workflows/development/).


Tools inside the sandbox can use credentials configured on the host without copying secret values into the VM. See [Authenticate command-line tools](https://docs.docker.com/ai/sandboxes/workflows/authentication/) for GitHub CLI, registry, and external secret-provider workflows.


## [Reuse and automate workflows](https://docs.docker.com/ai/sandboxes/workflows#reuse-and-automate-workflows)


Sandbox environment files work like Compose files for sandboxes: they capture project configuration in a versioned YAML file. Use `sbxenv.yaml` to define the agent, workspaces, tools, resources, credentials, and ports so contributors can start a consistent environment without reproducing CLI flags and setup steps. See [Sandbox environment files](https://docs.docker.com/ai/sandboxes/configuration/environment-files/).


You can also add skills from Git repositories or import them from supported host agents into a persistent store shared with new sandboxes. See [Share agent skills](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/).


For unattended jobs, use headless authentication and manage the sandbox lifecycle from scripts. See [Run sandboxes in CI](https://docs.docker.com/ai/sandboxes/workflows/automation/).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Supported agents

`https://docs.docker.com/ai/sandboxes/agents`

# Supported agents


Ask Gordon


Copy Markdown


View Markdown

---


---


Docker Sandboxes runs the following agents in local sandboxes:


- [Claude Code](https://docs.docker.com/ai/sandboxes/agents/claude-code/)
- [Codex](https://docs.docker.com/ai/sandboxes/agents/codex/)
- [Copilot](https://docs.docker.com/ai/sandboxes/agents/copilot/)
- [Cursor](https://docs.docker.com/ai/sandboxes/agents/cursor/)
- [Devin](https://docs.docker.com/ai/sandboxes/agents/devin/)
- [Docker Agent](https://docs.docker.com/ai/sandboxes/agents/docker-agent/)
- [Droid](https://docs.docker.com/ai/sandboxes/agents/droid/)
- [Gemini](https://docs.docker.com/ai/sandboxes/agents/gemini/)
- [Kiro](https://docs.docker.com/ai/sandboxes/agents/kiro/)
- [OpenCode](https://docs.docker.com/ai/sandboxes/agents/opencode/)
- [Shell](https://docs.docker.com/ai/sandboxes/agents/shell/) — agent-less sandbox for manual setup or testing


Want to pre-install tools or customize an agent's environment? See [Customize](https://docs.docker.com/ai/sandboxes/customize/).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Configure Docker Sandboxes

`https://docs.docker.com/ai/sandboxes/configuration`

# Configure Docker Sandboxes


Ask Gordon


Copy Markdown


View Markdown

---


---


Configure credentials and how Docker Sandboxes run for a project, host, or network environment. These settings control sandbox creation, authentication, and connectivity. To change the tools and agent configuration inside a sandbox, see [Customize](https://docs.docker.com/ai/sandboxes/customize/).


- [Settings](https://docs.docker.com/ai/sandboxes/configuration/settings/) lists host-level settings, environment variable equivalents, and commands to inspect and change values.
- [Credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/) configures API keys, authentication credentials, and registry access for sandboxed agents.
- [Models](https://docs.docker.com/ai/sandboxes/configuration/models/) selects local models, hosted providers, or custom inference endpoints for sandboxed agents.
- [Environment files](https://docs.docker.com/ai/sandboxes/configuration/environment-files/) declare reusable project configuration in `sbxenv.yaml` for local or cloud sandboxes.
- [GPU passthrough](https://docs.docker.com/ai/sandboxes/configuration/gpu-passthrough/) configures a Linux host and sandbox for NVIDIA GPU workloads.
- [Registry mirror](https://docs.docker.com/ai/sandboxes/configuration/registry-mirror/) routes Docker Hub template, kit, and in-sandbox Docker image pulls through an organization's registry mirror.
- [Upstream proxy](https://docs.docker.com/ai/sandboxes/configuration/upstream-proxy/) routes sandbox and daemon traffic through an operating system or corporate proxy.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Editor and app integrations

`https://docs.docker.com/ai/sandboxes/integrations`

# Editor and app integrations


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Availability:
GA
Requires:
Docker Sandboxes 0.37.0 or later


These integrations use local sandbox SSH access. Cloud sandboxes use a different SSH configuration and address: see [Connect with SSH](https://docs.docker.com/ai/sandboxes/cloud/usage/#connect-with-ssh).


You can connect an external editor or desktop app to a running sandbox over SSH. This lets you use the tools you already know — VS Code, Cursor, Claude Desktop, and others — while your code runs, builds, and executes inside the isolated sandbox instead of on your host.


Each sandbox is reachable at `<name>.sbx`, where `<name>` is the sandbox name. Once SSH is set up, `<name>.sbx` behaves like any other SSH host, so any tool that supports remote development over SSH can connect to it.


## [Prerequisites](https://docs.docker.com/ai/sandboxes/integrations#prerequisites)


- The `sbx` CLI installed and signed in. See [Get started](https://docs.docker.com/ai/sandboxes/get-started/).
- An SSH client. macOS and most Linux distributions include OpenSSH. On Windows, install the OpenSSH client.
- The editor or app you want to connect, with its remote-over-SSH support installed.


## [Enable SSH access](https://docs.docker.com/ai/sandboxes/integrations#enable-ssh-access)


Run the SSH setup command once:


```console
$ sbx setup ssh
```


The command starts the Docker Sandboxes daemon if needed and configures your SSH client. You can re-run it at any time.


## [Set up desktop app connections](https://docs.docker.com/ai/sandboxes/integrations#set-up-desktop-app-connections)


On macOS and Windows, Docker Sandboxes can add connections to ChatGPT and Claude Desktop that create a dedicated sandbox on first use. This workflow uses a workspace inside the sandbox. To work directly on a mounted host project, [create a sandbox](https://docs.docker.com/ai/sandboxes/integrations#create-or-identify-a-sandbox) and connect to its hostname instead.


This setup requires Docker Sandboxes v0.48.0 or later. Launch each installed app at least once, then quit the apps before running:


```console
$ sbx setup ssh --auto-create
```


Setup adds the following connections to the apps and configures their SSH hostnames. It creates the sandboxes when the connections are used.


| App | Connection name | SSH hostname | Sandbox name |
| --- | --- | --- | --- |
| ChatGPT | Docker Sandbox (Codex) | `codex.sbx` | `ssh-codex` |
| Claude Desktop | Docker Sandbox (Claude) | `claude.sbx` | `ssh-claude` |


Reopen each app and select its added connection. Connecting for the first time creates the corresponding sandbox. Later connections reuse that sandbox and its files, starting it if it is stopped.


These sandboxes have no host workspace mounted. Clone your project inside the sandbox and select its directory in the app's remote folder picker. Changes stay inside the sandbox until you push them to a remote repository or copy them out.


Removing the sandbox with `sbx rm` leaves the app connection available. The next connection creates a replacement sandbox without restoring deleted files.


If setup reports that an app is running, quit it and rerun `sbx setup ssh`. Setup also provides sign-in guidance if Docker or agent authentication is missing.


### [Remove desktop app connections](https://docs.docker.com/ai/sandboxes/integrations#remove-desktop-app-connections)


Quit ChatGPT and Claude Desktop, then run:


```console
$ sbx setup ssh remove
```


This removes the managed SSH config and app connections. It leaves existing sandboxes running or stopped as they were. Remove the sandboxes separately with `sbx rm` if you no longer need them.


## [Create or identify a sandbox](https://docs.docker.com/ai/sandboxes/integrations#create-or-identify-a-sandbox)


To connect using a sandbox name as `<name>.sbx`, create the sandbox first. ChatGPT and Claude Desktop also support [creating a dedicated sandbox on first connection](https://docs.docker.com/ai/sandboxes/integrations#set-up-desktop-app-connections). To create a named shell sandbox for the current directory:


```console
$ sbx create --name demo shell .
```


To identify an existing sandbox, list your sandboxes:


```console
$ sbx ls
```


## [Connect to a sandbox over SSH](https://docs.docker.com/ai/sandboxes/integrations#connect-to-a-sandbox-over-ssh)


Use the sandbox name with the `.sbx` suffix. For example, to connect to a sandbox named `demo`:


```console
$ ssh demo.sbx
```


## [Select the workspace folder](https://docs.docker.com/ai/sandboxes/integrations#select-the-workspace-folder)


Connecting an app to a sandbox selects the remote environment, but it might not open the primary workspace automatically. The initial folder depends on the client. A remote folder picker might open at the sandbox user's home directory, `/home/agent`, while an interactive `ssh` shell might start in `/home/agent/workspace`. Select the intended folder explicitly instead of relying on the initial location.


For a sandbox with a primary workspace, each workspace path appears inside the sandbox at the same absolute path as on the host. For example, if you pass `/Users/bob/src/my-project`, select that path in the remote folder picker. For a mountless sandbox that uses a Docker-provided agent template, select `/home/agent/workspace`.


## [Connect a specific tool](https://docs.docker.com/ai/sandboxes/integrations#connect-a-specific-tool)


- [VS Code](https://docs.docker.com/ai/sandboxes/integrations/vscode/)
- [Cursor](https://docs.docker.com/ai/sandboxes/integrations/cursor/)
- [Claude Desktop](https://docs.docker.com/ai/sandboxes/integrations/claude-desktop/)
- [ChatGPT](https://docs.docker.com/ai/sandboxes/integrations/chatgpt/)
- [T3 Code](https://docs.docker.com/ai/sandboxes/integrations/t3-code/)


## [How SSH connections work](https://docs.docker.com/ai/sandboxes/integrations#how-ssh-connections-work)


### [Managed SSH configuration](https://docs.docker.com/ai/sandboxes/integrations#managed-ssh-configuration)


`sbx setup ssh` writes a managed block to your SSH config: `~/.ssh/config` on macOS and Linux, or `%USERPROFILE%\.ssh\config` on Windows. The block is similar to the following:


```text
# >>> docker sandboxes (managed) >>>
Host *.sbx
    User _default_user_
    ProxyCommand "sbx" ssh proxy %n
    IdentityAgent none
    IdentityFile /dev/null
    IdentitiesOnly yes
    ControlMaster no
    ControlPath none
    UserKnownHostsFile "~/.ssh/sbx_known_hosts"
    KnownHostsCommand "sbx" ssh known-hosts %H
    StrictHostKeyChecking yes
# <<< docker sandboxes (managed) <<<
```


You don't edit this block by hand. Its key entries work as follows:


- `Host *.sbx` maps sandbox hostnames to the sandbox daemon. Application host pickers don't discover individual sandbox names from this wildcard, so enter the hostname, such as `demo.sbx`, manually when you configure an integration.
- `User _default_user_` tells the daemon to use the sandbox image's default user, so your host username is never sent.


### [Connection and authentication](https://docs.docker.com/ai/sandboxes/integrations#connection-and-authentication)


Connections don't use a network port or an SSH key:


- A `ProxyCommand` relays the SSH stream to the daemon over its local socket (a Unix domain socket on macOS and Linux, a named pipe on Windows).
- The daemon accepts the connection only while you have an active Docker login. Authentication is tied to your login, not to a stored key.
- The host key is verified on every connection, so a rotated daemon key never triggers a host-key mismatch.


Because SSH terminates at the daemon, no SSH server runs inside the sandbox. For ordinary `<name>.sbx` connections, create the sandbox first. The [desktop app connections](https://docs.docker.com/ai/sandboxes/integrations#set-up-desktop-app-connections) create their dedicated sandboxes on first use. If a sandbox is stopped, connecting starts it automatically.


### [Environment variables](https://docs.docker.com/ai/sandboxes/integrations#environment-variables)


SSH connections don't forward client environment variables into the sandbox. The daemon acknowledges SSH environment requests for compatibility but ignores their names and values.


### [Port forwarding](https://docs.docker.com/ai/sandboxes/integrations#port-forwarding)


SSH clients can use local port forwarding to make a service listening on the sandbox's loopback interface available on the host. For example, a remote development client can map `127.0.0.1:4321` in the sandbox to `127.0.0.1:55565` on the host, choosing an available host port automatically. Traffic passes through the SSH connection instead of a published Docker port.


The sandbox daemon accepts forwarded connections only to loopback addresses in the sandbox, including `localhost`, `127.0.0.0/8`, and `::1`. The SSH client chooses the bind address for the listener on the host. A listener bound to `127.0.0.1` or `::1` is reachable only from the host. A client configured to bind to a non-loopback address can make the forwarded service reachable from other machines, subject to the host's network and firewall configuration.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# MCP gateway

`https://docs.docker.com/ai/sandboxes/mcp-gateway`

Back [Manuals](https://docs.docker.com/manuals/)


- [Get started](https://docs.docker.com/get-started/)
- [Guides](https://docs.docker.com/guides/)
- [Reference](https://docs.docker.com/reference/)


# MCP gateway


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This page describes the local MCP gateway. Cloud sandboxes use MCP servers configured in Docker Agentic Platform: see [Load an MCP server](https://docs.docker.com/ai/sandboxes/cloud/usage/#load-an-mcp-server).


Docker Sandboxes includes an MCP gateway for connecting agents to Model Context Protocol servers. The gateway gives the agent inside the sandbox one MCP endpoint, while `sbx` manages the registered servers, OAuth credentials, and sandbox lifecycle on the host.


This is different from configuring an MCP server directly in an agent such as Claude Code. Direct MCP setup configures that agent's own MCP client. With Docker Sandboxes, you register MCP servers once on the host, and the sandbox gateway exposes them to supported agents inside isolated sandboxes. That host-managed gateway provides a single path for credentials, explicit server loading, live updates, and organization governance.


> Note
>
> The Docker Sandboxes MCP gateway is separate from the Docker Desktop MCP Toolkit. You don't need the Docker Desktop MCP Toolkit to use `sbx mcp`, and MCP Toolkit server settings aren't shared with Docker Sandboxes.


## [Prerequisites](https://docs.docker.com/ai/sandboxes/mcp-gateway#prerequisites)


- Sign in with `sbx login`.
- Use an agent integration that configures MCP at startup: Claude Code, Codex, Devin, Gemini, Kiro, or OpenCode.
- For remote servers that require OAuth without Dynamic Client Registration, register an OAuth client with the server provider.
- For `--local --url` registrations that resolve to OCI packages, use a host with Docker installed and running. Docker is also required for explicit `--command docker ...` registrations.


## [Quick start](https://docs.docker.com/ai/sandboxes/mcp-gateway#quick-start)


Start by registering one MCP server on the host:


```console
$ sbx mcp add notion --url https://mcp.notion.com/mcp
```


If the server requires OAuth, `sbx` opens an authorization flow before it stores the registration. After registration, verify that the server is registered:


```console
$ sbx mcp ls
```


The listing shows each server's transport, status, gateway, and details.


Then start a sandbox and expose the registered server:


```console
$ sbx run claude --name mcp-demo --static-mcp notion
```


The sandbox starts with an MCP gateway and pre-loads the `notion` server. The registration remains on the host and can be reused by other sandboxes.


## [Register an MCP server](https://docs.docker.com/ai/sandboxes/mcp-gateway#register-an-mcp-server)


`sbx mcp add` registers an MCP server by name. The registration records the server definition on the host. It doesn't attach the server to a sandbox by itself. To expose a registered server to a sandbox, pass it with [`--static-mcp`](https://docs.docker.com/ai/sandboxes/mcp-gateway#use-static-mode) when you create the sandbox, or use [`sbx mcp load`](https://docs.docker.com/ai/sandboxes/mcp-gateway#add-a-server-to-a-running-sandbox) for a sandbox that's already running.


Server names can contain letters, numbers, dots, hyphens, and underscores.


The `--url` flag can point to different kinds of input. The execution location depends on what you register:


- A remote endpoint URL identifies a running MCP server. The server runs remotely, and the sandbox gateway connects to it.
- A metadata URL with `--local` returns a registry entry, `server.json`, or `server.yaml` that describes an OCI-packaged stdio server. `sbx` resolves the image and runs it on the host with Docker.
- An explicit command runs on the host as a stdio MCP server.


Local stdio servers run on the host, not inside the sandbox. The agent inside the sandbox connects only to the MCP gateway.


If a `--url` hostname resolves to a private, loopback, link-local, or cloud metadata address, `sbx` registers the server but warns you about the resolved address. Register only URLs you trust. Fetching a manifest from an untrusted URL can expose internal services or cloud metadata, and DNS rebinding can redirect a hostname after it has been checked.


OAuth metadata discovery also warns and continues when it encounters these addresses, including redirect destinations. For a trusted internal server, pass `--skip-ssrf-check` to skip both the MCP URL check and the OAuth metadata discovery checks and suppress their warnings. Use the flag only when you trust the MCP host, OAuth provider, and all metadata redirect destinations.


### [Remote endpoint URL](https://docs.docker.com/ai/sandboxes/mcp-gateway#remote-endpoint-url)


For a remote MCP endpoint, pass the server URL:


```console
$ sbx mcp add notion --url https://mcp.notion.com/mcp
$ sbx mcp add linear --url https://mcp.linear.app/mcp
```


If requests to a remote server stall, see [MCP server streams stall](https://docs.docker.com/ai/sandboxes/troubleshooting/#mcp-server-streams-stall).


#### [Custom request headers](https://docs.docker.com/ai/sandboxes/mcp-gateway#custom-request-headers)


Use `--header 'Name: value'` to send custom HTTP headers to a remote MCP endpoint, for example to authenticate with an API key. Repeat the flag for each header, using each header name once:


```console
$ sbx mcp add acme --url https://mcp.acme.com/mcp \
  --header 'Authorization: Bearer ${api-key}' \
  --header 'Accept: application/json, text/event-stream'
$ sbx secret set mcp:acme:api-key
```


Replace the example URL with your MCP endpoint. The `sbx secret set` command prompts for the API key and stores it in the [host credential store](https://docs.docker.com/ai/sandboxes/configuration/credentials/#where-secrets-are-stored). The `${api-key}` placeholder stays in the registration. When a sandbox connects, the gateway reads the secret and substitutes its value in the header. Use single quotes around header values so your shell preserves placeholders. Placeholders name stored secrets, not environment variables: `${api-key}` reads `mcp:acme:api-key`, regardless of your shell environment.


Store each placeholder with `sbx secret set mcp:<server>:<placeholder>`. Credential headers such as `Authorization` must use a secret placeholder. An explicit `Authorization` header takes precedence over an OAuth access token.


After storing the secret, expose the server to a sandbox:


```console
$ sbx run claude --name acme-demo --static-mcp acme
```


Custom headers require a remote HTTP endpoint and can't be used with `--command` or `--local`. They also require the host to connect to the server. The hosted gateway rejects these registrations unless you supply `--oauth-authorization-server`, which routes the connection through the host.


#### [Manage header secrets](https://docs.docker.com/ai/sandboxes/mcp-gateway#manage-header-secrets)


Header secrets use the global scope on the host. Set them with `sbx secret set mcp:<server>:<placeholder>` without `--sandbox`. Header secrets require a stored value and don't support `--ref` or `--command` dynamic sources. To check the header templates and whether their secrets are set, run `sbx mcp inspect acme`. The command doesn't display resolved secret values.


The secret store also contains an automatically managed `:endpoint` record, such as `mcp:acme:api-key:endpoint`. This metadata binds the secret to the registered server's URLs so the gateway can detect an endpoint change before sending the secret. You don't need to set this record yourself. If you change the server's endpoint, follow the CLI guidance to set the secret again for that endpoint.


To rotate a header secret, run `sbx secret set` with the same name. After setting, changing, or removing a header secret, stop and restart the sandbox or restart `sandboxd` to apply the change to an existing gateway. An existing connection keeps its previous value, and a server skipped because its secret was missing isn't retried automatically.


Removing a registration with `sbx mcp rm` keeps its header secrets and prints commands to remove them. To remove the example secret:


```console
$ sbx secret rm mcp:acme:api-key
```


### [Local stdio server](https://docs.docker.com/ai/sandboxes/mcp-gateway#local-stdio-server)


Some MCP servers communicate over stdio instead of exposing a remote HTTP endpoint. Use a local stdio server when `sbx` should launch the MCP server on the host. You can provide a metadata URL or an explicit command.


#### [From registry or manifest metadata](https://docs.docker.com/ai/sandboxes/mcp-gateway#from-registry-or-manifest-metadata)


Use `--local --url` when you have an MCP community registry URL or a URL that returns a `server.json` or `server.yaml` document. The registry entry or manifest must describe an OCI package that uses stdio transport. `sbx` doesn't launch non-OCI package types, such as `npm`, from metadata. To use those servers, register an explicit command.


This path resolves the image from the metadata and starts it on the host with Docker, so Docker must be installed and running on the host.


```console
$ sbx mcp add fetch --local \
  --url https://registry.modelcontextprotocol.io/v0/servers/fetch-mcp/versions/latest
```


If the entry doesn't publish an OCI stdio package, `sbx` rejects the registration instead of starting it locally.


A server manifest describes the MCP server package and how to start it. It can be hosted on a GitHub raw URL, internal HTTP server, or CDN.


```console
$ sbx mcp add opine --local --url https://example.com/mcp/opine/server.yaml
```


#### [From an explicit command](https://docs.docker.com/ai/sandboxes/mcp-gateway#from-an-explicit-command)


Use `--command` when you already know the executable and arguments, or when you need custom Docker flags. The command can be a package runner such as `npx` or a Docker container command:


```console
$ sbx mcp add playwright --command npx --args @playwright/mcp@latest
$ sbx mcp add local-image-server --command docker \
  --args "run,-i,--rm,your/image"
```


To set the working directory for the host process, pass `--dir`. This flag is only valid with `--command`:


```console
$ sbx mcp add local-fs --command node --args server.js --dir /srv/data
```


Use registry or manifest metadata when you have a published server definition and don't need to customize `docker run`. Use `--command` for local development, private servers, or custom container flags.


> Warning
>
> Local stdio servers run on the host, outside sandbox isolation. If the command starts a Docker container, that container uses host Docker isolation, not sandbox isolation. The process or container can access host files, host network resources, and credentials made available to it. Use trusted commands and images, and avoid mounting host paths or passing credentials unless the server needs them.


### [Docker Hardened Image](https://docs.docker.com/ai/sandboxes/mcp-gateway#docker-hardened-image)


For an MCP server packaged as a Docker Hardened Image, pass its `dhi.io` reference instead of a registry or manifest URL:


```console
$ sbx mcp add fetch --url dhi.io/fetch-mcp:latest
```


Use a tag or digest: `dhi.io/<IMAGE>:<TAG>` or `dhi.io/<IMAGE>@sha256:<DIGEST>`. For images from other registries, use a server-manifest URL or an [explicit command](https://docs.docker.com/ai/sandboxes/mcp-gateway#from-an-explicit-command).


*If requests to a remote server stall, see
MCP server streams stall.*

## [Authorize OAuth-backed servers](https://docs.docker.com/ai/sandboxes/mcp-gateway#authorize-oauth-backed-servers)


If a registered remote server requires OAuth, `sbx mcp add` starts the authorization flow by default:


```console
$ sbx mcp add notion --url https://mcp.notion.com/mcp
```


OAuth credentials stay on the host. In local gateway mode, `sbx` stores tokens in the host operating system's credential store.


To register an OAuth-backed server without authorizing it, pass `--skip-auth`:


```console
$ sbx mcp add notion --url https://mcp.notion.com/mcp --skip-auth
```


### [Use a pre-registered OAuth client](https://docs.docker.com/ai/sandboxes/mcp-gateway#use-a-pre-registered-oauth-client)


In local gateway mode, you can register a remote OAuth server that doesn't support Dynamic Client Registration. If the server publishes OAuth metadata, pass the client ID that you registered with the server provider:


```console
$ sbx mcp add slack --url https://slack.example.com/mcp \
  --client-id <CLIENT_ID>
```


If the server doesn't publish OAuth metadata, pass `--oauth-authorization-server` with the client ID. The flag accepts a local file path or an HTTP or HTTPS URL to an RFC 8414 authorization server metadata document. The document must define `authorization_endpoint` and `token_endpoint`:


```console
$ sbx mcp add serverx --url https://mcp.serverx.example/mcp \
  --oauth-authorization-server ./serverx-authorization-server.json \
  --client-id <CLIENT_ID>
```


These flags are only valid with `--url`.


For a confidential OAuth client, store the client secret before registering the server. There is no `--client-secret` flag:


```console
$ sbx secret set mcp:slack:client_secret
$ sbx mcp add slack --url https://slack.example.com/mcp \
  --client-id <CLIENT_ID>
```


The client secret stays in the host credential store and isn't written to the MCP registration. If the server requires a confidential client and no secret is stored, registration succeeds but authorization is skipped. Store the secret, then run `sbx mcp auth <server>`.


#### [Change the OAuth client](https://docs.docker.com/ai/sandboxes/mcp-gateway#change-the-oauth-client)


If you re-register a server name with a different client ID, issuer, or token endpoint, `sbx` refuses to use the secret bound to the previous client. After verifying that the registration points to the intended client and provider, store that client's secret, clear the old binding, and authorize:


```console
$ sbx secret set mcp:slack:client_secret
$ sbx secret rm mcp:slack:client_secret:identity
$ sbx mcp auth slack
```


Setting a secret alone doesn't clear the old binding. The `:identity` record is metadata that binds the stored secret to its OAuth client. Authorization records the binding for the new client.


For secrets stored under the legacy name `mcp:<server>.client_secret`, set the secret again using `mcp:<server>:client_secret`.


### [Set OAuth scopes](https://docs.docker.com/ai/sandboxes/mcp-gateway#set-oauth-scopes)


Use the repeatable `--scope` flag to record the default scopes requested during authorization:


```console
$ sbx mcp add serverx --url https://mcp.serverx.example/mcp \
  --scope read --scope write
```


The `sbx mcp auth` command accepts `--scope` to override the recorded defaults for one authorization:


```console
$ sbx mcp auth serverx --scope read
```


Unless you pass `--no-scope`, `sbx` requests the first available scope set in the following order:


1. Scopes passed to `sbx mcp auth --scope`
2. Default scopes recorded by `sbx mcp add --scope`
3. Scopes that the protected resource says it requires
4. Whichever of `openid`, `email`, `profile`, and `offline_access` the authorization server advertises


If none of these provide a scope set, `sbx` omits the OAuth `scope` parameter so the authorization server applies its default grant. Other advertised scopes aren't included in the fallback.


When `sbx` uses recorded defaults or resource-required scopes, it also requests `offline_access` if the authorization server advertises it. The server can then issue a refresh token, so you don't have to authorize again when the access token expires. Scopes passed to `sbx mcp auth --scope` are requested exactly as given, without `offline_access`. Existing credentials issued without a refresh token aren't upgraded; run `sbx mcp auth` again to request a new grant.


Pass `--no-scope` to suppress the recorded defaults, resource-required scopes, and advertised scope fallback for one authorization, without changing the stored defaults:


```console
$ sbx mcp auth serverx --no-scope
```


You can't combine `--no-scope` with `--scope`. Scopes you choose are checked against the authorization server's advertised scopes and the resource's required scopes. If either source publishes scopes, a scope present in neither produces a warning but is still requested. The authorization server can still refuse an advertised scope for a particular client. For a local authorization flow that requested scopes, `sbx` lists the requested, advertised, and refused scopes and suggests a retry command. If the server identifies the refused scopes, the command removes them. Otherwise, it uses `--no-scope`. `sbx` never retries automatically.


For each OAuth-backed remote server exposed to a sandbox, the gateway exposes a helper tool named `<server>-authorize`, such as `notion-authorize`. The agent can call the tool to authorize or reauthorize the server. If the server isn't authorized, the helper is the only tool exposed for that server.


You can manage OAuth credentials from the host:


```console
$ sbx mcp auth status notion
$ sbx mcp auth notion
$ sbx mcp auth rm notion
```


Use `--all` to apply `auth`, `auth status`, or `auth rm` to all registered OAuth-backed servers. The `auth status` output reports the scopes granted by the authorization server, the defaults recorded with `sbx mcp add --scope`, and the scopes the server supports. It collapses duplicate scope names and highlights granted scopes that weren't requested or are no longer in the supported set. Use `--json` for machine-readable output:


```console
$ sbx mcp auth status notion --json
```


### [Override the OAuth resource indicator](https://docs.docker.com/ai/sandboxes/mcp-gateway#override-the-oauth-resource-indicator)


Use `--resource` when your OAuth provider requires a token audience that differs from the resource identifier discovered by `sbx`. By default, `sbx` uses the server's protected-resource metadata, or the endpoint URL if the metadata is absent. Check the value with `sbx mcp inspect <SERVER>` before setting an override:


```console
$ sbx mcp add serverx --url https://mcp.serverx.example/mcp \
  --resource https://api.serverx.example/mcp
```


Use the resource URI supplied by your provider. It must have a scheme and host and no fragment. To change an existing registration's value, remove the registration and add it again.


This override requires OAuth authorization on the host. The hosted gateway doesn't use it unless you also supply `--oauth-authorization-server` or `--client-id` to route authorization through the host. Without those flags, `sbx mcp add` warns that the hosted gateway won't use the override.


*To register an OAuth-backed server without authorizing it, pass --skip-auth:*

*These flags are only valid with --url.*

## [Choose an MCP mode](https://docs.docker.com/ai/sandboxes/mcp-gateway#choose-an-mcp-mode)


Every sandbox starts an MCP gateway. When the sandbox starts, supported agent integrations read the gateway URL and register it with the agent.


Whether you pass `--static-mcp` when you create the sandbox determines its MCP mode:


- Static mode pre-loads the specified servers and doesn't expose dynamic discovery tools to the agent.
- Dynamic mode pre-loads no servers and lets the agent find and attach registered servers.


This choice persists across sandbox restarts unless you [unload every server in the static set](https://docs.docker.com/ai/sandboxes/mcp-gateway#remove-a-server-from-a-running-sandbox).


### [Use static mode](https://docs.docker.com/ai/sandboxes/mcp-gateway#use-static-mode)


Pass `--static-mcp` to pre-load registered MCP servers:


```console
$ sbx mcp add notion --url https://mcp.notion.com/mcp
$ sbx mcp add linear --url https://mcp.linear.app/mcp
$ sbx run claude --name my-session --static-mcp notion,linear
```


You can pass `--static-mcp` as a comma-separated list or repeat the flag:


```console
$ sbx run claude --name my-session \
  --static-mcp notion --static-mcp linear
```


Every name in the static set must already be registered with `sbx mcp add`. The gateway doesn't expose `mcp-find`, `mcp-add`, or `mcp-config-set` to the agent.


You can't replace the initial set by passing `--static-mcp` when reconnecting to an existing sandbox. To attach another server from the host, use [`sbx mcp load`](https://docs.docker.com/ai/sandboxes/mcp-gateway#add-a-server-to-a-running-sandbox).


### [Use dynamic mode](https://docs.docker.com/ai/sandboxes/mcp-gateway#use-dynamic-mode)


Omit `--static-mcp` to use dynamic mode. The gateway pre-loads no servers and exposes `mcp-find`, `mcp-add`, and `mcp-config-set` to the agent. The agent can search the registered server catalog and attach servers during the session.


If you run `sbx mcp add` after a dynamic sandbox starts, its gateway refreshes the searchable catalog. The agent can then find and attach the new registration without restarting. The `sbx mcp add` command doesn't attach the server by itself.


*Pass --static-mcp to pre-load registered MCP servers:*

*You can pass --static-mcp as a comma-separated list or repeat the flag:*

## [Add a server to a running sandbox](https://docs.docker.com/ai/sandboxes/mcp-gateway#add-a-server-to-a-running-sandbox)


To attach an already-registered server to a running sandbox, use `sbx mcp load`. This works in both static and dynamic modes:


```console
$ sbx mcp add linear --url https://mcp.linear.app/mcp
$ sbx mcp load linear --sandbox my-session
```


Connected agent sessions receive a tool-list update, so the added tools become visible without reconnecting. The loaded server remains attached across sandbox restarts.


## [Remove a server from a running sandbox](https://docs.docker.com/ai/sandboxes/mcp-gateway#remove-a-server-from-a-running-sandbox)


In Docker Sandboxes v0.48.0 and later, use `sbx mcp unload` to detach a server from a running sandbox's local MCP gateway. This works in both static and dynamic modes. Cloud sandboxes and hosted MCP gateways don't support unloading servers.


```console
$ sbx mcp unload linear --sandbox my-session
```


Connected agent sessions receive a tool-list update, so the server's tools are removed without restarting the agent. The command also removes the saved attachment so the server isn't restored when the sandbox or daemon restarts. The server's host registration and credentials remain available, and other sandboxes that have loaded the server are unaffected.


To attach the server again:


```console
$ sbx mcp load linear --sandbox my-session
```


In dynamic mode, the agent can also find and attach the registered server again. Unloading a server doesn't prevent the agent from reloading it.


If you unload all servers from a static sandbox, it stays in static mode for the current session. After restarting the Docker Sandboxes daemon and reconnecting, the agent can find and attach registered servers.


## [Built-in gateway tools](https://docs.docker.com/ai/sandboxes/mcp-gateway#built-in-gateway-tools)


The local MCP gateway exposes a small set of built-in tools. These tools belong to the gateway itself, not to a registered MCP server. Agents can see and call them on the same MCP connection as server tools, so they can appear in agent tool lists, logs, policy decisions, audit logs, or approval prompts.


You don't need to call these tools directly for normal setup. Use `sbx mcp` commands to register servers and manage credentials from the host. The tools matter because agents can call them during a session, and admins can govern them separately from tools provided by registered MCP servers.


| Tool | Description |
| --- | --- |
| `mcp-exec` | Executes a tool by name through the gateway. |
| `code-mode` | Creates an ephemeral JavaScript tool that can call selected tools through the MCP gateway. |
| `mcp-find` | Searches the registered server catalog without changing sandbox state. Dynamic mode only. |
| `mcp-add` | Attaches a registered server to the sandbox. Dynamic mode only. |
| `mcp-config-set` | Sets per-session configuration overrides for an attached server. Dynamic mode only. |
| `<server>-authorize` | Starts or restarts OAuth authorization for an exposed OAuth-backed remote server. |


Servers attached with `mcp-add` remain attached across sandbox restarts. The gateway exposes `<server>-authorize` for OAuth-backed remote servers, even when they already have a valid token. Local stdio servers don't expose this helper. If `code-mode` creates a generated tool, the tool is shared by clients connected to the sandbox's gateway and disappears when the gateway is replaced or stops.


In MCP access policies, built-in gateway tools are `MCP::Primordial` resources and use the `invokePrimordial` action. Tools from registered MCP servers are `MCP::Tool` resources and use the `invokeTool` action. For details, see the [MCP policy reference](https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/).


## [Manage registrations](https://docs.docker.com/ai/sandboxes/mcp-gateway#manage-registrations)


List registered servers:


```console
$ sbx mcp ls
```


Inspect a registered server:


```console
$ sbx mcp inspect notion
```


Remove a registered server:


```console
$ sbx mcp rm notion
```


Removing a registration doesn't detach the server from sandboxes that have already loaded it. Use [`sbx mcp unload`](https://docs.docker.com/ai/sandboxes/mcp-gateway#remove-a-server-from-a-running-sandbox) for each sandbox before removing the registration.


For OAuth-backed servers, `sbx mcp rm` removes the OAuth access token before it removes the server registration. A client secret for a pre-registered OAuth client and its identity binding remain in the host credential store so you can reuse them when you re-add the same client. The command prints the `sbx secret rm` commands for removing them. To remove only the OAuth access token, use `sbx mcp auth rm`.


## [Governance](https://docs.docker.com/ai/sandboxes/mcp-gateway#governance)


Organizations with AI Governance can use [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/) to control MCP server registration, tool calls, gateway meta-tools, resources, prompts, and approval requirements. MCP access policies are organization policies written in Cedar.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Architecture

`https://docs.docker.com/ai/sandboxes/architecture`

# Architecture


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This page describes local sandboxes. For cloud behavior and limitations, see [Compare local and cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/).


This page explains how Docker Sandboxes work under the hood. For the security properties of the architecture, see [Sandbox isolation](https://docs.docker.com/ai/sandboxes/security/isolation/).


## [Workspace storage](https://docs.docker.com/ai/sandboxes/architecture#workspace-storage)


Starting with `sbx` version 0.42.0, workspace paths are optional for `sbx create`. When you omit them, the sandbox has no host workspace bind mount. The sandbox uses the template image's configured `WORKDIR` as its default working directory. Docker-provided agent templates set `WORKDIR` to `/home/agent/workspace`. A custom template can set another absolute path. If the daemon can't resolve a usable absolute `WORKDIR` from the image config, it falls back to `/home/agent/workspace`. Files created there stay inside the sandbox and persist across stops and restarts.


When you pass a workspace path to `sbx create` or `sbx run`, the directory is mounted into the sandbox through a filesystem passthrough. `sbx run` uses the current directory when you don't pass a path. The sandbox sees your actual host files, so changes in either direction are instant with no sync process involved.


A directly mounted workspace appears at the same absolute path as on your host. Preserving absolute paths means error messages, configuration files, and build outputs all reference paths you can find on your host. The agent sees the same directory structure, which reduces confusion when debugging or reviewing changes.


Clone mode uses a third storage layout. The host repository is mounted read-only at `/run/sandbox/source`, and the agent works in a private clone inside the sandbox. See [Clone mode](https://docs.docker.com/ai/sandboxes/usage/#clone-mode).


> Warning
>
> Avoid mounting network-attached or remote storage (network drives, SMB/NFS shares, or cloud-synced folders) as a workspace. The sandbox accesses workspaces through a filesystem passthrough, so every file read and write goes over the network. This adds latency and slows agent performance.


## [Storage and persistence](https://docs.docker.com/ai/sandboxes/architecture#storage-and-persistence)


When you create a sandbox, everything inside it persists until you remove it: Docker images and containers built or pulled by the agent, installed packages, agent state and history, and files in mountless or cloned workspaces. Files in a directly mounted workspace live on the host instead.


Each sandbox maintains its own Docker daemon state, image cache, and package installations. Multiple sandboxes don't share images or layers. The [shared agent skills store](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/) is an exception: sandboxes created for supported agents mount the same host-side store read-only by default. Use `--skills` or [`skills.defaultMode`](https://docs.docker.com/ai/sandboxes/configuration/settings/#skillsdefaultmode) to choose another mode at creation. Existing sandboxes retain their mounts until recreated.


Each sandbox consumes disk space for its VM image, Docker images, container layers, and volumes, and this grows as you build images and install packages.


Virtiofs caching is enabled by default for directly mounted workspaces on all operating systems. File reads from the sandbox VM are cached on the host side, reducing round-trips through the filesystem passthrough and improving performance for read-heavy workloads such as `git status` or directory scans. To opt out, set `DOCKER_SANDBOXES_ENABLE_VIRTIOFS_CACHE=0` when creating the sandbox:


```console
$ DOCKER_SANDBOXES_ENABLE_VIRTIOFS_CACHE=0 sbx run <agent>
```


## [Networking](https://docs.docker.com/ai/sandboxes/architecture#networking)


All outbound TCP traffic from the sandbox routes through a proxy on your host. Agents use a forward proxy for HTTP and HTTPS; other TCP traffic is forwarded transparently. Both paths enforce [network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/). The forward proxy also handles [credential injection](https://docs.docker.com/ai/sandboxes/configuration/credentials/). See [Network isolation](https://docs.docker.com/ai/sandboxes/security/isolation/#network-isolation) for how this works and [Default security posture](https://docs.docker.com/ai/sandboxes/security/defaults/) for what is allowed out of the box.


### [Follow an authenticated request](https://docs.docker.com/ai/sandboxes/architecture#follow-an-authenticated-request)


Step through the following diagram to see where Docker Sandboxes checks network policy and replaces a sentinel credential with the real value. The real credential stays outside the sandbox throughout the request.


Follow an authenticated request


Use Next and Previous to follow the request at your own pace, or select a step to jump to it.


Previous
Next

1. The agent prepares the request: The agent sees a sentinel value instead of the real API credential.
2. The request leaves the microVM: Outbound HTTP and HTTPS traffic crosses the sandbox boundary through the host network path.
3. Network policy checks the destination: The request continues only when an active policy permits the provider domain.
4. The proxy retrieves the credential: The host-side proxy resolves the matching credential without copying it into the sandbox.
5. The proxy rewrites the header: The proxy replaces the sentinel with the real credential after the request has left the microVM.
6. The response returns: The provider response returns through the host proxy to the agent. The credential remains on the host.


### [Upstream proxy](https://docs.docker.com/ai/sandboxes/architecture#upstream-proxy)


The host-side proxy makes its outbound connections using your host's network configuration and routing. When a destination is reachable through a direct route, traffic follows that route. When reaching a destination requires an upstream proxy, the host-side proxy forwards the request to it. Chaining to an upstream proxy means sandbox traffic respects the same egress controls as other applications on your host.


By default, both sandbox traffic and the daemon's own traffic follow your OS system proxy, so this usually works without any configuration. To set a proxy explicitly — with a proxy URL, a PAC file, a SOCKS5 proxy, or separate settings for sandbox and daemon traffic — see [Configure an upstream proxy](https://docs.docker.com/ai/sandboxes/configuration/upstream-proxy/). Upstream proxy support is experimental and subject to change.


Only HTTP and HTTPS traffic can be forwarded to an upstream proxy. Other TCP traffic can't be redirected to a proxy.


## [MCP gateway](https://docs.docker.com/ai/sandboxes/architecture#mcp-gateway)


Supported agents connect to a single MCP gateway endpoint for the sandbox. The gateway runs on the host side of the sandbox boundary and brokers access to registered MCP servers.


Registered MCP servers can be remote endpoints, or they can be local stdio servers launched on the host. Local stdio servers don't run inside the sandbox VM. If a local stdio server is packaged as an OCI image, or if you register an explicit `docker` command, it uses Docker on the host.


When MCP policies apply, enforcement happens on the MCP gateway path, separate from the HTTP/HTTPS network proxy. Server registration is checked before the server is stored, and governed MCP requests are checked by the gateway before tool calls, resource reads, prompt retrieval, or gateway meta-tool execution.


## [Lifecycle](https://docs.docker.com/ai/sandboxes/architecture#lifecycle)


`sbx run` initializes a VM for a specified agent and starts the agent. You can stop and restart without recreating the VM, preserving installed packages, Docker images, and in-sandbox files.


Sandboxes persist until explicitly removed. Stopping an agent doesn't delete the VM; environment setup carries over between runs. Use `sbx rm` to delete the sandbox, its VM, and all of its contents. If the sandbox used [`--clone`](https://docs.docker.com/ai/sandboxes/usage/#clone-mode), the `sandbox-<name>` Git remote is also removed from your host repository.


## [Comparison to alternatives](https://docs.docker.com/ai/sandboxes/architecture#comparison-to-alternatives)


| Approach | Isolation | Docker access | Use case |
| --- | --- | --- | --- |
| Sandboxes (microVMs) | Full (hypervisor) | Isolated daemon | Autonomous agents |
| Container with socket mount | Partial (namespaces) | Shared host daemon | Trusted tools |
| [Docker-in-Docker](https://hub.docker.com/_/docker) | Partial (privileged) | Nested daemon | CI/CD pipelines |
| Host execution | None | Host daemon | Manual development |


Sandboxes trade higher resource overhead (a VM plus its own daemon) for complete isolation. Use containers when you need lightweight packaging without Docker access. Use sandboxes when you need to give something autonomous full Docker capabilities without trusting it with your host environment.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Kits

`https://docs.docker.com/ai/sandboxes/customize`

# Kits


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Availability:
Early Access


Kits let you shape a sandbox around the way you work. Use a custom base image, add the tools your project needs, and give your agent instructions for using them. You also control which services the sandbox can access, how it authenticates, and what runs when the sandbox starts.


A kit can define the whole environment or add something to an existing one, such as a toolchain or your team's shared configuration. Package those choices once, then reuse them across projects and share them with your team.


Docker recommends v3 kits. This section covers v3. For the supported v2 format, see [Kits v2](https://docs.docker.com/ai/sandboxes/customize/kits-v2/).


## [What is a kit?](https://docs.docker.com/ai/sandboxes/customize#what-is-a-kit)


A kit packages software and configuration for a sandbox. A YAML file, called its descriptor, tells Docker Sandboxes what the kit needs: network access, credentials, setup commands, or instructions for the agent. You publish the kit as a container image containing its files and descriptor.


You identify a published kit by its container image reference, such as `docker.io/docker/sbx-kit-claude:2.1.267`. When you use the kit, `sbx` prepares its files and applies its settings. You can use one kit for a complete environment or combine kits that contribute different parts.


## [What kits can do](https://docs.docker.com/ai/sandboxes/customize#what-kits-can-do)


Use kits to:


- Package a custom agent, or configure an existing agent for your team's projects.
- Include the tools the agent needs, such as linters, language runtimes, test runners, and compilers.
- Share linter rules, editor settings, helper scripts, and reference material. Give the agent instructions and skills for using them.
- Connect the agent to services through network rules and credentials, including internal APIs and private package registries.
- Initialize each sandbox and run supporting services when it starts, such as a development server for previewing the agent's work.


## [Workloads and mixins](https://docs.docker.com/ai/sandboxes/customize#workloads-and-mixins)


Kits have two roles in a sandbox: a workload supplies the base environment and launch command, and mixins add tools or behavior to it.


| Kind | What it supplies | How you use it |
| --- | --- | --- |
| `workload` | The environment and command to run, such as an agent or a shell | Pass it to `sbx run` or `sbx create` |
| `mixin` | Additional tools, configuration, or runtime behavior | Add it with `--kit` |


For example, this command runs a workload with a mixin:


```console
$ sbx run docker.io/docker/sbx-kit-claude:2.1.267 --kit docker.io/sbx/playwright:1.61.1
```


The Claude Code workload starts the agent, and the Playwright mixin adds browser-testing tools.


## [Kit sets](https://docs.docker.com/ai/sandboxes/customize#kit-sets)


A kit set combines kits into a single kit that you can publish and reuse. Use it to package a workload with the mixins you need, so you and your team can run the environment from one reference.


The set specifies which kits and versions to combine. It can also add setup commands, agent instructions, network access, and other settings for the combined environment.


If the set includes a workload, you run the published kit with `sbx run`. If it contains only mixins, you add it to a workload with `--kit`.


To share a combination without publishing another kit, list the workload and mixins in a [sandbox environment file](https://docs.docker.com/ai/sandboxes/configuration/environment-files/). Docker Sandboxes composes those kits when it creates the sandbox. An environment file can also configure the workspace and host resources. Choose a set when you want one published reference with a fixed list of components; the set records their image digests when you build it. You can also use a set in an environment file.


See [Use kits](https://docs.docker.com/ai/sandboxes/customize/use-kits/) for how to run kits and add mixins. To customize and publish your own combination, see [Compose a kit set](https://docs.docker.com/ai/sandboxes/customize/author/kit-sets/).


## [Version compatibility](https://docs.docker.com/ai/sandboxes/customize#version-compatibility)


V3 requires `sbx` v0.45 or later. Every kit in a v3 sandbox must use v3: select a v3 workload and add only v3 mixins.


Built-in agent names such as `claude` and `codex` select v2 kits, so `sbx run claude --kit ./some-v3-mixin` fails. To use that mixin, choose a [v3 workload](https://docs.docker.com/ai/sandboxes/customize/use-kits/#published-v3-workloads) by its image, local path, or Git reference.


A kit's capabilities can require a later release or a local sandbox. See [Kit capability support](https://docs.docker.com/ai/sandboxes/customize/author/capabilities/) for details. V2 remains supported and is not deprecated.


## [Choose your next step](https://docs.docker.com/ai/sandboxes/customize#choose-your-next-step)


- [Use kits](https://docs.docker.com/ai/sandboxes/customize/use-kits/) to run a published environment or combine a workload with mixins.
- [Author kits](https://docs.docker.com/ai/sandboxes/customize/author/) to build an agent environment, package a tool, or combine kits into a set to share with your team.
- Explore the [sandbox-kit-spec repository](https://github.com/docker/sandbox-kit-spec) for the authoritative v3 specification, build frontend, and examples.


To save an environment you've configured inside a sandbox, see [Save a sandbox as a template](https://docs.docker.com/ai/sandboxes/usage/#saving-a-sandbox-as-a-template).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# sbx

`https://docs.docker.com/reference/cli/sbx`

# sbx


| Description | Manage AI coding agent sandboxes. |
| --- | --- |
| Usage | `sbx COMMAND` |


## [Description](https://docs.docker.com/reference/cli/sbx#description)


Docker Sandboxes creates isolated sandbox environments for AI agents, powered by Docker.


Run without a command to launch interactive mode, or pass a command for CLI usage.


## [Commands](https://docs.docker.com/reference/cli/sbx#commands)


| Command | Description |
| --- | --- |
| [`sbx attach`](https://docs.docker.com/reference/cli/sbx/attach/) | Attach to a cloud sandbox, starting it first if it is stopped |
| [`sbx completion`](https://docs.docker.com/reference/cli/sbx/completion/) | Generate the autocompletion script for the specified shell |
| [`sbx cp`](https://docs.docker.com/reference/cli/sbx/cp/) | Copy files or directories between a sandbox and the host |
| [`sbx create`](https://docs.docker.com/reference/cli/sbx/create/) | Create a sandbox for an agent |
| [`sbx daemon`](https://docs.docker.com/reference/cli/sbx/daemon/) | Manage sandboxd daemon |
| [`sbx diagnose`](https://docs.docker.com/reference/cli/sbx/diagnose/) | Diagnose common issues with your sbx installation |
| [`sbx env`](https://docs.docker.com/reference/cli/sbx/env/) | experimental Manage sandboxes declaratively from an sbxenv.yaml file |
| [`sbx exec`](https://docs.docker.com/reference/cli/sbx/exec/) | Execute a command inside a sandbox |
| [`sbx kit`](https://docs.docker.com/reference/cli/sbx/kit/) | experimental Manage kit artifacts |
| [`sbx login`](https://docs.docker.com/reference/cli/sbx/login/) | Sign in to Docker |
| [`sbx logout`](https://docs.docker.com/reference/cli/sbx/logout/) | Stop running local sandboxes and sign out of Docker |
| [`sbx ls`](https://docs.docker.com/reference/cli/sbx/ls/) | List sandboxes |
| [`sbx mcp`](https://docs.docker.com/reference/cli/sbx/mcp/) | Manage MCP servers |
| [`sbx move`](https://docs.docker.com/reference/cli/sbx/move/) | Move a sandbox between local and cloud |
| [`sbx policy`](https://docs.docker.com/reference/cli/sbx/policy/) | Manage sandbox policies |
| [`sbx ports`](https://docs.docker.com/reference/cli/sbx/ports/) | Manage sandbox port publishing |
| [`sbx prune`](https://docs.docker.com/reference/cli/sbx/prune/) | Remove all stopped sandboxes |
| [`sbx reset`](https://docs.docker.com/reference/cli/sbx/reset/) | Reset all sandboxes and clean up state |
| [`sbx rm`](https://docs.docker.com/reference/cli/sbx/rm/) | Remove one or more sandboxes |
| [`sbx run`](https://docs.docker.com/reference/cli/sbx/run/) | Run an agent in a sandbox |
| [`sbx secret`](https://docs.docker.com/reference/cli/sbx/secret/) | Manage stored secrets |
| [`sbx settings`](https://docs.docker.com/reference/cli/sbx/settings/) | Manage Docker Sandboxes settings |
| [`sbx setup`](https://docs.docker.com/reference/cli/sbx/setup/) | experimental Detect host configuration and prepare Docker Sandboxes |
| [`sbx skills`](https://docs.docker.com/reference/cli/sbx/skills/) | experimental Manage skills available in sandboxes |
| [`sbx stop`](https://docs.docker.com/reference/cli/sbx/stop/) | Stop one or more sandboxes without removing them |
| [`sbx template`](https://docs.docker.com/reference/cli/sbx/template/) | Manage sandbox templates |
| [`sbx ttl`](https://docs.docker.com/reference/cli/sbx/ttl/) | Show or extend a cloud sandbox's TTL |
| [`sbx tui`](https://docs.docker.com/reference/cli/sbx/tui/) | Open the interactive TUI dashboard |
| [`sbx version`](https://docs.docker.com/reference/cli/sbx/version/) | Show Docker Sandboxes version information |
| [`sbx volume`](https://docs.docker.com/reference/cli/sbx/volume/) | Manage persistent volumes (cloud-only) |


## [Options](https://docs.docker.com/reference/cli/sbx#options)


| Option | Default | Description |
| --- | --- | --- |
| `--cloud` |  | Dispatch to Docker Cloud Sandboxes API instead of local sandboxd (supported by a growing set of verbs — run 'sbx --cloud --help' for the current list) |
| `-D, --debug` |  | Enable debug logging |[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Security model

`https://docs.docker.com/ai/sandboxes/security`

# Security model


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This page describes local sandboxes. For cloud behavior and limitations, see [Compare local and cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/).


Docker Sandboxes run AI agents in microVMs so they can execute code, install packages, and use tools without accessing host resources beyond those you share. Multiple isolation layers protect your host system.


## [Trust boundaries](https://docs.docker.com/ai/sandboxes/security#trust-boundaries)


The primary trust boundary is the microVM. The agent has full control inside the VM, including sudo access. The VM boundary prevents the agent from reaching anything on your host except what is explicitly shared.


What crosses the boundary into the VM:


- **Host workspace directory:** shared when you pass a workspace path or use `sbx run`, which defaults to the current directory. A direct mount is read-write, so the agent edits your working tree in place. With [`--clone`](https://docs.docker.com/ai/sandboxes/usage/#clone-mode), your repository is mounted read-only and the agent works on a private clone. A mountless sandbox doesn't share a host workspace.
- **Credentials:** the host-side proxy injects authentication headers into outbound HTTP requests. The raw credential values never enter the VM.
- **Network access:** outbound TCP connections to destinations allowed by [network policy](https://docs.docker.com/ai/sandboxes/security/defaults/) are proxied through the host.
- Shared agent skills: sandboxes created for supported agents mount a persistent host-side store read-only by default at the agent's skills directory. Use `--skills` or [`skills.defaultMode`](https://docs.docker.com/ai/sandboxes/configuration/settings/#skillsdefaultmode) to choose another mode at creation. Existing sandboxes retain their mounts until recreated.
- **MCP gateway traffic:** supported agents connect to a host-side MCP gateway endpoint. The gateway brokers access to registered MCP servers.


What crosses the boundary back to the host:


- **Workspace file changes:** visible on your host in real time when you use a direct mount.
- **Outbound TCP connections:** sent to allowed destinations through the host proxy.
- Shared skill changes: sandboxes with `readwrite` access can write to the host-side store. These changes are visible to other sandboxes that share it.


Outside the workspace and shared skills store, the agent cannot access your host filesystem. It also cannot access your host Docker daemon, your host network directly, or any destination not allowed by network policy. Sandboxes cannot communicate directly over the network. Outbound UDP is blocked unless you turn on the [experimental UDP feature](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#allow-outbound-udp) and allow it through network policy. ICMP is blocked.


MCP servers are an explicit integration point. Remote MCP servers run outside Docker Sandboxes, and local stdio MCP servers run on the host, not inside the sandbox VM. An agent can invoke the tools those servers expose through the MCP gateway, subject to MCP policies when organization governance is active. Treat local MCP servers as trusted host integrations.


### [MicroVM isolation](https://docs.docker.com/ai/sandboxes/security#microvm-isolation)


This topology shows what is private to the microVM, what is explicitly mounted, and which host resources remain outside the agent's reach.


Explore the microVM isolation boundary


Select a component or labeled connection to inspect what is private, mounted, or unreachable.


Isolation overview


The agent is contained inside the microVM


The agent controls the private VM filesystem and Docker Engine. The workspace, optional skills store, and forwarded SSH agent socket are explicit host connections; other host resources have no direct access path.


- AI agent: The agent has sudo access inside the microVM. It can install packages, run code, and modify resources that are inside the sandbox boundary.
- VM filesystem: The microVM has its own persistent filesystem. The agent cannot use it to browse files elsewhere on the host.
- Docker Engine: Containers created by the agent run on the Docker Engine inside the microVM. This engine has no connection to the Docker daemon on the host.
- Workspace: Direct mode mounts the host working tree read-write, so edits are visible on both sides. Clone mode mounts the host repository read-only and gives the agent a private clone.
- Shared skills store: Supported agents mount the host-side skills store read-write unless you opt out. Changes can become visible to agents in other participating sandboxes.
- SSH agent socket: When SSH_AUTH_SOCK is set on the host, Docker Sandboxes forwards the agent socket into the microVM. Sandbox processes can request signatures, but the private keys stay on the host.
- Other host resources: The agent has no direct path to the rest of the host filesystem, host processes, or the host Docker daemon.
- Workspace mount: This explicit mount is the agent's path to project files on the host. Its permissions depend on whether the sandbox uses direct mode or clone mode.
- Skills mount: This optional read-write mount connects supported agents to a persistent skills store shared through the host.
- SSH agent socket: The forwarded socket gives sandbox processes access to signing operations through the host SSH agent without exposing the private keys.


To follow an outbound request through network policy and credential injection, see [Architecture](https://docs.docker.com/ai/sandboxes/architecture/#follow-an-authenticated-request).


## [Isolation layers](https://docs.docker.com/ai/sandboxes/security#isolation-layers)


The sandbox security model has five layers. See [Isolation layers](https://docs.docker.com/ai/sandboxes/security/isolation/) for technical details on each.


- **Hypervisor isolation:** separate kernel per sandbox. No shared memory or processes with the host.
- **Network isolation:** outbound TCP traffic is proxied through the host and governed by a [deny-by-default policy](https://docs.docker.com/ai/sandboxes/security/defaults/). Experimental UDP egress also follows network policy. ICMP is blocked.
- **Docker Engine isolation:** each sandbox has its own Docker Engine with no path to the host daemon.
- **Workspace isolation:** a mountless sandbox has no host workspace mount. Clone mode gives the agent a private in-VM clone and mounts your repository read-only. Direct mode shares your working tree read-write.
- **Credential isolation:** API keys are injected into HTTP headers by the host-side proxy. Credential values never enter the VM.


## [What the agent can do inside the sandbox](https://docs.docker.com/ai/sandboxes/security#what-the-agent-can-do-inside-the-sandbox)


Inside the VM, the agent has full privileges: sudo access, package installation, a private Docker Engine, and read-write access to its in-sandbox filesystem and configured workspace. Installed packages, Docker images, and other VM state persist across restarts. See [Default security posture](https://docs.docker.com/ai/sandboxes/security/defaults/) for the full breakdown of what is permitted and what is blocked.


## [Security considerations](https://docs.docker.com/ai/sandboxes/security#security-considerations)


The sandbox isolates the agent from your host system, but the agent's actions can still affect you through explicitly shared resources and allowed network channels.


In direct mode, workspace changes are live on your host. The agent edits the same files you see on your host. This includes files that execute implicitly during normal development: Git hooks, CI configuration, IDE task configs, AI project configuration and settings, `Makefile`, `package.json` scripts, and similar build files. Review changes before running any modified code. Note that Git hooks live inside `.git/` and do not appear in `git diff` output — check them separately. See [Workspace isolation](https://docs.docker.com/ai/sandboxes/security/isolation/#workspace-isolation) for the full list and for the alternative clone-mode boundary.


The default allowed domains include broad wildcards. Some defaults like `*.googleapis.com` cover many services beyond AI APIs. Run `sbx policy ls` to see the full list of active rules, and remove entries you don't need. See [Default security posture](https://docs.docker.com/ai/sandboxes/security/defaults/).


Kits run install commands with root privileges inside the sandbox. To limit supply-chain risk, `sbx` restricts kit installs to an allowlist of sources that defaults to Docker Hub only. See [Restrict kit sources](https://docs.docker.com/ai/sandboxes/customize/use-kits/#restrict-kit-sources).


Shared agent skills create a narrow exception to cross-sandbox isolation. The store can be mounted with `readwrite` access, so one sandbox can modify instructions or scripts that an agent later uses in another sandbox, including one with `readonly` access. This doesn't expose the rest of the host filesystem or create a direct network path between sandboxes, but it does put participating sandboxes in the same trust boundary. See [Share agent skills](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/) for details and the per-sandbox opt-out.


Local stdio MCP servers run outside the sandbox VM. If you register a local MCP server that starts a host process or host Docker container, that process or container uses host permissions and host isolation, not sandbox isolation. See [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/).


## [Organization-wide control](https://docs.docker.com/ai/sandboxes/security#organization-wide-control)


On a single developer's machine, security and policy are configured locally — for example, network and filesystem rules set with `sbx policy`. Admins can move these controls to the organization level so that security, policy, and access apply consistently across every developer's sandboxes, rather than depending on local configuration.


See [Governance](https://docs.docker.com/ai/sandboxes/governance/) for the controls available to organization admins.


*See Governance for the controls available to organization
admins.*

## [Learn more](https://docs.docker.com/ai/sandboxes/security#learn-more)


- [Isolation layers](https://docs.docker.com/ai/sandboxes/security/isolation/): how hypervisor, network, Docker, workspace, and credential isolation work
- [Default security posture](https://docs.docker.com/ai/sandboxes/security/defaults/): what a fresh sandbox permits and blocks
- [Manage credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/): provide and manage API keys while keeping their values outside the sandbox
- [Governance](https://docs.docker.com/ai/sandboxes/governance/): configure network, filesystem, and MCP access controls locally or across your organization[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# FAQ

`https://docs.docker.com/ai/sandboxes/faq`

# FAQ


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Host integration and workspace instructions on this page describe local sandboxes. See [Local and cloud differences](https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/) before adapting those workflows to the cloud.


## [Is Docker Sandboxes free? Can I use it commercially?](https://docs.docker.com/ai/sandboxes/faq#is-docker-sandboxes-free-can-i-use-it-commercially)


The `sbx` CLI and local sandbox compute are free to use, including for commercial and professional work. Cloud sandbox compute uses a [pay-as-you-go subscription](https://docs.docker.com/agentic-platform/signup/#billing). Model-provider charges are separate from sandbox compute.


Organization governance for local sandboxes includes centrally managed network, filesystem, and MCP policies, [sign-in enforcement](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement/), and [audit logs](https://docs.docker.com/ai/sandboxes/governance/audit/). These [organization governance features](https://docs.docker.com/ai/sandboxes/governance/) require a separate paid subscription — [contact Docker Sales](https://www.docker.com/products/ai-governance/#contact-sales) to get started.


## [Why do I need to sign in?](https://docs.docker.com/ai/sandboxes/faq#why-do-i-need-to-sign-in)


Docker Sandboxes is built around the idea that you and your agents are a team. Signing in gives each sandbox a verified identity, which lets Docker:


- **Tie sandboxes to a real person.** Governance matters when agents can build containers, install packages, and push code. Your Docker identity is the anchor.
- **Enable team features.** Team-scale features like [organization governance](https://docs.docker.com/ai/sandboxes/governance/), shared environments, and audit logs need a concept of "who," and adding that later would be worse for everyone.
- **Authenticate against Docker infrastructure.** Sandboxes pull images, run daemons, and talk to Docker services. A Docker account authenticates those requests.


Your Docker account email is only used for authentication, not marketing.


## [Can I enforce sandbox policies across my organization?](https://docs.docker.com/ai/sandboxes/faq#can-i-enforce-sandbox-policies-across-my-organization)


Yes. Admins can centrally manage network, filesystem, and MCP policies. These controls apply to local sandboxes in the organization. When organization governance is active, only organization allow rules grant access: local allow rules set with `sbx policy` are no longer evaluated, while local deny rules still apply on top.


See [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/). This feature requires a separate paid subscription — [contact Docker Sales](https://www.docker.com/products/ai-governance/#contact-sales) to get started.


Cloud sandboxes use separate network policy configuration. See [Cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) for cloud controls.


## [Which domains do I need to allow for Docker Sandboxes to work?](https://docs.docker.com/ai/sandboxes/faq#which-domains-do-i-need-to-allow-for-docker-sandboxes-to-work)


If your organization restricts outbound network access with a firewall or proxy, add the following domains to your allowlist so that `sbx` can authenticate, pull images, and report diagnostics for local sandboxes. Cloud operations also connect to `https://api.sandboxes-cloud.docker.com`.


| Domain | Description |
| --- | --- |
| [https://login.docker.com](https://login.docker.com) | Authentication |
| [https://hub.docker.com](https://hub.docker.com) | Docker Hub |
| [https://api.docker.com](https://api.docker.com) | Docker API |
| [https://marlin-2.docker.com](https://marlin-2.docker.com) | Telemetry |
| [https://marlin-api.docker.com](https://marlin-api.docker.com) | Telemetry |
| [https://registry-1.docker.io](https://registry-1.docker.io) | Docker pull/push |
| [https://auth.docker.io](https://auth.docker.io) | Registry authentication |
| [https://dhi.io](https://dhi.io) | Docker Hardened Images |
| [https://sbx-diagnostics.s3.us-east-1.amazonaws.com](https://sbx-diagnostics.s3.us-east-1.amazonaws.com) | Diagnostics upload |


## [Does the CLI collect telemetry?](https://docs.docker.com/ai/sandboxes/faq#does-the-cli-collect-telemetry)


The `sbx` CLI collects basic usage data about CLI invocations:


- Which command you ran
- Whether it succeeded or failed
- How long it took
- If you're signed in, your Docker username is included


CLI usage telemetry does not include your prompts or code. Cloud sandboxes execute on Docker-managed infrastructure, so files you transfer to them are stored in the cloud.


To opt out of CLI usage analytics, set the `SBX_NO_TELEMETRY` environment variable:


```console
$ export SBX_NO_TELEMETRY=1
```


*The sbx CLI collects basic usage data about CLI invocations:*

## [How do I set custom environment variables inside a sandbox?](https://docs.docker.com/ai/sandboxes/faq#how-do-i-set-custom-environment-variables-inside-a-sandbox)


Starting with `sbx` version 0.39.0, use `-e` / `--env` or `--env-file` with `sbx run` and `sbx create`. See [Set environment variables](https://docs.docker.com/ai/sandboxes/usage/#set-environment-variables) for syntax, precedence rules, persistent configuration for an existing sandbox, and guidance for credentials.


Variables in `/etc/sandbox-persistent.sh` are available to interactive sessions and agents started with `sbx run`. A variable only takes effect for sessions and agents started after it's added. Restart a running agent, or stop and start the sandbox, to pick up the new value.


## [Why do agents run without approval prompts?](https://docs.docker.com/ai/sandboxes/faq#why-do-agents-run-without-approval-prompts)


The sandbox itself is the safety boundary. Because agents run inside an isolated microVM with [network policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/), [credential isolation](https://docs.docker.com/ai/sandboxes/security/isolation/#credential-isolation), and no access to your host system outside explicitly shared paths, the usual reasons for approval prompts (preventing destructive commands, network access, file modifications) are handled by the sandbox isolation layers instead.


If you prefer to re-enable approval prompts, change the permission mode inside the session. Most agents let you switch permission modes after startup. In Claude Code, use the `/permissions` command to change the mode interactively.


To make approval prompts the default for every session, create a v2 sandbox kit that extends the built-in agent and changes its launch options. See [Fork an existing agent](https://docs.docker.com/ai/sandboxes/customize/kits-v2/#fork-an-existing-agent) for a complete example.


For an environment built entirely with v3 kits, set the launch command in the workload's Dockerfile. See [Build a v3 agent kit](https://docs.docker.com/ai/sandboxes/customize/author/build-an-agent/).


## [How do I know if my agent is running in a sandbox?](https://docs.docker.com/ai/sandboxes/faq#how-do-i-know-if-my-agent-is-running-in-a-sandbox)


Ask the agent. The agent can see whether or not it's running inside a sandbox. In Claude Code, use the `/btw` slash command to ask without interrupting an in-progress task:


```text
/btw are you running in a sandbox?
```


## [Why doesn't the sandbox use my user-level agent configuration?](https://docs.docker.com/ai/sandboxes/faq#why-doesnt-the-sandbox-use-my-user-level-agent-configuration)


Local sandboxes don't import your complete user-level agent configuration. Hooks, settings, and other files under directories such as `~/.claude` remain on the host. Project-level configuration in the working directory remains available inside the sandbox.


Shared agent skills are the exception. Use `sbx skills add` to install skills from a Git repository, or run `sbx skills import` to copy skills from supported host directories. `sbx` keeps the skills in a persistent store shared with sandboxes. See [Share agent skills](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/) for repository management, supported host directories, mount behavior, and per-sandbox opt-out.


Keep project-specific skills and other agent configuration in the project itself. This versions the configuration alongside the code. Don't use symlinks to host paths because a sandboxed agent can't follow them outside the sandbox.


## [Can I paste images into an agent?](https://docs.docker.com/ai/sandboxes/faq#can-i-paste-images-into-an-agent)


In local sandboxes, image paste is off by default. Text paste works because the terminal sends it directly. Pasting an image or screenshot with `Ctrl+V` is different: the agent reads it from your host clipboard, and the sandbox blocks that access unless you opt in.


Turn on [`clipboard.imagePaste`](https://docs.docker.com/ai/sandboxes/configuration/settings/#clipboardimagepaste):


```console
$ sbx settings set clipboard.imagePaste true
```


`Ctrl+V` then pastes host images into agents that read the clipboard, including Claude Code and Codex. The setting takes effect within a few seconds, even for running sandboxes.


This is opt-in because it relaxes the sandbox's isolation: when enabled, a process inside the sandbox can read your host clipboard through the host-side proxy. The exposure is narrow — reads happen only on a paste, return image data only (`image/png`), and clipboard content is never cached or logged — but it's still host data crossing into the sandbox, so it stays off until you turn it on.


To turn it back off:


```console
$ sbx settings set clipboard.imagePaste false
```


*Turn on clipboard.imagePaste:*

## [Can I use Docker Sandboxes on headless Linux?](https://docs.docker.com/ai/sandboxes/faq#can-i-use-docker-sandboxes-on-headless-linux)


Yes. For local sandboxes on Linux, `sbx` stores secrets in the Secret Service exposed by your desktop keyring, such as GNOME Keyring or KDE Wallet. Headless servers and some WSL setups have no running Secret Service, so `sbx` falls back to a file under `$XDG_CONFIG_HOME/com.docker.sandboxes`, which defaults to `~/.config/com.docker.sandboxes` when `$XDG_CONFIG_HOME` is unset. No setup is required. When you store a secret on such a host, `sbx` prints a notice:


```text
No keychain detected - this secret will be stored on disk, protected by file permissions rather than a password
```


`sbx` stores the file in a directory with `0700` permissions, the same file-permission model used for `~/.docker/config.json`. Any user or process that can read the file can retrieve the stored credentials, so treat the directory as sensitive. Where available, prefer a keychain, which mediates access per application.


To keep secrets in a keyring instead, run a Secret Service on the host before storing them: install `gnome-keyring` and start `dbus-run-session`, or run the keyring daemon under a login session that unlocks it. Once a working Secret Service is available, `sbx` stores new secrets in the keychain again. For where each platform keeps secrets, see [Where secrets are stored](https://docs.docker.com/ai/sandboxes/configuration/credentials/#where-secrets-are-stored).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Troubleshooting

`https://docs.docker.com/ai/sandboxes/troubleshooting`

Back [Manuals](https://docs.docker.com/manuals/)


- [Get started](https://docs.docker.com/get-started/)
- [Guides](https://docs.docker.com/guides/)
- [Reference](https://docs.docker.com/reference/)


# Troubleshooting


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The following diagnostics and recovery steps apply to local sandboxes. Use [`sbx --cloud diagnose`](https://docs.docker.com/ai/sandboxes/cloud/usage/#diagnose-cloud-access) to check cloud connectivity and account access. For cloud files, expiration, and network access, see [Cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/). Local daemon restarts and `sbx reset` do not repair cloud sandbox state.


## [Run diagnostics](https://docs.docker.com/ai/sandboxes/troubleshooting#run-diagnostics)


Before digging into a specific issue, run [`sbx diagnose`](https://docs.docker.com/reference/cli/sbx/diagnose/) to check for common problems with your installation, such as a missing CLI binary, daemon reachability problems, a CLI/daemon version mismatch, missing storage directories, or broken authentication.


```console
$ sbx diagnose
```


The command prints a summary of checks that passed, warned, or failed, along with suggested fixes. Use `--json` or `--format yaml` for machine-readable output, or `--format github-issue` to generate a Markdown snippet suitable for pasting into a GitHub issue.


## [Sandbox is not responding](https://docs.docker.com/ai/sandboxes/troubleshooting#sandbox-is-not-responding)


If `sbx ls` shows `running (not responding)`, Docker Sandboxes has detected that the sandbox isn't responding to commands. Stop and start that sandbox, then retry your command:


```console
$ sbx stop <SANDBOX_NAME>
$ sbx start <SANDBOX_NAME>
```


Files saved in the sandbox are kept when you stop and start it.


## [Restart the sandbox daemon](https://docs.docker.com/ai/sandboxes/troubleshooting#restart-the-sandbox-daemon)


If sandbox commands hang, fail to connect to the daemon, or keep returning daemon errors, restart the sandbox daemon before resetting sandbox state:


```console
$ sbx daemon restart
```


Then retry the command that failed. Restarting the daemon doesn't delete sandbox data. If the issue persists or state is corrupted, use [`sbx reset`](https://docs.docker.com/reference/cli/sbx/reset/).


## [Resetting sandboxes](https://docs.docker.com/ai/sandboxes/troubleshooting#resetting-sandboxes)


If you hit persistent issues or corrupted state, run [`sbx reset`](https://docs.docker.com/reference/cli/sbx/reset/) to stop all VMs and delete all sandbox data. Create fresh sandboxes afterwards.


## [Sandbox doesn't contain my project files](https://docs.docker.com/ai/sandboxes/troubleshooting#sandbox-doesnt-contain-my-project-files)


Starting with `sbx` version 0.42.0, the workspace path is optional for `sbx create`. When you omit it, the command creates a mountless sandbox. For example, these commands create and attach to a sandbox without mounting your host project files:


```console
$ sbx create --name <sandbox-name> <agent>
$ sbx run --name <sandbox-name>
```


By contrast, `sbx run` mounts the current directory when you don't pass a workspace path:


```console
$ sbx run <agent>
```


A sandbox's workspace configuration is fixed when the sandbox is created. To reuse the name of an existing mountless sandbox, first [copy out any files you want to keep](https://docs.docker.com/ai/sandboxes/usage/#copy-files-between-host-and-sandbox), then remove and recreate it with a workspace path:


```console
$ sbx rm <sandbox-name>
$ sbx run --name <sandbox-name> <agent>
```


See [Choose a workspace](https://docs.docker.com/ai/sandboxes/usage/#choose-a-workspace) for mountless, direct, and clone-mode behavior.


*See Choose a workspace for mountless, direct,
and clone-mode behavior.*

## [Kiro, Copilot, or Droid shorthand fails](https://docs.docker.com/ai/sandboxes/troubleshooting#kiro-copilot-or-droid-shorthand-fails)


In Docker Sandboxes v0.42, `sbx run kiro`, `sbx run copilot`, and `sbx run droid` fail because these agents moved from built-in agents to public kits and their shorthand names aren't resolved in this release.


[Upgrade Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install/) to v0.43.0 or later to launch these agents by name again. If you need to stay on v0.42, use the full kit reference for your agent:


```console
$ sbx run docker.io/sbx/kiro-kit:latest
$ sbx run docker.io/sbx/copilot-kit:latest
$ sbx run docker.io/sbx/droid-kit:latest
```


## [Agent can't install packages or reach an API](https://docs.docker.com/ai/sandboxes/troubleshooting#agent-cant-install-packages-or-reach-an-api)


Sandboxes use [network access rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/) to control outbound traffic. If the agent fails to install packages or call an external API, the target domain is likely not in the allow list. Check which requests are being blocked:


```console
$ sbx policy log
```


Then allow the domains your workflow needs:


```console
$ sbx policy allow network "*.npmjs.org,*.pypi.org,files.pythonhosted.org"
```


To allow all outbound traffic instead:


```console
$ sbx policy allow network "**"
```


If `sbx policy allow` doesn't unblock the request, your organization may manage sandbox policies centrally and take precedence over local rules. See [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/).


## [Kit fails to install: source not in allowlist](https://docs.docker.com/ai/sandboxes/troubleshooting#kit-fails-to-install-source-not-in-allowlist)


If loading a kit fails with a message like its source is not in your allowlist:


```console
$ sbx run claude --kit "git+https://github.com/docker/sbx-kits-contrib.git#dir=vale"
```


`sbx` restricts kit installs to an allowlist of sources, which defaults to Docker Hub (`docker.io/`) only. Add the kit's publisher to the [`kit.allowedSources`](https://docs.docker.com/ai/sandboxes/configuration/settings/#kitallowedsources) setting, keeping the entries you want to retain:


```console
$ sbx settings set kit.allowedSources '["docker.io/","github.com/docker/"]'
```


Then run the command again. For details, including how to allow local kits or any remote source, see [Restrict kit sources](https://docs.docker.com/ai/sandboxes/customize/use-kits/#restrict-kit-sources).


*If loading a kit fails with a message like its source is not in your
allowlist:*

## [SSH and other non-HTTP connections fail](https://docs.docker.com/ai/sandboxes/troubleshooting#ssh-and-other-non-http-connections-fail)


Non-HTTP TCP connections such as SSH can be allowed by adding a policy rule for the destination. Hostname rules work for these connections because the sandbox recovers the hostname from its DNS resolver when the protocol doesn't include one:


```console
$ sbx policy allow network "myhost:22"
```


If the destination is reached by IP address without a DNS lookup, the hostname can't be recovered. Use an address-based rule in that case:


```console
$ sbx policy allow network "10.1.2.3:22"
```


UDP requires [experimental UDP egress](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#allow-outbound-udp) and UDP allow rules. ICMP is blocked and can't be unblocked with policy rules.


For Git operations over SSH, you can either add an allow rule for the Git server's hostname or IP address, or use HTTPS URLs instead:


```console
$ git clone https://github.com/owner/repo.git
```


## [Can't reach a service running on the host](https://docs.docker.com/ai/sandboxes/troubleshooting#cant-reach-a-service-running-on-the-host)


If a request to `127.0.0.1` or a local network IP returns "connection refused" from inside a sandbox, the address is not reachable from within the sandbox VM. See [Accessing host services from a sandbox](https://docs.docker.com/ai/sandboxes/workflows/development/#accessing-host-services-from-a-sandbox).


## [Docker authentication failure](https://docs.docker.com/ai/sandboxes/troubleshooting#docker-authentication-failure)


If you see a message like `You are not authenticated to Docker`, your login session has expired. In an interactive terminal, the CLI prompts you to sign in again. In non-interactive environments such as scripts or CI, run `sbx login` to re-authenticate.


## [Agent authentication failure](https://docs.docker.com/ai/sandboxes/troubleshooting#agent-authentication-failure)


If the agent can't reach its model provider or you see API key errors, the key is likely invalid, expired, or not configured. Verify it's set in your shell configuration file and that you sourced it or opened a new terminal.


For agents that use the [credential proxy](https://docs.docker.com/ai/sandboxes/configuration/credentials/), make sure you haven't set the API key to an invalid value inside the sandbox — the proxy injects credentials automatically on outbound requests.


If credentials are configured correctly but API calls still fail, check `sbx policy log` and look at the **PROXY** column. Requests routed through the `transparent` proxy don't get credential injection. This can happen when a client inside the sandbox (such as a process in a Docker container) isn't configured to use the forward proxy. See [Monitoring network activity](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/) for details.


## [MCP server streams stall](https://docs.docker.com/ai/sandboxes/troubleshooting#mcp-server-streams-stall)


If a remote MCP server's HTTP/2 handling stalls long-lived streams, register it with `--disable-http2` to use HTTP/1.1:


```console
$ sbx mcp add acme --url https://mcp.acme.com/mcp --disable-http2
```


Replace the example URL with your MCP endpoint. The setting applies to later connections to this server. The flag requires `--url` and can't be used with `--command` or `--local`. For registration options, see [Register an MCP server](https://docs.docker.com/ai/sandboxes/mcp-gateway/#register-an-mcp-server).


## [API calls fail with a certificate error](https://docs.docker.com/ai/sandboxes/troubleshooting#api-calls-fail-with-a-certificate-error)


If your organization uses a proxy that inspects HTTPS traffic, agent requests can fail with a certificate error such as `SSL certificate problem: self-signed certificate in certificate chain`. Install your organization's internal root CA inside the sandbox so the agent and its SDKs trust certificates signed by the proxy. Certificate errors can stop a request before the credential proxy can inject credentials.


For repeatable setup with a built-in agent, create a [v2 mixin kit](https://docs.docker.com/ai/sandboxes/customize/kits-v2/) that installs the CA when the sandbox is created. See [Install an internal CA certificate](https://docs.docker.com/ai/sandboxes/customize/kits-v2/#install-an-internal-ca-certificate) for an example kit.


Use a PEM-encoded certificate with a `.crt` extension. If traffic can be signed by more than one internal proxy, install each proxy's root CA before running `update-ca-certificates`.


Create a sandbox with the kit:


```console
$ sbx run claude --kit ./internal-ca/
```


To update an existing sandbox, copy the certificate into the sandbox and update the trust store:


```console
$ sbx cp ./internal-ca.crt <sandbox-name>:/tmp/internal-ca.crt
$ sbx exec <sandbox-name> -- sudo install -m 0644 /tmp/internal-ca.crt /usr/local/share/ca-certificates/internal-ca.crt
$ sbx exec <sandbox-name> -- sudo update-ca-certificates
```


> Important
>
> Install the CA into the system trust store with `update-ca-certificates`, as shown above. Don't override the sandbox's TLS trust variables (such as `SSL_CERT_FILE`) to point at only your internal CA. Doing so replaces the system bundle and breaks the trust the credential proxy depends on, so requests on the `forward` egress path fail.


If API calls still fail after installing the CA, run `sbx policy log` and check the egress path in the **PROXY** column:


- `forward`: the credential proxy terminates TLS and presents its own certificate, which the sandbox already trusts. Requests on this path don't need the internal CA, and overriding the sandbox's trust variables breaks them, as described above.
- `forward-bypass` and `transparent`: the proxy forwards packets to the upstream proxy without terminating TLS, so the sandbox sees your organization's certificate directly. These paths are where installing the internal CA applies. The only difference between them is whether the client knows it's talking to a proxy.


### [Certificate errors during Docker builds](https://docs.docker.com/ai/sandboxes/troubleshooting#certificate-errors-during-docker-builds)


Containers started by the sandbox's Docker Engine have their own trust stores. They don't inherit the sandbox's installed certificates. If an HTTPS download in a Dockerfile fails with `self signed certificate in certificate chain`, install the proxy CA in the build image before the download.


From a shell inside the sandbox, write its proxy CA into your build context:


```console
$ printf '%s' "$PROXY_CA_CERT_B64" | base64 -d > sbx-proxy-ca.crt
```


For a Debian-based image with `ca-certificates` installed, copy the certificate and update the trust store before commands that make HTTPS requests:


```dockerfile
FROM python:3.13-slim
COPY sbx-proxy-ca.crt /usr/local/share/ca-certificates/sbx-proxy-ca.crt
RUN update-ca-certificates
```


Build inside the sandbox, passing its proxy settings to the build:


```console
$ docker build --build-arg HTTP_PROXY --build-arg HTTPS_PROXY --build-arg NO_PROXY -t my-app .
```


If your organization also inspects TLS, install its root CA in the build image as a separate `.crt` file before `update-ca-certificates`. Keep the system CA bundle intact so the image trusts both proxies and public certificate authorities. The earlier [certificate troubleshooting](https://docs.docker.com/ai/sandboxes/troubleshooting#api-calls-fail-with-a-certificate-error) explains which proxy paths need each CA.


Keep the generated proxy certificate out of version control. Regenerate it and rebuild the image if the sandbox proxy CA changes.


## [Sandbox runs out of disk space](https://docs.docker.com/ai/sandboxes/troubleshooting#sandbox-runs-out-of-disk-space)


The sandbox root (`/`) filesystem defaults to 20 GB. To increase it, set `DOCKER_SANDBOXES_ROOT_SIZE` before creating the sandbox:


```console
$ DOCKER_SANDBOXES_ROOT_SIZE=40g sbx run claude
```


`DOCKER_SANDBOXES_ROOT_SIZE` controls the root filesystem size. The Docker data disk at `/var/lib/docker` is independent and defaults to 10 GB. To change the Docker data disk size for a sandbox, set `DOCKER_SANDBOXES_DOCKER_SIZE` when you create it:


```console
$ DOCKER_SANDBOXES_DOCKER_SIZE=20g sbx run claude
```


The Docker data disk must be at least 512 MiB. The environment variable doesn't resize existing volumes.


For a [clone-mode sandbox](https://docs.docker.com/ai/sandboxes/usage/#clone-mode), set `DOCKER_SANDBOXES_CLONED_WORKSPACE_SIZE` before creating the sandbox to configure the cloned workspace volume capacity. The variable accepts human-readable size strings such as `100g`:


```console
$ DOCKER_SANDBOXES_CLONED_WORKSPACE_SIZE=100g sbx run --clone claude .
```


## [Filesystem operations are slow in large repositories](https://docs.docker.com/ai/sandboxes/troubleshooting#filesystem-operations-are-slow-in-large-repositories)


Filesystem operations such as `git status`, `git log`, or directory scans can be noticeably slow when you pass a workspace path and use direct mode. Virtiofs caching speeds up these workloads. Clone-mode sandboxes always enable it, so this tuning applies only to direct mode.


Virtiofs caching is enabled by default on all operating systems. If you experience Git index corruption or unexpected file content, disable caching with the kill switch and recreate the sandbox:


```console
$ DOCKER_SANDBOXES_ENABLE_VIRTIOFS_CACHE=0 sbx run <agent>
```


## [Clone mode reports "not in a Git repository" on WSL](https://docs.docker.com/ai/sandboxes/troubleshooting#clone-mode-reports-not-in-a-git-repository-on-wsl)


On Windows, running [`sbx run --clone`](https://docs.docker.com/ai/sandboxes/usage/#clone-mode) against a repository on a WSL filesystem (a `\\wsl.localhost\...` path) can fail even though the directory is a valid Git repository:


```console
> sbx run --clone claude \\wsl.localhost\Ubuntu\home\you\repo
error: --clone requires a Git repository, but \\wsl.localhost\Ubuntu\home\you\repo is not in a Git repository
```


The cause is Git's dubious ownership check. When Git on Windows accesses a repository owned by a different user across the WSL boundary, it refuses to operate on it, so the underlying repository detection fails:


```console
> git -C \\wsl.localhost\Ubuntu\home\you\repo rev-parse --show-toplevel
fatal: detected dubious ownership in repository at '//wsl.localhost/Ubuntu/home/you/repo'
```


Add the repository to Git's `safe.directory` list to allow access, then run the command again:


```console
> git config --global --add safe.directory '%(prefix)///wsl.localhost/Ubuntu/home/you/repo'
> sbx run --clone claude \\wsl.localhost\Ubuntu\home\you\repo
```


## [SSH agent socket is missing](https://docs.docker.com/ai/sandboxes/troubleshooting#ssh-agent-socket-is-missing)


If `SSH_AUTH_SOCK` is set inside a sandbox but `ssh-add -L` reports `No such file or directory`, check whether your custom template includes `socat`. Docker Sandboxes uses it to create the socket that forwards requests to your host SSH agent. Installing OpenSSH client tools alone isn't enough.


For an Ubuntu-based custom template, add `socat` to the packages installed as root in your Dockerfile, then rebuild the template and create a sandbox from it. Docker-provided sandbox templates already include `socat`.


If the socket exists but forwarding still fails, check the [SSH agent settings](https://docs.docker.com/ai/sandboxes/configuration/credentials/#ssh-agent).


*If the socket exists but forwarding still fails, check the
SSH agent settings.*

## [Sandbox commits aren't signed](https://docs.docker.com/ai/sandboxes/troubleshooting#sandbox-commits-arent-signed)


Docker Sandboxes can sign Git commits with SSH keys from your host agent. For setup steps, see [Commit signing](https://docs.docker.com/ai/sandboxes/workflows/git/#commit-signing).


Forwarding is enabled by default. Check [`ssh.agentForwardingEnabled`](https://docs.docker.com/ai/sandboxes/configuration/settings/#sshagentforwardingenabled) and [`ssh.agentSocketPath`](https://docs.docker.com/ai/sandboxes/configuration/settings/#sshagentsocketpath) to confirm that forwarding is enabled and inspect the socket selection:


```console
$ sbx settings get ssh.agentForwardingEnabled
$ sbx settings get ssh.agentSocketPath
```


If you use each client's current `SSH_AUTH_SOCK`, reconnect from a shell where it points to the intended agent. If `ssh.agentSocketPath` returns a path, confirm that it points to an active host agent. After changing forwarding or the socket selection, run `sbx daemon restart`.


If `ssh-add -L` prints `The agent has no identities.`, the sandbox can reach the forwarded agent, but the host agent doesn't have a loaded key. Load the signing key into your host SSH agent:


```console
$ ssh-add ~/.ssh/id_ed25519
```


If commit signing works on the host but fails in a sandbox, check whether Git is configured to sign with a host file path such as `/Users/me/.ssh/id_ed25519.pub`. The sandbox uses the forwarded SSH agent, not the host key file path. Use the inline public key form instead:


```console
$ git config --global gpg.format ssh
$ git config --global user.signingkey "key::$(ssh-add -L | head -n 1)"
```


If Git reports that `ssh-keygen` is missing, use a sandbox template that includes OpenSSH client tools.


If `git log --show-signature` reports that `gpg.ssh.allowedSignersFile` needs to be configured, Git can't verify the SSH signature locally. This verification config isn't required to create signed commits. GitHub uses the SSH signing keys configured in your GitHub account to verify commits.


GPG and S/MIME signing keys aren't available inside the sandbox. If your repository or organization requires GPG or S/MIME signatures, or if SSH signing isn't configured, use one of these workarounds:


- Commit outside the sandbox. Let the agent make changes without committing, then commit and sign from your host terminal.
- Sign after the fact. Let the agent commit inside the sandbox, then re-sign the commits on your host: ```console $ git rebase --exec 'git commit --amend --no-edit -S' origin/main ``` This replays each commit on the branch and re-signs it with your local signing key.


## [Daemon fails to start after downgrading](https://docs.docker.com/ai/sandboxes/troubleshooting#daemon-fails-to-start-after-downgrading)


If you downgrade `sbx` to a version older than the one that last managed your local state, the daemon may fail to start with a database version mismatch:


```text
error: failed to start backend in-process: start backend: creating containerd
server: ... database is at major version 6, but this binary only supports up
to major version 1
```


A newer version of `sbx` upgraded the local database to a schema that older binaries don't understand. To recover, reset all sandbox state:


```console
$ sbx reset --preserve-secrets
```


This stops all VMs and deletes all sandbox data. You'll need to create new sandboxes afterwards. The `--preserve-secrets` flag keeps any secrets you've set so you don't have to reconfigure them.


## [Removing all state](https://docs.docker.com/ai/sandboxes/troubleshooting#removing-all-state)


As a last resort, if `sbx reset` doesn't resolve your issue, you can remove the `sbx` state directory entirely. This deletes all sandbox data, configuration, and cached images. Stop all running sandboxes first with `sbx reset`.


macOS


Windows


Linux


```console
$ rm -rf ~/Library/Application\ Support/com.docker.sandboxes/
```


```powershell
> Remove-Item -Recurse -Force "$env:LOCALAPPDATA\DockerSandboxes"
```


Sandbox state on Linux follows the XDG Base Directory specification and is spread across three directories:


```console
$ rm -rf ~/.local/state/sandboxes/
$ rm -rf ~/.cache/sandboxes/
$ rm -rf ~/.config/sandboxes/
```


If you have set custom `XDG_STATE_HOME`, `XDG_CACHE_HOME`, or `XDG_CONFIG_HOME` environment variables, replace `~/.local/state`, `~/.cache`, and `~/.config` with the corresponding values.


## [Enable automatic diagnostics uploads](https://docs.docker.com/ai/sandboxes/troubleshooting#enable-automatic-diagnostics-uploads)


To opt in to automatic diagnostics uploads after certain daemon errors, set [`diagnostics.autoUpload`](https://docs.docker.com/ai/sandboxes/configuration/settings/#diagnosticsautoupload) to `yes`:


```console
$ sbx settings set diagnostics.autoUpload yes
```


Automatic bundles include basic system information and client, daemon, crash, and MCP logs. Docker Sandboxes redacts recognized identity values and credential patterns, but collected logs can still contain user content. Failed uploads remain in a local queue for a later retry.


## [Report an issue](https://docs.docker.com/ai/sandboxes/troubleshooting#report-an-issue)


If you've exhausted the steps above and the problem persists, file a GitHub issue at [github.com/docker/sbx-releases/issues](https://github.com/docker/sbx-releases/issues).


To help Docker investigate, generate a diagnostics bundle and share it when reporting the issue:


```console
$ sbx diagnose --upload
```


The bundle contains daemon logs, diagnostic check results, and basic system information. When `--upload` is confirmed, the bundle is uploaded to Docker support and the command prints a diagnostics ID. Include this ID in your issue so the team can correlate it with the uploaded bundle.


Without terminal input, `sbx diagnose --upload` saves the bundle locally and skips the upload. Check for a diagnostics ID to confirm that the upload succeeded.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# https://docs.docker.com/llms.txt

`https://docs.docker.com/llms.txt`

# Docker Documentation

Docker Documentation is the official Docker library of resources, manuals, and guides to help you containerize applications.

Use this file as a generated discovery guide for the docs site. For the complete
page index, use [llms-full.txt](https://docs.docker.com/llms-full.txt).

> MCP endpoint for structured agent access: https://mcp-docs.docker.com/mcp
> Bulk text corpus for offline indexing: https://docs.docker.com/llms-full.txt

## Primary sections
- [Get started](https://docs.docker.com/get-started/): Choose a tutorial to build and run an application, work with an AI agent safely, or set up Docker for your organization.
  Markdown: https://docs.docker.com/get-started.md
- [Guides](https://docs.docker.com/guides/): Step-by-step tutorials, organized by what you're trying to do.
  Markdown: https://docs.docker.com/guides.md
- [Manuals](https://docs.docker.com/manuals/): Learn how to install, set up, configure, and use Docker products with this collection of user guides
  Markdown: https://docs.docker.com/manuals.md
- [Reference](https://docs.docker.com/reference/): Find reference documentation for the Docker platform’s various APIs, CLIs, and file formats
  Markdown: https://docs.docker.com/reference.md


## Starter paths
- [Build and share a containerized application](https://docs.docker.com/get-started/tutorials/run-an-app/): Run a container and an application stack, build an image, and share it through Docker Hub.
- [Run your coding agent in a sandbox](https://docs.docker.com/get-started/tutorials/run-an-agent/): Move your existing full-autonomy coding-agent workflow into a disposable Docker Sandbox.
- [Roll out Docker to a pilot group](https://docs.docker.com/get-started/tutorials/admin-set-up/): Invite a pilot user, apply a Docker Desktop policy, and verify the managed experience.


## Product documentation

### AI and agents
- [Docker Agentic Platform](https://docs.docker.com/agentic-platform/): Run agents in cloud sandboxes with this experimental platform.
- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/): Run AI coding agents in isolated environments.
- [Sandboxes API and SDK](https://docs.docker.com/ai/sandboxes-api/): Create and manage cloud sandboxes from your applications.
- [MCP Catalog and Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/): Augment your AI workflow with MCP servers.
- [Gordon](https://docs.docker.com/ai/gordon/): Streamline your workflow and get the most out of the Docker ecosystem with your personal AI assistant.
- [Docker Model Runner](https://docs.docker.com/ai/model-runner/): View and manage your local models.
- [Docker Agent](https://docs.docker.com/ai/docker-agent): The open-source multi-agent solution to assist you in your tasks.
- [Docker Skills](https://docs.docker.com/ai/skills/): Docker's official skills for AI coding agents.

### Application development
- [Docker Desktop](https://docs.docker.com/desktop/): Your command center for container development.
- [Docker Offload](https://docs.docker.com/offload/): Build and run containers in the cloud.
- [Docker Build Cloud](https://docs.docker.com/build-cloud/): Build your images faster in the cloud.
- [Testcontainers](https://docs.docker.com/testcontainers/): Run containers programmatically in your preferred programming language.
- [Docker Build](https://docs.docker.com/build/): Build and ship any application anywhere.
- [Docker Engine](https://docs.docker.com/engine/): The industry-leading container runtime.
- [Docker Compose](https://docs.docker.com/compose/): Define and run multi-container applications.

### Supply chain security
- [Docker Hub](https://docs.docker.com/docker-hub/): Discover, share, and integrate container images.
- [Docker Hardened Images](https://docs.docker.com/dhi/): Secure, minimal images for trusted software delivery.
- [Docker Scout](https://docs.docker.com/scout/): Image analysis and policy evaluation.


## Reference entry points

### File formats
- [Dockerfile](https://docs.docker.com/reference/dockerfile/): Defines the contents and startup behavior of a single container.
- [Compose file](https://docs.docker.com/reference/compose-file/): Defines a multi-container application.

### Command-line interfaces
- [Docker CLI](https://docs.docker.com/reference/cli/docker/): The main Docker CLI, includes all `docker` commands.
- [Compose CLI](https://docs.docker.com/reference/cli/docker/compose/): The CLI for Docker Compose, for building and running multi-container applications.
- [Daemon CLI (dockerd)](https://docs.docker.com/reference/cli/dockerd/): Persistent process that manages containers.

### APIs
- [Sandboxes API](https://docs.docker.com/reference/api/sandboxes/latest/): Create cloud sandboxes, run processes, and manage sandbox resources.
- [Engine API](https://docs.docker.com/reference/api/engine/): The main API for Docker, provides programmatic access to a daemon.
- [Docker Hub API](https://docs.docker.com/reference/api/hub/latest/): API to interact with Docker Hub.
- [DVP Data API](https://docs.docker.com/reference/api/dvp/latest/): API for Docker Verified Publishers to fetch analytics data.
- [Registry API](https://docs.docker.com/reference/api/registry/latest/): API for Docker Registry.

## Retrieval guidance

- Prefer section landing pages above for navigation and scope selection.
- Use [llms-full.txt](https://docs.docker.com/llms-full.txt) when you need the complete documentation corpus.
- Use page-level markdown routes such as `https://docs.docker.com/engine/install.md` for clean per-page retrieval.

---

# Automated traffic detection

`https://docs.docker.com/bot-detection`

# Automated traffic detection


Ask Gordon


Copy Markdown


View Markdown

---


---


This page is used to identify automated traffic.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

---

# https://docs.docker.com/llms-full.txt

`https://docs.docker.com/llms-full.txt`

# Docker Documentation full text

> Source index: https://docs.docker.com/llms.txt
> This file contains page metadata and stable markdown URLs for bulk ingestion.

## Latest
URL:
Markdown: https://docs.docker.com/.md

## AI Governance API
URL:
Markdown: https://docs.docker.com/.md
Description: Programmatic management of Docker AI Governance policies and rules via HTTP+JSON.

## Manage company organizations, owners, and members
URL: https://docs.docker.com/accounts/company/manage/
Markdown: https://docs.docker.com/accounts/company/manage.md
Description: Manage your Docker company in Docker Home. Add organizations, invite members, manage owners, resend invitations, export a member CSV, and add subscription seats.

## Create new company
URL: https://docs.docker.com/accounts/company/new-company/
Markdown: https://docs.docker.com/accounts/company/new-company.md
Description: Learn how to create a company to centrally manage multiple organizations.

## Create a Docker account
URL: https://docs.docker.com/accounts/individual/create-account/
Markdown: https://docs.docker.com/accounts/individual/create-account.md
Description: Create a Docker ID with email, Google, or GitHub, then verify your account

## Deactivate a Docker account
URL: https://docs.docker.com/accounts/individual/deactivate-user-account/
Markdown: https://docs.docker.com/accounts/individual/deactivate-user-account.md
Description: Prerequisites and steps to deactivate an individual Docker account

## Manage a Docker account
URL: https://docs.docker.com/accounts/individual/manage-account/
Markdown: https://docs.docker.com/accounts/individual/manage-account.md
Description: Update account settings, email, password, 2FA, tokens, and connected accounts

## Activity logs
URL: https://docs.docker.com/accounts/organization/activity-logs/
Markdown: https://docs.docker.com/accounts/organization/activity-logs.md
Description: View, filter, and export organization and repository activity logs in Docker Home.

## Insights
URL: https://docs.docker.com/accounts/organization/insights/
Markdown: https://docs.docker.com/accounts/organization/insights.md
Description: Gain insights about your organization's users and their Docker usage.

## Deactivate an organization
URL: https://docs.docker.com/accounts/organization/manage/deactivate-account/
Markdown: https://docs.docker.com/accounts/organization/manage/deactivate-account.md
Description: Learn how to deactivate a Docker organization and required prerequisite steps.

## Change general organization information
URL: https://docs.docker.com/accounts/organization/manage/general-settings/
Markdown: https://docs.docker.com/accounts/organization/manage/general-settings.md
Description: Learn how to manage settings for organizations.

## Create and manage a team
URL: https://docs.docker.com/accounts/organization/manage/manage-a-team/
Markdown: https://docs.docker.com/accounts/organization/manage/manage-a-team.md
Description: Learn how to create and manage teams for your organization

## Manage licenses
URL: https://docs.docker.com/accounts/organization/manage/manage-licenses/
Markdown: https://docs.docker.com/accounts/organization/manage/manage-licenses.md
Description: View your organization's license inventory and assign licenses to teams or members by team, invitation, or automatic assignment for Docker Team or Business, AI Governance, and Offload.

## Manage usage and access for Docker products
URL: https://docs.docker.com/accounts/organization/manage/manage-products/
Markdown: https://docs.docker.com/accounts/organization/manage/manage-products.md
Description: Learn how to manage access and usage for Docker products for your organization

## Manage subscription seats
URL: https://docs.docker.com/accounts/organization/manage/manage-seats/
Markdown: https://docs.docker.com/accounts/organization/manage/manage-seats.md
Description: Add or remove seats for Docker Team and Business subscriptions

## Invite and manage organization members
URL: https://docs.docker.com/accounts/organization/manage/members/
Markdown: https://docs.docker.com/accounts/organization/manage/members.md
Description: Invite organization members in Docker Home, assign roles and licenses, manage teams, remove members with or without SCIM, and export a CSV member list.

## Convert a Docker account to an organization
URL: https://docs.docker.com/accounts/organization/setup/convert-account/
Markdown: https://docs.docker.com/accounts/organization/setup/convert-account.md
Description: Convert an individual Docker account into an organization. Keep the same Docker ID and repository namespace, then assign a new owner for shared access.

## Onboard a Docker organization
URL: https://docs.docker.com/accounts/organization/setup/onboard/
Markdown: https://docs.docker.com/accounts/organization/setup/onboard.md
Description: Invite members, configure SSO and SCIM, and enforce Docker Desktop sign-in for a Team or Business organization.

## Create a Docker organization
URL: https://docs.docker.com/accounts/organization/setup/orgs/
Markdown: https://docs.docker.com/accounts/organization/setup/orgs.md
Description: Create a Docker organization and choose its namespace and plan.

## Docker Agentic Platform FAQ
URL: https://docs.docker.com/agentic-platform/faq/
Markdown: https://docs.docker.com/agentic-platform/faq.md
Description: Find answers about Docker Agentic Platform sandboxes, access, credentials, billing, and data retention.

## Get started with Docker Agentic Platform
URL: https://docs.docker.com/agentic-platform/get-started/
Markdown: https://docs.docker.com/agentic-platform/get-started.md
Description: Run your first cloud sandbox, ask an agent to review a sample project, save the result, and pause or delete the sandbox when you're finished.

## Kits
URL: https://docs.docker.com/agentic-platform/kits/
Markdown: https://docs.docker.com/agentic-platform/kits.md
Description: Browse sandbox kits, check kit formats and Docker Hub details, or launch a public kit in Docker Agentic Platform.

## MCP
URL: https://docs.docker.com/agentic-platform/mcp/
Markdown: https://docs.docker.com/agentic-platform/mcp.md
Description: Connect predefined and custom MCP servers for Docker Agentic Platform sandboxes.

## Network policies
URL: https://docs.docker.com/agentic-platform/policies/
Markdown: https://docs.docker.com/agentic-platform/policies.md
Description: Control outbound network access from Docker Agentic Platform sandboxes.

## Docker Agentic Platform release notes
URL: https://docs.docker.com/agentic-platform/release-notes/
Markdown: https://docs.docker.com/agentic-platform/release-notes.md
Description: Review feature updates, behavior changes, and fixes in Docker Agentic Platform.

## Sandboxes
URL: https://docs.docker.com/agentic-platform/sandboxes/
Markdown: https://docs.docker.com/agentic-platform/sandboxes.md
Description: Create and manage cloud sandboxes in Docker Agentic Platform.

## Secrets
URL: https://docs.docker.com/agentic-platform/secrets/
Markdown: https://docs.docker.com/agentic-platform/secrets.md
Description: Save and manage API keys and tokens for your Docker Agentic Platform sandboxes.

## Sign up for Docker Agentic Platform
URL: https://docs.docker.com/agentic-platform/signup/
Markdown: https://docs.docker.com/agentic-platform/signup.md
Description: Activate Docker Agentic Platform access for the Console, cloud sandbox CLI, and API or SDKs.

## Docker AI overview
URL: https://docs.docker.com/ai-overview/
Markdown: https://docs.docker.com/ai-overview.md
Description: Docker's AI tools help you build, run, and manage AI-powered applications and workflows.

## Define AI Models in Docker Compose applications
URL: https://docs.docker.com/ai/compose/models-and-compose/
Markdown: https://docs.docker.com/ai/compose/models-and-compose.md
Description: Learn how to define and use AI models in Docker Compose applications using the models top-level element

## Contributing
URL: https://docs.docker.com/ai/docker-agent/community/contributing/
Markdown: https://docs.docker.com/ai/docker-agent/community/contributing.md
Description: Docker Agent is open source. Here's how to set up your development environment and contribute.

## OpenTelemetry Tracing
URL: https://docs.docker.com/ai/docker-agent/community/opentelemetry/
Markdown: https://docs.docker.com/ai/docker-agent/community/opentelemetry.md
Description: Export Docker Agent traces to any OTLP backend, including Langfuse and LangSmith, for debugging agentic workflows.

## Telemetry
URL: https://docs.docker.com/ai/docker-agent/community/telemetry/
Markdown: https://docs.docker.com/ai/docker-agent/community/telemetry.md
Description: Docker Agent collects anonymous usage data to help improve the tool. Telemetry can be disabled at any time.

## Troubleshooting
URL: https://docs.docker.com/ai/docker-agent/community/troubleshooting/
Markdown: https://docs.docker.com/ai/docker-agent/community/troubleshooting.md
Description: Common issues and how to resolve them when working with Docker Agent.

## Agents
URL: https://docs.docker.com/ai/docker-agent/concepts/agents/
Markdown: https://docs.docker.com/ai/docker-agent/concepts/agents.md
Description: Agents are the core building blocks of Docker Agent. Each agent is an AI-powered entity with a model, instructions, tools, and optional sub-agents.

## Agent Distribution
URL: https://docs.docker.com/ai/docker-agent/concepts/distribution/
Markdown: https://docs.docker.com/ai/docker-agent/concepts/distribution.md
Description: Package, share, and run agents via OCI-compatible registries — just like container images.

## Models
URL: https://docs.docker.com/ai/docker-agent/concepts/models/
Markdown: https://docs.docker.com/ai/docker-agent/concepts/models.md
Description: Models are the AI brains behind your agents. Docker Agent supports multiple providers and flexible configuration.

## Multi-Agent Systems
URL: https://docs.docker.com/ai/docker-agent/concepts/multi-agent/
Markdown: https://docs.docker.com/ai/docker-agent/concepts/multi-agent.md
Description: Build teams of specialized agents that collaborate and delegate tasks to each other.

## Tools
URL: https://docs.docker.com/ai/docker-agent/concepts/tools/
Markdown: https://docs.docker.com/ai/docker-agent/concepts/tools.md
Description: Tools give agents the ability to interact with the world — read files, run commands, search the web, query databases, and more.

## Agent Configuration
URL: https://docs.docker.com/ai/docker-agent/configuration/agents/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/agents.md
Description: Complete reference for defining agents in your YAML configuration.

## Ignoring files
URL: https://docs.docker.com/ai/docker-agent/configuration/agentsignore/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/agentsignore.md
Description: Hide files from the agent with a .agentsignore file, using the same syntax as .gitignore.

## Budget
URL: https://docs.docker.com/ai/docker-agent/configuration/budget/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/budget.md
Description: Cap what a single run may spend in money, tokens, or working time.

## Custom Commands
URL: https://docs.docker.com/ai/docker-agent/configuration/commands/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/commands.md
Description: Define slash commands that send prompts, open URLs, or switch agents, and reuse them across agents with top-level command groups.

## Flavors
URL: https://docs.docker.com/ai/docker-agent/configuration/flavors/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/flavors.md
Description: Ship one agent file with named variants, enabled at run time as YAML patches.

## HCL Configuration
URL: https://docs.docker.com/ai/docker-agent/configuration/hcl/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/hcl.md
Description: Write Docker Agent configs in HCL instead of YAML, using labeled blocks, heredocs, and the same underlying schema.

## Hooks
URL: https://docs.docker.com/ai/docker-agent/configuration/hooks/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/hooks.md
Description: Run shell commands at various points during agent execution for deterministic control over behavior.

## Model Configuration
URL: https://docs.docker.com/ai/docker-agent/configuration/models/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/models.md
Description: Complete reference for defining models with providers, parameters, and reasoning settings.

## Configuration Overview
URL: https://docs.docker.com/ai/docker-agent/configuration/overview/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/overview.md
Description: Docker Agent uses YAML or HCL configuration files to define agents, models, tools, and their relationships.

## Permissions
URL: https://docs.docker.com/ai/docker-agent/configuration/permissions/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/permissions.md
Description: Control which tools can execute automatically, require confirmation, or are blocked entirely.

## Model Routing
URL: https://docs.docker.com/ai/docker-agent/configuration/routing/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/routing.md
Description: Route requests to different models based on the content of user messages.

## Sandbox Mode
URL: https://docs.docker.com/ai/docker-agent/configuration/sandbox/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/sandbox.md
Description: Run agents in an isolated sandbox VM managed by sbx.

## Structured Output
URL: https://docs.docker.com/ai/docker-agent/configuration/structured-output/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/structured-output.md
Description: Force the agent to respond with JSON matching a specific schema.

## Tool Configuration
URL: https://docs.docker.com/ai/docker-agent/configuration/tools/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/tools.md
Description: Complete reference for configuring built-in tools, MCP tools, and Docker-based tools.

## User Settings
URL: https://docs.docker.com/ai/docker-agent/configuration/user-settings/
Markdown: https://docs.docker.com/ai/docker-agent/configuration/user-settings.md
Description: Full reference for the global settings block in ~/.config/cagent/config.yaml: theme, layout, YOLO, sound, snapshots, permissions, hooks, keybindings, and how they interact with agent config and CLI flags.

## A2A Protocol
URL: https://docs.docker.com/ai/docker-agent/features/a2a/
Markdown: https://docs.docker.com/ai/docker-agent/features/a2a.md
Description: Expose Docker Agent agents via Google's Agent-to-Agent (A2A) protocol for interoperability with other agent frameworks.

## ACP (Agent Client Protocol)
URL: https://docs.docker.com/ai/docker-agent/features/acp/
Markdown: https://docs.docker.com/ai/docker-agent/features/acp.md
Description: Expose Docker Agent agents via the Agent Client Protocol for integration with ACP-compatible hosts like VS Code, IDEs, and other developer tools.

## API Server
URL: https://docs.docker.com/ai/docker-agent/features/api-server/
Markdown: https://docs.docker.com/ai/docker-agent/features/api-server.md
Description: Expose your agents via an HTTP API for programmatic access, web frontends, and integrations.

## Kanban Board
URL: https://docs.docker.com/ai/docker-agent/features/board/
Markdown: https://docs.docker.com/ai/docker-agent/features/board.md
Description: Orchestrate multiple agents from a Kanban TUI: each card runs an agent in a tmux session on an isolated git worktree.

## Chat Server
URL: https://docs.docker.com/ai/docker-agent/features/chat-server/
Markdown: https://docs.docker.com/ai/docker-agent/features/chat-server.md
Description: Expose your agents through an OpenAI-compatible Chat Completions API so any tool that already speaks OpenAI can drive a Docker Agent agent.

## CLI Reference
URL: https://docs.docker.com/ai/docker-agent/features/cli/
Markdown: https://docs.docker.com/ai/docker-agent/features/cli.md
Description: Complete reference for all Docker Agent command-line commands and flags.

## Code Mode
URL: https://docs.docker.com/ai/docker-agent/features/code-mode/
Markdown: https://docs.docker.com/ai/docker-agent/features/code-mode.md
Description: Let an agent write JavaScript that orchestrates several tool calls in one turn instead of calling tools one at a time.

## Evaluation
URL: https://docs.docker.com/ai/docker-agent/features/evaluation/
Markdown: https://docs.docker.com/ai/docker-agent/features/evaluation.md
Description: Measure agent quality with automated evaluations — tool call accuracy, response relevance, output size, and more.

## Coding Harnesses
URL: https://docs.docker.com/ai/docker-agent/features/harnesses/
Markdown: https://docs.docker.com/ai/docker-agent/features/harnesses.md
Description: Delegate coding tasks to external AI coding CLIs (Claude Code, Codex, opencode) as sub-agents.

## MCP Mode
URL: https://docs.docker.com/ai/docker-agent/features/mcp-mode/
Markdown: https://docs.docker.com/ai/docker-agent/features/mcp-mode.md
Description: Expose your Docker Agent agents as MCP tools for use in Claude Desktop, Claude Code, and other MCP-compatible applications.

## Remote MCP Servers
URL: https://docs.docker.com/ai/docker-agent/features/remote-mcp/
Markdown: https://docs.docker.com/ai/docker-agent/features/remote-mcp.md
Description: Connect Docker Agent to cloud services via remote MCP servers with built-in OAuth authentication.

## Sessions
URL: https://docs.docker.com/ai/docker-agent/features/sessions/
Markdown: https://docs.docker.com/ai/docker-agent/features/sessions.md
Description: How Docker Agent stores conversations, resumes them across runs, and tracks their token cost.

## Skills
URL: https://docs.docker.com/ai/docker-agent/features/skills/
Markdown: https://docs.docker.com/ai/docker-agent/features/skills.md
Description: Skills provide specialized instructions that agents can load on demand when a task matches a skill's description.

## Snapshots
URL: https://docs.docker.com/ai/docker-agent/features/snapshots/
Markdown: https://docs.docker.com/ai/docker-agent/features/snapshots.md
Description: Shadow-git snapshots capture your workspace at turn boundaries so you can review what an agent changed and undo it without touching your real git history.

## Terminal UI (TUI)
URL: https://docs.docker.com/ai/docker-agent/features/tui/
Markdown: https://docs.docker.com/ai/docker-agent/features/tui.md
Description: Docker Agent's default interface is a rich, interactive terminal UI with file attachments, themes, session management, and more.

## Installation
URL: https://docs.docker.com/ai/docker-agent/getting-started/installation/
Markdown: https://docs.docker.com/ai/docker-agent/getting-started/installation.md
Description: Get Docker Agent running on your system in minutes.

## Introduction
URL: https://docs.docker.com/ai/docker-agent/getting-started/introduction/
Markdown: https://docs.docker.com/ai/docker-agent/getting-started/introduction.md
Description: Docker Agent is a multi-agent runtime that lets you build, run, and share AI agents with a YAML or HCL config — no glue code required.

## Quick Start
URL: https://docs.docker.com/ai/docker-agent/getting-started/quickstart/
Markdown: https://docs.docker.com/ai/docker-agent/getting-started/quickstart.md
Description: Get up and running with Docker Agent in under 5 minutes. Pick whichever path suits you best.

## Set Up a Model
URL: https://docs.docker.com/ai/docker-agent/getting-started/set-up-a-model/
Markdown: https://docs.docker.com/ai/docker-agent/getting-started/set-up-a-model.md
Description: Make a model available to Docker Agent: connect a cloud provider, run a local model with Docker Model Runner, or register a custom OpenAI-compatible endpoint.

## Managing Context & Compaction
URL: https://docs.docker.com/ai/docker-agent/guides/compaction/
Markdown: https://docs.docker.com/ai/docker-agent/guides/compaction.md
Description: How to keep long Docker Agent sessions from filling the model's context window: automatic and on-demand compaction, trimming tool results, and reading the context gauge.

## Go SDK
URL: https://docs.docker.com/ai/docker-agent/guides/go-sdk/
Markdown: https://docs.docker.com/ai/docker-agent/guides/go-sdk.md
Description: Use Docker Agent as a Go library to embed AI agents in your applications.

## Running Agents Headless & in CI
URL: https://docs.docker.com/ai/docker-agent/guides/headless/
Markdown: https://docs.docker.com/ai/docker-agent/guides/headless.md
Description: Run Docker Agent without a TUI: structured JSON output, event hooks, sandboxed CI isolation, and a GitHub Actions example.

## Managing Secrets
URL: https://docs.docker.com/ai/docker-agent/guides/secrets/
Markdown: https://docs.docker.com/ai/docker-agent/guides/secrets.md
Description: How to securely provide API keys and credentials to Docker Agent using environment variables, env files, Docker Compose secrets, and 1Password references.

## Thinking / Reasoning
URL: https://docs.docker.com/ai/docker-agent/guides/thinking/
Markdown: https://docs.docker.com/ai/docker-agent/guides/thinking.md
Description: Control how much a model reasons before responding. Works across OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Docker Model Runner.

## Tips & Best Practices
URL: https://docs.docker.com/ai/docker-agent/guides/tips/
Markdown: https://docs.docker.com/ai/docker-agent/guides/tips.md
Description: Expert guidance for building effective, efficient, and secure agents.

## Anthropic
URL: https://docs.docker.com/ai/docker-agent/providers/anthropic/
Markdown: https://docs.docker.com/ai/docker-agent/providers/anthropic.md
Description: Use Claude Sonnet 4, Claude Sonnet 4.5, and other Anthropic models with Docker Agent.

## Baseten
URL: https://docs.docker.com/ai/docker-agent/providers/baseten/
Markdown: https://docs.docker.com/ai/docker-agent/providers/baseten.md
Description: Use Baseten AI models with Docker Agent.

## AWS Bedrock
URL: https://docs.docker.com/ai/docker-agent/providers/bedrock/
Markdown: https://docs.docker.com/ai/docker-agent/providers/bedrock.md
Description: Access Claude, Nova, Llama, and more through AWS infrastructure with enterprise-grade security and compliance.

## Cerebras
URL: https://docs.docker.com/ai/docker-agent/providers/cerebras/
Markdown: https://docs.docker.com/ai/docker-agent/providers/cerebras.md
Description: Use Cerebras models with Docker Agent.

## ChatGPT (OpenAI account)
URL: https://docs.docker.com/ai/docker-agent/providers/chatgpt/
Markdown: https://docs.docker.com/ai/docker-agent/providers/chatgpt.md
Description: Use your ChatGPT Plus/Pro/Business subscription with Docker Agent by signing in with your OpenAI account, no API key needed.

## Cloudflare AI Gateway
URL: https://docs.docker.com/ai/docker-agent/providers/cloudflare-ai-gateway/
Markdown: https://docs.docker.com/ai/docker-agent/providers/cloudflare-ai-gateway.md
Description: Use Cloudflare AI Gateway models with Docker Agent.

## Cloudflare Workers AI
URL: https://docs.docker.com/ai/docker-agent/providers/cloudflare-workers-ai/
Markdown: https://docs.docker.com/ai/docker-agent/providers/cloudflare-workers-ai.md
Description: Use Cloudflare Workers AI models with Docker Agent.

## Provider Definitions
URL: https://docs.docker.com/ai/docker-agent/providers/custom/
Markdown: https://docs.docker.com/ai/docker-agent/providers/custom.md
Description: Define reusable provider configurations with shared defaults for any provider type — OpenAI, Anthropic, Google, Bedrock, and more.

## DeepSeek
URL: https://docs.docker.com/ai/docker-agent/providers/deepseek/
Markdown: https://docs.docker.com/ai/docker-agent/providers/deepseek.md
Description: Use DeepSeek models with Docker Agent.

## Docker Model Runner
URL: https://docs.docker.com/ai/docker-agent/providers/dmr/
Markdown: https://docs.docker.com/ai/docker-agent/providers/dmr.md
Description: Run AI models locally with Docker — no API keys, no costs, full data privacy.

## Fireworks AI
URL: https://docs.docker.com/ai/docker-agent/providers/fireworks/
Markdown: https://docs.docker.com/ai/docker-agent/providers/fireworks.md
Description: Use Fireworks AI models with Docker Agent.

## GitHub Copilot
URL: https://docs.docker.com/ai/docker-agent/providers/github-copilot/
Markdown: https://docs.docker.com/ai/docker-agent/providers/github-copilot.md
Description: Use GitHub Copilot's hosted models (GPT-4o, Claude, Gemini, and more) with Docker Agent through your GitHub subscription.

## Google Gemini
URL: https://docs.docker.com/ai/docker-agent/providers/google/
Markdown: https://docs.docker.com/ai/docker-agent/providers/google.md
Description: Use Gemini 2.5 Flash, Gemini 3 Pro, and other Google models with Docker Agent.

## Groq
URL: https://docs.docker.com/ai/docker-agent/providers/groq/
Markdown: https://docs.docker.com/ai/docker-agent/providers/groq.md
Description: Use Groq fast-inference models with Docker Agent.

## Hugging Face
URL: https://docs.docker.com/ai/docker-agent/providers/huggingface/
Markdown: https://docs.docker.com/ai/docker-agent/providers/huggingface.md
Description: Use Hugging Face Inference Providers with Docker Agent.

## Local Models (Ollama, vLLM, LocalAI)
URL: https://docs.docker.com/ai/docker-agent/providers/local/
Markdown: https://docs.docker.com/ai/docker-agent/providers/local.md
Description: Run Docker Agent with locally hosted models for privacy, offline use, or cost savings.

## MiniMax
URL: https://docs.docker.com/ai/docker-agent/providers/minimax/
Markdown: https://docs.docker.com/ai/docker-agent/providers/minimax.md
Description: Use MiniMax AI models with Docker Agent.

## Mistral
URL: https://docs.docker.com/ai/docker-agent/providers/mistral/
Markdown: https://docs.docker.com/ai/docker-agent/providers/mistral.md
Description: Use Mistral AI models with Docker Agent.

## Moonshot AI
URL: https://docs.docker.com/ai/docker-agent/providers/moonshot/
Markdown: https://docs.docker.com/ai/docker-agent/providers/moonshot.md
Description: Use Moonshot AI (Kimi) models with Docker Agent.

## Nebius
URL: https://docs.docker.com/ai/docker-agent/providers/nebius/
Markdown: https://docs.docker.com/ai/docker-agent/providers/nebius.md
Description: Use Nebius AI models with Docker Agent.

## NVIDIA NIM
URL: https://docs.docker.com/ai/docker-agent/providers/nvidia/
Markdown: https://docs.docker.com/ai/docker-agent/providers/nvidia.md
Description: Use NVIDIA NIM models with Docker Agent.

## OpenAI
URL: https://docs.docker.com/ai/docker-agent/providers/openai/
Markdown: https://docs.docker.com/ai/docker-agent/providers/openai.md
Description: Use GPT-5.6, GPT-4o, GPT-5, GPT-5-mini, and other OpenAI models with Docker Agent.

## OpenCode Go
URL: https://docs.docker.com/ai/docker-agent/providers/opencode-go/
Markdown: https://docs.docker.com/ai/docker-agent/providers/opencode-go.md
Description: Use OpenCode Go models with Docker Agent.

## OpenCode Zen
URL: https://docs.docker.com/ai/docker-agent/providers/opencode-zen/
Markdown: https://docs.docker.com/ai/docker-agent/providers/opencode-zen.md
Description: Use OpenCode Zen models with Docker Agent.

## OpenRouter
URL: https://docs.docker.com/ai/docker-agent/providers/openrouter/
Markdown: https://docs.docker.com/ai/docker-agent/providers/openrouter.md
Description: Use OpenRouter models with Docker Agent.

## Model Providers
URL: https://docs.docker.com/ai/docker-agent/providers/overview/
Markdown: https://docs.docker.com/ai/docker-agent/providers/overview.md
Description: Docker Agent supports multiple AI model providers. Choose the right one for your use case, or use multiple providers in the same configuration.

## OVHcloud
URL: https://docs.docker.com/ai/docker-agent/providers/ovhcloud/
Markdown: https://docs.docker.com/ai/docker-agent/providers/ovhcloud.md
Description: Use OVHcloud AI Endpoints models with Docker Agent.

## Together AI
URL: https://docs.docker.com/ai/docker-agent/providers/together/
Markdown: https://docs.docker.com/ai/docker-agent/providers/together.md
Description: Use Together AI models with Docker Agent.

## Vercel AI Gateway
URL: https://docs.docker.com/ai/docker-agent/providers/vercel/
Markdown: https://docs.docker.com/ai/docker-agent/providers/vercel.md
Description: Use Vercel AI Gateway models with Docker Agent.

## xAI (Grok)
URL: https://docs.docker.com/ai/docker-agent/providers/xai/
Markdown: https://docs.docker.com/ai/docker-agent/providers/xai.md
Description: Use xAI's Grok models with Docker Agent.

## A2A Tool
URL: https://docs.docker.com/ai/docker-agent/tools/a2a/
Markdown: https://docs.docker.com/ai/docker-agent/tools/a2a.md
Description: Connect to remote agents via the Agent-to-Agent protocol.

## API Tool
URL: https://docs.docker.com/ai/docker-agent/tools/api/
Markdown: https://docs.docker.com/ai/docker-agent/tools/api.md
Description: Create custom tools that call HTTP APIs.

## Background Agents Tool
URL: https://docs.docker.com/ai/docker-agent/tools/background-agents/
Markdown: https://docs.docker.com/ai/docker-agent/tools/background-agents.md
Description: Dispatch work to sub-agents concurrently and collect results asynchronously.

## Background Jobs Tool
URL: https://docs.docker.com/ai/docker-agent/tools/background-jobs/
Markdown: https://docs.docker.com/ai/docker-agent/tools/background-jobs.md
Description: Run and manage long-running shell commands.

## Fetch Tool
URL: https://docs.docker.com/ai/docker-agent/tools/fetch/
Markdown: https://docs.docker.com/ai/docker-agent/tools/fetch.md
Description: Read content from HTTP/HTTPS URLs.

## Filesystem Tool
URL: https://docs.docker.com/ai/docker-agent/tools/filesystem/
Markdown: https://docs.docker.com/ai/docker-agent/tools/filesystem.md
Description: Read, write, list, search, and navigate files and directories.

## Git Tool
URL: https://docs.docker.com/ai/docker-agent/tools/git/
Markdown: https://docs.docker.com/ai/docker-agent/tools/git.md
Description: Read-only inspection of the working git repository.

## Handoff Tool
URL: https://docs.docker.com/ai/docker-agent/tools/handoff/
Markdown: https://docs.docker.com/ai/docker-agent/tools/handoff.md
Description: Hand off the active conversation to another local agent defined in the same config.

## LSP Tool
URL: https://docs.docker.com/ai/docker-agent/tools/lsp/
Markdown: https://docs.docker.com/ai/docker-agent/tools/lsp.md
Description: Connect to Language Server Protocol servers for code intelligence.

## MCP Catalog Tool
URL: https://docs.docker.com/ai/docker-agent/tools/mcp-catalog/
Markdown: https://docs.docker.com/ai/docker-agent/tools/mcp-catalog.md
Description: Let the agent discover and activate remote MCP servers from the Docker MCP Catalog on demand.

## MCP Tool
URL: https://docs.docker.com/ai/docker-agent/tools/mcp/
Markdown: https://docs.docker.com/ai/docker-agent/tools/mcp.md
Description: Extend agents with external tools via the Model Context Protocol.

## Memory Tool
URL: https://docs.docker.com/ai/docker-agent/tools/memory/
Markdown: https://docs.docker.com/ai/docker-agent/tools/memory.md
Description: Persistent key-value storage backed by SQLite for cross-session recall.

## Model Picker Tool
URL: https://docs.docker.com/ai/docker-agent/tools/model-picker/
Markdown: https://docs.docker.com/ai/docker-agent/tools/model-picker.md
Description: Let the agent pick between several models per turn.

## Open URL Tool
URL: https://docs.docker.com/ai/docker-agent/tools/open-url/
Markdown: https://docs.docker.com/ai/docker-agent/tools/open-url.md
Description: Open a fixed URL in the user's default browser.

## OpenAPI Tool
URL: https://docs.docker.com/ai/docker-agent/tools/openapi/
Markdown: https://docs.docker.com/ai/docker-agent/tools/openapi.md
Description: Automatically generate tools from an OpenAPI specification.

## Plan Tool
URL: https://docs.docker.com/ai/docker-agent/tools/plan/
Markdown: https://docs.docker.com/ai/docker-agent/tools/plan.md
Description: Shared persistent scratchpad for multi-agent collaboration.

## RAG Tool
URL: https://docs.docker.com/ai/docker-agent/tools/rag/
Markdown: https://docs.docker.com/ai/docker-agent/tools/rag.md
Description: Give your agents access to document knowledge bases with background indexing, multiple retrieval strategies, and hybrid search.

## Scheduler Tool
URL: https://docs.docker.com/ai/docker-agent/tools/scheduler/
Markdown: https://docs.docker.com/ai/docker-agent/tools/scheduler.md
Description: Schedule instructions to run at a time or on a recurring interval.

## Script Tool
URL: https://docs.docker.com/ai/docker-agent/tools/script/
Markdown: https://docs.docker.com/ai/docker-agent/tools/script.md
Description: Define custom shell scripts as named tools with typed parameters.

## Session Context Tool
URL: https://docs.docker.com/ai/docker-agent/tools/session_context/
Markdown: https://docs.docker.com/ai/docker-agent/tools/session_context.md
Description: Reference a previous session as context in the current one.

## Session Plan Tool
URL: https://docs.docker.com/ai/docker-agent/tools/session_plan/
Markdown: https://docs.docker.com/ai/docker-agent/tools/session_plan.md
Description: Per-session plan tracker for the draft, review, execute workflow.

## Shell Tool
URL: https://docs.docker.com/ai/docker-agent/tools/shell/
Markdown: https://docs.docker.com/ai/docker-agent/tools/shell.md
Description: Execute arbitrary shell commands in the user's environment.

## Tasks Tool
URL: https://docs.docker.com/ai/docker-agent/tools/tasks/
Markdown: https://docs.docker.com/ai/docker-agent/tools/tasks.md
Description: Persistent task database with priorities and dependencies, shared across sessions.

## Think Tool
URL: https://docs.docker.com/ai/docker-agent/tools/think/
Markdown: https://docs.docker.com/ai/docker-agent/tools/think.md
Description: Step-by-step reasoning scratchpad for planning and decision-making.

## Todo Tool
URL: https://docs.docker.com/ai/docker-agent/tools/todo/
Markdown: https://docs.docker.com/ai/docker-agent/tools/todo.md
Description: Task list management for complex multi-step workflows.

## Transfer Task Tool
URL: https://docs.docker.com/ai/docker-agent/tools/transfer-task/
Markdown: https://docs.docker.com/ai/docker-agent/tools/transfer-task.md
Description: Delegate tasks to sub-agents in multi-agent setups.

## User Prompt Tool
URL: https://docs.docker.com/ai/docker-agent/tools/user-prompt/
Markdown: https://docs.docker.com/ai/docker-agent/tools/user-prompt.md
Description: Ask the user questions and collect interactive input during agent execution.

## Webhook Tool
URL: https://docs.docker.com/ai/docker-agent/tools/webhook/
Markdown: https://docs.docker.com/ai/docker-agent/tools/webhook.md
Description: Reliable outbound notifications to Slack, Discord, Telegram, IFTTT, and more.

## Gordon's capabilities
URL: https://docs.docker.com/ai/gordon/concepts/capabilities/
Markdown: https://docs.docker.com/ai/gordon/concepts/capabilities.md
Description: Understand what Gordon can do and the tools it has access to

## Data privacy and Gordon
URL: https://docs.docker.com/ai/gordon/concepts/data-privacy/
Markdown: https://docs.docker.com/ai/gordon/concepts/data-privacy.md
Description: How Gordon handles your data and what information is collected

## Using Gordon via CLI
URL: https://docs.docker.com/ai/gordon/how-to/cli/
Markdown: https://docs.docker.com/ai/gordon/how-to/cli.md
Description: Access and use Gordon through the docker ai command

## Configure Gordon's tools
URL: https://docs.docker.com/ai/gordon/how-to/configure-tools/
Markdown: https://docs.docker.com/ai/gordon/how-to/configure-tools.md
Description: Enable and disable Gordon's built-in tools based on your needs

## Using Gordon in Docker Desktop
URL: https://docs.docker.com/ai/gordon/how-to/docker-desktop/
Markdown: https://docs.docker.com/ai/gordon/how-to/docker-desktop.md
Description: Access and use Gordon through the Docker Desktop graphical interface

## Gordon's permission model
URL: https://docs.docker.com/ai/gordon/how-to/permissions/
Markdown: https://docs.docker.com/ai/gordon/how-to/permissions.md
Description: How Gordon's ask-first approach keeps you in control

## Gordon usage limits and tiers
URL: https://docs.docker.com/ai/gordon/usage-limits/
Markdown: https://docs.docker.com/ai/gordon/usage-limits.md
Description: Gordon subscription tiers and usage limits for Docker Desktop and the CLI

## Gordon use cases and examples
URL: https://docs.docker.com/ai/gordon/use-cases/
Markdown: https://docs.docker.com/ai/gordon/use-cases.md
Description: Example prompts for common Docker workflows

## Docker MCP Catalog
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog.md
Description: Browse Docker's curated collection of verified MCP servers, and create custom catalogs for your team or organization.

## Use MCP Toolkit from the CLI
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/cli/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/cli.md
Description: Manage MCP profiles, servers, and catalogs using Docker MCP CLI.

## Dynamic MCP
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp.md
Description: Discover and add MCP servers on-demand using natural language with Dynamic MCP servers

## MCP Toolkit FAQs
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/faqs/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/faqs.md
Description: Frequently asked questions related to MCP Catalog and Toolkit security

## Get started with Docker MCP Toolkit
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started.md
Description: Learn how to quickly install and use the MCP Toolkit to set up servers and clients.

## MCP Gateway
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway.md
Description: Docker's MCP Gateway provides secure, centralized, and scalable orchestration of AI tools through containerized MCP servers, empowering developers, operators, and security teams.

## MCP Profiles
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/profiles/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/profiles.md
Description: Organize MCP servers into profiles for different projects and environments

## Docker MCP Toolkit
URL: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
Markdown: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit.md
Description: Use the MCP Toolkit to set up MCP servers and MCP clients.

## DMR REST API
URL: https://docs.docker.com/ai/model-runner/api-reference/
Markdown: https://docs.docker.com/ai/model-runner/api-reference.md
Description: Reference documentation for the Docker Model Runner REST API endpoints, including OpenAI, Anthropic, and Ollama compatibility.

## Configuration options
URL: https://docs.docker.com/ai/model-runner/configuration/
Markdown: https://docs.docker.com/ai/model-runner/configuration.md
Description: Configure context size, runtime parameters, and model behavior in Docker Model Runner.

## DMR examples
URL: https://docs.docker.com/ai/model-runner/examples/
Markdown: https://docs.docker.com/ai/model-runner/examples.md
Description: Example projects and CI/CD workflows for Docker Model Runner.

## Get started with DMR
URL: https://docs.docker.com/ai/model-runner/get-started/
Markdown: https://docs.docker.com/ai/model-runner/get-started.md
Description: How to install, enable, and use Docker Model Runner to manage and run AI models.

## IDE and tool integrations
URL: https://docs.docker.com/ai/model-runner/ide-integrations/
Markdown: https://docs.docker.com/ai/model-runner/ide-integrations.md
Description: Configure popular AI coding assistants and tools to use Docker Model Runner as their backend.

## Inference engines
URL: https://docs.docker.com/ai/model-runner/inference-engines/
Markdown: https://docs.docker.com/ai/model-runner/inference-engines.md
Description: Learn about the llama.cpp, vLLM, and Diffusers inference engines in Docker Model Runner.

## Open WebUI integration
URL: https://docs.docker.com/ai/model-runner/openwebui-integration/
Markdown: https://docs.docker.com/ai/model-runner/openwebui-integration.md
Description: Set up Open WebUI as a ChatGPT-like interface for Docker Model Runner.

## Authentication and authorization
URL: https://docs.docker.com/ai/sandboxes-api/authentication/
Markdown: https://docs.docker.com/ai/sandboxes-api/authentication.md
Description: Authenticate requests to the Docker Sandboxes API with a personal access token or browser sign-in, and learn which permissions your application needs.

## Docker Sandboxes API concepts
URL: https://docs.docker.com/ai/sandboxes-api/concepts/
Markdown: https://docs.docker.com/ai/sandboxes-api/concepts.md
Description: Learn how kits and images define a cloud sandbox, how to connect to it, and how to manage resources throughout their lifecycle.

## Add a Docker credential for cloud sandboxes
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/add-a-docker-credential-for-cloud-sandboxes/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/add-a-docker-credential-for-cloud-sandboxes.md
Description: Exchange a Docker OIDC identity token for a credential that the service stores for your sandboxes to use.

## Run agents with kits
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/add-tools-with-kits/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/add-tools-with-kits.md
Description: Discover the available kits, launch an agent sandbox, and run work inside it.

## Attach persistent storage
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/attach-persistent-storage/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/attach-persistent-storage.md
Description: Create a volume, mount it into a new sandbox so its data outlives the sandbox, and delete the volume when you no longer need it.

## Clone a cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/clone-a-cloud-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/clone-a-cloud-sandbox.md
Description: Read how a running sandbox was configured, then create a second sandbox with the same image and environment.

## Authenticate to Docker
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/connect-to-cloud-with-a-bearer-token/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/connect-to-cloud-with-a-bearer-token.md
Description: Sign in interactively, use a Docker personal access token, or supply an access token from your application.

## Control what a sandbox can reach
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/control-what-a-sandbox-can-reach/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/control-what-a-sandbox-can-reach.md
Description: Attach your account's network policies to a new sandbox, read the policy the service enforces, and review which destinations it allowed or blocked.

## Copy a file into a cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/copy-a-file-into-a-cloud-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/copy-a-file-into-a-cloud-sandbox.md
Description: Create a directory inside a running cloud sandbox, write one file into it from memory, and read the size the write reports back.

## Create your first sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/create-your-first-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/create-your-first-sandbox.md
Description: Launch a kit, run a command in its sandbox, and inspect the result.

## Delete a cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/delete-a-cloud-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/delete-a-cloud-sandbox.md
Description: Delete a sandbox you have read back and wait until it is gone, with the option to override a refusal based on its current state.

## Expose a port from a cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/expose-a-port-from-a-cloud-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/expose-a-port-from-a-cloud-sandbox.md
Description: Publish a TCP port that a program inside a cloud sandbox listens on, read back the URL that reaches it, list the sandbox's published ports, and withdraw the publication.

## Find a process you lost track of
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/find-a-process-you-lost-track-of/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/find-a-process-you-lost-track-of.md
Description: Look up a running process by the session tag you gave it when you created it, then pick up its output from the resume point its own report publishes.

## Get a stored secret into a sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/get-a-stored-secret-into-a-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/get-a-stored-secret-into-a-sandbox.md
Description: Store a credential once, then pass its resource name when creating a sandbox so the sandbox starts with that secret attached.

## Get an SSH certificate
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/get-an-ssh-certificate/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/get-an-ssh-certificate.md
Description: Have the service sign your SSH public key for one sandbox and return the host, port, username, and host keys your SSH client needs.

## Get image pull URLs
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/get-image-pull-urls/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/get-image-pull-urls.md
Description: Get the manifest details and short-lived download URLs for a managed image so a registry tool can pull its contents.

## Give a sandbox an MCP gateway
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/give-a-sandbox-an-mcp-gateway/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/give-a-sandbox-an-mcp-gateway.md
Description: Configure MCP tools when launching a kit, then inspect, authorize, and manage the gateway.

## Handle errors and degradation
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/handle-errors-and-degradation/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/handle-errors-and-degradation.md
Description: Tell an API refusal, a failed sandbox transition, and a nonzero command exit apart, and read the code and details each one carries.

## Keep a cloud sandbox running
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/keep-a-cloud-sandbox-running/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/keep-a-cloud-sandbox-running.md
Description: Choose a sandbox's lifetime and what happens when it ends, then renew the lifetime before the deadline passes.

## Let a stopped sandbox resume on demand
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/let-a-stopped-sandbox-resume-on-demand/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/let-a-stopped-sandbox-resume-on-demand.md
Description: Choose at creation whether a stopped cloud sandbox starts itself when a request arrives at one of its published ports, then read back the setting in force.

## Manage cloud secrets
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/manage-cloud-secrets/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/manage-cloud-secrets.md
Description: Store a token as a stored secret, list your secrets' metadata, replace the token, and delete the secret.

## Manage network policies
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/manage-network-policies/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/manage-network-policies.md
Description: Create, read, update, and delete personal network policies through the SDK.

## Page through and filter lists
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/page-through-and-filter-lists/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/page-through-and-filter-lists.md
Description: Walk every page of a list with the SDK's iterators, and narrow a list on the server with a filter and an ordering.

## Read files out of a sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/read-files-out-of-a-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/read-files-out-of-a-sandbox.md
Description: List a directory in a running cloud sandbox, download files from it into memory, then move or remove paths inside it.

## Recover when the endpoint moves
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/recover-when-the-endpoint-moves/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/recover-when-the-endpoint-moves.md
Description: Read a sandbox again to learn its current endpoint, then run one command through a connection built for that endpoint.

## Register and manage an image
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/register-and-manage-an-image/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/register-and-manage-an-image.md
Description: Register an image with Cloud Sandboxes, get the target to push its content to, check when it is ready, list your images, and delete one you no longer need.

## Retry without creating duplicates
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/retry-without-creating-duplicates/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/retry-without-creating-duplicates.md
Description: Retry a sandbox or process create under one request ID so a failure you can't interpret never leaves two copies behind.

## Run a complete example
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-a-complete-example/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-a-complete-example.md
Description: Sign in, launch the shell kit, print a greeting, and clean up with one runnable program.

## Run an interactive shell in a cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-an-interactive-shell-in-a-cloud-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-an-interactive-shell-in-a-cloud-sandbox.md
Description: Start a shell on a pseudo-terminal, send it input and read its output over one connection, connect again and pick up the output the service kept, and stop it.

## Run something that produces real output
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-something-that-produces-real-output/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-something-that-produces-real-output.md
Description: Choose between a call that returns a command's captured output when it finishes and a process whose output you read while it runs.

## Run work across many sandboxes
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-work-across-many-sandboxes/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-work-across-many-sandboxes.md
Description: Run one command on every running sandbox you hold, a bounded number at a time, and read one answer per sandbox even when some of them fail.

## Run your first command
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-first-command/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-first-command.md
Description: Connect to a running sandbox, run a command in it, and tell a command that exited unsuccessfully apart from a call that failed.

## Run your own container image
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-own-container-image/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-own-container-image.md
Description: Start a sandbox from a container image in a registry you name, instead of from a managed image.

## Send values the API accepts
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/send-values-the-api-accepts/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/send-values-the-api-accepts.md
Description: Build a create request whose durations, counts, and flags mean what you intend, then read back the values the service settled on.

## Snapshot and fork a sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/snapshot-and-fork-a-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/snapshot-and-fork-a-sandbox.md
Description: Capture the state of a running sandbox as a snapshot, then start a new sandbox from that snapshot.

## Stop and restart a sandbox
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/stop-and-restart-a-sandbox/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/stop-and-restart-a-sandbox.md
Description: Stop a running sandbox without deleting it, wait for the stop to settle, and start the same sandbox again when you need it.

## What your workload starts with
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/what-your-workload-starts-with/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/what-your-workload-starts-with.md
Description: Read the environment variables every command in a sandbox starts with, and see which source wins when two of them set the same name.

## Work within the limits
URL: https://docs.docker.com/ai/sandboxes-api/cookbook/work-within-the-limits/
Markdown: https://docs.docker.com/ai/sandboxes-api/cookbook/work-within-the-limits.md
Description: Choose a supported compute size, understand account quotas, and handle refusals without endless retries.

## Errors and retries
URL: https://docs.docker.com/ai/sandboxes-api/errors/
Markdown: https://docs.docker.com/ai/sandboxes-api/errors.md
Description: Handle Docker Sandboxes API errors, recover from failed waits, and retry requests without duplicating work.

## Run your first cloud sandbox
URL: https://docs.docker.com/ai/sandboxes-api/get-started/
Markdown: https://docs.docker.com/ai/sandboxes-api/get-started.md
Description: Use the TypeScript SDK to create a cloud sandbox, run a command, and delete the sandbox.

## Install the Docker Sandboxes SDK
URL: https://docs.docker.com/ai/sandboxes-api/install/
Markdown: https://docs.docker.com/ai/sandboxes-api/install.md
Description: Install and use the Docker Sandboxes SDK in your JavaScript or TypeScript application.

## Compute sizes and limits
URL: https://docs.docker.com/ai/sandboxes-api/limits/
Markdown: https://docs.docker.com/ai/sandboxes-api/limits.md
Description: Choose a Cloud Sandboxes compute size and plan for account quotas and request rate limits.

## Claude Code
URL: https://docs.docker.com/ai/sandboxes/agents/claude-code/
Markdown: https://docs.docker.com/ai/sandboxes/agents/claude-code.md
Description: Use Claude Code in Docker Sandboxes with authentication, local models, configuration, and YOLO mode for AI-assisted development.

## Codex
URL: https://docs.docker.com/ai/sandboxes/agents/codex/
Markdown: https://docs.docker.com/ai/sandboxes/agents/codex.md
Description: Use OpenAI Codex in Docker Sandboxes with API key authentication and YOLO mode configuration.

## Copilot
URL: https://docs.docker.com/ai/sandboxes/agents/copilot/
Markdown: https://docs.docker.com/ai/sandboxes/agents/copilot.md
Description: Use GitHub Copilot in Docker Sandboxes with GitHub token authentication and trusted folder configuration.

## Cursor
URL: https://docs.docker.com/ai/sandboxes/agents/cursor/
Markdown: https://docs.docker.com/ai/sandboxes/agents/cursor.md
Description: Use Cursor in Docker Sandboxes with API key or proxy-managed OAuth authentication.

## Devin
URL: https://docs.docker.com/ai/sandboxes/agents/devin/
Markdown: https://docs.docker.com/ai/sandboxes/agents/devin.md
Description: Use Devin CLI in Docker Sandboxes with reusable, proxy-managed authentication.

## Docker Agent
URL: https://docs.docker.com/ai/sandboxes/agents/docker-agent/
Markdown: https://docs.docker.com/ai/sandboxes/agents/docker-agent.md
Description: Use Docker Agent in Docker Sandboxes with multi-provider authentication supporting OpenAI, Anthropic, and more.

## Droid
URL: https://docs.docker.com/ai/sandboxes/agents/droid/
Markdown: https://docs.docker.com/ai/sandboxes/agents/droid.md
Description: Use Droid in Docker Sandboxes with API key or OAuth authentication.

## Gemini
URL: https://docs.docker.com/ai/sandboxes/agents/gemini/
Markdown: https://docs.docker.com/ai/sandboxes/agents/gemini.md
Description: Use Google Gemini in Docker Sandboxes with proxy-managed authentication and API key configuration.

## Kiro
URL: https://docs.docker.com/ai/sandboxes/agents/kiro/
Markdown: https://docs.docker.com/ai/sandboxes/agents/kiro.md
Description: Use Kiro in Docker Sandboxes with device flow authentication for interactive AI-assisted development.

## OpenCode
URL: https://docs.docker.com/ai/sandboxes/agents/opencode/
Markdown: https://docs.docker.com/ai/sandboxes/agents/opencode.md
Description: Use OpenCode in Docker Sandboxes with multi-provider authentication and TUI interface for AI development.

## Shell
URL: https://docs.docker.com/ai/sandboxes/agents/shell/
Markdown: https://docs.docker.com/ai/sandboxes/agents/shell.md
Description: Run an agent-less sandbox with a Bash login shell for manual setup, testing custom agent implementations, or inspecting a running environment.

## Architecture
URL: https://docs.docker.com/ai/sandboxes/architecture/
Markdown: https://docs.docker.com/ai/sandboxes/architecture.md
Description: Technical architecture of Docker Sandboxes; workspace mounting, storage, networking, and sandbox lifecycle.

## Authenticate cloud agents
URL: https://docs.docker.com/ai/sandboxes/cloud/credentials/
Markdown: https://docs.docker.com/ai/sandboxes/cloud/credentials.md
Description: Configure cloud-specific API keys and OpenAI OAuth credentials for agents without storing credentials in the cloud sandbox filesystem.

## Compare local and cloud sandboxes
URL: https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud/
Markdown: https://docs.docker.com/ai/sandboxes/cloud/local-vs-cloud.md
Description: Compare local and cloud Docker Sandboxes, including workspaces, host integrations, ports, secrets, storage, and lifecycle behavior.

## Move a sandbox
URL: https://docs.docker.com/ai/sandboxes/cloud/move/
Markdown: https://docs.docker.com/ai/sandboxes/cloud/move.md
Description: Transfer a Docker Sandbox filesystem between local and cloud environments and understand which state, files, policies, and secrets remain behind.

## Manage cloud network policy
URL: https://docs.docker.com/ai/sandboxes/cloud/network-policy/
Markdown: https://docs.docker.com/ai/sandboxes/cloud/network-policy.md
Description: Control outbound connections from Docker cloud sandboxes with account-level and sandbox-level allow and deny network rules.

## Use cloud sandboxes
URL: https://docs.docker.com/ai/sandboxes/cloud/usage/
Markdown: https://docs.docker.com/ai/sandboxes/cloud/usage.md
Description: Create and manage Docker cloud sandboxes with the sbx CLI, including file transfer, commands, ports, storage, and lifecycle controls.

## Manage credentials
URL: https://docs.docker.com/ai/sandboxes/configuration/credentials/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/credentials.md
Description: How Docker Sandboxes handle API keys and authentication credentials for sandboxed agents.

## Sandbox environment files
URL: https://docs.docker.com/ai/sandboxes/configuration/environment-files/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/environment-files.md
Description: Use a declarative sbxenv.yaml file to describe and share your sandbox configuration.

## Enable NVIDIA GPU passthrough
URL: https://docs.docker.com/ai/sandboxes/configuration/gpu-passthrough/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/gpu-passthrough.md
Description: Run GPU-accelerated workloads in a sandbox by building and installing the NVIDIA driver bundle for VFIO passthrough.

## Use local and hosted models
URL: https://docs.docker.com/ai/sandboxes/configuration/models/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/models.md
Description: Choose a local model, hosted provider, or custom inference endpoint for Claude Code, Codex, or OpenCode in Docker Sandboxes.

## Configure a registry mirror
URL: https://docs.docker.com/ai/sandboxes/configuration/registry-mirror/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/registry-mirror.md
Description: Route Docker Hub template, kit, and in-sandbox Docker image pulls through an organization's registry mirror.

## Docker Sandboxes settings
URL: https://docs.docker.com/ai/sandboxes/configuration/settings/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/settings.md
Description: Configure Docker Sandboxes with sbx settings. View effective values, manage persistent overrides, and use environment variables for supported settings.

## Configure an upstream proxy
URL: https://docs.docker.com/ai/sandboxes/configuration/upstream-proxy/
Markdown: https://docs.docker.com/ai/sandboxes/configuration/upstream-proxy.md
Description: Route sandbox and daemon traffic through a corporate or upstream proxy, including PAC files, SOCKS5, and your OS system proxy.

## Base images for sandbox workloads
URL: https://docs.docker.com/ai/sandboxes/customize/author/base-images/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/base-images.md
Description: Choose a Docker-provided agent image or your own Linux base image for a sandbox workload kit.

## Build an agent workload
URL: https://docs.docker.com/ai/sandboxes/customize/author/build-an-agent/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/build-an-agent.md
Description: Build a schema v3 agent workload from your own Linux base image, prepare its sandbox environment, and configure credentials and agent instructions.

## Kit capability support
URL: https://docs.docker.com/ai/sandboxes/customize/author/capabilities/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/capabilities.md
Description: Check which v3 kit capabilities Docker Sandboxes supports locally and in the cloud, their minimum sbx versions, and restrictions that affect kit authors.

## Build and distribute kits
URL: https://docs.docker.com/ai/sandboxes/customize/author/distribute/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/distribute.md
Description: Build and publish v3 kit images, share source through Git, and sign images for distribution.

## Compose a kit set
URL: https://docs.docker.com/ai/sandboxes/customize/author/kit-sets/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/kit-sets.md
Description: Combine published workloads and mixins into a kit set, configure shared settings and arguments, and publish it for your team.

## Kit authoring patterns
URL: https://docs.docker.com/ai/sandboxes/customize/author/patterns/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/patterns.md
Description: Build reusable kits that carry the access their tools need, prepare certificates and storage during setup, and offer useful options to your team.

## Build a tool mixin
URL: https://docs.docker.com/ai/sandboxes/customize/author/tool-mixins/
Markdown: https://docs.docker.com/ai/sandboxes/customize/author/tool-mixins.md
Description: Package Claude Code as a reusable mixin with API access and credentials, test it in a shell workload, and publish it.

## Kits v2
URL: https://docs.docker.com/ai/sandboxes/customize/kits-v2/
Markdown: https://docs.docker.com/ai/sandboxes/customize/kits-v2.md
Description: Reference for v2 kits, including usage, schema fields, maintenance examples, signing, and migration to v3.

## Use kits
URL: https://docs.docker.com/ai/sandboxes/customize/use-kits/
Markdown: https://docs.docker.com/ai/sandboxes/customize/use-kits.md
Description: Run published v3 kit sets and workloads, add compatible mixins, and configure kit arguments and runtime access.

## FAQ
URL: https://docs.docker.com/ai/sandboxes/faq/
Markdown: https://docs.docker.com/ai/sandboxes/faq.md
Description: Frequently asked questions about Docker Sandboxes.

## Get started with local Docker Sandboxes
URL: https://docs.docker.com/ai/sandboxes/get-started/
Markdown: https://docs.docker.com/ai/sandboxes/get-started.md
Description: Configure agent credentials and work through your first local Docker Sandboxes session.

## Filesystem access policies
URL: https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/
Markdown: https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem.md
Description: Control which host paths Docker Sandboxes can mount as workspaces with organization filesystem policies.

## Local policy
URL: https://docs.docker.com/ai/sandboxes/governance/access-controls/local/
Markdown: https://docs.docker.com/ai/sandboxes/governance/access-controls/local.md
Description: Configure local network access rules for sandboxes on your machine.

## MCP access policies
URL: https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/
Markdown: https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp.md
Description: Use Cedar-based policies to control MCP server registration and activity routed through the Docker Sandboxes MCP gateway.

## Network access policies
URL: https://docs.docker.com/ai/sandboxes/governance/access-controls/network/
Markdown: https://docs.docker.com/ai/sandboxes/governance/access-controls/network.md
Description: Control outbound network access from Docker Sandboxes with local and organization policy rules.

## Organization policies
URL: https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/
Markdown: https://docs.docker.com/ai/sandboxes/governance/access-controls/organization.md
Description: Centrally manage sandbox network, filesystem, and MCP policies for your organization.

## Configure audit delivery
URL: https://docs.docker.com/ai/sandboxes/governance/audit/configure/
Markdown: https://docs.docker.com/ai/sandboxes/governance/audit/configure.md
Description: Configure local and cloud delivery, retention, and history for Docker AI Governance Audit Logs.

## Local audit logs
URL: https://docs.docker.com/ai/sandboxes/governance/audit/local/
Markdown: https://docs.docker.com/ai/sandboxes/governance/audit/local.md
Description: Collect Docker AI Governance audit records from local JSON Lines files written by the sandbox daemon.

## Audit record reference
URL: https://docs.docker.com/ai/sandboxes/governance/audit/record-reference/
Markdown: https://docs.docker.com/ai/sandboxes/governance/audit/record-reference.md
Description: Reference fields, categories, decisions, and payload types for Docker AI Governance audit records.

## SIEM forwarding
URL: https://docs.docker.com/ai/sandboxes/governance/audit/siem/
Markdown: https://docs.docker.com/ai/sandboxes/governance/audit/siem.md
Description: Forward Docker AI Governance audit events to Splunk, Dynatrace, Datadog, Sumo Logic, or CrowdStrike Falcon Next-Gen SIEM.

## View and export audit events
URL: https://docs.docker.com/ai/sandboxes/governance/audit/view-export/
Markdown: https://docs.docker.com/ai/sandboxes/governance/audit/view-export.md
Description: Search, filter, and export Docker AI Governance audit events from the hosted audit log UI.

## Policy concepts
URL: https://docs.docker.com/ai/sandboxes/governance/concepts/
Markdown: https://docs.docker.com/ai/sandboxes/governance/concepts.md
Description: The resource model, rule syntax, and evaluation logic behind Docker sandbox governance.

## Monitoring policies
URL: https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/
Markdown: https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring.md
Description: Inspect active policy rules and monitor sandbox network traffic with sbx policy ls and sbx policy log.

## Sign-in enforcement
URL: https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement/
Markdown: https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement.md
Description: Require Docker Sandboxes users to sign in as members of your organization, enforced through endpoint management.

## MCP policy reference
URL: https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/
Markdown: https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy.md
Description: Reference for Docker MCP policy actions, resources, attributes, context fields, and approval behavior.

## Install Docker Sandboxes
URL: https://docs.docker.com/ai/sandboxes/install/
Markdown: https://docs.docker.com/ai/sandboxes/install.md
Description: Install the sbx CLI on macOS, Windows, or Linux and sign in to Docker Sandboxes.

## Connect ChatGPT to a sandbox
URL: https://docs.docker.com/ai/sandboxes/integrations/chatgpt/
Markdown: https://docs.docker.com/ai/sandboxes/integrations/chatgpt.md
Description: Run Codex in the ChatGPT desktop app against a Docker Sandbox over SSH.

## Connect Claude Desktop to a sandbox
URL: https://docs.docker.com/ai/sandboxes/integrations/claude-desktop/
Markdown: https://docs.docker.com/ai/sandboxes/integrations/claude-desktop.md
Description: Run Claude Code from Claude Desktop against a Docker Sandbox over SSH.

## Connect Cursor to a sandbox
URL: https://docs.docker.com/ai/sandboxes/integrations/cursor/
Markdown: https://docs.docker.com/ai/sandboxes/integrations/cursor.md
Description: Use Cursor's Remote - SSH support to develop inside a Docker Sandbox.

## Connect T3 Code to a sandbox
URL: https://docs.docker.com/ai/sandboxes/integrations/t3-code/
Markdown: https://docs.docker.com/ai/sandboxes/integrations/t3-code.md
Description: Run T3 Code against a Docker Sandbox over SSH.

## Connect VS Code to a sandbox
URL: https://docs.docker.com/ai/sandboxes/integrations/vscode/
Markdown: https://docs.docker.com/ai/sandboxes/integrations/vscode.md
Description: Use VS Code Remote - SSH to develop inside a Docker Sandbox.

## MCP gateway
URL: https://docs.docker.com/ai/sandboxes/mcp-gateway/
Markdown: https://docs.docker.com/ai/sandboxes/mcp-gateway.md
Description: Register MCP servers, authorize OAuth-backed servers, and connect MCP tools to Docker Sandboxes.

## Docker Sandboxes release notes
URL: https://docs.docker.com/ai/sandboxes/release-notes/
Markdown: https://docs.docker.com/ai/sandboxes/release-notes.md
Description: New features, bug fixes, and changes in Docker Sandboxes

## Default security posture
URL: https://docs.docker.com/ai/sandboxes/security/defaults/
Markdown: https://docs.docker.com/ai/sandboxes/security/defaults.md
Description: What a sandbox permits and blocks before you change any settings.

## Isolation layers
URL: https://docs.docker.com/ai/sandboxes/security/isolation/
Markdown: https://docs.docker.com/ai/sandboxes/security/isolation.md
Description: How Docker Sandboxes isolate AI agents using hypervisor, network, Docker Engine, workspace, and credential boundaries.

## Troubleshooting
URL: https://docs.docker.com/ai/sandboxes/troubleshooting/
Markdown: https://docs.docker.com/ai/sandboxes/troubleshooting.md
Description: Resolve common issues when using Docker Sandboxes.

## Usage
URL: https://docs.docker.com/ai/sandboxes/usage/
Markdown: https://docs.docker.com/ai/sandboxes/usage.md
Description: Basic sbx commands for creating, managing, and connecting to Docker Sandboxes.

## Share agent skills
URL: https://docs.docker.com/ai/sandboxes/workflows/agent-skills/
Markdown: https://docs.docker.com/ai/sandboxes/workflows/agent-skills.md
Description: Add skills from Git repositories or import them from supported host agents into a store shared with Docker Sandboxes.

## Authenticate command-line tools
URL: https://docs.docker.com/ai/sandboxes/workflows/authentication/
Markdown: https://docs.docker.com/ai/sandboxes/workflows/authentication.md
Description: Use authenticated command-line tools and dynamic secret sources inside Docker Sandboxes.

## Run sandboxes in CI
URL: https://docs.docker.com/ai/sandboxes/workflows/automation/
Markdown: https://docs.docker.com/ai/sandboxes/workflows/automation.md
Description: Authenticate and run Docker Sandboxes in CI systems and other headless environments.

## Develop and test locally
URL: https://docs.docker.com/ai/sandboxes/workflows/development/
Markdown: https://docs.docker.com/ai/sandboxes/workflows/development.md
Description: Build, test, and connect to development services in Docker Sandboxes.

## Use Git with sandboxes
URL: https://docs.docker.com/ai/sandboxes/workflows/git/
Markdown: https://docs.docker.com/ai/sandboxes/workflows/git.md
Description: Choose a Git workspace mode and manage branches, parallel tasks, and signed commits with Docker Sandboxes.

## Install Docker Skills
URL: https://docs.docker.com/ai/skills/install/
Markdown: https://docs.docker.com/ai/skills/install.md
Description: Install Docker's official skills in compatible coding agents, Docker Sandboxes, or Docker Agent, and verify that your agent can use them.

## Builder settings
URL: https://docs.docker.com/build-cloud/builder-settings/
Markdown: https://docs.docker.com/build-cloud/builder-settings.md
Description: Set your builder settings relating to private registries, disk allocation .

## Use Docker Build Cloud in CI
URL: https://docs.docker.com/build-cloud/ci/
Markdown: https://docs.docker.com/build-cloud/ci.md
Description: Speed up your continuous integration pipelines with Docker Build Cloud in CI

## Optimize for building in the cloud
URL: https://docs.docker.com/build-cloud/optimization/
Markdown: https://docs.docker.com/build-cloud/optimization.md
Description: Building remotely is different from building locally. Here's how to optimize for remote builders.

## Docker Build Cloud release notes
URL: https://docs.docker.com/build-cloud/release-notes/
Markdown: https://docs.docker.com/build-cloud/release-notes.md
Description: Learn about the latest features of Docker Build Cloud

## Docker Build Cloud setup
URL: https://docs.docker.com/build-cloud/setup/
Markdown: https://docs.docker.com/build-cloud/setup.md
Description: How to get started with Docker Build Cloud

## Building with Docker Build Cloud
URL: https://docs.docker.com/build-cloud/usage/
Markdown: https://docs.docker.com/build-cloud/usage.md
Description: Invoke your cloud builds with the Buildx CLI client

## Building with Bake from a Compose file
URL: https://docs.docker.com/build/bake/compose-file/
Markdown: https://docs.docker.com/build/bake/compose-file.md
Description: Build your compose services with Bake

## Using Bake with additional contexts
URL: https://docs.docker.com/build/bake/contexts/
Markdown: https://docs.docker.com/build/bake/contexts.md
Description: Additional contexts are useful when you want to pin image versions, or reference the output of other targets

## Expression evaluation in Bake
URL: https://docs.docker.com/build/bake/expressions/
Markdown: https://docs.docker.com/build/bake/expressions.md
Description: Learn about advanced Bake features, like user-defined functions

## Functions
URL: https://docs.docker.com/build/bake/funcs/
Markdown: https://docs.docker.com/build/bake/funcs.md
Description: Learn about built-in and user-defined HCL functions with Bake

## Inheritance in Bake
URL: https://docs.docker.com/build/bake/inheritance/
Markdown: https://docs.docker.com/build/bake/inheritance.md
Description: Learn how to inherit attributes from other targets in Bake

## Introduction to Bake
URL: https://docs.docker.com/build/bake/introduction/
Markdown: https://docs.docker.com/build/bake/introduction.md
Description: Get started with using Bake to build your project

## Matrix targets
URL: https://docs.docker.com/build/bake/matrices/
Markdown: https://docs.docker.com/build/bake/matrices.md
Description: Learn how to define and use matrix targets in Bake to fork a single target into multiple different variants

## Overriding configurations
URL: https://docs.docker.com/build/bake/overrides/
Markdown: https://docs.docker.com/build/bake/overrides.md
Description: Learn how to override configurations in Bake files to build with different attributes.

## Bake file reference
URL: https://docs.docker.com/build/bake/reference/
Markdown: https://docs.docker.com/build/bake/reference.md

## Remote Bake file definition
URL: https://docs.docker.com/build/bake/remote-definition/
Markdown: https://docs.docker.com/build/bake/remote-definition.md
Description: Build with Bake using a remote file definition using Git or HTTP

## Bake standard library functions
URL: https://docs.docker.com/build/bake/stdlib/
Markdown: https://docs.docker.com/build/bake/stdlib.md

## Bake targets
URL: https://docs.docker.com/build/bake/targets/
Markdown: https://docs.docker.com/build/bake/targets.md
Description: Learn how to define and use targets in Bake

## Variables in Bake
URL: https://docs.docker.com/build/bake/variables/
Markdown: https://docs.docker.com/build/bake/variables.md

## Cloud driver
URL: https://docs.docker.com/build/builders/drivers/cloud/
Markdown: https://docs.docker.com/build/builders/drivers/cloud.md
Description: The cloud driver connects Buildx to managed builders in Docker Build Cloud.

## Docker container driver
URL: https://docs.docker.com/build/builders/drivers/docker-container/
Markdown: https://docs.docker.com/build/builders/drivers/docker-container.md
Description: The Docker container driver runs BuildKit in a container image.

## Docker driver
URL: https://docs.docker.com/build/builders/drivers/docker/
Markdown: https://docs.docker.com/build/builders/drivers/docker.md
Description: The Docker driver is the default driver. It uses the BuildKit bundled with the Docker Engine.

## Kubernetes driver
URL: https://docs.docker.com/build/builders/drivers/kubernetes/
Markdown: https://docs.docker.com/build/builders/drivers/kubernetes.md
Description: The Kubernetes driver lets you run BuildKit in a Kubernetes cluster. You can connect to, and run your builds in, the cluster using Buildx.

## Remote driver
URL: https://docs.docker.com/build/builders/drivers/remote/
Markdown: https://docs.docker.com/build/builders/drivers/remote.md
Description: The remote driver lets you connect to a remote BuildKit instance that you set up and configure manually.

## Manage builders
URL: https://docs.docker.com/build/builders/manage/
Markdown: https://docs.docker.com/build/builders/manage.md

## Base images
URL: https://docs.docker.com/build/building/base-images/
Markdown: https://docs.docker.com/build/building/base-images.md
Description: Learn about base images and how they're created

## Building best practices
URL: https://docs.docker.com/build/building/best-practices/
Markdown: https://docs.docker.com/build/building/best-practices.md
Description: Hints, tips and guidelines for writing clean, reliable Dockerfiles

## Container Device Interface (CDI)
URL: https://docs.docker.com/build/building/cdi/
Markdown: https://docs.docker.com/build/building/cdi.md
Description: Using CDI to access GPUs and other devices in your builds

## Export binaries
URL: https://docs.docker.com/build/building/export/
Markdown: https://docs.docker.com/build/building/export.md
Description: Using Docker builds to create and export executable binaries

## Multi-platform builds
URL: https://docs.docker.com/build/building/multi-platform/
Markdown: https://docs.docker.com/build/building/multi-platform.md
Description: Introduction to what multi-platform builds are and how to execute them using Docker Buildx.

## Multi-stage builds
URL: https://docs.docker.com/build/building/multi-stage/
Markdown: https://docs.docker.com/build/building/multi-stage.md
Description: Learn about multi-stage builds and how you can use them to improve your builds and get smaller images

## Build secrets
URL: https://docs.docker.com/build/building/secrets/
Markdown: https://docs.docker.com/build/building/secrets.md
Description: Manage credentials and other secrets securely

## Build variables
URL: https://docs.docker.com/build/building/variables/
Markdown: https://docs.docker.com/build/building/variables.md
Description: Using build arguments and environment variables to configure builds

## Configure BuildKit
URL: https://docs.docker.com/build/buildkit/configure/
Markdown: https://docs.docker.com/build/buildkit/configure.md
Description: Learn how to configure BuildKit for your builder.

## Dockerfile release notes
URL: https://docs.docker.com/build/buildkit/dockerfile-release-notes/
Markdown: https://docs.docker.com/build/buildkit/dockerfile-release-notes.md

## Custom Dockerfile syntax
URL: https://docs.docker.com/build/buildkit/frontend/
Markdown: https://docs.docker.com/build/buildkit/frontend.md
Description: Dive deep into the Dockerfile frontend, and learn about custom frontends

## buildkitd.toml
URL: https://docs.docker.com/build/buildkit/toml-configuration/
Markdown: https://docs.docker.com/build/buildkit/toml-configuration.md

## Azure Blob Storage cache
URL: https://docs.docker.com/build/cache/backends/azblob/
Markdown: https://docs.docker.com/build/cache/backends/azblob.md
Description: Manage build cache with Azure blob storage

## GitHub Actions cache
URL: https://docs.docker.com/build/cache/backends/gha/
Markdown: https://docs.docker.com/build/cache/backends/gha.md
Description: Use the GitHub Actions cache to manage your build cache in CI

## Inline cache
URL: https://docs.docker.com/build/cache/backends/inline/
Markdown: https://docs.docker.com/build/cache/backends/inline.md
Description: Embed the build cache into the image

## Local cache
URL: https://docs.docker.com/build/cache/backends/local/
Markdown: https://docs.docker.com/build/cache/backends/local.md
Description: Manage build cache with a local directory

## Registry cache
URL: https://docs.docker.com/build/cache/backends/registry/
Markdown: https://docs.docker.com/build/cache/backends/registry.md
Description: Manage build cache with an OCI registry

## Amazon S3 cache
URL: https://docs.docker.com/build/cache/backends/s3/
Markdown: https://docs.docker.com/build/cache/backends/s3.md
Description: Manage build cache with Amazon S3 buckets

## Build garbage collection
URL: https://docs.docker.com/build/cache/garbage-collection/
Markdown: https://docs.docker.com/build/cache/garbage-collection.md
Description: Learn about garbage collection in the BuildKit daemon

## Build cache invalidation
URL: https://docs.docker.com/build/cache/invalidation/
Markdown: https://docs.docker.com/build/cache/invalidation.md
Description: Dig into the details about how cache invalidation works for Docker's build cache

## Optimize cache usage in builds
URL: https://docs.docker.com/build/cache/optimize/
Markdown: https://docs.docker.com/build/cache/optimize.md
Description: An overview on how to optimize cache utilization in Docker builds.

## Checking your build configuration
URL: https://docs.docker.com/build/checks/
Markdown: https://docs.docker.com/build/checks.md
Description: Learn how to use build checks to validate your build configuration.

## Add image annotations with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/annotations/
Markdown: https://docs.docker.com/build/ci/github-actions/annotations.md
Description: Add OCI annotations to image components using GitHub Actions

## Add SBOM and provenance attestations with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/attestations/
Markdown: https://docs.docker.com/build/ci/github-actions/attestations.md
Description: Add SBOM and provenance attestations to your images with GitHub Actions

## GitHub Actions build summary
URL: https://docs.docker.com/build/ci/github-actions/build-summary/
Markdown: https://docs.docker.com/build/ci/github-actions/build-summary.md
Description: Get an overview of your Docker Builds with GitHub Actions

## Cache management with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/cache/
Markdown: https://docs.docker.com/build/ci/github-actions/cache.md
Description: Configure build cache backends for GitHub Actions and handle cache write restrictions.

## Validating build configuration with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/checks/
Markdown: https://docs.docker.com/build/ci/github-actions/checks.md
Description: Discover how to validate your build configuration and identify best practice violations using build checks in GitHub Actions.

## Configuring your GitHub Actions builder
URL: https://docs.docker.com/build/ci/github-actions/configure-builder/
Markdown: https://docs.docker.com/build/ci/github-actions/configure-builder.md
Description: Configuring BuildKit instances for building in CI with GitHub Actions

## Copy image between registries with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/copy-image-registries/
Markdown: https://docs.docker.com/build/ci/github-actions/copy-image-registries.md
Description: Build multi-platform images and copy them between registries with GitHub Actions

## Export to Docker with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/export-docker/
Markdown: https://docs.docker.com/build/ci/github-actions/export-docker.md
Description: Load the build results to the image store with GitHub Actions

## Docker GitHub Builder architecture
URL: https://docs.docker.com/build/ci/github-actions/github-builder/architecture/
Markdown: https://docs.docker.com/build/ci/github-actions/github-builder/architecture.md
Description: Learn about the architecture of Docker GitHub Builder, a set of reusable workflows for building images and artifacts with BuildKit in GitHub Actions.

## Bake with Docker GitHub Builder
URL: https://docs.docker.com/build/ci/github-actions/github-builder/bake/
Markdown: https://docs.docker.com/build/ci/github-actions/github-builder/bake.md
Description: Use the Docker GitHub Builder bake.yml reusable workflow to build images and local artifacts from a Bake definition.

## Build with Docker GitHub Builder
URL: https://docs.docker.com/build/ci/github-actions/github-builder/build/
Markdown: https://docs.docker.com/build/ci/github-actions/github-builder/build.md
Description: Use the Docker GitHub Builder build.yml reusable workflow to build images and local artifacts from a Dockerfile.

## Local registry with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/local-registry/
Markdown: https://docs.docker.com/build/ci/github-actions/local-registry.md
Description: Create and use a local OCI registry with GitHub Actions

## Manage tags and labels with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/manage-tags-labels/
Markdown: https://docs.docker.com/build/ci/github-actions/manage-tags-labels.md
Description: Assign tags and labels to images automatically with GitHub Actions

## Multi-platform image with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/multi-platform/
Markdown: https://docs.docker.com/build/ci/github-actions/multi-platform.md
Description: Build for multiple architectures with GitHub Actions using QEMU emulation or multiple native builders

## Named contexts with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/named-contexts/
Markdown: https://docs.docker.com/build/ci/github-actions/named-contexts.md
Description: Use additional contexts in multi-stage builds with GitHub Actions

## Push to multiple registries with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/push-multi-registries/
Markdown: https://docs.docker.com/build/ci/github-actions/push-multi-registries.md
Description: Push to multiple registries with GitHub Actions

## Reproducible builds with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/reproducible-builds/
Markdown: https://docs.docker.com/build/ci/github-actions/reproducible-builds.md
Description: How to create reproducible builds in GitHub Actions using the SOURCE_EPOCH environment variable

## Using secrets with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/secrets/
Markdown: https://docs.docker.com/build/ci/github-actions/secrets.md
Description: Example using secret mounts with GitHub Actions

## Share built image between jobs with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/share-image-jobs/
Markdown: https://docs.docker.com/build/ci/github-actions/share-image-jobs.md
Description: Share an image between runners without pushing to a registry

## Test before push with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/test-before-push/
Markdown: https://docs.docker.com/build/ci/github-actions/test-before-push.md
Description: Here's how you can validate an image, before pushing it to a registry

## Update Docker Hub description with GitHub Actions
URL: https://docs.docker.com/build/ci/github-actions/update-dockerhub-desc/
Markdown: https://docs.docker.com/build/ci/github-actions/update-dockerhub-desc.md
Description: How to update the repository README in Docker Hub using with GitHub Actions

## Build context
URL: https://docs.docker.com/build/concepts/context/
Markdown: https://docs.docker.com/build/concepts/context.md
Description: Learn how to use the build context to access files from your Dockerfile

## Dockerfile overview
URL: https://docs.docker.com/build/concepts/dockerfile/
Markdown: https://docs.docker.com/build/concepts/dockerfile.md
Description: Learn about Dockerfiles and how to use them with Docker Images to build and package your software

## Docker Build Overview
URL: https://docs.docker.com/build/concepts/overview/
Markdown: https://docs.docker.com/build/concepts/overview.md
Description: Learn about Docker Build and its components.

## OpenTelemetry support
URL: https://docs.docker.com/build/debug/opentelemetry/
Markdown: https://docs.docker.com/build/debug/opentelemetry.md
Description: Analyze telemetry data for builds

## Image and registry exporters
URL: https://docs.docker.com/build/exporters/image-registry/
Markdown: https://docs.docker.com/build/exporters/image-registry.md
Description: The image and registry exporters create an image that can be loaded to your local image store or pushed to a registry

## Local and tar exporters
URL: https://docs.docker.com/build/exporters/local-tar/
Markdown: https://docs.docker.com/build/exporters/local-tar.md
Description: The local and tar exporters save the build result to the local filesystem

## OCI and Docker exporters
URL: https://docs.docker.com/build/exporters/oci-docker/
Markdown: https://docs.docker.com/build/exporters/oci-docker.md
Description: The OCI and Docker exporters create an image layout tarball on the local filesystem

## Annotations
URL: https://docs.docker.com/build/metadata/annotations/
Markdown: https://docs.docker.com/build/metadata/annotations.md
Description: Annotations specify additional metadata about OCI images

## Image attestation storage
URL: https://docs.docker.com/build/metadata/attestations/attestation-storage/
Markdown: https://docs.docker.com/build/metadata/attestations/attestation-storage.md

## SBOM attestations
URL: https://docs.docker.com/build/metadata/attestations/sbom/
Markdown: https://docs.docker.com/build/metadata/attestations/sbom.md
Description: SBOM attestations describe what software artifacts an image contains and the artifacts used to create the image.

## SLSA definitions
URL: https://docs.docker.com/build/metadata/attestations/slsa-definitions/
Markdown: https://docs.docker.com/build/metadata/attestations/slsa-definitions.md

## Provenance attestations
URL: https://docs.docker.com/build/metadata/attestations/slsa-provenance/
Markdown: https://docs.docker.com/build/metadata/attestations/slsa-provenance.md
Description: Provenance build attestations describe how and where your image was built.

## Built-in functions
URL: https://docs.docker.com/build/policies/built-ins/
Markdown: https://docs.docker.com/build/policies/built-ins.md
Description: Buildx includes built-in helper functions to make writing policies easier

## Debugging build policies
URL: https://docs.docker.com/build/policies/debugging/
Markdown: https://docs.docker.com/build/policies/debugging.md
Description: Debug policies during development with inspection and testing tools

## Policy templates and examples
URL: https://docs.docker.com/build/policies/examples/
Markdown: https://docs.docker.com/build/policies/examples.md
Description: Browse policy examples from quick-start configs to production-grade security templates

## Input reference
URL: https://docs.docker.com/build/policies/inputs/
Markdown: https://docs.docker.com/build/policies/inputs.md
Description: Reference documentation for policy input fields

## Introduction to build policies
URL: https://docs.docker.com/build/policies/intro/
Markdown: https://docs.docker.com/build/policies/intro.md
Description: Get started with writing and evaluating build policies

## Test build policies
URL: https://docs.docker.com/build/policies/testing/
Markdown: https://docs.docker.com/build/policies/testing.md
Description: Write and run unit tests for build policies, similar to the opa test command

## Using build policies
URL: https://docs.docker.com/build/policies/usage/
Markdown: https://docs.docker.com/build/policies/usage.md
Description: Apply policies to builds and develop policies iteratively

## Validating Git repositories
URL: https://docs.docker.com/build/policies/validate-git/
Markdown: https://docs.docker.com/build/policies/validate-git.md
Description: Write policies to validate Git repositories used in your builds

## Validating image inputs
URL: https://docs.docker.com/build/policies/validate-images/
Markdown: https://docs.docker.com/build/policies/validate-images.md
Description: Write policies to validate container images used in your builds

## Build release notes
URL: https://docs.docker.com/build/release-notes/
Markdown: https://docs.docker.com/build/release-notes.md

## Customize Compose Bridge
URL: https://docs.docker.com/compose/bridge/customize/
Markdown: https://docs.docker.com/compose/bridge/customize.md
Description: Learn how to customize Compose Bridge transformations using Go templates and Compose extensions

## Use the default Compose Bridge transformation
URL: https://docs.docker.com/compose/bridge/usage/
Markdown: https://docs.docker.com/compose/bridge/usage.md
Description: Learn how to use the default Compose Bridge transformation to convert Compose files into Kubernetes manifests

## Use Docker Model Runner with Compose Bridge
URL: https://docs.docker.com/compose/bridge/use-model-runner/
Markdown: https://docs.docker.com/compose/bridge/use-model-runner.md
Description: How to use Docker Model Runner with Compose Bridge for consistent deployments

## Using the Compose SDK
URL: https://docs.docker.com/compose/compose-sdk/
Markdown: https://docs.docker.com/compose/compose-sdk.md
Description: Integrate Docker Compose directly into your applications with the Compose SDK.

## Docker Compose Quickstart
URL: https://docs.docker.com/compose/gettingstarted/
Markdown: https://docs.docker.com/compose/gettingstarted.md
Description: Follow this hands-on tutorial to learn how to use Docker Compose from defining application dependencies to experimenting with commands.

## Build dependent images
URL: https://docs.docker.com/compose/how-tos/dependent-images/
Markdown: https://docs.docker.com/compose/how-tos/dependent-images.md
Description: Build images for services with shared definition

## Best practices for working with environment variables in Docker Compose
URL: https://docs.docker.com/compose/how-tos/environment-variables/best-practices/
Markdown: https://docs.docker.com/compose/how-tos/environment-variables/best-practices.md
Description: Explainer on the best ways to set, use, and manage environment variables in Compose

## Environment variables precedence in Docker Compose
URL: https://docs.docker.com/compose/how-tos/environment-variables/envvars-precedence/
Markdown: https://docs.docker.com/compose/how-tos/environment-variables/envvars-precedence.md
Description: Scenario overview illustrating how environment variables are resolved in Compose

## Configure pre-defined environment variables in Docker Compose
URL: https://docs.docker.com/compose/how-tos/environment-variables/envvars/
Markdown: https://docs.docker.com/compose/how-tos/environment-variables/envvars.md
Description: Compose pre-defined environment variables

## Set environment variables within your container's environment
URL: https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/
Markdown: https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables.md
Description: How to set, use, and manage environment variables with Compose

## Set, use, and manage variables in a Compose file with interpolation
URL: https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/
Markdown: https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation.md
Description: How to set, use, and manage variables in your Compose file with interpolation

## Use Compose Watch
URL: https://docs.docker.com/compose/how-tos/file-watch/
Markdown: https://docs.docker.com/compose/how-tos/file-watch.md
Description: Use File watch to automatically update running services as you work

## Run Docker Compose services with GPU access
URL: https://docs.docker.com/compose/how-tos/gpu-support/
Markdown: https://docs.docker.com/compose/how-tos/gpu-support.md
Description: Learn how to configure Docker Compose to use NVIDIA GPUs with CUDA-based containers

## Use init containers in Compose
URL: https://docs.docker.com/compose/how-tos/init-containers/
Markdown: https://docs.docker.com/compose/how-tos/init-containers.md
Description: Use pre_start init containers to run setup tasks before a service starts in Docker Compose.

## Using lifecycle hooks with Compose
URL: https://docs.docker.com/compose/how-tos/lifecycle/
Markdown: https://docs.docker.com/compose/how-tos/lifecycle.md
Description: Learn how to use Docker Compose lifecycle hooks like pre_start, post_start, and pre_stop to customize container behavior.

## Extend your Compose file
URL: https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/
Markdown: https://docs.docker.com/compose/how-tos/multiple-compose-files/extends.md
Description: Learn how to reuse service configurations across files and projects using Docker Compose’s extends attribute.

## Include
URL: https://docs.docker.com/compose/how-tos/multiple-compose-files/include/
Markdown: https://docs.docker.com/compose/how-tos/multiple-compose-files/include.md
Description: How to use Docker Compose's include top-level element

## Merge Compose files
URL: https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
Markdown: https://docs.docker.com/compose/how-tos/multiple-compose-files/merge.md
Description: How merging Compose files works

## Networking in Compose
URL: https://docs.docker.com/compose/how-tos/networking/
Markdown: https://docs.docker.com/compose/how-tos/networking.md
Description: How Docker Compose sets up networking between containers

## Package and deploy Docker Compose applications as OCI artifacts
URL: https://docs.docker.com/compose/how-tos/oci-artifact/
Markdown: https://docs.docker.com/compose/how-tos/oci-artifact.md
Description: Learn how to package, publish, and securely run Docker Compose applications from OCI-compliant registries.

## Use Compose in production
URL: https://docs.docker.com/compose/how-tos/production/
Markdown: https://docs.docker.com/compose/how-tos/production.md
Description: Learn how to configure, deploy, and update Docker Compose applications for production environments.

## Using profiles with Compose
URL: https://docs.docker.com/compose/how-tos/profiles/
Markdown: https://docs.docker.com/compose/how-tos/profiles.md
Description: How to use profiles with Docker Compose

## Specify a project name
URL: https://docs.docker.com/compose/how-tos/project-name/
Markdown: https://docs.docker.com/compose/how-tos/project-name.md
Description: Learn how to set a custom project name in Compose and understand the precedence of each method.

## Use provider services
URL: https://docs.docker.com/compose/how-tos/provider-services/
Markdown: https://docs.docker.com/compose/how-tos/provider-services.md
Description: Learn how to use provider services in Docker Compose to integrate external capabilities into your applications

## Control startup and shutdown order in Compose
URL: https://docs.docker.com/compose/how-tos/startup-order/
Markdown: https://docs.docker.com/compose/how-tos/startup-order.md
Description: Learn how to manage service startup and shutdown order in Docker Compose using depends_on and healthchecks.

## Manage secrets securely in Docker Compose
URL: https://docs.docker.com/compose/how-tos/use-secrets/
Markdown: https://docs.docker.com/compose/how-tos/use-secrets.md
Description: Learn how to securely manage runtime and build-time secrets in Docker Compose.

## Install the Docker Compose plugin
URL: https://docs.docker.com/compose/install/linux/
Markdown: https://docs.docker.com/compose/install/linux.md
Description: Step-by-step instructions for installing the Docker Compose plugin on Linux using a package repository or manual method.

## Install the Docker Compose standalone (Legacy)
URL: https://docs.docker.com/compose/install/standalone/
Markdown: https://docs.docker.com/compose/install/standalone.md
Description: Instructions for installing the legacy Docker Compose standalone tool on Linux and Windows Server

## Uninstall Docker Compose
URL: https://docs.docker.com/compose/install/uninstall/
Markdown: https://docs.docker.com/compose/install/uninstall.md
Description: How to uninstall Docker Compose

## How Compose works
URL: https://docs.docker.com/compose/intro/compose-application-model/
Markdown: https://docs.docker.com/compose/intro/compose-application-model.md
Description: Learn how Docker Compose works, from the application model to Compose files and CLI, whilst following a detailed example.

## Why use Compose?
URL: https://docs.docker.com/compose/intro/features-uses/
Markdown: https://docs.docker.com/compose/intro/features-uses.md
Description: Discover the benefits and typical use cases of Docker Compose for containerized application development and deployment

## History and development of Docker Compose
URL: https://docs.docker.com/compose/intro/history/
Markdown: https://docs.docker.com/compose/intro/history.md
Description: Explore the evolution of Docker Compose from v1 to v5, including CLI changes, YAML versioning, and the Compose Specification.

## Release notes
URL: https://docs.docker.com/compose/release-notes/
Markdown: https://docs.docker.com/compose/release-notes.md

## Frequently asked questions about Docker Compose
URL: https://docs.docker.com/compose/support-and-feedback/faq/
Markdown: https://docs.docker.com/compose/support-and-feedback/faq.md
Description: Answers to common questions about Docker Compose, including v1 vs v2, commands, shutdown behavior, and development setup.

## Give feedback
URL: https://docs.docker.com/compose/support-and-feedback/feedback/
Markdown: https://docs.docker.com/compose/support-and-feedback/feedback.md
Description: Find a way to provide feedback on Docker Compose that's right for you

## Trust model for Compose files
URL: https://docs.docker.com/compose/trust-model/
Markdown: https://docs.docker.com/compose/trust-model.md
Description: Learn how Docker Compose treats Compose files as trusted input and what this means when using files you did not author.

## Allowlist for Docker Desktop
URL: https://docs.docker.com/desktop/enterprise/allow-list/
Markdown: https://docs.docker.com/desktop/enterprise/allow-list.md
Description: A list of domain URLs required for Docker Desktop to function correctly within an organization.

## Configure sign-in enforcement
URL: https://docs.docker.com/desktop/enterprise/enforce-sign-in/methods/
Markdown: https://docs.docker.com/desktop/enterprise/enforce-sign-in/methods.md
Description: Configure sign-in enforcement for Docker Desktop using registry keys, configuration profiles, plist files, or registry.json files

## Docker Desktop in Microsoft Dev Box
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/dev-box/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/dev-box.md
Description: Learn about the benefits of and  how to setup Docker Desktop in Microsoft Dev Box

## Enterprise deployment FAQs
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/faq/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/faq.md
Description: Frequently asked questions for deploying Docker Desktop at scale

## Install Docker Desktop from the Microsoft Store on Windows
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/ms-store/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/ms-store.md
Description: Install Docker Desktop for Windows through the Microsoft Store. Understand its update behavior and limitations.

## MSI installer
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/msi-install-and-configure/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/msi-install-and-configure.md
Description: Understand how to use the MSI installer. Also explore additional configuration options.

## PKG installer
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/pkg-install-and-configure/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/pkg-install-and-configure.md
Description: Understand how to use the PKG installer to deploy Docker Desktop for Mac at scale.

## Deploy with Intune
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/use-intune/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/use-intune.md
Description: Use Intune, Microsoft's cloud-based device management tool, to deploy Docker Desktop

## Deploy with Jamf Pro
URL: https://docs.docker.com/desktop/enterprise/enterprise-deployment/use-jamf-pro/
Markdown: https://docs.docker.com/desktop/enterprise/enterprise-deployment/use-jamf-pro.md
Description: Use Jamf Pro to deploy Docker Desktop for Mac

## Air-gapped containers
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/air-gapped-containers/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/air-gapped-containers.md
Description: Restrict outbound container traffic using proxy rules, PAC files, and network isolation with Docker Desktop air-gapped containers

## Configure Docker socket exceptions and advanced settings
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/config/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/config.md
Description: Configure Docker socket exceptions and advanced settings for Enhanced Container Isolation

## Enable Enhanced Container Isolation
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/enable-eci/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/enable-eci.md
Description: Enable Enhanced Container Isolation to secure containers in Docker Desktop

## Enhanced Container Isolation FAQs
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/faq/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/faq.md
Description: Frequently asked questions about Enhanced Container Isolation

## Enhanced Container Isolation limitations
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/limitations/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/limitations.md
Description: Known limitations and platform-specific considerations for Enhanced Container Isolation

## Image Access Management
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/image-access-management/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/image-access-management.md
Description: Control which Docker Hub images developers can access with Image Access Management for enhanced supply chain security

## Namespace access control
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/namespace-access/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/namespace-access.md
Description: Control whether organization members can push content to their personal namespaces on Docker Hub

## Registry Access Management
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/registry-access-management/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/registry-access-management.md
Description: Control which container registries developers can access through Docker Desktop with Registry Access Management.

## Desktop settings reporting
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/compliance-reporting/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/compliance-reporting.md
Description: Track and monitor user compliance with Docker Desktop settings policies using the reporting dashboard

## Configure Settings Management in Docker Home
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/configure-admin-console/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/configure-admin-console.md
Description: Configure and enforce Docker Desktop settings across your organization in Docker Home

## Configure Settings Management with a JSON file
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/configure-json-file/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/configure-json-file.md
Description: Configure and enforce Docker Desktop settings using an admin-settings.json file

## Settings reference
URL: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/settings-reference/
Markdown: https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/settings-reference.md
Description: Complete reference for all Docker Desktop settings and configuration options

## containerd image store
URL: https://docs.docker.com/desktop/features/containerd/
Markdown: https://docs.docker.com/desktop/features/containerd.md
Description: Learn about the containerd image store in Docker Desktop and how it extends image management capabilities.

## Use the Docker Desktop CLI
URL: https://docs.docker.com/desktop/features/desktop-cli/
Markdown: https://docs.docker.com/desktop/features/desktop-cli.md
Description: How to use the Docker Desktop CLI

## GPU support in Docker Desktop for Windows
URL: https://docs.docker.com/desktop/features/gpu/
Markdown: https://docs.docker.com/desktop/features/gpu.md
Description: How to use GPU in Docker Desktop

## Explore networking how-tos on Docker Desktop
URL: https://docs.docker.com/desktop/features/networking/networking-how-tos/
Markdown: https://docs.docker.com/desktop/features/networking/networking-how-tos.md
Description: Learn how to connect containers to the host, across containers, or through proxies and VPNs in Docker Desktop.

## Synchronized file shares
URL: https://docs.docker.com/desktop/features/synchronized-file-sharing/
Markdown: https://docs.docker.com/desktop/features/synchronized-file-sharing.md
Description: Get started with Synchronized file shares on Docker Desktop.

## Using USB/IP with Docker Desktop
URL: https://docs.docker.com/desktop/features/usbip/
Markdown: https://docs.docker.com/desktop/features/usbip.md
Description: How to use USB/IP in Docker Desktop

## Virtual Machine Manager
URL: https://docs.docker.com/desktop/features/vmm/
Markdown: https://docs.docker.com/desktop/features/vmm.md
Description: Learn about Docker Desktop's Virtual Machine Manager options, including Docker VMM for Mac and Windows

## Wasm workloads
URL: https://docs.docker.com/desktop/features/wasm/
Markdown: https://docs.docker.com/desktop/features/wasm.md
Description: How to run Wasm workloads with Docker Desktop

## WSL 2 best practices for Docker Desktop on Windows
URL: https://docs.docker.com/desktop/features/wsl/best-practices/
Markdown: https://docs.docker.com/desktop/features/wsl/best-practices.md
Description: Best practices for using Docker Desktop with WSL 2

## Custom kernels on WSL
URL: https://docs.docker.com/desktop/features/wsl/custom-kernels/
Markdown: https://docs.docker.com/desktop/features/wsl/custom-kernels.md
Description: Using custom kernels with Docker Desktop on WSL 2

## Develop with Docker Desktop using WSL 2 on Windows
URL: https://docs.docker.com/desktop/features/wsl/use-wsl/
Markdown: https://docs.docker.com/desktop/features/wsl/use-wsl.md
Description: How to develop with Docker and WSL 2 and understand GPU support for WSL

## Docker Desktop release notes
URL: https://docs.docker.com/desktop/release-notes/
Markdown: https://docs.docker.com/desktop/release-notes.md
Description: Find the Docker Desktop release notes for Mac, Linux, and Windows.

## How to back up and restore your Docker Desktop data
URL: https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/
Markdown: https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore.md

## Change your Docker Desktop settings
URL: https://docs.docker.com/desktop/settings-and-maintenance/settings/
Markdown: https://docs.docker.com/desktop/settings-and-maintenance/settings.md
Description: Learn about and change Docker Desktop's settings

## Install Docker Desktop on Arch-based distributions
URL: https://docs.docker.com/desktop/setup/install/linux/archlinux/
Markdown: https://docs.docker.com/desktop/setup/install/linux/archlinux.md
Description: Instructions for installing Docker Desktop Arch package. Mostly meant for hackers who want to try out Docker Desktop on a variety of Arch-based distributions.

## Install Docker Desktop on Debian
URL: https://docs.docker.com/desktop/setup/install/linux/debian/
Markdown: https://docs.docker.com/desktop/setup/install/linux/debian.md
Description: Instructions for installing Docker Desktop on Debian

## Install Docker Desktop on Fedora
URL: https://docs.docker.com/desktop/setup/install/linux/fedora/
Markdown: https://docs.docker.com/desktop/setup/install/linux/fedora.md
Description: Instructions for installing Docker Desktop on Fedora

## Install Docker Desktop on RHEL
URL: https://docs.docker.com/desktop/setup/install/linux/rhel/
Markdown: https://docs.docker.com/desktop/setup/install/linux/rhel.md
Description: Instructions for installing Docker Desktop on RHEL

## Install Docker Desktop on Ubuntu
URL: https://docs.docker.com/desktop/setup/install/linux/ubuntu/
Markdown: https://docs.docker.com/desktop/setup/install/linux/ubuntu.md
Description: Learn how to install, launch, and upgrade Docker Desktop on Ubuntu. This quick guide will cover prerequisites, installation methods, and more.

## Install Docker Desktop on Mac
URL: https://docs.docker.com/desktop/setup/install/mac-install/
Markdown: https://docs.docker.com/desktop/setup/install/mac-install.md
Description: Install Docker Desktop for Mac to get started. This guide covers system requirements, where to download, and instructions on how to install and update.

## Understand permission requirements for Docker Desktop on Mac
URL: https://docs.docker.com/desktop/setup/install/mac-permission-requirements/
Markdown: https://docs.docker.com/desktop/setup/install/mac-permission-requirements.md
Description: Understand permission requirements for Docker Desktop for Mac and the differences between versions

## Install Docker Desktop on Windows
URL: https://docs.docker.com/desktop/setup/install/windows-install/
Markdown: https://docs.docker.com/desktop/setup/install/windows-install.md
Description: Get started with Docker for Windows. This guide covers system requirements, where to download, and instructions on how to install and update.

## Understand permission requirements for Windows
URL: https://docs.docker.com/desktop/setup/install/windows-permission-requirements/
Markdown: https://docs.docker.com/desktop/setup/install/windows-permission-requirements.md
Description: Understand permission requirements for Docker Desktop for Windows

## Run Docker Desktop for Windows in a VM or VDI environment
URL: https://docs.docker.com/desktop/setup/vm-vdi/
Markdown: https://docs.docker.com/desktop/setup/vm-vdi.md
Description: Instructions on how to enable nested virtualization

## General FAQs for Desktop
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general.md
Description: Frequently asked Docker Desktop questions for all platforms

## FAQs for Docker Desktop for Linux
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/linuxfaqs/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/linuxfaqs.md
Description: Frequently asked questions for Docker Desktop for Linux

## FAQs for Docker Desktop for Mac
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/macfaqs/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/macfaqs.md
Description: Frequently asked questions for Docker Desktop for Mac

## FAQs on Docker Desktop releases
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/releases/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/releases.md
Description: Frequently asked Docker Desktop questions for all platforms

## FAQs for Docker Desktop for Windows
URL: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/windowsfaqs/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/faqs/windowsfaqs.md
Description: Frequently asked questions for Docker Desktop for Windows

## Give feedback
URL: https://docs.docker.com/desktop/troubleshoot-and-support/feedback/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/feedback.md
Description: Find a way to provide feedback that's right for you

## Troubleshoot topics for Docker Desktop
URL: https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics/
Markdown: https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/topics.md
Description: Explore common troubleshooting topics for Docker Desktop

## Uninstall Docker Desktop
URL: https://docs.docker.com/desktop/uninstall/
Markdown: https://docs.docker.com/desktop/uninstall.md
Description: How to uninstall Docker Desktop

## Explore the Builds view in Docker Desktop
URL: https://docs.docker.com/desktop/use-desktop/builds/
Markdown: https://docs.docker.com/desktop/use-desktop/builds.md
Description: Understand how to use the Builds view in Docker Desktop

## Explore the Containers view in Docker Desktop
URL: https://docs.docker.com/desktop/use-desktop/container/
Markdown: https://docs.docker.com/desktop/use-desktop/container.md
Description: Understand what you can do with the Containers view on Docker Dashboard

## Explore the Images view in Docker Desktop
URL: https://docs.docker.com/desktop/use-desktop/images/
Markdown: https://docs.docker.com/desktop/use-desktop/images.md
Description: Understand what you can do with the Images view on Docker Dashboard

## Explore the Kubernetes view
URL: https://docs.docker.com/desktop/use-desktop/kubernetes/
Markdown: https://docs.docker.com/desktop/use-desktop/kubernetes.md
Description: See how you can deploy to Kubernetes on Docker Desktop

## Explore the Logs view in Docker Desktop
URL: https://docs.docker.com/desktop/use-desktop/logs/
Markdown: https://docs.docker.com/desktop/use-desktop/logs.md
Description: Understand what you can do with the Logs view on Docker Dashboard

## Docker Desktop's Resource Saver mode
URL: https://docs.docker.com/desktop/use-desktop/resource-saver/
Markdown: https://docs.docker.com/desktop/use-desktop/resource-saver.md
Description: Understand what Docker Desktop Resource Saver mode is and how to configure it

## Explore the Volumes view in Docker Desktop
URL: https://docs.docker.com/desktop/use-desktop/volumes/
Markdown: https://docs.docker.com/desktop/use-desktop/volumes.md
Description: Understand what you can do with the Volumes view on Docker Dashboard

## Available types of Docker Hardened Images
URL: https://docs.docker.com/dhi/explore/available/
Markdown: https://docs.docker.com/dhi/explore/available.md
Description: Learn about the different image types, distributions, and variants offered in the Docker Hardened Images catalog.

## How Docker Hardened Images are built
URL: https://docs.docker.com/dhi/explore/build-process/
Markdown: https://docs.docker.com/dhi/explore/build-process.md
Description: Learn how Docker builds, tests, and maintains Docker Hardened Images through an automated, security-focused pipeline.

## EU data residency for Docker Hardened Images
URL: https://docs.docker.com/dhi/explore/eu-region/
Markdown: https://docs.docker.com/dhi/explore/eu-region.md
Description: Learn how Docker stores your mirrored and customized Docker Hardened Images in the EU when your DHI subscription is in the EU region, and what works differently in that region.

## Malware scanning
URL: https://docs.docker.com/dhi/explore/malware-scanning/
Markdown: https://docs.docker.com/dhi/explore/malware-scanning.md
Description: Learn how Docker scans Docker Hardened Images for viruses and malware using ClamAV, and how to view and verify the scan attestation.

## Understanding roles and responsibilities for Docker Hardened Images
URL: https://docs.docker.com/dhi/explore/responsibility/
Markdown: https://docs.docker.com/dhi/explore/responsibility.md
Description: Understand the division of responsibilities between Docker, upstream projects, and you when using Docker Hardened Images.

## Scanner integrations
URL: https://docs.docker.com/dhi/explore/scanner-integrations/
Markdown: https://docs.docker.com/dhi/explore/scanner-integrations.md
Description: Learn which vulnerability scanners work with Docker Hardened Images and how to choose the right scanner for accurate vulnerability assessment.

## Attestations
URL: https://docs.docker.com/dhi/explore/security-concepts/attestations/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/attestations.md
Description: Review the full set of signed attestations included with each Docker Hardened Image, such as SBOMs, VEX, build provenance, and scan results.

## CIS Benchmark
URL: https://docs.docker.com/dhi/explore/security-concepts/cis/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/cis.md
Description: Learn how Docker Hardened Images comply with the CIS Docker Benchmark to help organizations harden container images for secure deployments.

## Common Vulnerabilities and Exposures (CVEs)
URL: https://docs.docker.com/dhi/explore/security-concepts/cves/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/cves.md
Description: Understand what CVEs are, how Docker Hardened Images reduce exposure, and how to scan images for vulnerabilities using popular tools.

## Image digests
URL: https://docs.docker.com/dhi/explore/security-concepts/digests/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/digests.md
Description: Learn how Docker Hardened Images help secure every stage of your software supply chain with signed metadata, provenance, and minimal attack surface.

## Minimal or distroless images
URL: https://docs.docker.com/dhi/explore/security-concepts/distroless/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/distroless.md
Description: Learn how Docker Hardened Images use distroless variants to minimize attack surface and remove unnecessary components.

## FIPS
URL: https://docs.docker.com/dhi/explore/security-concepts/fips/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/fips.md
Description: Learn how Docker Hardened Images support FIPS 140 through validated cryptographic modules to help organizations meet compliance requirements.

## glibc and musl support in Docker Hardened Images
URL: https://docs.docker.com/dhi/explore/security-concepts/glibc-musl/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/glibc-musl.md
Description: Compare glibc and musl variants of DHIs to choose the right base image for your application’s compatibility, size, and performance needs.

## Base image hardening
URL: https://docs.docker.com/dhi/explore/security-concepts/hardening/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/hardening.md
Description: Learn how Docker Hardened Images are designed for security, with minimal components, nonroot execution, and secure-by-default configurations.

## Immutable infrastructure
URL: https://docs.docker.com/dhi/explore/security-concepts/immutability/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/immutability.md
Description: Understand how image digests, read-only containers, and signed metadata ensure Docker Hardened Images are tamper-resistant and immutable.

## Image provenance
URL: https://docs.docker.com/dhi/explore/security-concepts/provenance/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/provenance.md
Description: Learn how build provenance metadata helps trace the origin of Docker Hardened Images and support compliance with SLSA.

## Software Bill of Materials (SBOMs)
URL: https://docs.docker.com/dhi/explore/security-concepts/sbom/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/sbom.md
Description: Learn what SBOMs are, why they matter, and how Docker Hardened Images include signed SBOMs to support transparency and compliance.

## Code signing
URL: https://docs.docker.com/dhi/explore/security-concepts/signatures/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/signatures.md
Description: Understand how Docker Hardened Images are cryptographically signed using Cosign to verify authenticity, integrity, and secure provenance.

## Supply-chain Levels for Software Artifacts (SLSA)
URL: https://docs.docker.com/dhi/explore/security-concepts/slsa/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/slsa.md
Description: Learn how Docker Hardened Images comply with SLSA Build Level 3 and how to verify provenance for secure, tamper-resistant builds.

## Software Supply Chain Security
URL: https://docs.docker.com/dhi/explore/security-concepts/sscs/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/sscs.md
Description: Learn how Docker Hardened Images help secure every stage of your software supply chain with signed metadata, provenance, and minimal attack surface.

## Secure Software Development Lifecycle
URL: https://docs.docker.com/dhi/explore/security-concepts/ssdlc/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/ssdlc.md
Description: See how Docker Hardened Images support a secure SDLC by integrating with scanning, signing, and debugging tools.

## STIG
URL: https://docs.docker.com/dhi/explore/security-concepts/stig/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/stig.md
Description: Learn how Docker Hardened Images provide STIG-ready container images with verifiable security scan attestations for government and enterprise compliance requirements.

## Vulnerability Exploitability eXchange (VEX)
URL: https://docs.docker.com/dhi/explore/security-concepts/vex/
Markdown: https://docs.docker.com/dhi/explore/security-concepts/vex.md
Description: Learn how VEX helps you prioritize real risks by identifying which vulnerabilities in Docker Hardened Images are actually exploitable.

## How Docker Hardened Images are tested
URL: https://docs.docker.com/dhi/explore/test/
Markdown: https://docs.docker.com/dhi/explore/test.md
Description: See how Docker Hardened Images are automatically tested for standards compliance, functionality, and security.

## What are hardened images and why use them?
URL: https://docs.docker.com/dhi/explore/what/
Markdown: https://docs.docker.com/dhi/explore/what.md
Description: Learn what a hardened image is, why it matters, and how Docker Hardened Images offer stronger security, compliance, and operational efficiency.

## Docker Hardened Images quickstart
URL: https://docs.docker.com/dhi/get-started/
Markdown: https://docs.docker.com/dhi/get-started.md
Description: Follow a quickstart guide to explore and run a Docker Hardened Image.

## Create and build a Docker Hardened Image
URL: https://docs.docker.com/dhi/how-to/build/
Markdown: https://docs.docker.com/dhi/how-to/build.md
Description: Learn how to write a DHI definition file and build your own Docker Hardened Image from the declarative YAML schema.

## Customize a Docker Hardened Image or chart
URL: https://docs.docker.com/dhi/how-to/customize/
Markdown: https://docs.docker.com/dhi/how-to/customize.md
Description: Learn how to customize Docker Hardened Images (DHI) and charts.

## Use Hardened System Packages
URL: https://docs.docker.com/dhi/how-to/hardened-packages/
Markdown: https://docs.docker.com/dhi/how-to/hardened-packages.md
Description: Learn how to use and verify Docker's hardened system packages in your images.

## Use a Docker Hardened Image chart
URL: https://docs.docker.com/dhi/how-to/helm/
Markdown: https://docs.docker.com/dhi/how-to/helm.md
Description: Learn how to use a Docker Hardened Image chart.

## Mirror a Docker Hardened Image repository
URL: https://docs.docker.com/dhi/how-to/mirror/
Markdown: https://docs.docker.com/dhi/how-to/mirror.md
Description: Learn how to mirror an image into your organization's namespace and optionally push it to another private registry.

## Apply Docker Hardened Image policies to your images
URL: https://docs.docker.com/dhi/how-to/policies/
Markdown: https://docs.docker.com/dhi/how-to/policies.md
Description: Learn how to hold your own images to Docker Hardened Image security and compliance standards using the Docker Scout CLI.

## Scan Docker Hardened Images
URL: https://docs.docker.com/dhi/how-to/scan/
Markdown: https://docs.docker.com/dhi/how-to/scan.md
Description: Learn how to scan Docker Hardened Images for known vulnerabilities using Docker Scout, Grype, or Trivy.

## Search and evaluate Docker Hardened Images
URL: https://docs.docker.com/dhi/how-to/search-evaluate/
Markdown: https://docs.docker.com/dhi/how-to/search-evaluate.md
Description: Learn how to find, compare, and evaluate Docker Hardened Images using the Docker Hub catalog, DHI CLI, and Docker Scout.

## Get started with DHI Select and Enterprise
URL: https://docs.docker.com/dhi/how-to/select-enterprise/
Markdown: https://docs.docker.com/dhi/how-to/select-enterprise.md
Description: Mirror a repository and start using Docker Hardened Images for Select and Enterprise subscriptions.

## Troubleshoot
URL: https://docs.docker.com/dhi/how-to/troubleshoot/
Markdown: https://docs.docker.com/dhi/how-to/troubleshoot.md
Description: Resolve common issues when building, running, or debugging Docker Hardened Images, such as non-root behavior, missing shells, and port access.

## Use a Docker Hardened Image
URL: https://docs.docker.com/dhi/how-to/use/
Markdown: https://docs.docker.com/dhi/how-to/use.md
Description: Learn how to pull, run, and reference Docker Hardened Images in Dockerfiles, CI pipelines, and standard development workflows.

## Verify a Docker Hardened Image or chart
URL: https://docs.docker.com/dhi/how-to/verify/
Markdown: https://docs.docker.com/dhi/how-to/verify.md
Description: Use Docker Scout or cosign to verify signed attestations like SBOMs, provenance, and vulnerability data for Docker Hardened Images and charts.

## Query VEX for a Docker Hardened Image
URL: https://docs.docker.com/dhi/how-to/vex-api/
Markdown: https://docs.docker.com/dhi/how-to/vex-api.md
Description: Use the DHI GraphQL API to fetch VEX statements and suppressed CVEs for a Docker Hardened Image by digest.

## Migration checklist
URL: https://docs.docker.com/dhi/migration/checklist/
Markdown: https://docs.docker.com/dhi/migration/checklist.md
Description: A checklist of considerations when migrating to Docker Hardened Images

## .NET
URL: https://docs.docker.com/dhi/migration/examples/dotnet/
Markdown: https://docs.docker.com/dhi/migration/examples/dotnet.md
Description: Migrate a .NET application to Docker Hardened Images

## Go
URL: https://docs.docker.com/dhi/migration/examples/go/
Markdown: https://docs.docker.com/dhi/migration/examples/go.md
Description: Migrate a Go application to Docker Hardened Images

## Java
URL: https://docs.docker.com/dhi/migration/examples/java/
Markdown: https://docs.docker.com/dhi/migration/examples/java.md
Description: Migrate a Java application to Docker Hardened Images

## Node.js
URL: https://docs.docker.com/dhi/migration/examples/node/
Markdown: https://docs.docker.com/dhi/migration/examples/node.md
Description: Migrate a Node.js application to Docker Hardened Images

## Python
URL: https://docs.docker.com/dhi/migration/examples/python/
Markdown: https://docs.docker.com/dhi/migration/examples/python.md
Description: Migrate a Python application to Docker Hardened Images

## Migrate from Alpine or Debian
URL: https://docs.docker.com/dhi/migration/migrate-from-doi/
Markdown: https://docs.docker.com/dhi/migration/migrate-from-doi.md
Description: Step-by-step guide to migrate from Docker Official Images to Docker Hardened Images

## Migrate from Ubuntu
URL: https://docs.docker.com/dhi/migration/migrate-from-ubuntu/
Markdown: https://docs.docker.com/dhi/migration/migrate-from-ubuntu.md
Description: Step-by-step guide to migrate from Ubuntu-based images to Docker Hardened Images

## Migrate from Wolfi
URL: https://docs.docker.com/dhi/migration/migrate-from-wolfi/
Markdown: https://docs.docker.com/dhi/migration/migrate-from-wolfi.md
Description: Step-by-step guide to migrate from Wolfi distribution images to Docker Hardened Images

## Migrate using Gordon
URL: https://docs.docker.com/dhi/migration/migrate-with-ai/
Markdown: https://docs.docker.com/dhi/migration/migrate-with-ai.md
Description: Use Gordon to automatically migrate your Dockerfile to Docker Hardened Images

## DHI CLI release notes
URL: https://docs.docker.com/dhi/release-notes/cli/
Markdown: https://docs.docker.com/dhi/release-notes/cli.md
Description: New features, bug fixes, and changes in the DHI CLI

## Docker Hardened Images release notes
URL: https://docs.docker.com/dhi/release-notes/platform/
Markdown: https://docs.docker.com/dhi/release-notes/platform.md
Description: Learn about the latest features and changes in Docker Hardened Images

## Resources and feedback
URL: https://docs.docker.com/dhi/resources/
Markdown: https://docs.docker.com/dhi/resources.md
Description: Additional resources, community links, GitHub repositories, and how to give feedback for Docker Hardened Images.

## Use the DHI API
URL: https://docs.docker.com/dhi/tools/api/
Markdown: https://docs.docker.com/dhi/tools/api.md
Description: Query Docker Hardened Images data programmatically using the DHI GraphQL API.

## Use the DHI CLI
URL: https://docs.docker.com/dhi/tools/cli/
Markdown: https://docs.docker.com/dhi/tools/cli.md
Description: Learn how to install and use docker dhi, the command-line interface for managing Docker Hardened Images.

## Use Docker Hub
URL: https://docs.docker.com/dhi/tools/hub/
Markdown: https://docs.docker.com/dhi/tools/hub.md
Description: Browse the DHI catalog on Docker Hub to search repositories, inspect image metadata, and view SBOMs, CVEs, and attestations.

## Use the DHI MCP server
URL: https://docs.docker.com/dhi/tools/mcp/
Markdown: https://docs.docker.com/dhi/tools/mcp.md
Description: Connect an AI assistant to the Docker Hardened Images catalog using the DHI MCP server to search repositories, inspect images, view SBOMs, and check CVEs.

## Use the DHI Terraform provider
URL: https://docs.docker.com/dhi/tools/terraform/
Markdown: https://docs.docker.com/dhi/tools/terraform.md
Description: Use the DHI Terraform provider to manage mirrors and customizations as infrastructure as code.

## Generative AI content
URL: https://docs.docker.com/docker-hub/image-library/catalogs/
Markdown: https://docs.docker.com/docker-hub/image-library/catalogs.md
Description: Explore Docker Hub's generative AI catalogs and sandbox kits.

## Mirror the Docker Hub library
URL: https://docs.docker.com/docker-hub/image-library/mirror/
Markdown: https://docs.docker.com/docker-hub/image-library/mirror.md
Description: Setting-up a local mirror for Docker Hub images

## Docker Hub search
URL: https://docs.docker.com/docker-hub/image-library/search/
Markdown: https://docs.docker.com/docker-hub/image-library/search.md
Description: Discover how to browse and search Docker Hub's extensive resources.

## Trusted content
URL: https://docs.docker.com/docker-hub/image-library/trusted-content/
Markdown: https://docs.docker.com/docker-hub/image-library/trusted-content.md
Description: Learn about Docker Hub's trusted content.

## Docker Hub MCP server
URL: https://docs.docker.com/docker-hub/mcp-server/
Markdown: https://docs.docker.com/docker-hub/mcp-server.md
Description: The Docker Hub MCP Server makes Docker Hub image metadata accessible to LLMs for content discovery.

## Docker Hub quickstart
URL: https://docs.docker.com/docker-hub/quickstart/
Markdown: https://docs.docker.com/docker-hub/quickstart.md
Description: Learn how to get started using Docker Hub

## Docker Hub release notes
URL: https://docs.docker.com/docker-hub/release-notes/
Markdown: https://docs.docker.com/docker-hub/release-notes.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Hub

## Archive or unarchive a repository
URL: https://docs.docker.com/docker-hub/repos/archive/
Markdown: https://docs.docker.com/docker-hub/repos/archive.md
Description: Learn how to archive or unarchive a repository on Docker Hub

## Create a repository
URL: https://docs.docker.com/docker-hub/repos/create/
Markdown: https://docs.docker.com/docker-hub/repos/create.md
Description: Learn how to create a repository on Docker Hub

## Delete a repository
URL: https://docs.docker.com/docker-hub/repos/delete/
Markdown: https://docs.docker.com/docker-hub/repos/delete.md
Description: Learn how to delete a repository on Docker Hub

## Access management
URL: https://docs.docker.com/docker-hub/repos/manage/access/
Markdown: https://docs.docker.com/docker-hub/repos/manage/access.md
Description: Discover how to manage access to repositories on Docker Hub.

## Advanced options for autobuild and autotest
URL: https://docs.docker.com/docker-hub/repos/manage/builds/advanced/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/advanced.md
Description: Automated builds

## Automated repository tests
URL: https://docs.docker.com/docker-hub/repos/manage/builds/automated-testing/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/automated-testing.md
Description: Automated tests

## Configure automated builds from GitHub and BitBucket
URL: https://docs.docker.com/docker-hub/repos/manage/builds/link-source/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/link-source.md
Description: Link to GitHub and BitBucket

## Manage autobuilds
URL: https://docs.docker.com/docker-hub/repos/manage/builds/manage-builds/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/manage-builds.md
Description: How to manage autobuilds in Docker Hub

## Migrate from Autobuilds
URL: https://docs.docker.com/docker-hub/repos/manage/builds/migrate/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/migrate.md
Description: Migrate from Autobuilds to CI/CD workflows

## Set up automated builds
URL: https://docs.docker.com/docker-hub/repos/manage/builds/setup/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/setup.md
Description: Set up automated builds

## Troubleshoot your autobuilds
URL: https://docs.docker.com/docker-hub/repos/manage/builds/troubleshoot/
Markdown: https://docs.docker.com/docker-hub/repos/manage/builds/troubleshoot.md
Description: How to troubleshoot Automated builds

## Export organization repositories to CSV
URL: https://docs.docker.com/docker-hub/repos/manage/export/
Markdown: https://docs.docker.com/docker-hub/repos/manage/export.md
Description: Learn how to export a complete list of your organization's Docker Hub repositories using the API.

## Bulk migrate images
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/bulk-migrate/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/bulk-migrate.md
Description: Learn how to migrate multiple Docker images and tags between organizations using scripts and automation.

## Immutable tags on Docker Hub
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/immutable-tags/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/immutable-tags.md
Description: Learn about immutable tags and how they help maintain image version consistency on Docker Hub.

## Image Management
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/manage/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/manage.md
Description: Discover how to delete image tags.

## Move images between repositories
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/move/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/move.md
Description: Discover how to move images between repositories.

## Software artifacts on Docker Hub
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts.md
Description: You can use Docker Hub to store software artifacts packaged as OCI artifacts.

## Push images to a repository
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/push/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/push.md
Description: Learn how to add content to a repository on Docker Hub.

## Tags on Docker Hub
URL: https://docs.docker.com/docker-hub/repos/manage/hub-images/tags/
Markdown: https://docs.docker.com/docker-hub/repos/manage/hub-images/tags.md
Description: Discover how to manage repository tags on Docker Hub.

## Repository information
URL: https://docs.docker.com/docker-hub/repos/manage/information/
Markdown: https://docs.docker.com/docker-hub/repos/manage/information.md
Description: Learn how to describe and optimize your Docker Hub repositories for better discoverability.

## Docker-Sponsored Open Source Program
URL: https://docs.docker.com/docker-hub/repos/manage/trusted-content/dsos-program/
Markdown: https://docs.docker.com/docker-hub/repos/manage/trusted-content/dsos-program.md
Description: Learn about the Docker-Sponsored Open Source Program and how it works

## Docker Verified Publisher Program
URL: https://docs.docker.com/docker-hub/repos/manage/trusted-content/dvp-program/
Markdown: https://docs.docker.com/docker-hub/repos/manage/trusted-content/dvp-program.md
Description: Learn what the Docker Verified Publisher Program is and how it works

## Insights and analytics
URL: https://docs.docker.com/docker-hub/repos/manage/trusted-content/insights-analytics/
Markdown: https://docs.docker.com/docker-hub/repos/manage/trusted-content/insights-analytics.md
Description: Discover how to access usage statistics of your images on Docker Hub

## Docker Official Images
URL: https://docs.docker.com/docker-hub/repos/manage/trusted-content/official-images/
Markdown: https://docs.docker.com/docker-hub/repos/manage/trusted-content/official-images.md
Description: This article describes how Docker Official Images are created, and how you can contribute or leave feedback.

## Image security insights
URL: https://docs.docker.com/docker-hub/repos/manage/vulnerability-scanning/
Markdown: https://docs.docker.com/docker-hub/repos/manage/vulnerability-scanning.md
Description: Learn about vulnerability scanning and Docker Scout image analysis in Docker Hub.

## Webhooks
URL: https://docs.docker.com/docker-hub/repos/manage/webhooks/
Markdown: https://docs.docker.com/docker-hub/repos/manage/webhooks.md
Description: Docker Hub Webhooks

## Settings
URL: https://docs.docker.com/docker-hub/settings/
Markdown: https://docs.docker.com/docker-hub/settings.md
Description: Learn about settings in Docker Hub

## Troubleshoot Docker Hub
URL: https://docs.docker.com/docker-hub/troubleshoot/
Markdown: https://docs.docker.com/docker-hub/troubleshoot.md
Description: Learn how to troubleshoot common Docker Hub issues.

## Best practices for optimizing Docker Hub usage
URL: https://docs.docker.com/docker-hub/usage/manage/
Markdown: https://docs.docker.com/docker-hub/usage/manage.md
Description: Learn how to optimize and manage your Docker Hub usage.

## Docker Hub pull usage and limits
URL: https://docs.docker.com/docker-hub/usage/pulls/
Markdown: https://docs.docker.com/docker-hub/usage/pulls.md
Description: Learn about pull usage and limits for Docker Hub.

## Completion
URL: https://docs.docker.com/engine/cli/completion/
Markdown: https://docs.docker.com/engine/cli/completion.md
Description: Set up your shell to get autocomplete for Docker commands and flags

## Filter commands
URL: https://docs.docker.com/engine/cli/filter/
Markdown: https://docs.docker.com/engine/cli/filter.md
Description: Use the filtering function in the CLI to selectively include resources that match the pattern you define.

## Format command and log output
URL: https://docs.docker.com/engine/cli/formatting/
Markdown: https://docs.docker.com/engine/cli/formatting.md
Description: CLI and log output formatting reference

## OpenTelemetry for the Docker CLI
URL: https://docs.docker.com/engine/cli/otel/
Markdown: https://docs.docker.com/engine/cli/otel.md
Description: Learn about how to capture OpenTelemetry metrics for the Docker command line

## Use a proxy server with the Docker CLI
URL: https://docs.docker.com/engine/cli/proxy/
Markdown: https://docs.docker.com/engine/cli/proxy.md
Description: How to configure the Docker client CLI to use a proxy server

## GPU access
URL: https://docs.docker.com/engine/containers/gpu/
Markdown: https://docs.docker.com/engine/containers/gpu.md
Description: How to access NVIDIA GPUs from a container

## Run multiple processes in a container
URL: https://docs.docker.com/engine/containers/multi-service_container/
Markdown: https://docs.docker.com/engine/containers/multi-service_container.md
Description: Learn how to run more than one process in a single container

## Resource constraints
URL: https://docs.docker.com/engine/containers/resource_constraints/
Markdown: https://docs.docker.com/engine/containers/resource_constraints.md
Description: Limit container memory and CPU usage with runtime configuration flags

## Running containers
URL: https://docs.docker.com/engine/containers/run/
Markdown: https://docs.docker.com/engine/containers/run.md
Description: Running and configuring containers with the Docker CLI

## Runtime metrics
URL: https://docs.docker.com/engine/containers/runmetrics/
Markdown: https://docs.docker.com/engine/containers/runmetrics.md
Description: Learn how to measure running containers, and about the different metrics

## Start containers automatically
URL: https://docs.docker.com/engine/containers/start-containers-automatically/
Markdown: https://docs.docker.com/engine/containers/start-containers-automatically.md
Description: How to start containers automatically

## Alternative container runtimes
URL: https://docs.docker.com/engine/daemon/alternative-runtimes/
Markdown: https://docs.docker.com/engine/daemon/alternative-runtimes.md
Description: Docker Engine uses runc as the default container runtime, but you can specify alternative runtimes using the CLI or by configuring the daemon

## Run containerd in the Docker daemon
URL: https://docs.docker.com/engine/daemon/embedded-containerd/
Markdown: https://docs.docker.com/engine/daemon/embedded-containerd.md
Description: Configure Docker Engine to run an experimental containerd server in the Docker daemon process

## Use IPv6 networking
URL: https://docs.docker.com/engine/daemon/ipv6/
Markdown: https://docs.docker.com/engine/daemon/ipv6.md
Description: How to enable IPv6 support in the Docker daemon

## Live restore
URL: https://docs.docker.com/engine/daemon/live-restore/
Markdown: https://docs.docker.com/engine/daemon/live-restore.md
Description: Learn how to keep containers running when the daemon isn't available

## Read the daemon logs
URL: https://docs.docker.com/engine/daemon/logs/
Markdown: https://docs.docker.com/engine/daemon/logs.md
Description: How to read Docker daemon logs and force a stack trace using SIGUSR1 for debugging

## Collect Docker metrics with Prometheus
URL: https://docs.docker.com/engine/daemon/prometheus/
Markdown: https://docs.docker.com/engine/daemon/prometheus.md
Description: Collecting Docker metrics with Prometheus

## Daemon proxy configuration
URL: https://docs.docker.com/engine/daemon/proxy/
Markdown: https://docs.docker.com/engine/daemon/proxy.md
Description: Learn how to configure the Docker daemon to use an HTTP proxy

## Configure remote access for Docker daemon
URL: https://docs.docker.com/engine/daemon/remote-access/
Markdown: https://docs.docker.com/engine/daemon/remote-access.md
Description: Configuring remote access allows Docker to accept requests from remote hosts by configuring it to listen on an IP address and port as well as the Unix socket

## Start the daemon
URL: https://docs.docker.com/engine/daemon/start/
Markdown: https://docs.docker.com/engine/daemon/start.md
Description: Starting the Docker daemon manually

## Troubleshooting the Docker daemon
URL: https://docs.docker.com/engine/daemon/troubleshoot/
Markdown: https://docs.docker.com/engine/daemon/troubleshoot.md
Description: Learn how to troubleshoot errors and misconfigurations in the Docker daemon

## Deprecated Docker Engine features
URL: https://docs.docker.com/engine/deprecated/
Markdown: https://docs.docker.com/engine/deprecated.md
Description: Deprecated Features.

## Plugin Config Version 1 of Plugin V2
URL: https://docs.docker.com/engine/extend/config/
Markdown: https://docs.docker.com/engine/extend/config.md
Description: How to develop and use a plugin with the managed plugin system

## Use Docker Engine plugins
URL: https://docs.docker.com/engine/extend/legacy_plugins/
Markdown: https://docs.docker.com/engine/extend/legacy_plugins.md
Description: How to add additional functionality to Docker with plugins extensions

## Docker Plugin API
URL: https://docs.docker.com/engine/extend/plugin_api/
Markdown: https://docs.docker.com/engine/extend/plugin_api.md
Description: How to write Docker plugins extensions

## Access authorization plugin
URL: https://docs.docker.com/engine/extend/plugins_authorization/
Markdown: https://docs.docker.com/engine/extend/plugins_authorization.md
Description: How to create authorization plugins to manage access control to your Docker daemon.

## Docker log driver plugins
URL: https://docs.docker.com/engine/extend/plugins_logging/
Markdown: https://docs.docker.com/engine/extend/plugins_logging.md
Description: Log driver plugins.

## Docker network driver plugins
URL: https://docs.docker.com/engine/extend/plugins_network/
Markdown: https://docs.docker.com/engine/extend/plugins_network.md
Description: Network driver plugins.

## Docker volume plugins
URL: https://docs.docker.com/engine/extend/plugins_volume/
Markdown: https://docs.docker.com/engine/extend/plugins_volume.md
Description: How to manage data with external volume plugins

## Install Docker Engine from binaries
URL: https://docs.docker.com/engine/install/binaries/
Markdown: https://docs.docker.com/engine/install/binaries.md
Description: Learn how to install Docker as a binary. These instructions are most suitable for testing purposes.

## Install Docker Engine on CentOS
URL: https://docs.docker.com/engine/install/centos/
Markdown: https://docs.docker.com/engine/install/centos.md
Description: Learn how to install Docker Engine on CentOS. These instructions cover the different installation methods, how to uninstall, and next steps.

## Install Docker Engine on Debian
URL: https://docs.docker.com/engine/install/debian/
Markdown: https://docs.docker.com/engine/install/debian.md
Description: Learn how to install Docker Engine on Debian. These instructions cover the different installation methods, how to uninstall, and next steps.

## Install Docker Engine on Fedora
URL: https://docs.docker.com/engine/install/fedora/
Markdown: https://docs.docker.com/engine/install/fedora.md
Description: Learn how to install Docker Engine on Fedora. These instructions cover the different installation methods, how to uninstall, and next steps.

## Linux post-installation steps for Docker Engine
URL: https://docs.docker.com/engine/install/linux-postinstall/
Markdown: https://docs.docker.com/engine/install/linux-postinstall.md
Description: Find the recommended Docker Engine post-installation steps for Linux users, including how to run Docker as a non-root user and more.

## Install Docker Engine on Raspberry Pi OS (32-bit / armhf)
URL: https://docs.docker.com/engine/install/raspberry-pi-os/
Markdown: https://docs.docker.com/engine/install/raspberry-pi-os.md
Description: Learn how to install Docker Engine on a 32-bit Raspberry Pi OS system. These instructions cover the different installation methods, how to uninstall, and next steps. Note that 32-bit support will be deprecated in Docker Engine v29 and later.

## Install Docker Engine on RHEL
URL: https://docs.docker.com/engine/install/rhel/
Markdown: https://docs.docker.com/engine/install/rhel.md
Description: Learn how to install Docker Engine on RHEL. These instructions cover the different installation methods, how to uninstall, and next steps.

## Install Docker Engine on Ubuntu
URL: https://docs.docker.com/engine/install/ubuntu/
Markdown: https://docs.docker.com/engine/install/ubuntu.md
Description: Jumpstart your client-side server applications with Docker Engine on Ubuntu. This guide details prerequisites and multiple methods to install Docker Engine on Ubuntu.

## Configure logging drivers
URL: https://docs.docker.com/engine/logging/configure/
Markdown: https://docs.docker.com/engine/logging/configure.md
Description: Learn how to configure logging driver for the Docker daemon

## Amazon CloudWatch Logs logging driver
URL: https://docs.docker.com/engine/logging/drivers/awslogs/
Markdown: https://docs.docker.com/engine/logging/drivers/awslogs.md
Description: Learn how to use the Amazon CloudWatch Logs logging driver with Docker Engine

## ETW logging driver
URL: https://docs.docker.com/engine/logging/drivers/etwlogs/
Markdown: https://docs.docker.com/engine/logging/drivers/etwlogs.md
Description: Learn how to use the Event Tracing for Windows (ETW) logging driver with Docker Engine

## Fluentd logging driver
URL: https://docs.docker.com/engine/logging/drivers/fluentd/
Markdown: https://docs.docker.com/engine/logging/drivers/fluentd.md
Description: Learn how to use the fluentd logging driver

## Google Cloud Logging driver
URL: https://docs.docker.com/engine/logging/drivers/gcplogs/
Markdown: https://docs.docker.com/engine/logging/drivers/gcplogs.md
Description: Learn how to use the Google Cloud Logging driver with Docker Engine

## Graylog Extended Format logging driver
URL: https://docs.docker.com/engine/logging/drivers/gelf/
Markdown: https://docs.docker.com/engine/logging/drivers/gelf.md
Description: Learn how to use the Graylog Extended Format logging driver with Docker Engine

## Journald logging driver
URL: https://docs.docker.com/engine/logging/drivers/journald/
Markdown: https://docs.docker.com/engine/logging/drivers/journald.md
Description: Learn how to use the Journald logging driver with Docker Engine

## JSON File logging driver
URL: https://docs.docker.com/engine/logging/drivers/json-file/
Markdown: https://docs.docker.com/engine/logging/drivers/json-file.md
Description: Learn how to use the json-file logging driver with Docker Engine

## Local file logging driver
URL: https://docs.docker.com/engine/logging/drivers/local/
Markdown: https://docs.docker.com/engine/logging/drivers/local.md
Description: Learn how to use the local logging driver with Docker Engine

## Splunk logging driver
URL: https://docs.docker.com/engine/logging/drivers/splunk/
Markdown: https://docs.docker.com/engine/logging/drivers/splunk.md
Description: Learn how to use the Splunk logging driver with Docker Engine

## Syslog logging driver
URL: https://docs.docker.com/engine/logging/drivers/syslog/
Markdown: https://docs.docker.com/engine/logging/drivers/syslog.md
Description: Learn how to use the syslog logging driver with Docker Engine

## Use docker logs with remote logging drivers
URL: https://docs.docker.com/engine/logging/dual-logging/
Markdown: https://docs.docker.com/engine/logging/dual-logging.md
Description: Learn how to read container logs locally when using a third party logging solution.

## Customize log driver output
URL: https://docs.docker.com/engine/logging/log_tags/
Markdown: https://docs.docker.com/engine/logging/log_tags.md
Description: Learn about how to format log output with Go templates

## Use a logging driver plugin
URL: https://docs.docker.com/engine/logging/plugins/
Markdown: https://docs.docker.com/engine/logging/plugins.md
Description: Learn about logging driver plugins for extending and customizing Docker's logging capabilities

## Docker contexts
URL: https://docs.docker.com/engine/manage-resources/contexts/
Markdown: https://docs.docker.com/engine/manage-resources/contexts.md
Description: Learn about managing multiple daemons from a single client with contexts

## Docker object labels
URL: https://docs.docker.com/engine/manage-resources/labels/
Markdown: https://docs.docker.com/engine/manage-resources/labels.md
Description: Learn about labels, a tool to manage metadata on Docker objects.

## Prune unused Docker objects
URL: https://docs.docker.com/engine/manage-resources/pruning/
Markdown: https://docs.docker.com/engine/manage-resources/pruning.md
Description: Free up disk space by removing unused resources with the prune command

## Use CA certificates with Docker
URL: https://docs.docker.com/engine/network/ca-certs/
Markdown: https://docs.docker.com/engine/network/ca-certs.md
Description: Learn how to install and use CA certificates on the Docker host and in Linux containers

## Bridge network driver
URL: https://docs.docker.com/engine/network/drivers/bridge/
Markdown: https://docs.docker.com/engine/network/drivers/bridge.md
Description: All about using user-defined bridge networks and the default bridge

## Host network driver
URL: https://docs.docker.com/engine/network/drivers/host/
Markdown: https://docs.docker.com/engine/network/drivers/host.md
Description: All about exposing containers on the Docker host's network

## IPvlan network driver
URL: https://docs.docker.com/engine/network/drivers/ipvlan/
Markdown: https://docs.docker.com/engine/network/drivers/ipvlan.md
Description: All about using IPvlan to make your containers appear like physical machines on the network

## Macvlan network driver
URL: https://docs.docker.com/engine/network/drivers/macvlan/
Markdown: https://docs.docker.com/engine/network/drivers/macvlan.md
Description: All about using Macvlan to make your containers appear like physical machines on the network

## None network driver
URL: https://docs.docker.com/engine/network/drivers/none/
Markdown: https://docs.docker.com/engine/network/drivers/none.md
Description: How to isolate the networking stack of a container using the none driver

## Overlay network driver
URL: https://docs.docker.com/engine/network/drivers/overlay/
Markdown: https://docs.docker.com/engine/network/drivers/overlay.md
Description: All about using overlay networks

## Docker with iptables
URL: https://docs.docker.com/engine/network/firewall-iptables/
Markdown: https://docs.docker.com/engine/network/firewall-iptables.md
Description: How Docker works with iptables

## Docker with nftables
URL: https://docs.docker.com/engine/network/firewall-nftables/
Markdown: https://docs.docker.com/engine/network/firewall-nftables.md
Description: How Docker works with nftables

## Legacy container links
URL: https://docs.docker.com/engine/network/links/
Markdown: https://docs.docker.com/engine/network/links.md
Description: Learn how to connect Docker containers together.

## Packet filtering and firewalls
URL: https://docs.docker.com/engine/network/packet-filtering-firewalls/
Markdown: https://docs.docker.com/engine/network/packet-filtering-firewalls.md
Description: How Docker works with packet filtering, iptables, and firewalls

## Port publishing and mapping
URL: https://docs.docker.com/engine/network/port-publishing/
Markdown: https://docs.docker.com/engine/network/port-publishing.md
Description: Accessing container ports

## Docker Engine 17.03 release notes
URL: https://docs.docker.com/engine/release-notes/17.03/
Markdown: https://docs.docker.com/engine/release-notes/17.03.md

## Docker Engine 17.04 release notes
URL: https://docs.docker.com/engine/release-notes/17.04/
Markdown: https://docs.docker.com/engine/release-notes/17.04.md

## Docker Engine 17.05 release notes
URL: https://docs.docker.com/engine/release-notes/17.05/
Markdown: https://docs.docker.com/engine/release-notes/17.05.md

## Docker Engine 17.06 release notes
URL: https://docs.docker.com/engine/release-notes/17.06/
Markdown: https://docs.docker.com/engine/release-notes/17.06.md

## Docker Engine 17.07 release notes
URL: https://docs.docker.com/engine/release-notes/17.07/
Markdown: https://docs.docker.com/engine/release-notes/17.07.md

## Docker Engine 17.09 release notes
URL: https://docs.docker.com/engine/release-notes/17.09/
Markdown: https://docs.docker.com/engine/release-notes/17.09.md

## Docker Engine 17.10 release notes
URL: https://docs.docker.com/engine/release-notes/17.10/
Markdown: https://docs.docker.com/engine/release-notes/17.10.md

## Docker Engine 17.11 release notes
URL: https://docs.docker.com/engine/release-notes/17.11/
Markdown: https://docs.docker.com/engine/release-notes/17.11.md

## Docker Engine 17.12 release notes
URL: https://docs.docker.com/engine/release-notes/17.12/
Markdown: https://docs.docker.com/engine/release-notes/17.12.md

## Docker Engine 18.01 release notes
URL: https://docs.docker.com/engine/release-notes/18.01/
Markdown: https://docs.docker.com/engine/release-notes/18.01.md

## Docker Engine 18.02 release notes
URL: https://docs.docker.com/engine/release-notes/18.02/
Markdown: https://docs.docker.com/engine/release-notes/18.02.md

## Docker Engine 18.03 release notes
URL: https://docs.docker.com/engine/release-notes/18.03/
Markdown: https://docs.docker.com/engine/release-notes/18.03.md

## Docker Engine 18.04 release notes
URL: https://docs.docker.com/engine/release-notes/18.04/
Markdown: https://docs.docker.com/engine/release-notes/18.04.md

## Docker Engine 18.05 release notes
URL: https://docs.docker.com/engine/release-notes/18.05/
Markdown: https://docs.docker.com/engine/release-notes/18.05.md

## Docker Engine 18.06 release notes
URL: https://docs.docker.com/engine/release-notes/18.06/
Markdown: https://docs.docker.com/engine/release-notes/18.06.md

## Docker Engine 18.09 release notes
URL: https://docs.docker.com/engine/release-notes/18.09/
Markdown: https://docs.docker.com/engine/release-notes/18.09.md

## Docker Engine 19.03 release notes
URL: https://docs.docker.com/engine/release-notes/19.03/
Markdown: https://docs.docker.com/engine/release-notes/19.03.md

## Docker Engine 20.10 release notes
URL: https://docs.docker.com/engine/release-notes/20.10/
Markdown: https://docs.docker.com/engine/release-notes/20.10.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine 23.0 release notes
URL: https://docs.docker.com/engine/release-notes/23.0/
Markdown: https://docs.docker.com/engine/release-notes/23.0.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine 24.0 release notes
URL: https://docs.docker.com/engine/release-notes/24.0/
Markdown: https://docs.docker.com/engine/release-notes/24.0.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine 25.0 release notes
URL: https://docs.docker.com/engine/release-notes/25.0/
Markdown: https://docs.docker.com/engine/release-notes/25.0.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine 26.0 release notes
URL: https://docs.docker.com/engine/release-notes/26.0/
Markdown: https://docs.docker.com/engine/release-notes/26.0.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine 26.1 release notes
URL: https://docs.docker.com/engine/release-notes/26.1/
Markdown: https://docs.docker.com/engine/release-notes/26.1.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine version 27 release notes
URL: https://docs.docker.com/engine/release-notes/27/
Markdown: https://docs.docker.com/engine/release-notes/27.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine version 28 release notes
URL: https://docs.docker.com/engine/release-notes/28/
Markdown: https://docs.docker.com/engine/release-notes/28.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine version 29 release notes
URL: https://docs.docker.com/engine/release-notes/29/
Markdown: https://docs.docker.com/engine/release-notes/29.md
Description: Learn about the new features, bug fixes, and breaking changes for Docker Engine

## Docker Engine prior releases
URL: https://docs.docker.com/engine/release-notes/prior-releases/
Markdown: https://docs.docker.com/engine/release-notes/prior-releases.md
Description: Release notes for Docker CE

## Antivirus software and Docker
URL: https://docs.docker.com/engine/security/antivirus/
Markdown: https://docs.docker.com/engine/security/antivirus.md
Description: General guidelines for using antivirus software with Docker

## AppArmor security profiles for Docker
URL: https://docs.docker.com/engine/security/apparmor/
Markdown: https://docs.docker.com/engine/security/apparmor.md
Description: Enabling AppArmor in Docker

## Verify repository client with certificates
URL: https://docs.docker.com/engine/security/certificates/
Markdown: https://docs.docker.com/engine/security/certificates.md
Description: How to set up and use certificates with a registry to verify access

## Docker security non-events
URL: https://docs.docker.com/engine/security/non-events/
Markdown: https://docs.docker.com/engine/security/non-events.md
Description: Review of security vulnerabilities Docker mitigated

## Protect the Docker daemon socket
URL: https://docs.docker.com/engine/security/protect-access/
Markdown: https://docs.docker.com/engine/security/protect-access.md
Description: How to setup and run Docker with SSH or HTTPS

## Tips
URL: https://docs.docker.com/engine/security/rootless/tips/
Markdown: https://docs.docker.com/engine/security/rootless/tips.md
Description: Tips for the Rootless mode

## Troubleshooting
URL: https://docs.docker.com/engine/security/rootless/troubleshoot/
Markdown: https://docs.docker.com/engine/security/rootless/troubleshoot.md
Description: Troubleshooting the Rootless mode

## UID/GID mapping
URL: https://docs.docker.com/engine/security/rootless/uid-gid-mapping/
Markdown: https://docs.docker.com/engine/security/rootless/uid-gid-mapping.md
Description: How container UIDs and GIDs are mapped to the host in rootless mode

## Seccomp security profiles for Docker
URL: https://docs.docker.com/engine/security/seccomp/
Markdown: https://docs.docker.com/engine/security/seccomp.md
Description: Enabling seccomp in Docker

## Deploy Notary Server with Compose
URL: https://docs.docker.com/engine/security/trust/deploying_notary/
Markdown: https://docs.docker.com/engine/security/trust/deploying_notary.md
Description: Deploying Notary

## Automation with content trust
URL: https://docs.docker.com/engine/security/trust/trust_automation/
Markdown: https://docs.docker.com/engine/security/trust/trust_automation.md
Description: Automating content push pulls with trust

## Delegations for content trust
URL: https://docs.docker.com/engine/security/trust/trust_delegation/
Markdown: https://docs.docker.com/engine/security/trust/trust_delegation.md
Description: Delegations for content trust

## Manage keys for content trust
URL: https://docs.docker.com/engine/security/trust/trust_key_mng/
Markdown: https://docs.docker.com/engine/security/trust/trust_key_mng.md
Description: Manage keys for content trust

## Play in a content trust sandbox
URL: https://docs.docker.com/engine/security/trust/trust_sandbox/
Markdown: https://docs.docker.com/engine/security/trust/trust_sandbox.md
Description: Play in a trust sandbox

## Isolate containers with a user namespace
URL: https://docs.docker.com/engine/security/userns-remap/
Markdown: https://docs.docker.com/engine/security/userns-remap.md
Description: Isolate containers within a user namespace

## Bind mounts
URL: https://docs.docker.com/engine/storage/bind-mounts/
Markdown: https://docs.docker.com/engine/storage/bind-mounts.md
Description: Using bind mounts

## containerd image store with Docker Engine
URL: https://docs.docker.com/engine/storage/containerd/
Markdown: https://docs.docker.com/engine/storage/containerd.md
Description: Learn about the containerd image store

## BTRFS storage driver
URL: https://docs.docker.com/engine/storage/drivers/btrfs-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/btrfs-driver.md
Description: Learn how to optimize your use of Btrfs driver.

## Device Mapper storage driver (deprecated)
URL: https://docs.docker.com/engine/storage/drivers/device-mapper-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/device-mapper-driver.md
Description: Learn how to optimize your use of device mapper driver.

## OverlayFS storage driver
URL: https://docs.docker.com/engine/storage/drivers/overlayfs-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/overlayfs-driver.md
Description: Learn how to optimize your use of OverlayFS driver.

## Select a storage driver
URL: https://docs.docker.com/engine/storage/drivers/select-storage-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/select-storage-driver.md
Description: Learn how to select the proper storage driver for your container.

## VFS storage driver
URL: https://docs.docker.com/engine/storage/drivers/vfs-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/vfs-driver.md
Description: Learn how to optimize your use of VFS driver.

## windowsfilter storage driver
URL: https://docs.docker.com/engine/storage/drivers/windowsfilter-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/windowsfilter-driver.md
Description: Learn about the windowsfilter storage driver

## ZFS storage driver
URL: https://docs.docker.com/engine/storage/drivers/zfs-driver/
Markdown: https://docs.docker.com/engine/storage/drivers/zfs-driver.md
Description: Learn how to optimize your use of ZFS driver.

## Image mounts
URL: https://docs.docker.com/engine/storage/image-mounts/
Markdown: https://docs.docker.com/engine/storage/image-mounts.md
Description: Using image mounts

## tmpfs mounts
URL: https://docs.docker.com/engine/storage/tmpfs/
Markdown: https://docs.docker.com/engine/storage/tmpfs.md
Description: Using tmpfs mounts

## Volumes
URL: https://docs.docker.com/engine/storage/volumes/
Markdown: https://docs.docker.com/engine/storage/volumes.md
Description: Learn how to create, manage, and use volumes instead of bind mounts for persisting data generated and used by Docker.

## Administer and maintain a swarm of Docker Engines
URL: https://docs.docker.com/engine/swarm/admin_guide/
Markdown: https://docs.docker.com/engine/swarm/admin_guide.md
Description: Manager administration guide

## Store configuration data using Docker Configs
URL: https://docs.docker.com/engine/swarm/configs/
Markdown: https://docs.docker.com/engine/swarm/configs.md
Description: How to store configuration data separate from the runtime

## How nodes work
URL: https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/
Markdown: https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes.md
Description: How swarm nodes work

## Manage swarm security with public key infrastructure (PKI)
URL: https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/
Markdown: https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki.md
Description: How PKI works in swarm mode

## How services work
URL: https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/
Markdown: https://docs.docker.com/engine/swarm/how-swarm-mode-works/services.md
Description: How swarm mode services work

## Swarm task states
URL: https://docs.docker.com/engine/swarm/how-swarm-mode-works/swarm-task-states/
Markdown: https://docs.docker.com/engine/swarm/how-swarm-mode-works/swarm-task-states.md
Description: Learn about tasks that are scheduled on your swarm.

## Use Swarm mode routing mesh
URL: https://docs.docker.com/engine/swarm/ingress/
Markdown: https://docs.docker.com/engine/swarm/ingress.md
Description: Use the routing mesh to publish services externally to a swarm

## Join nodes to a swarm
URL: https://docs.docker.com/engine/swarm/join-nodes/
Markdown: https://docs.docker.com/engine/swarm/join-nodes.md
Description: Add worker and manager nodes to a swarm

## Swarm mode key concepts
URL: https://docs.docker.com/engine/swarm/key-concepts/
Markdown: https://docs.docker.com/engine/swarm/key-concepts.md
Description: Introducing key concepts for Docker Engine swarm mode

## Manage nodes in a swarm
URL: https://docs.docker.com/engine/swarm/manage-nodes/
Markdown: https://docs.docker.com/engine/swarm/manage-nodes.md
Description: Manage existing nodes in a swarm

## Manage swarm service networks
URL: https://docs.docker.com/engine/swarm/networking/
Markdown: https://docs.docker.com/engine/swarm/networking.md
Description: Use swarm mode overlay networking features

## Raft consensus in swarm mode
URL: https://docs.docker.com/engine/swarm/raft/
Markdown: https://docs.docker.com/engine/swarm/raft.md
Description: Raft consensus algorithm in swarm mode

## Manage sensitive data with Docker secrets
URL: https://docs.docker.com/engine/swarm/secrets/
Markdown: https://docs.docker.com/engine/swarm/secrets.md
Description: How to securely store, retrieve, and use sensitive data with Docker services

## Deploy services to a swarm
URL: https://docs.docker.com/engine/swarm/services/
Markdown: https://docs.docker.com/engine/swarm/services.md
Description: Deploy services to a swarm

## Deploy a stack to a swarm
URL: https://docs.docker.com/engine/swarm/stack-deploy/
Markdown: https://docs.docker.com/engine/swarm/stack-deploy.md
Description: How to deploy a stack to a swarm

## Lock your swarm to protect its encryption key
URL: https://docs.docker.com/engine/swarm/swarm_manager_locking/
Markdown: https://docs.docker.com/engine/swarm/swarm_manager_locking.md
Description: Automatically lock Swarm managers to protect encryption keys

## Run Docker Engine in swarm mode
URL: https://docs.docker.com/engine/swarm/swarm-mode/
Markdown: https://docs.docker.com/engine/swarm/swarm-mode.md
Description: Run Docker Engine in swarm mode

## Add nodes to the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes.md
Description: Add nodes to the swarm

## Create a swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm.md
Description: Initialize the swarm

## Delete the service running on the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/delete-service/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/delete-service.md
Description: Remove the service from the swarm

## Deploy a service to the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service.md
Description: Deploy a service to the swarm

## Drain a node on the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/drain-node/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/drain-node.md
Description: Drain nodes on the swarm

## Inspect a service on the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service.md
Description: Inspect the application

## Apply rolling updates to a service
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update.md
Description: Apply rolling updates to a service on the swarm

## Scale the service in the swarm
URL: https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/
Markdown: https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service.md
Description: Scale the service running in the swarm

## Extension metadata
URL: https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/
Markdown: https://docs.docker.com/extensions/extensions-sdk/architecture/metadata.md
Description: Docker extension metadata

## Extension security
URL: https://docs.docker.com/extensions/extensions-sdk/architecture/security/
Markdown: https://docs.docker.com/extensions/extensions-sdk/architecture/security.md
Description: Aspects of the security model of extensions

## Add a backend to your extension
URL: https://docs.docker.com/extensions/extensions-sdk/build/backend-extension-tutorial/
Markdown: https://docs.docker.com/extensions/extensions-sdk/build/backend-extension-tutorial.md
Description: Learn how to add a backend to your extension.

## Create an advanced frontend extension
URL: https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial/
Markdown: https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial.md
Description: Advanced frontend extension tutorial

## Create a simple extension
URL: https://docs.docker.com/extensions/extensions-sdk/build/minimal-frontend-extension/
Markdown: https://docs.docker.com/extensions/extensions-sdk/build/minimal-frontend-extension.md
Description: Minimal frontend extension tutorial

## Design guidelines for Docker extensions
URL: https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/
Markdown: https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines.md
Description: Docker extension design

## Docker design principles
URL: https://docs.docker.com/extensions/extensions-sdk/design/design-principles/
Markdown: https://docs.docker.com/extensions/extensions-sdk/design/design-principles.md
Description: Docker extension design

## MUI best practices
URL: https://docs.docker.com/extensions/extensions-sdk/design/mui-best-practices/
Markdown: https://docs.docker.com/extensions/extensions-sdk/design/mui-best-practices.md
Description: Guidelines for using MUI to maximize compatibility with Docker Desktop

## Extension Backend
URL: https://docs.docker.com/extensions/extensions-sdk/dev/api/backend/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/api/backend.md
Description: Docker extension API

## Navigation
URL: https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard-routes-navigation/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard-routes-navigation.md
Description: Docker extension API

## Dashboard
URL: https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard.md
Description: Docker extension API

## Docker
URL: https://docs.docker.com/extensions/extensions-sdk/dev/api/docker/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/api/docker.md
Description: Docker extension API

## Extension UI API
URL: https://docs.docker.com/extensions/extensions-sdk/dev/api/overview/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/api/overview.md
Description: Docker extension development overview

## Continuous Integration (CI)
URL: https://docs.docker.com/extensions/extensions-sdk/dev/continuous-integration/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/continuous-integration.md
Description: Automatically test and validate your extension.

## Test and debug
URL: https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/test-debug.md
Description: Test and debug your extension.

## CLI reference
URL: https://docs.docker.com/extensions/extensions-sdk/dev/usage/
Markdown: https://docs.docker.com/extensions/extensions-sdk/dev/usage.md
Description: Docker extension CLI

## Package and release your extension
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/DISTRIBUTION/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/DISTRIBUTION.md
Description: Docker extension distribution

## Extension image labels
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/labels/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/labels.md
Description: Docker extension labels

## Build multi-arch extensions
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/multi-arch/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/multi-arch.md
Description: Step three in creating an extension.

## Publish in the Marketplace
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/publish/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/publish.md
Description: Docker extension distribution

## Share your extension
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/share/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/share.md
Description: Share your extension with a share link

## Validate your extension
URL: https://docs.docker.com/extensions/extensions-sdk/extensions/validate/
Markdown: https://docs.docker.com/extensions/extensions-sdk/extensions/validate.md
Description: Step three in the extension creation process

## Invoke host binaries
URL: https://docs.docker.com/extensions/extensions-sdk/guides/invoke-host-binaries/
Markdown: https://docs.docker.com/extensions/extensions-sdk/guides/invoke-host-binaries.md
Description: Add invocations to host binaries from the frontend with the extension SDK.

## Interacting with Kubernetes from an extension
URL: https://docs.docker.com/extensions/extensions-sdk/guides/kubernetes/
Markdown: https://docs.docker.com/extensions/extensions-sdk/guides/kubernetes.md
Description: How to connect to a Kubernetes cluster from an extension

## Authentication
URL: https://docs.docker.com/extensions/extensions-sdk/guides/oauth2-flow/
Markdown: https://docs.docker.com/extensions/extensions-sdk/guides/oauth2-flow.md
Description: Docker extension OAuth 2.0 flow

## Use the Docker socket from the extension backend
URL: https://docs.docker.com/extensions/extensions-sdk/guides/use-docker-socket-from-backend/
Markdown: https://docs.docker.com/extensions/extensions-sdk/guides/use-docker-socket-from-backend.md
Description: Docker extension metadata

## The build and publish process
URL: https://docs.docker.com/extensions/extensions-sdk/process/
Markdown: https://docs.docker.com/extensions/extensions-sdk/process.md
Description: Understand the process of creating an extension.

## Quickstart
URL: https://docs.docker.com/extensions/extensions-sdk/quickstart/
Markdown: https://docs.docker.com/extensions/extensions-sdk/quickstart.md
Description: Guide on how to build an extension quickly

## Marketplace extensions
URL: https://docs.docker.com/extensions/marketplace/
Markdown: https://docs.docker.com/extensions/marketplace.md
Description: Extensions

## Non-marketplace extensions
URL: https://docs.docker.com/extensions/non-marketplace/
Markdown: https://docs.docker.com/extensions/non-marketplace.md
Description: Extensions

## Configure a private marketplace for extensions
URL: https://docs.docker.com/extensions/private-marketplace/
Markdown: https://docs.docker.com/extensions/private-marketplace.md
Description: How to configure and use Docker Extensions' private marketplace

## Settings and feedback for Docker Extensions
URL: https://docs.docker.com/extensions/settings-feedback/
Markdown: https://docs.docker.com/extensions/settings-feedback.md
Description: Extensions

## Account FAQs
URL: https://docs.docker.com/faqs/accounts/
Markdown: https://docs.docker.com/faqs/accounts.md
Description: FAQs about Docker IDs, account creation, organizations, companies, seats, and members

## Platform FAQs
URL: https://docs.docker.com/faqs/platform/
Markdown: https://docs.docker.com/faqs/platform.md
Description: Frequently asked questions about Docker platform security, containers, networking, and VMs.

## Security FAQs
URL: https://docs.docker.com/faqs/security/
Markdown: https://docs.docker.com/faqs/security.md
Description: Frequently asked questions about Docker single sign-on, identity providers, user management, SSO enforcement, and domain verification

## Subscription and billing FAQs
URL: https://docs.docker.com/faqs/subscription-billing/
Markdown: https://docs.docker.com/faqs/subscription-billing.md
Description: Frequently asked questions about Docker subscriptions, billing, failed payments, taxes, and plans.

## Build, tag, and publish an image
URL: https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/
Markdown: https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image.md
Description: This concept page will teach you how to build, tag, and publish an image to Docker Hub or any other registry

## Multi-stage builds
URL: https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/
Markdown: https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds.md
Description: This concept page will teach you about the purpose of the multi-stage build and its benefits

## Understanding the image layers
URL: https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/
Markdown: https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers.md
Description: This concept page will teach you about the layers of container image.

## Using the build cache
URL: https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/
Markdown: https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache.md
Description: This concept page will teach you about the build cache, what changes invalidate the cache and how to effectively use the build cache.

## Writing a Dockerfile
URL: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
Markdown: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile.md
Description: This concept page will teach you how to create image using Dockerfile.

## Multi-container applications
URL: https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/
Markdown: https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications.md
Description: This concept page will teach you the significance of multi-container application and how it is different from single-container application

## Overriding container defaults
URL: https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults/
Markdown: https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults.md
Description: This concept page will teach you how to override the container defaults using the `docker run` command.

## Persisting container data
URL: https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/
Markdown: https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data.md
Description: This concept page will teach you the significance of data persistence in Docker

## Publishing and exposing ports
URL: https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/
Markdown: https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports.md
Description: This concept page will teach you the significance of publishing and exposing ports in Docker

## Sharing local files with containers
URL: https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/
Markdown: https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files.md
Description: This concept page will teach you the various storage options available in Docker and their common usage.

## What is a container?
URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
Markdown: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container.md
Description: What is a container? This concept page will teach you about containers and provide a quick hands-on where you will run your first container.

## What is a registry?
URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/
Markdown: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry.md
Description: What is a registry? This Docker Concept will explain what a registry is, explore their interoperability, and have you interact with registries.

## What is an image?
URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/
Markdown: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image.md
Description: What is an image

## What is Docker Compose?
URL: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/
Markdown: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose.md
Description: What is Docker Compose?

## What is Docker?
URL: https://docs.docker.com/get-started/docker-overview/
Markdown: https://docs.docker.com/get-started/docker-overview.md
Description: Get an in-depth overview of the Docker platform including what it can be used for, the architecture it employs, and its underlying technology.

## Get Docker
URL: https://docs.docker.com/get-started/get-docker/
Markdown: https://docs.docker.com/get-started/get-docker.md
Description: Download and install Docker on the platform of your choice, including Mac, Linux, or Windows.

## Educational resources
URL: https://docs.docker.com/get-started/resources/
Markdown: https://docs.docker.com/get-started/resources.md
Description: Get started resources learning docker

## Roll out Docker to a pilot group
URL: https://docs.docker.com/get-started/tutorials/admin-set-up/
Markdown: https://docs.docker.com/get-started/tutorials/admin-set-up.md
Description: Invite a pilot user, apply a Docker Desktop settings policy, and verify the managed experience before a wider deployment.

## Run your coding agent in a sandbox
URL: https://docs.docker.com/get-started/tutorials/run-an-agent/
Markdown: https://docs.docker.com/get-started/tutorials/run-an-agent.md
Description: Move your existing AI coding agent workflow into a disposable Docker Sandbox.

## Build and share a containerized application
URL: https://docs.docker.com/get-started/tutorials/run-an-app/
Markdown: https://docs.docker.com/get-started/tutorials/run-an-app.md
Description: Run a container and an application stack, build an image, and share it through Docker Hub.

## Set up your company for success with Docker
URL: https://docs.docker.com/guides/admin-set-up/
Markdown: https://docs.docker.com/guides/admin-set-up.md
Description: Learn how to onboard your company and take advantage of all of the Docker products and features.

## Mastering user and access management
URL: https://docs.docker.com/guides/admin-user-management/
Markdown: https://docs.docker.com/guides/admin-user-management.md
Description: A guide for managing roles, provisioning users, and optimizing Docker access with tools like SSO and activity logs.

## Build and run agentic AI applications with Docker
URL: https://docs.docker.com/guides/agentic-ai/
Markdown: https://docs.docker.com/guides/agentic-ai.md

## Angular language-specific guide
URL: https://docs.docker.com/guides/angular/
Markdown: https://docs.docker.com/guides/angular.md
Description: Containerize and develop Angular apps using Docker

## Introduction to Azure Pipelines with Docker
URL: https://docs.docker.com/guides/azure-pipelines/
Markdown: https://docs.docker.com/guides/azure-pipelines.md

## Mastering multi-platform builds, testing, and more with Docker Buildx Bake
URL: https://docs.docker.com/guides/bake/
Markdown: https://docs.docker.com/guides/bake.md
Description: Learn how to manage simple and complex build configurations with Buildx Bake.

## Bun language-specific guide
URL: https://docs.docker.com/guides/bun/
Markdown: https://docs.docker.com/guides/bun.md
Description: Containerize and develop Bun applications using Docker.

## Use Claude Code with Docker Model Runner
URL: https://docs.docker.com/guides/claude-code-model-runner/
Markdown: https://docs.docker.com/guides/claude-code-model-runner.md
Description: Configure Claude Code to use Docker Model Runner so you can code with local models.

## Run Claude Code in a Docker Sandbox with Docker Model Runner
URL: https://docs.docker.com/guides/claude-code-sandbox-model-runner/
Markdown: https://docs.docker.com/guides/claude-code-sandbox-model-runner.md
Description: Run Claude Code inside an isolated Docker Sandbox and route requests to Docker Model Runner so the agent uses local models on your host.

## Building Compose projects with Bake
URL: https://docs.docker.com/guides/compose-bake/
Markdown: https://docs.docker.com/guides/compose-bake.md
Description: Learn how to build Docker Compose projects with Docker Buildx Bake

## C++ language-specific guide
URL: https://docs.docker.com/guides/cpp/
Markdown: https://docs.docker.com/guides/cpp.md
Description: Containerize and develop C++ applications using Docker.

## Use containerized databases
URL: https://docs.docker.com/guides/databases/
Markdown: https://docs.docker.com/guides/databases.md
Description: Learn how to run, connect to, and persist data in a local containerized database.

## Deno language-specific guide
URL: https://docs.docker.com/guides/deno/
Markdown: https://docs.docker.com/guides/deno.md
Description: Containerize and develop Deno applications using Docker.

## Mocking OAuth services in testing with Dex
URL: https://docs.docker.com/guides/dex/
Markdown: https://docs.docker.com/guides/dex.md
Description: Mocking OAuth services in testing with Dex

## Secure a Backstage application with Docker Hardened Images
URL: https://docs.docker.com/guides/dhi-backstage/
Markdown: https://docs.docker.com/guides/dhi-backstage.md
Description: Secure a Backstage developer portal using Docker Hardened Images, covering native module compilation, Socket Firewall protection, and distroless runtime images.

## Use Docker Hardened Images with Red Hat OpenShift
URL: https://docs.docker.com/guides/dhi-openshift/
Markdown: https://docs.docker.com/guides/dhi-openshift.md
Description: Deploy Docker Hardened Images on Red Hat OpenShift Container Platform, covering Security Context Constraints, arbitrary user ID assignment, file permissions, and best practices.

## Explore VEX statements in Docker Hardened Images
URL: https://docs.docker.com/guides/dhi-vex-walkthrough/
Markdown: https://docs.docker.com/guides/dhi-vex-walkthrough.md
Description: Scan a Docker Hardened Image with and without VEX and audit every CVE suppression and its justification.

## Containerize a Django application
URL: https://docs.docker.com/guides/django/
Markdown: https://docs.docker.com/guides/django.md
Description: Learn how to containerize a Django application using Docker.

## .NET language-specific guide
URL: https://docs.docker.com/guides/dotnet/
Markdown: https://docs.docker.com/guides/dotnet.md
Description: Containerize and develop .NET apps using Docker

## Give sandboxed agents live web access with Firecrawl
URL: https://docs.docker.com/guides/firecrawl-sandbox-kit/
Markdown: https://docs.docker.com/guides/firecrawl-sandbox-kit.md
Description: Add the Firecrawl kit to a Docker Sandbox so the agent can search the web, scrape pages to Markdown, and crawl sites through the sandbox proxy, with your API key kept on the host.

## Generate Docker Compose Files with Claude Code and Docker MCP Toolkit
URL: https://docs.docker.com/guides/genai-claude-code-mcp/
Markdown: https://docs.docker.com/guides/genai-claude-code-mcp.md
Description: Learn how to use Claude Code with Docker MCP Toolkit to generate production-ready Docker Compose files from natural language using the Docker Hub MCP server.

## Introduction to GitHub Actions with Docker
URL: https://docs.docker.com/guides/gha/
Markdown: https://docs.docker.com/guides/gha.md

## Monitor a Golang application with Prometheus and Grafana
URL: https://docs.docker.com/guides/go-prometheus-monitoring/
Markdown: https://docs.docker.com/guides/go-prometheus-monitoring.md
Description: Containerize a Golang application and monitor it with Prometheus and Grafana.

## Go language-specific guide
URL: https://docs.docker.com/guides/golang/
Markdown: https://docs.docker.com/guides/golang.md
Description: Containerize Go apps using Docker

## Connect Gemini to Grafana via MCP
URL: https://docs.docker.com/guides/grafana-mcp-server-gemini/
Markdown: https://docs.docker.com/guides/grafana-mcp-server-gemini.md
Description: Integrate Gemini CLI with Grafana via Docker MCP Toolkit for natural language observability.

## Java language-specific guide
URL: https://docs.docker.com/guides/java/
Markdown: https://docs.docker.com/guides/java.md
Description: Containerize Java apps using Docker

## Data science with JupyterLab
URL: https://docs.docker.com/guides/jupyter/
Markdown: https://docs.docker.com/guides/jupyter.md
Description: Run, develop, and share data science projects using JupyterLab and Docker

## Developing event-driven applications with Kafka and Docker
URL: https://docs.docker.com/guides/kafka/
Markdown: https://docs.docker.com/guides/kafka.md
Description: Developing event-driven applications with Kafka and Docker

## Lab: Building Agentic Apps with Docker
URL: https://docs.docker.com/guides/lab-agentic-apps/
Markdown: https://docs.docker.com/guides/lab-agentic-apps.md
Description: Build agentic applications with Docker Model Runner, MCP Gateway, and Compose in this hands-on interactive lab.

## Lab: AI Fundamentals for Developers
URL: https://docs.docker.com/guides/lab-ai-fundamentals/
Markdown: https://docs.docker.com/guides/lab-ai-fundamentals.md
Description: Learn the core concepts of AI development — models, prompt engineering, tool calling, and RAG — through hands-on exercises in a live environment.

## Lab: Container Image Attestations
URL: https://docs.docker.com/guides/lab-attestation-basics/
Markdown: https://docs.docker.com/guides/lab-attestation-basics.md
Description: Learn to attach SBOMs, build provenance, image signatures, and VEX statements to container images for a verifiable software supply chain.

## Lab: Building Container Images
URL: https://docs.docker.com/guides/lab-building-images/
Markdown: https://docs.docker.com/guides/lab-building-images.md
Description: Learn to build production-grade container images using Dockerfile best practices — layer caching, multi-stage builds, non-root users, base image selection, and secure build-time secret handling.

## Lab: Docker Compose Quickstart
URL: https://docs.docker.com/guides/lab-compose-quickstart/
Markdown: https://docs.docker.com/guides/lab-compose-quickstart.md
Description: Build a multi-container Flask and Redis application from scratch using Docker Compose. Learn health checks, watch mode, named volumes, and multi-file configurations.

## Lab: Getting Started with Docker
URL: https://docs.docker.com/guides/lab-container-getting-started/
Markdown: https://docs.docker.com/guides/lab-container-getting-started.md
Description: Learn Docker fundamentals by running containers, exploring the container lifecycle, and packaging a real Node.js app into your own custom image.

## Lab: Container-Supported Development
URL: https://docs.docker.com/guides/lab-container-supported-development/
Markdown: https://docs.docker.com/guides/lab-container-supported-development.md
Description: Learn to use containers for local development by running a PostgreSQL database, defining a Compose file, and adding a pgAdmin dev tool — no local installations required.

## Lab: The Containerized SDLC
URL: https://docs.docker.com/guides/lab-containerized-sdlc/
Markdown: https://docs.docker.com/guides/lab-containerized-sdlc.md
Description: Build a Node.js API and containerize every stage of the software development lifecycle — local development, integration testing, CI/CD, and Kubernetes deployment.

## Lab: Building an AI Product Reviewer
URL: https://docs.docker.com/guides/lab-creating-ai-product-reviewer/
Markdown: https://docs.docker.com/guides/lab-creating-ai-product-reviewer.md
Description: Build a complete AI-powered feedback analysis pipeline — sentiment analysis, semantic clustering with embeddings, and response generation — all running locally via Docker Model Runner. No API keys required.

## Lab: Migrating a Node App to Docker Hardened Images
URL: https://docs.docker.com/guides/lab-dhi-node/
Markdown: https://docs.docker.com/guides/lab-dhi-node.md
Description: Migrate a Node.js application from a standard base image to Docker Hardened Images. Use Docker Scout to analyze CVEs, compare images, and inspect supply chain attestations.

## Lab: Getting Started with Docker Agent
URL: https://docs.docker.com/guides/lab-docker-agent/
Markdown: https://docs.docker.com/guides/lab-docker-agent.md
Description: Build intelligent multi-agent teams with Docker Agent and Docker in this hands-on interactive lab.

## Lab: Docker MCP Gateway
URL: https://docs.docker.com/guides/lab-mcp-gateway/
Markdown: https://docs.docker.com/guides/lab-mcp-gateway.md
Description: Run containerized MCP servers safely and securely with the Docker MCP Gateway in this hands-on interactive lab.

## Develop and Deploy Laravel applications with Docker Compose
URL: https://docs.docker.com/guides/laravel/
Markdown: https://docs.docker.com/guides/laravel.md
Description: A guide on using Docker Compose to manage Laravel applications for development and production, covering container configurations and service management.

## Develop and test AWS Cloud applications using LocalStack and Docker
URL: https://docs.docker.com/guides/localstack/
Markdown: https://docs.docker.com/guides/localstack.md
Description: How to develop and test AWS Cloud applications using LocalStack and Docker

## Run Mistral Vibe in a Docker Sandbox
URL: https://docs.docker.com/guides/mistral-vibe-sandbox/
Markdown: https://docs.docker.com/guides/mistral-vibe-sandbox.md
Description: Package Mistral's Vibe coding agent as a v3 Docker Sandbox kit with a pinned agent version and host-managed API credentials.

## Containerize a Next.js application
URL: https://docs.docker.com/guides/nextjs/
Markdown: https://docs.docker.com/guides/nextjs.md
Description: Containerize, develop, and test Next.js apps with Docker

## Node.js language-specific guide
URL: https://docs.docker.com/guides/nodejs/
Markdown: https://docs.docker.com/guides/nodejs.md
Description: Containerize and develop Node.js applications using Docker

## Use OpenCode with Docker Model Runner
URL: https://docs.docker.com/guides/opencode-model-runner/
Markdown: https://docs.docker.com/guides/opencode-model-runner.md
Description: Configure OpenCode to use Docker Model Runner so you can code with local models.

## Instrumenting a JavaScript App with OpenTelemetry
URL: https://docs.docker.com/guides/opentelemetry/
Markdown: https://docs.docker.com/guides/opentelemetry.md
Description: Learn how to instrument a JavaScript application using OpenTelemetry in a Dockerized environment.

## Visualizing your PostgreSQL databases with pgAdmin
URL: https://docs.docker.com/guides/pgadmin/
Markdown: https://docs.docker.com/guides/pgadmin.md
Description: Visualizing your PostgreSQL databases with pgAdmin

## PHP language-specific guide
URL: https://docs.docker.com/guides/php/
Markdown: https://docs.docker.com/guides/php.md
Description: Containerize and develop PHP apps using Docker

## PostgreSQL specific guide
URL: https://docs.docker.com/guides/postgresql/
Markdown: https://docs.docker.com/guides/postgresql.md
Description: Containerize PostgreSQL databases using Docker

## Pre-seeding database with schema and data at startup for development environment
URL: https://docs.docker.com/guides/pre-seeding/
Markdown: https://docs.docker.com/guides/pre-seeding.md
Description: Pre-seeding database with schema and data at startup for development environment

## Python language-specific guide
URL: https://docs.docker.com/guides/python/
Markdown: https://docs.docker.com/guides/python.md
Description: Containerize Python apps using Docker

## R language-specific guide
URL: https://docs.docker.com/guides/r/
Markdown: https://docs.docker.com/guides/r.md
Description: Containerize R apps using Docker

## React.js language-specific guide
URL: https://docs.docker.com/guides/reactjs/
Markdown: https://docs.docker.com/guides/reactjs.md
Description: Containerize and develop React.js apps using Docker

## Introduction to ROS 2 Development with Docker
URL: https://docs.docker.com/guides/ros2/
Markdown: https://docs.docker.com/guides/ros2.md
Description: Learn how to containerize and develop ROS 2 applications using Docker.

## Ruby on Rails language-specific guide
URL: https://docs.docker.com/guides/ruby/
Markdown: https://docs.docker.com/guides/ruby.md
Description: Containerize Ruby on Rails apps using Docker

## Rust language-specific guide
URL: https://docs.docker.com/guides/rust/
Markdown: https://docs.docker.com/guides/rust.md
Description: Containerize Rust apps using Docker

## Testing an ASP.NET Core web app with Testcontainers
URL: https://docs.docker.com/guides/testcontainers-dotnet-aspnet-core/
Markdown: https://docs.docker.com/guides/testcontainers-dotnet-aspnet-core.md
Description: Learn how to use Testcontainers for .NET to replace SQLite with a real Microsoft SQL Server in ASP.NET Core integration tests.

## Getting started with Testcontainers for .NET
URL: https://docs.docker.com/guides/testcontainers-dotnet-getting-started/
Markdown: https://docs.docker.com/guides/testcontainers-dotnet-getting-started.md
Description: Learn how to use Testcontainers for .NET to test database interactions with a real PostgreSQL instance.

## Getting started with Testcontainers for Go
URL: https://docs.docker.com/guides/testcontainers-go-getting-started/
Markdown: https://docs.docker.com/guides/testcontainers-go-getting-started.md
Description: Learn how to use Testcontainers for Go to test database interactions with a real PostgreSQL instance.

## Getting started with Testcontainers for Java
URL: https://docs.docker.com/guides/testcontainers-java-getting-started/
Markdown: https://docs.docker.com/guides/testcontainers-java-getting-started.md
Description: Learn how to use Testcontainers for Java to test a customer service with a real PostgreSQL database.

## Testcontainers container lifecycle management using JUnit 5
URL: https://docs.docker.com/guides/testcontainers-java-lifecycle/
Markdown: https://docs.docker.com/guides/testcontainers-java-lifecycle.md
Description: Learn how to manage Testcontainers container lifecycle using JUnit 5 callbacks, extension annotations, and the singleton containers pattern.

## Replace H2 with a real database for testing
URL: https://docs.docker.com/guides/testcontainers-java-replace-h2/
Markdown: https://docs.docker.com/guides/testcontainers-java-replace-h2.md
Description: Learn how to replace an H2 in-memory database with a real PostgreSQL database for testing using Testcontainers.

## Configuration of services running in a container
URL: https://docs.docker.com/guides/testcontainers-java-service-configuration/
Markdown: https://docs.docker.com/guides/testcontainers-java-service-configuration.md
Description: Learn how to configure services running in Testcontainers by copying files and executing commands inside containers.

## Testing a Spring Boot REST API with Testcontainers
URL: https://docs.docker.com/guides/testcontainers-java-spring-boot-rest-api/
Markdown: https://docs.docker.com/guides/testcontainers-java-spring-boot-rest-api.md
Description: Learn how to test a Spring Boot REST API using Testcontainers with PostgreSQL and REST Assured.

## Getting started with Testcontainers for Node.js
URL: https://docs.docker.com/guides/testcontainers-nodejs-getting-started/
Markdown: https://docs.docker.com/guides/testcontainers-nodejs-getting-started.md
Description: Learn how to use Testcontainers for Node.js to test database interactions with a real PostgreSQL instance.

## Getting started with Testcontainers for Python
URL: https://docs.docker.com/guides/testcontainers-python-getting-started/
Markdown: https://docs.docker.com/guides/testcontainers-python-getting-started.md
Description: Learn how to use Testcontainers for Python to test database interactions with a real PostgreSQL instance.

## HTTP routing with Traefik
URL: https://docs.docker.com/guides/traefik/
Markdown: https://docs.docker.com/guides/traefik.md
Description: Use Traefik to easily route traffic between multiple containers or non-containerized workloads

## Vue.js language-specific guide
URL: https://docs.docker.com/guides/vuejs/
Markdown: https://docs.docker.com/guides/vuejs.md
Description: Containerize and develop Vue.js apps using Docker

## Mocking API services in development and testing with WireMock
URL: https://docs.docker.com/guides/wiremock/
Markdown: https://docs.docker.com/guides/wiremock.md
Description: Mocking API services in development and testing with WireMock

## Using Docker with Zscaler
URL: https://docs.docker.com/guides/zscaler/
Markdown: https://docs.docker.com/guides/zscaler.md

## About Docker Offload
URL: https://docs.docker.com/offload/about/
Markdown: https://docs.docker.com/offload/about.md
Description: Learn about Docker Offload, its features, and how it works.

## Configure Docker Offload
URL: https://docs.docker.com/offload/configuration/
Markdown: https://docs.docker.com/offload/configuration.md
Description: Learn how to configure build settings for Docker Offload.

## Give feedback
URL: https://docs.docker.com/offload/feedback/
Markdown: https://docs.docker.com/offload/feedback.md
Description: Find a way to provide feedback that's right for you

## Optimize Docker Offload usage
URL: https://docs.docker.com/offload/optimize/
Markdown: https://docs.docker.com/offload/optimize.md
Description: Learn how to optimize your Docker Offload usage.

## Docker Offload quickstart
URL: https://docs.docker.com/offload/quickstart/
Markdown: https://docs.docker.com/offload/quickstart.md
Description: Learn how to use Docker Offload to build and run your container images in the cloud.

## Troubleshoot Docker Offload
URL: https://docs.docker.com/offload/troubleshoot/
Markdown: https://docs.docker.com/offload/troubleshoot.md
Description: Learn how to troubleshoot issues with Docker Offload.

## Docker Offload usage
URL: https://docs.docker.com/offload/usage/
Markdown: https://docs.docker.com/offload/usage.md
Description: Learn about Docker Offload usage and how to monitor your cloud resources.

## Accounts and admin release notes
URL: https://docs.docker.com/platform-release-notes/
Markdown: https://docs.docker.com/platform-release-notes.md
Description: Learn about new features, bug fixes, and breaking changes for Docker accounts and admin features, including Docker Home, billing, security, and subscriptions.

## Create policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/createPolicy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/createPolicy.md
Description: POST /orgs/{org_name}/governance/policies — AI Governance API 1.

## Create rule
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/createRule/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/createRule.md
Description: POST /orgs/{org_name}/governance/policies/{policy_id}/rules — AI Governance API 1.

## Delete policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/deletePolicy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/deletePolicy.md
Description: DELETE /orgs/{org_name}/governance/policies/{policy_id} — AI Governance API 1.

## Delete rule
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/deleteRule/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/deleteRule.md
Description: DELETE /orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id} — AI Governance API 1.

## Get policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/getPolicy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/getPolicy.md
Description: GET /orgs/{org_name}/governance/policies/{policy_id} — AI Governance API 1.

## List policies
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/listPolicies/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/listPolicies.md
Description: GET /orgs/{org_name}/governance/policies — AI Governance API 1.

## Update policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/updatePolicy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/updatePolicy.md
Description: PATCH /orgs/{org_name}/governance/policies/{policy_id} — AI Governance API 1.

## Update rule
URL: https://docs.docker.com/reference/api/ai-governance/latest/operations/updateRule/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/operations/updateRule.md
Description: PATCH /orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id} — AI Governance API 1.

## AllowlistV0
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/AllowlistV0/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/AllowlistV0.md
Description: AllowlistV0 schema in AI Governance API 1.

## CedarV1Policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CedarV1Policy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CedarV1Policy.md
Description: CedarV1Policy schema in AI Governance API 1.

## CreatePolicyRequest
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreatePolicyRequest/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreatePolicyRequest.md
Description: CreatePolicyRequest schema in AI Governance API 1.

## CreateRuleRequest
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreateRuleRequest/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreateRuleRequest.md
Description: CreateRuleRequest schema in AI Governance API 1.

## DeletePolicyResponse
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeletePolicyResponse/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeletePolicyResponse.md
Description: DeletePolicyResponse schema in AI Governance API 1.

## DeleteRuleResponse
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeleteRuleResponse/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeleteRuleResponse.md
Description: DeleteRuleResponse schema in AI Governance API 1.

## Error
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Error/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Error.md
Description: Error schema in AI Governance API 1.

## HTTPResource
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResource/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResource.md
Description: HTTPResource schema in AI Governance API 1.

## HTTPResources
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResources/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResources.md
Description: HTTPResources schema in AI Governance API 1.

## Policy
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Policy/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Policy.md
Description: Policy schema in AI Governance API 1.

## PolicySummary
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/PolicySummary/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/PolicySummary.md
Description: PolicySummary schema in AI Governance API 1.

## Rule
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Rule/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Rule.md
Description: Rule schema in AI Governance API 1.

## RuleActions
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleActions/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleActions.md
Description: RuleActions schema in AI Governance API 1.

## RuleDecision
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleDecision/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleDecision.md
Description: RuleDecision schema in AI Governance API 1.

## RuleResources
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleResources/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleResources.md
Description: RuleResources schema in AI Governance API 1.

## Scope
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Scope/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/Scope.md
Description: Scope schema in AI Governance API 1.

## ScopePatch
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/ScopePatch/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/ScopePatch.md
Description: ScopePatch schema in AI Governance API 1.

## UpdatePolicyRequest
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyRequest/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyRequest.md
Description: UpdatePolicyRequest schema in AI Governance API 1.

## UpdatePolicyResponse
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyResponse/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyResponse.md
Description: UpdatePolicyResponse schema in AI Governance API 1.

## UpdateRuleRequest
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleRequest/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleRequest.md
Description: UpdateRuleRequest schema in AI Governance API 1.

## UpdateRuleResponse
URL: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleResponse/
Markdown: https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleResponse.md
Description: UpdateRuleResponse schema in AI Governance API 1.

## Docker Verified Publisher API changelog
URL: https://docs.docker.com/reference/api/dvp/changelog/
Markdown: https://docs.docker.com/reference/api/dvp/changelog.md
Description: Docker Verified Publisher API changelog

## Deprecated Docker Verified Publisher API endpoints
URL: https://docs.docker.com/reference/api/dvp/deprecated/
Markdown: https://docs.docker.com/reference/api/dvp/deprecated.md
Description: Deprecated Docker Verified Publisher API endpoints

## Get pull data for multiple repos
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getManyReposPulls/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getManyReposPulls.md
Description: GET /repos/pulls — Publisher analytics API 1.0.0.

## Get namespace
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespace/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespace.md
Description: GET /namespaces/{namespace} — Publisher analytics API 1.0.0.

## Get namespace data for timespan
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceDataByTimespan/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceDataByTimespan.md
Description: GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview} — Publisher analytics API 1.0.0.

## Get pull data
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespacePulls/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespacePulls.md
Description: GET /namespaces/{namespace}/pulls — Publisher analytics API 1.0.0.

## Get namespaces and repos
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaces/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaces.md
Description: GET / — Publisher analytics API 1.0.0.

## Get namespace metadata for timespan
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceTimespanMetadata/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceTimespanMetadata.md
Description: GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan} — Publisher analytics API 1.0.0.

## Get timespans with data
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceTimespans/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceTimespans.md
Description: GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype} — Publisher analytics API 1.0.0.

## Get years with data
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceYears/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getNamespaceYears.md
Description: GET /namespaces/{namespace}/pulls/exports/years — Publisher analytics API 1.0.0.

## Get pull data
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getRepoPulls/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getRepoPulls.md
Description: GET /namespaces/{namespace}/repos/{repo}/pulls — Publisher analytics API 1.0.0.

## Get user's namespaces
URL: https://docs.docker.com/reference/api/dvp/latest/operations/getUserNamespaces/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/getUserNamespaces.md
Description: GET /namespaces — Publisher analytics API 1.0.0.

## Second factor authentication
URL: https://docs.docker.com/reference/api/dvp/latest/operations/PostUsers2FALogin/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/PostUsers2FALogin.md
Description: POST /v2/users/2fa-login — Publisher analytics API 1.0.0.

## Create an authentication token
URL: https://docs.docker.com/reference/api/dvp/latest/operations/PostUsersLogin/
Markdown: https://docs.docker.com/reference/api/dvp/latest/operations/PostUsersLogin.md
Description: POST /v2/users/login — Publisher analytics API 1.0.0.

## DatasetModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/DatasetModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/DatasetModel.md
Description: DatasetModel schema in Publisher analytics API 1.0.0.

## DatasetType
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/DatasetType/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/DatasetType.md
Description: DatasetType schema in Publisher analytics API 1.0.0.

## DataviewType
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/DataviewType/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/DataviewType.md
Description: DataviewType schema in Publisher analytics API 1.0.0.

## GroupType
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/GroupType/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/GroupType.md
Description: GroupType schema in Publisher analytics API 1.0.0.

## MonthData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/MonthData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/MonthData.md
Description: MonthData schema in Publisher analytics API 1.0.0.

## MonthModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/MonthModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/MonthModel.md
Description: MonthModel schema in Publisher analytics API 1.0.0.

## NamespaceData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/NamespaceData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/NamespaceData.md
Description: NamespaceData schema in Publisher analytics API 1.0.0.

## NamespaceMetadata
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/NamespaceMetadata/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/NamespaceMetadata.md
Description: NamespaceMetadata schema in Publisher analytics API 1.0.0.

## PeriodType
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PeriodType/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PeriodType.md
Description: PeriodType schema in Publisher analytics API 1.0.0.

## PostUsers2FALoginErrorResponse
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsers2FALoginErrorResponse/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsers2FALoginErrorResponse.md
Description: PostUsers2FALoginErrorResponse schema in Publisher analytics API 1.0.0.

## PostUsersLoginErrorResponse
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsersLoginErrorResponse/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsersLoginErrorResponse.md
Description: PostUsersLoginErrorResponse schema in Publisher analytics API 1.0.0.

## PostUsersLoginSuccessResponse
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsersLoginSuccessResponse/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PostUsersLoginSuccessResponse.md
Description: PostUsersLoginSuccessResponse schema in Publisher analytics API 1.0.0.

## PullData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PullData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PullData.md
Description: PullData schema in Publisher analytics API 1.0.0.

## PullModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/PullModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/PullModel.md
Description: PullModel schema in Publisher analytics API 1.0.0.

## ReposPullData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/ReposPullData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/ReposPullData.md
Description: ReposPullData schema in Publisher analytics API 1.0.0.

## ResponseData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/ResponseData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/ResponseData.md
Description: ResponseData schema in Publisher analytics API 1.0.0.

## ResponseDataFile
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/ResponseDataFile/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/ResponseDataFile.md
Description: ResponseDataFile schema in Publisher analytics API 1.0.0.

## TimespanData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanData.md
Description: TimespanData schema in Publisher analytics API 1.0.0.

## TimespanModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanModel.md
Description: TimespanModel schema in Publisher analytics API 1.0.0.

## TimespanType
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanType/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/TimespanType.md
Description: TimespanType schema in Publisher analytics API 1.0.0.

## Users2FALoginRequest
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/Users2FALoginRequest/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/Users2FALoginRequest.md
Description: Users2FALoginRequest schema in Publisher analytics API 1.0.0.

## UsersLoginRequest
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/UsersLoginRequest/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/UsersLoginRequest.md
Description: UsersLoginRequest schema in Publisher analytics API 1.0.0.

## WeekData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/WeekData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/WeekData.md
Description: WeekData schema in Publisher analytics API 1.0.0.

## WeekModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/WeekModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/WeekModel.md
Description: WeekModel schema in Publisher analytics API 1.0.0.

## YearData
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/YearData/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/YearData.md
Description: YearData schema in Publisher analytics API 1.0.0.

## YearModel
URL: https://docs.docker.com/reference/api/dvp/latest/schemas/YearModel/
Markdown: https://docs.docker.com/reference/api/dvp/latest/schemas/YearModel.md
Description: YearModel schema in Publisher analytics API 1.0.0.

## Examples using the Docker Engine SDKs and Docker API
URL: https://docs.docker.com/reference/api/engine/sdk/examples/
Markdown: https://docs.docker.com/reference/api/engine/sdk/examples.md
Description: Examples on how to perform a given Docker operation using the Go and Python SDKs and the HTTP API using curl.

## Engine API version history
URL: https://docs.docker.com/reference/api/engine/version-history/
Markdown: https://docs.docker.com/reference/api/engine/version-history.md
Description: Documentation of changes that have been made to Engine API.

## Docker Engine API v1.40 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.40/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.40.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.41 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.41/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.41.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.42 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.42/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.42.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.43 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.43/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.43.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.44 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.44/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.44.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.45 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.45/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.45.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.46 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.46/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.46.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.47 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.47/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.47.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.48 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.48/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.48.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.49 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.49/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.49.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.50 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.50/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.50.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.51 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.51/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.51.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.52 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.52/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.52.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.53 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.53/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.53.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.54 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.54/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.54.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.55 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.55/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.55.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Docker Engine API v1.56 reference
URL: https://docs.docker.com/reference/api/engine/version/v1.56/
Markdown: https://docs.docker.com/reference/api/engine/version/v1.56.md
Description: Reference documentation and Swagger (OpenAPI) specification for the Docker Engine API.

## Interface: BackendV0
URL: https://docs.docker.com/reference/api/extensions-sdk/BackendV0/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/BackendV0.md
Description: Docker extension API reference

## Interface: DesktopUI
URL: https://docs.docker.com/reference/api/extensions-sdk/DesktopUI/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/DesktopUI.md
Description: Docker extension API reference

## Interface: Dialog
URL: https://docs.docker.com/reference/api/extensions-sdk/Dialog/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Dialog.md
Description: Docker extension API reference

## Interface: Docker
URL: https://docs.docker.com/reference/api/extensions-sdk/Docker/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Docker.md
Description: Docker extension API reference

## Interface: DockerCommand
URL: https://docs.docker.com/reference/api/extensions-sdk/DockerCommand/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/DockerCommand.md
Description: Docker extension API reference

## Interface: DockerDesktopClient
URL: https://docs.docker.com/reference/api/extensions-sdk/DockerDesktopClient/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/DockerDesktopClient.md
Description: Docker extension API reference

## Interface: Exec
URL: https://docs.docker.com/reference/api/extensions-sdk/Exec/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Exec.md
Description: Docker extension API reference

## Interface: ExecOptions
URL: https://docs.docker.com/reference/api/extensions-sdk/ExecOptions/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExecOptions.md
Description: Docker extension API reference

## Interface: ExecProcess
URL: https://docs.docker.com/reference/api/extensions-sdk/ExecProcess/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExecProcess.md
Description: Docker extension API reference

## Interface: ExecResult
URL: https://docs.docker.com/reference/api/extensions-sdk/ExecResult/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExecResult.md
Description: Docker extension API reference

## Interface: ExecResultV0
URL: https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0.md
Description: Docker extension API reference

## Interface: ExecStreamOptions
URL: https://docs.docker.com/reference/api/extensions-sdk/ExecStreamOptions/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExecStreamOptions.md
Description: Docker extension API reference

## Interface: Extension
URL: https://docs.docker.com/reference/api/extensions-sdk/Extension/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Extension.md
Description: Docker extension API reference

## Interface: ExtensionCli
URL: https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli.md
Description: Docker extension API reference

## Interface: ExtensionHost
URL: https://docs.docker.com/reference/api/extensions-sdk/ExtensionHost/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExtensionHost.md
Description: Docker extension API reference

## Interface: ExtensionVM
URL: https://docs.docker.com/reference/api/extensions-sdk/ExtensionVM/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ExtensionVM.md
Description: Docker extension API reference

## Interface: Host
URL: https://docs.docker.com/reference/api/extensions-sdk/Host/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Host.md
Description: Docker extension API reference

## Interface: HttpService
URL: https://docs.docker.com/reference/api/extensions-sdk/HttpService/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/HttpService.md
Description: Docker extension API reference

## Interface: NavigationIntents
URL: https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents.md
Description: Docker extension API reference

## Interface: OpenDialogResult
URL: https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult.md
Description: Docker extension API reference

## Interface: RawExecResult
URL: https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/RawExecResult.md
Description: Docker extension API reference

## Interface: RequestConfig
URL: https://docs.docker.com/reference/api/extensions-sdk/RequestConfig/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/RequestConfig.md
Description: Docker extension API reference

## Interface: RequestConfigV0
URL: https://docs.docker.com/reference/api/extensions-sdk/RequestConfigV0/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/RequestConfigV0.md
Description: Docker extension API reference

## Interface: ServiceError
URL: https://docs.docker.com/reference/api/extensions-sdk/ServiceError/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/ServiceError.md
Description: Docker extension API reference

## Interface: SpawnOptions
URL: https://docs.docker.com/reference/api/extensions-sdk/SpawnOptions/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/SpawnOptions.md
Description: Docker extension API reference

## Interface: Toast
URL: https://docs.docker.com/reference/api/extensions-sdk/Toast/
Markdown: https://docs.docker.com/reference/api/extensions-sdk/Toast.md
Description: Docker extension API reference

## Docker Hub API changelog
URL: https://docs.docker.com/reference/api/hub/changelog/
Markdown: https://docs.docker.com/reference/api/hub/changelog.md
Description: Docker Hub API changelog

## Deprecated Docker Hub API endpoints
URL: https://docs.docker.com/reference/api/hub/deprecated/
Markdown: https://docs.docker.com/reference/api/hub/deprecated.md
Description: Deprecated Docker Hub API endpoints

## List audit log actions
URL: https://docs.docker.com/reference/api/hub/latest/operations/AuditLogs_ListAuditActions/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/AuditLogs_ListAuditActions.md
Description: GET /v2/auditlogs/{account}/actions — Docker Hub API 2-beta.

## List audit log events
URL: https://docs.docker.com/reference/api/hub/latest/operations/AuditLogs_ListAuditLogs/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/AuditLogs_ListAuditLogs.md
Description: GET /v2/auditlogs/{account} — Docker Hub API 2-beta.

## Create access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/AuthCreateAccessToken/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/AuthCreateAccessToken.md
Description: POST /v2/auth/token — Docker Hub API 2-beta.

## Check repository in a namespace
URL: https://docs.docker.com/reference/api/hub/latest/operations/CheckRepository/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/CheckRepository.md
Description: HEAD /v2/namespaces/{namespace}/repositories/{repository} — Docker Hub API 2-beta.

## Create a new repository
URL: https://docs.docker.com/reference/api/hub/latest/operations/CreateRepository/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/CreateRepository.md
Description: POST /v2/namespaces/{namespace}/repositories — Docker Hub API 2-beta.

## Assign a group (Team) to a repository for access
URL: https://docs.docker.com/reference/api/hub/latest/operations/CreateRepositoryGroup/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/CreateRepositoryGroup.md
Description: POST /v2/repositories/{namespace}/{repository}/groups — Docker Hub API 2-beta.

## Delete personal access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2AccessTokensByUuid/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2AccessTokensByUuid.md
Description: DELETE /v2/access-tokens/{uuid} — Docker Hub API 2-beta.

## Cancel an invite
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2InvitesById/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2InvitesById.md
Description: DELETE /v2/invites/{id} — Docker Hub API 2-beta.

## Delete access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameAccessTokensByAccessTokenId/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameAccessTokensByAccessTokenId.md
Description: DELETE /v2/orgs/{org_name}/access-tokens/{access_token_id} — Docker Hub API 2-beta.

## Delete an organization group
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupName/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupName.md
Description: DELETE /v2/orgs/{org_name}/groups/{group_name} — Docker Hub API 2-beta.

## Remove a user from a group
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupNameMembersByUsername/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupNameMembersByUsername.md
Description: DELETE /v2/orgs/{org_name}/groups/{group_name}/members/{username} — Docker Hub API 2-beta.

## Remove member from org
URL: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameMembersByUsername/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameMembersByUsername.md
Description: DELETE /v2/orgs/{org_name}/members/{username} — Docker Hub API 2-beta.

## Get repository in a namespace
URL: https://docs.docker.com/reference/api/hub/latest/operations/GetRepository/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/GetRepository.md
Description: GET /v2/namespaces/{namespace}/repositories/{repository} — Docker Hub API 2-beta.

## Read repository tag
URL: https://docs.docker.com/reference/api/hub/latest/operations/GetRepositoryTag/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/GetRepositoryTag.md
Description: GET /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} — Docker Hub API 2-beta.

## List personal access tokens
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2AccessTokens/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2AccessTokens.md
Description: GET /v2/access-tokens — Docker Hub API 2-beta.

## Get personal access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2AccessTokensByUuid/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2AccessTokensByUuid.md
Description: GET /v2/access-tokens/{uuid} — Docker Hub API 2-beta.

## List access tokens
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByNameAccessTokens/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByNameAccessTokens.md
Description: GET /v2/orgs/{name}/access-tokens — Docker Hub API 2-beta.

## Get organization settings
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByNameSettings/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByNameSettings.md
Description: GET /v2/orgs/{name}/settings — Docker Hub API 2-beta.

## Get access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameAccessTokensByAccessTokenId/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameAccessTokensByAccessTokenId.md
Description: GET /v2/orgs/{org_name}/access-tokens/{access_token_id} — Docker Hub API 2-beta.

## Get groups of an organization
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroups/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroups.md
Description: GET /v2/orgs/{org_name}/groups — Docker Hub API 2-beta.

## Get a group of an organization
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupName/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupName.md
Description: GET /v2/orgs/{org_name}/groups/{group_name} — Docker Hub API 2-beta.

## List members of a group
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupNameMembers/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupNameMembers.md
Description: GET /v2/orgs/{org_name}/groups/{group_name}/members — Docker Hub API 2-beta.

## List org invites
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameInvites/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameInvites.md
Description: GET /v2/orgs/{org_name}/invites — Docker Hub API 2-beta.

## List org members
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembers/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembers.md
Description: GET /v2/orgs/{org_name}/members — Docker Hub API 2-beta.

## Export org members CSV
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembersExport/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembersExport.md
Description: GET /v2/orgs/{org_name}/members/export — Docker Hub API 2-beta.

## List resource types
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ResourceTypes/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ResourceTypes.md
Description: GET /v2/scim/2.0/ResourceTypes — Docker Hub API 2-beta.

## Get a resource type
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ResourceTypesByName/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ResourceTypesByName.md
Description: GET /v2/scim/2.0/ResourceTypes/{name} — Docker Hub API 2-beta.

## List schemas
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20Schemas/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20Schemas.md
Description: GET /v2/scim/2.0/Schemas — Docker Hub API 2-beta.

## Get a schema
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20SchemasById/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20SchemasById.md
Description: GET /v2/scim/2.0/Schemas/{id} — Docker Hub API 2-beta.

## Get service provider config
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ServiceProviderConfig/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20ServiceProviderConfig.md
Description: GET /v2/scim/2.0/ServiceProviderConfig — Docker Hub API 2-beta.

## List users
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20Users/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20Users.md
Description: GET /v2/scim/2.0/Users — Docker Hub API 2-beta.

## Get a user
URL: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20UsersById/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/getV2Scim20UsersById.md
Description: GET /v2/scim/2.0/Users/{id} — Docker Hub API 2-beta.

## Check repository tags
URL: https://docs.docker.com/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTags/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTags.md
Description: HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags — Docker Hub API 2-beta.

## Check repository tag
URL: https://docs.docker.com/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTagsByTag/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTagsByTag.md
Description: HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} — Docker Hub API 2-beta.

## List repositories in a namespace
URL: https://docs.docker.com/reference/api/hub/latest/operations/listNamespaceRepositories/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/listNamespaceRepositories.md
Description: GET /v2/namespaces/{namespace}/repositories — Docker Hub API 2-beta.

## List repository tags
URL: https://docs.docker.com/reference/api/hub/latest/operations/ListRepositoryTags/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/ListRepositoryTags.md
Description: GET /v2/namespaces/{namespace}/repositories/{repository}/tags — Docker Hub API 2-beta.

## Update personal access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/patchV2AccessTokensByUuid/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/patchV2AccessTokensByUuid.md
Description: PATCH /v2/access-tokens/{uuid} — Docker Hub API 2-beta.

## Resend an invite
URL: https://docs.docker.com/reference/api/hub/latest/operations/patchV2InvitesByIdResend/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/patchV2InvitesByIdResend.md
Description: PATCH /v2/invites/{id}/resend — Docker Hub API 2-beta.

## Update access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/patchV2OrgsByOrgNameAccessTokensByAccessTokenId/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/patchV2OrgsByOrgNameAccessTokensByAccessTokenId.md
Description: PATCH /v2/orgs/{org_name}/access-tokens/{access_token_id} — Docker Hub API 2-beta.

## Update some details for an organization group
URL: https://docs.docker.com/reference/api/hub/latest/operations/patchV2OrgsByOrgNameGroupsByGroupName/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/patchV2OrgsByOrgNameGroupsByGroupName.md
Description: PATCH /v2/orgs/{org_name}/groups/{group_name} — Docker Hub API 2-beta.

## Second factor authentication
URL: https://docs.docker.com/reference/api/hub/latest/operations/PostUsers2FALogin/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/PostUsers2FALogin.md
Description: POST /v2/users/2fa-login — Docker Hub API 2-beta.

## Create an authentication token
URL: https://docs.docker.com/reference/api/hub/latest/operations/PostUsersLogin/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/PostUsersLogin.md
Description: POST /v2/users/login — Docker Hub API 2-beta.

## Create personal access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2AccessTokens/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2AccessTokens.md
Description: POST /v2/access-tokens — Docker Hub API 2-beta.

## Bulk create invites
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2InvitesBulk/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2InvitesBulk.md
Description: POST /v2/invites/bulk — Docker Hub API 2-beta.

## Create access token
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByNameAccessTokens/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByNameAccessTokens.md
Description: POST /v2/orgs/{name}/access-tokens — Docker Hub API 2-beta.

## Create a new group
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroups/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroups.md
Description: POST /v2/orgs/{org_name}/groups — Docker Hub API 2-beta.

## Add a member to a group
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroupsByGroupNameMembers/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroupsByGroupNameMembers.md
Description: POST /v2/orgs/{org_name}/groups/{group_name}/members — Docker Hub API 2-beta.

## Create user
URL: https://docs.docker.com/reference/api/hub/latest/operations/postV2Scim20Users/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/postV2Scim20Users.md
Description: POST /v2/scim/2.0/Users — Docker Hub API 2-beta.

## Update organization settings
URL: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByNameSettings/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByNameSettings.md
Description: PUT /v2/orgs/{name}/settings — Docker Hub API 2-beta.

## Update the details for an organization group
URL: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByOrgNameGroupsByGroupName/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByOrgNameGroupsByGroupName.md
Description: PUT /v2/orgs/{org_name}/groups/{group_name} — Docker Hub API 2-beta.

## Update org member (role)
URL: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByOrgNameMembersByUsername/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/putV2OrgsByOrgNameMembersByUsername.md
Description: PUT /v2/orgs/{org_name}/members/{username} — Docker Hub API 2-beta.

## Update a user
URL: https://docs.docker.com/reference/api/hub/latest/operations/putV2Scim20UsersById/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/putV2Scim20UsersById.md
Description: PUT /v2/scim/2.0/Users/{id} — Docker Hub API 2-beta.

## Update repository immutable tags
URL: https://docs.docker.com/reference/api/hub/latest/operations/UpdateRepositoryImmutableTags/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/UpdateRepositoryImmutableTags.md
Description: PATCH /v2/namespaces/{namespace}/repositories/{repository}/immutabletags — Docker Hub API 2-beta.

## Verify repository immutable tags
URL: https://docs.docker.com/reference/api/hub/latest/operations/VerifyRepositoryImmutableTags/
Markdown: https://docs.docker.com/reference/api/hub/latest/operations/VerifyRepositoryImmutableTags.md
Description: POST /v2/namespaces/{namespace}/repositories/{repository}/immutabletags/verify — Docker Hub API 2-beta.

## accessToken
URL: https://docs.docker.com/reference/api/hub/latest/schemas/accessToken/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/accessToken.md
Description: accessToken schema in Docker Hub API 2-beta.

## AuditLog
URL: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLog/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLog.md
Description: AuditLog schema in Docker Hub API 2-beta.

## AuditLogAction
URL: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLogAction/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLogAction.md
Description: AuditLogAction schema in Docker Hub API 2-beta.

## AuditLogActions
URL: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLogActions/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/AuditLogActions.md
Description: AuditLogActions schema in Docker Hub API 2-beta.

## AuthCreateTokenResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/AuthCreateTokenResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/AuthCreateTokenResponse.md
Description: AuthCreateTokenResponse schema in Docker Hub API 2-beta.

## bulk_invite
URL: https://docs.docker.com/reference/api/hub/latest/schemas/bulk_invite/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/bulk_invite.md
Description: bulk_invite schema in Docker Hub API 2-beta.

## category
URL: https://docs.docker.com/reference/api/hub/latest/schemas/category/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/category.md
Description: category schema in Docker Hub API 2-beta.

## createAccessTokenRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/createAccessTokenRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/createAccessTokenRequest.md
Description: createAccessTokenRequest schema in Docker Hub API 2-beta.

## createAccessTokensResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/createAccessTokensResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/createAccessTokensResponse.md
Description: createAccessTokensResponse schema in Docker Hub API 2-beta.

## createOrgAccessTokenRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/createOrgAccessTokenRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/createOrgAccessTokenRequest.md
Description: createOrgAccessTokenRequest schema in Docker Hub API 2-beta.

## createOrgAccessTokenResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/createOrgAccessTokenResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/createOrgAccessTokenResponse.md
Description: createOrgAccessTokenResponse schema in Docker Hub API 2-beta.

## email_address
URL: https://docs.docker.com/reference/api/hub/latest/schemas/email_address/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/email_address.md
Description: email_address schema in Docker Hub API 2-beta.

## email_with_username
URL: https://docs.docker.com/reference/api/hub/latest/schemas/email_with_username/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/email_with_username.md
Description: email_with_username schema in Docker Hub API 2-beta.

## error
URL: https://docs.docker.com/reference/api/hub/latest/schemas/error/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/error.md
Description: error schema in Docker Hub API 2-beta.

## getAccessTokensResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/getAccessTokensResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/getAccessTokensResponse.md
Description: getAccessTokensResponse schema in Docker Hub API 2-beta.

## GetAuditActionsResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/GetAuditActionsResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/GetAuditActionsResponse.md
Description: GetAuditActionsResponse schema in Docker Hub API 2-beta.

## GetAuditLogsResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/GetAuditLogsResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/GetAuditLogsResponse.md
Description: GetAuditLogsResponse schema in Docker Hub API 2-beta.

## getOrgAccessTokenResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/getOrgAccessTokenResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/getOrgAccessTokenResponse.md
Description: getOrgAccessTokenResponse schema in Docker Hub API 2-beta.

## getOrgAccessTokensResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/getOrgAccessTokensResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/getOrgAccessTokensResponse.md
Description: getOrgAccessTokensResponse schema in Docker Hub API 2-beta.

## group_member
URL: https://docs.docker.com/reference/api/hub/latest/schemas/group_member/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/group_member.md
Description: group_member schema in Docker Hub API 2-beta.

## image
URL: https://docs.docker.com/reference/api/hub/latest/schemas/image/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/image.md
Description: image schema in Docker Hub API 2-beta.

## immutable_tags_settings
URL: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_settings/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_settings.md
Description: immutable_tags_settings schema in Docker Hub API 2-beta.

## immutable_tags_verify_request
URL: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_verify_request/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_verify_request.md
Description: immutable_tags_verify_request schema in Docker Hub API 2-beta.

## immutable_tags_verify_response
URL: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_verify_response/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/immutable_tags_verify_response.md
Description: immutable_tags_verify_response schema in Docker Hub API 2-beta.

## invite
URL: https://docs.docker.com/reference/api/hub/latest/schemas/invite/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/invite.md
Description: invite schema in Docker Hub API 2-beta.

## layer
URL: https://docs.docker.com/reference/api/hub/latest/schemas/layer/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/layer.md
Description: layer schema in Docker Hub API 2-beta.

## legacy_email_address
URL: https://docs.docker.com/reference/api/hub/latest/schemas/legacy_email_address/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/legacy_email_address.md
Description: legacy_email_address schema in Docker Hub API 2-beta.

## list_repositories_response
URL: https://docs.docker.com/reference/api/hub/latest/schemas/list_repositories_response/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/list_repositories_response.md
Description: list_repositories_response schema in Docker Hub API 2-beta.

## org_group
URL: https://docs.docker.com/reference/api/hub/latest/schemas/org_group/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/org_group.md
Description: org_group schema in Docker Hub API 2-beta.

## org_member_paginated
URL: https://docs.docker.com/reference/api/hub/latest/schemas/org_member_paginated/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/org_member_paginated.md
Description: org_member_paginated schema in Docker Hub API 2-beta.

## org_member
URL: https://docs.docker.com/reference/api/hub/latest/schemas/org_member/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/org_member.md
Description: org_member schema in Docker Hub API 2-beta.

## orgAccessToken
URL: https://docs.docker.com/reference/api/hub/latest/schemas/orgAccessToken/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/orgAccessToken.md
Description: orgAccessToken schema in Docker Hub API 2-beta.

## orgAccessTokenResource
URL: https://docs.docker.com/reference/api/hub/latest/schemas/orgAccessTokenResource/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/orgAccessTokenResource.md
Description: orgAccessTokenResource schema in Docker Hub API 2-beta.

## orgSettings
URL: https://docs.docker.com/reference/api/hub/latest/schemas/orgSettings/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/orgSettings.md
Description: orgSettings schema in Docker Hub API 2-beta.

## page
URL: https://docs.docker.com/reference/api/hub/latest/schemas/page/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/page.md
Description: page schema in Docker Hub API 2-beta.

## paginated_tags
URL: https://docs.docker.com/reference/api/hub/latest/schemas/paginated_tags/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/paginated_tags.md
Description: paginated_tags schema in Docker Hub API 2-beta.

## patchAccessTokenRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/patchAccessTokenRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/patchAccessTokenRequest.md
Description: patchAccessTokenRequest schema in Docker Hub API 2-beta.

## patchAccessTokenResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/patchAccessTokenResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/patchAccessTokenResponse.md
Description: patchAccessTokenResponse schema in Docker Hub API 2-beta.

## PostUsers2FALoginErrorResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsers2FALoginErrorResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsers2FALoginErrorResponse.md
Description: PostUsers2FALoginErrorResponse schema in Docker Hub API 2-beta.

## PostUsersLoginErrorResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsersLoginErrorResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsersLoginErrorResponse.md
Description: PostUsersLoginErrorResponse schema in Docker Hub API 2-beta.

## PostUsersLoginSuccessResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsersLoginSuccessResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/PostUsersLoginSuccessResponse.md
Description: PostUsersLoginSuccessResponse schema in Docker Hub API 2-beta.

## repo_creation_request
URL: https://docs.docker.com/reference/api/hub/latest/schemas/repo_creation_request/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/repo_creation_request.md
Description: repo_creation_request schema in Docker Hub API 2-beta.

## repo_permissions
URL: https://docs.docker.com/reference/api/hub/latest/schemas/repo_permissions/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/repo_permissions.md
Description: repo_permissions schema in Docker Hub API 2-beta.

## repository_info
URL: https://docs.docker.com/reference/api/hub/latest/schemas/repository_info/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/repository_info.md
Description: repository_info schema in Docker Hub API 2-beta.

## repository_list_entry
URL: https://docs.docker.com/reference/api/hub/latest/schemas/repository_list_entry/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/repository_list_entry.md
Description: repository_list_entry schema in Docker Hub API 2-beta.

## RepositoryGroup
URL: https://docs.docker.com/reference/api/hub/latest/schemas/RepositoryGroup/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/RepositoryGroup.md
Description: RepositoryGroup schema in Docker Hub API 2-beta.

## RepositoryGroupCreationRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/RepositoryGroupCreationRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/RepositoryGroupCreationRequest.md
Description: RepositoryGroupCreationRequest schema in Docker Hub API 2-beta.

## restricted_images
URL: https://docs.docker.com/reference/api/hub/latest/schemas/restricted_images/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/restricted_images.md
Description: restricted_images schema in Docker Hub API 2-beta.

## scim_email
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_email/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_email.md
Description: scim_email schema in Docker Hub API 2-beta.

## scim_error
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_error/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_error.md
Description: scim_error schema in Docker Hub API 2-beta.

## scim_group
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_group/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_group.md
Description: scim_group schema in Docker Hub API 2-beta.

## scim_resource_type
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_resource_type/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_resource_type.md
Description: scim_resource_type schema in Docker Hub API 2-beta.

## scim_schema_attribute
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema_attribute/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema_attribute.md
Description: scim_schema_attribute schema in Docker Hub API 2-beta.

## scim_schema_parent_attribute
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema_parent_attribute/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema_parent_attribute.md
Description: scim_schema_parent_attribute schema in Docker Hub API 2-beta.

## scim_schema
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_schema.md
Description: scim_schema schema in Docker Hub API 2-beta.

## scim_service_provider_config
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_service_provider_config/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_service_provider_config.md
Description: scim_service_provider_config schema in Docker Hub API 2-beta.

## scim_user_display_name
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_display_name/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_display_name.md
Description: scim_user_display_name schema in Docker Hub API 2-beta.

## scim_user_id
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_id/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_id.md
Description: scim_user_id schema in Docker Hub API 2-beta.

## scim_user_name
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_name/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_name.md
Description: scim_user_name schema in Docker Hub API 2-beta.

## scim_user_schemas
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_schemas/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_schemas.md
Description: scim_user_schemas schema in Docker Hub API 2-beta.

## scim_user_username
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_username/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user_username.md
Description: scim_user_username schema in Docker Hub API 2-beta.

## scim_user
URL: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/scim_user.md
Description: scim_user schema in Docker Hub API 2-beta.

## tag
URL: https://docs.docker.com/reference/api/hub/latest/schemas/tag/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/tag.md
Description: tag schema in Docker Hub API 2-beta.

## update_repository_immutable_tags_request
URL: https://docs.docker.com/reference/api/hub/latest/schemas/update_repository_immutable_tags_request/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/update_repository_immutable_tags_request.md
Description: update_repository_immutable_tags_request schema in Docker Hub API 2-beta.

## updateOrgAccessTokenRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/updateOrgAccessTokenRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/updateOrgAccessTokenRequest.md
Description: updateOrgAccessTokenRequest schema in Docker Hub API 2-beta.

## updateOrgAccessTokenResponse
URL: https://docs.docker.com/reference/api/hub/latest/schemas/updateOrgAccessTokenResponse/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/updateOrgAccessTokenResponse.md
Description: updateOrgAccessTokenResponse schema in Docker Hub API 2-beta.

## user
URL: https://docs.docker.com/reference/api/hub/latest/schemas/user/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/user.md
Description: user schema in Docker Hub API 2-beta.

## Users2FALoginRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/Users2FALoginRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/Users2FALoginRequest.md
Description: Users2FALoginRequest schema in Docker Hub API 2-beta.

## UsersLoginRequest
URL: https://docs.docker.com/reference/api/hub/latest/schemas/UsersLoginRequest/
Markdown: https://docs.docker.com/reference/api/hub/latest/schemas/UsersLoginRequest.md
Description: UsersLoginRequest schema in Docker Hub API 2-beta.

## Registry authentication
URL: https://docs.docker.com/reference/api/registry/auth/
Markdown: https://docs.docker.com/reference/api/registry/auth.md
Description: Specifies the Docker Registry v2 authentication

## Cancel blob upload
URL: https://docs.docker.com/reference/api/registry/latest/operations/CancelBlobUpload/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/CancelBlobUpload.md
Description: DELETE /v2/{name}/blobs/uploads/{uuid} — Registry API 2.

## Check existence of blob
URL: https://docs.docker.com/reference/api/registry/latest/operations/CheckBlobExists/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/CheckBlobExists.md
Description: HEAD /v2/{name}/blobs/{digest} — Registry API 2.

## Complete blob upload
URL: https://docs.docker.com/reference/api/registry/latest/operations/CompleteBlobUpload/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/CompleteBlobUpload.md
Description: PUT /v2/{name}/blobs/uploads/{uuid} — Registry API 2.

## Delete image manifest
URL: https://docs.docker.com/reference/api/registry/latest/operations/DeleteImageManifest/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/DeleteImageManifest.md
Description: DELETE /v2/{name}/manifests/{reference} — Registry API 2.

## Retrieve blob
URL: https://docs.docker.com/reference/api/registry/latest/operations/GetBlob/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/GetBlob.md
Description: GET /v2/{name}/blobs/{digest} — Registry API 2.

## Get blob upload status
URL: https://docs.docker.com/reference/api/registry/latest/operations/GetBlobUploadStatus/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/GetBlobUploadStatus.md
Description: GET /v2/{name}/blobs/uploads/{uuid} — Registry API 2.

## Get image manifest
URL: https://docs.docker.com/reference/api/registry/latest/operations/GetImageManifest/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/GetImageManifest.md
Description: GET /v2/{name}/manifests/{reference} — Registry API 2.

## Check if manifest exists
URL: https://docs.docker.com/reference/api/registry/latest/operations/HeadImageManifest/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/HeadImageManifest.md
Description: HEAD /v2/{name}/manifests/{reference} — Registry API 2.

## Initiate blob upload or attempt cross-repository blob mount
URL: https://docs.docker.com/reference/api/registry/latest/operations/InitiateBlobUpload/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/InitiateBlobUpload.md
Description: POST /v2/{name}/blobs/uploads/ — Registry API 2.

## Put image manifest
URL: https://docs.docker.com/reference/api/registry/latest/operations/PutImageManifest/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/PutImageManifest.md
Description: PUT /v2/{name}/manifests/{reference} — Registry API 2.

## Upload blob chunk
URL: https://docs.docker.com/reference/api/registry/latest/operations/UploadBlobChunk/
Markdown: https://docs.docker.com/reference/api/registry/latest/operations/UploadBlobChunk.md
Description: PATCH /v2/{name}/blobs/uploads/{uuid} — Registry API 2.

## AddMcpGatewayServer adds one server to an existing ready gateway.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/addMcpGatewayServer/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/addMcpGatewayServer.md
Description: POST /v1/sandboxes/{sandbox}/mcp-gateway/servers — Docker Sandboxes API v1.

## AuthorizeMcpServer authorizes credentials for one named upstream.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/authorizeMcpServer/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/authorizeMcpServer.md
Description: POST /v1/mcp-servers/{mcpServer}/authorization/authorize — Docker Sandboxes API v1.

## CreateEndpointCredential grants short-lived access to one sandbox endpoint.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createEndpointCredential/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createEndpointCredential.md
Description: POST /v1/sandboxes/{sandbox}/endpoint-credentials — Docker Sandboxes API v1.

## CreateImage registers pushed OCI content or disk content derived from a snapshot or sandbox.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createImage/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createImage.md
Description: POST /v1/images — Docker Sandboxes API v1.

## CreatePort makes one sandbox port reachable outside the sandbox.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createPort/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createPort.md
Description: POST /v1/sandboxes/{sandbox}/ports — Docker Sandboxes API v1.

## CreateProcess starts a durable interactive process and returns its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createProcess/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createProcess.md
Description: POST /v1/processes — Docker Sandboxes API v1.

## CreateSandbox admits a sandbox.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSandbox.md
Description: POST /v1/sandboxes — Docker Sandboxes API v1.

## CreateSecret stores new secret material.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSecret/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSecret.md
Description: POST /v1/secrets — Docker Sandboxes API v1.

## CreateSnapshot checkpoints a running sandbox; a stopped source is rejected.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSnapshot/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createSnapshot.md
Description: POST /v1/sandboxes/{sandbox}/snapshots — Docker Sandboxes API v1.

## CreateVolume creates a persistent volume.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/createVolume/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/createVolume.md
Description: POST /v1/volumes — Docker Sandboxes API v1.

## DeleteImage deletes an image; deleting an already absent image succeeds.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteImage/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteImage.md
Description: DELETE /v1/images/{image} — Docker Sandboxes API v1.

## DeletePort withdraws one published port.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deletePort/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deletePort.md
Description: DELETE /v1/sandboxes/{sandbox}/ports/{port} — Docker Sandboxes API v1.

## DeleteSandbox returns the deleting resource while work remains, or an empty message when absent.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSandbox.md
Description: DELETE /v1/sandboxes/{sandbox} — Docker Sandboxes API v1.

## DeleteSecret deletes a secret; deleting an already absent secret succeeds.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSecret/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSecret.md
Description: DELETE /v1/secrets/{secret} — Docker Sandboxes API v1.

## DeleteSnapshot deletes a snapshot; deleting an already absent snapshot succeeds.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSnapshot/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteSnapshot.md
Description: DELETE /v1/snapshots/{snapshot} — Docker Sandboxes API v1.

## DeleteVolume deletes a volume; deleting an already absent volume succeeds.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteVolume/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/deleteVolume.md
Description: DELETE /v1/volumes/{volume} — Docker Sandboxes API v1.

## Download streams file headers, bytes, and per-file errors.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/download/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/download.md
Description: GET /v1/files/download — Docker Sandboxes API v1.

## ExchangeDockerCredential consumes an identity token once for the authenticated owner.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/exchangeDockerCredential/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/exchangeDockerCredential.md
Description: POST /v1/identity/exchange — Docker Sandboxes API v1.

## Exec runs one command to completion.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/exec/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/exec.md
Description: POST /v1/processes/exec — Docker Sandboxes API v1.

## GetImage reads one image by its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getImage/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getImage.md
Description: GET /v1/images/{image} — Docker Sandboxes API v1.

## GetImagePullSpec returns short-lived pull material through registry-transfer support.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getImagePullSpec/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getImagePullSpec.md
Description: GET /v1/images/{image}/pull-spec — Docker Sandboxes API v1.

## GetMcpAuthorization reads the owner-scoped flow, including its pending URL, under mcp.write.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getMcpAuthorization/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getMcpAuthorization.md
Description: GET /v1/mcp-servers/{mcpServer}/authorization — Docker Sandboxes API v1.

## GetMcpGateway reads gateway state for the sandbox.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getMcpGateway/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getMcpGateway.md
Description: GET /v1/sandboxes/{sandbox}/mcp-gateway — Docker Sandboxes API v1.

## GetNetworkPolicies returns effective and exact views of the same installed generation.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getNetworkPolicies/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getNetworkPolicies.md
Description: GET /v1/sandboxes/{sandbox}/network-policies — Docker Sandboxes API v1.

## GetNetworkPolicies returns effective and exact views of the same installed generation.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getNetworkPoliciesInOwnerScope/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getNetworkPoliciesInOwnerScope.md
Description: GET /v1/network-policies — Docker Sandboxes API v1.

## GetPort reads one published port by its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getPort/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getPort.md
Description: GET /v1/sandboxes/{sandbox}/ports/{port} — Docker Sandboxes API v1.

## GetProcess reads one process by its endpoint-scoped resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getProcess/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getProcess.md
Description: GET /v1/processes/{process} — Docker Sandboxes API v1.

## GetSandbox reads one sandbox by its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSandbox.md
Description: GET /v1/sandboxes/{sandbox} — Docker Sandboxes API v1.

## GetSecret reads one secret's metadata; material is never returned.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSecret/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSecret.md
Description: GET /v1/secrets/{secret} — Docker Sandboxes API v1.

## GetSnapshot reads one snapshot by its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSnapshot/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getSnapshot.md
Description: GET /v1/snapshots/{snapshot} — Docker Sandboxes API v1.

## GetVolume reads one volume by its resource name.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/getVolume/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/getVolume.md
Description: GET /v1/volumes/{volume} — Docker Sandboxes API v1.

## Interact binds the complete process name from the path to the first Attach frame.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/interact/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/interact.md
Description: GET /v1/processes/{process}/interact — Docker Sandboxes API v1.

## IssueSSHCert signs a caller-held public key for sandbox SSH access.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/issueSSHCert/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/issueSSHCert.md
Description: POST /v1/sandboxes/{sandbox}/ssh-certificates — Docker Sandboxes API v1.

## List lists directory entries by path ascending.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/list/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/list.md
Description: GET /v1/files — Docker Sandboxes API v1.

## ListImages lists images in the caller's owner scope.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listImages/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listImages.md
Description: GET /v1/images — Docker Sandboxes API v1.

## ListPolicyLogEntries lists observed policy decisions.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPolicyLogEntries/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPolicyLogEntries.md
Description: GET /v1/sandboxes/{sandbox}/policy-logs — Docker Sandboxes API v1.

## ListPolicyLogEntries lists observed policy decisions.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPolicyLogEntriesInOwnerScope/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPolicyLogEntriesInOwnerScope.md
Description: GET /v1/policy-logs — Docker Sandboxes API v1.

## ListPorts lists currently published ports for one sandbox.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPorts/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listPorts.md
Description: GET /v1/sandboxes/{sandbox}/ports — Docker Sandboxes API v1.

## ListProcesses lists processes in creation order.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listProcesses/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listProcesses.md
Description: GET /v1/processes — Docker Sandboxes API v1.

## ListSandboxes lists sandboxes in the caller's owner scope.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSandboxes/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSandboxes.md
Description: GET /v1/sandboxes — Docker Sandboxes API v1.

## ListSecrets lists secret metadata in the caller's owner scope.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSecrets/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSecrets.md
Description: GET /v1/secrets — Docker Sandboxes API v1.

## ListSnapshots lists snapshots in the caller's owner scope.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSnapshots/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listSnapshots.md
Description: GET /v1/snapshots — Docker Sandboxes API v1.

## ListVolumes lists volumes in the caller's owner scope.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/listVolumes/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/listVolumes.md
Description: GET /v1/volumes — Docker Sandboxes API v1.

## Mkdir creates a directory.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/mkdir/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/mkdir.md
Description: PUT /v1/files/directories — Docker Sandboxes API v1.

## Move renames or moves a path.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/move/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/move.md
Description: POST /v1/files/move — Docker Sandboxes API v1.

## ReadFile returns raw file content over HTTP; Stat exposes file metadata.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/readFile/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/readFile.md
Description: GET /v1/files/content — Docker Sandboxes API v1.

## ReadOutput returns one page of retained output after a stream_sequence, the same cursor Interact resumes from, so a REST client can read what a process printed.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/readOutput/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/readOutput.md
Description: GET /v1/processes/{process}/output — Docker Sandboxes API v1.

## Remove deletes a path.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/remove/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/remove.md
Description: DELETE /v1/files — Docker Sandboxes API v1.

## RenewSandboxTimeout sets a TTL when timeout renewal is supported.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/renewSandboxTimeout/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/renewSandboxTimeout.md
Description: POST /v1/sandboxes/{sandbox}/renew-timeout — Docker Sandboxes API v1.

## RestoreSnapshot forks a new sandbox from a snapshot.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/restoreSnapshot/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/restoreSnapshot.md
Description: POST /v1/snapshots/{snapshot}/restore — Docker Sandboxes API v1.

## Signal sends one signal to an existing process.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/signal/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/signal.md
Description: POST /v1/processes/{process}/signal — Docker Sandboxes API v1.

## StartSandbox starts a stopped sandbox; a backend that preserved memory resumes it.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/startSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/startSandbox.md
Description: POST /v1/sandboxes/{sandbox}/start — Docker Sandboxes API v1.

## Stat reads metadata for one path.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/stat/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/stat.md
Description: GET /v1/files/stat — Docker Sandboxes API v1.

## StopSandbox stops a running sandbox; a backend advertising memory preservation hibernates it.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/stopSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/stopSandbox.md
Description: POST /v1/sandboxes/{sandbox}/stop — Docker Sandboxes API v1.

## UpdateSandbox changes only the display label under the observed etag.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/updateSandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/updateSandbox.md
Description: PATCH /v1/sandboxes/{sandbox} — Docker Sandboxes API v1.

## UpdateSecret replaces secret metadata and material.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/updateSecret/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/updateSecret.md
Description: PUT /v1/secrets/{secret} — Docker Sandboxes API v1.

## Upload streams one or more files.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/upload/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/upload.md
Description: POST /v1/files/upload — Docker Sandboxes API v1.

## WriteFile accepts raw content with path and mode query parameters.
URL: https://docs.docker.com/reference/api/sandboxes/latest/operations/writeFile/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/operations/writeFile.md
Description: PUT /v1/files/content — Docker Sandboxes API v1.

## AddMcpGatewayServerResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AddMcpGatewayServerResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AddMcpGatewayServerResponse.md
Description: AddMcpGatewayServerResponse schema in Docker Sandboxes API v1.

## AppliedKit
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AppliedKit/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AppliedKit.md
Description: AppliedKit schema in Docker Sandboxes API v1.

## AttachmentMode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AttachmentMode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AttachmentMode.md
Description: AttachmentMode schema in Docker Sandboxes API v1.

## AttributedRule
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AttributedRule/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/AttributedRule.md
Description: AttributedRule schema in Docker Sandboxes API v1.

## BadRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequest.md
Description: BadRequest schema in Docker Sandboxes API v1.

## BadRequestErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequestErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequestErrorDetail.md
Description: BadRequestErrorDetail schema in Docker Sandboxes API v1.

## BadRequestFieldViolation
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequestFieldViolation/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/BadRequestFieldViolation.md
Description: BadRequestFieldViolation schema in Docker Sandboxes API v1.

## CaptureMode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CaptureMode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CaptureMode.md
Description: CaptureMode schema in Docker Sandboxes API v1.

## CreateImageRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateImageRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateImageRequest.md
Description: CreateImageRequest schema in Docker Sandboxes API v1.

## CreatePortRequestPortInput
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreatePortRequestPortInput/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreatePortRequestPortInput.md
Description: CreatePortRequestPortInput schema in Docker Sandboxes API v1.

## CreateProcessRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateProcessRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateProcessRequest.md
Description: CreateProcessRequest schema in Docker Sandboxes API v1.

## CreateSandboxRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateSandboxRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateSandboxRequest.md
Description: CreateSandboxRequest schema in Docker Sandboxes API v1.

## CreateSecretRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateSecretRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateSecretRequest.md
Description: CreateSecretRequest schema in Docker Sandboxes API v1.

## CreateVolumeRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateVolumeRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CreateVolumeRequest.md
Description: CreateVolumeRequest schema in Docker Sandboxes API v1.

## CredentialFenceReceipt
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CredentialFenceReceipt/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CredentialFenceReceipt.md
Description: CredentialFenceReceipt schema in Docker Sandboxes API v1.

## CustomInjection
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CustomInjection/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CustomInjection.md
Description: CustomInjection schema in Docker Sandboxes API v1.

## CustomSecretMaterial
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CustomSecretMaterial/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/CustomSecretMaterial.md
Description: CustomSecretMaterial schema in Docker Sandboxes API v1.

## DebugInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DebugInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DebugInfo.md
Description: DebugInfo schema in Docker Sandboxes API v1.

## DebugInfoErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DebugInfoErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DebugInfoErrorDetail.md
Description: DebugInfoErrorDetail schema in Docker Sandboxes API v1.

## DeleteSecretResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DeleteSecretResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/DeleteSecretResponse.md
Description: DeleteSecretResponse schema in Docker Sandboxes API v1.

## Duration
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Duration/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Duration.md
Description: Duration schema in Docker Sandboxes API v1.

## EffectiveCoreLifecycle
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveCoreLifecycle/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveCoreLifecycle.md
Description: EffectiveCoreLifecycle schema in Docker Sandboxes API v1.

## EffectiveFeatures
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveFeatures/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveFeatures.md
Description: EffectiveFeatures schema in Docker Sandboxes API v1.

## EffectiveManagedVolumes
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveManagedVolumes/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveManagedVolumes.md
Description: EffectiveManagedVolumes schema in Docker Sandboxes API v1.

## EffectiveNetworkPolicy
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveNetworkPolicy/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveNetworkPolicy.md
Description: EffectiveNetworkPolicy schema in Docker Sandboxes API v1.

## EffectiveTimeouts
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveTimeouts/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveTimeouts.md
Description: EffectiveTimeouts schema in Docker Sandboxes API v1.

## EffectiveVolumeAttachment
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveVolumeAttachment/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EffectiveVolumeAttachment.md
Description: EffectiveVolumeAttachment schema in Docker Sandboxes API v1.

## EndpointAuthentication
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointAuthentication/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointAuthentication.md
Description: EndpointAuthentication schema in Docker Sandboxes API v1.

## EndpointAuthenticationScheme
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointAuthenticationScheme/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointAuthenticationScheme.md
Description: EndpointAuthenticationScheme schema in Docker Sandboxes API v1.

## EndpointCredential
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointCredential/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointCredential.md
Description: EndpointCredential schema in Docker Sandboxes API v1.

## EndpointCredentialTransport
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointCredentialTransport/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EndpointCredentialTransport.md
Description: EndpointCredentialTransport schema in Docker Sandboxes API v1.

## Error
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Error/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Error.md
Description: Error schema in Docker Sandboxes API v1.

## ErrorCode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorCode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorCode.md
Description: ErrorCode schema in Docker Sandboxes API v1.

## ErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorDetail.md
Description: ErrorDetail schema in Docker Sandboxes API v1.

## ErrorInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorInfo.md
Description: ErrorInfo schema in Docker Sandboxes API v1.

## ErrorInfoErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorInfoErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ErrorInfoErrorDetail.md
Description: ErrorInfoErrorDetail schema in Docker Sandboxes API v1.

## EtagMismatch
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EtagMismatch/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EtagMismatch.md
Description: EtagMismatch schema in Docker Sandboxes API v1.

## EtagMismatchErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EtagMismatchErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/EtagMismatchErrorDetail.md
Description: EtagMismatchErrorDetail schema in Docker Sandboxes API v1.

## ExactDestination
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactDestination/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactDestination.md
Description: ExactDestination schema in Docker Sandboxes API v1.

## ExactDestinationKind
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactDestinationKind/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactDestinationKind.md
Description: ExactDestinationKind schema in Docker Sandboxes API v1.

## ExactNetworkPolicy
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactNetworkPolicy/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactNetworkPolicy.md
Description: ExactNetworkPolicy schema in Docker Sandboxes API v1.

## ExactPolicyConstant
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyConstant/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyConstant.md
Description: ExactPolicyConstant schema in Docker Sandboxes API v1.

## ExactPolicyNode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyNode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyNode.md
Description: ExactPolicyNode schema in Docker Sandboxes API v1.

## ExactPolicyOperands
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyOperands/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyOperands.md
Description: ExactPolicyOperands schema in Docker Sandboxes API v1.

## ExactPolicyOrigin
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyOrigin/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicyOrigin.md
Description: ExactPolicyOrigin schema in Docker Sandboxes API v1.

## ExactPolicySource
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicySource/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExactPolicySource.md
Description: ExactPolicySource schema in Docker Sandboxes API v1.

## ExchangeCompositionCredentialResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExchangeCompositionCredentialResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExchangeCompositionCredentialResponse.md
Description: ExchangeCompositionCredentialResponse schema in Docker Sandboxes API v1.

## ExecRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExecRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExecRequest.md
Description: ExecRequest schema in Docker Sandboxes API v1.

## ExecResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExecResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ExecResponse.md
Description: ExecResponse schema in Docker Sandboxes API v1.

## FeatureOptions
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FeatureOptions/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FeatureOptions.md
Description: FeatureOptions schema in Docker Sandboxes API v1.

## FileError
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileError/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileError.md
Description: FileError schema in Docker Sandboxes API v1.

## FileHeader
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileHeader/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileHeader.md
Description: FileHeader schema in Docker Sandboxes API v1.

## FileInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileInfo.md
Description: FileInfo schema in Docker Sandboxes API v1.

## FilesDownloadRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesDownloadRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesDownloadRequest.md
Description: FilesDownloadRequest schema in Docker Sandboxes API v1.

## FilesDownloadResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesDownloadResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesDownloadResponse.md
Description: FilesDownloadResponse schema in Docker Sandboxes API v1.

## FilesListResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesListResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesListResponse.md
Description: FilesListResponse schema in Docker Sandboxes API v1.

## FilesMkdirRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMkdirRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMkdirRequest.md
Description: FilesMkdirRequest schema in Docker Sandboxes API v1.

## FilesMkdirResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMkdirResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMkdirResponse.md
Description: FilesMkdirResponse schema in Docker Sandboxes API v1.

## FilesMoveRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMoveRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMoveRequest.md
Description: FilesMoveRequest schema in Docker Sandboxes API v1.

## FilesMoveResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMoveResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesMoveResponse.md
Description: FilesMoveResponse schema in Docker Sandboxes API v1.

## FilesReadFileRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesReadFileRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesReadFileRequest.md
Description: FilesReadFileRequest schema in Docker Sandboxes API v1.

## FilesReadFileResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesReadFileResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesReadFileResponse.md
Description: FilesReadFileResponse schema in Docker Sandboxes API v1.

## FilesRemoveResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesRemoveResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesRemoveResponse.md
Description: FilesRemoveResponse schema in Docker Sandboxes API v1.

## FilesStatResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesStatResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesStatResponse.md
Description: FilesStatResponse schema in Docker Sandboxes API v1.

## FilesUploadRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesUploadRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesUploadRequest.md
Description: FilesUploadRequest schema in Docker Sandboxes API v1.

## FilesUploadResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesUploadResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesUploadResponse.md
Description: FilesUploadResponse schema in Docker Sandboxes API v1.

## FilesWriteFileRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesWriteFileRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesWriteFileRequest.md
Description: FilesWriteFileRequest schema in Docker Sandboxes API v1.

## FilesWriteFileResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesWriteFileResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FilesWriteFileResponse.md
Description: FilesWriteFileResponse schema in Docker Sandboxes API v1.

## FileType
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileType/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/FileType.md
Description: FileType schema in Docker Sandboxes API v1.

## GetNetworkPoliciesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/GetNetworkPoliciesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/GetNetworkPoliciesResponse.md
Description: GetNetworkPoliciesResponse schema in Docker Sandboxes API v1.

## Help
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Help/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Help.md
Description: Help schema in Docker Sandboxes API v1.

## HelpErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/HelpErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/HelpErrorDetail.md
Description: HelpErrorDetail schema in Docker Sandboxes API v1.

## HelpLink
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/HelpLink/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/HelpLink.md
Description: HelpLink schema in Docker Sandboxes API v1.

## IdentityExchangeServiceExchangeDockerCredentialRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/IdentityExchangeServiceExchangeDockerCredentialRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/IdentityExchangeServiceExchangeDockerCredentialRequest.md
Description: IdentityExchangeServiceExchangeDockerCredentialRequest schema in Docker Sandboxes API v1.

## Image
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Image/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Image.md
Description: Image schema in Docker Sandboxes API v1.

## ImageBlobRef
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageBlobRef/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageBlobRef.md
Description: ImageBlobRef schema in Docker Sandboxes API v1.

## ImageFromImage
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageFromImage/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageFromImage.md
Description: ImageFromImage schema in Docker Sandboxes API v1.

## ImagePullSpec
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImagePullSpec/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImagePullSpec.md
Description: ImagePullSpec schema in Docker Sandboxes API v1.

## ImagePushTarget
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImagePushTarget/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImagePushTarget.md
Description: ImagePushTarget schema in Docker Sandboxes API v1.

## ImageSource
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageSource/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageSource.md
Description: ImageSource schema in Docker Sandboxes API v1.

## ImageStatus
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageStatus/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageStatus.md
Description: ImageStatus schema in Docker Sandboxes API v1.

## ImageSummary
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageSummary/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ImageSummary.md
Description: ImageSummary schema in Docker Sandboxes API v1.

## InteractRequest
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/InteractRequest/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/InteractRequest.md
Description: InteractRequest schema in Docker Sandboxes API v1.

## IssueSSHCertResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/IssueSSHCertResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/IssueSSHCertResponse.md
Description: IssueSSHCertResponse schema in Docker Sandboxes API v1.

## KitArtifactInput
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitArtifactInput/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitArtifactInput.md
Description: KitArtifactInput schema in Docker Sandboxes API v1.

## KitFieldDisposition
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldDisposition/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldDisposition.md
Description: KitFieldDisposition schema in Docker Sandboxes API v1.

## KitFieldOutcome
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcome/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcome.md
Description: KitFieldOutcome schema in Docker Sandboxes API v1.

## KitFieldOutcomeReport
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReport/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReport.md
Description: KitFieldOutcomeReport schema in Docker Sandboxes API v1.

## KitFieldOutcomeReportErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReportErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldOutcomeReportErrorDetail.md
Description: KitFieldOutcomeReportErrorDetail schema in Docker Sandboxes API v1.

## KitFieldReason
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldReason/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitFieldReason.md
Description: KitFieldReason schema in Docker Sandboxes API v1.

## KitInput
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitInput/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitInput.md
Description: KitInput schema in Docker Sandboxes API v1.

## KitRef
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitRef/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitRef.md
Description: KitRef schema in Docker Sandboxes API v1.

## KitStartup
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitStartup/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitStartup.md
Description: KitStartup schema in Docker Sandboxes API v1.

## KitStartupCommand
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitStartupCommand/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/KitStartupCommand.md
Description: KitStartupCommand schema in Docker Sandboxes API v1.

## ListImagesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListImagesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListImagesResponse.md
Description: ListImagesResponse schema in Docker Sandboxes API v1.

## ListPolicyLogEntriesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListPolicyLogEntriesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListPolicyLogEntriesResponse.md
Description: ListPolicyLogEntriesResponse schema in Docker Sandboxes API v1.

## ListPortsResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListPortsResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListPortsResponse.md
Description: ListPortsResponse schema in Docker Sandboxes API v1.

## ListProcessesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListProcessesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListProcessesResponse.md
Description: ListProcessesResponse schema in Docker Sandboxes API v1.

## ListSandboxesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSandboxesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSandboxesResponse.md
Description: ListSandboxesResponse schema in Docker Sandboxes API v1.

## ListSecretsResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSecretsResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSecretsResponse.md
Description: ListSecretsResponse schema in Docker Sandboxes API v1.

## ListSnapshotsResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSnapshotsResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListSnapshotsResponse.md
Description: ListSnapshotsResponse schema in Docker Sandboxes API v1.

## ListVolumesResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListVolumesResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ListVolumesResponse.md
Description: ListVolumesResponse schema in Docker Sandboxes API v1.

## LocalizedMessage
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/LocalizedMessage/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/LocalizedMessage.md
Description: LocalizedMessage schema in Docker Sandboxes API v1.

## LocalizedMessageErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/LocalizedMessageErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/LocalizedMessageErrorDetail.md
Description: LocalizedMessageErrorDetail schema in Docker Sandboxes API v1.

## ManagedVolumeOptions
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ManagedVolumeOptions/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ManagedVolumeOptions.md
Description: ManagedVolumeOptions schema in Docker Sandboxes API v1.

## McpAuthorization
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpAuthorization/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpAuthorization.md
Description: McpAuthorization schema in Docker Sandboxes API v1.

## McpAuthorizationStatus
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpAuthorizationStatus/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpAuthorizationStatus.md
Description: McpAuthorizationStatus schema in Docker Sandboxes API v1.

## McpConfigurationMode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationMode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationMode.md
Description: McpConfigurationMode schema in Docker Sandboxes API v1.

## McpConfigurationOutcome
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationOutcome/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationOutcome.md
Description: McpConfigurationOutcome schema in Docker Sandboxes API v1.

## McpConfigurationReport
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationReport/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationReport.md
Description: McpConfigurationReport schema in Docker Sandboxes API v1.

## McpConfigurationReportErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationReportErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfigurationReportErrorDetail.md
Description: McpConfigurationReportErrorDetail schema in Docker Sandboxes API v1.

## McpConfiguredServer
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfiguredServer/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpConfiguredServer.md
Description: McpConfiguredServer schema in Docker Sandboxes API v1.

## McpCreateSpec
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpCreateSpec/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpCreateSpec.md
Description: McpCreateSpec schema in Docker Sandboxes API v1.

## McpGateway
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpGateway/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpGateway.md
Description: McpGateway schema in Docker Sandboxes API v1.

## McpGatewayState
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpGatewayState/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpGatewayState.md
Description: McpGatewayState schema in Docker Sandboxes API v1.

## McpServer
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpServer/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpServer.md
Description: McpServer schema in Docker Sandboxes API v1.

## McpServerType
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpServerType/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/McpServerType.md
Description: McpServerType schema in Docker Sandboxes API v1.

## NetworkPolicy
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/NetworkPolicy/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/NetworkPolicy.md
Description: NetworkPolicy schema in Docker Sandboxes API v1.

## NetworkPolicyMode
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/NetworkPolicyMode/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/NetworkPolicyMode.md
Description: NetworkPolicyMode schema in Docker Sandboxes API v1.

## OAuthConfig
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OAuthConfig/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OAuthConfig.md
Description: OAuthConfig schema in Docker Sandboxes API v1.

## OAuthRefreshMaterial
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OAuthRefreshMaterial/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OAuthRefreshMaterial.md
Description: OAuthRefreshMaterial schema in Docker Sandboxes API v1.

## OutputRetention
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OutputRetention/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/OutputRetention.md
Description: OutputRetention schema in Docker Sandboxes API v1.

## Permission
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Permission/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Permission.md
Description: Permission schema in Docker Sandboxes API v1.

## Platform
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Platform/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Platform.md
Description: Platform schema in Docker Sandboxes API v1.

## PolicyDecision
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyDecision/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyDecision.md
Description: PolicyDecision schema in Docker Sandboxes API v1.

## PolicyDomain
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyDomain/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyDomain.md
Description: PolicyDomain schema in Docker Sandboxes API v1.

## PolicyLayer
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyLayer/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyLayer.md
Description: PolicyLayer schema in Docker Sandboxes API v1.

## PolicyLogEntry
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyLogEntry/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PolicyLogEntry.md
Description: PolicyLogEntry schema in Docker Sandboxes API v1.

## Port
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Port/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Port.md
Description: Port schema in Docker Sandboxes API v1.

## PreconditionFailure
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailure/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailure.md
Description: PreconditionFailure schema in Docker Sandboxes API v1.

## PreconditionFailureErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailureErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailureErrorDetail.md
Description: PreconditionFailureErrorDetail schema in Docker Sandboxes API v1.

## PreconditionFailureViolation
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailureViolation/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PreconditionFailureViolation.md
Description: PreconditionFailureViolation schema in Docker Sandboxes API v1.

## Process
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Process/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Process.md
Description: Process schema in Docker Sandboxes API v1.

## ProcessAttach
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessAttach/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessAttach.md
Description: ProcessAttach schema in Docker Sandboxes API v1.

## ProcessChunk
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessChunk/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessChunk.md
Description: ProcessChunk schema in Docker Sandboxes API v1.

## ProcessExited
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessExited/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessExited.md
Description: ProcessExited schema in Docker Sandboxes API v1.

## ProcessHeartbeat
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessHeartbeat/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessHeartbeat.md
Description: ProcessHeartbeat schema in Docker Sandboxes API v1.

## ProcessOutput
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessOutput/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessOutput.md
Description: ProcessOutput schema in Docker Sandboxes API v1.

## ProcessSignal
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessSignal/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessSignal.md
Description: ProcessSignal schema in Docker Sandboxes API v1.

## ProcessState
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessState/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ProcessState.md
Description: ProcessState schema in Docker Sandboxes API v1.

## Protocol
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Protocol/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Protocol.md
Description: Protocol schema in Docker Sandboxes API v1.

## PtyConfig
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PtyConfig/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PtyConfig.md
Description: PtyConfig schema in Docker Sandboxes API v1.

## PublishedPort
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PublishedPort/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/PublishedPort.md
Description: PublishedPort schema in Docker Sandboxes API v1.

## QuotaFailure
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailure/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailure.md
Description: QuotaFailure schema in Docker Sandboxes API v1.

## QuotaFailureErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailureErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailureErrorDetail.md
Description: QuotaFailureErrorDetail schema in Docker Sandboxes API v1.

## QuotaFailureViolation
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailureViolation/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/QuotaFailureViolation.md
Description: QuotaFailureViolation schema in Docker Sandboxes API v1.

## RawImageStartup
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RawImageStartup/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RawImageStartup.md
Description: RawImageStartup schema in Docker Sandboxes API v1.

## ReadOutputResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ReadOutputResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ReadOutputResponse.md
Description: ReadOutputResponse schema in Docker Sandboxes API v1.

## ReceiptKind
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ReceiptKind/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ReceiptKind.md
Description: ReceiptKind schema in Docker Sandboxes API v1.

## RequestInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RequestInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RequestInfo.md
Description: RequestInfo schema in Docker Sandboxes API v1.

## RequestInfoErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RequestInfoErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RequestInfoErrorDetail.md
Description: RequestInfoErrorDetail schema in Docker Sandboxes API v1.

## ResourceInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ResourceInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ResourceInfo.md
Description: ResourceInfo schema in Docker Sandboxes API v1.

## ResourceInfoErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ResourceInfoErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ResourceInfoErrorDetail.md
Description: ResourceInfoErrorDetail schema in Docker Sandboxes API v1.

## Resources
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Resources/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Resources.md
Description: Resources schema in Docker Sandboxes API v1.

## RetryInfo
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RetryInfo/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RetryInfo.md
Description: RetryInfo schema in Docker Sandboxes API v1.

## RetryInfoErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RetryInfoErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/RetryInfoErrorDetail.md
Description: RetryInfoErrorDetail schema in Docker Sandboxes API v1.

## Sandbox
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Sandbox/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Sandbox.md
Description: Sandbox schema in Docker Sandboxes API v1.

## SandboxCore
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxCore/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxCore.md
Description: SandboxCore schema in Docker Sandboxes API v1.

## SandboxEndpoint
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxEndpoint/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxEndpoint.md
Description: SandboxEndpoint schema in Docker Sandboxes API v1.

## SandboxEndpointProtocol
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxEndpointProtocol/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxEndpointProtocol.md
Description: SandboxEndpointProtocol schema in Docker Sandboxes API v1.

## SandboxStatus
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxStatus/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SandboxStatus.md
Description: SandboxStatus schema in Docker Sandboxes API v1.

## Secret
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Secret/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Secret.md
Description: Secret schema in Docker Sandboxes API v1.

## SecretType
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SecretType/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SecretType.md
Description: SecretType schema in Docker Sandboxes API v1.

## SignalResponse
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SignalResponse/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SignalResponse.md
Description: SignalResponse schema in Docker Sandboxes API v1.

## Snapshot
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Snapshot/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Snapshot.md
Description: Snapshot schema in Docker Sandboxes API v1.

## SnapshotStatus
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SnapshotStatus/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SnapshotStatus.md
Description: SnapshotStatus schema in Docker Sandboxes API v1.

## SnapshotSummary
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SnapshotSummary/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/SnapshotSummary.md
Description: SnapshotSummary schema in Docker Sandboxes API v1.

## StartupArgv
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StartupArgv/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StartupArgv.md
Description: StartupArgv schema in Docker Sandboxes API v1.

## StartupExecution
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StartupExecution/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StartupExecution.md
Description: StartupExecution schema in Docker Sandboxes API v1.

## StopMemoryOutcome
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StopMemoryOutcome/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StopMemoryOutcome.md
Description: StopMemoryOutcome schema in Docker Sandboxes API v1.

## StoredSecretOptions
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StoredSecretOptions/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StoredSecretOptions.md
Description: StoredSecretOptions schema in Docker Sandboxes API v1.

## StreamType
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StreamType/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/StreamType.md
Description: StreamType schema in Docker Sandboxes API v1.

## TerminalSize
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TerminalSize/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TerminalSize.md
Description: TerminalSize schema in Docker Sandboxes API v1.

## TimeoutAction
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TimeoutAction/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TimeoutAction.md
Description: TimeoutAction schema in Docker Sandboxes API v1.

## TimeoutOptions
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TimeoutOptions/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TimeoutOptions.md
Description: TimeoutOptions schema in Docker Sandboxes API v1.

## Timestamp
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Timestamp/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Timestamp.md
Description: Timestamp schema in Docker Sandboxes API v1.

## TokenSecretMaterial
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TokenSecretMaterial/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/TokenSecretMaterial.md
Description: TokenSecretMaterial schema in Docker Sandboxes API v1.

## UnknownErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/UnknownErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/UnknownErrorDetail.md
Description: UnknownErrorDetail schema in Docker Sandboxes API v1.

## UpdateSecretBody
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/UpdateSecretBody/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/UpdateSecretBody.md
Description: UpdateSecretBody schema in Docker Sandboxes API v1.

## ValidationFieldPath
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldPath/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldPath.md
Description: ValidationFieldPath schema in Docker Sandboxes API v1.

## ValidationFieldPathElement
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldPathElement/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldPathElement.md
Description: ValidationFieldPathElement schema in Docker Sandboxes API v1.

## ValidationFieldType
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldType/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationFieldType.md
Description: ValidationFieldType schema in Docker Sandboxes API v1.

## ValidationViolation
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolation/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolation.md
Description: ValidationViolation schema in Docker Sandboxes API v1.

## ValidationViolations
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolations/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolations.md
Description: ValidationViolations schema in Docker Sandboxes API v1.

## ValidationViolationsErrorDetail
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolationsErrorDetail/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/ValidationViolationsErrorDetail.md
Description: ValidationViolationsErrorDetail schema in Docker Sandboxes API v1.

## Volume
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Volume/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/Volume.md
Description: Volume schema in Docker Sandboxes API v1.

## VolumeAttachment
URL: https://docs.docker.com/reference/api/sandboxes/latest/schemas/VolumeAttachment/
Markdown: https://docs.docker.com/reference/api/sandboxes/latest/schemas/VolumeAttachment.md
Description: VolumeAttachment schema in Docker Sandboxes API v1.

## ConsistentInstructionCasing
URL: https://docs.docker.com/reference/build-checks/consistent-instruction-casing/
Markdown: https://docs.docker.com/reference/build-checks/consistent-instruction-casing.md
Description: All commands within the Dockerfile should use the same casing (either upper or lower)

## CopyIgnoredFile
URL: https://docs.docker.com/reference/build-checks/copy-ignored-file/
Markdown: https://docs.docker.com/reference/build-checks/copy-ignored-file.md
Description: Attempting to Copy file that is excluded by .dockerignore

## DuplicateStageName
URL: https://docs.docker.com/reference/build-checks/duplicate-stage-name/
Markdown: https://docs.docker.com/reference/build-checks/duplicate-stage-name.md
Description: Stage names should be unique

## ExposeInvalidFormat
URL: https://docs.docker.com/reference/build-checks/expose-invalid-format/
Markdown: https://docs.docker.com/reference/build-checks/expose-invalid-format.md
Description: IP address and host-port mapping should not be used in EXPOSE instruction. This will become an error in a future release

## ExposeProtoCasing
URL: https://docs.docker.com/reference/build-checks/expose-proto-casing/
Markdown: https://docs.docker.com/reference/build-checks/expose-proto-casing.md
Description: Protocol in EXPOSE instruction should be lowercase

## FromAsCasing
URL: https://docs.docker.com/reference/build-checks/from-as-casing/
Markdown: https://docs.docker.com/reference/build-checks/from-as-casing.md
Description: The 'as' keyword should match the case of the 'from' keyword

## FromPlatformFlagConstDisallowed
URL: https://docs.docker.com/reference/build-checks/from-platform-flag-const-disallowed/
Markdown: https://docs.docker.com/reference/build-checks/from-platform-flag-const-disallowed.md
Description: FROM --platform flag should not use a constant value

## InvalidDefaultArgInFrom
URL: https://docs.docker.com/reference/build-checks/invalid-default-arg-in-from/
Markdown: https://docs.docker.com/reference/build-checks/invalid-default-arg-in-from.md
Description: Default value for global ARG results in an empty or invalid base image name

## InvalidDefinitionDescription
URL: https://docs.docker.com/reference/build-checks/invalid-definition-description/
Markdown: https://docs.docker.com/reference/build-checks/invalid-definition-description.md
Description: Comment for build stage or argument should follow the format: `#  `. If this is not intended to be a description comment, add an empty line or comment between the instruction and the comment.

## JSONArgsRecommended
URL: https://docs.docker.com/reference/build-checks/json-args-recommended/
Markdown: https://docs.docker.com/reference/build-checks/json-args-recommended.md
Description: JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals

## LegacyKeyValueFormat
URL: https://docs.docker.com/reference/build-checks/legacy-key-value-format/
Markdown: https://docs.docker.com/reference/build-checks/legacy-key-value-format.md
Description: Legacy key/value format with whitespace separator should not be used

## MaintainerDeprecated
URL: https://docs.docker.com/reference/build-checks/maintainer-deprecated/
Markdown: https://docs.docker.com/reference/build-checks/maintainer-deprecated.md
Description: The MAINTAINER instruction is deprecated, use a label instead to define an image author

## MultipleInstructionsDisallowed
URL: https://docs.docker.com/reference/build-checks/multiple-instructions-disallowed/
Markdown: https://docs.docker.com/reference/build-checks/multiple-instructions-disallowed.md
Description: Multiple instructions of the same type should not be used in the same stage

## NoEmptyContinuation
URL: https://docs.docker.com/reference/build-checks/no-empty-continuation/
Markdown: https://docs.docker.com/reference/build-checks/no-empty-continuation.md
Description: Empty continuation lines will become errors in a future release

## RedundantTargetPlatform
URL: https://docs.docker.com/reference/build-checks/redundant-target-platform/
Markdown: https://docs.docker.com/reference/build-checks/redundant-target-platform.md
Description: Setting platform to predefined $TARGETPLATFORM in FROM is redundant as this is the default behavior

## ReservedStageName
URL: https://docs.docker.com/reference/build-checks/reserved-stage-name/
Markdown: https://docs.docker.com/reference/build-checks/reserved-stage-name.md
Description: Reserved words should not be used as stage names

## SecretsUsedInArgOrEnv
URL: https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/
Markdown: https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env.md
Description: Sensitive data should not be used in the ARG or ENV commands

## StageNameCasing
URL: https://docs.docker.com/reference/build-checks/stage-name-casing/
Markdown: https://docs.docker.com/reference/build-checks/stage-name-casing.md
Description: Stage names should be lowercase

## UndefinedArgInFrom
URL: https://docs.docker.com/reference/build-checks/undefined-arg-in-from/
Markdown: https://docs.docker.com/reference/build-checks/undefined-arg-in-from.md
Description: FROM command must use declared ARGs

## UndefinedVar
URL: https://docs.docker.com/reference/build-checks/undefined-var/
Markdown: https://docs.docker.com/reference/build-checks/undefined-var.md
Description: Variables should be defined before their use

## WorkdirRelativePath
URL: https://docs.docker.com/reference/build-checks/workdir-relative-path/
Markdown: https://docs.docker.com/reference/build-checks/workdir-relative-path.md
Description: Relative workdir without an absolute workdir declared within the build can have unexpected results if the base image changes

## docker build
URL: https://docs.docker.com/reference/cli/docker/build/
Markdown: https://docs.docker.com/reference/cli/docker/build.md

## docker builder build
URL: https://docs.docker.com/reference/cli/docker/builder/build/
Markdown: https://docs.docker.com/reference/cli/docker/builder/build.md

## docker builder prune
URL: https://docs.docker.com/reference/cli/docker/builder/prune/
Markdown: https://docs.docker.com/reference/cli/docker/builder/prune.md

## docker buildx bake
URL: https://docs.docker.com/reference/cli/docker/buildx/bake/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/bake.md

## docker buildx build
URL: https://docs.docker.com/reference/cli/docker/buildx/build/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/build.md

## docker buildx create
URL: https://docs.docker.com/reference/cli/docker/buildx/create/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/create.md

## docker buildx dap build
URL: https://docs.docker.com/reference/cli/docker/buildx/dap/build/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/dap/build.md

## docker buildx debug build
URL: https://docs.docker.com/reference/cli/docker/buildx/debug/build/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/debug/build.md

## docker buildx dial-stdio
URL: https://docs.docker.com/reference/cli/docker/buildx/dial-stdio/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/dial-stdio.md

## docker buildx du
URL: https://docs.docker.com/reference/cli/docker/buildx/du/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/du.md

## docker buildx history export
URL: https://docs.docker.com/reference/cli/docker/buildx/history/export/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/export.md

## docker buildx history import
URL: https://docs.docker.com/reference/cli/docker/buildx/history/import/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/import.md

## docker buildx history inspect attachment
URL: https://docs.docker.com/reference/cli/docker/buildx/history/inspect/attachment/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/inspect/attachment.md

## docker buildx history logs
URL: https://docs.docker.com/reference/cli/docker/buildx/history/logs/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/logs.md

## docker buildx history ls
URL: https://docs.docker.com/reference/cli/docker/buildx/history/ls/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/ls.md

## docker buildx history open
URL: https://docs.docker.com/reference/cli/docker/buildx/history/open/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/open.md

## docker buildx history rm
URL: https://docs.docker.com/reference/cli/docker/buildx/history/rm/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/rm.md

## docker buildx history trace
URL: https://docs.docker.com/reference/cli/docker/buildx/history/trace/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/history/trace.md

## docker buildx imagetools create
URL: https://docs.docker.com/reference/cli/docker/buildx/imagetools/create/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/imagetools/create.md

## docker buildx imagetools inspect
URL: https://docs.docker.com/reference/cli/docker/buildx/imagetools/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/imagetools/inspect.md

## docker buildx inspect
URL: https://docs.docker.com/reference/cli/docker/buildx/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/inspect.md

## docker buildx ls
URL: https://docs.docker.com/reference/cli/docker/buildx/ls/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/ls.md

## docker buildx policy eval
URL: https://docs.docker.com/reference/cli/docker/buildx/policy/eval/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/policy/eval.md

## docker buildx policy test
URL: https://docs.docker.com/reference/cli/docker/buildx/policy/test/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/policy/test.md

## docker buildx prune
URL: https://docs.docker.com/reference/cli/docker/buildx/prune/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/prune.md

## docker buildx replay build
URL: https://docs.docker.com/reference/cli/docker/buildx/replay/build/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/replay/build.md

## docker buildx rm
URL: https://docs.docker.com/reference/cli/docker/buildx/rm/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/rm.md

## docker buildx stop
URL: https://docs.docker.com/reference/cli/docker/buildx/stop/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/stop.md

## docker buildx use
URL: https://docs.docker.com/reference/cli/docker/buildx/use/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/use.md

## docker buildx version
URL: https://docs.docker.com/reference/cli/docker/buildx/version/
Markdown: https://docs.docker.com/reference/cli/docker/buildx/version.md

## docker checkpoint create
URL: https://docs.docker.com/reference/cli/docker/checkpoint/create/
Markdown: https://docs.docker.com/reference/cli/docker/checkpoint/create.md

## docker checkpoint ls
URL: https://docs.docker.com/reference/cli/docker/checkpoint/ls/
Markdown: https://docs.docker.com/reference/cli/docker/checkpoint/ls.md

## docker checkpoint rm
URL: https://docs.docker.com/reference/cli/docker/checkpoint/rm/
Markdown: https://docs.docker.com/reference/cli/docker/checkpoint/rm.md

## docker compose alpha dry-run
URL: https://docs.docker.com/reference/cli/docker/compose/alpha/dry-run/
Markdown: https://docs.docker.com/reference/cli/docker/compose/alpha/dry-run.md

## docker compose alpha scale
URL: https://docs.docker.com/reference/cli/docker/compose/alpha/scale/
Markdown: https://docs.docker.com/reference/cli/docker/compose/alpha/scale.md

## docker compose alpha watch
URL: https://docs.docker.com/reference/cli/docker/compose/alpha/watch/
Markdown: https://docs.docker.com/reference/cli/docker/compose/alpha/watch.md

## docker compose attach
URL: https://docs.docker.com/reference/cli/docker/compose/attach/
Markdown: https://docs.docker.com/reference/cli/docker/compose/attach.md

## docker compose bridge convert
URL: https://docs.docker.com/reference/cli/docker/compose/bridge/convert/
Markdown: https://docs.docker.com/reference/cli/docker/compose/bridge/convert.md

## docker compose bridge transformations create
URL: https://docs.docker.com/reference/cli/docker/compose/bridge/transformations/create/
Markdown: https://docs.docker.com/reference/cli/docker/compose/bridge/transformations/create.md

## docker compose bridge transformations list
URL: https://docs.docker.com/reference/cli/docker/compose/bridge/transformations/list/
Markdown: https://docs.docker.com/reference/cli/docker/compose/bridge/transformations/list.md

## docker compose build
URL: https://docs.docker.com/reference/cli/docker/compose/build/
Markdown: https://docs.docker.com/reference/cli/docker/compose/build.md

## docker compose commit
URL: https://docs.docker.com/reference/cli/docker/compose/commit/
Markdown: https://docs.docker.com/reference/cli/docker/compose/commit.md

## docker compose config
URL: https://docs.docker.com/reference/cli/docker/compose/config/
Markdown: https://docs.docker.com/reference/cli/docker/compose/config.md

## docker compose convert
URL: https://docs.docker.com/reference/cli/docker/compose/convert/
Markdown: https://docs.docker.com/reference/cli/docker/compose/convert.md

## docker compose cp
URL: https://docs.docker.com/reference/cli/docker/compose/cp/
Markdown: https://docs.docker.com/reference/cli/docker/compose/cp.md

## docker compose create
URL: https://docs.docker.com/reference/cli/docker/compose/create/
Markdown: https://docs.docker.com/reference/cli/docker/compose/create.md

## docker compose down
URL: https://docs.docker.com/reference/cli/docker/compose/down/
Markdown: https://docs.docker.com/reference/cli/docker/compose/down.md

## docker compose events
URL: https://docs.docker.com/reference/cli/docker/compose/events/
Markdown: https://docs.docker.com/reference/cli/docker/compose/events.md

## docker compose exec
URL: https://docs.docker.com/reference/cli/docker/compose/exec/
Markdown: https://docs.docker.com/reference/cli/docker/compose/exec.md

## docker compose export
URL: https://docs.docker.com/reference/cli/docker/compose/export/
Markdown: https://docs.docker.com/reference/cli/docker/compose/export.md

## docker compose images
URL: https://docs.docker.com/reference/cli/docker/compose/images/
Markdown: https://docs.docker.com/reference/cli/docker/compose/images.md

## docker compose kill
URL: https://docs.docker.com/reference/cli/docker/compose/kill/
Markdown: https://docs.docker.com/reference/cli/docker/compose/kill.md

## docker compose logs
URL: https://docs.docker.com/reference/cli/docker/compose/logs/
Markdown: https://docs.docker.com/reference/cli/docker/compose/logs.md

## docker compose ls
URL: https://docs.docker.com/reference/cli/docker/compose/ls/
Markdown: https://docs.docker.com/reference/cli/docker/compose/ls.md

## docker compose pause
URL: https://docs.docker.com/reference/cli/docker/compose/pause/
Markdown: https://docs.docker.com/reference/cli/docker/compose/pause.md

## docker compose port
URL: https://docs.docker.com/reference/cli/docker/compose/port/
Markdown: https://docs.docker.com/reference/cli/docker/compose/port.md

## docker compose ps
URL: https://docs.docker.com/reference/cli/docker/compose/ps/
Markdown: https://docs.docker.com/reference/cli/docker/compose/ps.md

## docker compose publish
URL: https://docs.docker.com/reference/cli/docker/compose/publish/
Markdown: https://docs.docker.com/reference/cli/docker/compose/publish.md

## docker compose pull
URL: https://docs.docker.com/reference/cli/docker/compose/pull/
Markdown: https://docs.docker.com/reference/cli/docker/compose/pull.md

## docker compose push
URL: https://docs.docker.com/reference/cli/docker/compose/push/
Markdown: https://docs.docker.com/reference/cli/docker/compose/push.md

## docker compose restart
URL: https://docs.docker.com/reference/cli/docker/compose/restart/
Markdown: https://docs.docker.com/reference/cli/docker/compose/restart.md

## docker compose rm
URL: https://docs.docker.com/reference/cli/docker/compose/rm/
Markdown: https://docs.docker.com/reference/cli/docker/compose/rm.md

## docker compose run
URL: https://docs.docker.com/reference/cli/docker/compose/run/
Markdown: https://docs.docker.com/reference/cli/docker/compose/run.md

## docker compose scale
URL: https://docs.docker.com/reference/cli/docker/compose/scale/
Markdown: https://docs.docker.com/reference/cli/docker/compose/scale.md

## docker compose start
URL: https://docs.docker.com/reference/cli/docker/compose/start/
Markdown: https://docs.docker.com/reference/cli/docker/compose/start.md

## docker compose stats
URL: https://docs.docker.com/reference/cli/docker/compose/stats/
Markdown: https://docs.docker.com/reference/cli/docker/compose/stats.md

## docker compose stop
URL: https://docs.docker.com/reference/cli/docker/compose/stop/
Markdown: https://docs.docker.com/reference/cli/docker/compose/stop.md

## docker compose top
URL: https://docs.docker.com/reference/cli/docker/compose/top/
Markdown: https://docs.docker.com/reference/cli/docker/compose/top.md

## docker compose unpause
URL: https://docs.docker.com/reference/cli/docker/compose/unpause/
Markdown: https://docs.docker.com/reference/cli/docker/compose/unpause.md

## docker compose up
URL: https://docs.docker.com/reference/cli/docker/compose/up/
Markdown: https://docs.docker.com/reference/cli/docker/compose/up.md

## docker compose version
URL: https://docs.docker.com/reference/cli/docker/compose/version/
Markdown: https://docs.docker.com/reference/cli/docker/compose/version.md

## docker compose volumes
URL: https://docs.docker.com/reference/cli/docker/compose/volumes/
Markdown: https://docs.docker.com/reference/cli/docker/compose/volumes.md

## docker compose wait
URL: https://docs.docker.com/reference/cli/docker/compose/wait/
Markdown: https://docs.docker.com/reference/cli/docker/compose/wait.md

## docker compose watch
URL: https://docs.docker.com/reference/cli/docker/compose/watch/
Markdown: https://docs.docker.com/reference/cli/docker/compose/watch.md

## docker config create
URL: https://docs.docker.com/reference/cli/docker/config/create/
Markdown: https://docs.docker.com/reference/cli/docker/config/create.md

## docker config inspect
URL: https://docs.docker.com/reference/cli/docker/config/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/config/inspect.md

## docker config ls
URL: https://docs.docker.com/reference/cli/docker/config/ls/
Markdown: https://docs.docker.com/reference/cli/docker/config/ls.md

## docker config rm
URL: https://docs.docker.com/reference/cli/docker/config/rm/
Markdown: https://docs.docker.com/reference/cli/docker/config/rm.md

## docker container attach
URL: https://docs.docker.com/reference/cli/docker/container/attach/
Markdown: https://docs.docker.com/reference/cli/docker/container/attach.md

## docker container commit
URL: https://docs.docker.com/reference/cli/docker/container/commit/
Markdown: https://docs.docker.com/reference/cli/docker/container/commit.md

## docker container cp
URL: https://docs.docker.com/reference/cli/docker/container/cp/
Markdown: https://docs.docker.com/reference/cli/docker/container/cp.md

## docker container create
URL: https://docs.docker.com/reference/cli/docker/container/create/
Markdown: https://docs.docker.com/reference/cli/docker/container/create.md

## docker container diff
URL: https://docs.docker.com/reference/cli/docker/container/diff/
Markdown: https://docs.docker.com/reference/cli/docker/container/diff.md

## docker container exec
URL: https://docs.docker.com/reference/cli/docker/container/exec/
Markdown: https://docs.docker.com/reference/cli/docker/container/exec.md

## docker container export
URL: https://docs.docker.com/reference/cli/docker/container/export/
Markdown: https://docs.docker.com/reference/cli/docker/container/export.md

## docker container inspect
URL: https://docs.docker.com/reference/cli/docker/container/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/container/inspect.md

## docker container kill
URL: https://docs.docker.com/reference/cli/docker/container/kill/
Markdown: https://docs.docker.com/reference/cli/docker/container/kill.md

## docker container logs
URL: https://docs.docker.com/reference/cli/docker/container/logs/
Markdown: https://docs.docker.com/reference/cli/docker/container/logs.md

## docker container ls
URL: https://docs.docker.com/reference/cli/docker/container/ls/
Markdown: https://docs.docker.com/reference/cli/docker/container/ls.md

## docker container pause
URL: https://docs.docker.com/reference/cli/docker/container/pause/
Markdown: https://docs.docker.com/reference/cli/docker/container/pause.md

## docker container port
URL: https://docs.docker.com/reference/cli/docker/container/port/
Markdown: https://docs.docker.com/reference/cli/docker/container/port.md

## docker container prune
URL: https://docs.docker.com/reference/cli/docker/container/prune/
Markdown: https://docs.docker.com/reference/cli/docker/container/prune.md

## docker container rename
URL: https://docs.docker.com/reference/cli/docker/container/rename/
Markdown: https://docs.docker.com/reference/cli/docker/container/rename.md

## docker container restart
URL: https://docs.docker.com/reference/cli/docker/container/restart/
Markdown: https://docs.docker.com/reference/cli/docker/container/restart.md

## docker container rm
URL: https://docs.docker.com/reference/cli/docker/container/rm/
Markdown: https://docs.docker.com/reference/cli/docker/container/rm.md

## docker container run
URL: https://docs.docker.com/reference/cli/docker/container/run/
Markdown: https://docs.docker.com/reference/cli/docker/container/run.md

## docker container start
URL: https://docs.docker.com/reference/cli/docker/container/start/
Markdown: https://docs.docker.com/reference/cli/docker/container/start.md

## docker container stats
URL: https://docs.docker.com/reference/cli/docker/container/stats/
Markdown: https://docs.docker.com/reference/cli/docker/container/stats.md

## docker container stop
URL: https://docs.docker.com/reference/cli/docker/container/stop/
Markdown: https://docs.docker.com/reference/cli/docker/container/stop.md

## docker container top
URL: https://docs.docker.com/reference/cli/docker/container/top/
Markdown: https://docs.docker.com/reference/cli/docker/container/top.md

## docker container unpause
URL: https://docs.docker.com/reference/cli/docker/container/unpause/
Markdown: https://docs.docker.com/reference/cli/docker/container/unpause.md

## docker container update
URL: https://docs.docker.com/reference/cli/docker/container/update/
Markdown: https://docs.docker.com/reference/cli/docker/container/update.md

## docker container wait
URL: https://docs.docker.com/reference/cli/docker/container/wait/
Markdown: https://docs.docker.com/reference/cli/docker/container/wait.md

## docker context create
URL: https://docs.docker.com/reference/cli/docker/context/create/
Markdown: https://docs.docker.com/reference/cli/docker/context/create.md

## docker context export
URL: https://docs.docker.com/reference/cli/docker/context/export/
Markdown: https://docs.docker.com/reference/cli/docker/context/export.md

## docker context import
URL: https://docs.docker.com/reference/cli/docker/context/import/
Markdown: https://docs.docker.com/reference/cli/docker/context/import.md

## docker context inspect
URL: https://docs.docker.com/reference/cli/docker/context/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/context/inspect.md

## docker context ls
URL: https://docs.docker.com/reference/cli/docker/context/ls/
Markdown: https://docs.docker.com/reference/cli/docker/context/ls.md

## docker context rm
URL: https://docs.docker.com/reference/cli/docker/context/rm/
Markdown: https://docs.docker.com/reference/cli/docker/context/rm.md

## docker context show
URL: https://docs.docker.com/reference/cli/docker/context/show/
Markdown: https://docs.docker.com/reference/cli/docker/context/show.md

## docker context update
URL: https://docs.docker.com/reference/cli/docker/context/update/
Markdown: https://docs.docker.com/reference/cli/docker/context/update.md

## docker context use
URL: https://docs.docker.com/reference/cli/docker/context/use/
Markdown: https://docs.docker.com/reference/cli/docker/context/use.md

## docker debug
URL: https://docs.docker.com/reference/cli/docker/debug/
Markdown: https://docs.docker.com/reference/cli/docker/debug.md

## docker desktop auth status
URL: https://docs.docker.com/reference/cli/docker/desktop/auth/status/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/auth/status.md

## docker desktop diagnose
URL: https://docs.docker.com/reference/cli/docker/desktop/diagnose/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/diagnose.md

## docker desktop disable model-runner
URL: https://docs.docker.com/reference/cli/docker/desktop/disable/model-runner/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/disable/model-runner.md

## docker desktop enable model-runner
URL: https://docs.docker.com/reference/cli/docker/desktop/enable/model-runner/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/enable/model-runner.md

## docker desktop engine ls
URL: https://docs.docker.com/reference/cli/docker/desktop/engine/ls/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/engine/ls.md

## docker desktop engine use
URL: https://docs.docker.com/reference/cli/docker/desktop/engine/use/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/engine/use.md

## docker desktop kubernetes images
URL: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/images/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/images.md

## docker desktop kubernetes reset-cluster
URL: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/reset-cluster/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/reset-cluster.md

## docker desktop kubernetes status
URL: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/status/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/kubernetes/status.md

## docker desktop logs
URL: https://docs.docker.com/reference/cli/docker/desktop/logs/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/logs.md

## docker desktop restart
URL: https://docs.docker.com/reference/cli/docker/desktop/restart/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/restart.md

## docker desktop start
URL: https://docs.docker.com/reference/cli/docker/desktop/start/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/start.md

## docker desktop status
URL: https://docs.docker.com/reference/cli/docker/desktop/status/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/status.md

## docker desktop stop
URL: https://docs.docker.com/reference/cli/docker/desktop/stop/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/stop.md

## docker desktop update
URL: https://docs.docker.com/reference/cli/docker/desktop/update/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/update.md

## docker desktop version
URL: https://docs.docker.com/reference/cli/docker/desktop/version/
Markdown: https://docs.docker.com/reference/cli/docker/desktop/version.md

## docker dhi attestation get
URL: https://docs.docker.com/reference/cli/docker/dhi/attestation/get/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/attestation/get.md

## docker dhi attestation list
URL: https://docs.docker.com/reference/cli/docker/dhi/attestation/list/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/attestation/list.md

## docker dhi attestation sbom
URL: https://docs.docker.com/reference/cli/docker/dhi/attestation/sbom/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/attestation/sbom.md

## docker dhi auth apk
URL: https://docs.docker.com/reference/cli/docker/dhi/auth/apk/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/auth/apk.md

## docker dhi auth deb
URL: https://docs.docker.com/reference/cli/docker/dhi/auth/deb/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/auth/deb.md

## docker dhi catalog get
URL: https://docs.docker.com/reference/cli/docker/dhi/catalog/get/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/catalog/get.md

## docker dhi catalog list
URL: https://docs.docker.com/reference/cli/docker/dhi/catalog/list/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/catalog/list.md

## docker dhi customization build get
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/build/get/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/build/get.md

## docker dhi customization build list
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/build/list/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/build/list.md

## docker dhi customization build logs
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/build/logs/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/build/logs.md

## docker dhi customization create
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/create/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/create.md

## docker dhi customization delete
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/delete/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/delete.md

## docker dhi customization edit
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/edit/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/edit.md

## docker dhi customization get
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/get/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/get.md

## docker dhi customization list
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/list/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/list.md

## docker dhi customization prepare
URL: https://docs.docker.com/reference/cli/docker/dhi/customization/prepare/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/customization/prepare.md

## docker dhi mirror list
URL: https://docs.docker.com/reference/cli/docker/dhi/mirror/list/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/mirror/list.md

## docker dhi mirror start
URL: https://docs.docker.com/reference/cli/docker/dhi/mirror/start/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/mirror/start.md

## docker dhi mirror stop
URL: https://docs.docker.com/reference/cli/docker/dhi/mirror/stop/
Markdown: https://docs.docker.com/reference/cli/docker/dhi/mirror/stop.md

## docker exec
URL: https://docs.docker.com/reference/cli/docker/exec/
Markdown: https://docs.docker.com/reference/cli/docker/exec.md

## docker image build
URL: https://docs.docker.com/reference/cli/docker/image/build/
Markdown: https://docs.docker.com/reference/cli/docker/image/build.md

## docker image history
URL: https://docs.docker.com/reference/cli/docker/image/history/
Markdown: https://docs.docker.com/reference/cli/docker/image/history.md

## docker image import
URL: https://docs.docker.com/reference/cli/docker/image/import/
Markdown: https://docs.docker.com/reference/cli/docker/image/import.md

## docker image inspect
URL: https://docs.docker.com/reference/cli/docker/image/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/image/inspect.md

## docker image load
URL: https://docs.docker.com/reference/cli/docker/image/load/
Markdown: https://docs.docker.com/reference/cli/docker/image/load.md

## docker image ls
URL: https://docs.docker.com/reference/cli/docker/image/ls/
Markdown: https://docs.docker.com/reference/cli/docker/image/ls.md

## docker image prune
URL: https://docs.docker.com/reference/cli/docker/image/prune/
Markdown: https://docs.docker.com/reference/cli/docker/image/prune.md

## docker image pull
URL: https://docs.docker.com/reference/cli/docker/image/pull/
Markdown: https://docs.docker.com/reference/cli/docker/image/pull.md

## docker image push
URL: https://docs.docker.com/reference/cli/docker/image/push/
Markdown: https://docs.docker.com/reference/cli/docker/image/push.md

## docker image rm
URL: https://docs.docker.com/reference/cli/docker/image/rm/
Markdown: https://docs.docker.com/reference/cli/docker/image/rm.md

## docker image save
URL: https://docs.docker.com/reference/cli/docker/image/save/
Markdown: https://docs.docker.com/reference/cli/docker/image/save.md

## docker image tag
URL: https://docs.docker.com/reference/cli/docker/image/tag/
Markdown: https://docs.docker.com/reference/cli/docker/image/tag.md

## docker images
URL: https://docs.docker.com/reference/cli/docker/images/
Markdown: https://docs.docker.com/reference/cli/docker/images.md

## docker info
URL: https://docs.docker.com/reference/cli/docker/info/
Markdown: https://docs.docker.com/reference/cli/docker/info.md

## docker init
URL: https://docs.docker.com/reference/cli/docker/init/
Markdown: https://docs.docker.com/reference/cli/docker/init.md

## docker inspect
URL: https://docs.docker.com/reference/cli/docker/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/inspect.md

## docker login
URL: https://docs.docker.com/reference/cli/docker/login/
Markdown: https://docs.docker.com/reference/cli/docker/login.md

## docker logout
URL: https://docs.docker.com/reference/cli/docker/logout/
Markdown: https://docs.docker.com/reference/cli/docker/logout.md

## docker manifest annotate
URL: https://docs.docker.com/reference/cli/docker/manifest/annotate/
Markdown: https://docs.docker.com/reference/cli/docker/manifest/annotate.md

## docker manifest create
URL: https://docs.docker.com/reference/cli/docker/manifest/create/
Markdown: https://docs.docker.com/reference/cli/docker/manifest/create.md

## docker manifest inspect
URL: https://docs.docker.com/reference/cli/docker/manifest/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/manifest/inspect.md

## docker manifest push
URL: https://docs.docker.com/reference/cli/docker/manifest/push/
Markdown: https://docs.docker.com/reference/cli/docker/manifest/push.md

## docker manifest rm
URL: https://docs.docker.com/reference/cli/docker/manifest/rm/
Markdown: https://docs.docker.com/reference/cli/docker/manifest/rm.md

## docker mcp catalog create
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/create/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/create.md

## docker mcp catalog list
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/list/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/list.md

## docker mcp catalog ls
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/ls.md

## docker mcp catalog pull
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/pull/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/pull.md

## docker mcp catalog push
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/push/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/push.md

## docker mcp catalog remove
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/remove/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/remove.md

## docker mcp catalog rm
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/rm/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/rm.md

## docker mcp catalog server add
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/add/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/add.md

## docker mcp catalog server inspect
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/inspect.md

## docker mcp catalog server ls
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/ls.md

## docker mcp catalog server remove
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/remove/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/server/remove.md

## docker mcp catalog show
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/show/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/show.md

## docker mcp catalog tag
URL: https://docs.docker.com/reference/cli/docker/mcp/catalog/tag/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/catalog/tag.md

## docker mcp client connect
URL: https://docs.docker.com/reference/cli/docker/mcp/client/connect/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/client/connect.md

## docker mcp client disconnect
URL: https://docs.docker.com/reference/cli/docker/mcp/client/disconnect/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/client/disconnect.md

## docker mcp client ls
URL: https://docs.docker.com/reference/cli/docker/mcp/client/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/client/ls.md

## docker mcp feature disable
URL: https://docs.docker.com/reference/cli/docker/mcp/feature/disable/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/feature/disable.md

## docker mcp feature enable
URL: https://docs.docker.com/reference/cli/docker/mcp/feature/enable/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/feature/enable.md

## docker mcp feature list
URL: https://docs.docker.com/reference/cli/docker/mcp/feature/list/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/feature/list.md

## docker mcp feature ls
URL: https://docs.docker.com/reference/cli/docker/mcp/feature/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/feature/ls.md

## docker mcp gateway run
URL: https://docs.docker.com/reference/cli/docker/mcp/gateway/run/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/gateway/run.md

## docker mcp profile config
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/config/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/config.md

## docker mcp profile create
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/create/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/create.md

## docker mcp profile export
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/export/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/export.md

## docker mcp profile import
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/import/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/import.md

## docker mcp profile list
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/list/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/list.md

## docker mcp profile pull
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/pull/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/pull.md

## docker mcp profile push
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/push/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/push.md

## docker mcp profile remove
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/remove/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/remove.md

## docker mcp profile server add
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/server/add/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/server/add.md

## docker mcp profile server ls
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/server/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/server/ls.md

## docker mcp profile server remove
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/server/remove/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/server/remove.md

## docker mcp profile show
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/show/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/show.md

## docker mcp profile tools
URL: https://docs.docker.com/reference/cli/docker/mcp/profile/tools/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/profile/tools.md

## docker mcp secret ls
URL: https://docs.docker.com/reference/cli/docker/mcp/secret/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/secret/ls.md

## docker mcp secret rm
URL: https://docs.docker.com/reference/cli/docker/mcp/secret/rm/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/secret/rm.md

## docker mcp secret set
URL: https://docs.docker.com/reference/cli/docker/mcp/secret/set/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/secret/set.md

## docker mcp server init
URL: https://docs.docker.com/reference/cli/docker/mcp/server/init/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/server/init.md

## docker mcp tools call
URL: https://docs.docker.com/reference/cli/docker/mcp/tools/call/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/tools/call.md

## docker mcp tools count
URL: https://docs.docker.com/reference/cli/docker/mcp/tools/count/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/tools/count.md

## docker mcp tools inspect
URL: https://docs.docker.com/reference/cli/docker/mcp/tools/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/tools/inspect.md

## docker mcp tools list
URL: https://docs.docker.com/reference/cli/docker/mcp/tools/list/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/tools/list.md

## docker mcp tools ls
URL: https://docs.docker.com/reference/cli/docker/mcp/tools/ls/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/tools/ls.md

## docker mcp version
URL: https://docs.docker.com/reference/cli/docker/mcp/version/
Markdown: https://docs.docker.com/reference/cli/docker/mcp/version.md

## docker model bench
URL: https://docs.docker.com/reference/cli/docker/model/bench/
Markdown: https://docs.docker.com/reference/cli/docker/model/bench.md

## docker model context create
URL: https://docs.docker.com/reference/cli/docker/model/context/create/
Markdown: https://docs.docker.com/reference/cli/docker/model/context/create.md

## docker model context inspect
URL: https://docs.docker.com/reference/cli/docker/model/context/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/model/context/inspect.md

## docker model context ls
URL: https://docs.docker.com/reference/cli/docker/model/context/ls/
Markdown: https://docs.docker.com/reference/cli/docker/model/context/ls.md

## docker model context rm
URL: https://docs.docker.com/reference/cli/docker/model/context/rm/
Markdown: https://docs.docker.com/reference/cli/docker/model/context/rm.md

## docker model context use
URL: https://docs.docker.com/reference/cli/docker/model/context/use/
Markdown: https://docs.docker.com/reference/cli/docker/model/context/use.md

## docker model df
URL: https://docs.docker.com/reference/cli/docker/model/df/
Markdown: https://docs.docker.com/reference/cli/docker/model/df.md

## docker model gateway
URL: https://docs.docker.com/reference/cli/docker/model/gateway/
Markdown: https://docs.docker.com/reference/cli/docker/model/gateway.md

## docker model inspect
URL: https://docs.docker.com/reference/cli/docker/model/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/model/inspect.md

## docker model install-runner
URL: https://docs.docker.com/reference/cli/docker/model/install-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/install-runner.md

## docker model launch
URL: https://docs.docker.com/reference/cli/docker/model/launch/
Markdown: https://docs.docker.com/reference/cli/docker/model/launch.md

## docker model list
URL: https://docs.docker.com/reference/cli/docker/model/list/
Markdown: https://docs.docker.com/reference/cli/docker/model/list.md

## docker model logs
URL: https://docs.docker.com/reference/cli/docker/model/logs/
Markdown: https://docs.docker.com/reference/cli/docker/model/logs.md

## docker model package
URL: https://docs.docker.com/reference/cli/docker/model/package/
Markdown: https://docs.docker.com/reference/cli/docker/model/package.md

## docker model ps
URL: https://docs.docker.com/reference/cli/docker/model/ps/
Markdown: https://docs.docker.com/reference/cli/docker/model/ps.md

## docker model pull
URL: https://docs.docker.com/reference/cli/docker/model/pull/
Markdown: https://docs.docker.com/reference/cli/docker/model/pull.md

## docker model purge
URL: https://docs.docker.com/reference/cli/docker/model/purge/
Markdown: https://docs.docker.com/reference/cli/docker/model/purge.md

## docker model push
URL: https://docs.docker.com/reference/cli/docker/model/push/
Markdown: https://docs.docker.com/reference/cli/docker/model/push.md

## docker model reinstall-runner
URL: https://docs.docker.com/reference/cli/docker/model/reinstall-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/reinstall-runner.md

## docker model requests
URL: https://docs.docker.com/reference/cli/docker/model/requests/
Markdown: https://docs.docker.com/reference/cli/docker/model/requests.md

## docker model restart-runner
URL: https://docs.docker.com/reference/cli/docker/model/restart-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/restart-runner.md

## docker model rm
URL: https://docs.docker.com/reference/cli/docker/model/rm/
Markdown: https://docs.docker.com/reference/cli/docker/model/rm.md

## docker model run
URL: https://docs.docker.com/reference/cli/docker/model/run/
Markdown: https://docs.docker.com/reference/cli/docker/model/run.md

## docker model search
URL: https://docs.docker.com/reference/cli/docker/model/search/
Markdown: https://docs.docker.com/reference/cli/docker/model/search.md

## docker model show
URL: https://docs.docker.com/reference/cli/docker/model/show/
Markdown: https://docs.docker.com/reference/cli/docker/model/show.md

## docker model skills
URL: https://docs.docker.com/reference/cli/docker/model/skills/
Markdown: https://docs.docker.com/reference/cli/docker/model/skills.md

## docker model start-runner
URL: https://docs.docker.com/reference/cli/docker/model/start-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/start-runner.md

## docker model status
URL: https://docs.docker.com/reference/cli/docker/model/status/
Markdown: https://docs.docker.com/reference/cli/docker/model/status.md

## docker model stop-runner
URL: https://docs.docker.com/reference/cli/docker/model/stop-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/stop-runner.md

## docker model tag
URL: https://docs.docker.com/reference/cli/docker/model/tag/
Markdown: https://docs.docker.com/reference/cli/docker/model/tag.md

## docker model uninstall-runner
URL: https://docs.docker.com/reference/cli/docker/model/uninstall-runner/
Markdown: https://docs.docker.com/reference/cli/docker/model/uninstall-runner.md

## docker model unload
URL: https://docs.docker.com/reference/cli/docker/model/unload/
Markdown: https://docs.docker.com/reference/cli/docker/model/unload.md

## docker model version
URL: https://docs.docker.com/reference/cli/docker/model/version/
Markdown: https://docs.docker.com/reference/cli/docker/model/version.md

## docker network connect
URL: https://docs.docker.com/reference/cli/docker/network/connect/
Markdown: https://docs.docker.com/reference/cli/docker/network/connect.md

## docker network create
URL: https://docs.docker.com/reference/cli/docker/network/create/
Markdown: https://docs.docker.com/reference/cli/docker/network/create.md

## docker network disconnect
URL: https://docs.docker.com/reference/cli/docker/network/disconnect/
Markdown: https://docs.docker.com/reference/cli/docker/network/disconnect.md

## docker network inspect
URL: https://docs.docker.com/reference/cli/docker/network/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/network/inspect.md

## docker network ls
URL: https://docs.docker.com/reference/cli/docker/network/ls/
Markdown: https://docs.docker.com/reference/cli/docker/network/ls.md

## docker network prune
URL: https://docs.docker.com/reference/cli/docker/network/prune/
Markdown: https://docs.docker.com/reference/cli/docker/network/prune.md

## docker network rm
URL: https://docs.docker.com/reference/cli/docker/network/rm/
Markdown: https://docs.docker.com/reference/cli/docker/network/rm.md

## docker node demote
URL: https://docs.docker.com/reference/cli/docker/node/demote/
Markdown: https://docs.docker.com/reference/cli/docker/node/demote.md

## docker node inspect
URL: https://docs.docker.com/reference/cli/docker/node/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/node/inspect.md

## docker node ls
URL: https://docs.docker.com/reference/cli/docker/node/ls/
Markdown: https://docs.docker.com/reference/cli/docker/node/ls.md

## docker node promote
URL: https://docs.docker.com/reference/cli/docker/node/promote/
Markdown: https://docs.docker.com/reference/cli/docker/node/promote.md

## docker node ps
URL: https://docs.docker.com/reference/cli/docker/node/ps/
Markdown: https://docs.docker.com/reference/cli/docker/node/ps.md

## docker node rm
URL: https://docs.docker.com/reference/cli/docker/node/rm/
Markdown: https://docs.docker.com/reference/cli/docker/node/rm.md

## docker node update
URL: https://docs.docker.com/reference/cli/docker/node/update/
Markdown: https://docs.docker.com/reference/cli/docker/node/update.md

## docker offload diagnose
URL: https://docs.docker.com/reference/cli/docker/offload/diagnose/
Markdown: https://docs.docker.com/reference/cli/docker/offload/diagnose.md

## docker offload start
URL: https://docs.docker.com/reference/cli/docker/offload/start/
Markdown: https://docs.docker.com/reference/cli/docker/offload/start.md

## docker offload status
URL: https://docs.docker.com/reference/cli/docker/offload/status/
Markdown: https://docs.docker.com/reference/cli/docker/offload/status.md

## docker offload stop
URL: https://docs.docker.com/reference/cli/docker/offload/stop/
Markdown: https://docs.docker.com/reference/cli/docker/offload/stop.md

## docker offload version
URL: https://docs.docker.com/reference/cli/docker/offload/version/
Markdown: https://docs.docker.com/reference/cli/docker/offload/version.md

## docker pass get
URL: https://docs.docker.com/reference/cli/docker/pass/get/
Markdown: https://docs.docker.com/reference/cli/docker/pass/get.md

## docker pass ls
URL: https://docs.docker.com/reference/cli/docker/pass/ls/
Markdown: https://docs.docker.com/reference/cli/docker/pass/ls.md

## docker pass plugins 1password purge
URL: https://docs.docker.com/reference/cli/docker/pass/plugins/1password/purge/
Markdown: https://docs.docker.com/reference/cli/docker/pass/plugins/1password/purge.md

## docker pass plugins 1password setup
URL: https://docs.docker.com/reference/cli/docker/pass/plugins/1password/setup/
Markdown: https://docs.docker.com/reference/cli/docker/pass/plugins/1password/setup.md

## docker pass plugins disable
URL: https://docs.docker.com/reference/cli/docker/pass/plugins/disable/
Markdown: https://docs.docker.com/reference/cli/docker/pass/plugins/disable.md

## docker pass plugins enable
URL: https://docs.docker.com/reference/cli/docker/pass/plugins/enable/
Markdown: https://docs.docker.com/reference/cli/docker/pass/plugins/enable.md

## docker pass plugins ls
URL: https://docs.docker.com/reference/cli/docker/pass/plugins/ls/
Markdown: https://docs.docker.com/reference/cli/docker/pass/plugins/ls.md

## docker pass rm
URL: https://docs.docker.com/reference/cli/docker/pass/rm/
Markdown: https://docs.docker.com/reference/cli/docker/pass/rm.md

## docker pass run
URL: https://docs.docker.com/reference/cli/docker/pass/run/
Markdown: https://docs.docker.com/reference/cli/docker/pass/run.md

## docker pass set
URL: https://docs.docker.com/reference/cli/docker/pass/set/
Markdown: https://docs.docker.com/reference/cli/docker/pass/set.md

## docker plugin create
URL: https://docs.docker.com/reference/cli/docker/plugin/create/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/create.md

## docker plugin disable
URL: https://docs.docker.com/reference/cli/docker/plugin/disable/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/disable.md

## docker plugin enable
URL: https://docs.docker.com/reference/cli/docker/plugin/enable/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/enable.md

## docker plugin inspect
URL: https://docs.docker.com/reference/cli/docker/plugin/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/inspect.md

## docker plugin install
URL: https://docs.docker.com/reference/cli/docker/plugin/install/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/install.md

## docker plugin ls
URL: https://docs.docker.com/reference/cli/docker/plugin/ls/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/ls.md

## docker plugin push
URL: https://docs.docker.com/reference/cli/docker/plugin/push/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/push.md

## docker plugin rm
URL: https://docs.docker.com/reference/cli/docker/plugin/rm/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/rm.md

## docker plugin set
URL: https://docs.docker.com/reference/cli/docker/plugin/set/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/set.md

## docker plugin upgrade
URL: https://docs.docker.com/reference/cli/docker/plugin/upgrade/
Markdown: https://docs.docker.com/reference/cli/docker/plugin/upgrade.md

## docker ps
URL: https://docs.docker.com/reference/cli/docker/ps/
Markdown: https://docs.docker.com/reference/cli/docker/ps.md

## docker pull
URL: https://docs.docker.com/reference/cli/docker/pull/
Markdown: https://docs.docker.com/reference/cli/docker/pull.md

## docker push
URL: https://docs.docker.com/reference/cli/docker/push/
Markdown: https://docs.docker.com/reference/cli/docker/push.md

## docker run
URL: https://docs.docker.com/reference/cli/docker/run/
Markdown: https://docs.docker.com/reference/cli/docker/run.md

## docker scout attestation add
URL: https://docs.docker.com/reference/cli/docker/scout/attestation/add/
Markdown: https://docs.docker.com/reference/cli/docker/scout/attestation/add.md

## docker scout attestation get
URL: https://docs.docker.com/reference/cli/docker/scout/attestation/get/
Markdown: https://docs.docker.com/reference/cli/docker/scout/attestation/get.md

## docker scout attestation list
URL: https://docs.docker.com/reference/cli/docker/scout/attestation/list/
Markdown: https://docs.docker.com/reference/cli/docker/scout/attestation/list.md

## docker scout cache df
URL: https://docs.docker.com/reference/cli/docker/scout/cache/df/
Markdown: https://docs.docker.com/reference/cli/docker/scout/cache/df.md

## docker scout cache prune
URL: https://docs.docker.com/reference/cli/docker/scout/cache/prune/
Markdown: https://docs.docker.com/reference/cli/docker/scout/cache/prune.md

## docker scout compare
URL: https://docs.docker.com/reference/cli/docker/scout/compare/
Markdown: https://docs.docker.com/reference/cli/docker/scout/compare.md

## docker scout config
URL: https://docs.docker.com/reference/cli/docker/scout/config/
Markdown: https://docs.docker.com/reference/cli/docker/scout/config.md

## docker scout cves
URL: https://docs.docker.com/reference/cli/docker/scout/cves/
Markdown: https://docs.docker.com/reference/cli/docker/scout/cves.md

## docker scout enroll
URL: https://docs.docker.com/reference/cli/docker/scout/enroll/
Markdown: https://docs.docker.com/reference/cli/docker/scout/enroll.md

## docker scout environment
URL: https://docs.docker.com/reference/cli/docker/scout/environment/
Markdown: https://docs.docker.com/reference/cli/docker/scout/environment.md

## docker scout help
URL: https://docs.docker.com/reference/cli/docker/scout/help/
Markdown: https://docs.docker.com/reference/cli/docker/scout/help.md

## docker scout integration configure
URL: https://docs.docker.com/reference/cli/docker/scout/integration/configure/
Markdown: https://docs.docker.com/reference/cli/docker/scout/integration/configure.md

## docker scout integration delete
URL: https://docs.docker.com/reference/cli/docker/scout/integration/delete/
Markdown: https://docs.docker.com/reference/cli/docker/scout/integration/delete.md

## docker scout integration list
URL: https://docs.docker.com/reference/cli/docker/scout/integration/list/
Markdown: https://docs.docker.com/reference/cli/docker/scout/integration/list.md

## docker scout policy publish
URL: https://docs.docker.com/reference/cli/docker/scout/policy/publish/
Markdown: https://docs.docker.com/reference/cli/docker/scout/policy/publish.md

## docker scout push
URL: https://docs.docker.com/reference/cli/docker/scout/push/
Markdown: https://docs.docker.com/reference/cli/docker/scout/push.md

## docker scout quickview
URL: https://docs.docker.com/reference/cli/docker/scout/quickview/
Markdown: https://docs.docker.com/reference/cli/docker/scout/quickview.md

## docker scout recommendations
URL: https://docs.docker.com/reference/cli/docker/scout/recommendations/
Markdown: https://docs.docker.com/reference/cli/docker/scout/recommendations.md

## docker scout repo disable
URL: https://docs.docker.com/reference/cli/docker/scout/repo/disable/
Markdown: https://docs.docker.com/reference/cli/docker/scout/repo/disable.md

## docker scout repo enable
URL: https://docs.docker.com/reference/cli/docker/scout/repo/enable/
Markdown: https://docs.docker.com/reference/cli/docker/scout/repo/enable.md

## docker scout repo list
URL: https://docs.docker.com/reference/cli/docker/scout/repo/list/
Markdown: https://docs.docker.com/reference/cli/docker/scout/repo/list.md

## docker scout sbom
URL: https://docs.docker.com/reference/cli/docker/scout/sbom/
Markdown: https://docs.docker.com/reference/cli/docker/scout/sbom.md

## docker scout stream
URL: https://docs.docker.com/reference/cli/docker/scout/stream/
Markdown: https://docs.docker.com/reference/cli/docker/scout/stream.md

## docker scout version
URL: https://docs.docker.com/reference/cli/docker/scout/version/
Markdown: https://docs.docker.com/reference/cli/docker/scout/version.md

## docker scout vex get
URL: https://docs.docker.com/reference/cli/docker/scout/vex/get/
Markdown: https://docs.docker.com/reference/cli/docker/scout/vex/get.md

## docker scout watch
URL: https://docs.docker.com/reference/cli/docker/scout/watch/
Markdown: https://docs.docker.com/reference/cli/docker/scout/watch.md

## docker search
URL: https://docs.docker.com/reference/cli/docker/search/
Markdown: https://docs.docker.com/reference/cli/docker/search.md

## docker secret create
URL: https://docs.docker.com/reference/cli/docker/secret/create/
Markdown: https://docs.docker.com/reference/cli/docker/secret/create.md

## docker secret inspect
URL: https://docs.docker.com/reference/cli/docker/secret/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/secret/inspect.md

## docker secret ls
URL: https://docs.docker.com/reference/cli/docker/secret/ls/
Markdown: https://docs.docker.com/reference/cli/docker/secret/ls.md

## docker secret rm
URL: https://docs.docker.com/reference/cli/docker/secret/rm/
Markdown: https://docs.docker.com/reference/cli/docker/secret/rm.md

## docker service create
URL: https://docs.docker.com/reference/cli/docker/service/create/
Markdown: https://docs.docker.com/reference/cli/docker/service/create.md

## docker service inspect
URL: https://docs.docker.com/reference/cli/docker/service/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/service/inspect.md

## docker service logs
URL: https://docs.docker.com/reference/cli/docker/service/logs/
Markdown: https://docs.docker.com/reference/cli/docker/service/logs.md

## docker service ls
URL: https://docs.docker.com/reference/cli/docker/service/ls/
Markdown: https://docs.docker.com/reference/cli/docker/service/ls.md

## docker service ps
URL: https://docs.docker.com/reference/cli/docker/service/ps/
Markdown: https://docs.docker.com/reference/cli/docker/service/ps.md

## docker service rm
URL: https://docs.docker.com/reference/cli/docker/service/rm/
Markdown: https://docs.docker.com/reference/cli/docker/service/rm.md

## docker service rollback
URL: https://docs.docker.com/reference/cli/docker/service/rollback/
Markdown: https://docs.docker.com/reference/cli/docker/service/rollback.md

## docker service scale
URL: https://docs.docker.com/reference/cli/docker/service/scale/
Markdown: https://docs.docker.com/reference/cli/docker/service/scale.md

## docker service update
URL: https://docs.docker.com/reference/cli/docker/service/update/
Markdown: https://docs.docker.com/reference/cli/docker/service/update.md

## docker stack config
URL: https://docs.docker.com/reference/cli/docker/stack/config/
Markdown: https://docs.docker.com/reference/cli/docker/stack/config.md

## docker stack deploy
URL: https://docs.docker.com/reference/cli/docker/stack/deploy/
Markdown: https://docs.docker.com/reference/cli/docker/stack/deploy.md

## docker stack ls
URL: https://docs.docker.com/reference/cli/docker/stack/ls/
Markdown: https://docs.docker.com/reference/cli/docker/stack/ls.md

## docker stack ps
URL: https://docs.docker.com/reference/cli/docker/stack/ps/
Markdown: https://docs.docker.com/reference/cli/docker/stack/ps.md

## docker stack rm
URL: https://docs.docker.com/reference/cli/docker/stack/rm/
Markdown: https://docs.docker.com/reference/cli/docker/stack/rm.md

## docker stack services
URL: https://docs.docker.com/reference/cli/docker/stack/services/
Markdown: https://docs.docker.com/reference/cli/docker/stack/services.md

## docker swarm ca
URL: https://docs.docker.com/reference/cli/docker/swarm/ca/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/ca.md

## docker swarm init
URL: https://docs.docker.com/reference/cli/docker/swarm/init/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/init.md

## docker swarm join-token
URL: https://docs.docker.com/reference/cli/docker/swarm/join-token/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/join-token.md

## docker swarm join
URL: https://docs.docker.com/reference/cli/docker/swarm/join/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/join.md

## docker swarm leave
URL: https://docs.docker.com/reference/cli/docker/swarm/leave/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/leave.md

## docker swarm unlock-key
URL: https://docs.docker.com/reference/cli/docker/swarm/unlock-key/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/unlock-key.md

## docker swarm unlock
URL: https://docs.docker.com/reference/cli/docker/swarm/unlock/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/unlock.md

## docker swarm update
URL: https://docs.docker.com/reference/cli/docker/swarm/update/
Markdown: https://docs.docker.com/reference/cli/docker/swarm/update.md

## docker system df
URL: https://docs.docker.com/reference/cli/docker/system/df/
Markdown: https://docs.docker.com/reference/cli/docker/system/df.md

## docker system events
URL: https://docs.docker.com/reference/cli/docker/system/events/
Markdown: https://docs.docker.com/reference/cli/docker/system/events.md

## docker system info
URL: https://docs.docker.com/reference/cli/docker/system/info/
Markdown: https://docs.docker.com/reference/cli/docker/system/info.md

## docker system prune
URL: https://docs.docker.com/reference/cli/docker/system/prune/
Markdown: https://docs.docker.com/reference/cli/docker/system/prune.md

## docker trust inspect
URL: https://docs.docker.com/reference/cli/docker/trust/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/trust/inspect.md

## docker trust key generate
URL: https://docs.docker.com/reference/cli/docker/trust/key/generate/
Markdown: https://docs.docker.com/reference/cli/docker/trust/key/generate.md

## docker trust key load
URL: https://docs.docker.com/reference/cli/docker/trust/key/load/
Markdown: https://docs.docker.com/reference/cli/docker/trust/key/load.md

## docker trust revoke
URL: https://docs.docker.com/reference/cli/docker/trust/revoke/
Markdown: https://docs.docker.com/reference/cli/docker/trust/revoke.md

## docker trust sign
URL: https://docs.docker.com/reference/cli/docker/trust/sign/
Markdown: https://docs.docker.com/reference/cli/docker/trust/sign.md

## docker trust signer add
URL: https://docs.docker.com/reference/cli/docker/trust/signer/add/
Markdown: https://docs.docker.com/reference/cli/docker/trust/signer/add.md

## docker trust signer remove
URL: https://docs.docker.com/reference/cli/docker/trust/signer/remove/
Markdown: https://docs.docker.com/reference/cli/docker/trust/signer/remove.md

## docker version
URL: https://docs.docker.com/reference/cli/docker/version/
Markdown: https://docs.docker.com/reference/cli/docker/version.md

## docker volume create
URL: https://docs.docker.com/reference/cli/docker/volume/create/
Markdown: https://docs.docker.com/reference/cli/docker/volume/create.md

## docker volume inspect
URL: https://docs.docker.com/reference/cli/docker/volume/inspect/
Markdown: https://docs.docker.com/reference/cli/docker/volume/inspect.md

## docker volume ls
URL: https://docs.docker.com/reference/cli/docker/volume/ls/
Markdown: https://docs.docker.com/reference/cli/docker/volume/ls.md

## docker volume prune
URL: https://docs.docker.com/reference/cli/docker/volume/prune/
Markdown: https://docs.docker.com/reference/cli/docker/volume/prune.md

## docker volume rm
URL: https://docs.docker.com/reference/cli/docker/volume/rm/
Markdown: https://docs.docker.com/reference/cli/docker/volume/rm.md

## docker volume update
URL: https://docs.docker.com/reference/cli/docker/volume/update/
Markdown: https://docs.docker.com/reference/cli/docker/volume/update.md

## dockerd
URL: https://docs.docker.com/reference/cli/dockerd/
Markdown: https://docs.docker.com/reference/cli/dockerd.md
Description: The daemon command description and usage

## sbx attach
URL: https://docs.docker.com/reference/cli/sbx/attach/
Markdown: https://docs.docker.com/reference/cli/sbx/attach.md

## sbx completion bash
URL: https://docs.docker.com/reference/cli/sbx/completion/bash/
Markdown: https://docs.docker.com/reference/cli/sbx/completion/bash.md

## sbx completion fish
URL: https://docs.docker.com/reference/cli/sbx/completion/fish/
Markdown: https://docs.docker.com/reference/cli/sbx/completion/fish.md

## sbx completion powershell
URL: https://docs.docker.com/reference/cli/sbx/completion/powershell/
Markdown: https://docs.docker.com/reference/cli/sbx/completion/powershell.md

## sbx completion zsh
URL: https://docs.docker.com/reference/cli/sbx/completion/zsh/
Markdown: https://docs.docker.com/reference/cli/sbx/completion/zsh.md

## sbx cp
URL: https://docs.docker.com/reference/cli/sbx/cp/
Markdown: https://docs.docker.com/reference/cli/sbx/cp.md

## sbx create claude
URL: https://docs.docker.com/reference/cli/sbx/create/claude/
Markdown: https://docs.docker.com/reference/cli/sbx/create/claude.md

## sbx create codex
URL: https://docs.docker.com/reference/cli/sbx/create/codex/
Markdown: https://docs.docker.com/reference/cli/sbx/create/codex.md

## sbx create cursor
URL: https://docs.docker.com/reference/cli/sbx/create/cursor/
Markdown: https://docs.docker.com/reference/cli/sbx/create/cursor.md

## sbx create devin
URL: https://docs.docker.com/reference/cli/sbx/create/devin/
Markdown: https://docs.docker.com/reference/cli/sbx/create/devin.md

## sbx create docker-agent
URL: https://docs.docker.com/reference/cli/sbx/create/docker-agent/
Markdown: https://docs.docker.com/reference/cli/sbx/create/docker-agent.md

## sbx create gemini
URL: https://docs.docker.com/reference/cli/sbx/create/gemini/
Markdown: https://docs.docker.com/reference/cli/sbx/create/gemini.md

## sbx create opencode
URL: https://docs.docker.com/reference/cli/sbx/create/opencode/
Markdown: https://docs.docker.com/reference/cli/sbx/create/opencode.md

## sbx create shell
URL: https://docs.docker.com/reference/cli/sbx/create/shell/
Markdown: https://docs.docker.com/reference/cli/sbx/create/shell.md

## sbx daemon log-level set
URL: https://docs.docker.com/reference/cli/sbx/daemon/log-level/set/
Markdown: https://docs.docker.com/reference/cli/sbx/daemon/log-level/set.md

## sbx daemon restart
URL: https://docs.docker.com/reference/cli/sbx/daemon/restart/
Markdown: https://docs.docker.com/reference/cli/sbx/daemon/restart.md

## sbx daemon start
URL: https://docs.docker.com/reference/cli/sbx/daemon/start/
Markdown: https://docs.docker.com/reference/cli/sbx/daemon/start.md

## sbx daemon status
URL: https://docs.docker.com/reference/cli/sbx/daemon/status/
Markdown: https://docs.docker.com/reference/cli/sbx/daemon/status.md

## sbx daemon stop
URL: https://docs.docker.com/reference/cli/sbx/daemon/stop/
Markdown: https://docs.docker.com/reference/cli/sbx/daemon/stop.md

## sbx diagnose
URL: https://docs.docker.com/reference/cli/sbx/diagnose/
Markdown: https://docs.docker.com/reference/cli/sbx/diagnose.md

## sbx env create
URL: https://docs.docker.com/reference/cli/sbx/env/create/
Markdown: https://docs.docker.com/reference/cli/sbx/env/create.md

## sbx env exec
URL: https://docs.docker.com/reference/cli/sbx/env/exec/
Markdown: https://docs.docker.com/reference/cli/sbx/env/exec.md

## sbx env plan
URL: https://docs.docker.com/reference/cli/sbx/env/plan/
Markdown: https://docs.docker.com/reference/cli/sbx/env/plan.md

## sbx env rm
URL: https://docs.docker.com/reference/cli/sbx/env/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/env/rm.md

## sbx env run
URL: https://docs.docker.com/reference/cli/sbx/env/run/
Markdown: https://docs.docker.com/reference/cli/sbx/env/run.md

## sbx exec
URL: https://docs.docker.com/reference/cli/sbx/exec/
Markdown: https://docs.docker.com/reference/cli/sbx/exec.md

## sbx kit add
URL: https://docs.docker.com/reference/cli/sbx/kit/add/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/add.md

## sbx kit builder history export
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/export/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/export.md

## sbx kit builder history inspect
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/inspect.md

## sbx kit builder history logs
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/logs/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/logs.md

## sbx kit builder history ls
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/ls.md

## sbx kit builder history rm
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/rm.md

## sbx kit builder history trace
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/history/trace/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/history/trace.md

## sbx kit builder rm
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/rm.md

## sbx kit builder status
URL: https://docs.docker.com/reference/cli/sbx/kit/builder/status/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/builder/status.md

## sbx kit inspect
URL: https://docs.docker.com/reference/cli/sbx/kit/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/inspect.md

## sbx kit pack
URL: https://docs.docker.com/reference/cli/sbx/kit/pack/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/pack.md

## sbx kit provenance
URL: https://docs.docker.com/reference/cli/sbx/kit/provenance/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/provenance.md

## sbx kit pull
URL: https://docs.docker.com/reference/cli/sbx/kit/pull/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/pull.md

## sbx kit push
URL: https://docs.docker.com/reference/cli/sbx/kit/push/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/push.md

## sbx kit sign
URL: https://docs.docker.com/reference/cli/sbx/kit/sign/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/sign.md

## sbx kit validate
URL: https://docs.docker.com/reference/cli/sbx/kit/validate/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/validate.md

## sbx kit verify
URL: https://docs.docker.com/reference/cli/sbx/kit/verify/
Markdown: https://docs.docker.com/reference/cli/sbx/kit/verify.md

## sbx login
URL: https://docs.docker.com/reference/cli/sbx/login/
Markdown: https://docs.docker.com/reference/cli/sbx/login.md

## sbx logout
URL: https://docs.docker.com/reference/cli/sbx/logout/
Markdown: https://docs.docker.com/reference/cli/sbx/logout.md

## sbx ls
URL: https://docs.docker.com/reference/cli/sbx/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/ls.md

## sbx mcp add
URL: https://docs.docker.com/reference/cli/sbx/mcp/add/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/add.md

## sbx mcp auth rm
URL: https://docs.docker.com/reference/cli/sbx/mcp/auth/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/auth/rm.md

## sbx mcp auth status
URL: https://docs.docker.com/reference/cli/sbx/mcp/auth/status/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/auth/status.md

## sbx mcp inspect
URL: https://docs.docker.com/reference/cli/sbx/mcp/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/inspect.md

## sbx mcp load
URL: https://docs.docker.com/reference/cli/sbx/mcp/load/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/load.md

## sbx mcp ls
URL: https://docs.docker.com/reference/cli/sbx/mcp/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/ls.md

## sbx mcp rm
URL: https://docs.docker.com/reference/cli/sbx/mcp/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/rm.md

## sbx mcp unload
URL: https://docs.docker.com/reference/cli/sbx/mcp/unload/
Markdown: https://docs.docker.com/reference/cli/sbx/mcp/unload.md

## sbx move
URL: https://docs.docker.com/reference/cli/sbx/move/
Markdown: https://docs.docker.com/reference/cli/sbx/move.md

## sbx policy allow network
URL: https://docs.docker.com/reference/cli/sbx/policy/allow/network/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/allow/network.md

## sbx policy check network
URL: https://docs.docker.com/reference/cli/sbx/policy/check/network/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/check/network.md

## sbx policy deny network
URL: https://docs.docker.com/reference/cli/sbx/policy/deny/network/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/deny/network.md

## sbx policy init
URL: https://docs.docker.com/reference/cli/sbx/policy/init/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/init.md

## sbx policy inspect
URL: https://docs.docker.com/reference/cli/sbx/policy/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/inspect.md

## sbx policy log
URL: https://docs.docker.com/reference/cli/sbx/policy/log/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/log.md

## sbx policy ls
URL: https://docs.docker.com/reference/cli/sbx/policy/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/ls.md

## sbx policy reset
URL: https://docs.docker.com/reference/cli/sbx/policy/reset/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/reset.md

## sbx policy rm network
URL: https://docs.docker.com/reference/cli/sbx/policy/rm/network/
Markdown: https://docs.docker.com/reference/cli/sbx/policy/rm/network.md

## sbx ports
URL: https://docs.docker.com/reference/cli/sbx/ports/
Markdown: https://docs.docker.com/reference/cli/sbx/ports.md

## sbx prune
URL: https://docs.docker.com/reference/cli/sbx/prune/
Markdown: https://docs.docker.com/reference/cli/sbx/prune.md

## sbx reset
URL: https://docs.docker.com/reference/cli/sbx/reset/
Markdown: https://docs.docker.com/reference/cli/sbx/reset.md

## sbx rm
URL: https://docs.docker.com/reference/cli/sbx/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/rm.md

## sbx run
URL: https://docs.docker.com/reference/cli/sbx/run/
Markdown: https://docs.docker.com/reference/cli/sbx/run.md

## sbx secret import
URL: https://docs.docker.com/reference/cli/sbx/secret/import/
Markdown: https://docs.docker.com/reference/cli/sbx/secret/import.md

## sbx secret ls
URL: https://docs.docker.com/reference/cli/sbx/secret/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/secret/ls.md

## sbx secret rm
URL: https://docs.docker.com/reference/cli/sbx/secret/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/secret/rm.md

## sbx secret set-custom
URL: https://docs.docker.com/reference/cli/sbx/secret/set-custom/
Markdown: https://docs.docker.com/reference/cli/sbx/secret/set-custom.md

## sbx secret set
URL: https://docs.docker.com/reference/cli/sbx/secret/set/
Markdown: https://docs.docker.com/reference/cli/sbx/secret/set.md

## sbx settings get
URL: https://docs.docker.com/reference/cli/sbx/settings/get/
Markdown: https://docs.docker.com/reference/cli/sbx/settings/get.md

## sbx settings ls
URL: https://docs.docker.com/reference/cli/sbx/settings/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/settings/ls.md

## sbx settings set
URL: https://docs.docker.com/reference/cli/sbx/settings/set/
Markdown: https://docs.docker.com/reference/cli/sbx/settings/set.md

## sbx settings unset
URL: https://docs.docker.com/reference/cli/sbx/settings/unset/
Markdown: https://docs.docker.com/reference/cli/sbx/settings/unset.md

## sbx setup ssh remove
URL: https://docs.docker.com/reference/cli/sbx/setup/ssh/remove/
Markdown: https://docs.docker.com/reference/cli/sbx/setup/ssh/remove.md

## sbx skills add
URL: https://docs.docker.com/reference/cli/sbx/skills/add/
Markdown: https://docs.docker.com/reference/cli/sbx/skills/add.md

## sbx skills import
URL: https://docs.docker.com/reference/cli/sbx/skills/import/
Markdown: https://docs.docker.com/reference/cli/sbx/skills/import.md

## sbx skills ls
URL: https://docs.docker.com/reference/cli/sbx/skills/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/skills/ls.md

## sbx skills rm
URL: https://docs.docker.com/reference/cli/sbx/skills/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/skills/rm.md

## sbx skills update
URL: https://docs.docker.com/reference/cli/sbx/skills/update/
Markdown: https://docs.docker.com/reference/cli/sbx/skills/update.md

## sbx stop
URL: https://docs.docker.com/reference/cli/sbx/stop/
Markdown: https://docs.docker.com/reference/cli/sbx/stop.md

## sbx template inspect
URL: https://docs.docker.com/reference/cli/sbx/template/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/template/inspect.md

## sbx template load
URL: https://docs.docker.com/reference/cli/sbx/template/load/
Markdown: https://docs.docker.com/reference/cli/sbx/template/load.md

## sbx template ls
URL: https://docs.docker.com/reference/cli/sbx/template/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/template/ls.md

## sbx template rm
URL: https://docs.docker.com/reference/cli/sbx/template/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/template/rm.md

## sbx template save
URL: https://docs.docker.com/reference/cli/sbx/template/save/
Markdown: https://docs.docker.com/reference/cli/sbx/template/save.md

## sbx ttl
URL: https://docs.docker.com/reference/cli/sbx/ttl/
Markdown: https://docs.docker.com/reference/cli/sbx/ttl.md

## sbx tui
URL: https://docs.docker.com/reference/cli/sbx/tui/
Markdown: https://docs.docker.com/reference/cli/sbx/tui.md

## sbx version
URL: https://docs.docker.com/reference/cli/sbx/version/
Markdown: https://docs.docker.com/reference/cli/sbx/version.md

## sbx volume create
URL: https://docs.docker.com/reference/cli/sbx/volume/create/
Markdown: https://docs.docker.com/reference/cli/sbx/volume/create.md

## sbx volume inspect
URL: https://docs.docker.com/reference/cli/sbx/volume/inspect/
Markdown: https://docs.docker.com/reference/cli/sbx/volume/inspect.md

## sbx volume ls
URL: https://docs.docker.com/reference/cli/sbx/volume/ls/
Markdown: https://docs.docker.com/reference/cli/sbx/volume/ls.md

## sbx volume rm
URL: https://docs.docker.com/reference/cli/sbx/volume/rm/
Markdown: https://docs.docker.com/reference/cli/sbx/volume/rm.md

## Compose Build Specification
URL: https://docs.docker.com/reference/compose-file/build/
Markdown: https://docs.docker.com/reference/compose-file/build.md
Description: Learn about the Compose Build Specification

## Configs top-level element
URL: https://docs.docker.com/reference/compose-file/configs/
Markdown: https://docs.docker.com/reference/compose-file/configs.md
Description: Manage and share configuration data using the configs element in Docker Compose.

## Compose Deploy Specification
URL: https://docs.docker.com/reference/compose-file/deploy/
Markdown: https://docs.docker.com/reference/compose-file/deploy.md
Description: Learn about the Compose Deploy Specification

## Compose Develop Specification
URL: https://docs.docker.com/reference/compose-file/develop/
Markdown: https://docs.docker.com/reference/compose-file/develop.md
Description: Learn about the Compose Develop Specification

## Extensions
URL: https://docs.docker.com/reference/compose-file/extension/
Markdown: https://docs.docker.com/reference/compose-file/extension.md
Description: Define and reuse custom fragments with extensions in Docker Compose

## Fragments
URL: https://docs.docker.com/reference/compose-file/fragments/
Markdown: https://docs.docker.com/reference/compose-file/fragments.md
Description: Reuse configuration with YAML anchors and fragments

## Use include to modularize Compose files
URL: https://docs.docker.com/reference/compose-file/include/
Markdown: https://docs.docker.com/reference/compose-file/include.md
Description: Reference external Compose files using the include top-level element

## Interpolation
URL: https://docs.docker.com/reference/compose-file/interpolation/
Markdown: https://docs.docker.com/reference/compose-file/interpolation.md
Description: Substitute environment variables in Docker Compose files using interpolation syntax.

## Legacy versions
URL: https://docs.docker.com/reference/compose-file/legacy-versions/
Markdown: https://docs.docker.com/reference/compose-file/legacy-versions.md

## Merge Compose files
URL: https://docs.docker.com/reference/compose-file/merge/
Markdown: https://docs.docker.com/reference/compose-file/merge.md
Description: Understand how Docker Compose merges multiple files and resolves conflicts

## Models
URL: https://docs.docker.com/reference/compose-file/models/
Markdown: https://docs.docker.com/reference/compose-file/models.md
Description: Learn about the models top-level element

## Define and manage networks in Docker Compose
URL: https://docs.docker.com/reference/compose-file/networks/
Markdown: https://docs.docker.com/reference/compose-file/networks.md
Description: Learn how to configure and control networks using the top-level networks element in Docker Compose.

## Learn how to use profiles in Docker Compose
URL: https://docs.docker.com/reference/compose-file/profiles/
Markdown: https://docs.docker.com/reference/compose-file/profiles.md
Description: Learn about profiles

## Secrets
URL: https://docs.docker.com/reference/compose-file/secrets/
Markdown: https://docs.docker.com/reference/compose-file/secrets.md
Description: Explore all the attributes the secrets top-level element can have.

## Define services in Docker Compose
URL: https://docs.docker.com/reference/compose-file/services/
Markdown: https://docs.docker.com/reference/compose-file/services.md
Description: Explore all the attributes the services top-level element can have.

## Version and name top-level elements
URL: https://docs.docker.com/reference/compose-file/version-and-name/
Markdown: https://docs.docker.com/reference/compose-file/version-and-name.md
Description: Understand when and if to set the version and name top-level element

## Define and manage volumes in Docker Compose
URL: https://docs.docker.com/reference/compose-file/volumes/
Markdown: https://docs.docker.com/reference/compose-file/volumes.md
Description: Control how volumes are declared and shared between services using the top-level volumes element.

## Dockerfile reference
URL: https://docs.docker.com/reference/dockerfile/
Markdown: https://docs.docker.com/reference/dockerfile.md

## Glossary
URL: https://docs.docker.com/reference/glossary/
Markdown: https://docs.docker.com/reference/glossary.md
Description: Glossary of terms used around Docker

## Agentic AI samples
URL: https://docs.docker.com/reference/samples/agentic-ai/
Markdown: https://docs.docker.com/reference/samples/agentic-ai.md
Description: Docker samples for agentic AI.

## AI/ML samples
URL: https://docs.docker.com/reference/samples/ai-ml/
Markdown: https://docs.docker.com/reference/samples/ai-ml.md
Description: Docker samples for AI/ML.

## Angular samples
URL: https://docs.docker.com/reference/samples/angular/
Markdown: https://docs.docker.com/reference/samples/angular.md
Description: Docker samples for Angular.

## Cloudflared samples
URL: https://docs.docker.com/reference/samples/cloudflared/
Markdown: https://docs.docker.com/reference/samples/cloudflared.md
Description: Docker samples for cloudflared.

## Django samples
URL: https://docs.docker.com/reference/samples/django/
Markdown: https://docs.docker.com/reference/samples/django.md
Description: Docker samples for Django.

## .NET samples
URL: https://docs.docker.com/reference/samples/dotnet/
Markdown: https://docs.docker.com/reference/samples/dotnet.md
Description: Docker samples for .NET.

## Elasticsearch / Logstash / Kibana samples
URL: https://docs.docker.com/reference/samples/elasticsearch/
Markdown: https://docs.docker.com/reference/samples/elasticsearch.md
Description: Docker samples for Elasticsearch, Logstash, and Kibana.

## Express samples
URL: https://docs.docker.com/reference/samples/express/
Markdown: https://docs.docker.com/reference/samples/express.md
Description: Docker samples for Express.

## FastAPI samples
URL: https://docs.docker.com/reference/samples/fastapi/
Markdown: https://docs.docker.com/reference/samples/fastapi.md
Description: Docker samples for .NET.

## Flask samples
URL: https://docs.docker.com/reference/samples/flask/
Markdown: https://docs.docker.com/reference/samples/flask.md
Description: Docker samples for Flask.

## Gitea samples
URL: https://docs.docker.com/reference/samples/gitea/
Markdown: https://docs.docker.com/reference/samples/gitea.md
Description: Docker samples for Gitea.

## Go samples
URL: https://docs.docker.com/reference/samples/go/
Markdown: https://docs.docker.com/reference/samples/go.md
Description: Docker samples for Go.

## Java samples
URL: https://docs.docker.com/reference/samples/java/
Markdown: https://docs.docker.com/reference/samples/java.md
Description: Docker samples for Java.

## JavaScript samples
URL: https://docs.docker.com/reference/samples/javascript/
Markdown: https://docs.docker.com/reference/samples/javascript.md
Description: Docker samples for JavaScript.

## MariaDB samples
URL: https://docs.docker.com/reference/samples/mariadb/
Markdown: https://docs.docker.com/reference/samples/mariadb.md
Description: Docker samples for MariaDB.

## Minecraft samples
URL: https://docs.docker.com/reference/samples/minecraft/
Markdown: https://docs.docker.com/reference/samples/minecraft.md
Description: Docker samples for Minecraft.

## MongoDB samples
URL: https://docs.docker.com/reference/samples/mongodb/
Markdown: https://docs.docker.com/reference/samples/mongodb.md
Description: Docker samples for MongoDB.

## MS-SQL samples
URL: https://docs.docker.com/reference/samples/ms-sql/
Markdown: https://docs.docker.com/reference/samples/ms-sql.md
Description: Docker samples for MS-SQL.

## MySQL samples
URL: https://docs.docker.com/reference/samples/mysql/
Markdown: https://docs.docker.com/reference/samples/mysql.md
Description: Docker samples for MySQL.

## Nextcloud samples
URL: https://docs.docker.com/reference/samples/nextcloud/
Markdown: https://docs.docker.com/reference/samples/nextcloud.md
Description: Docker samples for Nextcloud.

## NGINX samples
URL: https://docs.docker.com/reference/samples/nginx/
Markdown: https://docs.docker.com/reference/samples/nginx.md
Description: Docker samples for NGINX.

## Node.js samples
URL: https://docs.docker.com/reference/samples/nodejs/
Markdown: https://docs.docker.com/reference/samples/nodejs.md
Description: Docker samples for Node.js.

## PHP samples
URL: https://docs.docker.com/reference/samples/php/
Markdown: https://docs.docker.com/reference/samples/php.md
Description: Docker samples for PHP.

## Pi-hole samples
URL: https://docs.docker.com/reference/samples/pi-hole/
Markdown: https://docs.docker.com/reference/samples/pi-hole.md
Description: Docker samples for Pi-hole.

## Plex samples
URL: https://docs.docker.com/reference/samples/plex/
Markdown: https://docs.docker.com/reference/samples/plex.md
Description: Docker samples for Plex.

## Portainer samples
URL: https://docs.docker.com/reference/samples/portainer/
Markdown: https://docs.docker.com/reference/samples/portainer.md
Description: Docker samples for Portainer.

## PostgreSQL samples
URL: https://docs.docker.com/reference/samples/postgres/
Markdown: https://docs.docker.com/reference/samples/postgres.md
Description: Docker samples for PostgreSQL.

## Prometheus samples
URL: https://docs.docker.com/reference/samples/prometheus/
Markdown: https://docs.docker.com/reference/samples/prometheus.md
Description: Docker samples for Prometheus.

## Python samples
URL: https://docs.docker.com/reference/samples/python/
Markdown: https://docs.docker.com/reference/samples/python.md
Description: Docker samples for Python.

## Rails samples
URL: https://docs.docker.com/reference/samples/rails/
Markdown: https://docs.docker.com/reference/samples/rails.md
Description: Docker samples for Rails.

## React samples
URL: https://docs.docker.com/reference/samples/react/
Markdown: https://docs.docker.com/reference/samples/react.md
Description: Docker samples for React.

## Redis samples
URL: https://docs.docker.com/reference/samples/redis/
Markdown: https://docs.docker.com/reference/samples/redis.md
Description: Docker samples for Redis.

## Ruby samples
URL: https://docs.docker.com/reference/samples/ruby/
Markdown: https://docs.docker.com/reference/samples/ruby.md
Description: Docker samples for Ruby.

## Rust samples
URL: https://docs.docker.com/reference/samples/rust/
Markdown: https://docs.docker.com/reference/samples/rust.md
Description: Docker samples for Rust.

## Spark samples
URL: https://docs.docker.com/reference/samples/spark/
Markdown: https://docs.docker.com/reference/samples/spark.md
Description: Docker samples for Spark.

## Spring Boot samples
URL: https://docs.docker.com/reference/samples/spring/
Markdown: https://docs.docker.com/reference/samples/spring.md
Description: Docker samples for Spring Boot.

## Traefik samples
URL: https://docs.docker.com/reference/samples/traefik/
Markdown: https://docs.docker.com/reference/samples/traefik.md
Description: Docker samples for Traefik.

## TypeScript samples
URL: https://docs.docker.com/reference/samples/typescript/
Markdown: https://docs.docker.com/reference/samples/typescript.md
Description: Docker samples for TypeScript.

## Vue.js samples
URL: https://docs.docker.com/reference/samples/vuejs/
Markdown: https://docs.docker.com/reference/samples/vuejs.md
Description: Docker samples for Vue.js.

## WireGuard samples
URL: https://docs.docker.com/reference/samples/wireguard/
Markdown: https://docs.docker.com/reference/samples/wireguard.md
Description: Docker samples for WireGuard.

## WordPress samples
URL: https://docs.docker.com/reference/samples/wordpress/
Markdown: https://docs.docker.com/reference/samples/wordpress.md
Description: Docker samples for WordPress.

## Docker's product release lifecycle
URL: https://docs.docker.com/release-lifecycle/
Markdown: https://docs.docker.com/release-lifecycle.md
Description: Describes the various stages of feature lifecycle from beta to GA.

## Deprecated and retired Docker products and features
URL: https://docs.docker.com/retired/
Markdown: https://docs.docker.com/retired.md
Description: Explore deprecated and retired Docker features, products, and open source projects, including details on transitioned tools and archived initiatives.

## Advisory database sources and matching service
URL: https://docs.docker.com/scout/deep-dive/advisory-db-sources/
Markdown: https://docs.docker.com/scout/deep-dive/advisory-db-sources.md
Description: More details on the advisory database and CVE-to-package matching service behind Docker Scout analysis.

## Data collection and storage in Docker Scout
URL: https://docs.docker.com/scout/deep-dive/data-handling/
Markdown: https://docs.docker.com/scout/deep-dive/data-handling.md
Description: How Docker Scout handles image metadata

## Docker Scout image analysis
URL: https://docs.docker.com/scout/explore/analysis/
Markdown: https://docs.docker.com/scout/explore/analysis.md
Description: Docker Scout image analysis provides a detailed view into the composition of your images and the vulnerabilities that they contain

## Dashboard
URL: https://docs.docker.com/scout/explore/dashboard/
Markdown: https://docs.docker.com/scout/explore/dashboard.md
Description: The Docker Scout Dashboard helps review and share the analysis of images.

## Manage vulnerability exceptions
URL: https://docs.docker.com/scout/explore/exceptions/
Markdown: https://docs.docker.com/scout/explore/exceptions.md
Description: Exceptions let you provide additional context and documentation for how vulnerabilities affect your artifacts, and provides the ability to suppress non-applicable vulnerabilities

## Image details view
URL: https://docs.docker.com/scout/explore/image-details-view/
Markdown: https://docs.docker.com/scout/explore/image-details-view.md
Description: The Docker Scout image detail view analyzes images to show their hierarchy, layers, packages, and vulnerabilities

## Docker Scout metrics exporter
URL: https://docs.docker.com/scout/explore/metrics-exporter/
Markdown: https://docs.docker.com/scout/explore/metrics-exporter.md
Description: Learn how to scrape data from Docker Scout using Prometheus to create your own vulnerability and policy dashboards with Grafana

## Use Scout with different artifact types
URL: https://docs.docker.com/scout/how-tos/artifact-types/
Markdown: https://docs.docker.com/scout/how-tos/artifact-types.md
Description: Some of the Docker Scout commands support image references prefixes for controlling the location of the images or files that you want to analyze.

## Configure Docker Scout with environment variables
URL: https://docs.docker.com/scout/how-tos/configure-cli/
Markdown: https://docs.docker.com/scout/how-tos/configure-cli.md
Description: Configure how the behavior of Docker Scout CLI commands using these environment variables

## Create an exception using the GUI
URL: https://docs.docker.com/scout/how-tos/create-exceptions-gui/
Markdown: https://docs.docker.com/scout/how-tos/create-exceptions-gui.md
Description: Create an exception for a vulnerability in an image using the Docker Scout Dashboard or Docker Desktop.

## Create an exception using the VEX
URL: https://docs.docker.com/scout/how-tos/create-exceptions-vex/
Markdown: https://docs.docker.com/scout/how-tos/create-exceptions-vex.md
Description: Create an exception for a vulnerability in an image using VEX documents.

## Docker Scout SBOMs
URL: https://docs.docker.com/scout/how-tos/view-create-sboms/
Markdown: https://docs.docker.com/scout/how-tos/view-create-sboms.md
Description: Use Docker Scout to extract the SBOM for your project.

## Install Docker Scout
URL: https://docs.docker.com/scout/install/
Markdown: https://docs.docker.com/scout/install.md
Description: Installation instructions for the Docker Scout CLI plugin

## Integrate Docker Scout with Microsoft Azure DevOps Pipelines
URL: https://docs.docker.com/scout/integrations/ci/azure/
Markdown: https://docs.docker.com/scout/integrations/ci/azure.md
Description: How to integrate Docker Scout with Microsoft Azure DevOps Pipelines

## Integrate Docker Scout with Circle CI
URL: https://docs.docker.com/scout/integrations/ci/circle-ci/
Markdown: https://docs.docker.com/scout/integrations/ci/circle-ci.md
Description: How to integrate Docker Scout with Circle CI

## Integrate Docker Scout with GitHub Actions
URL: https://docs.docker.com/scout/integrations/ci/gha/
Markdown: https://docs.docker.com/scout/integrations/ci/gha.md
Description: How to integrate Docker Scout with GitHub Actions

## Integrate Docker Scout with GitLab CI/CD
URL: https://docs.docker.com/scout/integrations/ci/gitlab/
Markdown: https://docs.docker.com/scout/integrations/ci/gitlab.md
Description: How to integrate Docker Scout with GitLab CI

## Integrate Docker Scout with Jenkins
URL: https://docs.docker.com/scout/integrations/ci/jenkins/
Markdown: https://docs.docker.com/scout/integrations/ci/jenkins.md
Description: How to integrate Docker Scout with Jenkins

## Generic environment integration with CLI
URL: https://docs.docker.com/scout/integrations/environment/cli/
Markdown: https://docs.docker.com/scout/integrations/environment/cli.md
Description: Integrate your runtime environments with Docker Scout using the CLI client

## Integrate Docker Scout with a container registry
URL: https://docs.docker.com/scout/integrations/registry/
Markdown: https://docs.docker.com/scout/integrations/registry.md
Description: Integrate Docker Scout with any container registry using the docker scout watch CLI command

## Evaluate policies
URL: https://docs.docker.com/scout/policy/local/
Markdown: https://docs.docker.com/scout/policy/local.md
Description: Evaluate Docker Scout policies using the CLI, with built-in and custom Rego policies

## Docker Scout quickstart
URL: https://docs.docker.com/scout/quickstart/
Markdown: https://docs.docker.com/scout/quickstart.md
Description: Learn how to get started with Docker Scout to analyze images and fix vulnerabilities

## CLI release notes
URL: https://docs.docker.com/scout/release-notes/cli/
Markdown: https://docs.docker.com/scout/release-notes/cli.md

## Docker Scout release notes
URL: https://docs.docker.com/scout/release-notes/platform/
Markdown: https://docs.docker.com/scout/release-notes/platform.md
Description: Learn about the latest features of Docker Scout

## Create and manage organization access tokens
URL: https://docs.docker.com/security/access-tokens/organization-access-tokens/
Markdown: https://docs.docker.com/security/access-tokens/organization-access-tokens.md
Description: Create an organization access token, choose its repository and organization scopes, and use it in CI/CD and the Docker Hub API.

## Create and manage personal access tokens
URL: https://docs.docker.com/security/access-tokens/personal-access-tokens/
Markdown: https://docs.docker.com/security/access-tokens/personal-access-tokens.md
Description: Create a personal access token, set repository permissions and Cloud Sandboxes access, set expiration, and sign in to the Docker CLI.

## Access token reference
URL: https://docs.docker.com/security/access-tokens/reference/
Markdown: https://docs.docker.com/security/access-tokens/reference.md
Description: Personal access token permissions, Cloud Sandboxes access, organization access token scopes, and the Docker Hub API endpoints an organization access token can call.

## Manage two-factor authentication for your Docker account
URL: https://docs.docker.com/security/authentication/2fa/manage/
Markdown: https://docs.docker.com/security/authentication/2fa/manage.md
Description: Turn on two-factor authentication for your Docker account, save the recovery code, move 2FA to a new device, or turn 2FA off.

## Recover your Docker account and two-factor recovery code
URL: https://docs.docker.com/security/authentication/2fa/recover-hub-account/
Markdown: https://docs.docker.com/security/authentication/2fa/recover-hub-account.md
Description: Sign in with a recovery code, generate a new recovery code, or contact Support when you lose your authenticator app.

## Create and manage OIDC connections
URL: https://docs.docker.com/security/authentication/oidc-connections/create-manage/
Markdown: https://docs.docker.com/security/authentication/oidc-connections/create-manage.md
Description: Create and manage OIDC connections in Docker Home, then authenticate GitHub Actions to Docker Hub with docker/login-action and short-lived tokens

## Configure OIDC rulesets and subject claims
URL: https://docs.docker.com/security/authentication/oidc-connections/rulesets-claims/
Markdown: https://docs.docker.com/security/authentication/oidc-connections/rulesets-claims.md
Description: Rulesets and subject claims control which GitHub Actions workflows can push images, pull images, read public repositories, and connect to Docker Build Cloud.

## Troubleshoot OIDC connections
URL: https://docs.docker.com/security/authentication/oidc-connections/troubleshoot/
Markdown: https://docs.docker.com/security/authentication/oidc-connections/troubleshoot.md
Description: Troubleshoot common OIDC connection token-exchange errors with GitHub Actions

## Set up single sign-on
URL: https://docs.docker.com/security/authentication/single-sign-on/connect/
Markdown: https://docs.docker.com/security/authentication/single-sign-on/connect.md
Description: Connect Docker and your identity provider, test the setup, and enable enforcement.

## Manage SSO domains and connections
URL: https://docs.docker.com/security/authentication/single-sign-on/manage/
Markdown: https://docs.docker.com/security/authentication/single-sign-on/manage.md
Description: Learn how to manage single sign-on domains, connections, users, and provisioning for your organization or company.

## Troubleshoot single sign-on
URL: https://docs.docker.com/security/authentication/single-sign-on/troubleshoot-sso/
Markdown: https://docs.docker.com/security/authentication/single-sign-on/troubleshoot-sso.md
Description: Troubleshoot common Docker single sign-on configuration and authentication issues.

## Auto-provisioning
URL: https://docs.docker.com/security/provisioning/auto-provisioning/
Markdown: https://docs.docker.com/security/provisioning/auto-provisioning.md
Description: Auto-provision users by associating members to your organization when email addresses match a verified domain.

## Add and manage domains
URL: https://docs.docker.com/security/provisioning/domain-management/
Markdown: https://docs.docker.com/security/provisioning/domain-management.md
Description: Add, verify, and manage domains to control user access and enable auto-provisioning in Docker organizations

## Just-in-Time provisioning
URL: https://docs.docker.com/security/provisioning/just-in-time/
Markdown: https://docs.docker.com/security/provisioning/just-in-time.md
Description: Learn how Just-in-Time provisioning works with your SSO connection.

## Map identity provider groups to Docker teams
URL: https://docs.docker.com/security/provisioning/scim/group-mapping/
Markdown: https://docs.docker.com/security/provisioning/scim/group-mapping.md
Description: Automate Docker team membership by mapping groups from your identity provider with SSO or SCIM.

## Migrate JIT to SCIM
URL: https://docs.docker.com/security/provisioning/scim/migrate-scim/
Markdown: https://docs.docker.com/security/provisioning/scim/migrate-scim.md
Description: Move from Just-in-Time provisioning to SCIM so your identity provider manages Docker user lifecycle.

## Set up SCIM provisioning
URL: https://docs.docker.com/security/provisioning/scim/provision-scim/
Markdown: https://docs.docker.com/security/provisioning/scim/provision-scim.md
Description: Configure SCIM user provisioning and role mapping for Docker with Okta or Microsoft Entra ID.

## Troubleshoot provisioning
URL: https://docs.docker.com/security/provisioning/troubleshoot-provisioning/
Markdown: https://docs.docker.com/security/provisioning/troubleshoot-provisioning.md
Description: Troubleshoot common user provisioning issues with SCIM and Just-in-Time provisioning

## Docker core roles and permissions
URL: https://docs.docker.com/security/roles-and-permissions/core-roles/
Markdown: https://docs.docker.com/security/roles-and-permissions/core-roles.md
Description: Compare Member, Editor, and Owner permissions across Docker products

## Manage custom roles in Docker Home
URL: https://docs.docker.com/security/roles-and-permissions/custom-roles/manage/
Markdown: https://docs.docker.com/security/roles-and-permissions/custom-roles/manage.md
Description: Create, edit, assign, reassign, and delete custom roles in Docker Home for organization users and teams

## Custom role permissions reference
URL: https://docs.docker.com/security/roles-and-permissions/custom-roles/permissions-reference/
Markdown: https://docs.docker.com/security/roles-and-permissions/custom-roles/permissions-reference.md
Description: Permissions available for Docker custom roles across organization management, Docker Hub, billing, licensing, AI Governance, Docker Hardened Images, Docker Offload, and Docker Cloud Sandboxes.

## Docker security announcements
URL: https://docs.docker.com/security/security-announcements/
Markdown: https://docs.docker.com/security/security-announcements.md
Description: Security announcements for Docker products, including CVE fixes for Docker Desktop, Docker Sandboxes, and Docker Official Images.

## Docker Desktop license agreement
URL: https://docs.docker.com/subscription-billing/desktop-license/
Markdown: https://docs.docker.com/subscription-billing/desktop-license.md
Description: Learn how the Docker Subscription Service Agreement licenses Docker Desktop and when commercial use requires a paid subscription.

## Use 3D Secure authentication for Docker billing
URL: https://docs.docker.com/subscription-billing/manage/3d-secure/
Markdown: https://docs.docker.com/subscription-billing/manage/3d-secure.md
Description: Learn how 3D Secure authentication works for Docker subscription payments and how to troubleshoot verification issues.

## Update your billing details
URL: https://docs.docker.com/subscription-billing/manage/details/
Markdown: https://docs.docker.com/subscription-billing/manage/details.md
Description: Learn how to update billing details, like contact information, addresses, and notification email for Docker subscriptions.

## Billing and invoice history
URL: https://docs.docker.com/subscription-billing/manage/history/
Markdown: https://docs.docker.com/subscription-billing/manage/history.md
Description: Learn how to view your Docker billing history, understand what's on an invoice, and pay by invoice.

## Add or update a payment method
URL: https://docs.docker.com/subscription-billing/manage/payment-method/
Markdown: https://docs.docker.com/subscription-billing/manage/payment-method.md
Description: Manage cards, US bank accounts, and Stripe Link in Docker Home, and choose pay by invoice when you subscribe an organization to an annual plan.

## Manage plans
URL: https://docs.docker.com/subscription-billing/manage/plans/
Markdown: https://docs.docker.com/subscription-billing/manage/plans.md
Description: Learn how to set up, upgrade, downgrade, or cancel plans, and how to manage auto-renewal and credits.

## Sales tax exemption and VAT
URL: https://docs.docker.com/subscription-billing/manage/tax-certificate/
Markdown: https://docs.docker.com/subscription-billing/manage/tax-certificate.md
Description: Learn how Docker collects sales tax and VAT, how to submit a US tax exemption certificate, and how to add a VAT number at checkout.

## AI Governance plan
URL: https://docs.docker.com/subscription-billing/plans/ai-governance/
Markdown: https://docs.docker.com/subscription-billing/plans/ai-governance.md
Description: Manage AI Governance licenses for your organization, including purchasing, assigning, and deactivating

## DHI plans
URL: https://docs.docker.com/subscription-billing/plans/dhi/
Markdown: https://docs.docker.com/subscription-billing/plans/dhi.md
Description: Manage Docker Hardened Images Select and Enterprise repositories for organization accounts, including purchasing, adding repositories, and deactivating

## Docker Agentic Platform plans
URL: https://docs.docker.com/subscription-billing/plans/docker-agentic-platform/
Markdown: https://docs.docker.com/subscription-billing/plans/docker-agentic-platform.md
Description: Learn about Docker Agentic Platform for individual developers, including usage, pay-as-you-go billing cycle, and cancellation.

## Docker Verified Publisher plans
URL: https://docs.docker.com/subscription-billing/plans/docker-verified-publisher/
Markdown: https://docs.docker.com/subscription-billing/plans/docker-verified-publisher.md
Description: Manage DVP Starter and DVP Growth for organization accounts, including how to apply, add consuming domains, and handle billing.

## Docker plans
URL: https://docs.docker.com/subscription-billing/plans/docker/
Markdown: https://docs.docker.com/subscription-billing/plans/docker.md
Description: Learn about Docker plans that upgrade personal and organization accounts, including usage entitlements, billing cycle, and downgrade options.

## Gordon plans
URL: https://docs.docker.com/subscription-billing/plans/gordon/
Markdown: https://docs.docker.com/subscription-billing/plans/gordon.md
Description: Manage Gordon Plus, Max, and Ultra plans for personal accounts, including purchasing, upgrading, and deactivating

## Testcontainers Cloud
URL: https://docs.docker.com/tcc/
Markdown: https://docs.docker.com/tcc.md

## Testcontainers
URL: https://docs.docker.com/testcontainers/
Markdown: https://docs.docker.com/testcontainers.md
Description: Learn how to use Testcontainers to run containers programmatically in your preferred programming language.

---

# Docker guides

`https://docs.docker.com/guides`

Back [Guides](https://docs.docker.com/guides/)


- [Get started](https://docs.docker.com/get-started/)
- [Manuals](https://docs.docker.com/manuals/)
- [Reference](https://docs.docker.com/reference/)


# Guides


Step-by-step tutorials, organized by what you're trying to do.


Featured

[Explore VEX statements in Docker Hardened Images Scan a Docker Hardened Image with and without VEX and audit every suppression and its justification.](https://docs.docker.com/guides/dhi-vex-walkthrough/) [Node.js language-specific guide This guide explains how to containerize Node.js applications using Docker.](https://docs.docker.com/guides/nodejs/) [Use OpenCode with Docker Model Runner Connect OpenCode to Docker Model Runner with an OpenAI-compatible endpoint, choose coding models, and package `gpt-oss` with a larger context window.](https://docs.docker.com/guides/opencode-model-runner/)

of 71 guides


Clear filter

01


## Languages & frameworks


Containerize and develop apps in your language of choice.

[Node.js language-specific guide](https://docs.docker.com/guides/nodejs/)
This guide explains how to containerize Node.js applications using Docker. [Angular language-specific guide](https://docs.docker.com/guides/angular/)
This guide explains how to containerize Angular applications using Docker. [Bun language-specific guide](https://docs.docker.com/guides/bun/)
Learn how to containerize JavaScript applications with the Bun runtime. [.NET language-specific guide](https://docs.docker.com/guides/dotnet/)
Learn how to containerize .NET applications using Docker. [C++ language-specific guide](https://docs.docker.com/guides/cpp/)
This guide explains how to containerize C++ applications using Docker. [Deno language-specific guide](https://docs.docker.com/guides/deno/)
Learn how to containerize JavaScript applications with the Deno runtime using Docker. [Containerize a Django application](https://docs.docker.com/guides/django/)
This guide shows how to containerize a Django application using Docker.
You'll scaffold the project with uv, create a production-ready Dockerfile
using a Docker Hardened Image, then add a development stage and Compose Watch
for fast iteration. [Go language-specific guide](https://docs.docker.com/guides/golang/)
This guide teaches you how to containerize Go applications using Docker. [Java language-specific guide](https://docs.docker.com/guides/java/)
This guide demonstrates how to containerize Java applications using Docker. [Develop and Deploy Laravel applications with Docker Compose](https://docs.docker.com/guides/laravel/)
Learn how to efficiently set up Laravel development and production environments using Docker Compose. [Containerize a Next.js application](https://docs.docker.com/guides/nextjs/)
This guide explains how to containerize Next.js applications and set up
development and testing in containers. [PHP language-specific guide](https://docs.docker.com/guides/php/)
This guide explains how to containerize PHP applications using Docker. [Python language-specific guide](https://docs.docker.com/guides/python/)
This guide explains how to containerize Python applications using Docker. [R language-specific guide](https://docs.docker.com/guides/r/)
This guide details how to containerize R applications using Docker. [React.js language-specific guide](https://docs.docker.com/guides/reactjs/)
This guide explains how to containerize React.js applications using Docker. [Ruby on Rails language-specific guide](https://docs.docker.com/guides/ruby/)
This guide explains how to containerize Ruby on Rails applications using
Docker. [Rust language-specific guide](https://docs.docker.com/guides/rust/)
This guide covers how to containerize Rust applications using Docker. [Vue.js language-specific guide](https://docs.docker.com/guides/vuejs/)
This guide explains how to containerize Vue.js applications using Docker.

02


## AI


Build AI-powered apps, agents, and integrations with Docker.

[Use OpenCode with Docker Model Runner](https://docs.docker.com/guides/opencode-model-runner/)
Connect OpenCode to Docker Model Runner with an OpenAI-compatible endpoint,
choose coding models, and package `gpt-oss` with a larger context window. [Build and run agentic AI applications with Docker](https://docs.docker.com/guides/agentic-ai/)
Learn how to create AI agent applications using Docker Model Runner, and MCP Toolkit. [Connect Gemini to Grafana via MCP](https://docs.docker.com/guides/grafana-mcp-server-gemini/)
Learn how to leverage the Model Context Protocol (MCP) to interact with Grafana dashboards and datasources directly from your terminal. [Data science with JupyterLab](https://docs.docker.com/guides/jupyter/)
Use Docker to run Jupyter notebooks. [Generate Docker Compose Files with Claude Code and Docker MCP Toolkit](https://docs.docker.com/guides/genai-claude-code-mcp/)
This guide shows how to wire Claude Code to the Docker MCP Toolkit so it can search Docker Hub images and generate complete Docker Compose stacks from natural language.
You’ll enable the Docker Hub MCP server, connect Claude Code, verify MCP access, and create a Node.js + PostgreSQL stack with a conversational prompt. [Run Claude Code in a Docker Sandbox with Docker Model Runner](https://docs.docker.com/guides/claude-code-sandbox-model-runner/)
Combine Docker Sandboxes with Docker Model Runner to run Claude Code in an
isolated microVM that talks to a local model on your host through the
Anthropic-compatible API. [Run Mistral Vibe in a Docker Sandbox](https://docs.docker.com/guides/mistral-vibe-sandbox/)
Build a reusable v3 workload kit for Mistral's Vibe CLI. Vibe runs in an
isolated microVM and reaches Mistral through the sandbox proxy, so your API
key stays on the host. Verify the setup with a small coding task. [Use Claude Code with Docker Model Runner](https://docs.docker.com/guides/claude-code-model-runner/)
Connect Claude Code to Docker Model Runner with the Anthropic-compatible API,
package `gpt-oss` with a larger context window, and inspect requests. [Give sandboxed agents live web access with Firecrawl](https://docs.docker.com/guides/firecrawl-sandbox-kit/)
Compose the Firecrawl v3 mixin onto a sandbox workload. The agent gets the
Firecrawl Python SDK and a network rule for the Firecrawl API, and the
sandbox proxy adds your API key to requests, so the key never enters the
sandbox.

03


## Testing


Integration testing with real databases and services.

[Testing an ASP.NET Core web app with Testcontainers](https://docs.docker.com/guides/testcontainers-dotnet-aspnet-core/)
Learn how to test an ASP.NET Core web app using Testcontainers for .NET
with a real Microsoft SQL Server instance instead of SQLite. [Develop and test AWS Cloud applications using LocalStack and Docker](https://docs.docker.com/guides/localstack/)
This guide explains how to use Docker to run LocalStack, a local AWS cloud
stack emulator. [Testcontainers container lifecycle management using JUnit 5](https://docs.docker.com/guides/testcontainers-java-lifecycle/)
Learn different approaches to manage container lifecycle with Testcontainers
using JUnit 5 lifecycle callbacks, extension annotations, and the singleton
containers pattern. [Mocking API services in development and testing with WireMock](https://docs.docker.com/guides/wiremock/)
Mocking API services in development and testing with WireMock [Mocking OAuth services in testing with Dex](https://docs.docker.com/guides/dex/)
Mocking OAuth services in testing with Dex [Replace H2 with a real database for testing](https://docs.docker.com/guides/testcontainers-java-replace-h2/)
Replace your H2 in-memory test database with a real PostgreSQL instance
using the Testcontainers special JDBC URL — a one-line change. [Configuration of services running in a container](https://docs.docker.com/guides/testcontainers-java-service-configuration/)
Learn how to initialize and configure Docker containers for testing
by copying files into containers and executing commands inside them. [Testing a Spring Boot REST API with Testcontainers](https://docs.docker.com/guides/testcontainers-java-spring-boot-rest-api/)
Learn how to create a Spring Boot REST API with Spring Data JPA and PostgreSQL,
then test it using Testcontainers and REST Assured. [Getting started with Testcontainers for .NET](https://docs.docker.com/guides/testcontainers-dotnet-getting-started/)
Learn how to create a .NET application and test database interactions
using Testcontainers for .NET with a real PostgreSQL instance. [Getting started with Testcontainers for Go](https://docs.docker.com/guides/testcontainers-go-getting-started/)
Learn how to create a Go application and test database interactions
using Testcontainers for Go with a real PostgreSQL instance. [Getting started with Testcontainers for Java](https://docs.docker.com/guides/testcontainers-java-getting-started/)
Learn how to create a Java application and test database interactions
using Testcontainers for Java with a real PostgreSQL instance. [Getting started with Testcontainers for Node.js](https://docs.docker.com/guides/testcontainers-nodejs-getting-started/)
Learn how to create a Node.js application and test database interactions
using Testcontainers for Node.js with a real PostgreSQL instance. [Getting started with Testcontainers for Python](https://docs.docker.com/guides/testcontainers-python-getting-started/)
Learn how to create a Python application and test database interactions
using Testcontainers for Python with a real PostgreSQL instance.

04


## CI/CD


Automate builds, tests, and deployments in your pipelines.

[Introduction to Azure Pipelines with Docker](https://docs.docker.com/guides/azure-pipelines/)
Learn how to automate Docker image build and push using Azure Pipelines. [Building Compose projects with Bake](https://docs.docker.com/guides/compose-bake/)
This guide demonstrates how you can use Bake to build production-grade images for Docker Compose projects. [Introduction to GitHub Actions with Docker](https://docs.docker.com/guides/gha/)
Learn how to automate image build and push with GitHub Actions. [Mastering multi-platform builds, testing, and more with Docker Buildx Bake](https://docs.docker.com/guides/bake/)
Learn to automate Docker builds and testing with declarative configurations using Buildx Bake.

05


## Observability


Monitor application metrics and traces with containerized tools.

[Instrumenting a JavaScript App with OpenTelemetry](https://docs.docker.com/guides/opentelemetry/)
Learn how to instrument a JavaScript application using OpenTelemetry in a Dockerized environment. [Monitor a Golang application with Prometheus and Grafana](https://docs.docker.com/guides/go-prometheus-monitoring/)
Learn how to containerize a Golang application and monitor it with Prometheus and Grafana.

06


## Security


Harden images, scan vulnerabilities, and secure your supply chain.

[Explore VEX statements in Docker Hardened Images](https://docs.docker.com/guides/dhi-vex-walkthrough/)
Scan a Docker Hardened Image with and without VEX and audit every suppression and its justification. [Secure a Backstage application with Docker Hardened Images](https://docs.docker.com/guides/dhi-backstage/)
Learn how to secure a Backstage developer portal using Docker Hardened Images (DHI), handle native module compilation with better-sqlite3, add Socket Firewall protection during dependency installation, and produce a distroless runtime image using DHI customizations. [Use Docker Hardened Images with Red Hat OpenShift](https://docs.docker.com/guides/dhi-openshift/)
Learn how to deploy Docker Hardened Images (DHI) on Red Hat OpenShift, configure Security Context Constraints, handle arbitrary user ID assignment, and set file permissions for both runtime and development image variants.

07


## Databases


Run and connect to databases in containers.

[PostgreSQL specific guide](https://docs.docker.com/guides/postgresql/)
This guide explains how to containerize PostgreSQL databases using
Docker. [Pre-seeding database with schema and data at startup for development environment](https://docs.docker.com/guides/pre-seeding/)
Pre-seeding database with schema and data at startup for development environment [Use containerized databases](https://docs.docker.com/guides/databases/)
Learn how to effectively run and manage databases as containers. [Visualizing your PostgreSQL databases with pgAdmin](https://docs.docker.com/guides/pgadmin/)
Explore how to add pgAdmin to your development stack and make it as easy as possible for your teammates to navigate through your PostgreSQL databases.

08


## Services & infrastructure


Run containerized services and set up development infrastructure.

[Developing event-driven applications with Kafka and Docker](https://docs.docker.com/guides/kafka/)
This guide explains how to run Apache Kafka in Docker containers. [HTTP routing with Traefik](https://docs.docker.com/guides/traefik/)
Use Traefik to easily route traffic between multiple containers or non-containerized workloads [Introduction to ROS 2 Development with Docker](https://docs.docker.com/guides/ros2/)
This guide details how to containerize ROS 2 applications using Docker.

09


## Admin


Manage Docker organizations, users, and access controls.

[Set up your company for success with Docker](https://docs.docker.com/guides/admin-set-up/)
Get the most out of Docker by streamlining workflows, standardizing development environments, and ensuring smooth deployments across your company. [Mastering user and access management](https://docs.docker.com/guides/admin-user-management/)
Simplify user access while ensuring security and efficiency in Docker. [Using Docker with Zscaler](https://docs.docker.com/guides/zscaler/)
This guide explains how to embed Zscaler's root certificate into Docker
images, allowing containers to operate securely with Zscaler proxies and
avoid SSL errors.

10


## Hands-on labs


Interactive, guided labs you can run directly in your browser.

[Lab: AI Fundamentals for Developers](https://docs.docker.com/guides/lab-ai-fundamentals/)
Hands-on lab: Learn the four core pillars of AI application development.
Work with the Chat Completions API, prompt engineering, tool calling, and RAG
through interactive exercises. [Lab: Building an AI Product Reviewer](https://docs.docker.com/guides/lab-creating-ai-product-reviewer/)
Hands-on lab: Build an AI pipeline that classifies product reviews by
sentiment, clusters them by topic using embeddings, extracts actionable
features, and generates context-aware responses — all running locally. [Lab: Building Agentic Apps with Docker](https://docs.docker.com/guides/lab-agentic-apps/)
Hands-on lab: Build agentic apps with Docker Model Runner, MCP Gateway, and
Compose. Learn about models, tools, and agentic frameworks. [Lab: Building Container Images](https://docs.docker.com/guides/lab-building-images/)
Hands-on lab: Transform a basic Dockerfile into a production-ready image.
Master layer caching, multi-stage builds, .dockerignore, non-root users,
base image selection, and build secrets. [Lab: Container-Supported Development](https://docs.docker.com/guides/lab-container-supported-development/)
Hands-on lab: Run dependent services in containers during local development.
Start a PostgreSQL database, write a compose.yaml, and add a database
visualizer — all without installing anything on the host. [Lab: Getting Started with Docker Agent](https://docs.docker.com/guides/lab-docker-agent/)
Hands-on lab: Create, share, and orchestrate intelligent AI agents using
Docker Agent, MCP Toolkit, and Docker. [Lab: Getting Started with Docker](https://docs.docker.com/guides/lab-container-getting-started/)
Hands-on lab: Run your first containers, write a Dockerfile, build a custom
image from a Node.js app, and optionally push it to Docker Hub. [Lab: Docker Compose Quickstart](https://docs.docker.com/guides/lab-compose-quickstart/)
Hands-on lab: Define and run a multi-container app with Docker Compose.
Progress from a bare compose.yaml through health checks, live development
with watch mode, data persistence, and modular Compose file composition. [Lab: Docker MCP Gateway](https://docs.docker.com/guides/lab-mcp-gateway/)
Hands-on lab: Configure, secure, and connect MCP servers to your agentic
applications using the Docker MCP Gateway. [Lab: Container Image Attestations](https://docs.docker.com/guides/lab-attestation-basics/)
Hands-on lab: Add supply chain metadata to a container image. Generate
SBOMs and SLSA provenance with BuildKit, sign images with Cosign, and
attach OpenVEX statements to declare vulnerability exploitability status. [Lab: Migrating a Node App to Docker Hardened Images](https://docs.docker.com/guides/lab-dhi-node/)
Hands-on lab: Replace a Node.js base image with a Docker Hardened Image.
Analyze CVEs with Docker Scout, rewrite the Dockerfile to use multi-stage
builds with DHI, and explore SBOMs, VEX, and compliance attestations. [Lab: The Containerized SDLC](https://docs.docker.com/guides/lab-containerized-sdlc/)
Hands-on lab: Take a Node.js app from source to live Kubernetes deployment
using Docker Compose, Testcontainers, Gitea Actions CI/CD, and kubectl —
with containers at every stage of the SDLC.

No guides match “”.


Clear filter[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Get started

`https://docs.docker.com/get-started`

Start a new chat
Answers are generated based on the documentation.

Back [Get started](https://docs.docker.com/get-started/)


- [Guides](https://docs.docker.com/guides/)
- [Manuals](https://docs.docker.com/manuals/)
- [Reference](https://docs.docker.com/reference/)


## Install what you need

[Docker ### Install Docker Get Docker Desktop or Docker Engine for your operating system.](https://docs.docker.com/get-started/get-docker/) [Docker Sandboxes ### Install Docker Sandboxes Install the sbx command to run coding agents in isolated environments.](https://docs.docker.com/ai/sandboxes/install/)

## Choose a tutorial

[New to Docker ### Build and share a containerized application Run a container and an application stack, build an image, and share it through Docker Hub.](https://docs.docker.com/get-started/tutorials/run-an-app/) [AI developers ### Run your coding agent in a sandbox Move your existing full-autonomy coding-agent workflow into a disposable Docker Sandbox.](https://docs.docker.com/get-started/tutorials/run-an-agent/) [Administrators ### Roll out Docker to a pilot group Invite a pilot user, apply a Docker Desktop policy, and verify the managed experience.](https://docs.docker.com/get-started/tutorials/admin-set-up/)

---

# Manage licenses

`https://docs.docker.com/accounts/organization/manage/manage-licenses`

# Manage licenses


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Licenses control which organization members can use supported Docker products. As an organization owner, you manage license availability for your organization.


> Tip
>
> To learn more about product licenses, Docker Team and Business seats, and other Docker add-ons, see [Docker plans](https://docs.docker.com/subscription-billing/plans/), or [contact sales](https://www.docker.com/pricing/contact-sales/) to purchase licenses.


## [License assignment](https://docs.docker.com/accounts/organization/manage/manage-licenses#license-assignment)


You have a few options for assigning a license to a member. You can assign:


- Through a team, so every member of that team gets the license, including people who join the team later
- Through the **Members** page with the action menu, or through invitations
- By turning on automatic assignment so members receive a license when they use a supported product.


A member can use the product if they have a license from their team, from an individual assignment, or from automatic assignment. Each member uses one license per product. Assigning the same product again through another team or as an individual assignment does not consume a second license.


## [Assign licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses#assign-licenses)


Assign licenses from the **Teams** view, the **Members** view, through invitations, or with automatic assignment.


### [Teams](https://docs.docker.com/accounts/organization/manage/manage-licenses#teams)


Assigning a license to a team ensures every member of that team receives the license, including members who join the team later.


1. Sign in to [Docker Home](https://app.docker.com), then choose your organization.
2. Select **Teams** from the left navigation, then select the team name.
3. On the **Licenses** card, select the **edit** icon to open **Add licenses**.
4. Under **Licenses**, select one or more licenses.
  - Each license shows how many are available
  - The modal reports how many members receive each license5. Select **Save**.


Docker grants the license only to team members who don't already have it.


- If a member already holds that license, they keep access and the extra assignment does not consume another license.
- A product can be selected for the team only when enough licenses are available for every member of the team.


### [Members](https://docs.docker.com/accounts/organization/manage/manage-licenses#members)


1. Sign in to [Docker Home](https://app.docker.com), then choose your organization.
2. Select **Members** from the left navigation.
3. Select the **action menu** at the end of the member's row to assign or revoke an active license.
4. Optional. To assign or revoke licenses for several members, use multi-select to choose the members you want to manage, then select the **Bulk actions** menu.


### [Invitations](https://docs.docker.com/accounts/organization/manage/manage-licenses#invitations)


Assignment happens on acceptance if a license is available:


- If a license is available when they accept, Docker assigns it to them and the number of available licenses decreases by one.
- If no licenses remain when they accept, they still join your organization, but without a license.
- Docker doesn't reserve or deduct the license at invite time.


You can monitor availability on the **Licenses** page while invitations are pending.


To select licenses through invitations:


1. Sign in to [Docker Home](https://app.docker.com), then choose your organization.
2. Select **Members** from the left navigation, then select **Invite**.
3. Select **Emails or usernames**.
4. Enter the email addresses or Docker IDs of the people you want to invite, then assign their [role](https://docs.docker.com/security/roles-and-permissions/).
5. Under **Licenses (optional)**, select one or more licenses that are available to your organization.
6. Select **Invite** to send the invite.


A user can accept from the link in their invitation email or from their **Notifications Center**. For more about sending, resending, and removing invitations, including CSV file limits, see [Manage organization members](https://docs.docker.com/accounts/organization/manage/members/).


### [Automatic assignment](https://docs.docker.com/accounts/organization/manage/manage-licenses#automatic-assignment)


Automatic license assignment gives members a product license when they use a supported product. Use the **Automatic license assignment** toggle on the product's license card on the **Licenses** page. The toggle appears only when that product supports automatic assignment, so you may not see it on every card.


When the toggle is on:


- Docker Team or Business: members receive a license when they sign in to Docker Desktop.
- AI Governance: members receive a license when they sign in to [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/). The `sbx login` command provisions licenses on a first-come, first-served basis.
- Licenses are assigned until exhausted.
  - Once the available licenses are exhausted, automatic license assignment stops until more licenses are available.
  - Members can still use Docker Sandboxes or Docker Desktop, but organization policies for those products won't affect their usage.


AI Governance licenses include single sign-on (SSO) and provisioning with System for Cross-domain Identity Management (SCIM) or Just-in-Time (JIT), even if your organization doesn't have a Docker Business subscription. Members who join through SSO can receive an automatically assigned license when they use Docker Sandboxes, the same as members you invite. See [Authentication](https://docs.docker.com/security/authentication/).


*You can monitor availability on the Licenses page while invitations are
pending.*

## [View licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses#view-licenses)


The **Licenses** page shows how many licenses you have, how many are assigned, and whether those assignments are to teams or to individual members. Use it to check remaining capacity, view the members or teams that have a license, add licenses to your subscription, and turn automatic assignment on or off.


1. Sign in to [Docker Home](https://app.docker.com), then choose your organization.
2. Select **Licenses** from the left navigation.


Products you haven't purchased appear as cards with **Learn more** and **Add licenses**. Products you own show:


- Remaining licenses under **Available**, and how many of your total are assigned. To view the members who have the license, select **View all**.
- Team-assigned licenses under **Team assignment**. To view those teams, select **View teams with this license**.
- Individual assignments under **Direct assignment**


## [Remove licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses#remove-licenses)


Removing a license from a team, or [deleting a team](https://docs.docker.com/accounts/organization/manage/manage-a-team/#delete-a-team), removes that license from every member of the team, unless they hold it from a direct assignment or through membership in another team. The license returns to the available pool. The same applies when a member leaves a team. Revoking a license from one member returns that license to the available pool.


To remove licenses:


1. Sign in to [Docker Home](https://app.docker.com), then choose your organization.
2. To remove licenses from a team:
  - Select **Teams**, then select the team name.
  - On the **Licenses** card, select the **edit** icon.
  - Remove the license you no longer want the team to assign.3. To revoke a license from one member:
  - Select **Members**.
  - Use the **action menu** at the end of the member's row.
  - Select **Remove**.4. Review the confirmation message, then select **Remove license**.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Reference documentation

`https://docs.docker.com/reference`

# Reference documentation


Ask Gordon


Copy Markdown


View Markdown

---


---


This section includes the reference documentation for the Docker platform's various APIs, CLIs, drivers and specifications, and file formats.


## [File formats](https://docs.docker.com/reference#file-formats)

[### Dockerfile Defines the contents and startup behavior of a single container.](https://docs.docker.com/reference/dockerfile/) [### Compose file Defines a multi-container application.](https://docs.docker.com/reference/compose-file/)

## [Command-line interfaces (CLIs)](https://docs.docker.com/reference#command-line-interfaces-clis)

[### Docker CLI The main Docker CLI, includes all `docker` commands.](https://docs.docker.com/reference/cli/docker/) [### Compose CLI The CLI for Docker Compose, for building and running multi-container applications.](https://docs.docker.com/reference/cli/docker/compose/) [### Daemon CLI (dockerd) Persistent process that manages containers.](https://docs.docker.com/reference/cli/dockerd/)

## [Application programming interfaces (APIs)](https://docs.docker.com/reference#application-programming-interfaces-apis)

[### Sandboxes API Create cloud sandboxes, run processes, and manage sandbox resources.](https://docs.docker.com/reference/api/sandboxes/latest/) [### Engine API The main API for Docker, provides programmatic access to a daemon.](https://docs.docker.com/reference/api/engine/) [### Docker Hub API API to interact with Docker Hub.](https://docs.docker.com/reference/api/hub/latest/) [### DVP Data API API for Docker Verified Publishers to fetch analytics data.](https://docs.docker.com/reference/api/dvp/latest/) [### Registry API API for Docker Registry.](https://docs.docker.com/reference/api/registry/latest/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Share agent skills

`https://docs.docker.com/ai/sandboxes/workflows/agent-skills`

# Share agent skills


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Shared agent skills let you install skills from Git repositories or import skills from supported agents on your host for use in local sandboxes. `sbx` keeps installed skills in a persistent store that survives sandbox deletion and is shared by default with new sandboxes that run a supported agent.


> Note
>
> Shared agent skills are experimental.


## [Add skills from a repository](https://docs.docker.com/ai/sandboxes/workflows/agent-skills#add-skills-from-a-repository)


Add every skill from a Git repository:


```console
$ sbx skills add anthropics/skills
```


The repository must contain one or more valid `SKILL.md` files. You can use GitHub `owner/repository` shorthand or a Git URL, including HTTPS and SSH URLs.


To add specific skills, use `--skill` with each name or pass a comma-separated list:


```console
$ sbx skills add https://github.com/anthropics/skills --skill frontend-design --skill pdf
```


When a skill with the same name is already installed, `sbx` prompts before replacing it. Use `--force` to replace existing skills without prompts.


## [Manage installed skills](https://docs.docker.com/ai/sandboxes/workflows/agent-skills#manage-installed-skills)


List the skills in the shared store:


```console
$ sbx skills ls
```


Update every skill installed from a repository:


```console
$ sbx skills update
```


To update specific skills, pass one or more names:


```console
$ sbx skills update frontend-design pdf
```


`sbx skills update` only refreshes skills installed with `sbx skills add`. To refresh a skill imported from the host, run `sbx skills import` again. To manage it with `sbx skills update`, install it from a repository instead.


Remove one or more installed skills:


```console
$ sbx skills rm frontend-design pdf
```


`sbx` asks for confirmation before removing skills that running agents may be using. Use `--force` to skip confirmation in scripts.


## [Import skills from the host](https://docs.docker.com/ai/sandboxes/workflows/agent-skills#import-skills-from-the-host)


Preview the skills that `sbx` finds without copying them:


```console
$ sbx skills import --dry-run
```


The preview scans the host sources in the following order. The table also shows where supported agents read the shared store inside the sandbox:


| Agent | Host source | Sandbox mount target |
| --- | --- | --- |
| Codex and Devin | `~/.agents/skills` | `/home/agent/.agents/skills` |
| Claude Code | `~/.claude/skills` | `/home/agent/.claude/skills` |
| OpenCode | `~/.config/opencode/skills` | `/home/agent/.config/opencode/skills` |
| Copilot | `~/.copilot/skills` | `/home/agent/.copilot/skills` |
| Cursor | `~/.cursor/skills` | `/home/agent/.cursor/skills` |
| Droid | `~/.factory/skills` | `/home/agent/.factory/skills` |


All imported skills go into the same store, regardless of their source. If more than one source contains a skill with the same directory name, the skill from the first source in the table wins and `sbx` warns about the others.


Copy the skills into the shared store:


```console
$ sbx skills import
```


Import copies each skill directory, including directories reached through a symlink at the top level of a source. It skips symlinks inside skill directories and loose files in the source directory. If a skill depends on linked files, replace those links with files before importing it.


The final output reports the shared store path. The default locations are:


| Platform | Shared store path |
| --- | --- |
| macOS | `~/Library/Application Support/com.docker.sandboxes/sandboxes/agent-skills` |
| Linux | `~/.local/state/sandboxes/sandboxes/agent-skills` |
| Windows | `%LOCALAPPDATA%\DockerSandboxes\sandboxes\state\agent-skills` |


On Linux, `sbx` uses `$XDG_STATE_HOME/sandboxes/sandboxes/agent-skills` when `XDG_STATE_HOME` is set.


When a skill already exists in the store, `sbx` prompts before replacing it. Use `--force` to replace existing skills without prompts. Importing replaces the complete skill directory rather than merging files. Run the import command again when you want to copy updates from the host. If an import replaces a repository-installed skill, `sbx` no longer associates that skill with its repository, so `sbx skills update` won't refresh it.


*Preview the skills that sbx finds without copying them:*

## [Shared store behavior](https://docs.docker.com/ai/sandboxes/workflows/agent-skills#shared-store-behavior)


Running `sbx reset` clears the shared store.


Sandboxes created for a supported agent mount the shared store read-only by default. These sandboxes mount the contents of the store each time they start, so you can install skills before or after creating them.


Use `--skills` with `sbx run` or `sbx create` to choose the access mode when creating a sandbox:


- `readonly`: Mount the store so the agent can read skills but cannot modify them.
- `readwrite`: Mount the store so the agent can read and modify shared skills.
- `off`: Omit the shared store mount.


For example, create a sandbox without the shared store:


```console
$ sbx run --skills=off claude
```


To change the default for future sandboxes, set [`skills.defaultMode`](https://docs.docker.com/ai/sandboxes/configuration/settings/#skillsdefaultmode) to `off`, `readonly`, or `readwrite`:


```console
$ sbx settings set skills.defaultMode readonly
```


The mode is applied only when a sandbox is created. Upgrading `sbx` or changing `skills.defaultMode` leaves existing sandbox mounts unchanged. Remove and recreate a sandbox to change its mode. Sandboxes created without shared skills also need to be recreated to mount the store.


> Warning
>
> A sandbox with `readwrite` access can modify skills that other sandboxes load, including sandboxes with `readonly` access. Read-only access prevents writes from that sandbox but does not isolate it from changes to the store. The store is dedicated sandbox state, so this does not by itself execute modified skills on your host. Use `--skills=off` when creating a sandbox to keep it outside this shared trust boundary.


Some agents scan for skills when a session starts. If installed skills don't appear in an existing session, start another agent session.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Skills

`https://docs.docker.com/ai/skills`

# Docker Skills


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker Skills are Docker's official, open-source guidance for compatible AI coding agents. They help agents with Docker tasks, such as improving a Dockerfile or setting up a Compose application. The collection evolves and doesn't cover every Docker product. Browse the [repository catalog](https://github.com/docker/skills#readme) for available skills and their descriptions.


## [Get started](https://docs.docker.com/ai/skills#get-started)


1. [Install Docker Skills](https://docs.docker.com/ai/skills/install/) with a method supported by your agent, and start a new agent session.
2. Ask for an outcome in plain language, for example, “Make this Dockerfile smaller and run as a non-root user.”
3. Review the proposed changes and commands, run your project's tests, and confirm destructive operations before approving them. Skills guide the agent; they don't replace validation.


## [How agents use skills](https://docs.docker.com/ai/skills#how-agents-use-skills)


A compatible agent matches your request to descriptions of skills it can access, then loads the relevant instructions. You don't need to name a skill in your prompt. A skill is a directory containing a `SKILL.md` file that describes when and how to use it, with optional references or assets. An agent can use more than one skill when a task spans Docker products.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Usage

`https://docs.docker.com/ai/sandboxes/usage`

Back [Manuals](https://docs.docker.com/manuals/)


- [Get started](https://docs.docker.com/get-started/)
- [Guides](https://docs.docker.com/guides/)
- [Reference](https://docs.docker.com/reference/)


# Usage


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This page describes local sandboxes. For cloud commands, file transfers, ports, and expiration, see [Use cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/usage/).


Use this page as a command-oriented guide to day-to-day `sbx` operations. For scenario-based recommendations, see [Workflow patterns](https://docs.docker.com/ai/sandboxes/workflows/). For script output and the v0.48.0 CLI migration, see [CI and headless use](https://docs.docker.com/ai/sandboxes/workflows/automation/#update-scripts-for-v0480).


## [Sign in](https://docs.docker.com/ai/sandboxes/usage#sign-in)


Sign in from a terminal:


```console
$ sbx login
```


For scripts or CI runners where a browser isn't available, see [CI and headless use](https://docs.docker.com/ai/sandboxes/workflows/automation/).


## [Start, stop, and remove](https://docs.docker.com/ai/sandboxes/usage#start-stop-and-remove)


The basic workflow is [`run`](https://docs.docker.com/reference/cli/sbx/run/) to start, [`ls`](https://docs.docker.com/reference/cli/sbx/ls/) to check status, [`stop`](https://docs.docker.com/reference/cli/sbx/stop/) to pause, and [`rm`](https://docs.docker.com/reference/cli/sbx/rm/) to clean up:


```console
$ sbx run claude                    # start an agent in the current directory
$ sbx ls                            # see what's running
$ sbx stop my-sandbox               # pause it
$ sbx rm my-sandbox                 # delete it entirely
```


`sbx rm` asks for confirmation before deleting a sandbox. Use `--force` to skip the prompt. This flag also permits removal when the sandbox has an active session — an open attach, SSH connection, or in-flight SFTP transfer:


```console
$ sbx rm --force my-sandbox
```


If you need a clean slate, remove the sandbox and run it again:


```console
$ sbx stop my-sandbox
$ sbx rm my-sandbox
$ sbx run claude
```


To remove all stopped local sandboxes, use `sbx prune`. Running sandboxes are never removed. Preview the sandboxes that would be removed, or filter out sandboxes stopped within the last week:


```console
$ sbx prune --dry-run
$ sbx prune --filter until=168h
```


The `until` filter uses the time the sandbox stopped. It accepts a duration such as `168h`, an RFC 3339 timestamp, or a Unix timestamp. The older `since=<duration>` filter remains supported.


Run `sbx prune` without flags to confirm and remove all stopped sandboxes.


### [Remove a sandbox when the agent exits](https://docs.docker.com/ai/sandboxes/usage#remove-a-sandbox-when-the-agent-exits)


Pass `--rm` to `sbx run` for a throwaway session. The sandbox is removed when the agent exits, without a confirmation prompt:


```console
$ sbx run --rm claude
```


The sandbox is removed however the agent exits, and `sbx run` exits with the agent's exit status. If `sbx run` created the sandbox and the agent fails to start, the sandbox is also removed. If you reattach to an existing sandbox with `--rm`, that sandbox is removed only after its agent session finishes.


`--rm` needs an attached agent session to know when to remove the sandbox, so you can't combine it with `--detach` or `--detach-keys`.


*Run sbx prune without flags to confirm and remove all stopped sandboxes.*

## [Choose a workspace](https://docs.docker.com/ai/sandboxes/usage#choose-a-workspace)


`sbx run` mounts the current directory when you don't pass a workspace path. Pass a path to mount another directory instead:


```console
$ sbx run claude
$ sbx run claude ~/my-project
```


The first workspace path is the primary workspace. The agent starts there, and `sbx exec` uses it as the default working directory. The host directory is mounted at the same absolute path inside the sandbox. When you don't pass a path to `sbx run`, the current directory is the primary workspace.


Starting with `sbx` version 0.42.0, workspace paths are optional for `sbx create`. Omit them to create a mountless sandbox without a host workspace bind mount, then attach to the sandbox by name:


```console
$ sbx create --name scratch claude
$ sbx run --name scratch
```


In a mountless sandbox, the agent starts in the template image's working directory. Docker-provided templates use `/home/agent/workspace`. Files there persist across stops and restarts but are deleted when you remove the sandbox. Assign the sandbox a name so you can reconnect to it, and use [`sbx cp`](https://docs.docker.com/ai/sandboxes/usage#copy-files-between-host-and-sandbox) to transfer files between the sandbox and the host.


## [Reconnect and name sandboxes](https://docs.docker.com/ai/sandboxes/usage#reconnect-and-name-sandboxes)


Sandboxes persist after the agent exits. Running the same workspace path again reconnects to the existing sandbox rather than creating another sandbox:


```console
$ sbx run claude ~/my-project  # creates sandbox
$ sbx run claude ~/my-project  # reconnects to same sandbox
```


Use `--name` to give a sandbox an explicit identity:


```console
$ sbx run --name my-project claude
```


Once a named sandbox exists, reattach from any working directory with `sbx run --name`. You can omit the agent name when reattaching:


```console
$ sbx run --name my-project        # re-attaches from anywhere
$ sbx run claude --name my-project # same, with agent confirmed
```


To run multiple sandboxes against the same workspace, give each a distinct name:


```console
$ sbx run claude --name feature ~/my-project
$ sbx run claude --name spike ~/my-project
```


*Use --name to give a sandbox an explicit identity:*

*To run multiple sandboxes against the same workspace, give each a distinct
name:*

## [Create without attaching](https://docs.docker.com/ai/sandboxes/usage#create-without-attaching)


[`sbx run`](https://docs.docker.com/reference/cli/sbx/run/) creates the sandbox and attaches you to the agent. To create a sandbox with the current directory mounted, without attaching to it:


```console
$ sbx create --name my-project claude .
```


Omit the path to create a mountless sandbox instead. Attach later with `sbx run --name`:


```console
$ sbx create --name scratch claude
$ sbx run --name scratch
```


After `sbx create` finishes, the local sandbox stops automatically when no sessions keep it running. Its files and configuration persist. Running `sbx run --name <sandbox-name>` starts it again and attaches you to the agent.


### [Keep a sandbox running in the background](https://docs.docker.com/ai/sandboxes/usage#keep-a-sandbox-running-in-the-background)


To keep a sandbox running after every session ends, for example to serve an application on a [published port](https://docs.docker.com/ai/sandboxes/usage#publish-ports), start it with `sbx run --detach` (`-d`). The command starts the sandbox, prints its ID, and returns without opening an agent session:


```console
$ sbx run -d --name my-project claude .
```


A detached sandbox keeps running until you stop it with `sbx stop` or remove it with `sbx rm`. You can attach to it with `sbx run --name` or run commands with `sbx exec`, and it keeps running after those sessions end.


Running `sbx run -d --name <sandbox-name>` against an existing sandbox, such as one created with `sbx create`, switches it to detached mode permanently. To return to the default behavior, remove the sandbox and create it again.


## [Set environment variables](https://docs.docker.com/ai/sandboxes/usage#set-environment-variables)


> Note
>
> The `-e` / `--env` and `--env-file` flags require `sbx` version 0.39.0 or later.


Pass `-e` or `--env` to `sbx run` or `sbx create` to set an environment variable in the sandbox:


```console
$ sbx run -e LOG_LEVEL=debug claude
```


Specify a variable name without a value to copy its value from the host environment:


```console
$ export API_URL=https://api.example.com
$ sbx run -e API_URL claude
```


To load multiple variables, pass one or more environment files:


```console
$ sbx create --name my-project --env-file .env.sandbox claude .
```


The flags follow `docker run` precedence rules. Values passed with `-e` override values from environment files. When you pass multiple environment files, a value in a later file overrides the same variable in an earlier file.


When either command creates a sandbox, the variables are stored with the sandbox. They are also available to the agent session started by `sbx run`. When `sbx run` re-attaches to an existing sandbox, the variables apply to that agent session without changing the sandbox's stored environment. To set variables for one command instead, use `sbx exec -e` or `sbx exec --env-file`.


To persist a variable across future sessions of an existing sandbox, append an export to `/etc/sandbox-persistent.sh`:


```console
$ sbx exec <sandbox-name> bash -c "echo 'export INTERNAL_API_URL=https://api.example.com' >> /etc/sandbox-persistent.sh"
```


The `bash -c` wrapper ensures the `>>` redirect runs inside the sandbox instead of on your host. The file is sourced when Bash starts inside the sandbox, including for interactive sessions and agents started with `sbx run`. A command passed directly to `sbx exec` doesn't start a shell. Wrap that command in `bash -c` if it needs variables from the persistent environment file.


A variable added to the file only takes effect for sessions and agents started afterward. Restart a running agent, or stop and start the sandbox, to pick up the new value.


Environment variables are readable by processes inside the sandbox. For API keys and other credentials, use [`sbx secret set`](https://docs.docker.com/ai/sandboxes/configuration/credentials/#store-a-secret) for a supported service or the experimental [`sbx secret set-custom`](https://docs.docker.com/ai/sandboxes/configuration/credentials/#custom-secrets) for a credential sent to known hosts. The host-side proxy can then inject the real value without exposing it to the agent.


## [Run commands inside a sandbox](https://docs.docker.com/ai/sandboxes/usage#run-commands-inside-a-sandbox)


To get a shell inside a running sandbox, use [`sbx exec`](https://docs.docker.com/reference/cli/sbx/exec/):


```console
$ sbx exec -it <sandbox-name> bash
```


Without `--workdir`, the command starts in the sandbox's primary workspace. In a mountless sandbox, it starts in the container image's working directory.


`sbx exec` runs commands in the foreground. Detached execution (`-d` or `--detach`) isn't supported.


*To get a shell inside a running sandbox, use
sbx exec:*

## [Interactive mode](https://docs.docker.com/ai/sandboxes/usage#interactive-mode)


Running `sbx` with no subcommands opens an interactive terminal dashboard:


```console
$ sbx
```


The dashboard shows all your sandboxes as cards with live status, CPU, and memory usage. From here you can:


- **Create** a sandbox (`c`).
- **Start or stop** a sandbox (`s`).
- **Attach** to an agent session (`Enter`), same as `sbx run`.
- **Open a shell** inside the sandbox (`x`), same as `sbx exec`.
- **Remove** a sandbox (`r`).


The dashboard also includes a network governance panel where you can monitor outbound connections made by your sandboxes and manage network rules. Use `tab` to switch between the sandboxes panel and the network panel.


From the network panel you can browse connection logs, allow or block specific hosts, and add custom network rules. Press `?` to see all keyboard shortcuts.


At selection and text prompts, Enter accepts the default. Ctrl-D cancels the prompt. Declining a required confirmation returns a non-zero exit status.


*Running sbx with no subcommands opens an interactive terminal dashboard:*

## [Git workspace modes](https://docs.docker.com/ai/sandboxes/usage#git-workspace-modes)


When your primary workspace is a Git repository, choose how the sandbox receives it when you create the sandbox:


- Direct mode is the default for `sbx run`. It also applies when you pass a workspace path to `sbx create`. The agent has read-write access to your working tree, and changes appear on your host immediately.
- [Clone mode](https://docs.docker.com/ai/sandboxes/usage#clone-mode) uses `--clone`. The agent edits a separate Git clone inside the sandbox. Its changes stay there until you fetch them or the agent pushes them. Your host repository is also available at `/run/sandbox/source`, but only with read access.


For guidance on branch strategy, fetching work from a sandbox, and parallel agent workflows, see [Git workflows](https://docs.docker.com/ai/sandboxes/workflows/git/). For the security model behind each mode, see [Workspace isolation](https://docs.docker.com/ai/sandboxes/security/isolation/#workspace-isolation).


### [Clone mode](https://docs.docker.com/ai/sandboxes/usage#clone-mode)


To create a clone-mode sandbox, pass `--clone` when you run or create it:


```console
$ sbx run --clone claude .
```


You can also create the sandbox in the background and attach later:


```console
$ sbx create --clone --name my-sandbox claude .
$ sbx run --name my-sandbox
```


Clone mode has a few create-time constraints:


- Clone mode is fixed at create time. To switch an existing sandbox to clone mode, remove it and recreate it with `sbx create --clone`.
- The clone follows whichever ref your host repository has checked out at create time. No branch is created automatically.
- The primary workspace must be a Git repository. Omit `--clone` for non-Git workspaces.
- Clone mode is rejected from inside a Git worktree other than the main one. The read-only bind mount can't resolve the worktree's `.git` pointer file. Run `sbx create --clone <agent> .` from the main repository checkout instead.
- Removing a clone-mode sandbox drops the in-sandbox clone. Fetch or push any commits you want to keep before you remove it.


*To create a clone-mode sandbox, pass --clone when you run or create it:*

## [Multiple workspaces](https://docs.docker.com/ai/sandboxes/usage#multiple-workspaces)


You can mount extra directories into a sandbox alongside the main workspace. The first path is the primary workspace — the agent starts here, and the sandbox's in-container Git clone is populated from this directory if you use `--clone`. Extra workspaces are always mounted directly.


Each workspace path appears inside the sandbox at the same absolute path as on the host. Append `:ro` to mount an extra workspace read-only — useful for reference material or shared libraries the agent shouldn't modify:


```console
$ sbx run claude ~/project-a ~/shared-libs:ro ~/docs:ro
```


You can also run separate projects side-by-side. Remove unused sandboxes when you're done to reclaim disk space:


```console
$ sbx run claude ~/project-a
$ sbx run claude ~/project-b
$ sbx rm <sandbox-name>       # when finished
```


## [Copy files between host and sandbox](https://docs.docker.com/ai/sandboxes/usage#copy-files-between-host-and-sandbox)


Use [`sbx cp`](https://docs.docker.com/reference/cli/sbx/cp/) to copy files or directories between your host and a sandbox. This is useful for one-off files that aren't part of a mounted workspace, such as generated output, logs, or setup files. The sandbox path must be absolute. `sbx cp` doesn't resolve relative paths such as `.` against the sandbox's default working directory.


For example, copy files to or from the default working directory used by a Docker-provided agent template:


```console
$ sbx cp ./config.json my-sandbox:/home/agent/workspace/
$ sbx cp my-sandbox:/home/agent/workspace/output.log ./
$ sbx cp ./src/ my-sandbox:/home/agent/workspace/src
```


One side of the copy must use `SANDBOX:PATH`. Copying directly between two sandboxes isn't supported.


## [Publish ports](https://docs.docker.com/ai/sandboxes/usage#publish-ports)


Sandboxes are [network-isolated](https://docs.docker.com/ai/sandboxes/security/isolation/) — your browser or local tools can't reach a server running inside one by default. A port mapping of `8080:3000` publishes sandbox port 3000 on host port 8080.


If you know which ports you need, publish them when you create the sandbox:


```console
$ sbx run --publish 8080:3000 --name my-sandbox claude
```


For an existing sandbox, use [`sbx ports`](https://docs.docker.com/reference/cli/sbx/ports/) to forward traffic from your host. Publishing a port on a stopped local sandbox starts it first:


```console
$ sbx ports my-sandbox --publish 8080:3000
$ open http://localhost:8080
```


To let the OS pick a free host port instead of choosing one yourself, specify only the sandbox port. Then use `sbx ports` to check which host port was assigned:


```console
$ sbx ports my-sandbox --publish 3000
$ sbx ports my-sandbox
```


`sbx ls` shows active port mappings alongside each sandbox. `sbx ports` lists them in detail. The `CREATED` column shows the sandbox age, and the `STATUS` column identifies sandboxes kept running in detached mode with `(detached)`.


```console
$ sbx ls
SANDBOX      AGENT    STATUS      PORTS                       WORKSPACE         CREATED
my-sandbox   claude   ● running   127.0.0.1:8080->3000/tcp4    /home/user/proj    2m
```


To stop forwarding a port:


```console
$ sbx ports my-sandbox --unpublish 8080:3000
```


When `sbx run` re-attaches to an existing sandbox, it ignores `--publish`. Use `sbx ports` to publish ports on that sandbox. For dev server and host-service recipes, see [Local services](https://docs.docker.com/ai/sandboxes/workflows/development/#local-services).


## [What persists](https://docs.docker.com/ai/sandboxes/usage#what-persists)


While a sandbox exists, installed packages, Docker images, configuration changes, command history, and mountless workspace files all persist across stops and restarts. When you remove a sandbox, everything inside is deleted. Host workspace files, including repositories used as clone sources, and the [shared agent skills store](https://docs.docker.com/ai/sandboxes/workflows/agent-skills/) remain on your host. To capture changes in the container filesystem, [save a template](https://docs.docker.com/ai/sandboxes/usage#saving-a-sandbox-as-a-template). For a reproducible environment defined in source, [author a kit](https://docs.docker.com/ai/sandboxes/customize/author/).


## [Saving a sandbox as a template](https://docs.docker.com/ai/sandboxes/usage#saving-a-sandbox-as-a-template)


Save a sandbox's container filesystem as a reusable template image after setting up tools or configuration interactively. A template contains image content; the agent kit still supplies runtime settings such as credentials and network rules. The examples here reuse templates with built-in agents.


A saved template isn't a backup of the whole sandbox. Mounted filesystems, including host workspaces and the Docker store at `/var/lib/docker`, aren't included. Save any data from those mounts separately.


> Warning
>
> Saving a sandbox captures files in its container filesystem, including any secrets stored there. If you manually added API keys, tokens, or other credentials to the sandbox, they're embedded in the saved template and shared with anyone you distribute it to. To keep credentials out of templates, manage them with `sbx secret set` instead — the proxy injects them at runtime so they're never written to the filesystem. For more information, see [Manage credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials/).


### [Save and reuse](https://docs.docker.com/ai/sandboxes/usage#save-and-reuse)


Stop the sandbox (or let the CLI prompt you), then save it with a name and tag:


```console
$ sbx template save my-sandbox my-template:v1
```


The image is stored in the sandbox runtime's local image store. Create a new sandbox from it with the `-t` flag:


```console
$ sbx run -t my-template:v1 claude
```


### [List and remove templates](https://docs.docker.com/ai/sandboxes/usage#list-and-remove-templates)


List all saved templates:


```console
$ sbx template ls
```


Remove a template you no longer need:


```console
$ sbx template rm my-template:v1
```


### [Export and import](https://docs.docker.com/ai/sandboxes/usage#export-and-import)


To share a saved template or move it to another machine, export it as a tar file:


```console
$ sbx template save my-sandbox my-template:v1 --output my-template.tar
```


On the other machine, load the tar file and use it:


```console
$ sbx template load my-template.tar
$ sbx run -t my-template:v1 claude
```


### [Limitations](https://docs.docker.com/ai/sandboxes/usage#limitations)


Agent configuration files are always recreated when a sandbox is created. Changes to user-level agent configuration files, such as `/home/agent/.claude/settings.json` and `/home/agent/.claude.json`, do not persist in saved templates.


If the saved template was built for a different agent than the one you specify in `sbx run`, the CLI prints a warning to stderr with a suggested command. For example, saving a Claude sandbox and running it with `codex` suggests `sbx run -t my-template:v1 claude`.


*Stop the sandbox (or let the CLI prompt you), then save it with a name and
tag:*

## [Load a template](https://docs.docker.com/ai/sandboxes/usage#load-a-template)


To create a sandbox from a template image in a registry, pass its full image reference to `--template`. Use the agent the image was prepared for:


```console
$ sbx run --template docker.io/my-org/my-template:v1 claude
```


Unlike Docker commands, `sbx` doesn't automatically add the Docker Hub domain (`docker.io`) to image references. For available images and the built-in agent workflow, see [Base images](https://docs.docker.com/ai/sandboxes/customize/author/base-images/).


> Note
>
> The Docker daemon used by Docker Sandboxes pulls templates from a registry directly; it doesn't share the image store of your local Docker daemon on the host. To route Docker Hub image pulls through your organization's registry infrastructure, configure a [registry mirror](https://docs.docker.com/ai/sandboxes/configuration/registry-mirror/).


> Important
>
> For Docker Hub, `sbx` reuses your `sbx login` session to pull private images. For other registries (GitHub Container Registry, ECR, ACR, a self-hosted Nexus, and so on), store pull credentials with [`sbx secret set --registry`](https://docs.docker.com/ai/sandboxes/configuration/credentials/#registry-credentials) before running the sandbox:
>
>
>
>
>
> ```console
> $ gh auth token | sbx secret set --registry ghcr.io --password-stdin
> ```
>
>
>
> Without stored credentials, pulls from non-Docker Hub registries are anonymous and private images fail to pull.


For locally-built images, save the image to a tar and load it directly into the sandbox runtime instead of pulling from a registry:


```console
$ docker image save my-org/my-template:v1 -o my-template.tar
$ sbx template load my-template.tar
$ sbx run --template my-org/my-template:v1 claude
```


`sbx template load` imports the tar into the sandbox runtime's image store, so the image doesn't need to be reachable from a registry at sandbox creation time.


### [Template caching](https://docs.docker.com/ai/sandboxes/usage#template-caching)


When creating a sandbox, `sbx` checks the registry for the template image by default and downloads missing or updated layers. If the pull fails and the image is cached locally, it can use the cached image. Cached images persist across sandbox creation and deletion, and are cleared when you run `sbx reset`.


### [Updating agents](https://docs.docker.com/ai/sandboxes/usage#updating-agents)


Agent templates include an agent version, which can differ from the agent's latest release. Updating the `sbx` CLI or pulling an updated template doesn't update agents inside existing sandboxes.


To update an installed agent, run its documented update command inside the sandbox, either from a sandbox shell or with `sbx exec`. Restart the agent session to use the updated version. The update persists across sandbox stops and starts, but is deleted when you remove the sandbox. To reuse the updated agent in other sandboxes, [save a template](https://docs.docker.com/ai/sandboxes/usage#saving-a-sandbox-as-a-template).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Agentic Platform

`https://docs.docker.com/agentic-platform`

# Docker Agentic Platform


Ask Gordon


Copy Markdown


View Markdown

---


---


> Note
>
> Docker Agentic Platform is experimental. Features and behavior may change.


Docker Agentic Platform lets you run agents and tools in isolated cloud sandboxes. Your agent keeps working when you close the Console, disconnect your computer, or put it to sleep.


The `sbx` CLI supports both [local sandboxes](https://docs.docker.com/ai/sandboxes/get-started/) and [cloud sandboxes](https://docs.docker.com/ai/sandboxes/cloud/). These pages describe the web Console experience. The Console and CLI use different secret names; see [Cloud credentials](https://docs.docker.com/ai/sandboxes/cloud/credentials/).


In the Console, choose a [kit](https://docs.docker.com/agentic-platform/kits/) and configure the sandbox's credentials, network access, tools, and compute size. Once it starts, use its terminal to work with the agent. You can return to running or paused sandboxes from **Sandboxes**.


You can reuse these settings across sandboxes:


- [MCP](https://docs.docker.com/agentic-platform/mcp/) connects external tools.
- [Secrets](https://docs.docker.com/agentic-platform/secrets/) provide credentials without placing their values inside a sandbox.
- [Network policies](https://docs.docker.com/agentic-platform/policies/) control which hosts and services a sandbox can reach.


To begin, [activate your subscription](https://docs.docker.com/agentic-platform/signup/#activate-cloud-access), then [start a sandbox](https://docs.docker.com/agentic-platform/get-started/). You pay for compute by the second while your sandbox runs. See [Signup and billing](https://docs.docker.com/agentic-platform/signup/) for account and payment information.

[### Sign up Activate cloud access and review billing.](https://docs.docker.com/agentic-platform/signup/) [### Get started Start your first sandbox.](https://docs.docker.com/agentic-platform/get-started/) [### Kits Find a kit or run your own public kit.](https://docs.docker.com/agentic-platform/kits/) [### Sandboxes Access, pause, resume, and delete your sandboxes.](https://docs.docker.com/agentic-platform/sandboxes/) [### MCP Connect predefined or custom MCP servers.](https://docs.docker.com/agentic-platform/mcp/) [### Secrets Manage model provider and service credentials.](https://docs.docker.com/agentic-platform/secrets/) [### Policies Control outbound network access from sandboxes.](https://docs.docker.com/agentic-platform/policies/) [### FAQ Find answers about access, billing, and supported features.](https://docs.docker.com/agentic-platform/faq/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Gordon

`https://docs.docker.com/ai/gordon`

# Gordon


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Requires:
Docker Desktop
[4.74.0](https://docs.docker.com/desktop/release-notes/#4740) or later


Gordon is an AI-powered assistant that takes action on your Docker workflows. It analyzes your environment, proposes solutions, and executes commands with your permission.


## [What Gordon does](https://docs.docker.com/ai/gordon#what-gordon-does)


Gordon takes action to help you with Docker tasks:


- Explains Docker concepts and commands
- Searches Docker documentation and web resources for solutions
- Writes and modifies Dockerfiles following best practices
- Debugs container failures by reading logs and proposing fixes
- Manages containers, images, volumes, and networks


Gordon proposes every action before executing. You approve what it does.


## [Where to use Gordon](https://docs.docker.com/ai/gordon#where-to-use-gordon)


Gordon is available on four surfaces:


- Open the Gordon view from the Docker Desktop sidebar to run Docker commands with your approval. See [Using Gordon in Docker Desktop](https://docs.docker.com/ai/gordon/how-to/docker-desktop/).
- Run `docker ai` in the terminal to use the full assistant from the command line. See [Using Gordon via CLI](https://docs.docker.com/ai/gordon/how-to/cli/).
- Select the Gordon icon on any repository page at [hub.docker.com](https://hub.docker.com) to ask about a repository's images, tags, and metadata. Hand off to Docker Desktop to take action.
- Select the Gordon icon on any page at [docs.docker.com](https://docs.docker.com) to ask Docker questions.


Docker Desktop and the CLI count against your Gordon plan's [usage limits](https://docs.docker.com/ai/gordon/usage-limits/). Gordon on Docker Hub and docs.docker.com is free and does not require a Docker account or a Docker Desktop install. It has its own shared public usage limit and does not access your Docker environment.


## [Get started](https://docs.docker.com/ai/gordon#get-started)


### [Prerequisites](https://docs.docker.com/ai/gordon#prerequisites)


Before you begin:


- Docker Desktop 4.74 or later
- Sign in to your Docker account


> Note
>
> Gordon is enabled by default for signed-in Docker users. If your account belongs to an organization with a Business subscription, access requires two additional steps:
>
>
>
> 1. Contact Docker Support to activate Gordon for your organization. Docker will confirm when activation is complete.
> 2. Once confirmed, an organization administrator must turn on Gordon via [Settings Management](https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/). Set **Enable Gordon** to **Enabled** or **Always enabled**. Ensure all Settings Management prerequisites are met for the setting to take effect on Docker Desktop clients.


### [Quick start](https://docs.docker.com/ai/gordon#quick-start)


Docker Desktop


CLI

1. Open Docker Desktop.
2. Select **Gordon** in the sidebar.
3. Select your project directory.
4. Type a question: "What containers are running?" ![Gordon running in Docker Desktop](https://docs.docker.com/ai/gordon/images/gordon_gui.avif)
5. Review Gordon's proposed actions and approve.


1. Open your terminal and run: ```console $ docker ai ``` This opens the Terminal User Interface (TUI) for Gordon.
2. Type a question: "what containers are running?" and press Enter. ![Gordon running in the terminal](https://docs.docker.com/ai/gordon/images/gordon_tui.avif)
3. Review Gordon's proposed actions and approve by typing `y`.


### [Permissions](https://docs.docker.com/ai/gordon#permissions)


By default, Gordon asks for approval before executing actions. You can approve individual actions or allow all actions for the current session.

![Gordon permission request](https://docs.docker.com/ai/gordon/images/gordon_permissions_prompt.avif)


Permissions reset for each session. To configure default permissions or enable auto-approve mode, see [Permissions](https://docs.docker.com/ai/gordon/how-to/permissions/).


### [Try these examples](https://docs.docker.com/ai/gordon#try-these-examples)


Container inspection:


```console
$ docker ai "show me logs from my nginx container"
```


Dockerfile review:


```console
$ docker ai "review my Dockerfile for best practices"
```


Image management:


```console
$ docker ai "list my local images and their sizes"
```[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker MCP Catalog and Toolkit

`https://docs.docker.com/ai/mcp-catalog-and-toolkit`

# Docker MCP Catalog and Toolkit


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Availability:
Beta


[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is an open protocol that standardizes how AI applications access external tools and data sources. By connecting LLMs to local development tools, databases, APIs, and other resources, MCP extends their capabilities beyond their base training.


The challenge is that running MCP servers locally creates operational friction. Each server requires separate installation and configuration for every application you use. You run untrusted code directly on your machine, manage updates manually, and troubleshoot dependency conflicts yourself. Configure a GitHub server for Claude, then configure it again for Cursor, and so on. Each time you manage credentials, permissions, and environment setup.


## [Docker MCP features](https://docs.docker.com/ai/mcp-catalog-and-toolkit#docker-mcp-features)


The [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) and [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) solve these challenges through centralized management. Instead of configuring each server for every AI application separately, you set things up once and connect all your clients to it. The workflow centers on three concepts: catalogs, profiles, and clients.

![MCP overview](https://docs.docker.com/ai/mcp-catalog-and-toolkit/images/mcp_toolkit.avif)


[Catalogs](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/) are curated collections of MCP servers. The Docker MCP Catalog provides 300+ verified servers packaged as container images with versioning, provenance, and security updates. Organizations can create [custom catalogs](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/#custom-catalogs) with approved servers for their teams.


[Profiles](https://docs.docker.com/ai/mcp-catalog-and-toolkit/profiles/) organize servers into named collections for different projects. Your "web-dev" profile might use GitHub and Playwright; your "backend" profile, database tools. Profiles support both containerized servers from catalogs and remote MCP servers. Configure a profile once, then share it across clients or with your team.


Clients are the AI applications that connect to your profiles. Claude Code, Cursor, Zed, and others connect through the MCP Gateway, which routes requests to the right server and handles authentication and lifecycle management.


> Note
>
> MCP Gateway as part of Docker AI Governance is an invite-only feature. [Contact Docker Sales](https://www.docker.com/pricing/contact-sales/) to learn more.


## [Learn more](https://docs.docker.com/ai/mcp-catalog-and-toolkit#learn-more)

[### Get started with MCP Toolkit Learn how to quickly install and use the MCP Toolkit to set up servers and clients.](https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/) [### MCP Catalog Browse Docker's curated collection of verified MCP servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/) [### MCP Profiles Organize servers into profiles for different projects and share configurations](https://docs.docker.com/ai/mcp-catalog-and-toolkit/profiles/) [### MCP Toolkit Use Docker Desktop's UI to discover, configure, and manage MCP servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) [### MCP Gateway Use the CLI and Gateway to run MCP servers with custom configurations](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) [### Dynamic MCP Discover and add MCP servers on-demand using natural language. This feature is experimental.](https://docs.docker.com/ai/mcp-catalog-and-toolkit/dynamic-mcp/) [### Security FAQs Common questions about MCP security, credentials, and server verification](https://docs.docker.com/ai/mcp-catalog-and-toolkit/faqs/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Model Runner

`https://docs.docker.com/ai/model-runner`

# Docker Model Runner


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Requires:
Docker Engine or Docker Desktop (Windows) 4.41+ or Docker Desktop (MacOS) 4.40+
For:
See Requirements section below

Docker Model Runner (DMR) makes it easy to manage, run, and deploy AI models using Docker. Designed for developers, Docker Model Runner streamlines the process of pulling, running, and serving large language models (LLMs) and other AI models directly from Docker Hub, any OCI-compliant registry, or [Hugging Face](https://huggingface.co/).


With seamless integration into Docker Desktop and Docker Engine, you can serve models via OpenAI and Ollama-compatible APIs, package GGUF files as OCI Artifacts, and interact with models from both the command line and graphical interface.


Whether you're building generative AI applications, experimenting with machine learning workflows, or integrating AI into your software development lifecycle, Docker Model Runner provides a consistent, secure, and efficient way to work with AI models locally.


## [Key features](https://docs.docker.com/ai/model-runner#key-features)


- [Pull and push models to and from Docker Hub or any OCI-compliant registry](https://hub.docker.com/u/ai)
- [Pull models from Hugging Face](https://huggingface.co/)
- Serve models on [OpenAI and Ollama-compatible APIs](https://docs.docker.com/ai/model-runner/api-reference/) for easy integration with existing apps
- Support for [llama.cpp, vLLM, and Diffusers inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) (vLLM and Diffusers on Linux with NVIDIA GPUs)
- [Generate images from text prompts](https://docs.docker.com/ai/model-runner/inference-engines/#diffusers) using Stable Diffusion models with the Diffusers backend
- Package GGUF and Safetensors files as OCI Artifacts and publish them to any Container Registry
- Run and interact with AI models directly from the command line or from the Docker Desktop GUI
- [Connect to AI coding tools](https://docs.docker.com/ai/model-runner/ide-integrations/) like Cline, Continue, Cursor, and Aider
- [Configure context size and model parameters](https://docs.docker.com/ai/model-runner/configuration/) to tune performance
- [Set up Open WebUI](https://docs.docker.com/ai/model-runner/openwebui-integration/) for a ChatGPT-like web interface
- Manage local models and display logs
- Display prompt and response details
- Conversational context support for multi-turn interactions


## [Requirements](https://docs.docker.com/ai/model-runner#requirements)


Docker Model Runner is supported on the following platforms:


Windows


MacOS


Linux

Windows(amd64):


- NVIDIA GPUs
- NVIDIA drivers 576.57+


Windows(arm64):


- OpenCL for Adreno
- Qualcomm Adreno GPU (6xx series and later) > Note > > Some llama.cpp features might not be fully supported on the 6xx series.


- Apple Silicon


Docker Engine only:


- Supports CPU, NVIDIA (CUDA), AMD (ROCm), and Vulkan backends
- Requires NVIDIA driver 575.57.08+ when using NVIDIA GPUs


## [How Docker Model Runner works](https://docs.docker.com/ai/model-runner#how-docker-model-runner-works)


Models are pulled from Docker Hub, an OCI-compliant registry, or [Hugging Face](https://huggingface.co/) the first time you use them and are stored locally. They load into memory only at runtime when a request is made, and unload when not in use to optimize resources. Because models can be large, the initial pull may take some time. After that, they're cached locally for faster access. You can interact with the model using [OpenAI and Ollama-compatible APIs](https://docs.docker.com/ai/model-runner/api-reference/).


### [Inference engines](https://docs.docker.com/ai/model-runner#inference-engines)


Docker Model Runner supports three inference engines:


| Engine | Best for | Model format |
| --- | --- | --- |
| [llama.cpp](https://docs.docker.com/ai/model-runner/inference-engines/#llamacpp) | Local development, resource efficiency | GGUF (quantized) |
| [vLLM](https://docs.docker.com/ai/model-runner/inference-engines/#vllm) | Production, high throughput | Safetensors |
| [Diffusers](https://docs.docker.com/ai/model-runner/inference-engines/#diffusers) | Image generation (Stable Diffusion) | Safetensors |


llama.cpp is the default engine and works on all platforms. vLLM requires NVIDIA GPUs and is supported on Linux x86_64 and Windows with WSL2. Diffusers enables image generation and requires NVIDIA GPUs on Linux (x86_64 or ARM64). See [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) for detailed comparison and setup.


### [Context size](https://docs.docker.com/ai/model-runner#context-size)


Models have a configurable context size (context length) that determines how many tokens they can process. The default varies by model but is typically 2,048-8,192 tokens. You can adjust this per-model:


```console
$ docker model configure --context-size 8192 ai/qwen2.5-coder
```


See [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) for details on context size and other parameters.


> Tip
>
> Using Testcontainers or Docker Compose? [Testcontainers for Java](https://java.testcontainers.org/modules/docker_model_runner/) and [Go](https://golang.testcontainers.org/modules/dockermodelrunner/), and [Docker Compose](https://docs.docker.com/ai/compose/models-and-compose/) support Docker Model Runner.


*See Configuration options for details on context size and other parameters.*

## [Security and isolation](https://docs.docker.com/ai/model-runner#security-and-isolation)


### [Execution environment](https://docs.docker.com/ai/model-runner#execution-environment)


Docker Model Runner isolates inference engines from your host:


- On Linux, Docker Model Runner and its inference engines, such as Diffusers, run inside a container, which provides the isolation boundary.
- On macOS and Windows, the engines don't run inside a container, so Docker Model Runner runs them in a sandboxed environment (seatbelt/sandbox-exec and Job Objects respectively)


### [Networking](https://docs.docker.com/ai/model-runner#networking)


The Model Runner API is not authenticated. Any client that can reach it, including other containers on the same Docker network, can pull, load, and run models, and send inference requests.


## [Known issues](https://docs.docker.com/ai/model-runner#known-issues)


### [`docker model` is not recognised](https://docs.docker.com/ai/model-runner#docker-model-is-not-recognised)


If you run a Docker Model Runner command and see:


```text
docker: 'model' is not a docker command
```


It means Docker can't find the plugin because it's not in the expected CLI plugins directory.


To fix this, create a symlink so Docker can detect it:


```console
$ ln -s /Applications/Docker.app/Contents/Resources/cli-plugins/docker-model ~/.docker/cli-plugins/docker-model
```


Once linked, rerun the command.


## [Privacy and data collection](https://docs.docker.com/ai/model-runner#privacy-and-data-collection)


Docker Model Runner respects your privacy settings in Docker Desktop. Data collection is controlled by the **Send usage statistics** setting:


- **Disabled**: No usage data is collected
- **Enabled**: Only minimal, non-personal data is collected:
  - [Model names](https://github.com/docker/model-runner/blob/eb76b5defb1a598396f99001a500a30bbbb48f01/pkg/metrics/metrics.go#L96) (via HEAD requests to Docker Hub)
  - User agent information
  - Whether requests originate from the host or containers


When using Docker Model Runner with Docker Engine, HEAD requests to Docker Hub are made to track model names, regardless of any settings.


No prompt content, responses, or personally identifiable information is ever collected.


## [Share feedback](https://docs.docker.com/ai/model-runner#share-feedback)


Thanks for trying out Docker Model Runner. To report bugs or request features, [open an issue on GitHub](https://github.com/docker/model-runner/issues). You can also give feedback through the **Give feedback** link next to the **Enable Docker Model Runner** setting.


## [Next steps](https://docs.docker.com/ai/model-runner#next-steps)


- [Get started with DMR](https://docs.docker.com/ai/model-runner/get-started/) - Enable DMR and run your first model
- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - OpenAI and Ollama-compatible API documentation
- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Context size and runtime parameters
- [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) - llama.cpp, vLLM, and Diffusers details
- [IDE integrations](https://docs.docker.com/ai/model-runner/ide-integrations/) - Connect Cline, Continue, Cursor, and more
- [Open WebUI integration](https://docs.docker.com/ai/model-runner/openwebui-integration/) - Set up a web chat interface[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Agent

`https://docs.docker.com/ai/docker-agent`

# Docker Agent


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


[Docker Agent](https://github.com/docker/docker-agent) is an open-source framework for building teams of specialized AI agents. Instead of prompting one generalist model, you define agents with specific roles and instructions that collaborate to solve problems. Run these agent teams from your terminal using any LLM provider.


> Note
>
> Docker Agent is a framework for building and running custom agent teams. For Docker's built-in AI assistant, see [Gordon](https://docs.docker.com/ai/gordon/) (`docker ai`).


## [Why agent teams](https://docs.docker.com/ai/docker-agent#why-agent-teams)


One agent handling complex work means constant context-switching. Split the work across focused agents instead - each handles what it's best at. Docker Agent manages the coordination.


Here's a two-agent team that debugs problems:


```yaml
agents:
  root:
    model: openai/gpt-5-mini # Change to the model that you want to use
    description: Bug investigator
    instruction: |
      Analyze error messages, stack traces, and code to find bug root causes.
      Explain what's wrong and why it's happening.
      Delegate fix implementation to the fixer agent.
    sub_agents: [fixer]
    toolsets:
      - type: filesystem
      - type: mcp
        ref: docker:duckduckgo

  fixer:
    model: anthropic/claude-sonnet-4-5 # Change to the model that you want to use
    description: Fix implementer
    instruction: |
      Write fixes for bugs diagnosed by the investigator.
      Make minimal, targeted changes and add tests to prevent regression.
    toolsets:
      - type: filesystem
      - type: shell
```


The root agent investigates and explains the problem. When it understands the issue, it hands off to `fixer` for implementation. Each agent stays focused on its specialty.


## [Installation](https://docs.docker.com/ai/docker-agent#installation)


Docker Agent is included in Docker Desktop 4.63 and later. In Docker Desktop versions 4.49 through 4.62, this feature was called cagent.


For Docker Engine users or custom installations:


- **Homebrew**: `brew install docker-agent`
- **Winget**: `winget install Docker.Agent`
- **Pre-built binaries**: [GitHub releases](https://github.com/docker/docker-agent/releases)
- **From source**: See the [Docker Agent repository](https://github.com/docker/docker-agent?tab=readme-ov-file#build-from-source)


The `docker-agent` binary should be copied to `~/.docker/cli-plugins` and then can be used with the `docker agent` command. Alternatively, it can be used as a standalone binary.


## [Get started](https://docs.docker.com/ai/docker-agent#get-started)


Try the bug analyzer team:


1. Set your API key for the model provider you want to use: ```console $ export ANTHROPIC_API_KEY=<your_key> # For Claude models $ export OPENAI_API_KEY=<your_key> # For OpenAI models $ export GOOGLE_API_KEY=<your_key> # For Gemini models ```
2. Save the [example configuration](https://docs.docker.com/ai/docker-agent#why-agent-teams) as `debugger.yaml`.
3. Run your agent team: ```console $ docker agent run debugger.yaml ```


You'll see a prompt where you can describe bugs or paste error messages. The investigator analyzes the problem, then hands off to the fixer for implementation.


## [How it works](https://docs.docker.com/ai/docker-agent#how-it-works)


You interact with the *root agent*, which can delegate work to sub-agents you define. Each agent:


- Uses its own model and parameters
- Has its own context (agents don't share knowledge)
- Can access built-in tools like todo lists, memory, and task delegation
- Can use external tools via [MCP servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)


The root agent delegates tasks to agents listed under `sub_agents`. Sub-agents can have their own sub-agents for deeper hierarchies.


## [Configuration options](https://docs.docker.com/ai/docker-agent#configuration-options)


Agent configurations are YAML files. A basic structure looks like this:


```yaml
agents:
  root:
    model: claude-sonnet-4-0
    description: Brief role summary
    instruction: |
      Detailed instructions for this agent...
    sub_agents: [helper]

  helper:
    model: gpt-5-mini
    description: Specialist agent role
    instruction: |
      Instructions for the helper agent...
```


You can also configure model settings (like context limits), tools (including MCP servers), and more. See the [configuration reference](https://docs.docker.com/ai/docker-agent/configuration/overview/) for complete details.


## [Share agent teams](https://docs.docker.com/ai/docker-agent#share-agent-teams)


Agent configurations are packaged as OCI artifacts. Push and pull them like container images:


```console
$ docker agent share push ./debugger.yaml myusername/debugger
$ docker agent share pull myusername/debugger
```


Use Docker Hub or any OCI-compatible registry. Pushing creates the repository if it doesn't exist yet.


## [What's next](https://docs.docker.com/ai/docker-agent#whats-next)


- Follow the [quickstart](https://docs.docker.com/ai/docker-agent/getting-started/quickstart/) to build your first agent
- Learn [best practices](https://docs.docker.com/ai/docker-agent/guides/tips/) for building effective agents
- Integrate Docker Agent with your [editor](https://docs.docker.com/ai/docker-agent/features/acp/) or use agents as [tools in MCP clients](https://docs.docker.com/ai/docker-agent/tools/mcp/)
- Browse example agent configurations in the [Docker Agent repository](https://github.com/docker/docker-agent/tree/main/examples)
- Connect agents to external tools via the [Docker MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)
- Read the full [configuration reference](https://docs.docker.com/ai/docker-agent/configuration/overview/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Desktop

`https://docs.docker.com/desktop`

# Docker Desktop


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker Desktop is a one-click-install application for your Mac, Linux, or Windows environment that lets you build, share, and run containerized applications and microservices.


It provides a straightforward GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine.


Docker Desktop reduces the time spent on complex setups so you can focus on writing code. It takes care of port mappings, file system concerns, and other default settings, and is regularly updated with bug fixes and security updates.


Docker Desktop integrates with your preferred development tools and languages, and gives you access to a vast ecosystem of trusted images and templates via Docker Hub. This empowers teams to accelerate development, automate builds, enable CI/CD workflows, and collaborate securely through shared repositories.


## [Key features](https://docs.docker.com/desktop#key-features)


- Ability to containerize and share any application on any cloud platform, in multiple languages and frameworks.
- Quick installation and setup of a complete Docker development environment.
- Includes the latest version of Kubernetes.
- On Windows, the ability to toggle between Linux and Windows containers to build applications.
- Fast and reliable performance with native Windows Hyper-V virtualization.
- Ability to work natively on Linux through WSL 2 on Windows machines.
- Volume mounting for code and data, including file change notifications and easy access to running containers on the localhost network.


## [Products inside Docker Desktop](https://docs.docker.com/desktop#products-inside-docker-desktop)


- [Docker MCP Toolkit and Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/)
- [Docker Model Runner](https://docs.docker.com/ai/model-runner/)
- [Gordon](https://docs.docker.com/ai/gordon/)
- [Docker Offload](https://docs.docker.com/offload/)
- [Docker Engine](https://docs.docker.com/engine/)
- Docker CLI client
- [Docker Build](https://docs.docker.com/build/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Docker Scout](https://docs.docker.com/scout/)
- [Kubernetes](https://github.com/kubernetes/kubernetes/)


## [Next steps](https://docs.docker.com/desktop#next-steps)


### Install Docker Desktop


Install Docker Desktop on [Mac](https://docs.docker.com/desktop/setup/install/mac-install/), [Windows](https://docs.docker.com/desktop/setup/install/windows-install/), or [Linux](https://docs.docker.com/desktop/setup/install/linux/).

[### Learn about Docker Desktop Navigate Docker Desktop.](https://docs.docker.com/desktop/use-desktop/)

### Explore its key features


Find information about [Networking](https://docs.docker.com/desktop/features/networking/), [Docker VMM](https://docs.docker.com/desktop/features/vmm/), [WSL](https://docs.docker.com/desktop/features/wsl/), and more.

[### View the release notes Find out about new features, improvements, and bug fixes.](https://docs.docker.com/desktop/release-notes/) [### Browse common FAQs Explore general FAQs or FAQs for specific platforms.](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/) [### Give feedback Provide feedback on Docker Desktop or Docker Desktop features.](https://docs.docker.com/desktop/troubleshoot-and-support/feedback/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Offload

`https://docs.docker.com/offload`

# Docker Offload


Ask Gordon


Copy Markdown


View Markdown

---


---

Subscription:
Docker Offload
Requires:
Docker Desktop 4.68 or later


Docker Offload is a fully managed service that lets you offload building and running containers to the cloud using the Docker tools you already know. It enables developers to work efficiently in virtual desktop infrastructure (VDI) environments or systems that don't support nested virtualization.


In the following topics, learn about Docker Offload, how to set it up, use it for your workflows, and troubleshoot common issues.

[### Quickstart Get up and running with Docker Offload in just a few steps.](https://docs.docker.com/offload/quickstart/) [### About Learn about Docker Offload and how it works.](https://docs.docker.com/offload/about/) [### Configure Configure Docker Offload settings for your organization and Docker Desktop.](https://docs.docker.com/offload/configuration/) [### Usage Learn about Docker Offload usage and how to monitor your cloud resources.](https://docs.docker.com/offload/usage/) [### Optimize Improve performance and cost efficiency in Docker Offload.](https://docs.docker.com/offload/optimize/) [### Troubleshoot Learn how to troubleshoot issues with Docker Offload.](https://docs.docker.com/offload/troubleshoot/) [### Feedback Provide feedback on Docker Offload.](https://docs.docker.com/offload/feedback/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Build Cloud

`https://docs.docker.com/build-cloud`

# Docker Build Cloud


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Subscription:
Pro

Team

Business


Docker Build Cloud is a service that lets you build your container images faster, both locally and in CI. Builds run on cloud infrastructure optimally dimensioned for your workloads, no configuration required. The service uses a remote build cache, ensuring fast builds anywhere and for all team members.


## [How Docker Build Cloud works](https://docs.docker.com/build-cloud#how-docker-build-cloud-works)


Using Docker Build Cloud is no different from running a regular build. You invoke a build the same way you normally would, using `docker buildx build`. The difference is in where and how that build gets executed.


By default when you invoke a build command, the build runs on a local instance of BuildKit, bundled with the Docker daemon. With Docker Build Cloud, you send the build request to a BuildKit instance running remotely, in the cloud. All data is encrypted in transit.


The remote builder executes the build steps, and sends the resulting build output to the destination that you specify. For example, back to your local Docker Engine image store, or to an image registry.


Docker Build Cloud provides several benefits over local builds:


- Improved build speed
- Shared build cache
- Native multi-platform builds


And the best part: you don't need to worry about managing builders or infrastructure. Just connect to your builders, and start building. Each cloud builder provisioned to an organization is completely isolated to a single Amazon EC2 instance, with a dedicated EBS volume for build cache, and encryption in transit. That means there are no shared processes or data between cloud builders.


> Note
>
> Docker Build Cloud is only available in the US East region.


## [Get Docker Build Cloud](https://docs.docker.com/build-cloud#get-docker-build-cloud)


To get started with Docker Build Cloud, [create a Docker account](https://docs.docker.com/accounts/individual/create-account/). There are two options to get access to Docker Build Cloud:


- Users with a free Personal account can opt-in to a 7-day free trial, with the option to subscribe for access. To start your free trial, sign in to [Docker Build Cloud Dashboard](https://app.docker.com/build/) and follow the on-screen instructions.
- All users with a paid Docker subscription have access to Docker Build Cloud included with their Docker suite of products. See [Docker subscriptions and features](https://www.docker.com/pricing?ref=Docs&refAction=DocsBuildCloud) for more information.


Once you've signed up and created a builder, continue by [setting up the builder in your local environment](https://docs.docker.com/build-cloud/setup/).


For information about roles and permissions related to Docker Build Cloud, see [Roles and Permissions](https://docs.docker.com/security/roles-and-permissions/core-roles/#docker-build-cloud).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Testcontainers

`https://docs.docker.com/testcontainers`

# Testcontainers


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Testcontainers is a set of open source libraries that provides easy and lightweight APIs for bootstrapping local development and test dependencies with real services wrapped in Docker containers. Using Testcontainers, you can write tests that depend on the same services you use in production without mocks or in-memory services.

[### What is Testcontainers? Learn about what Testcontainers does and its key benefits](https://testcontainers.com/getting-started/#what-is-testcontainers) [### The Testcontainers workflow Understand the Testcontainers workflow](https://testcontainers.com/getting-started/#testcontainers-workflow)

## [Quickstart](https://docs.docker.com/testcontainers#quickstart)


### [Supported languages](https://docs.docker.com/testcontainers#supported-languages)


Testcontainers provide support for the most popular languages, and Docker sponsors the development of the following Testcontainers implementations:


- [Go](https://golang.testcontainers.org/quickstart/)
- [Java](https://java.testcontainers.org/quickstart/junit_5_quickstart/)


The rest are community-driven and maintained by independent contributors.


### [Prerequisites](https://docs.docker.com/testcontainers#prerequisites)


Testcontainers requires a Docker-API compatible container runtime. During development, Testcontainers is actively tested against recent versions of Docker on Linux, as well as against Docker Desktop on Mac and Windows. These Docker environments are automatically detected and used by Testcontainers without any additional configuration being necessary.


It is possible to configure Testcontainers to work for other Docker setups, such as a remote Docker host or Docker alternatives. However, these are not actively tested in the main development workflow, so not all Testcontainers features might be available and additional manual configuration might be necessary.


If you have further questions about configuration details for your setup or whether it supports running Testcontainers-based tests, contact the Testcontainers team and other users from the Testcontainers community on [Slack](https://slack.testcontainers.org/).

[### Testcontainers for Go A Go package that makes it simple to create and clean up container-based dependencies for automated integration/smoke tests.](https://golang.testcontainers.org/quickstart/) [### Testcontainers for Java A Java library that supports JUnit tests, providing lightweight, throwaway instances of anything that can run in a Docker container.](https://java.testcontainers.org/)

## [Guides](https://docs.docker.com/testcontainers#guides)


Explore hands-on Testcontainers guides to learn how to use Testcontainers with different languages and popular frameworks:


- [Getting started with Testcontainers for .NET](https://docs.docker.com/guides/testcontainers-dotnet-getting-started/)
- [Getting started with Testcontainers for Go](https://docs.docker.com/guides/testcontainers-go-getting-started/)
- [Getting started with Testcontainers for Java](https://docs.docker.com/guides/testcontainers-java-getting-started/)
- [Getting started with Testcontainers for Node.js](https://docs.docker.com/guides/testcontainers-nodejs-getting-started/)
- [Getting started with Testcontainers for Python](https://docs.docker.com/guides/testcontainers-python-getting-started/)
- [Testing a Spring Boot REST API with Testcontainers](https://docs.docker.com/guides/testcontainers-java-spring-boot-rest-api/)
- [Testcontainers container lifecycle management](https://docs.docker.com/guides/testcontainers-java-lifecycle/)
- [Replace H2 with a real database for testing](https://docs.docker.com/guides/testcontainers-java-replace-h2/)
- [Configuration of services running in a container](https://docs.docker.com/guides/testcontainers-java-service-configuration/)
- [Testing an ASP.NET Core web app](https://docs.docker.com/guides/testcontainers-dotnet-aspnet-core/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Build

`https://docs.docker.com/build`

# Docker Build


Ask Gordon


Copy Markdown


View Markdown

---


---


Docker Build is one of Docker Engine's most used features. Whenever you are creating an image you are using Docker Build. Build is a key part of your software development life cycle allowing you to package and bundle your code and ship it anywhere.


Docker Build is more than a command for building images, and it's not only about packaging your code. It's a whole ecosystem of tools and features that support not only common workflow tasks but also provides support for more complex and advanced scenarios.

[### Packaging your software Build and package your application to run it anywhere: locally or in the cloud.](https://docs.docker.com/build/concepts/overview/) [### Multi-stage builds Keep your images small and secure with minimal dependencies.](https://docs.docker.com/build/building/multi-stage/) [### Multi-platform images Build, push, pull, and run images seamlessly on different computer architectures.](https://docs.docker.com/build/building/multi-platform/) [### BuildKit Explore BuildKit, the open source build engine.](https://docs.docker.com/build/buildkit/) [### Build drivers Configure where and how you run your builds.](https://docs.docker.com/build/builders/drivers/) [### Docker Build Cloud Run builds on managed cloud builders with a shared cache.](https://docs.docker.com/build-cloud/) [### Exporters Export any artifact you like, not just Docker images.](https://docs.docker.com/build/exporters/) [### Build caching Avoid unnecessary repetitions of costly operations, such as package installs.](https://docs.docker.com/build/cache/) [### Bake Orchestrate your builds with Bake.](https://docs.docker.com/build/bake/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Engine

`https://docs.docker.com/engine`

# Docker Engine


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker Engine is an open source containerization technology for building and containerizing your applications. Docker Engine acts as a client-server application with:


- A server with a long-running daemon process [`dockerd`](https://docs.docker.com/reference/cli/dockerd).
- APIs which specify interfaces that programs can use to talk to and instruct the Docker daemon.
- A command line interface (CLI) client [`docker`](https://docs.docker.com/reference/cli/docker/).


The CLI uses [Docker APIs](https://docs.docker.com/reference/api/engine/) to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI. The daemon creates and manages Docker objects, such as images, containers, networks, and volumes.


For more details, see [Docker Architecture](https://docs.docker.com/get-started/docker-overview/#docker-architecture).

[### Install Docker Engine Learn how to install the open source Docker Engine for your distribution.](https://docs.docker.com/engine/install) [### Storage Use persistent data with Docker containers.](https://docs.docker.com/storage) [### Networking Manage network connections between containers.](https://docs.docker.com/network) [### Container logs Learn how to view and read container logs.](https://docs.docker.com/config/containers/logging/) [### Prune Tidy up unused resources.](https://docs.docker.com/config/pruning) [### Configure the daemon Delve into the configuration options of the Docker daemon.](https://docs.docker.com/config/daemon) [### Rootless mode Run Docker without root privileges.](https://docs.docker.com/engine/security/rootless) [### Deprecated features Find out what features of Docker Engine you should stop using.](https://docs.docker.com/engine/deprecated/) [### Release notes Read the release notes for the latest version.](https://docs.docker.com/engine/release-notes)

*For more details, see
Docker Architecture.*

## [Licensing](https://docs.docker.com/engine#licensing)


Commercial use of Docker Engine obtained via Docker Desktop within larger enterprises (exceeding 250 employees OR with annual revenue surpassing $10 million USD), requires a [paid subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsEngine). Apache License, Version 2.0. See [LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full license.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Cloud driver

`https://docs.docker.com/build/builders/drivers/cloud`

# Cloud driver


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The Buildx cloud driver connects to managed BuildKit instances in Docker Build Cloud. Docker provisions and maintains the builder infrastructure, shared build cache, and native `linux/amd64` and `linux/arm64` nodes.


The cloud driver requires Buildx version 0.37.0 or later and access to Docker Build Cloud.


## [Synopsis](https://docs.docker.com/build/builders/drivers/cloud#synopsis)


Before connecting Buildx, create a cloud builder on the [Docker Build Cloud Dashboard](https://app.docker.com/build/). Then sign in and connect to the builder:


```console
$ docker login
$ docker buildx create --driver cloud <ORG>/<BUILDER_NAME>
```


The command adds the cloud builder to your local Buildx configuration. It does not create a builder in Docker Build Cloud.


For service prerequisites and authentication, see [Docker Build Cloud setup](https://docs.docker.com/build-cloud/setup/). For build examples, see [Building with Docker Build Cloud](https://docs.docker.com/build-cloud/usage/).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Compose

`https://docs.docker.com/compose`

# Docker Compose


Ask Gordon


Copy Markdown


View Markdown

---


---


Docker Compose is a tool for defining and running multi-container applications. It is the key to unlocking a streamlined and efficient development and deployment experience.


Compose simplifies the control of your entire application stack, making it easy to manage services, networks, and volumes in a single YAML configuration file. Then, with a single command, you create and start all the services from your configuration file.


Compose works in all environments - production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application:


- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service

[### Why use Compose? Understand Docker Compose's key benefits](https://docs.docker.com/compose/intro/features-uses/) [### How Compose works Understand how Compose works](https://docs.docker.com/compose/intro/compose-application-model/) [### Install Compose Follow the instructions on how to install Docker Compose.](https://docs.docker.com/compose/install) [### Quickstart Learn the key concepts of Docker Compose whilst building a simple Python web application.](https://docs.docker.com/compose/gettingstarted) [### View the release notes Find out about the latest enhancements and bug fixes.](https://github.com/docker/compose/releases) [### Explore the Compose file reference Find information on defining services, networks, and volumes for a Docker application.](https://docs.docker.com/reference/compose-file) [### Use Compose Bridge Transform your Compose configuration file into configuration files for different platforms, such as Kubernetes.](https://docs.docker.com/compose/bridge) [### Browse common FAQs Explore general FAQs and find out how to give feedback.](https://docs.docker.com/compose/faq)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Hub

`https://docs.docker.com/docker-hub`

# Docker Hub


Ask Gordon


Copy Markdown


View Markdown

---


---


[Explore the Docker Hub API 2-beta →](https://docs.docker.com/reference/api/hub/latest/)


Docker Hub simplifies development with the world's largest container registry for storing, managing, and sharing Docker images. By integrating seamlessly with your tools, it enhances productivity and ensures reliable deployment, distribution, and access to containerized applications. It also provides developers with pre-built images and assets to speed up development workflows.


Key features of Docker Hub:


- Unlimited public repositories
- Private repositories
- Webhooks to automate workflows
- GitHub and Bitbucket integrations
- Concurrent and automated builds
- Trusted content featuring high-quality, secure images


In addition to the graphical interface, you can interact with Docker Hub using the [Docker Hub API](https://docs.docker.com/reference/api/hub/latest/), the experimental [Docker Hub CLI tool](https://github.com/docker/hub-tool#readme), or the [Docker Hub MCP server](https://docs.docker.com/docker-hub/mcp-server/) for AI agent integrations.

[### Quickstart Step-by-step instructions on getting started on Docker Hub.](https://docs.docker.com/docker-hub/quickstart) [### Library Explore the content library, featuring millions of images for operating systems, frameworks, databases, and more.](https://docs.docker.com/docker-hub/image-library/) [### Repositories Create a repository to share your images with your team, customers, or the Docker community.](https://docs.docker.com/docker-hub/repos) [### Settings Learn about settings in Docker Hub.](https://docs.docker.com/docker-hub/settings) [### Organizations Learn about organization administration.](https://docs.docker.com/accounts/organization/) [### Usage and limits Explore usage limits and how to better utilize Docker Hub.](https://docs.docker.com/docker-hub/usage/) [### MCP server Use the Docker Hub MCP server to access image metadata and manage repositories with AI agents.](https://docs.docker.com/docker-hub/mcp-server/) [### Release notes Find out about new features, improvements, and bug fixes.](https://docs.docker.com/docker-hub/release-notes)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Hardened Images

`https://docs.docker.com/dhi`

# Docker Hardened Images


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker Hardened Images (DHI) provide minimal, secure, and production-ready container images, Helm charts, and system packages maintained by Docker. Designed to reduce vulnerabilities and simplify compliance, DHI integrates easily into your existing Docker-based workflows with little to no retooling required.


DHI is available in the following three subscriptions.


| Feature | Community | Select | Enterprise |
| --- | --- | --- | --- |
| Hardened, minimal images | ✅ | ✅ | ✅ |
| Near-zero CVEs | ✅ | ✅ | ✅ |
| Verifiable SBOMs & SLSA Build L3 provenance | ✅ | ✅ | ✅ |
| Full, unsuppressed CVE visibility | ✅ | ✅ | ✅ |
| Drop-in adoption, no workflow changes | ✅ | ✅ | ✅ |
| Full catalog of open source images under Apache 2.0 | ✅ | ✅ | ✅ |
| Built with Docker Hardened System Packages | ✅ | ✅ | ✅ |
| Upstream cadence for Docker-released patches | ✅ | ✅ | ✅ |
| FIPS/STIG variants | ❌ | ✅ | ✅ |
| Critical CVE fixes < 7 days with SLA-backed continuous patching | ❌ | ✅ | ✅ |
| Customizations | ❌ | ✅ Up to 5 | ✅ Unlimited |
| Access to Hardened System Packages repository | ❌ | ❌ | ✅ |
| Full catalog access available | ❌ | ❌ | ✅ |
| Extended Lifecycle Support add-on available | ❌ | ❌ | ✅ +5 years of hardened updates |


For pricing and more details, see the [Docker Hardened Images subscription comparison](https://www.docker.com/products/hardened-images/#compare).


## [Community features](https://docs.docker.com/dhi#community-features)


DHI's core features are free to use, share, and build on under Apache 2.0.


- [Near-zero CVEs](https://docs.docker.com/dhi/explore/security-concepts/cves/): continuously scanned and patched to maintain minimal known vulnerabilities
- [Distroless variants](https://docs.docker.com/dhi/explore/security-concepts/distroless/): remove unnecessary components, reducing attack surface by up to 95%
- Non-root execution: containers run as non-root by default
- [Hardened system packages](https://docs.docker.com/dhi/how-to/hardened-packages/): system packages built from source, cryptographically signed, and verified by Docker
- [SLSA Build Level 3 provenance](https://docs.docker.com/dhi/explore/security-concepts/slsa/), [signed SBOMs](https://docs.docker.com/dhi/explore/security-concepts/sbom/), [VEX statements](https://docs.docker.com/dhi/explore/security-concepts/vex/), and [cryptographic signatures](https://docs.docker.com/dhi/explore/security-concepts/signatures/) on every image
- Built on Alpine and Debian with [glibc and musl variants](https://docs.docker.com/dhi/explore/security-concepts/glibc-musl/); dev and runtime image variants available
- Works with existing Docker workflows, CI/CD pipelines, and tools with no retooling required
- [Helm charts](https://docs.docker.com/dhi/how-to/helm/): Docker-provided charts built from upstream sources, tested for compatibility with DHI, and available as OCI artifacts in the DHI catalog; include SLSA Level 3 provenance, SBOMs, and cryptographic signing


## [Select and Enterprise features](https://docs.docker.com/dhi#select-and-enterprise-features)


For organizations with strict security or compliance requirements:


- [7-day SLA](https://docs.docker.com/go/dhi-sla/) for critical and high severity CVE remediation
- [FIPS-enabled](https://docs.docker.com/dhi/explore/security-concepts/fips/) and [STIG-ready](https://docs.docker.com/dhi/explore/security-concepts/stig/) compliance variants
- [Customization](https://docs.docker.com/dhi/how-to/customize/): add packages, tools, certificates, and configurations (up to 5 with Select, unlimited with Enterprise)
- [Enterprise package repository](https://docs.docker.com/dhi/how-to/hardened-packages/) access and full catalog access (Enterprise)
- Extended Lifecycle Support: post-EOL security patches, updated SBOMs, provenance, and signing (Enterprise add-on)


## [Get started](https://docs.docker.com/dhi#get-started)


Explore the sections below to get started with Docker Hardened Images, integrate them into your workflow, and learn what makes them secure and enterprise-ready.

[### Quickstart Follow a step-by-step guide to explore and run a Docker Hardened Image.](https://docs.docker.com/dhi/get-started/) [### Explore Learn what Docker Hardened Images are, how they're built, and what sets them apart from typical base images.](https://docs.docker.com/dhi/explore/) [### How-tos Step-by-step guides for using, verifying, scanning, and migrating to Docker Hardened Images.](https://docs.docker.com/dhi/how-to/) [### Security concepts Understand the secure supply chain principles that make Docker Hardened Images production-ready.](https://docs.docker.com/dhi/explore/security-concepts/) [### Tools Browse and manage Docker Hardened Images using Docker Hub, the CLI, MCP server, or Terraform.](https://docs.docker.com/dhi/tools/) [### Resources and feedback Guides, GitHub repositories, community channels, and how to give feedback.](https://docs.docker.com/dhi/resources/) [### Release notes New features, improvements, and changes in Docker Hardened Images.](https://docs.docker.com/dhi/release-notes/platform/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Scout

`https://docs.docker.com/scout`

# Docker Scout


Ask Gordon


Copy Markdown


View Markdown

---


---


Container images consist of layers and software packages, which are susceptible to vulnerabilities. These vulnerabilities can compromise the security of containers and applications.


Docker Scout is a solution for proactively enhancing your software supply chain security. By analyzing your images, Docker Scout compiles an inventory of components, also known as a Software Bill of Materials (SBOM). The SBOM is matched against a continuously updated vulnerability database to pinpoint security weaknesses.


Docker Scout is a standalone service and platform that you can interact with using Docker Hub, the Docker CLI, and the Docker Scout Dashboard.

[### Quickstart Learn what Docker Scout can do, and how to get started.](https://docs.docker.com/scout/quickstart/) [### Image analysis Reveal and dig into the composition of your images.](https://docs.docker.com/scout/image-analysis/) [### Advisory database Learn about the information sources that Docker Scout uses.](https://docs.docker.com/scout/advisory-db-sources/) [### Integrations Connect Docker Scout with your CI, registries, and other third-party services.](https://docs.docker.com/scout/integrations/) [### Dashboard The web interface for Docker Scout.](https://docs.docker.com/scout/dashboard/) [### Policy Ensure that your artifacts align with supply chain best practices.](https://docs.docker.com/scout/policy/) [### Upgrade A Personal subscription includes up to 1 repository. Upgrade for more.](https://docs.docker.com/subscription-billing/manage/plans/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Accounts

`https://docs.docker.com/accounts`

# Accounts


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


A Docker account identifies you and lets you access Docker products. You manage it in [Docker Home](https://app.docker.com/). Docker has two primary account types: individual and organization. A company groups multiple organizations.


| Account type | What it is | Who it's for |
| --- | --- | --- |
| Individual | A Docker ID with personal settings, Hub repositories, and sign-in methods | A person |
| Organization | A shared workspace for members, teams, and repositories | Teams on Docker Team or Business |
| Company | Shared sign-in and administration for organizations that keep their own members, repositories, and billing | Docker Business subscribers |


You always sign in with your individual account, then work in the organizations you own or belong to.


## [Next steps](https://docs.docker.com/accounts#next-steps)

[### Docker individual accounts Create and manage your Docker ID, email, and sign-in methods.](https://docs.docker.com/accounts/individual/) [### Organization accounts Manage members, teams, and organization settings.](https://docs.docker.com/accounts/organization/) [### Company accounts Group multiple organizations for centralized administration.](https://docs.docker.com/accounts/company/) [### Security Authentication, tokens, and roles for accounts and organizations.](https://docs.docker.com/security/) [### Subscription and billing Plans, payments, and invoices for your account or organization.](https://docs.docker.com/subscription-billing/) [### FAQs Common questions about accounts, billing, and security.](https://docs.docker.com/faqs/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Secure Docker accounts and organizations

`https://docs.docker.com/security`

# Secure Docker accounts and organizations


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Security helps individual users and organization owners secure their accounts, manage access, and control membership. You configure these settings in [Docker Home](https://app.docker.com/).


## [Individual accounts](https://docs.docker.com/security#individual-accounts)


You sign in with your individual account.


- [Two-factor authentication](https://docs.docker.com/security/authentication/2fa/) (2FA) adds a time-based one-time password (TOTP) from an authenticator app to your password.
- A [personal access token](https://docs.docker.com/security/access-tokens/personal-access-tokens/) (PAT) authenticates the Docker CLI and tools without your password, and is required for CLI sign-in when 2FA is on or single sign-on (SSO) is enforced.


## [Organization accounts](https://docs.docker.com/security#organization-accounts)


Organization and company owners set up how members sign in, add them to the organization, configure automation, and control what members can do.


- [Single sign-on](https://docs.docker.com/security/authentication/single-sign-on/) (SSO) federates sign-in through your identity provider, which can cover one organization or every organization in a company.
- [Provisioning](https://docs.docker.com/security/provisioning/) adds users with System for Cross-domain Identity Management (SCIM), Just-in-Time (JIT) provisioning, auto-provisioning, or domain matching.
- An [organization access token](https://docs.docker.com/security/access-tokens/organization-access-tokens/) (OAT) stays with the organization when membership changes.
- [OIDC connections](https://docs.docker.com/security/authentication/oidc-connections/) use OpenID Connect to authenticate GitHub Actions with short-lived tokens, as an alternative to a long-lived OAT.
- [Roles and permissions](https://docs.docker.com/security/roles-and-permissions/) control what members can do after they join.


## [Next steps](https://docs.docker.com/security#next-steps)

[### Authentication Two-factor authentication, single sign-on, and OIDC connections.](https://docs.docker.com/security/authentication/) [### Access tokens Personal and organization access tokens for the Docker CLI and automation.](https://docs.docker.com/security/access-tokens/) [### Provisioning Add users with SCIM, JIT, auto-provisioning, and domain management.](https://docs.docker.com/security/provisioning/) [### Roles and permissions Assign core or custom roles to control access in your organization.](https://docs.docker.com/security/roles-and-permissions/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Subscription and billing

`https://docs.docker.com/subscription-billing`

# Subscription and billing


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


A Docker plan is a subscription tied to a personal account, an organization account, or a specific product. When you upgrade a plan, you expand your usage entitlements and feature sets. You can also top up some plans, extending usage without changing your plan type.


## [Docker plans](https://docs.docker.com/subscription-billing#docker-plans)


The following table summarizes the available plans.


| Plans | Billing model | Types |
| --- | --- | --- |
| [Docker](https://docs.docker.com/subscription-billing/plans/docker/) | Flat-rate plans for personal and organization accounts | Docker Personal, Docker Pro, Docker Team, Docker Business |
| [Docker Hardened Images (DHI)](https://docs.docker.com/subscription-billing/plans/dhi/) | Graduated security features for hardened container images | DHI Community, DHI Select, DHI Enterprise |
| [Gordon](https://docs.docker.com/subscription-billing/plans/gordon/) | Prepaid usage for the Gordon AI agent | Gordon Plus, Gordon Max, Gordon Ultra |
| [AI Governance](https://docs.docker.com/subscription-billing/plans/ai-governance/) | Purchase set amount of licenses | AI Governance |
| [Docker Verified Publisher (DVP)](https://docs.docker.com/subscription-billing/plans/docker-verified-publisher/) | Annual plans based on consuming domains | DVP Starter, DVP Growth |


Docker plans that upgrade your account (Docker Pro, Team, and Business) cover most use cases. Some product plans require an upgraded Docker account. Others let you subscribe without one. For details, see [Plans](https://docs.docker.com/subscription-billing/plans/).


## [Top up your plan](https://docs.docker.com/subscription-billing#top-up-your-plan)


Plans come with usage entitlements that can be extended without upgrading to a different plan.


| Unit | Description | Examples |
| --- | --- | --- |
| [Seats](https://docs.docker.com/accounts/organization/manage/manage-seats/) | Each seat extends entitlements to one more member. | Docker Team, Docker Business |
| [Licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses/) | Access to specific products or features. | AI Governance, Docker Offload |
| [Minutes](https://docs.docker.com/subscription-billing/plans/docker/#docker-build-cloud-minutes) | Cloud build capacity, sold in blocks and consumed within the billing period. | Docker Build Cloud |
| [Repositories](https://docs.docker.com/subscription-billing/plans/dhi/) | Additional container repositories covered by security scanning and analysis features. | DHI |
| [Consuming domains](https://docs.docker.com/subscription-billing/plans/docker-verified-publisher/#add-consuming-domains) | Additional consuming domains tracked in publisher analytics, sold in blocks of 25. | DVP Starter, DVP Growth |


## [Manage your plans](https://docs.docker.com/subscription-billing#manage-your-plans)


To subscribe to a new plan or upgrade an active plan, see [Manage plans](https://docs.docker.com/subscription-billing/manage/plans/). See [Docker plans](https://docs.docker.com/subscription-billing/plans/docker/) to learn about Docker Team, Business, and Pro. You can also [contact sales](https://www.docker.com/pricing/contact-sales/).


To update payment methods, review usage and credits, or download invoices, see [Manage billing](https://docs.docker.com/subscription-billing/manage/).


## [Next steps](https://docs.docker.com/subscription-billing#next-steps)

[### Explore plans Browse available Docker plans and add-ons for individuals, teams, and organizations.](https://docs.docker.com/subscription-billing/plans/) [### Manage billing Manage payment methods, invoices, credits, and billing details in the billing portal.](https://docs.docker.com/subscription-billing/manage/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# FAQs

`https://docs.docker.com/faqs`

# FAQs


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Answers to common questions about Docker accounts, organizations, companies, subscriptions, billing, and security.


## [Next steps](https://docs.docker.com/faqs#next-steps)

[### Account FAQs FAQs about Docker IDs, account creation, organizations, and companies.](https://docs.docker.com/faqs/accounts/) [### Security FAQs FAQs about single sign-on, identity providers, enforcement, and domains.](https://docs.docker.com/faqs/security/) [### Subscription and billing FAQs FAQs about Docker plans, payments, taxes, and invoices.](https://docs.docker.com/faqs/subscription-billing/) [### Platform FAQs FAQs about Docker Desktop containers, networking, VMs, and general platform security.](https://docs.docker.com/faqs/platform/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Get support for Docker products

`https://docs.docker.com/support`

# Get support for Docker products


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Docker offers multiple support channels depending on your subscription level and needs.


## [Paid subscription support](https://docs.docker.com/support#paid-subscription-support)


All Docker Pro, Team, and Business subscribers receive email support for Docker products.


### [Support response times](https://docs.docker.com/support#support-response-times)


- Docker Pro: 5 business day response
- Docker Team: 2 business day response, 24×5 availability
- Docker Business: 1 business day response, 24×5 availability


Docker Verified Publisher (DVP) organizations follow the response times for their Docker Pro, Team, or Business subscription. Without one of those subscriptions, the following response times apply:


- DVP Starter: 3 business day response
- DVP Growth: 2 business day response, 24×5 availability


> Tip
>
> Premium Support with faster response times and 24×7 availability is available as an add-on for [Docker Business and Docker Hardened Images subscribers](https://www.docker.com/pricing?ref=Docs&refAction=DocsSupport).


### [Support severity levels](https://docs.docker.com/support#support-severity-levels)


| Level | Description |
| --- | --- |
| Critical | Widespread or company-wide service outage affecting many customers or all users within a single organization. Business operations are halted with no workaround available. |
| High | Team or department-level impact preventing significant users from accessing core functionality. Severe business impact with no workaround available. |
| Medium | Individual user or small group impact causing partial loss of functionality. Business operations continue, often with workarounds available but reduced productivity. |


### [Request support](https://docs.docker.com/support#request-support)


> Tip
>
> Before reaching out for support, review the troubleshooting documentation for your product.


If you have a paid Docker subscription, [contact the Support team](https://hub.docker.com/support/contact/).


*If you have a paid Docker subscription,
contact the Support team.*

## [Community support](https://docs.docker.com/support#community-support)


All Docker users can seek support through community resources, where Docker or the community respond on a best-effort basis:


- [Docker Community Forums](https://forums.docker.com/)
- [Docker Community Slack](http://dockr.ly/comm-slack)


## [Docker Desktop support](https://docs.docker.com/support#docker-desktop-support)


Docker Desktop support is available with a paid subscription.


### [Scope of support](https://docs.docker.com/support#scope-of-support)


Covered


Not covered

Docker Desktop support includes:


- Account management and billing
- Configuration and installation issues
- Desktop updates
- Sign-in issues
- Push or pull issues, including rate limiting
- Application crashes or unexpected behavior
- Automated builds
- Basic product how-to questions


On Windows, support also covers:


- Turning on virtualization in BIOS
- Turning on Windows features
- Running inside [certain VM or VDI environments](https://docs.docker.com/desktop/setup/vm-vdi/) (Docker Business only)


Docker Desktop support excludes:


- Unsupported operating systems, including beta and preview versions
- Running containers of a different architecture using emulation
- Docker Engine, Docker CLI, or other bundled Linux components
- Kubernetes
- Features labeled as experimental
- System and server administration activities
- Desktop as a production runtime
- Scale deployment and multi-machine installation
- Routine product maintenance (data backup, disk space, log rotation)
- Third-party applications not provided by Docker
- Altered or modified Docker software
- Hardware malfunction, abuse, or improper use
- Versions older than the latest release (except Docker Business)
- Training, customization, and integration
- Running multiple instances on a single machine


> Note
>
> Support for [running Docker Desktop in a VM or VDI environment](https://docs.docker.com/desktop/setup/vm-vdi/) is only available to Docker Business customers.


### [Supported versions](https://docs.docker.com/support#supported-versions)


- Docker Business: Versions up to six months older than the latest version (fixes applied to latest version only)
- Docker Pro and Team: Latest version only


### [Machines per subscription](https://docs.docker.com/support#machines-per-subscription)


- Docker Pro: One machine
- Docker Team: Number of machines equal to subscription seats
- Docker Business: Unlimited machines


### [Supported operating systems](https://docs.docker.com/support#supported-operating-systems)


- [Mac system requirements](https://docs.docker.com/desktop/setup/install/mac-install/#system-requirements)
- [Windows system requirements](https://docs.docker.com/desktop/setup/install/windows-install/#system-requirements)
- [Linux system requirements](https://docs.docker.com/desktop/setup/install/linux/#system-requirements)


### [Docker Desktop community resources](https://docs.docker.com/support#docker-desktop-community-resources)


- [Docker Desktop issue tracker](https://github.com/docker/desktop-feedback)


### [Diagnostic data and privacy](https://docs.docker.com/support#diagnostic-data-and-privacy)


When uploading diagnostics, the bundle may contain personal data such as usernames and IP addresses. Diagnostics bundles are only accessible to Docker, Inc. employees directly involved in diagnosing issues.


By default, Docker, Inc. deletes uploaded diagnostics bundles after 30 days. You can request removal of a diagnostics bundle by specifying the diagnostics ID or your GitHub ID. Docker, Inc. only uses the data to investigate specific user issues but may derive high-level (non-personal) metrics.


For more information, see [Docker Data Processing Agreement](https://www.docker.com/legal/data-processing-agreement).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Accounts and admin release notes

`https://docs.docker.com/platform-release-notes`

# Accounts and admin release notes


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


This page lists new features, enhancements, known issues, and bug fixes for Docker accounts and admin features, including Docker Home, billing, security, and subscriptions.


## [2026-09-30](https://docs.docker.com/platform-release-notes#2026-09-30)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements)


- Accounts that already have cloud sandboxes skip [Docker Agentic Platform](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform/) checkout.


## [2026-09-29](https://docs.docker.com/platform-release-notes#2026-09-29)


### [New](https://docs.docker.com/platform-release-notes#new)


- Organization owners can now [assign a license to a team](https://docs.docker.com/accounts/organization/manage/manage-licenses/#teams). Every member of the team receives the license, including people who join the team later. Each member uses one license per product.
- The [Licenses page](https://docs.docker.com/accounts/organization/manage/manage-licenses/#view-licenses) in Docker Home shows how many licenses are available and whether they are assigned to teams or to individual members.


## [2026-09-28](https://docs.docker.com/platform-release-notes#2026-09-28)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-1)


- [Creating a team](https://docs.docker.com/accounts/organization/manage/manage-a-team/#create-a-team) in Docker Home opens that team's page.
- The [member list CSV](https://docs.docker.com/accounts/organization/manage/members/#export-a-member-list-csv) includes a **Licenses** column when the organization has at least one active license pool. The column lists each member's assigned licenses.


## [2026-09-24](https://docs.docker.com/platform-release-notes#2026-09-24)


### [New](https://docs.docker.com/platform-release-notes#new-1)


- You can now subscribe to the [Docker Agentic Platform](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform/) pay-as-you-go plan with a personal account to run agents in cloud sandboxes. Compute is metered by the second while a sandbox runs.


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-2)


- The [support request form](https://app.docker.com/support/contact) **Legal** topic includes **PII/Sensitive information**, **Service abuse**, and **Trademark takedowns**.


## [2026-09-14](https://docs.docker.com/platform-release-notes#2026-09-14)


### [New](https://docs.docker.com/platform-release-notes#new-2)


- Organization owners can now [export a member list](https://docs.docker.com/accounts/organization/manage/members/#export-a-member-list-csv) from Docker Home and receive the CSV by email. Docker generates the file asynchronously and emails a download link to the owner.


## [2026-08-20](https://docs.docker.com/platform-release-notes#2026-08-20)


### [New](https://docs.docker.com/platform-release-notes#new-3)


- [Docker Verified Publisher](https://docs.docker.com/subscription-billing/plans/docker-verified-publisher/) Starter and Growth plans are now available via self-serve. Organizations can apply and subscribe without contacting sales.


## [2026-08-14](https://docs.docker.com/platform-release-notes#2026-08-14)


### [New](https://docs.docker.com/platform-release-notes#new-4)


- Administrators can now [select a product license when inviting a member](https://docs.docker.com/accounts/organization/manage/manage-licenses/#licenses-and-invites). Docker assigns the license when the invitee accepts.


## [2026-07-31](https://docs.docker.com/platform-release-notes#2026-07-31)


### [New](https://docs.docker.com/platform-release-notes#new-5)


- Administrators can now create [OIDC connections](https://docs.docker.com/security/authentication/oidc-connections/) so GitHub Actions workflows authenticate to Docker with short-lived tokens instead of stored personal or organization access tokens. Available for Docker Team, Docker Business, Docker Hardened Images, and Docker Sponsored Open Source organizations.


## [2026-06-18](https://docs.docker.com/platform-release-notes#2026-06-18)


### [New](https://docs.docker.com/platform-release-notes#new-6)


- Custom roles now include [AI Governance permissions](https://docs.docker.com/security/roles-and-permissions/custom-roles/permissions-reference/#ai-governance) so owners can delegate policy management to other users and teams.


## [2026-06-02](https://docs.docker.com/platform-release-notes#2026-06-02)


### [New](https://docs.docker.com/platform-release-notes#new-7)


- Administrators can now provision products to organization members with [licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses/). Licenses were introduced with AI Governance. Owners can assign or revoke them from the Members page, or turn on automatic assignment when a member first uses a supported product.


## [2026-05-19](https://docs.docker.com/platform-release-notes#2026-05-19)


### [New](https://docs.docker.com/platform-release-notes#new-8)


- You can now purchase [Gordon Plus, Max, and Ultra plans](https://docs.docker.com/subscription-billing/plans/gordon/) for personal accounts from the billing portal in Docker Home.
- Organizations can now purchase [DHI Select](https://docs.docker.com/subscription-billing/plans/dhi/) repositories via self-serve from the billing portal in Docker Home.


## [2026-05-12](https://docs.docker.com/platform-release-notes#2026-05-12)


### [New](https://docs.docker.com/platform-release-notes#new-9)


- [AI Governance](https://docs.docker.com/subscription-billing/plans/ai-governance/) is now available. Administrators can purchase licenses through sales, [assign them to members](https://docs.docker.com/accounts/organization/manage/manage-licenses/), and enforce [organization policies](https://docs.docker.com/ai/sandboxes/governance/) for Docker AI products from Docker Home.


## [2026-03-03](https://docs.docker.com/platform-release-notes#2026-03-03)


### [New](https://docs.docker.com/platform-release-notes#new-10)


- [DHI Select](https://docs.docker.com/subscription-billing/plans/dhi/) is now available as a Docker Hardened Images plan for organizations that need SLA-backed patching and compliance-ready images.


## [2026-02-18](https://docs.docker.com/platform-release-notes#2026-02-18)


### [New](https://docs.docker.com/platform-release-notes#new-11)


- Administrators can now [configure DVP analytics settings](https://docs.docker.com/docker-hub/repos/manage/trusted-content/insights-analytics/#configure-dvp-analytics-settings) for consuming domain and benchmark report allocations in the Admin Console.


## [2026-02-13](https://docs.docker.com/platform-release-notes#2026-02-13)


### [New](https://docs.docker.com/platform-release-notes#new-12)


- Administrators can now control whether organization members can push content to their personal namespaces on Docker Hub with [namespace access control](https://docs.docker.com/desktop/enterprise/hardened-desktop/namespace-access/).
- Administrators can now prevent creating public repositories within organization namespaces using the [Disable public repositories](https://docs.docker.com/docker-hub/settings/#disable-creation-of-public-repos) setting.


## [2026-01-27](https://docs.docker.com/platform-release-notes#2026-01-27)


### [New](https://docs.docker.com/platform-release-notes#new-13)


- Administrators can now use an allow list with [Image Access Management](https://docs.docker.com/desktop/enterprise/hardened-desktop/image-access-management/) to approve specific repositories that bypass image access controls.


## [2025-11-04](https://docs.docker.com/platform-release-notes#2025-11-04)


### [New](https://docs.docker.com/platform-release-notes#new-14)


- Owners can now create [custom roles](https://docs.docker.com/security/roles-and-permissions/custom-roles/) and assign them to members and teams.


## [2025-10-28](https://docs.docker.com/platform-release-notes#2025-10-28)


### [New](https://docs.docker.com/platform-release-notes#new-15)


- Docker Business subscribers can now add [Premium Support](https://docs.docker.com/support/#paid-subscription-support), with faster response times and 24/7 availability.


## [2025-10-22](https://docs.docker.com/platform-release-notes#2025-10-22)


### [New](https://docs.docker.com/platform-release-notes#new-16)


- Organizations can now [pay by invoice](https://docs.docker.com/subscription-billing/manage/payment-method/#pay-by-invoice).


## [2025-10-14](https://docs.docker.com/platform-release-notes#2025-10-14)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-3)


- Docker Home now keeps [activity logs](https://docs.docker.com/accounts/organization/activity-logs/#access-activity-logs) for 30 days. Use the Docker Hub API to retrieve older events.


## [2025-10-07](https://docs.docker.com/platform-release-notes#2025-10-07)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-4)


- Organization management has moved out of Docker Hub. Manage organizations in Docker Home.


## [2025-06-30](https://docs.docker.com/platform-release-notes#2025-06-30)


### [New](https://docs.docker.com/platform-release-notes#new-17)


- Organization owners can now [export Docker Desktop user data](https://docs.docker.com/accounts/organization/insights/#export-docker-desktop-user-data) from Insights as a CSV file.


## [2025-06-23](https://docs.docker.com/platform-release-notes#2025-06-23)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-5)


- [Organization access tokens](https://docs.docker.com/security/access-tokens/organization-access-tokens/) now work with Docker Scout.


## [2025-06-18](https://docs.docker.com/platform-release-notes#2025-06-18)


### [New](https://docs.docker.com/platform-release-notes#new-18)


- Organization owners can now [resend invitations in bulk](https://docs.docker.com/accounts/organization/manage/members/#manage-invitations) from the Members page.


## [2025-06-10](https://docs.docker.com/platform-release-notes#2025-06-10)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-6)


- [Activity logs](https://docs.docker.com/accounts/organization/activity-logs/) now record single sign-on connection changes, and changes to SCIM and just-in-time provisioning.


## [2025-05-12](https://docs.docker.com/platform-release-notes#2025-05-12)


### [New](https://docs.docker.com/platform-release-notes#new-19)


- You can now connect [more than one identity provider](https://docs.docker.com/security/authentication/single-sign-on/connect/#configure-multiple-idps) to a single sign-on domain. Users choose a provider when they sign in with SSO.


## [2025-04-30](https://docs.docker.com/platform-release-notes#2025-04-30)


### [New](https://docs.docker.com/platform-release-notes#new-20)


- You can now pay for a subscription with a [verified US bank account](https://docs.docker.com/subscription-billing/manage/payment-method/#verify-a-bank-account).


## [2025-04-22](https://docs.docker.com/platform-release-notes#2025-04-22)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-7)


- [Personal access tokens](https://docs.docker.com/security/access-tokens/personal-access-tokens/) now transfer to the organization owners when you [convert a user account into an organization](https://docs.docker.com/accounts/organization/setup/convert-account/).


## [2025-04-08](https://docs.docker.com/platform-release-notes#2025-04-08)


### [New](https://docs.docker.com/platform-release-notes#new-21)


- Organization owners can now onboard an organization with [guided setup](https://docs.docker.com/accounts/organization/setup/onboard/#onboard-with-guided-setup) in Docker Home.


## [2025-04-01](https://docs.docker.com/platform-release-notes#2025-04-01)


### [New](https://docs.docker.com/platform-release-notes#new-22)


- [Organization access tokens](https://docs.docker.com/security/access-tokens/organization-access-tokens/) are now generally available.
- Single sign-on now supports the [`dockerSessionMinutes` attribute](https://docs.docker.com/security/provisioning/#sso-attributes), so a session can follow the identity provider timeout.
- Administrators can now [track whether users comply with Docker Desktop settings policies](https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/compliance-reporting/) from Docker Home (Early Access). Compliance status is reported by Docker Desktop version 4.40 and later.


## [2025-03-12](https://docs.docker.com/platform-release-notes#2025-03-12)


### [New](https://docs.docker.com/platform-release-notes#new-23)


- You can now [disconnect a linked Google or GitHub account](https://docs.docker.com/accounts/individual/manage-account/#manage-connected-accounts) from Account settings.


## [2025-03-11](https://docs.docker.com/platform-release-notes#2025-03-11)


### [New](https://docs.docker.com/platform-release-notes#new-24)


- [Organization access tokens](https://docs.docker.com/security/access-tokens/reference/#organization-access-token-scopes) now include repository scopes and organization management scopes for members, invites, and groups.


## [2025-02-21](https://docs.docker.com/platform-release-notes#2025-02-21)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-8)


- Organization access tokens now work with Docker Build Cloud and the Docker Hub APIs. Company owners can manage them.


## [2025-02-11](https://docs.docker.com/platform-release-notes#2025-02-11)


### [New](https://docs.docker.com/platform-release-notes#new-25)


- Docker Home and the Docker Admin Console are now generally available.


## [2025-01-31](https://docs.docker.com/platform-release-notes#2025-01-31)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-9)


- Docker began collecting VAT for all European countries on March 1, 2025. See [Sales tax exemption and VAT](https://docs.docker.com/subscription-billing/manage/tax-certificate/).


## [2025-01-30](https://docs.docker.com/platform-release-notes#2025-01-30)


### [New](https://docs.docker.com/platform-release-notes#new-26)


- Installing Docker Desktop via the PKG installer is now generally available.
- Enforcing sign-in via configuration profiles is now generally available.


## [2025-01-10](https://docs.docker.com/platform-release-notes#2025-01-10)


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-10)


- [Activity logs](https://docs.docker.com/accounts/organization/activity-logs/) now record when a settings policy is created, updated, deleted, or transferred.


## [2024-12-10](https://docs.docker.com/platform-release-notes#2024-12-10)


### [New](https://docs.docker.com/platform-release-notes#new-27)


- New Docker subscriptions are now available. For more information, see [Docker subscriptions and features](https://www.docker.com/pricing?ref=Docs&refAction=DocsPlatformReleaseNotes) and [Announcing Upgraded Docker Plans: Simpler, More Value, Better Development and Productivity](https://www.docker.com/blog/november-2024-updated-plans-announcement/).


## [2024-11-18](https://docs.docker.com/platform-release-notes#2024-11-18)


### [New](https://docs.docker.com/platform-release-notes#new-28)


- Administrators can now:
  - Enforce sign-in with [configuration profiles](https://docs.docker.com/desktop/enterprise/enforce-sign-in/methods/#configuration-profiles-method-mac-only) (Early Access).
  - Enforce sign-in for more than one organization at a time (Early Access).
  - Deploy Docker Desktop for Mac in bulk with the [PKG installer](https://docs.docker.com/desktop/enterprise/enterprise-deployment/pkg-install-and-configure/) (Early Access).
  - [Use Desktop Settings Management via the Docker Admin Console](https://docs.docker.com/desktop/enterprise/hardened-desktop/settings-management/configure-admin-console/) (Early Access).


### [Bug fixes and enhancements](https://docs.docker.com/platform-release-notes#bug-fixes-and-enhancements-11)


- Enhanced Container Isolation (ECI) has been improved to:
  - Permit administrators to [turn off Docker socket mount restrictions](https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/config/#allowing-all-containers-to-mount-the-docker-socket).
  - Support wildcard tags when using the [`allowedDerivedImages` setting](https://docs.docker.com/desktop/enterprise/hardened-desktop/enhanced-container-isolation/config/#docker-socket-mount-permissions-for-derived-images).


## [2024-11-11](https://docs.docker.com/platform-release-notes#2024-11-11)


### [New](https://docs.docker.com/platform-release-notes#new-29)


- [Personal access tokens](https://docs.docker.com/security/access-tokens/personal-access-tokens/) (PATs) now support expiration dates.


## [2024-10-15](https://docs.docker.com/platform-release-notes#2024-10-15)


### [New](https://docs.docker.com/platform-release-notes#new-30)


- Beta: You can now create [organization access tokens](https://docs.docker.com/security/access-tokens/organization-access-tokens/) (OATs) to enhance security for organizations and streamline access management for organizations in the Docker Admin Console.


## [2024-08-29](https://docs.docker.com/platform-release-notes#2024-08-29)


### [New](https://docs.docker.com/platform-release-notes#new-31)


- Deploying Docker Desktop via the [MSI installer](https://docs.docker.com/desktop/enterprise/enterprise-deployment/msi-install-and-configure/) is now generally available.
- Two new methods to [enforce sign-in](https://docs.docker.com/desktop/enterprise/enforce-sign-in/) (Windows registry key and `.plist` file) are now generally available.


## [2024-08-24](https://docs.docker.com/platform-release-notes#2024-08-24)


### [New](https://docs.docker.com/platform-release-notes#new-32)


- Administrators can now view [organization Insights](https://docs.docker.com/accounts/organization/insights/).


## [2024-07-17](https://docs.docker.com/platform-release-notes#2024-07-17)


### [New](https://docs.docker.com/platform-release-notes#new-33)


- You can now centrally access and manage Docker products in [Docker Home](https://app.docker.com).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker Agentic Platform plans

`https://docs.docker.com/subscription-billing/plans/docker-agentic-platform`

# Docker Agentic Platform plans


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


> Tip
>
> Docker Agentic Platform signups receive a one-time promotional credit toward cloud compute usage. To review your balance, see [Credits](https://docs.docker.com/subscription-billing/manage/#credits).


[Docker Agentic Platform](https://agentic-platform.docker.com/) is a pay-as-you-go plan for running agent and tool workloads in isolated sandboxes with Docker-managed cloud infrastructure. You pay for the usage you accrue without a recurring subscription fee.


To activate access for the Console, cloud sandbox CLI, or API and SDKs, follow [Signup and billing](https://docs.docker.com/agentic-platform/signup/#activate-cloud-access).


## [Usage](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform#usage)


> Note
>
> Subscribe using your personal Docker account, including if you belong to an organization. The subscription is attached to your personal account.


Docker Agentic Platform requires bringing your own API keys for inference. Your inference provider handles those costs.


After you subscribe, your invoice reflects metered, pay-as-you-go compute usage. Docker meters compute usage in seconds, based on sandbox runtime and the vCPU plus memory configuration you choose at setup. Different sandbox configurations can produce different costs.


You can track usage and pricing from the [Usage & billing](https://agentic-platform.docker.com/usage) page in Agentic Platform.


To track usage for Docker Agentic Platform from Docker Home:


1. Sign in to [Docker Home](https://app.docker.com/), then choose your account.
2. Go to **Billing** to view the Overview page, then go to **Active subscriptions**.
3. Select **Manage** next to **Docker Agentic Platform**.
4. View the estimated totals and usage for the current pay period.


## [Billing cycle](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform#billing-cycle)


Docker Agentic Platform is billed monthly on the day you subscribe. Your invoice reflects compute usage accrued during the previous period. For example:


- If you subscribed on September 10, you are billed on October 10.
- Your invoice from October 10 reflects accrued usage from September 10 through October 9.
- Your invoice can take up to 24 hours after your billing date to appear.


## [Cancel a plan](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform#cancel-a-plan)


Canceling Docker Agentic Platform disables subscription renewal at the start of the next plan period. Docker bills you for usage at the end of the plan period.


1. Sign in to [Docker Home](https://app.docker.com/) and go to **Billing**.
2. From **Active subscriptions**, select **Manage** next to **Docker Agentic Platform**.
3. Select **Cancel subscription**.
4. Review your usage, then select **Cancel subscription** to confirm.


## [Next steps](https://docs.docker.com/subscription-billing/plans/docker-agentic-platform#next-steps)


- To add or cancel a plan, see [Manage plans](https://docs.docker.com/subscription-billing/manage/plans/)
- To track usage across plans, see [Usage](https://docs.docker.com/subscription-billing/manage/#usage)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Get started with Docker Agentic Platform

`https://docs.docker.com/agentic-platform/get-started`

# Get started with Docker Agentic Platform


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Use a cloud sandbox to have an agent review a project without setting up the project on your computer. In this walkthrough, you'll launch Claude Code, clone a public sample application, and save a project review. Then you'll pause the sandbox to return later or delete it when you're finished.


You can complete the walkthrough in the browser. An optional step shows how to open the same project in VS Code or Cursor over SSH.


## [Before you begin](https://docs.docker.com/agentic-platform/get-started#before-you-begin)


You need:


- A personal Docker account with an active [Docker Agentic Platform subscription](https://docs.docker.com/agentic-platform/signup/#activate-cloud-access).
- An Anthropic API key for the Claude Code kit. Add it under **Secrets** or enter it when you launch the sandbox. Your model provider bills inference separately from Docker's sandbox compute charges.


This example uses a public repository, so you don't need a GitHub token. For other agents and their credentials, see [Kits](https://docs.docker.com/agentic-platform/kits/) and [Secrets](https://docs.docker.com/agentic-platform/secrets/).


## [Start a sandbox](https://docs.docker.com/agentic-platform/get-started#start-a-sandbox)


1. Open [Docker Agentic Platform](https://agentic-platform.docker.com/) and select **New**.
2. Choose the Claude Code kit.
3. Add your Anthropic API key if it isn't already saved. Don't enter it in the agent's prompt or in a file inside the sandbox.
4. Keep the defaults and select **Run**.


On your first launch, the default **Open** network policy permits outbound access to any host. If you're using a custom policy, make sure it permits GitHub and your model provider. See [Network policies](https://docs.docker.com/agentic-platform/policies/).


When the sandbox is ready, its terminal opens with Claude Code. After launch, you can't change the selected credentials, tools, network policies, or compute size. See [Sandbox options](https://docs.docker.com/agentic-platform/get-started#sandbox-options) for other launch settings.


## [Give the agent a task](https://docs.docker.com/agentic-platform/get-started#give-the-agent-a-task)


Your local files aren't mounted in a cloud sandbox. Ask Claude Code to clone and review a public sample project:


```text
Clone https://github.com/docker/welcome-to-docker.git into
/home/agent/workspace/project, then review the application.
Read the source, package.json, and Dockerfile. Don't modify the application
or install dependencies.
Write /home/agent/workspace/review.md with:
- A short explanation of what the application does.
- The commands defined in package.json for running and building it.
- An explanation of how the Dockerfile builds and serves the application.
- One small improvement you'd recommend, with the relevant file path.
Base the review on the files you read. Don't claim to have run the application.
Summarize your findings in your response.
```


Claude Code summarizes the project in the conversation and saves the review at `/home/agent/workspace/review.md`. You can ask follow-up questions or give it another task in the same session.


## [Keep your work](https://docs.docker.com/agentic-platform/get-started#keep-your-work)


The cloned project and review are stored in the sandbox. Files don't sync automatically with your computer or a remote repository. They remain available when you pause and resume the sandbox, but are lost when you delete it.


To keep files outside the sandbox, use the CLI to [transfer files](https://docs.docker.com/ai/sandboxes/cloud/usage/#transfer-files), or commit and push changes to a repository. Include a [GitHub credential](https://docs.docker.com/agentic-platform/secrets/#github-credential) when launching a sandbox that needs to push changes.


## [Open the project in your editor (optional)](https://docs.docker.com/agentic-platform/get-started#open-the-project-in-your-editor-optional)


Open the project and review in VS Code or Cursor over SSH. Your editor runs on your computer, while the files and terminal commands stay in the cloud sandbox.


1. Install the [Docker Sandboxes CLI](https://docs.docker.com/ai/sandboxes/install/), version 0.45.0 or later.
2. In a terminal on your computer, sign in with the same Docker account you used in the Console and configure cloud SSH access: ```console $ sbx login $ sbx --cloud setup ssh $ sbx --cloud ls ```
3. Find your sandbox in the list and copy its `sbx_` -prefixed ID. Test the connection, replacing `<SANDBOX_ID>` with that ID: ```console $ ssh <SANDBOX_ID>@sbx_cloud ``` A successful connection opens a shell inside the cloud sandbox. Run `exit` to return to your computer's terminal.
4. In VS Code, install the [Remote - SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh). In Cursor, install its Remote - SSH support.
5. Open your editor's Command Palette and run **Remote-SSH: Connect to Host**. Enter `<SANDBOX_ID>@sbx_cloud`, using the same ID as in the SSH command.
6. Open `/home/agent/workspace` in the remote window. You'll find the cloned application in `project` and the agent's output in `review.md`.


The first connection installs the editor's server inside the sandbox.


To download the review, run this command in a terminal on your computer:


```console
$ sbx --cloud cp <SANDBOX_ID>:/home/agent/workspace/review.md ./review.md
```


## [Pause, keep running, or delete the sandbox](https://docs.docker.com/agentic-platform/get-started#pause-keep-running-or-delete-the-sandbox)


Closing the browser or disconnecting your editor leaves the sandbox running. An agent can continue working until you pause or delete the sandbox, or its timer expires. Compute is billed while the sandbox runs, even when the agent has finished its task.


Return to **Sandboxes** in the Console and choose what to do next:


- Pause the sandbox to stop compute charges and keep its files. Confirm that it is paused in the list. To continue later, reopen the sandbox and resume it. Resuming starts a fresh timer with the original duration.
- Leave it running if the agent still has work to do. Check the expiration time: the default **Stop** action stops the sandbox after one hour, including background processes, and keeps its files.
- Delete it when you no longer need it. Save the review or push any changes you want to keep first. Deletion removes files stored only in the sandbox.


For more detail, see [Lifecycle actions](https://docs.docker.com/agentic-platform/sandboxes/#manage-the-lifecycle). To run a task from your own terminal, follow the [cloud CLI walkthrough](https://docs.docker.com/ai/sandboxes/cloud/#get-started). For programmatic workflows, see the [Sandboxes API quickstart](https://docs.docker.com/ai/sandboxes-api/get-started/).


## [Sandbox options](https://docs.docker.com/agentic-platform/get-started#sandbox-options)


Configure these options before selecting **Run**:


| Option | What to choose |
| --- | --- |
| Agent credentials | Add the API keys or tokens your kit needs. Saved credentials are reused by default; deselect optional credentials you don't want to include. See [Secrets](https://docs.docker.com/agentic-platform/secrets/). |
| GitHub token | Provide a token for Copilot or for cloning private repositories and pushing changes. Copilot uses the same token for both. Repository access is optional for other agents. See [GitHub credential](https://docs.docker.com/agentic-platform/secrets/#github-credential). |
| Network policies | Review the hosts and services the sandbox can reach. See [Network policies](https://docs.docker.com/agentic-platform/policies/). |
| MCP tools | Choose the servers your agent can use and authorize them if prompted. See [MCP](https://docs.docker.com/agentic-platform/mcp/). |
| Compute and platform | Choose CPU and memory resources. Under **Platform**, use **auto** or a platform supported by the kit's image. See [Sandbox platforms](https://docs.docker.com/agentic-platform/sandboxes/#choose-a-platform). |
| Timer | Under **Run for**, choose 1 to 24 hours. Under **When the time is up**, choose **Stop**, **Delete**, or **Restart** if offered. See [Lifecycle actions](https://docs.docker.com/agentic-platform/sandboxes/#manage-the-lifecycle). |


The launcher remembers your policy selections from the previous launch in the same browser. Policies marked **Always applied** are selected automatically. Review the selected policies before launching. Selecting **Balanced** alongside **Open** doesn't restrict Open's access; see [How policies combine](https://docs.docker.com/agentic-platform/policies/#how-policies-combine).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Governance

`https://docs.docker.com/ai/sandboxes/governance`

# Governance


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


[Explore the AI Governance API 1 →](https://docs.docker.com/reference/api/ai-governance/latest/)


The governance described here applies to local sandboxes. Cloud sandboxes use separate network policy configuration. See [Cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) for cloud controls.


Sandbox governance covers the policy system that controls what sandboxes can access over the network, on the filesystem, and through MCP. For MCP setup and server registration, see [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/). Governance operates at two layers:


**Local policy** is configured per machine using the `sbx policy` CLI. It lets individual developers customize which domains their sandboxes can reach. See [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/).


**Organization policy** is configured centrally in Docker Home. Network and filesystem policies can also be managed via the [Governance API](https://docs.docker.com/reference/api/ai-governance/). Controls defined at the org level apply uniformly across every local sandbox in the organization. Organization governance can also include MCP policies for sandbox MCP activity. When organization governance is active, only organization allow rules grant access: local `sbx policy` allow rules are no longer evaluated, while local deny rules still apply on top. See [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/).


Alongside this access-control policy, admins can require developers to sign in as members of their organization before using sandboxes at all. [Sign-in enforcement](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement/) is deployed through endpoint management and ensures developers can't bypass organization policy by using a personal account.


> Note
>
> Organization governance is available on a separate paid subscription. [Contact Docker Sales](https://www.docker.com/products/ai-governance/#contact-sales) to request access.


## [Learn more](https://docs.docker.com/ai/sandboxes/governance#learn-more)


Start with [Policy concepts](https://docs.docker.com/ai/sandboxes/governance/concepts/) for the resource model, rule syntax, MCP policy basics, evaluation, and precedence.


### [Access controls](https://docs.docker.com/ai/sandboxes/governance#access-controls)


- [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/): configure network rules on your machine with the `sbx policy` CLI.
- [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/): centrally manage sandbox policies across your organization.
- [Network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/): control outbound network access from sandboxes, by host or by HTTP method and path.
- [Filesystem access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/): control which host paths sandboxes can mount as workspaces.
- [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/): control MCP server registration, tool calls, resources, prompts, and approval gates.


### [Monitor and enforce](https://docs.docker.com/ai/sandboxes/governance#monitor-and-enforce)


- [Monitoring policies](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/): inspect active rules and monitor sandbox network traffic with `sbx policy ls` and `sbx policy log`.
- [Audit logs](https://docs.docker.com/ai/sandboxes/governance/audit/): view, configure, export, and collect governance audit records.
- [Sign-in enforcement](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/sign-in-enforcement/): require developers to sign in as organization members, enforced through endpoint management.


### [Reference](https://docs.docker.com/ai/sandboxes/governance#reference)


- [AI Governance API](https://docs.docker.com/reference/api/ai-governance/): manage network and filesystem org policies programmatically.
- [MCP policy reference](https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/): look up Docker MCP policy actions, resources, attributes, context fields, and approval behavior.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Access controls

`https://docs.docker.com/ai/sandboxes/governance/access-controls`

# Access controls


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Access controls are expressed as policies. Local and organization pages describe where policies apply. Network and filesystem pages describe the rules inside those policies. MCP policies use Cedar statements instead of the network and filesystem rule format.


## [Policy scope](https://docs.docker.com/ai/sandboxes/governance/access-controls#policy-scope)


- [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/): configure network rules on a developer machine with the `sbx policy` CLI.
- [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/): manage centralized policies for an organization or team.


## [Access surfaces](https://docs.docker.com/ai/sandboxes/governance/access-controls#access-surfaces)


- [Network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/): control outbound network access from sandboxes, by host or by HTTP method and path.
- [Filesystem access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/): control which host paths sandboxes can mount as workspaces.
- [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/): control MCP server registration, tool calls, resources, prompts, and approval gates with Cedar policy.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Manage cloud network policy

`https://docs.docker.com/ai/sandboxes/cloud/network-policy`

# Manage cloud network policy


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Cloud network policy controls outbound connections from cloud sandboxes. It is a separate, network-only policy store with Docker account and individual sandbox scopes.


> Important
>
> Local policy configuration isn't copied to cloud sandboxes. Configure cloud rules with `sbx --cloud policy` and verify network access using connection checks and policy logs.


## [Understand policy scope](https://docs.docker.com/ai/sandboxes/cloud/network-policy#understand-policy-scope)


The cloud CLI supports account and sandbox policy scopes. Your account policy supplies the default for cloud sandboxes you create in the Docker account. A sandbox policy adds rules for one cloud sandbox. Matching deny rules take precedence over allow rules across the applicable policies.


Cloud creation uses cloud account policy, network rules passed to the command, and network access declared by the agent or kit. Both `sbx --cloud create` and `sbx --cloud run` leave local network and organization policies on the host. Moving a local sandbox to the cloud works the same way, except that rules you added locally don't transfer.


Define the intended policy in the cloud store. After creation, inspect the configured rules and [verify connection decisions](https://docs.docker.com/ai/sandboxes/cloud/network-policy#inspect-network-policy).


## [Initialize account policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy#initialize-account-policy)


Set the account policy to `allow-all`, `balanced`, or `deny-all`:


```console
$ sbx --cloud policy init deny-all
```


The default applies to your cloud sandboxes in the Docker account. You can add rules after initialization or specify initial rules when creating a sandbox. A deny-all default still permits destinations allowed by applicable sandbox or agent-kit rules.


The `balanced` preset sets deny-all as the default and adds allow rules for common development services. To set a default for one sandbox, use `sbx --cloud policy init deny-all --sandbox cloud-project`.


You can run `init` again to change the default. Existing allow and deny rules remain in place. Use `reset` to remove account rules before choosing another preset.


*Set the account policy to allow-all, balanced, or deny-all:*

## [Add network rules](https://docs.docker.com/ai/sandboxes/cloud/network-policy#add-network-rules)


Add an account-level exception:


```console
$ sbx --cloud policy allow network api.github.com:443
```


Scope a rule to one sandbox:


```console
$ sbx --cloud policy allow network api.anthropic.com:443 \
    --sandbox cloud-project
```


Deny rules take precedence when the same destination matches both an allow rule and a deny rule.


Cloud rules match network destinations. HTTP method and path restrictions, `--protocol`, and local governance profiles aren't supported.


You can also add initial rules while creating a sandbox:


```console
$ sbx --cloud create --name cloud-project \
    --allow-network api.github.com:443 \
    --deny-network example.com claude
```


## [Inspect network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy#inspect-network-policy)


Inspect your account policy or a sandbox's configured policy:


```console
$ sbx --cloud policy ls
$ sbx --cloud policy ls cloud-project
```


The sandbox view shows its policy document, or your account default when the sandbox has no policy document. It does not show the complete combination of applicable rules.


To verify enforcement, attempt the connection from the sandbox, then review the connection decisions:


```console
$ sbx --cloud exec cloud-project curl -I https://api.github.com
$ sbx --cloud policy log cloud-project
```


These records describe cloud network policy decisions. They aren't Docker AI Governance organization audit logs.


## [Remove network rules](https://docs.docker.com/ai/sandboxes/cloud/network-policy#remove-network-rules)


Remove a rule by its pattern, from whichever allow or deny list contains it:


```console
$ sbx --cloud policy rm network --resource api.github.com:443
$ sbx --cloud policy rm network --sandbox cloud-project --resource api.anthropic.com:443
```


Remove the custom account policy and return to the platform default:


```console
$ sbx --cloud policy reset
```


The command asks for confirmation and prints the default stored by the server after the reset. Use `--force` in scripts. The local daemon is unaffected. Sandbox-specific policies remain in place and can still grant access. Inspect those policies separately.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Local policy

`https://docs.docker.com/ai/sandboxes/governance/access-controls/local`

# Local policy


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The `sbx policy` command manages the local policy on your machine. The local policy contains network access rules. Rules apply to all sandboxes on the machine when you use the global scope, or to a single sandbox when scoped by name.


Local policy interacts with organization governance as follows:


- **No org governance**: the local policy controls what sandboxes can access.
- **Org governance active**: only organization allow rules grant access, so local allow rules are inactive and can't expand what the organization permits. Local deny rules are still evaluated, so you can restrict access further than the organization policy does. To list inactive rules, run `sbx policy ls --include-inactive`. See [Monitoring](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/#showing-inactive-rules).


See [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/) for how organization governance works.


For domain patterns, wildcards, CIDR ranges, and filesystem path syntax, see [Policy concepts](https://docs.docker.com/ai/sandboxes/governance/concepts/#rule-syntax).


*See Organization policies for how organization governance
works.*

## [Default preset](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#default-preset)


Outbound TCP traffic passes through a proxy on your host, which enforces access rules on every connection. Non-HTTP TCP traffic, including SSH, can be allowed with a hostname rule (for example, `sbx policy allow network "myhost:22"`) or an address-based rule. UDP requires the experimental feature and policy rules described in [Allow outbound UDP](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#allow-outbound-udp). ICMP is blocked.


If you haven't chosen a default preset, the CLI prompts you before it runs a sandbox. Running `sbx policy reset` clears the preset and prompts you to choose again:


```text
Initialize the global network policy for your sandboxes:

  Applies to all sandboxes, current and future — change it later with
  "sbx policy allow/deny/rm". Kits, including built-in agent kits, may
  also add per-sandbox rules.

     1. Open         — All network traffic allowed, no restrictions.
  ❯  2. Balanced     — Default deny, with common dev sites allowed.
     3. Locked Down  — All network traffic blocked unless you allow it.

  Use ↑/↓ or 1–3 to navigate, Enter to confirm, Esc to cancel.
```


| Preset | Description |
| --- | --- |
| Open | All outbound TCP traffic is allowed. Equivalent to adding a wildcard allow rule with `sbx policy allow network "**"`. |
| Balanced | Default deny, with a baseline allowlist covering AI provider APIs, package managers, code hosts, container registries, and common cloud services. |
| Locked Down | No baseline allow rules. Destinations need an allow rule from you or a kit. |


Presets initialize the global policy. Built-in agent kits and other kits can add per-sandbox allow rules, including under **Locked Down** (`deny-all`). The preset isn't an explicit deny rule that overrides those allowances.


Under **Balanced** and **Locked Down**, a sandbox request that no rule matches is blocked and asks for your approval instead of being denied outright, so you can open access to each destination as a sandbox needs it. See [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


To inspect the rules a kit adds to a sandbox, run:


```console
$ sbx policy ls my-sandbox --source kit --type network --wide
```


To block a destination allowed by a kit, add an explicit deny rule:


```console
$ sbx policy deny network --sandbox my-sandbox openrouter.ai
```


Deny rules take precedence over allow rules. See [Policy precedence](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence).


The **Balanced** preset's baseline allowlist is a good starting point for most workflows. Run `sbx policy ls` to see exactly which rules it includes.


> Note
>
> If your organization manages sandbox policies centrally, organization rules take precedence over the preset you select here. See [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/).


### [Non-interactive environments](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#non-interactive-environments)


In non-interactive environments such as CI pipelines or headless servers, the interactive prompt can't be displayed. Use `sbx policy init` to set the preset before running any other `sbx` commands:


```console
$ sbx policy init balanced
```


Available values are `allow-all`, `balanced`, and `deny-all`.


*Deny rules take precedence over allow rules. See
Policy precedence.*

*Available values are allow-all, balanced, and deny-all.*

## [Managing rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#managing-rules)


A rule covers a destination host. It can also name HTTP methods and paths to narrow the match to part of that host.


### [Network rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#network-rules)


Use [`sbx policy allow`](https://docs.docker.com/reference/cli/sbx/policy/allow/) and [`sbx policy deny`](https://docs.docker.com/reference/cli/sbx/policy/deny/) to add or restrict access on top of the active preset. Changes take effect immediately. Rules apply to all sandboxes by default:


```console
$ sbx policy allow network api.anthropic.com
$ sbx policy deny network ads.example.com
```


Pass `--sandbox <name>` to scope a rule to one sandbox:


```console
$ sbx policy allow network --sandbox my-sandbox api.example.com
$ sbx policy deny network --sandbox my-sandbox ads.example.com
```


As of v0.38.0, you can also set per-sandbox deny rules at creation time with `--deny-network` on `sbx create` or `sbx run`, instead of adding them after the fact:


```console
$ sbx create --deny-network ads.example.com claude .
$ sbx run --deny-network ads.example.com claude
```


Pass the flag multiple times to deny more than one host. Rules added this way appear in `sbx policy ls <name>` and can be removed with `sbx policy rm network --sandbox <name> --resource <host>`.


Specify multiple hosts in one command with a comma-separated list:


```console
$ sbx policy allow network "api.anthropic.com,*.npmjs.org,*.pypi.org"
```


Remove a rule by resource or by rule ID:


```console
$ sbx policy rm network --resource ads.example.com
$ sbx policy rm network --id 2d3c1f0e-4a73-4e05-bc9d-f2f9a4b50d67
```


To remove a sandbox-scoped rule, pass `--sandbox <name>`:


```console
$ sbx policy rm network --sandbox my-sandbox --resource api.example.com
```


### [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#http-method-and-path-rules)


Add `--method` to an allow or deny rule to match specific HTTP methods on a host, and `--path` to restrict it to part of the host's URL space:


```console
$ sbx policy allow network api.github.com --method GET --path '/repos/org/project/**'
```


Quote the path so your shell doesn't expand the wildcard. Pass several methods as a comma-separated list:


```console
$ sbx policy allow network api.github.com --method GET,HEAD
```


`--method ANY` matches every HTTP method, and `--path` defaults to `/**` when you omit it:


```console
$ sbx policy allow network api.github.com --method ANY
```


`ANY` can't be combined with specific methods, and a path without a method is rejected. Pass a method, or use `ANY` when you mean every method.


Method names are case-insensitive. The accepted values are `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, `CONNECT`, and `TRACE`.


A path must start with `/` and be canonical. It can't contain a query string, a fragment, percent-encoding, control characters, surrounding whitespace, repeated or trailing slashes, or dot segments such as `.` and `..`. Each rule takes one path. Repeating `--path` keeps only the last value, and a comma is read as part of the path, so add a separate rule for each path:


```console
$ sbx policy allow network api.github.com --method GET --path '/repos/**'
$ sbx policy allow network api.github.com --method GET --path '/users/**'
```


Hosts follow the same patterns as network rules and can include a port. Write the host on its own, without a scheme, so an HTTP rule takes `api.example.com` rather than `https://api.example.com`.


A local HTTP rule takes a hostname. To match an IP address or a CIDR range, add a plain network rule for that destination instead.


Deny rules take the same flags, which is the usual way to carve a method or path out of a broader allow:


```console
$ sbx policy allow network api.example.com
$ sbx policy deny network api.example.com --method POST --path '/admin/**'
```


For how the two layers combine, see [HTTP rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#http-method-and-path).


Remove an HTTP rule by naming the same qualifiers you added it with, or by rule ID:


```console
$ sbx policy rm network --resource api.github.com --method GET --path '/repos/org/project/**'
$ sbx policy rm network --id 7f3a1c2e-4a73-4e05-bc9d-f2f9a4b50d67
```


List HTTP rules with `--type http`, or see them alongside network rules in a wide listing, where the `METHOD` and `PATH` columns are empty for rules that match a whole host:


```console
$ sbx policy ls --wide
TYPE      METHOD   PATH
network   -        -
http      GET      /repos/org/project/**
```


> Note
>
> `sbx policy check network` and `sbx policy log` don't evaluate or display HTTP methods and paths. A check reports the decision for the host, which can differ from the decision for a specific method and path on that host.


*Pass --sandbox <name> to scope a rule to one sandbox:*

*To remove a sandbox-scoped rule, pass --sandbox <name>:*

*For how the two layers combine, see
HTTP rules.*

## [Inspecting rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#inspecting-rules)


To inspect which policies are active and where they come from, use `sbx policy ls`. Use `--source` to filter by origin (`local`, `org`, `kit`), `--decision` to filter by outcome (`allow`, `deny`), and `--wide` for rule-level detail including rule IDs. To inspect a single policy or rule in full, use `sbx policy inspect`. See [Monitoring](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/).


### [Allow outbound UDP](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#allow-outbound-udp)


Outbound UDP is experimental and disabled by default. Turn on experimental features and UDP egress before adding UDP allow rules:


```console
$ sbx settings set platform.allowExperimentalFeatures true
$ sbx settings set feature.udp-egress true
$ sbx policy allow network --protocol udp api.example.com:443
```


Local allow rules apply to TCP by default. Use `--protocol udp` for UDP or `--protocol tcp,udp` for both. Deny rules apply to both protocols by default. Use `--protocol` to restrict a deny rule to one protocol.


UDP follows the same organization and local policy precedence as TCP. It is refused when the destination requires an HTTP, SOCKS5, system, or PAC-selected proxy, because those proxies can't carry UDP. ICMP remains blocked.


UDP to local-network destinations is blocked before any policy is evaluated, so no allow rule can permit it, including one that allows all hosts. This covers multicast, link-local, and unspecified addresses, `255.255.255.255`, and the broadcast addresses of the host's networks. As a result, discovery protocols that use multicast, such as mDNS and SSDP, don't work from a sandbox. UDP to `host.docker.internal` isn't affected. The network log records these connections under the rule `<udp local network boundary>`.


Inspect UDP rules or check a destination:


```console
$ sbx policy ls --protocol udp
$ sbx policy check network --protocol udp api.example.com:443
```


The CLI warns if you save a UDP rule while UDP egress is disabled.


## [Testing policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#testing-policy)


Before running a sandbox, you can check whether the current policy would allow a network request with `sbx policy check network`:


```console
$ sbx policy check network api.anthropic.com
$ sbx policy check network blocked.example.com
```


The output reports `Allowed` or `Denied`, along with governance and context details. A denied check returns a non-zero exit status.


The target can be a hostname, a `host:port` pair, an IP address, or a URL. Bare hostnames and IP addresses are evaluated against port 443. This is useful for verifying custom rules or checking what the Locked Down preset blocks before you start an agent.


A check never creates an approval request. A destination that a sandbox would ask you to approve shows as `Denied:`, with a `Reason:` line of `no matching allow rule (default deny)`, or `approval required by policy` under organization governance.


To check policy in the context of a specific sandbox:


```console
$ sbx policy check network --sandbox my-sandbox api.example.com
```


### [Resetting](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#resetting)


To remove all custom rules and start fresh with a new preset, use `sbx policy reset`:


```console
$ sbx policy reset
```


This deletes the local policy store, restarts the daemon, and prompts you to choose a new preset. Running sandboxes stop when the daemon shuts down. Pass `--force` to skip the confirmation prompt:


```console
$ sbx policy reset --force
```


## [Troubleshooting](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#troubleshooting)


### [Local allow rules have no effect](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#local-allow-rules-have-no-effect)


If rules you add with `sbx policy allow` don't change sandbox behavior, your organization likely has governance enabled. Run `sbx policy ls` to check: if the summary block contains `Governance: Managed by <org>`, org governance is active. When it's active, local allow rules are inactive. You can't use them to loosen restrictions the org policy imposes.


Inactive allow rules are hidden from `sbx policy ls` by default; run `sbx policy ls --include-inactive` to see them with an `inactive` status in the `STATUS` column.


When organization governance is active, only organization allow rules can grant access. Ask your admin to update the organization policy if you need access to an additional resource. Local deny rules remain active, so you can use `sbx policy deny` to restrict access further.


### [A domain is still blocked after adding an allow rule](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#a-domain-is-still-blocked-after-adding-an-allow-rule)


If a domain remains blocked after you add a local allow rule, your organization likely enforces governance, which makes local allow rules inactive. Run `sbx policy ls` to check whether org governance is active; if the output starts with a `Governance:` status line showing `Managed by <org>`, it is. Add `--include-inactive` to confirm your rule shows an `inactive` status. If so, the block can only be lifted by updating the org policy in Docker Home or via the [API](https://docs.docker.com/reference/api/ai-governance/).


### [An HTTP method or path is blocked on an allowed host](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#an-http-method-or-path-is-blocked-on-an-allowed-host)


A host that a network rule allows can still have individual methods or paths denied by an HTTP rule. Run `sbx policy ls --type http` to see which HTTP rules apply. `sbx policy check network` reports the decision for the host only, so it shows a host as allowed even when the specific request is denied. See [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#http-method-and-path-rules).


### [A request is blocked with "Approval required"](https://docs.docker.com/ai/sandboxes/governance/access-controls/local#a-request-is-blocked-with-approval-required)


The destination needs your confirmation. Either no allow or deny rule matches it and your machine isn't under organization governance, or an organization policy allows it but requires approval first.


Run `sbx policy approval ls` to see the pending request and respond to it with `sbx policy approval respond`. Approving applies to later requests, not the one that was blocked, so run the operation again afterward. See [Respond to an approval request](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#respond-to-an-approval-request).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Docker core roles and permissions

`https://docs.docker.com/security/roles-and-permissions/core-roles`

# Docker core roles and permissions


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

For:
Administrators


Docker organizations use built-in Member, Editor, and Owner roles with predefined permissions. This reference compares their permissions across Docker products. To assign a different combination of permissions, use [custom roles](https://docs.docker.com/security/roles-and-permissions/custom-roles/) instead.


## [Core roles](https://docs.docker.com/security/roles-and-permissions/core-roles#core-roles)


Docker organizations have three core roles:


- Owner provides full administrative access. Owners can manage all organization settings, including repositories, teams, members, billing, and security features.
- Editor has partial administrative access. Editors can create, edit, and delete repositories. They can also manage team permissions for repositories.
- Member has basic, non-administrative access. Members can view other organization members and pull images from repositories they have access to.


A company owner has the same organization-management permissions as an organization owner. Content and registry permissions, such as repository pull and push, don't apply to company owners. For more information, see [Company overview](https://docs.docker.com/accounts/company/).


## [Permissions reference](https://docs.docker.com/security/roles-and-permissions/core-roles#permissions-reference)


### [Content and registry](https://docs.docker.com/security/roles-and-permissions/core-roles#content-and-registry)


These permissions apply organization-wide.


| Permission | Member | Editor | Owner |
| --- | --- | --- | --- |
| Explore images and extensions | ✅ | ✅ | ✅ |
| Star, favorite, vote, and comment on content | ✅ | ✅ | ✅ |
| Pull images | ✅ | ✅ | ✅ |
| Create and publish an extension | ✅ | ✅ | ✅ |
| Become a Verified, Official, or Open Source publisher | ❌ | ❌ | ✅ |
| Edit and delete publisher repository logos | ❌ | ✅ | ✅ |
| Configure DVP analytics settings | ❌ | ✅ | ✅ |
| Observe content engagement as a publisher | ❌ | ❌ | ✅ |
| Create public and private repositories | ❌ | ✅ | ✅ |
| Disable public repositories | ❌ | ✅ | ✅ |
| Edit and delete repositories | ❌ | ✅ | ✅ |
| Manage tags | ❌ | ✅ | ✅ |
| View repository activity | ❌ | ❌ | ✅ |
| Set up Automated builds | ❌ | ❌ | ✅ |
| Edit build settings | ❌ | ❌ | ✅ |
| View teams | ✅ | ✅ | ✅ |
| Assign team permissions to repositories | ❌ | ✅ | ✅ |
| Manage OIDC connections | ❌ | ✅ | ✅ |


You can grant repository permissions beyond a member's organization role:


- Role permissions: Applied organization-wide (member or editor)
- Team permissions: Additional permissions for specific repositories


To extend access to private repositories, configure team permissions. Custom roles can grant organization-wide permissions to manage repositories (create, edit, delete) but don't grant pull access to private repositories. Use team permissions for that.


### [Organization management](https://docs.docker.com/security/roles-and-permissions/core-roles#organization-management)


| Permission | Member | Editor | Owner |
| --- | --- | --- | --- |
| Create teams | ❌ | ❌ | ✅ |
| Manage teams (including delete) | ❌ | ❌ | ✅ |
| Configure the organization's settings (including linked services) | ❌ | ❌ | ✅ |
| Add organizations to a company | ❌ | ❌ | ✅ |
| Invite members | ❌ | ❌ | ✅ |
| Manage members | ❌ | ❌ | ✅ |
| Manage member roles and permissions | ❌ | ❌ | ✅ |
| View member activity | ❌ | ❌ | ✅ |
| Export and reporting | ❌ | ❌ | ✅ |
| Image Access Management | ❌ | ❌ | ✅ |
| Registry Access Management | ❌ | ❌ | ✅ |
| Namespace access control | ❌ | ❌ | ✅ |
| Set up Single Sign-On (SSO) and SCIM | ❌ | ❌ | ✅ * |
| Require Docker Desktop sign-in | ❌ | ❌ | ✅ * |
| Manage billing information (for example, billing address) | ❌ | ❌ | ✅ |
| Manage payment methods (for example, credit card or invoice) | ❌ | ❌ | ✅ |
| View billing history | ❌ | ❌ | ✅ |
| Manage subscriptions | ❌ | ❌ | ✅ |
| Manage seats | ❌ | ❌ | ✅ |
| Upgrade and downgrade plans | ❌ | ❌ | ✅ |


> Tip
>
> For more granular access control, [upgrade to a Docker Business plan](https://www.docker.com/pricing?ref=Docs&refAction=DocsEnterpriseCoreRoles) to use [custom roles](https://docs.docker.com/security/roles-and-permissions/custom-roles/).


** If not part of a company*


### [Docker Scout](https://docs.docker.com/security/roles-and-permissions/core-roles#docker-scout)


| Permission | Member | Editor | Owner |
| --- | --- | --- | --- |
| View and compare analysis results | ✅ | ✅ | ✅ |
| Upload analysis records | ✅ | ✅ | ✅ |
| Activate and deactivate Docker Scout for a repository | ❌ | ✅ | ✅ |
| Create environments | ❌ | ❌ | ✅ |
| Manage registry integrations | ❌ | ❌ | ✅ |


### [Docker Build Cloud](https://docs.docker.com/security/roles-and-permissions/core-roles#docker-build-cloud)


| Permission | Member | Editor | Owner |
| --- | --- | --- | --- |
| Use a cloud builder | ✅ | ✅ | ✅ |
| Create and remove builders | ✅ | ✅ | ✅ |
| Configure builder settings | ✅ | ✅ | ✅ |
| Buy minutes | ❌ | ❌ | ✅ |
| Manage subscription | ❌ | ❌ | ✅ |


** If not part of a company*

## [Next steps](https://docs.docker.com/security/roles-and-permissions/core-roles#next-steps)


- [Custom roles](https://docs.docker.com/security/roles-and-permissions/custom-roles/): Create tailored permission sets on a Docker Business plan
- [Manage organization members](https://docs.docker.com/accounts/organization/manage/members/): Invite users and assign roles
- [Company overview](https://docs.docker.com/accounts/company/): Understand company owner permissions versus organization owner permissions[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# MCP access policies

`https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp`

# MCP access policies


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


MCP access policies let organization administrators control which Model Context Protocol (MCP) servers developers can register and what agents can do through Docker's MCP gateway. Use these policies to approve trusted servers, withdraw access to a server, require approval for tool calls, and restrict host-run servers. To register MCP servers and connect them to sandboxes, see [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/).


MCP access policies apply only to server registration and requests handled by Docker's MCP gateway. They don't govern an MCP server that an agent or MCP client configures and connects to directly from inside the sandbox. A direct connection to a remote MCP server is outbound sandbox traffic, so [network access policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/) determines whether the sandbox can reach the server. To prevent access through both paths, block the server in MCP access policy and block its network destination in network access policy.


Unlike [network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/) and [filesystem access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/), MCP policies are organization policies written in Cedar. Docker defines the `MCP` namespace, including the actions, resource types, attributes, and approval behavior that policies can match. This page focuses on representative access patterns. For Docker's exact policy surface, see the [MCP policy reference](https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/). For Cedar syntax and language semantics, see the [Cedar documentation](https://docs.cedarpolicy.com/).


## [Govern the server lifecycle](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#govern-the-server-lifecycle)


MCP policy applies at two points in a server's lifecycle. A rule for one point doesn't automatically govern the other.


| Admin decision | Evaluation point | Match with |
| --- | --- | --- |
| Whether a server can be registered | When a developer runs `sbx mcp add` | The registered name and resolved server attributes, such as `identityURL` |
| What agents can do through the MCP gateway | When the gateway handles a governed request | The registered server name, tool annotations, resource URI, or prompt name |


Registration rules affect future registrations. They don't remove a saved registration or prevent an existing registration from being loaded with `sbx mcp load`. Use-time rules govern tool calls, resource reads, and prompt retrieval from servers that are already registered or loaded.


Server names are chosen during registration. Registration rules can match the chosen name and resolved server identity together. At use time, tools, resources, and prompts are associated with the registered name, so rules for an existing server must match every name under which it was registered.


Built-in gateway tools, such as `mcp-add`, `code-mode`, and OAuth authorization helpers, are also governed at use time. They are `MCP::Primordial` resources rather than tools associated with a registered server. For details, see [Built-in gateway tools](https://docs.docker.com/ai/sandboxes/mcp-gateway/#built-in-gateway-tools).


Use-time policy doesn't hide or remove existing registrations. Tool and resource listings can also include entries that policy denies when an agent tries to use them.


## [Choose an access posture](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#choose-an-access-posture)


When MCP policy enforcement is active for a user, registration and governed MCP requests are denied unless a matching `permit` allows them. A matching `forbid` overrides any `permit`, including a permit with `@requireApproval`.


Use permits for an allowlist policy. For a blocklist policy that grants MCP activity except for explicit restrictions, start with an actionless permit:


```text
permit (principal, action, resource);
```


This statement permits every MCP action that reaches Cedar evaluation. Add `forbid` statements for the restrictions the policy must enforce.


Policy scope supplies the principal. Use organization or team scope instead of matching users, teams, tenants, or roles in Cedar. If MCP policy enforcement isn't active for a user, the gateway doesn't evaluate Cedar policy and permits MCP activity. MCP doesn't have a local preset equivalent to network policy.


## [Approve a server](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#approve-a-server)


For an allowlist, approve both the server registration and its use-time capabilities. The following policy approves a remote server only when it is registered as `example` with the expected identity URL. It permits read-only tool calls, resource reads, and prompt retrieval from that registered server:


```text
// Permit registration with the expected name and identity URL.
permit (principal, action == MCP::Action::"register", resource)
when {
  resource in MCP::Server::"example" &&
  resource.identityURL == "https://mcp.example.com/mcp"
};

// Permit read-only tool calls.
permit (principal, action == MCP::Action::"invokeTool", resource)
when {
  resource in MCP::Server::"example" &&
  resource.readOnly == true
};

// Permit resource reads.
permit (principal, action == MCP::Action::"readResource", resource)
when { resource in MCP::Server::"example" };

// Permit prompt retrieval.
permit (principal, action == MCP::Action::"getPrompt", resource)
when { resource in MCP::Server::"example" };
```


Matching both the name and identity URL establishes a canonical registration. It prevents a developer from registering another endpoint under the approved name or registering the approved endpoint under another name. Remove the resource or prompt permit if users don't need that capability.


## [Require confirmation with MCP elicitation](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#require-confirmation-with-mcp-elicitation)


Use `@requireApproval` to require per-request confirmation through MCP. When a request matches the annotated `permit`, the gateway sends an `elicitation/create` request to the same MCP client session that made the governed request. In a human-driven client, the person operating the agent sees the prompt and decides whether to proceed.


The following policy requires confirmation for non-read-only tools on a server registered as `example`. Use it alongside any permits needed to register the server or use its other capabilities. The annotation string becomes the reason shown in the elicitation:


```text
@requireApproval("non-read-only tool call")
permit (principal, action == MCP::Action::"invokeTool", resource)
when {
  resource in MCP::Server::"example" &&
  resource.readOnly == false
};
```


Tool annotations are supplied by the server and are advisory. `readOnly` defaults to `false` for tools that don't declare it, so this pattern requires confirmation for unannotated tools.


The gateway handles a matching request as follows:


```
flowchart TD
  request["Agent sends a governed MCP request"] --> evaluate["Gateway evaluates MCP policy"]
  evaluate -->|"Normal permit"| forward["Forward request"]
  evaluate -->|"No permit or matching forbid"| deny["Deny request"]
  evaluate -->|"Permit with @requireApproval"| elicit["Send MCP elicitation to connected client"]
  elicit --> confirm{"Client returns explicit confirmation?"}
  confirm -->|"No, unsupported, or error"| deny
  confirm -->|"Yes"| reevaluate["Re-evaluate with approval digest"]
  reevaluate -->|"Allowed"| forward
  reevaluate -->|"Denied or changed"| deny
```


The prompt identifies the server or gateway tool and includes the annotation reason. It doesn't include raw tool arguments. Each matching request requires a new confirmation. After confirmation, the gateway re-evaluates the request with a digest that binds the response to the evaluated authorization request.


Use this mechanism as a confirmation guardrail for human-driven clients. It doesn't create administrator approval or separation of duties. An autonomous MCP client can respond to an in-protocol elicitation programmatically. Use `forbid` for operations that must never run.


The request is denied if the originating client session can't handle MCP elicitation, the user declines, the elicitation fails, or re-evaluation doesn't allow the request. `sbx mcp add` can't present an elicitation, so a registration permit with `@requireApproval` results in a denial. Tool calls made from an execution context that can't relay an elicitation, including calls from inside `code-mode`, are also denied.


## [Withdraw server access](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#withdraw-server-access)


To withdraw access from a server that broader rules permit, block it at registration and at use time. Registration policy controls future `sbx mcp add` operations, while use-time policy controls requests from servers that are already registered or loaded.


Prevent future registrations of the server by matching its identity URL:


```text
forbid (principal, action == MCP::Action::"register", resource)
when { resource.identityURL == "https://mcp.example.com/mcp" };
```


Deny use-time requests for each registered name that refers to the server:


```text
forbid (principal, action == MCP::Action::"invokeTool", resource)
when { resource in MCP::Server::"example" };

forbid (principal, action == MCP::Action::"readResource", resource)
when { resource in MCP::Server::"example" };

forbid (principal, action == MCP::Action::"getPrompt", resource)
when { resource in MCP::Server::"example" };
```


The registration remains saved and can still be listed or loaded. These rules prevent another registration for the identity URL and deny governed use under the registered name. If the server was registered under other names, add use-time rules for those names as well.


An OAuth authorization helper is a built-in gateway tool, not a child of the registered server. To prevent agents from starting authorization for the server, govern the helper separately:


```text
forbid (principal, action == MCP::Action::"invokePrimordial", resource)
when { resource in MCP::Primordial::"example-authorize" };
```


## [Restrict host-run servers](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#restrict-host-run-servers)


Local stdio servers run on the host, outside the sandbox VM. This includes explicit host commands and OCI-packaged stdio servers started with host Docker. For details about this boundary, see [Docker Engine isolation](https://docs.docker.com/ai/sandboxes/security/isolation/#docker-engine-isolation).


In a blocklist policy that otherwise permits registration, deny the host-run server type:


```text
forbid (principal, action == MCP::Action::"register", resource)
when { resource.type == "local-stdio" };
```


`local-stdio` covers explicit commands, including commands that start a Docker container, and OCI-packaged stdio servers resolved from registry or manifest metadata with `--local`.


## [Related information](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp#related-information)


- [MCP policy concepts](https://docs.docker.com/ai/sandboxes/governance/concepts/#mcp-policies): policy model and rule evaluation.
- [MCP policy reference](https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/): exact action, resource, attribute, context, and approval behavior.
- [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/): policy creation and scope.
- [MCP policy audit logs](https://docs.docker.com/ai/sandboxes/governance/audit/): policy decision records.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Custom roles and permissions overview

`https://docs.docker.com/security/roles-and-permissions/custom-roles`

# Custom roles and permissions overview


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Subscription:
Business
For:
Administrators


Custom roles are permission sets that you choose to grant access to users or teams based on specific use cases. Use custom roles when you need specialized roles, department-specific access, or least-privilege grants.


If Docker's predefined permission sets meet your needs, use [core roles](https://docs.docker.com/security/roles-and-permissions/) instead.


*If Docker's predefined permission sets meet your needs, use
core roles
instead.*

## [Prerequisites](https://docs.docker.com/security/roles-and-permissions/custom-roles#prerequisites)


- A Docker Business subscription
- Owner permissions in your Docker organization


## [Creating custom roles](https://docs.docker.com/security/roles-and-permissions/custom-roles#creating-custom-roles)


To create a custom role, you select permissions from organization management, Docker Hub, billing, AI Governance, Docker Hardened Images, and Docker Offload. You then assign custom roles you created to individual users or to teams.


## [Next steps](https://docs.docker.com/security/roles-and-permissions/custom-roles#next-steps)

[### Manage custom roles Create, edit, assign, and delete custom roles for users and teams.](https://docs.docker.com/security/roles-and-permissions/custom-roles/manage/) [### Permissions reference Review every permission you can assign when building a custom role.](https://docs.docker.com/security/roles-and-permissions/custom-roles/permissions-reference/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Policy concepts

`https://docs.docker.com/ai/sandboxes/governance/concepts`

# Policy concepts


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The governance described here applies to local sandboxes. Cloud sandboxes use separate network policy configuration. See [Cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) for cloud controls.


## [Resource model](https://docs.docker.com/ai/sandboxes/governance/concepts#resource-model)


Docker sandbox governance is built around two resource types: **policies** and **rules**.


A **policy** is a named collection of rules that controls sandbox access. Policies exist at two levels:


- **Local**: configured per machine using the `sbx policy` CLI. Applies to sandboxes on that machine only.
- **Organization**: configured in Docker Home. Network and filesystem policies can also be managed via the [Governance API](https://docs.docker.com/reference/api/ai-governance/). Applies to sandboxes across the organization. An organization can have several policies, each applying either org-wide or to specific teams. See [Policy scope](https://docs.docker.com/ai/sandboxes/governance/concepts#policy-scope).


*A destination can include a port, and a path pattern looks like /api/**.*

When organization governance is active, only organization allow rules can grant access. Local and kit-defined deny rules still apply on top. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts#precedence).


A **rule** is the unit of access control within a policy. Each rule has:


- **Name**: a human-readable label
- **Actions**: the type of access the rule controls
- **Resources**: the targets the rule matches against
- **Decision**: `allow` or `deny`


Rules are grouped by domain. Network and filesystem rules in a policy must share the same domain, either `network` or `filesystem`. MCP policies use Cedar statements written in the `MCP` namespace instead of the network and filesystem rule format.


An organization network policy can also require approval, which turns every allow in that policy into a request the developer must confirm before access is granted. Approval is set on the policy rather than on individual rules, so it applies to all of the policy's allow rules at once. Without organization governance, a request with no matching allow or deny rule also asks for approval. See [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


Network approval is separate from the MCP `@requireApproval` annotation. An MCP approval confirms a single call within the session and creates no rule, while an approved network destination stays allowed until you remove the rule. See [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/).


### [Limits](https://docs.docker.com/ai/sandboxes/governance/concepts#limits)


Organization policies have the following limits, which help ensure fair usage and resource availability across organizations:


| Limit | Value |
| --- | --- |
| Policies per organization | 100 |
| Rules per policy | 250 |
| Policy size | 400 KB total, shared across all of a policy's rules |


Typical policies use only a small fraction of the policy size limit. Domain and file path values have no separate length limit beyond valid format.


If these limits don't fit your organization's needs, [contact Docker Sales](https://www.docker.com/products/ai-governance/#contact-sales) to discuss options.


## [Policy scope](https://docs.docker.com/ai/sandboxes/governance/concepts#policy-scope)


Each organization policy applies either across the whole organization or only to specific teams:


- Org-wide: with no teams assigned, the policy applies to every member of the organization.
- Team-scoped: with one or more teams assigned, the policy applies only to members of those teams.


*A destination can include a port, and a path pattern looks like /api/**.*

*For local and organization policy configuration, see
Network access policies.*

Teams are the same [teams](https://docs.docker.com/accounts/organization/manage/manage-a-team/) you manage for your organization; Docker matches a policy's teams against each user's team membership. Because an organization can mix org-wide and team-scoped policies, a single user is often subject to several at once. The policies that apply to a given user are their *effective policies*: every org-wide policy, plus every team-scoped policy for a team they belong to. See [Rule evaluation](https://docs.docker.com/ai/sandboxes/governance/concepts#rule-evaluation) for how a user's effective policies combine.


## [Rule syntax](https://docs.docker.com/ai/sandboxes/governance/concepts#rule-syntax)


### [Network rules](https://docs.docker.com/ai/sandboxes/governance/concepts#network-rules)


Network rules use `connect:tcp` for TCP and `connect:udp` for UDP. Resources are hostnames, CIDR ranges, or ports. UDP requires [experimental outbound UDP](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#allow-outbound-udp). ICMP is blocked.


**Hostname patterns**


| Pattern | Example | Matches |
| --- | --- | --- |
| Exact hostname | `example.com` | `example.com` on any port, not subdomains |
| Single-level wildcard | `*.example.com` | One subdomain level, any port: `api.example.com` |
| Multi-level wildcard | `**.example.com` | Any depth, any port: `api.example.com`, `v2.api.example.com` |
| Hostname with port | `example.com:443` | `example.com` on port 443 only |


`example.com` and `*.example.com` don't cover each other. Specify both if you need to match the root domain and its subdomains.


**CIDR ranges**


Both IPv4 and IPv6 notation are supported: `10.0.0.0/8`, `192.168.1.0/24`, `2001:db8::/32`.


#### [HTTP method and path](https://docs.docker.com/ai/sandboxes/governance/concepts#http-method-and-path)


A network rule matches a destination host on its own. An HTTP rule is a network rule that also names an HTTP method and URL path, so a policy can allow reads from an API without allowing writes to it.


An HTTP rule names one or more methods, a destination, and path patterns. What each part accepts depends on where you configure the rule:


| Part | Organization policy | Local policy |
| --- | --- | --- |
| Method | One or more listed methods | `ANY`, or one or more methods |
| Destination | A host or IP address | A host |
| Path | One or more absolute path patterns | One absolute path pattern |


A destination can include a port, and a path pattern looks like `/api/**`.


A local rule doesn't accept an IP address or a CIDR range. Use a plain network rule for those destinations. To cover a second path in a local policy, add a second rule.


Every rule applies to at least one method. On the CLI, `--method ANY` covers every HTTP method. In the composer, a rule with no methods selected covers every method the composer lists. For the methods you can select individually, see [Add a network rule](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/#add-a-network-rule) for an organization policy and [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#http-method-and-path-rules) for a local one.


Path patterns follow the same wildcard rules as filesystem paths, where `*` matches within one path segment and `**` matches any depth. A pattern without a wildcard matches that path exactly, so `/repos` matches `/repos` and nothing below it. Every pattern must start with `/` and can't contain a query string, a fragment, or a `..` segment. A local rule's path must also be canonical, so it can't contain percent-encoding, control characters, repeated or trailing slashes, or a `.` segment. For the full list, see [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#http-method-and-path-rules).


HTTP requests are evaluated against both layers. A network rule sets the baseline for a host, and HTTP rules adjust individual methods and paths within it:


| Rules that cover the host | Result for an HTTP request |
| --- | --- |
| Network allow only | Allowed at any method and path |
| HTTP allow only | Allowed only where a rule matches the method and path. Anything else is denied |
| Network allow and HTTP deny | The denied methods and paths are blocked. The rest stay allowed |
| Network deny | Blocked. An HTTP allow can't reopen a denied host |


A network deny is therefore a floor that HTTP rules can't raise, while a network allow is a ceiling that HTTP rules can carve into.


When a rule requires a method and path decision, the sandbox HTTP proxy evaluates each request separately instead of deciding once per connection.


Those requests have to go through the proxy. A connection it can't inspect, such as one it handles transparently, is blocked rather than evaluated. Traffic that isn't HTTP, such as SSH, carries no method or path, so HTTP rules never match it. Control those destinations with network rules.


For local and organization policy configuration, see [Network access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/).


### [Filesystem rules](https://docs.docker.com/ai/sandboxes/governance/concepts#filesystem-rules)


Filesystem rules use the actions `read` and `write`. Resources are host paths that sandboxes can mount as workspaces.


A workspace mounted with write access must be allowed by both a `read` and a `write` rule; a read-only workspace needs only `read`. When default deny blocks a mount, the denial reason names whether read or write access was missing.


`~` expands to the user's home directory on every platform, including Windows, where it resolves to `%USERPROFILE%`. A single `~/**` rule therefore matches each user's home tree on macOS, Linux, and Windows. The policy engine expands only `~`: it does not expand environment variables, so a pattern such as `%USERPROFILE%\**` or `$HOME/**` matches nothing.


For a path outside the home directory, write it in the format the user's operating system uses. A rule matches only the format it's written in, so a location that several platforms share needs a rule for each:


| Operating system | Example path |
| --- | --- |
| macOS, Linux | `/data/project/**` |
| Windows | `C:\data\project\**` |
| WSL | `\\wsl.localhost\<distro>\data\project\**` |


On Windows, `*:` matches any drive letter, so `*:\data\**` matches the path on any drive.


Wildcards behave the same way in every path format:


| Pattern | Example | Matches |
| --- | --- | --- |
| Exact path | `/data` | `/data` only |
| Segment wildcard | `/data/*` | `/data/project`, one path segment only, not subdirectories |
| Recursive wildcard | `/data/**` | `/data/project`, `/data/project/src`, any depth |


Use `**` to match a directory tree recursively. A single `*` matches within one path segment and won't cross a path separator. For example, `~/**` matches all paths under the home directory, while `~/*` matches only its direct children.


For organization policy configuration and enforcement details, see [Filesystem access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem/).


### [MCP policies](https://docs.docker.com/ai/sandboxes/governance/concepts#mcp-policies)


MCP policies control Model Context Protocol activity made available to a sandbox through Docker's [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/). They are organization policies written in Cedar using the `MCP` namespace, rather than the network and filesystem rule format.


MCP policy applies when a developer registers a server and when an agent uses the MCP gateway. Registration rules control future `sbx mcp add` operations. Use-time rules control tool calls, gateway meta-tools, resource reads, and prompt retrieval from servers that are already registered or loaded.


Governed MCP activity is default deny: a request is blocked unless a matching `permit` allows it. A matching `forbid` overrides any `permit`, including a permit that requires approval. Policy scope supplies the principal, so use organization or team scope instead of matching users, teams, tenants, or roles in Cedar.


For representative policies, see [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/). For exact action, resource, context, and approval behavior, see the [MCP policy reference](https://docs.docker.com/ai/sandboxes/governance/reference/mcp-policy/).


## [Rule evaluation](https://docs.docker.com/ai/sandboxes/governance/concepts#rule-evaluation)


When organization governance is active, the rules from all of a user's [effective policies](https://docs.docker.com/ai/sandboxes/governance/concepts#policy-scope) are combined and evaluated together against each request, following two principles:


- Deny wins: if any rule matches with `decision: deny`, the request is denied, regardless of any matching allow rules.
- Default deny: anything an allow rule doesn't match is blocked. Outbound network traffic is blocked unless a network rule allows the destination, and a host path can't be mounted unless a filesystem rule allows it. MCP activity is blocked unless an MCP `permit` allows it.


Because every effective policy feeds the same evaluation, allows are additive (a request is allowed if any effective policy allows it) and denies are absolute (a request is blocked if any effective policy denies it). A deny rule in an org-wide policy therefore applies to everyone and can't be overridden by a team-scoped policy, which makes org-wide deny rules useful as guardrails.


Local and kit-defined allow rules take no part in this evaluation. Deny rules from those sources do still apply. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts#precedence).


A request that an approval-required policy allows produces a third outcome. Rather than being allowed outright, it's held back until the developer confirms the destination, and the confirmation governs later requests to it. This holds even when another policy allows the same request without requiring approval. A matching deny still wins, so a denied destination is blocked without asking. See [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


## [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts#precedence)


What applies depends on whether your organization has governance enabled:


- No organization governance: local rules and any kit-defined network rules determine what sandboxes can access.
- Organization governance active: organization policy determines what access can be granted. Only organization allow rules grant access, so local and kit-defined allow rules are inactive and can't expand what the organization permits. Deny rules apply from every source, so a local or kit-defined deny can still restrict access further.


For kit-defined rules, see [Network policies](https://github.com/docker/sandbox-kit-spec/blob/main/docs/spec/capabilities/com.docker.sandbox/network-policy@1.md) in the kit specification.


Precedence is decided by a rule's decision rather than its source:


| Rule | Evaluated under organization governance |
| --- | --- |
| Organization allow | Yes |
| Organization deny | Yes |
| Local allow | No |
| Local deny | Yes |
| Kit-defined allow | No |
| Kit-defined deny | Yes |


Local and kit-defined rules cover network access only, so a deny that layers on top of organization policy is always a network deny. `sbx policy ls` hides inactive rules by default. See [Monitoring](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/#showing-inactive-rules) for how to list them.


A local deny takes precedence over an organization approval requirement as well, so the request is blocked and no approval is requested. Rules that a developer gains by approving a request are the one exception to local allow rules being inactive, because they record an answer to the organization's own approval requirement rather than granting new access. See [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


When organization governance is active, a user's organization policies are evaluated together, as described in [Rule evaluation](https://docs.docker.com/ai/sandboxes/governance/concepts#rule-evaluation).[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Network access policies

`https://docs.docker.com/ai/sandboxes/governance/access-controls/network`

# Network access policies


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


The governance described here applies to local sandboxes. Cloud sandboxes use separate network policy configuration. See [Cloud network policy](https://docs.docker.com/ai/sandboxes/cloud/network-policy/) for cloud controls.


Network access policies control outbound connections from sandboxes. Each policy contains one or more rules that allow the domains, IP ranges, and ports a workflow needs, or block destinations that should stay unavailable. Rules can also match the HTTP method and path of a request, so a policy can allow part of an API without allowing all of it.


You can configure network access in two places:


- [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/), which applies to sandboxes on one developer machine when organization governance is not active.
- [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/), which apply centrally across an organization or to selected teams.


When organization governance is active, only organization allow rules grant network access. Local allow rules are inactive until organization governance no longer applies, while local deny rules still apply on top of the organization policy. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence).


## [Rule syntax](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#rule-syntax)


Network rules use `connect:tcp` for TCP and `connect:udp` for UDP. Resources are hostnames, CIDR ranges, ports, or hostnames with ports. UDP requires [experimental outbound UDP](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#allow-outbound-udp). ICMP is blocked.


Examples:


- `api.example.com`
- `*.example.com`
- `**.example.com`
- `example.com:443`
- `10.0.0.0/8`


For exact wildcard behavior and CIDR support, see [Network rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#network-rules).


*For exact wildcard behavior and CIDR support, see
Network rules.*

## [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#http-method-and-path-rules)


A network rule matches a destination, so it allows or blocks everything a sandbox sends there. An HTTP rule narrows the match to specific HTTP methods and URL paths on that destination, which lets a policy allow reads from an API without allowing writes to it.


HTTP rules layer on top of network rules. A network allow is the baseline for a destination and HTTP rules carve into it, while a network deny blocks the destination outright and no HTTP allow can reopen it. For the pattern syntax and the full matching table, see [HTTP rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#http-method-and-path).


Configure them in either place:


- Organization policies, in the network rule composer in Docker Home. Set the rule **Type** to **HTTP**, then select the methods and path patterns. See [Add a network rule](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/#add-a-network-rule).
- Local policies, with `--method` and `--path` on `sbx policy`. See [HTTP method and path rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#http-method-and-path-rules).


## [Local network rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#local-network-rules)


Use `sbx policy allow network` and `sbx policy deny network` to manage local network rules:


```console
$ sbx policy allow network api.example.com
$ sbx policy deny network ads.example.com
```


For presets, sandbox-scoped rules, testing, and troubleshooting, see [Local policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/).


## [Organization network rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#organization-network-rules)


Organization network rules belong to policies that can apply to the whole organization or to selected teams. For setup steps and team scoping, see [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/).


Use [Monitoring policies](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring/) to inspect which network rules are active on a developer machine.


## [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#approval-required-access)


An organization network policy can require approval instead of granting access outright. Destinations the policy allows aren't reachable until the developer confirms them, which keeps an allowlist broad enough to be usable while still putting a person in front of each destination an agent reaches for.


Without organization governance, a request with no matching allow or deny rule also asks for approval rather than being denied outright, so access opens up as the developer approves each destination.


Under organization governance, approval is a property of the policy rather than of individual rules, so turning it on applies it to every allow rule in that policy. A destination stays directly reachable only when no policy that allows it requires approval. If a policy that requires approval also matches, the request needs approval regardless of what the other policies allow.


Only a destination the developer has already approved satisfies the requirement. Preset rules, [kit-defined rules](https://github.com/docker/sandbox-kit-spec/blob/main/docs/spec/capabilities/com.docker.sandbox/network-policy@1.md), and rules the developer added with `sbx policy allow network` don't answer it. An approval also can't reach a destination the organization doesn't allow at all, and it can't override a deny rule. To withdraw a destination, add a deny rule, which takes precedence over any approval already recorded.


To require approval on an organization policy, see [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/#require-approval-for-a-network-policy).


### [Respond to an approval request](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#respond-to-an-approval-request)


When a destination needs approval, a sandbox can't reach it until you confirm it. The request is blocked and the sandbox receives a message naming the destination:


```text
Approval required for api.example.com.

Review and respond with:
  sbx policy approval ls
```


If your organization [configures a support message](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/#configure-a-support-message), it appears after the approval instructions.


The request that triggers the prompt doesn't wait for an answer. It's denied, and approving the destination affects later requests. Agents that retry a failed request pick up the new access on their next attempt. For others, run the operation again.


List the destinations waiting for a response:


```console
$ sbx policy approval ls
APPROVAL                                              SANDBOX      TITLE                 DETAIL                                                                              OPTIONS
network:cWtN-4xUrNjxh4ouezcstgjrky6Rg57QfeRe3WEkyyY   my-sandbox   api.example.com:443   Protocol: TCP Resource type: domain approval required by policy "default network"   allow (Allow), dismiss (Dismiss)
```


Each entry names the destination, the sandbox that asked for it, and why it needs approval. Under organization governance that reason names the policy, as shown. Without it, the reason is that no matching allow rule covers the destination. A request that an HTTP rule matches also shows the method and path, such as `GET api.example.com:443/v1/data`.


To inspect a single entry, pass its ID to `sbx policy approval inspect`:


```console
$ sbx policy approval inspect network:cWtN-4xUrNjxh4ouezcstgjrky6Rg57QfeRe3WEkyyY
```


Respond by selecting one of the options the entry offers:


```console
$ sbx policy approval respond network:cWtN-4xUrNjxh4ouezcstgjrky6Rg57QfeRe3WEkyyY --option allow
```


Choosing `allow` grants access to that destination. Choosing `dismiss` leaves it blocked, and the destination is requested again the next time the sandbox tries to reach it. Repeated attempts collapse into a single entry, so a sandbox retrying in a loop leaves one request to answer, not a queue of duplicates.


#### [What approving grants](https://docs.docker.com/ai/sandboxes/governance/access-controls/network#what-approving-grants)


Approving records a rule that allows the destination the sandbox actually asked for, scoped to the sandbox that asked. Three things follow from that:


- The rule covers one destination, not the pattern the policy rule used. A policy that allows `*.example.com` with approval asks about `api.example.com` and `cdn.example.com` separately.
- A destination includes its port, so `api.example.com:443` and `api.example.com:8443` are approved separately.
- Another sandbox reaching the same destination asks again.


When an [HTTP rule](https://docs.docker.com/ai/sandboxes/governance/concepts/#http-method-and-path) in the policy matches the request, approving covers the method and exact path the sandbox requested rather than the whole destination. `GET /v1/data` and `POST /v1/data` on the same host are approved separately. A request whose method or path can't be recorded as a rule, such as a path with percent-encoding, is blocked without an entry to respond to.


Approved destinations stay allowed until the rule is removed. List them with `sbx policy ls --wide --created-via approval`, and remove one the same way as any other local rule, with [`sbx policy rm network`](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#managing-rules).


Approvals live in the local policy store, so [`sbx policy reset`](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/#resetting) removes all of them along with your other local rules. Each destination is requested again the next time a sandbox reaches it.


> Note
>
> To manage Model Context Protocol (MCP) server registration and requests through Docker's MCP gateway, use [MCP access policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/mcp/). These policies apply only to the gateway. Direct MCP connections from a sandbox don't use the gateway, but you can control access to remote MCP servers with network policy.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Manage credentials

`https://docs.docker.com/ai/sandboxes/configuration/credentials`

Back [Manuals](https://docs.docker.com/manuals/)


- [Get started](https://docs.docker.com/get-started/)
- [Guides](https://docs.docker.com/guides/)
- [Reference](https://docs.docker.com/reference/)


# Manage credentials


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


These credential stores and authentication flows apply to local sandboxes. Cloud credentials require separate setup: see [Authenticate cloud agents](https://docs.docker.com/ai/sandboxes/cloud/credentials/).


Most agents need an API key for their model provider. An HTTP/HTTPS proxy on your host intercepts outbound requests from the sandbox, looks up the matching credential on the host, and overwrites the auth header before forwarding. The real credential stays on the host when proxy management is active; the sandbox sees only a sentinel value. See [Trust boundaries](https://docs.docker.com/ai/sandboxes/security/#trust-boundaries) for how credential isolation fits into the broader sandbox security model.


## [How credential injection works](https://docs.docker.com/ai/sandboxes/configuration/credentials#how-credential-injection-works)


When a sandbox makes an outbound request, the host-side proxy decides three things: whether the request **matches** a service the kit (or built-in agent) declares, what **header** to write, and what **value** to inject. The kit declares the match and the header; you provide the value on the host. For proxy-managed credentials, the real value never enters the sandbox — the agent sees only a sentinel like `proxy-managed`.


A kit can set OAuth `passthrough: true` to opt out of sentinel masking. This sends the real token response into the sandbox and reduces credential isolation. See the [`oauth` kit fields](https://github.com/docker/sandbox-kit-spec/blob/main/docs/spec/capabilities/com.docker.sandbox/credential@1.md).


There are several ways to provide that value. When more than one source has a value for the same service, the stored secret takes precedence.


| Form | What it is | Use it when |
| --- | --- | --- |
| [Stored secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#stored-secrets) (`sbx secret set`) | A value or dynamic source in your OS keychain, keyed by service | The default for any built-in or kit-declared service |
*The store backing sbx secret set depends on your operating system:*

*Use --ref with a 1Password secret reference or an AWS Secrets Manager ARN:*

*The corresponding op or aws CLI must be installed and authenticated on the
host.*

*Use --command for another host tool that prints a secret to standard output:*

*To remove a sandbox-scoped secret, pass --sandbox:*

| [Custom secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#custom-secrets) (`sbx secret set-custom`) | A value keyed to a domain and environment variable | The service model doesn't fit — the agent validates the variable's format, or the secret rides in a request body |
| OAuth | A host-side sign-in flow; the token never enters the sandbox | The agent supports it, such as Claude Code, Codex, Cursor, or Droid |
| [Registry credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials#registry-credentials) (`sbx secret set --registry`) | Authentication for pulling images and kits | Pulling templates or kits from a private registry |


Providing a value and approving its use are separate steps. [Credential bindings](https://docs.docker.com/ai/sandboxes/configuration/credentials#credential-bindings) record which mechanisms and domains you authorize a kit to use. They don't store the credential value.


For multi-provider agents (OpenCode, Docker Agent), the proxy selects credentials based on the API endpoint being called. See individual [agent pages](https://docs.docker.com/ai/sandboxes/agents/) for provider-specific details.


## [Stored secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#stored-secrets)


`sbx secret set` stores credential values or dynamic secret sources in your OS keychain, keyed on a service identifier. Built-in agents declare a fixed set of services. Custom kits can declare their own. The same `sbx secret set` flow works for both.


Secrets whose names start with `mcp:` are reserved for the host's [MCP gateway](https://docs.docker.com/ai/sandboxes/mcp-gateway/). See [MCP secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#mcp-secrets) for how these differ from agent and provider credentials.


### [Where secrets are stored](https://docs.docker.com/ai/sandboxes/configuration/credentials#where-secrets-are-stored)


The store backing `sbx secret set` depends on your operating system:


- macOS: the system Keychain.
- Windows: the Windows Credential Manager.
- Linux: the Secret Service exposed by your desktop keyring, such as GNOME Keyring or KDE Wallet.


The Ubuntu package depends on GNOME Keyring, so a standard desktop install needs no extra setup.


On Linux hosts without a running Secret Service — headless servers and some WSL setups — `sbx` falls back to a file under your user config directory `$XDG_CONFIG_HOME/com.docker.sandboxes`, which defaults to `~/.config/com.docker.sandboxes` when `$XDG_CONFIG_HOME` is unset. The fallback is automatic and needs no configuration. When you store a secret this way, `sbx` prints a notice:


```text
No keychain detected - this secret will be stored on disk, protected by file permissions rather than a password
```


`sbx` stores the file in a directory with `0700` permissions, the same file-permission model used for `~/.docker/config.json`. Any user or process that can read the file can retrieve the stored credentials, so treat the directory as sensitive. Where available, prefer a keychain, which mediates access per application.


If you start a Secret Service on the host later, `sbx` stores new secrets in the keychain again. For more on running sandboxes without a desktop keyring, see [Can I use Docker Sandboxes on headless Linux?](https://docs.docker.com/ai/sandboxes/faq/#can-i-use-docker-sandboxes-on-headless-linux)


### [Store a secret](https://docs.docker.com/ai/sandboxes/configuration/credentials#store-a-secret)


```console
$ sbx secret set anthropic
```


This prompts you for the secret value interactively. Service secrets are global by default, so the secret is available to all sandboxes. To scope a secret to a specific sandbox instead:


```console
$ sbx secret set openai --sandbox my-sandbox
```


Adding, updating, or removing a service secret takes effect in existing local sandboxes without a restart, including secrets configured with `--command` or `--ref`. Sandbox-scoped secrets take precedence over global secrets.


### [MCP secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#mcp-secrets)


The MCP gateway uses the same host credential store for OAuth client secrets and custom request header secrets. These records have names starting with `mcp:` and appear in `sbx secret ls`. They stay on the host and aren't injected into sandboxes. The gateway uses them to authenticate connections to MCP servers on behalf of sandboxed agents.


For setup instructions, see [OAuth client secrets](https://docs.docker.com/ai/sandboxes/mcp-gateway/#use-a-pre-registered-oauth-client) and [custom request headers](https://docs.docker.com/ai/sandboxes/mcp-gateway/#custom-request-headers). Header secrets use the global scope and have their own [restart requirements](https://docs.docker.com/ai/sandboxes/mcp-gateway/#manage-header-secrets).


### [Use a dynamic secret source](https://docs.docker.com/ai/sandboxes/configuration/credentials#use-a-dynamic-secret-source)


Dynamic secret sources let `sbx` retrieve a credential from an authenticated host tool when the proxy needs it. The secret store contains the reference or command instead of the credential value. Resolution and caching happen on the host, and the sandbox still receives only the proxy-managed placeholder.


Use `--ref` with a 1Password secret reference or an AWS Secrets Manager ARN:


```console
$ sbx secret set anthropic --ref 'op://Work/Anthropic/credential'
$ sbx secret set openai \
    --ref 'arn:aws:secretsmanager:us-west-2:123456789012:secret:openai-api-key'
```


The corresponding `op` or `aws` CLI must be installed and authenticated on the host.


> Note
>
> To resolve a reference with a specific 1Password account or AWS profile, set `OP_ACCOUNT` or `AWS_PROFILE` when you run `sbx secret set`. `sbx` uses that account or profile whenever it resolves the secret. If neither variable is set, the provider CLI uses its default.


Use `--command` for another host tool that prints a secret to standard output:


```console
$ sbx secret set github --command 'gh auth token'
```


`sbx` runs the command through the host shell and trims its output. The command text is stored and replayed by the daemon. Don't embed a secret directly in the command because the text can appear in shell history and process listings.


Secret commands run from a fresh temporary directory on the host during verification and refresh. Relative paths such as `./credential-helper` resolve from that temporary directory. This applies to both `sbx secret set --command` and `sbx secret set-custom --command`.


Store helpers and any code or configuration they load outside writable sandbox mounts. Run a helper by name from an absolute directory on the host's `PATH`, use its absolute path, or explicitly change to its private directory in the command. Keep the host's temporary directory outside writable sandbox mounts as well.


By default, `sbx` verifies the source when you register it and reports an error without exposing the resolver's standard error. Use `--no-verify` to store a source that can't be resolved during registration. To troubleshoot an initial verification failure, use `--show-error`. Provider error output can contain sensitive information. You can't combine `--show-error` with `--no-verify`.


Resolved service secrets are cached for 55 minutes by default. To change the cache duration, use `--refresh <duration>`. To resolve the source for every credential use instead of caching it, pass `--refresh on-demand`:


```console
$ sbx secret set anthropic \
    --ref 'op://Work/Anthropic/credential' \
    --refresh 30m
$ sbx secret set github --command 'gh auth token' --refresh on-demand
```


`--ref` and `--command` are mutually exclusive. They can't be combined with `--token`, `--oauth`, or `--registry`.


### [Import from environment variables](https://docs.docker.com/ai/sandboxes/configuration/credentials#import-from-environment-variables)


If you already have API keys set in your shell, `sbx secret import` reads them and stores them in the keychain without typing each value manually:


```console
$ sbx secret import
```


This scans your current session for the environment variables in the [built-in services table](https://docs.docker.com/ai/sandboxes/configuration/credentials#built-in-services) below and prompts you to confirm each one before writing. To import a single service:


```console
$ sbx secret import openai
```


Pass `--all` to import everything without prompting (new entries only; existing entries are left unchanged), or `--force` to overwrite existing entries:


```console
$ sbx secret import --all
$ sbx secret import openai --force
```


Pass `--dry-run` to preview what would be imported without writing anything. Run `sbx secret ls` afterwards to confirm what's stored. For setting up credentials in CI, see [CI and headless use](https://docs.docker.com/ai/sandboxes/workflows/automation/).


### [Built-in services](https://docs.docker.com/ai/sandboxes/configuration/credentials#built-in-services)


Each built-in service name maps to the environment variables `sbx secret import` reads and the API domains the proxy injects credentials into:


| Service | Environment variables | API domains |
| --- | --- | --- |
| `anthropic` | `ANTHROPIC_API_KEY` | `api.anthropic.com`, `console.anthropic.com`, `claude.ai`, `mcp-proxy.anthropic.com` |
| `cursor` | `CURSOR_API_KEY` | `api2.cursor.sh`, `api3.cursor.sh`, `repo42.cursor.sh`, `cursor.com` |
| `droid` | `FACTORY_API_KEY` | `api.factory.ai`, `app.factory.ai`, `relay.factory.ai` |
| `github` | `GH_TOKEN`, `GITHUB_TOKEN` | `api.github.com`, `github.com`, `raw.githubusercontent.com`, `gist.github.com`, `copilot.github.com`, `api.githubcopilot.com` |
| `google` | `GEMINI_API_KEY`, `GOOGLE_API_KEY` | `generativelanguage.googleapis.com`, `oauth2.googleapis.com`, `aiplatform.googleapis.com`, `vertexai.googleapis.com` |
| `groq` | `GROQ_API_KEY` | `api.groq.com` |
| `mistral` | `MISTRAL_API_KEY` | `api.mistral.ai` |
| `nebius` | `NEBIUS_API_KEY` | `api.studio.nebius.com`, `api.tokenfactory.nebius.com` |
| `openai` | `OPENAI_API_KEY` | `api.openai.com`, `openai.com`, `chatgpt.com`, `www.chatgpt.com` |
| `openrouter` | `OPENROUTER_API_KEY` | `openrouter.ai` |
| `xai` | `XAI_API_KEY` | `api.x.ai` |


When you store a secret with `sbx secret set <service>`, the proxy injects it into requests to the listed API domains.


### [Services declared by kits](https://docs.docker.com/ai/sandboxes/configuration/credentials#services-declared-by-kits)


Use the service identifier from the kit's documentation when storing its credential. For a kit that declares `my-service`, run:


```console
$ sbx secret set my-service
```


There's no separate registration step. The stored value and the kit's request use the same identifier. Approve the kit's credential request when prompted. See [Credential bindings](https://docs.docker.com/ai/sandboxes/configuration/credentials#credential-bindings).


When authoring a kit, declare how it uses that service. V3 uses a credential capability, and v2 uses a top-level `credentials` list. Both examples declare the service and permit access to its API host:


v3


v2


```yaml
capabilities:
  - type: com.docker.sandbox/network-policy@1
    config:
      runtime:
        allow: [api.my-service.com]
  - type: com.docker.sandbox/credential@1
    config:
      service: my-service
      phase: runtime
      apiKey:
        name: MY_SERVICE_TOKEN
        proxyManaged: true
        inject:
          - domain: api.my-service.com
            header: Authorization
            format: "Bearer %s"
```


For API keys, specify both the HTTP header and its value format, as in this example. `sbx` doesn't use `apiKey.inject[].scheme` in v3 kits.


For OAuth, use JSON credential files and a provider that returns the refresh token in `refresh_token`. `sbx` doesn't support TOML credential files or a different refresh-token field.


Credentials declared for the install phase are available during install hooks. Add the domains that receive these credentials to the network policy's `install.allow` list. An entry in `runtime.allow` alone doesn't grant access during installation. If a hook reads a credential environment variable, include that name in its `env` list.


In `sbx`, the proxy stops injecting credentials into install-only domains before the agent launches. A domain remains available for credential injection if any runtime credential targets it, even under a different service name. If you declare the same service for both phases, `sbx` uses the runtime declaration's credential settings in both phases.


```yaml
credentials:
  - service: my-service
    apiKey:
      name: MY_SERVICE_TOKEN
      proxyManaged: true
      inject:
        - domain: api.my-service.com
          scheme: bearer

permissions:
  network:
    allow: [api.my-service.com]
```


Each service declares `apiKey`, `oauth`, or both. When both resolve at runtime, the API key takes precedence and OAuth acts as the fallback. For complete kit-side configuration, see [V3 credential definition](https://github.com/docker/sandbox-kit-spec/blob/main/docs/spec/capabilities/com.docker.sandbox/credential@1.md) or [V2 credentials](https://docs.docker.com/ai/sandboxes/customize/kits-v2/#credentials).


### [List and remove secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#list-and-remove-secrets)


List all stored secrets:


```console
$ sbx secret ls
SCOPE      SERVICE   SECRET
(global)   github    gho_GCaw4o****...****43qy
```


Remove a secret:


```console
$ sbx secret rm github
```


To remove a sandbox-scoped secret, pass `--sandbox`:


```console
$ sbx secret rm github --sandbox my-sandbox
```


Removing a sandbox-scoped secret restores the global secret for that service, if one is available.


> Note
>
> Running `sbx reset` deletes all stored secrets along with all sandbox state. You'll need to re-add your secrets after a reset.


### [GitHub token](https://docs.docker.com/ai/sandboxes/configuration/credentials#github-token)


The `github` service gives the agent access to the `gh` CLI inside the sandbox. Resolve your existing GitHub CLI token on the host:


```console
$ sbx secret set github --command 'gh auth token'
```


The daemon refreshes the token from the host command after the default cache period. This is useful for agents that create pull requests, open issues, or interact with GitHub APIs on your behalf.


### [SSH agent](https://docs.docker.com/ai/sandboxes/configuration/credentials#ssh-agent)


SSH agent forwarding is enabled by default. V3 kits must also request [`ssh-agent@1`](https://docs.docker.com/ai/sandboxes/customize/author/capabilities/#support-by-capability) for the phase where they need it. Without that request, no agent socket is forwarded to a v3 sandbox.


When `SSH_AUTH_SOCK` is set, Docker Sandboxes uses the value from the client that creates, starts, or joins each sandbox. It forwards that agent into the sandbox and sets `SSH_AUTH_SOCK` there.


If your agent exposes a stable socket path, such as the 1Password SSH agent, configure that path for every sandbox:


```console
$ sbx settings set ssh.agentSocketPath "$SSH_AUTH_SOCK"
```


An empty [`ssh.agentSocketPath`](https://docs.docker.com/ai/sandboxes/configuration/settings/#sshagentsocketpath), which is the default, uses the agent supplied by each client instead. Use [`ssh.agentForwardingEnabled`](https://docs.docker.com/ai/sandboxes/configuration/settings/#sshagentforwardingenabled) to turn forwarding on or off.


After changing forwarding or the socket selection, restart the daemon so existing sandboxes use the new configuration:


```console
$ sbx daemon restart
```


The private keys stay on your host. Processes inside the sandbox can request signatures from the forwarded agent, but they can't read or copy a private key.


Use SSH agent forwarding for Git operations over SSH and SSH-based commit signing. The signing key must be loaded in the host SSH agent for sandboxed commit signing to work. Outbound SSH connections are still subject to sandbox network policy. For details, see [Commit signing](https://docs.docker.com/ai/sandboxes/workflows/git/#commit-signing).


## [Custom secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#custom-secrets)


> Important
>
> Custom secrets are experimental. Behavior, flags, and the placeholder format may change without notice.


For credentials that don't fit the service-identifier model — for example, when an agent validates the environment variable format at boot, or when the credential lands in a request body rather than a header — use `sbx secret set-custom`. The secret is keyed on one or more target domains, an environment variable name, and an optional placeholder string, instead of a service identifier.


Prefer the [service-based flow](https://docs.docker.com/ai/sandboxes/configuration/credentials#stored-secrets) whenever it's an option — the kit handles the wiring; you only provide the value.


### [Set a custom secret](https://docs.docker.com/ai/sandboxes/configuration/credentials#set-a-custom-secret)


Custom secrets are global by default. Pass `--sandbox` to scope one to a specific sandbox.


```console
$ sbx secret set-custom \
    --host api.example.com \
    --env API_KEY \
    --value <secret>
```


> Warning
>
> Passing the secret as `--value <secret>` records it in your shell history and exposes it to other processes running as your user. Avoid pasting real credentials inline — read the value from a variable that's already in your environment, and clear shell history if a real secret was passed on the command line.


Inside the sandbox, `API_KEY` is set to a generated placeholder (for example, `sbx-cs-<rand>`). When a sandboxed process sends a request to any of the configured hosts and the placeholder appears anywhere in the request, the proxy replaces it with the real value. The agent never sees the real secret.


### [Target multiple hosts](https://docs.docker.com/ai/sandboxes/configuration/credentials#target-multiple-hosts)


Repeat `--host` to cover multiple domains with the same secret — useful when an API is split across related hostnames or when two unrelated endpoints share a credential:


```console
$ sbx secret set-custom \
    --host api.example.com \
    --host uploads.example.com \
    --env API_KEY \
    --value <secret>
```


A `--host` value can also use wildcards, with the same syntax as [network rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#network-rules): `*` matches a single label (`*.example.com` covers `api.example.com`) and `**` matches any number (`**.example.com` covers `api.example.com` and `v2.api.example.com`).


### [Resolve custom secrets dynamically](https://docs.docker.com/ai/sandboxes/configuration/credentials#resolve-custom-secrets-dynamically)


Custom secrets also accept [dynamic secret sources](https://docs.docker.com/ai/sandboxes/configuration/credentials#use-a-dynamic-secret-source). Replace `--value` with either `--ref` or `--command`:


```console
$ sbx secret set-custom \
    --host api.example.com \
    --env API_KEY \
    --ref 'op://Work/Example/credential'
```


Dynamic custom secrets resolve on demand by default. Pass `--refresh` with a duration to cache the resolved value. The verification and error-output flags work the same as they do for service secrets. `--ref` and `--command` can't be combined with `--value` or `--token`.


### [Install npm packages from GitHub Packages](https://docs.docker.com/ai/sandboxes/configuration/credentials#install-npm-packages-from-github-packages)


The built-in `github` service doesn't inject credentials into requests to `npm.pkg.github.com`. To install private npm packages from GitHub Packages, add a custom secret for that host.


On the host, authenticate the GitHub CLI with a token that can read the package. GitHub documents a personal access token (classic) with at least `read:packages` scope for this use. See [Authenticating to GitHub Packages](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-npm-registry#authenticating-to-github-packages). Then register the token source, replacing `my-sandbox` with your sandbox's name:


```console
$ sbx secret set-custom \
    --sandbox my-sandbox \
    --host npm.pkg.github.com \
    --env NODE_AUTH_TOKEN \
    --command 'gh auth token'
```


The command prints a generated placeholder. For an existing sandbox, set `NODE_AUTH_TOKEN` to that placeholder using `sbx run -e` for an agent session, or `/etc/sandbox-persistent.sh` for future sessions. See [Set environment variables](https://docs.docker.com/ai/sandboxes/usage/#set-environment-variables). Use the placeholder, not the actual GitHub token.


Inside the sandbox, add the following entries to your project's `.npmrc`, replacing `@my-org` with the package's scope. Keep `${NODE_AUTH_TOKEN}` literal so npm reads the environment variable:


```ini
@my-org:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NODE_AUTH_TOKEN}
```


Install the package inside the sandbox:


```console
$ npm install @my-org/my-package
```


Replace `@my-org/my-package` with your package name. npm sends the placeholder to `npm.pkg.github.com`, and the proxy replaces it with the token retrieved by `gh auth token` on the host.


## [Credential bindings](https://docs.docker.com/ai/sandboxes/configuration/credentials#credential-bindings)


A credential bindings file records which credential mechanisms and domains you've approved for each service. It lives at `~/.config/sbx/credentials.yaml`, or `%APPDATA%\sbx\credentials.yaml` on Windows.


Third-party kits require an approved binding for each credential they use, regardless of schema version. `sbx` creates one interactively the first time you run such a kit (see [First-run approval](https://docs.docker.com/ai/sandboxes/configuration/credentials#first-run-approval)); you can also write entries by hand. Credentials requested only by the built-in kits shipped with `sbx` don't need a binding.


Each entry under `bindings` is keyed by a [service identifier](https://docs.docker.com/ai/sandboxes/configuration/credentials#built-in-services) and approves one or both credential mechanisms:


- `apiKey` — approves injecting the service's stored API key. The value comes from the [secret store](https://docs.docker.com/ai/sandboxes/configuration/credentials#stored-secrets) (`sbx secret set <service>`); the binding records approval, it doesn't hold or locate the value.
- `oauth` — approves the OAuth flow for the service. You sign in on the host, and the proxy handles token refresh and routing. OAuth domains include the token endpoint host and any resource hosts declared by the kit.


Each mechanism takes a `domains` list that records the domains you approved. `sbx` asks for approval when a kit requests domains that the existing binding doesn't cover.


```yaml
bindings:
  anthropic:
    apiKey:
      domains: [api.anthropic.com]
  github:
    apiKey:
      domains: [api.github.com, github.com]
```


A binding is only an approval record: the presence of `apiKey` or `oauth` authorizes that mechanism. Declining a credential writes no entry at all. The real credential isn't stored in this file.


### [First-run approval](https://docs.docker.com/ai/sandboxes/configuration/credentials#first-run-approval)


When a third-party kit needs a credential that has no binding, `sbx` walks you through approving one. For an API key, you can use a value already in the secret store or enter one at the prompt. For OAuth, you approve the sign-in flow. In both cases, you approve the domains declared by the kit. `sbx` writes the entry to `credentials.yaml`.


In non-interactive contexts (CI or `--detach`), there's no one to answer the prompt. In `sbx`, the sandbox starts with the credential withheld when no binding exists. For a required credential, `sbx` prints a warning rather than failing sandbox creation. This is a limitation of `sbx` enforcement: kit authors shouldn't rely on a required credential being available merely because the sandbox started.


Pre-create the binding by running the kit interactively once or by writing `credentials.yaml` directly before running unattended.


The bindings file gates whether a third-party kit can use a service credential. The kit's credential injection rules and network permissions still constrain which requests can carry the credential.


### [Kits that require a binding](https://docs.docker.com/ai/sandboxes/configuration/credentials#kits-that-require-a-binding)


Third-party kits require your approval to use credentials, regardless of schema version. The built-in kits shipped with `sbx` can use credentials they request without a binding. If a third-party v2 kit extends a built-in agent, you must approve its use of the inherited credentials. You must also approve a third-party kit that requests the same service itself.


## [Registry credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials#registry-credentials)


Registry credentials authenticate to private OCI registries when pulling [templates](https://docs.docker.com/ai/sandboxes/usage/#load-a-template) or [kits](https://docs.docker.com/ai/sandboxes/customize/), and can also let the agent pull and push images from inside the sandbox through the host-side proxy. Use `sbx secret set --registry <host>` to store them. For Docker Hub, `sbx` reuses your `sbx login` session — no registry secret needed. For other registries (GitHub Container Registry, ECR, ACR, self-hosted Nexus, and so on), store credentials with `sbx secret set --registry`.


Choose the scope by adding `--all-sandboxes`, adding `--sandbox SANDBOX`, or passing neither:


```text
sbx secret set [--all-sandboxes | --sandbox SANDBOX] --registry HOST
```


- **Host-only** (no scope flag): the `sbx` CLI uses it to pull templates and kits when creating a sandbox. The credential stays on the host and is never available inside the sandbox.
- **All sandboxes** (`--all-sandboxes`): same as host-only, plus the proxy authenticates registry login requests from sandboxes. The credential stays on the host and is never written to the sandbox filesystem. Use it when agents build and publish container images.
- **Sandbox-scoped** (`--sandbox SANDBOX`): same proxy behavior as `--all-sandboxes`, but only for the named sandbox. Use it when only one sandbox needs registry access.


### [Store registry credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials#store-registry-credentials)


Pipe a token from stdin and target the registry hostname:


```console
$ gh auth token | sbx secret set --registry ghcr.io --password-stdin
```


For registries that require a username (for example, ACR with an admin account), add `--username`:


```console
$ echo "$ACR_PASSWORD" | sbx secret set \
    --registry myregistry.azurecr.io \
    --username myuser \
    --password-stdin
```


Add `--all-sandboxes` to make the credential available to every new sandbox:


```console
$ gh auth token | sbx secret set --all-sandboxes --registry ghcr.io --password-stdin
$ sbx run claude
```


Store all-sandboxes registry credentials before creating a sandbox. Existing sandboxes don't pick up all-sandboxes registry credentials added later. To add registry access to an existing sandbox, use a sandbox-scoped credential instead.


To scope the credential to a single sandbox, store it under that sandbox's name:


```console
$ gh auth token | sbx secret set --sandbox my-app --registry ghcr.io --password-stdin
```


For v2 kits on Docker Hub, `sbx kit pull` and `sbx kit push` use the session from `sbx login`. For other registries, both commands use these credentials. Both commands fall back to the Docker credential store, so credentials from `docker login` also work. V3 kits are [published with Docker Buildx](https://docs.docker.com/ai/sandboxes/customize/author/distribute/#publish-an-image), which uses the credentials from `docker login`.


### [Trust a private registry authentication endpoint](https://docs.docker.com/ai/sandboxes/configuration/credentials#trust-a-private-registry-authentication-endpoint)


Use `--registry-auth-endpoint` with `--registry` when a self-hosted registry authenticates sandbox requests through a separate host. For example, a self-hosted GitLab registry at `registry.example.com` might advertise `https://gitlab.example.com/jwt/auth` as the `realm` in its Registry v2 `WWW-Authenticate: Bearer` challenge.


Store the credential and trust that endpoint for a specific sandbox:


```console
$ echo "$GITLAB_PAT" | sbx secret set --sandbox my-app \
    --registry registry.example.com \
    --username "$GITLAB_USER" \
    --registry-auth-endpoint https://gitlab.example.com/jwt/auth \
    --password-stdin
```


Replace the example hosts with your registry and authentication hosts, and set `GITLAB_USER` and `GITLAB_PAT` to your GitLab username and personal access token.


This authorizes the proxy to send the stored registry credential to `https://gitlab.example.com/jwt/auth` to exchange it for a registry token. The advertised realm must use HTTPS and match the configured host and path exactly. Other paths on that host, including `/jwt/auth/`, aren't covered. The endpoint URL must contain no embedded credentials, query string, or fragment. Token requests can still include protocol parameters such as `service` and `scope`.


Without this flag, the proxy accepts authentication endpoints on the registry's own host and built-in registry relationships, such as Docker Hub's authentication host. Other authentication hosts require explicit configuration.


### [Remove registry credentials](https://docs.docker.com/ai/sandboxes/configuration/credentials#remove-registry-credentials)


Remove both the host-only and all-sandboxes entries for a registry:


```console
$ sbx secret rm --registry ghcr.io -f
```


To remove only the all-sandboxes entry and leave the host-only credential in place, pass `--all-sandboxes`:


```console
$ sbx secret rm --all-sandboxes --registry ghcr.io -f
```


To remove a sandbox-scoped credential, pass the sandbox name:


```console
$ sbx secret rm --sandbox my-sandbox --registry ghcr.io -f
```


*Add --all-sandboxes to make the credential available to every new sandbox:*

## [Best practices](https://docs.docker.com/ai/sandboxes/configuration/credentials#best-practices)


- Use [stored secrets](https://docs.docker.com/ai/sandboxes/configuration/credentials#stored-secrets) to provide credentials. The OS keychain protects them at rest; on Linux hosts without a keychain they are held in a permission-protected file instead. See [Where secrets are stored](https://docs.docker.com/ai/sandboxes/configuration/credentials#where-secrets-are-stored).
- Don't set API keys manually inside the sandbox. Sandbox agents are pre-configured to use proxy-managed credentials.
- Registry credentials stay on the host and are injected by the proxy when a sandbox authenticates to the registry. Reserve them for sandboxes that need registry access, and prefer sandbox scope over `--all-sandboxes` to limit exposure.
- Several agents support OAuth as another secure option: the flow runs on the host, so the token is never exposed inside the sandbox. If you haven't stored a credential, the agent prompts you to authenticate — Codex prompts on the host from `sbx run codex`, while Claude Code, Cursor, and Droid prompt interactively inside the sandbox. To authenticate ahead of time, run `sbx secret set openai --oauth` for Codex or use `/login` inside Claude Code; Cursor and Droid have no ahead-of-time option, so their sign-in prompt appears when the agent starts. See the individual [agent pages](https://docs.docker.com/ai/sandboxes/agents/) for each agent's flow.
- If you store credentials in 1Password or AWS Secrets Manager, see [Sourcing credentials from 1Password](https://docs.docker.com/ai/sandboxes/workflows/authentication/#source-credentials-from-1password) and [Sourcing credentials from AWS Secrets Manager](https://docs.docker.com/ai/sandboxes/workflows/authentication/#source-credentials-from-aws-secrets-manager).


## [Custom templates and placeholder values](https://docs.docker.com/ai/sandboxes/configuration/credentials#custom-templates-and-placeholder-values)


When building custom templates or installing agents manually in a shell sandbox, some agents require environment variables like `OPENAI_API_KEY` to be set before they start. Set these to placeholder values (e.g. `proxy-managed`) if needed. The proxy injects actual credentials regardless of the environment variable value.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Filesystem access policies

`https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem`

# Filesystem access policies


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


Filesystem access policies control which host paths a sandbox can mount as a workspace. Each policy contains one or more rules that restrict sandbox workspaces to approved directories.


Filesystem access is managed with [organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/). When organization governance is active, organization rules determine which paths a sandbox can mount, and the local filesystem allow rules from the default preset become inactive. `sbx policy deny` applies to network access only, so there are no local filesystem deny rules to layer on top. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence).


## [Rule syntax](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem#rule-syntax)


Filesystem rules use the actions `read` and `write`. Resources are host path patterns.


A writable workspace mount must be allowed by both a `read` rule and a `write` rule. A read-only workspace needs only `read`.


Examples:


- `~/**`
- `/data/project/**`
- `C:\data\project\**`
- `\\wsl.localhost\<distro>\data\project\**`


Use `**` to match a directory tree recursively. A single `*` matches only one path segment. For exact path matching behavior across macOS, Linux, Windows, and WSL, see [Filesystem rules](https://docs.docker.com/ai/sandboxes/governance/concepts/#filesystem-rules).


## [Organization filesystem rules](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem#organization-filesystem-rules)


Organization filesystem rules belong to policies that can apply to the whole organization or to selected teams. For setup steps and team scoping, see [Organization policies](https://docs.docker.com/ai/sandboxes/governance/access-controls/organization/).


Filesystem policy is checked when a workspace is mounted, which happens when a sandbox is created. To apply a filesystem policy change to a running workflow, remove the sandbox and create a new one.


## [Troubleshooting](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem#troubleshooting)


### [Sandbox cannot mount workspace](https://docs.docker.com/ai/sandboxes/governance/access-controls/filesystem#sandbox-cannot-mount-workspace)


If a sandbox fails to mount with a `mount policy denied` error, verify that the filesystem allow rule uses `**` rather than `*`. A single `*` doesn't match across directory separators.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Monitoring policies

`https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring`

# Monitoring policies


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---


`sbx policy ls` and `sbx policy log` give you a combined view of all active policy rules and sandbox network activity, regardless of whether those rules come from local configuration or organization governance. They're useful both for verifying rules you've written and for debugging why a request is being blocked or allowed.


## [Listing rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#listing-rules)


Use `sbx policy ls` to see all active policies and their current status:


```console
$ sbx policy ls
POLICY                                 SOURCE   APPLIES TO          SUMMARY
local-policy                           local    all                 network: 42 allow, 1 deny; filesystem read: 1 allow; filesystem write: 1 allow
1b2633ea-e604-48bb-a5e6-3ac86ba383fe   kit      sandbox:my-sandbox  network: 3 allow
```


The columns are:


- `POLICY`: the policy name.
- `SOURCE`: where the policy came from. `local` means your local configuration — a preset or rules you added with `sbx policy`. `kit` means a [kit](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence). `org` means your organization.
- `APPLIES TO`: which sandboxes the policy applies to. `all` means the policy is global. `sandbox:<name>` scopes it to a single sandbox; a profile name scopes it to sandboxes using that profile.
- `SUMMARY`: a count of rule entries by type and decision, for example `network: 5 allow, 1 deny`. A rule that names several destinations contributes one entry per destination. When the listing includes rules that match an HTTP method and path, the network count labels each part `(L4)` or `(L7)`. See [HTTP rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#http-rules).


To see full rule-level detail including rule IDs and resources, pass `--wide`. To inspect a single policy or rule, use `sbx policy inspect`:


```console
$ sbx policy inspect Balanced
```


Use `--source` to filter by origin (`local`, `org`, or `kit`) and `--decision` to filter by outcome (`allow` or `deny`).


Use `--protocol tcp` or `--protocol udp` to filter network rules.


Use `--created-via` to filter by how a rule was created. Pass `default` for preset rules, `added` for rules you added yourself, `provisioned` for rules a kit or application added, or `approval` for rules recorded when you approved a destination. A wide listing shows the same information per rule:


```console
$ sbx policy ls --wide --created-via approval
```


See [Approval-required access](https://docs.docker.com/ai/sandboxes/governance/access-controls/network/#approval-required-access).


A `STATUS` column also appears when you pass `--include-inactive`; see [Showing inactive rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#showing-inactive-rules).


When organization governance is active, the output starts with a summary block showing which organization manages the policy, the sync state, and how many inactive rules are hidden:


```console
$ sbx policy ls
POLICY RULES
  Governance: Managed by my-org
  Sync:       OK, last synced 08:21:01
  Hidden:     9 inactive rules. Show with: sbx policy ls --include-inactive

POLICY               SOURCE   APPLIES TO   SUMMARY
default filesystem   org      all          filesystem read: 2 allow; filesystem write: 7 allow, 2 deny
default network      org      all          network: 38 allow, 4 deny
```


`Governance` shows which organization manages the policy, and `Sync` confirms the daemon has pulled the latest rules. If the sync state shows an error or a stale timestamp, the daemon may not have the most recent org policy. Run `sbx policy reset` to force a fresh pull. `Hidden` reports how many inactive rules are suppressed and how to reveal them.


If Docker can't determine which organization governs your account, policy output shows `Governance: Unresolved`, and the dashboard shows the same unresolved state. For example, this happens when your account belongs to multiple organizations with governance enabled. Policy enforcement fails closed until the conflict is resolved, so local allow rules can't grant access. Contact an administrator for the affected organizations to resolve the conflicting governance configuration.


### [Showing inactive rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#showing-inactive-rules)


When organization governance is active, local and kit-defined allow rules are not evaluated, so `sbx policy ls` hides them by default. To list them too — for example, to confirm which allow rules the organization policy overrides — pass `--include-inactive`. This adds a `STATUS` column:


```console
$ sbx policy ls --include-inactive
POLICY RULES
  Governance: Managed by my-org
  Sync:       OK, last synced 08:41:06

POLICY                       SOURCE   APPLIES TO   SUMMARY                                                    STATUS
default filesystem           org      all          filesystem read: 2 allow; filesystem write: 7 allow, 2 deny   active
default network              org      all          network: 38 allow, 4 deny                                   active
default-fs-read-allow-all    local    all          filesystem read: 1 allow                                    inactive
default-fs-write-allow-all   local    all          filesystem write: 1 allow                                   inactive
```


Inactive policies show `inactive` in the `STATUS` column. They have no effect while organization governance is active. Local and kit-defined deny rules stay active and aren't hidden, because a deny still applies on top of the organization policy. See [Precedence](https://docs.docker.com/ai/sandboxes/governance/concepts/#precedence).


Use `--type network`, `--type filesystem`, or `--type http` to show only policies of that type. Without a sandbox argument, `sbx policy ls` shows every policy across all sandboxes. Pass a sandbox name to filter to global policies and those scoped to that sandbox:


```console
$ sbx policy ls my-sandbox
```


### [Filesystem rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#filesystem-rules)


`sbx policy ls` lists filesystem policies alongside network policies. Filesystem rules control which host paths a sandbox can mount as a workspace. Pass `--type filesystem` to show only them:


```console
$ sbx policy ls --type filesystem
POLICY         SOURCE   APPLIES TO   SUMMARY
local-policy   local    all          filesystem read: 1 allow; filesystem write: 1 allow
```


A writable workspace mount must be allowed by both a `filesystem:read` and a `filesystem:write` rule; a read-only mount needs only `filesystem:read`. The default local policy allows read and write access to all paths, shown as the two `default-fs-*` rules above. For the rule syntax and path patterns, see [Policy concepts](https://docs.docker.com/ai/sandboxes/governance/concepts/#filesystem-rules).


### [HTTP rules](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#http-rules)


Rules that match an HTTP method and path are listed as type `http`. Pass `--wide` to see the `METHOD` and `PATH` columns alongside network rules:


```console
$ sbx policy ls --wide
TYPE      METHOD   PATH
network   -        -
http      GET      /repos/org/project/**
http      POST     /admin/**
```


Rules that match a whole destination show `-` in both columns. To list only HTTP rules, pass `--type http`.


HTTP rules are counted as network rules in the `SUMMARY` column, with each part labeled by the network layer it matches on. `L4` counts entries that match a whole destination, and `L7` counts those that also match an HTTP method and path:


```console
$ sbx policy ls
POLICY         SOURCE   APPLIES TO   SUMMARY
local-policy   local    all          network: 2 allow (L4), 1 deny (L7)
```


When the same decision has entries at both layers, each layer gets its own count, L4 first. Two host allows and one HTTP allow read `network: 2 allow (L4), 1 allow (L7)`.


The labels appear when the current listing includes at least one HTTP rule. Because filters and hidden inactive rules change what the listing contains, a filtered listing with no HTTP rules shows an unlabeled count, such as `network: 42 allow`.


For the rule syntax, see [HTTP method and path](https://docs.docker.com/ai/sandboxes/governance/concepts/#http-method-and-path).


*Use sbx policy ls to see all active policies and their current status:*

*Use --protocol tcp or --protocol udp to filter network rules.*

*See Approval-required access.*

*For the rule syntax, see
HTTP method and path.*

## [Monitoring traffic](https://docs.docker.com/ai/sandboxes/governance/monitor-and-enforce/monitoring#monitoring-traffic)


Use `sbx policy log` to see which hosts your sandboxes have contacted and which rules matched:


```console
$ sbx policy log
BLOCKED REQUESTS
SANDBOX      TYPE     HOST                   PROXY        RULE            REASON         LAST SEEN        COUNT
my-sandbox   network  blocked.example.com    transparent  domain-blocked  default-deny   10:15:25 29-Jan  1

ALLOWED REQUESTS
SANDBOX      TYPE     HOST                   PROXY          RULE             REASON   LAST SEEN        COUNT
my-sandbox   network  api.anthropic.com      forward        domain-allowed            10:15:23 29-Jan  42
my-sandbox   network  registry.npmjs.org     forward-bypass domain-allowed            10:15:20 29-Jan  18
my-sandbox   network  app.example.com        browser-open                             10:15:10 29-Jan  1
```


The `PROXY` column shows how the request left the sandbox:


| Value | Description |
| --- | --- |
| `forward` | Routed through the forward proxy. Supports [credential injection](https://docs.docker.com/ai/sandboxes/configuration/credentials/). |
| `forward-bypass` | Routed through the forward proxy without credential injection. |
| `transparent` | Intercepted by the transparent proxy. Policy is enforced but credential injection is not available. |
| `network` | Non-HTTP traffic. TCP and experimental UDP egress follow network policy. ICMP is blocked. |
| `browser-open` | A sandbox process requested opening a URL in the host browser. Policy is enforced before opening the URL. |


The `RULE` column identifies the policy rule that matched the request. The `REASON` column includes extra context when the daemon records one.


Filter by sandbox name by passing it as an argument:


```console
$ sbx policy log my-sandbox
```


Use `--limit N` to show only the last `N` entries, `--json` or `--format yaml` for machine-readable output, or `--type network` to filter by policy type. `sbx policy log` records network traffic only; filesystem mount decisions aren't available in the log yet.


Structured output uses the same document for local and cloud sandboxes: `{updated_at, allowed: [...], blocked: [...]}`. Each entry includes `sandbox_id`, `host`, `proxy_type`, `rule`, `reason`, `count`, `first_seen`, and `last_seen`. The `--limit` flag applies to structured output too.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Create and manage a team

`https://docs.docker.com/accounts/organization/manage/manage-a-team`

# Create and manage a team


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Subscription:
Team

Business
For:
Administrators


You can create teams for your organization in Docker Home or Docker Hub, and configure team repository access in Docker Hub.


A team is a group of Docker users that belong to an organization. An organization can have multiple teams. An organization owner can create new teams and add members to an existing team using their Docker ID or email address. Members aren't required to be part of a team to be associated with an organization.


The organization owner can add additional organization owners to help them manage users, teams, and repositories in the organization by assigning them the owner role.


## [What is an organization owner?](https://docs.docker.com/accounts/organization/manage/manage-a-team#what-is-an-organization-owner)


An organization owner is an administrator who has the following permissions:


- Manage repositories and add team members to the organization
- Access private repositories, all teams, billing information, and organization settings
- Specify [permissions](https://docs.docker.com/accounts/organization/manage/manage-a-team#permissions-reference) for each team in the organization
- Enable [SSO](https://docs.docker.com/security/authentication/single-sign-on/) for the organization


When SSO is enabled for your organization, the organization owner can also manage users. Docker can auto-provision Docker IDs for new end-users or users who'd like to have a separate Docker ID for company use through SSO enforcement.


Organization owners can add others with the owner role to help them manage users, teams, and repositories in the organization.


For more information on roles, see [Roles and permissions](https://docs.docker.com/security/roles-and-permissions/).


*For more information on roles, see
Roles and permissions.*

## [Create a team](https://docs.docker.com/accounts/organization/manage/manage-a-team#create-a-team)


1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. Select **Teams**.
3. Select **Create team**.
4. Provide the team's information, then select **Create**.


Docker opens the team view, where you can add members and assign licenses.


## [Assign licenses to a team](https://docs.docker.com/accounts/organization/manage/manage-a-team#assign-licenses-to-a-team)


Each team has a **Licenses** card that lists the product licenses the team assigns. Every member of the team receives those licenses, including members who join later.


To assign licenses, open the team from **Teams**, then select the **edit** icon on the **Licenses** card. For the full procedure, what happens when you don't have enough licenses, and what members lose when you remove a license, see [Manage licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses/#teams).


## [Set team repository permissions](https://docs.docker.com/accounts/organization/manage/manage-a-team#set-team-repository-permissions)


You must create a team before you are able to configure repository permissions. For more details, see [Create a team](https://docs.docker.com/accounts/organization/manage/manage-a-team#create-a-team).


To set team repository permissions:


1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** > **Repositories**. A list of your repositories appears.
3. Select a repository. The **General** page for the repository appears.
4. Select the **Permissions** tab.
5. Add, modify, or remove a team's repository permissions.
  - Add: Specify the **Team**, select the **Permission**, and then select **Add**.
  - Modify: Specify the new permission next to the team.
  - Remove: Select the **Remove permission** icon next to the team.


### [Permissions reference](https://docs.docker.com/accounts/organization/manage/manage-a-team#permissions-reference)


- `Read-only` access lets users view, search, and pull a private repository in the same way as they can a public repository.
- `Read & Write` access lets users pull, push, and view a repository. In addition, it lets users view, cancel, retry or trigger builds.
- `Admin` access lets users pull, push, view, edit, and delete a repository. You can also edit build settings and update the repository’s description, collaborator permissions, public/private visibility, and delete.


Permissions are cumulative. For example, if you have "Read & Write" permissions, you automatically have "Read-only" permissions.


The following table shows what each permission level allows users to do:


| Action | Read-only | Read & Write | Admin |
| --- | --- | --- | --- |
| Pull a Repository | ✅ | ✅ | ✅ |
| View a Repository | ✅ | ✅ | ✅ |
| Push a Repository | ❌ | ✅ | ✅ |
| Edit a Repository | ❌ | ❌ | ✅ |
| Delete a Repository | ❌ | ❌ | ✅ |
| Update a Repository Description | ❌ | ❌ | ✅ |
| View Builds | ✅ | ✅ | ✅ |
| Cancel Builds | ❌ | ✅ | ✅ |
| Retry Builds | ❌ | ✅ | ✅ |
| Trigger Builds | ❌ | ✅ | ✅ |
| Edit Build Settings | ❌ | ❌ | ✅ |


> Note
>
> A user who hasn't verified their email address only has `Read-only` access to the repository, regardless of the rights their team membership has given them.


## [Delete a team](https://docs.docker.com/accounts/organization/manage/manage-a-team#delete-a-team)


Organization owners can delete a team. When you remove a team from your organization, this action revokes member access to the team's permitted resources. It won't remove users from other teams that they belong to, and it won't delete any resources. Members also lose the licenses that came only from that team, unless another team assigns the same license or they hold a direct assignment. See [Remove licenses](https://docs.docker.com/accounts/organization/manage/manage-licenses/#remove-licenses).


1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.
2. Select **Teams**.
3. Select the **Actions** icon next to the name of the team you want to delete.
4. Select **Delete team**.
5. Review the confirmation message, then select **Delete**.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# Map identity provider groups to Docker teams

`https://docs.docker.com/security/provisioning/scim/group-mapping`

# Map identity provider groups to Docker teams


Ask Gordon


Copy Markdown


View Markdown

---

Table of contents

---

Subscription:
Business
For:
Administrators


Group mapping synchronizes groups from your identity provider (IdP) with teams in your Docker organization. For example, when you add a developer to the `moby:backend` group in your IdP, Docker adds them to the `backend` team in the `moby` organization.


Use group mapping to manage team membership through SAML SSO, SCIM, or both.


> Tip
>
> Use group mapping to add users to multiple organizations or teams. To assign each user to one organization or team, you can use SCIM [user-level attributes](https://docs.docker.com/security/provisioning/scim/provision-scim/#set-up-role-mapping).


## [Prerequisites](https://docs.docker.com/security/provisioning/scim/group-mapping#prerequisites)


Before you begin, you must have:


- SSO configured for your organization
- Administrator access to Docker Home and your identity provider


## [How group mapping works](https://docs.docker.com/security/provisioning/scim/group-mapping#how-group-mapping-works)


Group mapping uses IdP attributes to keep Docker Team membership synchronized:


- With SAML SSO, the IdP sends group membership when a user signs in.
- With SCIM, the IdP synchronizes group membership on its provisioning schedule.
- Docker identifies users by email address. Each Docker account must have a unique email address.
- Docker creates teams when a mapped group references a team that doesn't exist.


## [Set up group mapping](https://docs.docker.com/security/provisioning/scim/group-mapping#set-up-group-mapping)


To configure group mapping:


- Create groups in your IdP using Docker's naming format
- Configure your IdP to send group data
- Add users to the groups
- Test that membership synchronizes


You can use group mapping with SAML SSO alone or with SCIM for user lifecycle management.


### [Group naming format](https://docs.docker.com/security/provisioning/scim/group-mapping#group-naming-format)


Create groups in your IdP using the format: `organization:team`.


For example:


- For the "developers" team in the "moby" organization: `moby:developers`
- For multi-organization access: `moby:backend` and `whale:desktop`


Docker creates teams automatically if they don't already exist when groups sync.


### [Supported attributes](https://docs.docker.com/security/provisioning/scim/group-mapping#supported-attributes)


| Attribute | Description |
| --- | --- |
| `id` | Unique ID of the group in UUID format. This attribute is read-only. |
| `displayName` | Group name in the `organization:team` format. |
| `members` | A list of users that are members of this group. |
| `members(x).value` | Unique ID of a user in the group. |


*Create groups in your IdP using the format: organization:team.*

## [Configure group mapping with SSO](https://docs.docker.com/security/provisioning/scim/group-mapping#configure-group-mapping-with-sso)


Use group mapping with SSO connections that use the SAML authentication method.


> Note
>
> Group mapping through SSO isn't supported with the Microsoft Entra ID OIDC authentication method. Use SCIM to synchronize groups for OIDC connections.


Okta


Entra ID

The IdP interface may differ from these steps. For more information, see the [Okta documentation](https://help.okta.com/oie/en-us/content/topics/apps/define-group-attribute-statements.htm).


To set up group mapping:


1. Sign in to Okta and open your application.
2. Navigate to the **SAML Settings** page for your application.
3. In **Group Attribute Statements (optional)**, configure these values:
  - **Name**: `groups`
  - **Name format**: `Unspecified`
  - **Filter**: **Starts with** and `organization:`, where `organization` is your Docker organization name4. Create your groups by selecting **Directory**, then **Groups**.
5. Add groups in the `organization:team` format that match your Docker organization and team names.
6. Assign users to the groups.


The next time users sign in, Docker maps them to the teams you defined.


The IdP interface may differ from these steps. For more information, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims).


To set up group mapping:


1. Sign in to Entra ID and open your application.
2. Select **Manage**, then **Single sign-on**.
3. Select **Add a group claim**.
4. In **Group Claims**, select **Groups assigned to the application** with the source attribute **Cloud-only group display names**.
5. Select **Advanced options**, then the **Filter groups** option.
6. Configure the attribute like the following:
  - **Attribute to match**: `Display name`
  - **Match with**: `Contains`
  - **String**: `:`7. Select **Save**.
8. Select **Groups** > **All groups** > **New group** to create your groups.
9. Assign users to the groups.


The next time users sign in, Docker maps them to the teams you defined.


## [Configure group mapping with SCIM](https://docs.docker.com/security/provisioning/scim/group-mapping#configure-group-mapping-with-scim)


Use group mapping with SCIM to synchronize membership on your IdP's provisioning schedule. Before you begin, [set up SCIM](https://docs.docker.com/security/provisioning/scim/provision-scim/#enable-scim-in-docker).


Okta


Entra ID

The IdP interface may differ from these steps. For more information, see the [Okta documentation](https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-enable-group-push.htm).


To set up your groups:


1. Sign in to Okta and open your application.
2. Select **Applications**, then **Provisioning**, and **Integration**.
3. Select **Edit**, enable **Push Groups**, then select **Save**. The **Push Groups** tab appears in your application.
4. Create your groups by navigating to **Directory** and selecting **Groups**.
5. Add groups in the `organization:team` format that match your Docker organization and team names.
6. Assign users to the groups.
7. Return to **Integration**, then select **Push Groups**.
8. Select **Push Groups**, then **Find groups by rule**.
9. Configure the groups by rule like the following:
  - Enter a rule name, such as `Sync groups with Docker`.
  - Match groups by name. For example, use **Starts with** and `moby:`, or **Contains** and `:` for multiple organizations.
  - To sync after changes to groups or assignments, enable **Immediately push groups by rule**.


Find the rule under **By rule** in the **Pushed Groups** column. Matching groups appear in the groups table.


To push the groups from this table:


1. Select **Group in Okta**.
2. Select the **Push Status** drop-down.
3. Select **Push Now**.


The IdP interface may differ from these steps. For more information, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups).


1. Sign in to Entra ID and go to your application.
2. In your application, select **Provisioning**, then **Mappings**.
3. Select **Provision Microsoft Entra ID Groups**.
4. Set **Enabled** to **Yes**.
5. Confirm these attribute mappings:
  - `displayName` to `displayName`
  - `objectId` to `externalId`
  - `members` to `members`6. Select **Save**.


Next, set up group mapping:


1. Go to **Users and groups**.
2. Select **Add user/group**.
3. Select groups that use the `organization:team` format.
4. Select **Assign**.
5. Go to **Provisioning** and select **Start provisioning**.


To verify the sync, select **Monitor**, then **Provisioning logs**. In Docker Home, confirm that members appear in the mapped teams.


After synchronization, Docker adds users to the organizations and teams mapped in the IdP.


> Tip
>
> [Enable SCIM](https://docs.docker.com/security/provisioning/scim/provision-scim/) to provision and deprovision users automatically. Group mapping through SSO manages team membership but doesn't deprovision users.


## [Next steps](https://docs.docker.com/security/provisioning/scim/group-mapping#next-steps)


- [Assign roles](https://docs.docker.com/security/roles-and-permissions/core-roles/) to organization members.
- [Enforce sign-in](https://docs.docker.com/desktop/enterprise/enforce-sign-in/) for your organization.[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)

---

# AI Governance API 1

`https://docs.docker.com/reference/api/ai-governance`

Back [Reference](https://docs.docker.com/reference/)


- [Get started](https://docs.docker.com/get-started/)
- [Guides](https://docs.docker.com/guides/)
- [Manuals](https://docs.docker.com/manuals/)

API version
1 [Product manual](https://docs.docker.com/ai/sandboxes/governance/) [Download OpenAPI specification](https://docs.docker.com/reference/api/ai-governance/api.yaml) [Markdown](https://docs.docker.com/reference/api/ai-governance/latest.md)

Hosted API


# AI Governance API
## Privacy Preference Center



API 1 · 8 operations · 21 named schemas


## Overview


HTTP+JSON API for managing Docker governance policies and rules.


**Resource model.** An organization owns one or more policies. Each policy contains a list of rules grouped into a single domain: either `network` or `filesystem`. A policy's domain is derived from its rule actions; mixing domains within a single policy is not permitted.


**Lifecycle.** Create a policy with CreatePolicy, then add rules with CreateRule. Rules can be updated in place with UpdateRule or removed with DeleteRule. Deleting all rules does not delete the policy itself.


**Rule evaluation.** All rules in a policy are tested against every request. `deny` always wins: if any rule matches with `decision: deny`, the request is denied regardless of any `allow` rules.


**Enforcement.** Organization policies take precedence over local sandbox policies and cannot be overridden by individual users.


**Propagation.** Policy changes take up to five minutes to reach developer machines after being written.


See the [AI Governance documentation](https://docs.docker.com/ai/sandboxes/governance/) for product documentation.


## Connecting to the AI Governance API


### bearerAuth


Short-lived JWT obtained by exchanging Docker Hub credentials at `POST https://hub.docker.com/v2/auth/token`. Pass the JWT in the `Authorization: Bearer <token>` header. Tokens expire after a short period; request a fresh one when you receive a `401`.


The `password` field of the token request accepts any of the following credential types:


| Type | Format | Notes |
| --- | --- | --- |
| Password | Plain text | Your Docker Hub account password. |
| Personal Access Token (PAT) | `dckr_pat_*` | Recommended over passwords. Create one under Account Settings → Security. |
| Organization Access Token (OAT) | `dckr_oat_*` | Scoped to an organization. Create one under Organization Settings → Access Tokens. |


PAT and OAT strings can't be used directly as a bearer token. They must be exchanged at the token endpoint first.


See [Docker Hub authentication](https://docs.docker.com/reference/api/hub/latest/operations/AuthCreateAccessToken/) for full details.

`https://hub.docker.com/v2`

## Policies

Policy lifecycle management

## Rules

Rule management within an allowlist policy

*API 1 · 8 operations ·
21 named schemas*

## Operations

Filter operations
[GET `/orgs/{org_name}/governance/policies` List policies](https://docs.docker.com/reference/api/ai-governance/latest/operations/listPolicies/)
[POST `/orgs/{org_name}/governance/policies` Create policy](https://docs.docker.com/reference/api/ai-governance/latest/operations/createPolicy/)
[GET `/orgs/{org_name}/governance/policies/{policy_id}` Get policy](https://docs.docker.com/reference/api/ai-governance/latest/operations/getPolicy/)
[DELETE `/orgs/{org_name}/governance/policies/{policy_id}` Delete policy](https://docs.docker.com/reference/api/ai-governance/latest/operations/deletePolicy/)
[PATCH `/orgs/{org_name}/governance/policies/{policy_id}` Update policy](https://docs.docker.com/reference/api/ai-governance/latest/operations/updatePolicy/)
[POST `/orgs/{org_name}/governance/policies/{policy_id}/rules` Create rule](https://docs.docker.com/reference/api/ai-governance/latest/operations/createRule/)
[DELETE `/orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}` Delete rule](https://docs.docker.com/reference/api/ai-governance/latest/operations/deleteRule/)
[PATCH `/orgs/{org_name}/governance/policies/{policy_id}/rules/{rule_id}` Update rule](https://docs.docker.com/reference/api/ai-governance/latest/operations/updateRule/)

## Schemas


- [`AllowlistV0`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/AllowlistV0/)
- [`CedarV1Policy`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/CedarV1Policy/)
- [`CreatePolicyRequest`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreatePolicyRequest/)
- [`CreateRuleRequest`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/CreateRuleRequest/)
- [`DeletePolicyResponse`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeletePolicyResponse/)
- [`DeleteRuleResponse`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/DeleteRuleResponse/)
- [`Error`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/Error/)
- [`HTTPResource`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResource/)
- [`HTTPResources`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/HTTPResources/)
- [`Policy`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/Policy/)
- [`PolicySummary`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/PolicySummary/)
- [`Rule`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/Rule/)
- [`RuleActions`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleActions/)
- [`RuleDecision`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleDecision/)
- [`RuleResources`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/RuleResources/)
- [`Scope`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/Scope/)
- [`ScopePatch`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/ScopePatch/)
- [`UpdatePolicyRequest`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyRequest/)
- [`UpdatePolicyResponse`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdatePolicyResponse/)
- [`UpdateRuleRequest`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleRequest/)
- [`UpdateRuleResponse`](https://docs.docker.com/reference/api/ai-governance/latest/schemas/UpdateRuleResponse/)[llms.txt](https://docs.docker.com/llms.txt)

[llms-full.txt](https://docs.docker.com/llms-full.txt)

[Automated traffic detection](https://docs.docker.com/bot-detection/)