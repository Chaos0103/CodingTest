INF = int(1e9)

n, m = map(int, input().split())
data = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            data[a][b] = 0
for _ in range(m):
    x, y = map(int, input().split())
    data[x][y] = 1

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

result = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if data[a][b] != INF or data[b][a] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)