arr=[1,2,3,4,5,6,7,8,9]
arr.sort(reverse=True)
beg=0
end=len(arr)-1
ls=[]
while beg<end:
    ls.append(arr[beg])
    beg+=1
    ls.append(arr[end])
    end-=1
if len(arr)%2!=0:
    ls.append(arr[beg])
print(ls)


