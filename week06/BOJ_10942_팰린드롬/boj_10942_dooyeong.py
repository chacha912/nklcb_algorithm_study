from sys import stdin


def pal(nums, dp, s, e):
    if (s, e) in dp:
        return dp[(s, e)]

    if s == e:
        return 1

    if nums[s-1] != nums[e-1]:
        return 0

    if e - s == 1:
        return 1

    if s + 1 <= e - 1:
        dp[(s, e)] = pal(nums, dp, s+1, e-1)
        return dp[(s, e)]


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
dp = dict()

for _ in range(M):
    s, e = map(int, stdin.readline().split())
    print(pal(nums, dp, s, e))
