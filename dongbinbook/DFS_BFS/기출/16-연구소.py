from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    graph[i] = [0] + row

zeros = []
viruses = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 0:
            zeros.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

walls = list(combinations(zeros, 3))


def count_safe(graph):
    safe = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 0:
                safe += 1
    return safe


def expand(x, y, graph):
    for mx, my in moves:
        nx = x + mx
        ny = y + my
        if nx < 1 or nx > n:
            continue
        if ny < 1 or ny > m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            expand(nx, ny, graph)


answer = -1
for wall in walls:
    changed = deepcopy(graph)
    for wx, wy in wall:
        changed[wx][wy] = 1
    for vx, vy in viruses:
        expand(vx, vy, changed)
    answer = max(answer, count_safe(changed))

print(answer)
