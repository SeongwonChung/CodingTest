from itertools import combinations
from copy import deepcopy

n = int(input())
teachers = []
spaces = []
graph = []
for i in range(n):
    row = list(input().split())
    graph.append(row)
    for j in range(n):
        if row[j] == "X":
            spaces.append((i, j))
        elif row[j] == "T":
            teachers.append((i, j))


def watch(teacher, direction, graph):
    r, c = teacher

    if direction == 0:  # top
        while r >= 0:
            if graph[r][c] == "S":
                return True
            if graph[r][c] == "O":
                return False
            r -= 1
    if direction == 1:  # bottom
        while r < n:
            if graph[r][c] == "S":
                return True
            if graph[r][c] == "O":
                return False
            r += 1
    if direction == 2:  # left
        while c >= 0:
            if graph[r][c] == "S":
                return True
            if graph[r][c] == "O":
                return False
            c -= 1
    if direction == 3:  # right
        while c < n:
            if graph[r][c] == "S":
                return True
            if graph[r][c] == "O":
                return False
            c += 1
    return False


spaces_comb = list(combinations(spaces, 3))


def put_objects(graph, comb):
    ret = deepcopy(graph)
    for r, c in comb:
        ret[r][c] = "O"
    return ret


result = False

for comb in spaces_comb:
    graph_with_objects = put_objects(graph, comb)

    success = True
    for teacher in teachers:
        for d in range(4):
            if watch(teacher, d, graph_with_objects):
                success = False
                break
        if not success:
            break

    if success:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")
