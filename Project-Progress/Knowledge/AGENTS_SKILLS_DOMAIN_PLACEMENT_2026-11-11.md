# ANALISA & REKOMENDASI LOKASI DOMAIN AGENTS-SKILLS
Tanggal: 2026-11-11
Repo: /root/Repository MusGo-OS_2in1-main @ 8cb2f8f
Amanat Founder: "Semua Agents MusGo-OS 2in1 hanya menggunakan Daftar Agents dan Skills.
Tidak menggunakan persona lagi. 525 Persona hanya digunakan Default Local Model
sebagai AI Live Guide berdasarkan konteks interaksi dengan user."

---

## BAGIAN 1 — KOREKSI ARSITEKTUR (diterima, mengikat)

### Yang SALAH (pemahaman lama)
Persona (525+) dianggap sebagai bagian dari Agents-Skills.

### Yang BENAR (amanat Founder 2026-11-11)
Ada DUA kategori berbeda yang harus DIPISAH TOTAL:

| kategori | Pemakai | Fungsi | Sumber |
|---|---|---|---|
| **Daftar Agents & Skills** | Semua Agent MusGo-OS 2in1 | Kapabilitas/knowledge yang dipanggil saat eksekusi tugas | `/root/projects/Agents-Skills/` |
| **525 Persona** | Default Local Model SAJA (AI Live Guide) | Persona percakapan berbasis konteks interaksi user | `Blueprints_MusGo-OS_2in1/Ai_models-agent-personas_Pool/personas/` |

**Agent TIDAK memakai persona.** Agent memakai Agent+Skill pair (prinsip duality).

### Bukti Kode yang MENGKONFIRMASI Pemisahan Ini
`cognitive_domain/persona_registry/registry_config.yaml`:
```yaml
persona:
  required_fields: [name, role, behavior_rules]
  max_definition_bytes: 65536
  single_active_persona: true   # <-- HANYA 1 aktif = konteks percakapan, bukan agent
```
`single_active_persona: true` adalah tanda jelas ini **runtime persona percakapan**
(AI Live Guide), BUKAN registri agent (agent bisa banyak aktif bersamaan).

### Konsekuensi untuk Audit
Fase 4 sebelumnya menganggap 525 persona bagian dari gap Agents-Skills.
**KOREKSI: itu dua gap berbeda:**
- Gap A: Agents-Skills (4.408 file blueprint) — belum di repo
- Gap B: Persona pool (297 file, `personas/` berisi Core 525+) — untuk AI Live Guide

---

## BAGIAN 2 — INVENTARIS FAKTA

### Sumber Agents-Skills
`/root/projects/Agents-Skills/`
- 4.408 file total | 3.940 .md | 151 .py | 34 yaml
- 109 file root: 71 AGENT.md + 38 SKILL.md
- 37 subdirektori skill pack
- 74 kelompok numerik (1–75, gap 24)
- INDEX_AGENTS_SKILLS.md: 98 baris tabel (Agent↔Skill pair per kelompok)

### Sumber Persona (TERPISAH)
`Blueprints_MusGo-OS_2in1/Ai_models-agent-personas_Pool/`
- 297 file total
- `personas/` berisi 4 entri:
  - `1. Ai live guide 25 persona`
  - `2. Musyawarah Planner persona`
  - `3. GoRo Executor persona`
  - `Core 525+ Persona.md`

### Struktur Repo Relevan (existing)
| Path | File | Peran saat ini |
|---|---:|---|
| `cognitive_domain/layer_05_agent_orchestration/` | 59 | Layer orkestrasi agent |
| `→ agents/` | 19 | Implementasi agent (code) |
| `→ agent_registry/` | 5 | Registry agent (code) |
| `→ swarm_coordinator/` | 5 | Koordinasi swarm |
| `→ ai_provider_9router/` | 26 | Modul 9router (agent+skill+prompt+wf+hook) |
| `cognitive_domain/persona_registry/` | 3 | Registry PERSONA (percakapan) |
| `cognitive_domain/planner_registry/` | 3 | Registry planner |
| `ai_live_guide/` | 17 | AI Live Guide (persona runtime) |
| `knowledge_graph/` | 11 | Knowledge graph |
| `persona_communication_policy/` | 15 | Policy mode komunikasi |

### Apa yang Dikatakan Blueprint v9.1
`STRUKTUR REPOSITORY FINAL.md`:
- **TIDAK ADA** entri `Agents-Skills/` di root
- Satu-satunya `agents/` ada di **baris 210** = subfolder kode di dalam `layer_05`:
  ```
  ├── 📁layer_05_agent_orchestration/
  │   ├── 📁 agent_registry/
  │   ├── 📁 agents/          <-- kode agent (executor/, planner/)
  ```
- Blueprint punya klausul eksplisit: `| <tambahan folder/file> jika ada Update`
  → perluasan sah.

---

## BAGIAN 3 — EVALUASI 4 OPSI LOKASI

### OPSI A — Domain baru di root: `agents_skills/`
```
/agents_skills/
├── INDEX_AGENTS_SKILLS.md
├── agents/          (71 agent persona)
├── skills/          (38 skill root)
└── packs/           (37 skill pack)
```
Kelebihan:
- Terpisah total dari persona (sesuai amanat Founder) ✅
- Sejajar dengan domain lain (specifications/, extensions/, knowledge_graph/) ✅
- Mudah diaudit: 1 tempat, 1 index ✅
- Tidak mengganggu struktur 21 layer ✅

Kekurangan:
- Menambah root dir baru (root jadi 32)
- Perlu update blueprint v9.1

### OPSI B — Di dalam layer_05 (`agent_orchestration/`)
```
cognitive_domain/layer_05_agent_orchestration/
├── agents/          (kode agent — SUDAH ADA)
├── skills/          (BARU: 71 agent.md + 38 skill.md)
└── packs/           (BARU: 37 skill pack)
```
Kelebihan:
- "Agent" secara konsep di layer orkestrasi agent — koheren
- Dekat dengan `agent_registry/` dan `swarm_coordinator/` ✅

Kekurangan:
- **MENCAMPUR kode dengan konten aset** (layer_05 sudah 59 file kode)
- 4.408 file akan membuat layer_05 jadi raksasa (59 → 4.467)
- Melanggar prinsip pemisahan kode vs knowledge
- Blueprint menempatkan `agents/` di layer_05 untuk **kode**, bukan aset

### OPSI C — Di `cognitive_domain` root (sejajar persona_registry)
```
cognitive_domain/
├── persona_registry/     (persona — AI Live Guide)
├── agents_skills/        (BARU: Agent+Skill catalog)
├── planner_registry/
└── ...
```
Kelebihan:
- Sejajar dengan `persona_registry/` = simetri konsep (persona vs agent+skill)
- Tetap dalam domain kognitif ✅

Kekurangan:
- `cognitive_domain` lebih berorientasi kode Python (persona_registry = 3 file .py)
- Menaruh 4.408 file .md di dalam domain kode tidak konsisten

### OPSI D — Di `knowledge_graph/` atau `persona_communication_policy/`
DITOLAK:
- `knowledge_graph/` = graph entitas & relasi, bukan katalog capability
- `persona_communication_policy/` = mode komunikasi (casual/developer/enterprise), bukan agent

---

## BAGIAN 4 — REKOMENDASI FINAL

### ✅ PILIHAN: OPSI A — Domain baru `agents_skills/` di root repository

Struktur yang diusulkan:
```
/agents_skills/
├── README.md
├── SECURITY.md
├── API.md
├── INDEX_AGENTS_SKILLS.md          (master index: 98 pair)
├── agents/                          (71 file AGENT.md)
│   ├── governance/
│   ├── engineering/
│   ├── ai_intelligence/
│   ├── business/
│   └── research/
├── skills/                          (38 file SKILL.md root)
└── packs/                           (37 subdirektori skill pack)
    ├── composio-skills/
    ├── anthropic-cybersecurity/
    ├── awesome-copilot/
    └── ...
```

### Alasan (berbasis bukti, bukan opini)

1. **PRINSIP PEMISAHAN (amanat Founder)**
   Agents-Skills ≠ Persona. Harus punya rumah sendiri, sejajar dengan
   `persona_communication_policy/` dan `ai_live_guide/` yang sudah dipisah.

2. **KONSISTENSI DENGAN POLA REPO**
   Repo sudah memakai pola "domain sejajar di root" untuk komponen besar:
   `knowledge_graph/`, `ai_live_guide/`, `agent_sandbox/`, `persona_communication_policy/`,
   `resource_governor/`. Agents-Skills ukurannya jauh lebih besar (4.408 file)
   → layak jadi domain root sendiri.

3. **TIDAK MERUSAK 21 LAYER**
   Audit Fase 3: 21/21 layer cocok 100%. Menaruh aset di root tidak menyentuh layer.

4. **SKALABILITAS**
   4.408 file bisa tumbuh. Di root, bisa dipisah per kategori/kelompok (74 kelompok)
   tanpa mengganggu kode.

5. **AUDITABILITY**
   Satu lokasi + satu INDEX = mudah diverifikasi ulang kapan pun.

6. **BLUEPRINT MENGIZINKAN**
   Klausul `| <tambahan folder/file> jika ada Update` secara eksplisit
   membuka ruang penambahan folder root.

### Yang DITOLAK beserta alasan
- **Opsi B (layer_05)**: melanggar pemisahan kode vs aset; layer_05 akan membengkak
  dari 59 → 4.467 file. Blueprint menempatkan `agents/` di layer_05 untuk KODE saja.
- **Opsi C (cognitive_domain)**: domain ini berorientasi kode .py; 4.408 .md
  tidak konsisten.
- **Opsi D (knowledge_graph/persona_policy)**: salah peran sepenuhnya.

---

## BAGIAN 5 — PEMISAHAN PERSONA (pelengkap)

Persona **TIDAK** masuk `agents_skills/`. Tetap di jalurnya sendiri:

```
ai_live_guide/                        (sudah ada, 17 file)
├── adaptive_personality/
├── avatar_runtime/
├── conversation_memory/
├── emotional_engine/
├── gesture_animation/
├── realtime_voice/
└── screen_assistance/

cognitive_domain/persona_registry/    (sudah ada, 3 file — code)
  → loader + registry + config (single_active_persona: true)
```

Sumber persona `Ai_models-agent-personas_Pool/personas/` (Core 525+)
belum dimigrasikan. **Bukan bagian dari Fase 4 Agents-Skills.**
Ini pekerjaan terpisah: "AI Live Guide Persona Pipeline".

---

## BAGIAN 6 — KEPUTUSAN YANG DIPERLUKAN FOUNDER

1. Setujui `agents_skills/` sebagai domain root baru? (Rekomendasi: YA)
2. Cakupan migrasi:
   - (a) Penuh 4.408 file
   - (b) Root 109 file (71 AGENT + 38 SKILL) dulu
   - (c) 71 AGENT persona inti dulu
3. Update blueprint v9.1 untuk mencantumkan `agents_skills/`?

---

## File Tersimpan
- `Knowledge/AGENTS_SKILLS_DOMAIN_PLACEMENT_2026-11-11.md` (file ini)
- `memory/agents_skills_persona_separation_2026-11-11.md`

---
Founder Sig: DHANI YULIAWAN
