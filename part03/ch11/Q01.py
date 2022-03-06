n = int(input())
data = list(map(int, input().split()))
group = 0

data.sort()
cnt = 0
for n in data:
    cnt += 1
    if cnt >= n:
        group += 1
        cnt = 0

print(group)
