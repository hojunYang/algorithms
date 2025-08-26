from itertools import combinations

def solution(relation):
    answer = []
    rows = len(relation)
    cols = len(relation[0])
    
    for i in range(1, cols+1):
        for comb in combinations(range(cols), i):
            valid = set()
            for row in range(rows):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                valid.add(temp)
            if len(valid) == rows:
                answer.append(set(comb))

    minimality = set()
    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if answer[i].issubset(answer[j]):
                minimality.add(frozenset(answer[j]))
    return len(answer) - len(minimality)
"""
GPT 5
from itertools import combinations

def solution(relation):
    rows = len(relation)
    n = len(relation[0])
    candidates = []  # 비트마스크로 보관

    for r in range(1, n + 1):
        for comb in combinations(range(n), r):
            mask = 0
            for c in comb:
                mask |= 1 << c
            print(mask)

            # 최소성 사전 가지치기: 이미 찾은 후보키의 상위집합이면 스킵
            if any((cand & mask) == cand for cand in candidates):
                continue

            # 유일성 검사: 튜플 투영으로 set 비교 (문자열 이어붙이기보다 빠름)
            seen = {tuple(row[c] for c in comb) for row in relation}
            if len(seen) == rows:
                candidates.append(mask)

    return len(candidates)
"""
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))