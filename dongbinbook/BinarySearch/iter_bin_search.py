#반복문으로 구현한 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은 경우, 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값이 target보다 큰 경우
        elif array[mid] >target:
            end = mid - 1
        # 중간점 값이 target보다 작은 경우
        else:
            start = mid + 1
    return None

#n(원소의 개수)과 target(찾고자 하는 문자열)입력받기
n, target = map(int, input().split())
# 전체원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)