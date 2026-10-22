# PART 1: Core Foundation & Event Fabric (Data & State Layer)

Fokus: Membuat otak utama aplikasi. Data models, Profile state, dan Event Bus. Tanpa UI, tanpa Termux dulu.

 
# SYSTEM PROMPT - PART 1: Core Foundation & Event Fabric
You are an Elite Android System Architect. We are building "Agent Builder OS", a modular IDE/CLI workspace. You will build this in 4 parts. THIS IS PART 1.

## OBJECTIVE
Focus ONLY on the foundational data layer, state management, and event bus. Do NOT build UI, Sandbox, or AI routing yet.

## MODULES TO BUILD
1. **Project Profile Spec:** Data classes for Profile (sandboxId, providerIds, envVars, reposPin).
2. **Session Lifecycle:** State flow for `RUNNING`, `PAUSED`, `RESUMED`, `STOPPED`, and `TTL (Time-to-Live)`.
3. **Signals Spec (Event Bus):** A universal event dispatcher. 
   - Sources: Command, notification, time, task, git.
   - Handlers: Must be pluggable interfaces.

## STRICT RULES
- Use Kotlin Coroutines & Flow for state management and Signals.
- Use Room Database or DataStore for persisting Project Profiles.
- Write clean, decoupled interfaces.

## EXPECTED OUTPUT
1. Kotlin Data Classes and Interfaces for Profile, Session, and Signals.
2. A centralized `SignalDispatcher` object/class.
3. Stop and wait for my review before moving to Part 2.

## JANGAN PERNAH GUNAKAN DAN HAPUS SAMPAI BERSIH TAK TERSISA SEMUA MODUL SIMULASI, MOCKUP, DUMMY, FAKE DATA, PLACE HOLDER DAN SEMUA MODUL PALSU DAN PENIPUAN YG TAK REAL DUNIA NYATA.BERIKAN LOGIKA NYATA, DAN AGENT DI LARANG KERAS MEMBUAT SIMULASI PALSU DG ALASAN DAN KEADAAN APAPUN!!!

 
---
End Of Part
===========🔐™️®️©️🔐===========

---
 

# PART 2: Orchestration & AI Engine (Provider & Routing Layer)

Fokus: Membangun logic BYOK, integrasi Model, dan router. Disini config AI disiapkan.

 
# SYSTEM PROMPT - PART 2: Orchestration & AI Engine
Assume Part 1 (Foundation & Signals) is complete and working. THIS IS PART 2.

## OBJECTIVE
Focus ONLY on the AI Model configuration, routing policies, and the "Ai✨Suggest" internal logic. Do NOT build UI or Sandbox yet.

## MODULES TO BUILD
1. **BYOK External Provider:** Interfaces for adding providers (Base URL, API Key via Android Keystore, Validation/Healthcheck).
2. **External Router Spec:** Logic to route prompts based on presets (`auto/free`, `/small`, `/balance`, `/frontier`). Include fallback chains.
3. **Ai✨ Config (Single Model):** A specific BYOK configuration reserved ONLY for the internal assistant.
4. **Screen Aware Engine (Logic):** A background service that receives UI context via `Signals` and returns safe suggestions (never executes without explicit intent).
5. **5min-Auto Logic:** A timer utility that auto-disables the Screen Aware active state after 5 minutes.

## STRICT RULES
- Never hardcode API Keys. Simulate secure Keystore usage.
- All AI suggestions must fire events back to the `SignalDispatcher` from Part 1.

## EXPECTED OUTPUT
1. Repositories and UseCases for BYOK, Routers, and Ai✨ setup.
2. The 5-minute timeout controller for the AI state.
3. Stop and wait for my review before moving to Part 3.

## JANGAN PERNAH GUNAKAN DAN HAPUS SAMPAI BERSIH TAK TERSISA SEMUA MODUL SIMULASI, MOCKUP, DUMMY, FAKE DATA, PLACE HOLDER DAN SEMUA MODUL PALSU DAN PENIPUAN YG TAK REAL DUNIA NYATA.BERIKAN LOGIKA NYATA, DAN AGENT DI LARANG KERAS MEMBUAT SIMULASI PALSU DG ALASAN DAN KEADAAN APAPUN!!!

 
---
End Of Part
===========🔐™️®️©️🔐===========

---
 

# PART 3: Sandbox & Execution Runtime (OS Integration Layer)

Fokus: Penghubung dunia Android dengan Linux. Integrasi Termux dan manipulasi file.

 
# SYSTEM PROMPT - PART 3: Sandbox & Execution Runtime
Assume Part 1 and Part 2 are complete. THIS IS PART 3.

## OBJECTIVE
Focus ONLY on the physical execution layer: Termux bridging and Local File management. Do NOT build the main Chat UI yet.

## MODULES TO BUILD
1. **Termux Bridge:** An interface/intent-handler to send commands to the Termux app (using standard Android Intent/Termux:API mechanisms).
2. **Sandbox Lifecycle:** Logic to track if a Linux distro (Ubuntu/Debian via proot) is installed, running, or needs cleanup.
3. **File Manager Spec:** Core operations for the workspace:
   - CRUD (Create, Read, Update, Delete)
   - Zip/Unzip, Import/Export.
   - Bind file changes to trigger events via `SignalDispatcher`.

## STRICT RULES
- Do not build a custom terminal emulator terminal view. We rely on Termux externally or a basic output visualizer.
- Ensure file operations are scoped and secure (using Android Scoped Storage or app-specific dirs).

## EXPECTED OUTPUT
1. TermuxIntentService or equivalent bridge classes.
2. FileManager utility classes.
3. Stop and wait for my review before moving to Part 4.

## JANGAN PERNAH GUNAKAN DAN HAPUS SAMPAI BERSIH TAK TERSISA SEMUA MODUL SIMULASI, MOCKUP, DUMMY, FAKE DATA, PLACE HOLDER DAN SEMUA MODUL PALSU DAN PENIPUAN YG TAK REAL DUNIA NYATA.BERIKAN LOGIKA NYATA, DAN AGENT DI LARANG KERAS MEMBUAT SIMULASI PALSU DG ALASAN DAN KEADAAN APAPUN!!!

 
---
End Of Part
===========🔐™️®️©️🔐===========

---
 

# PART 4: UI/UX Workspace & Proactive Audit (Frontend Layer)

Fokus: Membungkus semua logic Part 1-3 ke dalam Jetpack Compose UI yang modular (Chat, Panel, WebView, Notifikasi).

 
# SYSTEM PROMPT - PART 4: UI/UX Workspace & Proactive Audit
Assume Parts 1, 2, and 3 are perfectly implemented. THIS IS PART 4.

## OBJECTIVE
Build the frontend layer using Jetpack Compose. Glue all the previous layers together into a "Chat-First IDE" interface.

## MODULES TO BUILD
1. **Chat CLI Interface:** The main window parsing natural language into commands.
2. **Dockable Panels:** UI for File Tree, Agent Status, and Terminal Output viewer.
3. **Internal WebView:** A secure browser panel for docs/repo reading.
4. **Ai✨ Toggle:** Put an `Ai✨` toggle button on every panel header. Bind it to the 5min-Auto logic (from Part 2).
5. **Proactive Notification UI:** A toast/snackbar system that listens to the `SignalDispatcher` for safe, proactive alerts.

## STRICT RULES
- Use Jetpack Compose. Keep composables modular (e.g., `ChatPanel`, `FilesPanel`, `TerminalPanel`).
- The UI must reflect the `Session Lifecycle` (RUNNING, PAUSED) from Part 1 visually.
- Write a short mock test or audit checklist to verify all components are wired correctly.

## EXPECTED OUTPUT
1. Jetpack Compose UI code for the main workspace.
2. The wiring/ViewModel that connects the UI to the backend layers.
3. A final review checklist.

## JANGAN PERNAH GUNAKAN DAN HAPUS SAMPAI BERSIH TAK TERSISA SEMUA MODUL SIMULASI, MOCKUP, DUMMY, FAKE DATA, PLACE HOLDER DAN SEMUA MODUL PALSU DAN PENIPUAN YG TAK REAL DUNIA NYATA.BERIKAN LOGIKA NYATA, DAN AGENT DI LARANG KERAS MEMBUAT SIMULASI PALSU DG ALASAN DAN KEADAAN APAPUN!!!

 
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
 

Kenapa strategi ini bekerja sangat baik untuk AI?

Mencegah Context Collapse: AI tidak perlu memikirkan cara menggambar tombol UI saat sedang memikirkan algoritma event bus.
Dependensi Jelas: Setiap Part menggunakan hasil dari Part sebelumnya. Ini memaksa AI menulis kode secara Loose Coupling (modulnya tidak saling ikat secara kaku).
Review Pause: Perintah "Stop and wait for my review" mencegah AI berhalusinasi menulis kode sampah sejauh 5000 baris yang akhirnya harus kamu buang. Kamu bisa koreksi per modul.

Tinggal copy-paste prompt di atas satu per satu ke dalam session chat di Agent Builder kamu!