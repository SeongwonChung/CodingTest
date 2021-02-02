from collections import deque

n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

rotate = deque([])
l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    rotate.append((x, c))

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check_rotate(rotate, time, direction):
    if len(rotate) == 0:
        return direction
    change = 0
    time_to_rotate, move = rotate[0]
    if time_to_rotate == time:
        rotate.popleft()
        if move == "D":
            change = 1
        else:
            change = -1
    if direction + change < 0:
        return (direction + change) + 4
    else:
        return (direction + change) % 4


time = 0
snake = deque([(1, 1)])
direction = 0
while True:
    time += 1

    head = snake[-1]
    move = moves[direction]
    togo = (head[0] + move[0], head[1] + move[1])

    if togo[0] < 1 or togo[0] > n or togo[1] < 1 or togo[1] > n:
        break

    if togo in snake:
        break

    snake.append(togo)

    if board[togo[0]][togo[1]] == 1:
        board[togo[0]][togo[1]] = 0
    else:
        snake.popleft()

    direction = check_rotate(rotate, time, direction)
print(time)
