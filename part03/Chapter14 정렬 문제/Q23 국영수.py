import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((int(kor), int(eng), int(math), name))

data.sort(key = lambda x: (-x[0], x[1], -x[2], x[3]))

for i in data:
    print(i[3])