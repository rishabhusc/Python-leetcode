n=2
res = []
size = 1 << n
for i in range(size):
    res.append((i >> 1) ^ i)
print(res)
