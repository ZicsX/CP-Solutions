MOD = 998244353


def power(b, n):
    s = 1
    while n:
        if n % 2 == 1:
            s = s * b % MOD
        b = b * b % MOD
        n //= 2
    return s


def count(i, j):
    return ((i // (1 << (j + 1))) << j) + (max(0, i % (1 << (j + 1)) - (1 << j) + 1))


for _ in range(int(input())):
    n, m = map(int, input().split())
    s = 0
    for i in range(31):
        s = (s + (power(count(m, i), n) << i) % MOD) % MOD
    print(s)
