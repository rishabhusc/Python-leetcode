num=[1,1,2,3]
val = [0] * 1001
for i in num:
    val[i] += 1

counter = 0
val = val[::-1]
ans = []
for i in val:
    if i > 0:
        counter += i
        ans.append(counter)
print(ans[::-1])
