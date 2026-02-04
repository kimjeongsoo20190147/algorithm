def is_valid(brackets):
    pair = {')':'(', ']':'[', '}':'{'}
    stack = []
    
    for ch in brackets:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
            
    return not stack


def solution(s):
    n = len(s)
    answer = 0
    
    for x in range(n):
        rotated = s[x:] + s[:x]
        if is_valid(rotated):
            answer += 1
    
    return answer