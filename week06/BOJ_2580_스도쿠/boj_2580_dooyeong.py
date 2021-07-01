from sys import stdin


def getEmpty(empty):
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                empty.append((i, j))

    return empty


def check(board, r, c, cur):
    lc = (c // 3) * 3
    lr = (r // 3) * 3

    for i in range(9):
        if board[i][c] == cur and i != r:
            return False

    for i in range(9):
        if board[r][i] == cur and i != c:
            return False

    for i in range(lr, lr + 3):
        for j in range(lc, lc + 3):
            if board[i][j] == cur and (i, j) != (r, c):
                return False

    return True


def dfs(lev, empty):
    if found[0]:
        return

    if lev == M:
        found[0] = True
        for b in board:
            print(' '.join(map(str, b)))

        return

    r, c = empty[lev]

    for i in range(1, 10):
        if not check(board, r, c, i):
            continue

        board[r][c] = i
        dfs(lev + 1, empty)
        board[r][c] = 0


N = 9
board = [list(map(int, stdin.readline().split())) for _ in range(9)]
empty = getEmpty([])
M = len(empty)
found = [False]
dfs(0, empty)
