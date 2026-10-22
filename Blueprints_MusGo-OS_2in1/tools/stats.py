import json, collections
d = json.load(open('tools/blueprint_manifest.json', encoding='utf-8'))
L = []
L.append("files: %d" % len(d))
c = collections.Counter((x['size'], x['lines']) for x in d if x['lines'] > 0)
dups = [k for k, v in c.items() if v > 1]
L.append("dup groups: %d  files: %d" % (len(dups), sum(c[k] for k in dups)))
junk = [x for x in d if x['title'].startswith('=')]
L.append("junk titles: %d" % len(junk))
for x in junk[:8]:
    L.append("   " + x['path'])
L.append("empty titles: %d" % sum(1 for x in d if not x['title']))
L.append("no-excerpt text: %d" % sum(1 for x in d if x['kind']=='text' and not x['excerpt']))
open('tools/report.txt','w',encoding='utf-8').write("\n".join(L))
