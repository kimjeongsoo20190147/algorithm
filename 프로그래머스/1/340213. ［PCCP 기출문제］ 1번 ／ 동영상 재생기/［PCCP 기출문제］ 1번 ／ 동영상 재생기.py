def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    new_pos = int(pos[0:2]) * 60 + int(pos[3:5])
    new_op_start = int(op_start[0:2]) * 60 + int(op_start[3:5])
    new_op_end = int(op_end[0:2]) * 60 + int(op_end[3:5])
    new_video_len = int(video_len[0:2]) * 60 + int(video_len[3:5])
    
    for elem in commands:
        if new_op_start <= new_pos <= new_op_end:
            new_pos = new_op_end

        if elem == 'next':
            new_pos += 10
        elif elem == 'prev':
            new_pos -= 10


        if new_pos < 0:
            new_pos = 0
        if new_pos > new_video_len:
            new_pos = new_video_len

        if new_op_start <= new_pos <= new_op_end:
            new_pos = new_op_end
    
    minute = str(new_pos//60)
    second = str(new_pos%60)
    
    if len(minute) == 1:
        minute = '0' + minute

    if len(second) == 1:
        second = '0' + second
        
    answer = minute + ':' + second
    
    return answer