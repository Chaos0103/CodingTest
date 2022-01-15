num = input()

result = 0

for i in range(len(num)):
    n = int(num[i])
    if n == 0 or n == 1 or result == 0:  # result가 1일 때 생각을 못함
        result += n
    else:
        result *= n

print(result)

# 틀림