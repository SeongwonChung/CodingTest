def solution(s):
    length = len(s)
    answer = length
    for w in range(1, length // 2 + 1):
        compressed = ""
        count = 1
        _cur = s[0:w]
        for j in range(w, length, w):
            if _cur == s[j : j + w]:
                count += 1
            else:
                compressed += str(count) + _cur if count >= 2 else _cur
                _cur = s[j : j + w]
                count = 1
        compressed += str(count) + _cur if count >= 2 else _cur
        answer = min(answer, len(compressed))

    return answer