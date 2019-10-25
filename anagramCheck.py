st1='anagram'
st2='naagram'

ls=[0]*26
def fun(st1,st2):
    if len(st1)==len(st2):
        for i in st1:
            ls[ord(i)-ord('a')]+=1
        for j in st2:
            ls[ord(j)-ord('a')]-=1

        if max(ls)==0 and min(ls)==0:
            return True
        else:
            return False
    else:
        return False

print(fun(st1,st2))