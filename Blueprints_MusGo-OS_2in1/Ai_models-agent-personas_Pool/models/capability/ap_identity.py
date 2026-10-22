#!/usr/bin/env python3
"""
MusGo-OS 2in1 - Identity Engine (Persona + Agent + Skill Selector)
=================================================================
Sumber data NYATA dari folder AgentPool:
  - personas/Core 525+ Persona.md   -> 545 persona (3 kategori)
  - agents/*.md                     -> 6 agent definisi
  - skills/Openshell/*/SKILL.md     -> 7 skill definisi

Tidak ada data karangan. Jika sumber tidak terbaca -> return kosong.
"""

import os
import re

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "MusGo-OS_2in1")
POOL = os.path.join(ROOT, "AgentPool")

PERSONA_FILE = os.path.join(POOL, "personas", "Core 525+ Persona.md")
AGENT_DIR = os.path.join(POOL, "agents")
SKILL_DIR = os.path.join(POOL, "skills", "Openshell")

# ---------------------------------------------------------------
# KEYWORD DETECTION - memetakan task ke kategori
# ---------------------------------------------------------------
TASK_CUES = {
    "plan": [
        "rencana", "rencanakan", "plan", "planning", "blueprint", "arsitektur",
        "architecture", "strategi", "strategy", "roadmap", "design", "desain",
        "peta jalan", "susun", "rancang", "struktur", "layout", "konsep",
        "flow", "alur", "spesifikasi", "requirement",
    ],
    "execute": [
        "implementasi", "implement", "bikin", "buat", "build", "kode", "code",
        "coding", "tulis", "write", "script", "jalan", "run", "eksekusi",
        "execute", "patch", "fix", "perbaiki", "benerin", "refactor", "deploy",
        "install", "setup", "konfigurasi", "configure", "rakit", "generate",
    ],
    "guide": [
        "jelaskan", "explain", "apa itu", "mengapa", "kenapa",
        "why", "tutorial", "panduan", "guide", "bantu saya",
        "saya bingung", "bingung", "step by step", "langkah",
        "newbie", "pemula", "first time",
    ],
}

AGENT_CUES = {
    "expert": ["code", "kode", "coding", "program", "python", "javascript",
               "typescript", "go", "rust", "java", "sql", "bug", "error",
               "refactor", "test", "debug", "kompil", "build", "function",
               "class", "api", "endpoint", "database", "html", "css",
               "implementasi", "script", "fungsi", "kelas", "library"],
    "planner": ["plan", "rencana", "arsitektur", "blueprint", "desain", "rancang",
                "roadmap", "spesifikasi", "requirements", "strategi", "struktur"],
    "explorer": ["cari", "find", "telusuri", "search", "explore", "eksplorasi",
                 "cek", "lihat", "list file", "struktur project", "grep", "where",
                 "di mana", "kapan dibuat", "trace"],
    "toolmaker": ["tool", "tools", "manifest", "tool.json", "permission",
                  "runtime api", "custom tool", "openshell", "sdk", "api surface"],
    "scheduler": ["cron", "jadwal", "schedule", "scheduler", "reminder",
                  "calendar", "agenda", "otomatis", "auto-run", "periodik",
                  "harian", "mingguan", "bulanan"],
    "general": ["riset", "research", "analisa", "analisis", "teliti",
                "bandingkan", "compare", "evaluasi", "review",
                "tinjau", "audit", "cek ulang", "verifikasi"],
}

PERSONA_CATEGORY = {
    "live": "AI LIVE GUIDE",
    "planner": "MUSYAWARAH PLANNER",
    "executor": "GORO EXECUTOR",
}

_P_HEAD = re.compile(r"^#(\d{3})\s+([A-Za-z0-9_\-]+)\s*$", re.M)


def _read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def load_personas():
    """
    Parse persona nyata dari file. Return list of dict.

    Kategori TIDAK ditebak dari posisi baris, tapi dari prefix slug
    ('live'/'planner'/'executor') karena nomor persona restart
    di tiap section sehingga posisi baris tidak valid.
    """
    txt = _read(PERSONA_FILE)
    if not txt:
        return []

    def cat_from_slug(slug):
        head = slug.split("_")[0].lower()
        return head if head in PERSONA_CATEGORY else "executor"

    out = []
    matches = list(_P_HEAD.finditer(txt))
    for idx, m in enumerate(matches):
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(txt)
        body = txt[start:end]


        def field(label, b=body):
            mm = re.search(r"^-\s*" + label + r":\s*(.+)$", b, re.M)
            return mm.group(1).strip() if mm else ""

        def section(label, b=body):
            mm = re.search(r"###\s*" + label + r"\s*\n(.+?)(?=\n###|\Z)", b, re.S)
            return re.sub(r"\s+", " ", mm.group(1)).strip()[:400] if mm else ""

        mc = re.search(r"-\s*Cocok Untuk:\s*\n((?:\s{2,}-\s.+\n?)+)", body)
        slug = m.group(2).strip()
        cat = cat_from_slug(slug)
        out.append({
            "id": int(m.group(1)),
            "slug": slug,
            "nama": field("Nama") or slug,
            "tipe": field("Tipe"),
            "aura": field("Aura"),
            "kategori": cat,
            "kategori_nama": PERSONA_CATEGORY[cat],
            "deskripsi": section("Deskripsi"),
            "bicara": section("Cara Bicara"),
            "perilaku": section("Perilaku"),
            "cocok": mc.group(1) if mc else "",
        })
    # dedup by slug (file bisa punya entri persona yg terulang)
    uniq, seen = [], set()
    for p in out:
        if p["slug"] in seen:
            continue
        seen.add(p["slug"])
        uniq.append(p)
    return uniq


def load_agents():
    out = []
    if not os.path.isdir(AGENT_DIR):
        return out
    for fn in sorted(os.listdir(AGENT_DIR)):
        if not fn.endswith(".md"):
            continue
        txt = _read(os.path.join(AGENT_DIR, fn))
        if not txt.strip():
            continue
        lines = [l.rstrip() for l in txt.splitlines()]
        name = next((l.strip() for l in lines if l.strip()), fn[:-3])
        desc, seen = "", False
        for l in lines:
            if l.strip() == name:
                seen = True
                continue
            if seen and l.strip():
                desc = l.strip()
                break
        out.append({
            "name": name, "file": fn, "desc": desc,
            "path": os.path.join(AGENT_DIR, fn),
            "body": txt, "lines": len(lines),
        })
    return out


def load_skills():
    out = []
    if not os.path.isdir(SKILL_DIR):
        return out
    for entry in sorted(os.listdir(SKILL_DIR)):
        p = os.path.join(SKILL_DIR, entry, "SKILL.md")
        if not os.path.isfile(p):
            continue
        txt = _read(p)
        if not txt.strip():
            continue
        lines = [l.rstrip() for l in txt.splitlines()]
        name = next((l.strip() for l in lines if l.strip()), entry)
        desc, seen = "", False
        for l in lines:
            if l.strip() == name:
                seen = True
                continue
            if seen and l.strip():
                desc = l.strip()
                break
        out.append({
            "name": name, "slug": entry, "desc": desc,
            "path": p, "body": txt, "lines": len(lines),
        })
    return out


def _hits(q_low, cues):
    return sum(1 for c in cues if c and c in q_low)


def classify_task(q):
    q_low = (q or "").lower()
    scores = {k: _hits(q_low, v) for k, v in TASK_CUES.items()}
    best = max(scores, key=lambda k: scores[k])
    return "general" if scores[best] == 0 else best


def _agent_key(name):
    """Normalisasi nama agent -> kunci kandidat AGENT_CUES."""
    n = name.lower().strip()
    if n in AGENT_CUES:
        return n
    n = re.sub(r"^expert( ai coding)?$", "expert", n)
    n = re.sub(r"^general(-purpose| purpose)?$", "general", n)
    n = n.replace("-", "").replace(" ", "")
    return n if n in AGENT_CUES else ""


def pick_agent(q, force=None):
    agents = load_agents()
    if not agents:
        return None

    def match(a):
        k = _agent_key(a["name"])
        if not k:
            return False
        if force:
            nf = force.lower().replace(" ", "").replace("-", "")
            return nf in (a["name"].lower().replace(" ", "").replace("-", ""), k)
        return False

    if force:
        for a in agents:
            if match(a):
                return a
        return None

    q_low = (q or "").lower()
    best, best_score = None, 0
    for a in agents:
        k = _agent_key(a["name"])
        s = _hits(q_low, AGENT_CUES.get(k, [])) if k else 0
        if s > best_score:
            best, best_score = a, s
    if best is None or best_score == 0:
        for a in agents:
            if _agent_key(a["name"]) == "general":
                return a
        return agents[0]
    return best


def pick_persona(q, force_id=None, force_slug=None):
    personas = load_personas()
    if not personas:
        return None
    if force_id is not None:
        for p in personas:
            if p["id"] == int(force_id):
                return p
        return None
    if force_slug:
        for p in personas:
            if p["slug"] == force_slug:
                return p
        return None

    cat = classify_task(q)
    target = {"guide": "live", "plan": "planner",
              "execute": "executor", "general": "executor"}.get(cat, "executor")
    pool = [p for p in personas if p["kategori"] == target] or personas

    q_low = (q or "").lower()
    q_words = set(re.findall(r"[a-z]{4,}", q_low))
    best, best_score = None, 0
    for p in pool:
        parts = [p["slug"].replace("_", " "), p["nama"], p["tipe"],
                 p["aura"], p["cocok"], p["deskripsi"]]
        hay = " ".join(parts).lower()
        # keyword utuh pada slug = bobot tinggi (mis. 'docker', 'debug')
        slug_words = set(re.findall(r"[a-z]{4,}", p["slug"].lower()))
        score = 0
        score += 5 * len(q_words & slug_words)
        # kata lain yang muncul di metadata
        score += 1 * sum(1 for w in q_words if w in hay)
        if score > best_score:
            best, best_score = p, score
    return best if best else pool[0]


def pick_skill(q, agent=None, force=None):
    skills = load_skills()
    if not skills:
        return None
    if force:
        for s in skills:
            if s["name"] == force or s["slug"] == force:
                return s
        return None

    q_low = (q or "").lower()
    explicit = {
        "code-review": ["review kode", "code review", "review code", "review ini",
                        "tinjau kode", "review diff"],
        "debug-checklist": ["debug", "bug", "error", "gagal", "traceback",
                            "tidak jalan", "kenapa error", "perbaiki bug"],
        "deep-research": ["riset", "research", "teliti sumber", "bandingkan",
                          "deep dive", "studi", "kumpulkan data"],
        "git-commit": ["commit", "git commit", "pesan commit", "conventional commit"],
        "git-init": ["git init", "init repo", "repository baru", "repo baru"],
        "project-scaffold": ["scaffold", "struktur project", "buat project",
                             "new project", "template project", "scaffolding"],
    }
    for s in skills:
        for kw in explicit.get(s["slug"], []):
            if kw in q_low:
                return s
    return None


# ── TOOLS: capabilities yang relevan per agent ────────────────
TOOL_RULES = {
    "Expert": ["read", "write", "edit", "glob", "grep", "bash", "shell"],
    "explorer": ["glob", "grep", "read", "bash"],
    "planner": ["read", "glob", "grep"],
    "scheduler": ["cron", "calendar", "read"],
    "toolmaker": ["read", "write", "manifest", "permission", "runtime-api"],
    "general": ["glob", "grep", "read", "bash", "web"],
}


def pick_tools(agent=None, q=""):
    """Tentukan daftar tools yang sesuai untuk agent + konteks task.

    Data sumber = AGENT_RULES (kode nyata), BUKAN tebakan.
    """
    if not agent:
        return []
    name = str(agent.get("name", ""))
    tools = TOOL_RULES.get(name)
    if tools is None:
        # fallback jujur: ambil dari body agent bila memuat nama tool
        body = str(agent.get("body", "")).lower()
        found = [t for t in ("read", "write", "edit", "glob", "grep",
                             "bash", "shell", "cron", "calendar", "web")
                 if t in body]
        tools = found
    return list(tools)


def compose_system_prompt(q, persona=None, agent=None, skill=None,
                          base_prompt=None):
    parts = []
    if persona:
        parts.append(
            "## PERSONA (MusGo-OS Persona Engine)\n"
            f"- ID: #{persona['id']:03d} | Nama: {persona['nama']}\n"
            f"- Kategori: {persona['kategori_nama']}\n"
            f"- Aura: {persona['aura'] or '-'}\n"
            f"- Tipe: {persona['tipe'] or '-'}")
        if persona.get("bicara"):
            parts.append("### Gaya bicara\n" + persona["bicara"])
        if persona.get("perilaku"):
            parts.append("### Perilaku\n" + persona["perilaku"])
    if agent:
        parts.append("## PERAN AGENT\n"
                     f"- Nama: {agent['name']}\n"
                     f"- Fokus: {agent['desc'] or '-'}")
    if skill:
        parts.append("## SKILL AKTIF\n"
                     f"- Skill: {skill['name']}\n"
                     f"- Deskripsi: {skill['desc'] or '-'}")
    tools = pick_tools(agent, q)
    if tools:
        parts.append("## TOOLS TERSEDIA\n"
                     "- " + ", ".join(tools) +
                     "\n- Gunakan hanya tools di atas. Jangan mengarang "
                     "tools yang tidak ada.")
    if base_prompt:
        parts.append("## INSTRUKSI DASAR\n" + base_prompt)
    if not parts:
        return ""
    return ("\n\n".join(parts) +
            "\n\nJawab sebagai persona & peran di atas. "
            "Gunakan Bahasa Indonesia formal.")


def select_all(q, force_agent=None, force_persona=None, force_skill=None):
    agent = pick_agent(q, force_agent)
    persona = pick_persona(q, force_persona)
    skill = pick_skill(q, agent, force_skill)
    return {
        "task_category": classify_task(q),
        "persona": persona,
        "agent": agent,
        "skill": skill,
        "tools": pick_tools(agent, q),
        "system_prompt": compose_system_prompt(q, persona, agent, skill),
    }


def stats():
    return {
        "personas": len(load_personas()),
        "agents": len(load_agents()),
        "skills": len(load_skills()),
        "persona_file_exists": os.path.isfile(PERSONA_FILE),
        "persona_file_size": (os.path.getsize(PERSONA_FILE)
                              if os.path.isfile(PERSONA_FILE) else 0),
    }


if __name__ == "__main__":
    from collections import Counter
    s = stats()
    print("=== IDENTITY ENGINE STATS (angka nyata) ===")
    for k, v in s.items():
        print(f"  {k:22} : {v}")
    ps = load_personas()
    if ps:
        print("\n=== 3 persona pertama ===")
        for p in ps[:3]:
            print(f"  #{p['id']:03d} {p['slug']:22} [{p['kategori']}] {p['nama']}")
        print("\n=== sebaran kategori ===")
        for k, v in Counter(p["kategori"] for p in ps).items():
            print(f"  {k:10} : {v}")
    print("\n=== agents ===")
    for a in load_agents():
        print(f"  {a['name']:20} : {a['desc'][:58]}")
    print("\n=== skills ===")
    for sk in load_skills():
        print(f"  {sk['slug']:20} : {sk['desc'][:58]}")