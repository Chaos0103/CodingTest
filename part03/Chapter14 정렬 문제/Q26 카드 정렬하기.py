import heapq

n = int(input())
data = []
for _ in range(n):
    card = int(input())
    heapq.heappush(data, card)

result = 0
while len(data) != 1:
    card1 = heapq.heappop(data)
    card2 = heapq.heappop(data)
    result += card1 + card2
    heapq.heappush(data, card1+card2)

print(result)
