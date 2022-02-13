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

'''
[input]
5 3
1 3 2 3 2
[output]
8
[input]
8 5
1 5 4 3 2 4 5 2
[output]
25
'''