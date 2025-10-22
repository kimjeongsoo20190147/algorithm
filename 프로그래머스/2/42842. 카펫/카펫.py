def solution(brown, yellow):
    answer = []
    
    # 전체 넓이 계산
    total_area = brown + yellow
    
    for H in range(3, int(total_area**0.5)+1):
        if total_area % H == 0:
            W = total_area // H
            
            if (W-2) * (H-2) == yellow:
                return [W,H]
    
    return answer