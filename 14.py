def f(x, q):
    s = 0
    x = x[::-1]
    for i in range(0, len(x)):
        s += x[i] * q ** i
    return s


for x in range(37):
    a1 = f([22, 15, x, 7, 2], 37)
    a2 = f([29, x, 7, 34, 2], 37)
    d = a1 + a2
    if d % 536 == 0:
        print(d // 536, x)