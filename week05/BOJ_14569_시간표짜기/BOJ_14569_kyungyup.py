def solution():
    N = int(input())
    subject, student, answer = [], [], []
    for _ in range(N):
        subject.append(list(map(int, input().split(" "))))
    M = int(input())

    for _ in range(M):
        temp = list(map(int, input().split(" ")))
        arr = [False for _ in range(51)]
        for i in temp[1:]:
            arr[i] = True
        student.append(arr)
    for stud in student:
        count = 0
        for sub in subject:
            for i in sub[1:]:
                if not stud[i]:
                    break
            else:
                count += 1
        answer.append(count)
    for i in answer:
        print(i)
    return


solution()
