import sys

sudoku = [[0 for _ in range(9)] for _ in range(9)]
row = [[0 for _ in range(10)] for _ in range(9)]
col = [[0 for _ in range(10)] for _ in range(9)]
sq = [[0 for _ in range(10)] for _ in range(9)]
empty = []
found = False

def check(i, j, val):
    if row[i][val] == 1 or col[j][val] == 1 or sq[(i//3) + (j//3)*3][val] == 1:
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
        row[i][val] = 1
        col[j][val] = 1
        sq[(i//3) + (j//3)*3][val] = 1
        
        dfs(lev + 1)

        row[i][val] = 0
        col[j][val] = 0
        sq[(i//3) + (j//3)*3][val] = 0


for i in range(9):
    line = sys.stdin.readline().split()
    for j, val in enumerate(line):
        sudoku[i][j] = val
        val = int(val)
        if val == 0:
            empty.append([i,j])
            continue
        row[i][val] = 1
        col[j][val] = 1
        sq[(i//3) + (j//3)*3][val] = 1

M = len(empty)
dfs(0)
