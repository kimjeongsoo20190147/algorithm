def solution(s, n):
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '
            continue
            
        ascii_code = ord(char)
        
        new_ascii = ascii_code + n
        
        if 'a' <= char <= 'z':
            if new_ascii > ord('z'):
                new_ascii -= 26
        elif 'A' <= char <= 'Z':
            if new_ascii > ord('Z'):
                new_ascii -= 26
                    
        answer += chr(new_ascii)            
            
    
    return answer