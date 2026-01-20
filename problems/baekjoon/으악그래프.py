"""
2026.01.20
link: https://www.acmicpc.net/problem/35112

고민을 많이 했는데 알고보니 너무 간단한 문제였다.. 
정점과 간선 개수가 동일할때까진 으악 그래프가 되는데, 
간선이 더 많아지면 으악 그래프가 안 되는 것 같아서 시도해보니 맞았다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

if N < M:
    print("No")
else:
    print("Yes")

