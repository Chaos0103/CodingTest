n = int(input())

dp = [0] * 30001

for num in range(2, n+1):
    dp[num] = dp[num-1]+1
    if num % 5 == 0:
        dp[num] = min(dp[num], dp[num // 5] + 1)
    if num % 3 == 0:
        dp[num] = min(dp[num], dp[num // 3] + 1)
    if num % 2 == 0:
        dp[num] = min(dp[num], dp[num // 2] + 1)

print(dp[n])

'''
[input]
26
[output]
3
'''