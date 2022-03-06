from collections import deque
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_x, shark_y = 0, 0
shark_size = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    distance = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if distance[nx][ny] != -1:
                continue
            if graph[nx][ny] <= shark_size:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
    return distance


def find(distance):
    x, y = 0, 0
    min_distance = INF
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 0 < graph[i][j] < shark_size:
                if distance[i][j] < min_distance:
                    x, y = i, j
                    min_distance = distance[i][j]
    if min_distance == INF:
        return None
    return min_distance, x, y


result = 0
cnt = 0
while True:
    fish = find(bfs(shark_x, shark_y))
    if fish == None:
        print(result)
        break
    else:
        distance, x, y = fish
        result += distance
        shark_x, shark_y = x, y
        graph[x][y] = 0
        cnt += 1
        if cnt == shark_size:
            shark_size += 1
            cnt = 0
