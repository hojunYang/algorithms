from itertools import zip_longest

def get_path(start, end):
    path = []
    
    # 수평 이동
    x_step = 1 if start[0] < end[0] else -1
    if start[0] != end[0]:
        path.extend((x, start[1]) for x in range(start[0], end[0], x_step))
    
    # 수직 이동
    y_step = 1 if start[1] < end[1] else -1
    if start[1] != end[1]:
        path.extend((end[0], y) for y in range(start[1], end[1], y_step))
    
    return path

def solution(points, routes):
    answer = 0
    
    points = [[0,0]] + points 
    coordinates = []
    for route in routes:
        temp = []
        for i in range(1, len(route)):
            temp.extend(get_path(points[route[i-1]], points[route[i]]))
            
        temp.append((points[route[-1]][0], points[route[-1]][1]))
        coordinates.append(temp)
    
    # 각 경로의 좌표들을 시간별로 묶어서 처리
    for positions in zip_longest(*coordinates):
        # None을 제외한 현재 시간의 모든 좌표
        current_positions = [pos for pos in positions if pos is not None]
        if not current_positions:
            break
            
        # 중복된 좌표 개수를 답에 추가
        answer += len([pos for pos in set(current_positions) 
                      if current_positions.count(pos) > 1])
    
    return answer

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))