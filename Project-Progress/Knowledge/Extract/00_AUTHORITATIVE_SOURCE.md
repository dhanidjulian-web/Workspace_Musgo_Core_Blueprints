# ⚠️ SUMBER OTORITATIF

**Tanggal berlaku: 2026-10-29 · Engine v6 · Status VERIFIED_CONSISTENT**

## File yang WAJIB dipakai sebagai acuan angka:

| File | Peran |
|---|---|
| `03_module_mapping.csv` | **SUMBER TUNGGAL** — 776 verdict, dipetakan 1:1 ke `integrated` |
| `05_GAP_REPORT.md` | laporan final (regenerate dari CSV) |
| `summary.json` | ringkasan terverifikasi |

## Angka resmi berlaku:
- Batas BAWAH = 553/776 = **71,3%**
- Batas ATAS  = 634/776 = **81,7%**
- GAP SEJATI  =  97/776 = **12,5%**
- Perlu tinjau  =  45/776 =  **5,8%**

## ⚠️ FILE LAMA — JANGAN DIPAKAI UNTUK ANGKA
File berikut memuat angka **BASI (v5)** dan hanya bernilai historis.
TIDAK DIHAPUS sesuai aturan Founder (addition-only):

| File | Angka basi |
|---|---|
| `Project-Progress/memory/extract_engine_2026-10-28.md` | relocated 238, consolidated 76, name_dup 38 |
| `Project-Progress/.state/state_extract_engine_2026-10-28.json` | relocated 238 |
| `scripts/extract_audit_v5_backup.py` | parser v5 |

Bila ada perbedaan angka antara file lama dan baru → **file baru menang.**

## Riwayat angka yang ditarik
| Angka | Alasan |
|---|---|
| 58,7% | basis 375 salah (benar 776) |
| 87,5% | inflated, 321/335 same_domain beda domain |
| 442 missing | false negative, 10/10 sampel ternyata ADA |
| 238 relocated | angka staging v5, bukan hasil final |

Founder Sig: DHANI YULIAWAN
