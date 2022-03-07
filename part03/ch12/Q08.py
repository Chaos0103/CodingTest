data = input()
result = []
num = 0
for c in data:
    if c.isalpha():
        result.append(c)
    else:
        num += int(c)
result.sort()
result.append(str(num))

print(''.join(result))
