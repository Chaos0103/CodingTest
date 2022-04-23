from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
add, dif, mul, div = map(int, input().split())
data = '+' * add + '-' * dif + '*' * mul + '/' * div
max_value = int(1e9) * -1
min_value = int(1e9)

for d in list(permutations(data, (n-1))):
    result = num[0]
    for i in range(n-1):
        if d[i] == '+':
            result += num[i+1]
        elif d[i] == '-':
            result -= num[i+1]
        elif d[i] == '*':
            result *= num[i+1]
        elif d[i] == '/':
            if result < 0:
                result *= -1
                result //= num[i+1]
                result *= -1
            else:
                result //= num[i+1]
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
