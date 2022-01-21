import sys

data = sys.stdin.readline().rstrip()
alpha = []
result = ''
num = 0
for ch in data:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num += int(ch)

alpha.sort()

for ch in alpha:
    result += ch
result += str(num)

print(result)
