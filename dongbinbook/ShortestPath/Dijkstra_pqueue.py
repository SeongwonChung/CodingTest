import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드개수, 간선개수 입력받기
v, e = map(int, input().rstrip().split())
# 시작노드번호 입력받기
s = int(input().rstrip())
# 그래프 연결정보 adjacency list
graph = [[] for i in range(v + 1)]
# 최단거리 테이블 초기화
distance = [INF] * (v + 1)

# 간선정보 입력받기
for _ in range(e):
    # a => b, weight = c
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면,
        # 가장 최단거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드이면 무시 -- 이미 처리된 최단거리값이 더 작으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재노드(now)거쳐서 가는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(s)

# 모든 노드로의 최단거리 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


"""
시간복잡도: O(ElogV)
우선순위 큐를 사용하여 최단거리가 가장 짧은 노드를 선정한다. 따라서 기존의 순차탐색을 통한 다익스트라알고리즘보다 속도가 빠르다.

우선순위큐에 E개의 원소를 넣었다 빼는 연산과 유사하여 간단하게 O(ElogE)로 나타낼 수 있는데, logE는 항상 logV^2보다 작고, 빅오로 나타내면 
O(logE) 보다 O(logV^2) == O(logV)는 항상 크므로 O(ElogV)로 이해할 수 있다.

"""