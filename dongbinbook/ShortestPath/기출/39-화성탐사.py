import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
t = int(input())
for tc in range(t):
    n = int(input())

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    d = [[INF] * n for i in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    d[x][y] = graph[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        dist, x, y = heapq.heappop(q)

        if d[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < d[nx][ny]:
                d[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(d[n - 1][n - 1])
