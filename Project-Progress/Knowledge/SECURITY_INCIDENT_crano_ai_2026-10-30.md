# INSIDEN KEAMANAN — LOGIN TELEGRAM TIDAK SAH (crano.ai)

**Status:** TERBUKA — butuh tindakan Founder di perangkat
**Dikonfirmasi Founder:** 2026-10-30 ~20:10 WIB
**Kejadian:** 2026-10-23 02:37 WIB
**Durasi terpapar:** 7 hari

---

## 1. KONFIRMASI FOUNDER

Founder DHANI YULIAWAN menyatakan **TIDAK PERNAH** login atau mendaftar ke `crano.ai`.

Kesimpulan: login Telegram via `@crano_ai_oidc_bot` dari Padang = **AKSES TIDAK SAH**.

## 2. FAKTA TERVERIFIKASI

| Item | Detail |
|---|---|
| Waktu | 2026-10-23 02:37 WIB |
| Layanan | crano.ai |
| Mekanisme | Login with Telegram (OIDC) |
| Bot perantara | @crano_ai_oidc_bot |
| Lokasi | Padang |
| IP | IPv6 2404:00c0:d002:de13:... |
| Durasi terpapar | 7 hari (23 Okt -> 30 Okt) |

**Catatan bukti:** notifikasi asli sudah tidak tersimpan di sistem perangkat
(`search_notifications` = 0 hasil untuk "crano", "Telegram", "login", "sign-in").
Bukti bersandar pada catatan memory sesi 2026-10-23.

## 3. INDIKATOR PENDUKUNG (hari yang sama)

- **2026-10-23 16:26 WIB** — Google Play services: "New sign-in on Android"
  akun `dhanidjulian@gmail.com`. Belum dikonfirmasi Founder. Perlu diperiksa.

Dua anomali dalam satu hari (02:37 dan 16:26) = pola yang perlu diwaspadai.

## 4. DAMPAK POTENSIAL

Dengan akses ke akun Telegram, pihak lain dapat:
1. Membaca seluruh riwayat chat
2. Melihat daftar kontak
3. Mengirim pesan atas nama Founder (social engineering ke kontak)
4. Masuk ke layanan lain yang memakai "Login with Telegram"
5. Memantau aktivitas tanpa diketahui

## 5. TINDAKAN DIBERIKAN KE FOUNDER

Urutan prioritas (Telegram dulu, karena itu yang dikompromikan):

1. Telegram -> Settings -> Devices -> **Terminate All Other Sessions**
2. Aktifkan **Two-Step Verification** (password tambahan)
3. Ganti password Telegram
4. Periksa ulang Active Sessions beberapa hari ke depan
5. Google: myaccount.google.com -> Security -> Your devices -> keluarkan yang asing
6. Ganti password akun Google + aktifkan 2FA
7. crano.ai: cek apakah ada akun dengan email Founder, hapus bila ada

## 6. BATASAN AGENT

Sandbox tidak dapat logout Telegram atau Google milik Founder.
Tindakan harus dilakukan Founder di perangkat. Agent hanya bisa:
- Mencatat insiden
- Memberi panduan berurutan
- Memantau notifikasi baru untuk indikator tambahan

---

Founder Sig: DHANI YULIAWAN

---

# RESOLUSI — INSIDEN DITUTUP

**Ditutup:** 2026-10-30 ~20:25 WIB
**Status akhir:** CLOSED — BUKAN pelanggaran (no breach)
**Diputuskan oleh:** Founder DHANI YULIAWAN

## Keterangan Founder

Founder memeriksa langsung layanan crano.ai dan menemukan bahwa
**login ke Telegram GAGAL** beberapa hari lalu. Artinya tidak ada
sesi yang berhasil terbentuk, sehingga tidak ada akses tidak sah
yang benar-benar terjadi.

## Klarifikasi Bukti (dicatat apa adanya)

| Sumber | Isi |
|---|---|
| Notifikasi perangkat 2026-10-23 02:37 | "login baru" via @crano_ai_oidc_bot, Padang |
| Pemeriksaan langsung crano.ai oleh Founder | login GAGAL |

Kedua sumber tidak saling bertentangan secara fatal: notifikasi OIDC
dapat terkirim saat permintaan otorisasi dibuat, meskipun proses
login akhirnya gagal di sisi layanan. Karena pemeriksaan langsung
ke layanan adalah bukti yang lebih kuat, status ditetapkan CLOSED.

**Catatan kejujuran:** notifikasi asli sudah terhapus dari sistem
perangkat sehingga tidak dapat diverifikasi ulang oleh agent.
Kesimpulan ini bersandar pada pemeriksaan langsung Founder.

## Tindakan yang TIDAK diperlukan lagi

- Terminate All Other Sessions — tidak mendesak (login gagal)
- Ganti password Telegram — tidak mendesak
- Audit perangkat Google — boleh dilakukan kapan saja sebagai kebiasaan baik

## Sisa saran (opsional, bukan wajib)

1. Hapus akun crano.ai bila ada, karena tidak dipakai
2. Sekali waktu cek Telegram -> Settings -> Devices untuk memastikan
   tidak ada sesi lokasi Padang (kebiasaan higienis, bukan karena alarm)
3. Tidak perlu lagi memantau insiden ini

## Pengingat terjadwal

Task f34610dc-970f-4b37-937c-dfd0d56f4732 DIBATALKAN atas permintaan Founder.

---

Founder Sig: DHANI YULIAWAN
