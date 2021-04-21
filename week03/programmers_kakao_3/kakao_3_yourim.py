import collections
import bisect
from itertools import product

def solution(info, query):
    answer = []
    
    info_dict = collections.defaultdict(list)

    for str in info:
        lang, type, career, food, score = str.split()
        items = [[lang, '-'],[type, '-'],[career, '-'],[food, '-']]
        conds = list(map(lambda x: "".join(x), product(*items)))
        
        for cond in conds:
            info_dict[cond].append(int(score))
            # bisect.insort(info_dict[cond], int(score)) 

    for key in info_dict:
        info_dict[key].sort()

    for str in query:
        lang, _, type, _, career, _,  food, score = str.split()
        cond = lang + type + career + food 
        scores = info_dict[cond]
        length = len(scores)
        if length == 0:
            answer.append(0)
            continue
        index = bisect.bisect_left(scores, int(score))
        answer.append(length - index)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))