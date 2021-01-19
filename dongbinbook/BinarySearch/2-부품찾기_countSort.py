N = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)] += 1

M = int(input())
requests = list(map(int, input().split()))

for req in requests:
    if array[req] > 0:
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