hermes-agentAgent:

https://hermes-agent.nousresearch.com/docs/

https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

---
===========🔐™️®️©️🔐===========

README.md

```
Agen Hermes ☤
Dokumentasi Perselisihan Lisensi: MIT Dibuat oleh Nous Research tid

Agen AI yang terus berkembang sendiri yang dibangun oleh Nous Research . Ini adalah satu-satunya agen dengan siklus pembelajaran bawaan — ia menciptakan keterampilan dari pengalaman, meningkatkannya selama penggunaan, mendorong dirinya sendiri untuk mempertahankan pengetahuan, mencari percakapan masa lalunya sendiri, dan membangun model yang semakin mendalam tentang siapa Anda di berbagai sesi. Jalankan di VPS seharga $5, klaster GPU, atau infrastruktur tanpa server yang hampir tidak memerlukan biaya saat tidak aktif. Ia tidak terikat pada laptop Anda — ajak bicara melalui Telegram sementara ia bekerja di VM cloud.

Gunakan model apa pun yang Anda inginkan — Nous Portal , OpenRouter (200+ model), NovitaAI (cloud berbasis AI untuk Model API, Agent Sandbox, dan GPU Cloud), NVIDIA NIM (Nemotron), Xiaomi MiMo , z.ai/GLM , Kimi/Moonshot , MiniMax , Hugging Face , OpenAI, atau endpoint Anda sendiri. Beralihlah dengan mudah hermes model— tanpa perubahan kode, tanpa ketergantungan pada satu vendor.

Antarmuka terminal sungguhan	TUI (Tuned User Interface) lengkap dengan pengeditan multi-baris, pelengkapan otomatis perintah garis miring, riwayat percakapan, interupsi dan pengalihan, serta output alat streaming.
Tinggal di tempat Anda tinggal	Telegram, Discord, Slack, WhatsApp, Signal, dan CLI — semuanya dari satu proses gateway tunggal. Transkripsi memo suara, kontinuitas percakapan lintas platform.
Siklus pembelajaran tertutup	Memori yang dikelola agen dengan dorongan berkala. Penciptaan keterampilan otonom setelah tugas-tugas kompleks. Keterampilan meningkat sendiri selama penggunaan. Pencarian sesi FTS5 dengan ringkasan LLM untuk mengingat kembali lintas sesi. Pemodelan pengguna dialektika Honcho . Kompatibel dengan standar terbuka agentskills.io .
Otomatisasi terjadwal	Penjadwal cron bawaan dengan pengiriman ke platform apa pun. Laporan harian, pencadangan malam, audit mingguan — semuanya dalam bahasa alami, berjalan tanpa pengawasan.
Mendelegasikan dan memparalelkan	Buat subagen terisolasi untuk alur kerja paralel. Tulis skrip Python yang memanggil alat melalui RPC, merampingkan alur kerja multi-langkah menjadi putaran tanpa biaya konteks.
Dapat dijalankan di mana saja, bukan hanya di laptop Anda.	Tujuh backend terminal — lokal, Docker, SSH, Singularity, Modal, Daytona, dan Vercel Sandbox. Daytona dan Modal menawarkan persistensi tanpa server — lingkungan agen Anda akan hibernasi saat tidak aktif dan bangun sesuai permintaan, dengan biaya hampir nol di antara sesi. Jalankan di VPS seharga $5 atau klaster GPU.
Siap untuk penelitian	Pembuatan lintasan secara batch, kompresi lintasan untuk melatih generasi model pemanggilan alat berikutnya.
Instalasi Cepat
Linux, macOS, WSL2, Termux
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
Windows (asli, PowerShell) — Beta Awal
Perhatian: Dukungan Windows asli masih dalam versi beta awal . Instalasi dan pengoperasiannya berhasil, tetapi belum diuji secara luas seperti jalur Linux/macOS/WSL2 kami. Mohon laporkan masalah jika Anda menemukan kendala. Untuk pengaturan Windows yang paling teruji saat ini, jalankan perintah satu baris Linux/macOS di atas di dalam WSL2 .

Jalankan perintah ini di PowerShell:

iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
Installer menangani semuanya: uv, Python 3.11, Node.js, ripgrep, ffmpeg, dan Git Bash portabel (MinGit, diekstrak ke %LOCALAPPDATA%\hermes\git— tidak memerlukan hak administrator, sepenuhnya terisolasi dari instalasi Git sistem apa pun). Hermes menggunakan Git Bash yang disertakan ini untuk menjalankan perintah shell.

Jika Anda sudah memasang Git, penginstal akan mendeteksinya dan menggunakannya sebagai gantinya. Jika tidak, Anda hanya perlu mengunduh MinGit sekitar 45MB — ini tidak akan menyentuh atau mengganggu Git sistem apa pun.

Android / Termux: Jalur manual yang telah diuji didokumentasikan dalam panduan Termux . Di Termux, Hermes menginstal .[termux]extra pilihan karena .[all]extra lengkap saat ini menarik dependensi suara yang tidak kompatibel dengan Android.

Windows: Windows asli didukung sebagai versi beta awal — perintah PowerShell satu baris di atas menginstal semuanya, tetapi harap perhatikan bahwa mungkin ada beberapa kekurangan dan harap laporkan masalah jika Anda menemukannya. Jika Anda lebih suka menggunakan WSL2 (jalur Windows kami yang paling teruji), perintah Linux juga berfungsi di sana. Instalasi Windows asli berada di bawah %LOCALAPPDATA%\hermes; WSL2 diinstal di bawah ~/.hermesseperti pada Linux. Satu-satunya fitur Hermes yang saat ini membutuhkan WSL2 secara khusus adalah panel obrolan dasbor berbasis browser (fitur ini menggunakan POSIX PTY — CLI klasik dan gateway keduanya berjalan secara native).

Setelah instalasi:

source ~/.bashrc    # reload shell (or: source ~/.zshrc)
hermes              # start chatting!
Memulai
hermes              # Interactive CLI — start a conversation
hermes model        # Choose your LLM provider and model
hermes tools        # Configure which tools are enabled
hermes config set   # Set individual config values
hermes gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup        # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update       # Update to the latest version
hermes doctor       # Diagnose any issues
📖 Dokumentasi lengkap →

Lewati pengumpulan kunci API — Nous Portal
Hermes bekerja dengan penyedia mana pun yang Anda inginkan — itu tidak akan berubah. Tetapi jika Anda lebih memilih untuk tidak mengumpulkan lima kunci API terpisah untuk model, pencarian web, pembuatan gambar, TTS, dan peramban cloud, Nous Portal mencakup semuanya dalam satu langganan:

Lebih dari 300 model — pilih salah satunya dengan/model <name>
Tool Gateway — pencarian web (Firecrawl), pembuatan gambar (FAL), teks ke ucapan (OpenAI), peramban cloud (Penggunaan Peramban), semuanya dialihkan melalui langganan Anda. Tidak perlu akun tambahan.
Satu perintah dari instalasi baru:

hermes setup --portal
Itu akan membuat Anda masuk melalui OAuth, mengatur Nous sebagai penyedia Anda, dan mengaktifkan Tool Gateway. Periksa apa yang terhubung kapan saja dengan perintah ` hermes portal status. Detail lengkapnya ada di halaman dokumentasi Tool Gateway .

Anda masih dapat membawa kunci Anda sendiri per-alat kapan pun Anda mau — gateway berlaku per-backend, bukan semuanya atau tidak sama sekali.

Referensi Singkat CLI vs Messaging
Hermes memiliki dua titik masuk: mulai UI terminal dengan hermes, atau jalankan gateway dan berkomunikasi dengannya dari Telegram, Discord, Slack, WhatsApp, Signal, atau Email. Setelah Anda berada dalam percakapan, banyak perintah slash yang sama digunakan di kedua antarmuka.

Tindakan	CLI	Platform perpesanan
Mulai mengobrol	hermes	Jalankan hermes gateway setup+ hermes gateway start, lalu kirim pesan ke bot.
Mulailah percakapan baru.	/newatau/reset	/newatau/reset
Ubah model	/model [provider:model]	/model [provider:model]
Tetapkan kepribadian	/personality [name]	/personality [name]
Coba lagi atau batalkan giliran terakhir	/retry,/undo	/retry,/undo
Kompres konteks / periksa penggunaan	/compress, /usage,/insights [--days N]	/compress, /usage,/insights [days]
Jelajahi keterampilan	/skillsatau/<skill-name>	/<skill-name>
Hentikan pekerjaan yang sedang berlangsung	Ctrl+Catau kirim pesan baru	/stopatau kirim pesan baru
Status khusus platform	/platforms	/status,/sethome
Untuk daftar perintah lengkap, lihat panduan CLI dan panduan Messaging Gateway .

Dokumentasi
Semua dokumentasi tersedia di hermes-agent.nousresearch.com/docs :

Bagian	Apa yang Dicakup
Panduan Singkat	Instal → pengaturan → percakapan pertama dalam 2 menit
Penggunaan CLI	Perintah, pintasan keyboard, kepribadian, sesi
Konfigurasi	File konfigurasi, penyedia, model, semua opsi.
Gerbang Pesan	Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant
Keamanan	Persetujuan perintah, pemasangan DM, isolasi kontainer
Peralatan & Perlengkapan	40+ alat, sistem perangkat alat, backend terminal
Sistem Keterampilan	Memori prosedural, Pusat Keterampilan, menciptakan keterampilan
Ingatan	Memori persisten, profil pengguna, praktik terbaik
Integrasi MCP	Hubungkan server MCP mana pun untuk kemampuan yang lebih luas.
Penjadwalan Cron	Tugas terjadwal dengan pengiriman platform.
Berkas Konteks	Konteks proyek yang membentuk setiap percakapan
Arsitektur	Struktur proyek, siklus agen, kelas-kelas kunci
Berkontribusi	Pengaturan pengembangan, proses PR, gaya penulisan kode
Referensi CLI	Semua perintah dan bendera
Variabel Lingkungan	Referensi variabel lingkungan lengkap
Migrasi dari OpenClaw
Jika Anda berasal dari OpenClaw, Hermes dapat secara otomatis mengimpor pengaturan, memori, keterampilan, dan kunci API Anda.

Selama pengaturan pertama kali: Panduan pengaturan ( hermes setup) secara otomatis mendeteksi ~/.openclawdan menawarkan migrasi sebelum konfigurasi dimulai.

Kapan saja setelah instalasi:

hermes claw migrate              # Interactive migration (full preset)
hermes claw migrate --dry-run    # Preview what would be migrated
hermes claw migrate --preset user-data   # Migrate without secrets
hermes claw migrate --overwrite  # Overwrite existing conflicts
Apa yang diimpor:

SOUL.md — berkas persona
Kenangan — entri MEMORY.md dan USER.md
Keterampilan — keterampilan yang dibuat pengguna →~/.hermes/skills/openclaw-imports/
Daftar perintah yang diizinkan — pola persetujuan
Pengaturan perpesanan — konfigurasi platform, pengguna yang diizinkan, direktori kerja
Kunci API — rahasia yang diizinkan (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
Aset TTS — file audio ruang kerja
Instruksi ruang kerja — AGENTS.md (dengan --workspace-target)
Lihat hermes claw migrate --helpsemua opsi, atau gunakan openclaw-migrationfitur ini untuk migrasi interaktif yang dipandu agen dengan pratinjau uji coba.

Berkontribusi
Kami menerima kontribusi! Lihat Panduan Kontribusi untuk pengaturan pengembangan, gaya penulisan kode, dan proses permintaan pull (PR).

Panduan cepat untuk kontributor — klon dan langsung jalankan setup-hermes.sh:

git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
./setup-hermes.sh     # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/hermes
./hermes              # auto-detects the venv, no need to `source` first
Jalur manual (setara dengan di atas):

curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
Masyarakat
💬 Discord
📚 Pusat Keterampilan
🐛 Masalah
🔌 computer-use-linux — Server MCP pengontrol desktop Linux untuk Hermes dan host MCP lainnya, dengan pohon aksesibilitas AT-SPI, input Wayland/X11, tangkapan layar, dan penargetan jendela komposer.
🔌 HermesClaw — Jembatan WeChat Komunitas: Jalankan Hermes Agent dan OpenClaw di akun WeChat yang sama.
Lisensi
MIT — lihat LICENSE .
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Panduan Singkat
Panduan ini akan membawa Anda dari nol hingga memiliki pengaturan Hermes yang berfungsi dan tahan lama dalam penggunaan nyata. Instal, pilih penyedia, verifikasi obrolan yang berfungsi, dan ketahui persis apa yang harus dilakukan jika terjadi masalah.

Lebih suka menonton?
Onchain AI Garage telah menyusun panduan Masterclass tentang instalasi, pengaturan, dan perintah dasar — ​​pelengkap yang bagus untuk halaman ini jika Anda lebih suka mengikuti melalui video. Untuk informasi lebih lanjut, lihat daftar putar Tutorial & Kasus Penggunaan Agen Hermes selengkapnya .


Untuk siapa ini
Benar-benar baru dan ingin jalur tercepat menuju pengaturan yang berfungsi.
Beralih penyedia layanan dan tidak ingin membuang waktu karena kesalahan konfigurasi.
Mengatur Hermes untuk tim, bot, atau alur kerja yang selalu aktif.
Bosan dengan masalah "sudah terpasang, tapi tetap tidak berfungsi"?
Jalur tercepat
Pilih baris yang sesuai dengan tujuan Anda:

Sasaran	Lakukan ini terlebih dahulu	Kemudian lakukan ini
Saya hanya ingin Hermes berfungsi di mesin saya.	hermes setup	Lakukan obrolan sungguhan dan verifikasi apakah ada respons.
Saya sudah mengenal penyedia layanan saya.	hermes model	Simpan konfigurasi, lalu mulailah mengobrol.
Saya menginginkan bot atau pengaturan yang selalu aktif.	hermes gateway setupsetelah CLI berfungsi	Hubungkan Telegram, Discord, Slack, atau platform lainnya.
Saya menginginkan model lokal atau yang dihosting sendiri.	hermes model→ titik akhir khusus	Verifikasi endpoint, nama model, dan panjang konteks.
Saya menginginkan opsi cadangan multi-penyedia.	hermes modelPertama	Tambahkan perutean dan mekanisme cadangan hanya setelah obrolan dasar berfungsi.
Aturan praktis: jika Hermes tidak dapat menyelesaikan obrolan normal, jangan tambahkan fitur lain dulu. Buat satu percakapan yang bersih berfungsi terlebih dahulu, kemudian tambahkan gateway, cron, skill, suara, atau routing.

1. Instal Agen Hermes
Opsi A — pip (paling sederhana):

pip install hermes-agent
hermes postinstall     # optional: installs Node.js, browser, ripgrep, ffmpeg + runs setup


Rilis PyPI melacak versi yang diberi tag (rilis utama/minor), bukan setiap commit pada main. Untuk versi terbaru, gunakan Opsi B.

Opsi B — git installer (melacak cabang utama):

# Linux / macOS / WSL2 / Android (Termux)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash


Android / Termux
Jika Anda menginstal di ponsel, lihat panduan Termux khusus untuk jalur manual yang telah diuji, fitur tambahan yang didukung, dan batasan khusus Android saat ini.

Pengguna Windows
Instal WSL2 terlebih dahulu, kemudian jalankan perintah di atas di dalam terminal WSL2 Anda.

Setelah selesai, muat ulang shell Anda:

source ~/.bashrc   # or source ~/.zshrc


Untuk opsi instalasi, prasyarat, dan pemecahan masalah yang lebih detail, lihat panduan instalasi .

2. Pilih Penyedia Layanan
Langkah pengaturan terpenting. Gunakan hermes modeluntuk menelusuri pilihan secara interaktif:

hermes model

Jalur termudah: Portal Nous
Satu langganan mencakup 300+ model ditambah Tool Gateway (pencarian web, pembuatan gambar, TTS, peramban cloud). Pada instalasi baru:

hermes setup --portal

Itu akan membuat Anda masuk, mengatur Nous sebagai penyedia layanan Anda, dan mengaktifkan Tool Gateway dalam satu perintah.

Pengaturan default yang baik:

Penyedia	Apa itu	Cara mengatur
Portal Nous	Berbasis langganan, tanpa konfigurasi.	Login OAuth melaluihermes model
Kodeks OpenAI	ChatGPT OAuth, menggunakan model Codex.	Otentikasi kode perangkat melaluihermes model
Antropis	Model Claude secara langsung — Paket Max + kredit penggunaan tambahan (OAuth), atau kunci API untuk pembayaran per token.	hermes model→ Login OAuth (membutuhkan Max + kredit tambahan), atau kunci API Anthropic
OpenRouter	Perutean multi-penyedia di berbagai model	Masukkan kunci API Anda
Z.AI	Model yang dihosting oleh GLM/Zhipu	Mengatur GLM_API_KEY/ZAI_API_KEY
Kimi / Moonshot	Model pengkodean dan obrolan yang dihosting oleh Moonshot	Set KIMI_API_KEY(atau yang spesifik untuk Kimi-Coding KIMI_CODING_API_KEY)
Kimi / Moonshot China	Titik akhir Moonshot wilayah Tiongkok	MengaturKIMI_CN_API_KEY
Arcee AI	Model Trinity	MengaturARCEEAI_API_KEY
GMI Cloud	API langsung multi-model	MengaturGMI_API_KEY
MiniMax (OAuth)	MiniMax-M2.7 melalui OAuth browser — tidak memerlukan kunci API.	hermes model→ MiniMax (OAuth)
MiniMax	Titik akhir MiniMax internasional	MengaturMINIMAX_API_KEY
MiniMax China	Titik akhir MiniMax wilayah Tiongkok	MengaturMINIMAX_CN_API_KEY
Alibaba Cloud	Model Qwen melalui DashScope	MengaturDASHSCOPE_API_KEY
Wajah yang Memeluk	20+ model terbuka melalui router terpadu (Qwen, DeepSeek, Kimi, dll.)	MengaturHF_TOKEN
AWS Bedrock	Claude, Nova, Llama, DeepSeek melalui API Converse asli	Peran IAM atau aws configure( panduan )
Kode Kilogram	Model yang dihosting oleh KiloCode	MengaturKILOCODE_API_KEY
Kode Terbuka Zen	Akses bayar per penggunaan ke model-model pilihan.	MengaturOPENCODE_ZEN_API_KEY
Kode Terbuka Go	Langganan $10/bulan untuk model terbuka	MengaturOPENCODE_GO_API_KEY
DeepSeek	Akses API DeepSeek langsung	MengaturDEEPSEEK_API_KEY
NVIDIA NIM	Model Nemotron tersedia melalui build.nvidia.com atau NIM lokal.	Atur NVIDIA_API_KEY(opsional: NVIDIA_BASE_URL)
Rekan Kerja GitHub	Langganan GitHub Copilot (GPT-5.x, Claude, Gemini, dll.)	OAuth melalui hermes model, atau COPILOT_GITHUB_TOKEN/GH_TOKEN
GitHub Copilot ACP	Backend agen Copilot ACP (meluncurkan copilotCLI lokal)	hermes model(membutuhkan copilotCLI + copilot login)
Gerbang AI Vercel	Perutean Vercel AI Gateway	MengaturAI_GATEWAY_API_KEY
Titik Akhir Kustom	VLLM, SGLang, Ollama, atau API apa pun yang kompatibel dengan OpenAI.	Tetapkan URL dasar + kunci API
Bagi sebagian besar pengguna baru: pilih penyedia, terima pengaturan default kecuali Anda tahu mengapa Anda mengubahnya. Katalog penyedia lengkap dengan variabel lingkungan dan langkah-langkah penyiapan terdapat di halaman Penyedia .

Konteks minimum: 64.000 token
Hermes Agent membutuhkan model dengan setidaknya 64.000 token konteks. Model dengan jendela yang lebih kecil tidak dapat mempertahankan memori kerja yang cukup untuk alur kerja pemanggilan alat multi-langkah dan akan ditolak saat startup. Sebagian besar model yang dihosting (Claude, GPT, Gemini, Qwen, DeepSeek) dengan mudah memenuhi persyaratan ini. Jika Anda menjalankan model lokal, atur ukuran konteksnya minimal 64K (misalnya --ctx-size 65536untuk llama.cpp atau -c 65536untuk Ollama).

tip
Anda dapat beralih penyedia kapan saja tanpa hermes modelterikat kontrak. Untuk daftar lengkap semua penyedia yang didukung dan detail pengaturan, lihat Penyedia AI .

Bagaimana pengaturan disimpan
Hermes memisahkan rahasia dari konfigurasi normal:

Rahasia dan token →~/.hermes/.env
Pengaturan non-rahasia →~/.hermes/config.yaml
Cara termudah untuk mengatur nilai dengan benar adalah melalui CLI:

hermes config set model anthropic/claude-opus-4.6
hermes config set terminal.backend docker
hermes config set OPENROUTER_API_KEY sk-or-...


Nilai yang tepat akan masuk ke file yang tepat secara otomatis.

3. Jalankan Obrolan Pertama Anda
hermes            # classic CLI
hermes --tui      # modern TUI (recommended)


Anda akan melihat banner selamat datang dengan model Anda, alat yang tersedia, dan keterampilan. Gunakan petunjuk yang spesifik dan mudah diverifikasi:

Pilih antarmuka Anda
Hermes hadir dengan dua antarmuka terminal: CLI klasik prompt_toolkitdan TUI yang lebih baru dengan overlay modal, pemilihan mouse, dan input non-blokir. Keduanya berbagi sesi, perintah slash, dan konfigurasi yang sama — coba masing-masing dengan hermes`vs` hermes --tui.

Summarize this repo in 5 bullets and tell me what the main entrypoint is.


Check my current directory and tell me what looks like the main project file.


Help me set up a clean GitHub PR workflow for this codebase.


Seperti apa kesuksesan itu:

Banner tersebut menampilkan model/penyedia yang Anda pilih.
Hermes menjawab tanpa kesalahan
Dapat menggunakan alat bantu jika diperlukan (terminal, pembacaan file, pencarian web)
Percakapan berlanjut secara normal selama lebih dari satu giliran.
Jika itu berhasil, berarti Anda sudah melewati bagian tersulit.

4. Verifikasi Sesi Berfungsi
Sebelum melanjutkan, pastikan resume Anda berfungsi:

hermes --continue    # Resume the most recent session
hermes -c            # Short form


Itu seharusnya membawa Anda kembali ke sesi yang baru saja Anda lakukan. Jika tidak, periksa apakah Anda berada di profil yang sama dan apakah sesi tersebut benar-benar tersimpan. Ini penting nanti ketika Anda mengelola beberapa pengaturan atau mesin sekaligus.

5. Coba Fitur Utama
Gunakan terminal
❯ What's my disk usage? Show the top 5 largest directories.


Agen tersebut menjalankan perintah terminal atas nama Anda dan menampilkan hasilnya.

Perintah garis miring
Ketik /untuk melihat daftar pilihan otomatis semua perintah:

Memerintah	Apa fungsinya?
/help	Tampilkan semua perintah yang tersedia
/tools	Daftar alat yang tersedia
/model	Beralih antar model secara interaktif
/personality pirate	Cobalah kepribadian yang menyenangkan.
/save	Simpan percakapan ini
Input multi-baris
Tekan Alt+Enter, Ctrl+J, atau Shift+Enteruntuk menambahkan baris baru. Shift+Entermemerlukan terminal yang mengirimkannya sebagai urutan yang berbeda (Kitty / foot / WezTerm / Ghostty secara default; iTerm2 / Alacritty / terminal VS Code setelah protokol keyboard Kitty diaktifkan). Alt+Enterdan Ctrl+Jberfungsi di setiap terminal.

Sela agen tersebut
Jika agen terlalu lama merespons, ketik pesan baru dan tekan Enter — ini akan menghentikan tugas yang sedang berjalan dan beralih ke instruksi baru Anda. Ctrl+Cjuga berfungsi.

6. Tambahkan Lapisan Berikutnya
Hanya setelah obrolan utama berfungsi. Pilih yang Anda butuhkan:

Bot atau asisten bersama
hermes gateway setup    # Interactive platform configuration


Hubungkan Telegram , Discord , Slack , WhatsApp , Signal , Email , atau Home Assistant , atau Microsoft Teams .

Otomatisasi dan alat
hermes tools— menyesuaikan akses alat per platform
hermes skills— menelusuri dan menginstal alur kerja yang dapat digunakan kembali
Cron — hanya setelah pengaturan bot atau CLI Anda stabil.
Terminal terisolasi (sandboxed terminal)
Demi keamanan, jalankan agen di dalam kontainer Docker atau di server jarak jauh:

hermes config set terminal.backend docker    # Docker isolation
hermes config set terminal.backend ssh       # Remote server


Mode suara
# From the Hermes install directory (the curl installer placed it at
# ~/.hermes/hermes-agent on Linux/macOS or %LOCALAPPDATA%\hermes\hermes-agent on Windows):
cd ~/.hermes/hermes-agent
uv pip install -e ".[voice]"
# Includes faster-whisper for free local speech-to-text


Kemudian di CLI: /voice on. Tekan Ctrl+Buntuk merekam. Lihat Mode Suara .

Keterampilan
hermes skills search kubernetes
hermes skills install openai/skills/k8s


Atau gunakan /skillsdi dalam sesi obrolan.

Server MCP
# Add to ~/.hermes/config.yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxx"


Integrasi editor (ACP)
Dukungan ACP sudah termasuk dalam paket tambahan standar [all], jadi penginstal curl sudah menyertakannya. Cukup jalankan:

hermes acp

(Jika Anda menginstal tanpa [all], jalankan cd ~/.hermes/hermes-agent && uv pip install -e ".[acp]"terlebih dahulu.)

Lihat Integrasi Editor ACP .

Modus Kegagalan Umum
Berikut adalah masalah-masalah yang paling banyak membuang waktu:

Gejala	Kemungkinan penyebab	Memperbaiki
Hermes membuka pintu tetapi memberikan jawaban kosong atau tidak jelas.	Otorisasi penyedia atau pemilihan model salah.	Jalankan hermes modellagi dan konfirmasikan penyedia, model, dan otentikasi.
Endpoint kustom "berfungsi" tetapi mengembalikan data yang tidak valid.	URL dasar, nama model, atau sebenarnya tidak kompatibel dengan OpenAI salah.	Verifikasi endpoint di klien terpisah terlebih dahulu.
Gateway aktif tetapi tidak ada yang bisa mengirim pesan ke gateway tersebut.	Token bot, daftar yang diizinkan, atau pengaturan platform belum lengkap.	Jalankan ulang hermes gateway setupdan periksahermes gateway status
hermes --continueTidak dapat menemukan sesi lama.	Berganti profil atau sesi tidak pernah tersimpan	Periksa hermes sessions listdan pastikan Anda berada di profil yang tepat.
Model tidak tersedia atau perilaku fallback yang aneh.	Pengaturan perutean atau cadangan penyedia terlalu agresif.	Tetap matikan perutean sampai penyedia layanan utama stabil.
hermes doctormasalah konfigurasi bendera	Nilai konfigurasi hilang atau sudah usang.	Perbaiki konfigurasi, uji ulang obrolan biasa sebelum menambahkan fitur.
Perangkat Pemulihan
Jika ada sesuatu yang terasa tidak beres, gunakan urutan ini:

hermes doctor
hermes model
hermes setup
hermes sessions list
hermes --continue
hermes gateway status
Urutan tersebut akan membawa Anda dari "suasana yang kacau" kembali ke keadaan yang stabil dengan cepat.

Referensi Cepat
Memerintah	Keterangan
hermes	Mulai mengobrol
hermes model	Pilih penyedia dan model LLM Anda.
hermes tools	Konfigurasikan alat mana yang diaktifkan per platform.
hermes setup	Panduan pengaturan lengkap (mengonfigurasi semuanya sekaligus)
hermes doctor	Mendiagnosis masalah
hermes update	Perbarui ke versi terbaru
hermes gateway	Mulai gerbang pesan
hermes --continue	Lanjutkan sesi terakhir
Langkah Selanjutnya
Panduan CLI — Kuasai antarmuka terminal
Konfigurasi — Sesuaikan pengaturan Anda
Gateway Perpesanan — Hubungkan Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant, Teams, dan banyak lagi
Alat & Perangkat — Jelajahi kemampuan yang tersedia
Penyedia AI — Daftar lengkap penyedia dan detail pengaturan
Sistem Keterampilan — Alur kerja dan pengetahuan yang dapat digunakan kembali
Tips & Praktik Terbaik — Tips untuk pengguna tingkat lanjut
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Instalasi
Instal dan jalankan Hermes Agent dalam waktu kurang dari dua menit dengan penginstal satu baris.

Instalasi Cepat
Penginstal Satu Baris (Linux / macOS / WSL2)
Untuk instalasi berbasis Git yang melacak maindan memberikan perubahan terbaru secara langsung:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash


Windows (asli, PowerShell) — Beta Awal
Versi BETA awal
Dukungan native Windows masih dalam versi beta awal . Instalasinya berhasil dan berfungsi untuk jalur umum, tetapi belum diuji secara luas seperti installer POSIX kami. Silakan laporkan masalah jika Anda menemukan kendala. Untuk pengaturan yang paling teruji di Windows saat ini, gunakan perintah satu baris Linux/macOS di atas di dalam WSL2 sebagai gantinya.

Buka PowerShell dan jalankan perintah berikut:

iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)


Installer menangani semuanya : uvPython 3.11, Node.js 22, ripgrepdan ffmpegGit Bash portabel (PortableGit — distribusi Git-for-Windows mandiri yang menyertakan bash.exetoolchain POSIX lengkap yang digunakan Hermes untuk perintah shell; pada Windows 32-bit, installer akan kembali ke MinGit, yang tidak memiliki bash dan menonaktifkan fitur terminal-tool/agent-browser). Installer akan mengkloning repositori di bawah %LOCALAPPDATA%\hermes\hermes-agent, membuat virtualenv, dan menambahkannya hermeske PATH pengguna Anda . Restart terminal Anda (atau buka jendela PowerShell baru) setelah instalasi agar PATH berfungsi.

Cara penggunaan Git:

Jika gitsudah ada di PATH Anda, penginstal akan menggunakan instalasi yang sudah ada.
Jika tidak, ia akan mengunduh PortableGit versi portabel (~50MB, dari rilis resmi git-for-windowsGitHub) dan mengekstraknya ke %LOCALAPPDATA%\hermes\git. Tidak memerlukan hak administrator. Sepenuhnya terisolasi — ia tidak akan mengganggu instalasi Git sistem apa pun, baik yang rusak maupun tidak. (Pada Windows 32-bit, ia akan kembali menggunakan MinGit karena PortableGit hanya menyediakan aset 64-bit dan ARM64; fitur Hermes yang bergantung pada bash tidak akan berfungsi pada host 32-bit.)
Mengapa tidak menggunakan winget? Desain sebelumnya menginstal Git secara otomatis melalui winget install Git.Git, tetapi winget gagal total ketika instalasi Git sistem dalam keadaan sebagian atau rusak (tepat ketika pengguna membutuhkan penginstal untuk langsung berfungsi). Pendekatan Git portabel menghindari winget, registri penginstal Windows, dan Git sistem yang ada sepenuhnya. Jika instalasi Git Hermes itu sendiri rusak, Remove-Item %LOCALAPPDATA%\hermes\gitjalankan kembali penginstal — tidak ada dampak sistem, tidak ada drama penghapusan instalasi.

Installer juga mengatur HERMES_GIT_BASH_PATHlokasi tersebut bash.exesehingga Hermes dapat menyelesaikannya secara deterministik di shell baru.

Jika Anda lebih menyukai WSL2, penginstal Linux di atas berfungsi di dalamnya; instalasi native dan WSL dapat berjalan berdampingan tanpa konflik (data native berada di bawah %LOCALAPPDATA%\hermes, data WSL berada di bawah ~/.hermes).

Desktop installer (alternative): A thin GUI installer is also available — download Hermes Desktop, run the .exe, and on first launch it calls install.ps1 under the hood to provision Python (via uv), Node, PortableGit, and the rest of the dependencies. The desktop app and the PowerShell-installed CLI share the same install and data directories, so you can use either or both. See the Windows (Native) guide for details.

Android / Termux
Hermes now ships a Termux-aware installer path too:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash


The installer detects Termux automatically and switches to a tested Android flow:

uses Termux pkg for system dependencies (git, python, nodejs, ripgrep, ffmpeg, build tools)
creates the virtualenv with python -m venv
exports ANDROID_API_LEVEL automatically for Android wheel builds
prefers the broad .[termux-all] extra and falls back to the smaller .[termux] extra (and finally a base install) if the first attempt fails to compile
skips the untested browser / WhatsApp bootstrap by default
If you want the fully explicit path, follow the dedicated Termux guide.

Windows Feature Parity (Early Beta)
Native Windows is in early beta. Everything except the browser-based dashboard chat terminal runs natively on Windows:

CLI (hermes chat, hermes setup, hermes gateway, …) — native, uses your default terminal
Gateway (Telegram, Discord, Slack, …) — native, runs as a background PowerShell process
Cron scheduler — native
Browser tool — native (Chromium via Node.js)
MCP servers — native (stdio and HTTP transports both supported)
Dashboard /chat terminal pane — WSL2 only (uses a POSIX PTY; native Windows has no equivalent). The rest of the dashboard (sessions, jobs, metrics) works natively — only the embedded PTY terminal tab is gated.
Set HERMES_DISABLE_WINDOWS_UTF8=1 in your environment if you hit an encoding-related bug and want to fall back to the legacy cp1252 stdio path (useful for bisecting).

What the Installer Does
The installer handles everything automatically — all dependencies (Python, Node.js, ripgrep, ffmpeg), the repo clone, virtual environment, global hermes command setup, and LLM provider configuration. By the end, you're ready to chat.

Install Layout
Where the installer puts things depends on whether you're installing as a normal user or as root:

Installer	Code lives at	hermes binary	Data directory
pip install	Python site-packages	~/.local/bin/hermes (console_scripts)	~/.hermes/
Per-user (git installer)	~/.hermes/hermes-agent/	~/.local/bin/hermes (symlink)	~/.hermes/
Root-mode (sudo curl … | sudo bash)	/usr/local/lib/hermes-agent/	/usr/local/bin/hermes	/root/.hermes/ (or $HERMES_HOME)
The root-mode FHS layout (/usr/local/lib/…, /usr/local/bin/hermes) matches where other system-wide developer tools land on Linux. It's useful for shared-machine deployments where one system install should serve every user. Per-user config (auth, skills, sessions) still lives under each user's ~/.hermes/ or explicit HERMES_HOME.

After Installation
Reload your shell and start chatting:

source ~/.bashrc   # or: source ~/.zshrc
hermes             # Start chatting!


To reconfigure individual settings later, use the dedicated commands:

hermes model          # Choose your LLM provider and model
hermes tools          # Configure which tools are enabled
hermes gateway setup  # Set up messaging platforms
hermes config set     # Set individual config values
hermes setup          # Or run the full setup wizard to configure everything at once


Fastest path: Nous Portal
One subscription covers 300+ models plus the Tool Gateway (web search, image generation, TTS, cloud browser). Skip the per-tool key juggling:

hermes setup --portal

That logs you in, sets Nous as your provider, and turns on the Tool Gateway in one command.

Prerequisites
pip install: No prerequisites beyond Python 3.11+. Everything else is handled automatically.

Git installer: The only prerequisite is Git. The installer automatically handles everything else:

uv (fast Python package manager)
Python 3.11 (via uv, no sudo needed)
Node.js v22 (for browser automation and WhatsApp bridge)
ripgrep (fast file search)
ffmpeg (audio format conversion for TTS)
info
You do not need to install Python, Node.js, ripgrep, or ffmpeg manually. The installer detects what's missing and installs it for you. Just make sure git is available (git --version).

Nix users
If you use Nix (on NixOS, macOS, or Linux), there's a dedicated setup path with a Nix flake, declarative NixOS module, and optional container mode. See the Nix & NixOS Setup guide.

Manual / Developer Installation
If you want to clone the repo and install from source — for contributing, running from a specific branch, or having full control over the virtual environment — see the Development Setup section in the Contributing guide.

Non-Sudo / System Service User Installs
Running Hermes as a dedicated unprivileged user (e.g. a hermes systemd service account, or any user without sudo access) is supported. The only thing on the install path that genuinely needs root is Playwright's --with-deps step, which apt-installs shared libraries (libnss3, libxkbcommon, etc.) used by Chromium. The installer detects whether sudo is available and gracefully degrades when it isn't — it will install the Chromium binary into the service user's own Playwright cache and print the exact command an administrator needs to run separately.

Recommended split (Debian/Ubuntu):

One time, as an admin user with sudo, install the system libraries Chromium needs:

sudo npx playwright install-deps chromium


(You can run this from anywhere — npx will fetch Playwright on the fly.)

Sebagai pengguna layanan tanpa hak istimewa , jalankan penginstal biasa. Penginstal akan mendeteksi hilangnya sudo, melewati langkah-langkah tertentu --with-deps, dan menginstal Chromium ke dalam cache Playwright lokal pengguna:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash


Jika Anda ingin melewati langkah Playwright sepenuhnya — misalnya karena Anda menjalankan aplikasi tanpa antarmuka grafis dan tidak memerlukan otomatisasi browser — berikan nilai --skip-browser:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash -s -- --skip-browser


Sediakan hermesakses ke shell pengguna layanan. Installer menulis peluncur ke ~/.local/bin/hermes. Akun layanan sistem seringkali memiliki PATH minimal yang tidak menyertakan ~/.local/bin. Tambahkan ke lingkungan pengguna, atau buat symlink peluncur ke lokasi sistem:

# Option A — add to the service user's profile
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Option B — symlink system-wide (run as an admin)
sudo ln -s /home/hermes/.hermes/hermes-agent/venv/bin/hermes /usr/local/bin/hermes


Verifikasi: hermes doctor seharusnya sekarang berjalan dengan lancar. Jika Anda mendapatkan ModuleNotFoundError: No module named 'dotenv', Anda memanggil hermesfile sumber repositori ( ~/.hermes/hermes-agent/hermes) dengan Python sistem, bukan peluncur venv ( ~/.hermes/hermes-agent/venv/bin/hermes) — perbaiki langkah 3.

Pola yang sama berlaku untuk Arch (installer menggunakan pacman dengan logika deteksi sudo yang sama), Fedora/RHEL, dan openSUSE — distro-distro tersebut --with-depssama sekali tidak mendukungnya, sehingga administrator selalu menginstal pustaka sistem secara terpisah. Perintah dnf/ yang relevan zypperakan dicetak oleh installer.

Penyelesaian Masalah
Masalah	Larutan
hermes: command not found	Muat ulang shell Anda ( source ~/.bashrc) atau periksa PATH
API key not set	Jalankan perintah hermes modeluntuk mengkonfigurasi penyedia Anda, atauhermes config set OPENROUTER_API_KEY your_key
Konfigurasi hilang setelah pembaruan.	Lari hermes config checklaluhermes config migrate
Untuk diagnosis lebih lanjut, jalankan perintah ini hermes doctor— perintah ini akan memberi tahu Anda secara tepat apa yang hilang dan bagaimana cara memperbaikinya.

Metode instalasi deteksi otomatis
Hermes secara otomatis mendeteksi apakah instalasi dilakukan melalui pipgit installer, Homebrew, atau NixOS, dan hermes updatemencetak perintah pembaruan yang sesuai untuk jalur tersebut. Tidak ada variabel lingkungan yang perlu diatur — deteksi didasarkan pada tata letak instalasi (site-packages Python, ~/.hermes/hermes-agent/prefiks Homebrew, atau jalur penyimpanan Nix). hermes doctorHermes juga menampilkan metode yang terdeteksi di bawah ringkasan lingkungannya.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Hermes di Android dengan Termux
Ini adalah jalur yang telah diuji untuk menjalankan Hermes Agent langsung di ponsel Android melalui Termux .

Ini memberi Anda CLI lokal yang berfungsi di ponsel, ditambah fitur tambahan inti yang saat ini diketahui dapat diinstal dengan bersih di Android.

Apa yang didukung pada jalur yang diuji?
Paket Termux yang diuji menginstal:

CLI Hermes
dukungan cron
Dukungan terminal PTY/latar belakang
Dukungan gateway Telegram (manual / menjalankan proses di latar belakang dengan upaya terbaik)
Dukungan MCP
Dukungan memori Honcho
Dukungan ACP
Secara konkret, ini dipetakan ke:

python -m pip install -e '.[termux]' -c constraints-termux.txt


Apa yang belum menjadi bagian dari jalur yang diuji?
Beberapa fitur masih memerlukan dependensi bergaya desktop/server yang belum dipublikasikan untuk Android, atau belum divalidasi pada ponsel:

.[all]saat ini tidak didukung di Android.
Ekstra tersebut voicediblokir oleh faster-whisper -> ctranslate2, dan ctranslate2tidak menerbitkan Android wheels.
Browser otomatis / Playwright bootstrap dilewati di penginstal Termux.
Isolasi terminal berbasis Docker tidak tersedia di dalam Termux.
Android mungkin masih menangguhkan pekerjaan latar belakang Termux, sehingga persistensi gateway bersifat upaya terbaik dan bukan layanan terkelola normal.
Hal itu tidak menghalangi Hermes untuk berfungsi dengan baik sebagai agen CLI asli ponsel — itu hanya berarti instalasi seluler yang direkomendasikan sengaja lebih terbatas daripada instalasi desktop/server.

Opsi 1: Penginstal satu baris
Hermes kini menyertakan jalur penginstal yang kompatibel dengan Termux:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash


Di Termux, penginstal akan secara otomatis:

kegunaan pkguntuk paket sistem
membuat venv denganpython -m venv
mencoba melakukan .[termux-all]instalasi tambahan yang lebih luas terlebih dahulu dan kemudian beralih ke .[termux]instalasi tambahan yang lebih kecil (lalu instalasi dasar) — penginstal curl secara otomatis mencocokkan urutan ini.
tautan hermeske $PREFIX/binsehingga tetap ada di PATH Termux Anda
Melewati bootstrap browser/WhatsApp yang belum diuji.
Jika Anda menginginkan perintah eksplisit atau perlu men-debug instalasi yang gagal, gunakan jalur manual di bawah ini.

Opsi 2: Instalasi manual (penjelasan lengkap)
1. Perbarui Termux dan instal paket sistem.
pkg update
pkg install -y git python clang rust make pkg-config libffi openssl nodejs ripgrep ffmpeg


Mengapa paket-paket ini?

python— dukungan runtime + venv
git— klon/perbarui repositori
clang, rust, make, pkg-config, libffi, openssl— perlu membangun beberapa dependensi Python di Android
nodejs— Runtime Node opsional untuk eksperimen di luar jalur inti yang telah diuji
ripgrep— pencarian file cepat
ffmpeg— konversi media / TTS
2. Kloning Hermes
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
cd hermes-agent


Jika Anda sudah melakukan kloning tanpa submodule:

git submodule update --init --recursive


3. Buat lingkungan virtual
python -m venv venv
source venv/bin/activate
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
python -m pip install --upgrade pip setuptools wheel


ANDROID_API_LEVELpenting untuk paket berbasis Rust/maturin seperti jiter.

4. Instal paket Termux yang telah diuji.
python -m pip install -e '.[termux]' -c constraints-termux.txt


Jika Anda hanya menginginkan agen inti minimal, ini juga bisa dilakukan:

python -m pip install -e '.' -c constraints-termux.txt


5. Tambahkan hermesPATH ke Termux Anda
ln -sf "$PWD/venv/bin/hermes" "$PREFIX/bin/hermes"


$PREFIX/binsudah ada di PATH di Termux, jadi ini membuat hermesperintah tetap berjalan di shell baru tanpa perlu mengaktifkan venv setiap kali.

6. Verifikasi instalasi
hermes version
hermes doctor

7. Mulai Hermes
hermes

Pengaturan tindak lanjut yang direkomendasikan
Konfigurasikan model
hermes model

Atau atur kunci secara langsung di ~/.hermes/.env.

Jalankan kembali wizard pengaturan interaktif lengkap nanti.
hermes setup

Instal dependensi Node opsional secara manual.
Jalur Termux yang diuji sengaja melewati proses bootstrap Node/browser. Jika Anda ingin bereksperimen dengan alat bantu browser nanti:

pkg install nodejs-lts
npm install

Alat peramban secara otomatis menyertakan direktori Termux ( /data/data/com.termux/files/usr/bin) dalam pencarian PATH-nya, sehingga agent-browserdan npxditemukan tanpa konfigurasi PATH tambahan apa pun.

Anggaplah fitur browser/WhatsApp di Android sebagai fitur eksperimental sampai ada dokumentasi yang menjelaskan lebih lanjut.

Penyelesaian Masalah
No solution foundsaat memasang.[all]
Gunakan paket Termux yang sudah teruji sebagai gantinya:

python -m pip install -e '.[termux]' -c constraints-termux.txt


Pemblokirnya saat ini adalah pemain voicetambahan:

voicetarikanfaster-whisper
faster-whispertergantung padactranslate2
ctranslate2tidak menerbitkan Android wheels
uv pip installgagal di Android
Gunakan jalur Termux dengan stdlib venv + pipsebagai gantinya:

python -m venv venv
source venv/bin/activate
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e '.[termux]' -c constraints-termux.txt


jiter/ maturinmengeluh tentangANDROID_API_LEVEL
Tetapkan level API secara eksplisit sebelum menginstal:

export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
python -m pip install -e '.[termux]' -c constraints-termux.txt


hermes doctormengatakan ripgrep atau Node hilang
Instal aplikasi tersebut menggunakan paket Termux:

pkg install ripgrep nodejs

Gagal saat membangun instalasi paket Python.
Pastikan toolchain build sudah terpasang:

pkg install clang rust make pkg-config libffi openssl


Kemudian coba lagi:

python -m pip install -e '.[termux]' -c constraints-termux.txt


Keterbatasan yang diketahui pada ponsel
Backend Docker tidak tersedia.
Transkripsi suara lokal melalui faster-whispertidak tersedia di jalur yang diuji.
Pengaturan otomatisasi browser sengaja dilewati oleh penginstal.
Beberapa tambahan opsional mungkin berfungsi, tetapi hanya .[termux]dan .[termux-all]yang saat ini didokumentasikan sebagai paket Android yang telah diuji.
Jika Anda menemukan masalah baru yang khusus untuk Android, silakan buka masalah di GitHub dengan:

versi Android Anda
termux-info
python --version
hermes doctor
Perintah instalasi yang tepat dan output kesalahan lengkap
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Pengaturan Nix & NixOS
Hermes Agent mengirimkan Nix flake dengan tiga tingkat integrasi:

Tingkat	Untuk siapa ini	Apa yang Anda dapatkan
nix run/nix profile install	Pengguna Nix mana pun (macOS, Linux)	Binary yang sudah dibuat sebelumnya dengan semua dependensi — kemudian gunakan alur kerja CLI standar.
Modul NixOS (asli)	Penyebaran server NixOS	Konfigurasi deklaratif, layanan systemd yang diperkuat, rahasia yang dikelola.
Modul NixOS (kontainer)	Agen yang membutuhkan modifikasi diri	Semua hal di atas, ditambah kontainer Ubuntu permanen tempat agen dapat apt/ pip/npm install
Apa yang berbeda dari instalasi standar?
Installer curl | bashmengelola Python, Node, dan dependensinya sendiri. Nix flake menggantikan semua itu — setiap dependensi Python adalah turunan Nix yang dibangun oleh uv2nix , dan alat runtime (Node.js, git, ripgrep, ffmpeg) dibungkus ke dalam PATH biner. Tidak ada pip runtime, tidak ada aktivasi venv, tidak ada npm install.

Bagi pengguna non-NixOS , ini hanya mengubah langkah instalasi. Semua yang terjadi setelahnya ( hermes setup, hermes gateway install, pengeditan konfigurasi) berfungsi identik dengan instalasi standar.

Bagi pengguna modul NixOS , seluruh siklus hidupnya berbeda: konfigurasi berada di configuration.nix, rahasia melalui sops-nix/agenix, layanannya adalah unit systemd, dan perintah konfigurasi CLI diblokir. Anda mengelola hermes dengan cara yang sama seperti Anda mengelola layanan NixOS lainnya.

Prasyarat
Nix dengan fitur flakes diaktifkan — Nix determinate direkomendasikan (fitur flakes diaktifkan secara default)
Kunci API untuk layanan yang ingin Anda gunakan (minimal: kunci OpenRouter atau Anthropic)
Panduan Memulai Cepat (Untuk Semua Pengguna Nix)
Tidak perlu kloning. Nix mengambil, membangun, dan menjalankan semuanya:

# Run directly (builds on first use, cached after)
nix run github:NousResearch/hermes-agent -- setup
nix run github:NousResearch/hermes-agent -- chat

# Or install persistently
nix profile install github:NousResearch/hermes-agent
hermes setup
hermes chat


Setelah nix profile install, hermes, hermes-agent, dan hermes-acpberada di PATH Anda. Dari sini, alur kerjanya identik dengan instalasi standar — hermes setupmemandu Anda melalui pemilihan penyedia, hermes gateway installmenyiapkan layanan pengguna launchd (macOS) atau systemd, dan konfigurasi berada di ~/.hermes/.

Membangun dari klon lokal
Modul NixOS
Flake mengekspor nixosModules.default— sebuah modul layanan NixOS lengkap yang secara deklaratif mengelola pembuatan pengguna, direktori, pembuatan konfigurasi, rahasia, dokumen, dan siklus hidup layanan.

catatan
Modul ini membutuhkan NixOS. Untuk sistem non-NixOS (macOS, distribusi Linux lainnya), gunakan nix profile installdan alur kerja CLI standar di atas.

Tambahkan Input Serpihan
# /etc/nixos/flake.nix (or your system flake)
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    hermes-agent.url = "github:NousResearch/hermes-agent";
  };

  outputs = { nixpkgs, hermes-agent, ... }: {
    nixosConfigurations.your-host = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        hermes-agent.nixosModules.default
        ./configuration.nix
      ];
    };
  };
}


Konfigurasi Minimal
# configuration.nix
{ config, ... }: {
  services.hermes-agent = {
    enable = true;
    settings.model.default = "anthropic/claude-sonnet-4";
    environmentFiles = [ config.sops.secrets."hermes-env".path ];
    addToSystemPackages = true;
  };
}


Selesai. Proses ini nixos-rebuild switchmembuat hermespengguna, menghasilkan config.yaml, menghubungkan rahasia, dan memulai gateway — layanan jangka panjang yang menghubungkan agen ke platform perpesanan (Telegram, Discord, dll.) dan mendengarkan pesan masuk.

Rahasia diperlukan
The environmentFiles line above assumes you have sops-nix or agenix configured. The file should contain at least one LLM provider key (e.g., OPENROUTER_API_KEY=sk-or-...). See Secrets Management for full setup. If you don't have a secrets manager yet, you can use a plain file as a starting point — just ensure it's not world-readable:

echo "OPENROUTER_API_KEY=sk-or-your-key" | sudo install -m 0600 -o hermes /dev/stdin /var/lib/hermes/env


services.hermes-agent.environmentFiles = [ "/var/lib/hermes/env" ];


addToSystemPackages
Setting addToSystemPackages = true does two things: puts the hermes CLI on your system PATH and sets HERMES_HOME system-wide so the interactive CLI shares state (sessions, skills, cron) with the gateway service. Without it, running hermes in your shell creates a separate ~/.hermes/ directory.

Container-aware CLI
info
When container.enable = true and addToSystemPackages = true, every hermes command on the host automatically routes into the managed container. This means your interactive CLI session runs inside the same environment as the gateway service — with access to all container-installed packages and tools.

The routing is transparent: hermes chat, hermes sessions list, hermes version, etc. all exec into the container under the hood
All CLI flags are forwarded as-is
If the container isn't running, the CLI retries briefly (5s with a spinner for interactive use, 10s silently for scripts) then fails with a clear error — no silent fallback
For developers working on the hermes codebase, set HERMES_DEV=1 to bypass container routing and run the local checkout directly
Set container.hostUsers to create a ~/.hermes symlink to the service state directory, so the host CLI and the container share sessions, config, and memories:

services.hermes-agent = {
  container.enable = true;
  container.hostUsers = [ "your-username" ];
  addToSystemPackages = true;
};


Users listed in hostUsers are automatically added to the hermes group for file permission access.

Podman users: The NixOS service runs the container as root. Docker users get access via the docker group socket, but Podman's rootful containers require sudo. Grant passwordless sudo for your container runtime:

security.sudo.extraRules = [{
  users = [ "your-username" ];
  commands = [{
    command = "/run/current-system/sw/bin/podman";
    options = [ "NOPASSWD" ];
  }];
}];


The CLI auto-detects when sudo is needed and uses it transparently. Without this, you'll need to run sudo hermes chat manually.

Verify It Works
After nixos-rebuild switch, check that the service is running:

# Check service status
systemctl status hermes-agent

# Watch logs (Ctrl+C to stop)
journalctl -u hermes-agent -f

# If addToSystemPackages is true, test the CLI
hermes version
hermes config       # shows the generated config


Choosing a Deployment Mode
The module supports two modes, controlled by container.enable:

Native (default)	Container
How it runs	Hardened systemd service on the host	Persistent Ubuntu container with /nix/store bind-mounted
Security	NoNewPrivileges, ProtectSystem=strict, PrivateTmp	Container isolation, runs as unprivileged user inside
Agent can self-install packages	No — only tools on the Nix-provided PATH	Yes — apt, pip, npm installs persist across restarts
Config surface	Same	Same
When to choose	Standard deployments, maximum security, reproducibility	Agent needs runtime package installation, mutable environment, experimental tools
To enable container mode, add one line:

{
  services.hermes-agent = {
    enable = true;
    container.enable = true;
    # ... rest of config is identical
  };
}


info
Container mode auto-enables virtualisation.docker.enable via mkDefault. If you use Podman instead, set container.backend = "podman" and virtualisation.docker.enable = false.

Configuration
Declarative Settings
The settings option accepts an arbitrary attrset that is rendered as config.yaml. It supports deep merging across multiple module definitions (via lib.recursiveUpdate), so you can split config across files:

# base.nix
services.hermes-agent.settings = {
  model.default = "anthropic/claude-sonnet-4";
  toolsets = [ "all" ];
  terminal = { backend = "local"; timeout = 180; };
};

# personality.nix
services.hermes-agent.settings = {
  display = { compact = false; personality = "kawaii"; };
  memory = { memory_enabled = true; user_profile_enabled = true; };
};


Both are deep-merged at evaluation time. Nix-declared keys always win over keys in an existing config.yaml on disk, but user-added keys that Nix doesn't touch are preserved. This means if the agent or a manual edit adds keys like skills.disabled or streaming.enabled, they survive nixos-rebuild switch.

Model naming
settings.model.default uses the model identifier your provider expects. With OpenRouter (the default), these look like "anthropic/claude-sonnet-4" or "google/gemini-3-flash". If you're using a provider directly (Anthropic, OpenAI), set settings.model.base_url to point at their API and use their native model IDs (e.g., "claude-sonnet-4-20250514"). When no base_url is set, Hermes defaults to OpenRouter.

Discovering available config keys
Run nix build .#configKeys && cat result to see every leaf config key extracted from Python's DEFAULT_CONFIG. You can paste your existing config.yaml into the settings attrset — the structure maps 1:1.

Full example: all commonly customized settings
Escape Hatch: Bring Your Own Config
If you'd rather manage config.yaml entirely outside Nix, use configFile:

services.hermes-agent.configFile = /etc/hermes/config.yaml;


This bypasses settings entirely — no merge, no generation. The file is copied as-is to $HERMES_HOME/config.yaml on each activation.

Customization Cheatsheet
Quick reference for the most common things Nix users want to customize:

I want to...	Option	Example
Change the LLM model	settings.model.default	"anthropic/claude-sonnet-4"
Use a different provider endpoint	settings.model.base_url	"https://openrouter.ai/api/v1"
Add API keys	environmentFiles	[ config.sops.secrets."hermes-env".path ]
Give the agent a personality	${services.hermes-agent.stateDir}/.hermes/SOUL.md	manage the file directly
Add MCP tool servers	mcpServers.<name>	See MCP Servers
Mount host directories into container	container.extraVolumes	[ "/data:/data:rw" ]
Pass GPU access to container	container.extraOptions	[ "--gpus" "all" ]
Use Podman instead of Docker	container.backend	"podman"
Share state between host CLI and container	container.hostUsers	[ "sidbin" ]
Make extra tools available to the agent	extraPackages	[ pkgs.pandoc pkgs.imagemagick ]
Use a custom base image	container.image	"ubuntu:24.04"
Override the hermes package	package	inputs.hermes-agent.packages.${system}.default.override { ... }
Change state directory	stateDir	"/opt/hermes"
Set the agent's working directory	workingDirectory	"/home/user/projects"
Secrets Management
Never put API keys in settings or environment
Values in Nix expressions end up in /nix/store, which is world-readable. Always use environmentFiles with a secrets manager.

Both environment (non-secret vars) and environmentFiles (secret files) are merged into $HERMES_HOME/.env at activation time (nixos-rebuild switch). Hermes reads this file on every startup, so changes take effect with a systemctl restart hermes-agent — no container recreation needed.

sops-nix
{
  sops = {
    defaultSopsFile = ./secrets/hermes.yaml;
    age.keyFile = "/home/user/.config/sops/age/keys.txt";
    secrets."hermes-env" = { format = "yaml"; };
  };

  services.hermes-agent.environmentFiles = [
    config.sops.secrets."hermes-env".path
  ];
}


The secrets file contains key-value pairs:

# secrets/hermes.yaml (encrypted with sops)
hermes-env: |
    OPENROUTER_API_KEY=sk-or-...
    TELEGRAM_BOT_TOKEN=123456:ABC...
    ANTHROPIC_API_KEY=sk-ant-...


agenix
{
  age.secrets.hermes-env.file = ./secrets/hermes-env.age;

  services.hermes-agent.environmentFiles = [
    config.age.secrets.hermes-env.path
  ];
}


OAuth / Auth Seeding
For platforms requiring OAuth (e.g., Discord), use authFile to seed credentials on first deploy:

{
  services.hermes-agent = {
    authFile = config.sops.secrets."hermes/auth.json".path;
    # authFileForceOverwrite = true;  # overwrite on every activation
  };
}


The file is only copied if auth.json doesn't already exist (unless authFileForceOverwrite = true). Runtime OAuth token refreshes are written to the state directory and preserved across rebuilds.

Documents
The documents option installs files into the agent's working directory (the workingDirectory, which the agent reads as its workspace). Hermes looks for specific filenames by convention:

USER.md — context about the user the agent is interacting with.
Any other files you place here are visible to the agent as workspace files.
The agent identity file is separate: Hermes loads its primary SOUL.md from $HERMES_HOME/SOUL.md, which in the NixOS module is ${services.hermes-agent.stateDir}/.hermes/SOUL.md. Putting SOUL.md in documents only creates a workspace file and will not replace the main persona file.

{
  services.hermes-agent.documents = {
    "USER.md" = ./documents/USER.md;  # path reference, copied from Nix store
  };
}


Values can be inline strings or path references. Files are installed on every nixos-rebuild switch.

MCP Servers
The mcpServers option declaratively configures MCP (Model Context Protocol) servers. Each server uses either stdio (local command) or HTTP (remote URL) transport.

Stdio Transport (Local Servers)
{
  services.hermes-agent.mcpServers = {
    filesystem = {
      command = "npx";
      args = [ "-y" "@modelcontextprotocol/server-filesystem" "/data/workspace" ];
    };
    github = {
      command = "npx";
      args = [ "-y" "@modelcontextprotocol/server-github" ];
      env.GITHUB_PERSONAL_ACCESS_TOKEN = "\${GITHUB_TOKEN}"; # resolved from .env
    };
  };
}


tip
Environment variables in env values are resolved from $HERMES_HOME/.env at runtime. Use environmentFiles to inject secrets — never put tokens directly in Nix config.

HTTP Transport (Remote Servers)
{
  services.hermes-agent.mcpServers.remote-api = {
    url = "https://mcp.example.com/v1/mcp";
    headers.Authorization = "Bearer \${MCP_REMOTE_API_KEY}";
    timeout = 180;
  };
}


HTTP Transport with OAuth
Set auth = "oauth" for servers using OAuth 2.1. Hermes implements the full PKCE flow — metadata discovery, dynamic client registration, token exchange, and automatic refresh.

{
  services.hermes-agent.mcpServers.my-oauth-server = {
    url = "https://mcp.example.com/mcp";
    auth = "oauth";
  };
}


Tokens are stored in $HERMES_HOME/mcp-tokens/<server-name>.json and persist across restarts and rebuilds.

Initial OAuth authorization on headless servers
Sampling (Server-Initiated LLM Requests)
Some MCP servers can request LLM completions from the agent:

{
  services.hermes-agent.mcpServers.analysis = {
    command = "npx";
    args = [ "-y" "analysis-server" ];
    sampling = {
      enabled = true;
      model = "google/gemini-3-flash";
      max_tokens_cap = 4096;
      timeout = 30;
      max_rpm = 10;
    };
  };
}


Managed Mode
When hermes runs via the NixOS module, the following CLI commands are blocked with a descriptive error pointing you to configuration.nix:

Blocked command	Why
hermes setup	Config is declarative — edit settings in your Nix config
hermes config edit	Config is generated from settings
hermes config set <key> <value>	Config is generated from settings
hermes gateway install	The systemd service is managed by NixOS
hermes gateway uninstall	The systemd service is managed by NixOS
This prevents drift between what Nix declares and what's on disk. Detection uses two signals:

HERMES_MANAGED=true environment variable — set by the systemd service, visible to the gateway process
.managed marker file in HERMES_HOME — set by the activation script, visible to interactive shells (e.g., docker exec -it hermes-agent hermes config set ... is also blocked)
To change configuration, edit your Nix config and run sudo nixos-rebuild switch.

Container Architecture
info
This section is only relevant if you're using container.enable = true. Skip it for native mode deployments.

When container mode is enabled, hermes runs inside a persistent Ubuntu container with the Nix-built binary bind-mounted read-only from the host:

Host                                    Container
────                                    ─────────
/nix/store/...-hermes-agent-0.1.0  ──►  /nix/store/... (ro)
~/.hermes -> /var/lib/hermes/.hermes       (symlink bridge, per hostUsers)
/var/lib/hermes/                    ──►  /data/          (rw)
  ├── current-package -> /nix/store/...    (symlink, updated each rebuild)
  ├── .gc-root -> /nix/store/...           (prevents nix-collect-garbage)
  ├── .container-identity                  (sha256 hash, triggers recreation)
  ├── .hermes/                             (HERMES_HOME)
  │   ├── .env                             (merged from environment + environmentFiles)
  │   ├── config.yaml                      (Nix-generated, deep-merged by activation)
  │   ├── .managed                         (marker file)
  │   ├── .container-mode                  (routing metadata: backend, exec_user, etc.)
  │   ├── state.db, sessions/, memories/   (runtime state)
  │   └── mcp-tokens/                      (OAuth tokens for MCP servers)
  ├── home/                                ──►  /home/hermes    (rw)
  └── workspace/                           (MESSAGING_CWD)
      ├── SOUL.md                          (from documents option)
      └── (agent-created files)

Container writable layer (apt/pip/npm):   /usr, /usr/local, /tmp


The Nix-built binary works inside the Ubuntu container because /nix/store is bind-mounted — it brings its own interpreter and all dependencies, so there's no reliance on the container's system libraries. The container entrypoint resolves through a current-package symlink: /data/current-package/bin/hermes gateway run --replace. On nixos-rebuild switch, only the symlink is updated — the container keeps running.

What Persists Across What
Event	Container recreated?	/data (state)	/home/hermes	Writable layer (apt/pip/npm)
systemctl restart hermes-agent	No	Persists	Persists	Persists
nixos-rebuild switch (code change)	No (symlink updated)	Persists	Persists	Persists
Host reboot	No	Persists	Persists	Persists
nix-collect-garbage	No (GC root)	Persists	Persists	Persists
Image change (container.image)	Yes	Persists	Persists	Lost
Volume/options change	Yes	Persists	Persists	Lost
environment/environmentFiles change	No	Persists	Persists	Persists
The container is only recreated when its identity hash changes. The hash covers: schema version, image, extraVolumes, extraOptions, and the entrypoint script. Changes to environment variables, settings, documents, or the hermes package itself do not trigger recreation.

Writable layer loss
When the identity hash changes (image upgrade, new volumes, new container options), the container is destroyed and recreated from a fresh pull of container.image. Any apt install, pip install, or npm install packages in the writable layer are lost. State in /data and /home/hermes is preserved (these are bind mounts).

If the agent relies on specific packages, consider baking them into a custom image (container.image = "my-registry/hermes-base:latest") or scripting their installation in the agent's SOUL.md.

GC Root Protection
The preStart script creates a GC root at ${stateDir}/.gc-root pointing to the current hermes package. This prevents nix-collect-garbage from removing the running binary. If the GC root somehow breaks, restarting the service recreates it.

Plugins
The NixOS module supports declarative plugin installation — no imperative hermes plugins install needed.

Directory Plugins (extraPlugins)
For plugins that are just a source tree with plugin.yaml + __init__.py (e.g., hermes-lcm):

services.hermes-agent.extraPlugins = [
  (pkgs.fetchFromGitHub {
    owner = "stephenschoettler";
    repo = "hermes-lcm";
    rev = "v0.7.0";
    hash = "sha256-...";
  })
];


Plugins are symlinked into $HERMES_HOME/plugins/ at activation time. Hermes discovers them via its normal directory scan. Removing a plugin from the list and running nixos-rebuild switch removes the symlink.

Entry-Point Plugins (extraPythonPackages)
For pip-packaged plugins that register via [project.entry-points."hermes_agent.plugins"] (e.g., rtk-hermes):

services.hermes-agent.extraPythonPackages = [
  (pkgs.python312Packages.buildPythonPackage {
    pname = "rtk-hermes";
    version = "1.0.0";
    src = pkgs.fetchFromGitHub {
      owner = "ogallotti";
      repo = "rtk-hermes";
      rev = "v1.0.0";
      hash = "sha256-...";
    };
    format = "pyproject";
    build-system = [ pkgs.python312Packages.setuptools ];
  })
];


The package's site-packages is added to PYTHONPATH in the hermes wrapper. importlib.metadata discovers the entry point at session start.

Optional Dependency Groups (extraDependencyGroups)
For optional extras already declared in hermes-agent's pyproject.toml (e.g., memory providers like hindsight or honcho), use extraDependencyGroups to include them in the sealed venv at build time:

services.hermes-agent = {
  extraDependencyGroups = [ "hindsight" ];
  settings.memory.provider = "hindsight";
};


This is resolved by uv alongside core dependencies in a single pass — no PYTHONPATH patching, no collision risk. Available groups match the [project.optional-dependencies] keys in pyproject.toml (e.g., "hindsight", "honcho", "voice", "matrix", "mistral", "bedrock").

When to use which:

Need	Option
Enable a pyproject.toml optional extra	extraDependencyGroups
Add an external Python plugin not in pyproject.toml	extraPythonPackages
Add a system binary (pandoc, jq, etc.)	extraPackages
Add a directory-based plugin source tree	extraPlugins
Combining Both
A directory plugin with third-party Python dependencies needs both options:

services.hermes-agent = {
  extraPlugins = [ my-plugin-src ];          # plugin source
  extraPythonPackages = [ pkgs.python312Packages.redis ];  # its Python dep
  extraPackages = [ pkgs.redis ];            # system binary it needs
};


Using the Overlay
External flakes can override the package directly:

{
  inputs.hermes-agent.url = "github:NousResearch/hermes-agent";
  outputs = { hermes-agent, nixpkgs, ... }: {
    nixpkgs.overlays = [ hermes-agent.overlays.default ];
    # Then:
    #   pkgs.hermes-agent.override { extraPythonPackages = [...]; }
    #   pkgs.hermes-agent.override { extraDependencyGroups = [ "hindsight" ]; }
  };
}


Plugin Configuration
Plugins still need to be enabled in config.yaml. Add them via the declarative settings:

services.hermes-agent.settings.plugins.enabled = [
  "hermes-lcm"
  "rtk-rewrite"
];


note
A build-time collision check prevents plugin packages from shadowing core hermes dependencies. If a plugin provides a package already in the sealed venv, nixos-rebuild fails with a clear error.

Development
Dev Shell
The flake provides a development shell with Python 3.12, uv, Node.js, and all runtime tools:

cd hermes-agent
nix develop

# Shell provides:
#   - Python 3.12 + uv (deps installed into .venv on first entry)
#   - Node.js 22, ripgrep, git, openssh, ffmpeg on PATH
#   - Stamp-file optimization: re-entry is near-instant if deps haven't changed

hermes setup
hermes chat


direnv (Recommended)
The included .envrc activates the dev shell automatically:

cd hermes-agent
direnv allow    # one-time
# Subsequent entries are near-instant (stamp file skips dep install)


Flake Checks
The flake includes build-time verification that runs in CI and locally:

# Run all checks
nix flake check

# Individual checks
nix build .#checks.x86_64-linux.package-contents   # binaries exist + version
nix build .#checks.x86_64-linux.entry-points-sync  # pyproject.toml ↔ Nix package sync
nix build .#checks.x86_64-linux.cli-commands        # gateway/config subcommands
nix build .#checks.x86_64-linux.managed-guard       # HERMES_MANAGED blocks mutation
nix build .#checks.x86_64-linux.bundled-skills      # skills present in package
nix build .#checks.x86_64-linux.config-roundtrip    # merge script preserves user keys


What each check verifies
Options Reference
Core
Option	Type	Default	Description
enable	bool	false	Enable the hermes-agent service
package	package	hermes-agent	The hermes-agent package to use
user	str	"hermes"	System user
group	str	"hermes"	System group
createUser	bool	true	Auto-create user/group
stateDir	str	"/var/lib/hermes"	State directory (HERMES_HOME parent)
workingDirectory	str	"${stateDir}/workspace"	Agent working directory (MESSAGING_CWD)
addToSystemPackages	bool	false	Add hermes CLI to system PATH and set HERMES_HOME system-wide
Configuration
Option	Type	Default	Description
settings	attrs (deep-merged)	{}	Declarative config rendered as config.yaml. Supports arbitrary nesting; multiple definitions are merged via lib.recursiveUpdate
configFile	null or path	null	Path to an existing config.yaml. Overrides settings entirely if set
Secrets & Environment
Option	Type	Default	Description
environmentFiles	listOf str	[]	Paths to env files with secrets. Merged into $HERMES_HOME/.env at activation time
environment	attrsOf str	{}	Non-secret env vars. Visible in Nix store — do not put secrets here
authFile	null or path	null	OAuth credentials seed. Only copied on first deploy
authFileForceOverwrite	bool	false	Always overwrite auth.json from authFile on activation
Documents
Option	Type	Default	Description
documents	attrsOf (either str path)	{}	Workspace files. Keys are filenames, values are inline strings or paths. Installed into workingDirectory on activation
MCP Servers
Option	Type	Default	Description
mcpServers	attrsOf submodule	{}	MCP server definitions, merged into settings.mcp_servers
mcpServers.<name>.command	null or str	null	Server command (stdio transport)
mcpServers.<name>.args	listOf str	[]	Command arguments
mcpServers.<name>.env	attrsOf str	{}	Environment variables for the server process
mcpServers.<name>.url	null or str	null	Server endpoint URL (HTTP/StreamableHTTP transport)
mcpServers.<name>.headers	attrsOf str	{}	HTTP headers, e.g. Authorization
mcpServers.<name>.auth	null or "oauth"	null	Authentication method. "oauth" enables OAuth 2.1 PKCE
mcpServers.<name>.enabled	bool	true	Enable or disable this server
mcpServers.<name>.timeout	null or int	null	Tool call timeout in seconds (default: 120)
mcpServers.<name>.connect_timeout	null or int	null	Connection timeout in seconds (default: 60)
mcpServers.<name>.tools	null or submodule	null	Tool filtering (include/exclude lists)
mcpServers.<name>.sampling	null or submodule	null	Sampling config for server-initiated LLM requests
Service Behavior
Option	Type	Default	Description
extraArgs	listOf str	[]	Extra args for hermes gateway
extraPackages	listOf package	[]	Extra packages available to the agent. Added to the hermes user's per-user profile so terminal commands, skills, and cron jobs all see them
extraPlugins	listOf package	[]	Paket plugin direktori yang akan ditautkan secara simbolis $HERMES_HOME/plugins/. Masing-masing harus berisiplugin.yaml
extraPythonPackages	listOf package	[]	Paket Python ditambahkan ke PYTHONPATH untuk penemuan plugin titik masuk. Bangun denganpython312Packages
extraDependencyGroups	listOf str	[]	Ekstra opsional pyproject.toml untuk disertakan dalam venv tertutup (misalnya ["hindsight"]). Diselesaikan oleh uv — tidak ada benturan
restart	str	"always"	Restart=kebijakan systemd
restartSec	int	5	RestartSec=nilai sistemd
Wadah
Pilihan	Jenis	Bawaan	Keterangan
container.enable	bool	false	Aktifkan mode kontainer OCI
container.backend	enum ["docker" "podman"]	"docker"	Lingkungan eksekusi kontainer
container.image	str	"ubuntu:24.04"	Gambar dasar (diambil saat runtime)
container.extraVolumes	listOf str	[]	Dudukan volume ekstra ( host:container:mode)
container.extraOptions	listOf str	[]	Argumen tambahan diteruskan kedocker create
container.hostUsers	listOf str	[]	Pengguna interaktif yang mendapatkan ~/.hermessymlink ke stateDir layanan dan ditambahkan secara otomatis ke hermesgrup.
Tata Letak Direktori
Mode Asli
/var/lib/hermes/                     # stateDir (owned by hermes:hermes, 0750)
├── .hermes/                         # HERMES_HOME
│   ├── config.yaml                  # Nix-generated (deep-merged each rebuild)
│   ├── .managed                     # Marker: CLI config mutation blocked
│   ├── .env                         # Merged from environment + environmentFiles
│   ├── auth.json                    # OAuth credentials (seeded, then self-managed)
│   ├── gateway.pid
│   ├── state.db
│   ├── mcp-tokens/                  # OAuth tokens for MCP servers
│   ├── sessions/
│   ├── memories/
│   ├── skills/
│   ├── cron/
│   └── logs/
├── home/                            # Agent HOME
└── workspace/                       # MESSAGING_CWD
    ├── SOUL.md                      # From documents option
    └── (agent-created files)


Mode Kontainer
Tata letak yang sama, dipasang di dalam kontainer:

Jalur kontainer	Jalur host	Mode	Catatan
/nix/store	/nix/store	ro	Hermes biner + semua dependensi Nix
/data	/var/lib/hermes	rw	Semua status, konfigurasi, ruang kerja
/home/hermes	${stateDir}/home	rw	Beranda agen tetap — pip install --user, cache alat
/usr, /usr/local,/tmp	(lapisan yang dapat ditulis)	rw	apt// pipinstalasi npm— tetap ada meskipun di-restart, hilang saat dibuat ulang
Memperbarui
# Update the flake input (run from the directory containing flake.nix)
cd /etc/nixos && nix flake update hermes-agent

# Rebuild
sudo nixos-rebuild switch


Dalam mode kontainer, current-packagesymlink diperbarui dan agen akan mengambil biner baru saat restart. Tidak ada pembuatan ulang kontainer, tidak ada kehilangan paket yang terinstal.

Penyelesaian Masalah
Pengguna Podman
Semua dockerperintah di bawah ini berfungsi sama dengan podman. Ganti sesuai kebutuhan jika Anda mengatur container.backend = "podman".

Log Layanan
# Both modes use the same systemd unit
journalctl -u hermes-agent -f

# Container mode: also available directly
docker logs -f hermes-agent


Inspeksi Kontainer
systemctl status hermes-agent
docker ps -a --filter name=hermes-agent
docker inspect hermes-agent --format='{{.State.Status}}'
docker exec -it hermes-agent bash
docker exec hermes-agent readlink /data/current-package
docker exec hermes-agent cat /data/.container-identity


Rekreasi Kontainer Paksa
Jika Anda perlu mengatur ulang lapisan yang dapat ditulis (Ubuntu versi terbaru):

sudo systemctl stop hermes-agent
docker rm -f hermes-agent
sudo rm /var/lib/hermes/.container-identity
sudo systemctl start hermes-agent


Verifikasi Rahasia Telah Dimuat
Jika agen berjalan tetapi tidak dapat melakukan autentikasi dengan penyedia LLM, periksa apakah .envfile telah digabungkan dengan benar:

# Native mode
sudo -u hermes cat /var/lib/hermes/.hermes/.env

# Container mode
docker exec hermes-agent cat /data/.hermes/.env


Verifikasi Akar GC
nix-store --query --roots $(docker exec hermes-agent readlink /data/current-package)


Masalah Umum
Gejala	Menyebabkan	Memperbaiki
Cannot save configuration: managed by NixOS	CLI melindungi secara aktif	Edit configuration.nixdannixos-rebuild switch
Kontainer dibuat ulang secara tidak terduga.	extraVolumes, extraOptions, atau imagediubah	Sesuai dugaan — lapisan yang dapat ditulis diatur ulang. Instal ulang paket atau gunakan citra kustom.
hermes versionmenampilkan versi lama	Kontainer tidak dihidupkan ulang	systemctl restart hermes-agent
Izin ditolak pada/var/lib/hermes	Direktur negara adalah0750 hermes:hermes	Gunakan docker execatausudo -u hermes
nix-collect-garbageHermes dihapus	Akar GC hilang	Mulai ulang layanan (preStart membuat ulang root GC)
no container with name or ID "hermes-agent"(Podman)	Kontainer Podman rootful tidak terlihat oleh pengguna biasa.	Tambahkan sudo tanpa kata sandi untuk podman (lihat bagian Mode Kontainer )
unable to find user hermes	Kontainer masih dalam proses memulai (entrypoint belum membuat pengguna)	Tunggu beberapa detik dan coba lagi — CLI akan mencoba lagi secara otomatis.
Alat ditambahkan melalui extraPackagestidak ditemukan di terminal.	Membutuhkan nixos-rebuild switchpembaruan profil per pengguna.	Bangun ulang dan mulai ulang:nixos-rebuild switch && systemctl restart hermes-agent
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Memperbarui & Menghapus Instalasi
Memperbarui
Instalasi Git
Perbarui ke versi terbaru dengan satu perintah:

hermes update

Ini mengambil kode terbaru dari main, memperbarui dependensi, dan meminta Anda untuk mengkonfigurasi opsi baru apa pun yang ditambahkan sejak pembaruan terakhir Anda.

pip menginstal
Rilis PyPI melacak versi yang diberi tag (rilis utama dan minor), bukan setiap commit pada main. Periksa pembaruan dan tingkatkan dengan:

hermes update --check    # see if a newer release is on PyPI
hermes update            # runs pip install --upgrade hermes-agent


Atau secara manual:

pip install --upgrade hermes-agent    # or: uv pip install --upgrade hermes-agent


tip
hermes updateSecara otomatis mendeteksi opsi konfigurasi baru dan meminta Anda untuk menambahkannya. Jika Anda melewatkan permintaan tersebut, Anda dapat menjalankannya secara manual hermes config checkuntuk melihat opsi yang hilang, lalu hermes config migratemenambahkannya secara interaktif.

Apa yang terjadi selama pembaruan (git install)?
Saat Anda menjalankan program hermes update, langkah-langkah berikut terjadi:

Snapshot data pasangan — snapshot status pra-pembaruan yang ringan disimpan (mencakup ~/.hermes/pairing/aturan komentar Feishu, dan file status lain yang dimodifikasi saat runtime). Dapat dipulihkan melalui alur pemulihan snapshot yang dijelaskan di bawah Snapshot dan rollback , atau dengan mengekstrak zip snapshot cepat terbaru yang ditulis Hermes di sebelah ~/.hermes/direktori Anda.
Git pull — mengambil kode terbaru dari maincabang dan memperbarui submodule.
Instalasi dependensi — dijalankan uv pip install -e ".[all]"untuk mengambil dependensi baru atau yang diubah.
Migrasi konfigurasi — mendeteksi opsi konfigurasi baru yang ditambahkan sejak versi Anda dan meminta Anda untuk mengaturnya.
Restart otomatis gateway — gateway yang sedang berjalan akan di-refresh setelah pembaruan selesai sehingga kode baru langsung berlaku. Gateway yang dikelola layanan (systemd di Linux, launchd di macOS) akan di-restart melalui pengelola layanan. Gateway manual akan diluncurkan kembali secara otomatis ketika Hermes dapat memetakan PID yang sedang berjalan kembali ke profil.
Hanya pratinjau:hermes update --check
Ingin tahu apakah pembaruan tersedia sebelum melakukan pull? Jalankan perintah ini hermes update --check— untuk instalasi git, perintah ini mengambil dan membandingkan commit dengan origin/main; untuk instalasi pip, perintah ini menanyakan PyPI untuk rilis terbaru. Tidak ada file yang dimodifikasi, tidak ada gateway yang di-restart. Berguna dalam skrip dan cron job yang memeriksa "adanya pembaruan".

Pencadangan lengkap sebelum pembaruan:--backup
Untuk profil bernilai tinggi (gateway produksi, instalasi tim bersama), Anda dapat memilih untuk melakukan pencadangan pra-penarikan penuh HERMES_HOME(konfigurasi, otentikasi, sesi, keterampilan, pemasangan):

hermes update --backup

Atau jadikan itu sebagai pengaturan default untuk setiap kali dijalankan:

# ~/.hermes/config.yaml
updates:
  pre_update_backup: true

--backupFitur ini selalu aktif pada versi sebelumnya, tetapi fitur ini menambah waktu beberapa menit pada setiap pembaruan di rumah-rumah besar, jadi sekarang fitur ini bersifat opsional. Snapshot data pemasangan yang ringan di atas masih berjalan tanpa syarat.

Windows: yang lain hermes.exesedang berjalan
Di Windows, hermes updateprogram akan menolak untuk berjalan jika mendeteksi hermes.exeproses lain yang sedang membuka executable titik masuk venv — paling sering backend yang dijalankan oleh aplikasi Hermes Desktop, hermesREPL yang terbuka di terminal lain, atau gateway yang sedang berjalan:

$ hermes update
✗ Another hermes.exe is running:
    PID 12345  hermes.exe

  Updating now would fail to overwrite ...\venv\Scripts\hermes.exe because
  Windows blocks REPLACE on a running executable.

  Close Hermes Desktop, exit any open `hermes` REPLs, and
  stop the gateway (`hermes gateway stop`) before retrying.
  Override with `hermes update --force` if you've already
  confirmed those processes will not write to the venv.


Close the listed processes and re-run. If you're sure the concurrent process won't interfere (rare — usually only useful when an antivirus shim is mis-attributed), pass --force to skip the check. In that case the updater will still retry the .exe rename with exponential backoff and, on stubborn locks, schedule the replacement for next reboot via MoveFileEx(MOVEFILE_DELAY_UNTIL_REBOOT) so the update can complete.

Expected output looks like:

$ hermes update
Updating Hermes Agent...
📥 Pulling latest code...
Already up to date.  (or: Updating abc1234..def5678)
📦 Updating dependencies...
✅ Dependencies updated
🔍 Checking for new config options...
✅ Config is up to date  (or: Found 2 new options — running migration...)
🔄 Restarting gateways...
✅ Gateway restarted
✅ Hermes Agent updated successfully!


Recommended Post-Update Validation
hermes update handles the main update path, but a quick validation confirms everything landed cleanly:

git status --short — if the tree is unexpectedly dirty, inspect before continuing
hermes doctor — checks config, dependencies, and service health
hermes --version — confirm the version bumped as expected
If you use the gateway: hermes gateway status
If doctor reports npm audit issues: run npm audit fix in the flagged directory
Dirty working tree after update
If git status --short shows unexpected changes after hermes update, stop and inspect them before continuing. This usually means local modifications were reapplied on top of the updated code, or a dependency step refreshed lockfiles.

If your terminal disconnects mid-update
hermes update protects itself against accidental terminal loss:

The update ignores SIGHUP, so closing your SSH session or terminal window no longer kills it mid-install. pip and git child processes inherit this protection, so the Python environment cannot be left half-installed by a dropped connection.
All output is mirrored to ~/.hermes/logs/update.log while the update runs. If your terminal disappears, reconnect and inspect the log to see whether the update finished and whether the gateway restart succeeded:
tail -f ~/.hermes/logs/update.log

Ctrl-C (SIGINT) and system shutdown (SIGTERM) are still honored — those are deliberate cancellations, not accidents.
You no longer need to wrap hermes update in screen or tmux to survive a terminal drop.

Checking your current version
hermes version

Compare against the latest release at the GitHub releases page.

Updating from Messaging Platforms
You can also update directly from Telegram, Discord, Slack, WhatsApp, or Teams by sending:

/update

This pulls the latest code, updates dependencies, and restarts running gateways. The bot will briefly go offline during the restart (typically 5–15 seconds) and then resume.

Manual Update
If you installed manually (not via the quick installer):

cd /path/to/hermes-agent
export VIRTUAL_ENV="$(pwd)/venv"

# Pull latest code
git pull origin main

# Reinstall (picks up new dependencies)
uv pip install -e ".[all]"

# Check for new config options
hermes config check
hermes config migrate   # Interactively add any missing options


Rollback instructions
If an update introduces a problem, you can roll back to a previous version:

cd /path/to/hermes-agent

# List recent versions
git log --oneline -10

# Roll back to a specific commit
git checkout <commit-hash>
git submodule update --init --recursive
uv pip install -e ".[all]"

# Restart the gateway if running
hermes gateway restart


To roll back to a specific release tag:

git checkout v0.6.0
git submodule update --init --recursive
uv pip install -e ".[all]"


warning
Rolling back may cause config incompatibilities if new options were added. Run hermes config check after rolling back and remove any unrecognized options from config.yaml if you encounter errors.

Note for Nix users
If you installed via Nix flake, updates are managed through the Nix package manager:

# Update the flake input
nix flake update hermes-agent

# Or rebuild with the latest
nix profile upgrade hermes-agent

Nix installations are immutable — rollback is handled by Nix's generation system:

nix profile rollback

See Nix Setup for more details.

Uninstalling
Git installs
hermes uninstall

Program uninstaller memberi Anda opsi untuk menyimpan file konfigurasi Anda ( ~/.hermes/) untuk instalasi ulang di masa mendatang.

pip menginstal
pip uninstall hermes-agent
rm -rf ~/.hermes            # Optional — keep if you plan to reinstall


Pencopotan Instalasi Manual
rm -f ~/.local/bin/hermes
rm -rf /path/to/hermes-agent
rm -rf ~/.hermes            # Optional — keep if you plan to reinstall


informasi
Jika Anda menginstal gateway sebagai layanan sistem, hentikan dan nonaktifkan terlebih dahulu:

hermes gateway stop
# Linux: systemctl --user disable hermes-gateway
# macOS: launchctl remove ai.hermes.gateway
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Jalur Pembelajaran
Hermes Agent dapat melakukan banyak hal — asisten CLI, bot Telegram/Discord, otomatisasi tugas, pelatihan RL, dan banyak lagi. Halaman ini membantu Anda menentukan dari mana harus memulai dan apa yang perlu dibaca berdasarkan tingkat pengalaman Anda dan apa yang ingin Anda capai.

Mulai di sini
Jika Anda belum menginstal Hermes Agent, mulailah dengan panduan Instalasi dan kemudian ikuti Panduan Cepat . Semua hal di bawah ini mengasumsikan Anda memiliki instalasi yang berfungsi.

Cara Menggunakan Halaman Ini
Apakah Anda sudah mengetahui level Anda? Langsung saja ke tabel tingkat pengalaman dan ikuti urutan bacaan sesuai level Anda.
Punya tujuan spesifik? Langsung saja ke Berdasarkan Kasus Penggunaan dan temukan skenario yang sesuai.
Hanya sekadar melihat-lihat? Periksa tabel Fitur Utama untuk gambaran singkat tentang semua yang dapat dilakukan Hermes Agent.
Berdasarkan Tingkat Pengalaman
Tingkat	Sasaran	Bacaan yang Direkomendasikan	Perkiraan Waktu
Pemula	Mulailah menggunakan aplikasi, lakukan percakapan dasar, dan gunakan fitur bawaan.	Instalasi → Panduan Cepat → Penggunaan CLI → Konfigurasi	~1 jam
Intermediat	Siapkan bot perpesanan, gunakan fitur-fitur canggih seperti memori, cron job, dan skill.	Sesi → Pesan → Alat → Keterampilan → Memori → Cron	~2–3 jam
Canggih	Buat alat khusus, kembangkan keterampilan, latih model dengan RL, berkontribusi pada proyek.	Arsitektur → Menambahkan Alat → Mengembangkan Keterampilan → Pelatihan RL → Berkontribusi	~4–6 jam
Berdasarkan Kasus Penggunaan
Pilih skenario yang sesuai dengan apa yang ingin Anda lakukan. Setiap skenario akan mengarahkan Anda ke dokumen yang relevan sesuai urutan yang seharusnya Anda baca.

"Saya menginginkan asisten pengkodean CLI"
Gunakan Hermes Agent sebagai asisten terminal interaktif untuk menulis, meninjau, dan menjalankan kode.

Instalasi
Panduan Singkat
Penggunaan CLI
Eksekusi Kode
Berkas Konteks
Tips & Trik
tip
Lewatkan file langsung ke percakapan Anda dengan file konteks. Hermes Agent dapat membaca, mengedit, dan menjalankan kode dalam proyek Anda.

"Saya ingin bot Telegram/Discord"
Gunakan Hermes Agent sebagai bot di platform perpesanan favorit Anda.

Instalasi
Konfigurasi
Gambaran Umum Pesan
Pengaturan Telegram
Pengaturan Discord
Mode Suara
Gunakan Mode Suara dengan Hermes
Keamanan
Untuk contoh proyek selengkapnya, lihat:

Bot Ringkasan Harian
Asisten Tim Telegram
"Saya ingin mengotomatiskan tugas"
Jadwalkan tugas berulang, jalankan pekerjaan batch, atau rangkai tindakan agen secara bersamaan.

Panduan Singkat
Penjadwalan Cron
Pemrosesan Batch
Delegasi
Kait
tip
Cron job memungkinkan Hermes Agent menjalankan tugas sesuai jadwal — ringkasan harian, pemeriksaan berkala, laporan otomatis — tanpa kehadiran Anda.

"Saya ingin membangun alat/keterampilan khusus"
Perluas kemampuan Hermes Agent dengan alat dan paket keterampilan yang dapat digunakan kembali milik Anda sendiri.

Plugin
Buat Plugin Hermes
Gambaran Umum Alat
Gambaran Umum Keterampilan
MCP (Model Context Protocol)
Arsitektur
Menambahkan Alat
Membangun Keterampilan
tip
Untuk sebagian besar pembuatan alat kustom, mulailah dengan plugin. Halaman Menambahkan Alat ditujukan untuk pengembangan inti Hermes bawaan, bukan jalur pengguna/alat kustom yang biasa.

"Saya ingin melatih model"
Gunakan pembelajaran penguatan (reinforcement learning) untuk menyempurnakan perilaku model dengan alur pelatihan RL bawaan Hermes Agent.

Panduan Singkat
Konfigurasi
Pelatihan RL
Perutean Penyedia
Arsitektur
tip
Pelatihan RL akan berjalan paling baik jika Anda sudah memahami dasar-dasar cara Hermes Agent menangani percakapan dan panggilan alat. Jika Anda masih baru, ikuti jalur Pemula terlebih dahulu.

"Saya ingin menggunakannya sebagai pustaka Python"
Integrasikan Hermes Agent ke dalam aplikasi Python Anda secara terprogram.

Instalasi
Panduan Singkat
Panduan Pustaka Python
Arsitektur
Peralatan
Sesi
Fitur Utama Sekilas
Tidak yakin apa saja yang tersedia? Berikut adalah direktori singkat fitur-fitur utama:

Fitur	Apa Fungsinya	Link
Peralatan	Alat bawaan yang dapat dipanggil oleh agen (input/output file, pencarian, shell, dll.)	Peralatan
Keterampilan	Paket plugin yang dapat diinstal yang menambahkan kemampuan baru.	Keterampilan
Ingatan	Memori persisten antar sesi	Ingatan
Berkas Konteks	Masukkan file dan direktori ke dalam percakapan.	Berkas Konteks
MCP	Terhubung ke server alat eksternal melalui Protokol Konteks Model.	MCP
Cron	Jadwalkan tugas agen berulang.	Cron
Delegasi	Buat sub-agen untuk pekerjaan paralel.	Delegasi
Eksekusi Kode	Menjalankan skrip Python yang memanggil alat Hermes secara terprogram.	Eksekusi Kode
Browser	Penjelajahan web dan pengambilan data (scraping)	Browser
Kait	Callback dan middleware berbasis peristiwa	Kait
Pemrosesan Batch	Memproses banyak input secara massal.	Pemrosesan Batch
Pelatihan RL	Sempurnakan model dengan pembelajaran penguatan.	Pelatihan RL
Perutean Penyedia	Permintaan rute melintasi beberapa penyedia LLM.	Perutean Penyedia
Apa yang Harus Dibaca Selanjutnya
Berdasarkan lokasi Anda saat ini:

Baru saja selesai menginstal? → Buka Panduan Cepat untuk menjalankan percakapan pertama Anda.
Sudah menyelesaikan Panduan Cepat? → Baca Penggunaan dan Konfigurasi CLI untuk menyesuaikan pengaturan Anda.
Sudah menguasai dasar-dasarnya? → Jelajahi Alat , Keterampilan , dan Memori untuk membuka potensi penuh agen.
Sedang menyiapkan untuk sebuah tim? → Baca Keamanan dan Sesi untuk memahami kontrol akses dan manajemen percakapan.
Siap untuk membangun? → Masuk ke Panduan Pengembang untuk memahami cara kerjanya dan mulai berkontribusi.
Ingin contoh praktis? → Lihat bagian Panduan untuk proyek dan kiat-kiat dunia nyata.
tip
Anda tidak perlu membaca semuanya. Pilih jalur yang sesuai dengan tujuan Anda, ikuti tautan secara berurutan, dan Anda akan segera produktif. Anda selalu dapat kembali ke halaman ini untuk menemukan langkah selanjutnya.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Antarmuka CLI
CLI Hermes Agent adalah antarmuka pengguna terminal (TUI) lengkap — bukan UI web. Fitur-fiturnya meliputi pengeditan multi-baris, pelengkapan otomatis perintah slash, riwayat percakapan, interupsi dan pengalihan, serta output alat streaming. Dirancang untuk orang-orang yang terbiasa bekerja di terminal.

tip
Hermes juga menyertakan TUI modern dengan overlay modal, pemilihan menggunakan mouse, dan input non-blocking. Luncurkan dengan hermes --tui— lihat panduan TUI .

Menjalankan CLI
# Start an interactive session (default)
hermes

# Single query mode (non-interactive)
hermes chat -q "Hello"

# With a specific model
hermes chat --model "anthropic/claude-sonnet-4"

# With a specific provider
hermes chat --provider nous        # Use Nous Portal
hermes chat --provider openrouter  # Force OpenRouter

# With specific toolsets
hermes chat --toolsets "web,terminal,skills"

# Start with one or more skills preloaded
hermes -s hermes-agent-dev,github-auth
hermes chat -s github-pr-workflow -q "open a draft PR"

# Resume previous sessions
hermes --continue             # Resume the most recent CLI session (-c)
hermes --resume <session_id>  # Resume a specific session by ID (-r)

# Verbose mode (debug output)
hermes chat --verbose

# Isolated git worktree (for running multiple agents in parallel)
hermes -w                         # Interactive mode in worktree
hermes -w -q "Fix issue #123"     # Single query in worktree


Tata Letak Antarmuka
Pratinjau bergaya dari tata letak CLI Hermes yang menampilkan banner, area percakapan, dan prompt input tetap.
Banner CLI Hermes, alur percakapan, dan prompt input tetap ditampilkan sebagai gambar dokumentasi yang stabil, bukan seni teks yang rapuh.

Banner selamat datang menampilkan model Anda, backend terminal, direktori kerja, alat yang tersedia, dan keterampilan yang terpasang secara sekilas.

Bilah Status
Bilah status permanen terletak di atas area input, dan diperbarui secara real-time:

 ⚕ claude-sonnet-4-20250514 │ 12.4K/200K │ [██████░░░░] 6% │ $0.06 │ 15m


Elemen	Keterangan
Nama model	Model saat ini (dipersingkat jika lebih panjang dari 26 karakter)
Jumlah token	Token konteks yang digunakan / jendela konteks maksimum
Bilah konteks	Indikator pengisian visual dengan ambang batas berkode warna
Biaya	Perkiraan biaya sesi (atau n/auntuk model yang tidak diketahui/berharga nol)
🗜️ N	Jumlah kompresi konteks — berapa kali sesi yang sedang berjalan telah dikompresi secara otomatis. Muncul sekali saat kompresi pertama kali dijalankan.
▶ N	Tugas latar belakang aktif — berapa banyak /backgroundperintah yang masih berjalan dalam sesi saat ini. Muncul setiap kali setidaknya satu tugas sedang berjalan.
Lamanya	Waktu sesi yang telah berlalu
⚠ YOLO	Peringatan mode YOLO — ditampilkan setiap kali HERMES_YOLO_MODEdiaktifkan (baik hermes --yolosaat diluncurkan atau /yolodiaktifkan di tengah sesi). Meniru peringatan baris banner sehingga Anda tidak akan lupa bahwa Anda berada dalam mode persetujuan otomatis.
Bar tersebut menyesuaikan dengan lebar terminal — tata letak penuh pada ≥ 76 kolom, ringkas pada 52–75 kolom, minimal (model + durasi, ditambah lencana YOLO saat aktif) di bawah 52 kolom.

Pemberian kode warna kontekstual:

Warna	Ambang	Arti
Hijau	< 50%	Ruang yang luas
Kuning	50–80%	Merasa kenyang
Oranye	80–95%	Mendekati batas
Merah	≥ 95%	Hampir meluap — pertimbangkan/compress
Gunakan /usageuntuk rincian lengkap termasuk biaya per kategori (token input vs token output).

Tampilan Lanjutan Sesi
Saat melanjutkan sesi sebelumnya ( hermes -catau hermes --resume <id>), panel "Percakapan Sebelumnya" muncul di antara banner dan prompt input, menampilkan ringkasan singkat riwayat percakapan. Lihat Sesi — Ringkasan Percakapan saat Melanjutkan untuk detail dan konfigurasi.

Tombol pintasan
Kunci	Tindakan
Enter	Kirim pesan
Alt+Enter, Ctrl+J, atauShift+Enter	Baris baru (input multi-baris) Shift+Entermemerlukan terminal yang membedakannya dari Enter— lihat di bawah. Pada Windows Terminal, Alt+Enterditangkap oleh terminal (tombol layar penuh); gunakan Ctrl+Enteratau Ctrl+Jsebagai gantinya.
Alt+V	Tempel gambar dari papan klip jika didukung oleh terminal.
Ctrl+V	Tempel teks dan lampirkan gambar dari clipboard secara oportunistik.
Ctrl+B	Mulai/hentikan perekaman suara saat mode suara diaktifkan ( voice.record_key, default: ctrl+b)
Ctrl+G	Buka buffer input saat ini di $EDITOR(vim/nvim/nano/VS Code/dll.). Simpan dan keluar untuk mengirim teks yang diedit sebagai prompt berikutnya — ideal untuk prompt panjang yang terdiri dari beberapa paragraf.
Ctrl+X Ctrl+E	Pengikatan alternatif ala Emacs untuk editor eksternal (perilaku sama seperti Ctrl+G).
Ctrl+C	Menginterupsi agen (tekan dua kali dalam 2 detik untuk memaksa keluar)
Ctrl+D	KELUAR
Ctrl+Z	Hentikan Hermes agar berjalan di latar belakang (khusus Unix). Jalankan fgdi shell untuk melanjutkan.
Tab	Terima saran otomatis (teks bayangan) atau perintah garis miring pelengkap otomatis.
Pratinjau tempel multi-baris. Saat Anda menempelkan blok multi-baris, CLI akan menampilkan pratinjau satu baris yang ringkas ( [pasted: 47 lines, 1,842 chars — press Enter to send]) alih-alih menampilkan seluruh muatan ke dalam scrollback. Konten lengkap tetap dikirim; ini hanya penyempurnaan tampilan.

Penghapusan Markdown dalam respons akhir. CLI menghapus bagian-bagian Markdown yang paling bertele-tele dan pembungkus **bold**( *italic*wrapper) dari balasan agen akhir sehingga balasan tersebut ditampilkan sebagai teks terminal yang mudah dibaca, bukan kode sumber mentah. Blok kode dan daftar tetap dipertahankan. Hal ini tidak memengaruhi platform gateway atau hasil alat — platform tersebut mempertahankan Markdown untuk rendering asli.

Perintah Garis Miring
Ketik /untuk melihat menu tarik-turun pelengkap otomatis. Hermes mendukung sejumlah besar perintah slash CLI, perintah skill dinamis, dan perintah cepat yang ditentukan pengguna.

Contoh umum:

Memerintah	Keterangan
/help	Tampilkan bantuan perintah
/model	Tampilkan atau ubah model saat ini
/tools	Daftar alat yang tersedia saat ini
/skills browse	Jelajahi pusat keterampilan dan keterampilan opsional resmi.
/background <prompt>	Jalankan perintah dalam sesi latar belakang terpisah.
/skin	Tampilkan atau ganti tampilan CLI yang aktif.
/voice on	Aktifkan mode suara CLI (tekan Ctrl+Buntuk merekam)
/voice tts	Aktifkan/nonaktifkan pemutaran suara untuk balasan Hermes
/reasoning high	Tingkatkan upaya penalaran
/title My Session	Sebutkan nama sesi saat ini
/status	Tampilkan info sesi — model/profil/token/durasi — diikuti oleh blok rekap sesi lokal (jumlah giliran terbaru, alat teratas yang digunakan, file yang disentuh, perintah pengguna terbaru + balasan asisten). Komputasi lokal murni; tanpa panggilan LLM.
/sessions	Buka pemilih sesi interaktif langsung di dalam CLI klasik (antarmuka yang sama yang digunakan TUI). Ketik untuk memfilter, tombol panah untuk bernavigasi, Enter untuk melanjutkan.
Untuk daftar CLI dan pesan bawaan selengkapnya, lihat Referensi Perintah Slash .

Untuk pengaturan, penyedia layanan, penyetelan senyap, dan penggunaan suara untuk pesan/Discord, lihat Mode Suara .

tip
Perintah tidak peka terhadap huruf besar/kecil — /HELPberfungsi sama seperti /help. Skill yang terpasang juga secara otomatis menjadi perintah slash.

Perintah Cepat
Anda dapat menentukan perintah khusus yang menjalankan perintah shell secara instan tanpa memanggil LLM. Perintah ini berfungsi baik di CLI maupun platform perpesanan (Telegram, Discord, dll.).

# ~/.hermes/config.yaml
quick_commands:
  status:
    type: exec
    command: systemctl status hermes-agent
  gpu:
    type: exec
    command: nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader
  restart:
    type: alias
    target: /gateway restart


Kemudian ketik /status, /gpu, atau /restartdi obrolan mana pun. Lihat panduan Konfigurasi untuk contoh lainnya.

Keterampilan Pra-Pemuatan pada Saat Peluncuran
Jika Anda sudah mengetahui keterampilan mana yang ingin Anda aktifkan untuk sesi ini, berikan keterampilan tersebut saat memulai sesi:

hermes -s hermes-agent-dev,github-auth
hermes chat -s github-pr-workflow -s github-auth


Hermes loads each named skill into the session prompt before the first turn. The same flag works in interactive mode and single-query mode.

Skill Slash Commands
Every installed skill in ~/.hermes/skills/ is automatically registered as a slash command. The skill name becomes the command:

/gif-search funny cats
/axolotl help me fine-tune Llama 3 on my dataset
/github-pr-workflow create a PR for the auth refactor

# Just the skill name loads it and lets the agent ask what you need:
/excalidraw


Personalities
Set a predefined personality to change the agent's tone:

/personality pirate
/personality kawaii
/personality concise

Built-in personalities include: helpful, concise, technical, creative, teacher, kawaii, catgirl, pirate, shakespeare, surfer, noir, uwu, philosopher, hype.

You can also define custom personalities in ~/.hermes/config.yaml:

personalities:
  helpful: "You are a helpful, friendly AI assistant."
  kawaii: "You are a kawaii assistant! Use cute expressions..."
  pirate: "Arrr! Ye be talkin' to Captain Hermes..."
  # Add your own!


Multi-line Input
There are two ways to enter multi-line messages:

Alt+Enter, Ctrl+J, or Shift+Enter — inserts a new line
Backslash continuation — end a line with \ to continue:
❯ Write a function that:\
  1. Takes a list of numbers\
  2. Returns the sum

info
Pasting multi-line text is supported — use any of the newline keys above, or simply paste content directly.

Shift+Enter compatibility
Most terminals send the same byte sequence for Enter and Shift+Enter by default, so applications cannot distinguish them. Hermes recognises Shift+Enter only when the terminal sends a distinct sequence via the Kitty keyboard protocol or xterm's modifyOtherKeys mode.

Terminal	Status
Kitty, foot, WezTerm, Ghostty	Distinct Shift+Enter enabled by default
iTerm2 (recent), Alacritty, VS Code terminal, Warp	Supported once the Kitty protocol is enabled in settings
Windows Terminal Preview 1.25+	Supported once the Kitty protocol is enabled in settings
macOS Terminal.app, stock Windows Terminal (stable)	Not supported — Shift+Enter is indistinguishable from Enter
Where the terminal cannot distinguish them, Alt+Enter and Ctrl+J continue to work everywhere. On Windows Terminal specifically, Alt+Enter is captured by the terminal (toggles fullscreen) and never reaches Hermes — use Ctrl+Enter (delivered as Ctrl+J) or Ctrl+J directly for a newline.

Interrupting the Agent
You can interrupt the agent at any point:

Type a new message + Enter while the agent is working — it interrupts and processes your new instructions
Ctrl+C — interrupt the current operation (press twice within 2s to force exit)
In-progress terminal commands are killed immediately (SIGTERM, then SIGKILL after 1s)
Multiple messages typed during interrupt are combined into one prompt
Busy Input Mode
The display.busy_input_mode config key controls what happens when you press Enter while the agent is working:

Mode	Behavior
"interrupt" (default)	Your message interrupts the current operation and is processed immediately
"queue"	Your message is silently queued and sent as the next turn after the agent finishes
"steer"	Your message is injected into the current run via /steer, arriving at the agent after the next tool call — no interrupt, no new turn
# ~/.hermes/config.yaml
display:
  busy_input_mode: "steer"   # or "queue" or "interrupt" (default)


"queue"Mode ini berguna ketika Anda ingin menyiapkan pesan tindak lanjut tanpa sengaja membatalkan pekerjaan yang sedang berjalan. "steer"Mode ini berguna ketika Anda ingin mengarahkan ulang agen di tengah tugas tanpa mengganggu — misalnya, "sebenarnya, periksa juga pengujiannya" saat agen masih mengedit kode. Nilai yang tidak diketahui akan kembali ke "interrupt".

"steer"memiliki dua mekanisme cadangan otomatis: jika agen belum dimulai, atau jika gambar dilampirkan, pesan akan kembali ke "queue"perilaku default sehingga tidak ada yang hilang.

Anda juga dapat mengubahnya di dalam CLI:

/busy queue
/busy steer
/busy interrupt
/busy status

Petunjuk sentuhan pertama
Saat pertama kali Anda menekan Enter ketika Hermes sedang bekerja, Hermes akan mencetak pengingat satu baris yang menjelaskan /busytombol tersebut ( "(tip) Your message interrupted the current run…"). Pengingat ini hanya muncul sekali per instalasi — sebuah flag di config.yamlbawah onboarding.seen.busy_input_promptmenguncinya. Hapus tombol tersebut untuk melihat petunjuknya lagi.

Menangguhkan ke Latar Belakang
Pada sistem Unix, tekan Ctrl+Zuntuk menangguhkan Hermes ke latar belakang — sama seperti proses terminal lainnya. Shell akan mencetak konfirmasi:

Hermes Agent has been suspended. Run `fg` to bring Hermes Agent back.


Ketikkan perintah fgdi shell Anda untuk melanjutkan sesi tepat di tempat Anda berhenti. Fitur ini tidak didukung di Windows.

Tampilan Kemajuan Alat
CLI menampilkan umpan balik animasi saat agen bekerja:

Animasi berpikir (selama panggilan API):

  ◜ (｡•́︿•̀｡) pondering... (1.2s)
  ◠ (⊙_⊙) contemplating... (2.4s)
  ✧٩(ˊᗜˋ*)و✧ got it! (3.1s)

Umpan eksekusi alat:

  ┊ 💻 terminal `ls -la` (0.3s)
  ┊ 🔍 web_search (1.2s)
  ┊ 📄 web_extract (2.1s)

Berganti-ganti antar mode tampilan dengan /verbose: off → new → all → verbose. Perintah ini juga dapat diaktifkan untuk platform perpesanan — lihat konfigurasi .

Panjang Pratinjau Alat
Tombol display.tool_preview_lengthkonfigurasi mengontrol jumlah maksimum karakter yang ditampilkan dalam baris pratinjau panggilan alat (misalnya jalur file, perintah terminal). Nilai defaultnya adalah 0, yang berarti tidak ada batasan — jalur dan perintah lengkap akan ditampilkan.

# ~/.hermes/config.yaml
display:
  tool_preview_length: 80   # Truncate tool previews to 80 chars (0 = no limit)


Ini berguna pada terminal dengan layar sempit atau ketika argumen alat berisi jalur file yang sangat panjang.

Manajemen Sesi
Melanjutkan Sesi
Saat Anda keluar dari sesi CLI, perintah resume akan dicetak:

Resume this session with:
  hermes --resume 20260225_143052_a1b2c3

Session:        20260225_143052_a1b2c3
Duration:       12m 34s
Messages:       28 (5 user, 18 tool calls)


Opsi resume:

hermes --continue                          # Resume the most recent CLI session
hermes -c                                  # Short form
hermes -c "my project"                     # Resume a named session (latest in lineage)
hermes --resume 20260225_143052_a1b2c3     # Resume a specific session by ID
hermes --resume "refactoring auth"         # Resume by title
hermes -r 20260225_143052_a1b2c3           # Short form


Melanjutkan percakapan akan memulihkan seluruh riwayat percakapan dari SQLite. Agen akan melihat semua pesan, panggilan alat, dan respons sebelumnya — seolah-olah Anda tidak pernah berhenti.

Gunakan /title My Session Namedi dalam obrolan untuk memberi nama sesi saat ini, atau hermes sessions rename <id> <title>dari baris perintah. Gunakan hermes sessions listuntuk menelusuri sesi sebelumnya.

Penyimpanan Sesi
Sesi CLI disimpan dalam basis data status SQLite Hermes di bawah ~/.hermes/state.db. Basis data tersebut menyimpan:

metadata sesi (ID, judul, stempel waktu, penghitung token)
riwayat pesan
silsilah di seluruh sesi yang dikompresi/dilanjutkan
indeks pencarian teks lengkap yang digunakan olehsession_search
Beberapa adaptor perpesanan juga menyimpan file transkrip per platform di samping basis data, tetapi CLI itu sendiri melanjutkan dari penyimpanan sesi SQLite.

Kompresi Konteks
Percakapan panjang akan secara otomatis diringkas ketika mendekati batas konteks:

# In ~/.hermes/config.yaml
compression:
  enabled: true
  threshold: 0.50    # Compress at 50% of context limit by default

# Summarization model configured under auxiliary:
auxiliary:
  compression:
    model: ""  # Leave empty to use the main chat model (default). Or pin a cheap fast model, e.g. "google/gemini-3-flash-preview".


Saat kompresi dipicu, putaran tengah diringkas sementara 3 putaran pertama dan 20 putaran terakhir selalu dipertahankan.

Sesi Latar Belakang
Jalankan perintah dalam sesi latar belakang terpisah sambil terus menggunakan CLI untuk pekerjaan lain:

/background Analyze the logs in /var/log and summarize any errors from today


Hermes segera mengkonfirmasi tugas tersebut dan memberikan petunjuknya kepada Anda:

🔄 Background task #1 started: "Analyze the logs in /var/log and summarize..."
   Task ID: bg_143022_a1b2c3


Cara Kerjanya
Setiap /backgroundperintah memunculkan sesi agen yang sepenuhnya terpisah dalam thread daemon:

Percakapan terisolasi — agen latar belakang tidak mengetahui riwayat sesi Anda saat ini. Agen tersebut hanya menerima perintah yang Anda berikan.
Konfigurasi yang sama — agen latar belakang mewarisi model, penyedia, perangkat, pengaturan penalaran, dan model cadangan Anda dari sesi saat ini.
Tidak memblokir — sesi latar depan Anda tetap sepenuhnya interaktif. Anda dapat mengobrol, menjalankan perintah, atau bahkan memulai lebih banyak tugas latar belakang.
Beberapa tugas — Anda dapat menjalankan beberapa tugas latar belakang secara bersamaan. Masing-masing mendapatkan ID bernomor.
Hasil
Saat tugas latar belakang selesai, hasilnya akan muncul sebagai panel di terminal Anda:

╭─ ⚕ Hermes (background #1) ──────────────────────────────────╮
│ Found 3 errors in syslog from today:                         │
│ 1. OOM killer invoked at 03:22 — killed process nginx        │
│ 2. Disk I/O error on /dev/sda1 at 07:15                      │
│ 3. Failed SSH login attempts from 192.168.1.50 at 14:30      │
╰──────────────────────────────────────────────────────────────╯


Jika tugas gagal, Anda akan melihat pemberitahuan kesalahan. Jika display.bell_on_completediaktifkan dalam konfigurasi Anda, bel terminal akan berbunyi saat tugas selesai.

Kasus Penggunaan
Penelitian jangka panjang — "/penelitian latar belakang perkembangan terbaru dalam koreksi kesalahan kuantum" sambil Anda mengerjakan kode
Pemrosesan berkas — "/background menganalisis semua berkas Python di repositori ini dan mencantumkan masalah keamanan apa pun" sambil Anda melanjutkan percakapan
Investigasi paralel — jalankan beberapa tugas latar belakang untuk mengeksplorasi berbagai sudut pandang secara bersamaan.
informasi
Sesi latar belakang tidak muncul dalam riwayat percakapan utama Anda. Sesi ini merupakan sesi mandiri dengan ID tugasnya sendiri (misalnya, bg_143022_a1b2c3).

Mode Senyap
Secara default, CLI berjalan dalam mode senyap yang:

Menekan pencatatan log yang bertele-tele dari alat.
Mengaktifkan umpan balik animasi bergaya kawaii.
Menjaga agar hasil keluaran tetap bersih dan mudah digunakan.
Untuk output debug:

hermes chat --verbose
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
TUI
TUI adalah antarmuka pengguna modern untuk Hermes — antarmuka terminal yang didukung oleh runtime Python yang sama dengan CLI Klasik . Agen yang sama, sesi yang sama, perintah slash yang sama; permukaan yang lebih bersih dan responsif untuk berinteraksi dengannya.

Ini adalah cara yang direkomendasikan untuk menjalankan Hermes secara interaktif.

Meluncurkan
# Launch the TUI
hermes --tui

# Resume the latest TUI session (falls back to the latest classic session)
hermes --tui -c
hermes --tui --continue

# Resume a specific session by ID or title
hermes --tui -r 20260409_000000_aa11bb
hermes --tui --resume "my t0p session"

# Run source directly — skips the prebuild step (for TUI contributors)
hermes --tui --dev


Anda juga dapat mengaktifkannya melalui variabel lingkungan:

export HERMES_TUI=1
hermes          # now uses the TUI
hermes chat     # same

CLI klasik tetap tersedia sebagai default. Apa pun yang didokumentasikan dalam Antarmuka CLI — perintah slash, perintah cepat, pra-pemuatan keterampilan, kepribadian, input multi-baris, interupsi — berfungsi identik di TUI.

Mengapa TUI?
Tampilan pertama instan — banner muncul sebelum aplikasi selesai dimuat, sehingga terminal tidak pernah terasa macet saat Hermes sedang dimulai.
Input non-blokir — ketik dan antrekan pesan sebelum sesi siap. Perintah pertama Anda akan terkirim saat agen online.
Overlay yang kaya — pemilih model, pemilih sesi, permintaan persetujuan dan klarifikasi semuanya ditampilkan sebagai panel modal, bukan alur sebaris.
Panel sesi langsung — alat dan keterampilan akan diperkenalkan secara bertahap seiring berjalannya sesi.
Seleksi ramah mouse — seret untuk menyorot dengan latar belakang seragam, bukan invers SGR. Salin dengan gerakan salin normal terminal Anda.
Rendering layar bergantian — pembaruan diferensial berarti tidak ada kedipan saat streaming, tidak ada tampilan gulir balik yang berantakan setelah Anda keluar.
Fitur-fitur Composer — tempel-ciutkan sebaris untuk cuplikan panjang, Cmd+Vtempel Ctrl+Vteks dengan fallback gambar clipboard, keamanan tempel dalam tanda kurung, dan normalisasi lampiran gambar/jalur file.
Tampilan dan kepribadian yang sama berlaku. Beralih di tengah sesi dengan /skin ares, /personality pirate, dan UI akan diperbarui secara langsung. Lihat Tampilan & Tema untuk daftar lengkap tombol yang dapat disesuaikan dan mana yang berlaku untuk klasik vs TUI — TUI menghormati palet banner, warna UI, glyph/warna prompt, tampilan sesi, menu penyelesaian, latar belakang pemilihan, tool_prefix, dan help_header.

Bagian spanduk yang dapat dilipat
Banner startup TUI mengelompokkan informasi runtime ke dalam empat bagian yang dapat dilipat, masing-masing ditampilkan dengan tanda panah ▸/ ▾di samping judul bagian:

Bagian	Keadaan default
Peralatan	Membuka
Keterampilan	Runtuh
Perintah Sistem	Runtuh
Server MCP	Runtuh
Klik di mana saja pada header bagian (atau tanda panahnya) untuk mengaktifkan atau menonaktifkannya. Daftar Alat terbuka secara default karena merupakan bagian yang paling sering dicentang saat sesi dimulai; Keterampilan, Perintah Sistem, dan Server MCP tertutup secara default sehingga banner tetap ringkas meskipun Anda telah menginstal lusinan keterampilan atau menghubungkan banyak server MCP. Status bersifat lokal untuk instance banner, sehingga peluncuran berikutnya akan diatur ulang ke pengaturan default.

Persyaratan
Node.js ≥ 20 — TUI berjalan sebagai subproses yang diluncurkan dari CLI Python. hermes doctorIni memverifikasinya.
TTY — seperti CLI klasik, pengalihan stdin atau menjalankan di lingkungan non-interaktif akan kembali ke mode kueri tunggal.
Saat pertama kali diluncurkan, Hermes menginstal dependensi Node TUI ke dalam ui-tui/node_modules(sekali saja, beberapa detik). Peluncuran selanjutnya akan cepat. Jika Anda menarik versi Hermes yang baru, bundel TUI akan dibangun ulang secara otomatis ketika sumbernya lebih baru daripada distribusinya.

Pra-bangun eksternal
Distribusi yang mengirimkan bundel yang sudah dibuat sebelumnya (Nix, paket sistem) dapat mengarahkan Hermes ke sana:

export HERMES_TUI_DIR=/path/to/prebuilt/ui-tui
hermes --tui


Direktori tersebut harus berisi dist/entry.js.

Tombol pintasan
Pengaturan tombol pintas sama persis dengan CLI Klasik . Satu-satunya perbedaan perilaku adalah:

Seret mouse akan menyorot teks dengan latar belakang seleksi yang seragam.
Cmd+VPertama -Ctrl+V tama mencoba menempelkan teks biasa, kemudian beralih ke pembacaan clipboard OSC52/asli, dan akhirnya melampirkan gambar ketika isi clipboard atau teks yang ditempelkan berupa gambar.
/terminal-setupMenginstal binding terminal VS Code / Cursor / Windsurf lokal untuk Cmd+Enterkesamaan fungsi undo/redo yang lebih baik di macOS.
Fitur pelengkapan otomatis Slash terbuka sebagai panel mengambang dengan deskripsi, bukan sebagai menu tarik-turun sebaris.
Ctrl+X— Saat pesan yang mengantre disorot (dikirim saat agen masih berjalan), hapus pesan tersebut dari antrean. EscMembatalkan pengeditan dan membatalkan penyorotan tanpa menghapus.
Ctrl+G/Ctrl+X Ctrl+E — membuka buffer input saat ini $EDITORuntuk komposisi multi-baris / prompt panjang; simpan dan keluar mengirimkan kembali isinya sebagai prompt.
Perintah garis miring
Semua perintah slash berfungsi tanpa perubahan. Beberapa di antaranya merupakan milik TUI — perintah ini menghasilkan output yang lebih kaya atau ditampilkan sebagai overlay alih-alih panel sebaris:

Memerintah	Perilaku TUI
/help	Overlay dengan perintah yang dikategorikan, dapat dinavigasi dengan tombol panah.
/sessions	Pemilih sesi modal — pratinjau, judul, jumlah token, lanjutkan secara langsung
/model	Pemilih model modal yang dikelompokkan berdasarkan penyedia, dengan petunjuk biaya.
/skin	Pratinjau langsung — perubahan tema diterapkan saat Anda menjelajahi
/details	Alihkan tampilan detail panggilan alat (global atau per bagian)
/usage	Panel token/biaya/konteks yang kaya
/agents(alias /tasks)	Lapisan pengamatan — pohon subagen langsung dengan kontrol matikan/jeda, rangkuman biaya/token/file per cabang, riwayat langkah demi langkah.
/reload	Membaca ulang ~/.hermes/.envke dalam proses TUI yang sedang berjalan sehingga kunci API yang baru ditambahkan berlaku tanpa perlu memulai ulang.
/mouse [on|off|toggle|wheel|buttons|all]	Pilih preset pelacakan mouse saat runtime (juga tersimpan display.mouse_trackingdi config.yaml). wheel(1000+1006) mempertahankan pengguliran roda gulir tanpa peristiwa hover yang membuat tmux mengirimkan pesan "Tidak ada gambar di clipboard" berulang kali pada baris prompt; buttonsmenambahkan seret untuk memilih; allmerupakan default dengan UI yang digerakkan oleh hover.
Semua perintah slash lainnya (termasuk skill yang terpasang, perintah cepat, dan pengaktifan/penonaktifan kepribadian) berfungsi identik dengan CLI klasik. Lihat Referensi Perintah Slash .

Rendering matematika LaTeX
Pipeline markdown TUI merender matematika LaTeX secara inline: $E = mc^2$dan $$\frac{a}{b}$$merender sebagai matematika berformat Unicode, bukan kode sumber TeX mentah. Berfungsi untuk matematika inline dan blok; sintaks yang tidak didukung akan kembali menampilkan TeX literal yang dibungkus dalam rentang kode sehingga tetap dapat disalin.

Ini selalu aktif — tidak perlu dikonfigurasi. CLI klasik mempertahankan TeX mentah.

Deteksi terminal cahaya
TUI secara otomatis mendeteksi terminal berwarna terang dan beralih ke tema terang sesuai kebutuhan. Deteksi bekerja dalam tiga lapisan:

HERMES_TUI_THEMEVariabel lingkungan — prioritas tertinggi. Nilai: light, dark, atau heksadesimal latar belakang 6 karakter mentah (misalnya ffffff, 1a1a2e).
COLORFGBGVariabel lingkungan — petunjuk klasik "apa warna latar belakang saya?" yang digunakan oleh terminal turunan xterm.
Pemeriksaan latar belakang terminal melalui OSC 11 — berfungsi pada terminal modern (Ghostty, Warp, iTerm2, WezTerm, Kitty) yang tidak mengatur COLORFGBG.
Jika Anda menginginkan tema terang secara permanen terlepas dari perangkat yang digunakan:

export HERMES_TUI_THEME=light

Gaya indikator sibuk
Indikator sibuk di bilah status dapat diubah — secara default, palet wajah kawaii Hermes berputar setiap 2,5 detik selama agen bekerja. Pilih gaya yang berbeda melalui konfigurasi atau /indicatorperintah slash:

display:
  tui_status_indicator: kaomoji   # kaomoji | emoji | unicode | ascii


Atau dalam sesi: /indicator emoji(dll.). Gaya dikirimkan dengan lebar glyph yang sesuai sehingga bagian lain dari bilah status tidak bergetar saat diputar.

Lanjutkan secara otomatis
Secara default, hermes --tuisesi baru akan dimulai setiap kali aplikasi diluncurkan. Untuk menyambungkan kembali ke sesi TUI terbaru secara otomatis (berguna ketika koneksi terminal atau SSH Anda terputus secara tiba-tiba), pilih opsi ini:

export HERMES_TUI_RESUME=1          # most-recent TUI session
# or:
export HERMES_TUI_RESUME=<session-id>   # specific session


Hapus variabel atau berikan --resume <id>secara eksplisit untuk menimpa pengaturan pada setiap peluncuran.

Baris status
Sistem status TUI melacak status agen secara real-time:

Status	Arti
starting agent…	ID sesi sudah aktif; alat dan keterampilan masih terus dikembangkan. Anda dapat mengetik — pesan akan mengantre dan dikirim saat sudah siap.
ready	Agen dalam keadaan diam, menerima masukan.
thinking…/running…	Agen sedang melakukan penalaran atau menjalankan suatu alat.
interrupted	Giliran saat ini dibatalkan; tekan Enter untuk mengirim lagi.
forging session…/resuming…	Kontak awal atau --resumejabat tangan.
Warna dan ambang batas bilah status per-skin sama dengan CLI klasik — lihat Skin untuk penyesuaian.

Baris status juga menampilkan:

Direktori kerja dengan cabang git — ~/projects/hermes-agent (docs/two-week-gap-sweep). Akhiran cabang diperbarui saat Anda git checkoutberada di terminal samping (cache mtime) sehingga TUI mencerminkan cabang aktif Anda yang sebenarnya, bukan cabang yang ada saat peluncuran.
Waktu yang berlalu per perintah — ⏱ 12s/3m 45ssaat giliran sedang berjalan (langsung), dibekukan ⏲ 32s / 3m 45ssetelah giliran selesai. Angka pertama adalah waktu sejak pesan pengguna terakhir; angka kedua adalah total durasi sesi. Diatur ulang setiap kali ada perintah baru.
🗜️ N— Jumlah kali sesi yang sedang berjalan telah dikompresi secara otomatis. Muncul sekali saat kompresi pertama kali dijalankan.
▶ N— jumlah /backgroundtugas yang sedang berjalan dalam sesi ini. Muncul setiap kali setidaknya satu tugas sedang berjalan.
⚠ YOLO— peringatan yang terlihat setiap kali mode YOLO diaktifkan ( hermes --yolo, /yolo, atau HERMES_YOLO_MODE=1). Lencana yang sama juga muncul di banner startup sehingga Anda tidak dapat meluncurkan sesi persetujuan otomatis tanpa menyadarinya.
Konfigurasi
TUI menghormati semua konfigurasi standar Hermes: ~/.hermes/config.yamlprofil, kepribadian, tampilan, perintah cepat, kumpulan kredensial, penyedia memori, pengaktifan alat/keterampilan. Tidak ada file konfigurasi khusus TUI.

Sejumlah tombol tertentu mengatur antarmuka TUI secara spesifik:

display:
  skin: default              # any built-in or custom skin
  personality: helpful
  details_mode: collapsed    # hidden | collapsed | expanded — global accordion default
  sections:                  # optional: per-section overrides (any subset)
    thinking: expanded       # always open
    tools: expanded          # always open
    activity: collapsed      # opt back IN to the activity panel (hidden by default)
  mouse_tracking: all        # off | wheel | buttons | all (or true/false for back-compat).
                             #   wheel   — 1000+1006 (scroll + click; no drag, no hover —
                             #             recommended inside tmux to silence the prompt-row
                             #             "No image in clipboard" spam from hover events)
                             #   buttons — adds 1002 for terminal-side drag selection
                             #   all     — adds 1003 for hover (scrollbar paginate-on-hover,
                             #             link mouseenter, etc.)


Tombol pengaktifan/penonaktifan saat runtime:

/details [hidden|collapsed|expanded|cycle]— atur mode global
/details <section> [hidden|collapsed|expanded|reset]— menimpa satu bagian (bagian: thinking, tools, subagents, activity)
Visibilitas default

TUI dilengkapi dengan pengaturan default per bagian yang memberikan opini tertentu, yang menampilkan transkrip langsung alih-alih deretan tanda panah:

thinking— diperluas . Alur penalaran berjalan serempak saat model memancarkannya.
tools— diperluas . Panggilan alat dan hasilnya ditampilkan secara terbuka.
subagents— diteruskan ke global details_mode(tertutup di bawah tanda panah secara default — tetap diam sampai delegasi benar-benar terjadi).
activity— tersembunyi . Meta ambien (petunjuk gerbang, pengingat kesamaan terminal, pemberitahuan latar belakang) adalah gangguan untuk sebagian besar penggunaan sehari-hari. Kegagalan alat masih ditampilkan langsung pada baris alat yang gagal; kesalahan/peringatan ambien muncul melalui latar belakang peringatan mengambang ketika setiap panel disembunyikan.
Pengaturan per bagian akan diutamakan daripada pengaturan default bagian maupun pengaturan global details_mode. Untuk mengubah tata letak:

display.sections.thinking: collapsed— kembalikan pemikiran ke bawah tanda panah
display.sections.tools: collapsed— kembalikan panggilan alat ke bawah tanda panah
display.sections.activity: collapsed— aktifkan kembali panel aktivitas
/details <section> <mode>saat dijalankan
Apa pun yang diatur secara eksplisit akan display.sectionsmengalahkan pengaturan default, sehingga konfigurasi yang ada tetap berfungsi tanpa perubahan.

Sesi
Sesi dibagikan antara TUI dan CLI klasik — keduanya menulis ke file yang sama ~/.hermes/state.db. Anda dapat memulai sesi di satu tempat, dan melanjutkannya di tempat lain. Pemilih sesi menampilkan sesi dari kedua sumber, dengan tag sumber.

Lihat Sesi untuk siklus hidup, pencarian, kompresi, dan ekspor.

Menghubungkan ke gateway yang sedang berjalan
Secara default, TUI menjalankan gateway in-process-nya sendiri, sehingga setiap instance TUI bersifat mandiri. Jika Anda sudah memiliki gateway yang berjalan dalam jangka panjang (misalnya hermes gateway rundi tmux, atau layanan systemd/launchd), Anda dapat mengarahkan TUI ke gateway tersebut — TUI kemudian menjadi thin client dan berbagi status dengan setiap surface lain (platform perpesanan, dashboard web, sesi TUI lainnya) yang terhubung ke gateway yang sama.

Atur URL websocket melalui variabel lingkungan sebelum meluncurkan aplikasi:

export HERMES_TUI_GATEWAY_URL="ws://localhost:8765/api/ws?token=<auth-token>"
hermes --tui


Token tersebut berasal dari konfigurasi otentikasi API gateway (lihat Server API ). Saat variabel lingkungan diatur, TUI:

Melewatkan pembuatan gateway lokal sepenuhnya — tidak ada adaptor platform duplikat, tidak ada konflik port.
Mengarahkan setiap aksi (perintah slash, melampirkan gambar, kemajuan browser, peristiwa suara, ...) melalui websocket ke gateway bersama.
Terhubung kembali secara otomatis jika URL gateway berubah (token baru) di antara permintaan.
Ini adalah saluran yang sama yang digunakan oleh TUI (Transaction Interface User) yang tertanam di dasbor web (lihat Dasbor Web ) — satu gerbang, banyak klien.

Kembali ke CLI klasik
Saat menjalankan hermes(tanpa --tui) tetap menggunakan CLI klasik. Untuk membuat mesin lebih menyukai TUI, atur HERMES_TUI=1di profil shell Anda. Untuk kembali, batalkan pengaturannya.

Jika TUI gagal diluncurkan (tidak ada Node, bundel hilang, masalah TTY), Hermes akan mencetak diagnostik dan menggunakan solusi alternatif — daripada membiarkan Anda terjebak.

Lihat juga
Antarmuka CLI — referensi lengkap perintah slash dan pintasan keyboard (bersama)
Sesi — ringkasan, cabang, dan riwayat
Skin & Tema — ubah tema banner, bilah status, dan overlay.
Mode Suara — berfungsi di kedua antarmuka
Konfigurasi — semua kunci konfigurasi
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Panduan Windows (Asli) — Beta Awal
Versi BETA awal
Dukungan Windows asli masih dalam versi beta awal . Program ini dapat diinstal, dijalankan, dan lolos pemeriksaan lint Windows kami, tetapi belum diuji coba secara menyeluruh seperti jalur Linux/macOS/WSL2 kami. Harapkan beberapa kekurangan — terutama terkait penanganan subproses, keanehan jalur, dan output konsol non-ASCII. Harap laporkan masalah dengan langkah-langkah reproduksi jika Anda menemukan sesuatu. Jika Anda menginginkan pengaturan yang sudah teruji hari ini, gunakan penginstal Linux/macOS di bawah WSL2 sebagai gantinya.

Hermes berjalan secara native di Windows 10 dan Windows 11 — tanpa WSL, tanpa Cygwin, tanpa Docker. Halaman ini adalah penjelasan mendalam: apa yang berfungsi secara native, apa yang hanya berfungsi dengan WSL, apa yang sebenarnya dilakukan oleh installer, dan pengaturan khusus Windows yang mungkin perlu Anda ubah.

Jika Anda hanya ingin menginstal, satu baris petunjuk di halaman arahan atau halaman Instalasi sudah cukup. Kembali lagi ke sini jika ada hal yang mengejutkan Anda.

Mau WSL saja?
Jika Anda lebih menyukai lingkungan POSIX asli (untuk terminal terintegrasi dasbor, forksemantik, pengawas file bergaya Linux, dll.), lihat Panduan Windows (WSL2) . Keduanya dapat berjalan berdampingan dengan baik: data asli berada di bawah %LOCALAPPDATA%\hermes, data WSL berada di bawah ~/.hermes.

Instalasi cepat
Buka PowerShell (atau Windows Terminal) dan jalankan perintah berikut:

iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)


Tidak memerlukan hak administrator. Installer akan masuk ke %LOCALAPPDATA%\hermes\dan menambahkan hermeske PATH pengguna Anda — buka terminal baru setelah selesai.

Opsi penginstal (membutuhkan formulir scriptblock untuk meneruskan parameter):

& ([scriptblock]::Create((irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1))) -NoVenv -SkipSetup -Branch main


Parameter	Bawaan	Tujuan
-Branch	main	Kloning cabang tertentu (berguna untuk menguji PR)
-Commit	batalkan	Tetapkan instalasi ke SHA commit tertentu (menggantikan -Branch)
-Tag	batalkan	Sematkan instalasi ke tag git tertentu (misalnya v0.14.0)
-NoVenv	mati	Lewati pembuatan venv (tingkat lanjut — Anda mengelola Python sendiri)
-SkipSetup	mati	hermes setupLewati wizard pasca-instalasi
-HermesHome	%LOCALAPPDATA%\hermes	Direktori data pengganti
-InstallDir	%LOCALAPPDATA%\hermes\hermes-agent	Lokasi kode penggantian
Installer secara otomatis mencoba ulang pengambilan data git yang tidak stabil dan menghapus BOM dari setiap install.ps1payload yang diunduh, sehingga BOM UTF-8 yang diambil selama transit HTTP tidak lagi merusak [scriptblock]::Create((irm ...))formulir.

Penginstal desktop (alternatif)
Installer GUI yang sederhana juga tersedia — berguna jika Anda lebih suka mengklik dua kali .exedaripada membuka PowerShell. Unduh Hermes Desktop, jalankan installer, dan pada peluncuran pertama, GUI akan memanggil fungsi install.ps1di balik layar untuk menyediakan Python (melalui uv), Node, PortableGit, dan sisa bootstrap dependensi yang dijelaskan di bawah ini. Setelah dijalankan pertama kali, aplikasi desktop dan CLI yang diinstal PowerShell berbagi direktori instalasi dan data hermesyang sama — beralihlah antara GUI dan CLI dengan bebas.%LOCALAPPDATA%\hermes\hermes-agent%USERPROFILE%\.hermes

Gunakan penginstal desktop jika Anda menginginkan pengalaman instalasi Windows yang familiar atau jika Anda menyerahkan Hermes kepada orang yang bukan pengembang; gunakan perintah satu baris PowerShell jika Anda sudah berada di terminal.

Bootstrap dependensi ( dep_ensure)
Saat pertama kali diluncurkan (dan sesuai permintaan ketika alat yang hilang terdeteksi), Hermes menjalankan program bootstrap Python kecil — hermes_cli/dep_ensure.pyyang memeriksa dan menginstal dependensi non-Python yang dibutuhkannya secara bertahap. Di Windows, dependensi yang relevan adalah:

Ketergantungan	Mengapa Hermes membutuhkannya?
PortableGit	Menyediakan bash.exealat terminal dan gitkloning dalam sesi. Disediakan pada saat instalasi, bukan oleh dep_ensure.
Node.js 22	Diperlukan untuk alat peramban ( agent-browser), jembatan web TUI, dan jembatan WhatsApp.
ffmpeg	Konversi format audio untuk TTS/pesan suara.
ripgrep	Pencarian file cepat — akan menggunakan metode lain grepjika tidak tersedia.
paket npm	agent-browserPlaywright Chromium, dan semua dependensi Node per-toolset diinstal sekali pada penggunaan browser-tool pertama kali.
Setiap dependensi memiliki shutil.which(...)pemeriksaan bergaya -; jika sebuah biner hilang dan eksekusinya interaktif, dep_ensureia menawarkan untuk menginstalnya (menyerahkan scripts\install.ps1 -ensure <dep>logika instalasi sebenarnya kepada). Eksekusi non-interaktif (gateway, cron, peluncuran desktop tanpa antarmuka grafis) melewati prompt dan menampilkan this feature needs <dep>kesalahan yang jelas sebagai gantinya.

Apa yang sebenarnya dilakukan oleh penginstal?
Dari atas ke bawah, secara berurutan:

Bootstrapsuv — Manajer Python cepat dari Astral. Diinstal ke %USERPROFILE%\.local\bin.
Menginstal Python 3.11 melalui uv. Tidak diperlukan Python yang sudah ada.
Menginstal Node.js 22 (winget jika tersedia, jika tidak, tarball Node portabel yang diekstrak di bawah %LOCALAPPDATA%\hermes\node). Digunakan untuk alat peramban dan jembatan WhatsApp.
Menginstal Git portabel — jika sudah ada di PATH, penginstal akan menggunakannya; jika tidak, ia akan mengunduh PortableGitgit yang dipangkas dan mandiri (~45 MB, dari rilis resmi ) ke . Tidak memerlukan hak administrator, tidak ada registri penginstal Windows, dan tidak ada gangguan dengan hal lain di komputer.git-for-windows%LOCALAPPDATA%\hermes\git
Mengkloning repositori ke %LOCALAPPDATA%\hermes\hermes-agentdan membuat virtualenv di dalamnya.
Bertingkatuv pip install — mencoba .[all]terlebih dahulu, kemudian beralih ke set yang ukurannya semakin kecil ( [messaging,dashboard,ext]→ [messaging]→ .) jika git+httpsdependensi mengalami masalah pada GitHub yang memiliki batasan laju. Mencegah mode kegagalan "satu masalah saja membuat Anda harus melakukan instalasi ulang".
Menginstal SDK perpesanan secara otomatis berdasarkan kunci .env— jika TELEGRAM_BOT_TOKEN/ DISCORD_BOT_TOKEN/ SLACK_BOT_TOKEN/ SLACK_APP_TOKEN/ WHATSAPP_ENABLEDada, maka akan dijalankan python -m ensurepip --upgradedan pip installpanggilan yang ditargetkan sehingga SDK setiap platform benar-benar dapat diimpor.
SetHERMES_GIT_BASH_PATH tersebut diselesaikan bash.exesehingga Hermes menemukannya secara pasti dalam cangkang baru.
Menambahkan %LOCALAPPDATA%\hermes\binke PATH pengguna — menampilkan hermesperintah setelah Anda membuka terminal baru.
Menjalankanhermes setup — wizard pengaturan awal normal (model, penyedia, perangkat). Lewati dengan -SkipSetup.
Lewati pencarian penyedia di Windows
Native Windows masih dalam versi beta awal, dan pengaturan kunci API per alat (Firecrawl, FAL, Penggunaan Browser, OpenAI TTS) adalah bagian yang paling rumit untuk mendapatkan agen yang berguna. Langganan Nous Portal mencakup model dan semua alat tersebut melalui satu login OAuth. Setelah penginstal selesai, jalankan hermes setup --portaluntuk menghubungkan semuanya.

Matriks fitur
Semua fitur kecuali panel terminal terintegrasi pada dasbor berjalan secara native di Windows.

Fitur	Windows Asli	WSL2
CLI ( hermes chat, hermes setup, hermes gateway, …)	✓	✓
TUI Interaktif ( hermes --tui)	✓	✓
Gerbang perpesanan (Telegram, Discord, Slack, WhatsApp, 15+ platform)	✓	✓
Penjadwal Cron	✓	✓
Alat peramban (Chromium melalui Node)	✓	✓
Server MCP (stdio dan HTTP)	✓	✓
Ollama Lokal / LM Studio / llama-server	✓	✓ (melalui jaringan WSL)
Dasbor web (sesi, pekerjaan, metrik, konfigurasi)	✓	✓
/chatPanel terminal terintegrasi dasbor	✗ (membutuhkan POSIX PTY)	✓
Mulai otomatis saat masuk	✓ (tugas-tugas)	✓ (systemd)
Tab dasbor /chatmenyematkan terminal sungguhan melalui POSIX PTY ( ptyprocess). Windows asli tidak memiliki primitif yang setara; ConPTY Python pywinpty/Windows akan berfungsi tetapi merupakan implementasi terpisah — anggap sebagai pekerjaan di masa mendatang. Bagian lain dari dasbor berfungsi secara native — hanya tab tersebut yang menampilkan banner "gunakan WSL2 untuk ini".

Cara Hermes menjalankan perintah shell di Windows
Alat terminal Hermes menjalankan perintah melalui Git Bash , strategi yang sama yang digunakan Claude Code. Ini menghindari kesenjangan POSIX-vs-Windows tanpa perlu menulis ulang setiap alat.

Perintah penyelesaian untuk bash.exe:

HERMES_GIT_BASH_PATHvariabel lingkungan jika diatur.
%LOCALAPPDATA%\hermes\git\usr\bin\bash.exe(PortableGit yang dikelola oleh penginstal).
%LOCALAPPDATA%\hermes\git\bin\bash.exe(Tata letak Git-for-Windows yang lebih lama).
Instalasi Git-for-Windows sistem ( %ProgramFiles%\Git\bin\bash.exe, dll.).
MSYS2, Cygwin, atau apa pun yang bash.exeada di PATH sebagai pilihan terakhir.
Installer HERMES_GIT_BASH_PATHsecara eksplisit mengatur agar sesi PowerShell baru tidak perlu melakukan pencarian ulang. Ganti pengaturan ini jika Anda ingin Hermes menggunakan bash tertentu — misalnya, Git Bash sistem Anda atau bash yang dihosting WSL melalui symlink.

Kesalahan umum: Tata letak MinGit berbeda dari penginstal Git-for-Windows lengkap — bash berada di bawah usr\bin\bash.exe, bukan bin\bash.exe. Hermes memeriksa keduanya. Jika Anda membongkar zip MinGit secara manual, pastikan Anda memilih varian non-busybox ( MinGit-*-64-bit.zip, bukan MinGit-*-busybox*.zip) — build busybox dikirimkan ashsebagai pengganti bashdan sebagian besar coreutils hilang.

Konsol UTF-8 di Windows
Stdio bawaan Python di Windows menggunakan halaman kode aktif konsol (biasanya cp1252 atau cp437). Banner Hermes, daftar perintah slash, umpan alat, panel Rich, dan deskripsi keterampilan semuanya berisi Unicode. Tanpa intervensi, semua itu akan mengalami crash dengan pesan kesalahan UnicodeEncodeError: 'charmap' codec can't encode character….

Perbaikan ada di hermes_cli/stdio.py::configure_windows_stdio(), dipanggil lebih awal di setiap titik masuk ( cli.py::main, hermes_cli/main.py::main, gateway/run.py::main). Ini:

Membalik halaman kode konsol ke CP_UTF8 (65001) melalui kernel32.SetConsoleCP/ SetConsoleOutputCP.
Mengonfigurasi ulang sys.stdout/ sys.stderr/ sys.stdinmenjadi UTF-8 dengan errors='replace'.
Set PYTHONIOENCODING=utf-8dan PYTHONUTF8=1(melalui setdefault, sehingga nilai pengguna eksplisit yang berlaku) sehingga subproses Python anak mewarisi UTF-8.
Mengatur EDITOR=notepadjika baik EDITORmaupun tidak VISUALdiatur (lihat bagian Editor di bawah).
Idempotent. Tidak melakukan apa pun pada sistem operasi selain Windows.

Nonaktifkan opsi ini: HERMES_DISABLE_WINDOWS_UTF8=1 di lingkungan tersebut akan kembali menggunakan jalur stdio cp1252 lama. Berguna untuk melakukan bisecting terhadap bug pengkodean; kemungkinan besar bukan pengaturan yang tepat dalam operasi normal.

Editor ( Ctrl-X Ctrl-E, /edit)
Sebelum #21561, menekan Ctrl-X Ctrl-Eatau mengetik /edittanpa suara tidak menghasilkan apa pun di Windows. prompt_toolkit memiliki daftar cadangan POSIX absolut yang dikodekan secara permanen ( /usr/bin/nano, /usr/bin/pico, /usr/bin/vi, …) yang tidak pernah terselesaikan di Windows — bahkan dengan Git for Windows versi lengkap yang terpasang.

Shim stdio Windows Hermes sekarang ditetapkan EDITOR=notepadsebagai default. Notepad disertakan dengan setiap instalasi Windows dan berfungsi sebagai editor yang memblokir — subprocess.call(["notepad", file])memblokir hingga jendela ditutup.

Pengaturan pengguna tetap diutamakan (pengaturan tersebut diperiksa sebelum setdefault):

Editor	Perintah PowerShell
VS Code	$env:EDITOR = "code --wait"
Notepad++	$env:EDITOR = "'C:\Program Files\Notepad++\notepad++.exe' -multiInst -nosession"
Neovim	$env:EDITOR = "nvim"
Spiral	$env:EDITOR = "hx"
Pengaturan ini --waitdi VS Code sangat penting — tanpanya editor akan langsung kembali dan Hermes akan mendapatkan buffer kosong.

Atur secara permanen di profil PowerShell Anda:

# In $PROFILE
$env:EDITOR = "code --wait"

Atau sebagai variabel lingkungan pengguna di Pengaturan Sistem sehingga setiap shell baru dapat menggunakannya.

Ctrl+Enteruntuk baris baru di CLI
Windows Terminal diteruskan Ctrl+Entersebagai urutan tombol khusus. Hermes mengikatnya ke "sisipkan baris baru" sehingga Anda dapat membuat prompt multi-baris di CLI tanpa harus kembali ke Esc-lalu- Enter. Berfungsi di Windows Terminal, terminal terintegrasi VS Code, dan host konsol Windows modern apa pun yang menghargai urutan escape VT.

Pada cmd.exekonsol lama, Ctrl+Entertampilannya berubah menjadi polos Enter— gunakan Esc Entersebagai gantinya, atau tingkatkan ke Windows Terminal (gratis dan terpasang secara default di Windows 11).

Menjalankan gateway saat login Windows
hermes gateway installPada Windows, aplikasi ini menggunakan Tugas Terjadwal dengan fallback folder Startup — tidak memerlukan hak administrator.

Memasang
hermes gateway install

Apa yang terjadi di balik layar:

schtasks /Create /SC ONLOGON /RL LIMITED /TN HermesGateway— mendaftarkan tugas yang berjalan saat Anda masuk dengan izin standar (bukan hak akses administrator). Tidak ada permintaan UAC.
Jika schtasks diblokir oleh kebijakan grup, maka akan beralih ke penulisan start /min cmd.exe /d /c <wrapper>pintasan ke %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup. Efeknya sama, hanya sedikit lebih kasar.
Memunculkan gateway secara terpisah melaluipythonw.exe — bukan python.exe. pythonw.exetidak memiliki konsol yang terpasang, yang melindunginya dari CTRL_C_EVENTsiaran dari proses saudara (masalah nyata yang dulu dapat mematikan gateway saat Anda menekan Ctrl+C pada apa pun dalam grup proses yang sama).
Bendera yang digunakan saat memunculkan objek: DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW | CREATE_BREAKAWAY_FROM_JOB.

Mengelola
hermes gateway status      # Merged view: schtasks + Startup folder + running PID
hermes gateway start       # Starts the scheduled task now
hermes gateway stop        # Graceful SIGTERM equivalent (TerminateProcess via psutil)
hermes gateway restart
hermes gateway uninstall   # Removes schtasks entry, Startup shortcut, pid file


hermes gateway statusBersifat idempoten — panggil fungsi ini seribu kali berturut-turut dan tidak akan pernah secara tidak sengaja mematikan gateway. (Sebelum PR #21561, hal itu terjadi secara diam-diam, melalui os.kill(pid, 0)benturan CTRL_C_EVENTdi level C — lihat "internal manajemen proses" di bawah jika Anda tertarik dengan ceritanya.)

Mengapa tidak menggunakan Windows Service?
Layanan memerlukan hak administrator untuk menginstal dan mengaitkan siklus hidup gateway dengan booting mesin, bukan login pengguna. Pengguna Hermes pada umumnya menginginkan: login → gateway tersedia, logout → gateway hilang. Tugas Terjadwal melakukan hal itu tanpa perlu peningkatan hak akses. Jika Anda benar-benar menginginkan layanan, gunakan nssmatau sc createinstal secara manual — tetapi kemungkinan besar Anda tidak membutuhkannya.

Tata letak data
Jalur	Isi
%LOCALAPPDATA%\hermes\hermes-agent\	Git checkout + venv. Aman untuk Remove-Item -Recursediinstal ulang.
%LOCALAPPDATA%\hermes\git\	PortableGit (hanya jika penginstal telah menyediakannya).
%LOCALAPPDATA%\hermes\node\	Node.js portabel (hanya jika penginstal telah menyediakannya).
%LOCALAPPDATA%\hermes\bin\	hermes.cmdshim, ditambahkan ke PATH Pengguna.
%USERPROFILE%\.hermes\	Konfigurasi, otentikasi, keterampilan, sesi, dan log Anda. Tetap tersimpan meskipun diinstal ulang.
Pemisahan ini disengaja: %LOCALAPPDATA%\hermesadalah infrastruktur sekali pakai (Anda dapat menghapusnya dan perintah satu baris akan mengembalikannya). %USERPROFILE%\.hermesadalah data Anda — konfigurasi, memori, keterampilan, riwayat sesi — dan bentuknya identik dengan instalasi Linux. Salin di antara mesin dan Hermes Anda akan ikut berpindah bersama Anda.

Timpa HERMES_HOME: atur variabel lingkungan untuk menunjuk ke direktori data yang berbeda. Berfungsi sama seperti di Linux.

Alat peramban
Alat peramban ini menggunakan agent-browser(pembantu Node) untuk menjalankan Chromium. Di Windows:

Installer menambahkan agent-browserke PATH melalui npm.
shutil.which("agent-browser", path=...)Secara otomatis mengambil .cmdshim — CreateProcessWtidak dapat mengeksekusi shebang tanpa ekstensi, jadi Hermes selalu menyelesaikan ke .CMDwrapper. Jangan memanggil skrip shebang secara manual; selalu melalui .cmd.
Playwright Chromium diinstal secara otomatis saat pertama kali dijalankan ( npx playwright install chromium). Jika instalasi gagal, hermes doctorakan ditampilkan dengan petunjuk perbaikan.
Menjalankan Hermes di Windows — catatan praktis
PATH setelah instalasi
Installer akan menambahkan %LOCALAPPDATA%\hermes\binke PATH pengguna Anda melalui [Environment]::SetEnvironmentVariable. Terminal yang sudah ada tidak akan mengambil ini — buka jendela PowerShell baru (atau tab Terminal Windows) setelah instalasi. Tutup dan buka kembali, jangan lakukan $env:PATH += …secara manual kecuali Anda tahu apa yang Anda lakukan.

Memeriksa:

Get-Command hermes        # should print C:\Users\<you>\AppData\Local\hermes\bin\hermes.cmd
hermes --version


Variabel lingkungan
Hermes menghormati variabel $env:Xlingkungan (lingkup proses) dan variabel lingkungan pengguna (permanen, diatur di Properti Sistem → Variabel Lingkungan). Mengatur kunci API di %USERPROFILE%\.hermes\.envjalur normal — sama seperti Linux:

OPENROUTER_API_KEY=sk-or-...
TELEGRAM_BOT_TOKEN=...

Jangan menyimpan rahasia di variabel lingkungan pengguna kecuali Anda memang ingin setiap proses Windows dapat melihatnya (bukan itu yang Anda inginkan).

Variabel lingkungan khusus Windows
Ini hanya memengaruhi instalasi Windows asli:

Variabel	Memengaruhi
HERMES_GIT_BASH_PATH	Ganti pengaturan penemuan bash.exe. Arahkan ke bash apa pun — Git-for-Windows lengkap, bash WSL melalui symlink, MSYS2, Cygwin. Penginstal akan mengaturnya secara otomatis.
HERMES_DISABLE_WINDOWS_UTF8	Atur ke `true` 1untuk menonaktifkan shim stdio UTF-8 dan kembali ke halaman kode lokal. Berguna untuk melakukan bisecting pada bug pengkodean.
EDITOR/VISUAL	Editor Anda untuk /editdan Ctrl-X Ctrl-E. Hermes secara default menggunakan notepadjika keduanya tidak diatur.
Hapus instalasi
Dari PowerShell:

hermes uninstall

Itulah jalur bersih — menghapus entri schtasks, pintasan folder Startup, hermes.cmdshim, menghapus %LOCALAPPDATA%\hermes\hermes-agent\, dan memangkas PATH Pengguna. Ini membiarkan %USERPROFILE%\.hermes\(konfigurasi, otentikasi, keterampilan, sesi, log Anda) tetap utuh jika Anda melakukan instalasi ulang.

Untuk menghancurkan semuanya dengan bom nuklir:

hermes uninstall
Remove-Item -Recurse -Force "$env:USERPROFILE\.hermes"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\hermes"


Subperintah hermes uninstallCLI juga menangani kasus di mana entri schtasks terdaftar dengan nama tugas yang berbeda (instalasi lama) — subperintah ini mencari berdasarkan jalur instalasi, bukan berdasarkan nama tugas yang dikodekan secara permanen.

Internal manajemen proses
Ini adalah materi latar belakang — lewati saja kecuali Anda sedang melakukan debugging terhadap masalah aneh "komputer itu menghancurkan dirinya sendiri".

Di Linux dan macOS, idiom POSIX os.kill(pid, 0)adalah pemeriksaan izin tanpa operasi: "apakah PID ini aktif dan dapatkah saya memberi sinyal padanya?" Di Windows, os.killpemetaan Python sig=0ke CTRL_C_EVENT— keduanya bertabrakan pada nilai integer 0 — dan mengarahkannya melalui GenerateConsoleCtrlEvent(0, pid), yang menyiarkan Ctrl+C ke seluruh grup proses konsol yang berisi PID target. Itu adalah bpo-14484 , terbuka sejak 2012. Itu tidak akan diperbaiki karena mengubahnya akan merusak skrip yang bergantung pada perilaku saat ini.

Konsekuensi: jalur kode apa pun yang mengatakan "periksa apakah PID ini masih aktif" melalui os.kill(pid, 0)Windows secara diam-diam mematikan target. Hermes memigrasikan setiap situs tersebut (14 di 11 file) ke gateway.status._pid_exists(), yang menggunakan psutil.pid_exists()(yang pada gilirannya menggunakan OpenProcess + GetExitCodeProcessdi Windows — tanpa sinyal). Jika Anda menulis plugin atau patch, gunakan psutil.pid_exists()langsung atau gateway.status._pid_exists()— jangan pernah os.kill(pid, 0).

scripts/check-windows-footguns.pyCI memberlakukan hal ini: setiap os.kill(pid, 0)panggilan baru akan gagal dalam Windows footguns (blocking)pemeriksaan kecuali jika baris tersebut membawa # windows-footgun: ok — <reason>penanda.

Jebakan umum
hermes: command not foundSegera setelah instalasi. Buka jendela PowerShell baru. Penginstal telah ditambahkan %LOCALAPPDATA%\hermes\binke PATH pengguna, tetapi shell yang ada perlu dihidupkan ulang agar dapat menggunakannya. Sementara itu, Anda dapat menjalankan & "$env:LOCALAPPDATA\hermes\bin\hermes.cmd".

WinError 193: %1 is not a valid Win32 applicationSaat menjalankan sebuah alat, Anda menemukan pemanggilan skrip shebang yang melewati .cmdshim. Hermes menyelesaikan perintah melalui shutil.which(cmd, path=local_bin)PATHEXT sehingga PATHEXT dapat mengambil alih .CMD— jika Anda memanggil alat tersebut melalui jalur yang dikodekan secara langsung, beralihlah ke .cmdvarian (misalnya, npx.cmd, bukan npx).

[scriptblock]::Create(...)Gagal dengan The assignment expression is not valid. Unduhan Anda install.ps1mengambil BOM UTF-8. irm | iexFormulir tersebut secara otomatis menghapus BOM; [scriptblock]::Create((irm ...))tidak. Jalankan ulang dengan irm | iexformulir sederhana, atau unduh skrip secara manual dan simpan tanpa BOM melalui [IO.File]::WriteAllText($path, $text, (New-Object Text.UTF8Encoding $false)).

Gateway tidak akan tetap berjalan setelah restart. Periksa hermes gateway status— ini menggabungkan entri schtasks, pintasan folder Startup (jika digunakan), dan PID aktif. Jika schtasks terdaftar tetapi tidak berjalan, kebijakan grup mungkin memblokir ONLOGONpemicu. Jalankan schtasks /Query /TN HermesGateway /V /FO LISTuntuk melihat alasan kegagalan tugas, atau kembali ke jalur folder Startup dengan mencopot pemasangan dan memasang kembali dengan HERMES_GATEWAY_FORCE_STARTUP=1.

/editTetap tidak terjadi apa-apa setelah mengaturnya $env:EDITOR. Anda hanya mengaturnya di proses saat ini; tutup dan buka kembali shell, atau atur di cakupan Pengguna di Properti Sistem → Variabel Lingkungan. Verifikasi dengan echo $env:EDITORdi jendela PowerShell baru.

Alat peramban diluncurkan tetapi alat tersebut mengalami batas waktu. Chromium diinstal secara otomatis pada saat pertama kali dijalankan. Jika instalasi gagal (pembatasan laju GitHub, gangguan CDN Playwright), jalankan perintah ini hermes doctor— perintah ini akan menampilkan Chromium yang hilang dan mencetak npx playwright install chromiumperintah yang tepat untuk memperbaikinya.

agent-browserGagal dengan kesalahan versi Node yang aneh. Installer menyediakan Node 22 di PATH, %LOCALAPPDATA%\hermes\nodetetapi PATH Anda mungkin memiliki Node 18 sistem yang lebih lama terlebih dahulu. Pindahkan direktori node Hermes ke PATH sebelumnya, atau hapus instalasi sistem jika Anda tidak menggunakan Node di tempat lain.

Karakter Cina/Jepang/Arab ditampilkan seperti ?di CLI. Shim stdio UTF-8 tidak aktif. Periksa apakah HERMES_DISABLE_WINDOWS_UTF8TIDAK diatur ( Get-ChildItem env:HERMES_DISABLE_WINDOWS_UTF8). Jika kosong dan Anda masih melihat ?, host konsol (sangat lama cmd.exe) mungkin tidak mendukung UTF-8 sama sekali — beralihlah ke Windows Terminal.

Gateway tidak dapat mengirim foto Telegram — " BadRequest: payload contains invalid characters". Ini tidak terkait dengan Windows tetapi terkadang muncul pertama kali di sana. Biasanya ini berarti jalur file Anda berisi garis miring terbalik yang tidak di-escape dalam badan JSON. Telegram seharusnya menerima jalur yang dinormalisasi oleh Hermes, bukan jalur Windows mentah — jika Anda melihat ini di dalam plugin kustom, pastikan Anda mengirimkan jalur yang disediakan Hermes, bukan str(Path(...))dari input pengguna.

"Berfungsi di mesin saya yang lain" keanehan pengkodean setelah git pull. Jika Anda mengedit konfigurasi Hermes atau skill di Windows menggunakan editor non-UTF-8 (Notepad pada versi Windows yang lebih lama, beberapa IME berbahasa Mandarin), file tersebut mungkin telah disimpan dengan BOM. Hermes mentolerir utf-8-sigsebagian besar pembacaan konfigurasi, tetapi BOM di dalam skalar YAML terlipat ( description: >) secara diam-diam merusak penguraian YAML. Simpan ulang file sebagai UTF-8 biasa tanpa BOM.

Ke mana harus pergi selanjutnya?
Instalasi — halaman instalasi lengkap, termasuk Linux/macOS/WSL2/Termux.
Panduan Windows (WSL2) — jika Anda menginginkan semantik POSIX atau panel terminal dasbor.
Referensi CLI — setiaphermessubperintah.
FAQ — pertanyaan umum yang tidak spesifik untuk Windows.
Gateway Pesan — menjalankan Telegram/Discord/Slack di Windows.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Panduan Windows (WSL2)
Hermes Agent kini mendukung Windows asli dan WSL2. Halaman ini membahas jalur WSL2; untuk instalasi PowerShell asli, lihat Panduan Windows (Asli) khusus .

Kapan sebaiknya memilih WSL2 daripada native:

Anda ingin menggunakan terminal terintegrasi dasbor ( /chattab) — panel tersebut memerlukan POSIX PTY dan hanya tersedia di WSL2.
Anda melakukan pekerjaan pengembangan yang banyak menggunakan POSIX dan ingin sesi Hermes Anda berbagi sistem file/jalur yang sama dengan alat pengembangan Anda.
Anda sudah memiliki lingkungan WSL2 dan tidak ingin memelihara instalasi kedua.
Ketika fitur bawaan sudah memadai (atau lebih baik):

Obrolan interaktif, gateway (Telegram/Discord/dll.), penjadwal cron, alat peramban, server MCP, dan sebagian besar fitur Hermes berjalan secara native di Windows.
Anda tentu tidak ingin memikirkan tentang melintasi batas WSL↔Windows setiap kali Anda merujuk ke sebuah file atau membuka URL.
Di WSL2, pada dasarnya ada dua komputer yang berperan: host Windows Anda, dan VM Linux yang dikelola oleh WSL. Kebingungan paling sering muncul karena tidak yakin Anda sedang menggunakan komputer yang mana pada saat tertentu.

Panduan ini membahas bagian-bagian dari pemisahan tersebut yang secara khusus memengaruhi Hermes: menginstal WSL2, mentransfer file bolak-balik antara Windows dan Linux, jaringan dua arah, dan kendala yang sebenarnya dihadapi orang.

简体中文
Panduan langkah demi langkah dalam bahasa Mandarin mengenai jalur instalasi minimum tersedia di halaman yang sama ini — beralihlah melalui menu bahasa (pojok kanan atas) dan pilih简体中文.

Mengapa WSL2 (dibandingkan dengan Windows asli)?
Instalasi Windows asli berjalan langsung di Windows: terminal Windows Anda (PowerShell, Windows Terminal, dll.), jalur sistem file Windows ( C:\Users\…), dan proses Windows. Hermes menggunakan Git Bash untuk menjalankan perintah shell, yang merupakan cara Claude Code dan agen lainnya menangani Windows saat ini — ini menghindari kesenjangan POSIX-vs-Windows tanpa penulisan ulang penuh.

WSL2 menjalankan kernel Linux asli dalam VM ringan, sehingga Hermes di dalamnya pada dasarnya identik dengan yang berjalan di Ubuntu. Itu sangat berharga ketika Anda menginginkan lingkungan POSIX yang sebenarnya: forksoket /tmpUNIX, semantik sinyal, terminal berbasis PTY, shell seperti bash/ , zshdan alat seperti yang berperilaku seperti di Linux.rggitffmpeg

Konsekuensi praktis dari WSL2:

CLI Hermes, gateway, sesi, memori, keterampilan, dan runtime alat semuanya berada di dalam VM Linux.
Program Windows (browser, aplikasi bawaan, Chrome dengan profil yang Anda masuki) berada di luarnya.
Setiap kali Anda ingin keduanya berkomunikasi — berbagi file, membuka URL, mengontrol Chrome, mengakses server model lokal, mengekspos gateway Hermes ke ponsel Anda — Anda melanggar sebuah batasan. Batasan-batasan itulah yang dibahas dalam panduan ini.
Instal WSL2
Dari PowerShell atau Windows Terminal sebagai administrator:

wsl --install

Pada instalasi Windows 10 22H2+ atau Windows 11 yang baru, ini akan menginstal kernel WSL2, fitur Virtual Machine Platform, dan distribusi Ubuntu default. Restart saat diminta. Setelah restart, Ubuntu akan terbuka dan meminta nama pengguna + kata sandi Linux — ini adalah pengguna Linux baru , tidak terkait dengan akun Windows Anda.

Pastikan Anda benar-benar menggunakan WSL2 (bukan WSL1 versi lama):

wsl --list --verbose

Anda seharusnya melihat VERSION 2. Jika distribusi menampilkan VERSION 1, konversikan:

wsl --set-version Ubuntu 2
wsl --set-default-version 2

Hermes tidak berfungsi dengan andal di WSL1 — WSL1 menerjemahkan syscall Linux secara langsung dan beberapa perilaku (procfs, sinyal, jaringan) berbeda dari Linux sebenarnya.

Pilihan Distro
Ubuntu (LTS) adalah sistem yang kami uji. Debian berfungsi. Arch dan NixOS berfungsi bagi mereka yang menginginkannya, tetapi penginstal satu baris mengasumsikan aptsistem turunan Debian — lihat panduan pengaturan Nix untuk jalur tersebut.

Aktifkan systemd (disarankan)
Gateway Hermes (dan apa pun yang ingin Anda jalankan) lebih mudah dikelola dengan systemd. Pada WSL modern, aktifkan systemd setelah masuk ke distro Anda:

sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true

[interop]
enabled=true
appendWindowsPath=true

[automount]
options = "metadata,umask=22,fmask=11"
EOF


Kemudian dari PowerShell:

wsl --shutdown

Buka kembali terminal WSL Anda. ps -p 1 -o comm=Seharusnya akan menampilkan systemd.

Opsi metadatamount di atas sangat penting — tanpanya, file /mnt/c/...tidak dapat menyimpan bit izin Linux yang sebenarnya, yang menyebabkan masalah chmod +xpada hal-hal seperti skrip di bawah jalur Windows.

Instal Hermes di dalam WSL
Setelah Anda membuka shell WSL2:

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes


Program instalasi memperlakukan WSL2 sebagai Linux biasa — tidak ada hal khusus WSL yang dibutuhkan. Lihat Instalasi untuk tata letak lengkapnya.

Sistem berkas: melintasi batas Windows ↔ WSL2
Inilah bagian yang paling sering membingungkan orang. Terdapat dua sistem file , dan di mana Anda meletakkan file Anda sangat penting — untuk kinerja, kebenaran, dan apa yang dapat dilihat oleh alat-alat terkait.

Kedua arah tersebut
Arah	Jalan di dalam	Jalur yang Anda gunakan
Disk Windows, dilihat dari WSL.	C:\Users\you\Documents	/mnt/c/Users/you/Documents
Disk WSL, dilihat dari Windows	/home/you/code	\\wsl$\Ubuntu\home\you\code(atau \\wsl.localhost\Ubuntu\...pada bangunan yang lebih baru)
Keduanya nyata, keduanya berfungsi, tetapi keduanya bukan sistem file yang sama — keduanya dihubungkan oleh protokol jaringan 9P di balik layar. Hal itu memiliki konsekuensi nyata terhadap kinerja dan semantik.

Di mana menempatkan Hermes dan proyek Anda?
Aturan praktis: simpan semua hal yang berkaitan dengan Linux di dalam sistem file Linux.

Instalasi Hermes Anda ( ~/.hermes/) — Sisi Linux. Penginstal sudah melakukan ini.
Repositori git Anda yang Anda kerjakan dari WSL — sisi Linux ( ~/code/..., ~/projects/...).
Model, dataset, venv Anda — dari sisi Linux.
Apa yang Anda dapatkan dengan mengikuti aturan ini:

I/O cepat. Operasi pada /mnt/c/...9P berjalan melalui 10–100 kali lebih lambat daripada ext4 asli. git statusPada repositori berisi 10.000 file yang terasa instan di , ~/codebisa memakan waktu 15+ detik di /mnt/c.
Izin yang benar. Bit izin Linux adalah emulasi upaya terbaik /mnt/c. Hal-hal seperti sshmenolak kunci dengan "izin yang buruk" atau chmod +xgagal tanpa pemberitahuan adalah hal yang umum.
Pengawas berkas yang andal. inotify di seluruh 9P tidak stabil — pengawas berkas (server pengembangan, pelaksana pengujian) secara rutin melewatkan perubahan pada /mnt/c.
Tidak ada kejutan terkait sensitivitas huruf besar/kecil. Jalur Windows secara default tidak peka terhadap huruf besar/kecil; Linux peka terhadap huruf besar/kecil. Proyek yang menggunakan keduanya Readme.mdberperilaku README.mdberbeda tergantung pada sisi mana Anda berada.
Aktifkan opsi ini /mnt/chanya jika Anda membutuhkan file tersebut untuk berada di sisi Windows — misalnya, Anda ingin membukanya dari aplikasi GUI Windows, atau DevTools MCP Chrome Windows membutuhkan direktori saat ini agar dapat diakses oleh Windows.

Mengirim dan menerima berkas
Dari Windows → ke WSL: cara termudah adalah membuka Explorer dan mengetikkan \\wsl.localhost\Ubuntualamat di bilah alamat. Anda kemudian dapat menyeret dan meletakkan ke \home\<you>\.... Atau dari PowerShell:

wsl cp /mnt/c/Users/you/Downloads/file.pdf ~/incoming/


Dari WSL → ke Windows: salin ke /mnt/c/Users/<you>/...dan akan langsung muncul di Windows Explorer:

cp ~/reports/output.pdf /mnt/c/Users/you/Desktop/


Buka file WSL di aplikasi Windows (editor GUI, browser, dll.): gunakan explorer.exeatau wslview:

sudo apt install wslu     # once — gives you wslview, wslpath, wslopen, etc.
wslview ~/reports/output.pdf    # opens with the Windows default handler
explorer.exe .                  # opens the current WSL dir in Windows Explorer


Konversikan jalur antara kedua alam semesta:

wslpath -w ~/code/project        # → \\wsl.localhost\Ubuntu\home\you\code\project
wslpath -u 'C:\Users\you'        # → /mnt/c/Users/you


Akhiran baris, BOM, dan git
Jika Anda mengedit file di sisi Windows dengan editor Windows, file tersebut mungkin akan memiliki CRLFkarakter akhir baris. Ketika bashPython di sisi Linux membacanya, skrip shell akan mengalami kesalahan bad interpreter: /bin/bash^Mdan Python dapat gagal pada .envfile yang memiliki BOM (Base of Meter).

Solusinya adalah konfigurasi git yang masuk akal di dalam WSL (bukan di Windows):

git config --global core.autocrlf input
git config --global core.eol lf


Untuk file yang sudah memiliki CRLF:

sudo apt install dos2unix
dos2unix path/to/script.sh

"Kloning di dalam WSL atau di /mnt/c?"
Kloning di dalam WSL. Selalu, kecuali Anda memiliki alasan khusus untuk tidak melakukannya. Alur kerja Hermes yang khas ( hermes chatalat yang disebut rg/ ripgreprepositori, pengawas file, gateway latar belakang) akan jauh lebih cepat dan lebih andal dibandingkan ~/code/myrepodengan /mnt/c/Users/you/myrepo.

Satu pengecualian: jembatan MCP yang meluncurkan biner Windows. Jika Anda menggunakannya chrome-devtools-mcpmelalui cmd.exe(lihat panduan MCP: WSL → Windows Chrome ), Windows mungkin akan menampilkan peringatan UNCjika direktori kerja Hermes saat ini adalah ~. Dalam hal ini, jalankan Hermes dari suatu tempat di bawah /mnt/c/sehingga proses Windows memiliki huruf drive cwd.

Jaringan: WSL ↔ Windows
WSL2 berjalan di dalam VM ringan dengan tumpukan jaringan sendiri. Itu berarti localhostkondisi di dalam WSL tidak sama dengan localhost di Windows — keduanya adalah dua host terpisah dari sudut pandang jaringan. Anda perlu memutuskan, untuk setiap layanan, ke arah mana lalu lintas mengalir dan memilih bridge yang tepat.

Dua kasus selalu muncul.

Kasus 1 — Hermes di WSL berkomunikasi dengan layanan di Windows
Yang paling umum: Anda menjalankan Ollama, LM Studio, atau llama-server di Windows , dan Hermes (di dalam WSL) perlu mengaksesnya.

Panduan baku untuk hal ini terdapat dalam panduan penyedia: Jaringan WSL2 untuk Model Lokal →

Versi singkat:

Windows 11 22H2+: aktifkan mode jaringan mirroring ( networkingMode=mirroreddi %USERPROFILE%\.wslconfig, lalu wsl --shutdown). localhostmaka akan berfungsi di kedua arah.
Windows 10 atau versi yang lebih lama: gunakan IP host Windows (gateway default jaringan virtual WSL) dan pastikan server di Windows terikat ke 0.0.0.0, bukan hanya 127.0.0.1. Firewall Windows biasanya juga memerlukan aturan untuk port tersebut.
Untuk tabel lengkap (alamat bind Ollama / LM Studio / vLLM / SGLang, aturan firewall satu baris, helper IP dinamis, solusi firewall Hyper-V), ikuti tautan di atas — jangan menduplikasi tautan tersebut.

Kasus 2 — Sesuatu di Windows (atau LAN Anda) berkomunikasi dengan Hermes di WSL
Ini adalah arah sebaliknya dan kurang terdokumentasi di tempat lain, tetapi inilah yang Anda butuhkan untuk:

Menggunakan dasbor web Hermes dari browser Windows.
Menggunakan server API yang kompatibel dengan OpenAI (yang diekspos oleh hermes gatewaywhen API_SERVER_ENABLED=true) dari alat sisi Windows. Lihat halaman fitur Server API .
Menguji gerbang pesan (Telegram, Discord, dll.) di mana platform tersebut mengirimkan ping ke URL webhook lokal — biasanya Anda akan menggunakan cloudflared/ ngrokdaripada penerusan port mentah.
Subkasus 2a: dari host Windows itu sendiri
Pada Windows 11 22H2+ dengan mode mirroring diaktifkan , tidak ada yang perlu dilakukan. Proses di WSL yang terikat ke 0.0.0.0:8080(atau bahkan 127.0.0.1:8080) dapat diakses dari browser Windows di http://localhost:8080. WSL secara otomatis mempublikasikan ikatan tersebut kembali ke host.

Pada mode NAT (Windows 10 / Windows 11 versi lama), "penerusan localhost" default di WSL2 umumnya akan meneruskan 127.0.0.1bind sisi Linux ke Windows localhost, sehingga layanan Hermes yang dimulai dengan --host 127.0.0.1biasanya dapat dijangkau http://localhost:PORTdari Windows. Jika tidak:

Ikat 0.0.0.0secara eksplisit di dalam WSL.
Temukan alamat IP VM WSL ip -4 addr show eth0 | grep inetdan akses alamat tersebut dari Windows.
Subkasus 2b: dari perangkat lain di LAN Anda (telepon, tablet, PC lain)
Inilah masalah sebenarnya. Alur lalu lintas perangkat LAN → host Windows → VM WSL , dan Anda harus mengatur kedua hop tersebut:

Lakukan pengikatan pada semua antarmuka di dalam WSL. Proses yang mendengarkan pada antarmuka tersebut 127.0.0.1tidak akan pernah dapat dijangkau dari luar VM. Gunakan 0.0.0.0.

Lakukan port forwarding Windows → WSL VM. Dalam mode mirroring, ini otomatis. Dalam mode NAT, Anda harus melakukannya sendiri, per port, di PowerShell Admin:

# Grab the WSL VM's current IP (it changes on every WSL restart under NAT)
$wslIp = (wsl hostname -I).Trim().Split(' ')[0]

# Forward Windows port 8080 → WSL:8080
netsh interface portproxy add v4tov4 `
  listenaddress=0.0.0.0 listenport=8080 `
  connectaddress=$wslIp connectport=8080

# Allow it through Windows Firewall
New-NetFirewallRule -DisplayName "Hermes WSL 8080" `
  -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow


Hapus nanti dengan netsh interface portproxy delete v4tov4 listenaddress=0.0.0.0 listenport=8080.

Arahkan perangkat LAN ke http://<windows-lan-ip>:8080.

Karena IP VM WSL berubah setiap kali dihidupkan ulang dalam mode NAT, aturan sekali pakai hanya berlaku hingga versi berikutnya wsl --shutdown. Untuk sesuatu yang bersifat permanen, gunakan mode mirroring atau masukkan langkah port-proxy ke dalam skrip yang berjalan saat login Windows.

Untuk webhook dari penyedia pesan berbasis cloud (Telegram setWebhook, acara Slack, dll.), jangan melawan penerusan port — gunakan cloudflaredterowongan. Lihat panduan webhook .

Menjalankan layanan Hermes jangka panjang di Windows
Hermes Tool Gateway dan server API adalah proses yang berjalan lama. Di WSL2, Anda memiliki beberapa opsi untuk menjaga agar proses tersebut tetap berjalan.

Di dalam WSL dengan systemd (direkomendasikan)
Jika Anda telah mengaktifkan systemd sesuai bagian pengaturan di atas, hermes gatewaydan server API berfungsi sebagaimana mestinya pada mesin Linux mana pun, gunakan wizard pengaturan gateway:

hermes gateway setup

Ini akan menawarkan untuk menginstal unit pengguna systemd sehingga gateway aktif secara otomatis saat WSL dimulai.

Membuat WSL itu sendiri berjalan saat login Windows.
VM WSL hanya akan tetap aktif selama ada sesuatu yang menggunakannya. Untuk menjaga agar gateway Anda tetap dapat diakses tanpa jendela terminal terbuka, jalankan proses WSL saat masuk ke Windows melalui Penjadwal Tugas:

Pemicu: Saat masuk (pengguna Anda).
Tindakan: Mulai sebuah program
Program:C:\Windows\System32\wsl.exe
Argumen:-d Ubuntu --exec /bin/sh -c "sleep infinity"
Hal itu menjaga agar VM tetap aktif sehingga gateway yang dikelola systemd tetap berjalan. Pada Windows 11, wsl --install --no-launchalur yang lebih baru + auto-start juga berfungsi; sleep infinitykuncinya adalah versi portabel.

Penerusan GPU (model lokal)
WSL2 mendukung GPU NVIDIA secara native sejak kernel WSL 5.10.43+ — instal driver NVIDIA standar di Windows (jangan instal driver NVIDIA Linux di dalam WSL), dan nvidia-smidi dalam WSL akan mengenali GPU. Dari situ, toolkit CUDA, torch, vllm, sglang, dan llama-serverproses build terhadap GPU sebenarnya berjalan seperti biasa.

Dukungan AMD ROCm dan Intel Arc di dalam WSL2 masih terus berkembang dan berada di luar matriks pengujian Hermes — mungkin berfungsi dengan driver saat ini, tetapi kami belum memiliki resep yang dapat direkomendasikan.

Jika Anda menjalankan server model lokal asli Windows (Ollama for Windows, LM Studio) yang sudah menggunakan GPU Anda melalui driver Windows, Anda sama sekali tidak memerlukan passthrough GPU WSL — cukup ikuti Kasus 1 di atas dan akses melalui jaringan dari WSL.

Jebakan umum
"Koneksi ditolak" ke Ollama / LM Studio yang dihosting di Windows saya. Lihat Jaringan WSL2 . Sembilan puluh persen dari waktu server terikat 127.0.0.1dan membutuhkan 0.0.0.0(Ollama: OLLAMA_HOST=0.0.0.0), atau Anda kehilangan aturan firewall.

Terjadi kelambatan yang sangat besar pada git statusrepositori hermes chat. Anda mungkin bekerja di bawah /mnt/c/.... Pindahkan repositori ke ~/code/...(sisi Linux). Jauh lebih cepat.

bad interpreter: /bin/bash^Mpada skrip. Akhiran baris CRLF dari editor Windows. dos2unix script.sh, dan diatur core.autocrlf inputdalam konfigurasi git WSL Anda.

Peringatan "Jalur UNC tidak didukung" dari biner Windows yang diluncurkan melalui MCP. Direktori kerja Hermes saat ini berada di dalam sistem file Linux, dan Windows cmd.exetidak tahu harus berbuat apa dengannya. Jalankan Hermes dari /mnt/c/...direktori tersebut untuk sesi itu, atau gunakan pembungkus yang cdmengarahkan ke jalur yang dapat dijangkau Windows sebelum menjalankan file eksekusi Windows.

Pergeseran waktu setelah tidur/hibernasi. Jam WSL2 dapat tertinggal beberapa menit setelah host kembali dari mode tidur, yang menyebabkan masalah pada semua hal yang berbasis sertifikat (OAuth, API HTTPS). Perbaiki sesuai kebutuhan:

sudo hwclock -s

Atau instal ntpdatedan jalankan saat masuk.

DNS berhenti berfungsi setelah mengaktifkan mode mirroring, atau saat VPN terhubung. Mode mirroring memproksikan pengaturan jaringan host ke WSL — jika DNS Windows bermasalah (VPN split-tunnel, resolver perusahaan), WSL akan mewarisinya. Solusi: timpa resolv.confsecara manual (atur generateResolvConf=falsedi /etc/wsl.conf, lalu tulis sendiri /etc/resolv.confdengan 1.1.1.1atau DNS VPN Anda).

hermesTidak ditemukan setelah menjalankan penginstal. Penginstal menambahkan ~/.local/binke PATH shell Anda melalui ~/.bashrc. Anda perlu source ~/.bashrc(atau membuka terminal baru) agar perubahan tersebut berlaku di sesi saat ini.

Windows Defender lambat pada file WSL. Defender memindai file melalui jembatan 9P saat diakses dari Windows, yang memperbesar kelambatan /mnt/cakses lintas batas. Jika Anda hanya menyentuh file WSL dari dalam WSL, ini tidak masalah. Jika Anda \\wsl$\...sering menggunakan alat Windows untuk memindai file WSL, pertimbangkan untuk mengecualikan jalur distribusi WSL dari pemindaian waktu nyata.

Ruang disk hampir habis. WSL2 menyimpan disk VM-nya sebagai VHDX sparse di bawah %LOCALAPPDATA%\Packages\.... Ukurannya bertambah tetapi tidak menyusut secara otomatis saat Anda menghapus file. Untuk mengklaim kembali ruang: wsl --shutdown, lalu dari PowerShell Admin jalankan Optimize-VHD -Path <path-to-ext4.vhdx> -Mode Full(membutuhkan alat Hyper-V) — atau jalur yang lebih sederhana diskpartyang didokumentasikan pada dokumentasi WSL.

Ke mana harus pergi selanjutnya?
Instalasi — langkah-langkah instalasi sebenarnya (Linux/WSL2/Termux semuanya menggunakan penginstal yang sama).
Integrasi → Penyedia → Jaringan WSL2 — pembahasan mendalam tentang jaringan untuk server model lokal.
Panduan MCP → WSL → Windows Chrome — mengontrol Chrome Windows yang sedang Anda masuki dari Hermes di WSL.
Tool Gateway dan Web Dashboard — layanan jangka panjang yang paling sering ingin Anda ekspos dari WSL ke seluruh jaringan Anda.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Konfigurasi
Semua pengaturan disimpan di ~/.hermes/direktori agar mudah diakses.

Struktur Direktori
~/.hermes/
├── config.yaml     # Settings (model, terminal, TTS, compression, etc.)
├── .env            # API keys and secrets
├── auth.json       # OAuth provider credentials (Nous Portal, etc.)
├── SOUL.md         # Primary agent identity (slot #1 in system prompt)
├── memories/       # Persistent memory (MEMORY.md, USER.md)
├── skills/         # Agent-created skills (managed via skill_manage tool)
├── cron/           # Scheduled jobs
├── sessions/       # Gateway sessions
└── logs/           # Logs (errors.log, gateway.log — secrets auto-redacted)


Mengelola Konfigurasi
hermes config              # View current configuration
hermes config edit         # Open config.yaml in your editor
hermes config set KEY VAL  # Set a specific value
hermes config check        # Check for missing options (after updates)
hermes config migrate      # Interactively add missing options

# Examples:
hermes config set model anthropic/claude-opus-4
hermes config set terminal.backend docker
hermes config set OPENROUTER_API_KEY sk-or-...  # Saves to .env


tip
Perintah ini hermes config setsecara otomatis mengarahkan nilai ke file yang tepat — kunci API disimpan ke .env, sedangkan yang lainnya disimpan ke config.yaml.

Prioritas Konfigurasi
Pengaturan diselesaikan dalam urutan ini (prioritas tertinggi terlebih dahulu):

Argumen CLI — misalnya, hermes chat --model anthropic/claude-sonnet-4(penggantian per-pemanggilan)
~/.hermes/config.yaml— file konfigurasi utama untuk semua pengaturan non-rahasia
~/.hermes/.env— sebagai alternatif untuk variabel lingkungan; diperlukan untuk rahasia (kunci API, token, kata sandi)
Pengaturan default bawaan — pengaturan default aman yang telah ditetapkan secara permanen jika tidak ada pengaturan lain yang dilakukan.
Aturan Praktis
Rahasia (kunci API, token bot, kata sandi) dimasukkan ke dalam .env. Semua hal lainnya (model, backend terminal, pengaturan kompresi, batasan memori, perangkat) dimasukkan ke dalam config.yaml. Jika keduanya diatur, config.yamlmaka akan menang untuk pengaturan non-rahasia.

Substitusi Variabel Lingkungan
Anda dapat merujuk variabel lingkungan dengan config.yamlmenggunakan ${VAR_NAME}sintaks:

auxiliary:
  vision:
    api_key: ${GOOGLE_API_KEY}
    base_url: ${CUSTOM_VISION_URL}

delegation:
  api_key: ${DELEGATION_KEY}

Beberapa referensi dalam satu nilai berfungsi: url: "${HOST}:${PORT}". Jika variabel yang direferensikan tidak diatur, placeholder dipertahankan apa adanya ( ${UNDEFINED_VAR}tetap seperti semula). Hanya ${VAR}sintaks yang didukung — bare $VARtidak diperluas.

Untuk pengaturan penyedia AI (OpenRouter, Anthropic, Copilot, titik akhir khusus, LLM yang dihosting sendiri, model cadangan, dll.), lihat Penyedia AI .

Batas Waktu Penyedia
Anda dapat mengatur providers.<id>.request_timeout_secondsbatas waktu permintaan di seluruh penyedia, serta providers.<id>.models.<model>.timeout_secondspenggantian khusus model. Berlaku untuk klien TURN utama di setiap transport (OpenAI-wire, Anthropic asli, kompatibel dengan Anthropic), rantai cadangan, pembangunan ulang setelah rotasi kredensial, dan (untuk OpenAI-wire) argumen kata kunci batas waktu per permintaan — sehingga nilai yang dikonfigurasi akan menggantikan HERMES_API_TIMEOUTvariabel lingkungan lama.

Anda juga dapat mengatur providers.<id>.stale_timeout_secondsdetektor panggilan usang non-streaming, serta providers.<id>.models.<model>.stale_timeout_secondspenggantian khusus model. Ini lebih unggul daripada HERMES_API_CALL_STALE_TIMEOUTvariabel lingkungan lama.

Jika dibiarkan tidak diatur, pengaturan default lama ( HERMES_API_TIMEOUT=1800s, HERMES_API_CALL_STALE_TIMEOUT=300s, Anthropic 900 asli) akan tetap berlaku. Saat ini belum terhubung untuk AWS Bedrock (baik bedrock_conversejalur SDK AnthropicBedrock maupun boto3 dengan konfigurasi batas waktu sendiri). Lihat contoh yang dikomentari di cli-config.yaml.example.

Konfigurasi Backend Terminal
Hermes mendukung tujuh backend terminal. Masing-masing menentukan di mana perintah shell agen benar-benar dieksekusi — mesin lokal Anda, kontainer Docker, server jarak jauh melalui SSH, sandbox cloud Modal (langsung atau melalui gateway yang dikelola Nous), ruang kerja Daytona, Sandbox Vercel, atau kontainer Singularity/Apptainer.

terminal:
  backend: local    # local | docker | ssh | modal | daytona | vercel_sandbox | singularity
  cwd: "."          # Gateway/cron working directory (CLI always uses launch dir)
  timeout: 180      # Per-command timeout in seconds
  env_passthrough: []  # Env var names to forward to sandboxed execution (terminal + execute_code)
  singularity_image: "docker://nikolaik/python-nodejs:python3.11-nodejs20"  # Container image for Singularity backend
  modal_image: "nikolaik/python-nodejs:python3.11-nodejs20"                 # Container image for Modal backend
  daytona_image: "nikolaik/python-nodejs:python3.11-nodejs20"               # Container image for Daytona backend


Untuk sandbox berbasis cloud seperti Modal, Daytona, dan Vercel Sandbox, container_persistent: trueini berarti Hermes akan mencoba mempertahankan status sistem file saat sandbox dibuat ulang. Namun, ini tidak menjamin bahwa sandbox aktif, ruang PID, atau proses latar belakang yang sama akan tetap berjalan di kemudian hari.

Gambaran Umum Backend
Backend	Di mana perintah dijalankan	Isolasi	Terbaik untuk
lokal	Mesin Anda secara langsung	Tidak ada	Pengembangan, penggunaan pribadi
buruh pelabuhan	Kontainer Docker tunggal yang persisten (dibagikan di seluruh sesi, /new, subagen)	Lengkap (namespace, penghapusan huruf kapital)	Pengujian keamanan berbasis sandbox, CI/CD
ssh	Server jarak jauh melalui SSH	Batas jaringan	Pengembangan jarak jauh, perangkat keras yang canggih
modal	Kotak pasir awan modal	Penuh (VM cloud)	Komputasi awan sementara, evaluasi
Daytona	Ruang kerja Daytona	Penuh (kontainer cloud)	Lingkungan pengembangan cloud terkelola
kotak pasir vercel	Kotak Pasir Vercel	Penuh (cloud microVM)	Eksekusi cloud dengan persistensi sistem file berbasis snapshot.
keganjilan	Kontainer Singularity/Apptainer	Ruang nama (--containall)	Klaster HPC, mesin bersama
Backend Lokal
Pengaturan default. Perintah dijalankan langsung di mesin Anda tanpa isolasi. Tidak diperlukan pengaturan khusus.

terminal:
  backend: local

peringatan
Agen memiliki akses sistem file yang sama dengan akun pengguna Anda. Gunakan ini hermes toolsuntuk menonaktifkan alat yang tidak Anda inginkan, atau beralih ke Docker untuk sandboxing.

Backend Docker
Menjalankan perintah di dalam kontainer Docker dengan pengamanan yang diperkuat (semua kemampuan dinonaktifkan, tidak ada peningkatan hak akses, batasan PID).

Satu kontainer persisten, bukan per perintah. Hermes memulai SATU kontainer berumur panjang pada penggunaan pertama dan mengarahkan setiap terminal, file, dan execute_codepanggilan ke docker execdalam kontainer yang sama — di seluruh sesi, /newdan /resetsubagen delegate_task— selama masa hidup proses Hermes. Perubahan direktori kerja, paket yang diinstal, dan file di dalamnya /workspaceakan terbawa dari satu panggilan alat ke panggilan berikutnya, seperti halnya shell lokal. Kontainer dihentikan dan dihapus saat dimatikan. Lihat Siklus hidup Kontainer di bawah untuk detailnya.

terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  docker_mount_cwd_to_workspace: false  # Mount launch dir into /workspace
  docker_run_as_host_user: false   # See "Running container as host user" below
  docker_forward_env:              # Env vars to forward into container
    - "GITHUB_TOKEN"
  docker_volumes:                  # Host directory mounts
    - "/home/user/projects:/workspace/projects"
    - "/home/user/data:/data:ro"   # :ro for read-only
  docker_extra_args:               # Extra flags appended verbatim to `docker run`
    - "--gpus=all"
    - "--network=host"

  # Resource limits
  container_cpu: 1                 # CPU cores (0 = unlimited)
  container_memory: 5120           # MB (0 = unlimited)
  container_disk: 51200            # MB (requires overlay2 on XFS+pquota)
  container_persistent: true       # Persist /workspace and /root across sessions


terminal.docker_extra_args(juga dapat ditimpa melalui TERMINAL_DOCKER_EXTRA_ARGS='["--gpus=all"]') memungkinkan Anda untuk meneruskan docker runflag sembarang yang tidak ditampilkan Hermes sebagai kunci kelas satu — --gpus, --network, --add-host, penggantian alternatif --security-opt, dll. Setiap entri harus berupa string; daftar ditambahkan terakhir ke docker runpemanggilan yang dirakit sehingga dapat menimpa default Hermes jika diperlukan. Gunakan dengan hemat — flag yang bertentangan dengan pengerasan sandbox (penurunan kemampuan, --user, pemasangan bind workspace) akan secara diam-diam melemahkan isolasi.

Persyaratan: Docker Desktop atau Docker Engine terpasang dan berjalan. Probe Hermes $PATHplus lokasi instalasi macOS umum ( /usr/local/bin/docker, /opt/homebrew/bin/docker, paket aplikasi Docker Desktop). Podman didukung secara langsung: atur HERMES_DOCKER_BINARY=podman(atau jalur lengkapnya) untuk memaksanya jika keduanya terpasang.

Siklus hidup kontainer: Hermes menggunakan kembali satu kontainer berumur panjang ( docker run -d ... sleep 2h) untuk setiap panggilan terminal dan alat file, di seluruh sesi, /new, /reset, dan delegate_tasksubagen, selama masa hidup proses Hermes. Perintah dijalankan melalui docker execdengan shell login, sehingga perubahan direktori kerja, paket yang diinstal, dan file di /workspacesemuanya tetap ada dari satu panggilan alat ke panggilan berikutnya. Kontainer dihentikan dan dihapus saat Hermes dimatikan (atau ketika pembersihan idle mengambilnya kembali).

Subagen paralel yang dibuat melalui delegate_task(tasks=[...])berbagi satu kontainer ini — cdperubahan lingkungan dan penulisan bersamaan ke jalur yang sama akan bertabrakan. Jika subagen membutuhkan sandbox terisolasi, ia harus mendaftarkan penggantian citra per tugas melalui register_task_env_overrides(), yang secara otomatis dilakukan oleh lingkungan RL dan benchmark (TerminalBench2, HermesSweEnv, dll.) untuk citra Docker per tugas mereka.

Penguatan keamanan:

--cap-drop ALLdengan hanya DAC_OVERRIDE, CHOWN, FOWNERditambahkan kembali
--security-opt no-new-privileges
--pids-limit 256
tmpfs dengan batasan ukuran untuk /tmp(512MB), /var/tmp(256MB), /run(64MB)
Penerusan kredensial: Variabel lingkungan yang tercantum docker_forward_envdi-resolusi dari lingkungan shell Anda terlebih dahulu, kemudian ~/.hermes/.env. Skill juga dapat mendeklarasikan required_environment_variablesmana yang digabungkan secara otomatis.

Backend SSH
Menjalankan perintah pada server jarak jauh melalui SSH. Menggunakan ControlMaster untuk penggunaan kembali koneksi (keepalive idle 5 menit). Shell persisten diaktifkan secara default — status (cwd, variabel lingkungan) tetap ada di antara perintah yang dijalankan.

terminal:
  backend: ssh
  persistent_shell: true           # Keep a long-lived bash session (default: true)


Variabel lingkungan yang dibutuhkan:

TERMINAL_SSH_HOST=my-server.example.com
TERMINAL_SSH_USER=ubuntu


Opsional:

Variabel	Bawaan	Keterangan
TERMINAL_SSH_PORT	22	Port SSH
TERMINAL_SSH_KEY	(standar sistem)	Jalur menuju kunci privat SSH
TERMINAL_SSH_PERSISTENT	true	Aktifkan shell persisten
Cara kerjanya: Terhubung pada saat inisialisasi dengan BatchMode=yesdan StrictHostKeyChecking=accept-new. Shell persisten menjaga satu bash -lproses tetap aktif di host jarak jauh, berkomunikasi melalui file sementara. Perintah yang membutuhkan stdin_dataatau sudosecara otomatis beralih ke mode sekali jalan.

Backend Modal
Menjalankan perintah dalam lingkungan sandbox cloud Modal . Setiap tugas mendapatkan VM terisolasi dengan CPU, memori, dan disk yang dapat dikonfigurasi. Sistem file dapat di-snapshot/dipulihkan di seluruh sesi.

terminal:
  backend: modal
  container_cpu: 1                 # CPU cores
  container_memory: 5120           # MB (5GB)
  container_disk: 51200            # MB (50GB)
  container_persistent: true       # Snapshot/restore filesystem


Diperlukan: Variabel lingkungan MODAL_TOKEN_ID+ MODAL_TOKEN_SECRETatau ~/.modal.tomlfile konfigurasi.

Persistensi: Saat diaktifkan, sistem file sandbox akan diambil snapshot-nya saat pembersihan dan dipulihkan pada sesi berikutnya. Snapshot dilacak di ~/.hermes/modal_snapshots.json. Ini mempertahankan status sistem file, bukan proses yang sedang berjalan, ruang PID, atau pekerjaan latar belakang.

Berkas kredensial: Dipasang secara otomatis dari ~/.hermes/(token OAuth, dll.) dan disinkronkan sebelum setiap perintah.

Backend Daytona
Menjalankan perintah di ruang kerja yang dikelola Daytona . Mendukung penghentian/pengaktifan kembali untuk penyimpanan permanen.

terminal:
  backend: daytona
  container_cpu: 1                 # CPU cores
  container_memory: 5120           # MB → converted to GiB
  container_disk: 10240            # MB → converted to GiB (max 10 GiB)
  container_persistent: true       # Stop/resume instead of delete


Diperlukan: DAYTONA_API_KEY variabel lingkungan.

Keberlangsungan: Saat diaktifkan, sandbox dihentikan (bukan dihapus) saat pembersihan dan dilanjutkan pada sesi berikutnya. Nama sandbox mengikuti pola hermes-{task_id}.

Batas disk: Daytona memberlakukan batas maksimum 10 GiB. Permintaan di atas batas ini akan dibatasi dengan peringatan.

Vercel Sandbox Backend
Menjalankan perintah di dalam microVM cloud Vercel Sandbox . Hermes menggunakan antarmuka terminal dan alat file standar; tidak ada alat khusus Vercel yang berinteraksi langsung dengan model.

terminal:
  backend: vercel_sandbox
  vercel_runtime: node24          # node24 | node22 | python3.13
  cwd: /vercel/sandbox            # default workspace root
  container_persistent: true      # Snapshot/restore filesystem
  container_disk: 51200           # Shared default only; custom disk is unsupported


Instalasi yang diperlukan: Instal SDK tambahan opsional:

pip install 'hermes-agent[vercel]'

Autentikasi yang diperlukan: Konfigurasikan autentikasi token akses dengan ketiga parameter VERCEL_TOKEN, VERCEL_PROJECT_ID, dan VERCEL_TEAM_ID. Ini adalah pengaturan yang didukung untuk penerapan dan proses Hermes jangka panjang normal pada Render, Railway, Docker, dan host serupa.

Untuk pengembangan lokal sekali pakai, Hermes juga menerima token Vercel OIDC berumur pendek:

VERCEL_OIDC_TOKEN="$(vc project token <project-name>)" hermes chat


Dari direktori proyek Vercel yang tertaut, Anda dapat menghilangkan nama proyek:

VERCEL_OIDC_TOKEN="$(vc project token)" hermes chat


Token OIDC berumur pendek dan tidak boleh digunakan sebagai jalur penyebaran yang didokumentasikan.

Runtime: terminal.vercel_runtime mendukung node24, node22, dan python3.13. Jika tidak diatur, Hermes akan menggunakan nilai default node24.

Persistensi: Saat container_persistent: trueHermes mengambil snapshot sistem file sandbox selama pembersihan dan memulihkan sandbox berikutnya untuk tugas yang sama dari snapshot tersebut. Isi snapshot dapat mencakup kredensial, keterampilan, dan file cache yang disinkronkan Hermes yang disalin ke dalam sandbox. Ini hanya mempertahankan status sistem file; ini tidak mempertahankan identitas sandbox aktif, ruang PID, status shell, atau proses latar belakang yang sedang berjalan.

Perintah latar belakang: terminal(background=true) menggunakan alur proses latar belakang non-lokal generik Hermes. Anda dapat membuat, memantau, menunggu, melihat log, dan menghentikan proses melalui alat proses normal saat sandbox aktif. Hermes tidak menyediakan pemulihan proses terpisah Vercel asli setelah pembersihan atau memulai ulang.

Pengaturan ukuran disk: Vercel Sandbox saat ini tidak mendukung container_diskpengaturan sumber daya Hermes. Biarkan container_disktidak diatur atau pada nilai default bersama 51200; nilai non-default akan menyebabkan kegagalan diagnostik dan pembuatan backend, alih-alih diabaikan secara diam-diam.

Backend Singularity/Apptainer
Menjalankan perintah di dalam kontainer Singularity/Apptainer . Dirancang untuk klaster HPC dan mesin bersama di mana Docker tidak tersedia.

terminal:
  backend: singularity
  singularity_image: "docker://nikolaik/python-nodejs:python3.11-nodejs20"
  container_cpu: 1                 # CPU cores
  container_memory: 5120           # MB
  container_persistent: true       # Writable overlay persists across sessions


Persyaratan: apptainer atau singularitybiner di $PATH.

Penanganan gambar: URL Docker ( docker://...) secara otomatis dikonversi ke file SIF dan disimpan dalam cache. .sifFile yang sudah ada digunakan secara langsung.

Direktori sementara: Diselesaikan secara berurutan: TERMINAL_SCRATCH_DIR→ TERMINAL_SANDBOX_DIR/singularity→ /scratch/$USER/hermes-agent(Konvensi HPC) → ~/.hermes/sandboxes/singularity.

Isolasi: Digunakan --containall --no-homeuntuk isolasi namespace penuh tanpa memasang direktori home host.

Masalah Umum pada Backend Terminal
Jika perintah terminal langsung gagal atau alat terminal dilaporkan dinonaktifkan:

Lokal — Tidak ada persyaratan khusus. Pengaturan default teraman saat memulai.
Docker — Jalankan docker versionuntuk memverifikasi apakah Docker berfungsi. Jika gagal, perbaiki Docker atau hermes config set terminal.backend local.
SSH — Keduanya TERMINAL_SSH_HOSTharus TERMINAL_SSH_USERdiatur. Hermes akan mencatat kesalahan yang jelas jika salah satunya hilang.
Modal — Membutuhkan MODAL_TOKEN_IDvariabel lingkungan atau ~/.modal.toml. Jalankan hermes doctoruntuk memeriksa.
Daytona — Kebutuhan DAYTONA_API_KEY. SDK Daytona menangani konfigurasi URL server.
Singularitas — Membutuhkan apptaineratau singularitydi dalam $PATH. Umum terjadi pada klaster HPC.
Jika ragu, terminal.backendkembali ke pengaturan awal localdan pastikan perintah dijalankan di sana terlebih dahulu.

Sinkronisasi File Jarak Jauh ke Host saat Pemutusan Koneksi
Untuk backend SSH , Modal , dan Daytona (di mana pun working tree agen berada di mesin yang berbeda dari host yang menjalankan Hermes), Hermes melacak file yang disentuh agen di dalam sandbox jarak jauh dan, pada saat pemutusan sesi/pembersihan sandbox, menyinkronkan file yang dimodifikasi kembali ke host di bawah ~/.hermes/cache/remote-syncs/<session-id>/.

Dipicu pada: penutupan sesi, /new, /reset, batas waktu pesan gateway, delegate_taskpenyelesaian subagen ketika anak menggunakan backend jarak jauh.
Mencakup seluruh struktur direktori yang dimodifikasi oleh agen, bukan hanya file yang secara eksplisit dibuka. Penambahan, pengeditan, dan penghapusan semuanya tercatat.
Lingkungan pengujian jarak jauh mungkin telah dihapus pada saat Anda mencarinya; ~/.hermes/cache/remote-syncs/…salinan lokal adalah catatan resmi tentang apa yang diubah oleh agen tersebut.
Output biner berukuran besar (checkpoint model, dataset mentah) dibatasi ukurannya — sinkronisasi akan melewati beberapa file file_sync_max_mb(default 100). Tingkatkan nilai tersebut jika Anda mengharapkan artefak yang lebih besar untuk dikembalikan.
terminal:
  file_sync_max_mb: 100     # default — sync files up to 100 MB each
  file_sync_enabled: true   # default — set false to skip the sync entirely


Inilah cara Anda memulihkan hasil dari sandbox cloud sementara yang dihancurkan setelah sesi berakhir, tanpa harus memberi tahu agen secara eksplisit scpatau modal volume putsetiap artefak.

Pemasangan Volume Docker
Saat menggunakan backend Docker, docker_volumesAnda dapat berbagi direktori host dengan kontainer. Setiap entri menggunakan -vsintaks Docker standar: host_path:container_path[:options].

terminal:
  backend: docker
  docker_volumes:
    - "/home/user/projects:/workspace/projects"   # Read-write (default)
    - "/home/user/datasets:/data:ro"              # Read-only
    - "/home/user/.hermes/cache/documents:/output" # Gateway-visible exports


Ini berguna untuk:

Menyediakan file ke agen (dataset, konfigurasi, kode referensi)
Menerima file dari agen (kode yang dihasilkan, laporan, ekspor)
Ruang kerja bersama tempat Anda dan agen mengakses file yang sama.
Jika Anda menggunakan gateway pesan dan ingin agen mengirimkan file yang dihasilkan melalui MEDIA:/..., sebaiknya gunakan mount ekspor yang terlihat oleh host seperti /home/user/.hermes/cache/documents:/output.

Tulis file di dalam Docker ke/output/...
Keluarkan jalur host di MEDIA:, misalnya: MEDIA:/home/user/.hermes/cache/documents/report.txt
Jangan memancarkan atau kecuali jalur persis tersebut juga ada untuk proses gateway pada host ./workspace/.../output/...
peringatan
Kunci duplikat YAML secara diam-diam menimpa kunci sebelumnya. Jika Anda sudah memiliki docker_volumes:blok, gabungkan mount baru ke dalam daftar yang sama alih-alih menambahkan docker_volumes:kunci lain di kemudian hari dalam file tersebut.

Dapat juga diatur melalui variabel lingkungan: TERMINAL_DOCKER_VOLUMES='["/host:/container"]'(array JSON).

Penerusan Kredensial Docker
Secara default, sesi terminal Docker tidak mewarisi kredensial host sembarangan. Jika Anda memerlukan token khusus di dalam kontainer, tambahkan ke terminal.docker_forward_env.

terminal:
  backend: docker
  docker_forward_env:
    - "GITHUB_TOKEN"
    - "NPM_TOKEN"

Hermes pertama-tama menyelesaikan setiap variabel yang terdaftar dari shell Anda saat ini, kemudian beralih ke ~/.hermes/.envvariabel yang disimpan dengan hermes config set.

peringatan
Apa pun yang tercantum di dalamnya docker_forward_envakan terlihat oleh perintah yang dijalankan di dalam kontainer. Hanya teruskan kredensial yang Anda rasa nyaman untuk ditampilkan ke sesi terminal.

Menjalankan Kontainer sebagai Pengguna Host Anda
Secara default, kontainer Docker berjalan sebagai root(UID 0). File yang dibuat di dalam /workspaceatau bind-mount lainnya akhirnya dimiliki oleh root di host, jadi setelah sesi berakhir, Anda harus sudo chownmenghapusnya terlebih dahulu sebelum dapat mengeditnya dari editor host Anda. terminal.docker_run_as_host_userFlag ini memperbaiki masalah tersebut:

terminal:
  backend: docker
  docker_run_as_host_user: true   # default: false


Saat diaktifkan, Hermes menambahkan --user $(id -u):$(id -g)perintah docker runsehingga file yang ditulis ke direktori yang dipasang (bind-mounted) ( /workspace, /root, apa pun di docker_volumes) dimiliki oleh pengguna host Anda, bukan root. Konsekuensinya: kontainer tidak lagi dapat apt installmenulis ke jalur yang dimiliki root seperti /root/.npm— gunakan citra dasar yang HOMEdimiliki oleh pengguna non-root (atau tambahkan alat yang Anda perlukan pada saat pembuatan citra) jika Anda membutuhkan keduanya.

Biarkan ini false(pengaturan default) untuk perilaku yang kompatibel dengan versi sebelumnya. Aktifkan ini jika alur kerja Anda sebagian besar adalah "mengedit file host yang terpasang" dan Anda bosan dengan sudo chown -R.

Opsional: Pasang Direktori Peluncuran ke dalam/workspace
Secara default, sandbox Docker tetap terisolasi. Hermes tidak meneruskan direktori kerja host Anda saat ini ke dalam kontainer kecuali Anda secara eksplisit memilih untuk melakukannya.

Aktifkan di config.yaml:

terminal:
  backend: docker
  docker_mount_cwd_to_workspace: true


Saat diaktifkan:

Jika Anda menjalankan Hermes dari ~/projects/my-app, direktori host tersebut akan dipasang (bind-mounted) ke/workspace
Backend Docker dimulai di/workspace
Baik alat file maupun perintah terminal sama-sama melihat proyek yang terpasang yang sama.
Saat dinonaktifkan, /workspacetetap dimiliki oleh sandbox kecuali Anda secara eksplisit memasang sesuatu melalui docker_volumes.

Kompromi keamanan:

falsemempertahankan batas kotak pasir
truememberikan akses langsung ke direktori tempat Anda menjalankan Hermes kepada sandbox.
Gunakan opsi ikut serta hanya jika Anda memang ingin kontainer tersebut berfungsi pada file host yang sedang berjalan.

Cangkang Permanen
Secara default, setiap perintah terminal berjalan dalam subprosesnya sendiri — direktori kerja, variabel lingkungan, dan variabel shell diatur ulang di antara perintah. Ketika shell persisten diaktifkan, satu proses bash yang berumur panjang tetap aktif di antara execute()panggilan sehingga status tetap terjaga di antara perintah.

This is most useful for the SSH backend, where it also eliminates per-command connection overhead. Persistent shell is enabled by default for SSH and disabled for the local backend.

terminal:
  persistent_shell: true   # default — enables persistent shell for SSH


To disable:

hermes config set terminal.persistent_shell false


What persists across commands:

Working directory (cd /tmp sticks for the next command)
Exported environment variables (export FOO=bar)
Shell variables (MY_VAR=hello)
Precedence:

Level	Variable	Default
Config	terminal.persistent_shell	true
SSH override	TERMINAL_SSH_PERSISTENT	follows config
Local override	TERMINAL_LOCAL_PERSISTENT	false
Per-backend environment variables take highest precedence. If you want persistent shell on the local backend too:

export TERMINAL_LOCAL_PERSISTENT=true


note
Commands that require stdin_data or sudo automatically fall back to one-shot mode, since the persistent shell's stdin is already occupied by the IPC protocol.

See Code Execution and the Terminal section of the README for details on each backend.

Skill Settings
Skills can declare their own configuration settings via their SKILL.md frontmatter. These are non-secret values (paths, preferences, domain settings) stored under the skills.config namespace in config.yaml.

skills:
  config:
    myplugin:
      path: ~/myplugin-data   # Example — each skill defines its own keys


How skill settings work:

hermes config migrate scans all enabled skills, finds unconfigured settings, and offers to prompt you
hermes config show displays all skill settings under "Skill Settings" with the skill they belong to
When a skill loads, its resolved config values are injected into the skill context automatically
Setting values manually:

hermes config set skills.config.myplugin.path ~/myplugin-data


For details on declaring config settings in your own skills, see Creating Skills — Config Settings.

Guard on agent-created skill writes
When the agent uses skill_manage to create, edit, patch, or delete a skill, Hermes can optionally scan the new/updated content for dangerous keyword patterns (credential harvesting, obvious prompt injection, exfil instructions). The scanner is off by default — real agent workflows that legitimately touch ~/.ssh/ or mention $OPENAI_API_KEY were tripping the heuristic too often. Turn it back on if you want the scanner to prompt you before the agent's skill writes land:

skills:
  guard_agent_created: true   # default: false


When on, any flagged skill_manage write surfaces as an approval prompt with the scanner's rationale. Accepted writes land; denied writes return an explanatory error to the agent.

Memory Configuration
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200   # ~800 tokens
  user_char_limit: 1375     # ~500 tokens


File Read Safety
Controls how much content a single read_file call can return. Reads that exceed the limit are rejected with an error telling the agent to use offset and limit for a smaller range. This prevents a single read of a minified JS bundle or large data file from flooding the context window.

file_read_max_chars: 100000  # default — ~25-35K tokens


Raise it if you're on a model with a large context window and frequently read big files. Lower it for small-context models to keep reads efficient:

# Large context model (200K+)
file_read_max_chars: 200000

# Small local model (16K context)
file_read_max_chars: 30000

Agen ini juga secara otomatis melakukan deduplikasi pembacaan file — jika wilayah file yang sama dibaca dua kali dan file tersebut tidak berubah, maka akan dikembalikan cuplikan ringan alih-alih mengirim ulang konten. Ini akan diatur ulang saat kompresi konteks sehingga agen dapat membaca ulang file setelah kontennya diringkas.

Batas Pemotongan Keluaran Alat
Tiga batasan terkait mengontrol seberapa banyak output mentah yang dapat dikembalikan oleh suatu alat sebelum Hermes memotongnya:

tool_output:
  max_bytes: 50000        # terminal output cap (chars)
  max_lines: 2000         # read_file pagination cap
  max_line_length: 2000   # per-line cap in read_file's line-numbered view


max_bytes— Ketika sebuah terminalperintah menghasilkan lebih dari jumlah karakter ini untuk gabungan stdout/stderr, Hermes menyimpan 40% pertama dan 60% terakhir, lalu menyisipkan [OUTPUT TRUNCATED]pemberitahuan di antara keduanya. Default 50000(≈12-15 ribu token di seluruh tokeniser umum).
max_lines— Batas atas limitparameter untuk satu read_filepanggilan. Permintaan di atas batas ini akan dibatasi sehingga satu kali pembacaan tidak dapat membanjiri jendela konteks. Default 2000.
max_line_length— Batasan per baris diterapkan saat read_filemenampilkan tampilan bernomor baris. Baris yang lebih panjang dari ini akan dipotong menjadi sejumlah karakter ini diikuti dengan ... [truncated]. Default 2000.
Tingkatkan batasan pada model dengan jendela konteks besar yang mampu menghasilkan lebih banyak output mentah per panggilan. Turunkan batasan tersebut untuk model konteks kecil agar hasil alat tetap ringkas:

# Large context model (200K+)
tool_output:
  max_bytes: 150000
  max_lines: 5000

# Small local model (16K context)
tool_output:
  max_bytes: 20000
  max_lines: 500

Penonaktifan Perangkat Alat Global
Untuk menyembunyikan toolset tertentu di seluruh CLI dan setiap platform gateway di satu tempat, cantumkan namanya di bawah ini agent.disabled_toolsets:

agent:
  disabled_toolsets:
    - memory       # hide memory tools + MEMORY_GUIDANCE injection
    - web          # no web_search / web_extract anywhere


Ini berlaku setelah konfigurasi alat per platform ( platform_toolsetsditulis oleh hermes tools), sehingga kumpulan alat yang tercantum di sini selalu dihapus — bahkan jika konfigurasi tersimpan platform masih mencantumkannya. Gunakan ini ketika Anda menginginkan satu saklar untuk "matikan X di mana saja" daripada mengedit 15+ baris platform di hermes toolsUI.

Membiarkan daftar kosong, atau menghilangkan kunci, tidak akan berpengaruh.

Isolasi Worktree Git
Aktifkan worktree git terisolasi untuk menjalankan beberapa agen secara paralel pada repositori yang sama:

worktree: true    # Always create a worktree (same as hermes -w)
# worktree: false # Default — only when -w flag is passed


Saat diaktifkan, setiap sesi CLI membuat worktree baru .worktrees/dengan cabangnya sendiri. Agen dapat mengedit file, melakukan commit, push, dan membuat PR tanpa saling mengganggu. Worktree yang bersih akan dihapus saat keluar; worktree yang kotor akan disimpan untuk pemulihan manual.

Anda juga dapat mencantumkan file yang diabaikan oleh Git untuk disalin ke dalam worktree melalui perintah .worktreeincludedi root repositori Anda:

# .worktreeinclude
.env
.venv/
node_modules/

Kompresi Konteks
Hermes secara otomatis mengompres percakapan panjang agar tetap berada dalam jendela konteks model Anda. Ringkasan kompresi adalah panggilan LLM terpisah — Anda dapat mengarahkannya ke penyedia atau titik akhir mana pun.

Semua pengaturan kompresi berada di config.yaml(tidak ada variabel lingkungan).

Referensi lengkap
compression:
  enabled: true                                     # Toggle compression on/off
  threshold: 0.50                                   # Compress at this % of context limit
  target_ratio: 0.20                                # Fraction of threshold to preserve as recent tail
  protect_last_n: 20                                # Min recent messages to keep uncompressed
  hygiene_hard_message_limit: 400                   # Gateway safety valve — see below

# The summarization model/provider is configured under auxiliary:
auxiliary:
  compression:
    model: ""                                       # Empty = use main chat model. Override with e.g. "google/gemini-3-flash-preview" for cheaper/faster compression.
    provider: "auto"                                # Provider: "auto", "openrouter", "nous", "codex", "main", etc.
    base_url: null                                  # Custom OpenAI-compatible endpoint (overrides provider)


Migrasi konfigurasi lama
Konfigurasi lama dengan compression.summary_model, compression.summary_provider, dan compression.summary_base_urlsecara otomatis dimigrasikan ke auxiliary.compression.*saat pemuatan pertama (versi konfigurasi 17). Tidak diperlukan tindakan manual.

hygiene_hard_message_limitadalah katup pengaman pra-kompresi khusus gateway . Sesi yang berjalan tak terkendali dengan ribuan pesan dapat mencapai batas konteks model sebelum ambang batas persentase konteks normal tercapai; ketika jumlah pesan melampaui batas ini, Hermes memaksa kompresi terlepas dari penggunaan token. Default 400— naikkan nilainya untuk platform di mana sesi yang sangat panjang adalah hal yang normal, turunkan nilainya untuk memaksa kompresi yang lebih agresif. Mengedit nilai ini pada gateway yang sedang berjalan akan berlaku pada pesan berikutnya (lihat di bawah).

Pengaktifan ulang kompresi dan panjang konteks melalui gateway.
Pada rilis terbaru, pengeditan model.context_lengthatau compression.*perubahan kunci apa pun config.yamlpada gateway yang sedang berjalan akan berlaku pada pesan berikutnya — tidak perlu memulai ulang gateway, tidak /resetperlu melakukan rotasi sesi. Tanda tangan agen yang di-cache mencakup kunci-kunci ini, sehingga gateway secara transparan membangun ulang agen ketika melihat perubahan. Kunci API dan konfigurasi alat/keterampilan masih memerlukan jalur pemuatan ulang seperti biasa.

Pengaturan umum
Default (deteksi otomatis) — tidak perlu konfigurasi:

compression:
  enabled: true
  threshold: 0.50

Menggunakan penyedia utama dan model utama Anda. Ganti pengaturan per tugas (misalnya auxiliary.compression.provider: openrouter+ model: google/gemini-2.5-flash) jika Anda menginginkan kompresi pada model yang lebih murah daripada model obrolan utama Anda.

Paksa penggunaan penyedia tertentu (berbasis OAuth atau kunci API):

auxiliary:
  compression:
    provider: nous
    model: gemini-3-flash

Berfungsi dengan penyedia mana pun: nous, openrouter, codex, anthropic, main, dll.

Endpoint kustom (hosting sendiri, Ollama, zai, DeepSeek, dll.):

auxiliary:
  compression:
    model: glm-4.7
    base_url: https://api.z.ai/api/coding/paas/v4


Mengarah ke titik akhir khusus yang kompatibel dengan OpenAI. Digunakan OPENAI_API_KEYuntuk otentikasi.

Bagaimana ketiga kenop tersebut berinteraksi
auxiliary.compression.provider	auxiliary.compression.base_url	Hasil
auto(bawaan)	tidak diatur	Mendeteksi penyedia terbaik yang tersedia secara otomatis
nous/ openrouter/ dll.	tidak diatur	Paksa penyedia tersebut, gunakan otorisasi mereka.
setiap	mengatur	Gunakan endpoint kustom secara langsung (penyedia diabaikan)
Persyaratan panjang konteks model ringkasan
Model ringkasan harus memiliki jendela konteks setidaknya sebesar jendela konteks model agen utama Anda. Kompresor mengirimkan seluruh bagian tengah percakapan ke model ringkasan — jika jendela konteks model tersebut lebih kecil daripada jendela konteks model utama, panggilan peringkasan akan gagal dengan kesalahan panjang konteks. Ketika ini terjadi, giliran tengah akan dihilangkan tanpa ringkasan , sehingga konteks percakapan hilang tanpa pemberitahuan. Jika Anda mengganti model, pastikan panjang konteksnya sesuai atau melebihi panjang konteks model utama Anda.

Mesin Konteks
Mesin konteks mengontrol bagaimana percakapan dikelola ketika mendekati batas token model. Mesin bawaan compressormenggunakan peringkasan yang merugikan (lihat Kompresi Konteks ). Mesin plugin dapat menggantinya dengan strategi alternatif.

context:
  engine: "compressor"    # default — built-in lossy summarization


Untuk menggunakan mesin plugin (misalnya, LCM untuk manajemen konteks tanpa kehilangan data):

context:
  engine: "lcm"          # must match the plugin's name


Mesin plugin tidak pernah diaktifkan secara otomatis — Anda harus mengaturnya secara eksplisit context.engineke nama plugin. Mesin yang tersedia dapat dijelajahi dan dipilih melalui hermes plugins→ Plugin Penyedia → Mesin Konteks.

Lihat Penyedia Memori untuk sistem pemilihan tunggal yang serupa untuk plugin memori.

Tekanan Anggaran Iterasi
Ketika agen mengerjakan tugas kompleks dengan banyak panggilan alat, ia dapat menghabiskan anggaran iterasinya (standar: 90 putaran) tanpa menyadari bahwa anggarannya hampir habis. Tekanan anggaran secara otomatis memperingatkan model saat mendekati batas:

Ambang	Tingkat	Apa yang dilihat model
70%	Peringatan	[BUDGET: 63/90. 27 iterations left. Start consolidating.]
90%	Peringatan	[BUDGET WARNING: 81/90. Only 9 left. Respond NOW.]
Peringatan disisipkan ke dalam JSON hasil alat terakhir (sebagai sebuah _budget_warningfield) dan bukan sebagai pesan terpisah — ini mempertahankan caching prompt dan tidak mengganggu struktur percakapan.

agent:
  max_turns: 90                # Max iterations per conversation turn (default: 90)
  api_max_retries: 3           # Retries per provider before fallback engages (default: 3)


Tekanan anggaran diaktifkan secara default. Agen melihat peringatan secara alami sebagai bagian dari hasil alat, mendorongnya untuk mengkonsolidasikan pekerjaannya dan memberikan respons sebelum kehabisan iterasi.

Ketika anggaran iterasi habis sepenuhnya, CLI akan menampilkan notifikasi kepada pengguna: ⚠ Iteration budget reached (90/90) — response may be incomplete. Jika anggaran habis selama pekerjaan aktif, agen akan menghasilkan ringkasan tentang apa yang telah dicapai sebelum berhenti.

agent.api_max_retriesMengontrol berapa kali Hermes mencoba kembali panggilan API penyedia pada kesalahan sementara (batas laju, putusnya koneksi, 5xx) sebelum peralihan ke penyedia cadangan diaktifkan. Nilai default adalah 3empat kali percobaan total. Jika Anda telah mengkonfigurasi penyedia cadangan dan ingin melakukan failover lebih cepat, turunkan nilai ini 0sehingga kesalahan sementara pertama pada penyedia utama Anda segera beralih ke penyedia cadangan alih-alih melakukan percobaan ulang terhadap endpoint yang tidak stabil.

Batas Waktu API
Hermes memiliki lapisan batas waktu terpisah untuk streaming, ditambah detektor data usang untuk panggilan non-streaming. Detektor data usang menyesuaikan diri secara otomatis hanya untuk penyedia lokal jika Anda membiarkannya pada pengaturan default implisitnya.

Waktu habis	Bawaan	Penyedia lokal	Konfigurasi / lingkungan
Batas waktu baca soket	120an	Ditingkatkan secara otomatis ke tahun 1800-an	HERMES_STREAM_READ_TIMEOUT
Deteksi aliran data usang	tahun 180-an	Dinonaktifkan secara otomatis	HERMES_STREAM_STALE_TIMEOUT
Deteksi non-aliran usang	300an	Dinonaktifkan secara otomatis jika dibiarkan implisit	providers.<id>.stale_timeout_secondsatauHERMES_API_CALL_STALE_TIMEOUT
Panggilan API (non-streaming)	tahun 1800-an	Tidak berubah	providers.<id>.request_timeout_seconds/ timeout_secondsatauHERMES_API_TIMEOUT
Pengaturan waktu tunggu baca soket mengontrol berapa lama httpx menunggu potongan data berikutnya dari penyedia. LLM lokal dapat memakan waktu beberapa menit untuk pengisian awal pada konteks besar sebelum menghasilkan token pertama, jadi Hermes menaikkan nilai ini menjadi 30 menit ketika mendeteksi titik akhir lokal. Jika Anda secara eksplisit mengatur nilai tersebut HERMES_STREAM_READ_TIMEOUT, nilai itu akan selalu digunakan terlepas dari deteksi titik akhir.

Deteksi aliran usang akan memutus koneksi yang menerima ping keep-alive SSE tetapi tidak menerima konten sebenarnya. Fitur ini dinonaktifkan sepenuhnya untuk penyedia lokal karena mereka tidak mengirimkan ping keep-alive selama pengisian awal.

Deteksi non-streaming yang usang akan menghentikan panggilan non-streaming yang tidak menghasilkan respons terlalu lama. Secara default, Hermes menonaktifkan ini pada endpoint lokal untuk menghindari false positive selama prefill yang lama. Jika Anda secara eksplisit mengatur providers.<id>.stale_timeout_seconds, providers.<id>.models.<model>.stale_timeout_seconds, atau HERMES_API_CALL_STALE_TIMEOUT, nilai eksplisit tersebut akan dihormati bahkan pada endpoint lokal.

Peringatan Tekanan Konteks
Terlepas dari tekanan anggaran iterasi, tekanan konteks melacak seberapa dekat percakapan dengan ambang batas pemadatan — titik di mana kompresi konteks diaktifkan untuk meringkas pesan-pesan yang lebih lama. Ini membantu Anda dan agen memahami kapan percakapan mulai panjang.

Kemajuan	Tingkat	Apa yang terjadi?
≥ 60% hingga ambang batas	Informasi	CLI menampilkan bilah kemajuan berwarna cyan; gateway mengirimkan pemberitahuan informatif.
≥ 85% hingga ambang batas	Peringatan	CLI menampilkan bilah kuning tebal; gateway memperingatkan bahwa pemadatan akan segera terjadi.
Di CLI, tekanan kontekstual muncul sebagai bilah kemajuan di umpan keluaran alat:

  ◐ context ████████████░░░░░░░░ 62% to compaction  48k threshold (50%) · approaching compaction


Pada platform perpesanan, notifikasi berupa teks biasa akan dikirimkan:

◐ Context: ████████████░░░░░░░░ 62% to compaction (threshold: 50% of window).


Jika kompresi otomatis dinonaktifkan, peringatan tersebut memberi tahu Anda bahwa konteks mungkin akan terpotong.

Tekanan konteks bersifat otomatis — tidak diperlukan konfigurasi. Tekanan konteks ini hanya muncul sebagai notifikasi bagi pengguna dan tidak memodifikasi aliran pesan atau menyuntikkan apa pun ke dalam konteks model.

Strategi Kumpulan Kredensial
Jika Anda memiliki beberapa kunci API atau token OAuth untuk penyedia yang sama, konfigurasikan strategi rotasinya:

credential_pool_strategies:
  openrouter: round_robin    # cycle through keys evenly
  anthropic: least_used      # always pick the least-used key


Opsi: fill_first(default), round_robin, least_used, random. Lihat Kumpulan Kredensial untuk dokumentasi lengkap.

Penyimpanan cache yang cepat
Hermes mengaktifkan caching prompt lintas sesi secara otomatis ketika penyedia aktif mendukungnya — tidak diperlukan konfigurasi pengguna.

Untuk Claude pada Anthropic , OpenRouter , dan Nous Portal asli , Hermes melampirkan breakpoint dengan TTL 1 jam ( ) pada prompt sistem dan blok keterampilan. Pengiriman pertama dalam satu jam baru membayar tarif input penuh; pengiriman selanjutnya di seluruh sesi dalam jam yang sama mengambil dari cache dengan tarif baca cache yang didiskon. Ini berarti prompt sistem, konten keterampilan yang dimuat, dan bagian awal dari setiap include konteks panjang digunakan kembali di seluruh sesi dan di seluruh subagen yang di-fork selama jam pertama.cache_controlttl: "1h"hermes

Qwen Cloud (Alibaba DashScope) di hulu membatasi TTL cache hingga 5 menit, jadi Hermes menggunakan breakpoint TTL 5 menit di sana sebagai gantinya. Jalur Claude-via-pihak ketiga lainnya (AWS Bedrock, Azure Foundry) kembali ke pengaturan default caching penyedia. xAI Grok menggunakan mekanisme ID percakapan yang terikat sesi terpisah — lihat caching prompt xAI .

Tidak ada tombol untuk menonaktifkan ini — caching selalu aktif dan menghemat biaya bahkan pada percakapan satu putaran karena perintah sistem saja merupakan sebagian kecil yang signifikan dari jumlah token input.

Model Tambahan
Hermes uses "auxiliary" models for side tasks like image analysis, web page summarization, browser screenshot analysis, session-title generation, and context compression. By default (auxiliary.*.provider: "auto"), Hermes routes every auxiliary task to your main chat model — the same provider/model you picked in hermes model. You don't need to configure anything to get started, but be aware that on expensive reasoning models (Opus, MiniMax M2.7, etc.) auxiliary tasks add meaningful cost. If you want cheap-and-fast side tasks regardless of your main model, set auxiliary.<task>.provider and auxiliary.<task>.model explicitly (for example, Gemini Flash on OpenRouter for vision and web extraction).

Why "auto" uses your main model
Earlier builds split aggregator users (OpenRouter, Nous Portal) onto a cheap provider-side default. That was surprising — users who paid for an aggregator subscription would see a different model handling their auxiliary traffic. auto now uses the main model for everyone, and per-task overrides in config.yaml still win (see Full auxiliary config reference below).

Configuring auxiliary models interactively
Instead of hand-editing YAML, run hermes model and pick "Configure auxiliary models" from the menu. You'll get an interactive per-task picker:

$ hermes model
→ Configure auxiliary models

[ ] vision               currently: auto / main model
[ ] web_extract          currently: auto / main model
[ ] title_generation     currently: openrouter / google/gemini-3-flash-preview
[ ] compression          currently: auto / main model
[ ] approval             currently: auto / main model
[ ] triage_specifier     currently: auto / main model
[ ] kanban_decomposer    currently: auto / main model
[ ] profile_describer    currently: auto / main model


Select a task, pick a provider (OAuth flows open a browser; API-key providers prompt), pick a model. The change persists to auxiliary.<task>.* in config.yaml. Same machinery as the main-model picker — no extra syntax to learn.

Video Tutorial

The universal config pattern
Every model slot in Hermes — auxiliary tasks, compression, fallback — uses the same three knobs:

Key	What it does	Default
provider	Which provider to use for auth and routing	"auto"
model	Which model to request	provider's default
base_url	Custom OpenAI-compatible endpoint (overrides provider)	not set
When base_url is set, Hermes ignores the provider and calls that endpoint directly (using api_key or OPENAI_API_KEY for auth). When only provider is set, Hermes uses that provider's built-in auth and base URL.

Available providers for auxiliary tasks: auto, main, plus any provider in the provider registry — openrouter, nous, openai-codex, copilot, copilot-acp, anthropic, gemini, google-gemini-cli, qwen-oauth, zai, kimi-coding, kimi-coding-cn, minimax, minimax-cn, minimax-oauth, deepseek, nvidia, xai, xai-oauth, ollama-cloud, alibaba, bedrock, huggingface, arcee, xiaomi, kilocode, opencode-zen, opencode-go, ai-gateway, azure-foundry — or any named custom provider from your custom_providers list (e.g. provider: "beans").

MiniMax OAuth
minimax-oauthMasuk melalui OAuth browser (tidak memerlukan kunci API). Jalankan hermes modeldan pilih MiniMax (OAuth) untuk melakukan autentikasi. Tugas tambahan akan digunakan MiniMax-M2.7-highspeedsecara otomatis. Lihat panduan MiniMax OAuth .

xAI Grok OAuth
xai-oauthMasuk melalui browser OAuth untuk pelanggan SuperGrok dan X Premium+ (tidak memerlukan kunci API). Jalankan hermes modeldan pilih xAI Grok OAuth (SuperGrok / Premium+) untuk melakukan autentikasi. Token OAuth yang sama digunakan kembali untuk setiap antarmuka langsung ke xAI (obrolan, tugas tambahan, TTS, pembuatan gambar, pembuatan video, transkripsi). Lihat panduan xAI Grok OAuth , dan jika Hermes berada di host jarak jauh, lihat OAuth melalui SSH / Host Jarak Jauh .

"main"hanya untuk tugas-tugas tambahan
Opsi penyedia "main"berarti "gunakan penyedia apa pun yang digunakan agen utama saya" — ini hanya berlaku di dalam konfigurasi auxiliary:, compression:, dan fallback_model:. Ini bukan nilai yang valid untuk pengaturan tingkat atas Anda model.provider. Jika Anda menggunakan endpoint kustom yang kompatibel dengan OpenAI, atur provider: customdi model:bagian Anda. Lihat Penyedia AI untuk semua opsi penyedia model utama.

Referensi konfigurasi tambahan lengkap
auxiliary:
  # Image analysis (vision_analyze tool + browser screenshots)
  vision:
    provider: "auto"           # "auto", "openrouter", "nous", "codex", "main", etc.
    model: ""                  # e.g. "openai/gpt-4o", "google/gemini-2.5-flash"
    base_url: ""               # Custom OpenAI-compatible endpoint (overrides provider)
    api_key: ""                # API key for base_url (falls back to OPENAI_API_KEY)
    timeout: 120               # seconds — LLM API call timeout; vision payloads need generous timeout
    download_timeout: 30       # seconds — image HTTP download; increase for slow connections

  # Web page summarization + browser page text extraction
  web_extract:
    provider: "auto"
    model: ""                  # e.g. "google/gemini-2.5-flash"
    base_url: ""
    api_key: ""
    timeout: 360               # seconds (6min) — per-attempt LLM summarization

  # Dangerous command approval classifier
  approval:
    provider: "auto"
    model: ""
    base_url: ""
    api_key: ""
    timeout: 30                # seconds

  # Context compression timeout (separate from compression.* config)
  compression:
    timeout: 120               # seconds — compression summarizes long conversations, needs more time

  # Skills hub — skill matching and search
  skills_hub:
    provider: "auto"
    model: ""
    base_url: ""
    api_key: ""
    timeout: 30

  # MCP tool dispatch
  mcp:
    provider: "auto"
    model: ""
    base_url: ""
    api_key: ""
    timeout: 30

  # Kanban triage specifier — `hermes kanban specify <id>` (or the
  # dashboard's ✨ Specify button on Triage-column cards) uses this
  # slot to expand a one-liner into a concrete spec and promote the
  # task to `todo`. Cheap fast models work well here; spec expansion
  # is short and doesn't need reasoning depth.
  triage_specifier:
    provider: "auto"
    model: ""
    base_url: ""
    api_key: ""
    timeout: 120


tip
Setiap tugas tambahan memiliki waktu yang dapat dikonfigurasi timeout(dalam detik). Nilai default: vision 120 detik, web_extract 360 detik, approval 30 detik, compression 120 detik. Tingkatkan nilai ini jika Anda menggunakan model lokal yang lambat untuk tugas tambahan. Vision juga memiliki waktu terpisah download_timeout(default 30 detik) untuk pengunduhan gambar HTTP — tingkatkan nilai ini untuk koneksi yang lambat atau server gambar yang dihosting sendiri.

informasi
Kompresi konteks memiliki blok tersendiri compression:untuk ambang batas dan auxiliary.compression:blok untuk pengaturan model/penyedia — lihat Kompresi Konteks di atas. Model cadangan menggunakan fallback_model:blok — lihat Model Cadangan . Ketiganya mengikuti pola penyedia/model/base_url yang sama.

Perutean OpenRouter & Kode Pareto untuk tugas-tugas tambahan
Ketika tugas tambahan terhubung ke OpenRouter (baik secara eksplisit atau melalui saat agen utama Anda berada di OpenRouter), pengaturan agen provider: "main"utama tidak akan menyebar — sesuai desain, setiap tugas tambahan bersifat independen. Untuk mengatur preferensi penyedia OpenRouter atau menggunakan router Kode Pareto untuk tugas tambahan tertentu, atur per tugas melalui :provider_routingopenrouter.min_coding_scoreextra_body

auxiliary:
  compression:
    provider: openrouter
    model: openrouter/pareto-code         # use the Pareto Code router for this task
    extra_body:
      provider:                            # OpenRouter provider routing prefs
        order: [anthropic, google]         # try these providers in order
        sort: throughput                   # or "price" | "latency"
        # only: [anthropic]                # restrict to a specific provider
        # ignore: [deepinfra]              # exclude specific providers
      plugins:                             # OpenRouter Pareto Code router knob
        - id: pareto-router
          min_coding_score: 0.5            # 0.0–1.0; higher = stronger coders


Bentuknya mencerminkan apa yang diterima OpenRouter dalam isi permintaan penyelesaian obrolan. Hermes meneruskan seluruhnya extra_bodyapa adanya, sehingga bidang isi permintaan OpenRouter lainnya yang didokumentasikan di openrouter.ai/docs berfungsi dengan cara yang sama.

Mengubah Model Visi
Untuk menggunakan GPT-4o sebagai pengganti Gemini Flash untuk analisis gambar:

auxiliary:
  vision:
    model: "openai/gpt-4o"

Atau melalui variabel lingkungan (di ~/.hermes/.env):

AUXILIARY_VISION_MODEL=openai/gpt-4o


Opsi Penyedia
Opsi ini berlaku untuk konfigurasi tugas tambahan ( auxiliary:, compression:, fallback_model:), bukan untuk model.providerpengaturan utama Anda.

Penyedia	Keterangan	Persyaratan
"auto"	Pilihan terbaik yang tersedia (default). Vision mencoba OpenRouter → Nous → Codex.	—
"openrouter"	Paksa OpenRouter — merute ke model apa pun (Gemini, GPT-4o, Claude, dll.)	OPENROUTER_API_KEY
"nous"	Portal Force Nous	hermes auth
"codex"	Paksa penggunaan Codex OAuth (akun ChatGPT). Mendukung vision (gpt-5.3-codex).	hermes model→ Kodeks
"minimax-oauth"	Paksa penggunaan MiniMax OAuth (login melalui browser, tanpa kunci API). Menggunakan MiniMax-M2.7-highspeed untuk tugas-tugas tambahan.	hermes model→ MiniMax (OAuth)
"xai-oauth"	Paksa xAI Grok OAuth (login melalui browser untuk pelanggan SuperGrok atau X Premium+, tanpa kunci API). Token OAuth yang sama mencakup obrolan, TTS, gambar, video, dan transkripsi.	hermes model→ xAI Grok OAuth (SuperGrok / Premium+)
"main"	Gunakan endpoint kustom/utama aktif Anda. Ini bisa berasal dari OPENAI_BASE_URL+ OPENAI_API_KEYatau dari endpoint kustom yang disimpan melalui hermes model/ config.yaml. Berfungsi dengan OpenAI, model lokal, atau API apa pun yang kompatibel dengan OpenAI. Hanya untuk tugas tambahan — tidak berlaku untuk model.provider.	Kredensial endpoint kustom + URL dasar
Penyedia kunci API langsung dari katalog penyedia utama juga berfungsi di sini ketika Anda ingin tugas sampingan melewati router default Anda. gmiIni berlaku setelah GMI_API_KEYdikonfigurasi:

auxiliary:
  compression:
    provider: "gmi"
    model: "anthropic/claude-opus-4.6"


Untuk perutean tambahan GMI, gunakan ID model yang tepat yang dikembalikan oleh titik akhir GMI /v1/models.

Pengaturan Umum
Menggunakan endpoint kustom langsung (lebih jelas daripada provider: "main"untuk API lokal/yang dihosting sendiri):

auxiliary:
  vision:
    base_url: "http://localhost:1234/v1"
    api_key: "local-key"
    model: "qwen2.5-vl"


base_urllebih diutamakan daripada provider, jadi ini adalah cara paling eksplisit untuk mengarahkan tugas tambahan ke titik akhir tertentu. Untuk penggantian titik akhir secara langsung, Hermes menggunakan yang dikonfigurasi api_keyatau kembali ke OPENAI_API_KEY; Hermes tidak menggunakan kembali OPENROUTER_API_KEYuntuk titik akhir khusus tersebut.

Menggunakan kunci API OpenAI untuk visi:

# In ~/.hermes/.env:
# OPENAI_BASE_URL=https://api.openai.com/v1
# OPENAI_API_KEY=sk-...

auxiliary:
  vision:
    provider: "main"
    model: "gpt-4o"       # or "gpt-4o-mini" for cheaper


Menggunakan OpenRouter untuk visi (rute ke model apa pun):

auxiliary:
  vision:
    provider: "openrouter"
    model: "openai/gpt-4o"      # or "google/gemini-2.5-flash", etc.


Menggunakan Codex OAuth (akun ChatGPT Pro/Plus — tidak memerlukan kunci API):

auxiliary:
  vision:
    provider: "codex"     # uses your ChatGPT OAuth token
    # model defaults to gpt-5.3-codex (supports vision)


Menggunakan MiniMax OAuth (login melalui browser, tidak memerlukan kunci API):

model:
  default: MiniMax-M2.7
  provider: minimax-oauth
  base_url: https://api.minimax.io/anthropic


Jalankan hermes modeldan pilih MiniMax (OAuth) untuk masuk dan mengaturnya secara otomatis. Untuk wilayah Tiongkok, URL dasarnya adalah https://api.minimaxi.com/anthropic. Lihat panduan MiniMax OAuth untuk panduan lengkapnya.

Menggunakan model lokal/mandiri:

auxiliary:
  vision:
    provider: "main"      # uses your active custom endpoint
    model: "my-local-model"


provider: "main"menggunakan penyedia apa pun yang digunakan Hermes untuk obrolan normal — baik itu penyedia khusus bernama (misalnya beans), penyedia bawaan seperti openrouter, atau OPENAI_BASE_URLtitik akhir lama.

tip
Jika Anda menggunakan Codex OAuth sebagai penyedia model utama Anda, Vision akan bekerja secara otomatis — tidak diperlukan konfigurasi tambahan. Codex termasuk dalam rantai deteksi otomatis untuk Vision.

peringatan
Penglihatan membutuhkan model multimodal. Jika Anda mengaturnya provider: "main", pastikan titik akhir Anda mendukung multimodal/penglihatan — jika tidak, analisis gambar akan gagal.

Variabel Lingkungan (lama)
Model bantu juga dapat dikonfigurasi melalui variabel lingkungan. Namun, config.yamlmetode ini lebih disukai — lebih mudah dikelola dan mendukung semua opsi termasuk base_urldan api_key.

Pengaturan	Variabel Lingkungan
Penyedia layanan penglihatan	AUXILIARY_VISION_PROVIDER
Model visi	AUXILIARY_VISION_MODEL
Titik akhir visi	AUXILIARY_VISION_BASE_URL
Kunci API Vision	AUXILIARY_VISION_API_KEY
Penyedia ekstrak web	AUXILIARY_WEB_EXTRACT_PROVIDER
Model ekstrak web	AUXILIARY_WEB_EXTRACT_MODEL
Web extract endpoint	AUXILIARY_WEB_EXTRACT_BASE_URL
Web extract API key	AUXILIARY_WEB_EXTRACT_API_KEY
Compression and fallback model settings are config.yaml-only.

tip
Run hermes config to see your current auxiliary model settings. Overrides only show up when they differ from the defaults.

Reasoning Effort
Control how much "thinking" the model does before responding:

agent:
  reasoning_effort: ""   # empty = medium (default). Options: none, minimal, low, medium, high, xhigh (max)


When unset (default), reasoning effort defaults to "medium" — a balanced level that works well for most tasks. Setting a value overrides it — higher reasoning effort gives better results on complex tasks at the cost of more tokens and latency.

You can also change the reasoning effort at runtime with the /reasoning command:

/reasoning           # Show current effort level and display state
/reasoning high      # Set reasoning effort to high
/reasoning none      # Disable reasoning
/reasoning show      # Show model thinking above each response
/reasoning hide      # Hide model thinking


Tool-Use Enforcement
Some models occasionally describe intended actions as text instead of making tool calls ("I would run the tests..." instead of actually calling the terminal). Tool-use enforcement injects system prompt guidance that steers the model back to actually calling tools.

agent:
  tool_use_enforcement: "auto"   # "auto" | true | false | ["model-substring", ...]


Value	Behavior
"auto" (default)	Enabled for models matching: gpt, codex, gemini, gemma, grok. Disabled for all others (Claude, DeepSeek, Qwen, etc.).
true	Always enabled, regardless of model. Useful if you notice your current model describing actions instead of performing them.
false	Always disabled, regardless of model.
["gpt", "codex", "qwen", "llama"]	Enabled only when the model name contains one of the listed substrings (case-insensitive).
What it injects
When enabled, three layers of guidance may be added to the system prompt:

General tool-use enforcement (all matched models) — instructs the model to make tool calls immediately instead of describing intentions, keep working until the task is complete, and never end a turn with a promise of future action.

OpenAI execution discipline (GPT and Codex models only) — additional guidance addressing GPT-specific failure modes: abandoning work on partial results, skipping prerequisite lookups, hallucinating instead of using tools, and declaring "done" without verification.

Google operational guidance (Gemini and Gemma models only) — conciseness, absolute paths, parallel tool calls, and verify-before-edit patterns.

These are transparent to the user and only affect the system prompt. Models that already use tools reliably (like Claude) don't need this guidance, which is why "auto" excludes them.

When to turn it on
If you're using a model not in the default auto list and notice it frequently describes what it would do instead of doing it, set tool_use_enforcement: true or add the model substring to the list:

agent:
  tool_use_enforcement: ["gpt", "codex", "gemini", "grok", "my-custom-model"]


TTS Configuration
tts:
  provider: "edge"              # "edge" | "elevenlabs" | "openai" | "minimax" | "mistral" | "gemini" | "xai" | "neutts"
  speed: 1.0                    # Global speed multiplier (fallback for all providers)
  edge:
    voice: "en-US-AriaNeural"   # 322 voices, 74 languages
    speed: 1.0                  # Speed multiplier (converted to rate percentage, e.g. 1.5 → +50%)
  elevenlabs:
    voice_id: "pNInz6obpgDQGcFmaJgB"
    model_id: "eleven_multilingual_v2"
  openai:
    model: "gpt-4o-mini-tts"
    voice: "alloy"              # alloy, echo, fable, onyx, nova, shimmer
    speed: 1.0                  # Speed multiplier (clamped to 0.25–4.0 by the API)
    base_url: "https://api.openai.com/v1"  # Override for OpenAI-compatible TTS endpoints
  minimax:
    speed: 1.0                  # Speech speed multiplier
    # base_url: ""              # Optional: override for OpenAI-compatible TTS endpoints
  mistral:
    model: "voxtral-mini-tts-2603"
    voice_id: "c69964a6-ab8b-4f8a-9465-ec0925096ec8"  # Paul - Neutral (default)
  gemini:
    model: "gemini-2.5-flash-preview-tts"   # or gemini-2.5-pro-preview-tts
    voice: "Kore"               # 30 prebuilt voices: Zephyr, Puck, Kore, Enceladus, etc.
  xai:
    voice_id: "eve"             # xAI TTS voice
    language: "en"              # ISO 639-1
    sample_rate: 24000
    bit_rate: 128000            # MP3 bitrate
    # base_url: "https://api.x.ai/v1"
  neutts:
    ref_audio: ''
    ref_text: ''
    model: neuphonic/neutts-air-q4-gguf
    device: cpu


This controls both the text_to_speech tool and spoken replies in voice mode (/voice tts in the CLI or messaging gateway).

Hierarki fallback kecepatan: kecepatan khusus penyedia (misalnya tts.edge.speed) → global tts.speed→ 1.0default. Atur kecepatan global tts.speeduntuk menerapkan kecepatan seragam di semua penyedia, atau timpa per penyedia untuk kontrol yang lebih detail.

Pengaturan Tampilan
display:
  tool_progress: all      # off | new | all | verbose
  tool_progress_command: false  # Enable /verbose slash command in messaging gateway
  platforms: {}           # Per-platform display overrides (see below)
  tool_progress_overrides: {}  # DEPRECATED — use display.platforms instead
  interim_assistant_messages: true  # Gateway: send natural mid-turn assistant updates as separate messages
  skin: default           # Built-in or custom CLI skin (see user-guide/features/skins)
  personality: "kawaii"  # Legacy cosmetic field still surfaced in some summaries
  compact: false          # Compact output mode (less whitespace)
  resume_display: full    # full (show previous messages on resume) | minimal (one-liner only)
  bell_on_complete: false # Play terminal bell when agent finishes (great for long tasks)
  show_reasoning: false   # Show model reasoning/thinking above each response (toggle with /reasoning show|hide)
  streaming: false        # Stream tokens to terminal as they arrive (real-time output)
  show_cost: false        # Show estimated $ cost in the CLI status bar
  timestamps: false       # When true, prefixes user and assistant labels with [HH:MM] timestamps in the CLI / TUI transcript
  tool_preview_length: 0  # Max chars for tool call previews (0 = no limit, show full paths/commands)
  runtime_footer:         # Gateway: append a runtime-context footer to final replies
    enabled: false
    fields: ["model", "context_pct", "cwd"]
  file_mutation_verifier: true    # Append an advisory footer when write_file/patch calls failed this turn
  language: en            # UI language for static messages (approval prompts, some gateway replies). en | zh | zh-hant | ja | de | es | fr | tr | uk | af | ko | it | ga | pt | ru | hu


Verifikator mutasi berkas
Saat ( display.file_mutation_verifierdefault true), Hermes menambahkan satu baris pemberitahuan ke respons akhir asisten setiap kali write_filepanggilan patchgagal selama giliran dan tidak pernah digantikan oleh penulisan yang berhasil ke jalur yang sama. Ini menangkap kelas klaim berlebihan "sekumpulan patch paralel, setengahnya gagal secara diam-diam, model merangkum keberhasilan" tanpa mengharuskan Anda menjalankannya secara manual git statussetelah setiap pengeditan.

Contoh footer:

⚠️ File-mutation verifier: 3 file(s) were NOT modified this turn despite any wording above that may suggest otherwise. Run `git status` or `read_file` to confirm.
  • concepts/automatic-organization.md — [patch] Could not find match for old_string
  • concepts/lora.md — [patch] Could not find match for old_string
  • concepts/rag-pipeline.md — [patch] Could not find match for old_string


Atur file_mutation_verifier: false(atau HERMES_FILE_MUTATION_VERIFIER=0) untuk menekan footer. Verifikator hanya akan aktif ketika ada kegagalan nyata yang belum terselesaikan di akhir giliran — model yang mencoba kembali patch yang gagal dan berhasil dalam giliran yang sama tidak akan memicunya untuk file tersebut.

Bahasa UI untuk pesan statis
Pengaturan ini display.languagemenerjemahkan sejumlah kecil pesan statis yang ditampilkan kepada pengguna — permintaan persetujuan CLI, beberapa balasan perintah slash gateway (misalnya pemberitahuan restart-drain, "persetujuan kedaluwarsa", "tujuan tercapai"). Pengaturan ini tidak menerjemahkan respons agen, baris log, output alat, pelacakan kesalahan, atau deskripsi perintah slash — semuanya tetap dalam bahasa Inggris. Jika Anda ingin agen itu sendiri membalas dalam bahasa lain, cukup beri tahu agen tersebut dalam permintaan atau pesan sistem Anda.

Nilai yang didukung: en(default), zh(Bahasa Mandarin Sederhana), ja(Bahasa Jepang), de(Bahasa Jerman), es(Bahasa Spanyol), fr(Bahasa Prancis), tr(Bahasa Turki), uk(Bahasa Ukraina). Nilai yang tidak dikenal akan menggunakan Bahasa Inggris sebagai pengganti.

Anda juga dapat mengatur ini per sesi dengan HERMES_LANGUAGEvariabel lingkungan, yang akan menimpa nilai konfigurasi.

display:
  language: zh   # CLI approval prompts appear in Chinese


Mode	Apa yang Anda lihat
off	Diam — hanya respons terakhir
new	Indikator alat hanya muncul saat alat berubah.
all	Setiap panggilan alat disertai pratinjau singkat (default)
verbose	Argumen lengkap, hasil, dan log debug
Di CLI, beralihlah di antara mode-mode ini dengan /verbose. Untuk menggunakannya /verbosedi platform perpesanan (Telegram, Discord, Slack, dll.), atur tool_progress_command: truedi displaybagian di atas. Perintah tersebut kemudian akan beralih mode dan menyimpannya ke config.

Footer metadata runtime (khusus gateway)
Saat diaktifkan display.runtime_footer.enabled: true, Hermes menambahkan catatan kaki konteks runtime kecil ke pesan akhir setiap giliran gateway — informasi yang sama yang ditampilkan CLI di bilah statusnya (model, persentase konteks, direktori kerja saat ini, durasi sesi, token, biaya). Secara default dinonaktifkan; aktifkan per-gateway jika tim Anda ingin setiap balasan menyertakan asal usulnya.

display:
  runtime_footer:
    enabled: true
    fields: ["model", "context_pct", "cwd"]   # any of: model, context_pct, cwd, duration, tokens, cost


Perintah /footerslash akan mengaktifkan atau menonaktifkan ini saat runtime di sesi mana pun.

Contoh footer yang ditambahkan ke balasan Telegram/Discord/Slack:

— claude-opus-4.7 · 12 tool calls · 2m 14s · $0.042


Hanya pesan terakhir dari suatu giliran yang mendapat bagian bawah (footer); pembaruan sementara tetap bersih.

Penggantian kemajuan per platform
Platform yang berbeda memiliki kebutuhan detail pesan yang berbeda. Misalnya, Signal tidak dapat mengedit pesan, sehingga setiap pembaruan kemajuan menjadi pesan terpisah — berisik. Gunakan display.platformsuntuk mengatur mode per platform:

display:
  tool_progress: all          # global default
  platforms:
    signal:
      tool_progress: 'off'    # silence progress on Signal
    telegram:
      tool_progress: verbose  # detailed progress on Telegram
    slack:
      tool_progress: 'off'    # quiet in shared Slack workspace


Platform tanpa pengaturan penggantian akan menggunakan tool_progressnilai global. Kunci platform yang valid: telegram, discord, slack, signal, whatsapp, matrix, mattermost, email, sms, homeassistant, dingtalk, feishu, wecom, weixin, bluebubbles, qqbot. Kunci lama display.tool_progress_overridesmasih dimuat untuk kompatibilitas mundur tetapi sudah usang dan dimigrasikan pada display.platformspemuatan pertama.

interim_assistant_messagesIni hanya berlaku untuk gateway. Saat diaktifkan, Hermes mengirimkan pembaruan asisten di tengah giliran yang telah selesai sebagai pesan obrolan terpisah. Ini independen dari tool_progressdan tidak memerlukan streaming gateway.

Pribadi
privacy:
  redact_pii: false  # Strip PII from LLM context (gateway only)


Saat redact_pii, truegateway akan menyunting informasi identitas pribadi dari perintah sistem sebelum mengirimkannya ke LLM pada platform yang didukung:

Bidang	Perlakuan
Nomor telepon (ID pengguna di WhatsApp/Signal)	Di-hash menjadiuser_<12-char-sha256>
ID Pengguna	Di-hash menjadiuser_<12-char-sha256>
ID Obrolan	Bagian numerik di-hash, awalan platform dipertahankan ( telegram:<hash>)
ID saluran utama	Bagian numerik di-hash
Nama pengguna / nama pengguna	Tidak terpengaruh (dipilih pengguna, terlihat publik)
Dukungan platform: Redaksi berlaku untuk WhatsApp, Signal, dan Telegram. Discord dan Slack dikecualikan karena sistem penyebutan mereka ( <@user_id>) memerlukan ID asli dalam konteks LLM.

Hash bersifat deterministik — pengguna yang sama selalu dipetakan ke hash yang sama, sehingga model masih dapat membedakan antara pengguna dalam obrolan grup. Perutean dan pengiriman menggunakan nilai asli secara internal.

Konversi Ucapan ke Teks (STT)
stt:
  provider: "local"            # "local" | "groq" | "openai" | "mistral"
  local:
    model: "base"              # tiny, base, small, medium, large-v3
  openai:
    model: "whisper-1"         # whisper-1 | gpt-4o-mini-transcribe | gpt-4o-transcribe
  # model: "whisper-1"         # Legacy fallback key still respected


Perilaku penyedia:

localmenggunakan faster-whisperyang berjalan di mesin Anda. Instal secara terpisah dengan pip install faster-whisper.
groqmenggunakan endpoint yang kompatibel dengan Whisper milik Groq dan membaca GROQ_API_KEY.
openaimenggunakan API ucapan OpenAI dan membaca VOICE_TOOLS_OPENAI_KEY.
Jika penyedia yang diminta tidak tersedia, Hermes akan secara otomatis beralih ke penyedia lain dengan urutan sebagai berikut: local→ groq→ openai.

Penggantian model Groq dan OpenAI didorong oleh lingkungan:

STT_GROQ_MODEL=whisper-large-v3-turbo
STT_OPENAI_MODEL=whisper-1
GROQ_BASE_URL=https://api.groq.com/openai/v1
STT_OPENAI_BASE_URL=https://api.openai.com/v1


Mode Suara (CLI)
voice:
  record_key: "ctrl+b"         # Push-to-talk key inside the CLI
  max_recording_seconds: 120    # Hard stop for long recordings
  auto_tts: false               # Enable spoken replies automatically when /voice on
  beep_enabled: true            # Play record start/stop beeps in CLI voice mode
  silence_threshold: 200        # RMS threshold for speech detection
  silence_duration: 3.0         # Seconds of silence before auto-stop


Gunakan /voice ondi CLI untuk mengaktifkan mode mikrofon, record_keymemulai/menghentikan perekaman, dan /voice ttsmengaktifkan/menonaktifkan balasan suara. Lihat Mode Suara untuk pengaturan ujung-ke-ujung dan perilaku khusus platform.

Mengalir
Kirim token secara terus-menerus ke terminal atau platform perpesanan saat token tersebut tiba, alih-alih menunggu respons lengkap.

Streaming CLI
display:
  streaming: true         # Stream tokens to terminal in real-time
  show_reasoning: true    # Also stream reasoning/thinking tokens (optional)


Saat diaktifkan, respons akan muncul token demi token di dalam kotak streaming. Panggilan alat tetap ditangkap secara diam-diam. Jika penyedia tidak mendukung streaming, secara otomatis akan kembali ke tampilan normal.

Streaming melalui Gateway (Telegram, Discord, Slack)
streaming:
  enabled: true           # Enable progressive message editing
  transport: edit         # "edit" (progressive message editing) or "off"
  edit_interval: 0.3      # Seconds between message edits
  buffer_threshold: 40    # Characters before forcing an edit flush
  cursor: " ▉"            # Cursor shown during streaming
  fresh_final_after_seconds: 60   # Send fresh final (Telegram) when preview is this old; 0 = always edit in place


Saat diaktifkan, bot akan mengirim pesan pada token pertama, lalu secara bertahap mengeditnya seiring dengan kedatangan token berikutnya. Platform yang tidak mendukung pengeditan pesan (Signal, Email, Home Assistant) akan terdeteksi secara otomatis pada percobaan pertama — streaming akan dinonaktifkan dengan baik untuk sesi tersebut tanpa membanjiri pesan.

Untuk pembaruan asisten pertengahan giliran alami terpisah tanpa pengeditan token progresif, atur display.interim_assistant_messages: true.

Penanganan luapan: Jika teks yang dialirkan melebihi batas panjang pesan platform (~4096 karakter), pesan saat ini akan diakhiri dan pesan baru akan dimulai secara otomatis.

Pembaruan akhir (Telegram): Telegram editMessageTextmempertahankan stempel waktu pesan asli, sehingga balasan streaming yang berjalan lama akan mempertahankan stempel waktu token pertama bahkan setelah selesai. Saat fresh_final_after_seconds > 0(default 60), balasan yang selesai dikirim sebagai pesan baru (dengan pratinjau usang dihapus) sehingga stempel waktu yang terlihat di Telegram mencerminkan waktu penyelesaian. Pratinjau singkat tetap diselesaikan di tempat. Atur ke 0untuk selalu mengedit di tempat.

catatan
Streaming dinonaktifkan secara default. Aktifkan ~/.hermes/config.yamluntuk mencoba pengalaman pengguna (UX) streaming.

Sesi Obrolan Grup Terisolasi
Kontrol apakah obrolan bersama menyimpan satu percakapan per ruangan atau satu percakapan per peserta:

group_sessions_per_user: true  # true = per-user isolation in groups/channels, false = one shared session per chat


trueadalah pengaturan default dan yang direkomendasikan. Di saluran Discord, grup Telegram, saluran Slack, dan konteks berbagi serupa, setiap pengirim mendapatkan sesi mereka sendiri ketika platform menyediakan ID pengguna.
falsekembali ke perilaku ruang bersama yang lama. Ini bisa berguna jika Anda secara eksplisit ingin Hermes memperlakukan saluran seperti percakapan kolaboratif, tetapi itu juga berarti pengguna berbagi konteks, biaya token, dan status interupsi.
Pesan langsung tidak terpengaruh. Hermes tetap mengklasifikasikan pesan langsung berdasarkan ID obrolan/pesan langsung seperti biasa.
Dalam kedua kasus, thread tetap terisolasi dari saluran induknya; dengan true, setiap peserta juga mendapatkan sesi mereka sendiri di dalam thread.
Untuk detail perilaku dan contohnya, lihat Sesi dan panduan Discord .

Perilaku DM yang Tidak Sah
Kendalikan apa yang dilakukan Hermes ketika pengguna yang tidak dikenal mengirim pesan langsung:

unauthorized_dm_behavior: pair

whatsapp:
  unauthorized_dm_behavior: ignore

pairadalah pengaturan default. Hermes menolak akses, tetapi membalas dengan kode pemasangan satu kali di DM.
ignoreSecara diam-diam menghapus pesan pribadi yang tidak sah.
Bagian platform akan menimpa pengaturan default global, sehingga Anda dapat tetap mengaktifkan pemasangan secara luas sambil membuat satu platform lebih senyap.
Perintah Cepat
Definisikan perintah kustom yang menjalankan perintah shell tanpa memanggil LLM, atau membuat alias dari satu perintah slash ke perintah slash lainnya. Perintah Exec quick tidak memerlukan token dan berguna dari platform perpesanan (Telegram, Discord, dll.) untuk pengecekan server cepat atau skrip utilitas.

quick_commands:
  status:
    type: exec
    command: systemctl status hermes-agent
  disk:
    type: exec
    command: df -h /
  update:
    type: exec
    command: cd ~/.hermes/hermes-agent && git pull && pip install -e .
  gpu:
    type: exec
    command: nvidia-smi --query-gpu=name,utilization.gpu,memory.used,memory.total --format=csv,noheader
  restart:
    type: alias
    target: /gateway restart


Penggunaan: ketik /status, /disk, /update, /gpu, atau /restartdi CLI atau platform perpesanan apa pun. execPerintah dijalankan secara lokal di host dan mengembalikan output secara langsung — tanpa panggilan LLM, tanpa token yang dikonsumsi. aliasPerintah ditulis ulang ke target perintah slash yang dikonfigurasi.

30-second timeout — long-running commands are killed with an error message
Priority — quick commands are checked before skill commands, so you can override skill names
Autocomplete — quick commands are resolved at dispatch time and are not shown in the built-in slash-command autocomplete tables
Type — supported types are exec and alias; other types show an error
Works everywhere — CLI, Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant
String-only prompt shortcuts are not valid quick commands. For reusable prompt workflows, create a skill or alias to an existing slash command.

Human Delay
Simulate human-like response pacing in messaging platforms:

human_delay:
  mode: "off"                  # off | natural | custom
  min_ms: 800                  # Minimum delay (custom mode)
  max_ms: 2500                 # Maximum delay (custom mode)


Code Execution
Configure the execute_code tool:

code_execution:
  mode: project                # project (default) | strict
  timeout: 300                 # Max execution time in seconds
  max_tool_calls: 50           # Max tool calls within code execution


mode controls the working directory and Python interpreter for scripts:

project (default) — scripts run in the session's working directory with the active virtualenv/conda env's python. Project deps (pandas, torch, project packages) and relative paths (.env, ./data.csv) resolve naturally, matching what terminal() sees.
strict — scripts run in a temp staging directory with sys.executable (Hermes's own python). Maximum reproducibility, but project deps and relative paths won't resolve.
Environment scrubbing (strips *_API_KEY, *_TOKEN, *_SECRET, *_PASSWORD, *_CREDENTIAL, *_PASSWD, *_AUTH) and the tool whitelist apply identically in both modes — switching mode does not change the security posture.

Web Search Backends
The web_search, web_extract, and web_crawl tools support five backend providers. Configure the backend in config.yaml or via hermes tools:

web:
  backend: firecrawl    # firecrawl | searxng | parallel | tavily | exa

  # Or use per-capability keys to mix providers (e.g. free search + paid extract):
  search_backend: "searxng"
  extract_backend: "firecrawl"


Backend	Env Var	Search	Extract	Crawl
Firecrawl (default)	FIRECRAWL_API_KEY	✔	✔	✔
SearXNG	SEARXNG_URL	✔	—	—
Parallel	PARALLEL_API_KEY	✔	✔	—
Tavily	TAVILY_API_KEY	✔	✔	✔
Exa	EXA_API_KEY	✔	✔	—
Backend selection: If web.backend is not set, the backend is auto-detected from available API keys. If only SEARXNG_URL is set, SearXNG is used. If only EXA_API_KEY is set, Exa is used. If only TAVILY_API_KEY is set, Tavily is used. If only PARALLEL_API_KEY is set, Parallel is used. Otherwise Firecrawl is the default.

SearXNG is a free, self-hosted, privacy-respecting metasearch engine that queries 70+ search engines. No API key needed — just set SEARXNG_URL to your instance (e.g., http://localhost:8080). SearXNG is search-only; web_extract and web_crawl require a separate extract provider (set web.extract_backend). See the Web Search setup guide for Docker setup instructions.

Self-hosted Firecrawl: Set FIRECRAWL_API_URL to point at your own instance. When a custom URL is set, the API key becomes optional (set `USE_DB_AUTHENTICATION=*** on the server to disable auth).

Parallel search modes: Set PARALLEL_SEARCH_MODE to control search behavior — fast, one-shot, or agentic (default: agentic).

Exa: Ditetapkan EXA_API_KEYdi ~/.hermes/.env. Mendukung categorypemfilteran ( company, research paper, news, people, personal site, pdf) dan filter domain/tanggal.

Browser
Konfigurasikan perilaku otomatisasi browser:

browser:
  inactivity_timeout: 120        # Seconds before auto-closing idle sessions
  command_timeout: 30             # Timeout in seconds for browser commands (screenshot, navigate, etc.)
  record_sessions: false         # Auto-record browser sessions as WebM videos to ~/.hermes/browser_recordings/
  # Optional CDP override — when set, Hermes attaches directly to your own
  # Chromium-family browser (via /browser connect) rather than starting a headless browser.
  cdp_url: ""
  # Dialog supervisor — controls how native JS dialogs (alert / confirm / prompt)
  # are handled when a CDP backend is attached (Browserbase, local Chromium-family
  # browser via /browser connect). Ignored on Camofox and default local agent-browser mode.
  dialog_policy: must_respond    # must_respond | auto_dismiss | auto_accept
  dialog_timeout_s: 300          # Safety auto-dismiss under must_respond (seconds)
  camofox:
    managed_persistence: false   # When true, Camofox sessions persist cookies/logins across restarts
    user_id: ""                  # Optional externally managed Camofox userId
    session_key: ""              # Optional session key sent when Hermes creates a tab
    adopt_existing_tab: false    # Reuse an existing tab for this identity before creating one


Kebijakan dialog:

must_respond(default) — tangkap dialog, tampilkan di browser_snapshot.pending_dialogs, dan tunggu agen memanggil browser_dialog(action=...). Setelah dialog_timeout_sbeberapa detik tanpa respons, dialog akan ditutup secara otomatis untuk mencegah thread JS halaman macet selamanya.
auto_dismiss— tangkap, segera tolak. Agen masih melihat catatan dialog tersebut browser_snapshot.recent_dialogssetelah closed_by="auto_policy"kejadian.
auto_accept— tangkap, terima segera. Berguna untuk halaman dengan beforeunloadajakan yang agresif.
Lihat halaman fitur peramban untuk alur kerja dialog lengkap.

Perangkat alat peramban mendukung berbagai penyedia. Lihat halaman fitur Peramban untuk detail tentang Browserbase, Penggunaan Peramban, dan pengaturan CDP keluarga Chromium lokal.

Zona waktu
Ganti zona waktu lokal server dengan string zona waktu IANA. Mempengaruhi stempel waktu dalam log, penjadwalan cron, dan injeksi waktu prompt sistem.

timezone: "America/New_York"   # IANA timezone (default: "" = server-local time)


Nilai yang didukung: pengidentifikasi zona waktu IANA apa pun (misalnya America/New_York, Europe/London, Asia/Kolkata, UTC). Biarkan kosong atau hilangkan untuk waktu lokal server.

Perselisihan
Konfigurasikan perilaku khusus Discord untuk gateway pesan:

discord:
  require_mention: true          # Require @mention to respond in server channels
  free_response_channels: ""     # Comma-separated channel IDs where bot responds without @mention
  auto_thread: true              # Auto-create threads on @mention in channels


require_mention— ketika true(default), bot hanya merespons di saluran server ketika disebutkan dengan @BotName. Pesan pribadi selalu berfungsi tanpa penyebutan.
free_response_channels— daftar ID saluran yang dipisahkan koma tempat bot merespons setiap pesan tanpa memerlukan penyebutan.
auto_thread— Saat true(default), penyebutan di saluran secara otomatis membuat utas untuk percakapan, menjaga saluran tetap rapi (mirip dengan fitur utas di Slack).
Keamanan
Pemindaian keamanan pra-eksekusi dan penyuntingan rahasia:

security:
  redact_secrets: false          # Redact API key patterns in tool output and logs (off by default)
  tirith_enabled: true           # Enable Tirith security scanning for terminal commands
  tirith_path: "tirith"          # Path to tirith binary (default: "tirith" in $PATH)
  tirith_timeout: 5              # Seconds to wait for tirith scan before timing out
  tirith_fail_open: true         # Allow command execution if tirith is unavailable
  website_blocklist:             # See Website Blocklist section below
    enabled: false
    domains: []
    shared_files: []


redact_secrets— Saat diaktifkan true, secara otomatis mendeteksi dan menyunting pola yang menyerupai kunci API, token, dan kata sandi dalam output alat sebelum masuk ke konteks percakapan dan dicatat. Nonaktif secara default — aktifkan jika Anda sering bekerja dengan kredensial asli dalam output alat dan menginginkan jaring pengaman. Atur truesecara eksplisit untuk mengaktifkannya.
tirith_enabled— ketika true, perintah terminal dipindai oleh Tirith sebelum dieksekusi untuk mendeteksi operasi yang berpotensi berbahaya.
tirith_path— jalur ke biner tirith. Atur ini jika tirith diinstal di lokasi non-standar.
tirith_timeout— waktu tunggu maksimum dalam detik untuk pemindaian tirith. Perintah akan dilanjutkan jika pemindaian habis waktu.
tirith_fail_open— Saat true(default), perintah diizinkan untuk dieksekusi jika tirith tidak tersedia atau gagal. Atur ke falseuntuk memblokir perintah saat tirith tidak dapat memverifikasinya.
Daftar Blokir Situs Web
Blokir akses ke domain tertentu oleh alat web dan peramban agen:

security:
  website_blocklist:
    enabled: false               # Enable URL blocking (default: false)
    domains:                     # List of blocked domain patterns
      - "*.internal.company.com"
      - "admin.example.com"
      - "*.local"
    shared_files:                # Load additional rules from external files
      - "/etc/hermes/blocked-sites.txt"


When enabled, any URL matching a blocked domain pattern is rejected before the web or browser tool executes. This applies to web_search, web_extract, browser_navigate, and any tool that accesses URLs.

Domain rules support:

Exact domains: admin.example.com
Wildcard subdomains: *.internal.company.com (blocks all subdomains)
TLD wildcards: *.local
Shared files contain one domain rule per line (blank lines and # comments are ignored). Missing or unreadable files log a warning but don't disable other web tools.

The policy is cached for 30 seconds, so config changes take effect quickly without restart.

Smart Approvals
Control how Hermes handles potentially dangerous commands:

approvals:
  mode: manual   # manual | smart | off


Mode	Behavior
manual (default)	Prompt the user before executing any flagged command. In the CLI, shows an interactive approval dialog. In messaging, queues a pending approval request.
smart	Use an auxiliary LLM to assess whether a flagged command is actually dangerous. Low-risk commands are auto-approved with session-level persistence. Genuinely risky commands are escalated to the user.
off	Skip all approval checks. Equivalent to HERMES_YOLO_MODE=true. Use with caution.
Smart mode is particularly useful for reducing approval fatigue — it lets the agent work more autonomously on safe operations while still catching genuinely destructive commands.

warning
Setting approvals.mode: off disables all safety checks for terminal commands. Only use this in trusted, sandboxed environments.

Checkpoints
Automatic filesystem snapshots before destructive file operations. See the Checkpoints & Rollback for details.

checkpoints:
  enabled: false                 # Enable automatic checkpoints (also: hermes chat --checkpoints). Default: false (opt-in).
  max_snapshots: 20              # Max checkpoints to keep per directory (default: 20)


Delegation
Configure subagent behavior for the delegate tool:

delegation:
  # model: "google/gemini-3-flash-preview"  # Override model (empty = inherit parent)
  # provider: "openrouter"                  # Override provider (empty = inherit parent)
  # base_url: "http://localhost:1234/v1"    # Direct OpenAI-compatible endpoint (takes precedence over provider)
  # api_key: "local-key"                    # API key for base_url (falls back to OPENAI_API_KEY)
  # api_mode: ""                            # Wire protocol for base_url: "chat_completions", "codex_responses", or "anthropic_messages". Empty = auto-detect from URL (e.g. /anthropic suffix → anthropic_messages). Set explicitly for non-standard endpoints the heuristic can't detect.
  max_concurrent_children: 3                # Parallel children per batch (floor 1, no ceiling). Also via DELEGATION_MAX_CONCURRENT_CHILDREN env var.
  max_spawn_depth: 1                        # Delegation tree depth cap (1-3, clamped). 1 = flat (default): parent spawns leaves that cannot delegate. 2 = orchestrator children can spawn leaf grandchildren. 3 = three levels.
  orchestrator_enabled: true                # Global kill switch. When false, role="orchestrator" is ignored and every child is forced to leaf regardless of max_spawn_depth.


Subagent provider:model override: By default, subagents inherit the parent agent's provider and model. Set delegation.provider and delegation.model to route subagents to a different provider:model pair — e.g., use a cheap/fast model for narrowly-scoped subtasks while your primary agent runs an expensive reasoning model.

Direct endpoint override: If you want the obvious custom-endpoint path, set delegation.base_url, delegation.api_key, and delegation.model. That sends subagents directly to that OpenAI-compatible endpoint and takes precedence over delegation.provider. If delegation.api_key is omitted, Hermes falls back to OPENAI_API_KEY only.

Wire protocol (api_mode): Hermes auto-detects the wire protocol from delegation.base_url (e.g. paths ending in /anthropic → anthropic_messages; Codex / native Anthropic / Kimi-coding hostnames keep their existing detection). For endpoints the heuristic can't classify — for example Azure AI Foundry, MiniMax, Zhipu GLM, or LiteLLM proxies fronting an Anthropic-shaped backend — set delegation.api_mode explicitly to one of chat_completions, codex_responses, or anthropic_messages. Leave it empty (the default) to keep auto-detection.

Penyedia delegasi menggunakan resolusi kredensial yang sama dengan startup CLI/gateway. Semua penyedia yang dikonfigurasi didukung: openrouter, nous, copilot, zai, kimi-coding, minimax, minimax-cn. Saat penyedia diatur, sistem secara otomatis menyelesaikan URL dasar, kunci API, dan mode API yang benar — tidak diperlukan pengaturan kredensial manual.

Prioritas: delegation.base_url dalam konfigurasi → delegation.providerdalam konfigurasi → penyedia induk (diwarisi). delegation.modeldalam konfigurasi → model induk (diwarisi). Pengaturan modeltanpa providerperubahan hanya mengubah nama model sambil mempertahankan kredensial induk (berguna untuk beralih model dalam penyedia yang sama seperti OpenRouter).

Lebar dan kedalaman: max_concurrent_children membatasi jumlah subagen yang berjalan secara paralel per batch (default 3, minimal 1, tanpa batas atas). Dapat juga diatur melalui DELEGATION_MAX_CONCURRENT_CHILDRENvariabel lingkungan. Ketika model mengirimkan tasksarray yang lebih panjang dari batas, delegate_taskakan mengembalikan kesalahan alat yang menjelaskan batas tersebut daripada memotong secara diam-diam. max_spawn_depthmengontrol kedalaman pohon delegasi (dibatasi antara 1-3). Pada nilai default 1, delegasi bersifat datar: anak tidak dapat menghasilkan cucu, dan meneruskan nilai role="orchestrator"akan secara diam-diam menurunkan kualitas menjadi leaf. Tingkatkan menjadi 2agar anak orchestrator dapat menghasilkan cucu daun; 3untuk pohon tiga tingkat. Agen memilih untuk melakukan orkestrasi per panggilan melalui role="orchestrator"; orchestrator_enabled: falsememaksa setiap anak kembali ke daun tanpa terkecuali. Biaya meningkat secara multiplikatif — pada max_spawn_depth: 3dengan max_concurrent_children: 3, pohon dapat mencapai 3×3×3 = 27 agen daun bersamaan. Lihat Delegasi Subagen → Batas Kedalaman dan Orkestrasi Bersarang untuk pola penggunaan.

Menjelaskan
Konfigurasikan perilaku permintaan klarifikasi:

clarify:
  timeout: 120                 # Seconds to wait for user clarification response


File Konteks (SOUL.md, AGENTS.md)
Hermes menggunakan dua cakupan konteks yang berbeda:

Mengajukan	Tujuan	Cakupan
SOUL.md	Identitas agen utama — mendefinisikan siapa agen tersebut (slot #1 dalam perintah sistem)	~/.hermes/SOUL.mdatau$HERMES_HOME/SOUL.md
.hermes.md/HERMES.md	Instruksi khusus proyek (prioritas tertinggi)	Berjalan ke root git
AGENTS.md	Instruksi khusus proyek, konvensi pengkodean	Penelusuran direktori rekursif
CLAUDE.md	Berkas konteks Kode Claude (juga terdeteksi)	Direktori kerja saja
.cursorrules	Aturan IDE kursor (juga terdeteksi)	Direktori kerja saja
.cursor/rules/*.mdc	Berkas aturan kursor (juga terdeteksi)	Direktori kerja saja
SOUL.md adalah identitas utama agen. File ini menempati slot #1 di prompt sistem, sepenuhnya menggantikan identitas default bawaan. Edit file ini untuk menyesuaikan sepenuhnya siapa agen tersebut.
Jika file SOUL.md hilang, kosong, atau tidak dapat dimuat, Hermes akan menggunakan identitas default bawaan.
File konteks proyek menggunakan sistem prioritas — hanya SATU tipe yang dimuat (kecocokan pertama yang menang): .hermes.md→ AGENTS.md→ CLAUDE.md→ .cursorrules. SOUL.md selalu dimuat secara independen.
AGENTS.md bersifat hierarkis: jika subdirektori juga memiliki AGENTS.md, semuanya akan digabungkan.
Hermes secara otomatis membuat instance default SOUL.mdjika instance tersebut belum ada.
Semua berkas konteks yang dimuat dibatasi hingga 20.000 karakter dengan pemotongan cerdas.
Lihat juga:

Personality & SOUL.md
Berkas Konteks
Direktori Kerja
Konteks	Bawaan
CLI ( hermes)	Direktori saat ini tempat Anda menjalankan perintah
Gerbang pesan	Direktori beranda ~(ganti dengan MESSAGING_CWD)
Docker / Singularity / Modal / SSH	Direktori beranda pengguna di dalam kontainer atau mesin jarak jauh
Ganti direktori kerja:

# In ~/.hermes/.env or ~/.hermes/config.yaml:
MESSAGING_CWD=/home/myuser/projects    # Gateway sessions
TERMINAL_CWD=/workspace                # All terminal sessions

```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Mengonfigurasi Model
Hermes menggunakan dua jenis slot model:

Model utama — apa yang digunakan agen untuk berpikir. Setiap pesan pengguna, setiap siklus panggilan alat, setiap respons yang dialirkan melewati model ini.
Model tambahan — tugas sampingan yang lebih kecil yang dialihkan oleh agen. Kompresi konteks, visi (analisis gambar), ringkasan halaman web, penilaian persetujuan, perutean alat MCP, pembuatan judul sesi, dan pencarian keterampilan. Masing-masing memiliki slotnya sendiri dan dapat ditimpa secara independen.
Halaman ini membahas konfigurasi baik dari dasbor. Jika Anda lebih suka file konfigurasi atau CLI, langsung saja ke Metode alternatif di bagian bawah.

Jalur tercepat: Portal Nous
Nous Portal menyediakan lebih dari 300 model dalam satu langganan. Pada instalasi baru, jalankan perintah hermes setup --portaluntuk masuk dan mengatur Nous sebagai penyedia Anda dalam satu perintah. Periksa apa yang terhubung dengan perintah hermes portal status.

Halaman Model
Buka dasbor dan klik Model di bilah sisi. Anda akan mendapatkan dua bagian:

Pengaturan Model — panel atas, tempat Anda menetapkan model ke slot.
Analisis penggunaan — kartu berperingkat yang menunjukkan setiap model yang menjalankan sesi dalam periode yang dipilih, dengan jumlah token, biaya, dan lencana kemampuan.
Ikhtisar halaman model

Kartu paling atas adalah panel Pengaturan Model . Baris utama selalu menampilkan apa yang akan dijalankan agen untuk sesi baru. Klik Ubah untuk membuka pemilih.

Menetapkan model utama
Klik Ubah pada baris model Utama:

Dialog pemilih model

Pemilih ini memiliki dua kolom:

Sebelah kiri — penyedia terautentikasi. Hanya penyedia yang telah Anda siapkan (kunci API telah diatur, diautentikasi dengan OAuth, atau didefinisikan sebagai titik akhir khusus) yang muncul di sini. Jika penyedia tidak ada, buka Kunci dan tambahkan kredensialnya.
Benar — daftar model pilihan untuk penyedia yang dipilih. Ini adalah model-model agen yang direkomendasikan Hermes untuk penyedia tersebut, bukan /modelsdata mentah (yang di OpenRouter mencakup lebih dari 400 model termasuk TTS, generator gambar, dan perankinger ulang).
Ketik di kotak filter untuk mempersempit pencarian berdasarkan nama penyedia, slug, atau ID model.

Pilih model, tekan Switch , dan Hermes akan menuliskannya di ~/.hermes/config.yamlbawah modelbagian tersebut. Ini hanya berlaku untuk sesi baru — tab obrolan yang sudah Anda buka akan tetap menjalankan model yang sama seperti saat pertama kali dibuka. Untuk mengganti obrolan saat ini secara instan, gunakan /modelperintah slash di dalamnya.

Menyetel model bantu
Klik Tampilkan tugas tambahan untuk melihat delapan slot tugas:

Panel tambahan diperluas

Setiap tugas tambahan secara default menggunakan auto— artinya Hermes juga menggunakan model utama Anda untuk pekerjaan tersebut. Ganti tugas tertentu jika Anda menginginkan model yang lebih murah atau lebih cepat untuk pekerjaan sampingan.

Pola penggantian umum
Tugas	Kapan harus menimpa (override)?
Judul Umum	Hampir selalu. Model flash seharga $0,10/M dapat menulis judul sesi serta Opus. Konfigurasi default mengatur ini ke aktif google/gemini-3-flash-previewdi OpenRouter.
Penglihatan	Saat model utama Anda adalah model pengkodean tanpa visi (misalnya Kimi, DeepSeek). Arahkan ke google/gemini-2.5-flashatau gpt-4o-mini.
Kompresi	Saat Anda menghabiskan token penalaran di Opus/M2.7 hanya untuk meringkas konteks. Model obrolan cepat dapat melakukan pekerjaan tersebut dengan biaya 1/50-nya.
Persetujuan	Untuk approval_mode: smartitu, model yang cepat/murah (haiku, flash, gpt-5-mini) akan menentukan apakah perintah berisiko rendah akan disetujui secara otomatis. Model yang mahal di sini adalah pemborosan.
Ekstrak Web	Saat Anda menggunakannya web_extractsecara intensif. Logikanya sama seperti kompresi — peringkasan tidak memerlukan penalaran.
Pusat Keterampilan	hermes skills searchmenggunakan ini. Biasanya baik-baik saja di auto.
MCP	Perutean alat MCP. Biasanya baik-baik saja pada auto.
Penggantian per tugas
Klik Ubah pada baris bantu mana pun. Pemilih yang sama terbuka, perilaku yang sama — pilih penyedia + model, tekan Ganti. Baris diperbarui untuk menampilkan provider · modelalih-alih auto (use main model).

Atur ulang semua ke otomatis
Jika Anda telah melakukan penyetelan berlebihan dan ingin memulai dari awal, klik Atur ulang semua ke otomatis di bagian atas bagian tambahan. Setiap slot akan kembali menggunakan model utama Anda.

Pintasan "Gunakan sebagai"
Setiap kartu model di halaman memiliki menu tarik-turun " Gunakan sebagai ". Ini adalah cara cepat — pilih model yang Anda lihat di analitik Anda, klik " Gunakan sebagai" , dan tetapkan ke slot utama atau tugas tambahan tertentu dalam satu klik:

Gunakan sebagai menu tarik-turun

Menu tarik-turun berisi:

Model utama — sama seperti mengklik Ubah pada baris utama.
Semua tugas tambahan — menetapkan model ini ke semua 8 slot tambahan sekaligus. Berguna ketika Anda hanya menginginkan semua tugas sampingan pada model flash yang murah.
Opsi tugas individual — Visi, Ekstraksi Web, Kompresi, dll. Model yang saat ini ditugaskan untuk setiap tugas ditandai dengan current.
Kartu diberi label mainatau tanda aux · <task>ketika kartu tersebut saat ini ditugaskan ke sesuatu — sehingga Anda dapat melihat sekilas model historis mana yang terhubung ke mana.

Apa yang dituliskan untukconfig.yaml
Saat Anda menyimpan melalui dasbor, Hermes akan menulis ke ~/.hermes/config.yaml:

Model utama:

model:
  provider: openrouter
  default: anthropic/claude-opus-4.7
  base_url: ''        # cleared on provider switch
  api_mode: chat_completions


Penggantian tambahan (contoh — visi pada gemini-flash):

auxiliary:
  vision:
    provider: openrouter
    model: google/gemini-2.5-flash
    base_url: ''
    api_key: ''
    timeout: 120
    extra_body: {}
    download_timeout: 30

Fitur tambahan pada mode otomatis (default):

auxiliary:
  compression:
    provider: auto
    model: ''
    base_url: ''
    # ... other fields unchanged

provider: autodengan model: ''memberi tahu Hermes untuk menggunakan model utama untuk tugas itu.

Kapan mulai berlaku?
CLI ( hermes chat): hermes chatpemanggilan berikutnya.
Gateway (Telegram, Discord, Slack, dll.): sesi baru berikutnya . Sesi yang sudah ada mempertahankan modelnya. Mulai ulang gateway ( hermes gateway restart) jika Anda ingin memaksa semua sesi untuk menerapkan perubahan.
Tab obrolan dasbor ( /chat): PTY baru berikutnya. Obrolan yang sedang terbuka mempertahankan modelnya — gunakan /modeldi dalamnya untuk melakukan hot-swap.
Perubahan tidak pernah membatalkan cache prompt pada sesi yang sedang berjalan. Itu disengaja: mengganti model utama di dalam sesi memerlukan pengaturan ulang cache (prompt sistem berisi konten spesifik model), dan kami mencadangkan itu untuk /modelperintah slash eksplisit di dalam obrolan.

Penyelesaian Masalah
"Tidak ada penyedia terautentikasi" di pemilih
Hermes hanya mencantumkan penyedia jika memiliki kredensial yang berfungsi. Periksa Kunci di bilah sisi — Anda akan melihat salah satu dari: kunci API, OAuth yang berhasil, atau URL titik akhir khusus. Jika penyedia yang Anda inginkan tidak ada di sana, jalankan perintah hermes setupuntuk menghubungkannya, atau buka Kunci dan tambahkan variabel lingkungan.

Model utama tidak berubah dalam obrolan yang sedang saya jalankan.
Sesuai harapan. Dasbor menulis config.yaml, yang dibaca oleh sesi baru. Obrolan yang sedang terbuka adalah proses agen langsung — ia mempertahankan model apa pun yang digunakan saat pertama kali dijalankan. Gunakan /model <name>di dalam obrolan untuk beralih sesi secara instan.

Penggantian tambahan "tidak berlaku"
Tiga hal yang perlu diperiksa:

Apakah Anda memulai sesi baru? Obrolan yang sudah ada tidak akan membaca ulang konfigurasi.
Apakah providerdiatur ke sesuatu selain auto? Jika kolom tersebut menampilkan auto, tugas tersebut masih menggunakan model utama Anda. Klik Ubah dan pilih penyedia yang sebenarnya.
Apakah penyedia layanan sudah terautentikasi? Jika Anda ditugaskan minimaxke suatu tugas tetapi tidak memiliki kunci API MiniMax, tugas tersebut akan kembali menggunakan default OpenRouter dan mencatat peringatan di log agent.log.
Saya sudah memilih model, tetapi Hermes mengganti penyedia layanan saya.
Pada OpenRouter (atau agregator lainnya), nama model dasar akan diselesaikan terlebih dahulu di dalam agregator. Jadi claude-sonnet-4pada OpenRouter menjadianthropic/claude-sonnet-4.6 , dan tetap menggunakan otentikasi OpenRouter Anda. Tetapi jika Anda mengetikkan claude-sonnet-4pada otentikasi Anthropic asli, itu akan tetap sebagai claude-sonnet-4-6. Jika Anda melihat pergantian penyedia yang tidak terduga, periksa apakah penyedia Anda saat ini sesuai dengan yang Anda harapkan — pemilih selalu menampilkan penyedia utama saat ini di bagian atas dialog.

Metode alternatif
Perintah garis miring CLI
Di dalam hermes chatsesi mana pun:

/model gpt-5.4 --provider openrouter             # session-only
/model gpt-5.4 --provider openrouter --global    # also persists to config.yaml


--globalmelakukan hal yang sama seperti dasbor.Fungsinya sama seperti tombol Ubah , ditambah lagi, tombol ini mengganti sesi yang sedang berjalan secara langsung.

Alias ​​kustom
Tetapkan nama pendek Anda sendiri untuk model yang sering Anda gunakan, lalu gunakan /model <alias>di CLI atau platform perpesanan apa pun:

# ~/.hermes/config.yaml
model_aliases:
  fav:
    model: claude-sonnet-4.6
    provider: anthropic
  grok:
    model: grok-4
    provider: x-ai

Atau dari cangkang (bentuk singkat provider/model):

hermes config set model.aliases.fav anthropic/claude-opus-4.6
hermes config set model.aliases.grok x-ai/grok-4


Kemudian /model favatau /model grokdalam obrolan. Alias ​​pengguna menutupi nama pendek bawaan ( sonnet, kimi, opus, dll.). Lihat Alias ​​model kustom untuk referensi lengkapnya.

hermes modelsubperintah
hermes model            # Interactive provider + model picker (the canonical way to switch defaults)


hermes modelPanduan ini akan memandu Anda dalam memilih penyedia, melakukan autentikasi (alur OAuth membuka browser; penyedia kunci API meminta kunci), dan kemudian memilih model tertentu dari katalog pilihan penyedia tersebut. Pilihan tersebut ditulis ke model.providerdanmodel.model format ~/.hermes/config.yaml.

Untuk melihat daftar penyedia/model tanpa menjalankan pemilih, gunakan dasbor atau titik akhir REST di bawah ini. Untuk memeriksa apa yang sebenarnya akan digunakan CLI saat ini:hermes config get model dan hermes status.

Pengeditan konfigurasi langsung
Edit ~/.hermes/config.yamldan mulai ulang apa pun yang membacanya. Lihat referensi Konfigurasi untuk skema lengkapnya.

API REST
Dasbor ini menggunakan tiga titik akhir. Berguna untuk pembuatan skrip:

# List authenticated providers + curated model lists
curl -H "X-Hermes-Session-Token: $TOKEN" http://localhost:PORT/api/model/options

# Read current main + auxiliary assignments
curl -H "X-Hermes-Session-Token: $TOKEN" http://localhost:PORT/api/model/auxiliary

# Set the main model
curl -X POST -H "Content-Type: application/json" -H "X-Hermes-Session-Token: $TOKEN" \
  -d '{"scope":"main","provider":"openrouter","model":"anthropic/claude-opus-4.7"}' \
  http://localhost:PORT/api/model/set

# Override a single auxiliary task
curl -X POST -H "Content-Type: application/json" -H "X-Hermes-Session-Token: $TOKEN" \
  -d '{"scope":"auxiliary","task":"vision","provider":"openrouter","model":"google/gemini-2.5-flash"}' \
  http://localhost:PORT/api/model/set

# Assign one model to every auxiliary task
curl -X POST -H "Content-Type: application/json" -H "X-Hermes-Session-Token: $TOKEN" \
  -d '{"scope":"auxiliary","task":"","provider":"openrouter","model":"google/gemini-2.5-flash"}' \
  http://localhost:PORT/api/model/set

# Reset all auxiliary tasks to auto
curl -X POST -H "Content-Type: application/json" -H "X-Hermes-Session-Token: $TOKEN" \
  -d '{"scope":"auxiliary","task":"__reset__","provider":"","model":""}' \
  http://localhost:PORT/api/model/set


Token sesi disuntikkan ke dalam HTML dasbor saat startup dan berganti setiap kali server dimulai ulang. Ambil token tersebut dari devtools browser ( window.__HERMES_SESSION_TOKEN__) jika Anda membuat skrip terhadap dasbor yang sedang berjalan.
```

---
===========🔐™️®️©️🔐===========

---
```

SECRET 
Hermes dapat mengambil kunci API dari pengelola rahasia eksternal saat proses dimulai, alih-alih menyimpannya di ~/.hermes/.env. Token bootstrap untuk pengelola rahasia berada di .env; setiap kunci penyedia lainnya (OpenAI, Anthropic, OpenRouter, dll.) dapat tetap berada di pengelola dan dirotasi secara terpusat.

Didukung:

Bitwarden Secrets Manager — bwsCLI, instalasi malas (lazy-installed), versi gratis berfungsi.
Lebih banyak backend (Vault, AWS Secrets Manager, 1Password CLI) mudah ditambahkan di balik antarmuka yang sama — hanya perlu satu modul agent/secret_sources/dan satu handler CLI. Ajukan permintaan jika Anda memiliki backend spesifik yang ingin ditambahkan
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Pengelola Rahasia Bitwarden
Ambil kunci API dari Bitwarden Secrets Manager saat proses dimulai, alih-alih menyimpannya dalam bentuk teks biasa di dalam file ~/.hermes/.env. Satu rahasia bootstrap (token akses akun mesin) menggantikan N kunci per penyedia, dan rotasi kredensial menjadi satu perubahan di aplikasi web Bitwarden.

Cara kerjanya
Anda membuat akun mesin di Bitwarden Secrets Manager, memberikannya akses baca ke sebuah proyek, dan menghasilkan token akses .
Hermes menyimpan token tunggal itu ~/.hermes/.envsebagai BWS_ACCESS_TOKEN.
Setiap kali hermes(atau gateway, atau cron job) dimulai, setelah ~/.hermes/.envdimuat, Hermes memanggil bws secret list <project_id>dan mengatur kunci yang dikembalikan ke dalam os.environ.
Secara default, Hermes menimpa nilai yang sudah ada di lingkungan Anda, jadi Bitwarden adalah sumber kebenaran — putar kunci sekali di aplikasi web dan setiap proses Hermes akan mengambilnya pada saat dimulai berikutnya. Ubah override_existing: falsedi konfigurasi jika Anda ingin .envmenang.
File bwsbiner diunduh secara otomatis ~/.hermes/bin/saat pertama kali digunakan — tidak apt, tidak brew, tidak sudo.

Mengapa akun mesin (dan mengapa tidak ada permintaan otentikasi dua faktor)?
Bitwarden Secrets Manager dirancang untuk beban kerja non-interaktif: akun mesin tidak dapat di-2FA karena tidak ada campur tangan manusia. Token akses adalah kredensialnya. Siapa pun yang memilikinya dapat membaca setiap rahasia yang dapat diakses oleh akun mesin tersebut, jadi perlakukanlah seperti token pembawa bernilai tinggi — simpan di .env(bukan config.yaml), dan cabut + buat ulang dari aplikasi web Bitwarden jika terjadi kebocoran.

Anda mengatur akun mesin di aplikasi web , tempat otentikasi dua faktor (2FA) normal Anda berlaku. Setelah itu, token akan berfungsi secara otomatis.

Pengaturan
1. Buat akun mesin dan token akses
Di aplikasi web Bitwarden (atau vault.bitwarden.eu untuk akun Uni Eropa):

Beralihlah ke Secrets Manager dari pengalih produk.
Buat atau pilih Proyek (misalnya "Kunci Hermes").
Tambahkan kunci penyedia Anda sebagai rahasia. Nama rahasia tersebut menjadi nama variabel lingkungan — gunakan OPENROUTER_API_KEY, ANTHROPIC_API_KEY, dll.
Akun mesin → Akun mesin baru → Mesin Hermes saya → Tab Proyek → berikan akses Baca ke proyek Anda.
Tab Token Akses → Buat token akses → Tidak pernah kedaluwarsa (atau pilih tanggal) → salin token (diawali dengan 0.). Bitwarden tidak dapat mengambilnya lagi — simpan salinannya.
Secrets Manager termasuk dalam paket gratis Bitwarden dengan batasan tertentu; tidak diperlukan paket berbayar untuk mencobanya.

2. Jalankan wizard
hermes secrets bitwarden setup

Itu akan:

Unduh dan verifikasi bws v2.0.0ke ~/.hermes/bin/bws.
Meminta Anda memasukkan token akses (input disembunyikan). Disimpan ~/.hermes/.envsebagai BWS_ACCESS_TOKEN.
Tanyakan wilayah Bitwarden mana yang menjadi bagian dari akun mesin Anda — US Cloud , EU Cloud , atau URL kustom/hosting sendiri . Disimpan dalam config.yamldan secrets.bitwarden.server_urlditeruskan bwske BWS_SERVER_URL.
Daftar proyek yang dapat dilihat oleh akun mesin; pilih salah satu. Disimpan config.yamlsebagai secrets.bitwarden.project_id.
Lakukan pengujian dengan mengambil rahasia proyek dan menunjukkan variabel lingkungan mana yang akan diselesaikan.
Balikkan secrets.bitwarden.enabled: true.
Pengaturan non-interaktif juga didukung melalui flag:

hermes secrets bitwarden setup \
  --access-token "$BWS_ACCESS_TOKEN" \
  --server-url https://vault.bitwarden.eu \
  --project-id <project-uuid>


3. Konfirmasi
hermes secrets bitwarden status

Mulai sekarang, setiap hermespemanggilan akan mengambil rahasia baru saat startup. Anda akan melihat ringkasan satu baris di stderr pertama kali rahasia diterapkan dalam suatu proses.

CLI
Memerintah	Apa fungsinya?
hermes secrets bitwarden setup	Panduan interaktif (instalasi biner, minta token, pilih proyek, uji pengambilan data)
hermes secrets bitwarden status	Tampilkan konfigurasi + versi biner + keberadaan token
hermes secrets bitwarden sync	Simulasi: ambil rahasia sekarang dan tunjukkan apa yang akan diterapkan.
hermes secrets bitwarden sync --apply	Ambil dan ekspor ke lingkungan shell saat ini.
hermes secrets bitwarden install	Cukup unduh bwsfile biner yang disematkan (tidak perlu otentikasi)
hermes secrets bitwarden disable	Balikkan enabled: false; membiarkan token + ID proyek tetap di tempatnya
Konfigurasi
Nilai default dalam ~/.hermes/config.yaml:

secrets:
  bitwarden:
    enabled: false
    access_token_env: BWS_ACCESS_TOKEN
    project_id: ""
    server_url: ""
    cache_ttl_seconds: 300
    override_existing: true
    auto_install: true


Kunci	Bawaan	Apa fungsinya?
enabled	false	Saklar utama. Jika bernilai false, Bitwarden tidak akan pernah dihubungi.
access_token_env	BWS_ACCESS_TOKEN	Nama variabel lingkungan yang menyimpan token bootstrap. Ubah ini jika Anda sudah menggunakannya BWS_ACCESS_TOKENuntuk hal lain.
project_id	""	UUID proyek yang akan disinkronkan.
server_url	""	Wilayah Bitwarden atau titik akhir yang dihosting sendiri. Kosong = bwsdefault (Cloud AS https://vault.bitwarden.com). Atur ke https://vault.bitwarden.euuntuk Cloud UE, atau URL Anda sendiri untuk yang dihosting sendiri. Dimasukkan ke dalam bwssubproses sebagai BWS_SERVER_URL.
cache_ttl_seconds	300	Berapa lama hasil pengambilan data dalam proses digunakan kembali. Atur ke `true` 0untuk menonaktifkan caching. Cache bersifat per-proses; hermespemanggilan baru dimulai dari awal.
override_existing	true	Jika bernilai true, nilai Bitwarden akan menimpa apa pun yang sudah ada di env (sehingga rotasi di aplikasi web benar-benar berlaku). Ubah ke true falsejika Anda ingin .envekspor shell berlaku secara lokal.
auto_install	true	Jika bernilai true, bwsmaka akan diunduh secara otomatis ~/.hermes/bin/saat pertama kali digunakan.
Mode kegagalan
Bitwarden tidak pernah menghalangi proses startup Hermes. Jika terjadi kesalahan, Anda akan melihat peringatan satu baris di stderr dan Hermes akan melanjutkan dengan kredensial .envyang sudah ada:

Gejala	Menyebabkan	Memperbaiki
BWS_ACCESS_TOKEN is not set	Diaktifkan dalam konfigurasi tetapi token dihapus dari.env	Memutarkan lagihermes secrets bitwarden setup
bws exited 1: invalid access token	Token dicabut atau salah	Buat token baru, jalankan kembali pengaturan.
[400 Bad Request] {"error":"invalid_client"}	Token tersebut untuk wilayah Bitwarden yang berbeda dari wilayah bwsyang melakukan panggilan (misalnya, token EU yang digunakan untuk mengakses endpoint identitas AS).	Jalankan ulang pengaturan dan pilih wilayah yang tepat, atau atur secrets.bitwarden.server_urlke https://vault.bitwarden.eu(atau URL yang Anda host sendiri)
bws timed out	Jaringan diblokir atau API Bitwarden lambat	Periksa konektivitas ke api.bitwarden.com(atau milik Anda server_url)
bws binary not available	auto_install: falsedan bwstidak ada di PATH	Instal secara manual dari github.com/bitwarden/sdk-sm/releases atau kembali auto_installke pengaturan semula.
Checksum mismatch	Unduhan rusak atau telah dimodifikasi	Akan dijalankan ulang; jika masalah berlanjut, laporkan masalah tersebut.
Catatan keamanan
Token bootstrap ( BWS_ACCESS_TOKEN) itu sendiri bersifat sensitif — siapa pun yang memilikinya dapat membaca setiap rahasia yang dapat diakses oleh akun mesin. Perlakukan token ini sama seperti kunci API lainnya.
Hermes akan menolak untuk membiarkan Bitwarden menimpa token bootstrap itu sendiri, bahkan dengan override_existing: true. Jika Anda menyimpannya BWS_ACCESS_TOKENsebagai rahasia di dalam proyek, itu akan dilewati secara diam-diam selama penerapan.
File bwsbiner yang diunduh diverifikasi terhadap checksum SHA-256 yang dipublikasikan dari rilis GitHub yang sama. Ketidakcocokan akan membatalkan instalasi.
Versi yang disematkan ( bws v2.0.0pada saat penulisan) diperbarui melalui PR ke repositori ini — Hermes tidak secara otomatis memperbarui bwske "versi terbaru" karena bentuk rilis upstream dapat berubah.
Kapan TIDAK menggunakan ini
Pengaturan pribadi pada satu mesin tidak ~/.hermes/.envmasalah. Anda menukar satu kredensial dengan kredensial lain dan menambahkan ketergantungan jaringan saat startup.
Lingkungan terisolasi udara yang tidak dapat dijangkau api.bitwarden.com.
CI/CD di mana mekanisme injeksi rahasia yang ada (rahasia GitHub Actions, Vault, dll.) sudah diatur — pilih satu jalur, bukan dua.
Contoh yang tepat untuk ini adalah armada multi-mesin, kotak pengembangan bersama, VPS gateway, atau pengaturan apa pun di mana Anda menginginkan rotasi dan pencabutan terpusat di beberapa instalasi Hermes.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Sesi
Hermes Agent secara otomatis menyimpan setiap percakapan sebagai sesi. Sesi memungkinkan melanjutkan percakapan, pencarian lintas sesi, dan manajemen riwayat percakapan lengkap.

Cara Kerja Sesi
Setiap percakapan — baik dari CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams, atau platform perpesanan lainnya — disimpan sebagai sesi dengan riwayat pesan lengkap. Sesi dilacak di:

Basis data SQLite ( ~/.hermes/state.db) — metadata sesi terstruktur dengan pencarian teks lengkap FTS5, ditambah riwayat pesan lengkap
Basis data SQLite menyimpan:

ID sesi, platform sumber, ID pengguna
Judul sesi (nama unik yang mudah dibaca manusia)
Nama dan konfigurasi model
Cuplikan tampilan prompt sistem
Riwayat pesan lengkap (peran, konten, panggilan alat, hasil alat)
Jumlah token (masukan/keluaran)
Stempel waktu (dimulai pada, berakhir pada)
ID sesi induk (untuk pemisahan sesi yang dipicu oleh kompresi)
Apa yang Dianggap Sebagai Konteks
Hermes menyimpan riwayat sesi sehingga dapat melanjutkan percakapan, tetapi tidak terus mengirim ulang setiap byte yang pernah ditanganinya. Pada setiap giliran, model melihat perintah sistem yang dipilih, jendela percakapan saat ini, dan konten apa pun yang secara eksplisit disuntikkan Hermes untuk giliran tersebut.

Lampiran media ditangani sebagai masukan yang dibatasi oleh giliran:

Gambar dapat dilampirkan secara langsung ke panggilan model berikutnya, atau dianalisis terlebih dahulu menjadi deskripsi teks ketika model aktif tidak mendukung penglihatan bawaan.
Audio akan ditranskripsikan menjadi teks ketika fitur pengenalan suara ke teks diaktifkan.
Dokumen teks dapat menyertakan teks yang diekstrak; jenis dokumen lain biasanya diwakili oleh jalur lokal yang tersimpan dan catatan singkat.
Jalur lampiran dan teks yang diekstrak/diturunkan dapat muncul dalam transkrip, tetapi byte gambar mentah, audio, atau file biner tidak disalin berulang kali ke dalam perintah selanjutnya.
Sebagai contoh, jika pengguna mengirimkan gambar dan meminta Hermes untuk membuat meme darinya, Hermes mungkin akan memeriksa gambar tersebut sekali dengan penglihatan dan menjalankan skrip pemrosesan gambar. Giliran selanjutnya tidak secara otomatis membawa JPEG asli dalam konteksnya. Giliran tersebut hanya membawa apa pun yang ditulis ke dalam percakapan, seperti permintaan pengguna, deskripsi singkat gambar, jalur cache lokal, atau respons akhir asisten.

Penyebab paling umum dari pertumbuhan konteks bukanlah file media itu sendiri. Melainkan teks yang bertele-tele: transkrip yang disalin, log lengkap, output alat yang besar, perbedaan yang panjang, laporan status yang berulang, dan dump bukti yang detail. Lebih baik gunakan ringkasan, jalur file, kutipan yang terfokus, dan pencarian yang didukung alat daripada menyalin artefak besar ke dalam obrolan.

tip
Gunakan /compresssaat sesi berlangsung lama, /newuntuk memulai thread baru, dan hermes sessions prunehanya saat Anda ingin menghapus sesi lama yang telah berakhir dari penyimpanan. Kompresi mengurangi konteks aktif; ini bukan penghapusan privasi. Berikan nama ke /new(misalnya /new payments-refactor) untuk mengatur judul awal sesi baru di awal — berguna untuk menemukannya nanti dengan /resume <name>atau di /sessionspemilih.

Sumber Sesi
Setiap sesi diberi tag dengan platform sumbernya:

Sumber	Keterangan
cli	CLI interaktif ( hermesatau hermes chat)
telegram	Telegram Messenger
discord	Server Discord/DM
slack	Ruang kerja Slack
whatsapp	WhatsApp Messenger
signal	Pembawa pesan sinyal
matrix	Ruang Matrix dan DM
mattermost	Saluran Mattermost
email	Email (IMAP/SMTP)
sms	SMS melalui Twilio
dingtalk	Aplikasi pesan DingTalk
feishu	Utusan Feishu/Lark
wecom	WeCom (WeChat Work)
weixin	Weixin (WeChat pribadi)
bluebubbles	Apple iMessage melalui server macOS BlueBubbles
qqbot	QQ Bot (Tencent QQ) melalui API Resmi v2
homeassistant	Percakapan dengan Asisten Rumah
webhook	Webhook masuk
api-server	Permintaan server API
acp	Integrasi editor ACP
cron	Tugas cron terjadwal
batch	Pemrosesan batch berjalan
Lanjutkan Sesi CLI
Lanjutkan percakapan sebelumnya dari CLI menggunakan --continueatau --resume:

Lanjutkan Sesi Sebelumnya
# Resume the most recent CLI session
hermes --continue
hermes -c

# Or with the chat subcommand
hermes chat --continue
hermes chat -c


Ini mencari sesi terbaru clidari basis data SQLite dan memuat riwayat percakapan lengkapnya.

Resume berdasarkan Nama
Jika Anda telah memberi judul pada sesi (lihat Penamaan Sesi di bawah), Anda dapat melanjutkannya dengan nama tersebut:

# Resume a named session
hermes -c "my project"

# If there are lineage variants (my project, my project #2, my project #3),
# this automatically resumes the most recent one
hermes -c "my project"   # → resumes "my project #3"


Lanjutkan Sesi Spesifik
# Resume a specific session by ID
hermes --resume 20250305_091523_a1b2c3d4
hermes -r 20250305_091523_a1b2c3d4

# Resume by title
hermes --resume "refactoring auth"

# Or with the chat subcommand
hermes chat --resume 20250305_091523_a1b2c3d4


ID sesi ditampilkan saat Anda keluar dari sesi CLI, dan dapat ditemukan dengan hermes sessions list.

Rekap Percakapan tentang Resume
Saat Anda melanjutkan sesi, Hermes menampilkan ringkasan singkat percakapan sebelumnya dalam panel bergaya sebelum kolom input:

Pratinjau bergaya dari panel rekap Percakapan Sebelumnya yang ditampilkan saat melanjutkan sesi Hermes.
Mode resume menampilkan panel rekap ringkas dengan giliran pengguna dan asisten terbaru sebelum mengembalikan Anda ke prompt langsung.

Ringkasannya:

Menampilkan pesan pengguna (emas ●) dan respons asisten (hijau ◆)
Memotong pesan panjang (300 karakter untuk pengguna, 200 karakter / 3 baris untuk asisten)
Menggabungkan jumlah panggilan alat menjadi hitungan beserta nama alat (misalnya, [3 tool calls: terminal, web_search])
Menyembunyikan pesan sistem, hasil alat, dan penalaran internal.
Batasan pada 10 pertukaran terakhir dengan indikator "... N pesan sebelumnya ..."
Menggunakan gaya redup untuk membedakan dari percakapan aktif.
Untuk menonaktifkan rekap dan mempertahankan perilaku satu baris minimal, atur di ~/.hermes/config.yaml:

display:
  resume_display: minimal   # default: full


tip
ID sesi mengikuti format YYYYMMDD_HHMMSS_<hex>— sesi CLI/TUI menggunakan akhiran heksadesimal 6 karakter (misalnya 20250305_091523_a1b2c3), sesi gateway menggunakan akhiran 8 karakter (misalnya 20250305_091523_a1b2c3d4). Anda dapat melanjutkan berdasarkan ID (lengkap atau awalan unik) atau berdasarkan judul — keduanya berfungsi dengan -cdan -r.

Pengalihan Lintas Platform
Gunakan /handoff <platform>dari sesi CLI untuk mentransfer percakapan langsung ke saluran utama platform perpesanan. Agen akan melanjutkan tepat di tempat CLI berhenti — ID sesi yang sama, transkrip lengkap yang mempertimbangkan peran, panggilan alat, dan semuanya.

# Inside a CLI session
/handoff telegram

Yang terjadi:

CLI memvalidasi bahwa <platform>fitur tersebut diaktifkan dan memiliki saluran utama yang telah diatur (jalankan /sethomesekali dari obrolan tujuan untuk mengkonfigurasinya).

CLI menandai sesi sebagai tertunda dan melakukan polling blok ke gateway . Ia menolak jika agen sedang dalam giliran — tunggu hingga respons saat ini selesai terlebih dahulu.

Pengawas gateway mengklaim serah terima dan meminta adaptor tujuan untuk thread baru:

Telegram — membuka topik forum baru (topik DM jika mode Topik Bot API 9.4+ diaktifkan di obrolan, atau topik supergrup forum).
Discord — membuat utas arsip otomatis berdurasi 1440 menit di bawah saluran teks utama.
Slack — mengirimkan pesan awal dan menggunakannya tssebagai jangkar utas.
WhatsApp / Signal / Matrix / SMS — tidak ada percakapan internal, langsung beralih ke saluran utama.
Gateway mengikat ulang kunci tujuan ke ID sesi CLI Anda yang sudah ada, kemudian membuat giliran pengguna sintetis yang meminta agen untuk mengkonfirmasi dan meringkas. Balasan tersebut masuk ke thread baru.

Ketika gateway mengkonfirmasi keberhasilan, CLI akan mencetak /resumepetunjuk dan keluar dengan bersih:

↻ Handoff complete. The session is now active on telegram.
  Resume it on this CLI later with: /resume my-session-title


Dari titik itu, percakapan berlanjut di platform. Balas di utas baru — siapa pun yang berwenang di saluran tersebut berbagi sesi yang sama, dan pesan pengguna sebenarnya berikutnya dalam utas akan bergabung dengan lancar karena sesi utas menggunakan kunci tanpa titik user_id.

Kembali ke CLI: saat Anda ingin kembali ke desktop, cukup jalankan /resume <title>(atau hermes -r "<title>"dari shell) dan lanjutkan dari tempat platform berhenti.

Mode kegagalan:

Tidak ada saluran utama yang dikonfigurasi → CLI menolak dengan /sethomepetunjuk.
Platform tidak diaktifkan / gateway tidak berjalan → CLI akan habis waktu (timeout) pada 60 detik dengan pesan yang jelas dan sesi CLI Anda tetap utuh.
Pembuatan thread gagal (izin, topics-mode nonaktif) → kembali ke channel utama secara langsung dan tetap selesai; tidak ada isolasi thread tetapi proses handoff itu sendiri berhasil.
adapter.sendGagal (batas laju, kesalahan API sementara) → serah terima ditandai gagal dengan alasannya; baris tersebut dihapus sehingga Anda dapat mencoba lagi.
Keterbatasan yang perlu diketahui: untuk platform yang tidak mendukung threading dengan saluran grup multi-pengguna, fitur ini berfungsi sebagai sesi bergaya DM. Ini berfungsi untuk saluran DM pribadi (pengaturan umum) tetapi tidak ideal untuk obrolan grup bersama yang sebenarnya. Threading mencakup Telegram / Discord / Slack — yang merupakan kasus paling umum — sehingga sebagian besar pengaturan tidak pernah mencapai tahap ini.

Penamaan Sesi
Berikan judul sesi yang mudah dibaca agar Anda dapat menemukan dan melanjutkan sesi tersebut dengan mudah.

Judul yang Dihasilkan Secara Otomatis
Hermes secara otomatis menghasilkan judul deskriptif singkat (3–7 kata) untuk setiap sesi setelah pertukaran pertama. Proses ini berjalan di thread latar belakang menggunakan model bantu yang cepat, sehingga tidak menambah latensi. Anda akan melihat judul yang dihasilkan secara otomatis saat menjelajahi sesi dengan hermes sessions listatau hermes sessions browse.

Pembuatan judul otomatis hanya berjalan sekali per sesi dan akan dilewati jika Anda telah menetapkan judul secara manual.

Mengatur Judul Secara Manual
Gunakan /titleperintah slash di dalam sesi obrolan apa pun (CLI atau gateway):

/title my research project

Judul diterapkan secara langsung. Jika sesi belum dibuat di basis data (misalnya, Anda menjalankannya /titlesebelum mengirim pesan pertama Anda), judul tersebut akan dimasukkan ke dalam antrian dan diterapkan setelah sesi dimulai.

Anda juga dapat mengganti nama sesi yang sudah ada dari baris perintah:

hermes sessions rename 20250305_091523_a1b2c3d4 "refactoring auth module"


Aturan Judul
Unik — tidak ada dua sesi yang dapat memiliki judul yang sama.
Maksimal 100 karakter — agar hasil daftar tetap rapi.
Disterilkan — karakter kontrol, karakter tanpa lebar, dan penggantian RTL dihilangkan secara otomatis.
Unicode standar sudah cukup — emoji, CJK, dan karakter beraksen semuanya berfungsi.
Auto-Lineage pada Kompresi
Ketika konteks sesi dikompresi (secara manual /compressatau otomatis), Hermes membuat sesi lanjutan baru. Jika sesi asli memiliki judul, sesi baru secara otomatis mendapatkan judul bernomor:

"my project" → "my project #2" → "my project #3"


Saat Anda melanjutkan berdasarkan nama ( hermes -c "my project"), sistem akan secara otomatis memilih sesi terbaru dalam silsilah.

/judul di Platform Perpesanan
Perintah ini /titleberfungsi di semua platform gateway (Telegram, Discord, Slack, WhatsApp):

/title My Research— tetapkan judul sesi
/title— tampilkan judul saat ini
Perintah Manajemen Sesi
Hermes menyediakan serangkaian perintah manajemen sesi lengkap melalui hermes sessions:

Daftar Sesi
# List recent sessions (default: last 20)
hermes sessions list

# Filter by platform
hermes sessions list --source telegram

# Show more sessions
hermes sessions list --limit 50


Jika sesi memiliki judul, output akan menampilkan judul, pratinjau, dan stempel waktu relatif:

Title                  Preview                                  Last Active   ID
────────────────────────────────────────────────────────────────────────────────────────────────
refactoring auth       Help me refactor the auth module please   2h ago        20250305_091523_a
my project #3          Can you check the test failures?          yesterday     20250304_143022_e
—                      What's the weather in Las Vegas?          3d ago        20250303_101500_f


Jika tidak ada sesi yang memiliki judul, format yang lebih sederhana akan digunakan:

Preview                                            Last Active   Src    ID
──────────────────────────────────────────────────────────────────────────────────────
Help me refactor the auth module please             2h ago        cli    20250305_091523_a
What's the weather in Las Vegas?                    3d ago        tele   20250303_101500_f


Ekspor Sesi
# Export all sessions to a JSONL file
hermes sessions export backup.jsonl

# Export sessions from a specific platform
hermes sessions export telegram-history.jsonl --source telegram

# Export a single session
hermes sessions export session.jsonl --session-id 20250305_091523_a1b2c3d4


File yang diekspor berisi satu objek JSON per baris dengan metadata sesi lengkap dan semua pesan.

Hapus Sesi
# Delete a specific session (with confirmation)
hermes sessions delete 20250305_091523_a1b2c3d4

# Delete without confirmation
hermes sessions delete 20250305_091523_a1b2c3d4 --yes


Mengganti nama sesi
# Set or change a session's title
hermes sessions rename 20250305_091523_a1b2c3d4 "debugging auth flow"

# Multi-word titles don't need quotes in the CLI
hermes sessions rename 20250305_091523_a1b2c3d4 debugging auth flow


Jika judul tersebut sudah digunakan oleh sesi lain, akan ditampilkan pesan kesalahan.

Pangkas Sesi Lama
# Delete ended sessions older than 90 days (default)
hermes sessions prune

# Custom age threshold
hermes sessions prune --older-than 30

# Only prune sessions from a specific platform
hermes sessions prune --source telegram --older-than 60

# Skip confirmation
hermes sessions prune --older-than 30 --yes


informasi
Penghapusan sesi yang sudah berakhir (sesi yang telah diakhiri secara eksplisit atau direset secara otomatis) hanya akan dihapus. Sesi aktif tidak akan pernah dihapus.

Statistik Sesi
hermes sessions stats

Keluaran:

Total sessions: 142
Total messages: 3847
  cli: 89 sessions
  telegram: 38 sessions
  discord: 15 sessions
Database size: 12.4 MB

Untuk analisis yang lebih mendalam — penggunaan token, perkiraan biaya, rincian alat, dan pola aktivitas — gunakan hermes insights.

Alat Pencarian Sesi
Agen ini memiliki alat bawaan session_searchyang melakukan pencarian teks lengkap di seluruh percakapan sebelumnya menggunakan mesin FTS5 SQLite — dan memungkinkan agen untuk menelusuri sesi apa pun yang ditemukannya. Tidak ada panggilan LLM, tidak ada peringkasan, tidak ada pemotongan. Setiap bentuk mengembalikan pesan aktual dari basis data.

Tiga bentuk panggilan
Alat ini menyimpulkan apa yang Anda inginkan dari argumen yang Anda tetapkan. Tidak ada modeparameter.

1. Discovery — pass query:

session_search(query="auth refactor", limit=3)


Menjalankan FTS5, menghilangkan duplikasi hit berdasarkan silsilah sesi, mengembalikan N sesi teratas. Setiap hasil berisi:

session_id, title, when,source
snippet— Cuplikan pertandingan unggulan FTS5
bookend_start— 3 pesan pertama pengguna+asisten dalam sesi tersebut (tujuan/awal sesi)
messages— ±5 pesan di sekitar kecocokan FTS5, dengan pesan jangkar ditandai (kecocokan dalam konteks)
bookend_end— 3 pesan terakhir pengguna+asisten dalam sesi tersebut (resolusi/keputusan)
match_message_id, messages_before,messages_after
Bookends + window bersama-sama merekonstruksi tujuan → pertandingan → resolusi tanpa membayar seluruh transkrip. Waktu eksekusi tipikal: 15–50ms pada basis data sesi nyata.

2. Gulir — lewati session_id+ around_message_id:

session_search(session_id="20260510_174648_805cc2", around_message_id=590803, window=10)


Mengembalikan jendela berisi ± windowpesan yang berpusat pada jangkar. Tanpa FTS5, tanpa pembatas — hanya potongan gambar. Gunakan setelah panggilan penemuan ketika Anda membutuhkan konteks lebih dari jendela default ±5.

Untuk menggulir ke depan : lewati messages[-1].idke belakang sebagaiaround_message_id
Untuk menggulir ke belakang : kembalikan messages[0].idsebagaiaround_message_id
Pesan batas muncul di kedua jendela sebagai penanda orientasi.
Ketika messages_beforeatau messages_afterkurang dari window, Anda berada di awal atau akhir sesi.
Waktu respons tipikal: 1–2 ms per panggilan gulir.

3. Jelajahi — tanpa argumen:

session_search()

Menampilkan sesi terbaru secara kronologis (judul, pratinjau, stempel waktu). Berguna ketika pengguna bertanya "sedang mengerjakan apa" tanpa menyebutkan topik.

Sintaks kueri FTS5
Mode kata kunci mendukung sintaks kueri FTS5 standar:

Kata kunci sederhana: docker deployment(FTS5 secara default menggunakan AND)
Frasa:"exact phrase"
Boolean: docker OR kubernetes,python NOT java
Awalan:deploy*
Parameter opsional
sort— newestatau oldest, di atas peringkat FTS5. Abaikan untuk pengurutan hanya berdasarkan relevansi (standar; cocok untuk mengingat secara eksploratif). Gunakan newestuntuk pertanyaan "di mana kita meninggalkan X", oldestuntuk pertanyaan "bagaimana X dimulai".
role_filter— peran yang dipisahkan koma untuk disertakan. Penemuan default ke user,assistant(output alat biasanya berupa gangguan). Lewatkan user,assistant,tooluntuk menyertakan output alat (perilaku alat debugging) atau tooluntuk hanya mencari output alat.
Saat Digunakan
Agen tersebut diminta untuk menggunakan pencarian sesi secara otomatis:

"Ketika pengguna merujuk sesuatu dari percakapan sebelumnya atau Anda menduga ada konteks relevan sebelumnya, gunakan session_search untuk mengingatnya sebelum meminta mereka mengulanginya."

Pemicu umum: "kita pernah melakukan ini sebelumnya", "ingatkah saat itu", "terakhir kali", "seperti yang sudah saya sebutkan", atau referensi apa pun ke proyek/orang/konsep yang tidak ada di jendela saat ini.

Pelacakan Sesi Per Platform
Sesi Gerbang
Pada platform perpesanan, sesi ditandai dengan kunci sesi deterministik yang dibangun dari sumber pesan:

Jenis Obrolan	Format Tombol Default	Perilaku
Telegram DM	agent:main:telegram:dm:<chat_id>	Satu sesi per obrolan DM
DM Discord	agent:main:discord:dm:<chat_id>	Satu sesi per obrolan DM
Pesan Langsung WhatsApp	agent:main:whatsapp:dm:<canonical_identifier>	Satu sesi per pengguna DM (LID/alias telepon digabungkan menjadi satu identitas jika pemetaan ada)
Obrolan grup	agent:main:<platform>:group:<chat_id>:<user_id>	Per pengguna di dalam grup ketika platform menampilkan ID pengguna.
Diskusi/topik grup	agent:main:<platform>:group:<chat_id>:<thread_id>	Sesi bersama untuk semua peserta thread (default). Per pengguna dengan thread_sessions_per_user: true.
Saluran	agent:main:<platform>:channel:<chat_id>:<user_id>	Per pengguna di dalam saluran ketika platform mengekspos ID pengguna.
Jika Hermes tidak dapat memperoleh pengidentifikasi peserta untuk obrolan bersama, maka Hermes akan menggunakan satu sesi bersama untuk ruangan tersebut.

Sesi Kelompok Bersama vs Sesi Kelompok Terpisah
Secara default, Hermes menggunakan group_sessions_per_user: true. config.yamlItu artinya:

Alice dan Bob sama-sama dapat berbicara dengan Hermes di saluran Discord yang sama tanpa perlu berbagi riwayat transkrip.
Tugas panjang dan berat yang dilakukan oleh satu pengguna tidak mengganggu jendela konteks pengguna lain.
Penanganan interupsi juga tetap per pengguna karena kunci agen yang berjalan cocok dengan kunci sesi terisolasi.
Jika Anda menginginkan satu "otak ruangan" bersama, atur:

group_sessions_per_user: false

Hal itu mengembalikan grup/saluran ke sesi bersama tunggal per ruangan, yang mempertahankan konteks percakapan bersama tetapi juga berbagi biaya token, status interupsi, dan pertumbuhan konteks.

Kebijakan Reset Sesi
Sesi gateway direset secara otomatis berdasarkan kebijakan yang dapat dikonfigurasi:

tidak aktif — diatur ulang setelah N menit tidak aktif
harian — diatur ulang pada jam tertentu setiap hari
keduanya — direset berdasarkan mana yang terjadi lebih dulu (tidak aktif atau harian)
tidak ada — tidak pernah diatur ulang secara otomatis
Sebelum sesi direset secara otomatis, agen diberi kesempatan untuk menyimpan kenangan atau keterampilan penting dari percakapan tersebut.

Sesi dengan proses latar belakang yang aktif tidak akan pernah direset secara otomatis, terlepas dari kebijakan yang diterapkan.

Lokasi Penyimpanan
Apa	Jalur	Keterangan
Basis data SQLite	~/.hermes/state.db	Semua metadata sesi + pesan dengan FTS5
Pesan gerbang	~/.hermes/state.db	SQLite — penyimpanan kanonik untuk semua pesan sesi.
Indeks perutean gateway	~/.hermes/sessions/sessions.json	Memetakan kunci sesi ke ID sesi aktif (metadata asal, flag kedaluwarsa)
Basis data SQLite menggunakan mode WAL untuk pembaca bersamaan dan penulis tunggal, yang sangat sesuai dengan arsitektur multi-platform gateway.

Transkrip JSONL lama
Sesi yang dibuat sebelum state.db menjadi kanonik mungkin memiliki sisa *.jsonlfile di ~/.hermes/sessions/. File-file tersebut tidak lagi ditulis atau dibaca oleh Hermes. Aman untuk dihapus setelah memverifikasi bahwa sesi yang bersangkutan ada di state.db.

Skema Basis Data
Tabel-tabel utama dalam state.db:

sesi — metadata sesi (id, sumber, user_id, model, judul, stempel waktu, jumlah token). Judul memiliki indeks unik (judul NULL diperbolehkan, hanya yang bukan NULL yang harus unik).
pesan — riwayat pesan lengkap (peran, konten, panggilan alat, nama alat, jumlah token)
messages_fts — Tabel virtual FTS5 untuk pencarian teks lengkap di seluruh konten pesan
Kedaluwarsa Sesi dan Pembersihan
Pembersihan Otomatis
Sesi gateway akan direset secara otomatis berdasarkan kebijakan reset yang telah dikonfigurasi.
Sebelum direset, agen menyimpan memori dan keterampilan dari sesi yang akan berakhir.
Opsi penghapusan otomatis: ketika sessions.auto_prune, truesesi yang telah berakhir dan lebih lama dari sessions.retention_days(default 90) akan dihapus saat CLI/gateway dimulai.
Setelah penghapusan baris yang sebenarnya dilakukan, state.dbdata VACUUMdikirim untuk menghemat ruang disk (SQLite tidak mengecilkan file pada perintah DELETE biasa).
Pemangkasan dijalankan paling banyak sekali per sessions.min_interval_hours(standar 24); stempel waktu eksekusi terakhir dilacak di dalam state.dbdirinya sendiri sehingga dibagikan di setiap proses Hermes yang sama.HERMES_HOME
Secara default, fitur ini dinonaktifkan — riwayat sesi sangat berharga untuk session_searchmengingat kembali informasi, dan menghapusnya secara diam-diam dapat mengejutkan pengguna. Aktifkan di ~/.hermes/config.yaml:

sessions:
  auto_prune: true          # opt in — default is false
  retention_days: 90        # keep ended sessions this many days
  vacuum_after_prune: true  # reclaim disk space after a pruning sweep
  min_interval_hours: 24    # don't re-run the sweep more often than this


Sesi aktif tidak pernah dihapus secara otomatis, terlepas dari usianya.

Pembersihan Manual
# Prune sessions older than 90 days
hermes sessions prune

# Delete a specific session
hermes sessions delete <session_id>

# Export before pruning (backup)
hermes sessions export backup.jsonl
hermes sessions prune --older-than 30 --yes


tip
Basis data tumbuh perlahan (biasanya: 10-15 MB untuk ratusan sesi) dan riwayat sesi mendukung session_searchpemanggilan kembali percakapan masa lalu, sehingga fitur auto-prune dinonaktifkan. Aktifkan fitur ini jika Anda menjalankan beban kerja gateway/cron yang berat yang state.dbsecara signifikan memengaruhi kinerja (mode kegagalan yang diamati: state.db 384 MB dengan ~1000 sesi memperlambat penyisipan dan /resumepencatatan FTS5). Gunakan hermes sessions pruneuntuk pembersihan sekali saja tanpa mengaktifkan pembersihan otomatis.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Sesi
Hermes Agent secara otomatis menyimpan setiap percakapan sebagai sesi. Sesi memungkinkan melanjutkan percakapan, pencarian lintas sesi, dan manajemen riwayat percakapan lengkap.

Cara Kerja Sesi
Setiap percakapan — baik dari CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams, atau platform perpesanan lainnya — disimpan sebagai sesi dengan riwayat pesan lengkap. Sesi dilacak di:

Basis data SQLite ( ~/.hermes/state.db) — metadata sesi terstruktur dengan pencarian teks lengkap FTS5, ditambah riwayat pesan lengkap
Basis data SQLite menyimpan:

ID sesi, platform sumber, ID pengguna
Judul sesi (nama unik yang mudah dibaca manusia)
Nama dan konfigurasi model
Cuplikan tampilan prompt sistem
Riwayat pesan lengkap (peran, konten, panggilan alat, hasil alat)
Jumlah token (masukan/keluaran)
Stempel waktu (dimulai pada, berakhir pada)
ID sesi induk (untuk pemisahan sesi yang dipicu oleh kompresi)
Apa yang Dianggap Sebagai Konteks
Hermes menyimpan riwayat sesi sehingga dapat melanjutkan percakapan, tetapi tidak terus mengirim ulang setiap byte yang pernah ditanganinya. Pada setiap giliran, model melihat perintah sistem yang dipilih, jendela percakapan saat ini, dan konten apa pun yang secara eksplisit disuntikkan Hermes untuk giliran tersebut.

Lampiran media ditangani sebagai masukan yang dibatasi oleh giliran:

Gambar dapat dilampirkan secara langsung ke panggilan model berikutnya, atau dianalisis terlebih dahulu menjadi deskripsi teks ketika model aktif tidak mendukung penglihatan bawaan.
Audio akan ditranskripsikan menjadi teks ketika fitur pengenalan suara ke teks diaktifkan.
Dokumen teks dapat menyertakan teks yang diekstrak; jenis dokumen lain biasanya diwakili oleh jalur lokal yang tersimpan dan catatan singkat.
Jalur lampiran dan teks yang diekstrak/diturunkan dapat muncul dalam transkrip, tetapi byte gambar mentah, audio, atau file biner tidak disalin berulang kali ke dalam perintah selanjutnya.
Sebagai contoh, jika pengguna mengirimkan gambar dan meminta Hermes untuk membuat meme darinya, Hermes mungkin akan memeriksa gambar tersebut sekali dengan penglihatan dan menjalankan skrip pemrosesan gambar. Giliran selanjutnya tidak secara otomatis membawa JPEG asli dalam konteksnya. Giliran tersebut hanya membawa apa pun yang ditulis ke dalam percakapan, seperti permintaan pengguna, deskripsi singkat gambar, jalur cache lokal, atau respons akhir asisten.

Penyebab paling umum dari pertumbuhan konteks bukanlah file media itu sendiri. Melainkan teks yang bertele-tele: transkrip yang disalin, log lengkap, output alat yang besar, perbedaan yang panjang, laporan status yang berulang, dan dump bukti yang detail. Lebih baik gunakan ringkasan, jalur file, kutipan yang terfokus, dan pencarian yang didukung alat daripada menyalin artefak besar ke dalam obrolan.

tip
Gunakan /compresssaat sesi berlangsung lama, /newuntuk memulai thread baru, dan hermes sessions prunehanya saat Anda ingin menghapus sesi lama yang telah berakhir dari penyimpanan. Kompresi mengurangi konteks aktif; ini bukan penghapusan privasi. Berikan nama ke /new(misalnya /new payments-refactor) untuk mengatur judul awal sesi baru di awal — berguna untuk menemukannya nanti dengan /resume <name>atau di /sessionspemilih.

Sumber Sesi
Setiap sesi diberi tag dengan platform sumbernya:

Sumber	Keterangan
cli	CLI interaktif ( hermesatau hermes chat)
telegram	Telegram Messenger
discord	Server Discord/DM
slack	Ruang kerja Slack
whatsapp	WhatsApp Messenger
signal	Pembawa pesan sinyal
matrix	Ruang Matrix dan DM
mattermost	Saluran Mattermost
email	Email (IMAP/SMTP)
sms	SMS melalui Twilio
dingtalk	Aplikasi pesan DingTalk
feishu	Utusan Feishu/Lark
wecom	WeCom (WeChat Work)
weixin	Weixin (WeChat pribadi)
bluebubbles	Apple iMessage melalui server macOS BlueBubbles
qqbot	QQ Bot (Tencent QQ) melalui API Resmi v2
homeassistant	Percakapan dengan Asisten Rumah
webhook	Webhook masuk
api-server	Permintaan server API
acp	Integrasi editor ACP
cron	Tugas cron terjadwal
batch	Pemrosesan batch berjalan
Lanjutkan Sesi CLI
Lanjutkan percakapan sebelumnya dari CLI menggunakan --continueatau --resume:

Lanjutkan Sesi Sebelumnya
# Resume the most recent CLI session
hermes --continue
hermes -c

# Or with the chat subcommand
hermes chat --continue
hermes chat -c


Ini mencari sesi terbaru clidari basis data SQLite dan memuat riwayat percakapan lengkapnya.

Resume berdasarkan Nama
Jika Anda telah memberi judul pada sesi (lihat Penamaan Sesi di bawah), Anda dapat melanjutkannya dengan nama tersebut:

# Resume a named session
hermes -c "my project"

# If there are lineage variants (my project, my project #2, my project #3),
# this automatically resumes the most recent one
hermes -c "my project"   # → resumes "my project #3"


Lanjutkan Sesi Spesifik
# Resume a specific session by ID
hermes --resume 20250305_091523_a1b2c3d4
hermes -r 20250305_091523_a1b2c3d4

# Resume by title
hermes --resume "refactoring auth"

# Or with the chat subcommand
hermes chat --resume 20250305_091523_a1b2c3d4


ID sesi ditampilkan saat Anda keluar dari sesi CLI, dan dapat ditemukan dengan hermes sessions list.

Rekap Percakapan tentang Resume
Saat Anda melanjutkan sesi, Hermes menampilkan ringkasan singkat percakapan sebelumnya dalam panel bergaya sebelum kolom input:

Pratinjau bergaya dari panel rekap Percakapan Sebelumnya yang ditampilkan saat melanjutkan sesi Hermes.
Mode resume menampilkan panel rekap ringkas dengan giliran pengguna dan asisten terbaru sebelum mengembalikan Anda ke prompt langsung.

Ringkasannya:

Menampilkan pesan pengguna (emas ●) dan respons asisten (hijau ◆)
Memotong pesan panjang (300 karakter untuk pengguna, 200 karakter / 3 baris untuk asisten)
Menggabungkan jumlah panggilan alat menjadi hitungan beserta nama alat (misalnya, [3 tool calls: terminal, web_search])
Menyembunyikan pesan sistem, hasil alat, dan penalaran internal.
Batasan pada 10 pertukaran terakhir dengan indikator "... N pesan sebelumnya ..."
Menggunakan gaya redup untuk membedakan dari percakapan aktif.
Untuk menonaktifkan rekap dan mempertahankan perilaku satu baris minimal, atur di ~/.hermes/config.yaml:

display:
  resume_display: minimal   # default: full


tip
ID sesi mengikuti format YYYYMMDD_HHMMSS_<hex>— sesi CLI/TUI menggunakan akhiran heksadesimal 6 karakter (misalnya 20250305_091523_a1b2c3), sesi gateway menggunakan akhiran 8 karakter (misalnya 20250305_091523_a1b2c3d4). Anda dapat melanjutkan berdasarkan ID (lengkap atau awalan unik) atau berdasarkan judul — keduanya berfungsi dengan -cdan -r.

Pengalihan Lintas Platform
Gunakan /handoff <platform>dari sesi CLI untuk mentransfer percakapan langsung ke saluran utama platform perpesanan. Agen akan melanjutkan tepat di tempat CLI berhenti — ID sesi yang sama, transkrip lengkap yang mempertimbangkan peran, panggilan alat, dan semuanya.

# Inside a CLI session
/handoff telegram

Yang terjadi:

CLI memvalidasi bahwa <platform>fitur tersebut diaktifkan dan memiliki saluran utama yang telah diatur (jalankan /sethomesekali dari obrolan tujuan untuk mengkonfigurasinya).

CLI menandai sesi sebagai tertunda dan melakukan polling blok ke gateway . Ia menolak jika agen sedang dalam giliran — tunggu hingga respons saat ini selesai terlebih dahulu.

Pengawas gateway mengklaim serah terima dan meminta adaptor tujuan untuk thread baru:

Telegram — membuka topik forum baru (topik DM jika mode Topik Bot API 9.4+ diaktifkan di obrolan, atau topik supergrup forum).
Discord — membuat utas arsip otomatis berdurasi 1440 menit di bawah saluran teks utama.
Slack — mengirimkan pesan awal dan menggunakannya tssebagai jangkar utas.
WhatsApp / Signal / Matrix / SMS — tidak ada percakapan internal, langsung beralih ke saluran utama.
Gateway mengikat ulang kunci tujuan ke ID sesi CLI Anda yang sudah ada, kemudian membuat giliran pengguna sintetis yang meminta agen untuk mengkonfirmasi dan meringkas. Balasan tersebut masuk ke thread baru.

Ketika gateway mengkonfirmasi keberhasilan, CLI akan mencetak /resumepetunjuk dan keluar dengan bersih:

↻ Handoff complete. The session is now active on telegram.
  Resume it on this CLI later with: /resume my-session-title


Dari titik itu, percakapan berlanjut di platform. Balas di utas baru — siapa pun yang berwenang di saluran tersebut berbagi sesi yang sama, dan pesan pengguna sebenarnya berikutnya dalam utas akan bergabung dengan lancar karena sesi utas menggunakan kunci tanpa titik user_id.

Kembali ke CLI: saat Anda ingin kembali ke desktop, cukup jalankan /resume <title>(atau hermes -r "<title>"dari shell) dan lanjutkan dari tempat platform berhenti.

Mode kegagalan:

Tidak ada saluran utama yang dikonfigurasi → CLI menolak dengan /sethomepetunjuk.
Platform tidak diaktifkan / gateway tidak berjalan → CLI akan habis waktu (timeout) pada 60 detik dengan pesan yang jelas dan sesi CLI Anda tetap utuh.
Pembuatan thread gagal (izin, topics-mode nonaktif) → kembali ke channel utama secara langsung dan tetap selesai; tidak ada isolasi thread tetapi proses handoff itu sendiri berhasil.
adapter.sendGagal (batas laju, kesalahan API sementara) → serah terima ditandai gagal dengan alasannya; baris tersebut dihapus sehingga Anda dapat mencoba lagi.
Keterbatasan yang perlu diketahui: untuk platform yang tidak mendukung threading dengan saluran grup multi-pengguna, fitur ini berfungsi sebagai sesi bergaya DM. Ini berfungsi untuk saluran DM pribadi (pengaturan umum) tetapi tidak ideal untuk obrolan grup bersama yang sebenarnya. Threading mencakup Telegram / Discord / Slack — yang merupakan kasus paling umum — sehingga sebagian besar pengaturan tidak pernah mencapai tahap ini.

Penamaan Sesi
Berikan judul sesi yang mudah dibaca agar Anda dapat menemukan dan melanjutkan sesi tersebut dengan mudah.

Judul yang Dihasilkan Secara Otomatis
Hermes secara otomatis menghasilkan judul deskriptif singkat (3–7 kata) untuk setiap sesi setelah pertukaran pertama. Proses ini berjalan di thread latar belakang menggunakan model bantu yang cepat, sehingga tidak menambah latensi. Anda akan melihat judul yang dihasilkan secara otomatis saat menjelajahi sesi dengan hermes sessions listatau hermes sessions browse.

Pembuatan judul otomatis hanya berjalan sekali per sesi dan akan dilewati jika Anda telah menetapkan judul secara manual.

Mengatur Judul Secara Manual
Gunakan /titleperintah slash di dalam sesi obrolan apa pun (CLI atau gateway):

/title my research project

Judul diterapkan secara langsung. Jika sesi belum dibuat di basis data (misalnya, Anda menjalankannya /titlesebelum mengirim pesan pertama Anda), judul tersebut akan dimasukkan ke dalam antrian dan diterapkan setelah sesi dimulai.

Anda juga dapat mengganti nama sesi yang sudah ada dari baris perintah:

hermes sessions rename 20250305_091523_a1b2c3d4 "refactoring auth module"


Aturan Judul
Unik — tidak ada dua sesi yang dapat memiliki judul yang sama.
Maksimal 100 karakter — agar hasil daftar tetap rapi.
Disterilkan — karakter kontrol, karakter tanpa lebar, dan penggantian RTL dihilangkan secara otomatis.
Unicode standar sudah cukup — emoji, CJK, dan karakter beraksen semuanya berfungsi.
Auto-Lineage pada Kompresi
Ketika konteks sesi dikompresi (secara manual /compressatau otomatis), Hermes membuat sesi lanjutan baru. Jika sesi asli memiliki judul, sesi baru secara otomatis mendapatkan judul bernomor:

"my project" → "my project #2" → "my project #3"


Saat Anda melanjutkan berdasarkan nama ( hermes -c "my project"), sistem akan secara otomatis memilih sesi terbaru dalam silsilah.

/judul di Platform Perpesanan
Perintah ini /titleberfungsi di semua platform gateway (Telegram, Discord, Slack, WhatsApp):

/title My Research— tetapkan judul sesi
/title— tampilkan judul saat ini
Perintah Manajemen Sesi
Hermes menyediakan serangkaian perintah manajemen sesi lengkap melalui hermes sessions:

Daftar Sesi
# List recent sessions (default: last 20)
hermes sessions list

# Filter by platform
hermes sessions list --source telegram

# Show more sessions
hermes sessions list --limit 50


Jika sesi memiliki judul, output akan menampilkan judul, pratinjau, dan stempel waktu relatif:

Title                  Preview                                  Last Active   ID
────────────────────────────────────────────────────────────────────────────────────────────────
refactoring auth       Help me refactor the auth module please   2h ago        20250305_091523_a
my project #3          Can you check the test failures?          yesterday     20250304_143022_e
—                      What's the weather in Las Vegas?          3d ago        20250303_101500_f


Jika tidak ada sesi yang memiliki judul, format yang lebih sederhana akan digunakan:

Preview                                            Last Active   Src    ID
──────────────────────────────────────────────────────────────────────────────────────
Help me refactor the auth module please             2h ago        cli    20250305_091523_a
What's the weather in Las Vegas?                    3d ago        tele   20250303_101500_f


Ekspor Sesi
# Export all sessions to a JSONL file
hermes sessions export backup.jsonl

# Export sessions from a specific platform
hermes sessions export telegram-history.jsonl --source telegram

# Export a single session
hermes sessions export session.jsonl --session-id 20250305_091523_a1b2c3d4


File yang diekspor berisi satu objek JSON per baris dengan metadata sesi lengkap dan semua pesan.

Hapus Sesi
# Delete a specific session (with confirmation)
hermes sessions delete 20250305_091523_a1b2c3d4

# Delete without confirmation
hermes sessions delete 20250305_091523_a1b2c3d4 --yes


Mengganti nama sesi
# Set or change a session's title
hermes sessions rename 20250305_091523_a1b2c3d4 "debugging auth flow"

# Multi-word titles don't need quotes in the CLI
hermes sessions rename 20250305_091523_a1b2c3d4 debugging auth flow


Jika judul tersebut sudah digunakan oleh sesi lain, akan ditampilkan pesan kesalahan.

Pangkas Sesi Lama
# Delete ended sessions older than 90 days (default)
hermes sessions prune

# Custom age threshold
hermes sessions prune --older-than 30

# Only prune sessions from a specific platform
hermes sessions prune --source telegram --older-than 60

# Skip confirmation
hermes sessions prune --older-than 30 --yes


informasi
Penghapusan sesi yang sudah berakhir (sesi yang telah diakhiri secara eksplisit atau direset secara otomatis) hanya akan dihapus. Sesi aktif tidak akan pernah dihapus.

Statistik Sesi
hermes sessions stats

Keluaran:

Total sessions: 142
Total messages: 3847
  cli: 89 sessions
  telegram: 38 sessions
  discord: 15 sessions
Database size: 12.4 MB

Untuk analisis yang lebih mendalam — penggunaan token, perkiraan biaya, rincian alat, dan pola aktivitas — gunakan hermes insights.

Alat Pencarian Sesi
Agen ini memiliki alat bawaan session_searchyang melakukan pencarian teks lengkap di seluruh percakapan sebelumnya menggunakan mesin FTS5 SQLite — dan memungkinkan agen untuk menelusuri sesi apa pun yang ditemukannya. Tidak ada panggilan LLM, tidak ada peringkasan, tidak ada pemotongan. Setiap bentuk mengembalikan pesan aktual dari basis data.

Tiga bentuk panggilan
Alat ini menyimpulkan apa yang Anda inginkan dari argumen yang Anda tetapkan. Tidak ada modeparameter.

1. Discovery — pass query:

session_search(query="auth refactor", limit=3)


Menjalankan FTS5, menghilangkan duplikasi hit berdasarkan silsilah sesi, mengembalikan N sesi teratas. Setiap hasil berisi:

session_id, title, when,source
snippet— Cuplikan pertandingan unggulan FTS5
bookend_start— 3 pesan pertama pengguna+asisten dalam sesi tersebut (tujuan/awal sesi)
messages— ±5 pesan di sekitar kecocokan FTS5, dengan pesan jangkar ditandai (kecocokan dalam konteks)
bookend_end— 3 pesan terakhir pengguna+asisten dalam sesi tersebut (resolusi/keputusan)
match_message_id, messages_before,messages_after
Bookends + window bersama-sama merekonstruksi tujuan → pertandingan → resolusi tanpa membayar seluruh transkrip. Waktu eksekusi tipikal: 15–50ms pada basis data sesi nyata.

2. Gulir — lewati session_id+ around_message_id:

session_search(session_id="20260510_174648_805cc2", around_message_id=590803, window=10)


Mengembalikan jendela berisi ± windowpesan yang berpusat pada jangkar. Tanpa FTS5, tanpa pembatas — hanya potongan gambar. Gunakan setelah panggilan penemuan ketika Anda membutuhkan konteks lebih dari jendela default ±5.

Untuk menggulir ke depan : lewati messages[-1].idke belakang sebagaiaround_message_id
Untuk menggulir ke belakang : kembalikan messages[0].idsebagaiaround_message_id
Pesan batas muncul di kedua jendela sebagai penanda orientasi.
Ketika messages_beforeatau messages_afterkurang dari window, Anda berada di awal atau akhir sesi.
Waktu respons tipikal: 1–2 ms per panggilan gulir.

3. Jelajahi — tanpa argumen:

session_search()

Menampilkan sesi terbaru secara kronologis (judul, pratinjau, stempel waktu). Berguna ketika pengguna bertanya "sedang mengerjakan apa" tanpa menyebutkan topik.

Sintaks kueri FTS5
Mode kata kunci mendukung sintaks kueri FTS5 standar:

Kata kunci sederhana: docker deployment(FTS5 secara default menggunakan AND)
Frasa:"exact phrase"
Boolean: docker OR kubernetes,python NOT java
Awalan:deploy*
Parameter opsional
sort— newestatau oldest, di atas peringkat FTS5. Abaikan untuk pengurutan hanya berdasarkan relevansi (standar; cocok untuk mengingat secara eksploratif). Gunakan newestuntuk pertanyaan "di mana kita meninggalkan X", oldestuntuk pertanyaan "bagaimana X dimulai".
role_filter— peran yang dipisahkan koma untuk disertakan. Penemuan default ke user,assistant(output alat biasanya berupa gangguan). Lewatkan user,assistant,tooluntuk menyertakan output alat (perilaku alat debugging) atau tooluntuk hanya mencari output alat.
Saat Digunakan
Agen tersebut diminta untuk menggunakan pencarian sesi secara otomatis:

"Ketika pengguna merujuk sesuatu dari percakapan sebelumnya atau Anda menduga ada konteks relevan sebelumnya, gunakan session_search untuk mengingatnya sebelum meminta mereka mengulanginya."

Pemicu umum: "kita pernah melakukan ini sebelumnya", "ingatkah saat itu", "terakhir kali", "seperti yang sudah saya sebutkan", atau referensi apa pun ke proyek/orang/konsep yang tidak ada di jendela saat ini.

Pelacakan Sesi Per Platform
Sesi Gerbang
Pada platform perpesanan, sesi ditandai dengan kunci sesi deterministik yang dibangun dari sumber pesan:

Jenis Obrolan	Format Tombol Default	Perilaku
Telegram DM	agent:main:telegram:dm:<chat_id>	Satu sesi per obrolan DM
DM Discord	agent:main:discord:dm:<chat_id>	Satu sesi per obrolan DM
Pesan Langsung WhatsApp	agent:main:whatsapp:dm:<canonical_identifier>	Satu sesi per pengguna DM (LID/alias telepon digabungkan menjadi satu identitas jika pemetaan ada)
Obrolan grup	agent:main:<platform>:group:<chat_id>:<user_id>	Per pengguna di dalam grup ketika platform menampilkan ID pengguna.
Diskusi/topik grup	agent:main:<platform>:group:<chat_id>:<thread_id>	Sesi bersama untuk semua peserta thread (default). Per pengguna dengan thread_sessions_per_user: true.
Saluran	agent:main:<platform>:channel:<chat_id>:<user_id>	Per pengguna di dalam saluran ketika platform mengekspos ID pengguna.
Jika Hermes tidak dapat memperoleh pengidentifikasi peserta untuk obrolan bersama, maka Hermes akan menggunakan satu sesi bersama untuk ruangan tersebut.

Sesi Kelompok Bersama vs Sesi Kelompok Terpisah
Secara default, Hermes menggunakan group_sessions_per_user: true. config.yamlItu artinya:

Alice dan Bob sama-sama dapat berbicara dengan Hermes di saluran Discord yang sama tanpa perlu berbagi riwayat transkrip.
Tugas panjang dan berat yang dilakukan oleh satu pengguna tidak mengganggu jendela konteks pengguna lain.
Penanganan interupsi juga tetap per pengguna karena kunci agen yang berjalan cocok dengan kunci sesi terisolasi.
Jika Anda menginginkan satu "otak ruangan" bersama, atur:

group_sessions_per_user: false

Hal itu mengembalikan grup/saluran ke sesi bersama tunggal per ruangan, yang mempertahankan konteks percakapan bersama tetapi juga berbagi biaya token, status interupsi, dan pertumbuhan konteks.

Kebijakan Reset Sesi
Sesi gateway direset secara otomatis berdasarkan kebijakan yang dapat dikonfigurasi:

tidak aktif — diatur ulang setelah N menit tidak aktif
harian — diatur ulang pada jam tertentu setiap hari
keduanya — direset berdasarkan mana yang terjadi lebih dulu (tidak aktif atau harian)
tidak ada — tidak pernah diatur ulang secara otomatis
Sebelum sesi direset secara otomatis, agen diberi kesempatan untuk menyimpan kenangan atau keterampilan penting dari percakapan tersebut.

Sesi dengan proses latar belakang yang aktif tidak akan pernah direset secara otomatis, terlepas dari kebijakan yang diterapkan.

Lokasi Penyimpanan
Apa	Jalur	Keterangan
Basis data SQLite	~/.hermes/state.db	Semua metadata sesi + pesan dengan FTS5
Pesan gerbang	~/.hermes/state.db	SQLite — penyimpanan kanonik untuk semua pesan sesi.
Indeks perutean gateway	~/.hermes/sessions/sessions.json	Memetakan kunci sesi ke ID sesi aktif (metadata asal, flag kedaluwarsa)
Basis data SQLite menggunakan mode WAL untuk pembaca bersamaan dan penulis tunggal, yang sangat sesuai dengan arsitektur multi-platform gateway.

Transkrip JSONL lama
Sesi yang dibuat sebelum state.db menjadi kanonik mungkin memiliki sisa *.jsonlfile di ~/.hermes/sessions/. File-file tersebut tidak lagi ditulis atau dibaca oleh Hermes. Aman untuk dihapus setelah memverifikasi bahwa sesi yang bersangkutan ada di state.db.

Skema Basis Data
Tabel-tabel utama dalam state.db:

sesi — metadata sesi (id, sumber, user_id, model, judul, stempel waktu, jumlah token). Judul memiliki indeks unik (judul NULL diperbolehkan, hanya yang bukan NULL yang harus unik).
pesan — riwayat pesan lengkap (peran, konten, panggilan alat, nama alat, jumlah token)
messages_fts — Tabel virtual FTS5 untuk pencarian teks lengkap di seluruh konten pesan
Kedaluwarsa Sesi dan Pembersihan
Pembersihan Otomatis
Sesi gateway akan direset secara otomatis berdasarkan kebijakan reset yang telah dikonfigurasi.
Sebelum direset, agen menyimpan memori dan keterampilan dari sesi yang akan berakhir.
Opsi penghapusan otomatis: ketika sessions.auto_prune, truesesi yang telah berakhir dan lebih lama dari sessions.retention_days(default 90) akan dihapus saat CLI/gateway dimulai.
Setelah penghapusan baris yang sebenarnya dilakukan, state.dbdata VACUUMdikirim untuk menghemat ruang disk (SQLite tidak mengecilkan file pada perintah DELETE biasa).
Pemangkasan dijalankan paling banyak sekali per sessions.min_interval_hours(standar 24); stempel waktu eksekusi terakhir dilacak di dalam state.dbdirinya sendiri sehingga dibagikan di setiap proses Hermes yang sama.HERMES_HOME
Secara default, fitur ini dinonaktifkan — riwayat sesi sangat berharga untuk session_searchmengingat kembali informasi, dan menghapusnya secara diam-diam dapat mengejutkan pengguna. Aktifkan di ~/.hermes/config.yaml:

sessions:
  auto_prune: true          # opt in — default is false
  retention_days: 90        # keep ended sessions this many days
  vacuum_after_prune: true  # reclaim disk space after a pruning sweep
  min_interval_hours: 24    # don't re-run the sweep more often than this


Sesi aktif tidak pernah dihapus secara otomatis, terlepas dari usianya.

Pembersihan Manual
# Prune sessions older than 90 days
hermes sessions prune

# Delete a specific session
hermes sessions delete <session_id>

# Export before pruning (backup)
hermes sessions export backup.jsonl
hermes sessions prune --older-than 30 --yes


tip
Basis data tumbuh perlahan (biasanya: 10-15 MB untuk ratusan sesi) dan riwayat sesi mendukung session_searchpemanggilan kembali percakapan masa lalu, sehingga fitur auto-prune dinonaktifkan. Aktifkan fitur ini jika Anda menjalankan beban kerja gateway/cron yang berat yang state.dbsecara signifikan memengaruhi kinerja (mode kegagalan yang diamati: state.db 384 MB dengan ~1000 sesi memperlambat penyisipan dan /resumepencatatan FTS5). Gunakan hermes sessions pruneuntuk pembersihan sekali saja tanpa mengaktifkan pembersihan otomatis.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Profil: Menjalankan Beberapa Agen
Jalankan beberapa agen Hermes independen pada mesin yang sama — masing-masing dengan konfigurasi, kunci API, memori, sesi, keterampilan, dan status gateway sendiri.

Apa itu profil?
Profil adalah direktori utama Hermes yang terpisah. Setiap profil mendapatkan direktorinya sendiri yang berisi memori, sesi, keterampilan, tugas cron, dan basis data statusnya sendiri config.yaml. .envProfil SOUL.mdmemungkinkan Anda menjalankan agen terpisah untuk tujuan yang berbeda — asisten pengkodean, bot pribadi, agen penelitian — tanpa mencampuradukkan status Hermes.

Saat Anda membuat profil, profil tersebut secara otomatis menjadi perintah tersendiri. Buat profil bernama coderdan Anda akan langsung memiliki coder chat, coder setup, coder gateway start, dan seterusnya.

Mulai cepat
hermes profile create coder       # creates profile + "coder" command alias
coder setup                       # configure API keys and model
coder chat                        # start chatting


Selesai. coderSekarang ini memiliki profil Hermes tersendiri dengan konfigurasi, memori, dan statusnya sendiri.

Membuat profil
Profil kosong
hermes profile create mybot

Membuat profil baru dengan keterampilan bawaan. Jalankan mybot setupuntuk mengkonfigurasi kunci API, model, dan token gateway.

Jika Anda berencana menggunakan profil ini sebagai pekerja kanban (atau ingin orchestrator kanban mengarahkan pekerjaan ke profil ini), berikan parameter berikut --description "<role>"saat pembuatan profil agar orchestrator mengetahui kemampuan terbaiknya:

hermes profile create researcher --description "Reads source code and external docs, writes findings."


Anda juga dapat mengatur atau membuat deskripsi secara otomatis nanti hermes profile describe— lihat panduan Kanban untuk model routing lengkapnya.

Hanya klon konfigurasi ( --clone)
hermes profile create work --clone

config.yamlMenyalin , .env, dan profil Anda saat ini SOUL.mdke profil baru. Kunci API dan model yang sama, tetapi sesi dan memori baru. Edit ~/.hermes/profiles/work/.envuntuk kunci API yang berbeda, atau ~/.hermes/profiles/work/SOUL.mduntuk kepribadian yang berbeda.

Gandakan semuanya ( --clone-all)
hermes profile create backup --clone-all


Menyalin semuanya — konfigurasi, kunci API, kepribadian, semua memori, riwayat sesi lengkap, keterampilan, tugas cron, plugin. Sebuah snapshot lengkap. Berguna untuk pencadangan atau membuat salinan agen yang sudah memiliki konteks.

Kloning dari profil tertentu
hermes profile create work --clone --clone-from coder


Memori Honcho + profil
Saat Honcho diaktifkan, --clonesecara otomatis akan membuat rekan AI khusus untuk profil baru sambil berbagi ruang kerja pengguna yang sama. Setiap profil membangun pengamatan dan identitasnya sendiri. Lihat Honcho -- Multi-agen / Profil untuk detailnya.

Menggunakan profil
Alias ​​perintah
Setiap profil secara otomatis mendapatkan alias perintah di ~/.local/bin/<name>:

coder chat                    # chat with the coder agent
coder setup                   # configure coder's settings
coder gateway start           # start coder's gateway
coder doctor                  # check coder's health
coder skills list             # list coder's skills
coder config set model.default anthropic/claude-sonnet-4


Alias ​​tersebut berfungsi dengan setiap subperintah hermes — hanya saja bekerja hermes -p <name>di balik layar.

Bendera-p​
Anda juga dapat menargetkan profil secara eksplisit dengan perintah apa pun:

hermes -p coder chat
hermes --profile=coder doctor
hermes chat -p coder -q "hello"    # works in any position


Tetap default ( hermes profile use)
hermes profile use coder
hermes chat                   # now targets coder
hermes tools                  # configures coder's tools
hermes profile use default    # switch back


Menetapkan nilai default sehingga hermesperintah biasa menargetkan profil tersebut. Seperti kubectl config use-context.

Mengetahui di mana Anda berada
CLI selalu menampilkan profil mana yang aktif:

Perintah : coder ❯sebagai gantinya❯
Banner : Muncul Profile: codersaat startup
hermes profileMenampilkan nama profil, jalur, model, dan status gateway saat ini.
Profil vs ruang kerja vs sandboxing
Profil seringkali disalahartikan dengan ruang kerja atau lingkungan uji coba (sandbox), padahal ketiganya berbeda:

Sebuah profil memberi Hermes direktori statusnya sendiri: config.yaml, .env, SOUL.md, sesi, memori, log, tugas cron, dan status gateway.
Ruang kerja atau direktori kerja adalah tempat perintah terminal dimulai. Hal itu dikendalikan secara terpisah oleh terminal.cwd.
Sandbox adalah yang membatasi akses ke sistem file. Profil tidak membatasi akses agen melalui sandbox.
Pada localbackend terminal default, agen masih memiliki akses sistem file yang sama dengan akun pengguna Anda. Profil tidak mencegahnya mengakses folder di luar direktori profil.

Jika Anda ingin profil dimulai di folder proyek tertentu, tetapkan lokasi absolut secara eksplisit terminal.cwddi dalam file konfigurasi profil tersebut config.yaml.

terminal:
  backend: local
  cwd: /absolute/path/to/project

Menggunakan " cwd: "."on the local backend" berarti "direktori tempat Hermes diluncurkan", bukan "direktori profil".

Juga mencatat:

SOUL.mddapat memandu model, tetapi tidak memberlakukan batasan ruang kerja.
Perubahan akan SOUL.mdberlaku secara otomatis pada sesi baru. Sesi yang sudah ada mungkin masih menggunakan status prompt lama.
Menanyakan kepada model "Anda berada di direktori mana?" bukanlah uji isolasi yang dapat diandalkan. Jika Anda memerlukan direktori awal yang dapat diprediksi untuk alat, atur terminal.cwdsecara eksplisit.
Menjalankan gerbang
Setiap profil menjalankan gateway-nya sendiri sebagai proses terpisah dengan token bot-nya sendiri:

coder gateway start           # starts coder's gateway
assistant gateway start       # starts assistant's gateway (separate process)


Token bot yang berbeda
Setiap profil memiliki file tersendiri .env. Konfigurasikan token bot Telegram/Discord/Slack yang berbeda di setiap profil:

# Edit coder's tokens
nano ~/.hermes/profiles/coder/.env

# Edit assistant's tokens
nano ~/.hermes/profiles/assistant/.env


Keamanan: kunci token
Jika dua profil secara tidak sengaja menggunakan token bot yang sama, gateway kedua akan diblokir dengan pesan kesalahan yang jelas yang menyebutkan profil yang bertentangan. Didukung untuk Telegram, Discord, Slack, WhatsApp, dan Signal.

Layanan berkelanjutan
coder gateway install         # creates hermes-gateway-coder systemd/launchd service
assistant gateway install     # creates hermes-gateway-assistant service


Setiap profil mendapatkan nama layanannya masing-masing. Mereka berjalan secara independen.

Di dalam image Docker resmi
Gateway per-profil diawasi oleh s6-overlay (PID 1 di dalam kontainer), sehingga hermes profile create <name>secara otomatis mendaftarkan slot layanan s6 di /run/service/gateway-<name>/. hermes -p <name> gateway start/stop/restartmengirimkan ke s6-svcalih-alih membuat proses kosong — jika terjadi crash, akan otomatis dimulai ulang dan docker restartmempertahankan kumpulan gateway yang sebelumnya berjalan. Lihat Pengawasan gateway per-profil untuk detailnya.

Mengonfigurasi profil
Setiap profil memiliki ciri khasnya masing-masing:

config.yaml— model, penyedia, perangkat, semua pengaturan
.env— Kunci API, token bot
SOUL.md— kepribadian dan instruksi
coder config set model.default anthropic/claude-sonnet-4
echo "You are a focused coding assistant." > ~/.hermes/profiles/coder/SOUL.md


Jika Anda ingin profil ini berfungsi secara default di proyek tertentu, atur juga pengaturannya sendiri terminal.cwd:

coder config set terminal.cwd /absolute/path/to/project


Memperbarui
hermes updateMengambil kode sekali (bersama) dan menyinkronkan keterampilan baru yang dibundel ke semua profil secara otomatis:

hermes update
# → Code updated (12 commits)
# → Skills synced: default (up to date), coder (+2 new), assistant (+2 new)


Keterampilan yang dimodifikasi pengguna tidak akan pernah ditimpa.

Mengelola profil
hermes profile list           # show all profiles with status
hermes profile show coder     # detailed info for one profile
hermes profile rename coder dev-bot   # rename (updates alias + service)
hermes profile export coder   # export to coder.tar.gz
hermes profile import coder.tar.gz   # import from archive


Menghapus profil
hermes profile delete coder

Ini menghentikan gateway, menghapus layanan systemd/launchd, menghapus alias perintah, dan menghapus semua data profil. Anda akan diminta untuk mengetikkan nama profil untuk konfirmasi.

Gunakan ini --yesuntuk melewati konfirmasi:hermes profile delete coder --yes

catatan
Anda tidak dapat menghapus profil default ( ~/.hermes). Untuk menghapus semuanya, gunakan hermes uninstall.

Penyelesaian tab
# Bash
eval "$(hermes completion bash)"

# Zsh
eval "$(hermes completion zsh)"

Tambahkan baris ini ke ~/.bashrcatau ~/.zshrcuntuk penyelesaian otomatis. Melengkapi nama profil setelah -p, subperintah profil, dan perintah tingkat atas.

Cara kerjanya
Profil menggunakan HERMES_HOMEvariabel lingkungan. Saat Anda menjalankan coder chat, skrip pembungkus akan mengatur HERMES_HOME=~/.hermes/profiles/codersebelum meluncurkan hermes. Karena 119+ file dalam basis kode menyelesaikan jalur melalui get_hermes_home(), status Hermes secara otomatis mencakup direktori profil — konfigurasi, sesi, memori, keterampilan, basis data status, PID gateway, log, dan tugas cron.

Ini terpisah dari direktori kerja terminal. Eksekusi alat dimulai dari terminal.cwd(atau direktori peluncuran saat cwd: "."berada di backend lokal), bukan secara otomatis dari HERMES_HOME.

Profil default hanyalah profil itu ~/.hermessendiri. Tidak perlu migrasi — instalasi yang ada berfungsi identik.

Berbagi profil sebagai distribusi
Profil yang Anda buat di satu mesin dapat dikemas sebagai repositori Git dan diinstal dengan satu perintah di mesin lain — workstation Anda sendiri, laptop rekan tim, atau lingkungan pengguna komunitas. Paket bersama tersebut mencakup SOUL, konfigurasi, keterampilan, tugas cron, dan koneksi MCP. Kredensial, memori, dan sesi tetap per mesin.

# Install a whole agent from a git repo
hermes profile install github.com/you/research-bot --alias

# Update later when the author ships a new version (keeps your memories + .env)
hermes profile update research-bot


Lihat Distribusi Profil: Berbagi Seluruh Agen untuk panduan lengkap — pembuatan, penerbitan, semantik pembaruan, model keamanan, dan kasus penggunaan.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Distribusi Profil: Bagikan Seluruh Agen
Distribusi profil mengemas agen Hermes lengkap — kepribadian, keterampilan, tugas cron, koneksi MCP, konfigurasi — sebagai repositori git. Siapa pun yang memiliki akses ke repositori dapat menginstal seluruh agen dengan satu perintah, memperbaruinya di tempat, dan tetap mempertahankan memori, sesi, dan kunci API mereka sendiri tanpa perubahan.

Jika sebuah profil adalah agen lokal, maka distribusi adalah agen tersebut yang dibuat agar dapat dibagikan.

Apa artinya ini?
Sebelum adanya sistem distribusi, berbagi agen Hermes berarti mengirim seseorang:

Jiwamu.md
Daftar keterampilan yang perlu diinstal
File config.yaml Anda, tanpa bagian rahasia.
Deskripsi tentang server MCP mana yang telah Anda hubungkan.
Semua tugas cron yang telah Anda jadwalkan
Petunjuk tentang variabel lingkungan mana yang perlu diatur.
…dan berharap mereka merakitnya dengan benar. Setiap peningkatan versi atau perbaikan bug berarti pengulangan proses serah terima.

Dengan distribusi, semuanya tersimpan dalam satu repositori git:

my-research-agent/
├── distribution.yaml    # manifest: name, version, env-var requirements
├── SOUL.md              # the agent's personality / system prompt
├── config.yaml          # model, temperature, reasoning, tool defaults
├── skills/              # bundled skills that come with the agent
├── cron/                # scheduled tasks the agent runs
└── mcp.json             # MCP servers the agent connects to


Penerima menjalankan:

hermes profile install github.com/you/my-research-agent --alias


…dan sekarang mereka memiliki seluruh agen. Mereka mengisi kunci API mereka sendiri ( .env.EXAMPLE→ .env), dan mereka dapat menjalankan my-research-agent chatatau mengaksesnya melalui Telegram / Discord / Slack / platform gateway apa pun. Saat Anda mengirimkan versi baru, mereka menjalankan hermes profile update my-research-agentdan menarik perubahan Anda — memori dan sesi mereka tetap utuh.

Mengapa Git?
Kami mempertimbangkan tarball, arsip HTTP, dan format khusus. Tak satu pun dari metode tersebut mengalahkan git:

Tidak ada langkah pembuatan sama sekali untuk penulis. Unggah ke GitHub; konsumen menginstal. Tidak ada siklus "kemas ini, unggah itu, perbarui indeks".
Tag, branch, dan commit sudah menjadi sistem kontrol versi. Push tag melakukan hal yang sama untuk kita seperti "pack + upload a release" pada alat lain.
Pembaruan dilakukan dengan mengambil data, bukan mengunduh ulang seluruh arsip.
Transparan. Pengguna dapat menelusuri repositori, membaca perbedaan antar versi, membuka masalah terkait repositori tersebut, dan melakukan fork untuk melakukan kustomisasi.
Repositori pribadi berfungsi secara gratis. Kunci SSH, git credentialhelper, kredensial tersimpan GitHub CLI — apa pun metode otentikasi yang sudah diatur di terminal Anda akan berlaku secara transparan.
Reproduksibilitas adalah SHA commit. Hal yang sama dicatat oleh pip dan npm.
Konsekuensinya: penerima perlu menginstal git. Pada mesin mana pun yang menjalankan Hermes pada tahun 2026, hal itu sudah berlaku.

Kapan Anda harus menggunakan distribusi?
Cocok untuk:

Anda berbagi agen khusus — pemantau kepatuhan, peninjau kode, asisten penelitian, bot dukungan pelanggan — dengan tim atau komunitas.
Anda menyebarkan agen yang sama ke beberapa mesin dan tidak ingin menyalin file secara manual setiap kali.
Anda sedang melakukan iterasi pada sebuah agen dan ingin agar penerima dapat mengambil versi baru dengan satu perintah.
Anda sedang membangun agen sebagai sebuah produk — pengaturan default yang terarah, keterampilan yang dipilih dengan cermat, dan petunjuk yang disesuaikan — yang seharusnya digunakan orang lain sebagai titik awal.
Tidak cocok:

Anda hanya ingin mencadangkan profil di komputer Anda sendiri. Gunakan hermes profile export/import — itulah gunanya.
Anda ingin berbagi kunci API bersama dengan agen, auth.json dan .envsengaja dikecualikan dari distribusi. Setiap penginstal membawa kredensialnya sendiri.
Anda ingin berbagi kenangan/sesi/riwayat percakapan. Itu adalah data pengguna, bukan konten distribusi. Tidak pernah dikirim.
Siklus hidup: penulis ke penginstal ke pembaruan
Berikut adalah alur lengkap dari awal hingga akhir. Pilih sisi yang Anda minati.

Untuk penulis: menerbitkan distribusi
Langkah 1 — Mulai dari profil yang berfungsi
Bangun dan sempurnakan agen seperti halnya profil lainnya:

hermes profile create research-bot
research-bot setup                    # configure model, API keys
# Edit ~/.hermes/profiles/research-bot/SOUL.md
# Install skills, wire up MCP servers, schedule cron jobs, etc.
research-bot chat                     # dogfood until it feels right


Langkah 2 — Tambahkandistribution.yaml
Membuat ~/.hermes/profiles/research-bot/distribution.yaml:

name: research-bot
version: 1.0.0
description: "Autonomous research assistant with arXiv and web tools"
hermes_requires: ">=0.12.0"
author: "Your Name"
license: "MIT"

# Tell installers which env vars the agent needs. These are checked against
# the installer's shell and existing .env file so they don't get nagged
# about keys they already have configured.
env_requires:
  - name: OPENAI_API_KEY
    description: "OpenAI API key (for model access)"
    required: true
  - name: SERPAPI_KEY
    description: "SerpAPI key for web search"
    required: false
    default: ""


Itulah keseluruhan manifesnya. Setiap kolom kecuali namememiliki nilai default yang masuk akal.

Langkah 3 — Dorong ke repositori git
cd ~/.hermes/profiles/research-bot
git init
git add .
git commit -m "v1.0.0"
git remote add origin git@github.com:you/research-bot.git
git tag v1.0.0
git push -u origin main --tags


Repositori ini sekarang menjadi distribusi. Siapa pun yang memiliki akses dapat menginstalnya.

catatan
Repositori Git berisi semua yang ada di direktori profil kecuali hal-hal yang sudah dikecualikan dari distribusi : auth.json, .env, memories/, sessions/, state.db*, logs/, workspace/, *_cache/, local/. Hal-hal tersebut tetap berada di mesin Anda. Anda juga dapat menambahkan .gitignorejika ingin mengecualikan jalur tambahan.

Langkah 4 — Beri tag pada rilis yang memiliki versi
Setiap kali agen mencapai titik stabil, naikkan versi dan tag-nya:

# Edit distribution.yaml: version: 1.1.0
git add distribution.yaml SOUL.md skills/
git commit -m "v1.1.0: tighter research SOUL, add arxiv skill"
git tag v1.1.0
git push --tags


Penerima yang menjalankan program hermes profile update research-botakan mendapatkan informasi terbaru.

Beginilah tampilan repositori tersebut.
Distribusi lengkap yang dibuat oleh penulis:

research-bot/
├── distribution.yaml            # required
├── SOUL.md                      # strongly recommended
├── config.yaml                  # model, provider, tool defaults
├── mcp.json                     # MCP server connections
├── skills/
│   ├── arxiv-search/SKILL.md
│   ├── paper-summarization/SKILL.md
│   └── citation-lookup/SKILL.md
├── cron/
│   └── weekly-digest.json       # scheduled tasks
└── README.md                    # human-facing description (optional)


Dimiliki oleh distributor vs dimiliki oleh pengguna
Saat program instalasi diperbarui ke versi baru, beberapa hal akan diganti (domain penulis) dan beberapa hal tetap sama (domain program instalasi). Pengaturan default:

Kategori	Jalan setapak	Sedang diperbarui
Dimiliki oleh distributor	SOUL.md, config.yaml, mcp.json, skills/, cron/,distribution.yaml	Digantikan dari klon baru
Penggantian konfigurasi	config.yaml	Sebenarnya dipertahankan secara default — penginstal mungkin telah menyesuaikan model atau penyedia. Lewatkan --force-configpembaruan untuk mengatur ulang.
Dimiliki oleh pengguna	memories/, sessions/, state.db*, auth.json, .env, logs/, workspace/, plans/, home/, *_cache/,local/	Tidak pernah disentuh
Anda dapat menimpa daftar yang dimiliki distribusi di manifes:

distribution_owned:
  - SOUL.md
  - skills/research/            # only my research skills; other installed skills stay
  - cron/digest.json


Jika dihilangkan, pengaturan default di atas akan berlaku — yang memang diinginkan oleh sebagian besar distribusi.

Untuk penginstal: menggunakan distribusi
Memasang
hermes profile install github.com/you/research-bot --alias


Yang terjadi:

Mengkloning repositori ke direktori sementara.
Membaca distribution.yaml, menampilkan manifes (nama, versi, deskripsi, penulis, variabel lingkungan yang dibutuhkan).
Memeriksa setiap variabel lingkungan yang dibutuhkan terhadap lingkungan shell Anda dan profil target yang sudah ada .env. Menandai setiap variabel sebagai "berhasil" ✓ setatau "gagal needs setting" sehingga Anda tahu persis apa yang perlu dikonfigurasi.
Meminta konfirmasi. Lewati -y/ --yesdilewati.
Menyalin file milik distribusi ke ~/.hermes/profiles/research-bot/(atau ke mana pun manifest namemengarah).
Menulis .env.EXAMPLEdengan kunci yang diperlukan dikomentari — salin ke .envdan isi.
Dengan --alias, akan dibuat sebuah pembungkus sehingga Anda dapat menjalankannya research-bot chatsecara langsung.
Jenis sumber
URL Git apa pun bisa digunakan:

# GitHub shorthand
hermes profile install github.com/you/research-bot

# Full HTTPS
hermes profile install https://github.com/you/research-bot.git

# SSH
hermes profile install git@github.com:you/research-bot.git

# Self-hosted, GitLab, Gitea, Forgejo — any Git host
hermes profile install https://git.example.com/team/research-bot.git

# Private repo using your configured git auth
hermes profile install git@github.com:your-org/internal-bot.git

# Local directory during development (no git push needed)
hermes profile install ~/my-profile-in-progress/


Ganti nama profil
Dua pengguna menginginkan distribusi yang sama dengan nama profil yang berbeda:

# Alice
hermes profile install github.com/acme/support-bot --name support-us --alias
# Bob (same distribution, different local name)
hermes profile install github.com/acme/support-bot --name support-eu --alias


Isi variabel lingkungan
Setelah instalasi, profil agen berisi .env.EXAMPLE:

# Environment variables required by this Hermes distribution.
# Copy to `.env` and fill in your own values before running.

# OpenAI API key (for model access)
# (required)
OPENAI_API_KEY=

# SerpAPI key for web search
# (optional)
# SERPAPI_KEY=


Salin ini:

cp ~/.hermes/profiles/research-bot/.env.EXAMPLE ~/.hermes/profiles/research-bot/.env
# Edit .env, paste your real keys


Kunci yang diperlukan yang sudah ada di lingkungan shell Anda (misalnya OPENAI_API_KEYdiekspor di ~/.zshrc) akan ditandai ✓ setselama instalasi — Anda tidak perlu menduplikasi kunci tersebut di .env.

Periksa apa yang telah Anda instal.
hermes profile info research-bot

Pertunjukan:

Distribution: research-bot
Version:      1.0.0
Description:  Autonomous research assistant with arXiv and web tools
Author:       Your Name
Requires:     Hermes >=0.12.0
Source:       https://github.com/you/research-bot
Installed:    2026-05-08T17:04:32+00:00

Environment variables:
  OPENAI_API_KEY (required) — OpenAI API key (for model access)
  SERPAPI_KEY (optional) — SerpAPI key for web search


hermes profile listSelain itu, juga menampilkan Distributionkolom sehingga Anda dapat melihat sekilas profil mana yang berasal dari repositori dan mana yang Anda buat sendiri:

 Profile          Model                        Gateway      Alias        Distribution
 ───────────────    ───────────────────────────    ───────────    ───────────    ────────────────────
 ◆default         claude-sonnet-4              stopped      —            —
  coder           gpt-5                        stopped      coder        —
  research-bot    claude-opus-4                stopped      research-bot research-bot@1.0.0
  telemetry       claude-sonnet-4              running      telemetry    telemetry@2.3.1


Memperbarui
hermes profile update research-bot

Yang terjadi:

Mengkloning ulang repositori dari URL sumber yang tercatat.
Menggantikan file milik distribusi (SOUL, skills, cron, mcp.json).
Mempertahankan pengaturan Anda config.yaml— Anda mungkin telah menyetel model, suhu, atau pengaturan lainnya. Lewatkan --force-configuntuk menimpa.
Tidak pernah menyentuh data pengguna: memori, sesi, otentikasi .env, log, status.
Tidak perlu mengunduh ulang seluruh arsip. Tidak perlu menimpa perubahan konfigurasi lokal Anda. Tidak perlu menghapus riwayat percakapan Anda.

Menghapus
hermes profile delete research-bot

Perintah penghapusan menampilkan informasi distribusi sebelum meminta Anda untuk mengkonfirmasi:

Profile: research-bot
Path:    ~/.hermes/profiles/research-bot
Model:   claude-opus-4 (anthropic)
Skills:  12
Distribution: research-bot@1.0.0
Installed from: https://github.com/you/research-bot

This will permanently delete:
  • All config, API keys, memories, sessions, skills, cron jobs
  • Command alias (~/.local/bin/research-bot)

Type 'research-bot' to confirm:


Dengan demikian, Anda tidak akan pernah secara tidak sengaja menghapus agen tanpa mengetahui dari mana asalnya atau tanpa dapat menginstalnya kembali.

Kasus penggunaan dan pola
Personal: sinkronkan satu agen di seluruh mesin.
Anda telah membuat asisten riset di laptop Anda. Anda menginginkan agen yang sama di workstation Anda.

# Laptop
cd ~/.hermes/profiles/research-bot
git init && git add . && git commit -m "initial"
git remote add origin git@github.com:you/research-bot.git
git push -u origin main

# Workstation
hermes profile install github.com/you/research-bot --alias
# Fill in .env. Done.


Setiap iterasi pada laptop ( git commit && push) ditarik ke workstation dengan hermes profile update research-bot. Memori tetap per mesin — laptop mengingat percakapannya sendiri, workstation mengingat percakapannya sendiri, keduanya tidak bertabrakan.

Tim: kirim agen internal yang telah ditinjau.
Tim teknik Anda menginginkan bot peninjau PR bersama dengan SOUL khusus, keterampilan khusus, dan cron yang menjalankan setiap PR melaluinya.

# Engineering lead
cd ~/.hermes/profiles/pr-reviewer
# ... build and tune ...
git init && git add . && git commit -m "v1.0 PR reviewer"
git tag v1.0.0
git push -u origin main --tags    # push to your company's internal Git host

# Each engineer
hermes profile install git@github.com:your-org/pr-reviewer.git --alias
# Fill in .env with their own API key (billed to them), .env.EXAMPLE points at what's required
pr-reviewer chat


Ketika versi 1.1 (SOUL yang lebih baik, skill baru) dirilis, para insinyur langsung bergegas hermes profile update pr-reviewerdan semua orang beralih ke versi baru dalam hitungan menit.

Komunitas: publikasikan agen publik
Anda telah membangun sesuatu yang baru — mungkin "pedagang Polymarket" atau "peringkas makalah akademis" atau "asisten operasi server Minecraft." Anda ingin membagikannya.

# You
cd ~/.hermes/profiles/polymarket-trader
# Write a solid README.md at the repo root — GitHub shows it on the repo page
git init && git add . && git commit -m "v1.0"
git tag v1.0.0
# Publish to a public GitHub repo
git remote add origin https://github.com/you/hermes-polymarket-trader.git
git push -u origin main --tags

# Anyone
hermes profile install github.com/you/hermes-polymarket-trader --alias


Tweet perintah instalasinya. Orang-orang yang mencobanya akan mengirimkan masalah dan permintaan pull (PR) kepada Anda. Jika seseorang ingin menyesuaikannya, mereka akan melakukan fork — alur kerja git yang sama seperti yang sudah diketahui semua orang.

Produk: kirim agen yang punya pendapat kuat.
Anda membangun Hermes di atasnya — mungkin sebuah sistem pemantauan kepatuhan, tumpukan dukungan pelanggan, atau platform riset khusus domain. Anda ingin mendistribusikannya sebagai sebuah produk.

# distribution.yaml
name: telemetry-harness
version: 2.3.1
description: "Compliance telemetry harness — monitors and reviews regulated workflows"
hermes_requires: ">=0.13.0"
author: "Acme Compliance Inc."
license: "Commercial"

env_requires:
  - name: ACME_API_KEY
    description: "Your Acme Compliance license key (email support@acme.com)"
    required: true
  - name: OPENAI_API_KEY
    description: "OpenAI API key for model access"
    required: true
  - name: GRAPHITI_MCP_URL
    description: "URL for your Graphiti knowledge graph instance"
    required: false
    default: "http://127.0.0.1:8000/sse"


Pelanggan Anda menginstal melalui satu perintah; pratinjau instalasi memberi tahu mereka persis kunci mana yang perlu disiapkan; pembaruan diluncurkan saat Anda menandai rilis baru; data kepatuhan mereka ( memories/, sessions/) tidak pernah meninggalkan mesin mereka.

Ephemeral: skrip sekali pakai pada infrastruktur bersama
Anda adalah pemimpin operasional. Anda menginginkan agen sementara yang mendiagnosis insiden produksi — sebuah SOUL siap pakai dengan alat yang tepat dan koneksi MCP — dan berjalan di laptop tiga insinyur siaga selama seminggu ke depan.

# You
# Build the profile, commit, push a private repo
git push -u origin main

# Each on-call
hermes profile install git@github.com:your-org/incident-2026-q2.git --alias

# Incident resolved — tear it down
hermes profile delete incident-2026-q2


Siklus instal-hapus cukup murah sehingga bisa dibuang begitu saja.

Resep
Sematkan ke versi tertentu
catatan
Git ref pinning ( #v1.2.0) direncanakan tetapi tidak termasuk dalam rilis awal — instalasi saat ini melacak cabang default. Lacak versi terinstal Anda melalui hermes profile info <name>dan tunda pembaruan hingga Anda siap.

Periksa versi yang Anda gunakan dibandingkan dengan versi terbaru.
# Your installed version
hermes profile info research-bot | grep Version

# Latest upstream (without installing)
git ls-remote --tags https://github.com/you/research-bot | tail -5


Pertahankan penyesuaian konfigurasi lokal melalui pembaruan.
Perilaku pembaruan default sudah melakukan ini: config.yamlakan dipertahankan. Untuk berjaga-jaga, simpan perubahan lokal Anda ke file yang bukan milik distribusi:

# ~/.hermes/profiles/research-bot/local/my-overrides.yaml
# (distribution never touches local/)


…dan merujuknya dari config.yamlJIWA Anda sesuai kebutuhan.

Paksa instal ulang bersih.
# Nuke and re-install from scratch (loses memories/sessions too)
hermes profile delete research-bot --yes
hermes profile install github.com/you/research-bot --alias

# Update to current main but reset config.yaml to the distribution's default
hermes profile update research-bot --force-config --yes


Buat salinan dan sesuaikan
Alur kerja Git standar — distribusi hanyalah repositori:

# Fork the repo on GitHub, then install your fork
hermes profile install github.com/yourname/forked-research-bot --alias

# Iterate locally in ~/.hermes/profiles/forked-research-bot/
# Edit SOUL.md, commit, push to your fork
# Upstream changes: pull them into your fork the usual way


Uji distribusi sebelum melakukan push.
Dari komputer penulis:

# Install from a local directory (no git push needed)
hermes profile install ~/.hermes/profiles/research-bot --name research-bot-test --alias

# Tweak, delete, re-install until it's right
hermes profile delete research-bot-test --yes
hermes profile install ~/.hermes/profiles/research-bot --name research-bot-test


Apa yang TIDAK ada dalam distribusi (selamanya)
Program penginstal secara otomatis mengecualikan jalur-jalur ini bahkan jika penulis secara tidak sengaja menyertakannya. Tidak ada opsi konfigurasi yang memungkinkan Anda untuk mengesampingkan hal ini — pengaman ini merupakan invarian yang telah diuji regresi:

auth.json— Token OAuth, kredensial platform
.env— Kunci API, rahasia
memories/— memori percakapan
sessions/— riwayat percakapan
state.db, state.db-shm, state.db-wal— metadata sesi
logs/— log agen dan kesalahan
workspace/— menghasilkan file kerja
plans/— rencana awal
home/— pemasangan beranda pengguna di backend Docker
*_cache/— cache gambar / audio / dokumen
local/— ruang nama kustomisasi yang dicadangkan pengguna
Saat Anda mengkloning distribusi, data ini tidak ada. Saat Anda memperbarui, data tersebut tetap ada. Jika Anda menginstal distribusi yang sama pada lima mesin, Anda memiliki lima set data yang terisolasi — satu per mesin.

Keamanan dan kepercayaan
Distribusi profil secara default tidak ditandatangani. Anda mempercayai:

Penyedia layanan Git (GitHub / GitLab / di mana pun) untuk menyajikan byte yang diunggah oleh penulis.
Penulis tidak akan mengirimkan SOUL, skill, atau cron job yang berbahaya.
Tugas Cron dari distribusi tidak dijadwalkan secara otomatis — penginstal mencetak hermes -p <name> cron listdan Anda mengaktifkannya secara eksplisit. SOUL.md dan keterampilan AKTIF segera setelah Anda mulai mengobrol dengan profil, jadi bacalah sebelum menjalankan instalasi pertama kali jika Anda menginstal dari seseorang yang tidak Anda kenal.

Analogi sederhana: menginstal distribusi itu seperti menginstal ekstensi browser atau ekstensi VS Code. Mudah digunakan, performa tinggi, percayai sumbernya. Untuk distribusi internal perusahaan, gunakan repositori pribadi dan otentikasi git standar Anda — tidak ada yang perlu dikonfigurasi ulang.

Versi mendatang mungkin akan menambahkan penandatanganan, file kunci (lockfile .distribution-lock.yaml) dengan SHA commit yang telah diselesaikan, dan sebuah --dry-runflag yang mencetak perbedaan sebelum menerapkan pembaruan. Namun, fitur-fitur tersebut belum dirilis.

Di balik kap mesin
Untuk detail implementasi, perilaku CLI yang tepat, dan semua flag, lihat referensi Perintah Profil .

Versi singkatnya:

install, update, infoberada di dalam hermes profile— bukan di pohon perintah paralel.
Format manifesnya adalah YAML dengan skema yang sangat kecil ( namehanya).
Program penginstal menggunakan gitbiner lokal Anda untuk kloning, sehingga otentikasi apa pun yang sudah ditangani oleh shell Anda (kunci SSH, pembantu kredensial) berfungsi secara transparan.
Setelah dikloning, .git/profil yang diinstal akan dihapus — profil yang diinstal itu sendiri bukanlah hasil git checkout, sehingga menghindari .envjebakan "oh, saya tidak sengaja melakukan commit ke riwayat git distribusi".
Nama profil yang dicadangkan ( hermes, test, tmp, root, sudo) ditolak pada saat instalasi untuk menghindari bent bentrokan dengan biner umum.
Lihat juga
Profil: Menjalankan Banyak Agen — konsep dasarnya
Referensi Perintah Profil — setiap flag, setiap opsi
hermes profile export/import — pencadangan/pemulihan lokal (bukan distribusi)
Menggunakan SOUL bersama Hermes — kepribadian penulis
Kepribadian & JIWA — bagaimana JIWA berperan dalam diri seorang agen
Katalog keterampilan — keterampilan yang dapat Anda gabungkan
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Pohon Kerja Git
Hermes Agent sering digunakan pada repositori besar dan berumur panjang. Saat Anda ingin:

Jalankan beberapa agen secara paralel pada proyek yang sama, atau
Pisahkan refactoring eksperimental dari cabang utama Anda,
Git worktree adalah cara teraman untuk memberikan setiap agen checkout-nya sendiri tanpa menduplikasi seluruh repositori.

Halaman ini menunjukkan cara menggabungkan worktree dengan Hermes sehingga setiap sesi memiliki direktori kerja yang bersih dan terisolasi.

Mengapa Menggunakan Worktree dengan Hermes?
Hermes memperlakukan direktori kerja saat ini sebagai akar proyek:

CLI: direktori tempat Anda menjalankan hermesatauhermes chat
Gerbang pesan: direktori yang ditetapkan olehMESSAGING_CWD
Jika Anda menjalankan beberapa agen dalam checkout yang sama , perubahan yang mereka lakukan dapat saling mengganggu:

Salah satu agen dapat menghapus atau menimpa file yang sedang digunakan oleh agen lainnya.
Hal ini mempersulit untuk memahami perubahan mana yang termasuk dalam eksperimen mana.
Dengan worktree, setiap agen mendapatkan:

Cabang dan direktori kerjanya sendiri
Riwayat Checkpoint Manager -nya sendiri untuk/rollback
Lihat juga: Checkpoint dan /rollback .

Panduan Singkat: Membuat Worktree
Dari repositori utama Anda (yang berisi .git/), buat worktree baru untuk cabang fitur:

# From the main repo root
cd /path/to/your/repo

# Create a new branch and worktree in ../repo-feature
git worktree add ../repo-feature feature/hermes-experiment


Hal ini menghasilkan:

Direktori baru:../repo-feature
Cabang baru: feature/hermes-experimenttelah di-checkout di direktori tersebut.
Sekarang Anda dapat cdmasuk ke worktree baru dan menjalankan Hermes di sana:

cd ../repo-feature

# Start Hermes in the worktree
hermes

Hermes akan:

Lihat ../repo-featuresebagai akar proyek.
Gunakan direktori tersebut untuk file konteks, pengeditan kode, dan alat-alat.
Gunakan riwayat checkpoint terpisah untuk /rollbacklingkup worktree ini.
Menjalankan Beberapa Agen Secara Paralel
Anda dapat membuat beberapa worktree, masing-masing dengan cabangnya sendiri:

cd /path/to/your/repo

git worktree add ../repo-experiment-a feature/hermes-a
git worktree add ../repo-experiment-b feature/hermes-b


Di terminal terpisah:

# Terminal 1
cd ../repo-experiment-a
hermes

# Terminal 2
cd ../repo-experiment-b
hermes

Setiap proses Hermes:

Bekerja pada cabangnya sendiri ( feature/hermes-avs feature/hermes-b).
Menulis checkpoint di bawah hash shadow repo yang berbeda (diperoleh dari jalur worktree).
Dapat digunakan /rollbacksecara independen tanpa memengaruhi yang lain.
Hal ini sangat berguna terutama ketika:

Menjalankan refaktorisasi secara batch.
Mencoba berbagai pendekatan untuk tugas yang sama.
Memasangkan sesi CLI + gateway terhadap repositori upstream yang sama.
Membersihkan Area Kerja dengan Aman
Setelah Anda selesai melakukan percobaan:

Putuskan apakah akan menyimpan atau membuang karya tersebut.
Jika Anda ingin menyimpannya:
Gabungkan cabang tersebut ke cabang utama Anda seperti biasa.
Hapus worktree:
cd /path/to/your/repo

# Remove the worktree directory and its reference
git worktree remove ../repo-feature


Catatan:

git worktree removeakan menolak untuk menghapus worktree dengan perubahan yang belum di-commit kecuali Anda memaksanya.
Menghapus worktree tidak secara otomatis menghapus branch; Anda dapat menghapus atau mempertahankan branch menggunakan git branchperintah biasa.
Data checkpoint Hermes di bawah ini ~/.hermes/checkpoints/tidak secara otomatis dipangkas saat Anda menghapus worktree, tetapi biasanya ukurannya sangat kecil.
Praktik Terbaik
Satu pohon kerja per eksperimen Hermes
Buat cabang/pohon kerja khusus untuk setiap perubahan substansial.
Hal ini menjaga agar perbedaan tetap terfokus dan permintaan perubahan (PR) berukuran kecil dan mudah ditinjau.
Beri nama cabang-cabang tersebut sesuai dengan nama percobaan.
misalnya feature/hermes-checkpoints-docs, feature/hermes-refactor-tests.
Berkomitmenlah secara sering
Gunakan commit Git untuk pencapaian tingkat tinggi.
Gunakan checkpoint dan /rollback sebagai jaring pengaman untuk pengeditan yang dilakukan menggunakan alat di antara proses.
Hindari menjalankan Hermes dari root repositori kosong saat menggunakan worktree.
Lebih baik menggunakan direktori worktree, agar setiap agen memiliki cakupan yang jelas.
Menggunakan hermes -w(Mode Worktree Otomatis)
Hermes memiliki flag bawaan -wyang secara otomatis membuat worktree git sekali pakai dengan branch-nya sendiri. Anda tidak perlu menyiapkan worktree secara manual — cukup cdmasuk ke repo Anda dan jalankan:

cd /path/to/your/repo
hermes -w

Hermes akan:

Buat worktree sementara di .worktrees/dalam repositori Anda.
Periksa cabang yang terisolasi (misalnya hermes/hermes-<hash>).
Jalankan sesi CLI lengkap di dalam worktree tersebut.
Ini adalah cara termudah untuk mendapatkan isolasi worktree. Anda juga dapat menggabungkannya dengan satu kueri:

hermes -w -q "Fix issue #123"

Untuk agen paralel, buka beberapa terminal dan jalankan hermes -wdi masing-masing terminal — setiap pemanggilan akan mendapatkan worktree dan branch-nya sendiri secara otomatis.

Menyatukan Semuanya
Gunakan git worktrees untuk memberikan setiap sesi Hermes checkout bersihnya sendiri.
Gunakan cabang untuk mencatat riwayat eksperimen Anda secara garis besar.
Gunakan checkpoint +/rollback untuk memulihkan kesalahan di dalam setiap worktree.
Kombinasi ini memberi Anda:

Jaminan kuat bahwa berbagai agen dan eksperimen tidak saling tumpang tindih.
Siklus iterasi cepat dengan pemulihan mudah dari kesalahan pengeditan.
Permintaan perubahan kode (pull request) yang bersih dan dapat ditinjau.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Agen Hermes — Docker
Ada dua cara berbeda Docker berinteraksi dengan Hermes Agent:

Menjalankan Hermes DI dalam Docker — agen itu sendiri berjalan di dalam kontainer (fokus utama halaman ini)
Docker sebagai backend terminal — agen berjalan di host Anda tetapi mengeksekusi setiap perintah di dalam satu kontainer sandbox Docker yang persisten dan tetap ada di seluruh panggilan alat, /newdan subagen selama masa proses Hermes (lihat Konfigurasi → Backend Docker ).
Halaman ini membahas opsi 1. Kontainer menyimpan semua data pengguna (konfigurasi, kunci API, sesi, keterampilan, memori) dalam satu direktori yang dipasang dari host di /opt/data. Citra itu sendiri bersifat stateless dan dapat ditingkatkan dengan menarik versi baru tanpa kehilangan konfigurasi apa pun.

Mulai cepat
Jika ini pertama kalinya Anda menjalankan Hermes Agent, buat direktori data di host dan jalankan kontainer secara interaktif untuk menjalankan wizard pengaturan:

mkdir -p ~/.hermes
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent setup

Ini akan membawa Anda ke wizard pengaturan, yang akan meminta kunci API Anda dan menuliskannya ke ~/.hermes/.env. Anda hanya perlu melakukan ini sekali. Sangat disarankan untuk menyiapkan sistem obrolan agar gateway dapat berfungsi pada tahap ini.

Berjalan dalam mode gateway
Setelah dikonfigurasi, jalankan kontainer di latar belakang sebagai gateway permanen (Telegram, Discord, Slack, WhatsApp, dll.):

docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run


Port 8642 mengekspos server API yang kompatibel dengan OpenAI dan endpoint kesehatan gateway . Ini opsional jika Anda hanya menggunakan platform obrolan (Telegram, Discord, dll.), tetapi wajib jika Anda ingin dasbor atau alat eksternal mengakses gateway.

Catatan: server API dibatasi pada API_SERVER_ENABLED=true. Untuk mengeksposnya di luar 127.0.0.1kontainer, atur juga API_SERVER_HOST=0.0.0.0dan API_SERVER_KEY(minimal 8 karakter — buat satu dengan openssl rand -hex 32). Contoh:

docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  -e API_SERVER_ENABLED=true \
  -e API_SERVER_HOST=0.0.0.0 \
  -e API_SERVER_KEY="$(openssl rand -hex 32)" \
  -e API_SERVER_CORS_ORIGINS='*' \
  nousresearch/hermes-agent gateway run


Membuka port apa pun pada mesin yang terhubung ke internet merupakan risiko keamanan. Anda tidak boleh melakukannya kecuali Anda memahami risikonya.

Menjalankan dasbor
Dasbor web bawaan berjalan sebagai proses sampingan opsional di dalam kontainer yang sama dengan gateway. Diatur HERMES_DASHBOARD=1untuk menjalankan dasbor pada loopback kontainer ( 127.0.0.1) secara default:

docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent gateway run


Titik masuk (entrypoint) dimulai hermes dashboarddi latar belakang (berjalan sebagai pengguna non-root hermes) sebelum execmenjalankan perintah utama. Output dasbor diawali dengan [dashboard]awalan "in" docker logssehingga mudah dipisahkan dari log gateway.

Variabel lingkungan	Keterangan	Bawaan
HERMES_DASHBOARD	Atur ke 1(atau true/ yes) untuk meluncurkan dasbor bersamaan dengan perintah utama.	(tidak diatur — dasbor belum dimulai)
HERMES_DASHBOARD_HOST	Alamat pengikatan untuk server HTTP dasbor	127.0.0.1
HERMES_DASHBOARD_PORT	Port untuk server HTTP dasbor	9119
HERMES_DASHBOARD_TUI	Atur agar 1tab Obrolan dalam browser (tertanam hermes --tuimelalui PTY/WebSocket) ditampilkan.	(tidak diatur)
Secara default, dasbor tetap berada dalam mode loopback untuk menghindari tereksposnya antarmuka web yang tidak terautentikasi melalui jaringan. Untuk mempublikasikannya secara sengaja, atur HERMES_DASHBOARD_HOST=0.0.0.0dan konfigurasikan batas jaringan tepercaya/proksi terbalik Anda sendiri. Dalam hal ini, Anda harus secara eksplisit menambahkan --insecureperilaku dengan meneruskan host/flag di jalur perintah Anda (titik masuk tidak lagi secara otomatis mengaktifkan mode tidak aman).

catatan
Dasbor berjalan sebagai layanan s6 yang diawasi di dalam kontainer. Jika proses dasbor mengalami crash, s6-overlay akan memulai ulang secara otomatis setelah penundaan singkat — Anda akan melihat PID baru tanpa perlu memulai ulang kontainer. Log dan output crash dapat dilihat melalui docker logs <container>(s6 meneruskan stdout/stderr layanan ke sana).

Menjalankan dasbor sebagai kontainer terpisah tidak didukung: deteksi keaktifan gateway-nya memerlukan namespace PID bersama dengan proses gateway.

Menjalankan secara interaktif (obrolan CLI)
Untuk membuka sesi obrolan interaktif terhadap direktori data yang sedang berjalan:

docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent

Atau jika Anda sudah membuka terminal di dalam kontainer yang sedang berjalan (misalnya melalui Docker Desktop), cukup jalankan:

/opt/hermes/.venv/bin/hermes

Volume persisten
Volume ini /opt/dataadalah satu-satunya sumber kebenaran untuk semua status Hermes. Volume ini dipetakan ke direktori host Anda ~/.hermes/dan berisi:

Jalur	Isi
.env	Kunci dan rahasia API
config.yaml	Semua konfigurasi Hermes
SOUL.md	Kepribadian/identitas agen
sessions/	Riwayat percakapan
memories/	Penyimpanan memori persisten
skills/	Keterampilan yang terpasang
cron/	Definisi pekerjaan terjadwal
hooks/	Pengait acara
logs/	Log waktu eksekusi
skins/	Tampilan CLI kustom
peringatan
Jangan pernah menjalankan dua kontainer gateway Hermes terhadap direktori data yang sama secara bersamaan — file sesi dan penyimpanan memori tidak dirancang untuk akses tulis bersamaan.

Dukungan multi-profil
Hermes mendukung beberapa profil — ~/.hermes/direktori terpisah yang memungkinkan Anda menjalankan agen independen (SOUL, keterampilan, memori, sesi, kredensial yang berbeda) dari satu instalasi. Saat berjalan di bawah Docker, penggunaan fitur multi-profil bawaan Hermes tidak disarankan.

Sebaliknya, pola yang disarankan adalah satu kontainer per profil , dengan setiap kontainer memasang direktori host-nya sendiri sebagai berikut /opt/data:

# Work profile
docker run -d \
  --name hermes-work \
  --restart unless-stopped \
  -v ~/.hermes-work:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run

# Personal profile
docker run -d \
  --name hermes-personal \
  --restart unless-stopped \
  -v ~/.hermes-personal:/opt/data \
  -p 8643:8642 \
  nousresearch/hermes-agent gateway run


Mengapa kontainer dipisahkan berdasarkan profil di Docker:

Isolasi — setiap kontainer memiliki sistem file, tabel proses, dan batasan sumber daya sendiri. Kerusakan, perubahan dependensi, atau sesi yang tidak terkendali dalam satu profil tidak dapat memengaruhi profil lainnya.
Siklus hidup independen — tingkatkan, mulai ulang, jeda, atau kembalikan setiap agen secara terpisah ( tidak docker restart hermes-workada hermes-personalyang diubah).
Pemisahan port dan jaringan yang bersih — setiap gateway mengikat port host-nya sendiri; tidak ada risiko gangguan silang antara platform obrolan atau server API.
Model mental yang lebih sederhana — kontainer adalah profilnya. Pencadangan, migrasi, dan izin semuanya mengikuti direktori yang dipasang (bind-mounted), tanpa perlu --profilemengingat flag tambahan apa pun.
Menghindari risiko penulisan bersamaan — peringatan di atas tentang tidak pernah menjalankan dua gateway terhadap direktori data yang sama masih berlaku untuk profil dalam satu kontainer.
Dalam Docker Compose, ini hanya berarti mendeklarasikan satu layanan per profil dengan container_name, volumes, dan yang berbeda ports:

services:
  hermes-work:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-work
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.hermes-work:/opt/data

  hermes-personal:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-personal
    restart: unless-stopped
    command: gateway run
    ports:
      - "8643:8642"
    volumes:
      - ~/.hermes-personal:/opt/data


Penerusan variabel lingkungan
Kunci API dibaca dari /opt/data/.envdalam kontainer. Anda juga dapat meneruskan variabel lingkungan secara langsung:

docker run -it --rm \
  -v ~/.hermes:/opt/data \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  -e OPENAI_API_KEY="sk-..." \
  nousresearch/hermes-agent


Flag langsung -emenimpa nilai dari .env. Ini berguna untuk integrasi CI/CD atau pengelola rahasia di mana Anda tidak ingin kunci berada di disk.

Mencari Docker sebagai backend terminal ?
terminalHalaman ini membahas cara menjalankan Hermes itu sendiri di dalam Docker. Jika Anda ingin Hermes mengeksekusi panggilan agen execute_codedi dalam kontainer sandbox Docker (satu kontainer persisten per proses Hermes), itu adalah blok konfigurasi terpisah — terminal.backend: dockerditambah terminal.docker_image, terminal.docker_volumes, terminal.docker_forward_env, terminal.docker_run_as_host_user, dan terminal.docker_extra_args. Lihat Konfigurasi → Backend Docker untuk rangkaian lengkapnya.

Contoh Docker Compose
Untuk penerapan berkelanjutan dengan gateway dan dashboard, cara berikut ini docker-compose.yamlsangat praktis:

services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"   # gateway API
      - "9119:9119"   # dashboard (only reached when HERMES_DASHBOARD=1)
    volumes:
      - ~/.hermes:/opt/data
    environment:
      - HERMES_DASHBOARD=1
      # Uncomment to forward specific env vars instead of using .env file:
      # - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      # - OPENAI_API_KEY=${OPENAI_API_KEY}
      # - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: "2.0"


Mulailah dengan docker compose up -ddan lihat log dengan docker compose logs -f. Output dasbor diawali dengan [dashboard]sehingga mudah untuk memfilter dari log gateway.

Keterbatasan sumber daya
Kontainer Hermes membutuhkan sumber daya dalam jumlah sedang. Rekomendasi minimum:

Sumber	Minimum	Direkomendasikan
Ingatan	1 GB	2–4 GB
CPU	1 inti	2 inti
Disk (volume data)	500 MB	2+ GB (bertambah seiring sesi/keterampilan)
Otomatisasi browser (Playwright/Chromium) adalah fitur yang paling banyak memakan memori. Jika Anda tidak memerlukan alat browser, 1 GB sudah cukup. Dengan alat browser aktif, alokasikan setidaknya 2 GB.

Tetapkan batasan di Docker:

docker run -d \
  --name hermes \
  --restart unless-stopped \
  --memory=4g --cpus=2 \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent gateway run


Fungsi Dockerfile
Gambar resmi ini didasarkan pada debian:13.4dan mencakup:

Python 3 dengan semua dependensi Hermes ( uv pip install -e ".[all]")
Node.js + npm (untuk otomatisasi browser dan jembatan WhatsApp)
Penulis drama dengan Chromium ( npx playwright install --with-deps chromium --only-shell)
ripgrep, ffmpeg, git, dan xz-utilssebagai utilitas sistem
docker-cli— sehingga agen yang berjalan di dalam kontainer dapat mengendalikan daemon Docker host (bind-mount /var/run/docker.sockuntuk mengaktifkannya) untuk docker buildinspeksi docker runkontainer, dll.
openssh-client— mengaktifkan backend terminal SSH dari dalam kontainer. Backend SSH akan menjalankan perintah shell ke sshbinary sistem; tanpa ini, instalasi dalam kontainer akan gagal tanpa pemberitahuan.
Jembatan WhatsApp ( scripts/whatsapp-bridge/)
s6-overlayv3 sebagai PID 1 (menggantikan yang lebih lama tini) — mengawasi dasbor dan gateway per-profil dengan restart otomatis saat terjadi crash, menghentikan subproses zombie, dan meneruskan sinyal.
Kontainer tersebut ENTRYPOINTadalah s6-overlay /init. Saat booting, tampilannya adalah:

Berjalan /etc/cont-init.d/01-hermes-setup(= docker/stage2-hook.sh) sebagai root: pemetaan ulang UID/GID opsional, memperbaiki kepemilikan volume, menambahkan .env/ config.yaml/ SOUL.mdpada boot pertama, menyinkronkan skill yang dibundel.
Menjalankan /etc/cont-init.d/02-reconcile-profiles(= hermes_cli.container_boot): berjalan $HERMES_HOME/profiles/<name>/, membuat ulang slot layanan gateway s6 per-profil di bawah /run/service/gateway-<profile>/, dan secara otomatis memulai hanya layanan yang status terakhirnya tercatat adalah running(lihat Pengawasan gateway per-profil ).
Memulai layanan statis main-hermesdan dashboards6-rc.
Menjalankan perintah CMD kontainer sebagai program utama ( /opt/hermes/docker/main-wrapper.sh), yang mengarahkan argumen yang diberikan pengguna ke docker run:
tanpa argumen → hermes(default)
Argumen pertama adalah file yang dapat dieksekusi di PATH (misalnya sleep, bash) → jalankan langsung
hal lainnya → hermes <args>(penerusan subperintah) Kontainer keluar ketika program utama ini keluar, dengan kode keluarnya.
Perubahan mendasar vs. gambar sebelum season 6
Kontainer ENTRYPOINT sekarang adalah /init(s6-overlay), bukan /usr/bin/tini. Kelima docker runpola pemanggilan yang didokumentasikan (tanpa argumen, chat -q "…", sleep infinity, bash, --tui) berperilaku identik dengan citra berbasis tini. Jika Anda memiliki pembungkus hilir yang bergantung pada perilaku sinyal khusus tini atau /usr/bin/tini --pemanggilan yang dikodekan secara permanen, tetapkan ke tag citra sebelumnya.

Model hak istimewa
Jangan menimpa titik masuk gambar kecuali Anda tetap menggunakan /init(atau, secara setara, shim lama docker/entrypoint.shyang meneruskan ke hook stage2) dalam rantai perintah. s6-overlay /initberjalan sebagai root sehingga dapat mengubah kepemilikan volume pada boot pertama, kemudian beralih ke pengguna hermesmelalui s6-setuidgiduntuk setiap layanan yang diawasi DAN untuk program utama. Memulai hermes gateway runsebagai root di dalam gambar resmi ditolak secara default karena dapat meninggalkan file yang dimiliki root /opt/datadan merusak proses memulai dashboard atau gateway selanjutnya. Atur HERMES_ALLOW_ROOT_GATEWAY=1hanya jika Anda secara sengaja menerima risiko tersebut.

Pengawasan gerbang per profil
Di dalam kontainer, setiap profil yang dibuat secara hermes profile create <name>otomatis mendapatkan layanan gateway yang diawasi oleh s6 yang terdaftar di /run/service/gateway-<name>/. Perintah siklus hidup yang Anda jalankan di host bekerja dengan cara yang sama:

hermes profile create coder            # registers gateway-coder s6 slot
hermes -p coder gateway start          # s6-svc -u  → supervised gateway
hermes -p coder gateway stop           # s6-svc -d  → service down
hermes -p coder gateway restart        # s6-svc -t  → SIGTERM the supervisor
hermes profile delete coder            # tears down the s6 slot


Keunggulan pengawasan dibandingkan citra sebelum S6:

Gateway yang mengalami crash akan otomatis dihidupkan kembali s6-supervisesetelah jeda sekitar 1 detik.
Jika terjadi kerusakan pada dashboard, aplikasi akan otomatis dimulai ulang (diatur HERMES_DASHBOARD=1untuk memulainya).
docker restartMempertahankan gateway yang sedang berjalan: reconciler cont-init membaca $HERMES_HOME/profiles/<name>/gateway_state.jsondan mengaktifkan kembali slot jika status terakhir yang tercatat adalah running. Gateway yang dihentikan tetap dihentikan.
Log gateway per profil tetap tersimpan di bawah $HERMES_HOME/logs/gateways/<profile>/current(dirotasi oleh s6-log), dan tindakan rekonsiliator ditambahkan ke $HERMES_HOME/logs/container-boot.logsetiap kali booting.
hermes statusdi dalam laporan kontainer Manager: s6 (container supervisor). Gunakan /command/s6-svstat /run/service/gateway-<name>untuk tampilan supervisor mentah (catatan: /command/hanya ada di PATH untuk proses pohon pengawasan; berikan jalur absolut saat memanggil dari docker exec).

Perbaikan
Unduh image terbaru dan buat ulang container. Direktori data Anda tidak akan berubah.

docker pull nousresearch/hermes-agent:latest
docker rm -f hermes
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent gateway run


Atau dengan Docker Compose:

docker compose pull
docker compose up -d

Berkas keterampilan dan kredensial
Saat menggunakan Docker sebagai lingkungan eksekusi (bukan metode di atas, tetapi saat agen menjalankan perintah di dalam sandbox Docker — lihat Konfigurasi → Backend Docker ), Hermes menggunakan kembali satu kontainer berumur panjang untuk semua panggilan alat dan secara otomatis memasang direktori keterampilan ( ~/.hermes/skills/) dan file kredensial apa pun yang dideklarasikan oleh keterampilan ke dalam kontainer tersebut sebagai volume hanya baca. Skrip keterampilan, templat, dan referensi tersedia di dalam sandbox tanpa konfigurasi manual, dan karena kontainer bertahan selama masa proses Hermes, dependensi apa pun yang Anda instal atau file yang Anda tulis akan tetap ada untuk panggilan alat berikutnya.

Sinkronisasi yang sama terjadi untuk backend SSH dan Modal — file keterampilan dan kredensial diunggah melalui rsync atau API mount Modal sebelum setiap perintah.

Memasang lebih banyak alat di dalam kontainer.
Citra resmi dilengkapi dengan serangkaian utilitas pilihan (lihat Apa yang dilakukan Dockerfile ), tetapi tidak semua alat yang mungkin dibutuhkan agen sudah terinstal sebelumnya. Ada lima pendekatan yang direkomendasikan, dengan urutan peningkatan upaya dan ketahanan.

npm atau alat Python — gunakan npxatauuvx
Untuk alat apa pun yang diterbitkan ke npm atau PyPI, instruksikan Hermes untuk menjalankannya melalui npx(npm) atau uvx(Python) dan untuk mengingat perintah tersebut dalam memori permanennya. Jika alat tersebut membutuhkan file konfigurasi atau kredensial, instruksikan untuk meletakkannya di bawah /opt/data(misalnya /opt/data/<tool>/config.yaml).

Dependensi diambil sesuai permintaan dan disimpan dalam cache selama masa aktif kontainer. Konfigurasi yang ditulis di bawah ini /opt/datatetap ada setelah kontainer dimulai ulang karena berada di direktori host yang dipasang (bind-mounted). Cache paket itu sendiri dibangun ulang setelah docker rm, tetapi npxdan uvxdiambil ulang secara transparan pada saat alat dijalankan berikutnya.

Alat lainnya (paket apt, biner) — instal dan ingat
Untuk hal-hal di luar npm atau PyPI — aptpaket, biner yang sudah dibuat sebelumnya, runtime bahasa yang belum ada di dalam image — instruksikan Hermes cara menginstalnya (misalnya apt-get update && apt-get install -y <package>) dan beri tahu Hermes untuk mengingat perintah instalasi tersebut. Alat ini akan tetap ada selama masa aktif kontainer, dan Hermes akan menjalankan kembali perintah instalasi setelah kontainer dimulai ulang ketika membutuhkan alat tersebut lagi.

Ini cocok untuk alat yang cepat dipasang dan digunakan sesekali. Untuk alat yang digunakan terus-menerus, lebih baik gunakan pendekatan selanjutnya.

Instalasi yang tahan lama — buat citra turunan.
Jika suatu alat harus tersedia segera pada setiap kali kontainer dijalankan tanpa penundaan instal ulang, buat citra baru yang mewarisi nousresearch/hermes-agentdan menginstal alat tersebut dalam sebuah lapisan:

FROM nousresearch/hermes-agent:latest

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends <your-package> \
    && rm -rf /var/lib/apt/lists/*
USER hermes


Buatlah dan gunakan sebagai pengganti gambar resmi:

docker build -t my-hermes:latest .
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  my-hermes:latest gateway run

Skrip dan /opt/datasemantik titik masuk diwariskan tanpa perubahan, jadi bagian lain dari halaman ini masih berlaku. Ingat untuk membangun ulang citra saat menarik versi upstream yang lebih baru nousresearch/hermes-agent.

Alat yang kompleks atau tumpukan multi-layanan — jalankan kontainer sidecar.
Untuk alat yang membawa layanan sendiri (basis data, server web, antrian, kumpulan browser tanpa antarmuka grafis) atau yang terlalu berat untuk berada di dalam kontainer Hermes, jalankan sebagai kontainer terpisah di jaringan Docker bersama. Hermes mengakses sidecar melalui nama kontainer, dengan cara yang sama seperti mengakses server inferensi lokal (lihat Menghubungkan ke server inferensi lokal ).

services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.hermes:/opt/data
    networks:
      - hermes-net

  my-tool:
    image: example/my-tool:latest
    container_name: my-tool
    restart: unless-stopped
    networks:
      - hermes-net

networks:
  hermes-net:
    driver: bridge


Dari dalam kontainer Hermes, sidecar dapat diakses di http://my-tool:<port>(atau protokol apa pun yang digunakannya). Pola ini menjaga agar siklus hidup, batasan sumber daya, dan ritme peningkatan setiap layanan tetap independen, dan menghindari pembengkakan citra Hermes dengan dependensi yang hanya dibutuhkan oleh satu alat.

Alat yang sangat berguna — buka issue atau pull request.
Jika suatu alat kemungkinan besar akan berguna bagi sebagian besar pengguna Hermes Agent, pertimbangkan untuk menyumbangkannya ke upstream daripada membawanya dalam image turunan pribadi. Buka issue atau pull request di repositori hermes-agent yang menjelaskan alat tersebut dan kasus penggunaannya. Alat yang dibundel ke dalam image resmi akan menguntungkan setiap pengguna dan menghindari biaya pemeliharaan dari fork downstream.

Menghubungkan ke server inferensi lokal (vLLM, Ollama, dll.)
Saat menjalankan Hermes di Docker dan server inferensi Anda (vLLM, Ollama, text-generation-inference, dll.) juga berjalan di host atau di kontainer lain, pengaturan jaringan memerlukan perhatian ekstra.

Docker Compose (direkomendasikan)
Tempatkan kedua layanan tersebut pada jaringan Docker yang sama. Ini adalah pendekatan yang paling andal:

services:
  vllm:
    image: vllm/vllm-openai:latest
    container_name: vllm
    command: >
      --model Qwen/Qwen2.5-7B-Instruct
      --served-model-name my-model
      --host 0.0.0.0
      --port 8000
    ports:
      - "8000:8000"
    networks:
      - hermes-net
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.hermes:/opt/data
    networks:
      - hermes-net

networks:
  hermes-net:
    driver: bridge


Kemudian di file konfigurasi Anda ~/.hermes/config.yaml, gunakan nama kontainer sebagai nama host:

model:
  provider: custom
  model: my-model
  base_url: http://vllm:8000/v1
  api_key: "none"

Poin-poin penting
Gunakan nama kontainer ( vllm) sebagai nama host — bukan localhostatau 127.0.0.1, yang mengacu pada kontainer Hermes itu sendiri.
Nilai tersebut modelharus sesuai dengan nilai --served-model-nameyang Anda berikan ke vLLM.
Atur api_keyke string apa pun yang tidak kosong (vLLM memerlukan header tetapi tidak memvalidasinya secara default).
Jangan menyertakan garis miring di akhir base_url.
Menjalankan Docker secara mandiri (tanpa Compose)
Jika server inferensi Anda berjalan langsung di host (bukan di Docker), gunakan host.docker.internaldi macOS/Windows, atau --network hostdi Linux:

macOS / Windows:

docker run -d \
  --name hermes \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run


# config.yaml
model:
  provider: custom
  model: my-model
  base_url: http://host.docker.internal:8000/v1
  api_key: "none"


Linux (jaringan host):

docker run -d \
  --name hermes \
  --network host \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent gateway run


# config.yaml
model:
  provider: custom
  model: my-model
  base_url: http://127.0.0.1:8000/v1
  api_key: "none"


Dengan opsi ini --network host, -pflag diabaikan — semua port kontainer langsung terekspos pada host.
Memverifikasi konektivitas
Dari dalam kontainer Hermes, pastikan server inferensi dapat dijangkau:

docker exec hermes curl -s http://vllm:8000/v1/models


Anda seharusnya melihat respons JSON yang mencantumkan model yang Anda layani. Jika ini gagal, periksa:

Kedua kontainer berada di jaringan Docker yang sama ( docker network inspect hermes-net)
Server inferensi sedang mendengarkan di 0.0.0.0, bukan .127.0.0.1
Nomor port cocok
Ollama
Ollama bekerja dengan cara yang sama. Jika Ollama berjalan di host, gunakan host.docker.internal:11434(macOS/Windows) atau 127.0.0.1:11434(Linux dengan --network host). Jika Ollama berjalan di dalam kontainernya sendiri di jaringan Docker yang sama:

model:
  provider: custom
  model: llama3
  base_url: http://ollama:11434/v1
  api_key: "none"

Penyelesaian Masalah
Kontainer segera keluar
Periksa log: docker logs hermes. Penyebab umum:

Berkas hilang atau tidak valid .env— jalankan secara interaktif terlebih dahulu untuk menyelesaikan pengaturan.
Terjadi konflik port jika dijalankan dengan port yang terbuka.
Kesalahan "Izin ditolak"
Hook stage2 pada container menurunkan hak akses ke hermespengguna non-root (UID 10000) melalui s6-setuidgidbagian dalam setiap layanan yang diawasi. Jika host Anda ~/.hermes/dimiliki oleh UID yang berbeda, atur HERMES_UID/ HERMES_GIDagar sesuai dengan pengguna host Anda, atau pastikan direktori data dapat ditulis:

chmod -R 755 ~/.hermes

Alat peramban tidak berfungsi
Penulis naskah drama membutuhkan memori bersama. Tambahkan ini --shm-size=1gke perintah Docker run Anda:

docker run -d \
  --name hermes \
  --shm-size=1g \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent gateway run


Gateway tidak terhubung kembali setelah terjadi masalah jaringan.
Flag ini --restart unless-stoppedmenangani sebagian besar kegagalan sementara. Jika gateway macet, mulai ulang kontainer:

docker restart hermes

Memeriksa kondisi kontainer
docker logs --tail 50 hermes          # Recent logs
docker run -it --rm nousresearch/hermes-agent:latest version     # Verify version
docker stats hermes                    # Resource usage
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Keamanan
Hermes Agent dirancang dengan model keamanan berlapis. Halaman ini mencakup setiap batasan keamanan — mulai dari persetujuan perintah hingga isolasi kontainer hingga otorisasi pengguna pada platform perpesanan.

Ringkasan
Model keamanan ini memiliki tujuh lapisan:

Otorisasi pengguna — siapa yang dapat berbicara dengan agen (daftar yang diizinkan, pemasangan DM)
Persetujuan komando yang berbahaya — campur tangan manusia dalam operasi destruktif
Isolasi kontainer — Docker/Singularity/Sandboxing Modal dengan pengaturan yang diperkuat.
Penyaringan kredensial MCP — isolasi variabel lingkungan untuk subproses MCP
Pemindaian berkas konteks — deteksi injeksi prompt dalam berkas proyek
Isolasi lintas sesi — sesi tidak dapat mengakses data atau status satu sama lain; jalur penyimpanan tugas cron diperkuat terhadap serangan path traversal.
Sanitasi input — parameter direktori kerja di backend alat terminal divalidasi terhadap daftar yang diizinkan untuk mencegah injeksi shell.
Persetujuan Perintah Berbahaya
Sebelum menjalankan perintah apa pun, Hermes memeriksanya terhadap daftar pola berbahaya yang telah dikurasi. Jika ditemukan kecocokan, pengguna harus secara eksplisit menyetujuinya.

Mode Persetujuan
Sistem persetujuan mendukung tiga mode, yang dikonfigurasi approvals.modemelalui ~/.hermes/config.yaml:

approvals:
  mode: manual    # manual | smart | off
  timeout: 60     # seconds to wait for user response (default: 60)


Mode	Perilaku
manual (default)	Selalu mintalah persetujuan pengguna untuk perintah berbahaya.
cerdas	Gunakan LLM tambahan untuk menilai risiko. Perintah berisiko rendah (misalnya, python -c "print('hello')") disetujui secara otomatis. Perintah yang benar-benar berbahaya ditolak secara otomatis. Kasus yang tidak pasti akan ditangani secara manual.
mati	Nonaktifkan semua pemeriksaan persetujuan — setara dengan menjalankan dengan --yolo. Semua perintah dieksekusi tanpa permintaan konfirmasi.
peringatan
Pengaturan ini approvals.mode: offmenonaktifkan semua peringatan keamanan. Gunakan hanya di lingkungan tepercaya (CI/CD, kontainer, dll.).

Mode YOLO
Mode YOLO melewati semua permintaan persetujuan perintah berbahaya untuk sesi saat ini. Mode ini dapat diaktifkan dengan tiga cara:

Bendera CLI : Memulai sesi dengan hermes --yoloatauhermes chat --yolo
Perintah slash : Ketik /yoloselama sesi untuk mengaktifkan/menonaktifkannya.
Variabel lingkungan : AturHERMES_YOLO_MODE=1
Perintah ini /yoloadalah sebuah sakelar — setiap penggunaan akan mengaktifkan atau menonaktifkan mode:

> /yolo
  ⚡ YOLO mode ON — all commands auto-approved. Use with caution.

> /yolo
  ⚠ YOLO mode OFF — dangerous commands will require approval.


Mode YOLO tersedia baik dalam sesi CLI maupun gateway. Secara internal, mode ini mengatur HERMES_YOLO_MODEvariabel lingkungan yang diperiksa sebelum setiap eksekusi perintah.

Saat YOLO aktif, Hermes menampilkan dua pengingat visual yang terus-menerus sehingga sulit untuk melupakan bahwa permintaan persetujuan dilewati:

Garis spanduk merah di awal sesi saat YOLO sudah aktif: ⚠ YOLO mode — all approval prompts bypassed. Disembunyikan saat YOLO dimatikan agar spanduk default tetap rapi.
Sebuah ⚠ YOLOfragmen di bilah status di semua tingkatan lebar, diperbarui secara langsung saat Anda mengaktifkan atau menonaktifkan YOLO (renderer teks kaya dan fallback teks biasa).
bahaya
Mode YOLO menonaktifkan semua pemeriksaan keamanan perintah berbahaya untuk sesi tersebut — kecuali daftar blokir yang ketat (lihat di bawah). Gunakan hanya jika Anda sepenuhnya mempercayai perintah yang dihasilkan (misalnya, skrip otomatisasi yang telah diuji dengan baik di lingkungan sekali pakai).

Untuk perintah slash yang merusak sesi ( /clear, /new/ /reset, /undo, /exit --delete), CLI juga meminta konfirmasi sebelum menjalankannya. Lihat Perintah Slash — Permintaan konfirmasi untuk perintah yang merusak .

Daftar Blokir Garis Keras (Lantai Selalu Aktif)
Beberapa perintah sangat merusak — penghapusan sistem file yang tidak dapat dipulihkan, fork bomb, penulisan langsung ke perangkat blok — sehingga Hermes menolak untuk menjalankannya terlepas dari:

--yolo/ /yolodiaktifkan
approvals.mode: off
Tugas Cron berjalan dalam approvemode headless.
Pengguna secara eksplisit mengklik "izinkan selalu"
Daftar blokir adalah lapisan paling bawah --yolo. Daftar ini akan aktif sebelum lapisan persetujuan melihat perintah, dan tidak ada opsi untuk mengesampingkannya. Pola yang saat ini tercakup (tidak lengkap; selalu diperbarui tools/approval.py::UNRECOVERABLE_BLOCKLIST):

Pola	Mengapa ini garis keras?
rm -rf /dan varian yang jelas	Menghapus root sistem file
rm -rf --no-preserve-root /	Varian eksplisit "ya, maksudku akar"
:(){ :|:& };:(bash fork bomb)	Menahan host hingga reboot
mkfs.*pada perangkat root yang terpasang	Memformat sistem langsung
dd if=/dev/zero of=/dev/sd*	Mengosongkan disk fisik
Mengarahkan URL yang tidak tepercaya ke shtingkat teratas rootfs.	Vektor serangan eksekusi kode jarak jauh terlalu luas untuk disetujui.
Jika Anda menemui daftar blokir, panggilan alat akan mengembalikan kesalahan penjelasan ke agen dan tidak ada yang dijalankan. Jika alur kerja yang sah membutuhkan salah satu perintah ini (misalnya, Anda adalah operator dari alur kerja penghapusan dan penginstalan ulang), jalankan di luar agen.

Batas Waktu Persetujuan
Ketika prompt perintah berbahaya muncul, pengguna memiliki waktu yang dapat dikonfigurasi untuk merespons. Jika tidak ada respons yang diberikan dalam batas waktu tersebut, perintah akan ditolak secara default (fail-closed).

Konfigurasikan batas waktu di ~/.hermes/config.yaml:

approvals:
  timeout: 60  # seconds (default: 60)


Apa yang Memicu Persetujuan?
Pola-pola berikut memicu permintaan persetujuan (didefinisikan dalam tools/approval.py):

Pola	Keterangan
rm -r/rm --recursive	Penghapusan rekursif
rm ... /	Hapus di jalur akar
chmod 777/666//o+w​a+w	Izin tulis untuk seluruh dunia/lainnya
chmod --recursivedengan pengeritingan yang tidak aman	Dunia rekursif/dapat ditulis oleh pihak lain (bendera panjang)
chown -R root/chown --recursive root	Kepemilikan hak akses rekursif ke root
mkfs	Format sistem file
dd if=	Salinan disk
> /dev/sd	Tulis ke perangkat blok.
DROP TABLE/DATABASE	SQL DROP
DELETE FROM(tanpa WHERE)	SQL DELETE tanpa WHERE
TRUNCATE TABLE	SQL TRUNCATE
> /etc/	Timpa konfigurasi sistem
systemctl stop/restart/disable/mask	Hentikan/mulai ulang/nonaktifkan layanan sistem
kill -9 -1	Hentikan semua proses
pkill -9	Memaksa penghentian proses
Pola bom garpu	Bom garpu
bash -c// sh -c/zsh -c​ksh -c	Eksekusi perintah shell melalui -cflag (termasuk flag gabungan seperti -lc)
python -e// perl -e/ruby -e​node -c	Eksekusi skrip melalui flag -e/-c
curl ... | sh/wget ... | sh	Salurkan konten jarak jauh ke shell.
bash <(curl ...)/sh <(wget ...)	Menjalankan skrip jarak jauh melalui substitusi proses.
teeke /etc/, ~/.ssh/,~/.hermes/.env	Timpa file sensitif melalui tee
>/ >>ke /etc/, ~/.ssh/,~/.hermes/.env	Timpa file sensitif melalui pengalihan
xargs rm	xargs dengan rm
find -exec rm/find -delete	Temukan dengan tindakan destruktif
cp/ mv/ installke/etc/	Salin/pindahkan file ke konfigurasi sistem
sed -i/ sed --in-placepada/etc/	Pengeditan konfigurasi sistem secara langsung
pkill/ killallhermes/gateway	Pencegahan penghentian diri
gateway rundengan &/ disown/ nohup/setsid	Mencegah memulai gateway di luar pengelola layanan.
informasi
Pembukaan kontainer : Saat dijalankan di docker, singularity, modal, daytona, atau vercel_sandboxbackend, pemeriksaan perintah berbahaya dilewati karena kontainer itu sendiri merupakan batas keamanan. Perintah destruktif di dalam kontainer tidak dapat membahayakan host.

Alur Persetujuan (CLI)
Pada CLI interaktif, perintah berbahaya akan menampilkan permintaan persetujuan langsung:

  ⚠️  DANGEROUS COMMAND: recursive delete
      rm -rf /tmp/old-project

      [o]nce  |  [s]ession  |  [a]lways  |  [d]eny

      Choice [o/s/a/D]:


Keempat opsi tersebut:

sekali — izinkan eksekusi tunggal ini
sesi — izinkan pola ini untuk sisa sesi
selalu — tambahkan ke daftar izin permanen (disimpan ke config.yaml)
tolak (default) — blokir perintah
Alur Persetujuan (Gerbang/Pesan)
Pada platform perpesanan, agen mengirimkan detail perintah berbahaya ke obrolan dan menunggu pengguna membalas:

Balas ya , y , setujui , oke , atau lanjutkan ke persetujuan
Balas dengan no , n , deny , atau cancel untuk menolak.
Variabel HERMES_EXEC_ASK=1lingkungan diatur secara otomatis saat menjalankan gateway.

Daftar Permanen yang Diizinkan
Perintah yang disetujui dengan "selalu" disimpan ke ~/.hermes/config.yaml:

# Permanently allowed dangerous command patterns
command_allowlist:
  - rm
  - systemctl


Pola-pola ini dimuat saat startup dan disetujui secara otomatis di semua sesi mendatang.

tip
Gunakan fitur ini hermes config edituntuk meninjau atau menghapus pola dari daftar pola yang diizinkan secara permanen.

Otorisasi Pengguna (Gateway)
Saat menjalankan gateway pesan, Hermes mengontrol siapa yang dapat berinteraksi dengan bot melalui sistem otorisasi berlapis.

Otorisasi Cek Pesanan
Metode ini _is_user_authorized()melakukan pengecekan dalam urutan berikut:

Bendera izinkan semua per platform (misalnya, DISCORD_ALLOW_ALL_USERS=true)
Daftar pengguna yang disetujui untuk dipasangkan melalui DM (pengguna yang disetujui melalui kode pasangan)
Daftar izin khusus platform (misalnya, TELEGRAM_ALLOWED_USERS=12345,67890)
Daftar izin global ( GATEWAY_ALLOWED_USERS=12345,67890)
Izinkan semua secara global ( GATEWAY_ALLOW_ALL_USERS=true)
Default: tolak
Daftar yang Diizinkan Platform
Tetapkan ID pengguna yang diizinkan sebagai nilai yang dipisahkan koma di ~/.hermes/.env:

# Platform-specific allowlists
TELEGRAM_ALLOWED_USERS=123456789,987654321
DISCORD_ALLOWED_USERS=111222333444555666
WHATSAPP_ALLOWED_USERS=15551234567
SLACK_ALLOWED_USERS=U01ABC123

# Cross-platform allowlist (checked for all platforms)
GATEWAY_ALLOWED_USERS=123456789

# Per-platform allow-all (use with caution)
DISCORD_ALLOW_ALL_USERS=true

# Global allow-all (use with extreme caution)
GATEWAY_ALLOW_ALL_USERS=true


peringatan
Jika tidak ada daftar izin yang dikonfigurasi dan GATEWAY_ALLOW_ALL_USERStidak diatur, semua pengguna akan ditolak . Gateway mencatat peringatan saat startup:

No user allowlists configured. All unauthorized users will be denied.
Set GATEWAY_ALLOW_ALL_USERS=true in ~/.hermes/.env to allow open access,
or configure platform allowlists (e.g., TELEGRAM_ALLOWED_USERS=your_id).


Sistem Pencocokan DM
Untuk otorisasi yang lebih fleksibel, Hermes menyertakan sistem pemasangan berbasis kode. Alih-alih memerlukan ID pengguna di awal, pengguna yang tidak dikenal menerima kode pemasangan satu kali yang disetujui oleh pemilik bot melalui CLI.

Cara kerjanya:

Seorang pengguna tak dikenal mengirimkan pesan langsung (DM) ke bot.
Bot tersebut membalas dengan kode pasangan 8 karakter.
Pemilik bot berjalan hermes pairing approve <platform> <code>di CLI.
Pengguna tersebut disetujui secara permanen untuk platform tersebut.
Kendalikan bagaimana pesan langsung yang tidak sah ditangani di ~/.hermes/config.yaml:

unauthorized_dm_behavior: pair

whatsapp:
  unauthorized_dm_behavior: ignore

pairadalah pengaturan default. DM yang tidak berwenang akan mendapatkan balasan berupa kode pasangan.
ignoreSecara diam-diam menghapus pesan pribadi yang tidak sah.
Bagian platform akan menimpa pengaturan default global, sehingga Anda dapat tetap melakukan pairing di Telegram sambil tetap membisukan WhatsApp.
Fitur keamanan (berdasarkan panduan OWASP + NIST SP 800-63-4):

Fitur	Detail
Format kode	8 karakter dari alfabet 32 ​​karakter yang tidak ambigu (tanpa 0/O/1/I)
Keserampangan	Kriptografi ( secrets.choice())
Kode TTL	Masa berlaku 1 jam
Pembatasan laju	1 permintaan per pengguna setiap 10 menit
Batas tertunda	Maksimal 3 kode tertunda per platform
Penguncian	5 kali upaya persetujuan gagal → Penguncian selama 1 jam
Keamanan berkas	chmod 0600pada semua file data pasangan
Pencatatan	Kode tidak pernah dicatat ke stdout.
Memasangkan perintah CLI:

# List pending and approved users
hermes pairing list

# Approve a pairing code
hermes pairing approve telegram ABC12DEF

# Revoke a user's access
hermes pairing revoke telegram 123456789

# Clear all pending codes
hermes pairing clear-pending


Penyimpanan: Data pasangan disimpan dalam ~/.hermes/pairing/file JSON per platform:

{platform}-pending.json— permintaan pemasangan tertunda
{platform}-approved.json— pengguna yang disetujui
_rate_limits.json— pembatasan laju dan pelacakan penguncian
Isolasi Kontainer
Saat menggunakan dockerbackend terminal, Hermes menerapkan penguatan keamanan yang ketat pada setiap kontainer.

Bendera Keamanan Docker
Setiap kontainer berjalan dengan flag-flag ini (yang didefinisikan dalam tools/environments/docker.py):

_SECURITY_ARGS = [
    "--cap-drop", "ALL",                          # Drop ALL Linux capabilities
    "--cap-add", "DAC_OVERRIDE",                  # Root can write to bind-mounted dirs
    "--cap-add", "CHOWN",                         # Package managers need file ownership
    "--cap-add", "FOWNER",                        # Package managers need file ownership
    "--security-opt", "no-new-privileges",         # Block privilege escalation
    "--pids-limit", "256",                         # Limit process count
    "--tmpfs", "/tmp:rw,nosuid,size=512m",         # Size-limited /tmp
    "--tmpfs", "/var/tmp:rw,noexec,nosuid,size=256m",  # No-exec /var/tmp
    "--tmpfs", "/run:rw,noexec,nosuid,size=64m",   # No-exec /run
]


Keterbatasan Sumber Daya
Sumber daya kontainer dapat dikonfigurasi di ~/.hermes/config.yaml:

terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  docker_forward_env: []  # Explicit allowlist only; empty keeps secrets out of the container
  container_cpu: 1        # CPU cores
  container_memory: 5120  # MB (default 5GB)
  container_disk: 51200   # MB (default 50GB, requires overlay2 on XFS)
  container_persistent: true  # Persist filesystem across sessions


Ketahanan Sistem Berkas
Mode persisten ( container_persistent: true): Bind-mount /workspacedan /rootdari~/.hermes/sandboxes/docker/<task_id>/
Mode sementara ( container_persistent: false): Menggunakan tmpfs untuk ruang kerja — semuanya hilang saat pembersihan
tip
Untuk penerapan gateway produksi, gunakan docker, modal, daytona, atau vercel_sandboxbackend untuk mengisolasi perintah agen dari sistem host Anda. Ini sepenuhnya menghilangkan kebutuhan akan persetujuan perintah yang berbahaya.

peringatan
Jika Anda menambahkan nama ke terminal.docker_forward_env, variabel-variabel tersebut sengaja disuntikkan ke dalam kontainer untuk perintah terminal. Ini berguna untuk kredensial khusus tugas seperti GITHUB_TOKEN, tetapi juga berarti kode yang berjalan di dalam kontainer dapat membaca dan mengekstraknya.

Perbandingan Keamanan Backend Terminal
Backend	Isolasi	Pemeriksaan Cmd Berbahaya	Terbaik untuk
lokal	Tidak ada — berjalan di host	✅ Ya	Pengembangan, pengguna tepercaya
ssh	Mesin jarak jauh	✅ Ya	Berjalan di server terpisah
buruh pelabuhan	Wadah	❌ Dilewati (wadah adalah batas)	Gerbang produksi
keganjilan	Wadah	❌ Dilewati	Lingkungan HPC
modal	Kotak pasir awan	❌ Dilewati	Isolasi cloud yang dapat diskalakan
Daytona	Kotak pasir awan	❌ Dilewati	Ruang kerja cloud permanen
kotak pasir vercel	Cloud microVM	❌ Dilewati	Eksekusi cloud dengan persistensi snapshot.
Penerusan Variabel Lingkungan
Baik execute_codedan sama- terminalsama menghapus variabel lingkungan sensitif dari proses anak untuk mencegah eksfiltrasi kredensial oleh kode yang dihasilkan LLM. Namun, keterampilan yang menyatakan required_environment_variablessecara sah memerlukan akses ke variabel-variabel tersebut.

Cara Kerjanya
Dua mekanisme memungkinkan variabel spesifik melewati filter sandbox:

1. Penerusan berdasarkan keahlian (otomatis)

Saat sebuah skill dimuat (melalui skill_viewatau /skillperintah) dan mendeklarasikan required_environment_variables, variabel apa pun yang sebenarnya diatur dalam lingkungan akan secara otomatis didaftarkan sebagai passthrough. Variabel yang hilang (masih dalam status setup-needed) tidak didaftarkan.

# In a skill's SKILL.md frontmatter
required_environment_variables:
  - name: TENOR_API_KEY
    prompt: Tenor API key
    help: Get a key from https://developers.google.com/tenor


Setelah memuat skill ini, TENOR_API_KEYmaka akan diteruskan ke execute_codebackend terminallokal dan jarak jauh (Docker, Modal) — tidak diperlukan konfigurasi manual.

Docker & Modal
Sebelum versi 0.5.1, Docker forward_envmemiliki sistem terpisah dari passthrough skill. Sekarang keduanya telah digabungkan — variabel lingkungan yang dideklarasikan oleh skill secara otomatis diteruskan ke kontainer Docker dan sandbox Modal tanpa perlu menambahkannya docker_forward_envsecara manual.

2. Penerusan berbasis konfigurasi (manual)

Untuk variabel lingkungan yang tidak dideklarasikan oleh skill apa pun, tambahkan ke terminal.env_passthroughdalam config.yaml:

terminal:
  env_passthrough:
    - MY_CUSTOM_KEY
    - ANOTHER_TOKEN

Penerusan File Kredensial (token OAuth, dll.)
Beberapa skill memerlukan file (bukan hanya variabel lingkungan) di dalam sandbox — misalnya, Google Workspace menyimpan token OAuth di google_token.jsonbawah profil aktif HERMES_HOME. Skill mendeklarasikan ini di bagian frontmatter:

required_credential_files:
  - path: google_token.json
    description: Google OAuth2 token (created by setup script)
  - path: google_client_secret.json
    description: Google OAuth2 client credentials


Saat dimuat, Hermes memeriksa apakah file-file ini ada di profil aktif HERMES_HOMEdan mendaftarkannya untuk dipasang:

Docker : Pemasangan bind hanya baca ( -v host:container:ro)
Modal : Dipasang saat pembuatan sandbox + disinkronkan sebelum setiap perintah (menangani pengaturan OAuth di tengah sesi)
Lokal : Tidak perlu tindakan apa pun (file sudah dapat diakses)
Anda juga dapat mencantumkan file kredensial secara manual di config.yaml:

terminal:
  credential_files:
    - google_token.json
    - my_custom_oauth_token.json

Jalur bersifat relatif terhadap ~/.hermes/. File dipasang ke /root/.hermes/dalam kontainer.

Apa yang Difilter oleh Setiap Sandbox
Bak pasir	Filter Default	Penggantian Lewat
jalankan_kode	Memblokir variabel yang mengandung KEY, TOKEN, SECRET, PASSWORD, CREDENTIAL, PASSWD, AUTHdalam namanya; hanya mengizinkan variabel dengan awalan aman yang lolos.	✅ Variabel passthrough melewati kedua pemeriksaan
terminal (lokal)	Memblokir variabel infrastruktur Hermes eksplisit (kunci penyedia, token gateway, kunci API alat)	✅ Variabel passthrough melewati daftar blokir
terminal (Docker)	Tidak ada variabel lingkungan host secara default.	✅ Variabel passthrough + docker_forward_envditeruskan melalui-e
terminal (Modal)	Tidak ada variabel lingkungan/file host secara default.	✅ File kredensial terpasang; penerusan variabel lingkungan melalui sinkronisasi
MCP	Memblokir semuanya kecuali variabel sistem yang aman + yang dikonfigurasi secara eksplisit.env	❌ Tidak terpengaruh oleh passthrough (gunakan envkonfigurasi MCP sebagai gantinya)
Pertimbangan Keamanan
Penerusan ini hanya memengaruhi variabel yang Anda atau keahlian Anda deklarasikan secara eksplisit — postur keamanan default tidak berubah untuk kode yang dihasilkan LLM secara sembarangan.
File kredensial dipasang hanya untuk dibaca ke dalam kontainer Docker.
Skills Guard memindai konten skill untuk pola akses lingkungan yang mencurigakan sebelum instalasi.
Missing/unset vars are never registered (you can't leak what doesn't exist)
Hermes infrastructure secrets (provider API keys, gateway tokens) should never be added to env_passthrough — they have dedicated mechanisms
MCP Credential Handling
MCP (Model Context Protocol) server subprocesses receive a filtered environment to prevent accidental credential leakage.

Safe Environment Variables
Only these variables are passed through from the host to MCP stdio subprocesses:

PATH, HOME, USER, LANG, LC_ALL, TERM, SHELL, TMPDIR


Plus any XDG_* variables. All other environment variables (API keys, tokens, secrets) are stripped.

Variables explicitly defined in the MCP server's env config are passed through:

mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_..."  # Only this is passed


Credential Redaction
Error messages from MCP tools are sanitized before being returned to the LLM. The following patterns are replaced with [REDACTED]:

GitHub PATs (ghp_...)
OpenAI-style keys (sk-...)
Bearer tokens
token=, key=, API_KEY=, password=, secret= parameters
Website Access Policy
You can restrict which websites the agent can access through its web and browser tools. This is useful for preventing the agent from accessing internal services, admin panels, or other sensitive URLs.

# In ~/.hermes/config.yaml
security:
  website_blocklist:
    enabled: true
    domains:
      - "*.internal.company.com"
      - "admin.example.com"
    shared_files:
      - "/etc/hermes/blocked-sites.txt"


When a blocked URL is requested, the tool returns an error explaining the domain is blocked by policy. The blocklist is enforced across web_search, web_extract, browser_navigate, and all URL-capable tools.

See Website Blocklist in the configuration guide for full details.

SSRF Protection
All URL-capable tools (web search, web extract, vision, browser) validate URLs before fetching them to prevent Server-Side Request Forgery (SSRF) attacks. Blocked addresses include:

Private networks (RFC 1918): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
Loopback: 127.0.0.0/8, ::1
Link-local: 169.254.0.0/16 (includes cloud metadata at 169.254.169.254)
CGNAT / shared address space (RFC 6598): 100.64.0.0/10 (Tailscale, WireGuard VPNs)
Cloud metadata hostnames: metadata.google.internal, metadata.goog
Reserved, multicast, and unspecified addresses
SSRF protection is always active for internet-facing use and DNS failures are treated as blocked (fail-closed). Redirect chains are re-validated at each hop to prevent redirect-based bypasses.

Intentionally allowing private URLs
Some setups legitimately need private/internal URL access — home networks that resolve home.arpa to RFC 1918 space, LAN-only Ollama/llama.cpp endpoints, internal wikis, cloud metadata debugging, and the like. For those cases there's a global opt-out:

security:
  allow_private_urls: true   # default: false


Saat diaktifkan, alat web, peramban, pengambilan URL visi, dan unduhan media gateway tidak lagi menolak tujuan RFC 1918 / loopback / link-local / CGNAT / cloud-metadata. Ini adalah batasan kepercayaan yang disengaja — aktifkan hanya pada mesin di mana agen yang menjalankan URL yang disuntikkan secara sembarangan terhadap jaringan lokal merupakan risiko yang dapat diterima. Gateway yang menghadap publik harus membiarkannya nonaktif.

Pelindung substring host (yang memblokir trik domain Unicode yang mirip bahkan ketika IP yang mendasarinya bersifat publik) tetap aktif terlepas dari pengaturan ini.

Pemindaian Keamanan Pra-Eksekutif Tirith
Hermes mengintegrasikan Tirith untuk pemindaian perintah tingkat konten sebelum dieksekusi. Tirith mendeteksi ancaman yang tidak terdeteksi oleh pencocokan pola saja:

Pemalsuan URL homograf (serangan domain internasional)
Pola pipa ke interpreter ( curl | bash, wget | sh)
Serangan injeksi terminal
Tirith menginstal secara otomatis dari rilis GitHub pada penggunaan pertama dengan verifikasi checksum SHA-256 (dan verifikasi asal usul tanda tangan bersama jika tanda tangan bersama tersedia).

# In ~/.hermes/config.yaml
security:
  tirith_enabled: true       # Enable/disable tirith scanning (default: true)
  tirith_path: "tirith"      # Path to tirith binary (default: PATH lookup)
  tirith_timeout: 5          # Subprocess timeout in seconds
  tirith_fail_open: true     # Allow execution when tirith is unavailable (default: true)


Saat tirith_fail_openbernilai true(default), perintah akan dilanjutkan jika tirith tidak terpasang atau mengalami batas waktu. Atur ke falsedi lingkungan dengan keamanan tinggi untuk memblokir perintah saat tirith tidak tersedia.

Tirith menyediakan biner yang sudah dibuat sebelumnya untuk Linux (x86_64 / aarch64) dan macOS (x86_64 / arm64). Pada platform yang tidak memiliki biner yang sudah dibuat sebelumnya (Windows, dll.), tirith dilewati secara diam-diam — pengaman pencocokan pola tetap berjalan, dan CLI tidak menampilkan banner "tidak tersedia". Untuk menggunakan tirith di Windows, jalankan Hermes di bawah WSL.

Putusan Tirith terintegrasi dengan alur persetujuan: perintah yang aman akan diteruskan, sementara perintah yang mencurigakan dan diblokir akan memicu persetujuan pengguna dengan temuan Tirith lengkap (tingkat keparahan, judul, deskripsi, alternatif yang lebih aman). Pengguna dapat menyetujui atau menolak — pilihan default adalah menolak untuk menjaga keamanan skenario tanpa pengawasan.

Perlindungan Injeksi File Konteks
File konteks (AGENTS.md, .cursorrules, SOUL.md) dipindai untuk mendeteksi injeksi prompt sebelum dimasukkan ke dalam prompt sistem. Pemindai memeriksa:

Instruksi untuk mengabaikan/mengabaikan instruksi sebelumnya
Komentar HTML tersembunyi dengan kata kunci mencurigakan
Upaya membaca rahasia ( .env, credentials, .netrc)
Pengambilan kredensial melaluicurl
Karakter Unicode tak terlihat (spasi tanpa lebar, penggantian dua arah)
File yang diblokir menampilkan peringatan:

[BLOCKED: AGENTS.md contained potential prompt injection (prompt_injection). Content not loaded.]


Praktik Terbaik untuk Penerapan di Lingkungan Produksi
Daftar Periksa Penyebaran Gateway
Tetapkan daftar izin eksplisit — jangan pernah digunakan GATEWAY_ALLOW_ALL_USERS=truedalam produksi.
Gunakan backend kontainer — atur terminal.backend: dockerdi config.yaml
Batasi penggunaan sumber daya — tetapkan batasan CPU, memori, dan disk yang sesuai.
Simpan rahasia dengan aman — simpan kunci API ~/.hermes/.envdengan izin file yang tepat.
Aktifkan pemasangan DM — gunakan kode pemasangan alih-alih memasukkan ID pengguna secara manual jika memungkinkan.
Tinjau daftar perintah yang diizinkan — lakukan audit secara berkala command_allowlistdi config.yaml
AturMESSAGING_CWD — jangan izinkan agen beroperasi dari direktori sensitif.
Jalankan sebagai pengguna non-root — jangan pernah menjalankan gateway sebagai root.
Pantau log — periksa ~/.hermes/logs/upaya akses tidak sah.
Selalu perbarui — jalankan hermes updatesecara teratur untuk mendapatkan patch keamanan.
Mengamankan Kunci API
# Set proper permissions on the .env file
chmod 600 ~/.hermes/.env

# Keep separate keys for different services
# Never commit .env files to version control


Isolasi Jaringan
Untuk keamanan maksimal, jalankan gateway pada mesin atau VM terpisah. Atur terminal.backend: sshdi config.yaml, lalu berikan detail host melalui variabel lingkungan di ~/.hermes/.env:

# ~/.hermes/config.yaml
terminal:
  backend: ssh

# ~/.hermes/.env
TERMINAL_SSH_HOST=agent-worker.local
TERMINAL_SSH_USER=hermes
TERMINAL_SSH_KEY=~/.ssh/hermes_agent_key


Detail koneksi SSH tersimpan di .env(bukan config.yaml) sehingga tidak diperiksa atau dibagikan bersama dengan ekspor profil. Hal ini menjaga agar koneksi pesan gateway tetap terpisah dari eksekusi perintah agen.

Pemeriksaan penasihat rantai pasokan
Hermes dilengkapi dengan pemindai penasihat bawaan yang menandai paket Python di venv aktif yang sesuai dengan katalog versi yang diketahui telah disusupi (worm rantai pasokan seperti mistralai 2.4.6serangan peracunan Mei 2026). Implementasinya ada di hermes_cli/security_advisories.py.

Cara kerjanya:

Banner startup CLI. Sebuah peringatan satu baris akan dicetak jika ada saran yang cocok, dengan petunjuk hermes doctoruntuk perbaikan lengkap.
hermes doctorMenampilkan setiap pemberitahuan aktif beserta detail versi dan instruksi perbaikan 2-4 langkah .
Pengaktifan gateway. Tercatat di gateway.log; pesan interaktif pertama mendapatkan banner operator singkat.
Setiap pemberitahuan memiliki ID tetap. Setelah Anda membaca dan menindaklanjutinya, Anda dapat mengabaikannya sepenuhnya:

hermes doctor --ack <advisory-id>

Konfirmasi tersebut tetap tersimpan config.security.acked_advisoriesdan bertahan setelah restart. Pemberitahuan lama sengaja tidak dihapus dari katalog — membiarkannya tetap ada akan mencegah instalasi baru terkena dampak versi yang bermasalah di masa lalu yang mungkin masih tersimpan dalam cache di mirror pribadi.

Pemeriksaan itu sendiri hanya dilakukan pada pustaka standar (stdlib) dan berjalan dari satu importlib.metadata.version()pencarian per pemberitahuan, jadi aman untuk dijalankan setiap kali sistem dimulai.

Instalasi bertahap dependensi opsional
Banyak fitur (Mistral TTS, ElevenLabs, memori Honcho, Bedrock, Slack, Matrix, …) bergantung pada paket Python yang tidak dibutuhkan oleh setiap pengguna. Hermes menginstal paket-paket ini secara bertahap pada penggunaan pertama, bukan secara langsung hermes-agent[all]. Implementasinya berada di tools/lazy_deps.py.

Kompromi yang diatasi dengan ini:

Kerentanan. Ketika dependensi transisi dari sebuah extra menjadi tidak tersedia di PyPI (dikarantina karena malware, ditarik, unggahan rusak), seluruh proses [all]resolve akan gagal dan instalasi baru akan secara diam-diam kembali ke tier yang dipangkas — kehilangan lebih dari 10 extra yang tidak terkait sekaligus. Instalasi lazy mengisolasi setiap backend sehingga satu dependensi yang bermasalah tidak dapat merusak fitur yang tidak terkait.
Pembengkakan. Pengguna yang hanya berkomunikasi dengan satu penyedia layanan tidak lagi mengunduh ratusan paket yang tidak akan pernah mereka impor.
Cara kerjanya:

Modul backend dipanggil ensure("feature.name")di bagian atas jalur impor pertamanya.
Jika dependensi hilang, ensureperiksa security.allow_lazy_installsdi config.yaml(default true) dan jalankan venv-scoped pip installuntuk spesifikasi yang diizinkan.
Jika instalasi gagal atau pengguna telah menonaktifkan instalasi tunda (lazy install), panggilan tersebut akan menimbulkan kesalahan FeatureUnavailabledengan output stderr pip yang sebenarnya dan penunjuk ke hermes tools.
Jaminan keamanan yang diberlakukan oleh tools/lazy_deps.py:

Menjamin	Apa artinya
Hanya lingkup Venv	Menginstal target sys.executabledi venv aktif — bukan di Python sistem.
PyPI hanya namanya saja	Spesifikasi menerima "package>=1.0,<2"sintaks. Tidak ada --index-url, git+https://, atau jalur file: — program jahat config.yamltidak dapat mengalihkan instalasi.
Daftar yang Diizinkan	Hanya spesifikasi yang muncul di peta dalam pohon LAZY_DEPSyang dapat diinstal melalui jalur ini. Kesalahan ketik pada nama fitur TIDAK mendapatkan semantik instal-apa pun.
Menolak untuk ikut serta	Diatur security.allow_lazy_installs: falseuntuk menonaktifkan instalasi saat runtime sepenuhnya. Berguna untuk jaringan terbatas atau kebijakan keamanan yang ketat.
Tidak ada percobaan ulang senyap.	Kegagalan muncul sebagai FeatureUnavailable— tidak ada caching untuk kondisi buruk, tidak ada badai percobaan ulang.
Untuk menonaktifkan instalasi saat runtime:

# ~/.hermes/config.yaml
security:
  allow_lazy_installs: false

Saat dinonaktifkan, backend yang membutuhkan dependensi opsional akan memberi tahu pengguna untuk menjalankan instalasi secara manual ( pip install …) atau memilih backend yang berbeda melalui hermes tools.
```

---
===========🔐™️®️©️🔐===========

---
```

Di halaman ini
Pos pemeriksaan dan/rollback
Hermes Agent dapat secara otomatis mengambil snapshot proyek Anda sebelum operasi yang merusak dan memulihkannya dengan satu perintah. Checkpoint bersifat opsional sejak versi 2 — sebagian besar pengguna tidak pernah menggunakannya /rollback, dan penyimpanan shadow-store cukup besar seiring waktu, jadi pengaturan default-nya adalah nonaktif.

Aktifkan titik pemeriksaan per sesi dengan --checkpoints:

hermes chat --checkpoints

Atau aktifkan secara global di ~/.hermes/config.yaml:

checkpoints:
  enabled: true

Jaring pengaman ini didukung oleh Checkpoint Manager internal yang menyimpan satu repositori git bayangan bersama ~/.hermes/checkpoints/store/— proyek asli Anda .gittidak pernah disentuh. Setiap proyek yang dikerjakan agen berbagi penyimpanan yang sama, sehingga basis data objek yang dapat diakses berdasarkan konten (content-addressable object DB) git melakukan deduplikasi di seluruh proyek dan di seluruh giliran.

Apa yang Memicu Pos Pemeriksaan?
Pos pemeriksaan diambil secara otomatis sebelum:

Alat file — write_filedanpatch
Perintah terminal yang merusak — rm, rmdir, cp, install, mv, sed -i, truncate, dd, shred, pengalihan keluaran ( >), dan git reset/ clean/checkout
Agen tersebut membuat paling banyak satu titik pemeriksaan per direktori per giliran , sehingga sesi yang berjalan lama tidak membanjiri snapshot.

Referensi Cepat
Perintah garis miring dalam sesi:

Memerintah	Keterangan
/rollback	Cantumkan semua titik pemeriksaan beserta statistik perubahannya.
/rollback <N>	Kembalikan ke titik pemeriksaan N (juga membatalkan giliran obrolan terakhir)
/rollback diff <N>	Lihat pratinjau perbedaan antara titik pemeriksaan N dan keadaan saat ini.
/rollback <N> <file>	Pulihkan satu file dari titik pemeriksaan N
CLI untuk memeriksa dan mengelola toko di luar sesi:

Memerintah	Keterangan
hermes checkpoints	Tampilkan ukuran total, jumlah proyek, dan rincian per proyek.
hermes checkpoints status	Sama seperti telanjangcheckpoints
hermes checkpoints list	Nama lain untukstatus
hermes checkpoints prune	Lakukan pembersihan paksa: hapus file yatim piatu/usang, GC (Garbage Collection), terapkan batasan ukuran.
hermes checkpoints clear	Ledakkan seluruh pangkalan pos pemeriksaan dengan bom nuklir (tanyakan dulu).
hermes checkpoints clear-legacy	Hapus hanya legacy-*arsip dari migrasi v1.
Cara Kerja Pos Pemeriksaan
Secara garis besar:

Hermes mendeteksi kapan alat-alat akan memodifikasi file di pohon kerja Anda.
Sekali per giliran percakapan (per direktori), hal itu:
Menentukan direktori root proyek yang wajar untuk file tersebut.
Menginisialisasi atau menggunakan kembali penyimpanan bayangan bersama tunggal di ~/.hermes/checkpoints/store/.
Mengolah data menjadi indeks per proyek, membangun struktur pohon, dan melakukan commit ke referensi per proyek ( refs/hermes/<project-hash>).
Referensi per proyek ini membentuk riwayat titik pemeriksaan yang dapat Anda periksa dan pulihkan melalui /rollback.
tool call

before mutate
ensure_checkpoint()

git add/commit-tree/update-ref

OK / skipped

apply changes

User command
(hermes, gateway)

AIAgent
(run_agent.py)

File & terminal tools

CheckpointManager

Shared shadow store
~/.hermes/checkpoints/store/

Konfigurasi
Konfigurasi di ~/.hermes/config.yaml:

checkpoints:
  enabled: false              # master switch (default: false — opt-in)
  max_snapshots: 20           # max checkpoints per project (enforced via ref rewrite + gc)
  max_total_size_mb: 500      # hard cap on total store size; oldest commits dropped
  max_file_size_mb: 10        # skip any single file larger than this

  # Auto-maintenance (on by default): sweep ~/.hermes/checkpoints/ at startup
  # and delete project entries whose working directory no longer exists
  # (orphans) or whose last_touch is older than retention_days. Runs at most
  # once per min_interval_hours, tracked via a .last_prune marker.
  auto_prune: true
  retention_days: 7
  delete_orphans: true
  min_interval_hours: 24


Untuk menonaktifkan semuanya:

checkpoints:
  enabled: false
  auto_prune: false

Saat enabled: false, Checkpoint Manager tidak melakukan apa pun dan tidak pernah mencoba operasi git. Saat auto_prune: false, penyimpanan akan terus bertambah hingga Anda menjalankannya hermes checkpoints prunesecara manual.

Daftar Titik Pemeriksaan
Dari sesi CLI:

/rollback

Hermes merespons dengan daftar yang diformat yang menunjukkan statistik perubahan:

📸 Checkpoints for /path/to/project:

  1. 4270a8c  2026-03-16 04:36  before patch  (1 file, +1/-0)
  2. eaf4c1f  2026-03-16 04:35  before write_file
  3. b3f9d2e  2026-03-16 04:34  before terminal: sed -i s/old/new/ config.py  (1 file, +1/-1)

  /rollback <N>             restore to checkpoint N
  /rollback diff <N>        preview changes since checkpoint N
  /rollback <N> <file>      restore a single file from checkpoint N


Memeriksa Toko dari Luar
hermes checkpoints

Contoh output:

Checkpoint base: /home/you/.hermes/checkpoints
Total size:      142.3 MB
  store/         138.1 MB
  legacy-*       4.2 MB
Projects:        12

  WORKDIR                                                       COMMITS    LAST TOUCH  STATE
  /home/you/code/hermes-agent                                        20       2h ago  live
  /home/you/code/experiments/rl-runner                                8       1d ago  live
  /home/you/code/old-prototype                                        3       9d ago  orphan
  ...

Legacy archives (1):
  legacy-20260506-050616                           4.2 MB

Clear with: hermes checkpoints clear-legacy


Paksa pemindaian penuh (mengabaikan penanda idempotensi 24 jam):

hermes checkpoints prune --retention-days 3 --max-size-mb 200


Melihat Pratinjau Perubahan dengan/rollback diff
Sebelum melakukan pemulihan, pratinjau perubahan apa saja yang terjadi sejak titik pemulihan:

/rollback diff 1

Ini menampilkan ringkasan git diff stat diikuti oleh perbedaan sebenarnya.

Memulihkan dengan/rollback
/rollback 1

Di balik layar, Hermes:

Memverifikasi apakah commit target ada di shadow store.
Mengambil snapshot keadaan saat ini sebelum rollback sehingga Anda dapat "membatalkan pembatalan" di kemudian hari.
Mengembalikan file yang dilacak di direktori kerja Anda.
Membatalkan giliran percakapan terakhir sehingga konteks agen sesuai dengan keadaan sistem file yang dipulihkan.
Pemulihan Berkas Tunggal
Pulihkan hanya satu file dari titik pemeriksaan tanpa memengaruhi sisa direktori:

/rollback 1 src/broken_file.py

Pelindung Keselamatan dan Kinerja
Ketersediaan Git — jika gittidak ditemukan di PATH, checkpoint akan dinonaktifkan secara transparan.
Lingkup direktori — Hermes melewati direktori yang terlalu luas (root /, home $HOME).
Ukuran repositori — direktori dengan lebih dari 50.000 file akan dilewati.
Batasan ukuran per file — file yang lebih besar dari max_file_size_mb(standar 10 MB) akan dikecualikan dari snapshot. Mencegah terbuangnya dataset, bobot model, atau media yang dihasilkan secara tidak sengaja.
Batasan total ukuran penyimpanan — ketika penyimpanan melebihi max_total_size_mb(standar 500 MB), commit terlama per proyek akan dihapus secara bergilir hingga berada di bawah batasan tersebut.
Pemangkasan sebenarnya — max_snapshotsdilakukan dengan menulis ulang referensi per proyek dan menjalankannya git gc --prune=nowsetelahnya, sehingga objek yang tidak terpakai tidak menumpuk.
Snapshot tanpa perubahan — jika tidak ada perubahan sejak snapshot terakhir, checkpoint dilewati.
Kesalahan yang tidak fatal — semua kesalahan di dalam Checkpoint Manager dicatat pada tingkat debug; alat Anda tetap berjalan.
Di mana Pos Pemeriksaan Berada
~/.hermes/checkpoints/
  ├── store/                 # single shared bare git repo
  │   ├── HEAD, objects/     # git internals (shared across projects)
  │   ├── refs/hermes/<hash> # per-project branch tip
  │   ├── indexes/<hash>     # per-project git index
  │   ├── projects/<hash>.json  # workdir + created_at + last_touch
  │   └── info/exclude
  ├── .last_prune            # auto-prune idempotency marker
  └── legacy-<ts>/           # archived pre-v2 per-project shadow repos


Masing-masing <hash>berasal dari jalur absolut direktori kerja. Anda biasanya tidak perlu menyentuh ini secara manual — gunakan hermes checkpoints status/ prune/ clearsebagai gantinya.

Migrasi dari v1
Sebelum penulisan ulang v2, setiap direktori kerja mendapatkan repositori git bayangan lengkapnya sendiri langsung di bawahnya ~/.hermes/checkpoints/<hash>/. Tata letak tersebut tidak dapat melakukan deduplikasi objek di seluruh proyek dan memiliki pemangkas tanpa operasi yang terdokumentasi — penyimpanan akan terus bertambah tanpa batas.

Pada eksekusi v2 pertama, semua shadow repo pra-v2 dipindahkan ~/.hermes/checkpoints/legacy-<timestamp>/sehingga tata letak single-store yang baru dimulai dengan bersih. /rollbackRiwayat lama masih dapat diakses dengan memeriksa arsip lama secara manual menggunakan git; setelah Anda yakin tidak membutuhkannya, jalankan:

hermes checkpoints clear-legacy

untuk merebut kembali ruang tersebut. Arsip-arsip lama juga ikut terhapus auto_prunesetelahnya retention_days.

Praktik Terbaik
Aktifkan pos pemeriksaan hanya saat Anda membutuhkannya — hermes chat --checkpointsatau per profil enabled: true.
Gunakan /rollback diffsebelum memulihkan — pratinjau perubahan yang akan terjadi untuk memilih titik pemulihan yang tepat.
Gunakan /rollbackalih-alihgit reset saat Anda hanya ingin membatalkan perubahan yang didorong oleh agen.
Periksa hermes checkpoints statussecara berkala jika Anda menggunakan checkpoint secara teratur — ini menunjukkan proyek mana yang aktif dan berapa biaya yang harus Anda keluarkan untuk toko tersebut.
Gabungkan dengan Git worktree untuk keamanan maksimal — simpan setiap sesi Hermes di worktree/cabangnya sendiri, dengan checkpoint sebagai lapisan tambahan.
Untuk menjalankan beberapa agen secara paralel pada repositori yang sama, lihat panduan tentang Git worktrees .
```

---
===========🔐™️®️©️🔐===========

---
```

