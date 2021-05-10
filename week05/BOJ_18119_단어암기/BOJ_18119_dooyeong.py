from sys import stdin

N, M = map(int, stdin.readline().split())
wordList = [0] * N

for i in range(N):
    word = stdin.readline().strip()
    tmp = 0
    a = ord('a')

    for w in word:
        tmp |= 1 << ord(w) - a

    wordList[i] = tmp

status = (1 << 27) - 1
aeiou = set('aeiou')

for _ in range(M):
    cmd, ch = stdin.readline().split()

    if ch in aeiou:
        continue

    if cmd == '1':
        status &= ~(1 << (ord(ch) - ord('a')))
    else:
        status |= (1 << (ord(ch) - ord('a')))

    cnt = 0

    for i in range(N):
        if wordList[i] & status == wordList[i]:
            cnt += 1

    print(cnt)
