'''
Shortest key press
'''
import sys
def fn(arr):

    cur=0
    start=0
    min=-sys.maxsize
    elem=""
    for i in arr:
        if i[1]-start>min:
            elem=i[0]
            min=i[1]-start
        start=i[1]
    return(chr(elem+ord('a')))


arr=[[0,2],[1,5],[0,9],[2,15]]
print(fn(arr))