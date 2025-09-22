def solution(food):
    answer = '0'
    
    for i in range(len(food)-1,0,-1):
        food_count = food[i] // 2
        for j in range(food_count):
            answer = str(i) + answer + str(i) 
    
    return answer