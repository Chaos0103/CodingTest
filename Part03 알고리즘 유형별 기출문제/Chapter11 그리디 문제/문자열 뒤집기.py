bit = input()
part = 1

for i in range(len(bit)-1):
    if bit[i] != bit[i+1]:
        part += 1

print(part//2)