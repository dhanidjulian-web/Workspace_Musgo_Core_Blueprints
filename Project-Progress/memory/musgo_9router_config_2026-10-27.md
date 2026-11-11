# MEMORY — Config 9router untuk MusGo-OS 2in1
Tanggal: 2026-10-27 | Founder: Dhani Yuliawan

## AMANAT FOUNDER (KOREKSI PENTING)
"harusnya kerjakan di path clone repo: /root/Repository MusGo-OS_2in1-main
 setelah itu baru commit dan push ke github"

=> ALUR BAKU: EDIT DI CLONE LOKAL -> COMMIT LOKAL -> PUSH.
   BUKAN langsung push. BUKAN kerja di /root/projects.

## KOREKSI LAPORAN SAYA SENDIRI
Sesi sebelumnya saya klaim "belum di-commit / belum di-push". ITU SALAH.
Verifikasi sesi ini membuktikan config sudah ter-commit di f60f297 (sesi lalu).

## HASIL KERJA SESI INI (semua di clone lokal)
Commit 174b567 (PUSHED, dc451fe..174b567):
  1. README.md          (153 baris) — arsitektur, kelas/fungsi, routing, panduan start
  2. scripts/9router_ctl.sh (executable) — start|stop|restart|status|models|test|health

Push: git@github.com:dhanidjulian-web/MusGo-OS_2in1.git (SSH, tanpa PAT)
Verifikasi: ahead/behind 0/0, HEAD=origin/main=174b567

## HASIL UJI NYATA SESI INI
- Offline test: 10 PASS / 0 FAIL
- Live test: 4/4 PASS
- Health: http=200 {"ok":true}
- Models: 861 total | 86 provider
- Allowlist filter: 69 model lolos
- Routing resolve -> deepseek/deepseek-chat
- Fail-closed: chat tanpa API key -> NineRouterError terkontrol (bukan crash)

## PITFALL PROOT (TERBUKTI ULANG SESI INI)
1. `nohup ... &` GAGAL — proses dibunuh setelah tool call selesai.
2. `ss -tln | grep 20128` -> "NO_PORT" padahal server HIDUP.
3. `ps aux | grep 9router` -> count 0 padahal server HIDUP.
=> INDIKATOR SAH HANYA: curl -s http://127.0.0.1:20128/api/health

## START COMMAND TERBUKTI
node /usr/local/lib/node_modules/9router/cli.js \
  --no-browser --host 127.0.0.1 --port 20128 --skip-update
(wajib background job persisten; --no-browser WAJIB)

## FILE NYASAR (temuan, TIDAK dihapus — aturan addition-only)
/root/projects/Project-Progress/Runtime/scripts/musgo_config.py  (310 baris, 11051 B)
/root/projects/Project-Progress/config/scripts/musgo_config.py   (identik, md5 sama)
Isi: loader config Project-Progress (paths, founder_rules, write-policy zero-trust).
BUKAN bagian modul 9router. Dibiarkan, menunggu keputusan Founder.

Founder Sig: DHANI YULIAWAN

## TAMBAHAN — PEMBERSIHAN /root (2026-10-27)
Commit 19c0a8c (PUSHED, 67bc8ed..19c0a8c)

PERINTAH: bersihkan/pindahkan hasil 9router di /root ke clone repo.

DIPINDAH -> runtime_artifacts/ (1.1 MB, 8 file):
  logs/apt.log (133K), npm.log, ver.log, ver2.log, 9r.log, 9router_run.log
  catalog/model-catalog.json (318K), model-catalog-raw.json (622K)
Dihapus dari /root SETELAH: (a) cmp identik, (b) push terverifikasi di remote.

TETAP di /root: .9router/ (20M) — TIGA ALASAN:
  1. masih aktif dipakai server yang berjalan
  2. berisi jwt-secret + auth/cli-secret (DILARANG masuk repo)
  3. runtime/node_modules ~19MB = dependensi runtime

KEAMANAN: secret scan CLEAN; .gitignore diperkuat (.9router/, **/jwt-secret,
**/cli-secret, **/auth/cli-secret, **/runtime/node_modules/).
Server setelah pembersihan: http=200 {"ok":true} — TIDAK terganggu.

PELAJARAN: verifikasi cmp + push SEBELUM rm. Jangan hapus sumber dulu.

Founder Sig: DHANI YULIAWAN

## TAMBAHAN — FIX RUNTIME HARNESS (2026-10-27)
Commit 67bc8ed (PUSHED, 174b567..67bc8ed)

ANOMALI SESI LALU: "skrip Runtime tidak ditemukan ls"
=> FALSE ALARM. File ADA, md5 cocok. Artefak dua tool-call paralel.
=> PELAJARAN: jangan tulis ulang sebelum verifikasi ulang perintah tunggal.

2 BUG NYATA ditemukan:
1. BUG PATH (fatal): subcommand `test` memakai HERE bukan MODULE_DIR,
   sehingga mencari tests/ di Project-Progress -> file not found.
   FIX: MODULE_DIR absolut + cd "$MODULE_DIR".
2. BUG EXEC-BIT: chmod 755 rc=0 TAPI mode tetap 660.
   SEBAB: filesystem Android/proot tidak menyimpan exec bit.
   STATUS: batasan platform, tidak bisa diperbaiki. SELALU pakai `bash <script>`.

PENINGKATAN v2: preflight, info, health, output PASS/FAIL, start tunggu 25s.
UJI: preflight PASS, health {"ok":true}, status 861 model, offline 10/10 PASS.

VERIFIKASI LISTING (2026-10-27 lanjutan): semua file progress TERBUKTI ADA
(memory 3116 B, Knowledge 1976/2445/3322 B, .state 3 JSON valid, Runtime 6689 B).

Founder Sig: DHANI YULIAWAN
