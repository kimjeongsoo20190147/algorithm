def solution(n,a,b):
    answer = 0
    players = list(range(1,n+1))
    
    while True:
        answer += 1
        next_players = []
        
        for i in range(0, len(players), 2):
            p1, p2 = players[i], players[i+1]
            
            if (p1 == a and p2 == b) or (p1 == b and p2 == a):
                return answer
            if p1 == a or p1 == b:
                next_players.append(p1)
            elif p2 == a or p2 == b:
                next_players.append(p2)
            else:
                next_players.append(p1)

        players = next_players

    return answer