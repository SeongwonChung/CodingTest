"""
집합자료형 set을 활용한 풀이.
한번씩 등장여부만 확인하면 되므로 set을 사용하여 처리한다.

집합자료형의 특징은
1. 중복을 허용하지 않는다.
2. 순서가 없다.
"""
N = int(input())
array = set(map(int, input().split()))

M = int(input())
for x in list(map(int, input().split())):
    if x in array:
        print('yes',end=' ')
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