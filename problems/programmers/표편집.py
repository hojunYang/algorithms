def solution(n, k, cmd):
    # 연결 리스트 형태로 이전/다음 노드 정보 저장
    prev_node = list(range(-1, n-1))  # 이전 노드 인덱스
    next_node = list(range(1, n+1))   # 다음 노드 인덱스
    
    # 삭제된 행의 정보를 저장할 스택
    deleted_stack = []
    
    # 현재 커서 위치
    current = k
    
    for command in cmd:
        if command[0] == 'U':
            # 위로 이동
            steps = int(command[2:])
            for _ in range(steps):
                current = prev_node[current]
                    
        elif command[0] == 'D':
            # 아래로 이동
            steps = int(command[2:])
            for _ in range(steps):
                current = next_node[current]
                    
        elif command[0] == 'C':
            # 현재 행 삭제
            deleted_stack.append((current, prev_node[current], next_node[current]))
            
            # 연결 리스트에서 현재 노드 제거
            prev_pos = prev_node[current]
            next_pos = next_node[current]
            
            if prev_pos != -1:
                next_node[prev_pos] = next_pos
            if next_pos != n:
                prev_node[next_pos] = prev_pos
            
            # 삭제 후 커서 이동
            if next_pos != n:
                current = next_pos
            else:
                current = prev_pos
            print(next_node, prev_node)
        elif command[0] == 'Z':
            # 가장 최근에 삭제된 행 복구
            restored_row, prev_pos, next_pos = deleted_stack.pop()
            
            # 연결 리스트에 노드 복구
            if prev_pos != -1:
                next_node[prev_pos] = restored_row
            if next_pos != n:
                prev_node[next_pos] = restored_row
            
            print(next_node, prev_node)
            
    # 결과 문자열 생성
    result = ['O'] * n
    for deleted_row, _, _ in deleted_stack:
        result[deleted_row] = 'X'
    
    return ''.join(result)

print(solution(2, 0, ["C", "C", "Z", "Z"]))


