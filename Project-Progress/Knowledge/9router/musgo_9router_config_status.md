# KNOWLEDGE — Status Modul AI Provider 9router (MusGo-OS 2in1)
Diperbarui: 2026-10-27 | HEAD repo: 174b567

## LOKASI
Repo target : /root/Repository MusGo-OS_2in1-main
Remote      : git@github.com:dhanidjulian-web/MusGo-OS_2in1.git (SSH)
Path modul  : cognitive_domain/layer_05_agent_orchestration/ai_provider_9router/

## 13 FILE MODUL (11 tracked di f60f297 + 2 baru di 174b567)
| # | File | Ket |
|---|------|-----|
| 1 | __init__.py | ekspor publik |
| 2 | router_9router.py | logika inti, stdlib-only, 407 baris |
| 3 | config/9router_config.yaml | config kanonik 5174 B |
| 4 | config/9router_config.json | fallback tanpa PyYAML 4028 B |
| 5 | agents/ai_provider_agent.yaml | agent 2178 B, authority matrix |
| 6 | skills/skill_ai_provider_9router.md | pasangan skill (duality) 2921 B |
| 7 | prompts/system_prompt_ai_provider.md | system prompt 1936 B |
| 8 | workflows/wf_ai_inference.yaml | alur 8 langkah 2198 B |
| 9 | hooks/hooks_9router.py | hook lifecycle |
| 10 | tests/test_9router_offline.py | 10 test |
| 11 | tests/test_9router_live.py | 4 probe |
| 12 | README.md | BARU 174b567, 153 baris |
| 13 | scripts/9router_ctl.sh | BARU 174b567, executable |

## PRINSIP
- deny_by_default: true
- fail_closed: true
- API key: env MUSGO_9ROUTER_API_KEY (JANGAN hardcode)
- audit_all_calls: true -> logs/ai_provider_9router.log (JSONL)
- budget: daily $5.0 / monthly $100.0, on_exceed: block

## KELAS & FUNGSI
Exception: NineRouterError, ModelNotAllowedError, GatewayUnhealthyError,
           BudgetExceededError, RoutingError
AllowlistGuard : check(model_id), _match(pattern, value)
HealthProbe    : is_healthy(), failure_count()
NineRouterClient: resolve(), chat(), list_models(), _check_budget(),
                  _audit(), _post_chat(), load_config()

## ROUTING (capability_then_cost)
general      -> deepseek/deepseek-chat, gemini/gemini-2.5-flash (8192)
reasoning    -> deepseek/deepseek-reasoner, anthropic/* (32768, req reasoning)
code         -> deepseek/deepseek-coder, glm/glm-4.6 (16384, req tools)
vision       -> gemini/gemini-2.5-pro, anthropic/* (req vision)
long_context -> gemini/gemini-2.5-pro (min 1,000,000)
cheap_bulk   -> groq/llama-3.3-70b-versatile, cerebras/llama-3.3-70b (<=$0.001/1k)
fallback: enabled, max_hops 2, only_within_allowlist true

## ALLOWLIST PROVIDER (10)
deepseek, gemini, groq, cerebras, fireworks, hyperbolic,
cloudflare-ai, cohere, anthropic, glm
deny_patterns: *-web/* , */DeepSeek-R1-Search

## STATUS UJI TERAKHIR (terbukti)
offline : 10 PASS / 0 FAIL
live    : 4/4 PASS
health  : {"ok":true}
models  : 861 total, 86 provider, 69 lolos allowlist
routing : deepseek/deepseek-chat
fail-closed: OK (tanpa API key -> error terkontrol)

## YANG BELUM
- Belum ada API key valid -> chat nyata belum diuji sampai respons sukses
- Belum ada supervisor autostart (proot tanpa systemd)
- Belum push versi modul ke repo Workspace_Musgo_Core_Blueprints

## CARA PAKAI
cd "/root/Repository MusGo-OS_2in1-main/cognitive_domain/layer_05_agent_orchestration/ai_provider_9router"
bash scripts/9router_ctl.sh start     # nyalakan server
bash scripts/9router_ctl.sh status    # health + models
bash scripts/9router_ctl.sh test      # offline + live
bash scripts/9router_ctl.sh models    # daftar model per provider
bash scripts/9router_ctl.sh stop

Founder Sig: DHANI YULIAWAN
