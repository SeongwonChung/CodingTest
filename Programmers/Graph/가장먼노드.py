"""
우선순위큐 다익스트라로 풀이.
"""
import heapq


def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF for _ in range(n + 1)]

    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def dijkstra(s):
        distance[s] = 0
        q = []
        heapq.heappush(q, (0, s))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for v in graph[now]:
                cost = dist + 1
                if cost < distance[v]:
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))

    dijkstra(1)
    distance = list(filter(lambda x: x < INF, distance))
    answer = distance.count(max(distance))
    return answer