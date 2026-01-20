"""
2026.01.20
link: https://www.acmicpc.net/problem/2293

동전을 먼저 반복할 건지, 가치의 합부터 구할 건지 선택하는 것이 중요한 문제.
가치의 합부터 구하면 순서에 따라 같은 구성도 경우의 수에 포함되고,
동전을 먼저 반복하면 같은 구성은 제외할 수 있다.
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_array = []
dp = [ 0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    n_array.append(int(input()))

for x in n_array:
    for i in range(x, k+1):
        dp[i] += dp[i - x]

print(dp[k])