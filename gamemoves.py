st="wwwwbbb"
def saa(st):
    wmoves=0
    bmoves=0
    i=0
    while i <(len(st)):
        if st[i]=="w":
            count=0
            while i<len(st) and st[i]=="w":
                count+=1
                i+=1
            wmoves+=max(count-2,0)
        else:
            count = 0
            while i < len(st) and st[i] == "b":
                count += 1
                i += 1
            bmoves += max(count - 2, 0)

    if wmoves>bmoves:
        return "wendy"
    else:
        return "bob"


print(saa(st))



