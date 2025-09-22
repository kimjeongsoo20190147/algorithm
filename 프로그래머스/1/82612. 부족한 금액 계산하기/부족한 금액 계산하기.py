def solution(price, money, count):
    answer = 0
    
    total_cost = 0
    
    for i in range(1, count+1):
        total_cost += price * i
    
    if money > total_cost:
        return 0
    else:
        answer = abs(money - total_cost)

    return answer