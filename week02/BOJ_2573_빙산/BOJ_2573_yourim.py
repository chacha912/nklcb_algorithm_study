from sys import stdin
import collections

row, col = map(int,stdin.readline().split())
iceberg =  [[int(i) for i in stdin.readline().split()] for _ in range(row)]
year = 1
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# 다음 년도 빙산 배열 구하기
def get_newIceberg(iceberg):
    sum = 0
    last = (0,0)
    new_iceberg = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            curr = iceberg[i][j]
            if curr > 0:
                melting = 0
                for dx, dy in dirs:
                    if iceberg[i+dx][j+dy] == 0:
                        melting += 1

                if curr > melting:
                    new_iceberg[i][j] = curr - melting
                    sum += 1
                    last = (i,j)
                else:
                    new_iceberg[i][j] = 0
    return sum, last, new_iceberg

# 빙산덩어리 구하기
def get_icebergSet(start, iceberg):
    iceberg_set = set()
    deq = collections.deque()
    deq.append(start)

    set_cnt = 0
    while deq:
        i, j = deq.popleft()
        if (i,j) in iceberg_set:
            continue
        iceberg_set.add((i,j))
        set_cnt += 1
        for dx, dy in dirs:
            if iceberg[i+dx][j+dy] > 0:
                deq.append((i+dx,j+dy))
    return set_cnt

while year > 0:
    sum, last, iceberg = get_newIceberg(iceberg)
    if last == (0,0):
        year = 0
        break

    len_icebergSet = get_icebergSet(last, iceberg)
    if sum > len_icebergSet:
        break
    
    year += 1

print(year)