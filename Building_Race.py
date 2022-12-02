for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    if x != y:
        if x > y:
            print("Chef")
        else:
            print("Chefina")
    else:
        if a > b:
            print("Chefina")
        elif a < b:
            print("Chef")
        else:
            print("Both")
