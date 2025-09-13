from itertools import permutations
import math


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    all_numbers = set()
    
    num_list = list(numbers)
    
    for i in range(1, len(num_list)+1):
        perms = permutations(num_list, i)
        
        for p in perms:
            num = int("".join(p))
            all_numbers.add(num)
            
            
    for num in all_numbers:
        if is_prime(num):
            answer += 1
            
    return answer
    
    
    return answer