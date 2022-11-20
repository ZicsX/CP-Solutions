for _ in range(int(input())):
    p, q, r = map(int, input().split())
    ans = 1
    a = [1, 0, 1, 4]
    for i in range(30):
        temp = ((p >> i) & 1) + ((q >> i) & 1) + ((r >> i) & 1)
        ans *= a[temp]
    print(ans)
