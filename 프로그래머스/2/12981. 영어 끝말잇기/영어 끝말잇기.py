def solution(n, words):
    answer = [0,0]
    
    used = set()
    
    used.add(words[0])
    
    for i in range(1, len(words)):
        prev, curr = words[i-1], words[i]
        
        if prev[-1] != curr[0]:
            return [i % n + 1, i // n + 1]
        
        if curr in used:
            return [i % n + 1, i // n + 1]

        used.add(curr)


    return answer