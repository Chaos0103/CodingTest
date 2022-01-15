import sys

data = list(sys.stdin.readline().rstrip())
data.sort()

num = 0
idx = 0
while '0' <= data[idx] <= '9':
    num += int(data[idx])
    idx += 1

print(''.join(data[idx:]) + str(num))