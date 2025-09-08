"""
2025.09.08
문제
초라기는 각각 W명으로 구성된 특수소대를 다수 출동시켜 모든 구역에 침투시킬 예정이며, 각 구역 별로 적이 몇 명씩 배치되어 있는지는 초라기가 모두 알고 있다. 특수소대를 아래 조건에 따라 침투 시킬 수 있다.

한 특수소대는 침투한 구역 외에, 인접한 한 구역 더 침투할 수 있다. (같은 경계를 공유하고 있으면 인접 하다고 한다. 위 그림에서 1구역은 2, 8, 9 구역과 서로 인접한 상태다.) 즉, 한 특수소대는 한 개 혹은 두 개의 구역을 커버할 수 있다.
특수소대끼리는 아군인지 적인지 구분을 못 하기 때문에, 각 구역은 하나의 소대로만 커버해야 한다.
한 특수소대가 커버하는 구역의 적들의 합은 특수소대원 수 W 보다 작거나 같아야 한다.
이때 초라기는 원타곤의 모든 구역을 커버하기 위해 침투 시켜야 할 특수 소대의 최소 개수를 알고 싶어 한다.

풀이
DP를 통해서 많은 케이스에 대해 처리할 수 있다.
state = 0: 현재 열의 두 칸 모두 이전에 처리됨
state = 1: 현재 열의 위쪽만 이전에 처리됨  
state = 2: 현재 열의 아래쪽만 이전에 처리됨
state = 3: 현재 열의 두 칸 모두 이전에 처리되지 않음

예제
1
8 100
70 60 55 43 57 60 44 50
58 40 47 90 45 52 80 40
==> 11

1
5 10
3 2 8 3 8
5 2 8 3 5
==> 6
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution():
    def solve_dp(first_state):
        dp = [[INF] * 4 for _ in range(N + 1)]

        if first_state == 0:  # 첫 번째 열 두 칸 모두 처리됨
            dp[0][0] = 2
        elif first_state == 1:  # 첫 번째 열 위쪽만 처리됨
            dp[0][1] = 1
        elif first_state == 2:  # 첫 번째 열 아래쪽만 처리됨
            dp[0][2] = 1
        elif first_state == 3:  # 첫 번째 열 두 칸 모두 처리되지 않음
            dp[0][3] = 0
        
        for i in range(0, N):
            ni = i+1
            adj_ni = ni % N

            for state in range(4):
                if dp[i][state] == INF:
                    continue

                if state == 3:
                    if enemy[0][i] + enemy[1][i] <= W:
                        dp[ni][3] = min(dp[ni][3], dp[i][state] + 1)
                    if enemy[0][i] + enemy[0][adj_ni] <= W:
                        dp[ni][1] = min(dp[ni][1], dp[i][state] + 2)
                    if enemy[1][i] + enemy[1][adj_ni] <= W:
                        dp[ni][2] = min(dp[ni][2], dp[i][state] + 2)
                    if enemy[0][i] + enemy[0][adj_ni] <= W and enemy[1][i] + enemy[1][adj_ni] <= W:
                        dp[ni][0] = min(dp[ni][0], dp[i][state] + 2)
                    dp[ni][3] = min(dp[ni][3], dp[i][state] + 2)
                elif state == 1:
                    if enemy[1][i] + enemy[1][adj_ni] <= W:
                        dp[ni][2] = min(dp[ni][2], dp[i][state] + 1)
                    else:
                        dp[ni][3] = min(dp[ni][3], dp[i][state] + 1)
                elif state == 2:
                    if enemy[0][i] + enemy[0][adj_ni] <= W:
                        dp[ni][1] = min(dp[ni][1], dp[i][state] + 1)
                    else:
                        dp[ni][3] = min(dp[ni][3], dp[i][state] + 1)
                elif state == 0:
                    dp[ni][3] = min(dp[ni][3], dp[i][state])
        # print(dp)
        if first_state == 0:
            dp[N][0] = dp[N][0] -2
        elif first_state == 1:
            dp[N][1] = dp[N][1] -1
        elif first_state == 2:
            dp[N][2] = dp[N][2] -1
        return min(dp[N])

    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        enemy = [list(map(int, input().split())), 
                list(map(int, input().split()))]
        
        # DP 테이블: dp[i][mask] = i번째 열의 mask 상태에서 최소 소대 수
        INF = float('inf')

        result = float('inf')
        
        # 맨 마지막과 상관이 없는 경우 (first_state = 0)
        result = min(result, solve_dp(0))
        
        # 맨 마지막의 윗줄과 연결되는 경우 (first_state = 1)
        result = min(result, solve_dp(1))
        
        # 맨 마지막의 아래줄과 연결되는 경우 (first_state = 2)
        result = min(result, solve_dp(2))
        
        # 맨 마지막과 모두 연결되는 경우 (first_state = 3)
        result = min(result, solve_dp(3))
        
        print(result)
solution()


"""
Claude 4 Sonnet에게 코드 리팩토링을 시킴
기가 막히게 깔끔하게 만들었다..
리팩토링 하나는 참 잘한다.. 리참잘~

# 상태 상수 정의
class State:
    BOTH_COVERED = 0    # 두 칸 모두 처리됨
    TOP_COVERED = 1     # 위쪽만 처리됨
    BOTTOM_COVERED = 2  # 아래쪽만 처리됨
    NONE_COVERED = 3    # 두 칸 모두 처리되지 않음

def solution():
    def initialize_dp(columns, initial_state):
        #DP 테이블을 초기화하고 초기 상태를 설정합니다.#
        INF = float('inf')
        dp = [[INF] * 4 for _ in range(columns + 1)]
        
        initial_costs = {
            State.BOTH_COVERED: 2,
            State.TOP_COVERED: 1,
            State.BOTTOM_COVERED: 1,
            State.NONE_COVERED: 0
        }
        
        dp[0][initial_state] = initial_costs[initial_state]
        return dp, INF
    
    def can_cover_vertical(enemy_grid, column, squad_capacity):
        #세로로 두 칸을 한 소대로 커버할 수 있는지 확인합니다.#
        return enemy_grid[0][column] + enemy_grid[1][column] <= squad_capacity
    
    def can_cover_horizontal(enemy_grid, row, col1, col2, squad_capacity):
        #가로로 두 칸을 한 소대로 커버할 수 있는지 확인합니다.#
        return enemy_grid[row][col1] + enemy_grid[row][col2] <= squad_capacity
    
    def update_dp_state(dp, current_col, next_col, current_state, next_state, cost):
        #DP 상태를 업데이트합니다.#
        dp[next_col][next_state] = min(dp[next_col][next_state], dp[current_col][current_state] + cost)
    
    def process_none_covered_state(dp, enemy_grid, current_col, next_col, squad_capacity, INF):
        #현재 열이 모두 처리되지 않은 상태를 처리합니다.#
        if dp[current_col][State.NONE_COVERED] == INF:
            return
            
        next_col_index = next_col % len(enemy_grid[0])
        
        # 현재 열을 세로로 한 소대로 처리
        if can_cover_vertical(enemy_grid, current_col, squad_capacity):
            update_dp_state(dp, current_col, next_col, State.NONE_COVERED, State.NONE_COVERED, 1)
        
        # 현재 열 위쪽과 다음 열 위쪽을 한 소대로 처리
        if can_cover_horizontal(enemy_grid, 0, current_col, next_col_index, squad_capacity):
            update_dp_state(dp, current_col, next_col, State.NONE_COVERED, State.TOP_COVERED, 2)
        
        # 현재 열 아래쪽과 다음 열 아래쪽을 한 소대로 처리
        if can_cover_horizontal(enemy_grid, 1, current_col, next_col_index, squad_capacity):
            update_dp_state(dp, current_col, next_col, State.NONE_COVERED, State.BOTTOM_COVERED, 2)
        
        # 두 가로 소대로 처리
        can_cover_top = can_cover_horizontal(enemy_grid, 0, current_col, next_col_index, squad_capacity)
        can_cover_bottom = can_cover_horizontal(enemy_grid, 1, current_col, next_col_index, squad_capacity)
        
        if can_cover_top and can_cover_bottom:
            update_dp_state(dp, current_col, next_col, State.NONE_COVERED, State.BOTH_COVERED, 2)
        
        # 각각 별도 소대로 처리
        update_dp_state(dp, current_col, next_col, State.NONE_COVERED, State.NONE_COVERED, 2)
    
    def process_partial_covered_state(dp, enemy_grid, current_col, next_col, squad_capacity, INF):
        #현재 열이 부분적으로 처리된 상태를 처리합니다.#
        next_col_index = next_col % len(enemy_grid[0])
        
        # 위쪽만 처리된 경우
        if dp[current_col][State.TOP_COVERED] != INF:
            if can_cover_horizontal(enemy_grid, 1, current_col, next_col_index, squad_capacity):
                update_dp_state(dp, current_col, next_col, State.TOP_COVERED, State.BOTTOM_COVERED, 1)
            else:
                update_dp_state(dp, current_col, next_col, State.TOP_COVERED, State.NONE_COVERED, 1)
        
        # 아래쪽만 처리된 경우
        if dp[current_col][State.BOTTOM_COVERED] != INF:
            if can_cover_horizontal(enemy_grid, 0, current_col, next_col_index, squad_capacity):
                update_dp_state(dp, current_col, next_col, State.BOTTOM_COVERED, State.TOP_COVERED, 1)
            else:
                update_dp_state(dp, current_col, next_col, State.BOTTOM_COVERED, State.NONE_COVERED, 1)
    
    def process_both_covered_state(dp, current_col, next_col, INF):
        #현재 열이 모두 처리된 상태를 처리합니다.#
        if dp[current_col][State.BOTH_COVERED] != INF:
            update_dp_state(dp, current_col, next_col, State.BOTH_COVERED, State.NONE_COVERED, 0)
    
    def solve_with_initial_state(enemy_grid, squad_capacity, columns, initial_state):
        #주어진 초기 상태로 DP를 수행합니다.#
        dp, INF = initialize_dp(columns, initial_state)
        
        for col in range(columns):
            next_col = col + 1
            
            # 각 상태별 처리
            process_none_covered_state(dp, enemy_grid, col, next_col, squad_capacity, INF)
            process_partial_covered_state(dp, enemy_grid, col, next_col, squad_capacity, INF)
            process_both_covered_state(dp, col, next_col, INF)
        
        # 초기 상태에 따른 조정
        adjustment = {
            State.BOTH_COVERED: -2,
            State.TOP_COVERED: -1,
            State.BOTTOM_COVERED: -1,
            State.NONE_COVERED: 0
        }
        
        final_states = dp[columns].copy()
        if initial_state in adjustment:
            final_states[initial_state] += adjustment[initial_state]
        
        return min(final_states)
    
    # 메인 로직
    test_cases = int(input())
    
    for _ in range(test_cases):
        columns, squad_capacity = map(int, input().split())
        enemy_grid = [
            list(map(int, input().split())),
            list(map(int, input().split()))
        ]
        
        # 모든 가능한 초기 상태에 대해 최솟값 계산
        min_squads = float('inf')
        for initial_state in range(4):
            squads_needed = solve_with_initial_state(enemy_grid, squad_capacity, columns, initial_state)
            min_squads = min(min_squads, squads_needed)
        
        print(min_squads)

solution()
"""