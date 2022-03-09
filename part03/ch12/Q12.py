def check(datas):
    for data in datas:
        x, y, a = data
        if a == 0:
            if y == 0 or [x, y-1, 0] in datas or [x-1, y, 1] in datas or [x, y, 1] in datas:
                continue
            return False
        else:
            if [x, y-1, 0] in datas or [x+1, y-1, 0] in datas or ([x-1, y, 1] in datas and [x+1, y, 1] in datas):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for data in build_frame:
        x, y, a, b = data
        if b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not check(answer):
                answer.pop()
    answer.sort()
    return answer


test1 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
test2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(5, test1))
print(solution(5, test2))
