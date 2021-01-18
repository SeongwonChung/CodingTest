array=[5,7,3,6,4,9,0,8,1,2]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right: #엇갈릴때까지 반복
        #피벗보다 큰 데이터 찾을때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 작은 데이터 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: #엇갈린경우 -- 작은값과 피벗 교체 
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않은 경우 -- 작은값(right)과 큰값(left)교체
            array[left], array[right] = array[right], array[left]
        
    #분할 이후(right --작은값위치에 pivot들어옴) 기준 왼쪽, 오른쪽도 sort
    quick_sort(array, start, right-1) 
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

"""
퀵정렬
평균 시간복잡도: O(NlogN) -- 배열이 절반씩 분할될 경우
최악의 경우에는 O(N^2) -- 가장 왼쪽 데이터를 피벗으로 시작할 때, 배열이 정렬되어 있을 경우 매우 느림. 

파이썬 정렬 라이브러리 - O(NlogN) 보장함.🍯
"""