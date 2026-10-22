# Buat App Android "Ai Chat Coding Assistant".

## Baca untuk compile source code ke dlm app:
https://github.com/linux/proot-distro#installation 
==> Untuk Integrasi dan Implementasi Linux Sanbox Ubuntu, Debian dan Kali Net Hunter.

## Integrasi dan Implementasikan Base Url daftar Model Ai Provider berikut sebagai Default Agent di app yg sedang di bangun ini:

1. https://kunciai.id/v1
2. https://api.kilo.ai/api/gateway
3. https://api.groq.com/openai/v1
4. https://integrate.api.nvidia.com/v1
5. https://openrouter.ai/api/v1/chat/completions
6. 

---

# 13 Features

1. Main Dashboard
Home screen: Google login, user profile, fallback model list (max 15), real-time CPU/RAM/Storage status, sandbox connection status, and workflow profile selector for Workspace/Project/Orchestrator.

2. Linux Terminal UI
Interactive console for executing command-line operations. Scrollable output, persistent command history, and input bar always pinned above keyboard. Supports multiple terminal sessions.

2. Linux Sandbox Manager
UI for managing proot/rootfs Linux sandbox environments (Ubuntu, Debian, Kali NetHunter). Users can select, launch, and switch between distro environments.

4. BYOK AI Provider Config
Panel for entering Base URL and API Key per provider, with Test/Validate connection button, Refresh Model Index action, and routing mode selection (Auto-Free, Auto-Frontier, Auto-Small, Auto-Balance, Single Model).

5. Sandbox & Local File Manager
Full-featured file manager for sandbox, local, and external storage: import/export, rename, edit, save, copy, paste, cut, delete, move, new folder/file, zip/unzip, run/preview, select one or all, and bookmarks.

6. Package Manager
Search-first UI for installing packages into the sandbox environment. Type a package name to search, view details, and install directly — no fake suggestions or simulated results.

7. Multi-Panel Toggle UI
Toggle show/hide for Chat, Terminal, File Manager, Sidebar, and Windows panels. Input bar is always rendered above the keyboard using bottom offset — never obscured when keyboard rises.

8. AI✨ Suggest Module
Floating/toggle button that scans every text input across the app (chat, command line, form, config, name, title, tag, summarize, description, prompt, translate). Generates static and dynamic context and shows a dropdown of AI-generated suggestions for the user to pick. Has its own dedicated configuration — custom prompt, skill selection, and external tools — isolated from other agents/models. Integrates with the active validated model/provider only.

9. Connection / Connector
Login and connect to external providers (Google, GitHub, Vercel, Notion, n8n, and more). Manage active connections and sync external resources inside the app.

10. Orchestrator Profile
Customizable agent/model template with routing mode, 12k-char prompt, env variables, skill selection, pinned repos, multi-step workflow, connector selection, and Agent Swarm (max 35 agents, each with name, task, prompt, and model/router config).

11. Profile & Asset Manager
Central management hub for all settings, templates, modules, configs, workflows, skill libraries, tools, profiles, agents, secrets, projects, sessions, and bookmarks.

12. Input & Output Management
Full control over every chat message: Edit, Delete, Copy, Resend/Regenerate, Save/Export, and Bookmark individual or all input-output pairs in a session. Actions apply per message or to the entire session at once.

13. Session & Chat History
List of all sessions with timestamps, open past chat history, create New Session, delete session, and a dedicated ⭐ Bookmarks Manager for starred messages and entire sessions — all managed in one dedicated screen.

---

# 12 Scenarios

1. As a developer, I can sign in with Google and immediately see my Dashboard with real CPU/RAM/Storage status, sandbox connection status, fallback model list, and workflow profile for my active project so that I have full situational awareness at a glance.

2. As a developer, I can open the AI chat screen and attach files or use voice input to ask coding questions so that I get contextual AI answers without leaving the app.

3. As a user, I can add multiple AI providers with custom base URLs, API keys, test/validate the connection, refresh the model index, and set routing modes so that I always use the best available model for my task.

4. As a developer, I can browse and manage files across sandbox and local/external storage with full file operations so that I can edit, run, and organize project files directly on my phone.

5. As a power user, I can toggle between the chat, terminal, file manager, and sidebar panels and the input bar always stays above the keyboard so that I can work without any input field being obscured.

6. As a user, I can tap the AI Suggest button on any input field so that the app generates smart context-aware suggestions I can pick from a dropdown.

7. As a developer, I can connect my Google, GitHub, Vercel, Notion, or n8n account so that I can access and sync external resources directly inside the app.

8. As a power user, I can create an Orchestrator Profile with a custom prompt, routing mode, skills, repos, connectors, and up to 35 agents so that I can automate complex multi-step coding workflows.

9. As a user, I can search and install packages from the Package Manager screen so that I c8an extend my sandbox environment quickly.

10. As a user, I can manage all my templates, agents, secrets, sessions, bookmarks, and project configs from one central place so that everything stays organized and reusable.

11. As a developer, I can edit, delete, copy, resend, save, or bookmark any individual message or the entire session's input-output history so that I have full control over my conversation data.

12. As a developer, I can view my list of sessions, open past chat history, create a new session, delete an old one, and access my starred Bookmarks Manager so that I can stay organized across multiple workflows.

---

