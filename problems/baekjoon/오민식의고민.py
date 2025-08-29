"""
아이디어 제출만 하고 코드는 GPT가 작성함
"""
def solution():
    n, start, end, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((a, b, cost))

    earn_money = list(map(int, input().split()))
    
    """
    벨만-포드 알고리즘 (Bellman-Ford Algorithm):
    - 단일 시작점에서 모든 다른 정점까지의 최단/최장 경로를 구하는 알고리즘
    - 음수 가중치가 있는 그래프에서도 동작 가능
    - 음수 순환(negative cycle) 감지 가능
    - 시간복잡도: O(V*E) (V: 정점 수, E: 간선 수)
    
    이 문제에서는 최대 이익을 구하므로 최장 경로를 찾는 변형된 벨만-포드를 사용
    """
    
    # 벨만-포드 알고리즘으로 최대 경로 찾기
    # dist[i]: 시작점에서 i번째 도시까지 가는 최대 이익
    dist = [-float('inf')] * n
    dist[start] = earn_money[start]  # 시작 도시에서 벌 수 있는 돈으로 초기화
    
    # n-1번 반복하여 최대 경로 계산
    # 벨만-포드의 핵심: 최대 n-1번의 간선 완화(relaxation)로 최적해 구함
    for _ in range(n - 1):
        updated = False
        for a, b, cost in edges:
            if dist[a] != -float('inf'):  # a 도시에 도달 가능한 경우
                # 새로운 경로의 이익 = 현재까지 이익 - 교통비 + 목적지에서 벌 수 있는 돈
                new_dist = dist[a] - cost + earn_money[b]
                if new_dist > dist[b]:  # 더 큰 이익을 얻을 수 있다면 업데이트
                    dist[b] = new_dist
                    updated = True
        if not updated:  # 더 이상 업데이트가 없으면 조기 종료 (최적화)
            break    # 양의 순환 감지 및 전파
    # 양의 순환: 순환을 돌 때마다 이익이 증가하는 경우 (무한히 돈을 벌 수 있음)
    reachable_from_positive_cycle = [False] * n
    
    # 양의 순환이 있는 노드들을 찾고 전파
    # n번 더 반복하여 양의 순환 감지 및 영향받는 모든 노드 표시
    for _ in range(n):
        for a, b, cost in edges:
            if dist[a] != -float('inf'):
                new_dist = dist[a] - cost + earn_money[b]
                if new_dist > dist[b]:  # n-1번 후에도 업데이트된다면 양의 순환 존재
                    dist[b] = new_dist
                    reachable_from_positive_cycle[b] = True
            # 양의 순환에 도달 가능한 노드에서 갈 수 있는 모든 노드도 표시
            # 양의 순환의 영향이 전파되는 모든 경로를 추적
            if reachable_from_positive_cycle[a]:
                reachable_from_positive_cycle[b] = True
    
    # 결과 출력
    if dist[end] == -float('inf'):
        print("gg")  # 목적지에 도달할 수 없는 경우
    elif reachable_from_positive_cycle[end]:
        print("Gee")  # 양의 순환으로 인해 무한히 돈을 벌 수 있는 경우
    else:
        print(dist[end])  # 목적지에서 얻을 수 있는 최대 이익
    

solution()
"""
input
5 0 4 7
0 1 13
1 2 17
2 4 20
0 3 22
1 3 4747
2 0 10
3 4 10
0 0 0 0 0
"""