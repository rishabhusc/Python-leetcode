s="abcde"
sa=set()
for i in range(len(s)):
    for j in range(i,len(s)+1):
        if len(s[i:j])>0:
            sa.add(s[i:j])
print((sorted(sa,key=lambda x:len(x),reverse=True)))