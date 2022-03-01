INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)

'''
[input]
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
[output]
3

[input]
4 2
1 3
2 4
3 4
[output]
-1
'''