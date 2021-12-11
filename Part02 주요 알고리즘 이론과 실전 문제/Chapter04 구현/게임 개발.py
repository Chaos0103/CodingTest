N, M = map(int, input().split())
visited = [[0]*M for _ in range(N)]

x, y, d = map(int, input().split())
visited[x][y] = 1
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))


def leftTurn():
    global d
    d -= 1
    if d == -1:
        d = 3


D = [[-1, 0], [0, 1], [1, 0], [0, -1]]

turnTime = 0
visitCnt = 1
while True:
    leftTurn()
    nx = x + D[d][0]
    ny = y + D[d][1]
    if data[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        visitCnt += 1
        x, y = nx, ny
        turnTime = 0
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = x - D[d][0]
        ny = y - D[d][1]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turnTime = 0

print(visitCnt)

# time: 40minute | running time: 1sec | memory limit: 128MB

# input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# output
# 3

# 시뮬레이션 유형
# 일반적으로 방향(Direction)을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
# 파이썬에서 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적이라는 점을 기억
