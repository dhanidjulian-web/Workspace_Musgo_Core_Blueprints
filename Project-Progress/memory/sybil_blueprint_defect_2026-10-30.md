# MEMORY — CACAT DESAIN BLUEPRINT SYBIL GUARD (2026-10-30)

## TEMUAN KRITIS (terbukti lewat test, bukan dugaan)
Blueprint Miscellaneous/bahasan extraksi modul.md MODUL 3 menulis:
    computed_hash = sha256(f"{agent_id}:{hardware_token}")
    if computed_hash in active_bindings and active_bindings[computed_hash] != agent_id:

CACAT: karena `agent_id` ikut di-hash, dua agent BERBEDA dengan hardware_token
SAMA menghasilkan hash BERBEDA. Kunci dict tidak pernah bentrok ->
blok deteksi Sybil TIDAK PERNAH TERPICU (dead code).
Artinya modul "anti-Sybil" blueprint justru MELOLOSKAN serangan Sybil.

BUKTI ANGKA:
  sha256('agent-asli:hw-SAMA')  = 6acee299...
  sha256('agent-palsu:hw-SAMA') = 3b37a8ba...
  SAMA? False  -> tidak pernah bentrok

PERBAIKAN:
  Jangkar fisik HARUS diturunkan dari token fisik saja:
  sha256(f"{master_anchor}:{hardware_token}")
  agent_id dipertahankan di signature fungsi demi kompatibilitas API,
  TAPI tidak dipakai dalam perhitungan hash.
  Setelah fix: kedua hash identik -> SYBIL_DETECTED bekerja.

PELAJARAN UMUM: modul keamanan WAJIB diuji dengan SERANGAN NYATA, bukan hanya
happy-path. Test "identitas sah -> TRUSTED" lolos meski modulnya buta.

## CACAT BLUEPRINT LAIN YANG DIPERBAIKI
1. mcl_enforcer: release_lockdown mengembalikan True untuk kunci palsu
   (sebelumnya) -> kini fail-closed + hmac.compare_digest.
2. mcl_enforcer: regex rusak melempar exception -> kini _config_error,
   semua request DENIED.
3. planner_core: deconstruct_user_intent mengembalikan sub_tasks HARDCODED
   (selalu 2 tugas sama) -> kini dekomposisi nyata dari kata kunci.
4. planner_core: voting hanya hitung approve/total -> kini berbobot + veto
   + kuorum minimum.
5. parallel_engine (Go): SELALU Success:true (worker tak pernah gagal),
   tanpa timeout, rollback disebut di workflow tapi TIDAK diimplementasi.

## HASIL TEST (terverifikasi)
- mcl_enforcer    : 13/13 PASS
- sybil_guard     : 15/15 PASS
- planner_core    : 17/17 PASS
- parallel_engine : 523 baris dibuat, TEST BELUM DIJALANKAN
- logic_validator : BELUM DIBUAT

## PATH TERVERIFIKASI (find, 2026-10-30)
constitutional_domain/layer_00_governor/mcl_enforcer
constitutional_domain/layer_00_governor/sybil_guard
cognitive_domain/layer_02_musyawarah_planner/planner_core
cognitive_domain/layer_03_goro_executor/parallel_engine
logic_validator: BELUM ADA

## STATUS REPO
HEAD = 67ad661 (BELUM bergerak). Belum commit, belum push.
