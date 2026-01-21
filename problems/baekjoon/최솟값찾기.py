"""
2026.01.21
link: https://www.acmicpc.net/problem/11003
"""
import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
numbers = list(map(int, input().split()))
result = [0] * n
queue = deque()

for i in range(n):
    while queue and queue[0] < i - l + 1:
        queue.popleft()
    while queue and numbers[queue[-1]] > numbers[i]:
        queue.pop()
    queue.append(i)
    result[i] = numbers[queue[0]]

print(" ".join(map(str, result)))