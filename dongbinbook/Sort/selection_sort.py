array = [7,5,3,6,4,1,2,9,0,8]
# selection sort(ascending)
for i in range(len(array)):# n-1번 반복
    # 가장 작은 수 찾아서 앞으로
    min_idx = i
    for j in range(i, len(array)):
        if array[min_idx] > array[j]:
            min_idx=j
    #swap
    array[i], array[min_idx] = array[min_idx], array[i]

"""
선택정렬
시간복잡도: O(n^2)
"""