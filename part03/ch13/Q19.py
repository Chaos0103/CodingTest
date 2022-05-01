from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
add, dif, mul, div = map(int, input().split())

oper = '+' * add + '-' * dif + '*' * mul + '/' * div
cnt = add + dif + mul + div

maxResult = -1 * int(1e9)
minResult = int(1e9)

for data in list(permutations(oper, cnt)):
    result = num[0]
    for i in range(cnt):
        if data[i] == '+':
            result += num[i+1]
        elif data[i] == '-':
            result -= num[i+1]
        elif data[i] == '*':
            result *= num[i+1]
        elif data[i] == '/':
            if result < 0:
                result *= -1
                result //= num[i + 1]
                result *= -1
            else:
                result //= num[i+1]

    maxResult = max(maxResult, result)
    minResult = min(minResult, result)

print(maxResult)
print(minResult)
