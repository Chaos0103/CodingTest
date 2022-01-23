from collections import deque

snack = deque()
snack.append([1, 1])
apple = []
sec = 0

n = int(input())
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    apple.append([x, y])
l = int(input())
data = []
for _ in range(l):
    data.append(list(input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
di = 0
idx = 0

while True:
    sec += 1
    nx = snack[-1][0] + dx[di]
    ny = snack[-1][1] + dy[di]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        break
    if [nx, ny] in snack:
        break
    if [nx, ny] in apple:
        snack.append([nx, ny])
        apple.remove([nx, ny])
    else:
        snack.append([nx, ny])
        snack.popleft()
    if idx < l:
        if sec == int(data[idx][0]):
            if data[idx][1] == 'D':
                di += 1
                if di == 4:
                    di = 0
            else:
                di -= 1
                if di == -1:
                    di = 3
            idx += 1

print(sec)
