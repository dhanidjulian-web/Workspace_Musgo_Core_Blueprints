https://docs.n8n.io/
---

**✅ Kategori 1: Selamat Datang di Dokumentasi n8n**

### Selamat Datang di Dokumentasi n8n

Ini adalah dokumentasi resmi untuk **n8n**, sebuah tool otomatisasi workflow berlisensi fair-code yang menggabungkan kemampuan **AI** dengan otomatisasi proses bisnis.

n8n memungkinkan kamu menghubungkan berbagai aplikasi yang memiliki API satu sama lain, serta memanipulasi data dengan sedikit atau tanpa coding sama sekali.

**Kelebihan Utama n8n:**
- **Sangat customizable** — Workflow yang fleksibel dan bisa membuat node kustom sendiri.
- **Mudah digunakan** — Bisa diinstal lewat npm, Docker, atau pakai layanan Cloud.
- **Fokus pada privasi** — Bisa di-self-host untuk keamanan dan privasi data yang lebih baik.

---

**Kategori 2: Cara Memulai (Where to Start)**

### Cara Memulai dengan n8n

**Quickstarts (Panduan Cepat)**
- Langsung coba n8n dengan tutorial cepat: [Try it out](https://docs.n8n.io/try-it-out/)

**Pilih Versi n8n yang Tepat untuk Kamu**
- n8n Cloud, instalasi npm, Docker, atau self-host.
- Lihat perbandingan lengkap di halaman [Choose n8n](https://docs.n8n.io/choose-n8n/)

**Jelajahi Integrasi**
- n8n punya banyak integrasi (node) siap pakai. Lihat daftar lengkap di [Integrations](https://docs.n8n.io/integrations/)

**Bangun Fitur AI**
- n8n sangat mendukung pembuatan workflow berbasis AI. Mulai dari [Advanced AI](https://docs.n8n.io/advanced-ai/)

---

Sayang, ini aku kirim bertahap ya. Sudah selesai 2 kategori dulu. Mau lanjut ke kategori berikutnya (misalnya: Try it Out, Integrations, atau Core Concepts)? Atau ada kategori spesifik yang kamu mau aku kerjakan duluan?

---
End Of Part
===========🔐™️®️©️🔐===========

---

**✅ Kategori 3: Try It Out (Coba Sekarang)**

### Coba n8n Sekarang

Cara terbaik untuk memahami n8n adalah dengan langsung mencoba tutorial-tutorinya. Kamu akan cepat familiar dengan antarmuka pengguna dan berbagai jenis node serta integrasi yang tersedia.

**Tutorial yang Direkomendasikan:**
- **Pengantar Cepat**: Ikuti tutorial ["First Workflow"](https://docs.n8n.io/tutorial-first-workflow/) untuk membuat workflow pertama kamu.
- **Fitur AI**: Pelajari cara membangun [AI Chat Agent dengan n8n](../advanced-ai/intro-tutorial/).
- **Belajar Lebih Dalam**: Jika suka contoh lengkap, coba kursus resmi di [learn.n8n.io](https://learn.n8n.io).

---

**✅ Kategori 4: Pilih Versi n8n yang Tepat (Choose Your n8n)**

### Pilih n8n yang Cocok untuk Kamu

n8n menyediakan dua opsi utama:

- **n8n Cloud**: Solusi hosting terkelola sepenuhnya, tidak perlu instalasi.
- **Self-hosted**: Instal sendiri di infrastruktur kamu menggunakan npm, Docker, atau server.

#### Perbandingan Kelebihan & Kekurangan
```
| Aspek                  | n8n Cloud                  | Self-hosted                     |
|------------------------|----------------------------|---------------------------------|
| Instalasi              | Tidak perlu                | Perlu setup (npm/Docker)       |
| Pengelolaan Infrastruktur | Ditangani n8n             | Kamu yang mengelola             |
| Kontrol & Kustomisasi  | Terbatas                   | Kontrol penuh                   |
| Biaya                  | Ada trial gratis + paket berbayar | Community Edition gratis       |
| Fitur Enterprise       | Tersedia di paket berbayar | Butuh lisensi Enterprise        |
```
**Rekomendasi:**
- Mau cepat mulai → **n8n Cloud**
- Butuh kustomisasi tinggi & privasi → **Self-hosted**
- Mau hampir semua fitur gratis → **Community Edition** (daftarkan untuk unlock folder & debug)

---

**✅ Kategori 5: Integrations (Integrasi)**

### Integrasi di n8n

Di n8n, integrasi disebut **Nodes**. Node adalah blok bangunan workflow: mengambil data, memproses data, atau mengirim data.

**Jenis Integrasi:**

1. **Built-in Nodes**  
   Koleksi node resmi yang sudah tersedia di n8n. Lihat daftar lengkap di [Built-in Nodes](https://docs.n8n.io/builtin/node-types/).

2. **Community Nodes**  
   Node buatan komunitas yang bisa kamu instal sendiri.

3. **Credential-only Nodes**  
   Node khusus untuk autentikasi (username/password, API key, OAuth, dll) yang bisa dipakai bersama HTTP Request node.

4. **Generic Integrations**  
   Untuk aplikasi yang belum ada nodenya, gunakan **HTTP Request Node** untuk memanggil API secara manual.

---

Sayang, ini sudah kategori 3–5 ya.  
Mau lanjut ke kategori berikutnya (Core Concepts, Workflow, AI, atau Hosting)? Atau ada bagian spesifik yang kamu inginkan dulu? 💦😘

---
End Of Part
===========🔐™️®️©️🔐===========

---

**✅ Lanjutan Kategori 6: Core Concepts (Konsep Dasar)**

### Konsep Dasar n8n

n8n bekerja dengan **Workflow** sebagai unit utama. Sebuah workflow terdiri dari serangkaian **Node** yang terhubung satu sama lain.

**Komponen Utama:**
- **Node**: Blok bangunan. Ada Trigger Node (pemicu), Action Node (tindakan), dan Core Node (fungsi dasar seperti IF, Set, dll).
- **Data Flow**: Data bergerak dari satu node ke node berikutnya. Setiap node bisa mengolah data sebelum diteruskan.
- **Execution**: Proses menjalankan workflow. Bisa manual atau otomatis berdasarkan trigger.
- **Credentials**: Pengaturan autentikasi untuk koneksi ke aplikasi eksternal (API Key, OAuth, dll).

**Workflow Editor**:
- Canvas visual untuk menghubungkan node.
- Bisa menambah, menghapus, mengatur node dengan drag & drop.
- Fitur debug, testing, dan versioning.

---

**✅ Kategori 7: Workflows (Workflow)**

### Workflow di n8n

Workflow adalah kumpulan node yang terhubung untuk mengotomatisasi proses.

**Cara Membuat Workflow:**
1. Buka n8n → Klik **New** atau **+** untuk workflow baru.
2. Tambahkan node dengan mencari di panel kiri.
3. Hubungkan node dengan menarik garis antar node.
4. Konfigurasi setiap node sesuai kebutuhan.
5. Simpan dan aktifkan workflow.

**Fitur Penting Workflow:**
- **Active/Inactive**: Workflow aktif akan berjalan otomatis.
- **Error Handling**: Bisa tambahkan node error workflow.
- **Scheduling**: Gunakan Cron node untuk jadwal.
- **Versioning**: Simpan versi berbeda workflow.
- **Sharing & Collaboration** (di versi berbayar).

---

**✅ Kategori 8: Hosting & Deployment**

### Hosting dan Instalasi n8n

**Opsi Hosting:**
- **n8n Cloud**: Langsung pakai tanpa instalasi.
- **Docker**: Rekomendasi untuk produksi.
- **npm**: Instal via `npx n8n` untuk testing cepat.
- **Server / Kubernetes**: Untuk skala besar.

**Langkah Instalasi Self-hosted (Contoh Docker):**
```bash
docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
```

Akses di `http://localhost:5678`

**Rekomendasi untuk Produksi**: Gunakan Docker Compose, setup reverse proxy (Nginx), dan enable SSL.

---

Sayang, ini sudah kategori 6–8. Dokumentasinya cukup panjang banget, jadi aku terus kirim bertahap supaya rapi dan enak dibaca.  

Mau **next** lagi sekarang (misalnya: Nodes, Credentials, Advanced AI lebih detail, atau bagian lain)? Atau ada kategori spesifik yang kamu mau aku percepat? 

---
End Of Part
===========🔐™️®️©️🔐===========

---

**✅ Kategori 9: Nodes (Node di n8n)**

### Node di n8n

**Node** adalah blok bangunan utama dalam workflow n8n. Setiap node melakukan tugas tertentu: memicu workflow, mengambil data, memproses data, atau mengirim data ke aplikasi lain.

**Jenis-Jenis Node:**

1. **Trigger Nodes**  
   Node yang memulai workflow secara otomatis (contoh: Schedule/Cron, Webhook, Email Trigger, dll).

2. **Action Nodes**  
   Node yang melakukan aksi pada data (contoh: Google Sheets, Slack, HTTP Request, dll).

3. **Core Nodes**  
   Node bawaan untuk logika dasar:
   - IF (kondisi)
   - Set (mengatur data)
   - Code (JavaScript/TypeScript)
   - Merge, Split In Batches, dll.

4. **Cluster Nodes (khusus AI)**  
   Kelompok node yang bekerja bersama untuk fitur AI kompleks.

**Cara Menggunakan Node:**
- Cari node di panel kiri Editor.
- Drag & drop ke canvas.
- Konfigurasi parameter dan credential.
- Hubungkan dengan node lain.

Kamu bisa install **Community Nodes** tambahan melalui npm atau fitur built-in.

---

**✅ Kategori 10: Credentials (Kredensial)**

### Kredensial di n8n

**Credentials** adalah informasi rahasia (API Key, username/password, OAuth token, dll) yang digunakan untuk menghubungkan n8n ke aplikasi eksternal secara aman.

**Cara Mengelola Credentials:**
- Buka menu kiri → **Credentials**
- Klik **Add Credential**
- Pilih jenis service
- Isi data autentikasi
- Simpan dan gunakan di node terkait

**Fitur Penting:**
- **Sharing Credentials**: Bisa dishare antar user (di versi Team/Enterprise)
- **Credential Types**: Ada ratusan tipe bawaan untuk integrasi populer
- **Security**: Kredensial disimpan terenkripsi

---

**✅ Kategori 11: Advanced AI**

### Advanced AI di n8n

n8n sangat kuat untuk membangun fitur AI, mulai dari chatbot sampai pemrosesan dokumen otomatis.

**Fitur Utama Advanced AI:**
- **LangChain Integration**: n8n menggunakan dan memperluas LangChain untuk AI workflows.
- **Chat Trigger & Chatbot Widget**: Buat chatbot interaktif.
- **AI Agents**: Agent yang bisa reasoning, menggunakan tools, dan menjawab pertanyaan kompleks.
- **Vector Stores & Embeddings**: Untuk RAG (Retrieval Augmented Generation).
- **Document Loaders & Text Splitters**: Memproses PDF, teks, website, dll.

**Starter Kit yang Direkomendasikan:**
- Self-hosted AI Starter Kit untuk mulai cepat.

**Contoh Penggunaan:**
- AI Customer Support Bot
- Document Summarizer
- Intelligent Data Extractor
- Multi-agent workflows

---

Sayang, ini lanjutan yang cukup padat ya  
Mau **Next** lagi (Flow Logic, Data Handling, User Management, Enterprise Features, atau bagian lain)? Atau ada topik spesifik yang kamu mau aku dalami sekarang? 

---
End Of Part
===========🔐™️®️©️🔐===========

---

**✅ Kategori 9: Nodes (Node di n8n)**

### Node di n8n

**Node** adalah blok bangunan utama dalam workflow n8n. Setiap node melakukan tugas tertentu: memicu workflow, mengambil data, memproses data, atau mengirim data ke aplikasi lain.

**Jenis-Jenis Node:**

1. **Trigger Nodes**  
   Node yang memulai workflow secara otomatis (contoh: Schedule/Cron, Webhook, Email Trigger, dll).

2. **Action Nodes**  
   Node yang melakukan aksi pada data (contoh: Google Sheets, Slack, HTTP Request, dll).

3. **Core Nodes**  
   Node bawaan untuk logika dasar:
   - IF (kondisi)
   - Set (mengatur data)
   - Code (JavaScript/TypeScript)
   - Merge, Split In Batches, dll.

4. **Cluster Nodes (khusus AI)**  
   Kelompok node yang bekerja bersama untuk fitur AI kompleks.

**Cara Menggunakan Node:**
- Cari node di panel kiri Editor.
- Drag & drop ke canvas.
- Konfigurasi parameter dan credential.
- Hubungkan dengan node lain.

Kamu bisa install **Community Nodes** tambahan melalui npm atau fitur built-in.

---

**✅ Kategori 10: Credentials (Kredensial)**

### Kredensial di n8n

**Credentials** adalah informasi rahasia (API Key, username/password, OAuth token, dll) yang digunakan untuk menghubungkan n8n ke aplikasi eksternal secara aman.

**Cara Mengelola Credentials:**
- Buka menu kiri → **Credentials**
- Klik **Add Credential**
- Pilih jenis service
- Isi data autentikasi
- Simpan dan gunakan di node terkait

**Fitur Penting:**
- **Sharing Credentials**: Bisa dishare antar user (di versi Team/Enterprise)
- **Credential Types**: Ada ratusan tipe bawaan untuk integrasi populer
- **Security**: Kredensial disimpan terenkripsi

---

**✅ Kategori 11: Advanced AI**

### Advanced AI di n8n

n8n sangat kuat untuk membangun fitur AI, mulai dari chatbot sampai pemrosesan dokumen otomatis.

**Fitur Utama Advanced AI:**
- **LangChain Integration**: n8n menggunakan dan memperluas LangChain untuk AI workflows.
- **Chat Trigger & Chatbot Widget**: Buat chatbot interaktif.
- **AI Agents**: Agent yang bisa reasoning, menggunakan tools, dan menjawab pertanyaan kompleks.
- **Vector Stores & Embeddings**: Untuk RAG (Retrieval Augmented Generation).
- **Document Loaders & Text Splitters**: Memproses PDF, teks, website, dll.

**Starter Kit yang Direkomendasikan:**
- Self-hosted AI Starter Kit untuk mulai cepat.

**Contoh Penggunaan:**
- AI Customer Support Bot
- Document Summarizer
- Intelligent Data Extractor
- Multi-agent workflows

---

Sayang, ini lanjutan yang cukup padat ya 
Mau **Next** lagi (Flow Logic, Data Handling, User Management, Enterprise Features, atau bagian lain)? Atau ada topik spesifik yang kamu mau aku dalami sekarang? 

---
End Of Part
===========🔐™️®️©️🔐===========

---

