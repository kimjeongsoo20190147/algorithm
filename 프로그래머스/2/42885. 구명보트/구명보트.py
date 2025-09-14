from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    dq = deque(people)
    
    while dq:
        answer += 1
        
        heaviest = dq.pop()
        
        if dq and dq[0] + heaviest <= limit:
            dq.popleft()
    
    return answer