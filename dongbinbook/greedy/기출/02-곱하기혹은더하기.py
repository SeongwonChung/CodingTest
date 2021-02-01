S = list(map(int, input()))
print(S)
result = S[0]
for i in S[1:]:
    if i < 2 or result < 2:
        result += i
    else:
        result *= i
    print(i, result)
print(result)