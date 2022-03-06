data = input()
result = ''
alpha = []
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

'''
[input]
K1KA5CB7
[output]
ABCKK13

[input]
AJKDLSI412K4JS9D
[output]
ADDIJJJKKLSS20
'''