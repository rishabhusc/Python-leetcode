import heapq
arr=["i", "love", "leetcode", "i", "love", "coding"]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(sorted(d.items(),key=lambda x:(-x[1],x[0]),reverse=True))
