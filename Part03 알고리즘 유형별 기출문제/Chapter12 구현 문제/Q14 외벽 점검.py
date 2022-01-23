from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(n+weak[i])
    answer = len(dist) + 1

    for start in range(length):
        for people in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[start] + people[cnt-1]
            for i in range(start, start+length):
                if pos < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[i] + people[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer


test1_weak = [1, 5, 6, 10]
test1_dist = [1, 2, 3, 4]
test2_weak = [1, 3, 4, 9, 10]
test2_dist = [3, 5, 7]

print(solution(12, test1_weak, test1_dist))  # 2
print(solution(12, test2_weak, test2_dist))  # 1
