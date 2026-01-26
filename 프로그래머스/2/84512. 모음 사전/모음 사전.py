from itertools import product

def solution(word):
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    dictionary = []
    
    for length in range(1,6):
        for combination in product(vowels, repeat=length):
            dictionary.append(''.join(combination))
                              
    dictionary.sort()
    
    return dictionary.index(word) + 1