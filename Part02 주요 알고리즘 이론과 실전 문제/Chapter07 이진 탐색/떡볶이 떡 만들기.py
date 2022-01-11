n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in data:
        if mid < i:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

# time: 40minute | running time: 2sec | memory limit: 128MB

# 파라메트릭 서치(Parametric Search)유형: 최적화 문제를 결정 문제(예 혹은 아니오로 답하는 문제)로 바꾸어 해결하는 기법
# '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 사용
# 코딩 테스트나 프로그래밍 대회에서는 보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결
# 일반적으로 이 문제와 같은 파라메트릭 서치 문제 유현은 이진 탐색을 재귀적으로 구현하지 않고 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있음
