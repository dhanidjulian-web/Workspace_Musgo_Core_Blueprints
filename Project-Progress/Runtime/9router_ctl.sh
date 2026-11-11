#!/bin/bash
# 9router control script — MusGo-OS 2in1
# Diverifikasi bekerja di sandbox proot Android (2026-10-26)
# Usage: ./9router_ctl.sh start|stop|status|models|version

export TMPDIR=/root/tmp
CLI=/usr/local/lib/node_modules/9router/cli.js
PORT=20128
HOST=127.0.0.1
LOG=/root/projects/Project-Progress/Runtime/9router_server.log

case "$1" in
  start)
    if curl -s -m 2 "http://$HOST:$PORT/api/health" >/dev/null 2>&1; then
      echo "9router sudah berjalan di $HOST:$PORT"; exit 0
    fi
    nohup node "$CLI" --no-browser --host "$HOST" --port "$PORT" --skip-update > "$LOG" 2>&1 &
    echo "started pid=$! (log: $LOG)"
    sleep 10
    curl -s -m 5 "http://$HOST:$PORT/api/health" && echo "" || echo "GAGAL start — cek $LOG"
    ;;
  stop)
    pkill -f "9router/cli.js" && echo "stopped" || echo "tidak ada proses"
    ;;
  status)
    echo "--- process ---"; ps aux 2>/dev/null | grep "[9]router/cli.js" | head -3
    echo "--- health ---"
    curl -s -m 5 "http://$HOST:$PORT/api/health" || echo "DOWN"
    echo ""
    ;;
  models)
    curl -s -m 10 "http://$HOST:$PORT/v1/models" -o /root/models.json && \
    node -e "const d=require('/root/models.json').data;console.log('models:',d.length,'| providers:',new Set(d.map(m=>m.owned_by)).size)"
    ;;
  version)
    node "$CLI" --version
    ;;
  *)
    echo "Usage: $0 {start|stop|status|models|version}"
    ;;
esac
