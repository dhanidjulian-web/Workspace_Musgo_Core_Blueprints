# 9ROUTER SUPERVISOR + UNTRACK RUNTIME LOGS — SELESAI
Tanggal: 2026-10-30 | Commit: 6b2af4e (83167d1..6b2af4e main->main)

## VERIFIKASI PUSH
HEAD == origin/main == 6b2af4ee1feea8fc5686e5a9019d60378a652f96 ✅
ahead/behind 0/0 | porcelain 0 baris ✅

## ITEM 1 — UNTRACK RUNTIME ARTIFACTS
- 7 file di-untrack: 6 log (9r, 9router_run, apt, npm, ver, ver2) + model-catalog-raw.json (608K)
- model-catalog.json (312K, DIPAKAI runtime) TETAP tracked ✅
- File TETAP ADA di disk (patuh no_delete_files_rule) — terbukti ls -1 = 6 log
- .gitignore tambah: **/runtime_artifacts/logs/ dan **/runtime_artifacts/catalog/model-catalog-raw.json
- Remote: git ls-tree origin/main | grep runtime_artifacts/logs = 0 ✅

## ITEM 3 — SUPERVISOR AUTOSTART (proot tanpa systemd)
Script: cognitive_domain/layer_05_agent_orchestration/ai_provider_9router/scripts/9router_supervisor.sh
Fitur: health-probe nyata /api/health, backoff eksponensial maks 60s,
       mode --once untuk CI/test, deteksi proses mati (fail-closed).

### DUA PELAJARAN KRITIS (terbukti lewat kegagalan nyata)
1. nohup & TIDAK CUKUP — proses anak ikut dibunuh saat shell induk selesai.
   FIX: setsid (detach penuh dari sesi shell induk).
2. Warm-up 9router LAMBAT ~28 DETIK di sandbox ini.
   Probe lama 20x0.5s = 10s -> SELALU FAILED padahal proses hidup.
   FIX: 45x1s = 45s. Terbukti: "healthy setelah 28s", STARTED_HEALTHY exit 0.

### BUKTI SUKSES
- Kondisi awal: MATI (curl gagal, proses 0)
- Jalankan supervisor --once -> STARTED_HEALTHY, EXIT=0
- Pasca: curl /api/health -> {"ok":true} ✅
- PID 24734 node cli.js hidup

## CATATAN ENVIRONMENT (jangan diulang)
- systemd PID1 KOSONG, crontab & cron daemon TIDAK ADA -> supervisor loop manual
- systemctl ada tapi tidak fungsional (tanpa init)
- pkill -f "9router/cli.js" untuk matikan; tunggu ~4s sebelum uji ulang

## FILE TERSIMPAN
Knowledge/9ROUTER_SUPERVISOR_2026-10-30.md
.state/state_9router_supervisor_2026-10-30.json
