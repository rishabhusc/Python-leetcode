'''

Select max difference

'''


arr=[5,9,3,0]
diff=arr[1]-arr[0]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]-min>diff:
        diff=arr[i]-min
    if arr[i]<min:
        min=arr[i]
print(diff)
