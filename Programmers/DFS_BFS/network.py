def dfs(graph, v, visited):
    visited[v] = True
    n = len(graph)
    
    for node in range(n):
        if graph[v][node] == 1 and visited[node] == False:
            dfs(graph, node, visited)
            
def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    for start in range(n): # n개의 node를 각각 시작 노드로 dfs
        if visited[start] == 0: # 이전 탐색에서 방문하지 않았을 경우에만 탐색 시작
            dfs(computers, start, visited)
            answer += 1
    
    return answer