grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxRow=[float('-inf')]*len(grid)
maxCol=[float('-inf')]*len(grid[0])
maxIncrese=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        curValue=grid[i][j]
        if curValue>maxRow[i]:
            maxRow[i]=curValue
        if curValue>maxCol[j]:
            maxCol[j]=curValue


for i in range(len(grid)):
    for j in range(len(grid[0])):
        maxIncrese+=min(maxRow[i],maxCol[i])-grid[i][j]
print(maxIncrese)