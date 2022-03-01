coin_types = (500, 100, 50, 10)

N = int(input())

cnt = 0
for coin in coin_types:
    cnt += N//coin
    N %= coin

print(cnt)

# '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것
# 화폐의 종류가 K개라고 할 때 위 소스 코드의 시간 복잡도: O(K)
# 시간 복잡도는 동전의 총 종류에만 영향을 받고, 거슬러 줘야하는 금액의 크기와는 무관
