import re
f = open('test.txt','r').read().strip()
zipCode = re.findall('(\d.+)\n([A-Z].+) ',f)
res = set()
for line in zipCode:
    s = line[0]+' '+line[1]
    res.add(s)
fhand = open('California.txt','a')
for line in res:
    fhand.write(line+'\n')
fhand.close()
