def solution(phone_book):
    answer = True
    
    hash_map = {num: True for num in phone_book}
    
    
    for num in phone_book:
        prefix = ""
        for ch in num[:-1]:
            prefix += ch
            if prefix in hash_map:
                return False
    
    return answer