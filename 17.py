f = open("17.txt")
a = [int(i) for i in f]

b = ""
for i in a:
    if i % 35 == 0:
        b += str(i)


sum35 = 0
for i in range(len(b)):
    sum35 += int(b[i])

ans = []
for i in range(len(a) - 1):
    if (a[i] > sum35 >= a[i + 1] and hex(a[i + 1])[-2:] == "ef") or (a[i + 1] > sum35 >= a[i] and hex(a[i])[-2:] == "ef"):
        ans.append(a[i] + a[i + 1])

print(len(ans), min(ans))