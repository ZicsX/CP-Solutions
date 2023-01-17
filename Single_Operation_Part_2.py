def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        if s[i] == "1":
            print(i)
            return
    print(n)


for _ in range(int(input())):
    solve()
