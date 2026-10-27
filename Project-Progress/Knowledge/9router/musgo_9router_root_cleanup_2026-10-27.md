# KNOWLEDGE — Pembersihan Artefak 9router dari /root
Tanggal: 2026-10-27 | Commit: 19c0a8c | Founder: Dhani Yuliawan

## PERINTAH FOUNDER
"hasil 9router sebelumnya di /root bersihkan atau pindahkan ke clone repo di
 path /root/Repository MusGo-OS_2in1-main"

## INVENTARIS AWAL /root
| Item | Ukuran | Isi | Keputusan |
|---|---|---|---|
| /root/9router-install/ | 148K | apt.log, npm.log, ver.log, ver2.log | PINDAH lalu HAPUS |
| /root/9r.log | 4K | log proses | PINDAH lalu HAPUS |
| /root/9router_run.log | 4K | log start via skrip | PINDAH lalu HAPUS |
| /root/.9router/ | 20M | jwt-secret, auth/cli-secret, db/, runtime | TETAP |

## TUJUAN DI REPO
cognitive_domain/layer_05_agent_orchestration/ai_provider_9router/runtime_artifacts/
  logs/     : 6 file (apt.log, npm.log, ver.log, ver2.log, 9r.log, 9router_run.log)
  catalog/  : 2 file (model-catalog.json 318K, model-catalog-raw.json 622K)
  README.md : dokumentasi asal-usul
Total: 1.1 MB

## PROSEDUR KEAMANAN
1. PINDAI SECRET: pola jwt-secret, cli-secret, sk-*, ghp_*, api_key, token, password
   HASIL: TIDAK ADA. (kata "token" di apt.log hanya nama paket Debian node-js-tokens)
2. Catalog diperiksa: hanya keys v, etag, syncedAt, models, providers (metadata murni)
3. cmp 8 file: SEMUA IDENTIK sebelum sumber dihapus
4. .gitignore diperkuat: .9router/, **/jwt-secret, **/cli-secret,
   **/auth/cli-secret, **/runtime/node_modules/ -> check-ignore PASS
5. Push diverifikasi (9 file di origin/main) SEBELUM hapus sumber

## MENGAPA /root/.9router TIDAK DIPINDAH
1. Masih AKTIF dipakai server (memindah = memutus proses)
2. Berisi SECRET: jwt-secret (64B), auth/cli-secret (64B)
3. Berisi runtime/node_modules ~19MB (sql.js) = dependensi runtime
Relokasi bila perlu: set HOME / flag config, JANGAN copy secret ke repo.

## HASIL
/root sisa: .9router/ (20M) saja. Server tetap hidup: http=200 {"ok":true}

## GIT
commit 19c0a8c, push 67bc8ed..19c0a8c, ahead/behind 0/0, 10 file masuk

Founder Sig: DHANI YULIAWAN
