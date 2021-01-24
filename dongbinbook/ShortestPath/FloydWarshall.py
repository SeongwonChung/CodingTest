"""
Floyd-Warshall algorithm
플로이드워셜 알고리즘
adjacency matrix를 활용하여 모든 노드간의 최단거리 정보를 알아낸다.
Dijkstra가 single source shortest path로 특정 시작노드에서의 최단거리를 구한다면,
FloydWarshall은 All-pair shortest path로 모든 노드들 간의 최단거리를 구할 수 있다.

노드의 개수가 V일 때, 시간복잡도는 O(V^3)이다. 

최단거리 테이블을 V*V 형태로 구성하고, 
이 안에서 현재 노드 (k) 를 제외한 노드들의 쌍 (a,b) 에 대해 
D_ab = min(D_ab, D_ak + D_kb) 와 같은 식으로 update한다.
다익스트라가 그리디 알고리즘을 사용하는데, 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 알고리즘을 사용한다.
"""

INF = int(1e9)

# 노드 개수 및 간선 개수 입력받기
v = int(input())
e = int(input())
# 2차원 리스트 만들고 (adjacency matrix)모든 값 무한으로 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 입력받아서 graph 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    # a=>b, weight: c
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행결과 출력
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()  # 개행
