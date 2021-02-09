from itertools import combinations

n, m = map(int, input().split())

chickens, houses = [], []

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        if row[j - 1] == 1:
            houses.append((i, j))
        elif row[j - 1] == 2:
            chickens.append((i, j))

combies = list(combinations(chickens, m))

total = int(1e9)
for combi in combies:
    city_total = 0
    for hx, hy in houses:
        distance = 2 * n
        for cx, cy in combi:
            new_dist = abs(hx - cx) + abs(hy - cy)
            distance = min(distance, new_dist)
        city_total += distance
    total = min(total, city_total)

print(total)