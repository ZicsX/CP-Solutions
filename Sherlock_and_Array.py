for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    temp_sum = 0
    f = True
    for i in a:
        if temp_sum == (s - i - temp_sum):
            print("YES")
            f = False
            break
        else:
            temp_sum += i
    if f:
        print("NO")
