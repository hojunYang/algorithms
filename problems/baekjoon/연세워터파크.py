"""
2026.01.22
link: https://www.acmicpc.net/problem/15678
DP를 deque로 최대값 관리하는 것을~ 잊지 말라구~
"""
import sys
from collections import deque
input = sys.stdin.readline

n, d = map(int, input().split())
stones = list(map(int, input().split()))
dp = [0] * n
queue = deque()

dp[0] = stones[0]
queue.append(0)

for i in range(1, n):
    while queue and queue[0] < i - d:
        queue.popleft()
    dp[i] = max(dp[queue[0]], 0) + stones[i]
    while queue and dp[queue[-1]] <= dp[i]:
        queue.pop()
    queue.append(i)
    
print(max(dp))