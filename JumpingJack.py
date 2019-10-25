'''
arr=set()
arr.add(1)
k=6
arr.add(k)
arr=list(arr)
target=1100

def fun(arr,target):
    result=[]

    def elem(arr,target,temp):
        for i in arr:
            if i>target:
                break
            temp.append(i)
            if i==target:
                result.append(temp.copy())
                temp.pop()
                break
            else:
                elem(arr[arr.index(i):],target-i,temp)
                temp.pop()

    elem(arr,target,[])
    return len(sorted(result,key=lambda x:len(x))[0])


print(fun(arr,target))

'''
'''
Code is flawd
'''
j=3
k=8
count=0
i=0
while i<=k:
    if i==k:
        print(count)
        break
    elif i+j<=k:
        count+=1
        i=i+j
    elif i+1<=k:
        count+=1
        i=i+1


