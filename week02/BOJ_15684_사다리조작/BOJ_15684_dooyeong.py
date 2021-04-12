from sys import stdin
from itertools import combinations


def solution(N, M, H, ladderInfo):
    def go_down_ladder():
        for i in range(1, N+1):
            pos = [1, i]
            while pos[0] < H+1:
                if board[pos[0]][pos[1]] == 1:
                    pos[1] += 1
                elif board[pos[0]][pos[1]] == -1:
                    pos[1] -= 1
                pos[0] += 1
            if pos[1] != i:
                return False

        return True

    def make_ladder(lev, cnt, si, sj):
        if possible[0]:
            return

        if lev >= cnt:
            possible[0] = go_down_ladder()
            return

        if sj >= N:
            si += 1
            sj = 1

        for i in range(si, H+1):
            for j in range(1, N):
                if board[i][j] == 0 and board[i][j+1] == 0:
                    board[i][j], board[i][j+1] = 1, -1
                    make_ladder(lev+1, cnt, i, j+2)
                    board[i][j], board[i][j+1] = 0, 0

    board = [[0 for _ in range(N+1)] for _ in range(H+2)]
    ladderPos = []
    possible = [False]

    for i in range(N+1):
        board[H+1][i] = i

    for r, c in ladderInfo:
        board[r][c], board[r][c+1] = 1, -1

    for i in range(4):
        possible[0] = False
        make_ladder(0, i, 0, 0)
        if possible[0]:
            return i

    return -1


N, M, H = map(int, stdin.readline().split())
ladderInfo = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

print(solution(N, M, H, ladderInfo))
