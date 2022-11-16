def missingNumbers(a, b):
    count = {}
    for num in a:
        count[num] = count.get(num, 0) + 1

    missing = []
    for num in b:
        if count.get(num, 0) == 0:
            missing.append(num)
        else:
            count[num] -= 1
    missing = list(set(missing))
    missing.sort()
    return missing


n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input().strip())
b = list(map(int, input().rstrip().split()))
result = missingNumbers(a, b)
print(*result)
