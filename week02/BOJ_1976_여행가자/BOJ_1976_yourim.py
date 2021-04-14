from sys import stdin
import collections

n = int(stdin.readline())
m = int(stdin.readline())
edges = collections.defaultdict(set)
deq = collections.deque()
connect = set()

for i in range(n):
    edge = list(map(int,stdin.readline().split()))
    for j in range(i+1, n):
        if edge[j] == 1:
            edges[i+1].add(j+1)
            edges[j+1].add(i+1)

route = list(map(int,stdin.readline().split()))
deq.append(route[0])

while deq:
    node = deq.popleft()
    connect.add(node)
    for i in edges[node]:
        if i not in connect:
            deq.append(i)

route = set(route)
answer = 'YES'
for i in route:
    if i not in connect:
        answer = 'NO'
        break

print(answer)