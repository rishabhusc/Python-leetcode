'''

Minimum price to the owner

'''

num=[4,9,2,3]
am=num[0]
min=num[0]
for i in range(1,len(num)):
    am+=max(0,num[i]-min)
    print(max(0,num[i]-min))

    if num[i]<min:
        min=num[i]
print(am)




