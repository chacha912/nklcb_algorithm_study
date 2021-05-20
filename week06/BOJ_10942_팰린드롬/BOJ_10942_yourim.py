import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

def chkPalindrome(arr):
    s = 0 
    e = len(arr) - 1
    while s < e:
        if arr[s] != arr[e]:
            return False
        s += 1
        e -= 1
    return True    

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    chk = chkPalindrome(arr[start-1:end])
    if chk is True:
        print(1)
    else:
        print(0)
