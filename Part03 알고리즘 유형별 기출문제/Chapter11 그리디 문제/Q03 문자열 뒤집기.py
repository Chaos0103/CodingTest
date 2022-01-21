S = input()

change = 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        change += 1

print(change//2)