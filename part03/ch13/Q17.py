from collections import deque

n, k = map(int, input().split())
data = []
virus = []
for i in range(n):
    d = list(map(int, input().split()))
    for j in range(n):
        if d[j] != 0:
            virus.append((d[j], 0, i, j))  # (virus, time, xpos, ypos)
    data.append(d)
T, X, Y = map(int, input().split())

virus.sort()  # 바이러스 넘버가 1부터 시작한다는 보장이 없으므로 오름차순 정렬 해야함
q = deque(virus)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    num, time, x, y = q.popleft()
    if time >= T:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = num
                q.append((num, time + 1, nx, ny))

print(data[X-1][Y-1])
