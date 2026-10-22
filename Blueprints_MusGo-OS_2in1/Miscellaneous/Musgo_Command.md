# 🔹 MusGo-Router Command Reference v1.0.0
**Ai-inside-OS | 2in1 Musyawarah & Gotong-Royong**
**© 2026 — Dhani Yuliawan | All Rights Reserved**

Dokumentasi lengkap semua command Musgo-Router, CLI bawaan, Linux command, dan custom command.

---

## 📋 Daftar Isi
1. [Musgo-Router Core Commands](#musgo-router-core-commands)
2. [Auto Agent CLI Commands](#auto-agent-cli-commands)
3. [Musgo-Agent Commands](#musgo-agent-commands)
4. [Musgo-Credential Commands](#musgo-credential-commands)
5. [AP-Detect & AP-Capability Commands](#ap-detect--ap-capability-commands)
6. [MR / Ask Aliases](#mr--ask-aliases)
6. [Linux System Commands](#linux-system-commands)
7. [Custom Commands & Shortcuts](#custom-commands--shortcuts)
8. [Environment Variables](#environment-variables)
9. [File & Config Locations](#file--config-locations)

---

## 🧠 Musgo-Router Core Commands

**File:** `bin/musgo-router` | **Version:** 2.0.1

### Basic Usage
```bash
musgo-router "tugas Anda"                    # Auto-route + eksekusi
musgo-router --cli codebuddy "tugas"         # Paksa CLI tertentu
musgo-router --model auto "tugas"            # Paksa model FREE
musgo-router --dry-run "tugas"               # Lihat keputusan routing saja
musgo-router --explain "tugas"               # Analisis kategori tugas
```

### Status & Monitoring
```bash
musgo-router status                          # Status CLI agent, model, kredensial
musgo-router models                          # Daftar model dari provider (butuh credential)
musgo-router models-status                   # Status kredensial & cache model
musgo-router log                             # Log router
musgo-router audit                           # Audit anti-simulasi/palsu
```

### Credential Management
```bash
musgo-router credential                      # Simpan base URL + API key
musgo-router credential status               # Cek kredensial (key disembunyikan)
musgo-router credential clear                # Hapus kredensial
```

### Model Management
```bash
musgo-router model-add <nama-model> <kategori> <kemampuan>
# Contoh: musgo-router model-add gemini-2.5-flash text "flash,lite,fast"
```

### Installation
```bash
musgo-router install <npm-package>           # Install CLI agent baru via npm
# Contoh: musgo-router install @tencent-ai/codebuddy-code
```

### Help & Version
```bash
musgo-router help                            # Bantuan lengkap
musgo-router --version                       # Versi router
musgo-router -h                              # Short help
```

### Routing Behavior
| Flag | Fungsi |
|------|--------|
| `--cli <name>` | Paksa gunakan CLI tertentu (codebuddy, gemini, aeon, mi, crush) |
| `--model <name>` | Paksa model (hanya FREE/AUTO yang diterima) |
| `--dry-run` | Tampilkan routing decision tanpa eksekusi |
| `--explain` | Analisis kategori & scoring |
| `MUSGO_MODEL=auto` | Env var untuk paksa model |
| `MUSGO_NOEXEC=1` | Routing saja, tanpa eksekusi |

---

## 🤖 Auto Agent CLI Commands

**File:** `bin/auto-agent` | **Python:** `AgentPool/index/auto_agent_cli.py`

### Agent Management
```bash
# List agents
auto-agent agent list                        # Daftar semua agents
auto-agent agent list --detail               # Dengan detail lengkap
auto-agent agent list --category security    # Filter kategori

# Search agents
auto-agent agent search "security"           # Cari agent

# Add agent
auto-agent agent add "Nama Agent" "Role/Deskripsi" --category security
# Kategori: governance, security, architecture, engineering, ai_ml, devops, quality, general

# Edit agent
auto-agent agent edit <agent_id> --name "Nama Baru" --role "Role Baru" --category governance

# Delete agent
auto-agent agent delete <agent_id>
```

### Skill Management
```bash
# List skills
auto-agent skill list                        # Daftar semua skills
auto-agent skill list --detail               # Dengan detail
auto-agent skill list --category security    # Filter kategori

# Search skills
auto-agent skill search "penetration"        # Cari skill

# Add skill
auto-agent skill add "Nama Skill" "Deskripsi skill" --category security
# Kategori: security, ai_ml, backend, frontend, devops, data, quality, documentation, general

# Edit skill
auto-agent skill edit <skill_id> --name "Nama Baru" --description "Deskripsi Baru" --category ai_ml

# Delete skill
auto-agent skill delete <skill_id>
```

### Config Flags (CRUD)
```bash
# Via Python
from AgentPool.config.config_manager import ConfigManager
cm = ConfigManager()

# Operasi flag
cm.list_flags()                              # Lihat semua flag
cm.get_flag("add")                           # Detail flag add
cm.enable_operation("delete")                # Aktifkan operasi
cm.disable_operation("edit")                 # Nonaktifkan operasi
cm.update_flag("delete", "soft_delete", false)  # Update nilai flag
cm.set_permission("admin", ["add","edit","delete","list","search","config"])
```

### Flag Configuration (flags.yaml)
```yaml
flags:
  add:
    enabled: true
    require_validation: true
    auto_assign_id: true
    backup_before_add: true
  edit:
    enabled: true
    require_backup: true
    validate_before_save: true
  delete:
    enabled: true
    require_confirmation: true
    soft_delete: true
    trash_retention_days: 30
  list:
    enabled: true
    show_details: true
    group_by_category: true
  search:
    enabled: true
    fuzzy_match: true
    case_sensitive: false
permissions:
  admin: [add, edit, delete, list, search, config]
  editor: [add, edit, list, search]
  viewer: [list, search]
```

---

## 🎯 Musgo-Agent Commands

**File:** `bin/musgo-agent`

```bash
musgo-agent list                             # Daftar agent tersedia
musgo-agent run <agent_id> "tugas"           # Jalankan agent spesifik
musgo-agent run --interactive <agent_id>     # Mode interaktif
musgo-agent info <agent_id>                  # Detail agent
musgo-agent create "Nama" "Role" --category  # Buat agent baru (template)
musgo-agent edit <agent_id> --role "..."     # Edit agent
musgo-agent delete <agent_id>                # Hapus agent
```

---

## 🔐 Musgo-Credential Commands

**File:** `bin/musgo-credential`

```bash
musgo-credential                             # Setup interaktif (base URL + API key)
musgo-credential status                      # Tampilkan status (key disamarkan)
musgo-credential clear                       # Hapus credential.env
musgo-credential test                        # Test koneksi ke provider
musgo-credential provider add <name>         # Tambah provider multi
musgo-credential provider list               # Daftar provider
musgo-credential provider remove <name>      # Hapus provider
musgo-credential provider switch <name>      # Ganti provider aktif
```

**File lokasi:** `~/.musgo-router/credential.env`

---

## 🔍 AP-Detect & AP-Capability Commands

### AP-Detect (`bin/ap-detect`)
```bash
ap-detect                                    # Deteksi kapabilitas sistem
ap-detect --full                             # Scan lengkap
ap-detect --json                             # Output JSON
ap-detect --save                             # Simpan ke cache
ap-detect list                               # Daftar deteksi tersimpan
```

### AP-Capability (`bin/ap-capability`)
```bash
ap-capability list                           # Daftar library kapabilitas
ap-capability search "code"                  # Cari kapabilitas
ap-capability info <cap_id>                  # Detail kapabilitas
ap-capability add "name" "desc" --tags       # Tambah kapabilitas
ap-capability edit <cap_id> --tags "..."     # Edit kapabilitas
ap-capability delete <cap_id>                # Hapus kapabilitas
```

---

## 💬 MR / Ask Aliases

Semua alias ini **sama fungsinya** — memanggil `musgo-router` dengan mode `ask` (butuh credential):

```bash
MR: "pertanyaan Anda"        # Format standar Founder
mr: "pertanyaan Anda"        # Lowercase
mr "pertanyaan Anda"         # Tanpa titik dua
mr- "pertanyaan Anda"        # Dengan strip
ask "pertanyaan Anda"        # English alias
```

### MR Special Commands
```bash
MR: --status                 # Status konfigurasi MR
MR: --models                 # Daftar model dari provider
MR: --help                   # Bantuan MR
MR: --model auto "tanya"     # Paksa model auto
```

---

## 🐧 Linux System Commands

### File & Directory
```bash
ls -la                       # List detail + hidden
ls -lh                       # Human readable size
find . -name "*.md"          # Cari file
find . -type f -size +10M    # File > 10MB
du -sh *                     # Ukuran folder
tar -czf backup.tar.gz dir/  # Kompres
tar -xzf backup.tar.gz       # Ekstrak
cp -r src/ dst/              # Copy recursive
mv old new                   # Rename/move
rm -rf folder/               # Hapus recursive
mkdir -p path/to/dir         # Buat folder nested
```

### Permission & Execution
```bash
chmod +x file                # Buat executable
chmod 755 file               # rwxr-xr-x
chmod 644 file               # rw-r--r--
chown user:group file        # Ganti owner
```

### Process & System
```bash
ps aux | grep python         # Cari proses
kill -9 <PID>                # Kill paksa
top / htop                   # Monitor sistem
df -h                        # Disk space
free -h                      # Memory
uptime                       # Uptime server
whoami                       # User saat ini
pwd                          # Current directory
```

### Network
```bash
curl -s url                  # GET request
curl -X POST -d '{}' -H "Content-Type: application/json" url
wget url                     # Download
ping host                    # Test koneksi
netstat -tlnp                # Port listening
ss -tlnp                     # Modern netstat
```

### Text Processing
```bash
grep -r "pattern" .          # Cari recursive
grep -i "pattern" file       # Case insensitive
sed 's/old/new/g' file       # Replace
awk '{print $1}' file        # Kolom 1
cut -d: -f1 file             # Split delimiter
sort file | uniq             # Unique lines
wc -l file                   # Hitung baris
head -20 file                # 20 baris pertama
tail -20 file                # 20 baris terakhir
tail -f file                 # Follow log
```

### Package Management (Termux/Ubuntu/Debian)
```bash
pkg update && pkg upgrade    # Termux
apt update && apt upgrade    # Debian/Ubuntu
pkg install python tar curl jq  # Termux deps
pip install package          # Python package
npm install -g package       # Node global
```

### Archive & Backup
```bash
tar -czf name.tar.gz dir/    # Compress gzip
tar -cjf name.tar.bz2 dir/   # Compress bzip2
tar -xzf name.tar.gz         # Extract gzip
tar -tvf name.tar.gz         # List isi tanpa ekstrak
zip -r name.zip dir/         # Zip
unzip name.zip               # Unzip
```

---

## ⚡ Custom Commands & Shortcuts

### Shortcut Aliases (Tambah ke ~/.bashrc)
```bash
# MusGo shortcuts
alias mr='musgo-router'
alias mra='musgo-router --cli aeon'
alias mrg='musgo-router --cli gemini'
alias mrc='musgo-router --cli codebuddy'
alias maa='auto-agent'
alias maa-agent='auto-agent agent'
alias maa-skill='auto-agent skill'
alias mcred='musgo-credential'
alias magent='musgo-agent'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline -10'
alias gd='git diff'

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# System
alias ports='ss -tlnp'
alias myip='curl -s ifconfig.me'
alias disk='df -h'
alias mem='free -h'
```

### Custom Functions (Tambah ke ~/.bashrc)
```bash
# Quick ask MusGo
mra() { musgo-router --cli aeon "$*"; }
mrg() { musgo-router --cli gemini "$*"; }
mrc() { musgo-router --cli codebuddy "$*"; }

# Auto agent shortcuts
aa-add() { auto-agent agent add "$1" "$2" --category "${3:-general}"; }
aa-search() { auto-agent agent search "$1"; }
as-add() { auto-agent skill add "$1" "$2" --category "${3:-general}"; }
as-search() { auto-agent skill search "$1"; }

# Project nav
mcd() { cd /data/user/0/com.openshell/files/home/Musgo-OS_2in1/Musgo-Router; }
mhome() { cd /data/user/0/com.openshell/files/home; }

# Package rebuild
mpkg() {
  cd /data/user/0/com.openshell/files/home/Musgo-OS_2in1/Musgo-Router
  bash package.sh
}

# Install & test
minstall() {
  cd /data/user/0/com.openshell/files/home/Musgo-OS_2in1/Musgo-Router
  bash install.sh
}
```

---

## 🌍 Environment Variables

| Variable | Default | Deskripsi |
|----------|---------|-----------|
| `MUSGO_MODEL` | `gemini-2.5-flash` | Paksa model (hanya FREE/AUTO) |
| `MUSGO_NOEXEC` | `0` | `1` = routing saja, tidak eksekusi |
| `MUSGO_BASE_URL` | - | Base URL provider (dari credential) |
| `MUSGO_API_KEY` | - | API Key provider (dari credential) |
| `HOME` | - | Home directory (config di `$HOME/.musgo-router`) |
| `PREFIX` | - | Termux prefix (symlink CLI) |
| `TMPDIR` | `/tmp` | Temp directory |

### Model yang Diizinkan (FREE ONLY)
```bash
export MUSGO_MODEL=gemini-2.5-flash      # T1-FREE
export MUSGO_MODEL=gemini-2.5-flash-lite # T1-FREE
export MUSGO_MODEL=gemini-2.0-flash      # T1-FREE
export MUSGO_MODEL=auto                  # T2-AUTO-FREE (router pilih)
# PAID MODEL DITOLAK OTOMATIS
```

---

## 📁 File & Config Locations

### Project Structure
```
/data/user/0/com.openshell/files/home/Musgo-OS_2in1/Musgo-Router/
├── bin/
│   ├── musgo-router          # Core router
│   ├── auto-agent            # Auto agent CLI
│   ├── musgo-agent           # Agent executor
│   ├── musgo-credential      # Credential manager
│   ├── ap-detect             # Capability detector
│   ├── ap-capability         # Capability library
│   ├── mr                    # Alias MR
│   ├── mr_                   # Alias MR
│   ├── mr-                   # Alias MR
│   └── mr-key                # Key helper
│
├── AgentPool/
│   ├── index/
│   │   ├── agent_index.py    # Agent search engine
│   │   ├── skill_index.py    # Skill search engine
│   │   ├── auto_agent.py     # Orchestrator
│   │   ├── auto_agent_cli.py # CLI logic
│   │   ├── agents_index.json # 103 agents registry
│   │   └── skills_index.json # 40 skills registry
│   ├── config/
│   │   ├── auto_agent.yaml   # Auto agent behavior
│   │   ├── flags.yaml        # CRUD flags
│   │   └── config_manager.py # Flag controller
│   ├── agents/               # 103 agent definitions (.md)
│   ├── skills/               # 40 skill collections
│   ├── cache/                # AI model/provider indices
│   ├── personas/             # Agent personalities
│   └── providers/            # API provider configs
│
├── install.sh                # Installer
├── package.sh                # Package builder
├── README.md                 # Documentation
├── Musgo_Command.md          # This file
├── Musgo-Router_index.md     # Project manifest
├── MusGo.json                # System config
├── AGENTS.md                 # Agent docs
├── mr-routing.md             # Routing docs
└── MusGo-Router_v1.0.0.tar.gz # Distribution package
```

### Runtime Config (User Directory)
```
~/.musgo-router/
├── credential.env            # Base URL + API Key (hidden)
├── router.log                # Router logs
├── history.log               # Command history
├── .models.cache             # Model list cache (5 min TTL)
└── providers/                # Multi-provider .env files
    ├── provider1.env
    └── provider2.env
```

---

## 🎯 Quick Reference Card

| Task | Command |
|------|---------|
| Tanya AI cepat | `MR: "pertanyaan"` |
| Status sistem | `musgo-router status` |
| Lihat model provider | `musgo-router models` |
| Setup API key | `musgo-credential` |
| Kelola agent | `auto-agent agent list/add/edit/delete` |
| Kelola skill | `auto-agent skill list/add/edit/delete` |
| Install CLI baru | `musgo-router install @pkg/name` |
| Audit keamanan | `musgo-router audit` |
| Build paket | `bash package.sh` |
| Install ulang | `bash install.sh` |

---

## 🔐 Founder Notes

> **ATURAN MUTLAK:**
> 1. Hanya model **FREE/AUTO** yang diperbolehkan
> 2. Tidak ada simulasi/mock/fake data — guard anti-penipuan aktif
> 3. Semua output harus jujur (error provider ditampilkan apa adanya)
> 4. Auto-retry ke model alternatif saat limit/error
> 5. Credential tidak pernah di-log penuh (hanya 4 karakter pertama)

---

===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)
🔹Sovereign AI Operating Civilization🔹
🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIGN: DHANI YULIAWAN**