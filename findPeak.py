nums = [1,2]
beg=0
end=len(nums)-1

def binarSearch(nums,beg,end):
    mid=(beg+end)//2
    if beg==end or nums[mid]>max(nums[mid-1],nums[mid+1]):
        return mid
    elif nums[mid+1]>nums[mid]:
        return binarSearch(nums,mid,end)
    else:
        return binarSearch(nums,beg,mid)
print(binarSearch(nums,beg,end))