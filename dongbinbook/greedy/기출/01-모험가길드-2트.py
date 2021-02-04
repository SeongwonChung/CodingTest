n = int(input())
people = list(map(int, input().split()))

counts = [0] * (n + 1)
for i in range(1, n + 1):
    counts[i] = people.count(i)

groups = 0
for i in range(1, n + 1):
    groups += counts[i] // i
    counts[i] = counts[i] % i

print(groups)


### 정석 정답
def count_group(n, people):
    people.sort()
    result = 0
    count = 0
    for i in people:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result


print(count_group(n, people))
