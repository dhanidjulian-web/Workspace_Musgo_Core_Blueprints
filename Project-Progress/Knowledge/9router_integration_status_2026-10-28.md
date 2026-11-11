# KNOWLEDGE — Status Integrasi 9router (MusGo-OS 2in1)

## STATUS: SELESAI & TER-PUSH
Commit 7246b8e di git@github.com:dhanidjulian-web/MusGo-OS_2in1.git
HEAD = origin/main, ahead/behind 0/0, tree bersih, 0 .pyc ter-track.

## ARSITEKTUR INTEGRASI
```
Aplikasi / Agent
    -> ModelRouter (SDK)              register_provider("9router", probe=is_available)
    -> provider_9router_adapter       sys.path -> ai_provider_9router/
    -> NineRouterClient               (modul stdlib-only)
    -> Gateway 9router 127.0.0.1:20128/v1
    -> 861 model / 86 provider
```
Jalur kedua: Layer 09 gateway blok `ai_inference` -> /ai/infer => /chat/completions

## KONTRAK API MODUL
health() | list_models() | chat_completion() | model_resolve()

## ENDPOINT & KONFIG
base_url  : http://127.0.0.1:20128/v1
health_url: http://127.0.0.1:20128/api/health
models_url: http://127.0.0.1:20128/v1/models
API key   : env MUSGO_9ROUTER_API_KEY (jangan hardcode)
Budget    : daily $5 / monthly $100, on_exceed block

## ROUTING (capability_then_cost)
general      -> deepseek/deepseek-chat
reasoning    -> deepseek/deepseek-reasoner
code         -> deepseek/deepseek-coder
vision       -> gemini/gemini-2.5-pro
long_context -> gemini/gemini-2.5-pro
cheap_bulk   -> groq/llama-3.3-70b

## CATATAN TEKNIS PENTING
1. PyYAML TIDAK tersedia di sandbox -> load_config() fallback ke JSON
   berdampingan. Adapter pakai prefer_json=True sebagai default.
   Kedua file (yaml & json) HARUS dijaga sinkron.
2. Exec-bit di proot tidak bisa diubah (chmod rc=0 tapi tetap 660)
   -> jalankan `bash <script>` bukan `./<script>`.
3. Impor SDK: root = SDK/python_sdk, paket = src.ai.
4. tests/unit/test_ai.py gagal karena isu impor relatif LAMA (bukan regresi).

## STATUS GATEWAY
Server 9router hidup: http=200 {"ok":true}
Start (WAJIB background=true di sandbox):
node /usr/local/lib/node_modules/9router/cli.js --no-browser --host 127.0.0.1 --port 20128 --skip-update

Founder Sig: DHANI YULIAWAN
