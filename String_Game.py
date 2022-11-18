for _ in range(int(input())):
    n = int(input())
    s = list(input())

    c0 = s.count("0")
    m = min(c0, n - c0)

    if m % 2 == 0:
        print("Ramos")
    else:
        print("Zlatan")
