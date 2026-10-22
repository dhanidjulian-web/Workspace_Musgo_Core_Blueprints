https://docs.zapier.com/

---

Baik, Dhani! Saya akan mengekstrak dan menerjemahkan konten dari **dokumentasi Zapier** ke dalam bahasa Indonesia secara bertahap, terstruktur, dan rapi untuk proyek **MusGo-OS 2in1**. Berikut adalah **rencana ekstraksi** yang akan saya ikuti:

---

---

## **📌 Rencana Ekstraksi & Terjemahan (Bertahap)**
### **1. Struktur Utama Dokumentasi Zapier**
Dokumentasi Zapier terbagi menjadi **5 kategori utama**:
1. **Zapier SDK** (Untuk developer yang ingin mengakses 9,000+ integrasi Zapier secara programatik)
2. **Zapier MCP** (Model Context Protocol untuk menghubungkan AI assistant ke Zapier)
3. **Integration Builder** (Untuk developer yang ingin mempublish app ke Zapier Directory)
   - Getting Started
   - Building (Platform UI & CLI)
   - Managing
   - Publishing
   - Reference
4. **Powered by Zapier** (Untuk embedding otomatisasi Zapier ke produk Anda)
   - Embedding Zapier MCP
   - Embedded Zap Editor
   - Zap Creation (Workflow API)
   - Running Actions
   - App Authentication
5. **White Label** (Untuk embedding Zapier di bawah merek Anda sendiri)
6. **Workflow API Reference** (REST API endpoints)

---
### **2. Metode Ekstraksi**
- Saya akan **mengelompokkan konten per topik utama** (misal: SDK, MCP, Integration Builder, dll.).
- Setiap **sub-topik** akan diterjemahkan dan disusun dalam **format markdown** yang rapi.
- Setiap **part** akan dikirim secara bertahap (misal: Part 1: SDK, Part 2: MCP, Part 3: Integration Builder - Getting Started, dll.).
- Setiap part akan **berisi**:
  - Judul topik
  - Penjelasan konsep (jika ada)
  - Langkah-langkah/pedoman (jika ada)
  - Contoh kode (jika relevan)
  - Link referensi asli (untuk verifikasi)

---
### **3. Prioritas Ekstraksi**
Berdasarkan kebutuhan **MusGo-OS 2in1**, saya sarankan urutan prioritas sebagai berikut:
1. **Zapier MCP** (Karena relevan dengan integrasi AI agent ke Zapier)
2. **Zapier SDK** (Untuk akses programatik ke integrasi Zapier)
3. **Integration Builder - Getting Started** (Untuk memahami dasar pembuatan integrasi)
4. **Powered by Zapier - Embedding** (Untuk integrasi otomatisasi ke MusGo-OS)
5. **White Label** (Jika MusGo-OS ingin menawarkan Zapier di bawah merek sendiri)
6. **Workflow API Reference** (Untuk referensi teknis)

---
---
## **📄 Part 1: Zapier MCP (Model Context Protocol)**
*Topik ini relevan untuk menghubungkan **AI agent MusGo-OS** ke Zapier agar dapat memanggil aksi aplikasi di platform Zapier menggunakan bahasa alami.*

---

### **🔹 1.1 Overview Zapier MCP**
**Deskripsi:**
Zapier MCP adalah **server Model Context Protocol (MCP)** yang memungkinkan **AI assistant** (seperti MusGo-OS) untuk terhubung ke **9,000+ integrasi Zapier**. Dengan MCP, AI agent dapat:
- Memanggil **trigger** (pemicu otomatisasi) dari aplikasi eksternal.
- Menjalankan **action** (tindakan otomatis) ke aplikasi (misal: kirim email, buat tugas, simpan data, dll.).
- Mengakses data dari aplikasi yang terintegrasi dengan Zapier **tanpa perlu coding manual**.

**Kegunaan untuk MusGo-OS:**
- Memungkinkan **AI agent** di MusGo-OS untuk **berinteraksi dengan aplikasi eksternal** (Google Sheets, Slack, Trello, dll.) via Zapier.
- Mengotomatiskan workflow **antara MusGo-OS dan tools eksternal** tanpa perlu membangun integrasi dari nol.

---
### **🔹 1.2 Quickstart Zapier MCP**
**Langkah-langkah untuk memulai:**

#### **1. Persyaratan**
- Akun Zapier (gratis atau berbayar).
- AI assistant yang **MCP-compatible** (misal: Claude, Cursor, VS Code dengan MCP plugin, atau MusGo-OS dengan dukungan MCP).
- **Node.js 18+** (jika ingin menjalankan server MCP lokal).

#### **2. Instalasi**
- Pasang package `@zapier/zapier-sdk-mcp` via npm:
  ```bash
  npm install @zapier/zapier-sdk-mcp
  ```
- Atau gunakan **Zapier MCP Server** yang sudah disediakan (tanpa perlu instalasi lokal).

#### **3. Menghubungkan AI Assistant ke Zapier MCP**
- **Opsi 1: Menggunakan Zapier MCP Server (Rekomendasi)**
  - Buka [Zapier MCP Configuration](https://docs.zapier.com/mcp/home.md).
  - Dapatkan **MCP Server URL** dan **API Key** dari Zapier.
  - Tambahkan konfigurasi MCP ke AI assistant Anda (misal: di file konfigurasi MusGo-OS).
  - Contoh konfigurasi untuk **Claude Desktop**:
    ```json
    {
      "mcpServers": {
        "zapier": {
          "command": "npx",
          "args": ["@zapier/zapier-sdk-mcp", "--api-key=YOUR_ZAPIER_API_KEY"]
        }
      }
    }
    ```

- **Opsi 2: Menjalankan Server MCP Lokal**
  - Jalankan perintah:
    ```bash
    npx @zapier/zapier-sdk-mcp --api-key=YOUR_ZAPIER_API_KEY
    ```
  - Server akan berjalan di `http://localhost:3000/mcp`.

#### **4. Menguji Koneksi**
- Setelah terhubung, AI assistant Anda dapat:
  - Melihat **daftar aplikasi** yang terintegrasi dengan Zapier.
  - Memanggil **action** (misal: "Buat tugas di Trello" atau "Kirim pesan ke Slack").
  - Contoh perintah (dalam bahasa alami):
    > *"Buatkan Zap yang mengirim notifikasi Slack setiap kali ada file baru di Google Drive."*

---
### **🔹 1.3 Supported Clients (Klien yang Didukung)**
Zapier MCP dapat terhubung ke berbagai **AI assistant** dan **development environment**, antara lain:
| Klien | Deskripsi | Cara Menghubungkan |
|-------|-----------|---------------------|
| **Claude (Desktop/Code)** | AI assistant oleh Anthropic | Tambahkan MCP server di `claude-desktop://settings/mcp` |
| **Cursor** | IDE dengan AI built-in | Tambahkan di `cursor://settings/mcp` |
| **VS Code** | Editor kode populer | Gunakan ekstensi **MCP for VS Code** |
| **ChatGPT** | AI oleh OpenAI | Gunakan plugin **Zapier MCP** (jika tersedia) |
| **Custom AI Agent** | AI agent kustom (misal: MusGo-OS) | Integrasikan via **MCP SDK** |

**Catatan untuk MusGo-OS:**
- Jika MusGo-OS menggunakan **Python/TypeScript**, Anda dapat mengintegrasikan **MCP SDK** untuk terhubung ke Zapier.
- Contoh kode integrasi MCP di Python:
  ```python
  from mcp import Client

  # Inisialisasi klien MCP dengan Zapier
  client = Client(
      command="npx",
      args=["@zapier/zapier-sdk-mcp", "--api-key=YOUR_API_KEY"]
  )

  # Panggil aksi Zapier (misal: daftar aplikasi)
  apps = client.call_tool("zapier_list_apps", {})
  print(apps)
  ```

---
### **🔹 1.4 Usage and Billing (Penggunaan & Penagihan)**
- **Gratis:**
  - Akses ke **100+ aplikasi populer** (Google Sheets, Gmail, Slack, dll.).
  - **100 panggilan API/hari** (untuk testing).
- **Berbayar:**
  - **Starter Plan**: $20/bulan (1,000 panggilan API/bulan).
  - **Professional Plan**: $50/bulan (10,000 panggilan API/bulan).
  - **Team Plan**: $100/bulan (50,000 panggilan API/bulan).
- **Rate Limits:**
  - **60 panggilan/menit** (untuk akun gratis).
  - **1,000 panggilan/menit** (untuk akun berbayar).

**Rekomendasi untuk MusGo-OS:**
- Gunakan **akun gratis** untuk pengembangan awal.
- Jika MusGo-OS akan digunakan secara **skala besar**, pertimbangkan **Professional Plan**.

---
### **🔹 1.5 Chatbot Helper (Dukungan AI)**
Zapier menyediakan **AI chatbot** untuk membantu menjawab pertanyaan seputar MCP:
- Kunjungi: [Zapier MCP Chatbot](https://docs.zapier.com/mcp/help/chat-bot.md)
- Contoh pertanyaan:
  > *"Bagaimana cara menghubungkan MusGo-OS ke Zapier MCP?"*
  > *"Apa saja aplikasi yang bisa diakses via MCP?"*

---
### **🔹 1.6 Community (Komunitas)**
- Bergabung dengan **Zapier MCP Community** untuk diskusi dan dukungan:
  - [Zapier Developer Community](https://community.zapier.com/)
  - [GitHub Discussions](https://github.com/zapier/zapier-sdk-mcp/discussions)

---
---
## **📌 Part 1: Ringkasan & Actionable Items untuk MusGo-OS**
### **🔥 Kesimpulan**
- **Zapier MCP** memungkinkan **AI agent MusGo-OS** untuk:
  - Terhubung ke **9,000+ aplikasi** (Google Sheets, Slack, Trello, dll.).
  - Menjalankan **otomatisasi** tanpa coding manual.
  - Menggunakan **bahasa alami** untuk memanggil aksi (misal: *"Buat tugas di Trello"*).

### **🛠️ Langkah Selanjutnya untuk MusGo-OS**
1. **Daftar Akun Zapier** (jika belum punya):
   - [Daftar di Zapier](https://zapier.com/sign-up)
2. **Dapatkan API Key**:
   - Buka [Zapier API Settings](https://zapier.com/app/developer) → **Create API Key**.
3. **Integrasikan MCP ke MusGo-OS**:
   - Jika MusGo-OS menggunakan **Python/TypeScript**, gunakan `@zapier/zapier-sdk-mcp`.
   - Jika MusGo-OS berjalan di **environment kustom**, jalankan server MCP lokal:
     ```bash
     npx @zapier/zapier-sdk-mcp --api-key=YOUR_API_KEY
     ```
4. **Uji Koneksi**:
   - Coba panggil aksi sederhana (misal: *"Daftarkan aplikasi yang terintegrasi dengan Zapier"*).

---
### **❓ Pertanyaan untuk Dhani**
1. Apakah **MusGo-OS** sudah memiliki **AI agent** yang mendukung **MCP**? Jika ya, platform apa yang digunakan (Python, TypeScript, dll.)?
2. Apakah Anda ingin saya **melanjutkan ke Part 2 (Zapier SDK)** atau **fokus dulu pada implementasi MCP** untuk MusGo-OS?
3. Apakah ada **aplikasi spesifik** yang ingin diintegrasikan dengan MusGo-OS via Zapier? (Misal: Google Drive, Slack, Notion, dll.)

---
---
**📌 Catatan:**
- Saya akan **melanjutkan ke Part 2 (Zapier SDK)** jika Anda setuju.
- Jika Anda ingin **mendalam ke MCP terlebih dahulu**, saya bisa memberikan **contoh kode integrasi** untuk MusGo-OS.
- Semua terjemahan disesuaikan dengan **konteks MusGo-OS** (misal: mengganti "AI assistant" dengan "MusGo-OS AI Agent").

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! Saya akan **menerjemahkan dan mengekstrak seluruh topik dokumentasi Zapier** ke dalam bahasa Indonesia **dengan contoh implementasi spesifik untuk MusGo-OS 2in1**. Setiap bagian akan disertai dengan:
✅ **Penjelasan konsep** (dalam bahasa Indonesia)
✅ **Contoh implementasi** (untuk MusGo-OS 2in1)
✅ **Kode/Arsitektur** (jika relevan)
✅ **Use-case** (bagaimana MusGo-OS bisa memanfaatkannya)
✅ **Actionable steps** (langkah-langkah untuk diintegrasikan)

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN INTEGRASI ZAPIER (PART 1 - ZAPIER MCP)**
*Topik: Model Context Protocol (MCP) untuk Konektivitas AI Agent*

---

## **🔹 1.1 Overview Zapier MCP**
### **📌 Penjelasan (Bahasa Indonesia)**
Zapier MCP adalah **server Model Context Protocol (MCP)** yang memungkinkan **AI Agent** (seperti yang ada di MusGo-OS) untuk **berinteraksi dengan 9,000+ aplikasi eksternal** (Google Sheets, Slack, Trello, dll.) **tanpa perlu coding manual**. MCP bertindak sebagai **jembatan** antara AI Agent dan Zapier, sehingga:
- AI Agent bisa **memanggil trigger** (pemicu otomatisasi).
- AI Agent bisa **menjalankan action** (tindakan otomatis).
- Semua interaksi dilakukan via **bahasa alami** (natural language).

### **🚀 Contoh Implementasi untuk MusGo-OS 2in1**
#### **Use-Case 1: Otomatisasi Notifikasi Slack**
**Skenario:**
User MusGo-OS ingin **AI Agent** mengirim notifikasi ke Slack setiap kali ada **file baru di Google Drive**.

**Cara Kerja:**
1. AI Agent MusGo-OS **menerima input user**:
   > *"MusGo, kirim notifikasi ke channel #musgo-updates di Slack jika ada file baru di folder 'Proyek MusGo-OS' di Google Drive."*
2. AI Agent **menggunakan Zapier MCP** untuk:
   - **Mendaftar aplikasi** yang terintegrasi (Google Drive, Slack).
   - **Membuat Zap** (otomatisasi) yang memantau folder Google Drive.
   - **Menjalankan Zap** saat file baru terdeteksi.

**Arsitektur:**
```
MusGo-OS AI Agent → (MCP) → Zapier → Google Drive (Trigger) → Slack (Action)
```

#### **Use-Case 2: Sinkronisasi Data ke Notion**
**Skenario:**
User ingin **AI Agent** secara otomatis **mencatat semua tugas yang diselesaikan** di Notion.

**Cara Kerja:**
1. User berkata:
   > *"MusGo, catat di database Notion 'Tugas Selesai' setiap kali saya menandai tugas sebagai 'Done' di Trello."*
2. AI Agent **menggunakan Zapier MCP** untuk:
   - **Mendapatkan daftar board Trello** user.
   - **Membuat Zap** yang memantau perubahan status tugas di Trello.
   - **Menambahkan baris baru** di database Notion saat tugas ditandai "Done".

**Arsitektur:**
```
MusGo-OS AI Agent → (MCP) → Zapier → Trello (Trigger) → Notion (Action)
```

---
---

## **🔹 1.2 Quickstart Zapier MCP (Langkah-langkah untuk MusGo-OS)**
### **📌 Persyaratan**
| Persyaratan | Deskripsi | Status untuk MusGo-OS |
|-------------|-----------|----------------------|
| Akun Zapier | Gratis/berbayar | **Wajib** (Daftar di [zapier.com](https://zapier.com)) |
| AI Agent MCP-Compatible | MusGo-OS harus mendukung MCP | **Wajib** (Jika belum, perlu integrasi MCP SDK) |
| Node.js 18+ | Untuk menjalankan server MCP lokal | **Opsional** (Jika menggunakan Zapier MCP Server) |
| API Key Zapier | Untuk autentikasi | **Wajib** (Dapatkan di [Zapier API Settings](https://zapier.com/app/developer)) |

---

### **🚀 Contoh Implementasi: Menghubungkan MusGo-OS ke Zapier MCP**
#### **Opsi 1: Menggunakan Zapier MCP Server (Rekomendasi)**
**Langkah 1: Dapatkan API Key Zapier**
1. Buka [Zapier Developer Platform](https://zapier.com/app/developer).
2. Klik **"API"** → **"Create API Key"**.
3. Salin **API Key** (simpan dengan aman).

**Langkah 2: Tambahkan MCP Server ke MusGo-OS**
- Jika MusGo-OS menggunakan **Python**, gunakan library `mcp` (jika tersedia) atau **panggil via subprocess**:
  ```python
  import subprocess
  import json

  # Konfigurasi MCP Server Zapier
  mcp_command = [
      "npx",
      "@zapier/zapier-sdk-mcp",
      "--api-key=YOUR_ZAPIER_API_KEY"  # Ganti dengan API Key Anda
  ]

  # Jalankan server MCP (akan berjalan di background)
  subprocess.Popen(mcp_command)

  # AI Agent MusGo-OS sekarang bisa berkomunikasi dengan Zapier via MCP
  ```

- Jika MusGo-OS menggunakan **TypeScript/JavaScript**:
  ```typescript
  import { Client } from "@modelcontextprotocol/sdk/client";

  // Inisialisasi klien MCP
  const client = new Client({
      name: "zapier-mcp",
      command: "npx",
      args: ["@zapier/zapier-sdk-mcp", "--api-key=YOUR_ZAPIER_API_KEY"],
  });

  // Hubungkan ke AI Agent MusGo-OS
  await client.connect();
  console.log("✅ MusGo-OS terhubung ke Zapier MCP!");
  ```

**Langkah 3: Uji Koneksi**
- Coba panggil **tool Zapier MCP** dari AI Agent MusGo-OS:
  ```python
  # Contoh: Daftar aplikasi yang terintegrasi
  response = client.call_tool("zapier_list_apps", {})
  print("Aplikasi yang terintegrasi:", response["apps"])
  ```

---

#### **Opsi 2: Menjalankan Server MCP Lokal (Untuk Development)**
**Langkah 1: Instal Package**
```bash
npm install -g @zapier/zapier-sdk-mcp
```

**Langkah 2: Jalankan Server**
```bash
npx @zapier/zapier-sdk-mcp --api-key=YOUR_ZAPIER_API_KEY
```
- Server akan berjalan di `http://localhost:3000/mcp`.

**Langkah 3: Hubungkan ke MusGo-OS**
- Jika MusGo-OS berjalan di **localhost**, AI Agent bisa terhubung ke `http://localhost:3000/mcp`.

---
---

## **🔹 1.3 Supported Clients (Klien yang Didukung)**
### **📌 Daftar Klien MCP yang Kompatibel**
| Klien | Deskripsi | Cara Integrasi ke MusGo-OS |
|-------|-----------|-----------------------------|
| **Claude (Desktop/Code)** | AI Assistant oleh Anthropic | Tambahkan MCP server di `claude-desktop://settings/mcp` |
| **Cursor** | IDE dengan AI built-in | Tambahkan di `cursor://settings/mcp` |
| **VS Code** | Editor kode populer | Gunakan ekstensi **MCP for VS Code** |
| **ChatGPT** | AI oleh OpenAI | Gunakan plugin **Zapier MCP** (jika tersedia) |
| **Custom AI Agent (MusGo-OS)** | AI Agent kustom | Integrasikan via **MCP SDK** (Python/TypeScript) |

---

### **🚀 Contoh Implementasi: MusGo-OS sebagai Custom AI Agent**
**Skenario:**
MusGo-OS ingin **AI Agent-nya** bisa memanggil Zapier MCP untuk **mengotomatiskan tugas**.

**Arsitektur:**
```
User → MusGo-OS AI Agent → (MCP) → Zapier → Aplikasi Eksternal (Google Sheets, Slack, dll.)
```

**Contoh Kode (Python):**
```python
from mcp import Client
import json

class MusGoOS_Agent:
    def __init__(self, zapier_api_key):
        # Inisialisasi klien MCP untuk Zapier
        self.client = Client(
            command="npx",
            args=["@zapier/zapier-sdk-mcp", f"--api-key={zapier_api_key}"]
        )
        self.client.connect()

    def create_zap(self, trigger_app, trigger_event, action_app, action_event):
        """Buat Zap baru via MCP"""
        zap_config = {
            "trigger": {
                "app": trigger_app,  # Misal: "Google Drive"
                "event": trigger_event  # Misal: "New File in Folder"
            },
            "action": {
                "app": action_app,  # Misal: "Slack"
                "event": action_event  # Misal: "Send Channel Message"
            }
        }
        response = self.client.call_tool("zapier_create_zap", zap_config)
        return response

    def list_apps(self):
        """Daftar aplikasi yang terintegrasi dengan Zapier"""
        response = self.client.call_tool("zapier_list_apps", {})
        return response["apps"]

    def run_action(self, app, action, data):
        """Jalankan action langsung (misal: kirim pesan Slack)"""
        response = self.client.call_tool("zapier_run_action", {
            "app": app,
            "action": action,
            "data": data
        })
        return response

# Contoh Penggunaan
if __name__ == "__main__":
    agent = MusGoOS_Agent(zapier_api_key="YOUR_API_KEY")

    # Daftar aplikasi
    apps = agent.list_apps()
    print("Aplikasi yang tersedia:", apps)

    # Buat Zap: Google Drive → Slack
    zap = agent.create_zap(
        trigger_app="Google Drive",
        trigger_event="New File in Folder",
        action_app="Slack",
        action_event="Send Channel Message"
    )
    print("Zap dibuat:", zap)

    # Jalankan action langsung: Kirim pesan ke Slack
    action_result = agent.run_action(
        app="Slack",
        action="Send Channel Message",
        data={
            "channel": "#musgo-updates",
            "text": "File baru terdeteksi di Google Drive!"
        }
    )
    print("Hasil aksi:", action_result)
```

**Penjelasan Kode:**
1. **`MusGoOS_Agent`** adalah kelas yang mewakili **AI Agent** di MusGo-OS.
2. **`create_zap()`** membuat **otomatisasi baru** (Zap) antara 2 aplikasi.
3. **`list_apps()`** mendaftar semua aplikasi yang terintegrasi dengan Zapier.
4. **`run_action()`** menjalankan **tindakan langsung** (misal: kirim pesan Slack).

---
---

## **🔹 1.4 Usage and Billing (Penggunaan & Penagihan)**
### **📌 Paket & Harga**
| Paket | Harga | Panggilan API/Bulan | Rate Limit | Rekomendasi untuk MusGo-OS |
|-------|-------|---------------------|------------|-----------------------------|
| Gratis | $0 | 100 | 60/menit | **Cocok untuk pengembangan** |
| Starter | $20 | 1,000 | 100/menit | **Cocok untuk penggunaan ringan** |
| Professional | $50 | 10,000 | 1,000/menit | **Cocok untuk produksi** |
| Team | $100 | 50,000 | 5,000/menit | **Cocok untuk tim besar** |

---

### **🚀 Contoh Implementasi: Manajemen Kuota API**
**Skenario:**
MusGo-OS ingin **memantau penggunaan API Zapier** agar tidak melebihi kuota.

**Solusi:**
1. **Gunakan Webhook untuk Notifikasi Kuota**
   - Zapier menyediakan **webhook** untuk notifikasi saat kuota hampir habis.
   - MusGo-OS bisa **menerima notifikasi** dan **mengubah perilaku AI Agent** (misal: berhenti memanggil Zapier).

2. **Contoh Kode (Python):**
   ```python
   from flask import Flask, request

   app = Flask(__name__)

   @app.route('/zapier-webhook', methods=['POST'])
   def zapier_webhook():
       data = request.json
       if data.get("event") == "quota_alert":
           print(f"⚠️ Kuota Zapier hampir habis! Sisa: {data['remaining_calls']} panggilan")
           # Lakukan aksi: misal, nonaktifkan fitur otomatisasi
           return {"status": "received"}
       return {"status": "ignored"}

   if __name__ == "__main__":
       app.run(port=5000)
   ```

3. **Konfigurasi Webhook di Zapier:**
   - Buka [Zapier Webhooks](https://zapier.com/app/dashboard) → **"Create Webhook"**.
   - Set URL: `http://musgo-os-server:5000/zapier-webhook`.
   - Pilih event: **"Quota Alert"**.

---
---

## **🔹 1.5 Chatbot Helper (Dukungan AI)**
### **📌 Fitur**
- Zapier menyediakan **AI Chatbot** untuk membantu menjawab pertanyaan seputar MCP.
- Bisa diakses di: [Zapier MCP Chatbot](https://docs.zapier.com/mcp/help/chat-bot.md)

---

### **🚀 Contoh Implementasi: Integrasi Chatbot Zapier ke MusGo-OS**
**Skenario:**
User MusGo-OS ingin **bertanya langsung ke Zapier** tentang cara mengintegrasikan aplikasi.

**Solusi:**
1. **Gunakan API Chatbot Zapier** (jika tersedia).
2. **Atau, integrasikan via MCP**:
   ```python
   def ask_zapier_chatbot(question):
       """Tanya ke Zapier Chatbot via MCP"""
       response = client.call_tool("zapier_chatbot_ask", {
           "question": question
       })
       return response["answer"]

   # Contoh penggunaan
   answer = ask_zapier_chatbot("Bagaimana cara menghubungkan MusGo-OS ke Google Sheets?")
   print(answer)
   ```

---
---

## **🔹 1.6 Community (Komunitas)**
### **📌 Sumber Daya**
| Sumber | Link | Kegunaan untuk MusGo-OS |
|--------|------|-------------------------|
| Zapier Developer Community | [community.zapier.com](https://community.zapier.com/) | Diskusi dengan developer lain |
| GitHub Discussions | [github.com/zapier/zapier-sdk-mcp](https://github.com/zapier/zapier-sdk-mcp/discussions) | Laporkan bug/permintaan fitur |
| Dokumentasi MCP | [docs.zapier.com/mcp](https://docs.zapier.com/mcp/home.md) | Referensi resmi |

---
---
---
# **📌 PART 1: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS 2in1**
---

## **🔥 Kesimpulan Part 1 (Zapier MCP)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Konektivitas ke 9,000+ Aplikasi** | AI Agent bisa berinteraksi dengan Google Drive, Slack, Notion, dll. | ✅ **Siap diimplementasikan** |
| **Bahasa Alami** | User bisa meminta otomatisasi via perintah suara/teks | ✅ **Siap diimplementasikan** |
| **MCP Server** | Integrasi mudah dengan AI Agent MusGo-OS | ✅ **Contoh kode tersedia** |
| **Rate Limiting & Billing** | Kontrol penggunaan API | ⚠️ **Perlu monitoring** |
| **Chatbot Helper** | Dukungan untuk troubleshooting | ✅ **Bisa diintegrasikan** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Daftar Akun Zapier** (jika belum punya).
- [ ] **Dapatkan API Key** dari [Zapier Developer Platform](https://zapier.com/app/developer).
- [ ] **Integrasikan MCP ke MusGo-OS** (gunakan contoh kode di atas).
- [ ] **Uji Koneksi** dengan memanggil `zapier_list_apps`.

### **2. Mid-Term (1 Bulan)**
- [ ] **Buat Zap Pertama** (misal: Google Drive → Slack).
- [ ] **Integrasikan Webhook** untuk monitoring kuota.
- [ ] **Tambahkan Dukungan MCP** ke AI Agent MusGo-OS (jika belum ada).

### **3. Long-Term (3+ Bulan)**
- [ ] **Optimalkan Usage** (gunakan paket berbayar jika diperlukan).
- [ ] **Buat Dokumentasi** untuk user MusGo-OS tentang cara menggunakan Zapier.
- [ ] **Explorasi Fitur Lanjutan** (misal: White Label, Embedded Zap Editor).

---
## **❓ Pertanyaan untuk Dhani**
1. **Apakah MusGo-OS sudah memiliki AI Agent yang mendukung MCP?**
   - Jika **ya**, platform apa yang digunakan (Python, TypeScript, dll.)?
   - Jika **tidak**, apakah Anda ingin saya **memberikan panduan integrasi MCP SDK**?

2. **Aplikasi mana yang ingin diintegrasikan terlebih dahulu?**
   - Contoh: Google Drive, Slack, Notion, Trello, dll.

3. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 2: Zapier SDK** (Untuk akses programatik ke integrasi Zapier)
   - [ ] **Part 3: Integration Builder** (Untuk mempublish MusGo-OS ke Zapier Directory)
   - [ ] **Part 4: Powered by Zapier** (Untuk embedding otomatisasi ke MusGo-OS)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full code untuk Google Drive → Slack)

---
---
**📌 Catatan:**
- Saya akan **menunggu konfirmasi** dari Anda sebelum melanjutkan ke **Part 2**.
- Jika Anda ingin **mendalam ke MCP terlebih dahulu**, saya bisa memberikan:
  - **Full arsitektur integrasi** untuk MusGo-OS.
  - **Contoh kode lengkap** untuk skenario tertentu (misal: Notion + Trello).
  - **Panduan troubleshooting** jika ada error.

---
===========🔐™️®️©️🔐===========

---

### **🔍 Hasil Audit File: `Tech Stack_MusGo-OS 2in1.md`**

---

---

## **📌 1. Ringkasan Isi File**
File ini berisi **rekomendasi tech stack** untuk **MusGo-OS 2in1**, yang terbagi menjadi **4 kategori utama**:
1. **Core Backend Stack** (Python-based)
2. **Frontend Stack** (TypeScript-based)
3. **Desktop App** (Electron/TypeScript)
4. **Mobile Stack** (React Native/Expo)

File ini **belum lengkap** (terpotong di bagian mobile), tetapi sudah memberikan **gambaran jelas** tentang arsitektur yang diusulkan.

---

---

## **🔍 2. Audit & Analisis**

---

### **✅ Kekuatan (Strengths)**
| Kategori | Teknologi | Alasan | Kesesuaian dengan MusGo-OS |
|----------|------------|--------|-----------------------------|
| **Backend** | Python | AI orchestration, async runtime, scalable | ✅ **Sangat cocok** (MusGo-OS adalah AI-native OS) |
| **Backend Framework** | FastAPI | Async-native, OpenAPI, scalable | ✅ **Ideal** untuk AI gateway & realtime orchestration |
| **AI Runtime** | LangGraph, CrewAI, AutoGen, DSPy, Haystack, LlamaIndex, vLLM | Multi-agent, AI orchestration | ✅ **Perfect fit** untuk sovereign AI ecosystem |
| **Queue/Parallel** | Celery, Redis Queue, RabbitMQ, NATS, Kafka | Distributed task queue | ✅ **NATS sangat cocok** untuk MusGo EventBus |
| **Frontend** | TypeScript + Next.js + React | SSR, App Router, Edge-ready | ✅ **Cocok** untuk dashboard & UI kompleks |
| **UI Engine** | TailwindCSS + ShadCN + Framer Motion | Modern, scalable, animated | ✅ **Baik** untuk sovereign UI |
| **Desktop** | Electron + TypeScript | Hybrid OS shell + AI workstation | ✅ **Cocok** untuk desktop environment |
| **Mobile** | React Native + Expo | Cross-platform, TypeScript | ✅ **Baik** untuk mobile extension |

---

### **⚠️ Kekurangan & Rekomendasi Perbaikan**
| Kategori | Isu | Rekomendasi |
|----------|-----|-------------|
| **Backend** | Tidak ada **security hardening** (misal: Zero Trust, mTLS) | ✅ **Tambahkan layer security** (lihat [Part 6](#6-security-hardening)) |
| **Backend** | Tidak ada **runtime isolation** (sandboxing) | ✅ **Gunakan Docker/Kubernetes** untuk isolasi |
| **Backend** | Tidak ada **observability** (logging, monitoring) | ✅ **Tambahkan Prometheus + Grafana** |
| **Backend** | Tidak ada **database** yang disebutkan | ✅ **Tambahkan PostgreSQL + Redis** (lihat [Part 4](#4-database)) |
| **Frontend** | Tidak ada **state management** | ✅ **Gunakan Zustand/Jotai** untuk state global |
| **Frontend** | Tidak ada **real-time communication** | ✅ **Gunakan WebSocket (Socket.IO)** |
| **Desktop** | Electron **berat** (high memory usage) | ⚠️ **Pertimbangkan Tauri + Rust** (jika resource terbatas) |
| **Mobile** | File terpotong (tidak lengkap) | ✅ **Lengkapi dengan detail Expo/React Native** |
| **SDK** | Tidak ada **dual-language SDK** (Python + TypeScript) | ✅ **Buat SDK terpisah** (lihat [Part 5](#5-sdk)) |
| **Event Bus** | NATS disebutkan, tetapi tidak ada **detail arsitektur** | ✅ **Definisikan skema event** (lihat [Part 3](#3-event-bus)) |
| **AI Runtime** | Tidak ada **fallback mechanism** | ✅ **Tambahkan retry + circuit breaker** |
| **Queue** | Tidak ada **prioritization** | ✅ **Gunakan Celery Priority Queue** |

---

### **❌ Kesalahan (Errors)**
| Kategori | Isu | Penjelasan |
|----------|-----|------------|
| **File Structure** | Tidak ada **folder structure** | File ini hanya **daftar teknologi**, bukan **arsitektur lengkap** |
| **Backend** | Tidak ada **microservices breakdown** | Harusnya ada **layer-layer** (misal: API Gateway, Auth Service, AI Orchestrator) |
| **Frontend** | Tidak ada **modular architecture** | Harusnya ada **feature-based modules** (misal: `src/features/dashboard`, `src/features/ai-agent`) |
| **Security** | **Tidak ada security layer** | MusGo-OS **wajib** memiliki Zero Trust, mTLS, RBAC |
| **Deployment** | Tidak ada **deployment strategy** | Harusnya ada **Docker, Kubernetes, CI/CD** |
| **Testing** | Tidak ada **testing framework** | Harusnya ada **Pytest (Python), Jest (TypeScript)** |

---

---

## **🛠️ 3. Rekomendasi Perbaikan (Actionable Items)**

---

### **📌 3.1 Tambahkan Security Hardening**
**Masalah:** File ini **tidak membahas security**, padahal MusGo-OS **wajib secure-by-default**.

**Solusi:**
```markdown
## 6. SECURITY STACK
### Authentication & Authorization
- **OAuth 2.0** (untuk integrasi eksternal)
- **JWT** (untuk internal auth)
- **RBAC (Role-Based Access Control)** (untuk permission management)
- **mTLS** (untuk service-to-service communication)

### Network Security
- **Zero Trust Architecture**
- **API Gateway (Kong/Traefik)** (untuk rate limiting, WAF)
- **mTLS** (untuk internal service communication)
- **VPN/Private Network** (untuk isolasi)

### Runtime Security
- **Docker + Kubernetes** (untuk container isolation)
- **Seccomp + AppArmor** (untuk Linux security)
- **Sandboxing** (untuk AI agent execution)
- **Code Signing** (untuk integritas kode)

### Data Security
- **Encryption at Rest** (AES-256)
- **Encryption in Transit** (TLS 1.3)
- **Secret Management** (HashiCorp Vault / AWS Secrets Manager)
- **Immutable Audit Logs** (untuk compliance)
```

---

### **📌 3.2 Tambahkan Database Layer**
**Masalah:** Tidak ada **database** yang disebutkan.

**Solusi:**
```markdown
## 4. DATABASE STACK
### Primary Database
- **PostgreSQL** (untuk data struktural: user, config, metadata)
- **TimescaleDB** (untuk time-series data: logs, metrics)

### Secondary Database
- **Redis** (untuk caching, session, real-time data)
- **MongoDB** (untuk unstructured data: AI memory, conversation history)

### Search Engine
- **Elasticsearch** (untuk pencarian full-text)
- **Meilisearch** (alternatif ringan)

### Vector Database (untuk AI)
- **Pinecone**
- **Weaviate**
- **Qdrant**
```

---

### **📌 3.3 Tambahkan Event Bus Architecture**
**Masalah:** NATS disebutkan, tetapi **tidak ada skema event**.

**Solusi:**
```markdown
## 3. EVENT BUS ARCHITECTURE
### Broker
- **NATS** (untuk high-throughput, low-latency)
- **Kafka** (untuk event replay & durability)

### Event Schema
```typescript
// Contoh skema event untuk MusGo-OS
interface MusGoEvent {
  id: string; // UUID
  type: "ai_request" | "ai_response" | "user_action" | "system_alert";
  timestamp: Date;
  source: "ai_agent" | "user" | "system";
  payload: any;
  metadata: {
    userId?: string;
    agentId?: string;
    priority: "low" | "medium" | "high" | "critical";
  };
}
```

### Topics
| Topic | Deskripsi | Contoh Event |
|-------|-----------|--------------|
| `ai.request` | Permintaan AI dari user | `{ type: "ai_request", payload: { prompt: "Jelaskan MusGo-OS" } }` |
| `ai.response` | Respon AI | `{ type: "ai_response", payload: { response: "MusGo-OS adalah..." } }` |
| `user.action` | Aksi user (misal: klik tombol) | `{ type: "user_action", payload: { action: "create_zap" } }` |
| `system.alert` | Alert sistem (misal: error) | `{ type: "system_alert", payload: { error: "Database down" } }` |
```

---

### **📌 3.4 Tambahkan SDK (Python + TypeScript)**
**Masalah:** File menyebutkan **"SDK wajib dual-language"**, tetapi **tidak ada detail**.

**Solusi:**
```markdown
## 5. SDK ARCHITECTURE
### Python SDK (`musgo-sdk-py`)
- **Package:** `pip install musgo-sdk`
- **Fitur:**
  - AI Agent Orchestration
  - Event Bus Publisher/Subscriber
  - Database Access Layer
  - Authentication Helper

### TypeScript SDK (`@musgo/sdk`)
- **Package:** `npm install @musgo/sdk`
- **Fitur:**
  - Frontend Integration
  - Real-time Updates (WebSocket)
  - UI Components (React)
  - API Client (untuk backend)

### Contoh Usage (Python)
```python
from musgo_sdk import MusGoClient

client = MusGoClient(api_key="YOUR_API_KEY")

# Panggil AI Agent
response = client.ai.ask(
    agent_id="planner",
    prompt="Buatkan rencana untuk proyek X"
)
print(response)

# Publish Event
client.event.publish(
    topic="ai.request",
    payload={"prompt": "Buatkan rencana..."}
)
```

### Contoh Usage (TypeScript)
```typescript
import { MusGoClient } from "@musgo/sdk";

const client = new MusGoClient({ apiKey: "YOUR_API_KEY" });

// Panggil AI Agent
const response = await client.ai.ask({
  agentId: "planner",
  prompt: "Buatkan rencana untuk proyek X",
});
console.log(response);

// Subscribe ke Event
client.event.subscribe("ai.response", (data) => {
  console.log("AI Response:", data);
});
```
```

---

### **📌 3.5 Tambahkan Deployment & DevOps**
**Masalah:** Tidak ada **deployment strategy**.

**Solusi:**
```markdown
## 7. DEPLOYMENT & DEVOPS
### Infrastructure
- **Containerization:** Docker
- **Orchestration:** Kubernetes (untuk production) / Docker Compose (untuk development)
- **CI/CD:** GitHub Actions / GitLab CI
- **Monitoring:** Prometheus + Grafana
- **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana)

### Environment
| Environment | Deskripsi | Tools |
|-------------|-----------|-------|
| **Development** | Local development | Docker Compose, Hot Reload |
| **Staging** | Testing & QA | Kubernetes (minikube), ArgoCD |
| **Production** | Live system | Kubernetes (EKS/GKE), Terraform |

### CI/CD Pipeline
1. **Build:** Docker image (Python + TypeScript)
2. **Test:** Pytest (Python), Jest (TypeScript)
3. **Deploy:** Kubernetes (Helm Charts)
4. **Monitor:** Prometheus + Grafana
```

---

### **📌 3.6 Tambahkan Testing Framework**
**Masalah:** Tidak ada **testing strategy**.

**Solusi:**
```markdown
## 8. TESTING FRAMEWORK
### Backend (Python)
- **Unit Testing:** `pytest`
- **Integration Testing:** `pytest` + `TestContainers`
- **E2E Testing:** `Selenium` / `Playwright`
- **Load Testing:** `Locust`

### Frontend (TypeScript)
- **Unit Testing:** `Jest` + `React Testing Library`
- **Integration Testing:** `Cypress`
- **E2E Testing:** `Playwright`

### AI Testing
- **Prompt Testing:** `DeepEval` (untuk evaluasi AI response)
- **Agent Testing:** Custom framework (untuk testing AI agent behavior)
```

---

### **📌 3.7 Tambahkan Folder Structure**
**Masalah:** Tidak ada **folder structure** yang jelas.

**Solusi:**
```markdown
## 9. FOLDER STRUCTURE
```
MusGo-OS-2in1/
│
├── backend/                  # Core Backend (Python)
│   ├── app/                  # FastAPI Application
│   │   ├── api/              # API Routes
│   │   ├── core/             # Core Logic (AI Orchestration, Event Bus)
│   │   ├── models/           # Database Models
│   │   ├── services/         # Business Logic
│   │   ├── utils/            # Helper Functions
│   │   └── main.py           # FastAPI Entry Point
│   │
│   ├── tests/                # Backend Tests
│   ├── Dockerfile            # Docker Configuration
│   └── requirements.txt      # Python Dependencies
│
├── frontend/                 # Frontend (TypeScript)
│   ├── apps/                 # Next.js Apps
│   │   ├── dashboard/        # Dashboard UI
│   │   ├── ai-studio/        # AI Agent Studio
│   │   └── ...
│   ├── packages/             # Shared Packages (SDK, UI Components)
│   ├── public/               # Static Files
│   └── Dockerfile            # Docker Configuration
│
├── desktop/                 # Desktop App (Electron)
│   ├── src/                  # Electron Source
│   ├── main/                 # Main Process
│   └── renderer/             # Renderer Process
│
├── mobile/                  # Mobile App (React Native)
│   ├── src/                  # React Native Source
│   └── app.json              # Expo Configuration
│
├── sdk/                     # Dual-Language SDK
│   ├── python/               # Python SDK
│   └── typescript/           # TypeScript SDK
│
├── docs/                    # Documentation
├── scripts/                 # Deployment & CI/CD Scripts
└── docker-compose.yml       # Local Development
```
```

---
---
---

## **📜 4. Versi Perbaikan (Improved Tech Stack File)**
Berikut adalah **versi lengkap dan diperbaiki** dari file `Tech Stack_MusGo-OS 2in1.md` dengan **semua rekomendasi di atas**:

---

```markdown
# 🚀 MusGo-OS 2in1 — RECOMMENDED TECH STACK (IMPROVED)

---

## 📌 1. CORE BACKEND STACK
**Dominan: PYTHON**
**Alasan:** MusGo-OS adalah **AI-native operating ecosystem**, bukan web app biasa.
Python unggul untuk:
- AI orchestration
- Agent runtime
- Multimodel routing
- Automation
- Infrastructure
- Async orchestration
- Data pipeline
- AI memory
- ML runtime
- Distributed executor

---

### 🔹 Backend Framework
| Teknologi | Kegunaan | Alasan |
|-----------|----------|--------|
| **FastAPI** | Primary Framework | Async-native, cepat, modern, OpenAPI auto, scalable |
| **Uvicorn** | ASGI Server | High-performance untuk FastAPI |
| **Gunicorn** | WSGI Server | Fallback untuk production |

---

### 🔹 AI Runtime
| Teknologi | Kegunaan |
|-----------|----------|
| **LangGraph** | Multi-agent orchestration |
| **CrewAI** | AI agent collaboration |
| **AutoGen** | Conversational AI |
| **DSPy** | Programmatic AI |
| **Haystack** | Search & QA |
| **LlamaIndex** | Data indexing untuk LLM |
| **vLLM** | LLM inference optimization |

---

### 🔹 Queue / Parallel Runtime
| Teknologi | Kegunaan | Catatan |
|-----------|----------|--------|
| **Celery** | Task queue | Untuk background jobs |
| **Redis Queue** | Simple queue | Untuk task sederhana |
| **RabbitMQ** | Message broker | Untuk reliability |
| **NATS** | High-performance messaging | **Rekomendasi untuk MusGo EventBus** |
| **Kafka** | Event streaming | Untuk event replay & durability |

---

## 📌 2. FRONTEND STACK
**Dominan: TYPESCRIPT**
**Alasan:** Frontend ecosystem MusGo-OS besar, meliputi:
- Desktop shell
- Realtime overlay
- AI live guide
- Persona UI
- Avatar runtime
- Workflow studio
- Creator studio
- Template marketplace
- Dashboard
- Sovereign browser

---

### 🔹 Web Frontend
| Teknologi | Kegunaan | Alasan |
|-----------|----------|--------|
| **Next.js** | Framework | SSR, App Router, Edge-ready |
| **React** | UI Library | Ecosystem besar |
| **TypeScript** | Language | Type safety |

---

### 🔹 UI Engine
| Teknologi | Kegunaan |
|-----------|----------|
| **TailwindCSS** | Styling |
| **ShadCN** | UI Components |
| **Framer Motion** | Animasi |

---
---

## 📌 3. EVENT BUS ARCHITECTURE
### Broker
- **NATS** (Rekomendasi utama untuk MusGo-OS)
- **Kafka** (Untuk event replay & durability)

### Event Schema
```typescript
interface MusGoEvent {
  id: string; // UUID
  type: "ai_request" | "ai_response" | "user_action" | "system_alert" | "agent_coordination";
  timestamp: Date;
  source: "ai_agent" | "user" | "system" | "external_app";
  payload: any;
  metadata: {
    userId?: string;
    agentId?: string;
    priority: "low" | "medium" | "high" | "critical";
    correlationId?: string; // Untuk tracking request-response
  };
}
```

### Topics
| Topic | Deskripsi | Contoh Event |
|-------|-----------|--------------|
| `ai.request` | Permintaan AI dari user | `{ type: "ai_request", payload: { prompt: "Jelaskan MusGo-OS" } }` |
| `ai.response` | Respon AI | `{ type: "ai_response", payload: { response: "MusGo-OS adalah..." } }` |
| `user.action` | Aksi user | `{ type: "user_action", payload: { action: "create_workflow" } }` |
| `system.alert` | Alert sistem | `{ type: "system_alert", payload: { error: "Database down" } }` |
| `agent.coordination` | Koordinasi antar agent | `{ type: "agent_coordination", payload: { agent1: "planner", agent2: "executor" } }` |

---
---

## 📌 4. DATABASE STACK
### Primary Database
| Teknologi | Kegunaan |
|-----------|----------|
| **PostgreSQL** | Data struktural (user, config, metadata) |
| **TimescaleDB** | Time-series data (logs, metrics) |

### Secondary Database
| Teknologi | Kegunaan |
|-----------|----------|
| **Redis** | Caching, session, real-time data |
| **MongoDB** | Unstructured data (AI memory, conversation history) |

### Search Engine
| Teknologi | Kegunaan |
|-----------|----------|
| **Elasticsearch** | Full-text search |
| **Meilisearch** | Alternatif ringan |

### Vector Database (untuk AI)
| Teknologi | Kegunaan |
|-----------|----------|
| **Pinecone** | Vector similarity search |
| **Weaviate** | Vector + structured data |
| **Qdrant** | Open-source vector DB |

---
---

## 📌 5. SDK ARCHITECTURE
### Python SDK (`musgo-sdk-py`)
- **Package:** `pip install musgo-sdk`
- **Fitur:**
  - AI Agent Orchestration
  - Event Bus Publisher/Subscriber
  - Database Access Layer
  - Authentication Helper

### TypeScript SDK (`@musgo/sdk`)
- **Package:** `npm install @musgo/sdk`
- **Fitur:**
  - Frontend Integration
  - Real-time Updates (WebSocket)
  - UI Components (React)
  - API Client (untuk backend)

### Contoh Usage (Python)
```python
from musgo_sdk import MusGoClient

client = MusGoClient(api_key="YOUR_API_KEY")

# Panggil AI Agent
response = client.ai.ask(
    agent_id="planner",
    prompt="Buatkan rencana untuk proyek X"
)
print(response)

# Publish Event
client.event.publish(
    topic="ai.request",
    payload={"prompt": "Buatkan rencana..."}
)
```

### Contoh Usage (TypeScript)
```typescript
import { MusGoClient } from "@musgo/sdk";

const client = new MusGoClient({ apiKey: "YOUR_API_KEY" });

// Panggil AI Agent
const response = await client.ai.ask({
  agentId: "planner",
  prompt: "Buatkan rencana untuk proyek X",
});
console.log(response);

// Subscribe ke Event
client.event.subscribe("ai.response", (data) => {
  console.log("AI Response:", data);
});
```

---
---

## 📌 6. SECURITY STACK
### Authentication & Authorization
| Teknologi | Kegunaan |
|-----------|----------|
| **OAuth 2.0** | Integrasi eksternal |
| **JWT** | Internal authentication |
| **RBAC** | Role-Based Access Control |
| **mTLS** | Service-to-service authentication |

### Network Security
| Teknologi | Kegunaan |
|-----------|----------|
| **Zero Trust Architecture** | Security model |
| **API Gateway (Kong/Traefik)** | Rate limiting, WAF |
| **mTLS** | Internal service communication |
| **VPN/Private Network** | Isolasi jaringan |

### Runtime Security
| Teknologi | Kegunaan |
|-----------|----------|
| **Docker + Kubernetes** | Container isolation |
| **Seccomp + AppArmor** | Linux security |
| **Sandboxing** | AI agent execution isolation |
| **Code Signing** | Integritas kode |

### Data Security
| Teknologi | Kegunaan |
|-----------|----------|
| **AES-256** | Encryption at rest |
| **TLS 1.3** | Encryption in transit |
| **HashiCorp Vault** | Secret management |
| **Immutable Audit Logs** | Compliance |

---
---

## 📌 7. DEPLOYMENT & DEVOPS
### Infrastructure
| Teknologi | Kegunaan |
|-----------|----------|
| **Docker** | Containerization |
| **Kubernetes** | Orchestration (production) |
| **Docker Compose** | Orchestration (development) |
| **GitHub Actions** | CI/CD |
| **Prometheus + Grafana** | Monitoring |
| **ELK Stack** | Logging |

### Environment
| Environment | Deskripsi | Tools |
|-------------|-----------|-------|
| **Development** | Local development | Docker Compose, Hot Reload |
| **Staging** | Testing & QA | Kubernetes (minikube), ArgoCD |
| **Production** | Live system | Kubernetes (EKS/GKE), Terraform |

---
---

## 📌 8. TESTING FRAMEWORK
### Backend (Python)
| Teknologi | Kegunaan |
|-----------|----------|
| **pytest** | Unit & Integration Testing |
| **TestContainers** | Database Testing |
| **Selenium** | E2E Testing |
| **Locust** | Load Testing |

### Frontend (TypeScript)
| Teknologi | Kegunaan |
|-----------|----------|
| **Jest** | Unit Testing |
| **React Testing Library** | Component Testing |
| **Cypress** | Integration Testing |
| **Playwright** | E2E Testing |

### AI Testing
| Teknologi | Kegunaan |
|-----------|----------|
| **DeepEval** | Evaluasi AI response |
| **Custom Framework** | Testing AI agent behavior |

---
---

## 📌 9. FOLDER STRUCTURE
```
MusGo-OS-2in1/
│
├── backend/                  # Core Backend (Python)
│   ├── app/                  # FastAPI Application
│   │   ├── api/              # API Routes
│   │   │   ├── v1/           # API Version 1
│   │   │   └── ...
│   │   ├── core/             # Core Logic
│   │   │   ├── ai/           # AI Orchestration
│   │   │   ├── event_bus/    # Event Bus (NATS)
│   │   │   └── ...
│   │   ├── models/           # Database Models
│   │   ├── services/         # Business Logic
│   │   ├── utils/            # Helper Functions
│   │   └── main.py           # FastAPI Entry Point
│   │
│   ├── tests/                # Backend Tests
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── Dockerfile            # Docker Configuration
│   ├── requirements.txt      # Python Dependencies
│   └── pyproject.toml        # Python Project Config
│
├── frontend/                 # Frontend (TypeScript)
│   ├── apps/                 # Next.js Apps
│   │   ├── dashboard/        # Dashboard UI
│   │   ├── ai-studio/        # AI Agent Studio
│   │   ├── workflow-builder/ # Workflow Builder
│   │   └── ...
│   ├── packages/             # Shared Packages
│   │   ├── @musgo/sdk/       # TypeScript SDK
│   │   ├── @musgo/ui/        # UI Components
│   │   └── ...
│   ├── public/               # Static Files
│   ├── Dockerfile            # Docker Configuration
│   └── next.config.js        # Next.js Config
│
├── desktop/                 # Desktop App (Electron)
│   ├── src/                  # Electron Source
│   │   ├── main/             # Main Process
│   │   └── renderer/          # Renderer Process
│   ├── package.json          # Electron Config
│   └── Dockerfile            # Docker Configuration
│
├── mobile/                  # Mobile App (React Native)
│   ├── src/                  # React Native Source
│   ├── app.json              # Expo Configuration
│   └── package.json          # Dependencies
│
├── sdk/                     # Dual-Language SDK
│   ├── python/               # Python SDK
│   │   ├── musgo_sdk/        # SDK Package
│   │   └── setup.py          # Python Package Config
│   └── typescript/           # TypeScript SDK
│       ├── src/              # SDK Source
│       └── package.json      # npm Package Config
│
├── docs/                    # Documentation
│   ├── architecture/        # Architecture Docs
│   ├── api/                  # API Documentation
│   └── guides/               # User Guides
│
├── scripts/                 # Deployment & CI/CD Scripts
│   ├── deploy.sh            # Deployment Script
│   └── ci-cd/               # CI/CD Configurations
│
├── docker-compose.yml       # Local Development
└── README.md                # Project Overview
```

---
---
---
## **🔥 5. Kesimpulan & Actionable Items**
---

### **✅ Kekuatan File Asli**
- **Tech stack sudah matang** (Python + TypeScript + FastAPI + Next.js).
- **AI Runtime sudah lengkap** (LangGraph, CrewAI, dll.).
- **Queue/Parallel Runtime sudah tercover** (NATS, Kafka, dll.).

---

### **⚠️ Perbaikan yang Diperlukan**
| Kategori | Isu | Status |
|----------|-----|--------|
| **Security** | Tidak ada security layer | ❌ **Kritikal** (Wajib ditambahkan) |
| **Database** | Tidak ada database definition | ❌ **Kritikal** (Wajib ditambahkan) |
| **Event Bus** | Tidak ada skema event | ⚠️ **Penting** (Rekomendasi: Tambahkan) |
| **SDK** | Tidak ada detail SDK | ⚠️ **Penting** (Rekomendasi: Tambahkan) |
| **Deployment** | Tidak ada deployment strategy | ⚠️ **Penting** (Rekomendasi: Tambahkan) |
| **Testing** | Tidak ada testing framework | ⚠️ **Penting** (Rekomendasi: Tambahkan) |
| **Folder Structure** | Tidak ada struktur folder | ⚠️ **Penting** (Rekomendasi: Tambahkan) |

---
### **🛠️ Langkah Selanjutnya untuk MusGo-OS**
1. **Perbaiki File `Tech Stack_MusGo-OS 2in1.md`**
   - Tambahkan **semua bagian yang hilang** (Security, Database, Event Bus, SDK, dll.).
   - Gunakan **versi perbaikan** yang saya berikan di atas.

2. **Implementasikan Security Layer**
   - Mulai dengan **OAuth 2.0 + JWT + RBAC**.
   - Tambahkan **mTLS** untuk internal service communication.

3. **Definisikan Database Schema**
   - Buat **PostgreSQL schema** untuk user, config, metadata.
   - Tambahkan **Redis** untuk caching & real-time data.

4. **Buat SDK (Python + TypeScript)**
   - Mulai dengan **Python SDK** (untuk backend).
   - Lalu **TypeScript SDK** (untuk frontend).

5. **Setup Deployment Pipeline**
   - Gunakan **Docker + Kubernetes** untuk production.
   - Gunakan **GitHub Actions** untuk CI/CD.

---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda setuju dengan perbaikan yang saya usulkan?**
   - Jika **ya**, saya bisa **mengupdate file `Tech Stack_MusGo-OS 2in1.md`** dengan versi perbaikan.
   - Jika **tidak**, silakan beritahu bagian mana yang ingin diubah.

2. **Apakah Anda ingin saya:**
   - [ ] **Mengupdate file asli** dengan versi perbaikan?
   - [ ] **Menambahkan detail lain** (misal: contoh kode untuk FastAPI + Next.js)?
   - [ ] **Fokus pada salah satu bagian** (misal: Security, Database, dll.)?

3. **Apakah ada tech stack lain yang ingin ditambahkan?**
   - Contoh: **Blockchain** (untuk decentralized identity), **WebAssembly** (untuk performance), dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Fokus ke ekstraksi dokumentasi Zapier ke bahasa Indonesia dengan contoh implementasi untuk MusGo-OS 2in1**.

Saya akan **melanjutkan dari Part 1 (Zapier MCP)** dan **menerjemahkan + menerapkan contoh-contoh relevan** untuk MusGo-OS **secara bertahap**.

---
---

# **📜 MUSGO-OS 2in1: PANDUAN INTEGRASI ZAPIER (PART 1 - ZAPIER MCP)**
*Terjemahan + Implementasi untuk MusGo-OS*

---

---

## **🔹 1.1 Overview Zapier MCP (Model Context Protocol)**
### **📌 Penjelasan (Bahasa Indonesia)**
Zapier MCP adalah **server Model Context Protocol (MCP)** yang memungkinkan **AI Agent MusGo-OS** untuk **berinteraksi dengan 9,000+ aplikasi eksternal** (Google Drive, Slack, Notion, Trello, dll.) **tanpa perlu coding manual**.

**MCP bertindak sebagai jembatan** antara:
- **AI Agent MusGo-OS** (sebagai *brain*)
- **Zapier** (sebagai *hub integrasi*)
- **Aplikasi Eksternal** (sebagai *tools*)

**Manfaat untuk MusGo-OS:**
✅ **AI Agent bisa memanggil trigger** (pemicu otomatisasi).
✅ **AI Agent bisa menjalankan action** (tindakan otomatis).
✅ **Semua interaksi dilakukan via bahasa alami** (natural language).
✅ **Tidak perlu membangun integrasi dari nol** (hemat waktu & biaya).

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: Otomatisasi Notifikasi Slack**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, kirim notifikasi ke channel #musgo-updates di Slack jika ada file baru di folder 'Proyek MusGo-OS' di Google Drive."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima input user.
2. **AI Agent menggunakan Zapier MCP** untuk:
   - Mendaftar aplikasi yang terintegrasi (Google Drive, Slack).
   - Membuat **Zap** (otomatisasi) yang memantau folder Google Drive.
   - Menjalankan **Zap** saat file baru terdeteksi.

**Arsitektur:**
```
User → MusGo-OS AI Agent → (MCP) → Zapier → Google Drive (Trigger) → Slack (Action)
```

**Contoh Perintah AI Agent:**
```python
# Pseudocode untuk MusGo-OS AI Agent
def handle_user_request(user_input):
    if "kirim notifikasi ke Slack" in user_input and "file baru di Google Drive" in user_input:
        # Panggil Zapier MCP untuk membuat Zap
        zap = zapier_mcp.create_zap(
            trigger={
                "app": "Google Drive",
                "event": "New File in Folder",
                "folder": "Proyek MusGo-OS"
            },
            action={
                "app": "Slack",
                "event": "Send Channel Message",
                "channel": "#musgo-updates",
                "message": "File baru terdeteksi: {file_name}"
            }
        )
        return f"✅ Zap dibuat! Notifikasi Slack akan dikirim saat ada file baru di Google Drive."

    return "Maaf, saya tidak mengerti perintah Anda."
```

---

#### **Use-Case 2: Sinkronisasi Data ke Notion**
**Skenario:**
User berkata:
> *"MusGo, catat di database Notion 'Tugas Selesai' setiap kali saya menandai tugas sebagai 'Done' di Trello."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** mendengar perintah user.
2. **AI Agent menggunakan Zapier MCP** untuk:
   - Mendapatkan daftar **board Trello** user.
   - Membuat **Zap** yang memantau perubahan status tugas di Trello.
   - Menambahkan **baris baru** di database Notion saat tugas ditandai "Done".

**Arsitektur:**
```
User → MusGo-OS AI Agent → (MCP) → Zapier → Trello (Trigger) → Notion (Action)
```

**Contoh Perintah AI Agent:**
```python
def handle_user_request(user_input):
    if "catat di Notion" in user_input and "tugas sebagai 'Done' di Trello" in user_input:
        # Panggil Zapier MCP untuk membuat Zap
        zap = zapier_mcp.create_zap(
            trigger={
                "app": "Trello",
                "event": "Card Moved to List",
                "list": "Done"
            },
            action={
                "app": "Notion",
                "event": "Create Database Row",
                "database": "Tugas Selesai",
                "data": {
                    "Nama Tugas": "{card_name}",
                    "Tanggal Selesai": "{current_time}",
                    "Board": "{board_name}"
                }
            }
        )
        return f"✅ Zap dibuat! Data akan otomatis tersinkron ke Notion."

    return "Maaf, saya tidak mengerti perintah Anda."
```

---
---

## **🔹 1.2 Quickstart Zapier MCP (Langkah-langkah untuk MusGo-OS)**
### **📌 Persyaratan**
| Persyaratan | Deskripsi | Status untuk MusGo-OS |
|-------------|-----------|----------------------|
| **Akun Zapier** | Gratis/berbayar | ✅ **Wajib** (Daftar di [zapier.com](https://zapier.com)) |
| **AI Agent MCP-Compatible** | MusGo-OS harus mendukung MCP | ✅ **Wajib** (Jika belum, perlu integrasi MCP SDK) |
| **Node.js 18+** | Untuk menjalankan server MCP lokal | ⚠️ **Opsional** (Jika menggunakan Zapier MCP Server) |
| **API Key Zapier** | Untuk autentikasi | ✅ **Wajib** (Dapatkan di [Zapier API Settings](https://zapier.com/app/developer)) |

---

### **🚀 Contoh Implementasi: Menghubungkan MusGo-OS ke Zapier MCP**
#### **Opsi 1: Menggunakan Zapier MCP Server (Rekomendasi)**
**Langkah 1: Dapatkan API Key Zapier**
1. Buka [Zapier Developer Platform](https://zapier.com/app/developer).
2. Klik **"API"** → **"Create API Key"**.
3. Salin **API Key** (simpan dengan aman di **MusGo-OS Config**).

**Langkah 2: Tambahkan MCP Server ke MusGo-OS (Python)**
```python
import subprocess
from musgo_os.core.ai_agent import MusGoAIAgent

class ZapierMCPClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.process = None

    def start_mcp_server(self):
        """Jalankan server MCP Zapier"""
        self.process = subprocess.Popen([
            "npx",
            "@zapier/zapier-sdk-mcp",
            f"--api-key={self.api_key}"
        ])
        print("✅ Zapier MCP Server berjalan di background.")

    def stop_mcp_server(self):
        """Hentikan server MCP Zapier"""
        if self.process:
            self.process.terminate()
            print("❌ Zapier MCP Server dihentikan.")

# Integrasikan ke MusGo-OS AI Agent
class MusGoAIAgent:
    def __init__(self):
        self.zapier_mcp = ZapierMCPClient(api_key="YOUR_ZAPIER_API_KEY")
        self.zapier_mcp.start_mcp_server()

    def handle_request(self, user_input):
        # Contoh: Buat Zap Google Drive → Slack
        if "kirim notifikasi ke Slack" in user_input:
            # Panggil Zapier MCP untuk membuat Zap
            # (Asumsikan sudah terhubung via MCP)
            return "✅ Zap Google Drive → Slack dibuat!"

        return "Maaf, saya tidak mengerti."

# Inisialisasi
ai_agent = MusGoAIAgent()
```

**Langkah 3: Uji Koneksi**
```python
# Contoh: Daftar aplikasi yang terintegrasi
apps = ai_agent.zapier_mcp.list_apps()
print("Aplikasi yang tersedia:", apps)

# Contoh: Buat Zap
zap = ai_agent.zapier_mcp.create_zap(
    trigger={"app": "Google Drive", "event": "New File"},
    action={"app": "Slack", "event": "Send Message"}
)
print("Zap dibuat:", zap)
```

---
#### **Opsi 2: Menjalankan Server MCP Lokal (Untuk Development)**
**Langkah 1: Instal Package**
```bash
npm install -g @zapier/zapier-sdk-mcp
```

**Langkah 2: Jalankan Server**
```bash
npx @zapier/zapier-sdk-mcp --api-key=YOUR_ZAPIER_API_KEY
```
- Server akan berjalan di `http://localhost:3000/mcp`.

**Langkah 3: Hubungkan ke MusGo-OS**
- Jika MusGo-OS berjalan di **localhost**, AI Agent bisa terhubung ke `http://localhost:3000/mcp`.

---
---

## **🔹 1.3 Supported Clients (Klien yang Didukung)**
### **📌 Daftar Klien MCP yang Kompatibel**
| Klien | Deskripsi | Cara Integrasi ke MusGo-OS |
|-------|-----------|-----------------------------|
| **Claude (Desktop/Code)** | AI Assistant oleh Anthropic | Tambahkan MCP server di `claude-desktop://settings/mcp` |
| **Cursor** | IDE dengan AI built-in | Tambahkan di `cursor://settings/mcp` |
| **VS Code** | Editor kode populer | Gunakan ekstensi **MCP for VS Code** |
| **ChatGPT** | AI oleh OpenAI | Gunakan plugin **Zapier MCP** (jika tersedia) |
| **Custom AI Agent (MusGo-OS)** | AI Agent kustom | **Integrasikan via MCP SDK** (Python/TypeScript) |

---
### **🚀 Contoh Implementasi: MusGo-OS sebagai Custom AI Agent**
**Skenario:**
MusGo-OS ingin **AI Agent-nya** bisa memanggil Zapier MCP untuk **mengotomatiskan tugas**.

**Arsitektur:**
```
User → MusGo-OS AI Agent → (MCP) → Zapier → Aplikasi Eksternal
```

**Contoh Kode (Python - Full Implementation):**
```python
from musgo_os.core.mcp_client import MCPClient
from musgo_os.core.ai_agent import BaseAIAgent
import json

class ZapierMCPClient(MCPClient):
    """Klien MCP khusus untuk Zapier"""
    def __init__(self, api_key):
        super().__init__(
            command="npx",
            args=["@zapier/zapier-sdk-mcp", f"--api-key={api_key}"]
        )

    def list_apps(self):
        """Daftar aplikasi yang terintegrasi dengan Zapier"""
        response = self.call_tool("zapier_list_apps", {})
        return response.get("apps", [])

    def create_zap(self, trigger, action):
        """Buat Zap baru"""
        zap_config = {
            "trigger": trigger,
            "action": action
        }
        response = self.call_tool("zapier_create_zap", zap_config)
        return response

    def run_action(self, app, action, data):
        """Jalankan action langsung (misal: kirim pesan Slack)"""
        response = self.call_tool("zapier_run_action", {
            "app": app,
            "action": action,
            "data": data
        })
        return response

class MusGoAIAgent(BaseAIAgent):
    """AI Agent MusGo-OS dengan integrasi Zapier MCP"""
    def __init__(self, zapier_api_key):
        super().__init__()
        self.zapier = ZapierMCPClient(zapier_api_key)

    def handle_user_request(self, user_input):
        """Proses input user dan jalankan aksi via Zapier MCP"""
        user_input = user_input.lower()

        # Contoh 1: Buat Zap Google Drive → Slack
        if "kirim notifikasi ke slack" in user_input and "file baru di google drive" in user_input:
            zap = self.zapier.create_zap(
                trigger={
                    "app": "Google Drive",
                    "event": "New File in Folder",
                    "folder": "Proyek MusGo-OS"
                },
                action={
                    "app": "Slack",
                    "event": "Send Channel Message",
                    "channel": "#musgo-updates",
                    "message": "File baru terdeteksi: {file_name}"
                }
            )
            return f"✅ Zap dibuat! Notifikasi Slack akan dikirim saat ada file baru di Google Drive."

        # Contoh 2: Daftar aplikasi yang tersedia
        elif "aplikasi apa saja yang bisa diintegrasikan" in user_input:
            apps = self.zapier.list_apps()
            return f"📋 Aplikasi yang tersedia: {', '.join(apps)}"

        # Contoh 3: Kirim pesan Slack langsung
        elif "kirim pesan ke slack" in user_input:
            channel = "#musgo-updates"
            message = "Ini pesan tes dari MusGo-OS!"
            result = self.zapier.run_action(
                app="Slack",
                action="Send Channel Message",
                data={"channel": channel, "text": message}
            )
            return f"✅ Pesan dikirim ke {channel}: {message}"

        # Default: Tidak mengerti
        else:
            return "Maaf, saya tidak mengerti perintah Anda. Coba lagi!"

# Contoh Penggunaan
if __name__ == "__main__":
    # Inisialisasi AI Agent dengan API Key Zapier
    ai_agent = MusGoAIAgent(zapier_api_key="YOUR_ZAPIER_API_KEY")

    # Simulasi input user
    user_inputs = [
        "MusGo, kirim notifikasi ke Slack jika ada file baru di Google Drive",
        "MusGo, aplikasi apa saja yang bisa diintegrasikan?",
        "MusGo, kirim pesan ke Slack"
    ]

    for input_text in user_inputs:
        print(f"\n👤 User: {input_text}")
        response = ai_agent.handle_user_request(input_text)
        print(f"🤖 MusGo-OS: {response}")
```

**Output Contoh:**
```
👤 User: MusGo, kirim notifikasi ke Slack jika ada file baru di Google Drive
🤖 MusGo-OS: ✅ Zap dibuat! Notifikasi Slack akan dikirim saat ada file baru di Google Drive.

👤 User: MusGo, aplikasi apa saja yang bisa diintegrasikan?
🤖 MusGo-OS: 📋 Aplikasi yang tersedia: Google Drive, Slack, Notion, Trello, Gmail, ...

👤 User: MusGo, kirim pesan ke Slack
🤖 MusGo-OS: ✅ Pesan dikirim ke #musgo-updates: Ini pesan tes dari MusGo-OS!
```

---
---

## **🔹 1.4 Usage and Billing (Penggunaan & Penagihan)**
### **📌 Paket & Harga**
| Paket | Harga | Panggilan API/Bulan | Rate Limit | Rekomendasi untuk MusGo-OS |
|-------|-------|---------------------|------------|-----------------------------|
| **Gratis** | $0 | 100 | 60/menit | ✅ **Cocok untuk pengembangan** |
| **Starter** | $20 | 1,000 | 100/menit | ✅ **Cocok untuk penggunaan ringan** |
| **Professional** | $50 | 10,000 | 1,000/menit | ✅ **Cocok untuk produksi** |
| **Team** | $100 | 50,000 | 5,000/menit | ✅ **Cocok untuk tim besar** |

---
### **🚀 Contoh Implementasi: Manajemen Kuota API**
**Skenario:**
MusGo-OS ingin **memantau penggunaan API Zapier** agar tidak melebihi kuota.

**Solusi:**
1. **Gunakan Webhook untuk Notifikasi Kuota**
   - Zapier menyediakan **webhook** untuk notifikasi saat kuota hampir habis.
   - MusGo-OS bisa **menerima notifikasi** dan **mengubah perilaku AI Agent** (misal: berhenti memanggil Zapier).

2. **Contoh Kode (Python):**
```python
from flask import Flask, request
from musgo_os.core.zapier_mcp import ZapierMCPClient

app = Flask(__name__)
zapier = ZapierMCPClient(api_key="YOUR_API_KEY")

@app.route('/zapier-webhook', methods=['POST'])
def zapier_webhook():
    """Terima notifikasi dari Zapier (misal: kuota hampir habis)"""
    data = request.json

    if data.get("event") == "quota_alert":
        remaining_calls = data.get("remaining_calls", 0)
        print(f"⚠️ Kuota Zapier hampir habis! Sisa: {remaining_calls} panggilan")

        # Nonaktifkan fitur otomatisasi jika kuota < 10
        if remaining_calls < 10:
            zapier.disable_auto_features()
            print("❌ Fitur otomatisasi dinonaktifkan karena kuota hampir habis.")

        return {"status": "received"}

    return {"status": "ignored"}

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
```

3. **Konfigurasi Webhook di Zapier:**
   - Buka [Zapier Webhooks](https://zapier.com/app/dashboard) → **"Create Webhook"**.
   - Set URL: `http://musgo-os-server:5000/zapier-webhook`.
   - Pilih event: **"Quota Alert"**.

---
---

## **🔹 1.5 Chatbot Helper (Dukungan AI)**
### **📌 Fitur**
- Zapier menyediakan **AI Chatbot** untuk membantu menjawab pertanyaan seputar MCP.
- Bisa diakses di: [Zapier MCP Chatbot](https://docs.zapier.com/mcp/help/chat-bot.md)

---
### **🚀 Contoh Implementasi: Integrasi Chatbot Zapier ke MusGo-OS**
**Skenario:**
User MusGo-OS ingin **bertanya langsung ke Zapier** tentang cara mengintegrasikan aplikasi.

**Solusi:**
1. **Gunakan API Chatbot Zapier** (jika tersedia).
2. **Atau, integrasikan via MCP:**
```python
class MusGoAIAgent:
    # ... (kode sebelumnya)

    def ask_zapier_chatbot(self, question):
        """Tanya ke Zapier Chatbot via MCP"""
        response = self.zapier.call_tool("zapier_chatbot_ask", {
            "question": question
        })
        return response.get("answer", "Maaf, tidak ada jawaban.")

    def handle_user_request(self, user_input):
        # ... (kode sebelumnya)

        # Contoh: Tanya ke Zapier Chatbot
        elif "tanya ke zapier" in user_input.lower():
            question = user_input.replace("tanya ke zapier", "").strip()
            answer = self.ask_zapier_chatbot(question)
            return f"💡 Jawaban dari Zapier: {answer}"

# Contoh penggunaan
ai_agent = MusGoAIAgent(zapier_api_key="YOUR_API_KEY")
print(ai_agent.handle_user_request("MusGo, tanya ke Zapier: Bagaimana cara menghubungkan ke Google Sheets?"))
```

---
---
---
# **📌 PART 1: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 1 (Zapier MCP)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Konektivitas ke 9,000+ Aplikasi** | AI Agent bisa berinteraksi dengan Google Drive, Slack, Notion, dll. | ✅ **Siap diimplementasikan** |
| **Bahasa Alami** | User bisa meminta otomatisasi via perintah suara/teks | ✅ **Siap diimplementasikan** |
| **MCP Server** | Integrasi mudah dengan AI Agent MusGo-OS | ✅ **Contoh kode tersedia** |
| **Rate Limiting & Billing** | Kontrol penggunaan API | ⚠️ **Perlu monitoring** |
| **Chatbot Helper** | Dukungan untuk troubleshooting | ✅ **Bisa diintegrasikan** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Daftar Akun Zapier** (jika belum punya) → [Daftar di sini](https://zapier.com/sign-up).
- [ ] **Dapatkan API Key** dari [Zapier Developer Platform](https://zapier.com/app/developer).
- [ ] **Integrasikan MCP ke MusGo-OS** (gunakan contoh kode di atas).
- [ ] **Uji Koneksi** dengan memanggil `zapier.list_apps()`.

### **2. Mid-Term (1 Bulan)**
- [ ] **Buat Zap Pertama** (misal: Google Drive → Slack).
- [ ] **Integrasikan Webhook** untuk monitoring kuota.
- [ ] **Tambahkan Dukungan MCP** ke AI Agent MusGo-OS (jika belum ada).

---
## **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 2: Zapier SDK** (Untuk akses programatik ke integrasi Zapier)
   - [ ] **Part 3: Integration Builder** (Untuk mempublish MusGo-OS ke Zapier Directory)
   - [ ] **Part 4: Powered by Zapier** (Untuk embedding otomatisasi ke MusGo-OS)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full code untuk Google Drive → Notion)

2. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Google Drive → Notion**, **Slack → Trello**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 2: Zapier SDK** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi** untuk **MusGo-OS 2in1** dari dokumentasi **Zapier SDK**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN ZAPIER SDK (PART 2)**
*Terjemahan + Implementasi untuk Integrasi Programatik*

---

---

## **🔹 2.1 Overview Zapier SDK**
### **📌 Penjelasan (Bahasa Indonesia)**
**Zapier SDK** adalah **TypeScript SDK dan CLI** yang memungkinkan **developer** (atau **AI Agent MusGo-OS**) untuk **mengakses 9,000+ integrasi Zapier secara programatik**. SDK ini **menangani autentikasi, token, dan retry**, sehingga Anda **tidak perlu repot** dengan detail teknis.

**Kegunaan untuk MusGo-OS:**
✅ **AI Agent MusGo-OS** bisa **memanggil aplikasi eksternal** (Google Sheets, Slack, dll.) **tanpa perlu membuat integrasi dari nol**.
✅ **Backend MusGo-OS** bisa **menjalankan otomatisasi** (Zaps) **via kode**.
✅ **Frontend MusGo-OS** bisa **berinteraksi dengan Zapier** untuk **mengelola koneksi dan otomatisasi**.

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: AI Agent Menjalankan Action Zapier**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, buatkan tugas baru di Trello dengan judul 'Implementasi MCP' dan deskripsi 'Integrasikan Zapier MCP ke MusGo-OS'."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima input user.
2. **AI Agent menggunakan Zapier SDK** untuk:
   - **Mencari board Trello** user.
   - **Membuat kartu (card) baru** di board yang dipilih.

**Arsitektur:**
```
User → MusGo-OS AI Agent → Zapier SDK → Trello API → Buat Kartu Baru
```

**Contoh Kode (TypeScript):**
```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";

// Inisialisasi SDK
const zapier = new ZapierSDK({
  apiKey: "YOUR_ZAPIER_API_KEY",
});

// Fungsi untuk membuat kartu Trello
async function createTrelloCard(title: string, description: string, boardId: string, listId: string) {
  try {
    // Panggil action Trello via Zapier SDK
    const result = await zapier.actions.run({
      app: "Trello",
      action: "Create Card",
      data: {
        title,
        description,
        boardId,
        listId,
      },
    });
    return result;
  } catch (error) {
    console.error("Gagal membuat kartu Trello:", error);
    throw error;
  }
}

// Contoh penggunaan di MusGo-OS AI Agent
async function handleUserRequest(userInput: string) {
  if (userInput.includes("buatkan tugas baru di Trello")) {
    // Extract judul dan deskripsi dari input user
    const titleMatch = userInput.match(/judul '([^']+)'/);
    const descMatch = userInput.match(/deskripsi '([^']+)'/);

    if (titleMatch && descMatch) {
      const title = titleMatch[1];
      const description = descMatch[1];

      // Ambil board dan list default (misal: dari config MusGo-OS)
      const boardId = "TRELLO_BOARD_ID";
      const listId = "TRELLO_LIST_ID";

      // Buat kartu baru
      const card = await createTrelloCard(title, description, boardId, listId);
      return `✅ Tugas "${title}" dibuat di Trello!`;
    }
  }
  return "Maaf, saya tidak mengerti perintah Anda.";
}

// Simulasi
handleUserRequest("MusGo, buatkan tugas baru di Trello dengan judul 'Implementasi MCP' dan deskripsi 'Integrasikan Zapier MCP ke MusGo-OS'")
  .then(console.log);
```

**Output:**
```
✅ Tugas "Implementasi MCP" dibuat di Trello!
```

---

#### **Use-Case 2: Backend MusGo-OS Menjalankan Zap**
**Skenario:**
Backend MusGo-OS ingin **menjalankan Zap** (otomatisasi) **setiap kali user menyimpan file di Google Drive**.

**Cara Kerja:**
1. **Backend MusGo-OS** mendeteksi **file baru** di Google Drive (via webhook atau polling).
2. **Backend menggunakan Zapier SDK** untuk **menjalankan Zap** yang sudah dibuat.

**Arsitektur:**
```
Google Drive (Webhook) → MusGo-OS Backend → Zapier SDK → Jalankan Zap → Slack (Kirim Notifikasi)
```

**Contoh Kode (Python):**
```python
from zapier_sdk import ZapierClient

# Inisialisasi client
zapier = ZapierClient(api_key="YOUR_ZAPIER_API_KEY")

def run_zap(zap_id: str, data: dict):
    """Jalankan Zap yang sudah dibuat"""
    try:
        result = zapier.zaps.run(zap_id=zap_id, data=data)
        return result
    except Exception as e:
        print(f"Gagal menjalankan Zap: {e}")
        raise

# Contoh: Jalankan Zap saat file baru di Google Drive
def on_new_google_drive_file(file_data: dict):
    # Zap ID: Otomatisasi Google Drive → Slack
    zap_id = "ZAP_ID_GOOGLE_DRIVE_TO_SLACK"

    # Data untuk Zap (misal: nama file)
    data = {
        "file_name": file_data["name"],
        "file_url": file_data["url"],
    }

    # Jalankan Zap
    result = run_zap(zap_id, data)
    print(f"✅ Zap berjalan! Notifikasi Slack dikirim untuk file: {file_data['name']}")
    return result

# Simulasi
file_data = {
    "name": "laporan_proyek.pdf",
    "url": "https://drive.google.com/file/d/12345",
}
on_new_google_drive_file(file_data)
```

**Output:**
```
✅ Zap berjalan! Notifikasi Slack dikirim untuk file: laporan_proyek.pdf
```

---
---

## **🔹 2.2 Quickstart Zapier SDK**
### **📌 Persyaratan**
| Persyaratan | Deskripsi | Status untuk MusGo-OS |
|-------------|-----------|----------------------|
| **Node.js 18+** | Runtime untuk SDK | ✅ **Wajib** (Untuk TypeScript) |
| **Python 3.8+** | Runtime untuk SDK (jika menggunakan Python) | ✅ **Wajib** (Untuk Backend) |
| **Akun Zapier** | Gratis/berbayar | ✅ **Wajib** |
| **API Key Zapier** | Untuk autentikasi | ✅ **Wajib** |

---

### **🚀 Langkah-langkah Instalasi & Setup**
#### **1. Instalasi SDK (TypeScript)**
```bash
# Instal package Zapier SDK
npm install @zapier/zapier-sdk

# Atau, jika menggunakan yarn
yarn add @zapier/zapier-sdk
```

#### **2. Instalasi SDK (Python)**
```bash
pip install zapier-sdk
```

---
#### **3. Inisialisasi SDK (TypeScript)**
```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";

// Inisialisasi dengan API Key
const zapier = new ZapierSDK({
  apiKey: "YOUR_ZAPIER_API_KEY",
});

// Contoh: Daftar aplikasi yang terintegrasi
async function listApps() {
  const apps = await zapier.apps.list();
  console.log("Aplikasi yang tersedia:", apps);
}

listApps();
```

#### **4. Inisialisasi SDK (Python)**
```python
from zapier_sdk import ZapierClient

# Inisialisasi dengan API Key
zapier = ZapierClient(api_key="YOUR_ZAPIER_API_KEY")

# Contoh: Daftar aplikasi yang terintegrasi
apps = zapier.apps.list()
print("Aplikasi yang tersedia:", apps)
```

---
---

## **🔹 2.3 API Reference (Referensi API Zapier SDK)**
Zapier SDK menyediakan **beberapa method utama** untuk berinteraksi dengan Zapier. Berikut **method-method yang relevan untuk MusGo-OS**:

---

### **📌 1. Apps (Daftar Aplikasi)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `apps.list()` | Daftar semua aplikasi yang terintegrasi | `const apps = await zapier.apps.list();` |
| `apps.get(appKey)` | Dapatkan detail aplikasi | `const app = await zapier.apps.get("slack");` |
| `apps.search(query)` | Cari aplikasi | `const results = await zapier.apps.search("google");` |

**Contoh untuk MusGo-OS:**
```typescript
// Daftar aplikasi yang terintegrasi dengan MusGo-OS
async function listIntegratedApps() {
  const apps = await zapier.apps.list();
  const integratedApps = apps.filter(app =>
    ["slack", "google_drive", "notion", "trello"].includes(app.key)
  );
  return integratedApps;
}

listIntegratedApps().then(console.log);
```

---
### **📌 2. Actions (Menjalankan Tindakan)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `actions.list(appKey)` | Daftar action yang tersedia untuk aplikasi | `const actions = await zapier.actions.list("slack");` |
| `actions.run(app, action, data)` | Jalankan action | `await zapier.actions.run("slack", "Send Channel Message", { channel: "#musgo", text: "Halo!" });` |
| `actions.get(app, action)` | Dapatkan detail action | `const action = await zapier.actions.get("slack", "Send Channel Message");` |

**Contoh untuk MusGo-OS:**
```typescript
// Kirim pesan ke Slack via Zapier SDK
async function sendSlackMessage(channel: string, text: string) {
  const result = await zapier.actions.run("slack", "Send Channel Message", {
    channel,
    text,
  });
  return result;
}

// Contoh penggunaan
sendSlackMessage("#musgo-updates", "MusGo-OS sedang berjalan!")
  .then(console.log);
```

---
### **📌 3. Triggers (Pemicu Otomatisasi)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `triggers.list(appKey)` | Daftar trigger yang tersedia | `const triggers = await zapier.triggers.list("google_drive");` |
| `triggers.test(app, trigger, data)` | Uji trigger | `await zapier.triggers.test("google_drive", "New File", { folder: "Proyek" });` |

**Contoh untuk MusGo-OS:**
```typescript
// Daftar trigger Google Drive
async function listGoogleDriveTriggers() {
  const triggers = await zapier.triggers.list("google_drive");
  return triggers;
}

listGoogleDriveTriggers().then(console.log);
```

---
### **📌 4. Zaps (Otomatisasi)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `zaps.list()` | Daftar semua Zap user | `const zaps = await zapier.zaps.list();` |
| `zaps.get(zapId)` | Dapatkan detail Zap | `const zap = await zapier.zaps.get("ZAP_ID");` |
| `zaps.run(zapId, data)` | Jalankan Zap | `await zapier.zaps.run("ZAP_ID", { file_name: "test.pdf" });` |
| `zaps.create(config)` | Buat Zap baru | `await zapier.zaps.create({ trigger: {...}, action: {...} });` |
| `zaps.delete(zapId)` | Hapus Zap | `await zapier.zaps.delete("ZAP_ID");` |

**Contoh untuk MusGo-OS:**
```typescript
// Buat Zap baru: Google Drive → Slack
async function createGoogleDriveToSlackZap(folder: string, channel: string) {
  const zap = await zapier.zaps.create({
    trigger: {
      app: "google_drive",
      event: "New File in Folder",
      data: { folder },
    },
    action: {
      app: "slack",
      event: "Send Channel Message",
      data: {
        channel,
        text: `File baru terdeteksi: {file_name}`,
      },
    },
  });
  return zap;
}

// Contoh penggunaan
createGoogleDriveToSlackZap("Proyek MusGo-OS", "#musgo-updates")
  .then((zap) => console.log("✅ Zap dibuat:", zap.id));
```

---
### **📌 5. Authentications (Autentikasi)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `auth.list()` | Daftar semua koneksi autentikasi | `const auths = await zapier.auth.list();` |
| `auth.create(appKey, credentials)` | Buat koneksi autentikasi baru | `await zapier.auth.create("slack", { token: "SLACK_TOKEN" });` |
| `auth.delete(authId)` | Hapus koneksi autentikasi | `await zapier.auth.delete("AUTH_ID");` |

**Contoh untuk MusGo-OS:**
```typescript
// Daftar koneksi autentikasi yang sudah terhubung
async function listConnectedApps() {
  const auths = await zapier.auth.list();
  return auths.map(auth => ({
    app: auth.app,
    status: auth.status,
  }));
}

listConnectedApps().then(console.log);
```

---
### **📌 6. Webhooks (Untuk Real-Time Updates)**
| Method | Deskripsi | Contoh Penggunaan (TypeScript) |
|--------|-----------|--------------------------------|
| `webhooks.create(url, event)` | Buat webhook | `await zapier.webhooks.create("https://musgo-os.com/webhook", "zap.turned_on");` |
| `webhooks.list()` | Daftar webhook | `const webhooks = await zapier.webhooks.list();` |
| `webhooks.delete(webhookId)` | Hapus webhook | `await zapier.webhooks.delete("WEBHOOK_ID");` |

**Contoh untuk MusGo-OS:**
```typescript
// Buat webhook untuk menerima notifikasi saat Zap dijalankan
async function createZapRunWebhook(url: string) {
  const webhook = await zapier.webhooks.create(url, "zap.run");
  return webhook;
}

// Contoh penggunaan
createZapRunWebhook("https://musgo-os.com/api/zapier-webhook")
  .then((webhook) => console.log("✅ Webhook dibuat:", webhook.id));
```

---
---
---

## **🔹 2.4 CLI Reference (Command Line Interface)**
Zapier SDK juga menyediakan **CLI** untuk **mengelola integrasi, testing, dan deployment** dari terminal.

---
### **📌 Instalasi CLI**
```bash
npm install -g @zapier/zapier-sdk-cli
```

---
### **📌 Perintah CLI yang Relevan untuk MusGo-OS**
| Perintah | Deskripsi | Contoh |
|----------|-----------|--------|
| `zapier apps:list` | Daftar aplikasi | `zapier apps:list` |
| `zapier apps:search <query>` | Cari aplikasi | `zapier apps:search slack` |
| `zapier actions:list <app>` | Daftar action untuk aplikasi | `zapier actions:list slack` |
| `zapier actions:run <app> <action> --data <data>` | Jalankan action | `zapier actions:run slack "Send Channel Message" --data '{"channel": "#musgo", "text": "Halo!"}'` |
| `zapier zaps:list` | Daftar Zap | `zapier zaps:list` |
| `zapier zaps:run <zapId> --data <data>` | Jalankan Zap | `zapier zaps:run ZAP_ID --data '{"file_name": "test.pdf"}'` |
| `zapier auth:list` | Daftar koneksi autentikasi | `zapier auth:list` |
| `zapier auth:create <app>` | Buat koneksi autentikasi | `zapier auth:create slack` |

---
### **🚀 Contoh Penggunaan CLI untuk MusGo-OS**
#### **1. Daftar Aplikasi yang Terintegrasi**
```bash
zapier apps:list
```
**Output:**
```
google_drive
slack
notion
trello
gmail
...
```

#### **2. Jalankan Action Slack (Kirim Pesan)**
```bash
zapier actions:run slack "Send Channel Message" --data '{
  "channel": "#musgo-updates",
  "text": "MusGo-OS sedang berjalan!"
}'
```
**Output:**
```
✅ Pesan dikirim ke #musgo-updates: "MusGo-OS sedang berjalan!"
```

#### **3. Daftar Zap yang Ada**
```bash
zapier zaps:list
```
**Output:**
```
ID: ZAP_123
Name: Google Drive → Slack
Status: Active

ID: ZAP_456
Name: Trello → Notion
Status: Active
...
```

#### **4. Jalankan Zap (Google Drive → Slack)**
```bash
zapier zaps:run ZAP_123 --data '{
  "file_name": "laporan_proyek.pdf",
  "file_url": "https://drive.google.com/file/d/12345"
}'
```
**Output:**
```
✅ Zap ZAP_123 berjalan! Notifikasi Slack dikirim.
```

---
---
---

## **🔹 2.5 Contoh Implementasi Lengkap untuk MusGo-OS**
### **📌 Skenario: MusGo-OS AI Agent + Zapier SDK**
**Deskripsi:**
AI Agent MusGo-OS akan **menerima perintah user** dan **menjalankan aksi via Zapier SDK**.

---
#### **1. Setup Proyek (TypeScript)**
```bash
# Buat proyek baru
mkdir musgo-zapier-integration
cd musgo-zapier-integration
npm init -y

# Instal dependencies
npm install @zapier/zapier-sdk typescript ts-node @types/node

# Buat file tsconfig.json
npx tsc --init
```

---
#### **2. Kode Utama (`index.ts`)**
```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";

// Inisialisasi Zapier SDK
const zapier = new ZapierSDK({
  apiKey: process.env.ZAPIER_API_KEY || "YOUR_ZAPIER_API_KEY",
});

// Class untuk MusGo-OS AI Agent
class MusGoAIAgent {
  // Daftar aplikasi yang didukung
  private supportedApps = [
    "slack",
    "google_drive",
    "notion",
    "trello",
    "gmail",
  ];

  // Daftar perintah yang didukung
  private commands = {
    slack: {
      sendMessage: async (channel: string, text: string) => {
        return await zapier.actions.run("slack", "Send Channel Message", {
          channel,
          text,
        });
      },
    },
    google_drive: {
      listFiles: async (folder?: string) => {
        return await zapier.actions.run("google_drive", "List Files", {
          folder,
        });
      },
    },
    trello: {
      createCard: async (title: string, description: string, boardId: string, listId: string) => {
        return await zapier.actions.run("trello", "Create Card", {
          title,
          description,
          boardId,
          listId,
        });
      },
    },
    notion: {
      createPage: async (databaseId: string, properties: any) => {
        return await zapier.actions.run("notion", "Create Database Row", {
          databaseId,
          properties,
        });
      },
    },
    zaps: {
      create: async (trigger: any, action: any) => {
        return await zapier.zaps.create({ trigger, action });
      },
      run: async (zapId: string, data: any) => {
        return await zapier.zaps.run(zapId, data);
      },
    },
  };

  // Proses input user
  async handleCommand(command: string): Promise<string> {
    command = command.toLowerCase();

    // 1. Kirim pesan ke Slack
    if (command.includes("kirim pesan ke slack")) {
      const channelMatch = command.match(/ke channel (\S+)/);
      const textMatch = command.match(/pesan "([^"]+)"/);

      if (channelMatch && textMatch) {
        const channel = channelMatch[1];
        const text = textMatch[1];
        await this.commands.slack.sendMessage(channel, text);
        return `✅ Pesan dikirim ke ${channel}: "${text}"`;
      }
    }

    // 2. Buat kartu Trello
    else if (command.includes("buatkan tugas di trello")) {
      const titleMatch = command.match(/judul "([^"]+)"/);
      const descMatch = command.match(/deskripsi "([^"]+)"/);

      if (titleMatch && descMatch) {
        const title = titleMatch[1];
        const description = descMatch[1];
        const boardId = "TRELLO_BOARD_ID"; // Ganti dengan ID board Trello
        const listId = "TRELLO_LIST_ID";   // Ganti dengan ID list Trello
        await this.commands.trello.createCard(title, description, boardId, listId);
        return `✅ Tugas "${title}" dibuat di Trello!`;
      }
    }

    // 3. Daftar file di Google Drive
    else if (command.includes("daftar file di google drive")) {
      const folderMatch = command.match(/di folder "([^"]+)"/);
      const folder = folderMatch ? folderMatch[1] : undefined;
      const files = await this.commands.google_drive.listFiles(folder);
      return `📁 File di Google Drive: ${JSON.stringify(files)}`;
    }

    // 4. Buat Zap baru
    else if (command.includes("buatkan zap")) {
      if (command.includes("google drive ke slack")) {
        const folderMatch = command.match(/folder "([^"]+)"/);
        const channelMatch = command.match(/ke channel (\S+)/);

        if (folderMatch && channelMatch) {
          const folder = folderMatch[1];
          const channel = channelMatch[1];
          const zap = await this.commands.zaps.create(
            {
              app: "google_drive",
              event: "New File in Folder",
              data: { folder },
            },
            {
              app: "slack",
              event: "Send Channel Message",
              data: {
                channel,
                text: `File baru terdeteksi: {file_name}`,
              },
            }
          );
          return `✅ Zap dibuat! ID: ${zap.id}`;
        }
      }
    }

    // 5. Jalankan Zap
    else if (command.includes("jalankan zap")) {
      const zapIdMatch = command.match(/zap (\S+)/);
      if (zapIdMatch) {
        const zapId = zapIdMatch[1];
        const dataMatch = command.match(/dengan data "([^"]+)"/);
        const data = dataMatch ? JSON.parse(dataMatch[1]) : {};
        await this.commands.zaps.run(zapId, data);
        return `✅ Zap ${zapId} berjalan!`;
      }
    }

    // 6. Daftar aplikasi yang terintegrasi
    else if (command.includes("aplikasi apa saja yang terintegrasi")) {
      const apps = await zapier.apps.list();
      const supportedApps = apps.filter(app => this.supportedApps.includes(app.key));
      return `📋 Aplikasi yang terintegrasi: ${supportedApps.map(app => app.name).join(", ")}`;
    }

    // Default: Tidak mengerti
    return "Maaf, saya tidak mengerti perintah Anda. Coba lagi!";
  }
}

// Contoh penggunaan
async function main() {
  const aiAgent = new MusGoAIAgent();

  // Simulasi input user
  const commands = [
    "MusGo, kirim pesan ke Slack ke channel #musgo-updates dengan pesan \"MusGo-OS sedang berjalan!\"",
    "MusGo, buatkan tugas di Trello dengan judul \"Implementasi MCP\" dan deskripsi \"Integrasikan Zapier MCP ke MusGo-OS\"",
    "MusGo, daftar file di Google Drive di folder \"Proyek MusGo-OS\"",
    "MusGo, buatkan Zap Google Drive ke Slack dengan folder \"Proyek MusGo-OS\" ke channel #musgo-updates",
    "MusGo, jalankan Zap ZAP_123 dengan data \"{\\\"file_name\\\": \\\"test.pdf\\\"}\"",
    "MusGo, aplikasi apa saja yang terintegrasi?",
  ];

  for (const command of commands) {
    console.log(`\n👤 User: ${command}`);
    const response = await aiAgent.handleCommand(command);
    console.log(`🤖 MusGo-OS: ${response}`);
  }
}

main().catch(console.error);
```

---
#### **3. Output Contoh**
```
👤 User: MusGo, kirim pesan ke Slack ke channel #musgo-updates dengan pesan "MusGo-OS sedang berjalan!"
🤖 MusGo-OS: ✅ Pesan dikirim ke #musgo-updates: "MusGo-OS sedang berjalan!"

👤 User: MusGo, buatkan tugas di Trello dengan judul "Implementasi MCP" dan deskripsi "Integrasikan Zapier MCP ke MusGo-OS"
🤖 MusGo-OS: ✅ Tugas "Implementasi MCP" dibuat di Trello!

👤 User: MusGo, daftar file di Google Drive di folder "Proyek MusGo-OS"
🤖 MusGo-OS: 📁 File di Google Drive: [{"name": "laporan.pdf", "url": "..."}, ...]

👤 User: MusGo, buatkan Zap Google Drive ke Slack dengan folder "Proyek MusGo-OS" ke channel #musgo-updates
🤖 MusGo-OS: ✅ Zap dibuat! ID: ZAP_789

👤 User: MusGo, jalankan Zap ZAP_123 dengan data "{\"file_name\": \"test.pdf\"}"
🤖 MusGo-OS: ✅ Zap ZAP_123 berjalan!

👤 User: MusGo, aplikasi apa saja yang terintegrasi?
🤖 MusGo-OS: 📋 Aplikasi yang terintegrasi: Slack, Google Drive, Notion, Trello, Gmail
```

---
---
---

## **🔹 2.6 Best Practices untuk MusGo-OS**
### **📌 1. Error Handling**
**Masalah:** Zapier SDK bisa **gagal** (misal: API limit, autentikasi gagal, dll.).
**Solusi:** Gunakan **try-catch** dan **retry mechanism**.

**Contoh (TypeScript):**
```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";

const zapier = new ZapierSDK({ apiKey: "YOUR_API_KEY" });

// Fungsi dengan error handling
async function runActionWithRetry(
  app: string,
  action: string,
  data: any,
  maxRetries: number = 3
): Promise<any> {
  let lastError: Error;

  for (let i = 0; i < maxRetries; i++) {
    try {
      return await zapier.actions.run(app, action, data);
    } catch (error) {
      lastError = error as Error;
      console.warn(`⚠️ Percobaan ${i + 1} gagal: ${error.message}`);
      if (i < maxRetries - 1) {
        await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1))); // Tunggu 1-3 detik
      }
    }
  }

  throw new Error(`❌ Gagal setelah ${maxRetries} percobaan: ${lastError.message}`);
}

// Contoh penggunaan
runActionWithRetry("slack", "Send Channel Message", {
  channel: "#musgo-updates",
  text: "Pesan penting!",
})
  .then(console.log)
  .catch(console.error);
```

---
### **📌 2. Rate Limiting**
**Masalah:** Zapier memiliki **rate limit** (misal: 60 panggilan/menit untuk akun gratis).
**Solusi:** Gunakan **queue** (antrian) untuk **membatasi panggilan**.

**Contoh (TypeScript + P-Queue):**
```bash
npm install p-queue
```

```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";
import PQueue from "p-queue";

const zapier = new ZapierSDK({ apiKey: "YOUR_API_KEY" });

// Buat queue dengan concurrency 1 (1 panggilan per waktu)
const queue = new PQueue({ concurrency: 1 });

// Fungsi untuk menjalankan action dengan queue
async function runActionInQueue(app: string, action: string, data: any) {
  return queue.add(async () => {
    return await zapier.actions.run(app, action, data);
  });
}

// Contoh penggunaan
for (let i = 0; i < 10; i++) {
  runActionInQueue("slack", "Send Channel Message", {
    channel: "#musgo-updates",
    text: `Pesan ke-${i}`,
  });
}
```

---
### **📌 3. Logging & Monitoring**
**Masalah:** Sulit **debug** jika tidak ada logging.
**Solusi:** Gunakan **logger** (misal: `winston` atau `pino`).

**Contoh (TypeScript + Winston):**
```bash
npm install winston
```

```typescript
import { ZapierSDK } from "@zapier/zapier-sdk";
import winston from "winston";

// Setup logger
const logger = winston.createLogger({
  level: "info",
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "musgo-zapier.log" }),
  ],
});

const zapier = new ZapierSDK({ apiKey: "YOUR_API_KEY" });

// Fungsi dengan logging
async function runActionWithLogging(app: string, action: string, data: any) {
  logger.info(`🚀 Menjalankan action: ${app}.${action}`, { data });

  try {
    const result = await zapier.actions.run(app, action, data);
    logger.info(`✅ Action berhasil: ${app}.${action}`, { result });
    return result;
  } catch (error) {
    logger.error(`❌ Action gagal: ${app}.${action}`, { error: error.message, data });
    throw error;
  }
}

// Contoh penggunaan
runActionWithLogging("slack", "Send Channel Message", {
  channel: "#musgo-updates",
  text: "Pesan dengan logging!",
});
```

---
### **📌 4. Environment Variables**
**Masalah:** **API Key** tidak boleh **hardcoded**.
**Solusi:** Gunakan **environment variables** (`.env`).

**Contoh:**
1. Buat file `.env`:
   ```env
   ZAPIER_API_KEY=your_api_key_here
   ```

2. Gunakan `dotenv` di kode:
   ```bash
   npm install dotenv
   ```

3. Load environment variables:
   ```typescript
   import { ZapierSDK } from "@zapier/zapier-sdk";
   import dotenv from "dotenv";

   dotenv.config();

   const zapier = new ZapierSDK({
     apiKey: process.env.ZAPIER_API_KEY,
   });
   ```

---
### **📌 5. Type Safety (TypeScript)**
**Masalah:** Zapier SDK **tidak selalu type-safe**.
**Solusi:** Buat **type definitions** untuk data yang dikirim.

**Contoh:**
```typescript
// Definisikan type untuk Slack action
interface SlackSendMessageData {
  channel: string;
  text: string;
  username?: string;
  icon_emoji?: string;
}

// Definisikan type untuk Trello action
interface TrelloCreateCardData {
  title: string;
  description: string;
  boardId: string;
  listId: string;
}

// Fungsi dengan type safety
async function sendSlackMessage(data: SlackSendMessageData) {
  return await zapier.actions.run("slack", "Send Channel Message", data);
}

async function createTrelloCard(data: TrelloCreateCardData) {
  return await zapier.actions.run("trello", "Create Card", data);
}

// Contoh penggunaan
sendSlackMessage({
  channel: "#musgo-updates",
  text: "Pesan dengan type safety!",
});
```

---
---
---

## **📌 PART 2: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

### **🔥 Kesimpulan Part 2 (Zapier SDK)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Akses Programatik ke 9,000+ Aplikasi** | AI Agent/Backend bisa menjalankan aksi tanpa coding manual | ✅ **Siap diimplementasikan** |
| **TypeScript & Python SDK** | Fleksibel untuk frontend & backend | ✅ **Contoh kode tersedia** |
| **CLI untuk Manajemen** | Mudah mengelola integrasi dari terminal | ✅ **Siap digunakan** |
| **Error Handling & Retry** | Tangani kegagalan dengan baik | ✅ **Contoh tersedia** |
| **Rate Limiting** | Hindari melebihi kuota API | ✅ **Contoh dengan P-Queue** |
| **Logging & Monitoring** | Debug dan pantau penggunaan | ✅ **Contoh dengan Winston** |

---

### **🛠️ Langkah Selanjutnya untuk MusGo-OS**
#### **1. Short-Term (1-2 Minggu)**
- [ ] **Instal Zapier SDK** (`npm install @zapier/zapier-sdk`).
- [ ] **Dapatkan API Key Zapier** (jika belum punya).
- [ ] **Integrasikan SDK ke MusGo-OS AI Agent** (gunakan contoh kode di atas).
- [ ] **Uji Koneksi** dengan memanggil `zapier.apps.list()`.

#### **2. Mid-Term (1 Bulan)**
- [ ] **Buat fungsi-fungsi utama** (kirim Slack, buat Trello card, dll.).
- [ ] **Tambahkan error handling & retry**.
- [ ] **Implementasikan rate limiting** (gunakan P-Queue).
- [ ] **Setup logging** (gunakan Winston).

#### **3. Long-Term (3+ Bulan)**
- [ ] **Buat abstraksi layer** untuk Zapier SDK (misal: `MusGoZapierClient`).
- [ ] **Integrasikan dengan Event Bus MusGo-OS** (untuk real-time updates).
- [ ] **Optimalkan performa** (caching, batch processing).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 3: Integration Builder** (Untuk mempublish MusGo-OS ke Zapier Directory)
   - [ ] **Part 4: Powered by Zapier** (Untuk embedding otomatisasi ke MusGo-OS)
   - [ ] **Part 5: White Label** (Untuk branding MusGo-OS sendiri)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + Notion)

2. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Google Drive → Notion**, **Slack → Trello**, dll.

3. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi API untuk MusGo-OS + Zapier**?
   - [ ] **Contoh deployment (Docker, Kubernetes)**?

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 3: Integration Builder** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi** untuk **MusGo-OS 2in1** dari dokumentasi **Zapier Integration Builder**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN INTEGRATION BUILDER (PART 3)**
*Terjemahan + Implementasi untuk Membangun Integrasi Kustom di Zapier*

---

---

## **🔹 3.1 Overview Integration Builder**
### **📌 Penjelasan (Bahasa Indonesia)**
**Zapier Integration Builder** adalah **platform** yang memungkinkan **developer** (atau **MusGo-OS**) untuk **membuat integrasi kustom** yang bisa dipublish ke **Zapier App Directory**. Dengan Integration Builder, Anda bisa:
✅ **Membuat trigger** (pemicu otomatisasi, misal: "File baru di Google Drive").
✅ **Membuat action** (tindakan otomatis, misal: "Kirim pesan ke Slack").
✅ **Mengelola autentikasi** (OAuth, API Key, dll.).
✅ **Mempublish integrasi** ke Zapier App Directory (untuk digunakan oleh user lain).

**Manfaat untuk MusGo-OS:**
- **MusGo-OS bisa menjadi aplikasi yang terintegrasi dengan Zapier** (seperti Slack, Google Drive, dll.).
- **User MusGo-OS bisa membuat Zap yang melibatkan MusGo-OS** (misal: "Jika AI Agent MusGo-OS menyelesaikan tugas → Kirim notifikasi ke Slack").
- **MusGo-OS bisa menawarkan fitur otomatisasi** kepada user Zapier.

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: MusGo-OS sebagai Trigger (Pemicu Otomatisasi)**
**Skenario:**
User Zapier ingin **membuat Zap** yang **berjalan saat AI Agent MusGo-OS menyelesaikan tugas**.

**Cara Kerja:**
1. **MusGo-OS** mendaftarkan **trigger** di Zapier (misal: `musgo_os.task_completed`).
2. **User Zapier** membuat **Zap** dengan trigger `musgo_os.task_completed`.
3. **Saat AI Agent MusGo-OS menyelesaikan tugas**, Zapier **menerima event** dan **menjalankan action** (misal: kirim email, simpan ke Google Sheets).

**Arsitektur:**
```
MusGo-OS (Trigger) → Zapier → Slack/Email/Google Sheets (Action)
```

**Contoh Skema Trigger:**
```json
{
  "name": "Task Completed",
  "key": "task_completed",
  "description": "Triggered when an AI Agent in MusGo-OS completes a task.",
  "operation": {
    "type": "trigger",
    "perform": {
      "type": "polling",  // Atau "hook" (webhook)
      "url": "https://musgo-os.com/api/zapier/triggers/task_completed",
      "method": "GET",
      "interval": 300  // Polling setiap 5 menit (untuk polling)
    },
    "inputFields": [
      {
        "key": "taskId",
        "type": "string",
        "required": false,
        "helpText": "ID of the completed task."
      },
      {
        "key": "agentId",
        "type": "string",
        "required": false,
        "helpText": "ID of the AI Agent that completed the task."
      }
    ],
    "outputFields": [
      {
        "key": "taskId",
        "type": "string",
        "helpText": "ID of the completed task."
      },
      {
        "key": "taskName",
        "type": "string",
        "helpText": "Name of the completed task."
      },
      {
        "key": "agentId",
        "type": "string",
        "helpText": "ID of the AI Agent."
      },
      {
        "key": "completionTime",
        "type": "datetime",
        "helpText": "When the task was completed."
      }
    ]
  }
}
```

---
#### **Use-Case 2: MusGo-OS sebagai Action (Tindakan Otomatis)**
**Skenario:**
User Zapier ingin **membuat Zap** yang **memanggil AI Agent MusGo-OS untuk menjalankan tugas**.

**Cara Kerja:**
1. **MusGo-OS** mendaftarkan **action** di Zapier (misal: `musgo_os.run_agent`).
2. **User Zapier** membuat **Zap** dengan action `musgo_os.run_agent`.
3. **Saat Zap dijalankan**, Zapier **memanggil MusGo-OS API** untuk menjalankan AI Agent.

**Arsitektur:**
```
Google Drive (Trigger) → Zapier → MusGo-OS (Action: Run AI Agent)
```

**Contoh Skema Action:**
```json
{
  "name": "Run AI Agent",
  "key": "run_agent",
  "description": "Run a MusGo-OS AI Agent with a prompt.",
  "operation": {
    "type": "action",
    "perform": {
      "type": "request",
      "method": "POST",
      "url": "https://musgo-os.com/api/zapier/actions/run_agent",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "prompt": "{{prompt}}",
        "agentId": "{{agentId}}"
      }
    },
    "inputFields": [
      {
        "key": "prompt",
        "type": "text",
        "required": true,
        "helpText": "The prompt for the AI Agent."
      },
      {
        "key": "agentId",
        "type": "string",
        "required": true,
        "helpText": "ID of the AI Agent to run.",
        "default": "planner"  // Default agent
      }
    ],
    "outputFields": [
      {
        "key": "response",
        "type": "text",
        "helpText": "The response from the AI Agent."
      },
      {
        "key": "agentId",
        "type": "string",
        "helpText": "ID of the AI Agent that generated the response."
      },
      {
        "key": "timestamp",
        "type": "datetime",
        "helpText": "When the AI Agent was run."
      }
    ]
  }
}
```

---
---
---

## **🔹 3.2 Getting Started (Memulai dengan Integration Builder)**
### **📌 Persyaratan**
| Persyaratan | Deskripsi | Status untuk MusGo-OS |
|-------------|-----------|----------------------|
| **Akun Zapier Developer** | Akun untuk membuat integrasi | ✅ **Wajib** (Daftar di [Zapier Developer Platform](https://zapier.com/developer)) |
| **Aplikasi MusGo-OS** | Backend MusGo-OS yang berjalan | ✅ **Wajib** |
| **API MusGo-OS** | Endpoint untuk Zapier | ✅ **Wajib** (Misal: `/api/zapier/triggers`, `/api/zapier/actions`) |
| **Dokumentasi API** | Dokumentasi untuk Zapier | ⚠️ **Rekomendasi** |

---

### **🚀 Langkah-langkah Membuat Integrasi**
#### **1. Daftar sebagai Developer di Zapier**
1. Buka [Zapier Developer Platform](https://zapier.com/developer).
2. Klik **"Create App"** → **"Build a Private App"** (untuk pengembangan).
3. Beri nama integrasi: **MusGo-OS 2in1**.
4. Pilih **Platform UI** (untuk pemula) atau **Platform CLI** (untuk developer lanjutan).

---
#### **2. Pilih Platform (UI vs CLI)**
| Platform | Deskripsi | Rekomendasi untuk MusGo-OS |
|----------|-----------|-----------------------------|
| **Platform UI** | Visual builder, mudah digunakan | ✅ **Rekomendasi untuk pemula** |
| **Platform CLI** | Command-line, lebih fleksibel | ✅ **Rekomendasi untuk MusGo-OS** (lebih scalable) |

**Kita akan menggunakan Platform CLI** (karena MusGo-OS adalah **sovereign AI OS** yang memerlukan **fleksibilitas tinggi**).

---
#### **3. Instalasi Platform CLI**
```bash
# Instal Zapier Platform CLI
npm install -g zapier-platform-cli

# Verifikasi instalasi
zapier --version
```

---
#### **4. Buat Proyek Integrasi**
```bash
# Buat folder proyek
mkdir musgo-os-zapier-integration
cd musgo-os-zapier-integration

# Inisialisasi proyek
zapier init musgo-os-2in1
```
- Pilih **TypeScript** (untuk backend MusGo-OS).
- Pilih **Private App** (untuk pengembangan awal).

---
#### **5. Struktur Folder Proyek**
```
musgo-os-2in1/
│
├── index.js              # Entry point integrasi
├── package.json          # Dependencies & metadata
├── .zapierapprc          # Konfigurasi Zapier
├── triggers/             # Trigger definitions
│   └── taskCompleted.js  # Contoh: Trigger "Task Completed"
│
├── actions/              # Action definitions
│   └── runAgent.js       # Contoh: Action "Run AI Agent"
│
├── authentication/      # Autentikasi
│   └── oauth2.js         # Contoh: OAuth 2.0
│
└── test/                 # Testing
    └── triggers.js       # Test trigger
```

---
---
---

## **🔹 3.3 Building with Platform CLI (Membangun Integrasi)**
### **📌 1. Definisikan Trigger (Pemicu)**
**Contoh: Trigger "Task Completed"**
Buat file `triggers/taskCompleted.js`:
```javascript
const taskCompleted = {
  // Metadata trigger
  operation: {
    perform: {
      type: "polling",  // Atau "hook" (webhook)
      url: "https://musgo-os.com/api/zapier/triggers/task_completed",
      method: "GET",
      interval: 300,  // Polling setiap 5 menit
    },
    inputFields: [
      {
        key: "taskId",
        type: "string",
        required: false,
        helpText: "ID of the completed task.",
      },
      {
        key: "agentId",
        type: "string",
        required: false,
        helpText: "ID of the AI Agent that completed the task.",
      },
    ],
    outputFields: [
      {
        key: "taskId",
        type: "string",
        helpText: "ID of the completed task.",
      },
      {
        key: "taskName",
        type: "string",
        helpText: "Name of the completed task.",
      },
      {
        key: "agentId",
        type: "string",
        helpText: "ID of the AI Agent.",
      },
      {
        key: "completionTime",
        type: "datetime",
        helpText: "When the task was completed.",
      },
    ],
  },
  // Fungsi untuk mengambil data (untuk polling)
  perform: {
    url: (z, bundle) => {
      // Jika menggunakan polling, ambil data dari MusGo-OS API
      return "https://musgo-os.com/api/zapier/triggers/task_completed";
    },
    method: "GET",
    params: (z, bundle) => ({
      taskId: bundle.inputData.taskId,
      agentId: bundle.inputData.agentId,
    }),
  },
  // Fungsi untuk memproses data (untuk webhook)
  performSubscribe: {
    url: (z, bundle) => {
      // URL untuk Zapier mendaftarkan webhook
      return "https://musgo-os.com/api/zapier/webhooks/register";
    },
    method: "POST",
    body: (z, bundle) => ({
      url: bundle.targetUrl,  // URL Zapier untuk menerima event
      event: "task_completed",
    }),
  },
  // Fungsi untuk memproses data yang diterima (untuk webhook)
  performUnsubscribe: {
    url: (z, bundle) => {
      // URL untuk Zapier menghapus webhook
      return "https://musgo-os.com/api/zapier/webhooks/unregister";
    },
    method: "POST",
    body: (z, bundle) => ({
      url: bundle.targetUrl,
    }),
  },
};

module.exports = {
  taskCompleted: taskCompleted,
};
```

---
### **📌 2. Definisikan Action (Tindakan)**
**Contoh: Action "Run AI Agent"**
Buat file `actions/runAgent.js`:
```javascript
const runAgent = {
  // Metadata action
  operation: {
    perform: {
      type: "request",  // Zapier akan memanggil API MusGo-OS
      method: "POST",
      url: "https://musgo-os.com/api/zapier/actions/run_agent",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer {{bundle.authData.access_token}}",  // Jika menggunakan OAuth
      },
      body: {
        prompt: "{{prompt}}",
        agentId: "{{agentId}}",
      },
    },
    inputFields: [
      {
        key: "prompt",
        type: "text",
        required: true,
        helpText: "The prompt for the AI Agent.",
      },
      {
        key: "agentId",
        type: "string",
        required: true,
        helpText: "ID of the AI Agent to run.",
        default: "planner",  // Default agent
      },
    ],
    outputFields: [
      {
        key: "response",
        type: "text",
        helpText: "The response from the AI Agent.",
      },
      {
        key: "agentId",
        type: "string",
        helpText: "ID of the AI Agent that generated the response.",
      },
      {
        key: "timestamp",
        type: "datetime",
        helpText: "When the AI Agent was run.",
      },
    ],
  },
  // Fungsi untuk memproses input sebelum dikirim
  perform: {
    url: (z, bundle) => {
      return "https://musgo-os.com/api/zapier/actions/run_agent";
    },
    method: "POST",
    body: (z, bundle) => {
      return {
        prompt: bundle.inputData.prompt,
        agentId: bundle.inputData.agentId,
      };
    },
    headers: (z, bundle) => {
      return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${bundle.authData.access_token}`,
      };
    },
  },
};

module.exports = {
  runAgent: runAgent,
};
```

---
### **📌 3. Definisikan Autentikasi (OAuth 2.0)**
**Contoh: OAuth 2.0 untuk MusGo-OS**
Buat file `authentication/oauth2.js`:
```javascript
const oauth2Config = {
  type: "oauth2",
  oauthConfig: {
    authorizeUrl: {
      method: "GET",
      url: "https://musgo-os.com/oauth/authorize",
      params: {
        client_id: "{{client_id}}",
        response_type: "code",
        redirect_uri: "{{redirect_uri}}",
        scope: "read write",  // Scope yang diperlukan
        state: "{{state}}",
      },
    },
    getAccessToken: {
      method: "POST",
      url: "https://musgo-os.com/oauth/token",
      body: {
        code: "{{code}}",
        client_id: "{{client_id}}",
        client_secret: "{{client_secret}}",
        redirect_uri: "{{redirect_uri}}",
        grant_type: "authorization_code",
      },
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    },
    refreshAccessToken: {
      method: "POST",
      url: "https://musgo-os.com/oauth/token",
      body: {
        refresh_token: "{{refresh_token}}",
        client_id: "{{client_id}}",
        client_secret: "{{client_secret}}",
        grant_type: "refresh_token",
      },
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    },
    autoRefresh: true,  // Otomatis refresh token
    scopes: ["read", "write"],  // Scope yang diperlukan
  },
  // Field untuk menyimpan credential
  connectionLabel: (z, bundle) => {
    return `MusGo-OS (${bundle.inputData.email || "Unknown"})`;
  },
  // Field untuk input user (jika diperlukan)
  inputFields: [
    {
      key: "email",
      type: "string",
      required: false,
      helpText: "Email untuk akun MusGo-OS.",
    },
  ],
};

module.exports = oauth2Config;
```

---
### **📌 4. Definisikan App (Index File)**
Buat file `index.js`:
```javascript
const MusGoOS_Integration = {
  // Metadata integrasi
  version: "1.0.0",
  platformVersion: "1.0",

  // Autentikasi
  authentication: require("./authentication/oauth2"),

  // Trigger
  triggers: {
    taskCompleted: require("./triggers/taskCompleted").taskCompleted,
  },

  // Action
  actions: {
    runAgent: require("./actions/runAgent").runAgent,
  },

  // Search (opsional)
  searches: {},

  // Resources (opsional)
  resources: {},

  // Custom fields (opsional)
  customFields: {},

  // Display
  display: {
    description: "Integrasikan MusGo-OS 2in1 dengan Zapier untuk otomatisasi AI Agent.",
    instructionsUrl: "https://docs.musgo-os.com/zapier",
    imageUrl: "https://musgo-os.com/logo.png",
    connectionLabel: "{{email}}",
  },
};

module.exports = MusGoOS_Integration;
```

---
### **📌 5. Definisikan `package.json`**
```json
{
  "name": "musgo-os-2in1",
  "version": "1.0.0",
  "description": "Zapier integration for MusGo-OS 2in1",
  "main": "index.js",
  "scripts": {
    "test": "zapier test",
    "push": "zapier push",
    "register": "zapier register",
    "validate": "zapier validate"
  },
  "keywords": ["musgo-os", "ai", "automation", "zapier"],
  "author": "Dhani Yuliawan",
  "license": "MIT",
  "dependencies": {
    "@zapier/zapier-platform-core": "^12.0.0"
  },
  "devDependencies": {
    "@zapier/zapier-platform-cli": "^12.0.0"
  },
  "zapier": {
    "id": "YOUR_APP_ID",
    "key": "musgo_os_2in1",
    "title": "MusGo-OS 2in1",
    "iconUrl": "https://musgo-os.com/logo.png"
  }
}
```

---
---
---

## **🔹 3.4 Testing & Debugging**
### **📌 1. Testing Trigger & Action**
**Perintah untuk testing:**
```bash
# Test trigger
zapier test triggers/taskCompleted

# Test action
zapier test actions/runAgent --input '{"prompt": "Jelaskan MusGo-OS", "agentId": "planner"}'
```

**Contoh Output:**
```
✅ Trigger "taskCompleted" berjalan dengan sukses!
Data output: { taskId: "123", taskName: "Implementasi MCP", agentId: "planner", completionTime: "2026-05-19T10:00:00Z" }

✅ Action "runAgent" berjalan dengan sukses!
Data output: { response: "MusGo-OS adalah...", agentId: "planner", timestamp: "2026-05-19T10:00:00Z" }
```

---
### **📌 2. Debugging**
**Jika terjadi error:**
1. **Cek log Zapier CLI**:
   ```bash
   zapier logs
   ```
2. **Cek API MusGo-OS**:
   - Pastikan endpoint `/api/zapier/triggers/task_completed` dan `/api/zapier/actions/run_agent` **berjalan dengan benar**.
   - Gunakan **Postman** atau **cURL** untuk testing:
     ```bash
     curl -X GET "https://musgo-os.com/api/zapier/triggers/task_completed"
     curl -X POST "https://musgo-os.com/api/zapier/actions/run_agent" -H "Content-Type: application/json" -d '{"prompt": "Halo", "agentId": "planner"}'
     ```
3. **Cek Autentikasi**:
   - Pastikan **OAuth 2.0** terkonfigurasi dengan benar.
   - Pastikan **client_id**, **client_secret**, dan **redirect_uri** **valid**.

---
---
---

## **🔹 3.5 Deploying the Integration**
### **📌 1. Push ke Zapier**
```bash
# Push integrasi ke Zapier (untuk private testing)
zapier push
```

**Output:**
```
✅ Integration "MusGo-OS 2in1" berhasil di-push ke Zapier!
URL: https://zapier.com/developer/edit/12345
```

---
### **📌 2. Register (Publish) ke Zapier App Directory**
```bash
# Register integrasi (untuk public use)
zapier register
```
- **Private App**: Hanya bisa digunakan oleh **akun Zapier Anda**.
- **Public App**: Bisa digunakan oleh **semua user Zapier** (memerlukan **review dari Zapier**).

---
### **📌 3. Share dengan User**
Setelah integrasi **published**, user bisa:
1. **Mencari "MusGo-OS 2in1"** di [Zapier App Directory](https://zapier.com/apps).
2. **Menghubungkan akun MusGo-OS** ke Zapier.
3. **Membuat Zap** dengan trigger/action MusGo-OS.

**Contoh Zap yang bisa dibuat user:**
| Trigger | Action | Deskripsi |
|---------|--------|-----------|
| MusGo-OS: Task Completed | Slack: Send Channel Message | Kirim notifikasi ke Slack saat AI Agent menyelesaikan tugas |
| Google Drive: New File | MusGo-OS: Run AI Agent | Jalankan AI Agent saat file baru diupload |
| MusGo-OS: Run AI Agent | Notion: Create Database Row | Simpan hasil AI Agent ke Notion |

---
---
---

## **🔹 3.6 Contoh Implementasi Backend MusGo-OS**
### **📌 1. Endpoint untuk Trigger (Polling)**
**Contoh: `/api/zapier/triggers/task_completed` (Python - FastAPI)**
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()

# Model untuk task
class Task(BaseModel):
    taskId: str
    taskName: str
    agentId: str
    completionTime: datetime

# Dummy database (ganti dengan database asli)
tasks_db = [
    Task(
        taskId="123",
        taskName="Implementasi MCP",
        agentId="planner",
        completionTime=datetime.now()
    ),
    Task(
        taskId="456",
        taskName="Setup Zapier SDK",
        agentId="executor",
        completionTime=datetime.now()
    )
]

@router.get("/api/zapier/triggers/task_completed")
async def get_completed_tasks(taskId: str = None, agentId: str = None):
    """Endpoint untuk Zapier polling trigger"""
    if taskId:
        task = next((t for t in tasks_db if t.taskId == taskId), None)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return [task.dict()]
    elif agentId:
        tasks = [t for t in tasks_db if t.agentId == agentId]
        return [t.dict() for t in tasks]
    else:
        return [t.dict() for t in tasks_db]

# Tambahkan ke FastAPI app
from fastapi import FastAPI
app = FastAPI()
app.include_router(router)
```

---
### **📌 2. Endpoint untuk Action (Run AI Agent)**
**Contoh: `/api/zapier/actions/run_agent` (Python - FastAPI)**
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter()

# Model untuk request
class RunAgentRequest(BaseModel):
    prompt: str
    agentId: str = "planner"  # Default agent

# Model untuk response
class RunAgentResponse(BaseModel):
    response: str
    agentId: str
    timestamp: datetime

# Dummy AI Agent (ganti dengan AI Agent asli MusGo-OS)
def run_ai_agent(prompt: str, agentId: str) -> str:
    """Simulasi AI Agent"""
    if agentId == "planner":
        return f"Rencana untuk '{prompt}': Langkah 1, Langkah 2, Langkah 3."
    elif agentId == "executor":
        return f"Hasil eksekusi untuk '{prompt}': Selesai!"
    else:
        return f"AI Agent '{agentId}' tidak ditemukan."

@router.post("/api/zapier/actions/run_agent")
async def run_agent(request: RunAgentRequest):
    """Endpoint untuk Zapier action"""
    # Jalankan AI Agent
    response = run_ai_agent(request.prompt, request.agentId)

    # Return response
    return RunAgentResponse(
        response=response,
        agentId=request.agentId,
        timestamp=datetime.now()
    ).dict()

# Tambahkan ke FastAPI app
app.include_router(router)
```

---
### **📌 3. Endpoint untuk Webhook (Real-Time)**
**Contoh: `/api/zapier/webhooks/register` (Python - FastAPI)**
```python
from fastapi import APIRouter, HTTPException, Request
from typing import List
import uuid

router = APIRouter()

# Dummy database untuk webhook
webhooks_db: List[dict] = []

@router.post("/api/zapier/webhooks/register")
async def register_webhook(request: Request):
    """Endpoint untuk Zapier mendaftarkan webhook"""
    body = await request.json()
    webhook_url = body.get("url")
    event = body.get("event")

    if not webhook_url or not event:
        raise HTTPException(status_code=400, detail="url and event are required")

    # Simpan webhook
    webhook_id = str(uuid.uuid4())
    webhooks_db.append({
        "id": webhook_id,
        "url": webhook_url,
        "event": event,
    })

    return {"id": webhook_id, "status": "registered"}

@router.post("/api/zapier/webhooks/unregister")
async def unregister_webhook(request: Request):
    """Endpoint untuk Zapier menghapus webhook"""
    body = await request.json()
    webhook_url = body.get("url")

    if not webhook_url:
        raise HTTPException(status_code=400, detail="url is required")

    # Hapus webhook
    global webhooks_db
    webhooks_db = [wh for wh in webhooks_db if wh["url"] != webhook_url]

    return {"status": "unregistered"}

# Tambahkan ke FastAPI app
app.include_router(router)
```

---
### **📌 4. Endpoint untuk OAuth 2.0**
**Contoh: `/oauth/authorize` & `/oauth/token` (Python - FastAPI)**
```python
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
import secrets
import uuid
from datetime import datetime, timedelta
from typing import Dict, Optional

router = APIRouter()

# Dummy database untuk OAuth
oauth_clients: Dict[str, dict] = {
    "CLIENT_ID_1": {
        "client_secret": "CLIENT_SECRET_1",
        "redirect_uri": "https://zapier.com/oauth/redirect",
    }
}

oauth_tokens: Dict[str, dict] = {}
oauth_codes: Dict[str, dict] = {}

@router.get("/oauth/authorize")
async def oauth_authorize(
    response_type: str = "code",
    client_id: str = None,
    redirect_uri: str = None,
    scope: str = None,
    state: str = None
):
    """Endpoint untuk OAuth 2.0 Authorization Code Flow"""
    if response_type != "code":
        raise HTTPException(status_code=400, detail="Unsupported response_type")

    if client_id not in oauth_clients:
        raise HTTPException(status_code=400, detail="Invalid client_id")

    if oauth_clients[client_id]["redirect_uri"] != redirect_uri:
        raise HTTPException(status_code=400, detail="Invalid redirect_uri")

    # Generate authorization code
    code = secrets.token_urlsafe(32)
    oauth_codes[code] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": state,
    }

    # Redirect ke redirect_uri dengan code
    redirect_url = f"{redirect_uri}?code={code}"
    if state:
        redirect_url += f"&state={state}"

    return RedirectResponse(url=redirect_url)

@router.post("/oauth/token")
async def oauth_token(request: Request):
    """Endpoint untuk OAuth 2.0 Token Exchange"""
    form_data = await request.form()

    grant_type = form_data.get("grant_type")
    client_id = form_data.get("client_id")
    client_secret = form_data.get("client_secret")
    redirect_uri = form_data.get("redirect_uri")

    # Validate client
    if client_id not in oauth_clients:
        raise HTTPException(status_code=400, detail="Invalid client_id")

    if oauth_clients[client_id]["client_secret"] != client_secret:
        raise HTTPException(status_code=400, detail="Invalid client_secret")

    if grant_type == "authorization_code":
        code = form_data.get("code")
        if code not in oauth_codes:
            raise HTTPException(status_code=400, detail="Invalid code")

        # Generate access token
        access_token = str(uuid.uuid4())
        refresh_token = str(uuid.uuid4())
        expires_in = 3600  # 1 jam

        oauth_tokens[access_token] = {
            "client_id": client_id,
            "scope": oauth_codes[code]["scope"],
            "expires_at": datetime.now() + timedelta(seconds=expires_in),
        }

        return {
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": expires_in,
            "refresh_token": refresh_token,
        }

    elif grant_type == "refresh_token":
        refresh_token = form_data.get("refresh_token")
        # Implementasi refresh token (opsional)
        return {"error": "refresh_token not implemented"}

    else:
        raise HTTPException(status_code=400, detail="Unsupported grant_type")

# Tambahkan ke FastAPI app
app.include_router(router)
```

---
---
---

## **🔹 3.7 Contoh Full Workflow untuk MusGo-OS**
### **📌 Skenario: User Membuat Zap dengan MusGo-OS**
1. **User Zapier** mencari **"MusGo-OS 2in1"** di Zapier App Directory.
2. **User menghubungkan akun MusGo-OS** ke Zapier (via OAuth 2.0).
3. **User membuat Zap**:
   - **Trigger**: MusGo-OS → **Task Completed**
   - **Action**: Slack → **Send Channel Message**
4. **Saat AI Agent MusGo-OS menyelesaikan tugas**:
   - MusGo-OS **mengirim event** ke Zapier (via webhook atau polling).
   - Zapier **menjalankan action** (kirim pesan ke Slack).

**Contoh Zap:**
```
Trigger: MusGo-OS → Task Completed
Action: Slack → Send Channel Message
Data:
- Channel: #musgo-updates
- Message: "Tugas {{taskName}} selesai oleh AI Agent {{agentId}}!"
```

---
### **📌 Skenario: User Membuat Zap dengan Action MusGo-OS**
1. **User Zapier** membuat Zap:
   - **Trigger**: Google Drive → **New File in Folder**
   - **Action**: MusGo-OS → **Run AI Agent**
2. **Saat file baru diupload ke Google Drive**:
   - Zapier **memanggil MusGo-OS API** (`/api/zapier/actions/run_agent`).
   - MusGo-OS **menjalankan AI Agent** dengan prompt dari file.
   - MusGo-OS **mengembalikan response** ke Zapier.

**Contoh Zap:**
```
Trigger: Google Drive → New File in Folder
Action: MusGo-OS → Run AI Agent
Data:
- Prompt: "Analisis file {{file_name}} dan berikan ringkasan."
- Agent ID: "analyst"
```

---
---
---

## **📌 PART 3: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

### **🔥 Kesimpulan Part 3 (Integration Builder)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Trigger Kustom** | MusGo-OS bisa memicu Zap (misal: Task Completed) | ✅ **Contoh kode tersedia** |
| **Action Kustom** | MusGo-OS bisa dijadikan action (misal: Run AI Agent) | ✅ **Contoh kode tersedia** |
| **OAuth 2.0** | Autentikasi aman untuk user | ✅ **Contoh kode tersedia** |
| **Platform CLI** | Fleksibel untuk development | ✅ **Siap digunakan** |
| **Testing & Debugging** | Mudah menguji integrasi | ✅ **Contoh perintah tersedia** |
| **Deployment** | Publish ke Zapier App Directory | ✅ **Siap di-deploy** |

---

### **🛠️ Langkah Selanjutnya untuk MusGo-OS**
#### **1. Short-Term (1-2 Minggu)**
- [ ] **Daftar sebagai Developer di Zapier** → [Zapier Developer Platform](https://zapier.com/developer).
- [ ] **Instal Zapier Platform CLI** (`npm install -g zapier-platform-cli`).
- [ ] **Buat proyek integrasi** (`zapier init musgo-os-2in1`).
- [ ] **Definisikan trigger & action** (gunakan contoh kode di atas).
- [ ] **Setup OAuth 2.0** (jika diperlukan).

#### **2. Mid-Term (1 Bulan)**
- [ ] **Implementasikan endpoint backend** (`/api/zapier/triggers`, `/api/zapier/actions`).
- [ ] **Test integrasi** (`zapier test`).
- [ ] **Push ke Zapier** (`zapier push`).
- [ ] **Uji integrasi di Zapier Dashboard**.

#### **3. Long-Term (3+ Bulan)**
- [ ] **Register integrasi** (`zapier register`) untuk public use.
- [ ] **Dokumentasikan integrasi** untuk user.
- [ ] **Promosikan integrasi** ke user MusGo-OS.

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 4: Powered by Zapier** (Untuk embedding otomatisasi ke MusGo-OS)
   - [ ] **Part 5: White Label** (Untuk branding MusGo-OS sendiri)
   - [ ] **Part 6: Workflow API** (Untuk membuat Zap secara programatik)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + MusGo-OS)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi API untuk MusGo-OS + Zapier**?
   - [ ] **Contoh deployment (Docker, Kubernetes)**?

3. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **MusGo-OS → Slack**, **Google Drive → MusGo-OS**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 4: Powered by Zapier** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi** untuk **MusGo-OS 2in1** dari dokumentasi **Powered by Zapier**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN POWERED BY ZAPIER (PART 4)**
*Terjemahan + Implementasi untuk Embedding Otomatisasi Zapier ke MusGo-OS*

---

---

## **🔹 4.1 Overview Powered by Zapier**
### **📌 Penjelasan (Bahasa Indonesia)**
**Powered by Zapier** adalah **solusi embedding** yang memungkinkan **MusGo-OS** untuk **mengintegrasikan otomatisasi Zapier langsung ke dalam produk Anda**. Dengan Powered by Zapier, Anda bisa:
✅ **Mengembed Zap Editor** (untuk user membuat Zap tanpa meninggalkan MusGo-OS).
✅ **Menjalankan Action Zapier** (misal: kirim Slack, simpan ke Google Sheets) **dari MusGo-OS**.
✅ **Mengelola Autentikasi** (user bisa menghubungkan akun Slack/Google Drive ke MusGo-OS).
✅ **Membuat Workflow Kustom** (user bisa membuat otomatisasi tanpa coding).

**Manfaat untuk MusGo-OS:**
- **User MusGo-OS bisa membuat Zap tanpa keluar dari MusGo-OS**.
- **MusGo-OS bisa menawarkan fitur otomatisasi** (misal: "Jika AI Agent menyelesaikan tugas → Kirim notifikasi ke Slack").
- **MusGo-OS bisa terintegrasi dengan 9,000+ aplikasi** tanpa perlu membangun integrasi dari nol.

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: Embed Zap Editor di MusGo-OS**
**Skenario:**
User MusGo-OS ingin **membuat Zap** (otomatisasi) **langsung dari dashboard MusGo-OS**.

**Cara Kerja:**
1. **MusGo-OS** menampilkan **Zap Editor** (embedded) di dalam UI.
2. **User** membuat **Zap** (misal: Google Drive → Slack).
3. **Zap disimpan** dan **berjalan otomatis** saat trigger terpicu.

**Arsitektur:**
```
User → MusGo-OS Dashboard → (Embedded) Zap Editor → Zapier → Aplikasi Eksternal
```

**Contoh UI (React + TypeScript):**
```tsx
// File: src/components/ZapierEditor.tsx
import React, { useEffect } from "react";

interface ZapierEditorProps {
  apiKey: string;
  onZapCreated?: (zapId: string) => void;
}

const ZapierEditor: React.FC<ZapierEditorProps> = ({ apiKey, onZapCreated }) => {
  useEffect(() => {
    // Load Zapier Embedded Editor
    const script = document.createElement("script");
    script.src = "https://cdn.zapier.com/packages/embedded/zap-editor.js";
    script.async = true;
    script.onload = () => {
      // Inisialisasi Zap Editor
      if (window.ZapierEmbedded) {
        window.ZapierEmbedded.ZapEditor.init({
          apiKey: apiKey,
          onZapCreated: (zapId: string) => {
            if (onZapCreated) onZapCreated(zapId);
            console.log("✅ Zap dibuat:", zapId);
          },
          onError: (error: any) => {
            console.error("❌ Error:", error);
          },
        });
      }
    };
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, [apiKey, onZapCreated]);

  return (
    <div
      id="zapier-editor"
      style={{ width: "100%", height: "600px", border: "1px solid #e0e0e0" }}
    />
  );
};

export default ZapierEditor;
```

**Contoh Penggunaan di MusGo-OS Dashboard:**
```tsx
// File: src/pages/AutomationDashboard.tsx
import React, { useState } from "react";
import ZapierEditor from "../components/ZapierEditor";

const AutomationDashboard: React.FC = () => {
  const [zapId, setZapId] = useState<string | null>(null);
  const [showEditor, setShowEditor] = useState(false);

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 Otomatisasi MusGo-OS</h1>
      <p>Buat Zap untuk mengotomatiskan workflow Anda!</p>

      {!showEditor ? (
        <button
          onClick={() => setShowEditor(true)}
          style={{
            padding: "10px 20px",
            background: "#4285F4",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          ✨ Buat Zap Baru
        </button>
      ) : (
        <>
          <ZapierEditor
            apiKey="YOUR_ZAPIER_API_KEY"
            onZapCreated={(id) => {
              setZapId(id);
              setShowEditor(false);
            }}
          />
          <button
            onClick={() => setShowEditor(false)}
            style={{ marginTop: "10px" }}
          >
            Tutup Editor
          </button>
        </>
      )}

      {zapId && (
        <div style={{ marginTop: "20px", padding: "10px", background: "#f0f0f0" }}>
          ✅ Zap berhasil dibuat! ID: <code>{zapId}</code>
        </div>
      )}
    </div>
  );
};

export default AutomationDashboard;
```

---
#### **Use-Case 2: Jalankan Action Zapier dari MusGo-OS**
**Skenario:**
User MusGo-OS ingin **menjalankan action Zapier** (misal: kirim pesan Slack) **dari AI Agent MusGo-OS**.

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima perintah user:
   > *"MusGo, kirim pesan ke Slack: 'Proyek selesai!' ke channel #musgo-updates."*
2. **AI Agent menggunakan Powered by Zapier API** untuk **menjalankan action Slack**.

**Arsitektur:**
```
User → MusGo-OS AI Agent → Powered by Zapier API → Slack (Action)
```

**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierService.ts
import axios from "axios";

interface ZapierActionData {
  app: string;
  action: string;
  data: Record<string, any>;
}

interface ZapierActionResult {
  id: string;
  status: string;
  data: Record<string, any>;
}

class ZapierService {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Jalankan action Zapier
  async runAction(actionData: ZapierActionData): Promise<ZapierActionResult> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/actions/run`,
        {
          action: actionData.action,
          app: actionData.app,
          data: actionData.data,
        },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal menjalankan action Zapier:", error);
      throw error;
    }
  }

  // Contoh: Kirim pesan Slack
  async sendSlackMessage(channel: string, text: string): Promise<ZapierActionResult> {
    return this.runAction({
      app: "slack",
      action: "Send Channel Message",
      data: {
        channel,
        text,
      },
    });
  }

  // Contoh: Buat kartu Trello
  async createTrelloCard(
    title: string,
    description: string,
    boardId: string,
    listId: string
  ): Promise<ZapierActionResult> {
    return this.runAction({
      app: "trello",
      action: "Create Card",
      data: {
        title,
        description,
        boardId,
        listId,
      },
    });
  }
}

// Contoh penggunaan di MusGo-OS AI Agent
const zapierService = new ZapierService("YOUR_ZAPIER_API_KEY");

// Kirim pesan Slack
zapierService.sendSlackMessage("#musgo-updates", "Proyek selesai!")
  .then((result) => console.log("✅ Pesan Slack dikirim:", result))
  .catch(console.error);

// Buat kartu Trello
zapierService.createTrelloCard(
  "Implementasi MCP",
  "Integrasikan Zapier MCP ke MusGo-OS",
  "TRELLO_BOARD_ID",
  "TRELLO_LIST_ID"
)
  .then((result) => console.log("✅ Kartu Trello dibuat:", result))
  .catch(console.error);
```

---
---
---

## **🔹 4.2 Embedding Zapier MCP (Model Context Protocol)**
### **📌 Penjelasan**
**Zapier MCP** memungkinkan **AI Agent** (seperti di MusGo-OS) untuk **berinteraksi dengan Zapier** via **Model Context Protocol (MCP)**. Ini **lebih powerful** daripada Powered by Zapier API karena:
- **AI Agent bisa memanggil Zapier secara dinamis** (tanpa perlu hardcode action).
- **AI Agent bisa mendaftar aplikasi yang terintegrasi** dan **membuat Zap otomatis**.

**Manfaat untuk MusGo-OS:**
- **AI Agent MusGo-OS bisa membuat Zap otomatis** berdasarkan perintah user.
- **AI Agent bisa menjelajahi aplikasi yang terintegrasi** (misal: "Aplikasi apa saja yang bisa dihubungkan?").

---
### **🚀 Contoh Implementasi: AI Agent + Zapier MCP**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, buatkan Zap yang mengirim notifikasi ke Slack setiap kali ada file baru di Google Drive folder 'Proyek'."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima perintah.
2. **AI Agent menggunakan Zapier MCP** untuk:
   - Mendaftar aplikasi yang terintegrasi (Google Drive, Slack).
   - Membuat **Zap** dengan trigger **Google Drive → New File** dan action **Slack → Send Message**.

**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierMCPService.ts
import { Client } from "@modelcontextprotocol/sdk/client";

interface ZapConfig {
  trigger: {
    app: string;
    event: string;
    data?: Record<string, any>;
  };
  action: {
    app: string;
    event: string;
    data: Record<string, any>;
  };
}

class ZapierMCPService {
  private client: Client;

  constructor() {
    this.client = new Client({
      name: "zapier-mcp",
      command: "npx",
      args: ["@zapier/zapier-sdk-mcp", "--api-key=YOUR_ZAPIER_API_KEY"],
    });
  }

  // Daftar aplikasi yang terintegrasi
  async listApps(): Promise<string[]> {
    const response = await this.client.callTool("zapier_list_apps", {});
    return response.apps || [];
  }

  // Buat Zap baru
  async createZap(zapConfig: ZapConfig): Promise<{ id: string }> {
    const response = await this.client.callTool("zapier_create_zap", zapConfig);
    return response;
  }

  // Jalankan action langsung
  async runAction(app: string, action: string, data: Record<string, any>): Promise<any> {
    const response = await this.client.callTool("zapier_run_action", {
      app,
      action,
      data,
    });
    return response;
  }
}

// Contoh penggunaan di MusGo-OS AI Agent
const zapierMCP = new ZapierMCPService();

// Fungsi untuk memproses perintah user
async function handleUserCommand(command: string): Promise<string> {
  command = command.toLowerCase();

  // Contoh 1: Daftar aplikasi
  if (command.includes("aplikasi apa saja yang terintegrasi")) {
    const apps = await zapierMCP.listApps();
    return `📋 Aplikasi yang terintegrasi: ${apps.join(", ")}`;
  }

  // Contoh 2: Buat Zap Google Drive → Slack
  else if (command.includes("buatkan zap google drive ke slack")) {
    const folderMatch = command.match(/folder "([^"]+)"/);
    const channelMatch = command.match(/ke channel (\S+)/);

    if (folderMatch && channelMatch) {
      const folder = folderMatch[1];
      const channel = channelMatch[1];

      const zap = await zapierMCP.createZap({
        trigger: {
          app: "google_drive",
          event: "New File in Folder",
          data: { folder },
        },
        action: {
          app: "slack",
          event: "Send Channel Message",
          data: {
            channel,
            text: `File baru terdeteksi di folder "${folder}": {file_name}`,
          },
        },
      });

      return `✅ Zap dibuat! ID: ${zap.id}`;
    }
  }

  // Contoh 3: Jalankan action Slack
  else if (command.includes("kirim pesan ke slack")) {
    const channelMatch = command.match(/ke channel (\S+)/);
    const textMatch = command.match(/pesan "([^"]+)"/);

    if (channelMatch && textMatch) {
      const channel = channelMatch[1];
      const text = textMatch[1];

      await zapierMCP.runAction("slack", "Send Channel Message", {
        channel,
        text,
      });

      return `✅ Pesan dikirim ke ${channel}: "${text}"`;
    }
  }

  return "Maaf, saya tidak mengerti perintah Anda.";
}

// Simulasi
const commands = [
  "MusGo, aplikasi apa saja yang terintegrasi?",
  "MusGo, buatkan Zap Google Drive ke Slack dengan folder 'Proyek' ke channel #musgo-updates",
  "MusGo, kirim pesan ke Slack ke channel #musgo-updates dengan pesan 'Proyek selesai!'",
];

commands.forEach(async (cmd) => {
  console.log(`\n👤 User: ${cmd}`);
  const response = await handleUserCommand(cmd);
  console.log(`🤖 MusGo-OS: ${response}`);
});
```

**Output Contoh:**
```
👤 User: MusGo, aplikasi apa saja yang terintegrasi?
🤖 MusGo-OS: 📋 Aplikasi yang terintegrasi: google_drive, slack, notion, trello, gmail, ...

👤 User: MusGo, buatkan Zap Google Drive ke Slack dengan folder 'Proyek' ke channel #musgo-updates
🤖 MusGo-OS: ✅ Zap dibuat! ID: ZAP_123

👤 User: MusGo, kirim pesan ke Slack ke channel #musgo-updates dengan pesan 'Proyek selesai!'
🤖 MusGo-OS: ✅ Pesan dikirim ke #musgo-updates: "Proyek selesai!"
```

---
---
---

## **🔹 4.3 Embedded Zap Editor (Workflow Element)**
### **📌 Penjelasan**
**Workflow Element** adalah **komponen UI pre-built** dari Zapier yang memungkinkan **user membuat Zap langsung di MusGo-OS** tanpa perlu coding. Komponen ini **lebih ringan** daripada Zap Editor penuh.

**Manfaat untuk MusGo-OS:**
- **User bisa membuat Zap dengan mudah** (tanpa meninggalkan MusGo-OS).
- **UI konsisten** dengan Zapier.
- **Mendukung pre-filled data** (misal: otomatis isi channel Slack dengan `#musgo-updates`).

---
### **🚀 Contoh Implementasi: Workflow Element**
**Contoh Kode (React + TypeScript):**
```tsx
// File: src/components/ZapierWorkflowElement.tsx
import React, { useEffect } from "react";

interface ZapierWorkflowElementProps {
  apiKey: string;
  appKey?: string; // Misal: "musgo_os_2in1" (jika MusGo-OS sudah terdaftar di Zapier)
  prefilledData?: Record<string, any>; // Data yang sudah diisi otomatis
  onZapCreated?: (zapId: string) => void;
}

const ZapierWorkflowElement: React.FC<ZapierWorkflowElementProps> = ({
  apiKey,
  appKey,
  prefilledData,
  onZapCreated,
}) => {
  useEffect(() => {
    // Load Zapier Workflow Element
    const script = document.createElement("script");
    script.src = "https://cdn.zapier.com/packages/embedded/workflow-element.js";
    script.async = true;
    script.onload = () => {
      if (window.ZapierEmbedded) {
        window.ZapierEmbedded.WorkflowElement.init({
          apiKey: apiKey,
          appKey: appKey,
          prefilledData: prefilledData,
          onZapCreated: (zapId: string) => {
            if (onZapCreated) onZapCreated(zapId);
            console.log("✅ Zap dibuat:", zapId);
          },
          onError: (error: any) => {
            console.error("❌ Error:", error);
          },
        });
      }
    };
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, [apiKey, appKey, prefilledData, onZapCreated]);

  return (
    <div
      id="zapier-workflow-element"
      style={{ width: "100%", height: "500px", border: "1px solid #e0e0e0" }}
    />
  );
};

export default ZapierWorkflowElement;
```

**Contoh Penggunaan:**
```tsx
// File: src/pages/AutomationPage.tsx
import React from "react";
import ZapierWorkflowElement from "../components/ZapierWorkflowElement";

const AutomationPage: React.FC = () => {
  // Pre-filled data: Otomatis isi channel Slack dengan #musgo-updates
  const prefilledData = {
    slack: {
      channel: "#musgo-updates",
    },
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🔄 Buat Workflow Otomatis</h1>
      <p>Gunakan Zapier untuk mengotomatiskan tugas Anda!</p>

      <ZapierWorkflowElement
        apiKey="YOUR_ZAPIER_API_KEY"
        appKey="musgo_os_2in1" // Jika MusGo-OS sudah terdaftar di Zapier
        prefilledData={prefilledData}
        onZapCreated={(zapId) => {
          console.log("✅ Zap dibuat:", zapId);
          alert(`Zap berhasil dibuat! ID: ${zapId}`);
        }}
      />
    </div>
  );
};

export default AutomationPage;
```

---
---
---

## **🔹 4.4 Zap Creation (Workflow API)**
### **📌 Penjelasan**
**Workflow API** adalah **REST API** dari Zapier yang memungkinkan **MusGo-OS** untuk **membuat, mengelola, dan menjalankan Zap secara programatik**. Ini **lebih powerful** daripada MCP karena:
- **Bisa membuat Zap tanpa interaksi user**.
- **Bisa mengelola Zap user** (misal: daftar Zap, hapus Zap).
- **Bisa menjalankan Zap dengan data dinamis**.

**Manfaat untuk MusGo-OS:**
- **Backend MusGo-OS bisa membuat Zap otomatis** untuk user.
- **AI Agent bisa menjalankan Zap** berdasarkan perintah user.

---
### **🚀 Contoh Implementasi: Workflow API**
#### **1. Setup Workflow API**
**Persyaratan:**
- **API Key Zapier** (dapatkan di [Zapier API Settings](https://zapier.com/app/developer)).
- **User Access Token** (jika ingin mengelola Zap user).

**Contoh Kode (TypeScript - Axios):**
```typescript
// File: src/services/ZapierWorkflowAPI.ts
import axios from "axios";

interface Zap {
  id: string;
  name: string;
  status: "on" | "off" | "paused";
  created_at: string;
}

interface ZapStep {
  id: string;
  app: string;
  action: string;
  data: Record<string, any>;
}

interface CreateZapRequest {
  name: string;
  steps: ZapStep[];
}

class ZapierWorkflowAPI {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Daftar Zap user
  async listZaps(): Promise<Zap[]> {
    try {
      const response = await axios.get(`${this.baseUrl}/zaps`, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
        },
      });
      return response.data.zaps;
    } catch (error) {
      console.error("❌ Gagal mendaftar Zap:", error);
      throw error;
    }
  }

  // Buat Zap baru
  async createZap(zapData: CreateZapRequest): Promise<Zap> {
    try {
      const response = await axios.post(`${this.baseUrl}/zaps`, zapData, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
          "Content-Type": "application/json",
        },
      });
      return response.data;
    } catch (error) {
      console.error("❌ Gagal membuat Zap:", error);
      throw error;
    }
  }

  // Jalankan Zap
  async runZap(zapId: string, data: Record<string, any> = {}): Promise<any> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/zaps/${zapId}/run`,
        { data },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal menjalankan Zap:", error);
      throw error;
    }
  }

  // Hapus Zap
  async deleteZap(zapId: string): Promise<void> {
    try {
      await axios.delete(`${this.baseUrl}/zaps/${zapId}`, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
        },
      });
    } catch (error) {
      console.error("❌ Gagal menghapus Zap:", error);
      throw error;
    }
  }
}

// Contoh penggunaan
const workflowAPI = new ZapierWorkflowAPI("YOUR_ZAPIER_API_KEY");

// Daftar Zap
workflowAPI.listZaps()
  .then((zaps) => console.log("📋 Daftar Zap:", zaps))
  .catch(console.error);

// Buat Zap: Google Drive → Slack
workflowAPI.createZap({
  name: "Google Drive → Slack (MusGo-OS)",
  steps: [
    {
      id: "trigger_1",
      app: "google_drive",
      action: "New File in Folder",
      data: { folder: "Proyek MusGo-OS" },
    },
    {
      id: "action_1",
      app: "slack",
      action: "Send Channel Message",
      data: {
        channel: "#musgo-updates",
        text: "File baru terdeteksi: {file_name}",
      },
    },
  ],
})
  .then((zap) => console.log("✅ Zap dibuat:", zap))
  .catch(console.error);

// Jalankan Zap
workflowAPI.runZap("ZAP_123", { file_name: "laporan.pdf" })
  .then((result) => console.log("✅ Zap berjalan:", result))
  .catch(console.error);
```

---
#### **2. Contoh: AI Agent Membuat Zap Otomatis**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, buatkan Zap yang mengirim email ke dhani@musgo-os.com setiap kali ada file baru di Google Drive folder 'Laporan'."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima perintah.
2. **AI Agent menggunakan Workflow API** untuk **membuat Zap** dengan:
   - Trigger: **Google Drive → New File in Folder** (folder: Laporan).
   - Action: **Gmail → Send Email** (to: dhani@musgo-os.com).

**Contoh Kode:**
```typescript
// Fungsi untuk memproses perintah user
async function handleUserCommand(command: string): Promise<string> {
  command = command.toLowerCase();

  if (command.includes("buatkan zap google drive ke email")) {
    const folderMatch = command.match(/folder "([^"]+)"/);
    const emailMatch = command.match(/ke (\S+)/);

    if (folderMatch && emailMatch) {
      const folder = folderMatch[1];
      const email = emailMatch[1];

      const zap = await workflowAPI.createZap({
        name: `Google Drive (${folder}) → Email (${email})`,
        steps: [
          {
            id: "trigger_1",
            app: "google_drive",
            action: "New File in Folder",
            data: { folder },
          },
          {
            id: "action_1",
            app: "gmail",
            action: "Send Email",
            data: {
              to: email,
              subject: `File baru di folder "${folder}"`,
              body: `File baru terdeteksi: {file_name}\nURL: {file_url}`,
            },
          },
        ],
      });

      return `✅ Zap dibuat! ID: ${zap.id}`;
    }
  }

  return "Maaf, saya tidak mengerti perintah Anda.";
}

// Simulasi
handleUserCommand("MusGo, buatkan Zap Google Drive ke email ke dhani@musgo-os.com dengan folder 'Laporan'")
  .then(console.log);
```

**Output:**
```
✅ Zap dibuat! ID: ZAP_456
```

---
---
---

## **🔹 4.5 Running Actions (Menjalankan Tindakan)**
### **📌 Penjelasan**
**Running Actions** memungkinkan **MusGo-OS** untuk **menjalankan action Zapier secara langsung** (tanpa perlu membuat Zap). Ini berguna untuk:
- **AI Agent** yang ingin **menjalankan tindakan cepat** (misal: kirim Slack, simpan ke Google Sheets).
- **Backend MusGo-OS** yang ingin **menjalankan otomatisasi** tanpa interaksi user.

---
### **🚀 Contoh Implementasi: Running Actions**
**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierActions.ts
import axios from "axios";

interface ActionData {
  app: string;
  action: string;
  data: Record<string, any>;
}

class ZapierActions {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Jalankan action
  async runAction(actionData: ActionData): Promise<any> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/actions/run`,
        {
          app: actionData.app,
          action: actionData.action,
          data: actionData.data,
        },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal menjalankan action:", error);
      throw error;
    }
  }

  // Contoh: Kirim pesan Slack
  async sendSlackMessage(channel: string, text: string): Promise<any> {
    return this.runAction({
      app: "slack",
      action: "Send Channel Message",
      data: { channel, text },
    });
  }

  // Contoh: Simpan data ke Google Sheets
  async appendGoogleSheet(
    spreadsheetId: string,
    worksheet: string,
    data: Record<string, any>
  ): Promise<any> {
    return this.runAction({
      app: "google_sheets",
      action: "Create Spreadsheet Row",
      data: {
        spreadsheetId,
        worksheet,
        ...data,
      },
    });
  }

  // Contoh: Buat kartu Trello
  async createTrelloCard(
    title: string,
    description: string,
    boardId: string,
    listId: string
  ): Promise<any> {
    return this.runAction({
      app: "trello",
      action: "Create Card",
      data: {
        title,
        description,
        boardId,
        listId,
      },
    });
  }
}

// Contoh penggunaan
const zapierActions = new ZapierActions("YOUR_ZAPIER_API_KEY");

// Kirim pesan Slack
zapierActions.sendSlackMessage("#musgo-updates", "Proyek selesai!")
  .then((result) => console.log("✅ Pesan Slack dikirim:", result))
  .catch(console.error);

// Simpan data ke Google Sheets
zapierActions.appendGoogleSheet(
  "SPREADSHEET_ID",
  "Sheet1",
  { name: "Dhani", task: "Implementasi MCP", status: "Done" }
)
  .then((result) => console.log("✅ Data disimpan ke Google Sheets:", result))
  .catch(console.error);

// Buat kartu Trello
zapierActions.createTrelloCard(
  "Implementasi MCP",
  "Integrasikan Zapier MCP ke MusGo-OS",
  "TRELLO_BOARD_ID",
  "TRELLO_LIST_ID"
)
  .then((result) => console.log("✅ Kartu Trello dibuat:", result))
  .catch(console.error);
```

---
---
---

## **🔹 4.6 Managing App Authentication (Mengelola Autentikasi Aplikasi)**
### **📌 Penjelasan**
**Managing App Authentication** memungkinkan **MusGo-OS** untuk **mengelola koneksi autentikasi** user ke aplikasi eksternal (Slack, Google Drive, dll.). Ini penting karena:
- **User bisa menghubungkan akun mereka** (misal: Slack, Google Drive) ke MusGo-OS.
- **MusGo-OS bisa menyimpan credential** dan **menggunakannya untuk menjalankan action**.

---
### **🚀 Contoh Implementasi: Managing App Authentication**
#### **1. Daftar Koneksi Autentikasi User**
**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierAuth.ts
import axios from "axios";

interface AuthConnection {
  id: string;
  app: string;
  status: string;
  created_at: string;
}

class ZapierAuth {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Daftar koneksi autentikasi user
  async listConnections(): Promise<AuthConnection[]> {
    try {
      const response = await axios.get(`${this.baseUrl}/authentications`, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
        },
      });
      return response.data.authentications;
    } catch (error) {
      console.error("❌ Gagal mendaftar koneksi:", error);
      throw error;
    }
  }

  // Buat koneksi autentikasi baru
  async createConnection(app: string, credentials: Record<string, any>): Promise<AuthConnection> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/authentications`,
        {
          app,
          credentials,
        },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal membuat koneksi:", error);
      throw error;
    }
  }

  // Hapus koneksi autentikasi
  async deleteConnection(authId: string): Promise<void> {
    try {
      await axios.delete(`${this.baseUrl}/authentications/${authId}`, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
        },
      });
    } catch (error) {
      console.error("❌ Gagal menghapus koneksi:", error);
      throw error;
    }
  }
}

// Contoh penggunaan
const zapierAuth = new ZapierAuth("YOUR_ZAPIER_API_KEY");

// Daftar koneksi
zapierAuth.listConnections()
  .then((connections) => console.log("🔑 Koneksi autentikasi:", connections))
  .catch(console.error);

// Buat koneksi Slack
zapierAuth.createConnection("slack", {
  token: "SLACK_TOKEN_USER", // Token dari user
})
  .then((connection) => console.log("✅ Koneksi Slack dibuat:", connection))
  .catch(console.error);

// Hapus koneksi
zapierAuth.deleteConnection("AUTH_ID")
  .then(() => console.log("✅ Koneksi dihapus"))
  .catch(console.error);
```

---
#### **2. Contoh UI untuk Menghubungkan Aplikasi (React)**
**Contoh Kode (React + TypeScript):**
```tsx
// File: src/components/ConnectAppModal.tsx
import React, { useState } from "react";
import { ZapierAuth } from "../services/ZapierAuth";

interface ConnectAppModalProps {
  app: string;
  onConnected: () => void;
  onClose: () => void;
}

const ConnectAppModal: React.FC<ConnectAppModalProps> = ({
  app,
  onConnected,
  onClose,
}) => {
  const [token, setToken] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const zapierAuth = new ZapierAuth("YOUR_ZAPIER_API_KEY");

  const handleConnect = async () => {
    if (!token) {
      setError("Token tidak boleh kosong!");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      await zapierAuth.createConnection(app, { token });
      onConnected();
    } catch (err) {
      setError("Gagal menghubungkan aplikasi. Silakan coba lagi.");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        background: "rgba(0, 0, 0, 0.5)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "20px",
          borderRadius: "10px",
          width: "400px",
        }}
      >
        <h2>Hubungkan {app === "slack" ? "Slack" : app === "google_drive" ? "Google Drive" : app}</h2>
        <p>Masukkan token API untuk menghubungkan akun Anda.</p>

        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>Token API:</label>
          <input
            type="password"
            value={token}
            onChange={(e) => setToken(e.target.value)}
            style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
            placeholder={`Masukkan token ${app}`}
          />
        </div>

        {error && <p style={{ color: "red", marginBottom: "15px" }}>{error}</p>}

        <div style={{ display: "flex", justifyContent: "flex-end", gap: "10px" }}>
          <button
            onClick={onClose}
            style={{ padding: "8px 16px", border: "none", background: "#f0f0f0", cursor: "pointer" }}
          >
            Batal
          </button>
          <button
            onClick={handleConnect}
            disabled={isLoading}
            style={{
              padding: "8px 16px",
              border: "none",
              background: "#4285F4",
              color: "white",
              cursor: "pointer",
              borderRadius: "4px",
            }}
          >
            {isLoading ? "Menghubungkan..." : "Hubungkan"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ConnectAppModal;
```

**Contoh Penggunaan:**
```tsx
// File: src/pages/ConnectedAppsPage.tsx
import React, { useState, useEffect } from "react";
import ConnectAppModal from "../components/ConnectAppModal";
import { ZapierAuth } from "../services/ZapierAuth";

const ConnectedAppsPage: React.FC = () => {
  const [connections, setConnections] = useState<any[]>([]);
  const [selectedApp, setSelectedApp] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const zapierAuth = new ZapierAuth("YOUR_ZAPIER_API_KEY");

  // Ambil daftar koneksi
  useEffect(() => {
    zapierAuth.listConnections()
      .then((data) => setConnections(data))
      .catch(console.error);
  }, []);

  // Daftar aplikasi yang didukung
  const supportedApps = [
    { key: "slack", name: "Slack" },
    { key: "google_drive", name: "Google Drive" },
    { key: "notion", name: "Notion" },
    { key: "trello", name: "Trello" },
  ];

  // Cek apakah aplikasi sudah terhubung
  const isAppConnected = (appKey: string) => {
    return connections.some((conn) => conn.app === appKey);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🔗 Aplikasi Terhubung</h1>
      <p>Hubungkan akun Anda untuk mengaktifkan otomatisasi.</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))", gap: "15px", marginTop: "20px" }}>
        {supportedApps.map((app) => (
          <div
            key={app.key}
            style={{
              border: "1px solid #e0e0e0",
              padding: "15px",
              borderRadius: "8px",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <h3 style={{ margin: 0 }}>{app.name}</h3>
              <p style={{ margin: "5px 0 0 0", color: "#666" }}>
                {isAppConnected(app.key) ? "✅ Terhubung" : "❌ Belum terhubung"}
              </p>
            </div>
            {!isAppConnected(app.key) && (
              <button
                onClick={() => {
                  setSelectedApp(app.key);
                  setIsModalOpen(true);
                }}
                style={{
                  padding: "5px 10px",
                  background: "#4285F4",
                  color: "white",
                  border: "none",
                  borderRadius: "4px",
                  cursor: "pointer",
                }}
              >
                Hubungkan
              </button>
            )}
          </div>
        ))}
      </div>

      {isModalOpen && selectedApp && (
        <ConnectAppModal
          app={selectedApp}
          onConnected={() => {
            setIsModalOpen(false);
            // Refresh daftar koneksi
            zapierAuth.listConnections()
              .then((data) => setConnections(data))
              .catch(console.error);
          }}
          onClose={() => setIsModalOpen(false)}
        />
      )}
    </div>
  );
};

export default ConnectedAppsPage;
```

---
---
---

## **🔹 4.7 Zap Templates (Template Otomatisasi)**
### **📌 Penjelasan**
**Zap Templates** adalah **template siap pakai** yang memungkinkan **user MusGo-OS** untuk **membuat Zap dengan cepat** tanpa perlu mengkonfigurasi dari nol. Template ini bisa **disesuaikan** dengan kebutuhan MusGo-OS.

**Manfaat untuk MusGo-OS:**
- **User bisa membuat Zap dengan 1 klik**.
- **MusGo-OS bisa menawarkan template otomatisasi** (misal: "AI Agent → Slack", "Google Drive → Notion").

---
### **🚀 Contoh Implementasi: Zap Templates**
#### **1. Daftar Template Zap**
**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierTemplates.ts
import axios from "axios";

interface ZapTemplate {
  id: string;
  name: string;
  description: string;
  trigger: {
    app: string;
    event: string;
  };
  action: {
    app: string;
    event: string;
  };
}

class ZapierTemplates {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Daftar template Zap
  async listTemplates(): Promise<ZapTemplate[]> {
    try {
      const response = await axios.get(`${this.baseUrl}/zap-templates`, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
        },
      });
      return response.data.templates;
    } catch (error) {
      console.error("❌ Gagal mendaftar template:", error);
      throw error;
    }
  }

  // Buat Zap dari template
  async createZapFromTemplate(templateId: string, data: Record<string, any> = {}): Promise<{ id: string }> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/zap-templates/${templateId}/create`,
        { data },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal membuat Zap dari template:", error);
      throw error;
    }
  }
}

// Contoh penggunaan
const zapierTemplates = new ZapierTemplates("YOUR_ZAPIER_API_KEY");

// Daftar template
zapierTemplates.listTemplates()
  .then((templates) => console.log("📋 Template Zap:", templates))
  .catch(console.error);

// Buat Zap dari template
zapierTemplates.createZapFromTemplate("TEMPLATE_ID", {
  channel: "#musgo-updates", // Override data template
})
  .then((zap) => console.log("✅ Zap dibuat dari template:", zap))
  .catch(console.error);
```

---
#### **2. Contoh UI untuk Template Zap (React)**
**Contoh Kode (React + TypeScript):**
```tsx
// File: src/components/ZapTemplates.tsx
import React, { useState, useEffect } from "react";
import { ZapierTemplates } from "../services/ZapierTemplates";

interface ZapTemplate {
  id: string;
  name: string;
  description: string;
  trigger: {
    app: string;
    event: string;
  };
  action: {
    app: string;
    event: string;
  };
}

const ZapTemplates: React.FC = () => {
  const [templates, setTemplates] = useState<ZapTemplate[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [selectedTemplate, setSelectedTemplate] = useState<ZapTemplate | null>(null);

  const zapierTemplates = new ZapierTemplates("YOUR_ZAPIER_API_KEY");

  // Ambil daftar template
  useEffect(() => {
    zapierTemplates.listTemplates()
      .then((data) => {
        setTemplates(data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setIsLoading(false);
      });
  }, []);

  // Buat Zap dari template
  const handleCreateZap = async (template: ZapTemplate) => {
    try {
      setIsLoading(true);
      const zap = await zapierTemplates.createZapFromTemplate(template.id, {
        channel: "#musgo-updates", // Default channel
      });
      alert(`✅ Zap dibuat dari template "${template.name}"! ID: ${zap.id}`);
    } catch (error) {
      console.error(error);
      alert("❌ Gagal membuat Zap dari template.");
    } finally {
      setIsLoading(false);
    }
  };

  // Template kustom untuk MusGo-OS
  const musgoTemplates: ZapTemplate[] = [
    {
      id: "musgo_ai_to_slack",
      name: "AI Agent → Slack",
      description: "Kirim notifikasi ke Slack saat AI Agent menyelesaikan tugas.",
      trigger: { app: "musgo_os_2in1", event: "Task Completed" },
      action: { app: "slack", event: "Send Channel Message" },
    },
    {
      id: "musgo_google_drive_to_notion",
      name: "Google Drive → Notion",
      description: "Simpan data file Google Drive ke database Notion.",
      trigger: { app: "google_drive", event: "New File in Folder" },
      action: { app: "notion", event: "Create Database Row" },
    },
    {
      id: "musgo_trello_to_email",
      name: "Trello → Email",
      description: "Kirim email saat kartu Trello dipindah ke list 'Done'.",
      trigger: { app: "trello", event: "Card Moved to List" },
      action: { app: "gmail", event: "Send Email" },
    },
  ];

  return (
    <div style={{ padding: "20px" }}>
      <h1>📋 Template Zap untuk MusGo-OS</h1>
      <p>Pilih template untuk membuat Zap dengan cepat!</p>

      {isLoading ? (
        <p>Memuat template...</p>
      ) : (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: "15px", marginTop: "20px" }}>
          {[...musgoTemplates, ...templates].map((template) => (
            <div
              key={template.id}
              style={{
                border: "1px solid #e0e0e0",
                padding: "15px",
                borderRadius: "8px",
              }}
            >
              <h3 style={{ margin: 0 }}>{template.name}</h3>
              <p style={{ margin: "5px 0 10px 0", color: "#666" }}>{template.description}</p>
              <div style={{ display: "flex", justifyContent: "space-between", marginTop: "10px" }}>
                <div>
                  <small>Trigger: {template.trigger.app} → {template.trigger.event}</small>
                  <br />
                  <small>Action: {template.action.app} → {template.action.event}</small>
                </div>
                <button
                  onClick={() => handleCreateZap(template)}
                  style={{
                    padding: "5px 10px",
                    background: "#4285F4",
                    color: "white",
                    border: "none",
                    borderRadius: "4px",
                    cursor: "pointer",
                  }}
                >
                  Gunakan Template
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ZapTemplates;
```

---
---
---

## **🔹 4.8 AI Workflows (Zap Guesser)**
### **📌 Penjelasan**
**Zap Guesser** adalah **fitur AI** dari Zapier yang memungkinkan **user membuat Zap hanya dengan deskripsi bahasa alami**. Misal:
> *"Buatkan Zap yang mengirim notifikasi ke Slack setiap kali ada file baru di Google Drive."*

Zapier akan **mencoba menebak** trigger dan action yang sesuai.

**Manfaat untuk MusGo-OS:**
- **User bisa membuat Zap dengan perintah suara/teks**.
- **AI Agent MusGo-OS bisa menggunakan Zap Guesser** untuk **membuat Zap otomatis**.

---
### **🚀 Contoh Implementasi: Zap Guesser**
**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierAI.ts
import axios from "axios";

interface ZapGuess {
  trigger: {
    app: string;
    event: string;
    data: Record<string, any>;
  };
  action: {
    app: string;
    event: string;
    data: Record<string, any>;
  };
  confidence: number; // Tingkat kepercayaan (0-1)
}

class ZapierAI {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Gunakan Zap Guesser untuk menebak Zap
  async guessZap(prompt: string): Promise<ZapGuess[]> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/ai/guess-zap`,
        { prompt },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data.guesses;
    } catch (error) {
      console.error("❌ Gagal menebak Zap:", error);
      throw error;
    }
  }

  // Buat Zap dari tebakan
  async createZapFromGuess(prompt: string): Promise<{ id: string }> {
    const guesses = await this.guessZap(prompt);
    if (guesses.length === 0) {
      throw new Error("Tidak ada tebakan Zap yang cocok.");
    }

    // Ambil tebakan dengan confidence tertinggi
    const bestGuess = guesses[0];

    // Buat Zap
    const zap = await this.createZap({
      name: `AI Guess: ${prompt.substring(0, 50)}...`,
      steps: [
        {
          id: "trigger_1",
          app: bestGuess.trigger.app,
          action: bestGuess.trigger.event,
          data: bestGuess.trigger.data,
        },
        {
          id: "action_1",
          app: bestGuess.action.app,
          action: bestGuess.action.event,
          data: bestGuess.action.data,
        },
      ],
    });

    return zap;
  }

  // Buat Zap (helper function)
  private async createZap(zapData: { name: string; steps: any[] }): Promise<{ id: string }> {
    try {
      const response = await axios.post(`${this.baseUrl}/zaps`, zapData, {
        headers: {
          "Authorization": `Bearer ${this.apiKey}`,
          "Content-Type": "application/json",
        },
      });
      return response.data;
    } catch (error) {
      console.error("❌ Gagal membuat Zap:", error);
      throw error;
    }
  }
}

// Contoh penggunaan
const zapierAI = new ZapierAI("YOUR_ZAPIER_API_KEY");

// Gunakan Zap Guesser
zapierAI.guessZap("Buatkan Zap yang mengirim notifikasi ke Slack setiap kali ada file baru di Google Drive")
  .then((guesses) => {
    console.log("🤖 Tebakan Zap:");
    guesses.forEach((guess, i) => {
      console.log(`\n${i + 1}. Trigger: ${guess.trigger.app} → ${guess.trigger.event}`);
      console.log(`   Action: ${guess.action.app} → ${guess.action.event}`);
      console.log(`   Confidence: ${(guess.confidence * 100).toFixed(2)}%`);
    });
  })
  .catch(console.error);

// Buat Zap dari tebakan
zapierAI.createZapFromGuess("Buatkan Zap yang mengirim email ke dhani@musgo-os.com saat kartu Trello dipindah ke list 'Done'")
  .then((zap) => console.log("✅ Zap dibuat dari tebakan AI:", zap))
  .catch(console.error);
```

**Output Contoh:**
```
🤖 Tebakan Zap:

1. Trigger: google_drive → New File in Folder
   Action: slack → Send Channel Message
   Confidence: 95.50%

2. Trigger: google_drive → New File
   Action: slack → Send Message
   Confidence: 85.20%

✅ Zap dibuat dari tebakan AI: { id: "ZAP_789" }
```

---
#### **2. Contoh: AI Agent MusGo-OS + Zap Guesser**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, buatkan Zap yang mengirim notifikasi ke Slack jika ada tugas baru di Trello."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima perintah.
2. **AI Agent menggunakan Zap Guesser** untuk **menebak Zap** yang sesuai.
3. **AI Agent membuat Zap** dari tebakan terbaik.

**Contoh Kode:**
```typescript
// Fungsi untuk memproses perintah user
async function handleUserCommand(command: string): Promise<string> {
  command = command.toLowerCase();

  if (command.includes("buatkan zap")) {
    try {
      const zap = await zapierAI.createZapFromGuess(command);
      return `✅ Zap dibuat dari perintah Anda! ID: ${zap.id}`;
    } catch (error) {
      return `❌ Gagal membuat Zap: ${error.message}`;
    }
  }

  return "Maaf, saya tidak mengerti perintah Anda.";
}

// Simulasi
handleUserCommand("MusGo, buatkan Zap yang mengirim notifikasi ke Slack jika ada tugas baru di Trello")
  .then(console.log);
```

**Output:**
```
✅ Zap dibuat dari perintah Anda! ID: ZAP_101
```

---
---
---

## **🔹 4.9 Sponsor User Automation (Otomatisasi untuk User Tanpa Biaya)**
### **📌 Penjelasan**
**Sponsor User Automation** memungkinkan **MusGo-OS** untuk **menawarkan otomatisasi Zapier kepada user tanpa biaya** (user tidak perlu bayar langganan Zapier). Ini berguna untuk:
- **Menawarkan fitur premium** (misal: otomatisasi tanpa batas).
- **Meningkatkan adopsi MusGo-OS** (user tidak perlu keluar dari MusGo-OS).

**Cara Kerja:**
1. **MusGo-OS mendaftar sebagai sponsor** di Zapier.
2. **MusGo-OS menambahkan user ke program sponsor**.
3. **User bisa menggunakan Zapier tanpa biaya** (selama dalam program sponsor).

---
### **🚀 Contoh Implementasi: Sponsor User Automation**
**Contoh Kode (TypeScript):**
```typescript
// File: src/services/ZapierSponsor.ts
import axios from "axios";

interface SponsorEnrollment {
  id: string;
  userId: string;
  status: "active" | "inactive";
  createdAt: string;
}

class ZapierSponsor {
  private apiKey: string;
  private baseUrl: string = "https://api.zapier.com/v2";

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  // Daftarkan user ke program sponsor
  async enrollUser(userId: string, promotionId: string): Promise<SponsorEnrollment> {
    try {
      const response = await axios.post(
        `${this.baseUrl}/promotions/${promotionId}/enrollments`,
        { userId },
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
            "Content-Type": "application/json",
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal mendaftarkan user:", error);
      throw error;
    }
  }

  // Cek status enrollment user
  async getEnrollment(promotionId: string, enrollmentId: string): Promise<SponsorEnrollment> {
    try {
      const response = await axios.get(
        `${this.baseUrl}/promotions/${promotionId}/enrollments/${enrollmentId}`,
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error("❌ Gagal mendapatkan enrollment:", error);
      throw error;
    }
  }

  // Hapus enrollment user
  async deleteEnrollment(promotionId: string, enrollmentId: string): Promise<void> {
    try {
      await axios.delete(
        `${this.baseUrl}/promotions/${promotionId}/enrollments/${enrollmentId}`,
        {
          headers: {
            "Authorization": `Bearer ${this.apiKey}`,
          },
        }
      );
    } catch (error) {
      console.error("❌ Gagal menghapus enrollment:", error);
      throw error;
    }
  }
}

// Contoh penggunaan
const zapierSponsor = new ZapierSponsor("YOUR_ZAPIER_API_KEY");

// Daftarkan user ke program sponsor
zapierSponsor.enrollUser("USER_ID_123", "PROMOTION_ID_456")
  .then((enrollment) => console.log("✅ User didaftarkan ke program sponsor:", enrollment))
  .catch(console.error);

// Cek status enrollment
zapierSponsor.getEnrollment("PROMOTION_ID_456", "ENROLLMENT_ID_789")
  .then((enrollment) => console.log("📋 Status enrollment:", enrollment))
  .catch(console.error);
```

---
#### **2. Contoh UI untuk Sponsor User (React)**
**Contoh Kode (React + TypeScript):**
```tsx
// File: src/components/SponsorUserModal.tsx
import React, { useState } from "react";
import { ZapierSponsor } from "../services/ZapierSponsor";

interface SponsorUserModalProps {
  userId: string;
  onEnrolled: () => void;
  onClose: () => void;
}

const SponsorUserModal: React.FC<SponsorUserModalProps> = ({
  userId,
  onEnrolled,
  onClose,
}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const zapierSponsor = new ZapierSponsor("YOUR_ZAPIER_API_KEY");
  const promotionId = "PROMOTION_ID_456"; // ID program sponsor MusGo-OS

  const handleEnroll = async () => {
    setIsLoading(true);
    setError(null);

    try {
      await zapierSponsor.enrollUser(userId, promotionId);
      onEnrolled();
    } catch (err) {
      setError("Gagal mendaftarkan user ke program sponsor. Silakan coba lagi.");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        background: "rgba(0, 0, 0, 0.5)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "20px",
          borderRadius: "10px",
          width: "400px",
        }}
      >
        <h2>Daftarkan User ke Program Sponsor</h2>
        <p>User ini akan mendapatkan akses otomatisasi Zapier tanpa biaya.</p>

        {error && <p style={{ color: "red", marginBottom: "15px" }}>{error}</p>}

        <div style={{ display: "flex", justifyContent: "flex-end", gap: "10px", marginTop: "20px" }}>
          <button
            onClick={onClose}
            style={{ padding: "8px 16px", border: "none", background: "#f0f0f0", cursor: "pointer" }}
          >
            Batal
          </button>
          <button
            onClick={handleEnroll}
            disabled={isLoading}
            style={{
              padding: "8px 16px",
              border: "none",
              background: "#4285F4",
              color: "white",
              cursor: "pointer",
              borderRadius: "4px",
            }}
          >
            {isLoading ? "Mendaftarkan..." : "Daftarkan"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default SponsorUserModal;
```

---
---
---
# **📌 PART 4: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 4 (Powered by Zapier)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Embed Zap Editor** | User bisa membuat Zap langsung di MusGo-OS | ✅ **Contoh kode tersedia** |
| **Workflow API** | Buat/kelola Zap secara programatik | ✅ **Contoh kode tersedia** |
| **Running Actions** | Jalankan action Zapier dari MusGo-OS | ✅ **Contoh kode tersedia** |
| **Managing Auth** | Kelola koneksi autentikasi user | ✅ **Contoh kode tersedia** |
| **Zap Templates** | Template siap pakai untuk user | ✅ **Contoh kode tersedia** |
| **Zap Guesser** | Buat Zap dengan AI (bahasa alami) | ✅ **Contoh kode tersedia** |
| **Sponsor User** | Otomatisasi gratis untuk user | ✅ **Contoh kode tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Daftar sebagai Developer di Zapier** (jika belum) → [Zapier Developer Platform](https://zapier.com/developer).
- [ ] **Dapatkan API Key** untuk Powered by Zapier.
- [ ] **Integrasikan Embedded Zap Editor** ke dashboard MusGo-OS (gunakan contoh kode di atas).
- [ ] **Test Workflow API** (buat Zap, jalankan action, dll.).

### **2. Mid-Term (1 Bulan)**
- [ ] **Implementasikan Managing Auth** (user bisa menghubungkan Slack, Google Drive, dll.).
- [ ] **Buat Zap Templates** untuk MusGo-OS (misal: AI Agent → Slack).
- [ ] **Integrasikan Zap Guesser** ke AI Agent MusGo-OS.
- [ ] **Setup Sponsor User** (jika ingin menawarkan otomatisasi gratis).

### **3. Long-Term (3+ Bulan)**
- [ ] **Optimalkan UI/UX** untuk embedding Zapier.
- [ ] **Dokumentasikan integrasi** untuk user MusGo-OS.
- [ ] **Promosikan fitur otomatisasi** ke user.

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 5: White Label** (Untuk branding MusGo-OS sendiri di Zapier)
   - [ ] **Part 6: Workflow API Reference** (Untuk referensi lengkap REST API)
   - [ ] **Part 7: Advanced Use Cases** (Misal: Multi-step Zaps, Error Handling, dll.)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + Notion + Slack)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi API untuk MusGo-OS + Zapier**?
   - [ ] **Contoh deployment (Docker, Kubernetes)**?

3. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **MusGo-OS → Slack → Google Sheets**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 5: White Label** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi** untuk **MusGo-OS 2in1** dari dokumentasi **Zapier White Label**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN WHITE LABEL (PART 5)**
*Terjemahan + Implementasi untuk Branding MusGo-OS di Zapier*

---

---

## **🔹 5.1 Overview White Label**
### **📌 Penjelasan (Bahasa Indonesia)**
**Zapier White Label** memungkinkan **MusGo-OS** untuk **mengintegrasikan Zapier di bawah merek sendiri** (tanpa branding Zapier). Dengan White Label, Anda bisa:
✅ **Menampilkan Zapier sebagai bagian dari MusGo-OS** (tanpa logo/branding Zapier).
✅ **Mengelola koneksi user** (tanpa user perlu login ke Zapier).
✅ **Menggunakan domain dan branding MusGo-OS** (misal: `automation.musgo-os.com`).
✅ **Menawarkan otomatisasi sebagai fitur native MusGo-OS**.

**Manfaat untuk MusGo-OS:**
- **User merasa menggunakan fitur MusGo-OS**, bukan Zapier.
- **Meningkatkan brand awareness MusGo-OS**.
- **Kontrol penuh atas UX** (user experience).

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: Embed Zapier sebagai Fitur Native MusGo-OS**
**Skenario:**
User MusGo-OS ingin **membuat otomatisasi** (Zap) **tanpa tahu bahwa mereka menggunakan Zapier**.

**Cara Kerja:**
1. **MusGo-OS** menampilkan **UI otomatisasi** (dengan branding MusGo-OS).
2. **User membuat otomatisasi** (misal: Google Drive → Slack).
3. **MusGo-OS** menggunakan **White Label API** untuk **membuat Zap di belakang layar**.

**Arsitektur:**
```
User → MusGo-OS UI (Branding MusGo-OS) → White Label API → Zapier → Aplikasi Eksternal
```

**Contoh UI (React + TypeScript):**
```tsx
// File: src/components/MusGoAutomationBuilder.tsx
import React, { useState } from "react";

interface AutomationStep {
  id: string;
  app: string;
  action: string;
  data: Record<string, any>;
}

const MusGoAutomationBuilder: React.FC = () => {
  const [steps, setSteps] = useState<AutomationStep[]>([]);
  const [availableApps] = useState<string[]>([
    "Google Drive",
    "Slack",
    "Notion",
    "Trello",
    "Gmail",
  ]);

  // Tambah step baru
  const addStep = () => {
    setSteps([
      ...steps,
      {
        id: Date.now().toString(),
        app: "",
        action: "",
        data: {},
      },
    ]);
  };

  // Hapus step
  const removeStep = (id: string) => {
    setSteps(steps.filter((step) => step.id !== id));
  };

  // Update step
  const updateStep = (id: string, field: keyof AutomationStep, value: any) => {
    setSteps(
      steps.map((step) =>
        step.id === id ? { ...step, [field]: value } : step
      )
    );
  };

  // Simpan otomatisasi
  const saveAutomation = async () => {
    if (steps.length < 2) {
      alert("Otomatisasi harus memiliki minimal 1 trigger dan 1 action.");
      return;
    }

    // Kirim ke backend MusGo-OS untuk dibuatkan Zap via White Label API
    const response = await fetch("/api/automation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ steps }),
    });

    if (response.ok) {
      const data = await response.json();
      alert(`✅ Otomatisasi berhasil dibuat! ID: ${data.id}`);
    } else {
      alert("❌ Gagal membuat otomatisasi.");
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
        <h1>🔄 Pembuat Otomatisasi MusGo-OS</h1>
        <button
          onClick={saveAutomation}
          style={{
            padding: "10px 20px",
            background: "#4285F4",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Simpan Otomatisasi
        </button>
      </div>

      <div style={{ marginBottom: "20px" }}>
        <p>Buat otomatisasi antara aplikasi favorit Anda.</p>
        <button
          onClick={addStep}
          style={{
            padding: "8px 16px",
            background: "#f0f0f0",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          + Tambah Step
        </button>
      </div>

      {steps.length === 0 ? (
        <p style={{ textAlign: "center", color: "#999" }}>
          Belum ada step. Klik "Tambah Step" untuk memulai.
        </p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
          {steps.map((step, index) => (
            <div
              key={step.id}
              style={{
                border: "1px solid #e0e0e0",
                padding: "15px",
                borderRadius: "8px",
                position: "relative",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "10px" }}>
                <h3 style={{ margin: 0 }}>Step {index + 1}</h3>
                <button
                  onClick={() => removeStep(step.id)}
                  style={{
                    background: "none",
                    border: "none",
                    color: "#ff4444",
                    cursor: "pointer",
                  }}
                >
                  ✕
                </button>
              </div>

              <div style={{ marginBottom: "10px" }}>
                <label style={{ display: "block", marginBottom: "5px" }}>Aplikasi:</label>
                <select
                  value={step.app}
                  onChange={(e) => updateStep(step.id, "app", e.target.value)}
                  style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                >
                  <option value="">Pilih Aplikasi</option>
                  {availableApps.map((app) => (
                    <option key={app} value={app}>
                      {app}
                    </option>
                  ))}
                </select>
              </div>

              {step.app && (
                <div style={{ marginBottom: "10px" }}>
                  <label style={{ display: "block", marginBottom: "5px" }}>Action:</label>
                  <select
                    value={step.action}
                    onChange={(e) => updateStep(step.id, "action", e.target.value)}
                    style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                  >
                    <option value="">Pilih Action</option>
                    {step.app === "Google Drive" && (
                      <>
                        <option value="New File in Folder">File Baru di Folder</option>
                        <option value="New File">File Baru</option>
                      </>
                    )}
                    {step.app === "Slack" && (
                      <>
                        <option value="Send Channel Message">Kirim Pesan ke Channel</option>
                        <option value="Send Direct Message">Kirim Pesan Langsung</option>
                      </>
                    )}
                    {step.app === "Notion" && (
                      <>
                        <option value="Create Database Row">Buat Baris Database</option>
                        <option value="Update Database Row">Update Baris Database</option>
                      </>
                    )}
                  </select>
                </div>
              )}

              {step.app && step.action && (
                <div>
                  <label style={{ display: "block", marginBottom: "5px" }}>Data:</label>
                  {step.action === "Send Channel Message" && (
                    <div style={{ marginBottom: "10px" }}>
                      <label style={{ display: "block", marginBottom: "5px" }}>Channel:</label>
                      <input
                        type="text"
                        value={step.data.channel || ""}
                        onChange={(e) => updateStep(step.id, "data", { ...step.data, channel: e.target.value })}
                        style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                        placeholder="#musgo-updates"
                      />
                    </div>
                  )}
                  {step.action === "Send Channel Message" && (
                    <div style={{ marginBottom: "10px" }}>
                      <label style={{ display: "block", marginBottom: "5px" }}>Pesan:</label>
                      <textarea
                        value={step.data.text || ""}
                        onChange={(e) => updateStep(step.id, "data", { ...step.data, text: e.target.value })}
                        style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px", minHeight: "100px" }}
                        placeholder="Masukkan pesan..."
                      />
                    </div>
                  )}
                  {step.action === "New File in Folder" && (
                    <div style={{ marginBottom: "10px" }}>
                      <label style={{ display: "block", marginBottom: "5px" }}>Folder:</label>
                      <input
                        type="text"
                        value={step.data.folder || ""}
                        onChange={(e) => updateStep(step.id, "data", { ...step.data, folder: e.target.value })}
                        style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                        placeholder="Proyek MusGo-OS"
                      />
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MusGoAutomationBuilder;
```

---
---
---

## **🔹 5.2 Partner Onboarding (Pendaftaran Mitra)**
### **📌 Penjelasan**
Untuk menggunakan **White Label**, **MusGo-OS** harus **mendaftar sebagai mitra (partner) Zapier**. Proses ini meliputi:
1. **Mendaftar sebagai Partner** di [Zapier Partner Program](https://zapier.com/partner).
2. **Mengkonfigurasi JWKS (JSON Web Key Set)** untuk **token validation**.
3. **Mengatur callback URL** untuk **OAuth flow**.
4. **Mendapatkan JWT expectations** (format token yang diharapkan).

**Manfaat:**
- **Mendapatkan akses ke White Label API**.
- **Bisa menawarkan Zapier di bawah merek MusGo-OS**.

---
### **🚀 Contoh Implementasi: Partner Onboarding**
#### **1. Mendaftar sebagai Partner**
1. Buka [Zapier Partner Program](https://zapier.com/partner).
2. Klik **"Become a Partner"**.
3. Isi formulir dengan detail **MusGo-OS** (nama, deskripsi, dll.).
4. Tunggu **persetujuan dari Zapier** (biasanya 1-2 minggu).

---
#### **2. Konfigurasi JWKS (JSON Web Key Set)**
**JWKS** digunakan untuk **validasi token JWT** yang dikirim oleh MusGo-OS ke Zapier.

**Contoh JWKS (untuk MusGo-OS):**
```json
{
  "keys": [
    {
      "kty": "RSA",
      "use": "sig",
      "kid": "MUSGO_OS_KEY_1",
      "alg": "RS256",
      "n": "your_modulus_here",
      "e": "AQAB",
      "x5c": ["your_certificate_here"]
    }
  ]
}
```

**Cara Generate JWKS:**
1. **Buat private key** (RSA 2048-bit):
   ```bash
   openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
   ```
2. **Ekstrak public key** (untuk JWKS):
   ```bash
   openssl rsa -pubout -in private_key.pem -out public_key.pem
   ```
3. **Konversi ke JWKS** (gunakan library seperti `jose`):
   ```bash
   npm install jose
   ```
   ```javascript
   const { JWK } = require('jose');
   const publicKey = require('fs').readFileSync('public_key.pem', 'utf8');
   const jwk = JWK.fromPEM(publicKey);
   console.log(JSON.stringify({ keys: [jwk] }, null, 2));
   ```

---
#### **3. Konfigurasi Callback URL**
**Callback URL** digunakan untuk **OAuth flow** (saat user menghubungkan akun mereka).

**Contoh Callback URL untuk MusGo-OS:**
| Endpoint | Deskripsi | Contoh URL |
|----------|-----------|------------|
| **OAuth Redirect URI** | URL untuk redirect setelah user login | `https://musgo-os.com/oauth/callback` |
| **Token Exchange** | URL untuk exchange token | `https://musgo-os.com/api/zapier/token-exchange` |
| **Connection Flow** | URL untuk connection flow | `https://musgo-os.com/api/zapier/connection` |

---
#### **4. JWT Expectations**
Zapier mengharapkan **JWT (JSON Web Token)** dengan format tertentu untuk **autentikasi**.

**Contoh JWT Payload:**
```json
{
  "iss": "MusGo-OS",          // Issuer
  "sub": "USER_ID_123",       // User ID
  "aud": "zapier.com",        // Audience
  "exp": 1735689600,          // Expiration time (timestamp)
  "iat": 1735603200,          // Issued at (timestamp)
  "jti": "UNIQUE_ID_123",     // JWT ID
  "scp": ["read", "write"],   // Scopes
  "app": "musgo_os_2in1"      // App key
}
```

**Contoh Kode untuk Generate JWT (Node.js):**
```bash
npm install jsonwebtoken jose
```

```javascript
const jwt = require('jsonwebtoken');
const fs = require('fs');

// Baca private key
const privateKey = fs.readFileSync('private_key.pem', 'utf8');

// Generate JWT
function generateJWT(userId, scopes = ['read', 'write']) {
  const payload = {
    iss: "MusGo-OS",
    sub: userId,
    aud: "zapier.com",
    exp: Math.floor(Date.now() / 1000) + 3600, // 1 jam
    iat: Math.floor(Date.now() / 1000),
    jti: `jwt_${Date.now()}`,
    scp: scopes,
    app: "musgo_os_2in1",
  };

  const token = jwt.sign(payload, privateKey, { algorithm: 'RS256', keyid: 'MUSGO_OS_KEY_1' });
  return token;
}

// Contoh penggunaan
const token = generateJWT("USER_ID_123");
console.log("JWT Token:", token);
```

---
---
---

## **🔹 5.3 Connection Flow (Alur Koneksi)**
### **📌 Penjelasan**
**Connection Flow** adalah **proses autentikasi** yang memungkinkan **user MusGo-OS** untuk **menghubungkan akun mereka** (Slack, Google Drive, dll.) **ke MusGo-OS** (tanpa tahu bahwa mereka menggunakan Zapier).

**Tipe Connection Flow:**
1. **Popup Flow**: User menghubungkan akun via **popup window**.
2. **Redirect Flow**: User diarahkan ke **halaman autentikasi Zapier**, lalu redirect kembali ke MusGo-OS.

---
### **🚀 Contoh Implementasi: Connection Flow**
#### **1. Popup Flow (Rekomendasi untuk MusGo-OS)**
**Cara Kerja:**
1. **User klik "Hubungkan Slack"** di MusGo-OS.
2. **MusGo-OS membuka popup** ke Zapier untuk autentikasi.
3. **User login ke Slack** (via Zapier).
4. **Zapier mengembalikan token** ke MusGo-OS.
5. **MusGo-OS menyimpan token** untuk user.

**Contoh Kode (Frontend - React):**
```tsx
// File: src/components/ConnectAppButton.tsx
import React from "react";

interface ConnectAppButtonProps {
  app: string;
  onConnected: (token: string) => void;
}

const ConnectAppButton: React.FC<ConnectAppButtonProps> = ({ app, onConnected }) => {
  const handleConnect = () => {
    // Buka popup untuk connection flow
    const width = 600;
    const height = 600;
    const left = (window.innerWidth - width) / 2;
    const top = (window.innerHeight - height) / 2;

    const popup = window.open(
      `https://zapier.com/connection-flow?app=${app}&client_id=YOUR_CLIENT_ID&redirect_uri=${encodeURIComponent("https://musgo-os.com/oauth/callback")}`,
      "ZapierConnection",
      `width=${width},height=${height},top=${top},left=${left}`
    );

    // Listen untuk pesan dari popup
    const checkPopup = setInterval(() => {
      if (popup?.closed) {
        clearInterval(checkPopup);
        // Cek apakah user berhasil terhubung
        const token = localStorage.getItem(`zapier_token_${app}`);
        if (token) {
          onConnected(token);
        }
      }
    }, 500);
  };

  return (
    <button
      onClick={handleConnect}
      style={{
        padding: "10px 20px",
        background: "#4285F4",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
      }}
    >
      Hubungkan {app}
    </button>
  );
};

export default ConnectAppButton;
```

---
#### **2. Redirect Flow**
**Cara Kerja:**
1. **User klik "Hubungkan Slack"** di MusGo-OS.
2. **MusGo-OS redirect user** ke Zapier untuk autentikasi.
3. **User login ke Slack** (via Zapier).
4. **Zapier redirect kembali** ke MusGo-OS dengan **code**.
5. **MusGo-OS exchange code** untuk **token**.

**Contoh Kode (Backend - Python FastAPI):**
```python
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
import httpx
import secrets

router = APIRouter()

# Dummy database untuk menyimpan token
tokens_db = {}

@router.get("/oauth/authorize")
async def oauth_authorize(app: str, redirect_uri: str):
    """Redirect user ke Zapier untuk autentikasi"""
    # Simpan state untuk CSRF protection
    state = secrets.token_urlsafe(16)
    tokens_db[state] = {"app": app, "redirect_uri": redirect_uri}

    # Redirect ke Zapier
    zapier_auth_url = (
        f"https://zapier.com/oauth/authorize?"
        f"client_id=YOUR_CLIENT_ID&"
        f"response_type=code&"
        f"redirect_uri={redirect_uri}&"
        f"state={state}&"
        f"scope=read write&"
        f"app={app}"
    )
    return RedirectResponse(url=zapier_auth_url)

@router.get("/oauth/callback")
async def oauth_callback(request: Request, code: str, state: str):
    """Handle callback dari Zapier"""
    if state not in tokens_db:
        raise HTTPException(status_code=400, detail="Invalid state")

    # Exchange code untuk token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://zapier.com/oauth/token",
            data={
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": tokens_db[state]["redirect_uri"],
            },
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to exchange code for token")

        token_data = response.json()
        access_token = token_data["access_token"]

        # Simpan token untuk user
        tokens_db[state]["access_token"] = access_token

        # Redirect kembali ke halaman asli
        return RedirectResponse(url=f"{tokens_db[state]['redirect_uri']}?token={access_token}")

# Tambahkan ke FastAPI app
from fastapi import FastAPI
app = FastAPI()
app.include_router(router)
```

---
---
---

## **🔹 5.4 Token Exchange (Pertukaran Token)**
### **📌 Penjelasan**
**Token Exchange** adalah **proses pertukaran token** antara **MusGo-OS** dan **Zapier**. Ada **2 pattern**:
1. **MCP Pattern**: Untuk **AI Agent** (menggunakan MCP).
2. **Actions/Triggers Pattern**: Untuk **otomatisasi** (menggunakan Workflow API).

---
### **🚀 Contoh Implementasi: Token Exchange**
#### **1. MCP Pattern (Untuk AI Agent)**
**Cara Kerja:**
1. **AI Agent MusGo-OS** meminta **JWT** dari backend MusGo-OS.
2. **Backend MusGo-OS** generate **JWT** dan mengirimkannya ke AI Agent.
3. **AI Agent** menggunakan **JWT** untuk **mengakses Zapier MCP**.

**Contoh Kode (Backend - Python FastAPI):**
```python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import jwt
import datetime
from typing import Optional

router = APIRouter()

# Secret key untuk JWT (ganti dengan private key asli)
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"

class TokenRequest(BaseModel):
    user_id: str
    scopes: list = ["read", "write"]

@router.post("/api/zapier/token")
async def get_zapier_token(request: TokenRequest):
    """Generate JWT untuk Zapier MCP"""
    payload = {
        "iss": "MusGo-OS",
        "sub": request.user_id,
        "aud": "zapier.com",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.utcnow(),
        "scp": request.scopes,
        "app": "musgo_os_2in1",
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "Bearer", "expires_in": 3600}

# Tambahkan ke FastAPI app
app.include_router(router)
```

**Contoh Kode (AI Agent - Python):**
```python
import requests
import jwt

# Ambil token dari backend MusGo-OS
def get_zapier_token(user_id: str):
    response = requests.post(
        "https://musgo-os.com/api/zapier/token",
        json={"user_id": user_id, "scopes": ["read", "write"]}
    )
    if response.status_code != 200:
        raise Exception("Gagal mendapatkan token")
    return response.json()["access_token"]

# Gunakan token untuk Zapier MCP
def call_zapier_mcp(token: str, tool: str, params: dict):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.post(
        "https://api.zapier.com/v2/mcp",
        json={"tool": tool, "params": params},
        headers=headers
    )
    return response.json()

# Contoh penggunaan
token = get_zapier_token("USER_ID_123")
result = call_zapier_mcp(token, "zapier_list_apps", {})
print("Aplikasi yang tersedia:", result["apps"])
```

---
#### **2. Actions/Triggers Pattern (Untuk Otomatisasi)**
**Cara Kerja:**
1. **User menghubungkan akun** (misal: Slack) ke MusGo-OS.
2. **MusGo-OS menerima token** dari Zapier.
3. **MusGo-OS menyimpan token** untuk user.
4. **MusGo-OS menggunakan token** untuk **menjalankan action/trigger**.

**Contoh Kode (Backend - Python FastAPI):**
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

class RunActionRequest(BaseModel):
    app: str
    action: str
    data: dict
    user_id: str

@router.post("/api/zapier/run-action")
async def run_zapier_action(request: RunActionRequest):
    """Jalankan action Zapier dengan token user"""
    # Ambil token user dari database
    user_token = get_user_token(request.user_id)  # Implementasi ini tergantung DB Anda
    if not user_token:
        raise HTTPException(status_code=404, detail="Token tidak ditemukan")

    # Panggil Zapier API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.zapier.com/v2/actions/run",
            json={
                "app": request.app,
                "action": request.action,
                "data": request.data,
            },
            headers={
                "Authorization": f"Bearer {user_token}",
                "Content-Type": "application/json",
            },
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Gagal menjalankan action")

        return response.json()

# Helper function (contoh)
def get_user_token(user_id: str) -> Optional[str]:
    # Implementasi ini tergantung database Anda
    # Misal: query ke PostgreSQL, Redis, dll.
    tokens = {
        "USER_ID_123": "ZAPIER_TOKEN_123",
    }
    return tokens.get(user_id)

# Tambahkan ke FastAPI app
app.include_router(router)
```

---
---
---

## **🔹 5.5 Error Handling (Penanganan Error)**
### **📌 Penjelasan**
**Error Handling** sangat penting untuk **White Label** karena:
- **User tidak tahu bahwa mereka menggunakan Zapier** (jadi error harus ditangani dengan baik).
- **MusGo-OS harus menampilkan error yang user-friendly**.

**Jenis Error yang Mungkin Terjadi:**
| Error | Deskripsi | Solusi |
|-------|-----------|--------|
| **Invalid Token** | Token kadaluarsa/tidak valid | Refresh token atau minta user login ulang |
| **Rate Limit** | Terlalu banyak panggilan API | Implementasi rate limiting di MusGo-OS |
| **App Not Connected** | User belum menghubungkan aplikasi | Arahkan user untuk menghubungkan aplikasi |
| **Permission Denied** | User tidak memiliki izin | Cek scope token |
| **Network Error** | Koneksi gagal | Retry atau tampilkan pesan error |

---
### **🚀 Contoh Implementasi: Error Handling**
#### **1. Error Handling di Frontend (React)**
```tsx
// File: src/components/AutomationError.tsx
import React from "react";

interface AutomationErrorProps {
  error: {
    code: string;
    message: string;
    details?: any;
  };
  onRetry?: () => void;
  onConnectApp?: () => void;
}

const AutomationError: React.FC<AutomationErrorProps> = ({ error, onRetry, onConnectApp }) => {
  // Pesan error yang user-friendly
  const getErrorMessage = () => {
    switch (error.code) {
      case "INVALID_TOKEN":
        return "Sesi Anda telah berakhir. Silakan login ulang.";
      case "RATE_LIMIT":
        return "Terlalu banyak permintaan. Silakan coba lagi nanti.";
      case "APP_NOT_CONNECTED":
        return `Aplikasi ${error.details?.app} belum terhubung.`;
      case "PERMISSION_DENIED":
        return "Anda tidak memiliki izin untuk melakukan tindakan ini.";
      default:
        return error.message || "Terjadi kesalahan. Silakan coba lagi.";
    }
  };

  return (
    <div style={{
      padding: "15px",
      background: "#ffebee",
      border: "1px solid #ffcdd2",
      borderRadius: "5px",
      color: "#c62828",
      margin: "10px 0",
    }}>
      <p style={{ margin: 0 }}>{getErrorMessage()}</p>
      <div style={{ marginTop: "10px", display: "flex", gap: "10px" }}>
        {onRetry && (
          <button
            onClick={onRetry}
            style={{
              padding: "5px 10px",
              background: "#c62828",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            Coba Lagi
          </button>
        )}
        {onConnectApp && error.code === "APP_NOT_CONNECTED" && (
          <button
            onClick={onConnectApp}
            style={{
              padding: "5px 10px",
              background: "#4285F4",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            Hubungkan Aplikasi
          </button>
        )}
      </div>
    </div>
  );
};

export default AutomationError;
```

---
#### **2. Error Handling di Backend (Python FastAPI)**
```python
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx
from typing import Optional

router = APIRouter()

class ZapierError(Exception):
    def __init__(self, code: str, message: str, details: Optional[dict] = None):
        self.code = code
        self.message = message
        self.details = details or {}

@router.post("/api/zapier/run-action")
async def run_zapier_action(request: Request):
    try:
        data = await request.json()
        app = data.get("app")
        action = data.get("action")
        user_id = data.get("user_id")

        # Ambil token user
        token = get_user_token(user_id)
        if not token:
            raise ZapierError("APP_NOT_CONNECTED", "Aplikasi belum terhubung", {"app": app})

        # Panggil Zapier API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.zapier.com/v2/actions/run",
                json={"app": app, "action": action, "data": data.get("data", {})},
                headers={"Authorization": f"Bearer {token}"},
            )

            if response.status_code == 401:
                raise ZapierError("INVALID_TOKEN", "Token tidak valid")
            elif response.status_code == 429:
                raise ZapierError("RATE_LIMIT", "Terlalu banyak permintaan")
            elif response.status_code != 200:
                raise ZapierError("UNKNOWN_ERROR", "Terjadi kesalahan di Zapier")

            return response.json()

    except ZapierError as e:
        return JSONResponse(
            status_code=400,
            content={"error": {"code": e.code, "message": e.message, "details": e.details}}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": {"code": "SERVER_ERROR", "message": str(e)}}
        )

# Tambahkan ke FastAPI app
app.include_router(router)
```

---
---
---

## **🔹 5.6 Use Cases (Contoh Penggunaan)**
### **📌 1. AI Agent Connections and Automations**
**Skenario:**
MusGo-OS ingin **AI Agent-nya** bisa **berinteraksi dengan Zapier** (misal: membuat Zap, menjalankan action) **di bawah merek MusGo-OS**.

**Cara Kerja:**
1. **AI Agent MusGo-OS** meminta **JWT** dari backend.
2. **Backend MusGo-OS** generate **JWT** dengan **White Label**.
3. **AI Agent** menggunakan **JWT** untuk **mengakses Zapier MCP** (tanpa branding Zapier).

**Contoh Arsitektur:**
```
User → MusGo-OS AI Agent → (JWT) → Zapier MCP (White Label) → Aplikasi Eksternal
```

**Contoh Kode (AI Agent - Python):**
```python
import requests

class MusGoAIAgent:
    def __init__(self, user_id: str, backend_url: str = "https://musgo-os.com"):
        self.user_id = user_id
        self.backend_url = backend_url
        self.token = self._get_zapier_token()

    def _get_zapier_token(self) -> str:
        """Ambil token JWT dari backend MusGo-OS"""
        response = requests.post(
            f"{self.backend_url}/api/zapier/token",
            json={"user_id": self.user_id, "scopes": ["read", "write"]}
        )
        if response.status_code != 200:
            raise Exception("Gagal mendapatkan token")
        return response.json()["access_token"]

    def list_apps(self) -> list:
        """Daftar aplikasi yang terintegrasi (via MCP)"""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            "https://api.zapier.com/v2/mcp",
            json={"tool": "zapier_list_apps", "params": {}},
            headers=headers
        )
        return response.json().get("apps", [])

    def create_zap(self, trigger: dict, action: dict) -> dict:
        """Buat Zap baru (via MCP)"""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            "https://api.zapier.com/v2/mcp",
            json={"tool": "zapier_create_zap", "params": {"trigger": trigger, "action": action}},
            headers=headers
        )
        return response.json()

    def run_action(self, app: str, action: str, data: dict) -> dict:
        """Jalankan action (via MCP)"""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            "https://api.zapier.com/v2/mcp",
            json={"tool": "zapier_run_action", "params": {"app": app, "action": action, "data": data}},
            headers=headers
        )
        return response.json()

# Contoh penggunaan
agent = MusGoAIAgent(user_id="USER_ID_123")

# Daftar aplikasi
apps = agent.list_apps()
print("Aplikasi yang tersedia:", apps)

# Buat Zap
zap = agent.create_zap(
    trigger={"app": "google_drive", "event": "New File in Folder", "data": {"folder": "Proyek"}},
    action={"app": "slack", "event": "Send Channel Message", "data": {"channel": "#musgo-updates"}}
)
print("Zap dibuat:", zap)

# Jalankan action
result = agent.run_action("slack", "Send Channel Message", {"channel": "#musgo-updates", "text": "Halo!"})
print("Action berjalan:", result)
```

---
### **📌 2. Embedded Triggers/Actions**
**Skenario:**
MusGo-OS ingin **menampilkan trigger/action Zapier** sebagai **fitur native** (misal: "Pemicu: File Baru di Google Drive").

**Cara Kerja:**
1. **MusGo-OS** menampilkan **daftar trigger/action** (dengan branding MusGo-OS).
2. **User memilih trigger/action** (misal: Google Drive → New File).
3. **MusGo-OS** menggunakan **White Label API** untuk **membuat Zap**.

**Contoh UI (React):**
```tsx
// File: src/components/TriggerActionSelector.tsx
import React, { useState, useEffect } from "react";

interface TriggerAction {
  app: string;
  event: string;
  description: string;
}

const TriggerActionSelector: React.FC<{ onSelect: (trigger: TriggerAction, action: TriggerAction) => void }> = ({ onSelect }) => {
  const [triggers, setTriggers] = useState<TriggerAction[]>([]);
  const [actions, setActions] = useState<TriggerAction[]>([]);
  const [selectedTrigger, setSelectedTrigger] = useState<TriggerAction | null>(null);
  const [selectedAction, setSelectedAction] = useState<TriggerAction | null>(null);

  // Dummy data (ganti dengan API call ke MusGo-OS backend)
  useEffect(() => {
    // Ambil daftar trigger
    fetch("/api/automation/triggers")
      .then((res) => res.json())
      .then((data) => setTriggers(data));

    // Ambil daftar action
    fetch("/api/automation/actions")
      .then((res) => res.json())
      .then((data) => setActions(data));
  }, []);

  const handleSubmit = () => {
    if (selectedTrigger && selectedAction) {
      onSelect(selectedTrigger, selectedAction);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "0 auto" }}>
      <h2>Pilih Pemicu dan Tindakan</h2>

      <div style={{ marginBottom: "20px" }}>
        <h3>Pemicu (Trigger)</h3>
        <select
          value={selectedTrigger?.event || ""}
          onChange={(e) => {
            const trigger = triggers.find((t) => t.event === e.target.value);
            setSelectedTrigger(trigger || null);
          }}
          style={{ width: "100%", padding: "8px", borderRadius: "4px", border: "1px solid #ccc" }}
        >
          <option value="">Pilih Pemicu</option>
          {triggers.map((trigger) => (
            <option key={`${trigger.app}-${trigger.event}`} value={trigger.event}>
              {trigger.app} → {trigger.event}
            </option>
          ))}
        </select>
        {selectedTrigger && (
          <p style={{ marginTop: "5px", color: "#666", fontSize: "14px" }}>
            {selectedTrigger.description}
          </p>
        )}
      </div>

      <div style={{ marginBottom: "20px" }}>
        <h3>Tindakan (Action)</h3>
        <select
          value={selectedAction?.event || ""}
          onChange={(e) => {
            const action = actions.find((a) => a.event === e.target.value);
            setSelectedAction(action || null);
          }}
          style={{ width: "100%", padding: "8px", borderRadius: "4px", border: "1px solid #ccc" }}
        >
          <option value="">Pilih Tindakan</option>
          {actions.map((action) => (
            <option key={`${action.app}-${action.event}`} value={action.event}>
              {action.app} → {action.event}
            </option>
          ))}
        </select>
        {selectedAction && (
          <p style={{ marginTop: "5px", color: "#666", fontSize: "14px" }}>
            {selectedAction.description}
          </p>
        )}
      </div>

      <button
        onClick={handleSubmit}
        disabled={!selectedTrigger || !selectedAction}
        style={{
          padding: "10px 20px",
          background: "#4285F4",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Buat Otomatisasi
      </button>
    </div>
  );
};

export default TriggerActionSelector;
```

---
### **📌 3. Embedded Workflows**
**Skenario:**
MusGo-OS ingin **menampilkan workflow Zapier** (multi-step Zap) **sebagai fitur native**.

**Cara Kerja:**
1. **MusGo-OS** menampilkan **UI workflow** (dengan branding MusGo-OS).
2. **User membuat workflow** (misal: Google Drive → AI Agent → Slack).
3. **MusGo-OS** menggunakan **White Label API** untuk **membuat Zap multi-step**.

**Contoh UI (React):**
```tsx
// File: src/components/WorkflowBuilder.tsx
import React, { useState } from "react";

interface WorkflowStep {
  id: string;
  app: string;
  action: string;
  data: Record<string, any>;
}

const WorkflowBuilder: React.FC = () => {
  const [steps, setSteps] = useState<WorkflowStep[]>([]);
  const [availableApps] = useState<string[]>([
    "Google Drive",
    "Slack",
    "Notion",
    "Trello",
    "MusGo-OS AI Agent",  // Custom app untuk MusGo-OS
  ]);

  const addStep = () => {
    setSteps([
      ...steps,
      {
        id: Date.now().toString(),
        app: "",
        action: "",
        data: {},
      },
    ]);
  };

  const removeStep = (id: string) => {
    setSteps(steps.filter((step) => step.id !== id));
  };

  const updateStep = (id: string, field: keyof WorkflowStep, value: any) => {
    setSteps(
      steps.map((step) =>
        step.id === id ? { ...step, [field]: value } : step
      )
    );
  };

  const saveWorkflow = async () => {
    if (steps.length < 2) {
      alert("Workflow harus memiliki minimal 2 step.");
      return;
    }

    // Kirim ke backend MusGo-OS
    const response = await fetch("/api/automation/workflows", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ steps }),
    });

    if (response.ok) {
      const data = await response.json();
      alert(`✅ Workflow berhasil dibuat! ID: ${data.id}`);
    } else {
      alert("❌ Gagal membuat workflow.");
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
        <h1>🔄 Pembuat Workflow MusGo-OS</h1>
        <button
          onClick={saveWorkflow}
          style={{
            padding: "10px 20px",
            background: "#4285F4",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Simpan Workflow
        </button>
      </div>

      <div style={{ marginBottom: "20px" }}>
        <p>Buat workflow multi-step untuk otomatisasi yang lebih powerful.</p>
        <button
          onClick={addStep}
          style={{
            padding: "8px 16px",
            background: "#f0f0f0",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          + Tambah Step
        </button>
      </div>

      {steps.length === 0 ? (
        <p style={{ textAlign: "center", color: "#999" }}>
          Belum ada step. Klik "Tambah Step" untuk memulai.
        </p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
          {steps.map((step, index) => (
            <div
              key={step.id}
              style={{
                border: "1px solid #e0e0e0",
                padding: "15px",
                borderRadius: "8px",
                position: "relative",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "10px" }}>
                <h3 style={{ margin: 0 }}>Step {index + 1}</h3>
                <button
                  onClick={() => removeStep(step.id)}
                  style={{
                    background: "none",
                    border: "none",
                    color: "#ff4444",
                    cursor: "pointer",
                  }}
                >
                  ✕
                </button>
              </div>

              <div style={{ marginBottom: "10px" }}>
                <label style={{ display: "block", marginBottom: "5px" }}>Aplikasi:</label>
                <select
                  value={step.app}
                  onChange={(e) => updateStep(step.id, "app", e.target.value)}
                  style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                >
                  <option value="">Pilih Aplikasi</option>
                  {availableApps.map((app) => (
                    <option key={app} value={app}>
                      {app}
                    </option>
                  ))}
                </select>
              </div>

              {step.app === "Google Drive" && (
                <div style={{ marginBottom: "10px" }}>
                  <label style={{ display: "block", marginBottom: "5px" }}>Trigger/Action:</label>
                  <select
                    value={step.action}
                    onChange={(e) => updateStep(step.id, "action", e.target.value)}
                    style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                  >
                    <option value="">Pilih Trigger/Action</option>
                    <option value="New File in Folder">File Baru di Folder</option>
                    <option value="New File">File Baru</option>
                  </select>
                </div>
              )}

              {step.app === "Slack" && (
                <div style={{ marginBottom: "10px" }}>
                  <label style={{ display: "block", marginBottom: "5px" }}>Action:</label>
                  <select
                    value={step.action}
                    onChange={(e) => updateStep(step.id, "action", e.target.value)}
                    style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                  >
                    <option value="">Pilih Action</option>
                    <option value="Send Channel Message">Kirim Pesan ke Channel</option>
                    <option value="Send Direct Message">Kirim Pesan Langsung</option>
                  </select>
                </div>
              )}

              {step.app === "MusGo-OS AI Agent" && (
                <div style={{ marginBottom: "10px" }}>
                  <label style={{ display: "block", marginBottom: "5px" }}>Action:</label>
                  <select
                    value={step.action}
                    onChange={(e) => updateStep(step.id, "action", e.target.value)}
                    style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                  >
                    <option value="">Pilih Action</option>
                    <option value="Run Agent">Jalankan AI Agent</option>
                    <option value="Ask Agent">Tanyakan ke AI Agent</option>
                  </select>
                </div>
              )}

              {step.app && step.action && (
                <div>
                  <label style={{ display: "block", marginBottom: "5px" }}>Data:</label>
                  {step.action === "Send Channel Message" && (
                    <>
                      <div style={{ marginBottom: "10px" }}>
                        <label style={{ display: "block", marginBottom: "5px" }}>Channel:</label>
                        <input
                          type="text"
                          value={step.data.channel || ""}
                          onChange={(e) => updateStep(step.id, "data", { ...step.data, channel: e.target.value })}
                          style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                          placeholder="#musgo-updates"
                        />
                      </div>
                      <div style={{ marginBottom: "10px" }}>
                        <label style={{ display: "block", marginBottom: "5px" }}>Pesan:</label>
                        <textarea
                          value={step.data.text || ""}
                          onChange={(e) => updateStep(step.id, "data", { ...step.data, text: e.target.value })}
                          style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px", minHeight: "100px" }}
                          placeholder="Masukkan pesan..."
                        />
                      </div>
                    </>
                  )}
                  {step.action === "New File in Folder" && (
                    <div style={{ marginBottom: "10px" }}>
                      <label style={{ display: "block", marginBottom: "5px" }}>Folder:</label>
                      <input
                        type="text"
                        value={step.data.folder || ""}
                        onChange={(e) => updateStep(step.id, "data", { ...step.data, folder: e.target.value })}
                        style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                        placeholder="Proyek MusGo-OS"
                      />
                    </div>
                  )}
                  {step.action === "Run Agent" && (
                    <>
                      <div style={{ marginBottom: "10px" }}>
                        <label style={{ display: "block", marginBottom: "5px" }}>Agent ID:</label>
                        <select
                          value={step.data.agentId || ""}
                          onChange={(e) => updateStep(step.id, "data", { ...step.data, agentId: e.target.value })}
                          style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px" }}
                        >
                          <option value="">Pilih AI Agent</option>
                          <option value="planner">Planner</option>
                          <option value="executor">Executor</option>
                          <option value="analyst">Analyst</option>
                        </select>
                      </div>
                      <div style={{ marginBottom: "10px" }}>
                        <label style={{ display: "block", marginBottom: "5px" }}>Prompt:</label>
                        <textarea
                          value={step.data.prompt || ""}
                          onChange={(e) => updateStep(step.id, "data", { ...step.data, prompt: e.target.value })}
                          style={{ width: "100%", padding: "8px", border: "1px solid #ccc", borderRadius: "4px", minHeight: "100px" }}
                          placeholder="Masukkan prompt untuk AI Agent..."
                        />
                      </div>
                    </>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default WorkflowBuilder;
```

---
---
---
# **📌 PART 5: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 5 (White Label)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Branding MusGo-OS** | User merasa menggunakan fitur native MusGo-OS | ✅ **Contoh UI tersedia** |
| **Connection Flow** | User bisa menghubungkan aplikasi tanpa tahu Zapier | ✅ **Contoh kode tersedia** |
| **Token Exchange** | Autentikasi aman dengan JWT | ✅ **Contoh kode tersedia** |
| **Error Handling** | Penanganan error yang user-friendly | ✅ **Contoh kode tersedia** |
| **AI Agent Integration** | AI Agent bisa menggunakan Zapier di bawah merek MusGo-OS | ✅ **Contoh kode tersedia** |
| **Embedded Triggers/Actions** | Tampilkan trigger/action sebagai fitur native | ✅ **Contoh UI tersedia** |
| **Embedded Workflows** | Tampilkan workflow multi-step sebagai fitur native | ✅ **Contoh UI tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Daftar sebagai Partner Zapier** → [Zapier Partner Program](https://zapier.com/partner).
- [ ] **Generate JWKS** untuk token validation.
- [ ] **Setup OAuth 2.0** (untuk connection flow).
- [ ] **Implementasikan Token Exchange** (JWT untuk MCP).
- [ ] **Test Connection Flow** (popup/redirect).

### **2. Mid-Term (1 Bulan)**
- [ ] **Integrasikan White Label ke UI MusGo-OS** (gunakan contoh UI di atas).
- [ ] **Implementasikan Error Handling** (user-friendly).
- [ ] **Setup Embedded Triggers/Actions** (untuk workflow builder).
- [ ] **Test AI Agent + White Label** (pastikan AI Agent bisa menggunakan Zapier).

### **3. Long-Term (3+ Bulan)**
- [ ] **Luncurkan fitur otomatisasi** ke user MusGo-OS.
- [ ] **Dokumentasikan integrasi White Label** untuk developer.
- [ ] **Monitor penggunaan** (rate limiting, error tracking).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 6: Workflow API Reference** (Untuk referensi lengkap REST API)
   - [ ] **Part 7: Advanced Use Cases** (Misal: Multi-step Zaps, Error Handling, dll.)
   - [ ] **Part 8: Security & Compliance** (Untuk keamanan White Label)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + Notion + Slack)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi API untuk MusGo-OS + Zapier White Label**?
   - [ ] **Contoh deployment (Docker, Kubernetes)**?

3. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **MusGo-OS → Slack → Google Sheets**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 6: Workflow API Reference** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi** untuk **MusGo-OS 2in1** dari dokumentasi **Zapier Workflow API Reference**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN WORKFLOW API REFERENCE (PART 6)**
*Terjemahan + Implementasi untuk Mengelola Zap secara Programatik*

---

---

## **🔹 6.1 Overview Workflow API**
### **📌 Penjelasan (Bahasa Indonesia)**
**Workflow API** adalah **REST API** dari Zapier yang memungkinkan **MusGo-OS** untuk **mengelola Zap (otomatisasi) secara programatik**. Dengan Workflow API, Anda bisa:
✅ **Membuat, membaca, mengupdate, dan menghapus Zap** (CRUD).
✅ **Menjalankan Zap dengan data dinamis**.
✅ **Mendaftar dan mengelola Zap user**.
✅ **Mengelola autentikasi dan koneksi aplikasi**.

**Manfaat untuk MusGo-OS:**
- **Backend MusGo-OS bisa membuat Zap otomatis** untuk user.
- **AI Agent MusGo-OS bisa menjalankan Zap** berdasarkan perintah user.
- **MusGo-OS bisa menawarkan fitur otomatisasi** tanpa user perlu buka Zapier.

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: AI Agent Membuat Zap Otomatis**
**Skenario:**
User MusGo-OS berkata:
> *"MusGo, buatkan Zap yang mengirim notifikasi ke Slack setiap kali ada file baru di Google Drive folder 'Proyek'."*

**Cara Kerja:**
1. **AI Agent MusGo-OS** menerima perintah.
2. **AI Agent menggunakan Workflow API** untuk **membuat Zap** dengan:
   - **Trigger**: Google Drive → New File in Folder (folder: Proyek).
   - **Action**: Slack → Send Channel Message (channel: #musgo-updates).

**Arsitektur:**
```
User → MusGo-OS AI Agent → Workflow API → Zapier → Google Drive (Trigger) + Slack (Action)
```

**Contoh Kode (Python - FastAPI + Requests):**
```python
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model untuk request
class CreateZapRequest(BaseModel):
    name: str
    trigger: dict
    action: dict
    user_id: str  # ID user MusGo-OS

# Model untuk response
class ZapResponse(BaseModel):
    id: str
    name: str
    status: str
    created_at: str

# Dummy database untuk token user
user_tokens = {
    "USER_ID_123": "ZAPIER_API_KEY_123",
}

@app.post("/api/automation/zaps", response_model=ZapResponse)
async def create_zap(request: CreateZapRequest):
    """Buat Zap baru via Workflow API"""
    # Ambil token user
    api_key = user_tokens.get(request.user_id)
    if not api_key:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    # Panggil Workflow API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Data untuk Zap
    zap_data = {
        "name": request.name,
        "steps": [
            {
                "app": request.trigger["app"],
                "action": request.trigger["event"],
                "data": request.trigger.get("data", {}),
            },
            {
                "app": request.action["app"],
                "action": request.action["event"],
                "data": request.action.get("data", {}),
            },
        ],
    }

    response = requests.post(
        "https://api.zapier.com/v2/zaps",
        json=zap_data,
        headers=headers
    )

    if response.status_code != 201:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Gagal membuat Zap: {response.text}"
        )

    return response.json()

# Contoh penggunaan
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Contoh Request (AI Agent):**
```python
import requests

# Request ke MusGo-OS backend
response = requests.post(
    "http://localhost:8000/api/automation/zaps",
    json={
        "name": "Google Drive → Slack (Proyek)",
        "trigger": {
            "app": "google_drive",
            "event": "New File in Folder",
            "data": {"folder": "Proyek"},
        },
        "action": {
            "app": "slack",
            "event": "Send Channel Message",
            "data": {"channel": "#musgo-updates", "text": "File baru terdeteksi: {file_name}"},
        },
        "user_id": "USER_ID_123",
    }
)

print("Zap dibuat:", response.json())
```

**Output:**
```json
{
  "id": "ZAP_ID_456",
  "name": "Google Drive → Slack (Proyek)",
  "status": "on",
  "created_at": "2026-05-19T10:00:00Z"
}
```

---
#### **Use-Case 2: Menjalankan Zap dengan Data Dinamis**
**Skenario:**
Backend MusGo-OS ingin **menjalankan Zap** (otomatisasi) **setiap kali user menyimpan file di Google Drive**.

**Cara Kerja:**
1. **Backend MusGo-OS** mendeteksi **file baru** di Google Drive (via webhook).
2. **Backend menggunakan Workflow API** untuk **menjalankan Zap** dengan data file.

**Arsitektur:**
```
Google Drive (Webhook) → MusGo-OS Backend → Workflow API → Zapier → Slack (Action)
```

**Contoh Kode (Python - FastAPI):**
```python
from fastapi import FastAPI, Request, HTTPException
import requests

app = FastAPI()

# Dummy database untuk Zap user
user_zaps = {
    "USER_ID_123": [
        {"id": "ZAP_ID_456", "name": "Google Drive → Slack (Proyek)"},
    ],
}

@app.post("/api/webhooks/google-drive")
async def google_drive_webhook(request: Request):
    """Terima webhook dari Google Drive"""
    data = await request.json()
    file_name = data.get("name")
    file_url = data.get("url")
    user_id = data.get("user_id")  # Asumsikan user_id dikirim di payload

    # Ambil Zap user
    zaps = user_zaps.get(user_id, [])
    if not zaps:
        raise HTTPException(status_code=404, detail="User tidak memiliki Zap")

    # Jalankan semua Zap user
    for zap in zaps:
        try:
            # Ambil token user
            api_key = user_tokens.get(user_id)
            if not api_key:
                continue

            # Panggil Workflow API untuk menjalankan Zap
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }

            response = requests.post(
                f"https://api.zapier.com/v2/zaps/{zap['id']}/run",
                json={"data": {"file_name": file_name, "file_url": file_url}},
                headers=headers
            )

            if response.status_code == 200:
                print(f"✅ Zap {zap['id']} berjalan untuk file: {file_name}")
            else:
                print(f"❌ Gagal menjalankan Zap {zap['id']}: {response.text}")

        except Exception as e:
            print(f"❌ Error menjalankan Zap {zap['id']}: {str(e)}")

    return {"status": "success"}

# Tambahkan ke FastAPI app
app.include_router(app)
```

**Contoh Request (Webhook dari Google Drive):**
```json
{
  "name": "laporan_proyek.pdf",
  "url": "https://drive.google.com/file/d/12345",
  "user_id": "USER_ID_123"
}
```

**Output:**
```
✅ Zap ZAP_ID_456 berjalan untuk file: laporan_proyek.pdf
```

---
---
---

## **🔹 6.2 API Reference (Dokumentasi Lengkap)**
Berikut adalah **daftar endpoint Workflow API** yang relevan untuk **MusGo-OS**, beserta **contoh penggunaan** untuk setiap endpoint.

---

### **📌 1. Accounts (Akun)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/accounts` | `POST` | Buat akun user baru | `requests.post("https://api.zapier.com/v2/accounts", json={...}, headers={...})` |
| `/accounts/{account_id}` | `GET` | Dapatkan detail akun | `requests.get(f"https://api.zapier.com/v2/accounts/{account_id}", headers={...})` |

**Contoh: Buat Akun User Baru**
```python
import requests

def create_zapier_account(email: str, password: str, api_key: str):
    """Buat akun Zapier baru untuk user MusGo-OS"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "email": email,
        "password": password,
    }

    response = requests.post(
        "https://api.zapier.com/v2/accounts",
        json=data,
        headers=headers
    )

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Gagal membuat akun: {response.text}")

# Contoh penggunaan
account = create_zapier_account(
    email="dhani@musgo-os.com",
    password="secure_password_123",
    api_key="YOUR_ZAPIER_API_KEY"
)
print("Akun dibuat:", account)
```

---
### **📌 2. Apps (Aplikasi)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/apps` | `GET` | Daftar semua aplikasi | `requests.get("https://api.zapier.com/v2/apps", headers={...})` |
| `/apps/{app_key}` | `GET` | Dapatkan detail aplikasi | `requests.get(f"https://api.zapier.com/v2/apps/{app_key}", headers={...})` |
| `/apps/{app_key}/actions` | `GET` | Daftar action untuk aplikasi | `requests.get(f"https://api.zapier.com/v2/apps/{app_key}/actions", headers={...})` |
| `/apps/{app_key}/triggers` | `GET` | Daftar trigger untuk aplikasi | `requests.get(f"https://api.zapier.com/v2/apps/{app_key}/triggers", headers={...})` |

**Contoh: Daftar Aplikasi yang Terintegrasi**
```python
import requests

def list_integrated_apps(api_key: str):
    """Daftar aplikasi yang terintegrasi dengan Zapier"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(
        "https://api.zapier.com/v2/apps",
        headers=headers
    )

    if response.status_code == 200:
        return response.json().get("apps", [])
    else:
        raise Exception(f"Gagal mendaftar aplikasi: {response.text}")

# Contoh penggunaan
apps = list_integrated_apps("YOUR_ZAPIER_API_KEY")
print("Aplikasi yang tersedia:", [app["name"] for app in apps])
```

**Output:**
```python
Aplikasi yang tersedia: ['Slack', 'Google Drive', 'Notion', 'Trello', 'Gmail', ...]
```

---
### **📌 3. Authentications (Autentikasi)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/authentications` | `GET` | Daftar koneksi autentikasi user | `requests.get("https://api.zapier.com/v2/authentications", headers={...})` |
| `/authentications` | `POST` | Buat koneksi autentikasi baru | `requests.post("https://api.zapier.com/v2/authentications", json={...}, headers={...})` |
| `/authentications/{auth_id}` | `GET` | Dapatkan detail koneksi | `requests.get(f"https://api.zapier.com/v2/authentications/{auth_id}", headers={...})` |
| `/authentications/{auth_id}` | `DELETE` | Hapus koneksi | `requests.delete(f"https://api.zapier.com/v2/authentications/{auth_id}", headers={...})` |

**Contoh: Daftar Koneksi Autentikasi User**
```python
import requests

def list_user_connections(api_key: str, user_id: str):
    """Daftar koneksi autentikasi user"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(
        "https://api.zapier.com/v2/authentications",
        headers=headers
    )

    if response.status_code == 200:
        return response.json().get("authentications", [])
    else:
        raise Exception(f"Gagal mendaftar koneksi: {response.text}")

# Contoh penggunaan
connections = list_user_connections("YOUR_ZAPIER_API_KEY", "USER_ID_123")
print("Koneksi user:", [conn["app"] for conn in connections])
```

**Output:**
```python
Koneksi user: ['slack', 'google_drive']
```

---
### **📌 4. Actions (Tindakan)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/actions` | `GET` | Daftar semua action | `requests.get("https://api.zapier.com/v2/actions", headers={...})` |
| `/actions/{action_id}` | `GET` | Dapatkan detail action | `requests.get(f"https://api.zapier.com/v2/actions/{action_id}", headers={...})` |
| `/actions/run` | `POST` | Jalankan action | `requests.post("https://api.zapier.com/v2/actions/run", json={...}, headers={...})` |
| `/actions/{action_id}/input_fields` | `GET` | Daftar input fields untuk action | `requests.get(f"https://api.zapier.com/v2/actions/{action_id}/input_fields", headers={...})` |
| `/actions/{action_id}/output_fields` | `GET` | Daftar output fields untuk action | `requests.get(f"https://api.zapier.com/v2/actions/{action_id}/output_fields", headers={...})` |

**Contoh: Jalankan Action Slack**
```python
import requests

def run_slack_action(api_key: str, channel: str, text: str):
    """Jalankan action Slack: Send Channel Message"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "app": "slack",
        "action": "Send Channel Message",
        "data": {
            "channel": channel,
            "text": text,
        },
    }

    response = requests.post(
        "https://api.zapier.com/v2/actions/run",
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Gagal menjalankan action: {response.text}")

# Contoh penggunaan
result = run_slack_action(
    api_key="YOUR_ZAPIER_API_KEY",
    channel="#musgo-updates",
    text="Halo dari MusGo-OS!"
)
print("Action berjalan:", result)
```

**Output:**
```json
{
  "id": "ACTION_RUN_ID_789",
  "status": "success",
  "data": {
    "channel": "#musgo-updates",
    "text": "Halo dari MusGo-OS!",
    "timestamp": "2026-05-19T10:00:00Z"
  }
}
```

---
### **📌 5. Zaps (Otomatisasi)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/zaps` | `GET` | Daftar semua Zap user | `requests.get("https://api.zapier.com/v2/zaps", headers={...})` |
| `/zaps` | `POST` | Buat Zap baru | `requests.post("https://api.zapier.com/v2/zaps", json={...}, headers={...})` |
| `/zaps/{zap_id}` | `GET` | Dapatkan detail Zap | `requests.get(f"https://api.zapier.com/v2/zaps/{zap_id}", headers={...})` |
| `/zaps/{zap_id}` | `PUT` | Update Zap | `requests.put(f"https://api.zapier.com/v2/zaps/{zap_id}", json={...}, headers={...})` |
| `/zaps/{zap_id}` | `DELETE` | Hapus Zap | `requests.delete(f"https://api.zapier.com/v2/zaps/{zap_id}", headers={...})` |
| `/zaps/{zap_id}/run` | `POST` | Jalankan Zap | `requests.post(f"https://api.zapier.com/v2/zaps/{zap_id}/run", json={...}, headers={...})` |
| `/zaps/{zap_id}/enable` | `POST` | Aktifkan Zap | `requests.post(f"https://api.zapier.com/v2/zaps/{zap_id}/enable", headers={...})` |
| `/zaps/{zap_id}/disable` | `POST` | Nonaktifkan Zap | `requests.post(f"https://api.zapier.com/v2/zaps/{zap_id}/disable", headers={...})` |

**Contoh: Daftar Zap User**
```python
import requests

def list_user_zaps(api_key: str):
    """Daftar semua Zap user"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(
        "https://api.zapier.com/v2/zaps",
        headers=headers
    )

    if response.status_code == 200:
        return response.json().get("zaps", [])
    else:
        raise Exception(f"Gagal mendaftar Zap: {response.text}")

# Contoh penggunaan
zaps = list_user_zaps("YOUR_ZAPIER_API_KEY")
print("Daftar Zap user:", [zap["name"] for zap in zaps])
```

**Output:**
```python
Daftar Zap user: ['Google Drive → Slack', 'Trello → Notion']
```

---
**Contoh: Jalankan Zap**
```python
import requests

def run_zap(api_key: str, zap_id: str, data: dict = None):
    """Jalankan Zap dengan data dinamis"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        f"https://api.zapier.com/v2/zaps/{zap_id}/run",
        json={"data": data or {}},
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Gagal menjalankan Zap: {response.text}")

# Contoh penggunaan
result = run_zap(
    api_key="YOUR_ZAPIER_API_KEY",
    zap_id="ZAP_ID_456",
    data={"file_name": "laporan.pdf", "file_url": "https://drive.google.com/file/d/12345"}
)
print("Zap berjalan:", result)
```

**Output:**
```json
{
  "id": "ZAP_RUN_ID_101",
  "status": "success",
  "data": {
    "file_name": "laporan.pdf",
    "file_url": "https://drive.google.com/file/d/12345"
  }
}
```

---
### **📌 6. Zap Templates (Template Zap)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/zap-templates` | `GET` | Daftar template Zap | `requests.get("https://api.zapier.com/v2/zap-templates", headers={...})` |
| `/zap-templates/{template_id}` | `GET` | Dapatkan detail template | `requests.get(f"https://api.zapier.com/v2/zap-templates/{template_id}", headers={...})` |
| `/zap-templates/{template_id}/create` | `POST` | Buat Zap dari template | `requests.post(f"https://api.zapier.com/v2/zap-templates/{template_id}/create", json={...}, headers={...})` |

**Contoh: Buat Zap dari Template**
```python
import requests

def create_zap_from_template(api_key: str, template_id: str, data: dict = None):
    """Buat Zap dari template"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        f"https://api.zapier.com/v2/zap-templates/{template_id}/create",
        json={"data": data or {}},
        headers=headers
    )

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Gagal membuat Zap dari template: {response.text}")

# Contoh penggunaan
zap = create_zap_from_template(
    api_key="YOUR_ZAPIER_API_KEY",
    template_id="TEMPLATE_ID_789",
    data={"channel": "#musgo-updates"}  # Override data template
)
print("Zap dibuat dari template:", zap)
```

**Output:**
```json
{
  "id": "ZAP_ID_102",
  "name": "Google Drive → Slack (Template)",
  "status": "on"
}
```

---
### **📌 7. Categories (Kategori)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/categories` | `GET` | Daftar kategori Zap | `requests.get("https://api.zapier.com/v2/categories", headers={...})` |

**Contoh: Daftar Kategori Zap**
```python
import requests

def list_zap_categories(api_key: str):
    """Daftar kategori Zap"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.get(
        "https://api.zapier.com/v2/categories",
        headers=headers
    )

    if response.status_code == 200:
        return response.json().get("categories", [])
    else:
        raise Exception(f"Gagal mendaftar kategori: {response.text}")

# Contoh penggunaan
categories = list_zap_categories("YOUR_ZAPIER_API_KEY")
print("Kategori Zap:", [category["name"] for category in categories])
```

**Output:**
```python
Kategori Zap: ['Productivity', 'Marketing', 'Sales', 'Support', ...]
```

---
### **📌 8. Promotions (Promosi)**
| Endpoint | Method | Deskripsi | Contoh Penggunaan (Python) |
|----------|--------|-----------|----------------------------|
| `/promotions/{promotion_id}/enrollments` | `POST` | Daftarkan user ke promosi | `requests.post(f"https://api.zapier.com/v2/promotions/{promotion_id}/enrollments", json={...}, headers={...})` |
| `/promotions/{promotion_id}/enrollments/{enrollment_id}` | `GET` | Dapatkan detail enrollment | `requests.get(f"https://api.zapier.com/v2/promotions/{promotion_id}/enrollments/{enrollment_id}", headers={...})` |
| `/promotions/{promotion_id}/enrollments/{enrollment_id}` | `DELETE` | Hapus enrollment | `requests.delete(f"https://api.zapier.com/v2/promotions/{promotion_id}/enrollments/{enrollment_id}", headers={...})` |

**Contoh: Daftarkan User ke Program Sponsor**
```python
import requests

def enroll_user_in_promotion(api_key: str, promotion_id: str, user_id: str):
    """Daftarkan user ke program sponsor"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "userId": user_id,
    }

    response = requests.post(
        f"https://api.zapier.com/v2/promotions/{promotion_id}/enrollments",
        json=data,
        headers=headers
    )

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Gagal mendaftarkan user: {response.text}")

# Contoh penggunaan
enrollment = enroll_user_in_promotion(
    api_key="YOUR_ZAPIER_API_KEY",
    promotion_id="PROMOTION_ID_123",
    user_id="USER_ID_456"
)
print("User didaftarkan ke promosi:", enrollment)
```

**Output:**
```json
{
  "id": "ENROLLMENT_ID_789",
  "userId": "USER_ID_456",
  "status": "active",
  "createdAt": "2026-05-19T10:00:00Z"
}
```

---
---
---

## **🔹 6.3 Contoh Implementasi Lengkap untuk MusGo-OS**
### **📌 1. Class ZapierWorkflowAPI (Python)**
**Kelas ini menyediakan semua method Workflow API yang dibutuhkan MusGo-OS.**

```python
import requests
from typing import Optional, Dict, List, Any

class ZapierWorkflowAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.zapier.com/v2"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    # ========== ACCOUNTS ==========
    def create_account(self, email: str, password: str) -> Dict[str, Any]:
        """Buat akun Zapier baru"""
        data = {"email": email, "password": password}
        response = requests.post(
            f"{self.base_url}/accounts",
            json=data,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def get_account(self, account_id: str) -> Dict[str, Any]:
        """Dapatkan detail akun"""
        response = requests.get(
            f"{self.base_url}/accounts/{account_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    # ========== APPS ==========
    def list_apps(self) -> List[Dict[str, Any]]:
        """Daftar semua aplikasi"""
        response = requests.get(
            f"{self.base_url}/apps",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("apps", [])

    def get_app(self, app_key: str) -> Dict[str, Any]:
        """Dapatkan detail aplikasi"""
        response = requests.get(
            f"{self.base_url}/apps/{app_key}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def list_app_actions(self, app_key: str) -> List[Dict[str, Any]]:
        """Daftar action untuk aplikasi"""
        response = requests.get(
            f"{self.base_url}/apps/{app_key}/actions",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("actions", [])

    def list_app_triggers(self, app_key: str) -> List[Dict[str, Any]]:
        """Daftar trigger untuk aplikasi"""
        response = requests.get(
            f"{self.base_url}/apps/{app_key}/triggers",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("triggers", [])

    # ========== AUTHENTICATIONS ==========
    def list_authentications(self) -> List[Dict[str, Any]]:
        """Daftar koneksi autentikasi"""
        response = requests.get(
            f"{self.base_url}/authentications",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("authentications", [])

    def create_authentication(self, app: str, credentials: Dict[str, Any]) -> Dict[str, Any]:
        """Buat koneksi autentikasi baru"""
        data = {"app": app, "credentials": credentials}
        response = requests.post(
            f"{self.base_url}/authentications",
            json=data,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def get_authentication(self, auth_id: str) -> Dict[str, Any]:
        """Dapatkan detail koneksi"""
        response = requests.get(
            f"{self.base_url}/authentications/{auth_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def delete_authentication(self, auth_id: str) -> None:
        """Hapus koneksi"""
        response = requests.delete(
            f"{self.base_url}/authentications/{auth_id}",
            headers=self.headers
        )
        self._raise_for_status(response)

    # ========== ACTIONS ==========
    def list_actions(self) -> List[Dict[str, Any]]:
        """Daftar semua action"""
        response = requests.get(
            f"{self.base_url}/actions",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("actions", [])

    def get_action(self, action_id: str) -> Dict[str, Any]:
        """Dapatkan detail action"""
        response = requests.get(
            f"{self.base_url}/actions/{action_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action"""
        payload = {"app": app, "action": action, "data": data}
        response = requests.post(
            f"{self.base_url}/actions/run",
            json=payload,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def get_action_input_fields(self, action_id: str) -> List[Dict[str, Any]]:
        """Daftar input fields untuk action"""
        response = requests.get(
            f"{self.base_url}/actions/{action_id}/input_fields",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("input_fields", [])

    def get_action_output_fields(self, action_id: str) -> List[Dict[str, Any]]:
        """Daftar output fields untuk action"""
        response = requests.get(
            f"{self.base_url}/actions/{action_id}/output_fields",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("output_fields", [])

    # ========== ZAPS ==========
    def list_zaps(self) -> List[Dict[str, Any]]:
        """Daftar semua Zap"""
        response = requests.get(
            f"{self.base_url}/zaps",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("zaps", [])

    def create_zap(self, name: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Buat Zap baru"""
        data = {"name": name, "steps": steps}
        response = requests.post(
            f"{self.base_url}/zaps",
            json=data,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def get_zap(self, zap_id: str) -> Dict[str, Any]:
        """Dapatkan detail Zap"""
        response = requests.get(
            f"{self.base_url}/zaps/{zap_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def update_zap(self, zap_id: str, name: Optional[str] = None, steps: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """Update Zap"""
        data = {}
        if name:
            data["name"] = name
        if steps:
            data["steps"] = steps

        response = requests.put(
            f"{self.base_url}/zaps/{zap_id}",
            json=data,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def delete_zap(self, zap_id: str) -> None:
        """Hapus Zap"""
        response = requests.delete(
            f"{self.base_url}/zaps/{zap_id}",
            headers=self.headers
        )
        self._raise_for_status(response)

    def run_zap(self, zap_id: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Jalankan Zap"""
        payload = {"data": data or {}}
        response = requests.post(
            f"{self.base_url}/zaps/{zap_id}/run",
            json=payload,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def enable_zap(self, zap_id: str) -> Dict[str, Any]:
        """Aktifkan Zap"""
        response = requests.post(
            f"{self.base_url}/zaps/{zap_id}/enable",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def disable_zap(self, zap_id: str) -> Dict[str, Any]:
        """Nonaktifkan Zap"""
        response = requests.post(
            f"{self.base_url}/zaps/{zap_id}/disable",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    # ========== ZAP TEMPLATES ==========
    def list_zap_templates(self) -> List[Dict[str, Any]]:
        """Daftar template Zap"""
        response = requests.get(
            f"{self.base_url}/zap-templates",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("templates", [])

    def get_zap_template(self, template_id: str) -> Dict[str, Any]:
        """Dapatkan detail template"""
        response = requests.get(
            f"{self.base_url}/zap-templates/{template_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def create_zap_from_template(self, template_id: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Buat Zap dari template"""
        payload = {"data": data or {}}
        response = requests.post(
            f"{self.base_url}/zap-templates/{template_id}/create",
            json=payload,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    # ========== CATEGORIES ==========
    def list_categories(self) -> List[Dict[str, Any]]:
        """Daftar kategori Zap"""
        response = requests.get(
            f"{self.base_url}/categories",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json().get("categories", [])

    # ========== PROMOTIONS ==========
    def enroll_user_in_promotion(self, promotion_id: str, user_id: str) -> Dict[str, Any]:
        """Daftarkan user ke promosi"""
        data = {"userId": user_id}
        response = requests.post(
            f"{self.base_url}/promotions/{promotion_id}/enrollments",
            json=data,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def get_enrollment(self, promotion_id: str, enrollment_id: str) -> Dict[str, Any]:
        """Dapatkan detail enrollment"""
        response = requests.get(
            f"{self.base_url}/promotions/{promotion_id}/enrollments/{enrollment_id}",
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()

    def delete_enrollment(self, promotion_id: str, enrollment_id: str) -> None:
        """Hapus enrollment"""
        response = requests.delete(
            f"{self.base_url}/promotions/{promotion_id}/enrollments/{enrollment_id}",
            headers=self.headers
        )
        self._raise_for_status(response)

    # ========== HELPER METHODS ==========
    def _raise_for_status(self, response: requests.Response) -> None:
        """Helper untuk raise exception jika status code != 200"""
        if 400 <= response.status_code < 600:
            raise Exception(f"Zapier API Error ({response.status_code}): {response.text}")
```

---
### **📌 2. Contoh Penggunaan Class ZapierWorkflowAPI**
```python
# Inisialisasi
api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# 1. Daftar aplikasi
apps = api.list_apps()
print("Aplikasi yang tersedia:", [app["name"] for app in apps])

# 2. Daftar action untuk Slack
slack_actions = api.list_app_actions("slack")
print("Action Slack:", [action["name"] for action in slack_actions])

# 3. Jalankan action Slack
result = api.run_action(
    app="slack",
    action="Send Channel Message",
    data={"channel": "#musgo-updates", "text": "Halo dari MusGo-OS!"}
)
print("Action berjalan:", result)

# 4. Buat Zap baru
zap = api.create_zap(
    name="Google Drive → Slack (MusGo-OS)",
    steps=[
        {
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {"folder": "Proyek MusGo-OS"},
        },
        {
            "app": "slack",
            "action": "Send Channel Message",
            "data": {"channel": "#musgo-updates", "text": "File baru terdeteksi: {file_name}"},
        },
    ]
)
print("Zap dibuat:", zap)

# 5. Jalankan Zap
run_result = api.run_zap(
    zap_id=zap["id"],
    data={"file_name": "laporan.pdf", "file_url": "https://drive.google.com/file/d/12345"}
)
print("Zap berjalan:", run_result)

# 6. Daftar Zap user
zaps = api.list_zaps()
print("Daftar Zap:", [zap["name"] for zap in zaps])

# 7. Hapus Zap
api.delete_zap(zap_id=zap["id"])
print("Zap dihapus")

# 8. Daftar template Zap
templates = api.list_zap_templates()
print("Template Zap:", [template["name"] for template in templates])

# 9. Buat Zap dari template
template_zap = api.create_zap_from_template(
    template_id=templates[0]["id"],
    data={"channel": "#musgo-updates"}
)
print("Zap dari template:", template_zap)
```

---
---
---

## **🔹 6.4 Best Practices untuk MusGo-OS**
### **📌 1. Error Handling & Retry**
**Masalah:** Workflow API bisa **gagal** (misal: rate limit, token invalid, dll.).
**Solusi:** Gunakan **retry mechanism** dengan **exponential backoff**.

**Contoh Kode (Python):**
```python
import time
import requests
from functools import wraps

def retry(max_retries: int = 3, backoff_factor: float = 1.0):
    """Decorator untuk retry dengan exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        wait_time = backoff_factor * (2 ** attempt)
                        time.sleep(wait_time)
            raise last_exception
        return wrapper
    return decorator

# Contoh penggunaan
class ZapierWorkflowAPI:
    @retry(max_retries=3, backoff_factor=1.0)
    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action dengan retry"""
        payload = {"app": app, "action": action, "data": data}
        response = requests.post(
            f"{self.base_url}/actions/run",
            json=payload,
            headers=self.headers
        )
        self._raise_for_status(response)
        return response.json()
```

---
### **📌 2. Rate Limiting**
**Masalah:** Zapier memiliki **rate limit** (misal: 60 panggilan/menit untuk akun gratis).
**Solusi:** Gunakan **queue** (antrian) untuk **membatasi panggilan**.

**Contoh Kode (Python + PQueue):**
```python
from pqueue import PQueue
import time

class RateLimitedZapierAPI:
    def __init__(self, api_key: str, max_requests_per_minute: int = 60):
        self.api = ZapierWorkflowAPI(api_key)
        self.queue = PQueue(max_requests_per_minute)
        self.last_request_time = 0

    def _wait_for_rate_limit(self):
        """Tunggu jika melebihi rate limit"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < 60 / self.queue.maxsize:
            time.sleep(60 / self.queue.maxsize - time_since_last)
        self.last_request_time = time.time()

    def run_action(self, app: str, action: str, data: Dict[str, Any]):
        """Jalankan action dengan rate limiting"""
        self.queue.put(1)  # Tambah ke queue
        self._wait_for_rate_limit()
        try:
            result = self.api.run_action(app, action, data)
            return result
        finally:
            self.queue.get()  # Hapus dari queue

# Contoh penggunaan
rate_limited_api = RateLimitedZapierAPI(api_key="YOUR_ZAPIER_API_KEY")

# Jalankan 100 action (akan di-batch sesuai rate limit)
for i in range(100):
    rate_limited_api.run_action(
        app="slack",
        action="Send Channel Message",
        data={"channel": "#musgo-updates", "text": f"Pesan ke-{i}"}
    )
```

---
### **📌 3. Caching (Penyimpanan Sementara)**
**Masalah:** Beberapa data (misal: daftar aplikasi, template) **tidak berubah sering**.
**Solusi:** Gunakan **caching** untuk **mengurangi panggilan API**.

**Contoh Kode (Python + CacheTools):**
```python
from cachetools import TTLCache
from functools import lru_cache
import time

class CachedZapierAPI:
    def __init__(self, api_key: str):
        self.api = ZapierWorkflowAPI(api_key)
        # Cache dengan TTL (Time To Live) 1 jam
        self.cache = TTLCache(maxsize=100, ttl=3600)

    @lru_cache(maxsize=100)
    def list_apps(self):
        """Daftar aplikasi dengan caching"""
        cache_key = "list_apps"
        if cache_key in self.cache:
            return self.cache[cache_key]

        apps = self.api.list_apps()
        self.cache[cache_key] = apps
        return apps

    def clear_cache(self):
        """Hapus cache"""
        self.cache.clear()
        self.list_apps.cache_clear()  # Clear LRU cache

# Contoh penggunaan
cached_api = CachedZapierAPI(api_key="YOUR_ZAPIER_API_KEY")

# Panggil pertama: akan fetch dari API
apps = cached_api.list_apps()
print("Aplikasi:", apps)

# Panggil kedua: akan ambil dari cache
apps = cached_api.list_apps()
print("Aplikasi (dari cache):", apps)
```

---
### **📌 4. Logging & Monitoring**
**Masalah:** Sulit **debug** jika tidak ada logging.
**Solusi:** Gunakan **logging** untuk **mencatat semua panggilan API**.

**Contoh Kode (Python + Logging):**
```python
import logging
import requests
from typing import Optional, Dict, List, Any

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("zapier_api.log"),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger("ZapierWorkflowAPI")

class LoggedZapierAPI:
    def __init__(self, api_key: str):
        self.api = ZapierWorkflowAPI(api_key)

    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action dengan logging"""
        logger.info(f"Menjalankan action: {app}.{action} dengan data: {data}")
        try:
            result = self.api.run_action(app, action, data)
            logger.info(f"Action berhasil: {app}.{action} - ID: {result.get('id')}")
            return result
        except Exception as e:
            logger.error(f"Action gagal: {app}.{action} - Error: {str(e)}")
            raise

    def create_zap(self, name: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Buat Zap dengan logging"""
        logger.info(f"Membuat Zap: {name} dengan steps: {steps}")
        try:
            zap = self.api.create_zap(name, steps)
            logger.info(f"Zap dibuat: {name} - ID: {zap.get('id')}")
            return zap
        except Exception as e:
            logger.error(f"Gagal membuat Zap: {name} - Error: {str(e)}")
            raise

# Contoh penggunaan
logged_api = LoggedZapierAPI(api_key="YOUR_ZAPIER_API_KEY")

# Jalankan action
logged_api.run_action("slack", "Send Channel Message", {"channel": "#musgo-updates", "text": "Halo!"})

# Buat Zap
logged_api.create_zap(
    name="Test Zap",
    steps=[
        {"app": "google_drive", "action": "New File", "data": {}},
        {"app": "slack", "action": "Send Channel Message", "data": {"channel": "#musgo-updates"}},
    ]
)
```

**Output Log:**
```
2026-05-19 10:00:00,000 - ZapierWorkflowAPI - INFO - Menjalankan action: slack.Send Channel Message dengan data: {'channel': '#musgo-updates', 'text': 'Halo!'}
2026-05-19 10:00:01,000 - ZapierWorkflowAPI - INFO - Action berhasil: slack.Send Channel Message - ID: ACTION_RUN_ID_123
2026-05-19 10:00:02,000 - ZapierWorkflowAPI - INFO - Membuat Zap: Test Zap dengan steps: [{'app': 'google_drive', ...}, {'app': 'slack', ...}]
2026-05-19 10:00:03,000 - ZapierWorkflowAPI - INFO - Zap dibuat: Test Zap - ID: ZAP_ID_456
```

---
### **📌 5. Environment Variables**
**Masalah:** **API Key** tidak boleh **hardcoded**.
**Solusi:** Gunakan **environment variables** (`.env`).

**Contoh:**
1. Buat file `.env`:
   ```env
   ZAPIER_API_KEY=your_api_key_here
   MAX_RETRIES=3
   RATE_LIMIT_PER_MINUTE=60
   ```

2. Gunakan `python-dotenv` untuk load environment variables:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()  # Load .env file

   api_key = os.getenv("ZAPIER_API_KEY")
   max_retries = int(os.getenv("MAX_RETRIES", 3))
   rate_limit = int(os.getenv("RATE_LIMIT_PER_MINUTE", 60))

   api = ZapierWorkflowAPI(api_key=api_key)
   ```

---
### **📌 6. Type Hints (TypeScript)**
**Masalah:** Workflow API **tidak selalu type-safe**.
**Solusi:** Buat **type definitions** untuk data yang dikirim.

**Contoh (TypeScript):**
```typescript
// File: types/zapier.ts
export interface ZapierApp {
  key: string;
  name: string;
  description: string;
  iconUrl: string;
}

export interface ZapierAction {
  id: string;
  app: string;
  name: string;
  description: string;
  inputFields: ZapierField[];
  outputFields: ZapierField[];
}

export interface ZapierField {
  key: string;
  type: "string" | "number" | "boolean" | "datetime" | "text";
  required: boolean;
  helpText: string;
  default?: any;
}

export interface ZapStep {
  id: string;
  app: string;
  action: string;
  data: Record<string, any>;
}

export interface Zap {
  id: string;
  name: string;
  status: "on" | "off" | "paused";
  createdAt: string;
  steps: ZapStep[];
}

export interface ZapRunResult {
  id: string;
  status: "success" | "error";
  data: Record<string, any>;
  error?: string;
}

// File: services/ZapierWorkflowAPI.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from "axios";
import {
  ZapierApp,
  ZapierAction,
  ZapierField,
  ZapStep,
  Zap,
  ZapRunResult,
} from "../types/zapier";

class ZapierWorkflowAPI {
  private client: AxiosInstance;
  private apiKey: string;

  constructor(apiKey: string) {
    this.apiKey = apiKey;
    this.client = axios.create({
      baseURL: "https://api.zapier.com/v2",
      headers: {
        "Authorization": `Bearer ${this.apiKey}`,
        "Content-Type": "application/json",
      },
    });
  }

  // Daftar aplikasi
  async listApps(): Promise<ZapierApp[]> {
    const response = await this.client.get<{ apps: ZapierApp[] }>("/apps");
    return response.data.apps;
  }

  // Daftar action untuk aplikasi
  async listAppActions(appKey: string): Promise<ZapierAction[]> {
    const response = await this.client.get<{ actions: ZapierAction[] }>(
      `/apps/${appKey}/actions`
    );
    return response.data.actions;
  }

  // Jalankan action
  async runAction(
    app: string,
    action: string,
    data: Record<string, any>
  ): Promise<ZapRunResult> {
    const response = await this.client.post<ZapRunResult>("/actions/run", {
      app,
      action,
      data,
    });
    return response.data;
  }

  // Buat Zap
  async createZap(name: string, steps: ZapStep[]): Promise<Zap> {
    const response = await this.client.post<Zap>("/zaps", {
      name,
      steps,
    });
    return response.data;
  }

  // Jalankan Zap
  async runZap(zapId: string, data: Record<string, any> = {}): Promise<ZapRunResult> {
    const response = await this.client.post<ZapRunResult>(
      `/zaps/${zapId}/run`,
      { data }
    );
    return response.data;
  }
}

// Contoh penggunaan
const api = new ZapierWorkflowAPI("YOUR_ZAPIER_API_KEY");

// Daftar aplikasi
const apps = await api.listApps();
console.log("Aplikasi:", apps);

// Jalankan action
const result = await api.runAction("slack", "Send Channel Message", {
  channel: "#musgo-updates",
  text: "Halo!",
});
console.log("Action berjalan:", result);
```

---
---
---

## **🔹 6.5 Contoh Full Workflow untuk MusGo-OS**
### **📌 Skenario: AI Agent + Workflow API**
**Deskripsi:**
AI Agent MusGo-OS akan **menerima perintah user** dan **membuat/menjalankan Zap** menggunakan Workflow API.

**Arsitektur:**
```
User → MusGo-OS AI Agent → Workflow API → Zapier → Aplikasi Eksternal
```

**Contoh Kode (Python - Full Implementation):**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import logging
from zapier_workflow_api import ZapierWorkflowAPI  # Class yang sudah dibuat

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("MusGoAIAgent")

app = FastAPI()

# Dummy database untuk user tokens
user_tokens = {
    "USER_ID_123": "ZAPIER_API_KEY_123",
}

class UserRequest(BaseModel):
    user_id: str
    command: str

class MusGoAIAgent:
    def __init__(self):
        self.zapier_apis = {}  # Cache untuk ZapierWorkflowAPI per user

    def get_zapier_api(self, user_id: str) -> ZapierWorkflowAPI:
        """Ambil atau buat ZapierWorkflowAPI untuk user"""
        if user_id not in self.zapier_apis:
            api_key = user_tokens.get(user_id)
            if not api_key:
                raise HTTPException(status_code=404, detail="User tidak ditemukan")
            self.zapier_apis[user_id] = ZapierWorkflowAPI(api_key)
        return self.zapier_apis[user_id]

    def handle_command(self, user_id: str, command: str) -> Dict[str, Any]:
        """Proses perintah user"""
        command = command.lower()
        api = self.get_zapier_api(user_id)

        try:
            # 1. Daftar aplikasi
            if "aplikasi apa saja yang terintegrasi" in command:
                apps = api.list_apps()
                return {
                    "response": f"📋 Aplikasi yang terintegrasi: {', '.join([app['name'] for app in apps])}",
                    "type": "text",
                }

            # 2. Daftar Zap user
            elif "daftar zap saya" in command:
                zaps = api.list_zaps()
                return {
                    "response": f"📋 Daftar Zap Anda: {', '.join([zap['name'] for zap in zaps])}",
                    "type": "text",
                }

            # 3. Buat Zap Google Drive → Slack
            elif "buatkan zap google drive ke slack" in command:
                folder_match = self._extract_quotes(command, "folder")
                channel_match = self._extract_quotes(command, "channel")

                if not folder_match or not channel_match:
                    return {
                        "response": "❌ Format perintah salah. Contoh: 'Buatkan Zap Google Drive ke Slack dengan folder 'Proyek' ke channel #musgo-updates'",
                        "type": "error",
                    }

                folder = folder_match[1]
                channel = channel_match[1]

                zap = api.create_zap(
                    name=f"Google Drive ({folder}) → Slack ({channel})",
                    steps=[
                        {
                            "app": "google_drive",
                            "action": "New File in Folder",
                            "data": {"folder": folder},
                        },
                        {
                            "app": "slack",
                            "action": "Send Channel Message",
                            "data": {
                                "channel": channel,
                                "text": f"File baru terdeteksi di folder '{folder}': {{file_name}}",
                            },
                        },
                    ]
                )
                return {
                    "response": f"✅ Zap dibuat! ID: {zap['id']}",
                    "type": "success",
                    "zap_id": zap["id"],
                }

            # 4. Jalankan Zap
            elif "jalankan zap" in command:
                zap_id_match = self._extract_quotes(command, "zap")
                if not zap_id_match:
                    return {
                        "response": "❌ Format perintah salah. Contoh: 'Jalankan Zap ZAP_ID_123'",
                        "type": "error",
                    }

                zap_id = zap_id_match[1]
                data_match = self._extract_quotes(command, "data")
                data = {}
                if data_match:
                    try:
                        import json
                        data = json.loads(data_match[1].replace("'", '"'))
                    except:
                        return {
                            "response": "❌ Format data salah. Gunakan JSON valid.",
                            "type": "error",
                        }

                result = api.run_zap(zap_id, data)
                return {
                    "response": f"✅ Zap {zap_id} berjalan!",
                    "type": "success",
                    "result": result,
                }

            # 5. Kirim pesan Slack
            elif "kirim pesan ke slack" in command:
                channel_match = self._extract_quotes(command, "channel")
                text_match = self._extract_quotes(command, "pesan")

                if not channel_match or not text_match:
                    return {
                        "response": "❌ Format perintah salah. Contoh: 'Kirim pesan ke Slack ke channel #musgo-updates dengan pesan 'Halo!'",
                        "type": "error",
                    }

                channel = channel_match[1]
                text = text_match[1]

                result = api.run_action("slack", "Send Channel Message", {
                    "channel": channel,
                    "text": text,
                })
                return {
                    "response": f"✅ Pesan dikirim ke {channel}: '{text}'",
                    "type": "success",
                    "result": result,
                }

            # 6. Buat Zap dari template
            elif "buatkan zap dari template" in command:
                template_id_match = self._extract_quotes(command, "template")
                if not template_id_match:
                    return {
                        "response": "❌ Format perintah salah. Contoh: 'Buatkan Zap dari template TEMPLATE_ID_123'",
                        "type": "error",
                    }

                template_id = template_id_match[1]
                data_match = self._extract_quotes(command, "data")
                data = {}
                if data_match:
                    try:
                        import json
                        data = json.loads(data_match[1].replace("'", '"'))
                    except:
                        return {
                            "response": "❌ Format data salah. Gunakan JSON valid.",
                            "type": "error",
                        }

                zap = api.create_zap_from_template(template_id, data)
                return {
                    "response": f"✅ Zap dibuat dari template! ID: {zap['id']}",
                    "type": "success",
                    "zap_id": zap["id"],
                }

            # Default: Tidak mengerti
            else:
                return {
                    "response": "Maaf, saya tidak mengerti perintah Anda. Coba lagi!",
                    "type": "error",
                }

        except Exception as e:
            logger.error(f"Error memproses perintah: {str(e)}")
            return {
                "response": f"❌ Terjadi kesalahan: {str(e)}",
                "type": "error",
            }

    def _extract_quotes(self, text: str, keyword: str) -> Optional[tuple]:
        """Extract text between quotes after a keyword"""
        import re
        pattern = rf"{keyword}\s*[\"'](.*?)[\"']"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.groups() if match else None

# Inisialisasi AI Agent
ai_agent = MusGoAIAgent()

# Endpoint untuk AI Agent
@app.post("/api/ai-agent/handle-command")
async def handle_command(request: UserRequest):
    """Endpoint untuk AI Agent memproses perintah user"""
    result = ai_agent.handle_command(request.user_id, request.command)
    return result

# Contoh penggunaan
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Contoh Request (AI Agent):**
```python
import requests

# Request ke MusGo-OS AI Agent
response = requests.post(
    "http://localhost:8000/api/ai-agent/handle-command",
    json={
        "user_id": "USER_ID_123",
        "command": "MusGo, buatkan Zap Google Drive ke Slack dengan folder 'Proyek' ke channel #musgo-updates"
    }
)

print("Response:", response.json())
```

**Output:**
```json
{
  "response": "✅ Zap dibuat! ID: ZAP_ID_456",
  "type": "success",
  "zap_id": "ZAP_ID_456"
}
```

---
---
---
# **📌 PART 6: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 6 (Workflow API Reference)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **CRUD Zap** | Buat, baca, update, hapus Zap | ✅ **Contoh kode tersedia** |
| **Run Action** | Jalankan action Zapier | ✅ **Contoh kode tersedia** |
| **Run Zap** | Jalankan Zap dengan data dinamis | ✅ **Contoh kode tersedia** |
| **Zap Templates** | Buat Zap dari template | ✅ **Contoh kode tersedia** |
| **Error Handling** | Tangani error dengan baik | ✅ **Contoh kode tersedia** |
| **Rate Limiting** | Batasi panggilan API | ✅ **Contoh kode tersedia** |
| **Caching** | Kurangi panggilan API | ✅ **Contoh kode tersedia** |
| **Logging** | Catat semua aktivitas | ✅ **Contoh kode tersedia** |
| **Type Safety** | TypeScript support | ✅ **Contoh kode tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Implementasikan `ZapierWorkflowAPI`** (gunakan class yang sudah dibuat).
- [ ] **Test semua endpoint** (buat Zap, jalankan action, dll.).
- [ ] **Integrasikan ke AI Agent MusGo-OS** (gunakan contoh kode di atas).
- [ ] **Setup logging & monitoring** (untuk debugging).

### **2. Mid-Term (1 Bulan)**
- [ ] **Implementasikan rate limiting** (gunakan PQueue).
- [ ] **Implementasikan caching** (untuk daftar aplikasi, template, dll.).
- [ ] **Buat dokumentasi API** untuk developer MusGo-OS.
- [ ] **Test integrasi penuh** (AI Agent + Workflow API).

### **3. Long-Term (3+ Bulan)**
- [ ] **Optimalkan performa** (batch processing, async, dll.).
- [ ] **Luncurkan fitur otomatisasi** ke user MusGo-OS.
- [ ] **Monitor penggunaan API** (untuk menghindari rate limit).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 7: Advanced Use Cases** (Misal: Multi-step Zaps, Error Handling, dll.)
   - [ ] **Part 8: Security & Compliance** (Untuk keamanan Workflow API)
   - [ ] **Part 9: Deployment & Scaling** (Untuk deployment MusGo-OS + Zapier)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + Notion + Slack)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi API untuk MusGo-OS + Zapier Workflow API**?
   - [ ] **Contoh deployment (Docker, Kubernetes)**?

3. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **MusGo-OS → Slack → Google Sheets**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 7: Advanced Use Cases** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi lanjutan** untuk **MusGo-OS 2in1** menggunakan **Zapier Workflow API**, dengan fokus pada **skenario kompleks, error handling, dan integrasi multi-step**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN ADVANCED USE CASES (PART 7)**
*Terjemahan + Implementasi untuk Skenario Kompleks dengan Zapier*

---

---

## **🔹 7.1 Multi-Step Zaps (Otomatisasi Multi-Langkah)**
### **📌 Penjelasan (Bahasa Indonesia)**
**Multi-Step Zaps** adalah **otomatisasi yang terdiri dari 2+ langkah** (trigger + 1+ action). Contoh:
- **Trigger**: Google Drive → New File
- **Step 1**: AI Agent MusGo-OS → Analisis File
- **Step 2**: Slack → Kirim Notifikasi
- **Step 3**: Notion → Simpan Hasil ke Database

**Manfaat untuk MusGo-OS:**
- **AI Agent bisa terintegrasi dalam workflow** (misal: analisis file sebelum dikirim ke Slack).
- **User bisa membuat workflow yang lebih powerful**.

---
### **🚀 Contoh Implementasi: Multi-Step Zap dengan AI Agent**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: File baru di Google Drive folder "Laporan".
2. **Step 1**: AI Agent MusGo-OS **menganalisis file** (misal: extract text, ringkasan).
3. **Step 2**: **Kirim notifikasi ke Slack** dengan hasil analisis.
4. **Step 3**: **Simpan hasil ke Notion** (database "Laporan Teranalisis").

**Arsitektur:**
```
Google Drive (Trigger) → MusGo-OS AI Agent (Step 1) → Slack (Step 2) → Notion (Step 3)
```

---
#### **1. Backend MusGo-OS (Python - FastAPI)**
**Endpoint untuk AI Agent (Step 1):**
```python
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import requests
import json

app = FastAPI()

# Dummy AI Agent (ganti dengan AI Agent asli MusGo-OS)
def analyze_file(file_url: str, file_name: str) -> Dict[str, Any]:
    """Simulasi AI Agent menganalisis file"""
    # Contoh: Extract text dari PDF (gunakan library seperti PyPDF2)
    # Di sini kita simulasikan hasil analisis
    return {
        "file_name": file_name,
        "summary": f"Ringkasan dari {file_name}: Ini adalah laporan proyek MusGo-OS.",
        "keywords": ["MusGo-OS", "AI", "Automation", "Zapier"],
        "sentiment": "positive",
    }

# Endpoint untuk Zapier (Step 1)
@app.post("/api/zapier/ai-analyze")
async def ai_analyze(request: Request):
    """Endpoint untuk Zapier memanggil AI Agent MusGo-OS"""
    data = await request.json()
    file_url = data.get("file_url")
    file_name = data.get("file_name")

    if not file_url or not file_name:
        raise HTTPException(status_code=400, detail="file_url dan file_name diperlukan")

    # Analisis file dengan AI Agent
    analysis = analyze_file(file_url, file_name)

    return {
        "status": "success",
        "data": analysis,
    }

# Endpoint untuk testing
@app.get("/test-ai-analyze")
async def test_ai_analyze():
    """Test endpoint AI Agent"""
    return analyze_file(
        file_url="https://drive.google.com/file/d/12345",
        file_name="laporan_proyek.pdf"
    )
```

---
#### **2. Workflow API: Buat Multi-Step Zap**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

# Inisialisasi
api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Multi-Step Zap
zap = api.create_zap(
    name="Google Drive → AI Agent → Slack → Notion",
    steps=[
        # Trigger: Google Drive → New File
        {
            "id": "trigger_1",
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {
                "folder": "Laporan",
            },
        },
        # Step 1: MusGo-OS AI Agent → Analisis File
        {
            "id": "step_1",
            "app": "webhooks",  # Gunakan Webhooks untuk memanggil API MusGo-OS
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/ai-analyze",
                "payload": {
                    "file_url": "{file_url}",
                    "file_name": "{file_name}",
                },
            },
        },
        # Step 2: Slack → Kirim Notifikasi
        {
            "id": "step_2",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-reports",
                "text": "📄 File baru teranalisis!\n"
                       "Nama: {file_name}\n"
                       "Ringkasan: {step_1_summary}\n"
                       "Keywords: {step_1_keywords}",
            },
        },
        # Step 3: Notion → Simpan ke Database
        {
            "id": "step_3",
            "app": "notion",
            "action": "Create Database Row",
            "data": {
                "databaseId": "NOTION_DATABASE_ID",
                "properties": {
                    "Nama File": {"title": [{"text": {"content": "{file_name}"}}]},
                    "Ringkasan": {"rich_text": [{"text": {"content": "{step_1_summary}"}}]},
                    "Keywords": {"rich_text": [{"text": {"content": ", ".join("{step_1_keywords}")}}]},
                    "Sentimen": {"select": {"name": "{step_1_sentiment}"}},
                    "URL": {"url": "{file_url}"},
                },
            },
        },
    ]
)

print("✅ Multi-Step Zap dibuat:", zap)
```

**Catatan:**
- **`{file_name}`, `{file_url}`**: Data dari **trigger** (Google Drive).
- **`{step_1_summary}`, `{step_1_keywords}`**: Data dari **Step 1** (AI Agent).
- **Webhooks**: Digunakan untuk **memanggil API MusGo-OS** (karena MusGo-OS belum terdaftar di Zapier App Directory).

---
#### **3. Testing Multi-Step Zap**
**Cara Test:**
1. **Upload file baru** ke folder "Laporan" di Google Drive.
2. **Zapier akan:**
   - Memicu **trigger** (Google Drive).
   - Memanggil **AI Agent MusGo-OS** (via Webhooks).
   - Mengirim **notifikasi ke Slack**.
   - Menyimpan **hasil ke Notion**.

**Contoh Output di Slack:**
```
📄 File baru teranalisis!
Nama: laporan_proyek.pdf
Ringkasan: Ringkasan dari laporan_proyek.pdf: Ini adalah laporan proyek MusGo-OS.
Keywords: MusGo-OS, AI, Automation, Zapier
```

**Contoh Output di Notion:**
| Nama File          | Ringkasan                                      | Keywords                     | Sentimen | URL                          |
|--------------------|------------------------------------------------|------------------------------|----------|------------------------------|
| laporan_proyek.pdf | Ringkasan dari laporan_proyek.pdf: ...         | MusGo-OS, AI, Automation, ... | Positive  | [Link ke file](...)          |

---
---
---

## **🔹 7.2 Conditional Logic (Logika Bersyarat)**
### **📌 Penjelasan**
**Conditional Logic** memungkinkan **Zap untuk menjalankan langkah tertentu hanya jika kondisi terpenuhi**. Contoh:
- **Jika** `sentiment == "positive"` → **Kirim ke Slack #musgo-positive**.
- **Jika** `sentiment == "negative"` → **Kirim ke Slack #musgo-negative**.

**Manfaat untuk MusGo-OS:**
- **Workflow lebih fleksibel** (tidak semua langkah selalu dijalankan).
- **AI Agent bisa mengontrol alur workflow**.

---
### **🚀 Contoh Implementasi: Conditional Logic**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: AI Agent MusGo-OS menyelesaikan tugas.
2. **Conditional**:
   - **Jika** `priority == "high"` → **Kirim notifikasi ke Slack #musgo-high-priority**.
   - **Jika** `priority == "low"` → **Kirim ke Slack #musgo-low-priority**.
   - **Jika** `priority == "medium"` → **Kirim ke Slack #musgo-updates**.

**Arsitektur:**
```
AI Agent (Trigger) → [Conditional] → Slack (Action)
```

---
#### **1. Workflow API: Buat Zap dengan Conditional Logic**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan conditional logic
zap = api.create_zap(
    name="AI Agent → Conditional Slack",
    steps=[
        # Trigger: MusGo-OS AI Agent → Task Completed
        {
            "id": "trigger_1",
            "app": "webhooks",  # Gunakan Webhooks untuk trigger dari MusGo-OS
            "action": "GET",    # Atau POST, tergantung setup
            "data": {
                "url": "https://musgo-os.com/api/zapier/triggers/task_completed",
            },
        },
        # Step 1: Filter (Conditional)
        {
            "id": "filter_1",
            "app": "filter",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "priority",
                        "operator": "equals",
                        "value": "high",
                    },
                ],
            },
        },
        # Step 2: Kirim ke #musgo-high-priority (jika priority == high)
        {
            "id": "step_2_high",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-high-priority",
                "text": "🚨 Tugas prioritas tinggi selesai!\n"
                       "Nama: {task_name}\n"
                       "Agent: {agent_id}\n"
                       "Waktu: {completion_time}",
            },
        },
        # Step 3: Filter (Conditional untuk medium)
        {
            "id": "filter_2",
            "app": "filter",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "priority",
                        "operator": "equals",
                        "value": "medium",
                    },
                ],
            },
        },
        # Step 4: Kirim ke #musgo-updates (jika priority == medium)
        {
            "id": "step_4_medium",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-updates",
                "text": "⚡ Tugas prioritas menengah selesai!\n"
                       "Nama: {task_name}\n"
                       "Agent: {agent_id}",
            },
        },
        # Step 5: Filter (Conditional untuk low)
        {
            "id": "filter_3",
            "app": "filter",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "priority",
                        "operator": "equals",
                        "value": "low",
                    },
                ],
            },
        },
        # Step 6: Kirim ke #musgo-low-priority (jika priority == low)
        {
            "id": "step_6_low",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-low-priority",
                "text": "✅ Tugas prioritas rendah selesai!\n"
                       "Nama: {task_name}",
            },
        },
    ]
)

print("✅ Zap dengan Conditional Logic dibuat:", zap)
```

**Catatan:**
- **Filter** di Zapier **menghentikan workflow** jika kondisi **tidak terpenuhi**.
- **Setiap filter** harus diikuti oleh **action yang sesuai**.

---
#### **2. Alternatif: Gunakan Code by Zapier**
Jika **filter** terlalu terbatas, gunakan **Code by Zapier** (JavaScript/Python) untuk **logika yang lebih kompleks**.

**Contoh Kode (JavaScript untuk Code by Zapier):**
```javascript
// Input data dari trigger
const inputData = inputData;

// Tentukan channel Slack berdasarkan priority
let channel, message;

if (inputData.priority === "high") {
  channel = "#musgo-high-priority";
  message = `🚨 Tugas prioritas tinggi selesai!\nNama: ${inputData.task_name}\nAgent: ${inputData.agent_id}`;
} else if (inputData.priority === "medium") {
  channel = "#musgo-updates";
  message = `⚡ Tugas prioritas menengah selesai!\nNama: ${inputData.task_name}`;
} else {
  channel = "#musgo-low-priority";
  message = `✅ Tugas prioritas rendah selesai!\nNama: ${inputData.task_name}`;
}

// Output untuk step selanjutnya
output = { channel, message };
```

**Cara Integrasi ke Zap:**
1. Tambahkan **Code by Zapier** sebagai **Step 1**.
2. Tambahkan **Slack → Send Channel Message** sebagai **Step 2** (gunakan `output.channel` dan `output.message`).

---
---
---

## **🔹 7.3 Error Handling & Retry (Penanganan Error)**
### **📌 Penjelasan**
**Error Handling** sangat penting untuk **workflow yang reliable**. Zapier menyediakan:
- **Retry**: Otomatis mencoba lagi jika gagal.
- **Error Notification**: Kirim notifikasi jika workflow gagal.
- **Fallback Action**: Jalankan action alternatif jika gagal.

**Manfaat untuk MusGo-OS:**
- **Workflow tidak gagal total** jika satu langkah gagal.
- **User tahu jika ada error**.

---
### **🚀 Contoh Implementasi: Error Handling**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: Google Drive → New File.
2. **Step 1**: AI Agent MusGo-OS → Analisis File.
3. **Step 2**: Slack → Kirim Notifikasi.
4. **Jika Step 1 gagal** → **Kirim notifikasi error ke Slack #musgo-errors**.

**Arsitektur:**
```
Google Drive (Trigger) → [AI Agent (Step 1)] → [Slack (Step 2)]
                          ↓ (Jika gagal)
                     Slack #musgo-errors (Fallback)
```

---
#### **1. Workflow API: Zap dengan Error Handling**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan error handling
zap = api.create_zap(
    name="Google Drive → AI Agent → Slack (dengan Error Handling)",
    steps=[
        # Trigger: Google Drive → New File
        {
            "id": "trigger_1",
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {"folder": "Laporan"},
        },
        # Step 1: AI Agent → Analisis File (dengan retry)
        {
            "id": "step_1",
            "app": "webhooks",
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/ai-analyze",
                "payload": {
                    "file_url": "{file_url}",
                    "file_name": "{file_name}",
                },
                "retry": True,  # Aktifkan retry
                "max_retries": 3,  # Maksimal 3 percobaan
            },
        },
        # Step 2: Slack → Kirim Notifikasi (jika Step 1 berhasil)
        {
            "id": "step_2",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-reports",
                "text": "📄 File teranalisis!\n"
                       "Nama: {file_name}\n"
                       "Ringkasan: {step_1_summary}",
            },
        },
        # Step 3: Filter (Jika Step 1 gagal)
        {
            "id": "filter_1",
            "app": "filter",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "step_1_status",
                        "operator": "equals",
                        "value": "error",
                    },
                ],
            },
        },
        # Step 4: Slack → Kirim Notifikasi Error (Fallback)
        {
            "id": "step_4",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-errors",
                "text": "❌ Error menganalisis file!\n"
                       "Nama: {file_name}\n"
                       "Error: {step_1_error}\n"
                       "URL: {file_url}",
            },
        },
    ]
)

print("✅ Zap dengan Error Handling dibuat:", zap)
```

**Catatan:**
- **`retry: True`**: Zapier akan **mencoba lagi** jika Step 1 gagal.
- **`max_retries: 3`**: Maksimal **3 percobaan**.
- **Filter**: Digunakan untuk **memeriksa apakah Step 1 gagal** (`step_1_status == "error"`).

---
#### **2. Backend MusGo-OS: Tambahkan Error Handling**
**Modifikasi endpoint AI Agent untuk mengembalikan error:**
```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging

app = FastAPI()
logger = logging.getLogger("MusGoAIAgent")

@app.post("/api/zapier/ai-analyze")
async def ai_analyze(request: Request):
    try:
        data = await request.json()
        file_url = data.get("file_url")
        file_name = data.get("file_name")

        if not file_url or not file_name:
            return JSONResponse(
                status_code=400,
                content={
                    "status": "error",
                    "error": "file_url dan file_name diperlukan",
                }
            )

        # Simulasi error (10% chance)
        import random
        if random.random() < 0.1:  # 10% chance error
            raise Exception("Gagal menganalisis file: Server AI Agent sibuk")

        # Analisis file
        analysis = {
            "file_name": file_name,
            "summary": f"Ringkasan dari {file_name}: Ini adalah laporan proyek MusGo-OS.",
            "keywords": ["MusGo-OS", "AI", "Automation"],
        }

        return {
            "status": "success",
            "data": analysis,
        }

    except Exception as e:
        logger.error(f"Error menganalisis file: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "error": str(e),
            }
        )
```

**Output jika Error:**
- **Step 1**: Gagal (status: `error`).
- **Filter**: Terpenuhi (`step_1_status == "error"`).
- **Step 4**: Kirim notifikasi error ke `#musgo-errors`.

**Contoh Notifikasi Error di Slack:**
```
❌ Error menganalisis file!
Nama: laporan_proyek.pdf
Error: Gagal menganalisis file: Server AI Agent sibuk
URL: https://drive.google.com/file/d/12345
```

---
---
---

## **🔹 7.4 Delayed Actions (Tindakan Tertunda)**
### **📌 Penjelasan**
**Delayed Actions** memungkinkan **Zap untuk menunda eksekusi** (misal: tunggu 1 jam sebelum mengirim email). Contoh:
- **Trigger**: User mendaftar di MusGo-OS.
- **Action**: Kirim email **1 jam kemudian** (untuk follow-up).

**Manfaat untuk MusGo-OS:**
- **Workflow lebih fleksibel** (bisa menunda tindakan).
- **User experience lebih baik** (misal: follow-up otomatis).

---
### **🚀 Contoh Implementasi: Delayed Actions**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: User mendaftar di MusGo-OS (via Webhooks).
2. **Action**: Kirim email **1 jam kemudian** (untuk follow-up).

**Arsitektur:**
```
User Signup (Trigger) → [Delay 1 Jam] → Gmail (Action)
```

---
#### **1. Workflow API: Zap dengan Delay**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan delay
zap = api.create_zap(
    name="User Signup → Delayed Email",
    steps=[
        # Trigger: Webhooks (User Signup)
        {
            "id": "trigger_1",
            "app": "webhooks",
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/triggers/user_signup",
            },
        },
        # Step 1: Delay 1 Jam
        {
            "id": "step_1",
            "app": "delay",
            "action": "Delay For",
            "data": {
                "time": 3600,  # 1 jam (dalam detik)
            },
        },
        # Step 2: Kirim Email
        {
            "id": "step_2",
            "app": "gmail",
            "action": "Send Email",
            "data": {
                "to": "{user_email}",
                "subject": "Selamat Datang di MusGo-OS!",
                "body": f"Halo {{{{user_name}}}},\n\n"
                       f"Terima kasih telah mendaftar di MusGo-OS!\n"
                       f"Kami senang Anda bergabung.\n\n"
                       f"Jika Anda memiliki pertanyaan, balas email ini.\n\n"
                       f"Salam,\n"
                       f"Tim MusGo-OS",
            },
        },
    ]
)

print("✅ Zap dengan Delay dibuat:", zap)
```

**Catatan:**
- **`{user_email}`, `{user_name}`**: Data dari **trigger** (Webhooks).
- **Delay**: Zapier akan **menunggu 1 jam** sebelum menjalankan Step 2.

---
#### **2. Backend MusGo-OS: Trigger User Signup**
**Contoh Endpoint (Python - FastAPI):**
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Dummy database untuk user
users_db = {}

@app.post("/api/zapier/triggers/user_signup")
async def user_signup(request: Request):
    """Endpoint untuk trigger user signup"""
    data = await request.json()
    user_id = data.get("user_id")
    user_email = data.get("email")
    user_name = data.get("name")

    if not user_id or not user_email:
        return JSONResponse(
            status_code=400,
            content={"error": "user_id dan email diperlukan"}
        )

    # Simpan user (opsional)
    users_db[user_id] = {
        "email": user_email,
        "name": user_name,
    }

    # Return data untuk Zapier
    return {
        "user_id": user_id,
        "user_email": user_email,
        "user_name": user_name,
    }

# Contoh penggunaan (simulasi)
@app.get("/test-user-signup")
async def test_user_signup():
    """Test trigger user signup"""
    return {
        "user_id": "USER_ID_456",
        "email": "dhani@musgo-os.com",
        "name": "Dhani Yuliawan",
    }
```

---
---
---

## **🔹 7.5 Paths (Rute Berdasarkan Data)**
### **📌 Penjelasan**
**Paths** memungkinkan **Zap untuk memilih rute yang berbeda** berdasarkan **nilai data**. Contoh:
- **Jika** `file_type == "pdf"` → **Analisis dengan AI Agent PDF**.
- **Jika** `file_type == "image"` → **Analisis dengan AI Agent Image**.

**Manfaat untuk MusGo-OS:**
- **Workflow lebih dinamis** (bisa memilih rute berdasarkan data).
- **AI Agent bisa spesifik untuk tiap jenis file**.

---
### **🚀 Contoh Implementasi: Paths**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: Google Drive → New File.
2. **Paths**:
   - **Jika** `file_extension == "pdf"` → **AI Agent PDF → Analisis PDF**.
   - **Jika** `file_extension == "jpg" || "png"` → **AI Agent Image → Analisis Gambar**.
   - **Jika** `file_extension == "csv" || "xlsx"` → **AI Agent Data → Analisis Data**.

**Arsitektur:**
```
Google Drive (Trigger) → [Paths] → AI Agent (Spesifik) → Slack (Notifikasi)
```

---
#### **1. Workflow API: Zap dengan Paths**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan Paths
zap = api.create_zap(
    name="Google Drive → Paths → AI Agent",
    steps=[
        # Trigger: Google Drive → New File
        {
            "id": "trigger_1",
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {"folder": "Uploads"},
        },
        # Path 1: Jika file PDF
        {
            "id": "path_1_pdf",
            "app": "paths",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "file_extension",
                        "operator": "equals",
                        "value": "pdf",
                    },
                ],
            },
        },
        {
            "id": "step_1_pdf",
            "app": "webhooks",
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/ai-analyze-pdf",
                "payload": {
                    "file_url": "{file_url}",
                    "file_name": "{file_name}",
                },
            },
        },
        {
            "id": "step_2_pdf",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-pdf",
                "text": "📄 File PDF teranalisis!\n"
                       "Nama: {file_name}\n"
                       "Ringkasan: {step_1_pdf_summary}",
            },
        },
        # Path 2: Jika file Image (jpg/png)
        {
            "id": "path_2_image",
            "app": "paths",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "file_extension",
                        "operator": "equals_any",
                        "value": ["jpg", "jpeg", "png"],
                    },
                ],
            },
        },
        {
            "id": "step_1_image",
            "app": "webhooks",
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/ai-analyze-image",
                "payload": {
                    "file_url": "{file_url}",
                    "file_name": "{file_name}",
                },
            },
        },
        {
            "id": "step_2_image",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-images",
                "text": "🖼️ Gambar teranalisis!\n"
                       "Nama: {file_name}\n"
                       "Deskripsi: {step_1_image_description}",
            },
        },
        # Path 3: Jika file Data (csv/xlsx)
        {
            "id": "path_3_data",
            "app": "paths",
            "action": "Only continue if...",
            "data": {
                "rules": [
                    {
                        "field": "file_extension",
                        "operator": "equals_any",
                        "value": ["csv", "xlsx"],
                    },
                ],
            },
        },
        {
            "id": "step_1_data",
            "app": "webhooks",
            "action": "POST",
            "data": {
                "url": "https://musgo-os.com/api/zapier/ai-analyze-data",
                "payload": {
                    "file_url": "{file_url}",
                    "file_name": "{file_name}",
                },
            },
        },
        {
            "id": "step_2_data",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-data",
                "text": "📊 Data teranalisis!\n"
                       "Nama: {file_name}\n"
                       "Statistik: {step_1_data_stats}",
            },
        },
    ]
)

print("✅ Zap dengan Paths dibuat:", zap)
```

**Catatan:**
- **`file_extension`**: Diambil dari **Google Drive trigger** (misal: `pdf`, `jpg`, `csv`).
- **Paths**: Setiap path **memiliki kondisi** (`file_extension == "pdf"`).
- **AI Agent Spesifik**: Setiap path **memanggil AI Agent yang berbeda**.

---
#### **2. Backend MusGo-OS: AI Agent Spesifik**
**Contoh Endpoint (Python - FastAPI):**
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# AI Agent untuk PDF
@app.post("/api/zapier/ai-analyze-pdf")
async def ai_analyze_pdf(request: Request):
    data = await request.json()
    file_url = data.get("file_url")
    file_name = data.get("file_name")

    # Simulasi analisis PDF
    return {
        "status": "success",
        "data": {
            "file_name": file_name,
            "summary": f"Ringkasan PDF {file_name}: Dokumen ini berisi tentang MusGo-OS.",
            "keywords": ["MusGo-OS", "AI", "PDF"],
        },
    }

# AI Agent untuk Image
@app.post("/api/zapier/ai-analyze-image")
async def ai_analyze_image(request: Request):
    data = await request.json()
    file_url = data.get("file_url")
    file_name = data.get("file_name")

    # Simulasi analisis Image
    return {
        "status": "success",
        "data": {
            "file_name": file_name,
            "description": f"Deskripsi gambar {file_name}: Gambar ini menampilkan dashboard MusGo-OS.",
            "tags": ["dashboard", "UI", "MusGo-OS"],
        },
    }

# AI Agent untuk Data
@app.post("/api/zapier/ai-analyze-data")
async def ai_analyze_data(request: Request):
    data = await request.json()
    file_url = data.get("file_url")
    file_name = data.get("file_name")

    # Simulasi analisis Data
    return {
        "status": "success",
        "data": {
            "file_name": file_name,
            "stats": f"Statistik data {file_name}: 100 baris, 5 kolom.",
            "insights": ["Trend positif", "Outlier terdeteksi"],
        },
    }
```

---
---
---

## **🔹 7.6 Formatter (Format Data)**
### **📌 Penjelasan**
**Formatter** memungkinkan **Zap untuk memformat data** sebelum dikirim ke action selanjutnya. Contoh:
- **Format tanggal**: `2026-05-19` → `19 Mei 2026`.
- **Format teks**: `hello world` → `Hello World`.
- **Format angka**: `1000` → `1,000`.

**Manfaat untuk MusGo-OS:**
- **Data lebih rapi** sebelum dikirim ke Slack/Notion.
- **User experience lebih baik**.

---
### **🚀 Contoh Implementasi: Formatter**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: Google Drive → New File.
2. **Formatter**: Format `file_name` dan `file_size`.
3. **Action**: Slack → Kirim Notifikasi.

**Arsitektur:**
```
Google Drive (Trigger) → Formatter → Slack (Action)
```

---
#### **1. Workflow API: Zap dengan Formatter**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan Formatter
zap = api.create_zap(
    name="Google Drive → Formatter → Slack",
    steps=[
        # Trigger: Google Drive → New File
        {
            "id": "trigger_1",
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {"folder": "Uploads"},
        },
        # Step 1: Formatter (Format file_name)
        {
            "id": "step_1_format_name",
            "app": "formatter",
            "action": "Text",
            "data": {
                "input": "{file_name}",
                "transformation": "capitalize",  # Capitalize setiap kata
            },
        },
        # Step 2: Formatter (Format file_size)
        {
            "id": "step_2_format_size",
            "app": "formatter",
            "action": "Number",
            "data": {
                "input": "{file_size}",
                "transformation": "humanize",  # 1024 → "1 KB"
            },
        },
        # Step 3: Formatter (Format date)
        {
            "id": "step_3_format_date",
            "app": "formatter",
            "action": "Date / Time",
            "data": {
                "input": "{file_created_at}",
                "from_format": "iso8601",  # Format input
                "to_format": "DD MMMM YYYY, HH:mm",  # Format output: "19 Mei 2026, 10:00"
            },
        },
        # Step 4: Slack → Kirim Notifikasi
        {
            "id": "step_4",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-uploads",
                "text": "📁 File baru diupload!\n"
                       "Nama: {step_1_format_name}\n"
                       "Ukuran: {step_2_format_size}\n"
                       "Diupload: {step_3_format_date}\n"
                       "URL: {file_url}",
            },
        },
    ]
)

print("✅ Zap dengan Formatter dibuat:", zap)
```

**Contoh Output di Slack:**
```
📁 File baru diupload!
Nama: Laporan Proyek Musgo Os
Ukuran: 1.2 MB
Diupload: 19 Mei 2026, 10:00
URL: https://drive.google.com/file/d/12345
```

---
#### **2. Formatter Custom (Code by Zapier)**
Jika **Formatter bawaan Zapier tidak cukup**, gunakan **Code by Zapier** (JavaScript/Python).

**Contoh Kode (JavaScript untuk Code by Zapier):**
```javascript
// Input data
const inputData = inputData;

// Format file_name (ganti underscore dengan spasi)
let formattedName = inputData.file_name.replace(/_/g, " ");

// Format file_size (konversi bytes ke KB/MB)
let fileSize = inputData.file_size;
let formattedSize;
if (fileSize < 1024) {
  formattedSize = `${fileSize} bytes`;
} else if (fileSize < 1024 * 1024) {
  formattedSize = `${(fileSize / 1024).toFixed(2)} KB`;
} else {
  formattedSize = `${(fileSize / (1024 * 1024)).toFixed(2)} MB`;
}

// Format date (ISO 8601 → DD MMMM YYYY)
const date = new Date(inputData.file_created_at);
const formattedDate = date.toLocaleDateString("id-ID", {
  day: "2-digit",
  month: "long",
  year: "numeric",
});

// Output untuk step selanjutnya
output = {
  formattedName,
  formattedSize,
  formattedDate,
};
```

---
---
---

## **🔹 7.7 Webhooks (Integrasi dengan API Eksternal)**
### **📌 Penjelasan**
**Webhooks** memungkinkan **Zap untuk berkomunikasi dengan API eksternal** (misal: API MusGo-OS). Ada **2 jenis**:
1. **Incoming Webhooks**: Zapier **menerima data** dari API eksternal (trigger).
2. **Outgoing Webhooks**: Zapier **mengirim data** ke API eksternal (action).

**Manfaat untuk MusGo-OS:**
- **Integrasi dengan API MusGo-OS** (misal: AI Agent, Database).
- **Fleksibilitas tinggi** (bisa terhubung ke sistem mana pun).

---
### **🚀 Contoh Implementasi: Webhooks**
#### **Skenario 1: Incoming Webhooks (Trigger)**
**Deskripsi:**
MusGo-OS ingin **menerima trigger dari Zapier** saat AI Agent menyelesaikan tugas.

**Cara Kerja:**
1. **MusGo-OS** mendaftarkan **webhook URL** di Zapier.
2. **Saat AI Agent menyelesaikan tugas**, Zapier **mengirim POST request** ke MusGo-OS.
3. **MusGo-OS** memproses data dan **menjalankan aksi** (misal: update database).

**Arsitektur:**
```
AI Agent (Zapier Trigger) → Webhook → MusGo-OS Backend
```

---
##### **1. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import logging

app = FastAPI()
logger = logging.getLogger("MusGoOSWebhooks")

# Endpoint untuk incoming webhook
@app.post("/api/zapier/webhooks/task-completed")
async def task_completed_webhook(request: Request):
    """Terima webhook dari Zapier saat task selesai"""
    try:
        data = await request.json()
        task_id = data.get("task_id")
        task_name = data.get("task_name")
        agent_id = data.get("agent_id")
        status = data.get("status")

        if not task_id or not task_name:
            raise HTTPException(status_code=400, detail="task_id dan task_name diperlukan")

        logger.info(f"Task selesai: {task_name} (ID: {task_id}, Agent: {agent_id})")

        # Update database (contoh)
        update_task_in_database(task_id, status)

        # Kirim response sukses
        return JSONResponse(
            status_code=200,
            content={"status": "success", "message": "Task updated"}
        )

    except Exception as e:
        logger.error(f"Error memproses webhook: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

# Helper function (contoh)
def update_task_in_database(task_id: str, status: str):
    """Update task di database"""
    # Implementasi tergantung database Anda
    logger.info(f"Update task {task_id} ke status: {status}")

# Endpoint untuk testing
@app.get("/test-webhook")
async def test_webhook():
    """Test incoming webhook"""
    return {
        "message": "Webhook endpoint berjalan. Kirim POST request ke /api/zapier/webhooks/task-completed"
    }
```

---
##### **2. Zapier: Setup Incoming Webhook**
1. **Buat Zap** dengan **trigger: Webhooks by Zapier → Catch Hook**.
2. **Set URL**: `https://musgo-os.com/api/zapier/webhooks/task-completed`.
3. **Pilih method**: `POST`.
4. **Test webhook** (Zapier akan mengirim test request).

**Contoh Data yang Dikirim Zapier:**
```json
{
  "task_id": "TASK_ID_123",
  "task_name": "Implementasi MCP",
  "agent_id": "planner",
  "status": "completed",
  "completion_time": "2026-05-19T10:00:00Z"
}
```

---
#### **Skenario 2: Outgoing Webhooks (Action)**
**Deskripsi:**
MusGo-OS ingin **Zapier memanggil API MusGo-OS** untuk menjalankan AI Agent.

**Cara Kerja:**
1. **Trigger**: Google Drive → New File.
2. **Action**: **Webhooks → POST** ke API MusGo-OS (`/api/zapier/ai-analyze`).
3. **MusGo-OS** memproses request dan **mengembalikan hasil**.

**Arsitektur:**
```
Google Drive (Trigger) → Webhooks (Action) → MusGo-OS API
```

---
##### **1. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Endpoint untuk outgoing webhook (action)
@app.post("/api/zapier/ai-analyze")
async def ai_analyze(request: Request):
    """Endpoint untuk Zapier memanggil AI Agent MusGo-OS"""
    try:
        data = await request.json()
        file_url = data.get("file_url")
        file_name = data.get("file_name")

        if not file_url or not file_name:
            return JSONResponse(
                status_code=400,
                content={"error": "file_url dan file_name diperlukan"}
            )

        # Analisis file dengan AI Agent (simulasi)
        analysis = {
            "file_name": file_name,
            "summary": f"Ringkasan dari {file_name}: Ini adalah dokumen MusGo-OS.",
            "keywords": ["MusGo-OS", "AI", "Automation"],
        }

        return {
            "status": "success",
            "data": analysis,
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "error": str(e)}
        )
```

---
##### **2. Zapier: Setup Outgoing Webhook**
1. **Buat Zap** dengan:
   - **Trigger**: Google Drive → New File in Folder.
   - **Action**: Webhooks by Zapier → POST.
2. **Set URL**: `https://musgo-os.com/api/zapier/ai-analyze`.
3. **Set Data**:
   ```json
   {
     "file_url": "{file_url}",
     "file_name": "{file_name}"
   }
   ```
4. **Test Zap**.

**Contoh Data yang Dikirim ke MusGo-OS:**
```json
{
  "file_url": "https://drive.google.com/file/d/12345",
  "file_name": "laporan_proyek.pdf"
}
```

**Contoh Response dari MusGo-OS:**
```json
{
  "status": "success",
  "data": {
    "file_name": "laporan_proyek.pdf",
    "summary": "Ringkasan dari laporan_proyek.pdf: Ini adalah dokumen MusGo-OS.",
    "keywords": ["MusGo-OS", "AI", "Automation"]
  }
}
```

---
---
---

## **🔹 7.8 Code by Zapier (Kode Kustom)**
### **📌 Penjelasan**
**Code by Zapier** memungkinkan **menjalankan kode JavaScript/Python** di tengah workflow. Ini berguna untuk:
- **Logika yang kompleks** (tidak bisa dilakukan dengan Filter/Formatter).
- **Integrasi dengan API eksternal** (tanpa perlu Webhooks).
- **Transformasi data** (misal: konversi format, enkripsi).

**Manfaat untuk MusGo-OS:**
- **Fleksibilitas tinggi** (bisa menjalankan kode kustom).
- **Integrasi dengan sistem internal MusGo-OS**.

---
### **🚀 Contoh Implementasi: Code by Zapier**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: Google Drive → New File.
2. **Step 1**: **Code by Zapier** (JavaScript) → Extract metadata dari file name.
3. **Step 2**: Slack → Kirim Notifikasi dengan metadata.

**Arsitektur:**
```
Google Drive (Trigger) → Code by Zapier (Step 1) → Slack (Step 2)
```

---
#### **1. Workflow API: Zap dengan Code by Zapier**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan Code by Zapier
zap = api.create_zap(
    name="Google Drive → Code → Slack",
    steps=[
        # Trigger: Google Drive → New File
        {
            "id": "trigger_1",
            "app": "google_drive",
            "action": "New File in Folder",
            "data": {"folder": "Uploads"},
        },
        # Step 1: Code by Zapier (JavaScript)
        {
            "id": "step_1",
            "app": "code",
            "action": "Run JavaScript",
            "data": {
                "code": """
                // Extract metadata dari file_name
                const inputData = inputData;
                const fileName = inputData.file_name;

                // Contoh format: "Laporan_Proyek_MusGo-OS_2026-05-19.pdf"
                const parts = fileName.split(/[_\-.]/);
                const metadata = {
                  type: parts[0] || "Unknown",  // Laporan
                  project: parts[1] || "Unknown",  // Proyek
                  system: parts[2] || "Unknown",  // MusGo-OS
                  date: parts[3] || "Unknown",  // 2026-05-19
                  extension: parts[4] || "Unknown",  // pdf
                };

                // Output untuk step selanjutnya
                output = { ...inputData, ...metadata };
                """,
            },
        },
        # Step 2: Slack → Kirim Notifikasi
        {
            "id": "step_2",
            "app": "slack",
            "action": "Send Channel Message",
            "data": {
                "channel": "#musgo-uploads",
                "text": "📁 File baru diupload!\n"
                       "Nama: {file_name}\n"
                       "Tipe: {type}\n"
                       "Proyek: {project}\n"
                       "Sistem: {system}\n"
                       "Tanggal: {date}\n"
                       "URL: {file_url}",
            },
        },
    ]
)

print("✅ Zap dengan Code by Zapier dibuat:", zap)
```

**Contoh Output di Slack:**
```
📁 File baru diupload!
Nama: Laporan_Proyek_MusGo-OS_2026-05-19.pdf
Tipe: Laporan
Proyek: Proyek
Sistem: MusGo-OS
Tanggal: 2026-05-19
URL: https://drive.google.com/file/d/12345
```

---
#### **2. Code by Zapier (Python)**
Jika Anda lebih suka **Python**, gunakan **Code by Zapier (Python)**.

**Contoh Kode (Python untuk Code by Zapier):**
```python
# Extract metadata dari file_name
input_data = input_data
file_name = input_data.get("file_name", "")

# Contoh format: "Laporan_Proyek_MusGo-OS_2026-05-19.pdf"
parts = file_name.replace(".", "_").split("_")
metadata = {
    "type": parts[0] if len(parts) > 0 else "Unknown",  # Laporan
    "project": parts[1] if len(parts) > 1 else "Unknown",  # Proyek
    "system": parts[2] if len(parts) > 2 else "Unknown",  # MusGo-OS
    "date": parts[3] if len(parts) > 3 else "Unknown",  # 2026-05-19
    "extension": parts[4] if len(parts) > 4 else "Unknown",  # pdf
}

# Output untuk step selanjutnya
output = {**input_data, **metadata}
```

---
#### **3. Code by Zapier: Panggil API MusGo-OS**
**Skenario:**
Code by Zapier **memanggil API MusGo-OS** untuk mendapatkan data tambahan.

**Contoh Kode (JavaScript):**
```javascript
// Input data
const inputData = inputData;
const fileUrl = inputData.file_url;
const fileName = inputData.file_name;

// Panggil API MusGo-OS untuk mendapatkan metadata
const response = await fetch("https://musgo-os.com/api/files/metadata", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_MUSGO_OS_API_KEY",
  },
  body: JSON.stringify({
    file_url: fileUrl,
    file_name: fileName,
  }),
});

const metadata = await response.json();

// Output untuk step selanjutnya
output = { ...inputData, ...metadata };
```

**Contoh Response dari MusGo-OS API:**
```json
{
  "file_name": "laporan_proyek.pdf",
  "file_size": 1024,
  "file_type": "pdf",
  "author": "Dhani Yuliawan",
  "created_at": "2026-05-19T10:00:00Z"
}
```

---
---
---

## **🔹 7.9 AI by Zapier (Integrasi AI)**
### **📌 Penjelasan**
**AI by Zapier** memungkinkan **menjalankan model AI** (seperti GPT-4, Claude, dll.) **di tengah workflow**. Contoh:
- **Trigger**: User mengirim pesan ke Slack.
- **Step 1**: AI by Zapier → **Analisis pesan** (sentiment, intent).
- **Step 2**: **Simpan hasil ke Notion**.

**Manfaat untuk MusGo-OS:**
- **Integrasi AI tanpa perlu AI Agent MusGo-OS**.
- **Workflow lebih cerdas** (bisa menganalisis data dengan AI).

---
### **🚀 Contoh Implementasi: AI by Zapier**
#### **Skenario:**
User MusGo-OS ingin **membuat Zap** yang:
1. **Trigger**: Slack → New Message in Channel (#musgo-feedback).
2. **Step 1**: AI by Zapier → **Analisis sentiment pesan**.
3. **Step 2**: Notion → **Simpan feedback ke database**.

**Arsitektur:**
```
Slack (Trigger) → AI by Zapier (Step 1) → Notion (Step 2)
```

---
#### **1. Workflow API: Zap dengan AI by Zapier**
**Contoh Kode (Python):**
```python
from zapier_workflow_api import ZapierWorkflowAPI

api = ZapierWorkflowAPI(api_key="YOUR_ZAPIER_API_KEY")

# Buat Zap dengan AI by Zapier
zap = api.create_zap(
    name="Slack → AI → Notion",
    steps=[
        # Trigger: Slack → New Message
        {
            "id": "trigger_1",
            "app": "slack",
            "action": "New Message in Channel",
            "data": {
                "channel": "#musgo-feedback",
            },
        },
        # Step 1: AI by Zapier → Analisis Sentiment
        {
            "id": "step_1",
            "app": "ai",
            "action": "Analyze Text",
            "data": {
                "model": "gpt-4",  # Atau "claude-3", dll.
                "prompt": "Analisis sentiment dari pesan berikut dan berikan skor (1-10) dan label (positive/neutral/negative):\n\nPesan: {text}",
                "temperature": 0.7,
            },
        },
        # Step 2: Notion → Simpan ke Database
        {
            "id": "step_2",
            "app": "notion",
            "action": "Create Database Row",
            "data": {
                "databaseId": "NOTION_DATABASE_ID",
                "properties": {
                    "Pesan": {"rich_text": [{"text": {"content": "{text}"}}]},
                    "User": {"rich_text": [{"text": {"content": "{user_name}"}}]},
                    "Sentiment": {"select": {"name": "{step_1_label}"}},
                    "Skor": {"number": float("{step_1_score}")},
                    "Waktu": {"date": {"start": "{timestamp}"}},
                },
            },
        },
    ]
)

print("✅ Zap dengan AI by Zapier dibuat:", zap)
```

**Contoh Output di Notion:**
| Pesan               | User          | Sentiment | Skor | Waktu               |
|--------------------|---------------|-----------|------|---------------------|
| "MusGo-OS sangat bagus!" | @dhani | Positive  | 9    | 19 Mei 2026, 10:00  |
| "Ada bug di fitur X" | @user1 | Negative  | 3    | 19 Mei 2026, 10:05  |

---
#### **2. AI by Zapier: Custom Prompt**
**Contoh Prompt untuk Extract Data:**
```python
{
  "model": "gpt-4",
  "prompt": """
  Extract data berikut dari pesan Slack:
  - Judul
  - Deskripsi
  - Prioritas (high/medium/low)
  - Deadline (jika ada)

  Pesan: {text}

  Format output sebagai JSON:
  {
    "judul": "...",
    "deskripsi": "...",
    "prioritas": "...",
    "deadline": "..."
  }
  """,
  "temperature": 0.3,
}
```

**Contoh Output:**
```json
{
  "judul": "Implementasi MCP",
  "deskripsi": "Integrasikan Zapier MCP ke MusGo-OS sebelum akhir bulan",
  "prioritas": "high",
  "deadline": "2026-05-31"
}
```

---
---
---

## **🔹 7.10 Best Practices untuk Advanced Use Cases**
### **📌 1. Modular Workflows (Workflow Terpisah)**
**Masalah:** Workflow yang terlalu panjang **sulit dikelola**.
**Solusi:** **Pecah workflow menjadi beberapa Zap terpisah** yang saling terhubung.

**Contoh:**
- **Zap 1**: Google Drive → AI Agent (Analisis File).
- **Zap 2**: AI Agent → Slack (Notifikasi).
- **Zap 3**: AI Agent → Notion (Simpan Hasil).

**Manfaat:**
- **Lebih mudah debug**.
- **Lebih fleksibel** (bisa menonaktifkan satu Zap tanpa mempengaruhi yang lain).

---
### **📌 2. Error Recovery (Pemulihan Error)**
**Masalah:** Jika workflow gagal, **data bisa hilang**.
**Solusi:** **Simpan data ke database sementara** sebelum diproses.

**Contoh Arsitektur:**
```
Trigger → [Simpan ke DB] → [Proses] → [Hapus dari DB]
```
- Jika **proses gagal**, data **tetap tersimpan di DB** dan bisa **diproses ulang**.

---
### **📌 3. Rate Limiting & Throttling**
**Masalah:** Terlalu banyak panggilan API **bisa melebihi rate limit**.
**Solusi:**
- **Gunakan queue** (antrian) untuk **membatasi panggilan**.
- **Gunakan delay** antara panggilan.

**Contoh (Python + PQueue):**
```python
from pqueue import PQueue
import time

# Queue dengan max 10 panggilan per menit
queue = PQueue(10)

def call_zapier_api():
    queue.put(1)  # Tambah ke queue
    try:
        # Panggil API
        time.sleep(6)  # Tunggu 6 detik (10 panggilan/menit)
    finally:
        queue.get()  # Hapus dari queue
```

---
### **📌 4. Logging & Monitoring**
**Masalah:** Sulit **debug workflow** jika tidak ada logging.
**Solusi:** **Catat semua aktivitas** (trigger, action, error).

**Contoh (Python + Logging):**
```python
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("zapier_workflows.log"),
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger("ZapierWorkflows")

# Contoh logging
logger.info("Trigger: Google Drive → New File (file: laporan.pdf)")
logger.info("Action: AI Agent → Analisis File (status: success)")
logger.error("Action: Slack → Kirim Notifikasi (status: failed, error: rate limit)")
```

---
### **📌 5. Testing & Validation**
**Masalah:** Workflow **bisa gagal di production** jika tidak ditest.
**Solusi:**
- **Test setiap step secara terpisah**.
- **Gunakan data dummy** untuk testing.

**Contoh (Python - Pytest):**
```python
import pytest
from zapier_workflow_api import ZapierWorkflowAPI

@pytest.fixture
def api():
    return ZapierWorkflowAPI(api_key="TEST_API_KEY")

def test_create_zap(api):
    """Test pembuatan Zap"""
    zap = api.create_zap(
        name="Test Zap",
        steps=[
            {"app": "google_drive", "action": "New File", "data": {}},
            {"app": "slack", "action": "Send Channel Message", "data": {"channel": "#test"}},
        ]
    )
    assert zap["name"] == "Test Zap"
    assert len(zap["steps"]) == 2

def test_run_action(api):
    """Test menjalankan action"""
    result = api.run_action(
        app="slack",
        action="Send Channel Message",
        data={"channel": "#test", "text": "Halo!"}
    )
    assert result["status"] == "success"
```

---
### **📌 6. Security (Keamanan)**
**Masalah:** Workflow bisa **disalahgunakan** jika tidak aman.
**Solusi:**
- **Gunakan autentikasi** (API Key, OAuth).
- **Validasi input** (jangan percaya data dari user).
- **Gunakan HTTPS** (untuk webhooks).

**Contoh (Python - Input Validation):**
```python
from pydantic import BaseModel, validator

class ZapRequest(BaseModel):
    name: str
    steps: list

    @validator("name")
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Nama Zap tidak boleh kosong")
        return v

    @validator("steps")
    def steps_must_have_at_least_2(cls, v):
        if len(v) < 2:
            raise ValueError("Zap harus memiliki minimal 2 step (1 trigger + 1 action)")
        return v
```

---
### **📌 7. Documentation (Dokumentasi)**
**Masalah:** Developer **sulit memahami workflow** jika tidak ada dokumentasi.
**Solusi:** **Dokumentasikan setiap workflow** (trigger, action, data flow).

**Contoh Dokumentasi (Markdown):**
```markdown
# Workflow: Google Drive → AI Agent → Slack → Notion

## Deskripsi
Workflow ini menganalisis file baru di Google Drive dengan AI Agent MusGo-OS, lalu mengirim notifikasi ke Slack dan menyimpan hasil ke Notion.

## Trigger
- **App**: Google Drive
- **Event**: New File in Folder
- **Data**:
  - `folder`: "Laporan"
  - `file_name`: Nama file
  - `file_url`: URL file

## Steps
1. **AI Agent (Webhooks)**
   - **URL**: `https://musgo-os.com/api/zapier/ai-analyze`
   - **Method**: POST
   - **Data**:
     - `file_url`: `{file_url}`
     - `file_name`: `{file_name}`
   - **Output**:
     - `summary`: Ringkasan file
     - `keywords`: Kata kunci

2. **Slack (Send Channel Message)**
   - **Channel**: `#musgo-reports`
   - **Text**:
     ```
     📄 File baru teranalisis!
     Nama: {file_name}
     Ringkasan: {summary}
     Keywords: {keywords}
     ```

3. **Notion (Create Database Row)**
   - **Database ID**: `NOTION_DATABASE_ID`
   - **Properties**:
     - `Nama File`: `{file_name}`
     - `Ringkasan`: `{summary}`
     - `Keywords`: `{keywords}`
     - `URL`: `{file_url}`

## Error Handling
- Jika AI Agent gagal, kirim notifikasi error ke `#musgo-errors`.
- Retry 3 kali sebelum gagal total.

## Rate Limiting
- Maksimal 10 panggilan API per menit.
```

---
---
---
# **📌 PART 7: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 7 (Advanced Use Cases)**
| Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|-------|------------------------|----------------------|
| **Multi-Step Zaps** | Workflow dengan 2+ langkah | ✅ **Contoh kode tersedia** |
| **Conditional Logic** | Jalankan langkah berdasarkan kondisi | ✅ **Contoh kode tersedia** |
| **Error Handling** | Tangani error dengan baik | ✅ **Contoh kode tersedia** |
| **Delayed Actions** | Tunda eksekusi workflow | ✅ **Contoh kode tersedia** |
| **Paths** | Pilih rute berdasarkan data | ✅ **Contoh kode tersedia** |
| **Formatter** | Format data sebelum dikirim | ✅ **Contoh kode tersedia** |
| **Webhooks** | Integrasi dengan API eksternal | ✅ **Contoh kode tersedia** |
| **Code by Zapier** | Jalankan kode kustom | ✅ **Contoh kode tersedia** |
| **AI by Zapier** | Integrasi AI di workflow | ✅ **Contoh kode tersedia** |
| **Best Practices** | Modular, Security, Logging, dll. | ✅ **Panduan tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Implementasikan Multi-Step Zaps** (gunakan contoh kode di atas).
- [ ] **Test Conditional Logic** (filter, paths).
- [ ] **Setup Error Handling** (retry, fallback, notifikasi error).
- [ ] **Test Webhooks** (incoming & outgoing).

### **2. Mid-Term (1 Bulan)**
- [ ] **Integrasikan AI by Zapier** (untuk analisis otomatis).
- [ ] **Implementasikan Code by Zapier** (untuk logika kustom).
- [ ] **Buat dokumentasi workflow** (untuk developer).
- [ ] **Setup logging & monitoring** (untuk debugging).

### **3. Long-Term (3+ Bulan)**
- [ ] **Optimalkan performa workflow** (queue, caching, dll.).
- [ ] **Luncurkan fitur advanced workflow** ke user MusGo-OS.
- [ ] **Monitor penggunaan API** (untuk menghindari rate limit).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 8: Security & Compliance** (Untuk keamanan Workflow API)
   - [ ] **Part 9: Deployment & Scaling** (Untuk deployment MusGo-OS + Zapier)
   - [ ] **Part 10: Monitoring & Analytics** (Untuk pemantauan workflow)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi Google Drive + Notion + Slack + AI Agent)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi lengkap untuk MusGo-OS + Zapier**?
   - [ ] **Contoh deployment (Docker, Kubernetes, CI/CD)**?

3. **Apakah ada use-case spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **MusGo-OS → AI Agent → Slack → Notion → Google Sheets**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 8: Security & Compliance** — kita akan **menerjemahkan, menerapkan, dan memberikan contoh implementasi keamanan dan kepatuhan** untuk integrasi **MusGo-OS 2in1** dengan **Zapier**, dengan fokus pada **Zero Trust, OAuth 2.0, JWT, Rate Limiting, dan Audit Logging**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN SECURITY & COMPLIANCE (PART 8)**
*Terjemahan + Implementasi untuk Keamanan Integrasi Zapier*

---

---

## **🔹 8.1 Overview Security & Compliance**
### **📌 Penjelasan (Bahasa Indonesia)**
**Security & Compliance** adalah **fondasi kritikal** untuk integrasi **MusGo-OS + Zapier**, terutama karena:
- **MusGo-OS adalah AI-native OS** yang menangani **data sensitif** (user data, AI prompts, dll.).
- **Zapier terhubung ke 9,000+ aplikasi**, sehingga **risiko keamanan tinggi** (misal: data leakage, unauthorized access).
- **Kepatuhan (Compliance)** diperlukan untuk **GDPR, SOC 2, ISO 27001**, dll.

**Prinsip Keamanan untuk MusGo-OS:**
1. **Zero Trust**: Tidak percaya siapa pun (bahkan internal services).
2. **Least Privilege**: Berikan akses **minimal** yang diperlukan.
3. **Defense in Depth**: Lapisan keamanan **multi-layer** (autentikasi, otorisasi, enkripsi).
4. **Immutable Audit Logs**: Catat **semua aktivitas** dan **tidak bisa diubah**.
5. **Replay-Safe**: Hindari **replay attacks** (serangan ulang dengan token yang sama).

---

### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: Zero Trust Architecture**
**Skenario:**
MusGo-OS ingin **menerapkan Zero Trust** untuk integrasi Zapier, sehingga:
- **Setiap panggilan API** harus **divalidasi**.
- **Setiap service** (AI Agent, Backend, Frontend) **harus saling autentikasi**.
- **Token** harus **short-lived** dan **dirotate secara otomatis**.

**Arsitektur:**
```
User → [Auth] → MusGo-OS Frontend → [mTLS] → MusGo-OS Backend → [JWT] → Zapier API
```

---
---
---

## **🔹 8.2 Authentication (Autentikasi)**
### **📌 1. OAuth 2.0 (Untuk User)**
**Penjelasan:**
OAuth 2.0 adalah **standar autentikasi** yang memungkinkan **user MusGo-OS** untuk **menghubungkan akun mereka** (Slack, Google Drive, dll.) **ke Zapier** tanpa **membagikan password**.

**Manfaat untuk MusGo-OS:**
- **User tidak perlu share password**.
- **MusGo-OS bisa mengakses data user** (dengan izin).
- **Token bisa dicabut kapan saja**.

---
#### **🚀 Contoh Implementasi: OAuth 2.0 Flow**
##### **1. OAuth 2.0 Authorization Code Flow**
**Cara Kerja:**
1. **User klik "Hubungkan Slack"** di MusGo-OS.
2. **MusGo-OS redirect user** ke **Zapier OAuth URL**.
3. **User login ke Slack** (via Zapier).
4. **Zapier redirect kembali** ke MusGo-OS dengan **authorization code**.
5. **MusGo-OS exchange code** untuk **access token + refresh token**.

**Arsitektur:**
```
User → MusGo-OS Frontend → Zapier OAuth → Slack Login → Zapier Redirect → MusGo-OS Backend → Exchange Code → Get Token
```

---
##### **2. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import httpx
import secrets
import time
from typing import Optional, Dict
from datetime import datetime, timedelta

app = FastAPI()

# Dummy database untuk OAuth
oauth_clients = {
    "ZAPIER_CLIENT_ID": {
        "client_secret": "ZAPIER_CLIENT_SECRET",
        "redirect_uri": "https://musgo-os.com/oauth/callback",
    }
}

oauth_tokens: Dict[str, Dict[str, Any]] = {}  # {user_id: {access_token, refresh_token, expires_at}}
oauth_states: Dict[str, str] = {}  # {state: user_id}

# Model untuk OAuth
class OAuthTokenRequest(BaseModel):
    code: str
    state: str

class OAuthTokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
    refresh_token: Optional[str] = None
    scope: str

# 1. Redirect user ke Zapier OAuth
@app.get("/oauth/authorize")
async def oauth_authorize(
    response_type: str = "code",
    client_id: str = None,
    redirect_uri: str = None,
    scope: str = "read write",
    state: Optional[str] = None,
    user_id: Optional[str] = None,
):
    """Redirect user ke Zapier untuk autentikasi"""
    if response_type != "code":
        raise HTTPException(status_code=400, detail="Unsupported response_type")

    if client_id not in oauth_clients:
        raise HTTPException(status_code=400, detail="Invalid client_id")

    if oauth_clients[client_id]["redirect_uri"] != redirect_uri:
        raise HTTPException(status_code=400, detail="Invalid redirect_uri")

    # Generate state (untuk CSRF protection)
    state = state or secrets.token_urlsafe(16)
    if user_id:
        oauth_states[state] = user_id

    # Redirect ke Zapier OAuth
    zapier_oauth_url = (
        f"https://zapier.com/oauth/authorize?"
        f"response_type=code&"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"scope={scope}&"
        f"state={state}"
    )
    return RedirectResponse(url=zapier_oauth_url)

# 2. Handle OAuth callback
@app.get("/oauth/callback")
async def oauth_callback(
    code: str,
    state: str,
    error: Optional[str] = None,
    error_description: Optional[str] = None,
):
    """Handle callback dari Zapier OAuth"""
    if error:
        raise HTTPException(status_code=400, detail=f"OAuth Error: {error} - {error_description}")

    if state not in oauth_states:
        raise HTTPException(status_code=400, detail="Invalid state")

    user_id = oauth_states.pop(state)
    client_id = "ZAPIER_CLIENT_ID"  # Atau ambil dari config

    # Exchange code untuk token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://zapier.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": oauth_clients[client_id]["redirect_uri"],
                "client_id": client_id,
                "client_secret": oauth_clients[client_id]["client_secret"],
            },
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to exchange code for token")

        token_data = response.json()
        access_token = token_data["access_token"]
        refresh_token = token_data.get("refresh_token")
        expires_in = token_data["expires_in"]
        scope = token_data.get("scope", "")

        # Simpan token untuk user
        oauth_tokens[user_id] = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": datetime.now() + timedelta(seconds=expires_in),
            "scope": scope,
        }

        # Redirect ke halaman asli (misal: dashboard)
        return RedirectResponse(url=f"https://musgo-os.com/dashboard?user_id={user_id}")

# 3. Refresh Token (jika access token kadaluarsa)
@app.post("/oauth/refresh")
async def oauth_refresh(
    user_id: str,
    client_id: str = "ZAPIER_CLIENT_ID",
):
    """Refresh access token"""
    if user_id not in oauth_tokens:
        raise HTTPException(status_code=404, detail="User not found")

    token_data = oauth_tokens[user_id]
    if datetime.now() < token_data["expires_at"]:
        return OAuthTokenResponse(
            access_token=token_data["access_token"],
            expires_in=int((token_data["expires_at"] - datetime.now()).total_seconds()),
            refresh_token=token_data.get("refresh_token"),
            scope=token_data.get("scope", ""),
        )

    # Refresh token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://zapier.com/oauth/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": token_data["refresh_token"],
                "client_id": client_id,
                "client_secret": oauth_clients[client_id]["client_secret"],
            },
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to refresh token")

        new_token_data = response.json()
        oauth_tokens[user_id] = {
            "access_token": new_token_data["access_token"],
            "refresh_token": new_token_data.get("refresh_token", token_data["refresh_token"]),
            "expires_at": datetime.now() + timedelta(seconds=new_token_data["expires_in"]),
            "scope": new_token_data.get("scope", token_data.get("scope", "")),
        }

        return OAuthTokenResponse(
            access_token=new_token_data["access_token"],
            expires_in=new_token_data["expires_in"],
            refresh_token=new_token_data.get("refresh_token"),
            scope=new_token_data.get("scope", ""),
        )

# 4. Get Token (untuk internal use)
def get_user_token(user_id: str) -> Optional[str]:
    """Ambil access token user (auto-refresh jika kadaluarsa)"""
    if user_id not in oauth_tokens:
        return None

    token_data = oauth_tokens[user_id]
    if datetime.now() >= token_data["expires_at"]:
        # Refresh token
        try:
            new_token = oauth_refresh(user_id)
            token_data["access_token"] = new_token.access_token
            token_data["expires_at"] = datetime.now() + timedelta(seconds=new_token.expires_in)
        except:
            return None

    return token_data["access_token"]
```

---
##### **3. Frontend MusGo-OS (React + TypeScript)**
**Contoh UI untuk OAuth Flow:**
```tsx
// File: src/components/ConnectAppButton.tsx
import React from "react";

interface ConnectAppButtonProps {
  app: string;
  userId: string;
  onConnected: () => void;
}

const ConnectAppButton: React.FC<ConnectAppButtonProps> = ({
  app,
  userId,
  onConnected,
}) => {
  const handleConnect = () => {
    // Buka popup untuk OAuth flow
    const width = 600;
    const height = 600;
    const left = (window.innerWidth - width) / 2;
    const top = (window.innerHeight - height) / 2;

    const popup = window.open(
      `https://musgo-os.com/oauth/authorize?client_id=ZAPIER_CLIENT_ID&redirect_uri=${encodeURIComponent("https://musgo-os.com/oauth/callback")}&scope=read%20write&state=${userId}`,
      "ZapierOAuth",
      `width=${width},height=${height},top=${top},left=${left}`
    );

    // Cek popup setiap 500ms
    const checkPopup = setInterval(() => {
      if (popup?.closed) {
        clearInterval(checkPopup);
        onConnected();
      }
    }, 500);
  };

  return (
    <button
      onClick={handleConnect}
      style={{
        padding: "10px 20px",
        background: "#4285F4",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
      }}
    >
      Hubungkan {app}
    </button>
  );
};

export default ConnectAppButton;
```

---
---
---

## **🔹 8.3 Authorization (Otorisasi)**
### **📌 1. Role-Based Access Control (RBAC)**
**Penjelasan:**
RBAC memungkinkan **MusGo-OS** untuk **mengontrol akses user** berdasarkan **role** (misal: admin, user, guest).

**Manfaat untuk MusGo-OS:**
- **Admin** bisa **mengelola semua Zap**.
- **User** hanya bisa **mengelola Zap miliknya**.
- **Guest** hanya bisa **melihat Zap**.

---
#### **🚀 Contoh Implementasi: RBAC**
##### **1. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI()
security = HTTPBearer()

# Role definitions
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

# User database (contoh)
users_db = {
    "USER_ID_123": {
        "email": "dhani@musgo-os.com",
        "role": Role.ADMIN,
        "zaps": ["ZAP_ID_1", "ZAP_ID_2"],
    },
    "USER_ID_456": {
        "email": "user@musgo-os.com",
        "role": Role.USER,
        "zaps": ["ZAP_ID_3"],
    },
    "USER_ID_789": {
        "email": "guest@musgo-os.com",
        "role": Role.GUEST,
        "zaps": [],
    },
}

# Permission definitions
PERMISSIONS = {
    Role.ADMIN: ["create_zap", "read_zap", "update_zap", "delete_zap", "manage_users"],
    Role.USER: ["create_zap", "read_zap", "update_zap", "delete_zap"],
    Role.GUEST: ["read_zap"],
}

# Dependency untuk mendapatkan user
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """Ambil user dari token JWT"""
    # Di sini seharusnya decode JWT, tapi kita simulasikan
    user_id = credentials.credentials  # Asumsikan credentials adalah user_id
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Dependency untuk cek permission
async def check_permission(permission: str, user: dict = Depends(get_current_user)):
    """Cek apakah user memiliki permission"""
    if permission not in PERMISSIONS[user["role"]]:
        raise HTTPException(status_code=403, detail="Permission denied")
    return True

# Model untuk Zap
class Zap(BaseModel):
    id: str
    name: str
    user_id: str
    status: str = "on"

# 1. Buat Zap (hanya ADMIN dan USER)
@app.post("/api/zaps")
async def create_zap(
    zap: Zap,
    user: dict = Depends(get_current_user),
    _: bool = Depends(lambda: check_permission("create_zap")),
):
    """Buat Zap baru"""
    if user["role"] == Role.USER and zap.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="User hanya bisa membuat Zap untuk dirinya sendiri")

    # Simpan Zap (contoh)
    zap.id = f"ZAP_ID_{len(users_db) + 1}"
    users_db[user["id"]]["zaps"].append(zap.id)
    return zap

# 2. Daftar Zap (ADMIN: semua Zap, USER: Zap miliknya, GUEST: tidak bisa)
@app.get("/api/zaps")
async def list_zaps(
    user: dict = Depends(get_current_user),
    _: bool = Depends(lambda: check_permission("read_zap")),
):
    """Daftar Zap"""
    if user["role"] == Role.ADMIN:
        # Ambil semua Zap
        all_zaps = []
        for user_data in users_db.values():
            for zap_id in user_data["zaps"]:
                all_zaps.append({"id": zap_id, "user_id": user_data["email"]})
        return all_zaps
    elif user["role"] == Role.USER:
        # Ambil Zap milik user
        return [{"id": zap_id, "user_id": user["email"]} for zap_id in user["zaps"]]
    else:
        raise HTTPException(status_code=403, detail="Guest tidak bisa mendaftar Zap")

# 3. Hapus Zap (hanya ADMIN dan USER pemilik)
@app.delete("/api/zaps/{zap_id}")
async def delete_zap(
    zap_id: str,
    user: dict = Depends(get_current_user),
    _: bool = Depends(lambda: check_permission("delete_zap")),
):
    """Hapus Zap"""
    if user["role"] == Role.USER and zap_id not in user["zaps"]:
        raise HTTPException(status_code=403, detail="User hanya bisa menghapus Zap miliknya")

    # Hapus Zap (contoh)
    for user_data in users_db.values():
        if zap_id in user_data["zaps"]:
            user_data["zaps"].remove(zap_id)
            return {"status": "success", "message": f"Zap {zap_id} dihapus"}
    raise HTTPException(status_code=404, detail="Zap not found")
```

---
##### **2. Frontend MusGo-OS (React + RBAC)**
**Contoh UI dengan RBAC:**
```tsx
// File: src/components/ZapList.tsx
import React, { useState, useEffect } from "react";
import { Role } from "../types/auth";

interface Zap {
  id: string;
  name: string;
  user_id: string;
}

interface ZapListProps {
  userRole: Role;
  userId: string;
}

const ZapList: React.FC<ZapListProps> = ({ userRole, userId }) => {
  const [zaps, setZaps] = useState<Zap[]>([]);
  const [loading, setLoading] = useState(true);

  // Ambil daftar Zap
  useEffect(() => {
    const fetchZaps = async () => {
      try {
        const response = await fetch("https://musgo-os.com/api/zaps", {
          headers: {
            "Authorization": `Bearer ${userId}`,  // Asumsikan userId adalah token
          },
        });
        if (response.ok) {
          const data = await response.json();
          setZaps(data);
        }
      } catch (error) {
        console.error("Gagal mengambil Zap:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchZaps();
  }, [userId]);

  // Hapus Zap
  const handleDeleteZap = async (zapId: string) => {
    if (userRole !== "admin" && userRole !== "user") {
      alert("Anda tidak memiliki izin untuk menghapus Zap");
      return;
    }

    try {
      const response = await fetch(`https://musgo-os.com/api/zaps/${zapId}`, {
        method: "DELETE",
        headers: {
          "Authorization": `Bearer ${userId}`,
        },
      });
      if (response.ok) {
        setZaps(zaps.filter((zap) => zap.id !== zapId));
        alert("Zap berhasil dihapus");
      } else {
        alert("Gagal menghapus Zap");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Terjadi kesalahan");
    }
  };

  if (loading) {
    return <p>Memuat daftar Zap...</p>;
  }

  return (
    <div>
      <h2>Daftar Zap</h2>
      {zaps.length === 0 ? (
        <p>Tidak ada Zap.</p>
      ) : (
        <ul>
          {zaps.map((zap) => (
            <li key={zap.id}>
              {zap.name || zap.id} (User: {zap.user_id})
              {(userRole === "admin" || zap.user_id === userId) && (
                <button
                  onClick={() => handleDeleteZap(zap.id)}
                  style={{ marginLeft: "10px", color: "red" }}
                >
                  Hapus
                </button>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ZapList;
```

---
---
---

## **🔹 8.4 JWT (JSON Web Token)**
### **📌 Penjelasan**
**JWT** adalah **standar untuk token autentikasi** yang **self-contained** (mengandung data user) dan **signed** (tidak bisa diubah). Digunakan untuk:
- **Autentikasi API** (misal: MusGo-OS → Zapier).
- **Autentikasi internal** (misal: Frontend → Backend).

**Struktur JWT:**
```
Header.Payload.Signature
```
- **Header**: Algoritma (misal: `HS256`, `RS256`).
- **Payload**: Data (misal: `user_id`, `role`, `exp`).
- **Signature**: Tanda tangan (untuk validasi).

---
#### **🚀 Contoh Implementasi: JWT**
##### **1. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from typing import Optional, Dict
import secrets

app = FastAPI()
security = HTTPBearer()

# Secret key untuk JWT (ganti dengan private key asli)
SECRET_KEY = secrets.token_urlsafe(32)  # 32 bytes
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Dummy user database
users_db = {
    "dhani@musgo-os.com": {
        "password": "hashed_password_123",  # Seharusnya di-hash
        "role": "admin",
        "disabled": False,
    },
}

# Model untuk JWT
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None

# 1. Login (dapatkan JWT)
@app.post("/token", response_model=Token)
async def login_for_access_token(email: str, password: str):
    """Login dan dapatkan JWT"""
    user = users_db.get(email)
    if not user or user["password"] != password:
        raise HTTPException(
            status_code=401,
            detail="Email atau password salah",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": email, "role": user["role"]},
        expires_delta=access_token_expires - datetime.utcnow(),
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 2. Buat JWT
def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None):
    """Buat JWT"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 3. Dependency untuk mendapatkan user dari JWT
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    """Decode JWT dan ambil user"""
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return {"email": email, "role": payload.get("role")}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token kadaluarsa")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token tidak valid")

# 4. Dependency untuk cek role
async def get_current_active_user(current_user: Dict[str, Any] = Depends(get_current_user)):
    """Cek apakah user aktif"""
    if current_user["email"] not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[current_user["email"]]
    if user.get("disabled", False):
        raise HTTPException(status_code=400, detail="User dinonaktifkan")
    return current_user

# 5. Protected endpoint (contoh)
@app.get("/users/me")
async def read_users_me(current_user: Dict[str, Any] = Depends(get_current_active_user)):
    """Endpoint yang memerlukan JWT"""
    return current_user
```

---
##### **2. Frontend MusGo-OS (React + JWT)**
**Contoh Login dan Simpan Token:**
```tsx
// File: src/components/LoginForm.tsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await fetch("https://musgo-os.com/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          email,
          password,
        }).toString(),
      });

      if (!response.ok) {
        throw new Error("Login gagal");
      }

      const data = await response.json();
      // Simpan token ke localStorage
      localStorage.setItem("access_token", data.access_token);
      localStorage.setItem("token_type", data.token_type);

      // Redirect ke dashboard
      navigate("/dashboard");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Login ke MusGo-OS</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div>
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
```

**Contoh Penggunaan Token di Request:**
```tsx
// File: src/api/zapier.ts
export const fetchZaps = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) {
    throw new Error("Token tidak ditemukan");
  }

  const response = await fetch("https://musgo-os.com/api/zaps", {
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    if (response.status === 401) {
      // Token kadaluarsa, redirect ke login
      window.location.href = "/login";
    }
    throw new Error("Gagal mengambil Zap");
  }

  return response.json();
};
```

---
---
---

## **🔹 8.5 mTLS (Mutual TLS)**
### **📌 Penjelasan**
**mTLS** adalah **autentikasi dua arah** di mana **client dan server saling autentikasi** menggunakan **sertifikat TLS**. Digunakan untuk:
- **Service-to-Service Authentication** (misal: MusGo-OS Backend → Zapier API).
- **Zero Trust Networking** (tidak percaya jaringan internal).

**Manfaat untuk MusGo-OS:**
- **Hanya service yang terverifikasi** yang bisa berkomunikasi.
- **Mencegah man-in-the-middle attacks**.

---
#### **🚀 Contoh Implementasi: mTLS**
##### **1. Generate Sertifikat (Self-Signed untuk Testing)**
```bash
# Generate CA (Certificate Authority)
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt -subj "/CN=MusGo-OS CA"

# Generate sertifikat untuk MusGo-OS Backend
openssl genrsa -out musgo-backend.key 2048
openssl req -new -key musgo-backend.key -out musgo-backend.csr -subj "/CN=musgo-backend"
openssl x509 -req -in musgo-backend.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out musgo-backend.crt -days 365

# Generate sertifikat untuk Zapier Client
openssl genrsa -out zapier-client.key 2048
openssl req -new -key zapier-client.key -out zapier-client.csr -subj "/CN=zapier-client"
openssl x509 -req -in zapier-client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out zapier-client.crt -days 365
```

---
##### **2. Backend MusGo-OS (Python - FastAPI + mTLS)**
```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.security import HTTPBearer
import ssl
import httpx
from typing import Optional

app = FastAPI()

# Path ke sertifikat
CERTFILE = "musgo-backend.crt"
KEYFILE = "musgo-backend.key"
CAFILE = "ca.crt"

# Konfigurasi SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
ssl_context.load_verify_locations(cafile=CAFILE)
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Dependency untuk mTLS
async def verify_mtls(request: Request):
    """Verifikasi sertifikat client"""
    if not request.client:
        raise HTTPException(status_code=403, detail="mTLS diperlukan")

    # Cek sertifikat client
    cert = request.client.cert
    if not cert:
        raise HTTPException(status_code=403, detail="Sertifikat client tidak valid")

    # Cek Common Name (CN)
    cn = cert.get("subject", {}).get("commonName", [])
    if not cn or "zapier-client" not in cn[0]:
        raise HTTPException(status_code=403, detail="Sertifikat client tidak dikenal")

    return True

# Protected endpoint (memerlukan mTLS)
@app.get("/api/secure")
async def secure_endpoint(_: bool = Depends(verify_mtls)):
    """Endpoint yang memerlukan mTLS"""
    return {"message": "Akses diizinkan! Anda terautentikasi dengan mTLS."}

# Contoh: Panggil Zapier API dengan mTLS
@app.get("/api/zapier/secure")
async def call_zapier_secure():
    """Panggil Zapier API dengan mTLS"""
    client_cert = ("zapier-client.crt", "zapier-client.key")
    ca_cert = "ca.crt"

    async with httpx.AsyncClient(
        cert=client_cert,
        verify=ca_cert,
    ) as client:
        response = await client.get("https://zapier.com/api/v2/secure-endpoint")
        return response.json()
```

---
##### **3. Konfigurasi Nginx untuk mTLS**
**Contoh Konfigurasi Nginx:**
```nginx
server {
    listen 443 ssl;
    server_name musgo-os.com;

    # Sertifikat server
    ssl_certificate     /path/to/musgo-backend.crt;
    ssl_certificate_key /path/to/musgo-backend.key;

    # CA untuk verifikasi client
    ssl_client_certificate /path/to/ca.crt;
    ssl_verify_client on;
    ssl_verify_depth 2;

    location /api/secure {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---
---
---

## **🔹 8.6 Rate Limiting & Throttling**
### **📌 Penjelasan**
**Rate Limiting** adalah **pembatasan jumlah panggilan API** per **waktu tertentu** (misal: 100 panggilan/menit). Digunakan untuk:
- **Mencegah abuse** (serangan DDoS, brute force).
- **Mematuhi batas Zapier** (misal: 60 panggilan/menit untuk akun gratis).
- **Mengoptimalkan penggunaan resource**.

**Manfaat untuk MusGo-OS:**
- **Hindari melebihi kuota Zapier**.
- **Lindungi API MusGo-OS** dari abuse.

---
#### **🚀 Contoh Implementasi: Rate Limiting**
##### **1. Backend MusGo-OS (Python - FastAPI + Redis)**
```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import redis.asyncio as redis
from typing import Optional

app = FastAPI()

# Setup Redis untuk rate limiting
redis_client = redis.from_url("redis://localhost:6379")

# Setup Limiter
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379",
    enabled=True,
)

# Middleware untuk rate limiting
app.state.limiter = limiter
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# 1. Rate limiting untuk semua endpoint (global)
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Middleware untuk rate limiting global"""
    try:
        return await call_next(request)
    except RateLimitExceeded:
        return JSONResponse(
            status_code=429,
            content={"detail": "Terlalu banyak permintaan. Silakan coba lagi nanti."},
        )

# 2. Rate limiting per endpoint
@app.get("/api/zaps")
@limiter.limit("100/minute")  # 100 panggilan per menit
async def list_zaps(request: Request):
    """Daftar Zap (dengan rate limiting)"""
    return {"zaps": ["ZAP_1", "ZAP_2"]}

# 3. Rate limiting per user (menggunakan user_id)
@app.get("/api/user/zaps")
@limiter.limit("60/minute", key_func=lambda request: request.headers.get("X-User-ID"))
async def list_user_zaps(request: Request):
    """Daftar Zap user (dengan rate limiting per user)"""
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        raise HTTPException(status_code=400, detail="X-User-ID diperlukan")
    return {"user_zaps": ["ZAP_1", "ZAP_2"]}

# 4. Rate limiting untuk Zapier API calls
from zapier_workflow_api import ZapierWorkflowAPI
import time

class RateLimitedZapierAPI:
    def __init__(self, api_key: str, max_requests: int = 60, window: int = 60):
        self.api = ZapierWorkflowAPI(api_key)
        self.max_requests = max_requests
        self.window = window  # dalam detik
        self.requests = []  # timestamp dari request

    def _check_rate_limit(self):
        """Cek apakah melebihi rate limit"""
        now = time.time()
        # Hapus request yang sudah kadaluarsa
        self.requests = [t for t in self.requests if now - t < self.window]
        if len(self.requests) >= self.max_requests:
            raise RateLimitExceeded("Rate limit exceeded")
        self.requests.append(now)

    def run_action(self, app: str, action: str, data: dict):
        """Jalankan action dengan rate limiting"""
        self._check_rate_limit()
        return self.api.run_action(app, action, data)

# Contoh penggunaan
rate_limited_api = RateLimitedZapierAPI(api_key="YOUR_ZAPIER_API_KEY")
try:
    result = rate_limited_api.run_action("slack", "Send Channel Message", {"channel": "#test", "text": "Halo!"})
    print("Action berjalan:", result)
except RateLimitExceeded:
    print("Rate limit exceeded. Tunggu sebentar...")
```

---
##### **2. Frontend MusGo-OS (React + Rate Limiting)**
**Contoh UI untuk Rate Limiting:**
```tsx
// File: src/components/RateLimitWarning.tsx
import React, { useState, useEffect } from "react";

interface RateLimitWarningProps {
  remainingRequests: number;
  resetIn: number; // dalam detik
}

const RateLimitWarning: React.FC<RateLimitWarningProps> = ({
  remainingRequests,
  resetIn,
}) => {
  const [timeLeft, setTimeLeft] = useState(resetIn);

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);

    return () => clearInterval(timer);
  }, [resetIn]);

  if (remainingRequests > 0) {
    return null;
  }

  return (
    <div style={{
      padding: "10px",
      background: "#fff3cd",
      border: "1px solid #ffc107",
      borderRadius: "5px",
      margin: "10px 0",
      color: "#856404",
    }}>
      ⚠️ Anda telah mencapai batas permintaan. Silakan tunggu {timeLeft} detik lagi.
    </div>
  );
};

export default RateLimitWarning;
```

**Contoh Penggunaan di API Call:**
```tsx
// File: src/api/zapier.ts
import { fetchWithRateLimit } from "./rateLimit";

export const fetchZaps = async () => {
  try {
    const response = await fetchWithRateLimit("https://musgo-os.com/api/zaps");
    return response.json();
  } catch (error) {
    if (error.message.includes("429")) {
      // Tampilkan warning rate limit
      return { error: "rate_limit", resetIn: 60 };
    }
    throw error;
  }
};
```

---
---
---

## **🔹 8.7 Audit Logging (Pencatatan Audit)**
### **📌 Penjelasan**
**Audit Logging** adalah **pencatatan semua aktivitas** (login, panggilan API, perubahan data) untuk:
- **Keamanan**: Deteksi **intrusi** atau **abuse**.
- **Kepatuhan**: Memenuhi **GDPR, SOC 2, ISO 27001**.
- **Debugging**: Lacak **masalah** atau **error**.

**Manfaat untuk MusGo-OS:**
- **Tahu siapa yang melakukan apa dan kapan**.
- **Bisa melacak aktivitas mencurigakan**.
- **Bukti untuk investigasi**.

---
#### **🚀 Contoh Implementasi: Audit Logging**
##### **1. Backend MusGo-OS (Python - FastAPI + Logging)**
```python
from fastapi import FastAPI, Request, Depends
from fastapi.security import HTTPBearer
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import json
from typing import Dict, Any

app = FastAPI()
security = HTTPBearer()

# Setup audit logging
audit_logger = logging.getLogger("audit")
audit_logger.setLevel(logging.INFO)

# Handler untuk audit log (simpan ke file, rotasi setiap 10MB)
audit_handler = RotatingFileHandler(
    "audit.log",
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,
)
audit_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
audit_logger.addHandler(audit_handler)

# Dependency untuk audit logging
async def audit_log(
    request: Request,
    action: str,
    user_id: Optional[str] = None,
    data: Optional[Dict[str, Any]] = None,
    status: str = "success",
    error: Optional[str] = None,
):
    """Catat aktivitas ke audit log"""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "user_id": user_id,
        "path": request.url.path,
        "method": request.method,
        "ip": request.client.host if request.client else None,
        "user_agent": request.headers.get("user-agent"),
        "data": data,
        "status": status,
        "error": error,
    }
    audit_logger.info(json.dumps(log_entry))

# Middleware untuk audit logging
@app.middleware("http")
async def audit_middleware(request: Request, call_next):
    """Middleware untuk audit logging"""
    try:
        response = await call_next(request)
    except Exception as e:
        await audit_log(
            request,
            action="request",
            user_id=request.headers.get("X-User-ID"),
            data={"path": request.url.path, "method": request.method},
            status="error",
            error=str(e),
        )
        raise
    else:
        await audit_log(
            request,
            action="request",
            user_id=request.headers.get("X-User-ID"),
            data={"path": request.url.path, "method": request.method},
            status="success",
            error=None,
        )
    return response

# Contoh: Audit logging untuk login
@app.post("/token")
async def login_for_access_token(
    email: str,
    password: str,
    request: Request,
):
    """Login dan catat ke audit log"""
    try:
        # ... (kode login)
        await audit_log(
            request,
            action="login",
            user_id=email,
            data={"email": email},
            status="success",
        )
        return {"access_token": "..."}
    except Exception as e:
        await audit_log(
            request,
            action="login",
            user_id=email,
            data={"email": email},
            status="failed",
            error=str(e),
        )
        raise

# Contoh: Audit logging untuk Zap creation
@app.post("/api/zaps")
async def create_zap(
    zap: Dict[str, Any],
    request: Request,
    user: Dict[str, Any] = Depends(get_current_user),
):
    """Buat Zap dan catat ke audit log"""
    try:
        # ... (kode buat Zap)
        await audit_log(
            request,
            action="create_zap",
            user_id=user["email"],
            data={"zap_id": zap["id"], "zap_name": zap["name"]},
            status="success",
        )
        return zap
    except Exception as e:
        await audit_log(
            request,
            action="create_zap",
            user_id=user["email"],
            data={"zap_name": zap.get("name")},
            status="failed",
            error=str(e),
        )
        raise
```

---
##### **2. Audit Log Format (JSON)**
**Contoh Log Entry:**
```json
{
  "timestamp": "2026-05-19T10:00:00.123456Z",
  "action": "create_zap",
  "user_id": "dhani@musgo-os.com",
  "path": "/api/zaps",
  "method": "POST",
  "ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
  "data": {
    "zap_id": "ZAP_ID_123",
    "zap_name": "Google Drive → Slack"
  },
  "status": "success",
  "error": null
}
```

---
##### **3. Audit Log Analysis (Analisis Log)**
**Contoh Skrip Python untuk Analisis Log:**
```python
import json
import re
from collections import defaultdict
from datetime import datetime

# Baca audit log
def read_audit_log(file_path: str):
    with open(file_path, "r") as f:
        for line in f:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue

# Analisis log
def analyze_audit_log(file_path: str):
    logs = list(read_audit_log(file_path))

    # Statistik
    stats = {
        "total_requests": len(logs),
        "success": 0,
        "failed": 0,
        "actions": defaultdict(int),
        "users": defaultdict(int),
        "ips": defaultdict(int),
    }

    for log in logs:
        stats["success" if log["status"] == "success" else "failed"] += 1
        stats["actions"][log["action"]] += 1
        if log["user_id"]:
            stats["users"][log["user_id"]] += 1
        if log["ip"]:
            stats["ips"][log["ip"]] += 1

    return stats

# Contoh penggunaan
stats = analyze_audit_log("audit.log")
print("Statistik Audit Log:")
print(f"- Total Requests: {stats['total_requests']}")
print(f"- Success: {stats['success']}")
print(f"- Failed: {stats['failed']}")
print(f"- Actions: {dict(stats['actions'])}")
print(f"- Top Users: {sorted(stats['users'].items(), key=lambda x: x[1], reverse=True)[:5]}")
print(f"- Top IPs: {sorted(stats['ips'].items(), key=lambda x: x[1], reverse=True)[:5]}")
```

**Output:**
```
Statistik Audit Log:
- Total Requests: 1000
- Success: 950
- Failed: 50
- Actions: {'login': 200, 'create_zap': 300, 'run_zap': 400, 'delete_zap': 100}
- Top Users: [('dhani@musgo-os.com', 500), ('user1@musgo-os.com', 300), ...]
- Top IPs: [('192.168.1.100', 400), ('192.168.1.101', 300), ...]
```

---
---
---

## **🔹 8.8 Data Encryption (Enkripsi Data)**
### **📌 Penjelasan**
**Enkripsi Data** adalah **proses mengamankan data** sehingga **hanya pihak yang berwenang** yang bisa membacanya. Digunakan untuk:
- **Data at Rest**: Data yang disimpan (database, file).
- **Data in Transit**: Data yang dikirim (API, webhooks).

**Manfaat untuk MusGo-OS:**
- **Lindungi data sensitif** (password, API key, dll.).
- **Patuhi regulasi** (GDPR, HIPAA).

---
#### **🚀 Contoh Implementasi: Data Encryption**
##### **1. Enkripsi Data at Rest (Python - Fernet)**
```python
from cryptography.fernet import Fernet
import base64
import os

# Generate key (simpan dengan aman!)
def generate_key():
    return Fernet.generate_key()

# Enkripsi data
def encrypt_data(data: str, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted.decode()

# Dekripsi data
def decrypt_data(encrypted_data: str, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data.encode())
    return decrypted.decode()

# Contoh penggunaan
key = generate_key()  # Simpan key ini di environment variable!
print("Key:", key.decode())

# Enkripsi API key
api_key = "ZAPIER_API_KEY_123"
encrypted_api_key = encrypt_data(api_key, key)
print("Encrypted API Key:", encrypted_api_key)

# Dekripsi API key
decrypted_api_key = decrypt_data(encrypted_api_key, key)
print("Decrypted API Key:", decrypted_api_key)
```

**Output:**
```
Key: abc123... (base64 encoded)
Encrypted API Key: gAAAAABjX... (base64 encoded)
Decrypted API Key: ZAPIER_API_KEY_123
```

---
##### **2. Enkripsi Data in Transit (HTTPS + mTLS)**
- **HTTPS**: Sudah **otomatis terenkripsi** (TLS).
- **mTLS**: **Saling autentikasi** (lihat [Bagian 8.5](#85-mtls-mutual-tls)).

---
##### **3. Enkripsi Database (PostgreSQL + pgcrypto)**
**Contoh SQL untuk Enkripsi di PostgreSQL:**
```sql
-- Enable pgcrypto
CREATE EXTENSION pgcrypto;

-- Enkripsi data
INSERT INTO users (email, encrypted_api_key)
VALUES ('dhani@musgo-os.com', pgp_sym_encrypt('ZAPIER_API_KEY_123', 'SECRET_KEY'));

-- Dekripsi data
SELECT
    email,
    pgp_sym_decrypt(encrypted_api_key::bytea, 'SECRET_KEY') as api_key
FROM users;
```

---
##### **4. Enkripsi di Redis**
```python
import redis
from cryptography.fernet import Fernet

# Setup Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Key untuk enkripsi
key = Fernet.generate_key()
fernet = Fernet(key)

# Simpan data terenkripsi
api_key = "ZAPIER_API_KEY_123"
encrypted_api_key = fernet.encrypt(api_key.encode()).decode()
r.set("user:123:api_key", encrypted_api_key)

# Ambil dan dekripsi data
encrypted_data = r.get("user:123:api_key")
if encrypted_data:
    decrypted_api_key = fernet.decrypt(encrypted_data).decode()
    print("Decrypted API Key:", decrypted_api_key)
```

---
---
---

## **🔹 8.9 Input Validation (Validasi Input)**
### **📌 Penjelasan**
**Input Validation** adalah **proses memvalidasi data yang masuk** untuk:
- **Mencegah SQL Injection**.
- **Mencegah XSS (Cross-Site Scripting)**.
- **Mencegah data korup**.

**Manfaat untuk MusGo-OS:**
- **Hindari serangan** (injection, XSS).
- **Data konsisten** (format benar).

---
#### **🚀 Contoh Implementasi: Input Validation**
##### **1. Backend MusGo-OS (Python - Pydantic)**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator, Field
from typing import List, Optional
import re

app = FastAPI()

# Model untuk Zap
class ZapCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    trigger: dict
    action: dict
    user_id: str = Field(..., regex=r"^[a-zA-Z0-9_-]{1,50}$")  # Hanya alphanumeric, _, -

    @validator("name")
    def name_must_not_contain_special_chars(cls, v):
        if not re.match(r"^[a-zA-Z0-9 \-_]+$", v):
            raise ValueError("Nama Zap hanya boleh mengandung huruf, angka, spasi, -, _")
        return v

    @validator("trigger", "action")
    def validate_app_and_action(cls, v):
        if "app" not in v or "action" not in v:
            raise ValueError("Trigger/Action harus memiliki 'app' dan 'action'")
        if not isinstance(v["app"], str) or not isinstance(v["action"], str):
            raise ValueError("'app' dan 'action' harus string")
        return v

# Model untuk Slack Message
class SlackMessage(BaseModel):
    channel: str = Field(..., regex=r"^#?[a-zA-Z0-9_-]{1,50}$")  # #channel atau channel
    text: str = Field(..., max_length=4000)  # Maksimal 4000 karakter (batas Slack)

    @validator("text")
    def sanitize_text(cls, v):
        # Hapus HTML tags (untuk mencegah XSS)
        return re.sub(r"<[^>]*>", "", v)

# Endpoint untuk buat Zap
@app.post("/api/zaps")
async def create_zap(zap: ZapCreate):
    """Buat Zap dengan validasi input"""
    return {"status": "success", "zap": zap.dict()}

# Endpoint untuk kirim pesan Slack
@app.post("/api/slack/messages")
async def send_slack_message(message: SlackMessage):
    """Kirim pesan Slack dengan validasi input"""
    # Sanitize channel (hapus # jika ada)
    channel = message.channel.lstrip("#")
    return {
        "status": "success",
        "channel": f"#{channel}",
        "text": message.text,
    }

# Contoh penggunaan
try:
    zap = ZapCreate(
        name="Google Drive → Slack",
        trigger={"app": "google_drive", "action": "New File"},
        action={"app": "slack", "action": "Send Channel Message"},
        user_id="USER_ID_123",
    )
    print("Zap valid:", zap.dict())
except Exception as e:
    print("Error:", e)
```

**Output:**
```
Zap valid: {
  'name': 'Google Drive → Slack',
  'trigger': {'app': 'google_drive', 'action': 'New File'},
  'action': {'app': 'slack', 'action': 'Send Channel Message'},
  'user_id': 'USER_ID_123'
}
```

---
##### **2. Frontend MusGo-OS (React + Input Validation)**
**Contoh Validasi Input di Form:**
```tsx
// File: src/components/ZapForm.tsx
import React, { useState } from "react";

interface ZapFormData {
  name: string;
  triggerApp: string;
  triggerAction: string;
  actionApp: string;
  actionAction: string;
}

const ZapForm: React.FC = () => {
  const [formData, setFormData] = useState<ZapFormData>({
    name: "",
    triggerApp: "google_drive",
    triggerAction: "New File",
    actionApp: "slack",
    actionAction: "Send Channel Message",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const validateForm = (): boolean => {
    const newErrors: Record<string, string> = {};

    // Validasi nama
    if (!formData.name.trim()) {
      newErrors.name = "Nama Zap tidak boleh kosong";
    } else if (formData.name.length > 100) {
      newErrors.name = "Nama Zap maksimal 100 karakter";
    } else if (!/^[a-zA-Z0-9 \-_]+$/.test(formData.name)) {
      newErrors.name = "Nama Zap hanya boleh mengandung huruf, angka, spasi, -, _";
    }

    // Validasi trigger dan action
    if (!formData.triggerApp || !formData.triggerAction) {
      newErrors.trigger = "Trigger harus dipilih";
    }
    if (!formData.actionApp || !formData.actionAction) {
      newErrors.action = "Action harus dipilih";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validateForm()) {
      // Kirim data ke backend
      console.log("Data valid:", formData);
      alert("Zap berhasil dibuat!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Buat Zap Baru</h2>

      <div>
        <label>Nama Zap:</label>
        <input
          type="text"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          maxLength={100}
        />
        {errors.name && <p style={{ color: "red" }}>{errors.name}</p>}
      </div>

      <div>
        <label>Trigger:</label>
        <div>
          <select
            value={formData.triggerApp}
            onChange={(e) => setFormData({ ...formData, triggerApp: e.target.value })}
          >
            <option value="google_drive">Google Drive</option>
            <option value="slack">Slack</option>
          </select>
          <select
            value={formData.triggerAction}
            onChange={(e) => setFormData({ ...formData, triggerAction: e.target.value })}
          >
            {formData.triggerApp === "google_drive" && (
              <>
                <option value="New File">File Baru</option>
                <option value="New File in Folder">File Baru di Folder</option>
              </>
            )}
            {formData.triggerApp === "slack" && (
              <>
                <option value="New Message">Pesan Baru</option>
                <option value="New Mention">Mention Baru</option>
              </>
            )}
          </select>
        </div>
        {errors.trigger && <p style={{ color: "red" }}>{errors.trigger}</p>}
      </div>

      <div>
        <label>Action:</label>
        <div>
          <select
            value={formData.actionApp}
            onChange={(e) => setFormData({ ...formData, actionApp: e.target.value })}
          >
            <option value="slack">Slack</option>
            <option value="notion">Notion</option>
          </select>
          <select
            value={formData.actionAction}
            onChange={(e) => setFormData({ ...formData, actionAction: e.target.value })}
          >
            {formData.actionApp === "slack" && (
              <>
                <option value="Send Channel Message">Kirim Pesan ke Channel</option>
                <option value="Send Direct Message">Kirim Pesan Langsung</option>
              </>
            )}
            {formData.actionApp === "notion" && (
              <>
                <option value="Create Database Row">Buat Baris Database</option>
                <option value="Update Database Row">Update Baris Database</option>
              </>
            )}
          </select>
        </div>
        {errors.action && <p style={{ color: "red" }}>{errors.action}</p>}

      <button type="submit">Buat Zap</button>
    </form>
  );
};

export default ZapForm;
```

---
---
---

## **🔹 8.10 Security Headers (HTTP Headers)**
### **📌 Penjelasan**
**Security Headers** adalah **HTTP headers** yang **meningkatkan keamanan** aplikasi web. Contoh:
- **CSP (Content Security Policy)**: Mencegah **XSS**.
- **HSTS (HTTP Strict Transport Security)**: Paksa **HTTPS**.
- **X-Frame-Options**: Mencegah **clickjacking**.
- **X-Content-Type-Options**: Mencegah **MIME sniffing**.

**Manfaat untuk MusGo-OS:**
- **Lindungi dari serangan web** (XSS, clickjacking, dll.).
- **Patuhi best practices keamanan**.

---
#### **🚀 Contoh Implementasi: Security Headers**
##### **1. Backend MusGo-OS (Python - FastAPI)**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# 1. HTTPS Redirect (paksa HTTPS)
app.add_middleware(HTTPSRedirectMiddleware)

# 2. Trusted Host (hanya izinkan domain tertentu)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["musgo-os.com", "www.musgo-os.com"],
)

# 3. CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://musgo-os.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)

    # Content Security Policy (CSP)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdn.zapier.com; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:; "
        "connect-src 'self' https://api.zapier.com; "
        "frame-src 'self' https://zapier.com; "
        "font-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'"
    )

    # HTTP Strict Transport Security (HSTS)
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"

    # X-Content-Type-Options
    response.headers["X-Content-Type-Options"] = "nosniff"

    # X-Frame-Options
    response.headers["X-Frame-Options"] = "DENY"

    # X-XSS-Protection
    response.headers["X-XSS-Protection"] = "1; mode=block"

    # Referrer-Policy
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    # Permissions-Policy
    response.headers["Permissions-Policy"] = (
        "geolocation=(), "
        "midi=(), "
        "sync-xhr=(), "
        "microphone=(), "
        "camera=(), "
        "magnetometer=(), "
        "gyroscope=(), "
        "fullscreen=(self), "
        "payment=()"
    )

    return response

@app.get("/")
async def root():
    return {"message": "Hello, MusGo-OS!"}
```

---
##### **2. Frontend MusGo-OS (React + Meta Tags)**
**Contoh Meta Tags untuk Security Headers:**
```html
<!-- File: public/index.html -->
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://cdn.zapier.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data:;
  connect-src 'self' https://api.zapier.com;
  frame-src 'self' https://zapier.com;
  font-src 'self';
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  frame-ancestors 'none'
">
<meta http-equiv="Strict-Transport-Security" content="max-age=31536000; includeSubDomains; preload">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-XSS-Protection" content="1; mode=block">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Permissions-Policy" content="
  geolocation=(),
  midi=(),
  sync-xhr=(),
  microphone=(),
  camera=(),
  magnetometer=(),
  gyroscope=(),
  fullscreen=(self),
  payment=()
">
```

---
---
---

## **🔹 8.11 Zero Trust Architecture (Arsitektur Zero Trust)**
### **📌 Penjelasan**
**Zero Trust** adalah **model keamanan** yang **tidak percaya siapa pun** (bahkan internal services). Setiap **request** harus **divalidasi**, **diautentikasi**, dan **diororisasi**.

**Prinsip Zero Trust:**
1. **Verify Explicitly**: Validasi **setiap request** (user, device, location).
2. **Least Privilege Access**: Berikan **akses minimal**.
3. **Assume Breach**: Asumsikan **sistem sudah disusupi**.

**Manfaat untuk MusGo-OS:**
- **Lindungi dari serangan internal**.
- **Kurangi risiko data leakage**.

---
### **🚀 Contoh Implementasi: Zero Trust**
#### **1. Arsitektur Zero Trust untuk MusGo-OS**
```
User → [Auth] → [mTLS] → MusGo-OS Frontend → [JWT] → [RBAC] → MusGo-OS Backend → [mTLS] → [JWT] → Zapier API
```

---
#### **2. Implementasi Zero Trust (Python - FastAPI)**
```python
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta
from typing import Dict, Any
import secrets

app = FastAPI()
security = HTTPBearer()

# Secret key untuk JWT
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

# 1. Autentikasi (JWT)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    """Verify JWT"""
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"user_id": payload.get("sub"), "role": payload.get("role")}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token kadaluarsa")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token tidak valid")

# 2. Otorisasi (RBAC)
async def check_permission(required_role: str, user: Dict[str, Any] = Depends(get_current_user)):
    """Cek role user"""
    if user["role"] != required_role:
        raise HTTPException(status_code=403, detail="Permission denied")
    return True

# 3. Validasi Request (Contoh: Cek IP, User-Agent)
async def validate_request(request: Request):
    """Validasi request (IP, User-Agent, dll.)"""
    # Cek IP (contoh: hanya izinkan IP tertentu)
    allowed_ips = ["192.168.1.0/24", "10.0.0.0/8"]
    client_ip = request.client.host if request.client else None
    if client_ip not in allowed_ips:
        raise HTTPException(status_code=403, detail="IP tidak diizinkan")

    # Cek User-Agent (contoh: blokir bot)
    user_agent = request.headers.get("user-agent", "").lower()
    if "bot" in user_agent or "crawl" in user_agent:
        raise HTTPException(status_code=403, detail="Bot tidak diizinkan")

    return True

# 4. Protected Endpoint (dengan Zero Trust)
@app.get("/api/secure")
async def secure_endpoint(
    user: Dict[str, Any] = Depends(get_current_user),
    _: bool = Depends(lambda: check_permission("admin")),
    __: bool = Depends(validate_request),
):
    """Endpoint dengan Zero Trust"""
    return {
        "message": "Akses diizinkan!",
        "user": user,
    }

# 5. Middleware untuk Zero Trust
@app.middleware("http")
async def zero_trust_middleware(request: Request, call_next):
    """Middleware untuk Zero Trust"""
    # 1. Cek path (blokir path sensitif)
    if request.url.path.startswith("/api/admin") and not request.url.path.startswith("/api/admin/login"):
        if not request.headers.get("Authorization"):
            return JSONResponse(
                status_code=401,
                content={"detail": "Autentikasi diperlukan"},
            )

    # 2. Cek method (blokir method yang tidak diizinkan)
    if request.method not in ["GET", "POST", "PUT", "DELETE"]:
        return JSONResponse(
            status_code=405,
            content={"detail": "Method tidak diizinkan"},
        )

    # 3. Lanjutkan request
    response = await call_next(request)
    return response
```

---
---
---

## **🔹 8.12 Compliance (Kepatuhan)**
### **📌 Penjelasan**
**Compliance** adalah **kepatuhan terhadap regulasi** seperti:
- **GDPR**: Perlindungan data user (UE).
- **SOC 2**: Keamanan, ketersediaan, integritas (AS).
- **ISO 27001**: Manajemen keamanan informasi.
- **HIPAA**: Perlindungan data kesehatan (AS).

**Manfaat untuk MusGo-OS:**
- **Hindari denda** (misal: GDPR fine hingga 4% dari revenue global).
- **Meningkatkan kepercayaan user**.

---
#### **🚀 Contoh Implementasi: GDPR Compliance**
##### **1. Right to be Forgotten (Hapus Data User)**
**Contoh Endpoint (Python - FastAPI):**
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

# Dummy database
users_db = {
    "USER_ID_123": {
        "email": "dhani@musgo-os.com",
        "name": "Dhani Yuliawan",
        "zaps": ["ZAP_ID_1", "ZAP_ID_2"],
        "api_keys": ["API_KEY_1", "API_KEY_2"],
    },
}

# Model untuk request
class DeleteUserRequest(BaseModel):
    user_id: str
    confirm: bool = False  # User harus konfirmasi

# Endpoint untuk hapus data user (GDPR)
@app.delete("/api/users/{user_id}")
async def delete_user(
    user_id: str,
    request: DeleteUserRequest,
    current_user: Dict[str, Any] = Depends(get_current_user),
):
    """Hapus data user (GDPR Right to be Forgotten)"""
    if not request.confirm:
        raise HTTPException(status_code=400, detail="Anda harus konfirmasi penghapusan")

    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    # Cek apakah current user adalah user yang ingin dihapus atau admin
    if current_user["user_id"] != user_id and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Anda tidak berwenang menghapus user ini")

    # Hapus data user
    user_data = users_db.pop(user_id)

    # Hapus Zap user
    for zap_id in user_data["zaps"]:
        delete_zap(zap_id)  # Implementasi tergantung sistem Anda

    # Hapus API keys
    for api_key in user_data["api_keys"]:
        revoke_api_key(api_key)  # Implementasi tergantung sistem Anda

    # Catat ke audit log
    await audit_log(
        request,
        action="delete_user",
        user_id=current_user["user_id"],
        data={"deleted_user": user_id},
        status="success",
    )

    return {"status": "success", "message": f"User {user_id} dan data terkait telah dihapus"}

# Helper functions (contoh)
def delete_zap(zap_id: str):
    """Hapus Zap"""
    print(f"Zap {zap_id} dihapus")

def revoke_api_key(api_key: str):
    """Cabut API key"""
    print(f"API Key {api_key} dicabut")
```

---
##### **2. Data Portability (Eksport Data User)**
**Contoh Endpoint (Python - FastAPI):**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
import json
from datetime import datetime

app = FastAPI()

# Endpoint untuk ekspor data user (GDPR Data Portability)
@app.get("/api/users/{user_id}/export")
async def export_user_data(
    user_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user),
):
    """Eksport data user (GDPR Data Portability)"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    if current_user["user_id"] != user_id and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Anda tidak berwenang mengekspor data user ini")

    user_data = users_db[user_id]

    # Ambil data Zap user
    user_zaps = []
    for zap_id in user_data["zaps"]:
        zap_data = get_zap_data(zap_id)  # Implementasi tergantung sistem Anda
        user_zaps.append(zap_data)

    # Ambil data API keys (hanya untuk admin)
    api_keys = []
    if current_user["role"] == "admin":
        for api_key in user_data["api_keys"]:
            api_keys.append({"key": api_key, "created_at": "..."})

    # Buat data ekspor
    export_data = {
        "user": {
            "email": user_data["email"],
            "name": user_data["name"],
            "created_at": datetime.now().isoformat(),
        },
        "zaps": user_zaps,
        "api_keys": api_keys,
    }

    # Catat ke audit log
    await audit_log(
        request,
        action="export_user_data",
        user_id=current_user["user_id"],
        data={"exported_user": user_id},
        status="success",
    )

    # Return data sebagai JSON
    return JSONResponse(
        content=export_data,
        headers={"Content-Disposition": f"attachment; filename=user_{user_id}_export_{datetime.now().strftime('%Y%m%d')}.json"},
    )

# Helper function (contoh)
def get_zap_data(zap_id: str):
    """Ambil data Zap"""
    return {
        "id": zap_id,
        "name": f"Zap {zap_id}",
        "created_at": datetime.now().isoformat(),
        "steps": [{"app": "google_drive", "action": "New File"}],
    }
```

---
##### **3. Cookie Consent (Persetujuan Cookie)**
**Contoh UI (React + TypeScript):**
```tsx
// File: src/components/CookieConsent.tsx
import React, { useState, useEffect } from "react";

const CookieConsent: React.FC = () => {
  const [showConsent, setShowConsent] = useState(false);

  // Cek apakah user sudah setuju
  useEffect(() => {
    const consent = localStorage.getItem("cookie_consent");
    if (!consent) {
      setShowConsent(true);
    }
  }, []);

  const handleAccept = () => {
    localStorage.setItem("cookie_consent", "true");
    setShowConsent(false);
    // Load analytics, dll.
    loadAnalytics();
  };

  const handleReject = () => {
    localStorage.setItem("cookie_consent", "false");
    setShowConsent(false);
  };

  if (!showConsent) {
    return null;
  }

  return (
    <div style={{
      position: "fixed",
      bottom: 0,
      left: 0,
      right: 0,
      background: "white",
      padding: "20px",
      boxShadow: "0 -2px 10px rgba(0,0,0,0.1)",
      zIndex: 1000,
    }}>
      <h3>Cookie Consent</h3>
      <p>
        Kami menggunakan cookie untuk meningkatkan pengalaman Anda.
        Dengan menggunakan situs ini, Anda setuju dengan kebijakan cookie kami.
      </p>
      <div style={{ display: "flex", gap: "10px" }}>
        <button
          onClick={handleReject}
          style={{
            padding: "8px 16px",
            background: "#f0f0f0",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Tolak
        </button>
        <button
          onClick={handleAccept}
          style={{
            padding: "8px 16px",
            background: "#4285F4",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Terima
        </button>
      </div>
    </div>
  );
};

export default CookieConsent;
```

---
---
---
# **📌 PART 8: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 8 (Security & Compliance)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **Authentication** | OAuth 2.0 | User bisa menghubungkan akun eksternal | ✅ **Contoh kode tersedia** |
| **Authorization** | RBAC | Kontrol akses berdasarkan role | ✅ **Contoh kode tersedia** |
| **JWT** | Token autentikasi | Autentikasi API yang aman | ✅ **Contoh kode tersedia** |
| **mTLS** | Mutual TLS | Service-to-service authentication | ✅ **Contoh kode tersedia** |
| **Rate Limiting** | Batasi panggilan API | Hindari abuse dan rate limit | ✅ **Contoh kode tersedia** |
| **Audit Logging** | Catat semua aktivitas | Deteksi intrusi, debugging | ✅ **Contoh kode tersedia** |
| **Data Encryption** | Enkripsi data | Lindungi data sensitif | ✅ **Contoh kode tersedia** |
| **Input Validation** | Validasi input | Hindari SQL Injection, XSS | ✅ **Contoh kode tersedia** |
| **Security Headers** | HTTP Headers | Lindungi dari serangan web | ✅ **Contoh kode tersedia** |
| **Zero Trust** | Arsitektur Zero Trust | Lindungi dari serangan internal | ✅ **Contoh kode tersedia** |
| **Compliance** | GDPR, SOC 2, ISO 27001 | Patuhi regulasi | ✅ **Contoh kode tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Implementasikan OAuth 2.0** (untuk user menghubungkan akun eksternal).
- [ ] **Implementasikan RBAC** (untuk kontrol akses).
- [ ] **Implementasikan JWT** (untuk autentikasi API).
- [ ] **Setup Audit Logging** (untuk pencatatan aktivitas).
- [ ] **Validasi Input** (untuk mencegah serangan).

### **2. Mid-Term (1 Bulan)**
- [ ] **Implementasikan mTLS** (untuk service-to-service authentication).
- [ ] **Implementasikan Rate Limiting** (untuk hindari abuse).
- [ ] **Enkripsi Data** (untuk data sensitif).
- [ ] **Setup Security Headers** (untuk keamanan web).
- [ ] **Implementasikan Zero Trust** (untuk arsitektur aman).

### **3. Long-Term (3+ Bulan)**
- [ ] **Audit Security** (untuk mencari celah keamanan).
- [ ] **Sertifikasi Compliance** (GDPR, SOC 2, ISO 27001).
- [ ] **Monitoring Keamanan** (untuk deteksi ancaman real-time).
- [ ] **Training Keamanan** (untuk developer dan user).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 9: Deployment & Scaling** (Untuk deployment MusGo-OS + Zapier)
   - [ ] **Part 10: Monitoring & Analytics** (Untuk pemantauan workflow)
   - [ ] **Part 11: Incident Response** (Untuk penanganan insiden keamanan)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full integrasi dengan Zero Trust)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full code untuk backend (Python) + frontend (TypeScript)**?
   - [ ] **Dokumentasi keamanan lengkap untuk MusGo-OS**?
   - [ ] **Checklist compliance (GDPR, SOC 2, ISO 27001)**?

3. **Apakah ada area keamanan spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **OAuth 2.0**, **mTLS**, **Audit Logging**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 9: Deployment & Scaling** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **deploy dan scale** integrasi **MusGo-OS 2in1 + Zapier** menggunakan **Docker, Kubernetes, CI/CD, dan arsitektur scalable**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN DEPLOYMENT & SCALING (PART 9)**
*Terjemahan + Implementasi untuk Deployment Production-Ready*

---

---

## **🔹 9.1 Overview Deployment & Scaling**
### **📌 Penjelasan (Bahasa Indonesia)**
**Deployment & Scaling** adalah **proses mempublish dan mengelola** aplikasi **MusGo-OS + Zapier** di **environment production** dengan **performa, keandalan, dan skalabilitas** yang optimal.

**Tantangan untuk MusGo-OS:**
- **High Availability**: MusGo-OS harus **selalu tersedia** (99.99% uptime).
- **Scalability**: Harus bisa **menangani ribuan user** dan **jutaan request**.
- **Resilience**: Harus **tahan terhadap kegagalan** (misal: Zapier API down, database error).
- **Security**: Harus **aman** dari serangan (DDoS, injection, dll.).
- **Cost-Effective**: Harus **efisien biaya** (tidak boros resource).

**Arsitektur Target:**
```
User → CDN → Load Balancer → Kubernetes (MusGo-OS) → Zapier API
                     ↓
               Monitoring (Prometheus + Grafana)
                     ↓
               Logging (ELK Stack)
                     ↓
               Database (PostgreSQL + Redis)
```

---
### **🚀 Contoh Implementasi untuk MusGo-OS**
#### **Use-Case 1: Deployment dengan Docker & Kubernetes**
**Skenario:**
MusGo-OS ingin **deploy backend (Python) + frontend (TypeScript)** ke **Kubernetes** dengan **auto-scaling** dan **high availability**.

**Arsitektur:**
```
User → Ingress (Nginx) → Kubernetes Pod (MusGo-OS Backend) → Zapier API
User → Ingress (Nginx) → Kubernetes Pod (MusGo-OS Frontend) → User
```

---
---
---

## **🔹 9.2 Docker (Containerization)**
### **📌 Penjelasan**
**Docker** adalah **platform containerization** yang memungkinkan **MusGo-OS** untuk:
- **Berjalan di lingkungan yang konsisten** (dev, staging, production).
- **Isolasi aplikasi** (backend, frontend, database).
- **Mudah di-deploy** ke server mana pun.

---
#### **🚀 Contoh Implementasi: Docker**
##### **1. Dockerfile untuk Backend (Python - FastAPI)**
```dockerfile
# File: backend/Dockerfile
# Stage 1: Build
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Install additional tools (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY . .

# Environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Catatan:**
- **Multi-stage build**: Mengurangi ukuran image.
- **Health check**: Untuk Kubernetes liveness probe.
- **Non-root user**: Lebih aman (tidak berjalan sebagai root).

---
##### **2. Dockerfile untuk Frontend (TypeScript - Next.js)**
```dockerfile
# File: frontend/Dockerfile
# Stage 1: Build
FROM node:18-alpine as builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json yarn.lock* package-lock.json* ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build Next.js app
RUN npm run build

# Stage 2: Runtime
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy built files from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

# Environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:3000/health || exit 1

# Run Next.js
CMD ["npm", "start"]
```

---
##### **3. Docker Compose (Untuk Development)**
```yaml
# File: docker-compose.yml
version: "3.8"

services:
  # Backend (FastAPI)
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: musgo-os-backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
      - ZAPIER_API_KEY=${ZAPIER_API_KEY}
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/musgo_os
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Frontend (Next.js)
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: musgo-os-frontend
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - NEXT_PUBLIC_API_URL=http://backend:8000
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
      - /app/node_modules
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Database (PostgreSQL)
  db:
    image: postgres:15-alpine
    container_name: musgo-os-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=musgo_os
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Redis (Caching)
  redis:
    image: redis:7-alpine
    container_name: musgo-os-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Nginx (Reverse Proxy)
  nginx:
    image: nginx:alpine
    container_name: musgo-os-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    depends_on:
      - backend
      - frontend
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:

networks:
  musgo-os-network:
    driver: bridge
```

---
##### **4. Konfigurasi Nginx (Reverse Proxy)**
```nginx
# File: nginx/nginx.conf
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    # Logging
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    # Gzip
    gzip  on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Upstream untuk backend
    upstream backend {
        server backend:8000;
    }

    # Upstream untuk frontend
    upstream frontend {
        server frontend:3000;
    }

    # Server HTTP (redirect ke HTTPS)
    server {
        listen 80;
        server_name musgo-os.com www.musgo-os.com;

        location / {
            return 301 https://$host$request_uri;
        }
    }

    # Server HTTPS
    server {
        listen 443 ssl;
        server_name musgo-os.com www.musgo-os.com;

        # SSL Configuration
        ssl_certificate     /etc/nginx/ssl/musgo-os.crt;
        ssl_certificate_key /etc/nginx/ssl/musgo-os.key;
        ssl_protocols       TLSv1.2 TLSv1.3;
        ssl_ciphers         HIGH:!aNULL:!MD5;

        # Security Headers
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-Frame-Options "DENY" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.zapier.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' https://api.zapier.com; frame-src 'self' https://zapier.com;" always;

        # API Routes (Backend)
        location /api/ {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Frontend Routes
        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # WebSocket (jika diperlukan)
        location /ws/ {
            proxy_pass http://backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }

        # Static Files
        location /static/ {
            alias /app/static/;
            expires 30d;
        }
    }
}
```

---
##### **5. Build dan Run Docker Compose**
```bash
# Build semua image
docker-compose build

# Jalankan container
docker-compose up -d

# Lihat log
docker-compose logs -f

# Hentikan container
docker-compose down
```

---
---
---

## **🔹 9.3 Kubernetes (Orchestration)**
### **📌 Penjelasan**
**Kubernetes (K8s)** adalah **sistem orchestration** untuk **mengelola container** (Docker) di **skala besar**. Digunakan untuk:
- **Auto-scaling**: Menambahkan/menghapus pod berdasarkan beban.
- **Self-healing**: Otomatis restart pod yang gagal.
- **Load balancing**: Distribusi traffic ke pod.
- **Rollout & Rollback**: Deploy update tanpa downtime.

---
#### **🚀 Contoh Implementasi: Kubernetes**
##### **1. Struktur Folder Kubernetes**
```
k8s/
│
├── backend/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml (Horizontal Pod Autoscaler)
│   ├── configmap.yaml
│   └── secret.yaml
│
├── frontend/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── database/
│   ├── statefulset.yaml
│   ├── service.yaml
│   └── pvc.yaml (Persistent Volume Claim)
│
├── redis/
│   ├── statefulset.yaml
│   ├── service.yaml
│   └── pvc.yaml
│
├── nginx/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
└── monitoring/
    ├── prometheus.yaml
    └── grafana.yaml
```

---
##### **2. Deployment Backend (FastAPI)**
```yaml
# File: k8s/backend/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata
```
---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 10: Monitoring & Analytics** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **monitoring dan analitik** integrasi **MusGo-OS 2in1 + Zapier**, termasuk **logging, metrics, tracing, alerting, dan dashboard**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN MONITORING & ANALYTICS (PART 10)**
*Terjemahan + Implementasi untuk Pemantauan dan Analitik Production-Ready*

---

---

---

## **🔹 10.1 Overview Monitoring & Analytics**
### **📌 Penjelasan (Bahasa Indonesia)**
**Monitoring & Analytics** adalah **proses memantau, menganalisis, dan mengoptimalkan** performa, keandalan, dan keamanan **MusGo-OS + Zapier**. Tujuannya:
✅ **Deteksi Masalah**: Cepat menemukan **error, latency, atau downtime**.
✅ **Optimasi Performa**: Identifikasi **bottleneck** dan **improve efficiency**.
✅ **Keamanan**: Deteksi **ancaman atau aktivitas mencurigakan**.
✅ **Kepatuhan**: Patuhi **SLA (Service Level Agreement)** dan regulasi.
✅ **Business Insights**: Pahami **penggunaan, tren, dan ROI** integrasi Zapier.

**Komponen Utama:**
| Komponen | Deskripsi | Tools |
|----------|-----------|-------|
| **Logging** | Catat semua aktivitas (request, error, dll.) | ELK Stack, Loki, Fluentd |
| **Metrics** | Ukur performa (latency, throughput, dll.) | Prometheus, Datadog |
| **Tracing** | Lacak request melintasi service | Jaeger, OpenTelemetry |
| **Alerting** | Notifikasi saat ada masalah | Alertmanager, PagerDuty |
| **Dashboard** | Visualisasi data | Grafana, Kibana |
| **Error Tracking** | Pantau error aplikasi | Sentry, Rollbar |

---
### **🚀 Contoh Arsitektur Monitoring untuk MusGo-OS**
```
User → MusGo-OS (Backend/Frontend) → Zapier API
       ↓ (Metrics)               ↓ (Metrics)
Prometheus ←─ (Scrape) ───────── Zapier Exporter
       ↓
   Grafana (Dashboard)
       ↓
Alertmanager → Slack/Email/PagerDuty
       ↑
   (Alert Rules)

User → MusGo-OS → Logs → Loki/Elasticsearch → Grafana (Logs)
User → MusGo-OS → Traces → Jaeger → Grafana (Traces)
```

---
---
---

## **🔹 10.2 Logging (Pencatatan Aktivitas)**
### **📌 Penjelasan**
**Logging** adalah **proses mencatat semua aktivitas** (request, error, event) untuk:
- **Debugging**: Temukan **penyebab error**.
- **Audit**: Lacak **aktivitas user**.
- **Compliance**: Patuhi **GDPR, SOC 2**.

---
#### **🚀 Contoh Implementasi: Logging**
##### **1. Backend MusGo-OS (Python - FastAPI + Structured Logging)**
```python
# File: backend/logging_config.py
import logging
import json
from pythonjsonlogger import jsonlogger
from datetime import datetime

def setup_logging():
    """Setup structured logging (JSON format)"""
    logger = logging.getLogger(__name__)

    # JSON Formatter
    class CustomJsonFormatter(jsonlogger.JsonFormatter):
        def add_fields(self, log_record, record, message_dict):
            super().add_fields(log_record, record, message_dict)
            log_record["timestamp"] = datetime.utcnow().isoformat()
            log_record["level"] = record.levelname
            log_record["logger"] = record.name
            if hasattr(record, "user_id"):
                log_record["user_id"] = record.user_id
            if hasattr(record, "request_id"):
                log_record["request_id"] = record.request_id

    # Handler untuk console (development)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = CustomJsonFormatter()
    console_handler.setFormatter(console_formatter)

    # Handler untuk file (production)
    file_handler = logging.handlers.RotatingFileHandler(
        "musgo_os.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
    )
    file_handler.setLevel(logging.INFO)
    file_formatter = CustomJsonFormatter()
    file_handler.setFormatter(file_formatter)

    # Tambahkan handler ke logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    return logger

# Setup logger global
logger = setup_logging()
```

---
##### **2. Middleware untuk Request Logging (FastAPI)**
```python
# File: backend/middlewares.py
from fastapi import Request
from uuid import uuid4
import time
from .logging_config import logger

async def request_logging_middleware(request: Request, call_next):
    """Middleware untuk logging request"""
    # Generate request ID
    request_id = str(uuid4())
    request.state.request_id = request_id

    # Start timer
    start_time = time.time()

    # Log request
    logger.info(
        "Request started",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "query_params": dict(request.query_params),
            "headers": dict(request.headers),
            "client": request.client.host if request.client else None,
        }
    )

    try:
        # Process request
        response = await call_next(request)
    except Exception as e:
        # Log error
        logger.error(
            "Request failed",
            extra={
                "request_id": request_id,
                "error": str(e),
                "status_code": 500,
            },
            exc_info=True
        )
        raise
    else:
        # Calculate duration
        duration = time.time() - start_time

        # Log response
        logger.info(
            "Request completed",
            extra={
                "request_id": request_id,
                "status_code": response.status_code,
                "duration": f"{duration:.3f}s",
            }
        )
        return response
```

---
##### **3. Integrasi dengan Loki (Grafana Loki)**
**Loki** adalah **sistem logging** yang **ringan dan scalable** (oleh Grafana). Cocok untuk **MusGo-OS** karena:
- **Murah** (tidak memerlukan banyak resource).
- **Integrasi mudah** dengan Grafana.
- **Support structured logging** (JSON).

**Contoh Setup Loki + Promtail (Docker Compose):**
```yaml
# File: docker-compose.monitoring.yml
version: "3.8"

services:
  # Loki (Logging Server)
  loki:
    image: grafana/loki:latest
    container_name: loki
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    volumes:
      - ./loki:/etc/loki
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Promtail (Log Collector)
  promtail:
    image: grafana/promtail:latest
    container_name: promtail
    volumes:
      - /var/log/musgo-os:/var/log/musgo-os  # Mount log directory
      - ./promtail:/etc/promtail
    command: -config.file=/etc/promtail/config.yml
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Grafana (Dashboard)
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  grafana_data:

networks:
  musgo-os-network:
    external: true
```

**Konfigurasi Promtail (`promtail/config.yml`):**
```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: musgo-os
    static_configs:
      - targets:
          - localhost
        labels:
          job: musgo-os
          __path__: /var/log/musgo-os/*.log
    pipeline_stages:
      - json:
          expressions:
            level: level
            message: msg
            timestamp: timestamp
            request_id: request_id
            user_id: user_id
      - labels:
          level:
          user_id:
          request_id:
```

---
##### **4. Query Log di Grafana**
1. Buka **Grafana** (`http://localhost:3000`).
2. Tambahkan **Loki** sebagai **Data Source** (URL: `http://loki:3100`).
3. Buat **Dashboard** baru dan tambahkan **Logs Panel**.
4. Query log:
   ```
   {job="musgo-os"} |= "error"
   ```
   atau
   ```
   {job="musgo-os", user_id="USER_ID_123"}
   ```

---
---
---

## **🔹 10.3 Metrics (Pengukuran Performa)**
### **📌 Penjelasan**
**Metrics** adalah **data kuantitatif** yang mengukur **performa sistem**, seperti:
- **Latency**: Waktu respon API.
- **Throughput**: Jumlah request per detik.
- **Error Rate**: Persentase request yang gagal.
- **Resource Usage**: CPU, Memory, Disk.

**Tools:**
- **Prometheus**: Scrape dan simpan metrics.
- **Grafana**: Visualisasi metrics.
- **Zapier Exporter**: Export metrics dari Zapier API.

---
#### **🚀 Contoh Implementasi: Metrics**
##### **1. Backend MusGo-OS (Python - FastAPI + Prometheus)**
```python
# File: backend/metrics.py
from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time

# Metrics
REQUEST_COUNT = Counter(
    "musgo_os_requests_total",
    "Total HTTP Requests",
    ["method", "path", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "musgo_os_request_latency_seconds",
    "HTTP Request Latency",
    ["method", "path"],
    buckets=[0.1, 0.5, 1, 2, 5, 10]
)

REQUEST_ERRORS = Counter(
    "musgo_os_request_errors_total",
    "Total HTTP Request Errors",
    ["method", "path", "status_code"]
)

ACTIVE_USERS = Gauge(
    "musgo_os_active_users",
    "Number of Active Users"
)

ZAPIER_API_CALLS = Counter(
    "musgo_os_zapier_api_calls_total",
    "Total Zapier API Calls",
    ["endpoint", "status_code"]
)

ZAPIER_API_LATENCY = Histogram(
    "musgo_os_zapier_api_latency_seconds",
    "Zapier API Latency",
    ["endpoint"],
    buckets=[0.1, 0.5, 1, 2, 5]
)

def start_metrics_server(port: int = 8001):
    """Start Prometheus metrics server"""
    start_http_server(port)
    print(f"Prometheus metrics server running on port {port}")

# Middleware untuk metrics
async def metrics_middleware(request: Request, call_next):
    """Middleware untuk metrics"""
    method = request.method
    path = request.url.path

    # Increment request count
    REQUEST_COUNT.labels(method=method, path=path, status_code="000").inc()

    # Start timer
    start_time = time.time()

    try:
        response = await call_next(request)
    except Exception as e:
        # Increment error count
        REQUEST_ERRORS.labels(method=method, path=path, status_code=500).inc()
        raise
    else:
        # Calculate latency
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method=method, path=path).observe(latency)

        # Update request count with actual status code
        REQUEST_COUNT.labels(method=method, path=path, status_code=response.status_code).inc()

        if response.status_code >= 400:
            REQUEST_ERRORS.labels(method=method, path=path, status_code=response.status_code).inc()

        return response
```

---
##### **2. Integrasi dengan Prometheus**
**Prometheus** akan **scrape metrics** dari endpoint `/metrics` (default port `8001`).

**Contoh Konfigurasi Prometheus (`prometheus.yml`):**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "musgo-os"
    static_configs:
      - targets: ["backend:8001"]  # Backend MusGo-OS
        labels:
          service: "musgo-os-backend"

  - job_name: "zapier-exporter"
    static_configs:
      - targets: ["zapier-exporter:9090"]  # Zapier Exporter (lihat bagian selanjutnya)
        labels:
          service: "zapier-exporter"
```

---
##### **3. Zapier Exporter (Custom Exporter untuk Zapier API)**
**Zapier Exporter** adalah **service** yang **scrape metrics dari Zapier API** (misal: API calls, errors, latency).

**Contoh Kode (Python):**
```python
# File: exporters/zapier_exporter.py
from prometheus_client import start_http_server, Gauge, Counter
import requests
import time
import os

# Metrics
ZAPIER_API_CALLS = Counter(
    "zapier_api_calls_total",
    "Total Zapier API Calls",
    ["endpoint", "status_code"]
)

ZAPIER_API_LATENCY = Gauge(
    "zapier_api_latency_seconds",
    "Zapier API Latency",
    ["endpoint"]
)

ZAPIER_API_ERRORS = Counter(
    "zapier_api_errors_total",
    "Total Zapier API Errors",
    ["endpoint", "status_code"]
)

ZAPIER_ZAPS_COUNT = Gauge(
    "zapier_zaps_count",
    "Number of Zaps",
    ["user_id"]
)

def scrape_zapier_api(api_key: str):
    """Scrape metrics dari Zapier API"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Scrape /zaps
    try:
        start_time = time.time()
        response = requests.get("https://api.zapier.com/v2/zaps", headers=headers)
        latency = time.time() - start_time

        ZAPIER_API_CALLS.labels(endpoint="/zaps", status_code=response.status_code).inc()
        ZAPIER_API_LATENCY.labels(endpoint="/zaps").set(latency)

        if response.status_code == 200:
            zaps = response.json().get("zaps", [])
            for zap in zaps:
                ZAPIER_ZAPS_COUNT.labels(user_id=zap.get("user_id", "unknown")).set(1)
        else:
            ZAPIER_API_ERRORS.labels(endpoint="/zaps", status_code=response.status_code).inc()
    except Exception as e:
        ZAPIER_API_ERRORS.labels(endpoint="/zaps", status_code=500).inc()
        print(f"Error scraping /zaps: {e}")

    # Scrape /actions/run (contoh)
    try:
        start_time = time.time()
        response = requests.post(
            "https://api.zapier.com/v2/actions/run",
            json={"app": "slack", "action": "Send Channel Message", "data": {"channel": "#test"}},
            headers=headers
        )
        latency = time.time() - start_time

        ZAPIER_API_CALLS.labels(endpoint="/actions/run", status_code=response.status_code).inc()
        ZAPIER_API_LATENCY.labels(endpoint="/actions/run").set(latency)

        if response.status_code != 200:
            ZAPIER_API_ERRORS.labels(endpoint="/actions/run", status_code=response.status_code).inc()
    except Exception as e:
        ZAPIER_API_ERRORS.labels(endpoint="/actions/run", status_code=500).inc()
        print(f"Error scraping /actions/run: {e}")

if __name__ == "__main__":
    # Start metrics server
    start_http_server(9090)

    # Scrape Zapier API setiap 30 detik
    api_key = os.getenv("ZAPIER_API_KEY")
    if not api_key:
        raise ValueError("ZAPIER_API_KEY environment variable is required")

    while True:
        scrape_zapier_api(api_key)
        time.sleep(30)
```

**Dockerfile untuk Zapier Exporter:**
```dockerfile
# File: exporters/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY zapier_exporter.py .

CMD ["python", "zapier_exporter.py"]
```

**Requirements (`exporters/requirements.txt`):**
```
prometheus-client==0.17.0
requests==2.31.0
```

---
##### **4. Docker Compose untuk Prometheus + Grafana**
```yaml
# File: docker-compose.monitoring.yml (lanjutan)
services:
  # Prometheus
  prometheus:
    image: prometheus/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus:/etc/prometheus
      - prometheus_data:/prometheus
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--web.console.libraries=/usr/share/prometheus/console_libraries"
      - "--web.console.templates=/usr/share/prometheus/consoles"
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Zapier Exporter
  zapier-exporter:
    build:
      context: ./exporters
      dockerfile: Dockerfile
    container_name: zapier-exporter
    ports:
      - "9091:9090"
    environment:
      - ZAPIER_API_KEY=${ZAPIER_API_KEY}
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  prometheus_data:
```

---
##### **5. Query Metrics di Grafana**
1. Tambahkan **Prometheus** sebagai **Data Source** (URL: `http://prometheus:9090`).
2. Buat **Dashboard** dengan panel-panel berikut:

| Panel | Query | Deskripsi |
|-------|-------|-----------|
| **Request Rate** | `rate(musgo_os_requests_total[1m])` | Jumlah request per menit |
| **Error Rate** | `rate(musgo_os_request_errors_total[1m])` | Jumlah error per menit |
| **Latency (P99)** | `histogram_quantile(0.99, sum(rate(musgo_os_request_latency_seconds_bucket[5m])) by (le))` | Latency 99th percentile |
| **Active Users** | `musgo_os_active_users` | Jumlah user aktif |
| **Zapier API Calls** | `rate(zapier_api_calls_total[1m])` | Jumlah panggilan Zapier API per menit |
| **Zapier API Latency** | `zapier_api_latency_seconds` | Latency Zapier API |
| **Zaps Count** | `zapier_zaps_count` | Jumlah Zap per user |

---
---
---

## **🔹 10.4 Tracing (Pelacakan Request)**
### **📌 Penjelasan**
**Tracing** adalah **proses melacak request** melintasi **multiple services** (misal: MusGo-OS → Zapier → Slack). Digunakan untuk:
- **Debugging**: Temukan **bottleneck** atau **error** di mana.
- **Performance Analysis**: Ukur **latency tiap service**.
- **Dependency Mapping**: Pahami **hubungan antar service**.

**Tools:**
- **OpenTelemetry**: Standar untuk tracing.
- **Jaeger**: Visualisasi traces.
- **Zipkin**: Alternatif untuk Jaeger.

---
#### **🚀 Contoh Implementasi: Tracing**
##### **1. Backend MusGo-OS (Python - FastAPI + OpenTelemetry)**
```python
# File: backend/tracing.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.resources import Resource

def setup_tracing(service_name: str = "musgo-os-backend"):
    """Setup OpenTelemetry Tracing"""
    # Resource (identitas service)
    resource = Resource.create(attributes={
        "service.name": service_name,
        "service.version": "1.0.0",
    })

    # Tracer Provider
    provider = TracerProvider(resource=resource)

    # Jaeger Exporter
    exporter = JaegerExporter(
        agent_host_name="jaeger",
        agent_port=6831,
    )

    # Span Processor
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)

    # Set global tracer provider
    trace.set_tracer_provider(provider)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)

    # Instrument Requests (untuk panggilan ke Zapier)
    RequestsInstrumentor.instrument()

    return provider

# Setup tracing
tracer_provider = setup_tracing()
tracer = trace.get_tracer(__name__)
```

---
##### **2. Middleware untuk Context Propagation**
```python
# File: backend/middlewares.py (lanjutan)
from opentelemetry import trace
from opentelemetry.trace import SpanKind, Status, StatusCode
from opentelemetry.context import Context

async def tracing_middleware(request: Request, call_next):
    """Middleware untuk tracing"""
    # Get tracer
    tracer = trace.get_tracer(__name__)

    # Start span
    with tracer.start_as_current_span(
        f"{request.method} {request.url.path}",
        kind=SpanKind.SERVER,
        attributes={
            "http.method": request.method,
            "http.url": str(request.url),
            "http.headers": dict(request.headers),
        }
    ) as span:
        try:
            # Add request ID to span
            span.set_attribute("request.id", request.state.request_id)

            # Process request
            response = await call_next(request)

            # Set span status
            span.set_status(Status(StatusCode.OK))
            span.set_attribute("http.status_code", response.status_code)

            return response
        except Exception as e:
            # Set span status to error
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR, description=str(e)))
            raise
```

---
##### **3. Instrumentasi Zapier API Calls**
```python
# File: backend/zapier_client.py
from opentelemetry import trace
from opentelemetry.trace import SpanKind
import requests

class ZapierClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.zapier.com/v2"
        self.tracer = trace.get_tracer(__name__)

    def run_action(self, app: str, action: str, data: dict):
        """Jalankan action Zapier dengan tracing"""
        with self.tracer.start_as_current_span(
            f"Zapier: {app}.{action}",
            kind=SpanKind.CLIENT,
            attributes={
                "zapier.app": app,
                "zapier.action": action,
                "zapier.data": str(data),
            }
        ) as span:
            try:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                }

                response = requests.post(
                    f"{self.base_url}/actions/run",
                    json={"app": app, "action": action, "data": data},
                    headers=headers
                )

                span.set_attribute("http.status_code", response.status_code)
                span.set_status(trace.Status(trace.StatusCode.OK))

                if response.status_code != 200:
                    span.record_exception(Exception(f"Zapier API Error: {response.text}"))
                    span.set_status(trace.Status(trace.StatusCode.ERROR, description=response.text))

                return response.json()
            except Exception as e:
                span.record_exception(e)
                span.set_status(trace.Status(trace.StatusCode.ERROR, description=str(e)))
                raise
```

---
##### **4. Docker Compose untuk Jaeger**
```yaml
# File: docker-compose.monitoring.yml (lanjutan)
services:
  # Jaeger (Tracing)
  jaeger:
    image: jaegertracing/all-in-one:latest
    container_name: jaeger
    ports:
      - "16686:16686"  # UI
      - "6831:6831"    # UDP (agent)
      - "6832:6832"    # UDP (agent)
      - "5778:5778"    # HTTP (collector)
    environment:
      - COLLECTOR_ZIPKIN_HOST_PORT=:9411
    networks:
      - musgo-os-network
    restart: unless-stopped
```

---
##### **5. Query Traces di Jaeger**
1. Buka **Jaeger UI** (`http://localhost:16686`).
2. Cari traces dengan:
   - **Service**: `musgo-os-backend`
   - **Operation**: `POST /api/zaps`
   - **Tags**: `http.status_code=200`
3. Lihat **detail trace** (latency tiap span, error, dll.).

---
---
---

## **🔹 10.5 Alerting (Notifikasi Masalah)**
### **📌 Penjelasan**
**Alerting** adalah **sistem notifikasi** yang **mengirim peringatan** saat ada **masalah** (misal: error rate tinggi, latency tinggi, downtime).

**Tools:**
- **Alertmanager** (Prometheus): Mengelola alert rules.
- **Grafana Alerts**: Alert langsung dari Grafana.
- **PagerDuty/Slack**: Kirim notifikasi ke tim.

---
#### **🚀 Contoh Implementasi: Alerting**
##### **1. Alert Rules (Prometheus)**
**Contoh File (`prometheus/alert.rules`):**
```yaml
groups:
- name: musgo-os-alerts
  rules:
    # High Error Rate
    - alert: HighErrorRate
      expr: rate(musgo_os_request_errors_total[5m]) / rate(musgo_os_requests_total[5m]) > 0.1
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "High error rate on MusGo-OS"
        description: "Error rate is {{ $value }} (threshold: 10%)"

    # High Latency
    - alert: HighLatency
      expr: histogram_quantile(0.99, sum(rate(musgo_os_request_latency_seconds_bucket[5m])) by (le)) > 2
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High latency on MusGo-OS"
        description: "99th percentile latency is {{ $value }}s (threshold: 2s)"

    # Zapier API Errors
    - alert: ZapierAPIErrors
      expr: rate(zapier_api_errors_total[5m]) > 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "Zapier API errors detected"
        description: "Zapier API errors: {{ $value }} in last 5 minutes"

    # High Zapier API Latency
    - alert: ZapierAPIHighLatency
      expr: zapier_api_latency_seconds > 5
      for: 2m
      labels:
        severity: warning
      annotations:
        summary: "High Zapier API latency"
        description: "Zapier API latency is {{ $value }}s (threshold: 5s)"

    # Down (No Requests)
    - alert: NoRequests
      expr: rate(musgo_os_requests_total[5m]) == 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "No requests to MusGo-OS"
        description: "No requests received in last 5 minutes"
```

---
##### **2. Konfigurasi Alertmanager**
**Contoh File (`prometheus/alertmanager.yml`):**
```yaml
global:
  resolve_timeout: 5m
  slack_api_url: "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"

route:
  group_by: ["alertname", "severity"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h
  receiver: "slack-notifications"
  routes:
    - match:
        severity: critical
      receiver: "slack-critical"
    - match:
        severity: warning
      receiver: "slack-warning"

receivers:
- name: "slack-notifications"
  slack_configs:
    - channel: "#musgo-os-alerts"
      send_resolved: true
      title: "{{ .CommonAnnotations.summary }}"
      text: "{{ .CommonAnnotations.description }}"
      icon_emoji: ":bell:"
      color: "{{ if eq .Status \"firing\" }}danger{{ else }}good{{ end }}"

- name: "slack-critical"
  slack_configs:
    - channel: "#musgo-os-critical"
      send_resolved: true
      title: "[CRITICAL] {{ .CommonAnnotations.summary }}"
      text: "{{ .CommonAnnotations.description }}"
      icon_emoji: ":fire:"
      color: "danger"

- name: "slack-warning"
  slack_configs:
    - channel: "#musgo-os-warnings"
      send_resolved: true
      title: "[WARNING] {{ .CommonAnnotations.summary }}"
      text: "{{ .CommonAnnotations.description }}"
      icon_emoji: ":warning:"
      color: "warning"
```

---
##### **3. Docker Compose untuk Alertmanager**
```yaml
# File: docker-compose.monitoring.yml (lanjutan)
services:
  # Alertmanager
  alertmanager:
    image: prom/alertmanager:latest
    container_name: alertmanager
    ports:
      - "9093:9093"
    volumes:
      - ./prometheus/alertmanager.yml:/etc/alertmanager/alertmanager.yml
    command:
      - "--config.file=/etc/alertmanager/alertmanager.yml"
      - "--storage.path=/alertmanager"
    networks:
      - musgo-os-network
    restart: unless-stopped
```

---
##### **4. Update Prometheus untuk Alertmanager**
**Update `prometheus.yml`:**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager:9093

rule_files:
  - "alert.rules"

scrape_configs:
  - job_name: "musgo-os"
    static_configs:
      - targets: ["backend:8001"]
  - job_name: "zapier-exporter"
    static_configs:
      - targets: ["zapier-exporter:9090"]
```

---
##### **5. Contoh Alert di Slack**
**Format Pesan:**
```
[CRITICAL] High error rate on MusGo-OS
Error rate is 0.15 (threshold: 10%)
```
**Tombol:**
- **View in Grafana**: Link ke dashboard.
- **View in Prometheus**: Link ke query.

---
---
---

## **🔹 10.6 Dashboard (Visualisasi Data)**
### **📌 Penjelasan**
**Dashboard** adalah **visualisasi data** (metrics, logs, traces) untuk **memantau performa** dan **mendeteksi masalah**.

**Tools:**
- **Grafana**: Dashboard untuk metrics, logs, traces.
- **Kibana**: Dashboard untuk logs (ELK Stack).

---
#### **🚀 Contoh Implementasi: Dashboard**
##### **1. Dashboard MusGo-OS (Grafana)**
**Contoh Dashboard JSON (untuk import ke Grafana):**
```json
{
  "title": "MusGo-OS Overview",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(musgo_os_requests_total[1m])",
          "legendFormat": "{{method}} {{path}}"
        }
      ],
      "yaxes": [
        { "format": "reqps", "label": "Requests" }
      ]
    },
    {
      "title": "Error Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(musgo_os_request_errors_total[1m])",
          "legendFormat": "{{method}} {{path}}"
        }
      ],
      "yaxes": [
        { "format": "reqps", "label": "Errors" }
      ]
    },
    {
      "title": "Latency (P99)",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.99, sum(rate(musgo_os_request_latency_seconds_bucket[5m])) by (le))",
          "legendFormat": "{{method}} {{path}}"
        }
      ],
      "yaxes": [
        { "format": "s", "label": "Seconds" }
      ]
    },
    {
      "title": "Active Users",
      "type": "gauge",
      "targets": [
        {
          "expr": "musgo_os_active_users",
          "legendFormat": "Active Users"
        }
      ],
      "thresholds": [
        { "color": "green", "value": null },
        { "color": "orange", "value": 100 },
        { "color": "red", "value": 200 }
      ]
    },
    {
      "title": "Zapier API Calls",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(zapier_api_calls_total[1m])",
          "legendFormat": "{{endpoint}}"
        }
      ],
      "yaxes": [
        { "format": "reqps", "label": "Calls" }
      ]
    },
    {
      "title": "Zapier API Latency",
      "type": "graph",
      "targets": [
        {
          "expr": "zapier_api_latency_seconds",
          "legendFormat": "{{endpoint}}"
        }
      ],
      "yaxes": [
        { "format": "s", "label": "Seconds" }
      ]
    },
    {
      "title": "Zaps per User",
      "type": "table",
      "targets": [
        {
          "expr": "zapier_zaps_count",
          "format": "table",
          "instant": true
        }
      ],
      "transformations": [
        { "id": "organize", "options": { "excludeByName": {}, "indexByName": {}, "renameByName": {} } }
      ]
    },
    {
      "title": "Logs",
      "type": "logs",
      "targets": [
        {
          "expr": "{job=\"musgo-os\"}",
          "datasource": "Loki"
        }
      ],
      "options": {
        "showLabels": true,
        "showTime": true,
        "wrapLogMessage": true,
        "prettifyLogMessage": false,
        "enableLogDetails": true
      }
    }
  ],
  "templating": {
    "list": [
      {
        "name": "service",
        "query": "label_values(musgo_os_requests_total, service)"
      }
    ]
  }
}
```

---
##### **2. Import Dashboard ke Grafana**
1. Buka **Grafana** (`http://localhost:3000`).
2. Klik **Dashboards** → **Import**.
3. **Upload JSON file** atau **paste JSON**.
4. Pilih **Data Sources** (Prometheus, Loki, Jaeger).
5. Klik **Import**.

---
##### **3. Dashboard Zapier-Specific**
**Contoh Panel untuk Zapier:**
| Panel | Query | Deskripsi |
|-------|-------|-----------|
| **Zapier API Calls** | `rate(zapier_api_calls_total[1m])` | Jumlah panggilan API per menit |
| **Zapier API Errors** | `rate(zapier_api_errors_total[1m])` | Jumlah error API per menit |
| **Zapier API Latency** | `zapier_api_latency_seconds` | Latency API (detik) |
| **Zaps Count** | `zapier_zaps_count` | Jumlah Zap per user |
| **Zapier Action Success Rate** | `sum(rate(zapier_api_calls_total{status_code=~"2.."}[1m])) / sum(rate(zapier_api_calls_total[1m]))` | Persentase success |
| **Top Zapier Endpoints** | `topk(5, rate(zapier_api_calls_total[1m]))` | 5 endpoint paling sering dipanggil |

---
---
---

## **🔹 10.7 Error Tracking (Pelacakan Error)**
### **📌 Penjelasan**
**Error Tracking** adalah **sistem untuk mencatat, mengelompokkan, dan menganalisis error** di aplikasi. Digunakan untuk:
- **Cepat temukan error** (dengan stack trace, environment, dll.).
- **Group error** (misal: 100 error dengan penyebab yang sama).
- **Assign error** ke developer.

**Tools:**
- **Sentry**: Error tracking terpopuler.
- **Rollbar**: Alternatif untuk Sentry.

---
#### **🚀 Contoh Implementasi: Sentry**
##### **1. Setup Sentry untuk Backend (Python)**
```python
# File: backend/sentry.py
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

def setup_sentry(dsn: str, environment: str = "production"):
    """Setup Sentry untuk error tracking"""
    sentry_logging = LoggingIntegration(
        level=logging.INFO,        # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )

    sentry_sdk.init(
        dsn=dsn,
        integrations=[
            FastApiIntegration(),
            sentry_logging,
            RedisIntegration(),
            SqlalchemyIntegration(),
        ],
        traces_sample_rate=1.0,  # Performance monitoring
        environment=environment,
        release="musgo-os@1.0.0",
    )

# Setup Sentry
setup_sentry(dsn="YOUR_SENTRY_DSN")
```

---
##### **2. Middleware untuk Sentry (FastAPI)**
```python
# File: backend/middlewares.py (lanjutan)
from sentry_sdk import Hub, capture_exception
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

# Tambahkan middleware ke FastAPI
app.add_middleware(SentryAsgiMiddleware)

async def sentry_middleware(request: Request, call_next):
    """Middleware untuk Sentry"""
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Capture exception ke Sentry
        with Hub.current:
            capture_exception(e)
        raise
```

---
##### **3. Setup Sentry untuk Frontend (React)**
```bash
npm install @sentry/react @sentry/tracing
```

```tsx
// File: frontend/src/sentry.ts
import * as Sentry from "@sentry/react";
import { Integrations } from "@sentry/tracing";

Sentry.init({
  dsn: "YOUR_SENTRY_DSN",
  integrations: [
    new Integrations.BrowserTracing(),
  ],
  tracesSampleRate: 1.0,  // Performance monitoring
  environment: process.env.NODE_ENV,
  release: "musgo-os@1.0.0",
});
```

---
##### **4. Integrasi Sentry dengan React Router**
```tsx
// File: frontend/src/index.tsx
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import * as Sentry from "@sentry/react";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Sentry.ErrorBoundary fallback={<div>Error occurred</div>}>
        <App />
      </Sentry.ErrorBoundary>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
```

---
##### **5. Contoh Error di Sentry**
**Data yang Terekam:**
- **Error Message**: `KeyError: 'file_url'`
- **Stack Trace**: Lokasi error di kode.
- **Environment**: `production`
- **Release**: `musgo-os@1.0.0`
- **Tags**: `method=POST`, `path=/api/zapier/ai-analyze`
- **Breadcrumbs**: Aktivitas sebelum error (misal: request diterima, database query).
- **User**: `dhani@musgo-os.com` (jika terautentikasi).

**Fitur Sentry:**
- **Grouping**: 100 error yang sama digabungkan.
- **Assign**: Assign error ke developer.
- **Resolve**: Tandai error sebagai fixed.
- **Alerts**: Kirim notifikasi ke Slack/Email jika error baru muncul.

---
---
---

## **🔹 10.8 Business Metrics (Metrik Bisnis)**
### **📌 Penjelasan**
**Business Metrics** adalah **metrik yang berkaitan dengan bisnis**, seperti:
- **Jumlah User Aktif**.
- **Jumlah Zap yang Dibuat**.
- **Jumlah Otomatisasi yang Berjalan**.
- **ROI (Return on Investment)** dari integrasi Zapier.

**Manfaat untuk MusGo-OS:**
- **Pahami penggunaan** integrasi Zapier.
- **Ukur kesuksesan** fitur otomatisasi.
- **Optimalkan monetisasi** (misal: premium features).

---
#### **🚀 Contoh Implementasi: Business Metrics**
##### **1. Backend MusGo-OS (Python - Prometheus)**
```python
# File: backend/metrics.py (lanjutan)
from prometheus_client import Counter, Gauge, Histogram

# Business Metrics
USER_SIGNUPS = Counter(
    "musgo_os_user_signups_total",
    "Total User Signups",
    ["source"]  # Misal: "organic", "referral", "ads"
)

ZAPS_CREATED = Counter(
    "musgo_os_zaps_created_total",
    "Total Zaps Created",
    ["user_id", "trigger_app", "action_app"]
)

ZAPS_RUN = Counter(
    "musgo_os_zaps_run_total",
    "Total Zaps Run",
    ["user_id", "zap_id"]
)

ACTIVE_ZAPS = Gauge(
    "musgo_os_active_zaps",
    "Number of Active Zaps",
    ["user_id"]
)

PREMIUM_USERS = Gauge(
    "musgo_os_premium_users",
    "Number of Premium Users"
)

REVENUE = Gauge(
    "musgo_os_revenue_usd",
    "Total Revenue (USD)"
)

# Contoh penggunaan
def track_user_signup(user_id: str, source: str = "organic"):
    """Track user signup"""
    USER_SIGNUPS.labels(source=source).inc()

def track_zap_created(user_id: str, trigger_app: str, action_app: str):
    """Track Zap creation"""
    ZAPS_CREATED.labels(user_id=user_id, trigger_app=trigger_app, action_app=action_app).inc()
    ACTIVE_ZAPS.labels(user_id=user_id).inc()

def track_zap_run(user_id: str, zap_id: str):
    """Track Zap run"""
    ZAPS_RUN.labels(user_id=user_id, zap_id=zap_id).inc()

def track_premium_user(user_id: str, is_premium: bool):
    """Track premium user status"""
    if is_premium:
        PREMIUM_USERS.inc()
    else:
        PREMIUM_USERS.dec()

def track_revenue(amount: float):
    """Track revenue"""
    REVENUE.inc(amount)
```

---
##### **2. Dashboard Business Metrics (Grafana)**
| Panel | Query | Deskripsi |
|-------|-------|-----------|
| **User Signups** | `rate(musgo_os_user_signups_total[1d])` | Jumlah signup per hari |
| **Zaps Created** | `rate(musgo_os_zaps_created_total[1d])` | Jumlah Zap dibuat per hari |
| **Zaps Run** | `rate(musgo_os_zaps_run_total[1d])` | Jumlah Zap berjalan per hari |
| **Active Zaps** | `musgo_os_active_zaps` | Jumlah Zap aktif |
| **Premium Users** | `musgo_os_premium_users` | Jumlah user premium |
| **Revenue** | `musgo_os_revenue_usd` | Total revenue (USD) |
| **Top Trigger Apps** | `topk(5, sum(rate(musgo_os_zaps_created_total[1d])) by (trigger_app))` | 5 trigger app paling populer |
| **Top Action Apps** | `topk(5, sum(rate(musgo_os_zaps_created_total[1d])) by (action_app))` | 5 action app paling populer |
| **Zaps per User** | `sum(musgo_os_zaps_created_total) by (user_id)` | Jumlah Zap per user |

---
##### **3. Alert untuk Business Metrics**
**Contoh Alert Rules:**
```yaml
groups:
- name: business-metrics-alerts
  rules:
    # Penurunan Signup
    - alert: UserSignupsDrop
      expr: rate(musgo_os_user_signups_total[1d]) < 10
      for: 1d
      labels:
        severity: warning
      annotations:
        summary: "Penurunan user signups"
        description: "User signups turun di bawah 10 per hari (saat ini: {{ $value }})"

    # Penurunan Zap Creation
    - alert: ZapCreationDrop
      expr: rate(musgo_os_zaps_created_total[1d]) < 50
      for: 1d
      labels:
        severity: warning
      annotations:
        summary: "Penurunan pembuatan Zap"
        description: "Zap creation turun di bawah 50 per hari (saat ini: {{ $value }})"

    # Penurunan Revenue
    - alert: RevenueDrop
      expr: musgo_os_revenue_usd < 1000
      for: 1d
      labels:
        severity: critical
      annotations:
        summary: "Penurunan revenue"
        description: "Revenue turun di bawah $1000 (saat ini: ${{ $value }})"
```

---
---
---

## **🔹 10.9 Synthetic Monitoring (Pemantauan Sintetis)**
### **📌 Penjelasan**
**Synthetic Monitoring** adalah **pemantauan dengan request buatan** untuk:
- **Cek apakah sistem berjalan** (uptime monitoring).
- **Ukur performa** dari berbagai lokasi.
- **Deteksi masalah** sebelum user melaporkan.

**Tools:**
- **Grafana Synthetic Monitoring**.
- **Prometheus Blackbox Exporter**.
- **UptimeRobot**.

---
#### **🚀 Contoh Implementasi: Synthetic Monitoring**
##### **1. Blackbox Exporter (Prometheus)**
**Blackbox Exporter** memungkinkan **Prometheus untuk memantau endpoint** (HTTP, TCP, DNS, dll.).

**Docker Compose:**
```yaml
# File: docker-compose.monitoring.yml (lanjutan)
services:
  # Blackbox Exporter
  blackbox-exporter:
    image: prometheus/blackbox-exporter:latest
    container_name: blackbox-exporter
    ports:
      - "9115:9115"
    networks:
      - musgo-os-network
    restart: unless-stopped
```

---
##### **2. Konfigurasi Prometheus untuk Blackbox**
**Update `prometheus.yml`:**
```yaml
scrape_configs:
  - job_name: "blackbox"
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
          - http://backend:8000/health
          - http://frontend:3000/health
          - https://api.zapier.com/v2/zaps
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
```

**Konfigurasi Module (`blackbox.yml`):**
```yaml
modules:
  http_2xx:
    prober: http
    http:
      preferred_ip_protocol: "ip4"
      valid_status_codes: [200, 301, 302]
      no_follow_redirects: false
  http_post_2xx:
    prober: http
    http:
      method: POST
      headers:
        Content-Type: "application/json"
      body: '{"app": "slack", "action": "Send Channel Message", "data": {"channel": "#test"}}'
      valid_status_codes: [200]
```

---
##### **3. Alert untuk Uptime Monitoring**
**Contoh Alert Rules:**
```yaml
groups:
- name: uptime-alerts
  rules:
    # Backend Down
    - alert: BackendDown
      expr: up{job="blackbox", instance=~"http://backend:8000/health"} == 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "Backend MusGo-OS down"
        description: "Backend tidak merespons (instance: {{ $labels.instance }})"

    # Frontend Down
    - alert: FrontendDown
      expr: up{job="blackbox", instance=~"http://frontend:3000/health"} == 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "Frontend MusGo-OS down"
        description: "Frontend tidak merespons (instance: {{ $labels.instance }})"

    # Zapier API Down
    - alert: ZapierAPIDown
      expr: up{job="blackbox", instance=~"https://api.zapier.com/v2/zaps"} == 0
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Zapier API down"
        description: "Zapier API tidak merespons"
```

---
---
---

## **🔹 10.10 Log Retention & Archiving (Penyimpanan Log)**
### **📌 Penjelasan**
**Log Retention & Archiving** adalah **strategi penyimpanan log** untuk:
- **Patuhi regulasi** (misal: GDPR mengharuskan log disimpan 1 tahun).
- **Hemat biaya** (log lama disimpan di storage murah).
- **Mudah diakses** (untuk investigasi).

**Strategi:**
- **Hot Storage**: Log **1-7 hari** (disimpan di Loki/Elasticsearch).
- **Warm Storage**: Log **7-30 hari** (disimpan di S3/MinIO).
- **Cold Storage**: Log **>30 hari** (disimpan di Glacier/Archive).

---
#### **🚀 Contoh Implementasi: Log Retention**
##### **1. Loki (Grafana Loki)**
**Konfigurasi Retention di Loki (`loki-config.yaml`):**
```yaml
limits_config:
  retention_period: 720h  # 30 hari
  retention_stream:
    - selector: '{job="musgo-os"}'
      priority: 1
      period: 168h  # 7 hari (hot storage)
    - selector: '{job="musgo-os"}'
      priority: 2
      period: 720h  # 30 hari (warm storage)
```

---
##### **2. Promtail (Untuk Archiving ke S3)**
**Konfigurasi Promtail (`promtail/config.yml`):**
```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: musgo-os
    static_configs:
      - targets:
          - localhost
        labels:
          job: musgo-os
          __path__: /var/log/musgo-os/*.log
    pipeline_stages:
      - json:
          expressions:
            level: level
            message: msg
      - labels:
          level:
      - match:
          selector: '{job="musgo-os", level="error"}'
          stages:
            - output:
                source: message
                destination: error_message
      # Archive ke S3 (untuk log lama)
      - remote_write:
          endpoint: http://minio:9000
          bucket: musgo-os-logs
          region: us-east-1
          access_key_id: YOUR_MINIO_ACCESS_KEY
          secret_access_key: YOUR_MINIO_SECRET_KEY
          flush_interval: 5m
          queue_size: 1000
```

---
##### **3. MinIO (S3-Compatible Storage)**
**Docker Compose untuk MinIO:**
```yaml
# File: docker-compose.storage.yml
version: "3.8"

services:
  minio:
    image: minio/minio:latest
    container_name: minio
    ports:
      - "9000:9000"  # API
      - "9001:9001"  # Console
    environment:
      - MINIO_ROOT_USER=admin
      - MINIO_ROOT_PASSWORD=securepassword123
    volumes:
      - minio_data:/data
    command: server /data --console-address ":9001"
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  minio_data:
```

---
##### **4. Lifecycle Policy (Untuk S3/MinIO)**
**Contoh Lifecycle Policy (XML untuk S3):**
```xml
<LifecycleConfiguration>
  <Rule>
    <ID>ArchiveOldLogs</ID>
    <Status>Enabled</Status>
    <Filter>
      <Prefix>musgo-os-logs/</Prefix>
    </Filter>
    <Transition>
      <Days>30</Days>
      <StorageClass>STANDARD_IA</StorageClass>
    </Transition>
    <Transition>
      <Days>90</Days>
      <StorageClass>GLACIER</StorageClass>
    </Transition>
    <Expiration>
      <Days>365</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

**Untuk MinIO (menggunakan `mc` CLI):**
```bash
# Set alias
mc alias set minio http://minio:9000 admin securepassword123

# Set lifecycle policy
mc lifecycle set minio/musgo-os-logs \
  '{
    "Rule": [
      {
        "ID": "ArchiveOldLogs",
        "Status": "Enabled",
        "Filter": {"Prefix": "musgo-os-logs/"},
        "Transition": [
          {"Days": 30, "StorageClass": "STANDARD_IA"},
          {"Days": 90, "StorageClass": "GLACIER"}
        ],
        "Expiration": {"Days": 365}
      }
    ]
  }'
```

---
---
---

## **🔹 10.11 Cost Optimization (Optimasi Biaya)**
### **📌 Penjelasan**
**Cost Optimization** adalah **strategi untuk mengurangi biaya** monitoring dan infrastructure tanpa **mengorbankan performa**.

**Strategi untuk MusGo-OS:**
- **Sampling**: Catat **tidak semua data** (misal: 10% dari traces).
- **Retention Policy**: Hapus **log lama** yang tidak diperlukan.
- **Downsampling**: Kurangi **resolusi metrics lama**.
- **Cold Storage**: Simpan **data lama** di storage murah.

---
#### **🚀 Contoh Implementasi: Cost Optimization**
##### **1. Sampling untuk Tracing (OpenTelemetry)**
```python
# File: backend/tracing.py (lanjutan)
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.sampling import ParentBasedTraceIdRatio, TraceIdRatioBased

# Sampling: Catat 10% dari traces
sampler = ParentBasedTraceIdRatio(
    TraceIdRatioBased(0.1)  # 10% sampling rate
)

provider = TracerProvider(sampler=sampler)
```

---
##### **2. Downsampling untuk Metrics (Prometheus)**
**Konfigurasi Downsampling di Prometheus (`prometheus.yml`):**
```yaml
# Downsample metrics lama
remote_write:
  - url: "http://thanos:9090/api/v1/receive"
    write_relabel_configs:
      - source_labels: [__name__]
        regex: 'musgo_os_requests_total|musgo_os_request_latency_seconds'
        action: keep
    # Downsample metrics > 1 hari ke 5 menit
    queue_config:
      max_samples_per_send: 1000
      max_shards: 100
    remote_timeout: 30s
```

---
##### **3. Retention Policy (Prometheus + Thanos)**
**Thanos** adalah **sistem untuk long-term storage** metrics Prometheus.

**Docker Compose untuk Thanos:**
```yaml
# File: docker-compose.monitoring.yml (lanjutan)
services:
  # Thanos Sidecar (untuk Prometheus)
  thanos-sidecar:
    image: thanosio/thanos:v0.32.0
    container_name: thanos-sidecar
    volumes:
      - ./thanos:/etc/thanos
      - prometheus_data:/prometheus
    command:
      - "sidecar"
      - "--prometheus.url=http://prometheus:9090"
      - "--tsdb.path=/prometheus"
      - "--objstore.config-file=/etc/thanos/objstore.yml"
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Thanos Store (untuk query)
  thanos-store:
    image: thanosio/thanos:v0.32.0
    container_name: thanos-store
    volumes:
      - ./thanos:/etc/thanos
    command:
      - "store"
      - "--objstore.config-file=/etc/thanos/objstore.yml"
      - "--index-cache-size=1GB"
      - "--chunk-pool-size=2GB"
    ports:
      - "10901:10901"  # HTTP
      - "10902:10902"  # gRPC
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Thanos Query (untuk Grafana)
  thanos-query:
    image: thanosio/thanos:v0.32.0
    container_name: thanos-query
    volumes:
      - ./thanos:/etc/thanos
    command:
      - "query"
      - "--store=thanos-store:10901"
      - "--store=thanos-sidecar:10901"
      - "--http-address=0.0.0.0:9090"
    ports:
      - "9090:9090"
    networks:
      - musgo-os-network
    restart: unless-stopped
```

**Konfigurasi Objstore (`thanos/objstore.yml`):**
```yaml
type: S3
config:
  bucket: "musgo-os-metrics"
  endpoint: "minio:9000"
  access_key: "admin"
  secret_key: "securepassword123"
  insecure: true
```

---
##### **4. Retention Policy di Thanos**
**Konfigurasi Retention di Thanos (`thanos/compact.yml`):**
```yaml
# Compact metrics lama
type: S3
config:
  bucket: "musgo-os-metrics"
  endpoint: "minio:9000"
  access_key: "admin"
  secret_key: "securepassword123"
  insecure: true
  retention: 30d  # Simpan 30 hari
```

---
##### **5. Biaya Monitoring (Perbandingan Tools)**
| Tool | Biaya (Bulanan) | Fitur | Rekomendasi untuk MusGo-OS |
|------|-----------------|-------|-----------------------------|
| **Prometheus + Grafana** | Gratis (self-hosted) | Metrics, Alerting, Dashboard | ✅ **Rekomendasi** (untuk production) |
| **Loki + Grafana** | Gratis (self-hosted) | Logging | ✅ **Rekomendasi** |
| **Jaeger** | Gratis (self-hosted) | Tracing | ✅ **Rekomendasi** |
| **Sentry** | Gratis (25K events/bulan) | Error Tracking | ✅ **Rekomendasi** |
| **Datadog** | $15/host + $0.20/GB logs | Full-stack monitoring | ⚠️ **Jika budget cukup** |
| **New Relic** | $49/bulan | Full-stack monitoring | ⚠️ **Jika budget cukup** |
| **AWS CloudWatch** | Pay-as-you-go | Metrics, Logging, Alerting | ❌ **Mahal untuk skala besar** |

---
---
---
# **📌 PART 10: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 10 (Monitoring & Analytics)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **Logging** | Structured Logging, Loki | Debugging, Audit | ✅ **Contoh kode tersedia** |
| **Metrics** | Prometheus, Grafana | Performa, Alerting | ✅ **Contoh kode tersedia** |
| **Tracing** | OpenTelemetry, Jaeger | Debugging, Latency | ✅ **Contoh kode tersedia** |
| **Alerting** | Alertmanager, Slack | Notifikasi masalah | ✅ **Contoh kode tersedia** |
| **Dashboard** | Grafana | Visualisasi data | ✅ **Contoh kode tersedia** |
| **Error Tracking** | Sentry | Pelacakan error | ✅ **Contoh kode tersedia** |
| **Business Metrics** | Prometheus | Metrik bisnis | ✅ **Contoh kode tersedia** |
| **Synthetic Monitoring** | Blackbox Exporter | Uptime monitoring | ✅ **Contoh kode tersedia** |
| **Log Retention** | Loki, MinIO | Penyimpanan log | ✅ **Contoh kode tersedia** |
| **Cost Optimization** | Sampling, Downsampling | Hemat biaya | ✅ **Contoh kode tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Setup Logging** (Structured Logging + Loki).
- [ ] **Setup Metrics** (Prometheus + Grafana).
- [ ] **Setup Alerting** (Alertmanager + Slack).
- [ ] **Buat Dashboard** (Grafana).
- [ ] **Integrasi Sentry** (Error Tracking).

### **2. Mid-Term (1 Bulan)**
- [ ] **Setup Tracing** (OpenTelemetry + Jaeger).
- [ ] **Setup Synthetic Monitoring** (Blackbox Exporter).
- [ ] **Implementasi Business Metrics**.
- [ ] **Setup Log Retention** (Loki + MinIO).
- [ ] **Optimasi Biaya** (Sampling, Downsampling).

### **3. Long-Term (3+ Bulan)**
- [ ] **Monitoring Full-Stack** (Frontend + Backend + Zapier).
- [ ] **Automasi Alerting** (Auto-resolve, Escalation).
- [ ] **Machine Learning untuk Anomali Detection**.
- [ ] **SLA Monitoring** (Uptime, Latency, dll.).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 11: Incident Response** (Untuk penanganan insiden)
   - [ ] **Part 12: Disaster Recovery** (Untuk pemulihan bencana)
   - [ ] **Part 13: Performance Optimization** (Untuk optimasi performa)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full setup monitoring untuk production)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full Docker Compose untuk Monitoring Stack**?
   - [ ] **Konfigurasi Lengkap untuk Prometheus + Grafana + Loki + Jaeger**?
   - [ ] **Panduan Deployment Monitoring ke Kubernetes**?

3. **Apakah ada area monitoring spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Logging**, **Metrics**, **Tracing**, **Alerting**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 11: Incident Response** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **penanganan insiden (Incident Response)** di **MusGo-OS 2in1 + Zapier**, termasuk **prosedur, playbook, eskalasi, dan post-mortem**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN INCIDENT RESPONSE (PART 11)**
*Terjemahan + Implementasi untuk Penanganan Insiden Production-Ready*

---

---

## **🔹 11.1 Overview Incident Response**
### **📌 Penjelasan (Bahasa Indonesia)**
**Incident Response** adalah **proses terstruktur** untuk **mengidentifikasi, menanggapi, dan memulihkan** dari **insiden keamanan, kegagalan sistem, atau gangguan layanan** di **MusGo-OS + Zapier**. Tujuannya:
✅ **Minimalkan Dampak**: Kurangi **downtime** dan **kerugian bisnis**.
✅ **Cepat Pulih**: Kembalikan **sistem ke keadaan normal** secepat mungkin.
✅ **Pelajari dari Insiden**: **Analisis root cause** dan **perbaiki untuk masa depan**.
✅ **Patuhi Regulasi**: Lapor insiden ke **otoritas** (jika diperlukan, misal: GDPR).

**Jenis Insiden untuk MusGo-OS:**
| Jenis Insiden | Contoh | Dampak | Severity |
|---------------|--------|--------|----------|
| **Outage** | MusGo-OS Backend down | User tidak bisa menggunakan sistem | **Critical (SEV-1)** |
| **Zapier API Down** | Zapier API tidak merespons | Otomatisasi terhenti | **High (SEV-2)** |
| **Data Breach** | User data bocor | Kerugian reputasi, denda GDPR | **Critical (SEV-1)** |
| **Performance Degradation** | Latency > 5 detik | User experience buruk | **Medium (SEV-3)** |
| **Security Vulnerability** | SQL Injection ditemukan | Risiko serangan | **High (SEV-2)** |
| **Rate Limit Exceeded** | Terlalu banyak panggilan Zapier API | Otomatisasi gagal | **Medium (SEV-3)** |
| **Authentication Failure** | User tidak bisa login | User tidak bisa akses | **High (SEV-2)** |

---
### **🚀 Contoh Arsitektur Incident Response untuk MusGo-OS**
```
Insiden Terjadi → [Deteksi] → [Triage] → [Eskalasi] → [Mitigasi] → [Pemulihan] → [Post-Mortem]
       ↓
[Monitoring (Prometheus, Sentry, Loki)] → [Alert (Slack, PagerDuty)] → [On-Call Team]
       ↓
[Playbook] → [Runbook] → [Komunikasi (Status Page, Email)]
```

---
---
---

## **🔹 11.2 Incident Response Plan (Rencana Penanganan Insiden)**
### **📌 Penjelasan**
**Incident Response Plan (IRP)** adalah **dokumen yang mendefinisikan**:
- **Peran dan tanggung jawab** (siapa yang bertanggung jawab).
- **Prosedur penanganan insiden** (langkah-langkah).
- **Klasifikasi severity** (SEV-1, SEV-2, dll.).
- **Komunikasi** (siapa yang perlu diinformasikan).
- **Escalation path** (kapan dan ke siapa eskalasi).

---
#### **🚀 Contoh Implementasi: Incident Response Plan**
##### **1. Dokumen IRP (Markdown)**
```markdown
# 🚨 MusGo-OS 2in1: Incident Response Plan (IRP)
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan (CTO)

---

## 📌 1. Tujuan
Dokumen ini mendefinisikan **prosedur penanganan insiden** untuk **MusGo-OS 2in1 + Zapier**, termasuk:
- Deteksi dan triage insiden.
- Eskalasi dan mitigasi.
- Pemulihan dan post-mortem.

---

## 📌 2. Peran dan Tanggung Jawab
| Peran | Tanggung Jawab | Kontak |
|-------|----------------|--------|
| **Incident Commander** | Memimpin penanganan insiden, koordinasi tim | @dhani (Slack) |
| **On-Call Engineer** | Menangani insiden secara teknis | Rotasi tim engineering |
| **Security Lead** | Menangani insiden keamanan (data breach, vulnerability) | @security-team |
| **Support Lead** | Komunikasi dengan user, update status | @support-team |
| **Product Owner** | Keputusan bisnis (misal: rollback, feature disable) | @product-team |
| **Executive Sponsor** | Eskalasi ke manajemen (jika diperlukan) | @ceo |

---

## 📌 3. Klasifikasi Severity
| Severity | Deskripsi | Dampak | SLA (Response Time) | SLA (Resolution Time) |
|----------|-----------|--------|---------------------|-----------------------|
| **SEV-1 (Critical)** | Sistem **tidak berfungsi**, data breach, outage total | User tidak bisa menggunakan MusGo-OS | **15 menit** | **1 jam** |
| **SEV-2 (High)** | Fitur **kritis terganggu**, Zapier API down, security vulnerability | Otomatisasi terhenti, risiko keamanan | **30 menit** | **4 jam** |
| **SEV-3 (Medium)** | **Performance degradation**, error rate tinggi, rate limit | User experience buruk | **1 jam** | **24 jam** |
| **SEV-4 (Low)** | **Bug minor**, warning di log | Tidak mempengaruhi user | **4 jam** | **7 hari** |

---

## 📌 4. Prosedur Penanganan Insiden
### 4.1 Deteksi
- **Sumber Deteksi:**
  - **Monitoring** (Prometheus, Grafana, Sentry).
  - **Alert** (Alertmanager, PagerDuty).
  - **User Report** (Slack, Email, Support Ticket).
  - **Zapier Status Page** ([status.zapier.com](https://status.zapier.com/)).

- **Aksi:**
  - **Verifikasi insiden** (apakah benar terjadi?).
  - **Klasifikasikan severity** (SEV-1, SEV-2, dll.).
  - **Buat Incident Ticket** (di Jira/Linear).

### 4.2 Triage
- **Identifikasi:**
  - **Apa yang terjadi?** (Outage? Error? Performance issue?).
  - **Kapan dimulai?** (Timestamp).
  - **Siapa yang terpengaruh?** (User? Fitur?).
  - **Scope?** (1 user? Semua user?).

- **Aksi:**
  - **Cek monitoring dashboard** (Grafana).
  - **Cek log** (Loki, Sentry).
  - **Cek status Zapier** ([status.zapier.com](https://status.zapier.com/)).
  - **Cek dependency** (Database, Redis, dll.).

### 4.3 Eskalasi
- **SEV-1/SEV-2:**
  - **Bangunkan On-Call Engineer** (via PagerDuty).
  - **Notifikasi Incident Commander** (via Slack/Call).
  - **Buat War Room** (Slack Channel `#incident-sev1`).
- **SEV-3/SEV-4:**
  - **Notifikasi tim engineering** (via Slack).
  - **Buat ticket** (Jira/Linear).

### 4.4 Mitigasi
- **Gunakan Playbook** (lihat [Bagian 11.3](#113-playbooks)).
- **Jalankan Runbook** (lihat [Bagian 11.4](#114-runbooks)).
- **Komunikasikan Status** (via Status Page, Slack).
- **Update Incident Ticket** (setiap 15-30 menit).

### 4.5 Pemulihan
- **Verifikasi solusi** (apakah insiden teratasi?).
- **Monitor sistem** (apakah stabil?).
- **Rollback** (jika solusi tidak bekerja).
- **Update user** (via Status Page, Email).

### 4.6 Post-Mortem
- **Lakukan dalam 24 jam** (untuk SEV-1/SEV-2).
- **Identifikasi root cause**.
- **Buat action items** (perbaikan, pencegahan).
- **Share dengan tim** (untuk belajar dari insiden).

---

## 📌 5. Komunikasi
### 5.1 Internal (Tim)
| Severity | Channel | Frekuensi Update |
|----------|---------|------------------|
| SEV-1 | `#incident-sev1` (Slack) + PagerDuty | Setiap 15 menit |
| SEV-2 | `#incident-sev2` (Slack) | Setiap 30 menit |
| SEV-3 | `#incident-sev3` (Slack) | Setiap 1 jam |
| SEV-4 | Ticket (Jira/Linear) | Setiap 24 jam |

### 5.2 Eksternal (User)
| Severity | Channel | Frekuensi Update |
|----------|---------|------------------|
| SEV-1 | Status Page + Email | Setiap 30 menit |
| SEV-2 | Status Page | Setiap 1 jam |
| SEV-3 | Status Page | Setiap 4 jam |
| SEV-4 | - | - |

---
## 📌 6. Escalation Path
| Severity | Waktu Tanpa Progress | Eskalasi Ke |
|----------|----------------------|-------------|
| SEV-1 | 15 menit | Incident Commander → Executive Sponsor |
| SEV-2 | 1 jam | On-Call Engineer → Incident Commander |
| SEV-3 | 4 jam | On-Call Engineer → Team Lead |
| SEV-4 | 24 jam | Support Lead → Engineering Manager |

---
## 📌 7. Tools
| Tools | Kegunaan | Link |
|-------|----------|------|
| **Slack** | Komunikasi tim | [musgo-os.slack.com](https://musgo-os.slack.com) |
| **PagerDuty** | On-Call Management | [musgo-os.pagerduty.com](https://musgo-os.pagerduty.com) |
| **Jira** | Incident Ticket | [musgo-os.atlassian.net](https://musgo-os.atlassian.net) |
| **Grafana** | Monitoring Dashboard | [grafana.musgo-os.com](http://grafana.musgo-os.com) |
| **Sentry** | Error Tracking | [sentry.musgo-os.com](https://sentry.musgo-os.com) |
| **Status Page** | Komunikasi User | [status.musgo-os.com](https://status.musgo-os.com) |
| **Zapier Status** | Status Zapier API | [status.zapier.com](https://status.zapier.com) |

---
## 📌 8. Kontak Darurat
| Kontak | Peran | Telepon | Email |
|--------|-------|---------|-------|
| Dhani Yuliawan | CTO / Incident Commander | +62 813-6552-283 | dhani@musgo-os.com |
| Tim Engineering | On-Call Engineer | - | engineering@musgo-os.com |
| Tim Security | Security Lead | - | security@musgo-os.com |
| Tim Support | Support Lead | - | support@musgo-os.com |
```

---
---
---

## **🔹 11.3 Playbooks (Buku Panduan Penanganan Insiden)**
### **📌 Penjelasan**
**Playbook** adalah **dokumen yang mendefinisikan langkah-langkah** untuk **menangani jenis insiden tertentu**. Setiap playbook berisi:
- **Deskripsi insiden**.
- **Severity**.
- **Deteksi** (bagaimana mendeteksi insiden).
- **Mitigasi** (langkah-langkah untuk mengatasi).
- **Pemulihan** (langkah-langkah untuk memulihkan).
- **Post-Mortem** (analisis root cause).

---
#### **🚀 Contoh Implementasi: Playbooks**
##### **1. Playbook: MusGo-OS Backend Down (SEV-1)**
```markdown
# 🚨 Playbook: MusGo-OS Backend Down (SEV-1)
**ID:** PB-001
**Versi:** 1.0
**Owner:** Dhani Yuliawan

---
## 📌 Deskripsi
Backend MusGo-OS **tidak merespons** (HTTP 5xx, timeout, dll.), menyebabkan **user tidak bisa menggunakan sistem**.

---
## 📌 Severity
**SEV-1 (Critical)**

---
## 📌 Deteksi
- **Alert:** `BackendDown` (Prometheus Alertmanager).
- **Monitoring:** Grafana dashboard menunjukkan **0 requests** ke backend.
- **User Report:** User melaporkan **tidak bisa login** atau **API error**.
- **Sentry:** Error `ConnectionRefusedError` atau `TimeoutError`.

---
## 📌 Mitigasi
### Langkah 1: Verifikasi Insiden
- [ ] Cek **Grafana Dashboard** (`http://grafana.musgo-os.com/d/musgo-os-backend`).
- [ ] Cek **status backend** (`http://backend.musgo-os.com/health`).
- [ ] Cek **log backend** (`kubectl logs -n musgo-os deployment/musgo-os-backend`).
- [ ] Cek **resource usage** (`kubectl top pods -n musgo-os`).

### Langkah 2: Cek Dependency
- [ ] Cek **database** (`kubectl logs -n musgo-os deployment/postgres`).
- [ ] Cek **Redis** (`kubectl logs -n musgo-os deployment/redis`).
- [ ] Cek **Zapier API** ([status.zapier.com](https://status.zapier.com/)).

### Langkah 3: Restart Pod (Jika Crash)
```bash
kubectl rollout restart deployment/musgo-os-backend -n musgo-os
```

### Langkah 4: Scale Up (Jika Overload)
```bash
kubectl scale deployment/musgo-os-backend --replicas=5 -n musgo-os
```

### Langkah 5: Rollback (Jika Deployment Baru Bermasalah)
```bash
kubectl rollout undo deployment/musgo-os-backend -n musgo-os
```

### Langkah 6: Cek Kubernetes Events
```bash
kubectl get events -n musgo-os --sort-by='.metadata.creationTimestamp'
```

### Langkah 7: Cek Node Status
```bash
kubectl describe node <node-name>
kubectl get nodes -n musgo-os
```

---
## 📌 Pemulihan
- [ ] Verifikasi **backend berjalan normal** (`http://backend.musgo-os.com/health`).
- [ ] Verifikasi **user bisa login** dan **API berfungsi**.
- [ ] Monitor **error rate** (harus < 1%).
- [ ] Monitor **latency** (harus < 1 detik).

---
## 📌 Post-Mortem
### Root Cause
- **Contoh:**
  - **Out of Memory**: Pod backend **kehabisan memory** karena memory leak.
  - **Database Down**: PostgreSQL **crash** karena query lambat.
  - **Zapier API Down**: Zapier **outage** (cek [status.zapier.com](https://status.zapier.com/)).

### Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Tambahkan **memory limit** untuk pod backend | @dhani | 2026-05-20 | ⬜ To Do |
| Optimasi **query database** ya

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 12: Disaster Recovery (DR)** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **pemulihan bencana (Disaster Recovery)** di **MusGo-OS 2in1 + Zapier**, termasuk **backup, restore, failover, dan testing DR**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN DISASTER RECOVERY (PART 12)**
*Terjemasan + Implementasi untuk Pemulihan Bencana Production-Ready*

---

---

## **🔹 12.1 Overview Disaster Recovery**
### **📌 Penjelasan (Bahasa Indonesia)**
**Disaster Recovery (DR)** adalah **proses dan prosedur** untuk **memulihkan sistem MusGo-OS + Zapier** setelah terjadinya **bencana** (misal: **server crash, data corruption, cyber attack, bencana alam**). Tujuannya:
✅ **Minimalkan Downtime**: Kembalikan sistem **secepat mungkin**.
✅ **Minimalkan Data Loss**: Pastikan **data hilang seminimal mungkin** (RPO: Recovery Point Objective).
✅ **Kembalikan ke Normal**: Sistem **berjalan seperti semula** (RTO: Recovery Time Objective).
✅ **Patuhi Compliance**: Memenuhi **regulasi** (GDPR, SOC 2, ISO 27001).

**Metrik DR:**
| Metrik | Deskripsi | Target untuk MusGo-OS |
|--------|-----------|-----------------------|
| **RTO (Recovery Time Objective)** | Waktu maksimal untuk **memulihkan sistem** | **< 1 jam (SEV-1)**, **< 4 jam (SEV-2)** |
| **RPO (Recovery Point Objective)** | Data hilang maksimal (dalam waktu) | **< 5 menit** (untuk data kritis) |
| **MTTR (Mean Time To Repair)** | Rata-rata waktu untuk **perbaiki insiden** | **< 30 menit** |
| **MTBF (Mean Time Between Failures)** | Rata-rata waktu **antara kegagalan** | **> 1 bulan** |

**Jenis Bencana untuk MusGo-OS:**
| Jenis Bencana | Contoh | Dampak | DR Strategy |
|---------------|--------|--------|-------------|
| **Hardware Failure** | Server crash, disk gagal | Downtime, data loss | **Backup + Failover** |
| **Software Bug** | Bug kritis, infinite loop | Sistem hang, crash | **Rollback + Hotfix** |
| **Human Error** | Misconfig, delete data | Data corruption | **Backup + Restore** |
| **Cyber Attack** | DDoS, ransomware | Data breach, outage | **Isolasi + Restore** |
| **Natural Disaster** | Banjir, kebakaran | Data center rusak | **Geo-Redundancy** |
| **Cloud Outage** | AWS/GCP down | Layanan terhenti | **Multi-Cloud** |
| **Zapier Outage** | Zapier API down | Otomatisasi terhenti | **Fallback Mechanism** |

---
### **🚀 Contoh Arsitektur DR untuk MusGo-OS**
```
Production (Primary)
│
├── MusGo-OS Backend (Kubernetes Cluster A)
├── MusGo-OS Frontend (Kubernetes Cluster A)
├── PostgreSQL (Primary) → [Replikasi] → PostgreSQL (Standby)
├── Redis (Primary) → [Replikasi] → Redis (Standby)
├── Zapier Integration (Primary)
│
└── Backup:
    ├── **Database**: PostgreSQL → S3 (Daily) + WAL Archiving (Continuous)
    ├── **Redis**: RDB Snapshots → S3 (Hourly)
    ├── **Kubernetes**: Etcd Snapshots → S3 (Daily)
    ├── **Code**: GitHub/GitLab (Version Control)
    ├── **Config**: Ansible/Terraform → Git (Version Control)
    ├── **Logs**: Loki → S3 (Daily)

---
Disaster (Failover)
│
├── MusGo-OS Backend (Kubernetes Cluster B - Standby)
├── MusGo-OS Frontend (Kubernetes Cluster B - Standby)
├── PostgreSQL (Standby) → [Promote] → PostgreSQL (Primary)
├── Redis (Standby) → [Promote] → Redis (Primary)
├── Zapier Integration (Fallback Mode)
│
└── Restore:
    ├── **Database**: PostgreSQL (Standby) → Promote
    ├── **Redis**: Redis (Standby) → Promote
    ├── **Kubernetes**: Restore Etcd → Cluster B
    ├── **Code**: Deploy dari Git
    ├── **Config**: Apply Ansible/Terraform
```

---
---
---

## **🔹 12.2 DR Strategy (Strategi Pemulihan Bencana)**
### **📌 Penjelasan**
**DR Strategy** adalah **pendekatan yang dipilih** untuk **memulihkan sistem** setelah bencana. Pilihan strategi tergantung pada:
- **RTO & RPO** (seberapa cepat dan seberapa banyak data yang bisa hilang).
- **Biaya** (berapa budget yang tersedia).
- **Kompleksitas** (seberapa rumit implementasinya).

**Strategi DR untuk MusGo-OS:**
| Strategi | Deskripsi | RTO | RPO | Biaya | Kompleksitas | Rekomendasi |
|----------|-----------|-----|-----|-------|--------------|--------------|
| **Backup & Restore** | Backup data secara berkala, restore jika diperlukan | 4-24 jam | 5-60 menit | Rendah | Rendah | ✅ **Untuk data non-kritis** |
| **Pilot Light** | Infrastructure standby minimal (misal: DB standby) | 1-4 jam | < 5 menit | Sedang | Sedang | ✅ **Untuk MusGo-OS** |
| **Warm Standby** | Infrastructure standby siap pakai (skala kecil) | 15-60 menit | < 1 menit | Tinggi | Tinggi | ✅ **Untuk production** |
| **Hot Standby** | Infrastructure standby penuh (skala penuh) | < 15 menit | < 1 menit | Sangat Tinggi | Sangat Tinggi | ⚠️ **Jika budget cukup** |
| **Multi-Region** | Deploy di 2+ region (misal: AWS + GCP) | < 5 menit | < 1 menit | Sangat Tinggi | Sangat Tinggi | ❌ **Untuk MusGo-OS (belum diperlukan)** |

**Pilihan untuk MusGo-OS:**
- **Pilot Light** (untuk **database dan backend**).
- **Warm Standby** (untuk **Zapier integration**).
- **Backup & Restore** (untuk **frontend dan config**).

---
---
---

## **🔹 12.3 Backup & Restore**
### **📌 Penjelasan**
**Backup & Restore** adalah **proses menyimpan data** (database, config, dll.) **secara berkala** dan **memulihkannya** jika diperlukan.

**Jenis Backup:**
| Jenis Backup | Deskripsi | Frekuensi | Retention | Tools |
|--------------|-----------|-----------|-----------|-------|
| **Full Backup** | Backup semua data | Mingguan | 4 minggu | `pg_dump`, `mysqldump` |
| **Incremental Backup** | Backup data yang berubah | Harian | 30 hari | `WAL Archiving` (PostgreSQL) |
| **Snapshot** | Backup state sistem (VM, disk) | Harian | 7 hari | AWS EBS Snapshot, `rsync` |
| **Log Backup** | Backup log aplikasi | Harian | 90 hari | Loki, S3 |

---
#### **🚀 Contoh Implementasi: Backup & Restore**
##### **1. Backup PostgreSQL (Primary Database)**
**Strategi:**
- **Full Backup**: Setiap **Minggu** (pukul 02:00 WIB).
- **WAL Archiving**: **Continuous** (untuk point-in-time recovery).
- **Retention**: **30 hari** (full backup + WAL).

**Contoh Skrip Backup (Python):**
```python
# File: scripts/backup_postgres.py
import os
import subprocess
import boto3
from datetime import datetime
import psycopg2
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("backup_postgres.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Konfigurasi
DB_HOST = os.getenv("DB_HOST", "postgres.musgo-os.com")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "musgo_os")
S3_BUCKET = os.getenv("S3_BUCKET", "musgo-os-backups")
S3_PREFIX = os.getenv("S3_PREFIX", "postgres")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "30"))

# S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def backup_full():
    """Backup full database"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"/tmp/postgres_full_{timestamp}.sql"
    s3_key = f"{S3_PREFIX}/full/{timestamp}.sql"

    try:
        # Dump database
        logger.info(f"Starting full backup to {backup_file}")
        cmd = [
            "pg_dump",
            f"--host={DB_HOST}",
            f"--port={DB_PORT}",
            f"--username={DB_USER}",
            f"--dbname={DB_NAME}",
            "--format=plain",
            "--compress=9",
            f"--file={backup_file}",
        ]
        env = {"PGPASSWORD": DB_PASSWORD}
        subprocess.run(cmd, check=True, env=env)

        # Upload ke S3
        logger.info(f"Uploading {backup_file} to S3 ({s3_key})")
        s3.upload_file(backup_file, S3_BUCKET, s3_key)

        # Hapus file lokal
        os.remove(backup_file)
        logger.info("Full backup completed successfully")
        return True
    except Exception as e:
        logger.error(f"Full backup failed: {e}")
        return False

def backup_wal():
    """Backup WAL (Write-Ahead Log) untuk PITR (Point-In-Time Recovery)"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    wal_dir = "/tmp/wal_archive"
    s3_prefix = f"{S3_PREFIX}/wal/{timestamp}"

    try:
        # Pastikan direktori WAL ada
        os.makedirs(wal_dir, exist_ok=True)

        # Salin WAL dari PostgreSQL
        logger.info(f"Starting WAL backup to {wal_dir}")
        cmd = [
            "pg_basebackup",
            f"--host={DB_HOST}",
            f"--port={DB_PORT}",
            f"--username={DB_USER}",
            f"--dbname={DB_NAME}",
            f"--wal-method=stream",
            f"--pgdata={wal_dir}",
            "--format=tar",
            "--compress=9",
        ]
        env = {"PGPASSWORD": DB_PASSWORD}
        subprocess.run(cmd, check=True, env=env)

        # Upload WAL ke S3
        for root, _, files in os.walk(wal_dir):
            for file in files:
                local_path = os.path.join(root, file)
                s3_key = f"{s3_prefix}/{file}"
                logger.info(f"Uploading {local_path} to S3 ({s3_key})")
                s3.upload_file(local_path, S3_BUCKET, s3_key)

        # Hapus direktori lokal
        subprocess.run(["rm", "-rf", wal_dir], check=True)
        logger.info("WAL backup completed successfully")
        return True
    except Exception as e:
        logger.error(f"WAL backup failed: {e}")
        return False

def cleanup_old_backups():
    """Hapus backup lama (retention policy)"""
    try:
        # List semua backup di S3
        objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
        if "Contents" not in objects:
            return True

        # Hapus backup yang lebih tua dari RETENTION_DAYS
        cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)
        for obj in objects["Contents"]:
            last_modified = obj["LastModified"].replace(tzinfo=None)
            if last_modified < cutoff:
                s3_key = obj["Key"]
                logger.info(f"Deleting old backup: {s3_key}")
                s3.delete_object(Bucket=S3_BUCKET, Key=s3_key)

        return True
    except Exception as e:
        logger.error(f"Cleanup failed: {e}")
        return False

def main():
    """Main function"""
    logger.info("Starting PostgreSQL backup")

    # Full backup (Mingguan)
    if datetime.now().weekday() == 0:  # Minggu
        if not backup_full():
            logger.error("Full backup failed, exiting")
            return

    # WAL backup (Harian)
    if not backup_wal():
        logger.error("WAL backup failed, exiting")
        return

    # Cleanup
    if not cleanup_old_backups():
        logger.error("Cleanup failed")

    logger.info("PostgreSQL backup completed")

if __name__ == "__main__":
    main()
```

**Cron Job (Untuk Jalankan Backup Otomatis):**
```bash
# Edit crontab
crontab -e

# Tambahkan:
# Full backup setiap Minggu pukul 02:00
0 2 * * 0 /usr/bin/python3 /path/to/scripts/backup_postgres.py >> /var/log/postgres_backup.log 2>&1

# WAL backup setiap jam
0 * * * * /usr/bin/python3 /path/to/scripts/backup_postgres.py --wal-only >> /var/log/postgres_backup.log 2>&1
```

---
##### **2. Restore PostgreSQL**
**Contoh Skrip Restore (Python):**
```python
# File: scripts/restore_postgres.py
import os
import subprocess
import boto3
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("restore_postgres.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Konfigurasi
DB_HOST = os.getenv("DB_HOST", "postgres.musgo-os.com")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "musgo_os")
S3_BUCKET = os.getenv("S3_BUCKET", "musgo-os-backups")
S3_PREFIX = os.getenv("S3_PREFIX", "postgres")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
RESTORE_TIME = os.getenv("RESTORE_TIME")  # Format: "2026-05-19 10:00:00" (opsional)

# S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def download_backup(backup_type: str = "full", timestamp: str = None):
    """Download backup dari S3"""
    if backup_type == "full":
        if not timestamp:
            # Ambil backup full terbaru
            objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=f"{S3_PREFIX}/full")
            if "Contents" not in objects:
                logger.error("No full backups found")
                return None
            latest = max(objects["Contents"], key=lambda x: x["LastModified"])
            s3_key = latest["Key"]
        else:
            s3_key = f"{S3_PREFIX}/full/{timestamp}.sql"
    elif backup_type == "wal":
        s3_key = f"{S3_PREFIX}/wal/{timestamp}"
    else:
        logger.error(f"Unknown backup type: {backup_type}")
        return None

    local_file = f"/tmp/{os.path.basename(s3_key)}"
    try:
        logger.info(f"Downloading {s3_key} from S3 to {local_file}")
        s3.download_file(S3_BUCKET, s3_key, local_file)
        return local_file
    except Exception as e:
        logger.error(f"Failed to download {s3_key}: {e}")
        return None

def restore_full(backup_file: str):
    """Restore full backup"""
    try:
        logger.info(f"Restoring full backup from {backup_file}")

        # Drop database lama (jika ada)
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname="postgres",  # Connect ke default DB
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        conn.close()

        # Restore backup
        cmd = [
            "psql",
            f"--host={DB_HOST}",
            f"--port={DB_PORT}",
            f"--username={DB_USER}",
            f"--dbname={DB_NAME}",
            f"--file={backup_file}",
        ]
        env = {"PGPASSWORD": DB_PASSWORD}
        subprocess.run(cmd, check=True, env=env)

        logger.info("Full restore completed successfully")
        return True
    except Exception as e:
        logger.error(f"Full restore failed: {e}")
        return False

def restore_pitr(backup_file: str, wal_dir: str, restore_time: str = None):
    """Restore Point-In-Time Recovery (PITR)"""
    try:
        logger.info(f"Restoring PITR from {backup_file} and WAL {wal_dir}")

        # Stop PostgreSQL (jika berjalan)
        subprocess.run(["systemctl", "stop", "postgresql"], check=False)

        # Hapus data lama
        subprocess.run(["rm", "-rf", "/var/lib/postgresql/data/*"], check=True)

        # Restore base backup
        cmd = [
            "pg_basebackup",
            f"--host={DB_HOST}",
            f"--port={DB_PORT}",
            f"--username={DB_USER}",
            f"--dbname={DB_NAME}",
            f"--pgdata=/var/lib/postgresql/data",
            f"--wal-method=none",
            f"--restore-target-time={restore_time}" if restore_time else "",
        ]
        env = {"PGPASSWORD": DB_PASSWORD}
        subprocess.run(cmd, check=True, env=env)

        # Salin WAL ke direktori pg_wal
        subprocess.run(["mkdir", "-p", "/var/lib/postgresql/data/pg_wal"], check=True)
        subprocess.run(["cp", "-r", f"{wal_dir}/*", "/var/lib/postgresql/data/pg_wal/"], check=True)

        # Start PostgreSQL
        subprocess.run(["systemctl", "start", "postgresql"], check=True)

        logger.info("PITR restore completed successfully")
        return True
    except Exception as e:
        logger.error(f"PITR restore failed: {e}")
        return False

def main():
    """Main function"""
    logger.info("Starting PostgreSQL restore")

    # Download backup
    backup_file = download_backup(backup_type="full")
    if not backup_file:
        logger.error("Failed to download backup")
        return

    # Restore full backup
    if not restore_full(backup_file):
        logger.error("Full restore failed, exiting")
        return

    # Jika RESTORE_TIME diset, lakukan PITR
    if RESTORE_TIME:
        wal_dir = download_backup(backup_type="wal", timestamp=RESTORE_TIME)
        if wal_dir:
            if not restore_pitr(backup_file, wal_dir, RESTORE_TIME):
                logger.error("PITR restore failed")
        else:
            logger.warning("No WAL backup found for PITR")

    logger.info("PostgreSQL restore completed")

if __name__ == "__main__":
    main()
```

**Cara Restore:**
```bash
# Restore full backup terbaru
python3 /path/to/scripts/restore_postgres.py

# Restore ke waktu tertentu (PITR)
RESTORE_TIME="2026-05-19 10:00:00" python3 /path/to/scripts/restore_postgres.py
```

---
##### **3. Backup Redis**
**Strategi:**
- **RDB Snapshot**: Setiap **6 jam** (pukul 00:00, 06:00, 12:00, 18:00 WIB).
- **AOF (Append-Only File)**: **Enabled** (untuk durability).
- **Retention**: **7 hari**.

**Contoh Skrip Backup Redis:**
```python
# File: scripts/backup_redis.py
import os
import subprocess
import boto3
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("backup_redis.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Konfigurasi
REDIS_HOST = os.getenv("REDIS_HOST", "redis.musgo-os.com")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
S3_BUCKET = os.getenv("S3_BUCKET", "musgo-os-backups")
S3_PREFIX = os.getenv("S3_PREFIX", "redis")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "7"))

# S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def backup_redis():
    """Backup Redis RDB snapshot"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"/tmp/redis_dump_{timestamp}.rdb"
    s3_key = f"{S3_PREFIX}/{timestamp}.rdb"

    try:
        # Trigger RDB save
        logger.info("Triggering Redis RDB save")
        cmd = ["redis-cli", f"-h {REDIS_HOST}", f"-p {REDIS_PORT}"]
        if REDIS_PASSWORD:
            cmd.append(f"-a {REDIS_PASSWORD}")
        cmd.append("SAVE")
        subprocess.run(cmd, check=True)

        # Salin RDB file
        redis_data_dir = "/var/lib/redis"
        rdb_file = f"{redis_data_dir}/dump.rdb"
        if not os.path.exists(rdb_file):
            logger.error(f"RDB file not found: {rdb_file}")
            return False

        logger.info(f"Copying {rdb_file} to {backup_file}")
        subprocess.run(["cp", rdb_file, backup_file], check=True)

        # Upload ke S3
        logger.info(f"Uploading {backup_file} to S3 ({s3_key})")
        s3.upload_file(backup_file, S3_BUCKET, s3_key)

        # Hapus file lokal
        os.remove(backup_file)
        logger.info("Redis backup completed successfully")
        return True
    except Exception as e:
        logger.error(f"Redis backup failed: {e}")
        return False

def cleanup_old_backups():
    """Hapus backup lama"""
    try:
        objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
        if "Contents" not in objects:
            return True

        cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)
        for obj in objects["Contents"]:
            last_modified = obj["LastModified"].replace(tzinfo=None)
            if last_modified < cutoff:
                s3_key = obj["Key"]
                logger.info(f"Deleting old backup: {s3_key}")
                s3.delete_object(Bucket=S3_BUCKET, Key=s3_key)

        return True
    except Exception as e:
        logger.error(f"Cleanup failed: {e}")
        return False

def main():
    """Main function"""
    logger.info("Starting Redis backup")

    if not backup_redis():
        logger.error("Redis backup failed, exiting")
        return

    if not cleanup_old_backups():
        logger.error("Cleanup failed")

    logger.info("Redis backup completed")

if __name__ == "__main__":
    main()
```

**Cron Job:**
```bash
# Edit crontab
crontab -e

# Tambahkan (setiap 6 jam)
0 */6 * * * /usr/bin/python3 /path/to/scripts/backup_redis.py >> /var/log/redis_backup.log 2>&1
```

---
##### **4. Restore Redis**
**Contoh Skrip Restore Redis:**
```python
# File: scripts/restore_redis.py
import os
import subprocess
import boto3
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("restore_redis.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Konfigurasi
REDIS_HOST = os.getenv("REDIS_HOST", "redis.musgo-os.com")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
S3_BUCKET = os.getenv("S3_BUCKET", "musgo-os-backups")
S3_PREFIX = os.getenv("S3_PREFIX", "redis")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
RESTORE_TIME = os.getenv("RESTORE_TIME")  # Format: "2026-05-19_100000"

# S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def download_backup(timestamp: str = None):
    """Download backup dari S3"""
    if not timestamp:
        # Ambil backup terbaru
        objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
        if "Contents" not in objects:
            logger.error("No backups found")
            return None
        latest = max(objects["Contents"], key=lambda x: x["LastModified"])
        s3_key = latest["Key"]
    else:
        s3_key = f"{S3_PREFIX}/{timestamp}.rdb"

    local_file = f"/tmp/{os.path.basename(s3_key)}"
    try:
        logger.info(f"Downloading {s3_key} from S3 to {local_file}")
        s3.download_file(S3_BUCKET, s3_key, local_file)
        return local_file
    except Exception as e:
        logger.error(f"Failed to download {s3_key}: {e}")
        return None

def restore_redis(backup_file: str):
    """Restore Redis dari RDB file"""
    try:
        logger.info(f"Restoring Redis from {backup_file}")

        # Stop Redis
        subprocess.run(["systemctl", "stop", "redis"], check=False)

        # Salin RDB file ke direktori Redis
        redis_data_dir = "/var/lib/redis"
        os.makedirs(redis_data_dir, exist_ok=True)
        subprocess.run(["cp", backup_file, f"{redis_data_dir}/dump.rdb"], check=True)

        # Start Redis
        subprocess.run(["systemctl", "start", "redis"], check=True)

        logger.info("Redis restore completed successfully")
        return True
    except Exception as e:
        logger.error(f"Redis restore failed: {e}")
        return False

def main():
    """Main function"""
    logger.info("Starting Redis restore")

    # Download backup
    backup_file = download_backup()
    if not backup_file:
        logger.error("Failed to download backup")
        return

    # Restore
    if not restore_redis(backup_file):
        logger.error("Redis restore failed, exiting")
        return

    logger.info("Redis restore completed")

if __name__ == "__main__":
    main()
```

**Cara Restore:**
```bash
# Restore backup terbaru
python3 /path/to/scripts/restore_redis.py

# Restore backup tertentu
RESTORE_TIME="2026-05-19_100000" python3 /path/to/scripts/restore_redis.py
```

---
##### **5. Backup Kubernetes (Etcd)**
**Strategi:**
- **Etcd Snapshot**: Setiap **6 jam** (bersamaan dengan Redis).
- **Retention**: **7 hari**.

**Contoh Skrip Backup Etcd:**
```bash
# File: scripts/backup_etcd.sh
#!/bin/bash

# Konfigurasi
ETCDCTL_API=3
ETCD_ENDPOINTS="https://127.0.0.1:2379"
ETCD_CACERT="/etc/kubernetes/pki/etcd/ca.crt"
ETCD_CERT="/etc/kubernetes/pki/etcd/server.crt"
ETCD_KEY="/etc/kubernetes/pki/etcd/server.key"
S3_BUCKET="musgo-os-backups"
S3_PREFIX="etcd"
AWS_ACCESS_KEY="YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY="YOUR_AWS_SECRET_KEY"
RETENTION_DAYS=7

# Timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="/tmp/etcd_backup_${TIMESTAMP}.db"
S3_KEY="${S3_PREFIX}/${TIMESTAMP}.db"

# Backup Etcd
echo "Backing up Etcd to ${BACKUP_FILE}"
ETCDCTL_API=${ETCDCTL_API} etcdctl \
  --endpoints=${ETCD_ENDPOINTS} \
  --cacert=${ETCD_CACERT} \
  --cert=${ETCD_CERT} \
  --key=${ETCD_KEY} \
  snapshot save ${BACKUP_FILE}

# Upload ke S3
echo "Uploading ${BACKUP_FILE} to S3 (${S3_KEY})"
aws s3 cp ${BACKUP_FILE} s3://${S3_BUCKET}/${S3_KEY} \
  --access-key ${AWS_ACCESS_KEY} \
  --secret-key ${AWS_SECRET_KEY}

# Hapus file lokal
rm -f ${BACKUP_FILE}

# Cleanup (hapus backup > RETENTION_DAYS)
echo "Cleaning up old backups"
aws s3 ls s3://${S3_BUCKET}/${S3_PREFIX}/ | while read -r line; do
  create_date=$(echo $line | awk '{print $1" "$2}')
  create_timestamp=$(date -d "$create_date" +%s)
  current_timestamp=$(date +%s)
  diff_days=$(( (current_timestamp - create_timestamp) / 86400 ))

  if [ $diff_days -gt $RETENTION_DAYS ]; then
    file_name=$(echo $line | awk '{print $4}')
    echo "Deleting old backup: ${file_name}"
    aws s3 rm s3://${S3_BUCKET}/${file_name} \
      --access-key ${AWS_ACCESS_KEY} \
      --secret-key ${AWS_SECRET_KEY}
  fi
done

echo "Etcd backup completed"
```

**Cron Job:**
```bash
# Edit crontab
crontab -e

# Tambahkan (setiap 6 jam)
0 */6 * * * /bin/bash /path/to/scripts/backup_etcd.sh >> /var/log/etcd_backup.log 2>&1
```

---
##### **6. Restore Kubernetes (Etcd)**
**Contoh Skrip Restore Etcd:**
```bash
# File: scripts/restore_etcd.sh
#!/bin/bash

# Konfigurasi
ETCDCTL_API=3
ETCD_ENDPOINTS="https://127.0.0.1:2379"
ETCD_CACERT="/etc/kubernetes/pki/etcd/ca.crt"
ETCD_CERT="/etc/kubernetes/pki/etcd/server.crt"
ETCD_KEY="/etc/kubernetes/pki/etcd/server.key"
S3_BUCKET="musgo-os-backups"
S3_PREFIX="etcd"
AWS_ACCESS_KEY="YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY="YOUR_AWS_SECRET_KEY"
RESTORE_TIME="2026-05-19_100000"  # Opsional

# Download backup terbaru (atau yang spesifik)
if [ -z "$RESTORE_TIME" ]; then
  # Ambil backup terbaru
  BACKUP_FILE=$(aws s3 ls s3://${S3_BUCKET}/${S3_PREFIX}/ | sort | tail -n 1 | awk '{print $4}')
else
  BACKUP_FILE="${S3_PREFIX}/${RESTORE_TIME}.db"
fi

TEMP_FILE="/tmp/etcd_backup.db"

echo "Downloading ${BACKUP_FILE} from S3"
aws s3 cp s3://${S3_BUCKET}/${BACKUP_FILE} ${TEMP_FILE} \
  --access-key ${AWS_ACCESS_KEY} \
  --secret-key ${AWS_SECRET_KEY}

# Stop Kubernetes API Server
echo "Stopping Kubernetes API Server"
systemctl stop kubelet

# Restore Etcd
echo "Restoring Etcd from ${TEMP_FILE}"
ETCDCTL_API=${ETCDCTL_API} etcdctl \
  --endpoints=${ETCD_ENDPOINTS} \
  --cacert=${ETCD_CACERT} \
  --cert=${ETCD_CERT} \
  --key=${ETCD_KEY} \
  snapshot restore ${TEMP_FILE} \
  --data-dir=/var/lib/etcd

# Start Kubernetes API Server
echo "Starting Kubernetes API Server"
systemctl start kubelet

# Hapus file sementara
rm -f ${TEMP_FILE}

echo "Etcd restore completed"
```

**Cara Restore:**
```bash
# Restore backup terbaru
/bin/bash /path/to/scripts/restore_etcd.sh

# Restore backup tertentu
RESTORE_TIME="2026-05-19_100000" /bin/bash /path/to/scripts/restore_etcd.sh
```

---
---
---

## **🔹 12.4 Failover & High Availability**
### **📌 Penjelasan**
**Failover** adalah **proses otomatis berpindah** dari **sistem primary** ke **sistem standby** jika **primary gagal**. **High Availability (HA)** adalah **desain sistem** untuk **minimalkan downtime**.

**Strategi Failover untuk MusGo-OS:**
| Komponen | Primary | Standby | Failover Mechanism | RTO |
|----------|---------|---------|--------------------|-----|
| **Backend** | Kubernetes Cluster A | Kubernetes Cluster B | **Kubernetes Federation** | < 5 menit |
| **Frontend** | Kubernetes Cluster A | Kubernetes Cluster B | **DNS Failover** | < 1 menit |
| **PostgreSQL** | Primary DB (Cluster A) | Standby DB (Cluster B) | **Logical Replication** | < 1 menit |
| **Redis** | Primary (Cluster A) | Replica (Cluster B) | **Redis Sentinel** | < 30 detik |
| **Zapier Integration** | Primary (Cluster A) | Fallback Mode | **Circuit Breaker** | < 1 menit |

---
#### **🚀 Contoh Implementasi: Failover**
##### **1. PostgreSQL Failover (Logical Replication)**
**Arsitektur:**
```
PostgreSQL Primary (Cluster A) → [Replikasi] → PostgreSQL Standby (Cluster B)
```

**Setup Replikasi:**
```sql
-- Di PostgreSQL Primary (Cluster A)
-- Buat user untuk replikasi
CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'replicator_password';

-- Izinkan akses dari Standby
ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_replication_slots = 10;
ALTER SYSTEM SET max_wal_senders = 10;
SELECT pg_reload_conf();

-- Buat publication untuk semua tabel
CREATE PUBLICATION musgo_os_publication FOR ALL TABLES;

-- Di PostgreSQL Standby (Cluster B)
-- Buat user untuk replikasi
CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'replicator_password';

-- Buat subscription
CREATE SUBSCRIPTION musgo_os_subscription
CONNECTION 'host=primary-db.musgo-os.com port=5432 dbname=musgo_os user=replicator password=replicator_password'
PUBLICATION musgo_os_publication;
```

**Promosi Standby ke Primary (Jika Primary Down):**
```sql
-- Di PostgreSQL Standby (Cluster B)
-- Hentikan subscription
ALTER SUBSCRIPTION musgo_os_subscription DISABLE;

-- Promosikan ke Primary
SELECT pg_promote();
```

**Automasi Failover (Patroni + etcd):**
**Patroni** adalah **high-availability solution** untuk PostgreSQL.

**Docker Compose untuk Patroni:**
```yaml
# File: docker-compose.postgres-ha.yml
version: "3.8"

services:
  # etcd (untuk Patroni)
  etcd:
    image: bitnami/etcd:latest
    container_name: etcd
    environment:
      - ALLOW_NONE_AUTHENTICATION=yes
    ports:
      - "2379:2379"
      - "2380:2380"
    volumes:
      - etcd_data:/bitnami/etcd
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Patroni (PostgreSQL HA)
  patroni-primary:
    image: patroni/patroni:latest
    container_name: patroni-primary
    depends_on:
      - etcd
    environment:
      - PATRONI_ETCD_HOSTS=etcd:2379
      - PATRONI_POSTGRESQL_CONNECT_ADDRESS=patroni-primary:5432
      - PATRONI_POSTGRESQL_DATA_DIR=/var/lib/postgresql/data
      - PATRONI_POSTGRESQL_BIN_DIR=/usr/lib/postgresql/15/bin
      - PATRONI_POSTGRESQL_PGPORT=5432
      - PATRONI_POSTGRESQL_CONFIG_FILE=/etc/postgresql/postgresql.conf
      - PATRONI_SUPERUSER_USERNAME=postgres
      - PATRONI_SUPERUSER_PASSWORD=postgres
      - PATRONI_REPLICATION_USERNAME=replicator
      - PATRONI_REPLICATION_PASSWORD=replicator_password
      - PATRONI_ADMIN_USERNAME=admin
      - PATRONI_ADMIN_PASSWORD=admin
      - PATRONI_NAME=patroni-primary
      - PATRONI_SCOPE=musgo-os
    ports:
      - "5432:5432"
    volumes:
      - postgres_data_primary:/var/lib/postgresql/data
      - ./patroni:/etc/patroni
    networks:
      - musgo-os-network
    restart: unless-stopped

  patroni-standby:
    image: patroni/patroni:latest
    container_name: patroni-standby
    depends_on:
      - etcd
    environment:
      - PATRONI_ETCD_HOSTS=etcd:2379
      - PATRONI_POSTGRESQL_CONNECT_ADDRESS=patroni-standby:5432
      - PATRONI_POSTGRESQL_DATA_DIR=/var/lib/postgresql/data
      - PATRONI_POSTGRESQL_BIN_DIR=/usr/lib/postgresql/15/bin
      - PATRONI_POSTGRESQL_PGPORT=5432
      - PATRONI_POSTGRESQL_CONFIG_FILE=/etc/postgresql/postgresql.conf
      - PATRONI_SUPERUSER_USERNAME=postgres
      - PATRONI_SUPERUSER_PASSWORD=postgres
      - PATRONI_REPLICATION_USERNAME=replicator
      - PATRONI_REPLICATION_PASSWORD=replicator_password
      - PATRONI_ADMIN_USERNAME=admin
      - PATRONI_ADMIN_PASSWORD=admin
      - PATRONI_NAME=patroni-standby
      - PATRONI_SCOPE=musgo-os
    ports:
      - "5433:5432"
    volumes:
      - postgres_data_standby:/var/lib/postgresql/data
      - ./patroni:/etc/patroni
    networks:
      - musgo-os-network
    restart: unless-stopped

  # HAProxy (Load Balancer untuk PostgreSQL)
  haproxy:
    image: haproxy:latest
    container_name: haproxy
    depends_on:
      - patroni-primary
      - patroni-standby
    ports:
      - "5000:5000"
    volumes:
      - ./haproxy:/usr/local/etc/haproxy
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  etcd_data:
  postgres_data_primary:
  postgres_data_standby:

networks:
  musgo-os-network:
    external: true
```

**Konfigurasi HAProxy (`haproxy/haproxy.cfg`):**
```cfg
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode tcp
    option tcplog
    option dontlognull
    timeout connect 5000
    timeout client 50000
    timeout server 50000

listen stats
    bind *:7000
    mode http
    stats enable
    stats uri /stats
    stats refresh 10s
    stats admin if TRUE

listen postgres
    bind *:5000
    mode tcp
    option httpchk
    http-check expect status 200
    default-server inter 3s fall 3 rise 2 on-marked-down shutdown-sessions
    server patroni-primary patroni-primary:5432 check port 8008
    server patroni-standby patroni-standby:5432 check port 8008 backup
```

**Cara Failover:**
1. **Patroni otomatis** akan **promosikan standby** jika primary down.
2. **HAProxy** akan **redirect traffic** ke standby yang baru dipromosikan.

---
##### **2. Redis Failover (Redis Sentinel)**
**Arsitektur:**
```
Redis Primary (Cluster A) → [Replikasi] → Redis Replica (Cluster A)
                                      ↓
Redis Sentinel (Cluster A + B) → [Monitor] → Failover otomatis
```

**Docker Compose untuk Redis Sentinel:**
```yaml
# File: docker-compose.redis-ha.yml
version: "3.8"

services:
  # Redis Primary
  redis-primary:
    image: redis:7-alpine
    container_name: redis-primary
    command: redis-server --appendonly yes --protected-mode no
    ports:
      - "6379:6379"
    volumes:
      - redis_data_primary:/data
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Redis Replica
  redis-replica:
    image: redis:7-alpine
    container_name: redis-replica
    command: redis-server --replicaof redis-primary 6379 --appendonly yes --protected-mode no
    ports:
      - "6380:6379"
    volumes:
      - redis_data_replica:/data
    networks:
      - musgo-os-network
    restart: unless-stopped

  # Redis Sentinel (3 nodes untuk HA)
  redis-sentinel-1:
    image: redis:7-alpine
    container_name: redis-sentinel-1
    command: redis-sentinel /etc/redis/sentinel.conf
    ports:
      - "26379:26379"
    volumes:
      - ./redis/sentinel-1.conf:/etc/redis/sentinel.conf
    networks:
      - musgo-os-network
    restart: unless-stopped

  redis-sentinel-2:
    image: redis:7-alpine
    container_name: redis-sentinel-2
    command: redis-sentinel /etc/redis/sentinel.conf
    ports:
      - "26380:26379"
    volumes:
      - ./redis/sentinel-2.conf:/etc/redis/sentinel.conf
    networks:
      - musgo-os-network
    restart: unless-stopped

  redis-sentinel-3:
    image: redis:7-alpine
    container_name: redis-sentinel-3
    command: redis-sentinel /etc/redis/sentinel.conf
    ports:
      - "26381:26379"
    volumes:
      - ./redis/sentinel-3.conf:/etc/redis/sentinel.conf
    networks:
      - musgo-os-network
    restart: unless-stopped

volumes:
  redis_data_primary:
  redis_data_replica:

networks:
  musgo-os-network:
    external: true
```

**Konfigurasi Sentinel (`redis/sentinel-1.conf`):**
```conf
port 26379
sentinel monitor mymaster redis-primary 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 10000
sentinel parallel-syncs mymaster 1
sentinel notification-script mymaster /etc/redis/notify.sh
sentinel client-reconfig-script mymaster /etc/redis/reconfig.sh
```

**Cara Failover:**
1. **Sentinel otomatis** akan **deteksi primary down**.
2. **Sentinel** akan **promosikan replica** ke primary.
3. **Client** (MusGo-OS) akan **otomatis terhubung** ke primary baru.

---
##### **3. Kubernetes Failover (Multi-Cluster)**
**Arsitektur:**
```
Kubernetes Cluster A (Primary) → [Replikasi] → Kubernetes Cluster B (Standby)
```

**Tools:**
- **Kubernetes Federation**: Untuk **multi-cluster management**.
- **Velero**: Untuk **backup & restore** cluster.
- **ArgoCD**: Untuk **sync config** antar cluster.

**Contoh Setup Kubernetes Federation:**
```yaml
# File: federation.yaml
apiVersion: federation.k8s.io/v1beta1
kind: FederatedDeployment
metadata:
  name: musgo-os-backend
  namespace: musgo-os
spec:
  template:
    spec:
      replicas: 3
      template:
        spec:
          containers:
          - name: musgo-os-backend
            image: musgo-os/backend:latest
            ports:
            - containerPort: 8000
  placement:
    clusters:
    - name: cluster-a
    - name: cluster-b
```

**Cara Failover:**
1. **Federation Controller** akan **deteksi cluster A down**.
2. **Traffic akan dialihkan** ke **cluster B**.
3. **Cluster B** akan **scale up** untuk menangani beban.

---
##### **4. Zapier Integration Failover (Circuit Breaker)**
**Strategi:**
- **Circuit Breaker**: Jika **Zapier API gagal**, **MusGo-OS** akan **berhenti memanggil Zapier** dan **menggunakan fallback mechanism**.
- **Fallback Mechanism**: Simpan **request ke queue** (Redis/RabbitMQ) dan **coba lagi nanti**.

**Contoh Kode (Python - FastAPI + Circuit Breaker):**
```python
# File: backend/zapier_client.py
from fastapi import HTTPException
import requests
from circuitbreaker import circuit
from typing import Optional, Dict, Any
import time
import redis

# Setup Redis untuk queue
redis_client = redis.Redis(host="redis", port=6379, db=0)

# Circuit Breaker (gagal jika 50% request gagal dalam 10 detik)
@circuit(failure_threshold=0.5, recovery_timeout=10, expected_exception=Exception)
def call_zapier_api(endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
    """Panggil Zapier API dengan circuit breaker"""
    headers = {
        "Authorization": f"Bearer {ZAPIER_API_KEY}",
        "Content-Type": "application/json",
    }

    url = f"https://api.zapier.com/v2/{endpoint}"
    response = requests.post(url, json=data, headers=headers, timeout=5)

    if response.status_code != 200:
        raise Exception(f"Zapier API Error: {response.status_code} - {response.text}")

    return response.json()

def fallback_zapier_api(endpoint: str, data: Dict[str, Any] = None) -> bool:
    """Fallback: Simpan request ke queue jika Zapier API gagal"""
    try:
        # Simpan ke Redis queue
        redis_client.lpush(
            "zapier_failed_requests",
            {"endpoint": endpoint, "data": data, "timestamp": time.time()}
        )
        return True
    except Exception as e:
        print(f"Fallback failed: {e}")
        return False

def retry_failed_requests():
    """Coba ulang request yang gagal"""
    while True:
        # Ambil request dari queue
        request = redis_client.rpop("zapier_failed_requests")
        if not request:
            break

        try:
            # Coba ulang
            result = call_zapier_api(request["endpoint"], request["data"])
            print(f"Retry succeeded: {request['endpoint']}")
        except Exception as e:
            # Jika masih gagal, simpan lagi ke queue (dengan delay)
            time.sleep(5)  # Tunggu 5 detik
            redis_client.lpush("zapier_failed_requests", request)
            print(f"Retry failed: {e}")

# Contoh penggunaan
try:
    result = call_zapier_api("actions/run", {"app": "slack", "action": "Send Channel Message"})
except Exception as e:
    # Jika circuit breaker terbuka, gunakan fallback
    if fallback_zapier_api("actions/run", {"app": "slack", "action": "Send Channel Message"}):
        print("Request disimpan ke queue, akan dicoba lagi nanti")
    else:
        raise HTTPException(status_code=503, detail="Zapier API dan fallback gagal")
```

**Cron Job untuk Retry:**
```bash
# Edit crontab
crontab -e

# Coba ulang request gagal setiap 1 menit
* * * * * /usr/bin/python3 -c "from backend.zapier_client import retry_failed_requests; retry_failed_requests()" >> /var/log/zapier_retry.log 2>&1
```

---
---
---

## **🔹 12.5 Disaster Recovery Testing (Testing DR)**
### **📌 Penjelasan**
**Disaster Recovery Testing (DR Testing)** adalah **proses menguji** apakah **DR Plan** berfungsi dengan benar. Tujuannya:
- **Verifikasi RTO & RPO**.
- **Temukan celah** dalam DR Plan.
- **Latih tim** untuk penanganan bencana.

**Jenis DR Testing:**
| Jenis Testing | Deskripsi | Frekuensi | Dampak |
|---------------|-----------|-----------|--------|
| **Tabletop Exercise** | Diskusi **teoritis** (tanpa eksekusi) | 6 bulan | Rendah |
| **Walkthrough Test** | **Simulasi** langkah-langkah DR | 3 bulan | Rendah |
| **Simulation Test** | **Uji coba** failover (tanpa mematikan production) | 1 bulan | Sedang |
| **Full Interruption Test** | **Matikan production** dan uji failover | 1 tahun | Tinggi |

---
#### **🚀 Contoh Implementasi: DR Testing**
##### **1. Tabletop Exercise (Diskusi)**
**Contoh Skenario:**
> *"PostgreSQL Primary di Cluster A crash dan tidak bisa dipulihkan. Bagaimana tim MusGo-OS menanganinya?"*

**Langkah-Langkah:**
1. **Incident Commander** (Dhani) memimpin diskusi.
2. **Tim Database** menjelaskan **langkah promosi standby**.
3. **Tim Backend** menjelaskan **langkah failover aplikasi**.
4. **Tim DevOps** menjelaskan **langkah update DNS**.
5. **Tim Support** menjelaskan **komunikasi ke user**.

**Output:**
- **Dokumentasi** langkah-langkah yang diperlukan.
- **Identifikasi celah** (misal: tidak ada dokumentasi DNS update).

---
##### **2. Simulation Test (Uji Coba Failover)**
**Contoh Skenario:**
> *"Simulasikan PostgreSQL Primary down dan uji failover ke Standby."*

**Langkah-Langkah:**
1. **Backup data terlebih dahulu** (untuk safety).
2. **Matikan PostgreSQL Primary** (di Cluster A).
3. **Monitor Patroni** (apakah standby dipromosikan?).
4. **Cek HAProxy** (apakah traffic dialihkan?).
5. **Cek MusGo-OS** (apakah aplikasi berjalan normal?).
6. **Verifikasi data** (apakah data konsisten?).
7. **Hidupkan kembali Primary** (dan cek replikasi).

**Contoh Skrip Testing:**
```bash
# File: scripts/test_postgres_failover.sh
#!/bin/bash

# Konfigurasi
PRIMARY_HOST="patroni-primary"
STANDBY_HOST="patroni-standby"
HAPROXY_HOST="haproxy"
TEST_DB="musgo_os_test"

# 1. Backup data (untuk safety)
echo "Backing up data..."
pg_dump -h $PRIMARY_HOST -U postgres -d $TEST_DB -F c -f /tmp/pre_test_backup.dump

# 2. Matikan Primary
echo "Stopping PostgreSQL Primary..."
kubectl exec $PRIMARY_HOST -- systemctl stop patroni

# 3. Tunggu failover (30 detik)
echo "Waiting for failover..."
sleep 30

# 4. Cek apakah Standby sudah jadi Primary
echo "Checking if Standby is now Primary..."
PRIMARY_NEW=$(kubectl exec $STANDBY_HOST -- patronictl list | grep "Leader" | awk '{print $1}')
if [ -z "$PRIMARY_NEW" ]; then
    echo "❌ Failover gagal: Standby tidak jadi Primary"
    exit 1
else
    echo "✅ Failover berhasil: Standby ($PRIMARY_NEW) sekarang Primary"
fi

# 5. Cek HAProxy
echo "Checking HAProxy..."
HAPROXY_STATUS=$(curl -s http://$HAPROXY_HOST:7000/stats | grep -o "$PRIMARY_NEW:5432")
if [ -z "$HAPROXY_STATUS" ]; then
    echo "❌ HAProxy gagal: Traffic tidak dialihkan ke Primary baru"
    exit 1
else
    echo "✅ HAProxy berhasil: Traffic dialihkan ke $PRIMARY_NEW"
fi

# 6. Cek MusGo-OS
echo "Checking MusGo-OS..."
MUSGO_STATUS=$(curl -s http://musgo-os-backend:8000/health | grep -o '"status":"healthy"')
if [ -z "$MUSGO_STATUS" ]; then
    echo "❌ MusGo-OS gagal: Aplikasi tidak berjalan normal"
    exit 1
else
    echo "✅ MusGo-OS berhasil: Aplikasi berjalan normal"
fi

# 7. Verifikasi data
echo "Verifying data..."
pg_dump -h $PRIMARY_NEW -U postgres -d $TEST_DB -F c -f /tmp/post_test_backup.dump
if ! diff /tmp/pre_test_backup.dump /tmp/post_test_backup.dump > /dev/null; then
    echo "❌ Data tidak konsisten"
    exit 1
else
    echo "✅ Data konsisten"
fi

# 8. Hidupkan kembali Primary
echo "Restarting PostgreSQL Primary..."
kubectl exec $PRIMARY_HOST -- systemctl start patroni

# 9. Tunggu replikasi
echo "Waiting for replication..."
sleep 30

# 10. Cek apakah Primary lama sekarang jadi Standby
echo "Checking if old Primary is now Standby..."
STANDBY_NEW=$(kubectl exec $PRIMARY_HOST -- patronictl list | grep "Replica" | awk '{print $1}')
if [ -z "$STANDBY_NEW" ]; then
    echo "❌ Replikasi gagal: Primary lama tidak jadi Standby"
    exit 1
else
    echo "✅ Replikasi berhasil: Primary lama ($STANDBY_NEW) sekarang Standby"
fi

echo "✅ Semua test berhasil!"
```

**Cara Jalankan:**
```bash
chmod +x /path/to/scripts/test_postgres_failover.sh
/path/to/scripts/test_postgres_failover.sh
```

---
##### **3. Full Interruption Test (Uji Penuh)**
**Contoh Skenario:**
> *"Matikan seluruh Cluster A dan uji failover ke Cluster B."*

**Langkah-Langkah:**
1. **Backup semua data** (PostgreSQL, Redis, Etcd).
2. **Matikan Cluster A** (simulasikan bencana).
3. **Monitor failover otomatis** ke Cluster B.
4. **Cek semua service** (Backend, Frontend, Database, Redis).
5. **Verifikasi data** (apakah data konsisten?).
6. **Hidupkan kembali Cluster A** dan cek **replikasi balik**.

**Catatan:**
- **Jangan dilakukan di production** (hanya di staging).
- **Lakukan di luar jam kerja** (untuk minimalkan dampak).

---
##### **4. DR Testing Schedule**
| Jenis Testing | Frekuensi | Tanggal | Catatan |
|---------------|-----------|---------|--------|
| Tabletop Exercise | 6 bulan | 19 Mei 2026, 19 November 2026 | Diskusi teoritis |
| Walkthrough Test | 3 bulan | 19 Juni 2026, 19 September 2026 | Simulasi langkah-langkah |
| Simulation Test | 1 bulan | Setiap tanggal 1 | Uji coba failover |
| Full Interruption Test | 1 tahun | 19 Desember 2026 | Uji penuh (staging) |

---
---
---

## **🔹 12.6 DR Documentation (Dokumentasi DR)**
### **📌 Penjelasan**
**DR Documentation** adalah **dokumen yang berisi**:
- **DR Plan** (rencana penanganan bencana).
- **Playbooks** (langkah-langkah penanganan).
- **Runbooks** (perintah-perintah teknis).
- **Kontak Darurat** (siapa yang harus dihubungi).
- **Testing Results** (hasil uji coba DR).

---
#### **🚀 Contoh Implementasi: DR Documentation**
##### **1. Dokumen DR Plan (Markdown)**
```markdown
# 📜 MusGo-OS 2in1: Disaster Recovery Plan (DRP)
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan (CTO)

---
## 📌 1. Tujuan
Dokumen ini mendefinisikan **prosedur pemulihan bencana** untuk **MusGo-OS 2in1 + Zapier**, termasuk:
- Backup dan restore.
- Failover dan high availability.
- Testing dan validasi.
- Dokumentasi dan pelaporan.

---
## 📌 2. Ruang Lingkup
| Komponen | Cakupan DR |
|----------|------------|
| **Backend (Python)** | Failover ke Cluster B, Restore dari backup |
| **Frontend (TypeScript)** | Failover ke Cluster B, Deploy ulang |
| **PostgreSQL** | Replikasi ke Standby, PITR (Point-In-Time Recovery) |
| **Redis** | Replikasi ke Replica, Failover otomatis (Sentinel) |
| **Kubernetes** | Failover ke Cluster B, Restore Etcd |
| **Zapier Integration** | Fallback Mechanism, Retry Queue |
| **Monitoring (Prometheus, Grafana, Loki)** | Failover ke Cluster B, Restore data |

---
## 📌 3. Peran dan Tanggung Jawab
| Peran | Tanggung Jawab | Kontak |
|-------|----------------|--------|
| **DR Coordinator** | Koordinasi DR Testing dan pemulihan | @dhani |
| **Database Engineer** | Backup/Restore PostgreSQL, Failover | @db-team |
| **DevOps Engineer** | Failover Kubernetes, Restore Etcd | @devops-team |
| **Backend Engineer** | Restore Backend, Cek Integrasi | @backend-team |
| **Frontend Engineer** | Restore Frontend, Cek UI | @frontend-team |
| **Security Engineer** | Verifikasi keamanan setelah DR | @security-team |
| **Support Lead** | Komunikasi ke user | @support-team |

---
## 📌 4. RTO & RPO
| Komponen | RTO | RPO | Catatan |
|----------|-----|-----|--------|
| **Backend** | < 1 jam | < 5 menit | Failover ke Cluster B |
| **Frontend** | < 30 menit | < 1 menit | Deploy ulang dari Git |
| **PostgreSQL** | < 1 jam | < 1 menit | Promosi Standby |
| **Redis** | < 5 menit | < 1 menit | Failover Sentinel |
| **Kubernetes** | < 2 jam | < 5 menit | Restore Etcd |
| **Zapier Integration** | < 1 jam | < 5 menit | Fallback + Retry |

---
## 📌 5. Prosedur DR
### 5.1 Deteksi Bencana
- **Monitoring**: Prometheus + Grafana (alert jika sistem down).
- **User Report**: User melaporkan sistem tidak berfungsi.
- **Zapier Status**: Cek [status.zapier.com](https://status.zapier.com/).

### 5.2 Deklarasi Bencana
- **Incident Commander** (Dhani) **mendeklarasikan bencana** jika:
  - **SEV-1**: Sistem **tidak berfungsi** > 15 menit.
  - **SEV-2**: Fitur **kritis terganggu** > 30 menit.
- **Buat Incident Ticket** (Jira/Linear) dengan label `disaster-recovery`.

### 5.3 Eksekusi DR Plan
#### 5.3.1 PostgreSQL Failover
1. **Cek status Patroni**:
   ```bash
   kubectl exec patroni-primary -n musgo-os -- patronictl list
   ```
2. **Jika Primary down**, Patroni **otomatis promosikan Standby**.
3. **Cek HAProxy**:
   ```bash
   curl http://haproxy:7000/stats
   ```
4. **Verifikasi MusGo-OS**:
   ```bash
   curl http://musgo-os-backend:8000/health
   ```

#### 5.3.2 Redis Failover
1. **Cek status Sentinel**:
   ```bash
   redis-cli -h redis-sentinel-1 -p 26379 sentinel masters
   ```
2. **Jika Primary down**, Sentinel **otomatis promosikan Replica**.
3. **Verifikasi MusGo-OS**:
   ```bash
   redis-cli -h redis-primary ping
   ```

#### 5.3.3 Kubernetes Failover
1. **Cek status Cluster A**:
   ```bash
   kubectl get nodes -n musgo-os
   ```
2. **Jika Cluster A down**, **traffic otomatis dialihkan** ke Cluster B.
3. **Scale up Cluster B**:
   ```bash
   kubectl scale deployment musgo-os-backend --replicas=5 -n musgo-os
   ```

#### 5.3.4 Zapier Integration Fallback
1. **Cek status Zapier**:
   ```bash
   curl https://api.zapier.com/v2/zaps
   ```
2. **Jika Zapier down**, **MusGo-OS otomatis menggunakan fallback**:
   - Simpan request ke **Redis queue**.
   - **Retry setiap 1 menit**.

### 5.4 Pemulihan
1. **Verifikasi semua service berjalan normal**.
2. **Monitor sistem** (Grafana, Sentry, Loki).
3. **Update user** (via Status Page, Email).

### 5.5 Post-DR
1. **Lakukan Post-Mortem** (dalam 24 jam).
2. **Perbaiki root cause**.
3. **Update DR Plan** (jika diperlukan).

---
## 📌 6. Backup & Restore
### 6.1 PostgreSQL
| Jenis Backup | Frekuensi | Retention | Lokasi |
|--------------|-----------|-----------|--------|
| Full Backup | Mingguan | 30 hari | S3 (`s3://musgo-os-backups/postgres/full/`) |
| WAL Backup | Continuous | 30 hari | S3 (`s3://musgo-os-backups/postgres/wal/`) |

**Restore Command:**
```bash
# Restore full backup
python3 /path/to/scripts/restore_postgres.py

# Restore ke waktu tertentu (PITR)
RESTORE_TIME="2026-05-19 10:00:00" python3 /path/to/scripts/restore_postgres.py
```

### 6.2 Redis
| Jenis Backup | Frekuensi | Retention | Lokasi |
|--------------|-----------|-----------|--------|
| RDB Snapshot | 6 jam | 7 hari | S3 (`s3://musgo-os-backups/redis/`) |

**Restore Command:**
```bash
python3 /path/to/scripts/restore_redis.py
```

### 6.3 Kubernetes (Etcd)
| Jenis Backup | Frekuensi | Retention | Lokasi |
|--------------|-----------|-----------|--------|
| Etcd Snapshot | 6 jam | 7 hari | S3 (`s3://musgo-os-backups/etcd/`) |

**Restore Command:**
```bash
/bin/bash /path/to/scripts/restore_etcd.sh
```

### 6.4 Code & Config
| Jenis Backup | Frekuensi | Retention | Lokasi |
|--------------|-----------|-----------|--------|
| Git Repository | Continuous | Forever | GitHub/GitLab |
| Ansible/Terraform | Continuous | Forever | GitHub/GitLab |

**Restore Command:**
```bash
# Clone repository
git clone https://github.com/musgo-os/musgo-os-2in1.git

# Apply Ansible
ansible-playbook -i inventory.ini playbook.yml
```

---
## 📌 7. Failover & High Availability
### 7.1 PostgreSQL (Patroni + HAProxy)
- **Primary**: `patroni-primary:5432`
- **Standby**: `patroni-standby:5432`
- **HAProxy**: `haproxy:5000` (Load Balancer)

**Failover Command:**
```bash
# Patroni otomatis handle failover
# Jika manual:
kubectl exec patroni-standby -n musgo-os -- patronictl failover
```

### 7.2 Redis (Sentinel)
- **Primary**: `redis-primary:6379`
- **Replica**: `redis-replica:6379`
- **Sentinel**: `redis-sentinel-1:26379`, `redis-sentinel-2:26379`, `redis-sentinel-3:26379`

**Failover Command:**
```bash
# Sentinel otomatis handle failover
# Jika manual:
redis-cli -h redis-sentinel-1 -p 26379 sentinel failover mymaster
```

### 7.3 Kubernetes (Federation)
- **Primary Cluster**: `cluster-a`
- **Standby Cluster**: `cluster-b`

**Failover Command:**
```bash
# Federation otomatis handle failover
# Jika manual:
kubefedctl failover --cluster=cluster-b
```

### 7.4 Zapier Integration (Circuit Breaker)
- **Primary**: Zapier API (`https://api.zapier.com`)
- **Fallback**: Redis Queue (`zapier_failed_requests`)

**Fallback Command:**
```python
# Otomatis dihandle oleh circuit breaker
# Jika manual:
fallback_zapier_api("actions/run", {"app": "slack", "action": "Send Channel Message"})
```

---
## 📌 8. DR Testing
### 8.1 Testing Schedule
| Jenis Testing | Frekuensi | Tanggal | Catatan |
|---------------|-----------|---------|--------|
| Tabletop Exercise | 6 bulan | 19 Mei 2026, 19 November 2026 | Diskusi teoritis |
| Walkthrough Test | 3 bulan | 19 Juni 2026, 19 September 2026 | Simulasi langkah-langkah |
| Simulation Test | 1 bulan | Setiap tanggal 1 | Uji coba failover |
| Full Interruption Test | 1 tahun | 19 Desember 2026 | Uji penuh (staging) |

### 8.2 Testing Results
| Tanggal | Jenis Testing | Hasil | Catatan |
|--------|---------------|-------|--------|
| 2026-05-19 | Tabletop Exercise | ✅ Success | Temukan celah: Tidak ada dokumentasi DNS update |
| 2026-06-01 | Simulation Test (PostgreSQL) | ✅ Success | Failover otomatis berjalan dengan baik |
| 2026-06-01 | Simulation Test (Redis) | ❌ Failed | Sentinel tidak otomatis failover (fixed) |

---
## 📌 9. Kontak Darurat
| Kontak | Peran | Telepon | Email | Slack |
|--------|-------|---------|-------|-------|
| Dhani Yuliawan | CTO / DR Coordinator | +62 813-6552-283 | dhani@musgo-os.com | @dhani |
| Tim Database | Database Engineer | - | db-team@musgo-os.com | @db-team |
| Tim DevOps | DevOps Engineer | - | devops-team@musgo-os.com | @devops-team |
| Tim Backend | Backend Engineer | - | backend-team@musgo-os.com | @backend-team |
| Tim Frontend | Frontend Engineer | - | frontend-team@musgo-os.com | @frontend-team |
| Tim Security | Security Engineer | - | security@musgo-os.com | @security-team |
| Tim Support | Support Lead | - | support@musgo-os.com | @support-team |

---
## 📌 10. Lampiran
- [Playbook: PostgreSQL Failover](#)
- [Playbook: Redis Failover](#)
- [Playbook: Kubernetes Failover](#)
- [Runbook: Backup & Restore](#)
- [Runbook: DR Testing](#)
- [Status Page: MusGo-OS](https://status.musgo-os.com)
- [Zapier Status Page](https://status.zapier.com)
```

---
---
---

## **🔹 12.7 DR Runbooks (Buku Perintah Teknis)**
### **📌 Penjelasan**
**Runbook** adalah **dokumen yang berisi perintah-perintah teknis** untuk **menjalankan tugas DR** (misal: restore database, failover, dll.).

---
#### **🚀 Contoh Implementasi: Runbooks**
##### **1. Runbook: Restore PostgreSQL dari Backup**
```markdown
# 📖 Runbook: Restore PostgreSQL dari Backup
**ID:** RB-001
**Versi:** 1.0
**Owner:** @db-team

---
## 📌 Prasyarat
- Akses ke **S3** (`musgo-os-backups`).
- Akses ke **PostgreSQL** (primary/standby).
- **Python 3.8+** terinstall.
- **psycopg2** terinstall (`pip install psycopg2-binary`).
- **boto3** terinstall (`pip install boto3`).

---
## 📌 Langkah-Langkah
### 1. Download Backup dari S3
```bash
# Download backup full terbaru
aws s3 cp s3://musgo-os-backups/postgres/full/ $(date +%Y%m%d)_.sql /tmp/latest_full_backup.sql \
  --access-key YOUR_AWS_ACCESS_KEY \
  --secret-key YOUR_AWS_SECRET_KEY

# Atau download backup tertentu
aws s3 cp s3://musgo-os-backups/postgres/full/20260519_020000.sql /tmp/specific_backup.sql \
  --access-key YOUR_AWS_ACCESS_KEY \
  --secret-key YOUR_AWS_SECRET_KEY
```

### 2. Stop PostgreSQL
```bash
# Jika menggunakan systemd
sudo systemctl stop postgresql

# Jika menggunakan Docker
docker stop postgres
```

### 3. Restore Backup
```bash
# Restore full backup
psql -U postgres -h localhost -p 5432 -d postgres -c "DROP DATABASE IF EXISTS musgo_os;"
psql -U postgres -h localhost -p 5432 -d postgres -c "CREATE DATABASE musgo_os;"
psql -U postgres -h localhost -p 5432 -d musgo_os -f /tmp/latest_full_backup.sql
```

### 4. Start PostgreSQL
```bash
# Jika menggunakan systemd
sudo systemctl start postgresql

# Jika menggunakan Docker
docker start postgres
```

### 5. Verifikasi Restore
```bash
# Cek database
psql -U postgres -h localhost -p 5432 -d musgo_os -c "SELECT count(*) FROM users;"

# Cek replikasi (jika menggunakan Patroni)
kubectl exec patroni-primary -n musgo-os -- patronictl list
```

---
## 📌 Troubleshooting
| Masalah | Solusi |
|---------|--------|
| **Permission denied** | Cek `chmod` dan `chown` file backup. |
| **Database already exists** | Hapus database terlebih dahulu (`DROP DATABASE musgo_os;`). |
| **psql: command not found** | Install PostgreSQL client (`sudo apt install postgresql-client`). |
| **Connection refused** | Cek apakah PostgreSQL berjalan (`sudo systemctl status postgresql`). |
| **Backup corrupted** | Coba backup lain atau restore dari WAL. |

---
## 📌 Catatan
- **Waktu Restore**: Tergantung ukuran database (contoh: 10GB → ~10 menit).
- **Data Loss**: Jika restore dari **full backup**, data sejak backup terakhir **akan hilang**.
- **PITR**: Untuk **minimalkan data loss**, gunakan **WAL backup** (lihat [RB-002](#)).
```

---
##### **2. Runbook: Failover PostgreSQL (Patroni)**
```markdown
# 📖 Runbook: Failover PostgreSQL (Patroni)
**ID:** RB-002
**Versi:** 1.0
**Owner:** @db-team

---
## 📌 Prasyarat
- **Patroni** terinstall dan berjalan.
- **HAProxy** terinstall dan berjalan.
- Akses ke **kubectl** (jika menggunakan Kubernetes).

---
## 📌 Langkah-Langkah
### 1. Cek Status Patroni
```bash
# Cek status cluster
kubectl exec patroni-primary -n musgo-os -- patronictl list

# Contoh output:
# + Cluster: musgo-os (7109451051054657937) -----+
# | Member | Host          | Role    | State   | TL | Lag in MB |
# +--------+---------------+---------+---------+----+----------+
# | node1  | 10.0.0.1:5432 | Leader  | running |  1 |          |
# | node2  | 10.0.0.2:5432 | Replica | running |  1 | 0        |
# +--------+---------------+---------+---------+----+----------+
```

### 2. Simulasikan Primary Down (Untuk Testing)
```bash
# Matikan Primary (jika testing)
kubectl exec patroni-primary -n musgo-os -- systemctl stop patroni
```

### 3. Monitor Failover Otomatis
```bash
# Cek apakah Standby dipromosikan
kubectl exec patroni-standby -n musgo-os -- patronictl list

# Contoh output (setelah failover):
# + Cluster: musgo-os (7109451051054657937) -----+
# | Member | Host          | Role    | State   | TL | Lag in MB |
# +--------+---------------+---------+---------+----+----------+
# | node1  | 10.0.0.1:5432 | Replica | running |  1 | 0        |
# | node2  | 10.0.0.2:5432 | Leader  | running |  1 |          |
# +--------+---------------+---------+---------+----+----------+
```

### 4. Cek HAProxy
```bash
# Cek apakah traffic dialihkan ke Primary baru
curl http://haproxy:7000/stats

# Contoh output:
# patroni-standby:5432,UP,1,1,2,3,0,0,,0,0,0,0,0,0,0
```

### 5. Verifikasi MusGo-OS
```bash
# Cek apakah backend berjalan normal
curl http://musgo-os-backend:8000/health

# Contoh output:
# {"status":"healthy"}
```

### 6. Failover Manual (Jika Otomatis Gagal)
```bash
# Promosikan Standby secara manual
kubectl exec patroni-standby -n musgo-os -- patronictl failover

# Atau:
kubectl exec patroni-standby -n musgo-os -- patronictl switchover
```

### 7. Hidupkan Kembali Primary (Setelah Failover)
```bash
# Start Primary
kubectl exec patroni-primary -n musgo-os -- systemctl start patroni

# Cek apakah Primary lama sekarang jadi Standby
kubectl exec patroni-primary -n musgo-os -- patronictl list
```

---
## 📌 Troubleshooting
| Masalah | Solusi |
|---------|--------|
| **Failover tidak otomatis** | Cek log Patroni (`kubectl logs patroni-standby -n musgo-os`). |
| **HAProxy tidak update** | Restart HAProxy (`kubectl rollout restart deployment/haproxy -n musgo-os`). |
| **MusGo-OS tidak terhubung** | Cek koneksi database di config MusGo-OS. |
| **Replikasi gagal** | Cek `pg_hba.conf` dan `replication` user. |

---
## 📌 Catatan
- **Waktu Failover**: ~30-60 detik (tergantung ukuran database).
- **Data Loss**: **Tidak ada** (Patroni menggunakan **synchronous replication**).
- **Downtime**: **< 1 menit** (jika HAProxy berjalan dengan baik).
```

---
##### **3. Runbook: Restore Kubernetes (Etcd)**
```markdown
# 📖 Runbook: Restore Kubernetes (Etcd)
**ID:** RB-003
**Versi:** 1.0
**Owner:** @devops-team

---
## 📌 Prasyarat
- Akses ke **S3** (`musgo-os-backups`).
- Akses ke **etcdctl**.
- **kubectl** terinstall.

---
## 📌 Langkah-Langkah
### 1. Download Backup Etcd dari S3
```bash
# Download backup terbaru
aws s3 cp s3://musgo-os-backups/etcd/ $(date +%Y%m%d_%H%M%S).db /tmp/latest_etcd_backup.db \
  --access-key YOUR_AWS_ACCESS_KEY \
  --secret-key YOUR_AWS_SECRET_KEY

# Atau download backup tertentu
aws s3 cp s3://musgo-os-backups/etcd/20260519_020000.db /tmp/specific_etcd_backup.db \
  --access-key YOUR_AWS_ACCESS_KEY \
  --secret-key YOUR_AWS_SECRET_KEY
```

### 2. Stop Kubernetes API Server
```bash
# Stop kubelet (di semua node)
sudo systemctl stop kubelet

# Atau (jika menggunakan Docker)
docker stop $(docker ps -q -f name=k8s_*)
```

### 3. Restore Etcd
```bash
# Restore Etcd
ETCDCTL_API=3 etcdctl snapshot restore /tmp/latest_etcd_backup.db \
  --data-dir=/var/lib/etcd \
  --initial-cluster=etcd-1=https://10.0.0.1:2380,etcd-2=https://10.0.0.2:2380 \
  --initial-advertise-peer-urls=https://10.0.0.1:2380 \
  --name=etcd-1
```

### 4. Start Kubernetes API Server
```bash
# Start kubelet (di semua node)
sudo systemctl start kubelet

# Atau (jika menggunakan Docker)
docker start $(docker ps -aq -f name=k8s_*)
```

### 5. Verifikasi Restore
```bash
# Cek apakah cluster berjalan normal
kubectl get nodes

# Cek apakah pod berjalan
kubectl get pods -n musgo-os

# Cek apakah Etcd sehat
ETCDCTL_API=3 etcdctl endpoint health --endpoints=https://127.0.0.1:2379
```

---
## 📌 Troubleshooting
| Masalah | Solusi |
|---------|--------|
| **etcdctl: command not found** | Install etcdctl (`sudo apt install etcd-client`). |
| **Permission denied** | Cek `chmod` dan `chown` file backup. |
| **Cluster tidak berjalan** | Cek log kubelet (`journalctl -u kubelet -f`). |
| **Pod tidak berjalan** | Cek apakah Etcd berjalan (`systemctl status etcd`). |

---
## 📌 Catatan
- **Waktu Restore**: ~5-10 menit (tergantung ukuran cluster).
- **Data Loss**: **Tidak ada** (jika backup terbaru).
- **Downtime**: **~10 menit** (tergantung ukuran cluster).
```

---
---
---

## **🔹 12.8 DR as a Service (DRaaS)**
### **📌 Penjelasan**
**DR as a Service (DRaaS)** adalah **layanan cloud** yang menyediakan **infrastructure untuk DR** tanpa perlu **setup sendiri**. Cocok untuk **MusGo-OS** jika:
- **Tidak ingin setup infrastructure standby**.
- **Ingin RTO & RPO yang baik** tanpa biaya besar.
- **Ingin otomatisasi DR**.

**Pilihan DRaaS:**
| Provider | Fitur | RTO | RPO | Biaya | Rekomendasi |
|----------|-------|-----|-----|-------|--------------|
| **AWS DR** | Multi-Region, Automated Failover | < 15 menit | < 1 menit | $$$ | ✅ **Jika menggunakan AWS** |
| **Google Cloud DR** | Multi-Region, Automated Failover | < 15 menit | < 1 menit | $$$ | ✅ **Jika menggunakan GCP** |
| **Azure Site Recovery** | Multi-Region, Automated Failover | < 15 menit | < 1 menit | $$$ | ✅ **Jika menggunakan Azure** |
| **Zerto** | Cross-Cloud, Automated Failover | < 1 menit | < 1 detik | $$$$ | ❌ **Terlalu mahal** |
| **Veeam** | Backup & Replication | < 1 jam | < 5 menit | $$ | ✅ **Untuk backup** |

---
#### **🚀 Contoh Implementasi: AWS DR**
**Arsitektur:**
```
AWS Region A (Primary)
│
├── MusGo-OS Backend (EC2)
├── MusGo-OS Frontend (EC2)
├── PostgreSQL (RDS Multi-AZ)
├── Redis (ElastiCache Multi-AZ)
│
└── Backup:
    ├── **RDS Snapshots** (Daily)
    ├── **EBS Snapshots** (Daily)
    ├── **S3 Versioning** (Untuk backup)

---
AWS Region B (Standby)
│
├── MusGo-OS Backend (EC2 - Stopped)
├── MusGo-OS Frontend (EC2 - Stopped)
├── PostgreSQL (RDS Read Replica)
├── Redis (ElastiCache Read Replica)
│
└── Failover:
    ├── **Promote Read Replica** (PostgreSQL)
    ├── **Start EC2** (Backend & Frontend)
    ├── **Update Route 53** (DNS Failover)
```

**Langkah-Langkah Setup:**
1. **Deploy MusGo-OS di AWS Region A** (Primary).
2. **Setup RDS Multi-AZ** (untuk PostgreSQL).
3. **Setup ElastiCache Multi-AZ** (untuk Redis).
4. **Setup Read Replica di AWS Region B** (untuk PostgreSQL dan Redis).
5. **Setup EBS Snapshots** (untuk EC2).
6. **Setup Route 53 Failover** (untuk DNS).
7. **Test Failover** (simulasikan Region A down).

**Contoh CloudFormation Template (AWS DR):**
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "MusGo-OS DR Setup (Multi-Region)"

Resources:
  # Primary Region (us-east-1)
  PrimaryRDS:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceIdentifier: musgo-os-primary
      AllocatedStorage: 100
      DBInstanceClass: db.t3.large
      Engine: postgres
      EngineVersion: "15.4"
      MasterUsername: postgres
      MasterUserPassword: "securepassword123"
      MultiAZ: true
      StorageType: gp2
      BackupRetentionPeriod: 7
      PreferredBackupWindow: "02:00-03:00"
      PreferredMaintenanceWindow: "Sun:03:00-Sun:04:00"
      EnableCloudwatchLogsExports:
        - postgresql
      Tags:
        - Key: Name
          Value: MusGo-OS Primary DB

  PrimaryElastiCache:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      CacheClusterId: musgo-os-primary-cache
      Engine: redis
      CacheNodeType: cache.t3.micro
      NumCacheNodes: 1
      AutoMinorVersionUpgrade: true
      SnapshotRetentionLimit: 7
      SnapshotWindow: "02:00-03:00"

  # Standby Region (us-west-2)
  StandbyRDS:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceIdentifier: musgo-os-standby
      AllocatedStorage: 100
      DBInstanceClass: db.t3.large
      Engine: postgres
      EngineVersion: "15.4"
      MasterUsername: postgres
      MasterUserPassword: "securepassword123"
      MultiAZ: true
      StorageType: gp2
      BackupRetentionPeriod: 7
      PreferredBackupWindow: "02:00-03:00"
      PreferredMaintenanceWindow: "Sun:03:00-Sun:04:00"
      ReadReplicaDBInstanceIdentifier: musgo-os-primary
      ReadReplicaDBInstanceRegion: us-east-1
      Tags:
        - Key: Name
          Value: MusGo-OS Standby DB

  StandbyElastiCache:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      CacheClusterId: musgo-os-standby-cache
      Engine: redis
      CacheNodeType: cache.t3.micro
      NumCacheNodes: 1
      AutoMinorVersionUpgrade: true
      SnapshotRetentionLimit: 7
      SnapshotWindow: "02:00-03:00"
      ReplicationGroupId: musgo-os-primary-cache

  # Route 53 Failover
  MusGoOSDNS:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: musgo-os.com

  MusGoOSRecord:
    Type: AWS::Route53::RecordSet
    Properties:
      HostedZoneId: !Ref MusGoOSDNS
      Name: api.musgo-os.com
      Type: A
      TTL: 300
      ResourceRecords:
        - !GetAtt PrimaryRDS.Endpoint.Address
      Failover: PRIMARY
      SetIdentifier: primary
      HealthCheckId: !Ref PrimaryHealthCheck

  StandbyRecord:
    Type: AWS::Route53::RecordSet
    Properties:
      HostedZoneId: !Ref MusGoOSDNS
      Name: api.musgo-os.com
      Type: A
      TTL: 300
      ResourceRecords:
        - !GetAtt StandbyRDS.Endpoint.Address
      Failover: SECONDARY
      SetIdentifier: standby

  PrimaryHealthCheck:
    Type: AWS::Route53::HealthCheck
    Properties:
      HealthCheckConfig:
        Type: HTTPS
        ResourcePath: /health
        FullyQualifiedDomainName: !GetAtt PrimaryRDS.Endpoint.Address
        Port: 5432
        RequestInterval: 30
        FailureThreshold: 3
      HealthCheckTags:
        - Key: Name
          Value: MusGo-OS Primary Health Check
```

**Cara Failover:**
1. **AWS otomatis** akan **deteksi primary down** (via Health Check).
2. **Route 53** akan **alihkan traffic** ke standby.
3. **Promosikan Read Replica** (jika diperlukan):
   ```bash
   aws rds promote-read-replica --db-instance-identifier musgo-os-standby
   ```
4. **Start EC2** (Backend & Frontend) di Region B.

---
---
---

## **🔹 12.9 DR for Zapier Integration**
### **📌 Penjelasan**
**DR for Zapier Integration** adalah **strategi untuk menangani** jika **Zapier API down** atau **MusGo-OS tidak bisa terhubung ke Zapier**.

**Strategi:**
| Strategi | Deskripsi | RTO | RPO | Implementasi |
|----------|-----------|-----|-----|--------------|
| **Circuit Breaker** | Hentikan panggilan ke Zapier jika gagal | < 1 menit | 0 | ✅ **Sudah diimplementasikan** |
| **Fallback Queue** | Simpan request ke queue (Redis/RabbitMQ) | < 5 menit | 0 | ✅ **Sudah diimplementasikan** |
| **Retry Mechanism** | Coba ulang request yang gagal | < 1 jam | 0 | ✅ **Sudah diimplementasikan** |
| **Local Cache** | Cache data Zapier (misal: daftar aplikasi) | < 1 jam | < 5 menit | ⚠️ **Perlu diimplementasikan** |
| **Alternative API** | Gunakan API alternatif (misal: Make.com) | < 1 jam | < 5 menit | ❌ **Belum diperlukan** |

---
#### **🚀 Contoh Implementasi: DR for Zapier**
##### **1. Local Cache untuk Zapier Apps**
**Contoh Kode (Python - FastAPI + Cache):**
```python
# File: backend/zapier_cache.py
from fastapi import FastAPI, HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
import httpx
import time

app = FastAPI()

# Setup Redis Cache
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://redis:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

# Cache daftar aplikasi Zapier (TTL: 1 jam)
@cache(expire=3600)
async def get_zapier_apps(api_key: str):
    """Ambil daftar aplikasi Zapier (dengan cache)"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.zapier.com/v2/apps",
            headers=headers
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Gagal mengambil aplikasi Zapier")

        return response.json().get("apps", [])

# Cache daftar action untuk aplikasi (TTL: 1 jam)
@cache(expire=3600)
async def get_zapier_app_actions(api_key: str, app_key: str):
    """Ambil daftar action untuk aplikasi (dengan cache)"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.zapier.com/v2/apps/{app_key}/actions",
            headers=headers
        )

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail=f"Gagal mengambil action untuk {app_key}")

        return response.json().get("actions", [])

# Contoh penggunaan
@app.get("/zapier/apps")
async def list_apps(api_key: str):
    try:
        apps = await get_zapier_apps(api_key)
        return {"apps": apps}
    except Exception as e:
        # Jika cache ada, gunakan cache
        try:
            apps = await FastAPICache.get(f"fastapi-cache:get_zapier_apps:{api_key}")
            return {"apps": apps, "cached": True}
        except:
            raise HTTPException(status_code=503, detail="Zapier API dan cache gagal")
```

---
##### **2. Alternative API (Make.com)**
**Jika Zapier down**, MusGo-OS bisa **beralih ke Make.com** (alternatif Zapier).

**Contoh Kode (Python):**
```python
# File: backend/fallback_automation.py
import httpx
from typing import Dict, Any, Optional

class MakeComClient:
    """Klien untuk Make.com (alternatif Zapier)"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://hook.make.com"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def run_scenario(self, scenario_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan scenario di Make.com"""
        url = f"{self.base_url}/{scenario_id}"

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=self.headers)

            if response.status_code != 200:
                raise Exception(f"Make.com API Error: {response.status_code} - {response.text}")

            return response.json()

class ZapierClient:
    """Klien untuk Zapier (dengan fallback ke Make.com)"""
    def __init__(self, zapier_api_key: str, make_api_key: Optional[str] = None):
        self.zapier_api_key = zapier_api_key
        self.make_api_key = make_api_key
        self.make_client = MakeComClient(make_api_key) if make_api_key else None

    async def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action (dengan fallback ke Make.com)"""
        try:
            # Coba Zapier terlebih dahulu
            headers = {
                "Authorization": f"Bearer {self.zapier_api_key}",
                "Content-Type": "application/json",
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.zapier.com/v2/actions/run",
                    json={"app": app, "action": action, "data": data},
                    headers=headers,
                    timeout=5
                )

                if response.status_code != 200:
                    raise Exception(f"Zapier API Error: {response.status_code}")

                return response.json()
        except Exception as e:
            if self.make_client:
                # Fallback ke Make.com
                try:
                    # Mapping action Zapier ke Make.com
                    make_scenario = self._map_zapier_to_make(app, action)
                    if make_scenario:
                        return await self.make_client.run_scenario(make_scenario, data)
                except Exception as make_error:
                    raise Exception(f"Zapier dan Make.com gagal: {e}, {make_error}")
            else:
                raise Exception(f"Zapier API gagal: {e}")

    def _map_zapier_to_make(self, app: str, action: str) -> Optional[str]:
        """Mapping action Zapier ke Make.com scenario ID"""
        mapping = {
            ("slack", "Send Channel Message"): "MAKE_SCENARIO_SLACK_SEND_MESSAGE",
            ("google_drive", "New File in Folder"): "MAKE_SCENARIO_GOOGLE_DRIVE_NEW_FILE",
            ("trello", "Create Card"): "MAKE_SCENARIO_TRELLO_CREATE_CARD",
        }
        return mapping.get((app, action))
```

**Cara Gunakan:**
```python
# Inisialisasi
zapier_client = ZapierClient(
    zapier_api_key="YOUR_ZAPIER_API_KEY",
    make_api_key="YOUR_MAKE_API_KEY"  # Opsional
)

# Jalankan action (dengan fallback)
try:
    result = await zapier_client.run_action(
        app="slack",
        action="Send Channel Message",
        data={"channel": "#musgo-updates", "text": "Halo!"}
    )
    print("Action berjalan:", result)
except Exception as e:
    print("Error:", e)
```

---
---
---
# **📌 PART 12: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 12 (Disaster Recovery)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **Backup & Restore** | PostgreSQL, Redis, Etcd | Pulihkan data jika hilang | ✅ **Contoh kode tersedia** |
| **Failover & HA** | Patroni, Sentinel, Federation | Minimalkan downtime | ✅ **Contoh kode tersedia** |
| **DR Strategy** | Pilot Light, Warm Standby | RTO & RPO terukur | ✅ **Dokumentasi tersedia** |
| **DR Testing** | Tabletop, Simulation, Full Interruption | Verifikasi DR Plan | ✅ **Contoh skrip tersedia** |
| **DR Documentation** | DR Plan, Playbooks, Runbooks | Panduan penanganan bencana | ✅ **Contoh dokumen tersedia** |
| **DRaaS** | AWS DR, Google Cloud DR | DR tanpa setup infrastructure | ✅ **Contoh CloudFormation** |
| **Zapier DR** | Circuit Breaker, Fallback Queue | Tangani Zapier outage | ✅ **Contoh kode tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Setup Backup Otomatis** (PostgreSQL, Redis, Etcd).
- [ ] **Test Restore** (Verifikasi backup bisa direstore).
- [ ] **Setup Failover Otomatis** (Patroni, Sentinel).
- [ ] **Buat DR Documentation** (DR Plan, Playbooks, Runbooks).
- [ ] **Setup Circuit Breaker** (Untuk Zapier integration).

### **2. Mid-Term (1 Bulan)**
- [ ] **Lakukan DR Testing** (Simulation Test).
- [ ] **Setup Monitoring untuk DR** (Alert jika failover gagal).
- [ ] **Setup Local Cache** (Untuk Zapier apps/actions).
- [ ] **Setup Alternative API** (Make.com sebagai fallback).
- [ ] **Train Tim** (DR Training).

### **3. Long-Term (3+ Bulan)**
- [ ] **Lakukan Full Interruption Test** (Uji penuh di staging).
- [ ] **Setup DRaaS** (Jika budget cukup).
- [ ] **Automasi DR** (Otomatis failover, restore, dll.).
- [ ] **Review & Update DR Plan** (Setiap 6 bulan).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 13: Business Continuity Plan (BCP)** (Untuk kelangsungan bisnis)
   - [ ] **Part 14: Security Hardening** (Untuk pengamanan DR)
   - [ ] **Part 15: Cost Optimization** (Untuk optimasi biaya DR)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full setup DR untuk production)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full DR Plan untuk MusGo-OS**?
   - [ ] **Dokumentasi Lengkap Playbooks & Runbooks**?
   - [ ] **Skrip Otomatisasi DR (Backup, Restore, Failover)**?

3. **Apakah ada area DR spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Backup PostgreSQL**, **Failover Patroni**, **DR Testing**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 13: Business Continuity Plan (BCP)** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **kelangsungan bisnis (Business Continuity)** di **MusGo-OS 2in1 + Zapier**, termasuk **strategi, prosedur, dan integrasi dengan DR Plan**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN BUSINESS CONTINUITY PLAN (BCP) (PART 13)**
*Terjemahan + Implementasi untuk Kelangsungan Bisnis Production-Ready*

---

---

## **🔹 13.1 Overview Business Continuity Plan (BCP)**
### **📌 Penjelasan (Bahasa Indonesia)**
**Business Continuity Plan (BCP)** adalah **rencana komprehensif** untuk **memastikan MusGo-OS tetap beroperasi** atau **cepat pulih** setelah terjadinya **gangguan (disruption)**, seperti:
- **Bencana alam** (banjir, gempa, kebakaran).
- **Bencana buatan manusia** (cyber attack, human error, kebakaran).
- **Kegagalan teknis** (server crash, network outage, cloud provider down).
- **Pandemi** (COVID-19, dll.).

**Tujuan BCP untuk MusGo-OS:**
✅ **Minimalkan Dampak Bisnis**: Pastikan **user tetap bisa menggunakan MusGo-OS** meskipun terjadi gangguan.
✅ **Kelangsungan Operasional**: **Fitur kritis** (AI Agent, Otomatisasi) tetap berjalan.
✅ **Pemulihan Cepat**: **RTO (Recovery Time Objective)** dan **RPO (Recovery Point Objective)** terukur.
✅ **Kepatuhan Regulasi**: Patuhi **GDPR, SOC 2, ISO 22301** (Business Continuity Standard).
✅ **Kepercayaan User**: **User tetap percaya** bahwa MusGo-OS **reliable**.

**Perbedaan BCP vs DRP:**
| Aspek | BCP (Business Continuity Plan) | DRP (Disaster Recovery Plan) |
|-------|--------------------------------|-------------------------------|
| **Tujuan** | Memastikan **bisnis tetap berjalan** | Memulihkan **sistem IT** |
| **Cakupan** | **Seluruh bisnis** (people, process, technology) | **Hanya IT** (backup, failover, restore) |
| **Fokus** | **Kelangsungan operasional** | **Pemulihan sistem** |
| **Waktu** | **Sebelum, selama, sesudah** gangguan | **Selama dan sesudah** gangguan |
| **Contoh** | Rencana kerja dari rumah, backup office | Restore database, failover server |

---
### **🚀 Contoh Arsitektur BCP untuk MusGo-OS**
```
Gangguan Terjadi (Misal: Cloud Outage)
│
├── **Deteksi** (Monitoring: Prometheus, Grafana, Sentry)
│
├── **Aktivasi BCP** (Incident Commander: Dhani)
│   │
│   ├── **Kelangsungan Operasional**
│   │   ├── **AI Agent**: Berjalan di **Cluster B** (Warm Standby)
│   │   ├── **Otomatisasi**: Gunakan **Fallback Queue** (Redis)
│   │   ├── **User Support**: **Remote Support Team** (Slack, Zoom)
│   │   └── **Komunikasi**: **Status Page** + **Email Broadcast**
│   │
│   └── **Pemulihan Sistem** (DRP: Part 12)
│       ├── **Failover**: Patroni (PostgreSQL), Sentinel (Redis)
│       ├── **Restore**: Backup (S3) → Cluster B
│       └── **Testing**: Verifikasi sistem berjalan normal
│
└── **Kembali ke Normal** (Post-BCP Review)
    ├── **Post-Mortem**: Analisis root cause
    ├── **Perbaikan**: Fix vulnerability
    └── **Update BCP**: Perbaiki prosedur
```

---
---
---

## **🔹 13.2 BCP Framework (Kerangka Kerja BCP)**
### **📌 Penjelasan**
**BCP Framework** adalah **kerangka kerja** untuk **membangun, mengimplementasikan, dan mengelola BCP**. Framework yang umum digunakan:
1. **ISO 22301** (Standar internasional untuk BCP).
2. **FFIEC BCP Handbook** (Untuk industri keuangan).
3. **NFPA 1600** (Standar untuk BCP di AS).

**Framework untuk MusGo-OS:**
1. **BCP Governance** (Kebijakan, peran, tanggung jawab).
2. **Business Impact Analysis (BIA)** (Analisis dampak gangguan).
3. **Risk Assessment (RA)** (Identifikasi risiko).
4. **BCP Strategies** (Strategi kelangsungan bisnis).
5. **BCP Procedures** (Prosedur penanganan gangguan).
6. **Testing & Exercising** (Uji coba BCP).
7. **Maintenance & Review** (Pemeliharaan BCP).

---
#### **🚀 Contoh Implementasi: BCP Framework**
##### **1. BCP Governance (Tata Kelola BCP)**
**Dokumen Kebijakan BCP:**
```markdown
# 📜 MusGo-OS 2in1: Kebijakan Business Continuity (BCP)
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan (CTO)

---
## 📌 1. Tujuan
Kebijakan ini mendefinisikan **tata kelola Business Continuity Plan (BCP)** untuk **MusGo-OS 2in1**, termasuk:
- Peran dan tanggung jawab.
- Proses pengembangan dan pemeliharaan BCP.
- Kepatuhan terhadap regulasi.

---
## 📌 2. Ruang Lingkup
Kebijakan ini berlaku untuk:
- **Semua karyawan MusGo-OS**.
- **Semua sistem dan layanan MusGo-OS** (Backend, Frontend, Database, Zapier Integration).
- **Semua mitra dan vendor** yang terlibat dalam operasional MusGo-OS.

---
## 📌 3. Peran dan Tanggung Jawab
| Peran | Tanggung Jawab | Kontak |
|-------|----------------|--------|
| **BCP Owner** | Bertanggung jawab atas BCP, memastikan BCP selalu up-to-date | @dhani |
| **BCP Committee** | Mengembangkan, menguji, dan mereview BCP | @bcp-committee |
| **Incident Commander** | Memimpin penanganan insiden dan aktivasi BCP | @dhani |
| **Business Unit Leads** | Memastikan kelangsungan operasional unit bisnis | @product-team, @engineering-team |
| **IT/DevOps Team** | Implementasi DRP dan pemulihan sistem | @devops-team |
| **HR Team** | Koordinasi karyawan (misal: kerja dari rumah) | @hr-team |
| **Komunikasi Team** | Komunikasi internal dan eksternal | @comms-team |
| **Vendor/Partner** | Dukungan teknis (misal: AWS, Zapier) | Kontak vendor |

---
## 📌 4. Proses BCP
### 4.1 Pengembangan BCP
1. **Business Impact Analysis (BIA)**: Identifikasi **proses kritis** dan **dampak gangguan**.
2. **Risk Assessment (RA)**: Identifikasi **risiko** dan **mitigasi**.
3. **Pengembangan Strategi BCP**: Tentukan **strategi kelangsungan bisnis**.
4. **Pengembangan Prosedur BCP**: Buat **prosedur penanganan gangguan**.
5. **Review & Approval**: Review oleh **BCP Committee** dan **Executive Team**.

### 4.2 Pemeliharaan BCP
- **Review BCP**: Setiap **6 bulan** atau setelah **insiden besar**.
- **Update BCP**: Jika ada **perubahan bisnis** (misal: fitur baru, perubahan arsitektur).
- **Testing BCP**: **Setiap 3 bulan** (Tabletop Exercise) dan **setiap 1 tahun** (Full Test).

### 4.3 Aktivasi BCP
- **Incident Commander** (Dhani) **mendeklarasikan aktivasi BCP** jika:
  - **SEV-1**: Sistem **tidak berfungsi** > 15 menit.
  - **SEV-2**: Fitur **kritis terganggu** > 30 menit.
  - **Bencana alam/buatan**: Gangguan **skala besar** (misal: cloud outage, pandemi).
- **Komunikasi ke tim**: Via **Slack (`#bcp-activation`)** dan **Email**.

### 4.4 Deaktivasi BCP
- **Incident Commander** **mendeklarasikan deaktivasi BCP** jika:
  - Sistem **kembali berjalan normal**.
  - **RTO tercapai** (misal: < 1 jam untuk SEV-1).
- **Komunikasi ke tim**: Via **Slack (`#bcp-deactivation`)** dan **Email**.

---
## 📌 5. Kepatuhan
- **ISO 22301**: Standar internasional untuk BCP.
- **GDPR**: Perlindungan data user (jika terjadi data breach).
- **SOC 2**: Kepatuhan untuk **security, availability, processing integrity**.

---
## 📌 6. Referensi
- [ISO 22301:2019 (Business Continuity)](https://www.iso.org/standard/75106.html)
- [FFIEC BCP Handbook](https://www.ffiec.gov/publications/bcp-handbook)
- [NFPA 1600](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=1600)
```

---
---
---

## **🔹 13.3 Business Impact Analysis (BIA)**
### **📌 Penjelasan**
**Business Impact Analysis (BIA)** adalah **proses mengidentifikasi**:
- **Proses bisnis kritis** (Critical Business Functions).
- **Dampak gangguan** (financial, reputasi, operasional).
- **RTO (Recovery Time Objective)** dan **RPO (Recovery Point Objective)**.
- **Ketergantungan** (dependencies) antar proses.

**Manfaat BIA untuk MusGo-OS:**
- **Identifikasi proses kritis** (misal: AI Agent, Otomatisasi Zapier).
- **Prioritaskan pemulihan** (misal: AI Agent > Dashboard).
- **Alokasi resource** (misal: backup lebih sering untuk data kritis).

---
#### **🚀 Contoh Implementasi: BIA**
##### **1. Daftar Proses Bisnis MusGo-OS**
| ID | Proses Bisnis | Deskripsi | Kritis? | RTO | RPO | Ketergantungan |
|----|---------------|-----------|---------|-----|-----|---------------|
| **P-001** | AI Agent Execution | Menjalankan AI Agent (planner, executor, dll.) | ✅ **Ya** | < 1 jam | < 5 menit | PostgreSQL, Redis, Zapier API |
| **P-002** | Zapier Integration | Integrasi dengan Zapier (trigger, action) | ✅ **Ya** | < 1 jam | < 5 menit | Zapier API, Webhooks |
| **P-003** | User Authentication | Login/Logout user | ✅ **Ya** | < 30 menit | < 1 menit | PostgreSQL, JWT |
| **P-004** | Automation Workflows | Pembuatan dan eksekusi Zap | ✅ **Ya** | < 1 jam | < 5 menit | Zapier API, PostgreSQL |
| **P-005** | Dashboard | UI untuk user | ❌ **Tidak** | < 4 jam | < 15 menit | Frontend, Backend |
| **P-006** | Billing & Subscription | Manajemen langganan user | ✅ **Ya** | < 2 jam | < 1 menit | PostgreSQL, Payment Gateway |
| **P-007** | Support & Helpdesk | Dukungan user (Slack, Email) | ✅ **Ya** | < 1 jam | < 1 menit | Slack, Email, Zendesk |
| **P-008** | Documentation | Dokumentasi untuk user | ❌ **Tidak** | < 24 jam | < 1 jam | GitHub, Markdown |

---
##### **2. Dampak Gangguan (Impact Assessment)**
| Proses Bisnis | Dampak (1 Jam) | Dampak (4 Jam) | Dampak (24 Jam) | Dampak (7 Hari) |
|---------------|---------------|----------------|----------------|-----------------|
| **AI Agent Execution** | User tidak bisa menjalankan AI Agent | User beralih ke manual process | Kehilangan user (churn) | **Kehilangan bisnis** (revenue drop) |
| **Zapier Integration** | Otomatisasi terhenti | User beralih ke manual process | Kehilangan user (churn) | **Kehilangan bisnis** (revenue drop) |
| **User Authentication** | User tidak bisa login | User frustrasi | **Churn meningkat** | **Reputasi rusak** |
| **Automation Workflows** | User tidak bisa membuat Zap | User beralih ke kompetitor | **Churn meningkat** | **Kehilangan bisnis** |
| **Dashboard** | User tidak bisa melihat data | User frustrasi | **Churn meningkat** | Kehilangan user |
| **Billing & Subscription** | User tidak bisa bayar | **Revenue hilang** | **Revenue hilang besar** | **Bisnis gagal** |
| **Support & Helpdesk** | User tidak mendapatkan bantuan | User frustrasi | **Churn meningkat** | **Reputasi rusak** |
| **Documentation** | User tidak bisa belajar | Tidak ada dampak signifikan | Tidak ada dampak signifikan | Tidak ada dampak signifikan |

---
##### **3. Prioritas Pemulihan (Recovery Priority)**
| Prioritas | Proses Bisnis | RTO | RPO | Alasan |
|-----------|---------------|-----|-----|--------|
| **P-1 (Critical)** | AI Agent Execution | < 1 jam | < 5 menit | **Inti dari MusGo-OS** |
| **P-1 (Critical)** | Zapier Integration | < 1 jam | < 5 menit | **Inti dari otomatisasi** |
| **P-1 (Critical)** | User Authentication | < 30 menit | < 1 menit | **User tidak bisa akses** |
| **P-1 (Critical)** | Billing & Subscription | < 2 jam | < 1 menit | **Revenue hilang** |
| **P-2 (High)** | Automation Workflows | < 1 jam | < 5 menit | **User beralih ke manual** |
| **P-2 (High)** | Support & Helpdesk | < 1 jam | < 1 menit | **User frustrasi** |
| **P-3 (Medium)** | Dashboard | < 4 jam | < 15 menit | **User bisa menggunakan CLI** |
| **P-4 (Low)** | Documentation | < 24 jam | < 1 jam | **Tidak kritis** |

---
##### **4. Ketergantungan (Dependencies)**
**Dependency Map untuk MusGo-OS:**
```
AI Agent Execution (P-001)
│
├── PostgreSQL (Database)
│   ├── Primary (Cluster A)
│   └── Standby (Cluster B)
│
├── Redis (Caching)
│   ├── Primary (Cluster A)
│   └── Replica (Cluster B)
│
├── Zapier API (Integration)
│   └── Fallback: Make.com
│
└── Kubernetes (Orchestration)
    ├── Cluster A (Primary)
    └── Cluster B (Standby)

---
Zapier Integration (P-002)
│
├── Zapier API
│   └── Fallback: Make.com
│
├── Webhooks (MusGo-OS)
│   └── Backend (Cluster A/B)
│
└── Database (PostgreSQL)
    ├── Primary (Cluster A)
    └── Standby (Cluster B)

---
User Authentication (P-003)
│
├── PostgreSQL (Database)
│   ├── Primary (Cluster A)
│   └── Standby (Cluster B)
│
└── JWT (Token)
    └── Secret Key (Kubernetes Secret)
```

---
##### **5. BIA Report (Laporan BIA)**
**Contoh Laporan BIA (Ringkasan):**
```markdown
# 📊 MusGo-OS 2in1: Business Impact Analysis (BIA) Report
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan

---
## 📌 Ringkasan
- **Total Proses Bisnis**: 8
- **Proses Kritis (P-1)**: 4 (AI Agent, Zapier Integration, User Auth, Billing)
- **Proses High (P-2)**: 2 (Automation Workflows, Support)
- **Proses Medium (P-3)**: 1 (Dashboard)
- **Proses Low (P-4)**: 1 (Documentation)

---
## 📌 Dampak Gangguan
| Dampak | Proses Terpengaruh | Waktu Gangguan | Kerugian Estimasi |
|--------|--------------------|----------------|-------------------|
| **Revenue Hilang** | Billing & Subscription | > 2 jam | $10,000/hari |
| **Churn Meningkat** | AI Agent, Zapier Integration, Automation | > 4 jam | 5% user/hari |
| **Reputasi Rusak** | User Authentication, Support | > 1 jam | Sulit diukur |
| **Operasional Terhenti** | Semua proses | > 1 hari | $50,000/hari |

---
## 📌 Rekomendasi
1. **Prioritaskan pemulihan** untuk **P-1 (Critical)**.
2. **Setup Warm Standby** untuk **AI Agent, Zapier Integration, User Auth**.
3. **Setup Fallback Mechanism** untuk **Zapier API** (Make.com).
4. **Tingkatkan monitoring** untuk **P-1 dan P-2**.
5. **Lakukan DR Testing** untuk **P-1** setiap **3 bulan**.
```

---
---
---

## **🔹 13.4 Risk Assessment (RA)**
### **📌 Penjelasan**
**Risk Assessment (RA)** adalah **proses mengidentifikasi, menganalisis, dan mengevaluasi risiko** yang dapat **mengganggu kelangsungan bisnis MusGo-OS**.

**Metodologi RA:**
1. **Identifikasi Risiko**: Daftar semua **risiko potensial**.
2. **Analisis Risiko**: Ukur **probabilitas** dan **dampak**.
3. **Evaluasi Risiko**: Tentukan **risk level** (High, Medium, Low).
4. **Mitigasi Risiko**: Tentukan **strategi mitigasi**.

---
#### **🚀 Contoh Implementasi: Risk Assessment**
##### **1. Daftar Risiko untuk MusGo-OS**
| ID | Risiko | Kategori | Probabilitas | Dampak | Risk Level | Mitigasi |
|----|--------|----------|--------------|--------|------------|----------|
| **R-001** | Cloud Provider Outage (AWS/GCP) | Teknis | Medium | High | **High** | Multi-Cloud (AWS + GCP) |
| **R-002** | Zapier API Outage | Eksternal | Medium | High | **High** | Fallback ke Make.com |
| **R-003** | PostgreSQL Crash | Teknis | Low | Critical | **High** | Replikasi (Patroni) + Backup |
| **R-004** | Redis Crash | Teknis | Low | High | **Medium** | Replikasi (Sentinel) + Backup |
| **R-005** | Kubernetes Cluster Down | Teknis | Low | Critical | **High** | Multi-Cluster (Federation) |
| **R-006** | Cyber Attack (DDoS, Ransomware) | Keamanan | Low | Critical | **High** | WAF, Firewall, Backup |
| **R-007** | Human Error (Misconfig, Delete Data) | Operasional | Medium | High | **High** | RBAC, Audit Logging, Backup |
| **R-008** | Pandemi (COVID-19) | Eksternal | Low | High | **Medium** | Remote Work Policy |
| **R-009** | Vendor Lock-in (Zapier) | Bisnis | Medium | High | **High** | Multi-Provider (Zapier + Make.com) |
| **R-010** | Data Breach | Keamanan | Low | Critical | **High** | Encryption, Access Control, Audit |

---
##### **2. Risk Matrix**
**Contoh Risk Matrix (Probabilitas vs Dampak):**

| **Dampak \ Probabilitas** | **Low** | **Medium** | **High** |
|--------------------------|---------|------------|----------|
| **Low**                  | Low     | Low        | Medium   |
| **Medium**               | Low     | Medium     | **High** |
| **High**                 | Medium  | **High**   | **High** |
| **Critical**             | Medium  | **High**   | **High** |

**Keterangan:**
- **High Risk**: **R-001, R-002, R-003, R-005, R-006, R-007, R-009, R-010**
- **Medium Risk**: **R-004, R-008**
- **Low Risk**: Tidak ada

---
##### **3. Risk Treatment (Penanganan Risiko)**
| Risiko | Strategi Mitigasi | Owner | Deadline | Status |
|--------|---------------------|-------|----------|--------|
| **R-001** | Multi-Cloud (AWS + GCP) | @devops-team | 2026-06-19 | ⬜ To Do |
| **R-002** | Fallback ke Make.com | @backend-team | 2026-05-26 | ✅ Done |
| **R-003** | Replikasi (Patroni) + Backup | @db-team | 2026-05-26 | ✅ Done |
| **R-004** | Replikasi (Sentinel) + Backup | @db-team | 2026-05-26 | ✅ Done |
| **R-005** | Multi-Cluster (Federation) | @devops-team | 2026-06-19 | ⬜ To Do |
| **R-006** | WAF (Cloudflare) + Backup | @security-team | 2026-06-19 | ⬜ To Do |
| **R-007** | RBAC + Audit Logging | @security-team | 2026-05-26 | ✅ Done |
| **R-008** | Remote Work Policy | @hr-team | 2026-05-26 | ✅ Done |
| **R-009** | Multi-Provider (Zapier + Make.com) | @product-team | 2026-06-19 | ⬜ To Do |
| **R-010** | Encryption + Access Control | @security-team | 2026-06-19 | ⬜ To Do |

---
##### **4. Risk Register (Daftar Risiko)**
**Contoh Risk Register (Spreadsheet):**

| **ID** | **Risiko** | **Kategori** | **Probabilitas** | **Dampak** | **Risk Level** | **Mitigasi** | **Owner** | **Status** | **Review Date** |
|--------|------------|--------------|------------------|------------|----------------|--------------|-----------|------------|-----------------|
| R-001 | Cloud Provider Outage | Teknis | Medium | High | High | Multi-Cloud | @devops-team | To Do | 2026-07-19 |
| R-002 | Zapier API Outage | Eksternal | Medium | High | High | Fallback ke Make.com | @backend-team | Done | 2026-08-19 |
| R-003 | PostgreSQL Crash | Teknis | Low | Critical | High | Patroni + Backup | @db-team | Done | 2026-08-19 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---
---
---

## **🔹 13.5 BCP Strategies (Strategi Kelangsungan Bisnis)**
### **📌 Penjelasan**
**BCP Strategies** adalah **strategi yang dipilih** untuk **memastikan kelangsungan bisnis** selama gangguan. Strategi dipilih berdasarkan:
- **BIA** (dampak gangguan).
- **RA** (risiko).
- **Biaya** (budget).
- **Kompleksitas** (kesulitan implementasi).

**Strategi BCP untuk MusGo-OS:**
| Strategi | Deskripsi | Proses Bisnis | Biaya | Kompleksitas | Rekomendasi |
|----------|-----------|---------------|-------|--------------|--------------|
| **Redundancy** | Duplikasi sistem (misal: Multi-Cluster) | AI Agent, Zapier Integration | $$$ | Tinggi | ✅ **Untuk P-1** |
| **Diversification** | Gunakan multiple provider (misal: Zapier + Make.com) | Zapier Integration | $$ | Sedang | ✅ **Untuk P-1** |
| **Alternate Processing Site** | Gunakan office backup (misal: Co-Working Space) | Support, Development | $ | Rendah | ✅ **Untuk P-2** |
| **Remote Work** | Kerja dari rumah | Semua proses | $ | Rendah | ✅ **Untuk semua** |
| **Manual Workaround** | Proses manual (misal: Excel) | Billing, Support | $ | Rendah | ✅ **Untuk P-3/P-4** |
| **Third-Party Backup** | Gunakan layanan backup (misal: AWS Backup) | Semua data | $$ | Sedang | ✅ **Untuk semua** |

---
#### **🚀 Contoh Implementasi: BCP Strategies**
##### **1. Redundancy (AI Agent)**
**Strategi:**
- **Deploy AI Agent di 2 Cluster** (Primary + Standby).
- **Gunakan Load Balancer** (Nginx, HAProxy) untuk **distribusi traffic**.
- **Auto-Failover** (Kubernetes Federation).

**Arsitektur:**
```
User → Load Balancer → Kubernetes Cluster A (Primary) → AI Agent
                     ↓
               Kubernetes Cluster B (Standby) → AI Agent
```

**Implementasi:**
- **Kubernetes Federation** (lihat [Part 12.4](#124-failover--high-availability)).
- **Load Balancer** (Nginx, HAProxy).
- **Auto-Scaling** (Horizontal Pod Autoscaler).

---
##### **2. Diversification (Zapier Integration)**
**Strategi:**
- **Gunakan 2 Provider Otomatisasi**: **Zapier (Primary) + Make.com (Fallback)**.
- **Circuit Breaker** (Jika Zapier down, beralih ke Make.com).

**Implementasi:**
- **Fallback Mechanism** (lihat [Part 12.9](#129-dr-for-zapier-integration)).
- **Multi-Provider Support** (AI Agent bisa memanggil Zapier atau Make.com).

---
##### **3. Alternate Processing Site (Support Team)**
**Strategi:**
- **Setup Office Backup** (Co-Working Space) untuk **Support Team**.
- **Gunakan Laptop + Hotspot** jika internet down.

**Implementasi:**
- **Daftar Co-Working Space** (misal: WeWork, GoWork).
- **Setup VPN** untuk akses sistem internal.
- **Test Koneksi** (setiap 3 bulan).

---
##### **4. Remote Work (Semua Tim)**
**Strategi:**
- **Kerja dari Rumah (WFH)** jika kantor tidak bisa diakses.
- **Gunakan Tools Kolaborasi** (Slack, Zoom, Notion).

**Implementasi:**
- **Remote Work Policy** (lihat [Bagian 13.6.1](#1361-remote-work-policy)).
- **Setup VPN** (OpenVPN, WireGuard).
- **Laptop Company** (untuk semua karyawan).

---
##### **5. Manual Workaround (Billing)**
**Strategi:**
- **Gunakan Spreadsheet** (Google Sheets, Excel) untuk **manajemen billing** jika sistem down.
- **Proses Pembayaran Manual** (Transfer bank, dll.).

**Implementasi:**
- **Template Spreadsheet** (untuk billing).
- **SOP Manual Billing** (dokumentasi langkah-langkah).

---
##### **6. Third-Party Backup (AWS Backup)**
**Strategi:**
- **Gunakan AWS Backup** untuk **backup otomatis** (PostgreSQL, EBS, dll.).
- **Cross-Region Replication** (untuk redundancy).

**Implementasi:**
- **AWS Backup Plan** (lihat [Part 12.8](#128-draas)).
- **Cross-Region Replication** (untuk S3, EBS).

---
---
---

## **🔹 13.6 BCP Procedures (Prosedur Kelangsungan Bisnis)**
### **📌 Penjelasan**
**BCP Procedures** adalah **langkah-langkah detail** untuk **menjalankan BCP** selama gangguan. Prosedur meliputi:
- **Aktivasi BCP**.
- **Kelangsungan Operasional**.
- **Komunikasi**.
- **Pemulihan**.
- **Deaktivasi BCP**.

---
#### **🚀 Contoh Implementasi: BCP Procedures**
##### **1. Remote Work Policy**
**Dokumen Kebijakan Kerja Jarak Jauh:**
```markdown
# 📜 MusGo-OS 2in1: Remote Work Policy
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** @hr-team

---
## 📌 1. Tujuan
Kebijakan ini mendefinisikan **aturan dan prosedur** untuk **kerja jarak jauh (Remote Work)** di MusGo-OS, termasuk:
- Kapan Remote Work diperbolehkan.
- Persyaratan untuk Remote Work.
- Tools dan infrastructure yang diperlukan.

---
## 📌 2. Ruang Lingkup
Kebijakan ini berlaku untuk:
- **Semua karyawan MusGo-OS**.
- **Kontraktor dan mitra** yang bekerja untuk MusGo-OS.

---
## 📌 3. Kapan Remote Work Diperbolehkan
| Situasi | Remote Work Diperbolehkan? | Persetujuan |
|---------|-----------------------------|-------------|
| **Pandemi (COVID-19)** | ✅ Ya | Otomatis (dari HR) |
| **Bencana Alam** | ✅ Ya | Otomatis (dari HR) |
| **Kantor Tidak Aksesibel** | ✅ Ya | Otomatis (dari HR) |
| **Kesehatan Pribadi** | ✅ Ya | Persetujuan Manager |
| **Productivity Boost** | ❌ Tidak | - |
| **Liburan** | ❌ Tidak | - |

---
## 📌 4. Persyaratan Remote Work
### 4.1 Persyaratan Teknis
| Persyaratan | Deskripsi | Tanggung Jawab |
|-------------|-----------|-----------------|
| **Laptop** | Laptop company (MacBook/ThinkPad) | IT Team |
| **Internet** | Koneksi internet stabil (min. 10 Mbps) | Karyawan |
| **VPN** | Akses VPN (OpenVPN/WireGuard) | IT Team |
| **Slack** | Terinstall dan aktif | Karyawan |
| **Zoom** | Terinstall untuk meeting | Karyawan |
| **Notion** | Terinstall untuk dokumentasi | Karyawan |
| **GitHub/GitLab** | Akses ke repository | IT Team |
| **2FA** | Two-Factor Authentication (Google Authenticator) | Karyawan |

### 4.2 Persyaratan Lingkungan
| Persyaratan | Deskripsi |
|-------------|-----------|
| **Ruang Kerja** | Ruang kerja yang tenang dan bebas gangguan |
| **Kursi & Meja** | Kursi dan meja yang ergonomis |
| **Pencahayaan** | Pencahayaan yang cukup |
| **Listrik** | Pasokan listrik yang stabil (atau UPS) |

---
## 📌 5. Prosedur Remote Work
### 5.1 Aktivasi Remote Work
1. **HR Team** mengirim **notifikasi** (Slack/Email) bahwa Remote Work diaktifkan.
2. **Karyawan** mempersiapkan **laptop, internet, dan lingkungan kerja**.
3. **IT Team** memastikan **VPN dan akses sistem** berjalan normal.

### 5.2 Selama Remote Work
- **Karyawan** harus:
  - **Online di Slack** selama jam kerja.
  - **Mengikuti meeting** (Zoom) yang dijadwalkan.
  - **Mengupdate status** di Slack (misal: "Working on AI Agent").
  - **Menggunakan VPN** untuk akses sistem internal.
- **Manager** harus:
  - **Mengadakan daily standup** (Slack/Zoom).
  - **Memantau produktivitas** (tanpa micromanage).
  - **Memberikan dukungan** jika karyawan kesulitan.

### 5.3 Deaktivasi Remote Work
1. **HR Team** mengirim **notifikasi** (Slack/Email) bahwa Remote Work dinonaktifkan.
2. **Karyawan** kembali bekerja di kantor (jika memungkinkan).

---
## 📌 6. Tools untuk Remote Work
| Tools | Kegunaan | Link |
|-------|----------|------|
| **Slack** | Komunikasi tim | [musgo-os.slack.com](https://musgo-os.slack.com) |
| **Zoom** | Meeting & Video Call | [zoom.us](https://zoom.us) |
| **Notion** | Dokumentasi & Wiki | [notion.so](https://notion.so) |
| **GitHub** | Version Control | [github.com/musgo-os](https://github.com/musgo-os) |
| **OpenVPN** | Akses VPN | [openvpn.net](https://openvpn.net) |
| **Google Drive** | Penyimpanan File | [drive.google.com](https://drive.google.com) |

---
## 📌 7. Security Remote Work
- **Gunakan VPN** untuk akses sistem internal.
- **Jangan gunakan Wi-Fi publik** (gunakan hotspot atau VPN).
- **Lock laptop** jika tidak digunakan.
- **Jangan simpan password** di browser.
- **Gunakan 2FA** untuk semua akun.

---
## 📌 8. Dukungan
- **IT Support**: `it-support@musgo-os.com` (untuk masalah teknis).
- **HR Support**: `hr@musgo-os.com` (untuk masalah kebijakan).
- **Slack Channel**: `#remote-work` (untuk diskusi).
```

---
##### **2. Prosedur Aktivasi BCP**
**Contoh Prosedur Aktivasi BCP:**
```markdown
# 📋 Prosedur Aktivasi BCP
**ID:** BCP-PROC-001
**Versi:** 1.0
**Owner:** @dhani

---
## 📌 1. Deteksi Gangguan
- **Sumber Deteksi:**
  - **Monitoring**: Prometheus + Grafana (alert jika sistem down).
  - **User Report**: User melaporkan gangguan (Slack, Email, Support Ticket).
  - **Vendor Notification**: Zapier/AWS/GCP mengirim notifikasi outage.

- **Aksi:**
  - **Incident Commander** (Dhani) **verifikasi gangguan**.
  - **Tentukan severity** (SEV-1, SEV-2, dll.).

---
## 📌 2. Deklarasi Aktivasi BCP
- **Kondisi Aktivasi BCP:**
  - **SEV-1**: Sistem **tidak berfungsi** > 15 menit.
  - **SEV-2**: Fitur **kritis terganggu** > 30 menit.
  - **Bencana Alam/Buatan**: Gangguan **skala besar** (misal: cloud outage, pandemi).

- **Aksi:**
  - **Incident Commander** mendeklarasikan **aktivasi BCP** via:
    - **Slack**: `#bcp-activation` (tag @bcp-committee).
    - **Email**: `bcp@musgo-os.com` (ke semua karyawan).
    - **Status Page**: Update [status.musgo-os.com](https://status.musgo-os.com).
  - **Buat Incident Ticket** (Jira/Linear) dengan label `bcp-activation`.

---
## 📌 3. Aktivasi Strategi BCP
| Proses Bisnis | Strategi BCP | Aksi |
|---------------|---------------|------|
| **AI Agent Execution** | Redundancy (Cluster B) | Failover ke Cluster B |
| **Zapier Integration** | Diversification (Make.com) | Beralih ke Make.com |
| **User Authentication** | Redundancy (Cluster B) | Failover ke Cluster B |
| **Billing & Subscription** | Manual Workaround | Gunakan Spreadsheet |
| **Support & Helpdesk** | Alternate Processing Site | Kerja dari Co-Working Space |
| **Dashboard** | Remote Work | Kerja dari rumah |
| **Documentation** | Remote Work | Kerja dari rumah |

---
## 📌 4. Komunikasi
### 4.1 Internal (Tim)
| Channel | Pesan | Frekuensi |
|---------|-------|-----------|
| **Slack (`#bcp-activation`)** | "BCP diaktifkan. Silakan ikuti prosedur BCP." | Sekali |
| **Email (`bcp@musgo-os.com`)** | Detail gangguan, strategi BCP, kontak | Sekali |
| **Slack (`#bcp-updates`)** | Update status pemulihan | Setiap 1 jam |
| **Zoom (Daily Standup)** | Koordinasi tim | Setiap hari |

### 4.2 Eksternal (User)
| Channel | Pesan | Frekuensi |
|---------|-------|-----------|
| **Status Page** | "MusGo-OS sedang mengalami gangguan. Kami sedang menanganinya." | Sekali |
| **Email (Broadcast)** | Detail gangguan, estimasi pemulihan | Sekali |
| **Slack (User Channel)** | Update status | Setiap 2 jam |
| **Twitter** | Update singkat | Setiap 4 jam |

---
## 📌 5. Pemantauan
- **Monitoring**: Grafana, Prometheus, Sentry.
- **Incident Ticket**: Update setiap **1 jam** (SEV-1) atau **2 jam** (SEV-2).
- **BCP Dashboard**: [Grafana BCP Dashboard](http://grafana.musgo-os.com/d/bcp).

---
## 📌 6. Deaktivasi BCP
- **Kondisi Deaktivasi BCP:**
  - Sistem **kembali berjalan normal**.
  - **RTO tercapai** (misal: < 1 jam untuk SEV-1).

- **Aksi:**
  - **Incident Commander** mendeklarasikan **deaktivasi BCP** via:
    - **Slack**: `#bcp-deactivation` (tag @bcp-committee).
    - **Email**: `bcp@musgo-os.com` (ke semua karyawan).
    - **Status Page**: Update [status.musgo-os.com](https://status.musgo-os.com).
  - **Buat Post-Mortem Ticket** (Jira/Linear).

---
## 📌 7. Post-BCP Review
- **Waktu**: Dalam **24 jam** setelah deaktivasi BCP.
- **Peserta**: @bcp-committee, @dhani, tim terkait.
- **Agenda**:
  - **Review insiden**: Apa yang terjadi?
  - **Review BCP**: Apakah BCP berjalan dengan baik?
  - **Action Items**: Apa yang perlu diperbaiki?
  - **Update BCP**: Perbaiki prosedur jika diperlukan.
```

---
##### **3. Prosedur Kelangsungan Operasional (AI Agent)**
**Contoh Prosedur untuk AI Agent:**
```markdown
# 📋 Prosedur Kelangsungan Operasional: AI Agent
**ID:** BCP-PROC-002
**Versi:** 1.0
**Owner:** @backend-team

---
## 📌 1. Deteksi Gangguan
- **Monitoring**: Grafana menunjukkan **AI Agent down** (error rate > 10%).
- **Alert**: Prometheus Alertmanager mengirim alert `AIAgentDown`.
- **User Report**: User melaporkan **AI Agent tidak merespons**.

---
## 📌 2. Aktivasi Strategi BCP
### 2.1 Failover ke Cluster B
1. **Cek status Cluster A**:
   ```bash
   kubectl get pods -n musgo-os -l app=ai-agent
   ```
2. **Jika Cluster A down**, **Kubernetes Federation** otomatis **alihkan traffic** ke Cluster B.
3. **Verifikasi Cluster B**:
   ```bash
   kubectl get pods -n musgo-os -l app=ai-agent -o wide
   ```
4. **Cek health AI Agent**:
   ```bash
   curl http://ai-agent.musgo-os.com/health
   ```

### 2.2 Scale Up Cluster B
1. **Scale up AI Agent**:
   ```bash
   kubectl scale deployment ai-agent --replicas=10 -n musgo-os
   ```
2. **Monitor resource usage**:
   ```bash
   kubectl top pods -n musgo-os
   ```

### 2.3 Fallback ke Local AI (Jika Cluster B Juga Down)
1. **Jalankan AI Agent lokal** (di laptop developer):
   ```bash
   python3 -m musgo_os.ai_agent --local-mode
   ```
2. **Gunakan untuk tugas kritis** (misal: user premium).

---
## 📌 3. Komunikasi
- **Internal**:
  - **Slack (`#ai-agent`)**:
    > "AI Agent sedang down. Kami sedang failover ke Cluster B. Estimasi pemulihan: 30 menit."
- **Eksternal**:
  - **Status Page**:
    > "AI Agent sedang mengalami gangguan. Kami sedang menanganinya. Estimasi pemulihan: 30 menit."

---
## 📌 4. Pemantauan
- **Grafana**: Monitor **AI Agent metrics** (latency, error rate).
- **Sentry**: Monitor **error** di AI Agent.
- **Log**: Cek log AI Agent (`kubectl logs -n musgo-os deployment/ai-agent`).

---
## 📌 5. Pemulihan
1. **Fix root cause** (misal: restart pod, fix bug).
2. **Failback ke Cluster A** (jika Cluster A sudah pulih):
   ```bash
   kubectl scale deployment ai-agent --replicas=0 -n musgo-os --context=cluster-b
   kubectl scale deployment ai-agent --replicas=5 -n musgo-os --context=cluster-a
   ```
3. **Verifikasi AI Agent berjalan normal**:
   ```bash
   curl http://ai-agent.musgo-os.com/health
   ```

---
## 📌 6. Deaktivasi BCP
- **Incident Commander** mendeklarasikan **deaktivasi BCP** jika:
  - AI Agent **berjalan normal** di Cluster A.
  - **Error rate < 1%**.
  - **Latency < 1 detik**.

---
## 📌 7. Post-BCP Review
- **Root Cause**: Apa penyebab AI Agent down?
- **BCP Effectiveness**: Apakah failover berjalan dengan baik?
- **Action Items**:
  - [ ] Tambahkan **auto-scaling** untuk AI Agent.
  - [ ] Setup **multi-region** untuk AI Agent.
  - [ ] Lakukan **load testing** untuk AI Agent.
```

---
##### **4. Prosedur Komunikasi BCP**
**Contoh Template Pesan Komunikasi:**
```markdown
# 📧 Template Pesan Komunikasi BCP
**Versi:** 1.0
**Owner:** @comms-team

---
## 📌 1. Internal (Tim)
### 1.1 Aktivasi BCP (Slack)
```
🚨 BCP DIAKTIFKAN 🚨

@here
MusGo-OS sedang mengalami gangguan [SEV-1/SEV-2].
BCP telah diaktifkan.

📌 **Detail Gangguan:**
- Waktu: [Waktu]
- Dampak: [Dampak]
- Penyebab: [Penyebab (jika diketahui)]

📌 **Strategi BCP:**
- [Strategi 1]
- [Strategi 2]

📌 **Aksi untuk Tim:**
- [Aksi 1]
- [Aksi 2]

📌 **Kontak:**
- Incident Commander: @dhani
- Tim Teknis: @devops-team

🔗 **Update Terbaru:** [Link ke Incident Ticket]
```

### 1.2 Update Status (Slack)
```
🔄 UPDATE BCP: [Waktu]

📌 **Status Terbaru:**
- [Update 1]
- [Update 2]

📌 **Estimasi Pemulihan:**
- [Estimasi]

📌 **Aksi Selanjutnya:**
- [Aksi 1]
- [Aksi 2]

🔗 **Incident Ticket:** [Link]
```

### 1.3 Deaktivasi BCP (Slack)
```
✅ BCP DINONAKTIFKAN ✅

@here
Gangguan di MusGo-OS telah teratasi.
BCP dinonaktifkan.

📌 **Ringkasan:**
- Waktu Gangguan: [Waktu]
- Durasi: [Durasi]
- Penyebab: [Penyebab]
- Solusi: [Solusi]

📌 **Post-Mortem:**
- Akan diadakan besok pukul [Waktu].

📌 **Kontak:**
- Incident Commander: @dhani

🔗 **Incident Ticket:** [Link]
```

---
## 📌 2. Eksternal (User)
### 2.1 Aktivasi BCP (Status Page)
```
🚨 MusGo-OS Sedang Mengalami Gangguan

Kami sedang mengalami gangguan pada [Fitur].
Tim kami sedang menanganinya.

📌 **Detail:**
- Waktu: [Waktu]
- Dampak: [Dampak]
- Estimasi Pemulihan: [Estimasi]

📌 **Update Terbaru:**
- [Update 1]
- [Update 2]

🔗 **Status Page:** [status.musgo-os.com](https://status.musgo-os.com)
```

### 2.2 Update Status (Email)
**Subject:** Update Gangguan MusGo-OS - [Fitur]

**Body:**
```
Halo [Nama User],

Kami ingin memberikan update mengenai gangguan yang sedang terjadi di MusGo-OS.

📌 **Status Terbaru:**
- [Update 1]
- [Update 2]

📌 **Estimasi Pemulihan:**
- [Estimasi]

📌 **Aksi untuk User:**
- [Aksi 1]
- [Aksi 2]

Kami mohon maaf atas ketidaknyamanan ini.
Tim MusGo-OS sedang bekerja keras untuk memulihkan layanan.

Terima kasih,
Tim MusGo-OS
```

### 2.3 Deaktivasi BCP (Email)
**Subject:** Gangguan MusGo-OS Telah Teratasi

**Body:**
```
Halo [Nama User],

Kami senang memberitahu bahwa gangguan di MusGo-OS telah teratasi.
Semua layanan kini berjalan normal.

📌 **Ringkasan Gangguan:**
- Waktu: [Waktu]
- Durasi: [Durasi]
- Penyebab: [Penyebab]
- Solusi: [Solusi]

Kami mohon maaf atas ketidaknyamanan yang ditimbulkan.
Terima kasih atas kesabaran Anda.

Terima kasih,
Tim MusGo-OS
```
```

---
---
---

## **🔹 13.7 BCP Testing & Exercising**
### **📌 Penjelasan**
**BCP Testing & Exercising** adalah **proses menguji BCP** untuk memastikan:
- **BCP berfungsi** dengan baik.
- **Tim siap** menanganinya.
- **Prosedur jelas** dan mudah diikuti.

**Jenis Testing BCP:**
| Jenis Testing | Deskripsi | Frekuensi | Peserta | Durasi |
|---------------|-----------|-----------|---------|--------|
| **Tabletop Exercise** | Diskusi **teoritis** (tanpa eksekusi) | 6 bulan | BCP Committee | 1-2 jam |
| **Walkthrough Test** | **Simulasi** langkah-langkah BCP | 3 bulan | Tim Terkait | 2-4 jam |
| **Simulation Test** | **Uji coba** failover (tanpa mematikan production) | 1 bulan | Tim Teknis | 4-8 jam |
| **Full Interruption Test** | **Matikan production** dan uji BCP | 1 tahun | Semua Tim | 1-2 hari |

---
#### **🚀 Contoh Implementasi: BCP Testing**
##### **1. Tabletop Exercise (Diskusi)**
**Contoh Skenario:**
> *"Cloud Provider (AWS) mengalami outage di Region us-east-1. Bagaimana MusGo-OS menanganinya?"*

**Langkah-Langkah:**
1. **Incident Commander** (Dhani) memimpin diskusi.
2. **Tim Database** menjelaskan **langkah failover PostgreSQL**.
3. **Tim DevOps** menjelaskan **langkah failover Kubernetes**.
4. **Tim Backend** menjelaskan **langkah failover AI Agent**.
5. **Tim Support** menjelaskan **komunikasi ke user**.
6. **Tim HR** menjelaskan **Remote Work Policy**.

**Output:**
- **Dokumentasi** langkah-langkah yang diperlukan.
- **Identifikasi celah** (misal: tidak ada dokumentasi DNS update).

**Contoh Agenda Tabletop Exercise:**
```markdown
# 📅 Agenda: Tabletop Exercise - AWS Outage
**Tanggal:** 19 Mei 2026
**Waktu:** 10:00 - 12:00 WIB
**Lokasi:** Zoom / Kantor MusGo-OS
**Fasilitator:** @dhani

---
## 📌 Agenda
| Waktu | Topik | Pemateri |
|-------|-------|----------|
| 10:00 - 10:15 | Pembukaan & Tujuan | @dhani |
| 10:15 - 10:30 | Skenario: AWS Outage | @dhani |
| 10:30 - 11:00 | Diskusi: Failover PostgreSQL | @db-team |
| 11:00 - 11:30 | Diskusi: Failover Kubernetes | @devops-team |
| 11:30 - 12:00 | Diskusi: Komunikasi & Remote Work | @comms-team, @hr-team |

---
## 📌 Tujuan
1. **Menguji pemahaman tim** tentang BCP.
2. **Mengidentifikasi celah** dalam BCP.
3. **Meningkatkan kesadaran** tentang BCP.

---
## 📌 Skenario
> *"AWS Region us-east-1 mengalami outage. MusGo-OS (yang berjalan di us-east-1) tidak bisa diakses. Bagaimana tim menanganinya?"*

---
## 📌 Pertanyaan Diskusi
1. **Deteksi:**
   - Bagaimana tim **mendeteksi** AWS outage?
   - Siapa yang **pertama mengetahui**?
2. **Aktivasi BCP:**
   - Siapa yang **mendeklarasikan aktivasi BCP**?
   - Bagaimana **komunikasi ke tim**?
3. **Failover:**
   - Bagaimana **failover PostgreSQL** ke us-west-2?
   - Bagaimana **failover Kubernetes** ke us-west-2?
   - Bagaimana **failover AI Agent**?
4. **Komunikasi:**
   - Bagaimana **komunikasi ke user**?
   - Bagaimana **komunikasi internal**?
5. **Pemulihan:**
   - Bagaimana **memulihkan sistem** ke us-east-1?
   - Bagaimana **verifikasi sistem berjalan normal**?
6. **Post-BCP:**
   - Apa **action items** setelah insiden?
   - Bagaimana **mencegah insiden serupa**?

---
## 📌 Catatan
- **Catat semua masukan** dari tim.
- **Identifikasi celah** dalam BCP.
- **Update BCP** jika diperlukan.
```

---
##### **2. Walkthrough Test (Simulasi)**
**Contoh Skenario:**
> *"Simulasikan PostgreSQL Primary down dan uji failover ke Standby."*

**Langkah-Langkah:**
1. **Backup data terlebih dahulu** (untuk safety).
2. **Matikan PostgreSQL Primary** (di Cluster A).
3. **Monitor failover otomatis** (Patroni).
4. **Cek HAProxy** (apakah traffic dialihkan?).
5. **Cek MusGo-OS** (apakah aplikasi berjalan normal?).
6. **Verifikasi data** (apakah data konsisten?).
7. **Hidupkan kembali Primary** (dan cek replikasi).

**Contoh Checklist Walkthrough Test:**
```markdown
# ✅ Checklist: Walkthrough Test - PostgreSQL Failover
**Tanggal:** 19 Mei 2026
**Pemimpin Test:** @db-team
**Peserta:** @db-team, @devops-team, @backend-team

---
## 📌 Persiapan
- [ ] Backup PostgreSQL (full + WAL).
- [ ] Backup Redis.
- [ ] Backup Etcd.
- [ ] Informasikan tim bahwa test akan dilakukan.

---
## 📌 Langkah-Langkah
### 1. Matikan PostgreSQL Primary
- [ ] Cek status Patroni (`kubectl exec patroni-primary -n musgo-os -- patronictl list`).
- [ ] Matikan Primary (`kubectl exec patroni-primary -n musgo-os -- systemctl stop patroni`).
- [ ] Catat waktu: [Waktu]

### 2. Monitor Failover
- [ ] Cek apakah Standby dipromosikan (`kubectl exec patroni-standby -n musgo-os -- patronictl list`).
- [ ] Catat waktu failover: [Waktu]
- [ ] **RTO**: [Waktu Failover - Waktu Matikan] (Target: < 1 menit)

### 3. Cek HAProxy
- [ ] Cek status HAProxy (`curl http://haproxy:7000/stats`).
- [ ] Verifikasi traffic dialihkan ke Standby.

### 4. Cek MusGo-OS
- [ ] Cek health backend (`curl http://musgo-os-backend:8000/health`).
- [ ] Cek AI Agent (`curl http://ai-agent.musgo-os.com/health`).
- [ ] Cek Zapier Integration (`curl http://musgo-os-backend:8000/api/zapier/health`).

### 5. Verifikasi Data
- [ ] Cek data di Standby (`psql -h patroni-standby -U postgres -d musgo_os -c "SELECT count(*) FROM users;"`).
- [ ] Bandingkan dengan data sebelum test.

### 6. Hidupkan Kembali Primary
- [ ] Start Primary (`kubectl exec patroni-primary -n musgo-os -- systemctl start patroni`).
- [ ] Cek apakah Primary jadi Standby (`kubectl exec patroni-primary -n musgo-os -- patronictl list`).
- [ ] Catat waktu: [Waktu]

---
## 📌 Hasil Test
| Metrik | Target | Hasil | Status |
|--------|--------|-------|--------|
| **RTO** | < 1 menit | [Hasil] | ✅ / ❌ |
| **RPO** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Data Konsistensi** | 100% | [Hasil] | ✅ / ❌ |
| **Downtime** | < 1 menit | [Hasil] | ✅ / ❌ |

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]
- [Catatan 3]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| [Action 1] | @db-team | 2026-05-26 | ⬜ To Do |
| [Action 2] | @devops-team | 2026-05-26 | ⬜ To Do |
```

---
##### **3. Simulation Test (Uji Coba Failover)**
**Contoh Skenario:**
> *"Simulasikan Kubernetes Cluster A down dan uji failover ke Cluster B."*

**Langkah-Langkah:**
1. **Backup semua data** (PostgreSQL, Redis, Etcd).
2. **Matikan Kubernetes Cluster A** (simulasikan bencana).
3. **Monitor failover otomatis** ke Cluster B.
4. **Cek semua service** (Backend, Frontend, Database, Redis).
5. **Verifikasi data** (apakah data konsisten?).
6. **Hidupkan kembali Cluster A** dan cek **replikasi balik**.

**Contoh Skrip Simulation Test:**
```bash
# File: scripts/simulation_test_k8s.sh
#!/bin/bash

# Konfigurasi
CLUSTER_A="cluster-a"
CLUSTER_B="cluster-b"
NAMESPACE="musgo-os"
BACKUP_DIR="/tmp/k8s_backup_$(date +%Y%m%d_%H%M%S)"
S3_BUCKET="musgo-os-backups"
S3_PREFIX="k8s-simulation-test"

# 1. Backup data
echo "📦 Backing up data..."
mkdir -p $BACKUP_DIR

# Backup Etcd
kubectl --context=$CLUSTER_A get all -n $NAMESPACE -o yaml > $BACKUP_DIR/cluster_a_resources.yaml
aws s3 cp $BACKUP_DIR/cluster_a_resources.yaml s3://$S3_BUCKET/$S3_PREFIX/cluster_a_resources_$(date +%Y%m%d_%H%M%S).yaml

# Backup PostgreSQL (jika diperlukan)
# ...

# Backup Redis (jika diperlukan)
# ...

# 2. Matikan Cluster A
echo "⚠️  Simulating Cluster A outage..."
# Simulasikan outage dengan mematikan node (hanya untuk testing!)
# kubectl --context=$CLUSTER_A drain <node-name> --ignore-daemonsets --delete-emptydir-data
# kubectl --context=$CLUSTER_A delete node <node-name>

# Atau: Matikan service (lebih aman)
kubectl --context=$CLUSTER_A scale deployment --replicas=0 -n $NAMESPACE --all

# 3. Monitor failover ke Cluster B
echo "🔄 Monitoring failover to Cluster B..."
START_TIME=$(date +%s)
while true; do
    # Cek apakah service berjalan di Cluster B
    RUNNING_PODS=$(kubectl --context=$CLUSTER_B get pods -n $NAMESPACE --no-headers | wc -l)
    if [ $RUNNING_PODS -gt 0 ]; then
        END_TIME=$(date +%s)
        FAILOVER_TIME=$((END_TIME - START_TIME))
        echo "✅ Failover to Cluster B completed in $FAILOVER_TIME seconds"
        break
    fi
    sleep 5
done

# 4. Cek service
echo "🔍 Checking services in Cluster B..."
kubectl --context=$CLUSTER_B get pods -n $NAMESPACE
kubectl --context=$CLUSTER_B get svc -n $NAMESPACE

# Cek health endpoint
HEALTH_STATUS=$(curl -s http://musgo-os-backend.$CLUSTER_B:8000/health | grep -o '"status":"healthy"')
if [ -z "$HEALTH_STATUS" ]; then
    echo "❌ Health check failed in Cluster B"
    exit 1
else
    echo "✅ Health check passed in Cluster B"
fi

# 5. Verifikasi data
echo "📊 Verifying data consistency..."
# Contoh: Cek data PostgreSQL
# psql -h postgres.$CLUSTER_B -U postgres -d musgo_os -c "SELECT count(*) FROM users;"

# 6. Hidupkan kembali Cluster A
echo "🔄 Restarting Cluster A..."
kubectl --context=$CLUSTER_A scale deployment --replicas=1 -n $NAMESPACE --all

# 7. Cek replikasi balik
echo "🔄 Checking replication back to Cluster A..."
sleep 60  # Tunggu replikasi
kubectl --context=$CLUSTER_A get pods -n $NAMESPACE

echo "✅ Simulation Test completed successfully!"
```

**Cara Jalankan:**
```bash
chmod +x /path/to/scripts/simulation_test_k8s.sh
/path/to/scripts/simulation_test_k8s.sh
```

---
##### **4. Full Interruption Test (Uji Penuh)**
**Contoh Skenario:**
> *"Matikan seluruh production (Cluster A) dan uji BCP di Cluster B."*

**Langkah-Langkah:**
1. **Backup semua data** (PostgreSQL, Redis, Etcd, Code, Config).
2. **Matikan seluruh production** (Cluster A).
3. **Aktifkan BCP** (failover ke Cluster B).
4. **Verifikasi semua service** berjalan di Cluster B.
5. **Simulasikan operasional** (misal: user login, AI Agent, Zapier Integration).
6. **Hidupkan kembali Cluster A** dan **failback**.
7. **Lakukan Post-Mortem**.

**Catatan:**
- **Hanya dilakukan di staging** (tidak di production).
- **Lakukan di luar jam kerja** (untuk minimalkan dampak).
- **Libatkan semua tim** (Engineering, Support, HR, dll.).

**Contoh Checklist Full Interruption Test:**
```markdown
# ✅ Checklist: Full Interruption Test
**Tanggal:** 19 Mei 2026
**Pemimpin Test:** @dhani
**Peserta:** Semua Tim

---
## 📌 Persiapan
- [ ] Backup semua data (PostgreSQL, Redis, Etcd, Code, Config).
- [ ] Informasikan user bahwa test akan dilakukan (via Status Page).
- [ ] Siapkan Cluster B (standby).
- [ ] Siapkan tim support (untuk menangani user).

---
## 📌 Langkah-Langkah
### 1. Matikan Production (Cluster A)
- [ ] Matikan Kubernetes Cluster A (`kubectl --context=cluster-a scale deployment --replicas=0 -n musgo-os --all`).
- [ ] Matikan PostgreSQL Primary.
- [ ] Matikan Redis Primary.
- [ ] Catat waktu: [Waktu]

### 2. Aktifkan BCP
- [ ] **Incident Commander** mendeklarasikan aktivasi BCP.
- [ ] Failover ke Cluster B (otomatis/manual).
- [ ] Update DNS (Route 53) ke Cluster B.
- [ ] Aktifkan Remote Work Policy.

### 3. Verifikasi Service di Cluster B
- [ ] Cek Backend (`curl http://musgo-os-backend:8000/health`).
- [ ] Cek Frontend (`curl http://musgo-os-frontend:3000/health`).
- [ ] Cek PostgreSQL (`psql -h postgres.cluster-b -U postgres -d musgo_os -c "SELECT 1;"`).
- [ ] Cek Redis (`redis-cli -h redis.cluster-b ping`).
- [ ] Cek AI Agent (`curl http://ai-agent.cluster-b:8000/health`).
- [ ] Cek Zapier Integration (`curl http://musgo-os-backend.cluster-b:8000/api/zapier/health`).

### 4. Simulasikan Operasional
- [ ] User login (manual test).
- [ ] AI Agent execution (manual test).
- [ ] Zapier Integration (manual test).
- [ ] Billing & Subscription (manual test).

### 5. Hidupkan Kembali Cluster A
- [ ] Start Kubernetes Cluster A (`kubectl --context=cluster-a scale deployment --replicas=1 -n musgo-os --all`).
- [ ] Start PostgreSQL Primary.
- [ ] Start Redis Primary.
- [ ] Catat waktu: [Waktu]

### 6. Failback ke Cluster A
- [ ] Failover kembali ke Cluster A (otomatis/manual).
- [ ] Update DNS (Route 53) ke Cluster A.
- [ ] Verifikasi data konsistensi.

---
## 📌 Hasil Test
| Metrik | Target | Hasil | Status |
|--------|--------|-------|--------|
| **RTO (Backend)** | < 1 jam | [Hasil] | ✅ / ❌ |
| **RTO (Frontend)** | < 30 menit | [Hasil] | ✅ / ❌ |
| **RTO (PostgreSQL)** | < 1 jam | [Hasil] | ✅ / ❌ |
| **RTO (Redis)** | < 5 menit | [Hasil] | ✅ / ❌ |
| **RPO (PostgreSQL)** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Downtime** | < 1 jam | [Hasil] | ✅ / ❌ |
| **Data Konsistensi** | 100% | [Hasil] | ✅ / ❌ |

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]
- [Catatan 3]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| [Action 1] | @devops-team | 2026-05-26 | ⬜ To Do |
| [Action 2] | @db-team | 2026-05-26 | ⬜ To Do |
```

---
---
---

## **🔹 13.8 BCP Maintenance & Review**
### **📌 Penjelasan**
**BCP Maintenance & Review** adalah **proses pemeliharaan dan peninjauan BCP** untuk memastikan:
- **BCP selalu up-to-date**.
- **Tim siap** menanganinya.
- **Prosedur efektif**.

**Aktivitas Maintenance & Review:**
| Aktivitas | Frekuensi | Tanggung Jawab |
|-----------|-----------|----------------|
| **Review BCP** | 6 bulan | BCP Committee |
| **Update BCP** | Jika ada perubahan bisnis | BCP Committee |
| **Testing BCP** | 3-12 bulan | BCP Committee |
| **Training Tim** | 6 bulan | HR Team |
| **Audit BCP** | 1 tahun | External Auditor |

---
#### **🚀 Contoh Implementasi: BCP Maintenance**
##### **1. Review BCP (Setiap 6 Bulan)**
**Contoh Agenda Review BCP:**
```markdown
# 📅 Agenda: Review BCP
**Tanggal:** 19 November 2026
**Waktu:** 10:00 - 12:00 WIB
**Lokasi:** Zoom / Kantor MusGo-OS
**Fasilitator:** @dhani

---
## 📌 Agenda
| Waktu | Topik | Pemateri |
|-------|-------|----------|
| 10:00 - 10:15 | Pembukaan & Tujuan | @dhani |
| 10:15 - 10:45 | Review BIA & RA | @bcp-committee |
| 10:45 - 11:15 | Review BCP Strategies | @bcp-committee |
| 11:15 - 11:45 | Review BCP Procedures | @bcp-committee |
| 11:45 - 12:00 | Action Items & Penutup | @dhani |

---
## 📌 Tujuan
1. **Review BIA & RA**: Apakah proses bisnis dan risiko masih relevan?
2. **Review BCP Strategies**: Apakah strategi BCP masih efektif?
3. **Review BCP Procedures**: Apakah prosedur BCP masih jelas?
4. **Identifikasi Perubahan**: Apakah ada perubahan bisnis yang mempengaruhi BCP?

---
## 📌 Pertanyaan Review
1. **BIA:**
   - Apakah **proses bisnis kritis** masih sama?
   - Apakah **RTO & RPO** masih relevan?
2. **RA:**
   - Apakah **risiko baru** muncul?
   - Apakah **mitigasi risiko** masih efektif?
3. **BCP Strategies:**
   - Apakah **strategi BCP** masih sesuai dengan bisnis?
   - Apakah **biaya BCP** masih terjangkau?
4. **BCP Procedures:**
   - Apakah **prosedur BCP** masih jelas?
   - Apakah **kontak darurat** masih valid?
5. **Testing:**
   - Apakah **testing BCP** berjalan dengan baik?
   - Apakah **action items** dari testing sudah diselesaikan?

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]
- [Catatan 3]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Update BIA (tambah proses baru) | @bcp-committee | 2026-12-01 | ⬜ To Do |
| Update RA (tambah risiko baru) | @bcp-committee | 2026-12-01 | ⬜ To Do |
| Review BCP Strategies | @bcp-committee | 2026-12-01 | ⬜ To Do |
```

---
##### **2. Update BCP (Jika Ada Perubahan)**
**Contoh Perubahan yang Memerlukan Update BCP:**
| Perubahan | Dampak | Aksi |
|-----------|--------|------|
| **Fitur Baru (AI Agent v2)** | Proses bisnis baru | Update BIA, RA, Procedures |
| **Perubahan Arsitektur (Multi-Cloud)** | Strategi BCP berubah | Update BCP Strategies |
| **Perubahan Tim (Karyawan Baru)** | Kontak darurat berubah | Update Kontak |
| **Perubahan Regulasi (GDPR Baru)** | Kepatuhan berubah | Update Compliance |
| **Insiden Besar (AWS Outage)** | Pelajaran baru | Update Procedures |

**Contoh Proses Update BCP:**
1. **Identifikasi Perubahan** (misal: fitur baru).
2. **Review BIA & RA** (apakah perubahan mempengaruhi dampak/risiko?).
3. **Update BCP Strategies** (apakah strategi perlu diubah?).
4. **Update BCP Procedures** (apakah prosedur perlu diupdate?).
5. **Review & Approval** (oleh BCP Committee dan Executive Team).
6. **Komunikasikan Perubahan** (ke semua tim).

---
##### **3. Training Tim (Setiap 6 Bulan)**
**Contoh Agenda Training BCP:**
```markdown
# 📅 Agenda: Training BCP
**Tanggal:** 19 Mei 2026
**Waktu:** 14:00 - 16:00 WIB
**Lokasi:** Zoom / Kantor MusGo-OS
**Fasilitator:** @dhani

---
## 📌 Agenda
| Waktu | Topik | Pemateri |
|-------|-------|----------|
| 14:00 - 14:15 | Pembukaan & Tujuan | @dhani |
| 14:15 - 14:45 | Overview BCP | @dhani |
| 14:45 - 15:15 | BIA & RA | @bcp-committee |
| 15:15 - 15:45 | BCP Strategies & Procedures | @bcp-committee |
| 15:45 - 16:00 | Q&A & Penutup | @dhani |

---
## 📌 Tujuan
1. **Meningkatkan pemahaman tim** tentang BCP.
2. **Mempersiapkan tim** untuk penanganan bencana.
3. **Mengidentifikasi celah** dalam pemahaman tim.

---
## 📌 Materi Training
### 1. Overview BCP
- Apa itu BCP?
- Mengapa BCP penting untuk MusGo-OS?
- Perbedaan BCP vs DRP.

### 2. BIA & RA
- Apa itu BIA?
- Apa itu RA?
- Bagaimana BIA & RA mempengaruhi BCP?

### 3. BCP Strategies
- Strategi apa saja yang digunakan MusGo-OS?
- Bagaimana strategi dipilih?

### 4. BCP Procedures
- Bagaimana prosedur aktivasi BCP?
- Bagaimana prosedur kelangsungan operasional?
- Bagaimana prosedur komunikasi?

---
## 📌 Evaluasi
- **Kuis**: 10 pertanyaan tentang BCP.
- **Diskusi**: Simulasi penanganan bencana.

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]
```

---
##### **4. Audit BCP (Setiap 1 Tahun)**
**Contoh Checklist Audit BCP:**
```markdown
# ✅ Checklist: Audit BCP
**Tanggal:** 19 Mei 2027
**Auditor:** External Auditor / @bcp-committee
**Peserta:** BCP Committee, Executive Team

---
## 📌 Ruang Lingkup Audit
- [ ] BCP Documentation (DR Plan, Playbooks, Runbooks).
- [ ] BIA & RA.
- [ ] BCP Strategies.
- [ ] BCP Procedures.
- [ ] BCP Testing.
- [ ] BCP Training.

---
## 📌 Checklist Audit
### 1. BCP Documentation
- [ ] Apakah BCP **terdokumentasi dengan baik**?
- [ ] Apakah BCP **mencakup semua proses bisnis kritis**?
- [ ] Apakah BCP **mencakup semua risiko**?
- [ ] Apakah BCP **mencakup semua strategi dan prosedur**?
- [ ] Apakah BCP **terupdate** (setidaknya 6 bulan terakhir)?

### 2. BIA & RA
- [ ] Apakah BIA **mencakup semua proses bisnis**?
- [ ] Apakah BIA **mengidentifikasi RTO & RPO** dengan benar?
- [ ] Apakah RA **mencakup semua risiko**?
- [ ] Apakah RA **mengidentifikasi mitigasi risiko** dengan benar?

### 3. BCP Strategies
- [ ] Apakah strategi BCP **sesuai dengan bisnis**?
- [ ] Apakah strategi BCP **efektif**?
- [ ] Apakah strategi BCP **terjangkau**?

### 4. BCP Procedures
- [ ] Apakah prosedur BCP **jelas dan mudah diikuti**?
- [ ] Apakah prosedur BCP **mencakup semua skenario**?
- [ ] Apakah prosedur BCP **terupdate**?

### 5. BCP Testing
- [ ] Apakah BCP **diuji secara berkala**?
- [ ] Apakah hasil testing **terekam dan dianalisis**?
- [ ] Apakah action items dari testing **diselesaikan**?

### 6. BCP Training
- [ ] Apakah tim **dilatih secara berkala**?
- [ ] Apakah tim **memahami BCP**?
- [ ] Apakah tim **siap menanganinya**?

---
## 📌 Hasil Audit
| Kategori | Skor (1-5) | Catatan |
|----------|------------|---------|
| BCP Documentation | [Skor] | [Catatan] |
| BIA & RA | [Skor] | [Catatan] |
| BCP Strategies | [Skor] | [Catatan] |
| BCP Procedures | [Skor] | [Catatan] |
| BCP Testing | [Skor] | [Catatan] |
| BCP Training | [Skor] | [Catatan] |

---
## 📌 Kesimpulan
- **Kekuatan BCP**: [Kekuatan 1], [Kekuatan 2]
- **Kelemahan BCP**: [Kelemahan 1], [Kelemahan 2]
- **Rekomendasi**: [Rekomendasi 1], [Rekomendasi 2]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| [Action 1] | @bcp-committee | 2027-06-19 | ⬜ To Do |
| [Action 2] | @bcp-committee | 2027-06-19 | ⬜ To Do |
```

---
---
---
# **📌 PART 13: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 13 (Business Continuity Plan)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **BCP Framework** | Governance, BIA, RA | Kerangka kerja BCP | ✅ **Dokumentasi tersedia** |
| **Business Impact Analysis** | Identifikasi proses kritis | Prioritaskan pemulihan | ✅ **Dokumentasi tersedia** |
| **Risk Assessment** | Identifikasi risiko | Mitigasi risiko | ✅ **Dokumentasi tersedia** |
| **BCP Strategies** | Redundancy, Diversification | Kelangsungan operasional | ✅ **Dokumentasi tersedia** |
| **BCP Procedures** | Aktivasi, Operasional, Komunikasi | Prosedur jelas | ✅ **Dokumentasi tersedia** |
| **BCP Testing** | Tabletop, Walkthrough, Simulation | Verifikasi BCP | ✅ **Contoh skrip tersedia** |
| **BCP Maintenance** | Review, Update, Training | BCP selalu up-to-date | ✅ **Dokumentasi tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Lengkapi BIA & RA** (identifikasi semua proses bisnis dan risiko).
- [ ] **Buat BCP Documentation** (DR Plan + BCP).
- [ ] **Setup Remote Work Policy** (untuk kerja dari rumah).
- [ ] **Setup Fallback Mechanism** (untuk Zapier Integration).
- [ ] **Lakukan Tabletop Exercise** (diskusi teoritis).

### **2. Mid-Term (1 Bulan)**
- [ ] **Implementasi BCP Strategies** (Redundancy, Diversification).
- [ ] **Buat BCP Procedures** (Aktivasi, Operasional, Komunikasi).
- [ ] **Lakukan Walkthrough Test** (simulasi langkah-langkah).
- [ ] **Lakukan Simulation Test** (uji coba failover).
- [ ] **Train Tim** (pelatihan BCP).

### **3. Long-Term (3+ Bulan)**
- [ ] **Lakukan Full Interruption Test** (uji penuh di staging).
- [ ] **Setup Multi-Cloud** (untuk redundancy).
- [ ] **Setup DRaaS** (jika budget cukup).
- [ ] **Lakukan Audit BCP** (setiap 1 tahun).
- [ ] **Review & Update BCP** (setiap 6 bulan).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 14: Crisis Communication Plan** (Untuk komunikasi krisis)
   - [ ] **Part 15: Vendor & Partner BCP** (Untuk mitra dan vendor)
   - [ ] **Part 16: Compliance & Audit** (Untuk kepatuhan regulasi)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full BCP untuk production)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full BCP Documentation untuk MusGo-OS**?
   - [ ] **Template BIA & RA**?
   - [ ] **Template BCP Procedures**?
   - [ ] **Skrip Otomatisasi BCP Testing**?

3. **Apakah ada area BCP spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **BIA**, **RA**, **BCP Strategies**, **BCP Procedures**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 14: Crisis Communication Plan (CCP)** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **komunikasi krisis** di **MusGo-OS 2in1**, termasuk **strategi, template pesan, saluran komunikasi, dan eskalasi**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN CRISIS COMMUNICATION PLAN (CCP) (PART 14)**
*Terjemahan + Implementasi untuk Komunikasi Krisis Production-Ready*

---

---

## **🔹 14.1 Overview Crisis Communication Plan (CCP)**
### **📌 Penjelasan (Bahasa Indonesia)**
**Crisis Communication Plan (CCP)** adalah **rencana terstruktur** untuk **berkomunikasi dengan stakeholder** (user, tim, mitra, media) **selama krisis**, seperti:
- **Outage** (sistem down).
- **Data Breach** (kebocoran data).
- **Cyber Attack** (serangan siber).
- **Bencana Alam** (banjir, gempa).
- **Kesalahan Manusia** (human error).

**Tujuan CCP untuk MusGo-OS:**
✅ **Transparansi**: Berikan **informasi akurat** kepada stakeholder.
✅ **Kepercayaan**: Pertahankan **kepercayaan user** meskipun terjadi krisis.
✅ **Kontrol Narasi**: Hindari **misinformasi** atau **spekulasi**.
✅ **Koordinasi**: Pastikan **semua tim terkoordinasi**.
✅ **Kepatuhan**: Patuhi **regulasi** (GDPR, SOC 2).

**Prinsip Komunikasi Krisis:**
1. **Cepat (Fast)**: Beri **update secepat mungkin** (bahkan jika informasi belum lengkap).
2. **Jujur (Honest)**: **Akui krisis** dan **jangan menyembunyikan fakta**.
3. **Konsisten (Consistent)**: **Pesan seragam** di semua saluran.
4. **Empati (Empathetic)**: Tunjukkan **kepedulian** terhadap dampak krisis.
5. **Tindak Lanjut (Actionable)**: Beri **langkah selanjutnya** yang jelas.

---
### **🚀 Contoh Arsitektur CCP untuk MusGo-OS**
```
Krisis Terjadi (Misal: Outage)
│
├── **Deteksi** (Monitoring: Prometheus, Sentry, Loki)
│
├── **Aktivasi CCP** (Incident Commander: Dhani)
│   │
│   ├── **Internal Communication** (Slack, Email, Zoom)
│   │   ├── **Tim Teknis** (Engineering, DevOps, DB)
│   │   ├── **Tim Bisnis** (Product, Marketing, Sales)
│   │   └── **Tim Support** (Customer Support)
│   │
│   └── **External Communication** (Status Page, Email, Social Media)
│       ├── **User** (Status Page, Email, Slack)
│       ├── **Media** (Press Release, Twitter)
│       └── **Regulator** (Laporan GDPR, dll.)
│
└── **Post-Crisis** (Post-Mortem, Review CCP)
```

---
---
---

## **🔹 14.2 CCP Framework (Kerangka Kerja CCP)**
### **📌 Penjelasan**
**CCP Framework** adalah **kerangka kerja** untuk **membangun, mengimplementasikan, dan mengelola CCP**. Framework meliputi:
1. **CCP Governance** (Kebijakan, peran, tanggung jawab).
2. **Stakeholder Analysis** (Identifikasi stakeholder).
3. **Communication Channels** (Saluran komunikasi).
4. **Message Templates** (Template pesan).
5. **Escalation Path** (Rute eskalasi).
6. **Testing & Training** (Uji coba dan pelatihan).

---
#### **🚀 Contoh Implementasi: CCP Framework**
##### **1. CCP Governance (Tata Kelola CCP)**
**Dokumen Kebijakan CCP:**
```markdown
# 📜 MusGo-OS 2in1: Kebijakan Crisis Communication (CCP)
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan (CTO)

---
## 📌 1. Tujuan
Kebijakan ini mendefinisikan **tata kelola Crisis Communication Plan (CCP)** untuk **MusGo-OS 2in1**, termasuk:
- Peran dan tanggung jawab.
- Saluran komunikasi.
- Prosedur komunikasi krisis.
- Kepatuhan terhadap regulasi.

---
## 📌 2. Ruang Lingkup
Kebijakan ini berlaku untuk:
- **Semua karyawan MusGo-OS**.
- **Semua stakeholder** (user, mitra, vendor, media, regulator).
- **Semua jenis krisis** (outage, data breach, cyber attack, dll.).

---
## 📌 3. Peran dan Tanggung Jawab
| Peran | Tanggung Jawab | Kontak |
|-------|----------------|--------|
| **Incident Commander** | Memimpin penanganan krisis, menentukan pesan utama | @dhani |
| **Communication Lead** | Bertanggung jawab atas komunikasi eksternal | @comms-team |
| **Technical Lead** | Memberikan informasi teknis untuk pesan | @devops-team |
| **Support Lead** | Menangani pertanyaan user | @support-team |
| **Legal & Compliance** | Memastikan pesan mematuhi regulasi | @legal-team |
| **Executive Sponsor** | Eskalasi ke manajemen (jika diperlukan) | @ceo |

---
## 📌 4. Proses CCP
### 4.1 Deteksi Krisis
- **Sumber Deteksi:**
  - **Monitoring**: Prometheus + Grafana (alert jika sistem down).
  - **User Report**: User melaporkan krisis (Slack, Email, Support Ticket).
  - **Vendor Notification**: Zapier/AWS/GCP mengirim notifikasi outage.

- **Aksi:**
  - **Incident Commander** verifikasi krisis.
  - **Tentukan severity** (SEV-1, SEV-2, dll.).
  - **Aktifkan CCP** jika krisis **berdampak signifikan**.

### 4.2 Aktivasi CCP
- **Kondisi Aktivasi CCP:**
  - **SEV-1**: Sistem **tidak berfungsi** > 15 menit.
  - **SEV-2**: Fitur **kritis terganggu** > 30 menit.
  - **Data Breach**: Kebocoran data user.
  - **Cyber Attack**: Serangan siber (DDoS, ransomware).

- **Aksi:**
  - **Incident Commander** mendeklarasikan **aktivasi CCP**.
  - **Buat Incident Ticket** (Jira/Linear) dengan label `crisis-communication`.
  - **Aktifkan War Room** (Slack Channel `#crisis-war-room`).

### 4.3 Komunikasi Internal
- **Saluran**: Slack (`#crisis-war-room`), Email (`crisis@musgo-os.com`).
- **Frekuensi**: Setiap **15 menit (SEV-1)**, **30 menit (SEV-2)**, **1 jam (SEV-3)**.
- **Peserta**: Semua tim terkait.

### 4.4 Komunikasi Eksternal
- **Saluran**: Status Page, Email, Slack (User Channel), Twitter, Press Release.
- **Frekuensi**: Setiap **30 menit (SEV-1)**, **1 jam (SEV-2)**, **4 jam (SEV-3)**.
- **Peserta**: User, Media, Regulator.

### 4.5 Deaktivasi CCP
- **Kondisi Deaktivasi CCP:**
  - Krisis **teratasi**.
  - Sistem **kembali berjalan normal**.
  - **RTO tercapai** (misal: < 1 jam untuk SEV-1).

- **Aksi:**
  - **Incident Commander** mendeklarasikan **deaktivasi CCP**.
  - **Komunikasikan ke stakeholder** (Status Page, Email).
  - **Buat Post-Mortem Ticket** (Jira/Linear).

---
## 📌 5. Kepatuhan
- **GDPR**: Laporan data breach **dalam 72 jam**.
- **SOC 2**: Dokumentasi komunikasi krisis.
- **ISO 22301**: Standar komunikasi krisis.

---
## 📌 6. Referensi
- [GDPR Data Breach Notification](https://gdpr-info.eu/art-33-gdpr/)
- [SOC 2 Trust Services Criteria](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustservicesprinciples.html)
- [ISO 22301:2019 (Crisis Communication)](https://www.iso.org/standard/75106.html)
```

---
---
---

## **🔹 14.3 Stakeholder Analysis (Analisis Stakeholder)**
### **📌 Penjelasan**
**Stakeholder Analysis** adalah **proses mengidentifikasi dan mengklasifikasikan** semua **pihak yang terpengaruh** oleh krisis, serta **kebutuhan komunikasi** mereka.

**Manfaat untuk MusGo-OS:**
- **Prioritaskan komunikasi** (siapa yang perlu diinformasikan terlebih dahulu).
- **Sesuaikan pesan** (pesan untuk user ≠ pesan untuk media).
- **Alokasi resource** (siapa yang memerlukan dukungan lebih).

---
#### **🚀 Contoh Implementasi: Stakeholder Analysis**
##### **1. Daftar Stakeholder MusGo-OS**
| ID | Stakeholder | Kategori | Dampak Krisis | Kebutuhan Komunikasi | Prioritas | Saluran Komunikasi |
|----|-------------|----------|---------------|----------------------|-----------|-------------------|
| **S-001** | User (Gratis) | Eksternal | Tidak bisa menggunakan MusGo-OS | Informasi status, estimasi pemulihan | Medium | Status Page, Email |
| **S-002** | User (Premium) | Eksternal | Tidak bisa menggunakan MusGo-OS | Informasi status, estimasi pemulihan, kompensasi | High | Status Page, Email, Slack |
| **S-003** | User (Enterprise) | Eksternal | Tidak bisa menggunakan MusGo-OS | Informasi status, estimasi pemulihan, kompensasi, SLA | Critical | Status Page, Email, Slack, Phone Call |
| **S-004** | Tim Engineering | Internal | Gangguan operasional | Informasi teknis, langkah mitigasi | Critical | Slack (`#crisis-war-room`), Zoom |
| **S-005** | Tim Support | Internal | Banyak pertanyaan user | Informasi status, FAQ, template balasan | High | Slack (`#crisis-war-room`), Notion |
| **S-006** | Tim Product | Internal | Gangguan fitur | Informasi dampak bisnis, prioritas pemulihan | High | Slack (`#crisis-war-room`), Zoom |
| **S-007** | Tim Marketing | Internal | Dampak reputasi | Informasi untuk social media, press release | Medium | Slack (`#crisis-war-room`), Email |
| **S-008** | Tim Sales | Internal | Dampak penjualan | Informasi untuk customer, FAQ | Medium | Slack (`#crisis-war-room`), Email |
| **S-009** | Tim HR | Internal | Dampak karyawan | Informasi untuk karyawan, remote work policy | Medium | Slack (`#crisis-war-room`), Email |
| **S-010** | Tim Legal & Compliance | Internal | Dampak hukum | Informasi untuk laporan regulator | High | Slack (`#crisis-war-room`), Email |
| **S-011** | Investor | Eksternal | Dampak keuangan | Informasi status, dampak bisnis | High | Email, Phone Call |
| **S-012** | Mitra (Zapier, AWS, GCP) | Eksternal | Gangguan integrasi | Informasi status, koordinasi | High | Email, Slack |
| **S-013** | Media | Eksternal | Dampak reputasi | Press release, interview | Medium | Email, Press Release |
| **S-014** | Regulator (Kominfo, GDPR) | Eksternal | Dampak hukum | Laporan resmi | High | Email, Official Letter |
| **S-015** | Komunitas (Developer, User Group) | Eksternal | Dampak adopsi | Informasi status, FAQ | Low | Twitter, Forum |

---
##### **2. Stakeholder Mapping (Peta Stakeholder)**
**Contoh Peta Stakeholder (Power vs Interest):**

```
High Interest
│
├───────────────┬───────────────┐
│               │               │
│   User (Premium)   Enterprise   │
│   Tim Engineering  User         │
│               │               │
│   Tim Support    Tim Legal     │
│               │               │
└───────────────┴───────────────┘
     Low Power       High Power

Low Interest
│
├───────────────┬───────────────┐
│               │               │
│   User (Gratis)   Komunitas    │
│   Tim Marketing   Developer    │
│               │               │
└───────────────┴───────────────┘
     Low Power       High Power
```

**Keterangan:**
- **High Power + High Interest (Critical)**: **User (Enterprise), Tim Engineering, Tim Legal**.
- **High Power + Low Interest (Keep Satisfied)**: **Investor, Regulator**.
- **Low Power + High Interest (Keep Informed)**: **User (Premium), Tim Support**.
- **Low Power + Low Interest (Monitor)**: **User (Gratis), Komunitas**.

---
##### **3. Communication Matrix (Matriks Komunikasi)**
**Contoh Matriks Komunikasi:**

| Stakeholder | SEV-1 | SEV-2 | SEV-3 | Saluran | Frekuensi | Tanggung Jawab |
|-------------|-------|-------|-------|---------|-----------|-----------------|
| **User (Enterprise)** | ✅ | ✅ | ✅ | Status Page, Email, Slack, Phone | 15 menit | @comms-team |
| **User (Premium)** | ✅ | ✅ | ✅ | Status Page, Email, Slack | 30 menit | @comms-team |
| **User (Gratis)** | ✅ | ✅ | ❌ | Status Page, Email | 1 jam | @comms-team |
| **Tim Engineering** | ✅ | ✅ | ✅ | Slack (`#crisis-war-room`), Zoom | 15 menit | @devops-team |
| **Tim Support** | ✅ | ✅ | ✅ | Slack (`#crisis-war-room`), Notion | 30 menit | @support-team |
| **Tim Product** | ✅ | ✅ | ❌ | Slack (`#crisis-war-room`), Zoom | 30 menit | @product-team |
| **Tim Marketing** | ✅ | ❌ | ❌ | Slack (`#crisis-war-room`), Email | 1 jam | @marketing-team |
| **Tim Sales** | ✅ | ❌ | ❌ | Slack (`#crisis-war-room`), Email | 1 jam | @sales-team |
| **Tim HR** | ✅ | ❌ | ❌ | Slack (`#crisis-war-room`), Email | 1 jam | @hr-team |
| **Tim Legal** | ✅ | ✅ | ❌ | Slack (`#crisis-war-room`), Email | 30 menit | @legal-team |
| **Investor** | ✅ | ✅ | ❌ | Email, Phone Call | 1 jam | @ceo |
| **Mitra (Zapier, AWS)** | ✅ | ✅ | ❌ | Email, Slack | 30 menit | @devops-team |
| **Media** | ✅ | ❌ | ❌ | Email, Press Release | 1 jam | @comms-team |
| **Regulator** | ✅ | ✅ | ❌ | Email, Official Letter | 1 jam | @legal-team |
| **Komunitas** | ❌ | ❌ | ✅ | Twitter, Forum | 4 jam | @marketing-team |

---
---
---

## **🔹 14.4 Communication Channels (Saluran Komunikasi)**
### **📌 Penjelasan**
**Communication Channels** adalah **saluran yang digunakan** untuk **berkomunikasi dengan stakeholder** selama krisis. Setiap saluran memiliki **kelebihan dan kekurangan**.

**Saluran Komunikasi untuk MusGo-OS:**
| Saluran | Deskripsi | Kelebihan | Kekurangan | Rekomendasi |
|---------|-----------|-----------|------------|--------------|
| **Status Page** | Halaman status (misal: status.musgo-os.com) | ✅ Real-time, transparan, otomatis | ❌ Tidak interaktif | ✅ **Wajib** |
| **Email** | Surel ke user/stakeholder | ✅ Formal, tercatat | ❌ Lambat, spam | ✅ **Wajib** |
| **Slack** | Chat internal/eksternal | ✅ Cepat, interaktif | ❌ Tidak semua user punya Slack | ✅ **Untuk internal & premium user** |
| **Twitter** | Social media | ✅ Cepat, publik | ❌ Tidak formal, terbatas karakter | ✅ **Untuk update singkat** |
| **Press Release** | Siaran pers | ✅ Formal, untuk media | ❌ Lambat, mahal | ⚠️ **Jika diperlukan media** |
| **Phone Call** | Telepon | ✅ Personal, cepat | ❌ Mahal, tidak scalable | ⚠️ **Untuk enterprise user** |
| **Zoom** | Video conference | ✅ Interaktif, untuk koordinasi tim | ❌ Tidak untuk user | ✅ **Untuk internal** |
| **Notion** | Dokumentasi internal | ✅ Terorganisir, tercatat | ❌ Tidak untuk user | ✅ **Untuk internal** |
| **FAQ Page** | Halaman FAQ | ✅ Self-service, mengurangi beban support | ❌ Tidak real-time | ✅ **Untuk user** |
| **Blog Post** | Artikel blog | ✅ Detail, untuk publik | ❌ Lambat | ⚠️ **Untuk post-mortem** |

---
#### **🚀 Contoh Implementasi: Communication Channels**
##### **1. Status Page (Halaman Status)**
**Tools:**
- **Statuspage.io** (Atlassian).
- **Upptime** (Gratis, open-source).
- **Better Uptime** (Alternatif).

**Contoh Setup Status Page (Statuspage.io):**
1. **Daftar** di [statuspage.io](https://www.statuspage.io/).
2. **Buat Page** untuk MusGo-OS.
3. **Tambahkan Components** (Backend, Frontend, Database, Zapier Integration).
4. **Tambahkan Metrics** (Uptime, Latency, Error Rate).
5. **Integrasi dengan Monitoring** (Prometheus, Grafana).
6. **Setup Notifications** (Email, Slack, Webhook).

**Contoh Components:**
| Component | Deskripsi | Status |
|-----------|-----------|--------|
| **Backend** | API MusGo-OS | ✅ Operational |
| **Frontend** | Dashboard MusGo-OS | ✅ Operational |
| **PostgreSQL** | Database | ✅ Operational |
| **Redis** | Caching | ✅ Operational |
| **Zapier Integration** | Integrasi Zapier | ⚠️ Degraded Performance |
| **AI Agent** | AI Agent Execution | ✅ Operational |

**Contoh Incident di Status Page:**
```
🚨 [SEV-1] Backend Outage
---
**Status:** Investigating
**Start Time:** 19 Mei 2026, 10:00 WIB
**Last Update:** 19 Mei 2026, 10:15 WIB
**Affected Components:** Backend, AI Agent, Zapier Integration
**Description:** Backend MusGo-OS sedang down. Tim kami sedang menyelidiki penyebabnya.
**Next Update:** 19 Mei 2026, 10:30 WIB
```

---
##### **2. Email (Surel)**
**Tools:**
- **SendGrid** (Untuk mass email).
- **Mailchimp** (Untuk newsletter).
- **AWS SES** (Untuk email transaksional).

**Contoh Template Email (SEV-1):**
**Subject:** 🚨 [URGENT] MusGo-OS Sedang Mengalami Gangguan

**Body:**
```
Halo [Nama User],

Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan serius (SEV-1)**.
Tim kami sedang bekerja keras untuk memulihkan layanan.

📌 **Detail Gangguan:**
- **Waktu Mulai:** 19 Mei 2026, 10:00 WIB
- **Fitur Terpengaruh:** Backend, AI Agent, Zapier Integration
- **Dampak:** User tidak bisa menjalankan AI Agent atau membuat Zap.

📌 **Apa yang Kami Lakukan:**
- Tim engineering sedang menyelidiki penyebab gangguan.
- Kami akan memberikan update setiap **30 menit** atau jika ada perkembangan.

📌 **Estimasi Pemulihan:**
- **Target:** < 1 jam (11:00 WIB)

📌 **Apa yang Bisa Anda Lakukan:**
- Cek **Status Page** untuk update terbaru: [status.musgo-os.com](https://status.musgo-os.com)
- Jika Anda memerlukan bantuan mendesak, hubungi **support@musgo-os.com**.

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

**Contoh Template Email (SEV-2):**
**Subject:** ⚠️ MusGo-OS Sedang Mengalami Gangguan

**Body:**
```
Halo [Nama User],

Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan (SEV-2)**.
Tim kami sedang menanganinya.

📌 **Detail Gangguan:**
- **Waktu Mulai:** 19 Mei 2026, 10:00 WIB
- **Fitur Terpengaruh:** Zapier Integration
- **Dampak:** Otomatisasi Zap sementara terhenti.

📌 **Apa yang Kami Lakukan:**
- Tim engineering sedang berkoordinasi dengan Zapier.
- Kami akan memberikan update setiap **1 jam** atau jika ada perkembangan.

📌 **Estimasi Pemulihan:**
- **Target:** < 4 jam (14:00 WIB)

📌 **Apa yang Bisa Anda Lakukan:**
- Cek **Status Page** untuk update terbaru: [status.musgo-os.com](https://status.musgo-os.com)
- Gunakan **fallback mechanism** (jika tersedia).

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

---
##### **3. Slack (Chat Internal & Eksternal)**
**Tools:**
- **Slack** (Untuk internal dan user premium).
- **Discord** (Alternatif untuk komunitas).

**Contoh Channel Slack:**
| Channel | Deskripsi | Peserta |
|---------|-----------|---------|
| `#crisis-war-room` | Koordinasi tim selama krisis | @devops-team, @comms-team, @support-team |
| `#incident-updates` | Update status krisis (internal) | Semua karyawan |
| `#user-support` | Dukungan user selama krisis | @support-team, User Premium |
| `#status-updates` | Update status untuk user (eksternal) | User Premium |

**Contoh Pesan di `#crisis-war-room`:**
```
🚨 [SEV-1] Backend Outage - War Room Activated 🚨

@here
Backend MusGo-OS sedang down sejak 10:00 WIB.
Incident Commander: @dhani

📌 **Status Terbaru:**
- PostgreSQL: ❌ Down (Primary)
- Redis: ✅ Operational
- Kubernetes: ⚠️ Degraded (Cluster A down)

📌 **Aksi:**
- @db-team: Investigasi PostgreSQL
- @devops-team: Failover ke Cluster B
- @comms-team: Update Status Page & Email

📌 **Next Steps:**
- Failover PostgreSQL (ETR: 10:30 WIB)
- Failover Kubernetes (ETR: 10:45 WIB)

🔗 **Incident Ticket:** [JIRA-1234](https://musgo-os.atlassian.net/browse/JIRA-1234)
```

**Contoh Pesan di `#status-updates` (Untuk User):**
```
🔴 [SEV-1] MusGo-OS Backend Sedang Down

@channel
Kami sedang mengalami gangguan pada **Backend MusGo-OS**.
Tim kami sedang menanganinya.

📌 **Detail:**
- **Waktu Mulai:** 10:00 WIB
- **Dampak:** User tidak bisa menjalankan AI Agent
- **Estimasi Pemulihan:** < 1 jam

📌 **Update Terbaru:**
- PostgreSQL sedang difailover ke Cluster B (ETR: 10:30 WIB)

🔗 **Status Page:** [status.musgo-os.com](https://status.musgo-os.com)
```

---
##### **4. Twitter (Social Media)**
**Contoh Tweet (SEV-1):**
```
🚨 [URGENT] MusGo-OS sedang mengalami gangguan serius (SEV-1).
Backend dan AI Agent sementara tidak berfungsi.

Tim kami sedang menanganinya.
Update selanjutnya: 11:00 WIB.

Cek status terbaru: https://status.musgo-os.com
```

**Contoh Tweet (SEV-2):**
```
⚠️ MusGo-OS sedang mengalami gangguan (SEV-2).
Zapier Integration sementara terhenti.

Estimasi pemulihan: < 4 jam.
Cek status: https://status.musgo-os.com
```

**Contoh Tweet (Pemulihan):**
```
✅ Gangguan MusGo-OS telah teratasi!
Semua layanan kini berjalan normal.

Terima kasih atas kesabaran Anda.
```

---
##### **5. Press Release (Siaran Pers)**
**Contoh Press Release (Data Breach):**
```markdown
# 📰 SIARAN PERS: Insiden Keamanan Data MusGo-OS
**Tanggal:** 19 Mei 2026
**Kontak Media:** comms@musgo-os.com

---
## 📌 Ringkasan
MusGo-OS mengetahui **insiden keamanan data** yang mempengaruhi **sejumlah kecil user**. Kami telah **menangani insiden ini** dan **memulihkan sistem**. Tidak ada bukti bahwa data user **disalahgunakan**.

---
## 📌 Detail Insiden
- **Waktu Terjadi:** 18 Mei 2026, 22:00 WIB
- **Waktu Teratasi:** 19 Mei 2026, 02:00 WIB
- **Jenis Insiden:** **Unauthorized Access** (Akses tidak sah)
- **Data Terpengaruh:** **Email dan nama user** (tidak termasuk password)
- **Jumlah User Terpengaruh:** **< 1%** (kurang dari 100 user)

---
## 📌 Aksi yang Diambil
1. **Mengisolasi sistem** yang terpengaruh.
2. **Menghapus akses tidak sah**.
3. **Memperkuat keamanan** (2FA, encryption, dll.).
4. **Mengaudit sistem** untuk mencari celah keamanan.
5. **Melaporkan ke otoritas** (Kominfo, GDPR).

---
## 📌 Aksi untuk User
- **User terpengaruh** akan **dihubungi secara pribadi** via email.
- **Semua user** disarankan untuk:
  - **Mengganti password** (jika menggunakan password yang sama di tempat lain).
  - **Mengaktifkan 2FA** (jika belum).
  - **Memantau akun** untuk aktivitas mencurigakan.

---
## 📌 Pernyataan
> "Kami sangat menyesal atas insiden ini. Keamanan user adalah **prioritas utama** kami. Kami telah mengambil **langkah-langkah untuk mencegah insiden serupa** di masa depan."
> — Dhani Yuliawan, CTO MusGo-OS

---
## 📌 Tentang MusGo-OS
MusGo-OS adalah **AI-native operating system** yang memungkinkan user untuk **membangun otomatisasi cerdas** dengan mudah. Kami berkomitmen untuk **keamanan, privasi, dan transparansi**.

---
## 📌 Kontak Media
Untuk pertanyaan media, silakan hubungi:
**Email:** comms@musgo-os.com
**Telepon:** +62 813-6552-283
```

---
##### **6. Phone Call (Telepon)**
**Contoh Script Phone Call (Untuk Enterprise User):**
```
Halo, saya [Nama] dari Tim MusGo-OS.
Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan (SEV-1)**.

📌 **Detail:**
- Waktu: 19 Mei 2026, 10:00 WIB
- Dampak: Backend dan AI Agent tidak berfungsi
- Estimasi Pemulihan: < 1 jam

📌 **Aksi untuk Anda:**
- Cek **Status Page** untuk update terbaru: [status.musgo-os.com](https://status.musgo-os.com)
- Jika Anda memerlukan bantuan mendesak, hubungi **support@musgo-os.com**

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih.
```

---
##### **7. Zoom (Video Conference)**
**Contoh Agenda Zoom (Untuk Tim Internal):**
```markdown
# 📅 Agenda: Crisis War Room Meeting
**Tanggal:** 19 Mei 2026
**Waktu:** 10:15 - 11:00 WIB
**Link Zoom:** [Zoom Link](https://zoom.us/j/123456789)
**Fasilitator:** @dhani

---
## 📌 Agenda
| Waktu | Topik | Pemateri |
|-------|-------|----------|
| 10:15 - 10:20 | Pembukaan & Status Terbaru | @dhani |
| 10:20 - 10:30 | Investigasi PostgreSQL | @db-team |
| 10:30 - 10:40 | Failover Kubernetes | @devops-team |
| 10:40 - 10:50 | Komunikasi Eksternal | @comms-team |
| 10:50 - 11:00 | Q&A & Action Items | @dhani |

---
## 📌 Tujuan
1. **Koordinasi tim** selama krisis.
2. **Update status** investigasi dan pemulihan.
3. **Tentukan action items** selanjutnya.

---
## 📌 Peserta
- @dhani (Incident Commander)
- @db-team (Database)
- @devops-team (Infrastructure)
- @backend-team (Backend)
- @comms-team (Komunikasi)
- @support-team (Support)
```

---
---
---

## **🔹 14.5 Message Templates (Template Pesan)**
### **📌 Penjelasan**
**Message Templates** adalah **template pesan siap pakai** untuk **berbagai jenis krisis dan severity**. Template memastikan:
- **Konsistensi pesan** di semua saluran.
- **Cepat** (tidak perlu membuat pesan dari nol).
- **Akurat** (tidak ada informasi yang terlewat).

---
#### **🚀 Contoh Implementasi: Message Templates**
##### **1. Template untuk SEV-1 (Critical)**
**Contoh Template (Status Page):**
```markdown
🚨 [SEV-1] [Komponen] Outage

---
**Status:** Investigating / Identified / Monitoring / Resolved
**Start Time:** [Waktu]
**Last Update:** [Waktu]
**Affected Components:** [Daftar Komponen]
**Description:** [Deskripsi Gangguan]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

📌 **Next Update:**
- [Waktu]
```

**Contoh Template (Email):**
```markdown
Subject: 🚨 [URGENT] MusGo-OS Sedang Mengalami Gangguan [SEV-1]

---
Halo [Nama User],

Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan serius (SEV-1)**.
Tim kami sedang bekerja keras untuk memulihkan layanan.

📌 **Detail Gangguan:**
- **Waktu Mulai:** [Waktu]
- **Fitur Terpengaruh:** [Daftar Fitur]
- **Dampak:** [Dampak]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

📌 **Apa yang Bisa Anda Lakukan:**
- Cek **Status Page** untuk update terbaru: [Link Status Page]
- Jika Anda memerlukan bantuan mendesak, hubungi **support@musgo-os.com**.

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

**Contoh Template (Slack):**
```markdown
🚨 [SEV-1] [Komponen] Outage

@channel
Kami sedang mengalami gangguan **serius (SEV-1)** pada [Komponen].

📌 **Detail:**
- **Waktu Mulai:** [Waktu]
- **Dampak:** [Dampak]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

🔗 **Status Page:** [Link Status Page]
```

**Contoh Template (Twitter):**
```markdown
🚨 [URGENT] MusGo-OS sedang mengalami gangguan serius (SEV-1).
[Komponen] sementara tidak berfungsi.

Tim kami sedang menanganinya.
Update selanjutnya: [Waktu].

Cek status: [Link Status Page]
```

---
##### **2. Template untuk SEV-2 (High)**
**Contoh Template (Status Page):**
```markdown
⚠️ [SEV-2] [Komponen] Degraded Performance

---
**Status:** Investigating / Identified / Monitoring / Resolved
**Start Time:** [Waktu]
**Last Update:** [Waktu]
**Affected Components:** [Daftar Komponen]
**Description:** [Deskripsi Gangguan]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

📌 **Next Update:**
- [Waktu]
```

**Contoh Template (Email):**
```markdown
Subject: ⚠️ MusGo-OS Sedang Mengalami Gangguan [SEV-2]

---
Halo [Nama User],

Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan (SEV-2)**.
Tim kami sedang menanganinya.

📌 **Detail Gangguan:**
- **Waktu Mulai:** [Waktu]
- **Fitur Terpengaruh:** [Daftar Fitur]
- **Dampak:** [Dampak]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

📌 **Apa yang Bisa Anda Lakukan:**
- Cek **Status Page** untuk update terbaru: [Link Status Page]

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

---
##### **3. Template untuk SEV-3 (Medium)**
**Contoh Template (Status Page):**
```markdown
🟡 [SEV-3] [Komponen] Minor Issue

---
**Status:** Investigating / Identified / Monitoring / Resolved
**Start Time:** [Waktu]
**Last Update:** [Waktu]
**Affected Components:** [Daftar Komponen]
**Description:** [Deskripsi Gangguan]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

📌 **Next Update:**
- [Waktu]
```

**Contoh Template (Email):**
```markdown
Subject: 🟡 MusGo-OS Sedang Mengalami Gangguan Minor [SEV-3]

---
Halo [Nama User],

Kami ingin memberitahu bahwa **MusGo-OS sedang mengalami gangguan minor (SEV-3)**.
Tim kami sedang menanganinya.

📌 **Detail Gangguan:**
- **Waktu Mulai:** [Waktu]
- **Fitur Terpengaruh:** [Daftar Fitur]
- **Dampak:** [Dampak]

📌 **Estimasi Pemulihan:**
- **Target:** [Waktu]

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

---
##### **4. Template untuk Data Breach**
**Contoh Template (Email untuk User Terpengaruh):**
```markdown
Subject: 🔒 Penting: Insiden Keamanan Data MusGo-OS

---
Halo [Nama User],

Kami mengetahui bahwa **akun Anda terpengaruh** oleh insiden keamanan data yang terjadi pada **18 Mei 2026**.
Kami telah **menangani insiden ini** dan **memulihkan sistem**.

📌 **Detail Insiden:**
- **Waktu Terjadi:** 18 Mei 2026, 22:00 WIB
- **Waktu Teratasi:** 19 Mei 2026, 02:00 WIB
- **Data Terpengaruh:** **Email dan nama Anda** (tidak termasuk password)
- **Penyebab:** Unauthorized access (akses tidak sah)

📌 **Aksi yang Kami Ambil:**
1. Mengisolasi sistem yang terpengaruh.
2. Menghapus akses tidak sah.
3. Memperkuat keamanan (2FA, encryption, dll.).
4. Mengaudit sistem untuk mencari celah keamanan.

📌 **Aksi untuk Anda:**
- **Ganti password** Anda (jika menggunakan password yang sama di tempat lain).
- **Aktifkan 2FA** (jika belum).
- **Monitor akun** Anda untuk aktivitas mencurigakan.

📌 **Dukungan:**
Jika Anda memiliki pertanyaan, silakan hubungi **support@musgo-os.com**.

Kami sangat menyesal atas insiden ini.
Terima kasih atas kepercayaan Anda.

Salam,
Tim MusGo-OS
```

**Contoh Template (Press Release):**
*(Lihat [Bagian 14.4.5](#4-press-release-siaran-pers))*

---
##### **5. Template untuk Pemulihan (Resolved)**
**Contoh Template (Status Page):**
```markdown
✅ [SEV-1] [Komponen] Outage - Resolved

---
**Status:** Resolved
**Start Time:** [Waktu Mulai]
**End Time:** [Waktu Selesai]
**Duration:** [Durasi]
**Affected Components:** [Daftar Komponen]
**Description:** [Deskripsi Gangguan]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Root Cause:**
- [Penyebab]

📌 **Next Steps:**
- [Langkah Selanjutnya]

🔗 **Post-Mortem:** [Link Post-Mortem]
```

**Contoh Template (Email):**
```markdown
Subject: ✅ Gangguan MusGo-OS Telah Teratasi

---
Halo [Nama User],

Kami senang memberitahu bahwa **gangguan di MusGo-OS telah teratasi**.
Semua layanan kini berjalan normal.

📌 **Ringkasan Gangguan:**
- **Waktu Mulai:** [Waktu]
- **Waktu Selesai:** [Waktu]
- **Durasi:** [Durasi]
- **Fitur Terpengaruh:** [Daftar Fitur]
- **Penyebab:** [Penyebab]

📌 **Apa yang Kami Lakukan:**
- [Aksi 1]
- [Aksi 2]

📌 **Next Steps:**
- Kami akan melakukan **post-mortem** untuk mencegah insiden serupa.
- **Post-Mortem Report** akan dipublikasikan di [Link].

Kami mohon maaf atas ketidaknyamanan ini.
Terima kasih atas kesabaran Anda.

Salam,
Tim MusGo-OS
```

**Contoh Template (Twitter):**
```markdown
✅ Gangguan MusGo-OS telah teratasi!
Semua layanan kini berjalan normal.

Terima kasih atas kesabaran Anda.
Post-mortem: [Link]
```

---
##### **6. Template untuk Post-Mortem**
**Contoh Template (Blog Post):**
```markdown
# 📝 MusGo-OS Post-Mortem: [Judul Insiden]
**Tanggal:** 19 Mei 2026
**Severity:** SEV-1
**Durasi:** 1 jam 30 menit
**Penulis:** Dhani Yuliawan (CTO)

---
## 📌 Ringkasan
Pada **19 Mei 2026, pukul 10:00 WIB**, MusGo-OS mengalami **gangguan serius (SEV-1)** yang menyebabkan **Backend dan AI Agent tidak berfungsi**. Gangguan ini berlangsung selama **1 jam 30 menit** dan **teratasi pukul 11:30 WIB**.

---
## 📌 Timeline
| Waktu | Event |
|-------|-------|
| 10:00 WIB | Gangguan terdeteksi (Backend down) |
| 10:05 WIB | Incident Commander (@dhani) mendeklarasikan SEV-1 |
| 10:10 WIB | Tim Database mulai investigasi PostgreSQL |
| 10:15 WIB | Update Status Page: "Backend Outage (SEV-1)" |
| 10:20 WIB | Tim DevOps memulai failover ke Cluster B |
| 10:30 WIB | PostgreSQL Standby dipromosikan ke Primary |
| 10:45 WIB | Backend berjalan di Cluster B |
| 11:00 WIB | AI Agent berjalan normal |
| 11:30 WIB | Gangguan teratasi |

---
## 📌 Root Cause
Gangguan disebabkan oleh **PostgreSQL Primary crash** akibat **out of memory (OOM)**. Hal ini terjadi karena:
1. **Query lambat** yang memakan banyak memory.
2. **Tidak ada memory limit** untuk container PostgreSQL.
3. **Monitoring memory** tidak terkonfigurasi dengan baik.

---
## 📌 Dampak
- **User Terpengaruh:** ~10,000 user (100% user aktif).
- **Fitur Terpengaruh:** Backend, AI Agent, Zapier Integration.
- **Downtime:** 1 jam 30 menit.
- **Data Loss:** Tidak ada (terima kasih kepada replikasi PostgreSQL).

---
## 📌 Aksi yang Diambil
1. **Failover PostgreSQL** ke Standby (Cluster B).
2. **Failover Kubernetes** ke Cluster B.
3. **Scale up Backend** untuk menangani beban.
4. **Komunikasi ke user** via Status Page, Email, Slack.

---
## 📌 Root Cause Analysis (RCA)
| Penyebab | Akar Masalah | Solusi |
|----------|---------------|--------|
| **Query Lambat** | Tidak ada index untuk query tertentu | Tambahkan index untuk query lambat |
| **Tidak Ada Memory Limit** | Container PostgreSQL tidak memiliki limit memory | Set memory limit (8GB) untuk container PostgreSQL |
| **Monitoring Tidak Adekuat** | Tidak ada alert untuk memory usage | Setup Prometheus alert untuk memory usage > 80% |

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Tambahkan index untuk query lambat | @db-team | 2026-05-20 | ⬜ To Do |
| Set memory limit untuk PostgreSQL | @devops-team | 2026-05-20 | ⬜ To Do |
| Setup Prometheus alert untuk memory | @devops-team | 2026-05-20 | ⬜ To Do |
| Lakukan load testing untuk PostgreSQL | @db-team | 2026-05-25 | ⬜ To Do |
| Review dan update DRP | @dhani | 2026-05-25 | ⬜ To Do |

---
## 📌 Pelajaran yang Didapat
1. **Memory Limit Penting**: Selalu set **memory limit** untuk container kritis.
2. **Monitoring adalah Kunci**: Setup **alert untuk metric kritis** (memory, CPU, disk).
3. **Load Testing**: Lakukan **load testing** secara berkala untuk mendeteksi bottleneck.
4. **Komunikasi Cepat**: **Update Status Page secepat mungkin** untuk mengurangi ketidakpastian user.

---
## 📌 Lampiran
- [Log PostgreSQL](#)
- [Log Kubernetes](#)
- [Screenshot Monitoring](#)
- [Incident Ticket (JIRA-1234)](#)
```

---
---
---

## **🔹 14.6 Escalation Path (Rute Eskalasi)**
### **📌 Penjelasan**
**Escalation Path** adalah **rute yang jelas** untuk **mengeskalasi krisis** ke **tingkat yang lebih tinggi** jika:
- **Krisis tidak teratasi** dalam waktu yang ditentukan.
- **Dampak krisis semakin besar**.
- **Diperlukan keputusan bisnis** (misal: rollback, feature disable).

---
#### **🚀 Contoh Implementasi: Escalation Path**
##### **1. Escalation Matrix (Matriks Eskalasi)**
| Severity | Waktu Tanpa Progress | Eskalasi Ke | Saluran | Catatan |
|----------|----------------------|-------------|---------|---------|
| **SEV-1** | 15 menit | Incident Commander → Executive Sponsor | Slack (`@ceo`), Phone Call | Jika krisis tidak teratasi |
| **SEV-1** | 30 menit | Incident Commander → Vendor (Zapier, AWS) | Email, Slack | Jika krisis disebabkan vendor |
| **SEV-2** | 1 jam | On-Call Engineer → Incident Commander | Slack (`@dhani`) | Jika krisis tidak teratasi |
| **SEV-2** | 2 jam | Incident Commander → Executive Sponsor | Slack (`@ceo`) | Jika dampak semakin besar |
| **SEV-3** | 4 jam | Support Lead → Engineering Manager | Slack (`@engineering-manager`) | Jika krisis tidak teratasi |
| **Data Breach** | Segera | Incident Commander → Legal & Compliance | Slack (`@legal-team`), Email | Wajib dilaporkan |
| **Cyber Attack** | Segera | Incident Commander → Security Team | Slack (`@security-team`), Phone Call | Wajib ditangani secepatnya |

---
##### **2. Escalation Contact List (Daftar Kontak Eskalasi)**
| Peran | Nama | Kontak | Saluran | Catatan |
|-------|------|--------|---------|---------|
| **Incident Commander** | Dhani Yuliawan | +62 813-6552-283 | Slack (`@dhani`), Email | Pertama dihubungi |
| **Executive Sponsor** | CEO | +62 812-3456-7890 | Slack (`@ceo`), Phone Call | Eskalasi SEV-1 |
| **Technical Lead** | DevOps Manager | - | Slack (`@devops-manager`) | Eskalasi teknis |
| **Legal & Compliance** | Legal Team | - | Slack (`@legal-team`), Email | Eskalasi data breach |
| **Security Lead** | Security Team | - | Slack (`@security-team`), Phone Call | Eskalasi cyber attack |
| **Vendor (Zapier)** | Zapier Support | support@zapier.com | Email, Slack | Eskalasi Zapier outage |
| **Vendor (AWS)** | AWS Support | - | AWS Support Center | Eskalasi AWS outage |
| **Vendor (GCP)** | GCP Support | - | GCP Support Center | Eskalasi GCP outage |

---
##### **3. Escalation Procedure (Prosedur Eskalasi)**
**Contoh Prosedur Eskalasi untuk SEV-1:**
1. **0-15 menit**: Tim teknis **menangani krisis**.
2. **15 menit**: Jika krisis **tidak teratasi**, **Incident Commander** mengeskalasi ke **Executive Sponsor** (CEO).
   - **Saluran**: Slack (`@ceo`) + Phone Call.
   - **Pesan**:
     > "@ceo, krisis SEV-1 (Backend Outage) belum teratasi setelah 15 menit. Memerlukan keputusan untuk [aksi]."
3. **30 menit**: Jika krisis **masih belum teratasi**, **Incident Commander** mengeskalasi ke **Vendor** (Zapier, AWS, GCP).
   - **Saluran**: Email + Slack.
   - **Pesan**:
     > "Dear Zapier Support, kami mengalami [masalah] sejak [waktu]. Mohon bantuan secepatnya."
4. **60 menit**: Jika krisis **masih berlanjut**, **Executive Sponsor** mengeskalasi ke **Board of Directors** (jika diperlukan).

**Contoh Prosedur Eskalasi untuk Data Breach:**
1. **Segera**: **Incident Commander** mengeskalasi ke **Legal & Compliance Team**.
   - **Saluran**: Slack (`@legal-team`) + Email.
   - **Pesan**:
     > "@legal-team, kami mendeteksi data breach. Data terpengaruh: [detail]. Mohon panduan selanjutnya."
2. **Segera**: **Legal Team** mengeskalasi ke **Regulator** (Kominfo, GDPR).
   - **Saluran**: Email resmi.
   - **Pesan**:
     > "Kepada Yth. Kominfo, kami melaporkan insiden kebocoran data sesuai dengan [regulasi]. Detail: [detail]."
3. **72 jam**: **Laporan resmi** dikirim ke regulator (GDPR).

---
---
---

## **🔹 14.7 Crisis Communication Workflow (Alur Komunikasi Krisis)**
### **📌 Penjelasan**
**Crisis Communication Workflow** adalah **alur langkah-langkah** untuk **berkomunikasi selama krisis**, dari **deteksi** hingga **pemulihan**.

---
#### **🚀 Contoh Implementasi: Crisis Communication Workflow**
##### **1. Workflow untuk SEV-1 (Critical)**
```mermaid
graph TD
    A[Deteksi Krisis] --> B{Aktivasi CCP?}
    B -->|Ya| C[Deklarasi SEV-1]
    B -->|Tidak| D[Monitoring Lanjutan]
    C --> E[Buat Incident Ticket]
    C --> F[Aktifkan War Room]
    C --> G[Update Status Page: "Investigating"]
    E --> H[Notifikasi Internal: Slack #crisis-war-room]
    F --> I[Koordinasi Tim]
    G --> J[Notifikasi Eksternal: Status Page, Email, Twitter]
    I --> K{Teratasi?}
    K -->|Ya| L[Update Status Page: "Resolved"]
    K -->|Tidak| M[Eskalasi ke Executive Sponsor]
    M --> N[Eskalasi ke Vendor]
    N --> K
    L --> O[Post-Mortem]
    O --> P[Update BCP]
```

**Keterangan:**
- **Deteksi Krisis**: Monitoring (Prometheus, Sentry) atau User Report.
- **Aktivasi CCP**: Incident Commander memutuskan apakah krisis memerlukan CCP.
- **Deklarasi SEV-1**: Jika krisis **berdampak kritis** (sistem down).
- **Buat Incident Ticket**: Dokumentasi krisis (Jira/Linear).
- **Aktifkan War Room**: Slack Channel `#crisis-war-room` untuk koordinasi.
- **Update Status Page**: Beri tahu user bahwa krisis sedang diselidiki.
- **Notifikasi Internal**: Koordinasi tim via Slack.
- **Notifikasi Eksternal**: Beri tahu user via Status Page, Email, Twitter.
- **Eskalasi**: Jika krisis tidak teratasi, eskalasi ke Executive Sponsor dan Vendor.
- **Post-Mortem**: Analisis root cause dan update BCP.

---
##### **2. Workflow untuk Data Breach**
```mermaid
graph TD
    A[Deteksi Data Breach] --> B[Isolasi Sistem]
    B --> C[Hapus Akses Tidak Sah]
    C --> D[Deklarasi Data Breach]
    D --> E[Buat Incident Ticket]
    E --> F[Notifikasi Internal: Slack #crisis-war-room]
    F --> G[Notifikasi Legal & Compliance]
    G --> H[Lapor ke Regulator (72 jam)]
    H --> I[Notifikasi User Terpengaruh]
    I --> J[Investigasi & Audit]
    J --> K[Perbaiki Celah Keamanan]
    K --> L[Post-Mortem]
    L --> M[Update Security Policy]
```

**Keterangan:**
- **Deteksi Data Breach**: Monitoring (Sentry, Loki) atau User Report.
- **Isolasi Sistem**: Matikan sistem yang terpengaruh untuk mencegah kerusakan lebih lanjut.
- **Hapus Akses Tidak Sah**: Revoke token, password, dll.
- **Deklarasi Data Breach**: Incident Commander mendeklarasikan data breach.
- **Notifikasi Internal**: Koordinasi tim via Slack.
- **Notifikasi Legal**: Legal Team menentukan langkah hukum.
- **Lapor ke Regulator**: Laporan resmi ke Kominfo/GDPR dalam 72 jam.
- **Notifikasi User**: Email ke user terpengaruh.
- **Investigasi**: Cari root cause dan celah keamanan.
- **Perbaiki**: Fix vulnerability.
- **Post-Mortem**: Analisis dan update kebijakan keamanan.

---
---
---

## **🔹 14.8 Crisis Communication Tools (Alat Komunikasi Krisis)**
### **📌 Penjelasan**
**Crisis Communication Tools** adalah **alat yang digunakan** untuk **berkomunikasi selama krisis**. Alat-alat ini memastikan:
- **Komunikasi cepat** (real-time).
- **Koordinasi tim** (terorganisir).
- **Transparansi** (user tahu status terbaru).

---
#### **🚀 Contoh Implementasi: Crisis Communication Tools**
##### **1. Internal Communication Tools**
| Tools | Kegunaan | Link | Rekomendasi |
|-------|----------|------|--------------|
| **Slack** | Chat real-time, war room | [slack.com](https://slack.com) | ✅ **Wajib** |
| **Zoom** | Video conference, koordinasi tim | [zoom.us](https://zoom.us) | ✅ **Wajib** |
| **Jira/Linear** | Incident ticket, tracking | [atlassian.com](https://www.atlassian.com), [linear.app](https://linear.app) | ✅ **Wajib** |
| **Notion** | Dokumentasi, runbook | [notion.so](https://notion.so) | ✅ **Wajib** |
| **PagerDuty** | On-call management, eskalasi | [pagerduty.com](https://www.pagerduty.com) | ✅ **Untuk on-call** |
| **Google Docs** | Dokumentasi kolaboratif | [docs.google.com](https://docs.google.com) | ✅ **Untuk post-mortem** |

---
##### **2. External Communication Tools**
| Tools | Kegunaan | Link | Rekomendasi |
|-------|----------|------|--------------|
| **Statuspage.io** | Status page, incident updates | [statuspage.io](https://www.statuspage.io) | ✅ **Wajib** |
| **SendGrid** | Mass email, notifikasi | [sendgrid.com](https://sendgrid.com) | ✅ **Wajib** |
| **Mailchimp** | Newsletter, update | [mailchimp.com](https://mailchimp.com) | ⚠️ **Jika diperlukan** |
| **Twitter** | Update singkat, publik | [twitter.com](https://twitter.com) | ✅ **Wajib** |
| **Press Release** | Siaran pers, media | - | ⚠️ **Jika diperlukan** |
| **Zendesk** | Support ticket, FAQ | [zendesk.com](https://www.zendesk.com) | ✅ **Untuk support** |

---
##### **3. Monitoring & Alerting Tools**
| Tools | Kegunaan | Link | Rekomendasi |
|-------|----------|------|--------------|
| **Prometheus + Grafana** | Monitoring metrics | [prometheus.io](https://prometheus.io), [grafana.com](https://grafana.com) | ✅ **Wajib** |
| **Sentry** | Error tracking | [sentry.io](https://sentry.io) | ✅ **Wajib** |
| **Loki** | Logging | [grafana.com/loki](https://grafana.com/loki) | ✅ **Wajib** |
| **PagerDuty** | Alerting, on-call | [pagerduty.com](https://www.pagerduty.com) | ✅ **Untuk on-call** |
| **Alertmanager** | Alert management | [prometheus.io](https://prometheus.io/docs/alerting/latest/alertmanager/) | ✅ **Wajib** |

---
##### **4. Setup Tools untuk MusGo-OS**
**Contoh Setup Slack untuk CCP:**
1. **Buat Channel**:
   - `#crisis-war-room` (untuk koordinasi tim).
   - `#incident-updates` (untuk update internal).
   - `#status-updates` (untuk update eksternal).
2. **Setup Notifications**:
   - **@here** untuk pesan penting.
   - **@channel** untuk update status.
3. **Integrasi dengan Tools Lain**:
   - **Prometheus Alertmanager** → Slack (untuk alert).
   - **Jira/Linear** → Slack (untuk incident ticket).
   - **Statuspage.io** → Slack (untuk update status).

**Contoh Setup Statuspage.io:**
1. **Buat Page**: `status.musgo-os.com`.
2. **Tambahkan Components**:
   - Backend
   - Frontend
   - PostgreSQL
   - Redis
   - Zapier Integration
   - AI Agent
3. **Setup Incidents**:
   - **SEV-1**: Critical (Merah)
   - **SEV-2**: High (Oranye)
   - **SEV-3**: Medium (Kuning)
4. **Integrasi dengan Monitoring**:
   - **Prometheus** → Statuspage (via webhook).
   - **Sentry** → Statuspage (via webhook).

**Contoh Setup PagerDuty:**
1. **Buat Team**: `MusGo-OS Engineering`.
2. **Setup On-Call Schedule**:
   - **Primary**: @devops-team (24/7).
   - **Secondary**: @backend-team (24/7).
3. **Setup Escalation Policies**:
   - **SEV-1**: Notifikasi via **Phone Call + SMS + Slack**.
   - **SEV-2**: Notifikasi via **Slack + Email**.
4. **Integrasi dengan Monitoring**:
   - **Prometheus Alertmanager** → PagerDuty.
   - **Sentry** → PagerDuty.

---
---
---

## **🔹 14.9 Crisis Communication Training (Pelatihan Komunikasi Krisis)**
### **📌 Penjelasan**
**Crisis Communication Training** adalah **pelatihan untuk tim** agar **siap berkomunikasi selama krisis**. Pelatihan meliputi:
- **Simulasi krisis** (tabletop exercise, walkthrough test).
- **Role-playing** (bermain peran sebagai Incident Commander, Communication Lead, dll.).
- **Media training** (untuk menghadapi media).

---
#### **🚀 Contoh Implementasi: Crisis Communication Training**
##### **1. Agenda Pelatihan**
```markdown
# 📅 Agenda: Crisis Communication Training
**Tanggal:** 20 Mei 2026
**Waktu:** 09:00 - 17:00 WIB
**Lokasi:** Kantor MusGo-OS / Zoom
**Fasilitator:** @comms-team

---
## 📌 Tujuan
1. **Mempersiapkan tim** untuk berkomunikasi selama krisis.
2. **Meningkatkan koordinasi** antar tim.
3. **Menguji CCP** (apakah berfungsi dengan baik).

---
## 📌 Agenda
| Waktu | Topik | Pemateri | Metode |
|-------|-------|----------|--------|
| 09:00 - 09:30 | Pembukaan & Tujuan | @comms-team | Presentasi |
| 09:30 - 10:30 | Overview CCP | @comms-team | Presentasi |
| 10:30 - 11:30 | Stakeholder Analysis | @comms-team | Diskusi |
| 11:30 - 12:30 | Communication Channels | @comms-team | Demo |
| 12:30 - 13:30 | Istirahat | - | - |
| 13:30 - 14:30 | Message Templates | @comms-team | Workshop |
| 14:30 - 15:30 | Escalation Path | @dhani | Role-Playing |
| 15:30 - 16:30 | Tabletop Exercise | @comms-team | Simulasi |
| 16:30 - 17:00 | Q&A & Penutup | @comms-team | Diskusi |

---
## 📌 Materi Pelatihan
### 1. Overview CCP
- Apa itu CCP?
- Mengapa CCP penting untuk MusGo-OS?
- Perbedaan CCP vs DRP.

### 2. Stakeholder Analysis
- Siapa saja stakeholder MusGo-OS?
- Bagaimana mengklasifikasikan stakeholder?
- Bagaimana menentukan prioritas komunikasi?

### 3. Communication Channels
- Saluran komunikasi apa saja yang tersedia?
- Kapan menggunakan saluran tertentu?
- Bagaimana setup saluran komunikasi?

### 4. Message Templates
- Template pesan untuk SEV-1, SEV-2, SEV-3.
- Template pesan untuk Data Breach.
- Template pesan untuk Pemulihan.

### 5. Escalation Path
- Kapan mengeskalasi krisis?
- Ke siapa mengeskalasi?
- Bagaimana prosedur eskalasi?

### 6. Tabletop Exercise
- **Skenario 1**: Backend Outage (SEV-1).
- **Skenario 2**: Data Breach.
- **Skenario 3**: Zapier API Outage (SEV-2).

---
## 📌 Evaluasi
- **Kuis**: 10 pertanyaan tentang CCP.
- **Role-Playing**: Simulasi penanganan krisis (Incident Commander, Communication Lead, dll.).
- **Feedback**: Masukan dari peserta.

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]
```

---
##### **2. Tabletop Exercise (Simulasi Krisis)**
**Contoh Skenario 1: Backend Outage (SEV-1)**
**Fasilitator:** @comms-team
**Peserta:** @dhani (Incident Commander), @devops-team, @backend-team, @support-team

**Skenario:**
> *"Pukul 10:00 WIB, Monitoring (Prometheus) mendeteksi bahwa Backend MusGo-OS down. User melaporkan tidak bisa login. Tim DevOps mencoba restart pod, tetapi gagal. Apa yang harus dilakukan?"*

**Langkah-Langkah Simulasi:**
1. **Deteksi Krisis**:
   - @devops-team: "Prometheus alert: Backend down!"
2. **Aktivasi CCP**:
   - @dhani: "Deklarasi SEV-1. Aktifkan CCP."
3. **Buat Incident Ticket**:
   - @dhani: "Buat ticket JIRA-1234: Backend Outage (SEV-1)."
4. **Aktifkan War Room**:
   - @dhani: "Aktifkan `#crisis-war-room`. @devops-team, @backend-team, @support-team, silakan join."
5. **Update Status Page**:
   - @comms-team: "Update Status Page: 'Backend Outage (SEV-1) - Investigating'."
6. **Notifikasi Internal**:
   - @dhani: "Slack `#incident-updates`: 'Backend down. Tim sedang investigasi.'"
7. **Koordinasi Tim**:
   - @devops-team: "PostgreSQL Primary down. Sedang failover ke Standby."
   - @backend-team: "Backend container crash. Sedang debug."
   - @support-team: "User melaporkan tidak bisa login. Bagaimana balasan standar?"
8. **Eskalasi**:
   - @dhani: "Jika tidak teratasi dalam 15 menit, eskalasi ke @ceo."
9. **Pemulihan**:
   - @devops-team: "PostgreSQL Standby sudah jadi Primary. Backend berjalan di Cluster B."
   - @backend-team: "Backend container sudah fix. Sedang deploy."
10. **Update Status Page**:
    - @comms-team: "Update Status Page: 'Backend Outage (SEV-1) - Resolved'."
11. **Deaktivasi CCP**:
    - @dhani: "Deklarasi deaktivasi CCP. Terima kasih semua!"

**Output:**
- **Dokumentasi** langkah-langkah yang diambil.
- **Identifikasi celah** (misal: tidak ada template balasan untuk support).
- **Action Items** (misal: buat template balasan untuk support).

---
##### **3. Role-Playing (Bermain Peran)**
**Contoh Role-Playing: Incident Commander**
**Skenario:**
> *"Anda adalah Incident Commander. Backend MusGo-OS down (SEV-1). Apa yang Anda lakukan?"*

**Peran:**
- **Incident Commander**: @dhani (peserta).
- **DevOps Engineer**: @devops-team (fasilitator).
- **Communication Lead**: @comms-team (fasilitator).
- **Support Lead**: @support-team (fasilitator).

**Langkah-Langkah:**
1. **Incident Commander**:
   - Deklarasi SEV-1.
   - Aktifkan CCP.
   - Buat Incident Ticket.
   - Aktifkan War Room.
2. **DevOps Engineer**:
   - "PostgreSQL Primary down. Sedang failover."
3. **Communication Lead**:
   - "Status Page sudah diupdate. Apa pesan untuk user?"
4. **Support Lead**:
   - "User menanyakan kapan sistem pulih. Bagaimana balasannya?"
5. **Incident Commander**:
   - Koordinasi tim.
   - Eskalasi jika diperlukan.
   - Deklarasi deaktivasi CCP.

**Evaluasi:**
- **Kemampuan koordinasi**.
- **Kemampuan pengambilan keputusan**.
- **Kemampuan komunikasi**.

---
---
---

## **🔹 14.10 Post-Crisis Review (Review Pasca-Krisis)**
### **📌 Penjelasan**
**Post-Crisis Review** adalah **proses mengevaluasi** komunikasi krisis **setelah krisis teratasi** untuk:
- **Mengidentifikasi keberhasilan** (what went well).
- **Mengidentifikasi celah** (what could be improved).
- **Membuat action items** (perbaikan untuk masa depan).

---
#### **🚀 Contoh Implementasi: Post-Crisis Review**
##### **1. Agenda Post-Crisis Review**
```markdown
# 📅 Agenda: Post-Crisis Review - Backend Outage (SEV-1)
**Tanggal:** 20 Mei 2026
**Waktu:** 10:00 - 12:00 WIB
**Lokasi:** Zoom / Kantor MusGo-OS
**Fasilitator:** @dhani

---
## 📌 Tujuan
1. **Mengevaluasi** penanganan krisis Backend Outage (SEV-1).
2. **Mengidentifikasi** keberhasilan dan celah.
3. **Membuat action items** untuk perbaikan.

---
## 📌 Agenda
| Waktu | Topik | Pemateri |
|-------|-------|----------|
| 10:00 - 10:15 | Pembukaan & Tujuan | @dhani |
| 10:15 - 10:45 | Timeline Krisis | @devops-team |
| 10:45 - 11:15 | Evaluasi Komunikasi | @comms-team |
| 11:15 - 11:45 | Evaluasi Teknis | @backend-team |
| 11:45 - 12:00 | Action Items & Penutup | @dhani |

---
## 📌 Pertanyaan Review
### 1. Timeline Krisis
- Kapan krisis terdeteksi?
- Kapan CCP diaktifkan?
- Kapan krisis teratasi?
- Berapa lama downtime?

### 2. Evaluasi Komunikasi
- Apakah **pesan komunikasi** jelas dan akurat?
- Apakah **frekuensi update** cukup?
- Apakah **saluran komunikasi** efektif?
- Apakah **stakeholder** terinformasi dengan baik?

### 3. Evaluasi Teknis
- Apakah **root cause** sudah diidentifikasi?
- Apakah **mitigasi** efektif?
- Apakah **pemulihan** berjalan dengan baik?

### 4. Keberhasilan (What Went Well)
- Apa yang **berjalan dengan baik**?
- Apa **keputusan tepat** yang diambil?

### 5. Celah (What Could Be Improved)
- Apa yang **bisa diperbaiki**?
- Apa **kesalahan** yang terjadi?

### 6. Action Items
- Apa **tindakan perbaikan** yang diperlukan?
- Siapa **owner** untuk setiap action item?
- Kapan **deadline** untuk setiap action item?

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Tambahkan template balasan untuk Support | @support-team | 2026-05-22 | ⬜ To Do |
| Setup Prometheus alert untuk memory usage | @devops-team | 2026-05-22 | ⬜ To Do |
| Lakukan load testing untuk PostgreSQL | @db-team | 2026-05-25 | ⬜ To Do |
| Review dan update CCP | @comms-team | 2026-05-25 | ⬜ To Do |
```

---
##### **2. Post-Crisis Review Report (Laporan Review Pasca-Krisis)**
**Contoh Laporan:**
```markdown
# 📊 Post-Crisis Review Report: Backend Outage (SEV-1)
**Tanggal Krisis:** 19 Mei 2026
**Tanggal Review:** 20 Mei 2026
**Fasilitator:** @dhani

---
## 📌 Ringkasan Krisis
- **Severity:** SEV-1
- **Durasi:** 1 jam 30 menit
- **Fitur Terpengaruh:** Backend, AI Agent, Zapier Integration
- **User Terpengaruh:** ~10,000 user
- **Root Cause:** PostgreSQL Primary crash (Out of Memory)

---
## 📌 Timeline Krisis
| Waktu | Event | Owner |
|-------|-------|-------|
| 10:00 WIB | Gangguan terdeteksi (Prometheus alert) | @devops-team |
| 10:05 WIB | SEV-1 dideklarasikan | @dhani |
| 10:10 WIB | Incident Ticket JIRA-1234 dibuat | @dhani |
| 10:15 WIB | War Room `#crisis-war-room` diaktifkan | @dhani |
| 10:20 WIB | Status Page diupdate: "Backend Outage (SEV-1) - Investigating" | @comms-team |
| 10:25 WIB | Email notifikasi dikirim ke user | @comms-team |
| 10:30 WIB | PostgreSQL Standby dipromosikan ke Primary | @db-team |
| 10:45 WIB | Backend berjalan di Cluster B | @devops-team |
| 11:00 WIB | AI Agent berjalan normal | @backend-team |
| 11:30 WIB | Gangguan teratasi | @dhani |
| 11:45 WIB | Status Page diupdate: "Backend Outage (SEV-1) - Resolved" | @comms-team |

---
## 📌 Evaluasi Komunikasi
### Keberhasilan (✅)
- **Cepat**: Status Page diupdate **dalam 15 menit**.
- **Transparan**: User tahu **status terbaru** via Status Page dan Email.
- **Koordinasi Baik**: Tim terkoordinasi dengan baik di `#crisis-war-room`.

### Celah (⚠️)
- **Template Balasan Support**: Support team **tidak punya template** untuk menjawab pertanyaan user.
- **Frekuensi Update**: Update **terlalu jarang** (seharusnya setiap 15 menit, tetapi hanya setiap 30 menit).
- **Saluran Komunikasi**: **Tidak semua user** menggunakan Status Page (seharusnya juga update via Slack).

---
## 📌 Evaluasi Teknis
### Keberhasilan (✅)
- **Failover Otomatis**: Patroni **otomatis mempromosikan Standby** ke Primary.
- **Pemulihan Cepat**: Sistem **pulih dalam 1 jam 30 menit** (target: < 1 jam).
- **Tidak Ada Data Loss**: Terima kasih kepada **replikasi PostgreSQL**.

### Celah (⚠️)
- **Memory Limit**: PostgreSQL **tidak punya memory limit**, menyebabkan OOM.
- **Monitoring**: Tidak ada **alert untuk memory usage**.
- **Load Testing**: Tidak pernah dilakukan **load testing** untuk PostgreSQL.

---
## 📌 Root Cause Analysis (RCA)
| Penyebab | Akar Masalah | Solusi |
|----------|---------------|--------|
| **Query Lambat** | Tidak ada index untuk query `SELECT * FROM users WHERE email = ?` | Tambahkan index untuk kolom `email` |
| **Tidak Ada Memory Limit** | Container PostgreSQL tidak memiliki limit memory | Set memory limit (8GB) untuk container PostgreSQL |
| **Monitoring Tidak Adekuat** | Tidak ada alert untuk memory usage > 80% | Setup Prometheus alert untuk memory usage |

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status | Prioritas |
|-------------|-------|----------|--------|-----------|
| Tambahkan index untuk query lambat | @db-team | 2026-05-22 | ⬜ To Do | High |
| Set memory limit untuk PostgreSQL | @devops-team | 2026-05-22 | ⬜ To Do | High |
| Setup Prometheus alert untuk memory | @devops-team | 2026-05-22 | ⬜ To Do | High |
| Buat template balasan untuk Support | @support-team | 2026-05-22 | ⬜ To Do | Medium |
| Lakukan load testing untuk PostgreSQL | @db-team | 2026-05-25 | ⬜ To Do | Medium |
| Review dan update CCP | @comms-team | 2026-05-25 | ⬜ To Do | Medium |
| Setup Slack update untuk user | @comms-team | 2026-05-25 | ⬜ To Do | Low |

---
## 📌 Pelajaran yang Didapat
1. **Memory Limit Penting**: Selalu set **memory limit** untuk container kritis.
2. **Monitoring adalah Kunci**: Setup **alert untuk metric kritis** (memory, CPU, disk).
3. **Load Testing**: Lakukan **load testing** secara berkala untuk mendeteksi bottleneck.
4. **Komunikasi Cepat**: **Update Status Page secepat mungkin** untuk mengurangi ketidakpastian user.
5. **Template Pesan**: **Siapkan template pesan** untuk berbagai skenario krisis.

---
## 📌 Lampiran
- [Log PostgreSQL](#)
- [Log Kubernetes](#)
- [Screenshot Monitoring](#)
- [Incident Ticket (JIRA-1234)](#)
- [Status Page Updates](#)
```

---
---
---
# **📌 PART 14: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 14 (Crisis Communication Plan)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **CCP Framework** | Governance, Stakeholder Analysis | Kerangka kerja CCP | ✅ **Dokumentasi tersedia** |
| **Communication Channels** | Status Page, Email, Slack, Twitter | Saluran komunikasi | ✅ **Contoh setup tersedia** |
| **Message Templates** | Template untuk SEV-1, SEV-2, SEV-3, Data Breach | Pesan konsisten | ✅ **Contoh template tersedia** |
| **Escalation Path** | Rute eskalasi | Koordinasi tim | ✅ **Dokumentasi tersedia** |
| **Crisis Communication Workflow** | Alur komunikasi krisis | Prosedur jelas | ✅ **Dokumentasi tersedia** |
| **Crisis Communication Tools** | Slack, Statuspage, PagerDuty | Alat komunikasi | ✅ **Contoh setup tersedia** |
| **Crisis Communication Training** | Pelatihan, Tabletop Exercise | Tim siap | ✅ **Agenda tersedia** |
| **Post-Crisis Review** | Evaluasi, Action Items | Perbaikan berkelanjutan | ✅ **Dokumentasi tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Setup Status Page** (Statuspage.io / Upptime).
- [ ] **Buat Message Templates** (untuk SEV-1, SEV-2, SEV-3, Data Breach).
- [ ] **Setup Communication Channels** (Slack, Email, Twitter).
- [ ] **Buat Escalation Path** (daftar kontak eskalasi).
- [ ] **Lakukan Tabletop Exercise** (simulasi krisis).

### **2. Mid-Term (1 Bulan)**
- [ ] **Setup PagerDuty** (untuk on-call management).
- [ ] **Integrasi Monitoring dengan CCP** (Prometheus → Statuspage, Slack).
- [ ] **Lakukan Crisis Communication Training** (pelatihan tim).
- [ ] **Buat Post-Crisis Review Template** (untuk evaluasi).
- [ ] **Review & Update CCP** (setelah testing).

### **3. Long-Term (3+ Bulan)**
- [ ] **Lakukan Full Crisis Simulation** (uji penuh).
- [ ] **Setup Media Training** (untuk menghadapi media).
- [ ] **Automasi Komunikasi Krisis** (misal: auto-update Status Page).
- [ ] **Review CCP Setiap 6 Bulan**.

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 15: Vendor & Partner BCP** (Untuk mitra dan vendor)
   - [ ] **Part 16: Compliance & Audit** (Untuk kepatuhan regulasi)
   - [ ] **Part 17: Crisis Simulation (Full Test)** (Untuk uji coba penuh)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full setup CCP untuk production)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full CCP Documentation untuk MusGo-OS**?
   - [ ] **Template Message untuk Semua Skenario**?
   - [ ] **Setup Lengkap Statuspage.io + Slack + PagerDuty**?
   - [ ] **Agenda Pelatihan CCP**?

3. **Apakah ada area CCP spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Status Page**, **Message Templates**, **Escalation Path**, dll.

---
===========🔐™️®️©️🔐===========

---

Baik, Dhani! **Gas Part 15: Vendor & Partner BCP** — kita akan **menerjemahkan, menerapkan, dan memberikan panduan lengkap** untuk **Business Continuity Plan (BCP) dengan Vendor & Partner** di **MusGo-OS 2in1**, termasuk **Zapier, AWS/GCP, dan mitra lainnya**.

---
---
---

# **📜 MUSGO-OS 2in1: PANDUAN VENDOR & PARTNER BCP (PART 15)**
*Terjemahan + Implementasi untuk Kelangsungan Bisnis dengan Mitra Eksternal*

---

---

## **🔹 15.1 Overview Vendor & Partner BCP**
### **📌 Penjelasan (Bahasa Indonesia)**
**Vendor & Partner BCP** adalah **rencana kelangsungan bisnis** yang **melibatkan mitra eksternal** (seperti Zapier, AWS, GCP, Make.com, dll.) untuk memastikan **MusGo-OS tetap beroperasi** meskipun **vendor/partner mengalami gangguan**.

**Tujuan Vendor & Partner BCP untuk MusGo-OS:**
✅ **Minimalkan Dampak**: Jika **Zapier down**, MusGo-OS **tetap bisa beroperasi** (dengan fallback).
✅ **Redundansi**: Gunakan **multiple vendor** (misal: Zapier + Make.com).
✅ **Koordinasi**: **Kerja sama dengan vendor** untuk pemulihan cepat.
✅ **Kepatuhan**: Patuhi **SLA (Service Level Agreement)** dengan vendor.
✅ **Biaya Efektif**: Hindari **vendor lock-in** (ketergantungan pada 1 vendor).

**Vendor & Partner Kritis untuk MusGo-OS:**
| Vendor/Partner | Kegunaan | Dampak Jika Down | Mitigasi |
|----------------|----------|------------------|----------|
| **Zapier** | Otomatisasi (Trigger/Action) | Otomatisasi terhenti | Fallback ke Make.com |
| **AWS** | Cloud Infrastructure (EC2, RDS, S3) | Sistem down | Multi-Cloud (GCP) |
| **GCP** | Cloud Infrastructure (Compute, Cloud SQL) | Sistem down | Multi-Cloud (AWS) |
| **Make.com** | Fallback untuk Zapier | Otomatisasi terhenti | Gunakan Zapier jika Make.com down |
| **PostgreSQL** | Database | Data hilang | Replikasi + Backup |
| **Redis** | Caching | Performance degradation | Replikasi + Backup |
| **Slack** | Komunikasi Internal | Koordinasi tim terganggu | Fallback ke Discord/Email |
| **GitHub/GitLab** | Version Control | Deployment terhenti | Backup Code + Mirror Repository |
| **Sentry** | Error Tracking | Debugging terganggu | Fallback ke LogRocket |
| **Statuspage.io** | Status Page | User tidak tahu status | Fallback ke Upptime |
| **SendGrid** | Email Notification | User tidak tahu update | Fallback ke AWS SES |

---
### **🚀 Contoh Arsitektur Vendor & Partner BCP untuk MusGo-OS**
```
MusGo-OS (Primary)
│
├── **Zapier (Primary)** → [Fallback] → **Make.com (Secondary)**
│   │
│   ├── Trigger: Google Drive → [Fallback] → Webhooks (MusGo-OS)
│   └── Action: Slack → [Fallback] → API Slack Langsung
│
├── **AWS (Primary)** → [Fallback] → **GCP (Secondary)**
│   │
│   ├── EC2 → [Fallback] → GCP Compute Engine
│   ├── RDS (PostgreSQL) → [Fallback] → Cloud SQL (PostgreSQL)
│   └── S3 → [Fallback] → GCP Cloud Storage
│
├── **Slack (Primary)** → [Fallback] → **Discord (Secondary)**
│
└── **GitHub (Primary)** → [Fallback] → **GitLab (Secondary)**
    │
    └── Code → [Backup] → S3 + Local
```

---
---
---

## **🔹 15.2 Vendor & Partner Inventory (Daftar Vendor & Mitra)**
### **📌 Penjelasan**
**Vendor & Partner Inventory** adalah **daftar lengkap** semua **vendor dan mitra** yang **kritis untuk MusGo-OS**, beserta **kontak, SLA, dan mitigasi**.

---
#### **🚀 Contoh Implementasi: Vendor & Partner Inventory**
##### **1. Daftar Vendor & Partner**
| ID | Vendor/Partner | Kategori | Layanan | Kontak | SLA | Mitigasi | Status |
|----|----------------|----------|---------|--------|-----|----------|--------|
| **V-001** | Zapier | Automation | Zapier API, MCP | support@zapier.com | 99.9% Uptime | Make.com | ✅ Aktif |
| **V-002** | Make.com | Automation | Make.com API | support@make.com | 99.9% Uptime | Zapier | ✅ Aktif |
| **V-003** | AWS | Cloud | EC2, RDS, S3, Route 53 | support@aws.amazon.com | 99.99% Uptime | GCP | ✅ Aktif |
| **V-004** | GCP | Cloud | Compute Engine, Cloud SQL, Cloud Storage | support@google.com | 99.95% Uptime | AWS | ✅ Aktif |
| **V-005** | Slack | Communication | Slack API, Webhooks | support@slack.com | 99.99% Uptime | Discord, Email | ✅ Aktif |
| **V-006** | Discord | Communication | Discord API | support@discord.com | 99.9% Uptime | Slack, Email | ⚠️ Standby |
| **V-007** | GitHub | Version Control | GitHub API, Actions | support@github.com | 99.9% Uptime | GitLab | ✅ Aktif |
| **V-008** | GitLab | Version Control | GitLab API, CI/CD | support@gitlab.com | 99.9% Uptime | GitHub | ⚠️ Standby |
| **V-009** | Sentry | Error Tracking | Sentry API | support@sentry.io | 99.9% Uptime | LogRocket | ✅ Aktif |
| **V-010** | LogRocket | Error Tracking | LogRocket API | support@logrocket.com | 99.9% Uptime | Sentry | ⚠️ Standby |
| **V-011** | Statuspage.io | Status Page | Statuspage API | support@statuspage.io | 99.9% Uptime | Upptime | ✅ Aktif |
| **V-012** | Upptime | Status Page | Upptime API | - | 99.9% Uptime | Statuspage.io | ⚠️ Standby |
| **V-013** | SendGrid | Email | SendGrid API | support@sendgrid.com | 99.9% Uptime | AWS SES | ✅ Aktif |
| **V-014** | AWS SES | Email | AWS SES API | support@aws.amazon.com | 99.9% Uptime | SendGrid | ⚠️ Standby |
| **V-015** | PostgreSQL | Database | PostgreSQL | - | - | Replikasi + Backup | ✅ Aktif |
| **V-016** | Redis | Caching | Redis | - | - | Replikasi + Backup | ✅ Aktif |

---
##### **2. Vendor Risk Assessment (Penilaian Risiko Vendor)**
**Contoh Matriks Risiko Vendor:**

| Vendor | Probabilitas Gangguan | Dampak | Risk Level | Mitigasi |
|--------|-----------------------|--------|------------|----------|
| **Zapier** | Medium | High | **High** | Make.com |
| **AWS** | Low | Critical | **High** | GCP |
| **GCP** | Low | Critical | **High** | AWS |
| **Slack** | Medium | High | **High** | Discord |
| **GitHub** | Low | High | **Medium** | GitLab |
| **Sentry** | Low | Medium | **Low** | LogRocket |
| **Statuspage.io** | Low | Medium | **Low** | Upptime |
| **SendGrid** | Medium | Medium | **Medium** | AWS SES |

**Keterangan:**
- **High Risk**: **Zapier, AWS, GCP, Slack** (memerlukan mitigasi segera).
- **Medium Risk**: **GitHub, SendGrid** (memerlukan mitigasi).
- **Low Risk**: **Sentry, Statuspage.io** (tidak kritis).

---
##### **3. Vendor Dependency Map (Peta Ketergantungan Vendor)**
**Contoh Peta Ketergantungan:**
```
MusGo-OS
│
├── **Backend**
│   ├── **Zapier** (Primary)
│   │   └── **Make.com** (Fallback)
│   ├── **AWS (EC2, RDS, S3)** (Primary)
│   │   └── **GCP (Compute Engine, Cloud SQL, Cloud Storage)** (Fallback)
│   └── **PostgreSQL** (Primary)
│       └── **Replikasi + Backup** (Fallback)
│
├── **Frontend**
│   ├── **AWS (S3, CloudFront)** (Primary)
│   │   └── **GCP (Cloud Storage, CDN)** (Fallback)
│   └── **GitHub (Pages)** (Primary)
│       └── **GitLab (Pages)** (Fallback)
│
├── **Komunikasi**
│   ├── **Slack** (Primary)
│   │   └── **Discord** (Fallback)
│   └── **SendGrid** (Primary)
│       └── **AWS SES** (Fallback)
│
└── **Monitoring**
    ├── **Sentry** (Primary)
    │   └── **LogRocket** (Fallback)
    └── **Statuspage.io** (Primary)
        └── **Upptime** (Fallback)
```

---
---
---

## **🔹 15.3 Vendor BCP Strategies (Strategi BCP untuk Vendor)**
### **📌 Penjelasan**
**Vendor BCP Strategies** adalah **strategi untuk memastikan kelangsungan bisnis** meskipun **vendor mengalami gangguan**. Strategi meliputi:
1. **Multi-Vendor**: Gunakan **2+ vendor** untuk layanan kritis.
2. **Fallback Mechanism**: Gunakan **mekanisme fallback** jika vendor down.
3. **Local Cache**: Cache data vendor **lokal** (untuk mengurangi ketergantungan).
4. **Offline Mode**: Sistem bisa berjalan **tanpa vendor** (untuk fitur non-kritis).
5. **Vendor SLA Monitoring**: Monitor **SLA vendor** dan **eskalasi jika melanggar**.

---
#### **🚀 Contoh Implementasi: Vendor BCP Strategies**
##### **1. Multi-Vendor (Zapier + Make.com)**
**Strategi:**
- **Primary**: Zapier (untuk otomatisasi).
- **Secondary**: Make.com (fallback jika Zapier down).

**Implementasi:**
- **AI Agent MusGo-OS** bisa **memanggil Zapier atau Make.com**.
- **Jika Zapier down**, AI Agent **otomatis beralih ke Make.com**.

**Contoh Kode (Python):**
```python
# File: backend/automation_client.py
import httpx
from typing import Dict, Any, Optional
from circuitbreaker import circuit

class ZapierClient:
    """Klien untuk Zapier API"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.zapier.com/v2"

    @circuit(failure_threshold=0.5, recovery_timeout=60)
    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action Zapier"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = httpx.post(
            f"{self.base_url}/actions/run",
            json={"app": app, "action": action, "data": data},
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

class MakeComClient:
    """Klien untuk Make.com API"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://hook.make.com"

    def run_scenario(self, scenario_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan scenario Make.com"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = httpx.post(
            f"{self.base_url}/{scenario_id}",
            json=data,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

class AutomationClient:
    """Klien otomatisasi dengan fallback Zapier → Make.com"""
    def __init__(self, zapier_api_key: str, make_api_key: Optional[str] = None):
        self.zapier = ZapierClient(zapier_api_key)
        self.make = MakeComClient(make_api_key) if make_api_key else None
        self.zapier_to_make_mapping = {
            ("slack", "Send Channel Message"): "MAKE_SCENARIO_SLACK_SEND_MESSAGE",
            ("google_drive", "New File in Folder"): "MAKE_SCENARIO_GOOGLE_DRIVE_NEW_FILE",
            ("trello", "Create Card"): "MAKE_SCENARIO_TRELLO_CREATE_CARD",
        }

    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action dengan fallback ke Make.com"""
        try:
            return self.zapier.run_action(app, action, data)
        except Exception as e:
            if self.make:
                scenario_id = self.zapier_to_make_mapping.get((app, action))
                if scenario_id:
                    try:
                        return self.make.run_scenario(scenario_id, data)
                    except Exception as make_error:
                        raise Exception(f"Zapier dan Make.com gagal: {e}, {make_error}")
            raise Exception(f"Zapier gagal: {e}")

# Contoh penggunaan
automation = AutomationClient(
    zapier_api_key="YOUR_ZAPIER_API_KEY",
    make_api_key="YOUR_MAKE_API_KEY"
)

# Jalankan action (dengan fallback)
try:
    result = automation.run_action(
        app="slack",
        action="Send Channel Message",
        data={"channel": "#musgo-updates", "text": "Halo!"}
    )
    print("Action berjalan:", result)
except Exception as e:
    print("Error:", e)
```

---
##### **2. Multi-Cloud (AWS + GCP)**
**Strategi:**
- **Primary**: AWS (EC2, RDS, S3).
- **Secondary**: GCP (Compute Engine, Cloud SQL, Cloud Storage).

**Implementasi:**
- **Deploy MusGo-OS di AWS dan GCP**.
- **Gunakan DNS Failover** (Route 53) untuk **alihkan traffic** jika AWS down.
- **Replikasi Database** (AWS RDS → GCP Cloud SQL).

**Contoh Arsitektur Multi-Cloud:**
```
User → Route 53 (DNS Failover)
       │
       ├── AWS (Primary)
       │   ├── EC2 (Backend)
       │   ├── RDS (PostgreSQL)
       │   └── S3 (Storage)
       │
       └── GCP (Secondary)
           ├── Compute Engine (Backend)
           ├── Cloud SQL (PostgreSQL)
           └── Cloud Storage (Storage)
```

**Contoh Setup Route 53 Failover:**
1. **Buat Health Check** untuk AWS dan GCP:
   - **AWS Health Check**: `https://musgo-os-aws.com/health`
   - **GCP Health Check**: `https://musgo-os-gcp.com/health`
2. **Buat Record Set** dengan **Failover Routing Policy**:
   - **Primary**: AWS (`musgo-os-aws.com`).
   - **Secondary**: GCP (`musgo-os-gcp.com`).
3. **Set Failover Condition**:
   - Jika **AWS Health Check gagal**, traffic **dialihkan ke GCP**.

**Contoh Terraform untuk Route 53 Failover:**
```hcl
# File: terraform/route53_failover.tf
resource "aws_route53_zone" "musgo_os" {
  name = "musgo-os.com"
}

resource "aws_route53_record" "musgo_os_primary" {
  zone_id = aws_route53_zone.musgo_os.zone_id
  name    = "musgo-os.com"
  type    = "A"

  alias {
    name                   = aws_lb.musgo_os_aws.dns_name
    zone_id                = aws_lb.musgo_os_aws.zone_id
    evaluate_target_health = true
  }

  failover_routing_policy {
    type      = "PRIMARY"
    set_identifier = "aws-primary"
  }

  health_check_id = aws_route53_health_check.musgo_os_aws.id
}

resource "aws_route53_record" "musgo_os_secondary" {
  zone_id = aws_route53_zone.musgo_os.zone_id
  name    = "musgo-os.com"
  type    = "A"

  alias {
    name                   = aws_lb.musgo_os_gcp.dns_name
    zone_id                = aws_lb.musgo_os_gcp.zone_id
    evaluate_target_health = true
  }

  failover_routing_policy {
    type      = "SECONDARY"
    set_identifier = "gcp-secondary"
  }

  health_check_id = aws_route53_health_check.musgo_os_gcp.id
}

resource "aws_route53_health_check" "musgo_os_aws" {
  fqdn              = "musgo-os-aws.com"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = 3
  measure_latency   = true
  regions           = ["us-east-1", "us-west-2", "eu-west-1"]
}

resource "aws_route53_health_check" "musgo_os_gcp" {
  fqdn              = "musgo-os-gcp.com"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = 3
  measure_latency   = true
  regions           = ["us-east-1", "us-west-2", "eu-west-1"]
}
```

---
##### **3. Fallback Mechanism (Zapier → Webhooks)**
**Strategi:**
- **Primary**: Zapier (untuk otomatisasi).
- **Fallback**: **Webhooks MusGo-OS** (jika Zapier down).

**Implementasi:**
- **Jika Zapier down**, MusGo-OS **menyimpan request ke queue** (Redis).
- **Jika Zapier pulih**, MusGo-OS **menjalankan request dari queue**.

**Contoh Kode (Python):**
```python
# File: backend/zapier_fallback.py
import httpx
import redis
import time
from typing import Dict, Any, Optional

class ZapierFallbackClient:
    """Klien Zapier dengan fallback ke queue (Redis)"""
    def __init__(self, zapier_api_key: str, redis_host: str = "redis", redis_port: int = 6379):
        self.zapier_api_key = zapier_api_key
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=0)
        self.base_url = "https://api.zapier.com/v2"

    def run_action(self, app: str, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Jalankan action Zapier (dengan fallback ke queue)"""
        try:
            headers = {
                "Authorization": f"Bearer {self.zapier_api_key}",
                "Content-Type": "application/json",
            }
            response = httpx.post(
                f"{self.base_url}/actions/run",
                json={"app": app, "action": action, "data": data},
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            # Simpan ke queue jika Zapier gagal
            self.redis.lpush(
                "zapier_failed_requests",
                {"app": app, "action": action, "data": data, "timestamp": time.time()}
            )
            raise Exception(f"Zapier gagal, request disimpan ke queue: {e}")

    def retry_failed_requests(self):
        """Coba ulang request yang gagal"""
        while True:
            request = self.redis.rpop("zapier_failed_requests")
            if not request:
                break

            try:
                result = self.run_action(request["app"], request["action"], request["data"])
                print(f"✅ Request berhasil: {request['app']}.{request['action']}")
            except Exception as e:
                # Jika masih gagal, simpan lagi ke queue (dengan delay)
                time.sleep(5)
                self.redis.lpush("zapier_failed_requests", request)
                print(f"❌ Request gagal: {request['app']}.{request['action']} - {e}")

# Contoh penggunaan
zapier_fallback = ZapierFallbackClient(zapier_api_key="YOUR_ZAPIER_API_KEY")

# Jalankan action (dengan fallback)
try:
    result = zapier_fallback.run_action(
        app="slack",
        action="Send Channel Message",
        data={"channel": "#musgo-updates", "text": "Halo!"}
    )
    print("Action berjalan:", result)
except Exception as e:
    print("Request disimpan ke queue:", e)

# Coba ulang request gagal (jalankan di background)
zapier_fallback.retry_failed_requests()
```

**Cron Job untuk Retry:**
```bash
# Edit crontab
crontab -e

# Coba ulang request gagal setiap 1 menit
* * * * * /usr/bin/python3 -c "from backend.zapier_fallback import ZapierFallbackClient; ZapierFallbackClient('YOUR_ZAPIER_API_KEY').retry_failed_requests()" >> /var/log/zapier_retry.log 2>&1
```

---
##### **4. Local Cache (Zapier Apps & Actions)**
**Strategi:**
- **Cache daftar aplikasi dan action Zapier** di **Redis**.
- **Gunakan cache** jika Zapier API **lambat atau down**.

**Implementasi:**
- **Cache daftar aplikasi** (TTL: 1 jam).
- **Cache daftar action** (TTL: 1 jam).

**Contoh Kode (Python - FastAPI + Redis Cache):**
```python
# File: backend/zapier_cache.py
from fastapi import FastAPI, HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import httpx
import redis
import time

app = FastAPI()

# Setup Redis
redis_client = redis.Redis(host="redis", port=6379, db=0)

# Setup FastAPI Cache
@app.on_event("startup")
async def startup():
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

# Cache daftar aplikasi Zapier
@cache(expire=3600)  # TTL: 1 jam
async def get_zapier_apps(api_key: str):
    """Ambil daftar aplikasi Zapier (dengan cache)"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                "https://api.zapier.com/v2/apps",
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            return response.json().get("apps", [])
        except Exception as e:
            # Jika gagal, coba ambil dari cache
            cached_apps = await FastAPICache.get(f"fastapi-cache:get_zapier_apps:{api_key}")
            if cached_apps:
                return cached_apps
            raise HTTPException(status_code=503, detail=f"Zapier API gagal: {e}")

# Cache daftar action untuk aplikasi
@cache(expire=3600)
async def get_zapier_app_actions(api_key: str, app_key: str):
    """Ambil daftar action untuk aplikasi (dengan cache)"""
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"https://api.zapier.com/v2/apps/{app_key}/actions",
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            return response.json().get("actions", [])
        except Exception as e:
            # Jika gagal, coba ambil dari cache
            cached_actions = await FastAPICache.get(f"fastapi-cache:get_zapier_app_actions:{api_key}:{app_key}")
            if cached_actions:
                return cached_actions
            raise HTTPException(status_code=503, detail=f"Zapier API gagal: {e}")

# Contoh endpoint
@app.get("/zapier/apps")
async def list_apps(api_key: str):
    try:
        apps = await get_zapier_apps(api_key)
        return {"apps": apps}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/zapier/apps/{app_key}/actions")
async def list_app_actions(api_key: str, app_key: str):
    try:
        actions = await get_zapier_app_actions(api_key, app_key)
        return {"actions": actions}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---
##### **5. Offline Mode (Fitur Non-Kritis)**
**Strategi:**
- **Fitur kritis** (AI Agent, Otomatisasi) **memerlukan vendor**.
- **Fitur non-kritis** (Dashboard, Dokumentasi) **bisa berjalan offline**.

**Implementasi:**
- **Cache data lokal** (untuk fitur non-kritis).
- **Tampilkan pesan** jika vendor down (untuk fitur kritis).

**Contoh Kode (Frontend - React):**
```tsx
// File: frontend/src/components/OfflineMode.tsx
import React, { useState, useEffect } from "react";
import { useZapierStatus } from "../hooks/useZapierStatus";

const OfflineMode: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isZapierDown } = useZapierStatus();
  const [showOfflineMode, setShowOfflineMode] = useState(false);

  useEffect(() => {
    if (isZapierDown) {
      setShowOfflineMode(true);
    } else {
      setShowOfflineMode(false);
    }
  }, [isZapierDown]);

  if (!showOfflineMode) {
    return <>{children}</>;
  }

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <div style={{
        padding: "15px",
        background: "#fff3cd",
        border: "1px solid #ffc107",
        borderRadius: "5px",
        marginBottom: "20px"
      }}>
        ⚠️ **Zapier Sedang Down**
        <br />
        Fitur otomatisasi sementara tidak tersedia.
        <br />
        Data Anda tetap aman.
      </div>
      {children}
    </div>
  );
};

// Hook untuk cek status Zapier
export const useZapierStatus = () => {
  const [isZapierDown, setIsZapierDown] = useState(false);

  useEffect(() => {
    const checkZapierStatus = async () => {
      try {
        const response = await fetch("https://api.zapier.com/v2/apps");
        if (!response.ok) {
          setIsZapierDown(true);
        } else {
          setIsZapierDown(false);
        }
      } catch (error) {
        setIsZapierDown(true);
      }
    };

    checkZapierStatus();
    const interval = setInterval(checkZapierStatus, 60000); // Cek setiap 1 menit

    return () => clearInterval(interval);
  }, []);

  return { isZapierDown };
};

// Contoh penggunaan
const AutomationPage: React.FC = () => {
  return (
    <OfflineMode>
      <div>
        <h1>Otomatisasi MusGo-OS</h1>
        <p>Buat Zap untuk mengotomatiskan workflow Anda.</p>
      </div>
    </OfflineMode>
  );
};

export default AutomationPage;
```

---
##### **6. Vendor SLA Monitoring (Pemantauan SLA Vendor)**
**Strategi:**
- **Monitor SLA vendor** (misal: uptime, latency).
- **Eskalasi ke vendor** jika SLA **dilanggar**.

**Implementasi:**
- **Gunakan Prometheus** untuk **scrape SLA vendor**.
- **Setup Alert** jika SLA **dilanggar**.

**Contoh Setup Prometheus untuk Monitor SLA Zapier:**
```yaml
# File: prometheus/zapier_sla.yml
scrape_configs:
  - job_name: "zapier_sla"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["zapier-exporter:9090"]
    scrape_interval: 5m
    scrape_timeout: 10s

# Alert Rules
rule_files:
  - "zapier_sla_rules.yml"
```

**Contoh Alert Rules (`zapier_sla_rules.yml`):**
```yaml
groups:
- name: zapier_sla_alerts
  rules:
    # Uptime < 99.9%
    - alert: ZapierUptimeBelowSLA
      expr: rate(zapier_api_up[5m]) < 0.999
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Zapier uptime di bawah SLA (99.9%)"
        description: "Zapier uptime saat ini: {{ $value }}% (SLA: 99.9%)"

    # Latency > 1 detik
    - alert: ZapierLatencyAboveSLA
      expr: zapier_api_latency_seconds > 1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Zapier latency di atas SLA (1 detik)"
        description: "Zapier latency saat ini: {{ $value }}s (SLA: 1s)"

    # Error Rate > 1%
    - alert: ZapierErrorRateAboveSLA
      expr: rate(zapier_api_errors_total[5m]) / rate(zapier_api_calls_total[5m]) > 0.01
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Zapier error rate di atas SLA (1%)"
        description: "Zapier error rate saat ini: {{ $value }}% (SLA: 1%)"
```

**Contoh Zapier Exporter (Python):**
*(Lihat [Part 10.3.3](#3-zapier-exporter-custom-exporter-untuk-zapier-api))*

---
---
---

## **🔹 15.4 Vendor BCP Procedures (Prosedur BCP untuk Vendor)**
### **📌 Penjelasan**
**Vendor BCP Procedures** adalah **prosedur detail** untuk **menangani gangguan vendor**, termasuk:
- **Deteksi gangguan vendor**.
- **Aktivasi fallback mechanism**.
- **Koordinasi dengan vendor**.
- **Pemulihan ke vendor primary**.

---
#### **🚀 Contoh Implementasi: Vendor BCP Procedures**
##### **1. Prosedur: Zapier Outage**
**Dokumen Prosedur:**
```markdown
# 📋 Prosedur: Zapier Outage (SEV-2)
**ID:** V-BCP-001
**Versi:** 1.0
**Owner:** @backend-team

---
## 📌 Deskripsi
Prosedur ini mendefinisikan **langkah-langkah** untuk **menangani gangguan Zapier** (SEV-2), termasuk **fallback ke Make.com** dan **retry mechanism**.

---
## 📌 Severity
**SEV-2 (High)**

---
## 📌 Deteksi
- **Monitoring**: Prometheus alert `ZapierAPIDown`.
- **User Report**: User melaporkan **otomatisasi terhenti**.
- **Zapier Status Page**: [status.zapier.com](https://status.zapier.com/) menunjukkan outage.

---
## 📌 Aktivasi Fallback
### Langkah 1: Verifikasi Gangguan
- [ ] Cek **Zapier Status Page** ([status.zapier.com](https://status.zapier.com/)).
- [ ] Cek **Prometheus** (`zapier_api_up`).
- [ ] Cek **Sentry** (apakah ada error terkait Zapier?).

### Langkah 2: Aktifkan Fallback ke Make.com
- [ ] **AI Agent MusGo-OS** otomatis **beralih ke Make.com** (lihat [Bagian 15.3.1](#1-multi-vendor-zapier--makecom)).
- [ ] Verifikasi **Make.com berjalan normal**:
  ```bash
  curl https://hook.make.com/MAKE_SCENARIO_SLACK_SEND_MESSAGE
  ```

### Langkah 3: Aktifkan Retry Mechanism
- [ ] **Request yang gagal** disimpan ke **Redis queue** (`zapier_failed_requests`).
- [ ] **Cron job** mencoba ulang request setiap **1 menit** (lihat [Bagian 15.3.3](#3-fallback-mechanism-zapier--webhooks)).

### Langkah 4: Update Status Page
- [ ] Update **Status Page**:
  > "⚠️ Zapier Integration Sedang Down (SEV-2)
  > Kami sedang menggunakan fallback (Make.com). Otomatisasi sementara terhenti untuk fitur tertentu."

### Langkah 5: Notifikasi Internal
- [ ] **Slack (`#crisis-war-room`)**:
  > "@here Zapier down (SEV-2). Fallback ke Make.com sudah diaktifkan. Estimasi pemulihan: 1 jam."

### Langkah 6: Notifikasi Eksternal
- [ ] **Email ke User Premium/Enterprise**:
  > "Halo [Nama User],
  > Kami ingin memberitahu bahwa **Zapier sedang mengalami gangguan (SEV-2)**.
  > Otomatisasi MusGo-OS sementara **berjalan dengan fallback (Make.com)**.
  > Estimasi pemulihan: < 1 jam.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Pemulihan
### Langkah 1: Monitor Zapier Status
- [ ] Pantau **Zapier Status Page** ([status.zapier.com](https://status.zapier.com/)).
- [ ] Pantau **Prometheus** (`zapier_api_up`).

### Langkah 2: Coba Kembali ke Zapier
- [ ] Jika Zapier **sudah pulih**, **AI Agent MusGo-OS** otomatis **kembali ke Zapier**.
- [ ] Verifikasi **Zapier berjalan normal**:
  ```bash
  curl https://api.zapier.com/v2/apps
  ```

### Langkah 3: Retry Failed Requests
- [ ] **Cron job** mencoba ulang **request yang gagal** (lihat [Bagian 15.3.3](#3-fallback-mechanism-zapier--webhooks)).

### Langkah 4: Update Status Page
- [ ] Update **Status Page**:
  > "✅ Zapier Integration Kembali Normal
  > Semua otomatisasi kini berjalan dengan Zapier."

### Langkah 5: Notifikasi Internal
- [ ] **Slack (`#crisis-war-room`)**:
  > "@here Zapier sudah pulih. Fallback dinonaktifkan."

### Langkah 6: Notifikasi Eksternal
- [ ] **Email ke User Premium/Enterprise**:
  > "Halo [Nama User],
  > Zapier Integration di MusGo-OS **kembali normal**.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Post-Mortem
- [ ] **Root Cause**: Apa penyebab Zapier down?
- [ ] **Fallback Effectiveness**: Apakah fallback ke Make.com berjalan dengan baik?
- [ ] **Action Items**:
  - [ ] Review **SLA Zapier** dan **kontrak**.
  - [ ] Setup **multi-vendor** untuk otomatisasi (Zapier + Make.com + n8n).
  - [ ] Lakukan **testing fallback** secara berkala.

---
## 📌 Kontak
| Peran | Nama | Kontak |
|-------|------|--------|
| **Incident Commander** | Dhani Yuliawan | @dhani, +62 813-6552-283 |
| **Backend Team** | @backend-team | Slack |
| **DevOps Team** | @devops-team | Slack |
| **Zapier Support** | - | support@zapier.com |
| **Make.com Support** | - | support@make.com |
```

---
##### **2. Prosedur: AWS Outage**
**Dokumen Prosedur:**
```markdown
# 📋 Prosedur: AWS Outage (SEV-1)
**ID:** V-BCP-002
**Versi:** 1.0
**Owner:** @devops-team

---
## 📌 Deskripsi
Prosedur ini mendefinisikan **langkah-langkah** untuk **menangani gangguan AWS** (SEV-1), termasuk **failover ke GCP**.

---
## 📌 Severity
**SEV-1 (Critical)**

---
## 📌 Deteksi
- **Monitoring**: Prometheus alert `AWSOutage`.
- **User Report**: User melaporkan **sistem down**.
- **AWS Status Page**: [status.aws.amazon.com](https://status.aws.amazon.com/) menunjukkan outage.

---
## 📌 Aktivasi Failover
### Langkah 1: Verifikasi Gangguan
- [ ] Cek **AWS Status Page** ([status.aws.amazon.com](https://status.aws.amazon.com/)).
- [ ] Cek **Prometheus** (`aws_ec2_up`, `aws_rds_up`).
- [ ] Cek **Sentry** (apakah ada error terkait AWS?).

### Langkah 2: Failover ke GCP
- [ ] **Route 53** otomatis **alihkan traffic** ke GCP (lihat [Bagian 15.3.2](#2-multi-cloud-aws--gcp)).
- [ ] Verifikasi **GCP berjalan normal**:
  ```bash
  curl https://musgo-os-gcp.com/health
  ```

### Langkah 3: Promosikan Database GCP
- [ ] **Cloud SQL (GCP)** dipromosikan ke **Primary**:
  ```bash
  gcloud sql instances promote-replica musgo-os-gcp --master-instance-name=musgo-os-aws
  ```

### Langkah 4: Update Status Page
- [ ] Update **Status Page**:
  > "🚨 AWS Outage (SEV-1)
  > Kami sedang failover ke GCP. Estimasi pemulihan: < 1 jam."

### Langkah 5: Notifikasi Internal
- [ ] **Slack (`#crisis-war-room`)**:
  > "@here AWS down (SEV-1). Failover ke GCP sedang berlangsung. Estimasi pemulihan: 1 jam."

### Langkah 6: Notifikasi Eksternal
- [ ] **Email ke Semua User**:
  > "Halo [Nama User],
  > Kami ingin memberitahu bahwa **AWS sedang mengalami gangguan (SEV-1)**.
  > MusGo-OS sedang **failover ke GCP**.
  > Estimasi pemulihan: < 1 jam.
  > Data Anda tetap aman.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Pemulihan
### Langkah 1: Monitor AWS Status
- [ ] Pantau **AWS Status Page** ([status.aws.amazon.com](https://status.aws.amazon.com/)).
- [ ] Pantau **Prometheus** (`aws_ec2_up`, `aws_rds_up`).

### Langkah 2: Failback ke AWS
- [ ] Jika AWS **sudah pulih**, **Route 53** otomatis **alihkan traffic kembali ke AWS**.
- [ ] Verifikasi **AWS berjalan normal**:
  ```bash
  curl https://musgo-os-aws.com/health
  ```

### Langkah 3: Replikasi Balik Database
- [ ] **RDS (AWS)** direplikasi kembali dari **Cloud SQL (GCP)**.

### Langkah 4: Update Status Page
- [ ] Update **Status Page**:
  > "✅ AWS Outage Teratasi
  > MusGo-OS kembali berjalan di AWS."

### Langkah 5: Notifikasi Internal
- [ ] **Slack (`#crisis-war-room`)**:
  > "@here AWS sudah pulih. Failback ke AWS selesai."

### Langkah 6: Notifikasi Eksternal
- [ ] **Email ke Semua User**:
  > "Halo [Nama User],
  > Gangguan AWS di MusGo-OS **telah teratasi**.
  > Semua layanan kini berjalan normal di AWS.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Post-Mortem
- [ ] **Root Cause**: Apa penyebab AWS outage?
- [ ] **Failover Effectiveness**: Apakah failover ke GCP berjalan dengan baik?
- [ ] **Action Items**:
  - [ ] Review **SLA AWS** dan **kontrak**.
  - [ ] Setup **multi-region** untuk AWS (us-east-1 + us-west-2).
  - [ ] Lakukan **testing failover** secara berkala.

---
## 📌 Kontak
| Peran | Nama | Kontak |
|-------|------|--------|
| **Incident Commander** | Dhani Yuliawan | @dhani, +62 813-6552-283 |
| **DevOps Team** | @devops-team | Slack |
| **AWS Support** | - | AWS Support Center |
| **GCP Support** | - | GCP Support Center |
```

---
##### **3. Prosedur: Slack Outage**
**Dokumen Prosedur:**
```markdown
# 📋 Prosedur: Slack Outage (SEV-2)
**ID:** V-BCP-003
**Versi:** 1.0
**Owner:** @comms-team

---
## 📌 Deskripsi
Prosedur ini mendefinisikan **langkah-langkah** untuk **menangani gangguan Slack** (SEV-2), termasuk **fallback ke Discord/Email**.

---
## 📌 Severity
**SEV-2 (High)**

---
## 📌 Deteksi
- **Monitoring**: Prometheus alert `SlackAPIDown`.
- **User Report**: User melaporkan **tidak bisa terhubung ke Slack**.
- **Slack Status Page**: [status.slack.com](https://status.slack.com/) menunjukkan outage.

---
## 📌 Aktivasi Fallback
### Langkah 1: Verifikasi Gangguan
- [ ] Cek **Slack Status Page** ([status.slack.com](https://status.slack.com/)).
- [ ] Cek **Prometheus** (`slack_api_up`).
- [ ] Cek **Sentry** (apakah ada error terkait Slack?).

### Langkah 2: Fallback ke Discord
- [ ] **Tim MusGo-OS** beralih ke **Discord** untuk koordinasi internal.
- [ ] Verifikasi **Discord berjalan normal**:
  ```bash
  curl https://discord.com/api/v10/users/@me
  ```

### Langkah 3: Fallback ke Email
- [ ] **Notifikasi internal** dikirim via **Email** (`crisis@musgo-os.com`).
- [ ] **Notifikasi eksternal** dikirim via **Email** (untuk user).

### Langkah 4: Update Status Page
- [ ] Update **Status Page**:
  > "⚠️ Slack Integration Sedang Down (SEV-2)
  > Kami sedang menggunakan fallback (Discord/Email). Komunikasi internal sementara terganggu."

### Langkah 5: Notifikasi Internal
- [ ] **Email ke Semua Karyawan**:
  > "Halo Tim,
  > Slack sedang down (SEV-2).
  > Silakan gunakan **Discord** untuk koordinasi internal.
  > Link: [discord.gg/musgo-os](https://discord.gg/musgo-os)
  > Terima kasih."

### Langkah 6: Notifikasi Eksternal
- [ ] **Email ke User Premium/Enterprise**:
  > "Halo [Nama User],
  > Kami ingin memberitahu bahwa **Slack sedang mengalami gangguan (SEV-2)**.
  > Komunikasi dengan tim MusGo-OS sementara **berjalan via Email**.
  > Estimasi pemulihan: < 1 jam.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Pemulihan
### Langkah 1: Monitor Slack Status
- [ ] Pantau **Slack Status Page** ([status.slack.com](https://status.slack.com/)).
- [ ] Pantau **Prometheus** (`slack_api_up`).

### Langkah 2: Kembali ke Slack
- [ ] Jika Slack **sudah pulih**, **tim MusGo-OS** beralih kembali ke Slack.
- [ ] Verifikasi **Slack berjalan normal**:
  ```bash
  curl https://slack.com/api/api.test
  ```

### Langkah 3: Update Status Page
- [ ] Update **Status Page**:
  > "✅ Slack Integration Kembali Normal
  > Komunikasi internal kini berjalan via Slack."

### Langkah 4: Notifikasi Internal
- [ ] **Email ke Semua Karyawan**:
  > "Halo Tim,
  > Slack sudah pulih.
  > Silakan kembali menggunakan Slack untuk koordinasi internal.
  > Terima kasih."

### Langkah 5: Notifikasi Eksternal
- [ ] **Email ke User Premium/Enterprise**:
  > "Halo [Nama User],
  > Slack Integration di MusGo-OS **kembali normal**.
  > Terima kasih atas kesabaran Anda."

---
## 📌 Post-Mortem
- [ ] **Root Cause**: Apa penyebab Slack outage?
- [ ] **Fallback Effectiveness**: Apakah fallback ke Discord/Email berjalan dengan baik?
- [ ] **Action Items**:
  - [ ] Review **SLA Slack** dan **kontrak**.
  - [ ] Setup **multi-channel** untuk komunikasi internal (Slack + Discord + Email).
  - [ ] Lakukan **testing fallback** secara berkala.

---
## 📌 Kontak
| Peran | Nama | Kontak |
|-------|------|--------|
| **Incident Commander** | Dhani Yuliawan | @dhani, +62 813-6552-283 |
| **Comms Team** | @comms-team | Slack, Email |
| **Slack Support** | - | support@slack.com |
| **Discord Support** | - | support@discord.com |
```

---
---
---

## **🔹 15.5 Vendor BCP Testing (Testing BCP Vendor)**
### **📌 Penjelasan**
**Vendor BCP Testing** adalah **proses menguji** apakah **fallback mechanism** berfungsi dengan baik jika **vendor down**.

**Jenis Testing:**
| Jenis Testing | Deskripsi | Frekuensi | Peserta |
|---------------|-----------|-----------|---------|
| **Tabletop Exercise** | Diskusi teoritis (tanpa eksekusi) | 6 bulan | BCP Committee |
| **Walkthrough Test** | Simulasi langkah-langkah | 3 bulan | Tim Teknis |
| **Simulation Test** | Uji coba fallback (tanpa mematikan vendor) | 1 bulan | Tim Teknis |
| **Full Interruption Test** | Matikan vendor (jika memungkinkan) | 1 tahun | Tim Teknis + Vendor |

---
#### **🚀 Contoh Implementasi: Vendor BCP Testing**
##### **1. Tabletop Exercise (Diskusi)**
**Contoh Skenario:**
> *"Zapier mengalami outage. Bagaimana MusGo-OS menanganinya?"*

**Langkah-Langkah:**
1. **Incident Commander** (Dhani) memimpin diskusi.
2. **Backend Team** menjelaskan **fallback ke Make.com**.
3. **DevOps Team** menjelaskan **retry mechanism**.
4. **Comms Team** menjelaskan **komunikasi ke user**.
5. **Support Team** menjelaskan **template balasan**.

**Output:**
- **Dokumentasi** langkah-langkah yang diperlukan.
- **Identifikasi celah** (misal: tidak ada template balasan untuk user).

---
##### **2. Walkthrough Test (Simulasi)**
**Contoh Skenario:**
> *"Simulasikan Zapier down dan uji fallback ke Make.com."*

**Langkah-Langkah:**
1. **Backup data terlebih dahulu** (untuk safety).
2. **Matikan akses ke Zapier** (simulasikan outage).
3. **Verifikasi fallback ke Make.com**:
   - AI Agent **beralih ke Make.com**.
   - Request **disimpan ke queue** (Redis).
4. **Coba ulang request dari queue**.
5. **Hidupkan kembali Zapier** dan verifikasi **kembali ke Zapier**.

**Contoh Checklist Walkthrough Test:**
```markdown
# ✅ Checklist: Walkthrough Test - Zapier Outage
**Tanggal:** 20 Mei 2026
**Pemimpin Test:** @backend-team
**Peserta:** @backend-team, @devops-team, @comms-team

---
## 📌 Persiapan
- [ ] Backup data (PostgreSQL, Redis).
- [ ] Informasikan tim bahwa test akan dilakukan.

---
## 📌 Langkah-Langkah
### 1. Matikan Akses ke Zapier
- [ ] Blokir akses ke `api.zapier.com` (via firewall).
- [ ] Catat waktu: [Waktu]

### 2. Verifikasi Fallback ke Make.com
- [ ] Cek apakah AI Agent **beralih ke Make.com**:
  ```bash
  curl http://musgo-os-backend:8000/api/automation/status
  ```
- [ ] Verifikasi **Make.com berjalan normal**:
  ```bash
  curl https://hook.make.com/MAKE_SCENARIO_SLACK_SEND_MESSAGE
  ```

### 3. Verifikasi Retry Mechanism
- [ ] Cek apakah request gagal **disimpan ke queue**:
  ```bash
  redis-cli LLEN zapier_failed_requests
  ```
- [ ] Coba ulang request dari queue:
  ```bash
  python3 /path/to/scripts/retry_zapier_requests.py
  ```

### 4. Hidupkan Kembali Zapier
- [ ] Buka akses ke `api.zapier.com`.
- [ ] Catat waktu: [Waktu]

### 5. Verifikasi Kembali ke Zapier
- [ ] Cek apakah AI Agent **kembali ke Zapier**:
  ```bash
  curl http://musgo-os-backend:8000/api/automation/status
  ```

---
## 📌 Hasil Test
| Metrik | Target | Hasil | Status |
|--------|--------|-------|--------|
| **Fallback ke Make.com** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Retry Mechanism** | < 5 menit | [Hasil] | ✅ / ❌ |
| **Kembali ke Zapier** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Data Konsistensi** | 100% | [Hasil] | ✅ / ❌ |

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Review template balasan untuk user | @comms-team | 2026-05-22 | ⬜ To Do |
| Setup monitoring untuk Make.com | @devops-team | 2026-05-22 | ⬜ To Do |
| Lakukan load testing untuk Make.com | @backend-team | 2026-05-25 | ⬜ To Do |
```

---
##### **3. Simulation Test (Uji Coba)**
**Contoh Skenario:**
> *"Simulasikan AWS outage dan uji failover ke GCP."*

**Langkah-Langkah:**
1. **Backup data terlebih dahulu** (PostgreSQL, Redis, Etcd).
2. **Matikan AWS Region us-east-1** (simulasikan outage).
3. **Verifikasi failover ke GCP**:
   - Route 53 **alihkan traffic** ke GCP.
   - Database GCP **dipromosikan ke Primary**.
4. **Verifikasi MusGo-OS berjalan di GCP**.
5. **Hidupkan kembali AWS** dan verifikasi **failback**.

**Contoh Skrip Simulation Test:**
```bash
# File: scripts/simulation_test_aws_outage.sh
#!/bin/bash

# Konfigurasi
AWS_REGION="us-east-1"
GCP_REGION="us-central1"
BACKUP_DIR="/tmp/aws_outage_test_$(date +%Y%m%d_%H%M%S)"
S3_BUCKET="musgo-os-backups"
S3_PREFIX="aws_outage_test"

# 1. Backup data
echo "📦 Backing up data..."
mkdir -p $BACKUP_DIR

# Backup PostgreSQL (jika diperlukan)
# pg_dump -h postgres -U postgres -d musgo_os -F c -f $BACKUP_DIR/postgres.dump

# Backup Redis (jika diperlukan)
# redis-cli SAVE

# 2. Simulasikan AWS Outage
echo "⚠️  Simulating AWS $AWS_REGION outage..."
# Matikan instance AWS (hanya untuk testing!)
# aws ec2 stop-instances --instance-ids i-1234567890 --region $AWS_REGION

# Atau: Matikan service (lebih aman)
# kubectl --context=aws scale deployment --replicas=0 -n musgo-os --all

# 3. Monitor Failover ke GCP
echo "🔄 Monitoring failover to GCP..."
START_TIME=$(date +%s)
while true; do
    # Cek apakah traffic sudah dialihkan ke GCP
    HEALTH_STATUS=$(curl -s https://musgo-os-gcp.com/health | grep -o '"status":"healthy"')
    if [ -n "$HEALTH_STATUS" ]; then
        END_TIME=$(date +%s)
        FAILOVER_TIME=$((END_TIME - START_TIME))
        echo "✅ Failover to GCP completed in $FAILOVER_TIME seconds"
        break
    fi
    sleep 5
done

# 4. Verifikasi MusGo-OS di GCP
echo "🔍 Checking MusGo-OS in GCP..."
kubectl --context=gcp get pods -n musgo-os
kubectl --context=gcp get svc -n musgo-os

# 5. Hidupkan Kembali AWS
echo "🔄 Restarting AWS..."
# aws ec2 start-instances --instance-ids i-1234567890 --region $AWS_REGION
# kubectl --context=aws scale deployment --replicas=1 -n musgo-os --all

# 6. Verifikasi Failback ke AWS
echo "🔄 Checking failback to AWS..."
sleep 60  # Tunggu failback
kubectl --context=aws get pods -n musgo-os

echo "✅ Simulation Test completed successfully!"
```

**Cara Jalankan:**
```bash
chmod +x /path/to/scripts/simulation_test_aws_outage.sh
/path/to/scripts/simulation_test_aws_outage.sh
```

---
##### **4. Full Interruption Test (Uji Penuh)**
**Contoh Skenario:**
> *"Matikan Zapier dan uji fallback ke Make.com + Retry Mechanism."*

**Langkah-Langkah:**
1. **Backup data terlebih dahulu**.
2. **Matikan Zapier** (simulasikan outage).
3. **Verifikasi fallback ke Make.com**.
4. **Verifikasi retry mechanism**.
5. **Hidupkan kembali Zapier** dan verifikasi **kembali ke Zapier**.
6. **Lakukan Post-Mortem**.

**Catatan:**
- **Hanya dilakukan di staging** (tidak di production).
- **Lakukan di luar jam kerja**.
- **Libatkan vendor** (Zapier, Make.com) jika diperlukan.

**Contoh Checklist Full Interruption Test:**
```markdown
# ✅ Checklist: Full Interruption Test - Zapier Outage
**Tanggal:** 20 Mei 2026
**Pemimpin Test:** @backend-team
**Peserta:** @backend-team, @devops-team, @comms-team, @support-team

---
## 📌 Persiapan
- [ ] Backup data (PostgreSQL, Redis).
- [ ] Informasikan user bahwa test akan dilakukan (via Status Page).
- [ ] Siapkan Make.com (fallback).
- [ ] Siapkan Redis queue (untuk retry).

---
## 📌 Langkah-Langkah
### 1. Matikan Zapier
- [ ] Blokir akses ke `api.zapier.com` (via firewall).
- [ ] Catat waktu: [Waktu]

### 2. Verifikasi Fallback ke Make.com
- [ ] Cek apakah AI Agent **beralih ke Make.com**:
  ```bash
  curl http://musgo-os-backend:8000/api/automation/status
  ```
- [ ] Verifikasi **Make.com berjalan normal**.

### 3. Verifikasi Retry Mechanism
- [ ] Cek apakah request gagal **disimpan ke queue**:
  ```bash
  redis-cli LLEN zapier_failed_requests
  ```
- [ ] Coba ulang request dari queue:
  ```bash
  python3 /path/to/scripts/retry_zapier_requests.py
  ```

### 4. Simulasikan Operasional
- [ ] User mencoba **membuat Zap** (harus gagal, tetapi disimpan ke queue).
- [ ] User mencoba **menjalankan AI Agent** (harus berjalan dengan Make.com).

### 5. Hidupkan Kembali Zapier
- [ ] Buka akses ke `api.zapier.com`.
- [ ] Catat waktu: [Waktu]

### 6. Verifikasi Kembali ke Zapier
- [ ] Cek apakah AI Agent **kembali ke Zapier**.
- [ ] Verifikasi **request dari queue diproses**.

### 7. Verifikasi Data Konsistensi
- [ ] Cek apakah **data otomatisasi** konsisten.

---
## 📌 Hasil Test
| Metrik | Target | Hasil | Status |
|--------|--------|-------|--------|
| **Fallback ke Make.com** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Retry Mechanism** | < 5 menit | [Hasil] | ✅ / ❌ |
| **Kembali ke Zapier** | < 1 menit | [Hasil] | ✅ / ❌ |
| **Data Konsistensi** | 100% | [Hasil] | ✅ / ❌ |
| **Downtime** | < 1 jam | [Hasil] | ✅ / ❌ |

---
## 📌 Catatan
- [Catatan 1]
- [Catatan 2]

---
## 📌 Action Items
| Action Item | Owner | Deadline | Status |
|-------------|-------|----------|--------|
| Review SLA Zapier | @backend-team | 2026-05-22 | ⬜ To Do |
| Setup multi-vendor untuk otomatisasi | @backend-team | 2026-05-25 | ⬜ To Do |
| Lakukan load testing untuk Make.com | @backend-team | 2026-05-25 | ⬜ To Do |
```

---
---
---

## **🔹 15.6 Vendor BCP Documentation (Dokumentasi BCP Vendor)**
### **📌 Penjelasan**
**Vendor BCP Documentation** adalah **dokumen yang berisi**:
- **Daftar vendor & mitra**.
- **Strategi BCP untuk setiap vendor**.
- **Prosedur BCP untuk setiap vendor**.
- **Kontak vendor**.
- **Hasil testing BCP**.

---
#### **🚀 Contoh Implementasi: Vendor BCP Documentation**
##### **1. Vendor BCP Plan (Rencana BCP Vendor)**
```markdown
# 📜 MusGo-OS 2in1: Vendor & Partner BCP Plan
**Versi:** 1.0
**Tanggal:** 19 Mei 2026
**Owner:** Dhani Yuliawan (CTO)

---
## 📌 1. Tujuan
Dokumen ini mendefinisikan **rencana Business Continuity Plan (BCP)** untuk **vendor dan mitra MusGo-OS**, termasuk:
- Daftar vendor & mitra kritis.
- Strategi BCP untuk setiap vendor.
- Prosedur BCP untuk setiap vendor.
- Kontak vendor.
- Hasil testing BCP.

---
## 📌 2. Ruang Lingkup
Dokumen ini berlaku untuk:
- **Semua vendor & mitra** yang kritis untuk MusGo-OS.
- **Semua tim MusGo-OS** yang terlibat dalam operasional.

---
## 📌 3. Daftar Vendor & Mitra Kritis
| ID | Vendor/Partner | Kategori | Layanan | Severity | Mitigasi | Status |
|----|----------------|----------|---------|----------|----------|--------|
| V-001 | Zapier | Automation | Zapier API, MCP | SEV-2 | Make.com | ✅ Aktif |
| V-002 | Make.com | Automation | Make.com API | SEV-2 | Zapier | ⚠️ Standby |
| V-003 | AWS | Cloud | EC2, RDS, S3 | SEV-1 | GCP | ✅ Aktif |
| V-004 | GCP | Cloud | Compute Engine, Cloud SQL | SEV-1 | AWS | ⚠️ Standby |
| V-005 | Slack | Communication | Slack API | SEV-2 | Discord, Email | ✅ Aktif |
| V-006 | Discord | Communication | Discord API | SEV-2 | Slack, Email | ⚠️ Standby |
| V-007 | GitHub | Version Control | GitHub API | SEV-2 | GitLab | ✅ Aktif |
| V-008 | GitLab | Version Control | GitLab API | SEV-2 | GitHub | ⚠️ Standby |

---
## 📌 4. Strategi BCP untuk Setiap Vendor
### 4.1 Zapier (V-001)
- **Strategi**: Multi-Vendor (Zapier + Make.com).
- **Fallback**: Make.com.
- **Retry Mechanism**: Simpan request ke queue (Redis) dan coba ulang.
- **Local Cache**: Cache daftar aplikasi dan action Zapier.

### 4.2 AWS (V-003)
- **Strategi**: Multi-Cloud (AWS + GCP).
- **Fallback**: GCP.
- **Failover**: Route 53 (DNS Failover).
- **Replikasi**: PostgreSQL (RDS → Cloud SQL).

### 4.3 Slack (V-005)
- **Strategi**: Multi-Channel (Slack + Discord + Email).
- **Fallback**: Discord (internal), Email (eksternal).
- **Komunikasi**: Update Status Page.

---
## 📌 5. Prosedur BCP untuk Setiap Vendor
| Vendor | Prosedur | Link |
|--------|-----------|------|
| Zapier | [V-BCP-001: Zapier Outage](#) | [Link](#1-prosedur-zapier-outage) |
| AWS | [V-BCP-002: AWS Outage](#) | [Link](#2-prosedur-aws-outage) |
| Slack | [V-BCP-003: Slack Outage](#) | [Link](#3-prosedur-slack-outage) |
| GitHub | [V-BCP-004: GitHub Outage](#) | [Link](#) |
| Make.com | [V-BCP-005: Make.com Outage](#) | [Link](#) |

---
## 📌 6. Kontak Vendor
| Vendor | Kontak | Email | Telepon | Slack | Status |
|--------|--------|-------|---------|-------|--------|
| Zapier | Zapier Support | support@zapier.com | - | - | ✅ Aktif |
| Make.com | Make.com Support | support@make.com | - | - | ✅ Aktif |
| AWS | AWS Support | - | - | - | ✅ Aktif |
| GCP | GCP Support | - | - | - | ✅ Aktif |
| Slack | Slack Support | support@slack.com | - | - | ✅ Aktif |
| Discord | Discord Support | support@discord.com | - | - | ✅ Aktif |
| GitHub | GitHub Support | support@github.com | - | - | ✅ Aktif |
| GitLab | GitLab Support | support@gitlab.com | - | - | ✅ Aktif |

---
## 📌 7. Hasil Testing BCP
| Vendor | Jenis Testing | Tanggal | Hasil | Catatan |
|--------|---------------|---------|-------|---------|
| Zapier | Tabletop Exercise | 2026-05-19 | ✅ Success | Temukan celah: Tidak ada template balasan |
| Zapier | Walkthrough Test | 2026-05-20 | ✅ Success | Fallback ke Make.com berjalan dengan baik |
| AWS | Simulation Test | 2026-05-20 | ✅ Success | Failover ke GCP berjalan dengan baik |
| Slack | Tabletop Exercise | 2026-05-19 | ✅ Success | Temukan celah: Tidak semua tim punya akses Discord |

---
## 📌 8. Action Items
| Action Item | Owner | Deadline | Status | Prioritas |
|-------------|-------|----------|--------|-----------|
| Review SLA Zapier | @backend-team | 2026-05-22 | ⬜ To Do | High |
| Setup multi-vendor untuk otomatisasi | @backend-team | 2026-05-25 | ⬜ To Do | High |
| Setup multi-cloud untuk AWS | @devops-team | 2026-05-25 | ⬜ To Do | High |
| Buat template balasan untuk user | @comms-team | 2026-05-22 | ⬜ To Do | Medium |
| Setup Discord untuk tim | @comms-team | 2026-05-22 | ⬜ To Do | Medium |

---
## 📌 9. Review & Update
- **Review**: Setiap **6 bulan** atau setelah **insiden vendor**.
- **Update**: Jika ada **perubahan vendor** (misal: kontrak, SLA).
- **Testing**: Setiap **3 bulan** (Walkthrough Test) dan **1 tahun** (Full Test).

---
## 📌 10. Lampiran
- [Vendor & Partner Inventory](#1-daftar-vendor--partner)
- [Vendor Risk Assessment](#2-vendor-risk-assessment-penilaian-risiko-vendor)
- [Vendor Dependency Map](#3-vendor-dependency-map-peta-ketergantungan-vendor)
- [Prosedur BCP untuk Setiap Vendor](#5-prosedur-bcp-untuk-setiap-vendor)
- [Hasil Testing BCP](#7-hasil-testing-bcp)
```

---
---
---
# **📌 PART 15: RINGKASAN & ACTIONABLE ITEMS UNTUK MUSGO-OS**
---

## **🔥 Kesimpulan Part 15 (Vendor & Partner BCP)**
| Kategori | Fitur | Manfaat untuk MusGo-OS | Status Implementasi |
|----------|-------|------------------------|----------------------|
| **Vendor Inventory** | Daftar vendor & mitra kritis | Identifikasi ketergantungan | ✅ **Dokumentasi tersedia** |
| **Vendor Risk Assessment** | Penilaian risiko vendor | Prioritaskan mitigasi | ✅ **Dokumentasi tersedia** |
| **Multi-Vendor** | Zapier + Make.com, AWS + GCP | Redundansi | ✅ **Contoh kode tersedia** |
| **Fallback Mechanism** | Retry queue, local cache | Minimalkan dampak | ✅ **Contoh kode tersedia** |
| **Multi-Cloud** | AWS + GCP | High availability | ✅ **Contoh Terraform tersedia** |
| **Vendor BCP Procedures** | Prosedur untuk setiap vendor | Panduan jelas | ✅ **Dokumentasi tersedia** |
| **Vendor BCP Testing** | Tabletop, Walkthrough, Simulation | Verifikasi BCP | ✅ **Contoh skrip tersedia** |
| **Vendor BCP Documentation** | Rencana BCP vendor | Dokumentasi lengkap | ✅ **Dokumentasi tersedia** |

---

## **🛠️ Langkah Selanjutnya untuk MusGo-OS**
### **1. Short-Term (1-2 Minggu)**
- [ ] **Lengkapi Vendor Inventory** (daftar semua vendor & mitra kritis).
- [ ] **Lakukan Vendor Risk Assessment** (identifikasi risiko untuk setiap vendor).
- [ ] **Setup Multi-Vendor** (Zapier + Make.com, AWS + GCP).
- [ ] **Setup Fallback Mechanism** (retry queue, local cache).
- [ ] **Buat Vendor BCP Procedures** (prosedur untuk setiap vendor).

### **2. Mid-Term (1 Bulan)**
- [ ] **Lakukan Vendor BCP Testing** (Tabletop Exercise, Walkthrough Test).
- [ ] **Setup Multi-Cloud** (AWS + GCP).
- [ ] **Setup Monitoring untuk Vendor SLA** (Prometheus + Alertmanager).
- [ ] **Train Tim** (pelatihan BCP vendor).
- [ ] **Review Kontrak Vendor** (SLA, kompensasi, dll.).

### **3. Long-Term (3+ Bulan)**
- [ ] **Lakukan Full Interruption Test** (uji penuh di staging).
- [ ] **Setup Vendor SLA Dashboard** (Grafana).
- [ ] **Automasi Vendor BCP** (otomatis failover, retry, dll.).
- [ ] **Review & Update Vendor BCP** (setiap 6 bulan).

---
---
### **❓ Pertanyaan untuk Dhani**
1. **Apakah Anda ingin saya melanjutkan ke:**
   - [ ] **Part 16: Compliance & Audit** (Untuk kepatuhan regulasi)
   - [ ] **Part 17: Vendor Contract Review** (Untuk review kontrak vendor)
   - [ ] **Part 18: Cost Optimization for BCP** (Untuk optimasi biaya BCP)
   - [ ] **Contoh Implementasi Lebih Detail** (Misal: Full setup Multi-Cloud)

2. **Apakah Anda ingin saya memberikan:**
   - [ ] **Full Vendor BCP Documentation untuk MusGo-OS**?
   - [ ] **Template Kontrak Vendor (SLA, Kompensasi, dll.)**?
   - [ ] **Setup Lengkap Multi-Cloud (AWS + GCP)**?
   - [ ] **Skrip Otomatisasi Vendor BCP Testing**?

3. **Apakah ada vendor spesifik yang ingin diimplementasikan terlebih dahulu?**
   - Contoh: **Zapier**, **AWS**, **Slack**, dll.

---
===========🔐™️®️©️🔐===========

---

