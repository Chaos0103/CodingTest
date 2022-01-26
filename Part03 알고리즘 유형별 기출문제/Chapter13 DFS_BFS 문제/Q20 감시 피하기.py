from itertools import permutations

n = int(input())
data = []
temp = [['']*n for _ in range(n)]
point = []
teacher = []
for a in range(n):
    l = list(input().split())
    for b in range(n):
        if l[b] == 'X':
            point.append((a, b))
        elif l[b] == 'T':
            teacher.append((a, b))
    data.append(l)


def watch(x, y):
    # right
    for i in range(1, n):
        ny = y + i
        if ny < n:
            if temp[x][ny] == 'S':
                return False
            if temp[x][ny] == 'O':
                break
    # left
    for i in range(1, n):
        ny = y - i
        if ny >= 0:
            if temp[x][ny] == 'S':
                return False
            if temp[x][ny] == 'O':
                break
    # up
    for i in range(1, n):
        nx = x - i
        if nx >= 0:
            if temp[nx][y] == 'S':
                return False
            if temp[nx][y] == 'O':
                break
    # down
    for i in range(1, n):
        nx = x + i
        if nx < n:
            if temp[nx][y] == 'S':
                return False
            if temp[nx][y] == 'O':
                break
    return True


teach = len(teacher)
for d in list(permutations(point, 3)):
    for a in range(n):
        for b in range(n):
            if (a, b) in d:
                temp[a][b] = 'O'
            else:
                temp[a][b] = data[a][b]
    cnt = 0
    for x, y in teacher:
        if not watch(x, y):
            break
        else:
            cnt += 1
    if cnt == teach:
        print('YES')
        exit()
print('NO')
