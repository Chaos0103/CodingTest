from collections import deque

n, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, index):
    point = []
    point.append((x, y))
    q = deque()
    q.append((x, y))
    visited[x][y] = index
    people = data[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                sub = abs(data[x][y] - data[nx][ny])
                if L <= sub <= R:
                    q.append((nx, ny))
                    point.append((nx, ny))
                    visited[nx][ny] = index
                    people += data[nx][ny]
                    cnt += 1
    for x, y in point:
        data[x][y] = people // cnt


result = 0
while True:
    visited = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n*n:
        break
    result += 1

print(result)
