for _ in range(int(input())):
    a, b = map(int, input().split())
    y = 2**a
    x = y - 1
    print(x * (x - 1))
