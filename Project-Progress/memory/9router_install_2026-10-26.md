# MEMORY — Instalasi 9router di Sandbox Kai (Android/proot)

- Tanggal: 2026-10-26 (WIB)
- Pelaku: Auto-Agent (Primary Orchestrator MusGo-OS 2in1)
- Permintaan Founder: "baca https://9router.com/#get-started — Install di local sandbox app kai ini"
- Status akhir: BERHASIL, server berjalan di background job persisten (session bg-1)

---

## 1. LINGKUNGAN SANDBOX (terverifikasi)
- Arsitektur: armhf / armv8l (ARM 32-bit)
- OS: Debian 12 (proot, Android)
- Node.js: v18.20.4 (dipasang via apt)
- npm: 9.2.0
- Batas tool: default 30s, maks 60s per perintah
- PEP 668 / venv gagal (symlink diblokir proot) — tidak relevan untuk Node

## 2. KRONOLOGI KEGAGALAN → SOLUSI

### Gagal #1 — npm install -g 9router
Error: `npm error Exit handler never called!`
Error pendamping: `ENOENT: no such file or directory, rename .../_cacache/tmp/...`
Root cause: proot memblokir/gagalkan operasi rename() lintas mount.
Dampak: npm exit code error, NAMUN paket tetap terektraksi lengkap
       77 MB di /usr/local/lib/node_modules/9router.
Pelajaran: jangan percaya exit code npm di proot — verifikasi isi disk.

### Gagal #2 — postinstall ~/.9router/runtime
Penyebab: `hooks/postinstall.js` memanggil ensureSqliteRuntime()
         → npm install sql.js ke ~/.9router/runtime
Hasil nyata: ternyata BERHASIL SEBAGIAN — sql.js 19 MB sudah lengkap.
Catatan: postinstall bersifat non-fatal (cli.js self-heals di runtime).

### Gagal #3 — CLI hang, exit 124 (timeout, tanpa output)
Diagnosa: `9router --version` dan `--help` hang.
Benar: `--version` normal jika dieksekusi langsung via node cli.js.
Penyebab hang server: CLI otomatis membuka browser (tanpa PTY → hang).
Solusi: flag `--no-browser`.
Tambahan: `--help` tetap hang karena update-check jaringan → dilewati saja.

### Gagal #4 — server mati setelah tool call selesai
Penyebab: proses anak dari execute_shell_command dibunuh saat call berakhir,
          meski sudah pakai nohup &.
Solusi: jalankan dengan execute_shell_command background=true → session persisten (bg-1).

## 3. KONFIGURASI YANG BERHASIL

### Start command (FINAL, terbukti)
```
export TMPDIR=/root/tmp
cd /root
node /usr/local/lib/node_modules/9router/cli.js --no-browser --host 127.0.0.1 --port 20128 --skip-update
```
Dijalankan dengan background=true agar persisten.

### Flag CLI yang tersedia (hasil grep cli.js)
--help, --host, --port, --no-browser, --skip-update, --tray,
--log, --output, --prompt, --url, --version, --dns-result-order
(mayoritas diteruskan ke Node via NODE_OPTIONS)

### Port
- DEFAULT_PORT = 20128
- PORT_ATTEMPTS = 10 (mencoba port berikutnya bila bentrok)

## 4. HASIL VERIFIKASI (bukti nyata, bukan asumsi)
| Item | Hasil |
|---|---|
| `node -v` | v18.20.4 |
| `cli.js --version` | 0.5.111 |
| port 20128 | OPEN (net.connect sukses) |
| GET / | HTTP 307 → location: /dashboard |
| GET / (follow) | HTTP 200, redirect final /login, 9936 byte |
| GET /api/health | `{"ok":true}` |
| GET /v1/models | 861 model, 86 provider |
| POST /v1/chat/completions (tanpa key) | HTTP 500 (butuh API key — normal) |
| Title login page | "9Router - AI Infrastructure Management" |
| Ukuran paket | 77 MB (/usr/local/lib/node_modules/9router) |
| Ukuran runtime | 20 MB (/root/.9router, termasuk sql.js 19 MB) |
| Isi ~/.9router | db/, jwt-secret (64 byte), runtime/ |

## 5. PROVIDER TERATAS (dari /v1/models)
alicode-intl, alicode, anthropic, ag, blackbox, byteplus, cerebras, cc, cl,
clinepass, cloudflare-ai, cbcn, cx, cohere, commandcode, cu, deepseek,
featherless, fireworks, gc, gemini, gh, glm-cn, glm, gcli, groq, hyperbolic,
if, kc, kimchi, ... (total 86 provider)

## 6. CATATAN OPERASIONAL
- Proses TIDAK auto-restart bila sandbox reboot. systemd tidak tersedia di proot.
  Opsi: nohup + cron @reboot, atau pindah ke VPS produksi x86_64.
- Sandbox armhf = performa terbatas; tidak disarankan untuk beban produksi.
- Semua operasi file = ADDITION ONLY (aturan Founder: no delete).
