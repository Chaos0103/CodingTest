n = int(input())
data = list(map(int, input().split()))

data.sort()

cnt = 1
result = 0
for num in data:
    if cnt == num:
        result += 1
        cnt = 1
    else:
        cnt += 1

print(result)