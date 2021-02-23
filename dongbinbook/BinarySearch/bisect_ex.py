"""
bisect library
birsect_left(a, x): 정렬순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 찾기
birsect_right(a, x): 정렬순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 찾기
시간복잡도 O(logN)
"""
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8, 15]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))