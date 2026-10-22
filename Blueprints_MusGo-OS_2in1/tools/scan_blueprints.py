import os, json, re, sys
from collections import Counter

ROOT = os.path.abspath('.')
TEXT_EXT = {'.md','.txt','.json','.csv','.yml','.yaml','.py','.js','.ts','.tsx','.jsx','.css','.html','.sh','.toml','.ini','.env','.glsl','.xml','.svg','.sql'}
SKIP_DIRS = {'.git','node_modules','__pycache__','dist','build','.next'}

def norm(p): return os.path.relpath(p, ROOT)

files=[]
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in SKIP_DIRS]
    for fn in fns:
        files.append(os.path.join(dp,fn))
files.sort()
print("TOTAL FILES:", len(files), flush=True)

STOP=set("""yang dan di ke dari untuk dengan pada ini itu adalah akan atau juga dalam tidak bisa oleh sebagai para lebih telah sudah agar karena seperti dapat serta secara namun tetapi jika maka saat bagi antara hanya harus kita kami anda mereka dia saya the and of to in for on with is are be by as at a it this that from we you they i""".split())

out=[]
for i,p in enumerate(files):
    rel=norm(p); ext=os.path.splitext(p)[1].lower()
    try: size=os.path.getsize(p)
    except Exception: size=0
    d={'path':rel,'ext':ext.lower(),'size':size,'lines':0,'title':'','headings':[],'excerpt':'','keywords':[],'kind':'binary'}
    if ext in TEXT_EXT and size<2_000_000:
        try:
            with open(p,'r',encoding='utf-8',errors='ignore') as f: txt=f.read()
        except Exception:
            txt=''
        if txt:
            d['lines']=txt.count('\n')+1
            hs=re.findall(r'^[ \t]{0,3}(#{1,4})[ \t]+(.+?)[ \t]*$', txt, re.M)
            if hs:
                d['headings']=[h[1].strip()[:120] for h in hs[:15]]
                d['title']=hs[0][1].strip()[:150]
            if not d['title']:
                for line in txt.splitlines():
                    if line.strip():
                        d['title']=line.strip()[:150]; break
            clean=re.sub(r'\s+',' ',re.sub(r'[#*`>\[\]()|]',' ',txt))
            d['excerpt']=clean.strip()[:400]
            words=[w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{3,}", txt)]
            cnt=Counter(w for w in words if w not in STOP)
            d['keywords']=[w for w,_ in cnt.most_common(12)]
            d['kind']='text'
    out.append(d)
    if i%50==0: print("...",i,flush=True)

os.makedirs('tools',exist_ok=True)
with open('tools/blueprint_manifest.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
print("DONE", len(out), flush=True)
