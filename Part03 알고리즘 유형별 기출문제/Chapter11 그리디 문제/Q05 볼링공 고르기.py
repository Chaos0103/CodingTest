n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        if data[i] == data[j]:
            continue
        result += 1

print(result)