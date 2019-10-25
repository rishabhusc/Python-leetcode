X = "AGGTAB"
Y = "GXTXAYB"
def lcs(X,Y):
    n=len(Y)
    m=len(X)
    L=[[0 for i in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                 L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    return L[m][n]
print(lcs(X,Y))
