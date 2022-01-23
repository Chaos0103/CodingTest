def check_list(data, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[n+i][n+j] == 1:
                cnt += 1
    if cnt == n**2:
        return True
    else:
        return False


def turn_right(data, n):
    result = [[0] * n for _ in range(n)]
    idx = n-1
    for i in data:
        for j in range(n):
            result[j][idx] = i[j]
        idx -= 1
    return result


def solution(key, lock):
    size = len(lock)
    for _ in range(4):
        for i in range(size*2 + 1):
            for j in range(size*2 + 1):
                data = [[0] * (size * 3) for i in range(size * 3)]
                for a in range(size):
                    for b in range(size):
                        data[size+a][size+b] = lock[a][b]

                for a in range(len(key)):
                    for b in range(len(key)):
                        data[i+a][j+b] += key[a][b]
                result = check_list(data, size)
                if result:
                    return True
        key = turn_right(key, len(key))

    return False


test_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
test_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(test_key, test_lock))