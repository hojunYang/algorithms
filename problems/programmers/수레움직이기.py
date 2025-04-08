def solution(maze):
    rows, cols = len(maze), len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)

    red_visited = set()
    blue_visited = set()

    red_visited.add(red_start)
    blue_visited.add(blue_start)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    min_moves = 17

    def dfs(red_pos, blue_pos, moves, red_visited, blue_visited):
        nonlocal min_moves
        red_x, red_y = red_pos
        blue_x, blue_y = blue_pos

        if maze[red_x][red_y] == 3 and maze[blue_x][blue_y] == 4:
            min_moves = min(min_moves, moves)
            return
        
        if moves >= min_moves:
            return
        
        # 빨간 수레가 이미 도착한 경우
        if maze[red_x][red_y] == 3:
            for blue_dx, blue_dy in directions:
                new_blue_x, new_blue_y = blue_x + blue_dx, blue_y + blue_dy
                if 0 <= new_blue_x < rows and 0 <= new_blue_y < cols and maze[new_blue_x][new_blue_y] != 5 \
                    and (new_blue_x, new_blue_y) not in blue_visited \
                    and (new_blue_x, new_blue_y) != (red_x, red_y):
                    blue_visited.add((new_blue_x, new_blue_y))
                    dfs((red_x, red_y), (new_blue_x, new_blue_y), moves + 1, red_visited, blue_visited) 
                    blue_visited.remove((new_blue_x, new_blue_y))
        
        # 파란 수레가 이미 도착한 경우
        elif maze[blue_x][blue_y] == 4:
            for red_dx, red_dy in directions:
                new_red_x, new_red_y = red_x + red_dx, red_y + red_dy
                if 0 <= new_red_x < rows and 0 <= new_red_y < cols and maze[new_red_x][new_red_y] != 5 \
                    and (new_red_x, new_red_y) not in red_visited \
                    and (new_red_x, new_red_y) != (blue_x, blue_y):
                    red_visited.add((new_red_x, new_red_y))
                    dfs((new_red_x, new_red_y), (blue_x, blue_y), moves + 1, red_visited, blue_visited)
                    red_visited.remove((new_red_x, new_red_y))
        
        # 두 수레 모두 이동해야 하는 경우
        else:
            for red_dx, red_dy in directions:
                new_red_x, new_red_y = red_x + red_dx, red_y + red_dy
                if 0 <= new_red_x < rows and 0 <= new_red_y < cols and maze[new_red_x][new_red_y] != 5 \
                    and (new_red_x, new_red_y) not in red_visited:

                    for blue_dx, blue_dy in directions:
                        new_blue_x, new_blue_y = blue_x + blue_dx, blue_y + blue_dy
                        if 0 <= new_blue_x < rows and 0 <= new_blue_y < cols and maze[new_blue_x][new_blue_y] != 5 \
                            and (new_blue_x, new_blue_y) not in blue_visited:

                            if (not (new_red_x == blue_x and new_red_y == blue_y and new_blue_x == red_x and new_blue_y == red_y)) and \
                                (new_blue_x, new_blue_y) != (new_red_x, new_red_y):
                                red_visited.add((new_red_x, new_red_y))
                                blue_visited.add((new_blue_x, new_blue_y))
                                dfs((new_red_x, new_red_y), (new_blue_x, new_blue_y), moves + 1, red_visited, blue_visited)
                                red_visited.remove((new_red_x, new_red_y))
                                blue_visited.remove((new_blue_x, new_blue_y))

    dfs(red_start, blue_start, 0, red_visited, blue_visited)
    return min_moves if min_moves != 17 else 0


# 핵심 테스트 케이스
maze = [
  [1, 0, 5, 2],
  [0, 3, 0, 0],
  [0, 4, 5, 0],
  [0, 0, 0, 0],
]