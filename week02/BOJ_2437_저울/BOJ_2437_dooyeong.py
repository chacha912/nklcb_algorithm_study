from sys import stdin


def solution(N, weights):
    weights.sort()
    total = 0

    for w in weights:
        if total + 1 < w:
            return total + 1

        total += w

    return total + 1


N = int(stdin.readline())
weights = list(map(int, stdin.readline().split()))

print(solution(N, weights))
