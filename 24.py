f = open("24.txt")
a = f.readline()

k = 0
kmax = 0
dot = 0
for i in range(len(a) - 1):
    if a[i] not in "AEIOUY":
        if a[i] == ".":
            dot += 1
        k += 1
    else:
        if dot >= 6:
            kmax = max(k, kmax)
        k = 0
        dot = 0

print(kmax)