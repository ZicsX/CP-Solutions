for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    minn = min(a)
    c = 0
    for i in a:
        if minn < i:
            c += 1
    print(c)
