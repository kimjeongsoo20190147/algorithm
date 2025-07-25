import sys
sys.setrecursionlimit(int(1e6))

def dfs(y,x,h):
    global dy, dx, N, matrix, visited
    
    if not (0 <= y < N and 0 <= x < N):
        return
    if visited[y][x] or matrix[y][x] <= h:
        return
    visited[y][x] = True
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        dfs(ny, nx, h)
        
        
def get_num(height):
    global dy, dx, N, matrix, visited
    
    visited = [[False] * N for _ in range(N)]
    
    num = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                dfs(y, x, height)
                num += 1
                
    return num


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for height in range(101):
    ans = max(ans, get_num(height))
    
print(ans)