import sys

courses = int(sys.stdin.readline())
mask_c = [0]*courses

for i in range(0, courses):
	temp = list(map(int, sys.stdin.readline().split()))
	res = 0
	len = temp[0]
	for j in range(1, len + 1):
		res |= (1<<temp[j])
	mask_c[i] = res

students = int(sys.stdin.readline())
mask_s = [0]*students

for i in range(0, students):
	temp = list(map(int, sys.stdin.readline().split()))
	res = 0
	len = temp[0]
	for j in range(1, len + 1):
		res |= (1<<temp[j])
	mask_s[i] = res


for i in range(0, students):
	ans = 0
	for j in range(0, courses):
		if (mask_s[i] & mask_c[j]) == mask_c[j]:
			ans += 1
	print(ans)