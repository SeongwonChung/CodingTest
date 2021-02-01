from itertools import combinations


def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n - 1)


n, m = map(int, input().split())
weights = list(map(int, input().split()))
weight_comb = combinations(weights, 2)

weight_set = set(weights)
same = 0
for w in weight_set:
    cnt = weights.count(w)
    if cnt > 1:
        same += facto(cnt) // facto(2) * facto(cnt - 2)
print("same", same)

result = len(list(weight_comb)) - same
print("result", result)
