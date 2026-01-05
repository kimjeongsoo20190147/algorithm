def solution(s, skip, index):
    answer = ''
    skip_list = []
    
    for char in skip:
        skip_list.append(ord(char))
    
    
    for char in s:
        char = ord(char)
        for i in range(index):
            char += 1
            if char == 123:
                char = 97

            while char in skip_list:
                char += 1
                if char == 123:
                    char = 97

        
        answer = answer + chr(char)


    return answer