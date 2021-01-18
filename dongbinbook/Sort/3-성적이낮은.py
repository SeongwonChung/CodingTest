N = int(input())
array=[]
for _ in range(N):
    name, score = input().split()
    score = int(score)
    array.append((name, score))

array = sorted(array, key=lambda x: x[1])

for info in array:
    print(info[0], end=' ')

