n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 1

for coin in data:
    if result < coin:
        break
    result += coin

print(result)