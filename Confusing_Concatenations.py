for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    for i in range(n):
        if a[i] > a[0]:
            flag = True
            Q = i
            break
    if not flag:
        print(-1)
        continue
    print(Q)
    for i in range(Q):
        print(a[i], end=" ")
    print()
    print(n - Q)
    for i in range(Q, n):
        print(a[i], end=" ")
    print()
