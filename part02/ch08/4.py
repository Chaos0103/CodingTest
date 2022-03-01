n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (m+1)
dp[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

'''
[input]
2 15
2
3
[output]
5

[input]
3 4
3
5
7
[output]
-1
'''