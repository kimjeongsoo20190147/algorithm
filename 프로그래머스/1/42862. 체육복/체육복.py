def solution(n, lost, reserve):
    answer = 0
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    sorted_lost = sorted(list(set_lost))
    reserve_list = list(set_reserve)
    
    answer = n - len(sorted_lost)
    
    for i in sorted_lost:
        if (i-1) in reserve_list:
            answer += 1
            reserve_list.remove(i-1)
            
        elif (i+1) in reserve_list:
            answer += 1
            reserve_list.remove(i+1)
    
    return answer