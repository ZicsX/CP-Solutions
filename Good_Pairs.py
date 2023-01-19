for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    d = {}

    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    print(sum(x * (x - 1) // 2 for x in d.values()))
