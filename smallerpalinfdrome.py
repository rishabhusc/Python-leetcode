s="acca"
l=list(s)
if len(s)==0:
    print("Impossible")
else:
    beg=0
    end=len(s)-1
    ls=[]

    for i in range(end):
        sa=list(l)

        if sa[i]!="a":
            sa[i]="a"
            c=(''.join(sa)[::-1])
            if ''.join(sa)!=c and ''.join(sa)<s:
                print(''.join((sa)))
                break

    print("Impossible")
