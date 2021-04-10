from sys import stdin

n = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))
weight.sort()

def solution(weight):
    sum = 0
    for i in weight:
        if i >= sum + 2:
            return sum + 1        
        else:
            sum += i
    return sum + 1

print(solution(weight))