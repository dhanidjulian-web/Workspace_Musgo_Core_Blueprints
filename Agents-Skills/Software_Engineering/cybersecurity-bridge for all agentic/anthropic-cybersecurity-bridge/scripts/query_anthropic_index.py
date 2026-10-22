#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query Anthropic-Cybersecurity-Skills via the generic bridge helper."
    )
    parser.add_argument("--query", required=True, help="Search terms for skill lookup.")
    parser.add_argument("--limit", type=int, default=8, help="Maximum results to print.")
    parser.add_argument(
        "--root",
        help="Optional explicit Anthropic-Cybersecurity-Skills root. Defaults to common paths.",
    )
    args = parser.parse_args()

    helper = Path("/home/roy/.codex/skills/cybersecurity-skill-bridge/scripts/query_index.py")
    if not helper.exists():
        raise SystemExit("cybersecurity-skill-bridge is not installed at the expected path.")

    cmd = [sys.executable, str(helper), "--query", args.query, "--limit", str(args.limit)]
    if args.root:
        cmd.extend(["--root", args.root])
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
