N, M = map(int, input().split())
rods = list(map(int, input().split()))

# h를 최댓값에서 하나씩 줄여가면서 test를 이진탐색을 활용.
# rods = sorted(rods)
# h = rods[-1]
# def binarySearch(array, M, start, end):
#     mid = (start + end) //2
#     if start > end:
#         return None
    
#     if sum(array[mid:]) - (len(array) - mid)*h >= M:
#         print('mid', mid)
#         return mid
#     else:
#         return binarySearch(array, M, start, mid-1)

# while h >=0 :
#     if binarySearch(rods, M, 0, len(rods)-1):
#         break
#     else: 
#         h-=1

# print(h)


# 풀이2(교재 풀이): 중간점을 떡을 자르는 높이로 보고, 이진탐색을 통해 찾는 풀이
start = 0
end = max(rods)

#binary search(iter)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2

    # mid에서 잘랐을 때 떡의 양.
    for rod in rods:
        if rod > mid:
            total += (rod - mid)
    
    # 떡의 양이 부족한 경우 - 자르는 높이를 줄인다. (중간점을 왼쪽으로)
    if total < M:
        end = mid-1
    # 떡의 양이 충분한 경우 - 자르는 높이(중간점) 기록한 후, 높인다.
    else:
        result = mid #최대한 덜 잘랐을 때가 
        start = mid+1

print(result)
"""
input

4 6
19 15 10 17
"""