N = int(input())
arr = list(map(int, input().split()))
removed = int(input()) #삭제된 노드


leafs = []
root = -1
for index in range(N):
    if arr[index] == -1: #루트 노드 찾기
        root = index
    if index not in arr: #leaf노드 찾기
        leafs.append(index)

parent = arr[removed]

for index in range(N):
    cur = index
    while cur != -1:
        if  cur == removed:
            if index in leafs:
                leafs.remove(index) #리프노드에서 삭제
            break
        cur = arr[cur]

count = 0 # 삭제한 노드의 부모가 가진 자식의 수
for elem in arr:
    if elem == parent:
        count += 1
if removed == root : #삭제한 노드가 부모일경우 0
    print(0)
elif count == 1:  # 자식의 수가 1인 경우 leaf 한개 추가
    print(len(leafs)+1)
else:
    print(len(leafs))
    
