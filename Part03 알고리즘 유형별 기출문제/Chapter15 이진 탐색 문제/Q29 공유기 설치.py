n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]

data.sort()

d = (data[-1] - data[0]) // (c-1)


def binary_search(array, target, start, end):
    if start > end:
        if abs(array[end]-target) < abs(array[start]-target):
            return end
        else:
            return start
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)


s = [data[0]]
idx = 0
for i in range(c-2):
    target = data[0] + d*(i+1)
    idx = binary_search(data, target, idx+2, n - 1)
    s.append(data[idx])

s.append(data[-1])
print(s)