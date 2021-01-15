N, M = map(int, input().split())
_map=[]
for _ in range(N):
    _map.append(list(map(int, list(input()))))
# print("map", _map)

#상하좌우
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def checkMap(_map, nx, ny):
    if nx in range(N) and ny in range(M) and _map[nx][ny]==0:
        return True
    return False

# make graph as adjacency list (2차원 list의 각 원소가 연결된 node 의 list)
graph=[]
for _ in range(N):
    row=[]
    for _ in range(M):
        row.append([])
    graph.append(row)

for x in range(N):
    for y in range(M):
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if _map[x][y] == 0 and checkMap(_map, nx, ny):
                graph[x][y].append((nx, ny))
print("graph", graph)

# dfs
def dfs(x, y):
    _map[x][y] = 1
    for node in graph[x][y]:
        nx=node[0]
        ny=node[1]
        if _map[nx][ny] == 0:
            dfs(nx, ny)

# dfs 통해 탐색하면서 count
answer=0
for x in range(N):
    for y in range(M):
        if _map[x][y] == 0:
            answer+=1
            dfs(x, y)
print('answer: ', answer)

"""input
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
