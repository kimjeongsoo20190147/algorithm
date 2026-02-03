def solution(clothes):
    clothes_dict = {}
    
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
            
    
    
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)
    
    return answer - 1