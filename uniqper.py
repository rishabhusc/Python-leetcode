from itertools import permutations
arr=[1,1,2]
s=set()
for i in permutations(arr,len(arr)):

    s.add(i)
print(list(s))
