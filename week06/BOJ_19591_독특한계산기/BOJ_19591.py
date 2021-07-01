import sys
from collections import deque


def parsing(exp):
    operators = []
    numbers = []

    res = ""  # result
    q = deque([])
    opers = set("+-*/")

    for c in exp:
        if c not in opers:
            q.append(c)
            continue

        operators.append(c)
        while q:
            res += q.popleft()
        if res:
            numbers.append(int(res))
        res = ""

    while q:
        res += q.popleft()
    numbers.append(int(res))
    if exp[0] == "-":
        numbers[0] = -1
        del operators[0]

    return (numbers, operators)

exp = sys.stdin.readline()
print(parsing(exp))