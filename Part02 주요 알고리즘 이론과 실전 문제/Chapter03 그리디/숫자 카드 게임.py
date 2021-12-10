N, M = map(int, input().split())

card = []
for _ in range(N):
    data = list(map(int, input().split()))
    card.append(min(data))

print(max(card))

# running time: 1sec | memory limit: 128MB

# input
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# output
# 2

# input
# 7 3 1 8
# 3 3 3 4
# output
# 3
