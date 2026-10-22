import json, os, re, csv, collections, hashlib

manifest = json.load(open('tools/blueprint_manifest.json', encoding='utf-8'))
TEXT_EXT = {'.md','.txt','.json','.csv','.yml','.yaml','.py','.js','.ts','.tsx','.jsx','.css','.html','.sh','.toml','.ini','.env','.glsl','.xml','.svg','.sql'}

# ---------- classification ----------
CATS = [
 ("01-governance", "Konstitusi, Tata Kelola & Kedaulatan", [
   r'governor', r'constitution', r'konstitus', r'governance', r'tata kelola', r'tier', r'legal',
   r'sovereign', r'kedaulatan', r'manifesto', r'policy', r'ethics', r'etika', r'license', r'pedoman',
   r'decision', r'konsensus', r'musyawarah', r'amanah', r'charter']),
 ("02-architecture", "Arsitektur Sistem & Layer", [
   r'arsitektur', r'architecture', r'layer', r'blueprint', r'struktur', r'framework', r'kernel',
   r'runtime', r'orchestrat', r'event bus', r'diagram', r'design']),
 ("03-security", "Keamanan Siber, Zero-Trust & Hardening", [
   r'security', r'keamanan', r'cyber', r'holes', r'threat', r'zero.trust', r'hardening', r'pentest',
   r'audit', r'firewall', r'encrypt', r'vpn', r'ssh', r'dns', r'forensic', r'malware', r'defence',
   r'defense', r'secret', r'credential', r'hacker', r'hacking']),
 ("04-agent-persona", "Agent, Persona & Prompt Engineering", [
   r'persona', r'\bagent\b', r'prompt', r'skill', r'llm', r'model', r'tool.use', r'system prompt',
   r'\bmcp\b', r'mindpal', r'openai', r'claude', r'gemini', r'qwen', r'grok', r'hugging', r'telegram',
   r'bot', r'notebooklm', r'personas']),
 ("05-economy", "Ekonomi, Monetisasi & Business Intelligence", [
   r'monetisasi', r'monetization', r'pricing', r'billing', r'token', r'revenue', r'bisnis', r'business',
   r'market', r'marketplace', r'ekonomi', r'economic', r'pay.as.you.go', r'commission', r'subscription',
   r'sales', r'customer', r'customer']),
 ("06-infrastructure", "Infrastruktur, VPS, Deployment & Storage", [
   r'vps', r'scalab', r'deploy', r'docker', r'kubernetes', r'nginx', r'hosting', r'infrastructure',
   r'storage', r'database', r'postgres', r'redis', r'backup', r'resilience', r'ipfs', r'cdn',
   r'network', r'networking', r'cloudflare', r'domain', r'configuration', r'server']),
 ("07-features", "Menu, Fitur & Product Specification", [
   r'fitur', r'menu', r'feature', r'suggest', r'\bui\b', r'\bux\b', r'desktop', r'shell', r'apps', r'task',
   r'dashboard', r'workflow', r'automation', r'integrasi', r'integration', r'\bapi\b', r'\bsdk\b', r'zapier',
   r'mobile', r'memori', r'memory']),
 ("08-repository", "Repository, Git & Development Workflow", [
   r'\brepo\b', r'repository', r'github', r'gitlab', r'commit', r'branch', r'vibe', r'development', r'developer',
   r'codebase', r'sandbox', r'sanbox', r'sanboxing', r'testing', r'ci/cd', r'changelog', r'release', r'git']),
 ("09-research", "Riset, Catatan & Laporan (Reports)", [
   r'\breport\b', r'laporan', r'catatan', r'research', r'riset', r'\bnote\b', r'briefing', r'whitepaper',
   r'analisa', r'analisis', r'finding', r'summary', r'ringkasan', r'\bide\b', r'saran', r'masukan',
   r'documentary', r'notebook', r'gems', r'riset']),
]

def classify(entry, folder_hint):
    text_hay = (entry['title'] + ' ' + ' '.join(entry['headings'][:6]) + ' ' + ' '.join(entry['keywords'])).lower()
    path_hay = entry['path'].lower()
    scores = {}
    for cid, name, pats in CATS:
        s = 0
        for p in pats:
            if re.search(p, text_hay):
                s += 2  # isi dokumen lebih berbobot
            if re.search(p, folder_hint):
                s += 3  # struktur folder paling kuat (keputusan manusia)
            if re.search(p, path_hay):
                s += 1
        scores[cid] = s
    best = max(scores.items(), key=lambda kv: kv[1])
    if best[1] == 0:
        return "99-other", "Lain-lain / Unclassified"
    return best[0], dict((c, n) for c, n, _ in CATS)[best[0]]

for e in manifest:
    parts = e['path'].split('/')
    folder_hint = ' '.join(parts[:-1]).lower()
    # Decode %20 style and normalise separators in folder names
    folder_hint = folder_hint.replace('%20', ' ')
    e['category_id'], e['category'] = classify(e, folder_hint)
    e['tags'] = e['keywords'][:8]

# ---------- dedupe detection ----------
by_hash = collections.defaultdict(list)
for e in manifest:
    if e['kind'] == 'text' and e['size'] > 0:
        key = (e['size'], e['lines'])
        by_hash[key].append(e)

dup_groups = []
for key, files in by_hash.items():
    if len(files) > 1 and len(key) > 0:
        canonical = min(files, key=lambda x: len(x['path']))
        for f in files:
            f['duplicate_of'] = None if f is canonical else canonical['path']
        dup_groups.append({'canonical': canonical['path'], 'copies': [f['path'] for f in files if f is not canonical]})
    else:
        for f in files:
            f.setdefault('duplicate_of', None)

for e in manifest:
    e.setdefault('duplicate_of', None)

# ---------- clean titles ----------
def clean_title(e):
    t = (e['title'] or '').strip()
    # strip leading markdown separators / code fences / BOM
    t = t.lstrip('\ufeff')
    if re.match(r'^[=\-_*#~`\|+]{3,}$', t):
        # fallback to filename
        t = os.path.splitext(os.path.basename(e['path']))[0]
    if not t:
        t = os.path.splitext(os.path.basename(e['path']))[0]
    return t

for e in manifest:
    e['display_title'] = clean_title(e)[:140]

# also enrich file stats live
def enrich(e):
    p = e['path']
    try:
        e['size'] = os.path.getsize(p)
    except Exception:
        pass
    ext = os.path.splitext(p)[1].lower()
    if ext in TEXT_EXT and e['kind'] == 'text':
        try:
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                txt = f.read()
            e['lines'] = txt.count('\n') + 1
        except Exception:
            pass
for e in manifest:
    enrich(e)

bycat = collections.defaultdict(list)
for e in manifest:
    bycat[e['category_id']].append(e)

def human_size(n):
    for u in ['B','KB','MB','GB']:
        if n < 1024 or u == 'GB':
            return f"{n:.0f}{u}" if u == 'B' else f"{n:.1f}{u}"
        n /= 1024

def anchor(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def desc(e):
    ex = e.get('excerpt', '').strip()
    if e['kind'] != 'text':
        return f"File {e['ext'] or 'biner'} ({human_size(e['size'])})"
    ex = re.sub(r'^[-=*#>\s]+', '', ex)
    return ex[:180] + ('…' if len(ex) > 180 else '')

def md_escape(s):
    return s.replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')

def link_path(p):
    return p.replace(' ', '%20').replace('#', '%23').replace('(', '%28').replace(')', '%29')

cat_names = {cid: name for cid, name, _ in CATS}
cat_names["99-other"] = "Lain-lain / Unclassified"

total_files = len(manifest)
total_text = sum(1 for e in manifest if e['kind'] == 'text')
total_bin = total_files - total_text
total_lines = sum(e['lines'] for e in manifest)
total_size = sum(e['size'] for e in manifest)
dup_total = sum(1 for e in manifest if e['duplicate_of'])

# footer
FOOTER = [
 "-" * 0,
 "===========🔐™️®️©️🔐===========",
 "",
 "🔹MusGo-OS 2in1🔹Ai-inside-OS🔹",
 "(2in1 Musyawarah & Gotong-Royong)",
 "🔹Sovereign AI Operating Civilization🔹",
 "🔹© 2026 — Dhani Yuliawan |",
 " All Rights Reserved🔹",
 "",
 "===========🔐™️®️©️🔐===========",
 "",
 "**FOUNDER SIGN: DHANI YULIAWAN**",
]

# ================= INDEX.md =================
L = []
L.append("# 📂 MUSGO-OS 2in1 — MASTER BLUEPRINT INDEX")
L.append("")
L.append(f"> **Indeks lengkap seluruh {total_files} file pada repositori ini.** Setiap entri berisi ringkasan yang diambil dari isi file (bukan dari nama saja).")
L.append("> Sumber data kanonik: `tools/blueprint_manifest.json` · Dibangun otomatis via `tools/build_index.py`.")
L.append("")
L.append("---")
L.append("")
L.append("## 📊 Statistik Repositori")
L.append("")
L.append(f"| Metrik | Nilai |")
L.append(f"|---|---|")
L.append(f"| Total file | **{total_files}** |")
L.append(f"| File teks (isi dibaca) | {total_text} |")
L.append(f"| File biner / aset / config | {total_bin} |")
L.append(f"| Total baris teks | {total_lines:,} |")
L.append(f"| Total ukuran | {human_size(total_size)} |")
L.append(f"| Duplikat terdeteksi | {dup_total} file |")
L.append(f"| Jumlah kategori | {len(bycat)} |")
L.append("")
L.append("## 🗂️ Navigasi Cepat per Kategori")
L.append("")
L.append("| No | Kategori | Jumlah | Anchor |")
L.append("|---|---|---|---|")
for i, cid in enumerate(sorted(bycat), 1):
    L.append(f"| {i} | **{cat_names[cid]}** | {len(bycat[cid])} | [buka](#{anchor(cid + '-' + cat_names[cid])}) |")
L.append("")
L.append("## 💡 Cara Pakai")
L.append("")
L.append("1. **Manusia** → gunakan tabel per kategori di bawah (judul + ringkasan isi + ukuran).")
L.append("2. **Agent** → `AGENT_INDEX.md` (format padat siap injeksi konteks).")
L.append("3. **Pencarian keyword** → `SEARCH_INDEX.csv` (bisa dibuka di spreadsheet atau `grep`).")
L.append("4. **Data mentah lengkap** → `tools/blueprint_manifest.json` dan `.blueprint_index.json`.")
L.append("")
L.append("---")
L.append("")

for cid in sorted(bycat):
    L.append(f"## {cid} — {cat_names[cid]}")
    L.append("")
    L.append(f"> **{len(bycat[cid])} file** pada kategori ini.")
    L.append("")
    L.append("| # | File | Baris | Ukuran | Ringkasan Isi | Dup |")
    L.append("|---|------|------:|-------:|---------------|:---:|")
    for i, e in enumerate(sorted(bycat[cid], key=lambda x: x['path'].lower()), 1):
        title = md_escape(e['display_title'][:100])
        d = md_escape(desc(e))
        dup = '✔' if e['duplicate_of'] else ''
        L.append(f"| {i} | [{title}]({link_path(e['path'])}) | {e['lines'] or '-'} | {human_size(e['size'])} | {d} | {dup} |")
    L.append("")

# duplicates section
if dup_groups:
    L.append("## 🔁 Indeks Duplikat (Alias File)")
    L.append("")
    L.append("> File dengan isi identik terdeteksi otomatis. Kolom kanan adalah file kanonik yang direkomendasikan.")
    L.append("")
    L.append("| Duplikat | Ukuran | Kanonik |")
    L.append("|---|---:|---|")
    for g in dup_groups:
        for c in g['copies']:
            f = next(e for e in manifest if e['path'] == c)
            L.append(f"| `{c}` | {human_size(f['size'])} | `{g['canonical']}` |")
    L.append("")

# directory tree
L.append("## 🌳 Peta Direktori (Top Level)")
L.append("")
L.append("| Folder | File | Dominan Kategori |")
L.append("|---|---:|---|")
dircount = collections.Counter(e['path'].split('/')[0] if '/' in e['path'] else '(root)' for e in manifest)
dir_cat = collections.defaultdict(collections.Counter)
for e in manifest:
    d = e['path'].split('/')[0] if '/' in e['path'] else '(root)'
    dir_cat[d][e['category_id']] += 1
for d, c in dircount.most_common():
    dom = dir_cat[d].most_common(1)[0][0]
    L.append(f"| `{d}` | {c} | {dom} |")
L.append("")
L.append("---")
L.append("")
L.extend(FOOTER)
open('INDEX.md', 'w', encoding='utf-8').write("\n".join(L))

# ================= AGENT_INDEX.md =================
A = []
A.append("# 🤖 AGENT_INDEX.md — High-Density Blueprint Map")
A.append("")
A.append(f"> **Total entri: {total_files}.** Tidak ada file yang dihilangkan. Field: `path ;; lines ;; category ;; keywords ;; title`.")
A.append("> Gunakan `grep`/`awk` pada file ini untuk menemukan referensi instan.")
A.append("")
A.append("## ⚡ ROUTING RULES (baca ini dulu)")
A.append("")
A.append("| Kebutuhan | Kategori | Jumlah |")
A.append("|---|---|---|")
routing = {
 "01-governance": "hukum, konstitusi, kebijakan, tier, etika, konsensus",
 "02-architecture": "arsitektur, 17-layer, blueprint, kernel, runtime",
 "03-security": "audit, threat model, zero-trust, hardening, network defence",
 "04-agent-persona": "prompt, persona, agent skill, LLM, model config",
 "05-economy": "pricing, billing, tier ekonomi, sales, revenue",
 "06-infrastructure": "VPS, deploy, database, backup, network, server",
 "07-features": "fitur, menu, UI/UX, workflow, SDK/API, memory",
 "08-repository": "repo, git, dev workflow, sandbox, release",
 "09-research": "riset, catatan, laporan, notebooklm, gems",
 "99-other": "belum terklasifikasi",
}
for cid in sorted(bycat):
    A.append(f"| {routing.get(cid,'-')} | `{cid}` — {cat_names[cid]} | {len(bycat[cid])} |")
A.append("")
A.append("## 🔍 QUICK LOOKUP COMMANDS")
A.append("")
A.append("```bash")
A.append("# cari path berdasarkan kata kunci")
A.append("grep -i '<keyword>' SEARCH_INDEX.csv")
A.append("")
A.append("# daftar semua file pada satu kategori")
A.append("awk -F',' 'NR>1 && $1==\"03-security\" {print $2}' SEARCH_INDEX.csv")
A.append("")
A.append("# cari entri pada AGENT_INDEX ini")
A.append("grep -i '<keyword>' AGENT_INDEX.md")
A.append("```")
A.append("")
A.append("## 📄 FILES PER KATEGORI")
A.append("")
for cid in sorted(bycat):
    A.append(f"### [{cid}] {cat_names[cid]} — {len(bycat[cid])} files")
    A.append("")
    A.append("```text")
    A.append("# path ;; lines ;; keywords ;; title")
    for e in sorted(bycat[cid], key=lambda x: x['path'].lower()):
        kw = ",".join(e['keywords'][:6])
        title = re.sub(r'[\r\n]+', ' ', e['display_title'])[:90]
        dup = ' ;; DUP:' + e['duplicate_of'] if e['duplicate_of'] else ''
        A.append(f"{e['path']} ;; {e['lines'] or 0} ;; {kw} ;; {title}{dup}")
    A.append("```")
    A.append("")

A.append("## 🗺️ DIRECTORY → CATEGORY MATRIX")
A.append("")
A.append("| Folder | Files | Dominant | Distribution |")
A.append("|---|---:|---|---|")
for d, c in dircount.most_common():
    dist = ', '.join(f"{k}:{v}" for k, v in dir_cat[d].most_common(4))
    A.append(f"| `{d}` | {c} | {dir_cat[d].most_common(1)[0][0]} | {dist} |")
A.append("")
A.append("---")
A.append("")
A.extend(FOOTER)
open('AGENT_INDEX.md', 'w', encoding='utf-8').write("\n".join(A))

# ================= SEARCH_INDEX.csv =================
with open('SEARCH_INDEX.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['category', 'path', 'title', 'lines', 'size_bytes', 'ext', 'kind', 'duplicate_of', 'keywords'])
    for e in sorted(manifest, key=lambda x: (x['category_id'], x['path'].lower())):
        w.writerow([e['category_id'], e['path'], e['display_title'][:120], e['lines'], e['size'], e['ext'], e['kind'], e['duplicate_of'] or '', ';'.join(e['keywords'][:8])])

# ================= .blueprint_index.json =================
idx = {
  "version": "2.1",
  "generated_from": "tools/blueprint_manifest.json",
  "total_files": total_files,
  "text_files": total_text,
  "binary_files": total_bin,
  "duplicate_files": dup_total,
  "total_lines": total_lines,
  "total_bytes": total_size,
  "categories": {cid: {"name": cat_names[cid], "count": len(bycat[cid])} for cid in sorted(bycat)},
  "duplicates": dup_groups,
  "files": [{k: e[k] for k in ('path','category_id','display_title','title','lines','size','ext','kind','duplicate_of','keywords')} for e in manifest],
}
json.dump(idx, open('.blueprint_index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ================= verification =================
lines_out = [
 "manifest files: %d" % total_files,
 "INDEX rows: %d" % sum(len(v) for v in bycat.values()),
 "AGENT entries: %d" % sum(len(v) for v in bycat.values()),
 "CSV rows: %d" % (sum(1 for _ in open('SEARCH_INDEX.csv', encoding='utf-8')) - 1),
 "dup files: %d in %d groups" % (dup_total, len(dup_groups)),
]
for cid in sorted(bycat):
    lines_out.append("  %-18s %4d  %s" % (cid, len(bycat[cid]), cat_names[cid]))
open('tools/build_report.txt', 'w', encoding='utf-8').write("\n".join(lines_out))
