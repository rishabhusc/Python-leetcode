'''

Psychometric Test 

'''
arr=[1,3,5,6,8]
ll=[2,5,0]
il=[6,5,8]
lw=[]

for i in range(len(ll)):
    count=0
    for j in range(len(arr)):
        if ll[i]<=arr[j]<=il[i]:
            count+=1
    lw.append(count)
print(lw)

