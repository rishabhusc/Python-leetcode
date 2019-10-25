andria=[123,543]
maria=[321,279]

mv=0
flag=True
longer=andria


for i in range(len(maria)):
    st=str(andria[i])
    mr=str(maria[i])
    if len(st)==len(mr):
        if st==mr:
            mv+=0
        else:
            for i in range(len(st)):
                mv+=abs((int(st[i])-int(mr[i])))



print(mv)



