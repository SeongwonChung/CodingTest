# 풀이 1 -- 테스트케이스 통과 못함.
def solution1(n, times):
    answer = 0

    start = 1
    end = n * min(times)
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for t in times:
            total += mid // t

        if total == n:
            answer = mid
            break
        elif total > n:
            end = mid - 1
        else:
            start = mid + 1

    # n명 심사가능한 시간 찾은 후에 1씩 줄여가면서 최솟값 찾기
    check = False
    while True:
        for t in times:
            if answer % t == 0:
                check = True
                break
        if check:
            break
        answer -= 1
    return answer


# 풀이 2 -- 6,9번 런타임 에러
def solution(n, times):
    answer = 0
    answers = []

    start = 1
    end = n * min(times)
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for t in times:
            total += mid // t

        if total == n:
            # n명 심사 가능한 시간 찾으면 배열에 넣고, 다시 왼쪽으로 이분탐색(최솟값 찾기 위해)
            answers.append(mid)
            end = mid - 1
        elif total > n:
            end = mid - 1
        else:
            start = mid + 1

    answer = min(answers)
    return answer