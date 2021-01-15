from collections import deque

N, M = map(int, input().split())
graph=[[0]*M]
for i in range(N):
    graph.append([0] + list(map(int, input())))
print('graph:',graph)

visited=[]
for _ in range(N+1):
    row=[0]*(M+1)
    visited.append(row)
print('visited:', visited)

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def checkMove(x, y, graph):
    if x in range(1, N+1) and y in range(1, M+1) and graph[x][y] > 0:
        return True
    return False

def bfs(x, y, visited):
    queue = deque([(x,y)])

    while queue:
        node = queue.popleft()
        visited[node[0]][node[1]] = 1
        distance = graph[node[0]][node[1]]
        for d in range(4):
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]
            if checkMove(nx, ny, graph) and visited[nx][ny] == 0:
                graph[nx][ny] = distance+1
                queue.append((nx, ny))

bfs(1, 1, visited)
for i in range(N+1):
    print(graph[i])
    
answer = graph[N][M]
print('answer: ', answer)

"""input
5 6
101010
111111
000001
111111
111111

answer: 10
"""