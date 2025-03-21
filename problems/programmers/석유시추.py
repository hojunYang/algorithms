from collections import deque

# claude 3.7 sonnet의 도움을 받음
def solution(land):
    rows, cols = len(land), len(land[0])
    oil_fields = {}  # 석유 덩어리 ID와 크기를 저장
    field_id = 2  # 0과 1을 피하기 위해 2부터 시작
    
    # BFS를 사용하여 석유 덩어리 식별
    def bfs(r, c, field_id):
        queue = deque([(r, c)])
        size = 0
        land[r][c] = field_id
        
        while queue:
            x, y = queue.popleft()
            size += 1
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and land[nx][ny] == 1:
                    land[nx][ny] = field_id
                    queue.append((nx, ny))
        
        return size
    
    # 모든 석유 덩어리 찾기
    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 1:
                oil_fields[field_id] = bfs(i, j, field_id)
                field_id += 1
    
    # 각 열에서 뽑을 수 있는 석유량 계산
    col_oil = [0] * cols
    for j in range(cols):
        visited_fields = set()
        for i in range(rows):
            field = land[i][j]
            if field >= 2 and field not in visited_fields:
                visited_fields.add(field)
                col_oil[j] += oil_fields[field]
    
    return max(col_oil) if col_oil else 0