#!/usr/bin/env bash
# =============================================================================
# MusGo-OS 2in1 — 9router Test & Control (Runtime harness)
# Founder   : Dhani Yuliawan | © 2026 All Rights Reserved
# Versi     : 2.0.0  (2026-10-27)
#
# PERBAIKAN v2 vs v1:
#   1. Menunjuk MODULE_DIR absolut ke clone repo (v1 salah pakai HERE/tests
#      sehingga subcommand `test` gagal: "can't open .../Project-Progress/tests")
#   2. Chmod +x (v1 tidak executable)
#   3. Preflight check: repo & modul harus ada sebelum aksi apa pun
#   4. Semua output berlabel PASS/FAIL/WARN agar tidak ambigu
#
# CATATAN SANDBOX (proot) — TERBUKTI:
#   - `nohup ... &` DIBUNUH setelah tool call selesai
#   - `ps aux` / `ss -tln` TIDAK ANDAL (bisa 0 padahal server hidup)
#   - INDIKATOR SAH HANYA: curl /api/health
#   - Flag --no-browser WAJIB (tanpa ini CLI hang, exit 124)
# =============================================================================
set -uo pipefail

# --- Path kanonik (bisa di-override via env) ---------------------------------
MODULE_DIR="${MUSGO_9ROUTER_MODULE:-/root/Repository MusGo-OS_2in1-main/cognitive_domain/layer_05_agent_orchestration/ai_provider_9router}"
HOST="${NINE_HOST:-127.0.0.1}"
PORT="${NINE_PORT:-20128}"
CLI="/usr/local/lib/node_modules/9router/cli.js"
HEALTH_URL="http://${HOST}:${PORT}/api/health"
MODELS_URL="http://${HOST}:${PORT}/v1/models"
LOGFILE="${NINE_LOG:-/root/9router_run.log}"

# --- Warna -------------------------------------------------------------------
if [ -t 1 ]; then
  G=$'\033[32m'; R=$'\033[31m'; Y=$'\033[33m'; B=$'\033[36m'; N=$'\033[0m'
else
  G=''; R=''; Y=''; B=''; N=''
fi

pass() { printf '  %sPASS%s  %s\n' "$G" "$N" "$*"; }
fail() { printf '  %sFAIL%s  %s\n' "$R" "$N" "$*"; }
warn() { printf '  %sWARN%s  %s\n' "$Y" "$N" "$*"; }
info() { printf '  %sINFO%s  %s\n' "$B" "$N" "$*"; }
hdr()  { printf '\n=== %s ===\n' "$*"; }

# --- Preflight ---------------------------------------------------------------
preflight() {
  local rc=0
  if [ -d "$MODULE_DIR" ]; then pass "modul ada: ${MODULE_DIR##*/}"
  else fail "modul TIDAK ADA: $MODULE_DIR"; rc=1; fi
  if [ -f "$MODULE_DIR/router_9router.py" ]; then pass "router_9router.py ditemukan"
  else fail "router_9router.py hilang"; rc=1; fi
  if [ -f "$MODULE_DIR/tests/test_9router_offline.py" ]; then pass "offline test ditemukan"
  else fail "offline test hilang"; rc=1; fi
  return $rc
}

# --- Health probe (satu-satunya indikator sah) -------------------------------
probe_health() {
  local body
  body="$(curl -s -m 5 "$HEALTH_URL" 2>/dev/null)"
  [ -n "$body" ] || return 1
  printf '%s' "$body"
}

is_up() { probe_health >/dev/null 2>&1; }

# --- Perintah -----------------------------------------------------------------
cmd_health() {
  hdr "health probe"
  if body="$(probe_health)"; then
    pass "endpoint: $HEALTH_URL"
    info "response: $body"
    return 0
  fi
  fail "tidak merespons: $HEALTH_URL"
  info "jalankan: $0 start"
  return 1
}

cmd_start() {
  hdr "start 9router"
  if is_up; then pass "sudah berjalan"; cmd_status; return 0; fi
  [ -f "$CLI" ] || { fail "cli.js tidak ditemukan: $CLI"; return 1; }
  info "menjalankan di ${HOST}:${PORT}"
  setsid node "$CLI" --no-browser --host "$HOST" --port "$PORT" --skip-update \
    >"$LOGFILE" 2>&1 </dev/null &
  disown 2>/dev/null || true
  local i
  for i in $(seq 1 25); do
    sleep 1
    if is_up; then pass "hidup setelah ${i}s"; cmd_status; return 0; fi
  done
  fail "tidak merespons setelah 25s"
  [ -f "$LOGFILE" ] && { info "log terakhir:"; tail -10 "$LOGFILE"; }
  return 1
}

cmd_stop() {
  hdr "stop 9router"
  if pkill -f "9router/cli.js" 2>/dev/null; then pass "proses dihentikan"
  else warn "tidak ada proses yang cocok (mungkin memang sudah mati)"; fi
  sleep 1
  if is_up; then warn "masih merespons — cek manual"
  else pass "health: sudah mati (sesuai harapan)"; fi
}

cmd_status() {
  hdr "status 9router (${HOST}:${PORT})"
  if body="$(probe_health)"; then pass "health: $body"
  else fail "health: tidak merespons"; return 1; fi

  local n
  n="$(curl -s -m 10 "$MODELS_URL" 2>/dev/null | python3 -c \
      'import sys,json
try:
    d=json.load(sys.stdin); print(len(d.get("data",[])))
except Exception: print("")' 2>/dev/null)"
  if [ -n "${n:-}" ]; then pass "models terdaftar: $n"
  else fail "gagal baca /v1/models"; fi
  [ -f "$LOGFILE" ] && info "log: $LOGFILE ($(wc -c <"$LOGFILE" 2>/dev/null) byte)"
  info "modul: $MODULE_DIR"
}

cmd_models() {
  hdr "daftar model per provider"
  curl -s -m 12 "$MODELS_URL" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception as e:
    print("  FAIL  JSON tidak valid:", e); sys.exit(1)
data = d.get("data", [])
prov = {}
for m in data:
    o = m.get("owned_by") or ""
    if o: prov[o] = prov.get(o, 0) + 1
print("  total model :", len(data))
print("  total provider:", len(prov))
print("  --- 15 provider teratas ---")
for k, v in sorted(prov.items(), key=lambda x: -x[1])[:15]:
    print("   %-22s %d" % (k, v))
'
}

cmd_test() {
  hdr "test suite"
  preflight || { fail "preflight gagal — batal"; return 1; }

  printf '\n--- OFFLINE (tanpa jaringan) ---\n'
  if ( cd "$MODULE_DIR" && python3 tests/test_9router_offline.py ); then
    pass "offline suite selesai"
  else
    fail "offline suite GAGAL"; return 1
  fi

  printf '\n--- LIVE (butuh server hidup) ---\n'
  if is_up; then
    if ( cd "$MODULE_DIR" && python3 tests/test_9router_live.py ); then
      pass "live suite selesai"
    else
      fail "live suite GAGAL"; return 1
    fi
  else
    warn "server mati — live suite dilewati"
    info "jalankan dulu: $0 start"
    return 2
  fi
}

cmd_info() {
  hdr "informasi lingkungan"
  info "modul      : $MODULE_DIR"
  info "host:port  : ${HOST}:${PORT}"
  info "health url : $HEALTH_URL"
  info "models url : $MODELS_URL"
  info "cli.js     : $CLI $([ -f "$CLI" ] && echo '(ada)' || echo '(TIDAK ADA)')"
  info "node       : $(node -v 2>/dev/null || echo 'tidak terpasang')"
  info "log        : $LOGFILE"
  if [ -d "$MODULE_DIR" ]; then
    printf '  %sINFO%s  isi modul:\n' "$B" "$N"
    ( cd "$MODULE_DIR" && find . -type f -not -path "*__pycache__*" | sort | sed 's/^/          /' )
  fi
}

# --- Dispatch ----------------------------------------------------------------
case "${1:-status}" in
  start)   cmd_start   ;;
  stop)    cmd_stop    ;;
  restart) cmd_stop; sleep 2; cmd_start ;;
  status)  cmd_status  ;;
  models)  cmd_models  ;;
  test)    cmd_test    ;;
  health)  cmd_health  ;;
  info)    cmd_info    ;;
  preflight) hdr "preflight"; preflight ;;
  *) echo "pakai: $0 {start|stop|restart|status|models|test|health|info|preflight}"; exit 2 ;;
esac
