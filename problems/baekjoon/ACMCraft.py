import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
"""
백준풀이시 위의 세팅을 꼭 해야함!!
"""
def solution():
    games = int(input())
    answer = []
    dp = []
    visited = []
    def dfs(start):
        visited[start] = True
        for next in edges[start]:
            if not visited[next]:
                dp[next] = dfs(next)
            dp[start] = max(dp[start], dp[next])

        dp[start] += times[start]
        return dp[start]

    for _ in range(games):
        n, k = map(int, input().split())
        times = list(map(int, input().split()))
        edges = [[] for _ in range(n)]
        for _ in range(k):
            a, b = map(int, input().split())
            edges[b-1].append(a-1)
        goal = int(input())

        dp = [0] * n
        visited = [False] * n

        answer.append(dfs(goal-1))
    for a in answer:
        print(a)

solution()

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque
def solution():
    games = int(input())
    answer = []
    def dp(goal):
        # 각 건물까지의 최소 시간을 저장하는 배열
        dp_arr = [0] * n
        
        # 위상정렬을 위한 진입차수 계산
        indegree = [0] * n
        for i in range(n):
            for next_node in edges[i]:
                indegree[next_node] += 1
        
        # 진입차수가 0인 노드들을 큐에 추가
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                dp_arr[i] = times[i]
                queue.append(i)
        
        # 위상정렬과 동시에 DP 수행
        while queue:
            now = queue.popleft()
            
            for next_node in edges[now]:
                # 현재 노드를 거쳐서 다음 노드로 가는 시간 계산
                dp_arr[next_node] = max(dp_arr[next_node], dp_arr[now] + times[next_node])
                indegree[next_node] -= 1
                
                # 진입차수가 0이 되면 큐에 추가
                if indegree[next_node] == 0:
                    queue.append(next_node)
        
        return dp_arr[goal]

    for _ in range(games):
        n, k = map(int, input().split())
        times = list(map(int, input().split()))
        edges = [[] for _ in range(n)]
        for _ in range(k):
            a, b = map(int, input().split())
            edges[a-1].append(b-1)
        goal = int(input())

        answer.append(dp(goal-1))
    for a in answer:
        print(a)

solution()
"""