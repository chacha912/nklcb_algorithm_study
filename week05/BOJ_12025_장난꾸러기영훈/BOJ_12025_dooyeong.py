from sys import stdin

password = stdin.readline().strip()
k = int(stdin.readline())
bit = 1
cnt = 0
ans = ''
i = 0

# 비밀번호를 받아 1,2,6,7 일 경우에만 저장해놓음
for p in password:
    if p == '1' or p == '6' or p == '2' or p == '7':
        bit <<= 1
        cnt += 1

# 만약 구하려는 k 번째가 가능한 순열의 경우의 수를 넘는다면 바로 종료
if k > bit:
    print(-1)
    exit(0)

# bit의 길이를 맞춰주기 위해 좌측에 '0'으로 패딩처리
bit = str(bin(bit - 1 & (k-1))[2:])
bit = '0' * (cnt - len(bit)) + bit


# 해당 비트에 해당하는 경우에 따라서 수를 정해서 ans 에 저장해나감
for p in password:
    if p == '1' or p == '6' or p == '2' or p == '7':
        if bit[i] == '0':
            if p == '6':
                ans += '1'
            elif p == '7':
                ans += '2'
            else:
                ans += p
            i += 1
            continue

        if p == '1':
            ans += '6'
        elif p == '2':
            ans += '7'
        else:
            ans += p
        i += 1
        continue

    ans += p

print(ans)
