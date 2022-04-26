from collections import deque
from itertools import permutations

n, m = map(int, input().split())

blank = []
viruses = []
graph = []
result = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        if graph[i][j] == 2:
            viruses.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for pos in list(permutations(blank, 3)):
    data = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if (i, j) in pos:
                data[i][j] = 1
            else:
                data[i][j] = graph[i][j]

    for virus in viruses:
        queue = deque()
        queue.append(virus)
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    queue.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1

    result = max(result, count)

print(result)