def solution(numbers):
    
    numList = list(map(str, numbers))
    
    numList.sort(key=lambda x:x*3, reverse=True)
    
    answer = ''.join(numList)
    
    if numList[0] == "0":
        return "0"
    
    return answer