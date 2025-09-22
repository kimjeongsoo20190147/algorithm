def solution(s):
    answer = ''
    
    sorted_s = sorted(s, reverse=True)
    
    answer = "".join(sorted_s)
    
    return answer