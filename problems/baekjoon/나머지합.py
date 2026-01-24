"""
2026.01.24
link: https://www.acmicpc.net/problem/10986

"""
import sys
from collections import defaultdict
input = sys.stdin.readline


n, m = map(int, input().split())
A = list(map(int, input().split()))
prefix = [0] * n + [0]
result = 0
for i in range(n):
    prefix[i] = prefix[i-1] + A[i]

# for i in range(n):
#     for j in range(i+1):
#         print(i, j, prefix[i] - prefix[j-1])
#         if (prefix[i] - prefix[j-1]) % m == 0:
#             result += 1
count = defaultdict(int)
count[0] = 1
for i in range(n):
    index = prefix[i] % m
    result += count[index]
    count[index] += 1
print(result)