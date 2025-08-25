from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []

    info_dict = defaultdict(list)
    for i in info:
        lang, pos, exp, food, score = i.split()
        info_dict[lang, pos, exp, food].append(int(score))
    info_dict = {k: sorted(v) for k, v in info_dict.items()}

    for q in query:
        q = q.replace(' and ', ' ').split()
        q[0] = ['java', 'python', 'cpp'] if q[0] == '-' else [q[0]]
        q[1] = ['backend', 'frontend'] if q[1] == '-' else [q[1]]
        q[2] = ['junior', 'senior'] if q[2] == '-' else [q[2]]
        q[3] = ['chicken', 'pizza'] if q[3] == '-' else [q[3]]
        
        count = 0
        for lang in q[0]:
            for pos in q[1]:
                for exp in q[2]:
                    for food in q[3]:
                        scores = info_dict.get((lang, pos, exp, food), [])
                        if scores:  # defaultdict는 빈 리스트를 반환하므로 존재 확인 불필요
                            # 점수는 이미 정렬되어 있으므로 이진 탐색으로 최소 점수 이상인 개수 찾기
                            target_score = int(q[4])
                            idx = bisect_left(scores, target_score)
                            count += len(scores) - idx
                          
        answer.append(count)
    return answer

"""
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)

    # 1) 모든 정보에 대해 16가지 키 생성
    for row in info:
        lang, pos, exp, food, score = row.split()
        score = int(score)
        attrs = [lang, pos, exp, food]
        for mask in range(16):  # 0~15, 4비트 마스크
            key_parts = []
            for i in range(4):
                key_parts.append('-' if (mask & (1 << i)) else attrs[i])
            db[' '.join(key_parts)].append(score)

    # 2) 각 키의 점수 리스트 정렬
    for key in db:
        db[key].sort()

    # 3) 쿼리 처리: 단일 키 조회 + 이진탐색
    answer = []
    for q in query:
        q = q.replace(' and ', ' ')
        parts = q.split()
        key = ' '.join(parts[:4])
        target = int(parts[4])

        arr = db.get(key, [])
        idx = bisect_left(arr, target)
        answer.append(len(arr) - idx)
    return answer
"""
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])