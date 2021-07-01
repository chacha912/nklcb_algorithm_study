
def solution():
    N, M = map(int, input().split(" "))
    board = [list(map(int, input().split(" "))) for _ in range(N)]
    answer = []

    def tetromino(x, y):
        answer = 0
        if x + 3 < M:  # 가로 네 줄
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y][x + 3])
        if  y + 3 < N:  # 세로y 네 줄
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 3][x])
        if x + 1 < M and y + 1 < N:  # 네모난 모양
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y + 1][x] + board[y + 1][x + 1])

        if y + 1 < N and y + 2 < N and x + 1 < M:  # 세번째 노대칭
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 2][x + 1])
        if x + 1 < M and x + 2 < M and y - 1 >= 0:  # 세번째 오른쪽 회전
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y - 1][x+2])
        if y - 1 >= 0 and y - 2 >= 0 and x - 1 >= 0:  # 세번째 180도 회전
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 2][x] + board[y - 2][x - 1])
        if x - 1 >= 0 and x - 2 >= 0 and y + 1 < N:  # 세번째 270도 회전
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y][x - 2] + board[y + 1][x - 2])
        if y + 1 < N and y + 2 < N and x - 1 >= 0:  # 세번째 대칭
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 2][x - 1])
        if x - 1 >= 0 and x - 2 >= 0 and y - 1 >= 0:  # 세번째 대칭 왼쪽 회전
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y][x - 2] + board[y - 1][x - 2])
        if y - 1 >= 0 and y - 2 >= 0 and x + 1 < M:  # 세번째 대칭 180도 회전
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 2][x] + board[y - 2][x + 1])
        if x + 1 < M and x + 2 < M and y + 1 < N:  # 세번째 대칭 270도 회전
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 2])

        if x + 1 < M and y + 2 < N:  # 네번쨰 꺼 노대칭
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x + 1])
        if x - 2 >= 0 and y + 1 < N:
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y + 1][x - 1] + board[y + 1][x - 2])
        if x - 1 >= 0 and y - 2 >= 0:
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 1][x - 1] + board[y - 2][x - 1])
        if x + 2 < M and y - 1 >= 0:
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y - 1][x + 1] + board[y - 1][x + 2])
        if x - 1 >= 0 and y + 2 < N:  # 네번째 꺼 대칭
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 1][x - 1] + board[y + 2][x - 1])
        if x - 2 >= 0 and y - 1 >= 0:
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y - 1][x - 1] + board[y - 1][x - 2])
        if x + 1 < M and y - 2 >= 0:
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 1][x + 1] + board[y - 2][x + 1])
        if x + 2 < M and y - 1 >= 0:
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y - 1][x + 1] + board[y - 1][x + 2])
        if x + 2 < M and y + 1 < N:  # 다섯번쨰 노대칭
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y + 1][x + 1] + board[y][x + 2])
        if x - 1 >= 0 and y + 2 < N:
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 1][x - 1] + board[y + 2][x])
        if x - 2 >= 0 and y - 1 >= 0:
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y][x - 2] + board[y - 1][x - 1])
        if y - 2 >= 0 and x + 1 < M:
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 1][x + 1] + board[y - 2][x])
        if x + 2 < M and y - 1 >= 0:  # 다섯번쨰 대칭
            answer = max(answer, board[y][x] + board[y][x + 1] + board[y - 1][x + 1] + board[y][x + 2])
        if y + 2 < N and x + 1 < M:
            answer = max(answer, board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x])
        if x - 2 >= 0 and y + 1 < N:
            answer = max(answer, board[y][x] + board[y][x - 1] + board[y + 1][x - 1] + board[y][x - 2])
        if y - 2 >= 0 and x - 1 >= 0:
            answer = max(answer, board[y][x] + board[y - 1][x] + board[y - 1][x - 1] + board[y - 2][x])
        return answer

    for i in range(M):
        for j in range(N):
            answer.append(tetromino(i, j))

    return max(answer)


print(solution())