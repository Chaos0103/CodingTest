t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    gold = []
    data = list(map(int, input().split()))
    for i in range(n):
        gold.append(data[i*m: (i+1)*m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                gold[i][j] += max(gold[i][j - 1], gold[i + 1][j - 1])
            elif i == n-1:
                gold[i][j] += max(gold[i][j - 1], gold[i - 1][j - 1])
            else:
                gold[i][j] += max(gold[i][j-1], gold[i-1][j-1], gold[i+1][j-1])
    result = 0
    for i in range(n):
        result = max(result, gold[i][m-1])
    print(result)
