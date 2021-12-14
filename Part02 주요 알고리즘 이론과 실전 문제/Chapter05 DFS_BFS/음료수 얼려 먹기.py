N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x >= N or y >= M or x < 0 or y < 0:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            cnt += 1

print(cnt)

# time: 30minute | running time: 1sec | memory limit: 128MB

# input
# 4 5
# 00110
# 00011
# 11111
# 00000
# output
# 3

# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있음
# 3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 셈
