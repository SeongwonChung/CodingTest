n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1
total = 0
for i in range(1, 11):
    total += array[i] * sum(array[i + 1 :])

print(total)
