def solution(n):
    answer = []
    
        
    while True:
        ans = n % 10
        answer.append(ans)
        if n // 10 == 0:
            break
        else:
            n = n // 10
    
    return answer