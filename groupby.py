from itertools import groupby
n=2
x="Y"*n
a=["na","na","na","na","na","na","na","na","YnaY"]
ls=([ len(list(v)) for k,v in groupby(a) if k==x])
if len(ls)>0:
    print(max(ls))
else:
    print(0)

