# MUSGo-OS_2in1

**API INTEGRATION - MODEL ROUTERS**


## Daftar External Ai Providers

1. **Kunciai** Base Url: 
- https://kunciai.id/v1 

**note:** Kunciai set as **default** Provider dan **Fallback** models. Semua Providers dan models masuk dalam daftar **Auto/free-routing** kecuali **Kunciai dan semua modelnya.

2. **kilo.ai** Base Url: 
- https://api.kilo.ai/api/gateway

3. **Nvidia** Base Url: 
- https://integrate.api.nvidia.com/v1

4. **Anyapi** Base Url: 
- https://api.anyapi.ai/v1

5. **Freetheai** Base Url: 
- https://api.freetheai.org/v1 
- https://freetheai.xyz

6. **Agnes Ai** Base Url: 
- https://apihub.agnes-ai.com/v1

7. **cheaperinference** Base Url: 
- https://api.cheaperinference.com/v1

---


## Configurasi Router Untuk Providers

### 1. External Ai Providers configurations.

**Provider** *1
- Add base url 
- Add Api Key *1 
- Auto test Api Key + test model respon balasan lalu validasi (background analisa dan audit). done ✅ **Next ==>** sync
- Sync - load dan index models kategori list (tiers, status, health, token, keunggulan, tools)
- Show Routing selections (provider-auto/free, -auto/BYOK, -auto/frontier, -auto/small, -auto/balance, -auto/mix models, -manual/single model).
- Routers menjalankan model yg di pilih berdasarkan hasil analisa dan audit internal. 
- Harus selalu **instant test model respon** sebelum di pilih utk di jalankan.
- Jika gagal pindah ke model lain. jika semua models provider gagal pindah ke provider berikutnya dan lakukan **instant test model respon** sebelum di pilih dan begitu seterusnya.
- **Kunciai** di atur sebagai Fallback semua Provider dan Fallback semua Models. Di jalankan hanya secara manual.
- Kemudin **Save** pengaturan dan **==> Next** Providers
- Add Api key *2
- Add Api Key *3
- Dan seterusnya jika ada

**Provider** *2
- 

**Provider** 3*
- 

**Dan seterusnya jika ada..**

## Buat script code auto/free-routing nya untuk mr yg bertugas secara global pada suatu sesi mengindex dan mengelola penuh semua free models utk di panggil secara auto random atau manual.

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


### 2. External Api Routers Configuration. 

Baca Dokumentasi dan bandingkan utk pilih router yg hemat token, ringan-cepat, tools calling, dan secure.

- [9Router](https://9router.com/) — Open-source gateway connecting 40+ providers with RTK token compression (2-4x reduction). One API key for all services. **Free-tier routing to Kiro AI (~50 credits/mo: Claude 4.5 + GLM-5 + MiniMax), OpenCode Free (no auth), and Vertex AI ($300 credits).** Smart 3-tier fallback (Subscription → Cheap → Free). MIT license. [GitHub](https://github.com/decolua/9router)
- [OmniRoute](https://omniroute.online/) — Full-stack AI gateway with 250+ providers, 90+ free. TypeScript, runs on Web/Desktop/Android. Prompt compression, 3-level proxy for geo restrictions. [GitHub](https://github.com/diegosouzapw/OmniRoute)
- [LiteLLM](https://litellm.ai/) — Python-based proxy unifying 100+ LLMs behind a single API. Spend tracking, virtual keys, production-ready. MIT license. [GitHub](https://github.com/BerriAI/litellm)
- [Portkey AI Gateway](https://portkey.ai/) — Production guardrails and routing for AI apps. Hybrid open-source (community) and managed (enterprise) tiers. [GitHub](https://github.com/Portkey-AI/gateway)


## Daftar Agent Persona
