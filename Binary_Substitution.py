for _ in range(int(input())):
    n = int(input())
    s = input()
    p, q = 0, 0
    for c in s:
        p += c == "0"
        q += c == "1"
    if p == 0:
        print(n, 0)
        continue
    if q == 0:
        print(n, 0)
        continue
    print(1, abs(p - q) + 1)
    for i in range(0, abs(p - q)):
        Q = 0
        for j in range(0, len(s) - 1):
            if (s[j] == "0" and s[j + 1] == "1") or (s[j] == "1" and s[j + 1] == "0"):
                Q = j
                break
        print(Q + 1, Q + 2, int(p > q))
        s = s[:Q] + chr(48 + int(p > q)) + s[Q + 2 :]
    print(1, len(s), 0)
