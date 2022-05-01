from collections import deque

n, m, k, start = map(int, input().split())

data = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

q = deque()
q.append(start)
visited[start] = 0
while q:
    city = q.popleft()
    for i in data[city]:
        if visited[i] == -1:
            visited[i] = visited[city] + 1
            q.append(i)

result = list()
for i in range(1, n+1):
    if visited[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for n in result:
        print(n)
