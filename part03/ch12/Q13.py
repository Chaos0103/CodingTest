from itertools import combinations

n, m = map(int, input().split())

chicken = []
house = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

result = 1e9
for data in list(combinations(chicken, m)):
    total = 0
    for home in house:
        dist = 1e9
        for ch in data:
            dist = min(abs(ch[0] - home[0]) + abs(ch[1] - home[1]), dist)
        total += dist
    result = min(result, total)

print(result)