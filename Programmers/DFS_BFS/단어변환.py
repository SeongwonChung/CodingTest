def solution(begin,target,words):
    answer = 0
    visited = [0]*len(words)
    stages = []
    
    def isLinked(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt+=1
        if cnt == 1: 
            return True
        return False

    def dfs(word, depth):
        # target word일 경우, 멈추고 depth를 기록
        if word == target:
            stages.append(depth)
            return
        else:
            for i in range(len(words)):
                if isLinked(word, words[i]) and visited[i] == 0:
                    visited[i] = 1 
                    dfs(words[i], depth+1)
                    visited[i] = 0 # 특정 노드에서 가능한 모든 변환과정 기록 후에는 방문처리 해제

    dfs(begin, 0)

    if stages:
        answer = min(stages)
    return answer