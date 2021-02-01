# def solution(food_times, k):
#     answer = 0
#     index = 0
#     spin_index = index % len(food_times)
#     for i in range(k):
#         while True:
#             if food_times[spin_index] != 0:
#                 break
#             index += 1
#             spin_index = index % len(food_times)
#         food_times[spin_index]-=1
#         index += 1
#         spin_index = index % len(food_times)

#     while True:
#             if food_times[spin_index] != 0:
#                 break
#             index += 1
#             spin_index = index % len(food_times)

#     if food_times.count(0) == len(food_times):
#         return -1

#     answer = (spin_index+1) % len(food_times)
#     return answer

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    prev = 0
    length = len(food_times)
    while sum_value + (q[0][0] - prev) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * length
        length -= 1
        prev = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


solution([3, 1, 2], 5)
