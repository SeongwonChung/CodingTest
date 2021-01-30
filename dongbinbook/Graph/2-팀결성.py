n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = []


def checkTeam(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        result.append("YES")
    else:
        result.append("NO")


for _ in range(m):
    t, a, b = map(int, input().split())
    if t:
        checkTeam(parent, a, b)
    else:
        union(parent, a, b)

for s in result:
    print(s)