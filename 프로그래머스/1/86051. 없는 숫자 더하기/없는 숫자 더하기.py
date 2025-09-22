def solution(numbers):
    answer = 0
    #numbers.sort()
    
    for i in range(0, 10, 1):
        if i in numbers:
            continue
        else:
            answer += i
    
    return answer