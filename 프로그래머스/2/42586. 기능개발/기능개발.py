def solution(progresses, speeds):
    answer = []
    days_needed = []
    
    for p, s in zip(progresses, speeds):
        remain_progress = 100 - p
        days = (remain_progress + s - 1) // s
        days_needed.append(days)
        
    if not days_needed:
        return []
    
    count = 0
    max_day = days_needed[0]
    
    for days in days_needed:
        if days <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days
            
    answer.append(count)
    
    return answer