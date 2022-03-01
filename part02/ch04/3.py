pos = input()
x = int(pos[1])
y = ord(pos[0]) - ord('a') + 1

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        result += 1

print(result)

'''
[input]
a1
[output]
2
'''