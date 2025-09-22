def solution(s):
    answer = False
    
    len_s = len(s)
    
    if len_s == 4 or len_s == 6:
        if s.isdigit():
            return True
    
    return answer