from fnmatch import *


def s(n):
    a = 0
    b = 0
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            a += int(n[i])
        b += int(n[i])

    return [a, b]


for i in range(0, 12500000):
    if fnmatch(str(i), "124*5*79"):
        k = s(i)
        if i % k[0] == 0:
            print(i, k[1])
