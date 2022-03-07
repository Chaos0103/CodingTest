num = input()

mid = len(num) // 2

result = 0
for n in num[:mid]:
    result += int(n)
for n in num[mid:]:
    result -= int(n)

if result == 0:
    print("LUCKY")
else:
    print("READY")
