def solution(phone_number):
    answer = ''
    
    hidden_length = len(phone_number) - 4
    
    answer = '*' * hidden_length + phone_number[-4:]
    
    return answer