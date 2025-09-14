def solution(s):
    answer = []
    
    transform_count = 0
    removed_zeros = 0
    
    while s != "1":
        transform_count += 1
        
        num_zeros = s.count('0')
        removed_zeros += num_zeros
        
        c = len(s) - num_zeros
        
        s = bin(c)[2:]
        
    answer.append(transform_count)
    answer.append(removed_zeros)
    
    return answer