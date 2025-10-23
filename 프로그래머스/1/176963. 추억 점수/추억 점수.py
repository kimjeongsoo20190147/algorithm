def solution(name, yearning, photo):
    answer = []
    
    yearning_dic = {}
    
    for n, y in zip(name, yearning):
        yearning_dic[n] = y

    for people in photo:
        s = 0
        for p in people:
            s += yearning_dic.get(p,0)
        answer.append(s)
    
    
    return answer