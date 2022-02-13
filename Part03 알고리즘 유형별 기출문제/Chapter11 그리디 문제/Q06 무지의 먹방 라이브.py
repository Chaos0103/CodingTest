import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_time = 0
    pre = 0
    length = len(food_times)
    while sum_time + (q[0][0] - pre) * length < k:
        now = heapq.heappop(q)[0]
        sum_time += (now - pre) * length
        pre = now
        length -= 1
    q.sort(key=lambda x: x[1])
    return q[(k - sum_time) % length][1]


print(solution([3, 1, 2], 5))  # 1
