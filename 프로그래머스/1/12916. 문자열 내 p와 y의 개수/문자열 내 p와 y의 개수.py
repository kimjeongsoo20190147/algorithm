def solution(s):
    answer = True
    
    s_lower = s.lower()
    
    p_count = s_lower.count('p')
    y_count = s_lower.count('y')
    
    if p_count != y_count:
        return False

    return True