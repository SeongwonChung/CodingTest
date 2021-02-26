def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, i + 1, j + 1)

cities = list(map(int, input().split()))
result = "YES"
p = []
for city in cities:
    p.append(find_parent(parent, city))
print(p)
if len(set(p)) != 1:
    result = "NO"
print(result)
