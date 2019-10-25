def numSubarrayProductLessThanK( nums, k):
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        print(prod,right)
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
nums = [1,1,1]
k = 1
print(numSubarrayProductLessThanK( nums, k))



