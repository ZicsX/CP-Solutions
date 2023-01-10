for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = min(abs(a[0] - a[1]), abs(a[-1] - a[-2]))

    for i in range(1, n - 1):
        m = min(m, max(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1])))

    print(m)
