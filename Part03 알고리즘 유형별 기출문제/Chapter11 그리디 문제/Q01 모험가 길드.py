n = int(input())
data = list(map(int, input().split()))

data.sort()

group = 0
member = 0

for h in data:
    member += 1
    if member >= h:
        member = 0
        group += 1

print(group)