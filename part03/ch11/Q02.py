data = input()

result = 0

for num in data:
    if result == 0 or result == 1:
        result += int(num)
    elif num == '1' or num == '0':
        result += int(num)
    else:
        result *= int(num)

print(result)
