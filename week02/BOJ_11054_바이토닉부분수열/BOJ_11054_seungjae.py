N = int(input())

arr = list(map(int, input().split()))

dp_asc = [0] * N
dp_desc = [0] * N


for (i, value) in enumerate(arr):
    max_result = 0
    for (j, j_value) in enumerate(arr[:i]):
        if j_value < value:
            max_result = max(dp_asc[j], max_result)
    dp_asc[i] = max_result + 1
        

for i in range(len(arr)-1, -1, -1):
    value = arr[i]
    max_result = 0
    for j in range(i+1, len(arr)):
        j_value = arr[j]
        if j_value < value:
            max_result = max(dp_desc[j], max_result)
    dp_desc[i] = max_result + 1
# print(dp_asc)
# print(dp_desc)
result = 0
for x in range(N):
    result = max(result, dp_asc[x]+dp_desc[x])

print(result-1)



        