#!/usr/bin/env python3
"""
MusGo-OS 2in1 - Audit Extractor v4 (STRICT)
==========================================
Perbaikan v4 (koreksi inflasi v3):
  - same_domain DIKETATKAN: domain repo HARUS sama dengan domain blueprint
  - nama yang cocok lintas-domain -> cross_domain / ambiguous (TIDAK dihitung terintegrasi)
  - tambah metrik inflasi: repo_path unik vs jumlah blueprint yang dipenuhi
  - subdir kosong tidak boleh jadi dasar pencocokan longgar

Verdict (kuat -> lemah):
  exact            domain+layer+subdir+name
  flattened        domain+subdir+name   (layer tidak ada di path repo)
  same_layer       domain+layer+name    (subdir beda)
  same_domain      domain+name          (layer & subdir beda)
  consolidated     <subdir>.py menggantikan banyak file
  ---- batas terintegrasi ----
  cross_domain     name ada, tapi domain repo BEDA  -> butuh tinjauan
  ambiguous        name ada di >1 domain, tak ada yang cocok -> butuh tinjauan
  missing          tidak ada sama sekali

Zero-dependency.
"""
import os, re, csv, json, sys
from collections import OrderedDict, defaultdict

BP_ROOT   = "/root/projects/Blueprints_MusGo-OS_2in1"
SRC_STRUCT= os.path.join(BP_ROOT, "STRUKTUR REPOSITORY FINAL.md")
REPO_ROOT = "/root/Repository MusGo-OS_2in1-main"
OUT       = "/root/projects/Project-Progress/Knowledge/Extract"

ICON_DIR, ICON_PY, ICON_DOC, ICON_LOCK = "\U0001F4C1","\U0001F40D","\U0001F4C4","\U0001F510"
ICONS=(ICON_DIR,ICON_PY,ICON_DOC,ICON_LOCK)
NOISE={"__init__.py"}

def clean(l):
    for ch in "│├└─|`": l=l.replace(ch,"")
    for ic in ICONS:    l=l.replace(ic,"")
    return re.sub(r"\s*#.*$","",l).strip().strip("/").strip()

def kind(l):
    if ICON_PY in l:  return "py"
    if ICON_DIR in l: return "dir"
    if ICON_DOC in l: return "doc"
    if ICON_LOCK in l:return "security"
    return None

def val(n): return bool(re.match(r"^[\w\-\.\+]+$",n)) and "." in n

def parse(path):
    """v6: ROOT-LEVEL detection by icon-at-column-0.
    Root dir (any name: *_domain, specifications, system, extensions, ...)
    resets the whole context. Fixes the 'last domain wins' mis-attribution."""
    rows,cd,cl,cs=[],None,None,None
    for raw in open(path,encoding="utf-8",errors="replace"):
        if not raw.strip(): continue
        k=kind(raw)
        if k is None: continue
        n=clean(raw)
        if not n: continue
        stripped=raw.lstrip()
        is_root = bool(stripped) and stripped[0] in ICONS
        if k=="dir":
            if is_root:                      cd,cl,cs=n,None,None   # ANY root dir
            elif re.match(r"^layer_\d\d_",n):cl,cs=n,None
            else:                            cs=n
            continue
        if cd is None or not val(n): continue
        rows.append({"domain":cd,"layer":cl or "","subdir":cs or "","name":n,
                     "kind":k,"ext":os.path.splitext(n)[1].lower()})
    return rows

def index(root):
    idx=defaultdict(list); allf=[]
    for dp,dns,fns in os.walk(root):
        if ".git" in dp.split(os.sep): continue
        for fn in fns:
            rel=os.path.relpath(os.path.join(dp,fn),root)
            allf.append(rel); idx[fn].append(rel)
    return idx,allf

def domain_of(rel): return rel.split(os.sep)[0]

def match(r, repo_idx):
    hits=repo_idx.get(r["name"],[])
    if not hits: return None,"missing"
    dom=r["domain"]; lay=r["layer"]; sub=r["subdir"]
    same_dom=[h for h in hits if domain_of(h)==dom]
    sep=os.sep

    if same_dom:
        if lay and sub:
            for h in same_dom:
                if lay in h and f"{sep}{sub}{sep}" in h: return h,"exact"
        if sub:
            for h in same_dom:
                if f"{sep}{sub}{sep}" in h: return h,"flattened"
        if lay:
            for h in same_dom:
                if lay in h: return h,"same_layer"
        return same_dom[0],"same_domain"

    # tidak ada di domain yang sama
    doms={domain_of(h) for h in hits}
    if len(doms)==1: return hits[0],"cross_domain"
    return hits[0],"ambiguous"

def main():
    bp=parse(SRC_STRUCT)
    py=[r for r in bp if r["kind"]=="py" and r["name"] not in NOISE]
    doc=[r for r in bp if r["kind"] in ("doc","security") and r["name"] not in NOISE]
    repo_idx,repo_files=index(REPO_ROOT)
    by_dir=defaultdict(list)
    for rel in repo_files:
        p=rel.split(os.sep)
        if len(p)>=2: by_dir[p[-2]].append(rel)

    print(f"[1] Blueprint: {len(bp)} entries | .py {len(py)} | doc/config {len(doc)}")
    print(f"[2] Repo: {len(repo_files)} files")

    os.makedirs(OUT,exist_ok=True)
    with open(os.path.join(OUT,"01_blueprint_index.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["domain","layer","subdir","name","kind","ext"])
        w.writeheader(); w.writerows({k:r[k] for k in w.fieldnames} for r in bp)
    with open(os.path.join(OUT,"02_repo_index.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["relpath","basename","ext"])
        for rel in sorted(repo_files):
            w.writerow([rel,os.path.basename(rel),os.path.splitext(rel)[1].lower()])

    POS=("exact","flattened","same_layer","same_domain","consolidated")
    stat=OrderedDict((k,0) for k in POS+("cross_domain","ambiguous","missing"))
    rows=[]
    for r in py:
        p,v=match(r,repo_idx)
        if v=="missing" and r["subdir"]:
            for h in by_dir.get(r["subdir"],[]):
                if os.path.basename(h)==f"{r['subdir']}.py":
                    p,v=h,"consolidated"; break
        if v=="consolidated" and p and domain_of(p)!=r["domain"]:
            v="cross_domain"
        stat[v]+=1
        rows.append({"domain":r["domain"],"layer":r["layer"],"subdir":r["subdir"],
                     "name":r["name"],"repo_path":p or "","verdict":v,
                     "integrated":"yes" if v in POS else "no"})
    with open(os.path.join(OUT,"03_module_mapping.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["domain","layer","subdir","name","repo_path","verdict","integrated"])
        w.writeheader(); w.writerows(rows)

    dstat={"found":0,"cross_domain":0,"ambiguous":0,"missing":0}; drows=[]
    for r in doc:
        p,v=match(r,repo_idx)
        if not p: v="missing"
        elif v not in POS: v=v
        else: v="found"
        dstat[v]=dstat.get(v,0)+1
        drows.append({"domain":r["domain"],"layer":r["layer"],"subdir":r["subdir"],
                      "name":r["name"],"repo_path":p or "","verdict":v})
    with open(os.path.join(OUT,"03b_doc_config_mapping.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["domain","layer","subdir","name","repo_path","verdict"])
        w.writeheader(); w.writerows(drows)

    layers=OrderedDict()
    for r in rows:
        d=layers.setdefault((r["domain"],r["layer"] or "-"),
            OrderedDict((k,0) for k in POS+("cross_domain","ambiguous","missing","total")))
        d["total"]+=1; d[r["verdict"]]+=1
    with open(os.path.join(OUT,"04_layer_summary.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["domain","layer","py_total","exact","flattened","same_layer","same_domain",
                    "consolidated","cross_domain","ambiguous","missing","integrated","coverage_pct"])
        for (dom,lay),d in layers.items():
            integ=sum(d[k] for k in POS)
            pct=integ/d["total"]*100 if d["total"] else 0
            w.writerow([dom,lay,d["total"]]+[d[k] for k in POS]+
                       [d["cross_domain"],d["ambiguous"],d["missing"],integ,f"{pct:.1f}"])

    # --- v5: pisahkan cross_domain/ambiguous berbasis keunikan nama di blueprint ---
    from collections import Counter as _C
    namecnt=_C(r["name"] for r in py)
    stat2=OrderedDict((k,0) for k in POS+("relocated","name_duplicate","ambiguous","missing"))
    for row in rows:
        v=row["verdict"]
        if v=="cross_domain":
            v="relocated" if namecnt[row["name"]]==1 else "name_duplicate"
            row["verdict"]=v
        elif v=="ambiguous":
            v="ambiguous"
        row["integrated"]="yes" if v in POS else ("likely" if v=="relocated" else "no")
        stat2[v]+=1
    stat=stat2
    with open(os.path.join(OUT,"03_module_mapping.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["domain","layer","subdir","name","repo_path","verdict","integrated"])
        w.writeheader(); w.writerows(rows)

    integrated=sum(stat[k] for k in POS)
    likely=stat.get("relocated",0)
    n=len(py)
    paths=[r["repo_path"] for r in rows if r["repo_path"]]
    uniq=len(set(paths))
    summary={
        "blueprint_entries":len(bp),
        "py_expected":n,
        "doc_config_expected":len(doc),
        "repo_files":len(repo_files),
        "py_exact":stat["exact"],"py_flattened":stat["flattened"],
        "py_same_layer":stat["same_layer"],"py_same_domain":stat["same_domain"],
        "py_consolidated":stat["consolidated"],
        "py_integrated":integrated,
        "py_cross_domain_relocated":stat.get("relocated",0),
        "py_name_duplicate":stat.get("name_duplicate",0),
        "py_ambiguous":stat.get("ambiguous",0),
        "py_integrated_likely":integrated+likely,
        "coverage_pct_with_relocated":round((integrated+likely)/n*100,1) if n else 0,
        "py_missing":stat["missing"],
        "coverage_pct":round(integrated/n*100,1) if n else 0,
        "strict_path_pct":round(stat["exact"]/n*100,1) if n else 0,
        "inflation_unique_repo_paths":uniq,
        "inflation_ratio":round(integrated/uniq,2) if uniq else 0,
        "doc_found":dstat.get("found",0),"doc_missing":dstat.get("missing",0),
        "doc_coverage_pct":round(dstat.get("found",0)/len(doc)*100,1) if doc else 0,
        "methodology":"STRICT: cross_domain & ambiguous NOT counted as integrated; inflasi diukur via unique repo paths",
    }
    print("\n=== SUMMARY v4 STRICT ==="); print(json.dumps(summary,indent=2))
    json.dump(summary,open(os.path.join(OUT,"summary.json"),"w",encoding="utf-8"),indent=2)
    print("\n[OK] ->",OUT)

if __name__=="__main__": main()
