from collections import deque

def solution(priorities, location):
    
    q = deque(priorities)
    count = 0
    
    count_list = [0] * len(priorities)
    
    while q:
        elem = q.popleft()
        
        # 지금 꺼낸 프로세스가 location에 해당하는지 표시
        is_target = (location == 0)
        
        # 큐에서 하나 꺼냈으니 location도 한 칸 앞으로 당겨짐
        location -= 1
        
        if any(elem < x for x in q):
            q.append(elem)
            
            if is_target:
                location = len(q) - 1
        else:
            count += 1
            
            if is_target:
                count_list[0] = count
                return count
    
    return count_list[0]