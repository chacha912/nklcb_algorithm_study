import copy

answer = 0


def move_right(N, board):
    # 오른쪽부터 반대쪽으로
    for i in range(N):
        p = N - 1
        x = 0
        for q in range(N - 1, -1, -1):
            if board[i][q] == 0:
                continue  # 값이 0 이라면 건너뛴다
            if x == 0:  # 기존에 담고있던 값이 없다면
                x = board[i][q]  # x에 값을 할당
            else:  # 기존에 담고있는 값이 있다면
                if x == board[i][q]:  # 동일한 값이라면
                    board[i][p] = 2 * x  # i번째 자리에 2x를 업데이트
                    p = p - 1  # p 한칸 이동
                    x = 0  # x 초기화
                else:  # 다른 값이라면
                    board[i][p] = x  # i번째 자리에 x값 입력
                    p = p - 1  # p 한칸 이동
                    x = board[i][q]  # 새로운 x값
            board[i][q] = 0  # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0:
            board[i][p] = x  # 마지막으로 고려해줘야 할것
    return board


def move_left(N, board):
    # 왼쪽에서 부터
    for i in range(N):
        p = 0
        x = 0
        for q in range(N):
            if board[i][q] == 0:
                continue  # 값이 0 이라면 건너뛴다
            if x == 0:  # 기존에 담고있던 값이 없다면
                x = board[i][q]  # x에 값을 할당
            else:  # 기존에 담고있는 값이 있다면
                if x == board[i][q]:  # 동일한 값이라면
                    board[i][p] = 2 * x  # i번째 자리에 2x를 업데이트
                    p = p + 1  # p 한칸 이동
                    x = 0  # x 초기화
                else:  # 다른 값이라면
                    board[i][p] = x  # i번째 자리에 x값 입력
                    p = p + 1  # p 한칸 이동
                    x = board[i][q]  # 새로운 x값
            board[i][q] = 0  # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0:
            board[i][p] = x  # 마지막으로 고려해줘야 할것
    return board


def move_up(N, board):
    for i in range(N):
        p = 0
        x = 0
        for q in range(N):
            if board[q][i] == 0:
                continue  # 값이 0 이라면 건너뛴다
            if x == 0:  # 기존에 담고있던 값이 없다면
                x = board[q][i]  # x에 값을 할당
            else:  # 기존에 담고있는 값이 있다면
                if x == board[q][i]:  # 동일한 값이라면
                    board[p][i] = 2 * x  # i번째 자리에 2x를 업데이트
                    p = p + 1  # p 한칸 이동
                    x = 0  # x 초기화
                else:  # 다른 값이라면
                    board[p][i] = x  # i번째 자리에 x값 입력
                    p = p + 1  # p 한칸 이동
                    x = board[q][i]  # 새로운 x값
            board[q][i] = 0  # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0:
            board[p][i] = x  # 마지막으로 고려해줘야 할것
    return board


def move_down(N, board):
    for i in range(N):
        p = N - 1
        x = 0
        for q in range(N - 1, -1, -1):
            if board[q][i] == 0:
                continue  # 값이 0 이라면 건너뛴다
            if x == 0:  # 기존에 담고있던 값이 없다면
                x = board[q][i]  # x에 값을 할당
            else:  # 기존에 담고있는 값이 있다면
                if x == board[q][i]:  # 동일한 값이라면
                    board[p][i] = 2 * x  # i번째 자리에 2x를 업데이트
                    p = p - 1  # p 한칸 이동
                    x = 0  # x 초기화
                else:  # 다른 값이라면
                    board[p][i] = x  # i번째 자리에 x값 입력
                    p = p - 1  # p 한칸 이동
                    x = board[q][i]  # 새로운 x값
            board[q][i] = 0  # 나중에 번거로운 작업을 없애주기 위한것
        if x != 0:
            board[p][i] = x  # 마지막으로 고려해줘야 할것
    return board


def check(N, board):
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > ans:
                ans = board[i][j]
    return ans


def dfs(N, board, count):
    global answer
    if count >= 5:
        answer = max(answer, check(N, board))
        return
    else:
        dfs(N, move_up(N, copy.deepcopy(board)), count + 1)
        dfs(N, move_down(N, copy.deepcopy(board)), count + 1)
        dfs(N, move_left(N, copy.deepcopy(board)), count + 1)
        dfs(N, move_right(N, copy.deepcopy(board)), count + 1)


def solution():
    N = int(input())
    board = [list(map(int, input().split(" "))) for _ in range(N)]
    dfs(N, board, 0)
    print(answer)


solution()
