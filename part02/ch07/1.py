def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return 'yes'
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
order = list(map(int, input().split()))

for num in order:
    print(binary_search(array, num, 0, n-1), end=' ')

'''
[input]
5
8 3 7 9 2
3
5 7 9
[output]
no yes yes
'''