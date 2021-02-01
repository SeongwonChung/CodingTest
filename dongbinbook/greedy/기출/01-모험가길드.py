n = int(input())
people = list(map(int, input().split()))

people.sort()
total = 0
group = []
for i in range(n):
    group.append(people[i])
    if people[i] <= len(group):
        total += 1
        group = []
print("total", total)
