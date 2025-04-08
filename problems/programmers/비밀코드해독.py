"""
  포문 5개 중복으로 돌리려고 했는데, 너무 느려서 GPT의 도움을 받았다. sonnet 3.7 굿
  레벨 2는 참 애매한 것 같다.. 어떻게 보면,, 레벨 3보다 어려운,,
  아래는 altdmfk 님의 코드
import itertools 

def solution(n, q, ans):
    f = list(itertools.combinations(range(1, n + 1), 5))

    for g, cnt in zip(q, ans):
         f = [code for code in f if len(set(code) & set(g)) == cnt]

    return len(f)
"""

def solution(n, q, ans):
    answer = 0
    def make_num_set(n):
        from itertools import combinations
        return [set(comb) for comb in combinations(range(1, n+1), 5)]

    def check_set(num_set, q, ans):
        for x in q:
            if len(num_set & set(x)) != ans[q.index(x)]:
                return False
        return True

    num_set_arr = make_num_set(n)
    for num_set in num_set_arr:
        if check_set(num_set, q, ans):
            answer += 1
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))
