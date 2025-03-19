def cal(diffs, times, level):
    time_prev = [0] + times
    time_cur = times
    return sum((max(0, diffs[i] - level)) * (time_cur[i] + time_prev[i]) + time_cur[i] for i in range(len(diffs)))

def solution(diffs, times, limit):
    # 이진 탐색을 위한 범위 설정
    left = 1
    right = max(diffs)  # 가능한 최대 레벨
    
    while left <= right:
        mid = (left + right) // 2
        result = cal(diffs, times, mid)
        
        if result > limit:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

# def solution(diffs, times, limit):
#     time_prev = [0] + times
#     time_cur = times
#     bottom = sum(time_cur[i] + time_prev[i] for i in range(len(time_cur)))
#     top = sum(diffs[i] * (time_cur[i] + time_prev[i]) + time_cur[i] for i in range(len(diffs)))
#     return max(1, math.ceil((top - limit)/bottom))


# print("Test case 1:", solution([1, 5, 3], [2, 4, 7], 30)) # 3
# print("Test case 2:", solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
# print("Test case 3:", solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))
# print("Test case 3:", solution([1, 1], [1, 2], 100))


def proove(diffs, times, level):
    time_prev = [0] + times
    time_cur = times
    
    left = sum(diffs[i] * (time_cur[i] + time_prev[i]) for i in range(len(diffs)))
    right = sum(level * (time_cur[i] + time_prev[i]) for i in range(len(diffs)))
    constant = sum(time_cur[i] for i in range(len(times)))
    return left - right + constant


print(proove([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 207))