# 맞았으나 시간초과..
def solution(routes):
    answer = 0
    counts = [0] * 60001
    cars = []
    for route in routes:
        s, e = route[0] + 30000, route[1] + 30000
        cars.append((s, e))
        for i in range(s, e + 1):
            counts[i] += 1

    while cars:
        camera = counts.index(max(counts))
        answer += 1
        for s, e in cars[:]:
            if camera >= s and camera <= e:
                for i in range(s, e + 1):
                    counts[i] -= 1
                cars.remove((s, e))
    return answer

    ##그리디 풀이
    def solution(routes):
    routes = sorted(routes, key=lambda route: route[1],reverse=True)
    answer = 0
    
    while routes:
        s,e = routes.pop()
        answer+=1
        for i,o in routes[:]:
            if e in range(i, o+1):
                routes.remove([i,o])
    return answer
    """
    그리디 풀이 정리
    차량들의 경로를 진출지점 기준으로 정렬한 후
    가장 빠른 진출 지점에 카메라 설치 + 겹치는 경로의 차량 제거 
    를 모든 차량이 나갈 때 까지 반복
    """