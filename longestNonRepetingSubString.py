s="abcddabc"



def funct(s):

    ml=0
    def helper(s,start):
        d=set()
        for i in range(start,len(s)):
            if s[i] not in d:
                d.add(s[i])
            else:
                return i-start
        return len(s)-start

    for i in range(len(s)):
        ml=max(ml,helper(s,i))
    return ml


print(funct(s))


def longestsubstringWithNoRepeatingChar(s):
    seen={}
    start=0
    ml=0
    for i in range(len(s)):
        if s[i] in seen:
            start=max(start,seen[s[i]]+1)
        seen[s[i]]=i
        ml=max(ml,i-start+1)
    return ml
print(longestsubstringWithNoRepeatingChar(s))

