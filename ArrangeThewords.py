from collections import OrderedDict
str="I love to code."
str=str[:-1]
str=str.lower()
x=str.split()
d=OrderedDict()
for i in x:
    a=len(i)
    if a not in d:
        d[a]=[]
    d[a].append(i)
k=sorted(d.items(),key=lambda x:x[0])
ls=[]
for i in k:
    ls.extend(i[1])
xx=(' '.join(ls))
xx+="."
xx=xx[0].upper()+xx[1:]
print(xx)
