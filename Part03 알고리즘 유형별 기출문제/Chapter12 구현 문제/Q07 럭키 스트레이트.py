data = input()

mid = len(data) // 2
result = 0

for n in data[:mid]:
    result += int(n)
for n in data[mid:]:
    result -= int(n)

if result == 0:
    print('LUCKY')
else:
    print('READY')
