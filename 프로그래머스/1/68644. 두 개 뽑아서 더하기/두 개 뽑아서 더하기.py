from itertools import combinations

def solution(numbers):
    answer = []
    answer_set = set()
    
    for i in combinations(numbers, 2):
        sum_ = sum(i)
        answer_set.add(sum_)
    
    
    for elem in answer_set:
        answer.append(elem)
    
    answer.sort()
    
    return answer