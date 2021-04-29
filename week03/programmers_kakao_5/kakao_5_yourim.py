def solution(play_time, adv_time, logs):
    def to_second(str):
        hh, mm, ss = str.split(':')
        second = 3600*int(hh) + 60*int(mm) + int(ss)
        return second

    def to_time(second):
        hh, mm = divmod(second, 3600)
        mm, ss = divmod(mm, 60)
        time = '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)
        return time

    play_second = to_second(play_time)
    adv_second = to_second(adv_time)
    sum_arr = [0 for _ in range(play_second+1)]

    for view_time in logs:
        start, end = view_time.split('-')
        start = to_second(start)
        end = to_second(end)
        sum_arr[start] += 1
        sum_arr[end] -= 1
    
    for i in range(1, play_second+1):
        sum_arr[i] += sum_arr[i-1]

    start_second = 0
    max_time = play_second - adv_second
    view_sum = sum(sum_arr[:adv_second])
    max_sum = view_sum

    for idx in range(0, max_time):
        view_sum = view_sum - sum_arr[idx] + sum_arr[adv_second+idx]
        if view_sum > max_sum:
            max_sum = view_sum
            start_second = idx+1

    return to_time(start_second)

play_time = "02:03:55"
adv_time = "00:14:15"	
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))