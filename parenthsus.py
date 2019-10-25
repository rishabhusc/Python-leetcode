def combinationSum( candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
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
candidates=[2,4]
target=6
print(len(combinationSum(candidates,target)))