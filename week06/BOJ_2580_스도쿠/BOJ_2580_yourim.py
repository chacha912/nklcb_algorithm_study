import sys

sudoku = [[0 for _ in range(9)] for _ in range(9)]
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
sq = [set() for _ in range(9)]
empty = []
found = False

def check(i, j, val):
    if val in row[i]:
        return False
    if val in col[j]:
        return False
    if val in sq[(i//3) + (j//3)*3]:
        return False
    return True

def dfs(lev):
    global found

    if lev == M:
        found = True
        for i in range(9):
            print(' '.join(sudoku[i]))
        return

    i, j = empty[lev]

    for val in range(1, 10):
        if found:
            continue

        if not check(i, j, val):
            continue

        sudoku[i][j] = str(val)
        row[i].add(val)
        col[j].add(val)
        sq[(i//3) + (j//3)*3].add(val)
        
        dfs(lev + 1)

        row[i].remove(val)
        col[j].remove(val)
        sq[(i//3) + (j//3)*3].remove(val)


for i in range(9):
    line = sys.stdin.readline().split()
    for j, val in enumerate(line):
        sudoku[i][j] = val
        val = int(val)
        row[i].add(val)
        col[j].add(val)
        sq[(i//3) + (j//3)*3].add(val)
        if val == 0:
            empty.append([i,j])

M = len(empty)
dfs(0)