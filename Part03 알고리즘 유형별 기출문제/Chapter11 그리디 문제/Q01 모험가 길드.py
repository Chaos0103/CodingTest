n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0
member = 1

for h in data:
    if member >= h:
        result += 1
        member = 1
        continue
    member += 1

print(result)

'''
[input]
5
2 3 1 2 2
[output]
2
'''