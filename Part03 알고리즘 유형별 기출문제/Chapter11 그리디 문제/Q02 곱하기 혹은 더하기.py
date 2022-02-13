data = input()
result = 0

for c in data:
    num = int(c)
    if result == 0:
        result += num
        continue
    if num == 0 or num == 1:
        result += num
    else:
        result *= num

print(result)

'''
[input]
02984
[output]
576

[input]
567
[output]
210
'''