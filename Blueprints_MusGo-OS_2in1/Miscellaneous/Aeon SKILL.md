---
name: aeon
description: Set up and run an Aeon agent instance - get started from scratch, pick which skills to turn on or install more from packs, reschedule or change what runs, edit what an existing skill does, fix a skill that isn't firing, set the STRATEGY.md north star and soul/ voice, turn a Claude Code chat into a scheduled Aeon skill, and mine past Claude Code conversations for recurring work worth automating as a skill. Use when the user mentions Aeon, aeon.yml, an Aeon skill / instance / routine / pack, asks to schedule, enable, edit, or debug an agent that runs on a cron, or asks what of their repeated/manual work Aeon could take over.
---

> **Self-contained copy.** This is the complete aeon setup skill. The six reference docs it points to are appended in full under **“Bundled references”** at the end, so everything is in this one file - you do not need to fetch anything. (They are also hosted individually under https://www.aeon.fun/skills/aeon/references/ if you prefer.)

# Aeon

Aeon is an agent that runs on the user's own GitHub repo via Actions. A skill is a Markdown file (`skills/<name>/SKILL.md`); `aeon.yml` says which ones run and when.

Pick the mode they're asking for:

| | |
|---|---|
| **1 · Start** | No instance yet, or set one up from scratch |
| **2 · Reschedule** | Change times, cadence, or what a skill focuses on |
| **3 · Unblock** | "It didn't run" / "nothing happened" |
| **4 · Chat → skill** | Turn what we just did into a scheduled skill |
| **5 · Edit a skill** | Change what an existing skill does |
| **6 · What to turn on** | Pick skills, browse packs, install more |
| **7 · Strategy & voice** | `STRATEGY.md` and `soul/` - the north star and the tone |
| **8 · Mine history → skill** | "What of my repeated work could Aeon do for me?" - surface it from past Claude Code chats |

## Preflight (every mode)

1. Find the repo: current dir → `gh repo set-default` → ask. Clone it if it isn't local.
2. **Confirm `gh` points at THEIR instance, before any command that writes.**

   ```bash
   gh repo view --json nameWithOwner -q .nameWithOwner
   ```

   If that prints `aeonfun/aeon` and they aren't working on upstream itself, stop and run `gh repo set-default <owner>/<repo>`. `gh` prefers an `upstream` remote over `origin` when no default is pinned, and every Aeon write (`auth`, `secrets set`, `skills run`, config pushes) is a `gh -R <resolved>` call - so it will cheerfully put their API keys on the upstream repo and dispatch runs there. It looks like success: no error, a real run id, and the skill just never fires on their instance.
3. `gh auth status` - everything routes through `gh`. If it fails, tell them to run `gh auth login` and stop.
4. Use the `./aeon` CLI for all config writes. It preserves comments in `aeon.yml` and validates. Never hand-edit the YAML - with one exception: the CLI cannot *create* an entry for a brand-new skill (see Mode 4 step 4).

**Don't trust "disabled" for a skill you just created.** The read path lists skills from disk and defaults a missing `aeon.yml` entry to `enabled: false`, so "not configured" and "disabled" look identical. One command tells them apart:

```bash
comm -23 <(ls skills/*/SKILL.md | cut -d/ -f2 | sort) \
         <(grep -oE '^  [a-z0-9-]+:' aeon.yml | tr -d ' :' | sort)
```

Anything it prints is on disk but unconfigured. **Orientation - what's installed, what's on, and where everything lives: `https://www.aeon.fun/skills/aeon/references/layout.md`.**

**Setting any key or token:** read `https://www.aeon.fun/skills/aeon/references/secrets.md` - it has every secret and repo variable with the exact page to get it from. Always set secrets with `./aeon secrets set NAME --stdin`, never as a command argument.

---

## Mode 1 - Start on Aeon

Goal: one real notification in their phone, fast. Do not configure a schedule first.

1. **Get a repo. Ask public or private before you run anything** - it changes the command, and switching later means moving the repo.

   **Public** (recommend this): Actions minutes are free, and upstream skill updates arrive with one command.

   ```bash
   gh repo fork aeonfun/aeon --clone && cd aeon
   gh repo set-default <owner>/aeon        # REQUIRED - see below
   ```

   **Private**: a fork of a public repo is always public, so a private instance is a mirror, not a fork.

   ```bash
   gh repo create <name> --private
   git clone --bare https://github.com/aeonfun/aeon.git
   git -C aeon.git push --mirror https://github.com/<owner>/<name>.git
   rm -rf aeon.git && git clone https://github.com/<owner>/<name>.git && cd <name>
   git remote add upstream https://github.com/aeonfun/aeon.git
   gh repo set-default <owner>/<name>      # REQUIRED - see below
   ```

   Say both costs out loud before they pick private: Actions minutes bill against the account quota (2,000/mo on Free - scheduled skills burn it), and updates come from `git fetch upstream && git merge upstream/main` instead of `gh repo sync`.

   **Pin the default repo before any other command - both paths.** Both end up with an `upstream` remote (`gh repo fork --clone` adds one for you), and with no default pinned **`gh` prefers `upstream` over `origin`**. Everything in Aeon routes through `gh -R $(gh repo view …)`, so an unpinned checkout silently writes secrets to and dispatches runs against `aeonfun/aeon` instead of their instance - with no error, because the commands genuinely succeed on the wrong repo. Verify:

   ```bash
   gh repo view --json nameWithOwner -q .nameWithOwner   # must print THEIR repo
   ```

   Everything after this step is identical either way.
2. **Auth a model.** At least one is required. Fastest is `./aeon auth --oauth` (Claude Pro/Max, opens a browser), or `./aeon auth --key <key>`, which detects the provider **from the key prefix** - `sk-ant-oat` (OAuth), `sk-or-` (OpenRouter), `bk_` (Bankr), `inf_` (Surplus), `xai-` (Grok); anything else lands in `ANTHROPIC_API_KEY`.

   **UsePod and Venice keys have no prefix** and are undetectable, so a bare `--key` files them as a plain Anthropic key and the run fails later with a confusing auth error. They must be named:

   ```bash
   ./aeon auth --key <token> --provider usepod    # same for venice
   ```

   `--dry-run` prints the resolved `method=… → secret …` without calling `gh` or `claude` - worth running whenever the provider is in doubt.

   **Don't assume they have a Claude subscription:** nine providers work, including OpenRouter, Grok, GLM, and crypto-settled gateways. See "Providers and harnesses".
3. **Wire one channel.** Telegram is the fastest: create a bot with @BotFather, then `./aeon secrets set TELEGRAM_BOT_TOKEN --stdin` and `TELEGRAM_CHAT_ID`. Skip Discord/Slack/email for now - one channel is enough to prove it works.
4. **Run one skill now.** Pick it with Mode 6 - ask what they want handled, propose one - then `./aeon skills run <name>`. Wait for it, then `./aeon runs logs <id>`. They should get a Telegram message.
5. **Only then, schedule it.** `./aeon skills enable <name>` and set a time (see Mode 2).

Good first skills: `digest` (topic briefing), `github-monitor` (their repos), `heartbeat` (already on by default, reports only when something needs attention).

---

## Mode 2 - Reschedule / change the routine

Show them their day as a **timeline in their own timezone**, not a config file:

```
07:00  digest           "solana"
09:00  pr-review        your repos
18:00  heartbeat        health check
```

Build it from `./aeon skills ls --enabled --json`. (`--enabled` matters: plain `ls` prints a `SCHEDULE` column for *disabled* skills too - that's their `aeon.yml` entry, not proof anything fires.) No CLI, or want the raw file? `https://www.aeon.fun/skills/aeon/references/layout.md` has grep-only equivalents. Then take plain-language edits and apply them:

| They say | You do |
|---|---|
| "move the digest to 7am" | `./aeon skills schedule digest "0 6 * * *"` |
| "weekdays only" | `... "0 6 * * 1-5"` |
| "too noisy, twice a week" | `... "0 6 * * 1,4"` |
| "stop the crypto one" | `./aeon skills disable token-movers` |
| "make it about rust instead" | `./aeon skills set digest --var rust` |

Rules:
- **All cron in `aeon.yml` is UTC.** Convert from their timezone, and say so: "7am Paris = `0 6 * * *` UTC (5am in summer - want it pinned to local time?" There is no local-time option, so if DST matters, tell them which half of the year is off by an hour.
- Confirm back the **next 3 fire times in their timezone** after any change.
- `--dry-run` first on anything ambiguous, show the diff, then apply.
- Changes need a push to take effect. The CLI does it; confirm it landed.
- **Then check the value came out quoted** - one grep, every time:

  ```bash
  grep '^  <skill>:' aeon.yml
  ```

  The scheduler only reads `schedule: "…"` **with double quotes**. The CLI writes a *new* key unquoted, so an entry that had no `schedule:` yet comes back as `schedule: 0 12 * * *` and the skill is skipped forever. Details below.

Skills with `schedule: workflow_dispatch` are on-demand only - they never fire on cron. `reactive` ones fire on conditions, not time.

---

## Mode 3 - Unblock

"It didn't run." Check in this order and stop at the first hit:

1. **Is it on?** `./aeon skills ls --enabled` - is it listed?
2. **Duplicate key?** `node scripts/validate-config.js`. A repeated skill name in `aeon.yml` silently shadows the first one. Common after hand-edits.
3. **Is it even cron?** `workflow_dispatch` and `reactive` never fire on a schedule.
4. **Are Actions disabled?** `gh api repos/{owner}/{repo}/actions/permissions`. GitHub auto-disables scheduled workflows after 60 days of repo inactivity - this silently kills forks and nothing in Aeon surfaces it. Re-enable in repo Settings.
5. **Is the schedule quoted?** `grep '^  <skill>:' aeon.yml` - the value must be `schedule: "0 12 * * *"`, **with double quotes**.

   ```
   schedule: "0 12 * * *"   ✅ fires
   schedule: 0 12 * * *     ❌ never fires, no error anywhere
   ```

   `scheduler.yml` matches schedules with the bash regex `schedule: *"([^"]+)"`. An unquoted value doesn't match, `$SCHED` is empty, and the match loop hits `[ -z "$SCHED" ] && continue` - skipped silently, every tick, forever.

   How it gets that way: the CLI edits `aeon.yml` through a YAML document model that preserves an *existing* quoted node but writes a **newly added** key in plain style. So `./aeon skills schedule <name> "0 12 * * *"` is safe on an entry that already had a quoted `schedule:`, and quietly breaks one that didn't. Same for a first-time `--var`.

   **Nothing else detects this.** The file is valid YAML, `validate-config.js` reports CLEAN, and `./aeon skills ls --enabled` lists the skill with its schedule - because they all parse YAML properly and only the scheduler uses a regex. Fix by adding the quotes by hand.
6. **Did it run and fail?** `./aeon runs ls` then `./aeon runs logs <id>`. A failed skill retries after a 30-minute cooldown.

Three more, if the above are clean:

- **It ran against the wrong repo.** The giveaway is a command that reported success with a run id, but `./aeon runs ls` on their instance shows nothing. `gh` prefers `upstream` over `origin` when no default is pinned, so an unpinned checkout sends every write to `aeonfun/aeon`.

  ```bash
  gh repo view --json nameWithOwner -q .nameWithOwner   # if this isn't their repo:
  gh repo set-default <owner>/<repo>
  ```

  Then **clean up what landed upstream** - re-running against the right repo does not undo it. Any key set while mispointed is now a secret on someone else's repo:

  ```bash
  gh secret list -R aeonfun/aeon      # timestamps matching the misfire = theirs
  ```

  **Rotate it at the provider first, always** - it sat on a repo whose collaborators can land a workflow that reads it. Then re-set it on their instance with `./aeon secrets set NAME --stdin`.

  **Don't blind-delete it.** `gh secret list` shows only *last-updated*, so it cannot tell you whether the upstream repo already had that secret and the misfire **overwrote** it. Ask before removing:
  - Upstream never had it → `gh secret delete <NAME> -R <upstream>`.
  - Upstream had its own → deleting breaks *their* scheduled runs. The owner must re-set upstream's own value; the overwrite is not reversible from here.

  If the delete 403s, they never had write access - nothing was ever written, and the earlier command failed while only *looking* fine.
- **Missing secret.** Skills declare keys in `requires:`. Check them against `./aeon secrets ls --set`. A missing optional key (`KEY?`) means it degrades quietly, not that it breaks.
- **"No MCP tools available."** On the Claude harness a single unresolved `${VAR}` in `.mcp.json` disables **every** MCP server for that run, not just the broken one (`::warning::.mcp.json references secret(s) not set:` … `Skipping MCP this run.`). Grok degrades per-server instead. If an OAuth server broke a run *after* working, suspect a rotated refresh token that couldn't be saved - `https://www.aeon.fun/skills/aeon/references/mcp.md`.
- **It ran but sent nothing.** That's usually correct. Aeon's convention is silence on no signal - a clean run sends nothing rather than an empty report.

Note: GitHub only delivers ~10% of `*/5` cron ticks, so the scheduler catches up missed slots for up to 12 hours. A skill firing 40 minutes late is normal.

---

## Mode 4 - Turn this chat into a skill

They just did something in Claude Code and want it to happen on a schedule.

1. **Write the skill file.** `skills/<name>/SKILL.md` - frontmatter, then the prompt. Derive it from what actually happened in the session:
   - the prompt body = what they asked for, plus the steps that worked
   - `mode:` = `read-only` unless it needs to commit or open PRs
   - `requires:` = any API key the work hit (`KEY?` if it can degrade without it)
   - `category:` = one of `core evolution basics dev crypto productivity`
   - if they liked the output, paste a trimmed sample into the body as the format spec

2. **Fix the three things that break unattended runs:**
   - **Nobody's there.** Any point where you asked them a question has to become a default or a rule.
   - **Stay silent on nothing.** Add an explicit "if there's nothing worth reporting, log and exit without notifying." Otherwise it gets muted in a week.
   - **Don't repeat yesterday.** Add "check the last 3 days of `memory/logs/` and skip anything already reported."

3. **Check it can actually run there.** No local filesystem, no logged-in tools. If the session read their home directory or used a local MCP server, say so plainly - that part won't work unattended unless it's wired as a repo secret / `.mcp.json`. Wiring an MCP server for unattended use (dashboard Connect, OAuth refresh, the rotating-token PAT): `https://www.aeon.fun/skills/aeon/references/mcp.md`.

4. **Add the `aeon.yml` entry yourself.** A new skill on disk has no entry, and `./aeon skills enable|schedule` **will not create one** - they only flip entries that already exist, and report `no change - already in that state`, which is false. Add it by hand, disabled, before the fallback `heartbeat:` line:

   ```yaml
     my-skill: { enabled: false, schedule: "0 12 * * *" }
   ```

   **Include the quoted `schedule:` even though it's disabled - the quotes are load-bearing.** Writing a bare `{ enabled: false }` and letting `./aeon skills schedule` add the key later produces an *unquoted* value the scheduler cannot read, and the skill never fires (Mode 3, check 5). Seeding a quoted node here means every later CLI edit preserves the quotes.

   Match the inline `{ … }` form the other 61 entries use, on one line. `aeon.yml:367` reads per-skill `model:`/`harness:` overrides with a single-line grep, so an entry split across lines takes the global default instead.

   This is the one sanctioned exception to "never hand-edit the YAML". Validate after: `node scripts/validate-config.js` - but note it only checks structure, and will not catch an unquoted value.

5. **Regenerate BOTH catalogs, then ship it as a PR.** A new skill trips three CI gates. Run them locally - **nothing blocks a merge on red**, `main` is unprotected and has no rulesets, so an unrun gate just fails after the fact:

   ```bash
   bash scripts/check-skill-categories.sh   # category is one of the six
   bin/generate-skills-json                 # catalog/skills.json
   bin/generate-packs-json                  # catalog/packs.json - NOT optional
   ```

   `generate-packs-json` is the one everyone forgets: `catalog/skills.json` is itself a trigger path for `ci-packs-json`, so committing the skills catalog without the pack catalog goes red on a workflow you never touched. Commit both files.

   Full gate list, triggers, and the `ci-tests` / `ci-apps` commands: `https://www.aeon.fun/skills/aeon/references/ci.md`.

6. **Run it once** (`./aeon skills run <name>`), show them the output, then schedule it via Mode 2.

### Skill file shape

```yaml
---
name: my-skill
description: One line - what it does and what it sends.
metadata:
  title: My Skill
  mode: read-only
  category: basics
  var: ""
  tags:
    - content
  requires:
    - SOME_API_KEY?
---

Today is ${today}. <the prompt - plain instructions, including judgment calls>

## Steps
1. <the procedure - 44 of 82 skills lead with this>

## Network note
<curl / WebFetch / `./secretcurl` / `gh api` - how this skill fetches>

## Log
Report via `./notify` (use `./notify -f file.md` for anything multi-line).
Send nothing if there's nothing worth reporting.
Append what you did to `memory/logs/${today}.md` under a `### <skill-name>` heading.
```

Bodies run 133-757 lines (~306 median) - a skill is a prompt in prose, not a config file. `## Steps` / `## Network note` / `## Constraints` / `## Log` is the house shape.

Four things that bite when authoring - full detail in `https://www.aeon.fun/skills/aeon/references/skill-anatomy.md`:

- **`requires:` is a least-privilege allowlist - the run exports only the keys named here.** Inline (`requires: [KEY?]`) and block (`- KEY` lines) both parse, top-level or nested under `metadata:`. The catch is the value: only names matching `^[A-Z][A-Z0-9_]{2,}$` (trailing `?` = optional) are injected; a lowercase or malformed entry is silently dropped.
- **A typo'd `mode:` grants write.** Unknown values fall back to `write`, never to the safer tier. The exact string is `read-only`.
- **`${today}` / `${var}` are not templated.** Nothing rewrites `SKILL.md`; the workflow puts the date and var in the surrounding prompt and the model resolves them in context. Inventing `${my_thing}` yields a literal `${my_thing}`.
- **Never put a secret on a command line.** Use `./secretcurl` with a `{ENV_NAME}` placeholder in braces - Claude Code's permission analyzer blocks `$SECRET` expansions at run time.

Schedules do **not** go in `SKILL.md` - they live in `aeon.yml`. 10 upstream skills carry a `schedule:` or `cron:` frontmatter line anyway; **nothing reads it** (`scheduler.yml` parses `aeon.yml` only). Don't copy that pattern, and don't trust one you find - check `aeon.yml`.

---

## Mode 5 - Change what an existing skill does

"Make the digest shorter", "stop covering X", "add a source". More common than authoring a new skill.

**First, check whether it's a config change, not a file edit.** Most skills take a topic, filter, or mode through `var` - read the skill's `var:` line and the comment on its `aeon.yml` entry before touching the body. If `var` covers it, you're done:

```bash
./aeon skills set digest --var "rust"          # no file edit at all
```

Otherwise edit `skills/<name>/SKILL.md`:

1. **Read the whole body first.** These files run long (200-750 lines) and carry judgment rules, exit taxonomies, and scoring rubrics that a targeted edit can silently contradict.
2. **Don't strip the survival machinery.** Whatever else changes, the skill must keep: the `./notify` path, the silent-on-no-signal exit, the `memory/logs/${today}.md` append under `### <skill-name>`, and any already-reported dedup. Edits that "tighten" a skill often delete these. The `### <skill-name>` heading is parsed by the health loop and the dedup rule reads the last 3 days of logs - breaking either makes the skill re-report until it gets muted. Conventions in `https://www.aeon.fun/skills/aeon/references/skill-anatomy.md`.
3. **Update frontmatter if the behaviour moved.** A new data source that needs a key → add it to `requires:`. Now writes files or opens PRs → `mode: write`. Changed `description:`, `name:`, `category:` or `requires:` → regenerate **both** catalogs (`bin/generate-skills-json && bin/generate-packs-json`) and commit both; `skills.json` carries those fields and feeds `packs.json`. See `https://www.aeon.fun/skills/aeon/references/ci.md`.
4. **Warn if it's an upstream skill.** Anything shipped in `aeonfun/aeon` will conflict on the next `git merge upstream/main`. Fine, but say so - the two-repo convention is to keep local edits deliberate and few.
5. **Run it once** (`./aeon skills run <name>`) and read the output before leaving.

Automated alternative: the in-repo `autoresearch` skill evolves a target skill by generating four scored variations and shipping the winner as a PR. Reach for it when the ask is "make this better" rather than a specific change.

---

## Mode 6 - "What should I turn on?"

The real first question during onboarding. **Don't dump the catalog.** Ask two or three questions about what they actually want handled while they're away, then propose **three** skills with a one-line reason each.

Three at a time, not twelve. Every enabled skill is a recurring notification, and the fastest way to kill an instance is to make it noisy on day one. `heartbeat` is already on and stays silent unless something needs attention.

```bash
./aeon skills ls                 # all skills - SKILL / ON / SCHEDULE / PACK / DESC
./aeon skills ls --enabled       # only what actually runs
./aeon skills ls --pack crypto   # one pack
./aeon skills <name>             # one skill's detail
./aeon packs ls                  # the six first-party packs
```

`ls` footers with `82 skills · 1 enabled` - read it to them before proposing anything. First run installs the CLI runtime (tsx + yaml, ~12MB); the npm noise is one-time and expected. Grep-only equivalents: `https://www.aeon.fun/skills/aeon/references/layout.md`.

Packs are a visibility filter, not a runtime switch - revealing one runs nothing. Core (12), Evolution (9) and Basics (18) show by default; Dev (13), Crypto (19) and Productivity (11) are on demand.

Reasonable starting sets:

| They care about | Propose |
|---|---|
| Their repos | `github-monitor`, `pr-review`, `changelog` |
| A topic / research | `digest`, `article`, `mention-radar` |
| Markets | `token-movers`, `defi-overview`, `monitor-polymarket` |
| Shipping / traction | `heartbeat`, `shiplog`, `bd-radar` |

### Installing more

```bash
bin/install-skill-pack --list             # browse the community registry
bin/install-skill-pack <owner>/<repo>     # install a curated pack
bin/add-skill <owner>/<repo> --list       # any repo containing SKILL.md files
```

Everything lands **disabled**, security-scanned, with provenance in `skills.lock`.

**Read a community SKILL.md before enabling it.** Installing a pack means running a stranger's prompt with your secrets injected. The scanner is regex - it can't catch prompt injection. Check that `requires:` matches the stated job, that `capabilities:` is honest, and that nothing instructs the agent to send data somewhere unrelated.

**Confirm explicitly before enabling anything with real-world blast radius:** `distribute-tokens` (sends USDC), `schedule-ads` (spends money), `send-email` and `vuln-scanner` (contact real people), `deploy-prototype` and `feature` (push to other people's repos).

---

## Mode 7 - Strategy and voice

Two files that ride in the context of **every** run. Neither is required, both are cheap, and they move output quality more than any per-skill tuning.

### `STRATEGY.md` - the north star

Imported into `CLAUDE.md`, so it's in every skill's context: goal, priorities, audience, hard constraints. When a choice isn't otherwise determined, this breaks the tie. Keep it **tight** (it costs tokens on every single run) and **specific** (a vague strategy can't break a tie).

```bash
./aeon strategy show
./aeon strategy set --file STRATEGY.md
./aeon strategy build "<one-line goal>"    # dispatches the strategy-builder skill
```

`build` reads the brief plus the repo README and `memory/MEMORY.md`, then commits a draft. It runs as an Action, so pull once it finishes. No API key needed.

### `soul/` - how it sounds

By default Aeon has no personality. `soul/SOUL.md` (identity, worldview, opinions) and `soul/STYLE.md` (voice, vocabulary, anti-patterns) are read on every run, so notifications and content sound like the operator. `soul/examples/` holds 10-20 calibration samples.

```bash
./aeon soul show
./aeon soul build --handle <x-handle> --name "<Full Name>" --links <url,url>
```

`XAI_API_KEY` gives the richest read of a real X timeline; without it, `soul-builder` falls back to web search. There's also a gallery of complete example souls at github.com/aeonfun/soul.md to start from.

**The quality bar: specific enough to be wrong.** *"I think most AI safety discourse is galaxy-brained cope"* is useful. *"I have nuanced views on AI safety"* is not. Push for the first kind - a soul that can't offend anyone won't sound like anyone.

---

## Mode 8 - Mine history for skills to automate

"What am I doing by hand over and over that Aeon could just do?" Mode 4 turns *this* chat into a skill; Mode 8 mines *past* chats to find which chat is worth turning into one. It reads the operator's local Claude Code transcripts (`~/.claude/projects/*/*.jsonl`), so it only works on their own machine - never inside an Aeon run.

1. **Scan.** Run the miner from the instance repo root:

   ```bash
   node .claude/skills/aeon/scripts/mine-history.mjs --days 45 --top 15
   ```

   It parses every top-level session in the window (skips subagent sidechains), normalises shell commands to `binary subcommand`, groups session titles, and prints a digest ranked by **distinct sessions × distinct days** - recurrence and cadence, not raw volume. Flags: `--days N` (window, default 120), `--project SUBSTR` (only sessions whose cwd matches - scope to one repo/topic), `--top N`, `--min-sessions N`, `--json`. It has no dependencies and reverts to a clean error if there's no history. Deeper reading of the tables and the candidate rubric: `https://www.aeon.fun/skills/aeon/references/history-mining.md`.

2. **Read it as a human would.** The digest is raw signal, not a verdict - the judgment is yours:
   - **Recurring command workflows** - a `binary subcommand` across many sessions *and* many days is a habit. Universal plumbing (`git status`, `gh auth`, bare `node`/`python3`) is already filtered out, but `gh pr`/`gh api`/`npm run` are substrate too - high everywhere, weak as a skill idea. Look for the *distinctive* recurring call: a named script, a specific CLI (`x-cli`, `langfuse`, `raindrop`), a tight `gh api` pattern.
   - **Recurring task themes** - grouped session titles are the strongest signal. A title you've hit across many days at a rough cadence ("check X", "review Y", "digest Z") is almost always the real automation candidate.
   - **Tooling / projects** - which MCP servers and repos the work lives in; tells you what a skill would need wired and where to scope `--project`.

3. **Filter to genuine candidates.** A row is worth proposing only if it's all of:
   - **Recurring** - spans several sessions across several days, not one busy afternoon.
   - **Fetch/compute/report-shaped** - pulls or checks something and reports. Interactive, decision-heavy, or one-off migration work does *not* automate.
   - **Unattended-safe** - no dependence on local files, logged-in desktop apps, or a human answering mid-task (Mode 4 step 2/3 covers hardening).
   - **Not already a skill.** Dedup against the instance: `./aeon skills ls`. Much recurring `gh pr` work is already `pr-review`/`pr-check`; a research cadence is already `digest`/`mention-radar`. If an existing skill covers it, the move is Mode 2 (reschedule) or Mode 5 (edit its `var`), **not** a new skill.

4. **Propose three, with evidence.** Don't dump the digest. Name **three** candidates, each with its recurrence count as proof ("you did X across N sessions over D days"), a one-line skill sketch (what it fetches, what it sends), a suggested `mode:` (`read-only` if it only fetches and reports) and a suggested `schedule:` inferred from the observed cadence (seen ~daily → daily; ~weekly → weekly). Ask which to build.

5. **Hand off to Mode 4** to author the chosen one - the same skill-file shape, unattended-hardening, quoted-`schedule:` entry, and dual-catalog CI. Mode 8 finds the work; Mode 4 ships it.

**Privacy:** the transcripts are read locally and only the aggregate digest is surfaced. Don't paste raw prompt bodies or anything sensitive from a session into a channel or a committed file; the counts and titles are enough to decide.

---

## Providers and harnesses

Two independent axes. Don't confuse them: the **gateway** decides which model answers; the **harness** decides which CLI runs the skill.

### Gateway - what powers Claude Code

Set a secret and it's live. `aeon.yml` ships `gateway: { provider: auto }`, which resolves at run time from whichever keys exist, in this priority order:

```
claude → anthropic → openrouter → bankr → usepod → venice → surplus → grok → glm
```

`direct` is **not** a hop in that chain - it's the placeholder when *none* of the nine secrets is set. It requires nothing and configures nothing, so the run proceeds on whatever `ANTHROPIC_*` env happens to exist and otherwise fails at the first model call. "Resolved to `direct`" in a log means **no key was found**, not that a fallback worked.

| Provider | Secret | Notes |
|---|---|---|
| Claude subscription | `CLAUDE_CODE_OAUTH_TOKEN` | One-click OAuth, included in Pro/Max |
| Anthropic API | `ANTHROPIC_API_KEY` | Pay-as-you-go |
| OpenRouter | `OPENROUTER_API_KEY` | `sk-or-…` · Anthropic-native passthrough, lowest-risk |
| Bankr | `BANKR_LLM_KEY` | `bk_…` · discounted Opus |
| UsePod | `USEPOD_TOKEN` | No prefix - pass `--provider usepod`. Token sits in the base URL, keep it secret |
| Venice | `VENICE_API_KEY` | No prefix - pass `--provider venice`. Privacy-first, bridged via a sidecar |
| Surplus | `SURPLUS_API_KEY` | `inf_…` · settles USDC on Base - fund the wallet + `approve()` once first |
| Grok (xAI) | `XAI_API_KEY` | `xai-…` · passthrough to `api.x.ai` |
| GLM (Z.AI) | `GLM_API_KEY` | No prefix - pass `--provider glm`. Alias `ZAI_API_KEY`. Passthrough to `api.z.ai/api/anthropic` |

It runs as a **cascade**, not a single choice: the highest-priority key goes first, and on *any* failure (no credits, rate limit, outage, dud response) the run falls over to the next provider whose key is set. It only errors if every one fails. The log prints `Routing attempt via '<provider>'` per hop.

- **Reorder:** repo variable `GATEWAY_ORDER` (space-separated names).
- **Pin one** (disables failover): `./aeon config set gateway <name>`.
- **Any Anthropic-compatible endpoint:** `ANTHROPIC_API_KEY` plus the repo variable `ANTHROPIC_BASE_URL` - e.g. `https://api.deepseek.com/anthropic`.

### Harness - which CLI runs the skill

`claude` (default) or `grok`. The Grok harness runs the `grok` CLI instead of Claude Code and **bypasses the gateway entirely** - it has its own auth.

- **Set it:** `./aeon config set harness grok` globally, or `harness: "grok"` on a single skill's `aeon.yml` entry - **quoted, on the entry's one inline line**. Per-skill `model:` and `harness:` are read by a single-line grep that requires double quotes (`aeon.yml:367`, `:380`), so an unquoted or line-split override is silently ignored and the skill keeps running the global default - no error, and the log's `model=` line looks normal. After setting either by CLI, re-read the entry and add the quotes if they're missing.
- **Auth:** `XAI_API_KEY`, or an X account (SuperGrok / X Premium+) via the dashboard's **Connect X account**, which stores `GROK_CREDENTIALS`. There is no CLI flag for the X OAuth flow - send them to `./aeon` (the dashboard) for that one.
- **Models:** `grok-4.5` (default, reasoning) or `grok-composer-2.5-fast` (cheap).
- **No free tier.**

Tell them up front:
- Grok runs report **0 tokens** - its JSON carries no token counts, so cost tracking reads blank. Not a bug.
- The X OAuth session expires. If unattended runs start failing on auth, reconnect.
- `mode: read-only` still applies (maps to `--sandbox read-only`), and MCP works.

Per-skill grok knobs, in `SKILL.md` frontmatter (ignored on the Claude harness): `max_turns` (default 60), `best_of_n`, `verify`, and `effort` (`low|medium|high|xhigh|max` - reasoning models only; `grok-composer-2.5-fast` rejects it).

# Bundled references

# Inventory & paths

Where everything lives in an Aeon repo, and the fastest way to see what's on.

## Listing skills

```bash
./aeon skills ls                  # all skills + live config
./aeon skills ls --enabled        # only what actually runs
./aeon skills ls --pack crypto    # one pack
./aeon skills <name>              # one skill's detail
./aeon skills ls --enabled --json # for building the Mode 2 timeline
```

`ls` prints `SKILL / ON / SCHEDULE / PACK / DESCRIPTION` and a footer - `82 skills · 1 enabled`. First run installs the CLI runtime (tsx + yaml, ~12MB, one-time); the noise is expected.

**The `SCHEDULE` column is populated for disabled skills too** - it's their `aeon.yml` entry, not proof anything fires. Only the `●` in `ON` means it runs.

### Without the CLI

Read-only greps for when the CLI isn't installed, `gh` isn't authed, or you want to see the raw file. Run from the repo root:

```bash
# every skill on disk
ls skills/*/SKILL.md | cut -d/ -f2

# what's actually enabled, with its cron
grep -E '^  [a-z0-9-]+: *\{[^}]*enabled: true' aeon.yml

# the day as a UTC-sorted timeline (Mode 2)
grep -E '^  [a-z0-9-]+: *\{[^}]*enabled: true' aeon.yml \
  | sed -E 's/^  ([a-z0-9-]+):.*schedule: *"([^"]*)".*/\2|\1/' \
  | awk -F'|' '{split($1,c," "); printf "%02d:%02d UTC  %-18s %s\n", c[2], c[1], $2, $1}' \
  | sort
```

### The two lists that should match

A skill directory with no `aeon.yml` entry reads as **disabled** and is indistinguishable from a configured-but-off skill - the Preflight warning. This is the command that tells them apart:

```bash
comm -23 <(ls skills/*/SKILL.md | cut -d/ -f2 | sort) \
         <(grep -oE '^  [a-z0-9-]+:' aeon.yml | tr -d ' :' | sort)
```

Anything printed is **on disk but unconfigured** - `./aeon skills enable` on it reports `no change - already in that state`, which is false (Mode 4 step 4). Empty output means every skill is configured.

The reverse - an `aeon.yml` entry with no skill directory - is caught by `node scripts/validate-config.js` ("skill-refs").

## Paths

```
aeon.yml           the only runtime config. What's enabled, when, per-skill var/model/harness.
                   Cron here is UTC and the scheduler is the ONLY thing that reads it.
aeon               the CLI + dashboard entrypoint. With args → apps/cli; bare → web dashboard.
CLAUDE.md          operating manual, in every run's context. Imports @STRATEGY.md.
STRATEGY.md        the north star (Mode 7). Costs tokens on every run - keep it tight.
AGENTS.md          GENERATED from STRATEGY.md for the grok harness. Never hand-edit;
                   run `node scripts/gen-agents-md.js` (gated by ci-agents-md).

skills/<name>/SKILL.md    the skills themselves - 61 upstream. One prompt per file.
soul/              SOUL.md + STYLE.md + examples/ - voice, read on every run (Mode 7).
memory/            durable state between runs:
  logs/<date>.md     per-run append under `### <skill-name>`. The dedup substrate.
  MEMORY.md          the durable index - long-lived facts, not run history.
  issues/, topics/   durable memory: issue tracker + knowledge notes by topic.
  cron-state.json    scheduler bookkeeping. Infrastructure - no skill touches it.
output/            what skills produce: articles/, images/.
catalog/           generated manifests - skills.json, packs.json (+ .config), skill-packs.json.
                   Never hand-edit; regenerate with bin/generate-*-json (ci gates).
bin/               operator tools: add-skill, install-skill-pack, generate-*-json, export-skill.
scripts/           runtime helpers + validators. notify.sh and secretcurl.sh are copied
                   to ./notify and ./secretcurl at run time - that's why they're not at root.
apps/              dashboard (Next.js), cli, mcp-server, webhook (Cloudflare Worker).
docs/              CONFIGURATION.md, CAPABILITIES.md, skill-packs.md, harnesses.md.
.github/workflows/ 14 workflows: aeon.yml (the runner), scheduler.yml (cron matcher),
                   chain-runner.yml, and 9 ci-*.yml gates (see references/ci.md).
```

### The three that get confused

- **`aeon.yml`** (repo root) - operator config: what runs and when.
- **`.github/workflows/aeon.yml`** - the runner that executes a skill. Different file, same name. When someone says "aeon.yml" mid-debug, check which they mean.
- **`catalog/skills.json`** - the generated catalog. Read by the dashboard and `bin/add-skill`; deliberately does **not** carry schedules, because those are per-deployment operator config.

# Aeon secrets and variables - where to get each one

## How to set anything

**Secrets** (credentials - write-only, can't be read back):

```bash
./aeon secrets set NAME --stdin      # paste the value, then Ctrl-D
./aeon secrets ls --set              # what's configured
./aeon secrets ls --unset            # what's missing
./aeon secrets rm NAME
```

Always `--stdin`. Passing a key as an argument puts it in shell history.

**Variables** (non-secret behaviour toggles - readable):

```bash
gh variable set NAME "value"
gh variable list
```

Getting the two mixed up is the most common setup mistake. A credential in variables is exposed; a toggle in secrets works but you can't read it back to check what it's set to.

Three things worth knowing:

- **Secrets are per-repo.** A forked instance inherits none of the parent's keys. That's deliberate - billing isolation and blast-radius containment.
- **Optional keys** are marked `KEY?` in a skill's `requires:`. Missing means the skill degrades to a public/lower-quality path, not that it breaks.
- **Two secrets have side effects when set:** `TELEGRAM_BOT_TOKEN` auto-registers the Telegram slash-command menu, and any gateway key re-resolves which provider the runs route through.

---

## 1. Model auth - need at least one

The first two are the direct-to-Anthropic options; the rest are gateways. Setting several is fine and encouraged - the runner cascades through them and fails over.

| Secret | Where to get it |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Run `claude setup-token` locally → paste the `sk-ant-oat01-…` (valid 1 year). Or click AUTH in the dashboard. Runs on your Pro/Max subscription, no per-token billing |
| `ANTHROPIC_API_KEY` | console.anthropic.com - pay-as-you-go `sk-ant-…`. Also accepts any Anthropic-compatible key for a proxy |
| `OPENROUTER_API_KEY` | openrouter.ai/keys - `sk-or-…` |
| `BANKR_LLM_KEY` | bankr.bot/api-keys - `bk_…`, discounted Opus |
| `USEPOD_TOKEN` | usepod.ai - token is embedded in the base URL, treat as secret |
| `VENICE_API_KEY` | venice.ai/settings/api - routed through a local translator sidecar |
| `SURPLUS_API_KEY` | surplusintelligence.ai - `inf_…`, settles USDC on Base. Fund the wallet and `approve()` once before first use |
| `XAI_API_KEY` | console.x.ai - `xai-…`. Triple duty: X/tweet skills, the Grok gateway, and API-key auth for the grok harness |
| `GROK_CREDENTIALS` | Dashboard → AUTH → **Connect X account**. Base64 of your `~/.grok` session; runs the grok harness on a SuperGrok / X Premium+ entitlement. No CLI path for this one |

## 2. Notification channels - need at least one

| Secret | Where to get it |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Message @BotFather → `/newbot` → copy the token |
| `TELEGRAM_CHAT_ID` | Message your new bot, then open `api.telegram.org/bot<TOKEN>/getUpdates` and read `message.chat.id` |
| `DISCORD_WEBHOOK_URL` | Channel Settings → Integrations → Webhooks → New Webhook → Copy URL (outbound only) |
| `DISCORD_BOT_TOKEN` + `DISCORD_CHANNEL_ID` | discord.com/developers/applications → your app → Bot. Add the `channels:history` scope. Only needed for inbound commands |
| `SLACK_WEBHOOK_URL` | api.slack.com/apps → Create App → Incoming Webhooks → Install → Copy URL |
| `SLACK_BOT_TOKEN` + `SLACK_CHANNEL_ID` | Same app → add `channels:history` + `reactions:write` scopes. Only for inbound |
| `RESEND_API_KEY` + `NOTIFY_EMAIL_TO` | resend.com/api-keys. Powers **all** outbound email - the notification channel, emailed digests, and security disclosures |
| `BUZZ_PRIVATE_KEY` + `BUZZ_CHANNEL_ID` (+ `BUZZ_RELAY_URL`) | [Buzz](https://buzz.xyz) (Block's Nostr-relay workspace). `BUZZ_PRIVATE_KEY` is the agent's `nsec` keypair, `BUZZ_CHANNEL_ID` the target channel UUID (`buzz channels list`), `BUZZ_RELAY_URL` your relay (defaults to localhost). Outbound only; needs the `buzz` CLI staged in the run |

Telegram is the fastest to set up and the only one with inline buttons and slash-commands. Start there.

**If the channel isn't private to you**, set `DISCORD_ALLOWED_AUTHOR_ID` / `SLACK_ALLOWED_USER_ID` (variables). Left unset, *anyone* in the channel can command the agent. Telegram is already scoped to a single chat ID.

## 3. GitHub tokens

| Secret | Where to get it |
|---|---|
| `GITHUB_TOKEN` | Built in - nothing to set. Scoped to this repo only |
| `GH_GLOBAL` | github.com/settings/tokens -> **Tokens (classic)** -> scopes **`repo`** + **`workflow`** -> add as `GH_GLOBAL`. One token covers everything cross-repo (`github-monitor`, `pr-review`, `feature`, `changelog` push-to), private reads, repository security advisories / PVR (disclosure skills), and secrets writeback. Auto-promoted to the run's `GITHUB_TOKEN` |
| `GH_READ_PAT` | *Legacy / optional.* Folded into `GH_GLOBAL`. Keep a separate read-only PAT only to give `bd-radar`'s private cross-repo enrichment a read token without granting the run write |
| `GH_SECRETS_PAT` | *Optional.* Folds into `GH_GLOBAL` (its `repo` scope already writes secrets). Set a dedicated PAT only to isolate secrets-write from the main token: github.com/settings/personal-access-tokens -> add this repo under Repository access (a PAT without it 404s) -> Repository permissions -> Secrets: Read and write. Used by OAuth-connected MCP servers or the Grok X-account harness |

`GH_SECRETS_PAT` gotcha: providers rotate the refresh token every run, and the runner needs this PAT to save each rotation back. Without it, auth breaks exactly one run after you connect. After adding it, re-connect any already-connected server once.

**Scope summary (one classic PAT as `GH_GLOBAL`):** `repo` = cross-repo + private read/write, security advisories / PVR, and secrets writeback; `workflow` = pushing `.github/workflows/` changes (`aeon-update`, `spawn-instance`, `auto-workflow`). `read:org` / `admin:org` are not needed. Use a **classic** PAT - the advisories / PVR API is unreliable with fine-grained tokens.

## 4. Skill API keys - all optional

Each is opt-in. Unset means the skills that want it skip or degrade.

| Secret | Used by | Where |
|---|---|---|
| `XAI_API_KEY` | tweet/X skills, `digest`, `shiplog`, `soul-builder` | console.x.ai |
| `COINGECKO_API_KEY` | crypto price/market skills | coingecko.com/en/api |
| `ALCHEMY_API_KEY` | on-chain RPC/data | dashboard.alchemy.com |
| `ETHERSCAN_API_KEY` | `tx-explain`, `investigation-report`, `onchain-monitor` | etherscan.io/apis - V2 is one multichain key covering Ethereum + Base |
| `BASESCAN_API_KEY` | `investigation-report` | Simplest is the **same value** as `ETHERSCAN_API_KEY` |
| `BASE_RPC_URL` | Base on-chain skills | docs.base.org/chain/node-providers - a public RPC is used by default |
| `BANKR_API_KEY` | `distribute-tokens` (real on-chain sends) | bankr.bot/api-keys - Wallet API, not the LLM key |
| `VERCEL_TOKEN` | `deploy-prototype` | vercel.com/account/settings/tokens |
| `REPLICATE_API_TOKEN` | `article --visual` hero images | replicate.com/account/api-tokens |
| `ADMANAGE_API_KEY` | `schedule-ads` | admanage.ai/api-docs |
| `RESEND_API_KEY` | `send-email`, `vuln-scanner` disclosures | resend.com |
| `YDC_API_KEY` | `you-web-search` (required for it) | api.you.com - optional `YOUCOM_FRESHNESS` / `YOUCOM_LIVECRAWL` variables tune freshness + full-page crawl |
| `TASKMARKET_API_KEY` | `taskmarket-delegate` - only `create`/`submit`; `browse` works without | tasks.taskmarket.dev - optional `TASKMARKET_WORKER_ADDRESS` tags submissions |

## 5. Observability - optional

| Secret | Where |
|---|---|
| `LANGFUSE_PUBLIC_KEY` | Langfuse → Settings → API Keys - `pk-lf-…` |
| `LANGFUSE_SECRET_KEY` | Same page - `sk-lf-…` |

Both must be set for tracing to activate. Then every run streams to Langfuse as a trace with LLM calls, tokens, cost, and prompts.

## 6. Repo variables (not secrets)

Set with `gh variable set NAME "value"`.

| Variable | Effect |
|---|---|
| `ANTHROPIC_BASE_URL` | Point `ANTHROPIC_API_KEY` at any Anthropic-compatible endpoint, e.g. `https://api.deepseek.com/anthropic` |
| `GATEWAY_ORDER` | Space-separated provider names - override the failover priority |
| `GROK_MODEL` | Model for the Grok gateway path |
| `GLM_MODEL` | Model for the GLM (Z.AI) gateway path (default `glm-5.2`) |
| `GLM_REASONING_EFFORT` | GLM gateway reasoning depth: `low` / `high` / `max` (default `high`) |
| `STATE_BACKEND` | `file` (default) · `dual` · `issues` - where run state lives |
| `HEALTH_ISSUES` | `0` disables the votable per-skill health Issues |
| `NOTIFY_MIN_SEVERITY` | Suppress notifications below this level |
| `NOTIFY_EMAIL_FROM` | Default `aeon@notifications.aeon.bot` - **must be a Resend-verified sender** |
| `NOTIFY_EMAIL_SUBJECT_PREFIX` | Default `[Aeon]` |
| `LANGFUSE_HOST` | Default `https://cloud.langfuse.com` (EU). Set the US host to switch region |
| `LANGFUSE_TRACING` | `0` to disable |
| `LANGFUSE_LOG_CONTENT` | `0` = metadata only, no prompt bodies |
| `DISCORD_ALLOWED_AUTHOR_ID` / `SLACK_ALLOWED_USER_ID` | Restrict who can command the agent inbound |
| `VENICE_BASE_URL` | Point Venice at a compatible endpoint |

# MCP servers

## First: which direction?

Two unrelated things share the name. Get this wrong and nothing works.

| | |
|---|---|
| **`.mcp.json`** - *external MCP servers, called BY Aeon skills* | Wired via the dashboard MCP panel or `./aeon mcp add`. This is what you want when a skill needs a tool. |
| **`bin/add-mcp`** - *Aeon itself AS an MCP server* | Builds `apps/mcp-server` and registers it with Claude Code / Desktop, so all 82 skills appear as `aeon-*` tools **in your local Claude**. Nothing to do with a skill calling out. |

The rest of this doc is the first one. For the second: `bin/add-mcp`, `--desktop` for a Claude Desktop snippet, `--uninstall` to remove, `claude mcp list` to verify.

## Adding a server

### Dashboard (the normal path)

`./aeon` → **MCP** panel. Featured servers install one-click. Behaviour depends on the catalog entry:

- **`authSecret`** → wires `Authorization: Bearer ${SECRET}` and shows a paste-token row.
- **`oauth: true`** → shows **Connect**, runs the browser OAuth flow, stores tokens as repo secrets. See *Key refresh* below.
- **Neither** → public server, no auth wired.

### CLI

```bash
./aeon mcp ls                              # what's configured
./aeon mcp catalog                         # featured slugs
./aeon mcp add glim                        # by catalog slug
./aeon mcp add myserver https://x.com/mcp  # custom HTTP
./aeon mcp add myserver https://… --sse    # SSE transport
./aeon mcp add myserver https://… --header "Authorization: Bearer \${MY_TOKEN}"
./aeon mcp rm myserver
```

Writes `.mcp.json` and pushes. `--dry-run` previews. **OAuth servers can't be connected from the CLI** - the flow needs a browser, so use the dashboard.

### In code - adding a featured server

Append to `MCP_CATALOG` in `apps/dashboard/lib/mcp-catalog.ts`. That one array feeds the dashboard's Featured list, `./aeon mcp catalog`, and the per-skill MCP panel:

```ts
{
  slug: 'myserver',                    // also the .mcp.json key and MCP_<SLUG>_* secret stem
  name: 'My Server',
  url: 'https://myserver.com/mcp',
  logo: 'https://…',
  description: '…',
  transport: 'http',                   // or 'sse'; default http
  authSecret: 'MYSERVER_API_KEY',      // static bearer - OR:
  oauth: true,                         // browser OAuth flow
  oauthScopes: ['openid', 'offline_access'],
  oauthClientId: '…',                  // only if the server has no dynamic registration
}
```

`authSecret` and `oauth` are **mutually exclusive**. Request `offline_access` only if the provider advertises it - Robinhood rejects it and only offers `internal`.

### `.mcp.json` shape

```json
{
  "mcpServers": {
    "glim": {
      "type": "http",
      "url": "https://glim.sh/mcp",
      "headers": { "Authorization": "Bearer ${MCP_GLIM_TOKEN}" }
    }
  }
}
```

`${VAR}` references are resolved from repo secrets at run time. Not committed upstream - each instance has its own.

## Writing a skill that uses one

```yaml
mcp: [glim]        # frontmatter - catalog metadata ONLY
```

**`mcp:` does not gate anything at run time.** Unlike `requires:` (a real least-privilege allowlist for secrets), `mcp:` is read only by `bin/generate-skills-json` for the catalog and the dashboard's requirement panel. Every server in `.mcp.json` is allowed for **every** skill on both harnesses. Declare it anyway - it's how the dashboard tells the operator what to connect.

In the body: tools surface as `mcp__<server>__*` (Claude) / `<server>__<tool>` (grok). **Discover them from the server rather than hardcoding a list** - the house convention is "the tool descriptions are the source of truth, don't assume a fixed list."

Always handle the not-connected case explicitly, as `glim-mcp` does:

> **No `mcp__glim__*` tool callable** → the server isn't connected (or its secrets are missing, in which case the workflow logged a `::warning::` and skipped MCP). Log `GLIM_NOT_CONNECTED`, notify once pointing at dashboard → MCP → Connect, exit.

If calls cost money, set a hard budget in the body (`glim-mcp`: ≤10 tool calls, ≤25 with `--deep`) and say to synthesize from what's in hand when it's spent.

## Where the credentials show up

A connected server's credentials are stored as ordinary repo secrets named from its slug (`tokenVar`/`oauthVar` in `lib/mcp-catalog.ts`), so they appear in **two** places:

- **MCP panel** - inline per server, next to the `${VAR}` it satisfies. Where you set or re-connect them.
- **Settings → Access Keys → MCP** - the credential inventory. Rows are built dynamically from whatever `MCP_*_TOKEN` / `MCP_*_OAUTH` secrets exist, each carrying its server's catalog logo; the section is hidden entirely until a server is connected. Removing one here leaves the server wired in `.mcp.json` but unauthenticated.

There is nothing to add to `BUILTIN_SECRETS` when you add a catalog server - the group is derived from `MCP_SECRET_RE` and `MCP_SECRET_OWNER`, so a new `MCP_CATALOG` entry brings its own group row, description, and logo.

## Key refresh

### Static tokens

Nothing to refresh. The secret named by `authSecret` is injected wherever `.mcp.json` references `${VAR}`.

### OAuth - the durable loop

1. **Connect** (dashboard) - discovery (RFC 9728 → RFC 8414/OIDC), dynamic client registration (RFC 7591), Authorization Code + PKCE. Tokens never reach the browser.
2. **Store** - two repo secrets:
   - `MCP_<SLUG>_TOKEN` - short-lived access token, referenced by the header
   - `MCP_<SLUG>_OAUTH` - JSON refresh material (`token_endpoint`, `client_id`, optional `client_secret`, `refresh_token`, `scope`)
3. **Refresh** - every run sources `scripts/mcp-oauth-refresh.sh` *before* the `${VAR}` resolution loop, mints a fresh access token, and exports `MCP_<SLUG>_TOKEN`. The loop keeps anything already in the environment, so the live token wins over the stored, stale one.

The script is **sourced, never executed**: it can't abort the run, guards every command, and masks tokens with `::add-mask::`. A server whose refresh fails is simply left without a token.

### The trap: rotating refresh tokens

If a provider rotates the refresh token on each use, the old one dies immediately. Unless the replacement is **saved back**, the *next* run fails with `invalid_grant` - auth breaks one run later, not now.

Writing a secret needs a secrets-write credential, and **the default `GITHUB_TOKEN` cannot do it.** Add a fine-grained PAT with **Secrets: read/write** as **`GH_SECRETS_PAT`** (or repo-wide `GH_GLOBAL`).

**Every catalog provider rotates - treat the PAT as required, not optional.**

After adding the PAT, **re-connect the affected server once**. A refresh token already consumed by an earlier run can't be revived by the PAT alone.

Concurrent runs that each refresh the same rotating token still race. For many-server or high-parallelism setups, refresh centrally on a schedule so exactly one run mints and persists per interval.

### Reading the log

| Line | Means |
|---|---|
| `MCP enabled: glim, base` | servers wired for this run |
| `::debug::MCP OAuth: refreshed MCP_GLIM_TOKEN` | refresh worked (needs step debug logging) |
| `MCP OAuth: persisted rotated refresh token for …` | rotation saved - durable refresh active |
| `::warning::… uses a ROTATING refresh token but no secrets-write credential` | next run's auth **will** fail - add the PAT |
| `::warning::… refresh failed … (invalid_grant)` | already broken; re-connect in the dashboard |
| `::warning::.mcp.json references secret(s) not set: …` | see below |

### The harnesses differ on a missing secret

- **Claude:** one unresolved `${VAR}` skips **MCP entirely for that run** - every server, not just the broken one. `Skipping MCP this run.`
- **grok:** only the affected server fails to connect; the run and other servers continue.

So on the Claude harness a single stale token silently disables every MCP tool. If a skill reports "no MCP tools available," check the warning list before assuming its own server broke.

## Files

| Piece | File |
|---|---|
| Catalog (add featured servers here) + credential-name derivation | `apps/dashboard/lib/mcp-catalog.ts` |
| Access Keys **MCP** group (row descriptions) | `apps/dashboard/lib/secrets-catalog.ts` |
| Per-credential logos | `apps/dashboard/lib/service-icons.ts` |
| OAuth core - PKCE, discovery, DCR, exchange | `apps/dashboard/lib/mcp-oauth.ts` |
| Server glue - pending flow, browser, secrets | `apps/dashboard/lib/mcp-oauth-server.ts` |
| Start + callback routes | `apps/dashboard/app/api/mcp-auth/{route,callback/route}.ts` |
| Panel Connect button | `apps/dashboard/components/McpPanel.tsx` |
| Runtime refresh (both harnesses) | `scripts/mcp-oauth-refresh.sh` |
| CLI | `apps/cli/src/commands/mcp.ts` |
| Aeon-as-MCP-server | `apps/mcp-server/`, `bin/add-mcp` |
| Upstream docs | `docs/mcp-oauth.md` |

# CI gates in `aeonfun/aeon`

Eight `ci-*.yml` workflows. Every one is **path-filtered** and fires on `pull_request`, `push` to `main`, and `workflow_dispatch`.

**None of them can block a merge.** `main` has no branch protection and the repo has zero rulesets - `gh api repos/aeonfun/aeon/branches/main/protection` returns 404. A red X is advisory. Nothing stops a broken PR from merging, and nothing stops a push straight to `main` (where the same gates run, and fail *after* the fact). So the only thing that actually keeps these respected is running them locally before pushing. Treat the checklist below as the enforcement.

## The gates

| Workflow | Fires when you touch | Enforces | Run locally |
|---|---|---|---|
| `ci-skill-category` | `skills/**` | every `SKILL.md` has a valid `category:` | `bash scripts/check-skill-categories.sh` |
| `ci-skills-json` | `skills/**`, `bin/generate-skills-json`, `catalog/skills.json` | committed catalog == fresh regen | `bin/generate-skills-json` |
| `ci-packs-json` | `catalog/packs.config.json`, **`catalog/skills.json`**, `bin/generate-packs-json`, `catalog/packs.json` | pack catalog == fresh regen; every skill in exactly one pack | `bin/generate-packs-json` |
| `ci-tests` | `scripts/**`, `aeon.yml` | the 13 `scripts/tests/` suites + config validation | see below |
| `ci-capabilities-parity` | `bin/install-skill-pack`, `docs/CAPABILITIES.md` | capabilities taxonomy in sync across both | `bash scripts/check-capabilities-parity.sh` |
| `ci-skill-packs` | `catalog/skill-packs.json`, `.github/README.md`, `bin/install-skill-pack`, `skills/security/trusted-sources.txt` | community registry well-formed + matches README table; no unbacked `trust_level: trusted` | `node scripts/validate-skill-packs.mjs` |
| `ci-agents-md` | `STRATEGY.md`, `AGENTS.md`, `scripts/gen-agents-md.js` | `AGENTS.md` regenerated from `STRATEGY.md` | `node scripts/gen-agents-md.js --check` |
| `ci-apps` | `apps/**` | dashboard typecheck+test+build, cli typecheck, mcp-server build, webhook bundle | per app, see below |

There is **no security-scan CI gate.** The pack security scan lives in `bin/install-skill-pack` and runs at *install* time, not in CI.

## Checklist: adding or editing a skill

This is the common case (Modes 4 and 5), and it trips **three** gates, not one. Run all of it from the repo root before opening the PR:

```bash
bash scripts/check-skill-categories.sh    # category is valid
bin/generate-skills-json                  # refresh catalog/skills.json
bin/generate-packs-json                   # REQUIRED - see the trap below
node scripts/validate-config.js           # only if you touched aeon.yml
git add catalog/skills.json catalog/packs.json
```

**The trap: `bin/generate-skills-json` alone is not enough.** It rewrites `catalog/skills.json`, which is itself a *trigger path* for `ci-packs-json`. Commit the skills catalog without regenerating the pack catalog and the PR goes red on a workflow you never touched. Always run both generators, always commit both files.

Both files carry a `generated` UTC timestamp that changes on every run - that's expected. `ci-skills-json` and `ci-packs-json` normalize it out (plus per-skill `sha`/`updated`, which churn on every squash-merge), so a timestamp-only diff is not drift and won't fail. On a clean tree, regenerating both should produce exactly a one-line diff per file.

### `category:` - the valid set

`core evolution basics dev crypto productivity`. Anything else fails the gate. Category is the *only* thing deciding which pack a skill joins.

## `ci-tests` in full

Needs `pip install pyyaml==6.0.2` first. Thirteen steps:

```bash
python3 scripts/tests/test_notify_format.py
bash    scripts/tests/test_notify.sh
bash    scripts/tests/test_telegram_route.sh
bash    scripts/tests/test_skill_mode.sh
bash    scripts/tests/test_skill_requires.sh
bash    scripts/tests/test_run_actions_summary.sh
bash    scripts/tests/test_validate_pack.sh
bash    scripts/tests/test_validate_skill_packs.sh
bash    scripts/tests/test_run_grok.sh
python3 scripts/tests/test_state_reduce.py
python3 scripts/tests/test_health_triage.py
node --test scripts/validate-config.test.js
node    scripts/validate-config.js
bash    scripts/tests/test_cron_due.sh
```

Editing `aeon.yml` alone is enough to fire this workflow - `node scripts/validate-config.js` is the one to run after any hand-edit (Mode 4 step 4).

## `ci-apps` in full

One job per app so a red X names the broken surface.

```bash
cd apps/dashboard && npm ci && npm run typecheck && npm test && npm run build
cd apps/cli       && npm ci && npm run typecheck   # needs apps/dashboard deps installed first
cd apps/mcp-server && npm install && npm run build
cd apps/webhook   && node --check src/worker.js && npm install && npx wrangler deploy --dry-run --outdir /tmp/w
```

The dashboard runs **both** `typecheck` and `build` on purpose: a past Dependabot bump crashed `next build` while `tsc --noEmit` passed. Don't treat the typecheck as sufficient. The CLI cannot typecheck without the dashboard's `node_modules` - its tsconfig compiles `../dashboard/lib/**/*.ts` and borrows that app's typescript and `@types`. `mcp-server` and `webhook` commit no lockfile, so `npm ci` is unavailable there.

# How Aeon skills are actually written

Surveyed across all 82 skills in `aeonfun/aeon`. Frequencies are real counts - match the dominant convention unless there's a reason not to. Bodies run 133-757 lines (~306 median); a skill is a prompt, not a config file, and reads as prose.

## Frontmatter

Universal - **all 82 skills** carry these five:

```yaml
name: my-skill       # the slug (matches the skills/<slug>/ directory)
description: One line - what it does and what it sends.
metadata:
  title: My Skill    # human-readable display name
  category: basics   # core | evolution | basics | dev | crypto | productivity
  tags: [content]
```

Then, in descending real-world use:

| Field | Used by | Meaning |
|---|---|---|
| `var:` | 56 | the operator-tunable knob (topic, filter, mode). Default value; `./aeon skills set <name> --var` overrides at run time |
| `requires:` | 28 | API keys to inject. **This is an allowlist** - see the trap below |
| `mode:` | 17 | `read-only` (10) or `write` (7). **Absent = `write`** |
| `permissions:` | 12 | GitHub token scopes, e.g. `contents:write`, `pull-requests:write` |
| `commits:` | 12 | `true` (9) / `false` (3) - whether the run may commit |
| `capabilities:` | 10 | declared blast radius, e.g. `external_api`, `sends_notifications`. Taxonomy locked by `ci-capabilities-parity` |
| `mcp:` | 4 | MCP servers the skill needs - **catalog metadata only, gates nothing at run time** (`references/mcp.md`) |
| `depends_on:` | 3 | other skills, for chain ordering |

### Trap 1 - `requires:` injects only names that pass the filter

`scripts/skill_requires.sh` reads it with awk and injects only entries matching `^[A-Z][A-Z0-9_]{2,}$` (a trailing `?` marks "works better with"; bare means required). Both list forms parse - inline or block, top-level or nested under `metadata:` (the spec form):

```yaml
metadata:
  requires:
    - COINGECKO_API_KEY?
    - ALCHEMY_API_KEY?
```

This is **least-privilege secret injection**: the run exports only the keys listed here - a skill sees nothing else from the secret store. The trap is the *value*, not the list style - a lowercase, too-short, or otherwise malformed entry is silently dropped, so the skill declares a credential it never receives and fails at run time as if the key were never set.

### Trap 2 - a typo'd `mode:` silently grants write

`scripts/skill_mode.sh` maps an unknown value to `write` ("never silently over-restrict"). `mode: readonly` or `mode: read_only` does **not** get you `read-only` - it gets you full access. The exact string is `read-only`.

### Trap 3 - `schedule:` / `cron:` in frontmatter does nothing

10 skills carry one (`schedule: "0 14 * * *"`, `cron: "0 9,15 * * *"`). Nothing reads it. `.github/workflows/scheduler.yml` parses **`aeon.yml` only** (`done < aeon.yml`). Those lines are stale documentation. Never set a schedule by editing `SKILL.md`, and don't trust one you find there - check `aeon.yml`.

## Body structure

The dominant shape, by heading frequency:

| Heading | Skills | Purpose |
|---|---|---|
| `## Steps` | 40 | the numbered procedure - the core of the skill |
| `## Network note` | 39 | how to fetch: curl vs WebFetch vs `./secretcurl` vs `gh api` |
| `## Constraints` | 29 | judgment rules, what not to do |
| `## Log` | 14 | the exact `memory/logs/` shape to append |
| `## Environment Variables` | 11 | one line per key in `requires:`, saying what degrades without it |
| `## Why this skill exists` | 9 | intent, so later edits don't erode it |
| `## Exit taxonomy` | 6 | the named ways it can end (incl. silent exits) |

Open with the date/var line, close with notify + log:

```markdown
Today is ${today}. <the prompt - plain instructions, including judgment calls>

Report via `./notify` (use `./notify -f file.md` for anything multi-line).
Send nothing if there's nothing worth reporting.
Append what you did to `memory/logs/${today}.md` under a `### <skill-name>` heading.
```

### `${today}` and `${var}` are NOT template variables

There is no substitution step. The workflow never rewrites `SKILL.md` - it builds a prompt that says:

```
Today is 2026-07-21. Read and execute the skill defined in skills/<name>/SKILL.md
Use this variable (override the default in the skill file):
var=<value>
```

…and the model reads the file with its Read tool. So `${today}` works only because the date is in the surrounding prompt and the model resolves it in context. It's a **convention, not an engine** - inventing `${my_thing}` gets you a literal `${my_thing}` with nothing to bind it. (Other `${...}` tokens you'll see in skill bodies - `${total_runs}`, `${network}` - are placeholders inside *sample output blocks*, showing the model what to fill in. Same mechanism: prose, not templating.)

## Calling external scripts

**These do not exist in the repo.** The workflow copies them to the repo root before each run (`.github/workflows/aeon.yml:435-444`), which is why `ls` shows no `notify` but 61 skills call `./notify`. Don't "fix" the missing file, and don't expect them locally.

| Call | Skills | Notes |
|---|---|---|
| `./notify "msg"` / `./notify -f body.md` | 57 | `-f` for anything multi-line. Structured form: `--title`, `--severity {info,success,warn,critical}`, `--link`. Falls back to `.pending-notify/` when the sandbox blocks outbound curl |
| `WebFetch` | 41 | preferred fallback for a flaky public GET |
| `./secretcurl` | 28 | authenticated curl - **the only safe way to use a key** |
| `gh api` | 24 | handles GitHub auth internally; prefer over raw curl for repo metadata |

### `./secretcurl` and the `{ENV_NAME}` placeholder

Claude Code's Bash permission analyzer **blocks any command containing a secret expansion** (`$XAI_API_KEY`, `${XAI_API_KEY}`) because it can't statically prove safety. `./secretcurl` takes curl's arguments and substitutes `{ENV_NAME}` tokens *inside* the script, so the secret never reaches the agent's command line:

```bash
./secretcurl -s -X POST https://api.x.ai/v1/responses \
  -H 'Authorization: Bearer {XAI_API_KEY}' -d "$PAYLOAD"
```

Braces, not `$`. A skill that writes `-H "Authorization: Bearer $XAI_API_KEY"` will be blocked at run time, not at author time.

There is **no network sandbox** - plain `curl` works for unauthenticated GETs.

## Memory

`memory/` is the durable state that survives between runs. Four conventions, in order of how often skills touch them:

### `memory/logs/${today}.md` - the run log (65 of 82 skills)

Every skill appends what it did, under **one** heading that is exactly its slug:

```markdown
### <skill-name>
- Phase: plan | send | all
- Mode: execute | dry-run
- <what happened, one line per fact>
```

The `### <skill-name>` shape is load-bearing - the health/heartbeat loop parses it. Use one heading per run and put discriminators on lines beneath it rather than inventing `### <skill-name> (plan)`.

This is also the **dedup substrate**. The standard rule, and the one to add to any new skill: *read the last 3 days of `memory/logs/` and skip anything already reported.* Without it a daily skill re-reports the same item until it's muted.

### `memory/MEMORY.md` - the durable index (87 references)

Long-lived facts, not run history. Skills read it for context; the `memory-flush` skill promotes important log lines into it and prunes stale ones. Don't append per-run noise here - that's what `logs/` is for.

### Domain state files

Skills that track things across runs own a file: `memory/watched-repos.md`, `memory/products.md`, `memory/instances.json`, `memory/on-chain-watches`, `memory/pending-disclosures/`, `memory/issues/INDEX.md`. Read-modify-write the one your skill owns; don't invent a parallel store.

### Not for skills: `memory/cron-state.json`

Scheduler bookkeeping, written by `scripts/state_store.sh` (append-only via GitHub Issue comments, folded by `state_reduce.py`). **Zero skills call it directly** - it's infrastructure. Leave it alone.

# History mining - deep reference (Mode 8)

`scripts/mine-history.mjs` reads the operator's local Claude Code transcripts and
surfaces recurring work that could become a scheduled Aeon skill. This file is the
detail behind Mode 8: what the tool reads, how it ranks, and how to turn a digest
row into a real skill without proposing junk.

## What it reads

Claude Code writes one JSONL transcript per session under
`~/.claude/projects/<encoded-cwd>/<session-uuid>.jsonl`. Each line is a record;
the ones the miner uses:

| record `type` | field | used for |
|---|---|---|
| `ai-title` | `aiTitle` | the session's generated title - the semantic label for theme grouping (last one in a file wins = freshest) |
| `user` | `message.content` (string) | real human prompts - only plain strings without a `<system-reminder>`/`<command-name>` wrapper; tool-result echoes are lists and are skipped |
| `assistant` | `message.content[].tool_use` | `Bash` commands → normalised workflows; `mcp__*` names → MCP tool usage |
| any | `cwd`, `timestamp`, `sessionId` | project scoping, cadence (distinct days), dedup |

It only scans **top-level sessions** - files under a `subagents/` path are
sidechains (agent fan-out) and would double-count the parent's work, so they're
skipped. The scan window is bounded by file mtime (`--days`, default 120) so it
stays a few seconds even over thousands of transcripts.

## How it ranks

Everything is ranked by `distinct sessions × 1000 + distinct days × 10 + runs` -
so **breadth of recurrence dominates raw volume**. A command run 500 times in one
marathon session ranks below one run once each across 20 days: the second is a
habit with a cadence, the first is a one-off you happened to repeat. Days are the
cadence signal that tells you *daily* vs *weekly* when you get to `schedule:`.

`--min-sessions N` (default 2) drops anything seen in a single session - a true
one-off is never an automation candidate.

### Command normalisation

Each `Bash` command is split on `&&`, `|`, `;`, and loop keywords into segments;
each segment's first token becomes `binary subcommand` (for `node`/`python3` the
script basename is the "subcommand", since that's the recurring workflow). Two
denylists keep the signal clean:

- **`NOISE_BIN`** - file-poking and shell/JS keywords (`ls`, `cat`, `grep`,
  `printf`, `done`, `const`, …). Never a workflow.
- **`PLUMBING`** - universal git/gh navigation (`git status`, `git log`,
  `git diff`, `gh auth`, …). Present in nearly every coding session, so it tells
  you nothing about *what* to automate. Filtered from the command table.

What survives is the distinctive stuff: named scripts, specific CLIs, tight API
patterns. Note that `gh pr`, `gh api`, `npm run` survive the filter but are still
near-substrate - high in *every* repo. Treat them as weak on their own; they
matter only when a **title theme** explains *what* the PR/API work was for.

### Title grouping

Session titles are lowercased, stripped to their content words (stopwords
removed), truncated to the first six, and grouped. Near-identical titles collapse
("Synthesize activity logs into timeline cards" ≈ "Synthesizing user activity
logs…"), and the group is ranked by sessions then days. This is usually the
**most useful table** - the titles are already semantic, so a high-count group is
a plain-language description of a thing the operator keeps doing.

## From a digest row to a skill

A row is a candidate only if it clears all four gates:

1. **Recurring** - several sessions across several days. One busy day = not yet.
2. **Fetch / compute / report-shaped** - it pulls or checks something and reports
   a result. Read-heavy monitoring, digests, and status checks automate cleanly.
   Interactive debugging, decision-heavy review, and one-off migrations do not -
   they need a human in the loop that a cron run doesn't have.
3. **Unattended-safe** - no reliance on local files, a logged-in desktop app, or
   the operator answering a question mid-task. If the observed work used a local
   MCP server or read `~`, that part has to be re-wired as a repo secret /
   `.mcp.json` or dropped (Mode 4 steps 2-3).
4. **Not already covered.** Dedup against `./aeon skills ls` *before* proposing.
   Common overlaps to watch for:

   | Digest signal | Already a skill → do this instead |
   |---|---|
   | Heavy `gh pr` / PR review | `pr-review`, `pr-check` → Mode 2 reschedule |
   | Recurring topic research / "digest X" | `digest`, `article`, `mention-radar` → Mode 5 `--var` |
   | Repo / commit monitoring | `github-monitor`, `changelog` |
   | Shipping recap | `shiplog`, `heartbeat` |

   If an existing skill fits, the win is a **reschedule (Mode 2)** or a **`var`
   change (Mode 5)**, not a new skill. Only genuinely uncovered recurring work
   earns a new `SKILL.md`.

## Inferring the schedule

Read cadence from the `days` column of the winning row against the window:

- days ≈ window length (hit almost every active day) → **daily** (`0 13 * * *`).
- days ≈ window / 7 (a weekly rhythm) → **weekly** (`0 13 * * 1`).
- bursty / irregular → propose `workflow_dispatch` (on-demand) first; let the
  operator promote it to cron once it proves useful.

Always convert to UTC and confirm the next 3 fire times in their timezone
(Mode 2 rules), and remember the quoted-`schedule:` gotcha when the entry lands
(Mode 4 step 4).

## Privacy

Transcripts are the operator's own and can contain anything they've ever pasted
into Claude Code. The miner only emits **aggregates** - command patterns, grouped
titles, counts. Keep it that way: never surface a raw prompt body, and never write
transcript contents into a committed file or a notification. The counts and titles
carry all the signal needed to decide what to automate.

## Running it

From the instance repo root, on the operator's own machine:

```bash
# default: last 120 days, markdown digest
node .claude/skills/aeon/scripts/mine-history.mjs

# a tighter recent window, more rows
node .claude/skills/aeon/scripts/mine-history.mjs --days 45 --top 20

# scope to one repo/topic (matches the session's cwd)
node .claude/skills/aeon/scripts/mine-history.mjs --project my-repo

# machine-readable, to post-process
node .claude/skills/aeon/scripts/mine-history.mjs --json | jq '.titles'
```

Needs only Node (>=16) and a local `~/.claude/projects` - it exits with a clear
message anywhere that directory is absent (e.g. a CI checkout), and never writes
anything. If a busy background app dominates the tables (a tool that itself drives
Claude Code will pile up near-identical sessions), scope past it with `--project`.

### Flags

| flag | default | effect |
|---|---|---|
| `--days N` | 120 | only sessions whose transcript was modified in the last N days |
| `--top N` | 20 | rows per table |
| `--project SUBSTR` | - | only sessions whose cwd contains SUBSTR |
| `--min-sessions N` | 2 | drop candidates seen in fewer than N distinct sessions |
| `--json` | off | raw JSON instead of the markdown digest |

### Sample output (synthetic)

```
# Automation candidates - mined from Claude Code history

Scanned 240 sessions (240 files, last 45 days) across 38 active days.

## Recurring command workflows
| # | pattern      | runs | sessions | days | projects |
| 1 | `gh pr`      | 610  | 92       | 34   | 40       |
| 2 | `gh api`     | 240  | 55       | 30   | 28       |
| 3 | `npm run`    | 180  | 41       | 22   | 12       |

## Recurring task themes
| # | recurring session title  | sessions | days |
| 1 | Review open pull requests| 14       | 12   |
| 2 | Weekly analytics digest  | 6        | 6    |
| 3 | Audit repos for cleanup  | 4        | 4    |
```

Read that as: PR review is a near-daily habit (route to `pr-review`, don't
re-invent it); a weekly analytics digest recurs on a clean 7-day cadence and has
no covering skill (a real new-skill candidate → daily/weekly `mode: read-only`);
the repo audit is real but low-cadence (offer `workflow_dispatch` first).