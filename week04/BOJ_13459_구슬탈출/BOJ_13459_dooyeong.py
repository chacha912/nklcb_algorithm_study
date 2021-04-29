from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().strip()) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
red, blue, hole = [0, 0], [0, 0], [0, 0]


def tilt(board, direct, oRed, oBlue):
    rr, rc = oRed
    br, bc = oBlue
    blueMet = redMet = goalIn = False
    result = True

    while board[rr + direct[0]][rc + direct[1]] != '#':
        rr += direct[0]
        rc += direct[1]

        if board[rr][rc] == 'B':
            blueMet = True
            break

        if board[rr][rc] == 'O':
            goalIn = True
            break

    while board[br + direct[0]][bc + direct[1]] != '#':
        br += direct[0]
        bc += direct[1]

        if board[br][bc] == 'R':
            redMet = True
            break

        if board[br][bc] == 'O':
            goalIn = True
            result = False
            break

    if goalIn:
        if redMet or blueMet:
            result = False
    else:
        if redMet:
            br, bc = rr - direct[0], rc - direct[1]

        elif blueMet:
            rr, rc = br - direct[0], bc - direct[1]

    return result, rr, rc, br, bc


goal = [False]


def dfs(cnt, red, blue, past):
    if goal[0] or cnt == 10:
        return

    for d in dirs:
        if d == past:
            continue
        res, rr, rc, br, bc = tilt(board, d, red, blue)

        if res:
            if board[rr][rc] == 'O':
                goal[0] = True
                return

            board[red[0]][red[1]] = '.'
            board[blue[0]][blue[1]] = '.'
            board[hole[0]][hole[1]] = 'O'
            board[rr][rc] = 'R'
            board[br][bc] = 'B'
            board[hole[0]][hole[1]] = 'O'

            dfs(cnt+1, [rr, rc], [br, bc], d)

            board[rr][rc] = '.'
            board[br][bc] = '.'
            board[hole[0]][hole[1]] = 'O'
            board[red[0]][red[1]] = 'R'
            board[blue[0]][blue[1]] = 'B'
            board[hole[0]][hole[1]] = 'O'


for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == 'R':
            red = [i, j]

        if board[i][j] == "B":
            blue = [i, j]

        if board[i][j] == "O":
            hole = [i, j]

dfs(0, red, blue, 0)


if goal[0]:
    print(1)
else:
    print(0)
