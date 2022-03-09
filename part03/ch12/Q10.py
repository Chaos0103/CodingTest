def check(data, n):
    for i in range(n):
        for j in range(n):
            if data[n+i][n+j] != 1:
                return False
    return True


def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


def solution(key, lock):
    n = len(lock)
    m = len(key)

    renew_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            renew_lock[n+i][n+j] = lock[i][j]

    for _ in range(4):
        for i in range(n * 2 + 1):
            for j in range(n * 2 + 1):
                for a in range(m):
                    for b in range(m):
                        renew_lock[i+a][j+b] += key[a][b]
                if(check(renew_lock, n)):
                    return True
                for a in range(m):
                    for b in range(m):
                        renew_lock[i+a][j+b] -= key[a][b]
        key = rotate_a_matrix_by_90_degree(key)

    return False


# test case
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))  # true
