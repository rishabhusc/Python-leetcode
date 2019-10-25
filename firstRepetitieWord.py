import re

st = 'one                 t   wo,    thr e   e       ; four-five,    six'

ls = [i for i in re.split(r'\s+|[,;.-]\s*', st) if len(i) > 0]


def func(ls):
    d = {}
    for i in ls:
        if i in d:
            return (i)


        else:
            d[i] = 1
    return ""


if len(ls) > 1:
    print(func(ls))
else:
    print("")
