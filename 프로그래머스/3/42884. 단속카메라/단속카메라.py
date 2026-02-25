def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])

    cam_pos = -30001
    
    for start, end in routes:
        if cam_pos < start:
            answer += 1
            cam_pos = end
    
    return answer