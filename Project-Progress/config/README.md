# PROJECT PROGRESS — GOVERNANCE & CONFIGURATION GUIDE

**Lokasi:** `/home/Project-Progress/config/README.md`
**Pemilik:** DHANI YULIAWAN · **Versi Config:** 1.0.0

Dokumen ini adalah peta konfigurasi kanonik untuk workflow `Prompt_Instructions_Project_Progress_Workflow.md`.
Semua konfigurasi bersifat **deklaratif + tervalidasi mesin**, sehingga agent berikutnya tidak perlu menebak.

---

## 1. Peta File Konfigurasi

| # | File | Fungsi | Prioritas |
|---|------|--------|-----------|
| 1 | `founder_rules.yaml` | Aturan paling tinggi: bahasa formal, sapaan, tanda tangan, larangan, security constitution | **0 (absolut)** |
| 2 | `paths.yaml` | Single source of truth semua path + write-scope zero-trust | 1 |
| 3 | `canonical_workflow.yaml` | Urutan step A→D, orchestration loop, output format, trigger gate | 2 |
| 4 | `agents_skills_registry.yaml` | Katalog Agent↔Skill (duality), nomenklatur, integrasi router | 3 |
| 5 | `project_progress.config.yaml` | Runtime contract: network, runner, memory/knowledge, guard anti-halusinasi, validation matrix | 3 |
| 6 | `signature_block.md` | Template tanda tangan + struktur output | terkunci oleh #1 |
| 7 | `schemas/*.schema.json` | JSON Schema: `memory_entry`, `session_state`, `agent_skill_registry` | 4 |
| 8 | `scripts/musgo_config.py` | Loader + resolver path + validator (BUKAN mock) | tool |
| 9 | `scripts/verify_config.py` | Eksekusi 12 check (C01–C12) → `runtime/config_verify_report.json` | tool |
| 10 | `scripts/bootstrap.sh` | Bootstrap direktori memory/knowledge/runtime + seed file index | tool |

---

## 2. Hirarki Prioritas (Conflict Resolution)

```
founder_rules.yaml (priority 0, immutable)
   └── paths.yaml
          └── canonical_workflow.yaml
                 └── agents_skills_registry.yaml
                        └── project_progress.config.yaml
                               └── schemas/*.json
```

Jika dua konfigurasi bertentangan → **yang nomor lebih kecil menang**, dan konflik dicatat di
`knowledge/OPEN_QUESTIONS.md` dengan tag `CONFLICT:CONFIG`.

---

## 3. Cara Pakai (Founder / Agent)

```bash
cd /home/Project-Progress

# 1) Bootstrap struktur memory, knowledge, runtime, .state
bash config/scripts/bootstrap.sh

# 2) Validasi seluruh konfigurasi (12 check)
python3 config/scripts/verify_config.py

# 3) Resolve path kapan saja (jangan menulis path literal!)
python3 config/scripts/musgo_config.py get memory
python3 config/scripts/musgo_config.py show-paths
python3 config/scripts/musgo_config.py check-write knowledge/PROGRESS_LOG.md
```

Contoh di dalam kode Python:

```python
import sys; sys.path.insert(0, "config/scripts")
from musgo_config import load_config, resolve
cfg = load_config()
print(resolve(cfg, "memory"))            # /data/.../home/Project-Progress/memory
```

---

## 4. Alur yang Dikunci Konfigurasi

1. **Phase A — Grounding**: `paths.yaml` menentukan apa yang dibaca (blueprint, agents-skills, memory, knowledge, repo).
2. **Phase B — Orchestration**: `agents_skills_registry.yaml` menentukan cara memilih pair (prefix numerik identik) + batas swarm.
3. **Phase C — Execution**: `canonical_workflow.yaml#phase_c_execution` menentukan kewajiban eksplisit (validation, rollback, dsb).
4. **Phase D — Persistence**: `paths.yaml#memory_layout` + `schemas/memory_entry.schema.json` menentukan format entri yang ditulis.
5. **Setiap output** ditutup `signature_block.md`.

---

## 5. Catatan Path (Penting)

Prompt menuliskan `# 1. Analisa dir path /home/Project-Progress/`.
Pada device ini, root writable adalah `/data/user/0/com.openshell/files`,
sehingga path nyata adalah:

```
/data/user/0/com.openshell/files/home/Project-Progress/
```

Notasi `/home/...` diperlakukan sebagai **path logis** (`root_dirs.prompt_root`).
Untuk memindahkan environment (mis. ke VPS/Linux biasa), cukup ubah `root_dirs` di `paths.yaml`
atau set env `MUSGO_HOME` / `MUSGO_WORKSPACE`. Tidak ada file lain yang perlu disentuh.

---

## 6. Security Posture (Zero Trust)

- Semua tulis **wajib** di dalam `paths.yaml#integrity.write_scopes`.
- `knowledge/PROGRESS_LOG.md` & `memory/SESSION_INDEX.md` bersifat **append-only**.
- File ber-prefix `FOUNDER-` adalah **immutable** (tidak boleh diedit agent).
- Batas ukuran tulis: 2 MiB per file (proteksi resource exhaustion).
- Entri memory wajib punya `integrity.checksum_sha256` + rantai `prev_entry_hash` (tamper-evident).

---
Seluruh konfigurasi ini adalah implementasi langsung dari prompt Founder — tanpa placeholder.
