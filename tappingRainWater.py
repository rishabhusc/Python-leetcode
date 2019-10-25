n=[0,1,0,2,1,0,1,3,2,1,2,1]
watr=0
for i in range(1,len(n)):
    lmax=max(n[0:i])
    rmax=max(n[i:len(n)])

    curCap=min(lmax,rmax)

    waterCur=curCap-n[i]
    if waterCur>0:
        watr+=waterCur
print(watr)
