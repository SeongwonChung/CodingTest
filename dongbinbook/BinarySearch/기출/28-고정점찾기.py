n = int(input())
numbers = list(map(int, input().split()))


def bin_search(numbers, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2
    if numbers[mid] == mid:
        return mid
    left = bin_search(numbers, start, mid - 1)
    if left != -1:
        return left
    right = bin_search(numbers, mid + 1, end)
    if right != -1:
        return right

    return -1


print(bin_search(numbers, 0, n - 1))
