def solve(N, K, parts):
    if N > 2 * K:
        return False
    h = {}
    for p in parts:
        if p in h:
            if h[p] == 2:
                return False
            else:
                h[p] += 1
        else:
            h[p] = 1
    return True


for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    parts = sorted(list(map(int, input().split())))
    print("Case #{}: {}".format(t, "YES" if solve(N, K, parts) else "NO"))
