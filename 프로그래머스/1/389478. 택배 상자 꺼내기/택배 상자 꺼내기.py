def solution(n, w, num):
    answer = 0
    

    if n % w == 0:
        rows = n // w
    else:
        rows = (n // w) + 1
        
    cols = w
    lst = [[0 for _ in range(cols)] for _ in range(rows)]
    
    start = 1
    for i in range(rows):
        for j in range(cols):
            if start > n:
                break
            lst[i][j] = start
            start += 1
    

    for i in range(1, rows, 2):
        lst[i].reverse()

    target_row = 0
    target_col = 0
    found = False
    for i in range(rows):
        for j in range(cols):
            if lst[i][j] == num:
                target_row = i
                target_col = j
                found = True
                break
        if found:
            break

    for i in range(target_row, rows):
        if lst[i][target_col] != 0:
            answer += 1
            
    return answer