arr=[0,1,0]
count=0
minvalue=0
val=0
d={}
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
    else:
        count-=1
    if minvalue==count:
        val=i+1
    if count in d:
        val=max(val,i-d[count])
    else:
        d[count]=i
print(val)