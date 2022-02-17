from itertools import combinations

n, m = map(int, input().split())
house = []
chicken = []
for i in range(n):
    date = list(map(int, input().split()))
    for j in range(n):
        if date[j] == 1:
            house.append((i, j))
        elif date[j] == 2:
            chicken.append((i, j))

min_dist = int(1e9)
for data in list(combinations(chicken, m)):
    bnow = 0
    for hx, hy in house:
        now = int(1e9)
        for cx, cy in data:
            dist = abs(hx-cx) + abs(hy-cy)
            now = min(now, dist)
        bnow += now
    min_dist = min(min_dist, bnow)

print(min_dist)
