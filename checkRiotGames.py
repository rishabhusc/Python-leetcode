from collections import deque
def bfs(grid, start, level):
    queue = deque([[start]])
    seen = set([start])
    level[start] = 0
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        # print(x,y)
        if grid[x][y] == "F":
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < int(a[0][1]) and 0 <= y2 < int(a[0][1]) and grid[y2][x2] != "W" and (x2, y2) not in seen:
                level[(x2, y2)] = level[(x, y)] + 1
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


a = []
# Below line read inputs from user using map() function
while True:
    try:
        a.append(input().split(','))
    except EOFError:
        break
# print(a)

b = [['B' for y in range(int(a[0][0]))] for x in range((int(a[0][1])))]

for i in a[1:]:
    if i[0] == "F":
        b[int(i[2])][int(i[1])] = 'F'
    if i[0] == "W":
        b[int(i[2])][int(i[1])] = 'W'

# print(b)
level = [None] * 10
path = bfs(b, (0, 0), 0)
print(path)
