n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[n] = (2 * dp[n - 2] + dp[n - 1]) % 796796

print(dp[n])


"""
점화식
a_n = a_(n-1) + 2 * a_(n-2)

"""