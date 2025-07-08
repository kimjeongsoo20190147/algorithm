from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for elem in permutations(dungeons):
        remain = k
        count = 0
        for need, cost in elem:
            if need <= remain:
                remain -= cost
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer