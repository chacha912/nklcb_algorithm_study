from sys import stdin
from collections import deque


def solution(N, M, board):
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
        cnt = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] != 0 and (i, j) not in visited:
                    bfs(visited, i, j)
                    cnt += 1

        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    gap = board[i][j][0] - board[i][j][1]
                    board[i][j] = gap if gap > 0 else 0

        return cnt

    ans = 0

    while 1:
        cnt = melt()
        if cnt == 0:
            return 0

        if cnt > 1:
            break
        ans += 1

    return ans


N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
print(solution(N, M, board))
