import copy
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 1
for elem in arr:
    if result < elem:
        break
    result += elem
print(result)
