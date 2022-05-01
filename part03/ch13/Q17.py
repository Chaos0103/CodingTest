from collections import deque

n, k = map(int, input().split())

graph = []
viruses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            viruses.append((graph[i][j], 0, i, j))
s, X, Y = map(int, input().split())

viruses.sort()
q = deque(viruses)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    virus, time, x, y = q.popleft()
    if time >= s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, time+1, nx, ny))

print(graph[X-1][Y-1])
