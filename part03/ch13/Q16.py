from collections import deque
from itertools import permutations

n, m = map(int, input().split())

graph = []
blanks = []
viruses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            blanks.append((i, j))
        if graph[i][j] == 2:
            viruses.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
data = [[0] * m for _ in range(n)]
for new_wall in list(permutations(blanks, 3)):
    for i in range(n):
        for j in range(m):
            if (i, j) in new_wall:
                data[i][j] = 1
            else:
                data[i][j] = graph[i][j]

    for virus in viruses:
        q = deque()
        q.append(virus)
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    q.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1

    result = max(result, count)

print(result)
