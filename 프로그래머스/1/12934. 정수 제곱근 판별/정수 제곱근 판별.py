import math

def solution(n):
    x = math.sqrt(n)
    
    if x == int(x):
        return (int(x) + 1) ** 2
    else:
        return -1
