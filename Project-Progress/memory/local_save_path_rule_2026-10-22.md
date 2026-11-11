# LOKAL SAVE PATH RULE (Mandatory)

**Rule founder (Dhani Yuliawan) 2026-10-22:**

Semua artefak sesi kerja MusGo-OS **wajib** disimpan di:

```
/root/projects/Project-Progress/
├── memory/        # catatan sesi, pembelajaran
├── Knowledge/     # knowledge base, decisions, configs
├── Runtime/       # runtime state
├── State/         # state snapshots
└── *.md           # file log/aturan langsung di root folder ini
```

**Dilarang:**
- ❌ Save ke repo target `/root/Repository MusGo-OS_2in1-main`
- ❌ Save ke path lain di `/root/`

**Alasan:**
- Pemisahan bersih antara workspace blueprint+progress dan repo target produksi
- Agent lain sesi berikutnya bisa langsung `cat /root/projects/Project-Progress/...` untuk grounding
- Tidak ada pencemaran repo target dengan artefak AI agent

## Struktur file aktif (2026-10-22):
- `memory/heartbeat_2026-10-22_0933.md`
- `memory/workspace_2026-10-22_0933.md`
- `memory/local_save_path_rule_2026-10-22.md`
- `Knowledge/workspace_2026-10-22_0933.md`
- `Knowledge/Workspace-File-Index/` (master + 5 area, ter-push juga ke repo workspace)

