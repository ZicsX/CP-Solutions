for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    s = 0
    for i in range(3):
        if a[i] != 0:
            a[i] -= 1
            s += 1
    for i in range(3):
        for j in range(i + 1, 3):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if a[0] >= 2:
        print(s + 3)
        continue
    if a[0] == 1:
        print(s + 2 if a[2] >= 2 else s + 1)
        continue
    print(s if a[1] == 0 else s + 1)
