def rotate(matrix):
    row = len(matrix)
    column = len(matrix[0])
    rotated = [[0 for _ in range(row)] for _ in range(column)]
    for i in range(row):
        for j in range(column):
            rotated[j][row - i - 1] = matrix[i][j]
    return rotated


def check(new_lock):
    size = len(new_lock) // 3
    for i in range(size, size * 2):
        for j in range(size, size * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    lock_expanded = [[0 for _ in range(n * 3)] for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            lock_expanded[i + n][j + n] = lock[i][j]

    for x in range(n * 2):
        for y in range(n * 2):
            for d in range(4):
                key = rotate(key)

                for i in range(m):
                    for j in range(m):
                        lock_expanded[i + x][j + y] += key[i][j]
                if check(lock_expanded):
                    return True

                for i in range(m):
                    for j in range(m):
                        lock_expanded[i + x][j + y] -= key[i][j]

    return False
