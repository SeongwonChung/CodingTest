from copy import deepcopy

graph = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

new_graph = deepcopy(graph)
new_graph[1][1] = 100
print(graph)

old = [1, 2, 3]
new = old[:]
new[1] = 100
print(old)