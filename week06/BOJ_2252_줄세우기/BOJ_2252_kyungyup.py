from _collections import deque


N, M = map(int, input().split(" "))
adj_list = [[] for _ in range(N+1)]
reference = [0 for i in range(32001)]
dq = deque([])

for _ in range(M):
    a, b = map(int, input().split(" "))
    reference[b] += 1  # 참조 값 추가
    adj_list[a].append(b)

for i in range(1, N + 1):
    if reference[i] == 0:
        dq.append(i)
while dq:
    student = dq.popleft()
    for j in adj_list[student]:
        reference[j] -= 1
        if reference[j] == 0:
            dq.append(j)
    print(student, end=" ")
