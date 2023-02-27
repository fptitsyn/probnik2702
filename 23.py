import sys
from functools import lru_cache
sys.setrecursionlimit(100000)


@lru_cache()
def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x + 5, y) + f(x * 3, y)


c = 0
for i in range(1000, 1025):
    if f(1, i) == 8:
        c += 1

print(c)