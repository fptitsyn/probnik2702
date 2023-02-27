def f(n):
    b = bin(n)[2:]
    a = [int(i) for i in b][::-1]
    if sum(a) % 2 == 0:
        for i in range(0, 4):
            if a[i] == 0:
                a[i] = 1
            else:
                a[i] = 0
    else:
        for i in range(1, 5):
            if a[i] == 0:
                a[i] = 1
            else:
                a[i] = 0

    r = ""
    for i in a[::-1]:
        r += str(i)

    return int(r, 2)


minr = 10000
n = 0
for i in range(64, 1000):
    r = f(i)
    if r < minr:
        minr = r
        n = i

print(n, minr)