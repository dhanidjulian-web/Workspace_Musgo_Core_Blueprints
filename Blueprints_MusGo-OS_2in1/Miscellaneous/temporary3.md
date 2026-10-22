# Buat app android "Ai Chat Coding Assistant".
## Baca:
https://github.com/linux/proot-distro#installation

### Fitur-fitur nya:
Linux Terminal
Sanbox linux Proot/Rootfs Ubuntu/Debian/Kali Net Hunter/.
BYOK. User Add beberapa Ai Provider dan config base url/end point dan mode routing(Auto-free, auto-frontier, auto-small, auto-balance, use only 1 model.
File manager Spec Sanbox-Local storage (import-export, Rename, edit, save, copy, paste, cut, delete, move, new folder, new file, zip-unzip, run/preview, select 1/all, bookmarks)

### UI/UX.
Kolom input user (chat dan terminal) harus selalu berada di atas keyboard
Chat screen(add +files, mic STT)
terminal screen spec
toggle show/hide(chat screen, terminal, files manager, sidebar, Windows).
Buat floating/toggle button. Modul Ai✨Suggest bertugas Scanning dan analisa setiap kolom input text user (kolom chat, command line, form, config, text field, name, title, tag, summarize, description, prompt, dan semua input text). Ai✨Suggest generate context statis/dinamis lalu tampilkan menu dropdown utk di pilih user.
Orchestrator Profile. Template yg bisa di custom dan di gunakan oleh model/Agent dg configurasi:
Pilih mode Routing
Kolom prompt: max 12.000 karakter
Environtment variable: pat token,secret.
Skill: pilih 1-beberapa dr Skill library atau Auto-Selection.
Repos: Pin 1+ Repository
Workflow: alur tugas multi langkah
Connector: pilih 1-beberapa connector yg di gunakan utk eksekusi
Agent Swarm: max 35 agent dg configurasi: nama agent, task, prompt singkat, pilih model/router.
Semua setting, template, modul, configurasi, workflow, library, tools, profile, agent, secret, project, session, bookmarks bisa di manage.

### Kebutuhan UI
Dashboard Utama
Login Default Google app User Profile.
Daftar Fallback Model spec max 15.
Menampilkan status resource (CPU/RAM/Storage) dan status koneksi ke Sandbox.
Profile configurasi workflows untuk Workspace/Project/Orchestrator.
Terminal:
Konsol interaktif untuk menjalankan command line.
File Manager:
Antarmuka untuk mengakses storage (lokal/eksternal) dengan dukungan manajemen all file spec.
Package Manager:
Kolom pencarian untuk menginstal paket secara cepat.
Ai Integration:
Panel untuk input Base Url dan API Key (BYOK) + Test validation, refresh Index Model.
Mode routing Pilih cuma 1 model, Auto/Free, Auto/small, Auto/Balance, Auto/Frontier.
UI Chat/Terminal:
Harus diperhatikan bahwa "Kolom input text/chat/command User Harus Selalu Berada Di Atas Keyboard".
Menghindari Kolom Input Text User terhalangi ketika Keyboard Rise Up.
JANGAN PERNAH GUNAKAN DAN HAPUS SAMPAI BERSIH TAK TERSISA SEMUA MODUL SIMULASI, MOCKUP, DUMMY, FAKE DATA, PLACE HOLDER DAN SEMUA MODUL PALSU DAN PENIPUAN YG TAK REAL DUNIA NYATA.
BERIKAN LOGIKA NYATA, DAN AGENT DI LARANG KERAS MEMBUAT SIMULASI PALSU DG ALASAN DAN KEADAAN APAPUN!!!

---
Sig

---
===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)
🔹Sovereign AI Operating Civilization🔹
🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIG: DHANI YULIAWAN**


## Tolong buatkan struktur desain dashboard yang sangat bersih (Clean neon tech & Dark Mode), fungsional, dan memiliki navigasi yang intuitif untuk alur kerja DevOps profesional.
Built NexusDev - AI Chat Coding Assistant, a native Android DevOps environment built with Kotlin and Jetpack Compose featuring a dark mode aesthetic (Deep Slate, Tech Dark Surface, Cyber Cyan, Neon Emerald, and…

Input user dan Output Agent harus bisa di (Edit, Delete, Copy, Resend/Regenerate, Save/Export, Save Bookmark user input+Agent Output, atau semua input-output dlm satu sesi.

Harus ada daftar session, chat history, bisa buat New Session, hapus session, dan ⭐Bookmarks Manager.

### Ai✨Suggest

Buat floating/toggle button. Ai✨Suggest bertugas mengelola dan bertanggung jawab menghasilkan content & context untuk setiap kolom input text user (kolom chat, command line, form, config, text field, name, title, tag, summarize, description, prompt, translate, suggesti, dan semua tempat input text).

### Ai✨Suggest generate content dan context statis dan dinamis lalu ditampilkan dlm menu dropdown utk di pilih user.

Seharusnya di Integrasikan oleh Model yg aktif/telah di validasi.

Agar lebih menjamin tanpa mengganggu Agent/Model lain, harus buat Spec Configurasi khusus Ai✨Suggests. Seperti add model/provider, hanya saja Ai✨Suggest harus di atur dg menambahkan Prompt khusus, Skill, dan tools External agar hasil sesuai dg context yg diinginkan.

---
Sig

---
===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)
🔹Sovereign AI Operating Civilization🔹
🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIG: DHANI YULIAWAN**

# Main Dashboard

## Home screen: Google login, user profile, fallback model list (max 15), real-time 

### CPU/RAM/Storage status, sandbox connection status, and workflow profile selector for Workspace/Project/Orchestrator.

### Termux Terminal UI
Interactive console for executing command-line operations. Scrollable output, persistent command history, and input bar always pinned above keyboard. Supports multiple terminal sessions.

### Linux Sandbox Manager
UI for managing proot/rootfs Linux sandbox environments (Ubuntu, Debian, Kali NetHunter). Users can select, launch, and switch between distro environments.

### BYOK AI Provider Config
Panel for entering Base URL and API Key per provider, with Test/Validate connection button, Refresh Model Index action, and routing mode selection (Auto-Free, Auto-Frontier, Auto-Small, Auto-Balance, Single Model).

### Sandbox & Local File Manager
Full-featured file manager for sandbox, local, and external storage: import/export, rename, edit, save, copy, paste, cut, delete, move, new folder/file, zip/unzip, run/preview, select one or all, and bookmarks.
Package Manager

### Search-first UI for installing packages into the sandbox environment. Type a package name to search, view details, and install directly — no fake suggestions or simulated results.

### Multi-Panel Toggle UI
Toggle show/hide for Chat, Terminal, File Manager, Sidebar, and Windows panels. Input bar is always rendered above the keyboard using bottom offset — never obscured when keyboard rises.

### AI✨ Suggest Module
Floating/toggle button that scans every text input across the app (chat, command line, form, config, name, title, tag, summarize, description, prompt, translate). Generates static and dynamic context and shows a dropdown of AI-generated suggestions for the user to pick. Has its own dedicated configuration — custom prompt, skill selection, and external tools — isolated from other agents/models. Integrates with the active validated model/provider only.

### Connection / Connector
Login and connect to external providers (Google, GitHub, Vercel, Notion, n8n, and more). Manage active connections and sync external resources inside the app.

### Orchestrator Profile
Customizable agent/model template with routing mode, 12k-char prompt, env variables, skill selection, pinned repos, multi-step workflow, connector selection, and Agent Swarm (max 35 agents, each with name, task, prompt, and model/router config).

### Profile & Asset Manager
Central management hub for all settings, templates, modules, configs, workflows, skill libraries, tools, profiles, agents, secrets, projects, sessions, and bookmarks.
Input & Output Management

### Full control over every chat message: Edit, Delete, Copy, Resend/Regenerate, Save/Export, and Bookmark individual or all input-output pairs in a session. Actions apply per message or to the entire session at once.

### Session & Chat History
List of all sessions with timestamps, open past chat history, create New Session, delete session, and a dedicated ⭐ Bookmarks Manager for starred messages and entire sessions — all managed in one dedicated screen.

### Baca lalu Integrasi dan implementasikan. Jangan install, tapi cukup "Ready To Install" jika user buka app dan klik tombol sanbox yg di pilih memicu sctipts background eksekusi oleh terminal:

https://github.com/linux/proot-distro#installation

### Default Provider:
1. https://api.kilo.ai/api/gateway
2. https://kunciai.id/v1

### Install/Integrasikan/Implementasikan Termux:

https://github.com/linux

### Anjing lu, Goblok 🤬🤬🤬. Ai Provider masih ga respon. Gue bilang apa, setiap Base url dan Api Key harus di Test dan validasi dulu goblok. Nyesel gue milih elu, mendingan Gue pilih Agent yg 1 lagi daripada elu ga becus banyak SIMULASI, MOCKUP, FAKE DATA. TERNYATA MODUL  MODUL DAN FITUR-FITUR ELU MEMANG KHUSUS UNTUK MODUS PENIPUAN KARNA ELU UDAH OVER HALUSINASI🤬

---
Sig

---
===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)
🔹Sovereign AI Operating Civilization🔹
🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIG: DHANI YULIAWAN**

