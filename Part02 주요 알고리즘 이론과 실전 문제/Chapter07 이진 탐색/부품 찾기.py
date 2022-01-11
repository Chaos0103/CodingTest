N = int(input())
data1 = list(map(int, input().split()))
M = int(input())
data2 = list(map(int, input().split()))

data1.sort()


def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return False
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return True


for n in data2:
    if binary_search(data1, n, 0, N):
        print(end='yes ')
    else:
        print(end='no ')

# time: 30minute | running time: 1sec | memory limit: 128MB
# 이진 탐색, 계수 정렬, 집합 자료형으로 풀이 가능