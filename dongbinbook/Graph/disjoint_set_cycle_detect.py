"""
서로소 집합으로 무뱡향 그래프에서 사이클을 판별할 때 사용할 수 있다.

union연산은 간선으로 표현된다. 
간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것 만으로 사이클을 판별할 수 있다.

그래프에 포함되어 있는 간선의 개수가 E일때, 모든 간선을 하나씩 확인하며, 매 간선에 대해 union, find를 호출하는 방식.
무향그래프에만 적용 가능
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())

    # 사이클 발생시 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("cycle exists")
else:
    print("no cycle")
