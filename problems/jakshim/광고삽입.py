def solution(play_time, adv_time, logs):
    pt = convert_time_string_to_number(play_time)
    at = convert_time_string_to_number(adv_time)

    # 광고 길이가 0이거나 전체 재생시간 이상인 경우 시작 시각이 최적
    if at == 0 or at >= pt:
        return "00:00:00"
    
    # 차분 배열
    timeline = [0] * (pt + 2)
    for log in logs:
        s, e = log.split('-')
        s = convert_time_string_to_number(s)
        e = convert_time_string_to_number(e)
        timeline[s] += 1
        timeline[e] -= 1

    for i in range(1, pt + 1):
        timeline[i] += timeline[i - 1]
    print(timeline)
    
    adv_index = convert_time_string_to_number(adv_time)
    current_sum = sum(timeline[:adv_index])
    max_result = current_sum
    answer = 0
    
    for i in range(1, len(timeline) - adv_index + 1):
        # 이전 윈도우의 첫 번째 값을 빼고, 새로운 값을 더함
        current_sum = current_sum - timeline[i-1] + timeline[i+adv_index-1]
        if current_sum > max_result:
            max_result = current_sum
            answer = i
    
    # answer을 시간 형식으로 변환
    hour = answer // 3600
    minute = (answer % 3600) // 60
    second = answer % 60
    return f"{hour:02d}:{minute:02d}:{second:02d}"

def convert_time_string_to_number(time: str) -> int:
    hour, minute, second = map(int, time.split(':'))
    return hour * 60 * 60 + minute * 60 + second

if __name__ == '__main__':
    print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))