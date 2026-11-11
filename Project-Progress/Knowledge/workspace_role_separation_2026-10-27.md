# KNOWLEDGE — Pemisahan Peran Path (MusGo-OS 2in1)
Tanggal: 2026-10-27 | Founder: Dhani Yuliawan

## TIGA PATH, TIGA PERAN — JANGAN DITUKAR

### 1. /root/projects  —  REFERENSI (read-only)
- Sumber referensi lokal untuk generate code.
- TIDAK punya commit git. NORMAL. Repo diisi via upload ZIP manual + unzip SSH.
- DILARANG: git fetch/clone/push/commit, git status berulang, inspeksi mendalam.
- Isi: AGENTS.md, Agent files/, Agents-Skills/, Blueprints_MusGo-OS_2in1/,
  MusGo.json, Project-Progress/, Prompt_Instructions_*, dll.
- PENGECUALIAN: Project-Progress/ boleh DITULIS (memory, Knowledge, .state, Runtime).

### 2. /root/Repository MusGo-OS_2in1-main  —  TEMPAT KERJA
- Edit / generate / tulis code DI SINI.
- commit lokal -> push SSH ke git@github.com:dhanidjulian-web/MusGo-OS_2in1.git
- Status sekarang: HEAD=19c0a8c, working tree bersih.

### 3. Workspace_Musgo_Core_Blueprints (GitHub)  —  KONSUMSI AGENT EKSTERNAL
- Tujuan: agent external yang butuh akses Blueprint.
- Dikelola Founder via upload ZIP. BUKAN target kerja rutin sesi.
- Jangan push ke sini tanpa perintah eksplisit Founder.
- Ukuran repo ~96 MB (fetch/clone penuh akan timeout di sandbox).

## ALUR BAKU
  [1] baca referensi  : /root/projects (READ-ONLY)
  [2] generate code   : /root/Repository MusGo-OS_2in1-main
  [3] commit lokal    : git add + git commit
  [4] push            : git push origin main (SSH ed25519, tanpa PAT)
  [5] save progress   : /root/projects/Project-Progress/{memory,Knowledge,.state,Runtime}

## KESALAHAN YANG PERNAH TERJADI (jangan diulang)
- Menganggap /root/projects "kehilangan histori git" lalu mencoba sinkronisasi.
  FAKTA: nol commit itu disengaja, bukan kerusakan.
- Mencoba git fetch ke repo blueprint 96MB -> timeout, tidak berguna.
- Menyiapkan push ringkasan ke repo blueprint tanpa perintah eksplisit.

## STATUS AKHIR SESI
- /tmp/bp_sync (261MB) dihapus
- /root/sync_blueprint.sh & .log dihapus
- /root/projects: 11 untracked, nol commit (kembali seperti semula, TIDAK diubah)
- Repo target: HEAD=19c0a8c, bersih
- Server 9router: http=200 {"ok":true}

Founder Sig: DHANI YULIAWAN
