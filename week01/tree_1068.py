n = int(input())
arr = list(map(int, input().split(" ")))
delete = int(input())


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.child = []


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def find(self, value):
        node = None

        def recur(curr):
            nonlocal node
            if curr.value == value:
                node = curr
                return

            for i in curr.child:
                recur(i)


        recur(self.root)
        return node

    def set(self, value, parent):
        leafs = []

        while True:
            if not self.nodes:
                break
            if not leafs:
                for node in self.nodes:
                    if node[1] == -1:
                        leafs.append(node)
            else:
                for node in self.nodes[:]:
                    for leaf in leafs[:]:
                        if leaf[0] == node[1]:
                            leafs.remove(leaf)
                            leafs.append(node)


        if self.root is None:
            self.root = Node(value, parent)
        else:
            parent_node = self.find(parent)
            new_node = Node(value, parent)
            parent_node.child.append(new_node)

    def delete(self, value):
        node = self.find(value)
        if node.parent == -1:
            self.root = None
        else:
            parent = self.find(node.parent)
            parent.child.remove(node)

    def count_leaf(self):
        count = 0

        def recur(node):
            nonlocal count
            if not node.child:
                count += 1
                return
            for i in node.child:
                recur(i)

        if self.root is None:
            return 0
        recur(self.root)
        return count


def tree_1068(n, setting, delete):
    tree = Tree()


    for index, parent in enumerate(setting):
        tree.nodes.append([index, parent])
    tree.delete(delete)
    print(tree.count_leaf())


tree_1068(n, arr, delete)
# Test 완료