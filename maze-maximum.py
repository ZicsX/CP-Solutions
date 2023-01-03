def find_max_value(matrix):
    lo = min(map(min, matrix))
    hi = max(map(max, matrix))

    ans = float("-inf")

    while lo <= hi:
        mid = (lo + hi) // 2
        row_flag = any(all(x >= mid for x in row) for row in matrix)
        col_flag = any(all(matrix[i][j] >= mid for i in range(n)) for j in range(m))
        if row_flag and col_flag:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1

    return ans


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(find_max_value(matrix))
