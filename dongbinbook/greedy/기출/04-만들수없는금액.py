from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)
print(coins)


def find_min(coins):
    for num in range(1, 1000000):
        result = num
        for coin in coins:
            if coin <= result:
                print("result-coin", result, "-", coin)
                result -= coin
            if result == 0:
                break
        if result != 0:
            return num


print(find_min(coins))