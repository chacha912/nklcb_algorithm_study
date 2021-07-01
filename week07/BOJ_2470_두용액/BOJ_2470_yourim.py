import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0
end = N - 1
min = float("inf")    
ansL, ansR = 0, 0

while start < end:
    
    sum = arr[end] + arr[start]

    if abs(sum) < min:
        min = abs(sum)
        ansL, ansR= start, end

        if sum == 0:
            break

    if sum < 0:
        start += 1
    else:
        end -= 1

print(arr[ansL], arr[ansR])