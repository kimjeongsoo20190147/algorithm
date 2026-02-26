def solution(arr, divisor):
    answer = []
    
    for elem in arr:
        if elem % divisor == 0:
            answer.append(elem)
    
    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    return answer