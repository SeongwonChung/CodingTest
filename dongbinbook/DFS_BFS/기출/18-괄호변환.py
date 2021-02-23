def isBalanced(w):
    stack = []
    brackets = list(w)
    for bracket in brackets:
        if len(stack) == 0:
            stack.append(bracket)
        elif bracket == ")" and stack[-1] == "(":
            stack.pop()
        elif bracket == "(" and stack[-1] == ")":
            stack.pop()
        else:
            stack.append(bracket)
    if len(stack) == 0:
        return True
    return False


def isCorrect(w):
    stack = []
    brackets = list(w)
    for bracket in brackets:
        if len(stack) == 0:
            stack.append(bracket)
        elif bracket == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(bracket)
    if len(stack) == 0:
        return True
    return False


def solution(p):
    answer = ""
    if len(p) == 0:
        return answer
    if isCorrect(p):
        return p
    u = ""
    v = ""
    for i in range(1, len(p) + 1):
        u = p[:i]
        v = p[i:]
        if isBalanced(u):
            break
    if isCorrect(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for b in u:
            if b == "(":
                answer += ")"
            elif b == ")":
                answer += "("

    return answer


print(solution("()))((()"))