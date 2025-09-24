def solution(n, m, section):
    answer = 0
    filled = [1] * n
    
    for i in range(len(section)):
        k = section[i]
        filled[k-1] = 0

    for i in range(n):
        if filled[i] == 0:
            answer += 1
            for j in range(m):
                if i+j < n:
                    filled[i+j] = 1
    
    
    return answer