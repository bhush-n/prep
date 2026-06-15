import heapq

pq = []

heapq.heappush(pq, 30)
heapq.heappush(pq, 10)
heapq.heappush(pq, 20)
print(heapq.heappop(pq))
print(heapq.heappop(pq))
print(heapq.heappop(pq))
print(pq)