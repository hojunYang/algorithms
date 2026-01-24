"""
2026.01.24
link: https://www.acmicpc.net/problem/16909

어떤 식으로 풀지 감은 왔는데,
    count_max = max_left[i] * max_right[i]
    count_min = min_left[i] * min_right[i]
    result += card_list[i] * (count_max - count_min)
이걸 떠올리긴 어려웠을 것 같다.
LLM의 도움을 받아 처리했다..
"""

import sys
input = sys.stdin.readline


n = int(input())
card_list = list(map(int, input().split()))

# first try
# result = 0
# for i in range(n):
#     for j in range(i, n):
#         if i == j:
#             continue
#         result += max(card_list[i:j+1]) - min(card_list[i:j+1])

# print(result)

result = 0

max_left = [0] * n
max_right = [0] * n

stack = []
for i in range(n):
    while stack and card_list[stack[-1]] < card_list[i]:
        stack.pop()
    max_left[i] = i - stack[-1] if stack else i + 1
    stack.append(i)

stack = []
for i in range(n-1, -1, -1):
    while stack and card_list[stack[-1]] <= card_list[i]:
        stack.pop()
    max_right[i] = stack[-1] - i if stack else n - i
    stack.append(i)

min_left = [0] * n
min_right = [0] * n

stack = []
for i in range(n):
    while stack and card_list[stack[-1]] > card_list[i]:
        stack.pop()
    min_left[i] = i - stack[-1] if stack else i + 1
    stack.append(i)

stack = []
for i in range(n-1, -1, -1):
    while stack and card_list[stack[-1]] >= card_list[i]:
        stack.pop()
    min_right[i] = stack[-1] - i if stack else n - i
    stack.append(i)

for i in range(n):
    count_max = max_left[i] * max_right[i]
    count_min = min_left[i] * min_right[i]
    result += card_list[i] * (count_max - count_min)

print(result)