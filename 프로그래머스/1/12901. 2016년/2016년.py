def solution(a, b):
    answer = ''
    
    days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    total_days = sum(days_in_month[:a-1]) + (b-1)
    
    answer = days[total_days % 7]
    
    return answer