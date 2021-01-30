from collections import defaultdict
import heapq
# min priority queue 사용위해서 heapq 모듈 사용.
INF = int(1e9)
graph=[
    [2,8],
    [1,3,8],
    [2,4,6,9],
    [3,5,6],
    [4,6],
    [3,4,5,7],
    [6,8,9],
    [1,2,7,9],
    [3,7,8]
]
weight = [
    [0, 4, INF, INF, INF, INF, INF, 8, INF],
    [4, 0, 8, INF, INF, INF, INF, 11, INF],
    [INF, 8, 0, 7, INF, 4, INF, INF, 2],
    [INF, INF, 7, 0, 9, 14, INF, INF, INF],
    [INF, INF, INF, 9, 0, 10, INF, INF, INF],
    [INF, INF, 4, 14, 10, 0, 2, INF, INF],
    [INF, INF, INF, INF, INF, 2, 0, 1, 6],
    [8, 11, INF, INF, INF, INF, 1, 0, 7],
    [INF, INF, 2, INF, INF, INF, 6, 7, 0]
]
def prim(graph, weight, root):
    mst = list()

    key=[[] for _ in range(len(graph))]
    pi=[[] for _ in range(len(graph))]
    for i in range(len(graph)):
        key[i] = INF
        pi[i] = None
    key[root] = 0
    q = heapq.heapify()
        

"""
나중에 다시 check
"""