from queue import Queue
N = int(input())
M = int(input())

arr = []
groups = [0] * N
for _ in range(N):
    arr.append(list(map(int, input().split())))

plans = list(map(int, input().split()))

def bfs(index, count):
    que = Queue()
    que.put(index)
    groups[index] = count
    visited = [False] * N
    visited[index] = True
    while not que.empty():
        now = que.get()
        for (nextIdx, next) in enumerate(arr[now]):
            if next==1 and visited[nextIdx] == False:
                que.put(nextIdx)
                visited[nextIdx] = True
                groups[nextIdx] = count
def check():
    result = groups[plans[0]-1]
    for i in range(1, len(plans)):
        if groups[plans[i]-1] != result:
            print("NO")
            return 0
    print("YES")

count = 0
for index in range(len(groups)):
    if groups[index] == 0 :
        count += 1
        bfs(index, count)

check()

