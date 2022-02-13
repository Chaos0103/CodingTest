data = input()
count = 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count += 1

print(count // 2)

'''
[input]
0001100
[output]
1
'''