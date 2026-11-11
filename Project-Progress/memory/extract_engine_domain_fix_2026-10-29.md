# MEMORY — EXTRACT ENGINE v6, KOREKSI BUG DOMAIN & AUDIT ANGKA
Tanggal: 2026-10-29 WIB
Status: SELESAI — VERIFIED_CONSISTENT

## 1. KEPUTUSAN FOUNDER (mengikat)
**Relokasi = DESAIN SAH.** 81 modul `relocated` dihitung TERINTEGRASI.

## 2. BUG DOMAIN — DIPERBAIKI
Gejala: recovery_domain 836 entri, padahal struktur asli ~15 file.
Akar: parser hanya me-reset current_domain pada folder berakhiran `_domain`.
Folder root lain (specifications/, system/, extensions/, deployment/, apps/,
Framework/, maintenance/, docs/, SDK/) tidak reset -> "last-domain-wins".
Fix: deteksi root-level via icon-at-column-0.
Hasil: recovery_domain 836 -> 23. TERVERIFIKASI.

## 3. ANOMALI BUKAN BUG
red_team_ai.py memang 2x di blueprint: baris 959 (simulation_domain),
baris 1810 (deployment). Duplikat asli di sumber, bukan misatribusi.

## 4. KOREKSI BERANTAI (3 lapis, dicatat jujur)
a) Klaim "58,7%" -> DITARIK (basis 375 salah, benar 776).
b) Klaim "87,5%" -> DITARIK (inflated, 321/335 same_domain beda domain).
c) Klaim "CSV invalid karena domain salah" -> KLAIM ITU SENDIRI SALAH.
   Verifikasi disk membuktikan CSV sudah pakai parser v6 benar.
d) SESI INI: tabel laporan saya & file memory membawa angka v5 BASI:
     relocated 238 -> benar 81
     consolidated 76 -> benar 81
     name_duplicate 38 -> benar 30
     ambiguous 51 -> benar 15
     same_domain 2 -> benar 3
   Akar: saya menyalin angka dari ingatan/versi lama, bukan dari CSV.
   FIX: semua file di-regenerate dari 03_module_mapping.csv (sumber tunggal).

## 5. PELAJARAN KUNCI
1. JANGAN kutip angka dari ingatan. Selalu baca CSV aktual.
2. JANGAN simpulkan dataset invalid tanpa verifikasi file di disk.
3. Audit konsistensi WAJIB: setiap verdict harus memetakan ke tepat
   satu nilai `integrated`, dan sum verdict == sum integrated == basis.
4. Validasi manual sampel SEBELUM melaporkan persentase.

## 6. ANGKA RESMI FINAL (dari CSV, terverifikasi)
Basis: 776 file .py

| verdict          | n   | integrated |
|------------------|-----|------------|
| flattened        | 248 | yes |
| exact            | 209 | yes |
| missing          |  97 | no  |
| consolidated     |  81 | yes |
| relocated        |  81 | likely |
| name_duplicate   |  30 | no  |
| ambiguous        |  15 | no  |
| same_layer       |  12 | yes |
| same_domain      |   3 | yes |
| TOTAL            | 776 | |

integrated: yes=553 | likely=81 | no=142

SETELAH relokasi = SAH:
- Batas BAWAH = 553/776 = 71,3%
- Batas ATAS  = 634/776 = 81,7%
- GAP SEJATI  =  97/776 = 12,5%
- PERLU TINJAU =  45/776 =  5,8%  (name_dup 30 + ambiguous 15)
SUM CHECK: 553+81+45+97 = 776 ✅

## 7. GAP 97 PER DOMAIN
apps/ecosystem 43 | security_domain 24 | services 13 | maintenance 10
runtime_domain 6 | system 1
Placeholder Reserve-01..05.py bukan gap nyata -> gap riil 92.

## 8. VALIDASI
15 sampel missing diuji `find -iname` -> 15/15 ABSEN.
Audit konsistensi verdict->integrated: PASS (9 verdict, 1:1 mapping).

## 9. FILE TERVERIFIKASI PADA DISK
Knowledge/Extract/
  01_blueprint_index.csv       101.190 B  (1556 entri, recovery_domain=23)
  02_repo_index.csv            122.357 B  (1586 file)
  03_module_mapping.csv        100.038 B  (776 verdict) <- SUMBER OTORITATIF
  03b_doc_config_mapping.csv    77.431 B
  04_layer_summary.csv           2.515 B
  05_GAP_REPORT.md               3.632 B  (v6, regenerate)
  summary.json                   (VERIFIED_CONSISTENT)
  scripts/extract_audit.py      10.095 B  (v6 is_root fix)
  scripts/extract_audit_v5_backup.py 9.783 B
Knowledge/AUDIT_FINAL_2026-10-29.md  3.632 B
memory/extract_engine_domain_fix_2026-10-29.md
.state/state_extract_engine_2026-10-29.json

## 10. NEXT
1. Tinjau 45 file (30 name_duplicate + 15 ambiguous)
2. Fase 4: Agents/Skills (4.408 file)
3. Fase 5: Zero-Trust policies
4. Fase 6: VPS S0-S16 & 8 Tier verbatim + code logic
5. Fase 7: LAPORAN FINAL

Founder Sig: DHANI YULIAWAN
