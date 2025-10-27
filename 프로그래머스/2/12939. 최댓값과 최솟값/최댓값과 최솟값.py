def solution(s):
    answer = ''
    
    numbers = list(map(int, s.split()))
    
    min_num = str(min(numbers))
    max_num = str(max(numbers))
    
    answer = min_num + " " + max_num
    
    return answer