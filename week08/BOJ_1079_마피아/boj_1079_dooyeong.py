from sys import stdin

N = int(stdin.readline())
guilty = list(map(int, stdin.readline().split()))
guiltyChange = [list(map(int, stdin.readline().split())) for _ in range(N)]
maphia = int(stdin.readline())
total = N
survived = [1] * N
ans = [0]


def killGuilty(guilty):
    _maxGuilty = -float('inf')
    _idx = 0

    for i in range(N):
        if not survived[i]:
            continue

        if _maxGuilty < guilty[i]:
            _maxGuilty = guilty[i]
            _idx = i

    survived[_idx] = 0

    return _idx


def killCivil(guilty, i):
    survived[i] = 0
    for j in range(N):
        if j == i:
            continue

        guilty[j] += guiltyChange[i][j]


def dfs(cnt, tmp):
    ans[0] = max(ans[0], tmp)
    if (cnt == 1 and survived[maphia]) or (not survived[maphia]):
        return

    if cnt % 2:
        _killed = killGuilty(guilty)
        dfs(cnt - 1, tmp)
        survived[_killed] = 1
        return

    for i in range(N):
        if not survived[i] or i == maphia:
            continue

        killCivil(guilty, i)
        dfs(cnt - 1, tmp + 1)
        survived[i] = 1
        for j in range(N):
            if j == i:
                continue

            guilty[j] -= guiltyChange[i][j]


dfs(N, 0)
print(ans[0])


'''
7
50 50 50 50 50 50 50
1 4 3 -2 7 6 7
-2 1 4 3 1 3 2
3 -2 1 4 3 3 2
4 3 -2 1 4 1 2
2 2 2 3 2 2 3
1 3 5 6 3 5 3
1 5 3 5 3 2 3
7

2
2 2
1 1
1 1
2

4
500 500 500 500
1 4 3 -2
-2 1 4 3
3 -2 1 4
4 3 -2 1

'''
