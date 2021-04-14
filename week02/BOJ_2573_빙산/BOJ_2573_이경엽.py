import sys
from _collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip().split(" "))
arr = [list(map(int, input().rstrip().split(" "))) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution():
    year = 0
    while True:
        count = 0
        should_melt = deque([])
        visited = [[False] * N for _ in range(M)]
        for j in range(M):
            for i in range(N):
                dq = deque([])
                if arr[j][i] > 0 and not visited[j][i]:
                    count += 1
                    dq.append([i, j])
                    visited[j][i] = True
                    while dq:
                        x, y = dq.popleft()
                        sea = 0
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < N and 0 <= ny < M:
                                if arr[ny][nx] > 0 and not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    dq.append([nx, ny])
                                if arr[ny][nx] <= 0:
                                    sea += 1
                        should_melt.append([x, y, sea])

                    if count > 1:
                        print(year)
                        return
                    elif count == 0:
                        print(0)
                        return
        if count == 0:
            print(0)
            return
        year += 1
        delete(should_melt)


def delete(should_melt):
    global arr
    for glacier in should_melt:
        arr[glacier[1]][glacier[0]] -= glacier[2]


solution()
