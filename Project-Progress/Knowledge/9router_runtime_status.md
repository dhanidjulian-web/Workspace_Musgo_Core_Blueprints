# KNOWLEDGE — 9router Runtime Status (Sandbox Kai)

- Terakhir diverifikasi: 2026-10-26 22:2x WIB
- Verifikasi ulang wajib: setiap sesi baru (server bisa mati saat sandbox reboot)

---

## STATUS RINGKAS

| Komponen | Nilai | Status |
|---|---|---|
| 9router versi | 0.5.111 | AKTIF |
| Node.js | v18.20.4 | MEMENUHI (>=18) |
| npm | 9.2.0 | OK |
| Binary | /usr/local/bin/9router → ../lib/node_modules/9router/cli.js | ADA |
| Paket | /usr/local/lib/node_modules/9router | 77 MB |
| Runtime home | /root/.9router | 20 MB |
| Port | 20128 (default) | LISTEN |
| Host binding | 127.0.0.1 (dipaksa via --host) | LOCAL ONLY |
| Health | GET /api/health → {"ok":true} | SEHAT |
| Model registry | GET /v1/models → 861 model | OK |
| Provider | 86 provider | OK |

## ENDPOINT PENTING

| Endpoint | Fungsi | Terverifikasi |
|---|---|---|
| GET / | redirect 307 → /dashboard | ya |
| GET /login | halaman login (9Router - AI Infrastructure Management) | ya |
| GET /api/health | health probe | ya → {"ok":true} |
| GET /v1/models | daftar model OpenAI-compatible | ya → 861 |
| POST /v1/chat/completions | chat completion | ya → HTTP 500 tanpa API key |
| /v1/responses, /api/v1, /api/v1beta, /api/v1/systemone | route internal app/server.js | terdaftar |

## FILE STATE (~/.9router)

```
/root/.9router/
├── db/                 # database (sqlite) — dibuat otomatis saat start
├── jwt-secret          # 64 byte, auth dashboard
└── runtime/
    ├── node_modules/sql.js   # 19 MB (dibutuhkan cli.js)
    ├── package.json          # name: 9router-runtime
    └── package-lock.json
```

## PERINTAH OPERASIONAL (copy-paste, terbukti jalan)

### START (persisten)
Jalankan via execute_shell_command dengan background=true:
```
export TMPDIR=/root/tmp && cd /root && node /usr/local/lib/node_modules/9router/cli.js --no-browser --host 127.0.0.1 --port 20128 --skip-update
```

### VERIFY
```
curl -s -m 5 http://127.0.0.1:20128/api/health
curl -s -m 5 http://127.0.0.1:20128/v1/models -o /root/models.json
node -e "const d=require('/root/models.json').data;console.log('models:',d.length,'providers:',new Set(d.map(m=>m.owned_by)).size)"
```

### STOP
```
pkill -f "9router/cli.js" || true
```

### VERSION (cepat, tidak hang)
```
node /usr/local/lib/node_modules/9router/cli.js --version
```

## JEBATAN (PITFALL) — JANGAN DIULANG

1. JANGAN pakai `npm install -g 9router` di sandbox proot.
   → selalu crash `Exit handler never called!` (rename ENOENT).
   → jika perlu reinstall: `npm pack` + `tar -xzf` manual.

2. JANGAN jalankan `9router` tanpa `--no-browser`.
   → CLI membuka browser, tanpa PTY = hang selamanya (exit 124).

3. JANGAN jalankan `9router --help`.
   → hang karena update-check jaringan. Pakai `--version` saja untuk probe.

4. JANGAN pakai `nohup ... &` di execute_shell_command biasa.
   → proses dibunuh saat call selesai. WAJIB background=true.

5. JANGAN percaya exit code npm di proot.
   → verifikasi dengan `du -sh` dan `ls` pada direktori target.

## RELEVANSI UNTUK MUSGO-OS 2in1

9router menyediakan **OpenAI-compatible gateway** ke 861 model dari 86 provider
dalam satu endpoint lokal (`http://127.0.0.1:20128/v1`).

Ini kandidat kuat untuk **AI Orchestration Layer** MusGo-OS:
- satu API key internal untuk semua provider
- routing/fallback antar model
- biaya & rate-limit terpusat
- mendukung tools, vision, reasoning, search per model (terekspos di /v1/models capabilities)

Langkah integrasi berikutnya (belum dikerjakan):
1. Buat API key di dashboard 9router (/login → settings).
2. Daftarkan endpoint 9router sebagai provider di konfigurasi agent MusGo-OS.
3. Definisikan policy routing: task ringan → model murah; reasoning berat → model besar.
