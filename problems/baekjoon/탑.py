"""
2026.01.21
link: https://www.acmicpc.net/problem/2493
하 구린 코드 짜다가 AI에게 힌트를 얻었습니다.
"""
import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
result = [0] * n
mono_stack = []

for i in range(n):
    while mono_stack and tops[mono_stack[-1]] < tops[i]:
        mono_stack.pop()
    if mono_stack:
        result[i] = mono_stack[-1] + 1
        mono_stack.append(i)
    else:
        result[i] = 0
        mono_stack.append(i)

print(" ".join(map(str, result)))