def check(lock, n):
    for i in range(n):
        for j in range(n):
            if lock[n+i][n+j] != 1:
                return False
    return True


def turn_key(key):
    row_length = len(key)
    column_length = len(key[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = key[r][c]

    return res


def solution(key, lock):
    lock_len = len(lock)
    new_lock = [[0] * (lock_len*3) for _ in range(lock_len*3)]
    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[lock_len+i][lock_len+j] = lock[i][j]

    for _ in range(4):
        key = turn_key(key)
        for x in range(lock_len * 2):
            for y in range(lock_len * 2):
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock, lock_len):
                    return True
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x+i][y+j] -= key[i][j]
    return False


# test case
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))  # true
