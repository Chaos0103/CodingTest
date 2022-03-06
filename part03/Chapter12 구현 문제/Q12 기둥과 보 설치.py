def check(data):
    for x, y, a in data:
        if a == 0:  # 기둥
            if y == 0 or [x, y-1, 0] in data or [x-1, y, 1] in data or [x, y, 1] in data:
                continue
            return False
        elif a == 1:  # 보
            if [x, y-1, 0] in data or [x+1, y-1, 0] in data or ([x-1, y, 1] in data and [x+1, y, 1] in data):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        elif b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.pop()
    answer.sort()
    return answer


test1 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
test2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(5, test1))
print(solution(5, test2))
