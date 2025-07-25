from collections import deque

INF = int(1e12)

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

q = deque()
time = [[INF] * M for _ in range(N)]

# 시작점 큐에 append 해주기
for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            q.append((y,x))
            time[y][x] = 0
            
            
while q:
    y, x = q.popleft()
    
    nxts = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
    for ny, nx in nxts:
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if time[ny][nx] <= time[y][x] + 1:
            continue
        if matrix[ny][nx] == -1:
            continue
            
        q.append((ny,nx))
        time[ny][nx] = time[y][x] + 1
        
        
ans = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] != -1:
            ans = max(ans, time[y][x])
            
print(ans if ans != INF else -1)