from collections import deque

n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [0] * (n+1)


def bfs(start, visited):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1


bfs(start, visited)
result = []
for i in range(1, n+1):
    if visited[i] == k+1:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for n in result:
        print(n)
