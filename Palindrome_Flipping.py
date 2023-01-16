for _ in range(int(input())):
    n = int(input())
    s = input()
    one = s.count("1")
    zero = n - one
    if n % 2 == 0:
        if one % 2 and zero % 2:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
