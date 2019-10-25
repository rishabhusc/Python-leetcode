A = [1, 2, 3, 5]
B = [6, 7, 8, 9]
C = [10, 11, 12]
def helper(a,b):
    n=len(a)
    m=len(b)
    i=0
    j=0
    d=[]
    while i<n and j<m:
        if a[i]<b[j]:
            d.append(a[i])
            i+=1
        else:
            d.append(b[j])
            j+=1
    while i<n:
        d.append(a[i])
        i+=1
    while j<m:
        d.append(b[j])
        j+=1
    return d
t=helper(A,B)
print(helper(t,C))