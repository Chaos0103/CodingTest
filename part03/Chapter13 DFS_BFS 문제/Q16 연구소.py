from itertools import permutations

n, m = map(int, input().split())
graph = []
point = []
temp = [[0]*m for _ in range(n)]
for a in range(n):
    data = list(map(int, input().split()))
    for b in range(m):
        if data[b] == 0:
            point.append((a, b))
    graph.append(data)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                dfs(nx, ny)


def count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


result = 0
for data in list(permutations(point, 3)):
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    for x, y in data:
        temp[x][y] = 1
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dfs(i, j)
    result = max(result, count())

print(result)
