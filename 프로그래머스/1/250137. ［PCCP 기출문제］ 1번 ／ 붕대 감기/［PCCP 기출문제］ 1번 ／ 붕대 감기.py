def solution(bandage, health, attacks):
    t,x,y = bandage[0], bandage[1], bandage[2]
    max_health = health
    last_attack_time = attacks[-1][0]
    
    #attacks 배열을 쉽게 처리하기 위해 큐처럼 사용할 수 있도록 변환
    attacks_dict = {attack[0]: attack[1] for attack in attacks}
    
    current_health = max_health
    last_time = 0
    success_streak = 0
    
    for time in range(1, last_attack_time + 1):
        # 현재 시간에 공격이 있는지 확인
        if time in attacks_dict:
            success_streak = 0
            current_health -= attacks_dict[time]
            
            if current_health <= 0:
                return -1
        
            last_time = time
            
        else:
            current_health += x
            success_streak += 1
            
            # 연속 성공 보너스 확인
            if success_streak == t:
                current_health += y
                success_streak = 0
        
            if current_health > max_health:
                current_health = max_health
                
                
    
    
    return current_health