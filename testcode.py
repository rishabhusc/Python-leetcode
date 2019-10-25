ls="abcde"
def reverseStr(st):
    # 1sr method
    output=''
    '''
    for i in st:
        output=i+output
    return output
    # 2nd method
    '''
    '''
    stack=[]
    for i in st:
        stack.append(i)
    output=''
    while len(stack)>0:
        output+=stack.pop()
    return output
    
    return st[::-1]
    
    beg=0
    end=int(len(st)/2)
    st=list(st)
    while beg<end:
        st[beg],st[len(st)-beg-1]=st[len(st)-beg-1],st[beg]
        beg+=1

    return st
    '''
    return ''.join(reversed(list(st)))
print(reverseStr(ls))
