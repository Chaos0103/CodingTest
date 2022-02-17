from collections import deque

n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1
l = int(input())
order = deque()
for _ in range(l):
    t, dist = input().split()
    order.append((int(t), dist))

snack = deque()
snack.append((1, 1))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx = 0
time = 0
while True:
    x, y = snack[-1]
    nx = x + dx[idx]
    ny = y + dy[idx]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        break
    if (nx, ny) in snack:
        break
    if data[nx][ny] == 1:
        data[nx][ny] = 0
    else:
        snack.popleft()
    snack.append((nx, ny))
    time += 1
    if len(order) != 0:
        if time == order[0][0]:
            if order[0][1] == 'D':
                idx += 1
                if idx == 4:
                    idx = 0
            else:
                idx -= 1
                if idx == -1:
                    idx = 3
            order.popleft()

print(time+1)
