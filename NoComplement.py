n=0
def nocomplement(n):
    st=bin(n)[2:]
    print(st)
    st=st.replace("1","*")
    st=st.replace("0","1")
    st=st.replace("*","0")
    return int(st,2)



print(nocomplement(0))


