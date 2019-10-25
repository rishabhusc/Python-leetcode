a=[1,2,3,4,5]
target=8
ls=set()
for i in range(len(a)-2):
    beg=i+1
    end=len(a)-1
    while beg<end and a[i]<a[beg]<a[end]:
        if a[i]+a[beg]+a[end]<=target:
            ls.add((a[i],a[beg],a[end]))
            beg+=1

        else:
            end-=1


for i in range(len(a)-2):
    beg=i+1
    end=len(a)-1
    while beg<end and a[i]<a[beg]<a[end]:
        if a[i]+a[beg]+a[end]<=target:
            ls.add((a[i],a[beg],a[end]))
            end-=1
        else:
            beg+=1

ls=(list(ls))
ls.sort()
print(ls)


