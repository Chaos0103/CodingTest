N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

cnt = M // (K+1)

result = data[1] * cnt + data[0] * (M-cnt)

print(result)

# time: 30minute | running time: 1sec | memory limit: 128MB

# input
# 5 8 3
# 2 4 5 4 6
# output
# 46
