from _collections import deque
# asd
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

    val_nodes = sorted(val_nodes, key=lambda x: x.parent)
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
