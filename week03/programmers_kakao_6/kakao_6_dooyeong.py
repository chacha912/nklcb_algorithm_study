from collections import deque


def solution(board, r, c):
    def get_dist(r1, c1, r2, c2):
        res = 0

        res += r1 - r2 if r1 >= r2 else r2 - r1
        res += c1 - c2 if c1 >= c2 else c2 - c1

        return res

    def ctrl_move(r, c, di):
        while 1:
            r += di[0]
            c += di[1]
            if 0 <= r < 4 and 0 <= c < 4 and not board[r][c]:
                continue

            break

        r = 0 if r < 0 else 3 if r > 3 else r
        c = 0 if c < 0 else 3 if c > 3 else c

        return r, c

    def select_card(board, cur, target):
        if board[cur['row']][cur['col']]:
            return (cur['row'], cur['col'], 0)

        card_distance_dict = dict()
        tmp = [[0 for _ in range(4)] for _ in range(4)]
        visited = set()
        q = deque()
        q.append((cur['row'], cur['col']))

        for i in range(4):
            for j in range(4):
                tmp[i][j] = get_dist(i, j, cur['row'], cur['col'])

        while q:
            r, c = q.popleft()
            for d in dirs:
                nr, nc = ctrl_move(r, c, d)

                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if tmp[nr][nc] > tmp[r][c] + 1:
                        tmp[nr][nc] = tmp[r][c] + 1
                    q.append((nr, nc))

        q.append((cur['row'], cur['col']))
        visited.clear()
        visited.add((cur['row'], cur['col']))

        while q:
            i, j = q.popleft()

            for d in dirs:
                ni, nj = i+d[0], j+d[1]

                if 0 <= ni < 4 and 0 <= nj < 4:
                    tmp[ni][nj] = min(tmp[ni][nj], tmp[i][j] + 1)
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))

        min_val = 2000
        for i in range(4):
            for j in range(4):
                if not board[i][j]:
                    tmp[i][j] = 0
                if tmp[i][j] > 0 and tmp[i][j] < min_val:
                    min_val = tmp[i][j]
        # tmp made after here ##
        if target < 0:
            for i in range(4):
                for j in range(4):
                    if tmp[i][j] == min_val:
                        return (i, j, tmp[i][j])

        for i in range(4):
            for j in range(4):
                if board[i][j] == target:
                    return (i, j, tmp[i][j])

    def enter_card(board, cur):
        cur['enter'] += 1
        board[cur['row']][cur['col']] = 0

    ans = 0
    cur = {'row': r, 'col': c, 'enter': 0}
    cards = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    kind = 0

    # cards locations
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards.add((i, j))

    while cur['enter'] < len(cards):
        card_pair = []
        _i, _j, _c = select_card(board, cur, -1)
        ans += _c
        cur['row'], cur['col'] = _i, _j
        kind = board[_i][_j]
        enter_card(board, cur)
        _i, _j, _c = select_card(board, cur, kind)
        cur['row'], cur['col'] = _i, _j
        ans += _c
        enter_card(board, cur)

    return ans + cur['enter']
