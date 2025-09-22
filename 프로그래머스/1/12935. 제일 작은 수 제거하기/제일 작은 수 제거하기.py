def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    min_ = min(arr)
    
    arr.remove(min_)
    
    return arr