n = 457892
def helper(n):
    c=0
    sumEven=0
    sumOdd=0
    while n!=0:
        if c%2==0:
            sumEven+=n%10
        else:
            sumOdd+=n%10
        c+=1
        n=n//10
    print(sumOdd,sumEven)
print(helper(n))