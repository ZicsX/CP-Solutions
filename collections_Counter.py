from collections import Counter

_ = int(input())
s = list(map(int, input().split()))

shoe_c = Counter(s)
money_earned = 0

for i in range(int(input())):
    shoe_num, price = map(int, input().split())
    if shoe_c[shoe_num] > 0:
        money_earned += price
        shoe_c[shoe_num] -= 1
print(money_earned)
