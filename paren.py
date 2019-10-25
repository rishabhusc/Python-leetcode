a=[2,3,4,5,6,70]
target=9
d={}
for i in range(len(a)):
    if a[i] in d:
        print(d[a[i]],i)
    else:
        d[target-a[i]]=i