from collections import deque
import copy

n = int(input())
times = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    times[i] = row[0]
    for j in row[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

print(times)
print(graph)
print(indegree)

# topology sort
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

total = copy.deepcopy(times)
while q:
    now = q.popleft()

    for i in graph[now]:
        total[i] = max(total[i], total[now] + times[i])
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(total[i], end=" ")
