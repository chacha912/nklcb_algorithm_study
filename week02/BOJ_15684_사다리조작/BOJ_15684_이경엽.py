n, m, h = map(int, input().split())
bridge = [[False] * n for _ in range(h)] # 사다리를 배열에 기록
for _ in range(m):
    a, b = map(int, input().split())
    bridge[a - 1][b - 1] = True
ans = 4


def check():
    for start in range(n): # 가로
        k = start
        for i in range(h): # 세로 내려옴
            if bridge[i][k]: # 배열에 bridge 있으면 오른쪽 이동
                k += 1
            elif k > 0 and bridge[i][k - 1]:
                k -= 1
        if start != k:
            return False
    return True


def bf(cnt, x, y): # 시작 점
    global ans
    if check():
        ans = min(ans, cnt) #
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x, h): # 내가 사다리를 놓을 곳 y 값
        k = y if i == x else 0
        for j in range(k, n - 1): #
            if not bridge[i][j] and not bridge[i][j + 1]:
                bridge[i][j] = True
                bf(cnt + 1, i, j + 2)
                bridge[i][j] = False

def solution():
    if m == 0:
        print(0)
        return
    bf(0, 0, 0)
    print(ans if ans < 4 else -1)
solution()


