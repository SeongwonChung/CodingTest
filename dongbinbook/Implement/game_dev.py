N, M = map(int, input().split())
a, b, d = map(int, input().split())
field=[]
for _ in range(N):
    field.append(list(map(int, input().split())))
print(field)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def getNextD(d):
    if d-1 < 0:
        nextD = d-1 + 4
    else:
        nextD = d-1
    return nextD

cnt = 1
stop = 0

while True:
    if stop: break
    check = [0,0,0,0]
    while True:
        d = getNextD(d)
        check[d] = 1
        if field[a+dx[d]][b+dy[d]] == 0:
            a+=dx[d]
            b+=dy[d]
            field[a][b] = 1 #map 에 표시
            cnt+=1
            break
        
        if 0 not in check:
            if field[a-dx[d]][b-dy[d]] == 1:
                stop = 1
            else:
                a-=dx[d]
                b-=dy[d]
                field[a][b] = 1 #map 에 표시
                cnt+=1
            break
print(cnt)

"""
4 4 
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1
"""