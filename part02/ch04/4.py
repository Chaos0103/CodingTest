n, m = map(int, input().split())
x, y, dist = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global dist
    dist -= 1
    if dist < 0:
        dist = 3


turn_time = 0
count = 1
visited[x][y] = 1
while True:
    turn_left()
    nx = x + dx[dist]
    ny = y + dy[dist]
    if data[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        count += 1
        x, y = nx, ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[dist]
        ny = y - dy[dist]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)

'''
[input]
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
[output]
3
'''