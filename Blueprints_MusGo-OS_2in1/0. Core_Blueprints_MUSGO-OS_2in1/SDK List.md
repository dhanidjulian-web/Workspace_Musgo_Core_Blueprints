Halaman ini tidak berisi tautan untuk mengunduh atau menyalin source code (kode sumber) SDK. Sebaliknya, halaman ini mendokumentasikan nama paket npm untuk setiap provider AI. Untuk mendapatkan kodenya, Anda perlu menginstal paket-paket ini.

📦 Daftar Paket SDK Provider AI

Berikut adalah daftar lengkap provider dan nama paket npm-nya yang tercantum di halaman tersebut, dikelompokkan untuk kemudahan:

Provider Resmi (oleh Vercel AI SDK):

· @ai-sdk/xai (xAI Grok)
· @ai-sdk/openai (OpenAI)
· @ai-sdk/azure (Azure OpenAI)
· @ai-sdk/anthropic (Anthropic)
· @ai-sdk/amazon-bedrock (Amazon Bedrock)
· @ai-sdk/google (Google Generative AI)
· @ai-sdk/google-vertex (Google Vertex)
· @ai-sdk/mistral (Mistral)
· @ai-sdk/togetherai (Together.ai)
· @ai-sdk/cohere (Cohere)
· @ai-sdk/fireworks (Fireworks)
· @ai-sdk/deepinfra (DeepInfra)
· @ai-sdk/deepseek (DeepSeek)
· @ai-sdk/cerebras (Cerebras)
· @ai-sdk/groq (Groq)
· @ai-sdk/perplexity (Perplexity)
· @ai-sdk/elevenlabs (ElevenLabs)
· @ai-sdk/lmnt (LMNT)
· @ai-sdk/hume (Hume)
· @ai-sdk/revai (Rev.ai)
· @ai-sdk/deepgram (Deepgram)
· @ai-sdk/gladia (Gladia)
· @ai-sdk/assemblyai (AssemblyAI)
· @ai-sdk/baseten (Baseten)

Provider Buatan Komunitas:

· ollama-ai-provider (Ollama)
· @friendliai/ai-provider (FriendliAI)
· @portkey-ai/vercel-provider (Portkey)
· workers-ai-provider (Cloudflare Workers AI)
· @openrouter/ai-sdk-provider (OpenRouter)
· (dan banyak lainnya seperti yang terdaftar di halaman)

Provider untuk Model yang Dihosting Sendiri:
Halaman tersebut juga menyebutkan bahwa model self-hosted (seperti yang dijalankan lokal) dapat diakses menggunakan @ai-sdk/openai-compatible jika model tersebut mendukung spesifikasi OpenAI.

🛠 Cara Mendapatkan Kode SDK

Kode SDK ini adalah paket Node.js. Untuk "mengekstrak" atau mendapatkannya, Anda perlu menggunakannya melalui npm (Node Package Manager).

1. Instal Paket: Gunakan perintah npm install di terminal proyek Anda.
   ```bash
   npm install @ai-sdk/openai @ai-sdk/anthropic
   ```
2. Akses Kode: Setelah terinstal, kode akan berada di folder node_modules proyek Anda. Anda dapat melihat atau menelusuri kode sumbernya di sana.
3. Lihat di Registry npm: Anda dapat membuka https://www.npmjs.com/package/[nama-paket] (misalnya, https://www.npmjs.com/package/@ai-sdk/openai) untuk melihat detail dan terkadang tautan ke repositori kode sumbernya.
+++------------


Kebanyakan framework AI/ML modern bersifat open-source dengan kode yang tersedia di GitHub.

Framework Utama (Full-Stack ML/DL)

1. TensorFlow & Keras
   · Sumber Kode: https://github.com/tensorflow/tensorflow
   · Keterangan: Framework paling populer untuk production dan research. Keras sekarang terintegrasi penuh sebagai high-level API tf.keras.
   · Bahasa: C++, Python, CUDA.
   · Aktifitas: Sangat aktif.
2. PyTorch
   · Sumber Kode: https://github.com/pytorch/pytorch
   · Keterangan: Framework pilihan untuk penelitian (research) karena dynamic computation graph-nya. Juga kuat untuk production.
   · Bahasa: C++, Python, CUDA.
   · Aktifitas: Sangat aktif.
3. JAX
   · Sumber Kode: https://github.com/google/jax
   · Keterangan: Bukan framework neural network utuh, tetapi library untuk komputasi numerik berperforma tinggi (dengan autograd & JIT). Menjadi dasar bagi banyak proyek baru (seperti Flax, Brax).
   · Bahasa: Python, C++.
   · Aktifitas: Sangat aktif.

High-Level Framework & Alternatif (Berdasarkan PyTorch/JAX/TF)

1. Flax (dibangun di atas JAX)
   · Sumber Kode: https://github.com/google/flax
   · Keterangan: Neural network library yang fleksibel dan elegan untuk JAX.
   · Aktifitas: Aktif.
2. Hugging Face Transformers
   · Sumber Kode: https://github.com/huggingface/transformers
   · Keterangan: De facto standard untuk model NLP (dan sekarang juga vision, audio). Dibangun di atas PyTorch, TensorFlow, dan JAX.
   · Bahasa: Python.
   · Aktifitas: Sangat aktif.
3. Lightning AI PyTorch Lightning
   · Sumber Kode: https://github.com/Lightning-AI/pytorch-lightning
   · Keterangan: Framework wrapper untuk PyTorch yang membuat kode lebih terstruktur, scalable, dan mengurangi boilerplate.
   · Aktifitas: Sangat aktif.
4. Fast.ai
   · Sumber Kode: https://github.com/fastai/fastai
   · Keterangan: High-level library yang dibangun di atas PyTorch, berfokus pada kemudahan penggunaan dan best practices.
   · Aktifitas: Aktif.

Untuk Edge, Mobile, & Production Inference (SDK Ringan)

1. ONNX Runtime
   · Sumber Kode: https://github.com/microsoft/onnxruntime
   · Keterangan: Runtime berperforma tinggi untuk mengeksekusi model dalam format ONNX di berbagai platform (cloud, edge, mobile).
   · Bahasa: C++, dengan binding ke banyak bahasa.
   · Aktifitas: Sangat aktif.
2. TensorFlow Lite
   · Sumber Kode: https://github.com/tensorflow/tflite-micro (untuk mikro) & bagian dari repo TensorFlow utama.
   · Keterangan: SDK untuk mendeply model TensorFlow di perangkat mobile, mikro-kontroler, dan edge devices.
   · Aktifitas: Aktif.
3. OpenVINO™ Toolkit
   · Sumber Kode: https://github.com/openvinotoolkit/openvino
   · Keterangan: Toolkit Intel untuk optimasi dan deploy inference AI di hardware Intel (CPU, GPU, VPU, FPGA).
   · Aktifitas: Sangat aktif.
4. MediaPipe
   · Sumber Kode: https://github.com/google/mediapipe
   · Keterangan: Framework cross-platform untuk pipeline ML yang dapat digunakan untuk live dan streaming media (vision, audio, dll).
   · Aktifitas: Aktif.

Pilihan Lain yang Menarik

1. Apache MXNet
   · Sumber Kode: https://github.com/apache/mxnet
   · Keterangan: Framework deep learning yang scalable dan efisien.
   · Aktifitas: Masih aktif, tetapi komunitas lebih kecil dibanding PyTorch/TensorFlow.
2. Caffe & Caffe2
   · Caffe2 telah digabung ke dalam PyTorch. Codebase Caffe2 sekarang ada di dalam repo PyTorch.

Cara Memilih & Rekomendasi:

· Untuk Riset & Eksperimen Cepat: PyTorch atau JAX/Flax.
· Untuk Production Skala Besar (Terutama di TensorFlow Ecosystem): TensorFlow.
· Untuk NLP: Hugging Face Transformers (dengan backend PyTorch/TF).
· Untuk Kode PyTorch yang Lebih Rapi dan Scalable: PyTorch Lightning.
· Untuk Deploy ke Berbagai Hardware Runtime: ONNX Runtime.
· Untuk Edge/Device Intel: OpenVINO.
· Untuk Aplikasi Mobile & Embedded: TensorFlow Lite atau MediaPipe.
--------------+++


Provider Resmi (oleh Vercel AI SDK)

Semua provider resmi dengan awalan @ai-sdk/ adalah bagian dari monorepo tunggal Vercel AI SDK. Anda dapat menemukan kode spesifik setiap provider di direktori packages/ dari repositori utama:

· Repositori Utama: github.com/vercel/ai-sdk
· Contoh direktori kode provider: packages/provider-openai/, packages/provider-anthropic/, dll.

---

Provider Buatan Komunitas

Berikut adalah tautan langsung ke repositori GitHub untuk provider buatan komunitas. Beberapa nama paket mungkin berbeda sedikit dengan nama repositorinya.

Nama Provider (berdasarkan halaman) Nama Paket / Organisasi Tautan ke Repositori GitHub
Ollama ollama-ai-provider github.com/ollama/ai-provider
FriendliAI @friendliai/ai-provider github.com/friendliai/ai-provider
Portkey @portkey-ai/vercel-provider github.com/Portkey-AI/vercel-provider
Cloudflare Workers AI workers-ai-provider github.com/cloudflare/workers-ai-provider
OpenRouter @openrouter/ai-sdk-provider github.com/openrouter/ai-sdk-provider
Requesty @requesty/ai-sdk github.com/requestyai/ai-sdk
Crosshatch @crosshatch/ai-provider github.com/crosshatch/ai-provider
Mixedbread mixedbread-ai-provider github.com/mixedbread-ai/mixedbread-ai-provider
Voyage AI voyage-ai-provider github.com/voyageai/voyage-ai-provider
Mem0 @mem0/vercel-ai-provider github.com/mem0ai/vercel-ai-provider
Letta @letta-ai/vercel-ai-sdk-provider github.com/letta-ai/vercel-ai-sdk-provider
Supermemory @supermemory/tools github.com/supermemoryai/tools
Spark spark-ai-provider github.com/spark-ai/ai-provider
LangDB @langdb/vercel-provider github.com/langdb/vercel-provider
Dify dify-ai-provider github.com/dify-ai/ai-provider
Sarvam sarvam-ai-provider github.com/sarvam-ai/ai-provider
A2A a2a-ai-provider github.com/a2a-ai/ai-provider
SAP-AI @mymediset/sap-ai-provider github.com/mymediset/sap-ai-provider
AI/ML API @ai-ml.api/aimlapi-vercel-ai github.com/ai-ml-api/aimlapi-vercel-ai
MCP Sampling @mcpc-tech/mcp-sampling-ai-provider github.com/mcpc-tech/mcp-sampling-ai-provider
ACP @mcpc-tech/acp-ai-provider github.com/mcpc-tech/acp-ai-provider

Catatan: Untuk provider komunitas lainnya seperti Aihubmix, AnthropicVertex, Claude Code, Built-in AI, Gemini CLI, OpenCode, dan Codex CLI, saya tidak dapat menemukan repositori publik yang secara langsung cocok dengan nama paketnya. Anda dapat mencoba mencarinya langsung di GitHub atau npm.

---
Sebagai gambaran, berikut adalah cuplikan kode inti yang sangat disederhanakan dari provider OpenAI (diambil dari repositori Vercel AI SDK). Ini menunjukkan bagaimana sebuah provider mendefinisikan kemampuan modelnya:

```typescript
// Contoh sederhana dari pola kode provider
import { createProvider } from '@ai-sdk/core';

export const openaiProvider = createProvider({
  name: 'openai',
  models: {
    'gpt-4o': {
      capabilities: {
        toolUse: true,
        imageInput: true,
        objectGeneration: false,
      },
      maxTokens: 128000,
    },
    // ... definisi model lainnya
  },
  createClient(apiKey) {
    // Logika untuk membuat klien API OpenAI
    return new OpenAIClient(apiKey);
  },
});
```

Untuk melihat kode lengkap dan tepat, silakan kunjungi direktori packages/provider-openai/src/ di repositori utama.
------------------------

## MCP Connections

Connect apps and accounts so that v0 can reference them when generating content.
10 MCPs

```
Z
Zapier
Workflow automation and app integration.
https://mcp.zapier.com/api/mcp/a/25664531/mcp

Z
Zapier
Workflow automation and app integration.
https://mcp.zapier.com/api/mcp/s/Mjk3M2E4MWUtYmQ5Zi00ZmVlLWFkODQtNDM3YTNlMmE5YmE3OjNlNWE4MDRhLTE0YmItNDYwZS1hNjA0LTViZWZkMWEyOTAwZQ==/mcp

Z
Zapier
Workflow automation and app integration.
https://mcp.zapier.com/api/mcp/

Z
Zapier
Workflow automation and app integration.
https://mcp.zapier.com/api/mcp/s/MGIxNjY0MmUtZjcxZi00NDdmLTg2NmEtMTYwMTQxMWRlMGJlOjdhNjA3ZGY2LTIzNDctNDRkZi1iN2ZhLWVjN2Y2OGVjYmNkMw==/mcp

Sanity
Sanity
Content management system.
https://mcp.sanity.io

Notion
Notion
Search and modify your Notion workspace.
https://mcp.notion.com/mcp

Linear
Project management and issue tracking.
https://mcp.linear.app/mcp

Hex
Data science and analytics platform.
https://app.hex.tech/mcp

Context7
Context7
Documentation and context tools.
https://mcp.context7.com/mcp

Z
Zapier
Workflow automation and app integration
https://mcp.zapier.com/api/mcp/s/OTU1ZTRmOWEtYzcwYy00Zjk3LTkwOTYtMjk5NTEzZWM3YmViOjE5OTA4NmQ3LTBhNjItNDY4Zi05YzZjLTJhMDljMGFmZjEzYg
```


---
===========🔐™️®️©️🔐===========

---

https://platform.minimax.io/docs/mcp

https://agentskills.io/mcp

https://huggingface.co/mcp?login

Sign

---
===========🔐™️®️©️🔐===========

🔹MusGo-OS 2in1🔹Ai-inside-OS🔹
(2in1 Musyawarah & Gotong-Royong)

🔹Sovereign AI Operating Civilization🔹

🔹© 2026 — Dhani Yuliawan | 
 All Rights Reserved🔹

===========🔐™️®️©️🔐===========

**FOUNDER SIGN: DHANI YULIAWAN**