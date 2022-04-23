from collections import deque

n, m, target, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


visited[start] = 0
q = deque()
q.append(start)
while q:
    city = q.popleft()
    for i in graph[city]:
        if visited[i] == -1:
            visited[i] = visited[city] + 1
            q.append(i)

result = []
for i in range(1, n+1):
    if visited[i] == target:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for num in result:
        print(num)