import copy

direction = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def solution():
    tank = []
    for _ in range(4):
        a, b, c, d, e, f, g, h = map(int, input().split())
        tank.append([[a, b], [c, d], [e, f], [g, h]])

    shark_pos = (0, 0)
    shark_eat = tank[0][0][0]
    shark_direction = tank[0][0][1]
    tank[0][0] = [0, 0]  # 상어가 있는 위치 표시

    max_eat = dfs(tank, shark_pos, shark_eat, shark_direction)
    print(max_eat)

def dfs(tank, shark_pos, shark_eat, shark_direction):
    # 물고기 이동
    tank = fish_move(tank, shark_pos)
    
    max_result = shark_eat
    
    # 상어가 이동할 수 있는 모든 위치 확인
    for i in range(1, 4):
        next_row = shark_pos[0] + direction[shark_direction][0] * i
        next_col = shark_pos[1] + direction[shark_direction][1] * i
        
        # 범위를 벗어나면 중단
        if not (0 <= next_row < 4 and 0 <= next_col < 4):
            break
            
        # 물고기가 있는 위치로만 이동 가능
        if tank[next_row][next_col][0] != 0:
            # 현재 상태 복사
            new_tank = copy.deepcopy(tank)
            new_shark_pos = (next_row, next_col)
            new_shark_eat = shark_eat + new_tank[next_row][next_col][0]
            new_shark_direction = new_tank[next_row][next_col][1]
            
            # 원래 상어 위치를 빈 공간으로 만들고, 새 위치에 상어 표시
            new_tank[shark_pos[0]][shark_pos[1]] = [0, 0]
            new_tank[next_row][next_col] = [0, 0]
            
            # 재귀 호출
            result = dfs(new_tank, new_shark_pos, new_shark_eat, new_shark_direction)
            max_result = max(max_result, result)
    
    return max_result

def fish_move(tank, shark_pos):
    for fish_num in range(1, 17):
        found = False
        for row in range(4):
            for col in range(4):
                if tank[row][col][0] == fish_num:
                    found = True
                    # 물고기가 이동할 수 있는 방향을 찾을 때까지 반복
                    for _ in range(8):
                        fish_direction = tank[row][col][1]
                        next_row = row + direction[fish_direction][0]
                        next_col = col + direction[fish_direction][1]
                        
                        # 이동 가능한 조건: 범위 내 + 상어가 없는 위치
                        if (0 <= next_row < 4 and 0 <= next_col < 4 and 
                            (next_row, next_col) != shark_pos):
                            # 위치 교환
                            tank[row][col], tank[next_row][next_col] = tank[next_row][next_col], tank[row][col]
                            break
                        else:
                            # 방향을 시계방향으로 45도 회전
                            tank[row][col][1] = fish_direction % 8 + 1
                    break
            if found:
                break
    return tank


solution()