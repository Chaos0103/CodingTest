from itertools import combinations

n, m = map(int, input().split())
house = []
chicken = []
for a in range(n):
    data = list(map(int, input().split()))
    for b in range(n):
        if data[b] == 1:
            house.append((a, b))
        elif data[b] == 2:
            chicken.append((a, b))

datas = list(combinations(chicken, m))


def getSum(data):
    result = 0
    for hx, hy in house:
        min_value = int(1e9)
        for cx, cy in data:
            min_value = min(min_value, abs(hx - cx) + abs(hy - cy))
        result += min_value
    return result


min_value = int(1e9)
for data in datas:
    min_value = min(min_value, getSum(data))

print(min_value)
