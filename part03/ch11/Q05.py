n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(n-1):
    for j in range(i+1, n):
        if data[i] != data[j]:
            result += 1

print(result)
