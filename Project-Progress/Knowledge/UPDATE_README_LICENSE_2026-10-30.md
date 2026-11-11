# UPDATE README.md & LICENSE — 2026-10-30

## KOMIT
cc49bfc665c4b1c4ca847386da9bf1fda8f39ba6
"docs: rewrite README (28 root folder, 21 layer, 9router) + LICENSE Proprietary"
Push SSH: 7246b8e..cc49bfc main->main | ahead/behind 0/0 | tree bersih

## TEMUAN KRITIS YANG DIPERBAIKI
KONTRADIKSI HUKUM: README menyatakan "Proprietary / All Rights Reserved",
tetapi berkas LICENSE berisi MIT License (Copyright (c) 2026 dhanidjulian).
MIT mengizinkan penggunaan komersial bebas, sublicense, dan penjualan —
berlawanan total dengan klaim "All Rights Reserved". Risiko: pelepasan hak
intelektual secara implisit atas IP utama (Musyawarah Planner, GoRo Executor,
NoBypassGate, Signature Engine, GENESIS_INIT).

## PERBAIKAN README.md (6.313 B -> 10.334 B, 189 baris)
1. Klaim "25 Root Folder" -> DIPERBAIKI menjadi 28 (terverifikasi find -maxdepth 1)
2. Tambah badge Layers 21 + License Proprietary
3. Tambah tabel pemetaan 21 layer (Layer 00-20) -> path domain
4. Tabel struktur: tambah kolom jumlah file per folder (total 1.579)
5. PERBAIKAN FAKTA: hapus klaim "Framework/musyawarah_core, goro_core"
   (tidak ada di repo). Diganti daftar modul Framework/ riil: core,
   signature_engine, keras3, atomic_transaction, circuit_breaker,
   distributed_lock, event_bus, idempotency_guard, integrity_hashchain,
   nonce_replay_guard, resource_governor, retry_orchestrator,
   rollback_manager, transaction_engine
6. Tambah bagian AI Provider Routing 9router (Layer 05): deny_by_default,
   fail_closed, audit_all_calls, capability->cost, env MUSGO_9ROUTER_API_KEY,
   budget $5/hari $100/bulan, 9router_ctl.sh
7. Tambah bagian Infrastruktur & Deployment: 6 tf, 4 docker, 3 systemd, migrasi
8. CI/CD: diperjelas dengan nama berkas (ci_cd.yml, security_scan.yml, deployment.yml)
9. Tambah perintah uji 9router offline + integrasi

## PERBAIKAN LICENSE (1.069 B MIT -> 9.222 B Proprietary, 202 baris)
11 pasal:
 1. Grant terbatas (hanya view/study + evaluasi non-komersial internal)
 2. Prohibited acts (copy, modify, merge, distribute, sublicense, sell,
    reverse engineer, hapus notice, pakai nama/merek)
 3. Ownership IP (21 layer + Musyawarah+GoRo+NoBypassGate+Signature+GENESIS_INIT)
 4. No warranty
 5. Limitation of liability
 6. Third-party & compatibility -> KLAUSUL KUNCI: seluruh lisensi open-source
    sebelumnya dinyatakan SUPERSEDED, REVOKED, NO FURTHER FORCE OR EFFECT
 7. Termination otomatis saat pelanggaran
 8. Audit & enforcement
 9. Governing law: Republik Indonesia
10. Severability & entire agreement
11. Inquiries

## VALIDASI PRA-COMMIT
- 28 folder di README == 28 folder riil (0 selisih, 0 klaim palsu)
- grep "MIT License" README = 0 ; LICENSE = 1 (hanya klausul penegasan)
- grep "Proprietary": LICENSE 4x, README 3x
- 67 baris tabel markdown
- Backup asli: Project-Progress/Runtime/backup_meta/{README,LICENSE}.bak_2026-10-30
- Verifikasi remote: git show origin/main:README.md = 10.334 B ; LICENSE = 9.222 B
