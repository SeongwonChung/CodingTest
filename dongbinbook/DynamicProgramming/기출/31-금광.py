def get_max(r, graph, n, m):
    dp = [0] * m
    dp[0] = graph[r][0]

    for c in range(1, m):
        top, mid, bottom = (-1, -1, -1)

        if r - 1 >= 0 and r - 1 < n:
            top = graph[r - 1][c]
        if r >= 0 and r < n:
            mid = graph[r][c]
        if r + 1 >= 0 and r + 1 < n:
            bottom = graph[r + 1][c]
        max_gold = max(top, mid, bottom)

        if max_gold == top:
            r = r - 1
        elif max_gold == bottom:
            r = r + 1

        dp[c] = dp[c - 1] + max_gold

    print(dp)
    return dp[m - 1]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    data = list(map(int, input().split()))
    for r in range(n):
        graph.append(data[r * m : r * m + m])

    total_gold = [0] * n
    for r in range(n):
        total_gold[r] = get_max(r, graph, n, m)
    print(total_gold)
    print(max(total_gold))
