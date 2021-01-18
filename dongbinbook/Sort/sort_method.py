"""
sorted - O(NlogN)
정렬해서 리스트로 반환
"""
array = [1,6,3,6,8,8,6,2,67,9,0]
result = sorted(array)

print('sorted', result)

"""
.sort() => list 의 method
return 없이 list가 바로 sort됨
"""
array.sort()
print('.sort', array)

pairs = [('성원', 25), ('다운', 23), ('재원', 26), ('범수', 30)]

key_sort = sorted(pairs, key=lambda x: x[1]) # key에 함수를 통해 정렬.
print('keysort', key_sort)
