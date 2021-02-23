"""
가장 작은수를 골라서 더하면 되므로 heapq의 최소힙활용
"""
import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

total = 0
for _ in range(n - 1):
    m1 = heapq.heappop(q)
    m2 = heapq.heappop(q)
    comp = m1 + m2
    total += comp
    heapq.heappush(q, m1 + m2)

print(total)