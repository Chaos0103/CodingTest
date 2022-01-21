strNum = input()

result = 0

for ch in strNum:
    num = int(ch)
    if result < 2 or num < 2:
        result += num
    else:
        result *= num

print(result)