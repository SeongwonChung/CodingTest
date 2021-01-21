dp = [0] * 30001

X = int(input())


# def make1(X):
#     if dp[X] != 0:
#         return dp[X]

#     if X % 5 == 0:
#         dp[X] = X // 5
#     elif X % 3 == 0:
#         dp[X] = X // 3
#     elif X % 2 == 0:
#         dp[X] = X // 2
#     else:
#         dp[X] = X - 1
#     return dp[X]

# count = 0
# while True:
#     if X == 1:
#         break
#     else:
#         X = make1(X)
#         count += 1

# bottom up dynamic programming
for i in range(2, X + 1):
    # -1
    dp[i] = dp[i - 1] + 1  # +1 => 연산 횟수 count

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[X])