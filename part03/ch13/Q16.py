from itertools import permutations
from collections import deque

n, m = map(int, input().split())
graph = []
blank = []
visited = [[0]*m for _ in range(n)]
virus = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 0:
            blank.append([i, j])
        elif data[j] == 2:
            virus.append([i, j])
    graph.append(data)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def count():
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                count += 1
    return count


result = 0
for new_wall in list(permutations(blank, 3)):
    for i in range(n):
        for j in range(m):
            visited[i][j] = graph[i][j]

    for x, y in new_wall:
        visited[x][y] = 1

    q = deque()
    for x, y in virus:
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 2
                    q.append((nx, ny))

    cnt = count()
    result = max(result, cnt)

print(result)
