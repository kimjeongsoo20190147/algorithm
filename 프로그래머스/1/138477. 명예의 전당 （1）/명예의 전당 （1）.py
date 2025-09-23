def solution(k, score):
    answer = []
    leader_board = []
    
    for i in range(len(score)):
        if len(leader_board) < k:
            leader_board.append(score[i])
            answer.append(min(leader_board))
        else:
            if score[i] < min(leader_board):
                answer.append(min(leader_board))
            else:
                leader_board.remove(min(leader_board))
                leader_board.append(score[i])
                answer.append(min(leader_board))
    
    return answer