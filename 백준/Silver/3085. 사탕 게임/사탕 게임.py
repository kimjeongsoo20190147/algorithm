def get_best():
    global N, matrix
    best = 0
    # 모든 열 탐색
    for i in range(N):
        bef = 'Z'
        value = 0
        for j in range(N):
            if bef == matrix[i][j]:
                value += 1
            else:
                value = 1
            bef = matrix[i][j]
            best = max(best, value)
            
    # 모든 행 탐색
    for j in range(N):
        bef = 'Z'
        value = 0
        for i in range(N):
            if bef == matrix[i][j]:
                value += 1
            else:
                value = 1
            bef = matrix[i][j]
            best = max(best, value)
            
    return best


dy = [-1,0,1,0]
dx = [0,1,0,-1]

N = int(input())
matrix = [list(input()) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[y][x] != matrix[ny][nx]:
                    matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                    ans = max(ans, get_best())
                    matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                    
                    
                    
print(ans)