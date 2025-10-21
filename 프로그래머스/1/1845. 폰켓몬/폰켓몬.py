def solution(nums):
    answer = 0
    
    n = len(nums)
    kinds = len(set(nums))
    answer = min(kinds, n//2)
    
    return answer