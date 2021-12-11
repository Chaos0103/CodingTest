N = int(input())

cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if s%10 == 3 or s//10 == 3 or m%10 == 3 or m//10==3 or h == 3:
                cnt += 1

print(cnt)

# time: 15minute | running time: 2sec | memory limit: 128MB

# input
# 5
# output
# 11475

# 완전 탐색 유형

# 정답 코드(좋은 아이디어)
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 문자열 연산을 이용하여 찾기
            if '3' in str(i)+str(j)+str(k):
                count += 1
                
print(count)
