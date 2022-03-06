n = int(input())

dp = [False] * (1001)
dp[1] = True
cnt = 1
for i in range(2, 1001):
    if dp[i//2] and i % 2 == 0:
        dp[i] = True
    elif dp[i//3] and i % 3 == 0:
        dp[i] = True
    elif dp[i//5] and i % 5 == 0:
        dp[i] = True
    if dp[i]:
        cnt += 1
    if cnt == n:
        print(i)
        break
