nums=[7,8,6,5]
def func(nums):
    d={}
    ls=[]
    for i in nums:
        st=bin(i)[2:].count("1")

        if st not in d:
            d[st]=[]
        d[st].append(i)
    for i in sorted(d.items(),key= lambda x:x[0]):
        lx=i[1]
        if len(lx)>1:
            lx.sort()
        ls.extend(lx)
    return ls


print(func(nums))
