s="abca"
def helper(s):
    beg=0
    end=len(s)-1
    while beg<end:
        if s[beg]!=s[end]:
            return isPalindrome(s,beg+1,end) or isPalindrome(s,beg,end-1)
        beg+=1
        end-=1

def isPalindrome(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

print(helper(s))