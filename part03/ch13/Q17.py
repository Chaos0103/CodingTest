from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))  # virus, time, x, y
s, x, y = map(int, input().split())

data.sort()
q = deque(data)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    v, t, xpos, ypos = q.popleft()
    if t >= s:
        break
    for i in range(4):
        nx = xpos + dx[i]
        ny = ypos + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append((v, t+1, nx, ny))

print(graph[x-1][y-1])