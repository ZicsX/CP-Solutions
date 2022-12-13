for _ in range(int(input())):
    n = int(input())
    print("LEFT" if abs(1 - n) < abs(100 - n) else "RIGHT")
