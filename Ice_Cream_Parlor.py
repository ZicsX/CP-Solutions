for _ in range(int(input())):
    c = int(input())
    n = int(input())
    a = list(map(int, input().split()))

    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if a[i]+a[j]==c:
    #                 print(i+1,j+1)
    #                 break

    hash = {}
    for i, x in enumerate(a):
        if c - x in hash:
            print(hash[c - x] + 1, i + 1)
            break
        else:
            hash[x] = i
