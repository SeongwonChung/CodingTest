#1트
# from collections import deque
# def solution(tickets):
#     answer = []

#     deps = dict()
#     for ticket in tickets:
#         if ticket[0] in deps:
#             deps[ticket[0]].append(ticket[1])
#         else:
#             deps[ticket[0]] = deque([ticket[1]])
#         if ticket[1] not in deps:
#             deps[ticket[1]] =deque([])
            
#     for key in deps:
#         deps[key] = deque(sorted(deps[key]))

#     def dfs(dep, answer):
#         print(deps)
#         answer.append(dep)
#         if not deps[dep]:
#             return
#         else:
#             test=answer[:]
#             _next=""
#             while deps[dep]:
#                 to = deps[dep].popleft()
#                 dfs(to, test)
#                 if len(test) == len(tickets):
#                     _next=to
#                     print('_next', _next)
#                     break
#                 else: 
#                     deps[dep].append(to)
#             dfs(_next, answer)
#     dfs("ICN", answer)
#     return answer

#2트
# def solution(tickets):
#     answer = []

#     deps = dict()
#     for ticket in tickets:
#         if ticket[0] in deps:
#             deps[ticket[0]].append(ticket[1])
#         else:
#             deps[ticket[0]] = [ticket[1]]
#         if ticket[1] not in deps:
#             deps[ticket[1]] =[]
            
#     for key in deps:
#         deps[key].sort()
#     def dfs_test(dep, answer):
#         test = answer[:]
#         print('test',test)
#         dfs(dep, test)
#         if len(test) == len(tickets):
#             return True
#         return False
            
#     def dfs(dep, answer):
#         print('deps',deps)
#         answer.append(dep)
#         if not deps[dep]:
#             return
#         else:
#             next = deps[dep][0]
#             if dfs_test(next, answer):
#                 deps[dep].pop(0)
#                 dfs(next, answer)
#     dfs("ICN", answer)
#     return answer

#3트
def solution(tickets):
    answer = []

    deps = dict()
    for ticket in tickets:
        if ticket[0] in deps:
            deps[ticket[0]].append(ticket[1])
        else:
            deps[ticket[0]] = [ticket[1]]
        if ticket[1] not in deps:
            deps[ticket[1]] =[]
            
    for key in deps:
        deps[key].sort()
    
    stack=["ICN"]
    while stack:
        top = stack[-1]
        if len(deps[top])==0:
            answer.append(stack.pop())
        else:
            stack.append(deps[top].pop(0))
    answer.reverse()            
        
    return answer

print('ans', solution([["ICN", "B"], ["ICN", "C"], ["C", "D"], ["D", "ICN"]]))