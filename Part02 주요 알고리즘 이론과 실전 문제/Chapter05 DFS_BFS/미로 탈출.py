from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append([0, 0])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                q.append([nx, ny])

print(data[n-1][m-1])

'''
[input]
5 6
101010
111111
000001
111111
111111
[output]
10
'''