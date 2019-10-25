arr=[0,1,1,0,1,1,0,0]
d={}
count=0
maxiss=0
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
    else:
        count-=1
    if count==0:
        maxiss=i+1
    if count in d:
        maxiss=max(maxiss,i-d[count])
    else:
        d[count]=i
print(maxiss)