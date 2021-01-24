def solution(triangle):
    answer = 0
    dp = []
    for row in triangle:
        dp.append([0] * len(row))

    dp[0][0] = triangle[0][0]
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    answer = max(dp[-1])
    return answer