def solution(n):
    answer = 0
    
    n_ones_count = bin(n).count('1')
    
    next_num = n + 1
    
    while True:
        next_num_ones_count = bin(next_num).count("1")
        if n_ones_count == next_num_ones_count:
            answer = next_num
            return answer
        
        next_num += 1
    
    return answer