N = int(input()) # 과목 수
courses = [] 
for _ in range(N): 
    tmp = list(map(int, input().split())) 
    courses.append(set(tmp[1:])) 

M = int(input()) # 학생 수
students = [] 
for _ in range(M): 
    tmp = list(map(int, input().split())) 
    students.append(set(tmp[1:])) 

for student in students: 
    count = 0 
    for course in courses: 
        if course.intersection(student) == course: # 학생의 빈 교시에 수업시간이 포함된다면 추가 
            count += 1 
    print(count)    
