import heapq
def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)].sort()
    
    heap = []
    for deadline, reward in arr:
        heapq.heappush(heap, reward)
        if len(heap) > deadline:
            heapq.heappop(heap)
    return sum(heap)

if __name__ == "__main__":
    print(solution())

