'''

Car pooling logic not the same Question
'''

arr=[4,5,6]

ls=[]
for i in arr:
    if i%2!=0:
        ls.append(0)
    else:

        def combinationSum(candidates, target):
            
            candidates.sort()
            ans = []

            def helper(candidates, target, t):
                if not target:
                    ans.append(t)
                    return
                for i, num in enumerate(candidates):
                    if target >= num:
                        helper(candidates[i:], target - num, t + [num])
                    else:
                        break

            helper(candidates, target, [])
            return ans


        candidates = [2, 4]
        target = i


        ls.append(len(combinationSum(candidates, target)))

print(ls)



