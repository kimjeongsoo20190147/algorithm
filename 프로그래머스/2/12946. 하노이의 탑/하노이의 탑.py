def solution(n):
    answer = []
    
    def hanoi(k,start,mid,end):
        if k == 1:
            answer.append([start, end])
            return
        
        hanoi(k-1, start, end, mid)
        answer.append([start, end])
        hanoi(k-1, mid, start, end)
        
    hanoi(n,1,2,3)
    return answer