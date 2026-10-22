# MUSGO-OS 2in1 — PANDUAN ISI API KEY PROVIDER

> © 2026 — Dhani Yuliawan | All Rights Reserved
> Anti-Penipuan: key tidak pernah ditampilkan penuh, tidak pernah masuk chat/log.

---

## 📁 LOKASI FILE KREDENSIAL

```
/home/.musgo-router/providers/
├── agnesai.env            ← Agnes AI        (KOSONG)
├── anyapi.env             ← AnyAPI          (KOSONG)
├── cheaperinference.env   ← Cheaper Infer.  (KOSONG)
├── freetheai.env          ← FreeTheAI       (KOSONG)
├── kiloai.env             ← Kilo/OpenCode   (KOSONG)
└── nvidia.env             ← NVIDIA NIM      (KOSONG)

/home/.musgo-router/credential.env
└── KunciAi (default+fallback)               (KEY AKTIF ✅)
```

> Semua file mode `600` (hanya root/user yang bisa baca).
> Direktori mode `700`.

---

## ⚡ CARA PALING CEPAT — SATU BARIS

```sh
mr-key set <slug> <api-key>
```

**Contoh nyata:**
```sh
mr-key set nvidia         nvapi-xxxxxxxxxxxxxxxx
mr-key set freetheai      fta_xxxxxxxxxxxxxxxx
mr-key set anyapi         ak-xxxxxxxxxxxxxxxx
mr-key set kiloai         ks-xxxxxxxxxxxxxxxx
mr-key set agnesai        ag-xxxxxxxxxxxxxxxx
mr-key set cheaperinference ci-xxxxxxxxxxxxxx
```

> Key otomatis tersimpan mode 600. Tidak perlu editor. Tidak perlu restart.

---

## ✍️ CARA MANUAL (EDIT FILE)

```sh
mr-key show nvidia          # cetak template
# lalu edit file dengan editor terminal Anda, isi:
#   API_KEY="nvapi-xxxxxxxx"
mr-key path nvidia          # cetak lokasi file
```

---

## 🔁 MULTI-KEY (ROTASI OTOMATIS)

Bila Founder punya >1 key untuk satu provider, isi berurutan:

```sh
mr-key set nvidia nvapi-key-pertama
mr-key set nvidia nvapi-key-kedua      # otomatis masuk slot API_KEY_2
mr-key set nvidia nvapi-key-ketiga     # slot API_KEY_3
```

Router akan mencoba key#1, lalu #2 bila HTTP 401/403, dst. Maks 5 key.

---

## 🧾 STRUKTUR FILE

```env
BASE_URL="https://integrate.api.nvidia.com/v1"
API_KEY="nvapi-xxxxxxxx"
API_KEY_2="nvapi-yyyyyyyy"   # opsional
API_KEY_3="nvapi-zzzzzzzz"   # opsional
```

---

## ✅ CEK STATUS

```sh
mr-key list              # daftar semua provider + status ADA/KOSONG
mr- providers             # status provider + jumlah key
mr- provider test         # health-check + instant-test respon nyata
```

---

## 🗂️ DAFTAR SLUG RESMI

| Slug | Provider | Base URL |
|------|----------|----------|
| `kunciai` | KunciAi (default+fallback) | `https://kunciai.id/v1` |
| `kiloai` | Kilo/OpenCode | `https://api.kilo.ai/api/gateway` |
| `nvidia` | NVIDIA NIM | `https://integrate.api.nvidia.com/v1` |
| `anyapi` | AnyAPI | `https://api.anyapi.ai/v1` |
| `freetheai` | FreeTheAI | `https://api.freetheai.org/v1` |
| `agnesai` | Agnes AI | `https://apihub.agnes-ai.com/v1` |
| `cheaperinference` | Cheaper Inference | `https://api.cheaperinference.com/v1` |

---

## ⚠️ ATURAN KEAMANAN

1. **JANGAN** kirim isi file `.env` ke chat mana pun.
2. **JANGAN** commit ke git (`~/.musgo-router` di luar repo, aman).
3. KunciAi = **default + fallback**, hanya dipakai **manual** atau bila semua provider auto gagal.
4. Semua provider auto (`auto=yes`) ikut **auto-router**.
5. Dedup lintas-provider: model yang sama → dipilih tier termurah (free > freemium > paid).

---

## 🚀 ALUR LENGKAP

```sh
# 1. Isi key provider
mr-key set nvidia nvapi-xxx
mr-key set freetheai fta_xxx

# 2. Verifikasi
mr-key list
mr- provider test

# 3. Sync/index model
mr- sync

# 4. Pakai auto-route
mr- "tulis fungsi Python untuk sorting"
```

---

**FOUNDER SIGN: DHANI YULIAWAN**
