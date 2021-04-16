# 유니온 파인드
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parents = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]


def solution():
    for i in range(1, N+1):
        arr = list(map(int, input().split(" ")))
        for j in range(1, N+1):
            if arr[j-1] == 1:
                root_x = find(j)
                root_y = find(i)
                union(root_y, root_x)
    spot = list(map(int, input().split(" ")))
    result = set([find(i) for i in spot])

    if len(result) > 1:
        print("NO")
    else:
        print("YES")

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # path compression
    return parents[x]


def union(a, b):
    if rank[a] < rank[b]:  # union-by-rank
        parents[b] = a
    else:
        parents[a] = b

    if rank[a] == rank[b]:
        rank[a] += 1

solution()