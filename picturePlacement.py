arr=[0,1,2,3,4]
placement=[0,1,2,1,2]
ls=[]
for i in range(len(arr)):
    ls.insert(placement[i],arr[i])
print(ls)