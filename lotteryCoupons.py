n=12
ls=[0]*n
for i in range(n+1):
    if i<10:
        ls[i]+=1
    else:
        s=str(i)
        a=sum([int(i) for i in s])
        ls[int(a)]+=1
x=(max(ls))
count=0
for i in ls:
    if i==x:
        count+=1
print(count)
