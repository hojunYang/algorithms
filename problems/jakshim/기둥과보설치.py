def solution(n, build_frame):
    frame = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    def check_install_pillar(x, y):
        """기둥 설치 가능성 검사"""
        
        # 바닥이면 설치 가능
        if y == n:
            return True
        
        # 아래에 기둥이 있거나, 현재 위치에 보가 있거나, 왼쪽에 보가 있으면 설치 가능
        if (0 in frame[y+1][x]) or (1 in frame[y][x]) or (x > 0 and 1 in frame[y][x-1]):
            return True
        
        return False
    
    def check_install_beam(x, y):
        """보 설치 가능성 검사"""
        
        # 한쪽 끝이 기둥 위에 있거나, 양쪽 끝이 다른 보와 연결되어 있으면 설치 가능
        left_pillar = 0 in frame[y+1][x]
        right_pillar = x < n and 0 in frame[y+1][x+1]
        left_beam = x > 0 and 1 in frame[y][x-1]
        right_beam = x < n-1 and 1 in frame[y][x+1]
        if left_pillar or right_pillar or (left_beam and right_beam):
            return True
        
        return False
    
    def check_delete_pillar(x, y):
        """기둥 제거 가능성 검사"""
        
        if 0 in frame[y][x]:
            # 기둥 임시 제거
            frame[y][x].remove(0)
        else:
            return True
        stable = True
        check_positions = []
        
        # 영향받는 구조물들 찾기
        # 제거된 기둥 위의 기둥
        if y > 0 and 0 in frame[y-1][x]:
            check_positions.append((x, y-1, 0))
        
        # 제거된 기둥에서 시작하는 보
        if y > 0 and 1 in frame[y-1][x]:
            check_positions.append((x, y-1, 1))
        
        # 제거된 기둥에서 끝나는 보
        if y > 0 and x > 0 and 1 in frame[y-1][x-1]:
            check_positions.append((x-1, y-1, 1))
        
        # 영향받는 구조물들의 안정성 검사
        for pos_x, pos_y, element in check_positions:
            if element == 0:  # 기둥
                if not check_install_pillar(pos_x, pos_y):
                    stable = False
                    break
            else:  # 보
                if not check_install_beam(pos_x, pos_y):
                    stable = False
                    break
        
        # 불안정하면 기둥 복원
        if not stable:
            frame[y][x].append(0)
            return False
        
        return True
    
    def check_delete_beam(x, y):
        """보 제거 가능성 검사"""
        
        # 보 임시 제거
        if 1 in frame[y][x]:
            frame[y][x].remove(1)
        else:
            return True
        stable = True
        check_positions = []
        
        # 영향받는 구조물들 찾기
        # 제거된 보의 양 끝점 기둥
        if 0 in frame[y][x]:
            check_positions.append((x, y, 0))
        if x < n and 0 in frame[y][x+1]:
            check_positions.append((x+1, y, 0))
        
        # 제거된 보와 연결된 인접 보들
        if x > 0 and 1 in frame[y][x-1]:
            check_positions.append((x-1, y, 1))
        if x < n-1 and 1 in frame[y][x+1]:
            check_positions.append((x+1, y, 1))
        
        # 영향받는 구조물들의 안정성 검사
        for pos_x, pos_y, element in check_positions:
            if element == 0:  # 기둥
                if not check_install_pillar(pos_x, pos_y):
                    stable = False
                    break
            else:  # 보
                if not check_install_beam(pos_x, pos_y):
                    stable = False
                    break
        
        # 불안정하면 보 복원
        if not stable:
            frame[y][x].append(1)
            return False
        
        return True

    # 실제 처리
    for x, y, element, install_yn in build_frame:
        adj_y = n - y  # 좌표 변환
        
        if install_yn == 1:  # 설치
            if element == 0 and not 0 in frame[adj_y][x]:  # 기둥
                if check_install_pillar(x, adj_y):
                    frame[adj_y][x].append(0)
            elif element == 1 and not 1 in frame[adj_y][x]:  # 보
                if check_install_beam(x, adj_y):
                    frame[adj_y][x].append(1)
        
        elif install_yn == 0:  # 제거
            if element == 0:  # 기둥
                check_delete_pillar(x, adj_y)
            elif element == 1:  # 보
                check_delete_beam(x, adj_y)

    
    # 결과 생성
    result = []
    for y in range(n+1):
        for x in range(n+1):
            if frame[n-y][x]:
                for element in sorted(frame[n-y][x]):
                    result.append([x, y, element])
    
    # 결과를 x, y, element 순으로 정렬
    result.sort(key=lambda item: (item[0], item[1], item[2]))
    
    return result

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
"""
이렇게 간단하게 풀 수 있다니..
def is_valid(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            if y == 0 or [x, y - 1, 0] in answer or \
               [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or \
               ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, stuff, operate in build_frame:
        if operate == 1:
            answer.append([x, y, stuff])
            if not is_valid(answer):
                answer.remove([x, y, stuff])
        else:
            answer.remove([x, y, stuff])
            if not is_valid(answer):
                answer.append([x, y, stuff])

    return sorted(answer)
"""