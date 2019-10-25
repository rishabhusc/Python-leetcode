def josephus(ls, skip):
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        print(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    print('survivor: ', ls[0])

josephus([1,2,3,4,5,6,6,7],3)