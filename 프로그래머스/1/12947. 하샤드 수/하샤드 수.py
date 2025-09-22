def solution(x):
    answer = True
    
    x_sum = sum(int(digit) for digit in str(x))
           
    if x % x_sum != 0:
        answer = False
        
    
    return answer