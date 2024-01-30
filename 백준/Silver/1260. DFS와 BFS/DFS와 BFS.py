import sys
input = sys.stdin.readline
N, M, V = map(int, input().split())

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
            
            
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
                
#그래프 초기 세팅
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

#1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
    
#2. dfs 실행
dfs(V)
print()

#3. bfs 실행 (앞에서 dfs를 실행 했으므로 visited 배열 초기화 후 진행)
visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()
