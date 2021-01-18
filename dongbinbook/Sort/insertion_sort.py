array = [7,5,3,6,4,1,2,9,0,8]
# Insertion sort(ascending)
for i in range(1,len(array)):# n-1번 반복
    print('sorted', array[:i])
    for j in range(i, 0, -1):
        print('i,j', i, j)
        if array[j] > array[j-1]:
            break
        array[j],array[j-1] = array[j-1],array[j]

"""
삽입정렬
시간복잡도: O(n^2)

미리 정렬되어 있는 형태에서는 최고 O(N)까지 빨라져 효율적.
"""