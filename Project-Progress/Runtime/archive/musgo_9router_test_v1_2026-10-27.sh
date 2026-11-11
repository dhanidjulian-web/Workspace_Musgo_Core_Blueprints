#!/usr/bin/env bash
# =============================================================================
# 9router Control — MusGo-OS 2in1 | Layer 05: AI Provider
# © 2026 — Dhani Yuliawan | All Rights Reserved
#
# Catatan sandbox (proot):
#   - ps aux / ss TIDAK andal -> indikator sah adalah curl /api/health
#   - nohup & bisa dibunuh   -> gunakan background job persisten
# =============================================================================
set -uo pipefail

HOST="${NINE_HOST:-127.0.0.1}"
PORT="${NINE_PORT:-20128}"
CLI="/usr/local/lib/node_modules/9router/cli.js"
HEALTH="http://${HOST}:${PORT}/api/health"
MODELS="http://${HOST}:${PORT}/v1/models"
LOGFILE="${NINE_LOG:-/root/9router_run.log}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

ok()   { printf '  \033[32mOK\033[0m   %s\n' "$*"; }
bad()  { printf '  \033[31mFAIL\033[0m %s\n' "$*"; }

health() {
  local body
  body="$(curl -s -m 5 "$HEALTH" 2>/dev/null)"
  if [ -n "$body" ]; then echo "$body"; return 0; fi
  return 1
}

cmd_start() {
  if health >/dev/null; then ok "sudah berjalan ($HEALTH)"; return 0; fi
  [ -f "$CLI" ] || { bad "cli.js tidak ditemukan: $CLI"; return 1; }
  echo "  .. menjalankan 9router di ${HOST}:${PORT}"
  # --no-browser wajib ; --skip-update menghindari hang
  setsid node "$CLI" --no-browser --host "$HOST" --port "$PORT" --skip-update \
    >"$LOGFILE" 2>&1 < /dev/null &
  disown 2>/dev/null || true
  for _ in $(seq 1 20); do
    sleep 1
    if health >/dev/null; then ok "hidup: $(health)"; return 0; fi
  done
  bad "tidak merespons setelah 20s — cek $LOGFILE"
  return 1
}

cmd_stop() {
  pkill -f "9router/cli.js" 2>/dev/null && ok "dihentikan" || bad "tidak ada proses"
}

cmd_status() {
  echo "=== 9router status (${HOST}:${PORT}) ==="
  if h="$(health)"; then ok "health: $h"
  else bad "health: tidak merespons"; return 1; fi
  local n
  n="$(curl -s -m 8 "$MODELS" 2>/dev/null | python3 -c \
       'import sys,json;d=json.load(sys.stdin);print(len(d.get("data",[])))' 2>/dev/null)"
  [ -n "${n:-}" ] && ok "models terdaftar: $n" || bad "gagal baca /v1/models"
  [ -f "$LOGFILE" ] && echo "  log: $LOGFILE ($(wc -c <"$LOGFILE") byte)"
}

cmd_models() {
  curl -s -m 10 "$MODELS" | python3 -c '
import sys, json
d = json.load(sys.stdin); data = d.get("data", [])
prov = {}
for m in data:
    o = m.get("owned_by") or ""
    if o: prov[o] = prov.get(o, 0) + 1
print("models:", len(data), "| providers:", len(prov))
for k, v in sorted(prov.items(), key=lambda x: -x[1])[:15]:
    print(f"  {k:<20} {v}")
'
}

cmd_test() {
  echo "=== OFFLINE ==="
  ( cd "$HERE" && python3 tests/test_9router_offline.py ) || return 1
  echo; echo "=== LIVE ==="
  if health >/dev/null; then
    ( cd "$HERE" && python3 tests/test_9router_live.py )
  else
    bad "server mati — jalankan: $0 start"
  fi
}

case "${1:-status}" in
  start)   cmd_start   ;;
  stop)    cmd_stop    ;;
  restart) cmd_stop; sleep 2; cmd_start ;;
  status)  cmd_status  ;;
  models)  cmd_models  ;;
  test)    cmd_test    ;;
  health)  health ;;
  *) echo "pakai: $0 {start|stop|restart|status|models|test|health}"; exit 2 ;;
esac
