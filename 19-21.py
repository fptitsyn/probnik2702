def f(s1, s2, c, m):
    if s1 + s2 >= 231:
        return c % 2 == m % 2
    if c > m:
        return 0
    a = [f(s1 + 2, s2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 + 2, c + 1, m), f(s1, s2 * 2, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(a)
    else:
        return all(a)


s1 = 17
for s2 in range(1, 214):
    for m in range(1, 10):
        if f(s1, s2, 0, m):
            print(s2, m)
            break