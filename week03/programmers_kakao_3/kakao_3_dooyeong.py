from itertools import combinations as cbi


def solution(info, query):
    def bin_search(li, target):
        st, en = 0, len(li)-1

        while st <= en:
            m = (st+en)//2

            if li[m] >= target:
                en = m - 1
            else:
                st = m + 1

        return en + 1

    ans = []
    infoDic = dict()

    for i in info:
        tmpI = i.split(' ')
        tmpScore = tmpI.pop()

        for cnt in range(5):
            for c in cbi(tmpI, cnt):
                if c not in infoDic:
                    infoDic[c] = []
                infoDic[c].append(int(tmpScore))

    for key in infoDic:
        infoDic[key].sort()

    for q in query:
        tmpQ = [word for word in q.split(' ') if word != 'and' and word != '-']
        tmpScore = int(tmpQ.pop())
        tmpQ = tuple(tmpQ)

        if tmpQ not in infoDic:
            ans.append(0)
            continue

        idx = bin_search(infoDic[tmpQ], tmpScore)
        ans.append(len(infoDic[tmpQ]) - idx)

    return ans
