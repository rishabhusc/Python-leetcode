str1 = "gksrek"
str2 = "geeksforgeeks"
def isSubSeq(str1,str2,m,n):
    if m==0:return True
    if n==0:return False
    if str1[m-1]==str2[n-1]:
        return isSubSeq(str1,str2,m-1,n-1)
    return isSubSeq(str1,str2,m,n-1)
print(isSubSeq(str1,str2,len(str1),len(str2)))

def secondApproach(str1,str2,m,n):
    i=0
    j=0
    while i<m and j<n:
        if str1[i]==str2[j]:
            i+=1
        j+=1
    return i==m
print(secondApproach(str1,str2,len(str1),len(str2)))
