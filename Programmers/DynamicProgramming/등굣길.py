def solution(m, n, puddles):
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (m + 1))
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j - 1, i] not in puddles and j > 1:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % 1000000007
            if [j, i - 1] not in puddles and i > 1:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % 1000000007
    answer = dp[n][m]

    return answer