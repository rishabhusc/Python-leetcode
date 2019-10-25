arr=[1, 2, 2, 3, 1]
d={}
for i in range(len(arr)):
    if arr[i] not in d:
        d[arr[i]]=[]
    d[arr[i]].append(i)
ml=0
print(sorted(d.values(),key=lambda x:len(x),reverse=True))

sm=[]
for k,v in d.items():
    if ml==len(v) and len(v)>1:
        sm.append(v[len(v)-1]-v[0]+1)

if ml==1:
    print(1)
else:
    print(sorted(sm)[0])


