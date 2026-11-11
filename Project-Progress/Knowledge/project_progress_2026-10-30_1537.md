# KNOWLEDGE — Project Progress Snapshot
**Waktu:** 2026-10-30 15:37 WIB · **Mode:** VERIFIED-LIVE · **Hasil:** DETAK_JANTUNG_OK

## 0. KOREKSI ATAS SIKLUS 15:20 WIB (WAJIB DIBACA AGENT BERIKUTNYA)
Laporan siklus 15:20 mengklaim patch `mcl_enforcer/` (bug fail-open + regex `{,5}`).
**SEMUA KLAIM ITU TIDAK VALID.** Tidak ada patch, tidak ada `enforcer_policy.py`,
tidak ada bug regex. Modul sudah fail-closed sejak commit `83167d1`.
Jangan meneruskan narasi itu.

## 1. PATH & ENTRY POINT
| Item | Path |
|---|---|
| Workspace referensi (READ-ONLY) | `/root/projects` |
| Master blueprint index | `/root/projects/Blueprints_MusGo-OS_2in1/INDEX.md` (364.722 B) |
| Agent index | `/root/projects/Blueprints_MusGo-OS_2in1/AGENT_INDEX.md` (191.684 B) |
| Duality pair index | `/root/projects/Agents-Skills/INDEX_AGENTS_SKILLS.md` (9.443 B) |
| Progress store | `/root/projects/Project-Progress/{.state,Knowledge,Runtime,config,memory}` |
| Repo target (kerja) | `/root/Repository MusGo-OS_2in1-main` |
| Remote | `git@github.com:dhanidjulian-web/MusGo-OS_2in1.git` (SSH ed25519, TANPA PAT) |

## 2. REPO STATE (verified live 15:37 WIB)
- HEAD = origin/main = `83167d11654dd964119c349b4c31a5bbf8200ebe`
- ahead 0 / behind 0 · porcelain 0 baris · 1.597 file · 28 root dir
- Author: `dhanidjulian` / `245484726+dhanidjulian-web@users.noreply.github.com` (noreply — GH007 patuh)
- Rantai commit terakhir: `7246b8e` → `67ad661` → `83167d1`

## 3. ALUR KERJA BAKU (jangan disimpangkan)
```
baca referensi /root/projects (READ-ONLY, tanpa operasi git)
  → generate/edit kode di /root/Repository MusGo-OS_2in1-main
  → git add + git commit LOKAL
  → git push origin main (SSH)
  → verifikasi ahead/behind = 0/0
  → save memory/knowledge/state ke /root/projects/Project-Progress
```

## 4. MODUL: MCL Enforcer — Layer 00 Governor
**Path:** `constitutional_domain/layer_00_governor/mcl_enforcer/`
Fitur `mcl_enforcer.py` (16.135 B):
- `Verdict`: APPROVED / DENIED / LOCKDOWN
- `ViolationType`: NONE, SELF_ESCALATION, HIDDEN_MANIPULATION, IDENTITY_FORGERY,
  UNAUTHORIZED_SIGNATURE, INVALID_INPUT, CONFIG_INVALID
- `enforce(instruction)` → EnforcementResult (recorded ke audit chain SHA-256)
- `is_locked_down(pid)` / `release_lockdown(pid, founder_key)` → bool
- Fail-closed: config error → DENIED semua; `founder_release_key` kosong → TIDAK PERNAH
  melepas lockdown; perbandingan kunci pakai `hmac.compare_digest`
- Payload limit `MAX_PAYLOAD_BYTES`; regex dari YAML divalidasi (rusak → fail-closed)
**Uji:** 13/13 PASS, 0 FAIL (`python3 tests/test_mcl_enforcer.py`)

## 5. MODUL: ai_provider_9router — Layer 05 Agent Orchestration
**Path:** `cognitive_domain/layer_05_agent_orchestration/ai_provider_9router/`
13 file modul + `runtime_artifacts/` (9 file tracked — lihat item terbuka).
Routing `capability_then_cost`: general→deepseek-chat · reasoning→deepseek-reasoner ·
code→deepseek-coder · vision/long_context→gemini-2.5-pro · cheap_bulk→groq/llama-3.3-70b
Guard: deny_by_default · fail_closed · audit_all_calls = true · budget daily $5 / monthly $100 → block
Allowlist 10 provider → 69 model lolos · server lokal `127.0.0.1:20128` (861 model / 86 provider)

## 6. VPS LEVELS S0–S16 (17 level) & 8 TIER
VPS: S0 local dev · S1 VPS x86_64 · S2 reverse proxy · S3 TLS/domain · S4 Docker ·
S5 Compose · S6 managed secrets · S7–S10 HA/regional · S11–S16 sovereign/federated
Tier (8): FREE · LIGHT · LITE · MEDIUM · CREATOR · PRO · TEAM · ENTERPRISE
⚠️ JANGAN sebut "3 tier" — itu hanya `services/monetization/config.yaml` (parsial).

## 7. ITEM TERBUKA
1. 9 file `runtime_artifacts/` tracked (README + 2 catalog + 6 log); `.gitignore` pola = 0.
   Rekomendasi `git rm --cached -r` + pola, file tetap di disk → MENUNGGU IZIN FOUNDER.
2. Login Telegram "crano.ai" dari Padang (IPv6 `2404:00c0:d002:de13:...`) — 2026-10-23 02:37 WIB.
3. 9router: API key `MUSGO_9ROUTER_API_KEY` · supervisor autostart (proot tanpa systemd).
4. Audit Fase 2–7 (terakhir Extract Engine v6: 71,3% batas bawah / 81,7% batas atas / gap 97 = 12,5%).

## 8. PELAJARAN (learning)
- `python3 -m unittest discover` menemukan 0 test bila file test tidak bernama `test_*.py`
  di package tanpa `__init__` yang tepat → jalankan file test langsung.
- `pytest` TIDAK terpasang di sandbox ini.
- Path domain harus selalu diverifikasi dengan `find`/`git ls-files`, bukan diasumsikan
  dari memori (kasus: cognitive_domain vs constitutional_domain).
