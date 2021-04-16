N = int(input())
arr = list(map(int, input().split(" ")))

def solution():
    max_dp = [1] * N
    answer = -1
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                max_dp[i] = max(max_dp[i], max_dp[j] + 1)
    min_dp = [1] * N
    arr_re = arr[::-1]
    for k in range(N):
        for m in range(k):
            if arr_re[k] > arr_re[m]:
                min_dp[k] = max(min_dp[k], min_dp[m] + 1)

    for i in range(N):
        answer = max(answer, max_dp[i] + min_dp[::-1][i] - 1)
    print(answer)
solution()

############################################################
# 아래는 실패
############################################################
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

