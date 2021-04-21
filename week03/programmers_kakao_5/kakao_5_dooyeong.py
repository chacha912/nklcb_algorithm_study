def solution(play_time, adv_time, logs):
    def to_sec(time):
        time = list(map(int, time.split(":")))
        res = time[0] * 3600 + time[1] * 60 + time[2]

        return res

    def to_time(sec):
        res = []

        res.append(str(sec // 3600))
        sec %= 3600

        res.append(str(sec // 60))
        sec %= 60

        res.append(str(sec))

        for i in range(3):
            if len(res[i]) < 2:
                res[i] = '0' + res[i]

        return ':'.join(res)

    if play_time == adv_time:
        return '00:00:00'

    pTime = to_sec(play_time)
    adTime = to_sec(adv_time)
    timeline = [0 for _ in range(pTime + 1)]

    for log in logs:
        st, en = list(map(to_sec, log.split('-')))
        timeline[st] += 1
        timeline[en] -= 1

    tmp = timeline[0]
    for i in range(1, pTime+1):
        if timeline[i] > -1:
            timeline[i] += tmp
            tmp = timeline[i]
            continue

        minus = timeline[i]
        timeline[i] = tmp
        tmp += minus

    cnt = 0
    tot = 0
    big = -1

    for i in range(pTime+1):

        tot += timeline[i]

        if cnt == adTime:
            tot -= timeline[i-adTime-1]
        else:
            cnt += 1

        if tot > big:
            big = tot
            ans = i - adTime
        elif tot == big and ans < 0:
            ans = i - adTime

    ans = to_time(ans)

    return ans
