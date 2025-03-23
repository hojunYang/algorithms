# cskhw 님 풀이 참고
def get_degree(h, m, s):
    sd = (s * 6) % 360
    md = (m * 6 + s * 0.1) % 360
    hd = (h * 30  + m * 0.5  + s * 0.5 / 60) % 360
    return hd, md, sd

def get_times(h, m, s):
    hd, md, sd = get_degree(h, m, s)

    # 분당 시침과 분침은 초침과 만남 => 60 * h + m 만큼 초침을 만남
    # 1:05:05 2:10:10 3:15:15 4:20:20 5:25:25 6:30:30 7:35:35 8:40:40 9:45:45 10:50:50 11:55:55 12:00:00 -> 초침이 동시에 만남
    # 즉, 시 당 중복을 제거해야함
    times = (60 * h + m) * 2 - h

    # 초침 각도가 시침 이상이면 한 번 만난 것
    if sd >= hd:
        times += 1

    # 초침 각도가 분침 이상이면 한 번 만난 것
    if sd >= md:
        times += 1

    # 11:59:59에서 12:00:00은 분침도 초침도 만나지 않음
    # 즉, 11시 59분에는 시침과 분침이 초침과 만나지 않음
    # h가 12 이상일땐 -2을 해줌
    if h >= 12:
        times -= 2
    
    return times

def solution(h1, m1, s1, h2, m2, s2):
    times1 = get_times(h1, m1, s1)
    times2 = get_times(h2, m2, s2)
    
    return times2 - times1 + 1 if m1 == 0 and s1 == 0 else times2 - times1



# 베스트 수식 풀이 (배형민, 3828 님 풀이)
# 각속도를 통한 계산법
# 초침의 각속도 = 6 도/초
# 분침의 각속도 = 1/10 도/초
# 시침의 각속도 = 1/120 도/초
# 상대각속도 = 초침각속도 - 시침/분침 각속도

# 한번 만나는데 걸리는 시간 = 360 / 상대각속도
# 초침과 분침이 만나는 시간 = 360 / (6 - 1/10)
# 360 / 59/10 = 3600/59 초
# 초침과 시침이 만나는 시간 = 360 / (6 - 1/120) 
# 360 / 719/120 = 43200/719 초

# def solution(h1, m1, s1, h2, m2, s2):
#     answer = 0
#     start = h1*3600+m1*60+s1
#     end   = h2*3600+m2*60+s2

#     answer+=int(end/(3600/59))
#     answer-=int(start//(3600/59))

#     answer+=int(end//(43200/719))
#     answer-=int(start//(43200/719))
#     if start<=12*60*60<=end:answer-=1
#     if start==0 or start==12*60*60:answer+=1

#     return answer



print(solution(0, 5, 30, 0, 7, 0))
print(solution(13, 0, 0, 13, 0, 30)) 
print(solution(0, 6, 1, 0, 6, 6))
print(solution(11, 59, 30, 12, 0, 0)) 
print(solution(11, 58, 59, 11, 59, 0))
print(solution(1, 5, 5, 1, 5, 6))
print(solution(0, 0, 0, 23, 59, 59))