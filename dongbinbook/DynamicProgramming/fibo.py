# recursion without memoization => O(2^n)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


d = [0] * 100

# Dynamic Programming -- memoization (topdown)활용! O(N)의 시간복잡도.
def fiboMemo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fiboMemo(x - 1) + fiboMemo(x - 2)
    return d[x]


dp = [0] * 100


def fiboBottomUp(x):
    d[1] = 1
    d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[x]


# print(fiboMemo(99))
print(fiboBottomUp(99))