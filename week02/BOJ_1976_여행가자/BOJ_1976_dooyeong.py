from sys import stdin


def solution(N, M, cityInfo, plan):
    def union(a, b):
        x, y = find(a), find(b)

        if x == y:
            return

        parent[x] = y

    def find(a):
        if parent[a] == a:
            return a

        parent[a] = find(parent[a])
        return parent[a]

    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if cityInfo[i][j]:
                union(i, j)

    prev = find(plan[0]-1)
    for i in range(1, len(plan)):
        if find(plan[i] - 1) != prev:
            return "NO"

    return "YES"


N = int(stdin.readline())
M = int(stdin.readline())
cityInfo = [list(map(int, stdin.readline().split())) for _ in range(N)]
plan = list(map(int, stdin.readline().split()))
print(solution(N, M, cityInfo, plan))
