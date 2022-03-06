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
    city = q.popleft()
    for i in graph[city]:
        if visited[i] == -1:
            visited[i] = visited[city] + 1
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

'''
[input]
4 4 2 1
1 2
1 3
2 3
2 4
[output]
4
'''