from collections import deque

N, M = map(int, input().split())
    
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
        
        
def BFS(x,y):
    # dy, dx 테크닉 사용(상하좌우 방향으로 이동하도록)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((x,y))
        
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 격자를 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 1이 아닌 0이면 가지 못하도록
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                    
    return graph[N-1][M-1]
    
                    
print(BFS(0,0))