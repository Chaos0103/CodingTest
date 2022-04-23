from collections import deque

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0  or nx >= n or ny >= m:
            continue
        if data[nx][ny] == 1:
            data[nx][ny] = data[x][y] + 1
            q.append((nx, ny))

print(data[n - 1][m - 1])