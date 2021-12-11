N = int(input())
order = list(input().split())
x, y = 1, 1

for c in order:
    nx, ny = x, y
    if c == 'L':
        ny -= 1
    elif c == 'R':
        ny += 1
    elif c == 'U':
        nx -= 1
    elif c == 'D':
        nx += 1
    if nx > N or ny > N or nx < 1 or ny < 1:
        continue
    x, y = nx, ny

print(x, y)

# time: 15minute | running time: 1sec | memory limit: 128MB

# input
# 5
# R R R U D D
# output
# 3 4

# 시뮬레이션 유형
