N = int(input())
parts = list(map(int, input().split()))
M = int(input())
requests = list(map(int, input().split()))

parts.sort()
print(parts)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for request in requests:
    if binary_search(parts, request, 0, len(parts)-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')

"""
example input
5
8 3 7 9 2
3 
5 7 9

answer: no yes yes
"""