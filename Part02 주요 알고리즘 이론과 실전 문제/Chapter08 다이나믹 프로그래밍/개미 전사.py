n = int(input())
data = list(map(int, input().split()))

dp = [0] * 101
dp[0] = data[0]
dp[1] = max(data[1], data[0])
for i in range(2, n):
    dp[i] = max(data[i] + dp[i-2], dp[i-1])

print(dp[n-1])

'''
[input]
4
1 3 1 5
[output]
8
'''