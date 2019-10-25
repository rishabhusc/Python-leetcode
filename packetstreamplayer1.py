def funct(arr):


    def highestPowerof2(n):
        if (n < 1):
            return 0

        res = 1
        for i in range(n):
            curr = 1 << i
            if (curr > n):
                break
            res = curr
        return res


    mxvalue=-1
    cf=0
    m=highestPowerof2(arr[0])
    if m>mxvalue:
        mxvalue=m
    if arr[0]>m:
        cf=arr[0]-m
    for i in range(1,len(arr)):
        w=(arr[i]+cf)
        m=highestPowerof2(w)
        if m>mxvalue:
            mxvalue=m

        cf=arr[i]-m
    return mxvalue


arr=[0,986,0]
print(funct(arr))



