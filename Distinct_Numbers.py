def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    m = 0
    for i in range(n):
        m = max(m, a[i])
    cnt = 1
    c1 = 0
    c2 = 0
    for i in range(1, 2 * n + 1):
        if cnt > k:
            break
        if i not in s:
            m = max(m, i)
            c1 += m - i
            cnt += 1
    cnt = 1
    for i in range(1, 2 * n + 1):
        if cnt > (k - 1):
            break
        if i not in s:
            c2 += (2 * n) - i
            cnt += 1
    print(max(c1, c2))


for _ in range(int(input())):
    solve()
