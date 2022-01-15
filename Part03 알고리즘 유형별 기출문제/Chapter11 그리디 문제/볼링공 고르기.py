from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0

data = list(combinations(data, 2))
for x in data:
    if x[0] != x[1]:
        result += 1

print(result)