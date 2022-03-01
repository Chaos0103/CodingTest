n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

cnt = m // (k + 1)
result = data[1] * cnt
result += data[0] * (m - cnt)

print(result)

'''
[input]
5 8 3
2 4 5 4 6
[output]
46
'''
