def solution(s):
    answer = []
    last_pos = {}
    
    for i, char in enumerate(s):
        if char not in last_pos:
            answer.append(-1)
        else:
            dis = i - last_pos[char]
            answer.append(dis)
            
        last_pos[char] = i
        
    
    return answer