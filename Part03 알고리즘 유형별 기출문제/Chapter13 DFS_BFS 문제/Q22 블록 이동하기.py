from collections import deque


def next_pos(pos, board):
    result = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        nx1, nx2 = x1 + dx[i], x2 + dx[i]
        ny1, ny2 = y1 + dy[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            result.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2:  # 가로
        for i in [1, -1]:
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                result.append({(x1, y1), (x1+i, y1)})
                result.append({(x2, y2), (x2+i, y2)})
    elif y1 == y2:  # 세로
        for i in [1, -1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                result.append({(x1, y1), (x1, y1+i)})
                result.append({(x2, y2), (x2, y2+i)})
    return result


def solution(board):
    n = len(board)
    data = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            data[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next in next_pos(pos, data):
            if next not in visited:
                visited.append(next)
                q.append((next, cost+1))
    return 0


test = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

print(solution(test))  # 7
