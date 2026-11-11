## 📁 STRUKTUR DIREKTORI REPOSITORY REVISION V9.3 (ROOT TREE)

```
/workspace/MusGo-OS/V9.3/
├── apps/
│   └── internal/
│       └── ai_live_guide/
│           ├── persona_database/               # Database 525 Persona Khusus AI Live Guide
│           │   ├── ui_companions/              # 25 Persona Companion & Voice Avatar
│           │   ├── syura_moderators/           # 250 Persona Moderator Musyawarah
│           │   └── local_admin_guardians/      # 250 Persona Local Admin & Offline Maintenance
│           └── runtime/
│               ├── ai_live_guide_core.py        # Subsystem Utama AI Live Guide
│               ├── offline_maintenance_agent.py # Agent Pengelola System Offline/Air-Gap
│               └── human_suggest_engine.ts      # Engine Interaksi UI Click-Right & Auto-Suggest
├── core/
│   ├── cognitive_domain/
│   │   ├── layer_02_musyawarah_planner/
│   │   │   └── planner_instruction_core.py     # Prompt Ramping Agent Planner
│   │   ├── layer_03_goro_executor/
│   │   │   └── executor_instruction_core.py    # Prompt Ramping Agent Executor
│   │   └── skill_engine/
│   │       ├── skill_router.py                  # Router Pencari & Penyaring 4000+ skill.md
│   │       ├── skill_loader.go                  # Dynamic Injection Engine (Hot-Reload)
│   │       └── skill_verifier.py                # Verifikator Kriptografis HMAC-SHA3-512
│   └── skill_repository/                        # Cermin Local/GitHub Repositori 4000+ skill.md
└── memory_domain/
    └── skill_execution_ledger/
        ├── skill_audit_trail.sql                # Ledger Histori Eksekusi Skill.md
        └── offline_event_log.sys                # Log Aktivitas Pemeliharaan Lokal Offline
```

```text
/workspace/MusGo-OS/V9.3/
├── apps/
│   └── internal/
│       ├── ai_live_guide/               # 525 Persona AI Live Guide, Local Admin, & Offline Maintenance
│       └── orchestration_console/      # Sovereign Command Console & Human Override Interface
├── core/
│   ├── cognitive_domain/
│   │   ├── layer_02_musyawarah_planner/ # Musyawarah Planner Agent (Instruction Core)
│   │   └── layer_03_goro_executor/     # Gotong-Royong Executor Agent (Instruction Core)
│   ├── security_governance/
│   │   ├── layer_00_ebpf_shield/       # eBPF Kernel Shield & Resource Enforcement
│   │   └── layer_06_policy_ethics/      # Policy & Ethics Guard (Non-Bypass Moral Filter)
│   └── skill_engine/
│       ├── skill_router.py              # Pembaca & Router 4.000+ SKILL.md dari Repositori GitHub
│       └── skill_verifier.py            # Verifikator Integritas Kriptografis HMAC-SHA3-512
├── infrastructure/
│   ├── vps_scaler/                      # Scaler VPS S0 - S16 (MVP hingga Planetary Cluster)
│   ├── federation/                      # Multi-Region Zero-Trust Mesh & IPFS Cold Storage
│   └── resilience/                      # Self-Healing Active Defense & Knowledge Resurrection Engine
└── business_domain/
    └── monetization/
        ├── billing_engine.py            # Logic Token Calculator & Pay-As-You-Go Billing
        └── revenue_router.py            # Revenue Splitter (60% Dev / 30% Founder / 10% Treasury)
```

Implementasi logika "1+1=2" sebagai Read-Only Security ini secara permanen tertanam dalam repositori resmi MusGo-OS 2in1 sebagai berikut:

```
/Direktori Path/MusGo-OS/V9.1/
├── /constitutional_domain/
│   ├── /core/
│   │   ├── mcl_enforcer.go             # Penegak Konstitusi "1+1=2" di Ring 0
│   │   ├── immutable_rules.yaml        # Definisi aturan Hard-Link Read-Only
│   │   ├── update_controller.go        # Gerbang Tunggal Pembaruan Legal (75% Quorum)
│   │   ├── mount_validator.go          # Verifikasi RSA-4096 Hash sebelum Mounting
│   │   └── overlayfs_manager.sh        # Orkestrator Pemisahan Lowerdir & Upperdir
│   └── /specs/
│       ├── MCL_V9_1_FINAL.yaml         # Specification Machine-Readable Law
│       ├── mgp_core.yaml               # Governor Protocol Specification (MGP-V & MGP-H)
│       └── mias_immutable_spec.md      # Immutable Architecture Specification (MIAS)
├── /security_domain/
│   ├── /defense/
│   │   ├── write_guard_interceptor.py  # Pendeteksi upaya bypass Read-Only di User-Space
│   │   └── /kernel/
│   │       └── write_guard.c           # eBPF LSM Interceptor di Kernel Space (Ring 0)
│   └── /core/
│       └── immutable_config_guard.sh   # Pengunci biner Sterilizer & Enforcer
├── /memory_domain/
│   └── /integrity/
│       └── tamper_evident_chain.py     # Hash-Chain Ledger Penjaga Sejarah Imutabel
└── /recovery_domain/
    ├── snapshot_validator.ext          # Verifikator Snapshot sebelum Pemulihan
    └── resurrection_controller.py
```

