def d(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    if len(a) == 3:
        return True
    return False


ans = []
for m in range(1, 1000):
    s = ">" + "1" * 17 + "2" * 34 + "3" * m
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">3" in s:
            s = s.replace(">3", "1>", 1)

    a = [int(i) for i in s if i != ">"]
    if d(sum(a)):
        print(m)
        ans.append(m)


print(min(ans))
