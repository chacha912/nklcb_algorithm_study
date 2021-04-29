def solution(info, query):
    answer = []

    scores = []
    cpp = set()
    java = set()
    python = set()
    backend = set()
    frontend = set()
    junior = set()
    senior = set()
    chicken = set()
    pizza = set()

    for idx, str in enumerate(info):
        lang, type, career, food, score = str.split()
        scores.append(int(score))

        cpp.add(idx) if lang == 'cpp' else java.add(idx) if lang == 'java' else python.add(idx)
        backend.add(idx) if type == 'backend' else frontend.add(idx)
        junior.add(idx) if career == 'junior' else senior.add(idx)
        chicken.add(idx) if food == 'chicken' else pizza.add(idx)

    for str in query:
        lang, _, type, _, career, _, food, score = str.split()
    
        if lang == '-':
            cond = cpp | java | python
        elif lang == 'cpp':
            cond = cpp
        elif lang == 'java':
            cond = java
        else:
            cond = python
        
        if type == '-':
            cond2 = backend | frontend
        elif type == 'backend':
            cond2 = backend
        else:
            cond2 = frontend

        if career == '-':
            cond3 = junior | senior
        elif career == 'junior':
            cond3 = junior
        else:
            cond3 = senior

        if food == '-':
            cond4 = chicken | pizza
        elif food == 'chicken':
            cond4 = chicken
        else:
            cond4 = pizza

        cond_all = cond & cond2 & cond3 & cond4

        cnt = 0
        for idx in cond_all:
            if scores[idx] >= int(score):
                cnt += 1

        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))