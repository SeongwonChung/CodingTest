N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# 내림차순으로 정렬
numbers = sorted(numbers, reverse=True)
answer = 0
cnt = 0
print(N, M, K)
print('numbers:' , numbers)

while True:
    # K번까지 가장 큰수를 더한다.
    for _ in range(K):
        # 총 더하는 횟수 도달 시 종료
        if cnt >= M:
            break   
        answer += numbers[0]
        cnt+= 1
        
    # 총 더하는 횟수 도달 시 종료
    if cnt >= M:
        break   
    # 두번째로 큰 수를 한번 더한다. 
    answer+= numbers[1]
    cnt += 1

print(answer)
