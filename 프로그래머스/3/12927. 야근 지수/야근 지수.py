import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        largest = heapq.heappop(heap)
        largest += 1
        heapq.heappush(heap, largest)
        
    answer = 0
    for w in heap:
        answer += w * w
    
    
    return answer