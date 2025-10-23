def solution(s):
    answer = 0
    x = None
    same = diff = 0
    
    for ch in s:
        if x is None:
            x = ch
            same = diff = 0
            
        if ch == x:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            answer += 1
            x = None
            
    if x is not None:
        answer += 1
    
    return answer