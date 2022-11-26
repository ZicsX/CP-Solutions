for _ in range(int(input())):
    A, X, B, Y = map(int, input().split())
    if A / X > B / Y:
        print("Alice")
    elif A / X < B / Y:
        print("Bob")
    else:
        print("Equal")
