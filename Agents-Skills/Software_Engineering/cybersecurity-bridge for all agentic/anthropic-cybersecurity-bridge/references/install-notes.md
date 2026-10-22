# Install Notes

This wrapper expects a local checkout of `Anthropic-Cybersecurity-Skills`.

## Supported Discovery

It can resolve the repo from:

- `--root /path/to/Anthropic-Cybersecurity-Skills`
- `AGENTSKILLS_LIB_ROOT`
- `/tmp/Anthropic-Cybersecurity-Skills`
- `~/Anthropic-Cybersecurity-Skills`

## Recommended Setup

```bash
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git ~/Anthropic-Cybersecurity-Skills
export AGENTSKILLS_LIB_ROOT=~/Anthropic-Cybersecurity-Skills
```

Then use:

```bash
python3 scripts/query_anthropic_index.py --query "memory dump credential theft"
```

## Boundary

Keep this wrapper separate from the external repo itself. Do not bundle third-party skill bodies or license files into this wrapper package.
