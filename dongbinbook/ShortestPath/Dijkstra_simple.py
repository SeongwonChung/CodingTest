import sys

input = sys.stdin.readline
INF = int(1e9)

# node 개수, edge 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
s = int(input().rstrip())
# 각 노드에 연결되어있는 노드 정보 담는 리스트 만들기(adjacency list 방식)
graph = [[] for i in range(n + 1)]
# 방문여부 체크 리스트 만들기
visited = [False] * (n + 1)
# 최단거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a => b, weight = c
    graph[a].append((b, c))  # (도착 노드, weight) 형태로 저장

# 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 번호 반환(순차 탐색 통해서)
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단거리가 짧은 노드 index
    # 최단거리 테이블 순차탐색
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    visited[start] = True
    # 최단거리 테이블 시작노드 연결정보로 update
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드 제외, 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재노드(now)와 연결된 노드 확인
        for j in graph[now]:
            # 현재 노드 거쳐서 연결된 노드로 가는 비용
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(s)


# 모든 노드로 가기위한 최단거리를 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

"""
시간복잡도: O(V^2)
총 O(V)번에 거쳐서 최단거리가 가장 짧은 노드를 찾기위해 최단거리 테이블을 매번 선형 탐색해야한다. 

전체노드개수가 5000개 이하라면 코테에서 가능 but 이상일 경우 다른 방법 필요!
"""