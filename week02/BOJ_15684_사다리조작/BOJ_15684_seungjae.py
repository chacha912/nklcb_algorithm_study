from sys import exit

N, M, H = map(int, input().split())

bridge = [[False]*(N) for _ in range(H)]

if M==0:
    print(0)
    exit()

for _ in range(M):
    x, y = map(int, input().split())
    bridge[x-1][y-1] = True 


def check():
    for col in range(N):
        nowY = col
        for row in range(H):
            if bridge[row][nowY]:
                nowY += 1
            elif nowY>0 and bridge[row][nowY-1]:
                nowY -= 1
        
        if nowY == col:
            continue
        else:
            return False
    
    return True

result = 5

def dfs(h, count):
    global result
    if count>3:
        return
    elif h == H:
        return
    for i in range(N-1):
        if bridge[h][i] == False:
            if i>0 and bridge[h][i-1] == False and bridge[h][i+1] == False:
                bridge[h][i] = True
                if check():
                    result = min(result, count+1)
                else:
                    dfs(h+1, count+1)
                bridge[h][i] = False
            elif i==0 and bridge[h][i+1] == False:
                bridge[h][i] = True
                if check():
                    result = min(result, count+1)
                else:
                    dfs(h+1, count+1)
                bridge[h][i] = False
    dfs(h+1, count)

dfs(0, 0)

if result == 5:
    print(-1)
else:
    print(result)
