def solution(N, stages):
    answer = []
    
    stages.sort()
    people = len(stages)
    fail_list = []
    
    for i in range(1, N+1):
        i_stage = stages.count(i)
        
        if people != 0 and i_stage != 0:
            fail = float(i_stage / people)
            fail_list.append(fail)
            people -= i_stage
    
        else:
            fail_list.append(0)
    
    
    while True:
        if len(answer) == N:
            break
        
        max_index = fail_list.index(max(fail_list))
        answer.append(max_index+1)
        fail_list[max_index] = -1
    
    return answer