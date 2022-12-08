for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    li = []
    i = 0
    j = n - 1
    while i < n / 2 or j >= n / 2:
        li.append(a[j] - a[i])
        i += 1
        j -= 1
    k = li[0]
    i = 0
    while i < len(li) - 1:
        if li[i] < 0:
            k = -1
            break
        if li[i] < li[i + 1]:
            k = -1
            break
        i += 1
    if li[len(li) - 1] < 0:
        print(-1)
    else:
        print(k)
