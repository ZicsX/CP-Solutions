import bisect


def discrete(li):
    a = li.copy()
    a.sort()
    a = list(set(a))
    for i in range(len(li)):
        li[i] = bisect.bisect_left(a, li[i])
    return li


for _ in range(int(input())):
    n = int(input())

    strength = [0] * n
    r = [0] * n
    c = [0] * n
    p = []

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = discrete(a)
    b = discrete(b)

    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))

    for i in range(n):
        r[b[i]] = i
        c[a[i]] = b[i]
        strength[i] = a[i] + b[i]

    for i in range(n):
        p.insert(bisect.bisect_right(p, c[i]), c[i])
        strength[r[c[i]]] -= bisect.bisect_left(p, c[i])

    print(strength.count(max(strength)))
