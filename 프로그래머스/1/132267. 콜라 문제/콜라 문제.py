def solution(a, b, n):
    answer = 0
    while n >= a:
        new_cola = (n//a) * b
        answer += new_cola
        
        n = (n % a) + new_cola
    
    return answer