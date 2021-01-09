"""
N을 K로 나눈 나머지를 구해서, 그 값만큼 N에서 빼주는 1. 을 반복후에 2. 를 반복해 최대한 N을 나눈다.
K >= 2 이므로 2번을 많이 반복할수록 최솟값을 구할 수 있다.
"""
N, K = map(int, input().split())
answer = 0

while True:
    if N < K:
        break
    #1. N이 K의 배수가 될때까지 1 빼기
    r = N % K
    N = N - r
    answer += r

    if N < K:
        break
    #2. K로 나누기
    N = N//K
    answer += 1

#나머지 수에 대해 N==1 될 때까지 1. 을 N-1번 반복
answer += N-1
print(answer)
