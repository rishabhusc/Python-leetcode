a=[1,2,3,4,5]
b=[8,9,10]
n=len(a)
m=len(b)
ls=[None]*((n+m))
i=0
j=0
k=0
while i<n and j<m:
    if a[i]<b[j]:
        ls[k]=a[i]
        i+=1
    else:
        ls[k]=b[j]
        j+=1
    k+=1
while i<n:
    ls[k]=a[i]
    k+=1
    i+=1
while j<m:
    ls[k]=b[j]
    j+=1
    k+=1
print(ls)

