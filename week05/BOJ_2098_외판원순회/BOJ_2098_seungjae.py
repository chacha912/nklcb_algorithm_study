import sys
INF = sys.maxsize
matrix = []
N = 0
answer = 987654321
dp= [] 

def dfs(current, bitmask):
    if  bitmask==(1<<N)-1:
        if matrix[current][0]==0:
            return INF
        else:
            return matrix[current][0]
    if dp[current][bitmask]!=INF:
        return dp[current][bitmask]
    for i in range(1,N):
        if not bitmask&(1<<i) and matrix[current][i]!=0:
            dp[current][bitmask]=min(dp[current][bitmask],dfs(i,bitmask|(1<<i))+matrix[current][i])
    return dp[current][bitmask]
       

def solution():
    global N
    global matrix
    global dp
    N = int(input())
    dp = [[INF]*(1<<N)for _ in range(N)]
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    print(dfs(0,1)) 

solution()