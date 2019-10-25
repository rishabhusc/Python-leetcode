s = "AAAAAAAAAAA"
d={}
i=0
lw=[]
while i+10<=len(s):
    a=s[i:i+10]
    if a in d:
        d[a]+=1
    else:
        d[a]=1

    if d[a]>=1:
        lw.append(a)

    i+=1
print(d)
