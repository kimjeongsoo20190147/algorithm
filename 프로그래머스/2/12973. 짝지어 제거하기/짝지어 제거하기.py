def solution(s):
    answer = -1

    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        answer = 1
    else:
        answer = 0
            
    return answer