# MEMORY — FASE 2 SELESAI: 5 MODUL ENTERPRISE (2026-10-30)

## STATUS: 5 MODUL DIBUAT + LULUS TEST

| Modul | Path | Baris | Test |
|---|---|---|---|
| mcl_enforcer | constitutional_domain/layer_00_governor/mcl_enforcer | ~430 | 13/13 |
| sybil_guard | constitutional_domain/layer_00_governor/sybil_guard | 473 | 15/15 |
| planner_core | cognitive_domain/layer_02_musyawarah_planner/planner_core | 563 | 17/17 |
| parallel_engine | cognitive_domain/layer_03_goro_executor/parallel_engine | 523 | 16/16 |
| logic_validator | cognitive_domain/layer_02_musyawarah_planner/logic_guard | 481 | 21/21 |
TOTAL TEST: 82/82 PASS

## CACAT BLUEPRINT YANG DIPERBAIKI (5 modul, 8 cacat)

1. mcl_enforcer — release_lockdown kembalikan True untuk kunci palsu
   -> fail-closed + hmac.compare_digest
2. mcl_enforcer — regex rusak melempar exception
   -> _config_error, semua request DENIED
3. sybil_guard — CACAT FATAL: sha256(f"{agent_id}:{token}") membuat
   dua agent dengan token fisik SAMA menghasilkan hash BERBEDA ->
   deteksi Sybil DEAD CODE. Fix: sha256(f"{master}:{token}")
   Tanpa agent_id. Terbukti: hash kini identik, SYBIL_DETECTED bekerja.
4. sybil_guard — parameter `signature` di blueprint TIDAK PERNAH dipakai
   -> kini WAJIB diverifikasi HMAC-SHA256 constant-time
5. planner_core — sub_tasks HARDCODED (selalu 2 tugas sama)
   -> dekomposisi nyata dari kata kunci
6. planner_core — voting hitung approve/total saja
   -> berbobot per persona + VETO + kuorum minimum
7. parallel_engine (Go) — SELALU Success:true, tanpa timeout,
   rollback disebut di workflow tapi TIDAK ADA implementasi
   -> kegagalan/timeout/panic ditangkap + Atomic Rollback LIFO nyata
8. logic_validator — substring naif `kw in code`:
   FALSE POSITIVE "retrieval(" tertangkap sebagai "eval(",
   FALSE NEGATIVE __import__('os').system() LOLOS
   -> AST analysis + token scan + deteksi obfuscation

## PELAJARAN KUNCI
- Modul keamanan WAJIB diuji dengan SERANGAN NYATA, bukan happy-path.
  Test "identitas sah -> TRUSTED" lolos meski modulnya buta total.
- Setiap modul blueprint punya cacat. JANGAN port apa adanya.
- Intent drift: kata kerja perintah (hitung/buat/audit) BUKAN istilah
  konten. Ikut menghitungnya = false positive parah.
  Fix: ACTION_VERBS dibuang dari _extract_terms.

## POLA ENTERPRISE BAKU (pakai untuk modul berikutnya)
- Verdict/State Enum + dataclass hasil (bukan dict/raise)
- config_valid property + _config_error (fail-closed konstruksi)
- verify() tidak pernah melempar -> try/except -> DENIED
- Rantai audit SHA-256: prev_digest + digest, verify_chain()
- threading.RLock untuk state bersama
- Batas input (MAX_*_BYTES, MAX_TASKS)
- Stdlib-only, docstring Bahasa Indonesia
- tests/ berisi test suite mandiri: python3 tests/test_xxx.py
