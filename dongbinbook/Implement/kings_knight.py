loc = list(input())
loc[0] = ord(loc[0]) - 96
loc[1] = int(loc[1])
print(loc)

moves = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)] #list 로 좌표평면에서 이동방향 기록.--> 자주 쓰이는 형태.
cnt = 0
for move in moves:
    print(move)
    col = loc[0]
    row = loc[1]
    col += move[0]
    row += move[1]
    if col in range(1, 9) and row in range(1,9):
        cnt +=1
print(cnt)
