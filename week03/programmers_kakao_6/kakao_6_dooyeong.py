from itertools import permutations as pmt
from collections import defaultdict, deque
import heapq
import copy


def log(arr):
    for a in arr:
        print(a)


def solution(board, r, c):
    def ctrl_move(board, cr, cc, d):
        while 1:
            cr += d[0]
            cc += d[1]
            if 0 <= cr < 4 and 0 <= cc < 4 and not board[cr][cc]:
                continue
            break

        cr = 0 if cr < 0 else 3 if cr > 3 else cr
        cc = 0 if cc < 0 else 3 if cc > 3 else cc

        return cr, cc

    def card_pop(board, cardDic, target, cur):
        # card1, card2 = cardDic[target]
        distances = [[float('inf') for _ in range(4)] for _ in range(4)]
        h = []

        heapq.heappush(h, (cur[0], cur[1], 0))
        distances[cur[0]][cur[1]] = 0

        # bfs 1
        while h:
            r, c, dist = heapq.heappop(h)

            if dist > distances[r][c]:
                continue

            for d in dirs:
                nr, nc = ctrl_move(board, r, c, d)

                if distances[nr][nc] > dist + 1:
                    distances[nr][nc] = dist + 1
                    heapq.heappush(h, (nr, nc, dist + 1))

        # bfs 2
        for i in range(4):
            for j in range(4):
                for d in dirs:
                    ni, nj = i+d[0], j+d[1]

                    if 0 <= ni < 4 and 0 <= nj < 4:
                        if distances[ni][nj] > distances[i][j] + 1:
                            distances[ni][nj] = distances[i][j] + 1

        # after set distances
        a, b = cardDic[target]
        if distances[a[0]][a[1]] > distances[b[0]][b[1]]:
            a, b = b, a

        if board[a[0]][a[1]] == 0:
            a = b

        board[a[0]][a[1]] = 0
        cur[0], cur[1] = a[0], a[1]

        return distances[a[0]][a[1]] + 1

    ans = float('inf')
    cardDic = defaultdict(list)
    leftCardCnt = 0
    cur = [r, c]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cardDic[board[i][j]].append((i, j))
                leftCardCnt += 1

    leftCardCnt //= 2

    for p in pmt(cardDic.keys(), leftCardCnt):
        # p = (1,3,2) -> (1, 2, 3) ...
        tmpCnt = 0
        cur = [r, c]
        tmpBoard = copy.deepcopy(board)
        for kind in p:
            for _ in range(2):
                tmpCnt += card_pop(tmpBoard, cardDic, kind, cur)
        if tmpCnt < ans:
            ans = tmpCnt

    return ans
