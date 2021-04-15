from sys import stdin
import collections

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
                if iceberg[i-1][j] == 0:
                    melting += 1
                if iceberg[i+1][j] == 0:
                    melting += 1
                if iceberg[i][j-1] == 0:
                    melting += 1
                if iceberg[i][j+1] == 0:
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

    while deq:
        i, j = deq.popleft()
        if (i,j) in iceberg_set:
            continue
        iceberg_set.add((i,j))
        if iceberg[i-1][j] > 0:
            deq.append((i-1, j))
        if iceberg[i+1][j] > 0:
            deq.append((i+1, j))
        if iceberg[i][j-1] > 0:
            deq.append((i, j-1))
        if iceberg[i][j+1] > 0:
            deq.append((i, j+1))
    return len(iceberg_set)


row, col = map(int,stdin.readline().split())
iceberg =  [[int(i) for i in stdin.readline().split()] for _ in range(row)]
year = 1

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