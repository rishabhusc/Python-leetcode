a=[1,5,3,4,2]
diff=2
count=0
for i in range(len(a)):
    for j in range(i,len(a)):
        if abs(a[i]-a[j])==diff:
            count+=1
print(count)


def funct(arr,k):
    count = 0
    n=len(arr)
    end = 0
    beg = 0
    arr.sort()
    while beg < n:
        if arr[beg] - arr[end] == k:
            count += 1
            end += 1
            beg += 1

        elif arr[beg]-arr[end]>k:
            end += 1
        else:
            beg += 1
    return count
print(funct(a,diff))



