n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for num in data:
        if num > mid:
            count += (num - mid)
    if count < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

'''
[input]
4 6
19 15 10 17
[output]
15
'''