import sys
from collections import deque
from itertools import permutations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end):
    targetX, targetY = end
    visited = [[0 for _ in range(W)] for _ in range(H)]

    q = deque()
    q.append((start, 0))

    while q:
        (x, y), depth = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if room[nx][ny] == "x":
                continue
            if visited[nx][ny] == 1:
                continue
            if nx == targetX and ny == targetY:
                return depth + 1
            visited[nx][ny] = 1
            q.append(((nx,ny), depth+1))    

    return -1

while True:
    W, H = map(int, sys.stdin.readline().split())
    
    if W == 0 and H == 0:
        break

    room = [list(input()) for _ in range(H)]
    dirties = []

    for i in range(H):
        for j in range(W):
            if room[i][j] == 'o':
                robot = (i,j)
            if room[i][j] == '*':
                dirties.append((i,j))
    
    numVertex = len(dirties) + 1
    adjArr = [[0 for _ in range(numVertex)] for _ in range(numVertex)]
    flag = False

    for i in range(len(dirties)):
        for j in range(i+1, len(dirties) + 1):
            if i == 0:
                dist = bfs(robot, dirties[j-1])
            else:
                dist = bfs(dirties[i-1], dirties[j-1])
            
            if dist == -1:
                flag = True
                break 

            adjArr[i][j] = dist
            adjArr[j][i] = dist

    if flag:
        print(-1)
        break

    comb = list(permutations([i+1 for i in range(len(dirties))], len(dirties)))

    answer = float('inf')
    for i in range(len(comb)):
        path = comb[i]
        sum = 0
        start = 0
        for j in range(len(path)):
            sum += adjArr[start][path[j]]
            start = path[j]
        answer = min(answer, sum)
    print(answer)

    