arr = [2,3,-2,4]
ans=-1
maxValue=1
minValue=1
for i in range(len(arr)):
    if arr[i]>0:
        maxValue=maxValue*arr[i]
        minValue=min(1,minValue*arr[i])
    elif arr[i]==0:
        minValue=1
        maxValue=0
    else:
        prevmax=maxValue
        maxValue*=arr[i]
        minValue=arr[i]*prevmax
    ans=max(ans,maxValue)
    if maxValue<=0:
        maxValue=1
print(ans)

