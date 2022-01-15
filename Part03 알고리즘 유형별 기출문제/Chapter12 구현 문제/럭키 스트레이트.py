data = input()

mid = len(data) // 2
left = 0
right = 0
for n in data[:mid]:
    left += int(n)
for n in data[mid:]:
    right += int(n)

if left == right:
    print('LUCKY')
else:
    print('READY')