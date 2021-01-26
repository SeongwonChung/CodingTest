"""
disjoint set source code
"""

# 특정 원소가 속한 집합을 찾기(find)
# 이 경우, find 는 O(V)이다.
def find_parent(parent, x):
    # 루트노드 아니면 재귀적으로 호출하여 루트노드를 찾는다.
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 경로압축 기법 적용한 find 함수
# 재귀적으로 호출한 뒤 부모테이블 갱신
def find_parent_compress(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기(union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 출력
print("부모 테이블: ", end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")


""" 
노드의 개수가 V일때, V-1개의 Union 연산과 M개의 find연산이 가능하다면 
시간복잡도는 O(V + M(1 + log_/(2-m/v)V))

"""