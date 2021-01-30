"""
위상정렬
Topology Sort
방향그래프의 모든 노드를 '방향성'에 거스르지 않도록 순서대로 나열하는 것.

Indegree(진입차수): 노드로 들어오는 edge개수

위상정렬 알고리즘
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌때까지 아래를 반복
    i. 큐에서 원소를 꺼내 해당노드에서 출발하는 간선을 그래프에서 제거한다.
    ii. 새롭게 진입차수가 0이된 노드를 큐에 넣는다.

위 과정에서 큐에서 빠져나온 노드 순서대로 => 위상정렬 결과.
위상정렬은 한 단계에서 큐에 삽입되는 노드가 여러개일 경우, 답이 여러개일 수 있다.

"""
from collections import deque

v, e = map(int, input().split())
# 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선정보를 담기위한 linked list 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a -> b
    indegree[b] += 1

# 위상정렬
def topology_sort():
    result = []
    q = deque()

    # 처음 시작시 진입차수가 0인 노드 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 꺼낸 노드 결과에 기록
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0인 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=" ")


topology_sort()

"""
위상정렬의 시간복잡도: O(V+E)
차례대로 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거해야 한다.
따라서 모든 노드와 간선을 확인하므로 O(V+E)이다.
"""
