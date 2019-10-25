'''

Finding sum in range queries

'''
i=0
j=5
k=-1
ls=[i for i in range(i,j+1)]
ls1=[i for i in range(j-1,k-1,-1)]
print(sum(ls)+sum(ls1))