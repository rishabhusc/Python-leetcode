'''
Counting bits
'''
n=161
ls=[]
str=(bin(n)[2:])
ls.append(str.count("1"))
for i,k in enumerate(str):
    if k=="1":
        ls.append(i+1)
print(ls)