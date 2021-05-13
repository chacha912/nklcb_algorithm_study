from collections import deque

N, M, fuel = map(int, input().split())

board = [] #지도 
customers = {}  #손님정보

dnX = [0, 0, -1, 1]
dnY = [-1, 1, 0, 0]


for _ in range(N):
    board.append(list(map(int, input().split())))

startX, startY = map(int, input().split())

startX -= 1
startY -= 1

for _ in range(M):
    a, b, c, d = map(int, input().split())
    customers[(a-1, b-1)] = (c-1, d-1)


# [x, y, 연료]
def pick_up(x, y):
    que = deque()
    que.append([x, y, 0])

    goalX = 987654321  #다음 승객 위치X
    goalY = 987654321  #다음 승객 위치 Y
    goalFuel = 987654321  #가는데 걸리는 연료

    check = [[False] * N for _ in range(N)]
    check[x][y] = True
    while que:
        [nowX, nowY, count] = que.popleft()
        if count > goalFuel:
            continue
        
        if (nowX, nowY) in customers:
            if count == goalFuel:
                if goalX == nowX:
                    if goalY > nowY:
                        goalX = nowX
                        goalY = nowY
                        goalFuel = count
                        continue
                elif goalX > nowX:
                    goalX = nowX
                    goalY = nowY
                    goalFuel = count
                    continue
            elif count < goalFuel:
                goalX = nowX
                goalY = nowY
                goalFuel = count
                continue
        for i in range(4):
            nextX = nowX + dnX[i]
            nextY = nowY + dnY[i]
            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                continue
            if board[nextX][nextY] ==0 and check[nextX][nextY] == False:
                que.append([nextX, nextY, count+1])
                check[nextX][nextY] = True
    return [goalX, goalY, goalFuel]

def go(startX, startY, goalX, goalY):
    que = deque()
    que.append([startX, startY, 0])
    check = [[False] * N for _ in range(N)]
    check[startX][startY] = True
    while que:
        [nowX, nowY, count] = que.popleft()
        if nowX == goalX and nowY == goalY:
            return count
        for i in range(4):
            nextX = nowX + dnX[i]
            nextY = nowY + dnY[i]
            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= N:
                continue
            if board[nextX][nextY] == 0 and check[nextX][nextY] == False:
                que.append([nextX, nextY, count+1])
                check[nextX][nextY] = True
    
    return 987654321



while True:
    if len(customers) == 0:
        print(fuel)
        break
    
    [customerX, customerY, minusFuel] = pick_up(startX, startY)
    fuel -= minusFuel
    if fuel <= 0 :
        print(-1)
        break
    
    (goalX, goalY) = customers[(customerX, customerY)]
    minus_fuel = go(customerX, customerY, goalX, goalY)
    if fuel - minus_fuel < 0 :
        print(-1)
        break
    fuel += minus_fuel
    startX = goalX
    startY = goalY
    del customers[(customerX, customerY)]

    
    