from sys import stdin
from itertools import product
import copy

row, col = map(int,stdin.readline().split())
company = [[0 for _ in range(col)] for _ in range(row)]
cctv = list()
cctv_item = list()
u = (-1,0)
d = (1,0)
l = (0,-1)
r = (0,1)

cctv1 = [u, d, l, r] 
cctv2 = [[u,d], [l,r]]
cctv3 = [[u,r],[u,l],[d,r],[d,l]]
cctv4 = [[u,r,l],[u,r,d],[d,r,l],[u,d,l]]
cctv5 = [[u,r,l,d]]

for i in range(row):
    for j, value in enumerate(stdin.readline().split()):
        val = int(value)
        company[i][j] = val
        if val == 6 or val == 0:
            continue
        if val == 1:
            cctv_item.append(cctv1)
        if val == 2:
            cctv_item.append(cctv2)
        if val == 3:
            cctv_item.append(cctv3)
        if val == 4:
            cctv_item.append(cctv4)
        if val == 5:
            cctv_item.append(cctv5)
        cctv.append(((i,j),val))  # [좌표], cctv종류

cctv_comb = list(product(*cctv_item))
answer = 64

def check(coord, chkord): 
    x, y = coord
    dx, dy = chkord
    for _ in range(8):
        x2, y2 = x + dx, y + dy
        if x2 < 0 or y2 < 0 or x2 >= row or y2 >= col:
            return
        if company_chk[x2][y2] == 6:
            return 
        if company_chk[x2][y2] == 0:
            company_chk[x2][y2] = 8
        x, y = x2, y2

for comb in cctv_comb: # cctv 조합 
    company_chk = copy.deepcopy(company) 
    for i, chkords in enumerate(comb): # i 번째 cctv 가 체크하는 방향 chkords
        if cctv[i][1] == 1: # cctv1 은 한쪽 방향만 확인
            check(cctv[i][0], chkords)
            continue
        for chkord in chkords:
            check(cctv[i][0], chkord)
    empty_num = 0
    for i in range(row):
        for j in range(col):
            if company_chk[i][j] == 0:
                empty_num += 1
    answer = min(answer, empty_num)
    
print(answer)