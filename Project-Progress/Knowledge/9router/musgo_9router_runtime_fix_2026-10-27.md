# KNOWLEDGE — Fix Runtime Harness 9router (MusGo-OS 2in1)
Diperbarui: 2026-10-27 | Commit: 67bc8ed | Founder: Dhani Yuliawan

## KONTEKS
Sesi sebelumnya melaporkan "anomali: skrip Runtime tampak jalan tapi ls tidak
menemukan". VERIFIKASI sesi ini: file ADA, md5 cocok dengan source repo.
Anomali itu artefak dua tool-call paralel — bukan file hilang.

NAMUN verifikasi lanjutan menemukan DUA BUG NYATA pada skrip tsb.

## BUG 1 — PATH TEST SALAH (fatal pada subcommand `test`)
Gejala:
  python3: can't open file
  '/root/projects/Project-Progress/tests/test_9router_offline.py':
  [Errno 2] No such file or directory

Sebab: skrip v1 memakai variabel HERE (dirname skrip) lalu `cd "$HERE"`,
sehingga mencari tests/ di dalam Project-Progress — padahal tests/ hanya
ada di modul repo.

Fix: gunakan MODULE_DIR absolut:
  MODULE_DIR="${MUSGO_9ROUTER_MODULE:-/root/Repository MusGo-OS_2in1-main/cognitive_domain/layer_05_agent_orchestration/ai_provider_9router}"
  ( cd "$MODULE_DIR" && python3 tests/test_9router_offline.py )

## BUG 2 — TIDAK EXECUTABLE
Gejala: perlu `bash <file>`, tidak bisa `./<file>`.
PENYELIDIKAN: `chmod 755` mengembalikan rc=0 TAPI permission TETAP 660.
SEBAB: filesystem Android/proot tidak menyimpan exec-bit pada mount ini.
STATUS: BATASAN PLATFORM, bukan bug skrip.
SOLUSI: SELALU panggil via `bash scripts/9router_ctl.sh ...`

## PENINGKATAN v2
- preflight check (modul + router_9router.py + test file harus ada)
- subcommand baru: info, preflight, health
- output berlabel PASS/FAIL/WARN/INFO (tidak ambigu)
- start: tunggu health hingga 25 detik, tail log bila gagal
- stop: verifikasi health benar-benar mati (bukan asumsi pkill)
- kompatibel dua lokasi via env MUSGO_9ROUTER_MODULE

## UJI TERBUKTI SETELAH FIX
preflight : PASS (modul, router, offline test ditemukan)
health    : PASS {"ok":true}
status    : PASS health ok + 861 model terdaftar
models    : PASS 861 model | 86 provider
offline   : 10 PASS / 0 FAIL
sync      : md5 skrip di repo == md5 di Project-Progress (81f4bdcd...)

## DAFTAR SUBCOMMAND v2
bash scripts/9router_ctl.sh {start|stop|restart|status|models|test|health|info|preflight}
exit code `test`: 0=sukses, 1=gagal, 2=server mati (live dilewati)

## GIT
commit 67bc8ed — "fix(layer_05): perbaiki path test pada 9router_ctl.sh
+ dokumentasi exec-bit"
push 174b567..67bc8ed main->main, ahead/behind 0/0
README: 166 baris (+ bagian 5b tentang exec-bit)

Founder Sig: DHANI YULIAWAN
