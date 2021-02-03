from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
graph = [[0] * (n + 1)] + [[0] for _ in range(n)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    graph[i] += row


def get_chicken_distance(graph, n, r, c):
    result = 2 * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 2:
                dist = abs(r - i) + abs(c - j)
                result = min(result, dist)
    return result


def total_chicken_distance(graph, n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 1:
                total += get_chicken_distance(graph, n, i, j)
    return total


def get_chicken_house(graph, n):
    houses = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 2:
                houses.append((i, j))
    return houses


houses = get_chicken_house(graph, n)
combs = list(combinations(houses, len(houses) - m))
dist = int(1e9)
for comb in combs:
    new_graph = deepcopy(graph)
    for r, c in comb:
        new_graph[r][c] = 0
    new_dist = total_chicken_distance(new_graph, n)
    dist = min(dist, new_dist)
print(dist)

"""2차원 리스트 사용 => 시간초과!"""