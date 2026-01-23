"""
2026.01.23
link: https://www.acmicpc.net/problem/1915
이젠 좀 쉬운 문제였다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

square = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for i in range(n):
    square[i] = list(map(int, input().strip()))

max_size = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and square[i][j] == 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = square[i][j]
        if dp[i][j] > max_size:
            max_size = dp[i][j] 
print(max_size * max_size)
