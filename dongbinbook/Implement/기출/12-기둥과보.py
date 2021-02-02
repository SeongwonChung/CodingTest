def solution(n, build_frame):
    answer = []
    graph = [[(-1, [])] * (n + 1) for _ in range(n + 1)]

    def insert(n, x, y, roof):
        cond = []
        if roof == 1:
            if graph[y - 1][n - x] == 0:
                cond.append(1)
            if graph[y - 1][n - (x + 1)] == 0:
                cond.append(2)
            if graph[y][n - (x - 1)] == 1 and graph[y][n - (x + 1)] == 1:
                cond.append(3)
        else:
            if y == 0:
                cond.append(1)
            if graph[y][n - (x - 1)] == 1:
                cond.append(2)
            if graph[y - 1][n - x] == 0:
                cond.append(3)
        if len(cond) > 0:
            graph[y][n - x] = (roof, cond)

    def delete(n, x, y, roof):
        if roof == 1:
            if graph[y][n - (x + 1)] == 0 and graph[y][n - (x + 1)][1] == [2]:
                return
            if graph[y][n - (x - 1)] == 1 and graph[y][n - (x - 1)][1] == [3]:
                return
            if graph[y][n - (x + 1)] == 1 and graph[y][n - (x + 1)][1] == [3]:
                return
        else:
            if graph[y + 1][n - x] == 0 and graph[y + 1][n - x][1] == [3]:
                return
            if graph[y + 1][n - x] == 1 and graph[y + 1][n - x][1] == [1]:
                return
            if graph[y + 1][n - (x - 1)] == 1 and graph[y + 1][n - (x - 1)][1] == [2]:
                return
        graph[x][y] = (-1, [])

    for command in build_frame:
        x, y, roof, ins = command
        if ins:
            insert(n, x, y, roof)
        else:
            delete(n, x, y, roof)

    for i in range(len(graph)):
        for j in range(len(graph)):
            _type, cond = graph[i][j]
            if _type > -1:
                answer.append([j, n - i, _type])

    answer.sort()
    print(answer)
    return answer