def solution(players, callings):
    
    dic = {player: i for i, player in enumerate(players)}
    
    for i in range(len(callings)):
        called = callings[i]
        chasing_index = dic[called]
        temp = players[chasing_index-1]
        players[chasing_index] = temp
        players[chasing_index-1] = called
        dic[called] = chasing_index - 1
        dic[temp] = chasing_index
        
    
    return players