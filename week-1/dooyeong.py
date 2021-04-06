from sys import stdin


def solve(cnt):
    if cnt >= m:
        print(' '.join(ans))
        return

    for i in range(1, n+1):
        if i in used:
            continue

        ans.append(str(i))
        used.add(i)
        solve(cnt+1)
        ans.pop()
        used.remove(i)


ans = []
used = set()
n, m = map(int, stdin.readline().split())
solve(0)
