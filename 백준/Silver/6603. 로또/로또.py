def combinations(index, level):
    global choose, arr, k
    
    if level == 6:
        for u in choose:
            print(u, end=' ')
        print()
        return
    
    for i in range(index, k):
        choose.append(arr[i])
        combinations(i+1, level+1)
        choose.pop()
        
while True:
    choose = []
    I = list(map(int, input().split()))
    
    k = I[0]
    arr = I[1:]
    if k == 0:
        break
    combinations(0,0)
    print()