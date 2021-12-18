N = int(input())

data = []

for _ in range(N):
    name, score = input().split()
    data.append([name, int(score)])

data = sorted(data, key=lambda student: student[1])

for d in data:
    print(d[0], end=' ')
