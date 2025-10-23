from collections import deque

def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    queue = deque()
    
    for elem in score:
        queue.append(elem)
    
    while queue:
        if len(queue) < m:
            break
        else:
            temp = []
            for i in range(m):
                temp.append(queue[i])
            answer += min(temp) * m
            for i in range(m):
                queue.popleft()
    
    return answer