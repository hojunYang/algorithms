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
"""
훨씬 빠른 식..
def fork(storage, box):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    index = []

    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if storage[ni][nj] == "0":
                        index.append((i, j))
                        break

    for i, j in index:
        storage[i][j] = "0"
        spread_outside(storage, i, j)

def crane(storage, box):
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                storage[i][j] = "1"
                spread_outside(storage, i, j)

def spread_outside(storage, x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    if any(storage[x + dx[k]][y + dy[k]] == "0" for k in range(4)):
        storage[x][y] = "0"
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if storage[nx][ny] == "1":
                spread_outside(storage, nx, ny)

def solution(storage, requests):
    answer = 0
    storage = [list("0" + row + "0") for row in storage]
    storage.insert(0, list("0" * len(storage[0])))
    storage.append(list("0" * len(storage[0])))

    for req in requests:
        if len(req) == 1:
            fork(storage, req)
        else:
            crane(storage, req[0])

    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1

    return answer
"""
if __name__ == '__main__':
    print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"],["C", "B", "B", "B", "B", "H"])) 
    print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"],["A", "BB", "A"]))