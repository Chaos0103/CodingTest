N, K = map(int, input().split())
cnt = 0

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    cnt += 1

print(cnt)

# running time: 1sec | memory limit: 128MB

# input
# 25 5
# output
# 2
