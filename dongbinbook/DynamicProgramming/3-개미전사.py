n = int(input())
containers = list(map(int, input().split()))

# 계산결과 저장을 위한 dp table
dp = [0] * (n + 1)

# dynamic programming
dp[0] = containers[0]
dp[1] = max(containers[0], containers[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + containers[i])

print(dp[n - 1])
