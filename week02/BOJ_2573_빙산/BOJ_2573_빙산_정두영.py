from sys import stdin
from collections import deque


def solution(N, M, board):
    def check():
        def bfs(visited, i, j):
            q = deque([(i, j)])
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]

                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        visited = set()
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0 and (i, j) not in visited:
                    bfs(visited, i, j)
                    cnt += 1
        return cnt

    def melt():
        def bfs(visited, i, j):
            q = deque([(i, j)])
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                cnt = 0

                for d in dirs:
                    nr, nc = r + d[0], c + d[1]

                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == 0:
                            cnt += 1
                        elif (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                board[r][c] = [board[r][c], cnt]

        visited = set()

        for i in range(N):
            for j in range(M):
                if board[i][j] != 0 and (i, j) not in visited:
                    bfs(visited, i, j)

        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    gap = board[i][j][0] - board[i][j][1]
                    board[i][j] = gap if gap > 0 else 0

    ans = 0

    while 1:
        melt()
        ans += 1

        c = check()

        if c == 0:
            return 0

        if c > 1:
            break

    return ans


N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
print(solution(N, M, board))

'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 2 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 3 3 1 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
1

2

'''
