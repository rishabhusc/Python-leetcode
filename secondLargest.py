a=[5,4,6,5,9,0,1,11]
first,second=-float('inf'),-float('inf')
for i in a:
    if i>first:
        second=first
        first=i
    elif i>second:
        second=i
print(second,first)