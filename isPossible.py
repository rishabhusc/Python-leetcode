source=(2,4)
des=(6,18)
ls=[]
ls.extend(source)
ls2=[]
ls2.extend(des)

def func(ls,ls2):

    for i in ls2:
        result=[]
        def faq(ls,i,temp):
            for j in ls:
                if j>i:
                    break
                temp.append(i)
                if j==i:
                    result.append(temp.copy())
                    temp.pop()
                    break
                else:
                    faq(ls[ls.index(j):],i-j,temp)
        faq(ls,i,[])
        if len(result)==0:
            return ("Not Possible")
    return "Possible"

print(func(ls,ls2))

