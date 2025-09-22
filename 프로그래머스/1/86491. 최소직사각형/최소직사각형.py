def solution(sizes):
    answer = 0
    
    sort_sizes = [sorted(size) for size in sizes]
    
    max_w = max(size[0] for size in sort_sizes)
    max_h = max(size[1] for size in sort_sizes)
    
    answer = max_w * max_h
    
    return answer