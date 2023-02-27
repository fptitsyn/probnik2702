import sys
from functools import lru_cache

sys.setrecursionlimit(1000000000)

@lru_cache()
def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 2 != 0:
        return 1 + f(n - 1)
    return f(n // 2)

c = 0
for i in range(1, 500_000_000 + 1):
    k = f(i)
    if k == 5:
        c += 1

print(c)