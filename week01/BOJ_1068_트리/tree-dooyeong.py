from sys import stdin


def dfs(idx):
    if idx not in children:
        ans[0] += 1
        return

    for c in children[idx]:
        if c == delnode:
            if len(children[idx]) < 2:
                ans[0] += 1
            continue
        dfs(c)


n = int(stdin.readline())
info = list(map(int, stdin.readline().split()))
delnode = int(stdin.readline())
children = dict()
root = 0
ans = [0]

for i, par in enumerate(info):
    if par == -1:
        root = i
        continue

    if par in children:
        children[par].append(i)
    else:
        children[par] = [i]


if delnode == root:
    print(0)
else:
    dfs(root)
    print(ans[0])
