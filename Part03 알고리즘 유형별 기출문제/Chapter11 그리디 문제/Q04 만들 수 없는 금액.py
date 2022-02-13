n = int(input())
coins = list(map(int, input().split()))

coins.sort()

result = 1
for coin in coins:
    if result < coin:
        break
    result += coin

print(result)

'''
[input]
5
3 2 1 1 9
[output]
8
'''