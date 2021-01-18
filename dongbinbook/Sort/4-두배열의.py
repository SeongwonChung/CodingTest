N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse=True)

for i in range(K):
    # A의 최솟값이 B의 최댓값보다 큰 경우, 바꿔치기 stop
    if A[i] >= B[i]:
        break
    A[i],B[i] = B[i],A[i]

print(sum(A))