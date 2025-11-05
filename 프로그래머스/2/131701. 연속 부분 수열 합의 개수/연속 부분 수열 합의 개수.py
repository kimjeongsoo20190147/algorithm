def solution(elements):
    answer = []
    circle = elements * 2
    
    for i, num in enumerate(elements):
        answer.append(num)
        
        for num2 in circle[i+1:i+len(elements)]:
            num += num2
            answer.append(num)
    
    
    return len(set(answer))