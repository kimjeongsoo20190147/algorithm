def solution(t, p):
    answer = 0
    temp = []
    
    len_p = len(p)

    for i in range(len(t) - len_p + 1):
        substring = t[i : i + len_p]
        temp.append(substring)
        
        
    for elem in temp:
        if elem <= p:
            answer += 1
    
    return answer