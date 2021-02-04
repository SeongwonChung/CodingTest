def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]

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

    costs = sorted(costs, key=lambda cost: cost[2])

    for cost in costs:
        a, b, dist = cost
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += dist

    return answer


## 크루스칼 알고리즘 문제!