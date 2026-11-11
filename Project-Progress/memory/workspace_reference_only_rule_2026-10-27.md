# MEMORY — ATURAN: /root/projects = REFERENSI SAJA
Tanggal: 2026-10-27 | Founder: Dhani Yuliawan | Status: MENGIKAT

## PERINTAH FOUNDER (verbatim)
"di path workspace local ga ada bekas commit ke git karna sebelumnya aku upload
 zip manual ke repo git lalu tugaskan agent unzip di sana lewat ssh.
 hentikan periksa dan utak-atik Workspace /root/projects
 Hanya sebagai sumber referensi local utk generate code repo di path local clone repo.
 Repository Blueprint di github bertujuan utk agents external yg butuhkan akses Blueprint."

## MAKNA OPERASIONAL
/root/projects TIDAK punya commit git. ITU NORMAL, BUKAN RUSAK, BUKAN DATA HILANG.
Penyebab: repo diisi lewat upload ZIP manual + unzip via SSH oleh agent lain.

## LARANGAN
- DILARANG git fetch / clone / push / commit di /root/projects
- DILARANG git status berulang / inspeksi mendalam di sana
- DILARANG menganggapnya repo yang perlu disinkronkan ke GitHub

## FUNGSI TIAP PATH (jangan tertukar)
1. /root/projects
   = SUMBER REFERENSI lokal. Baca saja (read-only).
   Isi: AGENTS.md, Agent files/, Agents-Skills/, Blueprints_MusGo-OS_2in1/,
        MusGo.json, Project-Progress/, dll.
   PENGECUALIAN: Project-Progress/ tetap boleh DITULIS untuk save memory/
   knowledge/state. Itu memang tujuannya.

2. /root/Repository MusGo-OS_2in1-main
   = TEMPAT KERJA. Di sini edit/generate code, commit lokal, push SSH.

3. Workspace_Musgo_Core_Blueprints (GitHub)
   = KONSUMSI AGENT EKSTERNAL. Dikelola Founder via upload. BUKAN target
     kerja sesi ini. Jangan push kesana tanpa perintah eksplisit.

## ALUR BAKU
  baca referensi di /root/projects
    -> generate/tulis code di /root/Repository MusGo-OS_2in1-main
    -> commit lokal
    -> push SSH ke git@github.com:dhanidjulian-web/MusGo-OS_2in1.git

## PEMBERSIHAN AKIBAT KESALAHAN SAYA
/tmp/bp_sync (261 MB), /root/sync_blueprint.sh, /root/sync_blueprint.log -> DIHAPUS.
/root/projects terverifikasi kembali seperti semula: 11 untracked, nol commit.

Founder Sig: DHANI YULIAWAN
