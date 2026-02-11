"""
2026.02.11
link: https://www.acmicpc.net/problem/31265
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chapters = list(map(int, input().split()))
times = [[] for _ in range(n)]
for i in range(n):
    times[i] = list(map(int, input().split()))

prev_dp = 0
mask = (1 << m) - 1
for i in range(n):
    next_dp = 0
    for j in range(chapters[i]):
        if i == 0:
            now_dp = ((prev_dp << times[i][j]) | (1 << (times[i][j] - 1))) & mask
        else:
            now_dp = (prev_dp << times[i][j]) & mask
        next_dp |= now_dp
        prev_dp |= now_dp
    prev_dp = next_dp

for i in range(m, -1, -1):
    if prev_dp & (1 << i):
        print(i + 1)
        break
else:
    print(-1)