OpenCode Zen adalah daftar model yang telah diuji dan diverifikasi yang disediakan oleh tim OpenCode.

Zen berfungsi seperti penyedia lainnya di OpenCode. Anda masuk ke OpenCode Zen dan mendapatkan kunci API Anda. Ini sepenuhnya opsional dan Anda tidak perlu menggunakannya untuk menggunakan OpenCode.

Latar Belakang
Ada banyak model di luar sana, tetapi hanya beberapa dari model ini yang bekerja dengan baik sebagai agen pengkode. Selain itu, sebagian besar penyedia dikonfigurasi dengan sangat berbeda; jadi Anda mendapatkan kinerja dan kualitas yang sangat berbeda.

Tips

Kami telah menguji sekelompok model dan penyedia yang bekerja dengan baik dengan OpenCode.

Jadi jika Anda menggunakan model melalui sesuatu seperti OpenRouter, Anda tidak akan pernah yakin jika Anda mendapatkan versi terbaik dari model yang Anda inginkan.

Untuk memperbaiki ini, kami melakukan beberapa hal:

Kami menguji sekelompok model yang dipilih dan berbicara dengan tim mereka tentang cara terbaik menjalankannya.
Kami kemudian bekerja dengan beberapa penyedia untuk memastikan bahwa model-model ini disajikan dengan benar.
Akhirnya, kami menguji kombinasi dari model/penyedia dan membuat daftar yang kami rasa baik untuk direkomendasikan.
OpenCode Zen adalah gerbang AI yang memberi Anda akses ke model-model ini.

Cara Kerjanya
OpenCode Zen berfungsi seperti penyedia lainnya di OpenCode.

Anda masuk ke OpenCode Zen, menambahkan rincian penagihan Anda, dan menyalin kunci API Anda.
Anda menjalankan perintah /connect di TUI, memilih OpenCode Zen, dan menempelkan kunci API Anda.
Jalankan /models di TUI untuk melihat daftar model yang kami rekomendasikan.
Anda dikenakan biaya per permintaan dan Anda dapat menambahkan kredit ke akun Anda.

Titik Akhir
Anda juga dapat mengakses model kami melalui titik akhir API berikut.

```
Model	Model ID	Titik Akhir	Paket AI SDK
GPT 5.5	gpt-5.5	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.5 Pro	gpt-5.5-pro	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4	gpt-5.4	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Pro	gpt-5.4-pro	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Mini	gpt-5.4-mini	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.4 Nano	gpt-5.4-nano	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.3 Codex	gpt-5.3-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.3 Codex Spark	gpt-5.3-codex-spark	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.2	gpt-5.2	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.2 Codex	gpt-5.2-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1	gpt-5.1	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex	gpt-5.1-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex Max	gpt-5.1-codex-max	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5.1 Codex Mini	gpt-5.1-codex-mini	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5	gpt-5	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5 Codex	gpt-5-codex	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
GPT 5 Nano	gpt-5-nano	https://opencode.ai/zen/v1/responses	@ai-sdk/openai
Claude Opus 4.8	claude-opus-4-8	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.7	claude-opus-4-7	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.6	claude-opus-4-6	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.5	claude-opus-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Opus 4.1	claude-opus-4-1	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4.6	claude-sonnet-4-6	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4.5	claude-sonnet-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Sonnet 4	claude-sonnet-4	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Haiku 4.5	claude-haiku-4-5	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Claude Haiku 3.5	claude-3-5-haiku	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Gemini 3.5 Flash	gemini-3.5-flash	https://opencode.ai/zen/v1/models/gemini-3.5-flash	@ai-sdk/google
Gemini 3.1 Pro	gemini-3.1-pro	https://opencode.ai/zen/v1/models/gemini-3.1-pro	@ai-sdk/google
Gemini 3 Flash	gemini-3-flash	https://opencode.ai/zen/v1/models/gemini-3-flash	@ai-sdk/google
Qwen3.7 Max	qwen3.7-max	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.7 Plus	qwen3.7-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.6 Plus	qwen3.6-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
Qwen3.5 Plus	qwen3.5-plus	https://opencode.ai/zen/v1/messages	@ai-sdk/anthropic
DeepSeek V4 Flash	deepseek-v4-flash	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiniMax M2.7	minimax-m2.7	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiniMax M2.5	minimax-m2.5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
GLM 5.1	glm-5.1	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
GLM 5	glm-5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Kimi K2.5	kimi-k2.5	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Kimi K2.6	kimi-k2.6	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Grok Build 0.1	grok-build-0.1	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Big Pickle	big-pickle	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
MiMo-V2.5 Free	mimo-v2.5-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
Nemotron 3 Ultra Free	nemotron-3-ultra-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
DeepSeek V4 Flash Free	deepseek-v4-flash-free	https://opencode.ai/zen/v1/chat/completions	@ai-sdk/openai-compatible
```

ID model dalam konfigurasi OpenCode Anda menggunakan format opencode/<model-id>. Sebagai contoh, untuk GPT 5.5, Anda akan menggunakan opencode/gpt-5.5 dalam konfigurasi Anda.

Model
Anda dapat mengambil daftar lengkap model yang tersedia dan metadata mereka dari:

https://opencode.ai/zen/v1/models