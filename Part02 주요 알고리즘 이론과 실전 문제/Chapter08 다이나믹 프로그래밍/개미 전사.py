# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
data = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + data[i])

# 계산된 결과 출력
print(d[n-1])

# 왼쪽부터 (i-3)번째 이하의 식량창고에 대해서는 고려할 필요가 없음(항상 털 수 있기 때문)