for _ in range(int(input())):
    n = int(input())
    a = str(input())
    l = 0
    r = n - 1
    Q = []
    while 1:
        if a[l] == "0":
            Q.insert(0, "0")
        else:
            Q.append("1")
        l = l + 1
        if l > r:
            break
        if a[r] == "1":
            Q.insert(0, "1")
        else:
            Q.append("0")
        r = r - 1
        if l > r:
            break
    print("".join(Q))
