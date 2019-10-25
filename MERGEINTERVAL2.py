import heapq
arr=[[0, 30],[5, 10],[15, 20]]


arr.sort(key=lambda x:x[0])
heap=[]
for i in arr:
    if not heap or heap[0]>i[0]:
        heapq.heappush(heap,i[1])
    else:
        heapq.heapreplace(heap,i[1])
print(len(heap))