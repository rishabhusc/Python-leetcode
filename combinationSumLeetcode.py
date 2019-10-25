arr=[2,4]
target=6
def combinationSum(arr,target):
    result=[]
    arr.sort()
    def findcandidate(temp,arr,target):
        for i in arr:
            if i>target:
                break
            temp.append(i)
            if i==target:
                result.append(temp.copy())
                temp.pop()
                break
            else:
                index=arr.index(i)
                findcandidate(temp,arr[index:],target-i)
                temp.pop()

    findcandidate([],arr,target)
    return result


print(combinationSum(arr,target))

