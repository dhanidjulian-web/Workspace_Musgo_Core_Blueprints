# MEMORY — Build Extract Engine (matcher domain-scoped) | 2026-10-28

## AMANAT
"finish_domain_scoped_matcher" — selesaikan matcher, hasilkan dataset yang bisa dipercaya.

## YANG DIKERJAKAN
1. Verifikasi v3 di disk (87,5% coverage) -> ternyata INFLATED
2. Validasi manual 15 sampel `missing` v3 -> 15/15 benar-benar absen (v3 akurat di kelas itu)
3. Audit kelas `same_domain` -> TEMUAN: 321 dari 335 BEDA DOMAIN = false positive besar
4. Ukur inflasi: 679 "covered" hanya menunjuk 588 repo_path unik
5. Tulis v4 STRICT: cross_domain & ambiguous TIDAK dihitung terintegrasi
6. Temuan: cross_domain BUKAN false positive, tapi RELOKASI nyata
7. Pisahkan berbasis keunikan nama: relocated (238) vs name_duplicate (38)
8. Final v5: semua 776 file terakuntansi (sum check OK)

## ANGKA FINAL (v5)
776 file .py diharapkan:
- exact 209 (26,9%) | relocated 238 (30,7%) | consolidated 76 (9,8%)
- flattened 53 (6,8%) | same_layer 12 (1,5%) | same_domain 2 (0,3%)
- ambiguous 51 (6,6%) | name_duplicate 38 (4,9%) | missing 97 (12,5%)

- integrated PASTI      : 352/776 = 45,4%  (batas bawah)
- integrated + relokasi : 590/776 = 76,0%  (batas atas)
- GAP SEJATI            : 97/776  = 12,5%

## GAP 97 FILE
recovery_domain 67 | security_domain 24 | runtime_domain 6

## KESALAHAN YANG SAYA ULANGI & PERBAIKI
- v1: 77% -> false positive (__init__.py dihitung, nama tercemar #anotasi)
- v2: 442 missing -> false negative (10/10 sampel manual ternyata ADA)
- v3: 87,5% -> inflated (same_domain lintas domain dihitung)
- v4/v5: STRICT + validasi manual = 45,4% / 76,0% / 12,5%

## PELAJARAN
1. JANGAN pakai basename matching lintas-domain -> nama generik (engine.py, guard.py)
   cocok di mana saja dan menggelembungkan coverage.
2. Selalu ukur inflasi: bandingkan jumlah "covered" vs repo_path UNIK.
3. Selalu validasi manual sampel SEBELUM melaporkan persentase.
4. Kelas `missing` harus diuji dengan `find -iname` (fuzzy), bukan exact match saja.
5. Laporkan batas BAWAH dan ATAS, jangan satu angka.
6. Simpan skrip parser setiap kali dibuat (kesalahan audit lalu: skrip hilang).

## TEMUAN STRUKTURAL (butuh keputusan Founder)
- Repo RELOKASI 238 modul ke domain top-level lain (system/, maintenance/,
  extensions/, resource_governor/, Framework/) — bukan hilang.
- Repo FLATTENING 53 modul: segmen layer_XX_ dibuang dari path.
- Repo KONSOLIDASI 76 kasus: 1 file modul menggantikan banyak file blueprint.
- PERTANYAAN: relokasi/flattening ini desain sah atau penyimpangan dari V9.1?

## FILE TERBUKTI ADA (Project-Progress)
Knowledge/Extract/:
  01_blueprint_index.csv 103.698 B | 02_repo_index.csv 120.770 B
  03_module_mapping.csv 101.450 B | 03b_doc_config_mapping.csv 80.807 B
  04_layer_summary.csv 1.704 B | 05_GAP_REPORT.md 4.787 B
  summary.json 717 B | scripts/extract_audit.py

## NEXT
- Tunggu keputusan Founder soal relokasi/flattening
- Lanjut: Agents/Skills (4.408 file), Zero-Trust, VPS S0-S16, 8 Tier, code logic
