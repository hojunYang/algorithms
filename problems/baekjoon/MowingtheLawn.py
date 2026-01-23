"""
2026.01.22
link: https://www.acmicpc.net/problem/5977
아직 벽이 좀 느껴지는 문제였다.
2차원 dp론 쉽게 풀었는데,
O(NK) -> O(N)으로 처리하기 쉽지 않았다.
모노톤 덱으로 바꾸는 법을 몰라 LLM에 물어봤다.
"""
# O(NK), O(NK)
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
cows = []
for _ in range(n):
    cows.append(int(input()))
dp = [[0] * k for _ in range(n)]
queue = deque()

for i in range(n):
    dp[i][0] = cows[i]
    for j in range(1, k):
        dp[i][j] = max(dp[i - 1][j - 1], 0) + cows[i]

for i in range(n):
    dp[i][k-1] = max(dp[i-k-1][k-1] if i-k-1 >= 0 else 0, 0) + dp[i][k-1]

print(max(list(zip(*dp))[1]))

# O(N), O(N)
# prefix = [0] * (n + 2)
# for i in range(n):
#     prefix[i + 1] = prefix[i] + cows[i]
# dp = [0] * (n + 2)
# dq = deque()

# dq.append((-1, 0 - prefix[0]))

# for i in range(n + 1):
#     while dq and dq[0][0] < i - k - 1:
#         dq.popleft()
#     dp[i] = prefix[i] + dq[0][1]

#     val = dp[i] - prefix[i + 1]
#     while dq and dq[-1][1] <= val:
#         dq.pop()
#     dq.append((i, val))

# print(dp[n])
