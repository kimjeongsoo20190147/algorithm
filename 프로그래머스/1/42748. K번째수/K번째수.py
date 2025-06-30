def solution(array, commands):
    answer = []
    
    for elem in commands:
        i = elem[0]
        j = elem[1]
        k = elem[2]

        target = array[i-1:j]
        target = sorted(target)

        
        ans = target[k-1]
        answer.append(ans)
    
    return answer