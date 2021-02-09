def solution(s):
    answer = len(s)
    for window in range(1, len(s) // 2 + 1):
        compressed = ""
        count = 1
        i = 0
        while True:
            left = s[window * i : window * (i + 1)]
            if window * (i + 2) > len(s):
                if count == 1:
                    compressed += left
                else:
                    compressed += str(count) + left
                rest = s[window * (i + 1) :]
                compressed += rest
                break
            right = s[window * (i + 1) : window * (i + 2)]
            if left == right:
                count += 1
            else:
                if count == 1:
                    compressed += left
                else:
                    compressed += str(count) + left
                count = 1
            i += 1
        print(window, compressed)
        answer = min(answer, len(compressed))

    return answer


print(solution("a"))
