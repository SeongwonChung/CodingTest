n = int(input())
data = []
for _ in range(n):
    info = input().split()
    info = [info[0]] + list(map(int, info[1:]))
    data.append(info)

data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for info in data:
    print(info[0])