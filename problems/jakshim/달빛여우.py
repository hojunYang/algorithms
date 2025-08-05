import heapq

def solution():
    n, m = map(int, input().split())
    graph = [GraphNode(_) for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].add_neighbor(b, c)
        graph[b].add_neighbor(a, c)
    
    fox_dist = dijkstra(graph, 1)
    wolf_dist = dijkstra_wolf_fixed(graph, 1)
    answer = 0
    for i in range(1, n+1):
        if fox_dist[i] < wolf_dist[i]:
            answer += 1
    print(answer)

# 그래프용 노드 구현 (연결 리스트 방식)
class GraphNode:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []  # 인접한 노드들의 리스트
    
    def add_neighbor(self, neighbor, weight=1):
        self.neighbors.append((neighbor, weight))

def dijkstra(graph, start):
        dist = [float('inf')] * (len(graph))
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            current_dist, current_node = heapq.heappop(heap)
            if current_dist > dist[current_node]:
                continue
            
            for neighbor, weight in graph[current_node].neighbors:
                if dist[neighbor] > dist[current_node] + weight:
                    dist[neighbor] = dist[current_node] + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        return dist

def dijkstra_wolf_fixed(graph, start):
    n = len(graph)
    # dist[node][state] : state 0=일반, 1=가속
    dist = [[float('inf')] * 2 for _ in range(n)]
    dist[start][0] = 0  # 시작은 일반 상태
    
    # (거리, 노드, 상태) : 상태 0=일반, 1=가속
    heap = [(0, start, 0)]
    
    while heap:
        current_dist, current_node, state = heapq.heappop(heap)
        
        # 이미 더 좋은 경로로 방문됨
        if current_dist > dist[current_node][state]:
            continue
            
        for neighbor, weight in graph[current_node].neighbors:
            # 늑대: 가속과 감속을 번갈아 사용
            if state == 0:  # 현재 일반 → 다음 가속
                new_cost = current_dist + (weight / 2)
                new_state = 1
            else:  # 현재 가속 → 다음 일반 (감속)
                new_cost = current_dist + (weight * 2)
                new_state = 0
            
            # 더 좋은 경로 발견시 업데이트
            if new_cost < dist[neighbor][new_state]:
                dist[neighbor][new_state] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, new_state))
    
    # 각 노드에 대해 일반/가속 상태 중 최솟값 반환
    result = []
    for i in range(n):
        result.append(min(dist[i][0], dist[i][1]))
    return result

if __name__ == "__main__":
    solution()