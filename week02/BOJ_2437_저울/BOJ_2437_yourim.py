from sys import stdin

def solution(weight):
    weight.sort()
    sum = 0
    for w in weight:
        if w >= sum + 2:
            return sum + 1        
        else:
            sum += w
    return sum + 1

n = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))
print(solution(weight))