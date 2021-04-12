from sys import stdin


def solution(N, nums):
    ans = -1
    tmp = [0 for _ in range(N)]
    up = [1 for _ in range(N)]
    down = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                up[i] = max(up[i], up[j] + 1)
        tmp[i] = up[i]

    for i in range(N-1, -1, -1):
        for j in range(i, N):
            if nums[i] > nums[j]:
                down[i] = max(down[i], down[j] + 1)
        ans = max(ans, tmp[i] + down[i])

    return ans - 1


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(solution(N, nums))
