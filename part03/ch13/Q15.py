from collections import deque

n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1] * (n+1)

q = deque()
q.append(start)
visited[start] = 0
while q:
    now = q.popleft()
    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            q.append(i)

result = []
for i in range(1, n+1):
    if visited[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for n in result:
        print(n)

