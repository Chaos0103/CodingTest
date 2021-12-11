pos = input()

x, y = ord(pos[0])-ord('a')+1, int(pos[1])

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if ny < 1 or nx < 1 or nx > 8 or ny > 8:
        continue
    cnt += 1

print(cnt)

# time: 20minute | running time: 1sec | memory limit: 128MB

# input
# a1
# output
# 2
