n = int(input())
coin = list(map(int, input().split()))

coin.sort()
result = 1
for num in coin:
    if result >= num:
        result += num
    else:
        break

print(result)