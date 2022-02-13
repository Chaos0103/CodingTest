n = int(input())
data = [int(input()) for _ in range(n)]

data.sort(reverse=True)

print(*data)

'''
[input]
3
15
27
12
[output]
27 15 12
'''