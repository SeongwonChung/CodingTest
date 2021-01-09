"""
반복되는 수열의 형태
first * K + second 의 형태로 총 숫자 개수가 M개일때 까지 반복된다. 
따라서 (first*K + second)가 (M//(K+1))번 반복되고, first가 (M%(K+1))번 더해진 값이 정답이다.
"""
N, M, K = map(int, input().split())
data = list(map(int, input().split())).sort(reverse=True)

first = data[0]
second = data[1]

answer = (first * K + second) * (M//(K+1)) + first * (M%(K+1))
print(answer)