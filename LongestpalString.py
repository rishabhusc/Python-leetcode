nums=[2,3,-2,4]
ans=-float('inf')
maxValue=1
minValue=1
for i in nums:
    if i>0:
        minValue=min(1,minValue*i)
        maxValue*=i
    elif i==0:
        maxValue=0
        minValue=1
    elif i<0:
        prod=maxValue
        maxValue=minValue*i
        minValue=prod*i
    ans=max(maxValue,ans)
    if maxValue<=0:
        maxValue=1
print(ans)