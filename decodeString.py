a="3[a2[c]]"

def solution(a):
    num_stack=[]
    word_stack=[]
    num=''
    word=''
    for i in a:
        if i.isdigit():
            num+=i
        elif i.isalpha():
            word+=i
        elif i=="[":
            num_stack.append(int(num))
            word_stack.append(word)
            num=''
            word=''
        elif i=="]":
            word=word_stack.pop()+word*num_stack.pop()
    return word
print(solution(a))