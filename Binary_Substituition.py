MOD = 998244353
for i in range(int(input())):
    s = input()
    n = len(s)
    a = [0]
    for i in range(n - 1):
        a.append(int(s[i] != s[i + 1]))
    dp = [[0, 0] for i in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
        if a[i] == 1:
            dp[i][1] = dp[i - 1][0]
        else:
            dp[i][1] = 0
    print((dp[n - 1][0] + dp[n - 1][1]) % MOD)
