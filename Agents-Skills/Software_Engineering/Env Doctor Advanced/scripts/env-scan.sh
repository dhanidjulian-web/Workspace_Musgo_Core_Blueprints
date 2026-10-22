#!/usr/bin/env bash
# env-scan.sh — Quick environment variable gap analysis
# Usage: ./env-scan.sh <project-root>
# Outputs: env var references found in source code

set -euo pipefail

PROJECT_ROOT="${1:-.}"

if [ ! -d "$PROJECT_ROOT" ]; then
  echo "Error: '$PROJECT_ROOT' is not a directory" >&2
  exit 1
fi

echo "=== Environment Variable Scan ==="
echo "Project: $PROJECT_ROOT"
echo ""

# Count env files
echo "--- Environment Files ---"
for f in .env .env.local .env.development .env.production .env.example .env.sample; do
  if [ -f "$PROJECT_ROOT/$f" ]; then
    vars=$(grep -cE '^[A-Z_]+=' "$PROJECT_ROOT/$f" 2>/dev/null || echo 0)
    echo "  $f: $vars variables"
  fi
done
echo ""

# Find env var references in source code
echo "--- Env Var References in Source ---"
cd "$PROJECT_ROOT"

# Node.js: process.env.VAR_NAME
node_vars=$(grep -rEho 'process\.env\.[A-Za-z_][A-Za-z0-9_]*' --include='*.{js,ts,jsx,tsx,mjs,cjs}' . 2>/dev/null | sed 's/process\.env\.//' | sort -u || true)
if [ -n "$node_vars" ]; then
  echo "Node.js ($ echo "$node_vars" | wc -l | tr -d ' ' refs):"
  echo "$node_vars" | head -30
  echo ""
fi

# Python: os.environ['VAR'] or os.getenv('VAR')
python_vars=$(grep -rEho "os\.environ\[['\"][A-Za-z_][A-Za-z0-9_]*['\"]\]|os\.getenv\(['\"][A-Za-z_][A-Za-z0-9_]*['\"]" --include='*.py' . 2>/dev/null | grep -oE "[A-Za-z_][A-Za-z0-9_]*" | sort -u || true)
if [ -n "$python_vars" ]; then
  echo "Python ($ echo "$python_vars" | wc -l | tr -d ' ' refs):"
  echo "$python_vars" | head -30
  echo ""
fi

# Shell: $VAR_NAME or ${VAR_NAME}
shell_vars=$(grep -rEho '\$\{?[A-Z_][A-Za-z0-9_]*\}?' --include='*.{sh,bash,zsh,fish}' --include='Makefile' --include='*.yml' --include='*.yaml' . 2>/dev/null | sed 's/[\${}]//g' | sort -u || true)
if [ -n "$shell_vars" ]; then
  echo "Shell/CI ($ echo "$shell_vars" | wc -l | tr -d ' ' refs):"
  echo "$shell_vars" | head -30
  echo ""
fi

# Check for potential secrets
echo "--- Potential Secret Patterns ---"
secrets=$(grep -rEi '(api_key|secret|password|passwd|token|private_key|access_key)\s*=\s*[^\s]+' --include='.env*' . 2>/dev/null || true)
if [ -n "$secrets" ]; then
  echo "$secrets" | head -10
  echo "(... redacted for security)"
else
  echo "  No obvious secrets found in .env files"
fi

echo ""
echo "=== Scan Complete ==="
