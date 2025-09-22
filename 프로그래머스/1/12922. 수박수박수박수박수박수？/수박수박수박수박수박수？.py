def solution(n):
    answer = ''
    
    for i in range(1,n+1):
        if i % 2 == 1:
            answer = answer + '수'
        else:
            answer = answer + '박'
    
    return answer