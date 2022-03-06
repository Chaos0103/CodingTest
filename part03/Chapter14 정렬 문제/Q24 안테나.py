n = int(input())
data = list(map(int, input().split()))

data.sort()

idx1 = len(data)//2
idx2 = idx1-1

result1 = 0
result2 = 0

for i in data:
    result1 += abs(data[idx1]-i)
    result2 += abs(data[idx2]-i)

if result1 < result2:
    print(data[idx1])
else:
    print(data[idx2])
