def convert_to_seconds(time):
    time = map(int, time.split(":"))
    result = 0
    for t, sec in zip(time, [3600, 60, 1]):
        result += t * sec
    return result


def seconds_to_time(seconds):
    s = seconds % 60
    seconds //= 60
    m = seconds % 60
    seconds //= 60
    h = seconds
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def solution(play_time, adv_time, logs):
    play_sec = convert_to_seconds(play_time)
    adv_sec = convert_to_seconds(adv_time)

    played = [0 for _ in range(360001)]
    for log in logs:
        log = log.split("-")
        start = convert_to_seconds(log[0])
        played[start] += 1
        played[convert_to_seconds(log[1])] -= 1

    for idx in range(1, play_sec + 1):
        played[idx] += played[idx - 1]
    for idx in range(1, play_sec + 1):
        played[idx] += played[idx - 1]

    max_time = 0
    max_sum_played = played[adv_sec]
    for start_time in range(1, play_sec+1):
        end_time = start_time + adv_sec if start_time + adv_sec < play_sec else play_sec
        sum_played = played[end_time] - played[start_time]
        if max_sum_played < sum_played:
            max_sum_played = sum_played
            max_time = start_time+1

    return seconds_to_time(max_time)


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00",
        "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))
