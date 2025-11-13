def solution(participant, completion):
    answer = ''
    
    hash = {}
    
    for people in participant:
        if people in hash:
            hash[people] += 1
        else:
            hash[people] = 1
        
    for people in completion:
        hash[people] += 1
        
    for people in hash:
        if hash[people] % 2 == 1:
            answer = answer + people

    
    return answer