for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    c = 0
    for i in A:
        if i - 1 > M - i:
            c = c + i - 1
        else:
            c = c + M - i
    print(c)
