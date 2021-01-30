"""
minimum spanning tree 알고리즘 - kruskal, prim

**kruskal**

Greedy algorithm!
모든 edge weight에 따라 정렬한뒤, 가장 거리가 짧은 것 부터 집합에 포함한다. 단, 사이클이 발생할 경우 제외한다.

parent list에 각 노드의 root node 정보를 저장.
이를 통해 union, find 연산 구성
이를 사용해 아래 과정 수행

1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    - 사이클이 발생하지 않는 경우, 최소신장트리에 포함
    - 사이클이 발생할 경우, 최소신장트리에 포함 x
3. 모든 간선에 대해 2. 반복
"""

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드가 아니면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산) 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종비용 담을 변수
edges = []
result = 0

# 부모테이블에서 부모를 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


# 모든 간선정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클 아닌경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)

"""
시간복잡도: O(ElogE)
간선 정렬에 ElogE만큼 걸린다. union/find는 그보다 적은 시간이므로 무시.
"""