def solve():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == "0":
            print(i)
            return
    print(n)


for _ in range(int(input())):
    solve()
