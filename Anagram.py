'''

       Anagram of strings :

'''

from collections import OrderedDict
arr=['code','doce','ecod','framer','frame']
d=OrderedDict()
for i in arr:
    a=''.join(sorted(i))
    if a not in d:
        d[a]=(i)
ls=[]
for k,v in d.items():
    ls.append(v)
print(sorted(ls))