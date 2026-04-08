def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    
    mats.sort(reverse=True)
    
    for size in mats:
        for i in range(rows-size+1):
            for j in range(cols-size+1):
                can_place = True
                
                for x in range(i, i+size):
                    for y in range(j, j+size):
                        if park[x][y] != "-1":
                            can_place = False
                    if not can_place:
                        break
                if can_place:
                    return size
    
    return -1