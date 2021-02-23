n = int(input())
houses = list(map(int, input().split()))
houses.sort()

median = (n - 1) // 2

print(houses[median])