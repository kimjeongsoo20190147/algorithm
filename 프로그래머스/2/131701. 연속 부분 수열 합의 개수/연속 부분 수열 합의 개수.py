def solution(elements):
    l = len(elements)
    sum_set = set()
    
    for i in range(l):
        v = elements[i]
        sum_set.add(v)
        
        for j in range(i+1, i+l):
            v += elements[j%l]
            sum_set.add(v)
    return len(sum_set)