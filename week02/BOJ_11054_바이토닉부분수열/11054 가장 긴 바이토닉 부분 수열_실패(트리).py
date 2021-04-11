
class Node:
    def __init__(self, value):
        self.value = value
        self.high = []
        self.low = []
        self.max_length = 0

class Tree:
    def __init__(self):
        self.head = None

    def add(self, value):

        def recursive(node, count):
            if node is None:
                self.head = Node(value)
                return
            curr = node
            # if not curr.high and not curr.low:
            #     return
            self.head.max_length = max(self.head.max_length, count)
            if curr.value < value:
                curr.high.append(Node(value))
            elif curr.value > value:
                curr.low.append(Node(value))

            for high_node in curr.high:
                count += 1
                recursive(high_node, count)

            for low_node in curr.low:
                count += 1
                recursive(low_node, count)
        recursive(self.head, 0)

n = int(input())
arr = list(map(int, input().split(" ")))
tree = Tree()
for i in arr:
    tree.add(i)
print(tree.head.max_length // 2)

