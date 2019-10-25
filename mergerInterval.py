arr=[[1,3],[2,6],[8,10],[15,18]]
arr.sort()
merger=[]
for i in arr:
    if not merger or merger[-1][-1]<i[0]:
        merger.append(i)
    else:
        merger[-1][-1]=max(merger[-1][-1],i[0])
print(merger)