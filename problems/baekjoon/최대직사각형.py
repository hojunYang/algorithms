"""
2026.01.23
link: https://www.acmicpc.net/problem/11873
아직 벽이 좀 느껴지는 문제였다.
"""

import sys
input = sys.stdin.readline
# first try 시간 초과
# def test(r, c):
#     max_size = 0
#     max_row = n
#     max_col = m

#     for row in range(r, n):
#         if square[row][c] == 0:
#             break
#         width = 0
#         for col in range(c, max_col):
#             if square[row][col] == 1:
#                 width +=1
#             else:
#                 break
#         max_col = min(max_col, c + width)
#         max_row = row + 1  # 직사각형은 r~row포함
#         max_size = max(max_size, (max_row - r) * (max_col - c))
#     return max_size

# second try
def test():
    height = [0] * m
    max_size = 0

    for i in range(n):
        for j in range(m):
            if square[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0

        stack = []
        extend = height + [0]
        for index, h in enumerate(extend):
            while stack and extend[stack[-1]] > h:
                row = stack.pop()
                left = stack[-1] if stack else -1
                size = (index - left - 1) * extend[row]
                max_size = max(max_size, size)
            stack.append(index)
    return max_size


while True: 
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        break
    square = [[0] * m for _ in range(n)]
    for i in range(n):
        square[i] = list(map(int, input().split()))

    max_size = test()
    print(max_size)