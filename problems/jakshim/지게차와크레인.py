from collections import deque
import copy

def solution(storage, requests):
    # BFS를 사용하여 석유 덩어리 식별
    def bfs(r, c, storage):
        queue = deque([(r, c)])
        visited = set([(r, c)])
        
        while queue:
            x, y = queue.popleft()
            
            # 경계에 도달했는지 확인
            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                return True
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                
                # 범위 체크 및 방문 체크
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if storage[nx][ny] == 1:  # 빈 공간에 도달
                        return True
                    elif storage[nx][ny] == 2:  # 같은 종류의 블록
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return False
    
    def crane_pop(store, req):
        if store == req:
            return 2
        else:
            return store
    
    for i in range(len(storage)):
        storage[i] = list(storage[i])
    rows, cols = len(storage), len(storage[0])

    for req in requests:
        if len(req) == 2:
            storage = [list(map(lambda x: crane_pop(x, req[0]), row)) for row in storage]
        temp = copy.deepcopy(storage)
        for row in range(rows):
            for col in range(cols):
                if storage[row][col] == req:
                    if bfs(row, col, storage):
                        temp[row][col] = 1
        storage = temp
        
    return sum(1 for row in storage for cell in row if cell != 1 and cell != 2)

if __name__ == '__main__':
    print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"],["C", "B", "B", "B", "B", "H"])) 
    print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"],["A", "BB", "A"]))