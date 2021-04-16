from queue import Queue
import sys
import copy
input = lambda : sys.stdin.readline().strip()
rows, cols = map(int, input().split())

times = 0
mountains = []
arr = []

dnX = [0, 0, -1, 1]
dnY = [1, -1, 0, 0]


def check():
    count = 0
    check_arr = [[False] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] >0 and not check_arr[i][j]:
                count+=1
                check_arr[i][j] = True
                que = Queue()
                que.put([i, j])
                while not que.empty():
                    [nowX, nowY] = que.get()
                    for i in range(4):
                        nextX = nowX+dnX[i]
                        nextY = nowY+dnY[i]
                        if nextX<0 or nextX>=rows or nextY<0 or nextY>=cols:
                            continue
                        if arr[nextX][nextY] >0 and not check_arr[nextX][nextY]:
                            que.put([nextX, nextY])
                            check_arr[nextX][nextY] = True
    return count

def next_turn():
    global mountains
    new_mountains = []
    check_arr = [[False] * cols for _ in range(rows)]
    for mountain in mountains:
        [nowX, nowY, nowH] = mountain
        check_arr[nowX][nowY] = True
        for i in range(4):
            nextX = nowX+dnX[i]
            nextY = nowY+dnY[i]
            if nextX <0 or nextX>=rows or nextY<0 or nextY>=cols:
                continue
            if arr[nextX][nextY] == 0 and check_arr[nextX][nextY] == False:
                nowH -= 1

        if nowH>0 :
            new_mountains.append([nowX, nowY, nowH])
            arr[nowX][nowY] = nowH
        else:
            arr[nowX][nowY] = 0
    mountains = new_mountains
    
for _ in range(rows):
    arr.append(list(map(int, input().split())))

for i in range(rows):
    for j in range(cols):
        if arr[i][j] != 0 :
            mountains.append([i, j, arr[i][j]])

while True:
    
    if len(mountains) ==0 :
        print(0)
        break
    
    check_num = check() 
    if check_num >1 :
        print(times)
        break
    next_turn()
    times += 1