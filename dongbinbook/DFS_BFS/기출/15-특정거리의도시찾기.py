import heapq

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
INF = int(1e9)
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for adj in graph[now]:
            cost = dist + adj[0]
            if cost < distance[adj[1]]:
                distance[adj[1]] = cost
                heapq.heappush(q, (cost, adj[1]))


dijkstra(x)

if distance.count(k) == 0:
    print(-1)
else:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)

"""
다익스트라 사용 => 시간초과
모든 간선의 길이가 1로 주어졌으므로 
BFS로 최단거리를 구할 수 있다.
"""