def solution(keymap, targets):
    answer = []
    
    min_map = {}
    
    for key_string in keymap:
        for i, char in enumerate(key_string):               
            press_count = i + 1
        
            if char not in min_map or press_count < min_map[char]:
                min_map[char] = press_count
                
    for target_string in targets:
        total_presses = 0
        is_possible = True
        
        for char in target_string:
            if char not in min_map:
                is_possible = False
                break
            else:
                total_presses += min_map[char]
                
        if is_possible:
            answer.append(total_presses)
        else:
            answer.append(-1)
    
    return answer