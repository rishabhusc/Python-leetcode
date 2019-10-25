num=[1,2,3,4,5]
output=[1]*len(num)
prod=1
for i in range(len(num)):
    output[i]*=prod
    prod*=num[i]
prod=1
for i in range(len(num)-1,-1,-1):
    output[i]*=prod
    prod*=num[i]
print(output)