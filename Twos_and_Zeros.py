def power(b, n):
    s = 1
    while n:
        if n % 2 == 1:
            s = (s * b) % MOD
        b = (b * b) % MOD
        n //= 2
    return s


#
def Inv(x):
    return power(x, MOD - 2)


#
MOD = 1000000007
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0, 0, 0]
    b = [0, 0, 0]
    a[0] = (([2, 1, -1, -2, -1, 1][n % 6] + power(2, n)) * Inv(3)) % MOD
    a[1] = (([-1, 1, 2, 1, -1, -2][n % 6] + power(2, n)) * Inv(3)) % MOD
    a[2] = (([-1, -2, -1, 1, 2, 1][n % 6] + power(2, n)) * Inv(3)) % MOD
    b[0] = (([2, 1, -1, -2, -1, 1][m % 6] + power(2, m)) * Inv(3)) % MOD
    b[1] = (([-1, 1, 2, 1, -1, -2][m % 6] + power(2, m)) * Inv(3)) % MOD
    b[2] = (([-1, -2, -1, 1, 2, 1][m % 6] + power(2, m)) * Inv(3)) % MOD
    print(((a[0] * b[0] + a[1] * b[1] + a[2] * b[2]) % MOD + MOD - 1) % MOD)
