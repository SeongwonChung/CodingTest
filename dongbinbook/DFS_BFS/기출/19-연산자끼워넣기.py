n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_ = int(1e9)
max_ = -int(1e9)


def dfs(i, now):
    global min_, max_, add, sub, mul, div

    if i == n:
        min_ = min(min_, now)
        max_ = max(max_, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1


# call dfs method
dfs(1, data[0])

print(max_)
print(min_)

# // 연산자는 floor devision. 음수 나누기할때 주의!
# -5 // 2 = -3
# int( -5 / 2 ) = -2
# -5 / 2  = -2.5
