n, m = map(int, input().split())
balls = list(map(int, input().split()))
counts = [balls.count(x) for x in range(m + 1)]
result = 0
for i in range(1, m + 1):
    result += counts[i] * (sum(counts) - counts[i])
result = result // 2
print(result)

"""
나는 모든 경우의 수 구해서 2!으로 나누어 조합의 경우의수를 구했는데, 
sum(counts[i+1])을 곱해서 순서대로 하면 중복되는 경우를 제외하면서 할 수 있다.
a, b 중 a를 기준으로 작은 무게부터 count하는 것. 
"""