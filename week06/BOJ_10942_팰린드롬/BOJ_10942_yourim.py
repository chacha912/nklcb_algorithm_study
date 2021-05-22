import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [dict() for _ in range(N+1)]
# dp = [[-1]*(N+1) for _ in range(N+1)]  

def chkPalindrome(start, end):
    
    if end in dp[start]: 
        return dp[start][end]

    # if dp[start][end] != -1:
    #     return dp[start][end]

    if start == end:
        dp[start][end] = 1
        return 1

    if arr[start] != arr[end]:
        dp[start][end] = 0
        return 0

    if start == end - 1: 
        dp[start][end] = 1
        return 1
    
    dp[start][end] = chkPalindrome(start+1, end-1)

    return dp[start][end] 


for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(chkPalindrome(start-1, end-1))