from collections import deque

n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])
sec, x, y = map(int, input().split())

data.sort()
q = deque(data)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    virus, s, ix, iy = q.popleft()
    if s == sec:
        break
    for i in range(4):
        nx = ix + dx[i]
        ny = iy + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append([virus, s + 1, nx, ny])

print(graph[x-1][y-1])
