n, m = map(int, input().split())
result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)

'''
[input]
3 3
3 1 2
4 1 4
2 2 2
[output]
2

[input]
2 4
7 3 1 8
3 3 3 4
[output]
3
'''