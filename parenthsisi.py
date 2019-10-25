a="jamadamja"
def findmaxPal(a):
    ls=[[False for j in range(len(a))]for i in range(len(a))]
    for i in range(len(a)):
        ls[i][i]=True
    maxLength=1
    start=0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            ls[i][i+1]=True
            maxLength=2
            start=i
    k=3
    while k<=len(a):
        i=0
        while i<len(a)-k+1:
            j=i+k-1
            if ls[i+1][j-1] and a[i]==a[j]:
                ls[i][j]=True
                if k>maxLength:
                    maxLength=k
                    start=i

            i+=1
        k+=1
    return a[start:start+maxLength]
print(findmaxPal(a))