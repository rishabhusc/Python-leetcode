st="([)]"
def funcc(st):
    stk=[]
    for i in st:
        if i in "([{":
            stk.append(i)
            continue
        elif i==")":
            if stk[-1]=="(":
                stk.pop()
            else:
                return -1

        elif i=="]":
            if stk[-1]=="[":
                stk.pop()
            else:
                return -1

        elif i=="{":
            if stk[-1]=="}":
                stk.pop()
            else:
                return -1
        else:
            return -1
    if len(stk)!=0:
        return -1
    else:
        return 1

print(True if funcc(st)==1 else False)



