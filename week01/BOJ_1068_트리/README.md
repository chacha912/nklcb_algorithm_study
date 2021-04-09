## 백준 #1068 트리

- 알고리즘 스터디 문제 풀이입니다.
- [백준 1068번](https://www.acmicpc.net/problem/1068) 에서 풀어볼 수 있습니다.

### 문제설명

- 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다. 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
- 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

### 풀이1. 노드로 트리 구현

```python
from collections import deque

n = int(input())
arr_node = list(map(int, input().split(" ")))
delete = int(input())

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = []

    def find(self, root, value):
        node = None

        def recur(curr):
            nonlocal node
            if curr.value == value:
                node = curr
                return

            for i in curr.child:
                recur(i)

        recur(root)
        return node

def solution():

    val_nodes = []
    for value, node in enumerate(arr_node):
        val_nodes.append(Node(value, node))

    for i in val_nodes:
        for j in val_nodes:
            if i.value == j.parent:
                i.child.append(j)

    val_nodes = sorted(val_nodes, key=lambda x : x.parent)
    for i in val_nodes:
        if i.value == delete:
            if i.parent == -1:
                print(0)
                return

            children = i.find(val_nodes[0], i.parent).child
            if not children:
                break
            else:
                children.remove(i)

    count = 0
    dq = deque([])
    dq.append(val_nodes[0])
    while dq:
        node = dq.popleft()
        if not node.child:
            count += 1
        else:
            for i in node.child:
                dq.append(i)
    print(count)

solution()
```

### 풀이2. dfs

dfs 로 순회하면서 리프노드 개수를 추가한다.  
만약 노드가 제거해야하는 노드일 경우, 부모의 자식 개수를 확인한다.
자식이 한 개일 경우 해당노드를 제거하면 부모가 리프노드가 되므로 리프노드 개수를 추가한다.

```python
from sys import stdin

def dfs(idx):
    if idx not in children:
        ans[0] += 1
        return

    for c in children[idx]:
        if c == delnode:
            if len(children[idx]) < 2:
                ans[0] += 1
            continue
        dfs(c)

n = int(stdin.readline())
info = list(map(int, stdin.readline().split()))
delnode = int(stdin.readline())
children = dict()
root = 0
ans = [0]

for i, par in enumerate(info):
    if par == -1:
        root = i
        continue

    if par in children:
        children[par].append(i)
    else:
        children[par] = [i]

if delnode == root:
    print(0)
else:
    dfs(root)
    print(ans[0])
```

### 풀이3. 배열 안에서 해결

```python
N = int(input())
arr = list(map(int, input().split()))
removed = int(input()) # 삭제된 노드

leafs = []
root = -1
for index in range(N):
    if arr[index] == -1: # 루트 노드 찾기
        root = index
    if index not in arr: # leaf노드 찾기
        leafs.append(index)

parent = arr[removed]

for index in range(N):
    cur = index
    while cur != -1:
        if  cur == removed:
            if index in leafs:
                leafs.remove(index) # 리프노드에서 삭제
            break
        cur = arr[cur]

count = 0 # 삭제한 노드의 부모가 가진 자식의 수
for elem in arr:
    if elem == parent:
        count += 1
if removed == root : # 삭제한 노드가 부모일경우 0
    print(0)
elif count == 1:  # 자식의 수가 1인 경우 leaf 한개 추가
    print(len(leafs)+1)
else:
    print(len(leafs))

```
