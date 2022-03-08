from collections import deque

n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

order = []
l = int(input())
for _ in range(l):
    t, d = input().split()
    order.append((int(t), d))

snack = deque()
snack.append((1, 1))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist = 0
result = 0
idx = 0
while True:
    nx = snack[-1][0] + dx[dist]
    ny = snack[-1][1] + dy[dist]
    result += 1
    if nx < 1 or ny < 1 or nx > n or ny > n:
        break
    if (nx, ny) in snack:
        break
    if data[nx][ny] == 1:
        data[nx][ny] = 0
    else:
        snack.popleft()
    snack.append((nx, ny))
    if idx < l:
        if order[idx][0] == result:
            if order[idx][1] == 'L':
                dist -= 1
                if dist == -1:
                    dist = 3
            else:
                dist += 1
                if dist == 4:
                    dist = 0
            idx += 1

print(result)
