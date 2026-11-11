#!/usr/bin/env python3
# Zero-dependency (stdlib) workspace file index generator for /root/projects
import os, json, time, re, sys, hashlib

ROOT = "/root/projects"
OUT  = os.path.join(ROOT, "Project-Progress", "Knowledge", "Workspace-File-Index")

def walk():
    entries = []  # (relpath, type, size, mtime)
    dirs = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        if ".git" in rel.split(os.sep):
            continue
        if rel == ".":
            rel = "(root)"
        dirs.append((rel, dirnames, filenames))
    return dirs

def first_line_desc(path, size):
    """Derive a short description from file head based on type."""
    try:
        with open(path, "rb") as f:
            raw = f.read(600)
    except Exception:
        return "(binary/unreadable)"
    text = raw.decode("utf-8", errors="replace")
    ext = os.path.splitext(path)[1].lower()
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l]

    if not lines:
        return "(empty file)"

    if ext == ".md":
        for l in lines[:8]:
            if l.startswith("#"):
                return re.sub(r"^#+\s*", "", l)[:130]
        return lines[0][:130]
    if ext == ".json":
        # try top-level title/name/description
        for key in ("title", "name", "description", "summary"):
            m = re.search(r'"%s"\s*:\s*"((?:[^"\\]|\\.)*)"' % key, text)
            if m:
                return m.group(1)[:130]
        return lines[0][:130] if lines else "(json)"
    if ext in (".html", ".htm"):
        m = re.search(r"<title[^>]*>\s*(.*?)\s*</title>", text, re.I | re.S)
        if m:
            return m.group(1)[:130]
        return "HTML page"
    if ext == ".tsv":
        return "TSV: " + lines[0][:100]
    if ext == ".csv":
        return "CSV: " + lines[0][:100]
    if ext == ".py":
        return "Python script: " + lines[0][:100]
    if ext == ".js":
        return "JS: " + lines[0][:100]
    if ext in (".sh",):
        return "Shell: " + lines[0][:100]
    # fallback: first content line
    return lines[0][:130]

def human_size(n):
    for u in ["B","KB","MB","GB"]:
        if n < 1024:
            return f"{n:.0f}{u}" if u=="B" else f"{n:.1f}{u}"
        n/=1024
    return f"{n}TB"

def main():
    dirs = walk()
    # Build list of all files
    all_files = []
    for rel, dn, fn in dirs:
        for f in fn:
            full = os.path.join(ROOT, rel if rel!="(root)" else ".")
            p = os.path.join(full, f)
            if os.path.relpath(p, ROOT).startswith(".git"):
                continue
            try:
                st = os.stat(p)
            except Exception:
                continue
            all_files.append((os.path.relpath(p, ROOT), st.st_size, int(st.st_mtime)))

    all_files.sort()
    print(f"TOTAL FILES: {len(all_files)}")

    # Group by top-level area
    areas = {}
    for rel, size, mt in all_files:
        top = rel.split(os.sep)[0] if os.sep in rel else "(root files)"
        areas.setdefault(top, []).append((rel, size, mt))

    index_rows = []   # for MASTER
    per_area = {}

    for area, fl in areas.items():
        fl.sort()
        desc_lines = []
        # index by directory
        by_dir = {}
        for rel, size, mt in fl:
            d = os.path.dirname(rel)
            d = "(root)" if d in ("", ".") else d
            by_dir.setdefault(d, []).append((rel, size, mt))
        for d in sorted(by_dir):
            desc_lines.append(f"\n### Dir: `{d}` ({len(by_dir[d])} files)\n")
            for rel, size, mt in by_dir[d]:
                fname = os.path.basename(rel)
                desc = first_line_desc(os.path.join(ROOT, rel), size)
                desc = desc.replace("`","'")
                desc_lines.append(f"- `{fname}` — {human_size(size)} · {desc}")
        per_area[area] = "\n".join(desc_lines)

    # ---- MASTER INDEX ----
    now = time.strftime("%Y-%m-%d %H:%M %Z", time.gmtime())
    md = ["# WORKSPACE FILE INDEX — /root/projects",
          f"Generated: {now} UTC · Zero-dependency stdlib scan",
          f"Total files: {len(all_files)} · Excludes .git internals",
          "", "## Top-Level Areas", ""]
    for area in sorted(areas, key=lambda a: (-len(areas[a]), a)):
        md.append(f"- **{area}** — {len(areas[area])} files")
    md.append("")
    md.append("## Directory Count")
    n_dir = len([r for (r,_,_) in walk() if r!='(root)' and '.git' not in r.split(os.sep)]) + 0
    # simpler
    # n_dir already computed above
    md.append(f"- Total directories (excl .git): {n_dir}")
    md.append("")
    md.append("All file-level descriptions are auto-derived from each file's header/first field "
              "(H1 for .md, title/name/description for .json, <title> for .html). Full per-file "
              "descriptions are in the per-area files under this same folder.")

    # write master
    with open(os.path.join(OUT, "MASTER_INDEX.md"), "w") as f:
        f.write("\n".join(md))

    # write per-area
    for area, content in per_area.items():
        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", area).strip("_") or "root_files"
        # header
        h = [f"# INDEX: {area}",
             f"Area total: {len(areas[area])} files",
             f"(auto-derived per-file descriptions; see header of each .md/.json for source)",
             content]
        with open(os.path.join(OUT, f"AREA_{safe}.md"), "w") as f:
            f.write("\n".join(h))
        print(f"wrote AREA_{safe}.md ({len(areas[area])} files)")

    # write TSV manifest (machine-readable, all depths)
    with open(os.path.join(OUT, "workspace_files.tsv"), "w") as f:
        f.write("rel_path\ttop_area\tdir\thuman_size\tdesc\n")
        for rel, size, mt in all_files:
            top = rel.split(os.sep)[0] if os.sep in rel else "(root)"
            d = os.path.dirname(rel) or "(root)"
            desc = first_line_desc(os.path.join(ROOT, rel), size).replace("\t"," ").replace("\n"," ")
            f.write(f"{rel}\t{top}\t{d}\t{human_size(size)}\t{desc}\n")
    print(f"wrote workspace_files.tsv ({len(all_files)} rows)")

    # summary stats
    stats = {"total_files": len(all_files), "total_dirs_excl_git": n_dir,
             "areas": {a: len(v) for a,v in sorted(areas.items(), key=lambda x: -len(x[1]))}}
    with open(os.path.join(OUT, "INDEX_STATS.json"), "w") as f:
        json.dump(stats, f, indent=2)
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
