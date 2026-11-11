# MEMORY — Ekstraksi Modul Miscellaneous → Code Enterprise (2026-10-30)

## SUMBER BLUEPRINT
- /root/projects/Blueprints_MusGo-OS_2in1/Miscellaneous/  = 63 file
- File kunci:
  - "bahasan extraksi modul 1.md" (461 KB) = daftar modul FASE A/B/C
  - "Modul_Tambahan.md" = spesifikasi Human CLI
  - MusGo.json = konfigurasi inti
  - Dokumen STRUKTUR REPOSITORY + CORE LOGIC SECURITY

## 10 MODUL YANG DIEKSTRAK
FASE B (Constitutional/Cognitive):
 1. mcl_enforcer        -> BELUM ADA di repo -> DIBUAT
 2. sybil_guard         -> HILANG
 3. planner_core        -> HILANG
 4. parallel_engine     -> HILANG
 5. logic_validator     -> HILANG
FASE C (Security/Memory) — SUDAH ADA SEMUA:
 6. instant_airgap  = ADA
 7. consensus       = ADA
 8. multi_hsm       = ADA
 9. integrity_chain = ADA
10. learning_validator = ADA

## PENEMPATAN
Blueprint pakai path FLAT; repo pakai 21-LAYER. Modul ditempatkan di layer yang tepat
BUKAN duplikat folder flat. Contoh terverifikasi:
constitutional_domain/layer_00_governor/mcl_enforcer/mcl_enforcer.py

## PELAJARAN KUNCI (BUG NYATA)
YAML TIDAK butuh escape backslash seperti string Python.
Salah: regex ditulis  setuid\\(0\\)  di YAML -> paren tak tertutup -> regex invalid.
Benar: setuid\(0\)
Ini BUKAN masalah test, ini masalah penulisan config.

## ATURAN
- stdlib-only Python, docstring Bahasa Indonesia
- fail-closed / deny-by-default
- workspace /root/projects = REFERENSI READ-ONLY saja
- kerja kode di /root/Repository MusGo-OS_2in1-main
- __pycache__ JANGAN di-commit
