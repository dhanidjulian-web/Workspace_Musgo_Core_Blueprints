#!/usr/bin/env python3
"""
Generator Index Deskripsi Semua File — /root/projects
Output: /root/projects/Project-Progress/Knowledge/Workspace-File-Index/
- WORKSPACE_FILE_INDEX_MASTER.md
- 01_root_files.md
- 02_agent_files.md
- 03_agents_skills.md
- 04_blueprints.md
- 05_project_progress.md
"""
import os, json, re, html
from collections import OrderedDict

ROOT = "/root/projects"
OUT  = os.path.join(ROOT, "Project-Progress", "Knowledge", "Workspace-File-Index")
AREAS = ["__root__", "Agent files", "Agents-Skills", "Blueprints_MusGo-OS_2in1", "Project-Progress"]
SLUG  = {"__root__":"01_root_files", "Agent files":"02_agent_files",
         "Agents-Skills":"03_agents_skills", "Blueprints_MusGo-OS_2in1":"04_blueprints",
         "Project-Progress":"05_project_progress"}

def desc_of(path, ext):
    """Return (size_kb, description) for a single file."""
    size_kb = os.path.getsize(path) / 1024.0
    desc = "(no readable header)"
    try:
        if ext in (".md", ".markdown", ".txt", ".json", ".yml", ".yaml", ".csv"):
            with open(path, "r", errors="replace") as f:
                head = f.read(3000)
            lines = [l.strip() for l in head.splitlines() if l.strip()]
            if ext == ".json":
                # try to find title/name/description
                for key in ("title", "name", "description", "summary", "subject"):
                    m = re.search(r'"%s"\s*:\s*"(.*?)"' % key, head, re.S)
                    if m and m.group(1).strip():
                        desc = m.group(1).strip()[:160]
                        break
                else:
                    # fallback: first non-empty line
                    if lines: desc = lines[0][:160]
            else:
                # md/txt: first heading, else first non-empty
                for l in lines:
                    if l.startswith("#"):
                        desc = l.lstrip("# ").strip()[:160]
                        break
                else:
                    if lines: desc = lines[0][:160]
        elif ext == ".html":
            with open(path, "r", errors="replace") as f:
                head = f.read(3000)
            m = re.search(r"<title>(.*?)</title>", head, re.S | re.I)
            desc = (m.group(1).strip()[:160] if m else head.strip()[:120])
        else:
            # text-like or unknown: first meaningful line
            try:
                with open(path, "r", errors="replace") as f:
                    raw = f.read(400)
                lines2 = [l.strip() for l in raw.splitlines() if l.strip()]
                desc = (lines2[0][:120] if lines2 else "(empty file)")
            except Exception:
                desc = "(binary file)"
    except Exception as e:
        desc = f"(error: {e})"
    return size_kb, desc

def walk_area(area):
    """Walk an area dir (or ROOT for __root__), return list of (relpath, size_kb, desc, mtime)."""
    results = []
    if area == "__root__":
        base = ROOT
        files = [f for f in os.listdir(base) if os.path.isfile(os.path.join(base, f))]
        for f in sorted(files):
            p = os.path.join(base, f)
            ext = os.path.splitext(f)[1].lower()
            size, desc = desc_of(p, ext)
            mtime = os.path.getmtime(p)
            results.append((f, size, desc, mtime))
    else:
        base = os.path.join(ROOT, area)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for fn in sorted(filenames):
                p = os.path.join(dirpath, fn)
                rel = os.path.relpath(p, ROOT)
                ext = os.path.splitext(fn)[1].lower()
                size, desc = desc_of(p, ext)
                mtime = os.path.getmtime(p)
                results.append((rel, size, desc, mtime))
    return results

def tree_view(area, all_files):
    """Build an indented tree showing directories + file counts for one area."""
    lines = []
    if area == "__root__":
        lines.append(f"# Root files — {len(all_files)} file\n")
        for rel, size, desc, _ in all_files:
            lines.append(f"- `{rel}`  ({size:.1f} KB)")
            if desc: lines.append(f"  → {desc}")
        return "\n".join(lines)
    else:
        # group by top-level dir under area
        by_dir = OrderedDict()
        for rel, size, desc, _ in all_files:
            # rel = area/subdir/.../file
            top = rel.split("/", 1)[1] if "/" in rel else rel
            by_dir.setdefault(top, 0)
            by_dir[top] += 1
        lines.append(f"## {area} — {len(all_files)} file, {len(by_dir)} top-level entries\n")
        lines.append("| Entry | File Count |")
        lines.append("|-------|------------|")
        for d, c in sorted(by_dir.items()):
            lines.append(f"| {d} | {c} |")
        lines.append("\n**Note**: Detail per-file di bawah (scroll ke bawah, semua lapisan & kedalaman).\n")
        return "\n".join(lines)

def main():
    os.makedirs(OUT, exist_ok=True)
    print("Walk & describe all files...")
    data = {}
    for area in AREAS:
        r = walk_area(area)
        data[area] = r
        print(f"  {area}: {len(r)} files")
    
    total = sum(len(v) for v in data.values())
    print(f"Total: {total} files")
    
    # --- Master ---
    with open(os.path.join(OUT, "WORKSPACE_FILE_INDEX_MASTER.md"), "w") as out:
        out.write("# WORKSPACE FILE INDEX — MASTER\n\n")
        out.write(f"Source: `/root/projects`  |  Total files: **{total}**  |  Generated: auto\n\n")
        out.write("## Summary per Area\n\n")
        out.write("| Area | File Count |\n|------|------------|\n")
        for area in AREAS:
            label = "Root files" if area == "__root__" else area
            out.write(f"| {label} | {len(data[area])} |\n")
        out.write("\n## Per-Area Index Files\n\n")
        for area in AREAS:
            out.write(f"- `{SLUG[area]}.md` — {label}\n".replace("{label}", "Root files" if area=="__root__" else area))
        out.write("\n---\n\n## Full Tree View (all layers & depths)\n\n")
        for area in AREAS:
            out.write(tree_view(area, data[area]))
            out.write("\n\n---\n\n")
        # per-file detail
        out.write("## Full Per-File Description Index\n\n")
        for area in AREAS:
            label = "Root files" if area == "__root__" else area
            out.write(f"\n### Area: {label} ({len(data[area])} files)\n\n")
            for rel, size, desc, _ in data[area]:
                out.write(f"- `{rel}`  ({size:.1f} KB)\n")
                if desc:
                    out.write(f"  → {desc}\n")
        print("Master written.")
    
    # --- Per-area files ---
    for area in AREAS:
        label = "Root files" if area == "__root__" else area
        with open(os.path.join(OUT, f"{SLUG[area]}.md"), "w") as out:
            out.write(f"# INDEX — {label}\n\n")
            out.write(f"Path: `{ROOT if area=='__root__' else ROOT + '/' + area}`  |  {len(data[area])} files\n\n")
            out.write("## Files (all layers & depths, sorted by path)\n\n")
            for rel, size, desc, _ in data[area]:
                out.write(f"- `{rel}`  ({size:.1f} KB)\n")
                if desc:
                    out.write(f"  → {desc}\n")
        print(f"  {SLUG[area]}.md written ({len(data[area])} entries).")
    
    print("DONE.")

if __name__ == "__main__":
    main()
