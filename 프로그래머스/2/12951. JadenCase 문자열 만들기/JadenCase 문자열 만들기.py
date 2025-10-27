def solution(s):
    answer = ''
    capitalize_next = True
    
    for ch in s:
        if ch == " ":
            answer += ch
            capitalize_next = True
        else:
            if capitalize_next:
                answer += ch.upper()
            else:
                answer += ch.lower()
            capitalize_next = False
    
             
    
    return answer