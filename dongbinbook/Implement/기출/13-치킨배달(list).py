from itertools import combinations

n, m = map(int, input().split())

chickens, houses = [], []

for r in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    for c in range(1, n + 1):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

combis = list(combinations(chickens, m))

answer = int(1e9)
for combi in combis:
    total = 0
    for hr, hc in houses:
        dist = int(1e9)
        for cr, cc in combi:
            new_dist = abs(hr - cr) + abs(hc - cc)
            dist = min(dist, new_dist)
        total += dist
    answer = min(answer, total)
print(answer)
