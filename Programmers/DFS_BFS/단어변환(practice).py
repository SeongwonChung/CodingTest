def overlap(word, compare):
    cnt = 0
    for i in range(len(word)):
        if word[i] == compare[i]:
            cnt+= 1
    return cnt

def dfs(index, words, depth, target):
    visited = [0] * len(words)
    visited[index] = 1
    
    if words[index] == target:
        print(" finish at ", index)
        return
    
    for j in range(len(words)):
        if overlap(words[index], words[j]) == len(target)-1 and visited[j] == 0:
            visited[j] = 1
            print(words[j], " ")
            depth+=1
            dfs(j, words, depth, target)
            
def solution(begin, target, words):
    answer = 0
    stages=[]
    
    for i in range(len(words)):
        # visited = [0] * len(words)
        depth = 0
        if overlap(begin, words[i]) == len(target)-1:
            # visited[i] = 1
            print(words[i], " -so ")
            depth += 1
            dfs(i, words, depth, target)
        stages.append(depth)
    
    if len(stages) == 0:
        answer = 0
    else:
        answer = min(stages)

    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])