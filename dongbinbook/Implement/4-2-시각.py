"""
총 경우의 수 = 24 * 60 * 60 =86400 으로, 완전탐색으로 해결 가능한 수준이다. 완전 탐색을 통해 가능한 모든 경우의 수를 검사해본다.
완전탐색: 가능한 모든 경우의 수를 검사해보는 방법.
"""

N = int(input())

count = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if "3" in time:
                count+=1
print(count)            