def solution(babbling):
    answer = 0
    
    syllables = ["aya", "ye", "woo", "ma"]
    
    for w in babbling:
        i = 0
        prev = ""
        ok = True
        
        while i < len(w):
            matched = False
            for s in syllables:
                if w.startswith(s, i) and s != prev:
                    i += len(s)
                    prev = s
                    matched = True
                    break
                    
            if not matched:
                ok = False
                break
                
        if ok:
            answer += 1
    
    return answer