for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    Y = 0
    for i in range(30):
        m = 0
        for j in range(n):
            m |= 1 << ((a[j] >> i) & 1)
        if m != 3:
            continue
        t = x
        if t & (1 << i):
            t ^= 1 << i
            for j in range(i - 1, -1, -1):
                t |= 1 << j
        Y = max(Y, t)
    print(Y)
