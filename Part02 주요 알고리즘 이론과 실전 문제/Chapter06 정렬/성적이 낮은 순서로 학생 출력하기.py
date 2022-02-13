n = int(input())
datas = []
for _ in range(n):
    name, score = input().split()
    datas.append([name, int(score)])

datas = sorted(datas, key=lambda x: x[1])

for data in datas:
    print(data[0], end=' ')

'''
[input]
2
홍길동 95
이순신 77
[output]
이순신 홍길동
'''