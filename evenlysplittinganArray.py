arr=[1,2,3,4,6]
for i in range(1,len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
        print(i)
'''
second solution
'''
leftarr=sum(arr)
rightsum=0
for i in range(len(arr)-1,-1,-1):
    rightsum+=arr[i]
    leftarr-=arr[i]
    if rightsum==leftarr:

        print(i)
