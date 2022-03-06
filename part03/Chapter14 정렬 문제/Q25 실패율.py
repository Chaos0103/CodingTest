def solution(N, stages):
    answer = []
    cnt = [0] * (N+2)
    data = []
    p = len(stages)
    for n in stages:
        cnt[n] += 1
    for i in range(1, N+1):
        if cnt[i] == 0:
            data.append((0, i))
            continue
        data.append((cnt[i]/p, i))
        p -= cnt[i]
    data.sort(key = lambda x: (-x[0], x[1]))
    for d in data:
        answer.append(d[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
