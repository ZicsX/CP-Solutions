from math import gcd
from functools import reduce

for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    g = reduce(gcd, A)
    count = 0
    cur = 0
    for i in A:
        cur = gcd(cur, i)
        if cur == g:
            count += 1
            cur = 0
    print("YES" if count >= K else "NO")
