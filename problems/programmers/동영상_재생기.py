# "mm:ss" to seconds
def mmss_to_seconds(mmss):
    m, s = map(int, mmss.split(':'))
    return m * 60 + s


# seconds to "mm:ss"
def seconds_to_mmss(seconds):
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"


def solution(video_len, pos, op_start, op_end, commands):
    video_len_seconds = mmss_to_seconds(video_len)
    pos_seconds = mmss_to_seconds(pos)
    op_start_seconds = mmss_to_seconds(op_start)
    op_end_seconds = mmss_to_seconds(op_end)

    if pos_seconds >= op_start_seconds and pos_seconds < op_end_seconds:
        pos_seconds = op_end_seconds
    
    # commands 처리
    while commands:
        command = commands.pop(0)

        if command == 'next':
            if pos_seconds + 10 >= video_len_seconds:
                pos_seconds = video_len_seconds
            else:
                pos_seconds += 10
        elif command == 'prev':
            if pos_seconds - 10 <= 0:
                pos_seconds = 0
            else:
                pos_seconds -= 10
        if pos_seconds >= op_start_seconds and pos_seconds < op_end_seconds:
            pos_seconds = op_end_seconds

    return seconds_to_mmss(pos_seconds)
