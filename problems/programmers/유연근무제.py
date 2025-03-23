def add_10minutes(time):
    hours = time // 100
    minutes = time % 100 + 10
    hours += minutes // 60
    minutes = minutes % 60
    return hours * 100 + minutes

def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for i, x in enumerate(timelogs):
        day = startday  
        for y in x:
            if day == 6:
                day += 1
                continue
            elif day == 7:
                day = 1
                continue
            if (add_10minutes(schedules[i])) < y:
                answer -= 1
                break
            day += 1
    return answer

schedules = [700, 800, 1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5

print(solution(schedules, timelogs, startday)) # =3